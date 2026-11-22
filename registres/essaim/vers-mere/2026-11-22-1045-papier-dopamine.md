# Papier « dopamine », étape 1 exploratoire — devis en compte rendu à la mère (2026-11-22T10:45Z, `date -u`)

**EXPLORATOIRE, non opposable** (GO-2026-11-21-44). Session fille du papier « dopamine », branche `claude/papier-dopamine-etape-1-v1`. Classe C. Aucune dépense faite, aucune machine créée.

## Verdict
Prêt à partir : machine louée, une carte A100 SXM4 de 80 Go chez Vast.ai, **attendu 4,2 à 4,5 USD et 3,4 h** (noyau seul : 2,1 à 2,4 USD, 1,6 h), **pire cas payable 8,1 à 8,5 USD** à l'offre retenue (9,65 USD au prix haut du devis), plafond 10 USD, destruction par minuterie à 6 h 30. Deux points bloquants à trancher par la mère avant la ligne de GO (ci-dessous, points 1 et 2).

## Devis
- Devis de référence inchangé : `prereg/papier-dopamine-moniteur-v1/exploratoire/devis-etape-1-rejeu-math500-exploratoire-v1.md` (33b558144c4757cc…), conception de Fable ; ligne déjà accordée GO-2026-11-21-48 (10 USD, échéance 2026-11-24).
- Relevé neuf à 10:40Z : `docs/notes/papier-dopamine-moniteur-v1/exploratoire/releve-offres-a100-80go-2026-11-22T1040Z-v1.json` (b3c766910bd33fe3…), 5 offres vérifiées, 3 dans les bornes du lanceur (carte ≤ 1,30, stockage ≤ 0,08 USD/h, 90 Go, 12 cœurs, 64 Go, CUDA ≥ 13) :
  - 29019282, Tchéquie, 1,122 USD/h, fiabilité 0,975 ;
  - **34475479, Tchéquie, 1,188 USD/h, fiabilité 0,983, descente 0,003 USD/Go — recommandée** (réseau presque gratuit, meilleure fiabilité que la moins chère) ;
  - 36695156, Montana, 1,255 USD/h, fiabilité 0,999.
- Durées (supposées par le devis, mesurées par la tranche de 32 questions) : mise en place 0,35 h, génération 0,26 h, sondes 2,4 h ; plus aucun lancement à 5 h 30 ; arrêt de la tranche à environ 0,5 USD si les réponses sont trop longues.
- Relecture forcée (étape 2a) **non lancée** dans cette course : aucun fichier de contextes (R-4571, condition C-2 à Lazar).

## Points à trancher par la mère
1. **Crédit du loueur** : 26,06 USD au relevé. Deux autres instances tournent (étalonnage du saboteur 61875617, 1,19 USD/h ; lentilles 61932710, 2,39 USD/h) : avec la mienne, environ 4,8 USD/h, crédit épuisé vers 5 h 30 sans recharge, ce qui arrêterait **toutes** les instances du compte. Condition 5 du devis (« aucune recharge supposée ») non tenue tant que les deux autres tournent au-delà de 2 à 3 h. Recommandation : recharge confirmée par Lazar, ou départ seulement quand l'une des deux s'arrête.
2. **Branche de versement** : l'amorce pousse depuis la machine sur `donnees/dopamine-exploratoire-v1` (amorce, l. 30), pas sur ma branche. Mon mandat : « tu ne pousses que sur ta branche ». Options : (a) la mère autorise `donnees/dopamine-exploratoire-v1` pour la machine (aucun code changé ; recommandé) ; (b) je change la branche de l'amorce vers la mienne (code à recontre-lire, essais à rejouer).
3. Commit de lancement : la tête de ma branche une fois ce compte rendu poussé (porte le paquet fusionné, 126 essais verts rejoués ici à 10:38Z).

## Ligne de GO proposée (numéro par la mère)
`| GO-2026-11-22-NN | 2026-11-22 | calcul | Papier « dopamine », étape 1 exploratoire, sous le devis 33b55814… et GO-2026-11-21-48 : une instance A100 SXM4 80 Go, offre 34475479 (ou une offre du relevé neuf b3c76691… dans les bornes), au plus 1,30 USD/h carte et 0,08 USD/h stockage, attendu 4,2 USD, pire 9,65 USD ; tranche de 32 questions avec règle d'arrêt ; plus aucun lancement à 5 h 30 ; destruction par minuterie à 6 h 30 ; versement par la machine sur donnees/dopamine-exploratoire-v1 ; relecture forcée exclue. Sorties « exploratoire », sans verdict ni porte. | 10 USD | 2026-11-24 | Lazar | GO-2026-11-22-40 (« papier dopamine, étape 1 : go ») |`

## Réserves (une ligne chacune)
- Routine : empreintes du lancement OK ; `verifier-arbre` rend 39 problèmes préexistants (compagnons absents ou mal nommés, hors de ce bras) ; suite complète non relancée (rejeu des échecs R-4640 fait foi), essais du bras 126/126.
- Inventaire : aucune instance ni serveur à moi ; serveur Hetzner 177170935 « essai-3-palier-0b » en marche, pas à moi, non touché ; instances Vast 58936096, -099, -100, 60988826 arrêtées, non touchées.
- Le client du loueur ignore le paquet d'autorités du mandataire : certifi de l'environnement local remplacé (original gardé à côté), jamais `--insecure`.

## Prochaine action
Attendre la ligne de GO de la mère et sa réponse aux points 1 et 2 ; puis relevé neuf, ligne d'engagement au registre des dépenses, commande par le lanceur, création, suivi, destruction par identifiant, versement scellé.
