# Registre des références du papier D — v1

- **Rédaction** : fille 1, 24 novembre 2026. Outil : `verifier_references_v1.py` (empreinte dans son compagnon). Résultats bruts : `resultats/` (trois passes, la dernière l'emporte).
- **Méthode** : notice de la source qui fait foi (arXiv ; éditeur par son identifiant numérique, ou DOI, via Crossref ; page des actes) comparée à ce que nos textes affirment (titre, premier auteur, année) ; PDF arXiv versionné téléchargé hors du dépôt et empreinté. Les verdicts automatiques douteux sont revus à la main ; la raison est écrite en colonne « note ».
- **Limite** : pour les références hors arXiv, seule la notice de l'éditeur est vérifiée ; le PDF n'est pas lu (accès payant). Aucune de ces références ne fournit de chiffre au papier : elles servent à l'attribution. La lecture de l'affirmation à la page citée (Price, Robertson, Fisher, Lancaster, Stein) reste à faire, sur PDF fourni par Lazar.
- **Bilan** : 67 références ; concordantes : 64 ; corrigée : 1 (`bartok2014`) ; non confirmée : 1 ; PDF non accessible : 1. Quatorze verdicts sont manuels : un vérificateur neuf les repasse, avec un échantillon tiré au sort des verdicts automatiques.

## Corrections à transmettre (à la fille 2, par les mères)

1. `bartok2014` : le numéro arXiv 1102.2041 désigne un autre article (« Toward a Classification of Finite Partial-Monitoring Games », Antos, Bartók, Pál, Szepesvári, 2011). L'article cité est *Mathematics of Operations Research* 39(4), 2014, DOI 10.1287/moor.2014.0663 : remplacer l'identifiant arXiv par ce DOI.
2. `hirsch2006monotone` : année 2006 (notice éditeur), chapitre 4, pp. 239–357.
3. `rivest2006` : non confirmée ; ne pas la citer tant que la source n'est pas trouvée.
4. `dresher1962sampling` : notice non vérifiable depuis la session ; à garder en réserve.
5. `griffin2024` : titre « … AI Deployment Protocols » confirmé (déjà corrigé par la fille 2).

## Table

| Clé | Verdict | Source | Identifiant | PDF | Note |
|---|---|---|---|---|---|
| `rivest2006` | NON_CONFIRMEE | web |  | — | l’adresse essayée renvoie un autre article de Rivest (« The ThreeBallot Voting System ») ; source à trouver |
| `dresher1962sampling` | PDF_NON_ACCESSIBLE | web |  | — | site de la RAND refusé par le réseau de la session (403) : panne d’accès, à demander à Lazar |
| `agarwal2021theory` | CONCORDE | arxiv | 1908.00261 | PDF arXiv 1908.00261v5 sha256 91e0f7c19a23bfcd…, 77 p. |  |
| `aitken1934` | CONCORDE | crossref (recherche) | 10.1017/s0013091500008063 | — |  |
| `ateniese2007` | CONCORDE | crossref (recherche) | 10.1145/1315245.1315318 | — |  |
| `avenhaus2002inspection` | CONCORDE | crossref (doi) | 10.1016/s1574-0005(02)03014-x | — | chapitre 51 du Handbook of Game Theory with Economic Applications, vol. 3, 2002 |
| `bailey2024` | CONCORDE | arxiv | 2412.09565 | PDF arXiv 2412.09565v2 sha256 9c23a613c5c7e3a2…, 51 p. |  |
| `baker2025` | CONCORDE | arxiv | 2503.11926 | PDF arXiv 2503.11926v1 sha256 2547162c549d70e0…, 39 p. |  |
| `bartok2014` | CORRIGEE | crossref (doi) | 10.1287/moor.2014.0663 | — | nos textes portent arXiv:1102.2041, qui est un autre article ; notice correcte vérifiée par DOI |
| `becker1968crime` | CONCORDE | crossref (doi) | 10.1086/259394 | — |  |
| `blocki2013audit` | CONCORDE | arxiv | 1303.0356 | PDF arXiv 1303.0356v2 sha256 dee408355be629f8…, 9 p. |  |
| `boucheron2013concentration` | CONCORDE | crossref (recherche) | 10.1093/acprof:oso/9780199535255.001.0001 | — | livre, Oxford University Press, notice éditeur |
| `cen2022fast` | CONCORDE | arxiv | 2007.06558 | PDF arXiv 2007.06558v5 sha256 23fddbc3f493d02e…, 40 p. |  |
| `chapman1951` | CONCORDE | crossref (doi) | 10.1214/aoms/1177729548 | — |  |
| `cloud2024` | CONCORDE | arxiv | 2410.04332 | PDF arXiv 2410.04332v2 sha256 b391aa6af529e5de…, 45 p. |  |
| `dong2023raft` | CONCORDE | arxiv | 2304.06767 | PDF arXiv 2304.06767v4 sha256 a4fd25115d817afd…, 29 p. |  |
| `evalplus2023` | CONCORDE | arxiv | 2305.01210 | PDF arXiv 2305.01210v3 sha256 52d35d25a10c38da…, 15 p. |  |
| `fisher1930` | CONCORDE | crossref (recherche) | 10.5962/bhl.title.27468 | — |  |
| `freedman1975tail` | CONCORDE | crossref (doi) | 10.1214/aop/1176996452 | — |  |
| `gao2022` | CONCORDE | arxiv | 2210.10760 | PDF arXiv 2210.10760v1 sha256 c793c551a1b02740…, 28 p. |  |
| `gebelein1941` | CONCORDE | crossref (doi) | 10.1002/zamm.19410210604 | — |  |
| `greenblatt2023` | CONCORDE | arxiv | 2312.06942 | PDF arXiv 2312.06942v5 sha256 999f7a92bb8c0857…, 47 p. |  |
| `greenblatt2024` | CONCORDE | arxiv | 2412.14093 | PDF arXiv 2412.14093v2 sha256 f448dfe38f2144f0…, 137 p. |  |
| `griffin2024` | CONCORDE | arxiv | 2409.07985 | PDF arXiv 2409.07985v2 sha256 698f0db6e87bd786…, 30 p. |  |
| `gulcehre2023rest` | CONCORDE | arxiv | 2308.08998 | PDF arXiv 2308.08998v2 sha256 b22741558628b305…, 23 p. |  |
| `gupta2025` | CONCORDE | arxiv | 2506.14261 | PDF arXiv 2506.14261v4 sha256 4b0960622664e77d…, 24 p. | titre complet « RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? », Gupta et Jenner |
| `halberstadt2026` | CONCORDE | web |  | — |  |
| `hardt2016` | CONCORDE | arxiv | 1506.06980 | PDF arXiv 1506.06980v2 sha256 cacff05c501e1f6c…, 26 p. |  |
| `hirsch2006monotone` | CONCORDE | arxiv | 1712.09223 | PDF arXiv 1712.09223v1 sha256 c8a00d760e1c35c3…, 5 p. | chapitre 4, Handbook of Differential Equations: Ordinary Differential Equations, pp. 239–357, notice éditeur datée 2006 (DOI 10.1016/S1874-5725(05)80006-9) ; auteurs absents de la notice Crossref |
| `hirschfeld1935` | CONCORDE | crossref (recherche) | 10.1017/s0305004100013517 | — |  |
| `hoeffding1963probability` | CONCORDE | crossref (doi) | 10.1080/01621459.1963.10500830 | — |  |
| `hu2021lora` | CONCORDE | arxiv | 2106.09685 | PDF arXiv 2106.09685v2 sha256 e9a0d3128767db61…, 26 p. | contrôle d’auteur automatique trompé par un nom de deux lettres |
| `hubinger2024` | CONCORDE | arxiv | 2401.05566 | PDF arXiv 2401.05566v3 sha256 988e62785a475337…, 71 p. |  |
| `impossiblebench2025` | CONCORDE | arxiv | 2510.20270 | PDF arXiv 2510.20270v1 sha256 93803f181efdc01b…, 25 p. |  |
| `jacot2018` | CONCORDE | arxiv | 1806.07572 | PDF arXiv 1806.07572v4 sha256 e052eb972f646747…, 19 p. |  |
| `joagdev1983` | CONCORDE | crossref (doi) | 10.1214/aos/1176346079 | — |  |
| `kakade2001natural` | CONCORDE | arxiv | 2405.18221 | PDF arXiv 2405.18221v3 sha256 48784506f91ab2e2…, 36 p. | actes de NeurIPS 2001, page des actes (titre et auteur lus) |
| `kolmogorov1960` | CONCORDE | crossref (recherche) | 10.1137/1105018 | — |  |
| `korbak2022` | CONCORDE | arxiv | 2205.11275 | PDF arXiv 2205.11275v2 sha256 a277797a90238e47…, 9 p. |  |
| `korbak2025` | CONCORDE | arxiv | 2507.11473 | PDF arXiv 2507.11473v2 sha256 420d2c12a787b690…, 11 p. |  |
| `kwa2024` | CONCORDE | arxiv | 2407.14503 | PDF arXiv 2407.14503v2 sha256 3361adbe5dec7a9d…, 26 p. | titre complet « Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification », Kwa et Thomas |
| `lancaster1957` | CONCORDE | crossref (doi) | 10.1093/biomet/44.1-2.289 | — |  |
| `lasalle1976stability` | CONCORDE | crossref (doi) | 10.1137/1.9781611970432 | — | SIAM, 1976 (graphie « La Salle » dans la notice) |
| `lawley1943` | CONCORDE | crossref (recherche) | 10.1017/s0080454100006385 | — |  |
| `lecam1973convergence` | CONCORDE | crossref (recherche) | 10.1214/aos/1193342380 | — |  |
| `manheim2018` | CONCORDE | arxiv | 1803.04585 | PDF arXiv 1803.04585v4 sha256 7691af8a05ed8826…, 10 p. |  |
| `mei2020global` | CONCORDE | arxiv | 2005.06392 | PDF arXiv 2005.06392v3 sha256 5afa9725299089f7…, 65 p. |  |
| `needham2025` | CONCORDE | arxiv | 2505.23836 | PDF arXiv 2505.23836v3 sha256 964c793edab708ab…, 31 p. |  |
| `pearson1903` | CONCORDE | crossref (doi) | 10.1098/rsta.1903.0001 | — |  |
| `price1970` | CONCORDE | crossref (doi) | 10.1038/227520a0 | — |  |
| `renyi1959` | CONCORDE | crossref (recherche) | 10.1007/bf02024507 | — |  |
| `robertson1966` | CONCORDE | crossref (recherche) | 10.1017/s0003356100037752 | — |  |
| `schoolrewardhacks2025` | CONCORDE | arxiv | 2508.17511 | PDF arXiv 2508.17511v1 sha256 27b3c8dd20be4896…, 42 p. |  |
| `serfling1974probability` | CONCORDE | crossref (doi) | 10.1214/aos/1176342611 | — |  |
| `shao2024grpo` | CONCORDE | arxiv | 2402.03300 | PDF arXiv 2402.03300v3 sha256 6cc20b3c5b8d25b8…, 30 p. |  |
| `skaf2025` | CONCORDE | arxiv | 2506.01926 | PDF arXiv 2506.01926v2 sha256 d73dcd244fd2cc3d…, 28 p. |  |
| `skalse2022` | CONCORDE | arxiv | 2209.13085 | PDF arXiv 2209.13085v2 sha256 d9a8567f6d5bc9fa…, 23 p. |  |
| `smith1995monotone` | CONCORDE | crossref (recherche) | 10.1090/surv/041/01 | — | AMS, Mathematical Surveys and Monographs 41 ; la notice Crossref date la mise en ligne (2008) |
| `stein1981` | CONCORDE | crossref (doi) | 10.1214/aos/1176345632 | — |  |
| `tambe2011security` | CONCORDE | crossref (recherche) | 10.1017/cbo9780511973031 | — | livre, Cambridge University Press, notice éditeur |
| `terekhov2025` | CONCORDE | arxiv | 2506.05296 | PDF arXiv 2506.05296v3 sha256 28234a585a776b96…, 48 p. |  |
| `ukaisi2025` | CONCORDE | web |  | — |  |
| `wen2024` | CONCORDE | arxiv | 2411.17693 | PDF arXiv 2411.17693v1 sha256 13a93a48dcb37359…, 44 p. | titre « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats », Wen et al. (titre non revendiqué dans ma liste) |
| `yao1977probabilistic` | CONCORDE | crossref (recherche) | 10.1109/sfcs.1977.24 | — |  |
| `yu1997assouad` | CONCORDE | crossref (doi) | 10.1007/978-1-4612-1880-7_29 | — | chapitre du Festschrift for Lucien Le Cam, Springer 1997 (contrôle d’auteur automatique trompé par un nom de deux lettres) |
| `zelikman2022` | CONCORDE | arxiv | 2203.14465 | PDF arXiv 2203.14465v2 sha256 d22a472fce263175…, 30 p. |  |
| `zhuang2021` | CONCORDE | arxiv | 2102.03896 | PDF arXiv 2102.03896v1 sha256 37723b9165855628…, 14 p. |  |
