# Contre-lecture (R2) — conception v4 du monde riche (famille MR-2, règle de garde) — v2

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), lecteur neuf, autre modèle que le concepteur (Claude Opus 5.5). Je
  n'ai écrit ni la conception, ni le code, ni le préenregistrement, ni la note de décision.
- **Heures** (relevées par `date -u`) : début 2026-11-13 09:21:16 UTC ; fin de rédaction 2026-11-13 09:36:45 UTC ; v2 écrite à 2026-11-13 09:36:56 UTC.
- **v2** : v1 (`ebeeb41b1347048a24a5f9ae6878cae340522fc45cf8b08a38920a2432b886ed`, gardée, R12) recopiée à l'identique, sauf l'heure de fin : la v1 portait « 09:40 », heure estimée et non relevée (interdit 7) ; l'heure relevée est 09:36:45. Aucun autre changement.
- **Interdits** : `interdits-communs-v2.md` lu en entier avant tout ; aucun chemin interdit ouvert ni listé ; aucune clé lue ;
  aucune écriture git (deux lectures `git log` seulement) ; aucun appel, aucune dépense ; aucun refus rencontré. Calculs : un
  processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`.

## Verdict (une ligne)

**Portable dans le préenregistrement après corrections (9 exigées) ; pas telle quelle** : la famille MR-2 est un dessin
honnête et reproductible qui ne règle aucun signe, mais la règle de garde, telle qu'elle est rendue opératoire, ne garde
pas du risque réel — son issue est presque une fonction de la seule probabilité « 0,02 », posée sans pièce à une valeur
voisine du point de bascule (≈ 0,03) ; je recommande le pilote avec les vrais proposeurs avant la course (Q-14 (b)).

## Pièces lues et vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` | égale au compagnon |
| `outils-v4/monde_riche_v4.py` | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` | égale au compagnon ; lu en entier |
| `outils-v4/lancer_sorties_v4.sh`, `table_v4.py`, `devis_multi_generations_v4.py` | compagnons | égales ; lus en entier |
| `sorties-v4/` (12 parties, résumé, table, devis, journal ; 31 fichiers) | compagnons | toutes égales ; `script_sha256` de chaque partie = `4b165847…` |
| `outils-v2/devis_multi_generations_v2.py` (formule), `outils-v1` et `outils-v2` (attribution, C5, C6, bruitage, vérificateur v2 : extraits) | — | lus |
| conception v3 (§1.2 à §1.5, §5, §6), brouillon 3 (§2, §3.5 à §3.7, §8, §10), note de décision `d2bcf581…` | — | lus |
| `registres/decisions.md` (R-2482, R-2485, R-2492, R-2500), `registres/go.md` (GO-2026-11-13-01 et -02) | registres vivants | lus |

**Rejeux** (au brouillon de session, rien écrit dans le dépôt hors de ce fichier) :
- monde 3, commande scellée telle quelle (09:25:05 → 09:29:15 UTC) : champ `resultat` **identique** à
  `sorties-v4/partie-v4-monde-3.json` ;
- monde 9, module scellé importé sans modification, avec relevé des ensembles proposés et des survies (aucun tirage ajouté
  ni retiré ; 09:29:30 → 09:34:23 UTC) : champ `resultat` **identique** à `sorties-v4/partie-v4-monde-9.json`. Le relevé
  confirme que le code fait ce que le texte dit : en génération 1 avec masquage, la conditionnelle E7 (condition E4) est
  proposée dans 2 cartes sur 24 (cartes 3 et 19, toutes deux retenues) alors que E4 n'est pas encore connue ; sans masquage,
  dans 7 cartes sur 24.

**Chiffres recomptés** : 8 sur 12 et 0 sur 12 ; Wilson de 8 sur 12 = [0,391 ; 0,862] ; 8 conditionnelles et 2 moyennes
restantes ; 7 mondes sur 12 gardent une conditionnelle ; médianes des parts marginales 0,0195 (14) et 0,47 (18) ; 204
retenues, 36 fausses ; 1 − 0,98²⁴ = 0,384 ; devis 363,00 ; 34,20 + 12,00 + 10 = 56,20 ; central 41,11 (27,96 ; 7,15 ; 6,00).
Tous justes.

## Corrections exigées

**E-1 — Dire le point de bascule de la règle et ce qu'elle mesure vraiment.** Sous le modèle déclaré, un monde « garde »
surtout quand aucune des 24 cartes de la génération 1 ne porte la conditionnelle : probabilité (1 − p)²⁴. Calcul (le mien,
approché : sans les chaînes ni les moyennes manquées par hasard ; cohérent avec le 8 sur 12 observé) :

| p de la conditionnelle cachée | part attendue des mondes qui gardent | règle tenue sur 12 mondes | sur 24 |
|---|---|---|---|
| 0,01 | 0,79 | 0,99 | 1,00 |
| **0,02 (posée)** | **0,62** | **0,87** | **0,91** |
| 0,0285 | 0,50 | 0,61 | 0,58 |
| 0,03 | 0,48 | 0,56 | 0,51 |
| 0,04 | 0,38 | 0,27 | 0,15 |
| 0,05 | 0,29 | 0,11 | 0,03 |
| 0,25 (sans masquage) | 0,00 | 0,00 | 0,00 |

Trois choses à écrire au texte : (i) la règle bascule vers **p ≈ 0,03** ; la valeur posée (0,02, sans pièce) est à un
facteur 1,5 du point de bascule ; (ii) au banc, avec le modèle gelé, la règle tient avec une probabilité d'environ 0,9 quel
que soit le tirage du secret : le banc **ne mesure que les mondes**, rien sur les proposeurs ; c'est une vérification que
la famille n'est pas vide sous le modèle favorable, pas une garde contre le cas « vrais proposeurs sans masquage » ;
(iii) le 0,25 « une fois la condition connue » est tout aussi estimé que le 0,02. Le §3.3 dit la dépendance ; il ne dit pas
qu'elle est à ce point proche du seuil.

**E-2 — Dire que MR-2 ne satisfait pas la lettre de Q-13 (c).** La note parlait de « composantes moyennes que la
génération 1 **ne peut pas** capter seule ». MR-2 rend la composante invisible dans la marginale de son trait ; rien
n'empêche une carte de la porter en génération 1 (la première conditionnelle y est captée dans 6 mondes sur 12 même avec
masquage). La dépendance à l'archive est logée **dans le comportement des proposeurs**, pas dans le monde ni dans le juge
(C5 et C6 tiennent « K1 + conditionnelle » pour une vraie dès la génération 1). À écrire en clair dans le §2.1 et au
préenregistrement ; et dire au §2.3 qu'une dépendance **du côté du juge** (composante dont le gain au-delà de l'archive
n'excède le seuil qu'une fois une autre captée, comme les faibles de MR-1) n'a pas été examinée.

**E-3 — Contradiction sur ce qui est servi aux proposeurs.** Le §6 (ligne « §3.6 ») fait dire au gabarit servi
« l'existence possible d'une condition sur le signe d'un trait » ; le brouillon 3 (§3.5) et la v3 (K-5) gèlent « aucune
description des sortes d'effets du monde (seulement la grammaire) », pour ne pas souffler la structure. La grammaire permet
déjà cette forme (§2.1 : « aucune sorte neuve dans la grammaire servie »). Publier le générateur (Q-10 (a)) n'oblige pas à le
dire dans la consigne. Ce choix déplace directement la probabilité « cachée » : il doit être tranché et écrit **avant**
toute mesure (banc ou pilote). Ma lecture : ne rien dire (K-5 tient) ; seule la profondeur d'arbre à 3 conditions est à
ouvrir au gardien.

**E-4 — Q-14 est un nœud, sans défaut à 48 heures.** Le défaut « (a) » engage jusqu'à 419,20 USD sur le silence, alors que
la condition de GO-2026-11-13-01 (« règle écrite d'avance ») ne tient que sous une hypothèse non mesurée : c'est la lecture
d'une condition de GO et une dépense (hiérarchie de décision). L'option (c) n'est pas une vraie option (elle échoue par
construction : « sans masquage », une conditionnelle se comporte comme une moyenne de MR-1) : la retirer ou le dire.

**E-5 — Essais R5 du vérificateur et du générateur v4 absents.** La règle neuve « toute conditionnelle certifiée, sinon
refus » n'a jamais tiré (0 refus C8 sur 24 tirages) : elle n'est éprouvée sur aucun artefact. Avant le gel : cas sain et
artefact pour (i) conditionnelle non certifiée → refus C8 ; (ii) plus de 3 conditions de seuil, plus de 48 feuilles, plus de
10 composantes, moins de 2 leurres → refus ; (iii) égalité de `compiler_v4` avec la grammaire de référence sur un monde à
conditionnelle chaînée. Le code v68 doit porter la sorte sous des noms neufs (R12), non par remplacement à l'exécution de
trois fonctions scellées.

**E-6 — Cause des refus C6 à établir avant le gel du générateur.** 8 refus C6 sur 24 tirages (un tiers), « cause non
établie ». C6 exige que l'attribution retrouve exactement les effets de chaque « K1 + un effet ». Si l'écart vient des
« K1 + conditionnelle » (soupçon du concepteur), soit le contrôle est mal posé pour la sorte neuve, soit il sélectionne
les mondes d'une façon non déclarée. Relire les motifs (calcul seul), l'écrire, et déclarer la sélection. Même demande,
plus légère, pour les 3 refus C0 (motif non relu dans les parties).

**E-7 — Dire ce qu'a été « l'essai à blanc du bac à sable » (§4.1) et la force réelle de « scellé avant toute partie ».**
Un essai avant le scellement est cité sans graine, sans sortie, sans dire ce qui en a été lu. Par ailleurs l'antériorité
du scellement repose sur l'heure du compagnon (08:02:15), sur l'empreinte portée par chaque sortie (solide : le code qui a
tourné est le code scellé) et sur une première ligne de journal **que le lanceur scellé n'écrit pas** (écrite à part) ; le
tout n'a été versé qu'en un seul commit à 09:20:57 (`2338b372`). Rien ne contredit « premier et seul passage » ; rien ne le
prouve hors la parole du concepteur. À dire au texte ; et pour le banc : code, modèle de proposeurs et règle **versés et
poussés avant** l'engagement du secret de calibration.

**E-8 — Définitions de la règle à fermer pour le banc.** (i) Nombre de mondes de calibration **fixé** (12 ou 24, Q-15), pas
« au moins 12 » ; (ii) dénominateur = tous les mondes tirés, un monde sans tirage conforme en 8 comptant comme ne gardant
rien (le concepteur le propose : le retenir, et le coder, le code scellé comptant aujourd'hui sur les seuls conformes) ;
(iii) rapporter à côté du compte de la règle le compte **restreint aux conditionnelles** (ici 7 sur 12) : dans le monde 0 la
règle n'est tenue que par une moyenne ordinaire manquée par le hasard du flux, « connue » mais non « captée » — ce n'est pas
la capacité que la famille revue devait créer ; (iv) le banc refait la variante sans masquage et la table de E-1.

**E-9 — Lecture de l'issue P sous MR-2.** Sous masquage, P devient presque mécanique (8 mondes sur 12) ; hors masquage,
PL-épuisé. Le préenregistrement doit écrire d'avance : (i) P sur une conditionnelle **n'établit pas** que l'archive a causé
la découverte (une seconde génération est aussi un second tirage) ; rapporter, pour chaque conditionnelle captée, si sa
composante de condition était dans l'archive servie au début de la génération, et la part des cartes qui la portent avant
et après (le §6 le prévoit : le rendre obligatoire) ; (ii) la génération 3 n'a de quoi répondre que dans les mondes à chaîne
(2 sur 12 ici) : avec deux mondes de test, la chance qu'un au moins en porte une est d'environ 0,3 ; (iii) la tolérance τ des
fausses découvertes est à refaire sur MR-2 (17,6 % ici contre 15,5 % en v3b).

## Corrections suggérées

- **S-1** La part marginale ne mesure que la correction **linéaire** sans condition sur z_t. Le mélange des deux branches
  laisse un effet pair en z_t (second ordre), qu'un seuil sur z_t peut prendre en partie. Ajouter la borne plus large :
  part de I_i rendue par la meilleure loi qui ignore le signe de z_B (par exemple le mélange des deux branches).
- **S-2** Exiger une chaîne (deux conditionnelles) dans chaque monde, si le gabarit le permet sous 10 composantes et
  3 conditions : la génération 3 aurait de quoi répondre partout. Changement de famille : à proposer à Lazar, pas à faire
  seul.
- **S-3** Monde 10 : 2, 1 et 1 retenues seulement (contre 5 à 13 ailleurs) ; c'est le seul progrès en génération 3. À
  regarder (regroupement très serré ou juge sourd) avant de s'appuyer dessus.
- **S-4** Le lanceur devrait écrire lui-même la ligne de début et l'empreinte du script ; `table_v4.py` (écrit à 08:09:53,
  après la sortie du monde 0) et le script de devis ont été scellés après leurs sorties : sans effet (lecture seule), à dire.
- **S-5** Le §5 devrait dire que le jeu planté compte **une** « K1 + un effet » par conditionnelle (et non deux, la
  conditionnelle étant développée en deux effets à la compilation) : c'est ce qui tient T_pire = 37.
- **S-6** Le modèle de proposeurs remplit toutes les cartes de la génération 2 de presque toutes les composantes (relevé du
  monde 9) : dire que les 8,58 retenues de la génération 2 sont un trait du modèle, pas une prédiction.

## Réponses aux six questions

**1. MR-2 répond-elle à Q-13 (c) sans rien régler sur un signe (R3) ?** Sur R3 : **oui, sous la réserve E-7**. La question
du progrès est une question ouverte à lectures gelées (brouillon 3, §2 (d)), pas une hypothèse affirmée ; la famille change
la capacité du dessin, et chaque scénario a sa lecture écrite (masquage vrai → P ; faux → PL-épuisé ; conditionnelles jamais
proposées → PL-proposeurs). Exiger des conditionnelles certifiées est une sélection de capacité, déclarée. Sur la réponse
à Q-13 (c) : **en partie seulement** (E-2). La composante est invisible marginalement (fait mesuré, sans modèle : 2 % en
médiane contre 47 %), mais « la génération 1 ne peut pas la capter seule » n'est pas tenu par construction.

**2. Règle de garde.** Écrite d'avance : **oui** (texte de Lazar recopié, définitions dans le code scellé, un passage,
variante sans masquage rapportée spontanément). Mesurée honnêtement : **oui**, et la dépendance au masquage est dite sans
détour (§0 ligne 7, §3.3, §4.2, Q-14, réserves, R-2500). Ce qui manque : la proximité du point de bascule et le fait que le
banc ne mesure rien sur les proposeurs (E-1). **Ce que vaut la conception** : elle vaut comme **dessin qui rend la question
posable et l'hypothèse mesurable**, pas comme assurance que la course répondra. Son seul fait solide est structurel (part
marginale). Tout le reste — 8 sur 12, progrès dans 8 mondes — est la conséquence arithmétique de deux nombres posés (0,02
et 0,25). L'hypothèse est plausible dans son sens (rien dans l'archive de départ ne désigne z_B), incertaine dans sa
taille, et fragile : il suffit que les vrais proposeurs essaient des conditions de signe sur plus de 3 cartes sur 100 pour
que la règle ne tienne plus. La course resterait lisible dans tous les cas, mais sa dépense ne serait justifiée, pour le
progrès, que par une supposition.

**3. Code, vérificateur, scellement, reproductibilité.** Code lu en entier : conforme au texte (masquage jugé sur les
composantes des cartes retenues ; K1 est une forte, jamais la condition ; seconde conditionnelle chaînée sur la première ;
priorité des opérateurs des lignes 292-293 correcte ; compte de la règle sur les conformes, dit). **Deux parties rejouées,
résultats identiques** (mondes 3 et 9). Empreintes toutes égales à leurs compagnons. Faiblesses : E-5 (aucun essai R5 des
règles neuves), E-6 (C6), E-7 (antériorité prouvée par l'horodatage seul, essai à blanc non décrit).

**4. Devis.** **Juste** : par génération et par monde, Claude 5 + 37 × 1,50 = 60,50, soit 363,00 sur six ; Argon
2 + 37 × 0,10 = 5,70, soit 34,20 ; Astra 12,00 ; machine 10 ; 56,20. T_pire = 37 tient avec au plus 10 composantes (au plus
9 « K1 + un effet », S-5) ; m = 48 est cohérent avec ce décompte. Central recalculé : 41,11. **Marges** : suffisantes
**comme bornes de formule**, parce que tout est tenu par des coupures dans le code (plafonds de session, borne par test,
plafond de chaque relais, garde 29, « aucune reprise ») : le pire ne peut pas être dépassé, il peut seulement arrêter la
course. Elles ne laissent **aucune** place à un imprévu : une seule session rejouée (2 à 3 USD) ou un prix d'Argon ou
d'Astra autre que le prix supposé mange la marge ; le concepteur le dit (« marges minces »). Le central (≈ 41 USD) est neuf
fois sous le plafond : le risque réel est l'arrêt, non le dépassement.

**5. Q-14 et Q-15.** **Q-14** : bien posée sur le fond, mal classée (E-4 : nœud, pas de défaut ; option (c) factice).
**Ma recommandation : (b), le pilote avec les vrais proposeurs avant la course, confiance 0,6.** Raisons : (i) l'hypothèse
porte tout le gain et sa valeur posée est au bord de la bascule (E-1) ; (ii) le pilote la mesure bien mieux que le banc :
2 mondes de calibration, 48 cartes ; à p = 0,02 on attend 1 carte portant la conditionnelle avant sa condition (0 ou 1 dans
75 % des cas), à 0,10 environ 5, à 0,25 douze (5 ou plus : probabilité 0,003 à p = 0,02, 0,53 à 0,10, 0,997 à 0,25) ;
(iii) coût au pire 18 USD (9 par monde, proposeurs seuls, juge mécanique gratuit) contre 419 engagés ; (iv) il consomme des
mondes de calibration, pas de test, et réemploie le début de la chaîne v68, qu'il faut écrire de toute façon ; (v) il donne
enfin une pièce au modèle de proposeurs (0,5 ; 0,25 ; 0,1 ; 0,02 : tous estimés). Conditions : texte court contre-lu et
scellé avant (R1), avec la règle de lecture écrite d'avance (par exemple : au plus 1 carte sur 48 → masquage compatible,
course ; 5 ou plus → masquage réfuté, pas de course sur MR-2 ; entre les deux → à Lazar), E-3 tranché avant, ligne de GO à
part. **Si l'échéance du 30 novembre ne laisse pas la place** : (a), mais alors avec E-1, E-2 et E-9 portées au texte et la
phrase « la question du progrès n'est posable que si les vrais proposeurs masquent » en tête du préenregistrement.
**Q-15** : bien posée ; **(b), 24 mondes**, d'accord (calcul seul) ; mais 24 mondes n'ôtent que le hasard des mondes : sous
le modèle gelé la règle tient neuf fois sur dix dans les deux cas (E-1). Fixer N avant l'engagement du secret (E-8).

**6. Prête à porter dans le préenregistrement ?** **Pas telle quelle ; oui après E-1 à E-9.** E-3 et E-4 (ce qui est servi
aux proposeurs ; Q-14) demandent le mot de Lazar ; E-5, E-6, E-8 sont du calcul et du code sans dépense ; E-1, E-2, E-7,
E-9 sont du texte. Rien dans les chiffres rendus n'est faux ; ce qui manque est la mesure de ce que la règle ne garde pas.

## Réserves de cette contre-lecture

- Deux parties rejouées sur douze ; les dix autres sont vérifiées par leurs empreintes et par recomptage de la table.
- La table de E-1 est un calcul approché de ma main, non une simulation ; le banc doit la refaire avec le code gelé.
- Je n'ai pas lu le code v68 (non écrit), ni les sections du brouillon 3 hors de celles citées.
- Lecteur d'une autre lignée que le concepteur, mais de la même maison de modèles (Claude) : ce n'est pas un juge d'une
  autre famille.
