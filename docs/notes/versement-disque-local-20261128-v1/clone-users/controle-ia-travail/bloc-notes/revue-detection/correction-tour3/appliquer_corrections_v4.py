"""Synthèse « comment détecter » v4 : v3 + constats VV3-sens-01 à 14 et VV3-fidelite-01 à 07.

Chiffres et phrases ajoutés : repris des deux rapports de vérification du tour 2 (relus à la page par leurs auteurs) ;
aucun chiffre neuf. Chaque remplacement doit trouver son texte d'origine exactement une fois ; les deux blocs (section 1,
paragraphe « Confiance ») sont remplacés entre leurs marqueurs. Sinon arrêt, rien n'est écrit.
Usage : python3 -I appliquer_corrections_v4.py V3 V4 HEURE
"""
import sys
from pathlib import Path

src, dst, heure = sys.argv[1:4]
t = Path(src).read_text(encoding="utf-8")


def bloc(texte, debut, fin, nouveau):
    i, j = texte.find(debut), texte.find(fin)
    if i < 0 or j < 0 or j <= i or texte.count(debut) != 1 or texte.count(fin) != 1:
        sys.exit(f"bloc introuvable ou ambigu : {debut[:40]!r} → {fin[:40]!r}")
    return texte[:i] + nouveau + texte[j:]


# --- section 1 (VV3-sens-01, 02, 03, 10, 11, 13 ; VV3-fidelite-02, 04) -----------------------------------------------
S1 = """## 1. Verdict

1. La détection interne marche quand la tromperie est **écrite dans le texte lu**, ou avec des **données du même
   domaine** ou très larges. La lecture à **une seule position après une question ajoutée** après l'action (réponse
   imposée) est appuyée hors domaine et à grande échelle, avec données larges et contraste [OA table 15 ; CA p. 7-8]. Sur
   les cas sur consigne, elle ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8 ; PAR table 3, sonde Pairs : 0,849 et
   0,879 contre 0,964 au sous-rendement]. À consigne égale (sous-rendement), elle s'effondre avec les sondes apprises sur
   « Roleplaying », qui lisent la consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] ; entre consignes, la
   même sonde sépare presque parfaitement [AP p. 18]. Son issue dépend donc des données d'apprentissage de la sonde. La
   détection gagne avec la **taille ou la capacité du modèle**. Par la taille, [CA] place la rupture entre 2 et 9
   milliards, dans la famille Qwen3.5 (p. 8 ; liste p. 18) ; par la capacité, la place de Llama-3.1-8B n'est pas mesurée
   (R8 : question) ; [DYL] range Llama-3.3-70B, souvent pris pour les organismes, sous Qwen 3.5 2B Reasoning (p. 5) : si
   Llama-3.1-8B est en dessous, il tomberait là où [CA] mesure des sondes faibles (transposition entre papiers, R8).
   **Plusieurs couches** n'ont qu'un appui, sur une autre tâche [CC p. 8] ; sur ce même modèle, le choix de la couche
   compte peu [BX p. 3]. Le dernier jeton seul, sans question, échoue sur les enjeux [MK p. 4] ; chez Apollo, une sonde
   « Roleplaying » apprise et lue sur les dernières positions est « comparable » en aire, avec un rappel à 1 % de faux
   positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes les positions (moyenne), mais en
   dessous de la sonde Instructed-Pairs [AP p. 23].
2. Deux types de contraste sont à séparer. **P3-P3** oppose deux consignes : le saboteur a une consigne privée, l'honnête
   n'en a pas ([P] l. 328-332). **T1** oppose, sous la même consigne, des actions qui gonflent et d'autres non ([P]
   l. 238-241). Analogues publiés de **P3-P3** (consignes différentes, consigne non notée) : sur « Backdoors », à 70
   milliards, sonde de recette « Pairs » (celle de la sonde de tromperie de P3, [P] l. 293-296), jetons publics seuls :
   moyenne 0,844, **maximum 0,768** [PAR table 3, p. 7 ; p. 3-4] (réserves : code fourni par la consigne, hors politique,
   p. 4 ; réponses honnêtes déjà plus hautes que presque tout Alpaca, p. 9) ; mensonges sur consigne, sonde en moyenne,
   consigne non notée : 0,95 ; 0,60 ; 0,69 ; 0,58 selon le modèle [LB p. 6-7 ; table 6, p. 54] ; « Varied Deception » :
   Qwen3-8B 0,74 en exactitude équilibrée [DYL p. 5 ; table 9, p. 28] ; sur ce même modèle, rappel à 1 % de faux positifs
   contre la conversation ordinaire, consigne et raisonnement exclus du score : 0,03 [BX p. 6 ; table 1]. Analogues de
   **T1** (consigne égale ; l'étiquette vient du choix du modèle) : 0,81 et 0,63 sur ce même modèle [BX p. 5-6 ; consigne
   unique, p. 4 ; étiquettes, p. 12], 0,606 [YS p. 3] ; l'empan public de [BX] porte sans doute une justification fausse
   (p. 12-13), et pour [YS] l'exclusion du raisonnement n'est pas dite : « rien d'écrit dans l'empan lu » n'est établi pour
   aucun des deux. Le 0,5 de [BX] vient d'un organisme affiné, sans consigne ni raisonnement, sondes réentraînées sur lui,
   organisme peut-être incomplet [BX p. 4, p. 8] ; P3 n'est pas affiné. [AU] : 0,653 sur Phi-4, sonde lue sur les 10
   derniers jetons, agrégation non dite (p. 7) ; la notation « +X » rend ambigu ce qui est lu : prise à la lettre,
   « Action » est l'action sans contexte, et le montage de P3 (rôle dans le contexte) serait « +System (AUC = 1.000) »
   (p. 6). **La littérature ne prévoit ni n'exclut le nul de P3** : à consignes différentes, de 0,58 à 0,95 selon le
   modèle, 0,768 au maximum à 70 milliards, rappel de 0,03 sur ce même modèle quand ni consigne ni raisonnement ne sont
   notés ; aucun de ces travaux ne mesure contre un plancher apparié. [BX], [YS] et [LB] agrègent par la moyenne, [PAR]
   donne moyenne et maximum, [AU] lit les derniers jetons ; P3, par le maximum ou l'attention. Une sonde qui lit le régime
   de consigne **séparerait** le saboteur de l'honnête [KU p. 9 ; AP p. 18] : ce fait prédit un faux positif sur P3-P3,
   pas un nul. Le nul ne prouve pas que l'information manque : même modèle, même couche, une sonde apprise sur la cible
   (sous-rendement sur consigne, raisonnement écrit peut-être inclus) atteint 0,869 [YS p. 3] ; « l'information est là »
   reste une hypothèse.
3. Aucun travail lu ne mesure contre un plancher apparié comme le nôtre, ni ne teste un **nombre faux dans un champ**
   (R8 : questions). Levier le mieux appuyé : **données du domaine**. La **lecture à une seule position après une
   question** est à éprouver, pas à présumer (point 1). Toujours lire contre le témoin, la mention, T1 et T4.

"""
t = bloc(t, "## 1. Verdict\n", "## 2. Ce qu'ont fait Anthropic et les autres\n", S1)

# --- section 5, paragraphe « Confiance » (VV3-sens-09 ; VV3-fidelite-07) ----------------------------------------------
CONF = """**Confiance** (jugement du correcteur ; revue depuis la v1, VV2-sens-09 et VV3-sens-09). ≈ 40 % (v1 : 60 %, pour E1
et E2 ensemble) que E1 dise d'où vient le nul (lecture ou direction ; un oracle non au-dessus ne dit pas « pas de
trace ») : les bras du champ sont déjà vus (T2), le bras « avant le champ » voit des nombres déjà écrits, et T1 n'y vaut
qu'avec T4. ≈ 15 à 25 % (v1 : 25 à 35 %) qu'une sonde apprise sans l'organisme passe le plancher **et** T1, T3 et T4 sur
ce modèle : T1 s'ajoute, à consigne égale, et rien de publié ne le passe sur un cas de ce type ; en sens contraire, le
montage corrigé lit des données du domaine, que [K] désigne comme le premier levier (« Deception −0.416 » hors domaine,
table 1, p. 7). L'oracle passera probablement son plancher, les contextes différant ; T1, T3 et T4 sont l'obstacle.

"""
t = bloc(t, "**Confiance** (jugement du correcteur", "**Nœuds de Lazar.**", CONF)

R = []  # (ancien, nouveau), chacun trouvé exactement une fois

R.append(("— synthèse v3\n", "— synthèse v4\n"))
R.append((
"  sections 1, 3, 4 et 5 : verdict, pouvoirs, expériences, recommandation, confiances, nœuds.\n- **Sources.**",
"  sections 1, 3, 4 et 5 : verdict, pouvoirs, expériences, recommandation, confiances, nœuds.\n"
f"- **v4 (correction, tour 3).** Par la session 14, 2026-10-20 vers {heure} UTC, qui n'a écrit ni la v1, ni la v2, ni la\n"
"  v3, ni les extractions, ni les vérifications. Part de la v3 (`ec4239e9…`) et applique les constats des deux\n"
"  vérifications du tour 2 : sens, VV3-sens-01 à 14 (`…/revue-detection/verification-v3-sens-v1.md`, `256f9181…`, « non\n"
"  conforme ») ; fidélité, VV3-fidelite-01 à 07 (`…/revue-detection/verification-v3-fidelite-v1.md`, `987b39ea…`,\n"
"  « conforme après corrections »). Phrases et chiffres ajoutés : repris de ces deux rapports, qui les ont relus à la\n"
"  page et à la ligne ; aucun chiffre neuf. Deux faits datés du dépôt ajoutés : compte Vast.ai à recharge automatique\n"
"  (R-283) ; proposition P-015 (périmètre de T0.6 en mode « coût »). Décisions et raisons :\n"
"  `…/revue-detection/traitement-verification-synthese-tour3-v1.md`. Rien d'autre n'est changé. Le fond change en\n"
"  sections 1, 3, 4 et 5 : contrastes séparés par type (P3-P3 contre T1), prédiction de E2, pouvoirs des rangs 2, 3, 4,\n"
"  6 et 9, confiances, nœuds.\n"
"- **Sources.**"))
R.append((
"Les sections 1, 3, 4 et 5 reprennent les chiffres des sections 2.1 et 2.2, où la phrase est donnée.\n",
"Les sections 1, 3, 4 et 5 reprennent les chiffres des sections 2.1 et 2.2, où la phrase est donnée. v4 : phrases et\n"
"  chiffres ajoutés repris des rapports du tour 2, à recontrôler à la page par la vérification du tour 3.\n"))

# 2.1 : [BX], [PAR], [AU] (VV3-sens-01, 02, 03 ; VV3-fidelite-02)
R.append((
"montage le plus proche de P3 : « Score Filtering » (0,81) ou consigne remplacée (0,63), pas l'organisme affiné ;",
"à consigne égale (type T1 : « a system prompt that instructs the model to underperform on questions related to WMDP », "
"p. 4 ; « For sandbagging the labels are derived from step-1 sandbagging decisions », p. 12) : « Score Filtering » (0,81) "
"ou consigne remplacée (0,63) ; l'empan public porte sans doute une justification fausse (« Instead, give bad logic and "
"reasoning, resulting in an incorrect answer », p. 12) ; à consignes différentes (type P3-P3) : rappel contre la "
"conversation ordinaire (« distinguish transcripts containing normal conversational data from those exhibiting the "
"studied behavior », p. 6), 0,03 en « Score Filtering » (table 1) ; pas l'organisme affiné ;"))
R.append((
"question sans contraste 0,457 et 0,437 ; sur les cinq jeux",
"question sans contraste 0,457 et 0,437 ; « Backdoors » (consignes différentes : « The system prompt also informs the "
"assistant whether the provided code contains a backdoor », p. 4), sonde Pairs : moyenne 0,844, maximum 0,768, questions "
"0,832 et 0,849 ; sur les cinq jeux"))
R.append((
"| Among Us [AU] | Phi-4, sondes génériques apprises sur RepEng, couche 20 (p. 6-7) ;",
"| Among Us [AU] | Phi-4, sondes génériques apprises sur RepEng, couche 20 (p. 6-7) ; « the last 10 tokens for each "
"datapoint », agrégation au test non écrite (p. 7) ;"))
R.append((
"légendes imprimées de la figure 6 (p. 6) : toutes actions (77 % sans parole) : « Action (AUC = 0.653) » contre "
"« +Thinking (AUC = 0.948) » ;",
"légendes imprimées de la figure 6 (p. 6) : toutes actions (77 % sans parole) : « Action (AUC = 0.653) » contre "
"« +Thinking (AUC = 0.948) » et « +System (AUC = 1.000) » ; « Note that the “+X” notation means the prompt includes all "
"inputs above and including X » (p. 6) : prise à la lettre, « Action » est l'action sans contexte ;"))

# 2.2 « Pour P3 » (VV3-sens-14 a ; VV3-fidelite-03)
R.append((
"le mensonge de P3 tient dans un champ, ce\n  qui sert le maximum",
"le mensonge de P3 peut tenir dans un champ, ce\n  qui sert le maximum"))
R.append((
"[PAR p. 7 ; MK p. 4 ; AP p. 22], vers le maximum\n  seulement sous dilution, au prix de faux positifs [GM table 3, p. 12].",
"[PAR p. 7 ; MK p. 4 ; AP p. 22], sauf la sonde RP de\n"
"  [PAR], où le maximum brut gagne sur trois des quatre autres jeux ; sous dilution, le maximum brut perd chez [PAR]\n"
"  (jeu « Dilution », table 3, p. 7 : Pairs, moyenne 0,931 contre maximum 0,811 ; RP, 0,907 contre 0,877), les maxima\n"
"  appris gagnent en contexte long chez [GM], au prix de faux positifs (table 3, p. 12)."))

# section 3
R.append((
"v3 : pouvoirs revus par le correcteur\n(VV2-sens-09) ;",
"v3 : pouvoirs revus par le correcteur\n(VV2-sens-09) ; v4 : rangs 2, 3, 4, 6 et 9 revus (VV3-sens-01, 02, 10) ;"))
R.append((
"| « deceptive prompt regime » [KU p. 9] ; entraînement sans tromperie réelle [AP p. 4] ;",
"| « deceptive prompt regime » [KU p. 9] : une telle sonde signale le régime de consigne (« flagging that a model is "
"operating under deceptive instructions even when its output happens to be correct », p. 9) ; même hypothèse pour la "
"sonde Instructed-Pairs (« activates somewhat when deception is incentivized (rather than performed) », [AP p. 18]) : "
"elle séparerait le saboteur de l'honnête, ce qui prédit un faux positif sur P3-P3, pas un nul ; entraînement sans "
"tromperie réelle [AP p. 4] ;"))
R.append((
"| **moyen** (v1 : fort) : sur consigne, la tromperie ne perd rien chez [K] (+0,035) ; les effets de l'origine des réponses "
"sont « often non-significant » [K table 1, p. 7] |",
"| **faible à moyen** (v1 : fort ; v3 : moyen) : il exige que la consigne du saboteur, « une règle de calcul », ne soit "
"pas lue comme un régime trompeur, sinon il prédit l'inverse du nul ; sur consigne, la tromperie ne perd rien chez [K] "
"(+0,035) ; les effets de l'origine des réponses sont « often non-significant » [K table 1, p. 7] |"))
R.append((
"| montages proches (rien d'écrit dans l'empan lu), en moyenne : 0,81, consigne et raisonnement dans le contexte "
"[BX p. 5] ; 0,63, consigne remplacée [BX p. 6] ; 0,653 contre 0,948, toutes actions [AU p. 6] ; 0,606 [YS p. 3] ; 0,5 "
"seulement sur organisme affiné [BX p. 8] ;",
"| type P3-P3 (consignes différentes, consigne non notée) : maximum 0,768 et moyenne 0,844 [PAR table 3, « Backdoors »] ; "
"0,58 à 0,95 [LB table 6] ; 0,74 [DYL table 9] ; rappel 0,03 [BX table 1] ; type T1 (consigne égale) : 0,81 et 0,63 "
"[BX p. 5-6], 0,606 [YS p. 3], pour lesquels « rien d'écrit dans l'empan lu » n'est pas établi ([BX p. 12-13] ; [YS] : "
"non dit) ; [AU] : 0,653, dix derniers jetons, agrégation non dite, « +System (AUC = 1.000) » selon la lecture de « +X » "
"[AU p. 6-7] ; 0,5 seulement sur organisme affiné [BX p. 8] ;"))
R.append((
"| **moyen** (v1 : fort) : les montages proches restent au-dessus du hasard ; le hasard ne vient que de l'organisme affiné |",
"| **moyen** (v1 : fort) : à consignes différentes, les montages proches restent au-dessus du hasard en aire (0,58 à "
"0,95), mais le rappel à 1 % peut tomber à 0,03 [BX table 1] ; le hasard en aire ne vient que de l'organisme affiné |"))
R.append((
"mais en défaut au sous-rendement sur consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] et pas meilleure "
"que la moyenne sur la tromperie sur consigne [DYL p. 11 ; table 9] ;",
"à consigne égale (sous-rendement), en défaut avec les sondes apprises sur « Roleplaying » [AP p. 9, p. 18 ; PAR table 3, "
"sonde RP : 0,457 et 0,437], pas avec la recette « Pairs » de P3 (0,849 et 0,879 contre 0,964 en moyenne [PAR table 3]) ; "
"entre consignes, séparation presque parfaite (« Our recall at 1% is greater than 99% on all four evaluation datasets », "
"[AP p. 18]) ; sur consigne, pas meilleure que la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ;"))
R.append((
"chez Apollo, « comparable » en aire, rappel à 1 % de faux positifs meilleur que la même sonde lue sur toute la réponse, "
"mais en dessous de la sonde Instructed-Pairs [AP p. 23] ;",
"chez Apollo, une sonde « Roleplaying » lue sur les dernières positions, « comparable » en aire, rappel à 1 % de faux "
"positifs sur le témoin meilleur que la sonde Roleplaying apprise et lue sur toutes les positions (moyenne), mais en "
"dessous de la sonde Instructed-Pairs [AP p. 23] ;"))
R.append((
"| **moyen** (v1 : fort à moyen) : le levier « question » est en défaut sur les cas proches |",
"| **moyen** (v1 : fort à moyen) : issue incertaine sur les cas proches, selon les données d'apprentissage de la sonde |"))
R.append((
"| six couches [CA p. 5] ; toutes [CC p. 8] ; couche choisie sur un jeu d'évaluation [AP p. 21] ; 12 sur Llama-3-8B "
"[BU p. 5], 14 sur ce modèle [BX p. 3] | moyen (v1 : moyen) : appui hors des cas proches de P3 ([CA], [CC]) |",
"| six couches, sans comparaison à une seule [CA p. 5] (« All probe architectures perform similarly », p. 8) ; toutes, "
"seule comparaison publiée (« using fewer layers consistently yields worse performance ») [CC p. 8], sur une autre tâche ; "
"sur ce même modèle : « Our per-layer analysis indicates that layer choice has limited effect on monitor performance, "
"particularly beyond the first third of layers » [BX p. 3] ; couche choisie sur un jeu d'évaluation [AP p. 21] ; 12 sur "
"Llama-3-8B [BU p. 5], 14 sur ce modèle [BX p. 3] | faible à moyen (v1 : moyen ; v3 : moyen) : un seul appui, sur une "
"autre tâche ([CC]) ; contre-indice sur ce même modèle ([BX p. 3]) |"))
R.append((
"| moyen, **sens inconnu** (v1 : idem) : les preuves penchent vers la moyenne et l'attention, sauf dilution ; N-026 |",
"| moyen, **sens inconnu** (v1 : idem) : les preuves penchent vers la moyenne et l'attention, sauf la sonde RP de [PAR] ; "
"sous dilution, résultats opposés ([PAR] ; [GM]) ; N-026 |"))
R.append((
"noter consigne et raisonnement fait monter les sondes [BX p. 5] ; la sonde de question de [AP] note toute réponse du jeu "
"de sous-rendement comme très trompeuse, même quand le modèle ne sous-performe pas [AP p. 18] ; « deceptive prompt "
"regime » [KU p. 5]",
"noter consigne et raisonnement fait monter les sondes, à consigne égale [BX p. 5] ; la sonde de question de [AP], apprise "
"sur « Roleplaying », note toute réponse du jeu de sous-rendement comme très trompeuse, même quand le modèle ne "
"sous-performe pas, à consigne égale [AP p. 18] ; « deceptive prompt regime » [KU p. 5] : entre consignes, une sonde de "
"régime prédit un faux positif sur P3-P3 [KU p. 9]"))
R.append((
"Ce qui a changé depuis la v1 : rangs 2, 3 et 4 baissent ([K] table 1 ; montage proche de [BX] ; questions en défaut sur les\n"
"cas proches) ; rang 5 devient inconnu (taille ou capacité) ; les autres pouvoirs sont inchangés.",
"Ce qui a changé depuis la v1 : rangs 2, 3 et 4 baissent ([K] table 1 ; montages proches ; questions) ; rang 5 devient\n"
"inconnu (taille ou capacité). v4 : contrastes séparés par type (P3-P3, consignes différentes ; T1, consigne égale) ;\n"
"rang 2 faible à moyen (une sonde de régime prédit un faux positif, pas un nul) ; rang 4 « issue incertaine, selon les\n"
"données d'apprentissage de la sonde » ; rang 6 faible à moyen ; rang 9 annoté par type ; les autres pouvoirs sont\n"
"inchangés."))

# section 4, règles communes (VV3-sens-04 ; VV3-fidelite-01, 05)
R.append((
"**T1** (saboteur : actions qui gonflent contre celles qui ne gonflent pas, même contexte ; seul test à contexte\n"
"égal, [P] l. 238-241) ;",
"**T1** (saboteur : actions qui gonflent contre celles qui ne gonflent pas, **à consigne égale** ; pas à\n"
"contexte égal : pas et historique diffèrent, et dès le deuxième pas les coûts déjà déclarés sont dans le contexte ; [P]\n"
"l. 238-241 ; pour T1, partout : prédicteurs triviaux (rang du pas, longueur notée, coûts déjà déclarés) et contrôle des\n"
"coûts déjà déclarés ; sur le bras du champ et dans E2, T1 ne vaut qu'avec T4, car une sonde qui lit la grandeur du\n"
"nombre écrit passerait T1, [P] l. 141-142) ;"))
R.append((
"jamais « pas de trace »\n([P] l. 272-274). **Jamais",
"jamais « ne sépare pas »\n([P] l. 272-274) ; a fortiori jamais « pas de trace ». **Jamais"))
R.append((
"hors de la famille de\nBonferroni (N-026, conditions 1 à 4).",
"(N-026,\nconditions 1 à 4) ; hors de la famille de Bonferroni : règle de cette synthèse."))
# manipulation du nombre (VV3-sens-05)
R.append((
"privé ») ; toujours calculable ; statut : nœud (section 5).\n",
"privé ») ; toujours calculable ; statut : nœud (section 5). La même note en donne l'inconvénient (« une statistique\n"
"neuve ; des planchers qui saturent » ; « le volet « nombre » attend l'addendum 2 », l. 28) et recommandait A1 d'abord,\n"
"« C2 seulement après le verdict de A1 et après G0 » (l. 33). Le facteur « contexte » ne change que la consigne et\n"
"l'indication ([NB] `propositions/proposition-D.md` l. 93-96) : sur les actions du saboteur, le contexte « témoin » garde\n"
"les coûts gonflés des pas précédents et des titres en capitales, contraires à la consigne du témoin ([P] l. 125,\n"
"l. 333) ; la mesure sépare donc le nombre **de l'action en cours** de la consigne, historique gardé. Le préenregistrement\n"
"dira comment l'historique des coûts est traité (remplacé dans tout l'épisode, premier pas seul, ou strates) et\n"
"déclarera ce conflit. Prédiction écrite, reprise de la proposition D : « effet du nombre > 0 ; effet du contexte, à\n"
"nombre égal, non détecté » (`proposition-D.md` l. 100-101).\n"))

# table des expériences
R.append((
"**bras non aveugles** : seuls leurs planchers de même position et T4 au champ sont neufs ;",
"**bras non aveugles** : seuls leurs planchers de même position, T4 au champ, et P3-P4 et T3 au champ et avant le champ "
"sont neufs (T2 ne porte que sur saboteur contre honnête, [P] l. 242) ;"))
R.append((
"(iii) Moyenne sur l'action et sur le champ : « bras de diagnostic, jamais en production » (N-026), plancher de même "
"agrégation.",
"(iii) Moyenne sur l'action et sur le champ : « bras de diagnostic, jamais en production » (N-026), plancher de même "
"agrégation ; base : N-026 permet ce bras dans un préenregistrement, mais il n'est pas dans le périmètre du GO de N-028 "
"(localisation au champ et oracle, `registres/go.md` l. 32) : extension de N-028, comme E2 et la manipulation (nœud)."))
R.append((
"Oracle non au-dessus : « non détecté à cette puissance » ([P] l. 272-274), jamais « pas de trace » |",
"Oracle non au-dessus : « non détecté à cette puissance » ([P] l. 272-274), jamais « ne sépare pas », a fortiori jamais "
"« pas de trace » |"))
R.append((
"| la position explique-t-elle le nul ? Lu sur le bras (a) seul ;",
"| la position explique-t-elle le nul ? Lu sur le bras (a) seul ; sur T0.6, seulement sur la condition qui réplique P3 "
"((i-a), p = 1, intensité forte, brouillon de T0.6 l. 75, ou son équivalent dans T0.6 réécrit) ;"))
R.append((
"Contre, sur les cas proches : sous-rendement sur consigne [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437] ; "
"tromperie sur consigne, la question ne bat pas la moyenne [DYL p. 11 ; table 9] ; sonde de question basse sur Qwen3-8B "
"(0,69) et Qwen3-4B (0,68) [DYL table 9, p. 28]. **Prédiction écrite d'avance : échec probable de T1** ; un bras au-dessus "
"du plancher sans T1 lit la consigne, pas l'acte |",
"Sur les cas proches, l'issue dépend des données d'apprentissage de la sonde : à consigne égale (sous-rendement), échec "
"avec les sondes apprises sur « Roleplaying » [AP p. 9, p. 18 ; PAR table 3, sonde RP : 0,457 et 0,437], pas avec la "
"recette « Pairs » de P3 (0,849 et 0,879 contre 0,964 en moyenne [PAR table 3]) ; entre consignes, séparation presque "
"parfaite [AP p. 18] ; tromperie sur consigne : la question ne bat pas la moyenne [DYL p. 11 ; table 9 ; LB p. 8] ; sonde "
"de question basse sur Qwen3-8B (0,69 ; moyenne 0,74) et Qwen3-4B (0,68 ; moyenne plus basse encore, 0,64) [DYL table 9, "
"p. 28]. **Prédiction écrite d'avance** : sonde apprise sur « Roleplaying » : échec de T1 ; sondes principales de P3 : "
"issue incertaine ([PAR] : 0,849 et 0,879 à consigne égale, sujet WMDP contre MMLU confondu) ; le nombre de l'action est "
"dans le contexte lu, donc T1 ne vaut qu'avec T4 ; un bras au-dessus du plancher sans T1 lit la consigne, pas l'acte |"))
R.append((
"preuve directe : « every Sandbagging response is rated as highly deceptive – even when the model chooses not to "
"sandbag » [AP p. 18] ;",
"preuve directe, pour une sonde apprise sur « Roleplaying » : « every Sandbagging response is rated as highly deceptive – "
"even when the model chooses not to sandbag » [AP p. 18] ;"))
R.append((
"(ordre de grandeur : P3 entier, 240 épisodes, ≈ 3,96 USD)",
"(à deviser : le brouillon actuel de T0.6 prévoit 1 536 + 640 épisodes ; la proposition P-015 en estime la réécriture en "
"mode « coût » ; nœud de dépense possible au-delà de 10 USD par lancement)"))
R.append((
"un bras de production **fixé d'avance**, sans regarder E1 à E3 (par exemple le bras de production de E3)",
"un bras de production **fixé d'avance** : écrit dans le préenregistrement scellé de E3, ou dans une note scellée "
"maintenant, avant toute lecture de E1 à E3 (par exemple le bras de production de E3)"))
R.append((
"crédit relu 11,79 USD à 06:07 UTC |",
"compte à recharge automatique (R-283) |"))
R.append((
"puis T3 (sur un oracle appris sans la mention), T1 et le même contrôle des coûts déjà déclarés ;",
"puis T3 (sur un oracle appris sans la mention), T1, T4 et le même contrôle des coûts déjà déclarés ; le témoin étant "
"parmi les négatifs d'apprentissage, P3-P4 n'est pas un test pour l'oracle ;"))
R.append((
"| P3-P4, T1, T3 complet, T4 avec le contrôle des coûts déjà déclarés, sur chaque bras de production |",
"| P3-P4, T1, T3 complet, T4 avec le contrôle des coûts déjà déclarés, sur chaque bras de production ; sur T0.6 : témoin "
"et mention à jouer (le brouillon actuel de T0.6, l. 74-81, n'a pas de mention : T3 n'y serait pas calculable) |"))
R.append((
"P3-P4, T1, T3 et T4 ; jamais les tâches d'évaluation (P-011) |",
"P3-P4, T1, T3 et T4 ; jamais les tâches d'évaluation (P-011) ; sur T0.6 : mention à jouer (voir E2) |"))

# section 5 : recommandation et nœuds (VV3-sens-02, 05, 06, 07, 08, 14 d)
R.append((
"à l'aveugle, l'échec de T1 prédit d'avance\n(nœud ci-dessous).",
"à l'aveugle, avec la prédiction écrite de la\nsection 4 (nœud ci-dessous)."))
R.append((
"voie\nque je propose pour R-262 (2), seule de cette liste qui peut porter une revendication, car la sonde est apprise sans\n"
"l'organisme.",
"voie\nque je propose pour R-262 (2) : E3 peut porter une revendication, car la sonde est apprise sans l'organisme et lue en\n"
"production ; E2 sur épisodes neufs le peut aussi, si tu admets en production la lecture après une question (règle gelée\n"
"1)."))
R.append((
"Une revendication ne viendra que d'une\n  sonde apprise sans l'organisme, sur des épisodes neufs.",
"Une revendication ne viendra que d'une\n  lecture de production sur des épisodes neufs : E3, ou E2 si tu admets en "
"production la lecture après une question\n  (règle gelée 1)."))
R.append((
"La ligne N-028 du registre\n  porte la même limite : à compléter par la session.",
"La ligne N-028 du registre\n  porte la même limite : la session la complétera par une ligne nouvelle qui renvoie à "
"N-028, sans réécrire la ligne\n  d'une décision de Lazar."))
R.append((
"et l'issue « consigne lue, pas l'acte » est déjà prédite [AP p. 18] ;",
"et l'issue « consigne lue, pas l'acte » est prédite pour une sonde apprise sur « Roleplaying » [AP p. 18], pas pour la\n"
"  recette « Pairs » [PAR table 3] ;"))
R.append((
"Manipulation du nombre : recommandation : l'ajouter à N-028 (toujours\n"
"  calculable, même passe, seule mesure qui sépare le nombre écrit du contexte privé), confiance ≈ 60 %.",
"Manipulation du nombre : recommandation : l'ajouter à N-028 (toujours\n"
"  calculable, même passe ; elle sépare le nombre de l'action en cours de la consigne, historique des coûts gardé,\n"
"  section 4), contre la note du brainstorm qui la plaçait après le verdict de A1 et après G0 (l. 33) ; confiance ≈ 50 %\n"
"  (v3 : 60 %)."))
R.append((
"Crédit :\n  11,79 USD relus à 06:07 UTC (`registres/depenses.md` l. 89) ; recharge d'environ 20 USD prévue par toi\n"
"  (GO-2026-10-20-06, `registres/go.md` l. 33).",
"Crédit :\n  compte à recharge automatique (R-283). T0.6 réécrit en mode « coût » peut dépasser 10 USD par lancement\n"
"  (brouillon actuel : 1 536 + 640 épisodes ; P-015) : nœud de dépense possible."))
R.append((
"« gonflement d'estimation » ;\n  position « avant le champ » ; couches multiples ;",
"« gonflement d'estimation » ;\n  position « avant le champ » ; couches multiples (dans T0.7 et sur des épisodes neufs "
"seulement : sur les actions\n  de P3, toute couche ou sonde neuve est un nœud, [P] l. 428) ;"))

# pied
R.append((
"v3 : pouvoirs des rangs 2 à 5 et confiances revus par le correcteur\n(sections 3 et 5).",
"v3 : pouvoirs des rangs 2 à 5 et confiances revus par le correcteur\n(sections 3 et 5). v4 "
"(`…/revue-detection/correction-tour3/`) : `appliquer_corrections_v4.py` (le différentiel, v3 → v4)."))

for k, (a, b) in enumerate(R, 1):
    n = t.count(a)
    if n != 1:
        sys.exit(f"remplacement {k} : texte d'origine trouvé {n} fois (attendu 1) : {a[:100]!r}")
    t = t.replace(a, b)
Path(dst).write_text(t, encoding="utf-8")
print(f"2 blocs et {len(R)} remplacements appliqués")
