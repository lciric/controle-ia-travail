"""Banc d'altérations des essais du lanceur v5 du réajustement (essai des essais) — v1.

= le banc du lanceur v4 (`banc_alterations_lanceur_v4_v1.py`, `615dedf7…`, gardé sans modification) rejoué sur le lanceur v5, le
rangement v2, l'amorce v6 et les essais `tests/test_neuron_lens_b_beta_lancer_v5.py` (les 32 altérations de la v4, mêmes motifs), plus
les altérations des corrections de la contre-lecture (C-1 : attente entre les essais d'un même fichier ; C-2 : relecture sans objet ;
C-3 : libellé de la vérification à l'arrivée), repérées « C-1 », « C-2 », « C-3 ». Le texte du banc v4 suit (noms à lire en v5).

Chaque garde neuve ou changée est faussée, une à la fois, sur une **copie** du code (dossier temporaire : rien du dépôt n'est touché) ;
les essais `tests/test_neuron_lens_b_beta_lancer_v4_v2.py` (hors ceux qui construisent l'arbre réduit ou lisent le programme de
comparaison, `-k "not copie_reelle"`) doivent échouer. Deux témoins : la copie non altérée passe ; chaque motif est trouvé exactement une
fois (sinon l'altération est « motif introuvable », comptée comme un échec du banc).

Usage : `.venv/bin/python docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/banc_alterations_lanceur_v4_v1.py <racine du dépôt>`
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

L4 = "src/controle_ia/neuron_lens/b_beta_lancer_v5.py"  # v5 : nom gardé, lanceur v5
RG = "src/controle_ia/neuron_lens/rangement_lentilles_v2.py"
AM = "scripts/amorce_neuron_lens_b_beta_v6.sh"
ESSAIS = "tests/test_neuron_lens_b_beta_lancer_v5.py"
COPIES = ("src", "tests/conftest.py", ESSAIS, AM, "requirements-neuron-lens-b-beta-v2.txt", "pyproject.toml")

ALTERATIONS = [  # (item, nom, fichier, motif, remplacement)
    ("a", "ligne du 18 admise", L4, "    if go in GO_REFUSES:", "    if False:"),
    ("a", "date antérieure admise", L4, "    if go[3:13] < GO_DATE_MIN:", "    if False:"),
    ("a", "forme du GO non vérifiée", L4, '    if not _GO.match(go or ""):', "    if False:"),
    ("f", "étape de B admise en A", L4, '    elif env.get("VARIANTE") == "A" and etape in ETAPES and etape not in ETAPES_A:', "    elif False:"),
    ("f", "variante A sans arrêt", L4, '        return ETAPES_A if self.variante == "A" else ETAPES', "        return ETAPES"),
    ("f", "variante illisible admise", L4, "        if self.variante not in VARIANTES:\n            raise Arret", "        if False:\n            raise Arret"),
    ("c", "copies sans clé", L4, 'JETON = frozenset({"telecharger-tokeniseur", "telecharger-poids"} | set(COPIES))',
     'JETON = frozenset({"telecharger-tokeniseur", "telecharger-poids"})'),
    ("c", "clôture sans clé", L4, 'COMMANDES_JETON = frozenset({"cloture"})', "COMMANDES_JETON = frozenset()"),
    ("c", "clé aux étapes sans jeton (amorce)", AM, '    [ "$cle" = jeton ] || unset HF_TOKEN\n', ""),
    ("c", "clé retirée après le téléchargement (amorce)", AM, '  unset HUGGING_FACE_HUB_TOKEN  #',
     '  [ -e "$DEPOT/diag/$RUN_ID/b-beta-telecharger-poids.json" ] && unset HF_TOKEN; unset HUGGING_FACE_HUB_TOKEN  #'),
    ("d", "dépôt non nommé admis", L4, "        pb += rg.probleme_depot(env.get(rg.VARIABLE_DEPOT, \"\"))", "        pb += []"),
    ("d", "dépôt public admis", RG, "        if not pb and not transport.prive(depot):", "        if False:"),
    ("d", "fichier changé envoyé", RG, '        if loc != f["sha256"] or t != f["taille"]:', "        if False:"),
    ("d", "empreinte à l'arrivée non comparée", RG, '                if s is not None and s != f["sha256"]:', "                if False:"),
    ("d", "taille à l'arrivée non comparée", RG, '                if not vu or vu.get("taille") != f["taille"]:', "                if not vu:"),
    ("d", "trois reprises", RG, "REPRISES = 2", "REPRISES = 3"),
    ("d", "révision non vérifiée", RG, '                if not _REVISION.match(str(rev or "")):', "                if False:"),
    ("e", "borne d'installation à 3 600 s (amorce)", AM, "TIMEOUT_PIP=${TIMEOUT_PIP_S:-7200}", "TIMEOUT_PIP=${TIMEOUT_PIP_S:-3600}"),
    ("g", "versions relevées autrement", L4, '    out["versions"] = versions()', '    out["versions"] = {}'),
    ("i", "commentaire d'origine remis", L4, "    # (i) v4 : aucun seuil de la course ne lit `diffs_float64` ;",
     "    # pour mémoire, jamais lue pour un seuil ;"),
    ("i", "texte de _split_half_64 touché", L4, '    """La même différence en double précision, couche par couche (mémoire bornée) ; pour mémoire seulement."""',
     '    """La même différence en double précision, couche par couche (mémoire bornée)."""'),
    ("k", "ancre de la lentille publique changée", L4, 'REVISION_NEURONPEDIA = "d2527c3cdbaa60dd4b65cbca1604921f044e989a"',
     'REVISION_NEURONPEDIA = "0000000000000000000000000000000000000000"'),
    ("l", "inventaire sans manifeste écrit", L4, "    if not ctx.manifeste.exists():\n        return None\n    d = ctx.diag",
     "    d = ctx.diag"),
    ("l", "empreinte reprise sans contrôle de date", L4,
     '            h = c["sha256"] if c and c.get("taille") == s.st_size and c.get("mtime_ns") == s.st_mtime_ns else sha256(p)',
     '            h = c["sha256"] if c else sha256(p)'),
    ("l", "clôture qui copie un ajustement inachevé", L4,
     "            if not ctx.resultat(f\"ajustement-{le}\").exists():\n                continue\n            faits",
     "            faits"),
    ("l", "clôture toujours à 0", L4, '    return 3 if json.loads(chemin.read_text(encoding="utf-8"))["non_copies"] else 0', "    return 0"),
    ("l", "copie en échec non signalée (amorce)", AM, '      log "COPIE EN ECHEC : voir', '      log "copie : voir'),
    ("m", "croquis sans vérification du fichier", L4, '            if sha256(f) != ctx.lire(f"ajustement-{le}")["sha256"]:', "            if False:"),
    ("m", "croquis sans borne de temps", L4, "                if au_dela():", "                if False:"),
    ("m", "croquis en simple précision", L4, "                m = sum(st[\"sums\"][(t, h)][l].double() for h in moities) / n",
     "                m = (sum(st[\"sums\"][(t, h)][l].float() for h in moities) / n).double().round(decimals=1)"),
    ("relecture", "relecture toujours égale", RG, '            r["egal"] = r["sha256_lue"] == a["sha256"] and r["taille_lue"] == a["taille"]',
     '            r["egal"] = True'),
    ("relecture", "inventaire non clos admis", RG, '        if inv.get("clos") is not True:', "        if False:"),
    # v5 : corrections de la contre-lecture du lanceur v4
    ("C-1", "reprises en rafale (aucune attente)", RG, "                attendre(pause)\n", ""),
    ("C-1", "attentes nulles", RG, "ATTENTES_S = (60, 300)", "ATTENTES_S = (0, 0)"),
    ("C-1", "même attente avant chaque reprise", RG, '                pause = ATTENTES_S[min(r["essais"], len(ATTENTES_S)) - 1]',
     "                pause = ATTENTES_S[0]"),
    ("C-1", "attente cumulée sans borne", RG, '                if out["attente_totale_s"] + pause > ATTENTE_MAX_APPEL_S:', "                if False:"),
    ("C-1", "borne d'attente à 3 600 s", RG, "ATTENTE_MAX_APPEL_S = 1200", "ATTENTE_MAX_APPEL_S = 3600"),
    ("C-1", "reprise remise comptée comme un essai", RG, '                    r["reprise_remise"] = True\n',
     '                    r["reprise_remise"] = True\n                    r["essais"] += 1\n'),
    ("C-1", "attente absente : rafale au lieu de la vraie", RG, "    attendre = attendre if attendre is not None else _dormir",
     "    attendre = attendre if attendre is not None else (lambda s: None)"),
    ("C-1", "lanceur : copie sans l'attente du contexte", L4,
     'course {ctx.run_id}",\n                             attendre=ctx.attendre)  # v5 (C-1)',
     'course {ctx.run_id}",\n                             )'),
    ("C-1", "lanceur : clôture sans l'attente du contexte", L4, "                                                attendre=ctx.attendre)  # v5 (C-1)",
     "                                                )"),
    ("C-2", "relecture sans objet jamais rendue", RG, '        if inv.get("prevus") == {} and inv.get("non_copies") == []:', "        if False:"),
    ("C-2", "relecture sans objet sur un inventaire sans « prevus »", RG,
     '        if inv.get("prevus") == {} and inv.get("non_copies") == []:',
     '        if not inv.get("prevus") and not inv.get("non_copies"):'),
    ("C-2", "relecture sans objet au code 0", RG, "            return 4\n", "            return 0\n"),
    ("C-3", "ancien libellé de la vérification", RG,
     "                         verification=\"taille rendue et empreinte déclarée par l'envoyeur, relues à la révision rendue \"",
     "                         verification=\"taille et empreinte rendues par la plateforme \""),
]


def jouer(racine: Path, alteration=None) -> tuple[str, str]:
    with tempfile.TemporaryDirectory() as t:
        t = Path(t)
        for c in COPIES:
            s, d = racine / c, t / c
            d.parent.mkdir(parents=True, exist_ok=True)
            (shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__")) if s.is_dir() else shutil.copyfile(s, d))
        if alteration:
            _, _, f, avant, apres = alteration
            texte = (t / f).read_text(encoding="utf-8")
            if texte.count(avant) != 1:
                return "motif introuvable", f"{texte.count(avant)} fois"
            (t / f).write_text(texte.replace(avant, apres), encoding="utf-8")
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS, "-k", "not copie_reelle"],
                           cwd=t, capture_output=True, text=True, env={"PATH": "/usr/bin:/bin", "PYTHONPATH": str(t / "src"), "HOME": str(t)},
                           timeout=600)
        fin = (r.stdout.strip().splitlines() or [""])[-1]
        return ("passe" if r.returncode == 0 else "échoue"), fin


def main(racine: Path) -> int:
    temoin, fin = jouer(racine)
    print(f"témoin (copie non altérée) : {temoin} — {fin}")
    tuees = 0
    for a in ALTERATIONS:
        etat, fin = jouer(racine, a)
        ok = etat == "échoue"
        tuees += ok
        print(f"({a[0]}) {a[1]} : {'tuée' if ok else 'NON TUÉE'} — {etat} — {fin[:120]}")
    print(f"BANC : {tuees} altérations tuées sur {len(ALTERATIONS)} ; témoin : {temoin}")
    return 0 if tuees == len(ALTERATIONS) and temoin == "passe" else 1


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve()))
