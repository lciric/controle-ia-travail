"""Écrit les couples du brouillon 9 (candidat) de T0.8 sur le brouillon 8 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon9-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- reprend, tels qu'écrits et dans leur ordre, les trois couples VT8C-01 à VT8C-03 de la vérification courte du brouillon 8,
  après contrôle de l'empreinte du rapport (bloc JSON de sa section « 3. Couples ») ;
- ajoute les couples de l'auteur (session du compte 4, modèle A) : VT8-04 (déclaration de vue : rapports lus nommés ; section
  « Devis de la confirmation 7b » ; renvoi dans « Ce que les auteurs savaient avant le scellement ») ; VT8-05 (sort de VT5-07
  porté au marqueur de la mère) ; VT8-06 (« (ii-b) » défini) ; entrée « Contre-lecture 6 » ; relecture suivante ; en-tête.
"""
import hashlib, json, re, sys
from pathlib import Path

B8 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon8.md")
SHA_B8 = "129b1db245e186040256c8630dfb585bcd2a1e1ab4ea7b8ff817696fbd3220a7"
RAPPORT = Path("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon8-verification-courte-v1.md")
SHA_RAPPORT = "220fe2fd8fedef8a06626e22f630fdd916f58675d5c441473be9c62dcca7b6fc"
SCRIPT_CL6 = ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon8-verification-courte-v1-calcul.py",
              "c738299edb8c720ad78f3dc626ab986b7adf6f5fcfab2d6ef160ab1b7f6ca266")
PRIS = ["VT8C-01", "VT8C-02", "VT8C-03"]
SCRIPT = "brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon9-v1.py"
COUPLES = "brouillons/t08-code-compte4-v1/couples-t08-brouillon9-v1.json"


def couples_verificateur():
    for ch, s in ((B8, SHA_B8), (RAPPORT, SHA_RAPPORT), (Path(SCRIPT_CL6[0]), SCRIPT_CL6[1])):
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    if [c["id"] for c in tous] != PRIS:
        sys.exit("ARRÊT : couples du vérificateur autres que VT8C-01 à VT8C-03")
    return [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in tous]


def fin_section_savaient():
    t = B8.read_text(encoding="utf-8")
    i = t.index("\n## Ce que les auteurs savaient avant le scellement\n")
    j = t.index("\n\n## Les surveillants\n", i)
    derniere = t[:j].rsplit("\n", 1)[1]
    ancien = derniere + "\n\n## Les surveillants\n"
    if t.count(ancien) != 1 or not derniere.strip():
        sys.exit("ARRÊT : fin de la section « Ce que les auteurs savaient avant le scellement » introuvable ou multiple")
    return derniere, ancien


def couples_auteur(d, h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("T9-01", "— v1 — brouillon 8 (candidat)", "— v1 — brouillon 9 (candidat)")
    a("T9-02", "- **Statut** : **brouillon 8 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 8 applique",
      "- **Statut** : **brouillon 9 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 9 applique par "
      "programme, tels qu'écrits, les trois couples VT8C-01 à VT8C-03 de la vérification courte du différentiel du brouillon 6 au "
      f"brouillon 8 (modèle B, « conforme après les corrections listées » ; `{RAPPORT}`, `{SHA_RAPPORT}`) et les couples de son auteur : "
      "déclaration de vue complétée (VT8-04) ; sort de VT5-07 porté au marqueur `LIGNE_MOT_LAZAR_T5_19` (VT8-05) ; « (ii-b) » défini "
      "(VT8-06) ; entrée « Contre-lecture 6 » et relecture suivante (section « Contre-lecture ») ; renvoi à la déclaration de vue dans "
      "« Ce que les auteurs savaient avant le scellement » ; titre, « Auteurs », « Date » ; script "
      f"`{SCRIPT}`, couples `{COUPLES}` ; aucune autre ligne ne change, aucune section de « Hypothèse » à « Liste d'arrêt » ; **non "
      "scellable avant la vérification courte du différentiel du brouillon 8 au brouillon 9, le marqueur `LIGNE_MOT_LAZAR_T5_19` et "
      "les six autres marqueurs**. Le brouillon 8 applique")
    a("T9-03", "les messages de commit de `main`, les seules sorties **factices** des essais jouets du code de T0.8 et de celui de (ii-b), et, "
      "pour (ii-b), des extraits de sa conception,",
      "les rapports de la contre-lecture du code de T0.8, de ses deux vérifications de corrections et des vérifications courtes des "
      "brouillons 5, 6 et 8 de ce texte (tous sur données factices ou sur des textes), les messages de commit de `main`, les seules "
      "sorties **factices** des essais jouets du code de T0.8 et de celui de (ii-b) — l'organisme exploratoire « saboteur à budget » "
      "de la session mère, dont le code est écrit et éprouvé sur données factices et dont aucune course n'est lancée —, et, pour "
      "(ii-b), des extraits de sa conception,")
    a("T9-04", "(chemins de fichiers et phrases de sa conception).",
      "(chemins de fichiers et phrases de sa conception) ; aucune de ces pièces ne lui a montré de résultat de 7a, de 7b, de la pièce "
      "HD ni de sonde. La section « Devis de la confirmation 7b » de T0.6 n'est dite lue par aucun journal du compte 4 ; ce texte en "
      "cite, depuis un brouillon antérieur à elle, les heures de 7a (« Calendrier »).")
    derniere, ancien = fin_section_savaient()
    a("T9-05", ancien,
      derniere + "\n- **Auteur des brouillons 5 à 9** (session du compte 4, modèle A) : sa déclaration de vue est écrite en tête, "
      "ligne « Auteurs » (« Ce qu'elle a vu avant le scellement » ; VT5-04, VT6-03, VT8-04).\n\n## Les surveillants\n")
    a("T9-06", "plus stricts que ce texte (contre-lecture du code, traitement) | avant le scellement, avant `GEL-T08` | session mère |",
      "plus stricts que ce texte (contre-lecture du code, traitement) ; et ce qu'il en est de VT5-07 (arrêt d'antériorité que la "
      "« Liste d'arrêt » ne nomme pas ; le mot de Lazar recopié ne porte que sur T5-19 : VT5-07 couvert par lui, ou porté à part) "
      "| avant le scellement, avant `GEL-T08` | session mère |")
    a("T9-07", "elle s'écrit au remplissage de `LIGNE_MOT_LAZAR_T5_19`).",
      "elle s'écrit au remplissage de `LIGNE_MOT_LAZAR_T5_19`).\n\n"
      "- **Contre-lecture 6** — vérification courte en différentiel du brouillon 6 au brouillon 8 (couples des brouillons 7 et 8), "
      "sous-agent neuf de la session du compte 4, modèle B (vérifié par l'auteur comme aux contre-lectures 4 et 5), autre modèle que "
      "l'auteur (modèle A) ; n'a écrit ni T0.8, ni la base (A), ni le code de T0.8, ni les relectures précédentes ; n'a lu ni T0.7, ni "
      "P3-bis, ni `registres/`, ni aucune pièce de (ii-b) ; n'a vu aucun résultat de 7b, de la pièce HD ni de sonde. **Brouillon relu** : "
      f"`{B8}`, `{SHA_B8}`. **Rapport** : `{RAPPORT}`, `{SHA_RAPPORT}` ; script `{SCRIPT_CL6[0]}`, `{SCRIPT_CL6[1]}`. **Verdict** : "
      "« conforme après les corrections listées » ; 0 bloquant, 0 majeur, 6 mineurs ; rejeux à l'octet (brouillons 7 et 8, et les "
      "couples des deux scripts) ; sections gelées égales au brouillon 4, « Plan d'analyse » hors la seule ligne de T5-19 ; mot de "
      "Lazar recopié à l'identique, lu comme l'option (a) et rien de plus, sans effet avant son inscription. **Traitement** : "
      "VT8C-01 à VT8C-03 appliqués tels qu'écrits (VT8-01 à VT8-03) ; VT8-04 : rapports lus nommés, section « Devis de la "
      "confirmation 7b » dite, renvoi ajouté dans « Ce que les auteurs savaient avant le scellement » ; VT8-05 : sort de VT5-07 porté "
      "au marqueur `LIGNE_MOT_LAZAR_T5_19` ; VT8-06 : « (ii-b) » défini, et dit sans résultat de 7a, de 7b, de la pièce HD ni de sonde. "
      "Écart déclaré par le vérificateur : un journal du compte 4 (version 10) empreinté sans être lu.")
    a("T9-08", "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 6 au brouillon 8 "
      "(couples du brouillon 7 et du brouillon 8),",
      "**Relecture du brouillon 8 (faite : contre-lecture 6)**, prévue alors : vérification courte du différentiel du brouillon 6 au "
      "brouillon 8 (couples du brouillon 7 et du brouillon 8),")
    a("T9-09", "puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.",
      "puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.\n\n"
      "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 8 au brouillon 9 (trois "
      "couples du vérificateur, phrases de l'auteur sur VT8-04 à VT8-06, entrée « Contre-lecture 6 »), par un sous-agent neuf d'un "
      "autre modèle que l'auteur (modèle A), qui n'a écrit ni ce texte, ni la base (A), ni le code de T0.8, ni les relectures "
      "précédentes, et n'a vu aucun résultat de 7b, de la pièce HD ni de sonde ; son entrée s'ajoute au texte qui suit ; puis "
      "`LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.")
    a("T9-10", "**brouillons 5 à 8 (candidats)**, la session du compte 4", "**brouillons 5 à 9 (candidats)**, la session du compte 4")
    a("T9-11", "- **Date (UTC)** : brouillon 8 écrit le ",
      f"- **Date (UTC)** : brouillon 9 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 8 écrit le ")
    return c


def principal():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    d, h, sortie = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) or not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : date AAAA-MM-JJ et heure HH:MM attendues")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples_verificateur() + couples_auteur(d, h)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")


principal()
