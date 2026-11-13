"""Écrit les couples du brouillon 5 « validité de l'adaptateur » (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-brouillon5-v1.py HEURE_UTC SORTIE_JSON
- reprend tels quels six couples de la vérification courte du brouillon 4 (VB4-03, VB4-04a, VB4-04b, VB4-05, VB4-07,
  VB4-08), après vérification de l'empreinte du rapport ; VB4-01 et VB4-06 sont remplacés par des couples de l'auteur
  (R-2604 étend la règle de lancement à la pièce R ; R-2597 demande la table de puissance entière) ;
- ajoute les couples de l'auteur (session du compte 4, modèle A ; modèles notés sans identifiant, R-2598).
"""
import hashlib, json, re, sys
from pathlib import Path

RAPPORT = Path("prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon4-verification-courte-v1.md")
SHA_RAPPORT = "a0dd42c6b6db369967effd3c25eb75602cae46de93ab052b3d3dacbef040fae1"
PRIS = ["VB4-03", "VB4-04a", "VB4-04b", "VB4-05", "VB4-07", "VB4-08"]

def couples_verificateur():
    if hashlib.sha256(RAPPORT.read_bytes()).hexdigest() != SHA_RAPPORT:
        sys.exit("ARRÊT : empreinte du rapport de la vérification courte différente")
    sec = RAPPORT.read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    tous = {c["id"]: c for c in json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))}
    return [tous[i] for i in PRIS]

def couples_auteur(h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("A5-01", "honnête (iii) — v1 — brouillon 4", "honnête (iii) — v1 — brouillon 5")
    a("A5-02", "- Auteur du **brouillon 4** : la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`), Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit",
      "- Auteur des **brouillons 4 et 5** : la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`), modèle A (modèles notés sans identifiant, R-2598), qui n'a écrit")
    a("A5-03", "sur le brouillon 3 et la contre-lecture 2.",
      "sur le brouillon 3 et la contre-lecture 2 ; le brouillon 5 de même, sur le brouillon 4, la vérification courte du brouillon 4 et les décisions R-2597 et R-2604.")
    a("A5-04", "- Date (UTC) : brouillon 4 écrit le 2026-11-13 à partir de ",
      "- Date (UTC) : brouillon 5 écrit le 2026-11-13 à partir de " + h + " UTC (heure relevée par `date -u`) ; brouillon 4 écrit le 2026-11-13 à partir de ")
    a("A5-05", "- Statut : **brouillon 4**, écrit sur le brouillon 3",
      "- Statut : **brouillon 5**, écrit sur le brouillon 4 (`417d6aee9a86d56f3478b57da30cb8d1af47493ff79ba69858f2167b8ad15f42`) par couples versés : applique la vérification courte du brouillon 4 (VB4-01 à VB4-09), la décision de la mère sur la règle de lecture (**R-2597** : règle (a) adoptée, table de puissance refaite) et la décision sur les pièces HD et R (**R-2604** : créées si et seulement si P3-bis rend « vu », règle écrite avant le verdict, garde d'arrêt au plafond de 30 USD, sans relèvement) ; un seul marqueur restant, `<<COMMIT_C7_T07>>`, gardé sur le mot de la mère (R-2597, point 3) jusqu'au commit corrigé de T0.7 ; **non scellable avant de l'avoir rempli** (VB4-02) et avant une vérification courte du différentiel. Le brouillon 4 était écrit sur le brouillon 3")
    a("A5-06", "**CLVA2-01 et CLVA2-10 selon la recommandation du lecteur (règle (a) de T0.7), en attente de la décision de la mère** ; **CLVA2-11 (pièce HD) selon l'option recommandée à Lazar par la session du compte 4, en attente de son mot (nœud)** ; non scellable comme préenregistrement avant ces deux réponses et la vérification courte prévue (section « Contre-lecture »).",
      "CLVA2-01 et CLVA2-10 selon la recommandation du lecteur (règle (a) de T0.7), **adoptée par la mère (R-2597)** ; CLVA2-11 (pièce HD) selon l'option recommandée, **tranchée par R-2604** et étendue à la pièce R au brouillon 5.")
    a("A5-07", "`)  : lus par la contre-lecture 2", "`) : lus par la contre-lecture 2")
    a("A5-08", "**option recommandée à Lazar, en attente de son mot (nœud)** ;", "**tranché par R-2604** ;")
    a("A5-09", "Les courses louées de ce texte se jouent l'une après l'autre, après relevé du crédit, par la session tenante que désigne la mère.",
      "Les courses louées de ce texte se jouent l'une après l'autre, après relevé du crédit, par la session tenante que désigne la mère (plan multi-comptes, `docs/notes/plan-paquet-multi-comptes-v1/plan-paquet-multi-comptes-v1.md`, `3b1bda252f9f893a9d00715c7442639534303dc4ac145da7302b024bde099887`, section 7, point 7 ; VB4-09).")
    a("A5-10", "`GO-RELECTURE-VADAPT`, `SCORES-T07`, `SONDES-T07`, `SORTIES-HD-VADAPT` ;",
      "`GO-RELECTURE-VADAPT`, `SCORES-T07`, `SONDES-T07`, `VERDICT-P3BIS` (issue « vu » : règle de lancement ci-dessous), et `SORTIES-HD-VADAPT` si la pièce HD a été créée ;")
    a("A5-11", "Engagement : jouée quelle que soit l'issue de P3-bis, de T0.6 et de T0.7 (ses scores restent fermés si l'aiguillage du point 5 les ferme).",
      "**Règle de lancement (R-2604 ; VB4-01), mécanique, écrite avant `VERDICT-P3BIS`** : la pièce R est créée **si et seulement si** E8 → `issue` vaut « vu » ; sinon elle n'est pas créée et ses lignes sont « non lues (G-1) » (rien de ce qui serait lu n'est perdu). La condition remplie, elle est jouée quelle que soit l'issue de T0.6 et de T0.7 (ses scores restent fermés si l'aiguillage du point 5 les ferme).")
    a("A5-12", "**Ce qui dépend de P3-bis** : L seulement (`VERDICT-P3BIS`).",
      "**Ce qui dépend de P3-bis** : L (`VERDICT-P3BIS`) et, depuis R-2604, la création des pièces HD et R (si et seulement si `issue` vaut « vu » ; plan, points 2 et 3 ; VB4-01).")
    a("A5-13", "toute relance d'une pièce est un retour à la mère et, au-delà du plafond, à Lazar.",
      "toute relance d'une pièce est un retour à la mère ; **aucun relèvement du plafond** (R-2604).")
    a("A5-14", ": **nœud N-VA-1** (journal du brouillon 3, § 3 ; ouvert à la connaissance de l'auteur du brouillon 4, qui n'a pas lu le registre).",
      ": nœud N-VA-1 **tranché par R-2604** : plafond de 30 USD gardé, **sans relèvement** ; la garde d'arrêt ci-dessus (cumul relevé plus un quart d'heure : HD 21,0, R 8,5, tout 29,5 USD) arrête les courses avant le plafond, et l'ordre de sacrifice ci-dessous s'applique au pire cas.")
    a("A5-15", "HD après `VERDICT-P3BIS`, si l'issue est « vu » (plan, point 2), ≈ 7,5 h ;",
      "HD et R après `VERDICT-P3BIS`, si l'issue est « vu » (plan, points 2 et 3 ; R-2604) ; HD ≈ 7,5 h ;")
    a("A5-16", "ni la règle de lancement de la pièce HD sur `issue` de P3-bis, écrite au plan, point 2, avant `VERDICT-P3BIS`).",
      "ni la règle de lancement des pièces HD et R sur `issue` de P3-bis (R-2604), écrite au plan, points 2 et 3, avant `VERDICT-P3BIS`).")
    a("A5-17", "Table pour quatre sondes (98,75 %) ; à trois (98,33 %) et deux (97,5 %), les valeurs baissent d'au plus 0,01 (journal).",
      "**Brouillon 5** (R-2597, point 1 ; VB4-06) : table aux trois niveaux de Bonferroni que T0.7 peut appliquer (quatre, trois ou deux sondes lues : 98,75 % / 98,33 % / 97,5 %), script `brouillons/validite-adaptateur-v1/candidat1-pieces/puissance-brouillon5-trois-niveaux-v1.py`, sortie `sortie-puissance-brouillon5-trois-niveaux-v1.txt` ; le brouillon 4 ne donnait que 98,75 % et écrivait à tort que les valeurs baissaient d'au plus 0,01 aux autres niveaux.")
    a("A5-18", "| 98,75 % | 0,881 ; 0,789 ; 0,711 ; 0,667 |",
      "| 98,75 % / 98,33 % / 97,5 % | (30, 100) : 0,881 / 0,873 / 0,861 ; (50, 200) : 0,789 / 0,783 / 0,774 ; (100, 300) : 0,711 / 0,706 / 0,700 ; (200, 300) : 0,667 / 0,663 / 0,658 |")
    a("A5-19", "| (20, 20) ou moins | 98,75 % | > 1 : **non informative** (`σ` = 0,110 > 0,060) |",
      "| (20, 20) ou moins | trois niveaux | > 1 : **non informative** (`σ` = 0,110 > 0,060 ; au seuil `σ` = 0,060 : 0,819 / 0,812 / 0,802) |")
    a("A5-20", "| 98,75 %, intervalle et plancher | tau ≥ 0,165 / 0,192 / 0,271 |",
      "| 98,75 % / 98,33 % / 97,5 %, intervalle et `Dτ` | tau ≥ 0,165 / 0,162 / 0,156 (dix lisibles) ; 0,192 / 0,188 / 0,182 (huit) ; 0,271 / 0,266 / 0,257 (cinq) |")
    a("A5-21", "| écart ≥ 0,30 à 0,17 |", "| écart ≥ 0,30 à 0,17 (98,75 % ; critère sans plancher, non refait aux autres niveaux) |")
    a("A5-22", "| 64 × 10 / 8 | 98,75 % | écart ≥ 0,147 / 0,170 |",
      "| 64 × 10 / 8 | 98,75 % / 98,33 % / 97,5 % | écart ≥ 0,147 / 0,142 / 0,135 (dix) ; 0,170 / 0,165 / 0,157 (huit) |")
    a("A5-23", "| 640 contre 640 | 98,75 % | 0,602 (T0.7 scellé,", "| 640 contre 640 | 98,75 % / 98,33 % / 97,5 % | 0,602 / 0,600 / 0,597 (T0.7 scellé,")
    a("A5-24", "Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur du brouillon 3 et que l'auteur du brouillon 4 (Claude Opus 5.5 ; N-052)",
      "modèle B (R-2598), autre modèle que le rédacteur du brouillon 3 et que l'auteur du brouillon 4 (modèle A ; N-052)")
    a("A5-25", "**option (a) du lecteur appliquée, en attente de la décision de la mère**", "option (a) du lecteur appliquée, **adoptée par la mère (R-2597)**")
    a("A5-26", "option (a) appliquée, en attente de la décision de la mère :", "option (a) appliquée, adoptée (R-2597) ; table refaite aux trois niveaux au brouillon 5 ;")
    a("A5-27", "**option recommandée à Lazar appliquée, en attente de son mot (nœud)** : HD après `VERDICT-P3BIS`, créée si et seulement si l'issue est « vu »",
      "option recommandée appliquée, **tranchée par R-2604** et étendue à la pièce R au brouillon 5 : HD et R après `VERDICT-P3BIS`, créées si et seulement si l'issue est « vu »")
    a("A5-28", "| CLVA2-18 (section « Contre-lecture ») | cette entrée ; paragraphe de la contre-lecture suivante réécrit | « Contre-lecture » |",
      "| CLVA2-18 (section « Contre-lecture ») | cette entrée ; paragraphe de la contre-lecture suivante réécrit | « Contre-lecture » |\n| CLVA-17 (journal des ouvertures ; rapport, § 4) | plus de confirmation du développeur exigée : T0.7 scellé, l. 2804, revérifié par le lecteur sur `main` (couple A4-29 ; ligne ajoutée au brouillon 5, VB4-09) | plan, point 4 |")
    a("A5-29", "**Vérification courte, prévue avant le scellement** : un sous-agent neuf, autre modèle que l'auteur du brouillon 4 (Claude Opus 5.5), non lecteur de P3-bis, en différentiel du brouillon 3 au brouillon 4 (couples versés et script d'application), contre le rapport de la contre-lecture 2 et T0.7 scellé ; puis la décision de la mère sur CLVA2-01 et CLVA2-10, et le mot de Lazar sur CLVA2-11.",
      "**Vérification courte du brouillon 4 (faite)** — sous-agent neuf de la session du compte 4, modèle B, autre modèle que l'auteur du brouillon 4 (modèle A) ; même modèle que les contre-lectures 1 et 2 (réserve qu'il déclare) ; lecteur de T0.7 scellé par lignes citées. Consigne : `brouillons/validite-adaptateur-v1/consigne-verification-courte-brouillon4-compte4-v1.md`, `eb58cb15b6bf5166509adaa078ae079fd060468a6595265008e2a0dbe3959478`. Brouillon relu : `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon4.md`, `417d6aee9a86d56f3478b57da30cb8d1af47493ff79ba69858f2167b8ad15f42`. Rapport : `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon4-verification-courte-v1.md`, `a0dd42c6b6db369967effd3c25eb75602cae46de93ab052b3d3dacbef040fae1`. Verdict : « conforme après les corrections listées » ; 0 bloquant, 2 majeurs, 7 mineurs ; rejeu des couples à l'octet. Traitement au brouillon 5 :\n\n"
      "| constat | traitement | où |\n|---|---|---|\n"
      "| VB4-01 (règle de lancement de HD non raccordée à R) | **R-2604** : la pièce R reçoit la même règle de lancement que HD (créée si et seulement si `issue` vaut « vu ») ; `SORTIES-HD-VADAPT` exigée seulement si HD est créée ; « ce qui dépend de P3-bis » réécrit (couples A5-10 à A5-12, A5-15, A5-16 ; le couple VB4-01 du vérificateur, qui supposait R engagée, n'est pas pris) | plan, points 2 et 3 ; « Calcul et dépense » ; « Liste d'arrêt » |\n"
      "| VB4-02 (remplissage du marqueur) | différé au commit corrigé de T0.7 (R-2597, point 3) : deux couples à contexte, parenthèse retirée, pièce de confirmation neuve pour `reextraction_p3_v1.py` | en-tête |\n"
      "| VB4-03, VB4-04a, VB4-04b, VB4-05, VB4-07, VB4-08 | couples du vérificateur, tels qu'écrits | « Métrique » ; « Code neuf » ; « Seuil » ; « Calcul et dépense » ; « Métrique », directions |\n"
      "| VB4-06 (« au plus 0,01 ») | table de puissance refaite aux trois niveaux (R-2597, point 1) ; le couple VB4-06 n'est pas pris, la phrase est remplacée (A5-17 à A5-23) | « Puissance » |\n"
      "| VB4-09 (traçabilité, forme) | ligne CLVA-17 ajoutée à la table de la contre-lecture 2 ; source de la phrase sur les courses louées citée ; double espace retiré | « Contre-lecture » ; plan, point 2 ; en-tête |\n"
      "| R-2604, garde au plafond | nœud N-VA-1 tranché : plafond de 30 USD sans relèvement ; garde d'arrêt au cumul plus un quart d'heure gardée et rappelée | « Calcul et dépense » |\n\n"
      "**Avant le scellement** : remplissage du marqueur `<<COMMIT_C7_T07>>` au commit corrigé de T0.7 (VB4-02), puis une vérification courte du différentiel brouillon 4 → brouillon suivant par un sous-agent neuf d'un autre modèle que l'auteur (modèle A), non lecteur de P3-bis.")
    return c

def principal():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    h, sortie = sys.argv[1], Path(sys.argv[2])
    if not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : heure au format HH:MM attendue")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples_verificateur() + couples_auteur(h)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

principal()
