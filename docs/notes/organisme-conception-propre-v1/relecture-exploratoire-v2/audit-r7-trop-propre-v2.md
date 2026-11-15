# Audit « R7 trop propre » — conclusion : **relu, accord explicable**

**Audit de symétrie (R4 du programme) de l'accord parfait de « R7 retenu » entre la première lecture et la relecture
exploratoire v2 des fiches de la course « conception propre » — v2.**
Écrit par un auditeur neuf (sous-agent de la session mère), le 15 novembre 2026 vers 07:40 UTC (`date -u`), qui n'a écrit
ni la règle, ni les témoins, ni l'outil du lecteur, ni le programme de classement, ni le rapport du lecteur.

**De la v1** (`RE/audit-r7-trop-propre-v1.md`, `8802c7ba`, scellée à 07:37 UTC par le même auditeur, gardée, non
modifiée ; relue par lui avant remise). **Conclusion et chiffres inchangés.** Cinq corrections de lettre, et seulement
elles : (1) en tête, « ce que le montage dément » était trop fort — le montage montre que L1 et L2 ne sont pas deux
rejeux, il ne prouve pas à lui seul un effet de place (limite (a) du § 4) ; (2) § 2, la fenêtre des horodatages est
tenue « à deux secondes près » ; (3) § 2, les passages cités sont « à peine plus souvent » identiques entre lectures
(0,80 contre 0,77), non « pas plus souvent » ; (4) § 5, le journal s'écrit en ajout, le refus d'écraser vaut pour les
réponses, erreurs et relevés ; (5) § 2 et § 4, l'affirmation « seuls les témoins voisins changent dans ce qui est servi »
est désormais calculée par le programme (v2 : `messages_servis`), au lieu d'être déduite. Le programme v2 ajoute ce seul
contrôle ; tous ses autres chiffres égalent ceux de la v1 (comparé).

**En trois lignes.**
1. La relecture a vraiment relu : 18 appels neufs, treize heures après les 18 de la première lecture, 36 identifiants
   d'appel tous distincts, aucune réponse ni aucun envoi commun, aucun motif de « non » (texte libre du lecteur)
   identique au caractère près ; l'outil n'a aucune voie qui relise une réponse de la première lecture.
2. L'accord n'est parfait que sur la valeur **retenue** (le « et » des deux passages) : sur les 46 valeurs de passage de
   R7 (23 fiches réelles × 2 passages), **2 ont changé** entre les deux lectures, et le « et » les masque toutes deux
   (l'autre passage valait déjà 0).
3. Avec le taux de changement d'une valeur rejouée **à la même place**, mesuré sur les autres critères (3,7 % à 5,9 %),
   un accord parfait du retenu a une probabilité de **0,16 à 0,32** : rien d'anormal. Il ne serait improbable (0,2 % à
   3,4 %) que si L1 et L2 étaient deux rejeux dont le désaccord (17 %) donnerait le bruit. Or ce ne sont pas deux
   rejeux : ils diffèrent par le rang, le lot et les voisines, alors que d'une lecture à l'autre chaque fiche réelle a
   gardé, dans chaque passage, son étiquette, son lot et son rang. **Cet accord mesure la répétabilité du lecteur à
   position fixe, pas la fiabilité de R7.**

Ce rapport ne désigne aucune fiche (aucune n'y est nommée : comptes et motifs seulement), ne prononce aucun verdict de
porte et ne change rien au classement, qui reste « non lisible ». Aucun chiffre d'ici n'est opposable (R1) : lecture
exploratoire, 23 fiches.

Chemins relatifs à `docs/notes/organisme-conception-propre-v1/` ; `RE/` = `relecture-exploratoire-v2/` ;
`P1/` = `lecture-g1-v3-1/` (première lecture) ; `P2/` = `lecture-g1-v3-2/` (relecture) ;
`OUT/` = `RE/lecture-classement-v3-2/` ; `AU/` = `RE/audit-r7-trop-propre-v1-outils/`.

## 0. Pièces lues, empreintes vérifiées

Chaque pièce lue par le programme de calcul est confrontée à son compagnon `.sha256` (arrêt si différent) ; la liste entière
(104 pièces, empreinte courte et état du compagnon) est dans [RC] `pieces_lues`. Principales :

| Abrégé | Pièce | Empreinte | Compagnon |
|---|---|---|---|
| [RC] | `AU/resultat-calculs-audit-r7-v2.json` (sortie du programme de cet audit) | `970ebef7` | scellé par moi |
| [PC] | `AU/calculs_audit_r7_v2.py` (programme de cet audit) | `df0b4ecf` | scellé par moi |
| — | v1 gardées : `AU/calculs_audit_r7_v1.py`, `AU/resultat-calculs-audit-r7-v1.json` | `872bd703`, `9a0e91f5` | scellés par moi |
| [RL] | `RE/lecture-exploratoire-classement-v3-2-v1.md` (rapport du lecteur) | `246c8852` | OK |
| [C1] | `P1/classement/classement-v3-1.json` | `6ee04e1b` | OK |
| [C2] | `P2/classement/classement-v3-2.json` | `95da8192` | OK |
| [V1] | `P1/classement/lecture-verifiee-L1-v3-1.json`, `…-L2-…` | `6e9d4ff4`, `fd516d48` | OK |
| [V2] | `P2/classement/lecture-verifiee-L1-v3-2.json`, `…-L2-…` | `8b3ff58d`, `81d23dbd` | OK |
| [J1] | `P1/envois/journal-depense-v3-1.jsonl` | `00354642` | **absent** (voir plus bas) |
| [J2] | `P2/envois/journal-depense-v3-2.jsonl` | `194ad32d` | OK |
| [M1] | `P1/envois/manifeste-envois-v3-1.json` | `86bc90dc` | OK |
| [M2] | `P2/envois/manifeste-relecture-v3-2.json` | `31cfb36a` | OK |
| [K1], [K2] | `P1/envois/cle-lectures-v3-1.json`, `P2/envois/cle-lectures-v3-2.json` | `bbf36295`, `e06694a4` | OK |
| [I1], [I2] | `P1/envois/pile-interne-v3-1.json`, `P2/envois/pile-interne-v3-2.json` | `7c1e958d`, `6e15c406` | OK |
| [S1] | `P1/envois/releve-depense-v3-1-1.json`, `…-2.json` | `4cce4821`, `e22de7bf` | OK |
| [S2] | `P2/envois/releve-depense-v3-2-1.json` à `…-4.json` | `f0675c8d`, `f54adaa7`, `68973241`, `27f844c2` | OK |
| [OL] | `OUT/outil_lecteur_conception_propre_v3_2_1.py` (outil du lecteur) | `65902da3` | OK |
| [CL] | `OUT/classer_conception_propre_v3_2_1.py` (programme de classement) | `384211ee` | OK |
| [CL1] | `lecture-classement-v3-1/classer_conception_propre_v3_1.py` | `f9ef3695` | OK |
| [D] | `OUT/differentiel-outil-v3-1-v3-2-1.diff`, `…-outil-v3-2-v3-2-1.diff`, `…-classer-v3-1-v3-2-1.diff`, `…-classer-v3-2-v3-2-1.diff` | `54d735bd`, `2985c23d`, `1bae05d0`, `3963e6e0` | OK |
| [RG] | `RE/regle-v2-1.md` (et `RE/regle-v2.md`, `56c58b09`) | `b955e730` | OK |
| [CE] | `RE/commandes-exactes-v3.md` | `a9421070` | OK |

Les 36 réponses brutes (`P1/envois/reponse-L{1,2}-lot{1..9}-v3-1.json`, `P2/envois/reponse-L{1,2}-lot{1..9}-v3-2.json`) et
les 36 corps d'envoi : compagnons OK, empreintes dans [RC] `pieces_lues`.

**Seule pièce sans compagnon** : le journal de la première lecture [J1]. Vérifié autrement (R11) : son empreinte entière
est celle qu'épingle l'outil [OL] (constante `PREMIERE_LECTURE`, ligne 150) et celle que porte le relevé final [S1]
(`journal_sha256`) ; [RC] `2_appels.croise.journal_premiere_egal_a_l_epingle_de_l_outil` : vrai.

Rien d'ouvert sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune autre branche ; aucun appel payant ; aucune clé lue ;
aucun commit, aucune poussée. Seuls fichiers écrits : ce rapport et sa v1, [PC], [RC], leurs v1, et les compagnons.

## 1. Comment « R7 retenu » se calcule

- Dans [CL], ligne 123 (fonction `retenir`) : `int(v1[c]["compte"] == 1 and v2[c]["compte"] == 1)`. La valeur retenue d'un
  critère vaut 1 **si et seulement si les deux passages rendent un « oui » prouvé** ; c'est un « et », sans départage ni
  autre règle. Ligne 300 : le retenu de la relecture se calcule sur les deux lectures vérifiées du dossier `P2/envois`,
  et sur rien d'autre.
- Même ligne dans le programme de la première lecture ([CL1], ligne 140) ; la fonction `retenir` est identique, ligne
  pour ligne, dans [CL1] et [CL] (comparée directement) : la règle du retenu n'a pas changé entre les deux lectures.
- Recalcul indépendant ([RC] `1_regle`) : le retenu écrit dans [C1] et dans [C2] égale le « et » des valeurs comptées de
  [V1] et de [V2] pour **301 valeurs sur 301** dans chaque lecture (43 fiches × 7 critères) ; la valeur brute de R7 des
  lectures vérifiées égale celle des réponses brutes pour 86 entrées sur 86 dans chaque lecture.
- La comparaison « relecture contre première lecture » de [C2] lit le champ `retenu` de [C1] (empreinte épinglée dans
  [CL], ligne 80) dans une seule fonction (`retenu_premiere_lecture`, ligne 248), dont le résultat ne sert qu'aux deux
  descriptifs (lignes 367 à 369) : la première lecture n'entre pas dans le retenu de la relecture.

Conséquence mécanique du « et » : une valeur de passage qui change entre deux lectures ne change le retenu que si
l'autre passage vaut 1. Sur une fiche où un passage dit déjà 0, le retenu reste 0 quoi que fasse l'autre.

## 2. La relecture a-t-elle relu ? Oui

Tout ce paragraphe : [RC] `2_appels`, `2_releves`, `2_contexte_servi`, `2_R7_textes`, `2_tous_criteres_fiches_reelles`,
calculé sur les 36 réponses brutes, [J1], [J2], [M1], [M2].

**Appels.**
- 18 réponses par lecture, **36 identifiants d'appel distincts, aucun commun** aux deux lectures ; triés caractère par
  caractère, les 36 identifiants sont dans l'ordre de leurs horodatages (ceux de la relecture suivent tous ceux du matin).
- Horodatages rendus par le fournisseur : première lecture du 14 novembre 10:37:47 au 10:47:46 UTC ; relecture du
  14 novembre 23:41:56 au 23:51:18 UTC ; **12,9 heures** entre la dernière réponse de l'une et la première de l'autre.
  Chaque horodatage tombe, à deux secondes près, entre l'« envoi » et la « réception » de son lot au journal chaîné :
  18 sur 18 dans chaque lecture.
- Chaque fichier de réponse a l'empreinte que le journal a consignée à la réception et à la clôture : 18 sur 18 dans
  chaque lecture. Aucune empreinte de réponse, aucune empreinte de contenu, aucune empreinte de corps d'envoi n'est
  commune aux deux lectures (0, 0, 0).
- Jetons : entrée 229 912 contre 255 564 ; sortie 56 283 contre 55 825 ; **jetons lus en cache : 0 dans les 36
  réponses** ; aucun des 18 lots n'a le même nombre de jetons d'entrée ni de sortie d'une lecture à l'autre. Dépense au
  journal : 2,556635 contre 2,673445 USD. Mêmes paramètres d'envoi hors message dans les 36 corps, même modèle servi.
- Les quatre relevés de la relecture [S2] (issues « pause », « pause », « pause », « fait » ; 1, 6, 6, 5 envois) sont les
  tranches commandées par [CE], points 6 et 7 (`--envois-max 1`, puis `--envois-max 6`), pas une reprise après incident :
  aucun arrêt, aucune anomalie au journal [J2] (54 lignes : 18 envois, 18 réceptions, 18 clôtures, statut 200).
- Historique git : première lecture versée par `0ac97452` (14 novembre, 10:50 UTC), relecture par `93c5a36d` (23:53 UTC).

**Textes.** Un « oui » se justifie par un passage recopié de la fiche (donc souvent le même d'un appel à l'autre) ; un
« non » par un motif écrit librement par le lecteur. Le motif libre est le bon témoin d'une reprise.
- R7, même passage, d'une lecture à l'autre, fiches réelles (46 paires) : 16 paires « non » et « non », **motif identique
  au caractère près : 0 sur 16** ; 28 paires « oui » et « oui », passage cité identique : 19 sur 28 ; 2 paires de valeurs
  différentes.
- Tous critères : motif libre identique d'une lecture à l'autre, **0 sur 39** (entre les deux passages d'une même
  lecture : 0 sur 38).
- Les passages cités sont à peine plus souvent identiques d'une lecture à l'autre (218 sur 272, soit 0,80) qu'entre
  deux appels différents d'une même lecture (209 sur 271, soit 0,77) : aucune signature de copie.
- 7 entrées de fiche sur 46 sont identiques en entier d'une lecture à l'autre ; toutes les sept sont des entrées « sept
  oui cités », faites de citations de la fiche seulement, sans aucun texte libre.
- La preuve « mot pour mot » des « oui » de R7, refaite par [PC] sur les fiches réelles : 30 sur 30 à la première
  lecture, 28 sur 28 à la relecture, comme l'outil ([RC] `2_R7_preuve_refaite`).

**Ce qui a été servi** ([RC] `2_contexte_servi`, `1_code`). Aucun des 18 messages n'est identique d'une lecture à l'autre ;
consigne, question, faits et catalogue ont la même empreinte dans [M1] et [M2]. Message par message
(`messages_servis`) : la partie qui précède les fiches (consigne, pièces, ligne du lot) est identique 18 fois sur 18 ;
mêmes étiquettes dans le même ordre, 18 sur 18 ; les fiches réelles servies sont identiques, étiquette et texte, 46 sur
46 ; les fiches témoins diffèrent 40 fois sur 40. **Seuls les témoins voisins ont changé.**

## 3. R7 fiche par fiche (23 fiches réelles)

Valeurs comptées après la preuve, dans l'ordre « première L1, première L2, relecture L1, relecture L2 » ([RC]
`2_R7_fiches_reelles`, sur [V1], [V2]) :

| Motif | Fiches | Retenu première | Retenu relecture |
|---|---|---|---|
| 1 1 1 1 | 13 | 1 | 1 |
| 0 0 0 0 | 6 | 0 | 0 |
| 0 1 0 0 | 2 | 0 | 0 |
| 0 1 0 1 | 1 | 0 | 0 |
| 1 0 1 0 | 1 | 0 | 0 |

- **Entre les deux passages d'une même lecture** : 4 désaccords sur 23 à la première lecture (accord corrigé du hasard,
  kappa de Cohen : 0,62) ; 2 sur 23 à la relecture (0,82).
- **Même passage, d'une lecture à l'autre** : L1, 0 changement sur 23 ; L2, 2 changements sur 23, tous deux de 1 vers 0.
  Soit **2 valeurs de passage changées sur 46**. Les deux tombent sur des fiches où L1 vaut 0 dans les deux lectures :
  le « et » rend 0 avant comme après. Sans le « et », l'accord entre lectures serait de 44 sur 46, pas parfait.
- Les 13 fiches au retenu 1 sont exactement les 13 fiches unanimes à « oui » sur les quatre passages ; les 4 fiches
  disputées (17 %) sont toutes au retenu 0 dans les deux lectures.
- Le retenu recalculé égale celui de [C1] et de [C2] ; l'accord 23 sur 23 du rapport du lecteur est confirmé.

**Remarque sur les chiffres rapprochés par le lecteur** ([RL] § 3.2). Le 0,62 est l'accord entre passages de la première
lecture sur les 23 fiches réelles ([RG] § 2, ligne 50 ; recalculé ici : 0,6198). Le 0,72 est celui de la relecture sur la
pile entière de 43 fiches ([C2] `L4` : 0,721 ; la première lecture y vaut 0,763, [C1] `L4`). À base égale, les 23 fiches
réelles : 0,62 puis 0,82. Et le 1,0 qu'il leur oppose porte sur des valeurs **retenues**, pas sur des valeurs de passage.

**Les autres critères, mêmes fiches** ([RC] `2_tous_criteres_fiches_reelles`) — R7 n'a rien de singulier :

| Critère | Valeurs de passage changées, même passage, entre lectures | Retenu changé entre lectures |
|---|---|---|
| R1, R2 | 0 sur 46 chacun (tout à « oui ») | 0 sur 23 |
| R3 | 1 sur 46 | 0 sur 23 (changement masqué par le « et », comme pour R7) |
| R4 (7 fiches lues par le lecteur ; les 16 autres valent 1 par programme) | 1 sur 14 | 1 sur 7 |
| R5 | 4 sur 46 | 2 sur 23 |
| R6 | 3 sur 46 | 2 sur 23 |
| **R7** | **2 sur 46** | **0 sur 23** |

R1 à R6 ensemble : 9 valeurs changées sur 244 (3,7 %) ; critères non constants seuls (R3 à R6) : 9 sur 152 (5,9 %).

## 4. Probabilité d'un accord parfait du retenu sur 23 fiches

Tout ce paragraphe : [RC] `3_probabilites` ; formules dans [PC] (fonctions `modele_classes_latentes`,
`modele_beta_binomial`, `modele_contexte_fixe`). Calculs exacts, sans tirage.

**Lecture A — « les deux passages sont deux tirages échangeables ».** On prend le désaccord entre passages de la première
lecture pour du bruit de rejeu, on ajuste un modèle sur cette seule lecture, et on prédit, fiche par fiche selon son
motif (13 « deux oui », 4 « un seul oui », 6 « aucun oui »), que le retenu se répète :

| Modèle | Ajusté sur | Probabilité d'un accord parfait |
|---|---|---|
| Deux classes de fiches, erreur indépendante par passage | 23 réelles | 0,0020 |
| idem | pile de 43 | 0,026 |
| Probabilité de « oui » propre à chaque fiche (loi bêta) | 23 réelles | 0,017 |
| idem | pile de 43 | 0,034 |

Sous cette lecture, l'accord parfait serait bien suspect : l'étonnement du lecteur est fondé **si** l'on tient L1 et L2
pour deux rejeux.

**Lecture B — « chaque passage est une place fixe, rejouée à l'identique ».** C'est le montage réel, déclaré par la règle
([RG] § 1, ligne 37 : « chaque fiche réelle garde l'étiquette et le lot de la première lecture » ; § 9 point 3) et
vérifié ici ([RC] `2_contexte_servi`, sur [K1], [K2], [I1], [I2], [M1], [M2]) : dans chaque passage, les 23 fiches
réelles ont la même étiquette, le même lot et le même rang aux deux lectures (23 sur 23, trois fois) ; mêmes graines
d'ordre ; même texte servi. À l'inverse, **aucune** des 23 fiches n'a la même étiquette en L1 et en L2. L1 et L2 diffèrent
donc par le rang, le lot et les voisines ; première lecture et relecture ne diffèrent, pour un passage donné, que par les
témoins voisins réécrits (§ 2, `messages_servis`) et par le hasard du lecteur. Le désaccord entre passages (17 %) mêle
donc le bruit d'un rejeu et un éventuel effet de place ; le bruit d'un rejeu seul se lit sur « même passage, entre
lectures ».

Si r est la probabilité qu'une valeur de passage change au rejeu, le retenu se répète sur les 23 fiches avec la
probabilité (1 − r)^26 × (1 − r(1 − r))^4 × (1 − r²)^6 :

| r | D'où vient r | Probabilité d'un accord parfait du retenu |
|---|---|---|
| 3,7 % | R1 à R6, même passage entre lectures (9 sur 244) — sans R7 | **0,32** |
| 5,9 % | R3 à R6, critères non constants (9 sur 152) — sans R7 | **0,16** |
| 4,3 % | R7 lui-même (2 sur 46) — circulaire, pour mémoire | 0,26 |
| 17,4 % | désaccord entre passages pris pour du bruit (lecture A) | 0,003 |

L'accord parfait garde une probabilité d'au moins 0,05 tant que r ≤ 9,5 %, et d'au moins 0,50 tant que r ≤ 2,3 %.
Sans le « et », la probabilité que les 46 valeurs de passage se répètent toutes serait de 0,18 (r = 3,7 %) ou 0,06
(r = 5,9 %) — et de fait elles ne se sont pas toutes répétées.

**Lecture retenue.** La relecture étant établie par les appels (§ 2), l'accord parfait s'explique par trois faits qui se
cumulent : places inchangées (rejeu à contexte presque fixe, changement d'environ 4 % par valeur), 19 fiches sur 23
stables sur les quatre passages, et un « et » qui absorbe les deux changements survenus. Une chance sur trois à une
chance sur six : ordinaire.

**Limites de ce calcul.** (a) 23 fiches : les données ne suffisent pas, sur R7 seul, à départager « effet de place » et
« chance » (2 changements sur 46 à place fixe, contre 6 désaccords sur 46 entre places différentes) ; l'explication tient
au montage déclaré et aux appels vérifiés, pas à un test. (b) Les changements ne sont pas indépendants entre passages :
sur R5, deux fiches changent dans les deux passages à la fois d'une lecture à l'autre (4 changements sur 46, aucun
désaccord entre passages) ; la formule donne un ordre de grandeur. (c) Le taux r des autres critères n'est pas celui de
R7 ; la borne r ≤ 9,5 % laisse de la marge.

## 5. Voies de reprise cherchées dans l'outil : aucune

Lu dans [OL] et [CL] ; comptes dans [RC] `1_code`.

1. **Reprise après « pause »** ([OL], `envoyer`, ligne 1048). À chaque lancement, l'outil relit son propre journal chaîné
   et n'envoie que les lots sans clôture (`a_faire`, ligne 1065). Une reprise **continue** les envois ; elle ne remplace
   jamais un appel par un fichier. Un appel resté sans clôture, une anomalie ou un arrêt consignés font refuser tout
   envoi (« aucune reprise »).
2. **Dossier et noms.** Un seul dossier accepté, `P2/envois` (`racine_du_dossier`) ; `preparer` refuse un dossier non vide
   (ligne 602) ; réponses, erreurs et relevés s'écrivent par `ecrire_scelle_octets` (ligne 248), qui refuse d'écraser ;
   le journal ne s'écrit qu'en ajout, chaque ligne portant l'empreinte de la précédente ; les réponses s'appellent
   `reponse-…-v3-2.json` (les 18 noms attendus du manifeste [M2] portent ce suffixe).
3. **Vérification** ([OL], `verifier_lecture`, ligne 1343). Seuls sont lus les fichiers `reponse-L-lotk-v3-2.json` du
   dossier, chacun rattaché à une clôture chaînée du journal par son nom, son empreinte et le statut 200 ; une réponse
   étrangère au journal est refusée (`controler_coherence`).
4. **Ce que l'outil lit de la première lecture.** Trois lignes de [OL] nomment `P1/` : manifeste, journal et relevé
   épinglés (`PREMIERE_LECTURE`), lus par `verifier_premiere_lecture` et `verifier_unicite` pour l'intégrité et pour la
   dépense déjà faite. **Aucune ligne ne nomme une réponse de la première lecture** (0). [CL] ne nomme `P1/` qu'une fois :
   le classement [C1], pour les deux descriptifs (§ 1).
5. **Cache.** Aucun cache de réponses dans [OL] : le mot n'y désigne que le prix et le compte des jetons d'entrée en
   cache chez le fournisseur. Le transport est un seul envoi, sans reprise ni redirection (`transport_reel`, ligne 750) ;
   les corps portent `store: false` ; jetons lus en cache : 0 (§ 2).
6. **Version jouée.** Le manifeste [M2] porte la version v3.2.1 et l'empreinte de [OL] (égalité vérifiée) ; [C2] porte la
   version v3.2.1 du classement. De la v3.2 à la v3.2.1, seuls changent les pièces épinglées et le nom de version. De la
   v3.1 à la v3.2.1, le dernier bloc changé est la garde du dossier unique et de la dépense déjà faite (ligne 552 de
   [OL]) : `envoyer`, le transport, le journal et la vérification sont identiques, ligne pour ligne, à ceux qui ont servi
   à la première lecture (différentiel refait par moi sur les deux fichiers : conforme à [D], `54d735bd`).
7. **Hors de ma portée.** Je n'ai fait aucun appel : ce que le fournisseur a calculé n'est pas vérifiable ici. La réserve
   déclarée par [CE] § 4 (« reprise invisible d'un envoi par le mandataire ») produirait un appel en double pour un même
   lot, pas une réponse de la première lecture ; identifiants et horodatages l'écartent pour la question posée.

## 6. Ce que cet accord ne dit pas

- **Pas une preuve de fiabilité de R7.** Même lecteur, même consigne, même place : l'accord entre lectures mesure la
  répétabilité à position fixe. Une erreur systématique du lecteur se répète ; ses écarts sur les témoins ([RL] § 2 et
  § 3.2) restent entiers. Le rapport du lecteur le disait déjà ; cet audit le confirme et en donne la cause.
- **Le « et » rend le retenu plus stable que ce qu'il résume.** Toute fiche disputée va à 0 et y reste ; le retenu 1 est
  la classe « oui aux quatre passages ». Un accord sur le retenu surestime l'accord sur les réponses.
- **L'effet de place n'est pas mesuré.** Ordres et lots n'ayant pas été retirés au sort, on ne sait pas ce que vaudrait R7
  à une autre place ; le désaccord entre L1 et L2 (4 puis 2 sur 23) en est le seul aperçu.
- **Remarque de méthode, sans décision** (rejoint [RL] § 5, point 5) : une lecture qui voudrait mesurer la répétabilité
  retirerait ordres et lots au sort entre lectures, et rapporterait l'accord des valeurs de passage à côté de celui du
  retenu. Ouvrir une telle lecture reste une décision de Lazar.

**Limites de l'audit.** Je n'ai pas rejoué le programme de classement lui-même : j'ai recalculé à part le « et », les
valeurs de R7 depuis les réponses brutes et la preuve des « oui » de R7 sur les fiches réelles. Je n'ai lu ni les fiches
sous `runs/`, ni les essais et mutations de l'outil. Les probabilités reposent sur 23 fiches et sur des modèles simples.

## 7. Refaire les calculs

Depuis la racine du dépôt, sans réseau ni clé :

`.venv/bin/python -I -B docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/audit-r7-trop-propre-v1-outils/calculs_audit_r7_v2.py --racine .`

La sortie affichée doit être identique, octet pour octet, à [RC] (rejeu fait : identique). Avec `--sortie FICHIER`, le
programme écrit le résultat et refuse d'écraser (essayé avec la v1 sur un fichier neuf : code 0 ; sur le fichier
existant : refus, code 2). Il s'arrête si une pièce diffère de son compagnon.
