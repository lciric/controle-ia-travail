# Vérification de la différence entre la v1 et la v2 du devis du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct)

- Heure (`date -u`) : 2026-11-19T08:15:27Z.
- Vérificateur : le contre-lecteur de la v1 (sous-agent, modèle Fable 5.2, `claude-fable-5-2`) ; il n'a écrit ni la v1 ni la v2.
- Empreintes recalculées (`sha256sum`) :
  - devis v2 `devis-reajustement-lentilles-b-beta-v2.md` : `49dcbc9345ad9851bb07cfeadb626ccb7f6be132bd8943acae07f0247859875e` — égale à l'annoncée et au compagnon ;
  - relevé de crédit `releve-credit-20261119T081130Z-v1.txt` : `2545c24128eb29d8335dd8d36949ab6bf7c94ddf7b6a6298ff795c401ea89800` — égale au compagnon ; il porte « 2026-11-19T08:11:29Z credit 9.051… » ;
  - verdict de la tranche `lecture-b-beta/verdict-b-beta-v1.md` : `3a9b947e…` ; inventaire des sorties : `9f95da40…` ; décision posée : `6aaf54e7…` — conformes aux abrégés du devis ;
  - code voisin, copie en lecture : `git log -1` rend `849bfe1678e28becceb1e3864afe5fc8297d02e4`, origine `stdlogits/neuron-lens`.
- Lu en plus de la première contre-lecture : la v2 ; le relevé de crédit ; `scripts/02_fit.py` (l. 125-175) et la classe d'accumulation
  de `neuron_lens/transport.py` du code voisin ; les champs `diffs`, `diffs_float64`, `diffs_recopie`, `ecarts_sommes` des deux
  fichiers d'ajustement et `matrices_moities` de l'export ; les lignes 25 et 29 du verdict (les deux marges citées) ; trois lignes de
  notre lanceur (`b_beta_lancer_v3.py`, l. 492-499) pour savoir comment `diffs_float64` est calculé. Aucune machine, aucun modèle,
  aucune commande du loueur, aucun commit.

## Verdict : **employable**, sous deux réserves majeures

Les deux réserves ne touchent pas les chiffres du devis. Elles se lèvent dans deux pièces que le devis exige déjà avant tout
lancement (le critère d'identité scellé, la commande v9) et doivent être dites à Lazar avec les décisions. La bloquante de la v1
est levée ; les six majeures sont traitées, deux d'entre elles en laissant un défaut neuf (ci-dessous) ; les onze mineures sont
traitées, une seule imparfaitement.

## Arithmétique du § 3, recalculée : juste partout

| chiffre de la v2 | recalcul | état |
|---|---|---|
| copies ≈ 31 Go (17,05 Go + 13 Gio = 13,96 Go) ; 0,35 h à 200 Mbit/s ; 0,69 h à 100 | 31,0 Go ; 1 240 s = 0,344 h ; 0,689 h | juste |
| ajustements et export attendus 10,16 h | 5,115 + 5,018 + 0,022 = 10,155 | juste |
| variante A : 12,0 h ; 16,5 h | 12,01 ; 16,54 | juste |
| variante B : 13,3 h ; 19,1 h | 13,31 ; 19,14 | juste |
| frais fixes 2,3 USD | 56 Go × 0,04 = 2,24 | juste (arrondi vers le haut) |
| A : 28,5 ; 39,2 ; 43,3 ; 45,6 USD | 28,5 ; 39,2 ; 43,3 ; 45,6 | juste |
| B : 31,6 ; 45,4 ; 50,1 ; 52,4 USD | 31,6 ; 45,4 ; 50,1 ; 52,4 à 52,5 | juste |
| plafond 54 : arrêt dur 48,6 ; minuterie 17,7 h ; prix minimal 1,29 ; compte rendu 32,4 vers 11,5 h ; filet 19,5 h à 2,37 | 48,6 ; 17,67 ; 1,286 ; 32,4 et 11,49 ; 19,53 | juste |
| plafond 62 : arrêt dur 55,8 ; minuterie 20,4 h ; prix minimal 1,49 ; compte rendu 37,2 vers 13,3 h ; filet 22,6 h à 2,37 | 55,8 ; 20,42 ; 1,486 ; 37,2 et 13,32 ; 22,56 | juste |
| marge d'au moins 5 % entre pire cas avec frais et arrêt dur | 48,6 / 45,6 = 1,065 ; 55,8 / 52,45 = 1,064 | juste |
| crédit 9,05 USD à 08:11:29Z | porté par le relevé | juste |
| 55 pôles sur 64 pour 58 ; 20 couches sur 28 pour 21 | verdict, l. 25 et l. 29 | porté (voir mineure 3) |
| contenu du fichier d'ajustement : `meta`, `state`, `next_doc`, sans heure ni chemin | `02_fit.py`, l. 140-148 et 161-166 | porté (le devis écrit 140-147 ; le type numérique est à la l. 148) |
| identifiant de génération absent du code voisin | aucune occurrence de `gen-` ni d'identifiant tiré dans ses fichiers `.py` | porté |

## Traitement des remarques de la v1

| remarque | état |
|---|---|
| B-1 plafonds | **levée** : frais fixes, copie, fin de course et plafonds refaits ; marges vérifiées |
| M-1 comparaison possible en variante A | levée dans la forme (paliers communs, argument de la variante B redit honnêtement) ; le palier 2 a un défaut neuf : **N-1** |
| M-2 seuil de 0,03 | levée : seuil retiré, comparaison des mesures rapportée sans critère, forme de la garde (j) |
| M-3 seconde mesure | levée : palier 3, préalable 6, décision 4 ; « indépendante » retiré ; marges sourcées |
| M-4 clé d'écriture | levée pour le lanceur, les copies au fil de l'eau et le lieu L3 ; l'ordre de la fin laisse un défaut neuf : **N-2** |
| M-5 égalité d'octets | levée, sauf l'essai local non versé (mineure 1) |
| M-6 crédit | levée : relevé versé, un seul montant, garde gardée |
| mineures 1 à 8, 10, 11 | levées |
| mineure 9 (heure d'écriture) | non levée : voir mineure 2 |

## Remarques majeures neuves

**N-1 — La tolérance de 10⁻⁶ du palier 2 n'est pas applicable aux différences entre moitiés, et sa justification est fausse (l. 98-102).**
- Le devis la justifie par « l'écart attendu d'un ordre de sommation différent en double précision ». Or les sommes de l'ajustement
  ne sont pas en double précision : l'accumulateur du code voisin est créé par `torch.zeros` sans type (simple précision), sur la
  carte (`transport.py`, l. 55), et le modèle tourne en `bfloat16` (champ `meta.dtype` des deux pièces). Seul le calcul final de la
  norme est refait en double précision par notre lanceur.
- Les pièces elles-mêmes montrent l'ordre de grandeur : pour les **mêmes sommes**, les trois versions versées de la même grandeur
  (`diffs`, `diffs_float64`, `diffs_recopie`) s'écartent de ≈ 1,5 × 10⁻⁵ (R, première couche : 0,111388 ; 0,111373 ; 0,111374) et
  jusqu'à ≈ 6 × 10⁻⁵ (S : 0,085555 contre 0,085497). Changer seulement la précision du calcul final déplace donc la valeur de 15 à 60
  fois la tolérance. Un réajustement sur une autre machine (sommes en simple précision de 932 documents, modèle en `bfloat16`) a
  toutes les chances de la dépasser dès que les octets diffèrent.
- Conséquence : le palier 2 est vide. Hors égalité d'octets, la conclusion sera presque sûrement « lentille différente » et un nœud
  de Lazar. C'est le sens sévère, pas une lecture orientée ; mais la décision 1 annonce « identité par les paliers 1 et 2 » (l. 151),
  ce que le palier 2 ne peut pas donner. Notre lanceur dit d'ailleurs de `diffs_float64` : « pour mémoire, jamais lue pour un seuil ».
- Autre limite à écrire : les différences entre moitiés sont 63 ou 64 nombres par lentille ; leur accord est une condition
  nécessaire, pas une preuve que les matrices sont les mêmes (les matrices du 18 n'existent plus). Les empreintes par couche de
  `matrices_moities` ne sont qu'une autre forme de l'égalité d'octets.
**Correction** (dans le critère scellé, et une phrase dans le devis ou dans le message à Lazar) : dire la précision réelle ; fixer
la tolérance au-dessus du plancher que les pièces mesurent (l'écart entre `diffs` et `diffs_float64`), la déclarer conventionnelle,
de préférence relative à la valeur ; nommer la mention « différences entre moitiés concordantes à tant près, contenu non comparable
matrice par matrice » plutôt que « lentille équivalente » ; dire à Lazar que, si les octets diffèrent, l'identité ne sera pas
établie, seulement une concordance grossière — et, en variante B, la comparaison des mesures rapportée à côté.

**N-2 — La fin de course fait attendre la machine, facturée, un geste de Lazar ; et l'ordre proposé ôte tout recours (l. 114-118, 119-122, 138-140).**
Le § 5 place la relecture des empreintes « après la révocation de la clé de la machine », révocation qui est un acte de Lazar, et
le point 9 dit que « la machine attend facturée la relecture et la révocation ». Le § 3 ne compte que 0,25 h pour cette fin. Si
Lazar n'est pas là, la machine se facture jusqu'à l'arrêt dur (jusqu'à ≈ 20 USD de plus que l'attendu en variante B). Et si la
relecture après révocation échoue, la machine ne peut plus repousser (clé révoquée, commande sans ssh, clé donnée à la création
seulement) : l'attente n'achète rien.
**Correction** (commande v9, et une phrase au § 5) : ordre en quatre temps — (1) copie et empreintes calculées sur la machine ;
(2) première relecture par la session, révision du dépôt notée, clé encore valide, donc nouvelle copie possible en cas d'écart ;
(3) destruction de la machine par son identifiant, sans attendre Lazar ; (4) révocation par Lazar quand il peut, puis seconde
relecture de la même révision par la session, qui confirme que rien n'a changé entre-temps. La durée de fin de 0,25 h tient alors.

## Remarques mineures

1. **Essai local de `torch.save` non versé (l. 29-30).** Décrit, sans chemin ni empreinte (R6). Il ne suffit pas tel quel : verser le
   script et sa sortie, scellés. Portée limitée : s'il se trompait, on tomberait au palier 2, sens sévère. Dire aussi que l'essai
   est sur processeur, à la version 2.14.1 des exigences, et vérifier qu'aucun de nos correctifs du code voisin ne touche `save()`.
2. **Heure d'écriture (l. 3-4).** « Entre 08:12 et 08:30 UTC » alors que le fichier date de 08:12 et son compagnon de 08:13 UTC :
   une heure à venir, comme en v1. À relever par `date -u` au scellement.
3. **« Lecteur neuf d'un autre modèle » (l. 5-6).** La contre-lecture de la v1 dit son modèle (Fable 5.2) ; rien dans le devis ne
   dit celui de l'auteur. Affirmation non portée par une pièce : la retirer ou donner le modèle de l'auteur.
4. **« Deux verdicts » (l. 43-45).** La marge de la lecture contre pilotage est de −0,0406 (verdict, l. 25), un peu au-delà de
   l'effet du matériel de 0,03 ; la comparaison des deux codes est dite « rapportée, non décisive » par le verdict (l. 29). À écrire
   ainsi : une condition décisive et une mesure rapportée.
5. **Empreintes rendues par la plateforme (l. 116-118).** Établir, au préalable 8, si l'empreinte rendue est recalculée ou vérifiée
   par la plateforme à la réception, ou seulement déclarée par la machine qui envoie. Dans le second cas elle ne prouve pas
   l'arrivée intacte : télécharger alors au moins une fois (disque, durée et trafic de la session à dire).
6. **Recharge automatique « 5 USD sous 5 USD » (l. 131).** Portée par `registres/decisions.md` (R-150) : la citer. « A tenu le 18 et
   le 19 » : le journal ne le porte que pour le 18 (23:49Z).
7. **Clé à droits restreints (l. 119-122).** Vérifier avant le GO que la plateforme permet bien une clé unique bornée à la lecture
   du modèle à accès contrôlé et à l'écriture d'un seul dépôt ; sinon la décision 3 est à reposer.

## Niveau des décisions et honnêteté des recommandations
Les cinq décisions sont des nœuds de Lazar, avec « rien ne part » pour défaut : conforme. Le statut de la seconde mesure est bien
posé (le verdict du 18 reste, lecteur neuf dans tous les cas, tout désaccord est un nœud). La recommandation de la variante B, à
confiance 0,6, est maintenant fondée sur sa vraie raison et dit que la variante A suffit pour les seuls poids : honnête. Seule
phrase à corriger dans ce qui est soumis à Lazar : « identité par les paliers 1 et 2 » (N-1).
