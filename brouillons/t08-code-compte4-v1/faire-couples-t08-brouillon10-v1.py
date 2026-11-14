"""Écrit les couples du brouillon 10 (candidat) de T0.8 sur le brouillon 9 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon10-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- reprend, tels qu'écrits et dans leur ordre, les cinq couples VT9C-01 à VT9C-05 de la vérification courte du brouillon 9
  (rapport, version 2, qui fait foi), après contrôle des empreintes ; vérifie que leur seule application au brouillon 9 rend
  l'empreinte écrite par le vérificateur (`4295c539…`) ;
- ajoute les couples de l'auteur (session du compte 4, modèle A) : VT9-04 (rapports des développeurs du code de T0.8 dits lus) ;
  bornage de la déclaration de vue ; entrée « Contre-lecture 7 » ; paragraphe « Avant le scellement, après le brouillon 10 » ;
  titre, statut, « Auteurs », « Date ».
"""
import hashlib, json, re, sys
from pathlib import Path

B9 = Path("brouillons/T0.8-bases-boite-noire-v0-v1-brouillon9.md")
SHA_B9 = "dae4cc12a2e9de07d97fc8e5739c5cf5db79b98f234be30d94c52dbf72fb64ef"
RAPPORT = Path("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon9-verification-courte-v2.md")
SHA_RAPPORT = "35d9a99f006179afa95e044634f74fbdf1423667522d117b3efd86792d139c54"
RAPPORT_V1 = ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon9-verification-courte-v1.md",
              "8201890a61bf19936d7a94c6e1eddb40d055a4e6b84873bdf0dfb3d11e2ef269")
SCRIPT_CL7 = ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon9-verification-courte-v1-calcul.py",
              "9c0471e0e5079cc7e5e9ecb1d77a796fa9a8c23b9e907abc4ae31117c2e64053")
SHA_APRES_VT9C = "4295c539624b566569008ea895cacf90dca56681535a3be44e46239882fe1710"
PRIS = ["VT9C-01", "VT9C-02", "VT9C-03", "VT9C-04", "VT9C-05"]
SCRIPT = "brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon10-v1.py"
COUPLES = "brouillons/t08-code-compte4-v1/couples-t08-brouillon10-v1.json"


def couples_verificateur():
    for ch, s in ((B9, SHA_B9), (RAPPORT, SHA_RAPPORT), (Path(RAPPORT_V1[0]), RAPPORT_V1[1]), (Path(SCRIPT_CL7[0]), SCRIPT_CL7[1])):
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    if [c["id"] for c in tous] != PRIS:
        sys.exit("ARRÊT : couples du vérificateur autres que VT9C-01 à VT9C-05")
    cs = [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in tous]
    t = B9.read_text(encoding="utf-8")
    for c in cs:
        if t.count(c["ancien"]) != 1:
            sys.exit(f"ARRÊT : « ancien » de {c['id']} absent ou multiple")
        t = t.replace(c["ancien"], c["nouveau"])
    if hashlib.sha256(t.encode("utf-8")).hexdigest() != SHA_APRES_VT9C:
        sys.exit("ARRÊT : les cinq couples du vérificateur ne rendent pas l'empreinte qu'il écrit")
    return cs


def couples_auteur(d, h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("T10-01", "— v1 — brouillon 9 (candidat)", "— v1 — brouillon 10 (candidat)")
    a("T10-02", "- **Statut** : **brouillon 9 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 9 applique",
      "- **Statut** : **brouillon 10 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 10 applique "
      "par programme, tels qu'écrits, les cinq couples VT9C-01 à VT9C-05 de la vérification courte du différentiel du brouillon 8 au "
      f"brouillon 9 (modèle B, « candidat conforme » ; rapport, version 2, qui fait foi, `{RAPPORT}`, `{SHA_RAPPORT}`) et les couples "
      "de son auteur : rapports des développeurs du code de T0.8 dits lus (VT9-04) ; entrée « Contre-lecture 7 » ; paragraphe « Avant "
      "le scellement, après le brouillon 10 » ; titre, « Auteurs », « Date » ; script "
      f"`{SCRIPT}`, couples `{COUPLES}` ; aucune autre ligne ne change, aucune section de « Hypothèse » à « Liste d'arrêt » ; **candidat "
      "rendu à la session mère** : non scellable avant le marqueur `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs ; la relecture "
      "du différentiel du brouillon 9 au brouillon 10 est à sa décision. Le brouillon 9 applique")
    a("T10-03", "puis au brouillon 9, VT8-04) :", "puis au brouillon 9, VT8-04, puis au brouillon 10, VT9-04) :")
    a("T10-04", "les rapports de la contre-lecture du code de T0.8, de ses deux vérifications de corrections",
      "les rapports des trois développeurs du code de T0.8 (premier développeur, corrections, seconde passe ; journaux du compte 4, "
      "C4-0024, C4-0034, C4-0039), les rapports de la contre-lecture du code de T0.8, de ses deux vérifications de corrections")
    a("T10-05", "Écart déclaré par le vérificateur : un journal du compte 4 (version 10) empreinté sans être lu.",
      "Écart déclaré par le vérificateur : un journal du compte 4 (version 10) empreinté sans être lu.\n\n"
      "- **Contre-lecture 7** — vérification courte en différentiel du brouillon 8 au brouillon 9, sous-agent neuf de la session du "
      "compte 4, modèle B (vérifié par l'auteur comme aux contre-lectures 4 à 6), autre modèle que l'auteur (modèle A) ; n'a écrit ni "
      "T0.8, ni la base (A), ni le code de T0.8, ni les relectures précédentes ; n'a lu ni T0.7, ni P3-bis, ni `registres/`, ni aucune "
      "pièce de (ii-b) ; n'a vu aucun résultat de 7b, de la pièce HD ni de sonde. **Brouillon relu** : "
      f"`{B9}`, `{SHA_B9}`. **Rapport** (version 2, qui fait foi) : `{RAPPORT}`, `{SHA_RAPPORT}` ; version 1 gardée telle quelle, "
      f"`{RAPPORT_V1[0]}`, `{RAPPORT_V1[1]}` (elle écrivait « aucune commande git », faux d'un `git status --short` lancé hors de "
      f"l'arbre permis, sans écriture : écart déclaré à la version 2) ; script `{SCRIPT_CL7[0]}`, `{SCRIPT_CL7[1]}`. **Verdict** : "
      "« candidat conforme » ; 0 bloquant, 0 majeur, 6 mineurs ; rejeu du script et des 14 couples à l'octet ; sections gelées "
      "égales au brouillon 4 ; « Plan d'analyse » égal au brouillon 8 ; sept marqueurs. **Traitement** : VT9C-01 à VT9C-05 appliqués "
      "tels qu'écrits (VT9-01, VT9-02, VT9-03, VT9-05, VT9-06 ; leur seule application au brouillon 9 rend l'empreinte que le "
      "vérificateur écrit, contrôlée par le script) ; VT9-04 : rapports des trois développeurs du code de T0.8 dits lus, avec les "
      "entrées du journal qui les portent. Non vérifiable par le vérificateur, déclaré par lui : ce que la déclaration dit de (ii-b) "
      "hors son nom, le contenu de la section « Devis de la confirmation 7b » de T0.6, l'appui par journal des lectures des rapports "
      "du code de T0.8.")
    a("T10-06", "entrée « Contre-lecture 6 »), par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), qui n'a écrit ni ce "
      "texte, ni la base (A), ni le code de T0.8, ni les relectures précédentes, et n'a vu aucun résultat de 7b, de la pièce HD ni de "
      "sonde ; son entrée s'ajoute au texte qui suit ; puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.",
      "entrée « Contre-lecture 6 »), par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), qui n'a écrit ni ce "
      "texte, ni la base (A), ni le code de T0.8, ni les relectures précédentes, et n'a vu aucun résultat de 7b, de la pièce HD ni de "
      "sonde ; son entrée s'ajoute au texte qui suit ; puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère "
      "(faite : contre-lecture 7).\n\n"
      "**Avant le scellement, après le brouillon 10** : le différentiel du brouillon 9 au brouillon 10 se limite aux cinq couples "
      f"VT9C-01 à VT9C-05 tels qu'écrits (leur seule application au brouillon 9 rend `{SHA_APRES_VT9C}`), à la phrase de VT9-04 et au "
      "bornage de la déclaration de vue, à l'entrée « Contre-lecture 7 », à ce paragraphe et à l'en-tête ; sa relecture est à la "
      "décision de la session mère ; puis `LIGNE_MOT_LAZAR_T5_19` et les six autres marqueurs, par la session mère.")
    a("T10-07", "**brouillons 5 à 9 (candidats)**, la session du compte 4", "**brouillons 5 à 10 (candidats)**, la session du compte 4")
    a("T10-08", "- **Date (UTC)** : brouillon 9 écrit le ",
      f"- **Date (UTC)** : brouillon 10 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 9 écrit le ")
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
