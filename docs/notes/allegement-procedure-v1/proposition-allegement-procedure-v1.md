# Alléger la procédure sans rien perdre en rigueur — proposition v1

- **Écrit par** : la session mère, le 2026-11-19T09:37:14Z (`date -u`), à la demande de Lazar (« ouiii go », vers 09:45Z).
- **Source** : ce que la mère a observé dans la seule matinée du 19 novembre (R-3655 à R-3697). Les compteurs cités sont relevés sur les registres de ce jour.
- **Hors du champ** : les règles gelées R1 à R14 et les interdits de CLAUDE.md ne changent pas. Seules changent les pratiques ajoutées par-dessus.

## Constat
Ce matin, environ la moitié du travail de la mère a servi à faire circuler de l'information, à la relire et à la re-vérifier, et non à faire avancer une mesure. Exemples :
- douze brouillons d'un même ordre ; la ligne « Statut » du brouillon 12 recopie l'histoire des onze précédents en un seul paragraphe de plusieurs milliers de signes ;
- sept commits « état intermédiaire » sur main, exigés par le crochet de fin de tour pendant que des agents écrivaient encore ;
- trois vérifications courtes successives sur un même code (contre-lecture, v2, essai de C2), chacune lancée à neuf ;
- des lignes du registre des décisions de 1 500 à 3 000 signes.
La rigueur a pourtant payé deux fois : un dossier mal nommé a été attrapé avant la création de la machine, et un essai tautologique avant l'inscription du code. Il faut garder ce qui attrape ces défauts, et retirer le reste.

## Propositions

### 1. Trois classes de pièces, une chaîne par classe (nœud de Lazar)
| classe | exemples | chaîne |
|---|---|---|
| A, décisive | préenregistrement, verdict, ordre d'une course payante, devis | inchangée : rédacteur neuf, contre-lecteur d'un autre modèle (R2), vérification courte de la différence, scellement |
| B, instrument | code, lanceur, programme de contrôle | contre-lecture d'un autre modèle, puis vérification des seules corrections **par le même contre-lecteur** |
| C, travail | notes, mandats, synthèses, registres, mémoire | aucune contre-lecture, sauf une relecture de cloisonnement quand la pièce sort vers une session fille |
*Rigueur gardée* : R2 et R13 portent sur les préenregistrements et les verdicts, qui restent en classe A. *Gain* : environ un agent par pièce de classe B, et plusieurs par pièce de classe C.

### 2. La vérification courte est faite par le contre-lecteur qui a demandé les corrections (routine)
C'est ce qui s'est passé ce matin pour le code de la base « mots et coût », et il a trouvé l'essai tautologique. Il connaît déjà le texte, le contexte et ses propres exigences ; il reste indépendant de l'auteur. *Gain* : une lecture complète évitée à chaque tour.

### 3. Une seule vérification courte par lot de corrections (routine)
On n'en relance pas une à chaque brouillon. Quand une vérification trouve un défaut, le rédacteur corrige **tout** ce qu'elle relève, y compris ses propres points douteux, avant la vérification suivante. *Exemple de ce matin* : les brouillons 11 et 12 auraient tenu en un seul, si le rédacteur avait traité dès le premier passage le rejeu unique qu'il avait lui-même relevé.

### 4. Les agents écrivent dans leur bloc-notes, et la mère verse à la fin (routine)
Un agent au travail écrit hors du dépôt. Il ne copie dans le dépôt qu'au rendu, puis la mère commite une fois. *Gain* : plus de commits « état intermédiaire » sur main, plus de demande du crochet pendant le travail, et main ne porte que des pièces finies. *Rigueur gardée* : R6 et R12 s'appliquent au versement ; R-3661 s'applique aussi au bloc-notes, qui est versé si l'agent s'arrête en chemin.

### 5. Une ligne « Statut » courte (routine)
L'en-tête d'une pièce dit seulement : version, source et empreinte, auteur, ce qu'il a lu. L'histoire des versions vit dans les notes de différences, déjà écrites et scellées. *Gain* : des pièces lisibles, et des contrôles par programme qui ne buttent plus sur des lignes géantes.

### 6. Des lignes de registre de 600 signes au plus (routine)
Une ligne donne : le fait, la décision, le renvoi par chemin et empreinte. Le détail va dans la pièce citée. *Rigueur gardée* : chaque chiffre renvoie toujours à un chemin et une empreinte (R6).

### 7. Les petites corrections mécaniques passent par un errata, sans nouveau brouillon complet (routine, classe B et C seulement)
Au plus trois couples, sans effet sur un seuil, une garde ou une revendication : on écrit un errata scellé, avec les couples avant et après, et la pièce n'est pas recopiée. Les pièces de classe A gardent leurs brouillons complets.

### 8. Moins de fronts actifs en même temps (nœud de Lazar)
Une dizaine de chantiers sont ouverts aujourd'hui (saboteur, bras A, repli, organisme, lentilles, veille, billets, second cycle, affinage, Bailey…). Proposition : trois chantiers actifs au plus, choisis par Lazar, et les autres gelés jusqu'à la fermeture d'un actif. *Recommandation* : saboteur et sondes pour l'entretien, bras A, organisme v9. *Gain* : la mère coordonne moins et mesure plus. *Coût* : des chantiers attendent.

## Ce qui ne change pas
Préenregistrement scellé avant toute lecture ; contre-lecture par un autre modèle pour la classe A ; verdict par un agent neuf ; aucune dépense sans accord sur devis ; mots de Lazar relus à la source ; récupérer ce qui est récupérable ; aucun contournement d'un refus.
