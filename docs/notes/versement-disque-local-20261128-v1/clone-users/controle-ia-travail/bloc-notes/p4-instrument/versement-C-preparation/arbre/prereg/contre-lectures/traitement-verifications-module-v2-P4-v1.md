# Traitement des deux vérifications du module v2 de P4-instrument — v1

Session 14. Décisions prises le 2026-10-20 vers 19:45 UTC et données telles quelles au correcteur du module v3 dans la
consigne de l'orchestration `wf_07b10b79-4d5` (correcteur lancé à 19:49 UTC). Elles sont écrites ici vers 21:45 UTC,
sans changement, pour être versées avec les rapports. La session n'a écrit ni le module, ni aucun rapport traité.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

Rapports traités :
- vérification « contournement » du module v2 :
  `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md`
  (`2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d`), « conforme après corrections » : 2 mineurs,
  4 de forme, 2 informations ;
- vérification « fidélité » du module v2 : `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md`
  (`ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196`), « conforme après corrections » : 3 mineurs,
  2 de forme.

| constat | décision | où |
|---|---|---|
| VM2-contournement-01 (mineur) : données d'un autre run sous le manifeste du run nommé | accepté : la lecture exige que l'identifiant des données du run source (résultat, résumé, identité) soit celui du manifeste lu et du dossier ; sinon refus sans rien écrire | module v3 |
| VM2-contournement-02 (mineur) et VM2-fidelite-01 (mineur) : rangées hors de la forme `\| Lk \|` ignorées par la garde de table | accepté : la garde compare toute la table de la section « Critères de lecture gelés » (chaque rangée entre l'en-tête et la fin du tableau, quelle que soit sa forme) à `LIGNES` ; une rangée en plus, en moins ou hors de la forme : refus | module v3 ; paires du texte |
| VM2-contournement-03 : section « Critères de lecture gelés » présente plus d'une fois | accepté : refus | module v3 ; paires du texte |
| VM2-contournement-04 : configuration du manifeste qui n'est pas un dictionnaire | accepté : traitée comme suspecte, refus au motif de CL3-01 (code 1, « ARRÊT », aucune trace Python) | module v3 ; paires du texte |
| VM2-contournement-05 : manifeste orphelin si `diag/<run de lecture>` existe | accepté : refus R12 avant la création du manifeste | module v3 |
| VM2-contournement-06 : fichiers `__pycache__` écrits sous le dossier du module | accepté : `sys.dont_write_bytecode = True` en tête de `lecture_p4_v1.py` et `instrument_p4_v1.py`, avant tout import du dépôt ; commandes écrites avec `-B` ; un test vérifie qu'une lecture refusée n'écrit aucun `__pycache__` | module v3 ; paire du plan d'analyse, point 2 |
| VM2-contournement-07 : source « complet » sans manifeste | accepté : refusée par `lire` | module v3 |
| VM2-contournement-08 (information) : comportement L1 gardé | rien à faire | — |
| VM2-fidelite-02 (mineur) : « Tests attendus » hors de la forme lue par la chaîne | accepté : `ecrire_candidat2_v1.py` écrit « Tests attendus : `N` » ; le reste de la ligne passe par une paire exacte (258 tests du module, 71, 49 et 138 ; `P4_TEXTE_PREREG`) | candidat 2 |
| VM2-fidelite-03 (mineur) : plan d'analyse, point 2, sans la garde de table ni le refus sans `--prereg` | accepté : deux paires exactes | candidat 2 |
| VM2-fidelite-04 (forme) : « Chaîne de lancement » garde « 194 tests » | accepté : « (faits, 194 tests ; module v3, après la contre-lecture 3 et les vérifications du module v2 : 258 tests) » | candidat 2 |
| VM2-fidelite-05 (forme) : deux ancres citées sans leurs retours à la ligne | accepté : ancres exactes, chacune comptée une fois | paires du module v3 |

Suite : module v3 (`…/module-v3/`, 258 tests : 71, 49 et 138) vérifié par un sous-agent neuf :
`…/verification-module-v3/verification-module-v3-v1.md`
(`86577f3d6d5b2c9edf7d893a041ebcd11d8322f2645c3337a545dfa5a881038f`), « conforme après corrections » : 1 de forme
(VM3-01 : deux phrases proposées disaient « refusée sans rien écrire » là où le module écrit L1 en mode décisif ; paires
corrigées par le vérificateur, mêmes ancres, éprouvées), 7 informations. Paires retenues pour le candidat 2 :
`…/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json`
(`324c164fd1cd2d9c654ec8b0ed120ed2cca90a224151652c3467e0640574ba7a`).
