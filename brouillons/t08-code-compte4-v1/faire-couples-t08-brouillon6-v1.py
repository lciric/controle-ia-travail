"""Écrit les couples du brouillon 6 (candidat) de T0.8 sur le brouillon 5 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon6-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- reprend, tels qu'écrits et dans leur ordre, les quatre couples VT5C-01 à VT5C-04 de la vérification courte du brouillon 5,
  après contrôle de l'empreinte du rapport, version 3 (bloc JSON de sa section « 3. Couples », égal à celui des versions 1 et 2) ;
- ajoute les couples de l'auteur (session du compte 4, modèle A) : T5-19 dite nœud de Lazar (VT5-03), déclaration de vue
  (VT5-04), entrée « Contre-lecture 4 », relecture suivante, en-tête.
"""
import hashlib, json, re, sys
from pathlib import Path

RAPPORT = Path("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v3.md")
SHA_RAPPORT = "f788bb73baa0d71f826d4778c2b2e2c55baa20383f2f49e777d670d849df6d7e"
REMPLACES = (("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v1.md", "0c808068f5564ada86e6ae1895a2f74e394f148aeddea8657d47b7f7b0f41c79"),
             ("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v2.md", "1dbe6533a362cad74e00b86812fe7110917b06e3c13c6c28bc78a48adac9cd91"))
B5 = "0c0e43270a819974168646406e349f48b6441d9afbdfaeb9d78b976228aba22b"
PRIS = ["VT5C-01", "VT5C-02", "VT5C-03", "VT5C-04"]

def couples_verificateur():
    sha = hashlib.sha256(RAPPORT.read_bytes()).hexdigest()
    if sha != SHA_RAPPORT:
        sys.exit(f"ARRÊT : empreinte du rapport de la vérification courte différente ({sha})")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    for ch, s in REMPLACES:
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    if [c["id"] for c in tous] != PRIS:
        sys.exit("ARRÊT : couples du vérificateur autres que VT5C-01 à VT5C-04")
    return [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in tous]

def couples_auteur(d, h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("T6-01", "— v1 — brouillon 5 (candidat)", "— v1 — brouillon 6 (candidat)")
    a("T6-02", "- **Statut** : **brouillon 5 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 5 est écrit",
      "- **Statut** : **brouillon 6 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 6 applique par "
      "programme, tels qu'écrits, les quatre couples VT5C-01 à VT5C-04 de la vérification courte du brouillon 5 (modèle B, « conforme "
      f"après les corrections listées » ; `{RAPPORT}`, `{SHA_RAPPORT}`), écrit la déclaration de vue de son auteur (VT5-04) et le statut "
      "de T5-19 (VT5-03 : nœud de Lazar) ; script `brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon6-v1.py` ; aucune autre "
      "ligne ne change. Le brouillon 5 est écrit")
    a("T6-03", "elle-même, que la lecture lit ; VCT8B-01), **soumise à la session mère** (section gelée du brouillon 4) ;",
      "elle-même, que la lecture lit ; VCT8B-01), **nœud de Lazar** (règle « Gel vérifiable », section « Ce que les auteurs savaient "
      "avant le scellement » ; section gelée du brouillon 4 ; VT5-03) : **non scellable avant son mot** ; refusée, elle est retirée, "
      "le code restant tel quel et l'écart à la lettre du point 1 déclaré (VCT8B-01) ;")
    a("T6-04", "(phrase ajoutée au brouillon 5, VCT8B-01, soumise à la session mère) ;",
      "(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, en attente de son mot, VT5-03) ;")
    a("T6-05", "**brouillon 5 (candidat)**, la session du compte 4", "**brouillons 5 et 6 (candidats)**, la session du compte 4")
    a("T6-06", "exclue de la lecture et du verdict de T0.8 et de P3-bis.",
      "exclue de la lecture et du verdict de T0.8 et de P3-bis. **Ce qu'elle a vu avant le scellement** (déclaration de vue, VT5-04) : "
      "aucune donnée ni aucun résultat de 7a ou de 7b, aucune sortie de la pièce HD (non créée), aucune valeur ni aucun score de sonde, "
      "aucun score de T0.7 ; elle a lu, sans résultat : T0.7 scellé (en partie) et le code de son module aux commits C7 et de fusion, "
      "P3-bis scellé (lecture ciblée, préparation de l'audit des fuites), la base (A) scellée, T0.6 scellé par sections, les messages "
      "de commit de `main`, et les seules sorties **factices** des essais jouets du code de T0.8.")
    a("T6-07", "- **Date (UTC)** : brouillon 5 écrit le ",
      f"- **Date (UTC)** : brouillon 6 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 5 écrit le ")
    a("T6-08", "**Relecture du brouillon 3 (faite : contre-lecture 3)**",
      "- **Contre-lecture 4** — vérification courte en différentiel du brouillon 5, sous-agent neuf de la session du compte 4, "
      "modèle B, autre modèle que l'auteur du brouillon 5 (modèle A) ; n'a écrit ni T0.8, ni la base (A), ni le code de T0.8, ni "
      "leurs relectures ; n'a lu ni T0.7, ni P3-bis, ni le registre ; n'a vu aucun résultat de 7b, de la pièce HD ni de sonde. "
      f"**Brouillon relu** : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon5.md`, `{B5}`. **Rapport** : `{RAPPORT}`, "
      f"`{SHA_RAPPORT}` (égale à son compagnon ; version 3, qui remplace les versions 1, `{REMPLACES[0][1]}`, et 2, "
      f"`{REMPLACES[1][1]}`, gardées : la première recopiait des extraits portant des identifiants de modèles, la seconde un "
      "nombre faux ; mêmes couples). **Verdict** : « conforme après les corrections listées » ; 1 bloquant, 4 majeurs, "
      "4 mineurs ; le rejeu des 19 couples rend le brouillon 5 à l'octet ; sections « Hypothèse » à « Liste d'arrêt » égales au "
      "brouillon 4, sauf la ligne de T5-19. **Traitement** : VT5C-01 à VT5C-04 appliqués tels qu'écrits (VT5-01, VT5-02, VT5-05, "
      "VT5-06) ; VT5-03 : T5-19 dite nœud de Lazar (en-tête ; plan, point 1) ; VT5-04 : déclaration de vue de l'auteur (en-tête) ; "
      "VT5-07, VT5-08, VT5-09 : portés à la session mère, sans changement (sections gelées ; table des marqueurs).\n\n"
      "**Relecture du brouillon 3 (faite : contre-lecture 3)**")
    a("T6-09", "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 4 au brouillon 5 par un",
      "**Relecture du brouillon 5 (faite : contre-lecture 4)**, prévue alors : vérification courte du différentiel du brouillon 4 au brouillon 5 par un")
    a("T6-10", "seuil ni critère de lecture neuf ; le commit cité égal à celui de la pièce des empreintes. Son entrée, avec ses deux empreintes, s'ajoute à cette section dans le texte qui suit.",
      "seuil ni critère de lecture neuf ; le commit cité égal à celui de la pièce des empreintes. Son entrée, avec ses deux empreintes, s'ajoute à cette section dans le texte qui suit.\n\n"
      "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 5 au brouillon 6 (quatre "
      "couples du vérificateur, déclaration de vue, statut de T5-19, entrée de la contre-lecture 4), par un sous-agent neuf d'un autre "
      "modèle que l'auteur (modèle A), qui n'a écrit ni ce texte, ni la base (A), ni le code de T0.8, et n'a vu aucun résultat de 7b, "
      "de la pièce HD ni de sonde ; son entrée, avec ses deux empreintes, s'ajoute au texte qui suit ; puis le mot de Lazar sur T5-19 "
      "et les six marqueurs.")
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
