# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 8 : corrections du contrôle de la version 7 — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-20 ; `date -u` lu à 04:41Z en cours de travail et à 04:45Z juste après l'appel de l'outil (heure exacte de la version 8 au journal de l'outil).
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-redacteur-palier-0b-v8-v1.md` (`df835a6bd021cc1ddeff82e55a53a9dbf66153f0a0d5649af084b963a243044d`), vérifié par son compagnon avant tout geste.
- Sur processeur seul : aucun tirage, aucun étalonnage, aucun audit, aucun lancement du code de l'étage ; aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau ; aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.** Rien de lu sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun code en ligne passé à un interpréteur ; un seul programme lancé, par son chemin : l'outil de remplacement (Python 3.13.18). Aucune commande de liste ; une commande simple par appel.

Dossier P0B : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## 1. Verdict

La version 8 est écrite, par **28 remplacements exacts** appliqués au premier appel, sans refus ni avertissement de l'outil : les dix-sept du contrôle (seize corrections, la correction 9 en comptant deux), à la lettre, et onze du rédacteur (tenue, tête des nœuds, liste du code v4). Elle n'est **ni contrôlée ni scellable en l'état** : son différentiel reste à contrôler, les nœuds 1 et 2 sont à Lazar sans défaut, elle demande un code v4, et le commit qu'elle inscrit (code v3) ne vaut qu'après lui.

## 2. Fichiers rendus

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v8/`. Chaque fichier a son compagnon `.sha256`.

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v8.md` (248 463 octets, 885 lignes) | `fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c` |
| `remplacements-preenregistrement-palier-0b-v7-v8.json` (28 remplacements) | `28c89e35f1e873af7f6f4f29c425ab9a2db93cd2ee14715a500549f92a0ba82b` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v8.md.journal-remplacements-v1.json` (journal de l'outil) | `f289516475b8b85af664d6f83539013389d746810f5bd09008a175261b53f30f` |
| `differentiel-preenregistrement-palier-0b-v7-v8.diff` (`diff -u` ; 19 lignes de la version 7 changées, 33 lignes côté version 8) | `14d7b4b8836c3a9153068246bd5c0d47f8ef0de2d5d131f0f2fc2a39fe0bf41c` |
| `rapport-redacteur-palier-0b-v8-v1.md` (ce rapport) | dans son compagnon |

La version 7 est intacte (compagnon revérifié après l'opération).

## 3. Sources, avec chemin et empreinte

Chaque empreinte vérifiée par son compagnon et recalculée sur disque.

| pièce | empreinte |
|---|---|
| `P0B/mandat-redacteur-palier-0b-v8-v1.md` | `df835a6bd021cc1ddeff82e55a53a9dbf66153f0a0d5649af084b963a243044d` |
| `P0B/controle-differentiel-palier-0b-v7-v1.md` | `1211fed3b3ce0baa2324c1976897dda622e9fabc91c6ccbe50ea110346db19d0` |
| `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v7.md` | `2f0f928f291b65a98bff2680e6bb7172bcf279da7e76b16bd837193f0704f4f0` |
| `P0B/rapport-redacteur-palier-0b-v7-v1.md` | `c06c2870a191fa90bedc2effe3e82078bbb625bb6c46e867f0e3e689b75d0736` |
| `P0B/controle-v7-outils/calcul_reserve_23_v1.py` (empreinte recalculée ; non lu, non lancé) | `354731b35dde1946052d3dbb9506de19a8977849bae8838b7d3ef510fada279a` |
| `P0B/controle-v7-outils/calcul_reserve_23_v1.sortie.txt` (empreinte recalculée ; non lue) | `d692b301960545ea1173689dd056a8e81bf9058c61bd85ccf8b56ae29dfb2dfa` |
| `scripts/remplacer_texte_exact_v1.py` (racine du dépôt ; lu en entier) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Les deux empreintes du calcul de la réserve 23 sont égales à celles que le contrôle écrit à son § 4.4. Je n'ai lu aucun module du code v3 : ce que la version 8 dit du code vient du contrôle (§ 6 et § 7).

## 4. Les seize corrections du contrôle

Appliquées à la lettre du § 9 du contrôle, par les remplacements n° 1 à 17 du fichier JSON (n° 9 et 10 : corrections 9a et 9b ; n° 11 à 17 : corrections 10 à 16). Chaque ancre a été comptée une seule fois dans la version 7 avant l'appel (`grep -c -F -e`, ou `grep -o -F -e` quand la ligne est très longue). Aucun texte ancien ni neuf n'a été retouché.

## 5. Les onze remplacements du rédacteur

Leurs mots sont les miens ; ils sont **à contrôler**. L'alinéa « Version 8 » de l'annexe H les déclare.

| n° du JSON | lieu | objet |
|---|---|---|
| 18 | titre | « v7 » devient « v8 » |
| 19 | ligne de version | phrase « Version 8 » : version 7 remplacée et intacte, contrôle et mandat cités avec chemin et empreinte, correction de fond dite en une phrase, sens de « cette version » dans les phrases reprises ; « Version 7 … remplaçait » |
| 20 | ligne de date | heure de la version 8 |
| 21 | annexe H, après le premier alinéa | alinéa de tenue « Version 8 » : les seize corrections une à une, les ajouts du rédacteur, ce qui est laissé tel quel, ce qui n'est pas traité |
| 22 | annexe H, « Ce qui revient à Lazar », avant le nœud 1 | alinéa commun aux deux nœuds (réponses du contrôle aux questions de R-4076 ; issue probable) et puce de tête du nœud 1 |
| 23 | annexe H, nœud 2 | puce de tête du nœud 2 |
| 24 | « Ce qui demande un code v4 », point 1 | arrêt sur une exactitude non calculable ; trois lectures pour les seuls audits des doses, lettre pour les audits de lois |
| 25 | point 2 | le fichier d'autorisation du lancement est à définir |
| 26 | point 5 | où se joue le jeu de la garde 27 ; le choix 8 peut être levé |
| 27 | point 6, suivi d'un point 7 neuf | fuite entre mondes frères : à regarder par le vérificateur du code v4 |
| 28 | écart 1, puce « Code » | renvoi au point 5 |

**Texte que le contrôle ne donne pas mot pour mot** (mandat, point 2) : les remplacements 22 et 23 résument le § 4 du contrôle dans mes mots. J'y ai repris ses chiffres et ses jugements en les lui attribuant, sans en ajouter et sans trancher. J'y ai joint sa remarque sur l'issue probable (son § 10, point 4), que le mandat ne demandait pas en toutes lettres : elle pèse sur les deux nœuds.

## 6. Nœuds pour Lazar, tels que la version 8 les pose

En tête des deux nœuds, la version 8 écrit ce que le contrôle répond aux trois questions de la mère (R-4076) :

- **D'où venait ce que le rédacteur savait** : d'essais du code sur le vrai générateur, sous la couche de graines « essai », et d'un calcul sous un nul gaussien ; d'aucune sortie décisive. Nuance : ces essais sont un avant-goût de la porte de l'étape 3.
- **Dépendance à l'attente d'un arrêt** : la règle du nœud 1 en dépend par son moment, non par son contenu ; la règle calibrée n'en dépend pas sur les trois audits des doses ; son extension aux deux audits de lois en dépendait, et la version 8 la retire.
- **Ce que dit la version 6** : elle admet une règle écrite après un diagnostic sur graines d'essai, si c'est déclaré, contre-lu et gardé (réserve 19) ; elle interdit qu'un ajustement remplace un arrêt sans erratum ; elle avait écrit d'avance le remède d'un échec de forme (réserve 18).
- **Issue probable sous les options (a)** : les exactitudes de forme passeront probablement ; l'exactitude de contenu « dépendantes contre indépendantes » dépassera probablement 0,55 ; le générateur serait alors non audité pour l'étage payant.

**Nœud 1 — la longueur du texte dans l'audit de présentation.**
- Décision : mesurer la longueur de forme sur le texte où chaque nombre est remplacé par son jeton, la longueur brute passant aux traits de contenu ?
- Enjeu : à la lettre de la version 6, l'audit s'arrêterait probablement à l'étape 3, sur un signal qui vient du signe des poids.
- Option (a), la règle écrite — avantage : la forme ne lit plus le contenu, le signal reste lu et lie l'étage payant ; inconvénient : écrite après un diagnostic, un arrêt probable devient un signalement.
- Option (b), la lettre de la version 6 — avantage : rien ne change après un diagnostic ; inconvénient : arrêt probable sur un signal réel du générateur rangé sous la forme, puis un erratum de toute façon.
- Option (c), le même filtre pour toutes les sous-lois, que la réserve 18 écrivait d'avance — avantage : traite la cause ; inconvénient : change le générateur gelé et les fréquences, code lourd, jamais éprouvé.
- Options qui ne dépendent pas de l'attente : (b) et (c) ; (a) n'en dépend que par son moment.
- Recommandation : (a) ; confiance moyenne à haute. Défaut : aucun.

**Nœud 2 — la règle calibrée de l'audit de présentation.**
- Décision : une exactitude de forme d'un audit des mondes par dose n'arrête-t-elle l'audit qu'au-dessus de 0,55 + 2 σ₀, une exactitude entre 0,55 et ce seuil liant l'étage payant sans arrêter, les deux audits de lois restant à la lettre de la version 6 ?
- Enjeu : à la lettre, un générateur parfait arrêterait l'étape 3 de 11 à 14 fois sur cent ; la règle calibrée voit mal un petit défaut des mondes par dose.
- Option (a), la règle écrite, désormais restreinte aux trois audits des doses — avantage : un arrêt vaut preuve, le bruit est mesuré sur les données mêmes ; inconvénient : seuil d'arrêt vers 0,61 ou plus haut, une exactitude vraie de 0,60 n'arrête qu'une fois sur trois à une fois sur neuf, deux régimes de lecture.
- Option (b), la lettre de la version 6 — avantage : aucun seuil ne bouge ; inconvénient : alarme à tort de 11 à 14 fois sur cent.
- Option (c), la lettre sur 100 suites par dose — avantage : seuil inchangé, alarme à tort de 1,1 % par paire ; inconvénient : la valeur de 50 change, construction doublée, pas de marge.
- Options qui ne dépendent pas de l'attente : les trois.
- Recommandation : (a) ; confiance moyenne ; (a) et (c) peuvent se joindre. Défaut : aucun.

**Proposition avec recommandation — la dose du jeu de la garde 27** (inchangée depuis la version 7) : jouer ce jeu à la dose 0,25 et ne plus revendiquer la marge face à la source étrangère à 0,5 sur la couche mécanique ; recommandation (a), confiance haute ; défaut sous 48 heures : (a). Le contrôle est d'accord avec ce classement, sous une réserve : si la mère lit la marge retirée comme une revendication, c'est un nœud sans défaut.

**Pour information** (inchangé) : le choix 11 ; les causes d'arrêt de plus ; les artefacts ajoutés aux gardes 25 et 27 ; le commit inscrit ne vaut qu'après un code v4.

## 7. Ce qui demande un code v4

1. `audit.py` et l'étape 3 : longueur de forme sur le texte aux nombres remplacés ; longueur brute parmi les traits de contenu ; σ₀ par 1 000 permutations, entre lois ou entre suites ; trois lectures **pour les trois audits des mondes par dose seulement** ; **lettre de la version 6 pour les deux audits de lois** (au-dessus de 0,55, arrêt) ; arrêt sur un pli privé d'une classe ; **arrêt sur une exactitude non calculable**, que le code v3 range en « non calculée » sans arrêter. Essais et défauts au banc, dont les quatre artefacts de plus de la garde 25. **Après les mots de Lazar sur les nœuds 1 et 2.**
2. `graines.py`, `constantes.py` : le verrou (note D6). **Le fichier d'autorisation du lancement est à définir** — forme, auteur, lieu —, par la mère et au code v4.
3. `etalonnage.py` : note D8.
4. `tirages.py` : la liste des étiquettes dans un fichier scellé (choix 12).
5. **Le jeu de la garde 27** : l'étape 4 du code v3 ne joue que les bras 1 à 3 ; le code v4 dit où ce jeu se joue et à quelle dose, et fixe 0,25 par une constante. L'ordre des bras du choix 8 est déjà suivi par le code v3 : point à lever par le vérificateur.
6. Sans changement du code : l'écart 1 hors du point 5 ; le choix 11 ; la note D5 ; la tenue.
7. **À regarder par le vérificateur du code v4** : la moyenne des exactitudes permutées aux audits des doses (fuite entre mondes frères). Tirer les plis par suite changerait une règle du texte et demande un erratum contre-lu.

Le commit inscrit (`3d332d2c`) ne vaut qu'après ce code v4, et l'erratum du commit se refait.

## 8. Écarts, incidents et points à relire

1. **Aucun incident d'outil, aucun refus.** Les 28 ancres ont été comptées une fois chacune avant l'appel ; l'outil a tout appliqué au premier essai. Aucun JSON fautif n'existe.
2. **L'heure écrite dans la version 8** (« vers 04:50Z ») a été écrite avant l'appel de l'outil, qui a tourné vers 04:45Z. Le texte renvoie au journal de l'outil pour l'heure exacte. C'est la même faiblesse que la correction 16 corrige pour la version 7, en plus petit.
3. **L'horloge et le contrôle.** Le contrôle se dit écrit « de 04:21Z à 04:45Z environ » ; mon premier `date -u` donne 04:41Z, après la remise du mandat. Je le signale sans l'expliquer.
4. **Tenue bornée par le mandat au titre et à la ligne de version.** Le contrôle (fin du § 9) nommait aussi « statut, heure, mandat et cette contre-lecture en tête ; un alinéa à l'annexe H » : je les ai faits, dans la ligne de version, la ligne de date et l'annexe H. Je n'ai ajouté ni ligne « Mandat de la version 8 » ni entrée « pièces de la version 8 » aux documents qui font foi : mandat et contrôle sont cités, chemin et empreinte, dans la ligne de version.
5. **Passages laissés tels quels et désormais inexacts ou à lire avec l'alinéa de tenue** (l'alinéa « Version 8 » de l'annexe H les nomme) :
   - la section « Contre-lecture » dit encore la version 7 « pas contre-lue », et sa liste de fichiers ne nomme pas les pièces de la version 8 ;
   - le premier alinéa de l'annexe H dit « cette version est produite par 30 remplacements », ce qui se dit de la version 7 ;
   - « trois causes d'arrêt de plus » (annexe H, deux endroits, et la table), alors que la correction 4 en ajoute une quatrième à l'audit ;
   - la fin de la réserve 23 sur la permutation entre lois, dont le σ₀ ne décide plus d'un arrêt ;
   - les tables « Ce que cette version touche » et « Ce qui n'est pas changé par la version 7 ».
   Le contrôleur du différentiel dira s'il faut des remplacements de tenue de plus, comme pour la version 6.
6. **Non traité, remis à la mère** : la remarque 3 du § 10 du contrôle (aucun point de la liste d'arrêt ne porte les causes d'arrêt de l'étalonnage, ni l'action qui suit) ; la part de la remarque 1 qui changerait une règle (plis tirés par suite). Elles demanderaient des mots que ni le contrôle ni le mandat ne donnent.
7. **L'option (a) du nœud 2 n'a pas été réécrite** : ses mots sont ceux de la version 7, et c'est la puce de tête qui dit qu'elle est désormais restreinte aux trois audits des doses (l'option notée (a′) par le contrôle). Les deux inconvénients que le contrôle y ajoute sont dans cette puce, non dans la ligne de l'option.
8. **Non faits** : le validateur du gabarit ; la recherche des listes « Ne pas écrire » par programme ; aucune relecture du code v3 ; aucun rejeu du calcul de la réserve 23. Mes ajouts ne citent aucun travail publié et ne portent aucun identifiant de modèle.
9. **Je n'ai pas relu la version 8 en entier après l'outil** : je m'appuie sur les contrôles internes de l'outil (chaque texte neuf présent une fois de plus qu'avant, octets hors zones identiques) et sur le compte des lignes du différentiel.

## 9. Reste à faire, hors de mon mandat

Verser les fichiers ; contrôle du différentiel de la version 7 à la version 8 par un sous-agent neuf (règle R2), mes onze remplacements compris ; mots de Lazar sur les deux nœuds et sur la proposition ; code v4 et sa vérification ; erratum du commit refait ; scellement par la mère.

*Rédacteur neuf, modèle F.*
