# Second vérificateur des références du papier D — v1

24 novembre 2026. Notices lues à la source (curl, agent générique) : arXiv, Crossref, OpenAlex, zbMATH, actes de NeurIPS, page de Rivest au MIT, Internet Archive. Comparées à la clé, au registre et à nos textes : `main-v4-correctif-1.tex`, `papiers/D/theorie/*.tex` et `brouillon-fable-*/*.tex` (bibliographie en commentaire). Le découplage et la dynamique n'ont que des `\cite`.

## Une ligne par référence

| Clé | Consulté | Verdict | Correction exacte |
|---|---|---|---|
| gupta2025 | arXiv 2506.14261 | confirmé | Gupta, Jenner, « RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors? », 2025 ; la mention « à confirmer » de `decouplage-geometrique-v3-references.md` peut tomber |
| kwa2024 | arXiv 2407.14503 | confirmé | trois auteurs : Kwa, Thomas, Garriga-Alonso (le registre n'en nomme que deux) ; clé citée dans aucun des textes contrôlés |
| boucheron2013concentration | Crossref | confirmé | aucune ; « Theorem 2.10, to be checked » reste ouvert (lecture sur PDF) |
| tambe2011security | Crossref | confirmé | aucune (Cambridge University Press, 2011) |
| smith1995monotone | Crossref, OpenAlex, zbMATH | confirmé, identifiant à corriger | le registre donne 10.1090/surv/041/01, qui est le DOI du chapitre 1 ; celui du livre est 10.1090/surv/041. zbMATH confirme Hal L. Smith, Mathematical Surveys and Monographs 41, AMS, 1995, x+174 p. |
| yu1997assouad | Crossref, zbMATH | confirmé | aucune (Festschrift for Lucien Le Cam, Springer 1997, pp. 423–435) |
| avenhaus2002inspection | Crossref | confirmé | aucune (chapitre 51, vol. 3, pp. 1947–1987, 2002) |
| lasalle1976stability | Crossref, OpenAlex, zbMATH | confirmé | série CBMS-NSF 25 confirmée (zbMATH) ; graphie « LaSalle » |
| hu2021lora | arXiv 2106.09685 | confirmé | aucune ; clé citée dans aucun des textes contrôlés |
| hirsch2006monotone | Crossref, OpenAlex, zbMATH | à corriger (registre), année non confirmée | Le registre porte arXiv 1712.09223 et son PDF, qui sont d'un autre article (Lemmens et al., 2017) : remplacer par le DOI 10.1016/S1874-5725(05)80006-9, sans PDF. Auteurs (OpenAlex, zbMATH) : M. W. Hirsch, H. L. Smith. Année : 2006 pour Crossref et OpenAlex, 2005 pour zbMATH (vol. II, ISBN 0-444-52027-9). La correction 2 du registre (« année 2006 ») n'est donc pas établie. |
| kakade2001natural | page des actes de NeurIPS 2001 | confirmé ; registre à corriger | Titre et auteur unique (Sham M. Kakade) lus sur les actes. Mais le registre porte arXiv 2405.18221 et son PDF : Cayci et Eryilmaz, « Recurrent Natural Policy Gradient for POMDPs », un autre article (voir correction 1). |
| wen2024 | arXiv 2411.17693 | confirmé | Le texte cite la clé `wen2024adaptive`, qui ne correspond pas à la clé du registre, avec le bon titre. |
| rivest2006 | page de publications de Rivest au MIT, notice bib, PDF | confirmé ; source trouvée | La bonne source est [Riv06d] : R. L. Rivest, « On Estimating the Size of a Statistical Audit », brouillon non publié du 14 novembre 2006, `https://people.csail.mit.edu/rivest/pubs/Riv06d.pdf` (20 p., sha256 b883153080a3821363083fee8511e6e0a6a971f1b30fc8c6a19025bf0359acf1, copie hors du dépôt). La première vérification a essayé Riv06c, qui est « ThreeBallot ». Rivest le dit remplacé par Aslam, Popa, Rivest, « On Estimating the Size and Confidence of a Statistical Audit », EVT'07 : citer le manuscrit et cette version publiée. Clé citée dans aucun des textes contrôlés. |
| dresher1962sampling | OpenAlex W266047537 ; Internet Archive DTIC_AD0278470 (notice et texte reconnu du scan) | confirmé | M. Dresher, « A Sampling Inspection Problem in Arms Control Agreements: A Game-Theoretic Analysis », RAND Memorandum RM-2972-ARPA, février 1962, préparé pour l'Advanced Research Projects Agency (DTIC AD0278470). Le texte cité est exact. La préface (nombre fixe d'inspections sur une suite d'événements) est cohérente avec « sequential game ». Pannes : rand.org, apps.dtic.mil, HathiTrust 403 ; openlibrary coupé ; Google Books, Semantic Scholar, Bibliothèque du Congrès 429. |
| bartok2014 | Crossref 10.1287/moor.2014.0663 ; arXiv 1102.2041 | à corriger (texte) | La correction du registre est exacte : MOR 39(4):967–997, 2014, cinq auteurs dans l'ordre Bartók, Foster, Pál, Rakhlin, Szepesvári. Mais `main-v4-correctif-1.tex`, ligne 366, porte encore « arXiv:1102.2041, 2014 ». Il faut écrire « Mathematics of Operations Research 39(4):967--997, 2014, doi:10.1287/moor.2014.0663 ». |
| blocki2013audit (échantillon) | arXiv 1303.0356 | confirmé | Les auteurs et leur ordre sont confirmés. Le lieu IJCAI 2013, donné en commentaire dans le texte, n'a pas pu être lu (page des actes sans résultat, DBLP 202). |
| cloud2024 (échantillon) | arXiv 2410.04332 | confirmé | aucune |
| greenblatt2024 (échantillon) | arXiv 2412.14093 | confirmé | L'entrée du manuscrit (« R. Greenblatt et al. ») est exacte. |
| jacot2018 (échantillon) | arXiv 1806.07572 (référence de revue : NeurIPS 2018) | confirmé | aucune |
| lawley1943 (échantillon) | Crossref, zbMATH | confirmé | Crossref donne 1944, zbMATH 1943 (Proc. R. Soc. Edinburgh A 62:28–30). Garder 1943, avec une note au registre. |
| skaf2025 (échantillon) | arXiv 2506.01926 | confirmé | aucune ; clé citée dans aucun des textes contrôlés |
| stein1981 (échantillon) | Crossref | confirmé | Ann. Statist. 9(6):1135–1151 |
| yao1977probabilistic (échantillon) | Crossref | confirmé | aucune (FOCS 1977, pp. 222–227) |

Contrôle annexe : le DOI de Le Cam de `references-a-verifier-v1.json` (10.1214/aos/1176342351) renvoie 404 ; le registre porte le bon (10.1214/aos/1193342380).

## Verdicts « CONCORDE » à revoir

- `kakade2001natural` et `hirsch2006monotone` : le fond concorde, mais source, identifiant et PDF désignent un autre article, empreinté ; ces lignes sont fausses en l'état (R6).
- `hirsch2006monotone` : l'année n'est pas établie (2005 ou 2006).
- Aucun verdict de fond « CONCORDE » ne s'est révélé être un écart de titre ou d'auteur.

## Liste fermée des corrections

1. Registre, `kakade2001natural` : source = page des actes (`papers.nips.cc/paper_files/paper/2001/hash/4b86abe48d358ecf194c56c69108433e-Abstract.html`), identifiant = cette adresse, PDF = « — ».
2. Registre, `hirsch2006monotone` : source = Crossref (DOI), identifiant = 10.1016/S1874-5725(05)80006-9, PDF = « — », auteurs Hirsch et Smith (OpenAlex, zbMATH). La correction 2 devient : « année 2005 ou 2006 selon la base ; à trancher sur la page de titre ».
3. Registre, `smith1995monotone` : identifiant = 10.1090/surv/041 (livre) ; année 1995 confirmée par zbMATH.
4. Registre, `rivest2006` : NON_CONFIRMEE devient CONCORDE (source web, Riv06d, empreinte ci-dessus). La correction 3 devient : « citer comme manuscrit non publié du 14 novembre 2006, avec la version publiée Aslam, Popa, Rivest, EVT'07 ».
5. Registre, `dresher1962sampling` : PDF_NON_ACCESSIBLE devient CONCORDE (OpenAlex et Internet Archive, DTIC AD0278470). Le numéro RM-2972-ARPA est confirmé. La correction 4 devient : « confirmée ; rand.org en panne d'accès ».
6. Registre, `kwa2024` : note « Kwa, Thomas, Garriga-Alonso ».
7. Registre, bilan : quinze verdicts manuels, et non quatorze. Une fois les points 4 et 5 appliqués, le bilan devient : concordantes 66, corrigée 1.
8. Registre, couverture : douze clés citées par nos textes manquent au registre : `christiano2021lowstakes`, `deng2019strategizing`, `rakhsha2020poisoning`, `zhang2008policyteaching` (budget d'audit, correctif 1) ; `anthony2017`, `cohen1983`, `hofbauer2002`, `hopfield1984`, `leonardos2022`, `wainwright2008`, `wilson1972` (dynamique, correctif 1) ; `testingthewaters2026` (manuscrit). Trois clés du budget d'audit (`greenblatt2023control`, `griffin2024games`, `wen2024adaptive`) n'ont pas le nom de leur entrée au registre (`greenblatt2023`, `griffin2024`, `wen2024`) : il faut harmoniser l'un ou l'autre.
9. Texte, `main-v4-correctif-1.tex`, ligne 366 : remplacer « arXiv:1102.2041, 2014. » par « Mathematics of Operations Research 39(4):967--997, 2014, doi:10.1287/moor.2014.0663. ».
10. Texte, `decouplage-geometrique-v3-references.md` : `gupta2025` devient « titre et auteurs vérifiés sur arXiv 2506.14261 (Gupta, Jenner) ».
11. Note `brouillon-fable-dynamique-v1/note-to-orchestrator-v1.md`, `hirsch2006monotone` : pp. 239–357 confirmées, année à trancher (voir point 2).

## Verdict

Le registre est juste sur le fond des 23 références contrôlées, mais il n'est pas opposable en l'état. Deux lignes rattachent un PDF étranger, deux références réputées introuvables sont en fait confirmées, une année est incertaine, et douze clés citées manquent.
