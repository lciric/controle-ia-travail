# Rapport de la fille — quatrième tir SPARKS-EXP7-NUL, code v11, jouet sur machine réelle (2026-11-05, 08:26 UTC)

Ordre de la mère (≈ 08:09 UTC, R-1547) : code v11 tel quel (cabc06e5d7e1c62c519990ed9709103c23cb08ec), sous GO-2026-11-05-05, avec la commande `tir … 30 1`. Un seul écart de pilotage était ordonné : les inventaires du verdict ne se prennent qu'après la ligne « ARRÊT OBTENU ».

## Verdict
**Conforme sur toute la chaîne.**
1. Fabrication factice, puis ARRÊT OBTENU.
2. Trois inventaires « exited/stopped » et verdict du script **« arretee »**.
3. Ordre « fin » poussé, puis `start`.
4. Second démarrage : ordre accepté, attente de 180 s, puis **autodestruction**. Inventaire « absente » à 08:24:21 UTC.

Il n'y a eu aucune destruction par la session.

## Écarts (déclarés)
1. **Ordonné par la mère** : les trois inventaires du verdict n'ont été pris qu'après « ARRÊT OBTENU », le premier 50 s après cette ligne.
2. **De mon fait** : l'étape 0 imprimée recrée la branche `essai/sparks-v11-tir-cabc06e5d7e1`, déjà poussée au troisième tir (commit 934e4824…). Je n'ai ni écrasé ni renommé cette branche. J'ai **réutilisé ce commit de tir** (même code, même registre des GO, même addendum factice df657d0a…) comme COMMIT de l'instance.
   - L'offre, les prix et l'échéance sont ceux imprimés par ce quatrième mode tir.
   - La branche des ordres `ordres/sparks-exp7-nul-v5-934e4824a36d` n'existait pas avant ce tir.

## Déroulé
- Offre 52708520 (rang 1) : carte 0,054722 USD/h, stockage 0,005479 USD/h. Devis : 0,0584 USD.
- Instance 59232437 créée ; T0 ≈ 08:08:20 UTC. Échéance de la minuterie : 08:37:56.
- Journal 1 (lu à 08:13:29), « AMORCE V10 DEMARRAGE 1 » à 08:11:43 :
  - installation (ca-certificates, curl, git) : code 0 ;
  - minuterie lancée ;
  - « mode jouet : addendum non exigé » ;
  - fabrication factice de 60 s, fin à 08:13:08 (code 0) ;
  - **« ARRÊT OBTENU (état voulu « stopped », HTTP 200) » à 08:13:09** ;
  - résumé du script : **DEMARRAGES=1**, ATTENDUS=1, BOUCLE=non.
- Inventaires du verdict :
  - 08:13:59 : exited (cur_state **stopped**) ;
  - 08:17:01 : exited (cur_state **stopped**) ;
  - 08:20:02 : exited (cur_state **stopped**) ;
  - verdict du script (`boucle 59232437`) : **arretee**.
- Étape 4 : ordre `{"numero": 1, "instance": "59232437", "phase": "fin", "deja_usd": 0}` poussé sur `ordres/sparks-exp7-nul-v5-934e4824a36d` (28fbd7a0…). Un avertissement de négociation git est apparu (« expected 'acknowledgments' »), mais le push a abouti : la branche est présente.
- Étape 5 : `start` envoyé à 08:20:33 (« starting instance 59232437. » lu).
- Étape 6, journal 2 (lu à 08:21:18), « AMORCE V10 DEMARRAGE 2 » à 08:20:35 :
  - « redémarrage consigné au registre des démarrages : démarrage n° 2 » ;
  - « ordre 1 (fin) accepté et consigné » ;
  - « attente de 180 s avant la destruction » ;
  - résumé du script : **DEMARRAGES=2**, ATTENDUS=2, BOUCLE=non (REDEMARRAGES=2).
- Étape 7, inventaires :
  - 08:22:18 : running ;
  - 08:23:20 : running ;
  - 08:24:21 : **absente**.

## Dépense
Au plus environ 16 min (08:08:20 → 08:24:21) à 0,0644 USD/h (carte + stockage), soit **au plus 0,0172 USD**. C'est moins en réalité : de 08:13:09 à 08:20:33, l'instance était arrêtée et seul le stockage était facturé. Cumul des quatre tirs : environ 0,050 USD sur l'enveloppe de 5 USD. Relevé de facturation Vast non lu.

## Remarques
- Le texte imprimé par le mode tir v11 annonce « Troisième tir (v11) » quel que soit le tir.
- Le journal porte encore le préfixe « AMORCE V5 » après la première ligne.
- La machine indique « vastai NON » : l'arrêt et la destruction passent sans doute par l'interface web de Vast via curl. Le « HTTP 200 » de l'arrêt va dans ce sens.
- Aucune sortie brute de vastai n'est versée. Garde des secrets à 0. Les R8 n'ont pas été touchées.
