# Consignes de la mère pour le pilote MR-2, procédure v13 (v1)

Écrites le 2026-11-16T01:00:11Z (`date -u`) par la session mère, avant le préavis et l'impression de la commande, d'après la vérification
`verification-differentiel-procedure-pilote-mr2-v74-machine-v13-v1.md` (`9f0bbd0e…`, « jouable sous consignes », K1 à K9). Elles
remplacent pour la v13 les consignes de la v12 (`consignes-mere-pilote-v12-v1.md`, qui restent). Pièces : commit
`2719dcb8320287ebc88cb648175a707a56d37729` de `lot/compte-organisme-v1` (procédure v13 `c90af275…`, outil v3). Dépenses :
GO-2026-11-14-13 et GO-2026-11-14-14 (machine jetable 3 USD), valides jusqu'au 30 novembre. Mots de Lazar : GO-2026-11-15-08
(clés sur la machine jusqu'à 17 heures, au-delà de la fin de l'autonomie ; phrase dans les 30 minutes), écrit pour la v12 et
**tenu par la mère pour valoir pour la v13**, qui ne change ni les clés, ni leur durée, ni la phrase ; R-2949 (la session qui
lance est la mère ou son opérateur).

- **Qui joue.** La session qui lance est la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` et son opérateur ; le dossier
  d'envoi est sur sa machine. Le compte organisme ne lance rien.
- **K1, phrase.** Lazar la tape dans la session mère, jamais relayée par une autre session. S'il n'y est pas joignable dans la
  demi-heure de la demande : nœud ; la machine attend le feu au plus une heure, puis s'arrête d'elle-même (arrêt (A)).
- **K2, autonomie.** Sa fin est le 2026-11-16T08:13Z (GO-2026-11-15-07) ; toute mention de 22:39Z dans la v13 est caduque.
- **N1.** Prix relu au-dessus de 0,17 USD/h : destruction aussitôt, puis nœud.
- **K3, états finaux.** « fini », « arret (A) », « sortie inattendue » : `recuperer` puis destruction aussitôt. « noeud, machine
  gardee » : destruction au mot de la mère, au plus tard à l'échéance plus cinq minutes.
- **C1, après 08:13Z.** La minuterie de la machine agit seule ; la session mère joue la section 11 (destruction par identifiant
  avec `-y`, preuve d'absence) cinq minutes après l'échéance ou dès la fin du pilote, sans attendre aucun mot ; elle ne lance, ne
  relance et ne prolonge rien ; un rappel est posé à cette heure (K7). Si la session mère n'est plus joignable : Lazar, par la
  console du loueur, avec l'identifiant, l'étiquette et l'échéance donnés dans le préavis.
- **K4, fenêtre seule.** Entre l'inventaire d'avant la création et la preuve d'absence, aucune autre création ni destruction chez
  le loueur par une session du programme. La quatrième passe de B bis est finie et sa machine absente (R-2957).
- **K5.** Instance peut-être déjà absente : `verifier-destruction` d'abord, `detruire` seulement si elle est encore listée.
- **K6, horaire.** Le feu du pilote réel est donné avant 08:13Z ; sinon il attend le mot de Lazar. La commande n'est pas
  imprimée après 03:40Z.
- **K8.** Crédit d'au moins 5 USD à l'outil ; une seule machine.
- **C2, K9.** Création sous la seule forme de la section 2, point 7, après l'essai du crochet par l'opérateur (cas sain,
  artefact).
- **Une seule tentative.** Tout arrêt avant le pilote réel demande une version nouvelle.
- **Refus.** Tout refus d'une permission, du crochet ou du classifieur : arrêt, sans reformulation ni contournement ; si la
  machine est louée, elle reste jusqu'au mot de la mère, au plus jusqu'à l'échéance.
