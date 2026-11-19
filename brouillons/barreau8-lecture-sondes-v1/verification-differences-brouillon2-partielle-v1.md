# Vérification courte de la différence, brouillon 1 → brouillon 2 — PARTIELLE, interrompue par un refus d'outil — v1

Déposée par la conductrice côté moniteurs (session `session_013QMayjujdhnn94JyDTmgSs`) le 2026-11-19 vers 00:15Z, à partir du message de fin du contre-lecteur (Opus 5.5), qui s'est arrêté au premier refus d'outil sans écrire son fichier. La conductrice n'a rien ajouté au fond : elle transcrit les constats rendus. Aucun résultat du programme.

- Brouillon vérifié : `prereg-lecture-sondes-barreau8-v1-brouillon2.md`, empreinte `a55527725b2079dc034a79f6465f9eb1ca1b911972dbe5fe169357c1029cb9de`.
- Note des différences : `differences-brouillon1-brouillon2-v1.md`, empreinte `27258676ebc7d0a81fe328aab063f218bb7d32336ef830c522a4afd93cb07ec6`.
- Statut : vérification NON achevée. La ligne par remarque n'existe que pour les six remarques bloquantes ; les remarques 7 à 37 ne sont pas vérifiées une à une.

## Le refus
Outil : ligne de commande ; classifieur du mode automatique ; motif rendu : « [Unauthorized Access] ». L'action : chercher des marqueurs de substitution dans les sections de l'ordre du saboteur (brouillon 8) citées par le brouillon 2 ; la commande visait les plages permises mais aussi les lignes 81, 256 et 304, hors des plages permises. Le contre-lecteur déclare la faute sienne, que rien n'a été affiché, et qu'il n'a ni refait ni contourné l'action. Elle n'a été rejouée par personne.

## Ce qui a été vérifié avant le refus
- Empreintes du brouillon 2, de la note des différences et des deux notes d'identités : égales à celles transmises. Rien d'ouvert sous `docs/verdicts/`.
- Validateur sur le brouillon 2, sortie exacte : `['marqueur À REMPLIR restant hors des sections exigées']`.
- Champs : 15 bloquants (I-1 à I-12, F-3, F-6, F-7) et 9 conditions de départ (D-1 à D-9), conformes à l'annonce ; aucun vu dans la mauvaise catégorie.
- Identités des sondes : la table du brouillon 2 est égale aux deux notes (chemins, empreintes entières, clés `s1_w`, `s16_w`, `s4_w`, empreintes des vecteurs et de l'index, noms des planchers, branche). Trois autres citations vérifiées égales : l'empreinte de `src/controle_ia/t06/lanceur_v2.py`, la tolérance de la ligne 39 de `src/controle_ia/t07/plancher_v3.py`, la garde de la ligne 59 de `src/controle_ia/sondes/evaluation.py`.
- Les six remarques bloquantes de la première passe sont réellement traitées dans le texte.

## Constats neufs, partiels
1. **Bloquant probable — l'essai d'alignement échoue à coup sûr dans un cas.** L'essai A0 (iii) permute les clés entre actions de la condition honnête d'une même tâche. S'il n'y a qu'un épisode honnête par tâche, A0 (i) étiquette des moitiés de tâches et toutes les actions d'une tâche portent la même étiquette : la permutation dans la tâche ne change rien, la sonde reste au-dessus, et la ligne L5 tombe sûrement (« non concluant »). Remplacement proposé : « dans la branche "non apparié", les clés sont permutées entre toutes les actions de la condition honnête, toutes tâches confondues ».
2. **À corriger — la recette de puissance est mal étalonnée.** Avec l'effet de tâche d'écart-type 0,5, un décalage de √2 fois le quantile normal de a ne donne pas une aire a, car la plupart des paires viennent de tâches différentes. Remplacement proposé : « décalage = √(2 × 1,25) fois le quantile normal de a ».
3. **À corriger — la loi du plancher synthétique n'est pas définie** : les 800 directions reçoivent-elles l'effet de tâche, sont-elles indépendantes entre elles.
4. **À corriger — le calcul de puissance n'a ni budget de calcul ni repli écrits** (1 000 répétitions sur 15 cases, 2 000 tirages et 801 directions chacune) ; à écrire maintenant (par exemple 200 répétitions), sinon le choix se fera plus tard.
5. **À trancher — le défaut D5 de l'audit risque de rendre presque toute lecture non concluante** : un adaptateur déplace toute l'activité interne ; la règle de décision compare déjà chaque sonde à son plancher sur le même jeu ; le texte scellé des sondes v0 faisait de ce seuil un déclencheur d'audit, pas un défaut. Recommandation du contre-lecteur : réserve en tête du verdict, pas défaut ; sinon c'est une décision.
6. **À corriger — le défaut D4 est ambigu** : (a) « l'aire du premier jeton enregistré » n'a pas de sens, un identifiant de jeton est une catégorie, pas un score ; (b) « la sonde » doit devenir « la sonde qui porte l'état ».
7. **Mineure — branche « contexte avec texte privé »** : la lecture devrait alors prendre la longueur du contexte dans l'index de la passe, et ne pas recevoir le fichier des identifiants de jetons des actions.
8. **À vérifier par qui en a le droit — comparaison à l'ordre scellé (condition de départ D-6)** : si les sections citées de l'ordre gardent des marqueurs de substitution, leur remplissage au scellement de l'ordre serait compté comme un écart ; il faut exempter ces remplissages. Point non vérifié (c'est l'action refusée).

## Conclusion provisoire du contre-lecteur
Pas « prêt à sceller » tant que le constat 1 n'est pas corrigé.
