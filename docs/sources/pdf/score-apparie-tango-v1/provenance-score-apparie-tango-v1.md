# Provenance — source du score apparié dit de Tango (v1)

- Relevé du 22 novembre 2026, entre 10:44Z et 10:47Z (`date -u`), par un Opus 5.5 neuf mandaté par la session des mathématiques nouvelles ; classe C, 0 USD.

## Source primaire visée
Tango T. (1998), « Equivalence test and confidence interval for the difference in proportions for the paired-sample design », Statistics in Medicine 17(8) : 891-908, DOI 10.1002/(sici)1097-0258(19980430)17:8<891::aid-sim780>3.0.co;2-b.
- **PDF primaire non obtenu.** OpenAlex (`api.openalex.org/works/doi:…`, interrogé le 22 novembre vers 10:46Z) : `is_oa: false`, `oa_status: closed`, aucun dépôt d'archive ouverte. Aucune copie chez l'éditeur en accès libre, aucun dépôt d'auteur ni PubMed Central trouvés. Pages de l'auteur à l'Institut national de santé publique du Japon (`niph.go.jp/soshiki/gijutsu/staffs/tango/sm_eng2.html`, `…/download/mcn99a/index.html`) : 404.
- Une copie existe sur une page de cours universitaire (`site.uottawa.ca/~nat/Courses/csi5388/Tango.paired.pdf`) : ni page de l'éditeur, ni dépôt d'auteur ; statut légal non établi ; **non téléchargée**.

## Source secondaire versée (code, pas PDF)
- Paquet R `contingencytables` 3.1.1 (CRAN, licence GPL-3, publié le 2026-10-27), compagnon du livre de Fagerland, Lydersen et Laake, « Statistical Analysis of Contingency Tables » (ISBN 9781466588172). Adresse : `https://cran.r-project.org/src/contrib/contingencytables_3.1.1.tar.gz`, téléchargé le 22 novembre 2026 entre 10:45:46Z et 10:47:23Z.
- Fichiers versés : `cran-contingencytables_3.1.1-20261122T1046Z.tar.gz` (archive telle que servie) ; `contingencytables-3.1.1-Tango_asymptotic_score_CI_paired_2x2.R` (extrait, MD5 `2a77db6b…` identique à celui du fichier `MD5` du paquet).
- Lignes : 78-85 (`test_statistic.4`, statistique), 89-98 (`ML_estimate.4`, A, B, C, racine) ; fonction nommée « The Tango asymptotic score confidence interval for the difference between paired probabilities ».

## Sources consultées, non versées
- NCSS, chapitre 520 « Two Correlated Proportions (McNemar Test) », `ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Two_Correlated_Proportions-McNemar_Test.pdf`, sha256 `7c7adf616797df9d890dcd6c147c803ec7a876d31cbbcf6349c59ce1d28c9f52` : intervalle « Nam's Score » renvoyant à « Nam (1997) or Tango (1998) », p. 520-4 et 520-9 ; paramétrisation différente (p̂21 = (−e + √(e² − 8f))/4), non identique terme à terme ; document « All Rights Reserved », non versé.
- Huang et Self (2010), manuscrit d'auteur NIH, PMC3481840 : quadratique 2n x² + (−b − c − (2n − b + c)δ)x + cδ(δ + 1) = 0 (convention de signe de la marge différente) ; PDF non téléchargeable par programme (épreuve anti-robot de PubMed Central) ; non versé.
- Vignette `ratesci` « Paired contrasts » (CRAN) : cite Tango 1998, ne donne pas la forme close.
