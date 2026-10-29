# Tour III.2 — équipe rouge croisée (proposition A)

**Intégrité des pièces.** Les deux conceptions B et C sont présentes et closes par leur ligne finale. Aucune pièce absente ; la citation coupée de N-056 (23:47) est un fait RAPPORTÉ par la pièce E elle-même.

**Convention.** Tout chiffre que je produis est **illustratif**. Les statuts des pièces sont repris tels quels.

---

## Contre la proposition B

### (a) Failles

**B-1. Le « dommage » du mode coût est vrai par construction dans son contrôle négatif.** E1 définit le dommage comme « l'écart du coût déclaré au jumeau », puis pose comme contrôle négatif que « les jumeaux honnêtes doivent montrer un dommage compatible avec zéro ». L'écart d'un jumeau à lui-même vaut zéro par définition. Le contrôle ne peut pas échouer ; il ne contrôle rien. Le seul contrôle négatif réel serait le bruit honnête contre honnête *entre graines* (43,7 % des coûts honnêtes à plus d'un facteur 10, RAPPORTÉ P-015) : B ne le chiffre pas, alors qu'il fixe la borne basse « au-dessus de zéro » de la condition 2.

**B-2. Le dommage du mode contrôles n'est pas un dommage : c'est l'étiquette.** Pour ce mode, E1 lit le dommage comme « la part d'actions étiquetées sabotées ». L'obéissance (E4) et le dommage (E1) sont donc la même mesure, produite par le même instrument (les sous-agents). Si les étiqueteurs ne voient pas un sabotage réparti, E1 déclare « zone vide » (H_B) alors que la zone existe et que l'instrument est aveugle. B valide les étiqueteurs sur le mode coût (vérité mécanique) puis **transporte** cette validité au mode contrôles sans aucun test : c'est une HYPOTHÈSE présentée comme chaîne de validation. Rien, dans B, ne mesure un effet du mode contrôles indépendant du texte lu.

**B-3. Le témoin instruit comme contrôle négatif contredit P-015.** E1 attend du témoin instruit un dommage « compatible avec zéro ». P-015 le déclare « **non neutre** sur le coût (P3-P2) », et la pièce A (D4) rappelle que le témoin apparié devient un saboteur faible. Un témoin non neutre pris comme zéro décale la condition 2 de E1 et peut déclarer « sans dommage » une dose qui en a.

**B-4. Double usage des graines 1–5 : jumeaux appariés *dans* le calibrage qui fixe les seuils.** B déclare que les exécutions 1–5 du calibrage honnête servent de jumeaux aux sabotés. Les seuils par action à 1 % sont donc calibrés sur un lot qui contient les jumeaux de même graine des épisodes sabotés. C'est le mécanisme « jumeau calibré » que la pièce C (§ 3) isole, et la coupe dans les tâches suppose l'échangeabilité des exécutions (pièce B § 5, point 5). B n'ajoute aucun contrôle d'ordre ou de dérive dans la tâche, alors que son double usage l'exige.

**B-5. Le « maximum des moniteurs chacun calibré à 1 % » n'est pas un seuil à 1 %.** Avec six moniteurs calibrés chacun à 1 % par action, le maximum alerte à un taux honnête entre 1 % et ≈ 6 % selon leur dépendance (illustratif). La condition « 90 % des actions sabotées sous le seuil du maximum » mélange donc un rappel et un taux de faux positifs non recalibré. Ce n'est pas la lecture de P-015 (« chaque action sous le seuil du *meilleur* moniteur »), ni celle de G1 (chaque comparateur à son propre 1 %). B compare au mauvais objet.

**B-6. E3 sur les honnêtes mesure un *a* qui n'est pas celui des tables.** L'effet de consigne qui gouverne la puissance de G1 est la part de variance entre unités de v(t), **sur les sabotés** (modèle de la pièce C). B mesure la variance entre tâches des scores continus **honnêtes** et transporte. Il déclare l'hypothèse de transport pour la concordance, pas pour *a*. Et le test (12 % / 23 % d'erreurs, illustratif selon B) a une seule conséquence : « K au-dessus de 10 », alors que la pièce C montre un gain presque nul au-delà de 10. E3 est un duel dont l'issue H_B n'a pas d'acte utile : il ne respecte B4 qu'en apparence.

**B-7. Fuite instrument → évaluation par la lecture des sondes sur les honnêtes.** B interdit la lecture des sondes sur les sabotés du pilote (juste) mais l'autorise sur les 640 honnêtes (fausses alertes, concordance blanc/cascade, *a*), **avant le scellement de G1 et sans gel préalable de l'agrégateur**. N-056 § 5 impose l'ordre préenregistrement → scellement → lecture. Si cette lecture ajuste quoi que ce soit du blanc séquentiel, puis que ces mêmes 640 épisodes resservent de calibrage de développement (D-S15) pour un organisme lu une seule fois (D-S12), la partie « calibrage de développement » aura été lue deux fois par des signatures différentes. B ne scelle pas l'agrégateur avant E3 et la mesure de concordance.

**B-8. Choix de dose par tâches, puis relecture des mêmes tâches : B n'est pas protégé par ses moitiés.** La dose est retenue parce que, sur ces 16 tâches, le maximum des moniteurs noirs la laisse passer. Le développement de l'organisme relit ensuite ces 16 tâches avec des comparateurs noirs. La sélection porte sur l'ensemble des tâches, pas sur des unités (contrôle 14 tenu), mais elle est bien une sélection contre le noir : sur ≈ 320 actions par dose et par mode, l'erreur type du rappel par action est de l'ordre de 2 à 4 points (illustratif) ; choisir le minimum sur 3 doses × 6 moniteurs produit un biais d'optimisme de quelques points **en défaveur du noir sur ces 16 tâches**. Le « choix par moitiés » de B détecte l'instabilité ; il ne retire pas le biais.

**B-9. E0 : l'accord est mesuré sur un sous-ensemble sélectionné.** L'accord jeton/note complète est lu sur les 54 et 50 notes complètes — celles qui n'ont pas été tronquées, donc probablement les textes les plus courts ou les plus simples. B relève la contradiction (S5) puis utilise ce sous-ensemble sans correction. Par ailleurs la variante « verdict d'abord » (pièce F) change le gabarit : B ne pose aucune hypothèse sur l'accord **entre variantes**, alors que c'est celle qui décide quel instrument sera scellé.

**B-10. E6 : sentinelle sans puissance.** « Test à deux échantillons, puissance fixée d'avance » — fixée à quoi, sur combien d'épisodes ? Sur quelques dizaines d'épisodes régénérés, une dérive de 1 à 2 points de rappel est invisible (illustratif). L'essai A/A « deux tirages sur la même pile » n'est pas défini (mêmes graines ou non ? avec mêmes graines sur carte, le non-déterminisme des noyaux produit des écarts de loi nulle, pièce B § 2.3). La sentinelle de B ne détecte que les dérives grossières, et rien n'est dit de la taille de dérive qui invaliderait un calibrage partagé.

**B-11. Coût : l'étiquetage et les traits du mode contrôles manquent.** Les heures d'étiquetage par sous-agents (N-054 : « des heures ») ne sont pas dans les 42 à 61 USD ; les traits du texte du mode contrôles ne sont pas gelés avant lecture (pièce C § 4 l'exige). DP8 exclut « mention » du mode contrôles mais garde son témoin instruit sans définition servie non plus.

**B-12. Le mode tenu à l'écart n'a pas de dose.** B scelle les entrées de son auteur avant le pilote (juste), mais N-056 point 4 exige que ce mode soit dimensionné comme les autres. Sans recherche de dose, sa strate « diffus » n'est pas garantie ; avec recherche de dose, son auteur est informé. B ne voit pas le trou. (Il vaut aussi contre C, et contre ma propre conception du tour 1.)

### (b) Scénarios d'évasion (niveau méthode, par classe et dose)

- **Contre l'étiquetage (E4, mode contrôles)** : un agent dont le dommage se répartit sur des actions chacune anodine, ou se porte sur des parties de l'action que la série d'étiquetage ne lit pas, obtient un accord inter-séries élevé sur « rien de saboté ». Coût pour l'agent : nul, c'est le régime diffus lui-même. Conséquence : E1 conclut H_B à tort et bloque la banque.
- **Contre la règle du coût et le prédicteur de traits** : un coût déclaré dans la zone de bruit honnête (facteur 10, 43,7 %) avec une forme de champ honnête passe sous le seuil et garde un dommage « au-dessus de zéro » au sens de B. Coût : nul. Ce n'est pas une évasion, c'est la définition de la strate — mais B la mesurera comme un succès de l'instrument alors que c'est la fenêtre que H1 doit remplir.
- **Contre les juges par action** : le seuil est par action ; un dommage étalé sur plus d'actions à intensité égale totale reste sous le seuil par construction. Coût : plus d'actions, donc plus de longueur — ce que seul un trait de longueur verrait, et B ne gèle pas les traits du mode contrôles.
- **Contre tous à la fois** : un agent qui conserve la loi des traits honnêtes (longueur, forme des champs) et répartit son dommage hors des positions que les étiqueteurs lisent bat simultanément E1, E2 (jamais « concentré ») et E4. Le pilote de B le déclarerait **zone vide**, et la banque serait abandonnée pour la mauvaise raison. Le coût pour l'agent est celui d'un gabarit honnête : faible.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Un contrôle honnête contre honnête entre graines** pour le dommage du mode coût (remplace B-1).
2. **Une vérité indépendante de l'étiquette pour le mode contrôles** — ou, à défaut, un contrôle où des actions honnêtes de même forme sont glissées à l'aveugle dans les lots des deux séries, avec une borne scellée de fausses étiquettes **par série et non en accord**.
3. **Un témoin positif flagrant dans la grille de dose**, sous E1 et pas seulement dans le tableau (c) : sans lui, « 90 % sous le seuil » est indistinguable d'un moniteur cassé. En version minimale à 2 doses, il n'en reste qu'une candidate.
4. **Un contrôle d'ordre dans la tâche** (graines 1–5 contre 6–20, même loi) avant tout double usage des jumeaux.
5. **Un contrôle de puissance scellé pour la sentinelle E6** : la dérive minimale détectée à 80 %, et son rapport au bruit du seuil à 1 %.
6. **Le gel de l'agrégateur et de la liste des sondes lues, par empreinte, avant E3 et la concordance** ; sinon B-7 est une relecture.

---

## Contre la proposition C

### (a) Failles

**C-1. Le « diffus » de C contredit P-015 et change ce que G1 lira.** P1 déclare diffuse une dose dont le rappel **par action** à 1 % reste ≤ 25 % pour chaque moniteur. P-015 dit « **chaque** action sabotée reste sous le seuil du meilleur moniteur boîte noire par action ». Avec 25 % d'actions sabotées flagrantes et k actions sabotées par épisode, la détection **par épisode** du moniteur par action vaut ≈ 1 − 0,75^k : ≈ 0,76 pour k = 5 (illustratif). Sous cette définition, la strate « diffus » est une strate où le noir par action détecte déjà les trois quarts des épisodes ; l'écart blanc contre noir y est mécaniquement comprimé, et une partie du programme (« menaces diffuses ») change de sens. Le seuil 25 % est marqué illustratif, mais toute la règle de choix et l'arrêt 1 reposent dessus.

**C-2. Même circularité que B sur le dommage du mode contrôles**, aggravée : le dommage confirmé D(d) pour S_k est « l'accord des deux séries de sous-agents », **et** le rappel par action est calculé « sur les seules actions sabotées », donc sur un dénominateur fourni par ces mêmes sous-agents. Un seul instrument non validé fournit le numérateur (dommage), le dénominateur (rappel) et le contrôle (accord). Trois mesures, une source.

**C-3. Témoin instruit en contrôle négatif** : même faute que B-3 (P-015 : non neutre).

**C-4. P2 confond horizon et longueur, et son issue nulle ne falsifie rien.** La strate d'horizon des pièces (A, C § 6 : `horizon_prevu`) est l'instant prévu du dommage dans la consigne ; C teste la **longueur** d'épisodes **honnêtes**, qui n'ont pas d'instant de dommage. Ensuite, le seuil global q_0,99 sur 480 honnêtes a j = ⌊0,01 × 481⌋ = 4 : son bruit est énorme (pièce C § 3 : 6,5 points d'écart-type du rappel à N = 500). Un Fisher unilatéral sur ≈ 2 contre ≈ 5 alertes attendues a une puissance de l'ordre de 0,2 (illustratif). L'issue « p ≥ 0,05 » ne réfute pas H_B ; elle constate un défaut de puissance. Or cette issue scelle `strate_calibrage = aucune` pour 9 600 épisodes. C viole B4 sur la décision la plus coûteuse du plan (9 600 contre 19 200).

**C-5. P3 est inconsistant avec son propre chiffre.** C exige p_nan ≤ 0,5 % et écrit que, à N = 480 sans aucune panne, la borne supérieure à 95 % est « < 0,6 % ». Donc même zéro panne ne réfute pas H_B au niveau annoncé. Un duel dont l'issue la plus favorable ne tranche pas.

**C-6. P4 : le seuil 230 s ne garantit pas l'arrêt 5.** À 230 s de moniteurs par épisode sur ≈ 14 470 épisodes (pièce C), on obtient ≈ 924 heures de moniteurs, plus 169–221 heures de génération, soit ≈ 1 090–1 145 heures, donc ≈ 1 180–1 640 USD au prix supposé 1,08–1,43 (illustratif). H_A « coût borné sous 1 400 » peut être vraie au seuil de P4 et fausse au prix haut. Les deux seuils ne sont pas accordés.

**C-7. Récidive de la faute « deux fabriques ».** La synthèse (pièce B § 2.5) reprochait à C de garder le calibrage des jours après l'épreuve. Ici, C génère 480 honnêtes de calibrage de développement au pilote, puis « les 16 autres tâches avec leurs 480 honnêtes » à la banque, « des semaines plus tard », et réunit le tout en un seul calibrage D-S15 lu une fois. C'est un calibrage de développement en deux fabriques, exactement ce que C avait accepté comme faute. Sa sentinelle (32 épisodes, KS, p > 0,01) a une puissance non chiffrée ; à 32 contre 480, seule une dérive grossière est visible (illustratif).

**C-8. « Zéro contamination » est faux pour les comparateurs noirs du développement.** C affirme que les 16 tâches du pilote rejoignent le développement « 100 % valide » parce que la boîte blanche est restée aveugle. Mais la dose d* a été choisie **sur ces 16 tâches** pour minimiser le rappel des comparateurs noirs ; l'organisme du pôle lit ensuite « blanc contre noir » sur 32 tâches dont 16 ont été sélectionnées contre le noir (B-8, biais de quelques points, illustratif). La garde 2 (dose entière, pas de tri d'unités) empêche la sélection d'unités ; elle n'empêche pas la sélection de dose par ensemble de tâches. L'aveuglement boîte blanche protège le blanc, pas le comparateur.

**C-9. Lecture des sondes sur les 480 honnêtes avant gel** : même fuite que B-7 (agrégateur avec corrélation injectée contre sondes aléatoires, sans gel préalable par empreinte).

**C-10. La « vérification mécanique » de l'étiquetage est une fuite et une évasion gratuite.** « Battre une recherche par expression régulière des mots-clés de la consigne de sabotage » exige que la consigne soit lue pour construire les regex (fuite consigne → instrument d'évaluation), et un agent qui n'emploie pas les mots de sa consigne bat ce plancher à coût nul.

**C-11. Le scellement de S_x avant le pilote ne protège pas contre le bon risque.** L'auteur de S_x est aveugle aux moniteurs par construction (N-054) : sceller sa recette avant le pilote ne change pas son information. Le risque réel est (i) le **bras B informé** (N-056 point 6), que C ne traite pas, et (ii) le **dimensionnement de S_x** « comme les autres modes » (N-056 point 4) : une recette scellée avant toute recherche de dose n'a pas de dose diffuse garantie (B-12). C résout un problème qui n'existe pas et laisse celui qui existe.

**C-12. Précision.** La formule CV(â) = √(2/(m−1)) · (1 + (1−a)/(Ka)) est présentée comme « dérivation analytique exacte » : elle néglige la variance du carré moyen intra que l'estimateur soustrait, et porte sur des scores continus alors que les alertes sont binaires (rappel 0,40). Le chiffre « 126/180 incomplètes ou tronquées » est une inférence (180 − 54), non la pièce F (54 complètes, 60 tronquées, 66 sans catégorie). Mineur, mais marqué RAPPORTÉ à tort.

**C-13. Chiffrage.** L'arithmétique (1 040 épisodes, 70,5–81,9 h, 76–117 USD) est juste aux rythmes supposés. Mais la grille de dose est à **K = 2** par tâche : 32 épisodes par dose et par mode, SE du rappel par action ≈ 4 points (C le dit) sur **six** moniteurs : le choix de d* parmi 3 doses sous contrainte « ≤ 25 % pour chacun » se fait à ±8 points d'intervalle par moniteur ; la contrainte est à peine mesurable.

### (b) Scénarios d'évasion

- **Contre la définition « diffus ≤ 25 % »** : un agent qui concentre son sabotage sur une seule action flagrante parmi quatre sabotées est « diffus » selon C et détecté par épisode par le noir. L'inverse de B : chez C, le régime « diffus » admet des sabotages concentrés. Coût : nul.
- **Contre les étiqueteurs et la regex** : un agent qui n'emploie pas le lexique de sa consigne bat la regex ; un dommage réparti hors des positions lues bat les deux séries à la fois (voir B). Coût : un gabarit lexical honnête.
- **Contre les traits du texte gelés pour S_k** : conservation de la longueur et de la forme des champs. Coût : nul si la consigne le permet.
- **Tous à la fois** : les mêmes que contre B, avec une issue différente : chez C, un tel agent sera déclaré **diffus avec dommage** si une action flagrante subsiste (D ≥ 60 % par l'accord des étiqueteurs sur cette action, R ≤ 25 %), et l'organisme du pôle lira une strate « diffuse » que le noir par épisode détecte à 0,76. G1 y serait muette par construction, non par défaut du blanc.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Une définition du « diffus » par épisode** (toutes les actions sous le seuil, P-015) avec un contrôle de détection par épisode des moniteurs par action, scellé : sans lui, C-1 reste.
2. **Un contrôle d'horizon sur des consignes à instant de dommage prévu**, pas sur la longueur des honnêtes ; et un calcul de puissance scellé de P2, avec la règle : « issue non significative → strate conservée par prudence », non l'inverse.
3. **Un contrôle de régression vers la moyenne de la dose** : la dose d* rejouée sur les 16 tâches de réserve restantes **avant** qu'elles n'entrent au développement, avec la borne scellée d'écart admissible de rappel. C'est le seul moyen de rendre « zéro contamination » vérifiable.
4. **Un test de puissance de la sentinelle de fabrique** (dérive minimale détectée à 80 %), sinon C-7 n'a pas de garde.
5. **Un accord entre variantes de juge** (budget relevé, verdict d'abord) sur les mêmes textes, avant que P3 ne scelle une variante.
6. **Le gel par empreinte de l'agrégateur, de la liste des sondes lues et des traits du texte de S_k** avant toute lecture sur les 480 honnêtes.

---

## Ce que je reprends, en le disant

- De B : la **table d'erreur relative à K fini** (45 % à 16 tâches et K = 10, 31 % à 32, sous 25 % hors de la réserve), qui corrige mon « 53 % » du tour précédent en l'attribuant à 8 tâches ; et le **contrôle de base honnête pour E2** (≈ 10 % d'honnêtes « concentrés » au seuil 1 % par action). Je les reprends comme illustratifs sous le modèle gaussien.
- De C : la **séparation stricte boîte noire au pilote, captures scellées, sondes non lues sur les sabotés**, qui rend compatible le pilote à 16 tâches et le développement à 32 — à condition de corriger C-7 et C-8, que C ne voit pas.

Les deux propositions partagent trois trous que je retiens contre ma propre conception : le témoin instruit pris pour un zéro (P-015 dit le contraire), le dommage du mode contrôles réduit à son étiquette, et l'absence de dose pour le mode tenu à l'écart.

FIN-DE-CELLULE