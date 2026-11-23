#!/usr/bin/env python3
"""Essais du programme produire_version_servie_v2.py : un cas sain et des artefacts, dont des mutants, chacun dans un
dossier de travail neuf ; aucun faux sceau n'est laissé hors du dossier de travail (N-3). Sans réseau.

Écrit le 23 novembre 2026 par Claude Opus 5.5 (sous-agent), pour N-3 et N-4 de la vérification des corrections du devis
(verification-corrections-devis-v8-v1.md, 64045cf7…). Pièce d'instrument (classe B), à contre-lire.

Chaque artefact doit arrêter le programme au code attendu, avec le motif attendu, sans rien écrire dans sa sortie. Les
contrôles redondants (reste identique hors zone, lignes, différentiel, garde résiduelle) ne peuvent échouer que si un
contrôle antérieur est faux : ils sont éprouvés par des mutants, copies du programme où le contrôle antérieur est
neutralisé et une faute injectée, chaque substitution étant exigée exactement une fois.

Usage :
  PYTHONPATH=src python3 essais_produire_version_servie_v2.py --programme produire_version_servie_v2.py --v8 V8.md \
      --paires-garde LISTE.json --paires-supplementaires LISTE.json --moteur v8d CHEMIN --moteur v8m CHEMIN \
      --empreinte-attendue EMPREINTE_DE_LA_VERSION_SERVIE --temp DOSSIER_DE_TRAVAIL --compte-rendu FICHIER
Code de sortie : 0 si tous les essais donnent le résultat attendu, 2 sinon.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VERSION = "essais-produire-version-servie-v2"


def empreinte(octets):
    return hashlib.sha256(octets).hexdigest()


def sceller(chemin):
    Path(str(chemin) + ".sha256").write_text(f"{empreinte(Path(chemin).read_bytes())}  {Path(chemin).name}\n",
                                             encoding="utf-8")


def ecrire_liste(chemin, liste, sceau=True):
    Path(chemin).write_text(json.dumps(liste, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if sceau:
        sceller(chemin)


def substituer(texte, avant, apres):
    if texte.count(avant) != 1:
        raise SystemExit(f"essai mal formé : {avant[:60]!r} trouvé {texte.count(avant)} fois dans la copie")
    return texte.replace(avant, apres)


def principal(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--programme", required=True)
    p.add_argument("--v8", required=True)
    p.add_argument("--paires-garde", required=True)
    p.add_argument("--paires-supplementaires", required=True)
    p.add_argument("--moteur", nargs=2, action="append", metavar=("NOM", "CHEMIN"), required=True)
    p.add_argument("--empreinte-attendue", required=True)
    p.add_argument("--temp", required=True)
    p.add_argument("--compte-rendu", required=True)
    a = p.parse_args(argv)
    programme = Path(a.programme).resolve()
    source_programme = programme.read_text(encoding="utf-8")
    racine = programme.parents[4]
    env = dict(os.environ, PYTHONPATH=str(racine / "src"))
    moteurs = {n: str(Path(c).resolve()) for n, c in a.moteur}
    v8 = Path(a.v8).read_text(encoding="utf-8")
    garde = json.loads(Path(a.paires_garde).read_text(encoding="utf-8"))
    supp = json.loads(Path(a.paires_supplementaires).read_text(encoding="utf-8"))
    temp = Path(a.temp)
    temp.mkdir(parents=True, exist_ok=True)
    resultats = []

    def lancer(nom, attendu_code, attendu_motif, programme_texte=None, v8_texte=None, liste_g=None, liste_s=None,
               sceau_g=True, sceau_s=True, moteurs_args=None, sortie_existante=False, empreinte_v8=None):
        dossier = Path(tempfile.mkdtemp(prefix=f"essai-{nom}-", dir=temp))
        try:
            prog = dossier / "produire_version_servie_v2.py"
            texte_prog = source_programme if programme_texte is None else programme_texte
            if empreinte_v8 is not None:
                texte_prog = substituer(texte_prog, 'EMPREINTE_V8 = "047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a"',
                                        f'EMPREINTE_V8 = "{empreinte_v8}"')
            prog.write_text(texte_prog, encoding="utf-8")
            chemin_v8 = dossier / "question-collisionneur-modes-sabotage-v8.md"
            chemin_v8.write_text(v8 if v8_texte is None else v8_texte, encoding="utf-8", newline="\n")
            lg, ls_ = dossier / "paires-garde.json", dossier / "paires-supplementaires.json"
            ecrire_liste(lg, garde if liste_g is None else liste_g, sceau_g)
            ecrire_liste(ls_, supp if liste_s is None else liste_s, sceau_s)
            if not sceau_g:
                Path(str(lg) + ".sha256").write_text("0" * 64 + "  paires-garde.json\n", encoding="utf-8")
            if not sceau_s:
                Path(str(ls_) + ".sha256").write_text("0" * 64 + "  paires-supplementaires.json\n", encoding="utf-8")
            sortie = dossier / "sortie"
            sortie.mkdir()
            if sortie_existante:
                (sortie / "question-collisionneur-modes-sabotage-v8-servie-v2.md").write_text("déjà là\n", encoding="utf-8")
            args = [sys.executable, str(prog), "--v8", str(chemin_v8), "--paires-garde", str(lg),
                    "--paires-supplementaires", str(ls_), "--sortie", str(sortie), "--temp", str(dossier / "travail")]
            for n, c in (moteurs_args if moteurs_args is not None else moteurs.items()):
                args += ["--moteur", n, c]
            r = subprocess.run(args, capture_output=True, text=True, env=env, cwd=str(racine))
            ecrits = sorted(x.name for x in sortie.iterdir())
            if sortie_existante:
                ecrits = [x for x in ecrits if x != "question-collisionneur-modes-sabotage-v8-servie-v2.md"]
            derniere = (r.stderr.strip().splitlines() or [""])[-1]
            if attendu_code == 0:
                servie = sortie / "question-collisionneur-modes-sabotage-v8-servie-v2.md"
                h = empreinte(servie.read_bytes()) if servie.exists() else None
                ok = r.returncode == 0 and h == a.empreinte_attendue
                detail = f"code {r.returncode}, version servie {h}"
            else:
                ok = r.returncode == attendu_code and attendu_motif in r.stderr and not ecrits
                detail = f"code {r.returncode}, {len(ecrits)} fichier(s) écrit(s), « {derniere[:150]} »"
            resultats.append((nom, ok, detail))
        finally:
            shutil.rmtree(dossier, ignore_errors=True)

    def copie(liste):
        return json.loads(json.dumps(liste))

    # cas sain
    lancer("sain", 0, None)
    # liste de la garde
    g = copie(garde); g["paires"] = g["paires"][:-1]
    lancer("garde-paire-manquante", 2, "n'est pas exactement ce que la garde refuse", liste_g=g)
    g = copie(garde); g["paires"].append(dict(copie(supp["paires"][0]), categorie="chemin interne"))
    for k in ("nom", "raison"):
        g["paires"][-1].pop(k)
    lancer("garde-paire-en-trop", 2, "n'est pas exactement ce que la garde refuse", liste_g=g)
    g = copie(garde); g["paires"][1]["ancien"] = "GO-2026-11-22-135"
    lancer("garde-identifiant-non-elargi", 2, "trouvé 2 fois", liste_g=g)
    lancer("garde-sceau-faux", 2, "≠ son sceau", sceau_g=False)
    g = copie(garde); del g["paires"][0]["ancien"]
    lancer("garde-paire-sans-ancien", 2, "malformée", liste_g=g)
    g = copie(garde); g["paires"] = {"n": 1}
    lancer("garde-paires-pas-une-liste", 2, "malformée", liste_g=g)
    # liste supplémentaire
    s = copie(supp); s["paires"][0]["ancien"] = "`absent-de-la-v8`"
    lancer("supplementaire-absente", 2, "trouvé 0 fois", liste_s=s)
    s = copie(supp); s["paires"][0]["ancien"] = "pièce d'entrée du rédacteur, 22 novembre 2026"
    lancer("supplementaire-double", 2, "trouvé 2 fois", liste_s=s)
    s = copie(supp); del s["paires"][1]["nom"]
    lancer("supplementaire-sans-nom", 2, "« nom »", liste_s=s)
    s = copie(supp); s["paires"].append({"n": 3, "nom": "chemin déjà pris par la garde", "ligne_v8": 179,
                                         "categorie": "chemin interne hors garde", "ancien": "`registres/go.md`",
                                         "nouveau": supp["mention"], "raison": "essai"})
    lancer("supplementaire-porte-un-motif", 2, "relève de la liste de la garde", liste_s=s)
    s = copie(supp); s["paires"].append({"n": 3, "nom": "hors zone", "ligne_v8": 22, "categorie": "essai",
                                         "ancien": "Llama-3.1-8B-Instruct", "nouveau": supp["mention"], "raison": "essai"})
    lancer("supplementaire-hors-zone", 2, "hors de la zone permise", liste_s=s)
    lancer("supplementaire-sceau-faux", 2, "≠ son sceau", sceau_s=False)
    s = copie(supp); s["mention"] = "[autre]"
    lancer("supplementaire-autre-mention", 2, "mention", liste_s=s)
    # entrées et moteurs
    lancer("v8-alteree", 2, "v8 : empreinte", v8_texte="x" + v8)
    lancer("sortie-existante", 2, "existe déjà", sortie_existante=True)
    lancer("moteur-inconnu", 2, "inconnu", moteurs_args=list(moteurs.items()) + [("v8z", moteurs["v8d"])])
    lancer("moteur-empreinte-fausse", 2, "empreinte fixée", moteurs_args=[("v8d", moteurs["v8m"]), ("v8m", moteurs["v8m"])])
    lancer("moteurs-exiges-absents", 2, "au moins", moteurs_args=[("v8d", moteurs["v8d"])])
    # restes (5e) : v8 témoin portant un reste hors des jetons, dans la zone
    temoin = substituer(v8, "(décision sur les modes de sabotage et le mode tenu à l'écart)",
                        "(décision sur les modes de sabotage et le mode tenu à l'écart, voir -137)")
    h_t = empreinte(temoin.encode("utf-8"))
    g = copie(garde); g["source"]["sha256"] = h_t
    s = copie(supp); s["source"]["sha256"] = h_t
    lancer("reste-dans-le-texte-servi", 2, "reste « suite abrégée d'un identifiant (élargi) »", v8_texte=temoin,
           liste_g=g, liste_s=s, empreinte_v8=h_t)
    # mutants : contrôles redondants
    sans_5a = substituer(source_programme, "        if reconstruit != base:\n", "        if False:\n")
    faute = '        morceaux = servi.split(MENTION)\n'
    lancer("mutant-hors-zone", 2, "le texte change hors de la zone permise", programme_texte=substituer(
        sans_5a, faute, '        servi = servi.replace("Le programme étudie", "Le programme examine", 1)\n' + faute))
    lancer("mutant-ligne-hors-paires", 2, "≠ lignes qui portaient un ancien", programme_texte=substituer(
        sans_5a, faute, '        servi = servi.replace("| [source 20] | pièce d\'entrée du rédacteur", '
                        '"| [source 20] | pièce d\'entrée", 1)\n' + faute))
    lancer("mutant-ligne-portee-alteree", 2, "la différence n'est pas exactement ses paires", programme_texte=substituer(
        sans_5a, faute, '        servi = servi.replace("(décision sur les modes de sabotage", '
                        '"(décision sur des modes de sabotage", 1)\n' + faute))
    lancer("mutant-differentiel", 2, "le différentiel unifié porte sur d'autres lignes", programme_texte=substituer(
        source_programme, "servi.splitlines(keepends=True),\n",
        'servi.replace("Le programme étudie", "Le programme examine", 1).splitlines(keepends=True),\n'))
    mutant_garde = substituer(substituer(source_programme,
                                         "        if [(d[0], d[1], d[2], d[3]) for d in derive] != [(q[0], q[1], q[2], q[3]) for q in garde]:\n",
                                         "        if False:\n"),
                              "        for nom, motif in RESTES:\n", "        for nom, motif in ():\n")
    g = copie(garde); g["paires"] = g["paires"][1:]
    lancer("mutant-garde-residuelle", 2, "la version servie porte encore", programme_texte=mutant_garde, liste_g=g)
    # garde différente entre deux moteurs : moteur mutant d'empreinte admise par une copie du programme
    texte_moteur = Path(moteurs["v8d"]).read_text(encoding="utf-8")
    texte_mutant = substituer(texte_moteur, 're.compile(r"\\bGO-\\d{4}-\\d{2}-\\d{2}-\\d+")', 're.compile(r"\\bGO-JAMAIS")')
    dossier_mutant = Path(tempfile.mkdtemp(prefix="moteur-mutant-", dir=temp))
    chemin_mutant = dossier_mutant / "collisionneur_v9_v8x.py"
    chemin_mutant.write_text(texte_mutant, encoding="utf-8")
    h_mutant = empreinte(chemin_mutant.read_bytes())
    prog_mutant = substituer(source_programme, 'MOTEURS_EXIGES = ("v8d", "v8m")',
                             f'MOTEURS_ATTENDUS["v8x"] = "{h_mutant}"\nMOTEURS_EXIGES = ("v8d", "v8m")')
    lancer("moteurs-en-desaccord", 2, "occurrences différentes", programme_texte=prog_mutant,
           moteurs_args=list(moteurs.items()) + [("v8x", str(chemin_mutant))])
    shutil.rmtree(dossier_mutant, ignore_errors=True)
    # compte rendu
    lignes = [f"Compte rendu de {VERSION} ; programme éprouvé {programme.name}, sha256 "
              f"{empreinte(programme.read_bytes())} ; essais {Path(__file__).name}, sha256 "
              f"{empreinte(Path(__file__).read_bytes())} ; moteurs {', '.join(moteurs)}.", ""]
    for nom, ok, detail in resultats:
        lignes.append(f"{'tenu ' if ok else 'ÉCHEC'} {nom} : {detail}")
    tenus = sum(1 for _, ok, _ in resultats if ok)
    lignes += ["", f"EN BREF : {tenus} essais sur {len(resultats)} donnent le résultat attendu (1 cas sain, "
                   f"{len(resultats) - 1} artefacts et mutants refusés sans écriture)."]
    texte = "\n".join(lignes) + "\n"
    with open(a.compte_rendu, "x", encoding="utf-8", newline="\n") as f:
        f.write(texte)
    print(texte, end="")
    return 0 if tenus == len(resultats) else 2


if __name__ == "__main__":
    sys.exit(principal())
