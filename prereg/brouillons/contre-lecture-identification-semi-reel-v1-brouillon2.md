# Contre-lecture du brouillon 2 — épreuve semi-réelle des méthodes d'identification causale — v1

- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`), canal `canal/conv-audit-n04`. N'a écrit ni le brouillon 1, ni le brouillon 2, ni les fiches de lecture, ni le script de règles. Réserve d'indépendance : modèle différent d'Opus, mais même dépôt et même chaîne de travail que les auteurs.
- Date (UTC) : 2026-10-31, vers 00:20 (horloge de l'outil : 01:20 à UTC+1).
- Règle appliquée : R2 (contre-lecture), R7 (page citée) ; verdict global à la fin.
- Interdits respectés : rien lu sous `donnees/` ; aucun réseau ; aucun `.sha256` écrit ; aucun commit ; aucune clé. **Écart à signaler** : en plus du script de règles (`python3 -I`), j'ai utilisé le shell en lecture seule (`sha256sum`, `diff`, `cat`, `sed`, `grep`, `ls`) pour vérifier les empreintes et lire les fichiers ; aucun autre programme exécuté.
- Fichiers lus et empreintes (SHA-256, recalculées) :
  - brouillon 2 `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon2.md` `f61ae4c01d51b05007b58103e22b5b9c5219c9da98b72d2c7eef135f7388c5b2` (conforme à son compagnon) ; lu en entier (562 lignes) ;
  - brouillon 1 `…-brouillon1.md` `d8ae28dc66888793886bc202ad47f7081c2033244b4bdfbce14cbbd664121516` (conforme) ; lu pour les sections Seuil, Critères, Métrique et Prédiction, survolé ailleurs ;
  - script `calcul-regles-identification-semi-reel-v1-brouillon2.py` `eb9d429d3e02c0e843941efed87efa233b05b62f43f141aaee784038a59ba05d` ; sortie `…brouillon2.sortie.txt` `35aa0d02445387bdbf7ed24d6d20468574a17104dc281bd43b63381b7f053a51` ; **rejeu par `python3 -I` : empreinte `35aa0d02…` identique, `diff` vide** ;
  - fiches `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79` ; lues en entier ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (lu, non exécuté) ;
  - `registres/decisions.md` `e21ddcf4bdbb3aa72339db500fe2397b14f7c8c209454e4b03dfe7c14f813509` (lignes R-631, R-633, R-641, R-650, R-653) ; le fichier est vivant, son empreinte diffère de celle citée par le brouillon, ce qui est normal ;
  - sept PDF ouverts à la page citée (empreintes conformes à leurs compagnons) : Khemakhem (p. 5, 6, 7, 9, 15), Reisach (p. 7, 9), Borjas (p. 29, 76), Campos (p. 11, 12, 17), Iaria (p. 22, 23, 40), Azoulay (p. 17, 28), Locatello (p. 4, 6).
- Non lus : tout `donnees/` ; la moisson ; les pièces du collisionneur (question 6, réponses, relectures) ; Lippe, Schölkopf et le reste de chaque PDF (contrôlés sur fiche seulement) ; le programme v2 ; les annexes en ligne.
- Portée : cette contre-lecture porte sur le **brouillon 2**, alors que le brouillon 2 demande une contre-lecture sur le **brouillon 3** (après le verdict du collisionneur). Elle ne remplace donc pas la contre-lecture finale de R2 ; elle sert à corriger avant ce brouillon 3.

Échelle de gravité : **majeur** = à corriger avant le gel ; **moyen** = à corriger, ou à écrire comme choix assumé ; **mineur** = à corriger quand on repasse sur le texte.

---

## A. Fidélité aux sources (R7) — verdict : **à corriger** (deux chiffres mal attribués, une page)

Contrôles à la source, page ouverte :

| Énoncé du brouillon | Source (page du fichier) | Résultat |
|---|---|---|
| Khemakhem, théorème 1 : (i) zéros de la fonction caractéristique du bruit de mesure nulle ; (ii) mélange injectif ; (iii) statistiques suffisantes dérivables, linéairement indépendantes ; (iv) **nk + 1 points distincts**, matrice L de taille nk × nk inversible ; conclusion « identifiable à une transformation linéaire inversible près » | p. 5 : conforme mot pour mot | **tenu** |
| Khemakhem, corrigendum : plus de revendication pour des observations **discrètes** | p. 9 : conforme | **tenu**, mais mal appliqué par le brouillon (CS2-05) |
| Khemakhem, hypothèse (iv) presque sûre si les paramètres sont tirés « au hasard et indépendamment » ; exemple n = 2, k = 1 | p. 15 (annexe B.2.3) : conforme | **tenu** |
| Khemakhem, proposition 1 (k = 1, seule la moyenne varie : pas de réduction à une permutation) ; théorèmes 2 et 3 ; théorème 4 (cohérence, limite de données infinies) | p. 6 : conforme | **tenu** |
| Khemakhem, simulation : segments M = 40, L = 1 000, d = 5, n = 5, coefficient de corrélation moyen par affectation linéaire, iVAE au-dessus de 95 %, balayage de 10 à 50 segments | p. 7 : conforme ; **d y est la dimension des observations, n celle des latentes** | **tenu** ; notation à corriger (CS2-04) |
| Reisach, « sortnregress » : tri par variance croissante, lasso à **critère d'information bayésien** | p. 7 : « using the Bayesian Information Criterion for model selection » | **tenu** |
| Reisach, sur données standardisées v = 1/2 ; la standardisation **ne suffit pas** : une chaîne simulée garde un motif de coefficients de régression standardisés croissants le long de l'ordre causal | p. 7 (v = 1/2) ; p. 9, § 5.1 | **tenu** ; la mesure construite sur ce motif ne le mesure pas (CS2-10) |
| Borjas et Doran : −0,133 (0,036) article par an, −19,577 (1,576) citations ; similarité −1,523 et −69,155 ; 804 180 observations ; cellule « −2378 » imprimée ainsi | tableau III p. 76 (numéro imprimé 75) : conforme ; signe négatif confirmé | **tenu** |
| Borjas : 0,13 × 17 = 2,2 articles sur 6,8, « environ un tiers » ; tendance préalable légèrement croissante du groupe exposé | p. 29 (imprimé 28) : conforme | **tenu** |
| Campos : −0,0241 (0,0088), moyenne 0,1563 ; même thème −0,0247 (0,0069) ; autre institution −0,0219 (0,0083) ; même institution −0,0085 (0,0064) | tableau 4, p. 12 : conforme | **tenu** |
| Campos : « environ −16 % » | **p. 11** (texte : « 2.4 percentage points, around 16 % »), non p. 12 ; le calcul −0,0241 / 0,1563 donne 15,4 % | **à corriger** (CS2-03) |
| Campos : taux de base 3 828 / 86 068 533 = 0,004 % ; 0,016 % dans le même thème | note 21, p. 17 : conforme (le script donne 0,004448 %) | **tenu** |
| Iaria : « −0,222 », « −85 % » | texte p. 22 (imprimé 948) : « fell by 0.22 … a reduction of 85 % » ; **tableau IV p. 23 : colonne (1) = −0,217 (0,033)** ; −0,222 est la colonne (3), ligne « × WWI » | **−85 % tenu ; −0,222 faux pour la colonne citée** (CS2-01) |
| Iaria : −1,727 (0,638) au seuil du 1 % supérieur ; −0,1 écart-type, environ −33 % | tableau VIII, p. 40 : conforme | **tenu** |
| Azoulay : −0,092 (0,022) sans témoins, −0,086 (0,025) avec ; « 8,79 % » ; trois à quatre ans après le décès, pas de résorption | tableau III p. 28 : −0,086 est la colonne 1b ; **la note du tableau calcule 1 − exp(−0,092) = 8,79 % pour la colonne 1a** ; p. 17 : 8,2 % ; délai conforme | **chiffres conformes, appariement faux** (CS2-02) |
| Locatello : 50 graines par configuration ; l'objectif seul explique 37 % de la variance, objectif × régularisation 59 %, le reste est dû à la graine | p. 4 et p. 6 : conforme | **tenu** |

Tout chiffre du brouillon que j'ai pu rattacher à un des neuf PDF l'est, sauf les trois écarts ci-dessus. Les chiffres non sourcés sont étiquetés SUPPOSÉ (Reisach 2023, PCMCI, prédiction invariante, Shimizu), ou présentés comme choix de l'auteur (0,80 de S17, 22 valeurs de S19) : pas de faute R7 cachée. Schölkopf, Lippe et les autres énoncés des fiches : contrôlés sur fiche seulement.

### Constats

- **CS2-01 (majeur)** — Hypothèse (branche H-C⁺) et table « Suites » (ligne Iaria) : « −0,222 … tableau IV » est mal attribué. La colonne (1), celle que le texte commente, est −0,217 (0,033) ; le texte arrondit à 0,22 ; −0,222 est le coefficient « × WWI » de la colonne (3). Origine : fiche § 9, énoncé 2, reprise telle quelle. Correction : écrire « −0,217 (0,033), colonne (1), soit 0,22 dans le texte, environ −85 % » (ou citer −0,222 avec la colonne (3)) ; corriger aussi la fiche.
- **CS2-02 (majeur)** — table « Suites » (ligne Azoulay) : « −0,086 (0,025) avec témoins, soit 8,79 % de baisse ». Le 8,79 % est l'élasticité de la colonne 1a (−0,092, sans témoins) d'après la note du tableau ; pour −0,086 le texte du papier donne 8,2 % (p. 17, attribué à tort à la « colonne 2b », incohérence interne déjà notée par la fiche). Origine : fiche § 6, énoncé 6, ambiguë. Correction : « −0,092 → 8,79 % ; −0,086 → 8,2 % ».
- **CS2-03 (mineur)** — « environ −16 % » (Campos) : page 11 (imprimé 1005), pas 12 ; noter que le calcul brut donne 15,4 % et que le chiffre 16 % est celui du papier.
- **CS2-19 (mineur, hors brouillon)** — fiche § 6 : l'empreinte abrégée d'Azoulay se termine par « …489a89 » (celle d'Iaria) ; l'empreinte réelle (table d'en-tête et compagnon) se termine par « …693354 ». À corriger dans la fiche.

---

## B. Variante B-θ (S19) — verdict : **tenu pour le théorème 1 ; à corriger pour la lecture « permutation », pour la marge de 22 et pour le statut de la lecture n° 6**

**Contrôle hypothèse par hypothèse** (théorème 1, p. 5, et modèle p. 3–4) :
- (i) bruit gaussien d'écart-type 0,1 : zéros de la fonction caractéristique de mesure nulle ✓ ;
- (ii) mélange injectif : deux couches carrées 5 × 5 à poids orthogonaux et pente négative 0,2 ✓ (injectif) ;
- (iii) statistiques (z, z²) pour une loi normale : dérivables, linéairement indépendantes ✓ ;
- (iv) nk + 1 = 11 valeurs de u avec matrice L inversible : presque sûre pour des (μ_i(u), σ_i(u)) tirés indépendamment à chaque u (p. 15) ✓, à condition d'avoir au moins 11 valeurs, et 22 sont exigées ;
- sources conditionnellement indépendantes sachant u : ✓ par construction (cinq sources toutes plantées), à condition que chaque z soit tiré **par paire-année** (non écrit, voir CS2-11) ;
- famille exponentielle, k fixé = 2 (moyenne et variance modulées, ce qui évite la proposition 1) ✓ ;
- observations continues (corrigendum) ✓ ; Bθc : λ constants, L nulle, condition (iv) en défaut, a priori effectivement inconditionnel : contre-exemple correct (p. 3, § 2.3).

Le brouillon a donc raison de dire que B-θ est « dans » le théorème 1. Mais :

- **CS2-06 (majeur)** — Le théorème 1 ne garantit que l'identifiabilité **à une transformation linéaire inversible près** (relation ∼A sur le vecteur des nk = 10 statistiques suffisantes). La réduction à une **permutation** (théorème 2, p. 6, k ≥ 2) exige des statistiques deux fois dérivables **et** un mélange f « ayant toutes ses dérivées secondes croisées ». L'activation à pente négative 0,2 est linéaire par morceaux, non dérivable aux plis : la condition (2.ii) n'est pas vérifiée telle qu'écrite, ou est au mieux triviale. Or PB-M4θ (r̃ ≥ 0,70, 0,75 à 0,95), le MCC ≥ 0,70 (« identification complète ») et la ligne 9 de la Table Bθ supposent une identification **à permutation près** d'une dimension unique. Correction : soit une activation lisse injective (deux fois dérivable), soit écrire que seule ∼A est garantie et que r̃ et MCC sont des paris hors du résultat garanti. Je n'ai pas pu vérifier à la source que l'iVAE du papier emploie une activation lisse (supplément H.1 absent du PDF) : à confirmer.
- **CS2-07 (moyen)** — La « marge de 22 = 2 × (nk + 1) » est un choix de l'auteur, pas une lecture du papier : le papier balaie M de 10 à 50 segments (p. 7), donc **sous** 11 à M = 10, et prend 40 par défaut. À écrire comme choix. De plus, le plancher de S13 (3 environnements, 12 ans) donne **21 < 22** : les seuils S13 et S19 se contredisent à une unité près ; la base minimale rend B-θ non exécutable par construction (le brouillon le dit, mais n'en tire pas la conséquence sur S13).
- **CS2-04 (moyen)** — Notation : dans Khemakhem, **d = dimension des observations, n = dimension des latentes** (p. 5 « Z ⊂ ℝⁿ, X ⊂ ℝᵈ » ; p. 7 « d = 5 (and n = 5) »). Le brouillon emploie « d » pour la dimension **apprise** (S6 : d = 6 ; B-θ : « d = n = 5 » ; encodeur « 2d »). La « lecture à confirmer » sur d est donc tranchée par la source : d désigne les observations ; la phrase de comparaison (« comme la simulation du papier ») reste vraie en B-θ (K = 5 = d, n = 5) mais la notation du brouillon doit être changée. Reste ouverte : la nature de la corrélation (rangs ou Pearson) du papier, que la page 7 ne précise pas.
- **CS2-05 (moyen)** — W5 (b) : « S et D sont des comptes … et le corrigendum retire toute revendication pour des observations discrètes » mélange deux choses. Le corrigendum (p. 9) vise des **observations** x discrètes ; S et D sont des **sources** discrètes, ce qui viole « densité de famille exponentielle », pas le corrigendum. En B-hors les observations sont des sorties continues d'un réseau. Reformuler.

**Question 6 (compter les valeurs de u) : est-ce une lecture au sens de R1 ?**
- R1 interdit de lire un **résultat** avant le scellement : compter des environnements et des années n'en est pas un. Mais le brouillon s'impose lui-même une règle plus stricte (scellement avant « toute lecture des métadonnées moissonnées »), et le manifeste scellé ne donne que la règle de sélection et les environnements, pas la couverture en années (qui dépend des données). Sous sa propre règle, la liste des années **est** une lecture de métadonnées.
- **CS2-08 (majeur)** — Plutôt que de trancher « lecture ou non », écrire **avant le scellement** une échelle ordonnée de définitions de u (par exemple environnement × année après la référence ; puis autres découpages nommés), avec la règle déterministe « première définition qui atteint le seuil de S19, appliquée par le booléen de S13 », et « aucune ne l'atteint → B-θ non exécutée ». Cela supprime la question (aucune lecture avant scellement, aucun choix discrétionnaire après) et lève la rigidité actuelle (« jamais de repli… ») qui, avec CS2-07, expose toute la décision de B-θ. Faire de cela la décision D-8 pour Lazar (elle figure aujourd'hui comme « nœud ouvert 2 », hors liste des décisions).

---

## C. Condition R2⁻ (S20) — verdict : **à corriger (moyen)**

- **Réfutable ?** Oui, faiblement. La prédiction « recouvrement R2⁻ comme R2 à 0,10 près » peut échouer ; la ligne 7bis peut faire échouer une méthode ; aucun run ne vise un signe positif (R3 tenu : le signe négatif est celui exigé). Mais la prédiction est peu tranchante : pour un recouvrement vrai de 0,85 sur 100 mondes, l'erreur type de l'écart R2 − R2⁻ est d'environ 0,05, donc un écart de plus de 0,10 survient avec une probabilité d'environ 5 % par méthode, et environ 18 % pour au moins une des quatre méthodes, **sous symétrie parfaite** (calcul mien, loi normale). Elle est descriptive : sans effet sur les tables ; à écrire comme telle (CS2-09).
- **Ce que R2⁻ teste vraiment.** La symétrie de signe des méthodes, pas l'hypothèse H-C⁻ de Borjas et Doran (afflux qui réduit la production en place). Le contact « retire » des ponts seulement au sens contrefactuel : on **ajoute** un fond synthétique à 90 % des paires-années. Cela augmente la variance des non-traitées, donc la puissance n'est pas celle de R2 miroir ; « un échec n'y viendra pas de la puissance » (S20) n'est pas démontré. À écrire.
- **Cohérence avec « aucune œuvre réelle supprimée »** : **tenue à la lettre** (seules des œuvres synthétiques sont ajoutées ; garde de plomberie prévue ; base inchangée à β = 0). Réserve de réalisme : 90 % de la base porte alors des œuvres synthétiques (artefact « œuvres synthétiques reconnaissables » du brouillon 1, à mesurer aussi en R2⁻).
- **Prédiction de signe à deux branches (section Hypothèse)** : la réfutation est **asymétrique** : H-C⁺ est réfutée si la borne haute est ≥ 0, c'est-à-dire par tout résultat nul sous-puissant (cas probable pour Campos, taux de base 0,004 %) ; H-C⁻ ne l'est que par une borne basse > 0. L'affectation d'une expérience à une branche (« niches distinctes et complémentaires » contre « afflux dans une même niche ») n'est pas opérationnalisée, et Azoulay n'en reçoit aucune : une réaffectation après coup resterait possible. Pas de conséquence sur les tables de ce préenregistrement, mais le texte l'écrit comme prédiction à deux issues réfutables.
- **CS2-09 (moyen)** — (a) écrire que la prédiction R2 / R2⁻ est descriptive et peu tranchante ; (b) dire que R2⁻ teste la symétrie de signe des méthodes, non H-C⁻ ; (c) renvoyer entièrement la prédiction à deux branches au préenregistrement de la gradation 2, avec règle d'affectation gelée et critères de réfutation symétriques.

---

## D. Témoin T2b et S17 — verdict : **à corriger (majeur)**

- **CS2-10 (majeur)** — T2b ne mesure pas le motif de Reisach et ne peut pas servir de témoin tel que défini.
  1. Le coefficient de détermination d'une variable régressée sur toutes les autres est **invariant au changement d'échelle** : l'ordre de T2b est identique en brut et en standardisé, et v_R² est identique dans les deux échelles. Les deux mesures « brute et standardisée » de v_R², et la prédiction « écart brute − standardisée ≤ 0,10 » (PA-T2b) sont donc vraies par construction (seule l'étape du lasso peut différer). C'est une prédiction qui ne peut qu'être confirmée (R3, esprit).
  2. Le motif de Reisach (p. 9, § 5.1) concerne une **chaîne** à forte triabilité dont les corrélations successives croissent. Le sous-graphe planté est une étoile courte (C → sortie, C → L, S → C, D → C). En affectation au hasard, C est binaire et indépendant de tout : son coefficient de détermination est voisin de zéro, il vient **toujours** en tête de l'ordre, T2b se réduit à une régression de la sortie sur C (et prédécesseurs) et v_R² ≥ 0,80 est presque garanti. Même remarque pour T2 en brut (C binaire à 10 %, variance 0,09). Ma prévision : T2b dépasse 0,70 de recouvrement en R2 et R3, au-dessus de la fourchette 0,2 à 0,8 du brouillon.
  3. Conséquence : S14 (h) (« T2b atteint la règle de recouvrement en standardisé dans R2 et R3 ») se déclenchera très probablement, et l'audit prévu (issues (i) à (iii) du brouillon 1 : lecture de la vérité, erreur de code, contrefactuel faux) ne peut rien constater d'un tri trivial : **déclencheur sans issue**, et verdict « non concluant » (ligne 1) en attendant.
  Correction : soit définir T2b plus fidèlement (ordre par corrélations successives le long du sous-graphe, évalué dans les conditions où le motif peut exister : O et H), soit renoncer à l'appeler témoin de l'artefact qui survit à la standardisation et dire que T2b est un témoin de « régression naïve sur une cause exogène à faible variance » ; dans tous les cas écrire l'issue de l'audit (h) et retirer la comparaison brut / standardisé de v_R².
- **Déclencheur d'audit sans disqualification (S17) : non justifié tel que posé.** S12 disqualifie (ligne 3) une méthode dominée par le tri par variance, alors que S17 ne fait que « mentionner » une méthode égalée par le tri par coefficient de détermination, artefact présenté comme plus insidieux. La justification (« aucune perturbation simple n'efface le motif ») dépasse la fiche, qui dit seulement que la standardisation et l'harmonisation d'échelle ne suffisent pas (p. 9). Il faut soit une règle de ligne (par exemple : mention portée au verdict **et** obligation de battre T2b d'une marge dans une condition où le motif est rompu), soit assumer que le verdict ne tient pas compte de cet artefact et l'écrire dans « Ce que l'épreuve n'autorise pas ».
- **CS2-18 (mineur)** — « R2 » désigne la condition (affectation au hasard, taille moyenne) **et** « R² » le coefficient de détermination (T2b, v_R²) ; avec « R2⁻ » le texte devient ambigu. Renommer l'un.

---

## E. Sélection supervisée (S21, D-5) — verdict : **à corriger (majeur)** ; la fuite n'est pas fermée

- Les deux moitiés sont coupées sur les **paires-années** (rôle 15), et E (20 %) est tenu à l'écart de l'entraînement par paire-année : les mêmes **paires** se retrouvent dans l'entraînement, E₁ et E₂. Les sorties Y⁺ sont des sommes sur trois années **qui se chevauchent** d'une année à la suivante ; aucune erreur groupée par paire n'est prévue pour le test sur E₂.
- En **B-hors**, les dimensions apprises contiennent des covariables réelles persistantes (S, D, A, g(Y⁰)) : une association trouvée sur E₁ se retrouve sur E₂ par la persistance de la paire, non par un effet ; la fausse détection dépasse alors le 0,01 nominal, et la garde « Bv0, 200 répétitions, ≤ 0,02 » (faite sur base jouet) ne le verrait pas.
- En **B-θ**, z est indépendant d'une paire-année à l'autre **si** le tirage est fait par paire-année (non écrit : « z_i (rôle 13) »), donc la fuite par z est fermée ; il reste la corrélation du bruit de sortie (anticonservateur, non quantifié).
- **CS2-11 (majeur)** — Couper E₁ / E₂ **par paire** (et séparer E de l'entraînement par paire), erreurs groupées par paire, fenêtres de sortie non chevauchantes entre les deux moitiés (ou espacées d'au moins τ_max), écrire que z est tiré par paire-année en B-θ.
- **CS2-12 (moyen)** — Deux restes d'oracle : (a) « graine médiane » = celle dont **r_g** (calculé avec la vérité) est la médiane ; (b) signe aligné = signe du coefficient × signe de ρ_S(ẑ_k̂, z₁). C'est identique pour M4 et M5, mais cela contredit « praticable et honnête » (D-5). Soit une règle sans vérité (par exemple, une graine fixée d'avance, ou la graine de plus petite perte sur E₁), soit l'écrire comme reste d'oracle assumé.

---

## F. Gabarit et règles — verdict : **gabarit tenu ; à corriger sur R4, R5, budget, étiquettes de seuils**

- **Gabarit.** Les huit sections exigées par `prereg.py` (Hypothèse ; Prédiction chiffrée et signe attendu ; Métrique ; Seuil ; Plan d'analyse ; Critères de lecture gelés ; Liste d'arrêt ; Contre-lecture) sont présentes ; l'en-tête (auteur, date, commit, documents) l'est aussi ; la section supplémentaire « À intégrer… » est hors liste exigée. **tenu.**
- **Blocage du scellement par la section « après le verdict du collisionneur » : tenu.** `problemes()` ajoute « marqueur À REMPLIR restant hors des sections exigées » dès que le marqueur subsiste dans le texte et qu'aucun autre problème ne le mentionne ; une fois les seuils remplis et la contre-lecture écrite, c'est ce contrôle global qui bloque (lecture du code, non exécuté). Réserve : blocage **mécanique** (supprimer le mot suffit à le lever) ; la vraie garde reste le GO de Lazar. Note : la contre-lecture finale doit citer deux empreintes (brouillon relu et rapport), sinon le validateur refuse.
- **Seize seuils, numérotation stable : numéros tenus, étiquettes inexactes.** S1 à S16 sont présents et numérotés comme au brouillon 1 ; mais l'en-tête annonce « conservées sauf S7, S12, S14, S15 », alors que **S11** (règle d'effet remplacée par S21 : demi-échantillons, k̂ = k*), **S13** (booléen ajouté), **S6** (portée réduite à B-hors) et **S9, S10, S16** (étendus à R2⁻) changent aussi. **CS2-13 (majeur)** ci-dessous pour S11 ; pour les autres, corriger les étiquettes.
- **CS2-13 (majeur)** — S11 « effet » : seuil de 90 % des mondes Bv1 (et, par renvoi, Bθv1) pour « trouve l'effet » **avec** sélection sur demi-échantillon et k̂ = k*. La propre prédiction du brouillon (PB-M4θ : 0,6 à 0,95 ; confiance 0,60) est centrée sous 90 %, alors que le verdict attendu « oui sous hypothèse » (confiance 0,55) exige la ligne 9, donc EFFθ vrai. Les deux ne tiennent pas ensemble ; et la ligne 8 (« non EFFθ ») placée avant la ligne 9 fait de l'effet le verdict probable, qui masque la question posée (identification de la latente). Le seuil est aussi une estimation ponctuelle sans intervalle (probabilité 0,5 au seuil exact). L'auteur signale la dureté du seuil à Lazar ; il faut en plus réconcilier prédiction et seuil, ou faire de l'effet une mention plutôt qu'une ligne bloquante, et marquer S11 « mis à jour ».
- **R4 (symétrie).** Pour le « trop propre » : (a), (c), (e), (h), (j), (k) ; pour le « trop mauvais » : (b), (i). **CS2-14 (moyen)** : aucune issue « trop mauvaise » en B-θ : si M4 échoue **dans** les hypothèses du théorème (r̃ < 0,50 en Bθv) alors que la garde sur base jouet est passée, c'est le résultat le plus suspect (erreur de code), et il n'a pas de déclencheur ; la ligne 4 le traite comme « échec en échantillon fini ». Ajouter un déclencheur (l).
- **R5 (chaque garde testée sur un cas sain et sur un artefact).** Les neuf gardes nouvelles listées ont chacune un cas sain et un artefact. **CS2-15 (moyen)** : la liste d'arrêt contient des lignes **sans garde testée** : M3 avec une autre classe que DirectLiNGAM ; dimension apprise ≠ 5 en B-θ ; sous-étude dont la plantation diffère au bit près ; T2b sélectionné autrement que par critère d'information bayésien (seule T2 est testée). Et la garde « fausse détection ≤ 0,02 sur 200 répétitions » échoue à tort avec une probabilité d'environ 5 % au niveau nominal 0,01 (loi de Poisson de moyenne 2 : P(≥ 5) ≈ 0,053) : fixer une borne exacte (binomiale) ou plus de répétitions. L'artefact de la garde « B-θ identifiable » (Bθc) est un contrôle négatif plus qu'un code fautif : acceptable, à nommer ainsi.
- **Budget (≈ 107 h).** Le script rejoué reproduit : option 2, 5 graines, **107,2 h** (volet A 37,5 h ; échelles 13,0 h ; volet B 53,3 h ; sous-étude 3,3 h) ; option 1 : 87,2 h ; 3 graines : 85,8 h ; 10 graines : 160,5 h. **Cohérent avec les temps supposés** (1,5 min par monde du volet A, 1,0 min par échelle, 1,0 min par entraînement). **CS2-16 (moyen)** : ces temps ne sont pas mesurés (SUPPOSÉ) et 1,5 min couvre six méthodes dont PCMCI, DirectLiNGAM et la prédiction invariante ; S15 = 110 h laisse 2,6 % de marge et ne compte ni les 20 mondes de validation, ni les relances ; la règle de réduction n'est pas chiffrée (le script ne calcule que « option 2 réduite » : 100,5 h) ; « environ 1 900 mondes » (Plan § 9) contre 1 820 par le script (1 500 + 200 + 120). À chiffrer ; et vérifier le calendrier contre la porte G0 (fin novembre 2026 au plus tard) : 107 h de temps mural s'ajoutent à l'écriture du code, aux gardes et à la contre-lecture de brouillon 3.
- **CS2-20 (moyen, prévu)** — Les sections Métrique et Plan d'analyse disent « inchangé par rapport au brouillon 1 » : un texte scellé doit se suffire à lui-même (R1, R6). Le brouillon 3 doit les reprendre en entier (déjà prévu en R-653) ; à vérifier à la contre-lecture finale.

---

## G. Les sept décisions D-1 à D-7 — verdict : **à corriger (format, noms, manques)**

- **Cohérence avec les chiffres.** D-1 (≈ 87 h, ≈ 107 h), D-2 (≈ 86 h, 107 h, 161 h ; S15 = 110 h), D-3 (0,852 → 0,818 ; 0,180) sont conformes à la sortie du script rejouée. D-1 option 3 (« coût moindre ») : le script ne la chiffre pas ; par recoupement (200 mondes × 2 méthodes × 5 graines) elle coûte environ autant que l'option 1 (≈ 87 h). Les confiances (0,65 ; 0,6 ; 0,7 ; 0,85 ; 0,75 ; 0,7) sont plausibles ; D-1 gagnerait à citer CS2-06 et CS2-13, qui réduisent l'intérêt de B-θ tel que défini.
- **CS2-17 (moyen) — format** (consignes du dépôt : décision en une phrase ; enjeu ; 2 ou 3 options avec avantage et inconvénient ; recommandation et confiance ; défaut). D-1, D-3, D-5 : conformes. **D-2** : options chiffrées sans avantage ni inconvénient. **D-4** : l'option 1 n'a ni avantage ni inconvénient. **D-6** : idem. **D-7** : hors format (ni options, ni recommandation, ni confiance). « Aucune ne prend de défaut » est défendable pour celles qui touchent une hypothèse avant scellement ; D-2, D-4 et D-6 relèvent du périmètre interne d'une phase, où la hiérarchie du dépôt applique un défaut de 48 heures : le dire.
- **Nom.** « D-1 … D-7 » collisionne avec les conditions descriptives « D1 à D4 » du même texte (« en D2 », « D-2 ») et avec « D1, D2, D3 » de la hiérarchie du dépôt. Renommer (par exemple « décision I-1 à I-7 »).
- **Décisions manquantes.** (1) **D-8** : traitement du compte de valeurs de u (échelle de définitions, CS2-08) ; (2) niveau et rôle de l'effet dans S11 et dans la Table Bθ (CS2-13) ; (3) règle de choix de la graine et du signe sans vérité (CS2-12) ; (4) unité de coupe et erreurs groupées (CS2-11) ; (5) statut de T2b et issue de S14 (h) (CS2-10) ; (6) statut de la prédiction à deux branches (ici ou gradation 2, CS2-09). Les « lectures à confirmer » restantes (corrélation de rangs ou de Pearson dans le papier ; invariance d'échelle de DirectLiNGAM démontrée ou attendue ; délais de Campos et d'Iaria) ne sont pas des décisions mais doivent être soldées ou écrites comme réserves avant le gel ; celle sur « d » est soldée (CS2-04).

---

## Tableau des constats

| N° | Gravité | Lieu | Objet |
|---|---|---|---|
| CS2-01 | majeur | Hypothèse ; Suites (Iaria) | −0,222 attribué à la colonne (1) ; c'est −0,217 (colonne 1) ou colonne (3) |
| CS2-02 | majeur | Suites (Azoulay) | 8,79 % accolé à −0,086 ; il correspond à −0,092 |
| CS2-03 | mineur | Hypothèse ; Suites (Campos) | « −16 % » : p. 11 ; calcul 15,4 % |
| CS2-04 | moyen | S6, S19, W5θ | d = dimension apprise dans le brouillon, observations dans le papier |
| CS2-05 | moyen | W5 (b) | corrigendum (observations discrètes) appliqué à des sources discrètes |
| CS2-06 | majeur | W5θ, PB-M4θ, S19 | théorème 1 garantit ∼A seulement ; permutation (théorème 2) exige un mélange à dérivées secondes ; activation linéaire par morceaux |
| CS2-07 | moyen | S19, S13 | 22 = choix non sourcé ; plancher de S13 = 21 < 22 |
| CS2-08 | majeur | nœud ouvert 2 ; S13, liste d'arrêt | échelle de définitions de u écrite d'avance ; décision à Lazar |
| CS2-09 | moyen | Hypothèse (signe) ; S20 | R2⁻ = symétrie de signe, prédiction peu tranchante ; deux branches à réfutation asymétrique |
| CS2-10 | majeur | T2b ; S17 ; S14 (h) | R² invariant à l'échelle ; T2b trivial en affectation au hasard ; déclencheur sans issue ; asymétrie avec S12 |
| CS2-11 | majeur | S21 ; Métrique (volet B) | coupe par paire-année, pas d'erreurs groupées : fuite non fermée en B-hors |
| CS2-12 | moyen | S21 | graine médiane et signe choisis avec la vérité |
| CS2-13 | majeur | S11 ; Table Bθ | seuil d'effet de 90 % contre prédiction 0,6–0,95 ; étiquette « inchangé » inexacte |
| CS2-14 | moyen | S14 | pas de déclencheur « trop mauvais » pour M4 en Bθv |
| CS2-15 | moyen | Liste d'arrêt | lignes sans garde R5 ; garde à 5 % de fausse alarme |
| CS2-16 | moyen | S15 ; Plan § 9 | temps non mesurés, marge 2,6 %, réduction non chiffrée, 1 820 contre « 1 900 » |
| CS2-17 | moyen | D-1 à D-7 | format incomplet (D-2, D-4, D-6, D-7) ; nom en collision ; décisions manquantes |
| CS2-18 | mineur | partout | « R2 » condition contre « R² » coefficient de détermination |
| CS2-19 | mineur | fiche § 6 (hors brouillon) | empreinte abrégée d'Azoulay fausse |
| CS2-20 | moyen (prévu) | Métrique ; Plan | renvois « inchangé » à reprendre en entier (brouillon 3) |

Aucun constat n'est « bloquant » au sens d'une faute qui interdirait de geler quoi que ce soit : tous se corrigent par réécriture, deux d'entre eux (CS2-10, CS2-13) changent des lignes de lecture et demandent une décision de Lazar.

## Verdict global

**Gelable après corrections.** Le brouillon 2 est fidèle aux sources pour l'essentiel (rejeu du script identique ; Khemakhem, Reisach, Borjas, Campos, Locatello vérifiés à la page), B-θ respecte bien les hypothèses du théorème 1 au sens de l'identifiabilité à transformation linéaire près, et le blocage du scellement par la section réservée fonctionne. Il n'est pas gelable en l'état à cause de CS2-01 et CS2-02 (chiffres mal attribués, règle R7), CS2-10 (témoin T2b tautologique et déclencheur sans issue), CS2-11 (fuite entre sélection et test), CS2-13 (seuil d'effet incompatible avec la prédiction) et CS2-06 (garantie surestimée en B-θ), et CS2-08 doit devenir une décision. Après ces corrections, intégrer le verdict du collisionneur (brouillon 3, déjà prévu), puis une contre-lecture sur ce brouillon 3 (le brouillon 2 l'annonce, et celle-ci n'en tient pas lieu).

## Contre-lecture (entrée à reporter dans le préenregistrement, après correction)

Contre-lecture 1 — sous-agent Sonnet 5.5 neuf ; brouillon relu `f61ae4c01d51b05007b58103e22b5b9c5219c9da98b72d2c7eef135f7388c5b2` ; rapport `prereg/brouillons/contre-lecture-identification-semi-reel-v1-brouillon2.md` (empreinte à calculer par l'orchestrateur à l'écriture du compagnon) ; traitement de chaque constat CS2-01 à CS2-20 : à écrire (accepté, refusé et pourquoi) dans le brouillon 3.
