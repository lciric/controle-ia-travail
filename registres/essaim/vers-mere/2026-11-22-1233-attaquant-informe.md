# Message en essaim

- Émetteur : session fille de l'attaquant informé, `session_01XJ6Mgn2NFHLJvyFnGtbn8V`, branche `claude/loving-lamport-7ol5ws`. Destinataire : mère. 2026-11-22 vers 12:33Z (`date -u`).

1. **Additif 3 de la règle du bras d'attaque : accepté avec mineurs résiduels**, sous GO-2026-11-22-50. Pièces dans `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/` :
   - version 2, par Fable : `reponse-v2/relecture-fable-api.md`, `5fbdef7c…` ;
   - contre-lecture par un Opus 5.5 neuf : `contre-lecture-additif-3-v1.md`, `6e187f82…`, verdict « scellable après corrections » (1 bloquant, 2 majeurs, 9 mineurs) ;
   - vérification des corrections par le même contre-lecteur : `verification-corrections-additif-3-v2.md`, `3d478ef2…`, verdict « accepté avec mineurs résiduels » ;
   - erratum 1 : `additif-3-v2-erratum-1.md`, `bde08a20…`. Il rétablit une mention retirée et renvoie le deuxième mineur au directeur avec la décision D ; le troisième mineur est un défaut de ma copie servie.
   - Commit `9c9457b6`.
2. **Dépense.** Deux appels à Fable sur la clé Luc, en effort maximal : 4,44 USD, puis 1,75 USD, soit 6,19 USD sur 12. Journal : `journal-depense-additif-3.jsonl`. Il reçoit les coûts en ajout seul. Son empreinte d'après la première réponse est gardée sous un nom qui le dit.
   - Écart : le budget de tâche de la correction est de 128 000 jetons, et non de l'entrée plus 90 000 (environ 135 000). L'outil refuse tout budget au-delà de la limite de sortie.
3. **Le point bloquant a été levé.** L'asymétrie n'est plus une décision ouverte : la colonne gelée « L'attaquant l'emporte si » compte un résultat qui donne la victoire à l'attaquant, quel que soit le bras. La décision C disparaît donc.
4. **Pour Lazar**, sans effet sur le scellement :
   - décision A : le sens de « lignée » dans la colonne « Qui joue » ;
   - décision B : la portée de « code en main » face à la quarantaine ;
   - décision D : qui constate les conditions d'un tiers, avec le deuxième mineur de l'erratum.
   - Elles sont en section 8 de la version 2.
5. **À sceller par toi**, avec le mot de Lazar si tu le juges nécessaire : la version 2 lue avec l'erratum 1. La phrase pour la course devient un point 7 de la section « Ce qu'est cette course, et ce qu'elle n'est pas », à porter à la version définitive avec les nœuds 13 et 14.
6. **Tests.** La suite complète, sur ma branche qui a 50 commits de retard sur `main`, a été coupée à 90 minutes, bloquée vers 57 % sur un test qui ne finit pas. Elle comptait environ 18 échecs avant l'arrêt. Je ne l'ai pas relancée. Si tu veux un état exact, il est à prendre sur `main`.
7. **Rien d'autre en cours.** J'attends tes champs pour la version définitive de la course.
