"""Brouillon 7 du préenregistrement du crible (v) : corrections du tour 6 de contre-lecture et décisions de la mère (R-2992).

Couples « ancien → nouveau » :
  (1) les 7 couples des corrections D6-01 à D6-06 (D6-01, D6-02, D6-03, D6-04a, D6-04b, D6-05, D6-06), lus dans le rapport
      de contre-lecture lui-même (bloc entre clôtures nommé `D6-…`, ligne « ANCIEN: » puis ligne « NOUVEAU: ») ; deux
      « nouveau » reçoivent une retouche déclarée (D6-02 et D6-05 : branche à 24 mondes retirée par R-2992, sonde neuve
      exigée par R-2992, « ci-dessous » corrigé en « ci-dessus »), chaque retouche vérifiée présente une seule fois dans
      son « nouveau » ;
  (2) les couples des décisions de la mère (ligne R-2992 de `registres/decisions.md`), nommés « r2992-… » : N = 20 dans
      tous les cas ; étage 5 rapporté sans verdict ; partie A sans le champ des « retenues » ; points ouverts de « Choix et
      doutes » à la recommandation écrite (donc sonde neuve exigée) ; mentions fausses « rédacteur modèle C » corrigées ;
  (3) des couples propres (titre, en-tête, statut, validateur, tête de la section « Contre-lecture », entrée
      « Contre-lecture 6 »).
Tous sont déclarés dans l'entrée « Contre-lecture 6 » de la cible.
Gardes : empreinte de la pièce de départ et du rapport ; 7 couples exactement dans le rapport, noms attendus ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; tous les couples
appliqués d'un coup sur la pièce de départ ; chaque « nouveau » présent dans la cible ; la cible ne doit pas exister
(ouverture en mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon7.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon6.md")
SOURCE_SHA = "08b430d7ec9cc4b7435dd46c772b0e56cc92a1630e945e38f46d1ec7d97624d6"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-b4-tour3-v1.md")
RAPPORT_SHA = "da47da2f5bd47c7eaa90ead4d4a2d9bcf65474d500ad83543ae2b35b31b5bec5"
NOM_CIBLE = "crible-v-brouillon7.md"
NOMS_RAPPORT = ["D6-01", "D6-02", "D6-03", "D6-04a", "D6-04b", "D6-05", "D6-06"]


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 0. Dossier de la cible.
args = sys.argv[1:]
if args == []:
    DOSSIER = ICI
elif len(args) == 2 and args[0] == "--essai":
    DOSSIER = os.path.abspath(args[1])
    if DOSSIER == ICI or not os.path.isdir(DOSSIER):
        arret(f"dossier d'essai invalide : {DOSSIER}")
else:
    arret(f"arguments illisibles : {args!r}")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)

# 1. Empreintes des entrées ; cible absente.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if not os.path.isfile(chemin):
        arret(f"absent : {chemin}")
    if sha(chemin) != attendu:
        arret(f"empreinte inattendue : {chemin}")
if os.path.exists(CIBLE):
    arret(f"la cible existe déjà : {CIBLE}")

with open(SOURCE, encoding="utf-8") as f:
    texte = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()

# 2. Couples du rapport, puis retouches déclarées.
blocs = re.findall(r"^`(D6-[0-9a-z]+)`\n```\nANCIEN: (.*?)\nNOUVEAU: (.*?)\n```", rapport, re.S | re.M)
if [b[0] for b in blocs] != NOMS_RAPPORT:
    arret(f"couples du rapport inattendus : {[b[0] for b in blocs]!r}")

RETOUCHES = {
    "D6-02": [(
        "pour N = 20 et pour N = 24, avec n_c = N et k_R = ⌊N/2⌋ (pire cas de l'énumération : 184 756 et 2 704 156 ensembles)",
        "pour N = 20 (seul nombre de mondes depuis R-2992), avec n_c = 20 et k_R = 10 (pire cas de l'énumération : "
        "184 756 ensembles)",
    )],
    "D6-05": [(
        "**les montants ci-dessous sont ceux de la branche « sonde neuve non exigée »** : si elle est exigée (décision écrite "
        "avant le scellement), κv1 passe à 104,39 et κv2 à 100,28 USD à 20 mondes (124,39 et 119,00 à 24).",
        "**les montants ci-dessus sont ceux de la branche « sonde neuve exigée »**, retenue (point 8 de « Choix et doutes » : "
        "recommandation prise par la mère, R-2992) : κv1 à 104,39 et κv2 à 100,28 USD à 20 mondes (sans la sonde, ils "
        "seraient de 100 et de 96,60 USD).",
    )],
}

couples = []
for nom, ancien, nouveau in blocs:
    if "\n" in ancien or "\n" in nouveau:
        arret(f"{nom} : ancien ou nouveau sur plusieurs lignes")
    nouveau = nouveau.replace("\\n", "\n")
    for a, b in RETOUCHES.get(nom, []):
        if nouveau.count(a) != 1:
            arret(f"{nom} : retouche introuvable une seule fois dans le « nouveau »")
        nouveau = nouveau.replace(a, b)
    couples.append((nom, ancien, nouveau))

# 3. Heure lue par `date -u`.
HEURE = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", HEURE):
    arret(f"heure illisible : {HEURE!r}")

D = []  # couples des décisions de la mère (R-2992)


def dec(nom, ancien, nouveau):
    D.append(("r2992-" + nom, ancien, nouveau))


# 3a. N = 20 dans tous les cas.
dec("n20-dix-2a",
    "(N = 20, ou 24 si le taux d'appels répondus du pilote est sous 0,95)",
    "(N = 20 dans tous les cas, décision de la mère, R-2992)")
dec("n20-dix-2b",
    "(80 appels à N = 20, 96 à N = 24)",
    "(80 appels)")
dec("n20-dix-6",
    "(4 de 16 à 22 mondes complets, 5 à 23 ou 24)",
    "(4 pour 16 à 20 mondes complets)")
dec("n20-dix-8",
    " ; **235,32** à 24 mondes : crédits 120,00, hors crédits 115,32)",
    ") ; **204,67** avec la sonde neuve, exigée (104,39 sur crédits, 100,28 hors crédits ; point 8 de « Choix et doutes », "
    "R-2992)")
dec("n20-notations",
    "n_c = nombre de mondes complets (20 au plus, ou 24 par la règle de la section « Taille »).",
    "n_c = nombre de mondes complets (20 au plus).")
dec("n20-placebo",
    "au plus C(24, 12) = 2 704 156 à 24 mondes, 184 756 à 20\n  ensembles)",
    "au plus C(20, 10) = 184 756\n  ensembles)")
dec("n20-minimum",
    "- **Minimum** : n_c ≥ 0,8 × (nombre de mondes tirés, 20 ou 24 par la règle de la section « Taille ») mondes complets, "
    "soit 16 sur 20 ou 20 sur 24 (arrondi au supérieur), et aucun",
    "- **Minimum** : n_c ≥ 0,8 × 20 = 16 mondes complets (N = 20 mondes tirés, section « Taille »), et aucun")
dec("n20-wmin",
    "n_c de 16 à 22 → 4 ; n_c = 23 ou 24 → 5.",
    "n_c de 16 à 20 → 4 (annexe A, points 5 et 11).")
dec("n20-epargne",
    " ; à 24 mondes, « dans 16 mondes ou plus » à 0,71 et « dans 17 mondes ou plus » à 0,75 (S_R = 0,25 exactement à k = 16 "
    "à 0,75)",
    "")
dec("n20-perte",
    "4 pour\n  n_c de 16 à 22, 5 pour n_c = 23 ou 24 ;",
    "4 pour\n  n_c de 16 à 20 ;")
dec("n20-mondes",
    "- **Mondes** : N mondes MR-2 (N = 20, ou 24 par la règle de la section « Taille » ; `generer_v4`",
    "- **Mondes** : N = 20 mondes MR-2 (`generer_v4`")
dec("n20-appels",
    "80 en tout (96 à 24 mondes),",
    "80 en tout,")
dec("n20-graines",
    "(r = 1 à N, N = 20 ou 24)",
    "(r = 1 à N, N = 20)")
dec("n20-etape-2",
    "le nombre de mondes (règle de la section « Taille »), ",
    "")
dec("n20-etape-3",
    "puis les 4 N appels (80 ou 96).",
    "puis les 4 N = 80 appels.")
dec("n20-taille-24",
    "**À 24 mondes** (W_min = 5",
    "**À 24 mondes, pour comparaison seulement** (raison de N = 20 ; W_min = 5")
dec("n20-taille-regle",
    "et peut porter le\nnombre de mondes de 20 à 24 **par cette seule règle, écrite d'avance** (décision de la mère, R-2977) : "
    "N = 20 si le taux d'appels répondus par appel du pilote est ≥ 0,95, N = 24 sinon ; pas de 30 ; devis à l'avenant "
    "(+ 20 %). Le taux se lit sur les appels du pilote",
    "à titre d'information ;\n**N = 20 dans tous les cas, gelé dès ce texte** (décision de la mère, R-2992, qui retire la règle "
    "« 24 mondes si le taux d'appels répondus par appel du pilote est sous 0,95 » de R-2977 : 24 mondes ne gagnent rien en "
    "puissance, ci-dessus, coûtent 20 % de plus et rendent le budget de durée probablement intenable, section « Devis ») ; "
    "pas de 24, pas de 30. Le taux d'appels répondus du pilote ne sert plus qu'à la probabilité d'atteindre le minimum "
    "(ci-dessous) ; il se lit sur les appels du pilote")
dec("n20-minuterie",
    "N = 20 ou 24) restante",
    "N = 20) restante")
dec("n20-ba-ordre",
    "**puis** le taux du pilote est lu avec cette B_a (section « Taille »), **puis** N, **puis** M =",
    "**puis** le taux du pilote est lu avec cette B_a (section « Taille », à titre d'information seulement), **puis** "
    "(N = 20 étant fixé, R-2992) M =")
dec("n20-table-duree",
    "pour N = 20 et pour N = 24, B_a",
    "pour N = 20, B_a")
dec("n20-non-lancable",
    "avec la case « non lançable » écrite en clair (à N = 24 et M = 1, les appels seuls font 24 × B_a, soit 12 h à "
    "B_a = 1 800 s : M ≥ 2 ou B_a plus court, à écrire)",
    "avec la case « non lançable » écrite en clair")
dec("n20-remesurer-3",
    "(le minimum de\nmondes complets : seul le nombre de mondes en dépend, règle de la section « Taille » ;",
    "(le minimum de\nmondes complets : seule la probabilité de l'atteindre en dépend, à titre d'information, section "
    "« Taille » ;")
dec("n20-go-24",
    " **À N = 24** (règle de la section « Taille ») : κv1 120,00 USD (Pr-2 48,00 ; Pr-4 72,00), κv2 115,32 USD (Pr-1 56,16 ; "
    "Pr-3 56,16 ; machine 3,00), 24 mondes ; les lignes s'écrivent pour le N que fixe cette règle, jamais pour l'autre.",
    " N = 20 dans tous les cas (R-2992) : aucune branche à 24 mondes.")
dec("n20-annexe-11",
    "« 1.0000 » est un arrondi",
    "Les lignes à n = 21 à 24 et à N = 24 sont sans objet depuis la décision de la mère R-2992 (N = 20 dans tous les cas) ; "
    "elles restent comme sortie recopiée. « 1.0000 » est un arrondi")
dec("n20-annexe-12",
    "qu'une illustration. Plus grande B_a",
    "qu'une illustration ; ses lignes à N = 24 sont sans objet depuis R-2992 (N = 20). Plus grande B_a")
dec("n20-choix-5",
    "**Tranché (R-2977)** : 24 mondes si le taux d'appels répondus par appel\n   du pilote est sous 0,95, 20 sinon (section "
    "« Taille »).",
    "**Tranché (R-2977)** : 24 mondes si le taux d'appels répondus par appel\n   du pilote est sous 0,95, 20 sinon. "
    "**Amendé (R-2992)** : N = 20 dans tous les cas ; la règle des 24 mondes est retirée (section « Taille »).")

# 3b. Étage 5 (ablation) rapporté sans verdict, hors des critères gelés (N-045 point 3 ; point 10 bis, option (a)).
dec("e5-dix-7",
    "le crible\n   éprouverait alors l'ablation (QO1), non la règle",
    "le crible\n   informerait alors surtout sur l'ablation (QO1, rapportée sans verdict, étage 5), non sur la règle")
dec("e5-v4",
    "| V4 | ablation : la moitié chère ajoute (« jamais les chers ») | + | W_B ≥ W_min | W_B = 0 | 0,45 |",
    "| V4 | ablation : la moitié chère ajoute (« jamais les chers ») ; **rapportée sans verdict** (étage 5, R-2992) | + | "
    "W_B ≥ W_min | aucune (lue sans zone de réfutation) | 0,45 |")
dec("e5-lecture-pred",
    "V3 et V4 : W de 1 à W_min − 1 ;",
    "V3 : W_R de 1 à W_min − 1 ; V4, rapportée sans verdict, n'a ni zone de réfutation ni zone d'indécision ;")
dec("e5-issues",
    "la lecture porte en fait sur l'ablation (H-v-a, étage 5).",
    "la lecture porte en fait sur l'ablation (H-v-a, étage 5, rapportée sans verdict).")
dec("e5-seuil-wb",
    "Mêmes seuils pour W_B.",
    "W_B et L_B sont rapportés avec leurs intervalles, sans verdict (étage 5, hors des critères gelés, R-2992).")
dec("e5-seuil-niveau",
    "le choix des mondes et l'ablation sont lus après\n  elle, sans correction (aucun ne peut faire adopter quoi que ce soit, "
    "section « Écarts »).",
    "le choix des mondes est lu après\n  elle, sans correction (il ne peut faire adopter quoi que ce soit, section "
    "« Écarts ») ; l'ablation est rapportée sans verdict (étage 5).")
dec("e5-comparaisons",
    "Puis, sans correction : le choix des mondes (règle contre\nplacebo, exact) et l'ablation (B contre T). Tout le reste "
    "est rapporté sans critère.",
    "Puis, sans correction : le choix des mondes (règle contre\nplacebo, exact). L'ablation (B contre T) et tout le reste "
    "sont rapportés sans critère (étage 5 hors des critères gelés, R-2992).")
dec("e5-table",
    "| 5 | ablation, QO1 (même règle que l'étage 3 sur W_B) | « la moitié chère n'ajoute rien d'observé » (W_B = 0) / "
    "« ajoute, établi » (W_B ≥ W_min(n_c)) / « ajoute peut-être » ; S_B rapporté |",
    "| 5 | ablation, QO1 : W_B, L_B, S_B et leurs intervalles | **rapportés, sans verdict** (N-045 point 3 : ablation "
    "rapportée, hors des critères gelés ; décision de la mère, R-2992) |")
dec("e5-ecarts",
    "- **N-045 point 3** dit l'ablation « rapportée, hors des critères gelés » dans les courses de l'organisme ; ici, c'est "
    "la question\n  du crible : elle entre aux critères gelés (étage 5) — à confirmer par la mère.",
    "- **N-045 point 3** dit l'ablation « rapportée, hors des critères gelés » dans les courses de l'organisme ; ici aussi, "
    "bien que ce\n  soit la question QO1 du crible : étage 5 rapporté sans verdict, hors des critères gelés (décision de la "
    "mère, R-2992 ; point 10 bis de « Choix et doutes »).")

# 3c. Partie A : archive de la génération 2 sans le champ des « retenues » (remarque F-4 du tour 4).
dec("pa-entrees",
    "et les archives de jugement de chaque génération ({K1} ; {K1} et les 11 retenues, verdict de v67, § 3, V-2).",
    "et l'archive de chaque génération, construite sans lire aucun champ du juge : {K1} pour la génération 1 ; {K1} et les "
    "lois des 11 cartes de la génération 1, prises toutes, pour la génération 2 (champ des « retenues » non lu : décision "
    "de la mère, R-2992, remarque F-4 du tour 4 ; d'après le verdict de v67, § 3, V-2, V-7 et V-8, et les faits du "
    "collisionneur, l. 34, les 11 cartes de la génération 1 ont toutes été retenues : cette archive est donc celle de "
    "v67, égalité non vérifiée sur le relevé).")
dec("pa-interdits",
    "- **Interdits** : aucun verdict (promotion, rejet, mort) du juge de v67 n'est lu ni rapproché de la décision de la "
    "règle ; les lois « retenues » qui entrent dans l'archive de la génération 2 sont un **résultat du juge** lu comme "
    "liste de lois, dit : la génération 2 de la partie A montre la dépendance indirecte de la règle aux verdicts (N-058, "
    "N-053 point 5), sans rien décider ;",
    "- **Interdits** : aucun verdict ni résultat du juge de v67 (promotion, rejet, mort, champ des « retenues ») n'est lu "
    "ni rapproché de la décision de la règle, **sans exception** (R-2992) ; la génération 2 de la partie A illustre la "
    "dépendance indirecte qu'aurait la règle aux verdicts au-delà de la génération 1 (N-058, N-053 point 5) seulement "
    "parce que son archive coïncide, dans v67, avec celle des retenues, sans rien décider ;")
dec("pa-arret",
    "| partie A : un verdict du juge de v67 lu (promotion, rejet, mort ; **hors** la liste des lois retenues, seule lecture "
    "permise du résultat du juge, lue comme liste de lois : « Interdits »), ou un seuil changé après sa lecture | partie A "
    "invalide ; partie B inchangée | lecture des seules lois, liste des retenues comprise | champ `promue` lu : refus ;",
    "| partie A : un verdict ou un résultat du juge de v67 lu (promotion, rejet, mort, champ des « retenues » : aucune "
    "exception, R-2992 ; « Interdits »), ou un seuil changé après sa lecture | partie A invalide ; partie B inchangée | "
    "lecture des seules lois, de leur proposeur et de leur génération ; archive de la génération 2 = {K1} et toutes les "
    "cartes de la génération 1 | champ `promue` lu : refus ; champ des retenues lu : refus ;")
dec("pa-choix-9",
    "sans aucun verdict du juge (les lois retenues de la génération 2 : « Partie A », « Interdits »).",
    "sans aucun verdict du juge. **Précisé (R-2992)** : l'archive de la génération 2 est {K1} et toutes les cartes de la "
    "génération 1, sans lire le champ des « retenues » (« Partie A », « Interdits », liste d'arrêt).")

# 3d. Points ouverts de « Choix et doutes » : la recommandation écrite (dont la sonde neuve, exigée).
dec("choix-titre",
    "(tranchés par la mère le 16 novembre, R-2977, aux points 2, 4, 5, 6, 9 et 11 ; points 1, 3, 7, 8, 10 et 10 bis encore "
    "ouverts, à trancher avant scellement ; recommandations ajoutées aux points 1, 7, 8, 10 et 10 bis, défaut de 48 heures)",
    "(tranchés par la mère le 16 novembre : R-2977 aux points 2, 4, 5, 6, 9 et 11 ; R-2992 aux points 1, 3, 7, 8, 10 et "
    "10 bis, qui prennent la recommandation écrite, et aux points 5, amendé, et 9, précisé ; aucun point ouvert)")
dec("choix-1",
    "Recommandation : oui (le bloc gelé fait foi ; un plafond plus bas arrêterait le crible) ; confiance 0,8.",
    "Recommandation : oui (le bloc gelé fait foi ; un plafond plus bas arrêterait le crible) ; confiance 0,8. "
    "**Tranché (R-2992)** : oui (recommandation prise).")
dec("choix-3",
    "Recommandation : garder\n   les quatre ; confiance 0,6.",
    "Recommandation : garder\n   les quatre ; confiance 0,6. **Tranché (R-2992)** : les quatre (recommandation prise).")
dec("choix-7",
    "M = 2 seulement si l'essai à blanc le tient ; confiance 0,6.",
    "M = 2 seulement si l'essai à blanc le tient ; confiance 0,6. **Tranché (R-2992)** : recommandation prise, la règle "
    "portant sur B_a et M, N étant fixé à 20.")
dec("choix-8",
    "Recommandation : l'exiger, le lanceur étant neuf ; confiance 0,55.",
    "Recommandation : l'exiger, le lanceur étant neuf ; confiance 0,55. **Tranché (R-2992)** : exigée (recommandation "
    "prise) ; lignes κv1 à 104,39 et κv2 à 100,28 USD (sections « Devis » et « Lignes de GO proposées »).")
dec("choix-10",
    "Recommandation : oui ; confiance 0,6.",
    "Recommandation : oui ; confiance 0,6. **Tranché (R-2992)** : oui (recommandation prise).")
dec("choix-10bis",
    "Recommandation : (a) ; confiance 0,6 ; défaut après 48 heures : (a).",
    "Recommandation : (a) ; confiance 0,6 ; défaut après 48 heures : (a). **Tranché (R-2992)** : (a), appliqué (étage 5, "
    "V4, « Seuil », « Comparaisons et corrections », « Écarts »).")
dec("dix-10",
    "choix tranchés en partie par la mère (R-2977), les autres à trancher\n    avant scellement (section « Choix et "
    "doutes »).",
    "choix tranchés par la mère (R-2977, puis R-2992 pour les points\n    restés ouverts et pour N = 20 ; section « Choix "
    "et doutes »).")
dec("sonde-etape-2",
    "sonde neuve exigée ou non, décidé avant le scellement (section « Devis »).",
    "sonde neuve exigée (point 8 de « Choix et doutes », R-2992 ; section « Devis »).")
dec("sonde-arret",
    "(si la sonde neuve est exigée, décision écrite avant le scellement)",
    "(sonde neuve exigée : point 8 de « Choix et doutes », R-2992)")
dec("sonde-devis-table",
    "sonde neuve : **exigée ou non, décidé avant le scellement** (si elle l'est, les lignes κv1 et κv2 passent à 104,39 et "
    "100,28 USD, total 204,67 ;",
    "sonde neuve : **exigée** (point 8 de « Choix et doutes », R-2992 ; les lignes κv1 et κv2 passent à 104,39 et "
    "100,28 USD, total 204,67 ;")
dec("sonde-regle-a",
    "(a) les pires cas (plafonds de session du bloc gelé × N, machine 3,00) et les montants des lignes de GO κv1 et κv2 "
    "**ne changent pas** avec le pilote, seulement avec N et avec la décision sur la sonde neuve (point 8 de « Choix et "
    "doutes », écrite avant le scellement : + 4,39 sur κv1 et + 3,68 sur κv2, à N = 20 comme à N = 24)",
    "(a) les pires cas (plafonds de session du bloc gelé × N, N = 20, machine 3,00, sonde neuve 8,07) et les montants des "
    "lignes de GO κv1 et κv2 (104,39 et 100,28 USD, sonde neuve comprise : + 4,39 sur κv1 et + 3,68 sur κv2 ; point 8 de "
    "« Choix et doutes », tranché par R-2992) **ne changent pas** avec le pilote")
dec("sonde-go-kv1-corps",
    "un appel par proposeur et par monde, au plus 6 cartes, aucune reprise ;",
    "un appel par proposeur et par monde, au plus 6 cartes, aucune reprise ; sonde neuve du chemin des relais du lanceur du "
    "crible, part sur crédits 4,39 USD (forme de la ligne s1 de la sonde v74), jouée et son relevé conforme avant tout appel "
    "du crible ;")
dec("sonde-go-kv1-montant",
    "| 100 USD (sur crédits) |",
    "| 104.39 USD (sur crédits) |")
dec("sonde-go-kv2-corps",
    "aucun réglage envoyé, machine jetable 3 USD ;",
    "aucun réglage envoyé, machine jetable 3 USD, part hors crédits de la sonde neuve 3,68 USD (forme de la ligne s2 de la "
    "sonde v74) ;")
dec("sonde-go-kv2-montant",
    "| 96.60 USD |",
    "| 100.28 USD |")
dec("documents",
    "R-2977 (décisions de la mère sur les choix de ce texte), R-2981, R-2982 (registre vivant)",
    "R-2977 et R-2992 (décisions de la mère sur les choix de ce texte ; R-2992 amende R-2977), R-2981, R-2982 (registre "
    "vivant)")

# 3e. Mentions fausses « rédacteur modèle C » (R-2992, point 0 : les rédacteurs de corrections étaient du modèle A).
dec("role-entete-2",
    "- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées par un rédacteur neuf (modèle C ; il n'a écrit ni le",
    "- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées par un rédacteur neuf (modèle A — « modèle C » écrit\n"
    "  ici par erreur dans les brouillons 2 à 6, corrigé d'après R-2992, point 0 ; il n'a écrit ni le")
dec("role-entete-3",
    "- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées par un rédacteur neuf (modèle C ; il n'a écrit ni le",
    "- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées par un rédacteur neuf (modèle A, même correction ; "
    "il n'a écrit ni le")
dec("role-entete-5",
    "(modèle C, **écart de rôle à\n  R-2982, déclaré** ; il n'a écrit ni le brouillon 1, ni les brouillons 2 à 4,",
    "(modèle A, même correction ;\n  l'écart de rôle à R-2982 déclaré ici n'a pas eu lieu ; il n'a écrit ni le brouillon 1, "
    "ni les brouillons 2 à 4,")
dec("role-entete-6",
    "(modèle C, **écart de rôle à\n  R-2982, déclaré** ; il n'a écrit ni le brouillon 1, ni les brouillons 2 à 5,",
    "(modèle A, même correction ;\n  l'écart de rôle à R-2982 déclaré ici n'a pas eu lieu ; il n'a écrit ni le brouillon 1, "
    "ni les brouillons 2 à 5,")
dec("role-cl1-application",
    "  - **Application** : par un rédacteur neuf (modèle C ; il n'a écrit ni le brouillon 1, ni le rapport, ni aucune pièce "
    "citée),",
    "  - **Application** : par un rédacteur neuf (modèle A ; « modèle C » écrit ici par erreur, corrigé d'après R-2992, "
    "point 0 ; il n'a écrit ni le brouillon 1, ni le rapport, ni aucune pièce citée),")
dec("role-cl1-roles",
    "celles-ci l'ont été par un rédacteur du\n    modèle C sur consigne de la session mère :",
    "celles-ci l'ont été par un rédacteur du\n    modèle A (« modèle C » écrit ici par erreur, R-2992, point 0) :")
dec("role-cl2-application",
    "  - **Application** : par un rédacteur neuf (modèle C ; il n'a écrit ni le brouillon 1, ni le brouillon 2,",
    "  - **Application** : par un rédacteur neuf (modèle A ; « modèle C » écrit ici par erreur, R-2992, point 0 ; il n'a "
    "écrit ni le brouillon 1, ni le brouillon 2,")
dec("role-cl2-roles",
    "elles l'ont été\n    par un rédacteur neuf du modèle C, sur consigne de la session mère : **écart de rôle à R-2982, "
    "déclaré**.",
    "elles l'ont été\n    par un rédacteur neuf du modèle A (« modèle C » et « écart de rôle à R-2982 » écrits ici par "
    "erreur, R-2992, point 0) : rôles tenus.")
dec("role-cl4-application",
    "par un rédacteur neuf du modèle C (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 4,",
    "par un rédacteur neuf du modèle A (« modèle C » écrit ici par erreur, R-2992, point 0 ; il n'a écrit ni le brouillon 1, "
    "ni les brouillons 2 à 4,")
dec("role-cl4-ecart",
    "  - **Écart de rôle à R-2982, déclaré** : R-2982 veut les corrections écrites par le modèle A, et le rapport le redit "
    "(« à\n    écrire par l'auteur (modèle A) ») ; elles sont appliquées ici par un rédacteur du modèle C, sur consigne de "
    "la session\n    mère, et les « nouveau » sont ceux du lecteur du tour 4 (modèle C), recopiés sans retouche : à la mère "
    "de dire si cela\n    suffit ou si un rédacteur du modèle A doit les reprendre.",
    "  - **Rôles (corrigé d'après R-2992, point 0)** : R-2982 veut les corrections écrites par le modèle A, et le rapport le "
    "redit (« à\n    écrire par l'auteur (modèle A) ») ; elles ont été appliquées par un rédacteur du modèle A (le « modèle "
    "C » et l'écart\n    de rôle déclaré ici étaient faux) ; les « nouveau » sont ceux du lecteur du tour 4 (modèle C), "
    "recopiés sans retouche.")
dec("role-cl5-application",
    "par un rédacteur neuf du modèle C (il n'a écrit ni le brouillon 1, ni les brouillons 2 à 5,",
    "par un rédacteur neuf du modèle A (« modèle C » écrit ici par erreur, R-2992, point 0 ; il n'a écrit ni le brouillon 1, "
    "ni les brouillons 2 à 5,")
dec("role-cl5-ecart",
    "  - **Écart de rôle à R-2982, déclaré** : R-2982 veut les corrections écrites par le modèle A, et le rapport le redit "
    "(« à\n    écrire par l'auteur (modèle A, R-2982) ») ; elles sont appliquées ici par un rédacteur du modèle C, sur "
    "consigne de la\n    session mère, et les « nouveau » sont ceux du lecteur du tour 5 (modèle C), recopiés sans "
    "retouche : à la mère de dire si\n    cela suffit ou si un rédacteur du modèle A doit les reprendre (point pour la mère "
    "2 du rapport).",
    "  - **Rôles (corrigé d'après R-2992, point 0)** : R-2982 veut les corrections écrites par le modèle A, et le rapport le "
    "redit (« à\n    écrire par l'auteur (modèle A, R-2982) ») ; elles ont été appliquées par un rédacteur du modèle A (le "
    "« modèle C »\n    et l'écart de rôle déclaré ici étaient faux) ; les « nouveau » sont ceux du lecteur du tour 5 "
    "(modèle C), recopiés sans retouche.")

# 4. Couples propres.
PROPRES = []

PROPRES.append(("titre",
    "(regroupement, sans juge) — brouillon 6",
    "(regroupement, sans juge) — brouillon 7"))

PROPRES.append(("en-tete",
    "  pièce citée), écrit et scellé le 2026-11-16T14:46:59Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).",
    "  pièce citée), écrit et scellé le 2026-11-16T14:46:59Z (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).\n"
    "- Brouillon 7 : corrections du tour 6 de contre-lecture et décisions de la mère (R-2992) appliquées par un rédacteur neuf\n"
    "  (modèle A, comme le veut R-2982 ; il n'a écrit ni le brouillon 1, ni les brouillons 2 à 6, ni aucun des six rapports,\n"
    f"  ni aucune pièce citée), écrit et scellé le {HEURE} (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »)."))

PROPRES.append(("statut",
    "**Statut.** Brouillon 6, **contre-lu cinq fois** (tours 1 à 5, corrections appliquées, section « Contre-lecture ») ; **non scellé",
    "**Statut.** Brouillon 7, **contre-lu six fois** (tours 1 à 6, corrections appliquées, section « Contre-lecture ») ; **non scellé"))

PROPRES.append(("statut-tour",
    "comme texte qui fait foi** (R1, R2) ; tour 6 de contre-lecture à faire.",
    "comme texte qui fait foi** (R1, R2) ; contrôle des couples du tour 6 et des décisions de R-2992 (différentiel) à faire\n"
    "avant scellement (point pour la mère 1 du rapport du tour 6)."))

PROPRES.append(("validateur",
    "aucun défaut sur ce brouillon 6 (vérifié avant",
    "aucun défaut sur ce brouillon 7 (vérifié avant"))

PROPRES.append(("contre-lecture-tete",
    "Tours 1 à 5 faits (entrées « Contre-lecture 1 » à « Contre-lecture 5 » ci-dessous)",
    "Tours 1 à 6 faits (entrées « Contre-lecture 1 » à « Contre-lecture 6 » ci-dessous)"))

NOMS_D = ", ".join(f"« {n} »" for n, _, _ in D)
ANCRE_CL6 = "## Annexe A — comptes exacts (sans donnée, sans tirage, sans appel)"
CL6 = """- **Contre-lecture 6** (tour 6, sur le brouillon 6) : sous-agent neuf du modèle C, qui n'a écrit aucune pièce citée (ni ce
  texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 à 5) et n'a pas touché les dossiers du premier
  lecteur (modèle B) ; lecture de 14:47:29Z à 14:52Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b4-tour3-v1.md`, empreinte
  `@@RAPPORT_SHA@@` ; brouillon relu : `crible-v-brouillon6.md`, empreinte
  `@@SOURCE_SHA@@`. Verdict : **corrections** (0 majeure, 6 mineures D6-01 à D6-06, 4 remarques
  facultatives F-D6-1 à F-D6-4) ; aucun « a_refaire » ; application du tour 5 jugée fidèle ; validateur sans défaut.
  - **Application** : par un rédacteur neuf du **modèle A**, comme le veut R-2982 (il n'a écrit ni le brouillon 1, ni les
    brouillons 2 à 6, ni aucun des six rapports, ni aucune pièce citée), au moyen du programme
    `appliquer-corrections-crible-v-brouillon7.py` (même dossier, empreinte dans son compagnon `.sha256`) : les 7 couples
    « ancien → nouveau » des corrections D6-01 à D6-06 (D6-01, D6-02, D6-03, D6-04a, D6-04b, D6-05, D6-06) sont lus dans le
    rapport lui-même ; deux « nouveau » reçoivent une retouche déclarée (ci-dessous) ; s'y ajoutent les couples des
    décisions de la mère (R-2992) et les couples propres ; chaque « ancien » vérifié présent une seule fois dans le
    brouillon 6 ; aucun chevauchement ; cible neuve ; écriture le @@HEURE@@ (`date -u`). Aucun appel de modèle, aucune
    dépense, aucune machine, aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote
    non ouverts ; issue et taux du pilote non lus).
  - **Réponse point par point** :
    - D6-01 (sources des durées que le budget lit au pilote) : **acceptée**, sans retouche : point (8) ajouté aux « Points à
      remesurer » (durées de la mise en place, de la mesure et du rapatriement, lues dans le journal d'états de la machine
      du pilote, entre deux états consécutifs nommés ; sans état qui la borne, « non lançable » et mot de la mère).
    - D6-02 (mesure de l'énumération exacte du placebo) : **acceptée, avec une retouche** : la mesure est portée par l'étape 0
      (« Essais »), processeur seul, avant le scellement ; le cas mesuré est N = 20 seul, n_c = 20, k_R = 10 (184 756
      ensembles), le cas N = 24 du rapport étant sans objet depuis R-2992 (N = 20 dans tous les cas).
    - D6-03 (durée des appels dans l'attendu de la machine) : **acceptée**, sans retouche : ⌈N/M⌉ fois la durée moyenne, sur
      les mondes du pilote, du plus long des quatre appels d'un monde, un appel au-delà de B_a pris égal à B_a.
    - D6-04 (tolérance de la réflexion de Pr-1 sur la seule ligne de Pr-1) : **acceptée**, sans retouche (D6-04a : la ligne
      κv2, part hors crédits, celle de Pr-1, le dit, κv1 restant sans exception ; D6-04b : κv2 reprend les conditions de
      κv1 sauf « coût au-dessus du pire cas = arrêt », qui reçoit pour Pr-1 la tolérance si la règle la retient). Conforme à
      R-2992 (tolérance écrite sur la seule ligne de GO de Pr-1).
    - D6-05 (montants des lignes de GO selon la sonde neuve) : **acceptée, avec deux retouches** : la sonde neuve est exigée
      (point 8 de « Choix et doutes », recommandation prise par R-2992), donc la phrase dit que les montants des lignes sont
      ceux de la branche « sonde neuve exigée » (104,39 et 100,28 USD), sans la sonde 100 et 96,60 ; la branche à 24 mondes
      (124,39 et 119,00) est retirée (R-2992) ; « ci-dessous » devient « ci-dessus » (la phrase suit les lignes). Les lignes
      κv1 et κv2 portent ces montants et la part de la sonde (couples « r2992-sonde-go-… »).
    - D6-06 (marque de gras non fermée) : **acceptée**, sans retouche.
    - Remarques facultatives : F-D6-4, pour sa partie « partie A sans le champ des retenues » (F-4 du tour 4), est
      **appliquée** parce que la mère l'a décidée (R-2992) ; F-D6-1 (la règle de durée exige probablement M = 2 à 20 mondes),
      F-D6-2 (« la règle suivante » désigne deux règles), F-D6-3 (risque d'arrêt de Pr-1 non chiffré) et le reste de F-D6-4
      (V1, V3, V5 en comptes absolus, règle de pertinence, seuil sur k_R pour n_c de 16 à 19) : **non appliquées** (non
      exigées ; consigne de ce tour bornée aux corrections et aux décisions de la mère) ; transmises à la mère. Avec N = 20
      dans tous les cas, la partie « à 24 mondes » de F-D6-1 et de F-D6-4 est sans objet.
  - **Décisions de la mère appliquées (R-2992, amendant R-2977)**, par couples nommés « r2992-… » :
    - **N = 20 dans tous les cas** (la règle « 24 si le taux par appel du pilote est sous 0,95 » de R-2977 est retirée) :
      « En dix lignes » (points 2, 6, 8), notations, placebo (au plus C(20, 10) = 184 756), minimum (16 sur 20), table
      W_min (n_c de 16 à 20 → 4), seuil d'épargne et de perte, partie B, graines, étapes 2 et 3, section « Taille » (N = 20
      gelé dès ce texte ; le taux du pilote ne sert plus qu'à la probabilité d'atteindre le minimum, à titre d'information),
      ordre de la règle de B_a et de M, table de durée, points à remesurer (3), ligne d'arrêt de la minuterie, lignes de GO,
      point 5 de « Choix et doutes » ; les sorties recopiées de l'annexe A (points 11 et 12) restent, leurs lignes à 24
      mondes dites sans objet.
    - **Étage 5 (ablation) rapporté sans verdict, hors des critères gelés** (N-045 point 3 ; point 10 bis, option (a)) :
      table des critères, V4 (sans zone de réfutation), lecture des prédictions, « Ce que serait chaque issue », « Seuil »,
      « Comparaisons et corrections », « Écarts », point 7 de « En dix lignes ».
    - **Partie A** : archive de la génération 2 = {K1} et toutes les cartes de la génération 1, sans lire le champ des
      « retenues » de v67 (remarque F-4 du tour 4) ; plus aucune exception à « sans aucun verdict du juge » ; ligne d'arrêt
      réécrite (champ des retenues lu : refus) ; point 9 de « Choix et doutes » précisé.
    - **Points ouverts de « Choix et doutes »** (1, 3, 7, 8, 10, 10 bis) : la recommandation écrite est prise ; d'où la sonde
      neuve **exigée** (point 8), reportée à l'étape 2, à la ligne d'arrêt du relevé de sonde, à la table et à la règle
      d'avance (a) du devis, à « En dix lignes » (point 8 : 204,67 USD au pire avec la sonde) et aux lignes de GO (κv1 104,39
      USD, κv2 100,28 USD, part de la sonde dite dans chacune, forme des lignes s1 et s2 de la sonde v74).
    - **Mentions fausses « rédacteur modèle C »** (R-2992, point 0 : les rédacteurs de corrections étaient du modèle A,
      vérifié par la mère) : corrigées dans l'en-tête (brouillons 2, 3, 5, 6) et dans les entrées « Contre-lecture 1, 2, 4
      et 5 » ; les « écarts de rôle à R-2982, déclarés » de ces entrées n'ont pas eu lieu. Les lecteurs étaient du modèle C :
      ces mentions restent.
    - **Tolérance de la réflexion de Pr-1 écrite sur la seule ligne de GO de Pr-1** (κv2) : par D6-04a et D6-04b.
    - R-2992 ajoutée aux documents qui font foi.
    - Liste des couples : @@NOMS_D@@.
  - Décisions de R-2977 : relues ; archive {K1}, mondes séparés, dollars au prix public, lecture de GO-2026-11-15-06 pour
    l'essai, partie A permise et descriptive sur données déjà vues, tension avec N-058 à dire à Lazar : présentes dans ce
    texte ; « 24 mondes sous 0,95 » retirée par R-2992 ; « recommandations de l'auteur sauf mention » vaut désormais pour
    tous les points (R-2992).
  - « Points pour la mère » 1 à 9 du rapport : (1) non scellé ; ce brouillon 7 demande le contrôle limité aux couples que le
    rapport recommande (différentiel), qui doit couvrir aussi les couples « r2992-… » ; (2) rôles : réglés par R-2992,
    point 0 (correcteurs du modèle A) ; (3) N = 20 : appliqué ; (4) date de lancement fixée par le code neuf : transmis ;
    (5) tolérance de Pr-1 : écrite sur κv2 seule ; risque d'arrêt non chiffré (F-D6-3) : transmis ; (6) étage 5 : option (a)
    appliquée ; (7) points de « Choix et doutes » : tranchés par R-2992 ; (8) enveloppe des cinq cribles et champs du
    lecteur du pilote : transmis (la ligne « Le témoin positif du pilote » des points à remesurer reste : V1 et V6 ne sont
    pas des prédictions à l'aveugle dans le texte qui fera foi, comme le dit l'étape 2) ; (9) fait par cette entrée.
  - Couples propres de ce tour : « titre » (brouillon 7) ; « en-tete » (ligne « Brouillon 7 » de l'en-tête) ; « statut » et
    « statut-tour » ; « validateur » ; « contre-lecture-tete » (tours 1 à 6) ; « contre-lecture-6 » (cette entrée). Aucun ne
    touche un critère, un seuil, une graine ni une ligne d'arrêt ; les couples « r2992-… » en touchent (étage 5, N, partie
    A, sonde), sur décision de la mère.
  - **Rôles** : corrections écrites par le modèle A, conformément à R-2982. Le contrôle suivant doit être fait par un lecteur
    neuf : ni le lecteur du tour 6, ni ce rédacteur, ni les lecteurs et rédacteurs des tours 1 à 5, ni l'auteur du
    brouillon 1. **Fichiers à lui donner** : ce texte, le brouillon 6 pour la comparaison, le rapport du tour 6, le
    programme `appliquer-corrections-crible-v-brouillon7.py`, la ligne R-2992 de `registres/decisions.md`.

@@ANCRE@@"""
CL6 = (CL6.replace("@@RAPPORT_SHA@@", RAPPORT_SHA).replace("@@SOURCE_SHA@@", SOURCE_SHA)
       .replace("@@HEURE@@", HEURE).replace("@@NOMS_D@@", NOMS_D).replace("@@ANCRE@@", ANCRE_CL6))
if "@@" in CL6:
    arret("marque @@ restante dans l'entrée Contre-lecture 6")
PROPRES.append(("contre-lecture-6", ANCRE_CL6, CL6))

# 5. Contrôles : chaque « ancien » une seule fois, aucun chevauchement, noms uniques.
tous = couples + D + PROPRES
noms = [n for n, _, _ in tous]
if len(set(noms)) != len(noms):
    arret("noms de couples en double")
places = []
for nom, ancien, nouveau in tous:
    n = texte.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » présent {n} fois dans la pièce de départ")
    debut = texte.index(ancien)
    places.append((debut, debut + len(ancien), nom))
places.sort()
for (d1, f1, n1), (d2, f2, n2) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 6. Application d'un coup, de la fin vers le début (positions de la pièce de départ).
par_nom = {nom: (ancien, nouveau) for nom, ancien, nouveau in tous}
cible = texte
for debut, fin, nom in sorted(places, reverse=True):
    cible = cible[:debut] + par_nom[nom][1] + cible[fin:]
for nom, ancien, nouveau in tous:
    if nouveau and nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

# 7. Écriture sans écraser.
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"écrit : {CIBLE}")
print(f"heure : {HEURE}")
print(f"couples du rapport : {len(couples)} ; couples de R-2992 : {len(D)} ; couples propres : {len(PROPRES)}")
print(f"empreinte : {sha(CIBLE)}")
