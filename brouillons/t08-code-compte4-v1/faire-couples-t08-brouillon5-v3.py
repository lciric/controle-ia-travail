"""Version 3 (remplace la version 2, `faire-couples-t08-brouillon5-v2.py`, gardée, jamais appliquée) : ajoute le couple T5-19
(point 1 du plan : sorties et manifeste de la course de T0.8 elle-même, VCT8B-01, soumis à la session mère) et le dit dans
l'en-tête et la relecture prévue. Version 2 : deux passes de corrections et deux vérifications citées. Écrit les couples du brouillon 5 (candidat) de T0.8 sur le brouillon 4 gelé
(R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon5-v3.py PARAMETRES_JSON SORTIE_JSON
PARAMETRES_JSON : {"date": "AAAA-MM-JJ", "heure": "HH:MM" (relevées par `date -u`), "commit": 40 caractères,
  "piece_empreintes": chemin, "sha_piece": 64, "n_fichiers": entier,
  "rapport_corrections": chemin, "sha_rapport_corrections": 64,
  "verification": chemin, "sha_verification": 64, "verdict_verification": texte,
  "rapport_corrections_2": chemin, "sha_rapport_corrections_2": 64,
  "verification_2": chemin, "sha_verification_2": 64, "verdict_verification_2": texte}
Chaque chemin est vérifié sur disque contre son empreinte. Couples de l'auteur du brouillon 5 (session du compte 4,
modèle A ; modèles notés sans identifiant, R-2598, R-2605) : marqueur `COMMIT_CODE_T08` rempli, en-tête, entrées de
relecture, identifiants de modèles ; aucune autre ligne.
"""
import hashlib, json, re, sys
from pathlib import Path

B4 = "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5"
CL_CODE = ("brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1.md", "7c47e18266a970abafb33335c5a0f7f9e768820a833e017aebc5bcec4b76d280")
RAPPORT_DEV = ("docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md", "5b1e873198f38c6b1725355c18212f9b889597071f7820d82f9f12b058c1a5cc")
JOURNAL_CHOIX = ("registres-provisoires/compte-4-2026-11-14-v3.md", "2f338351643350c502a43ceba163696e855d2cb103c72719eae91c35ef756c5d")
JOURNAL_CHOIX_2 = ("registres-provisoires/compte-4-2026-11-14-v6.md", "4029099988dddb13150d69fa2c77fb60d57a846b84c9f2e4774d60b6e06855b6")
VT3C = ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md", "ced3b43eb21dd201c09fa912d9855295b048d3bdb015fd0a09269458b0d1809e")
B3 = "947994e4487d2d2b01b7e8e01d5fb17f75c178b846aea5546b4bd8da78effdc1"
M = "<<" + "COMMIT_CODE_T08" + ">>"
ARBRE = "/home/user/t08-code-compte4-v1/"

def rel(x):
    """Chemin cité dans le texte : relatif à la racine de la branche pour un fichier de l'arbre de la branche."""
    return x[len(ARBRE):] if x.startswith(ARBRE) else x

def verifier(chemin, sha):
    if not re.fullmatch(r"[0-9a-f]{64}", sha) or hashlib.sha256(Path(chemin).read_bytes()).hexdigest() != sha:
        sys.exit(f"ARRÊT : empreinte de {chemin} différente ou mal formée")

def couples(p):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    d, h, k = p["date"], p["heure"], p["commit"]
    a("T5-01", "base (A) de la règle « mots et coût » par renvoi au texte scellé à part) — v1 — brouillon 4",
      "base (A) de la règle « mots et coût » par renvoi au texte scellé à part) — v1 — brouillon 5 (candidat)")
    a("T5-02", "- **Statut** : **brouillon 4**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 4 applique",
      f"- **Statut** : **brouillon 5 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 5 est écrit sur le "
      f"brouillon 4 gelé (`{B4}`, R-2251) par couples versés (script `brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon5-v1.py`) : "
      "il remplit le seul marqueur `COMMIT_CODE_T08`, après contre-lecture du code, corrections et essai sur le modèle jouet (section "
      "« Contre-lecture ») ; il note les modèles « modèle A » et « modèle B », sans identifiant (R-2598, R-2605) ; il ajoute les "
      "entrées de relecture ; il ajoute **une phrase au point 1 du plan d'analyse** (sorties et manifeste de la course de T0.8 "
      "elle-même, que la lecture lit ; VCT8B-01), **soumise à la session mère** (section gelée du brouillon 4) ; aucune autre "
      "ligne ne change ; six marqueurs restent, à la session mère et à Lazar ; le renvoi au "
      "texte de validité de l'adaptateur reste au brouillon 3, ce texte n'étant pas scellé (section « Les surveillants », « Renvoi ») ; "
      "depuis, ce texte ne crée la pièce HD que si P3-bis rend « vu » (R-2604) : sinon le point 8 bis, (2), rend « non lue (sorties "
      "de la pièce HD absentes) », sans changement de ce texte ; **non scellable avant la vérification courte du différentiel du "
      "brouillon 4 au brouillon 5** et avant les six marqueurs. Le brouillon 4 applique")
    a("T5-03", "(Fable 5.2, « gelable après corrections » ;", "(modèle B, « gelable après corrections » ;")
    a("T5-04", "(contre-lecture 1, Fable 5.2 : ses 44 couples", "(contre-lecture 1, modèle B : ses 44 couples")
    a("T5-05", "(vérification courte du brouillon 2, Fable 5.2, « gelable", "(vérification courte du brouillon 2, modèle B, « gelable")
    a("T5-06", "- **Marqueurs restants** (sept, une occurrence chacun, inchangés au brouillon 3 ; section « Marqueurs à remplir avant le scellement ») : `COMMIT_CODE_T08`, `CODE_MOTS_ET_COUT_T06`,",
      "- **Marqueurs restants** (six, une occurrence chacun ; `COMMIT_CODE_T08` rempli au brouillon 5 ; section « Marqueurs à remplir avant le scellement ») : `CODE_MOTS_ET_COUT_T06`,")
    a("T5-07", "(Claude Opus 5.5), qui n'a écrit ni T0.6", "(modèle A), qui n'a écrit ni T0.6")
    a("T5-08", "(Claude Opus 5.5), qui n'a écrit ni le brouillon 1", "(modèle A), qui n'a écrit ni le brouillon 1")
    a("T5-09", "qui n'a écrit ni la vérification courte du brouillon 2, ni le texte de validité de l'adaptateur.",
      "qui n'a écrit ni la vérification courte du brouillon 2, ni le texte de validité de l'adaptateur ; **brouillon 5 (candidat)**, "
      "la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`), modèle A, qui n'a écrit ni les brouillons 1 à 4 ni leurs "
      "relectures, ni la base (A), ni T0.6 ou P3-bis, ni le code de T0.8 (écrit par des développeurs neufs, sous-agents de cette "
      "session) ni sa contre-lecture ; elle a écrit des brouillons du texte de validité de l'adaptateur et lu T0.7 scellé : exclue "
      "de la lecture et du verdict de T0.8 et de P3-bis.")
    a("T5-10", "- **Date (UTC)** : brouillon 1 écrit le 2026-11-10 à partir de 10:04 UTC ;",
      f"- **Date (UTC)** : brouillon 5 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 1 écrit le 2026-11-10 à partir de 10:04 UTC ;")
    a("T5-11", f"- **Commit du code d'analyse** : `{M}` — code de la course et de la lecture de T0.8, **à écrire** (aucune ligne n'en existe) ; cité par la ligne `CODE-T08` du registre des scellements avant toute exécution.",
      f"- **Commit du code d'analyse** : `{k}` — code de la course et de la lecture de T0.8 (`src/controle_ia/t08/`, essais "
      "`tests/test_t08_*_v1.py`), branche `prep/t08-code-compte4-v1` (tirée de `main` à `ee7f2f9c`) ; empreintes de ses "
      f"{p['n_fichiers']} fichiers : `{p['piece_empreintes']}`, `{p['sha_piece']}` ; écrit sur données factices par des développeurs "
      "neufs (modèle A), contre-lu et vérifié (modèle B) et éprouvé par l'essai de bout en bout sur le modèle jouet (section « Contre-lecture ») ; "
      "cité par la ligne `CODE-T08` du registre des scellements avant toute exécution.")
    a("T5-12", "| 10 nov. | contre-lecteur neuf, d'un autre modèle que l'auteur (Fable 5.2) ; session mère |",
      "| 10 nov. | contre-lecteur neuf, d'un autre modèle que l'auteur (modèle B) ; session mère |")
    a("T5-13", "| 10 nov. | vérificateur neuf (Fable 5.2) ; même rédacteur |", "| 10 nov. | vérificateur neuf (modèle B) ; même rédacteur |")
    a("T5-14", "Claude Fable 5.2 (`claude-fable-5-2`, d'après son environnement ; autre modèle de la même famille que l'auteur du brouillon 1, Opus 5.5 ; N-052 nomme Fable 5.1 : écart déclaré par le contre-lecteur)",
      "modèle B (d'après son environnement ; autre modèle de la même famille que l'auteur du brouillon 1, modèle A ; N-052 nomme une autre version de ce modèle : écart déclaré par le contre-lecteur)")
    a("T5-15", "Claude Fable 5.2 (`claude-fable-5-2`, d'après son environnement ; autre modèle que le rédacteur, Opus 5.5)",
      "modèle B (d'après son environnement ; autre modèle que le rédacteur, modèle A)")
    a("T5-16", "**Relecture suivante, prévue avant le scellement** (R-2245) : vérification courte du différentiel du brouillon 2 au brouillon 3",
      f"- **Contre-lecture 3** — vérification courte en différentiel du brouillon 3, sous-agent neuf de la session mère "
      "`session_01VJdZpSMxSdk2SJ1ScmdfNv`, modèle B, autre modèle que le rédacteur (modèle A) ; n'a écrit ni T0.8, ni ses "
      f"contre-lectures, ni la base (A), ni le texte de validité de l'adaptateur ; n'a lu aucun fichier de T0.7. **Brouillon relu** : "
      f"`brouillons/T0.8-bases-boite-noire-v0-v1-brouillon3.md`, `{B3}`. **Rapport** : `{VT3C[0]}`, `{VT3C[1]}` (égale à son "
      "compagnon, vérifiée par l'auteur du brouillon 5). **Verdict** : « gelable après corrections » ; 11 couples VT3C-01 à VT3C-11. "
      "**Traitement** : les 11 couples appliqués par programme, tels qu'écrits, au brouillon 4 (script et couples du brouillon 4, "
      "en-tête) ; décision de la session mère R-2250 (VT3-05) ; brouillon 4 gelé (R-2251).\n\n"
      f"- **Contre-lecture du code de T0.8** (R2 ; plan, point 10) — sous-agent neuf de la session du compte 4, modèle B, qui n'a "
      "écrit ni ce code, ni ce texte, ni la base (A), ni T0.6, T0.7 ou P3-bis, et n'a lu ni T0.7, ni P3-bis, ni le registre. "
      f"**Code relu** : commit `27c092642247e01f57ea3f80ec9ccd29f5798557` de `prep/t08-code-compte4-v1` ; rapport du premier "
      f"développeur `{RAPPORT_DEV[0]}` (dans la branche), `{RAPPORT_DEV[1]}`. **Rapport** : `{CL_CODE[0]}`, `{CL_CODE[1]}`. "
      "**Verdict** : « autorisable après les corrections listées » ; 3 bloquants, 8 majeurs, 10 mineurs (CLT8C-01 à CLT8C-21) ; "
      "phrases gelées des tables D et F égales au texte ; aucune fuite de `cibles`. **Traitement** : les 21 constats corrigés "
      "(modèle A) par un développeur des corrections, arrêté par un redémarrage du conteneur après un premier jalon, puis par un "
      "développeur de reprise, selon les choix de la session du compte 4 sur les options du lecteur, tous à la lettre de ce texte "
      f"(journal du compte 4, C4-0030, `{JOURNAL_CHOIX[0]}`, `{JOURNAL_CHOIX[1]}`) : rapport `{rel(p['rapport_corrections'])}` (dans la "
      f"branche), `{p['sha_rapport_corrections']}` ; vérification courte des corrections (modèle B) : `{p['verification']}`, "
      f"`{p['sha_verification']}`, « {p['verdict_verification']} » ; seconde passe (VCT8-01 à VCT8-07, choix C4-0037, "
      f"`{JOURNAL_CHOIX_2[0]}`, `{JOURNAL_CHOIX_2[1]}`) par un développeur neuf (modèle A) : rapport `{rel(p['rapport_corrections_2'])}` "
      f"(dans la branche), `{p['sha_rapport_corrections_2']}` ; vérification de la seconde passe (modèle B) : `{p['verification_2']}`, "
      f"`{p['sha_verification_2']}`, « {p['verdict_verification_2']} ».\n\n"
      "**Relecture du brouillon 3 (faite : contre-lecture 3)**, prévue alors (R-2245) : vérification courte du différentiel du brouillon 2 au brouillon 3")
    a("T5-17", "traitement de chaque remarque (accepté, refusé et pourquoi).\n\n## Marqueurs à remplir avant le scellement",
      "traitement de chaque remarque (accepté, refusé et pourquoi).\n\n"
      "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 4 au brouillon 5 par un "
      "sous-agent neuf, d'un autre modèle que l'auteur du brouillon 5 (modèle A), qui n'a écrit ni ce texte, ni la base (A), ni le "
      "code de T0.8, ni sa contre-lecture, n'a vu aucun résultat de 7b, de la pièce HD ni de sonde, et ne lit ni T0.7 ni P3-bis ; "
      "fichiers à lui donner : ce brouillon, le brouillon 4 gelé, le script et les couples du brouillon 5, la pièce des empreintes "
      "du code, les rapports de la contre-lecture du code, des corrections et de leur vérification ; points à viser : aucun "
      "changement hors du marqueur rempli, de l'en-tête, des entrées de relecture, des identifiants de modèles et de la phrase "
      "ajoutée au point 1 (sa portée : aucune donnée de 7b, aucune sonde, aucun résultat) ; aucun signe, "
      "seuil ni critère de lecture neuf ; le commit cité égal à celui de la pièce des empreintes. Son entrée, avec ses deux "
      "empreintes, s'ajoute à cette section dans le texte qui suit.\n\n## Marqueurs à remplir avant le scellement")
    a("T5-19", "   - **jamais** : `lecture-sondes-t06.json` de quelque run que ce soit,",
      "   - de la course de T0.8 elle-même, pour la lecture seulement : ses sorties scellées (`diag/<run-t08>/course-t08.json` "
      "et les fichiers qu'il cite sous `donnees/<run-t08>/`) et son manifeste (`runs/<run-t08>/manifeste.json`, pour sa seule "
      "date de création : antériorité des lignes `SCELLEMENT-T08` et `CODE-T08` sur le début de la course, « avant toute "
      "exécution », en-tête), empreintes vérifiées contre leurs compagnons ; aucune donnée de 7b, aucune sonde, aucun résultat "
      "n'en est tiré au-delà de ce que nomment le plan et la « Métrique » (phrase ajoutée au brouillon 5, VCT8B-01, soumise à "
      "la session mère) ;\n   - **jamais** : `lecture-sondes-t06.json` de quelque run que ce soit,")
    a("T5-18", "**Remplis au brouillon 2** : `DECISIONS_LAZAR_T08`",
      "**Rempli au brouillon 5** : `COMMIT_CODE_T08` (commit du code et pièce de ses empreintes, en-tête). **Remplis au brouillon 2** : `DECISIONS_LAZAR_T08`")
    return c

def principal():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    p, sortie = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")), Path(sys.argv[2])
    attendu = {"date", "heure", "commit", "piece_empreintes", "sha_piece", "n_fichiers", "rapport_corrections",
               "sha_rapport_corrections", "verification", "sha_verification", "verdict_verification",
               "rapport_corrections_2", "sha_rapport_corrections_2", "verification_2", "sha_verification_2",
               "verdict_verification_2"}
    if set(p) != attendu:
        sys.exit(f"ARRÊT : clés des paramètres {sorted(set(p) ^ attendu)}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["date"]) or not re.fullmatch(r"\d{2}:\d{2}", p["heure"]):
        sys.exit("ARRÊT : date AAAA-MM-JJ et heure HH:MM attendues")
    if not re.fullmatch(r"[0-9a-f]{40}", p["commit"]) or not isinstance(p["n_fichiers"], int) or p["n_fichiers"] < 1:
        sys.exit("ARRÊT : commit complet ou nombre de fichiers mal formé")
    for x in (p["verdict_verification"], p["verdict_verification_2"]):
        if not x.strip() or "<<" in x:
            sys.exit("ARRÊT : verdict de la vérification vide ou marqué")
    verifier(p["piece_empreintes"], p["sha_piece"])
    if p["commit"] not in Path(p["piece_empreintes"]).read_text(encoding="utf-8"):
        sys.exit("ARRÊT : le commit cité n'est pas celui de la pièce des empreintes")
    verifier(p["rapport_corrections"], p["sha_rapport_corrections"])
    verifier(p["verification"], p["sha_verification"])
    verifier(p["rapport_corrections_2"], p["sha_rapport_corrections_2"])
    verifier(p["verification_2"], p["sha_verification_2"])
    for ch, sha in (CL_CODE, JOURNAL_CHOIX, JOURNAL_CHOIX_2, VT3C):
        verifier(ch, sha)
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples(p)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

principal()
