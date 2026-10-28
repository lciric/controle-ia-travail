# « The Preregistration Revolution » (Nosek et al.) — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Brian A. Nosek, Charles R. Ebersole, Alexander C. DeHaven, David T. Mellor. « The Preregistration Revolution » (p. 1).
- Version lue : prépublication déposée sur l'Open Science Framework (OSF, identifiant 2dxu5), fichier servi sous le nom « NEDM2017.pdf », créé le 24 août 2017 selon ses métadonnées. Le PDF ne mentionne aucun lieu de publication.
- Version publiée : Proceedings of the National Academy of Sciences, 2018, identifiant d'objet numérique 10.1073/pnas.1708274114 — d'après des pages tierces (notice IDEAS/RePEc, résultat de recherche citedrive), pas d'après le PDF : à vérifier, et le texte publié peut différer de la prépublication lue.

## Fichier lu
- `pdfs/preregistration-revolution/osf-2dxu5-preprint.pdf`, 221 013 octets, 19 pages ; SHA-256 `937416ea98b92b0df93cd3ab40fa8edfd6b285d9fdfef152ee277faed33bd783` (même empreinte que la v1 ; le stockage d'OSF nomme d'ailleurs l'objet par cette même empreinte).
- Pages lues : 1 à 15 (tout le texte et les notes) ; références parcourues.

## Comment la boucle est faite
- Pas de système : le cycle de recherche. Postdiction (engendrer une hypothèse à partir de données déjà vues) contre prédiction (tester une idée sur des données nouvelles) (p. 2).
- Cycle idéal (p. 6) : préenregistrer plan et analyse, recueillir, analyser selon le plan, puis explorer ; les postdictions les plus intéressantes deviennent les prédictions de l'étude suivante, et le cycle recommence.
- « Preregistration does not favor prediction over postdiction; its purpose is to make clear which is which » (p. 6).

## Traitement du bruit et du sur-ajustement
- La valeur diagnostique d'une valeur p dépend du nombre de tests faits et des chemins qui auraient pu être pris (p. 4 et 5, en reprenant Gelman et Loken).
- Outils (p. 7 à 11) : documenter les écarts au plan (p. 7) ; préenregistrement par étapes (p. 7) ; mise en aveugle des données par brouillage (p. 7) ; arbre de décision préenregistré (p. 7) ; procédures opératoires standard (p. 7) ; rapporter tous les résultats, y compris « 1 in 20 » positif (p. 10) ; validation croisée avec une part scellée jusqu'à la fin de l'exploration, en préenregistrant les conclusions de l'exploration avant de desceller (p. 10) ; correction de Bonferroni quand le récit se concentre sur quelques résultats (p. 11) ; rapports enregistrés (« Registered Reports »), acceptés sur le plan avant les résultats (p. 13).
- Éléments empiriques cités : chute des résultats positifs dans les essais cliniques après l'obligation d'enregistrer le critère principal (Kaplan et Irvin) (p. 5) ; dans un échantillon d'études préenregistrées, 40 % des articles omettent au moins une condition et 70 % au moins une variable de résultat (Franco, Malhotra et Simonovits) (p. 6).

## Échecs et limites rapportés par les auteurs
- Il n'y a « not yet sufficient experimental evidence » de la supériorité du préenregistrement pour la reproductibilité ; les preuves sont corrélationnelles (p. 5).
- Les bénéfices sont perdus si les préenregistrements ne sont pas suivis (p. 6).
- On peut préenregistrer des biais dans un arbre de décision (enchaîner des règles d'exclusion jusqu'à p < 0,05) : détectable, mais cela invalide l'inférence (p. 7).
- Le préenregistrement n'élimine ni les comparaisons multiples entre études ni le choix narratif des résultats mis en avant (p. 10 et 11) ; quand les données sont rares, « no magical solution » (p. 11).

## Vérifié par des tiers
- Non trouvé pour ce texte. Les études empiriques qu'il cite (p. 5 et 6) ne sont pas lues ici.

## À emprunter
- Boucle extérieure : le registre d'hypothèses écrit avant tout score est un préenregistrement ; y joindre l'arbre de décision du script de lecture, rapporter toutes les issues du registre (nulles comprises) et consigner chaque écart (p. 7 et 10).
- Boucle intérieure : une primitive qui laisse l'organisme lancer de nombreux tests trouvera des positifs par hasard (« 1 in 20 ») ; elle doit journaliser tous les tests, pas seulement les gagnants (p. 10).
- Mesure du bruit : part scellée et conclusions de l'exploration enregistrées avant de desceller (p. 10) — c'est le principe de `test_final`.
