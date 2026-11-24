# Préenregistrement : la géométrie lexicale du passé prédit-elle les premières cooccurrences de termes au-delà d'une hiérarchie de nuls topologiques ? (banc des corpus contre des modèles nuls emboîtés, version 1)

- **Auteur** : concepteur Claude Opus 5.5 neuf, distinct des lecteurs et des proposeurs (règle 1 a du protocole X 2.1). **Écart déclaré** : la règle nomme Claude Fable 5.2 ; Fable est gelé jusqu'au 2 décembre 2026.
- **Mandat** : GO-2026-11-24-46 (boucle fermée du collisionneur groupé). **Date** : 2026-11-24 (UTC). Classe A. Commit du code d'analyse : sera inscrit au scellement de l'additif de code ; aucun code n'existe à cette date.
- **Pièces lues (empreintes sha256)** : table des épreuves `docs/notes/boucle-fermee-groupe-v1/table-des-epreuves-v1.md` (`cc3bcbe9…`) ; protocole X 2.1 `docs/notes/protocole-x-v2/protocole-x-v2-1-boucle-fermee.md` (`c11b44aa…`) ; note de sortie du collisionneur, branche `idees/lot-8-chef-d-orchestre-v1` (`9b831716f`), `…/note-sortie-groupe-naissance-idees-fecondes-v1.md` (`2cdfa231…`) ; cellules d'Opus `E3-T3-reponse-A.md` des deux bras et critiques `E3-T2-critique-croisee-B.md`, `-C.md` des deux bras ; fiche du corpus `donnees/corpus-cit-hepth-stanford-snap-v1/fiche-corpus-cit-hepth-v1.md` (`34eddc1affd844baf85fac9cb586c08c611b2310daf99c67965272b80db9ad20`). Archives (non vues par le concepteur) : `cit-HepTh-abstracts.tar.gz` `d4f33c10ebae1d504328e62b5232ea67ac43ebaa1bd58fda13385ae29e610026` ; `cit-HepTh-dates.txt.gz` `4b5f2259b0feb848a2a93ab3345d344a4b1c3c9c773ddebcab95f2f6e0bf6225`.
- **Ce que le concepteur a vu du corpus** : le seul schéma de la fiche (nombres de fichiers par année, noms de champs d'en-tête, bornes du fichier de dates). Aucun titre, résumé ni mot.

## Hypothèse

Proposition éprouvée (note de sortie, section 8, retenue 2 ; cellule d'Opus, bras témoin, A1′ ; bras principal, P1′) : « la connaissance latente bat le nul topologique ». Forme opérationnelle : sur les résumés d'arXiv en physique théorique des hautes énergies (archive « cit-HepTh »), un plongement lexical appris sur les fenêtres de phrase du seul passé ajoute, à la prédiction des paires de termes qui co-apparaissent pour la première fois dans les douze mois qui suivent une coupure, une information que n'apportent ni les fréquences, ni les degrés, ni des blocs estimés sur le passé, ni la topologie à plusieurs sauts du graphe de co-mention documentaire (Katz, PageRank personnalisé, décomposition spectrale de même algorithme et de même dimension), ni des coordonnées aléatoires de même dimension.

Deux hypothèses complémentaires, sur le même dispositif, avec la statistique θ et le seuil c définis plus bas :
- **H_A** : θ > c (la géométrie lexicale porte une information propre sur les premières cooccurrences) ;
- **H_B** : θ ≤ c (ce qu'elle porte est déjà dans la hiérarchie de nuls, ou n'atteint pas le gain minimal jugé utile).
Elles sont exclusives et exhaustives ; il n'y a pas de zone d'abstention. Rien n'est revendiqué au programme par ce plan ; aucune hypothèse du programme (H1 à H9, HC1 à HC5) n'est modifiée.

## Prédiction chiffrée et signe attendu

- Prédiction du concepteur, jugement subjectif et non chiffre de littérature : θ̂ petit, de signe positif ou nul, dans [−0,02 ; 0,06] (unités : logarithme népérien du rapport des précisions moyennes) ; probabilité subjective de H_A : 0,35. Raison : une part de la « connaissance latente » peut n'être que de la cooccurrence de second ordre, que la décomposition spectrale documentaire capte déjà (cellule d'Opus, bras témoin, III.1 ; critiques de Carbon et de Neon).
- Témoin vrai (monde planté, section « Témoins ») : θ > c attendu, de signe positif, dans au moins 4 mondes sur 5. Monde nul : θ ≤ c dans au moins 4 sur 5. Témoin faux : θ ≤ c partout.
- Réfute H_A : θ̂ ≤ c sur la coupure principale, épreuve vivante et exécutable. Réfute H_B : θ̂ > c dans les mêmes conditions.
- Aucun chiffre de la littérature n'entre dans ce plan. Les effets publiés de type « connaissance latente » (faits servis, § 5) sont **non vérifiés** (R7) et ne fixent rien ici.

## Métrique

- **Unité de prédiction** : paire non ordonnée de termes (u, v) du vocabulaire V_s de la tranche s, ne partageant aucun mot (« black » et « black hole » exclus), **jamais co-mentionnés** dans un document d'identifiant daté ≤ s (tous documents, révisés ou non). C'est le dénominateur complet, sans échantillonnage, à l'évaluation.
- **Cible** Y(u, v) = 1 si u et v apparaissent tous deux dans au moins un document (titre et résumé) dont le mois d'identifiant est dans ]s ; s + 12 mois].
- **Décile de fréquence d'une paire** : décile de log df_u + log df_v (df : fréquence documentaire dans les documents de traits de la tranche) ; bornes calculées sur les paires candidates de la tranche de test, avant toute lecture de la cible.
- **Précision moyenne** AP_q(M) d'un modèle M dans le décile q : sémantique exacte de `sklearn.metrics.average_precision_score(y, score, sample_weight=w)` (scikit-learn 1.9.1), poids w = 1 pour l'estimation, multiplicités du bootstrap sinon.
- **Statistique unique** : θ = (1/|Q_j|) Σ_{q ∈ Q_j} [ ln AP_q(G+L) − ln max_{M ∈ C} AP_q(M) ], où Q_j est l'ensemble des déciles jugeables (section « Plan d'analyse », étape 5) et C = {M0, M1, M2, G, G+R} l'ensemble des comparateurs. Le maximum est pris décile par décile.
- **Intervalle** (rapporté, non décisif) : bootstrap par nœuds, 200 répliques ; intervalle percentile à 90 % bilatéral ; erreur type = écart type des répliques.

## Seuil

- c = max( ln 1,05 ; max_{b=1..19} θ_b ), où θ_b est la même statistique calculée en remplaçant L par des coordonnées aléatoires neuves R_b (nul de capacité, maximisation sur C refaite à chaque tirage). Avec 19 tirages, le maximum est le quantile de niveau 0,05. ln 1,05 ≈ 0,0488 est le gain minimal jugé utile : 5 % de précision moyenne relative au meilleur comparateur, choix de conception.
- Décision : θ̂ > c ⇒ H_A ; θ̂ ≤ c ⇒ H_B.
- Taux d'erreur visé : au plus 0,10 de mauvaise décision quand |θ − c| ≥ η = 0,02 (approximation normale) ; le risque dans la bande |θ − c| < 0,02 est rapporté, non contrôlé.
- c est calculé et inscrit au journal **avant** tout calcul impliquant L.

## Plan d'analyse

**Tranches** (mois d'identifiant ; « s » = dernier jour du mois inclus) :
- principale : apprentissage s0 = 2000-12 (cible 2001-01 à 2001-12), test s1 = 2001-12 (cible 2002-01 à 2002-12) ;
- placebo 1 (cible tirée dans le passé de s0) : s0 = 1998-12, s1 = 1999-12 (cible 2000) ; placebo 2 : s0 = 1997-12, s1 = 1998-12 (cible 1999).
Chaque tranche s recalcule tout sur ses seuls documents de traits.

**Modèles** (tous : `HistGradientBoostingClassifier(loss="log_loss", learning_rate=0.1, max_iter=200, max_leaf_nodes=31, min_samples_leaf=50, l2_regularization=1.0, max_bins=255, early_stopping=False, random_state=<graine de la tâche>)`, mêmes lignes d'apprentissage pour tous dans une tranche) :
- M0 (fréquences) : min et max de log df ;
- M1 (degrés) : M0 + min et max de log(1 + k), log(1 + k_u k_v) (k : degré binaire dans le graphe de co-mention) ;
- M2 (blocs) : M1 + indicatrice « même bloc », log(ω̂_{b_u b_v} + 1e-9) ;
- G (topologie à plusieurs sauts) : M2 + log(1 + voisins communs), Adamic-Adar, log Katz, log PageRank personnalisé symétrisé, cosinus du plongement documentaire S ;
- G+R : G + cosinus de coordonnées gaussiennes R ; G+L : G + cosinus du plongement lexical L ; G+F : G + cosinus du témoin faux F.
Chaque ajout (R, L, F) est un seul trait de même forme : capacité égale.

**Ordre des étapes, figé** (garde d'ordre, section « Gardes d'arrêt ») :
1. Mondes plantés (témoins) ; verdict des témoins scellé. Arrêt si épreuve morte.
2. Corpus réel : lecture, gardes de format, tranches, vocabulaires, traits (L compris : calculer le plongement n'est pas lire), empreinte de l'objet des traits écrite au manifeste **avant** le chargement de la cible.
3. Cible ; comptage des positifs par décile (aucun prédicteur lu).
4. Apprentissage de M0, M1, M2, G, G+R sur la tranche s0 : toutes les paires positives (au plus 50 000, tirées au hasard au-delà) et 4 fois autant de négatives tirées uniformément parmi les candidates (échantillonnage cas-témoins déclaré ; le rang n'en dépend pas) ; évaluation sur tout le dénominateur de s1, par blocs d'un million de paires.
5. Déciles jugeables Q_j : un décile est non jugeable si ses positifs sont moins de 20, ou si max_{M∈C} AP_q(M) ≥ 0,95 (plafond : analogue prédictif d'une fibre atomisée, le comparateur ne laisse plus de place). Plus de 3 déciles non jugeables ⇒ « non exécutable ».
6. Seuil c (19 tirages R_b, chacun réappris) ; inscrit.
7. Analyse de puissance, sur un tirage nul : θ_R calculée avec R_1 à la place de L, erreur type SE_0 par 200 répliques du bootstrap par nœuds. Exécutable si SE_0 ≤ η / 1,2816 = 0,0156. Effectif : N_V, plus petite valeur de {2000, 3000, 4000} qui satisfait les étapes 5 et 7, essayées dans cet ordre (étapes 2 à 7 refaites pour chaque N_V ; c refait pour le N_V retenu). Aucune ⇒ « non exécutable », arrêt, rien de L n'est calculé.
8. Témoin faux sur le corpus réel : θ_F (F à la place de L). θ_F > c ⇒ épreuve morte, arrêt.
9. Alors seulement : G+L, θ̂, décision, intervalle.
10. Descriptif, non décisif : placebos 1 et 2 (θ̂ et c propres à chacun, mêmes règles, N_V retenu) ; échelle des niveaux (θ contre chaque niveau seul, M0 à G+R ; niveau ℓ* le plus profond encore battu ; un niveau non jugeable par la règle de l'étape 5 est signalé, jamais lu comme négatif).

**Bootstrap par nœuds** (unité indépendante : le terme) : tirer des multiplicités m ~ Multinomiale(N_V ; 1/N_V) ; poids de la paire = m_u m_v ; modèles figés (pas de réapprentissage) ; bornes de déciles et Q_j figés ; une seule mise en ordre des scores par modèle, puis sommes cumulées pondérées vectorisées (testées contre scikit-learn sur échantillons réduits).

**Comparaisons multiples** : une seule statistique décisive ; placebos, échelle des niveaux et déciles isolés sont descriptifs et ne corrigent ni ne changent la décision.

**Graines (R9)** : `controle_ia.manifeste.graines(taches, entropie=2026112701)` ; noms de tâches : `monde-vrai-1..5`, `monde-nul-1..5`, `R-<tranche>-<N_V>`, `R-nul-<b>-<tranche>-<N_V>` (b = 1..19), `F-rff`, `negatifs-<tranche>-<N_V>`, `gbm-<modele>-<tranche>-<N_V>`, `kmeans-<tranche>-<N_V>`, `bootstrap-<objet>-<N_V>`, `pas-placebo` ; `<tranche>` ∈ {principale, placebo1, placebo2}. Manifeste par run (configuration, empreintes, versions, graines, commit).

## Témoins (règle 1 b)

Joués à l'étape 1 avec exactement le même code de traits, de modèles et de statistique (seule la lecture du texte est court-circuitée : les mondes fournissent directement des phrases de termes).

**Générateur du monde planté.** M = 2000 termes. Pour chaque terme : position latente z_u ~ N(0, I_8) ; bloc b_u uniforme sur 20 blocs ; poids w_u = r_u^(−0,9), r_u permutation aléatoire de 1..M (z, b et w indépendants). Huit années de 2500 documents. Chaque document est « pont » avec probabilité π = 0,10 (toutes années), « ordinaire » sinon.
- Ordinaire : bloc principal b1 uniforme, secondaire b2 ≠ b1 uniforme ; 30 termes distincts : à chaque tirage, bloc b1 avec probabilité 0,7, sinon b2, puis terme du bloc ∝ w (sans remise ; si un bloc est épuisé, l'autre).
- Pont : terme germe ∝ w ; puis 29 termes distincts, tirés sans remise ∝ w_u · exp(−‖z_u − z_germe‖² / (2 · 1,5²)) sur tous les termes.
- Phrases, force s ∈ {0, 1} : avec probabilité s, ordre glouton : départ sur un terme du document tiré uniformément, puis ajout répété du terme restant le plus proche en z du dernier ajouté ; sinon ordre uniforme. Découpe en 5 phrases de 6 termes consécutifs.
- Ainsi la co-mention documentaire passée ne dépend de z que par les ponts ; les fenêtres de phrase la révèlent dans tous les documents ordinaires. Tranches : s0 = fin de l'année 6 (cible année 7), s1 = fin de l'année 7 (cible année 8). V_s : tous les termes présents dans les documents de traits. Dans les mondes, les étapes 3 à 6, 8 et 9 s'appliquent telles quelles ; l'étape 7 (puissance) ne s'applique pas ; un monde dont plus de 3 déciles sont non jugeables compte comme un échec du témoin concerné.

**Témoin vrai** : 5 mondes à s = 1 (`monde-vrai-k`). Doit tenir : H_A (θ > c) dans au moins 4 sur 5. Sinon les nuls absorbent un signal qui n'existe que dans les fenêtres, ou le banc ne le voit pas : épreuve morte.
**Monde nul** : 5 mondes à s = 0 (`monde-nul-k`), L n'a alors que l'information documentaire. Doit donner H_B dans au moins 4 sur 5. Sinon le seuil laisse passer de faux gains : épreuve morte.
**Témoin faux** F, de même dimension d = 100 que L : x_u = (log df_u, log(1 + k_u)) centrés réduits sur V_s ; F_u = √(2/d) · cos(W x_u + β), W ∈ R^{100×2} de loi N(0, 1/0,5²), β uniforme sur [0, 2π[ (tirés une fois, tâche `F-rff`) ; trait = cosinus(F_u, F_v), fonction des seuls degrés et fréquences du passé, déguisée en plongement. Doit mourir : H_B dans les 5 mondes à s = 1 **et** sur le corpus réel (étape 8). Une seule survie ⇒ épreuve morte.
**Épreuve morte** : aucune issue n'est lue, l'arrêt est rapporté, aucun repli ni changement de paramètre (protocole X 2.1, règle 1 b).

## Données et étanchéité

- **Lecture** : fichiers `AAAA/NNNNNNN.abs` ; blocs séparés par une ligne `\\` ; en-tête = deuxième bloc ; résumé = blocs suivants non vides joints par une espace (cas des 11 fichiers à 5 à 7 blocs) ; lignes d'en-tête commençant par une espace jointes au champ précédent. Texte retenu : `Title` + « . » + résumé. Aucun autre champ (`Journal-ref`, `Comments`, `Report-no` peuvent porter de l'information postérieure).
- **Source de la date, fixée** : le mois de l'identifiant (`yymmnnn` ; année = 1900 + yy si yy ≥ 91, 2000 + yy sinon), qui couvre toute l'archive. Le fichier de dates (arrêté au 2002-03-12) n'entre pas dans la décision ; son accord avec l'identifiant (identifiants à 7 chiffres sans préfixe 11) est rapporté.
- **Révisions** : t_rev = plus tardive des dates analysables des lignes `Date` de l'en-tête (format de courrier, `email.utils.parsedate_to_datetime`). Document de traits pour la tranche s si mois d'identifiant ≤ s **et** t_rev ≤ fin de s (t_rev illisible : mois d'identifiant seul, compté). Les documents révisés après s restent comptés pour exclure des candidates les paires déjà co-mentionnées. Fuite résiduelle déclarée : un texte révisé sans ligne `Date` nouvelle n'est pas détectable.
- **Termes, sans dictionnaire externe** : suppression de `$…$` et des commandes `\mot` (remplacées par une coupure) ; minuscules ; phrases coupées sur `[.;:!?]` suivi d'un blanc ; mots `[a-z][a-z-]*[a-z]` de 3 lettres ou plus ; mots vides = `sklearn.feature_extraction.text.ENGLISH_STOP_WORDS` de scikit-learn 1.9.1, liste figée de mots outils sans terme de domaine, écrite dans un fichier empreinté ; un mot vide ou une ponctuation coupe les bigrammes. Termes = unigrammes et bigrammes de mots adjacents retenus ; aucune racinisation. V_s = les N_V termes de plus grande fréquence documentaire parmi ceux de fréquence ≥ 5 dans les documents de traits de s (égalités : ordre lexicographique).
- **Traits de la tranche s, figés avant la cible** : graphe A (co-mention documentaire, comptes ; A_bin = A > 0) ; k = degré dans A_bin ; blocs : 20 blocs par regroupement spectral (matrice d'adjacence régularisée A_bin + (k̄/N_V)·J, normalisée symétriquement ; 20 premiers vecteurs propres, lignes normées, `KMeans(n_clusters=20, n_init=10)`), ω̂_ab = arêtes entre blocs / paires possibles ; Katz = (I − βA_bin)⁻¹ − I, β = 0,5 / λ_max(A_bin) ; PageRank personnalisé Π = 0,15 (I − 0,85 P)⁻¹, P = A normalisée par ligne (boucle propre pour une ligne nulle), trait = log((Π_uv + Π_vu)/2 + 1e-12) ; voisins communs et Adamic-Adar sur A_bin (poids 1/ln k, nul si k < 2).
- **Plongements, même algorithme** : PPMI avec lissage des contextes à l'exposant 0,75, décomposition en valeurs singulières de rang d = 100, plongement U_d Σ_d^0,5, lignes normées. L : comptes de fenêtre, occurrences de termes distantes de 1 à 5 positions de mots retenus dans la même phrase, sans recouvrement (un bigramme occupe la position de son premier mot) ; S : comptes de co-mention documentaire A. R : vecteurs N(0, I_100) tirés une fois pour l'union triée des vocabulaires, indexés par terme.

## Gardes d'arrêt

Chacune lève `controle_ia.gardes.GardeArret`, sans repli ; chacune a un test sur cas sain (passe) et sur artefact (arrête) dans `tests/`.
- **Étanchéité** : tout document de traits de s a mois d'identifiant ≤ s et t_rev ≤ s ; l'empreinte de l'objet des traits est écrite avant que la fonction de cible puisse s'exécuter. Artefact : un document de 2002 injecté dans les traits de 2001-12.
- **Ordre** : automate d'états (témoins scellés → traits → cible → comparateurs → c → puissance → témoin faux → L) ; tout calcul de θ avec L avant l'état final arrête. Artefact : appel direct du calcul de θ pour L.
- **Format** : 29 555 fichiers ; empreintes des archives égales à celles de la fiche ; année du dossier = année de l'identifiant ; t_rev lisible pour au moins 95 % ; au moins 20 000 documents datés ≤ 2001-12. Artefact : archive tronquée de fixture.
- **Valeurs** : aucun NaN ni infini dans les traits, les scores ou les AP. Artefact : NaN injecté.
- **Graines** : numpy ≥ 1.25 (`exiger_numpy_minimal`) ; graine reconstruite = graine consignée. Artefact : manifeste altéré.
- **Budget** : 6 heures de temps réel ; dépassement, mémoire épuisée ou perte de machine = panne technique, consignée comme « faux échec » (jamais un résultat), relance permise sur le même accord.
- **Non exécutable** (étapes 5 et 7) : arrêt déclaré, jamais lu comme négatif. Artefact : corpus de fixture de 300 documents (doit être déclaré non exécutable).

## Spécification pour le code

Paquet `src/controle_ia/banc_corpus_nuls_v1/` : `corpus.py` (lecture, dates, révisions), `termes.py`, `traits.py` (graphe, blocs, Katz, PageRank, PPMI), `monde_plante.py`, `modeles.py`, `statistique.py` (AP pondérée, θ, c, bootstrap), `automate.py` (garde d'ordre), `lanceur.py` ; tests dans `tests/test_banc_corpus_nuls_v1.py`. Dépendances : `requirements-cpu.txt` (numpy, scipy, scikit-learn 1.9.1) ; aucun appel réseau. Sorties sous `runs/banc-corpus-nuls-v1/<run_id>/` : manifeste, journal d'étapes horodaté, tableaux par décile, scellés (R6). Code de classe B : contre-lu par un autre modèle avant la course.

## Critères de lecture gelés

| issue | verdict sur « la connaissance latente bat le nul topologique » |
|---|---|
| témoin vrai < 4/5, ou monde nul < 4/5 en H_B, ou témoin faux survit une fois | épreuve morte : non concluant, arrêt rapporté, aucun repli |
| non exécutable (étapes 5 ou 7) ou garde technique | non concluant (non exécutable ou faux échec), jamais négatif |
| épreuve vivante, exécutable, θ̂ ≤ c | **mort de la proposition** sur ce corpus (H_A réfutée) : la géométrie lexicale n'est pas revendicable comme supérieure à la topologie ; le volet corpus ne l'emploie plus comme signal sans nouvelle épreuve |
| épreuve vivante, exécutable, θ̂ > c | **la proposition vit** (H_B réfutée sur ce corpus) ; pas de confirmation générale : un seul corpus, un seul domaine |
| audit R4 qui trouve un défaut | non concluant ; l'audit ne peut jamais changer H_B en H_A |

- Placebos et échelle des niveaux sont rapportés avec la décision et n'en changent pas le sens.
- **Audit de symétrie R4 du banc des corpus**, déclenché par : θ̂ > ln 1,5 ; θ̂ < −ln 1,05 (ajouter un trait ne devrait pas dégrader nettement) ; signe de θ̂ opposé à celui des deux placebos ; SE_0 < 0,002 ; θ_F exactement nul. Contenu : (a) relecture indépendante des dates par l'identifiant seul ; (b) part des 1 000 paires les mieux classées par G+L qui touchent un terme vu surtout dans des documents révisés ; (c) rejeu de la tranche principale avec une graine racine neuve ; (d) vérification de l'étanchéité sur 20 documents tirés. Mené par un sous-agent neuf, rapporté avant toute communication du verdict.

## Liste d'arrêt

- Épreuve morte (témoins) : arrêt avant l'étape 2 ou à l'étape 8 ; rapport ; aucune lecture de θ pour L.
- Garde d'étanchéité, d'ordre, de format, de valeurs ou de graines : arrêt ; correction du seul code fautif (classe B, contre-lu) puis relance complète ; aucune lecture de résultat avant la correction.
- Non exécutable : arrêt, déclaré tel ; pas d'augmentation de N_V au-delà de 4000 ni de changement de tranche sans nouveau préenregistrement.
- Panne technique : faux échec, relance sur le même accord.
- **Repli si le format réel diffère du schéma de la fiche** (garde de format levée) : ne change que la lecture (découpe des blocs, champs, analyse des lignes `Date`), réécrite sur le schéma constaté par une extraction qui ne lit aucun titre ni résumé, contre-lue, inscrite en additif scellé avant toute lecture de résultat. Si le mois d'identifiant n'était pas lisible, la date viendrait du champ `Date` (première date analysable) et, à défaut, l'épreuve serait non exécutable. Ne changent pas : tranches, vocabulaire, traits, modèles, statistique, seuil, témoins, critères.
- Toute autre déviation : écart à un préenregistrement scellé, nœud de décision de Lazar.

## Contre-lecture

À REMPLIR après contre-lecture par un Sonnet 5.5 neuf.
