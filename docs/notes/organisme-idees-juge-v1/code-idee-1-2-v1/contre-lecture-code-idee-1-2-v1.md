# Contre-lecture du code qui jouera le préenregistrement de l'idée 1.2 — v1

- Auteur : contre-lecteur neuf, sous-agent de la session mère. Je n'ai écrit ni le préenregistrement (v1 à v4), ni ses
  relectures, ni le code, ni ses essais, ni le rapport du développeur, ni le juge.
- Date (UTC) : 2026-11-15, de 10:44 à 11:25 environ (`date -u`). Dépôt lu sur `main`, tête `e4411649`.
- Ce que je n'ai pas fait : **aucun jeu du préenregistrement**, aucune répétition miniature, **aucun tirage avec la
  racine du texte** (mes sondes emploient des racines d'essai, dont le programme vérifie qu'elles diffèrent de celle du
  texte) ; aucun commit, aucune poussée, aucun appel réseau ni payant ; rien écrit sous `diag/`, `donnees/`,
  `docs/verdicts/`, ni dans `docs/notes/organisme-idees-juge-v1/correction-poids-v1/` ; aucun fichier du dépôt modifié
  (mes mutations sont des greffons d'essai chargés en mémoire depuis le bloc-notes). Aucune garde ni aucun classifieur
  n'a refusé une de mes commandes.
- Notation : `<bloc-notes>` désigne le dossier de bloc-notes de la session mère ; mes programmes et leurs sorties sont
  dans `<bloc-notes>/cl/` et recopiés aux annexes A à C.
- Texte joué, ci-dessous **[T]**, lignes citées « l. n » : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`, compagnon conforme). Rapport du développeur,
  ci-dessous **[RD]** : `docs/notes/organisme-idees-juge-v1/code-idee-1-2-v1/rapport-developpeur-v1.md`
  (`774fbf78b1a2c3af52502a5a43ea330c9ad6f7a9998225dfbbf646e127784a66`, compagnon conforme). Registre : R-2886, R-2897.

## Verdict

**« Jouable après corrections ».** Le code joue bien le texte scellé : je n'ai trouvé **aucun écart de calcul** au banc
B v2, aux sept bras, à la valeur e, à l'oracle ni aux étages de lecture ; la valeur e est partout la richesse cumulée à
un temps d'arrêt ; le dénominateur est celui du juge réel, importé sous empreinte ; aucun chiffre de résultat n'est
affiché avant le scellement. Trois points sont à corriger avant le jeu, tous petits, tous hors du calcul :

- **Majeur 1** — la borne de 24 heures ne tient pas si un processus fils meurt : le parent reste bloqué sans fin, sans
  `arret.json` (démontré par une sonde).
- **Majeur 2** — l'essai du refus « préenregistrement non scellé » est vert pour une autre raison (c'est la garde de
  l'addendum qui lève) : R5 n'est pas tenue pour cette garde ; la garde elle-même est saine (sondée).
- **Majeur 3** — deux paramètres gelés du texte ne sont épinglés par aucun essai : deux de mes quatre mutations
  survivent aux 109 essais (intervalle à 90 % au lieu de 95 % ; seuil d'arrêt bas à 1/10 au lieu de 1/20). Le code est
  juste aujourd'hui ; ce sont les essais qui ne le garderaient pas.

Neuf mineurs. Écarts E-1 et E-2 du développeur : **sans effet sur le calcul, acceptables, à déclarer dans l'addendum**
(E-2 est une lecture du texte plutôt qu'un écart). Les dix-huit lectures du développeur sont **fidèles** (deux
remarques, sans correction exigée ; trois lectures de plus, non listées, à déclarer : mineur 6).

Comptes : six fichiers d'essais **109 sur 109** (413 s) ; essais d'infrastructure **30 sur 30** ; mutations du
contre-lecteur : **2 tuées, 2 survivantes** (dont une des trois demandées).

## Pièces vérifiées

- Les 18 fichiers du code et des essais : `python -m controle_ia.scellement verifier` rend « OK » pour chacun ; leurs
  18 empreintes sont celles du tableau de [RD] (liste recalculée : `ec882953493ab6796a9e3910edf580972f1ef0749b56e017c7ce3b6856aa0a2c`).
- Copie du juge `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` : `sha256sum -c
  empreintes-copie-v1.txt` conforme pour ses 53 fichiers ; la liste vaut `0153e02d4522fe21eb1cf52985574eba38b5f260f7a3a08183d63589f29f32df`,
  comme son compagnon et comme [T] l. 44-45. **Aucun fichier compilé** (`__pycache__`, `.pyc`) sous la copie.
  Je n'ai exécuté aucun fichier de ce dossier.
- **Comment le module importe le juge** (`juge_v1.py`) : avant tout import, `verifier_copie` (l. 57-87) vérifie la
  liste (contre l'empreinte citée par [T] et contre son compagnon), puis chacun des dix modules chargés contre la
  liste, et les cinq fichiers que [T] cite par empreinte entière (l. 29-35 ; valeurs égales à [T] l. 45-50) ;
  `charger` (l. 101-126) interdit l'écriture de code compilé, refuse un paquet homonyme déjà chargé, importe, puis
  vérifie que **tout** module `pole.*` présent vient de la copie et figure parmi les empreintes vérifiées (un import
  transitif non prévu lève `GardeArret`). Aucun repli. L'essai `test_copie_du_juge_verifiee_et_artefact` couvre le
  cas sain et une copie altérée. Conforme.

## 1. Conformité au texte scellé

Lecture ligne à ligne de [T] contre le code. « ✓ » : conforme, vérifié par lecture ; les sondes sont en annexe.

| [T] | exigence | code | constat |
|---|---|---|---|
| l. 358-360 | K = 3, D = 2, G = 2 ; traits arrondis à six décimales ; softmax aléatoire N(0 ; 1,5²), N(0 ; 0,3²) | `banc` l. 137-140 ; `lois` l. 126-129 | ✓ |
| l. 362-364 | archive A2 : S1, S2, S3 = `si_sinon` sur {z_jA > s_A}, S4 sur {z_{1−jA} > s_B} ; coupures retirées tant que \|s\| < 0,3 | `banc` l. 82-91 ; `lois` l. 183-188 | ✓ |
| l. 370 | Q1 : `melange`([S1, S2, S3, S4, uniforme fixe], Dirichlet, arrondis, renormalisés) | `lois` l. 148-157 | ✓ |
| l. 377-381 | V1 à V5 (formes, conditions, trait de l'effet 1 − j ; V3 : seuil retiré tant que \|c − cut(j)\| < 0,3 ; V5 : coupure de l'archive) | `lois` l. 254-329, l. 191-196 | ✓ |
| l. 388-389 | deux doses les plus basses par type, dix cellules, cellule g mod 10 | `lois` l. 243-250 | ✓ (ordre des cellules : lecture 3) |
| l. 391-405 | famille T, 750 générations : 6 porteuses, 6 copies de la classe, 4 copies par morceaux, 6 fausses construites (cosinus de l. 399-400, plafond 1 000, repli signalé ; signe opposé × 1 et × 0,5 ; V4 : six sous la règle), 2 nulles | `banc` l. 49-54, l. 165-227 ; `lois` l. 106-113 | ✓ ; le cosinus est bien E[f·f′]/(E‖f‖²·E‖f′‖²)^½ avec f = p − S1, sur les instances de l'oracle ; acceptée dès que cosinus ≤ 0 |
| l. 407-423 | famille N, 500 générations : M₀ pour g < 250, M₀′ pour g ≥ 250 (base parmi S1 et S2) ; 8 voisines (0,05·Δ, une Δ par carte), 8 membres exacts (1 + 4 + 3), 8 autres (2 + 2 + 2 + 2) ; fausses : référence = composante de la cellule | `banc` l. 105-124, l. 230-276 | ✓ |
| l. 425-428 | plan de 800, entraînement sur 100, 800 issues fraîches, flux propre ; richesses calculées une fois par `evaluer_v2`, plan « ordre_naturel » ; bras rejoués sur ces trajectoires | `banc` l. 300-306, l. 389-450 ; `execution` l. 139-171 | ✓ |
| l. 451-456 | racine = entier de l'empreinte ; `SeedSequence(entropy=racine, spawn_key=…)` ; clés (f, g, 24), (f, g, 25), (f, g, i, 0), (f, g, i, 1), (f, g, i, 2), (f, g, 1001), (f, g, 1000), (f, g, 2000), (99, b), (97, g) ; famille 0 = N, 1 = T | `banc` l. 61-70, l. 46, l. 83, l. 107, l. 144, l. 191, l. 240, l. 370, l. 394, l. 351-352 ; `rejeu` l. 210-211, l. 297 ; `lire` l. 65 ; `synthetique` l. 59, l. 130 | ✓ **exactement comme écrit** ; clés de longueurs différentes, aucune collision |
| l. 285-291 | oracle : 20 000 instances et issues du monde, (f, g, 2000) ; nul v8 ajusté par les routines du juge à 20 000, marge comprise ; gain ; quatre classes ; **calculé et scellé avant le rejeu** | `banc` l. 143-149 ; `oracle` l. 48-79 ; `execution` l. 233-254 | ✓ ; `oracle.json` est scellé avant la phase « jeu », revérifié au départ et à la fin du rejeu ; chaque génération jouée porte son empreinte ; la lecture refuse un jeu rattaché à un autre oracle (`lire` l. 106) ; mineur 1 (borne triviale silencieuse) |
| l. 432 | F : 200 par carte, valeur e arrêtée à m/α, sinon W₂₀₀ | `rejeu` l. 130-133, l. 180-184, l. 225 | ✓ |
| l. 433 | F-arrêt : F plus arrêts bas et haut, sans réallocation | `rejeu` l. 140-141 | ✓ |
| l. 434-437 | A : par tours, chaque active reçoit un bloc dans l'ordre des positions décalé du numéro du tour, tant que le budget le permet, au-delà de 200 jusqu'à épuisement | `rejeu` l. 90-120, l. 144-145 | ✓ (troisième écriture : 0 écart sur 1 200 cas) |
| l. 438-440 | P : comme A jusqu'à 200 ou l'arrêt, puis au hasard (graine indépendante) parmi les ni arrêtées haut ni au plafond, arrêtées bas comprises | `rejeu` l. 148-154, l. 210-211, l. 218 | ✓ ; le hasard vient de (f, g, 1000) seulement |
| l. 441 | P′ : comme P, à tour de rôle sur l'ensemble élargi | `rejeu` l. 157-159 | ✓ (lecture 13) |
| l. 442-443 | F125 : 250 par carte, 6 000 | `rejeu` l. 30-32, l. 136-137 | ✓ |
| l. 444-445 | G : deux blocs par carte, puis chaque bloc à la plus grande log W courante parmi les ni arrêtées haut ni au plafond, jusqu'à B ; famille N seulement | `rejeu` l. 33-34, l. 162-171 | ✓ |
| l. 279-281 | « au plus B » ; F exactement B ; F125 6 000 | `rejeu` l. 66-77, l. 221-226 | ✓ : chaque bloc passe par `Budget.prendre`, puis deux recomptes |
| l. 282-284, l. 233-236 | promotion par `cycle.appliquer_multiplicite`, m_fixe = 24, α = 0,05 ; valeur e = trajectoire tronquée, arrêtée au premier instant ≥ m/α | `rejeu` l. 180-207, l. 231-239 | ✓ (section 3) |
| l. 325-327 | blocs de 25, plafond 800 ; arrêt bas log W < log(1/20) après au moins 50 tirages ; arrêt haut ≥ log(m/α) | `banc` l. 41-43 ; `rejeu` l. 27-28, l. 80-87 | ✓ dans le code ; **non épinglé par les essais** pour le seuil bas (majeur 3) |
| l. 299-305, l. 328-338 | quatre lectures de validité ; 13 et 39 sur 500 ; domination à chacun des 32 instants ; **49 intervalles** (7 + 6 × 7), borne basse > 1 ; par monde : rapporté, audit | `lire` l. 32-41, l. 117-192 | ✓ : 49 exigés quand N compte 500 générations ; la domination est recalculée par la lecture sur les 32 instants de chaque carte (révélés ou non) ; les six sortes sont celles de [T] l. 333-334 ; quantiles 2,5 % et 97,5 % (**non épinglés** : majeur 3) |
| l. 486-493 | étages 1, 1 bis, 2, 3, 4, 5 | `lire` l. 275-334 | ✓ **exclusifs et exhaustifs** : étage 1 rend la main (rien d'autre n'est lu) ; 1 bis ajoute la réserve ; étage 2 ferme les étages 3 et 4 ; étage 3 : `if / elif / elif / else` dans l'ordre nuisible, gain, pas de gain, non tranché, avec les inégalités de [T] l. 339-342 (< 0 ; > + 0,02 ; > 0, ≥ + 0,05, ≤ + 0,05 ; < + 0,02) ; étage 4 : quatre issues selon les deux bornes hautes (< 0 ; ≤ 0), lues seulement si « gain » ; étage 5 toujours rapporté |
| l. 257-267 | Q1 à Q9 | `lire` l. 337-368 | ✓ chiffre prédit et critère de réfutation de chaque ligne (Q3 : ≥ 0,05, borne basse > 0, dose haute ≥ 0,08, dose basse ≤ 0,05 ; Q7 : ≥ 25 % et perte ≤ 0,02 ; Q8 : classe d'oracle « porteuse » sous A ; Q9 : moyennes par bras ≤ 0,8) |
| l. 495-500 | audit de symétrie : éléments | `lire` l. 250-272, l. 371-386 | ✓ éléments fournis (« trop propre », « tout négatif », porteuses arrêtées bas, partiellement vraies promues, cellules) ; le code ne prononce rien, l'audit reste à écrire par le lecteur |
| l. 504-515 | liste d'arrêt | sections 4 et 6 | ✓ sauf la ligne « durée murale > 24 h » (majeur 1) |

Montage du juge comparé à `a_blanc_v59.juger_carte` (lu, non exécuté) : même bibliothèque (standard, marginale
d'entraînement, `membres_archive_v8(dict(archive), None, K, DIM)`), même `construire_engagement_v2`, instants
`instants_reguliers(800, 32)` = 25, 50, …, 800 ; l'engagement ne porte pas de « fractions » : le numérateur est la
vraisemblance de la carte, donc Λ = q/P* est bien le bon terme de comparaison de la lecture (2). La trajectoire lue est
celle que le juge arrondit à six décimales ; la tolérance 10⁻⁶ de la domination couvre l'arrondi.

## 2. Les dix-huit lectures du développeur

| n° | lecture | jugement |
|---|---|---|
| 1 | ordre des tirages dans chaque générateur | **fidèle** ; l'ordre « plan, entraînement, issues d'entraînement » est celui de [T] l. 452-453 |
| 2 | famille N : composante de la cellule tirée du générateur du monde, après ses paramètres | **fidèle** (le texte ne donne pas de clé propre ; aucune clé inventée) |
| 3 | cellules : V1 à V5, dose basse puis haute | **fidèle** ; la parité de la cellule donne la dose, ce que la lecture emploie (`dose_haute`) |
| 4 | « mélange des lois d'archive » = ligne Q1, uniforme fixe comprise | **fidèle** ; avec l'uniforme, la carte reste dans la classe du nul (mise en commun linéaire avec toute loi aveugle fixe) |
| 5 | lois construites, puissance et inclinaison arrondies à six décimales | **fidèle** (extension de l'arrondi des softmax aléatoires ; effet de l'ordre de 10⁻⁶) |
| 6 | direction bruitée ; pour V4, les neuf paramètres de la loi neuve | **fidèle** pour V1, V2, V3, V5 ; pour V4 c'est un **choix** que le texte ne fixe pas, raisonnable ; à dire dans l'addendum |
| 7 | doublon : champ « poids » seulement | **fidèle** à la lettre (« chaque poids des lois softmax de M ») |
| 8 | « tirée indépendamment » : tous les paramètres aléatoires du type ; V5 garde la coupure de l'archive | **fidèle** |
| 9 | copie « au signe d'un trait » : trait tiré uniforme | **fidèle** (comme la ligne Q4 du banc) |
| 10 | membres exacts de Q2 et de l'étage 1 : ceux de N **et** les copies de la classe de T | **fidèle** et du côté prudent (Q2 : « dans aucun bras ni aucune famille ») |
| 11 | oracle sans la marginale d'entraînement ; évaluateur vectorisé | **fidèle** : la marginale au maximum de vraisemblance, membre de la bibliothèque standard, domine toute marginale fixe ; égalité à 10⁻¹² éprouvée |
| 12 | issues par les fonctions du juge sur des uniformes numpy de la clé | **fidèle** |
| 13 | G : deux blocs sans condition, égalité à la plus petite position ; P : tirage parmi les éligibles rangées par position ; P′ : tours continués | **fidèle** ; remarque : la phase 2 de P′ repart au tour max(tour, 8), non au tour qui suit (mineur 6) |
| 14 | E1 : 24 cartes de T g = 0, 24 de N g = 0, deux de T g = 1 ; remplacement y → (y + 1) mod 3 | **fidèle** à la lettre (50 cartes, chaque sorte) ; remarque : aucune de ces cartes n'est jugée dans un monde M₀′ ni dans une cellule V2 à V5 (mineur 7) |
| 15 | percentile : quantiles 2,5 % et 97,5 %, même rééchantillon pour un même ensemble | **fidèle** |
| 16 | hors de la zone utile : étages 3 et 4 non lus | **fidèle** (« rien ne se lit sur la principale ») |
| 17 | deux processus de calcul, le parent attend | **fidèle** ; une file de calcul par processus (variables d'environnement posées avant l'import de numpy) |
| 18 | banc de mutations sur racine d'essai, sauf le jeu synthétique | **fidèle**, et prudent : aucune génération du banc n'est touchée avec la racine du texte avant l'oracle |

**E-1 (lieu du code).** Aucun calcul ne change ; seule la traçabilité est en jeu, et elle est tenue par les empreintes.
Acceptable si l'addendum déclare le lieu et liste les 18 fichiers. Je recommande que l'addendum liste aussi les modules
d'infrastructure que ce code importe (mineur 8).

**E-2 (monde jouet tiré par génération).** [T] l. 309-312 dit « construit comme l'essai » et « graines (97, g) » ; le
programme `01c648a0…` (relu : lois tirées une fois, d'une racine à lui) ne peut pas être suivi à la lettre sans une clé
que le texte ne donne pas. Tirer les lois **et** les issues de (97, g) est la lecture la plus proche du texte. J'ai
comparé les deux écritures ligne à ligne : mêmes lois, même maximum de vraisemblance par bissection, même plancher par
la loi du monde, même plafond de log e à 50. Le risque est du côté sûr (si la mutation survivait avec la racine du
texte, le lanceur dirait « pas de jeu »). **Je le tiens pour une lecture, acceptable, à déclarer dans l'addendum**
(option (a) du développeur). Non éprouvé par moi avec la racine du texte (interdit par ma consigne) : la marge avec
la racine d'essai est large (borne basse 2,364 contre 1, [RD]).

## 3. Validité

- **La valeur e est la richesse cumulée à un temps d'arrêt, jamais un maximum.** `rejeu.log_valeur_e` (l. 180-184)
  rend la première valeur révélée ≥ log(m/α), sinon la dernière révélée ; `jouer_bras` (l. 231-239) la recoupe avec la
  valeur e que le juge lit lui-même (`appliquer_multiplicite`, champ `log_e`) et avec une seconde écriture de la règle
  de Benjamini et Hochberg. Une carte arrêtée bas qui reprend sous P ou P′ continue **la même** trajectoire cumulée
  (pas de richesse repartie de 1). `EvaluationFiltree` (`banc` l. 309-331) interdit les champs `promue`,
  `t_promotion`, `log_richesse_max`, `log_richesse_arretee` de l'évaluation à 800.
- **Aucune fuite d'instants non révélés.** Les sept bras ne lisent que `revelees()` et `courante()` de `Vue`
  (`rejeu` l. 37-63) ; les arrêts, la valeur e et la règle de promotion ne reçoivent que les instants révélés.
  La garde `Vue.lire` ne voit pas un accès direct au champ privé (ma mutation 1 le fait exprès) : c'est alors le
  vérificateur indépendant qui tue. **Sonde de validité** : j'ai joué les règles du moteur réel sur le rapport exact Λ
  d'un monde jouet (martingale d'espérance 1 ; c'est sur Λ, non sur W, qu'une fuite se voit, [T] l. 316-318) :

```
F                                                moyenne des valeurs e sur Λ = 1.008 ± 0.086 (6000 générations)
F-arret                                          moyenne des valeurs e sur Λ = 1.009 ± 0.086 (6000 générations)
A                                                moyenne des valeurs e sur Λ = 1.013 ± 0.100 (6000 générations)
P                                                moyenne des valeurs e sur Λ = 1.013 ± 0.089 (6000 générations)
P-prime                                          moyenne des valeurs e sur Λ = 1.016 ± 0.099 (6000 générations)
G                                                moyenne des valeurs e sur Λ = 0.976 ± 0.121 (6000 générations)
G mutée (lit le bloc suivant, témoin positif)    moyenne des valeurs e sur Λ = 1.237 ± 0.122 (6000 générations)
```

  Les six bras restent à 1 (dans l'incertitude) ; le témoin positif (la règle mutée du banc du développeur, garde
  levée) monte à 1,24, comme la contre-lecture du texte (1,267). Puissance limitée (6 000 générations) : dit.
- **Le dénominateur certifié est celui du juge réel.** `banc.trajectoire_de` (l. 334-341) appelle
  `nul_filles_v2.evaluer_v2` de la copie empreintée sur un engagement bâti par `construire_engagement_v2` et gelé par
  `geler_engagement` ; la bibliothèque est celle de `juger_carte` (essai `test_montage_comme_juger_carte`, relu) ; les
  membres ajustés rendent leur valeur **plus** la marge d'optimisation (écart de Frank-Wolfe, décrément de Newton),
  recalculée à chaque instant sur les seules issues de l'instant. Rien n'est réécrit du côté du banc.
- **Gel avant les issues fraîches, flux propres** : machine à états de `Generation` (`banc` l. 355-450), relue ;
  essais sur cas sain et artefacts, relus.
- Remarque, sans correction : l'essai E1 (étape 2) tire les issues fraîches de trois générations **avant** que
  l'oracle ne soit calculé (étape 3) ; c'est l'ordre de [T] l. 469-472, et l'oracle ne dépend que de sa graine.

## 4. R1 — aucun chiffre lu ou affiché avant le scellement

- Le jeu décisif n'appelle jamais la lecture ; il n'affiche que le chemin du manifeste et quatre empreintes
  (`scripts/jouer_idee_1_2_v1.py` l. 143). Les fils n'affichent rien. `jeu.json` n'est écrit qu'à la fin, d'un seul
  tenant, puis scellé (`execution` l. 255-258) ; sur arrêt, `arret.json` ne porte que le motif et le journal.
- La lecture (`scripts/lire_idee_1_2_v1.py`) refuse une sortie non scellée (`lire` l. 78-94), un manifeste non
  décisif ou d'un autre texte, une racine différente, un run incomplet (500 et 750 exigés), une lecture déjà écrite ;
  elle n'affiche que l'empreinte et le chemin.
- Ce qui peut s'afficher sur défaut seulement : le message d'une garde (`rejeu` l. 229, l. 237) porte l'allocation ou
  la valeur e d'une carte d'une génération, dans un run alors arrêté et invalide. Acceptable ; dit (mineur 9).
- **Refus du lanceur**, sondés dans des dépôts jetables (le jeu n'est jamais parti : une sentinelle remplace les
  essais ; programme et sortie en annexe) :

```
0 sain (préenregistrement, arbre propre, addendum scellé)      PASSE : gardes d'entrée passées : essais atteints (jeu non lancé)  [conforme]
1 préenregistrement absent                                     PASSE : gardes d'entrée passées : essais atteints (jeu non lancé)  [NON CONFORME à l'attendu : REFUS]
2 compagnon du préenregistrement absent                        PASSE : gardes d'entrée passées : essais atteints (jeu non lancé)  [NON CONFORME à l'attendu : REFUS]
3 préenregistrement modifié puis rescellé (autre empreinte)    PASSE : gardes d'entrée passées : essais atteints (jeu non lancé)  [NON CONFORME à l'attendu : REFUS]
4a arbre sale : fichier non suivi                              REFUS : arbre de travail non propre : committer avant le run, ou autoriser explicitement (la réserve est alors consignée au manifeste)  [conforme]
4b arbre sale : fichier gelé modifié, non versé                REFUS : arbre de travail non propre : committer avant le run, ou autoriser explicitement (la réserve est alors consignée au manifeste)  [conforme]
5a sortie existante sous diag/ (run arrêté)                    REFUS : une sortie de ce jeu existe déjà (['20261101-000000-idee-1-2-tirages-repartis-v1']) : relance seulement sous un texte ou un addendum neuf  [conforme]
5b manifeste d'un run antérieur sous runs/, rien sous diag/    PASSE : gardes d'entrée passées : essais atteints (jeu non lancé)
6a sans addendum                                               REFUS : addendum d'empreintes scellé exigé (--addendum) : pas de jeu  [conforme]
6b addendum non scellé                                         REFUS : <bloc-notes>/cl/sonde-lanceur.CaJT/c6b/addendum-v1.md : empreinte comp  [conforme]
6c addendum scellé auquel manque un fichier gelé               REFUS : addendum : fichiers gelés absents de la liste : ['tests/test_organisme_idees_juge_execution_v1.py']  [conforme]
6d fichier gelé modifié après l'addendum, puis versé           REFUS : un fichier gelé diffère de l'addendum : src/controle_ia/organisme_idees_juge/rejeu_v1.py (7fd31be71724… ≠ a1a08ef78c87…) : pas de jeu  [conforme]
6e addendum introuvable (chemin faux)                          REFUS : <bloc-notes>/cl/sonde-lanceur.CaJT/c6e/absent.md : fichier absent sur   [conforme]
```

  Les cas 1 à 3 « passent » dans cette sonde **parce que `jeu_decisif` appelle `exiger_prereg()` sans argument** et que
  la valeur par défaut du paramètre est liée au dépôt réel à la définition de la fonction (`scripts/jouer_idee_1_2_v1.py`
  l. 55, l. 113) : ce n'est pas le dépôt jetable qui est vérifié. La garde elle-même, appelée sur le dépôt jetable :

```
0 sain (dépôt jetable c0)          PASSE : bdabf2bc9b2c…
1 préenregistrement absent         REFUS : de-lanceur.CaJT/c1/prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md : fichier absent sur disque
2 compagnon absent                 REFUS : t-anticipe-v4.md : empreinte compagnon organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md.sha256 absente
3 modifié puis rescellé            REFUS : préenregistrement f1249b8ce1d6… ≠ texte scellé attendu bdabf2bc9b2c…
dépôt réel                         PASSE : bdabf2bc9b2c…
valeur par défaut du paramètre : /home/user/controle-ia-travail
```

  Elle est donc saine, et dans le jeu réel elle vérifie le bon dépôt ; `creer_manifeste(decisif=True, prereg=…)` la
  rejoue. Mais l'essai du développeur est vert pour une autre raison (majeur 2) :

```
garde levée dans le scénario de l'essai : addendum d'empreintes scellé exigé (--addendum) : pas de jeu
```

  Arbre sale, sortie existante, addendum absent, non scellé, incomplet ou démenti par un fichier : **refusés** pour la
  bonne raison. Cas 5b : un manifeste antérieur sous `runs/` sans rien sous `diag/` ne bloque pas (mineur 3).

## 5. R9 — graines au manifeste

Le manifeste du jeu décisif (`creer_manifeste`, `scripts/jouer_idee_1_2_v1.py` l. 131) consigne la configuration et son
empreinte, les versions (numpy compris), le commit, l'arbre propre, le préenregistrement et son empreinte. Les graines y
sont sous la forme **racine + règle de dérivation** (`config.racine_graines`, `config.cles_graines`, l. 88-93) : toute
graine du run se redérive. Le champ `graines` du manifeste reste vide (liste de tâches vide). **Tenu pour l'essentiel** ;
je recommande d'ajouter des états de contrôle (mineur 4).

## 6. Essais, mutations, gardes

**Suites rejouées** (machine chargée, charge moyenne 11 à 13) :

| suite | commande | résultat |
|---|---|---|
| six fichiers `tests/test_organisme_idees_juge_*_v1.py` | `python -B -m pytest -q -p no:cacheprovider …` | **109 passés sur 109**, 412,69 s |
| infrastructure : `tests/test_manifeste.py`, `test_scellement.py`, `test_prereg.py`, `test_run_factice.py` | idem | **30 passés sur 30**, 2,73 s |

L'arbre de travail est resté propre après ces suites (seul le dossier non suivi `correction-poids-v1/`, antérieur).

**Mes mutations** (greffons chargés par `-p`, en mémoire ; les six fichiers rejoués en entier sous chacune) :

| n° | mutation | sort | par quoi |
|---|---|---|---|
| 1 | le bras A lit l'issue du bloc suivant **hors de la garde d'accès** (champ privé de `Vue`) et évite les cartes qui vont tomber | **tuée** (29 échecs, 3 erreurs) | vérificateur indépendant : « bras A : allocation non conforme » (32 fois) ; la garde d'accès, elle, ne voit rien |
| 2 | le placebo P reçoit le ciblage (blocs restants parmi les seules actives) | **tuée** (24 échecs, 3 erreurs) | vérificateur indépendant : « bras P : allocation non conforme » |
| 3 | la lecture prend un intervalle à 90 % (quantiles 5 % et 95 %) | **survit** (109 passés sur 109) | aucun essai n'épingle le niveau de l'intervalle |
| 4 (en plus) | seuil d'arrêt bas à log(1/10) au lieu de log(1/20) | **survit** (109 passés sur 109) | la constante est partagée par le moteur et par le vérificateur ; aucun essai ne place une valeur entre les deux seuils ; le banc de mutations du développeur ne la voit pas non plus |

Les mutations 3 et 4 ne sont pas équivalentes au code (preuve d'effet) :

```
mutation 3 : bornes avant -0.01388 0.03387 ; après -0.01059 0.02889 ; borne basse > 0 avant : False ; après : False
mutation 4 : carte à log W = −2,5 après 50 tirages arrêtée bas avant : False ; après : True ; seuil du texte log(1/20) = -2.9957
```

**Troisième écriture des bras**, faite à partir du seul texte, comparée au moteur :

```
400 cas × 4 bras : 0 écart(s) entre la troisième écriture et le moteur ; propriétés de P tenues
ce que les cas exercent (bras A, sur 9600 cartes) : {'bas': 2215, 'haut': 716, 'plafond': 1, 'A<B': 1}
400 cas × 4 bras : 0 écart(s) entre la troisième écriture et le moteur ; propriétés de P tenues
ce que les cas exercent (bras A, sur 9600 cartes) : {'bas': 5194, 'haut': 0, 'plafond': 0, 'A<B': 0}
400 cas × 4 bras : 0 écart(s) entre la troisième écriture et le moteur ; propriétés de P tenues
ce que les cas exercent (bras A, sur 9600 cartes) : {'bas': 6489, 'haut': 0, 'plafond': 0, 'A<B': 0}
```

(Mes cas exercent peu le plafond ; les essais du développeur le font, relus.)

**Tenue de l'oracle à 20 000 issues** (30 générations, racine d'essai ; aucune issue fraîche, aucun bras) : aucun membre
ajusté à la borne triviale 0, écart de Frank-Wolfe de l'ajustement linéaire ≤ 10⁻⁵, aucun repli au plafond du cosinus ;
signes attendus : la carte « monde » de T a un gain > 0 (minimum 0,0017 nat par tirage), les membres exacts et les
copies de la classe ont tous un gain ≤ 0 (maximum −0,00002) ; 1,8 à 26 s par génération (moyenne 3,8 s). Je n'ai lu
aucune couverture ni aucune promotion : ces contrôles portent sur la construction, pas sur l'issue.

**Gardes de la liste d'arrêt (R5)** : chaque ligne a son cas sain et son artefact dans les essais (relus), sauf :
« durée murale > 24 h » pour l'artefact du fils mort (majeur 1) ; le refus sur préenregistrement non scellé, qui n'est
pas une ligne de la liste mais une garde du lanceur (majeur 2).

## 7. Durée et charge

Mesure à moi (racine d'essai, `nice` 10, charge moyenne ≈ 13 sur 4 cœurs partagés) :

```
T3 : construction 0.1 s processeur ; jeu 19.3 s processeur, 34.5 s muraux ; dont évaluations du juge 34.3 s muraux
N251 : construction 0.0 s processeur ; jeu 12.0 s processeur, 21.5 s muraux ; dont évaluations du juge 21.0 s muraux
T6 : construction 2.9 s processeur ; jeu 20.2 s processeur, 41.8 s muraux ; dont évaluations du juge 36.7 s muraux
```

Soit 12 à 20 s de processeur et 21 à 42 s muraux par génération et par processus : 1 250 générations sur deux processus
≈ **5 à 6 h de jeu sous la charge du jour**, plus l'oracle (≈ 0,5 h), E1 (≈ 20 min), les essais (≈ 7 min) et le banc de
mutations (≈ 3 min) : **≈ 6 à 7,5 h au total sous cette charge, ≈ 3 à 5 h sur machine libre**. Je confirme l'estimation
de [RD]. Marge de trois à quatre fois sous 24 h. Charge ajoutée : deux processus à priorité basse, une file de calcul
chacun, mémoire faible (quelques dizaines de mégaoctets retenus par le parent).

**Le lanceur borne-t-il sa durée ?** En marche normale, **oui** : l'horloge part au début de `jeu_decisif` (essais et
mutations compris), chaque tâche la relit à son départ, le parent la relit à chaque résultat ; le dépassement est d'au
plus une génération. **Non si un fils meurt ou se bloque** : majeur 1.

## Majeurs

**M1 — `src/controle_ia/organisme_idees_juge/execution_v1.py`, l. 195-203 (et l. 237-239, l. 250-252).** Si un
processus fils meurt (tué par le système, par exemple), `pool.imap` ne rend jamais la tâche perdue : le parent attend
sans fin, `garde.verifier` n'est plus relue, aucun `arret.json` n'est écrit. La ligne « durée murale > 24 h : arrêt ;
run invalide » de [T] l. 513 n'est donc pas tenue sur cet artefact (R5). Sonde (tâches factices passées à `execution_v1._carte`) :

```
reçu 0
reçu 1
reçu 2
TOUJOURS BLOQUÉ après 25 s : aucun retour, aucune exception (la garde de durée du parent n'est jamais relue)
code de sortie de la sonde = 3
```

Rien ne serait lu (pas de `jeu.json`) : l'échec est du côté sûr, mais la garde ne joue pas.
- ancien (l. 202-203) :
  ```python
      with multiprocessing.get_context("fork").Pool(processus) as pool:
          yield from pool.imap(tache, taches)
  ```
- nouveau (`_carte` reçoit la garde ; la sortie du bloc `with` tue les fils) :
  ```python
      with multiprocessing.get_context("fork").Pool(processus) as pool:
          resultats = pool.imap(tache, taches)
          for _ in range(len(taches)):
              while True:
                  garde.verifier("attente d'un processus fils")
                  try:
                      r = resultats.next(timeout=60)
                      break
                  except multiprocessing.TimeoutError:
                      continue
              yield r
  ```
  Correction éprouvée au bloc-notes (cas sain, puis fils mort, limite de 6 s) :
  ```
  cas sain : [0, 1, 2, 3, 4, 5, 6, 7]
  artefact (fils mort) : arrêt après 6.4 s : durée murale > 0 h (attente d'un processus fils) : arrêt ; run invalide
  ```
  À porter avec un essai de même forme (tâche factice dont un fils meurt, limite courte, « durée murale » attendue). Dans le même
  geste, poser `signal.signal(signal.SIGTERM, gardes.lever_sur_term)` au début de `jeu_decisif` (l. 109), pour qu'un
  arrêt externe soit consigné lui aussi.

**M2 — `tests/test_organisme_idees_juge_execution_v1.py`, l. 168-174, et `scripts/jouer_idee_1_2_v1.py`, l. 55 et
l. 113.** L'essai `test_lanceur_refuse_un_preenregistrement_non_scelle` attend une `GardeArret` sans motif ; celle qui
lève est « addendum d'empreintes scellé exigé » : le préenregistrement altéré du dépôt jetable n'est jamais vérifié,
parce que `exiger_prereg()` est appelée sans argument et que son défaut est lié au dépôt réel. Une garde « tuée pour une
autre raison » : R5 non tenue pour ce refus. La garde est saine dans le jeu réel (section 4).
- ancien (script, l. 55 et l. 113) : `def exiger_prereg(racine_depot: Path = RACINE_DEPOT) -> str:` ; `    exiger_prereg()`
- nouveau : `def exiger_prereg(racine_depot: Path) -> str:` ; `    exiger_prereg(RACINE_DEPOT)` (de même l. 158)
- ancien (essai, l. 172) : `        with pytest.raises(GardeArret):`
- nouveau : `        with pytest.raises(GardeArret, match="organisme-idee-1-2-tirages-repartis|texte scellé attendu"):` ;
  ajouter les cas « fichier absent », « compagnon absent » et « modifié puis rescellé » (les trois de ma sonde).

**M3 — deux paramètres gelés sans essai qui les épingle : `lire_banc_tirages_repartis_v1.py`, l. 73 ;
`rejeu_v1.py`, l. 28.** Mutations 3 et 4 survivantes. Le code est conforme à [T] (l. 293-294, l. 327) ; les essais ne
le garderaient pas.
- ancien : aucun essai sur la valeur des bornes ; `test_arrets_bas_seulement_apres_50_tirages_et_haut_des_25` n'emploie
  que −3,5 et −1,0 (`tests/test_organisme_idees_juge_rejeu_v1.py`, l. 59-70).
- nouveau : (a) un essai qui compare `Reechantillonneur.intervalle(v)` à `numpy.quantile(moyennes, [0.025, 0.975])`
  recalculé sur les indices `(99, b)`, et vérifie qu'il diffère des quantiles 5 % et 95 % ; (b) un essai où une carte à
  log W = −2,5 après 50 tirages **n'est pas** arrêtée et une carte à −3,0 **l'est**, plus
  `assert R.SEUIL_BAS == math.log(1 / 20) and R.SEUIL_HAUT == math.log(24 / 0.05)` ; (c) ces deux mutations ajoutées au
  banc `mutations_v1`.

## Mineurs

1. **`oracle_v1.py`, l. 62-66 ; juge, `nul_filles_v2.py`, l. 151.** Si l'ajustement logarithmique d'un membre ne
   converge pas à 20 000 issues, le juge rend la borne triviale 0 ; l'oracle la prendrait pour le meilleur membre et
   toute la génération serait sans « porteuse », sans signal (repli silencieux, R5). Non observé (0 sur 30).
   ancien : `valeurs[m["nom"]] = float(J.nf.valeurs_ajustees(m, cache, issues, B.K, [n])[n])` ; nouveau : la même
   ligne, puis `if valeurs[m["nom"]] == 0.0: triviaux.append(m["nom"])`, le champ `membres_a_la_borne_triviale` écrit
   dans la table, et son compte rapporté par la lecture dans `audit_R4` (sans toucher un critère).
2. **`scripts/lire_idee_1_2_v1.py`, l. 38-45.** L'empreinte du manifeste lu n'est pas comparée au champ
   `manifeste_sha256` des sorties ; la présence de `journal.json` et l'absence de `arret.json` ne sont pas exigées.
   ancien : `m, _ = lire_manifeste(chemin_m)` ; nouveau : `m, sha_m = lire_manifeste(chemin_m)`, puis refus si
   `LB.charger_sortie(dossier)["manifeste_sha256"] != sha_m`, si `arret.json` existe ou si `journal.json` manque.
3. **`scripts/jouer_idee_1_2_v1.py`, l. 62-69.** `exiger_sortie_absente` ne regarde que `diag/` pour les runs
   antérieurs : un run tué entre le manifeste et la première écriture sous `diag/` ne bloque pas la relance (sonde 5b).
   ancien : `if diag.is_dir():` … ; nouveau : la même recherche du suffixe `NOM_RUN` sous `runs/` aussi.
4. **`scripts/jouer_idee_1_2_v1.py`, l. 88-93 et l. 131.** Le champ `graines` du manifeste est vide. ancien :
   `"cles_graines": {…}` seul ; nouveau : ajouter `"etats_de_controle": {"(1, 0, 24)": B.etat_graine(racine, 1, 0, 24),
   "(0, 0, 0, 2)": B.etat_graine(racine, 0, 0, 0, 2), "(99, 0)": B.etat_graine(racine, 99, 0)}`, que la lecture
   revérifie (une dérive de numpy se verrait).
5. **Arrêt externe non consigné** : voir M1, dernière phrase (`scripts/jouer_idee_1_2_v1.py`, l. 109).
6. **Trois lectures non listées par [RD]**, à déclarer dans l'addendum, sans changer le code : (a) `banc` l. 206 : en
   famille T, la loi de base des trois tempérées est tirée uniforme parmi S1 à S4 ([T] l. 394-395 ne le dit que pour
   N) ; (b) `rejeu` l. 159 : la phase 2 de P′ commence au tour max(tour, 8) ; (c) `rejeu` l. 241-249 : l'étiquette
   d'arrêt suit l'ordre haut, plafond, bas, fin ; sous P et P′ une carte arrêtée bas qui a repris reste étiquetée
   « bas » (les parts d'arrêts de ces deux bras se lisent avec cette réserve).
7. **`banc` l. 495.** Les 50 cartes de E1 sont toutes dans les cellules 0 et 1 (V1) et le monde M₀ : la lettre de [T]
   l. 469 est tenue (« couvrant chaque sorte ») ; à dire dans l'addendum. Sans correction exigée.
8. **`execution_v1.py`, l. 33-52.** Les fichiers gelés n'incluent pas `src/controle_ia/gardes.py`, `scellement.py`,
   `manifeste.py`, `prereg.py`, `tests/conftest.py`, que ce code importe ; ils sont tenus par le commit et l'arbre
   propre. `verifier_addendum` vérifie **toute** ligne listée (l. 115-118) : l'addendum peut les lister sans changer
   le code. Recommandé.
9. **`rejeu_v1.py`, l. 229 et l. 237.** Les messages de ces deux gardes portent l'allocation ou la valeur e d'une
   carte ; ils ne sortent que sur défaut, dans un run arrêté. ancien : `… : {n} ≠ {list(attendu)}` ; nouveau, au
   choix : garder (acceptable), ou n'écrire que le numéro du bras et de la génération.

Note sur R12 : les 18 fichiers sont versés sous des noms en `_v1` (commit `e4411649`) ; les corrections sont de
nouvelles versions. Le choix entre noms `_v2` et correction avant addendum revient à la mère ; l'addendum n'étant pas
scellé, aucune empreinte gelée n'est encore engagée.

## Ce que je n'ai pas vérifié

- Le jeu réel, la répétition miniature, le banc de mutations et l'essai E1 avec la racine du texte (hors de ma
  consigne) ; la mise à mort de « valeur e au maximum » n'est établie que sur racine d'essai ([RD]).
- La tenue numérique du juge sur 1 250 générations (une exception arrête le run, par construction) ; la fréquence
  réelle du repli au plafond du cosinus (aucun sur mes 30 générations d'essai).
- La lecture gelée sur une sortie réelle : relue ligne à ligne, éprouvée seulement par les essais sur sorties
  fabriquées du développeur et par ma mutation 3.
- La preuve de validité elle-même : hors de ma tâche (déjà contre-lue) ; ma sonde sur Λ n'en est qu'un recoupement,
  de puissance limitée.

## Annexe A — programmes de mutation (bloc-notes de la session, recopiés en entier)

Dossier : `<bloc-notes>/cl/mut/`, où `<bloc-notes>` est le dossier de bloc-notes de la session mère (chemin entier rendu à la mère avec ce rapport ; il n'est pas écrit ici, et il est remplacé par `<bloc-notes>` dans les sorties recopiées). `lancer_mutation.sh` a été réécrit après les passes pour déduire ce dossier de son propre emplacement au lieu de l'écrire : même commande, mêmes options.

`mut/mutation_cl_1_allocation_lit_la_suite.py` (`c1f2fc4efc448ebaf24e3db9501384646fd8f87b899a168c5b77fa53ca55da1a`) :

```python
"""Mutation 1 de la contre-lecture (greffon pytest, en mémoire, aucun fichier du dépôt touché) : le bras A lit l'issue
du bloc suivant SANS passer par la garde d'accès (`Vue._valeurs`), et n'envoie pas de bloc à une carte dont le bloc
suivant la ferait tomber sous 1/20. La garde `Vue.lire` ne peut pas la voir ; attendu : tuée par le vérificateur
indépendant (« allocation non conforme »)."""
from controle_ia.organisme_idees_juge import rejeu_v1 as R


def _active_anticipee(v):
    if not R.active(v):
        return False
    if 1 <= v.n < R.NB and v._valeurs[v.n] < R.SEUIL_BAS:   # instant non révélé, lu hors de la garde
        return False
    return True


def bras_A_mute(vues, positions, budget, rng=None):
    R._tours(vues, positions, budget, R.NB, 0, _active_anticipee)


def pytest_configure(config):
    R.bras_A = bras_A_mute
    R.BRAS["A"] = (bras_A_mute, R.BUDGET_BLOCS)
```

`mut/mutation_cl_2_placebo_cible.py` (`60253624d5401d5cf245e0575e3e05ac1bd96e3d4aaf4e15d3cdf855afdb2a51`) :

```python
"""Mutation 2 de la contre-lecture : le placebo P reçoit le ciblage — ses blocs restants sont tirés au hasard parmi les
seules cartes actives (les arrêtées bas sont exclues, comme sous A), au lieu de l'ensemble élargi du texte. Attendu :
tuée par le vérificateur indépendant (« allocation non conforme »)."""
from controle_ia.organisme_idees_juge import rejeu_v1 as R


def bras_P_mute(vues, positions, budget, rng):
    R._tours(vues, positions, budget, R.PART_BLOCS, 0, R.active)
    while budget.reste > 0:
        candidates = R.par_position(positions, [i for i in range(R.M) if R.active(vues[i]) and vues[i].n < R.NB])
        if not candidates:
            return
        R.donner(vues[candidates[int(rng.integers(len(candidates)))]], budget)


def pytest_configure(config):
    R.bras_P = bras_P_mute
    R.BRAS["P"] = (bras_P_mute, R.BUDGET_BLOCS)
```

`mut/mutation_cl_3_intervalle_90.py` (`749cb52b9586db5068d861022a5f8a1de852d43e4374723c9fa789965ba16d16`) :

```python
"""Mutation 3 de la contre-lecture : la lecture gelée prend un intervalle percentile à 90 % (quantiles 5 % et 95 %) au
lieu de 95 % (2,5 % et 97,5 %) — toutes les bornes de la principale, des qualifications et de la lecture (3)."""
import numpy as np

from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB


def intervalle_mute(self, v):
    v = np.asarray(v, dtype=float)
    if v.size == 0:
        return {"estimation": None, "bas": None, "haut": None, "n": 0}
    moy = v[self.indices(len(v))].mean(axis=1)
    bas, haut = np.quantile(moy, [0.05, 0.95])
    return {"estimation": float(v.mean()), "bas": float(bas), "haut": float(haut), "n": int(len(v))}


def pytest_configure(config):
    LB.Reechantillonneur.intervalle = intervalle_mute
```

`mut/mutation_cl_4_seuil_bas_un_dixieme.py` (`690a4f3a54f7a4a04bb9927a36b6c62b877ef045ad6cbefaff599d5d17f6c9de`) :

```python
"""Mutation 4 de la contre-lecture (en plus des trois demandées) : le seuil d'arrêt bas passe de log(1/20) à log(1/10).
La constante `rejeu_v1.SEUIL_BAS` est partagée par le moteur des bras ET par le vérificateur indépendant : celui-ci ne
peut donc pas voir la mutation ; seuls des essais qui épinglent le seuil du texte le peuvent."""
import math

from controle_ia.organisme_idees_juge import rejeu_v1 as R


def pytest_configure(config):
    R.SEUIL_BAS = math.log(1 / 10)
```

`mut/lancer_mutation.sh` (`b8a4b32c0d0897610203e75606b788be1be6b342324ae12ebef5caa3bfe11718`) :

```sh
#!/bin/sh
# usage : lancer_mutation.sh NOM_DU_GREFFON [options pytest]   — rejoue les six fichiers d'essais sous la mutation
# (S : dossier parent de ce programme, dans le bloc-notes de la session ; les sorties y sont écrites)
S=$(cd "$(dirname "$0")/.." && pwd)
cd /home/user/controle-ia-travail || exit 2
nom=$1; shift
PYTHONPATH=src:$S/mut PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 nice -n 5 .venv/bin/python -B -m pytest -q \
  -p no:cacheprovider -p "$nom" --basetemp="$S/pytest-$nom" "$@" \
  tests/test_organisme_idees_juge_lecture_v1.py tests/test_organisme_idees_juge_rejeu_v1.py \
  tests/test_organisme_idees_juge_lois_v1.py tests/test_organisme_idees_juge_banc_v1.py \
  tests/test_organisme_idees_juge_mutations_v1.py tests/test_organisme_idees_juge_execution_v1.py \
  > "$S/sortie-$nom.txt" 2>&1
echo "code=$?" >> "$S/sortie-$nom.txt"
```

`mut/preuve_effet_mutations_3_4.py` (`a4fe27d181759b99d3a4441a3a9af898a52068b97e0f74bc959348eec4856aa0`) :

```python
"""Contre-lecture : les mutations 3 et 4, qui survivent, changent bien le comportement du code (elles ne sont pas
équivalentes) — vecteur fabriqué, aucune donnée du banc."""
import math
import numpy as np
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB, rejeu_v1 as R

v = np.random.default_rng(1).normal(0.02, 0.3, 500)
avant = LB.Reechantillonneur(123, 2000).intervalle(v)
import mutation_cl_3_intervalle_90 as m3
m3.pytest_configure(None)
apres = LB.Reechantillonneur(123, 2000).intervalle(v)
print("mutation 3 : bornes avant", round(avant["bas"], 5), round(avant["haut"], 5), "; après", round(apres["bas"], 5), round(apres["haut"], 5),
      "; borne basse > 0 avant :", avant["bas"] > 0, "; après :", apres["bas"] > 0)
vue = R.Vue([-1.0, -2.5] + [0.0] * 30); vue.reveler(); vue.reveler()   # 1/20 < W = e^-2,5 < 1/10 à 50 tirages
a = R.arretee_bas(vue)
import mutation_cl_4_seuil_bas_un_dixieme as m4
m4.pytest_configure(None)
print("mutation 4 : carte à log W = −2,5 après 50 tirages arrêtée bas avant :", a, "; après :", R.arretee_bas(vue),
      "; seuil du texte log(1/20) =", round(math.log(1 / 20), 4))
```

Dernière ligne de chaque sortie (`sortie-<greffon>.txt`, même dossier parent) :

```
sortie-mutation_cl_1_allocation_lit_la_suite.txt : 29 failed, 77 passed, 3 errors in 191.43s (0:03:11)
sortie-mutation_cl_2_placebo_cible.txt : 24 failed, 82 passed, 3 errors in 180.12s (0:03:00)
sortie-mutation_cl_3_intervalle_90.txt : 109 passed in 366.63s (0:06:06)
sortie-mutation_cl_4_seuil_bas_un_dixieme.txt : 109 passed in 327.87s (0:05:27)
```

## Annexe B — sondes (bloc-notes de la session, recopiées en entier)

Dossier : `<bloc-notes>/cl/`.

`sonde_pool_fils_mort_v1.py` (`8a1ad34accaf8366c9b19ae02ff3bb6954d351ccc0479e19b76182661186a370`) :

```python
"""Sonde de la contre-lecture : que fait `execution_v1._carte` (Pool « fork », imap) quand un processus fils meurt
brutalement (tué par le système, par exemple faute de mémoire) ? Tâches factices, aucun code du banc n'est joué."""
import os, sys, time, threading
from controle_ia.organisme_idees_juge import execution_v1 as X

def tache(t):
    if t == 3:
        os._exit(137)          # mort brutale du fils, comme un `kill -9`
    time.sleep(0.2)
    return t

def chien_de_garde():
    time.sleep(25)
    print("TOUJOURS BLOQUÉ après 25 s : aucun retour, aucune exception (la garde de durée du parent n'est jamais relue)", flush=True)
    os._exit(3)

threading.Thread(target=chien_de_garde, daemon=True).start()
recus = []
try:
    for r in X._carte(2, tache, list(range(8))):
        recus.append(r)
        print("reçu", r, flush=True)
    print("fin normale", recus)
except BaseException as e:
    print("exception", type(e).__name__, e)
```

`sonde_lanceur_v1.py` (`8136bca05208f540f0d8a885fc2970ead7833de16f8346f39d5ebbbb93f0ae1f`) :

```python
"""Sonde de la contre-lecture (R5) : refus du lanceur `scripts/jouer_idee_1_2_v1.py` en mode décisif, chaque garde sur
un cas sain et sur un artefact, dans des dépôts git jetables du bloc-notes. Le jeu n'est JAMAIS lancé : dans le cas
sain, `lancer_essais` est remplacé par une sentinelle qui arrête dès que toutes les gardes d'entrée sont passées."""
import argparse, importlib.util, shutil, subprocess, sys, tempfile
from pathlib import Path
from unittest import mock

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B, execution_v1 as X

DEPOT = Path("/home/user/controle-ia-travail")
BASE = Path(sys.argv[1])


class Sentinelle(Exception):
    pass


def git(r, *a):
    subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True)


def lanceur():
    spec = importlib.util.spec_from_file_location("jouer_idee_1_2_v1", DEPOT / "scripts" / "jouer_idee_1_2_v1.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def depot_sain(nom, addendum="scelle"):
    r = BASE / nom
    r.mkdir(parents=True)
    git(r, "init", "-q", "-b", "main"); git(r, "config", "user.email", "t@example.invalid"); git(r, "config", "user.name", "t")
    for f in (B.CHEMIN_PREREG, B.CHEMIN_PREREG + ".sha256", *X.FICHIERS_GELES):
        (r / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(DEPOT / f, r / f)
    if addendum:
        a = r / "addendum-v1.md"
        a.write_text("# addendum d'essai\n\n```\n" + X.lister_empreintes(r) + "```\n", encoding="utf-8")
        if addendum == "scelle":
            sceller(a)
    git(r, "add", "-A"); git(r, "commit", "-q", "-m", "init")
    return r


def essayer(nom, r, addendum="addendum-v1.md", attendu=None):
    L = lanceur()
    args = argparse.Namespace(addendum=addendum, processus=2, miniature=False, sortie=None)

    def sentinelle(_):
        raise Sentinelle("gardes d'entrée passées : essais atteints (jeu non lancé)")
    with mock.patch.object(L, "RACINE_DEPOT", r), mock.patch.object(L, "abaisser_priorite", lambda: None), \
            mock.patch.object(L, "lancer_essais", sentinelle):
        try:
            L.jeu_decisif(args)
            issue = "AUCUN ARRÊT (anormal)"
        except Sentinelle as e:
            issue = f"PASSE : {e}"
        except GardeArret as e:
            issue = "REFUS : " + str(e).splitlines()[0][:150]
        except Exception as e:  # noqa: BLE001
            issue = f"AUTRE EXCEPTION {type(e).__name__} : {str(e)[:150]}"
    conforme = "" if attendu is None else ("  [conforme]" if issue.startswith(attendu) else "  [NON CONFORME à l'attendu : " + attendu + "]")
    print(f"{nom:<62} {issue}{conforme}", flush=True)


essayer("0 sain (préenregistrement, arbre propre, addendum scellé)", depot_sain("c0"), attendu="PASSE")
r = depot_sain("c1"); git(r, "rm", "-q", B.CHEMIN_PREREG, B.CHEMIN_PREREG + ".sha256"); git(r, "commit", "-q", "-m", "x")
essayer("1 préenregistrement absent", r, attendu="REFUS")
r = depot_sain("c2"); git(r, "rm", "-q", B.CHEMIN_PREREG + ".sha256"); git(r, "commit", "-q", "-m", "x")
essayer("2 compagnon du préenregistrement absent", r, attendu="REFUS")
r = depot_sain("c3"); p = r / B.CHEMIN_PREREG; p.write_text(p.read_text(encoding="utf-8") + "\n", encoding="utf-8")
Path(str(p) + ".sha256").unlink(); sceller(p); git(r, "add", "-A"); git(r, "commit", "-q", "-m", "x")
essayer("3 préenregistrement modifié puis rescellé (autre empreinte)", r, attendu="REFUS")
r = depot_sain("c4"); (r / "brouillon.txt").write_text("x")
essayer("4a arbre sale : fichier non suivi", r, attendu="REFUS")
r = depot_sain("c4b"); f = r / X.FICHIERS_GELES[5]; f.write_text(f.read_text(encoding="utf-8") + "\n# x\n", encoding="utf-8")
essayer("4b arbre sale : fichier gelé modifié, non versé", r, attendu="REFUS")
r = depot_sain("c5"); d = r / X.DOSSIER_DIAG / ("20261101-000000-" + X.NOM_RUN); d.mkdir(parents=True); (d / "arret.json").write_text("{}")
git(r, "add", "-A"); git(r, "commit", "-q", "-m", "x")
essayer("5a sortie existante sous diag/ (run arrêté)", r, attendu="REFUS")
r = depot_sain("c5b"); d = r / "runs" / ("20261101-000000-" + X.NOM_RUN); d.mkdir(parents=True); (d / "manifeste.json").write_text("{}")
git(r, "add", "-A"); git(r, "commit", "-q", "-m", "x")
essayer("5b manifeste d'un run antérieur sous runs/, rien sous diag/", r)
essayer("6a sans addendum", depot_sain("c6a"), addendum=None, attendu="REFUS")
essayer("6b addendum non scellé", depot_sain("c6b", addendum="nu"), attendu="REFUS")
r = depot_sain("c6c", addendum=None); a = r / "addendum-v1.md"
a.write_text("```\n" + "".join(X.lister_empreintes(r).splitlines(keepends=True)[:-1]) + "```\n", encoding="utf-8"); sceller(a)
git(r, "add", "-A"); git(r, "commit", "-q", "-m", "x")
essayer("6c addendum scellé auquel manque un fichier gelé", r, attendu="REFUS")
r = depot_sain("c6d"); f = r / X.FICHIERS_GELES[5]; f.write_text(f.read_text(encoding="utf-8") + "\n# x\n", encoding="utf-8")
git(r, "add", "-A"); git(r, "commit", "-q", "-m", "x")
essayer("6d fichier gelé modifié après l'addendum, puis versé", r, attendu="REFUS")
essayer("6e addendum introuvable (chemin faux)", depot_sain("c6e"), addendum="absent.md", attendu="REFUS")
```

`sonde_prereg_v1.py` (`b31e46ef6d8bc3e55e5dd7df4852d93d1d50196e77a6ff678cbe5db0212f59e6`) :

```python
"""Sonde de la contre-lecture : la garde `exiger_prereg` du lanceur, appelée avec la racine du dépôt jetable (les cas
1 à 3 de `sonde_lanceur_v1.py` ne l'atteignent pas : `jeu_decisif` appelle `exiger_prereg()` sans argument, et la valeur
par défaut de son paramètre est liée au dépôt réel à la définition de la fonction)."""
import importlib.util, sys
from pathlib import Path
from controle_ia.gardes import GardeArret

DEPOT = Path("/home/user/controle-ia-travail")
spec = importlib.util.spec_from_file_location("jouer_idee_1_2_v1", DEPOT / "scripts" / "jouer_idee_1_2_v1.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
for nom, cas in (("0 sain (dépôt jetable c0)", "c0"), ("1 préenregistrement absent", "c1"), ("2 compagnon absent", "c2"),
                 ("3 modifié puis rescellé", "c3")):
    try:
        print(f"{nom:<34} PASSE : {L.exiger_prereg(Path(sys.argv[1]) / cas)[:12]}…")
    except GardeArret as e:
        print(f"{nom:<34} REFUS : {str(e).splitlines()[0][-110:]}")
print(f"{'dépôt réel':<34} PASSE : {L.exiger_prereg()[:12]}…")
import inspect
print("valeur par défaut du paramètre :", inspect.signature(L.exiger_prereg).parameters["racine_depot"].default)
```

`sonde_essai_prereg_v1.py` (`99c429e65f3aa94a432d0cf371fcdc50753ad1025d843b4675353efb4239d1cc`) :

```python
"""Sonde de la contre-lecture : le scénario exact de l'essai du développeur
`test_lanceur_refuse_un_preenregistrement_non_scelle` (préenregistrement altéré dans un dépôt jetable, `_args()` sans
addendum) — quelle garde lève réellement ?"""
import argparse, importlib.util, shutil, subprocess, sys
from pathlib import Path
from unittest import mock
from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B

DEPOT = Path("/home/user/controle-ia-travail")
r = Path(sys.argv[1]) / "essai-dev"
r.mkdir()
def git(*a): subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True)
git("init", "-q", "-b", "main"); git("config", "user.email", "t@example.invalid"); git("config", "user.name", "t")
p = r / B.CHEMIN_PREREG; p.parent.mkdir(parents=True)
shutil.copyfile(DEPOT / B.CHEMIN_PREREG, p); shutil.copyfile(DEPOT / (B.CHEMIN_PREREG + ".sha256"), str(p) + ".sha256")
with open(p, "a", encoding="utf-8") as f: f.write("\nligne ajoutée\n")
git("add", "-A"); git("commit", "-q", "-m", "x")
spec = importlib.util.spec_from_file_location("jouer_idee_1_2_v1", DEPOT / "scripts" / "jouer_idee_1_2_v1.py")
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
with mock.patch.object(L, "RACINE_DEPOT", r), mock.patch.object(L, "abaisser_priorite", lambda: None):
    try:
        L.jeu_decisif(argparse.Namespace(addendum=None, processus=2, miniature=False, sortie=None))
    except GardeArret as e:
        print("garde levée dans le scénario de l'essai :", str(e).splitlines()[0])
```

`troisieme_ecriture_bras_v1.py` (`f52f30bac32495f98ba3a6dc42e47ff235f5a943a675dab0cb515be1a6016b14`) :

```python
"""Contre-lecture : troisième écriture des bras, faite par le contre-lecteur à partir du seul texte scellé (section
« Bras »), bloc par bloc, comparée au moteur `rejeu_v1` (fonctions des bras, `Vue`, `Budget`) sur des trajectoires
tirées au hasard (aucun juge, aucune donnée du banc). F-arrêt, A, P′ et G : allocation exigée égale ; P : propriétés
de structure (phase 1 égale à F-arrêt tant qu'il reste du budget ; aucun bloc à une carte arrêtée haut ou au plafond ;
budget épuisé sauf si plus aucune carte n'est éligible)."""
import math, sys
import numpy as np
from controle_ia.organisme_idees_juge import rejeu_v1 as R

M, NB, B = 24, 32, 192
HAUT, BAS = math.log(24 / 0.05), math.log(1 / 20)


def haut(t, n):
    return any(x >= HAUT for x in t[:n])


def bas(t, n):                      # log W < log(1/20) après au moins 50 tirages : instants d'indice ≥ 1
    return any(x < BAS for x in t[1:n])


def tours(lw, pos, n, reste, plafond, tour, elargi):
    par_pos = sorted(range(M), key=lambda i: pos[i])
    while reste > 0:
        donne = False
        for k in range(M):
            i = par_pos[(k + tour) % M]
            if reste == 0:
                break
            if n[i] < plafond and not haut(lw[i], n[i]) and (elargi or not bas(lw[i], n[i])):
                n[i] += 1; reste -= 1; donne = True
        if not donne:
            break
        tour += 1
    return reste, tour


def texte(nom, lw, pos):
    n = [0] * M
    if nom == "F-arret":
        tours(lw, pos, n, B, 8, 0, False)
    elif nom == "A":
        tours(lw, pos, n, B, NB, 0, False)
    elif nom == "P-prime":
        reste, tour = tours(lw, pos, n, B, 8, 0, False)
        tours(lw, pos, n, reste, NB, max(tour, 8), True)      # numérotation des tours continuée (lecture 13)
    elif nom == "G":
        n = [2] * M; reste = B - 2 * M
        while reste > 0:
            libres = [i for i in range(M) if n[i] < NB and not haut(lw[i], n[i])]
            if not libres:
                break
            j = max(libres, key=lambda i: (lw[i][n[i] - 1], -pos[i]))
            n[j] += 1; reste -= 1
    return n


def moteur(nom, lw, pos, rng=None):
    vues = [R.Vue(t) for t in lw]
    budget = R.Budget(B)
    R.BRAS[nom][0](vues, pos, budget, rng)
    return [v.n for v in vues]


ecarts, cas, stats = 0, int(sys.argv[1]), {"bas": 0, "haut": 0, "plafond": 0, "A<B": 0}
for c in range(cas):
    rng = np.random.default_rng([2026, c])
    if len(sys.argv) > 2:      # régimes proches du banc : 18 (« banc ») ou 21 (« plafond ») cartes qui tombent, les autres indécises
        k = 18 if sys.argv[2] == "banc" else 21
        derive = np.r_[np.full(k, -0.4), rng.choice([-0.02, 0.0, 0.05, 0.15], size=M - k)][rng.permutation(M)][:, None]
        lw = np.cumsum(rng.normal(derive, 0.35, (M, NB)), axis=1).round(6).tolist()
    else:
        derive = rng.choice([-0.3, -0.1, 0.0, 0.1, 0.3], size=(M, 1))
        lw = np.cumsum(rng.normal(derive, rng.choice([0.3, 0.8, 1.5]), (M, NB)), axis=1).round(6).tolist()
    pos = [int(p) for p in rng.permutation(M)]
    for nom in ("F-arret", "A", "P-prime", "G"):
        a, b = texte(nom, lw, pos), moteur(nom, lw, pos)
        if a != b:
            ecarts += 1
            print("ÉCART", c, nom, a, b)
    nA = moteur("A", lw, pos)
    stats["bas"] += sum(bas(lw[i], nA[i]) for i in range(M)); stats["haut"] += sum(haut(lw[i], nA[i]) for i in range(M))
    stats["plafond"] += sum(x == NB for x in nA); stats["A<B"] += sum(nA) < B
    nFa, nP = moteur("F-arret", lw, pos), moteur("P", lw, pos, np.random.default_rng([7, c]))
    assert all(p >= f for p, f in zip(nP, nFa)), "P : phase 1 ≠ F-arrêt"
    for i in range(M):                      # aucun bloc donné après un arrêt haut ; plafond tenu
        assert nP[i] <= NB and not haut(lw[i], nP[i] - 1), "P : bloc donné à une carte arrêtée haut"
    eligibles = [i for i in range(M) if nP[i] < NB and not haut(lw[i], nP[i])]
    assert sum(nP) == B or not eligibles, "P : budget non épuisé alors qu'il reste des éligibles"
    assert sum(nP) >= sum(nA) and sum(nP) <= B
print(f"{cas} cas × 4 bras : {ecarts} écart(s) entre la troisième écriture et le moteur ; propriétés de P tenues")
print("ce que les cas exercent (bras A, sur", cas * M, "cartes) :", stats)
```

`validite_bras_sur_lambda_v1.py` (`d1ed0a500111aad9fd4a0d02f7744a34a28bf435e6d39806964ced49b5093860`) :

```python
"""Contre-lecture : les règles d'allocation du moteur réel (`rejeu_v1`, fonctions des bras) jouées sur le rapport exact
Λ du monde jouet (`synthetique_v1.trajectoires_lot`, martingale d'espérance 1 sous le monde), racine d'essai. Sur Λ, une
règle qui lirait un instant non révélé pousse la moyenne des valeurs e au-dessus de 1 (texte scellé, réserve (b) ;
contre-lecture du texte : 1,267) ; une règle non anticipante la laisse à 1 (arrêt optionnel). Témoin positif : la
règle mutée du banc du développeur (`mutations_v1._G_qui_lit_le_bloc_suivant`), garde d'accès levée. Aucun juge."""
import hashlib, math, sys
import numpy as np
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B, rejeu_v1 as R, synthetique_v1 as S, mutations_v1 as MU

RACINE = B.racine_de(hashlib.sha256(b"contre-lecture du code, idee 1.2, validite des bras sur le rapport exact (racine d'essai)").hexdigest())
assert RACINE != B.racine_de(B.EMPREINTE_PREREG)
N = int(sys.argv[1])


class VueSansGarde(R.Vue):          # témoin positif seulement : la garde d'accès est levée
    __slots__ = ()
    def lire(self, k):
        return self._valeurs[min(k, R.NB - 1)]


def jouer(nom, lam, pos, g, fonction=None, vue=R.Vue):
    vues = [vue(t) for t in lam]
    budget = R.Budget(R.BUDGET_BLOCS)
    rng = R.generateur_placebo(RACINE, 0, g) if nom == "P" else None
    (fonction or R.BRAS[nom][0])(vues, pos, budget, rng)
    return [R.log_valeur_e(v.revelees()) for v in vues], sum(v.n for v in vues)

noms = ["F", "F-arret", "A", "P", "P-prime", "G", "G mutée (lit le bloc suivant, témoin positif)"]
E = {n: np.empty((N, 24)) for n in noms}
for debut in range(0, N, 500):
    fin = min(N, debut + 500)
    _, lam = S.trajectoires_lot(RACINE, debut, fin)
    for x, g in enumerate(range(debut, fin)):
        t = lam[x].tolist()
        pos = [int(p) for p in B.generateur(RACINE, 0, g, 1001).permutation(24)]
        for n in noms[:-1]:
            le, tot = jouer(n, t, pos, g)
            assert tot <= R.BUDGET_BLOCS
            E[n][g] = np.exp(le)
        E[noms[-1]][g] = np.exp(jouer("G", t, pos, g, MU._G_qui_lit_le_bloc_suivant, VueSansGarde)[0])
for n in noms:
    par_gen = E[n].mean(axis=1)
    es = par_gen.std(ddof=1) / math.sqrt(N)
    print(f"{n:<48} moyenne des valeurs e sur Λ = {par_gen.mean():.3f} ± {1.96 * es:.3f} ({N} générations)")
```

`tenue_oracle_v1.py` (`441f339b3ad9ec46271b69b4da18dfff4c7635f6a72bb07fbe84eb0310069b78`) :

```python
"""Contre-lecture du code de l'idée 1.2 : tenue de l'oracle à 20 000 issues (racine d'essai, jamais celle du texte).
Pour chaque génération : valeur de chaque membre du nul (par tirage), membre ajusté rendu à la borne triviale 0
(ajustement logarithmique non convergé), écart de Frank-Wolfe de l'ajustement linéaire, classes de l'oracle par sorte,
replis au plafond du cosinus, durée. Aucune issue fraîche n'est tirée, aucun bras n'est joué."""
import hashlib, json, sys, time
import numpy as np
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B, juge_v1, oracle_v1 as O

RACINE = B.racine_de(hashlib.sha256(b"contre-lecture du code, idee 1.2, tenue de l'oracle (racine d'essai)").hexdigest())
assert RACINE != B.racine_de(B.EMPREINTE_PREREG)
J = juge_v1.charger()
gens = [("T", g) for g in range(int(sys.argv[1]))] + [("N", g) for g in list(range(int(sys.argv[2]))) + list(range(250, 250 + int(sys.argv[2])))]
vrai_lineaire = J.nf._lineaire
ecarts = []
def espion(G, w0=None):
    v, w, e = vrai_lineaire(G, w0)
    ecarts.append((G.shape[0], e))
    return v, w, e
J.nf._lineaire = espion   # en mémoire seulement, pour lire l'écart de Frank-Wolfe ; la valeur rendue est inchangée
for fam, g in gens:
    t0 = time.time(); ecarts.clear()
    gen = B.Generation(RACINE, fam, g)
    t = O.table_oracle(J, gen)
    triviaux = [k for k, v in t["membres"].items() if v == 0.0]
    cl = {}
    for c in t["cartes"]:
        cl.setdefault(c["sorte"], []).append((c["classe"][:12], round(c["gain"], 5)))
    plaf = [c.indice for c in gen.cartes if c.details.get("plafond_atteint")]
    print(json.dumps({"gen": gen.nom, "cellule": g % 10, "meilleur": t["meilleur_membre"], "membres_a_zero": triviaux,
                      "ecart_FW_a_20000": [e for n, e in ecarts if n == 20000], "plafond_cosinus": plaf,
                      "duree_s": round(time.time() - t0, 1), "classes": cl}, ensure_ascii=False), flush=True)
```

`mesure_duree_v1.py` (`06f8c9b1d154119460686ad562d1d5e920347887bd978bcd260446d3f09caa20`) :

```python
"""Contre-lecture : durée d'une génération du jeu (tâche `execution_v1._tache_jeu`, racine d'essai), temps processeur et
temps mural ; seules les durées sont affichées (aucun chiffre de promotion, de couverture ni de valeur e)."""
import hashlib, time, sys
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B, execution_v1 as X, juge_v1
RACINE = B.racine_de(hashlib.sha256(b"contre-lecture du code, idee 1.2, mesure de duree (racine d'essai)").hexdigest())
assert RACINE != B.racine_de(B.EMPREINTE_PREREG)
juge_v1.charger()
for fam, g in (("T", 3), ("N", 251), ("T", 6)):
    c0, m0 = time.process_time(), time.time()
    gen = B.Generation(RACINE, fam, g)
    emp = [c.empreinte for c in gen.cartes]
    c1 = time.process_time()
    r = X._tache_jeu((RACINE, fam, g, emp, "0" * 64, time.time()))
    print(f"{fam}{g} : construction {c1 - c0:.1f} s processeur ; jeu {time.process_time() - c1:.1f} s processeur, "
          f"{time.time() - m0:.1f} s muraux ; dont évaluations du juge {r['duree_evaluations_s']:.1f} s muraux", flush=True)
```

`essai_correction_m1_v1.py` (`be20c5afb5a97933a3f08247b01011ba1e3fba2f148549ceb930b523b46b36af`) :

```python
"""Contre-lecture : la correction proposée pour le majeur 1 (attente bornée, garde relue), éprouvée sur un cas sain et
sur l'artefact du fils mort (tâches factices, limite de 6 s, pas d'attente de 1 s)."""
import multiprocessing, os, time
from controle_ia.gardes import GardeArret
from controle_ia.organisme_idees_juge import execution_v1 as X


def carte_corrigee(processus, tache, taches, garde, pas=1.0):
    with multiprocessing.get_context("fork").Pool(processus) as pool:
        resultats = pool.imap(tache, taches)
        for _ in range(len(taches)):
            while True:
                garde.verifier("attente d'un processus fils")
                try:
                    r = resultats.next(timeout=pas)
                    break
                except multiprocessing.TimeoutError:
                    continue
            yield r


def saine(t):
    time.sleep(0.2); return t


def fils_mort(t):
    if t == 3:
        os._exit(137)
    time.sleep(0.2); return t


print("cas sain :", list(carte_corrigee(2, saine, list(range(8)), X.GardeDuree(limite_s=6, horloge=time.time))))
t0 = time.time()
try:
    print(list(carte_corrigee(2, fils_mort, list(range(8)), X.GardeDuree(limite_s=6, horloge=time.time))))
except GardeArret as e:
    print(f"artefact (fils mort) : arrêt après {time.time() - t0:.1f} s : {e}")
```

## Annexe C — empreintes des sorties des sondes

Sorties brutes, dans `<bloc-notes>/cl/` (le bloc-notes est volatil : ce sont les copies de ce rapport qui restent).

```
1a4681860ca7068b72989799cef4139e3943a59c549068c03031aef4ce8d4299  sortie-mutation_cl_1_allocation_lit_la_suite.txt
ac43c47958d6e81a4da0095660b391310eb9820c7d2b1b0bfc3f6701925e3ac9  sortie-mutation_cl_2_placebo_cible.txt
1322474611fda6c383513c0641eed21dbcf5ced23cf587f32bb2cb2fd6d2a507  sortie-mutation_cl_3_intervalle_90.txt
8782273348739f138de9f38c1f8ce12e47dc2566080b1490ec9fa3ce7a27be72  sortie-mutation_cl_4_seuil_bas_un_dixieme.txt
e65a7c91d1ccf730e9279edc6023d31dd8829365b82faaafc4bd5ae8a3f1b74c  sortie-validite-bras-sur-lambda-v1.txt
b42938561fe4bcbfd1e3eea6ff21415317dcf40e3157d6d88636f4add4c92e6a  sortie-sonde-lanceur-v1.txt
08393fcb83f787c65f15a099bf9a937001e1dc0bcc206f324ed0250f515c33c3  sortie-sonde-prereg-v1.txt
10fec9e1ddb831efd2ced2cb63a3352abd2855a91c601d5070111f21ae17febc  sortie-sonde-essai-prereg-v1.txt
990dfca13b275436bb593a32c9ff6f6541233e5e91dbad14504733a5755078ef  sortie-sonde-pool-v1.txt
91a0b028c07e47190a0596673413c74c98a725fe21ae8cfa53d85b44bd61ae29  sortie-essai-correction-m1-v1.txt
2d83ecfaa870ccfbd389f285dcbe6e180ad116b8c6f74f3a0c18b059513585f5  sortie-troisieme-ecriture-bras-v1.txt
edf717f58ff2a5291e8fc0131fb28d9884c61dfe152e8b37531a5fdcaa8a92f3  sortie-tenue-oracle-v1.txt
4a3ff7e0fcecd4ec8f908d2298af82b9a08ab3267cf82bc389157a5e57800d85  sortie-mesure-duree-v1.txt
a6a5c74ee6c7ec20dfd6a3a2ab008cb826058072797c876af2333c7957f63b05  sortie-preuve-effet-mutations-3-4.txt
e1b08b01be332e0f06b623c3952186fdcb2814842a2fbf1bb83d7a82a1f77b6c  suite-six.log
ec882953493ab6796a9e3910edf580972f1ef0749b56e017c7ce3b6856aa0a2c  empreintes-code.txt
```
