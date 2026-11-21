# Contre-lecture — conception v2 de la course « seuil et moniteurs », option (b) — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O. C'est le même contre-lecteur qu'à la v1 (R-4389 : « même contre-lecteur ensuite ») ; je n'ai écrit aucune des pièces relues. 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit, aucun lancement. Aucun refus de permission, de classifieur ou de garde.
- Pièces relues, toutes en entier, dans `docs/notes/ideation-seuil-moniteurs-v1/conception-v2/`. Table `empreintes-dossier-v2.txt` (`e66591ad315d6b585dbececac3c89ad91477219679d1325f58bfeb895bd96362`) vérifiée par `env -C … sha256sum -c` : six « OK ».

| pièce | empreinte |
|---|---|
| ordre v2 | `1fbd04c3…` |
| devis v2 | `67b64e6d…` |
| programme du devis v2 | `2c3d68a0…` |
| sortie du programme | `5b06bec2…` |
| préenregistrement court v2 | `54a89d27…` |
| rapport v2 | `c7c54d0d…` |

- Sources lues sur `origin/main` après `fetch`. Le commit courant est `a5f06087560ff8fb320ceef294ac303d34b2844f`. Au commit du rédacteur, `332080c5…`, les registres rendent `ba9ba9eb…` (go) et `a1f662fa…` (décisions), égales à ses empreintes. Lignes relues : GO-2026-11-20-10, GO-2026-11-20-22, GO-2026-11-21-13 à GO-2026-11-21-16 ; R-4371, R-4372, R-4374, R-4377, R-4381 à R-4386. Code relu : la table de prix du collisionneur v9 v3 (`850df311…`, lignes 100 à 141).

## 0. Verdict : **À corriger**

1. **Corrections de la v1** : toutes portées, ou dites sans objet sous (b) à juste titre, à trois reprises près. (a) La base invalide « ne tue personne » : c'est trop large. (b) Le témoin de la base n'a pas de monde fixé. (c) La dispute entre traducteurs ne porte pas sur les deux champs qui décident de la mort (§ 1).
2. **Programme v2** : juste, et rejoué à l'octet. Un défaut d'arrondi : un plafond minimal s'arrondit vers le haut, donc 75,77 et 114,07, non 75,76 et 114,06. C'est **114,07** qui est juste (§ 2).
3. **Mise en fiches** : sans juge au sens de N-058. Mais la pièce ne dit pas que `garantie_dite` et `suppositions_declarees` sont aussi des lectures de modèle, et ce sont elles qui décident de la mort (§ 3).
4. **Morts et témoin** : désormais cohérents dans leur principe. Deux trous de bord, la base invalide et le monde des témoins (§ 4).
5. **Sources** : suivre la ligne du registre est juste. Deux faits manquent. La liste des propositions nommées par Lazar oublie le troisième point accordé par GO-2026-11-21-15. Et la note du moniteur de dissonance est déjà rendue (R-4382) (§ 5).
6. **Noms de modèles** : remplacés dans le jeu, chaque ancre comptée. Deux points restent à trancher : « Kimi absent » et « Claude » (§ 6).
7. **Écart R12** : acceptable tel quel (§ 7).
8. **Un fait faux, en plus** : l'ordre v2, § 2.1, dit que le paquet de la version 68 et les lanceurs ne sont pas sur `origin/main`. Ils y sont depuis R-4385, y compris au commit cité par le rédacteur (§ 5).
9. **Un nœud de faisabilité** : la contrainte de lignées des mondes (D-M4), des traducteurs et de l'expérimentateur ne tient qu'avec une affectation précise (§ 3, point 4).

Jeu de corrections : vingt-sept remplacements, en quatre fichiers JSON. Chaque ancre est comptée une fois par `grep -c -F -e`. L'essai sur copie passe pour les quatre (§ 8).

## 1. La table « correction → lieu » (rapport v2, § 3), ligne par ligne

| correction | vérifiée dans la v2 | jugement |
|---|---|---|
| K-O1, K-P4 « sans gain » apparié | ordre § 6, table et alinéa ; § 7, V3Δ et « Ce qui tue » ; préenregistrement, « Seuil » | **portée** |
| K-O2, K-O3, K-P2 V1★, le tirage pour unité | ordre § 7 (V1★ ; V1 qui « ne tue jamais » ; trois morts « invalide » sur les R tirages) ; préenregistrement, « Métrique » et « Seuil » | **portée** |
| K-O4 base précisée | ordre § 7, alinéa « La base », (a) à (c) ; préenregistrement, C3 | **portée, mais élargie à tort**. Ma correction disait « sans mort “sans gain” » ; la v2 dit « ne tue personne », ce qui ôte aussi la mort « invalide » sur ce couple. C3 ne nomme que la famille D, alors que la famille F (dérive) peut rendre la base invalide elle aussi. **K2-O11, K2-P1** |
| K-O5, K-Q2 champ fermé et table | ordre § 3, sept valeurs plus « aucune dite » ; § 7, table A à G ; préenregistrement, « Seuil » | **portée**. « Aucune dite » vaut « déclare tenir partout » : c'est dur, mais dit |
| K-O6 D-M4 | ordre, en-tête ; § 2.2, point 6 ; § 7, changement 1 | **portée**. La clause « autre lignée que les cinq espèces » de D-M4 tombe en silence sous (b) ; à dire, et la faisabilité est à écrire (§ 3, point 4). **K2-O12** |
| K-O7 D-M2 | en-tête, § 0 point 5, § 2.2 point 6, § 10 ; préenregistrement, point 2 | **portée**. La note du moniteur de dissonance est rendue depuis 06:59Z (R-4382, `403fe3e2…`), ce que la v2 ne dit pas. **K2-O1, K2-P3, K2-R1** |
| K-O8, K-O9 `paquet/` | ordre § 2.1 | **portée** (empreintes `c1aeab4c…` et `6fce1735…` égales) |
| K-O10 GO-2026-11-20-10, point O3 | ordre § 2.1, citation exacte de la ligne | **portée** |
| K-P1, K-R1 règles du rédacteur | devis § 0 (table et troisième point), titres des § 2, § 4 et § 5 ; préenregistrement, « Prédiction » ; ordre § 0, point 6 ; rapport § 0 | **portée** (voir § 2, point 4) |
| K-P3 M6 | préenregistrement M6, sur `prediction_dite_par_le_texte` | **portée, adaptée à juste titre** : sous (b), aucun auteur n'écrit de test pour la course |
| K-P5, K-D1, K-D2 réservation | programme v2, champ `regle_de_reservation` ; devis § 3 | **portée**, sous réserve de l'arrondi (§ 2) |
| K-P6 arrêt n° 14 | préenregistrement, arrêt n° 14 et « Ordre des opérations » ; ordre § 9 | **portée** |
| K-D3 Luc « estimée » | devis § 6 | **portée** |
| K-Q1 question | sans objet | **juste** : la question n'est plus servie (rapport § 4) |
| K-Q3 neutralité | ordre § 7, deux réglages, « aucun n'est dit vrai » ; préenregistrement, « Hypothèse » et « Prédiction » | **portée** |
| Rem-1, Rem-2 | sans objet ; l'universalité n'est pas revendiquée (ordre § 7, changement 2) | **juste**, et plus honnête que la v1 |
| Rem-3, Rem-4, Rem-5 | devis § 2 et § 7 ; devis § 6, GO-2026-11-20-22 (relu : « l'aiguilleur et l'espèce 4 sur Luc ») ; ordre § 2.1 | **portées** |
| § 5, point 5 | ordre § 7 « Ce qui attend le gel » ; préenregistrement, point 5 ; risque du témoin invalide proposé à 5 % | **portée** |

## 2. Le programme v2

1. **Rejoué deux fois** (`python3 -B …/calcul_devis_course_seuil_et_moniteurs_v2.py`, vers `v2-sortie-1.json` puis `v2-sortie-2.json`) : `cmp` muet entre les deux, et muet contre la sortie versée (`5b06bec2…`). Arithmétique seule : `json` et `decimal`, aucun fichier lu, aucun réseau, aucun aléa.
2. **Cas refaits à la main :**
   - étage : 14 × 1,0664 = 14,93 ; 28 × 2,6832 = 75,13 ; 28 × 3,00 = 84,00 ;
   - mise en fiches, par appel : 0,04 + 0,08 = 0,12 ; 0,24 + 0,30 = 0,54 ; 0,24 + 0,40 = 0,64 ; fois trente-deux appels : 3,84 / 17,28 / 20,48 ;
   - **totaux : 20,77 / 97,41 / 114,48, justes.**
   - Leviers : (b) 15 × 6 + 30,48 = 120,48 ; (c) 8 × 6 + 30,48 = 78,48 ; D-M6 (b) 24 × 0,64 = 15,36. Justes.
   - Entrées : S1 et S2 comme à la v1 ; S3 égale à la table du collisionneur (borne haute 10 et 50, basse 4 et 20 hors l'espèce exclue, 2,5 caractères par jeton) ; S4 GO-2026-11-21-16 (120) ; S5 R-3984 ; S7 R-4371 (« 0,65 USD au prix haut » et 0,41). Égales.
3. **Réservation sous (b).** Une unité coûte 5,366 49 au cas haut et 6,00 au pire. Au cas haut, les quatorze partent : après treize, 69,76 sont dépensés, sous 84 − 6 = 78. Au pire aussi : 78 ≤ 78. Plafond pour toutes : 13 × 5,366 49 + 6 = **75,764…** au cas haut ; 84 au pire.
   - **Arrondi.** Le programme arrondit au plus proche. Pour un plafond *minimal* en cents, il faut arrondir vers le haut : à 75,76, la quatorzième ne partirait pas (69,764 + 6 = 75,764 > 75,76). **Il faut 75,77.**
   - **Contrôle sur la v1 : 19 sur 20, 101,96, 8 sur 10, 60,40, justes.** Pour le plafond des vingt, la borne exacte est 114,0633… : **114,07 est juste** comme plafond minimal en cents, et 114,06 laisserait la vingtième dehors. 60,40 tient par chance de l'arrondi (borne 60,398…).
   - **K2-D1 à K2-D3, K2-R4.** Un programme v3 qui arrondit vers le haut est laissé à la mère ; le texte corrigé suffit à ne tromper personne.
   - Remarque : sous (b), le plafond de l'étage (84) est égal à la somme des pires. Tout dépassement d'un plafond de session par le véhicule, même d'un appel, prive la dernière candidate de sa place. C'est un point à éprouver à blanc.
4. **« Règles du rédacteur »** : marquées dans le devis (table, troisième point, titres des § 2, § 4, § 5), dans le programme (R1, R2, R4 ; R3 « supposé »), au préenregistrement (« Prédiction » ; plafond de session) et au rapport (§ 0). Le préenregistrement, « Tailles » et ligne « ligne de calcul », renvoie au devis sans répéter le mot : c'est suffisant. **Conforme.**
5. **Remarque sur la mise en fiches** : le plafond de sortie de 8 000 jetons par appel ne tient pas pour une lignée qui consomme une provision de réflexion. La table du collisionneur en donne 8 192 et 32 768 à deux espèces du deuxième relais. Il est à fixer avec la lignée retenue au complément de valeurs, et le pire par appel est à refaire s'il change.

## 3. La mise en fiches et N-058

1. **Sans juge au sens de N-058** (`854f2724…` : l'interdit porte sur le choix d'**agents** sur un verdict de juge). Aucun modèle ne dit ce qu'une idée vaut. Les candidates sont tirées par graine, ou nommées par Lazar avant tout résultat (D-M7, écrit et déclaré). Les comptes par source ne servent à classer aucune espèce. **Oui.**
2. **Ce qui reste une lecture de modèle n'est dit qu'en partie.** L'ordre, § 4, dit : « découper » et « dire calculable ou incomplète ». Il ne dit pas que remplir `garantie_dite` et `suppositions_declarees` est aussi une lecture. Or ces deux champs décident de la mort et des mondes où elle se lit. Et la « traduction disputée » ne porte que sur `garantie_dite`, `etat` et `sorte`, non sur `suppositions_declarees` ni sur `parametres`, qui changent pourtant la règle jouée et ses mondes. **K2-O7, K2-O8.** Les critères gelés disent déjà « dans la lecture qu'en a faite la mise en fiches » : c'est juste.
3. **Forme fixe, extrait vérifié à l'octet, aucun chiffre ajouté (arrêt n° 13), aucune fusion, personne qui complète** : tenus (ordre § 3 et § 4 ; préenregistrement, arrêts n° 12 et n° 13). Une asymétrie déclarée : l'union vaut pour trouver une proposition, mais l'`etat` joué est celui du premier traducteur, tiré par graine. Acceptable, puisque c'est dit.
4. **Faisabilité des lignées** (non vue par le rédacteur).
   - Les contraintes posées : l'ordre, § 7, veut l'auteur des mondes « d'une autre lignée que l'expérimentateur et que les deux traducteurs » ; l'ordre, § 4, veut deux traducteurs de deux lignées, « dont aucun n'est l'expérimentateur ».
   - Trois lignées sont disponibles, l'espèce exclue mise à part. La seule affectation possible est donc : un traducteur de la lignée de l'expérimentateur, l'autre d'une deuxième lignée, l'auteur des mondes de la troisième. Celui-ci ne peut alors pas être une session de la lignée de l'expérimentateur.
   - Quant à la clause de D-M4 « autre lignée que les cinq espèces », elle est intenable sous (b), puisque les auteurs des textes couvrent toutes les lignées. Elle tombe sans dommage : ils ont écrit avant tout monde.
   - **K2-O12** ; à fixer en D-M9.

## 4. Le test de mort, les morts et le témoin

1. **Dans le principe, cohérents.** Une règle égale à la base a un V3Δ nul à chaque tirage, donc une borne basse de 0, qui « ne dépasse pas zéro » : elle meurt « sans gain », comme son témoin l'exige. La mort « invalide » se lit sur V1★ et sur les R tirages. La garantie « aucune » ne meurt que « sans gain ». Le test est tiré de la garantie dite, le même pour toutes ; c'est cohérent avec l'absence d'auteur du test sous (b).
2. **Trou 1 : la base invalide.** « Ne tue personne » dispense une candidate qui, comme la base, ne tiendrait 1 % qu'à partir d'une centaine d'épisodes, de mourir « invalide » sur la tranche de quarante. Il faut garder la mort « invalide » et ne retirer que « sans gain ». Les couples où la base est invalide sont à calculer, non à nommer : la famille F peut en donner. **K2-O11, K2-P1.**
3. **Trou 2 : le monde des témoins.** Le témoin « base » déclare des suppositions. S'il est joué sur la tranche de quarante de la famille D, ou sur F, sa garantie « en moyenne » est violée : il sort « morte, invalide », le témoin est manqué, et aucun étage ne part. Il faut jouer les témoins sur le monde A. **K2-O10, K2-P2.**
4. **Remarque** : pour le témoin « base contre elle-même », la variance de V3Δ est nulle. La méthode de l'intervalle apparié, gelée avec les mondes, doit rendre [0, 0] sans faute de calcul ; c'est un cas à éprouver (règle R5).

## 5. Les sources, et deux faits

1. **Le choix de la ligne du registre est juste.** La ligne GO-2026-11-21-16 inscrit le mot de Lazar et fait foi contre un message de la mère. Le rédacteur l'a dit, a compté quatorze textes en les disant « supposés », et porte l'écart à la mère (D-M6). Écarter les cinq critiques croisées est motivé, et la perte est dite (ordre § 11, réserve 4). Le compte de quinze du message correspond aux quinze cellules du collisionneur ; quatorze en est une autre lecture, non une erreur.
2. **Liste des propositions nommées incomplète.** GO-2026-11-21-15, point 2, accorde les « points 1 à 3 » : seuil certifié avec sa bande de seuils ; seuil unique sur score normalisé ; **aiguillage en lecture rétrospective par texte à part**. L'ordre, § 5, ne nomme que les deux premiers, avec le moniteur de dissonance. **K2-O9.** Il se peut que l'aiguillage sorte « non calculable » sur des mondes de scores ; c'est la mise en fiches qui le dira.
3. **La note du moniteur de dissonance est rendue** (R-4382, 06:59:05Z, `403fe3e2…`) : test de rang de l'action parmi K actions du jumeau honnête, lu par la sonde de réussite attendue. L'ordre, § 7, changement 3, décrit le monde nécessaire comme « une action et une valeur lue » par pas, ce qui ne suffit pas à ce test. **K2-O13.** La même note prévoit son propre premier test de mort sur MATH500 public : la mère veillera à ne pas compter deux fois la même épreuve.
4. **Fait faux : le paquet de la version 68 et les lanceurs sont sur `origin/main`.** Au commit cité par le rédacteur, `332080c5…`, `git cat-file -e` trouve le paquet, et `git show` rend `course2_v68.py` à `c1aeab4c…` et le lanceur 10 à `f4196ec5…`, égaux. C'est le versement du véhicule de la course « nouvelles attaques » (R-4383, R-4385). Le lanceur 11 n'y est pas. L'ordre v2, § 2.1, dit « rien de cela n'est sur `origin/main` ». **K2-O5.**

## 6. Les noms de modèles

- Remplacés : « les deux notes de conception de [nom commercial] » devient « … du modèle F », en cinq lieux de l'ordre, un du préenregistrement et deux du rapport (K2-O1, K2-O2, K2-O6, K2-O12, K2-O14 ; K2-P3 ; K2-R3, K2-R6). La ligne de la table des sources qui nomme les trois auteurs des consultations devient « un texte du modèle F et deux textes de deux modèles du deuxième relais » (K2-O4). Je ne recopie ici aucun des noms retirés. La citation de GO-2026-11-21-16 devient « « collisionneur, […], moniteur de dissonance » (retrait fait ici : trois noms de modèles […]) », dans l'ordre et dans le rapport (K2-O3, K2-R2).
- **« Claude »**, nom de fournisseur, apparaît au devis (§ 6, « un modèle Claude », « une clé Claude désignée ») et au rapport (§ 6). Je l'ai remplacé par « les clés désignées Minuit, Luc et Rigaud » (K2-D4, K2-R5). Si la mère tient « clé Claude » pour une désignation du registre, ces deux remplacements peuvent être retirés sans toucher aux autres.
- **« Kimi absent »** (ordre § 4) reste : c'est une règle du mandat (« Kimi est absent »), déjà admise à la v1. Si la règle de versement l'exclut aussi, il suffit d'écrire « l'espèce exclue par la mère est absente ». **À trancher par la mère** ; je ne l'ai pas mis au jeu.
- Après le jeu, une recherche sur les quatre sorties d'essai ne trouve plus que cette occurrence.

## 7. L'écart R12

**Acceptable tel quel.** R12 interdit d'écraser une version qu'un autre a pu lire, citer ou sceller. Ici, la première forme du calcul et de l'ordre n'a été ni rendue, ni citée, ni versée. Retoucher un brouillon avant de le rendre, c'est écrire, non écraser. La sortie rendue est égale à l'octet à celle du programme rendu (`cmp` muet). L'écart est déclaré (rapport § 5, points 1 et 2). Un v3 « à l'octet » n'apporterait rien.

## 8. Corrections (outil `scripts/remplacer_texte_exact_v1.py`)

Chaque ancre est comptée **1** par `grep -c -F -e` dans la pièce visée.

| fichier | empreinte | pièce | remplacements |
|---|---|---|---|
| `corrections-v2-ordre-v1.json` | `b8cd6d1755f08a92f7c9353d63e63c3770b6b29ef1de3cd0dc3fc42979d006a6` | ordre v2 | 14 : K2-O1, K2-O2, K2-O6, K2-O14 (« modèle F ») ; K2-O3 (citation avec retrait) ; K2-O4 (trois consultations) ; K2-O5 (`origin/main`) ; K2-O7 (champs disputés) ; K2-O8 (lectures de modèle) ; K2-O9 (troisième point de GO-2026-11-21-15) ; K2-O10 (témoins sur le monde A) ; K2-O11 (base invalide) ; K2-O12 (lignées, faisabilité, D-M4 sous (b)) ; K2-O13 (monde du moniteur de dissonance, R-4382) |
| `corrections-v2-preenregistrement-v1.json` | `5d664d89ae30a17e14ac6ec3991ecd3a10b0eded4d588080455ff49721a7b830` | préenregistrement court v2 | 3 : K2-P1 (C3) ; K2-P2 (arrêt n° 3, monde A) ; K2-P3 (« modèle F », R-4382) |
| `corrections-v2-devis-v1.json` | `84e164618dac54919a60fa110885a25b91033310787f5c68e239e48c019214c8` | devis v2 | 4 : K2-D1 (75,77) ; K2-D2 (114,07) ; K2-D3 (paragraphe du centime) ; K2-D4 (fournisseur) |
| `corrections-v2-rapport-v1.json` | `27a4b757f1118baa8227d4faac16dfb3043f22c16572554153caf41bc0d7826d` | rapport v2 | 6 : K2-R1 (« modèle F », R-4382) ; K2-R2 (citation avec retrait) ; K2-R3, K2-R6 (« modèle F ») ; K2-R4 (114,07, 75,77) ; K2-R5 (fournisseur) |

**Essai sur copie** (dossier `essai-v2/`, copies des pièces, d'empreintes égales à la table v2) : quatre « FAIT ».

| pièce | remplacements | empreinte de la sortie d'essai |
|---|---|---|
| ordre | 14 | `917868dbb811e95ace1cee55e96f94e56b7444fa6171684f22600a6c488390b1` |
| préenregistrement | 3 | `ee0bea7118efdf8dac4579d898b293613cf9a91b7a128236cf09c1abd86ae571` |
| devis | 4 | `b984983c61c31178069cf9f4c2124426b4ffb8e031509deaa6c391ee49ce6be1` |
| rapport | 6 | `3f9c4a676b54f19bef3b0d1346c2c2ff7c536b9e20df412f691acfe7b2776936` |

Le programme v2 et sa sortie ne changent pas.

## 9. Pour la mère et pour Lazar

**Pour la mère.**
- Appliquer les vingt-sept remplacements.
- Trancher « Kimi absent » et « clé Claude ».
- D-M6 : la ligne du registre, recommandée par le rédacteur comme par moi.
- D-M7 : y mettre le troisième point de GO-2026-11-21-15.
- D-M9 : l'affectation des lignées du § 3, point 4, qui est la seule possible.
- Fixer le plafond de sortie de la mise en fiches avec la lignée retenue.
- Accorder cette course avec le premier test de mort que prévoit la note du moniteur de dissonance (R-4382).
- Programme v3 pour l'arrondi : facultatif.

**Pour Lazar.**
- La ligne de calcul de 114,48 USD tient au centime sous le plafond indicatif de 120, et les quatorze unités partent même au pire.
- Aucune de ses trois lignes n'est une mesure.
- Une règle qui « tient » ne tient que dans la lecture qu'en a faite la mise en fiches, sur des lois choisies par nous.

— contre-lecteur de la conception seuil et moniteurs, modèle O
