#!/usr/bin/env python3
"""Essais du contrôle du gel du texte de T0.8 et du programme de scellement (version 4) : cas sains et artefacts (R5).

Usage (depuis la racine du dépôt) : PYTHONPATH=src python3 brouillons/t08-texte-complet-fable-v1/essais-controle-gel-t08-v5.py \
    --src-code <dossier src d'un arbre propre qui porte le code de T0.8 (configuration_v1)>
Version 5 : les 27 essais de la version 4, joués sur le programme de scellement en version 4 (le commit donné est la tête
de l'arbre `--src-code`), plus les essais du fichier des marqueurs : écriture et compagnon, rejeu du code de T0.8
(`exiger_marqueurs`, `exiger_marqueurs_au_texte`) sur le texte écrit, contrôle « à la place » (cas sain et artefacts :
fichier altéré, valeur citée ailleurs, remplissage doublé, remplissage du GO altéré), R12 sur le fichier des marqueurs,
arbre du code à une autre tête.
Version 4 : mêmes essais que la version 3, sur le brouillon 15.
Tout se joue dans un dossier temporaire ; rien n'est écrit dans le dépôt ; aucune entropie n'est tirée (les essais qui
écrivent passent `--entropie`). Sortie : une ligne par essai ; code 0 si chaque essai rend l'issue attendue, 1 sinon.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ICI = Path("brouillons/t08-texte-complet-fable-v1")
sys.path.insert(0, str(ICI))
import controle_gel_t08_v1 as gel  # noqa: E402

B12 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon15.md")   # le brouillon éprouvé (nom de variable gardé)
FINALISER = ICI / "finaliser-t08-scellement-v4.py"
NEUFS = json.loads((ICI / "textes-neufs-t08-brouillon15-v1.json").read_text(encoding="utf-8"))
VALEURS = NEUFS["valeurs_marqueurs_en_sections_gelees"]
SRC_CODE: Path = Path("src")   # fixé par --src-code
COMMIT = ""                    # tête de --src-code


def une(texte: str, ancien: str, nouveau: str) -> str:
    assert texte.count(ancien) == 1, (texte.count(ancien), ancien[:50])
    return texte.replace(ancien, nouveau)


def artefacts(b12: str) -> dict[str, str]:
    lignes = b12.split("\n")
    i = next(k for k, l in enumerate(lignes) if l.startswith(gel.DEBUT_T5_19))
    t5 = lignes[i]
    j = next(k for k, l in enumerate(lignes) if l.startswith("4. **Graines (R9)**"))
    return {
        "seuil gelé changé (0,10 devient 0,15)": une(b12, "sur la dose ≤ **0,10**", "sur la dose ≤ **0,15**"),
        "phrase gelée de la table F retouchée": une(b12, "« dose intermédiaire : ni diffuse ni flagrante à cette puissance »",
                                                    "« dose moyenne : ni diffuse ni flagrante à cette puissance »"),
        "phrase T5-19 réécrite": une(b12, "**gardée**, option (a), mot de Lazar",
                                     "**gardée**, option (b), et le seuil de « diffuse » est porté à 0,15, mot de Lazar"),
        "phrase T5-19 déplacée": "\n".join(lignes[:i] + lignes[i + 1:j] + [t5] + lignes[j:]),
        "phrase T5-19 doublée": "\n".join(lignes[:i + 1] + [t5] + lignes[i + 1:]),
        "phrase T5-19 retirée": "\n".join(lignes[:i] + lignes[i + 1:]),
        "valeur d'un marqueur altérée (run de 7b)": une(b12, "run `20261111-151701-t06-reel`, branche de sortie",
                                                        "run `20261111-151701-t06-faux`, branche de sortie"),
        "ligne ajoutée dans la liste d'arrêt": une(b12, "\n## Machine, devis et dépense", "\n- Arrêt neuf, non gelé.\n\n## Machine, devis et dépense"),
    }


def ecrire(dossier: Path, nom: str, contenu: str) -> Path:
    p = dossier / nom
    p.write_text(contenu, encoding="utf-8")
    Path(str(p) + ".sha256").write_text(f"{gel.sha(contenu.encode('utf-8'))}  {nom}\n", encoding="utf-8")
    return p


def finaliser(entree: Path, sha_entree: str, rapport: Path, emp: Path, cl: Path, sortie: Path, *plus: str,
              commit: str | None = None, depense: str = "essai : engagement, T0.8", src: Path | None = None) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(FINALISER), "--entree", str(entree), "--sha-entree", sha_entree,
                        "--rapport-verification", str(rapport), "--commit-code", commit or COMMIT, "--empreintes-code", str(emp),
                        "--contre-lecture-code", str(cl), "--ligne-gardes", "R-9999", "--ligne-depense", depense,
                        "--src-code", str(src or SRC_CODE),
                        "--dossier-sortie", str(sortie), *plus], capture_output=True, text=True)
    return r.returncode, (r.stderr or r.stdout).strip().split("\n")[-1][:150]


def charger_finaliser():
    import importlib.util
    spec = importlib.util.spec_from_file_location("finaliser_v4", FINALISER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def code_t08(mq_chemin: Path, texte_chemin: Path) -> tuple[int, str]:
    """Rejoue `exiger_marqueurs` et `exiger_marqueurs_au_texte` du code de T0.8 (arbre --src-code), processus à part."""
    import os
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["PYTHONPATH"] = str(SRC_CODE.resolve())
    prog = ("import json,sys; from pathlib import Path; from controle_ia.t08 import configuration_v1 as cf; "
            "mq=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')); cf.exiger_marqueurs(mq); "
            "print(cf.exiger_marqueurs_au_texte(sys.argv[2], mq))")
    r = subprocess.run([sys.executable, "-B", "-c", prog, str(mq_chemin), str(texte_chemin)], capture_output=True,
                       text=True, env=env)
    return r.returncode, (r.stderr or r.stdout).strip().split("\n")[-1][:150]


def main() -> int:
    global SRC_CODE, COMMIT
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-code", required=True)
    SRC_CODE = Path(ap.parse_args().src_code)
    COMMIT = subprocess.run(["git", "-C", str(SRC_CODE), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    b12 = B12.read_text(encoding="utf-8")
    sha12 = gel.sha(b12.encode("utf-8"))
    bilan = []

    def noter(nom: str, attendu: str, obtenu: str, detail: str = ""):
        bilan.append(attendu == obtenu)
        print(f"{'conforme' if attendu == obtenu else 'NON CONFORME'} | {nom} | attendu : {attendu} | obtenu : {obtenu} | {detail}")

    # A. le contrôle du gel, appelé directement
    try:
        gel.controler_gel(b12, VALEURS)
        noter("contrôle du gel, brouillon 14 (cas sain)", "tenu", "tenu")
    except SystemExit as e:
        noter("contrôle du gel, brouillon 14 (cas sain)", "tenu", "arrêt", str(e)[:110])
    arts = artefacts(b12)
    for nom, texte in arts.items():
        try:
            gel.controler_gel(texte, VALEURS)
            noter("contrôle du gel, artefact : " + nom, "arrêt", "tenu")
        except SystemExit as e:
            noter("contrôle du gel, artefact : " + nom, "arrêt", "arrêt", str(e)[:90])

    # B. le programme de scellement
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        sortie = d / "sortie"
        sortie.mkdir()
        emp = ecrire(d, "empreintes.md", f"commit {COMMIT}\n")
        cl = ecrire(d, "contre-lecture-code.md", "essai\n")
        rapport = ecrire(d, "verification.md", f"brouillon vérifié : {sha12}\n")
        sain = ecrire(d, "sain.md", b12)
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, cas sain", "0", str(code), msg)
        # artefacts du gel, épinglés à leur propre empreinte et à un rapport qui la cite : seul le gel doit les arrêter
        for k, (nom, texte) in enumerate(arts.items()):
            s = gel.sha(texte.encode("utf-8"))
            f = ecrire(d, f"artefact-{k}.md", texte)
            r = ecrire(d, f"verification-{k}.md", f"brouillon vérifié : {s}\n")
            code, msg = finaliser(f, s, r, emp, cl, sortie, "--a-blanc")
            noter("scellement à blanc, artefact : " + nom, "1", str(code), msg)
        # M-8 : une section non gelée modifiée après la vérification
        modifie = une(b12, "Rien n'est lancé, rien n'est dépensé. L'en-tête", "Rien n'est lancé. L'en-tête")
        f = ecrire(d, "non-gele-modifie.md", modifie)
        code, msg = finaliser(f, sha12, rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, section non gelée modifiée après la vérification", "1", str(code), msg)
        code, msg = finaliser(f, gel.sha(modifie.encode("utf-8")), rapport, emp, cl, sortie, "--a-blanc")
        noter("scellement à blanc, même fichier, empreinte donnée mais absente du rapport de vérification", "1", str(code), msg)
        # formes
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc", commit="453a71e1")
        noter("scellement à blanc, commit court", "1", str(code), msg)
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--a-blanc", depense="sans la tâche")
        noter("scellement à blanc, ligne de dépense sans la tâche", "1", str(code), msg)
        # écriture réelle dans le dossier temporaire, entropie donnée ; puis rejeu : n'écrase jamais
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--entropie", "123456789012345678901234567890")
        noter("scellement réel dans un dossier temporaire, cas sain", "0", str(code), msg)
        ecrit = sortie / "T0.8-bases-boite-noire-v0-v1.md"
        if ecrit.exists():
            t = ecrit.read_text(encoding="utf-8")
            import re
            noter("texte écrit : aucun marqueur restant", "0", str(len(re.findall(r"<<[A-Z0-9_]+>>", t))))
            noter("texte écrit : annexe intacte (phrase « non scellé » du brouillon 10 gardée une fois)", "1",
                  str(t.count("**non scellé** ; il ne vaut pas préenregistrement (R1)")))
            try:
                toutes = dict(VALEURS)
                toutes["ENTROPIE_T08"] = "`123456789012345678901234567890`"
                toutes["LIGNE_MOT_LAZAR_T5_19"] = ("R-2657 (mot de Lazar inscrit le 14 novembre), GO-2026-11-22-122 (garde "
                                                   "d'antériorité gardée, option (a) ; sort de VT5-07) et R-9999 (trois autres "
                                                   "gardes de code plus strictes confirmées)")
                gel.controler_gel(t, toutes)
                noter("texte écrit : contrôle du gel rejoué", "tenu", "tenu")
            except SystemExit as e:
                noter("texte écrit : contrôle du gel rejoué", "tenu", "arrêt", str(e)[:100])
        code, msg = finaliser(sain, sha12, rapport, emp, cl, sortie, "--entropie", "123456789012345678901234567890")
        noter("scellement réel rejoué sur des sorties existantes", "1", str(code), msg)
        essais_marqueurs(d, sortie, sain, sha12, rapport, emp, cl, b12, noter)
    print(f"\n{sum(bilan)} essais conformes sur {len(bilan)}")
    return 0 if all(bilan) else 1


def essais_marqueurs(d: Path, sortie: Path, sain: Path, sha12: str, rapport: Path, emp: Path, cl: Path, b12: str,
                     noter) -> None:
    """Essais de la version 4 : fichier des marqueurs (contraintes 1 à 3 de la session mère)."""
    import shutil
    f4 = charger_finaliser()
    texte_ecrit = sortie / "T0.8-bases-boite-noire-v0-v1.md"
    mq_chemin = sortie / "T0.8-marqueurs-scellement-v1.json"
    # écriture et compagnon
    ok = mq_chemin.is_file() and Path(str(mq_chemin) + ".sha256").is_file()
    noter("fichier des marqueurs écrit, avec son compagnon", "oui", "oui" if ok else "non")
    if not ok:
        return
    contenu = mq_chemin.read_text(encoding="utf-8")
    compag = Path(str(mq_chemin) + ".sha256").read_text(encoding="utf-8")
    noter("compagnon du fichier des marqueurs conforme", "oui",
          "oui" if compag == f"{gel.sha(contenu.encode('utf-8'))}  {mq_chemin.name}\n" else "non")
    mq = json.loads(contenu)
    t = texte_ecrit.read_text(encoding="utf-8")
    # contrainte 1 : valeurs = arguments et chaînes du texte
    attendu = {"COMMIT_CODE_T08": COMMIT, "ENTROPIE_T08": 123456789012345678901234567890,
               "LIGNE_DEPENSE_T08": "essai : engagement, T0.8", "RUN_7B.run_id": "20261111-151701-t06-reel",
               "GO_T08": {"id": "GO-2026-11-10-12", "plafond_usd": 120}}
    obtenu = {"COMMIT_CODE_T08": mq["COMMIT_CODE_T08"], "ENTROPIE_T08": mq["ENTROPIE_T08"],
              "LIGNE_DEPENSE_T08": mq["LIGNE_DEPENSE_T08"], "RUN_7B.run_id": mq["RUN_7B"]["run_id"], "GO_T08": mq["GO_T08"]}
    noter("fichier des marqueurs : valeurs = arguments donnés et chaînes du texte", "égales",
          "égales" if obtenu == attendu else "différentes", str(obtenu)[:100])
    # contrainte 2 : code de T0.8 rejoué sur le texte écrit, scellé (copie)
    copie = d / "rejeu"
    copie.mkdir()
    tc = copie / texte_ecrit.name
    shutil.copyfile(texte_ecrit, tc)
    Path(str(tc) + ".sha256").write_text(f"{gel.sha(tc.read_bytes())}  {tc.name}\n", encoding="utf-8")
    code, msg = code_t08(mq_chemin, tc)
    noter("code de T0.8 : exiger_marqueurs et exiger_marqueurs_au_texte sur le texte écrit (cas sain)", "0", str(code), msg)
    # contrainte 3 : contrôle « à la place », appelé directement
    neufs = f4.lire_json_epingle(f4.TEXTES, f4.SHA_TEXTES)
    rempl = f4.remplissages_prealables(neufs, f4.lire_json_epingle(f4.TEXTES_B11, f4.SHA_TEXTES_B11))
    rempl["ENTROPIE_T08"] = "`123456789012345678901234567890`"
    rempl["LIGNE_DEPENSE_T08"] = "ligne inscrite au scellement : essai : engagement, T0.8"
    rempl["COMMIT_CODE_T08"] = (f"`{COMMIT}` (pièce de ses empreintes `{emp}`, `{gel.sha(emp.read_bytes())}` ; "
                                f"contre-lecture de l'alignement `{cl}`, `{gel.sha(cl.read_bytes())}`)")

    def place(texte, marq) -> tuple[str, str]:
        try:
            f4.controler_place(texte, rempl, marq)
            return "tenu", ""
        except SystemExit as e:
            return "arrêt", str(e)[:110]

    o, x = place(t, mq)
    noter("contrôle « à la place », texte et fichier écrits (cas sain)", "tenu", o, x)

    def altere(chemin_cle, valeur):
        m2 = json.loads(contenu)
        cible = m2
        for k in chemin_cle[:-1]:
            cible = cible[k]
        cible[chemin_cle[-1]] = valeur
        return m2

    # VCT8-04 : une valeur citée ailleurs dans le texte passe le code de T0.8, pas le contrôle « à la place »
    for nom, cle, val in (("GO de prolongation (cité dans le remplissage du GO) à la place du GO", ("GO_T08", "id"),
                           "GO-2026-11-22-79"),
                          ("empreintes du manifeste et des mesures échangées", ("EMPREINTES_ENTREES_7B", "mesures-t06.npz"),
                           mq["EMPREINTES_ENTREES_7B"]["manifeste.json"])):
        m2 = altere(cle, val)
        if cle[0] == "EMPREINTES_ENTREES_7B":
            m2["EMPREINTES_ENTREES_7B"]["manifeste.json"] = mq["EMPREINTES_ENTREES_7B"]["mesures-t06.npz"]
            m2["RUN_7B"]["manifeste_sha256"] = mq["EMPREINTES_ENTREES_7B"]["mesures-t06.npz"]
        j = copie / "altere.json"
        j.write_text(json.dumps(m2, ensure_ascii=False), encoding="utf-8")
        code, msg = code_t08(j, tc)
        noter(f"limite VCT8-04 montrée : {nom} : le code de T0.8 l'admet", "0", str(code), msg)
        o, x = place(t, m2)
        noter(f"contrôle « à la place », artefact : {nom}", "arrêt", o, x)
    for nom, cle, val in (("entropie changée", ("ENTROPIE_T08",), 987654321),
                          ("run de 7b changé", ("RUN_7B", "run_id"), "20261111-151701-t06-faux"),
                          ("commit changé", ("COMMIT_CODE_T08",), "f" * 40)):
        o, x = place(t, altere(cle, val))
        noter(f"contrôle « à la place », artefact : {nom}", "arrêt", o, x)
    o, x = place(t + "\n" + rempl["GO_T08"] + "\n", mq)
    noter("contrôle « à la place », artefact : remplissage du GO doublé", "arrêt", o, x)
    o, x = place(t + f"\nLe commit `{COMMIT}` est aussi cité ici.\n", mq)
    noter("contrôle « à la place », artefact : commit cité une seconde fois, hors de son marqueur", "arrêt", o, x)
    o, x = place(t + f"\nEmpreinte `{mq['EMPREINTES_ENTREES_7B']['episodes-t06.json']}` citée ici.\n", mq)
    noter("contrôle « à la place », artefact : empreinte d'entrée de 7b citée hors de son marqueur", "arrêt", o, x)
    # le programme, sur un brouillon dont le remplissage du GO (section non gelée) est altéré : le gel ne le voit pas
    alt = une(b12, "(type « calcul », plafond 120 USD, inscrite le 10 novembre", "(type « calcul », plafond 150 USD, inscrite le 10 novembre")
    fa = ecrire(d, "go-altere.md", alt)
    ra = ecrire(d, "verification-go.md", f"brouillon vérifié : {gel.sha(alt.encode('utf-8'))}\n")
    code, msg = finaliser(fa, gel.sha(alt.encode("utf-8")), ra, emp, cl, d / "sortie-go", "--a-blanc")
    noter("scellement à blanc, artefact : remplissage du GO altéré hors des sections gelées", "1", str(code), msg)
    # R12 sur le seul fichier des marqueurs
    s2 = d / "sortie-r12"
    s2.mkdir()
    (s2 / "T0.8-marqueurs-scellement-v1.json").write_text("{}\n", encoding="utf-8")
    code, msg = finaliser(sain, sha12, rapport, emp, cl, s2, "--entropie", "123456789012345678901234567890")
    noter("scellement réel, fichier des marqueurs seul déjà présent (R12)", "1", str(code), msg)
    # arbre du code à une autre tête que le commit donné
    autre = "f" * 40
    emp2 = ecrire(d, "empreintes-autre.md", f"commit {autre}\n")
    code, msg = finaliser(sain, sha12, rapport, emp2, cl, d / "sortie", "--a-blanc", commit=autre)
    noter("scellement à blanc, arbre du code à une autre tête que le commit cité", "1 (tête)",
          f"{code} ({'tête' if 'tête' in msg else msg[:40]})", msg)


if __name__ == "__main__":
    sys.exit(main())
