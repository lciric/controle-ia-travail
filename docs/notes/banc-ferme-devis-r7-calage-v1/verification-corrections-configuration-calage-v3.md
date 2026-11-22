# Vérification des corrections de la configuration du calage v3

- **Objet** : la configuration de génération du calage de la porte G1, v3 (pièce de classe A), et sa note v3. Cette pièce vérifie ; elle ne corrige rien et ne tranche aucun nœud.
- **Qui** : la session fille ouverte par la mère pour le mandat `docs/notes/attaquant-informe-v1/course-brouillon17-v1/mandat-fable-devis-r7-calage-v2.md` (`6ec252bc942d0f8d68b805c90c877bf4d42354eee216316db6b34061825f6559`), identifiant `session_01XJ6MgnAtxhP88svZfgPvUa`, dans le rôle de concepteur que ce mandat lui donne. Elle n'a écrit ni la configuration, ni sa note, ni leurs corrections, ni le texte du banc fermé, et n'a conçu aucun moniteur.
- **Quand** : 22 novembre 2026, de 14:28 à 15:00 UTC (`date -u`).
- **Décisions qui la fondent** : GO-2026-11-21-77 (« go configuration du calage ») ; GO-2026-11-22-73 (machine virtuelle Vast.ai en Europe pour la coupure du réseau, plafond de 29 €), tel que le mandat le rapporte.
- **Refus d'un classifieur de sûreté** : aucun.

## Verdict

**« Accepté avec mineurs résiduels ».**

Les deux corrections demandées par la relecture sont portées mot pour mot, et rien d'autre ne change : aucune valeur de génération, aucune source, aucune pièce citée. Deux résiduels mineurs, que le correcteur avait lui-même signalés, sont à porter à la version qui sera scellée (§ 1.3).

Ce verdict porte sur les corrections. **Le scellement, lui, attend deux choses** : les noms internes « v2 » que la v3 garde encore, et les quatre accords avec le texte du banc fermé, qui restent entiers dans son brouillon 17 et dont trois changent avec la machine accordée (§ 2 et § 3).

## Pièces jugées, à leur empreinte

| Pièce | Chemin (branche `main`, commit `a5badd95c8c8567dd4ec290c054a07d7730381af`) | Empreinte (sha256) |
|---|---|---|
| configuration v3 | `prereg/configuration-generation-calage-g1-v3.json` | `28cf908f412fc2c777613a0971bb451868a469fb47818ee90e952b44997e90e9` |
| note v3 | `docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v3.md` | `f26cbb42e04617c14d88105bde8ab7fa818fdc3fe1db9187c70c5a3bb2285544` |
| relecture de la v2, verdict « à corriger » | `docs/notes/relecture-fable-api-v1/relectures/4-configuration-calage-g1/relecture-fable-api.md` | `381053520a1487585912487790af594aa1d3a467daefc8724961572718fa3287` |
| configuration v2, lue par différence seulement | `prereg/configuration-generation-calage-g1-v2.json` | `9bc08d00613ac9f55e098e264df6ec9045d63f5252c44e88dde0dd4aa768f368` |
| note v2, lue par différence seulement | `docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v2.md` | `2b8ef38c1823c57909d47d40c6b3c3d6c1ee765c0a38043f253cda0230877436` |
| programme de validation v2 | `docs/notes/configuration-calage-g1-v1/valider_configuration_calage_v2.py` | `9b4cff87083aea0188f0f441596b175ae64c31bc504749ee1cd74161012436d3` |
| programme de l'opérateur | `docs/notes/configuration-calage-g1-v1/empreinte_gabarit_calage_v1.py` | `7c3a541a38a4c33e679779802f0fae9e58a1c548a4557dd8f02cdcae88119640` |
| texte de la course du banc fermé, brouillon 17 | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/course-banc-ferme-v1-brouillon17.md`, branche `claude/loving-lamport-7ol5ws` | `cf5d35d8472137d30defedb2a61b375037d558e3937e4371cb5d8822a507a881` |
| coupure du réseau, autres voies | `docs/notes/attaquant-informe-v1/course-brouillon17-v1/coupure-reseau-autres-voies-champ-14-v1.md`, même branche | `b59dde76b05c6381d6ced0ec407e9a60245e729e01b55ef6c75fb15767ee8c77` |

Ce que cette vérification a produit, dans `docs/notes/banc-ferme-devis-r7-calage-v1/` :

| Pièce | Chemin | Empreinte (sha256) |
|---|---|---|
| programme de contrôle (classe B, à contre-lire) | `verification-configuration-v3/comparer_configurations_calage_v1.py` | `b58aebff9daeed2773aa5e34dd928529e0289d6db9389b7dda9f55830c4aa5c2` |
| sa sortie sur les pièces réelles | `verification-configuration-v3/comparer_configurations_calage_v1-sortie.txt` | `2ab744d216733aae1e5802b78e71efb6903df3a83b4211db7c57860263d2819a` |
| ses épreuves sur trois artefacts (R5) | `verification-configuration-v3/comparer_configurations_calage_v1-artefacts-sortie.txt` | `f041caf2076b9b0d9d5ee4f2df42a1a85ddfddb6f8b645e646dc298c0cefe23e` |
| rejeu du programme de validation v2 sur la v3, par le vérificateur | `verification-configuration-v3/rejeu-validation-configuration-v3-par-le-verificateur-sortie.txt` | `0b9673bc9bed3e7a00806798721380adc7bbf61d8277222063c1d3735e33e605` |
| relevé des offres de Vast.ai du 22 novembre, 14:45 UTC | `releves-2026-11-22/vast-offres-une-carte-24go-extrait.json` | `fc3fc0c60565cf56d2d146b9be8c217fd36abe06356b587d8ff0593a4fc0efdc` |

## 1. Table point par point

### 1.1 Les deux corrections demandées

| Point | Ce que la relecture demandait | Constat | Comment c'est établi |
|---|---|---|---|
| Correction 1, la règle | remplacer la cinquième règle de lecture par un texte qui écrit la dispense des deux entrées d'absence (`echantillonnage.troncature`, `outils.outils_exposes`) | **portée mot pour mot** | égalité stricte de chaînes entre la règle de la v3 et le texte de la relecture (sa ligne 32) : programme de contrôle, § 3 de sa sortie |
| Correction 1, point voisin | « s'il traite ce couple à part », ajouter après la phrase des dispenses la phrase sur le quantile (« q99 », lu comme 0,99) | **portée mot pour mot, à l'endroit demandé** ; la condition tient | même égalité stricte (ligne 36 de la relecture). Condition lue sur le programme de validation : `STATISTIQUES = {"max": None, "q99": 0.99}` (l. 59) ; `CLES_JSON`, entrée du quantile, qui lit `statistique_equivalence` et la convertit (l. 118) |
| Correction 1, les deux gardes | la dispense n'est acceptable qu'« une fois les deux gardes vues dans le programme » | **vues** | `FIXEES_PAR_UNE_GARDE` (l. 124-127) ; garde de la troncature (l. 405-406) ; garde des outils (l. 601-603). Les deux artefacts du correcteur (troncature « top-p 0,9 », outil `["lire_piece"]`) sont refusés chacun par sa garde (`rejeu-validation-configuration-v3-sortie.txt`, `8cf2e4413615bed76f120244d98b71ae3698d5f0045f6a452bc6e5ae54e6be17`) |
| Correction 2, verdict de la note | « Un nœud ouvert s'y ajoute, sur les fichiers des fonctions de montage (§ 9). » | **portée mot pour mot** ; « de classe B » est retiré | la phrase clôt le paragraphe du verdict ; l'ancienne n'y est plus : programme de contrôle, § 4 |
| Correction 2, titre | « ## 9. Nœud ouvert de la v2 (m4) » | **porté mot pour mot** | même paragraphe de la sortie |

### 1.2 « Et rien d'autre »

| Point | Constat | Comment c'est établi |
|---|---|---|
| Configuration, différences de la v2 à la v3 | **12 différences, toutes de tenue de version ou de la cinquième règle** : `version` ; `remplace` (chemin, empreinte) ; `corrections` (relecture, empreinte, `portees`, celles de la v2 rangées sous `corrections_de_la_v2`) ; `statut` ; `auteur` ; `date_utc` ; `regles_de_lecture`, cinquième règle | comparaison clé par clé, § 1 de la sortie |
| Configuration, le reste | **identique** : les 69 entrées de `parametres`, l'accord avec le banc fermé, ce qui reste ouvert, les 33 pièces citées, les pièces lues sans être sources, la portée, les six autres règles | même sortie, onze contrôles « tenu » |
| Configuration, texte brut | 10 lignes retirées, 15 ajoutées ; aucune clé écrite deux fois | § 2 de la sortie |
| Note, différences de la v2 à la v3 | hors des deux remplacements : titre ; en-tête ; table des corrections de la v3 et ses puces ; pièces livrées ; épreuves ; ce que le correcteur de la v3 a lu (§ 7) ; les recommandations de la relecture recopiées (§ 3 point 9, § 8, § 9). La note les déclare toutes (« Tenue de version, hors correction ») | différence ligne à ligne, lue en entier |
| Recommandations recopiées | **fidèles** : nœud 1 (a) à 0,7 ; nœud 2 (a) sous condition de mesure ; nœud 3 (a) à 0,85 ; nœud 4 (a) à 0,8 ; type conservé, 0,6 ; fichiers de montage, option 2 à 0,6 et ses cinq motifs ; dispense, 0,8 | rapprochement avec la relecture, l. 78 à 91 |
| Programme de validation v2 sur la v3 | **« configuration valide »** (cas sain et contrôle de lancement) ; épreuves : 5 cas sains et 62 artefacts, tous réussis ; 69 entrées, 211 sources relues, 33 pièces à leur empreinte | rejeu indépendant du vérificateur, 14:51 UTC, Python 3.13.18, numpy 2.5.3 ; il concorde avec les deux sorties du correcteur (`d79f4201…`, `8cf2e441…`) |
| Programme de contrôle du vérificateur | éprouvé sur un cas sain et trois artefacts (une température changée ; un mot de la règle changé ; la note v2 à la place de la v3) : les trois sont refusés | sortie des artefacts |

### 1.3 Les réserves du correcteur, jugées

| Réserve | Constat | Jugement |
|---|---|---|
| (i) La v3 garde les noms internes de la v2 | Vrai, et la conséquence est plus large que ne le dit la note. Le relevé de l'opérateur porte l'empreinte de la configuration qu'on lui donne (`empreinte_gabarit_calage_v1.py`, l. 447). Le programme de validation exige que cette empreinte soit celle de la configuration validée (l. 708) et l'exige égale entre postes (l. 94). Son chemin par défaut est la v2 (l. 1035). Donc, jouée telle que la v3 l'écrit, la commande de l'opérateur lit la v2 : le relevé est lié à la v2. Validé avec le chemin de la v3, il est refusé (« relevé établi pour une autre configuration »). Validé sans option, il passe, et **toute la chaîne tourne sur la v2 sans un défaut**, alors que les champs n° 1 et n° 2 du banc citeraient la v3 | **Résiduel mineur, à corriger avant le scellement.** Mineur : aucune valeur de génération ne diffère entre la v2 et la v3. À corriger : le fichier « ne change plus » une fois scellé, et une commande fausse dans une pièce scellée oblige, le jour du relevé, à un écart au texte scellé. Remplacements à porter, que cette pièce ne porte pas : (1) dans `gabarit_de_conversation.empreinte.methode.commande`, le chemin de la configuration (1 occurrence) ; (2) le numéro de version dans les noms des relevés (13 occurrences : six noms par poste, sept noms du relevé de référence) ; (3) dans `releve_de_reference.comparaison`, écrire l'option `--configuration` et son chemin. « (nœud ouvert de la note v2) » reste exact : rien à changer |
| (ii) `requirements-cpu.txt` a changé depuis le commit de lecture | Vrai : quatre lignes ajoutées (`anthropic`, `pypandoc_binary`, deux commentaires). Les six versions figées que cite la configuration sont inchangées (lignes 2 et 7 à 11). Le programme relit le fichier au commit de lecture et ne signale qu'un avis | **Sans conséquence.** À dire au scellement : l'empreinte citée (`bc86590f…`) est celle du commit de lecture `4814dc47…`, non celle de `main` (`04491d02…`) |

### 1.4 Les choix « à faire valider avec les entrées », et le nœud des fichiers de montage

Avis du vérificateur, sans trancher ; aucun ne change une valeur de génération.

| Choix | Avis | Confiance |
|---|---|---|
| La dispense des deux entrées d'absence | à accepter : les deux gardes sont vues, et rejouées | 0,85 |
| Le seuil de 40 caractères ; `conversion` ; le douzième artefact ; « source JSON sans clé désignée = défaut » | à accepter tels quels | 0,8 |
| `comparaison` (commande d'un programme de classe B sans chemin ni empreinte) | à accepter, avec l'option du § 1.3 (3) | 0,8 |
| Le nom du relevé de référence | à accepter, après le remplacement du § 1.3 (2) | 0,8 |
| `unicite` (« il ne se remplace que par une version nouvelle de ce fichier ») | à accepter, **en sachant ce qu'elle coûte sur une place de marché** : l'hôte du poste de calage peut retirer son offre entre deux locations ; un relevé de référence à refaire sur un autre hôte oblige alors à une version nouvelle de la configuration et du texte du banc | 0,6 |
| Les fichiers des fonctions de montage (nœud ouvert de la note, § 9) | option 2, ne pas geler, comme la relecture. Son motif du coût tombe (une version nouvelle vient de toute façon), mais les autres tiennent : `manifeste.py` devra changer pour déclarer le type conservé, et geler ne garde rien si un lanceur reproduit ces fonctions | 0,6 |

## 2. Les quatre points à accorder avec le texte du banc fermé

Le brouillon 17 du banc (`cf5d35d8…`) est comparé à la configuration v3. La note v3 avait lu le brouillon 14 : **ses quatre écarts sont entiers dans le brouillon 17**, aux lignes 351, 358 à 360 et 378.

« La machine accordée » : une machine virtuelle Vast.ai, carte de 24 Go, en Europe. Le relevé du 22 novembre à 14:45 UTC compte 389 offres à une carte d'au moins 24 Go de mémoire (vérifiées, louables ; filtre à 23 000 Mo) ; **15 seulement acceptent une machine virtuelle**. En 24 Go : deux RTX PRO 4000 au Québec, une RTX 4090 au Danemark (0,51 USD de l'heure), une RTX 4090 en Roumanie (0,69 USD). **Aucune des 17 offres d'A100 SXM4 n'accepte une machine virtuelle.** L'offre à 0,243 USD citée par la note sur la coupure du réseau n'est plus au relevé.

| Point | Ce que fixe la configuration v3 | Ce que dit le brouillon 17 du banc | Jugement | Ce qu'il devient avec la machine accordée |
|---|---|---|---|---|
| **Le lot** | huit épisodes joués ensemble (`episode.lot`, repris de la configuration scellée du premier test) | « les deux membres passent l'un après l'autre » (l. 358) ; l'agent agit « pour chaque épisode » (l. 359) ; aucun lot n'est dit | écart entier ; l'un des deux textes doit rejoindre l'autre (nœud B) | **Le lot de huit n'est pas établi sur 24 Go.** Estimation du vérificateur, à mesurer : poids, 16,1 Go ; mémoire d'attention du lot au contexte le plus long (8 épisodes de 5 900 positions environ), 6,2 Go ; calculs transitoires, 3 à 4 Go ; soit 25 à 26 Go pour une carte de 25,8 Go. Un épisode long peut donc tomber en panne de mémoire au milieu d'une course qui ne se rejoue pas |
| **Le lieu de lecture des activations** | une passe unique sur la transcription entière, en fin d'épisode, seule dans son lot et sans cache ; couches 7, 15 et 23 | chaque position « à son premier passage dans le modèle », à chaque couche (l. 360) ; un recalcul par passe unique « serait une autre course » | écart entier, et c'est le plus lourd : les sondes et le calage lisent la passe unique (nœud C) | La mémoire suffit : la passe unique se fait un épisode à la fois. **Le volume, lui, ne tient pas** : à toutes les couches et à toutes les positions, en float32, 0,5 Mo par position, soit 2,4 à 3,4 Go par épisode. Le choix des couches et du type conservé devient un nœud du devis (réserve 3 du texte du banc, l. 581) |
| **L'identité entre les deux postes** | toutes les entrées valent pour les deux postes, relevé de l'opérateur compris ; la note propose en plus une génération sous la même graine, comparée jeton à jeton | trois épreuves sans génération (pile déclarée, gabarit, pile numérique ; l. 349 à 351) ; l'épreuve de pile déclarée ne nomme ni le processeur ni le relevé ; la tolérance s'applique « à chaque couche enregistrée » ; la clé de graine est « (3,) », sans clé par épisode (l. 378) | écart entier (nœud D) ; trois précisions restent à porter au texte du banc (§ 4) | L'identité ne se tient qu'entre deux postes du même type de carte, du même modèle de processeur et de la même image. **Sur une place de marché d'hôtes, c'est en pratique la même machine hôte.** Les deux RTX 4090 d'Europe sont chez deux hôtes aux processeurs différents (AMD EPYC 7B12, AMD EPYC 7B13) |
| **La machine** | même type de carte, une seule carte, même modèle de processeur ; domaine où la garde d'équivalence est revalidée : A100 SXM4 de 80 Go, AMD EPYC 7513 ; hors de ce domaine, « nœud : revalidation de la garde d'équivalence sur le poste choisi, ou réserve écrite » | poste de calage : champ n° 19, à remplir (l. 348) ; machine du banc : champ n° 14 | la configuration ne choisit pas la machine ; elle pose une règle, que le champ n° 19 doit suivre (nœud A) | **La machine accordée est hors du domaine revalidé : la règle du fichier lui-même en fait un nœud.** La recommandation d'origine (A100 SXM4 de 80 Go des deux côtés) n'est plus possible en machine virtuelle Vast.ai. Et le poste de calage est celui de la campagne de calage de G1 : la carte du banc engage la carte de cette campagne |

## 3. Points qui demandent un mot du directeur du programme

Ordre conseillé : A, puis B, C et D ; E en dernier, puisqu'il recueille ce que les autres changent.

### Nœud A. La carte des deux postes, maintenant que le banc est une machine virtuelle Vast.ai

- **Décision** : quelle carte pour le banc et pour le poste de calage (champs n° 14 et n° 19).
- **Enjeu** : la machine accordée sort du domaine où la garde d'équivalence a été revalidée, et elle fixe du même coup la carte de la campagne de calage de G1, qui porte environ les deux tiers des épisodes de G1.
- **(a) La carte du banc pour les deux postes.** Le poste de calage est une machine du même type de carte, du même modèle de processeur et de la même image. La garde d'équivalence est revalidée sur cette carte pendant la répétition à blanc, sous un texte court contre-lu qui reprend tel quel le critère de la revalidation du pilote ; la version définitive de la configuration écrit ce domaine.
  - Avantage : tient dans la machine accordée ; l'identité jeton à jeton est vraisemblable entre deux instances d'un même hôte.
  - Inconvénient : la campagne de calage de G1 devra tourner sur ce type de carte, ou refaire la vérification de concordance contre les huit épisodes scellés ; l'hôte peut quitter le marché entre deux locations.
- **(b) L'A100 SXM4 de 80 Go des deux côtés**, comme la note et la relecture le recommandaient.
  - Avantage : domaine revalidé, rythmes connus, offres déjà employées par le programme.
  - Inconvénient : aucune n'est offerte en machine virtuelle ce jour ; il faudrait une autre voie de coupure du réseau, donc rouvrir le champ n° 14 et le plafond de 29 €.
- **(c) Deux cartes différentes, sous réserve écrite.**
  - Avantage : rien ne bouge.
  - Inconvénient : la concordance ne vaut au mieux qu'« en loi » ; la loi exacte du taux de fausses alertes ne s'applique plus aux épisodes de la famille, qui ne se rejoue pas.
- **Recommandation** : (a), confiance 0,6, **confirmée ou non par la répétition à blanc**, qui mesure sur la machine réelle la mémoire au lot retenu, la garde d'équivalence et l'identité entre deux instances. Si l'une des trois mesures échoue, le nœud revient avec (b).
- **Défaut** : aucun. C'est une dépense et une sortie du domaine revalidé.

### Nœud B. Le lot

- **Décision** : huit épisodes ensemble des deux côtés, un par un des deux côtés, ou un lot plus petit.
- **Enjeu** : le lot fait partie de la pile ; les deux textes ne disent pas la même chose, et 24 Go ne garantissent pas le lot de huit.
- **(a) Lot de huit des deux côtés** ; le texte du banc rejoint le fichier.
  - Avantage : aucune valeur du fichier ne change ; le calage garde le plan des courses passées.
  - Inconvénient : à mesurer sur 24 Go ; s'il ne tient pas, il demande la carte de 48 Go, hors du plafond accordé.
- **(b) Un lot plus petit, le même des deux côtés**, le plus grand qui tient au contexte le plus long ; au besoin un par un.
  - Avantage : tient sur 24 Go.
  - Inconvénient : une valeur du fichier change, donc une version nouvelle ; le calage de G1 ralentit d'un facteur non mesuré.
- **(c) Deux plans différents, sous réserve.**
  - Inconvénient : l'échangeabilité s'affaiblit sans gain.
- **Recommandation** : (a) si la répétition à blanc montre que le lot de huit tient au contexte le plus long ; sinon (b). Confiance 0,6. La mesure se fait sur un épisode forcé à dix actions de 400 jetons, et non sur un épisode anodin court. La condition que posait la contre-lecture — mesurer l'effet du lot avant de trancher — se remplit pendant la même répétition.
- **Défaut** : aucun.

### Nœud C. Le lieu de lecture des activations sur le banc

- **Décision** : le banc enregistre la passe unique de fin d'épisode, ou garde le seul premier passage.
- **Enjeu** : les sondes scellées et le calage lisent la passe unique ; un moniteur gelé lirait sinon un autre chemin de calcul que son calage.
- **(a) Le banc enregistre la passe unique de chaque épisode.**
  - Avantage : les mêmes nombres des deux côtés ; coût en temps faible.
  - Inconvénient : le texte du banc change (l. 360) ; le volume dépend des couches gardées.
- **(b) Garder le premier passage seul.**
  - Inconvénient : aucun recalcul n'est permis sous ce texte ; la matière de la famille serait lue hors du chemin du calage.
- **Recommandation** : (a), confiance 0,85, inchangée. Les couches et le type conservé se décident avec le devis (`devis-banc-ferme-v1.md`, même dossier) : le volume « toutes les couches, toutes les positions » n'entre pas dans la machine accordée.
- **Défaut** : aucun.

### Nœud D. Identité exigée, ou concordance « en loi » acceptée

- **Décision** : exiger que les huit épisodes de référence se rejouent jeton à jeton sous la même graine, ou accepter une concordance en loi.
- **Enjeu** : la famille ne sert qu'une fois ; sur huit épisodes, « en loi » ne prouve pas l'échangeabilité au niveau d'une fausse alerte pour cent.
- **(a) Exiger l'identité.**
  - Avantage : un fait, sans seuil à défendre.
  - Inconvénient : impose deux postes du même type ; arrête tout si un détail diffère. Sur Vast.ai, cela se constate entre deux instances d'un même hôte, pendant la répétition à blanc, avant toute heure de la répétition générale.
- **(b) Accepter « en loi », sous réserve écrite.**
  - Avantage : la course part même sur deux machines différentes.
  - Inconvénient : la loi exacte ne vaut plus qu'en approximation.
- **Recommandation** : (a), confiance 0,7, inchangée. Le texte du banc ne porte aujourd'hui ni cette génération sous même graine, ni sa règle : elles sont à y écrire si (a) est retenue.
- **Défaut** : aucun.

### Nœud E. Quelle version sceller

- **Décision** : sceller la v3 telle quelle, ou une version définitive qui porte les résiduels du § 1.3 et ce que tranchent les nœuds A à D.
- **Enjeu** : jouée telle qu'écrite, la commande de l'opérateur lit la v2, et la chaîne peut tourner sur la v2 sans défaut ; le fichier ne change plus après scellement.
- **(a) Une version définitive, sous un nom neuf.** Le correcteur porte mot pour mot les remplacements listés ; la vérification se fait par différence, avec le programme de contrôle de cette pièce.
  - Avantage : la pièce scellée dit vrai ; une demi-heure de chaîne si aucune valeur ne change.
  - Inconvénient : un tour de plus.
- **(b) Sceller la v3, et écrire au texte du banc que l'opérateur passe le chemin de la version scellée.**
  - Avantage : pas de version nouvelle.
  - Inconvénient : une commande fausse reste dans une pièce de classe A ; le relevé de référence se fait en écart au texte scellé.
- **Recommandation** : (a), confiance 0,85. Les nœuds A et B peuvent changer une valeur du fichier (le domaine revalidé, le lot) : une version nouvelle est alors due de toute façon.
- **Défaut** : aucun. Le scellement d'une pièce de classe A demande le mot du directeur.

## 4. À porter au texte du banc fermé, sans décision

1. **Le relevé de référence.** La configuration veut que les champs n° 1 et n° 2 du banc citent son empreinte et celle du relevé de référence. Le brouillon 17 ne nomme ce relevé nulle part. Or il n'existe qu'après une heure payée sur le poste de calage, donc après le scellement du texte définitif. Proposition : son empreinte va à l'addendum scellé après la répétition générale, et le texte le dit.
2. **Le programme de l'opérateur n'a jamais tourné en réel.** Son premier jeu aurait lieu sur une machine payée. Proposition : l'éprouver d'abord sans carte, sur un poste qui porte les fichiers du modèle, pour ne pas le découvrir à prix payant.
3. **La clé de graine par épisode de la vérification de concordance**, `(3, k)`, à la place de « (3,) » (l. 378).
4. **L'épreuve de pile numérique** jugée aux couches 7, 15 et 23, les autres rapportées (l. 351) : la tolérance n'a été fondée qu'à ces trois couches.
5. **L'épreuve de pile déclarée** (l. 349) : y nommer le modèle de processeur, la comparaison des relevés, et le type des activations conservées.
6. Les champs n° 1, n° 2, n° 13 et n° 19 portent la mention « attend l'étalonnage du saboteur à budget ». Le vérificateur ne lit pas cet étalonnage et ne sait pas ce qu'il fixe : à rapprocher par la mère des nœuds A à C.

## 5. Ce qui a été lu, et ce qui ne l'a pas été

- **Lu en entier** : la relecture ; la note v3 ; la configuration v3 (toutes les entrées, les sources par leur lieu seulement) ; la note sur la coupure du réseau ; la note des champs. **Lu par différence** : la configuration v2 et la note v2.
- **Lu en partie** : du programme de validation v2, les lignes 50 à 62, 90 à 130, 398 à 410, 436 à 470, 596 à 606, 690 à 760 et 1018 à 1040 ; du programme de l'opérateur, ses lignes sur la configuration ; du brouillon 17 du banc, les déclarations D1 à D8, le plan d'analyse, les critères de lecture, l'esquisse de devis, les champs ouverts ; de `src/controle_ia/environnements/propositions.py`, les lignes 236 à 270 et la longueur de deux consignes, sans leur texte.
- **Non vérifié** : le programme de l'opérateur sur la v3 (il demande les dépendances du modèle) ; les essais du dépôt ; la vérification de l'arbre ; la mémoire réelle d'un lot sur 24 Go, qui n'est ici qu'une estimation.
- **Non lus, par consigne** : aucun résultat cloisonné ; rien sous `donnees/`, `archives-reponses-modeles/` ; aucune famille aveugle ; aucune pièce du scellement 2 ; aucun contenu de moniteur ; ni le lot, ni les sorties, ni les agrégats du banc fermé ; aucun fichier « consigne-privee » ni « conception-ii-b » ; la ligne R-2059.
- **Vu sans le chercher** : le programme de validation lit lui-même les pièces que cite la configuration, dont des textes scellés ; le vérificateur n'en a vu que les comptes et le verdict.

## 6. Pour rejouer

Depuis un arbre de `main` au commit `a5badd95c8c8567dd4ec290c054a07d7730381af` :

```
python3 -I <ce dossier>/verification-configuration-v3/comparer_configurations_calage_v1.py \
  prereg/configuration-generation-calage-g1-v2.json prereg/configuration-generation-calage-g1-v3.json \
  docs/notes/relecture-fable-api-v1/relectures/4-configuration-calage-g1/relecture-fable-api.md \
  docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v2.md \
  docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v3.md
python3 -B docs/notes/configuration-calage-g1-v1/valider_configuration_calage_v2.py \
  --configuration prereg/configuration-generation-calage-g1-v3.json [--lancement | --essai]
```

Le programme de contrôle est de classe B : il reste à contre-lire par un autre modèle.
