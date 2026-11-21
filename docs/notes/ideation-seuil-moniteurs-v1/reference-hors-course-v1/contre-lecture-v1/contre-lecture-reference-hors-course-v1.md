# Contre-lecture — section « Référence hors course », critères de lecture en vigueur et réponse sur le véhicule, course « seuil et moniteurs » — v1

**Verdict : À corriger.** Onze corrections, aucune bloquante prise seule ; les corrections 1 à 7 sont à porter avant le scellement des critères, donc avant le départ de l'appel à l'auteur des mondes (condition (a) de GO-2026-11-21-37).

- Contre-lecteur neuf, modèle O, d'une autre lignée que le concepteur (modèle F). Écrit le 2026-11-21 ; relevé de `date -u` : 13:14:07Z. Pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit, aucun refus de permission, de classifieur ni de garde.
- Pièces relues, empreintes recalculées, toutes égales à la table du concepteur (`table-empreintes-concepteur-reference-hors-course-v1.txt`) : section `9fb4e28c…`, critères `ea5f224f…`, réponse sur le véhicule `0f35c248…`, rapport `68d31a30…`, texte extrait `f3388849…`, calculs `77910593…` et sortie `685045b7…` ; mandat du concepteur `4569acaf…`.
- Sources lues : sur `origin/main` (tête `fdbc8a73d178…`, 13:06:03Z), par `git show` redirigé : pièce de scellement de la conception `4286bf39…` et son erratum 1 `64e06388…` ; arbitrage des six points délicats (`docs/notes/arbitrages-points-delicats-v1/`, `44d1e86f…`), points 4 et 8 ; fiche de la dérive de régime `4a1579b3…`, en entier ; arbitrage de l'unité des décalages (`docs/notes/ideation-seuil-moniteurs-v1/arbitrage-unite-decalages-v1/`, `a8f8acfa…`, absent du disque, lu sur `origin/main`) ; `registres/go.md` (copie `608331ef…`), lignes -35 à -50 ; `registres/scellements-v1.md`, pour les chemins. Sur disque : ordre v6 `208454c5…`, préenregistrement court v6 `a2f1eaee…`, rapport v6 du programme de vérification `28d9155f…`.
- **Lecture au-delà de la liste (R2, signalé)** : le texte servi v3 (`f3d87162…`) et l'erratum 1 v5 du mandat (`2051450a…`, § 3), sans quoi la liste nominative et les issues des témoins imposés ne se vérifient pas. Ni l'un ni l'autre n'est la table de vérité ni une source de la liste scellée.
- Non lus : la table de vérité des témoins, le programme de vérité, toute source de la liste scellée, toute branche de quarantaine ou de matière première, rien sous `archives-reponses-modeles/`, l'ordre v4 scellé (`390af604…`, non au dossier nommé).

## Corrections

**1. Section, § 9 (objet vrai) et arrêt 20 : la garde de la référence sonne sur un cas sain plus d'une fois sur deux.**
Ce qui ne va pas : chaque prédiction de l'objet vrai est un intervalle à 99 % ; il y en a deux par monde, tranche et valeur de m, soit au moins 48 cellules à scores continus (familles A à I hors G, trois tranches, m = 200 et 400), plus les familles de l'auteur et celles à l'écart. Sur l'objet vrai exact (V1★ de loi bêta(k, m + 1 − k)), mon essai rend 12 manques sur 400 à m = 200 et 3 sur 400 à m = 400, soit environ 2 % par cellule (`essai-garde-reference-v1.py`, `190b6493…` ; sortie `ff2a41b9…`) ; sur 48 cellules, la garde manque au moins une fois avec une probabilité d'environ 0,6. L'arrêt 20 déclare alors la référence « non lisible », la retire du rapport et retient le rapport des candidates jusqu'à un audit. La garde échoue donc à R5 sur son propre cas sain. Par ailleurs, la section ne dit pas quand la garde lit les valeurs de la référence, alors que le § 10, point 4, veut une lecture unique à l'étape 8.
Correction proposée : au § 9, « chaque prédiction est éprouvée au niveau 1 − 0,01 / C, C étant le nombre de prédictions de l'objet vrai jouées, calculé par programme sur les mondes scellés ; la garde manque si l'une manque » ; ajouter C aux valeurs dérivées sans choix des critères (§ 6) ; ajouter au § 10 : « la garde est calculée par programme au passage du noyau et ne rend que passé ou manqué ; les valeurs de la référence ne sont lues qu'à l'étape 8 ». Là où V1★ vient du tirage scellé de dix millions de points, dire que son erreur (environ 3 × 10⁻⁵ à 1 %) est commune aux 2 000 tirages et l'ajouter à la demi-largeur.

**2. Critères, § 1 (contrôle par l'aire) et § 8, point 2 (saboteur gelé par son aire) : le cas du réseau n'est pas fermé.**
Ce qui ne va pas : le concepteur a lu le rapport v5 du programme de vérification ; le rapport v6 (`28d9155f…`) le remplace et ajoute sa remarque 9 : sur une grille grossière (famille G), l'aire est une fonction en escalier, l'intervalle de 0,005 autour de l'aire dite peut n'être atteint par aucun décalage, et « une tolérance propre aux réseaux attend un mot de la mère ». Sous la lettre du § 8, point 2, « la translation exacte qui réalise cette aire » n'existe pas alors : le saboteur de G ne serait pas jouable, et la règle qui le rendrait jouable serait choisie après la lecture de la sortie, ce que l'en-tête des critères interdit.
Correction proposée : écrire maintenant, au § 8, point 2 : « sur un réseau, le décalage joué est la plus petite translation dont l'aire, ex æquo pour moitié, atteint ou dépasse l'aire dite ; le contrôle par l'aire y est conforme si l'aire dite tombe dans le palier atteint ou à 0,005 près » (à confirmer par la mère, puisque le rapport v6 le lui renvoie) ; citer le rapport v6 dans les pièces lues.

**3. Critères, § 8, point 3 (décision D-1) : deux saboteurs différents dans la même famille.**
Ce qui ne va pas : la conversion des témoins par le programme de vérification pose le saboteur de F sur la loi d'avant la dérive (choix `CH5`, arbitrage de l'unité, § 3, point 4 ; l. 1468 du programme v3) ; D-1 (a) pose celui du générateur sur la loi d'après. De même, le générateur joue la translation gelée par l'aire, alors que la vérité des témoins à saboteur est recalculée à partir du nombre de l'auteur (au plus 0,005 d'aire d'écart). La valeur vraie d'un témoin à saboteur peut donc ne pas être celle du monde joué ; pour un témoin libre de grandeur « puissance » dans F, l'écart n'est pas petit (aire 0,80 en usage contre 0,70).
Correction proposée : « par famille et par tranche, un seul saboteur, celui du générateur (aire gelée ; dans F, en usage) ; la vérité de tout témoin à saboteur est calculée sous ce saboteur ; si le programme de vérité scellé ne le permet pas, les témoins à saboteur de F ne sont pas convertis et c'est rapporté, sans repli ». Dire dans la décision D-1 que (a) demande ce point, que (b) n'aurait pas demandé.

**4. Critères, en-tête (« leur lettre prime ») et § 3 (méthode de Student) : la pièce contredit la lettre qu'elle dit faire primer, et laisse une porte après la sortie.**
Ce qui ne va pas : le préenregistrement court v6 (« Métrique ») et l'ordre v6 (§ 7, « ce qui tue », et « ce qui attend le gel ») disent la méthode de l'intervalle d'une moyenne ou d'un écart apparié « à geler avec les mondes ». La règle de l'en-tête donne alors la primauté à cette lettre sur les points marqués « fixé ici ». De plus, le § 3 permet que la méthode de l'auteur « remplace celle-ci par une version neuve […] écrite avant toute lecture d'une issue », donc après la lecture de la sortie de l'auteur.
Correction proposée : dans l'en-tête, « les points marqués [fixé ici] priment sur les passages de ces textes qui les renvoient "au gel avec les mondes" ; la version suivante du préenregistrement court les reprend » ; au § 3, remplacer la dernière phrase par « La méthode que l'auteur propose est rapportée à côté ; elle ne remplace pas celle-ci dans cette course. » Dire aussi que l'ordre v6 n'est pas scellé (le registre des scellements ne porte que l'ordre v4) et que ce sont ses versions empreintées qui font foi pour cette pièce.

**5. Critères, § 2, dernier paragraphe : le relèvement du nombre de tirages n'a ni critère ni valeur.**
Ce qui ne va pas : « ne sépare pas 1 % de 2 % » n'est pas défini, et la valeur à laquelle R serait relevé non plus : c'est un nombre fixé après la lecture des mondes, hors de la liste du § 6.
Correction proposée : « R est relevé si, pour un taux vrai moyen de 1 % et de 2 % sous la loi scellée, les intervalles à 99 % de la moyenne de V1★ se recouvrent ; il passe alors à 5 000, puis à 10 000, au premier qui les sépare » ; la largeur entre aux valeurs dérivées.

**6. Critères, § 5 (T14) et § 4, point 2 (borne c(W)) : la sorte de T14, et son entrée dans W, se décideraient après la lecture.**
Ce qui ne va pas : D-6 dit le sort de T14 « celui du recalcul scellé » et précise qu'un sort « tient » n'est pas une épreuve morte, mais ne dit pas s'il devient alors un « doit tenir » compté dans W, ou un témoin « de marge ». W fixe c(W).
Correction proposée : écrire la règle maintenant : « couverture recalculée sous 0,930 : doit mourir ; de 0,930 à 0,95 : de marge ; 0,95 ou plus : doit tenir, compté dans W » (0,930 est l'angle mort que le préenregistrement court cite).

**7. Critères, § 9 (épreuve d'invariance au flux) : ses paramètres ne sont pas fixés, et elle s'écrirait quand les fiches seront connues.**
Ce qui ne va pas : parts du saboteur dans les deux flux, signal, nombre de tirages, ce qui compte pour « la décision change » : rien n'est fixé. Écrite après la mise en fiches, l'épreuve serait réglée en sachant quelles candidates se recalent.
Correction proposée : fixer ici les paramètres (même tirage de calibration ; flux 1 fait des seuls épisodes honnêtes ; flux 2, les mêmes épisodes honnêtes entrelacés à part égale d'épisodes du saboteur au signal moyen ; marque si une décision sur un même épisode honnête diffère, sur les cent premiers tirages) et exiger que son programme soit scellé avant l'étape 2 (mise en fiches).

**8. Critères, § 4, point 2 : la loi binomiale de c(W) suppose des morts indépendantes.**
Ce qui ne va pas : des témoins « doit tenir » joués sur les mêmes tirages de calibration (même monde, même n) ont des morts corrélées ; sans indépendance, la seule borne générale (Markov) donne, à W = 30 et c = 1, 30 × 0,005 / 2 = 0,075, non 0,01.
Correction proposée : « chaque témoin reçoit sa propre suite de graines, dérivée par clé ; leurs tirages sont indépendants ».

**9. Critères, § 6, lignes 2 et 4 : contraintes trop lâches.**
Ligne 2 : ajouter « 200 et 400 obligatoires » (la mort « sans gain » se lit à 400 ; le préenregistrement court tient n ∈ {200, 400} pour l'énoncé du problème). Ligne 4 : ajouter « trois aires distinctes, croissantes, entre 0,5 et 1 », puisque le « signal moyen » se définit comme celle du milieu.

**10. Réponse sur le véhicule, « Ce qui manque » : juste, mais incomplète.**
La réponse est juste : « oui, sur le dessin ; non, aujourd'hui » ; l'absence du lanceur est vérifiée par moi sur `origin/main`, sur la tête de la branche et sur disque. Manquent à la liste : (i) les gardes des arrêts 20 et 21, programmes à écrire et éprouver sur un cas sain et sur un artefact (R5), dans le noyau ; (ii) l'épreuve d'invariance des critères, § 9 (classe B) ; (iii) dans le générateur, le tirage de témoins sous la loi de calibration pour jouer l'objet faux sur la famille F scellée ; (iv) une ligne qui dit que l'ordre v6, § 7 bis (« Qui écrit, et quand »), fait écrire le générateur par l'auteur de la troisième lignée, alors que le texte servi v3 (§ 5 et § 7), postérieur et scellé, le fait écrire chez la mère : c'est ce dernier qui vaut, et la réponse s'appuie sur lui.

**11. Rapport, « Trouvaille de côté », point 1 : un chiffre mêle deux lectures.**
« Sous la condition de la course […] 1,2 point ; si le saboteur est posé avant la dérive, de 0,7 » : 0,7 est l'avance sans condition (0,0539 − 0,0471, bloc [E], aire 0,80) ; sous la condition, elle vaut 0,6 (0,0349 − 0,0293). Écrire 0,6, ou dire « sans condition ».

## Ce qui est conforme

- Point 8 de l'arbitrage : la référence reste hors de la liste scellée (`4e0aaaee…`, quatorze textes), jouée hors course, par programme, chez la mère, sur les mondes scellés, sous le titre imposé, à 200 et 400 témoins, rang 2 et 4, graine nommée à part ; aucune classe d'issue, aucune candidate tuée ni classée contre elle ; interface servie, mandat et liste inchangés.
- Texte extrait : `sed -n "106,113p"` sur la fiche rejouée, `cmp` muet contre le texte versé ; l'étendue fausse 106 à 114 diffère (EOF après l'octet 1 834).
- Programme de calcul rejoué deux fois, `cmp` muet contre la sortie versée les deux fois (`685045b7…`). Valeurs reprises dans les pièces conformes à la sortie : [A] 0,4456 ; 0,7012 ; 1,1902 ; 2,3262 ; [B] taux de la base aux trois tailles ; [C] 0,00995, 0,00998, 0,5954, 0,5675 ; [D] 0,0289, 0,0294 ; [F] témoins imposés « sans loi », qui retrouvent les valeurs de l'ordre v6, § 7 bis ; [G] c(W). L'aire en usage de 0,70 sous D-1 (b) est vérifiée à la main : Φ((1,1902 − 0,4456) / √2) ≈ 0,70.
- Réserve « sans gain en monde à dérive » (GO-2026-11-21-35, D-2 (b)) : écrite, avec les taux de la base aux trois tailles, marqués non opposables sous loi normale, et la phrase permise. Ligne d'arrêt « aucun score du suspect dans l'étalonnage d'un seuil » : arrêt 21 et critères, § 9. Unité des décalages : conforme à la phrase opposable de l'arbitrage (§ 1) et au contrôle par l'aire (§ 2), au réseau près (correction 2).
- Liste nominative : complète au regard des blocs du texte servi (§ 4.2), au resserrement des lignes 2 et 4 près.
- Section « Relevé de méthode » : présente dans le rapport du concepteur (§ 4), rubriques dans l'ordre, deux « Sans objet » motivés.

## Relevé de méthode

### Chaîne de raisonnement

1. Les pièces relues sont celles que le concepteur a rendues : huit empreintes recalculées par `sha256sum`, égales à sa table et au mandat (en-tête).
2. Les sources de `origin/main` sont celles que les pièces citent : `4286bf39…`, `64e06388…`, `44d1e86f…`, `4a1579b3…`, `a8f8acfa…` recalculées sur les copies `git show`.
3. Le texte extrait est fidèle : `sed -n "106,113p"` puis `cmp` muet ; objet faux, étendue 106 à 114, `cmp` en écart (`extrait-rejoue.md`, `extrait-faux-106-114.md`, dans mon dossier).
4. Les calculs du concepteur se rejouent : deux rejeux, deux `cmp` muets (`rejeu-1.txt`, `rejeu-2.txt`, tous deux `685045b7…`).
5. Aucune donnée qui sert au verdict n'existait quand les critères ont été écrits (11:41:46Z) : GO-2026-11-21-37 ne laisse partir l'appel qu'après le scellement des critères ; aucune ligne de `registres/go.md` jusqu'à -50, ni aucun scellement de `registres/scellements-v1.md` à `fdbc8a73…` (13:06:03Z), ne dit l'appel parti ou des mondes reçus ; le lanceur n'existe pas (`git cat-file -e` sur `origin/main` et sur la tête de la branche ; `sha256sum` sur disque). Donc aucun choix des pièces n'a été fixé après une lecture.
6. Le préenregistrement court v6 et l'ordre v6 renvoient la méthode de l'intervalle apparié et la borne des morts « au gel avec les mondes » (`a2f1eaee…`, « Métrique », arrêt 16 ; `208454c5…`, § 7 et § 7 bis) ; les critères les fixent, mais disent la lettre de ces textes prioritaire (`ea5f224f…`, en-tête) : correction 4.
7. Le rapport v6 de vérification (`28d9155f…`, § 6, remarque 9) laisse ouverte la tolérance des réseaux ; les critères gèlent le saboteur par une « translation exacte » (§ 8, point 2), qui n'existe pas sur un réseau : correction 2.
8. L'arbitrage de l'unité (`a8f8acfa…`, § 3, point 4) place le saboteur de F, pour la conversion, sur la loi d'avant la dérive ; D-1 (a) place celui du générateur après : correction 3.
9. La garde de l'arrêt 20 manque sur l'objet vrai environ 2 % des fois par cellule (essai rejouable, `190b6493…`, sortie `ff2a41b9…`) ; au moins 48 cellules (texte servi `f3d87162…`, § 3.2 : neuf familles imposées, trois tranches ; deux valeurs de m) : 1 − 0,981⁴⁸ ≈ 0,6 ; correction 1. **Supposé** : l'indépendance des cellules entre elles, qui tient si chaque jeu de témoins a sa graine.
10. Les points laissés à après la sortie (corrections 5, 6, 7) se lisent dans les pièces elles-mêmes (critères, § 2, § 5 et § 9 ; rapport, D-6).
11. La famille H : le texte servi dit « les épisodes d'usage viennent de familles neuves » (§ 3.2, ligne H) ; la loi des témoins de la section (§ 5) lui est donc conforme à la lettre ; reste, comme le concepteur le dit, à voir sous quelle loi le noyau calcule V1★.

### Objets de contrôle

- **Mécanisme : ma propre garde (`cmp`) sur le texte extrait.** Objet vrai : l'étendue 106 à 113, attendu muet ; rendu : muet. Objet faux : l'étendue 106 à 114, attendu en écart ; rendu : « EOF après l'octet 1 834 ».
- **Mécanisme : la garde de l'arrêt 20 (prédictions de l'objet vrai).** Objet vrai : V1★ de loi bêta exacte, prédit par moi d'avance : environ 1 à 2 % de manques par cellule ; rendu : 12 sur 400 et 3 sur 400. Objet faux : témoins tirés de la loi de calibration sous la dérive qui triple 1 %, prédit : tué à chaque réplique ; rendu : 40 sur 40 aux deux valeurs de m (moyennes 0,0290 et 0,0296, proches du bloc [D]).
- **Mécanisme : le critère « invalide, en moyenne » appliqué à l'objet faux** : même essai, objet faux ci-dessus ; son objet vrai est l'objet vrai ci-dessus, qui n'est jamais tué par ce critère (borne basse sous 1 % : k / (m + 1) < 1 %).
- Limite : mes essais tirent V1★ de sa loi exacte, non par le noyau, qui n'est pas écrit.

### Premier pas non justifié

Le pas 9 : le nombre de cellules est une borne basse tirée du texte servi, non des mondes scellés, et l'indépendance des cellules est supposée. Le justifierait : le compte des prédictions par programme sur les mondes scellés, et la règle de graines par clé que la section exige (§ 5).

### Mode d'échec affecté

Question : un seuil, un critère ou un choix d'analyse a-t-il été fixé après lecture des données qui servent au verdict ; le jeu final a-t-il été lu plus d'une fois ?

- **Pour ce qui est fixé : tenu.** Toutes les pièces sont datées de 11:41:46Z ; aucune sortie d'auteur, aucune fiche, aucune issue n'existait, ni n'existe à 13:06:03Z sur `origin/main` (pas 5). Les calculs ne lisent aucune donnée (loi normale seule, bloc d'en-tête du programme). Aucun jeu final n'a été lu ; la section ne lit la référence qu'une fois, à l'étape 8 (§ 10, point 4), sous réserve de la correction 1.
- **Pour ce qui reste ouvert : cassé, sur cinq pas.** Les pièces laissent se fixer après la lecture de la sortie de l'auteur : la tolérance des réseaux (correction 2) ; la méthode d'intervalle, par version neuve (correction 4) ; la valeur relevée de R (correction 5) ; la sorte de T14 et son entrée dans W (correction 6) ; les paramètres de l'épreuve d'invariance, après la mise en fiches (correction 7). Preuve : les passages cités à chaque correction ; la règle de l'en-tête des critères (« rien de chiffré ne se fixe après la lecture de la sortie, hors de la liste du § 6 ») ne les couvre pas.
- Un choix fait en connaissant l'effet attendu : D-1 (a) rend la base plus dure à battre dans F (puissance de 4,7 % à 10,6 % à 400, bloc [E]). Fixé avant toute donnée et sans candidate connue, il ne vise aucun signe ; il est dit par le concepteur. Tenu.

### Dérivation de l'énoncé seul

Sans objet : je suis contre-lecteur, non agent de re-dérivation.

### Trouvaille de côté

1. L'ordre v6 définit V1★ pour « la règle telle que ce tirage l'a réglée » : pour une candidate qui se recale sur le flux d'épreuve, ce taux vrai n'est pas défini sans la composition du flux. La marque de la correction 7 ne le règle pas ; à porter à l'ordre. Non poursuivi.
2. Le concepteur dit que l'avance de la référence vient surtout de la prudence de la base dans le monde sain ; c'est juste à la lecture du bloc [E] (7,2 points sans dérive, 1,2 en dérive sous condition). Rien de plus.

### Évaluateur et conseil

- Ce qui juge ma pièce : la vérification des corrections par moi-même, puis le scellement par la mère. Aucun témoin n'admet ce juge.
- Par où elle pourrait être bien jugée sans le mériter : mon essai de la garde tire V1★ de la loi bêta, comme le ferait un générateur juste ; il ne dit rien d'un noyau faux. Les corrections 2 et 3 reposent sur des pièces (rapport v6, arbitrage de l'unité) que le concepteur n'avait pas toutes ; je n'ai pas lu le programme de vérité, qui peut déjà traiter le point 3.
- Conseil à qui portera les corrections : écrire C, la règle du réseau, la règle de T14 et les paramètres de l'épreuve d'invariance avant toute autre retouche, puisqu'ils doivent précéder la sortie de l'auteur ; garder la référence sans classe.
