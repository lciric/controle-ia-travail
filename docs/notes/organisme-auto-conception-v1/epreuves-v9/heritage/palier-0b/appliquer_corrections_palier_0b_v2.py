"""Produit la version 2 du preenregistrement du palier 0b par remplacements exacts
sur la version 1 (lue dans le depot, jamais modifiee). Chaque chaine remplacee doit
figurer exactement une fois dans la version 1 ; sinon le programme s arrete.
Usage : python3 -I -B appliquer_corrections_v2.py V1 V2 HEURE_DE_FIN QUEUE
(QUEUE : reserves 12 a 16 et annexe E, ajoutees a la fin)."""
import hashlib, sys

V1, V2, FIN = sys.argv[1], sys.argv[2], sys.argv[3]
texte = open(V1, encoding="utf-8").read()
assert hashlib.sha256(texte.encode("utf-8")).hexdigest() == \
    "a7189bbb598d0dbc4bc6d0390381d45d5ec652a4cf78b9e077898f690449db74"
origine = texte
R = []


def r(ancien, neuf):
    R.append((ancien, neuf))


# ---------------------------------------------------------------- en-tete
r("aucun appel de modèle — v1\n", "aucun appel de modèle — v2\n")
r("""Pièce décisive (classe A), **brouillon à contre-lire** : rien ici n'est scellé, aucun tirage décisif n'a été fait, aucun code d'analyse n'existe encore.""",
  """Pièce décisive (classe A), **brouillon corrigé, à faire vérifier par le même contre-lecteur** : rien ici n'est scellé, aucun tirage décisif n'a été fait, aucun code d'analyse n'existe encore. **Version 2** : elle remplace la version 1 (`palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v1.md`, `a7189bbb598d0dbc4bc6d0390381d45d5ec652a4cf78b9e077898f690449db74`), qui reste intacte (règle R12) ; elle se vérifie sur son différentiel (annexe E).""")
r("""- Date (UTC) : 2026-11-19, écrit de 15:16Z à 15:55Z environ (`date -u`), sur processeur seul""",
  """- Date (UTC) : 2026-11-19 ; version 1 écrite de 15:16Z à 15:55Z environ, version 2 de 16:39Z à """ + FIN + """ environ (`date -u`), sur processeur seul""")
r("""- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/mandat-redacteur-preenregistrement-palier-0b-v1.md`""",
  """- Mandat de la version 2 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/mandat-redacteur-preenregistrement-palier-0b-v2-v1.md` (`311a2272c3bc5fc56c4868e3f0a02f4790f289912a6bd75227c53884d4ac7f8e`, branche `lot/compte-organisme-v1`, commit `68f3e5fc906f3cf640d3fb10e0682106debba774`). Les lignes d'accord y sont relues sur `main` au commit `0bf0a3b0b2e27aab4bc7072096e66ea8c66337a1` (`registres/go.md`, `a23e482cf904c3fad4b04ce11cbd9dc6cafa8b237fab1b78da467f49433ec338`), où s'ajoute `GO-2026-11-19-77` : trois décisions sur ce palier, option (a) chaque fois — lecteur témoin des tests de mort joué en réel au seul palier 1, puis décision ; une tenue « établie » s'écrit d'avance « servir un registre tenu, forme comprise » ; engagements à forme imposée aux paliers payants ; aucune dépense engagée par ce mot. S'y ajoute le mot de la mère (vers 16:33Z, rapporté par le mandat) sur deux ajouts sans critère.
- Mandat de la version 1 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/mandat-redacteur-preenregistrement-palier-0b-v1.md`""")
r("""lignes R-3858, R-3868, R-3882, R-3904, R-3907 ;""",
  """lignes R-3858, R-3868, R-3882, R-3904, R-3907 ; ligne R-3925, lue au commit `0bf0a3b0` (`657ec502d7915a82cd074cefbbfe08329b0fb45066d3cc072224168a323f76bb`) ;""")
r("""rejouée deux fois à l'octet ; dit ici « le calcul des ordres de grandeur ».""",
  """rejouée deux fois à l'octet ; dit ici « le calcul des ordres de grandeur » ;
  - **calcul de la version 2**, sans tirage (même dossier de travail, à verser avec ce texte) : `calcul_ordres_de_grandeur_palier_0b_v2.py` (`470f3385aa2c21b10c3e50eab769599c0963a4d1799a45ac23074151f5e7dc13`) et sa sortie `calcul-ordres-de-grandeur-palier-0b-v2.json` (`b97ed1f15361179252cdb4cf3a8fc546a53aea3b04d2c38b53adfbf002db9083`), rejouée deux fois à l'octet ; elle redonne à l'identique tous les champs de la version 1 et ajoute la règle corrigée de C1 et de C4, le seuil chiffré de « beaucoup plus de sources » et deux comptes de paires ; dit ici « le calcul de la version 2 » ;
  - contre-lecture de la version 1 de ce texte : `palier-0b/contre-lecture-preenregistrement-palier-0b-v1-v1.md` (`127aa59ffcd229de8faed7be9d7347dc653f813478d63439d7c6d1dbf88a8b6e`) et ses vérifications à la main (`416a907bacf382dbbadb183e7b115f8c82224124c5dc488ae6711b054c4704c5`) ; dit ici « la contre-lecture ».""")

# ---------------------------------------------------------------- hypothese
r("""son sort au-delà reste une question pour Lazar (rapport du rédacteur, décision 1) |""",
  """au-delà, voir la table suivante (`GO-2026-11-19-77`, décision 1) |""")
r("""**Écart déclaré à la lettre de N-058.** N-058 définit""",
  """**Trois décisions de Lazar sur ce palier, portées telles quelles** (ligne `GO-2026-11-19-77`, option (a) chaque fois ; aucune dépense n'est engagée par ce mot ni par ce texte) :

| décision | ce que ce texte en fait |
|---|---|
| 1 — lecteur témoin des tests de mort joué en réel au seul palier 1, puis décision | à cet étage il reste une doublure écrite par programme, sans poids sur aucun verdict (B4) ; le lecteur réel du palier 1 se chiffre au devis de ce palier et part sur sa ligne d'accord ; rien n'est dit ici des paliers suivants |
| 2 — une tenue « établie » s'écrit d'avance « servir un registre tenu, forme comprise » | la phrase est gelée aux critères de lecture, pour être reprise à l'octet au préenregistrement de l'étage payant ; la famille F et le bras de diagnostic (famille H) mesurent, sans critère, ce que « forme comprise » recouvre sur des proposeurs écrits par programme |
| 3 — engagements à forme imposée aux paliers payants | la forme de cet étage (B4) est donc celle des paliers payants ; ce que cela change pour l'expérimentateur est écrit en B4, sans revenir sur `GO-2026-11-19-75` |

**Écart déclaré à la lettre de N-058.** N-058 définit""")

# ---------------------------------------------------------------- pronostics
r("""| 6 — contrôle de construction | au moins huit dixièmes de l'écart d'héritage du lecteur sont portés par les lois dépendantes ; l'écart sur les lois indépendantes est faiblement négatif (coût de lecture) | une part sous 0,8 |""",
  """| 6 — contrôle de construction | la part vaut un : l'écart sur les lois indépendantes (I) est négatif ou nul (coût de lecture, déplacement de l'effort), et tout l'écart positif est porté par les lois dépendantes ; I, rapporté à part, est faiblement négatif | une part sous 0,8, c'est-à-dire un écart positif sur les lois indépendantes de plus du quart de l'écart sur les lois dépendantes |""")
r("""| 7 — repli sans `resultat` ni `gardee` | signe : le lecteur retrouve **moins** ; rapport de l'écart d'héritage du repli à l'écart servi entre 0,3 et 0,8 (des entrées qui n'ont pas tenu diluent ses compositions) ; la règle « presque autant » ne se déclenche pas |""",
  """| 7 — repli sans `resultat` ni `gardee` | signe : le lecteur retrouve **moins**, à effort d'examen égal (le même nombre K de paires) ; rapport R sous 0,3, de l'ordre de l'inverse du facteur d'enrichissement : les paires vraies sont diluées parmi toutes les paires des entrées de la source (28 paires de lois vraies au plus, sur 39 621 paires si les 282 entrées attendues portent des lois distinctes ; calcul de la version 2, champ `paires`) ; issue « le repli coûte ». **Pronostic changé avec la mécanique** : la version 1, où chaque paire était examinée avec une probabilité, disait de 0,3 à 0,8 |""")
r("""une règle de la version 2 qui coûterait plus que celle de la version 1 |
""",
  """une règle de la version 2 qui coûterait plus que celle de la version 1 |
| ajout, sans critère — puissance du seul contraste de l'héritage (M13, S9) | lu seul au seuil de 0,05, il atteint 0,8 à un nombre n₁ inférieur de zéro à quatre sources au n des deux contrastes ; la condition « beaucoup plus de sources » n'est pas remplie. Appui : par approximation normale, 8,22 sources au seuil de 0,05 contre 9,95 au seuil de 0,025 à la taille de référence (calcul des ordres de grandeur) | un écart d'au moins huit sources et d'au moins la moitié de n₁ : la condition est remplie, et la mère repose le nœud 4 à Lazar |
| ajout, sans critère — bras de diagnostic « registre d'une autre source » (M14, B7 bis) | suiveur à la lettre du plan : le contraste de la tenue (bras 2 moins bras 1) est positif, l'écart du bras 2 au bras « registre tenu par une autre source » est nul à l'intervalle près, et l'écart du bras « registre hérité d'une autre source » au bras 2 ne porte que le coût de lecture ; lecteur réglé pour la tenue : l'écart du bras 2 au bras « registre tenu par une autre source » garde l'effet planté ; lecteur réglé pour l'héritage : l'écart du bras 3 au bras « registre hérité d'une autre source » garde l'effet planté | un bras de diagnostic qui efface l'effet planté d'un lecteur ; ou un suiveur à la lettre qui garde un écart positif face au registre tenu par une autre source |
""")

# ---------------------------------------------------------------- metriques
r("""à réglage du lecteur égal, à la taille de référence, par dose non nulle. Rapportées à côté : la puissance du contraste de l'héritage sous le repli, sur la grille des nombres de sources, et la même chose pour le contraste de la tenue.""",
  """à réglage du lecteur égal (le même nombre K de paires examinées par génération, B7), à la taille de référence, par dose non nulle. Rapportés à côté : la puissance du contraste de l'héritage sous le repli, sur la grille des nombres de sources ; **la part des entrées venues de la source qui sont gardées** ; **le facteur d'enrichissement** — la part des lois vraies de la source parmi les entrées gardées, divisée par cette part parmi toutes les entrées de la source — et le même rapport au grain des paires (part des paires faites de deux lois vraies de la source, parmi les paires des entrées gardées, divisée par cette part parmi les paires de toutes les entrées). Le contraste de la tenue sous le repli est **sans objet par construction** et n'est pas rapporté (B7, « Le repli du point 7 »).""")
r("""et le même rapport pour le lecteur (il dit l'hétérogénéité entre sources que les jumelles ne voient pas).""",
  """et le même rapport pour le lecteur (il dit l'hétérogénéité entre sources que les jumelles ne voient pas). **D'où vient cet écart-type** : les jumelles ne sont jouées qu'à l'étalonnage (B7), jamais dans les tirages décisifs ; l'écart-type entre jumelles qui définit la taille réduite est celui de l'étalonnage, gelé dans le fichier des réglages ; la taille réalisée des tirages décisifs (liste d'arrêt, point 6) est l'écart moyen de ces tirages divisé par cet écart-type gelé.""")
r("""La part vaut D divisé par la somme des valeurs absolues de D et de I, si D est positif ; zéro sinon. Raison de cette forme : le coût de lecture rend I négatif, et un simple rapport D sur (D + I) dépasserait alors un sans rien dire.""",
  """La part vaut D divisé par la somme de D et de la plus grande des deux valeurs : I ou zéro, si D est positif ; zéro sinon. Raison de cette forme : un écart négatif sur les lois indépendantes vient du coût de lecture et du déplacement de l'effort (plan, § 5) et n'est pas un effet de forme ; seul un écart positif sur elles retire de la part. I est rapporté à part, avec son signe et son intervalle.""")
r("""- **M12 — fréquences des classes d'issue par type de tentative**, mesurées sur la couche mécanique (B2, B5) : part de « tient », « ne tient pas », « non exécutable ou indéterminée » pour une tentative appariée à une loi vraie plantée, à une loi fausse plantée, ou à rien. C'est aussi le compte des lois fausses tenues, qui dit si l'épreuve est trop facile (plan, § 3.0).""",
  """- **M12 — fréquences des classes d'issue, par loi et par type**, mesurées sur la couche mécanique (B2, B5) : la part des **lois engagées** qui tiennent, par type — loi vraie plantée, loi fausse plantée, loi non plantée (appariée à rien) —, une loi engagée plusieurs fois sur un même monde comptant une fois, puisque le même engagement sur la même tranche d'épreuve rend le même verdict ; et, par composition examinée et par monde, le taux de faux passage du criblage (B7). Rapportée à côté, au grain de la tentative : la part de « tient », « ne tient pas », « non exécutable ou indéterminée », échecs de l'expérimentateur compris. C'est aussi le compte des lois fausses tenues, qui dit si l'épreuve est trop facile (plan, § 3.0).
- **M13 — puissance du seul contraste de l'héritage, information sans critère** (ajout de la version 2) : sur les tirages de la famille B du lecteur réglé pour l'héritage, la part des tirages où le contraste de l'héritage, **lu seul** au seuil bilatéral de 0,05 (M3, sans la procédure de Holm), est « établi » au sens de M5 (signe et condition des lois fausses) ; à chaque nombre de la grille et, en plus, à 6, 7, 8 et 9 sources, lues comme les premières sources des mêmes tirages emboîtés (six est le plancher technique d'un seul contraste ; plan, § 12, question 4). À côté, sur la famille A : le taux de rejet de ce contraste lu seul. **n₁** est le plus petit de ces nombres où cette puissance est au moins 0,8, à ce nombre et à tous les suivants, à chaque dose non nulle où la taille de référence est atteignable, au taux d'échec de 0,25. Aucun tirage de plus n'est fait pour cette lecture.
- **M14 — écarts du bras de diagnostic « registre d'une autre source », sans critère** (ajout de la version 2 ; B7 bis) : écarts moyens de M1, en lois et en taille réduite, chacun avec son intervalle — bras 3 moins bras 4a (héritage : contenu contre présence) ; bras 4a moins bras 2 ; bras 2 moins bras 4b (tenue : contenu contre présence) ; bras 4b moins bras 1 (présence seule) ; bras 2 moins bras 1 (rappel) — et, à chaque nombre de la grille, la part des tirages où le test M3, lu seul au seuil de 0,05, rejette pour « bras 2 moins bras 1 » et pour « bras 2 moins bras 4b ».""")

# ---------------------------------------------------------------- valeurs gelees, criteres
r("""| tirage de confirmation | 100 000 tirages, graines neuves | **ajouté** (voir C1 et C4) |""",
  """| tirage de confirmation | 100 000 tirages, graines neuves, pour toute case de C1 ou de C4 dont le taux observé dépasse 0,05 (plus de 500 rejets sur 10 000) | **ajouté** (voir C1 et C4) ; **règle corrigée à la version 2** : la case est en échec si le tirage de confirmation compte au moins 5 236 rejets, plus petit compte dont la borne basse de l'intervalle exact bilatéral de niveau 1 − 0,05/72 dépasse 0,05 (calcul de la version 2, champ `regle_corrigee_de_C1_et_de_C4`) |
| plage du réglage K du lecteur | de 0 à 256 paires examinées par génération | **ajoutée à la version 2** (B7) ; valeur du rédacteur, sans appui mesuré ; une cible non atteinte à 256 est « non atteignable » |
| « beaucoup plus de sources » (devis, § 9, nœud 4) | au moins 8 sources de plus **et** au moins une fois et demie | **ajouté à la version 2**, sans critère (S9) |""")
r("""une case **tient** si la borne haute de son intervalle est au plus 0,06 (au plus 553 rejets sur 10 000). Une case qui ne tient pas est **retirée une fois**, à 100 000 tirages de graines neuves ; elle est **en échec** si la borne basse de l'intervalle de ce tirage de confirmation dépasse 0,05.""",
  """une case **tient** si son taux observé est au plus 0,05 (au plus 500 rejets sur 10 000 ; sa borne haute est alors au plus 0,0545). Une case au-dessus est **retirée une fois**, à 100 000 tirages de graines neuves ; elle est **en échec** si la borne basse de l'intervalle binomial exact bilatéral de niveau 1 − 0,05/72 de ce tirage de confirmation dépasse 0,05, 72 étant le nombre de cases que compte le critère (douze nombres de sources, deux doses, trois taux d'échec) : soit au moins 5 236 rejets sur 100 000.""")
r("""La borne haute à 0,06 est gardée telle quelle ; le tirage de confirmation remplace la première clause par une preuve que le niveau dépasse 0,05 |""",
  """La clause du plan est gardée comme déclencheur du tirage de confirmation, et l'échec exige une preuve, corrigée pour le nombre de cases, que le niveau dépasse 0,05 ; la borne haute à 0,06 est tenue d'office. Ce que la règle voit (calcul de la version 2) : une case de niveau vrai 0,053 est en échec avec une probabilité de 0,74, une case de niveau vrai 0,055 avec 0,99 ; une case de niveau vrai 0,05 avec 0,0002, soit moins de 0,015 sur les 72 cases |""")
r("""| déclenchée au moins 8 fois sur 10 | gardé ; « atteint à un nombre » se lit comme pour C2 |""",
  """| déclenchée au moins 8 fois sur 10, au taux d'échec de 0,25 ; les taux 0 et 0,5 sont rapportés | gardé ; « atteint à un nombre » se lit comme pour C2 |""")
r("""| même règle que C1 : borne haute au plus 0,06, sinon tirage de confirmation, échec si sa borne basse dépasse 0,05 |""",
  """| même règle que C1, aux trois taux d'échec de la famille C ; le nombre de cases de C4 est aussi 72 (douze nombres de sources, deux sourds, trois taux d'échec) |""")
r("""| part M10 au moins 0,8, à chaque nombre de la grille et à chaque dose non nulle où la taille de référence est atteignable |""",
  """| part M10 au moins 0,8, à chaque nombre de la grille et à chaque dose non nulle où la taille de référence est atteignable, au taux d'échec de 0,25 |""")

# ---------------------------------------------------------------- autres seuils
r("""Cette règle ne décide que d'une revue ; elle ne change ni l'issue de l'étage ni ce qui est servi.""",
  """**R est une propriété du lecteur écrit par programme et du banc**, mesurée à effort d'examen égal (le même K au repli) ; sont rapportés à côté la part des entrées de la source qui sont gardées et le facteur d'enrichissement (M7) ; la proposition de revue faite à Lazar, s'il y en a une, porte cette phrase. Cette règle ne décide que d'une revue ; elle ne change ni l'issue de l'étage ni ce qui est servi.""")
r("""sur la couche mécanique, la part de « tient » parmi les tentatives exécutées appariées à une loi vraie est au moins 0,5, et parmi celles appariées à une loi fausse au plus 0,5""",
  """sur la couche mécanique, la part des lois vraies plantées engagées qui tiennent (M12, par loi) est au moins 0,5, et celle des lois fausses plantées engagées au plus 0,5""")
r("""Un classifieur simple sur la présentation seule ne sépare ni les lois dépendantes des indépendantes, ni les mondes par dose : exactitude équilibrée au plus 0,55 en validation croisée.""",
  """Un classifieur simple sur la présentation seule ne sépare ni les lois vraies des fausses, ni les lois dépendantes des indépendantes, ni les mondes par dose : exactitude équilibrée au plus 0,55 en validation croisée. Pour les lois vraies et fausses, la présentation est la forme écrite des lois de la clé (les lois fausses ne figurent pas dans les données servies) ; l'audit est gardé parce que le plan (§ 5) le nomme et qu'une loi fausse reconnaissable à sa seule forme fausserait la condition des lois fausses. Pour le bras de diagnostic (B7 bis) : toute loi d'un monde cible est aussi séparée d'au moins 0,25 nat de toute loi vraie de la source étrangère et de toute composition de deux d'entre elles.""")
r("""et la plus petite force de la grille où il atteint 0,8 au nombre m retenu.
""",
  """et la plus petite force de la grille où il atteint 0,8 au nombre m retenu.
- **S9 — « beaucoup plus de sources », chiffré avant tout tirage ; ne décide de rien dans l'étage** (ajout de la version 2). Le devis (§ 9, nœud 4) écrit ce qui ferait changer sa recommandation de deux contrastes décisifs : « une table de puissance du palier 0b où deux contrastes demandent beaucoup plus de sources qu'un seul à la taille de référence ». Soient **n₁** le nombre du seul contraste de l'héritage (M13) et **n₂** le n de l'étage, celui des deux contrastes sous la procédure de Holm (critères de lecture). **La condition est remplie si n₂ − n₁ est d'au moins 8 sources et si n₂ vaut au moins une fois et demie n₁.** Si C2 n'est atteint à aucun nombre jusqu'à 48, elle est remplie quand n₁ est au plus 32, et « indéterminée » sinon ; si n₁ n'existe pas jusqu'à 48, elle est « sans objet ». Raisons des deux chiffres. *Huit sources* : le devis a déjà pesé un écart de six sources (douze contre six, soit 5 280 USD à 880 USD la source à cinq espèces ; devis, § 7 et § 9) et a recommandé deux contrastes quand même ; « beaucoup plus » doit dépasser ce qui a été pesé ; huit sources font 7 040 USD. *Une fois et demie* : le prix attendu de la procédure de Holm, par approximation normale, est de 1,73 source et d'un rapport de 1,21 à la taille de référence (9,95 contre 8,22) ; un rapport de 1,5 ne s'explique plus par elle seule. Table des couples (n₁, plus petit n₂ qui remplit la condition) : calcul de la version 2, champ `seuil_de_beaucoup_plus_de_sources` ; par exemple 14 pour n₁ égal à 6, 20 pour 10 ou 12, 24 pour 14 ou 16. **Suite** : si la condition est remplie, la mère repose le nœud 4 à Lazar, table à l'appui ; sinon, ou si elle est « indéterminée » ou « sans objet », rien ne change. Cette lecture ne touche ni l'issue de l'étage, ni n, ni la décision du nœud 4 (`GO-2026-11-19-76`, point 4), qui reste : deux contrastes décisifs.
""")

# ---------------------------------------------------------------- B2
r("""sa classe d'issue est tirée selon les fréquences M12 **mesurées sur la couche mécanique, toutes tentatives réunies**, puis gelées par programme dans un fichier scellé avant tout tirage décisif.""",
  """sa classe d'issue (« tient » ou « ne tient pas ») est tirée **une fois par loi engagée et par monde** — loi plantée vraie, loi plantée fausse, ou loi non plantée — selon les fréquences M12 mesurées **par loi** sur la couche mécanique, puis reprise pour toute tentative qui engage la même loi sur le même monde ; seul l'échec de l'expérimentateur se tire par tentative (B5). Raison : sur la couche mécanique, un même engagement sur la même tranche d'épreuve rend le même verdict. Ces fréquences sont gelées par programme dans un fichier scellé avant tout tirage décisif.""")

# ---------------------------------------------------------------- B4
r("""La forme admise à l'étage payant se gèle à son préenregistrement (rapport du rédacteur, décision 3).""",
  """**C'est aussi la forme des paliers payants** (`GO-2026-11-19-77`, décision 3, option (a)) ; chaque préenregistrement payant la reprend.""")
r("""**et la description bornée**, chacun entre balises de donnée. Les autres champs que l'étage exige d'une fiche (nom, hypothèse, prédiction chiffrée, signe et métrique de la « loi prédictive ») sont des **textes neutres écrits par l'orchestrateur**, comme le fait le tour fermé ; ils ne viennent jamais du registre.""",
  """**et la description bornée**, chacun entre balises de donnée. **La description bornée est portée par le champ `enonce` de la fiche**, entre balises de donnée, à la place de l'hypothèse neutre que le tour fermé y écrit (nom de champ pris au rapport du palier 0a, § 3.1 et § 3.2 ; le développeur le confirme à la lecture du code et s'arrête s'il trouve autre chose, réserve 1). Les autres champs que l'étage exige d'une fiche (nom, prédiction chiffrée, signe et métrique de la « loi prédictive ») sont des **textes neutres écrits par l'orchestrateur**, comme le fait le tour fermé ; ils ne viennent jamais du registre. **La part de données que l'étage lui donne est gelée de même** : l'index et les fichiers de la tranche d'épreuve du monde en cours, la consigne de l'étage (quotas, règles, liste d'arrêt) et l'historique de ses propres tours ; rien d'autre.""")
r("""le sens étant lu par l'étage dans une phrase ; tenue du budget par bras.""",
  """le sens étant lu par l'étage dans une phrase ; tenue du budget par bras ; le classement que l'étage exige est écrit par l'enveloppe dans l'ordre du scellement, toutes les lignes éligibles, sans juge ni rang tiré d'un juge.""")
r("""- **Le lecteur témoin** de l'étage, qui ne pèse sur aucun verdict, est ici une doublure écrite par programme, comme au palier 0a.""",
  """- **Le lecteur témoin** de l'étage, qui ne pèse sur aucun verdict, est ici une doublure écrite par programme, comme au palier 0a. Il est joué en réel au seul palier 1, puis Lazar décide (`GO-2026-11-19-77`, décision 1) ; ce texte n'engage pour lui aucune dépense.
- **Ce que la forme imposée change pour l'expérimentateur** (`GO-2026-11-19-77`, décision 3 ; contre-lecture, § 9, point 3). Avec la forme imposée, la loi est dans le texte du test, lui-même dans l'engagement scellé : la raison que le plan donnait pour servir la description bornée à l'expérimentateur (plan, § 3.0 : « sans la description, l'expérimentateur ne sait pas ce que la loi affirme ») tombe, et servir l'engagement seul fermerait ce canal du proposeur vers l'expérimentateur. Et l'expérimentateur modèle, gardé par `GO-2026-11-19-75`, n'a plus qu'un script fixe à lancer : relire la loi, appeler l'évaluateur (rapport du palier 0a, § 4). **Ce que cela change ici** : (i) rien dans le dessin — l'expérimentateur reste une session de modèle, nommée, et `GO-2026-11-19-75` n'est pas rouvert ; (ii) la liste gelée ci-dessus garde la description à cet étage, parce que le plan la propose et que la réduire touche ce que reçoit un rôle gardé par Lazar ; **la garde 11 est éprouvée sur les deux listes** (avec la description ; l'engagement seul, `enonce` redevenant un texte neutre), pour que la réponse de Lazar ne demande aucun code neuf ; (iii) le taux d'échec simulé de 0,25 (B5) est sans doute prudent pour un script fixe ; il n'est pas changé, les bords 0 et 0,5 sont joués, et le palier 1 le mesure ; (iv) la question « l'engagement seul aux paliers payants ? » est posée à Lazar pour le préenregistrement du palier 1 (rapport du rédacteur de la version 2, décision B).""")

# ---------------------------------------------------------------- B6, B7
r("""(trois générations de 94 tentatives) sur 55 appels""",
  """(trois générations de 94 tentatives ; cette taille du « registre plein » est une identification du rédacteur) sur 55 appels""")
r("""`prediction` : un vecteur fixe de probabilités en dixièmes, scellé avant l'épreuve).""",
  """`prediction` : un vecteur fixe de probabilités en dixièmes, scellé avant l'épreuve). Les longueurs bornées des champs (plan, § 1) sont sans objet à cet étage : tous les textes sont fixes.""")
r("""il forme les paires de ces lois, examine chaque paire avec la probabilité λ, compose la loi""",
  """il forme les paires de ces lois et en examine, à chaque génération, un nombre fixe K, tirées sans remise dans l'ordre d'une permutation semée (toutes si elles sont moins de K), compose la loi""")
r("""les compositions qui passent le criblage. Sans entrée venue de la source (bras 1 et 2), il ne fait que la recherche de base | λ, de 0 à 1 |""",
  """les compositions qui passent le criblage. Si plus de compositions passent que la moitié de ses tentatives, celles qu'il engage sont prises dans l'ordre d'une permutation semée ; une composition qui passe le criblage sur plusieurs domaines est engagée sur celui où elle s'ajuste le mieux, le domaine de plus petit rang en cas d'égalité. Sans entrée venue de la source (bras 1 et 2), il ne fait que la recherche de base | K, de 0 à 256 ; un K non entier est arrondi à l'entier inférieur ou supérieur par un tirage semé, de moyenne K |""")
r("""564 est deux fois 282, la taille attendue du registre du bras 3 à la génération finale |""",
  """564 est deux fois 282, la taille attendue du registre du bras 3 à la génération finale. Cet écart ne change ni hypothèse ni revendication ; il est porté à Lazar pour information (contre-lecture, § 5, point (c)) |""")
r("""et le taux de rejet du **contraste de la tenue** qu'il produit à la dose 0,25 (réserve 3) |""",
  """et le taux de rejet du **contraste de la tenue** qu'il produit à la dose 0,25 (réserve 3) ; il est aussi le proposeur contre lequel se joue le bras de diagnostic (B7 bis, famille H) |""")
r("""sur 200 000 sources d'étalonnage, jusqu'à ce que""",
  """sur 200 000 sources d'étalonnage, chaque continuation y étant jouée avec sa jumelle (M9), jusqu'à ce que""")
r("""celle du contraste de l'héritage pour λ, φ et γ (à dose nulle pour φ et γ)""",
  """celle du contraste de l'héritage pour K, φ et γ (à dose nulle pour φ et γ)""")
r("""**Le repli du point 7.** Même lecteur, même λ, registre servi sans `resultat` ni `gardee` : le lecteur forme alors ses paires sur **toutes** les entrées venues de la source. Pour le réglage de la tenue, la condition devient « au moins une entrée de sa propre continuation ».""",
  """**Le repli du point 7.** Même lecteur, même K, registre servi sans `resultat` ni `gardee` : le lecteur forme alors ses paires sur **toutes** les entrées venues de la source, et en examine le même nombre K par génération. **Le repli garde le même K : il mesure ce que perd le lecteur quand l'information « gardée » manque, à effort d'examen égal.** Raison (contre-lecture, correction 2) : si chaque paire était examinée avec une probabilité, le lecteur du repli examinerait sans frais bien plus de paires (39 621 pour 282 entrées à lois distinctes, contre 28 paires de lois vraies au plus), et R dépendrait du seul taux de faux passage du criblage. Le lecteur réglé pour la tenue n'est pas joué au repli : sa condition (« au moins une entrée de sa propre continuation ») y serait presque toujours vraie et son écart planté égal ; cette ligne est sans objet par construction.""")
r("""ce taux de faux passage est mesuré sur la couche mécanique avec M12 et injecté de même dans la couche statistique.""",
  """ce taux de faux passage est mesuré sur la couche mécanique avec M12, **par composition et par monde** (une composition examinée plusieurs fois sur un même monde rend le même criblage), et injecté de même dans la couche statistique.""")

# ---------------------------------------------------------------- B7 bis, B8
r("""### B8 — Les cases, les tirages, les graines""",
  """### B7 bis — Le bras de diagnostic « registre d'une autre source » (ajout de la version 2, sans critère)

Plan, § 9 : « registre d'une autre source, de même forme et d'un monde disjoint, qui sépare le contenu de la présence » ; les bras de diagnostic s'y jouent d'abord sur processeur, à 0 USD. Accordé par la mère pour cet étage et **rapporté sans critère** : il n'entre dans aucune issue, aucun seuil ne le lit, et il ne retire rien aux trois bras.

- **La source étrangère** d'une source est la source suivante du même tirage, dans l'ordre fixe (la première pour la dernière), à la même dose ; ses mondes sont tirés sans rapport avec ceux de la source servie, et l'audit du générateur vérifie la marge (section « Seuil »).
- **Deux lectures du bras, jouées toutes deux, parce que le plan ne dit pas quel registre est remplacé.** **Bras 4a — registre hérité d'une autre source, puis tenu** : le bras 3, où le registre reçu au départ est celui de la course de la source étrangère ; c'est la lecture la plus proche de la lettre du plan. **Bras 4b — registre tenu par une autre source, servi à la place du sien** : le bras 2, où ce qui est servi à chaque génération est le registre que tient, à la même génération, le bras 2 de la source étrangère ; la continuation écrit toujours son propre registre, scellé et jamais servi, comme le bras 1 écrit ses champs. **Le bras 4b est un ajout du rédacteur** : c'est lui, et non le bras 4a, qui peut séparer le contenu de la présence **pour la tenue**, puisque dans le bras 4a comme dans le bras 2 la continuation lit son propre registre tenu.
- **Mêmes règles que les bras du critère** : mêmes mondes, même budget, même taux d'échec, lecture payée sur le nombre d'entrées servies, génération finale sans écriture, test de mort du monde final hors budget. Le registre étranger est une copie scellée, déposée par l'orchestrateur dans le dossier du bras ; son empreinte est celle du registre de la source étrangère (B9, garde 27). La garde d'équivalence S8 ne porte que sur les trois bras du critère ; les bras 4a et 4b se jouent sur la couche statistique, et sur la couche mécanique pour la seule garde 27.
- **Contre qui** : le suiveur de forme à la lettre du plan — c'est la question : un effet dû à la seule présence d'un registre, qui gonfle le contraste de la tenue, est-il vu ? — ; et, pour que la réponse se lise, les deux lecteurs à la taille de référence (un bras de diagnostic qui effacerait un effet planté de contenu ne protégerait rien) et le sourd qui paie (le coût seul).
- **Ce qui est lu** : M14. **Ce que cela dira, sans décider** : si, pour le suiveur à la lettre, le contraste de la tenue est positif alors que l'écart du bras 2 au bras 4b est nul, et si, pour le lecteur réglé pour la tenue, cet écart garde l'effet planté, alors un registre tenu par une autre source sépare la présence du contenu pour la tenue ; le compte rendu le dira à Lazar avant tout devis d'un bras de diagnostic payant. La phrase « servir un registre tenu, forme comprise » (`GO-2026-11-19-77`, décision 2) n'en est pas changée.
- **Borne** : l'effet de tenue du lecteur est planté par paramètre (réserve 3) ; que le bras 4b le garde est vrai par construction de sa condition (« une entrée de sa propre continuation ») et n'apprend rien d'un vrai proposeur. Le seul fait mesuré est du côté du suiveur et du coût.

### B8 — Les cases, les tirages, les graines""")
r("""| C1 ; M11 ; rapport d'écarts-types de M9 |""",
  """| C1 ; M11 ; rapport d'écarts-types de M9 ; taux de rejet du contraste de l'héritage lu seul (M13, sans critère) |""")
r("""| C2 ; C5 ; M9 ; M11 |""",
  """| C2 ; C5 ; M9 ; M11 ; M13 (sans critère) ; part des tirages où l'autre contraste passe la première marche de Holm |""")
r("""| D — repli | lecteur, les deux réglages, registre servi sans `resultat` ni `gardee` | 1, 2, 3 | 0,25 ; 0,5 | 0,25 | 1 | S7 (R sur 200 000 sources par dose) ; puissance sous le repli |""",
  """| D — repli | lecteur réglé pour l'héritage, registre servi sans `resultat` ni `gardee`, même K | 1, 2, 3 | 0,25 ; 0,5 | 0,25 | 1 | S7 (R, part des entrées gardées et facteur d'enrichissement, sur 200 000 sources par dose) ; puissance du contraste de l'héritage sous le repli |""")
r("""| M1 par bras ; nombre de lois appariées par une copie (zéro attendu ; garde de C6) |
""",
  """| M1 par bras ; nombre de lois appariées par une copie (zéro attendu ; garde de C6) |
| H — bras de diagnostic « registre d'une autre source » (B7 bis) | suiveur à la lettre du plan ; lecteur réglé pour l'héritage ; lecteur réglé pour la tenue ; sourd qui paie | 1, 2, 3, 4a, 4b | 0,25 ; et 0,5 pour les deux lecteurs | 0,25 | lecteurs à la taille 1 ; suiveur à la valeur de φ de sa force de référence | M14 : écarts sur 200 000 sources par case, taux de rejet sur 10 000 tirages emboîtés ; **aucun critère** |
""")
r("""**Pourquoi la puissance de chaque contraste est tirée avec l'autre contraste sans effet** (famille B, deux réglages séparés) : sous la procédure de Holm, un contraste est lu au seuil de 0,025 tant que l'autre ne passe pas ; c'est le cas le plus dur. La puissance ainsi mesurée borne par le bas celle d'un dessin où les deux effets existent ; le nombre n qui en sort est donc prudent. Le lecteur aux deux réglages ensemble est rapporté à côté.""",
  """**Pourquoi la puissance de chaque contraste est tirée avec l'autre contraste sans effet planté** (famille B, deux réglages séparés ; l'autre contraste ne porte que l'effet du coût de lecture) : sous la procédure de Holm, un contraste est lu au seuil de 0,025 tant que l'autre ne passe pas ; c'est le cas le plus dur tant que l'autre contraste ne passe pas la première marche. Or il peut la passer : pour le lecteur réglé pour l'héritage, le contraste de la tenue porte le coût de lecture du bras 2, négatif ; pour le lecteur réglé pour la tenue, celui de l'héritage porte le surcoût de lecture du bras 3. Aux grands nombres de sources, ce contraste peut passer la première marche comme « effet négatif », et l'autre est alors lu à 0,05 : la puissance mesurée n'est une borne basse sûre que là où cela n'arrive pas. **La part des tirages où l'autre contraste passe la première marche est rapportée par case.** Le lecteur aux deux réglages ensemble est rapporté à côté.""")
r("""est tenu par le tirage de confirmation de C1 et de C4.""",
  """est tenu par le tirage de confirmation de C1 et de C4, dont l'intervalle est corrigé pour le nombre de cases de chaque critère (niveau 1 − 0,05/72) : moins de 0,015 par critère à un niveau vrai de 0,05 (calcul de la version 2).""")

# ---------------------------------------------------------------- B9
r("""| seuls l'engagement et la description, entre balises de donnée | une justification""",
  """| seuls l'engagement et la description (portée par `enonce`), entre balises de donnée, la part de données gelée en B4 et un classement écrit par l'enveloppe dans l'ordre du scellement ; le même essai rejoué sur la liste réduite à l'engagement seul | une justification""")
r("""| un appel au test ou un taux de rejet dans le programme d'étalonnage : l'essai échoue |
""",
  """| un appel au test ou un taux de rejet dans le programme d'étalonnage : l'essai échoue |
| 23 | garde d'équivalence S8 (ii) | couche statistique nourrie des fréquences de la couche mécanique : moyennes dans l'intervalle | la fréquence de « tient » des lois vraies divisée par deux dans la couche statistique, lue sur le bras 3 du lecteur réglé pour l'héritage à la dose 0,5 (seule conduite dont M1 dépend de cette fréquence) ; valeur fixée ici, avant l'essai, qui vérifie d'abord que ce décalage sort de l'intervalle à 24 sources et échoue sinon : arrêt |
| 24 | S8 (i) : l'épreuve simulée discrimine | exécuteur simulé sain : les deux parts sont du bon côté de 0,5 | un exécuteur qui rend « tient » à toute loi : arrêt |
| 25 | audit du générateur (B1) | générateur sain : accepté | deux lois plantées à moins de 0,25 nat : le monde est rejeté ; une dose inscrite dans la présentation : exactitude équilibrée au-dessus de 0,55, rejet |
| 26 | taille réalisée (liste d'arrêt, point 6) et règle du tirage de confirmation (couche statistique) | réglage étalonné : aucune alarme ; un compte planté de 500 rejets sur 10 000 : aucune confirmation ; 501 puis 5 235 sur 100 000 : confirmation, case tenue | un réglage faussé de 20 % : case « taille non tenue » ; un compte planté de 501 puis de 5 236 : case en échec. Les comptes sont plantés, non tirés : au niveau vrai de 0,055 la règle n'arrête que 986 fois sur 1 000 (calcul de la version 2), et un essai ne doit pas dépendre d'une graine |
| 27 | bras de diagnostic : registre étranger servi dans les seuls bras 4a et 4b (B7 bis) | la copie servie a l'empreinte du registre de la source étrangère, et aucun bras du critère ne la reçoit | le registre de la source propre servi au bras 4a (ce serait le bras 3), ou un registre étranger servi à un bras du critère : arrêt |
""")

# ---------------------------------------------------------------- ordre, rapporte
r("""1. Contre-lecture de ce texte par un autre modèle, corrections, vérification des corrections par le même contre-lecteur.""",
  """1. Contre-lecture de la version 1 par un autre modèle (faite), corrections (cette version 2), vérification des corrections par le même contre-lecteur (à faire).""")
r("""6. Étalonnage des réglages (B7) et gel de leur fichier. 7. Garde d'équivalence S8.""",
  """6. Étalonnage des réglages (B7) et gel de leur fichier. 6 bis. Couche mécanique rejouée aux réglages gelés, sous des étiquettes de graines disjointes, pour la garde d'équivalence. 7. Garde d'équivalence S8.""")
r("""Le rapport R et la puissance sous le repli.""",
  """Le rapport R, la part des entrées gardées, le facteur d'enrichissement et la puissance du contraste de l'héritage sous le repli.""")
r("""Les nombres n lus aux taux d'échec 0 et 0,5, à côté du n qui décide.""",
  """Les nombres n lus aux taux d'échec 0 et 0,5, à côté du n qui décide. La part des tirages où l'autre contraste passe la première marche de Holm, par case. **Sans critère, ajouts de la version 2** : la puissance du seul contraste de l'héritage à chaque nombre, n₁ et la lecture de S9 (« remplie », « non remplie », « indéterminée » ou « sans objet ») ; les écarts et les taux de rejet du bras de diagnostic « registre d'une autre source » (M14).""")

# ---------------------------------------------------------------- criteres de lecture
r("""où C3 et C4 sont tenus ensemble, à ce nombre et à tous les suivants (au moins 5) |""",
  """où C3 (au taux d'échec de 0,25) et C4 (aux trois taux d'échec) sont tenus ensemble, à ce nombre et à tous les suivants (au moins 5) |""")
r("""l'issue est **suspendue** : ni « lisible » ni « à reconstruire » ; elle se prononce quand la garde est jouée.""",
  """l'issue est **suspendue** : ni « lisible » ni « à reconstruire ». « Suspendue » n'est pas une quatrième issue de la table : c'est un arrêt, rapporté tel quel avec sa cause, et l'issue se prononce quand la garde est jouée.""")
r("""- **Le point 8** et la famille F ne décident de rien ; ils sont écrits dans le compte rendu et portés aux préenregistrements suivants.""",
  """- **Le point 8**, la famille F et la famille H (bras de diagnostic) ne décident de rien ; ils sont écrits dans le compte rendu et portés aux préenregistrements suivants.
- **La tenue, phrase gelée** (`GO-2026-11-19-77`, décision 2) : au préenregistrement de l'étage payant et dans tout compte rendu, une tenue « établie » se dit « servir un registre tenu, forme comprise ». Raison : la règle de validité ne protège que le contraste de l'héritage (réserve 3). Ni la famille F ni le bras de diagnostic ne changent cette phrase.
- **La puissance du seul contraste de l'héritage** (M13) et la lecture de S9 sont une information : elles ne changent ni n, ni l'issue, ni la décision du nœud 4. Si S9 est « remplie », la mère repose le nœud 4 à Lazar ; sinon, rien ne change.""")

# ---------------------------------------------------------------- contre-lecture
r("""**Non faite à l'heure où ce brouillon est rendu ; ce texte ne peut pas être scellé avant elle** (règle R2 ; pièce de classe A). Elle revient à un autre modèle que le rédacteur, qui n'a pas écrit ce texte, puis au même contre-lecteur pour la vérification des corrections. La mère inscrira ici l'identifiant du contre-lecteur, l'empreinte du brouillon relu, le chemin et l'empreinte de son rapport, et le sort de chaque remarque.""",
  """**Première contre-lecture faite, sur la version 1** (règle R2 ; pièce de classe A) : contre-lecteur neuf, modèle O, qui n'a écrit aucune des pièces lues ; brouillon relu : la version 1 (empreinte en tête de ce texte) ; rapport : la contre-lecture (chemin et empreinte en tête de ce texte) ; verdict : « scellable après corrections », onze corrections dont deux majeures. Sort de chaque remarque : annexe E. **La vérification des corrections par le même contre-lecteur n'est pas faite à l'heure où cette version 2 est rendue ; ce texte ne peut pas être scellé avant elle**, ni avant l'erratum qui inscrit le commit du code. La mère inscrira ici l'empreinte de la version vérifiée, le chemin et l'empreinte du rapport de vérification.""")
r("""le calcul des ordres de grandeur et sa sortie.

Points que le rédacteur lui demande de vérifier en premier : (a) les trois changements""",
  """le calcul des ordres de grandeur et sa sortie. Pour la vérification de la version 2 : cette version et la version 1, la contre-lecture, le mandat de la version 2, la ligne `GO-2026-11-19-77`, le calcul de la version 2 et sa sortie, le rapport du rédacteur de la version 2.

Points de la version 2 à vérifier en premier : (a) les deux corrections majeures telles qu'écrites (M10 ; K, repli, S7) ; (b) le nombre de cases de C1 et de C4, 72 chacun, et le compte de 5 236 ; (c) les deux lectures du bras de diagnostic (B7 bis), dont le bras 4b, ajout du rédacteur ; (d) le chiffrage de S9 ; (e) que la liste de ce que reçoit l'expérimentateur n'a pas été réduite sans mot de Lazar ; (f) le pronostic du point 7, changé avec la mécanique ; (g) les deux précisions faites aux gardes 23 et 26.

Points de la version 1, que la contre-lecture a vérifiés : (a) les trois changements""")

# ---------------------------------------------------------------- annexes
r("""**Manque 1 — l'étiquette « loi plantée retrouvée » est liée à la promotion par le juge statistique.**""",
  """La numérotation des deux manques suit le mandat de la version 1 ; au § 3.3 du rapport du palier 0a, ce sont les manques 2 et 1.

**Manque 1 — l'étiquette « loi plantée retrouvée » est liée à la promotion par le juge statistique.**""")
r("""la dérivation des graines (étiquettes disjointes, mondes communs aux bras).""",
  """la dérivation des graines (étiquettes disjointes, mondes communs aux bras) ; le comparateur neuf redonne la table des divergences du palier 0a sur son monde (rapport du palier 0a, § 1, et sa sortie).""")
r("""ses sorties ne sont jamais lues comme un critère, ne sont pas rapportées comme résultat, et le disent dans leur nom.""",
  """ses sorties ne sont jamais lues comme un critère, ne sont pas rapportées comme résultat, et le disent dans leur nom. Il ne calcule ni taux de rejet, ni puissance, ni taux de déclenchement, ni taille réalisée, ni rapport R : il vérifie l'exécution, la forme des fichiers et le temps de calcul, qui n'est estimé nulle part ailleurs.""")

# ---------------------------------------------------------------- reserves
r("""C'est une borne du dessin, non de cet étage ; elle revient à Lazar (rapport du rédacteur, décision 2).""",
  """C'est une borne du dessin, non de cet étage ; Lazar l'a tranchée (`GO-2026-11-19-77`, décision 2) : une tenue « établie » se dit « servir un registre tenu, forme comprise ». Le bras de diagnostic (B7 bis) dit, sans critère, si un registre tenu par une autre source séparerait la présence du contenu.""")
r("""8. **La puissance est tirée contraste par contraste**, l'autre sans effet. Le n qui en sort est prudent pour un dessin où les deux effets existent ; il peut être plus grand qu'il ne faudrait.""",
  """8. **La puissance est tirée contraste par contraste**, l'autre sans effet planté. Le n qui en sort est prudent pour un dessin où les deux effets existent, tant que l'autre contraste ne passe pas la première marche de Holm par le seul coût de lecture ; la part des tirages où il la passe est rapportée par case (B8).""")
r("""il est ici une doublure, et son sort aux paliers payants reste ouvert (rapport du rédacteur, décision 1).""",
  """il est ici une doublure ; il est joué en réel au seul palier 1, puis Lazar décide (`GO-2026-11-19-77`, décision 1).""")
r("""(iii) Les fréquences des trois classes d'issue du test de mort, par type de tentative, mesurées sur la couche mécanique,""",
  """(iii) Les fréquences des classes d'issue du test de mort, par loi et par type (M12), mesurées sur la couche mécanique,""")

for ancien, neuf in R:
    n = origine.count(ancien)
    if n != 1:
        sys.exit("chaine trouvee %d fois dans la version 1 : %r" % (n, ancien[:90]))
    if texte.count(ancien) != 1:
        sys.exit("chaine alteree par un remplacement precedent : %r" % ancien[:90])
    texte = texte.replace(ancien, neuf)

texte = texte.rstrip("\n") + "\n"
assert texte.endswith("que les tirages eux-mêmes corrigeront.\n"), repr(texte[-80:])
texte += open(sys.argv[4], encoding="utf-8").read()
open(V2, "w", encoding="utf-8").write(texte)
print(len(R), "remplacements ;", len(origine), "->", len(texte), "caracteres")
