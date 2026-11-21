# Vérification du programme des deux essais d'admission du bras A — livraison 6 (fichiers `_v5`) — v1

- **Vérificateur** : Claude Opus 5.5, contre-lecteur des livraisons 1 à 5, le 2026-11-21. N'a pas écrit cette livraison : un autre agent Opus l'a rédigée.
- **Objet** : le commit `8befb4975` et sa note `note-programme-essais-admission-bras-a-v5.md`. Les six fichiers `_v5` (chef d'essai, deux relais, faux fournisseur, essais, gabarit v5) répondent « OK » à leur compagnon, et les outils de mutation sont versés sous `tests/mutations_essais_admission_v1/`.
- **Essais** :
  - la commande imposée, deux fois : **203 passés à chaque fois** ;
  - la commande des mutations, rejouée telle que versée (`… campagne_mutations_v1.py toutes`) : **271 mutants, 271 tués, 0 survivant, 0 erreur, code de sortie 0** ;
  - six essais jetables, hors du dépôt (`…/scratchpad/essais_jetables_l6/test_l6_jetable.py`), qui passent tous.
- **Interdits tenus** : aucun réseau, aucun `git fetch`, aucune liste de chemins par motif, aucune clé, `GO_ID` jamais fixé. Du journal, j'ai lu la seule entrée OD-315, par une recherche de ligne. Rien écrit hors ce rapport, rien scellé.

## Verdict

**Engageable pour les lignes de Mistral, dès que leur configuration définitive et leur constat existent. Une correction de code est due avant toute ligne de Google : R-1, le régime prudent imposé par la mère.** D-1 est fermé, le crédit « au moins X » est juste, la borne de 49 536 tient, et les 271 mutants sont tués. Il reste un mineur sur l'âge du taux, que le programme ne borne que par l'heure de la pièce, non par celle de l'envoi.

## 1. D-1 : le constat lu par fournisseur

- **Fermé.** Deux essais le montrent :
  - `test_d1_mistral_seul` : une pièce « Mistral seul » sert une ligne de Mistral et est refusée pour Google ;
  - `test_d1_credit_mistral_bas_n_arrete_pas_google` : un crédit de Mistral à 1,00 USD n'arrête plus Google, et arrête bien Mistral.
- La garde 9 prend le fournisseur de la ligne (`garde_constat`, `chef:863-881`). Le tableau est fermé par la portée de la pièce (`portee_du_constat`, `chef:684-694`) : toute portée autre que les trois admises est refusée, et une clé de l'autre fournisseur est refusée « de trop ».
- **La seconde pièce, `constat_second`** : une ligne ne lit que la seule pièce qui porte son fournisseur. Aucune pièce : la ligne ne part pas. Deux pièces : ambiguïté, la ligne ne part pas. Rien n'est silencieux. Un constat complet, sans ligne de portée, exige encore ses vingt-huit clés même pour Mistral, mais il ne juge que les sept de Mistral. C'est sain : aucune clé ne s'absente sans le dire.
- **Écart à l'avenant 1 (5.1)** : **accepté**. La pièce partielle est la forme que proposait D-1. Elle ne lève aucune clé de plus et ne change aucun seuil. L'avenant 2 devrait l'écrire, pour que la forme ait sa lettre.

## 2. Âge du taux : le dernier fixage publié

- **Ce que le programme tient** : il exige la date du fixage. Celle-ci ne doit pas être après l'heure du taux. Son début (minuit en temps universel) doit être au plus `age_max_du_fixage_heures` avant l'heure de la pièce. La borne est un entier de 1 à 168, exigée en définitive (`chef:565-616`). Je n'ai pas trouvé d'entrée par la pièce elle-même : les mutations de `lire_taux` (41 mutants) sont toutes tuées.
- **Une voie, par l'âge de la pièce (m-a)**, éprouvée par `test_voie_taux_vieux_par_un_constat_vieux` : toutes les bornes (24 heures avant, 6 heures après, âge du fixage) se comptent **depuis l'heure de la pièce**. Seule « jamais après l'envoi » regarde l'envoi. Une pièce de constat vieille d'un mois, avec un taux et un fixage du même jour, passe pour une ligne lancée aujourd'hui : le taux appliqué a un mois. C'est la conséquence de l'abandon du constat ligne par ligne. Le solde lui-même vieillit de la même façon, mais le contrôle par la dépense comptée le tient ; le taux, rien ne le tient. **Proposition** : borner aussi l'âge du fixage par l'heure de l'envoi (même borne, ou une borne propre), ou dire à Lazar qu'un constat en euros ne sert que tant que son taux est frais. C'est un choix de la mère ; le code est simple.

## 3. Crédit dit « au moins X » : 1,1008 ou 1,0980 ?

**1,1008 est juste.** Le programme compte un crédit en euros comme montant × taux × (1 − marge), arrondi au centime inférieur (`convertir`). Il faut donc 7,87 × t × 0,95 ≥ 8,23, soit t ≥ 8,23 ÷ (7,87 × 0,95) = 1,100782… Au quatrième chiffre, 1,1007 donne 8,22 USD, sous le seuil ; 1,1008 donne 8,23. Le chiffre de 1,0980 vient de 8,23 × 1,05 ÷ 7,87 : il multiplie par 1 + marge au lieu de diviser par 1 − marge. Or 1 ÷ 0,95 vaut 1,0526, non 1,05. À 1,0980, le crédit compté vaut 8,20 USD, et la ligne ne part pas (calcul en décimal exact, refait ici).

La lecture « au moins X lu comme X » est du côté prudent : **acceptée**. La forme n'est admise que sur les clés de crédit, avec la source exacte.

## 4. Borne de réflexion sous 65 536

**Juste.** « La plus haute admise » se lit comme 65 536 − 16 000 = 49 536 (essai `test_borne_49536`). Un entier de 49 537 est refusé. Une borne plus basse est admise et dite au manifeste, ce qui répond à ma remarque de la livraison 5. Le relais reçoit la borne lue.

## 5. Les campagnes de mutations

Rejouées par la commande versée, sans clé dans l'environnement : **règle Google, 108 mutants, 108 tués ; livraison 6, 163 mutants, 163 tués ; total 271 tués sur 271, aucune erreur.** Les mutants vivent hors du dépôt, et `git status` ne montre aucun fichier touché par la campagne. Limite dite par le rédacteur, et confirmée : une seule mutation à la fois, et les fonctions qui appellent les gardes ne sont pas mutées.

## 6. Les mineurs encore ouverts

- **m-a, âge du taux par l'âge de la pièce** : section 2.
- **m-7, deux fichiers hors du périmètre modifiés** : toujours ` M` à `git status`, sur décision de Lazar.
- **Plafonds en dollars, seuils de crédit et délais à 65 536** : ce sont des valeurs de configuration. Ils sont à fixer par l'avenant 2 ; le débit requis est maintenant écrit au manifeste. Sans objet pour le code.
- **m-4, sonde sous la forme « budget »** : sans objet tant que le niveau est gardé.

## 7. Le régime prudent pour Google : la décision de la mère est-elle suivie ?

**Non pour la file ; il faut du code.** La décision est au journal, OD-315 : « régime prudent pour les lignes de Google, en vérification comme en file ».

- **En vérification : suivie, sans changement.** Le compteur d'une vérification est toujours prudent (devis 6.4 ; `jouer_verification`).
- **En file : non suivie.** `garde_cle_verifiee` met la file du juge au régime courant dès que les deux sondes disent « comprise » (`chef:1379-1381`). Aucun champ de configuration ne l'impose prudent. La seule voie prudente sans code est un mot de Lazar sur une sonde non « comprise », ce qui n'est pas le cas visé.
- **R-1 — correction** : un champ fermé de configuration, `regime_de_la_file_google`, à « prudent » exigé en configuration définitive (sans défaut ; « courant » refusé en définitive), lu par la garde 10 pour la file du juge. Le régime retenu est recopié au manifeste et au rapport. Un essai par cas.
- **Conséquence à redire à Lazar** (devis 6.4) : au régime prudent, un envoi de Neon coupé au délai total est compté à 200 jetons par seconde de sa durée et arrête la file, sans reprise. À 65 536, le plafond de la file doit être celui de l'avenant 2, au pire cas de 32,97 USD retenu par la mère.

## 8. Ce que j'ai ouvert

- La note de livraison 6, en entier.
- Le chef `_v5`, aux lignes 565 à 616, 684 à 700, 844 à 885 et 1374 à 1384, plus des recherches de lignes. Les essais `_v5`, par recherche de lignes. Les soixante premières lignes de `campagne_mutations_v1.py`. Une ligne du gabarit v5.
- Le journal, la seule ligne OD-315.
- `git log`, `git status`, `git ls-files` sur `tests/mutations_essais_admission_v1/`, et les empreintes par `sha256sum -c`, chemin par chemin.
- Lus par programme pendant les essais et les mutations : le lot des entrées nommé par le devis, les consignes et les règles par empreinte, les modules du programme de forme.
- Aucun chemin interdit ouvert, listé ni empreinté.
