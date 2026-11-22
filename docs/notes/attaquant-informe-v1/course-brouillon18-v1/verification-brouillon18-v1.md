# Vérification courte — brouillon 18 du préenregistrement de la course du banc fermé — v1

- Vérificateur : Claude Opus 5.5, même contre-lecteur que pour les brouillons 15 à 17 (R2).
- Date (UTC, `date -u`) : 2026-11-22, 15:05.
- Pièces, avec leurs empreintes recalculées :
  - brouillon 18, `docs/notes/attaquant-informe-v1/course-brouillon18-v1/course-banc-ferme-v1-brouillon18.md` : `dc8fbde3e544716be042c64d2a4dd2878901661a65d028e5a5af4f8adde17fae` ;
  - remplacements, `…/course-brouillon18-v1/remplacements-brouillon18-v1.md` : `c6bb42a9f4a24608f81c3897512300502a5ed68842e5c0b7cbe188fd85cf1ac6` ;
  - brouillon 17 : `cf5d35d8472137d30defedb2a61b375037d558e3937e4371cb5d8822a507a881` ;
  - ma vérification du brouillon 17 : `0ce5d5657d1f519aeca08293f6828fefa897150d9db25f84efa5a3acc7e93bb5` ;
  - registre des décisions, `origin/main:registres/decisions.md`, ligne R-4930 seule.

**Verdict : accepté avec mineurs résiduels.**

| Vérification | Constat |
|---|---|
| Différence avec le brouillon 17 (`diff`) | **Tient.** Quatre blocs et rien d'autre : le titre ; le point 2 de la section D6 ; la ligne « Lieu d'où part l'envoi » de la table des nœuds tranchés ; la section « Contre-lecture », avec l'entrée neuve du brouillon 18 et « (à son écriture) » ajouté à l'entrée du brouillon 17. Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance, aucun critère ni aucune ligne d'arrêt ne change. |
| Lieu d'envoi : les deux endroits | **Couverts.** Les deux endroits nomment la session `session_01XJ6MgmSDBZpPAuXLe3diix`, conforme à R-4930 (« monteur de l'oracle du cycle 1, relance »). L'ancienne session n'apparaît plus que dans ces deux endroits, dite « auparavant » et « injoignable ». Aucun autre passage ne la donne pour lieu d'envoi. |
| Phrase d'état (entrée « Brouillon 18 » de la section « Contre-lecture ») | **Juste sur le fond.** Reste mineur : elle cite R-4779 (monteur injoignable) et R-4919 (accès au coffre), lignes que je n'avais pas le droit de lire et que je n'ai donc pas vérifiées. R-4930 n'a pas de repère avec commit et empreinte dans la table « Documents qui font foi », comme en avait [R79] (R6). |
| Paragraphe d'état de l'en-tête | **Mineur résiduel.** Contrairement à ce que dit la demande (« blocs 1 et 2 : titre et état »), ce paragraphe n'est pas touché. Il dit toujours « Ce brouillon 17 porte ceci… ». La ligne « Date » ne nomme pas le brouillon 18, et la ligne « Auteur » ne dit pas comment il a été produit. Correction : « Le brouillon 17 (`cf5d35d8…`) portait… » ; une phrase « Ce brouillon 18 porte… », qui reprend celle de la section « Contre-lecture » ; l'heure du brouillon 18 ; une phrase « Auteur ». |
| Entrée de vérification du brouillon 17 | **Mineur.** La section « Contre-lecture » n'inscrit pas ma vérification du brouillon 17 (« accepté avec mineurs résiduels », `verification-corrections-brouillon17-v1.md`, `0ce5d565…`), comme les brouillons 15 et 16 l'avaient fait pour leur vérification. |
| Mineurs résiduels du brouillon 17 | **Tous encore présents, non perdus, mais inscrits nulle part dans le texte.** « Sa contre-lectrice », en D8 (ligne « Tous les rôles nommés… ») et dans la ligne d'arrêt « Le lot ou une sortie lu par… » : **à corriger avant le scellement**. À porter dans la version définitive : « brouillons 15 et 16 » dans le repère [PR-3] ; la condition 12 et le paragraphe « L'oracle est figé… », qui ne nomment pas l'attestation neuve ; la puce « deux cas » de D6. La mère doit les tenir en liste jusqu'à la version définitive. |
