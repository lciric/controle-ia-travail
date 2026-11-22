# Devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), pour les ranger et les faire entrer dans le programme — v4

- **Auteur** : le rédacteur, sous-agent lancé par la session `session_013QMaykLXtozHttcSQ4ke1s`, modèle **Claude Fable 5.2**
  (`claude-fable-5-2`), selon le mot de Lazar du 19 novembre (R-3735, « Qui conçoit »). Il n'a écrit ni les versions 1 à 3, ni leurs
  contre-lectures.
- **Origine, déclarée** : la v3 (`devis-reajustement-lentilles-b-beta-v3.md`, `815acc33…`), rédigée par la session des lentilles sur
  Claude Opus 5.5, prise comme matière première ; elle reste archivée sans modification, comme la v1 (`1bf439ac…`), la v2 (`49dcbc93…`)
  et l'erratum (`erratum-devis-reajustement-v2-v1.md`, `c7915a23…`, retiré du circuit : pas d'erratum sur une pièce de classe A,
  décision de la mère). Lues aussi : la contre-lecture de la v1 (`e58dc66c…`, lecteur neuf sur Fable 5.2 : non employable, une
  bloquante, six majeures, onze mineures) et la vérification de la différence entre la v1 et la v2 (`3cc64c86…`, même lecteur :
  employable sous deux réserves majeures, N-1 et N-2, et sept mineures) ; la vérification du critère v2 (`8a6045bb…`, correction D7).
- Heure (`date -u`) à l'écriture : 2026-11-19T10:49:17Z ; l'heure du scellement est celle du fichier compagnon. Pièce de **classe A**.
- Demande d'origine : mots de Lazar du 19 novembre (« je vais faire entrer maintenant ces lentilles dans le programme », « a, prépare
  le devis du réajustement ») ; décision posée `decision-entree-lentilles-programme-v1.md` (`6aaf54e7…`) ; accord GO-2026-11-19-33
  (pièce 3 du billet ; paramètres du devis non tranchés, aucune ligne de calcul avant une confirmation de Lazar).
- Statut : **devis, aucune dépense engagée**. Rien ne part sans ligne de GO de calcul neuve (nœud de Lazar), sans les préalables du
  § 5, et sans la contre-lecture de cette v4 par un lecteur neuf d'un autre modèle (R2, R-3735).

## 0. Différences avec la v3, chacune avec sa raison
**Aucun chiffre de durée, de prix ni de plafond n'est changé** : l'arithmétique du § 3 a été recalculée ligne à ligne par la
vérification `3cc64c86…` (« juste partout ») et la v3 n'y a pas touché. Un ordre de grandeur est ajouté (n° 7), une confiance est changée
(n° 8) ; un renvoi de lignes est corrigé (n° 5).
| n° | différence | raison |
|---|---|---|
| 1 | Le § 4 renvoie au **critère d'identité v4** (`critere-identite-reajustement-lentilles-v4.md`) et en résume les règles, dont la règle neuve : **au palier 2, en variante A, la lentille n'entre dans aucune lecture sans nœud de Lazar**. | Le critère v4 remplace la v3 ; sa règle neuve pèse sur le choix de la variante, Lazar doit la lire avant d'accorder la dépense. |
| 2 | § 1 : « une reprise est notée et fait tomber au palier 2 » → « une reprise est notée ; si l'empreinte est égale, le palier 1 est prononcé, avec audit ». | La v3 contredisait le critère (contre-lecture du critère v1, mineure 2 : refuser le palier 1 à des octets égaux ferait écrire une mention fausse). |
| 3 | « § 4, palier 3 » → « statut de la seconde mesure » (§ 2, § 4, § 5, § 7). | Le critère n'a plus de palier 3 ; le mot désignait autre chose que les mentions du critère. |
| 4 | § 2 : « deux verdicts du 18 tiennent à une marge… » → « une condition décisive et une mesure rapportée ». | Mineure 4 de la vérification `3cc64c86…`, non reprise par la v3 : la comparaison des deux codes est « rapportée, non décisive » dans le verdict. |
| 5 | § 1 : les deux essais de `torch.save` cités avec chemin et empreinte ; « sur processeur » ; aucun des cinq correctifs ne touche à l'écriture du fichier. | Mineure 1 de la même vérification (R6) ; les essais ont été versés depuis, la v3 ne les citait pas. |
| 6 | § 1 : paragraphe « Ce qu'on peut attendre » : aucune pièce ne permet de prévoir le palier. | Lazar décide d'une dépense dont l'issue utile dépend du palier ; le dire avant, pas après. |
| 7 | § 7, décision 1 : ordre de grandeur d'une course de mesure à part, si la variante A tombe au palier 2 (≈ 2,8 h, ≈ 6,6 USD, tiré des blocs du § 3 ; pas un devis). | Sans lui, l'écart de ≈ 3,1 USD entre A et B se lit comme un pur surcoût ; il est aussi une assurance. |
| 8 | § 7, décision 1 : confiance de la recommandation de B portée de 0,6 à **0,7**. | Avec la règle n° 1, la variante A au palier 2 range une lentille que rien ne peut lire ; aucune pièce n'exclut le palier 2. |
| 9 | § 5, point 5 : le lanceur neuf verse en plus (g) le modèle de carte, le pilote et les versions de la machine, (h) les pièces que le critère exige, dans les deux variantes, (i) le commentaire « jamais lue pour un seuil » corrigé. | (g) : non consignés le 18 (réserve 2 du lecteur du verdict), l'audit du critère en a besoin ; (h) : sans ces pièces la mention est « non comparable » ; (i) : mineure 5 de la contre-lecture du critère v1, renvoyée au lanceur neuf sans y avoir été inscrite. |
| 10 | § 5, points 3, 4, 7 et 8 : empreinte rendue par la plateforme (recalculée ou seulement déclarée ?) ; clé à droits restreints à vérifier avant le GO ; recharge automatique citée (R-150) et « a tenu le 18 » seulement. | Mineures 5, 6 et 7 de la vérification `3cc64c86…`, non reprises par la v3. |
| 11 | § 5, point 6 : préalable neuf — décider si les contrôles hors programme du critère v4 s'appliquent à la main ou entrent dans une version neuve du programme de comparaison. | Défauts du programme montrés par les sondes du rédacteur (critère v4, § 7). |
| 12 | En-tête : auteur, modèle, heure relevée ; modèles des lecteurs dits. | R-3735 ; mineures 2 et 3 de la vérification `3cc64c86…`. |
| 13 | § 10 : traitement des réserves et mineures de la vérification `3cc64c86…` et de la correction D7, en tableau. | La v3 ne le donnait pas ; R2 demande que chaque remarque ait sa réponse. |

## 1. Pourquoi
Les deux lentilles ajustées par la tranche close (course `20261118-164930-neuron-lens-b-beta`, verdict « partiel » accepté,
`lecture-b-beta/accord-lazar-verdict-b-beta-v1.md`, `8469add5…`) **n'existent plus** : la décision de lancement (GO-2026-11-18-02, lieu
L1) les laissait sur la machine louée, détruite le 2026-11-19 à 05:45:00Z. Il reste leurs empreintes et des empreintes numériques de
leur contenu, versées (`inventaire-sorties-courses-lentilles-v1.md`, `9f95da40…`) :

| pièce (dans `diag/20261118-164930-neuron-lens-b-beta/`) | ce qu'elle porte pour comparer |
|---|---|
| `b-beta-ajustement-R.json` (`129c43b0…`) | fichier d'ajustement de R `r-llama-3.1-8b-instruct-L32-dclm-T128.pt` : empreinte `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`, 8 455 720 309 octets ; différences entre moitiés non arrondies par couche et cible (`diffs_float64`), `n_docs`, longueurs ; `rows_sha256` `a6afd972…` |
| `b-beta-ajustement-S.json` (`2dce646e…`) | fichier d'ajustement de S : `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`, 8 589 938 049 octets ; mêmes champs |
| `b-beta-export.json` (`17304c93…`) | **trois exports de R** (entier, moitié paire, moitié impaire) : une empreinte par fichier exporté (noms portant un identifiant de génération propre à chaque export) ; deux empreintes par couche des matrices des moitiés (`matrices_moities`, 31 couches) ; pour la lentille entière, deux séries d'écart à la lentille publique et à l'identité (28 couches) ; aucune taille |
| code de course | dépôt réduit, commit `5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` ; code voisin au commit `849bfe16…` |

**Ce qui est établi sur les octets** (lu sans dépense) :
- Le fichier d'ajustement ne contient que `meta` (lentille, modèle, couches, corpus, règles, `rows_sha256`, nombre de documents,
  longueur, `dim_batch`, cibles, part, type numérique : aucune heure, aucun chemin, aucun nom de machine), `state` (sommes et nombre de
  documents) et `next_doc` (code voisin `scripts/02_fit.py`, l. 140-148 et 161-166, au commit `849bfe16`).
- `torch.save` du même dictionnaire, au même nom de fichier, écrit les mêmes octets, et le nom du fichier entre dans les octets, le
  dossier non : essais sur processeur, torch 2.14.1 (`essai_torch_save_octets_v1.py`, `4fdec19d…`, sortie `3a18c2c2…` ;
  `essai_torch_save_nom_v1.py`, `1893d03e…`, sortie `3a2dbb16…`). Aucun des cinq correctifs du code voisin cités au manifeste ne
  contient d'appel d'écriture (`save(`), et aucun ne modifie `scripts/02_fit.py` : relevé du rédacteur par recherche dans leurs textes.
- **Non établi** : que la carte rende les mêmes sommes en virgule flottante d'une machine à l'autre (ordre des réductions ; modèle en
  demi-précision `bfloat16`, produits en TF32, sommes en simple précision), ni qu'une reprise sur sauvegarde ne change rien. Aucune
  reprise n'est prévue ; **une reprise est notée ; si l'empreinte est égale, le palier 1 est prononcé quand même, avec audit**
  (critère v4, § 4).
- L'identifiant de génération des fichiers exportés ne vient pas du code voisin (aucune occurrence) mais de la bibliothèque des
  lentilles qu'il appelle : tenu pour différent à chaque export ; les exports se comparent **par couche et par contenu**, jamais par nom.

**Ce qu'on peut attendre.** Aucune pièce ne mesure l'écart d'un réajustement : on ne sait pas d'avance quel palier sortira. Le palier 1
demande que dix heures de sommes en simple précision sur une autre carte retombent sur les mêmes octets : possible sur le même modèle
de carte avec les mêmes versions, non garanti (le pilote de la machine du 18 n'est pas consigné, on ne peut pas l'exiger). Le devis ne
compte donc pas sur le palier 1 ; la décision 1 se lit dans les deux cas.

## 2. Deux variantes
**Variante A — ajustement seul, puis rangement.** Montage ; ajustement de R ; export ; copie de R ; ajustement de S ; copie de S ;
comparaison selon le critère d'identité v4 ; destruction. Aucune mesure refaite. **Au palier 2, la lentille rangée par la variante A
n'a aucune mesure propre** (hors la différence entre moitiés que l'ajustement produit lui-même et, pour R, deux séries d'écart) : le
verdict du 18 ne se transporte pas, et elle n'entre dans aucune lecture sans nœud de Lazar (critère v4, § 5).

**Variante B — la course rejouée, plus le rangement.** La commande de la tranche (v8) rejouée entière, avec les changements du § 5,
point 5, et les copies ; les sept mesures de la tranche sont refaites sur une autre machine. **Ce qu'elle ajoute à A** : non pas
l'identité des lentilles (les paliers 1 et 2 sont communs ; **seul le palier 1 établit l'identité**), mais des mesures :
- au palier 1, une **seconde mesure de la même lentille** sur un autre exemplaire du même modèle de carte (même code, même corpus,
  mêmes graines : seule la machine change) ; utile parce qu'**une condition décisive** du 18 tient à une marge de l'ordre de l'effet
  du matériel (lecture contre pilotage : 55 pôles sur 64 à la couche 8 pour 58 exigés, marge −0,0406) et qu'**une mesure rapportée,
  non décisive**, est à une couche de son repère (comparaison des deux codes : 20 couches sur 28 pour 21) ;
  `lecture-b-beta/verdict-b-beta-v1.md`, `3a9b947e…`, tableau du verdict et réserve 2 du lecteur ;
- au palier 2, **les seules mesures de la lentille rangée** : **au palier 2, seule la variante B donne à la lentille rangée des
  mesures propres.**
Son statut est fixé par le § 4 (« statut de la seconde mesure ») et exige un texte scellé avant la création (§ 5, point 7).

## 3. Durées et coût (chiffres de la v3, inchangés)
Durées **mesurées** sur H100 SXM le 18-19 novembre (pièces ci-dessus et `controles-b-beta-v1.log`) : montage jusqu'au début de
l'ajustement de R 1 h 14 (16:48:55 → 18:03:15 ; dont installation ≈ 59 min pour une borne de 3 600 s : le lanceur neuf la porte à
7 200 s, § 5) ; ajustement de R 18 414 s ; export 78 s ; ajustement de S 18 065 s ; suite de la course 1 h 19 (04:12:35 → 05:31:55) ;
fin de course jusqu'à la destruction 0,2 h (12,72 h de course, 12,93 h de location). Volume à copier : ≈ 17 Go de fichiers
d'ajustement et ≈ 13 Gio d'exports (commande v8, l. 288, estimé), soit **≈ 31 Go** ; à 200 Mbit/s (débit montant exigé) ≈ 0,35 h ;
le débit en écriture de la plateforme de modèles n'est pas mesuré (pire cas pris à 100 Mbit/s).

| bloc | attendu | pire cas | source du pire cas |
|---|---|---|---|
| montage | 1,25 h | 2,5 h | deux fois le mesuré (borne d'installation relevée à 7 200 s) |
| ajustements R et S, export | 10,16 h | 13,1 h | pire cas du devis v12 (6,56 h par lentille) |
| suite de la course (variante B) | 1,3 h | 2,6 h | deux fois le mesuré |
| copies (≈ 31 Go) | 0,35 h | 0,69 h | 100 Mbit/s |
| vérification à l'arrivée, préavis, destruction | 0,25 h | 0,25 h | mesuré 0,2 h le 19, plus la relecture au lieu |
| **variante A** | **12,0 h** | **16,5 h** | |
| **variante B** | **13,3 h** | **19,1 h** | |

**Prix** : relevé `releve-prix-vast-h100-20261119T080302Z-v1.tsv` (`90395583…`, 08:03:02 UTC) : une seule offre vérifiée sous
4 USD/h au filtre complet, Japon, offre 59816165, **2,3713 USD/h avec 200 Go**, trafic sortant et entrant **0**, débit montant
1 744 Mbit/s, fiabilité 0,9917 ; la suivante à 4,0990 (États-Unis). Le relevé est refait dans l'heure qui précède la création, avec
les colonnes des deux options ci-dessous (ses colonnes actuelles sont celles de la v8).

**Trafic** : réservé à **2,3 USD** de frais fixes (≈ 25 Go entrants et ≈ 31 Go sortants à 0,04 USD/Go, plafond de trafic du filtre) ;
nul à l'offre du relevé.

| | attendu à 2,37 | pire cas à 2,37 | pire cas au prix exigé de 2,62 | avec frais fixes |
|---|---|---|---|---|
| variante A | ≈ 28,5 USD | ≈ 39,2 USD | ≈ 43,3 USD | ≈ 45,6 USD |
| variante B | ≈ 31,6 USD | ≈ 45,4 USD | ≈ 50,1 USD | ≈ 52,4 USD |

**Plafonds proposés** (formules de la v8 : compte rendu 60 %, arrêt dur 90 %, minuterie = (arrêt dur − frais fixes) / prix lu ; la
garde compte au plus grand du prix déclaré, 2,62, et du prix lu ; marge d'au moins 5 % entre le pire cas avec frais et l'arrêt dur) :
- **variante A : plafond 54 USD** ; arrêt dur 48,6 ; minuterie (48,6 − 2,3) / 2,62 = **17,7 h** pour un pire cas de 16,5 h ; prix
  minimal de la règle du refus (48,6 − 2,3) / 36 = 1,29 USD/h ; compte rendu 32,4 USD, atteint vers 11,5 h, **donc en course
  normale** (avant les 12,0 h attendues) : il est attendu et ne signale rien à lui seul ;
- **variante B : plafond 62 USD** ; arrêt dur 55,8 ; minuterie (55,8 − 2,3) / 2,62 = **20,4 h** pour un pire cas de 19,1 h ; prix
  minimal 1,49 USD/h ; compte rendu 37,2 USD vers 13,3 h, **attendu en course normale**.
La garde arrête à ces durées quel que soit le prix lu ; la minuterie, plus longue au prix lu (19,5 h et 22,6 h à 2,37), est le filet.

**Risques** : le mesuré de l'ajustement (5,12 h) vaut 78 % du pire cas par lentille et a dépassé le haut de l'attendu du devis v12 ;
une machine plus lente arrête la course au banc du montage (seuil de 23,6 s par document) : perte faible, aucune reprise sans devis
neuf. **Perte de la machine** : arrêt, aucune reprise sans devis neuf ; avec les copies faites au fil de l'eau (§ 5, point 3), une
perte après la copie de R ne coûte que S. **Aucune relance pour obtenir un autre palier** sans devis neuf et mot de Lazar (critère
v4, § 6).

## 4. Critère d'identité, et statut de la seconde mesure
**Le critère d'identité v4 (`critere-identite-reajustement-lentilles-v4.md`) fait foi et prime sur toute phrase de ce devis** ; il
est scellé avant toute création. En bref, lentille par lentille :
- **palier 1** — octets du fichier d'ajustement identiques à ceux du 18 : **seul ce palier établit l'identité** ; les mesures et le
  verdict du 18 décrivent la lentille rangée ;
- **palier 2** — « différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables » : l'identité
  n'est pas établie, le verdict du 18 ne se transporte pas ; en variante B, la lentille n'est lue qu'après la lecture de la seconde
  course par un lecteur neuf ; **en variante A, aucune lecture sans nœud de Lazar** ;
- **« différente », « non comparable », mention suspendue** : rangée, marquée, aucune lecture sans nœud de Lazar ;
- la comparaison est faite par la mère ou un agent neuf, sur les pièces poussées par la machine, avant toute lecture d'une mesure de
  la nouvelle course ; la mention s'écrit sur le fichier rangé, une fois son empreinte relue au lieu de rangement.
**Statut de la seconde mesure (variante B)**, inchangé depuis la v2 : le verdict scellé et accepté du 18 reste celui de la tranche ;
la seconde course est lue par un lecteur neuf sur un plan scellé et rapportée à côté, sans critère de concordance fixé après coup ;
tout désaccord est un nœud de Lazar. Au palier 2, cette seconde course est la seule mesure de la lentille rangée : son texte de statut
le dit.

## 5. Préalables, tous sans dépense (rien ne part sans eux)
1. **Ligne de GO de calcul neuve** (type « calcul »), nommée par la mère sur le mot de Lazar : variante, prix exigé, plafond, échéance.
2. **Nœud de l'entrée des lentilles dans le programme** inscrit par la mère (pièces : `decision-entree-lentilles-programme-v1.md`).
3. **Lieu de rangement** choisi par Lazar (§ 6) et prêt. Avec L2 : copie de R dès son export, de S dès la fin de son ajustement (la
   clé est de toute façon sur la machine : copier au fil de l'eau ne l'expose pas plus longtemps et borne la perte) ; empreintes
   calculées sur la machine avant envoi. **Fin de course en quatre temps** (réserve N-2) : (1) copie ; (2) **première relecture** des
   empreintes au lieu de rangement par la session, clé de la machine encore valide (une copie fausse peut encore être refaite),
   révision du dépôt notée ; (3) **destruction de la machine par son identifiant, sans attendre Lazar** ; (4) révocation de la clé par
   Lazar quand il peut, puis **seconde relecture** de la même révision avec la clé gardée de la session (lecture seule). Relecture par
   les empreintes que la plateforme rend pour ses gros fichiers, sans retéléchargement, **seulement s'il est établi (point 9) que la
   plateforme les recalcule ou les vérifie à la réception** ; si elle ne fait que recopier ce que la machine déclare, la session
   télécharge au moins une fois (≈ 31 Go : disque, durée et trafic de la session à dire avant).
4. **Clé** : la clé actuelle reste gardée (mot de Lazar) et **n'est pas passée** à la machine ; une **clé neuve à droits restreints**
   (lecture du modèle à accès contrôlé ; écriture sur le seul dépôt de rangement) est créée par Lazar, passée à la création, révoquée
   par Lazar après la copie. **À vérifier avant le GO** : que la plateforme permet bien une clé unique bornée ainsi ; sinon la
   décision 3 est à reposer. Risque déclaré : exposée dès la création, elle permet d'écraser le dépôt ; parade : chaque copie vérifiée
   par empreinte à l'arrivée, révision du dépôt notée à chaque copie.
5. **Code et commande** (à écrire, essayer sur cas sain et artefact, contre-lire) : lanceur et amorce neufs (v4) = v3 avec (a) le GO
   attendu nouveau, (b) la branche de résultats `calcul/neuron-lens-reajustement-v1`, (c) **la clé gardée sur la machine toute la
   course** au lieu d'être retirée après le téléchargement (changement des gardes de secrets : le balayage des secrets avant chaque
   poussée, toutes les dix minutes, est refait et ses 14 formes rejouées à blanc avec cette clé présente), (d) les deux étapes de
   copie avec vérification, sans dupliquer les fichiers sur le disque, (e) la borne d'installation portée à 7 200 s, (f) pour la
   variante A, arrêt après la copie de S, (g) **une pièce de résultat qui consigne le modèle de carte, la version du pilote et les
   versions de la machine** (non consignés le 18), (h) **dans les deux variantes, les pièces que le critère exige**, poussées sur la
   branche de résultats : pour R et pour S le résultat d'ajustement avec les mêmes champs qu'au 18 (empreinte et taille du fichier,
   nom du fichier inchangé, `diffs`, `diffs_float64` calculée par la fonction `_split_half_64` au texte inchangé, `meta`, `n_docs`,
   `next_doc`, `finies`, heure de début), le manifeste, pour R le résultat d'export (matrices des moitiés, deux séries), et au journal
   l'indication de toute reprise, (i) le commentaire du lanceur « jamais lue pour un seuil » corrigé, sans toucher au texte de la
   fonction ; commande v9 ; essai à blanc refait.
6. **Programme de comparaison** : décider, avant la création, si les sept contrôles hors programme du critère v4 (§ 7, H1 à H7)
   s'appliquent à la main, ou si la session des lentilles les porte dans une version neuve du programme (nom neuf, un essai par
   sonde, contre-lecture ; le critère prend alors une version neuve, courte). Recommandation du rédacteur : la version neuve, si elle
   ne retarde pas la création de plus d'une demi-journée.
7. **Textes scellés et contre-lus** : le critère d'identité v4 ; pour la variante B, le **statut de la seconde mesure** (§ 4) et le
   plan de sa lecture par un lecteur neuf.
8. **Crédit du loueur** : **9,05 USD** au relevé de la session (`releve-credit-20261119T081130Z-v1.txt`, `2545c241…`, 08:11:29 UTC,
   crédit seul) ; à relire avant la création. La recharge automatique (5 USD dès que le crédit passe sous 5 USD, réglage lu sur le
   compte : `registres/decisions.md`, R-150) est celle sur laquelle Lazar a levé la condition de crédit de la v8 (R-3319) ; le journal
   la montre tenir le 18. **Proposition, un seul montant** : recharger **au moins le plafond retenu** (54 ou 62 USD) avant la création,
   en plus des autres lignes ouvertes ce jour-là sur le même compte (à chiffrer par la mère le jour du GO), et garder la garde de la
   v8 (crédit < 1 USD → arrêt). Budget journalier de 100 euros (mot de Lazar relayé par la mère, devis v12, § 2, point 8) : la dépense
   attendue (≈ 29 à 32 USD) y tient seule ; avec les autres courses du jour, à vérifier par la mère.
9. **Plateforme de modèles** : coût et quota du stockage privé, débit en écriture, licence du modèle pour des poids dérivés rangés en
   privé, **et nature de l'empreinte qu'elle rend pour un gros fichier (recalculée à la réception, ou déclarée par l'envoyeur)**,
   relevés avant le GO.
10. **Leçon du 19 novembre** : un redémarrage du conteneur de la session tue la minuterie et la garde ; la veille les réarme sur
    l'échéance absolue. La machine n'attend plus Lazar (point 3) ; si la session est absente à la fin, la garde (plafond) et la
    minuterie restent le filet, et la mère détruit par identifiant.

## 6. Lieu de rangement (choix de Lazar)
≈ 31 Go (fichiers d'ajustement ≈ 17 Go, exports ≈ 13 Gio) ; au-delà de la limite de l'hébergeur de code (100 Mo par fichier).
- **L2 — dépôt privé de modèles chez la plateforme de modèles** (Hugging Face), créé par Lazar sous son compte ; copie par la machine,
  relecture par la session (§ 5, point 3). Coût et quota : à relever (§ 5, point 9).
- **L3 — une machine de Lazar** : la machine louée pousse vers elle (un accès de sa machine sur la machine louée). « Lazar tire depuis
  la machine louée » supposerait un accès entrant, alors que la commande est sans ssh : écarté sauf changement de commande.
Dans les deux cas, le verdict d'identité de chaque lentille est écrit dans un fichier compagnon au lieu de rangement (critère v4, § 5).

## 7. Décisions demandées à Lazar (par la mère)
**Décision 1 — variante.** Enjeu :
« ranger des lentilles ; on ne saura si ce sont celles qui ont été jugées qu'au palier 1 » ; en option, remesurer.
Conséquence pour le choix :
« au palier 2, la lentille rangée par la variante A n'a aucune mesure propre ; seule la variante B lui en donne ».
Le critère v4 en tire la règle : au palier 2, la lentille de la variante A n'entre dans aucune lecture
sans un nœud de Lazar ; pour la lire il faudrait alors la mesurer par une course à part (ordre de grandeur, tiré des blocs du § 3 et
non d'un devis : montage 1,25 h, suite de la course 1,3 h, fin 0,25 h, soit ≈ 2,8 h et ≈ 6,6 USD à 2,37 USD/h, hors retour des
≈ 31 Go vers la machine et hors préparation). On ne sait pas d'avance quel palier sortira (§ 1).
Options :
- **A** — ≈ 28,5 USD attendus, plafond 54. Identité établie au seul palier 1 ; au palier 2, ni identité, ni mesure propre, ni
  lecture. Avantage : le moins cher, moins de textes à sceller avant la création. Inconvénient : au palier 2, on range des poids
  inutilisables en l'état.
- **B** — ≈ 31,6 USD attendus, plafond 62. Mêmes paliers ; au palier 1, une seconde mesure de la même lentille sur une autre machine
  (la condition décisive à marge mince du 18 y est rejouée) ; au palier 2, les seules mesures de la lentille rangée ; lue par un
  lecteur neuf, sans effet sur le verdict accepté du 18. Inconvénient : ≈ 3,1 USD et ≈ 1,3 h de plus ; deux textes de plus à sceller
  avant la création (statut de la seconde mesure, plan de lecture).
**Recommandation : B, confiance 0,7.** Pour ≈ 3,1 USD de plus, B rend la dépense utile quel que soit le palier ; A ne vaut que si le
palier 1 sort, ce que rien ne garantit, ou si l'on ne veut que des poids rangés. Défaut sous 48 heures : rien ne part.

**Décision 2 — prix exigé et plafond.** Recommandation : prix exigé 2,62 USD/h ; plafond 62 USD (B) ou 54 (A). Défaut : rien ne part.

**Décision 3 — lieu de rangement et clé.** Recommandation : L2 sous le compte de Lazar ; clé neuve à droits restreints, révoquée après
la copie ; la clé gardée reste hors de la machine. Confiance 0,6 (L3 évite toute clé d'écriture sur la machine mais demande un accès
de la machine de Lazar ; et la clé restreinte reste à vérifier, § 5, point 4). Défaut : rien ne part.

**Décision 4 — statut de la seconde mesure** (variante B) : le verdict du 18 reste ; la seconde course est rapportée à côté ; tout
désaccord est un nœud de Lazar (§ 4). Recommandation : accepter cette règle. Défaut : rien ne part en variante B.

**Décision 5 — recharge** d'au moins le plafond retenu avant la création (crédit 9,05 USD à 08:11Z).

## 8. Ce que ce devis ne fait pas
Il ne décide pas de l'usage des lentilles dans le programme : chaque expérience qui s'en servira le dira dans son préenregistrement
(R1) ; toute modification d'un texte déjà scellé (par exemple la lecture des sondes apprises sur la tâche, qui ne lit aujourd'hui que
la lentille publique) passe par une version nouvelle, contre-lue, et un mot de Lazar. Il ne promet pas la pièce 3 du billet avant le
22 novembre : la note sur la place des lentilles (`place-lentilles-billet-v1.md`, `a6e91e25…`) la tient pour improbable à cette date.

## 9. Traitement de la contre-lecture de la v1 (`e58dc66c…`), gardé de la v2
| remarque | traitement |
|---|---|
| B-1 plafonds sous le pire cas | acceptée : frais fixes 2,3 USD ; copie de ≈ 31 Go au pire 0,69 h ; fin 0,25 h ; plafonds 54 et 62, marge ≥ 5 % (§ 3) |
| M-1 comparaison possible en variante A | acceptée : paliers 1 et 2 communs aux deux variantes ; l'argument de B redit (§ 2, § 7) |
| M-2 seuil de 0,03 | acceptée : retiré ; la comparaison des mesures de la seconde course est rapportée sans critère (§ 4) ; la tolérance du palier 2 est celle du critère v4 |
| M-3 seconde mesure sans statut | acceptée : statut de la seconde mesure, préalable 7, décision 4 ; « indépendante » retiré ; marges avec chemin et empreinte (§ 2) |
| M-4 clé d'écriture | acceptée : changement du lanceur dit (§ 5, point 5 c) ; copies au fil de l'eau ; relecture après révocation ; L3 « tirer » écarté (§ 6) |
| M-5 égalité d'octets | acceptée : contenu du fichier lu dans le code voisin, essais de `torch.save` versés, identifiant de génération, trois exports (§ 1) |
| M-6 crédit | acceptée : relevé de la session versé ; un seul montant ; recharge automatique et garde dites (§ 5, point 8) |
| m-1 à m-5, m-7 à m-11 | acceptées (prix minimal, compte rendu et arrêt réel dits au § 3 ; marge de l'ajustement en risque ; borne d'installation à 7 200 s ; plateforme et licence au point 9 ; fin de 0,25 h ; fin 05:31:55Z ; session absente au point 10 ; chaque lentille jugée seule) |
| m-6 disque | acceptée en partie : 200 Go gardés ; la copie lit les fichiers sans les dupliquer (§ 5, point 5 d) |

## 10. Traitement de la vérification de la différence entre la v1 et la v2 (`3cc64c86…`) et de la correction D7 (`8a6045bb…`)
| remarque | traitement |
|---|---|
| N-1 tolérance de 10⁻⁶ inapplicable, « identité par les paliers 1 et 2 » | levée par le critère (v4) : tolérance de 10⁻³ déclarée conventionnelle, mention sans « équivalente », seul le palier 1 établit l'identité ; dit à Lazar dans la décision 1 |
| N-2 fin de course qui attend Lazar | levée : fin en quatre temps (§ 5, point 3) ; la machine est détruite sans attendre |
| mineure 1 essai de `torch.save` non versé | levée : deux essais versés et cités (§ 1) ; sur processeur ; aucun correctif ne touche à l'écriture |
| mineure 2 heure d'écriture | levée : relevée par `date -u` (en-tête) |
| mineure 3 « lecteur neuf d'un autre modèle » | levée : modèles de l'auteur de la v3, du rédacteur et des lecteurs dits (en-tête) |
| mineure 4 « deux verdicts » | levée : une condition décisive et une mesure rapportée (§ 2) |
| mineure 5 empreintes rendues par la plateforme | levée : préalables 3 et 9 |
| mineure 6 recharge automatique | levée : R-150 citée ; « tenir le 18 » seulement (§ 5, point 8) |
| mineure 7 clé à droits restreints | levée : à vérifier avant le GO (§ 5, point 4 ; décision 3) |
| D7, enjeu de la décision 1 | recopiée mot pour mot : « ranger des lentilles ; on ne saura si ce sont celles qui ont été jugées qu'au palier 1 » (§ 7) |
| D7, § 2 | gardée : « (les paliers 1 et 2 sont communs ; seul le palier 1 établit l'identité) » |
| D7, conséquence pour le choix de la variante | recopiée mot pour mot : « au palier 2, la lentille rangée par la variante A n'a aucune mesure propre ; seule la variante B lui en donne » (§ 7), et dite au § 2 |
