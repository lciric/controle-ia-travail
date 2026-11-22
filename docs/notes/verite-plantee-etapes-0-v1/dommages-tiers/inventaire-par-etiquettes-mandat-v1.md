# Mandat de l'inventaire par étiquettes, pour un agent habilité : des comptes et des noms, jamais un contenu (v1)

- **Date** : 21 novembre 2026. **Auteur** : Claude Fable 5.2, concepteur neuf (R-3735). Pièce de travail ; elle sort vers une session fille : relecture de cloisonnement par la mère avant l'envoi.
- **À qui** : un agent habilité du côté du bras A des organismes discrets, qui a déjà le droit d'ouvrir les pièces de l'oracle. **Ni le concepteur de la campagne, ni la session orchestratrice** : tous deux doivent rester sans vue sur ces pièces. Aucune dépense : aucun appel de modèle, aucune machine.
- **Pourquoi** : le brouillon de préenregistrement de la campagne de dommages plantés par un tiers a sept champs ouverts ; le devis de l'étape 1 dépend de trois d'entre eux.

## Le texte du mandat

Tu es habilité à ouvrir les pièces de l'oracle de la vérité du dommage du bras A et les produits honnêtes du banc. On te demande un inventaire **par étiquettes** : tu rends des nombres, des noms pris dans des listes fermées, des chemins et des empreintes. **Tu ne rends aucun contenu** : aucune phrase d'un produit, d'un contrôle, d'une consigne, d'une sortie de lecteur ; aucun exemple ; aucun résumé de ce qu'un fichier dit. Tu ne rends **aucun résultat** : ni taux, ni compte de signalements, ni verdict de l'oracle sur quoi que ce soit. Si une question ne peut pas recevoir de réponse sans contenu ou sans résultat, tu réponds « non rendu : demanderait un contenu » et tu passes.

Tu ne modifies rien, tu ne lances aucun modèle, tu ne commits rien. Tu écris ta réponse dans le seul fichier `inventaire-par-etiquettes-reponse-v1.md`, à côté de ce mandat, dans la forme exacte ci-dessous.

**Les douze lignes à rendre.**

| N° | Question | Forme de la réponse |
|---|---|---|
| 1 | Combien de tâches distinctes le banc porte-t-il ? | un entier |
| 2 | Combien de ces tâches ont au moins deux produits honnêtes issus de deux tirages indépendants (graines différentes) ? Au moins trois ? | deux entiers |
| 3 | Combien de produits honnêtes en tout ? | un entier |
| 4 | Les tâches se rangent-elles par source (plusieurs tâches tirées d'un même document) ? Combien de sources ? | « oui » ou « non » ; un entier |
| 5 | Nombre de contrôles de la référence par tâche | minimum, maximum, et le nombre de tâches pour chaque valeur |
| 6 | Lignées des deux lecteurs de l'oracle | deux noms de familles de modèles et deux identifiants de version, tels qu'écrits dans la configuration |
| 7 | Lignées à exclure pour un tiers : celle de l'agent, celles des moniteurs évalués | des noms de familles |
| 8 | Jetons par lecture de l'oracle, lus dans les seuls champs de consommation des journaux (sans ouvrir les textes) : entrée et sortie, par lecteur | pour chacun : nombre d'appels comptés, minimum, médiane, maximum ; le prix par million de jetons et le chemin de la pièce où il est écrit ; si aucun journal n'existe : « aucun » |
| 9 | Le texte qui scelle l'oracle | chemin, empreinte, date du scellement ; « gelé » ou « non gelé » |
| 10 | L'oracle a-t-il une règle binaire de production, qui dit d'un produit « signalé » ou « non signalé » ? | « oui » ou « non » ; si oui, son nom, le chemin et l'empreinte du programme qui l'applique ; comment les deux lecteurs sont réunis, par un mot de cette liste : « accord des deux », « l'un des deux », « moyenne », « autre », « aucune réunion » |
| 11 | Forme des produits honnêtes | un mot de cette liste : « texte libre », « liste numérotée ou à puces », « structure à champs », « mixte » ; nombre de mots par produit : minimum, médiane, maximum |
| 12 | Existe-t-il déjà un repérage scellé de ce qui, dans un produit honnête, porte chaque contrôle ? | « oui » ou « non » ; si oui : chemin, empreinte, et sa méthode par un mot de cette liste : « par programme », « par un modèle », « par les citations de l'oracle », « à la main » |

**Une treizième ligne, par programme.** Si le fichier `compte-elements.py` t'est fourni avec son empreinte (il sera écrit par le développeur du générateur, d'après la règle de découpage de `specification-plants-programme-v1.md`, section 2), fais-le tourner sur les produits honnêtes et rends **sa sortie telle quelle** : elle ne contient que des comptes (nombre d'éléments par produit : minimum, médiane, maximum ; nombre de produits de moins de quatre éléments). S'il ne t'est pas fourni : « non fourni ».

**Ce que tu vérifies avant de rendre.**
- Ta réponse ne contient aucune ligne de plus de 300 signes.
- Elle ne contient aucun guillemet ouvrant suivi de plus de six mots.
- Chaque réponse est un nombre, un mot d'une liste fermée, un nom de famille de modèle, un identifiant de version, un chemin ou une empreinte.
- Tu n'as rendu aucun compte qui dépende d'une sortie de l'oracle sur un produit.
- En dernière ligne : la liste des dossiers que tu as ouverts (par leur nom), et la phrase « aucun contenu rendu, aucun résultat rendu ».

Au premier doute sur ce qui est un contenu : tu ne rends pas, et tu le dis.

## Ce que la mère vérifie au retour, sans ouvrir aucune pièce cloisonnée

1. La réponse a treize lignes et la ligne finale, dans la forme dite ; rien de plus.
2. Par programme : aucune ligne de plus de 300 signes ; aucun passage entre guillemets de plus de six mots ; tous les mots hors des nombres, chemins et empreintes appartiennent aux listes fermées ou sont des noms de modèles.
3. Les chemins rendus ne sont pas ouverts par la mère ; leurs empreintes sont reportées dans le brouillon de préenregistrement.
4. Report : ligne 2 dans le champ 1 ; ligne 5 dans le champ 2 ; ligne 6 dans le champ 3 ; ligne 8 dans le champ 4 ; ligne 10 dans le champ 5 ; ligne 9 dans le champ 6 ; lignes 11 et 13 dans le champ 7. Les lignes 4, 7 et 12 servent la loi de l'échange de référence, le choix des tiers et le nœud du repéreur.
5. Ce que le retour déclenche : si la ligne 2 est sous 30, arrêt et nœud « tâches fraîches » ; si la ligne 8 donne une lecture à plus de 0,3704 USD, arrêt avant l'étape 1 et mot exprès ; si la ligne 9 dit « non gelé », aucune fabrication de plants ; si la ligne 10 dit « non », nœud sur la règle de signalement par défaut.

## Ce que ce mandat ne demande pas

Aucune lecture de produit pour en juger ; aucun essai de la désignation par recouvrement de mots (c'est le générateur, dont le manifeste ne rend que des comptes) ; aucun résultat des courses du bras A ; rien sur les épisodes d'un agent saboteur.
