# « The garden of forking paths » (Gelman et Loken, 2013) — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Andrew Gelman, Eric Loken. « The garden of forking paths: Why multiple comparisons can be a problem, even when there is no “fishing expedition” or “p-hacking” and the research hypothesis was posited ahead of time ». Manuscrit daté du 14 novembre 2013 (p. 1), téléchargé depuis le répertoire « unpublished » de la page d'Andrew Gelman à l'Université Columbia (département de statistique). Pas de lieu de publication avec comité de lecture indiqué sur le PDF.
- Un article voisin des mêmes auteurs, « The statistical crisis in science » (2014), est cité p. 22 du PDF de « Preserving Statistical Validity in Adaptive Data Analysis » (fiche `reusable-holdout-stoc.md`) ; non lu, et sa référence n'est pas vérifiée ici.

## Fichier lu
- `pdfs/garden-forking-paths/gelman-loken-2013-p_hacking.pdf`, 219 914 octets, 17 pages ; SHA-256 `8cfd8ffd854e4269979c83d7d41b0ee843b0223e9923e3e47f60ca3a0403cb3c` (même empreinte que la v1). Source : `https://www.stat.columbia.edu/~gelman/research/unpublished/p_hacking.pdf`, redirigée vers `sites.stat.columbia.edu` (même établissement).
- Pages lues : 1 à 15 (tout le texte) ; références parcourues.

## Comment la boucle est faite
- Pas de système : la boucle est celle du chercheur qui analyse ses données. Quatre procédures (p. 2) : (1) un test unique ; (2) un test choisi d'avance, préenregistré ; (3) un seul test calculé, mais dont les choix (exclusions, codages, interactions, sous-groupes) auraient été autres si les données avaient été autres ; (4) la « pêche » : plusieurs tests et le meilleur rapporté.
- Thèse : les chercheurs font (3) en croyant faire (2), et répondent qu'ils ne font pas (4) (p. 2 et 3). Il y a une correspondance « one-to-many » entre hypothèse scientifique et hypothèses statistiques (p. 6).
- Exemples analysés : circonférence du bras et attitudes politiques, perception extrasensorielle, cycle menstruel et intentions de vote, entre autres (p. 4 à 11).

## Traitement du bruit et du sur-ajustement
- Le problème de comparaisons multiples existe dès que l'analyse dépend des données, même sans pêche consciente ; les valeurs p publiées ne peuvent pas être prises « at face value » (p. 12).
- Remèdes proposés (p. 13 à 15) : le préenregistrement ; la réplication avant publication — une première expérience exploratoire, une seconde purement confirmatoire avec son protocole préenregistré (p. 13 et 14) ; l'analyse de toutes les comparaisons pertinentes, au besoin par modèle multiniveau (p. 14) ; une distinction nette entre analyse exploratoire et analyse confirmatoire (p. 15).
- Exemple de réplication préenregistrée qui échoue (Nosek, Spies et Motyl, cités) : puissance annoncée « over 99% », valeur p de 0,59 (p. 14).

## Échecs et limites rapportés par les auteurs
- Pour une grande partie de leurs propres travaux, le préenregistrement « hardly seems possible » ; leurs hypothèses les plus importantes n'auraient pas pu être formulées d'avance (p. 13).
- Les difficultés pratiques de l'approche multiniveau « are not trivial » et l'inférence peut être sensible aux hypothèses du modèle quand les comparaisons sont peu nombreuses (p. 14).
- Texte argumentatif : pas de méthode formelle ni d'estimation chiffrée de l'inflation des erreurs.

## Vérifié par des tiers
- Non trouvé comme vérification. « The preregistration revolution » (lu) reprend le cadre du « jardin aux sentiers qui bifurquent » et le cite (p. 4 de son PDF).

## À emprunter
- Boucle extérieure : chaque choix du script de lecture (classes, générations comparées, exclusions, agrégats) doit être figé avant tout score ; sinon les verdicts relèvent du cas (3) même sans pêche (p. 2).
- Boucle intérieure : un organisme qui « teste ses hypothèses » sur les données mêmes où il s'adapte fait, par construction, du (3) ou du (4) ; ses gains internes ne valent que confirmés sur des données séparées.
- Mesure du bruit : apparier chaque gain exploratoire à une réplication confirmatoire préenregistrée, en deux temps (p. 13 à 15).
