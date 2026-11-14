"""Répétition à blanc du jour du rendez-vous de P3-bis, sur jouet, dans le bac du rédacteur (aucun fichier du dépôt touché).

Module d'ouverture : copie de `ouverture_p3bis_v3.py` tirée de S (`4a54a437…`), importée depuis le bac. Registres, texte de
T0.7, décisions et paquets : FACTICES, fabriqués ici. But : éprouver la forme exacte du fichier de décision, des lignes du
registre des préalables, des appels `ouvrir` et `exposer-issue`, et les refus attendus.

Usage : python essai_rendez_vous_v1.py <bac> <src du module>
"""
import io
import json
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

B = Path(sys.argv[1])
sys.path.insert(0, sys.argv[2])
from controle_ia.premier_test_ia import ouverture_p3bis_v3 as o  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

RUN = "20261113-121129-p3bis-reel"
RL, RLC = "20261113-154301-p3bis-lecture", "20261113-154301-p3bis-lecture-complementaire"
ECRITS = ("ECRIT-PERIMETRE-JEUX-P3BIS", "ECRIT-LANCEMENT-RELANCE-P3BIS", "ECRIT-ENGAGEMENT-ETAPE-A-P3BIS")
t = o.instant_utc


def decision(mot: str, date: str, espace=" ") -> str:
    return ("# Rendez-vous de P3-bis — décision n° 1 de Lazar (v1)\n\n"
            "- Mots de Lazar, verbatim, reçus dans la session mère à 12:05:00 UTC le 20 novembre 2026 (heure relevée par "
            "`date -u`) :\n\n"
            f"> {mot}\n\n"
            f"Décision{espace}: {mot}\n"
            f"Date : {date}\n\n"
            "- Recopiée mot pour mot par la session mère ; scellée par son compagnon ; citée par la ligne "
            "`RENDEZ-VOUS-P3BIS-1` de `registres/prealables-p3bis-v1.md`.\n")


def monter(nom, ecrits=True, decisions=(), t07_dates=("2026-11-11T07:11:42Z", "2026-11-11T07:12:25Z")):
    r = B / nom
    if r.exists():
        shutil.rmtree(r)
    for d in ("registres", "prereg", "docs/decisions", "docs/verdicts"):
        (r / d).mkdir(parents=True)
    t07 = r / "prereg/T0.7-sondes-v0-v1.md"
    t07.write_text("texte factice (bac d'essai), aucun lien avec T0.7\n", encoding="utf-8")
    s7 = sceller(t07)
    (r / "registres/scellements-v1.md").write_text(
        "# Registre des scellements (T0.6, T0.7, P3-bis) — lignes ajoutées, jamais réécrites\n\n"
        f"| SCELLEMENT-T07 | {t07_dates[0]} | prereg/T0.7-sondes-v0-v1.md | {s7} |\n", encoding="utf-8")
    lignes = ["# Registre des préalables de P3-bis (factice)", "",
              f"| GARDE-ADAPTEE-T07-P3BIS | {t07_dates[1]} | prereg/T0.7-sondes-v0-v1.md | {s7} |"]
    if ecrits:
        lignes += [f"| {k} | 2026-11-14T09:00:00Z | prereg/T0.7-sondes-v0-v1.md | {s7} |" for k in ECRITS]
    for n, (texte, date_ligne) in enumerate(decisions, start=1):
        f = r / f"docs/decisions/rendez-vous-P3-bis-v{n}.md"
        f.write_text(texte, encoding="utf-8")
        lignes.append(f"| RENDEZ-VOUS-P3BIS-{n} | {date_ligne} | docs/decisions/rendez-vous-P3-bis-v{n}.md | {sceller(f)} |")
    (r / "registres/prealables-p3bis-v1.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return r


def fabriquer_paquets(p: Path, issue=("vu", 4)):
    if p.exists():
        shutil.rmtree(p)
    tmp = p.parent / (p.name + "-tmp")
    if tmp.exists():
        shutil.rmtree(tmp)
    # lectures (factices) : lecture-p3bis.json scellé, comme `ecrire_resultat`
    for c, contenu in ((f"diag/{RLC}/lecture-p3bis.json", {"run_id": RLC, "manifeste_sha256": "0" * 64,
                                                            "resultat": {"issue_mecanique": {"issue": issue[0], "ligne": issue[1]}}}),
                       (f"diag/{RL}/lecture-p3.json", {"run_id": RL, "manifeste_sha256": "0" * 64, "resultat": {}})):
        (tmp / c).parent.mkdir(parents=True, exist_ok=True)
        (tmp / c).write_text(json.dumps(contenu, ensure_ascii=False) + "\n", encoding="utf-8")
        sceller(tmp / c)
    (tmp / "espace-ferme-p3bis").mkdir(parents=True)
    (tmp / "espace-ferme-p3bis/durees-lectures-v1.json").write_text("{}\n", encoding="utf-8")
    chemins = sorted(str(x.relative_to(tmp)) for x in tmp.rglob("*") if x.is_file())
    lect = o.paquet_lectures(o.archive_des_fichiers(tmp, chemins), o.tirer_sel())
    cible = p / o.dossier_ferme(RUN) / o.PAQUET_LECTURES
    cible.parent.mkdir(parents=True)
    cible.write_bytes(lect)
    sha_l = sceller(cible)
    # second paquet (factice) : donnees/<run>/ et épisodes
    tmp2 = p.parent / (p.name + "-tmp2")
    if tmp2.exists():
        shutil.rmtree(tmp2)
    for c in [f"donnees/{RUN}/{n}" for n in o.DONNEES_EXIGEES] + [f"diag/{RUN}/{o.EPISODES}"]:
        (tmp2 / c).parent.mkdir(parents=True, exist_ok=True)
        (tmp2 / c).write_bytes(b"factice " + c.encode())
        sceller(tmp2 / c)
    ch2 = sorted(str(x.relative_to(tmp2)) for x in tmp2.rglob("*") if x.is_file())
    octets = o.paquet_run(o.archive_des_fichiers(tmp2, ch2), o.tirer_sel())
    d = p / "diag" / RUN
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{o.PAQUET_RUN}.000").write_bytes(octets)
    m = {"nom": f"{o.PAQUET_RUN}.000", "sha256": sceller(d / f"{o.PAQUET_RUN}.000"), "taille": len(octets)}
    index = {"version": 1, "run": RUN, "paquet": o.PAQUET_RUN, "sha256": o._sha(octets), "taille": len(octets),
             "taille_morceau_max": o.TAILLE_MORCEAU_MAX, "morceaux": [m]}
    (d / o.INDEX_RUN).write_text(json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sceller(d / o.INDEX_RUN)
    shutil.rmtree(tmp)
    shutil.rmtree(tmp2)
    return sha_l, index["sha256"]


def essai(nom, fn, attendu):
    try:
        r = fn()
        obtenu = "AUTORISÉ " + r["mode"] + " (" + r["chemin"] + ") appui " + r["appui"]
    except o.RefusOuverture as e:
        obtenu = "REFUS " + e.code
    except GardeArret as e:
        obtenu = "ARRÊT " + str(e)[:80]
    ok = obtenu.startswith(attendu)
    print(("CONFORME " if ok else "NON CONFORME ") + nom + " → " + obtenu[:230])
    return ok


ok = []
OUV = decision("ouvrir", "2026-11-20T12:05:00Z")
L = "2026-11-20T12:10:00Z"
APRES = t("2026-11-20T12:30:00Z")
# 1. garde seule : cas sain et refus attendus
r = monter("sain-ouvrir", decisions=[(OUV, L)])
ok.append(essai("ouvrir → reduite", lambda: o.garde_ouverture(r, "reduite", APRES), "AUTORISÉ reduite"))
ok.append(essai("ouvrir → pleine-anticipee", lambda: o.garde_ouverture(r, "pleine-anticipee", APRES), "REFUS ni-scores-ni-ouvrir"))
ok.append(essai("ouvrir → pleine (sans SCORES-T07)", lambda: o.garde_ouverture(r, "pleine", APRES), "REFUS ligne-absente"))
ok.append(essai("ouvrir, instant égal à la ligne", lambda: o.garde_ouverture(r, "reduite", t(L)), "REFUS date-posterieure"))
r = monter("sans-ecrits", ecrits=False, decisions=[(OUV, L)])
ok.append(essai("trois écrits absents", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ligne-absente"))
r = monter("maintenir", decisions=[(decision("maintenir", "2026-11-20T12:05:00Z"), L)])
ok.append(essai("maintenir → reduite", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS decision-maintenir"))
r = monter("pleinement", decisions=[(decision("ouvrir pleinement", "2026-11-20T12:05:00Z"), L)])
ok.append(essai("ouvrir pleinement → pleine-anticipee", lambda: o.garde_ouverture(r, "pleine-anticipee", APRES), "AUTORISÉ pleine-anticipee"))
ok.append(essai("ouvrir pleinement → reduite", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ni-scores-ni-ouvrir"))
r = monter("avant-midi", decisions=[(decision("ouvrir", "2026-11-20T11:59:59Z"), L)])
ok.append(essai("Date avant 12:00:00Z", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ligne-mal-formee"))
r = monter("apres-ligne", decisions=[(decision("ouvrir", "2026-11-20T12:10:01Z"), L)])
ok.append(essai("Date après sa ligne", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ligne-mal-formee"))
r = monter("insecable", decisions=[(decision("ouvrir", "2026-11-20T12:05:00Z", espace=" "), L)])
ok.append(essai("espace insécable avant « : »", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ligne-mal-formee"))
r = monter("majuscule", decisions=[(decision("Ouvrir", "2026-11-20T12:05:00Z"), L)])
ok.append(essai("« Ouvrir » avec majuscule", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS ligne-mal-formee"))
r = monter("date-midi-pile", decisions=[(decision("ouvrir", "2026-11-20T12:00:00Z"), "2026-11-20T12:00:00Z")])
ok.append(essai("Date et ligne à 12:00:00Z pile", lambda: o.garde_ouverture(r, "reduite", t("2026-11-20T12:00:01Z")), "AUTORISÉ reduite"))
r = monter("garde-tardive", decisions=[(OUV, L)], t07_dates=("2026-11-11T07:11:42Z", "2026-11-20T12:10:00Z"))
ok.append(essai("garde adaptée datée à la ligne « ouvrir »", lambda: o.garde_ouverture(r, "reduite", APRES), "REFUS garde-adaptee-posterieure"))

# 2. ouverture réduite de bout en bout (paquets factices), journal, exposer-issue
r = monter("bout-en-bout", decisions=[(OUV, L)])
p = B / "paquets-factices"
sha_l, sha_r = fabriquer_paquets(p)
sortie = B / "espace-ferme" / "paquets-ouverts"
if sortie.parent.exists():
    shutil.rmtree(sortie.parent)
sortie.parent.mkdir(parents=True)
g = o.ouvrir(r, "reduite", RUN, sortie, racine_paquets=p, date_paquet="2026-11-13T15:45:00Z", instant=APRES,
             imprimer=lambda x: print("    sortie de ouvrir : " + x))
journal = (r / o.JOURNAL_OUVERTURES).read_text(encoding="utf-8")
print("    journal :\n" + "".join("      " + x + "\n" for x in journal.splitlines()))
ok.append(journal.splitlines()[2].startswith("| OUVERTURE-P3BIS | 2026-11-20T12:30:00Z | reduite | RENDEZ-VOUS-P3BIS-1=")
          and f"| {sha_l} {sha_r} | - |" in journal)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + "ligne OUVERTURE-P3BIS au format attendu")
ok.append(len(g["reserves"]) == 3)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"trois réserves « écrit après la lecture fermée » : {g['reserves']}")
fichiers = sorted(str(x.relative_to(sortie)) for x in sortie.rglob("*") if x.is_file())
print("    extraits : " + ", ".join(fichiers))
# fichier d'issue écrit par le « lecteur » (factice), scellé par la « mère », exposé par le module
verdict = B / "espace-ferme" / "verdict-ferme" / "verdict-P3-bis-v1.md"
verdict.parent.mkdir(parents=True)
verdict.write_text("verdict factice\n", encoding="utf-8")
import hashlib  # noqa: E402
issue = {"issue": "vu", "ligne": 4, "verdict": "docs/verdicts/verdict-P3-bis-v1.md",
         "verdict_sha256": hashlib.sha256(verdict.read_bytes()).hexdigest()}
fi = r / "docs/verdicts/verdict-P3-bis-v1-issue.json"
fi.write_text(json.dumps(issue, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
sceller(fi)
cmd = [sys.executable, "-B", "-m", "controle_ia.premier_test_ia.ouverture_p3bis_v3", "exposer-issue", str(fi),
       "--lecture-p3bis", str(sortie / f"diag/{RLC}/lecture-p3bis.json")]
pr = subprocess.run(cmd, capture_output=True, text=True, env={"PYTHONPATH": sys.argv[2], "PATH": "/usr/bin:/bin"})
print(f"    exposer-issue : code {pr.returncode}, sortie {pr.stdout.strip()!r}, erreurs {pr.stderr.strip()[:200]!r}")
ok.append(pr.returncode == 0 and json.loads(pr.stdout) == {"issue": "vu", "ligne": 4})
print(("CONFORME " if ok[-1] else "NON CONFORME ") + "exposer-issue n'affiche que issue et ligne")
# 3. seconde tentative après l'ouverture réduite : reduite refusée (deja-ouverte), ligne de refus écrite
ok.append(essai("seconde reduite après une reduite", lambda: o.ouvrir(r, "reduite", RUN, B / "espace-ferme" / "x",
                                                                         racine_paquets=p, date_paquet="2026-11-13T15:45:00Z",
                                                                         instant=APRES + 60, imprimer=lambda x: None),
                "REFUS deja-ouverte"))
print("    dernière ligne : " + (r / o.JOURNAL_OUVERTURES).read_text(encoding="utf-8").splitlines()[-1][:160])
# 4. « ouvrir pleinement » après « ouvrir » et l'ouverture réduite : pleine-anticipee, mêmes paquets
dec2 = r / "docs/decisions/rendez-vous-P3-bis-v2.md"
dec2.write_text(decision("ouvrir pleinement", "2026-11-21T09:00:00Z").replace("n° 1", "n° 2").replace(
    "RENDEZ-VOUS-P3BIS-1", "RENDEZ-VOUS-P3BIS-2"), encoding="utf-8")
with open(r / "registres/prealables-p3bis-v1.md", "a", encoding="utf-8") as f:
    f.write(f"| RENDEZ-VOUS-P3BIS-2 | 2026-11-21T09:01:00Z | docs/decisions/rendez-vous-P3-bis-v2.md | {sceller(dec2)} |\n")
ok.append(essai("ouvrir pleinement après ouvrir + reduite", lambda: o.ouvrir(
    r, "pleine-anticipee", RUN, B / "espace-ferme" / "complement", racine_paquets=p, date_paquet="2026-11-13T15:45:00Z",
    instant=t("2026-11-21T09:05:00Z"), imprimer=lambda x: print("    sortie de ouvrir : " + x)), "AUTORISÉ pleine-anticipee"))
print("    dernière ligne : " + (r / o.JOURNAL_OUVERTURES).read_text(encoding="utf-8").splitlines()[-1][:200])
# 5. ligne de commande réelle (horloge du jour, avant le rendez-vous) : refus date-posterieure, code 2, ligne au journal
r = monter("ligne-de-commande", decisions=[(OUV, L)])
pr = subprocess.run([sys.executable, "-B", "-m", "controle_ia.premier_test_ia.ouverture_p3bis_v3", "ouvrir", "--mode",
                     "reduite", "--run", RUN, "--racine", str(r), "--racine-paquets", str(p), "--sortie",
                     str(B / "espace-ferme" / "cli")], capture_output=True, text=True,
                    env={"PYTHONPATH": sys.argv[2], "PATH": "/usr/bin:/bin"})
print(f"    ligne de commande : code {pr.returncode} ; erreurs {pr.stderr.strip()[:200]!r}")
ok.append(pr.returncode == 2 and "date-posterieure" in pr.stderr)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + "appel en ligne de commande : refus code 2, motif date-posterieure")
print("    journal : " + (r / o.JOURNAL_OUVERTURES).read_text(encoding="utf-8").splitlines()[-1][:200])

# 6. contrôle à blanc sur copie (`controle_prealables_p3bis_v1.py`, à côté de ce script) : il imprime les lignes exactes et
#    rejoue la garde sur une copie, sans rien écrire dans la racine
CONTROLE = Path(__file__).resolve().parent / "controle_prealables_p3bis_v1.py"
brouillons = B / "brouillons"
brouillons.mkdir(exist_ok=True)
(brouillons / "ouvrir.md").write_text(OUV, encoding="utf-8")
(brouillons / "ouvrir-insecable.md").write_text(decision("ouvrir", "2026-11-20T12:05:00Z", espace=" "), encoding="utf-8")


def controle(nom, racine, *args):
    avant = {x: x.read_bytes() for x in racine.rglob("*") if x.is_file()}
    pr = subprocess.run([sys.executable, "-B", str(CONTROLE), "--racine", str(racine), "--bac", str(B / "controles" / nom),
                         *args], capture_output=True, text=True, env={"PYTHONPATH": sys.argv[2], "PATH": "/usr/bin:/bin"})
    apres = {x: x.read_bytes() for x in racine.rglob("*") if x.is_file()}
    return pr.returncode, pr.stdout + pr.stderr, avant == apres


r = monter("controle-sans-ecrits", ecrits=False)
c, sortie_c, intacte = controle("h1", r, "--mode", "reduite", "--ecrits", "2026-11-14T09:00:00Z")
lignes = [x for x in sortie_c.splitlines() if x.startswith("LIGNE À INSCRIRE")]
ok.append(c == 2 and "REFUS ni-scores-ni-ouvrir" in sortie_c and len(lignes) == 3 and intacte)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"contrôle à blanc, écrits seuls : code {c}, 3 lignes imprimées, "
      f"refus attendu (aucune décision), racine intacte {intacte}")
for x in lignes:
    print("    " + x)
c, sortie_c, intacte = controle("h2", r, "--mode", "reduite", "--ecrits", "2026-11-14T09:00:00Z", "--decision",
                                str(brouillons / "ouvrir.md"), "--date-ligne", "2026-11-20T12:10:00Z")
ok.append(c == 0 and "AUTORISÉ reduite" in sortie_c and intacte)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"contrôle à blanc, écrits et décision « ouvrir » : code {c}, "
      f"racine intacte {intacte}")
print("    " + next((x for x in sortie_c.splitlines() if x.startswith("LIGNE À INSCRIRE") and "RENDEZ-VOUS-P3BIS-" in x), "(aucune ligne de rendez-vous imprimée)"))
c, sortie_c, intacte = controle("h3", r, "--mode", "reduite", "--ecrits", "2026-11-14T09:00:00Z", "--decision",
                                str(brouillons / "ouvrir-insecable.md"), "--date-ligne", "2026-11-20T12:10:00Z")
ok.append(c == 2 and "REFUS ligne-mal-formee" in sortie_c and intacte)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"contrôle à blanc, décision à espace insécable : code {c}, refus "
      f"ligne-mal-formee, racine intacte {intacte}")
r = monter("controle-avec-ecrits")
c, sortie_c, intacte = controle("h4", r, "--mode", "pleine-anticipee", "--decision", str(brouillons / "ouvrir.md"),
                                "--date-ligne", "2026-11-20T12:10:00Z")
ok.append(c == 2 and "REFUS ni-scores-ni-ouvrir" in sortie_c and intacte)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"contrôle à blanc, « ouvrir » et mode pleine-anticipee : code {c}, "
      f"refus ni-scores-ni-ouvrir, racine intacte {intacte}")
c, sortie_c, intacte = controle("h5", r, "--mode", "reduite", "--ecrits", "2026-11-14T09:00:00Z")
ok.append(c == 2 and "REFUS ligne-double" in sortie_c and intacte)
print(("CONFORME " if ok[-1] else "NON CONFORME ") + f"contrôle à blanc, écrits déjà inscrits puis réinscrits : code {c}, "
      f"refus ligne-double, racine intacte {intacte}")
print(f"BILAN : {sum(ok)} conformes sur {len(ok)}")
sys.exit(0 if all(ok) else 1)
