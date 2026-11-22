"""Écrit les couples du brouillon 7 (candidat) de T0.8 sur le brouillon 6 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-t08-brouillon7-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- reprend, tels qu'écrits et dans leur ordre, les deux couples VT6C-01 et VT6C-02 de la vérification courte du brouillon 6,
  après contrôle de l'empreinte du rapport (bloc JSON de sa section « 3. Couples ») ;
- ajoute les couples de l'auteur (session du compte 4, modèle A) : septième marqueur `MOT_LAZAR_T5_19` à la place de « en
  attente de son mot » (VT6-02) ; déclaration de vue bornée (VT6-03) ; renvois (VT6-05) ; entrée « Contre-lecture 4 »
  précisée (VT6-06) ; confirmation de la mère rattachée au marqueur (VT6-07) ; entrée « Contre-lecture 5 » ; en-tête.
"""
import hashlib, json, re, sys
from pathlib import Path

RAPPORT = Path("prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon6-verification-courte-v1.md")
SHA_RAPPORT = "8794f9d7f772d85b76b2d2364f5e23dc8f2843f192e8b89b90c0c0246c287322"
B6 = "ff7b0ddda5294aaba7b51276f6dfb5c857a9df4c6c0c444d723cf28fd68c92c6"
J10 = ("registres-provisoires/compte-4-2026-11-14-v10.md", "3c8b0e1f4f9812b51a7b2d41ac19e17d4603cdfedd5b5b8f61047e684bfd76a3")
PRIS = ["VT6C-01", "VT6C-02"]
MK = "<<" + "MOT_LAZAR_T5_19" + ">>"

def couples_verificateur():
    for ch, s in ((RAPPORT, SHA_RAPPORT), (Path(J10[0]), J10[1])):
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    if [c["id"] for c in tous] != PRIS:
        sys.exit("ARRÊT : couples du vérificateur autres que VT6C-01 et VT6C-02")
    return [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in tous]

def couples_auteur(d, h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("T7-01", "— v1 — brouillon 6 (candidat)", "— v1 — brouillon 7 (candidat)")
    a("T7-02", "- **Statut** : **brouillon 6 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 6 applique",
      "- **Statut** : **brouillon 7 (candidat)**, **non scellé** ; il ne vaut pas préenregistrement (R1). Le brouillon 7 applique par "
      f"programme, tels qu'écrits, les deux couples VT6C-01 et VT6C-02 de la vérification courte du brouillon 6 (modèle B, « conforme "
      f"après les corrections listées » ; `{RAPPORT}`, `{SHA_RAPPORT}`) et les couples de son auteur : septième marqueur "
      "`MOT_LAZAR_T5_19` à la place d'un statut d'attente (VT6-02) ; déclaration de vue bornée (VT6-03) ; renvois (VT6-05, VT6-06, "
      "VT6-07) ; entrée « Contre-lecture 5 » ; titre, « Auteurs », « Date » ; script "
      "`brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon7-v1.py`, couples `brouillons/t08-code-compte4-v1/couples-t08-brouillon7-v1.json` ; "
      "aucune autre ligne ne change ; **non scellable avant le mot de Lazar sur T5-19 (marqueur `MOT_LAZAR_T5_19`), la vérification "
      "courte du différentiel du brouillon 6 au texte qui remplit ce marqueur, et les six autres marqueurs**. Le brouillon 6 applique")
    a("T7-03", "six marqueurs restent, à la session mère et à Lazar", "sept marqueurs restent, à la session mère et à Lazar")
    a("T7-04", "- **Marqueurs restants** (six, une occurrence chacun ; `COMMIT_CODE_T08` rempli au brouillon 5 ;",
      "- **Marqueurs restants** (sept, une occurrence chacun ; `COMMIT_CODE_T08` rempli au brouillon 5 ; `MOT_LAZAR_T5_19` ajouté au brouillon 7 ;")
    a("T7-05", ": **non scellable avant son mot** ;", ": **non scellable avant son mot** (marqueur `MOT_LAZAR_T5_19`, plan, point 1) ;")
    a("T7-06", "(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, en attente de son mot, VT5-03) ;",
      f"(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, VT5-03 : `{MK}`) ;")
    a("T7-07", "**Ce qu'elle a vu avant le scellement** (déclaration de vue, VT5-04) : aucune donnée ni aucun résultat de 7a ou de 7b,",
      "**Ce qu'elle a vu avant le scellement** (déclaration de vue, VT5-04 ; bornée au brouillon 7, VT6-03) : hors ce que les textes "
      "qu'elle a lus citent eux-mêmes (ce texte cite des durées et une dépense de 7a et des résultats de P3 ; T0.6, T0.7 et P3-bis "
      "scellés en citent aussi), aucun fichier de données, de diagnostic ni de run de 7a ou de 7b ouvert, aucun résultat de 7b,")
    a("T7-08", "T0.6 scellé par sections, les messages",
      "T0.6 scellé par sections (règle « mots et coût », concordance avec T0.7, et les sections que citent les textes qu'elle "
      "écrivait ou vérifiait), les messages")
    a("T7-09", "autre modèle que l'auteur du brouillon 5 (modèle A) ; n'a écrit ni T0.8",
      "autre modèle que l'auteur du brouillon 5 (modèle A ; vérifié par l'auteur, le rapport ne pouvant le faire : modèle configuré "
      "et servi de sa session, contre l'identifiant que le vérificateur donne dans son rendu) ; n'a écrit ni T0.8")
    a("T7-10", "leurs relectures ; n'a lu ni T0.7, ni P3-bis, ni le registre ; n'a vu aucun résultat",
      "leurs relectures ; n'a lu ni T0.7, ni P3-bis, ni aucun fichier de `registres/` (il a lu deux journaux provisoires du compte 4) ; "
      "n'a vu aucun résultat")
    a("T7-11", "VT5-07, VT5-08, VT5-09 : portés à la session mère, sans changement (sections gelées ; table des marqueurs).",
      f"VT5-07 (arrêt d'antériorité que la « Liste d'arrêt » ne nomme pas) : suit T5-19 chez Lazar ; VT5-08, VT5-09 : portés à la "
      f"session mère, sans changement (sections gelées ; table des marqueurs) ; renvoi : journal du compte 4, `{J10[0]}`, `{J10[1]}`, "
      "C4-0045 et C4-0046.\n\n"
      "- **Contre-lecture 5** — vérification courte en différentiel du brouillon 6, sous-agent neuf de la session du compte 4, "
      "modèle B (vérifié par l'auteur comme à la contre-lecture 4), autre modèle que l'auteur (modèle A) ; n'a écrit ni T0.8, ni la "
      "base (A), ni le code de T0.8 ; n'a lu ni T0.7, ni P3-bis, ni `registres/` ; n'a vu aucun résultat de 7b, de la pièce HD ni de "
      f"sonde. **Brouillon relu** : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon6.md`, `{B6}`. **Rapport** : `{RAPPORT}`, "
      f"`{SHA_RAPPORT}` (égale à son compagnon). **Verdict** : « conforme après les corrections listées » ; 0 bloquant, 3 majeurs, "
      "4 mineurs ; le rejeu des 14 couples rend le brouillon 6 à l'octet. **Traitement** : VT6C-01 et VT6C-02 appliqués tels "
      "qu'écrits (VT6-01, VT6-04) ; VT6-02 : septième marqueur `MOT_LAZAR_T5_19`, que le validateur refuse tant qu'il n'est pas "
      "rempli ; VT6-03 : déclaration de vue bornée ; VT6-05 : renvoi au journal ; VT6-06 : modèle et lectures précisés (contre-lecture "
      "4) ; VT6-07 : la confirmation de la session mère sur les trois points gardés s'écrit au remplissage de `MOT_LAZAR_T5_19`.")
    a("T7-12", "à confirmer par elle", "à confirmer par elle au remplissage du marqueur `MOT_LAZAR_T5_19`")
    a("T7-13", "| `LIGNE_DEPENSE_T08` | ligne d'engagement de `registres/depenses.md` | au lancement | session mère |",
      "| `LIGNE_DEPENSE_T08` | ligne d'engagement de `registres/depenses.md` | au lancement | session mère |\n"
      "| `MOT_LAZAR_T5_19` | le mot de Lazar sur la phrase T5-19 du point 1 du plan (gardée : son mot et sa ligne au registre, cités ; "
      "refusée : le texte suivant retire la phrase, la mention de l'en-tête et le membre de la relecture prévue, le code restant tel "
      "quel et l'écart à la lettre du point 1 déclaré, VCT8B-01) ; avec la confirmation de la session mère sur les trois points gardés "
      "plus stricts que ce texte (contre-lecture du code, traitement) | avant le scellement, avant `GEL-T08` | Lazar ; session mère |")
    a("T7-14", "**Relecture suivante, prévue avant le scellement** : vérification courte du différentiel du brouillon 5 au brouillon 6",
      "**Relecture du brouillon 6 (faite : contre-lecture 5)**, prévue alors : vérification courte du différentiel du brouillon 5 au brouillon 6")
    a("T7-15", "s'ajoute au texte qui suit ; puis le mot de Lazar sur T5-19 et les six marqueurs.",
      "s'ajoute au texte qui suit ; puis le mot de Lazar sur T5-19 et les six marqueurs.\n\n"
      "**Relecture suivante, prévue avant le scellement** : au mot de Lazar sur T5-19, le texte qui remplit `MOT_LAZAR_T5_19` (et, "
      "si la phrase est refusée, la retire) ; puis une vérification courte du différentiel du brouillon 6 à ce texte, qui couvre "
      "aussi les couples du brouillon 7, par un sous-agent neuf d'un autre modèle que l'auteur, qui n'a vu aucun résultat de 7b, de "
      "la pièce HD ni de sonde ; son entrée s'ajoute au texte qui suit ; puis les six autres marqueurs.")
    a("T7-16", "**brouillons 5 et 6 (candidats)**, la session du compte 4", "**brouillons 5 à 7 (candidats)**, la session du compte 4")
    a("T7-17", "- **Date (UTC)** : brouillon 6 écrit le ",
      f"- **Date (UTC)** : brouillon 7 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 6 écrit le ")
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
