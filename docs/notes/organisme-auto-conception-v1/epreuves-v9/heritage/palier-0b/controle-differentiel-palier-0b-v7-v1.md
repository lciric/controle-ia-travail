# Contre-lecture — préenregistrement du palier 0b, différentiel v6 → v7 — v1

- Auteur : contre-lecteur, modèle O, neuf. Je n'ai écrit ni le texte ni le code. Écart déclaré à la règle « même contre-lecteur » (mandat). Pièce de travail (classe C).
- Date : 2026-11-20, de 04:21Z à 04:45Z environ (`date -u` à 04:34Z en cours de travail).
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-contre-lecteur-palier-0b-v7-v1.md` (`d32a978ef2e33f14a73b33c50a24666d575ef23375d50f2ee8d6c279f46f61cc`), vérifié par son compagnon avant tout geste. Trois questions de la mère (R-4076), reçues en cours de travail par la session qui m'a lancé : réponses au § 4.
- Conditions : processeur seul. Aucun tirage, aucun étalonnage, aucun audit, aucun lancement du code de l'étage. Aucun appel à un fournisseur de modèles, aucune dépense, aucun réseau. Aucune écriture dans le dépôt, aucun commit. Rien lu sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Python 3.13.18. Deux programmes lancés par leur chemin : l'outil de remplacement du dépôt (rejeu, sortie dans mon dossier) et mon calcul à la main `calcul_reserve_23_v1.py` (fonctions de répartition normales, aucune graine). Quatre `git show` redirigés vers mon dossier. **Aucun refus de permission, de classifieur ni de garde.**

Dossier P0B : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Verdict

**Conforme après corrections.** La v7 est exactement la v6 plus les 30 remplacements. Les trois remplacements de tenue sont à la lettre. La table des 51 empreintes et le commit sont justes. Il faut **une correction de fond** : la règle calibrée (règle 3) étendue aux deux audits de lois dépend de l'arrêt attendu. Elle doit se restreindre aux trois audits des mondes par dose (corrections 1 à 9). S'y ajoutent une correction de justesse sur la réserve 23 (correction 6) et quatre de tenue ou de silence (corrections 10 à 16). Aucune ne touche un des six critères, une valeur gelée ou une prédiction. Les nœuds 1 et 2 restent à Lazar, sans défaut.

## 1. Empreintes vérifiées

Toutes sont égales à leur compagnon, et aux préfixes du mandat :

| pièce (P0B/) | empreinte |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v7.md` | `2f0f928f291b65a98bff2680e6bb7172bcf279da7e76b16bd837193f0704f4f0` |
| `remplacements-preenregistrement-palier-0b-v6-v7.json` | `a20a925fbd3022686d74c92467483da2a48b7fb5d74c393f3711e738b6a735a9` |
| `…-v7.md.journal-remplacements-v1.json` | `e137dc922d8cd9f74ea70f7a4f3aaeba32baf8c80c91682eb63457294fc4070e` |
| `differentiel-preenregistrement-palier-0b-v6-v7.diff` | `4dc998f4eab95b0e9e2ca8bb7e6e6d3c1594f6b33be6293bcab984872d4a7d07` |
| `rapport-redacteur-palier-0b-v7-v1.md` | `c06c2870a191fa90bedc2effe3e82078bbb625bb6c46e867f0e3e689b75d0736` |
| `table-empreintes-code-v3-extraite-du-rapport-v1.txt` | `91e8e96e76646f834d470ffa0c5863ed3f67bc42a79b1912e3f23c50f9522529` |
| `mandat-redacteur-palier-0b-v7-erratum-du-commit-v1.md` | `9f948bb1718214d81304c77144f9d10b041663b2991b50f7410e7c70cb19b0af` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v6.md` | `4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029` |
| `controle-differentiel-palier-0b-v6-v1.md` | `c079a89d…` (compagnon OK) |
| `code-v2/rapport-developpeur-code-palier-0b-v2.md` | `ca61bf7e89aefe7ffe9e7a62e80ff7da1653668542f8fbd8498909a10e409b75` |
| `code-v2/contre-lecture-v1/contre-lecture-code-palier-0b-v2-v1.md` | `3778fb395dae1e2003ce8236f93c77cfbd6bc78c355417bf0b40e0b5e694c5e5` |
| `code-v2/contre-lecture-v1/outils-cl/bruit_nul_doses.py` | `a765ed8bd7e97ae3e1710bf30d4a1f08c420fde55663a0a93d6392210da6b0c7` (lu, non lancé) |
| `code-v3/rapport-developpeur-code-palier-0b-v3.md` | `5e3fa3e8…` (compagnon OK) |
| `code-v3/verification-v1/verification-corrections-code-palier-0b-v3-v1.md` | `c5c211c7…` (compagnon OK) |
| `scripts/remplacer_texte_exact_v1.py` (racine du dépôt) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

## 2. Point 1 — le différentiel est exactement les 30 remplacements

- **Rejeu** : l'outil `391db990…`, appliqué à la v6 `4aee136b…` avec le JSON `a20a925f…`, sortie dans mon dossier. Résultat : 30 remplacements, sortie `2f0f928f…`, égale à la v7 à l'octet (`cmp` muet).
- **Journal rendu** : outil `391db990…`, cible `4aee136b…` (181 077 octets), sortie `2f0f928f…` (228 894 octets), 30 remplacements, aucun avertissement. Mon journal ne diffère que par l'heure et les chemins.
- **Différentiel** : refait par `diff -u`, v6 contre ma v7 rejouée. Hors des deux lignes d'en-tête (chemins et heures), il est égal à l'octet au différentiel versé.

## 3. Point 2 — les trois remplacements de tenue

Chacun des trois textes nouveaux du § 3 du contrôle de la v6 figure une fois, à l'octet, dans la v7 (`grep -c -F`, et `-f` pour le troisième) :

1. « le reprend après la relecture de la version 4, celle de la version 5 et le contrôle du différentiel de la version 6 » ;
2. l'étape 1 de l'ordre des opérations ;
3. la section « Contre-lecture ».

Aucun des trois textes anciens ne reste. Le premier se trouve désormais dans l'alinéa « Histoire, reprise de la version 6 » de la ligne du commit, avec « s'écrivait » au lieu de « s'écrit ». C'est un texte neuf autour du remplacement, non une altération de celui-ci. Conforme.

## 4. Point 3 et questions de la mère — les trois règles des écarts

### 4.1 Question 1 : d'où vient ce que le rédacteur savait ?

D'**essais du code**, tirés sur le vrai générateur B1 sous la couche de graines « essai », et d'un **calcul sous un nul gaussien** qui ne lit rien du générateur. **D'aucune sortie décisive.** Sources :

- **Signal de la longueur (règle 2).** Rapport du code v2 (`ca61bf7e…`), § 5, point 2. Sur 8 suites par dose et des graines d'essai (288 lois dépendantes, 480 indépendantes), la longueur seule donne une exactitude de 0,565. L'outil est `code-v3/outils-dev/diagnostic_forme_dependantes.py` (`10af2b5a…`). Il tire ses suites sous `couche="essai"` (sa ligne 16) et rend l'exactitude par `default_rng(1)` (lignes 33 et 47). La contre-lecture du code (`3778fb39…`, § 5.2) ne fait aucun tirage neuf. Elle recoupe ce chiffre par le calcul (d ≈ 0,3, exactitude ≈ 0,56, incertitude ≈ 0,01 à pleine taille) et en tire « l'arrêt à pleine taille est probable ».
- **Bruit des audits par dose (règle 3).** Rapport du code v2, § 5, point 3 : 8 suites par dose, graines d'essai, exactitudes de 0,34 à 0,59 selon la graine de validation croisée. L'outil est `code-v3/outils-dev/diagnostic_presentation.py` (`8b2ba07b…`, `couche="essai"`, sa ligne 15). La contre-lecture du code, § 5.3, s'appuie sur `bruit_nul_doses.py` (`a765ed8b…`). Ce dernier tire des **traits gaussiens indépendants** sous une graine locale 424242, sans aucune couche du dispositif, et ne reprend du code que la fonction `exactitude_equilibree`. D'où 0,032, 4,8 % et « 11 à 14 % ».
- **Absence de sortie décisive.** Le rapport du code v2, § 6, dit qu'aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » n'a été dérivée hors des essais de refus. La contre-lecture du code, § 2.7, dit que le journal ne porte que « essai » et « essai-de-forme ». Je n'ai pas relu ce journal ; je m'appuie sur ces deux pièces et sur la lecture des deux outils.
- **Nuance qui compte pour R4.** Les essais tirent sur **le même générateur** et lisent **le même classifieur** que l'étape 3, sur moins de suites et sous d'autres graines. Ce n'est pas une sortie décisive, mais c'est un **avant-goût de la porte de l'étape 3**. Le rédacteur le déclare (réserve 22).

### 4.2 Question 2 : les règles ont-elles été choisies pour que l'étape 3 passe ?

**Règle 2 (longueur de forme).** Son moment dépend de l'attente : elle est écrite parce que l'essai a vu le signal. Son contenu n'en dépend pas, pour trois raisons :

- Elle applique la dichotomie que la v6 pose déjà : la forme est faite des jetons, nombres neutralisés ; le contenu est fait des normes et de l'entropie. La raison « pour que la valeur des nombres n'entre pas dans la forme » n'est pas écrite en toutes lettres dans la v6 (ligne 149) : c'est une lecture du rédacteur, mais une lecture juste de la règle des jetons.
- Le complément du rédacteur (la longueur brute passe au contenu) garde le signal, et une exactitude de contenu au-dessus de 0,55 lie l'étage payant.
- Aucun proposeur écrit par programme ne lit la longueur d'une loi (table B7, v7, lignes 276-286). Le signal ne touche donc aucun des six critères ; il ne vaut que pour l'étage payant, où la règle le garde liant.

Son effet est réel, et la mère doit l'entendre : un arrêt probable devient un signalement probable qui lie l'étage payant. Le compte n'est pas évité, il est reporté avant tout préenregistrement payant ; la voie de la réserve 18 reste alors à prendre. **Jugement : la règle 2 ne vise pas un passage ; elle est acceptable comme nœud.**

**Règle 3 (règle calibrée).**

- **Sur les trois audits des mondes par dose**, elle ne dépend pas de l'attente : le défaut de calibrage est établi sous un nul pur, sans rien du générateur.
- **Son extension aux deux audits de lois en dépend**, à mon jugement. Sur ces audits il n'y a aucun défaut de calibrage : avec σ₀ ≈ 0,01, la lettre n'arrête un générateur parfait qu'environ 3·10⁻⁷ fois. L'extension n'a donc qu'un effet : tolérer les exactitudes de 0,55 à 0,57 environ, là même où les essais placent le signal de la longueur. Calcul à la main (§ 4.4) : une exactitude vraie de 0,56 arrête 0,84 fois à la lettre et 0,16 fois sous la règle calibrée ; 0,565 arrête 0,93 contre 0,31.
- Cette extension fait aussi dépendre les nœuds l'un de l'autre. Avec le nœud 1 en (b) (lettre) et le nœud 2 en (a), l'arrêt attendu disparaîtrait par la règle 3 seule, et l'inconvénient de l'option (b) du nœud 1 (« arrêt probable ») deviendrait faux.
- La raison du rédacteur (« une seule règle ; σ₀ petit, la règle reste proche de la lettre ») décrit justement la bande où se trouve le signal attendu. **Correction : restreindre la règle calibrée aux trois audits des doses** (corrections 1 à 5 et 7 à 9). Les deux nœuds se tranchent alors l'un sans l'autre.

**Options qui ne dépendent pas de l'attente** :

| règle | option | avantage | inconvénient |
|---|---|---|---|
| 2 | (b) lettre de la v6 | rien n'est changé après un diagnostic | arrêt probable, sur un signal réel rangé sous la forme, puis un erratum de toute façon |
| 2 | (c) même filtre pour toutes les sous-lois — la voie que la réserve 18 de la v6 écrivait d'avance pour un échec sur la forme | traite la cause, et suit un texte écrit avant le diagnostic | change le générateur gelé, la loi des lois et les fréquences ; code lourd ; jamais éprouvé |
| 2 | (a) de la v7 (longueur aux jetons, longueur brute au contenu) — dépend de l'attente par son moment seulement | la forme ne lit plus le contenu ; le signal reste lu et liant pour l'étage payant | écrite après un diagnostic ; un arrêt probable devient un signalement |
| 3 | (a′) règle calibrée sur les trois audits des doses seulement (proposée ici) | corrige le calibrage là où il est démontré faux, sur un nul pur ; ne touche pas les audits de lois | deux régimes de lecture pour les cinq exactitudes de forme ; voit mal un petit défaut des doses (réserve 23) |
| 3 | (b) lettre de la v6 | aucun seuil ne bouge | alarme à tort de 11 à 14 fois sur cent sur les doses ; un arrêt n'y dirait rien du générateur |
| 3 | (c) lettre sur 100 suites par dose | seuil inchangé ; alarme à tort de 1,1 % par paire | la valeur de 50 change ; construction doublée, de temps non mesuré ; pas de marge |

### 4.3 Question 3 : une règle choisie avant toute sortie décisive, après avoir vu le code sur des mondes inventés, est-elle acceptable ?

**Oui, sous trois conditions** : sa justification tient sans l'attente ; elle ne retire rien de ce que la porte doit voir pour ce qui compte ; elle est déclarée et contre-lue avant le scellement. Règle par règle :

- **R1.** Aucune lecture de résultat avant scellement. Les essais du code ont leur couche, disjointe de « audit » et des couches décisives (B8). L'annexe C permet d'exécuter le code avant le scellement, et ce que les essais ont lu n'est ni un critère ni un résultat de l'étage. Écrire la règle **avant** l'audit vaut même mieux, au regard de R1, que la voie de la v6 : la liste d'arrêt, point 2, ligne 356 de la v6, prévoit d'arrêter **puis** de changer la définition par un erratum, donc après lecture de la sortie de la couche « audit ».
- **R3.** L'audit n'entre dans aucun critère. Une règle ne vise pas un signe si sa justification est indépendante de l'issue attendue. C'est vrai de la règle 2 et de la règle 3 sur les doses ; ce ne l'est pas de l'extension aux audits de lois (§ 4.2).
- **R4.** La symétrie demande la même règle si l'essai avait montré l'inverse. Pour le calibrage des doses, oui : la règle calibrée corrige les deux côtés (moins d'alarme à tort, mais une zone médiane liante). L'histoire du texte montre aussi un durcissement après diagnostic : la v4 a rendu l'audit plus sévère à seuil égal. La réserve 22 déclare ce que le rédacteur savait.

**Ce que la v6 dit de ce cas** (`4aee136b…`) :

- **Réserve 19** (ligne 460). La stratification de M12 a été écrite après un diagnostic sur des graines « essai », avec trois garde-fous : graines disjointes pour la vraie garde ; aucune strate sans erratum contre-lu ; « un nouveau désaccord est un arrêt, non une strate de plus ». C'est le précédent exact : la v6 l'admet une fois, déclaré et gardé.
- **Réserve 18** (ligne 459). Pour un échec sur les traits de forme : « c'est un arrêt », et « la voie à écrire alors, par un erratum contre-lu, serait de faire passer toutes les sous-lois d'une suite par un même filtre ». La v6 avait donc écrit d'avance un remède, l'option (c) du nœud 1. Le nœud doit le dire (correction 11).
- **Réserve 17** (ligne 458) : la marge de 0,30 nat et les bornes viennent des essais du développeur sur des graines « essai ».
- **Liste d'arrêt, point 2** (ligne 356) : l'audit échoue, arrêt, puis la définition se change par un erratum contre-lu avant tout tirage.
- **Annexe C** (essai de forme) : ses sorties « ne sont jamais lues comme un critère ».
- **Version 4 entière (annexe F)** : erratum de conception écrit après que le développeur eut trouvé des points impossibles à coder.

**En une phrase** : la v6 admet qu'une règle soit écrite après un diagnostic sur graines d'essai, si c'est déclaré, contre-lu et gardé ; elle interdit qu'un nouvel ajustement remplace un arrêt sans erratum ; et elle avait écrit d'avance le remède d'un échec de forme.

### 4.4 Calcul à la main de la réserve 23 (refait)

Programme : `calcul_reserve_23_v1.py` (`354731b35dde1946052d3dbb9506de19a8977849bae8838b7d3ef510fada279a`), sortie `calcul_reserve_23_v1.sortie.txt` (`d692b301960545ea1173689dd056a8e81bf9058c61bd85ccf8b56ae29dfb2dfa`), dans mon dossier. Il suppose une loi normale, d'écart-type de A égal à σ₀, comme le rédacteur.

| cas (audits des doses, une paire) | σ₀ = 0,032 (seuil 0,614) | σ₀ = 0,045 (0,640) | σ₀ = 0,064 (0,678) |
|---|---|---|---|
| générateur parfait, arrêt | 1,8·10⁻⁴ (5,5·10⁻⁴ sur trois paires) | 9,3·10⁻⁴ | 2,7·10⁻³ |
| exactitude vraie 0,60, arrêt | **0,331** | 0,187 | 0,111 |
| exactitude vraie 0,65, arrêt | **0,870** | 0,588 | 0,331 |
| exactitude vraie 0,60, A > 0,55 (liant) | 0,941 | 0,867 | 0,783 |

- Les chiffres du rédacteur sont justes **à σ₀ = 0,032** : « moins d'une fois sur mille », « une fois sur trois », « près de neuf fois sur dix ».
- Audits de lois (σ₀ = 0,01, seuil 0,57) : une exactitude vraie de 0,60 arrête 0,9987 fois (« presque toujours », juste).
- **Mais** 0,032 est le σ₀ de mondes indépendants (`bruit_nul_doses.py`). Sous la permutation entre suites que la v7 prescrit, si les quatre mondes d'une suite se ressemblent, σ₀ grandit, jusqu'à 0,064 environ s'ils étaient identiques. L'arrêt à 0,60 tombe alors vers une fois sur neuf. La réserve doit le dire (correction 6).

## 5. Point 4 — les classements

- **Écart 1 en proposition avec défaut** : d'accord. Le texte ne disait pas la dose du jeu de la garde 27, aucune valeur gelée ni aucun seuil ne bouge, et le bras est sans critère. Réserve : la règle retire une garantie à la dose 0,5. Ce n'est pas une « revendication » au sens de la hiérarchie (hypothèse ou papier), mais une propriété de l'instrument. Si la mère la lit autrement, c'est un nœud sans défaut.
- **Causes d'arrêt ajoutées (D8, D9, choix 6) en information** : d'accord. Elles vont dans le sens de l'arrêt, remplacent des replis silencieux (R5) et ne changent aucun seuil, comme aux versions 4 et 5. La correction 4 en ajoute une de même nature.
- **Choix 11 en information** : d'accord. La ligne « taux d'échec » de la table des valeurs gelées porte sur « les cases qui décident », et le lecteur aux deux réglages ne décide de rien.
- **Nœuds 1 et 2 sans défaut** : juste. Après la correction 1, le nœud 2 reste un nœud, puisqu'il change ce qui vaut dépassement pour les doses.

## 6. Point 5 — silences, choix 11 et 12, notes D5, D6, D8, D9, contre le code v3

Chemins relatifs à `P0B/code-v3/src/controle_ia/heritage_etage_processeur_v1/`.

- **Choix 10** (`audit.py`). Le jeton est un mot, un nombre (signe et exposant compris) ou un signe de ponctuation (l. 150) ; un nombre d'au moins quatre décimales donne `<nombre>`, signe absorbé (l. 155-158) ; la longueur est `len(texte)`, en caractères (l. 169) ; un trait de variance nulle est centré sans être réduit (l. 200). Juste.
- **D9** (`audit.py`). Les plis viennent d'une permutation sans stratification (l. 194-195) ; un centre est calculé sur une classe peut-être absente (l. 202, `argmin` l. 204). La règle est juste. **Silence voisin non inscrit** : `exactitude_equilibree` rend `None` sous cinq exemples d'une classe (l. 191-193), et `audit_presentation` le range en « non_calculees » sans arrêter (l. 239-243). Correction 4.
- **D6** (`constantes.py` l. 8 ; `graines.py` l. 85-103). La constante porte l'empreinte de la v6 ; `Autorisation` exige le texte, l'erratum et leurs compagnons, et que l'erratum cite l'empreinte du texte, sans la comparer à la constante. Le constat et la règle sont justes. Le « fichier d'autorisation du lancement » n'est défini nulle part dans la v7 (deux mentions) ; sa forme revient au code v4 et à la mère (remarque).
- **Choix 9** (`graines.py` l. 22-23 pour le champ `tour`, juste). **La liste des rôles est incomplète** : le code emploie aussi `role="source"` (`etapes.py` l. 186, `tirages.py` l. 81, `etalonnage.py` l. 75) et `role="intervalle"` (`etapes.py` l. 190). Correction 12.
- **Choix 6 et D8** (`etalonnage.py`). Au plus 40 pas (l. 129) ; « non convergé » arrête à l'étape 6 (`etapes.py` l. 222-223) ; une taille `nan` tombe en « non atteignable » (l. 97, l. 120-122). Écarts-types aux taux 0 et 0,5 : `etapes.py` l. 229-235. Juste.
- **Choix 11** (`etapes.py` l. 65-69) : taille de référence, taux de 0,25. Juste.
- **Choix 12** (`tirages.py` l. 219-228) : nombre et empreinte de la liste triée, aucun fichier de la liste. Juste.
- **Choix 8** (`mecanique.py` l. 48-50 et l. 276) : la première tentative notée l'emporte, les bras sont pris dans l'ordre joué. Le code v3 suit déjà la règle ; le point 5 de « Ce qui demande un code v4 » peut être levé par le vérificateur du code.
- **Garde 27 au bras 4b** (`registre.py` l. 278-295) : les artefacts que la v7 ajoute existent déjà dans le code v3. Juste.
- **D5** : laissée, motivée. Juste : aucun résultat n'en dépend.

## 7. Point 6 — erratum du commit sous condition

- `3d332d2c` se résout en `3d332d2c6be171a2c73b4aa14472d309ede87553`. C'est un ancêtre de `origin/lot/compte-organisme-v1` (`a3711ecc…`) et de `HEAD` (`git merge-base --is-ancestor`, code 0). La branche citée est donc juste.
- **Les 51 empreintes de la table recalculées sur disque** (`sha256sum -c` de la table, dans `code-v3/`) : 51 OK. Au commit, quatre modules sortis par `git show` vers mon dossier (`audit.py`, `constantes.py`, `graines.py`, `tirages.py`) ont l'empreinte de la table.
- La table de la v7 (lignes 10-60, indentation de deux espaces retirée) est égale à l'octet à la table extraite, elle-même égale aux lignes 605-655 du rapport du code v3.
- **Liste du code v4** : complète pour ce que la v7 change, avec deux ajouts.
  - Par la correction 4 : l'arrêt sur une exactitude non calculable.
  - Par la correction 1 : le cas d'un audit de lois au-dessus de 0,55 dans les essais.
  - Remarque sur le point 5 : `etape_4` (`etapes.py` l. 149-168) ne joue que les bras 1 à 3. Le code v4 doit dire où se joue le jeu de la garde 27 et à quelle dose, non seulement « vérifier que l'étape 4 le joue ».

## 8. Points 7 et 8 — nœuds au format ; identifiants de modèle

- **Nœuds** (annexe H et rapport, § 8) : décision en une phrase ; enjeu ; trois options, chacune avec avantage et inconvénient ; recommandation et confiance ; défaut. Le format est tenu, et le défaut est « aucun » pour les deux nœuds, comme il se doit. Deux inexactitudes de présentation, corrigées par les corrections 10 et 11 :
  - l'option (b) du nœud 1 dit d'un arrêt qu'il « ne dit rien de l'instrument », alors qu'il dirait un fait réel du générateur ;
  - l'option (c) ne dit pas que la réserve 18 l'avait écrite d'avance.

  Le rapport, § 8, est une pièce du rédacteur et ne se réécrit pas : c'est l'annexe H corrigée qui va à Lazar.
- **Identifiants de modèle** : aucun dans la v7. Dans le différentiel et le rapport, les seules occurrences sont le chemin `/tmp/claude-0/…`, un nom de dossier et non un identifiant de modèle.

## 9. Corrections (remplacements exacts dans la v7)

Chaque texte ancien figure **une seule fois** dans la v7 (`grep -o -F -f`, motifs dans `rejeu/a01.txt` à `a14.txt` de mon dossier). Les remplacements ne se chevauchent pas. À appliquer par l'outil `391db990…`, sous un nom neuf (v8), avec un alinéa de tenue à l'annexe H.

**Correction 1 (fond ; section « Seuil »).**
- Ancien : `**les exactitudes lues sur les traits de forme décident (liste d'arrêt, point 2), selon la règle calibrée écrite à la fin de cette puce (version 7, sous réserve du nœud 2 de l'annexe H ; la version 6 écrivait « chacune au plus 0,55 ») ;`
- Neuf : `**les exactitudes lues sur les traits de forme décident (liste d'arrêt, point 2) : celles des deux audits de lois, chacune au plus 0,55, comme la version 6 l'écrivait ; celles des trois audits des mondes par dose, selon la règle calibrée écrite à la fin de cette puce (version 7, sous réserve du nœud 2 de l'annexe H ; la version 6 écrivait « chacune au plus 0,55 ») ;`

**Correction 2 (fond ; « Seuil »).**
- Ancien : `Trois lectures d'une exactitude de forme : **A au plus 0,55**`
- Neuf : `Trois lectures d'une exactitude de forme d'un audit des mondes par dose : **A au plus 0,55**`

**Correction 3 (fond ; « Seuil »).**
- Ancien : `seules les cinq de forme décident.`
- Neuf : `seules les cinq de forme décident : les deux des audits de lois à la lettre de la version 6 (au-dessus de 0,55, arrêt), les trois des audits des mondes par dose selon ces trois lectures (annexe H, écart 3).`

**Correction 4 (silence, R5 ; « Seuil »).**
- Ancien : `un pli d'entraînement où une classe manque, ou un centre de classe non fini, arrête l'audit, à la lecture observée comme sous permutation, au lieu de rendre une exactitude (annexe H, note D9).`
- Neuf : `un pli d'entraînement où une classe manque, un centre de classe non fini, ou une exactitude qui ne peut être calculée (moins de cinq exemples d'une classe), arrête l'audit, à la lecture observée comme sous permutation, au lieu de rendre une exactitude ou de la laisser « non calculée » (annexe H, note D9).`

**Correction 5 (garde 25, artefacts).**
- Ancien : `des valeurs plantées, non tirées, de A et de σ₀ avec A entre 0,55 et 0,55 + 2 σ₀ : aucun arrêt, mention « non départagée du hasard à cette taille » ;`
- Neuf : `des valeurs plantées, non tirées, de A et de σ₀ d'un audit des mondes par dose avec A entre 0,55 et 0,55 + 2 σ₀ : aucun arrêt, mention « non départagée du hasard à cette taille » ; une exactitude de forme plantée à 0,56 dans un audit de lois : arrêt (lettre de la version 6) ; une exactitude non calculable : arrêt ;`

**Correction 6 (justesse ; réserve 23).**
- Ancien : `Pour les deux audits de lois, où σ₀ est de l'ordre de 0,01 (contre-lecture du code, § 5.2), une exactitude vraie de 0,60 arrête presque toujours.`
- Neuf : `Pour les deux audits de lois, où σ₀ est de l'ordre de 0,01 (contre-lecture du code, § 5.2), la règle calibrée ne s'applique pas : ils restent à la lettre de la version 6 (annexe H, écart 3). Le σ₀ de 0,032 est celui de mondes indépendants : sous la permutation entre suites, si les quatre mondes d'une suite se ressemblent, σ₀ est plus grand — jusqu'à 0,064 environ s'ils étaient identiques —, le seuil d'arrêt monte jusqu'à 0,68 environ, et l'arrêt d'une exactitude vraie de 0,60 tombe d'une fois sur trois à une fois sur neuf environ ; la part des exactitudes observées au-dessus de 0,55, qui lient l'étage payant, reste de 0,78 à 0,94 (calcul à la main de la contre-lecture de la version 7, par approximation normale).`

**Correction 7 (fond ; annexe H, écart 3).**
- Ancien : `- **Pourquoi les cinq exactitudes de forme et non les trois des doses** : une seule règle ; pour les deux audits de lois, σ₀ est petit et la règle reste proche de la lettre de la version 6.`
- Neuf : `- **Pourquoi les trois exactitudes de forme des doses, et non les cinq** (contre-lecture de la version 7) : le défaut de calibrage n'est établi que pour les audits des mondes par dose, sous un nul pur qui ne lit rien du générateur (contre-lecture du code, § 5.3). Pour les deux audits de lois, σ₀ est de l'ordre de 0,01 : la lettre de la version 6 n'y arrête un générateur parfait qu'environ trois fois sur dix millions, et la règle calibrée n'y ferait que tolérer les exactitudes de 0,55 à 0,57 environ, là où les essais du code placent le signal de la longueur (de l'ordre de 0,56 ; réserve 22) : une exactitude vraie de 0,56 y arrêterait de l'ordre de huit fois sur dix à la lettre, moins de deux fois sur dix sous la règle calibrée. Une extension dont le seul effet porte sur un résultat attendu dépendrait de cette attente (règles R3 et R4) : elle est écartée. Les deux audits de lois restent à la lettre de la version 6, et les nœuds 1 et 2 se tranchent l'un sans l'autre.`

**Correction 8 (fond ; écart 3, règle retenue).**
- Ancien : `entre 0,55 et ce seuil, pas d'arrêt, mais l'exactitude lie l'étage payant.`
- Neuf : `entre 0,55 et ce seuil, pas d'arrêt, mais l'exactitude lie l'étage payant ; pour les trois audits des mondes par dose seulement, les deux audits de lois restant à la lettre de la version 6.`

**Correction 9 (fond ; nœud 2, deux remplacements).**
- 9a. Ancien : `- *Décision* : une exactitude de forme arrête-t-elle l'audit seulement au-dessus de 0,55 + 2 σ₀, une exactitude entre 0,55 et ce seuil liant l'étage payant sans arrêter ?`
- 9a. Neuf : `- *Décision* : une exactitude de forme d'un audit des mondes par dose arrête-t-elle l'audit seulement au-dessus de 0,55 + 2 σ₀, une exactitude entre 0,55 et ce seuil liant l'étage payant sans arrêter, les deux audits de lois restant à la lettre de la version 6 ?`
- 9b. Ancien : `- *Recommandation* : (a) ; confiance moyenne. Les options (a) et (c) peuvent se joindre.`
- 9b. Neuf : `- *Recommandation* : (a) ; confiance moyenne. Les options (a) et (c) peuvent se joindre. L'extension de la règle calibrée aux deux audits de lois, d'abord écrite, est écartée (écart 3, « Pourquoi les trois exactitudes de forme des doses, et non les cinq »).`

**Correction 10 (présentation juste ; nœud 1, option (b)).**
- Ancien : `inconvénient : un arrêt probable à l'étape 3, qui ne dit rien de l'instrument, puis un erratum de toute façon.`
- Neuf : `inconvénient : un arrêt probable à l'étape 3, sur un signal réel du générateur (le signe des poids des lois dépendantes) rangé sous la forme ; aucun proposeur écrit par programme ne le lit, mais il vaut pour l'étage payant ; puis un erratum de toute façon.`

**Correction 11 (ce que la v6 disait ; nœud 1, option (c)).**
- Ancien : `- *Option (c), le même filtre pour toutes les sous-lois* (réserve 18) — avantage`
- Neuf : `- *Option (c), le même filtre pour toutes les sous-lois* (réserve 18, qui l'écrivait d'avance comme la voie à prendre, par un erratum contre-lu, après un échec sur les traits de forme) — avantage`

**Correction 12 (silence ; annexe H, choix 9).**
- Ancien : `le monde, les épisodes, le partage, les instances de l'oracle, les paires, l'échantillonnage, l'échec, le budget et le retrait ; la version 7 y ajoute la permutation de l'audit`
- Neuf : `le monde, la source (couche statistique), les épisodes, le partage, les instances de l'oracle, les paires, l'échantillonnage, l'échec, le budget, le retrait et l'intervalle (S8 (ii)) ; la version 7 y ajoute la permutation de l'audit`

**Correction 13 (code v4 ; annexe H, point 1).**
- Ancien : `pli privé d'une classe, arrêt. **Ces deux règles`
- Neuf : `pli privé d'une classe, ou exactitude non calculable, arrêt ; exactitude de forme d'un audit de lois au-dessus de 0,55, arrêt. **Ces deux règles`

**Correction 14 (tenue ; écart 3, « Ce que cela touche »).**
- Ancien : `la garde 25 reçoit deux artefacts de plus et son artefact de la dose se lit au seuil calibré`
- Neuf : `la garde 25 reçoit quatre artefacts de plus (zone médiane, pli privé d'une classe, exactitude non calculable, audit de lois au-dessus de 0,55) et son artefact de la dose se lit au seuil calibré`

**Correction 15 (tenue ; table « Ce que cette version touche »).**
- Ancien : `garde 25 (seuil calibré, zone médiane, pli privé d'une classe)`
- Neuf : `garde 25 (seuil calibré pour les doses, lettre pour les lois, zone médiane, pli privé d'une classe, exactitude non calculable)`

**Correction 16 (tenue ; en-tête, heure ; le rédacteur la signale, rapport § 9.5).**
- Ancien : `version 7 le 2026-11-20, de 04:08Z à 04:40Z environ`
- Neuf : `version 7 le 2026-11-20, de 04:08Z à 04:20Z environ`

Tenue de la v8 : titre, statut, heure, mandat et cette contre-lecture en tête ; un alinéa à l'annexe H qui inscrit ces seize remplacements (dix-sept en comptant 9a et 9b). Ils ne touchent ni un des six critères, ni une valeur gelée, ni une prédiction. Les corrections 1 à 3, 7, 8 et 9 restent sous le nœud 2.

## 10. Remarques non bloquantes

1. **Fuite entre mondes frères (audits des doses).** Les plis sont tirés sur les mondes, et la permutation est faite entre suites. Un monde de test a ses frères dans le pli d'entraînement, avec la même étiquette ; sous le nul, la moyenne des exactitudes permutées peut s'écarter un peu de 0,5, et la règle « 0,55 + 2 σ₀ » n'en tient pas compte. La v7 rapporte cette moyenne : que le vérificateur du code v4 la regarde, ou que les plis soient tirés par suite.
2. **« Fichier d'autorisation du lancement »** (note D6) : sa forme et son auteur sont à définir au code v4 et par la mère.
3. **Causes d'arrêt de l'étalonnage** (D8, choix 6) : aucun point de la liste d'arrêt ne les porte. L'action qui suit (un erratum contre-lu, comme au point 5) va de soi mais n'est pas écrite.
4. **Ce que la mère doit savoir de l'issue probable**, sous les options recommandées (nœud 1 (a), nœud 2 (a′)) : les exactitudes de forme passeront probablement, et l'exactitude de contenu « dépendantes contre indépendantes », qui lit la longueur brute, dépassera probablement 0,55. Le générateur sera alors « non audité pour l'étage payant », et la réserve 18 devra probablement être prise avant un étage payant.
5. Le rapport du rédacteur dit trois empreintes recalculées sur 51 : je les ai toutes recalculées sur disque, et quatre au commit.

## 11. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v7/` :

- cette pièce et son compagnon ;
- `calcul_reserve_23_v1.py` et sa sortie (empreintes au § 4.4) ;
- `rejeu/v7-rejouee.md` (`2f0f928f…`) et son journal ;
- `rejeu/diff-refait.diff` (`dc888eab58563d53f459a4325d0642a8b15cb7d21b012f8d3f1fd49a67cd554a`) ;
- les extraits au commit (`rejeu/commit-*.py`) ;
- les tables comparées ;
- les motifs d'ancre `rejeu/a01.txt` à `a14.txt`.

*Contre-lecteur, modèle O.*
