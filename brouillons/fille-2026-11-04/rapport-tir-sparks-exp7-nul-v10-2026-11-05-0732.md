# Rapport de la fille — second tir réel SPARKS-EXP7-NUL, code v10 (2026-11-05, 07:32 UTC)

Ordre de la mère (≈ 07:25 UTC) : tir sous GO-2026-11-05-05 (main 946b6cb7), selon la section 5 de `docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v10.md`, code au commit 3196884f80aae437913acdf677026f7788d507dc.

## Verdict
**Conforme aux attendus.** L'instance a démarré une seule fois (pas de boucle), a refusé de calculer, a attendu 300 s, puis s'est détruite elle-même. Inventaire « absente » à 07:31:03 UTC, sans aucune destruction par la session.

## Déroulé
- Recherche : 4 offres. Rang 1 : offre 34815247, carte 0,057389 USD/h, stockage 0,005479 USD/h. Devis du mode tir : 0,0556 USD.
- Étape 0 : commit de tir b80b91c6872cadb9f6a9462118d002efe9efb99d, branche `essai/sparks-v9-tir-3196884f80aa`, poussée.
- Étape 1 : instance 59227134 créée ; T0 ≈ 07:20:50 UTC. Échéance de la minuterie : 07:45:24.
- Étape 2, journal lu à 07:25:08 par `journal-amorce … 1` (lignes « AMORCE V » seules) :
  - AMORCE V10 DEMARRAGE 1 : 2026-11-05T07:23:42Z, machine 59227134, commit b80b91c6… ;
  - outils absents : curl git : installation bornée (apt-get, 300 s par étape) ;
  - installation (ca-certificates curl git) : code 0 ;
  - outils : curl oui, git oui, unshare oui, chroot oui, prlimit oui, vastai NON ;
  - minuterie lancée (échéance 1793864724, 2026-11-05T07:45:24Z) ;
  - création ;
  - code ou addendum non conformes : aucun calcul : refus avant l'ordre consommé : destruction de l'instance ;
  - attente de 300 s avant la destruction ;
  - résumé du script : `REDEMARRAGES=0 BOUCLE_PRESUMEE=0 DEMARRAGES=1 ATTENDUS=1 BOUCLE=non`.
- Étape 3, inventaire à 07:31:03 : **absente**.
- Étape 7 (repli) : sans objet.

## Dépense
Au plus 10,2 minutes (07:20:50 → 07:31:03) à 0,062868 USD/h (carte + stockage), soit **au plus 0,0107 USD**, sous le devis de 0,0556 USD. Avec le premier tir (≈ 0,0095 USD), l'enveloppe commune de 5 USD a reçu environ 0,020 USD. Chiffres estimés ; le relevé de facturation Vast n'a pas été lu.

## Remarques
1. **Étiquettes « v9 » restées dans le mode tir v10** : l'en-tête imprimé dit « Tir réel v9 », et le nom de branche et le message de commit gardent « v9 ». L'amorce appelée est bien `amorce_instance_sparks_exp7_nul_v10.sh`. C'est cosmétique, mais trompeur pour la traçabilité.
2. **Préfixe ancien dans le journal** : seule la première ligne porte « AMORCE V10 ». Les suivantes portent encore « AMORCE V5 ».
3. **« vastai NON » sur la machine** : l'autodestruction a quand même eu lieu, sans doute par l'interface web de Vast via curl. Je ne l'ai pas vérifié dans le code.
4. **Heure exacte de la destruction non observée** : elle est postérieure à la fin de l'attente (≈ 07:28:45 au plus tôt) et antérieure à 07:31:03.

## Réserves
- Aucune sortie brute de vastai n'est versée. Garde des secrets à 0. Aucune autre instance touchée : les R8 sont laissées à Lazar, sur ordre de la mère.
