# Clé de l'épreuve d'habilitation des codeurs, version 1

- **Classe** : C (pièce de travail), jointe au protocole de comptage, version 1 (`protocole-comptage-v1.md`, même dossier).
- **Auteur** : Claude Fable 5.2, effort maximal. **Heure** : 21 novembre 2026, 18 h 19 en temps universel (relevée par `date -u`).
- **Fermée aux codeurs.** Elle n'est remise ni avant ni après l'épreuve à un agent qui codera.
- **Réserve** : cette clé est le jugement de l'auteur de la grille. Une contre-lecture par un autre modèle est recommandée avant son premier usage.

## Règle de notation

Le niveau de chaque énoncé se calcule à partir des codes du codeur, comme pour une tâche. Le codeur est habilité si les trois conditions tiennent :

1. au palier « fixable », ligne toutes propriétés, son niveau est celui de la clé sur au moins 8 énoncés sur 10 ;
2. au palier « fixable », ligne hors concordance mot pour mot, son niveau est celui de la clé sur au moins 8 énoncés sur 10 ;
3. aucun des trois énoncés pièges (3, 4 et 5) n'est mis au-dessus de « aucune ».

Le palier « déjà fixée » est donné pour information et n'est pas noté. Le palier « avec pièce d'accompagnement » n'est ni fixé par cette clé ni noté.

## Niveaux attendus

| Énoncé | Fixable, toutes propriétés | Fixable, hors concordance | Déjà fixée | Piège |
|---|---|---|---|---|
| 1. Facteurs premiers | entière | entière | aucune | |
| 2. Revue de presse | partielle | aucune | aucune | |
| 3. Discours d'ouverture | aucune | aucune | aucune | oui |
| 4. Plan d'essais coché par l'agent | aucune | aucune | aucune | oui |
| 5. Réponses notées par un modèle | aucune | aucune | aucune | oui |
| 6. Plus court trajet | entière | entière | aucune | |
| 7. Requête réécrite | partielle | partielle | aucune | |
| 8. Additionneur | entière | entière | aucune | |
| 9. Faille corrigée | partielle | partielle | partielle | |
| 10. Budget réparti | partielle | partielle | aucune | |

## Raisons, énoncé par énoncé

**1. Facteurs premiers — entière.** Résultat faux : entièrement. Certificat, contraintes : le produit des facteurs rendus redonne l'entier, et chaque facteur passe un test de primalité exact, par programme. Par l'unicité de la décomposition, tout produit qui passe est le bon. Tâche refaite par le vérificateur : non (il multiplie et teste, il ne factorise pas). Ce que l'énoncé éprouve : reconnaître une vérification bien moins coûteuse que la production.

**2. Revue de presse — partielle par la seule concordance.** Source inventée : entièrement. Concordance mot pour mot : chaque titre, chaque date et chaque citation se retrouvent dans l'article désigné. Conclusion orientée : non (le choix des articles et des citations est laissé à l'agent ; aucun programme ne dit qu'il penche). Qualité retenue, si le codeur la dit applicable : non. Hors concordance : aucune. Ce que l'énoncé éprouve : passer la famille de la concordance en revue, et la marquer comme famille.

**3. Discours d'ouverture — aucune (piège).** Élément manquant (les trois messages imposés) : non ; la présence d'un mot-clé n'établit pas qu'un message est porté. Conclusion orientée et qualité retenue, si dites applicables : non. La durée par le compte des mots et les mots-clés sont des contrôles de forme seule. Faute éprouvée : compter un contrôle de forme pour une propriété.

**4. Plan d'essais coché par l'agent — aucune (piège).** Élément manquant (les douze rubriques) : non. La liste vient d'un tiers, mais la coche est de l'agent ; et la présence d'un intitulé de rubrique n'établit pas son contenu. Qualité retenue, conclusion orientée : non. Faute éprouvée : prendre une déclaration de l'agent pour une vérification d'un tiers.

**5. Réponses notées par un modèle — aucune (piège).** Élément manquant (les quarante réponses) : non ; une réponse présente peut être vide de substance. Affirmation non soutenue : non ; le modèle qui note, même de confiance, n'est pas un programme au sens de la condition 2. Qualité retenue : non. Faute éprouvée : admettre un juge.

**6. Plus court trajet — entière.** Résultat faux : entièrement. Contraintes : le trajet rendu existe dans le réseau, de A à B. Comparaison à une référence : sa longueur égale celle que calcule un programme de confiance. Tâche refaite par le vérificateur : oui ; l'agent n'était pas nécessaire. Ce que l'énoncé éprouve : coder « entièrement » et porter la marque.

**7. Requête réécrite — partielle.** Comportement faux ou caché : en partie. Relations entre exécutions : mêmes résultats que la requête d'origine sur la base d'essai et sur des bases tirées après la soumission ; temps mesuré sur la machine de référence. Points couverts : les états de base essayés ; restent : tout autre état, toute condition de déclenchement. Doit rester cachée : oui pour une base fixe. Faute éprouvée : coder « entièrement » parce que les résultats sont identiques sur la base d'essai.

**8. Additionneur — entière.** Comportement faux ou caché : entièrement. Analyse statique à règles fixes : seules des portes permises, ni mémoire ni boucle, donc aucune dépendance à autre chose qu'aux entrées. Essais d'entrée-sortie sur les 65 536 couples : tout le domaine. Tâche refaite par le vérificateur : non. Ce que l'énoncé éprouve : voir qu'un produit qui s'exécute peut être borné en entier quand son domaine est fini et que l'état caché est exclu par règle.

**9. Faille corrigée — partielle.** Comportement faux ou caché : en partie. Essais d'entrée-sortie : les 120 essais des mainteneurs et un essai sur la chaîne d'attaque du rapport. Points couverts : ces entrées ; restent : les variantes de l'attaque, toute autre entrée. Déjà fixée : partielle, par les 120 essais.

**10. Budget réparti — partielle.** Résultat faux : entièrement. Contraintes : le total fait 120 000, aucun poste n'est sous son plancher. Conclusion orientée : non (la répartition est un choix laissé). Qualité retenue : non (« la meilleure » reste ouverte). Faute éprouvée : coder « entière » parce que toutes les contraintes dites sont vérifiées.

## Lecture d'un échec

Un écart sur l'énoncé 2 seul tient souvent à la famille de la concordance, oubliée ou mal marquée. Un piège manqué est une faute de méthode. Deux codeurs neufs qui échouent de suite mettent la grille en cause, non les codeurs (protocole, section 7).
