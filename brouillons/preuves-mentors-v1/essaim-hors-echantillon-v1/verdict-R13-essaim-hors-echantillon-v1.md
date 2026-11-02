**confirmé avec réserves (listées)**

# Verdict du lecteur neuf (R13) — essaim hors échantillon — v1

Run décisif `20261102-005426-essaim-ho`, réplication unique `20261102-005705-essaim-ho-replication`, texte scellé
`prereg/essaim-hors-echantillon-v1.md` (sha256 `c35e738a9b10ddd98ed9a47c4f1befae1d2e5817ebfd70b2449fa3745222659f`),
grille `prereg/essaim-hors-echantillon-grille-v1.json` (sha256 `dbe1caf113ac12cf9e056cfd2f6916eb2d13341735cb58b0260acc64d86c8007`).
Écrit le 2 novembre 2026 (vers 01:20 UTC) par un sous-agent neuf : il n'a écrit ni le préenregistrement, ni le code,
ni les contre-lectures, ni lancé les runs. Aucun run relancé, aucun réseau, aucun commit, aucun fichier existant modifié.

## Verdict

- La lecture gelée calculée par le code est **exacte et conforme au texte** : mon recalcul indépendant, à partir des
  seuls comptes bruts, retrouve chaque état de cellule, chaque intervalle, chaque verdict, les trois scores et la
  fusion après réplication, **sans aucune divergence**.
- Issue : **mixte**. Prédictions risquées : 4 confirmées, 2 réfutées, 1 non concluante sur 7 ; cellules
  discriminantes : 13 conformes, 2 contraires, 3 non concluantes sur 18. Rejouée : confirmée. Instrument : 11 sur 11.
- Les deux réfutations portent sur la famille P3 (modèle de substitution gaussien) et **survivent à la réplication** :
  le modèle sous-estime la puissance de la co-élévation sous la sonde des enjeux, et la règle « au-dessus dès la
  moitié de l'essaim » de v1 tient à 5 agents sur ces épisodes, là où le modèle annonçait son échec.

## Réserves (une ligne chacune)

1. **Journal git du run décisif incomplet, non déclaré** : le relevé `git fsck --unreachable --no-reflogs` y vaut
   seulement « erreur : » (code de sortie non nul, message vide ; le lanceur jette alors la sortie standard), et ni
   R-1094 ni l'écart à l'étape G ne le disent ; le contrôle voulu (aucun commit abandonné depuis le gel) est couvert
   après coup par le journal de la réplication (00:57 UTC) et par mon propre relevé (01:02 UTC) : 428 lignes,
   octet pour octet identiques à la référence gelée (`3bfb671e…`), aucun objet inaccessible nouveau.
2. **Audit R4 dû par la table des issues, non compté par la lecture** : « toute prédiction réfutée » déclenche l'audit
   (texte, section « Ce qui déclenche l'audit ») alors que `audit_declenche` vaut faux (il ne compte que les variances
   et « trop beau ») ; « audit R4 non déclenché » (R-1094) ne vaut donc que pour ces deux déclencheurs ; la section
   « Symétrie » ci-dessous en fait le contenu (a) et (b), par un sous-agent neuf ; à consigner comme tel.
3. **Procédure, étape E** : la branche de l'arbre séparé `essaim-ho-scellement-v1` n'a pas été poussée avant le
   lancement (aucune référence distante locale) ; le texte n'exigeait que les empreintes, poussées à temps (R-1093,
   poussée à 00:54:20 UTC, lancement à 00:54:25).
4. **Brouillon 4** : le texte dit qu'il ne diffère du brouillon 3 que par les remplacements de la contre-lecture 3 ;
   il porte aussi E1 (une phrase de l'étape 0.d) et E2 (le marqueur de l'entrée de la contre-lecture 3 rempli),
   déclarés avant le scellement (`rapport-redaction-v4.md`, R-1092), sans effet sur hypothèses, prédictions ni
   critères ; pas de contre-lecture 4 (voie B, décision de routine).
5. **Marges fixées après coup (déclarées, C10)** : les deux réfutations tombent sur des cellules dont le sort dépend
   de ces marges (fourchette ± 0,15 de HP.4 ; cellule à 5 agents de HP.5a, retenue seulement pour une marge
   ≤ 0,0185) ; la lecture gelée s'applique telle quelle, et la substance tient (section « Symétrie »).

## Repères : à quoi renvoie chaque code

| Code | Surnom | Nature |
|---|---|---|
| HS.1, HQ.1, HP.1 | identités au bit près (surveillance par agent aveugle à la synchronisation) | instrument |
| HS.2, HQ.2, HP.2 | alarmes par agent à leur taux de fausse alarme | instrument |
| HS.3, HS.4 | puissance exacte de la co-élévation, loi de référence ; « pas de frontière à la moitié » | instrument (calcul) |
| HQ.3, HQ.4 | borne exacte de la co-élévation sous corrélation, et son signe | instrument |
| HP.3 | calibrage conforme sur essaims entiers de P3 | instrument |
| HS.5 | version séquentielle (e-valeur, détecteur e) sous la loi de référence, 10 pas | risquée |
| HQ.5 | baisse de la co-élévation et de la moyenne par pas sous corrélation 0,3 | risquée |
| HQ.6 | échappement de l'e-valeur sous corrélation 0,4, 5 agents (cellule vue en v1) | rejouée |
| HQ.7 | échappement de l'e-valeur sous corrélation 0,3, 5 agents | risquée |
| HP.4 | puissance contre la synchronisation totale sur P3 (fourchette du modèle) | risquée |
| HP.5a | échec de la règle « moitié de l'essaim » sous la sonde des enjeux | risquée |
| HP.5b | autres signes du modèle (co-élévation, moyenne par pas) | risquée |
| HP.6 | e-valeur au-dessus ou en dessous de son taux selon la sonde | risquée |

« Co-élévation » : nombre maximal, sur les pas, d'agents au-dessus du seuil par case au même pas. « Taux » : taux de
fausse alarme mesuré sous l'hypothèse nulle (essaims honnêtes), sur un échantillon indépendant. Les intervalles entre
crochets sont exacts (Clopper-Pearson, niveau 1 − 10⁻⁵).

## Les sept prédictions risquées, en clair

1. **Version séquentielle sous la loi de référence** : on prédisait que, sous scores indépendants et avec 10 pas,
   l'e-valeur cumulée et le détecteur e resteraient au plus à leur taux quand une partie de l'essaim se synchronise et
   passeraient en dessous quand tout l'essaim se synchronise ; on a observé 23 cellules sur 24 conformes (taux de 0,025
   à 0,051 aux synchronisations partielles contre environ 0,05 ; à synchronisation totale, e-valeur à 0,021
   [0,017 ; 0,026] avec 10 agents et 0,027 [0,022 ; 0,032] avec 20, détecteur e à 0,023 [0,018 ; 0,028] avec 10),
   mais avec 20 agents tous synchronisés le détecteur e reste à 0,047 [0,041 ; 0,054] contre 0,050 [0,047 ; 0,054] :
   non concluante.
2. **Baisse sous corrélation 0,3** : on prédisait qu'avec une corrélation de 0,3 entre agents d'un même pas (10 agents,
   20 pas), synchroniser 3 ou 5 agents ferait passer la co-élévation et la moyenne par pas sous leur taux, alors que
   sous scores indépendants la co-élévation serait très au-dessus (0,155 et 0,704) ; on a observé la co-élévation à
   0,021 [0,016 ; 0,025] et 0,035 [0,029 ; 0,041], la moyenne par pas à 0,016 [0,012 ; 0,020] et 0,023 [0,019 ; 0,029],
   contre des taux de 0,051 [0,048 ; 0,054] et 0,052 [0,049 ; 0,055] : confirmée, plus nettement que l'interpolation
   depuis v1 (qui plaçait la co-élévation vers 0,053 à 5 agents).
3. **Échappement de l'e-valeur sous corrélation 0,3** : on prédisait qu'avec une corrélation de 0,3 et 5 agents
   synchronisés sur 10, l'e-valeur cumulée et le détecteur e passeraient au-dessus de leur taux (l'interpolation les
   plaçait vers 0,060, à la limite de résolution) ; on a observé 0,061 [0,054 ; 0,069] et 0,065 [0,058 ; 0,073]
   contre 0,050 [0,047 ; 0,053] et 0,049 [0,046 ; 0,052] : confirmée, de peu pour l'e-valeur (borne basse 0,0542
   contre borne haute de référence 0,0528).
4. **Puissance contre la synchronisation totale sur P3** : on prédisait, sur les 60 épisodes honnêtes de P3
   rééchantillonnés, une puissance de la co-élévation entre 0,55 et 0,86 sous la sonde de tromperie (modèle : 0,705)
   et entre 0,31 et 0,62 sous la sonde des enjeux (modèle : 0,463), toutes deux sous 0,9285 (scores indépendants) ;
   on a observé 0,744 [0,730 ; 0,757] sous la sonde de tromperie, dans la fourchette, mais 0,665 [0,650 ; 0,679] sous
   la sonde des enjeux, au-dessus de la fourchette, redonné par la réplication à 100 000 essais (0,666 [0,659 ; 0,673]) :
   réfutée — le modèle sous-estime cette puissance d'environ 0,2 sous la sonde des enjeux.
5. **Échec de la règle « moitié de l'essaim » sous la sonde des enjeux** : on prédisait que synchroniser 3, 4 ou 5
   agents sur 10 ferait passer la co-élévation sous son taux (modèle : 0,025, 0,024, 0,032) et 3 à 6 agents la moyenne
   par pas (modèle : 0,021 à 0,034), donc que la règle de v1 échouerait à 5 agents ; on a observé la moyenne par pas sous
   son taux à 3, 4 et 5 agents (0,026, 0,029, 0,032 contre 0,050 [0,047 ; 0,053]) mais pas établi à 6 (0,049), la
   co-élévation à 0,0405 [0,0346 ; 0,0470] à 3 agents (non concluant, à une alarme près), 0,047 à 4 agents, et à 5 agents
   **au-dessus** de son taux, 0,068 [0,060 ; 0,076] contre 0,050 [0,047 ; 0,053], redonné par la réplication
   (0,070 [0,066 ; 0,073]) : réfutée — la règle de v1 tient à 5 agents pour la co-élévation sur ces épisodes.
6. **Autres signes du modèle** : on prédisait la co-élévation et la moyenne par pas au-dessus de leur taux sous la
   sonde de tromperie dès 4 agents synchronisés, et sous la sonde des enjeux à 7 et 10 agents ; on a observé les 13
   cellules au-dessus (tromperie : co-élévation de 0,107 [0,097 ; 0,117] à 4 agents jusqu'à 0,744 à 10, moyenne par
   pas de 0,082 [0,074 ; 0,091] à 0,950 ; enjeux : co-élévation 0,235 à 7 agents et 0,665 à 10, moyenne par pas 0,695
   à 10 ; taux d'environ 0,05) : confirmée, mais ce sont presque tous les signes qu'aurait donnés un pronostic naïf.
7. **E-valeur selon la sonde** : on prédisait l'e-valeur cumulée au-dessus de son taux à toutes les fractions sous la
   sonde des enjeux (modèle : 0,084 à 0,168), l'e-valeur et le détecteur e en dessous sous la sonde de tromperie à 6, 7
   et 10 agents, et le détecteur e en dessous à 10 agents sous la sonde des enjeux ; on a observé l'e-valeur des enjeux
   de 0,078 [0,070 ; 0,087] à 3 agents à 0,139 [0,128 ; 0,150] à 10 contre 0,050 [0,047 ; 0,053], celles de la
   tromperie entre 0,013 et 0,036 contre environ 0,050, et le détecteur des enjeux à 10 agents à 0,017
   [0,013 ; 0,021] : confirmée sur les 13 cellules, dont 6 discriminantes.

Rejouée (HQ.6, cellule déjà vue en v1, pas une prédiction indépendante) : sous corrélation 0,4 et 5 agents
synchronisés, e-valeur cumulée 0,067 [0,060 ; 0,075] et détecteur e 0,072 [0,064 ; 0,080] contre 0,052 et 0,050 :
confirmée à graine neuve (v1 : 0,0651 et 0,0658).

## Issue selon la table des issues écrites d'avance, et ce que change chaque réfutation

Issue mixte : ni « tout confirmé », ni arrêt, ni réfutation d'instrument. S'appliquent les rangées suivantes.

- **HS.5 non concluante** → « l'heuristique de Schur ne se transporte pas à T = 10 » ; action : la ligne « version
  séquentielle » de v1 est restreinte aux tailles de v1 (proposition à Lazar ; la table E de v1 n'est pas réécrite).
  Précision : l'échec tient à une seule cellule (détecteur e, 20 agents, synchronisation totale) ; l'e-valeur cumulée
  passe sous son taux aux deux tailles.
- **HP.4 réfutée** (au-dessus de la fourchette, sonde des enjeux) → « profil moins nuisible que modélisé » ; action :
  rapporter la puissance mesurée par son intervalle — tromperie 0,744 [0,730 ; 0,757], enjeux 0,665 [0,650 ; 0,679]
  (réplication 0,666 [0,659 ; 0,673]) — et **le modèle de substitution n'est pas un guide fiable de la puissance**. La
  ligne « puissance entre x_bas et x_haut » n'est pas prononcée. Fait observé, hors lecture gelée : les deux puissances
  restent très au-dessous de 0,9285, la valeur sous scores indépendants.
- **HP.5a : une cellule contraire** (exactement l'exemple de la table : co-élévation au-dessus de son taux à 5 agents
  sous la sonde des enjeux) → « la règle de la moitié tient sur ces 60 épisodes là où le modèle prévoyait son échec :
  l'effet du profil des pas est surestimé par le modèle » ; action : réplication faite, la contrariété persiste, donc
  **la ligne « règle de la moitié » n'est pas prononcée et l'énoncé de v1 garde un appui sur ces épisodes**. Ce qu'on
  ne peut pas en tirer : que la moyenne par pas suive la règle (ses cellules à 3, 4 et 5 agents sont sous leur taux,
  mais une cellule conforme d'une prédiction réfutée ne se prononce pas seule).
- **Toute prédiction réfutée** → audit R4 (réserve 2 ; contenu dans « Symétrie »).
- Toutes les autres prédictions sont confirmées : les lignes correspondantes de la table des énoncés sont prononcées
  telles que `lecture.md` les donne (identités sous les trois lois ; pas de frontière à la moitié sous la loi de
  référence, établi par le calcul ; baisse de la co-élévation sous corrélation 0,3 ; échappement de l'e-valeur sous
  corrélation 0,3 et 0,4 à 5 agents ; calibrage conforme sur P3 ; autres signes du modèle, non départageants ; e-valeur
  au-dessus ou en dessous de son taux selon la sonde). Les lignes qui contredisent la table E de v1 (échappement sous
  corrélation, e-valeur sur P3, absence de frontière) remontent à Lazar comme propositions.

## Portée exacte, et ce qui ne peut pas être revendiqué

- **Simulation** sur matrices de scores : la menace est un motif choisi (les agents synchronisés placent leur plus haut
  score au même pas), pas un comportement d'agents ni une idée qui se propage. **Aucun vrai essaim** : en P, les
  « agents » sont des épisodes indépendants de tâches différentes, sans communication.
- **Famille P** : les **60 épisodes honnêtes de P3** (un par tâche, 600 actions), **rééchantillonnés** ; calibrage,
  taux sous l'hypothèse nulle et essais **tirés dans les mêmes épisodes** ; intervalles **conditionnels à ces 60
  épisodes** (ils n'incluent pas l'incertitude sur les épisodes) ; prédictions d'un **modèle de substitution gaussien
  ajusté sur les moments de ces mêmes épisodes**. P éprouve l'approximation gaussienne, pas une loi de P3 au-delà.
- Familles S et Q : lois synthétiques (indépendante ; équicorrélée à c = 0,1, 0,3, 0,4).
- **Ne peut pas être revendiqué** : rien « sur P3 » ni « sur données réelles » en général ; rien sur des épisodes
  nouveaux (le calibrage conforme vérifié ne dit rien d'épisodes nouveaux) ; rien sur de vrais essaims (corrélation
  entre agents réels, propagation, pilotage du score) ; aucun mécanisme (les maxima arrachés au pas de co-élévation
  naturelle restent une conjecture : aucune cellule ne les mesure) ; ni « la règle de la moitié échoue sur P3 »
  (réfuté), ni « elle tient en général sur P3 » (elle tient pour la co-élévation à 5 agents, sous cette sonde, sur ces
  épisodes) ; ni une puissance de la co-élévation sur P3 au-delà des deux intervalles rapportés ; l'échappement de
  l'e-valeur sous corrélation n'est éprouvé qu'à c ∈ {0,3 ; 0,4} et 5 agents ; « au plus » veut dire « pas d'excès
  supérieur à environ 0,010 » ; l'absence de frontière à la moitié sous la loi de référence est un calcul vérifié par
  l'instrument, pas une découverte expérimentale ; les identités sur P contrôlent le code, ce ne sont pas des faits
  empiriques sur P3.

## 1. Sceaux et provenance

- `sha256sum -c`, depuis chaque dossier : texte scellé, grille, manifestes des deux runs, 9 fichiers de
  `diag/20261102-005426-essaim-ho/`, 4 de `diag/20261102-005705-essaim-ho-replication/` : **tous OK**. Chaque sortie
  est rattachée à l'empreinte de son manifeste (`3a2fbe42…`, `4d3b04b6…`) et à son identifiant de run. Fichiers
  inchangés depuis leurs commits (`c0e6fcd0`, `40972620`, `52422751`) ; arbre principal propre sur ces chemins.
- **Manifestes** : empreinte du texte `c35e738a…` ; commit cité `7e27c30c2d2859f81cb7f62427503d7cc865fa3d` ; lanceur
  `run_essaim_hors_echantillon_v3`, lecture `lecture_hors_echantillon_v3` ; commande citée ; `depot_propre` vrai ;
  `decisif` vrai ; `config_sha256` égal à l'empreinte de la configuration canonique ; aucune réserve.
- **Entropie** : int(h[:32], 16) avec h = sha256 du texte scellé = 259689878541342282915553522435420319662, égale à
  celle des deux manifestes (règle du texte, section « Graine racine »). Pour les 312 tâches de chaque manifeste : clé
  de dérivation = 8 premiers octets de sha256(nom), état de contrôle de `SeedSequence` recalculé : 0 écart ; noms des
  tâches = exactement ceux qu'énumère le texte (156, et leurs doubles `/replication`).
- **Code au moment des runs** : `git diff 7e27c30c 52422751 -- src tests grille` et `git diff 7e27c30c c0e6fcd0 --
  src tests grille` vides (HEAD du run décisif : `52422751` ; de la réplication : `c0e6fcd0`).
- **Texte** : ne diffère du brouillon 4 (`6afe7256…`) que par la ligne du commit cité ; le brouillon 4, reconstruit
  par moi en mémoire, = brouillon 3 + les 13 remplacements de la section 8 de la contre-lecture 3 + E1 + E2 (réserve 4).
  Grille = brouillon 2 de la grille, octet pour octet ; ses 84 entrées suivent les règles de sélection du texte
  appliquées aux valeurs du modèle (`tables-valeurs-predites-v2.md`, vérifié cellule par cellule).
- **Chronologie (UTC, git et journal des poussées)** : gel R-1092 commité 00:53:10, poussé 00:53:12 ; arbre séparé
  00:53:18 ; commit cité 00:53:31 ; texte scellé 00:53:53 ; R-1093 commité 00:54:18, poussé 00:54:20 ; lancement
  00:54:25, fin 00:55:56, code 0 ; sorties commitées 00:56:33 ; réplication 00:57:05 → 00:58:36, code 0. Les heures
  écrites dans R-1092 (00:55) et R-1093 (01:00) sont approximatives et postérieures aux commits ; l'ordre fait foi
  par git.
- **Journal git versé** : run décisif — journal des 40 commits et du reflog sans commit étranger (création de l'arbre,
  `reset` interne de `git worktree add`, même motif que l'arbre de v1, puis les deux commits) ; relevé des commits
  inaccessibles en échec (réserve 1 ; un commit concurrent de la session principale, `838d12f8` à 00:54:37, est une
  cause possible, non vérifiée). Réplication — relevé complet : 428 lignes, **identiques à la référence gelée** ; rien
  de nouveau. Mon relevé (01:02 UTC, code 0) : identique octet pour octet à la référence. Aucun réglage de nettoyage
  git (les objets récents ne peuvent pas avoir été effacés entre-temps).
- **Pas de pré-run visible** : aucun autre dossier de run de cette simulation dans les trois arbres ; l'entropie
  décisive n'apparaît que dans les deux manifestes et les sorties de lancement. Ce contrôle ne voit ni un clone ni
  un calcul non écrit ; la déclaration de passation (point 4 de la parade) reste à faire par la session principale.
- Écart à l'étape G (`verifier-arbre`, 193 problèmes préexistants hors du run) : déclaré, sans effet sur le run.
  Observation O1 : `lecture.json` porte `version` v2 et `lecture_version` v3 ; la seconde fait foi.

## 2. Recalcul indépendant

Code à moi, hors dépôt, sans aucun import de `controle_ia` (empreintes en fin de fichier) :
- intervalles de Clopper-Pearson par inversion numérique des queues binomiales, recoupés par la loi bêta (écart
  < 10⁻⁹) ; critères réécrits depuis la table « Critères de lecture gelés » du texte ; verdict, scores, cellules
  discriminantes, « trop beau », variances des écarts réduits ;
- seuils exacts de S recalculés depuis la loi binomiale : (4 ; 0,3228497802) à 10 × 10, (6 ; 0,3164929897) à 20 × 10,
  égaux au run ; seuil de la moyenne par pas égal ;
- **puissance exacte de HS.3 par une autre méthode** que le code : programmation dynamique sur les agents (histogramme
  des comptes des 9 pas autres que le pas commun), validée d'abord contre une énumération brute de la synchronisation
  (6 petits cas, écart ≤ 1,1·10⁻¹⁶) ; écart au code ≤ 4·10⁻¹⁰ sur les 12 valeurs (le code certifie ≤ 10⁻⁹) ;
- borne de HQ.3 par intégration adaptative sur le facteur commun (le code : Gauss-Hermite) : écart ≤ 5·10⁻¹⁵ ;
- région conforme par convolution directe de 50 lois bêta-binomiales : [843 ; 1 165] (rang 951, taux 50/1001),
  égale au texte ; totaux observés 960 à 1 087 ;
- u et taux empirique q de P3 recalculés depuis `scores-p3.npz` (empreinte `968414fc…` vérifiée) : égaux au run.

**Résultat** : 311 cellules du run décisif, 113 cellules P de la réplication, lecture fusionnée : **0
divergence** d'état, d'intervalle ou de verdict avec `lecture.json` (run et réplication). Scores identiques :
risquées 4 / 2 / 1 sur 7, cellules 59 / 2 / 4 sur 65, discriminantes 13 / 2 / 3 sur 18 ; rejouée 1 sur 1 ;
instrument 11 sur 11, 244 sur 244. Variances des écarts réduits : formes closes 0,949 (11), égalités 1,235 (165),
dans [0,3 ; 3].

## 3. Réplication

- Règle appliquée comme écrite : prédictions comptant une cellule statistique contraire = HP.4 et HP.5a → seule la
  famille P rejouée (`familles: ['P']`) ; R = 100 000, R_cal = R₀ = 500 000 (× 5) ; calibrage conforme inchangé
  (1 000 essaims, 50 tirages de 400) ; descriptif non rejoué ; une seule réplication (aucun autre dossier) ; lancée
  par le lanceur v3 sur son propre run principal ; fusion par la règle de T0.3, puis annotation.
- **Graines neuves** : même entropie racine, mais tâches suffixées `/replication`, dont chaque clé de dérivation et
  chaque état de contrôle diffèrent de ceux de la tâche principale (vérifié pour les 156 paires). Preuve empirique :
  la partie conforme, de tailles inchangées, donne des tirages différents (2 à 4 coïncidences sur 50, au hasard) ; u
  et q, déterministes, sont identiques.
- **Après fusion, HP.4 et HP.5a restent réfutées** parce que leurs deux cellules contraires sont **de nouveau
  contraires** en réplication (enjeux, synchronisation totale : 0,666 [0,659 ; 0,673] > 0,62 ; enjeux, 5 agents :
  co-élévation 0,070 [0,066 ; 0,073] contre un taux de 0,050 [0,049 ; 0,052]) ; la règle ne rend « non concluante »
  qu'une cellule contraire dont la réplication est conforme.

## 4. Symétrie (R4) — ce qui rendrait l'issue trop belle, ou trop laide

Contenu (a) et (b) de la première rangée des issues, fait ici par symétrie (réserve 2).

**Côté « trop beau »**
- « Trop beau » non atteint (2 réfutées, 3 discriminantes non concluantes) ; variances des écarts réduits ni trop
  serrées (échantillon réutilisé) ni trop larges.
- Confirmations peu exigeantes : 39 des 47 cellules risquées non discriminantes avaient déjà le sens du pronostic
  naïf ; les 20 cellules « au plus » de HS.5 ne protègent pas d'une fausse confirmation (un taux vrai de 0,058
  passerait avec probabilité 0,92) ; HP.5b ne départage pas ; la fourchette de HP.4 (0,31 de large) est peu exigeante.
- Confirmations discriminantes (13) : HQ.5 (3), HQ.7 (2), HP.6 sonde des enjeux (6), HP.4 tromperie (1), HP.5a
  moyenne par pas à 5 agents (1). HQ.7 passe de peu (0,0542 contre 0,0528), comme le texte l'annonçait (probabilité
  de conclure ≈ 0,43) : fragile, pas suspecte.
- Fuite des données dans le modèle (a) : `moments_et_substitution_v1.py` ne lit que les moments déclarés et tire un
  modèle gaussien à graine propre ; ses seuils diffèrent de ceux de la vraie loi rééchantillonnée (u 1,281 et 1,282
  contre 1,253 et 1,273 ; seuil de la co-élévation (5 ; 0,376) contre (4 ; 0,114) en tromperie, (6 ; 0,06) contre
  (6 ; 0,761) en enjeux) : aucun signe que les vraies valeurs l'aient nourri. `loi_p3_v1` (rééchantillonnage par
  épisodes entiers, sans remise dans un essaim, réduction regroupée, quantile « inverted_cdf ») est conforme au texte,
  et u et q recalculés sont égaux. Les bornes ont été recalculées par d'autres méthodes (section 2) plutôt que relues.
- Référence naïve (b) : sous scores indépendants à 10 × 10, la co-élévation vaudrait 0,122, 0,227, 0,378, 0,541, 0,686,
  0,929 pour 3, 4, 5, 6, 7, 10 agents ; sur P3 on observe beaucoup moins à chaque fraction (tromperie 0,071 à 0,744 ;
  enjeux 0,041 à 0,665). Le sens « puissance sous la référence » du modèle est juste partout ; ses magnitudes sont
  trop basses partout (co-élévation observée au-dessus du modèle à toutes les fractions et sous les deux sondes).

**Côté « trop laid »**
- Les deux réfutations dépendent des marges fixées après coup (réserve 5) : HP.4 sort de ]0,31 ; 0,62[ par 0,03
  (borne basse 0,650) — une marge de 0,20 l'aurait rendue non concluante, 0,25 conforme ; la cellule de HP.5a à
  5 agents n'était retenue que pour une marge ≤ 0,0185 — à 0,020, HP.5a aurait été non concluante. Mais l'énoncé en
  clair de HP.5a (« la moitié de l'essaim ferait passer la co-élévation sous son taux ») est contredit directement par
  cette cellule (0,068, puis 0,070 à 5 × R), quelle que soit la marge ; et HP.4 se trompe de 0,2 en valeur absolue.
- Non concluantes (4 risquées) : HS.5, détecteur e à 20 agents (0,047) ; HP.5a, co-élévation à 3 agents, **à une
  alarme près** (810 alarmes ; 809 aurait été conforme ; à titre descriptif seulement, la réplication donne
  0,039 [0,037 ; 0,042], nettement sous le taux, mais la règle gelée ne rejoue que les cellules contraires et cela ne
  change rien) ; HP.5a, co-élévation à 4 agents (0,047 ; réplication 0,046, non concluante aussi) et moyenne par pas à
  6 agents (0,049). Sans effet sur les verdicts : HP.5a est réfutée de toute façon.
- Résolution à R = 20 000 : « en dessous » exigeait environ 0,0405 au plus ; les valeurs du modèle (0,021 à 0,034)
  étaient résolubles ; les non-conclusions viennent d'effets plus faibles que modélisés, pas d'une puissance mal
  planifiée.
- Défaut d'instrument écarté : identités, égalités et région conforme toutes conformes sur P, au run et en
  réplication ; recalcul indépendant identique ; réplication à graines neuves concordante.
- Descriptif calculé par le lecteur après le run, sans verdict ni explication : part des cases au-dessus du seuil par
  pas, sonde des enjeux 0,08 / 0,05 / 0,05 / 0,03 / 0,02 / 0,07 / 0,12 / 0,05 / 0,22 / 0,33 (pas 0 à 9) ; sonde de
  tromperie 0,18 / 0,18 / 0,05 / 0,10 / 0,08 / 0,13 / 0,08 / 0,15 / 0,05 / 0,00.

## 5. Fichiers du lecteur (dossier de travail, hors dépôt, non committés)

Dossier `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/R13-essaim-ho/` :
- `recalcul_r13_essaim_ho_v1.py` — sha256 `14eb89e1bd2a0bc6cf2645f3c6d265295bcacc8f9af0b79a8282768a1683378d` ;
- `test_dp_v1.py` (validation par énumération brute) — `6b11772129ff7fd8ed777cf07328bfda1418c1fb4b8a509192fbf71ef2d0bd74` ;
- `verifier_graines_v1.py` — `79bd08a55a2e86e1f0b6f05ffcee62d8a7425055a4db1b068368fce1c65e8b49` ;
- `sortie-recalcul-r13-v1.json` — `b8638f180bc3e5fb63979ff31e1aca0ddd36c918d59e4a30874b8de9c07bd17c` ;
- `sortie-recalcul-r13-v1.txt` — `3d1c4cf7811ca565bd3a4dbf4b3c4bb8f5ae1a53b31ce224d57127fab3587939` ;
- `fsck-maintenant.txt` — `3bfb671ef4c77282e6078cb0b41718ab9b3b40273eb9414c1d821c9fdea57e27` (= référence gelée).

Ce fichier n'a pas de compagnon `.sha256` : la consigne était d'écrire un seul fichier ; à créer par la session
principale (R6), avec le versement éventuel des fichiers ci-dessus.
