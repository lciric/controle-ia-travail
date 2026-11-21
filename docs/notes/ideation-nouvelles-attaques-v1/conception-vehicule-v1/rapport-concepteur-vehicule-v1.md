# Rapport du concepteur — véhicule de la course « nouvelles attaques » — v1

- Auteur : concepteur du véhicule, modèle F. Je n'ai écrit ni la v9, ni l'inventaire, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 06:45:57Z, après la lecture des pièces, avant l'écriture.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-conception-vehicule-course-nouvelles-attaques-v1.md`, `d2130f6b0aab5d4d32f01f51acd71b23cc3d1623769b24cd4d6fb06317c19af2`, égale à son compagnon ; lu en entier.
- Processeur seul : aucun appel à un fournisseur de modèles, aucune clé lue ni nommée par sa variable, aucune dépense, aucun code écrit pour être lancé, aucun lancement, aucune écriture dans un dépôt, aucun commit. Aucune sortie d'aucun modèle sur la question n'a été lue. Rien n'a été ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`.
- **Aucun refus de permission, de classifieur ni de garde n'a été rencontré.**

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/concepteur-vehicule-nouvelles-attaques/`. Chaque pièce a son compagnon `.sha256` ; les empreintes sont à la table jointe.

| pièce | objet |
|---|---|
| `conception-vehicule-course-nouvelles-attaques-v1.md` | choix de base, modules, interfaces, épreuves, lots, calendrier, ce que la lettre ne fixe pas |
| `rapport-concepteur-vehicule-v1.md` | ce rapport |
| `table-empreintes-concepteur-vehicule-v1.md` | les empreintes des pièces rendues et des pièces lues |

Exclues du versement : `lecture-registre-origin-main.md`, `lecture-go-origin-main.md`, et le sous-dossier `lu/`, qui ne porte que des copies de lecture.

## 2. Pièces lues, et leurs empreintes

### 2.1 Sur `origin/main` du dépôt de l'organisme

Par `git show` redirigé, après `git fetch origin main` ; commit `ebb7492a8a2923a6a790ee0f8d29ee320b530f3d` (l'inventaire lisait `31b493b6…` : la branche a avancé).

| pièce | empreinte recalculée | contrôle | lecture |
|---|---|---|---|
| préenregistrement court v9 | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | égale à l'inventaire | en entier |
| additif 1 à la v9, v5 | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` | égale à l'inventaire | en entier |
| complément de valeurs, lot 1, v3 | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` | égale à l'inventaire | en entier |
| additif 1 au complément v3, v2 | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` | égale à l'inventaire et à R-4356 | en entier |
| devis v11 | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | égale à l'inventaire | **en partie** : son § 10 (l. 351 à 462) |
| partie servie de la question v5 | `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` | égale à la V9 | en entier |
| ordre de course v3 | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` | égale à l'inventaire | en entier |
| erratum 1 de l'ordre de course v3 | `6a02accbca4f12cebd6a70a52c07dc4c41e0cb2cf44d1371be2299e456bc45e2` | égale à R-4266 | en entier |
| `registres/decisions.md`, copie de lecture | `2c30a433d5bef80a151689c29f47ddf71f2b7706e7c4c1afac0f07e42d9ca3ad` | recalculée sur la copie | l. 3832, 3999, 4170 à 4199, 4204, 4269, 4436 à 4509 ; recherches par mot |
| `registres/go.md`, copie de lecture | `38f63a0d40b591fb1890437107cdb77511916360e2bda0baddda70ff5986d63b` | recalculée sur la copie | l. 584 à 613 |

**Non lues** : la question v5 (le véhicule ne l'ouvre jamais ; moi non plus), le corps de la synthèse servie, la note de périmètre, les § 0 à § 9 du devis v11. Les compagnons de ces pièces n'ont pas été tirés : chaque empreinte est comparée à celle que cite une pièce scellée ou l'inventaire.

### 2.2 Sur le disque de la branche `lot/compte-organisme-v1` (commit `9555d8b696d3aae9d17a9c41399d0ab24704c530`)

Ces pièces **ne sont pas sur `origin/main`** au commit lu.

| pièce | empreinte recalculée | contrôle | lecture |
|---|---|---|---|
| inventaire de l'allumage | `0737906f9901de39ddd9b1585679b5b44e6bac67e7051a10374d3e0e496c06e0` | égale au compagnon | en entier |
| gabarit des témoins plantés | `a84de0bf3168d93dda6928e2e165c14ecb8b091e976a629ace828813c24c89c0` | égale au compagnon | en entier |
| rapport du rédacteur de l'inventaire | `c60829a5f9b49b098f5d922a9f4b923ecd92abfe8b3f7b9994ddc6fbb63df512` | début égal au mandat (`c60829a5…`) | en entier |
| rapport du développeur de la v68 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | égale à l'ordre de course | en entier |
| contre-lecture de la v68 | `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325` | égale à l'ordre de course | en entier |
| manifeste du paquet v68 | `4ed9fd8e893646a5e361f81a2da58099175ac2e3708555b9e7725240fedc8627` | égale à la contre-lecture | en entier |
| paquet v68, `orchestrator/pole/course2_v68.py` | `c1aeab4cc58118a373dd1503d34fd4e02694aeed6e550675aacd74db050b1024` | égale au manifeste | en entier ; les sept autres fichiers du paquet non ouverts |
| fiche des quatre décisions v68, v7 | `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac` | égale à l'ordre de course | **non lue** : empreinte seule |
| contrôle de la fiche v7 | `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09` | égale à l'ordre de course | en entier |
| mandat de l'additif de la v69 | `0c0efa12e9d6dac0a3569a1c69368b8eaf063cd9f0b03e2840d71ddff3479736` | égale à l'ordre de course | en entier |
| additif des interrupteurs de la v69, v1 | `aef8ff2f8eb3597c8405c765c3432ce791a34ab65b851a75ac223de875fbe158` | début égal à R-4060 | **en partie** : l. 222 à 253, et les lignes qui nomment le lanceur ; la v4 scellée (R-4131) non ouverte |
| cadre de la v70, v1 | `84651a4c658e88f0bca7d299746ae05c267ae7f9f2002d8371dd19fccef4a5ee` | début égal à R-4060 | en entier ; la v3 scellée non ouverte |
| rapport du rédacteur de l'additif v69 | `b97cbd188cf1cb2d7ccc252990bff19655a4799db4cc625023d1c3b52870a707` | début égal à R-4060 | en entier |
| lanceur de course v9 | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` | début égal à R-4353 | **empreinte, 2 944 lignes, 97 fonctions comptées** ; corps non lu |
| lanceur de course v10 | `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` | début égal à R-3861 | **en partie** : l. 1 à 140, 496 à 565, 2889 à 3160 ; liste de ses fonctions et constantes |
| épreuve des témoins v9 | `5be161fa35e339d171399a3ba2a2c927cd517fba42c745306fd867a4b3e3c69b` | égale à l'empreinte épinglée par le lanceur v10 (l. 510) | **en partie** : l. 1 à 120 |

### 2.3 Dans le dépôt de l'orchestrateur

Lu à `/home/user/lciric/ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (le second des deux chemins que nomme le lanceur v10, l. 530, 531 ; le premier est absent de cette machine, vérifié sur disque).

| fichier | empreinte recalculée | contrôle | lecture |
|---|---|---|---|
| `orchestrator/pole/noyau_v56.py` | `eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b` | égale à l'empreinte épinglée par le lanceur v10 | en entier |
| `orchestrator/pole/course2_v53.py` | `8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237` | égale à l'empreinte épinglée | l. 1 à 330 sur 553 |
| `orchestrator/pole/aiguilleur_v53.py` | `a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f` | égale à l'empreinte épinglée | en entier |

## 3. Ce que la conception établit, et ce qu'elle laisse

- **Établi sur pièces** : la base (conception, § 1) ; le lieu unique par où passe tout envoi (`noyau_v56.py`, l. 165), donc le lieu de l'adaptateur gardé ; que la boucle des cases de la v68 sert les mêmes cases à chaque génération (`course2_v68.py`, l. 186), ce que l'ordre de course disait « non vérifié » ; que les valeurs 150, 140, 135 et 120 USD des arrêts n° 6 et n° 7 sont déjà celles de la configuration de la course v9 ; qu'aucun lanceur 11 n'est écrit.
- **Trouvé, et absent de l'inventaire** : trois trous (conception, § 9, points 1 à 3) et un artefact sans objet (point 17).
- **Laissé au lot 0** : onze questions fermées sur le code que je n'ai pas lu.

## 4. Décisions

Format : décision en une phrase ; enjeu ; options ; recommandation et confiance ; défaut sous 48 heures.

### Pour Lazar

**D9 — L'échéance de GO-2026-11-20-67 est-elle portée du 2026-11-22 au 2026-11-26 ?**
- *Enjeu.* Le véhicule demande environ 45 heures de sessions, 30 à 36 heures d'horloge sans interruption, avant les deux lignes à part ; puis la course. La ligne échoit le 22.
- *Options.* (a) Le 26 novembre : couvre un lot à refaire, les lignes à part et la course ; inconvénient : quatre jours de plus sous un accord de 456 USD. (b) Le 24 novembre : au plus juste ; un seul incident demande un second mot. (c) Garder le 22 : la course ne part pas sous cette ligne, et il faut une ligne neuve le moment venu ; aucun risque de départ pressé.
- *Recommandation.* (a), confiance 0,7. Je passerais à (c) si la mère préfère une ligne neuve posée sur le véhicule contre-lu.
- *Défaut.* Aucun : c'est une ligne d'accord de calcul.

### Pour la mère

**D1 — Le véhicule prend-il un nom de série propre, « NA-1 », plutôt qu'un numéro de plus ?**
- *Enjeu.* La V9 interdit 69 et 70 ; le registre montre 69, 70 et 71 déjà portés par une autre lignée du même orchestrateur.
- *Options.* (a) Série propre, suffixe `_na_v1`, lanceur `lancer_course_nouvelles_attaques_v1.py` : aucune collision possible ; rompt la suite des numéros. (b) Un numéro neuf, vérifié libre dans les deux dépôts : garde la suite ; demande une vérification que je n'ai pas faite.
- *Recommandation.* (a), confiance 0,6.
- *Défaut.* (a) : c'est du code, donc de la routine.

**D2 — L'enveloppe de la requête d'un proposeur porte-t-elle un texte sur la syntaxe de la sortie ?**
- *Enjeu.* La partie servie nomme les champs, non la syntaxe ; la V9 dit « rien d'autre de fixe » et confie l'enveloppe à l'additif. Trop peu dit, et la part « réponse illisible » peut vider la course ; trop dit, et un texte neuf est servi à un agent.
- *Options.* (a) Reprendre le texte fixe de rôle de la course v9 s'il existe, est neutre et passe la garde de motifs, déclaré comme enveloppe à l'additif : la chaîne de lecture éprouvée ; mais un texte de plus part, que la V9 ne nomme pas. (b) Rien de plus ; lecteur de fiches à deux syntaxes : la lettre de la V9 ; plus de code neuf et un risque d'illisible, mesuré seulement à la sonde. (c) Une version neuve de la partie servie, qui dit la syntaxe : propre ; demande Lazar, une contre-lecture et un préenregistrement neuf.
- *Recommandation.* (a) si le lot 0 trouve ce texte neutre, sinon (b) ; confiance 0,5. Ce qui est servi à un agent étant un nœud, la mère dit si (a) va à Lazar.
- *Défaut.* Aucun : sans ce mot, les lots 3 et 5 s'écrivent sous (b), qui n'ajoute rien de servi.

**D3 — Qui écrit les consignes du portier et des juges pour cette question, et sous quelles étiquettes ?**
- *Enjeu.* Elles n'existent pas. L'épreuve des témoins, seul oracle de la course, lit le portier sous sa consigne.
- *Options.* (a) Deux consignes courtes écrites par le modèle F contre la partie servie, étiquettes fermées de la conception, § 2.4, contre-lues, attestées « aucune recette » et scellées par la mère ; items des juges réduits à un rang. (b) Reprendre les consignes de la course v9 en changeant les seules étiquettes : moins de texte neuf ; elles parlent d'une autre question. (c) Aucun juge dans cette course : écart à la composition gelée, donc Lazar.
- *Recommandation.* (a), confiance 0,65.
- *Défaut.* (a) pour la rédaction ; le scellement reste à la mère.

**D4 — L'identifiant neutre est-il un mot de six lettres tiré par une clé de tirage neuve, portée à l'additif du véhicule ?**
- *Enjeu.* La V9 permet une clé neuve « si la construction demande un tirage » et la veut au complément ; il n'y a pas de lot 2.
- *Options.* (a) Clé n° 40, 120 mots tirés une fois pour toutes les cases, table scellée avec le tirage, clé portée à l'additif du véhicule. (b) Une table de 120 mots écrite à la main à l'additif, sans tirage : aucune clé neuve ; un choix d'auteur, et 120 mots à contre-lire. (c) Un additif court au complément pour la seule clé : la lettre de la V9 ; une pièce de plus à contre-lire et à sceller.
- *Recommandation.* (a), confiance 0,6.
- *Défaut.* (a) pour l'écriture du lot 1 ; le numéro de la clé ne se fige qu'à l'additif scellé.

**D5 — Dans le registre servi, le « nom » est-il l'identifiant de la fiche, et l'« énoncé » son champ `idee` ramené à une ligne ?**
- *Enjeu.* La V9 sert un nom et un énoncé que la fiche de la question v5 ne porte pas.
- *Options.* (a) Oui ; un champ `idee` au-dessus de sa borne sort la fiche du contrat à la réception. (b) Un nom tiré du champ `idee` par programme (ses premiers mots) : un nom lisible ; une coupe, que la garde de motifs peut refuser. (c) Un champ de nom ajouté à la fiche : version neuve de la question et de la partie servie.
- *Recommandation.* (a), confiance 0,65.
- *Défaut.* (a).

**D6 — Le portier est-il l'ensemble « programme de forme, modèle, programme hors case », dans cet ordre, et une réponse illisible du modèle portier vaut-elle « au coffre » ?**
- *Enjeu.* L'ordre fixe quelles fiches sont lues par un modèle et ce qui pèse sur la garde du coffre.
- *Options.* (a) Oui aux deux, la réponse illisible comptée à part. (b) Le modèle lit toutes les fiches, même à champ de plus : la lettre « le portier » au sens du modèle ; un appel de plus par fiche fautive. (c) Une réponse illisible du portier arrête la génération : plus sûr pour la mesure ; une panne d'un appel coûte une génération.
- *Recommandation.* (a), confiance 0,6.
- *Défaut.* (a).

**D7 — À la sonde de refus, l'issue est-elle lue par programme seul, tout texte sans fiche valant « illisible » (arrêt n° 27) ?**
- *Enjeu.* La lettre ne décrit pas la garde qui lit « accepte » ou « refuse », et aucun appel de portier n'est prévu à la sonde.
- *Options.* (a) Oui ; la mère demande alors une étiquette à la session à part, sans lire la réponse. (b) Le portier lit la réponse sans fiche, sur Minuit, dans la ligne de 1 USD : distingue un refus d'une réponse vide motivée ; un rôle de plus dans une ligne qui n'en nomme pas.
- *Recommandation.* (a), confiance 0,55.
- *Défaut.* (a).

**D8 — En course, l'arrêt n° 1 arrête-t-il l'appel seul ?**
- *Enjeu.* « Le tour s'arrête » ne dit pas si c'est l'appel, le rôle ou la course.
- *Options.* (a) L'appel : consigné, non relancé, la course continue. (b) Le rôle, pour le reste de la course : plus prudent ; la composition n'est plus celle du texte. (c) La course : le plus prudent ; un seul refus coûte la génération réservée.
- *Recommandation.* (a), confiance 0,5 ; c'est la lecture qui touche le moins la composition gelée.
- *Défaut.* Aucun : c'est la lecture d'un arrêt d'un texte scellé.

**D10 — Les pièces de base (paquet v68, lanceurs v9 et v10, épreuve des témoins v9) sont-elles versées sur `main` avant les mandats de code ?**
- *Enjeu.* Le mandat veut le chemin et l'empreinte sur `main` ; elles n'y sont pas. Le lanceur neuf doit épingler des pièces que la mère peut vérifier.
- *Options.* (a) Les verser, empreintes vérifiées, avant le lot 1. (b) Épingler par le commit de la branche : rien à verser ; la mère vérifie sur une branche qui ne partage pas l'histoire de `main` (R-4331).
- *Recommandation.* (a), confiance 0,7. La garde des secrets a déjà compté une ligne du lanceur v9, une expression de détection sans valeur de clé (R-4353) : même traitement.
- *Défaut.* (b), qui ne demande aucun geste.

**D11 — L'artefact « juge de l'espèce 3 sur la clé du proposeur de l'espèce 3 » de l'arrêt n° 12 est-il remplacé ?**
- *Enjeu.* Depuis GO-2026-11-21-02, ces deux rôles sont sur la même clé : l'artefact ne peut plus être refusé.
- *Options.* (a) Le remplacer par « juge de l'espèce 3 sur la clé de l'aiguilleur », et garder les artefacts du complément et de son additif. (b) Le retirer sans le remplacer : les deux artefacts écrits depuis suffisent à la lettre.
- *Recommandation.* (a), confiance 0,7.
- *Défaut.* (a) : c'est une épreuve de plus, non de moins.

Les autres points ouverts (conception, § 9, points 4, 8 à 16) portent chacun leur proposition ; aucun ne bloque un lot avant le lot 7.

## 5. Mes écarts

1. **Quatre `git show` ont échoué** sur des chemins que le mandat disait sur `origin/main` : le rapport du développeur de la v68, sa contre-lecture, le lanceur de course v9, son épreuve des témoins (« exists on disk, but not in 'origin/main' »). Ce sont des erreurs de chemin, non des refus de garde. J'ai lu ces pièces sur le disque de la branche, comme le message de lancement le permet. Les quatre redirections ont laissé quatre fichiers vides dans mon sous-dossier `lu/`.
2. **Trois commandes `wc -l` ont rendu une erreur** sur un chemin absent : le lanceur de course 11, que je cherchais sous un nom supposé ; le premier chemin de l'orchestrateur ; un module supposé. Aucune n'est un refus.
3. **Le dépôt de l'orchestrateur a été lu**, trois fichiers, par un chemin que le lanceur v10 nomme. Le mandat dit « à trouver par les chemins que citent le registre et la v9 » : celui-ci est cité par un script, non par le registre.
4. **Commandes à plusieurs chemins** : des `sha256sum`, des `wc -l` et un `cat` sur des chemins écrits en entier ; une commande simple chacune, sans joker ni liste de répertoire. Quatre `git rev-parse` et un `mkdir` de mon dossier.
5. **Recherches par motif** par l'outil de recherche : dans mes deux copies de lecture, et dans trois fichiers nommés par leur chemin complet (le lanceur v10, le lanceur v9 pour un compte, l'additif de la v69) ; aucune sur un dossier d'un dépôt.
6. **Lectures partielles**, dites au § 2 : le devis v11 hors son § 10 ; la fiche v7 de la v68, connue par son contrôle et par l'ordre de course ; l'additif de la v69, dans sa v1 et non dans sa v4 scellée ; les lanceurs et l'épreuve des témoins ; `course2_v53.py`.
7. **Les copies de lecture des registres portent des noms de modèles** ; aucune de mes trois pièces n'en porte. Les clés sont désignées par leur nom d'usage, comme dans le mandat, jamais par un nom de variable.
8. **Un mot du mandat porté sans pièce** : le mot de la mère de 06:40Z est cité d'après le mandat ; R-4370, sur `main`, le confirme.
9. Un seul relevé de `date -u`, avant l'écriture.

— concepteur du véhicule, modèle F
