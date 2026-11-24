# Contre-lecture du préenregistrement brouillon « banc des corpus contre des modèles nuls emboîtés, version 1 »

- **Contre-lecteur** : Claude Sonnet 5.5 neuf (règle R2), qui n'a pas écrit le plan. Classe A. Lecture le 24 novembre 2026.
- **Brouillon relu** : `docs/notes/boucle-fermee-groupe-v1/plans/plan-banc-corpus-nuls-emboites-v1.md`, 136 lignes, sha256 `7a8d7d511c0915e732781e9ca173d21bf6f5ad646dbd962ce14f36d6b45db26f` (vérifié identique à l'empreinte donnée).
- **Pièces lues** : CLAUDE.md ; protocole X 2.1 (règles 1 a, 1 b) ; table des épreuves (`cc3bcbe9c968411ec27757e01d0ebf417797c939f16e7d4419854c270da97864`, vérifiée) ; fiche du corpus, schéma seul (`34eddc1a…20ad`, vérifiée) ; gabarit v2 ; note de sortie de la branche `idees/lot-8-chef-d-orchestre-v1` (`2cdfa231…8b`, vérifiée), sections 3 et 8. Rien lu sous `coffre/`, `docs/verdicts/`, `diag/`, `versement/` ni dans le corpus brut. Aucun code exécuté, aucun modèle externe appelé. Les lignes citées sont celles du brouillon.

## Verdict : scellable après corrections

Le plan tient l'essentiel : une statistique et un seuil uniques, deux hypothèses complémentaires, un ordre d'étapes figé avec garde, un témoin faux défini, un témoin vrai, « non exécutable » déclaré d'avance, une unité indépendante (le terme), un dénominateur complet. Aucune remarque n'est bloquante. Douze remarques sont à corriger avant le scellement : la plupart tiennent à des choix laissés au codeur, ou à un témoin vrai dont la force n'est ni calibrée ni vérifiable avant la course. Sept sont mineures.

Décompte : bloquantes 0 ; à corriger 12 ; mineures 7.

## Réponses aux points demandés

- **L'épreuve peut-elle tuer ?** Le témoin faux peut mourir (remarque 3 : il risque plutôt de survivre à tort, ce qui tuerait l'épreuve). Le témoin vrai peut tenir, mais sa force est inconnue et le monde planté risque la saturation (2, 10). Aucun témoin vrai n'existe sur le corpus réel (3, 11).
- **Étanchéité** : le calendrier d'apprentissage et de test est sain (les étiquettes d'apprentissage s'arrêtent à s1). Deux fuites ou dépendances au futur subsistent : le dénominateur et le tri des documents par révision future (5).
- **Unicité de la statistique et du seuil** : respectée, mais c vaut de fait ln 1,05 et son niveau annoncé est injustifié (1).
- **Nul maximisé** : la maximisation est bien refaite à chaque tirage ; le nul est cohérent, mais il ne joue pas le rôle annoncé (1).
- **Comparateurs de même capacité** : respecté (un trait ajouté, mêmes lignes). Un biais d'échelle entre tranches touche inégalement les traits (4).
- **Unité et intervalle** : terme, bootstrap par nœuds, modèles figés ; l'intervalle ignore la variance d'apprentissage (1).
- **Codabilité sans choix libre** : non atteinte (6 à 10).
- **Faisabilité au 27 novembre** : plausible, non démontrée (17).
- **Critères de lecture** : toute issue a un verdict, quelques précisions manquent (15).
- **Gardes** : testables sauf une (16). **Chiffres non marqués** : plusieurs conventions de la littérature (18).

## Remarques

### 1. À corriger : le seuil c vaut de fait ln 1,05, son « niveau 0,05 » n'est pas fondé, la variance d'apprentissage est absente (lignes 35 à 37, 62, 67)

Dans θ_b, le maximum sur C contient G, G+R et d'autres modèles, alors que le candidat n'est qu'un tirage. Les θ_b seront donc presque tous négatifs et c = max(ln 1,05 ; …) = ln 1,05. Le nul « refait la maximisation », comme le veut la règle, mais il ne lie jamais. De plus « le maximum de 19 tirages est le quantile de niveau 0,05 » suppose que G+L soit échangeable avec G+R_b sous le nul : or R_b est un bruit gaussien isotrope et L un plongement structuré, dont les cosinus ont une tout autre loi. Enfin SE_0 vient d'un bootstrap à modèles figés : l'aléa de l'apprentissage (négatifs tirés, arbres) en est absent, de même que du critère d'exécutabilité et de l'intervalle de la ligne 33.
**Correction** : écrire que c est en pratique ln 1,05 et que le nul des 19 tirages sert de vérification de capacité ; retirer « niveau 0,05 » ; rapporter les 19 θ_b et leur écart type ; ajouter à l'étape 7 le critère « écart type des θ_b ≤ 0,0156 » (variance d'apprentissage) en plus de SE_0 ; dire que l'intervalle de la ligne 33 est conditionnel aux modèles appris.

### 2. À corriger : force du témoin vrai non calibrée, risque de saturation du monde, mort de l'épreuve par hasard (lignes 77 à 86)

Avec 15 000 documents de traits et 20 blocs de 100 termes, les paires intra-bloc sont presque toutes déjà co-mentionnées à s0. Les candidates sont surtout les paires entre blocs et de queue de fréquence, que les fréquences et les blocs expliquent. Le signal en z ne passe, dans l'avenir, que par les 10 % de ponts, que S (co-mention documentaire PPMI) apprend en partie dès le passé. Rien ne garantit donc que θ dépasse 0,0488 dans quatre mondes sur cinq. Par ailleurs, la règle « ≥ 4/5 », « ≥ 4/5 » et « zéro survie du témoin faux sur 6 essais » a une probabilité de tuer l'épreuve par pur hasard non chiffrée : à puissance 0,8 par monde, P(≥ 4/5) vaut environ 0,74, soit 26 % de mort accidentelle du seul témoin vrai. Les mondes servent à la fois de calibration et de jugement (règles 9 et 10 du gabarit v2).
**Correction** : (a) fixer la force du monde (π, σ du noyau, s, nombre de documents) par un pilote sur des graines disjointes de `entropie=2026112701`, sans corpus réel, résultats inscrits au plan ; (b) chiffrer la probabilité de mort accidentelle de l'épreuve et la porter à la prédiction ; (c) envisager 10 mondes vrais avec seuil ≥ 8/10, ou accepter explicitement le risque et le dire.

### 3. À corriger : témoin faux et absence de témoin vrai sur le corpus réel (lignes 63, 85)

F n'est pas strictement redondante avec G : le noyau en (log df, log k) apparie les deux termes, ce que les traits min et max séparés d'un arbre n'expriment que mal. θ_F peut donc dépasser c sans défaut du banc, ce qui tuerait l'épreuve à tort. Le témoin faux ne prouve pas non plus que la chaîne de lecture du vrai texte (LaTeX, phrases, termes) laisse passer un signal : un échec d'analyse silencieux donnerait H_B.
**Correction** : (a) prédire par le pilote de la remarque 2 la loi de θ_F dans les mondes ; (b) ajouter sur le corpus réel un témoin vrai « avec fuite » : le plongement L calculé sur les documents des deux périodes, doit donner θ > c ; il est calculé après l'étape 8 et ne sert qu'à prouver que la chaîne voit un gain, avec le même code, étiqueté comme témoin et jamais comme résultat ; (c) en cas d'échec de (b), épreuve morte.

### 4. À corriger : dérive d'échelle entre tranche d'apprentissage et tranche de test (lignes 47, 59)

Les modèles sont appris sur s0 et appliqués à s1, où df, degrés, Katz et PageRank ont une autre échelle (plus de documents). Les arbres extrapolent mal pour ces traits, alors que les cosinus (L, S, R) sont bornés : cela avantage un trait stable comme L, de façon systématique vers H_A, et sans que R le compense puisque R est du bruit.
**Correction** : transformer chaque trait en rang normalisé (fonction de répartition empirique) par tranche, avant apprentissage et prédiction, pour tous les comparateurs ; ou mesurer la dérive en descriptif et l'inscrire comme réserve.

### 5. À corriger : fuite du futur dans le dénominateur et tri des documents par révision future (lignes 26, 92)

Les paires « déjà co-mentionnées » sont exclues d'après le texte final de documents révisés après s : le dénominateur dépend donc de texte postérieur à la coupure. Les documents révisés après s sont aussi retirés des traits, de sorte que le choix des documents du passé dépend d'un événement futur. Le plan déclare seulement la fuite des textes révisés sans nouvelle ligne `Date`.
**Correction** : déclarer ces deux dépendances dans les fuites résiduelles ; ajouter à l'étape 10 une analyse descriptive de sensibilité, avec exclusion des seules paires co-mentionnées dans les documents de traits ; ne pas en tirer de décision.

### 6. À corriger : lecture des dates et des révisions non codable sans choix (lignes 91, 92, 102)

Ne sont pas fixés : le motif exact de la ligne (« Date: » seul, ou aussi « Date (revised v2): »), la fiche ne listant que `Date` ; l'extraction de la date dans « Mon, 7 Dec 1992 … (35kb) » ; les années à deux chiffres ; les fuseaux (date naïve ou avertie, comparée à « fin de s ») ; l'action si `parsedate_to_datetime` échoue. Le seuil de 95 % n'a pas de source, et la garde de format l'applique à toute l'archive plutôt qu'aux années utilisées.
**Correction** : écrire l'expression régulière de reconnaissance, la normalisation (suppression de la taille entre parenthèses, fuseau ramené à UTC, fin de s = dernier jour à 23:59:59 UTC), le traitement des échecs ; calculer les 95 % sur les documents de s ≤ 2001-12 ; ou marquer ce seuil comme convention non vérifiée.

### 7. À corriger : chaîne de texte à choix libres (ligne 93)

À préciser : forme exacte du retrait des `$…$` (et de `$$…$$`, `\(…\)`, environnements, dollars orphelins) ; ce qu'est une « coupure » (espace, fin de phrase, ou les deux) pour une commande `\mot` ; traitement des chiffres, apostrophes, accents, tirets multiples ; construction des bigrammes (deux mots retenus adjacents sans coupure entre eux) ; la fréquence documentaire de V_s se calcule-t-elle en comptant dans un même ensemble unigrammes et bigrammes ; la liste ENGLISH_STOP_WORDS est écrite en fichier mais l'empreinte n'est pas inscrite.
**Correction** : donner, par règle, un exemple d'entrée et de sortie attendues, que les tests de la fonction `termes.py` reprennent ; exiger que le fichier de mots vides soit généré par le code et son empreinte inscrite au manifeste.

### 8. À corriger : cas limites numériques et objets non définis (lignes 29 à 30, 94, 95, 103)

Non fixés : cosinus d'un vecteur de norme nulle (termes sans fenêtre) ; log Katz avec élément nul (seul PageRank a 1e-12) ; ω̂ pour un bloc d'un seul terme (division par zéro) ; calcul de λ_max (solveur, tolérance) ; solveur et graine de la décomposition en valeurs singulières, signe et ordre ; diagonale de A (comptes de documents ?) ; PPMI des lignes nulles ; traitement des égalités de scores dans la précision moyenne (sklearn les groupe, la version vectorisée doit en faire autant, ce que le test ne fixe pas). La garde « aucun NaN ni infini » arrêterait la course sur un cosinus indéfini légitime.
**Correction** : fixer chaque convention (cosinus nul = 0, epsilon identique, solveur et graine par tâche nommée) et tester la précision moyenne vectorisée sur des égalités de scores.

### 9. À corriger : graines incohérentes (lignes 71, 95)

La ligne 95 dit que R est tiré une fois pour l'union des vocabulaires ; la ligne 71 nomme des tâches `R-<tranche>-<N_V>` par tranche et par N_V. `graines()` refuse les noms en double et il faut déclarer la liste complète d'avance. Les sous-tâches des mondes (négatifs, GBM, kmeans, R_b, bootstrap) n'ont pas de nom. Les tâches `kmeans-`, `gbm-`, `negatifs-` ne distinguent pas la chaîne des mondes.
**Correction** : trancher R par tranche ou global ; faire dériver les sous-tâches des mondes de `monde-<type>-<k>-<objet>` ; lister toutes les tâches avant l'appel.

### 10. À corriger : générateur du monde planté incomplet (lignes 77 à 81)

Non précisés : tirage d'un terme « ∝ w dans le bloc » (poids relatifs au bloc) ; résolution des égalités dans le terme « le plus proche en z » ; sens d'« ordre uniforme » ; départ « tiré uniformément » parmi les termes du document ; statut des « années » dans le code (tranche, mois) ; arrêt du tirage sans remise quand 30 termes ne sont pas disponibles.
**Correction** : écrire le générateur en pseudo-code, ou renvoyer à une fonction testée contre un cas de 20 termes dont la sortie est donnée.

### 11. À corriger : dégénérescence silencieuse de L sur le vrai texte (lignes 57, 123)

Un défaut d'analyse du LaTeX, des phrases ou des bigrammes pourrait donner un L pauvre et un H_B apparent, sans qu'aucun contrôle ne le voie. L'audit R4 ne prévoit pas de déclencheur pour un résultat négatif banal.
**Correction** : inscrire, avant la cible, des diagnostics sur L : part de termes avec au moins 20 contextes, corrélation entre les cosinus de L et de S sur un tirage de 1 000 paires, nombre moyen de termes par phrase ; seuils fixés, arrêt ou audit R4 en cas de sortie des bornes.

### 12. À corriger : règles de forme du gabarit v2 (lignes 1 à 8, 134 à 136)

Le plan n'emploie pas le gabarit, mais ses règles doivent être couvertes. Règle 8 (amputation placebo) : à déclarer « sans objet : pas une redécouverte de primitive ». Règle 9 (seuils sur générateurs disjoints) : non tenue, voir 2 ; η, 20 positifs et 0,95 ne sont pas fixés sur des données disjointes. Règle 10 (lot d'étalonnage distinct du lot jugé) : c et N_V sont fixés sur la tranche jugée sans L, ce qu'il faut dire (le lot reste le même, la décision n'en dépend pas, grâce à la garde d'ordre). La section « Contre-lecture » contient « À REMPLIR », que le validateur du gabarit refuse ; à remplir après cette lecture.

### 13. Mineure : prédiction incohérente avec sa probabilité (ligne 19)

L'intervalle [−0,02 ; 0,06] et la probabilité de H_A de 0,35 ne se concilient que si 35 % de la masse tient entre 0,0488 et 0,06. Dire si l'intervalle est à 50 % ou à 80 %.

### 14. Mineure : « placebos » n'en sont pas (lignes 44, 123)

Les coupures de 1998 et 1999 sont des répliques sur d'autres années, pas des placebos où l'effet devrait disparaître. Le déclencheur d'audit « signe opposé à celui des deux placebos » en suppose l'effet nul. Les renommer « coupures de réplication », et ne déclencher l'audit que si les deux répliques ont des signes opposés à la principale et que ceux-ci l'emportent sur leur écart type.

### 15. Mineure : critères de lecture, trois précisions (lignes 114 à 123)

(a) Dire qu'un audit R4 qui ne trouve rien laisse le verdict. (b) La ligne « θ̂ ≤ c » doit nommer ce qui est réfuté : un gain d'au moins 5 % sur le meilleur comparateur, non l'absence d'information. (c) Dire qu'une réserve de la remarque 4 ou 5, si elle est mesurée en descriptif, s'écrit au verdict sans le changer.

### 16. Mineure : gardes à tester (lignes 99 à 106)

La garde « Budget » n'a pas d'artefact de test (dépassement simulé). La garde « Non exécutable » : préciser à quelle étape la fixture de 300 documents échoue, pour éviter qu'elle plante avant la garde.

### 17. Mineure : faisabilité d'ici le 27 novembre (lignes 62, 105, 110)

Le calcul est vraisemblable : environ 8 millions de paires au plus, inversions denses de 4 000 sur 4 000, une trentaine d'apprentissages. Mais la durée sous six heures n'est pas mesurée, l'empreinte mémoire d'un million de paires par bloc non plus, et il y a huit modules à écrire, tester et contre-lire en classe B en un jour.
**Correction** : mesurer la durée sur les dix mondes (étape 1, avant toute lecture du corpus) et en tirer le budget par étape ; fixer la limite de mémoire de la garde.

### 18. Mineure : conventions de la littérature non marquées (lignes 22, 35, 94, 95)

Amortissement 0,85 et 0,15 du PageRank, exposant 0,75 de lissage des contextes (usage des plongements PPMI), β = 0,5/λ_max de Katz, Adamic-Adar, `n_init=10` : conventions de la littérature, non vérifiées sur PDF (R7). Les marquer « convention, non vérifiée », comme déjà fait pour η, 0,95 et 20.

### 19. Mineure : références et formulation (lignes 5, 22, 39)

Les empreintes de la table, du protocole et de la note sont tronquées (`cc3bcbe9…`) ; donner les empreintes complètes (R6). Les cellules d'Opus citées n'ont pas d'empreinte. « faits servis, § 5 » renvoie à une section absente du plan. La ligne 39 (« c calculé avant tout calcul impliquant L ») contredit l'étape 2, où L est calculé : écrire « avant tout calcul de score ou de θ impliquant L ».

## Ce que le concepteur a déclaré non fixable

- (1) Dates et révisions : acceptées (déclaration honnête). (2) Seuil de 95 % : voir 6. (3) Durée non mesurée : voir 17. (4) Force du témoin vrai : voir 2, la mesurer par pilote sur graines disjointes est possible sans toucher au corpus. (5) Valeurs sans source : voir 12, 18. (6) Licence : sans objet pour la décision, déjà notée à la fiche. (7) Commit du code par additif : accepté, à condition que le code ne soit contre-lu qu'après le plan scellé et qu'il ne change aucune règle de ce plan.
