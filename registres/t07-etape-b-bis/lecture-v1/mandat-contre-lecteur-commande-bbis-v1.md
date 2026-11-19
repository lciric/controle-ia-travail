# Mandat du contre-lecteur de la commande de lecture — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf, d'un autre modèle que le préparateur ; tu n'as pas écrit la commande. Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie.

## Ta tâche
Contre-lire `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md` (vérifie son compagnon) contre ce qui fait foi, et dire si le lecteur-opérateur peut la jouer telle quelle. Tu ne lis **aucun** fichier de résultat et tu ne joues rien sur les données réelles.

## À lire
Les mêmes pièces que le préparateur : `prereg/T0.7-etape-B-bis-v1.md` (plan d'analyse, points 1, 2, 10, 11, 12 ; critères gelés ; liste d'arrêt ; données gardées ; lignes de registre), ses trois addenda, `registres/t07-etape-b-bis/feu-bbis-v7.txt` § 12 et § 13, `registres/t07-etape-b-bis-v1.md`, `registres/t07-etape-b-bis-v1-addenda-v1.md`, `registres/t07-etape-b-bis/code-bbis-v2.json`, le code `src/controle_ia/t07bbis/` et ses essais ; `registres/t07-etape-b-bis/lecture-v1/mandat-preparateur-lecture-bbis-v1.md`.

## Ce que tu vérifies, point par point
1. Le module de lecture en vigueur est bien celui que le texte et les addenda désignent ; les empreintes du code égalent celles de la fiche inscrite.
2. L'ordre est celui du texte : antériorité inscrite à part et journal des ouvertures créé **avant** toute lecture ; garde d'ouverture avant toute lecture ; au refus, rien n'est lu.
3. La preuve d'antériorité prouve bien ce que le plan, point 2, et les addenda demandent, depuis une histoire complète, par les noms et les commits seulement ; elle ne peut pas passer à tort (histoire tronquée, branche manquante, fichier renommé) ni refuser à tort.
4. Les entrées sont exactement la liste blanche du point 1 ; aucun fichier de la liste « Jamais » ; aucun fichier de l'étape B ne peut être ouvert par la commande.
5. Les arguments, l'entropie, les graines, les chemins et le nom du run de lecture sont ceux du texte et du code ; la ligne de commande est jouable (signature des fonctions, options existantes).
6. Les sorties sont scellées avant toute lecture humaine ; la ligne `LECTURE-BBIS` a le format du registre propre ; rien n'est écrit dans `registres/scellements-v1.md`.
7. Rien, dans la commande, ne fait apparaître une mesure, une aire ou une issue dans ce que l'opérateur rend à la conductrice.
8. Les points ouverts du préparateur : pour chacun, ce que le texte tranche, ou « nœud ».

## Rendu
Un fichier `registres/t07-etape-b-bis/lecture-v1/contre-lecture-commande-lecture-bbis-v1.md`, scellé : constats numérotés (majeur : la commande ne peut pas être jouée telle quelle ; mineur : à corriger sans rejouer la contre-lecture ; note), chacun avec la ligne de la commande et la ligne du texte ou du code qui le fonde ; conclusion en un mot : « jouable », « jouable après corrections mineures » ou « non jouable ». À la conductrice : chemin, empreinte, conclusion, nombre de constats par niveau, liste des fichiers de résultat ouverts (attendue : aucun).
