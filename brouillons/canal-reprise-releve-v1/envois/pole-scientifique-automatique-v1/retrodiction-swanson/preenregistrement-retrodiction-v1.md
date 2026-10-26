# Préenregistrement — rétrodiction de la marche « à la Swanson » sur arXiv — v1

Écrit par un sous-agent neuf de la lignée conv-audit, **avant tout calcul d'issue**, en exécution du brief
`BRIEF-retrodiction-swanson-v1.md` (empreinte `3b83d11396d8c0508912751cb0b40df11b83843b04c0d0b9ebf93e29d0c7c0e4`,
vérifiée). Le brief prime : ce document le reprend et tranche les seuls points d'implémentation qu'il laisse ouverts,
sans toucher aux seuils, aux périodes, au vocabulaire ni aux décisions.

Données : `donnees/arxiv-2003-2016-v1.parquet` (empreinte `1412b1c97276ef27a17ce6470ee2b0192c86dabda330d66d71e811d7fceeab7e`,
vérifiée avec `EMPREINTES-donnees-v1.txt`), 999 260 lignes ; révision du jeu source dans `provenance-jeu-v1.txt`.

**Ce qui a été regardé avant d'écrire ce document** : schéma du fichier ; effectifs par année ; préfixes des catégories
principales ; identifiants en double (37 identifiants, 47 lignes en trop, même année à l'intérieur de chaque
identifiant) ; trois résumés tirés au hasard pour régler le nettoyage du LaTeX. Rien d'autre : aucun vocabulaire, aucune
fréquence de terme, aucune cooccurrence, aucun score, aucune issue.

## 1. Hypothèse, prédictions, signe

- Hypothèse testée : sur arXiv 2003-2016, ordonner les paires de termes spécifiques de champs différents, jamais
  cooccurrents avant 2011, par la marche « à la Swanson » (S) donne une précision à 10 000 (i) supérieure de 12 points ou
  plus à celle du tirage stratifié (ST) — décision D1 ; (ii) supérieure d'au moins 2 points, intervalles disjoints, à celle
  de la meilleure méthode classique parmi Adamic-Adar (AA), allocation de ressources (RA), voisins communs (CN),
  attachement préférentiel (PA) — décision D2.
- Mes prédictions, écrites avant de rien voir, sans effet sur les décisions : signe de S − ST positif (confiance 0,9) ;
  S − ST ≥ 12 points : non (confiance 0,6) ; S bat la meilleure méthode classique de 2 points, intervalles disjoints : non
  (confiance 0,75) ; meilleure méthode classique attendue : allocation de ressources ou attachement préférentiel.

## 2. Corpus et découpages

- Une ligne par identifiant : pour les 37 identifiants en double, on garde la première ligne dans l'ordre croissant
  (catégories, titre, résumé). Année = colonne `annee` (année de la première version).
- Découpage principal : avant = 2003-2010 ; après = 2011-2016. Placebo : avant = 2003-2006 ; après = 2007-2010.
- Ordre des documents : (année, identifiant).
- Catégorie principale = premier élément de `categories` (séparateur : espace) ; groupe par préfixe (avant le premier
  point) : `math` → math ; `cs` → cs ; `astro-ph`, `cond-mat`, `gr-qc`, `hep-*`, `math-ph`, `nlin`, `nucl-*`, `physics`,
  `quant-ph` → physique ; `q-bio` → q-bio ; `q-fin` → q-fin ; `stat` → stat ; tout autre préfixe (`eess`, `econ` :
  environ 2 800 documents sur 2003-2016) → « autre ». Ces documents comptent dans les fréquences et les cooccurrences ;
  « autre » ne peut pas être le champ d'un terme spécifique.

## 3. Termes (règles du brief ; détails fixés ici)

1. Texte = titre + « . » + résumé (le point empêche un bigramme à cheval sur les deux).
2. Normalisation Unicode par décomposition de compatibilité (NFKD), caractères non ASCII retirés (« poincaré » →
   « poincare »), minuscules.
3. Formules retirées et remplacées par une coupure : `$$…$$`, `$…$`, `\(…\)`, `\[…\]`, environnements `equation`,
   `eqnarray`, `align`, `gather`, `multline`, `displaymath`, `math` (étoilés compris) ; appariement non gourmand, sur
   plusieurs lignes.
4. Commandes LaTeX retirées sans espace : barre oblique inverse suivie de lettres (et d'une étoile éventuelle), ou suivie
   d'un caractère non alphabétique non blanc (accents `\'`, `\"`, `` \` ``, `\^`, `\~`, symboles `\%`, `\&`…) ; accolades
   retirées (« schr\"{o}dinger » → « schrodinger »).
5. Éléments : suites de lettres `[a-z]+` (mots) et suites de caractères qui ne sont ni lettres, ni blancs, ni traits
   d'union (coupures). Blancs et traits d'union ne coupent pas.
6. Jeton = mot d'au moins trois lettres absent des deux listes fixes ci-dessous.
7. Unigrammes = jetons ; bigrammes = « j1 j2 » pour deux mots consécutifs qui sont tous deux des jetons (un mot vide, un
   mot de moins de trois lettres ou une coupure entre eux empêche le bigramme).
8. Document = ensemble de ses unigrammes et bigrammes (présence).
9. Vocabulaire = termes de fréquence documentaire d'avant df ∈ [50 ; 0,05 × N_avant], bornes incluses, N_avant = nombre de
   documents d'avant. Le placebo a son propre vocabulaire, même règle sur ses documents d'avant.
10. Comptage par empreinte blake2b de 64 bits des chaînes ; tout conflit d'empreinte touchant un terme d'un vocabulaire
    arrête le calcul (vérifié sur toutes les occurrences, avant et après).
11. Les documents d'après sont extraits par les mêmes règles et projetés sur le vocabulaire d'avant ; les termes hors
    vocabulaire sont ignorés.

Mots vides anglais (liste fixe ; le code en porte une copie et un essai vérifie l'égalité avec ce bloc) :

```liste-mots-vides
a about above across after afterwards again against all almost alone along already also although always am among
amongst an and another any anybody anyhow anyone anything anyway anywhere are aren around as at be became because become
becomes becoming been before beforehand behind being below beside besides between beyond both but by can cannot could
couldn did didn do does doesn doing don done down during each either else elsewhere enough etc ever every everybody
everyone everything everywhere except few for from further furthermore had hadn has hasn have haven having he hence her
here hereafter hereby herein hereupon hers herself him himself his how however i if in indeed into is isn it its itself
just less many may me meanwhile might mightn mine more moreover most mostly much must mustn my myself namely neither never
nevertheless no nobody none noone nor not nothing now nowhere of off often on once only onto or other others otherwise
ought our ours ourselves out over own per perhaps quite rather same shall shan she should shouldn since so some somebody
somehow someone something sometime sometimes somewhat somewhere still such than that the their theirs them themselves then
thence there thereafter thereby therefore therein thereof thereupon these they this those though through throughout thru
thus to together too toward towards under unless until up upon us very via was wasn we were weren what whatever when
whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whom
whose why will with within without won would wouldn yet you your yours yourself yourselves
```

Mots académiques génériques (liste fixe, même vérification) :

```liste-mots-generiques
additionally address addressed addresses aim aims analyse analysed analyze analyzed analyzes approach approaches article
articles based consider considered considering considers demonstrate demonstrated demonstrates demonstrating describe
described describes describing discuss discussed discusses discussing discussion examine examined examines examining
explore explored explores exploring finally find finding findings finds found give given gives giving important
importantly indicate indicated indicates introduce introduced introduces introducing investigate investigated investigates
investigating investigation letter manuscript method methodology methods novel obtain obtained obtaining obtains paper
papers particular particularly perform performed performing performs present presented presenting presents previous
previously propose proposed proposes proposing provide provided provides providing recent recently report reported reports
respectively result resulting results show showed showing shown shows significantly studied studies study studying suggest
suggested suggests use used uses using various
```

Mots volontairement absents des deux listes (ils portent des termes de métier : « work function », « fully developed »,
« main sequence », « top quark », « even parity », « two dimensional », « new physics ») : work, develop(ed), main, top,
bottom, even, well, one, two, first, new, analysis, effect, problem, case, system, model, data, theory.

## 4. Champs

- Pour chaque terme du vocabulaire : nombre de ses documents d'avant par groupe (six groupes et « autre ») ; champ =
  groupe de plus grande part (égalité : premier dans l'ordre math, cs, physique, q-bio, q-fin, stat, autre) ; part =
  effectif du champ / df.
- Terme spécifique : part ≥ 0,6 et champ ≠ « autre ».

## 5. Paires candidates et tirage

- Termes candidats : spécifiques, df_avant ∈ [50 ; 3 000] (bornes incluses).
- Paire candidate : paire non ordonnée {A, C} de termes candidats de champs différents, n_avant(A, C) = 0 (aucun document
  d'avant ne contient les deux).
- Strates : paires non ordonnées de champs (au plus 15).
- Effectif de strate N_s = |T_f| × |T_g| − nombre de paires de la strate cooccurrentes au moins une fois avant (calcul
  exact). « Nombre de paires possibles de chaque strate » est lu comme N_s (paires qui satisfont tous les critères).
- Allocation : n_s ∝ N_s, arrondi au plus fort reste (égalité de reste : ordre des strates), somme exactement 1 000 000
  (toutes les paires si Σ N_s < 1 000 000).
- Tirage dans la strate : uniforme sans remise, par rejet — on tire (a, c) uniformément dans T_f × T_g par lots, on écarte
  doublons et paires cooccurrentes, on garde les n_s premières valides dans l'ordre de tirage. Ordre des strates : ordre
  lexicographique des couples (f, g), f avant g dans l'ordre math, cs, physique, q-bio, q-fin, stat.
- Étiquetage : A = terme du champ qui vient en premier dans cet ordre, C = l'autre (n'affecte que les variantes orientées
  secondaires de S).
- Graines : `numpy.random.SeedSequence(entropy=20261026)` ; `spawn(2)` → enfant 0 : principal, enfant 1 : placebo ;
  chacun `spawn(6)` dans l'ordre : tirage des paires (un petit-enfant par strate, dans l'ordre des strates), ST, U,
  rééchantillonnage, permutations, sous-échantillon d'essai ; générateur `numpy.random.default_rng` (PCG64). Clés
  d'engendrement consignées dans le manifeste.

## 6. Issue

- Positive si n_après(A, C) ≥ 3 (nombre de documents d'après contenant A et C) ; sinon négative.
- Taux de base global et par strate, intervalles de Wilson à 95 %.
- Ordre d'exécution : scores calculés, écrits et empreintés (heure consignée) **avant** le calcul des issues.

## 7. Méthodes (données d'avant seulement)

Notations : n(X, Y) = nombre de documents d'avant contenant X et Y, X ≠ Y (pas de diagonale) ; |d| = nombre de termes du
vocabulaire du document d ; r(X) = Σ_{Y≠X} n(X, Y) = Σ_{d∋X} (|d| − 1) ; Γ(X) = {Y ≠ X : n(X, Y) > 0} ; deg(X) = |Γ(X)| ;
idf(B) = ln(N_avant / df(B)), logarithme népérien.

- (S) Σ_B P(B|A)·P(C|B)·idf(B), P(B|A) = n(A,B)/r(A), P(C|B) = n(B,C)/r(B), B parcourant tout le vocabulaire. Avec
  K(A,C) = Σ_B n(A,B)·n(B,C)·idf(B)/r(B) (symétrique) : S(A→C) = K/r(A), S(C→A) = K/r(C). **Score S qui décide =
  ½ [S(A→C) + S(C→A)]** : paires et issue sont non orientées et le brief ne fixe pas le sens de la marche. Les variantes
  orientées S(A→C) et S(C→A) sont rapportées à titre secondaire, sans effet sur les décisions.
- (AA) Σ_{B∈Γ(A)∩Γ(C)} 1/ln deg(B) ; (RA) Σ_{B∈Γ(A)∩Γ(C)} 1/deg(B) ; (CN) |Γ(A)∩Γ(C)| ; (PA) df(A)·df(C), df d'avant.
  (B = A ou B = C ne contribue jamais : n(A, C) = 0.)
- (ST) ordre aléatoire (graine) à l'intérieur de chaque strate ; ordre global par quantile intra-strate (rang − 0,5)/n_s
  croissant, égalités départagées par une clé aléatoire (graine) : les k premiers prennent ≈ k·n_s/Σn_s paires de chaque
  strate.
- (U) permutation uniforme (graine).
- « Précision à k » = précision des k premiers dans l'ordre décroissant du score (et non un tirage proportionnel au score).

## 8. Mesures

- Précision à 1 000 et à 10 000 ; précision moyenne = Σ sur les seuils distincts de (R_n − R_{n−1})·P_n ; aire sous la
  courbe de fonctionnement du récepteur (paires positives contre négatives, égalités comptées pour moitié). Égalités de
  score pour la précision à k : espérance sous départage aléatoire (le groupe à cheval sur le rang k compte au prorata).
- Intervalles à 95 % : 1 000 rééchantillonnages des paires avec remise (même taille), percentiles 2,5 et 97,5 ; ordres
  des méthodes fixes ; mêmes tirages pour toutes les méthodes ; différences appariées S − ST et S − meilleur classique
  rapportées avec leurs intervalles (pour information).
- Strate « dominée par les termes passe-partout » : top1 = les ⌈0,01·V⌉ termes du vocabulaire (V termes) de plus grand
  df_avant (égalités : ordre alphabétique) ; K_top(A,C) = la somme K restreinte à B ∈ top1 ; paire dominée si K > 0 et
  K_top/K > 0,5 (fraction identique pour les deux sens de S et pour leur moyenne). Mêmes mesures dans cette strate, sur
  les mêmes rééchantillonnages restreints ; ST y est recalculé avec les proportions de strates de la sous-population
  (graine dérivée de celle de ST) ; précision à k déclarée non définie si la strate compte moins de k paires.

## 9. Décisions (figées par le brief, reprises sans changement)

- **D1** : S est **retenue** comme règle de tirage de la version 0 si P@10 000(S) − P@10 000(ST) ≥ 12 points
  (estimations ponctuelles sur le million de paires) ; sinon **réfutée**.
- **D2** : meilleur classique = méthode de plus grande P@10 000 parmi {AA, RA, CN, PA} (estimation ponctuelle) ; S est une
  **contribution** si P@10 000(S) − P@10 000(meilleur) ≥ 2 points **et** si les intervalles à 95 % de P@10 000 de S et du
  meilleur sont disjoints ; sinon on adopte le meilleur classique **sous son nom**, sans revendication.
- Seul l'ensemble du million de paires décide. Strate dominée, placebo, variantes orientées : rapportés, sans effet sur
  D1 ni D2.

## 10. Contrôles

- (a) Issues permutées : 20 permutations globales des issues (graine) ; pour chaque méthode, précision à 1 000 et à
  10 000, précision moyenne, aire. Réussite si, pour chaque méthode, la moyenne sur les 20 permutations de P@10 000 est à
  moins de 4 erreurs-types (√(p(1−p)/10 000)/√20) du taux de base p, et la moyenne de l'aire à moins de 4 erreurs-types
  (√((n₊+n₋+1)/(12·n₊·n₋))/√20) de 0,5. Échec = fuite présumée, signalée en tête du rapport.
- (b) Placebo : toute la chaîne refaite sur 2003-2006 / 2007-2010 (vocabulaire, champs, candidats, tirage de 1 000 000
  de paires, scores, issues, mesures, intervalles). Stabilité : ordre des cinq méthodes à score {S, AA, RA, CN, PA} par
  P@10 000 identique → « stable » ; sinon « partiellement stable » si chaque paire de méthodes inversée a des intervalles
  qui se recouvrent dans au moins un des deux découpages ; sinon « instable ». Tau de Kendall sur les sept méthodes
  rapporté.
- (c) Absence de fuite temporelle, essais automatiques :
  (i) essai synthétique sur un petit corpus, avec la chaîne même du calcul réel : documents d'après modifiés, retirés ou
  bourrés de cooccurrences des paires candidates → vocabulaire, champs, candidats, paires tirées et scores identiques au
  bit près ; un document d'avant modifié → ils changent ; un calculateur volontairement fuyant (qui lit les documents
  d'après) doit être pris par l'essai (garde éprouvée sur un cas sain et sur un artefact) ;
  (ii) sur les données réelles : toutes les lignes des matrices qui servent aux scores ont une année ≤ 2010 (≤ 2006 au
  placebo) ; les fréquences documentaires recalculées sur ces seules lignes sont celles qui ont servi ; les composantes
  des scores (K, K_top, CN, AA, RA, r, df) de 1 000 paires tirées au hasard, recalculées par une implémentation de
  référence lente (ensembles Python sur les seuls documents d'avant), concordent à 1e−9 près en relatif ; les degrés de
  300 termes tirés au hasard sont recalculés de même ; toutes les paires tirées vérifient n_avant(A, C) = 0.
  Aucune issue n'est calculée si un essai échoue.

## 11. Liste d'arrêt

- Conflit d'empreinte sur un terme d'un vocabulaire ; échec d'un essai (c) ; paire tirée cooccurrente avant ;
  incohérence de comptage (double comptage impair, somme des n_s ≠ cible) → arrêt, diagnostic, rien d'interprété.
- Mémoire ou temps : seuls la taille des lots et le parallélisme changent, jamais une définition.
- Tout choix d'implémentation qu'il faudrait changer après ce document : avenant daté et empreinté, écrit avant tout
  calcul d'issue ; après une issue, écart signalé et décisions inchangées.

## 12. Ce qui sera rendu (sous `sortie/`)

`retrodiction-swanson-v1.md` (D1 et D2 en tête, chiffres dans les deux sens — écarts signés avec intervalles, y compris
quand S perd —, contrôles, limites) ; ce préenregistrement ; le code (`code/`) ; les résultats bruts (`resultats/*.json`,
tableaux par paire en `.npz`) ; un manifeste de run (versions, graines, empreintes, heures lues sur `date -u`) ; un
compagnon `.sha256` pour chaque fichier rendu.

Horodatage : écrit le 2026-10-26 20:13:35 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), avant tout calcul d'issue.
