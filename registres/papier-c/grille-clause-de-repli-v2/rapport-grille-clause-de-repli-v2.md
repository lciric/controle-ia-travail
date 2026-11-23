# Rapport de la grille de la clause de repli — stabilité de rang du papier C (C-P3a, C-P3b, C-P3c) — v2

Date : 2026-11-22. Auteur : agent neuf (Claude Opus 5.5), qui n'est rédacteur d'aucune version du préenregistrement
du papier C ni du rapport v1, sur la consigne scellée
`registres/papier-c/grille-clause-de-repli-v2/consigne-agent-grille-v1.md` (`37ee2527…`, vérifiée). Données
simulées seulement, tout sur processeur, aucune dépense ; aucun résultat d'expérience lu (rien sous `diag/`, `runs/`,
`donnees/`, `docs/verdicts/`). Mesure de conception, jamais un résultat. Ce rapport est celui que demande le verrou 10
du texte ; il couvre la **liste finie entière** pour les trois lignes. Il doit encore être contre-lu par un autre
modèle (condition de la clause) : **l'auteur de ce rapport est Opus 5.5 ; le contre-lecteur doit donc être d'un autre
modèle que lui** (le contre-lecteur de v1 était Opus 5.5, l'auteur de v1 Fable 5.2).

Dossier : `registres/papier-c/grille-clause-de-repli-v2/` (noté `./` ci-dessous).

## 1. Constat par ligne (mécanique)

Seuil de la clause : 0,05 + 2 × √(0,05 × 0,95 / R) ; « au-dessus » = strictement au-dessus ; première passe seule ;
aucune correction pour le nombre de cases (règles de lecture du rapport, texte c5).

| ligne | cases couvertes / liste | effectif | seuil | plus haut taux (case) | cases au-dessus du seuil |
|---|---|---|---|---|---|
| C-P3a | 144 / 144 | R = 1 000, 1 000 tirages | 0,0638 | 0,049 (case 005 : E30, g = 0, k = 5, T = 45) | 0 |
| C-P3b | 144 / 144 | R = 1 000, 1 000 tirages | 0,0638 | 0,056 (case 097 : KH, g = 0,10, k = 3, T = 30) | 0 |
| C-P3c, bras « insertion » | 144 / 144 | R = 8 000 | 0,0549 | 0,107 (case 111 : MH, g = 0, k = 3, T = 60) | 82 |
| C-P3c, bras « contenu » | 108 / 108 | R = 8 000 | 0,0549 | 0,095 (case 003 : E30, g = 0, k = 3, T = 60) | 50 |

C-P3c : 84 cases distinctes ont au moins un bras au-dessus du seuil. Liste des cases au-dessus : section 6.2.

**Ce que le texte appelle l'issue, par ligne, dit comme un constat** (bloc de la stabilité de rang, « Trois issues ») :
le rapport couvre la liste finie pour les trois lignes (garde de complétude saine, section 5) ;
- **C-P3a : issue 1, « la clause ne joue pas pour la ligne C-P3a »** (aucune case au-dessus du seuil) ;
- **C-P3b : issue 1, « la clause ne joue pas pour la ligne C-P3b »** (aucune case au-dessus du seuil) ;
- **C-P3c : issue 2, « la clause joue pour la ligne C-P3c »** (au moins une case au-dessus du seuil, dans les deux bras).

Ce constat ne vaut, selon le texte, que si ce rapport est contre-lu par un autre modèle sans remarque bloquante
ouverte, ses corrections vérifiées par le même contre-lecteur, et cité au scellement par son chemin et son empreinte ;
sinon l'issue 3 (« rapport incomplet ») s'applique aux trois lignes. Il vaut aussi sous la condition d'appariement du
texte (section 8, limite L1). Je ne décide d'aucune version ; je constate.

## 2. Pièces et empreintes

| pièce | chemin | empreinte |
|---|---|---|
| consigne | `./consigne-agent-grille-v1.md` | `37ee252784a4e37c88283f2ff6bed4cbe016b564368c8bbabf75887f5701cacf` |
| texte (version c5) | `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c5.md` | `0747f357c30335ec7c37192be7b0d827bdcb4c6e3287c27c000c9d9ee2de723d` |
| erratum 1 de la version c5 | `registres/papier-c/redaction-brouillon7-relance-v1/erratum-1-version-c5-brouillon7-relance-v1.md` | `78cc112718c516bfc30cbe1325ec0bb101c2ae87b6344f5d49395b85f5c30930` |
| liste finie (copie ; original sous la racine C du 19 novembre) | `./entrees/liste-finie-cases-grille-v1.md` | `0c62072c8fe7ea76f0d3dbe190c0f994fb1aa8c58ca793dddf60f412bf5bfb94` |
| rapport v1 (racine C) | `C/registres/papier-c/redaction-brouillon6-relance-v1/grille/rapport-grille-clause-de-repli-v1.md` | `8d1616fce0dc59ea6bd986e465ae24efd845e1db7954cb39d39399fbc1a6ea89` |
| manifeste des programmes de v1 figés avant lancement (racine C) | `…/grille/sha256sums-programmes-avant-lancement.txt` | `c5bc961a81041bc680806c8387a9fea243cc6fe4d070d0cb6f20aae5bd0a47b6` |
| manifeste des sorties de v1 (racine C) | `…/grille/sha256sums-sorties-v1.txt` | `9ab5c8a8ef8426e6f4f256957f9fa3f886f214139a955845465d372de2988048` |
| contre-lecture de v1 (racine C) | `…/contre-lecteur-grille/rapport-contre-lecture-grille-clause-de-repli-v1.md` | `d0485a406d0b13b97e2141d42a401e93b026a3a3953b35fe2561ba3848788819` |
| programmes v2 figés avant le premier lancement | `./sha256sums-programmes-avant-lancement-v2.txt` | `a91545e5b7db779293e69d220e364476090048db887b0d42368ce7df2fba800f` |
| archive (fonctions reprises de v1, configuration brouillon 3) | `./sha256sums-archive-v2.txt` | `1d203e8b945c95cc8df850a0cba764714cd779666c48122bd04afb0cae7e56f8` (égale au manifeste d'archive de v1) |
| entrées figées avant lancement (liste, cases à jouer, reprises) | `./sha256sums-entrees-avant-lancement-v2.txt` | `c239c4ce2dfef2c8887c741cb09e834bd8f913680cebf0c08bf381daeb6da14f` |
| programme de mise en tables, figé avant lecture de tout taux neuf | `./sha256sums-programme-resume-v2.txt` | `9371bfbcf9c9a6b7c0ea3ac3d89aecfe21bf5c6824131d0f569449fb12307e53` |
| manifeste du lot | `./manifestes/manifeste-lot-v2.json` | `35dd3d01f90107344b2f16792c114011a6307d5b55f48c64fec81ae975a998a2` |
| manifeste de la mesure du temps | `./manifestes/manifeste-mesure-temps-v2.json` | `777eb92fd44f19dc0915b772b7cdb1f0248fba3ba3018a30e6612ae4ff6041fd` |
| tables (sortie de `resume_v2.py`) | `./tables-grille-v2.md`, `./resume-grille-v2.json` | compagnons `.sha256` |
| sorties de toutes les cases | `./sorties/reprises-v1/`, `./sorties/neuves-v2/` | `./sha256sums-sorties-v2.txt` (compagnon) |

Racine C = `/tmp/claude-0/-home-user-controle-ia-travail/61e4d11a-8d28-5a5e-8f56-9a6c1ff76fbf/scratchpad/c19b`
(copie hors du dépôt des pièces du 19 novembre). Toutes les empreintes de v1 citées ont été revérifiées
(`sha256sum -c`) : programmes, archive, 198 sorties et leurs manifestes conformes.

Commit du dépôt au lancement : `8069d631a803767f22fc277160b850e39b237e9a` (branche `prep/papier-c-prereg-fable-v1`) ;
arbre non propre (fichiers neufs de cet agent sous `./`, aucun commit permis), écrit au manifeste.

## 3. Ce qui vient de v1 et ce qui est neuf

**Cases manquantes avant lancement** (programme `liste_et_garde_v2.py inventaire-v1`, sortie
`./entrees/inventaire-v1-sortie.txt`), en comparant la table de la liste finie aux sorties de passe 0 de v1 : chaque
sortie est reprise seulement si elle est la première passe de la case, aux paramètres, au modèle d'erreur, au gain et
à l'effectif fixés par le texte (C-P3a et C-P3b : R = 1 000, 1 000 tirages ; C-P3c : R = 8 000), avec un fichier
d'erreurs vide.

| ligne | reprises de v1 | neuves (v2) | cases à jouer (numéros de la liste) |
|---|---|---|---|
| C-P3a et C-P3b (une sortie commune) | 86 | 58 | les 48 cases à T = 30 et 10 cases E40 à T = 45 ou 60 : 021, 023, 024, 026, 027, 029, 032, 033, 035, 036 (dont les quatre à g = 0,20) — liste complète : `./entrees/cases_ab_a_jouer_v2.txt` |
| C-P3c (les deux bras dans une sortie) | 96 | 48 | les 48 cases à T = 30 — `./entrees/cases_c_a_jouer_v2.txt` |

Le décompte du texte (58 et 48) est confirmé ; aucun écart à la colonne « jouée » de la liste finie. Les six sorties
d'effet de v1 (P3, P6) sont hors liste et non reprises ; les deux sorties de la passe 1 de v1 ne sont pas reprises
(règle (i) : seule compte la première passe ; elles restent une information de v1).

**Pourquoi les 182 sorties reprises satisfont la liste et le texte.** Paramètres, modèle d'erreur, gain, effectif et
passe vérifiés par programme ; empreintes égales au manifeste des sorties de v1. Trois règles du texte c5, postérieures
aux programmes de v1, ne sont pas codées par eux ; elles ne changent rien sur ces sorties :
- règle (iii), C-P3c, « un essai où D₀ ≤ 0 chez un juge compte « non établie », et sa part est rapportée » : v1 ne la
  code pas. Dans le modèle de la liste, S_t − H_t = 2 + (r_S − r_H) + (e_S − e_H) est gaussien de variance
  2 × 0,8² + 2 s₀² (l'effet de tâche s'annule), donc D₀ est gaussien exact, de moyenne 2 et d'écart type au plus
  √(2/45) = 0,211 dans les cases reprises (T ≥ 45, s₀ ≤ 0,6) : P(D₀ ≤ 0) ≤ Φ(−9,49) ≈ 1,2 × 10⁻²¹ par juge et par
  essai, soit moins de 3 × 10⁻¹⁵ sur les 96 cases × 8 000 essais × 3 juges. La part est donc 0 hors d'un événement
  de probabilité négligeable ; dans les cases neuves, elle est comptée : **0 essai sur 48 × 8 000** ;
- précision 8 (rangs moyens, τ de Kendall forme b) : les programmes emploient des rangs ordinaux et le τ forme a. Les
  deux coïncident en l'absence d'égalités ; Ḡ et les gains d'écart sont continus, une égalité exacte a une probabilité
  nulle hors des bras « contenu » sous K16 et KH, que la liste déclare non définis. Compté dans les cases neuves :
  **0 essai avec égalité** (C-P3a et C-P3b, Ḡ observés et écarts tirés, corpus A et B ; C-P3c, quatre évaluateurs) ;
  dans les reprises de C-P3c, le compteur de v1 donne **0 essai avec ex æquo** ;
- précision 5 (tirage non fini au numérateur d'une valeur p) : la forme fermée divise par Σ (c − X_i)², strictement
  positif sauf si toutes les X_i sont égales ; compté dans les cases neuves : **0 essai avec Ḡ non fini**.

Pour les cases neuves à T = 45 et 60 (dix cases E40 de C-P3a et C-P3b), la graine est celle que v1 aurait dérivée.

## 4. Changements de programme (R12)

Programmes de v1 copiés sans modification sous `./programmes/` (`grille_commun_v1.py`, `grille_ab_v1.py`,
`grille_c_v1.py`, empreintes égales). Ils ne jouaient pas tels quels les cases manquantes ; copies neuves :

1. **`grille_commun_v2.py`** — une seule différence de calcul : `identifiant_case` code T par {45 : 0, 60 : 1, 30 : 2}
   au lieu de « 0 si T = 45, sinon 1 ». **Pourquoi** : sous la règle de v1, chaque case à T = 30 aurait reçu la graine
   de la case à T = 60 de mêmes modèle, attaque et k (deux cases, une graine : contraire à R9, flux de hasard corrélés
   entre cases). Pour T = 45 et 60 l'identifiant est inchangé ; tout autre T lève une erreur. Identifiants injectifs
   sur la liste (code T < 10).
2. **`grille_ab_v2.py`** — importe `grille_commun_v2` ; compteurs de contrôle (Ḡ non finis, égalités exactes),
   calculés sans tirage ; aucun changement de règle ni de flux de hasard.
3. **`grille_c_v2.py`** — importe `grille_commun_v2` ; **règle (iii) codée** : D₀ de chaque juge recalculé sur ses
   lectures v₀ (sans tirage) ; un essai où D₀ ≤ 0 chez un juge compte « non établie » dans tous les bras qui emploient
   D₀, et son nombre est écrit ; compteur de Ḡ non finis. Aucun changement de flux de hasard.
4. Programmes neufs, sans calcul de simulation : `liste_et_garde_v2.py` (lecture de la liste, inventaire, garde de
   complétude), `essais_garde_v2.py`, `lancer_v2.sh`, `mesure_temps_v2.sh`, `manifeste_v2.py`, `resume_v2.py` (mise en
   tables). Les différences 1 à 3 sont écrites en tête de chaque fichier.

Empreintes figées et scellées à 20:28:11 UTC, avant le premier lancement ; contrôlées conformes après le lot. Le
programme de tables a été écrit pendant le lot, essayé sur des sorties synthétiques, figé et scellé à 20:29:46 UTC,
avant la lecture de tout taux neuf. **Aucun programme n'a changé après la lecture d'un taux.**

## 5. Garde de complétude (R5) et autres contrôles

- **Garde** (`liste_et_garde_v2.verifier_completude`) : chaque case de la liste finie présente une fois et une seule,
  par ligne et par bras, en première passe à l'effectif fixé ; toute sortie hors liste, non conforme ou en double est
  une erreur ; un `.err` non vide est une erreur. Essais (`essais_garde_v2.py`, sorties synthétiques construites sur
  la liste, taux nuls) : cas sain « saine » (144 / 144 / 108) ; artefact 1, une case manquante (034, C-P3a et C-P3b)
  « échec » ; artefact 2, une case en double (001, C-P3c) « échec » ; artefact 3, effectif réduit (002, R = 4 000)
  « échec » ; artefact 4, bras « contenu » absent (109) « échec ». **Sur les sorties réelles** : « SAINE »,
  C-P3a et C-P3b 144 / 144, C-P3c insertion 144 / 144, C-P3c contenu 108 / 108
  (`./journal/garde-completude-sorties-reelles-v2.txt`). Le programme de tables refuse de s'exécuter si la garde
  échoue (essayé : refus sur une sortie retirée).
- **Liste contre programmes** : `lire_liste` vérifie 144 cases = 8 × 3 × 2 × 3, et que les triplets (s₀ ; σ ; κ) de
  chaque modèle de la liste sont ceux des programmes.
- **Seuil** : le seuil écrit dans chaque sortie est comparé au seuil du texte pour son R (0,063784 ; 0,054873).
- **Pannes** : aucune ; 106 fichiers d'erreurs vides ; aucune relance.
- **Cohérence avec v1** : sur les cases reprises, les décomptes au-dessus du seuil (C-P3c : 54 sur 96 dans le bras
  « insertion », 32 sur 72 dans le bras « contenu ») sont ceux du rapport v1.

## 6. Résultats

Taux de « établie » aux trois lectures jointes (règle du texte), sous la lecture de la précision 37 (C-P3a et C-P3b
toujours lues ; C-P3c : seule la règle sur D₀). Le tableau par case complet est en annexe A (sortie de `resume_v2.py`,
copiée telle quelle).

### 6.1 C-P3a et C-P3b

| ligne | reprises de v1 (86) | neuves (58) | ensemble (144) | au-dessus de 0,0638 |
|---|---|---|---|---|
| C-P3a | 0,003 à 0,049 | 0,003 à 0,048 | 0,003 à 0,049 | 0 |
| C-P3b | 0,009 à 0,053 | 0,015 à 0,056 | 0,009 à 0,056 | 0 |

**Marge, écrite comme un résultat gênant (R4).** C-P3a est partout sous le seuil d'au moins deux erreurs de
Monte-Carlo. C-P3b ne l'est pas dans trois cases (taux + 2 erreurs ≥ 0,0638), toutes sous la compression seule :
074 (K16, g = 0, k = 3, T = 45 ; 0,053 ± 0,007, v1), 093 (KH, g = 0, k = 3, T = 60 ; 0,051 ± 0,007, v1) et
**097 (KH, g = 0,10, k = 3, T = 30 ; 0,056 ± 0,007, neuve), le plus haut taux de C-P3b**. Sous la compression seule,
C-P3b est proche du niveau nominal 0,05 (K16 : 0,032 à 0,053 ; KH : 0,019 à 0,056) : sur une autre graine, une de ces
cases pourrait passer le seuil. Le texte ne lit que la première passe et ne permet aucun rejeu pour lever ou créer un
dépassement ; je n'ai rien rejoué. À un niveau vrai de 0,05, environ 2 % des cases passeraient le seuil par le seul
hasard ; l'absence de dépassement dans 144 cases n'est pas « trop propre » ici, parce que la plupart des taux sont
nettement sous 0,05 (la conjonction des trois lectures est conservatrice), mais elle tient à peu dans la région de la
compression seule.

Taux par modèle et attaque (étendue sur les six couples k × T) :

| modèle | g | C-P3a | C-P3b |
|---|---|---|---|
| E30 | 0 / 0,10 / 0,20 | 0,027–0,049 / 0,015–0,025 / 0,003–0,017 | 0,028–0,046 / 0,019–0,028 / 0,016–0,040 |
| E40 | 0 / 0,10 / 0,20 | 0,025–0,040 / 0,010–0,026 / 0,007–0,016 | 0,038–0,048 / 0,020–0,038 / 0,015–0,027 |
| E60 | 0 / 0,10 / 0,20 | 0,028–0,042 / 0,021–0,026 / 0,006–0,017 | 0,034–0,048 / 0,019–0,044 / 0,009–0,029 |
| EH | 0 / 0,10 / 0,20 | 0,024–0,040 / 0,008–0,023 / 0,004–0,009 | 0,030–0,042 / 0,022–0,033 / 0,012–0,023 |
| K16 | 0 / 0,10 / 0,20 | 0,027–0,043 / 0,020–0,035 / 0,020–0,029 | 0,038–0,053 / 0,032–0,049 / 0,033–0,045 |
| KH | 0 / 0,10 / 0,20 | 0,024–0,043 / 0,016–0,031 / 0,012–0,027 | 0,033–0,051 / 0,025–0,056 / 0,019–0,038 |
| MH | 0 / 0,10 / 0,20 | 0,029–0,037 / 0,013–0,019 / 0,011–0,019 | 0,029–0,040 / 0,022–0,031 / 0,023–0,040 |
| M616 | 0 / 0,10 / 0,20 | 0,032–0,046 / 0,014–0,029 / 0,004–0,019 | 0,036–0,047 / 0,021–0,032 / 0,016–0,034 |

### 6.2 C-P3c

| bras | reprises de v1 | neuves (T = 30) | ensemble | au-dessus de 0,0549 |
|---|---|---|---|---|
| insertion | 0,026 à 0,107 ; 54 sur 96 | 0,031 à 0,096 ; 28 sur 48 | 0,026 à 0,107 | **82 sur 144** |
| contenu | 0,026 à 0,095 ; 32 sur 72 | 0,030 à 0,089 ; 18 sur 36 | 0,026 à 0,095 | **50 sur 108** |

Cases au-dessus, bras « insertion » : 001 à 010, 012, 019 à 027, 030, 037 à 043, 045 à 048, 055 à 061, 091 à 132, 134.
Bras « contenu » : 001 à 009, 012, 019 à 027, 037 à 043, 045 à 047, 055 à 061, 109 à 114, 127 à 133, 135.

Nombre de cases au-dessus par modèle et attaque (sur six ; insertion / contenu) :

| modèle | g = 0 | g = 0,10 | g = 0,20 |
|---|---|---|---|
| E30 | 6 / 6 | 5 / 4 | 0 / 0 |
| E40 | 6 / 6 | 4 / 3 | 0 / 0 |
| E60 | 6 / 6 | 5 / 4 | 0 / 0 |
| EH | 6 / 6 | 1 / 1 | 0 / 0 |
| K16 | 0 / non défini | 0 / non défini | 0 / non défini |
| KH | 6 / non défini | 6 / non défini | 6 / non défini |
| MH | 6 / 6 | 6 / 0 | 6 / 0 |
| M616 | 6 / 6 | 1 / 2 | 0 / 0 |

Les cases neuves à T = 30 suivent le même dessin que les cases de v1 : sans attaque, tous les modèles où v₀ porte une
erreur passent le seuil dans les deux bras (S et D₀ partagés entre les deux gains d'écart, premier mécanisme de v1) ;
sous la compression hétérogène (KH, MH), le bras « insertion » passe à tout g (second mécanisme, qui dépend de
l'hypothèse G4) ; sous K16, rien. Les dépassements sans attaque (hors K16) sont nets : 0,076 au moins dans le bras « insertion » (case
131), 0,077 au moins dans le bras « contenu » (case 037), plus de sept erreurs de Monte-Carlo au-dessus du seuil. Près
du seuil, à moins de deux erreurs de part et d'autre : 24 cases du bras « insertion » et 25 du bras « contenu »,
presque toutes à g = 0,10 (exceptions : 073, K16 sans attaque, bras « insertion », 0,050 ; 014 et 032, g = 0,20, bras
« contenu », 0,051 et 0,050, sous le seuil). Elles ne changent pas l'issue, que fixent les cases sans attaque : la
clause demande une case.

Part des essais où D₀ ≤ 0 : 0 dans les 48 cases neuves (comptée) ; négligeable dans les reprises (section 3).

**Pour information, hors liste** (sauf sous la version (b), où l'étape (1) du repli lit les cases de C-P3c aux deux
premières lectures jointes) : aux deux premières lectures, bras « insertion » 0,032 à 0,337 (case 126, MH, g = 0,20),
90 cases sur 144 au-dessus de 0,0549 ; bras « contenu » 0,033 à 0,095, 71 sur 108.

## 7. Remarques de la contre-lecture du rapport v1 (`d0485a40…`)

| remarque | gravité | ce que le texte en a fait | ce que le rapport v2 en fait |
|---|---|---|---|
| CG-01 « grille entière » indécidable | bloquante | liste finie de 144 cases écrite au texte (« la grille entière » = cette liste, ni plus ni moins) | couvre la liste entière, pour les trois lignes et les deux bras ; garde de complétude saine (section 5) |
| CG-02 C-P3c dépend de la lecture des tirages dégénérés | majeure | précision 37 : ĉ hors bornes ne touche pas C-P3c ; seul D₀ la rend non identifiable ; décision GO-2026-11-22-125 | joué sous cette lecture ; règle (iii) sur D₀ codée dans les cases neuves, bornée dans les reprises (section 3) ; la lecture (ii) de v1 n'est plus celle du texte et n'est pas jouée |
| CG-03 lever A6 avant le scellement | majeure | levée par la précision 37 (C-P3a et C-P3b toujours lues) | jouée telle quelle (taux « conj3 », lecture (i) de v1) ; la lecture n'est pas jugée ici |
| CG-04 conclusion de C-P3c trop large | majeure | modèle des gains d'écart adopté du rapport v1 (deux bras, tous deux dans la liste) | constat borné aux cases de la liste et au modèle adopté ; G5 (aucun effet juge × tâche) reste une hypothèse qui atténuerait le premier mécanisme (limite L3) |
| CG-05 passe 1 inutile à la lettre | mineure | règle (i) : seule la première passe compte | lecture sur la première passe ; passe 1 de v1 non reprise ; aucune seconde passe en v2 |
| CG-06 le nombre d'essais déplace le seuil | mineure | R fixé par ligne (1 000 et 1 000 tirages ; 8 000) | respecté dans toutes les cases (contrôlé par la garde) |
| CG-07 T = 30 absent | mineure | T = 30 ajouté à la liste | les 48 cases à T = 30 jouées pour chaque ligne |
| CG-08 longueurs de la configuration brouillon 3 | mineure | configuration citée (`85173b22…`) ; contrôle d'appariement au scellement ; rejeu si différent, sinon issue 3 | joué sur ces longueurs (archive, empreinte égale) ; le contrôle sur la configuration à sceller n'est pas fait ici (limite L1) |
| CG-09 libellé « erreur sur v₀ seule » | mineure | liste : « erreur d'insertion, la même sur v₀ et sur les insertions (s₀ = σ) » | libellé de la liste repris |
| CG-10 marge de C-P3b sous la compression | mineure | liste finie ; les quatre cases du contre-lecteur hors liste | marge mesurée sur la liste entière et écrite comme résultat gênant (section 6.1) ; cases du contre-lecteur non reprises |
| CG-11 dépassement du budget de calcul | mineure | — | durée écrite (section 9) ; sous la borne de 8 heures de la consigne |
| CG-12 paraphrase du mandat et texte | mineure | le texte suit le registre (« sinon (b) ») | rien à faire ici |
| CG-13 écart 0,186 / 0,227 | mineure | — | hors liste (lecture calibrée seule) ; rien à faire ici |
| CG-14 C-P3c sans p centré | mineure | non retenu (note pour une version future, sur nœud) | statistique jouée telle qu'écrite |

## 8. Écarts et limites

**Écarts de procédure, déclarés.**
- E1. Calcul par `/usr/local/bin/python3` (python 3.13.18, numpy 2.5.3), l'interpréteur et les versions des sorties
  de v1, et non par `.venv` (numpy 2.4.6) : la grille entière est ainsi jouée sous une seule version de numpy.
  `.venv` (`PYTHONPATH=src`) sert au scellement ; le manifeste emprunte `config_canonique` et `versions` du module du
  dépôt sous l'interpréteur du calcul.
- E2. Manifestes écrits par `manifeste_v2.py`, non par `creer_manifeste` : celui-ci écrit sous `runs/` (interdit à
  cet agent) et dérive les graines du nom des tâches, alors que les programmes gardent la règle de graines de v1. Les
  champs sont ceux de R9 (configuration et empreinte, versions, graines avec leur état de contrôle, commit, commande,
  réserve d'arbre non propre).
- E3. J'ai lu les taux de v1 (rapport v1, pièce que la consigne fait lire) avant d'écrire les programmes v2. Les
  changements sont mécaniques (identité de graine, règle (iii) du texte, compteurs) et ne dépendent d'aucun taux ;
  aucun taux neuf n'a été lu avant le figement de tous les programmes.
- E4. Deux exécutions qui ne sont pas des cases : un essai de fumée (2 essais, graine de passe 8, sortie hors du
  dossier, non lue hors des champs de contrôle) avant le figement, et la mesure du temps (passe 9, graines distinctes
  de toute case, seules les durées lues ; sorties gardées sous `./mesure-temps/`).
- E5. Pièces du 19 novembre copiées dans le dépôt, sous `./` seulement (liste finie, programmes et archive de v1,
  182 sorties reprises avec leurs compagnons) : le rapport s'appuie sur des fichiers versables ; empreintes égales.
- E6. Deux contrôles `sha256sum -c` lancés d'abord depuis le mauvais dossier (« FAILED open or read »), refaits depuis
  le bon : conformes. Sans effet.

**Limites.**
- L1. Appariement des témoins joué sur les longueurs de `papier-C-config-v1-brouillon3.json` (`85173b22…`), comme la
  liste le fixe. Le contrôle par programme sur la configuration à sceller, que le texte demande au scellement, n'est
  pas fait ici ; s'il diffère, la liste est à rejouer, sinon l'issue 3 s'applique.
- L2. Précision 37, C-P3c : la règle « D₀* ≤ 0 dans plus de 1 % des tirages » ne se simule pas ici (la grille de
  C-P3c ne fait aucun tirage, comme en v1) ; la liste la remplace par la règle (iii) par essai. Avec D₀ à plus de
  7,7 écarts types de 0 dans toutes les cases (T = 30, s₀ = 0,6), le cas est hors d'atteinte.
- L3. Modèle de la liste : erreurs indépendantes entre juges, cellules et tâches (G5 de v1) ; aucun effet juge ×
  tâche, aucune compression non linéaire, aucun effet de longueur, aucun bord d'échelle. Un effet juge × tâche
  atténuerait le premier mécanisme de C-P3c (CG-04).
- L4. Le second mécanisme de C-P3c (KH, MH à g > 0) ne vaut que dans le bras « insertion » ; le premier (sans attaque,
  sous erreur sur v₀) vaut dans les deux bras et suffit à l'issue de C-P3c.
- L5. Pas de contrôle sur artefact rejoué en v2 pour C-P3a et C-P3b (« l'instrument voit un taux haut ») : ceux de
  v1 (effet vrai : 0,945 et 0,970) portent sur les mêmes programmes de calcul, inchangés hors graine et compteurs.

## 9. Programmes, graines, manifestes, durée

- Graines (R9) : `numpy.random.SeedSequence(20261119, spawn_key = (programme, case, passe))`, programme 1 pour C-P3a
  et C-P3b, 2 pour C-P3c ; case = 1 000 × rang du modèle (E30 0, E40 1, E60 2, EH 3, K16 4, KH 5, MH 6, M616 7)
  + 100 × rang de l'attaque + 10 × k + code de T (45 : 0 ; 60 : 1 ; 30 : 2) ; passe 0. Écrites dans chaque sortie
  (champ `graine`) et au manifeste du lot avec leur état de contrôle (`generate_state(2)`).
- Lot : `bash programmes/lancer_v2.sh lot`, 4 processus ; C-P3c de 20:28:42 à 20:35:23 UTC, C-P3a et C-P3b de 20:35:23
  à 20:53:37 UTC : **25 minutes d'horloge** ; 1 528 s de processeur pour les 48 cases de C-P3c (28 à 36 s par case),
  4 234 s pour les 58 cases de C-P3a et C-P3b (61 à 90 s par case). Estimation préalable (mesure à 20:28) : environ
  6 200 s de processeur, 30 à 40 minutes d'horloge, sous la borne de 8 heures.
- Durée totale du travail : de 20:22 à 20:56 UTC. Journal : `./journal/journal-agent-grille-v2.md`.

## 10. Ce que j'ai lu en fait

- Dépôt : `CLAUDE.md` (fourni) ; la consigne ; le texte c5 : en-tête (lignes 1 à 11 par recherche), verrou 10
  (lignes 474 à 494), bloc de la stabilité de rang en entier (lignes 937 à 1069), Plan, section 8, chapeau et
  précisions 1 à 9 (lignes 1929 à 1978, dont 3, 5 et 8), précision 37 (lignes 2099 à 2143), et les lignes que des
  recherches par mots ont affichées ; Métrique, points 7 à 13 : non lus (non nécessaires) ; l'erratum 1 de la
  version c5 en entier ; `src/controle_ia/manifeste.py` en entier ; `etat_git` de `src/controle_ia/gardes.py` ;
  `sceller` et `verifier` de `src/controle_ia/scellement.py`.
- Racine C : la liste finie en entier ; le rapport v1 en entier ; les programmes de v1 (`grille_commun_v1.py`,
  `grille_ab_v1.py`, `grille_c_v1.py`, les deux lanceurs) ; l'archive (`commun_b5_v1.py` en entier ; fonctions de
  rang de `t2_rang_temoins_partages_v1.py`) ; la contre-lecture de v1 en entier ; les listes d'empreintes. Le rejeu
  du rédacteur (`…/redacteur/travail/rejeu-grille-c1/`) : non ouvert. Les sorties de v1 : lues par programme
  (paramètres pour l'inventaire, taux pour les tables).
- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun fichier « consigne-privee » ou « conception-ii-b » ;
  ni le dossier `…/scratchpad/c19`, ni les branches interdites. Aucune dépense, aucun appel réseau, aucun commit.

## Annexe A — tableau par case (sortie de `programmes/resume_v2.py`, copiée telle quelle)

Produites par `programmes/resume_v2.py` à partir des 144 + 144 sorties de première passe (garde de complétude saine). Taux de « établie » aux trois lectures jointes ± erreur de Monte-Carlo ; « **>** » : strictement au-dessus du seuil de la case (C-P3a et C-P3b : 0,0638, R = 1 000, B = 1 000 ; C-P3c : 0,0549, R = 8 000). Origine : v1 = sortie reprise du rapport v1 ; v2 = jouée pour ce rapport. D₀ ≤ 0 : essais où D₀ ≤ 0 chez un juge (comptés « non établie ») ; « — » : non compté par le programme de v1 (borne au rapport). Deux dernières colonnes : C-P3c aux deux premières lectures jointes, pour information (hors liste, sauf sous la version (b)).

| case | modèle | g | k | T | origine | C-P3a | C-P3b | origine | C-P3c insertion | C-P3c contenu | D₀ ≤ 0 | C-P3c insertion, deux lectures | C-P3c contenu, deux lectures |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 001 | E30 | 0 | 3 | 30 | v2 | 0,048 ± 0,007 | 0,046 ± 0,007 | v2 | 0,089 ± 0,003 **>** | 0,089 ± 0,003 **>** | 0 | 0,090 | 0,089 |
| 002 | E30 | 0 | 3 | 45 | v1 | 0,031 ± 0,005 | 0,036 ± 0,006 | v1 | 0,083 ± 0,003 **>** | 0,082 ± 0,003 **>** | — | 0,083 | 0,082 |
| 003 | E30 | 0 | 3 | 60 | v1 | 0,027 ± 0,005 | 0,038 ± 0,006 | v1 | 0,088 ± 0,003 **>** | 0,095 ± 0,003 **>** | — | 0,088 | 0,095 |
| 004 | E30 | 0 | 5 | 30 | v2 | 0,032 ± 0,006 | 0,041 ± 0,006 | v2 | 0,082 ± 0,003 **>** | 0,087 ± 0,003 **>** | 0 | 0,083 | 0,088 |
| 005 | E30 | 0 | 5 | 45 | v1 | 0,049 ± 0,007 | 0,041 ± 0,006 | v1 | 0,083 ± 0,003 **>** | 0,079 ± 0,003 **>** | — | 0,083 | 0,080 |
| 006 | E30 | 0 | 5 | 60 | v1 | 0,033 ± 0,006 | 0,028 ± 0,005 | v1 | 0,079 ± 0,003 **>** | 0,078 ± 0,003 **>** | — | 0,079 | 0,078 |
| 007 | E30 | 0,10 | 3 | 30 | v2 | 0,025 ± 0,005 | 0,023 ± 0,005 | v2 | 0,059 ± 0,003 **>** | 0,060 ± 0,003 **>** | 0 | 0,062 | 0,062 |
| 008 | E30 | 0,10 | 3 | 45 | v1 | 0,022 ± 0,005 | 0,024 ± 0,005 | v1 | 0,056 ± 0,003 **>** | 0,055 ± 0,003 **>** | — | 0,059 | 0,059 |
| 009 | E30 | 0,10 | 3 | 60 | v1 | 0,019 ± 0,004 | 0,023 ± 0,005 | v1 | 0,060 ± 0,003 **>** | 0,057 ± 0,003 **>** | — | 0,062 | 0,060 |
| 010 | E30 | 0,10 | 5 | 30 | v2 | 0,015 ± 0,004 | 0,019 ± 0,004 | v2 | 0,057 ± 0,003 **>** | 0,050 ± 0,002 | 0 | 0,060 | 0,052 |
| 011 | E30 | 0,10 | 5 | 45 | v1 | 0,020 ± 0,004 | 0,028 ± 0,005 | v1 | 0,052 ± 0,002 | 0,054 ± 0,003 | — | 0,055 | 0,057 |
| 012 | E30 | 0,10 | 5 | 60 | v1 | 0,016 ± 0,004 | 0,020 ± 0,004 | v1 | 0,057 ± 0,003 **>** | 0,056 ± 0,003 **>** | — | 0,060 | 0,059 |
| 013 | E30 | 0,20 | 3 | 30 | v2 | 0,017 ± 0,004 | 0,040 ± 0,006 | v2 | 0,047 ± 0,002 | 0,046 ± 0,002 | 0 | 0,051 | 0,049 |
| 014 | E30 | 0,20 | 3 | 45 | v1 | 0,012 ± 0,003 | 0,021 ± 0,005 | v1 | 0,048 ± 0,002 | 0,051 ± 0,002 | — | 0,052 | 0,054 |
| 015 | E30 | 0,20 | 3 | 60 | v1 | 0,015 ± 0,004 | 0,023 ± 0,005 | v1 | 0,048 ± 0,002 | 0,046 ± 0,002 | — | 0,051 | 0,049 |
| 016 | E30 | 0,20 | 5 | 30 | v2 | 0,003 ± 0,002 | 0,020 ± 0,004 | v2 | 0,041 ± 0,002 | 0,040 ± 0,002 | 0 | 0,044 | 0,043 |
| 017 | E30 | 0,20 | 5 | 45 | v1 | 0,007 ± 0,003 | 0,020 ± 0,004 | v1 | 0,041 ± 0,002 | 0,040 ± 0,002 | — | 0,045 | 0,043 |
| 018 | E30 | 0,20 | 5 | 60 | v1 | 0,003 ± 0,002 | 0,016 ± 0,004 | v1 | 0,041 ± 0,002 | 0,042 ± 0,002 | — | 0,046 | 0,046 |
| 019 | E40 | 0 | 3 | 30 | v2 | 0,037 ± 0,006 | 0,038 ± 0,006 | v2 | 0,084 ± 0,003 **>** | 0,086 ± 0,003 **>** | 0 | 0,084 | 0,086 |
| 020 | E40 | 0 | 3 | 45 | v1 | 0,036 ± 0,006 | 0,048 ± 0,007 | v1 | 0,083 ± 0,003 **>** | 0,088 ± 0,003 **>** | — | 0,083 | 0,089 |
| 021 | E40 | 0 | 3 | 60 | v2 | 0,025 ± 0,005 | 0,042 ± 0,006 | v1 | 0,082 ± 0,003 **>** | 0,080 ± 0,003 **>** | — | 0,082 | 0,081 |
| 022 | E40 | 0 | 5 | 30 | v2 | 0,031 ± 0,005 | 0,048 ± 0,007 | v2 | 0,077 ± 0,003 **>** | 0,082 ± 0,003 **>** | 0 | 0,078 | 0,082 |
| 023 | E40 | 0 | 5 | 45 | v2 | 0,040 ± 0,006 | 0,039 ± 0,006 | v1 | 0,084 ± 0,003 **>** | 0,078 ± 0,003 **>** | — | 0,084 | 0,078 |
| 024 | E40 | 0 | 5 | 60 | v2 | 0,026 ± 0,005 | 0,042 ± 0,006 | v1 | 0,084 ± 0,003 **>** | 0,084 ± 0,003 **>** | — | 0,084 | 0,085 |
| 025 | E40 | 0,10 | 3 | 30 | v2 | 0,017 ± 0,004 | 0,020 ± 0,004 | v2 | 0,059 ± 0,003 **>** | 0,061 ± 0,003 **>** | 0 | 0,062 | 0,063 |
| 026 | E40 | 0,10 | 3 | 45 | v2 | 0,026 ± 0,005 | 0,031 ± 0,005 | v1 | 0,062 ± 0,003 **>** | 0,064 ± 0,003 **>** | — | 0,065 | 0,068 |
| 027 | E40 | 0,10 | 3 | 60 | v2 | 0,017 ± 0,004 | 0,029 ± 0,005 | v1 | 0,055 ± 0,003 **>** | 0,064 ± 0,003 **>** | — | 0,060 | 0,067 |
| 028 | E40 | 0,10 | 5 | 30 | v2 | 0,018 ± 0,004 | 0,038 ± 0,006 | v2 | 0,047 ± 0,002 | 0,053 ± 0,003 | 0 | 0,052 | 0,059 |
| 029 | E40 | 0,10 | 5 | 45 | v2 | 0,019 ± 0,004 | 0,029 ± 0,005 | v1 | 0,053 ± 0,003 | 0,053 ± 0,003 | — | 0,057 | 0,057 |
| 030 | E40 | 0,10 | 5 | 60 | v1 | 0,010 ± 0,003 | 0,033 ± 0,006 | v1 | 0,056 ± 0,003 **>** | 0,050 ± 0,002 | — | 0,059 | 0,053 |
| 031 | E40 | 0,20 | 3 | 30 | v2 | 0,013 ± 0,004 | 0,015 ± 0,004 | v2 | 0,045 ± 0,002 | 0,045 ± 0,002 | 0 | 0,049 | 0,049 |
| 032 | E40 | 0,20 | 3 | 45 | v2 | 0,016 ± 0,004 | 0,021 ± 0,005 | v1 | 0,048 ± 0,002 | 0,050 ± 0,002 | — | 0,052 | 0,056 |
| 033 | E40 | 0,20 | 3 | 60 | v2 | 0,007 ± 0,003 | 0,027 ± 0,005 | v1 | 0,048 ± 0,002 | 0,043 ± 0,002 | — | 0,051 | 0,047 |
| 034 | E40 | 0,20 | 5 | 30 | v2 | 0,010 ± 0,003 | 0,023 ± 0,005 | v2 | 0,040 ± 0,002 | 0,038 ± 0,002 | 0 | 0,046 | 0,043 |
| 035 | E40 | 0,20 | 5 | 45 | v2 | 0,012 ± 0,003 | 0,015 ± 0,004 | v1 | 0,042 ± 0,002 | 0,045 ± 0,002 | — | 0,046 | 0,052 |
| 036 | E40 | 0,20 | 5 | 60 | v2 | 0,008 ± 0,003 | 0,017 ± 0,004 | v1 | 0,037 ± 0,002 | 0,038 ± 0,002 | — | 0,042 | 0,044 |
| 037 | E60 | 0 | 3 | 30 | v2 | 0,037 ± 0,006 | 0,039 ± 0,006 | v2 | 0,080 ± 0,003 **>** | 0,077 ± 0,003 **>** | 0 | 0,082 | 0,078 |
| 038 | E60 | 0 | 3 | 45 | v1 | 0,028 ± 0,005 | 0,036 ± 0,006 | v1 | 0,088 ± 0,003 **>** | 0,089 ± 0,003 **>** | — | 0,089 | 0,089 |
| 039 | E60 | 0 | 3 | 60 | v1 | 0,036 ± 0,006 | 0,034 ± 0,006 | v1 | 0,082 ± 0,003 **>** | 0,088 ± 0,003 **>** | — | 0,082 | 0,088 |
| 040 | E60 | 0 | 5 | 30 | v2 | 0,039 ± 0,006 | 0,034 ± 0,006 | v2 | 0,079 ± 0,003 **>** | 0,078 ± 0,003 **>** | 0 | 0,080 | 0,079 |
| 041 | E60 | 0 | 5 | 45 | v1 | 0,042 ± 0,006 | 0,034 ± 0,006 | v1 | 0,081 ± 0,003 **>** | 0,080 ± 0,003 **>** | — | 0,081 | 0,080 |
| 042 | E60 | 0 | 5 | 60 | v1 | 0,040 ± 0,006 | 0,048 ± 0,007 | v1 | 0,076 ± 0,003 **>** | 0,082 ± 0,003 **>** | — | 0,078 | 0,083 |
| 043 | E60 | 0,10 | 3 | 30 | v2 | 0,021 ± 0,005 | 0,032 ± 0,006 | v2 | 0,056 ± 0,003 **>** | 0,058 ± 0,003 **>** | 0 | 0,060 | 0,062 |
| 044 | E60 | 0,10 | 3 | 45 | v1 | 0,021 ± 0,005 | 0,038 ± 0,006 | v1 | 0,055 ± 0,003 | 0,053 ± 0,003 | — | 0,060 | 0,058 |
| 045 | E60 | 0,10 | 3 | 60 | v1 | 0,023 ± 0,005 | 0,028 ± 0,005 | v1 | 0,059 ± 0,003 **>** | 0,056 ± 0,003 **>** | — | 0,064 | 0,061 |
| 046 | E60 | 0,10 | 5 | 30 | v2 | 0,026 ± 0,005 | 0,044 ± 0,006 | v2 | 0,056 ± 0,003 **>** | 0,055 ± 0,003 **>** | 0 | 0,061 | 0,062 |
| 047 | E60 | 0,10 | 5 | 45 | v1 | 0,024 ± 0,005 | 0,034 ± 0,006 | v1 | 0,058 ± 0,003 **>** | 0,058 ± 0,003 **>** | — | 0,064 | 0,064 |
| 048 | E60 | 0,10 | 5 | 60 | v1 | 0,022 ± 0,005 | 0,019 ± 0,004 | v1 | 0,057 ± 0,003 **>** | 0,051 ± 0,002 | — | 0,063 | 0,057 |
| 049 | E60 | 0,20 | 3 | 30 | v2 | 0,017 ± 0,004 | 0,029 ± 0,005 | v2 | 0,046 ± 0,002 | 0,043 ± 0,002 | 0 | 0,053 | 0,049 |
| 050 | E60 | 0,20 | 3 | 45 | v1 | 0,010 ± 0,003 | 0,022 ± 0,005 | v1 | 0,046 ± 0,002 | 0,048 ± 0,002 | — | 0,052 | 0,052 |
| 051 | E60 | 0,20 | 3 | 60 | v1 | 0,009 ± 0,003 | 0,020 ± 0,004 | v1 | 0,048 ± 0,002 | 0,046 ± 0,002 | — | 0,053 | 0,051 |
| 052 | E60 | 0,20 | 5 | 30 | v2 | 0,006 ± 0,002 | 0,020 ± 0,004 | v2 | 0,038 ± 0,002 | 0,040 ± 0,002 | 0 | 0,045 | 0,047 |
| 053 | E60 | 0,20 | 5 | 45 | v1 | 0,009 ± 0,003 | 0,009 ± 0,003 | v1 | 0,035 ± 0,002 | 0,036 ± 0,002 | — | 0,043 | 0,044 |
| 054 | E60 | 0,20 | 5 | 60 | v1 | 0,012 ± 0,003 | 0,020 ± 0,004 | v1 | 0,041 ± 0,002 | 0,039 ± 0,002 | — | 0,051 | 0,048 |
| 055 | EH | 0 | 3 | 30 | v2 | 0,038 ± 0,006 | 0,032 ± 0,006 | v2 | 0,086 ± 0,003 **>** | 0,087 ± 0,003 **>** | 0 | 0,087 | 0,088 |
| 056 | EH | 0 | 3 | 45 | v1 | 0,040 ± 0,006 | 0,035 ± 0,006 | v1 | 0,085 ± 0,003 **>** | 0,089 ± 0,003 **>** | — | 0,086 | 0,089 |
| 057 | EH | 0 | 3 | 60 | v1 | 0,024 ± 0,005 | 0,042 ± 0,006 | v1 | 0,087 ± 0,003 **>** | 0,091 ± 0,003 **>** | — | 0,087 | 0,091 |
| 058 | EH | 0 | 5 | 30 | v2 | 0,033 ± 0,006 | 0,034 ± 0,006 | v2 | 0,083 ± 0,003 **>** | 0,084 ± 0,003 **>** | 0 | 0,084 | 0,085 |
| 059 | EH | 0 | 5 | 45 | v1 | 0,034 ± 0,006 | 0,030 ± 0,005 | v1 | 0,080 ± 0,003 **>** | 0,078 ± 0,003 **>** | — | 0,081 | 0,079 |
| 060 | EH | 0 | 5 | 60 | v1 | 0,029 ± 0,005 | 0,038 ± 0,006 | v1 | 0,083 ± 0,003 **>** | 0,080 ± 0,003 **>** | — | 0,084 | 0,081 |
| 061 | EH | 0,10 | 3 | 30 | v2 | 0,017 ± 0,004 | 0,024 ± 0,005 | v2 | 0,056 ± 0,003 **>** | 0,057 ± 0,003 **>** | 0 | 0,060 | 0,062 |
| 062 | EH | 0,10 | 3 | 45 | v1 | 0,022 ± 0,005 | 0,029 ± 0,005 | v1 | 0,051 ± 0,002 | 0,051 ± 0,002 | — | 0,056 | 0,054 |
| 063 | EH | 0,10 | 3 | 60 | v1 | 0,023 ± 0,005 | 0,031 ± 0,005 | v1 | 0,046 ± 0,002 | 0,048 ± 0,002 | — | 0,052 | 0,052 |
| 064 | EH | 0,10 | 5 | 30 | v2 | 0,021 ± 0,005 | 0,033 ± 0,006 | v2 | 0,046 ± 0,002 | 0,045 ± 0,002 | 0 | 0,052 | 0,051 |
| 065 | EH | 0,10 | 5 | 45 | v1 | 0,016 ± 0,004 | 0,030 ± 0,005 | v1 | 0,047 ± 0,002 | 0,047 ± 0,002 | — | 0,053 | 0,052 |
| 066 | EH | 0,10 | 5 | 60 | v1 | 0,008 ± 0,003 | 0,022 ± 0,005 | v1 | 0,043 ± 0,002 | 0,041 ± 0,002 | — | 0,048 | 0,046 |
| 067 | EH | 0,20 | 3 | 30 | v2 | 0,009 ± 0,003 | 0,021 ± 0,005 | v2 | 0,040 ± 0,002 | 0,040 ± 0,002 | 0 | 0,046 | 0,048 |
| 068 | EH | 0,20 | 3 | 45 | v1 | 0,005 ± 0,002 | 0,023 ± 0,005 | v1 | 0,034 ± 0,002 | 0,033 ± 0,002 | — | 0,041 | 0,040 |
| 069 | EH | 0,20 | 3 | 60 | v1 | 0,006 ± 0,002 | 0,021 ± 0,005 | v1 | 0,035 ± 0,002 | 0,033 ± 0,002 | — | 0,041 | 0,038 |
| 070 | EH | 0,20 | 5 | 30 | v2 | 0,007 ± 0,003 | 0,018 ± 0,004 | v2 | 0,031 ± 0,002 | 0,032 ± 0,002 | 0 | 0,040 | 0,041 |
| 071 | EH | 0,20 | 5 | 45 | v1 | 0,004 ± 0,002 | 0,023 ± 0,005 | v1 | 0,029 ± 0,002 | 0,031 ± 0,002 | — | 0,037 | 0,038 |
| 072 | EH | 0,20 | 5 | 60 | v1 | 0,009 ± 0,003 | 0,012 ± 0,003 | v1 | 0,026 ± 0,002 | 0,026 ± 0,002 | — | 0,032 | 0,033 |
| 073 | K16 | 0 | 3 | 30 | v2 | 0,027 ± 0,005 | 0,039 ± 0,006 | v2 | 0,050 ± 0,002 | non défini | 0 | 0,050 | non défini |
| 074 | K16 | 0 | 3 | 45 | v1 | 0,043 ± 0,006 | 0,053 ± 0,007 | v1 | 0,041 ± 0,002 | non défini | — | 0,041 | non défini |
| 075 | K16 | 0 | 3 | 60 | v1 | 0,040 ± 0,006 | 0,049 ± 0,007 | v1 | 0,046 ± 0,002 | non défini | — | 0,046 | non défini |
| 076 | K16 | 0 | 5 | 30 | v2 | 0,033 ± 0,006 | 0,041 ± 0,006 | v2 | 0,041 ± 0,002 | non défini | 0 | 0,042 | non défini |
| 077 | K16 | 0 | 5 | 45 | v1 | 0,043 ± 0,006 | 0,038 ± 0,006 | v1 | 0,048 ± 0,002 | non défini | — | 0,048 | non défini |
| 078 | K16 | 0 | 5 | 60 | v1 | 0,037 ± 0,006 | 0,040 ± 0,006 | v1 | 0,045 ± 0,002 | non défini | — | 0,045 | non défini |
| 079 | K16 | 0,10 | 3 | 30 | v2 | 0,031 ± 0,005 | 0,043 ± 0,006 | v2 | 0,040 ± 0,002 | non défini | 0 | 0,040 | non défini |
| 080 | K16 | 0,10 | 3 | 45 | v1 | 0,021 ± 0,005 | 0,049 ± 0,007 | v1 | 0,043 ± 0,002 | non défini | — | 0,043 | non défini |
| 081 | K16 | 0,10 | 3 | 60 | v1 | 0,032 ± 0,006 | 0,047 ± 0,007 | v1 | 0,044 ± 0,002 | non défini | — | 0,044 | non défini |
| 082 | K16 | 0,10 | 5 | 30 | v2 | 0,031 ± 0,005 | 0,032 ± 0,006 | v2 | 0,040 ± 0,002 | non défini | 0 | 0,040 | non défini |
| 083 | K16 | 0,10 | 5 | 45 | v1 | 0,020 ± 0,004 | 0,036 ± 0,006 | v1 | 0,039 ± 0,002 | non défini | — | 0,039 | non défini |
| 084 | K16 | 0,10 | 5 | 60 | v1 | 0,035 ± 0,006 | 0,035 ± 0,006 | v1 | 0,037 ± 0,002 | non défini | — | 0,037 | non défini |
| 085 | K16 | 0,20 | 3 | 30 | v2 | 0,025 ± 0,005 | 0,033 ± 0,006 | v2 | 0,036 ± 0,002 | non défini | 0 | 0,036 | non défini |
| 086 | K16 | 0,20 | 3 | 45 | v1 | 0,024 ± 0,005 | 0,040 ± 0,006 | v1 | 0,036 ± 0,002 | non défini | — | 0,036 | non défini |
| 087 | K16 | 0,20 | 3 | 60 | v1 | 0,029 ± 0,005 | 0,045 ± 0,007 | v1 | 0,035 ± 0,002 | non défini | — | 0,035 | non défini |
| 088 | K16 | 0,20 | 5 | 30 | v2 | 0,024 ± 0,005 | 0,033 ± 0,006 | v2 | 0,041 ± 0,002 | non défini | 0 | 0,041 | non défini |
| 089 | K16 | 0,20 | 5 | 45 | v1 | 0,020 ± 0,004 | 0,034 ± 0,006 | v1 | 0,033 ± 0,002 | non défini | — | 0,033 | non défini |
| 090 | K16 | 0,20 | 5 | 60 | v1 | 0,021 ± 0,005 | 0,038 ± 0,006 | v1 | 0,034 ± 0,002 | non défini | — | 0,034 | non défini |
| 091 | KH | 0 | 3 | 30 | v2 | 0,037 ± 0,006 | 0,036 ± 0,006 | v2 | 0,088 ± 0,003 **>** | non défini | 0 | 0,088 | non défini |
| 092 | KH | 0 | 3 | 45 | v1 | 0,024 ± 0,005 | 0,040 ± 0,006 | v1 | 0,096 ± 0,003 **>** | non défini | — | 0,096 | non défini |
| 093 | KH | 0 | 3 | 60 | v1 | 0,033 ± 0,006 | 0,051 ± 0,007 | v1 | 0,101 ± 0,003 **>** | non défini | — | 0,101 | non défini |
| 094 | KH | 0 | 5 | 30 | v2 | 0,037 ± 0,006 | 0,042 ± 0,006 | v2 | 0,082 ± 0,003 **>** | non défini | 0 | 0,082 | non défini |
| 095 | KH | 0 | 5 | 45 | v1 | 0,038 ± 0,006 | 0,033 ± 0,006 | v1 | 0,094 ± 0,003 **>** | non défini | — | 0,094 | non défini |
| 096 | KH | 0 | 5 | 60 | v1 | 0,043 ± 0,006 | 0,034 ± 0,006 | v1 | 0,096 ± 0,003 **>** | non défini | — | 0,096 | non défini |
| 097 | KH | 0,10 | 3 | 30 | v2 | 0,031 ± 0,005 | 0,056 ± 0,007 | v2 | 0,077 ± 0,003 **>** | non défini | 0 | 0,077 | non défini |
| 098 | KH | 0,10 | 3 | 45 | v1 | 0,022 ± 0,005 | 0,036 ± 0,006 | v1 | 0,087 ± 0,003 **>** | non défini | — | 0,087 | non défini |
| 099 | KH | 0,10 | 3 | 60 | v1 | 0,020 ± 0,004 | 0,033 ± 0,006 | v1 | 0,099 ± 0,003 **>** | non défini | — | 0,099 | non défini |
| 100 | KH | 0,10 | 5 | 30 | v2 | 0,027 ± 0,005 | 0,025 ± 0,005 | v2 | 0,073 ± 0,003 **>** | non défini | 0 | 0,073 | non défini |
| 101 | KH | 0,10 | 5 | 45 | v1 | 0,016 ± 0,004 | 0,046 ± 0,007 | v1 | 0,079 ± 0,003 **>** | non défini | — | 0,079 | non défini |
| 102 | KH | 0,10 | 5 | 60 | v1 | 0,017 ± 0,004 | 0,043 ± 0,006 | v1 | 0,092 ± 0,003 **>** | non défini | — | 0,092 | non défini |
| 103 | KH | 0,20 | 3 | 30 | v2 | 0,012 ± 0,003 | 0,019 ± 0,004 | v2 | 0,073 ± 0,003 **>** | non défini | 0 | 0,075 | non défini |
| 104 | KH | 0,20 | 3 | 45 | v1 | 0,023 ± 0,005 | 0,038 ± 0,006 | v1 | 0,080 ± 0,003 **>** | non défini | — | 0,080 | non défini |
| 105 | KH | 0,20 | 3 | 60 | v1 | 0,023 ± 0,005 | 0,024 ± 0,005 | v1 | 0,091 ± 0,003 **>** | non défini | — | 0,092 | non défini |
| 106 | KH | 0,20 | 5 | 30 | v2 | 0,020 ± 0,004 | 0,026 ± 0,005 | v2 | 0,072 ± 0,003 **>** | non défini | 0 | 0,072 | non défini |
| 107 | KH | 0,20 | 5 | 45 | v1 | 0,024 ± 0,005 | 0,027 ± 0,005 | v1 | 0,077 ± 0,003 **>** | non défini | — | 0,078 | non défini |
| 108 | KH | 0,20 | 5 | 60 | v1 | 0,027 ± 0,005 | 0,033 ± 0,006 | v1 | 0,094 ± 0,003 **>** | non défini | — | 0,094 | non défini |
| 109 | MH | 0 | 3 | 30 | v2 | 0,029 ± 0,005 | 0,032 ± 0,006 | v2 | 0,096 ± 0,003 **>** | 0,087 ± 0,003 **>** | 0 | 0,099 | 0,090 |
| 110 | MH | 0 | 3 | 45 | v1 | 0,037 ± 0,006 | 0,039 ± 0,006 | v1 | 0,104 ± 0,003 **>** | 0,089 ± 0,003 **>** | — | 0,110 | 0,093 |
| 111 | MH | 0 | 3 | 60 | v1 | 0,034 ± 0,006 | 0,040 ± 0,006 | v1 | 0,107 ± 0,003 **>** | 0,083 ± 0,003 **>** | — | 0,110 | 0,085 |
| 112 | MH | 0 | 5 | 30 | v2 | 0,030 ± 0,005 | 0,029 ± 0,005 | v2 | 0,090 ± 0,003 **>** | 0,087 ± 0,003 **>** | 0 | 0,093 | 0,091 |
| 113 | MH | 0 | 5 | 45 | v1 | 0,035 ± 0,006 | 0,031 ± 0,005 | v1 | 0,104 ± 0,003 **>** | 0,082 ± 0,003 **>** | — | 0,109 | 0,085 |
| 114 | MH | 0 | 5 | 60 | v1 | 0,030 ± 0,005 | 0,035 ± 0,006 | v1 | 0,104 ± 0,003 **>** | 0,088 ± 0,003 **>** | — | 0,108 | 0,091 |
| 115 | MH | 0,10 | 3 | 30 | v2 | 0,019 ± 0,004 | 0,025 ± 0,005 | v2 | 0,086 ± 0,003 **>** | 0,054 ± 0,003 | 0 | 0,131 | 0,071 |
| 116 | MH | 0,10 | 3 | 45 | v1 | 0,016 ± 0,004 | 0,029 ± 0,005 | v1 | 0,091 ± 0,003 **>** | 0,051 ± 0,002 | — | 0,152 | 0,070 |
| 117 | MH | 0,10 | 3 | 60 | v1 | 0,013 ± 0,004 | 0,031 ± 0,005 | v1 | 0,106 ± 0,003 **>** | 0,050 ± 0,002 | — | 0,186 | 0,078 |
| 118 | MH | 0,10 | 5 | 30 | v2 | 0,015 ± 0,004 | 0,029 ± 0,005 | v2 | 0,076 ± 0,003 **>** | 0,048 ± 0,002 | 0 | 0,130 | 0,070 |
| 119 | MH | 0,10 | 5 | 45 | v1 | 0,015 ± 0,004 | 0,026 ± 0,005 | v1 | 0,092 ± 0,003 **>** | 0,041 ± 0,002 | — | 0,172 | 0,072 |
| 120 | MH | 0,10 | 5 | 60 | v1 | 0,017 ± 0,004 | 0,022 ± 0,005 | v1 | 0,098 ± 0,003 **>** | 0,041 ± 0,002 | — | 0,205 | 0,073 |
| 121 | MH | 0,20 | 3 | 30 | v2 | 0,011 ± 0,003 | 0,023 ± 0,005 | v2 | 0,088 ± 0,003 **>** | 0,038 ± 0,002 | 0 | 0,171 | 0,064 |
| 122 | MH | 0,20 | 3 | 45 | v1 | 0,019 ± 0,004 | 0,040 ± 0,006 | v1 | 0,093 ± 0,003 **>** | 0,030 ± 0,002 | — | 0,224 | 0,061 |
| 123 | MH | 0,20 | 3 | 60 | v1 | 0,014 ± 0,004 | 0,023 ± 0,005 | v1 | 0,098 ± 0,003 **>** | 0,029 ± 0,002 | — | 0,266 | 0,068 |
| 124 | MH | 0,20 | 5 | 30 | v2 | 0,017 ± 0,004 | 0,024 ± 0,005 | v2 | 0,078 ± 0,003 **>** | 0,030 ± 0,002 | 0 | 0,183 | 0,060 |
| 125 | MH | 0,20 | 5 | 45 | v1 | 0,018 ± 0,004 | 0,029 ± 0,005 | v1 | 0,088 ± 0,003 **>** | 0,029 ± 0,002 | — | 0,260 | 0,069 |
| 126 | MH | 0,20 | 5 | 60 | v1 | 0,015 ± 0,004 | 0,031 ± 0,005 | v1 | 0,099 ± 0,003 **>** | 0,028 ± 0,002 | — | 0,337 | 0,079 |
| 127 | M616 | 0 | 3 | 30 | v2 | 0,037 ± 0,006 | 0,047 ± 0,007 | v2 | 0,082 ± 0,003 **>** | 0,081 ± 0,003 **>** | 0 | 0,084 | 0,082 |
| 128 | M616 | 0 | 3 | 45 | v1 | 0,032 ± 0,006 | 0,037 ± 0,006 | v1 | 0,081 ± 0,003 **>** | 0,080 ± 0,003 **>** | — | 0,082 | 0,081 |
| 129 | M616 | 0 | 3 | 60 | v1 | 0,046 ± 0,007 | 0,041 ± 0,006 | v1 | 0,081 ± 0,003 **>** | 0,079 ± 0,003 **>** | — | 0,082 | 0,079 |
| 130 | M616 | 0 | 5 | 30 | v2 | 0,032 ± 0,006 | 0,036 ± 0,006 | v2 | 0,079 ± 0,003 **>** | 0,080 ± 0,003 **>** | 0 | 0,080 | 0,081 |
| 131 | M616 | 0 | 5 | 45 | v1 | 0,036 ± 0,006 | 0,040 ± 0,006 | v1 | 0,076 ± 0,003 **>** | 0,082 ± 0,003 **>** | — | 0,077 | 0,083 |
| 132 | M616 | 0 | 5 | 60 | v1 | 0,046 ± 0,007 | 0,036 ± 0,006 | v1 | 0,079 ± 0,003 **>** | 0,084 ± 0,003 **>** | — | 0,079 | 0,085 |
| 133 | M616 | 0,10 | 3 | 30 | v2 | 0,029 ± 0,005 | 0,023 ± 0,005 | v2 | 0,054 ± 0,003 | 0,056 ± 0,003 **>** | 0 | 0,057 | 0,061 |
| 134 | M616 | 0,10 | 3 | 45 | v1 | 0,025 ± 0,005 | 0,032 ± 0,006 | v1 | 0,058 ± 0,003 **>** | 0,053 ± 0,003 | — | 0,061 | 0,059 |
| 135 | M616 | 0,10 | 3 | 60 | v1 | 0,019 ± 0,004 | 0,030 ± 0,005 | v1 | 0,052 ± 0,002 | 0,057 ± 0,003 **>** | — | 0,057 | 0,061 |
| 136 | M616 | 0,10 | 5 | 30 | v2 | 0,025 ± 0,005 | 0,026 ± 0,005 | v2 | 0,051 ± 0,002 | 0,050 ± 0,002 | 0 | 0,056 | 0,055 |
| 137 | M616 | 0,10 | 5 | 45 | v1 | 0,018 ± 0,004 | 0,032 ± 0,006 | v1 | 0,053 ± 0,003 | 0,054 ± 0,003 | — | 0,058 | 0,059 |
| 138 | M616 | 0,10 | 5 | 60 | v1 | 0,014 ± 0,004 | 0,021 ± 0,005 | v1 | 0,051 ± 0,002 | 0,052 ± 0,002 | — | 0,056 | 0,058 |
| 139 | M616 | 0,20 | 3 | 30 | v2 | 0,019 ± 0,004 | 0,018 ± 0,004 | v2 | 0,041 ± 0,002 | 0,041 ± 0,002 | 0 | 0,047 | 0,049 |
| 140 | M616 | 0,20 | 3 | 45 | v1 | 0,014 ± 0,004 | 0,034 ± 0,006 | v1 | 0,040 ± 0,002 | 0,045 ± 0,002 | — | 0,045 | 0,050 |
| 141 | M616 | 0,20 | 3 | 60 | v1 | 0,007 ± 0,003 | 0,023 ± 0,005 | v1 | 0,046 ± 0,002 | 0,044 ± 0,002 | — | 0,052 | 0,051 |
| 142 | M616 | 0,20 | 5 | 30 | v2 | 0,012 ± 0,003 | 0,016 ± 0,004 | v2 | 0,040 ± 0,002 | 0,041 ± 0,002 | 0 | 0,045 | 0,048 |
| 143 | M616 | 0,20 | 5 | 45 | v1 | 0,004 ± 0,002 | 0,022 ± 0,005 | v1 | 0,042 ± 0,002 | 0,040 ± 0,002 | — | 0,049 | 0,048 |
| 144 | M616 | 0,20 | 5 | 60 | v1 | 0,008 ± 0,003 | 0,020 ± 0,004 | v1 | 0,037 ± 0,002 | 0,042 ± 0,002 | — | 0,043 | 0,048 |

## Par ligne

| ligne | cases | plus bas | plus haut (case) | seuil | cases au-dessus |
|---|---|---|---|---|---|
| C-P3a | 144 | 0,003 | 0,049 (case 005) | 0,0638 | 0 |
| C-P3b | 144 | 0,009 | 0,056 (case 097) | 0,0638 | 0 |
| C-P3c insertion | 144 | 0,026 | 0,107 (case 111) | 0,0549 | 82 : 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 012, 019, 020, 021, 022, 023, 024, 025, 026, 027, 030, 037, 038, 039, 040, 041, 042, 043, 045, 046, 047, 048, 055, 056, 057, 058, 059, 060, 061, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134 |
| C-P3c contenu | 108 | 0,026 | 0,095 (case 003) | 0,0549 | 50 : 001, 002, 003, 004, 005, 006, 007, 008, 009, 012, 019, 020, 021, 022, 023, 024, 025, 026, 027, 037, 038, 039, 040, 041, 042, 043, 045, 046, 047, 055, 056, 057, 058, 059, 060, 061, 109, 110, 111, 112, 113, 114, 127, 128, 129, 130, 131, 132, 133, 135 |
| C-P3c insertion (deux lectures), pour information | 144 | 0,032 | 0,337 (case 126) | 0,0549 | 90 : 001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 012, 019, 020, 021, 022, 023, 024, 025, 026, 027, 029, 030, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 055, 056, 057, 058, 059, 060, 061, 062, 091, 092, 093, 094, 095, 096, 097, 098, 099, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138 |
| C-P3c contenu (deux lectures), pour information | 108 | 0,033 | 0,095 (case 003) | 0,0549 | 71 : 001, 002, 003, 004, 005, 006, 007, 008, 009, 011, 012, 019, 020, 021, 022, 023, 024, 025, 026, 027, 028, 029, 032, 037, 038, 039, 040, 041, 042, 043, 044, 045, 046, 047, 048, 055, 056, 057, 058, 059, 060, 061, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138 |

## Issue au sens du texte (constat mécanique)

- C-P3a : issue 1, « la clause ne joue pas pour la ligne »
- C-P3b : issue 1, « la clause ne joue pas pour la ligne »
- C-P3c : issue 2, « la clause joue pour la ligne »
