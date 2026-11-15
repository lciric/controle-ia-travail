# Réfutation — correction des poids du nul, angle « toute autre voie » — v1

**Statut.** Mise au point exploratoire, sur processeur, **aucune revendication**. Réfutateur neuf, d'un autre modèle que
l'auteur : je n'ai écrit ni le juge, ni les nuls v8 et v9, ni la preuve du nul limité, ni son préenregistrement, ni la
contre-lecture, ni les fiches, ni le rendu que je réfute. Travail du 2026-11-15, de 18:05 à 19:30 UTC (`date -u`), dépôt lu
sur `main` (tête `7fcef1be`). Aucun commit, aucune poussée, aucun appel réseau ni payant. Aucun fichier de l'auteur n'est
modifié (empreintes revérifiées à la fin, section 12). Toute adoption est une **décision du directeur**.

Pièce réfutée : `methodes-libre-v1.md` (`e7a2bb6c67241cbb41477c3f6839d802392d74e60960272e5da10ef2cbffc14c`) et son résumé
chiffré `sortie-resume-libre-v1.json` (`b3e7f382c7884496e3a63a8ad7f86aea6be8c804c6b52099ad8946e9d502a0f6`), même dossier.

## 0. Verdict en sept lignes

1. **Les chiffres de l'auteur se rejouent à l'identique.** 22 690 décisions rejouées, aucune différence. Mon programme, écrit
   à part, rend les mêmes décisions que le sien sur ses 8 500 mondes, sauf une (le v9, un monde sur les 2 500 où il le calcule).
2. **Les méthodes qu'il dit valides tiennent, chacune sur sa propre classe** : maximum certifié (façon v9), nul limité aux
   coupures de l'archive, nul limité plus partitions déclarées, grille de déciles, filtre « ET ». Sur 44 000 mondes de taille
   neufs, dont 22 000 où la carte n'est pas une copie, la pire borne haute à 95 % est 0,0406, sous le niveau 0,05.
3. **Les trois nuls rétrécis ne tiennent pas sur la classe du v9**, comme l'auteur le dit : copies hors de leur classe promues
   de 0,27 à 0,99. Ce ne sont donc pas des corrections « valides » au sens demandé ; ce sont des nuls plus petits.
4. **L'artefact échoue dans les deux bancs** : poids appris en ligne, 0,999 à 1,000 ; poids ajustés sur une moitié, 0,19 à
   0,64.
5. **La conclusion centrale de l'auteur est trop forte.** Son lemme A est juste, mais il ne couvre que les dénominateurs lus
   au même instant pour tous les membres. Deux règles de lecture qu'il n'a pas essayées gardent la garantie sur **toute** la
   classe du v9 et promeuvent plus que le v9, monde pour monde : rejeter chaque membre à son propre instant (+0,005 à +0,008),
   et lire plus d'instants (+0,012 à +0,023 avec 40 instants). Ensemble : +0,020 à +0,032. C'est peu, et moins que les nuls
   rétrécis ; mais ce n'est pas « aucune ».
6. **Le gain annoncé des nuls rétrécis est gonflé par une omission du banc.** Avec les membres log-linéaires du nul v8, que
   les deux bancs omettent, le gain du nul limité sur le v9 tombe de +0,14 / +0,12 / +0,08 à +0,08 / +0,07 / +0,06.
7. **Deux rejets de l'auteur sont mal fondés** : le dépassement « au bord » de la méthode 5 vient pour partie de sa règle de
   quantile (la 95e valeur sur 100 au lieu de la 96e) ; et, pour la méthode 11, « mêmes taux attendus » est faux quand les
   autres données sont dix fois plus nombreuses (0 à 0,023 au lieu de 0,20 à 0,70). Aucune des deux n'a de preuve pour autant.

## 1. Pièces lues (empreintes recalculées, égales à leurs compagnons)

| pièce | chemin | sha256 |
|---|---|---|
| preuve du nul limité | `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` | `44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2` |
| préenregistrement de l'idée 1.1 | `docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md` | `46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089` |
| contre-lecture | `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-nul-limite-et-preuve-v1.md` | `763fc6e29cd80868dcdb1d848eafdc928a39fca7244fa16eb0ac721ec705014e` |
| nul v9 (lu en entier, jamais exécuté) | `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| code du juge, copie `94bfd92` (53 fichiers conformes), lus, jamais exécutés | `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/` : `selection_pari.py`, `nul_v8.py`, `nul_filles_v2.py`, `a_blanc_v59.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc`, `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888`, `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910`, `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` (dans cet ordre ; liste `empreintes-copie-v1.txt`) |
| relevé, § 1.1 | `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md` | `bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c` |
| fiches n° 0, 14, 9, 13 (argon-p1-01, argon-p2-01, opus-p1-05, fable-p1-05), champ `demande_organisme` | `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json` | `a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5` |
| verdict du v9 (seul fichier ouvert dans `docs/verdicts/`, par son chemin exact, sans recherche) | `docs/verdicts/verdict-validation-nul-v9-v1.md` | `1407e460367754bb9f76b37174f3a21585970864eb9beaa2699494d90125c1ea` |
| rendu de l'auteur : note, résumé, six programmes, 94 tranches | dossier `libre/` | les neuf empreintes du rendu sont égales aux compagnons ; les 94 tranches listées dans le résumé sont conformes |

« Puissance perdue », d'après le verdict : la taille du v9 est tenue sur ses 18 lignes fatales ; sa perte appariée contre le
v8 dépasse la marge 0,05 sur une ligne (I02 : 105 sur 1 000).

## 2. Ce que j'ai fait, point par point de la mission

| point | fait | où |
|---|---|---|
| (a) preuves suivies pas à pas | lemme A, lemme B, théorème 1 appliqué à chaque classe, marge de grille ; deux pas trop forts trouvés, contre-exemples calculés | section 3 |
| (b) programmes de l'auteur rejoués | résumé, banc (24 tranches, dont 14 entières), projection (2 tranches), coût | section 4 |
| (c) attaque par un programme à moi | 52 000 mondes en 24 cas, 2 000 mondes par cas au moins (4 000 pour les deux cas les plus durs) ; arrêt aux 8 instants du juge | sections 5 et 6 |
| (d) artefact | échoue dans son banc et dans le mien | section 7 |
| (e) puissance et loyauté | rejeu entier des trois doses ; mêmes tirages, mêmes instants, même seuil vérifiés sur son code ; 2 000 mondes neufs par dose ; effet du certificat lâche et des membres omis mesurés | section 8 |
| méthodes dites non valides | une passe : échec réel pour six, mal fondé pour deux, non mesurable pour deux | section 9 |

Mes fichiers (même dossier) : `attaque_libre_v1.py`, sa sortie `sortie-attaque-libre-v1.json`, le complément
`attaque_libre_lecture_dense_v1.py` et sa sortie `sortie-attaque-libre-lecture-dense-v1.json` (empreintes en section 12).
Sauf mention, tout chiffre « mien » vient de **[S]** = `sortie-attaque-libre-v1.json`, champ `cas.<nom>.taux` ou
`cas.<nom>.apparie` ; **[D]** = `sortie-attaque-libre-lecture-dense-v1.json`. Intervalles : Clopper-Pearson bilatéraux à 95 %.

## 3. Les preuves de l'auteur, pas à pas

**Théorème 1 de la preuve du nul limité, appliqué à chaque classe (référence, méthodes 1, 2, 3, 8).** Juste. Le
dénominateur domine la vraisemblance du monde dès que le monde est dans la classe ; la richesse reste sous le rapport de
vraisemblance au monde ; l'inégalité de Ville (à vérifier sur pièce) borne tous les instants à la fois. J'ai contrôlé ce pas
de domination monde par monde : sur les 44 000 mondes de taille, **aucune** promotion par un bras dont la classe contient le
monde sans que le rapport au monde atteigne 1/α à un instant lu ([S], `domination_violee` : 0 partout).

**Certificat (valeur atteinte plus écart de Frank-Wolfe).** Juste. Contrôle : 400 problèmes tirés au hasard (une cellule ou
une coupure, 25 à 200 tirages, 3 ou 6 lois connues, poids intérieurs ou au bord), comparés à un optimiseur indépendant
(programmation quadratique séquentielle, six départs). Le certificat de l'auteur (`essai_libre_commun_v1.em_certifie`, importé
tel quel) : **0 violation sur 400**. Le mien, après 3, 30 et 300 pas : 0 violation ([S], `certificat`).

**Lemme A (« le maximum est le plus petit dénominateur dominant »).** Juste, et presque une définition. **Mais la conclusion
que l'auteur en tire est plus large que le lemme.** Sa ligne 1 dit : « aucune méthode de cet angle n'est à la fois valide sur
toute la classe du nul v9 et plus puissante que lui. Ce n'est pas un manque d'essais ». Le lemme ne parle que d'une règle de la
forme « vraisemblance de la carte sur un dénominateur qui domine chaque membre, lu **au même instant pour tous les membres**,
aux 8 instants du juge ». Deux contre-exemples calculés (section 10) :

- **Rejeter chaque membre à son propre instant.** Règle : la carte est promue si, pour chaque famille F du nul (une cellule ;
  sous-population ; un trait et un seuil réel), il existe un instant lu t où le maximum certifié de F est sous
  log q(y_1..t) − log(1/α). Le v9 exige le **même** t pour toutes les familles. *Validité sur toute la classe du v9* : si le
  monde θ* est dans F*, « F* rejetée à t » entraîne log p_θ*(y_1..t) ≤ log q(y_1..t) − log(1/α), donc le rapport au monde
  vaut au moins 1/α à t ; Ville borne par α la probabilité que cela arrive à un instant quelconque. *Puissance* : toute
  promotion du v9 en est une (prendre le même t pour toutes). Mesuré : jamais moins, +0,005 à +0,008 de plus.
- **Lire plus d'instants.** La borne de Ville vaut pour tous les instants de 1 à n (la contre-lecture le dit déjà, correction
  p2 : fixer 8 instants n'est pas nécessaire au théorème). Lire 40 instants au lieu de 8 garde la garantie sur toute la
  classe et ne peut que promouvoir plus. Mesuré : +0,012 à +0,023. L'auteur a écarté « moins d'instants » ; il n'a pas
  regardé « plus d'instants ».

Ces gains sont petits. Le fond pratique de sa conclusion tient donc à peu près : les gains de l'ordre de +0,1 ne viennent
que d'une classe rétrécie. Mais la phrase « aucune méthode » est fausse telle qu'écrite, et le directeur avait demandé
d'épuiser les options.

**Lemme B (« le niveau ne se partage pas »).** Le sens suffisant est juste : si chaque test φ_P a le niveau α sur 𝒞_P, la
règle « tous rejettent » a le niveau α sur l'union ; et une règle « OU » n'est valide que si chaque branche l'est. Deux
phrases vont trop loin : « il **faut** α_P ≤ α pour chaque P » et « retirer un membre ouvre 𝒞_P **en entier** ».
Contre-exemples : (i) la famille « une cellule » est contenue dans toute autre famille (mêmes poids des deux côtés) : la
retirer ne change aucune décision ; (ii) la famille « coupure de l'archive » est absente de la grille de déciles, et ses
mondes ne sont pas promus à 1 : 0,0025 [0,0008 ; 0,0058] sur les membres par morceaux à poids tirés (mon cas C6), 0,377 sur la
copie pure (C5), 0,578 quand la coupure est dans la queue (C7) ; l'auteur lui-même mesure 0,001 (T4b) et 0,384 (T4). Ce
qui est vrai : il ne reste **aucune garantie** sur la part de 𝒞_P que les autres membres ne couvrent pas. Sans effet sur
les verdicts.

**Marge de grille de la méthode 4 (10^25,2 et 10^31,1 points).** L'arithmétique est juste (2^(1/200) = 1,00347 ; 3 986 points
par dimension, 7 dimensions). Ce sont deux conditions **suffisantes** grossières : elles montrent qu'une preuve par
recouvrement naïf est hors d'atteinte, pas qu'aucun certificat de seuil n'existe.

**Un manque du banc de l'auteur, sans faute de preuve.** Ses sept cas de taille sont tous des **copies exactes**. Pour un
dénominateur dominant, une copie a une richesse au plus 1 à chaque instant : ces cas éprouvent le certificat, pas la borne
de Ville. Mes cas « N » (monde dans la classe, carte qui n'est pas une copie) comblent ce manque.

## 4. Rejeu des programmes de l'auteur

- **Résumé** (`essai_libre_resume_v1.py`) : rejoué sur ses 94 tranches scellées ; sortie **égale à l'octet** à
  `sortie-resume-libre-v1.json` (`b3e7f382…`).
- **Banc** (`essai_libre_banc_v2.py`) : 14 tranches entières rejouées (cas 7, 8 et 9 en entier, soit les 1 500 mondes de
  puissance ; cas 6, mondes 0 à 249) et les 40 premiers mondes de chacun des 10 cas. **22 690 décisions comparées, 0
  différence** ; sur les 14 tranches entières, taux, quantiles de log W et restes de certificat sont identiques.
- **Projection** (`essai_libre_projection_carte_v1.py`) : cas 2 et 7, mondes 0 à 249 : décisions et quantiles identiques.
- **Coût** (`essai_libre_cout_v1.py`) : rejoué sur 20 cartes ; même ordre de grandeur (v9 0,19 s, nul limité 0,13 s, grille
  0,08 s, sur cœurs partagés).
- **Non rejoué** : la v1 du banc (l'auteur dit qu'elle n'a rien produit) ; les 54 autres tranches du banc en entier (temps).
- **Contrôle croisé** (mode `differentiel` de mon programme) : ses 8 500 mondes, rebâtis par ses fonctions de tirage, jugés
  par **mes** bras. Nul limité, nul limité plus partitions déclarées, grille : **mêmes décisions sur les 8 500 mondes**.
  Maximum certifié (2 500 mondes où il le calcule) : une seule différence, le monde 367 du cas 7, promu par mon v9 et pas par
  le sien (son certificat s'arrête à 400 pas). Sa réserve « certificat lâche jusqu'à 0,575 nat » coûte donc **une carte sur
  1 500** : 169 au lieu de 168 sur 500 à la dose 0,3 ([S], `differentiel_mondes_du_concepteur`).

## 5. Mon attaque : le banc

**Programme.** `attaque_libre_v1.py`, écrit sans recopier celui de l'auteur : mondes tirés par lots, décision au seuil au lieu
de la valeur, autres graines. La logique du juge est recopiée d'après lecture (pari plein, 200 tirages frais, instants 25 à
200, α = 0,05, promotion si la richesse passe 1/α à l'un des instants : arrêt optionnel compris). Aucun fichier des dossiers
de copie n'est exécuté ni importé.

**Décision.** Pour chaque partition et chaque instant, le programme monte par espérance-maximisation et tient deux bornes :
la valeur atteinte (borne basse du maximum) et le certificat (borne haute). La partition est « dégagée » si le certificat est
sous le seuil, « bloquée » si la valeur atteinte est au-dessus. Un nul promeut à un instant si toutes ses partitions y sont
dégagées. Si rien n'est acquis quand l'écart passe sous 10⁻³ nat (tolérance du nul v9) ou après 4 000 pas, la partition est
« indécise » : comptée non promue, et comptée promue dans le taux « au pire ». Les lectures de taille emploient le taux au
pire. Les indécis sont rares : au plus 5 couples (monde, instant) par bras et par cas, sur 2 000 mondes et 8 instants ([S],
`instants_indecis`).

**Simplification, la même que l'auteur.** Membres ordinaires et log-linéaires du nul v8 omis dans les bras de base. Un bras
« complet approché » les rajoute pour la puissance (section 8).

**Graines.** `numpy.random.SeedSequence(entropy=2026111518, spawn_key=(numéro du cas, numéro du lot))`, un générateur par lot
de 250 mondes ; écrites dans la sortie. Chaque simulation a duré 51 s au plus (61 s pour le complément).

**Cas** (2 000 mondes chacun, 4 000 pour N4a et N4b ; « dans la classe de » dit quels bras doivent tenir) :

| cas | monde | carte | dans la classe de |
|---|---|---|---|
| C1 | une cellule, poids Dirichlet(1) sur 3 lois connues et 3 lois certaines | copie | v9, La, Ld, grille |
| C2 | S1 seule (sommet) | copie | toutes |
| C3 | une cellule, poids Dirichlet(0,05) : poids extrêmes, bord du simplexe | copie | toutes |
| C4 | une cellule, **6 lois connues** et 3 lois certaines | copie | toutes |
| C5 | S1 et S2 de part et d'autre de la coupure de l'archive | copie | v9, La, Ld |
| C6 | même coupure, poids Dirichlet(1) par cellule, bruit aveugle commun | copie | v9, La, Ld |
| C7 | coupure de l'archive à 1,5 à 2,0 écarts-types : **petite cellule**, peu de tirages d'un côté | copie | v9, La, Ld |
| C8 | S1 et S2 par sous-population | copie | v9, Ld, grille |
| C9 | S1 et S2 selon le signe d'un trait | copie | v9, Ld |
| C10 | S1 et S2 de part et d'autre d'un décile du plan | copie | v9, grille |
| C11 | S1 et S2 de part et d'autre d'un seuil hors de l'archive | copie | v9 |
| N1a, N1b, N1c | S1 seule | S1 plus une composante qui n'existe pas, dose 0,15 ; 0,30 ; 0,50 | toutes |
| N2a, N2b | comme C5 | la même, S1 décalée, dose 0,25 ; 0,50 | v9, La, Ld |
| N3a, N3b | comme C1 | le monde incliné selon les traits, dose 0,20 ; 0,40 | toutes |
| N4a, N4b | S1 seule | **carte « tout ou rien »** : S1 partout, sauf sur quelques-unes des 25 premières instances, où elle mise tout sur l'issue la plus probable ; le rapport au monde vaut alors 20 au moins (N4a) ou 40 au moins (N4b) au premier instant lu, avec une probabilité proche de 1/20 ou de 1/40. C'est le pire cas de la borne de Ville avec peu de tirages. La carte lit le plan : la preuve le permet, un proposeur réel ne le peut pas | toutes |
| P1, P2, P3 | S1 plus une composante neuve, dose 0,3 ; 0,5 ; 0,7 (famille de l'auteur) | loi du monde | aucune |
| P4 | composante neuve d'un seul côté de la coupure de l'archive, dose 0,7 | loi du monde | aucune |

La = nul limité aux coupures de l'archive ; Ld = La plus sous-population et signe de chaque trait ; grille = déciles du plan.

## 6. Taille : résultats

**Copies (C1 à C11).** Pour chaque bras dont la classe contient le monde : **0 promotion sur 2 000**, borne haute 0,0018, dans
les onze cas. Cela vaut pour le maximum certifié (11 cas), La (7 cas), Ld (9 cas), la grille (6 cas), le filtre « ET ».

**Cartes qui ne sont pas des copies** (taux au pire ; borne haute à 95 % entre crochets) :

| cas | v9 | La | Ld | grille | rapport au monde (plafond de Ville) |
|---|---|---|---|---|---|
| N1a | 0 [0,0018] | 0,0005 [0,0028] | 0,0005 [0,0028] | 0,0005 [0,0028] | 0,006 |
| N1b | 0,003 [0,0065] | 0,0085 [0,0136] | 0,0065 [0,0111] | 0,0045 [0,0085] | 0,017 |
| N1c | 0,004 [0,0079] | 0,0105 [0,0160] | 0,0085 [0,0136] | 0,0075 [0,0123] | 0,020 |
| N2a | 0,001 [0,0036] | 0,0025 [0,0058] | 0,0025 [0,0058] | hors classe : 0,3005 | 0,0075 |
| N2b | 0,005 [0,0092] | 0,0075 [0,0123] | 0,0075 [0,0123] | hors classe : 0,192 | 0,0145 |
| N3a | 0 [0,0018] | 0 [0,0018] | 0 [0,0018] | 0 [0,0018] | 0,0125 |
| N3b | 0 [0,0018] | 0,0005 [0,0028] | 0,0005 [0,0028] | 0 [0,0018] | 0,0135 |
| **N4a** | 0,01525 [0,0196] | **0,0345 [0,0406]** | 0,03225 [0,0382] | 0,024 [0,0292] | 0,03975 [0,0463] |
| N4b | 0,015 [0,0193] | 0,0175 [0,0221] | 0,0175 [0,0221] | 0,01625 [0,0207] | 0,0175 |

**Toutes les bornes hautes sont sous 0,05.** Le cas le plus dur est la carte « tout ou rien » contre le nul limité : 138
promotions sur 4 000, borne haute 0,0406. Le nul limité y promeut plus que le v9 (0,0345 contre 0,015), parce que sa classe
est plus petite ; il reste sous le plafond. Emboîtement vérifié décision par décision : aucune carte promue par le v9 et
refusée par La, Ld ou la grille ([S], `emboitement_viole` : 0 partout).

**Hors de leur classe, les nuls rétrécis laissent passer** (ce que l'auteur dit aussi) :

| cas | La | Ld | grille |
|---|---|---|---|
| C8 sous-population | **0,985** [0,979 ; 0,990] | dans la classe : 0 | dans la classe : 0 |
| C9 signe d'un trait | **0,9135** [0,900 ; 0,925] | dans la classe : 0 | **0,2655** [0,246 ; 0,285] |
| C10 décile du plan | **0,8995** [0,885 ; 0,912] | **0,7665** [0,747 ; 0,785] | dans la classe : 0 |
| C11 seuil hors archive | **0,9405** [0,929 ; 0,950] | **0,886** [0,871 ; 0,900] | **0,412** [0,390 ; 0,434] |
| C5 coupure de l'archive | dans la classe : 0 | dans la classe : 0 | **0,377** [0,356 ; 0,399] |
| C7 coupure dans la queue | dans la classe : 0 | dans la classe : 0 | **0,578** [0,556 ; 0,600] |

Chiffres de l'auteur pour comparaison : La 0,991 (sous-population) et 0,948 (hors archive) ; Ld 0,897 ; grille 0,384 et 0,394.
Même ordre.

## 7. Artefact : les deux façons des fiches

| | banc de l'auteur (T1 à T4b, rejoué) | mon banc (C1 à C7, copies membres de la classe) |
|---|---|---|
| poids appris en ligne (argon-p2-01) | 0,999 à 1,000 | **0,999 à 1,000** |
| poids ajustés sur la première moitié (argon-p1-01), valeur e lue à la fin | lue à 125..200 : 0,202 à 0,581 | **0,1885 (C2) à 0,638 (C4)** ; lue à 125..200 : 0,1965 à 0,6695 |
| bras certifiés sur les mêmes tirages | 0 | 0 |

Les deux façons échouent nettement dans les deux bancs, sur des copies exactes de membres du nul qu'elles disent couvrir,
là où les bras certifiés restent à 0. Le banc de l'auteur voit le défaut ; le mien aussi. Avec 6 lois connues (C4), la façon
« moitié » échoue plus (0,638) qu'avec 3 (0,5485) : plus de poids à apprendre, plus de regret.

## 8. Puissance, et loyauté de la comparaison

**Rejeu.** Les trois doses sont rejouées en entier (1 500 mondes) : v9 0,336 / 0,650 / 0,792 ; La 0,476 / 0,768 / 0,876 ;
Ld 0,440 / 0,754 / 0,856 ; grille 0,400 / 0,722 / 0,836 ; gains appariés +0,140 / +0,118 / +0,084, +0,104 / +0,104 / +0,064,
+0,064 / +0,072 / +0,044 ; aucune carte promue par le v9 et refusée par un nul rétréci. Identiques.

**Loyauté, sur le code.** Tous les bras lisent les mêmes tirages `y`, aux mêmes instants `T`, contre le même seuil
(`essai_libre_banc_v2.py`, l. 164 à 205) ; le filtre « OU » emploie log(2/α) pour ses deux branches. Loyal sur ces trois
points.

**Mes mondes** (2 000 par dose, certificat serré à 10⁻³ nat) :

| bras | dose 0,3 | dose 0,5 | dose 0,7 | P4 (un côté de la coupure) |
|---|---|---|---|---|
| v9 | 0,2965 | 0,659 | 0,798 | 0,549 |
| La | 0,4425 (+0,146) | 0,775 (+0,116) | 0,8825 (+0,0845) | 0,656 (+0,107) |
| Ld | 0,4095 (+0,113) | 0,7545 (+0,0955) | 0,8685 (+0,0705) | 0,6345 (+0,0855) |
| grille | 0,3555 (+0,059) | 0,7075 (+0,0485) | 0,8355 (+0,0375) | 0,5975 (+0,0485) |

Entre parenthèses, le gain apparié sur le v9 ; aucune carte perdue. Les gains de l'auteur sont confirmés sur des mondes
neufs.

**Réserve 1, levée : le certificat lâche du v9.** Une carte sur 1 500 (section 4). Sans effet.

**Réserve 2, qui pèse : les membres omis.** L'auteur écrit que l'omission des membres du v8 « surestime la puissance de tous
les bras de la même façon ». Ce n'est pas exact pour le **gain** : un membre du v8 qui bloque une carte la bloque sous La
comme sous le v9, donc toute carte gagnée par La dans le juge complet l'est aussi dans le banc simplifié, et l'inverse est
faux. Le gain du banc est une borne haute. Mesure, en rajoutant les membres log-linéaires du v8 (chaque loi connue tempérée et
inclinée ; règle de `nul_filles_v2._logit`) :

| | dose 0,3 | dose 0,5 | dose 0,7 |
|---|---|---|---|
| nul « façon v8 » (une cellule et membres log-linéaires) | 0,3435 | 0,6745 | 0,819 |
| v9 complet approché | 0,239 | 0,575 | 0,7475 |
| La complet approché | 0,3255 | 0,654 | 0,806 |
| gain de La sur le v9, juge complet approché | **+0,0865** | **+0,079** | **+0,0585** |
| même gain, banc simplifié | +0,146 | +0,116 | +0,0845 |
| même gain, juge complet approché, **sur les mondes de l'auteur** | +0,078 | +0,072 | +0,062 |
| perte du v9 contre le nul « façon v8 » | 0,1045 | 0,0995 | 0,0715 |
| perte de La contre le nul « façon v8 » | 0,018 | 0,0205 | 0,013 |

Le gain annoncé (+0,14 / +0,12 / +0,08) devient +0,08 / +0,07 / +0,06 sur ses propres mondes. Il reste positif : le nul
limité reprend environ les quatre cinquièmes de ce que le v9 perd contre le nul « façon v8 » sur cette famille. La perte du
v9 que ce banc mesure (0,07 à 0,10) est du même ordre que celle du verdict (0,105 sur I02) ; je n'en tire rien de plus.

**Réserve 3 : une seule famille de découvertes.** La composante neuve d'un seul côté de la coupure de l'archive (P4) garde un
gain (+0,107 ; +0,0705 en juge complet approché). Je n'ai pas essayé d'autre famille.

## 9. Méthodes dites non valides : une passe

**Méthode 4 (seuil au pire cas sur une grille de 17 points).** Échec réel. Refaite par mon programme (mode `seuil`) :
0,270 [0,243 ; 0,299] sur des copies intérieures, 0,5835 [0,562 ; 0,605] au bord ([S], `seuil_simule`, `grille_seule_…`).
L'auteur : 0,269 et 0,617.

**Méthode 5 (grille plus projection de la carte).** Le rejet de l'auteur s'appuie sur 0,070 [0,055 ; 0,088] au bord. **Une
part de ce dépassement est un défaut de son banc.** Son seuil est `numpy.quantile(…, 0,95)` sur 100 simulations : cette
valeur tombe juste au-dessus de la 95e plus petite. Une statistique échangeable avec les 100 simulations la dépasse avec une
probabilité proche de 6/101 = 0,059, pas 0,05. Le rang exact est la 96e plus petite (5/101). Refait sur 2 000 mondes du
bord, mêmes simulations, deux règles ([S], `seuil_simule.T3`) :

| règle de quantile | grille plus projection | projection seule |
|---|---|---|
| celle de l'auteur | 0,0635 [0,0532 ; 0,0751] | 0,0695 [0,0587 ; 0,0815] |
| rang exact (96e sur 100) | **0,0575 [0,0477 ; 0,0686]** | 0,0635 [0,0532 ; 0,0751] |

Avec le rang exact, le dépassement n'est plus établi (0,05 est dans l'intervalle), sans que la taille soit établie non plus
(borne haute 0,0686). Ce qui reste vient de la projection, qui n'est pas exacte au bord après 600 pas (écart jusqu'à
0,014 nat) ; pour une copie, la projection exacte est la carte elle-même. J'ai cherché un vrai contre-exemple hors des
copies : monde = point de la classe le plus proche de la carte dans l'autre sens de la divergence, carte = vraie composante
neuve ; 2 000 mondes : 0,027 [0,020 ; 0,035], sous α. **Pas d'échec démontré, pas de preuve non plus : indéterminé.** Sa
puissance reste la plus faible (−0,29 à −0,35 sous La, rejoué) : sans intérêt pratique en l'état.

**Méthode 6 (rééchantillonnage sous le nul ajusté).** Échec réel au bord : 0,102 [0,084 ; 0,122]. La même règle de quantile
(190e sur 200) n'explique que 0,055. Non refaite par mon programme ; rejouée sur le sien.

**Méthodes 7 et 9 (filtre « OU », pari mixte).** Échec réel sur la copie hors archive (C11) : « OU » 0,9295 [0,917 ; 0,940] ;
pari mixte entre 0,9295 et 0,930 (encadré : le v9 y vaut au plus 1). L'auteur : 0,939 et 0,940.

**Méthode 8 (filtre « ET »).** Valide, et égale au v9, monde pour monde (0 différence sur mes 8 000 mondes de puissance).

**Méthode 10 (élagage certifié avant les tirages).** Ni l'auteur ni moi ne l'avons mesurée : il n'existe aucun certificat à
jouer. Son rejet repose sur un argument (« rien ne s'élague pour les découvertes faibles »), pas sur une mesure.
Indéterminé.

**Méthode 11 (poids appris sur d'autres données indépendantes).** L'auteur écrit « même mécanisme, mêmes taux attendus »,
sans la jouer. Le mécanisme est le même ; **les taux ne le sont pas**. Jouée sur les copies membres de la classe (C1 à C7),
poids ajustés sur N' tirages indépendants du même monde ([S], `M11_200`, `M11_2000`) :

| N' | taux de copies promues |
|---|---|
| 200 (autant que les tirages de la carte) | 0,2045 à 0,7025 : échec réel |
| 2 000 (dix fois plus) | **0 à 0,023** (borne haute la plus grande : 0,0306), sous α |

Elle n'a aucune garantie pour autant : l'espérance de la richesse dépasse 1, d'un facteur qui se rapproche de 1 quand N'
grandit ; une carte adverse peut donc dépasser α. Hors de la classe de l'archive elle laisse passer comme La (0,94 à 0,99).
Verdict : ne tient pas comme méthode garantie ; mais le rejet « mêmes taux » est faux tel qu'écrit, et les tirages frais des
autres cartes d'une même génération sont justement de telles données.

**Méthode 12 (seuil plus bas que log(1/α) sur la statistique du v9).** Non mesurée. Un tel seuil existe en principe (la
borne de Ville n'est pas atteinte : section 6, le v9 est à 0,015 quand le plafond est à 0,040) ; personne n'a de certificat
pour le calculer. Indéterminé.

## 10. Deux voies que l'auteur n'a pas essayées, valides sur toute la classe du v9

Mesurées pour donner un contre-exemple chiffré à sa ligne 1, pas pour les proposer : toute adoption change la règle de
lecture du juge, donc relève du directeur.

**Membre par membre** (preuve en section 3 ; [S], bras `v9_par_membre`). Taille : 0 sur les 22 000 copies ; carte « tout ou
rien » 0,02275 [0,0184 ; 0,0279] ; aucune promotion sans que le rapport au monde atteigne 1/α. Puissance, appariée au v9 :
+0,0065 / +0,008 / +0,005 (13, 16 et 10 cartes gagnées sur 2 000 ; 0 perdue) ; +0,0055 sur P4 ; +0,004 / +0,006 / +0,006 sur
les mondes de l'auteur.

**Lecture dense** (programme `attaque_libre_lecture_dense_v1.py`, sortie [D] ; mêmes mondes jugés deux fois, 8 instants puis
40 instants, un tous les 5 tirages ; 1 000 mondes par dose). Taille en lecture dense : 0 sur 1 000 copies ; cartes qui ne sont
pas des copies : v9 au plus 0,006, La au plus 0,007, bornes hautes au plus 0,0144.

| | dose 0,3 | dose 0,5 | dose 0,7 |
|---|---|---|---|
| v9, 8 instants | 0,293 | 0,679 | 0,796 |
| v9, 40 instants | 0,316 (+0,023) | 0,691 (+0,012) | 0,814 (+0,018) |
| v9 membre par membre, 40 instants | 0,322 (**+0,029**) | 0,699 (**+0,020**) | 0,821 (**+0,025**) |
| juge complet approché : v9, 8 instants | 0,238 | 0,596 | 0,751 |
| juge complet approché : v9 membre par membre, 40 instants | 0,265 (**+0,027**) | 0,628 (**+0,032**) | 0,778 (**+0,027**) |
| pour mémoire : La, 8 instants | 0,445 | 0,782 | 0,880 |

Aucune carte promue aux 8 instants et refusée en lecture dense. Lecture : ces deux règles reprennent, sans rien céder sur
la classe, à peu près un quart à deux cinquièmes de ce que le v9 perd contre le nul « façon v8 » sur ce banc (0,26 ; 0,36 ; 0,40). Elles restent loin du
nul limité (−0,06 à −0,12), qui, lui, cède les copies hors archive. Non essayé : lire les 200 instants ; la valeur e
arrêtée pour la règle de multiplicité (l'argument d'arrêt optionnel s'applique membre par membre, non joué) ; la réserve
log-linéaire du v8, qui joue à chaque instant lu.

## 11. Verdict par méthode

| méthode du rendu | l'auteur dit | verdict | raison courte, chiffre |
|---|---|---|---|
| Référence : maximum certifié (façon v9) | valide | **tient** | preuve suivie ; rejeu identique ; 0 sur 22 000 copies ; pire cas non copie 0,01525, borne haute 0,0196 ; puissance rejouée 0,336 / 0,650 / 0,792 et retrouvée 0,2965 / 0,659 / 0,798 |
| 1 : nul limité aux coupures de l'archive | valide sur sa classe | **tient, sur sa classe seulement** | 0 sur 14 000 copies de sa classe ; pire cas 0,0345, borne haute 0,0406 ; **ne couvre pas la classe du v9** : 0,90 à 0,99 hors classe ; gain +0,146 / +0,116 / +0,0845, ramené à +0,0865 / +0,079 / +0,0585 avec les membres log-linéaires |
| 2 : nul limité plus partitions déclarées | valide sur sa classe | **tient, sur sa classe seulement** | 0 sur 18 000 copies ; pire cas 0,03225, borne haute 0,0382 ; hors classe : 0,7665 (décile), 0,886 (hors archive) |
| 3 : grille de déciles | valide sur sa classe | **tient, sur sa classe seulement** | 0 sur 12 000 copies ; pire cas 0,024, borne haute 0,0292 ; hors classe : 0,27 à 0,58, dont la coupure de l'archive elle-même (0,377) |
| 4 : seuil au pire cas sur une grille | non valide | **ne tient pas** | échec réel : 0,270 et 0,5835 par mon programme |
| 5 : grille plus projection de la carte | non valide | **indéterminé** | aucune preuve ; le dépassement au bord vient pour partie de la règle de quantile ; rang exact : 0,0575 [0,0477 ; 0,0686] ; puissance très basse |
| 6 : rééchantillonnage sous le nul ajusté | non valide | **ne tient pas** | 0,102 [0,084 ; 0,122] au bord ; la règle de quantile n'explique que 0,055 |
| 7 : filtre « OU » | non valide | **ne tient pas** | 0,9295 sur la copie hors archive |
| 8 : filtre « ET » | valide, sans gain | **tient** | égal au v9, monde pour monde ; gain 0 |
| 9 : pari mixte | non valide | **ne tient pas** | 0,9295 à 0,930 sur la copie hors archive |
| 10 : élagage certifié avant les tirages | non valide, non mesurée | **indéterminé** | aucun certificat ; rien à mesurer ; rejet sur argument |
| 11 : poids appris sur d'autres données | non valide, non jouée | **ne tient pas** (aucune garantie) | 0,20 à 0,70 à N' = 200 ; mais 0 à 0,023 à N' = 2 000 : « mêmes taux attendus » est faux |
| 12 : seuil plus bas sur la statistique du v9 | non valide, non mesurée | **indéterminé** | aucun certificat ; un tel seuil existe en principe |
| Artefact A1 : poids appris en ligne | non valide | **ne tient pas** | 0,999 à 1,000 dans les deux bancs |
| Artefact A2 : poids ajustés sur une moitié | non valide | **ne tient pas** | 0,19 à 0,64 dans mon banc ; 0,20 à 0,58 dans le sien |

## 12. Réserves, et ce que je n'ai pas fait

1. Banc simplifié, comme celui de l'auteur : un seul espace de mondes (3 issues, 2 traits, 2 sous-populations), une seule
   famille de découvertes plus une variante ; les taux absolus ne se transportent pas au juge. Les membres ordinaires du v8
   (moyennes glissantes) ne sont nulle part ; les membres log-linéaires ne sont que dans le bras « complet approché ».
2. Le code réel du v9 n'est pas exécuté (consigne). Mon « v9 » est la même classe, résolue par un autre optimiseur.
3. Ma décision au seuil laisse quelques couples (monde, instant) indécis (au plus 5 par bras et par cas) ; les lectures de
   taille les comptent promus.
4. La carte « tout ou rien » lit le plan : pire cas de la preuve, pas un proposeur réel.
5. La lecture dense est à 40 instants, sur 1 000 mondes par dose. La règle « membre par membre » n'est éprouvée que sur ce
   banc ; sa preuve tient en trois lignes mais n'a pas été contre-lue.
6. Méthode 6 non refaite par un programme à moi ; méthodes 10 et 12 non mesurées.
7. Incident : mes premiers rejeux ont écrit un dossier `__pycache__` dans le dossier de l'auteur (deux fichiers de cache
   Python, ignorés par git). Je l'ai retiré et j'ai relancé avec `-B`. Aucun fichier de l'auteur n'a changé : ses neuf
   empreintes et celles de ses 94 tranches sont revérifiées après mes courses.
8. Références de méthode, à vérifier sur pièce, aucun chiffre repris : inégalité de Ville pour les surmartingales positives ;
   test de Monte-Carlo à rang exact.

**Fichiers écrits** (tous scellés, compagnon `.sha256` à côté) :

| fichier | sha256 |
|---|---|
| `attaque_libre_v1.py` | `722fca3346b165041395e182d9e37de62a403e5acfd902219b8c4206c68c5a5b` |
| `sortie-attaque-libre-v1.json` (297 lots fusionnés, décisions monde par monde, graines) | `105bf4c2c90a178861c2e8542bade8fb8cb4746b765ef52c6aa3482438767090` |
| `attaque_libre_lecture_dense_v1.py` | `cbb5601430b5bf004400e87c0cdd9a698b5ced96203bf782f26953a267934fa0` |
| `sortie-attaque-libre-lecture-dense-v1.json` (28 lots fusionnés) | `c9d0756232aa74772d45bc7ac9ae11e92ffcb9bcc324d6c523681ba854ea5bea` |
| `refutation-libre-v1.md` | voir son compagnon |
