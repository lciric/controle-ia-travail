# Collisionneurs v8d, compte rendu 57 : réponse de Fable sur le pilote de l'essaim (1,46 USD)

Écrit à 2026-11-22T13:33:21Z (`date -u`).

- Envoi par l'outil v5, clé RR_ANTHROPIC_API_KEY_LUC, effort max, budget de tâche de 90 000, sortie de 90 000, ligne de 4 USD (GO-2026-11-22-68). **Coût : 1,46 USD** ; 35 896 jetons de sortie, dont 33 215 de réflexion. Un premier lancement avait été refusé par l'outil avant l'envoi (il exige un fichier de remarques), sans coût. Réponse : `docs/notes/collisionneur-v9/essaim-v1/demande-fable-essaim-pilote-v1/reponse-fable-v1/relecture-fable-api.md` (28cc1d81…).
- **Décisions de Fable** :
  1. **Rejouer le jumeau**, en entier, sur la version avec balises, avec les textes neufs (confiance 0,85). Il devient la référence, et les parts du budget apparié se recalculent sur lui.
  2. **Tour III.3** : place « fin », plus une phrase neuve avant la forme imposée, donnée mot pour mot (confiance 0,8 pour la place, 0,6 pour la phrase).
  3. **Finale de l'essaim** : même bloc (phrase neuve et forme imposée) ; finale au « tu » ; ligne « Livrable » réécrite (« objections des revues ») ; ligne de format précisée (« 3 500 mots pour l'ensemble ; la page ne vaut que pour (c) »). Langue, format et marqueur de fin ajoutés à chaque invite de cycle. Cinq remplacements exacts.
  4. **Le temps 0 reste mot pour mot**, lettre comprise (confiance 0,7).
  5. Le pilote ne tient pas la tolérance de coût par modèle : le déclarer, écrire l'écart attendu avant le départ, refixer la tolérance sur les coûts mesurés, avant toute lecture des réponses.
  - Fable relève aussi que les parts citées somment à 12,30, non à 12,29 (arrondi des parts).
- **Fable conclut** : « Le pilote peut partir, à 2 cycles, une fois le jumeau rejoué, les remplacements vérifiés mot pour mot et l'écart de coût par modèle écrit. »
- **Ce qu'il faut ensuite** :
  - (i) deux versions de code, écrites par un Opus et contre-lues : le collisionneur, pour la phrase neuve et la ligne de format du tour III.3 ; l'essaim v7, pour la finale et le format des cycles. Sans dépense.
  - (ii) Le rejeu du jumeau : environ 12 USD réels, pire à calculer, sur une ligne de GO.
  - (iii) Le plafond : rejeu plus pilote font environ 61 USD au pire. Le plafond de 64 USD couvre-t-il les deux, ou le rejeu a-t-il sa propre ligne ?
  - Points que Fable ne tranche pas : le mot « duel » dans le livrable du tour III.1 (c'est bien « en duel H_A contre H_B ») ; « visez un dixième sous chaque limite », qu'elle écrirait « neuf dixièmes de chaque limite ».
