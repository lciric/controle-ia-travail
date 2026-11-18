# Contre-lecture des gabarits de clôture v4 — témoin de Bailey (addendum 7, § 3)

Fichiers lus : `docs/notes/reproduction-attaque-publiee-v1/gabarits-cloture-v4/` (cinq fichiers, versés sans modification
depuis l'exemplaire contre-lu, compagnons `.sha256`). Contre-lecture R2 par un sous-agent neuf (exécution de flux
`wf_83f57e7e-8f3`), après la ronde sur la v3 corrigée (`wf_c00aece0-baa`, « prêt après corrections » : deux constats
à corriger, quatre remarques ; publiée en v4 au nom de R12).

**Verdict : prêt.** Les six changements demandés sont en place, justes, sans défaut de fond. Ils ont été joués dans
un faux dépôt sous /tmp, supprimé ensuite. Essais du vérificateur : 6 réussis. `bash -n` passe.

Remarques de forme, gardées pour une v5 éventuelle avant la clôture (sans effet sur la cloison) :
1. Historique des en-têtes du vérificateur et de son essai mal réécrit par le renommage (« v3 : renommé …_v4 »).
2. e8, l. 600-601 : le commentaire et le message disent encore « la première ligne fait foi », alors que la première
   ligne est désormais « lancé » ; le comportement est juste.
3. Voie de repli de e6-pousser (branche `cloture-bailey-v1`) : les lignes e8 ne peuvent être poussées par le script ;
   à écrire au § 9 de la note (commit du seul journal, poussé vers `cloture-bailey-v1`, consigné). Point antérieur à la v4.
4. e3 : refuser aussi quand seul le compagnon de l'attendu existe ; ligne e2 : espace en trop quand le vérificateur
   rend du texte ; caches d'essais supprimés avant le versement (fait).
