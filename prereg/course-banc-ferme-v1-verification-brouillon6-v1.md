# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 6 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon6.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `41925ac54362d1468c01b89b426e9bd9f408981b`. Empreinte recalculée : `b23b4b3bcfc9fa903ca13a07a38aae3c6f0e1347474bf7968d96a4249a8f9fbc`, égale à son `.sha256` compagnon. Les brouillons 1 à 5 sont inchangés.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 19:10 UTC. Refus d'un classifieur : aucun.
- **Objet** : les seules différences avec le brouillon 5, accepté, établies par `diff` ligne à ligne et lues en entier. Un regard dur porte sur les cinq points que l'auteur désigne.
- **Sources des différences, lues et recalculées** :

| Source | Où | Empreinte |
|---|---|---|
| note du mot de Lazar sur le nœud 10 : « (a) une réserve écrite, et la course peut partir sans attendre » | branche `claude/loving-lamport-7ol5ws` | `43a9766d…`, égale |
| `registres/go.md`, lignes 675 (GO-2026-11-21-76) et 676 (GO-2026-11-21-77) seules | `main`, commit `c40eee73` | `19da46e1…`, égale |
| `registres/decisions.md`, ligne R-4668 seule | `main`, commit `c40eee73` | — |
| contre-lecture des trois choix du banc fermé, par Fable | `main` | `bc9ec0fd…`, égale |

  La contre-lecture des trois choix a été lue par recherche sur ses sections 1.2, 2, 3 et 5. Elle ne contient aucun contenu de famille. **L'index v2 n'a pas été lu**, puisqu'une de ses réserves parlerait du contenu.
- **Validateur** : il ne rend que le marqueur du champ n° 19, ce qui est attendu.

## Les cinq points désignés

**1. D6, « Où est l'écart ».** **Accepté.**
- La parenthèse « écart à N-060 v3 point 1 » de GO-2026-11-21-75 est une lecture inscrite par la mère, et non un mot de Lazar : le mot de Lazar est « go ». La mère peut donc la corriger par erratum (R-4668), et le texte le dit comme un erratum de la mère, ce qui est juste.
- Des lecteurs de deux familles hors de celles des moniteurs, aveugles à la condition, c'est bien ce que demande N-060 v3. L'écart réel est l'envoi avant la revue externe, et il est bien rattaché à GO-2026-11-21-76 et à la seule pièce de sécurité v8.
- L'exclusion des lignées de l'agent et des moniteurs évalués, celle de Mistral et le lecteur Claude par appel de programme seulement vont dans le sens de N-060 v3.

**2. D1, l'ordre inversé.** **Accepté sur le fond**, avec une précision (M1).
- GO-2026-11-21-77 nomme l'objet « la configuration de génération du calage de G1 », scellée avant la course, écrite par un Fable de la mère, et dit que les champs 1 et 2 y renvoient. Le texte l'appelle « configuration de génération de l'agent » et dit que le calage la copiera. C'est le même objet, au même rang : scellé avant la course, joué tel quel par la course, imposé au calage de G1.
- **La vérification de concordance tient sous cet ordre.** Elle compare deux postes qui jouent une même configuration scellée : le banc, et le poste de calage du champ n° 19. Elle ne suppose aucun épisode de calage existant. La tolérance et le quantile sont maintenant dans la configuration, et le verdict ne dépend que d'elle.
- La réserve, décidée par Lazar (« (a) une réserve écrite »), est rendue fidèlement, avec ta recommandation contraire.
- La garantie reste conditionnelle à ce que fera G1, et la réserve le dit.

**3. Le second juge retiré, le juge limité au second temps.** **Accepté sur le fond**, avec une précision de source (M2).
- La règle du bras ne fait exister le second juge que pour l'accord sur les classes de faille (« Classes de faille », « Accord »), et aucune classe n'est attribuée ici. Retirer un lecteur réduit l'exposition du coffre.
- GO-2026-11-21-75 n'a tranché que les lecteurs du dommage, et non l'existence d'un second juge : rien de décidé par Lazar n'est défait.
- Mais une table des « nœuds tranchés » appelle une autorité. Ici, c'est un choix de conception de l'auteur, éclairé par la contre-lecture des trois choix. Ce n'est pas une décision de la session qui t'a lancé, qui n'a pas d'autorité sur le fond du texte.

**4. Dépôt daté chez un tiers.** **Accepté**, avec une précision d'ordre (M3).
- Le texte porte des empreintes seules : index v1, index v2 et les quatre pièces de la famille. Il ne porte aucun contenu, et tu n'as pas lu l'index v2.
- « Daté, non opposable » tant que le projet est privé et non gelé : c'est juste.
- La garde 10 sur l'identifiant, la date et l'empreinte relue est bonne.

**5. Nœuds 12 et 13.** **Bien posés.** Une précision sur le nœud 12 (M4).

## Autres différences

Elles sont conformes :
- **D2** : la dixième question de l'attestation porte sur des épreuves de l'oracle qui demanderaient des épisodes de l'agent. Elle est juste, et la règle « génération unique » est préservée.
- **D5** : l'opérateur est lancé par la mère seule et ne détient aucune clé ; le relais d'arrêt suit la règle R10.
- **D7, poste d'envoi** : il est distinct du poste de transit, et ce dernier ne porte aucune clé.
- **Épreuves de l'oracle** : elles sont passées avec les mêmes lecteurs, les mêmes versions et les mêmes réglages.
- **Conditions de lancement** : elles sont renumérotées de 1 à 15, la v8 en condition 6, et le renvoi « condition 8 » vers la pièce du vérificateur est juste. La remarque de forme de la contre-lecture 5 est faite.
- **Liste d'arrêt** : cinq lignes neuves ; la ligne « nœud 10 non tranché » est retirée à bon droit, puisqu'il est tranché.
- **Seuil** : le minimum de paires est réglé sur les modes connus, sans toucher la famille.
- **Réserves 13 et 14** : elles sont honnêtes.

Aucun contenu de mode, de recette ni de paramètre.

## Restes mineurs

**M1 — Nommer GO-2026-11-21-77 par son identifiant.** Le repère « [GO76] » couvre deux lignes, et D1 cite « [GO76], l. 676 » pour un mot qui est GO-2026-11-21-77. Donner son propre repère à GO-2026-11-21-77. Dire en une phrase que la « configuration de génération de l'agent » est l'objet que GO-2026-11-21-77 appelle « configuration du calage de G1 ».

**M2 — L'autorité du retrait du second juge.** Dans la table des nœuds tranchés, écrire, à la ligne « second juge » : « choix de conception de l'auteur, sur la réserve de la contre-lecture des trois choix ». Ne pas écrire « à la demande de la session qui a lancé l'auteur ». Le dire à Lazar dans le message de scellement, puisque la proposition d'origine (un second juge Opus) lui avait été soumise.

**M3 — Ce qui porte l'empreinte de l'oracle dans le dépôt.** Le texte veut que le même dépôt porte l'empreinte de l'oracle figé. Or cette empreinte n'est écrite qu'à l'addendum B (condition 12), qui suit le dépôt (condition 11) et porte son identifiant. Le dépôt ne peut donc pas la prendre dans l'addendum B. Nommer la pièce, sous un dossier que le programme de dépôt lit, qui porte l'empreinte de l'oracle figé et est scellée avant le dépôt. Par exemple, une note sous `docs/decisions/`, comme le texte le propose déjà pour l'index.

**M4 — Nœud 12 et champ n° 15.** Le nœud 12 dit que la répétition générale fixerait le nombre minimal de paires sur une mesure. Mais le champ n° 15 est à l'addendum A, scellé avant la construction des gardes, alors que la répétition générale demande les gardes construites. Sous l'option (a), dire que le champ n° 15 passe à un addendum scellé après la répétition générale et avant l'assemblage du lot.

## Verdict

**Accepté.** Les différences du brouillon 6 sont fidèles à leurs sources. Les cinq points désignés tiennent. Quatre restes mineurs, M1 à M4, sont à porter à la version qui citera la pièce de sécurité v8. Je les vérifierai avec les seules différences de cette version.

Le scellement définitif attend encore :
- la v8 acceptée ;
- les identifiants de GO des mots du nœud 10 ;
- les champs ouverts remplis ;
- les nœuds 8, 12 et 13 ;
- le mot de Lazar.
