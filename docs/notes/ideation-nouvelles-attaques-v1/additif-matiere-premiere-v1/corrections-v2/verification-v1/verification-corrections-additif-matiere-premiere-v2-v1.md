# Vérification des corrections — additif « matière première » v2, devis v2, liste des lecteurs v2 — v1

**À corriger.** Les quinze corrections sont portées comme la table le dit. Les motifs des trois « portées autrement » (C1, C4, C11) tiennent. Le calcul se rejoue à l'octet. Le mandat de fin des lecteurs ne dit plus rien des objets de contrôle. Mais la fuite n'est pas fermée en entier : des pièces de la même chaîne, que l'additif v2 cite, portent encore la construction et l'issue attendue des objets (point 1). Et un point délicat, le dixième, n'est pas laissé ouvert dans l'additif lui-même (point 2).

1. **Fuite résiduelle par les pièces de la chaîne.**
   - *Passages* :
     - additif v2, en-tête, l. 4 : il cite la v1 « archivée sans modification » et donne le chemin de la relecture « fuite de la vérité » ;
     - additif v2, § 6, « Qui la lit » et « Limites » : « un lecteur qui le lit apprend que des contrôles existent, non lesquels » ;
     - § 10, valeur 6 ;
     - rapport v2, PD8 et l. 92.
   - *Ce qui manque* : la règle de lieu ne protège que l'annexe. Or « lesquels », et même l'issue attendue, se lisent dans six pièces que rien ne met hors de portée des lecteurs :
     - la v1 de l'additif (`d283dfe8…`, § 6 : table complète des objets et de leurs issues) ;
     - la relecture « fuite de la vérité » (`c04e65e8…`, l. 11 : construction et issues recopiées), citée par son chemin à l'en-tête de l'additif v2 ;
     - le différentiel `differentiels-v1-v2/additif-v1-vers-v2.diff` (`977facb7…`, l. 142 à 146, 152 et 155 : la table v1, ligne par ligne) ;
     - le rapport v2 (`f9e21f62…`, l. 92 : « la ligne étrangère », « la ligne « redite » ») ;
     - la contre-lecture (`54df8945…`, l. 89 et 93 : « la ligne témoin ») ;
     - la v1 de la liste et celle du devis, avec leurs différentiels (« deux témoins », « 24 visées et 2 témoins »).

     L'annexe dit elle-même : « Rien n'y est ajouté aux objets de la v1. » Un lecteur qui ouvre l'une de ces pièces rend donc les issues attendues sans soin. C'est le défaut que la relecture jugeait cassé, déplacé d'une pièce.
   - *Correction* :
     - (a) À l'additif, § 6 « Qui la lit » et § 10 valeur 6, et au rapport, PD8 : la règle de lieu de l'annexe vaut aussi pour la v1 de l'additif, de la liste et du devis, pour les deux relectures de la v1, pour les différentiels et pour le rapport des corrections. Aucune de ces pièces n'est dans un lieu que les lecteurs ouvrent.
     - (b) Au rapport, l. 92 : remplacer les deux noms par « les objets de l'annexe », par un erratum de classe C.
     - (c) Au § 6, « Limites », écrire la phrase vraie. Si l'une de ces pièces est déjà versée dans un lieu que les lecteurs ouvrent, l'écrire ; les objets de l'annexe doivent alors être construits autrement que ceux de la v1. C'est un point pour la mère, à porter avant le scellement.
2. **Le dixième point délicat (plafond de sortie de GO-2026-11-21-47) n'est pas ouvert dans l'additif.**
   - *Passages* : additif v2, § 5, « Bornes » (règle « gelée », 16 000 jetons au plus, réflexion comprise) ; § 10 (aucune valeur ne le porte) ; § 11, trouvaille 2 (« Rien de cela n'est poursuivi ici »).
   - *Ce qui manque* : GO-2026-11-21-47 (`go.md` à `d481b9a3`, l. 646) est une règle permanente de Lazar : tout appel au modèle qu'elle nomme laisse au moins 16 000 jetons de texte après la réflexion. Ce modèle a rendu l'une des trois réponses (GO-2026-11-21-20, l. 619). Si le juge de l'espèce 1 est servi par lui, la borne gelée contredit la règle. Le rapport le dit (PD10, recommandation (b) si c'est le cas), mais le texte qui sera scellé le présente comme tranché.
   - *Correction* : ajouter au § 10 une valeur 13. La mère constate, avant le scellement, si le relais du juge de l'espèce 1 sert ce modèle. Si oui, les bornes et le plafond de ce relais s'écrivent dans une version neuve avant le scellement (PD10). Un renvoi d'une ligne au § 5.

Hors de ces deux points, rien ne manque pour le scellement.

- Vérificateur neuf, modèle O, d'un autre modèle que le concepteur (modèle F) ; sous-agent ; 2026-11-21. Je n'ai écrit ni la v1, ni la v2, ni aucune relecture. Pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit.
- Non ouverts : le registre servi réel, toute branche `quarantaine/…` ou `matiere-premiere/…`, `archives-reponses-modeles/`, `/root/.claude/`.
- `origin/main` relu à `d481b9a325b1aeb89cb764414caa4f3b73ee719d`, après `git fetch origin main`.
- **Écarts de procédure, dits** :
  - deux appels composés, chacun une commande suivie de `; echo` pour afficher le code de sortie : le jeu de l'objet faux et le `test -e` ;
  - deux recherches de contenu (Grep) sur le dossier `corrections-v2/` et son sous-dossier des différentiels, l'une en mode « compte ». Elles ont rendu des noms de fichiers, comme le ferait une liste ; je les dis.
- Aucun refus de permission, de classifieur ni de garde.

## Pièces relues (empreintes recalculées par `sha256sum`)

| pièce | empreinte | égale à la table du concepteur |
|---|---|---|
| additif v2 | `55d9491b8f7748c26192a582b1d06c8f3bcefceacb4285c55b662910bf1820dd` | oui |
| annexe des objets de contrôle v1 (bloc-notes du concepteur) | `7406e5375dbfb1117fa9510eb6b47cee3c14c272cbe2bcfa708dd6c548ff707d` | oui |
| devis v2 | `837e88e822de0cc699ba220317710adb85e2cb35aad1ba8d0db4fbd18a60f3cd` | oui |
| programme v2 | `6b684a3764a810612c661c04733afb5edba0c547357de615c0f22d4d549cf208` | oui |
| entrées v2 | `061584b71052784e48ec7e383d519b2f6e3e5f6724b0bac5109e69e4e4f7e9ce` | oui |
| sortie v2 | `941c18a3c6ac3904fe5134fe78e4a4232c073aee855930c749e0ca91ad3d8749` | oui |
| objet faux de la règle | `b096b4edc0bbeb20d08999e1c548dcd08d0350e31f2bd01e3c42c5cdee57d132` | oui |
| liste des lecteurs v2 | `d3c50f337de2fff711b8dca16169261d8140bd601ca18fb20b8b5e9bb40451f9` | oui |
| table des corrections | `0e45c8714d5d58b3a2f32ae613aa9c3fbdbde1f91dc4dc81dcbbd005dcf78254` | oui |
| rapport des corrections | `f9e21f62035cfddc6b134ea45809b25aeec77829b7752e4ffc25a0db4ded07c4` | oui |
| contre-lecture de la v1 | `54df89455503582b06b4e6acefa80ea9867085916bd9ba1652ce7aae03ecec93` | égale à la citation de l'additif |
| relecture « fuite de la vérité » | `c04e65e89cc5e65ece89e9d3fc68c77ca3dab084dcd261b10cf0d0ac4b376261` | égale à la citation de l'additif |
| V9, `origin/main` à `d481b9a3` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | égale à la citation |
| `registres/go.md`, `origin/main` à `d481b9a3` | `cec2e676961775d059a05129c257e86d476edb3d8707908a69cc0ab60219d381` | différente de `c454dea5…` (citée à `fed5dc2f`) : `main` a avancé ; je n'ai pas tiré `fed5dc2f`, le mandat ne m'autorisant `git show` que sur `origin/main` |

Les six différentiels ont été lus. Le différentiel de l'additif a été lu en entier. Pour les cinq autres : une recherche ciblée, avec le texte v2 à côté.

## Rejeu du calcul

- Deux jeux de `python3 -I calcul_devis_lecture_de_fin_matiere_premiere_v2.py ENTREES SORTIE` vers mon dossier, Python 3.13.18, chacun en code 0.
  - `cmp` jeu 1 contre jeu 2 : muet.
  - `cmp` jeu 1 contre la sortie versée (`941c18a3…`) : muet.
- Objet faux de la règle (`entrees-objet-faux-regle-v2.json`) :
  - attendu : code 1, aucune sortie ;
  - rendu : code 1, message « objet de contrôle non conforme : aucune sortie écrite » ; `test -e` sur la sortie rend 1, donc aucun fichier.
- La règle, refaite à la main :
  - à 10 et 50 : (2 − 1,20) / 0,00005 = 16 000 ;
  - à 2 et 10 : 176 000, ramené à 16 000 ;
  - à 15 et 75 : 0,20 / 0,000075 = 2 666,67, soit 2 666, pour un coût de 1,80 + 0,19995 = 1,99995 ;
  - à 16 et 80 : 0,08 / 0,00008 = 1 000, sous le plancher ;
  - à 20 et 100 : négatif.
- Les trois cas, refaits à la main :
  - bas : 8 000 × 2 + 2 000 × 10, soit 0,036 par appel et 0,288 au total ;
  - haut : 0,56 par appel, 4,48 au total ;
  - pire : 2,00 par appel, 16,00 au total.
- Égaux au devis, § 2.

## Correction par correction

| n° | sort dit | constat |
|---|---|---|
| C1 | autrement | Porté aux lieux dits : cinq espèces (additif § 1 et § 2 ; liste § 2) ; 450 et 456 (devis, en-tête, § 0, E8) ; arrêts n° 1 à n° 27 ; clés 30 et 40 ; les quatre pièces en tête de l'additif ; devis § 3 récrit ; la ligne de GO dit le refus possible de l'arrêt C. **Motif tenu** : GO-2026-11-21-28 dit « la part de l'espèce 3 […] sur Minuit diminue d'autant », et GO-2026-11-21-30 dit « la part de Minuit diminuée de la reprise des collisionneurs » (`go.md` à `d481b9a3`, l. 627 et 629). Ces deux lignes sont postérieures au calcul de la marge de 24,90 USD. Ne promettre aucune marge, et s'en remettre au reste calculé (arrêt C), va dans le sens prudent. |
| C2 | telle quelle | Aucun tirage ; ordre lexicographique des octets UTF-8, défini à la V9, l. 311, relue. Réserve 8 et PD1 présents. |
| C3 | telle quelle | Voie (a) : § 3, pas 2 et 3 ; § 5 « Gardes » ; liste § 1, ligne 5, et § 4, point 1 ; ligne de GO « peut n'acheter aucun avis » ; journal de la garde en quarantaine, la mère ne reçoit qu'un compte. La garde jouée avant le mot ne porte que sur le texte servi, les énoncés des visées et les lignes de contrôle des juges. C'est cohérent avec C5 : les énoncés de défense ne sont plus servis. |
| C4 | autrement | D9 à D13 présents ; D3 à D7 au format complet (D7 renvoie à PD2, qui l'est). La phrase du § 10 énumère huit choix, et chacun a sa décision (D2, D3, D6, D9 à D13). L'arrêt C est renommé « l'arrêt n° 12, lu sur la ligne à part ». **Motif tenu** pour la ligne « recette » : la V9, l. 328, dit bien « « recette », au coffre ». Garder la lettre ôte l'écart que la contre-lecture demandait de déclarer ; l'autre voie est ouverte en PD3. |
| C5 | telle quelle | Pas d'énoncé de défense servi aux juges, et aucune étiquette sur eux : additif § 2, § 5, F6, tableau du § 8 ; liste § 3. |
| C6 | telle quelle | Additif § 5, dernier tiret ; liste § 3 ; arrêt F refuse une étiquette attachée à un identifiant hors de la quarantaine. |
| C7 | telle quelle | Cinq issues, comptées chacune à part (additif § 5 et F6). |
| C8 | telle quelle | Arrêt C : « la part de la ligne sur cette clé, 8,00 USD » ; Minuit « calculé au registre des dépenses de `main`, jamais lu » ; pire sur le tarif relevé ; arrêt A exige les tarifs relevés et le devis recalculé. |
| C9 | telle quelle | Règle gelée, à la formule du contre-lecteur, avec un plancher de 2 000 jetons ; arrêt D ; devis § 2 et § 3 ; programme et cinq objets de contrôle, rejoués. |
| C10 | telle quelle | Arrêt B nommé « l'arrêt n° 14, étendu au départ de la lecture de fin » ; le lot 10 a lit l'empreinte au manifeste (additif § 1 ; D3). |
| C11 | autrement | Lien avec la liste de la course écrit (en-tête de la liste) ; question à la mère et sa conséquence écrites (liste § 5 ; valeur 12 ; D4 ; PD7). **Motif tenu** : la liste de la course est bornée par GO-2026-11-20-57, qui nomme quatre entrées, et par GO-2026-11-20-65, qui ajoute « en cinquième nom » (`go.md`, l. 588 et 596). Y ajouter des entrées demanderait le mot de Lazar, comme pour la cinquième. GO-2026-11-21-41 (l. 640) demande les deux lecteurs « inscrits à la liste nominative » : ils y sont déjà. PD4 est ouvert. |
| C12 | telle quelle | `go.md` cité avec son commit `fed5dc2f`, empreinte non vérifiable par moi (voir la table des pièces) ; GO-2026-11-21-20 et -22 cités, relus (l. 619 et 621) ; relais d'origine dit par la mère (réserve 2 ; valeur 11 ; liste § 1). |
| C13 | telle quelle | Arrêt A : comparaison des deux heures, titre posé par le programme, épreuve dans les deux sens ; réserve 7 ; F7. |
| fuite, pas principal | telle quelle | Les sept points du § 4 ne disent ni que la liste porte des contrôles, ni leur nombre, ni leur issue, et ne renvoient à rien. Construction et issues sortent vers l'annexe. **Fermé pour le mandat ; ouvert par les pièces de la chaîne** (point 1). |
| fuite, pas second | telle quelle | Le programme de fin est inscrit (liste § 1, ligne 5). Il écrit sa ligne au journal avant d'ouvrir. Le journal de la garde est en quarantaine et n'est lu que par Lazar (additif § 5). |

Remarques portées, aussi vérifiées : « constat » au lieu d'« épreuve » (§ 1, F7) ; canal 9 (liste § 5, D4) ; canal 10 (arrêt F) ; canal 11 (valeur 10, PD9).

## Les onze points délicats

| point | ouvert dans le texte ? |
|---|---|
| PD1 tirage | oui : l'additif prend l'option sans écart, le dit (§ 4, « Hors du mandat » ; § 10, valeur 2 ; réserve 8) |
| PD2 garde avant le mot | oui : option (a), dite (§ 5, ligne de GO) |
| PD3 « recette » | oui : la lettre, dite, avec le signalement en plus (§ 4) |
| PD4 liste propre | oui : « point délicat porté à la mère, non tranché ici » (liste, en-tête) |
| PD5 composition et arrêts | oui : numéros des arrêts A, D et E laissés à la mère (valeur 1) |
| PD6 reste de Minuit | oui : arrêt C ; devis § 3, « aucune marge n'est promise » |
| PD7 la mère a-t-elle lu | oui : liste § 5 ; valeur 12 |
| PD8 lieu de l'annexe | oui : valeur 6, mais trop étroit (point 1) |
| PD9 octets de l'identifiant | oui : valeur 10, avec sa contrainte |
| PD10 GO-2026-11-21-47 | **non dans l'additif** : la règle est dite gelée au § 5 ; le point ne vit qu'en trouvaille de côté et au rapport (point 2) |
| PD11 extension de l'arrêt n° 12 | oui : option (a), dite (arrêt C) |

Aucun n'est tranché en silence au sens strict : PD10 est écrit au rapport. Mais le texte qui sera scellé ne le laisse pas ouvert.

## Relevé de méthode

**Chaîne de raisonnement.**

1. Les pièces lues ont les empreintes de la table du concepteur et des citations de l'additif (table ci-dessus, `sha256sum`).
2. Le calcul se rejoue à l'octet : deux `cmp` muets, dont un contre `941c18a3…`. L'objet faux rend le code 1, et aucun fichier n'est écrit (rejeu ci-dessus).
3. Chaque correction est au lieu que la table nomme, lu dans la v2 et dans le différentiel de l'additif (`977facb7…`, lu en entier).
4. C1 : GO-2026-11-21-28 et -30 diminuent la part de Minuit (`go.md` à `d481b9a3`, `cec2e676…`, l. 627 et 629). Donc la marge de 24,90 USD n'est plus à promettre, et le motif tient.
5. C4 : la V9 dit « « recette », au coffre » (`864f39a7…`, l. 328, relue). Donc garder la lettre n'est pas un écart, et le motif tient.
6. C11 : GO-2026-11-20-57 et -65 bornent la liste de la course (l. 588 et 596). Donc y ajouter des entrées demande le mot de Lazar, et le motif tient.
7. Le mandat des lecteurs (additif v2, § 4, sept points) ne nomme aucun objet de contrôle. Une recherche de « étrang|redite|hors du domaine|famille connue|deux témoins » sur les pièces v2 au format `.md` ne trouve rien dans l'additif ni dans la liste.
8. La même recherche trouve « la ligne étrangère » et « la ligne « redite » » au rapport v2, l. 92. Les différentiels portent 30 occurrences de « témoin|étrang|redite », dont la table v1 complète dans celui de l'additif (l. 142 à 146). La relecture « fuite » recopie construction et issues (l. 11), et l'additif v2 la cite par son chemin (l. 4).
9. Des pas 7 et 8 : l'annexe est protégée par la règle de lieu (§ 6 ; valeur 6), pas ces pièces. Donc la fuite est fermée dans le mandat, mais pas dans la chaîne (point 1).
10. GO-2026-11-21-47 (l. 646) est une règle permanente. GO-2026-11-21-20 (l. 619) montre que le modèle qu'elle nomme a rendu une réponse. Le § 10 de l'additif ne porte pas le constat (relu). Donc PD10 n'est pas ouvert dans le texte (point 2).
11. **Supposé** : que les lecteurs puissent ouvrir le dossier où ces pièces sont ou seront versées. Aucune pièce lue ne fixe ce lieu, aucune ne l'exclut.

**Objets de contrôle.**

- *Le programme de calcul.*
  - Objet faux par construction : `entrees-objet-faux-regle-v2.json`, dont un attendu est faux. Attendu d'avance : code 1, aucune sortie. Rendu : code 1, aucun fichier.
  - Objet vrai par construction : les entrées v2. Attendu : code 0 et une sortie égale à `941c18a3…`. Rendu : code 0, `cmp` muet.
- *Ma recherche d'un oracle dans une pièce.*
  - Objet vrai : le différentiel de l'additif, qui porte la table v1 par construction. Attendu : au moins une occurrence. Rendu : 22.
  - Objet faux : l'additif v2, écrit pour ne nommer aucun objet. Attendu : zéro. Rendu : zéro.
  - La méthode voit les noms, non une fuite par le sens.

**Premier pas non justifié.** Le pas 11 : le lieu où la v1, les relectures, les différentiels et le rapport sont ou seront versés, et si les lecteurs l'ouvrent. Le justifierait un mot de la mère sur ce lieu, ou sur la branche déjà poussée. Le point 1 vaut dans les deux cas : sa partie (a) protège pour l'avenir, sa partie (c) répare le passé.

**Mode d'échec affecté.** Fuite de la vérité.
- **Tenu** pour le mandat des lecteurs (pas 7), pour le texte servi aux juges (inchangé, `bbb50f64…` d'après la table, non recalculé par moi) et pour le journal de la garde (pas second).
- **Cassé, de forme** pour la chaîne. Le chemin : l'additif v2, l. 4, mène à la relecture « fuite », l. 11 ; la v1, § 6, et le différentiel de l'additif, l. 142 à 146, sont dans le même dossier ; le rapport v2, l. 92, nomme les objets. Tous mènent aux objets de l'annexe, qui sont les mêmes que ceux de la v1.
- Canaux examinés : le mandat des lecteurs, la liste de lecture, la requête des juges, le journal de la garde, l'export (arrêt F), les identifiants (valeur 10), les pièces citées par l'additif.

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur, non agent de re-dérivation.

**Trouvaille de côté.**
- (1) Le programme ramène la borne à 0 quand le reste est négatif, ou quand le tarif de sortie est nul. La règle écrite au § 5 rendrait un nombre négatif, ou une division par zéro. L'issue est la même, sous le plancher, aucun appel ; mais le devis, § 2, écrit « 0 » à 20 et 100 sur la foi du programme. Une phrase du § 5 (« zéro si le reste est nul ou négatif ») mettrait le texte d'accord avec le code.
- (2) A1, CV3, le devis v11 et l'additif 1 au complément ne sont pas dans ma liste : les chiffres 156,56, 105,05 et 131,66 ne sont pas vérifiés par moi.
- Non poursuivi.

**Évaluateur et conseil.** Ma pièce est jugée par la mère, puis par Lazar. Mes rejeux sont refaisables depuis mon dossier (`jeu-1.json`, `jeu-2.json`, `v9.md`, `go.md`). Elle pourrait obtenir un bon jugement sans le mériter sur deux points :
- le point 1 dépend du lieu de versement, que je suppose ouvert aux lecteurs (pas 11) ;
- je n'ai pas vérifié l'empreinte `c454dea5…` à `fed5dc2f`.

Conseil à la mère : régler d'abord le point 1. Il touche ce que l'annexe éprouve.

— vérificateur neuf, modèle O
