# Course d'idéation de l'organisme — devis v7 sexies (v42 ; contrôle d'Argon recalculé ; garde de taille ; bornes de fiche)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **05:08 UTC**. **Remplace le devis
v7 quinquies** (gardé, R12) ; le reste des v2 à v7 quinquies vaut. Code : **v42** (396 essais ; LISEZMOI `78df10a6…`, EMPREINTES
`637028fc…` ; relecture CL9 du différentiel v41 → v42 chez session-depot avant tout lancement). Répond à CL8 (`ffa07b12…`, CL41-01
à 08) et au doute principal de la v41.

1. **Plafonds** : inchangés en principe (Claude **40** ; Argon **11,6** ; total **51,6**), **mais le point 2 montre que le contrôle
   d'Argon de la course ne tient pas dans 2,5 aux tailles du devis** : voir le nœud du point 2.
2. **Contrôle d'Argon de la course, recalculé** (CL41-02 ; `sonde_tailles.py` du relecteur, rejoué sur la v42). Aux réglages du
   devis (pièces 750 000 + matériau attesté 350 000, huit fiches), la consigne de contrôle fait **1 199 154 caractères** (v41 :
   1 456 740 ; v40 : 1 132 223) grâce aux bornes de fiche de la v42 (au plus 9 questions, 12 antériorités, **12 000 caractères par
   fiche servie** — règle de validation neuve, une fiche plus longue est refusée seule avec son motif ; à confirmer ici). Coût au
   taux que le devis suppose (2,5 pour 1,1 million) : **2,73** ; au barème le plus haut du code (10 USD par million de jetons,
   4 caractères par jeton) : **3,00**. Les pièces et le matériau seuls font déjà ≈ 2,5 à ce taux : **toute marge de fiches dépasse
   2,5**. **Nœud (dépense, décision de Lazar)** : (a) **`--budget-controle-externe-usd 3.0`** et Argon porté à **12,1** (contrôle 3,0
   + 2 × 2,5 + juge 3,5 + contrôle du bras 0,2 = 11,7, marge 0,4), **total 52,1** (+ 0,5) — recommandé, confiance ≈ 0,7, et
   couvert à mes yeux par le GO anticipé sur les dépassements (R-383 : rallonge ≤ 50 % du plafond concerné, course déjà sous GO)
   sauf avis contraire de Lazar ; (b) `--taille-max-pieces 650000` pour rester sous 2,5 — perd ≈ 13 % du corpus servi ;
   (c) session-depot confirme d'abord le barème réel d'Argon : s'il est de 1 à 2,5 USD par million de jetons, 2,5 suffit
   largement (≈ 0,4 à 0,9) et l'on fixe `--taille-max-consigne-externe 1200000` explicitement. **Défaut sous 48 h : (a).**
3. **Garde de taille sans dépense** (CL41-01, v42) : avant tout contrôle, la course et le bras refusent, sans rien payer et avec
   motif scellé, toute consigne externe au-delà de `--taille-max-consigne-externe` (défaut : plafond de la session receveuse
   divisé par un prix prudent de 2,5 × 10⁻⁶ USD par caractère : **1 000 000** pour la course à 2,5, 1 200 000 à 3,0 ;
   1 400 000 pour le juge à 3,5). **Aux réglages du devis, le défaut à 2,5 refuse la course** (1 199 154 > 1 000 000) : le
   lancement passe donc `--budget-controle-externe-usd 3.0` (a) ou `--taille-max-consigne-externe 1200000` (c). Le juge d'Argon
   (plafond 3,5) reçoit au plus ≈ 1,38 million de caractères avec le gabarit borné : sous la garde, à la limite du plafond au
   taux du devis (≈ 3,1) ; le contrôle du bras est **court** (41 caractères, comme la v40 ; CL41-01 option (B)) — le risque de
   taille est porté par la garde, pas par un contrôle payé.
4. **Ordre des contrôles** (CL41-07) : **Argon d'abord**, puis les deux contrôles Claude ; une panne d'Argon au contrôle ne coûte
   rien chez Claude et laisse la relance permise tant que la somme externe tient. Clôture de chaque contrôle (CL41-03) :
   matériau entre délimiteurs, « Fin du matériau. Réponds exactement OK, sans rien d'autre. ».
5. **Tentatives et relance** (CL40-01, CL41-05, 06) : `relancable` est **calculé** (sommes de la relance, coûts imputés, compte des
   tentatives) et son motif nomme l'hypothèse « relais gardé » avec le calcul « relais relancé à neuf » à côté ; la phrase
   « trois tentatives au plus » du v7 quinquies **est retirée** : aux réglages du devis, un contrôle payé qui échoue rend la
   relance impossible (somme Claude = 40,0 exactement) — **CL40-01 reste la décision de Lazar** : (a) tout échec de contrôle
   payé = son mot (recommandé par session-depot, que je rejoins) ; (b) marge 41,2 / 16,6 ; (c) ne pas rejouer les contrôles
   réussis. Manifeste de départ écrit avant la création de SORTIE (plus de SORTIE vide « relançable »).
6. **Bras** : `--budget-externe-usd` transmis au bras ; dès qu'une tentative du bras est scellée non relançable, le **classement
   « sans juge externe »** (deux juges Claude) est écrit — aucune course payée ne reste sans classement.
7. **Ordre de lancement** (v7 quinquies, point 4) avec `sha256sum -c EMPREINTES-…-v42.txt`, et les options du point 3.
