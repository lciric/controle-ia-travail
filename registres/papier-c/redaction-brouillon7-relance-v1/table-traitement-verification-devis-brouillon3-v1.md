# Papier C — table de traitement de la vérification du devis du pilote (brouillon 3) — v1

Date : 2026-11-22. Auteur : rédacteur du devis (session fille `session_013QMayk1rjSZrn2u9UAVhEp`). Classe C.
- Rapport traité, partie B : `registres/papier-c/redaction-brouillon7-relance-v1/contre-lecteur/rapport-verification-c3-et-devis-brouillon3-v1.md`
  (`265f62e7cfada908e93aa0d1da3e1e7e90583107a04da46b23eab378cfc55b6e`) : CD-02, CD-03 et CD-05 levées ; CD-01, CD-04
  et CD-06 levées en partie ; 1 majeure et 3 mineures neuves ; avis « scellable après corrections ».
- Devis relu : brouillon 3 (`d68649ef…`). Résultat : brouillon 4, `devis-pilote-papier-C-v1-brouillon4.md` (empreinte :
  son compagnon), écrit en entier (le brouillon 3 reste tel quel).

| Remarque | Gravité | Décision | Ce qui est fait dans le brouillon 4 | Lieu |
|---|---|---|---|---|
| CE-01, le crédit du compte ne mesure pas la dépense du pilote (recharge automatique, autres instances) | majeure | acceptée | La dépense se compte **par instance**, par son identifiant : la plus grande de deux valeurs, le calcul du lanceur (heures de marche × prix relu, gigaoctets × prix au gigaoctet, heures à l'arrêt × prix du disque) et le coût que l'interface attribue à l'identifiant, là où elle le donne ; sans coût par identifiant, le calcul du lanceur, défaut consigné. Le crédit du compte devient un contrôle : relevé avec les recharges et les autres instances actives ; la baisse corrigée, si elle dépasse la dépense comptée, est retenue à sa place ; si le coût des autres instances ne peut pas être lu, le contrôle est « non exploitable » et n'arrête rien. La règle cumulative, la garde en marche et le compte final emploient cette dépense. Lève aussi le reste de CD-01 et de CD-06. | § 5 ; § 4, ligne ; § 8 |
| CE-02, la garde de projection sous-estime le mode raisonné ; un arrêt par elle ouvre-t-il le second lancement | mineure | acceptée | Deux projections : lectures directes (après les 500 premières lectures du vivier ; elle ne compte pas le mode raisonné et le dit) ; mode raisonné (après les 6 premières lectures raisonnées de chaque juge, temps mesuré). Un arrêt par l'une d'elles est un nœud : il n'est pas une panne technique et n'ouvre le second lancement que sur le mot du directeur. Le § 1 et la ligne du § 4 le disent. Je n'ai pas pris la durée forfaitaire au pire : aucune pièce ne me donne un temps par jeton généré. | § 5 ; § 1 ; § 4 |
| CE-03, disque gardé au-delà de 2 heures : hors plafond | mineure | acceptée | Ce disque entre dans le plafond ; le lanceur écrit dans le nœud l'heure à laquelle le reste sera consommé (reste ÷ prix du disque relu ; à 0,027 USD/h, un dollar tient environ 37 heures) ; le nœud est à trancher avant. Reste un cas que la remarque ne fermait pas : sans mot à cette heure, deux règles se contredisent (le plafond, et l'interdit de détruire avant versement). Posé au directeur comme second point à dire avec le mot, avec une recommandation (garder le disque, dépassement au seul prix du disque, consigné). | § 5 ; § 3 ; § 4, point 2 |
| CE-04, fichiers réellement descendus ; fourchette de fiabilité | mineure | acceptée | Fichiers fixés par motifs à l'addendum de lancement (un seul jeu de poids par modèle, configuration, découpeur en jetons, aux révisions figées) ; tailles lues avant la création ; leur somme, plus l'image, les roues et les sorties, est la place calculée et le volume du réseau estimé ; place calculée au-dessus du disque de l'offre : pas de création. Fourchette de fiabilité corrigée : 0,978 à 0,9986 (13 relevés, recomptés par moi dans `registres/depenses.md`). | § 2 ; § 5 ; § 7 ; § 8 |

## Ce que le contre-lecteur doit savoir
- **Un point de plus pour le directeur** (§ 4, point 2) : le seul cas où le plafond peut être dépassé. C'est une
  demande neuve dans le devis ; elle est petite (prix du disque), mais elle est une dépense au-delà d'un plafond :
  elle doit être dite avec le mot, non glissée dans une règle.
- Je ne connais pas l'interface du loueur : le § 5 est écrit pour les deux cas (coût par identifiant donné, ou non),
  et le § 8 renvoie le constat à l'auteur du lanceur, avant l'addendum de lancement.
- Les seuils restent les miens : 500 lectures, 6 lectures raisonnées par juge, 30 minutes, 2 heures, fiabilité 0,97,
  disque de 80 Go. Aucun ne lit un score.
