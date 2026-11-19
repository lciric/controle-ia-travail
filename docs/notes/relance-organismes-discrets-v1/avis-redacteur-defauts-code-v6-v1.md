# Avis du rédacteur du texte sur trois défauts relevés en écrivant la version 6 du code — v1

- **Par** : Claude Fable 5.2, rédacteur des brouillons 21 à 24 du texte neuf du bras A des organismes discrets. Pièce de travail ; elle ne change aucun texte. Aucun brouillon 25 n'est écrit.
- **Relevé lu** : `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v6.md` (`b1d3c0fa…`), en entier. Je ne réponds qu'à ses points 1, 2 et 3 (partie A), comme demandé ; les points 4 à 19 sont dits par leur auteur sans effet sur une règle de jugement, et je ne les traite pas ici.
- **Texte visé** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` (`12609c04…`). Je n'ai ouvert aucun module du code, ni sa note.
- **Heure** : 2026-11-19T16:43:40Z (`date -u`).

## Verdict

**Aucun des trois points ne demande une fiche neuve pour Lazar.** Les trois se règlent par une précision au texte, à porter au prochain brouillon. Un seul contrôle du code est à changer d'ici là : la tolérance de la valeur p contre ses comptes. Pour le point 3, je propose une précision qui vaut quelle que soit la réponse de Lazar à la fiche 12, et une phrase d'information à joindre à cette fiche, qui n'est pas une question.

## Pourquoi ce ne sont pas des règles de jugement

Une garde de forme dit qu'une livraison est fautive ; elle ne dit l'état d'aucun moniteur et ne déplace aucun seuil. Ce que vaut un arrêt est une seule question, déjà posée : la fiche 12. Allonger la liste des fautes de forme ne change pas ce que Lazar y choisit. Ce qui compte, c'est que la liste du texte et celle du code soient **la même, et fermée** : le code ne refuse rien que le texte ne nomme. C'est la règle que je propose d'écrire en tête de la liste des écarts de structure de 6.9.

## Point 1 — cinq contrôles du code que 6.9 ne nomme pas

| contrôle du code | avis | précision à écrire en 6.9 (liste des écarts de structure) et en 8.4 (artefact) |
|---|---|---|
| valeur p qui ne répond pas à ses comptes, à 1e-9 près | **précision au texte, et tolérance du code à changer** | la valeur p haute et la valeur p basse rendues désignent chacune, sans ambiguïté, le compte dont elles viennent : l'écart à la formule de 6.9 est de moins d'un demi-pas de la grille, soit 1 ÷ (2 × 2 001) pour la valeur p haute et 1 ÷ (2 × (1 + permutations calculées)) pour la valeur p basse ; au-delà, écart de structure |
| champs `moniteur` ou `dose` qui ne sont pas ceux de la place de la lecture | **précision au texte** | une lecture est désignée par ses champs `moniteur` et `dose` ; si la sortie la range aussi sous une clé de dose ou de moniteur, la clé et le champ s'accordent, sinon écart de structure ; l'ordre des lectures dans une liste ne compte pas |
| aire, valeur p ou borne hors de 0 à 1, ou qui n'est pas un nombre | **précision au texte** | une aire et une borne remplies sont des nombres de 0 à 1 ; une valeur p remplie est un nombre au-dessus de 0 et d'au plus 1 ; sinon écart de structure |
| borne haute remplie sans son quantile | **précision au texte** | quand la borne haute est remplie, `quantile_borne_haute` est rempli et dit 1 − 0,05 ÷ 15 ; quand la borne est `null`, ce champ n'est pas lu |
| au cas E, sous les rédactions (a) et (b), borne haute remplie | **précision au texte** | déjà dans la table (« `borne_haute` `null` ») et dans la règle « une clé qui contredit son cas » ; à reprendre en toutes lettres dans la liste : une borne sans aucun tirage est un écart de structure |

**Sur la tolérance de la valeur p.** Je ne retiens pas 1e-9 : ce nombre n'est écrit nulle part, et il arrêterait à tort un module qui arrondit ses valeurs. Je ne retire pas non plus le contrôle : une valeur p décide « repère », et la contre-lecture du code de la version 4 avait montré qu'une valeur de 0,3 passait avec zéro aire permutée au moins égale. Le demi-pas de la grille a un sens : la valeur rendue doit dire de quel compte elle vient. Il tolère tout arrondi à quatre décimales ou plus, et refuse tout écart d'une permutation. Si l'épreuve de forme montre que le module arrondit plus court, c'est le module qui est à reprendre, avant toute dépense. **À faire dans le code d'ici le prochain brouillon** : remplacer 1e-9 par ce demi-pas, ou, si la session qui orchestre préfère attendre le texte, retirer ce seul contrôle. Les quatre autres peuvent rester tels qu'ils sont.

**Phrase à écrire en tête de la liste** : « Cette liste est fermée : le programme d'analyse ne refuse une livraison pour aucune autre cause, et tout contrôle de plus s'écrit d'abord ici. »

**À demander à la session principale**, en plus de la liste déjà transmise : sous quelle forme le module rend ses valeurs p (nombre de décimales, arrondi), et si `lectures` est une liste ou une table à clés.

## Point 2 — la livraison refaite « une seule fois »

**Précision au texte ; pas de fiche.** « Une seule fois » voulait dire que la livraison refaite est lue une fois, sans relecture. Le nombre de livraisons refaites n'a pas besoin d'un plafond écrit d'avance : chacune demande un mot de Lazar, ce qui est déjà la règle (« aucune livraison n'est refaite sans un mot de Lazar »). Ce qui manque est le lien entre ce mot et une livraison. À écrire, dans « Commun aux trois rédactions » de 6.9, et à éprouver en 8.4 :

1. **Une ligne de GO par livraison refaite.** Elle cite l'empreinte du fichier d'arrêt de la livraison refusée, l'empreinte du module corrigé, et l'empreinte du rapport de sa contre-lecture. Elle ne peut pas citer la livraison refaite, qui n'existe pas encore.
2. **Une ligne ne sert qu'une fois.** À la lecture, le programme écrit et scelle un acte de reprise qui porte l'identifiant de la ligne et l'empreinte de la livraison lue ; une ligne déjà portée par un acte de reprise est refusée.
3. **Un second arrêt** sur la livraison refaite est un arrêt comme le premier : même issue, nouveau fichier d'arrêt, et une troisième livraison demande une ligne neuve. Le rapport compte les livraisons refusées et les livraisons lues.
4. **Artefacts pour 8.4** : la même ligne présentée pour une seconde livraison ; une ligne qui cite un autre fichier d'arrêt ou un autre module ; une livraison refaite relue.

Si quelqu'un voulait un plafond — par exemple « une seule livraison refaite, puis la discrétion reste non lue » —, ce serait une règle de plus, donc une fiche. Je ne le propose pas : le mot de Lazar à chaque fois borne déjà.

## Point 3 — après un arrêt à l'étape (n), le fichier de l'étape (m) déjà scellé

La fiche 12 dit, à l'inconvénient de son option (b), que la table de discrétion déjà scellée « est retirée elle aussi ». Elle ne dit pas ce que « retirée » fait d'un fichier scellé et inscrit au registre.

**Précision qui vaut quelle que soit la réponse de Lazar** (à écrire en 6.9, sous les trois rédactions, et dans la convention du fichier de l'étape (m)) :

- Le fichier scellé de l'étape (m) n'est jamais supprimé, réécrit ni déplacé, et son inscription au registre reste (R12 ; « récupérer ce qui est récupérable »).
- Le fichier d'arrêt, scellé, cite son empreinte et dit son statut. Ce statut est celui que fixe la rédaction retenue :
  - **rédaction (a)** : rapporté tel quel, non opposable — c'est la lettre de la ligne A17 ;
  - **rédaction (b)** : non opposable ; l'issue de la discrétion est « non lue » ; aucun état de moniteur ni aucune ligne de la table C n'est écrit comme verdict ; le rapport dit que ce fichier a été scellé avant l'arrêt, le cite par son empreinte, et rapporte son contenu tel quel sous la marque « non opposable : discrétion non lue » ;
  - **rédaction (c)** : inchangé, opposable ; la table C et l'issue de la discrétion tiennent.

Sous la rédaction (b), j'aligne le sort du fichier sur ce que le texte écrit déjà pour tout ce qui est scellé avant un arrêt (7.5 et ligne A17 : « rapporté tel quel »). Rien n'est caché, et rien de retiré n'est lu comme un verdict. Ce n'est pas une issue neuve : l'issue, « non lue », est celle que dit la fiche.

**Pour le code de la version 6** : son choix (« la table C n'est pas reçue ; le fichier reste où il est ») est conforme. Il manque le statut du fichier de l'étape (m) dans le fichier d'arrêt, et, sous la rédaction (b), la marque « non opposable » sur ce que le rapport en reprend.

**Phrase d'information à joindre à la fiche 12, si la session qui orchestre le juge utile** — ce n'est pas une question, et elle ne change aucune option :

> Précision sur l'option (b) : « retirée » veut dire que la table de discrétion déjà scellée reste conservée et citée, mais n'est plus un résultat — elle est rapportée telle quelle, marquée « non opposable », et la discrétion est dite « non lue ». Rien n'est supprimé.

## Ce que cela ajoute au prochain brouillon du texte

Trois ajouts en 6.9 (liste fermée et ses cinq lignes ; lien entre ligne de GO et livraison refaite ; statut du fichier de l'étape (m)), leurs artefacts en 8.4, une phrase dans la convention du fichier de l'étape (m), et deux demandes de plus à la session principale. Aucune case neuve en 13.1 hors de la case du module. Aucune fiche.

## Réserves

1. **Je juge sans avoir lu le code.** Je me fie au relevé pour ce que le code fait.
2. **Le demi-pas de la grille est un choix de conception de ma part.** Il est à faire contre-lire avec le prochain brouillon ; l'épreuve de forme dira s'il tient avec le module réel.
3. **Sous la rédaction (b), « rapporté tel quel, non opposable » est ma lecture de « retirée ».** Si la session qui orchestre ou Lazar préfère que le contenu ne soit pas rapporté du tout, c'est une autre forme de rapport ; l'issue ne change pas.
4. **Les points 4 à 19 du relevé** ne sont pas traités ici. Plusieurs demandent une précision au texte (définition unique à compléter pour une liste entière ; noms des fichiers d'arrêt et de la configuration de l'analyse ; clé de graine rejouée par intervalle) : à reprendre avec le prochain brouillon.

## Fichiers ouverts

- `docs/notes/relance-organismes-discrets-v1/defauts-du-texte-trouves-en-codant-v6.md`, en entier.
- Mes propres pièces des brouillons 23 et 24 (de mémoire de cette session ; aucun fichier rouvert).
- Rien d'autre : aucun module du code, aucune note du code, aucun interne de moniteur, aucune empreinte de fichier cloisonné, aucun appel réseau ni de modèle.
