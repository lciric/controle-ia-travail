# Fiche de lecture — 2506.24068 v3 — « STACK: Adversarial Attacks on LLM Safeguard Pipelines »

- **Auteurs** : Ian R. McKenzie, Oskar J. Hollinsworth, Tom Tseng, Xander Davies, Stephen Casper, Aaron D. Tucker, Robert Kirk, Adam Gleave (FAR.AI, institut britannique de sûreté de l'intelligence artificielle, Oxford) ; arXiv 2506.24068 v3, 5 février 2026.
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/2506.24068v3.pdf`, sha256 `3e08b7ccfe395ab1fd4d7f3413f1fdb3a0b2c78fc67dff7766c1af03612bf1f7` (recalculée, concorde avec le registre, R11).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, l. 87 (point 2, contre-indices à la pince) ; usage vérifié dans la v3 en vigueur (l. 96 ; l. 217, « à citer quand le point est abordé »), non touché par ses errata 1 à 3.
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46:50Z.

---

**(a) Ce que le papier établit.** Une chaîne de défense ouverte, faite d'un classifieur d'entrée et d'un classifieur de sortie autour d'un modèle génératif (Qwen3-14B, p. 6 du PDF) ; aucun classifieur de transcription, aucune sonde sur activations dans la chaîne (p. 3). Un classifieur par exemples dans la consigne ramène à 0 % le succès des attaques de base sur le jeu d'abus catastrophique ClearHarm (p. 1). L'attaque étagée, qui casse chaque étage à son tour puis les combine, atteint 71 % de succès en boîte noire, et 33 % par transfert, sans accès à la chaîne visée (p. 1, 10). Les 71 % supposent que l'attaquant voit quel étage a bloqué ; la recommandation est de le cacher, réponses de refus semblables et passage par tous les étages contre les canaux de temps (p. 10). Le domaine est l'abus par requête, non le sabotage.

**(b) Ce que voulait la décision.** Un contre-indice : « une chaîne de garde-fous se défait étage par étage ». **Le permet en partie** : vrai pour des regards séparables qu'on attaque un à un avec retour, et encore à 33 % sans ce retour. Rien sur deux regards liés par une relation que l'honnête respecte (le dilemme du point 2), ni sur des états internes, ni sur un dommage diffus. Ces silences sont la limite du papier (R8).

**(c) Usage.** Pour l'entretien, objection « vos deux regards, c'est la défense en profondeur, et STACK la casse » : on concède pour la réunion d'alertes, on répond par le dilemme, non revendiqué, et par le cloisonnement. Pour le bras d'attaque informé, il fournit une épreuve, l'attaque étagée, et une règle de conception : aucun retour à l'agent sur la mâchoire qui a sonné. Il crée une antériorité sur « attaquer une chaîne de défense étage par étage » : à citer, jamais à revendiquer.

**(d) Plus petite action.** Ajouter la page 10 (le retour sur l'étage bloquant fait la force de l'attaque) à la citation du point 2 dans la prochaine version de N-075, et une ligne « attaque étagée » à la liste des attaques du bras informé, sans dépense. Coût : vingt minutes de session ; la rejouer contre nos sondes demanderait un devis et un GO.
