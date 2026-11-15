# Consignes de la mère pour le pilote MR-2, procédure v12 (v1)

Écrites le 2026-11-15T23:56:52Z (`date -u`) par la session mère, avant l'impression de la commande de création, d'après la vérification
`verification-differentiel-procedure-pilote-mr2-v74-machine-v12-v1.md` (`bcdfe138…`, « jouable après corrections », § 10) et le
mot de Lazar GO-2026-11-15-08. Pièces de la v12 : commit `85a84ff5daf3c6df4bc0e13c2444eeb51b8d05db` de `lot/compte-organisme-v1`.
Dépenses : GO-2026-11-14-13 (part sur crédits de Claude, 20 USD) et GO-2026-11-14-14 (part hors crédits, 21,72 USD, dont la
machine jetable 3 USD), valides jusqu'au 30 novembre.

- **N1 (argent).** Après la création, si le prix imprimé par `relire` dépasse **0,17 USD/h** : détruire aussitôt (section 11),
  puis nœud écrit à la mère. La borne de 0,20 USD/h du texte de la v12 ne s'applique pas.
- **C1 (clés et acteur à l'échéance).** Lecture de M5, accordée par Lazar : les clés du pilote restent dans la configuration de
  la machine louée de la création à la destruction, au plus 17 heures, y compris après la fin de l'autonomie
  (2026-11-16T08:13Z). Après cette heure : la minuterie de la machine agit seule ; la session du compte organisme joue la
  section 11 (destruction par identifiant avec `-y`, preuve d'absence) cinq minutes après l'échéance, ou dès la fin du pilote,
  **sans attendre aucun mot** (un arrêt de sa propre machine est toujours permis, R10) ; elle ne lance, ne relance et ne
  prolonge rien ; toute autre décision attend Lazar. Si cette session n'est plus joignable, la mère joue la destruction par
  l'identifiant consigné ; à défaut, Lazar par la console du loueur.
- **C2 (forme de la création).** La création n'est jouée que sous la forme exacte de la section 2, point 7, après l'essai du
  crochet sur un cas sain et sur un artefact.
- **Autres consignes de la vérification, reprises.** n1 : lire « échéance dans les 17 h 05 » ; n6 : instance déjà absente,
  preuve par le témoin de la création ; n7 : aucune autre session du programme ne crée ni ne détruit de machine Vast pendant le
  pilote (la mère s'y engage pour ses propres travaux jusqu'à la preuve d'absence) ; n11 : pas de seconde tentative sans version
  nouvelle ; n3 : remplacement des clés proposé à Lazar après le pilote.
- **Phrase.** Lazar la donne dans les 30 minutes du lancement, dans la session du compte organisme.
- **Rapport.** Identifiant de l'instance, prix relu, échéance, puis chaque arrêt et la preuve d'absence, envoyés à la mère au fil
  de l'eau pour `registres/arrets.md` et `registres/depenses.md`.
