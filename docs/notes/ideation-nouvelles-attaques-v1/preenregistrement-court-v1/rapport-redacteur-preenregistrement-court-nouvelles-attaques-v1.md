# Rapport du rédacteur — préenregistrement court de la course « nouvelles attaques » — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevés de `date -u` : 05:05:09Z avant l'écriture, 05:09:31Z après le complément de la mère sur la troisième clé.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Réseau : deux `git fetch origin main`. **Aucun refus de permission, de classifieur ni de garde.**
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/mandat-redacteur-preenregistrement-court-nouvelles-attaques-v1.md` (`750ba73342670fbb8b163da7db35e85d8ad051d0b23f1576e8031f4c801ed7d0`, vérifiée contre son compagnon). Trois ajouts de la mère portés : deux clés et un relais par clé (R-4084, R-4087) ; parts ouvertes (R-4088) ; troisième clé et répartition proposée par branche (GO-2026-11-20-14, R-4089), reçu en cours d'écriture.

## 1. Verdict

1. Le préenregistrement court est écrit, selon le § 12 de l'ordre de course v3 et le gabarit : `preenregistrement-court-course-nouvelles-attaques-v1.md`, même dossier que ce rapport. Il ne contient ni méthode d'attaque, ni procédé, ni détail opérant, ni identifiant de modèle.
2. **Il ne revendique aucune prédiction chiffrée** : la course n'a ni hypothèse ni bras témoin. Il écrit au même rang « l'héritage ne laisse aucune trace » et son contraire, « aucune fiche n'est inédite » et son contraire.
3. **Les parts par clé ne sont pas figées.** Le texte porte une répartition proposée des rôles du premier relais sur les trois clés, pour les deux branches, et dit ce que les coûts du devis ne permettent pas : au pire du devis, aucune répartition ne tient chaque part sous son solde ; elles ne tiennent qu'au cas haut.

## 2. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-nouvelles-attaques/`. Chaque pièce a son compagnon `.sha256` ; les empreintes sont dans les compagnons et dans ma réponse. Le sous-dossier `lectures/` garde les deux extraits de `main` ; ce ne sont pas des pièces rendues.

## 3. Sources, avec empreinte

Dossier noté NA : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.

| pièce | empreinte | lu |
|---|---|---|
| `NA/conception-v3/question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` (compagnon : égal) | en entier |
| `NA/conception-v3/ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` (compagnon : égal) | en entier |
| `NA/conception-v3/rapport-redacteur-conception-nouvelles-attaques-v3.md` | `6c28636ce07f73b018e7746cb78a03672a224995ad0aff0d7602a6498174ee98` (compagnon : égal) | en entier |
| `NA/conception-v2/devis-course-nouvelles-attaques-v2.md` | `714e4fc6a9a292626022adac4a5ddcc4f3e16fd14f81629b6b8a98cf89fcf028` (compagnon : égal) | en entier |
| `NA/conception-v2/calcul-devis-course-nouvelles-attaques-v2.json` | `ffecbd1172888b815e6f7af84ae54f52c1991554d6d2ff376481af694e60b7cf` (recalculée ; égale à celle que le devis cite) | en entier |
| `NA/conception-v3/controle-differentiel-conception-nouvelles-attaques-v2-v3-v1.md` | `6fd50296fc7c674b516daa2c2895a96c42ccb775ac2de0b7a5d855a5736cbd5e` (compagnon : égal) | en entier |
| `NA/mandat-redacteur-conception-course-nouvelles-attaques-v1.md` | `8fd94f6f78e51665eccfd2bc11c634f7bce207f9ed70d237e464e2d9b3eda294` (recalculée ; égale à celle que la question cite) | empreinte seulement |
| `NA/complement-1-mandat-redacteur-conception-course-nouvelles-attaques-v1.md` | `226ea15243c947164d4c3595c350d90fea980694f7d4903cf8dac33e56b81fdd` (recalculée ; égale à celle que la question cite) | empreinte seulement |
| `registres/go.md` sur `main`, commit `8cf0d3d136ab78d77d8b7978d1fdaff4e9eac59f` | `8639e38fea4708c2f843202b1bb26fe0321381d9792e79bbdb853fcd3d288024` | lignes GO-2026-11-20-05 à -14 |
| `registres/decisions.md` sur `main`, même commit | `f45e63331edbb756fe5519ac9a763965cb1f7058c37225ae962d222c38032903` | R-607 à R-611, R-3237, R-3611, R-4084 à R-4090 |
| `/home/user/controle-ia-travail/prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` | en entier |
| `/home/user/controle-ia-travail/CLAUDE.md` | `c9d86f7366aa0108d922f167032e2226505d6ad08ef8d5bb8e8c21416fe2768c` | en entier |

Un premier extrait de `main` (commit `47e430c31cfcfe316d0613a0f07dd1090b78b767`) ne portait ni GO-2026-11-20-14 ni R-4089 ; le second les porte, et c'est lui que le texte cite. Non lu : le code de l'orchestrateur ; toute sortie d'une course ; le coffre ; les décisions N-044, N-045, N-049, N-053, N-054, N-058, N-065, que je cite d'après l'ordre de course.

## 4. Choix du rédacteur, à contre-lire

Le § 12 de l'ordre demande que ce texte gèle des valeurs que la conception laissait à geler. Celles que j'ai posées moi-même, marquées comme telles dans le texte :

1. **La racine des graines** : l'entier des 32 premiers caractères hexadécimaux de l'empreinte de la question ; une clé de dérivation par tâche. Le tirage lui-même n'est pas joué : il revient au programme du véhicule, et sa sortie se scelle à part.
2. **La borne de lecture d'antériorité : 60 fiches**, tirées par graine au-delà.
3. **Le périmètre de recherche dans la littérature** : six bases, période depuis le 1ᵉʳ janvier 2016, trois classes de requête, trente premiers résultats par base et par classe.
4. **Les seuils de l'audit de symétrie** : part d'inédites nulle ou d'au moins la moitié ; part de filiation égale à 0 ou à 1 ; aucun coffre et aucun hors case sur la course.
5. **Trois précisions** : le dénominateur de la part de filiation (les fiches passées) et le compte à part des filiations invalides ; une étiquette interdite dans le registre arrête la génération suivante, sans retrait silencieux ; une espèce retirée à la sonde de refus change la composition, donc la course ne part pas sans version neuve.
6. **Le « complément de valeurs »** : une pièce courte, contre-lue et scellée, qui fige les parts par clé et les bornes en octets avant tout allumage et avant la contre-lecture du véhicule. C'est ma façon de sceller ce texte maintenant sans inventer ces valeurs.
7. **La répartition par clé** : aiguilleur et proposeur de l'espèce 4 sur Minuit ; juge de l'espèce 3 sur Luc ; proposeur de l'espèce 3 sur Rigaud. Les coûts sur trois générations sont calculés à la main à partir du devis et de la sortie de son calcul, non rejoués par programme.

## 5. Ce qui reste ouvert

1. La branche des clés (bornes par clé, ou recharge), les parts en USD, la répartition confirmée : mot de Lazar, puis complément de valeurs.
2. **Le besoin du bras A sur la clé Rigaud** : écrit nulle part dans ce que j'ai lu. Au-delà d'environ 20 USD, Rigaud ne couvre plus son rôle au cas haut.
3. La clé qui paie les deux lignes à part (5 USD et 1 USD), et la dispense de lecture de solde pour les clés des deux autres relais (R-3237), à redire au devis final.
4. Les bornes en octets de la consigne et du registre : elles attendent la mesure des consignes.
5. Le véhicule neuf et son mot d'activation ; le commit du code d'analyse, absent à cette date.
6. La question n'est pas encore scellée ; ce texte n'est ni contre-lu ni scellé.
7. Le texte du contrôle (§ 3) sur les comptes « hors case » est repris dans les mesures et dans la liste d'arrêt ; l'ordre de course v3 lui-même ne le porte pas.

## 6. Nœuds pour Lazar

### N1 — La branche des clés
**Décision.** Sous quelle branche la part du premier relais se paie-t-elle sur Minuit, Luc et Rigaud ?
**Enjeu.** Il manque environ 26,44 USD à la somme des trois soldes pour la part au pire de 450 USD ; sans bascule, une clé épuisée arrête la course.
**Options.** (a) bornes par clé, aucune recharge : rien à payer d'avance, mais la somme des parts reste sous la ligne et l'arrêt nommé peut couper la course avant 450 USD. (b) recharge de Rigaud d'au moins 26,44 USD plus le besoin du bras A : la somme atteint 450 USD et le bras A garde sa part, mais c'est une dépense d'avance sur la clé la plus pauvre. (c) ligne à trois espèces, 195 USD : moins cher, mais deux espèces retirées sans preuve, et ce préenregistrement est à récrire.
**Recommandation.** (a), confiance 0,6 : au cas haut du devis, les trois parts tiennent avec une marge d'au moins 1,3 ; la mère recommandait déjà le bornage (R-4088). Je passerais à (b) si le bras A a besoin de plus de 20 USD sur Rigaud.
**Défaut.** Aucun : compte et dépense.

### N2 — Le besoin du bras A sur Rigaud
**Décision.** Quelle somme la course laisse-t-elle au bras A sur la clé Rigaud ?
**Enjeu.** Deux travaux sur une même clé, sans bascule : ce que l'un prend, l'autre le perd.
**Options.** (a) le montant du devis du bras A, retranché de la part de la course : net, mais Rigaud peut ne plus porter de rôle. (b) Rigaud laissée entière au bras A, le proposeur de l'espèce 3 passant sur Minuit : aucun partage, mais la marge de Minuit tombe à 1,08 au cas haut.
**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : compte.

Deux points de routine pour la mère, non des nœuds : confirmer ou changer la borne de 60 fiches et le périmètre de recherche avant le scellement ; dire si « une espèce ou un rôle fixe par clé » (GO-2026-11-20-14) permet de séparer le proposeur et le juge de l'espèce 3 sur deux clés, ce que la répartition proposée suppose.

## 7. Écarts et réserves

1. Aucun refus. Aucune commande de liste. Les deux `git show` ont été redirigés vers `lectures/`. Une commande `grep` a porté sur deux fichiers nommés de mon dossier.
2. Le mandat dit « deux clés » ; le complément reçu en cours d'écriture en dit trois. Le texte porte trois clés ; ses premières lignes écrites pour deux ont été remplacées avant la remise.
3. Le texte ne nomme pas le fournisseur des trois clés : il dit « le premier relais du devis », dont les rôles sont ceux que le devis lui donne (§ 3). Si la part visée par GO-2026-11-20-12 et -14 n'est pas exactement ce relais, la répartition est à reprendre.
4. Les soldes sont calculés ou déclarés, jamais lus sur le compte ; celui de Rigaud est « environ ».
5. Les heures des registres et celle de mon horloge ne s'accordent pas : R-4088 et R-4089 sont datées 05:02:38Z et 05:03:54Z et citent des mots de Lazar « vers 05:08Z » et « vers 05:14Z » ; mon relevé après ces lectures est 05:09:31Z. Je le signale, sans conclure.
6. L'ordre de course et le devis ne sont pas modifiés : le devis reste écrit pour un premier relais sur une seule clé. Le devis final devra porter les trois clés.

— rédacteur neuf, modèle F
