# Témoin de Bailey — nouvelle série : échec de l'envoi de l'archive avant l'amorce ; réponse de Luke Bailey sur la licence — 12 novembre 2026, 20:40 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`. Ne se réécrit pas (R12).

## Run
- Conduite v8 (addendum 3, code `91238a73`) sur le poste Hetzner v8 (175880281) : offre 59306789 (Caroline du Nord) ;
  instance 60400450 créée à 20:10:16Z, c = 1,5040 USD/h, prête à 20:11:43Z.
- Envoi de l'archive du code (`scp` vers l'instance) : `CalledProcessError`, code 255. La conduite a levé, transféré ce
  qui existait, détruit l'instance (`detruite: true`). Fin de la conduite : 20:20:40Z. Poste détruit à 20:36Z.
- **Rien n'a tourné** : ni amorce, ni mise en place, ni pilote. Aucune donnée. Ce n'est pas une chute du pilote : la
  nouvelle série de l'addendum 3 **n'est pas consommée** ; le texte permet de refaire la mise en place (liste d'arrêt,
  « La mise en place peut être refaite si aucune ligne de ce texte n'est touchée »).
- Cause probable : hôte (même image et même envoi réussis sur l'hôte 59858182 à 15:03Z). Réserve : `FournisseurVast.
  envoyer_fichier` ne refait pas un `scp` en échec (aucune nouvelle tentative), contrairement aux sondages.
- D du poste : 2,033 USD (cinq instances, toutes détruites).
- Relance : sur le mot de Lazar.

## Licence du code public (condition 4 ; GO-2026-11-11-01)
Réponse de Luke Bailey (premier auteur) au courriel de Lazar du 10 novembre 2026 (« License for the obfuscated-activations
repository »), transmise par Lazar le 12 novembre, verbatim : « Hi! Feel free to use the code however you like 🙂. All the
best, Luke ». Elle lève par écrit le risque de propriété intellectuelle que `GO-2026-11-11-01` avait accepté (« auteurs
contactés, sans réponse »). Ce qu'elle ne dit pas expressément : les fichiers `harmful_dataset` du dépôt (le courriel les
nommait). À inscrire sur `main` par la mère (registre des décisions ; mention à côté de `GO-2026-11-11-01`).
