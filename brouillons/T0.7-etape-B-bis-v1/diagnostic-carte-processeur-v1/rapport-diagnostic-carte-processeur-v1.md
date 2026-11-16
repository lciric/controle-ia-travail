# Diagnostic de l'arrêt « contrôle carte-processeur » de la course B bis de T0.7 — v1

- **Auteur** : développeur neuf (modèle A), sous-agent de la session mère ; n'a écrit ni le texte, ni le code de B bis, ni ses
  diagnostics antérieurs. **Heures (UTC, `date -u`)** : 2026-11-16, de 22:05:58 à la déclaration (§ 9).
- **Statut** : diagnostic, **processeur seulement, données fabriquées seulement** ; aucune machine, aucun appel au loueur, aucune
  dépense ; aucun score ; rien de 7a ni de 7b ; aucune sortie de l'étape B de T0.7. Pièces de ce dossier scellées (compagnons
  `.sha256`), non committées.
- **Course diagnostiquée** : run `20261116-172118-bbis-t07-v1`, code au commit `31fa8ac6` de `prep/t07bbis-code-v1` (entrées
  commitées sur la machine en `fa4889f7`, parent `31fa8ac6`) ; arrêt écrit à 21:35:28Z.

## 1. Verdict

1. **Cause la plus probable (confiance moyenne, environ 0,6)** : aucune erreur de chaîne n'est visible au code ; l'écart 1,004
   vient très probablement de l'**amplification des écarts d'arrondi** par l'apprentissage de la sonde linéaire agrégée par le
   maximum sur 300 époques d'Adam (pas 0,05) : sur des données fabriquées dont beaucoup de jetons d'une action sont des
   quasi-copies les uns des autres (forme plausible de vraies activations en demi-précision, **non vérifiée** sur les vraies
   données), deux piles qui ne diffèrent que par l'ordre des sommes rendent **une autre sonde** (écart du contrôle 1,3 à 12,8,
   rang de Spearman jusqu'à −0,04), alors qu'à 3 époques elles s'accordent à 10⁻¹⁰ près au plus. C'est le mécanisme déjà reconnu
   pour l'attention (addendum, EC-1), que la v3 croyait absent de la linéaire.
2. **Correction proposée** (`validation_imbriquee_v4.py`, nom neuf) : linéaire contrôlée comme l'attention — carte contre
   processeur à **3 époques** (≤ 10⁻⁴), **déterminisme au bit près à 300 époques** sur la carte, écart à 300 époques **écrit comme
   information sans arrêt**. Essais : 16 passés (reproduction de l'arrêt v3 sans erreur de chaîne, cas après correction,
   artefacts).
3. **Elle change ce que le texte gèle** (fragments EC-1, EC-4, EC-8 de l'addendum scellé, et la réserve R-PILE limitée à
   l'attention) : **écart à déclarer** (nœud de Lazar), non une « correction du code sous ce texte ». Critères d'état et d'issue,
   métrique, seuils, tolérance, découpages, graines : inchangés. **Une relance sous le texte actuel rejouerait le même couple** (même
   graine, mêmes données, mêmes piles) et s'arrêterait très probablement de même.

## 2. Ce que disent les traces (lues sur `donnees/t07-etape-b-bis-v1`, `8ec901fa`, par `git show` ; aucune ne porte de score)

| pièce | sha256 | ce qu'elle dit |
|---|---|---|
| `diag/20261116-172118-bbis-t07-v1/arret-marche-bbis.json` | `b116bd0d71d20a37e85206dfae1e90773b7bc5f7f7e16e7f36267c8383ee786b` (compagnon juste) | arrêt `GardeArret` à l'étape « contrôle carte-processeur », pile `marche_v3.py` l. 381 → `validation_imbriquee_v3.py` l. 150 → l. 91 ; `scores_ecrits` faux ; garde de débit : 20 premiers apprentissages (10 par famille), médiane 2,23 s, projeté 2,65 h (limite 11 h) |
| `runs/20261116-172118-bbis-t07-v1/manifeste.json` | `0a7693cc764a4b7a99595d2ce30bc01b53e4074935b3664fd09329690033258b` (compagnon juste) | configuration : appareil `cuda`, 300 époques, familles linéaire et attention, variante aucune, 4 plis internes, 100 réétiquetages, 800 directions ; versions torch 2.14.1, numpy 2.4.6, scipy 1.17.1, Python 3.11.18 ; graines (entropie et états de contrôle) ; aucun résultat |
| `traces/bbis-t07-v1/journal-bbis.txt` | `262d5789544367c85924be8adbdf230a873975170b3babc198b5474f73728327` | carte A100-SXM4-80GB, pilote servant CUDA 13.2 ; essais du paquet « 115 passed, 24 skipped » ; marche de 17:58:00Z à 21:35:28Z (code 4) |
| `traces/bbis-t07-v1/marche.txt`, `marche.err` | `7c38e88d…`, `ef846dbd…` | le même arrêt ; chargement du modèle deux fois (relecture à état imposé), aucune erreur |
| `traces/bbis-t07-v1/essais.txt`, `essais.err` (vide), `modele.txt`, `nvidia-smi*.txt`, `pip*.txt` | `0b608a67…`, `e3b0c442…`, `a045de48…`, `03ef1e75…` / `025883fe…`, `7fb575e8…` / `3b760b14…` | essais, téléchargement du modèle, en-tête de la carte (pilote 595.91.07), paquets (torch 2.14.1, numpy 2.4.6, cuBLAS 13.1.1.3) |

Quatrième passe de répétition (`calcul/t07bbis-repetition-v4`, `75bc5b32` ; `traces/bbis-t07-repetition-v4/repetition-carte.json`,
`cbcaeb52…` ; ligne R-2957 de `registres/decisions.md`) : **même carte, même pilote, mêmes versions**, déterminisme posé
(TF32 coupé, relu), 640 actions, 143 231 jetons, largeur 4 096 ; écarts linéaire 300 époques 1,95·10⁻⁸, attention 3 époques
1,49·10⁻⁸ — sur des jetons **N(0, I) indépendants en simple précision** (`scripts/repetition_carte_bbis_v3.py`, `jeu_synthetique`,
`355b3133…`). La pile de la carte marche donc sur des données bénignes ; ce qui change à la course est la **forme des données**.
Déjà sur ces données bénignes, l'écart de la carte (2·10⁻⁸) était quatre ordres au-dessus de celui de deux piles du processeur
(10⁻¹²) : l'apprentissage amplifiait déjà l'arrondi (`diagnostic-ecart-attention-carte-v1.md`, `5ecb9235…`, l. 24).

## 3. Lecture du code (commit `31fa8ac6` ; `src` et `scripts` de l'arbre égaux à ce commit, vérifié par `git diff`)

Fichiers : `validation_imbriquee_v3.py` (`71bffa5b…`), `apprentissage_carte_v1.py` (`4b98fcb9…`), `sondes/familles.py`
(`6758b651…`), `validation_imbriquee_v1.py` (`1ffb6e4d…`), `commun_v1.py` (`9db2b40b…`), `marche_v3.py` (`7009b34d…`),
`lecture_v2.py` (`154795f4…`), `harnais/modeles.py` (`d0befc29…`), `harnais/sondes.py` (`f92657a6…`), `sondes/evaluation.py`
(`1040674c…`), `t06/lanceur_v2.py` (`f2db51fc…`).

**Chaîne du contrôle linéaire** : `jouer` passe `sondes_300={famille retenue: res["sonde"]}` ; si le réglage retenu du couple est
linéaire, la sonde de la carte est la sonde finale ; sinon une linéaire est apprise sur la carte au même réglage. La référence
(`controle_carte_processeur`) réapprend par `familles.entrainer` sur **les mêmes objets** `res["sequences_app"]` et
`res["y_app"]` (ceux de l'apprentissage final, `apprendre_recette`), même régularisation, mêmes 300 époques, même pas ; la
graine ne joue pas pour la linéaire (départ w = 0, b = 0). Aucune écriture en place des séquences ni des sondes après
l'apprentissage (plancher : `np.concatenate` puis lecture ; notation : lecture ; `LotCarte` copie). Mêmes fonctions de score
des deux côtés (`ac.scores`). **Aucune erreur de chaîne trouvée.**

Pistes demandées, une à une :
- **Dénominateur** : `ecart_relatif` = max |a − b| / max(|b|, 1) : le plancher 1 interdit qu'un score voisin de 0 fasse exploser
  le rapport. 1,004 veut dire qu'au moins une action de contrôle porte |a − b| ≈ max(|b|, 1) : les deux sondes **diffèrent
  vraiment** (signe, échelle), pas un artefact de dénominateur ; aux essais, la définition de repli rapportée à l'échelle globale
  (max |a − b| / max |b|) donne 0,4 à 1,0 et le rang de Spearman descend à 0,16 et −0,04 (§ 4). Une forte régularisation ne crée
  pas l'écart : elle le **réduit** (§ 4, cas 2 et balayage préalable : 10⁻¹ plus stable que 10⁻³).
- **Grandeurs non déterministes** : algorithmes déterministes exigés sur la carte (`exiger_deterministe`) et posés par
  `regler_determinisme` (appelé par `t07/repli_recalcul_v1.recalculer`, première étape de la marche) ; processeur
  déterministe. La v3 ne vérifie pas le déterminisme de la linéaire à 300 époques sur la carte, mais la répétition l'a trouvé vrai
  pour les deux familles. Piste écartée sans preuve définitive ; la v4 l'ajoute.
- **Précision (TF32)** : coupée par `regler_determinisme` (`allow_tf32 = False`, relu « tf32_produits » faux à la répétition) ;
  surtout, **tous les tenseurs de l'apprentissage sont en double précision** (`LotCarte`, `entrainer`), où TF32 ne s'applique
  pas. Écartée.
- **Divergence ou saturation** : une perte ou des paramètres non finis auraient arrêté plus tôt (`SondeEnEchec`) ; l'écart est
  fini. La saturation (logits grands au début : la première époque d'Adam déplace chaque poids de 0,05, soit une variation de score
  de l'ordre de 0,05 × Σ|z| sur 4 096 dimensions réduites) fait partie du régime instable (§ 4, pertes de 5 à 8 à 3 époques).
- **Ordre des opérations** : c'est le mécanisme retenu. Sur la carte, moyenne et écart type (réduction de torch sur la carte, et non
  de numpy), produits (cuBLAS), perte moyenne, gradient (somme sur 143 000 jetons) et rétropropagation du maximum ne
  somment pas dans l'ordre du processeur (MKL, numpy) : écarts initiaux de 10⁻¹⁶ relatifs, que la dynamique peut amplifier.
- **Données de répétition contre vraies** (sans les ouvrir) : même taille (640 actions, largeur 4 096, ≈ 224 jetons par action),
  mais la répétition est un bruit gaussien indépendant en **simple** précision ; les vraies activations sont relues de fichiers en
  **demi-précision** (`t06/lanceur_v2.ActivationsDemi.ecrire` : `astype(np.float16)`), issues de flux résiduels (couches 7, 15
  ou 23) : moyenne forte, anisotropie, jetons voisins corrélés, quelques valeurs massives, et probablement des jetons de format
  presque identiques entre eux. C'est cette forme que les essais fabriquent.

## 4. Essais sur données fabriquées (processeur, `essai-amplification-lineaire-v1.py`, `2e063fcc…`)

Code de la course appelé tel quel. Trois comparaisons contre la référence `familles.entrainer` (« ref ») : `carte` = le code de
la carte (`LotCarte` + `entrainer`) sur processeur (ne diffère que par la moyenne et l'écart type, torch au lieu de numpy) ;
`permutee` = la référence sur les **mêmes actions dans un autre ordre** (seul l'ordre des sommes sur jetons et actions change :
émulation des réductions de la carte) ; `colonnes` = la référence aux **dimensions permutées** (seul l'ordre des sommes de chaque
produit change). 640 actions d'apprentissage, 256 de contrôle tenues à part, largeur 1 024, 40 à 120 jetons par action
(≈ 51 000 jetons), demi-précision sauf `repetition` ; graines `SeedSequence` à entropie fixe écrite dans le script ; 4 fils ;
Python 3.13.18, torch 2.14.1, numpy 2.4.6 de l'environnement du dépôt (la course : Python 3.11.18, mêmes torch et numpy).
« Gabarits 0,4 » : 40 % des jetons de chaque action remplacés par des quasi-copies (bruit 10⁻³, sous la résolution de la
demi-précision à ces échelles, ou 10⁻², 10⁻¹) de cinq jetons communs à toutes les actions.

Écart du contrôle (`ecart_relatif`, comme la course), carte / permutée / colonnes ; Spearman, aires (permutée / ref), part des
actions de contrôle dont le jeton du maximum change, et perte finale de la ref, à 300 époques :

| jeu (sortie, sha256) | l2 | 3 époques | 300 époques | Spearman | aires | jeton du max | perte |
|---|---|---|---|---|---|---|---|
| `1-repetition` (16238168…) | 0.001 | 6.02e-15 / 1.05e-10 / 1.35e-15 | 1.33e-14 / 8.87e-11 / 7.11e-15 | 1.00 | 0.491 / 0.491 | 0.00 | 0.11 |
| `1-repetition` (16238168…) | 0.01 | 8.07e-15 / 1.01e-10 / 1.05e-15 | 2.84e-14 / 6.58e-11 / 6.22e-15 | 1.00 | 0.540 / 0.540 | 0.00 | 0.20 |
| `1-repetition` (16238168…) | 0.1 | 8.86e-15 / 1.19e-10 / 1.96e-15 | 1.87e-14 / 1.92e-11 / 3.55e-15 | 1.00 | 0.466 / 0.466 | 0.00 | 0.48 |
| `2-gabarits04` (8b9f72f5…) | 0.001 | 3.36e-14 / 3.42e-11 / 1.94e-16 | 3.99e-5 / **5.18e+0** / 3.67e-6 | 0.42 | 0.840 / 0.811 | 0.99 | 0.64 |
| `2-gabarits04` (8b9f72f5…) | 0.01 | 3.34e-14 / 3.40e-11 / 0.00e+0 | 1.70e-9 / **4.30e+0** / 6.02e-11 | 0.44 | 0.729 / 0.686 | 0.97 | 0.61 |
| `2-gabarits04` (8b9f72f5…) | 0.1 | 3.44e-14 / 3.51e-11 / 0.00e+0 | 2.07e-6 / **1.32e+0** / 1.43e-7 | 0.91 | 0.669 / 0.701 | 0.25 | 0.68 |
| `3-gabarits04-sans-signal` (45f23021…) | 0.001 | 9.23e-15 / 1.24e-12 / 0.00e+0 | 7.94e-6 / **3.80e+0** / 3.96e-8 | 0.16 | 0.508 / 0.486 | 0.97 | 0.76 |
| `4-gabarits04-anisotrope` (c68b7176…) | 0.001 | 3.45e-15 / 7.83e-12 / 1.73e-16 | 9.99e-9 / **1.41e+0** / 3.01e-8 | 0.75 | 0.942 / 0.961 | 0.82 | 0.51 |
| `5-gabarits04-bruit1e-2` (5c7973e9…) | 0.001 | 2.42e-14 / 3.39e-11 / 2.19e-16 | **3.83e+0** / **1.28e+1** / 1.93e-4 | −0.04 | 0.607 / 0.575 | 1.00 | 2.89 |
| `6-gabarits04-bruit1e-1` (dcee3070…) | 0.001 | 6.63e-15 / 3.41e-11 / 0.00e+0 | 7.37e-10 / 4.94e-7 / 9.92e-12 | 1.00 | 0.657 / 0.657 | 0.00 | 1.16 |
| `7-sans-gabarits` (858448f8…) | 0.001 | 1.41e-14 / 1.10e-14 / 8.88e-16 | 8.44e-15 / 9.55e-15 / 5.77e-15 | 1.00 | 0.506 / 0.506 | 0.00 | 0.61 |

(Sorties complètes : `sortie-amplification-<jeu>-v1.json` de ce dossier, empreintes en tête de ligne et compagnons. Le jeu
`repetition` garde son décalage propre de 0,5 ; l'option `--decalage` ne le touche pas.)

Lecture :
- **Sans quasi-copies** (`repetition`, `sans-gabarits`, et neuf autres jeux d'un balayage préalable joué avec des versions
  intermédiaires du script, sorties non gardées : signal fort ou nul, corrélation 0,99, valeurs massives ou non, bruit fort), tout
  reste sous 10⁻¹⁰ : la linéaire est stable, comme la v3 l'avait supposé. Au même balayage, 20 % de quasi-copies donnaient déjà
  4·10⁻⁶ (signal faible) et 6,6·10⁻⁴ (signal fort) à l2 10⁻³, mais restaient sous 10⁻⁷ à l2 10⁻² et 10⁻¹.
- **Avec quasi-copies**, la sonde de 300 époques **dépend de l'ordre des sommes** : écart du contrôle 1,3 à 12,8 (l'arrêt de la
  course : 1,004), **même à forte régularisation** ; dans le cas 5, **même le code de la carte joué sur le processeur** s'écarte de
  3,83 du paquet gelé, par la seule moyenne et le seul écart type. Les aires du contrôle diffèrent entre piles de 0,02 à 0,04
  (0,840 contre 0,811) : la sonde lue n'est pas seulement imprécise, c'est une autre sonde.
- **À 3 époques**, toujours ≤ 1,2·10⁻¹⁰ (6 ordres sous la tolérance).
- **Trajectoire** (`sortie-amplification-8-trajectoire-gabarits04-v1.json`, `6fbddcc8…` ; boucle répliquée égale au bit près au
  code de la carte et au paquet gelé, vérifié et écrit) : sur le cas 2 (l2 10⁻³), l'écart des poids entre `carte` et `ref` reste à
  10⁻¹⁴ jusqu'à l'époque 150, puis croît (2,3·10⁻¹³ à 150 ; 6,0·10⁻¹⁰ à
  200 ; 3,4·10⁻⁷ à 250 ; 2,2·10⁻⁶ à 300) : **instabilité exponentielle** de la fin d'apprentissage, sans changement du jeton du
  maximum dans les actions d'apprentissage sur cette paire, avec des quasi-égalités au maximum (plus petit écart relatif entre le
  premier et le second jeton : 0 à l'époque 1, 10⁻⁸ ensuite). Entre les époques 150 et 250, environ un ordre de grandeur toutes
  les 15 à 18 époques, plus lentement ensuite. La pile `permutee`, dont l'écart à 3 époques est mille fois plus grand
  (3,4·10⁻¹¹ contre 3,4·10⁻¹⁴), finit à l'ordre 1 (5,18).
- **Échelle** : largeur 1 024 et ≈ 80 jetons par action contre 4 096 et ≈ 224 à la course : non joué à la taille réelle (calcul
  léger) ; plus de dimensions et plus de jetons ne peuvent qu'ajouter des quasi-égalités.

## 5. Cause la plus probable, et ce qui n'est pas exclu

**Retenue** : amplification d'arrondi par la sonde linéaire au maximum sur 300 époques, sur des vraies activations portant des
jetons presque identiques (quasi-égalités au maximum) ; la carte et le processeur ont rendu deux sondes différentes, sans erreur de
chaîne. **Arguments** : chaîne identique au code ; pile de la carte saine sur données bénignes (répétition) ; écart d'ordre 1
reproduit sans carte, par le seul ordre des sommes, sur une forme de données plausible ; ordre de grandeur et forme de l'écart
(sondes différentes, non dénominateur) conformes.

**Non exclu (R4, symétrie)** : (i) une erreur de chaîne propre aux vraies données que le code ne montre pas (environ 0,25) ;
(ii) une autre amplification numérique que les quasi-copies (environ 0,15). Je n'ai pas vu les vraies données : la présence de
jetons presque identiques y est **supposée**, non vérifiée. **Discriminant sans regarder les données** : à la relance sous la
v4, une erreur de chaîne arrêterait le contrôle **à 3 époques** (les artefacts du § 6 y donnent 10⁻² à 1) ; un passage à 3
époques avec un écart d'information à 300 époques au-dessus de 10⁻⁴ confirmerait l'amplification.

## 6. Correction proposée : contrôle v4 (`validation_imbriquee_v4.py`, `ba127aa0…`)

- Pour **chaque** famille de la marche (r1 : la linéaire seule), au réglage du couple : carte contre processeur **à 3 époques**
  (même départ, mêmes graines `bbis/entrainement/sonde/<cellule>/e<k>/<réglage>`, `familles.Reglages(epoques=3)`) ≤ 10⁻⁴, sinon
  arrêt ; **déterminisme à 300 époques** (sonde de 300 époques réapprise une seconde fois sur la carte, égale au bit près), sinon
  arrêt ; sonde de contrôle en échec à 3 ou 300 époques : arrêt. Pour la linéaire, l'écart à 300 époques de la v3 est calculé et
  **écrit comme information** (`ecart_300_information`, `decide` faux), sans arrêt.
- Tirage du couple, actions, graines, tolérance, ordre trié : ceux de la v3, inchangés (`ControleCarte` v4 = `jouer` de la v3
  appelant le contrôle v4). Champ écrit lisible par `lecture_v2.exiger_controle_carte` **sans changement** (essai 2 et 7).
- Coût en plus de la v3 : sur la carte, une linéaire de 3 époques et une linéaire de 300 (copie) — quelques secondes à la taille
  de la course (répétition : 1,75 s par linéaire de 300 époques) ; sur le processeur, une linéaire de 3 époques.

**Essais** (`essai_controle_v4_v1.py`, `d93289e9…` ; sortie `sortie-essai-controle-v4-v1.txt`, `7a47be47…` : **16 passés**,
92 s). « Carte émulée » : le code de la carte appelé tel quel sur les mêmes actions permutées (autre ordre des sommes, même
problème, même départ).
1. **Cas sain qui reproduit l'arrêt** (jeu « gabarits 0,4 », largeur 1 024, l2 10⁻³) : le contrôle **v3** arrête la carte émulée,
   « lineaire à 300 époques : contrôle carte-processeur : écart relatif 6.247e+00 > 0.0001 : arrêt (erreur de chaîne) », sans
   aucune erreur de chaîne.
2. **Cas après correction**, même jeu, même carte émulée : la **v4** passe — linéaire à 3 époques 3,3·10⁻¹¹, attention à 3
   époques 7,7·10⁻⁹, déterminisme des deux familles au bit près ; information à 300 époques 6,247 écrite ; lu par `lecture_v2`.
3. Cas sain sur la forme de la répétition : passe (information à 300 époques ≤ 10⁻⁴).
4. Artefacts à 3 époques, arrêt pour chacun : poids altérés de 1 % (linéaire 1,08·10⁻², attention 1,05·10⁻²), régularisation
   ×100 (4,5·10⁻¹ ; 1,06), une étiquette inversée (6,2·10⁻¹ ; 8,2·10⁻¹), autre graine de l'attention (9,9·10⁻¹), lot d'autres
   données (arrêt).
5. Non-déterminisme de la linéaire à 300 époques (un poids changé d'un flottant) : arrêt. 6. Sonde de contrôle en échec à 3 et à
   300 époques : arrêt. 7. Lecture : écart à 3 époques de 2·10⁻⁴ ou déterminisme de l'attention absent : refus. 8. Horizon hors
   de [1, 300[ : refus.

**Ce que la v4 ne fait pas** : elle ne rend pas la sonde de 300 époques reproductible d'une pile à l'autre ; elle cesse de le
prétendre. Si les vraies données sont de la forme du § 4, les aires lues des sondes linéaires dépendent de la pile (ici de 0,02 à
0,04), et le choix du réglage (ex aequo à 0,005) peut en dépendre aussi : la réserve R-PILE doit couvrir la linéaire.

## 7. La correction change-t-elle ce que le texte gèle ? Oui : écart à déclarer

Le texte scellé (`0ae6210f…`) et son addendum (`f00eda8a…`) gèlent, aux fragments remplacés :
- **EC-1** (plan, point 5) : « la linéaire à 300 époques, l'attention à **3 époques** … écart … ≤ 10⁻⁴ pour chacune … la sonde
  « attention » de 300 époques du couple est réapprise une seconde fois sur la carte » → la v4 contrôle la linéaire **à 3 époques**,
  ajoute son déterminisme à 300 époques et une information non décisive ;
- **EC-4** (liste d'arrêt) : « (linéaire à 300 époques, attention à 3 époques ; plan, point 5), sonde « attention » du couple non
  déterministe » → les deux familles à 3 époques, les deux non déterministes ;
- **EC-8** (épreuves) : « égalité carte-processeur (linéaire à 300 époques, attention à 3 époques ; … » ; **EC-5**, **EC-7** :
  noms `validation_imbriquee_v3`, `lanceur_bbis_v3.sh`, `amorce_bbis_v3.sh` (il faut une `marche_v4` qui importe la v4, et lanceur
  et amorce v4 ; non écrits ici) ;
- **EC-2, EC-3** (critères de lecture gelés, réserve toujours écrite et point (7) de la section D) : limités à la famille
  « attention » → à étendre à la linéaire (texte de la réserve seulement ; une `lecture_v3` devrait l'écrire : `reserve_pile` de
  `lecture_v2` ne compte que l'attention).

**Inchangés** : hypothèse, prédiction et signe, métrique, seuils et niveaux, tolérance 10⁻⁴, 256 actions, couple tiré (graine
`bbis/egalite-carte`, ordre trié), formes des clés de graines (aucune clé neuve), plis externes et internes, grille, 300
époques et pas 0,05 des sondes **lues**, choix du réglage, plancher, nul, notation, garde de débit, budget. La ligne d'arrêt dit
« correction du code sous un nom neuf, ligne `CODE-BBIS` remplacée une seule fois, relance sous ce texte » : la v4 n'est pas
une relance « sous ce texte » ; elle demande un **second addendum d'écart**, contre-lu et scellé avant `CODE-BBIS` remplacée,
puis la relance unique de GO-2026-11-14-09.

## 8. Points pour la mère

- Décision à porter à Lazar : **second addendum (contrôle v4 et R-PILE étendue à la linéaire)** ; recommandation : oui,
  confiance moyenne ; options : (a) v4 + addendum (recommandé) ; (b) relancer sous le texte actuel (déconseillé : même couple,
  mêmes données, même arrêt très probable, et la relance unique serait consommée) ; (c) contrôle sur la seule attention, sans
  linéaire (déconseillé : la linéaire n'aurait plus aucun contrôle de chaîne).
- La v4 coûte tout l'apprentissage à la relance (le contrôle vient à la fin, addendum § 5, point 8) ; aucun travail de la course
  arrêtée n'est réutilisable (aucun score écrit).
- La présence de quasi-copies dans les vraies activations n'est pas vérifiée ; l'information à 300 époques de la v4 le dira sans
  ouvrir de données hors de la marche.
- Incident : le dossier demandé « neuf » existait déjà, avec un fichier `essai-sensibilite-lineaire-v1.py`
  (`679f180882816869df7a57039fb8e14cf11eae9555b5c023ad7f98dafb2cb2a9`, modifié à 21:52:00Z, non scellé, auteur inconnu de moi,
  sans sortie) : lu, **ni modifié, ni joué, ni scellé** ; mes pièces portent d'autres noms.

## 9. Déclaration

Rôle : développeur neuf, diagnostic seulement ; lettre de modèle : A. Heures : 2026-11-16, 22:05:58Z – 22:44Z (`date -u`) ;
essais joués de 22:29:22Z à 22:40:14Z. Pièces lues (empreintes aux § 2 et § 3) : le code ci-dessus, `prereg/T0.7-etape-B-bis-v1.md`
(`0ae6210f…`) et `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` (`f00eda8a…`), la ligne R-2957 de `registres/decisions.md`
(fichier `bd4732e2…`), `diagnostic-ecart-attention-carte-v1.md` (`5ecb9235…`, lignes sur la linéaire), les pièces permises de
`donnees/t07-etape-b-bis-v1` (§ 2) et la répétition v4. **Jamais ouverts** : `relecture-bbis.json` (ni ses clés), toute donnée,
activation ou sortie de 7a et de 7b, toute sortie de l'étape B de T0.7, toute valeur de clé ; ni `env` ni `printenv` ; aucune
machine, aucun appel au loueur, aucune dépense ; aucun fichier existant modifié ; rien committé. Incident : § 8, dernier point.
