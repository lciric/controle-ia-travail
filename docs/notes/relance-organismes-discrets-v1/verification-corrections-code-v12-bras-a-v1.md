# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 12 — v1

- **Contre-lecteur** : Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni le code ni le brouillon. Rédacteur du code : Claude Fable 5.2.
- **Date** : 2026-11-20. Arbre au commit `e31dfc721` (« Code v12 de l'instrument et de l'analyse du bras A et programme du constat v5 »), aucun fichier modifié par moi hors celui-ci.
- **Pièces vérifiées par leur compagnon** (toutes conformes) : module de l'analyse `ba1acaa7c875c6a2…`, des verdicts `89e4b8d0b51e1b8e…`, des graines et du registre `381878cd7ef7e23c…`, du cloisonnement `be687467772fcc2d…`, de la configuration `8373851eef872300…`, des arrêts `cc632df305011290…`, des dépôts `db0aa22f0a7ef6d1…`, des mesures `7a1e6aab5e3e4216…`, de la permutation des étiquettes `20b78a8a3ecd7b19…` ; programme du constat de lancement en version 5 `fd5fddcd893e2cee91765ced911948009eb09ebd3b2382bc585fb7e4700ce290` ; aide des essais `6ee51f87ef67e43b…`, essais de l'analyse `a7bf64aa446837ae…` ; note du rédacteur `720cced721743e97…` ; relevé des défauts du texte `3b18aa4575ec409a…`.
- **Lu** : la note du code de la version 12 ; le relevé des défauts trouvés en codant la version 12 ; la vérification du brouillon 35 par ses titres (C-1, M-1) ; les fonctions neuves du module de l'analyse (`exiger_un_seul_fichier_de_l_etape_m`, `lectures_refaites_coherentes`, `_confronter_les_lectures_refaites`, `ouvrir_la_reprise_de_l_etape_n`, `ecrire_fichier_des_grandeurs_de_l_etape_n`, `_grandeurs_tirees_de_la_piece`), `retire_l_inscription` du module des graines, `dossier_des_arrets` du module de la configuration ; l'aide de reprise de l'étape (n) des essais (`ArretALEtapeN`).
- **Interdits tenus** : aucun interne de moniteur ouvert ni empreinté ; aucun chemin cloisonné ouvert (la garde statique n'a tourné que sur un faux dépôt, sous un crochet d'audit) ; aucune fiche de l'organisme d'idéation ; aucune réponse brute de l'essai de mesure ; le vrai registre non lu ; aucune clé, aucun appel réseau ni de modèle, aucun sous-agent, aucune dépense, aucun `pip install` ; un seul fichier écrit dans le dépôt, celui-ci ; aucun commit.

## Verdict

**Engageable, sous trois conditions d'écriture au texte ; je recommande de cesser de durcir le code.** Le défaut critique de la version 11 (une seconde table C par une livraison refaite après un arrêt à l'étape (n)) est fermé, et les trois mineurs que j'avais relevés sont tenus. Aucun essai ne m'a donné deux résultats de la discrétion dans une course sans toucher à la main un fichier scellé ou sans une ligne du registre écrite par Lazar. Ce qui reste — la copie d'une configuration dans un autre dossier, la destruction de pièces scellées, le retrait d'une configuration déjà lue — ne se ferme pas dans le programme d'analyse seul : c'est une garde de procédure, à déclarer comme telle (partie 4).

Un mineur neuf (M-1 ci-dessous) : une ligne de type « révocation » retire aussi une configuration **déjà lue**, ce qui ouvre une seconde course sous une autre configuration ; même nature que la copie, à dire au texte.

| point | état |
|---|---|
| Critique C-1 de la version 11 — seconde table C après un arrêt à l'étape (n) | **tenu** |
| Mineur M-1 de la version 11 — le contrôle d'avant le premier départ servait au rejeu | **tenu** |
| Mineur M-2 de la version 11 — garde du registre levée par une ligne de reprise sans empreinte | **tenu** |
| Mineur M-3 de la version 11 — une configuration abandonnée bloquait la suivante sans issue | **tenu** (seule une révocation à empreinte entière la lève) |
| Limite signalée par le rédacteur — configuration copiée dans un autre dossier de course | **confirmée**, et deux variantes de même nature |
| Mineur neuf M-1 — révocation d'une configuration déjà lue | **à écrire au texte** (garde de procédure) |
| Garde statique du cloisonnement | inchangée, sorties identiques à la version 11 |
| 331 essais de la commande de la note | **331 passent** (87,9 secondes) |

## 1. Corrections de la version 11 : rejeu des essais d'attaque

Pièces : `contre-lecture-code-v12/attaques_v12.py` (`8c1630637364e26c…`), sortie `attaques_v12.sortie.txt` (`d5ed3f7be09849fd…`) ; `attaques2_v12.py` (`bc95bb9036c6a44d…`), sortie `27cbca4aafc95b4a…` ; `attaques3_v12.py` (`5214b21271cd34ae…`), sortie `5868da3ca18f9234…` ; `attaques4_v12.py` (`3eb656e29054926f…`), sortie `aa115c77bbe8fcc2…` ; `abandon_v12.py` (`7d0e0a5a76aafe25…`), sortie `78318c94aa3f089d…`. Toutes dans le bloc-notes de la session, sous `contre-lecture-code-v12/`. Données fabriquées, registres fabriqués, dossiers temporaires.

### La seconde table de l'étape (m), d'abord

L'essai d'attaque de la version 11, rejoué tel quel : livraison lue au rang 1 (fichier de l'étape (m) scellé), fichier des scores par unité fautif (un champ de plus) qui arrête l'étape (n), ligne de GO qui cite ce fichier d'arrêt, configuration du rang 2 inscrite sur ce registre figé, constat de lancement sain par le programme.

- La pièce B (« repère ») sous cette ligne : **refusée** — « un fichier de l'étape (m) est déjà scellé dans cette course (`livraison-1/`) : il reste tel quel, opposable, et aucune autre lecture de l'étape (m) ne s'ouvre ».
- La pièce d'origine redonnée sous la même ligne : **refusée** — « livraison déjà refusée … elle n'est pas relue ».
- Fichiers de l'étape (m) dans la course après les deux tentatives : un seul, `livraison-1`, intact.

**Tenu.** Les trois gardes de la note (la ligne, la lecture, l'écriture) se recouvrent ; c'est celle de la lecture qui parle la première, comme le dit le rédacteur.

### Autres voies cherchées vers deux résultats de la discrétion

| essai | résultat |
|---|---|
| Fichier de l'étape (m) et son compagnon effacés à la main, nouvelle pièce sous la même configuration | **refusé** : l'ouverture de lecture scellée de la première livraison suffit (« toute autre pièce exige une ligne de GO ») |
| Même chose, **et** le dossier des arrêts vidé à la main | **passe** : « repère » — destruction de pièces scellées (partie 2) |
| Même configuration copiée dans `livraison-2/` de la même course | **refusé** : une configuration de rang supérieur à 1 doit inscrire un registre figé |
| Même configuration copiée dans le `livraison-1/` d'une autre course | **passe** : « ne repère pas » dans la première, « repère » dans la seconde, sans ligne de GO (partie 2) |
| Course entière copiée sous un autre nom, dossier des arrêts vidé | **passe** : « repère » (partie 2) |
| Configuration lue, puis « révoquée » au registre ; une autre configuration part dans une course neuve | **passe** : constat sain, « repère » dans la seconde course (M-1 ci-dessous) |
| Après une reprise de l'étape (n) aboutie, seconde ligne citant le même fichier d'arrêt d'origine | la configuration et son constat se font ; l'ouverture est **refusée** (« la ligne ne cite pas le fichier d'arrêt de la livraison refusée à reprendre ») |
| Second fichier des grandeurs de l'étape (n), autres grandeurs | **refusé** (« jamais écrasé ») ; le fichier des scores n'est plus lu une fois les grandeurs scellées |
| Rejeu de l'ouverture de l'étape (n) sous le même acte, avec une autre sortie refaite (autre fichier des scores) | **refusé** : l'acte lie la sortie refaite |

Chaque voie qui passe demande de copier ou de détruire un fichier scellé, ou une ligne de type « révocation » au registre. Aucune ne passe par l'appelant qui suit la procédure.

### Mineur M-1 de la version 11 — le contrôle d'avant le premier départ

Contrôle sain avant le premier départ ; première lecture interrompue (panne simulée) ; rejeu sur ce même contrôle : **refusé** (« le plus récent des contrôles est déjà porté par une pièce scellée »). Contrôle refait, sain ; rejeu : part, « ne repère pas ». **Tenu.**

### Mineurs M-2 et M-3 de la version 11 — la garde du registre au constat (programme en version 5)

Une configuration inscrite puis abandonnée ; constat d'une autre configuration de rang 1 :

| registre courant | constat |
|---|---|
| inscription abandonnée seule | refusé |
| + une ligne de reprise quelconque, après ou avant | refusé (la dispense « suivie d'une reprise » est bien retirée) |
| + révocation qui cite un abrégé de seize signes | refusé |
| + ligne de type « décision » qui cite l'empreinte entière | refusé |
| + révocation placée **avant** l'inscription | refusé |
| + révocation qui cite l'empreinte en majuscules | refusé |
| + révocation hors de la table (sans barres) | refusé |
| + révocation en gras (`**Révocation**`), empreinte entière | sain |
| + révocation, empreinte entière | sain |

**Tenus.** Le refus en majuscules est du bon côté (un retrait lève une garde) ; la consigne de tenue du registre doit dire que l'empreinte se cite en minuscules, comme le programme l'écrit.

### Mineur neuf M-1 — une révocation retire aussi une configuration déjà lue

`retire_l_inscription` lève la garde pour toute configuration qu'une révocation cite, qu'elle ait été lue ou non : le programme du constat ne voit pas les dossiers de course. Essai : la configuration de la première course est lue (« ne repère pas ») ; une révocation la cite ; une autre configuration (autre réglage) obtient un constat sain ; sa course lit la pièce B : « repère ». Le texte, lui, dit qu'une révocation retire une configuration « abandonnée avant sa lecture ». Ce n'est pas une voie de l'appelant : il faut une ligne écrite au registre, datée, de type « révocation », qui se voit. Mais c'est une seconde première livraison, de même nature que la copie. **À écrire** : (a) au registre (13.2), une révocation ne retire qu'une configuration dont aucune lecture n'a été ouverte ; (b) au rapport, la liste de toutes les inscriptions et de toutes les révocations de l'analyse, chacune avec son dossier de course et l'état de son dossier des arrêts. Le second remède de la partie 2, dans sa forme forte, la fermerait aussi.

## 2. La configuration copiée dans un autre dossier de course

**Confirmée.** Le fichier de configuration et son compagnon, copiés dans le `livraison-1/` d'une course neuve, ont la même empreinte ; le programme du constat rend un second constat sain sous la même ligne d'inscription ; la lecture donne « ne repère pas » dans la première course, « repère » dans la seconde, sans ligne de GO. Deux variantes de même nature passent aussi : la course entière copiée sous un autre nom, dossier des arrêts vidé ; et, dans la course d'origine, le fichier de l'étape (m) et le dossier des arrêts effacés. La cause est celle que dit le rédacteur : le dossier des arrêts est nommé relativement au fichier de configuration, et la garde du registre compare des empreintes, non des dossiers.

Une remarque qui borne la portée : rejouer **la même pièce** dans une copie redonne le même résultat (le calcul est déterministe). Une erreur honnête — un conteneur perdu, une course recréée depuis le dépôt — ne produit donc pas deux résultats différents. Deux résultats demandent une autre pièce, donc une intention.

### Jugement des deux remèdes proposés

1. **Une garde de procédure, dite comme telle.** Elle ne ferme pas ; elle rend la faute visible après coup, si le versement est tenu. Elle suffit à mon jugement **à une condition** : que le dossier de course entier (configuration, constat, ouverture de lecture, dossier des arrêts) soit versé — committé et poussé — **avant que le fichier de l'étape (m) soit lu par quiconque**, et que le manifeste de la course cite le chemin du dossier de course et l'empreinte de l'ouverture. Une seconde course sous la même empreinte se voit alors dans l'arbre et dans l'historique, et la destruction d'un fichier versé aussi.
2. **L'empreinte de l'ouverture de lecture inscrite au registre.** Dans la forme écrite au relevé (« avant que le fichier de l'étape (m) soit opposable »), **elle ne ferme pas** : la lecture rend son résultat dans le même appel qui écrit l'ouverture ; la session voit donc la table C avant toute inscription, et peut n'inscrire que l'ouverture de la course qui lui convient. Elle ne ferme que dans une forme plus lourde : le programme écrit l'ouverture **et s'arrête** ; Lazar l'inscrit ; la lecture ne part que si le registre porte cette ouverture, et une configuration n'en porte qu'une. Cela coûte un acte de Lazar et un aller-retour par livraison, et une seconde vérification du registre par le programme du constat. Cette forme fermerait aussi M-1 ci-dessus (le programme refuserait de retirer une configuration dont l'ouverture est inscrite).

### Une autre voie dans le code

Oui, partielle et bon marché : **ancrer la course dans la configuration**. La configuration nommerait le dossier des arrêts par un chemin relatif à la racine du dépôt (et non au fichier), et le programme vérifierait que le fichier de configuration se trouve bien dans le dossier de course qu'elle nomme. Une copie dans un autre dossier du même arbre pointerait alors vers le dossier des arrêts d'origine, où l'ouverture déjà scellée refuse toute autre pièce ; ou elle serait refusée parce que son chemin n'est pas le sien. Ce qui reste : un second clone du dépôt, où le même chemin existe vide. Ce reste retombe sur le versement du remède 1 : deux clones qui écrivent au même chemin des ouvertures différentes entrent en conflit au moment de pousser. Je ne la recommande que si elle ne rouvre pas un tour de durcissement ; elle n'est pas nécessaire si le remède 1 est écrit avec sa condition de versement.

**Ma recommandation** : le remède 1, écrit au texte comme garde de procédure, avec la condition de versement avant toute lecture du fichier de l'étape (m) ; le remède 2 seulement si Lazar veut une fermeture et accepte l'acte par livraison. C'est une **question pour Lazar**, parce que le remède 2 lui demande un acte. Confiance moyenne à haute.

## 3. Les six choix faits faute de texte

Je compte les trois choix de la confrontation (note, partie 4), le cas des lectures illisibles, le contrôle au rejeu de l'étape (n) (relevé, A.5) et la sortie d'origine donnée en entrée (relevé, B). La copie de configuration (relevé, A.1) est traitée en partie 2.

**Ce que j'ai vérifié d'abord.** La confrontation ne compare que la clé `lectures` : une autre provenance, d'autres agrégateurs, d'autres réglages ou d'autres plis dans la sortie refaite la laissent cohérente ; l'ordre des doses aussi ; un champ de plus dans une lecture la rend incohérente ; `0.52000000000000000001` contre `0.52` aussi, en fractions exactes. C'est sans danger, parce que ce que la règle rapporte, l'agrégateur et les comptes d'exclusion se recomposent **de la sortie d'origine** sous la configuration du rang d'origine (`_grandeurs_tirees_de_la_piece`, appelée sur la pièce d'origine) ; de la sortie refaite, seule la déclaration du fichier des scores est lue. Après une sortie refaite incohérente : l'acte est écrit, la ligne est dépensée, le constat d'incohérence est scellé, le fichier des scores n'est pas lu, les grandeurs de l'étape (n) sont « non rapportées : livraison refaite incohérente » ; une sortie cohérente sous la même ligne est refusée ; une ligne neuve qui cite le fichier d'arrêt d'origine fait sa configuration et son constat, puis son ouverture est refusée. **L'étape (n) de la course est perdue sans retour.**

| choix | jugement | classement |
|---|---|---|
| 1. Confrontation **après** l'acte : la ligne de GO est dépensée par une sortie refaite incohérente | À déplacer **avant** l'acte, comme les gardes du rangement et de la provenance, qui scellent leur constat sans dépenser la ligne. La confrontation ne révèle rien de neuf : les vingt lectures sont déjà connues et scellées à l'étape (m). Aucune pêche n'est possible : sous une ligne, le premier acte lie la première sortie refaite cohérente, et une autre est refusée (essai : rejeu sous le même acte avec une autre sortie refaite). La règle « une ligne n'ouvre qu'une reprise » reste vraie. Le constat d'incohérence reste scellé et compté au rapport, comme signe d'un défaut du côté habilité. | **précision au texte** ; une ligne d'information à Lazar, parce qu'elle touche l'usage de ses lignes de GO |
| 2. Une livraison refaite incohérente **ne se reprend pas** | Si le choix 1 est déplacé, la question tombe presque : l'incohérente n'a rien ouvert, la même ligne reste valable pour une sortie refaite cohérente. Il suffit d'écrire : une sortie refaite incohérente n'est ni refusée ni reprise ; elle n'ouvre rien ; la ligne attend une sortie cohérente. Si le choix 1 reste tel quel, il faut au contraire permettre qu'une ligne neuve cite le constat d'incohérence (avec module et rapport, comme un fichier d'arrêt) : sinon une seule sortie fautive du côté habilité ferme l'étape (n) pour toujours, ce que l'option (c) de Lazar (« discrétion non lue en distinguant les étapes ») ne demande pas. | **précision au texte** si le choix 1 est déplacé ; sinon **question pour Lazar** (une conséquence définitive sur un résultat rapporté) |
| 3. Mêmes lectures dans la même forme (liste contre table par dose, champ de plus : incohérent) | Le côté strict est le bon : il ne coûte rien si le choix 1 est déplacé. Le texte doit dire que la comparaison porte sur la seule clé `lectures`, en fractions exactes, sans égard à l'ordre, et que le reste de la sortie refaite n'est pas comparé parce qu'il n'est pas lu. | précision au texte |
| 4. Lectures illisibles (pièce illisible, clé absente, clé en double) : incohérente, non arrêt | Juste : un écart de la sortie refaite n'est pas un écart de la liste fermée de l'étape (n) ; il ne doit pas consommer d'issue. Avec le choix 1 déplacé, il ne consomme pas non plus de ligne. | précision au texte |
| 5. Aucun contrôle de lancement exigé au rejeu de l'étape (n) | Juste. L'acte lie la sortie refaite, la sortie refaite lie le fichier des scores, le fichier des grandeurs une fois scellé ferme l'étape : un rejeu ne peut lire que les mêmes pièces (essais : même sortie refaite acceptée sans contrôle, autre sortie refusée, fichier des scores relu refusé après les grandeurs). Un contrôle n'ajouterait rien. | précision au texte |
| 6. La sortie d'origine est une entrée de l'appelant, reconnue à l'empreinte que portent les constats de l'étape (m) | Juste ; une autre pièce est refusée (essai de la suite : la première ou la seconde sortie refaite donnée comme origine est refusée), et pour une livraison ordinaire elle ne se donne pas. | précision au texte |

## 4. Question d'ensemble : continuer à durcir le code ?

**Non, à mon jugement.** Depuis la version 9, chaque voie que j'ai trouvée demandait davantage : d'abord un appelant qui donne une autre pièce, puis une panne entre deux écritures, puis une reprise au mauvais rang ; aujourd'hui, il faut copier ou détruire un fichier scellé, ou faire écrire par Lazar une ligne de révocation. Ces voies-là ne se ferment pas dans le programme d'analyse : il ne voit que le dossier que sa configuration nomme, et il ne peut pas savoir qu'un fichier a existé puis disparu. Chaque garde de code de plus coûte un tour de contre-lecture et ajoute de la surface. Ce qui reste relève de gardes de procédure, à déclarer comme telles.

**Je recommande de cesser de durcir le code à ces conditions** :

1. **Les gardes de procédure sont écrites au texte, nommées, avec qui les tient** : un seul dossier de course par configuration inscrite ; aucune copie ni destruction d'une pièce scellée d'une course ; une révocation ne retire qu'une configuration jamais ouverte (M-1) ; le constat de lancement et le contrôle d'avant rejeu se font par le programme, jamais à la main (déjà déclaré) ; le registre tenu selon 13.2, empreintes entières en minuscules.
2. **Versement avant lecture** : le dossier de course entier — configuration, constat, ouverture de lecture, dossier des arrêts — est committé et poussé avant que le fichier de l'étape (m) soit lu par quiconque ; chaque pièce scellée ensuite l'est aussi avant la suivante.
3. **Un manifeste de course scellé et contre-lu** cite le chemin du dossier de course, l'empreinte de la configuration, de l'ouverture et de chaque pièce du dossier des arrêts ; le rapport liste toutes les inscriptions et révocations de l'analyse et rapproche chacune d'un dossier de course.
4. **Le choix 1 de la partie 3 est tranché** (confrontation avant l'acte), puisque c'est le seul point où le code tel quel fait perdre un résultat sur une erreur honnête ; s'il l'est dans ce sens, le code doit être changé une dernière fois, sur ce seul point, et je le vérifierais sur ce seul point.
5. **Une épreuve de forme de bout en bout** sur données fabriquées, par la session qui lancera, avec la commande réelle, avant toute dépense ; et une vérification indépendante du code et du texte ensemble au scellement du préenregistrement.

Si Lazar préfère une fermeture du côté du code pour la copie, le seul ajout qui en vaille la peine est le remède 2 dans sa forme forte (partie 2), et non une garde de plus dans le programme d'analyse.

## 5. Essais de la commande de la note

`PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v12.py tests/test_verdicts_bras_a_v12.py tests/test_graines_bras_a_v12.py tests/test_cloisonnement_bras_a_v12.py tests/test_permutation_etiquettes_bras_a_v12.py tests/test_mesures_bras_a_v12.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py` : **331 passent en 87,9 secondes**. Sortie : `contre-lecture-code-v12/essais.sortie.txt` (`cd4ce2175458c771…`). La suite entière du dépôt n'a pas été lancée.

## 6. Garde statique du cloisonnement et fouille des livraisons

- **Garde statique, sur un faux dépôt seulement**, sous un crochet d'audit de Python qui note chaque ouverture et chaque listage (`audit_cloisonnement_v12.py`, `995c560e41847b39…` ; sortie `c5ffaaace864d5bd…`) : aucune ouverture ni aucun listage sous un chemin cloisonné, majuscules comprises ; les voisins aux noms proches sont lus et signalés ; liens symboliques signalés ; le lien physique n'est pas ouvert ; départ cloisonné et départ par `..` refusés. **Sortie identique à celle de la version 11.**
- **Vingt-quatre modules plantés** (`attaques_cloisonnement_v12.py`, `43dcded87373e836…` ; sortie `060e09fb40011c2a…`) : mêmes issues qu'à la version 11 ; les trois qui passent (listage sans extension, nom tiré de la pièce, `mots_et_cout_` sous un dossier `outils/`) sont les mêmes qu'à la version 11, déjà rapportées dans mes vérifications précédentes : limites d'une garde qui lit le texte des modules.
- **Fouille de quatre cents livraisons altérées** (graine fixe, `fuzz_livraison_v12.py`, `64062bb092a21a1f…` ; sortie `bc078c811e7e1e46…`) : 94 passent, 290 arrêts nommés, 16 gardes ordinaires, toutes sur la provenance de la pièce, comme à la version 11. **Sortie identique.**

## 7. Ce qui reste

- **Pour Lazar** : le choix entre les deux remèdes à la copie de configuration (partie 2 ; recommandation : remède 1 avec versement avant lecture).
- **Pour le brouillon 36** : les six précisions de la partie 3 (le choix 1 dans le sens recommandé), M-1 (révocation d'une configuration lue), la consigne des empreintes en minuscules, et les gardes de procédure de la partie 4 écrites comme telles.
- **Pour le code, s'il change une dernière fois** : la confrontation déplacée avant l'acte, et rien d'autre ; je vérifierais ce seul point.
- **Non vérifié ici** : le brouillon 35 au-delà des titres de sa vérification ; le texte des gardes de procédure, qui n'existe pas encore.
