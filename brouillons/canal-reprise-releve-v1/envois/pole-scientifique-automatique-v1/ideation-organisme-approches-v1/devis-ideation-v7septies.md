# Course d'idéation de l'organisme — devis v7 septies (option (c) seule : barème réel d'Argon ; garde de taille sur le plus petit plafond ; borne de 12 000 par fiche dite)

Lignée conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` **06:14 UTC**. **Remplace le devis v7 sexies**
(`bab9d04b…`, gardé, R12) ; le reste des v2 à v7 sexies vaut. Code : **v43** (en cours, réponse à CL9 ; relecture CL10 ciblée chez
session-depot avant tout lancement ; jusqu'à sa relecture, aucun lancement). Répond à CL9 (`eed46db3…`, CL42-01 à 07).

1. **Plafonds : inchangés** — Claude **40**, Argon **11,6**, total **51,6** (pire cas au plafond sous (c) : Claude 40,00, Argon 11,2,
   total 51,2, classement à trois juges ; CL9 § 4). **Les options (a) et (b) du v7 sexies sont retirées** : (a) parce que la garde de
   taille se réglait sur le plafond du contrôle (3,0) et non sur celui de la passe 2 (2,5), qui reçoit presque la même consigne
   (1,10 à 1,14 million de caractères) — au taux du devis la passe 2 coûtait 2,51 > 2,5, course arrêtée sans classement, Claude 0,4
   et Argon ≈ 7 perdus, et il n'existe aucun intervalle de prix où (a) aide (CL42-01) ; (b) parce que la garde la refuse avant tout
   appel (1 099 145 > 1 000 000 ; CL42-02). **Le dépassement de 0,5 USD n'est plus demandé.**
2. **Option (c), seule retenue : condition sur le barème réel d'Argon.** Le lancement est permis si le barème réel d'Argon,
   **lu par Lazar sur la console de facturation de la clé** (sources tierces, non opposables : 2 USD par million de jetons d'entrée
   et 10 en sortie jusqu'au 30 novembre, 4 et 20 ensuite), est **≤ ≈ 8,3 USD par million de jetons d'entrée, passes et sortie
   comprises** (CL9 : alors le contrôle à 1,2 million de caractères coûte ≈ 0,4 à 0,9, la passe 2 ≈ 0,5 à 1,0 avec sa sortie, le juge
   ≈ 0,5 à 1,2 : tout sous les plafonds de 2,5 et 3,5). Si le barème est au-dessus, pas de lancement : devis v8 sur mesures.
   Réglages du lancement : `--taille-max-consigne-externe 1200000` (course, explicite), `--taille-max-consigne-externe-bras 1400000`
   (bras, option de la v43 ; la valeur de la course ne vaut plus pour le juge, CL42-05), `--budget-controle-externe-usd 2.5`
   (défaut), `--budget-externe-usd 11.6`.
3. **Garde de taille (v43, CL42-01)** : par défaut, la taille maximale se règle sur le **plus petit plafond** des sessions d'Argon qui
   reçoivent la consigne (contrôle et passe 2, 2,5 chacune) au prix prudent de 2,5 × 10⁻⁶ USD par caractère, **provision de sortie
   déduite** (huit fiches de 12 000 caractères au rapport sortie/entrée du barème du code) ; la passe 2 est aussi gardée contre son
   propre plafond avant son envoi, sans dépense. **Avant le GO, mesurer les consignes réelles** avec les vrais fichiers
   (`--mesurer-consignes`, v43, sans appel ; CL42-03 : la marge de la v42 était de 846 caractères et une question de 2 000 caractères
   suffit à dépasser 1,2 million). Un refus de taille au bras compte une tentative non relançable et écrit le classement sans bras.
4. **Borne de 12 000 caractères par fiche servie (CL42-04) — changement de protocole, décision de Lazar.** La v42 refuse entière toute
   fiche de plus de 12 000 caractères (témoins compris ; ni troncature ni écart entre la fiche écrite et la fiche jugée ; quatre champs
   à 3 000 caractères sont refusés alors que chacun tient sa borne) et le dit dans la consigne des proposeurs. Options : **(i)** garder
   la règle, la nommer au devis et dans la consigne, rapporter les refus pour taille par proposeur (journal et manifeste de fin, v43),
   essai sur la phrase (W35b) — **recommandé**, confiance ≈ 0,6 : règle simple, connue des proposeurs avant le tour, et la seule qui
   borne la passe 2 d'Argon et la consigne du juge ; **(ii)** garder 12 000 comme marge du contrôle seulement, sans refuser — ne borne
   plus la passe 2 (son plafond de 2,5 peut sauter après les 14,7 de Claude) ni le juge. Aucun préenregistrement de l'idéation n'existe
   (pas d'écart à R1) ; **défaut sous 48 h : (i)**.
5. **Repli (CL42-06, R5)** : l'échec du classement de repli n'est plus silencieux (`classement-sans-bras-impossible-N.json`
   scellé, motif dans l'exception) ; deux tentatives non relançables successives jouent le second repli (W36).
6. **Tentatives et relance** : v7 sexies, point 5 (`relancable` calculé ; « trois tentatives » retiré ; **CL40-01 reste la décision
   de Lazar**).
7. **Ordre de lancement** : v7 quinquies, point 4, avec `sha256sum -c EMPREINTES-…-v43.txt`, `--mesurer-consignes` avant le GO, et
   les options du point 2.
