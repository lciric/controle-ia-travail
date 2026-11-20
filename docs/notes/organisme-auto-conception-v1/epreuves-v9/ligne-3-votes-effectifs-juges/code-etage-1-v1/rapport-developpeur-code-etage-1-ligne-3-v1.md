# Rapport du développeur — code de l'étage 1 de la ligne 3 (banc de juges scriptés) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel) sous les mandats
`mandat-developpeur-code-etage-1-ligne-3-v1.md` (`1b6d0c7e…6eb4fbb`) et `…-v2.md` (`0769bc95…3271b60`), empreintes
recalculées égales. Texte qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`,
lu par `git show origin/main:…` après `git fetch origin main`, empreinte recalculée `4e3680d9…3e99d5a0`, égale. Calcul de
référence : `calcul_predictions_ligne_3_v2.py` (`802d4dd2…a5e12c11b`, égal à son compagnon) et sa sortie
(`2cf1eba7…14eae724`, égale). Python 3.13.18 (`/usr/local/bin/python3`), numpy 2.5.3, pytest 9.1.1 ; pas de scipy.

Les fichiers n'existent que dans le bloc-notes du développeur, à l'arborescence du dépôt ; rien n'est écrit dans le
dépôt, rien n'est committé.

## Fichiers écrits (dossier `code-etage-1-v1/`)

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v1.py` | `1d474cc905c25351ce3c4cc2c2a0661cefca353c31898c353700e34f8dd4ca0f` |
| `essais_banc_juges_scriptes_ligne_3_v1.py` | `13b2b8988825091e0f1c6af99cffff75d94efb1b640ffef99131dfd3bfb2e174` |
| `chronometrer_banc_ligne_3_v1.py` | `6d490094c21632cf28e0b5dbb1c6b189fbfa1f539d86159a218adfe2240f16d1` |
| `controle_defauts_reintroduits_ligne_3_v1.py` | `f8c94d6894c4a350c266c5ff04cf5bd9209fd111519635ef8799f1aba3fc3bbc` |
| `rapport-defauts-reintroduits-ligne-3-v1.json` | `1024aa462a8ffbd1441be8e2b9a72c5ec03de04d797f7f998c46cf891f03cd72` |

Chaque fichier a son compagnon `.sha256`. Rien de l'étage 2 n'est écrit (ni générateur de témoins, ni garde de
recouvrement, ni épreuve sur juges réels, ni compteur d'arrêt).

## Ce que fait le code

- **Banc** : lois 1 à 4 ; valeur plantée par la formule poolée (loi 2 par Gauss-Hermite à 200 points, `math.erf`,
  `statistics.NormalDist`) ; estimateur stratifié par classe, « indéfini » jamais 0 ; intervalles par rééchantillonnage
  multinomial des comptes de configurations, stratifié par classe ; bras S, U, F (« au moins un », majorité stricte,
  poids égaux), N, C, P, R (k = J ; et k = 3 à J = 2) ; règle choisie à deux juges (arrêt si hors des cinq) ; critère de
  `fa38f9faa24e0`, branche (2) de `fefca0bd94064` ; monde de puissance (bissection, cellules infaisables nommées, test
  entier : quatre valeurs de probabilité, Holm, écart observé de 0,05 au moins) ; puissance de la lecture « positif » de
  ρ′ − ρ ; double rendu (trois lois du lecteur sur les mêmes tirages, clauses et mot sur le suiveur séduisant seul) ;
  garde de cadrage ; alarme (bras A à D) ; application mécanique des critères gelés, marquée comme aide (le verdict
  revient à un agent neuf, R13) ; manifeste par exécution (configuration et empreinte, versions, graines, commit) ;
  gardes déterministes rejouées avant le premier tirage ; écriture exclusive (une exécution par dossier).
- **Chronométrage** : n'imprime que des lignes `duree_…_secondes: …` ; écrit un manifeste.
- **Contrôle des défauts réintroduits** : 27 défauts, un par copie, chacun contre son essai visé.

## Essais

`TMPDIR=<bloc-notes>/tmp PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q essais_banc_juges_scriptes_ligne_3_v1.py` :
**73 passés, 0 échoué** (8,4 s). Premier brouillon : 2 échecs, tous deux dans les essais eux-mêmes (bout en bout à
16 répliques où la garde P2 se déclenche à bon droit sur le bruit ; décompte des `SeedSequence(` qui comptait la
docstring), corrigés par l'outil de remplacement. Gardes de la liste d'arrêt couvertes, cas sain et artefact :
estimateur, théorie P2, formules, règle choisie à deux juges ; plus la garde des graines, l'exécution unique, le
manifeste, le chronométrage. Essais de formules : grand n par loi contre valeur plantée (11 cas, lois 1 à 4, taux
égaux, dissymétriques et inégaux) ; erreur équilibrée des règles contre le § 0 ; taux du double rendu (3 lois × 3 δ),
écarts de surface, abstentions (0,1275 ; 0,239) contre `calcul_predictions_ligne_3_v2.py` ; mots sans intervalle
contre sa sortie ; d, faisabilité et jouabilité sous la loi 3 du monde de puissance égaux au calcul (égalité exacte des
d), écart vrai de 0,10 retrouvé par simulation à grand n.

## Contrôle « trop beau » (R4)

`rapport-defauts-reintroduits-ligne-3-v1.json` : **27 défauts sur 27 vus** par l'essai visé ; les essais visés passent
sur le banc sain (40 passés). **Non réintroduits : les défauts de la garde des graines** — réintroduire un tel défaut
ferait dériver une racine décisive dans le processus d'essai, ce qui est interdit ; cette garde est à contrôler à la
lecture par le contre-lecteur.

## Où le texte se tait : choix les plus étroits, déclarés

1. Partage par moitié : l'étalonnage reçoit ceil(n_c/2) bons et floor(n_c/2) mauvais (25/25 à n = 50), pour garder les
   tailles d'étalonnage 25, 50, 100, 200 écrites à la branche (2).
2. J = 5 joué sous les lois 1 et 4 seulement (« banc à J = 5, lois 1 et 4 ») ; lois 1, 2, 3 à J = 2 ; loi 3 au seul
   taux 0,20 et ρ ≤ 0,75 ; loi 4 aux six profils à taux égaux entre juges (pas le profil inégal).
3. ρ moyenne « indéfinie » dès qu'un juge n'a aucune variance (comme la paire) ; votes effectifs indéfinis si le
   dénominateur est nul.
4. Intervalle : tirages indéfinis écartés et comptés ; couverture sur les répliques à estimation définie, un
   intervalle indéfini comptant « non couvrant » ; centiles de numpy (interpolation linéaire) ; « plus petit n qui
   tient » = plus petit n où la cellule tient, sans exiger les n plus grands.
5. Rééchantillonnage sur les comptes des configurations d'**erreurs** (équivalentes aux configurations de votes à
   classe fixée), par paquets gelés de 50 répliques (constante qui fixe l'ordre des tirages).
6. Égalité au seuil des bras C, P, poids égaux : tolérance 1e-9 × (1 + |seuil| + Σ|w|), dans laquelle le score rend
   « non notable » ; « notable » si le score dépasse le seuil, quel que soit le sens des moyennes de classe.
7. Repli du bras C : trace de S nulle, poids non finis, ou moyenne des poids ≤ 0.
8. Bras P : division par 2 une fois par paire au-dessus de 0,5 (un juge dans deux paires l'est deux fois) ; paire à
   corrélation indéfinie non divisée.
9. Bras N : réplique à votes effectifs d'étalonnage indéfinis écartée et comptée.
10. Bras R : le premier rendu est celui du juge 1 de la cellule (son taux) ; chaque rendu suivant copie le premier avec
    probabilité ρ′, sinon tire le sien (même loi jointe que la loi 1) ; k = 2 et k = 3 sur les mêmes tirages. Dans le
    monde de puissance, R est lié au juge 2 (pendant d'Argon, qui partage son premier rendu avec S-Argon).
11. Mot de `fa38f9faa24e0` à l'étage 1 : références « poids égaux » et R à k = J, un mot par ρ′.
12. Comparaisons descriptives de l'étage 1 : intervalle par rééchantillonnage des répliques (procédé des clauses de
    `fcfa3d98b90f8`).
13. Monde de puissance : dans les mondes « unanimité » et « juge seul », R est joué à ρ′ = 0 (convention du calcul v2) ;
    tolérance 1e-12 sur « écart ≤ 0 » et « écart ≥ 0,05 ».
14. Puissance de ρ′ − ρ : loi 1 emboîtée (choc commun ρ ; sinon choc propre au juge, (ρ′ − ρ)/(1 − ρ)), taux 0,20 dans
    les deux classes, 100 témoins sans partage, ρ de la grille avec ρ + écart ≤ 1, ρ et ρ′ par paire ; puissance par
    juge et des deux.
15. Double rendu : bras 4 = premiers rendus des deux juges du bras 1 ; bras 2 = ces deux juges plus deux autres ;
    prédicteur de surface = « non notable si trait » (prédicteur de la classe sur ce banc ; son exactitude contre le
    trait vaut 1 par construction ; accord avec le bras 1 rapporté comme information) ; réplique sans groupe écartée et
    comptée.
16. Garde de cadrage : rondes moitié vrais, moitié faux, s = 1 aussi pour les rondes saines ; « dépasse » strict.
17. Alarme : un seul juge (celui qui change) ; moitié des suites changées, dont moitié « à effet » ; départ 0,10/0,10
    (à effet) ou vrais rejetés 0,05 / faux acceptés 0,15 (sans effet), suites sans changement partagées entre ces deux
    départs ; ancres et référence moitié bonnes ; tests aux générations 2 à 12 (11 tests), alarme si p ≤ niveau ; z à
    variance poolée, aucune alarme à variance nulle ; bras D : m cartes de plus à 70 % arrondi ; binomial exact
    « probabilités au plus égales », tolérance relative 1e-7.
18. Racines 2026111931 à 2026111933 : autorisation = l'additif de code, chemin et empreinte, vérifiés avant toute
    dérivation ; 2026111934 à 2026111937 toujours refusées. Une cellule reçoit l'enfant de rang fixe de
    `SeedSequence(racine, spawn_key=(clé,)).spawn(nombre)` ; décisif : tirages 2026111932, rééchantillonnage
    2026111933 ; chronométrage : 2026111931 pour les deux.

## Points pour la mère (jugés ou lus ; je ne tranche pas)

- A. Le monde de la puissance de ρ′ − ρ (choix 14) n'est pas écrit par le texte ; il fixe un chiffre rendu à la mère.
- B. ρ′ de R dans les mondes non-R (choix 13) touche Holm, donc la puissance qui décide.
- C. Lien de R au juge 1 (étage 1) et au juge 2 (monde de puissance) : choix 10.
- D. Alarme à un seul juge et compositions (choix 17) : elles portent la lecture de P6.
- E. Table gelée de l'estimateur : « tient à n = 50 seulement » n'a pas de ligne ; le code rend « cas non prévu, rendu
  à la mère ».
- F. Le code calcule les mots et le verdict mécanique, marqués comme aide ; s'il ne doit rien calculer de ce qui est
  lu, ces fonctions se retirent sans toucher aux mesures.
- G. Garde des graines non éprouvée par défaut réintroduit (voir R4).
- H. L'annexe A nomme `calcul_predictions_ligne_3_v1.py` ; le mandat donne la v2 (mêmes valeurs, plus une partie) :
  essais faits contre la v2.
- I. Les essais retrouvent le calcul v2 à côté du dossier, sinon au chemin absolu du dépôt ; une fois le code versé,
  le chemin relatif sert.
- J. Le code tourne en un seul processus ; l'ordre de grandeur du texte (« l'heure, sur quatre cœurs ») ne vaut pas tel
  quel.

## Temps de calcul estimé

Chronométrage en essai (racine 2026111930, 40 répliques par famille, 2 000 tirages de rééchantillonnage), extrapolé :
**environ 6 560 s, soit 1 h 50 sur un cœur** (estimateur et agrégation 6 246 s ; monde de puissance 185 s ; ρ′ − ρ
114 s ; double rendu 13 s ; cadrage et alarme moins de 1 s). Ni l'étage 1 décisif ni le chronométrage décisif n'ont été
lancés.

## Attestation sur les graines

Seule la racine des essais, 2026111930, a été dérivée pendant mon travail : essais, contrôle des défauts réintroduits
(essais visés seulement, aucun défaut sur la garde des graines), chronométrage en essai. L'essai final
(`test_zz_final_…`) contrôle le journal des dérivations du banc et toute `SeedSequence` créée par du code Python dans
le processus : aucune entropie de 2026111931 à 2026111937 ; il passe.

Développeur, modèle L′.
