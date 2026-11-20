# Avis — comment ne servir que la partie servie de la question v4 (course « nouvelles attaques ») — v1

Pièce de travail (classe C), écrite le 2026-11-20 sur le mandat `docs/notes/ideation-nouvelles-attaques-v1/question-v4/mandat-avis-fable-partie-servie-v1.md` (`a4b99bcf75620f37d4c9b29dead844ecc959cf08482d0f4ed3dba4a39b191833`, vérifiée contre son compagnon). Avis de conception : il ne tranche rien, le directeur du programme choisit. Processeur seul : aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt. Aucune méthode d'attaque, aucun procédé, aucun identifiant de modèle, aucune valeur de clé.

Pièces lues en entier, empreintes recalculées : question v4 (`47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`) ; sa contre-lecture (`d8e0bce5334a7f6fa0cd9c8d23a546d69fc5c07e1826b6ca3ecc303317414ebd`) ; rapport du rédacteur (`6bed22dd3673da1f3cb447a15d99052350b52197143f793855b78185494b3485`) ; ordre de course v3 (`b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22`) ; préenregistrement court v6, tiré de `origin/main` (`7e240c8c9b059171e06b416d5cf8b14c6822978f84219ad2d9770a32f90f11c5`).

## 0. Verdict

1. **Je recommande (b), sous une forme précise que j'appelle « (b) dérivée »**, confiance 0,7 : la partie servie est un fichier à part, sans en-tête, **tiré une fois de la question v4 par extraction à l'octet**, scellé avec un journal de dérivation ; la question v4 n'est pas récrite et ne le cite pas ; c'est l'additif et le préenregistrement court v7 qui le nomment par son empreinte. Aucun lanceur n'ouvre jamais le fichier de la question.
2. (a) avec l'empreinte des octets est sûre aussi. Elle perd sur trois points : le découpage est rejoué à chaque départ, dans chaque lanceur (la course, les deux sondes de refus, l'épreuve des témoins) ; une zone « titre de début, titre de fin » ne sait pas dire la partie servie que le contre-lecteur recommande lui-même à sa remarque 2 ; le fichier qui porte les données internes reste ouvert par le programme qui parle aux fournisseurs.
3. (b) telle que le rédacteur l'écrit (« que la question cite par son empreinte ») et (c) demandent toutes deux une question v5, donc une empreinte de plus sous le préenregistrement. À écarter pour ce coût ; (c) aussi pour la provenance.
4. **La garde de motifs est un filet, non la garantie.** Elle attrape des formes connues ; elle ne voit ni une description interne sans identifiant, ni ce qu'un texte révèle par son sens. La garantie vient de ce que chaque pièce fixe servie est petite, lue une fois en entier comme « texte qui part », et gelée par son empreinte.

## 1. Deux faits des textes qui pèsent sur le choix

- **La partie servie n'est sans doute pas une zone d'un seul tenant.** Le préenregistrement v6 dit « servie telle quelle (§ 4 de la question), avec ses cases et ses champs fermés (§ 5) ». La lecture que le contre-lecteur recommande (remarque 2, confiance 0,6) est : le § 4, les trois valeurs de la case, et les deux paragraphes du § 5 sur les champs d'une fiche, sans la table des axes ni sa colonne « source ». Ces deux paragraphes ne commencent par aucun titre. Sa recommandation (a), « titres de début et de fin », ne peut donc pas porter sa propre lecture de la remarque 2 sans ancres plus fines que des titres. Servir le § 5 entier dirait de plus aux proposeurs qu'une famille de cases est tenue à l'écart.
- **L'arrêt n° 14 du v6 ne couvre pas tout ce qui part.** Sa liste est : question, additif, configuration, tirage, le préenregistrement et son complément. La pièce d'antériorité servie et les témoins plantés n'y sont pas. Quelle que soit la voie, le v7 doit les y mettre.

## 2. Les voies, une par une

| | (a) zone et empreinte des octets à l'additif | (b) dérivée : fichier à part, tiré de la v4 | (b) du rédacteur : fichier cité par la question | (c) fichier entier, en-tête vidé |
|---|---|---|---|---|
| rien d'interne ne part | oui, par deux barrières : l'empreinte des octets découpés, puis la garde de motifs. Tient à ce que l'empreinte soit calculée après le découpage, sur ce qui part vraiment | oui, par trois barrières : le fichier ouvert ne contient rien d'interne ; son empreinte ; la garde de motifs. Une faute de découpage ne peut pas faire partir l'en-tête : il n'est pas dans le fichier | comme (b) dérivée | oui pour les motifs ; mais les § 2, § 3, § 6 et § 7, écrits pour la mère, le portier et les lecteurs, partent aussi |
| provenance de ce qui part | forte : ce qui part est une tranche de la question scellée | forte si le journal de dérivation existe : empreinte de la source, ancres ou lignes de chaque zone, empreinte de la sortie, commande rejouable ; la contre-lecture rejoue et compare à l'octet | forte, portée par la question | perdue dans le fichier servi ; à reporter dans une pièce sœur, ce qui revient à (b) à l'envers |
| contrôle mécanique au départ | redécouper, recalculer, comparer : un découpeur dans chaque lanceur | deux empreintes à comparer (question, partie servie) ; aucun découpeur au départ. L'égalité « extraction de la v4 = partie servie » est un fait entre deux empreintes gelées : vérifiée une fois à la contre-lecture, elle tient tant que les deux empreintes tiennent | comme (b) dérivée | une empreinte |
| pièces neuves | aucune ; le découpeur et ses essais entrent dans le véhicule | une petite pièce scellée et son journal ; aucun programme neuf si l'extraction se fait par lignes avec une commande ordinaire consignée au journal | la même, plus une question v5 | une question v5 |
| contre-lectures | celles du véhicule et de l'additif, déjà prévues ; le découpeur s'y ajoute, dans chaque lanceur | un rejeu de l'extraction et une lecture entière de la pièce, que la contre-lecture du v7 peut porter (la pièce est dans sa table des documents) | le même, plus le contrôle du différentiel v4 → v5 | contrôle du différentiel v4 → v5 |
| risque d'écart entre deux fichiers | aucun fichier second ; mais plusieurs découpeurs (course, sondes, épreuve des témoins) peuvent diverger entre eux, ce que l'empreinte attrape au départ | nul si le fichier est tiré par extraction et jamais écrit à la main ; un écart ultérieur change une empreinte et l'arrêt n° 14 refuse | le même | sans objet |
| arrêt n° 14 | s'étend aux « octets à servir » : une empreinte qui n'est celle d'aucun fichier, recalculée par le lanceur | s'étend à un fichier de plus : même mécanisme que pour les autres pièces scellées | le même | inchangé |
| sonde de refus | chaque sonde doit découper comme la course ; la sonde de l'espèce 6 est une ligne à part, sur un lanceur minimal : un second découpeur | chaque sonde lit le même fichier, à la même empreinte : « la question, telle qu'elle est servie » devient un objet unique et nommé | le même | la sonde porte le fichier entier |
| empreinte de la question | v4, `47160d37…` | v4, `47160d37…` | une v5 | une v5 |

Autre voie regardée et écartée : recopier le texte servi dans l'additif ou dans la configuration. Ce serait deux copies du § 4 sans lien mécanique. L'additif et la configuration doivent citer la partie servie par chemin et empreinte, jamais en porter le texte.

## 3. Ce que « (b) dérivée » demande exactement

1. Le directeur du programme tranche d'abord **quelle** partie est servie (remarque 2 du rapport ; hors de ce mandat). La voie tient dans toutes les lectures, y compris une partie faite de plusieurs zones.
2. La mère fait tirer la partie servie de la question v4 scellée : une ou plusieurs zones, données par leurs lignes, copiées à l'octet, mises bout à bout dans l'ordre, sans aucune transformation (les chevrons de citation du § 4 restent). Le fichier porte la version dans son nom. Il n'a pas d'en-tête : sa provenance vit dans son compagnon et dans un **journal de dérivation** (empreinte de la source, lignes de chaque zone, empreinte de chaque zone et de la sortie, commande). Le journal est interne ; il ne part jamais.
3. Un contre-lecteur d'un autre modèle rejoue l'extraction, compare à l'octet, et lit la pièce en entier comme un texte qui part chez des fournisseurs. Puis la mère la scelle.
4. La question v4 n'est pas touchée. L'additif, la configuration et le v7 citent la partie servie par chemin et empreinte.
5. Aucun lanceur, aucune sonde, aucune épreuve n'ouvre le fichier de la question pour en servir quoi que ce soit ; ils en vérifient seulement l'empreinte.

## 4. Ce que chaque voie impose au préenregistrement court v7

Commun à toutes les voies (le v7 est dû de toute façon : le v6 ne vaut que pour la question `2cf2aae0…`) :

- la table des documents nomme la question v4 ; la racine des graines est fixée en toutes lettres avant tout calcul du tirage (nœud de la remarque 6, que le choix entre (a) et (b) dérivée ne touche pas ; (b) du rédacteur et (c) le rouvriraient, par une empreinte de plus) ;
- le point 1 de « Hypothèse » dit sans ambiguïté ce qui part de la question, et le point 4 emploie le même nom ; la sonde de l'espèce 6 dit « la partie servie, et rien d'autre » ;
- l'arrêt n° 14 s'étend à **toute pièce fixe servie** : la pièce d'antériorité dans sa version neuve expurgée, les témoins plantés, la liste gelée des motifs et le programme de la garde ;
- un **arrêt neuf, « motif interdit dans un texte à servir »** : départ ou appel refusé, arrêt nommé, aucune ligne retirée ni récrite en silence ; épreuve sur un cas sain et sur un artefact pour chaque famille de motifs ; il vaut pour la course, les deux sondes de refus et l'épreuve des témoins. Il est distinct de l'arrêt n° 9, qui garde les étiquettes interdites du registre ;
- « Ce qui reste à écrire avant l'allumage » reçoit : la version neuve de la pièce d'antériorité, la garde et sa liste ; les bornes en octets se mesurent sur ce qui part vraiment ;
- le renvoi de l'ordre de course v3 à « la question scellée » (§ 1, § 3, § 4) est porté par le v7 et un erratum d'une ligne à l'ordre.

En plus, pour (a) : le v7 gèle les ancres de la zone et l'empreinte des octets à servir ; l'arrêt n° 14 dit que cette empreinte est recalculée après le découpage, sur les octets remis au relais ; l'épreuve de l'arrêt porte un artefact « découpage décalé d'une ligne ». En plus, pour (b) dérivée : le v7 nomme la partie servie et son journal dans la table des documents ; l'arrêt n° 14 reçoit un fichier de plus ; « Ce qui reste à écrire » reçoit l'extraction, son rejeu et son scellement ; le v7 écrit qu'aucun programme n'ouvre la question pour la servir.

## 5. Ce que la garde de motifs doit couvrir, dans tous les cas

**Où elle se place.** Au dernier point avant l'envoi, sur la requête assemblée : tous les champs de texte du corps (consigne de système, messages, tout champ libre) et tout en-tête que le véhicule ajoute. Une garde posée sur les pièces une à une laisse passer ce que l'assemblage ajoute. Elle se joue aussi une fois sur chaque pièce fixe, au scellement.

**Sur quoi.**

| texte | nature | ce qu'il faut |
|---|---|---|
| partie servie de la question | fixe | garde au scellement et au départ ; lecture entière |
| synthèse d'antériorité servie | fixe | **version neuve expurgée, sous un nom neuf** (la version actuelle porte le prénom du directeur, des identifiants, des chemins, une empreinte, des noms de clés et de familles de modèles ; contre-lecture, § 7) ; garde ; lecture entière par un autre modèle avant l'attestation « aucune recette » de la mère ; empreinte à l'arrêt n° 14 |
| consigne de rôle et préambule (proposeur, portier, juges) | fixes, à écrire | écrits sans aucun renvoi interne dès l'origine ; garde ; ils ne nomment ni la composition, ni les autres espèces, ni les clés, ni les plafonds |
| case servie | fixe après le tirage | l'identifiant servi est neutre (un triplet ou un rang), jamais un nom de fichier ni une graine ; garde sur le tirage scellé |
| registre des tentatives, générations 2 et 3 | produit en course, à partir de sorties de modèles | garde sur chaque ligne, à chaque génération, en plus de l'arrêt n° 9 ; un motif trouvé arrête la génération suivante, sans retrait silencieux |
| fiches relayées au portier et aux juges ; témoins plantés | produit en course ; fixes | même garde ; les témoins sont écrits sans renvoi interne et scellés |
| requêtes des sondes de refus | fixes | même partie servie, même garde, même empreinte |

**Quels motifs**, en deux familles, la liste étant gelée par son empreinte avant le départ :

- *Identité et dépôt*, stricts sur tout ce qui part : prénom et nom du directeur, nom du compte distant et du dépôt, identifiants de session, adresses de courriel, noms des clés et de leurs variables, identifiants de registre, d'accord et de décision, chaînes hexadécimales de seize caractères et plus, chemins du dépôt, nom du fichier des consignes permanentes.
- *Composition et tenue*, stricts sur les pièces fixes : noms de fournisseurs et de familles de modèles, désignations « modèle F », « modèle O », numéros d'espèce, noms de règles du dépôt, « commit », noms de fichiers. Sur les textes produits en course, cette famille peut toucher un texte légitime (une fiche qui cite une adresse publique à son champ de voisin) : la conduite sur ces textes est à écrire d'avance et à éprouver sur un tel cas. Je recommande l'arrêt nommé avant la génération suivante, comme l'arrêt n° 9, plutôt qu'un simple compte.

**Comment.** Casse repliée, accents retirés, forme Unicode normalisée, bornes de mots pour les noms courts. Témoin positif **pour chaque motif**, sans exception : la contre-lecture note que le motif du nom de famille n'en avait qu'un indirect. La liste des motifs porte le prénom et le nom : elle est elle-même une donnée interne, jamais servie, masquée à l'affichage et dans les journaux.

**Ce qu'elle ne couvre pas, à dire dans le v7.** Les noms descriptifs de pièces internes (remarque 3), ce qu'un texte révèle par son sens (l'existence d'une famille tenue à l'écart, la composition), toute forme de donnée interne que la liste n'a pas prévue. C'est la lecture entière de chaque pièce fixe qui en répond.

## 6. Recommandation, confiance, défaut

- **Recommandation : (b) dérivée.** Confiance **0,7**. Raisons, par ordre de poids : un seul objet nommé pour « la question telle qu'elle est servie », lu par la course, les deux sondes et l'épreuve des témoins ; aucun découpage au départ ; le fichier aux données internes n'est jamais ouvert par un programme qui parle à un fournisseur ; elle porte une partie servie en plusieurs zones ; l'arrêt n° 14 garde son mécanisme ; la question reste la v4.
- **Son coût réel** : une pièce scellée de plus et un rejeu d'extraction. Pas de question v5, pas de programme neuf.
- **Ce qui me ferait passer à (a)** : que le directeur retienne une partie servie d'un seul tenant, bornée par deux titres, **et** que le véhicule n'ait qu'un seul chemin de code pour assembler toute requête, sondes et épreuve comprises. (a) vaut alors (b) dérivée, avec une pièce de moins.
- **Accord avec le contre-lecteur** : sur le fond, entier. Son ajout décisif, l'empreinte des octets exacts, est gardé dans les deux voies ; la garde sur tout texte servi aussi. L'écart porte sur l'endroit où le découpage se fait : une fois, hors ligne, rejoué par un autre modèle, ou à chaque départ.
- **Défaut proposé** : (b) dérivée pour écrire le mandat du véhicule, l'additif et le v7. Ce défaut ne fait rien partir : ce qui est servi à un agent est un nœud du directeur, et le v7 est une pièce décisive qu'il voit avant tout allumage.

## 7. Limites de cet avis

- Je n'ai lu ni le code du véhicule, qui n'existe pas, ni la synthèse d'antériorité, ni l'additif. Ce que je dis du nombre de lanceurs vient du v6 (« lanceur », « sonde […] sur le modèle de la sonde minimale », « épreuve réelle des témoins plantés »).
- Je ne tranche ni la remarque 2 (quelle partie), ni la remarque 6 (racine des graines).
- Aucune empreinte de la partie servie n'est donnée ici : elle n'existe pas tant que la remarque 2 n'est pas tranchée. L'empreinte du § 4 que rapporte la contre-lecture (`44bf5202…`, titre compris) vaut pour sa propre découpe seulement.

— concepteur neuf, modèle F
