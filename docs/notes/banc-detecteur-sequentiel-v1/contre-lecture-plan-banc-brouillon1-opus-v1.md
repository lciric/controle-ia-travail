# Contre-lecture du brouillon 1 du préenregistrement du banc de validité du détecteur séquentiel sous référence honnête finie, gelée et contaminée — v1

- **Classe** : rapport de contre-lecture d'une pièce de classe A (règle R2). Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf, qui n'a écrit ni la pièce ni sa consigne. Date : 2026-11-24 (UTC). Branche `banc/detecteur-sequentiel-reference-contaminee-v1`.
- **Pièce relue** : `prereg/banc-detecteur-sequentiel-reference-contaminee-v1-brouillon1.md`, SHA-256 `c10e3fa8967f1935ce3b569e91efb894f1a0173466f978de32aba6449d35ebe3` (vérifiée).
- **Lu** : la pièce en entier, annexes comprises ; la consigne (`edc2270d…`, vérifiée) ; la note d'antériorité (`9554a9df…`, vérifiée) ; la note de sortie du collisionneur (`2cdfa231…`, vérifiée), sections 2, 5, 6, 8, et la section 3 pour juger le point 1 des « Points pour la mère » ; N-076 (`49b664c1…`), sections 1, 2, 11, et ses errata 1 (`34a59c49…`), 2 (`c2943188…`), 3 (`3335284d…`) ; T0.3 (`7474743a…`), sections Hypothèse, P8, Métrique, Seuil, Liste d'arrêt ; les six modules de code (empreintes égales à celles citées par la pièce) et `agregateurs/indexation.py` (appelé par `trajectoire_e`) ; `CLAUDE.md`. Rien ouvert sous `coffre/`, `docs/verdicts/`, `diag/`, `runs/`, `donnees/`, `registres/`.
- **Annexe A rejouée** : le programme de l'annexe A.1 est, à l'octet, le fichier de travail `dimensionnement_banc_detecteur_sequentiel_v1.py` (`5133f26a…`) ; la sortie de l'annexe A.2 est, à l'octet, `sortie_dimensionnement_v1.txt` (`601dd07a…`). Rejoué (numpy 2.5.3, Python de la session, 6,5 s) : sortie identique à l'octet (`601dd07a…`).
- **Calculs refaits** : `docs/notes/banc-detecteur-sequentiel-v1/contre-lecture-plan-banc-brouillon1-opus-calculs-v1.py` (aucun tirage au hasard ; aucune cellule de la grille simulée). Sorties reprises en section 4. Le conteneur n'a pas `scipy`, que le code du dépôt importe : je l'ai installé dans un environnement de travail hors dépôt (scipy 1.18.1).

## Verdict

**Scellable après corrections.** La mathématique tient : la preuve en trois pas de la garantie conditionnelle de l'enveloppe est juste, y compris le pas sur un gain choisi sur la référence ; la borne 0,229 et les trois pentes du duel se reproduisent par un calcul indépendant ; le contrôle de banc peut vraiment échouer et passera, s'il est juste, avec une dizaine d'erreurs types de marge (taux exact de premier passage calculé : 0,279). Deux défauts majeurs sont à corriger avant scellement : la lecture du duel sur la pente déclare « réfutée » une thèse que ce dispositif ne peut pas réfuter, et la procédure d'attestation du code contient une garde impossible à satisfaire et n'interdit pas de faire tourner la grille pendant l'écriture du code. Sept constats moyens et huit mineurs suivent ; aucun ne demande de refaire le plan.

Décompte : **2 majeurs, 7 moyens, 8 mineurs.**

## 1. Constats

### Majeurs

**C1 — Le duel sur la pente ne peut pas réfuter la thèse « σ₀·√ε », et sa table de lecture le dit pourtant.** Majeur. Lieu : É7 (l. 55), bloc H (l. 116-119), lecture du bloc H (l. 273-285), point pour la mère 3 et 4.
- *Défaut.* La thèse « plancher en σ₀·√ε » (lettre A, d'après la note de sortie, section 5) est un énoncé au pire : sur la classe des lois honnêtes de variance au plus σ₀², une contamination de fraction ε peut déplacer la moyenne d'environ σ₀·√ε sans qu'aucun détecteur ne la distingue d'une loi honnête, parce que la loi la moins favorable porte une masse d'ordre ε à une distance d'ordre σ₀/√ε. Le dispositif du bloc H ne contient pas de telle loi : ses deux lois honnêtes sont uniformes (aucune queue), le sabotage est un décalage diffus de toute la loi, le contaminant est à la borne du support. Sur ce dispositif, une règle par quantiles voit un décalage diffus dès qu'il déplace la fonction de répartition de plus que le rayon, soit un plancher de l'ordre de (largeur de la loi) × r : linéaire par construction, quelle que soit la vérité de la thèse au pire. Le calcul le confirme (régime concentré, règle « quantiles » : plancher ≈ 0,12·r, en dessous même de σ₀·√r aux petites fractions). L'auteur l'écrit lui-même (« le duel est décidé par l'algèbre », point 4 ; « elles ne tranchent pas la frontière minimax », l. 285), mais la table écrit « la thèse « σ₀·√ε » est réfutée comme pente de la frontière » (l. 277) et « thèse réfutée, même pour sa propre règle » (l. 282). Un compte rendu tiré mécaniquement de cette table porterait une réfutation que le dispositif ne permet pas. De plus, la pente est fixée par la règle d'écrêtage choisie par l'analyste (règle « rayon de variance » : 1/2 ; règles « support » et « quantiles » : 1), non par la loi : ce que le duel mesure, c'est la règle, pas la frontière d'identifiabilité. Les « deux régimes de Neon » de la note de sortie (section 3 : « variance bornée : pente 1/2 ; scores bornés lus par indicateur de queue : pente 1 ») sont d'ailleurs des régimes de statistique, ce qui rejoint cette lecture.
- *Correction proposée.* (i) Réécrire la colonne « lecture » du bloc H sans le mot « réfutée » : par exemple « sur ce dispositif (lois sans queue, décalage diffus, famille gelée de trois règles), la pente observée de la meilleure règle est linéaire ; la thèse au pire « σ₀·√ε » n'est ni confirmée ni réfutée » ; et pour D2 « la pente 1/2 est celle de la règle d'écrêtage au rayon de variance ». (ii) Requalifier le bloc H comme **vérification des calculs** du collisionneur (borne ε/(1−ε) et loi en σ₀·√ε, que personne n'avait refaits, note d'antériorité, section 2, point 6) plutôt que comme réponse au désaccord, ce que dit déjà le point 4. (iii) Si la mère veut une réponse au désaccord, ajouter un troisième régime de loi **le moins favorable** (loi honnête dont une masse d'ordre ε se trouve à distance d'ordre σ₀/√ε, ou loi bornée à queue lourde dont la variance borne est atteinte) et un sabotage **rare et lointain** (option (c) du point 3) ; à concevoir par Fable, au prix d'environ 0,4 heure de calcul par régime ajouté.

**C2 — La procédure d'attestation du code a une garde impossible à satisfaire et laisse ouverte l'exécution de la grille pendant l'écriture du code.** Majeur. Lieu : en-tête (l. 5, 17-18), ordre d'exécution (l. 203-207), liste d'arrêt, point 2 (l. 293) et point 5 (l. 296), interface, attestation (l. 334), point pour la mère 10.
- *Défaut.* (a) La garde 2 exige une attestation « qui cite le commit courant » : l'attestation est committée après le code, donc le commit courant au lancement est celui qui contient l'attestation, qu'elle ne peut pas citer. Telle quelle, la garde arrête tout lancement légitime, ce qui forcerait un écart au lancement. (b) Rien n'interdit, entre le scellement et le run décisif, de faire tourner des cellules de la grille (tailles pleines, entropie racine du texte) pour mettre le code au point, puis de relancer : c'est la fourche que R1 veut fermer. (c) La liste des « écarts du code au plan » de l'attestation peut être non vide ; `CLAUDE.md` range « écart à un préenregistrement scellé » parmi les nœuds qui attendent le mot de Lazar ; le texte ne le dit pas. (d) La garde 5 vérifie l'empreinte de la grille JSON contre celle citée par l'attestation, ce qui prouve l'identité au fichier attesté, non l'égalité aux tables du texte ; il faut nommer qui vérifie cette égalité.
- *Correction proposée.* (a) Comme T0.3 (liste d'arrêt, point 2) : l'attestation cite le **commit du code** C (complet, non abrégé) ; le lanceur vérifie que `git diff C HEAD` est vide sur `src/`, `tests/` et la grille, que l'arbre est propre, que l'empreinte du préenregistrement scellé et celle de la grille sont celles de l'attestation. (b) Ajouter à la liste d'arrêt et au protocole : « avant le run décisif, aucune cellule de la grille n'est exécutée à taille pleine ni avec l'entropie racine de ce texte ; les essais du code emploient une autre entropie, déclarée, et des tailles réduites d'au moins un facteur 10 ; ils ne sont ni gardés ni lus comme résultats ». (c) « Une liste d'écarts non vide est un écart au préenregistrement scellé : nœud, mot de Lazar avant le lancement. » (d) « L'égalité de la grille aux tables est vérifiée ligne à ligne par le contre-lecteur du code, et le code compare la grille chargée à une copie des tables écrite en dur dans les tests. »

### Moyens

**C3 — La construction naïve sur la loi Bêta mêle deux défauts : la référence gelée et une échelle qui n'est pas sous-gaussienne.** Moyen. Lieu : table des constructions (l. 37-42), É1, A-i1, Table C (É1), blocs B à D (comparaisons de `naive` et `rognee` à `enveloppe`).
- *Défaut.* `naive` divise par l'écart type empirique du gain, `connue` et `enveloppe` par 1/2 (lemme de Hoeffding). Le gain sur Bêta(1 ; 4) est asymétrique (asymétrie 1,08) : z = (g − μ)/écart type **exact** n'est pas 1-sous-gaussien (max sur λ de log E e^{λz} − λ²/2 = +0,24, atteint vers λ = 1,8 ; section 4, partie 2), alors que l'échelle 1/2 l'est (marge −1·10⁻⁴). Même avec centre et écart type exacts, le processus-e de `naive` n'est donc pas une surmartingale. A-i1 « confirmée » ne prouverait pas É1 (le défaut de la référence gelée) sur Bêta, et les écarts entre `naive` ou `rognee` et `enveloppe` mêlent centre et échelle (facteur 1,4 sur l'échelle).
- *Correction proposée.* Ajouter aux cellules A3 et A4 une construction `connue_ecart_type` (centre et écart type exacts du gain) et lire A-i1 comme « `naive` au-dessus de `connue_ecart_type` » (forme « signe ») ; ou, à défaut, déclarer dans É1 que sur Bêta la chute de `naive` est jointe aux deux causes. Dire la même chose dans B5, C3, C4 (« par la dérive du centre, à échelle de l'écart type »).

**C4 — G4 étiquetée [preuve] promet pour l'enveloppe un taux au plus α_arrêt, que la preuve ne donne pas.** Moyen. Lieu : G4 (l. 112).
- *Défaut.* É2 donne : taux conditionnel ≤ α_arrêt sur l'événement de Dvoretzky-Kiefer-Wolfowitz, donc taux **moyen** ≤ α_étalonnage + α_arrêt = α. Le taux moyen de `enveloppe` au seuil α_arrêt n'est pas prouvé ≤ α_arrêt. Une prédiction [preuve] contraire déclenche audit et réplication du bloc : une étiquette fausse peut condamner une construction juste. (En pratique la marge rend le taux presque nul, mais l'étiquette doit être exacte.)
- *Correction proposée.* G4 : « `connue` : taux ≤ α_arrêt à tous les horizons [preuve] ; `enveloppe` : taux moyen ≤ α et part des références au-dessus de α_arrêt ≤ α_étalonnage [preuve] ».

**C5 — Les critères de lecture ne sont pas tous fermés.** Moyen. Lieu : Table A (l. 225-233), Table C (l. 246-254), lecture du bloc H (l. 273), A-i3, A-i4, C5, E1.
- *Défaut.* (a) É2 : « une contraire, confirmée à la réplication » est classée « non concluant » avec le libellé « tenue, une cellule rejouée » ; le cas de **plusieurs** cellules contraires toutes confirmées à la réplication n'est pas couvert. (b) É5 nomme B6 et C5 « prédictions décisives » mais la règle ne lit que B4. (c) É6 n'a pas de verdict d'ensemble (le renvoi à la « table du bloc G » ne couvre que G3, G5, G6 ; G1, G2, G4 se lisent par la table A) : écrire « pas de verdict d'ensemble », comme pour É4. (d) Bloc H : si un seul régime est « non exécutable », aucune ligne de la table ne s'applique. (e) Formes sans ligne dans la table A : « croît avec n/m » (A-i3), « part au moins 20 % » (A-i4), « croît avec ε_r » (C5), « croissant avec φ » (E1, et l'horizon de E1 n'est pas dit). (f) É4 : la correspondance entre « tient / tombe / non concluant » et les issues de la table A n'est pas écrite (C2, D2, E2 sont des tenues à deux issues ; D3 une chute à trois issues ; F2 un signe).
- *Correction proposée.* Une ligne par forme manquante (par exemple « monotonie : chaque paire consécutive confirmée par la forme signe ; une paire contraire = contraire ; sinon non concluant » ; « part au moins q : part nette ≥ q + Z·se ; ≤ q − Z·se contraire ») ; É2 : « k ≥ 1 cellules contraires, toutes confirmées à la réplication : « tenue, k cellules rejouées » » ; bloc H : « un régime non exécutable : la thèse ne se lit que dans l'autre régime, colonne D2 seule ; aucune ligne D1 » ; É4 : « tient = confirmé (tenue) ou contraire (chute) ; tombe = l'inverse ».

**C6 — La table B ne dit pas si un échec de vivacité arrête le banc ou la seule construction.** Moyen. Lieu : A-vivacité (l. 75), table B (l. 242), cellule A5 (l. 170).
- *Défaut.* La ligne dit « banc défectueux **pour cette construction** », mais la suite est « idem » (arrêt, rien n'est lu). De plus « donne l'alerte **avant** n = m » ne peut pas être satisfait par la somme à horizon fixe, qui ne lit qu'à n = m (la table A dit « à n = m »). La loi de la cellule A5 n'est pas nommée (Bêta, sans doute ; `connue_normale` et `naive_normale` comprises ou non ?).
- *Correction proposée.* Trancher : soit arrêt du banc entier (plus simple, plus sûr), soit retrait de la seule construction de tous les blocs, déclaré au verdict. Écrire « au plus tard à n = m » et nommer la loi et la liste exacte des détecteurs de A5.

**C7 — Constantes classiques employées sans PDF (R7), dont une entre dans le rayon décisif.** Moyen. Lieu : Rayon (l. 32), Citations (l. 354), point pour la mère 11.
- *Défaut.* La constante 2 de l'inégalité de Dvoretzky-Kiefer-Wolfowitz (Massart 1990), l'inégalité de Ville et le lemme de Hoeffding sont employés « non vérifiés sur PDF ». `CLAUDE.md` interdit tout « chiffre non vérifié dans un préenregistrement ». La forme bilatérale à constante 2 vaut pour tout rayon, la borne étant triviale dès qu'elle dépasse 1 ; la forme unilatérale à constante 1 demande, de mémoire, exp(−2mγ²) ≤ 1/2, condition remplie ici (α_étalonnage = 0,025) : à vérifier sur le PDF.
- *Correction proposée.* Avant scellement : verser au dépôt le PDF de Massart (1990), empreinté, page citée, pour la constante et sa condition ; citer un manuel empreinté pour Ville et Hoeffding, ou déclarer explicitement la dérogation (énoncés classiques) et le contrôle par la mesure (B3, A-sain-1, A-sain-2). Garder la forme bilatérale dans cette version (conservatrice).

**C8 — La règle d'horizon de N-076 est réinterprétée sans le dire.** Moyen. Lieu : Rattachements (l. 344), consigne, section 2, point 7.
- *Défaut.* La consigne demande : « lectures au-delà de n = m étiquetées « au-delà de la référence » et sans verdict, sauf pour les constructions dont la garantie porte explicitement sur n > m ». La pièce restreint l'étiquette aux lectures **de puissance**, puis ajoute une exception (ii) pour le contrôle de banc. Or plusieurs lectures de **validité** au-delà de m portent un verdict pour des constructions sans garantie au-delà de m : A-i1, A-i2, A-i4 (`naive`, 16m et 64m), B5 à ε_d = 0,02 (`rognee`, 16m), C3 (`naive`, 4m), E1 (`connue`, horizon non dit), F2. Sur le fond, je partage la lecture de l'auteur (N-076, section 2 : « aucun gain de rappel au-delà de n = m n'est lu comme un effet de l'accumulation » ; la règle plafonne ce que l'on conclut d'un gain, pas la mesure d'un taux de fausses alertes), mais c'est un écart à la lettre de la consigne, à déclarer.
- *Correction proposée.* Écrire la règle exacte (« les lectures de validité se font à tout horizon pour toutes les constructions ; les lectures de puissance au-delà de n = m sont étiquetées et sans verdict ») ; supprimer les exceptions (i) et (ii), devenues inutiles ; ajouter un point pour la mère qui demande l'accord sur cette lecture.

**C9 — L'interface du code laisse des choix ouverts que le contre-lecteur du code ne pourra pas juger.** Moyen. Lieu : Métrique (l. 133-136), Plan (l. 154, 181, 197), Interface (l. 313-334), liste d'arrêt, points 4 et 7.
- *Défaut et correction, un par ligne.*
  - Écart type empirique (`naive`, bases) : diviseur m ou m − 1 non dit ; le dépôt emploie m − 1 (`bases/sequentiel.py`). Le fixer.
  - `trajectoire_e` attend un tableau à deux dimensions (N, T) (`indexation.verifier_episode`) : la garde d'équivalence doit passer `x[None, :]` (comme `bases/sequentiel.py`) ; `calibrage.rho_optimal` rend un couple (ρ*, s*). L'écrire.
  - Graines : `manifeste.generateur` ne reconstruit que la clé `(clé de la tâche,)` ; la dérivation `(clé, j)` du tirage d'indice j n'est couverte ni par le manifeste ni par la garde 4. Nommer la fonction qui la fait et étendre la garde (reconstruction et contrôle d'état pour un échantillon d'indices j).
  - Bloc E, « référence et déploiement » : la chaîne autorégressive du déploiement part-elle de l'état stationnaire, indépendamment de la référence (supposition (ii) de É2), ou continue-t-elle la chaîne de la référence ? Le dire.
  - `rognee` : nœuds a et c calculés sur la référence rognée (comme l'annexe A, bloc 4 bis) : l'écrire dans la table des constructions.
  - Somme de Page : la valeur de référence 0,1 (en unités z) n'est pas justifiée ; G6 en dépend. La justifier (par exemple la moitié du décalage standardisé détectable à n = m, ≈ 0,1 sous loi connue) ou la déclarer arbitraire.
  - La garde d'équivalence ne couvre que les constructions ; ajouter les trois bases (référence scalaire : boucle en Python pur) et le plus petit décalage détecté du duel (contre une dichotomie scalaire sur quelques répétitions).
  - `bases.py` « mêmes entrées, même sortie » : écrire les signatures.
  - Duel : à n = 10⁶, `premieres_alertes` sur une matrice pleine coûte 8 Mo par trajectoire et par pas de dichotomie ; dire que la dichotomie se fait trajectoire par trajectoire.

### Mineurs

**C10 — Valeurs attendues de l'audit de symétrie à corriger.** Mineur. Lieu : l. 287. Taux exact de premier passage de `connue_normale` (m = 400, ρ*(400 ; 0,05)) : 0,0041 ; 0,0178 ; 0,0302 ; **0,0378** à n = m/4, m, 4m, 16m (section 4, partie 3), au-dessus de l'« attendu 0,005 à 0,03 » écrit. Taux exact de l'artefact (centre et échelle estimés, m = 400, 16m) : 0,279. Le déclencheur (« sous 0,001 », « au-dessus de 0,90 ») reste juste ; corriger les plages attendues : 0,03 à 0,045 et 0,25 à 0,35.

**C11 — À n = m, la construction naïve dépasse déjà α.** Mineur. Lieu : A-i3 (l. 76). Taux exact de premier passage de `naive_normale` à n = m : 0,055 (m = 400) et 0,052 (m = 100), contre α = 0,05 ; à 4m : 0,155, déjà au-dessus de 2α. La phrase « c'est la règle d'horizon de N-076 vue du côté des fausses alertes » laisse croire que la règle protège la validité à n = m ; écrire « à n = m le dépassement est petit (de l'ordre de 10 %, calcul exact), il devient grand au-delà ». Aucune prédiction ne change ; on peut dire que 4m suffirait au contrôle (0,155), mais 16m garde la marge : ne rien changer.

**C12 — G5 : la plage « attendu entre 1,5 et 3 » ne vaut que pour la couche « loi connue ».** Mineur. Lieu : l. 113, l. 271. Calcul de population (instant n, sans bruit de référence) : rapport 2,10 en loi connue, **1,29** sous enveloppe à ε_d = 0,02 (la marge commune r = 0,095 dilue le prix). Le critère (rapport > 1) est inchangé ; écrire les deux valeurs attendues.

**C13 — Duel : détails de calcul.** Mineur. Lieu : H-D1, H-D2 (l. 117-118), Métrique (l. 139). (a) La pente est prise contre r = ε + 0,0015, non contre ε, alors que les thèses portent sur ε ; contre ε, les pentes de population valent 0,98 ; 0,98 ; 0,58 (au lieu de 1,03 ; 1,04 ; 0,62). (b) Le terme séquentiel à n = 10⁶ (0,0015 sur le gain) n'est pas dans les pentes « de population » ; avec lui, contre r : 1,00 ; 1,01 ; 0,57. Aucune conclusion ne change par rapport au seuil 0,75. Rapporter aussi la pente contre ε. (c) « Un plancher deux à quatre fois plus bas » : les rapports calculés vont de 1,9 à 4,3. (d) Régime étalé : « la règle support l'emporte » à égalité exacte avec « rayon de variance », qui s'écrête au support dans tout ce régime ; le dire.

**C14 — Deux chiffres des points pour la mère.** Mineur. Point 5 : à α = 0,01 partagé par moitiés, le rayon à m = 400 vaut 0,0865, non 0,084. Point 7 : une marge de 0,074 sur le gain correspond à un décalage latent d ≈ 0,23, soit une distance de Kolmogorov ≈ 0,09 (non 0,12) ; la plage est « 0,09 à 0,2 ».

**C15 — Énoncé de É2 et biais de la marge.** Mineur. Lieu : É2 (l. 48-49), B4 (l. 82). (a) La supposition (i) (« les autres sont indépendants et de loi F ») est une contamination aveugle à la valeur. Une forme plus forte est disponible au même prix : appliquer l'inégalité aux m tirages honnêtes d'avant remplacement puis ajouter k/m, ce qui couvre un remplacement choisi d'après les valeurs (rayon d'échantillonnage en m au lieu de ⌊(1 − ε_d)m⌋). À mentionner ; le générateur, qui remplace des indices tirés au hasard, reste couvert par la forme actuelle. (b) B4 : les nœuds étant choisis sur la référence, la marge moyenne a un biais d'ordre 1/(2m) (environ +0,005 à m = 100, heuristique), la moitié de la tolérance de 0,01 ; à écrire.

**C16 — Base « somme cumulée corrigée de Bonferroni sur quatre horizons » absente.** Mineur. Lieu : bases (l. 133-136). C'est la base de Neon (note de sortie, section 3, sous-test 1b), valide sous arrêt optionnel à plusieurs horizons, y compris au-delà de m. L'ajouter en descriptif, ou dire pourquoi la somme de Page étalonnée à m la remplace.

**C17 — Menues retouches.** Mineur.
- B3 (l. 81) : « attendu près de la moitié » → « attendu près de α_étalonnage/2 ».
- É3 (l. 51) : « seuil rendu « robuste » » sans nombre ni placement ; ajouter « (fraction rognée ε_d, contamination à nombre fixe, placements haut, seuil, bas) » pour rester dans la règle des phrases interdites.
- F2 : la puissance attendue n'est pas déclarée ; ma grossière estimation (part des références à marge négative ≈ 0,02 à 20 tâches de 20, ω = 0,3 ; erreur type ≈ 0,006 à 500 références) donne une issue probable « non concluant » ; le dire d'avance.
- Temps de calcul : mon décompte (tailles × horizons × constructions) donne plutôt 4,5 à 5,5 heures de cœur que 3,5, soit 1,2 à 1,5 heure d'horloge sur quatre cœurs si la bande passante mémoire suit ; le plafond de 6 heures tient. Recommandation : un chronométrage du code écrit, à tailles réduites et autre entropie (voir C2), avant le lancement.

## 2. Exigences de la consigne (section 2, points 1 à 13)

| point | servi ? | où | réserve |
|---|---|---|---|
| 1 contrôle de banc, naïve doit échouer à écart fixé ; bien spécifiée doit tenir | oui | A-artefact (0,10 = α au-dessus de α), A-sain-1, A-sain-2, table B | C6 (vivacité) |
| 2 grille : contamination basse, haute, ciblée ; double ; dérive graduée ; autocorrélation ; grappes ; niveaux, justification, ce que chaque cellule fait tomber | oui | blocs C à F, table de la grille, « Justification des niveaux » | — |
| 3 unité épisode, h = 1, tâche comme unité sous grappes ; budget partagé ; garantie conditionnelle ou moyenne, rapporter les deux et la queue | oui | Vocabulaire, É2, F1, Métrique (parts conditionnelles) | C4 |
| 4 bases au même rayon, même score, même référence, horizon fixe et arrêt optionnel ; règle écrite d'avance | oui | Métrique (bases), « Règle qui tranche » | C16 |
| 5 duel : une statistique, un seuil, deux hypothèses complémentaires, puissance, non exécutable ; régimes ; ce qui réfuterait | en forme oui, sur le fond non | bloc H | **C1** |
| 6 critères gelés, liste d'arrêt, graines, manifeste, sorties sous `diag/`, lecture par sous-agent neuf | oui | sections correspondantes | C5, C9 |
| 7 rattachement à N-076 | oui | Rattachements | **C8** |
| 8 délai de l'oracle | oui | l. 346 | — |
| 9 prévision de la loi | oui | l. 61, 348 | — |
| 10 règle de diffusion, générateur réemployable | oui | l. 160, 350 | — |
| 11 phrases à ne pas écrire | oui | l. 352 | C17 (« robuste ») |
| 12 budget, erreur de Monte-Carlo déclarée, règle de dépassement | oui | « Tailles et erreur », liste d'arrêt 10 | C17 (temps) |
| 13 points pour la mère, aucun « À REMPLIR » | oui | section dédiée ; le validateur ne relève que la contre-lecture manquante, comme voulu | — |

## 3. Les points de la justesse mathématique, un par un

- **Preuve de É2, pas (a).** Juste. Avec F̂_h la répartition empirique des m − k honnêtes et F̂ celle de la référence entière, F̂ − F̂_h = (k/m)(F̂_c − F̂_h) ≤ k/m ; sur l'événement de l'inégalité, F̂_h ≤ F + γ ; donc F ≥ F̂ − (k/m + γ) ≥ F̂ − r dès que k ≤ ⌊ε_d·m⌋ et que le rayon d'échantillonnage est calculé sur au plus m − k honnêtes (⌊(1 − ε_d)m⌋ ≤ m − k). Voir C15 pour une forme plus forte.
- **Pas (b), le plus fragile selon l'auteur.** Juste. Pour g croissante à valeurs dans [0 ; 1], E_F g = ∫₀¹ P_F(g(X) > s) ds et {g(X) > s} = {X > t_s} ; sur l'événement, P_F(X > t) ≤ P_F̂(X > t) + r pour **tout** t (inégalités strictes et larges traitées par limites à gauche). L'événement est uniforme en t : la borne vaut simultanément pour tous les gains croissants, donc pour un gain choisi sur la référence, sans union. La formule de la borne (Métrique, l. 129) est bien ∫₀¹ min(1 ; P̂(g > s) + r) ds = moyenne après déplacement de la masse r la plus basse vers 1 ; je l'ai vérifiée terme à terme, y compris la cellule partielle (r·m − k)·g₍ₖ₊₁₎.
- **Pas (c).** Juste, à une condition que le texte respecte : le mélange doit être **unilatéral** (λ ≥ 0, loi demi-normale), car le passage E e^{λx} ≤ e^{λ E x} e^{λ²/8} ≤ e^{λ²/8} use de E x ≤ 0 et λ ≥ 0. Le mélange d'exponentielles surmartingales à loi de mélange fixe (ρ ne dépend que de m) est une surmartingale ; Ville donne α_arrêt conditionnellement à la référence ; le taux moyen est ≤ α_étalonnage + α_arrêt. Vérifié numériquement : log E e^{λ(g − μ)} − λ²/8 ≤ −1·10⁻⁴ sur la grille de λ (Bêta, gain par quantiles).
- **Extension à la dérive.** Juste, dans le sens écrit : il faut F ≥ G − ε_d (la loi de la référence G domine la loi honnête du déploiement d'au plus ε_d), ce qui couvre une dérive positive du déploiement ; contamination et dérive s'additionnent dans r.
- **Inégalité de Dvoretzky-Kiefer-Wolfowitz.** Forme bilatérale à constante 2 : valable pour tout rayon (triviale au-delà de 1). Forme unilatérale à constante 1 : sous exp(−2mγ²) ≤ 1/2, remplie ici ; gain de 8,2 % sur le rayon d'échantillonnage. Les deux de mémoire, à vérifier sur PDF (C7).
- **Borne 0,229 à n = 16m.** Reproduite indépendamment avec `calibrage.frontiere` et `calibrage.rho_optimal` du dépôt : 0,2288 (m = 100 et 400). C'est une vraie borne inférieure (l'alerte à l'instant n est incluse dans l'alerte avant n). Taux exact de premier passage, par propagation de densité (contrôle du propagateur : 0,04256 contre 0,04245 par la correction de Siegmund) : 0,278 (centre seul estimé) et 0,279 (centre et échelle estimés), m = 400, 16m ; écart type des taux conditionnels 0,378, d'où une erreur type de 0,012 à 1 000 références, conforme aux 0,013 annoncés. Le contrôle passe avec (0,279 − 0,148)/0,012 ≈ 11 erreurs types si le code est juste. Part des références au-dessus de 2α : ≈ 0,33 à 0,35 (A-i4 « au moins 20 % » tient ; quadrature grossière sur ce point).
- **Pentes du duel (1,03 ; 1,04 ; 0,62).** Reproduites par une mise en œuvre indépendante (formes fermées sur les uniformes) : 1,034 ; 1,039 ; 0,618. Voir C13 pour la pente contre ε et le terme séquentiel.
- **Processus-e de mélange normal à échelle de Hoeffding.** Valide (pas (c)). Le processus à l'échelle de l'écart type ne l'est pas sur Bêta (C3).
- **Multiplicité.** 150 comparaisons à Z = 4 (unilatéral) : probabilité d'au moins une contrariété due au bruit 0,0047, conforme au « 0,5 % ». Les prédictions de tenue sont loin de leur seuil ; les chutes que j'ai estimées (B5 ≈ 0,8 ; C3 ≈ 0,74 ; C4 ≥ 0,6 ; D3 ≈ 0,84, approximation normale avec bruit de référence) sont loin au-dessus de 2α + 4 erreurs types : la puissance de Monte-Carlo suffit. G1 : correction d'Edgeworth du taux de la somme à horizon fixe 0,0265 (asymétrie 1,08), dans la tolérance 0,005 + 4 erreurs types.
- **Effectif du duel.** Le calcul (erreur type de pente 0,03 ⇒ erreur relative de chaque plancher 0,043 ⇒ 19 répétitions à dispersion 0,15) est juste (√Σ(ln r − moyenne)² = 1,461).
- **Entropie racine.** Seize premiers octets, gros-boutiste, du SHA-256 de la chaîne déclarée : 17478886177536127460746961611737655340, conforme.

## 4. Testabilité, R1, R3, R4, R5, R6, R9

- **Signe, chiffre, réfutation.** Chaque prédiction a une forme et un seuil, sauf les formes de C5 (e). Aucun critère ne m'a paru réglé pour obtenir un signe, à l'exception du duel (C1), dont l'issue est fixée par la conception ; ce n'est pas un run « visant un signe positif » (R3) au sens strict, mais sa lecture en tirerait une réfutation.
- **Le contrôle de banc peut échouer.** Oui : un banc qui recalculerait le centre sur le déploiement, ou qui lirait les taux à n ≤ m, verrait `naive` tenir ; le seuil (0,10 + 4 erreurs types) est à une dizaine d'erreurs types sous la valeur exacte. Sa contrepartie A-vivacité ferme le cas du détecteur muet.
- **Audit de symétrie (R4).** Présent, symétrique (trop beau et contraire), avec déclencheurs chiffrés ; plages attendues à corriger (C10).
- **Gardes (R5).** Chaque garde est promise testée sur cas sain et artefact ; aucun repli silencieux ; arrêt sans réduction des tailles. Manques : C2 (garde 2 impossible, garde 5), C9 (graines d'indice j, équivalence des bases).
- **R6, R9, R12.** Manifeste, résultats scellés par bloc, entropie fixée, dérivation par tâche indépendante de l'ordre : conformes, sous réserve de C9.
- **Rattachement à N-076, phrases interdites, diffusion.** Conformes ; C8 et C17.
- **Citations (R7).** Aucun chiffre publié n'est cité ; les voisins à citer sont ceux de N-076 ; la prédiction conforme robuste à une fraction contaminée est déclarée non cherchée, « à faire avant toute phrase sur l'enveloppe » : bien. C7 pour les constantes.

## 5. Avis sur les douze points pour la mère

1. **« Somme cumulée écrêtée au même rayon ».** D'accord, confiance plus haute que 0,7 : la section 3 de la note de sortie donne, pour Carbon au témoin, « moyenne écrêtée des deux côtés majorée du biais pire cas, contre une somme cumulée écrêtée sur la **même** référence » : c'est la lecture retenue (gain borné entre deux nœuds, même borne). Neon ajoute une « somme cumulée corrigée de Bonferroni sur quatre horizons » : à ajouter en descriptif (C16).
2. **« Contamination basse ».** D'accord pour garder les deux sens. La section 5 de la note de sortie garde un désaccord non tranché sur la **puissance** sous contamination basse (A : elle la fait perdre ; B : elle la fait gagner avec l'enveloppe corrigée). Le banc a le placement bas : ajouter une lecture descriptive de puissance sous placement bas, à n ≤ m, sans verdict, coûte peu et répond à ce désaccord.
3. **Duel.** Je ne recommande (a) qu'avec la réécriture de la table (C1, corrections (i) et (ii)). Si la mère veut une réponse au désaccord et non une vérification de calcul, (c) ne suffit pas seul : il faut aussi une loi honnête la moins favorable (C1, correction (iii)).
4. **Le duel est décidé par l'algèbre.** D'accord, et c'est la raison de C1 : le dire à Lazar, et le dire dans la table de lecture.
5. **Niveau 0,05.** D'accord pour ce banc (le rayon à 1 % vaut 0,0865 à m = 400, non 0,084 ; C14). Une cellule descriptive à α = 0,01 (B, m = 400, ε_d = 0,02, enveloppe seule) rattacherait le banc au niveau de N-076 à faible coût.
6. **Mélange normal à échelle de Hoeffding.** D'accord. Le prix G5 en dépend fortement (facteur 1,4 sur l'échelle, et 1,29 seulement sous enveloppe, C12) ; une variante à variance empirique serait la suite naturelle.
7. **Résultat de principe qui pèse.** D'accord, c'est le message le plus utile du banc pour le programme, à dire avant de lire ; corriger la plage (0,09 à 0,2 en distance de Kolmogorov, C14).
8. **Contrôle décisif sur la loi normale seulement.** D'accord. Ajouter sur Bêta la construction `connue_ecart_type` pour que la lecture informative de `naive` y soit propre (C3).
9. **Contamination à nombre fixe.** D'accord ; l'écrire aussi dans l'énoncé de É2 (supposition (i)), et noter la forme plus forte de C15.
10. **Attestation du code.** D'accord pour l'attestation plutôt qu'une version 2 du texte (elle évite un second tour de contre-lecture de classe A), **à condition** des corrections de C2 : commit du code et différence vide jusqu'à HEAD, interdiction d'exécuter la grille avant le run, liste d'écarts non vide = nœud avec mot de Lazar ; et contrôle des champs de l'attestation par le contre-lecteur du code.
11. **PDF manquants.** D'accord, et à faire **avant** scellement (C7). Garder la forme bilatérale dans cette version.
12. **Lois synthétiques.** D'accord. Le versant honnête parle de 32 tâches : si la mère confirme cet ordre de grandeur, une cellule F à 32 tâches serait plus parlante que 20.

## 6. Calculs refaits

Programme : `docs/notes/banc-detecteur-sequentiel-v1/contre-lecture-plan-banc-brouillon1-opus-calculs-v1.py` (parties 1 et 2 : quelques secondes ; partie 3 : environ 4 minutes ; option `--sans-passage`). Aucun tirage au hasard. Sorties (extraits verbatim) :

```text
# Partie 1 — rayons (bilatéral | unilatéral) et bornes de la naïve à l'instant n, par calibrage.py
100 [0.148, 0.1695, 0.256] unilat [0.1358, 0.1572, 0.2432]
400 [0.074, 0.0948, 0.178] unilat [0.0679, 0.0886, 0.1716]
1600 [0.037, 0.0574, 0.139] unilat [0.034, 0.0543, 0.1358]
reduction unilaterale du rayon d'echantillonnage 0.08249228392333519
400 16 0.12935 244.98 0.2288
100 64 0.2587 261.61 0.3425
# Partie 2
Bêta(1;4) : a = 0.1591 c = 0.4377 moyenne du gain 0.2615 écart type 0.3570 asymétrie 1.076
  z = (g − μ)/écart type exact : max_λ∈]0,3] [log E e^(λz) − λ²/2] = 0.2429 à λ = 1.78 (positif = pas 1-sous-gaussien)
  Hoeffding : max [log E e^(λ(g−μ)) − λ²/8] = -9.75e-05 (doit être ≤ 0)
  G1 : taux de la somme à horizon fixe, correction d'Edgeworth : 0.0265 (contre 0,025)
150 comparaisons, Z = 4 unilatéral : 0.0047
G5, marge 0.0 : décalage latent détectable somme 0.111, processus-e (instant n) 0.234, rapport 2.10
G5, marge 0.0948 : décalage latent détectable somme 0.387, processus-e (instant n) 0.499, rapport 1.29
duel étalé     support   population  : planchers [0.01656 0.03176 0.06257 0.12585] ; pente contre r 1.034 ; contre ε 0.976
duel étalé     support   fini n=10^6 : planchers [0.0181  0.03333 0.06419 0.12759] ; pente contre r 0.996 ; contre ε 0.940
duel étalé     quantiles population  : planchers [0.01856 0.03578 0.07068 0.14241] ; pente contre r 1.039 ; contre ε 0.980
duel concentré variance  population  : planchers [0.0056  0.00817 0.01219 0.01885] ; pente contre r 0.618 ; contre ε 0.583
duel concentré variance  fini n=10^6 : planchers [0.00627 0.00872 0.01259 0.01915] ; pente contre r 0.569 ; contre ε 0.536
duel concentré quantiles population  : planchers [0.00129 0.00248 0.0049  0.00987] ; pente contre r 1.039 ; contre ε 0.980
duel concentré quantiles fini n=10^6 : planchers [0.00139 0.00258 0.005   0.00997] ; pente contre r 1.005 ; contre ε 0.948
# Partie 3 — premier passage exact (loi normale du contrôle ; α = 0,05 ; ρ*(m ; 0,05))
contrôle du propagateur : frontière constante 40.0, n = 400 : 0.04256 ; Siegmund 0.04245
m = 400 bien spécifiée (connue_normale) : n = 100 : 0.00410 ; n = 400 : 0.01784 ; n = 1600 : 0.03018 ; n = 6400 : 0.03775
m = 400 naïve (centre seul estimé) : n = 400 : taux 0.0548 ; n = 1600 : taux 0.1545 ; n = 6400 : taux 0.2783 (é.t. des taux conditionnels 0.377 ; part > 2α 0.325)
m = 400 naïve (centre et échelle estimés) : n = 400 : taux 0.0556 ; n = 1600 : taux 0.1553 ; n = 6400 : taux 0.2789 (é.t. des taux conditionnels 0.378 ; part > 2α 0.354)
m = 100 bien spécifiée (connue_normale) : n = 25 : 0.00338 ; n = 100 : 0.01590 ; n = 400 : 0.02775 ; n = 1600 : 0.03519 ; n = 6400 : 0.03943
m = 100 naïve (centre seul estimé) : n = 100 : taux 0.0515 ; n = 400 : taux 0.1513 ; n = 1600 : taux 0.2764 ; n = 6400 : taux 0.3646
m = 100 naïve (centre et échelle estimés) : n = 100 : taux 0.0545 ; n = 400 : taux 0.1544 ; n = 1600 : taux 0.2785 ; n = 6400 : taux 0.3670 (é.t. des taux conditionnels 0.444 ; part > 2α 0.500)
```

Réserves sur ces calculs : la partie 3 discrétise la densité au pas 0,25 (écart type 1 par pas) et intègre sur le centre estimé par 48 nœuds de Gauss-Hermite (3 pour l'échelle, approximation normale de σ̂/σ) ; les « parts » sont grossières (poids des nœuds). Durée de la partie 3 : 4 minutes. Ce sont des calculs de principe, sous supposition, non contre-lus.

## Ce que je n'ai pas fait

- Aucun PDF ouvert (Massart, Ville, Hoeffding : de mémoire, C7).
- Aucune simulation de cellule de la grille ; aucune lecture de résultat.
- Le biais de la marge de B4 (C15 b) et les taux de F2 (C17) sont des ordres de grandeur à la main.
- Je n'ai ni modifié la pièce, ni commité, ni poussé.
