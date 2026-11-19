# Contre-lecture du critère d'identité v4 et du devis v4 du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct) — v1

- Heure (`date -u`) à l'écriture : 2026-11-19T11:02:56Z ; l'heure du scellement est celle du fichier compagnon.
- Contre-lecteur : sous-agent neuf lancé par la session mère, modèle **Claude Opus 5.5** (`claude-opus-5-5`), d'un autre modèle que le
  rédacteur (Claude Fable 5.2), selon la section « Qui conçoit » (R-3735). Il n'a écrit ni les pièces relues, ni leurs versions
  précédentes, ni le programme de comparaison, ni les rapports d'historique. Pièces de **classe A** : contre-lecture complète.
- Objet : branche `claude/brave-galileo-jhp684`, commit `14eca8a13a56a64027614148b2ebaecbdf237d30`, lu par son identifiant
  (`git show`), sans extraction de l'arbre. Empreintes recalculées, égales à l'attendu et au compagnon :
  critère v4 `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v4.md`
  `60df6c539f8aa0a04d5eec0c5b47a421bb780dc5ab8d0251c80ebfb06c67ccfa` (37 168 octets) ; devis v4
  `docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v4.md`
  `770a779411ed4c3006b50671d0402363a4922871aa605dbeb0ea70cafd3678f4` (30 833 octets).
- Lu en plus : le critère v3 et le devis v3 du même commit (matière première du rédacteur) ; sur la branche principale, la
  contre-lecture du critère v1 (`9241903708eacef5244bf81b0b071131edab0023195d8a068dc7051cd57883ff`), la vérification du critère v2
  (`8a6045bb3db81188e9c0889fbd69bafa57085c5336bff6db7dec7e24de1a4f94`), la vérification du programme v2
  (`8cd01e58bbdb724c12924595ba681ad726e22f273a74a108b4e24311bc98523b`) ; les deux essais de `torch.save` et leurs sorties ; le relevé de
  prix ; au commit, `b_beta_lancer_v3.py` (l. 480-512 et 940-972) et `controles_b_beta_v2.py` (l. 139-161, 320-331, 407-410) ; la
  commande v8 par recherche (table de destruction) ; au registre des accords, la ligne GO-2026-11-18-02.
- Recalculé : empreinte du programme de comparaison v2 `23311588…` et de ses essais `65822ab5…` (égales au critère) ; empreinte du
  lanceur `582fd9ef322de2476b19eb4ce4868f99d7ea4ee52870edbaf316275bbd1dd1ea`, **identique au commit du dépôt réduit de la course du
  18** (`5e5cb65b…`, présent dans le dépôt) ; empreinte du texte de `_split_half_64` par la méthode de `empreinte_fonction` :
  `a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c`, égale à celle que cite le critère ; arithmétique du § 3 du devis
  (bloc par bloc : attendu 12,01 h et 13,31 h ; pire cas 16,54 h et 19,14 h ; coûts 28,5 / 39,2 / 43,3 / 45,6 et 31,6 / 45,4 / 50,1 /
  52,4 ; minuteries 17,7 h et 20,4 h ; marges 6,5 % et 6,4 % ; course de mesure à part 2,8 h × 2,3713 = 6,64 USD) : **juste** ; § 3 du
  devis v3 contre v4 : seuls des retours à la ligne, « lanceur v4 » → « lanceur neuf », et une phrase de risque ajoutée ; **aucun
  chiffre changé**, comme annoncé.
- **Non lu, selon le mandat** : `docs/verdicts/`, tout fichier dont le nom commence par « verdict » (donc ni `verdict-b-beta-v1.md`, que
  le devis cite pour les marges du 18), `diag/`, `runs/`, `donnees/`, tout résultat de l'étape B bis ou des lentilles, tout fichier
  « consigne-privee » ou « conception-ii-b », `brouillons/ii-b-saboteur-budget-v1/`. En conséquence **non vérifiés par moi** : les
  empreintes et valeurs des pièces du 18 (§ 2 du critère : `129c43b0…`, `2dce646e…`, `17304c93…`, `b90c1514…`, tailles, plages
  0,0694–0,6769 et 0,8015–2,1916, marges « 55 sur 64 » et « 20 sur 28 ») ; je les tiens des rapports d'historique, qui les ont
  recalculées pour la plupart. Les 82 essais n'ont pas été rejoués ici (ils lisent les pièces de `diag/`).
- Aucune dépense, aucune machine, aucun commit, aucun fichier existant modifié. **Aucun refus d'outil.** Une remarque : une demande
  `git cat-file` sur le commit du code voisin (`849bfe16…`, absent du dépôt) a déclenché une récupération paresseuse refusée par le
  serveur (« not our ref ») ; ce n'est pas un refus de permission, et rien n'a été obtenu.

## Conclusion

**Pas avant : six corrections courtes (E1 à E6), quatre au critère, une partagée, une au devis ; aucune ne touche un seuil ni un
chiffre du devis.** Le critère est bien écrit avant toute lentille réajustée, ses seuils sont fixés, et les cinq changements de fond
du rédacteur sont justes (la règle de la variante A au palier 2, la liste fermée H1 à H7, le zéro exact de H4, « plancher, jamais
plafond », l'ordre de grandeur de la course de mesure à part). Mais la liste H ne reprend pas la correction F2 (fonction de référence
fixée, lanceurs rattachés aux courses) ni la moitié de F3 (couches des matrices) ; le contrôle H6 ouvre un audit sans dire ce qu'il
peut conclure ; H5 laisse au contrôleur le cas d'une clé de versions neuve que le devis v4 risque justement de créer ; la phrase du
billet reste au pluriel malgré le cas mixte ; et le devis n'écrit ni l'inventaire de la machine avant destruction ni le chemin d'une
copie en échec, ce qui reproduirait la perte du 18. Une v5 courte de chaque pièce suffit ; vérification par le même lecteur.

**Recommandation au directeur entre les variantes : B, confiance 0,75** (§ 5 ci-dessous).

## 1. Fixé avant de voir, sans marge après coup (R1) ; contrôles à la main fermés ? — **Avant : oui. Fermés : presque ; trois choix restent (E3, E5, et E1 pour la fonction).**

- Aucune lentille réajustée n'existe, aucune ligne de calcul n'est ouverte : la règle du préenregistrement est tenue au moment de
  l'écriture. Les seuils sont des constantes (10⁻³, 10⁻⁹, 10⁻⁶ pour `diffs` au premier palier, 0,10 pour la stabilité), l'ordre
  d'évaluation est écrit (§ 4, « Procédure »), et les contrôles H ne peuvent que suspendre ou rendre « non comparable » : aucun ne peut
  faire monter une mention. Le choix entre « non comparable » et « suspendu » est mécanique (octets différents ou égaux).
- **Ce qui reste ouvert au contrôleur :**
  1. **H6** ouvre un audit (« le verdict attend l'audit, qui commence par H2 ») sans dire ce que l'audit conclut s'il ne trouve rien.
     Le cas n'est pas d'école : si seules les sommes de la cible `mid` diffèrent d'une machine à l'autre, le fichier d'ajustement
     change d'octets alors que l'export de R (moyenne des sommes de la cible `out`) peut être identique ; on aurait 31 matrices égales
     sur 31 et des séries inchangées, et la mention « matrices non comparables » serait fausse dans sa lettre. Le contrôleur devrait
     alors décider seul de garder le deuxième palier, de suspendre, ou de prétendre à l'identité de l'export. **E3** ferme : l'audit ne
     peut que suspendre ; s'il ne trouve rien, la mention reste, le fait est écrit, aucune identité n'en est tirée.
  2. **H5** exige « `versions` égales, hors le champ `plateforme` ». Le devis v4 (§ 5, point 5 g) fait consigner « le modèle de carte,
     la version du pilote et les versions de la machine » par une « pièce de résultat » sans dire qu'elle est à part du manifeste. Si le
     lanceur neuf ajoute une clé à `versions`, le contrôleur doit choisir entre « non comparable » (lettre de H5) et « clé neuve
     tolérée » (esprit). **E5** ferme des deux côtés.
  3. **Le préalable « même texte de `_split_half_64` »** compare les deux lanceurs passés en arguments, sans que le lanceur de
     référence soit fixé ni le lanceur neuf rattaché à sa course (vérification du programme v2, F2 et mineure 3 ; sonde T1 : le même
     lanceur modifié, donné deux fois, passe). Le critère cite l'empreinte de référence (§ 2) mais aucune règle ne l'emploie. Le
     contrôleur qui la vérifierait le ferait de son propre chef. **E1** l'écrit (H8).
- H1 « relève » le commit et les empreintes des pièces neuves, sans dire qu'elles doivent être **égales** aux fichiers du même chemin à
  ce commit : écrit dans E5 (après), sans changer l'esprit.
- Pas de marge par ailleurs : la tolérance de 10⁻³ ne décide plus que d'un nœud en variante B (différence n° 1) ; la liste des couches
  stables est fixée (« dans les deux ajustements ») ; les phrases permises et interdites sont écrites ; les chiffres de R sont
  obligatoires sans qualificatif.

## 2. Corrections des trois rapports d'historique — **toutes reprises sauf F2, la moitié de F3, la mineure 3 du programme, la remarque 4 de l'annexe ; deux remarques de l'annexe sans réponse.**

| rapport | remarque | état dans les v4 |
|---|---|---|
| contre-lecture du critère v1 (`92419037…`) | C1 à C6 | reprises (mention, aveuglement, ce que chaque mention autorise, audit dans les deux sens, rattachement de l'écart entre chemins, qui applique) |
| | mineures 1 à 7 | reprises ; la mineure 5 (commentaire « jamais lue pour un seuil ») est enfin inscrite au devis v4, § 5, point 5 i ; la mineure 7 (commit des références) est remplacée par les empreintes, ce que la vérification v2 (mineure 3) admettait |
| vérification du critère v2 (`8a6045bb…`) | D1 à D7 | reprises ; D6 précisée à juste titre (la v3 prêtait au programme une comparaison des manifestes qu'il ne fait pas) ; D7 tenue mot pour mot au devis v4, § 7 |
| | mineures 1 à 4 | reprises |
| vérification du programme v2 (`8cd01e58…`) | F1, export neuf rattaché | reprise par H2 (sondes T1, T1 bis) |
| | **F2, fonction de référence fixée par une constante** | **manque** ; l'empreinte `a5495c68…` est citée au § 2 sans règle ; correction **E1** (H8) |
| | **F3, mêmes couches des deux côtés** | **à moitié** : H3 couvre les séries (0 à 27), pas les matrices des moitiés (0 à 30 ; sonde T3c du vérificateur : couches décalées, « 0 égale sur 31 », sans alerte) ; correction **E2** |
| | F4, séries de R dans la cohérence du premier palier | reprise par H4, plus stricte (zéro exact au lieu de 10⁻⁹) ; défendable (point 4) |
| | F5, table des différences des manifestes | reprise à la main, mais seulement dans l'audit, qui n'a pas lieu au deuxième palier sans déclencheur ; H5 en couvre l'essentiel ; matériel : correction **E5** |
| | F6, essais à ajouter | renvoyés à une version 3 du programme (recommandation du rédacteur, devis § 5, point 6) ; sans effet sur le critère tant que la liste H s'applique à la main |
| | mineure 1, champ `etape` | sans réponse ; mineure m6 ci-dessous |
| | mineure 2, reprise lue au résultat | reprise (« lue au journal de la course », § 8) |
| | **mineure 3, lanceur neuf rattaché à sa course** | **manque** ; H1 relève son empreinte sans la rattacher ; correction **E1** |
| | annexe 1, 2, 3 (sauf F2), 5, 8 | reprises |
| | **annexe 4, phrase du billet et cas mixte** | **manque** : la phrase permise reste au pluriel (« Les deux lentilles… Nous les avons réajustées… ») alors que chaque lentille est jugée seule ; correction **E4** |
| | annexe 6, essai court sur deux machines avant la course | **sans réponse** dans le devis v4 (« Ce qu'on peut attendre » dit l'inconnu, ne dit pas pourquoi on ne le mesure pas) ; mineure m4 |
| | annexe 7, croquis numérique des matrices pour un réajustement futur | **sans réponse** ; relève de « récupérer ce qui est récupérable » ; mineure m4 |

Le rédacteur écrit que la liste H « couvre cinq défauts du programme v2 » : ce sont ceux de **ses** sondes (T1, T1 bis, T2, T3, T4,
plus les empreintes des pièces neuves non versées). Ceux que la vérification du programme v2 a trouvés et qu'il ne sonde pas (F2, la
partie matrices de F3, la mineure 3) ne sont pas couverts.

## 3. « Plancher, jamais plafond » — **juste ; la phrase du billet est honnête, ni trop forte ni trop faible ; deux précisions de lettre.**

- **Mathématiquement.** Soit, à une couche, s(M) = maxᵢⱼ |Mᵢⱼ − Aᵢⱼ| l'écart maximal entrée par entrée d'une matrice M à une ancre A
  fixe (la lentille R publique ou l'identité). C'est la distance de la norme du maximum ; par l'inégalité triangulaire inverse,
  |s(M) − s(M′)| ≤ maxᵢⱼ |Mᵢⱼ − M′ᵢⱼ|. Un changement δ de la série prouve donc que les deux matrices diffèrent d'au moins δ en une
  entrée ; un changement nul n'exclut rien (M′ = M + D avec D nul aux entrées qui font le maximum). Comme toute norme usuelle
  (Frobenius, spectrale) majore la norme du maximum, le « plancher » vaut pour elles aussi ; et le plus grand changement sur les
  couches 0 à 27 minore l'écart sur toutes les couches. **Juste.**
- **Deux conditions de lettre, qu'il faut dire.** (a) L'ancre doit être la même aux deux courses : elle l'est par construction, la
  lentille publique étant épinglée par révision et vérifiée par empreinte dans le lanceur (`b_beta_lancer_v3.py`, l. 58, 125-130 et 650 ;
  `LENTILLES_NP["npR"]`), à condition que le lanceur neuf garde ces lignes (E1 le vérifie par la fonction ; la phrase « l'ancre a
  changé » de H4 suppose ce cas). (b) Le calcul est fait en simple précision (`ecart_max`, `controles_b_beta_v2.py`, l. 139-143 :
  soustraction, valeur absolue et maximum en `float32`) : l'inégalité tient à l'arrondi près, soit au plus u·(s(M) + s(M′)) avec
  u = 2⁻²⁴, c'est-à-dire ≈ 2,6 × 10⁻⁷ pour des écarts de l'ordre de 2,19. Sans effet sur le sens ; à écrire pour que « jamais » reste
  vrai à la lettre (mineure m1).
- **La phrase du billet.** « ces changements sont un plancher, non un plafond, de l'écart entre les matrices des deux courses » est
  exacte et ferme la lecture flatteuse que D5 visait (« peu de changement, donc proches »), sans en ouvrir une défavorable : elle
  n'affirme aucun déplacement quand le changement est nul. Elle n'est pas trop faible : la conséquence positive (« les matrices
  diffèrent d'au moins [y] ») s'en lit directement, et les chiffres sont obligatoires. Elle n'est pas trop forte : rien n'y dit que les
  matrices bougent. Deux précisions : nommer la norme (« de l'écart maximal, entrée par entrée, entre les matrices ») et dire « le même
  code d'ajustement » plutôt que « le même code », le lanceur ayant changé (devis v4, § 5, point 5 a à i) : E4.

## 4. Zéro exact au palier 1 pour les séries de R (H4) — **tenable ; ne rend pas le palier 1 plus difficile qu'il ne l'est déjà ; ce qui le rend incertain est dit dans le devis, pas dans H4.**

- **Pourquoi c'est tenable.** Au palier 1, les octets du fichier d'ajustement sont identiques. L'export de R est la moyenne des sommes de
  la cible `out` (garde (o), `moyennes_fit`, l. 515 et suivantes du lanceur) : division et addition entrée par entrée, déterministes en
  arithmétique flottante normalisée, sur quelque machine que ce soit. Les séries sont calculées sur le processeur par soustraction,
  valeur absolue et maximum en `float32` : aucune réduction dont l'ordre dépendrait du processeur, du nombre de fils ou de la carte (un
  maximum est exact). L'ancre est épinglée par empreinte. Le passage par JSON garde les nombres à l'identique (`float` de Python). Les
  mêmes entrées donnent donc les mêmes bits, et un changement non nul signale bien un export ou une ancre différents.
- **Pas plus dur que ce qui est déjà exigé.** D1 (reprise au § 4, point 4) suspend déjà le premier palier si une empreinte de matrice
  des moitiés diffère : cela suppose déjà un export reproductible au bit près. H4 étend la même exigence à la lentille entière, la
  seule qu'une lecture charge et que rien d'autre ne trace. Si l'export n'était pas reproductible au bit, D1 tomberait avant H4.
- **Contraste utile, à juste titre non exigé à zéro** : `diffs_float64` (borne de 10⁻⁹) et `diffs` (borne de 10⁻⁶, H7) passent par
  `np.linalg.norm`, c'est-à-dire un produit scalaire de la bibliothèque d'algèbre linéaire, dont le noyau et l'ordre de sommation
  dépendent du processeur : des écarts de l'ordre de 10⁻¹⁷ et 10⁻⁸ sont possibles d'une machine à l'autre sur les mêmes sommes. Les
  bornes du critère les absorbent ; exiger zéro là aurait été une erreur, et le critère ne la fait pas.
- **Ce qui rend le palier 1 incertain** est en amont : dix heures de sommes sur carte (modèle en `bfloat16`, produits en TF32, sommes
  en simple précision) doivent retomber sur les mêmes bits. C'est plausible sur le même modèle de carte avec les mêmes bibliothèques de
  calcul (le filtre de la commande et le relevé exigent `H100_SXM`), non garanti. Le devis v4 le dit (§ 1, « Ce qu'on peut attendre » :
  « Le devis ne compte donc pas sur le palier 1 »). Le critère n'a pas à le redire ; une phrase dans H4 qui dit qu'il n'ajoute rien de
  plus dur que D1 éviterait qu'un lecteur le croie (mineure m2). Deux points de lettre sur l'égalité d'octets elle-même (mineure m3) :
  le nom qui entre dans les octets est celui **au moment de l'écriture** (`02_fit.py` écrit sous un nom provisoire puis remplace,
  `os.replace`, l. 166 ; l'essai `4fdec19d…` imite ce geste avec `r-llama.tmp`) : il faut que ce nom provisoire soit déterministe ; et le
  lieu des tenseurs (processeur, ou carte et son numéro) entre aussi dans l'archive, ce que les essais sur processeur ne couvrent pas
  (sans conséquence sur une machine à une seule carte, à dire).

## 5. Le devis — **le directeur lit en clair ce que chaque variante achète, le coût et le plafond ; la fin de course n'écrit ni l'inventaire avant destruction ni l'échec de copie (E6) ; aucune dépense cachée, deux montants encore ouverts et dits.**

- **Ce que chaque variante achète au palier 2** : clair (§ 2, § 4, § 7). A : « ni identité, ni mesure propre, ni lecture », « poids
  inutilisables en l'état ». B : « les seules mesures de la lentille rangée », lues par un lecteur neuf, sans effet sur le verdict du 18.
  Au palier 1 : A suffit à l'identité ; B ajoute une seconde mesure de la même lentille. L'ordre de grandeur de la course de mesure à
  part (≈ 2,8 h, ≈ 6,6 USD, juste) est utile et honnêtement dit « pas un devis ».
- **Coût et plafond** : clairs, justes (vérifiés bloc par bloc), et inchangés depuis la v3. Les plafonds (54 et 62 USD) laissent 6,5 %
  au-dessus du pire cas avec frais.
- **Fin de course.** La clé est bien traitée (clé gardée hors machine, clé neuve restreinte à vérifier avant le GO, risque d'écrasement
  dit, parade par empreinte). La destruction « sans attendre Lazar » après la première relecture lève la réserve N-2. **Mais** :
  (a) aucun **inventaire** des sorties de la machine (noms, tailles, empreintes) n'est exigé avant la destruction, alors que la consigne
  permanente « récupérer ce qui est récupérable » l'exige et que la perte du 18 vient précisément de là ; (b) rien n'est dit si la
  **copie ou la relecture échoue** : l'ordre (2) puis (3) laisse croire qu'on détruit de toute façon, la commande v8 avait pourtant une
  ligne « poussée finale en échec → pas sans la mère » ; (c) la garde (arrêt dur), la minuterie et la garde de crédit **détruisent
  même si une lentille n'est pas copiée** : c'est le seul cas de perte accepté d'avance, il faut l'écrire pour que Lazar le lise avant
  d'accorder ; (d) si la plateforme ne recalcule pas les empreintes, « la session télécharge au moins une fois (≈ 31 Go) » se heurte au
  disque limité du conteneur : le calcul d'empreinte en flux, sans écriture sur disque, lève l'obstacle. Correction **E6**.
- **Dépense cachée** : aucune dans les lignes chiffrées. Restent **ouverts et dits** : le coût mensuel du stockage privé chez la
  plateforme de modèles (§ 5, point 9 : « à relever avant le GO ») — c'est une dépense récurrente, elle doit figurer en chiffre dans la
  ligne de GO, pas seulement au relevé ; et, en variante A au palier 2, la course de mesure à part (≈ 6,6 USD hors retour des 31 Go et
  hors préparation), que le devis dit bien conditionnelle et sur devis neuf.
- **Ma recommandation entre A et B : B, confiance 0,75** (le rédacteur dit 0,7). Raisons : au palier 2, que rien n'exclut, A achète
  des poids qu'aucune lecture ne peut employer sans une seconde course (≈ 6,6 USD au moins, plus un montage, un transfert de 31 Go et
  des textes), soit plus que les ≈ 3,1 USD d'écart attendu ; au palier 1, B rejoue la condition décisive à marge mince du 18, ce qui
  est une information même sans effet sur le verdict accepté. Ce qui retient la confiance : B demande deux textes de plus scellés avant
  la création (statut de la seconde mesure, plan de lecture), et ce plan doit fixer **d'avance** sur quels critères gelés de la tranche
  la lentille du palier 2 sera dite lisible et à quelles couches — sinon « dans les limites de cette lecture » (critère, § 5) devient
  une marge ; A ne vaut mieux que si l'on tient le palier 1 pour probable, ce qu'aucune pièce ne permet.

## 6. Symétrie (R4) et replis (R5) — **symétrie tenue dans les déclencheurs ; trois replis silencieux possibles, dont un grave (copie en échec).**

- **Symétrie.** Le trop propre (premier palier ; écart nul à octets différents ; au deuxième palier, 31 matrices égales ou série nulle ;
  `diffs` qui bouge au-delà de la borne) et le décevant (« différente », « non comparable », anomalie) déclenchent le même audit, fait
  par la même personne, sans lire une mesure. Deux réserves : l'issue de l'audit de H6 n'est pas écrite (E3) ; et le deuxième palier
  sans déclencheur, l'issue la plus probable, n'a ni table des manifestes ni relevé du matériel, que les autres issues ont : le relevé
  du matériel, sans coût, doit être fait à tous les paliers (E5, dans H1).
- **Replis silencieux restants :**
  1. **Copie ou relecture en échec à la fin de course** : rien n'est écrit ; destruction possible avec des lentilles non versées
     (E6). C'est le plus grave : il reproduirait la perte du 18.
  2. **Arrêt du programme de comparaison sur une erreur** (la vérification v2 en a montré, par exemple `max()` d'une suite vide) :
     rien n'est dit ; la lentille resterait sans verdict. Écrire : arrêt sur erreur = « non comparable » (ou suspendue à empreinte
     égale) et nœud de Lazar (mineure m5).
  3. **Variante B, seconde course incomplète** après des ajustements copiés : la lentille du palier 2 n'aurait alors aucune mesure
     propre, comme en variante A ; à dire (mineure m5).
- Bien traités : le passage d'un palier à l'autre est nommé ; une valeur non finie ou absente rend « non comparable » avant tout
  maximum ; une lentille non lue est dite en une phrase dans le billet ; « aucune relance pour obtenir un autre palier » est écrit aux
  deux pièces.

## Corrections (texte avant et après)

**E1 — Fonction de référence fixée et lanceurs rattachés (critère, § 7, liste H ; F2 et mineure 3 de la vérification du programme v2).**
- Avant : la liste s'arrête à « **H7 — `diffs`.** […] déclencheur (vii), mention suspendue, nœud de Lazar. »
- Après, ajouter : « - **H8 — Fonction et lanceurs rattachés.** Le lanceur de référence passé au programme a l'empreinte
  `582fd9ef322de2476b19eb4ce4868f99d7ea4ee52870edbaf316275bbd1dd1ea` et est égal à
  `git show 5e5cb65b4daf8726ebe1c4032a836b850de7ea2f:src/controle_ia/neuron_lens/b_beta_lancer_v3.py` ; l'empreinte du texte de
  `_split_half_64` (méthode `empreinte_fonction` du programme) y vaut `a5495c68779bb67059cade18b3a92aaf7cf7fd0200f1770b038d8c5d0e62703c` ;
  le lanceur neuf passé au programme est égal au fichier du même chemin au commit que porte le manifeste neuf (`git show <commit>:<chemin>
  | sha256sum`), et l'empreinte du texte de sa fonction vaut la même. Manqué : « non comparable » ou suspendu. »
- Et partout où la liste est citée (critère § 4, point 4 ; § 6 ; § 8 ; § 7, recommandation du rédacteur ; devis § 5, point 6) :
  « H1 à H7 » → « H1 à H8 ».

**E2 — Couches des matrices (critère, § 7, H3 ; reste de F3).**
- Avant : « - **H3 — Séries de R sur les mêmes 28 couches.** Les clés des deux séries sont 0 à 27 des deux côtés, et la sortie du
  programme porte « couches : 28 » pour chacune. Manqué : « non comparable » ou suspendu. »
- Après : « - **H3 — Mêmes couches des deux côtés (R).** Les clés des deux séries sont 0 à 27 des deux côtés, et la sortie du programme
  porte « couches : 28 » pour chacune ; les clés de `matrices_moities` sont 0 à 30 des deux côtés. Manqué : « non comparable » ou
  suspendu. »

**E3 — Ce que l'audit peut conclure (critère, § 7, H6, et § 6).**
- Avant (H6) : « 31 matrices égales sur 31 avec des octets d'ajustement différents, ou une série inchangée à zéro exact : déclencheur
  (vi), audit ; le verdict attend l'audit, qui commence par H2. »
- Après : « 31 matrices égales sur 31 avec des octets d'ajustement différents, ou une série inchangée à zéro exact : déclencheur (vi),
  audit ; le verdict attend l'audit, qui commence par H2. S'il ne trouve aucun contrôle manqué, la mention du programme reste, sans
  montée, et le verdict l'écrit en une phrase (« pour R, [31 matrices des moitiés égales sur 31 | série … inchangée] malgré des octets
  d'ajustement différents ; audit sans contrôle manqué ») ; aucune identité, de la lentille ni de son export, n'en est tirée. »
- Avant (§ 6) : « L'audit est versé scellé avec le verdict d'identité ; un contrôle manqué suspend la mention et ouvre un nœud de Lazar. »
- Après : « L'audit est versé scellé avec le verdict d'identité ; un contrôle manqué suspend la mention et ouvre un nœud de Lazar ; un
  audit sans contrôle manqué laisse la mention telle que la procédure l'a rendue. L'audit ne fait jamais monter une mention. »

**E4 — Phrase du billet, lentille par lentille ; « même code d'ajustement » ; norme nommée (critère, § 5, deuxième palier).**
- Avant : « Phrase permise (les crochets se remplissent par les chiffres de la sortie du programme) : « Les deux lentilles mesurées le
  18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le même code, le même corpus et les mêmes graines
  sur une autre machine. […] et ces changements sont un plancher, non un plafond, de l'écart entre les matrices des deux courses. […] » »
- Après : « Phrase permise si **les deux** lentilles sont au deuxième palier (les crochets se remplissent par les chiffres de la sortie
  du programme) : « Les deux lentilles mesurées le 18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le
  même code d'ajustement, le même corpus et les mêmes graines sur une autre machine. […] et ces changements sont un plancher, non un
  plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux courses. […] » Si **une seule** lentille est au deuxième
  palier, la phrase est écrite pour elle seule, au singulier, et l'autre reçoit la phrase de son propre verdict :
  pour R : « La lentille R mesurée le 18 novembre a été détruite avec la machine louée. Nous l'avons réajustée avec le même code
  d'ajustement, le même corpus et les mêmes graines sur une autre machine. Le fichier obtenu n'est pas identique à l'octet. La différence
  entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de celle du 18 novembre (tolérance fixée
  d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux moitiés. L'écart maximal de chaque
  matrice à la lentille publique et à l'identité change d'au plus [valeur] et [valeur] d'une course à l'autre, pour des écarts qui
  valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était fixé d'avance pour ces deux séries, et ces changements sont un
  plancher, non un plafond, de l'écart maximal, entrée par entrée, entre les matrices des deux courses. Nous ne savons pas si la lentille
  réajustée lit comme celle du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elle | ont été refaites sur elle et
  sont rapportées à côté]. » ;
  pour S : la même, sans la phrase des deux séries, remplacée par « Aucune autre comparaison n'existe pour cette lentille. »
  En anglais, « the same code » → « the same fitting code » ; « on the gap between the matrices » → « on the largest entrywise gap
  between the matrices » ; versions au singulier sur le même patron. « Même code d'ajustement » ne s'écrit que si H5 et H8 sont tenus. »

**E5 — Versions et matériel : rien à décider pour le contrôleur, relevé à tous les paliers (critère, § 7, H1 et H5 ; devis, § 5, point 5 g).**
- Avant (H5) : « `versions` égales, hors le champ `plateforme` (le noyau de l'hôte) ; »
- Après : « `versions` : mêmes clés et mêmes valeurs des deux côtés, hors le champ `plateforme` (le noyau de l'hôte) ; une clé présente
  d'un seul côté est un manqué ; »
- Avant (H1) : « Le commit de la branche de résultats et l'empreinte de chaque pièce neuve passée au programme (résultat d'ajustement,
  manifeste, résultat d'export pour R, lanceur neuf) sont relevés et versés avec le verdict. Manqué : pas de verdict. »
- Après : « Le commit de la branche de résultats et l'empreinte de chaque pièce neuve passée au programme (résultat d'ajustement,
  manifeste, résultat d'export pour R, lanceur neuf) sont relevés ; chacune est égale au fichier du même chemin à ce commit ; elles sont
  versées avec le verdict. Le modèle de carte, la version du pilote et les versions de la machine neuve sont recopiés de la pièce du
  matériel (devis v4, § 5, point 5 g), à tous les paliers, sans vis-à-vis au 18. Manqué : pas de verdict. »
- Avant (devis, § 5, point 5 g) : « (g) **une pièce de résultat qui consigne le modèle de carte, la version du pilote et les versions
  de la machine** (non consignés le 18), »
- Après : « (g) **une pièce de résultat à part, poussée sur la branche de résultats, qui consigne le modèle de carte, la version du
  pilote et les versions de la machine** (non consignés le 18) ; le champ `versions` du manifeste garde exactement les clés du 18
  (contrôle H5 du critère), »

**E6 — Fin de course : inventaire, copie en échec, perte acceptée d'avance (devis, § 5, point 3).**
- Avant : « **Fin de course en quatre temps** (réserve N-2) : (1) copie ; (2) **première relecture** des empreintes au lieu de rangement
  par la session, clé de la machine encore valide (une copie fausse peut encore être refaite), révision du dépôt notée ; (3)
  **destruction de la machine par son identifiant, sans attendre Lazar** ; (4) révocation de la clé par Lazar quand il peut, puis
  **seconde relecture** de la même révision avec la clé gardée de la session (lecture seule). »
- Après : « **Fin de course** (réserve N-2) : (0) **inventaire** des sorties de la machine (noms, tailles, empreintes), poussé sur la
  branche de résultats avec toutes les pièces légères (résultats, manifeste, journaux) ; (1) copie ; (2) **première relecture** des
  empreintes au lieu de rangement par la session, clé de la machine encore valide, révision du dépôt notée ; si la relecture d'un
  fichier échoue, sa copie est refaite, au plus deux fois ; si elle échoue encore, **pas de destruction sans la mère** (ligne neuve de
  la table de destruction de la commande v9, sur le modèle de « poussée finale en échec »), dans la limite de l'arrêt dur ; (3)
  **destruction de la machine par son identifiant, sans attendre Lazar, seulement après (0) et (2) tenus** ; (4) révocation de la clé
  par Lazar quand il peut, puis **seconde relecture** de la même révision avec la clé gardée de la session (lecture seule). **Perte
  acceptée d'avance, et seulement celle-ci** : la garde de dépense (arrêt dur), la minuterie et la garde de crédit détruisent la machine
  même si une lentille n'est pas encore copiée ; la perte est alors écrite à l'inventaire, au verdict d'identité (« non réajustée ») et
  au billet. Si la plateforme ne recalcule pas les empreintes (point 9), la session les recalcule **en flux** (téléchargement passé
  directement au calcul d'empreinte, sans écriture sur disque) ; durée et trafic dits avant. »

## Remarques mineures
1. **m1 — Arrondi du plancher** (critère, § 4, « Leur sens exact ») : ajouter « à l'arrondi de la simple précision près (au plus
   ≈ 3 × 10⁻⁷ ici, le calcul étant fait en `float32`) ; l'ancre est la même aux deux courses, épinglée par empreinte dans le lanceur ».
2. **m2 — H4** : ajouter « H4 n'exige rien de plus que D1 : l'égalité des matrices des moitiés suppose déjà un export reproductible au
   bit ; les séries ne passent par aucune réduction dépendante de la machine (`ecart_max`, `controles_b_beta_v2.py`, l. 139-143). »
3. **m3 — Égalité d'octets** (critère, § 4, mention 1 ; devis, § 1) : « le nom de fichier » → « le nom de fichier au moment de
   l'écriture (nom provisoire avant `os.replace`, `02_fit.py`, l. 166) » ; dire que le lieu des tenseurs entre aussi dans l'archive et
   que les essais, sur processeur, ne le couvrent pas. Le critère dit « modèle de carte (connu du seul registre des accords : H100) » :
   le filtre de la commande exigeait `H100_SXM` (relevé `90395583…`, en-tête) ; le dire.
4. **m4 — Remarques 6 et 7 de l'annexe de la vérification du programme v2** : y répondre au devis, § 10. Pour l'essai court sur deux
   machines, une raison de l'écarter existe (deux montages ≈ 6 USD, l'ordre de l'écart entre A et B, et sans objet si B est retenue) :
   l'écrire. Pour le croquis numérique des matrices (projections sur des vecteurs tirés d'une graine fixée, normes par couche), versé
   par la course neuve : quelques minutes de processeur, et il rendrait un futur réajustement comparable matrice par matrice ; je
   recommande de l'ajouter au point 5 h, ou de dire pourquoi non.
5. **m5 — Replis** : écrire « un arrêt du programme de comparaison sur une erreur vaut « non comparable » (ou suspendue à empreinte
   égale) et nœud de Lazar » (critère, § 4, Procédure) ; et « en variante B, une seconde course incomplète laisse la lentille du
   deuxième palier sans mesure propre, comme en variante A » (critère, § 5 ; devis, § 2).
6. **m6 — Champ `etape`** des résultats neufs (« ajustement-R », « ajustement-S ») : à relever dans H1 (mineure 1 de la vérification du
   programme v2).
7. **m7 — Provenance des sondes et des essais rejoués** (critère, § 7) : la table des sondes T1 à T4 et « 82 passed » n'ont ni chemin ni
   empreinte dans le dépôt (R6). Verser `sondes_v1.py`, sa sortie et la sortie des essais, scellés, ou dire ces lignes non opposables,
   comme pour les dix altérations.
8. **m8 — Stockage privé** (devis, § 5, point 9, et décision 3) : le coût mensuel relevé entre en chiffre dans la ligne de GO de calcul.

## Ce qui a servi (hors dépôt)
Sous-dossier du bloc-notes `scratchpad/opus-contre-lecture-critere-v4/` : extraits du critère et du devis v3 et v4 au commit
`14eca8a1` ; un calcul de l'empreinte du texte de `_split_half_64` (module `ast` et `hashlib`, lancé en mode isolé) ; une comparaison
du § 3 des devis v3 et v4 (`difflib`). Rien n'écrit dans le dépôt hors ce rapport et son compagnon.
