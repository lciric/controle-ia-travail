"""Écrit les couples du brouillon 7 « validité de l'adaptateur » (candidat) sur le brouillon 6 (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-brouillon7-v1.py DATE_UTC HEURE_UTC SORTIE_JSON   (relevées par `date -u`)
- vérifie l'empreinte du brouillon 6 et du rapport de sa vérification courte ;
- reprend tel qu'écrit le seul couple du vérificateur, VB6-02 (bloc JSON de la section « 3. Couples » du rapport) ;
- ajoute les couples de l'auteur (session du compte 4, modèle A) : entrée de la vérification courte du brouillon 6 dans
  « Avant le scellement » (VB6-04), avec VB6-01 et VB6-03 portés à la session mère ; titre, auteur, date, statut.
Le différentiel du brouillon 6 au brouillon 7 se limite à cela (VB6-04).
"""
import hashlib, json, re, sys
from pathlib import Path

B6 = Path("brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon6.md")
SHA_B6 = "7f0a29d1e8a656b01e763b43a2948d90eb7cf8df0ea444f068d975716098a0f5"
RAPPORT = Path("prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon6-verification-courte-v1.md")
SHA_RAPPORT = "2c886d3e6f906584c7025cb46f8b7ac782e897acb4283507e1595a3196d4ebf3"
CONSIGNE = ("brouillons/validite-adaptateur-v1/consigne-verification-courte-brouillon6-compte4-v1.md",
            "1ccb67e33ed0e2ae1daba7b35c034905bced81a295816dc081beb1dd549db96e")
SCRIPT = "brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon7-v1.py"


def couple_verificateur():
    for ch, s in ((B6, SHA_B6), (RAPPORT, SHA_RAPPORT), (Path(CONSIGNE[0]), CONSIGNE[1])):
        if hashlib.sha256(Path(ch).read_bytes()).hexdigest() != s:
            sys.exit(f"ARRÊT : empreinte de {ch} différente")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    if [c["id"] for c in tous] != ["VB6-02"]:
        sys.exit("ARRÊT : couples du vérificateur autres que VB6-02")
    return [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in tous]


def couples_auteur(d, h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("A7-01", "et témoin distillé honnête (iii) — v1 — brouillon 6", "et témoin distillé honnête (iii) — v1 — brouillon 7 (candidat)")
    a("A7-02", "- Auteur des **brouillons 4 à 6** :", "- Auteur des **brouillons 4 à 7** :")
    a("A7-03", "et R-2605 (modèles notés « modèle A » et « modèle B » dans tout le texte).",
      "et R-2605 (modèles notés « modèle A » et « modèle B » dans tout le texte) ; le brouillon 7 de même, sur le brouillon 6 et "
      "sa vérification courte.")
    a("A7-04", "- Date (UTC) : brouillon 6 écrit le ",
      f"- Date (UTC) : brouillon 7 écrit le {d} à partir de {h} UTC (heure relevée par `date -u`) ; brouillon 6 écrit le ")
    a("A7-05", "- Statut : **brouillon 6**, écrit sur le brouillon 5",
      f"- Statut : **brouillon 7 (candidat)**, écrit sur le brouillon 6 (`{SHA_B6}`) par couples versés (script `{SCRIPT}`) : le "
      "couple VB6-02 de la vérification courte du brouillon 6, tel qu'écrit, et l'entrée de cette vérification dans « Avant le "
      "scellement » (VB6-04), avec le titre, l'auteur, la date et ce statut ; rien d'autre ne change ; aucun marqueur restant ; "
      "**candidat rendu à la session mère** : avant le scellement, elle confirme au registre l'égalité du commit cité avec la "
      "ligne `CODE-T07` en vigueur (VB6-01) et les renvois de la notation des modèles (VB6-03). Le brouillon 6, écrit sur le brouillon 5")
    a("A7-06", "**non scellable avant la vérification courte du différentiel brouillon 5 → brouillon 6** (section « Contre-lecture »).",
      "**non scellable avant la vérification courte du différentiel brouillon 5 → brouillon 6** (section « Contre-lecture » ; faite, "
      "brouillon 7).")
    a("A7-07", "**Avant le scellement** : marqueur du commit de T0.7 rempli au brouillon 6 (VB4-02) ; reste une vérification courte du "
      "différentiel brouillon 5 → brouillon 6 par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), non lecteur de P3-bis ; "
      "son entrée, avec ses deux empreintes, s'ajoute à cette section dans le texte qui suit.",
      "**Avant le scellement** : marqueur du commit de T0.7 rempli au brouillon 6 (VB4-02). **Vérification courte du différentiel "
      "brouillon 5 → brouillon 6 : faite** le 2026-11-14 par un sous-agent neuf de la session du compte 4, modèle B (autre modèle que "
      "l'auteur, modèle A, N-052 ; contrôlé par l'auteur contre l'identifiant rendu par le vérificateur), non lecteur de P3-bis ni de "
      "T0.7 scellé (aucun contenu de T0.7 ouvert : noms, statistiques et empreintes du module seulement) ; consigne "
      f"`{CONSIGNE[0]}`, `{CONSIGNE[1]}` ; brouillon relu `{B6.as_posix()}` (`{SHA_B6}`) ; "
      f"rapport `{RAPPORT}`, `{SHA_RAPPORT}`. Verdict : « candidat conforme » ; 0 bloquant, 0 majeur, 4 mineurs ; rejeu des 14 couples "
      "et du brouillon 6 à l'octet ; commit cité égal, à chaque occurrence, à celui de l'annonce ; affirmations vérifiables de la pièce "
      "de confirmation exactes ; validateur `[]`. Traitement : VB6-02 appliqué tel qu'écrit au brouillon 7 ; VB6-04 : cette entrée ; "
      "VB6-01 (égalité du commit avec la ligne `CODE-T07`, lue au registre) et VB6-03 (renvois R-2598, R-2605 de la notation des "
      "modèles) : portés à la session mère, sans changement du texte. Le différentiel du brouillon 6 au brouillon 7 se limite à VB6-02, "
      "à cette entrée et à l'en-tête ; sa relecture éventuelle est à la décision de la session mère.")
    return c


def principal():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    d, h, sortie = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) or not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : date AAAA-MM-JJ et heure HH:MM attendues")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couple_verificateur() + couples_auteur(d, h)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")


principal()
