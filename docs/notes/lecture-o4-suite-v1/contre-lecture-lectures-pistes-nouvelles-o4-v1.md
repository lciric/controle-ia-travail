# Contre-lecture d'ensemble des lectures de pistes nouvelles contre O4 (juge au nul formé des lois connues) — v1

- **Contre-lecteur : modèle J**, d'un autre modèle que les lecteurs (modèle I) ; J ≠ I. Une seule contre-lecture pour les sept lectures (consigne de proportion de la session mère du 18 novembre). Le contre-lecteur n'a écrit aucune des lectures, ni N-064, ni N-067, ni les notes d'englobement et de priorité haute.
- **Heures (`date -u`, recopiées des commandes)** : début 2026-11-18T03:45:09Z ; rejeu des sept lectures et comparaison aux sorties des lecteurs 2026-11-18T03:49:31Z ; rejeu final de mes deux listes 2026-11-18T03:50:20Z ; écriture de cette note 2026-11-18T03:51:45Z.
- **Règles** : R7 (rien sans PDF empreinté et page, ou fichier de code au commit relevé et lignes), R8 (*non trouvé* = non trouvé dans ce qui est lu, à la profondeur dite), R4 (doute tranché contre notre revendication), N-067 : **rien n'est déclaré libre** ; verdict en vigueur sur O4 : **occupée en partie** ; tout écart est un nœud pour Lazar. Pages = pages du PDF (1 = première page du fichier). Guillemets français : citations rejouées de mes deux listes ; les renvois [Exx] sont les extraits des lecteurs, [Jxx] les miens.
- **Aucune dépense, aucun accès réseau, aucun programme des clones lancé, aucun fichier des lecteurs modifié.** Aucun refus de permission, de crochet ou de classifieur.

## 0. Verdict d'ensemble

Les sept lectures **tiennent** ; quatre avec réserves. Aucun constat bloquant. Aucun statut déclaré par un lecteur n'est trouvé trop favorable à notre revendication ; deux manques vont dans le sens **non flatteur** (AA-1, LLBSTACK-1) et un constat transversal (T-1) demande que la synthèse ne dise plus (ii) *non trouvé* sans qualification. La conjonction (i)+(ii)+(iii)+(iv-a)+(iv-b) n'est trouvée dans aucune des sept pièces, à la profondeur relue ; ce constat ne dit rien du champ (R8) et ne change pas le verdict **occupée en partie**.

| pièce | verdict de la contre-lecture | constats |
|---|---|---|
| AA | **tient avec réserves** | AA-1 majeur, AA-2 mineur, AA-3 mineur, AA-4 mineur |
| LLB | **tient avec réserves** | LLB-1 mineur |
| LLBSTACK | **tient avec réserves** | LLBSTACK-1 majeur, LLBSTACK-2 mineur |
| AUTODISC | **tient** | AUTODISC-1 mineur |
| MANNING | **tient** | aucun |
| CHENDIM | **tient avec réserves** | CHENDIM-1 majeur (outil de rejeu, non la lecture), CHENDIM-2 mineur |
| CLZ | **tient** | aucun |
| ensemble | — | T-1 majeur, T-2 mineur, T-3 mineur |

## 1. Fichiers lus et profondeur de la contre-lecture

- **Contexte** : `lecture-o4-englobement-v3.md` l. 19-77 ; `lecture-pdf-code-priorite-haute-o4-v3.md` sections 4 et 7.
- **Lectures** : les sept notes `lecture-piste-nouvelle-<id>-o4-v1.md` (aa, llb, llbstack, autodisc, manning, chendim, clz). AA, LLB et LLBSTACK lues en entier ; AUTODISC, MANNING, CHENDIM et CLZ : en-tête, verdict, section 3 (composantes), table, nœuds, incidents ; leurs sections de recherche de termes et de *reste non lu* lues en partie. Les listes de citations et d'extraits des lecteurs sont rejouées, non relues entrée par entrée.
- **Sources rouvertes** : texte extrait par `pdftotext` des six PDF (empreintes recalculées, toutes égales à celles des lectures : `7c0eee05…`, `a8620e7c…`, `30210132…`, `c44f50f3…`, `d338d13e…`, `e8f061ef…`), **par recherche de termes ciblée et lecture des passages décisifs**, non relus en entier. Clone AssayingAnomalies au commit `f08a77f7f98bfec8de893effb8bd4f5524dbbb48` (vérifié par `git rev-parse HEAD`) : `makeCloseAnomResults.m` l. 40-129, `runTestSignal.m` l. 50-129, `makeResToPrint.m` l. 414-446, `makeCombStrats.m` l. 60-112, `prt/printCloseAnomsSection.m` l. 36-127, `prt/printCombStratsSection.m` l. 36-76, `prt/printReturnPredictionSection.m` l. 100-125, `makeAnomBenchmarkResults.m` l. 58-72, `Functions/Utilities/calcPanelCorrels.m` (lignes de code), et une recherche de seuils dans `Functions/Assay functions`. Clone autodiscovery au commit `66aa2d513cafdb23bf38313ebef522ade93f8cd9` : occurrences de `nodes_by_level` dans `src/` et définitions de fonctions de `run.py` seulement.
- **Consigne tronquée** : le texte de la consigne reçu s'arrête au milieu du statut (iii) de CHENDIM ; les statuts de CHENDIM et de CLZ ont été pris dans les notes elles-mêmes. Sans effet.
- **Priorité 3 sans objet** : aucune des sept pièces n'a été arrêtée *sans rapport* ; toutes ont été lues en entier par leur lecteur (AA : code seul).

## 2. Rejeux

Programmes inchangés. Rejeu des listes des lecteurs (sorties `contre-lecture-lectures-pistes-nouvelles-o4-v1-rejeu-<id>-citations-pdf.json` et `…-rejeu-<id>-extraits-code.json`), chacune **identique octet pour octet** à la sortie versée par le lecteur (`cmp`) :

| pièce | citations PDF | extraits de code |
|---|---|---|
| AA | 0 sur 0 (liste vide : code seul) | 53 sur 53 |
| LLB | 42 sur 42 | 0 sur 0 (liste vide) |
| LLBSTACK | 43 sur 43 | 0 sur 0 (liste vide) |
| AUTODISC | 46 sur 46 | 43 sur 43 |
| MANNING | 53 sur 53 | 0 sur 0 (liste vide) |
| CHENDIM | 66 sur 66 | 0 sur 0 (liste vide) |
| CLZ | 61 sur 61 | 0 sur 0 (liste vide) |

Mes citations neuves : **5 sur 5** (`…-o4-v1-citations-pdf.json`, sortie `…-resultat-citations-pdf.json`) ; mes extraits neufs : **6 sur 6** (`…-o4-v1-extraits-code.json`, sortie `…-resultat-extraits-code.json`), codes de sortie 0.

## 3. Constats par pièce

### AA — tient avec réserves

Vérifié sur le code : la forme exacte du test *Close Span* est celle que dit le lecteur — moindres carrés du rendement long-court du signal sur une constante, les rendements des six anomalies les plus proches et six facteurs (`makeCloseAnomResults.m` l. 121-122, [E24]) ; choix des six sur la période même du test (l. 71-88) ; la comparaison au zoo entier mis en commun n'est qu'une série de rendements sans puis avec le signal, sans statistique (`makeResToPrint.m` l. 424-438, « yWith(:, i) = res2.pret(:,end); ttl(i) = cellstr(combStrats(i).label); » [J05] ; `printCombStratsSection.m` l. 36-75 : croissance d'un dollar seulement). Le statut **(ii) pris sous forme fréquentiste, en échantillon** n'est ni trop fort ni trop faible, sous la précision de AA-4. Les absences (iii) et (iv-a) sont confirmées dans les fichiers rouverts.

- **AA-1 — majeur (manque, sens non flatteur).** La lecture ne décrit sous (ii) que la régression d'enjambement. Le même protocole fait un **second test contre le connu** : une régression de Fama et MacBeth des rendements des titres sur le signal **et les six signaux proches ensemble**, dont le rapport imprime le t du signal : « resCloseFMB(nCloseAnoms+1, 1) = runFamaMacBeth(ret, [testSignal fmbX], dates, 'timePeriod', timePeriod, ... 'printResults', 0); » [J01] et « 'controlling for ', minIndTStatLabel, '. Controlling ', ... 'for all ', nCloseAnomsChar, ' closely related anomalies, the t-statistic on ', signalChar, ... ' is ', allTstat, '.' '\\n\\n\\n']; » [J02]. C'est une régression prédictive en coupe, ajustée, où le signal nouveau doit garder un coefficient à côté des prédicteurs connus : elle porte sur la **prédiction du rendement des titres** et non sur des séries de portefeuilles. La première des trois différences que la lecture garde à notre (ii) (*lois prédictives et non rendements de portefeuilles*, section 3 (ii-a) et question 5) en est **affaiblie**. *Correction proposée* : ajouter ce test à (ii-a) et à la table ; ne plus présenter *lois prédictives et non rendements* comme une différence nette ; faire lire `runFamaMacBeth.m` (non lu par le lecteur ni par moi : erreurs types et forme exacte non établies).
- **AA-2 — mineur.** « Le seul 1,96 du code MATLAB hors tiers » est exact à la lettre, mais le même fichier compte aussi des t d'alphas au-dessus de 2 et de 3 : « numTAlphaGT2 = num2words(sum(sum(talphas>2))); numTAlphaGT3 = num2words(sum(sum(talphas>3))); » [J03]. Aucun de ces seuils ne décide ni ne porte sur l'enjambement : statut (iii) inchangé. *Correction* : écrire *seuils 1,96, 2 et 3 employés pour compter dans le texte imprimé, aucun pour juger*.
- **AA-3 — mineur.** La lecture dit la corrélation des signaux *en coupe* ; le code empile tout le panel titres-mois avant de corréler : « reshapedVars = [reshape(var1, n, 1) reshape(var2, n, 1)]; » [J06]. La conclusion *corrélation de rangs* tient : la matrice a deux colonnes (« resCorrels = nan(nAnoms,2); » [J04]) et l'affectation d'une sortie unique à une ligne de deux colonnes y met la même valeur deux fois (sémantique du langage, non exécutée). *Correction* : *corrélation de rangs sur le panel empilé*.
- **AA-4 — mineur (libellé).** *Pris sous forme fréquentiste* doit rester lié à sa restriction dans toute reprise : six proches choisis sur l'échantillon du test, six facteurs, rendements, sans seuil dans la boîte à outils (le seuil 1,96 est celui de NMV, [P04]). *Correction* : dans la synthèse, écrire *pris sous forme fréquentiste restreinte (six proches et six facteurs, en échantillon)* ; voir T-1 pour la cohérence avec SEADS et CLZ.

### LLB — tient avec réserves

Vérifié sur le texte : aucune occurrence de `expert` (hors introduction et travaux voisins, p. 1, 10, 11, 13), `known model`, `held-out`, `stacking`, `model selection` (hors titre de la référence [32], p. 13) qui ferait d'une loi connue un étalon ou un nul ; la seule comparaison est la moyenne *plate* des mêmes propositions (p. 3, 5-7, 15-44). Les statuts (ii) *voisin proche pour l'opérateur*, (iii) *non trouvé*, (iv-a) *voisin lointain* tiennent. La remarque du nœud 3 (rapport de vraisemblances marginales et e-valeur) est bien dite non opposable.

- **LLB-1 — mineur.** « Le connu est même écarté à dessein » est trop large : ce qui est écarté, ce sont les problèmes et données connus **dans l'évaluation** (p. 5). Des modèles écrits à la main entrent chez le proposeur comme exemples : « For in-context learning, we provided the LLM with six examples of ostensible user inputs, along with high quality outputs (Sec. G). » (p. 4). Ils n'entrent pas dans la mise en commun ni dans le jugement : statuts inchangés. *Correction* : *connu écarté de l'évaluation ; six modèles d'exemple donnés au proposeur*.

### LLBSTACK — tient avec réserves

Vérifié sur le texte : mise en commun = prédicteur final, aucune règle de décision, aucun test ; (ii) *voisin proche, forme prise* tient et est dit assez fort.

- **LLBSTACK-1 — majeur (prudence d'énoncé, sens non flatteur).** P *voisin (lointain)* est peut-être trop faible. La pièce dit elle-même que la pondération par l'évidence opère comme une **sélection** entre propositions : « Bayesian model averaging can behave more like model selection than model combination, concentrating its mass on a small subset of candidate models » (p. 1) ; « the posterior over models effectively collapses to a single candidate » (p. 5) ; et que l'empilement donne la masse selon la structure prédictive complémentaire (la moyenne bayésienne peut « fail to exploit complementary predictive structure », p. 3). Remarque du contre-lecteur, **non opposable** (R7, raisonnement et non texte de la pièce) : dans un empilement, un candidat ne garde un poids que s'il améliore le score prédictif de la mise en commun ajustée des autres — c'est la comparaison que fait notre juge, sans règle de décision ni garantie. *Correction proposée* : P *voisin* (sans *lointain*) ; et, dans tout énoncé public, ne pas écrire que personne ne mesure l'apport d'une proposition de modèle de langue au-delà d'une mise en commun ajustée : ce qui n'est pas trouvé ici est le **nul désigné, l'archive, la règle de promotion et sa garantie**. Nœud pour Lazar.
- **LLBSTACK-2 — mineur.** La piste Li, Fox et Goodman 2024 (arXiv 2402.17879), nommée par le lecteur (nœud 3), est citée par la pièce comme découverte automatique de modèles statistiques par modèles de langue ; d'après son seul titre elle peut toucher P et (i) ensemble. *Correction* : la porter en **priorité haute** parmi les pièces à verser, avec Yao et al. 2018 (outil d'empilement). Code de la pièce non cloné : (iv-b) reste *non établi*, comme dit.

### AUTODISC — tient

Vérifié : le défaut dit de la branche des croyances en ligne (`nodes_by_level` employé dans `compute_and_store_reward`, `run.py` l. 56-59, alors que ce nom n'est que paramètre d'autres fonctions, l. 21 et 169-171, et variable locale de `main`, l. 414-453) est conforme à ma lecture, non exécutée. POPPER n'entre pas dans la méthode : « However, these systems are mainly goal-driven, performing start-to-finish experimentation given a clear research goal, rather than iterative, open-ended, goal-free exploration (our context). » (p. 9). Absences (ii), (iii), (iv-a) confirmées par recherche (`literature`, `retriev`, `falsif`, `significance level`).

- **AUTODISC-1 — mineur.** P *pris sous forme subjective* est le choix non flatteur et se défend ; il doit toujours être dit avec sa limite, que la lecture donne : ce qui est mesuré contre le connu est le **résultat de l'expérience**, dans les deux sens, y compris quand l'hypothèse proposée échoue ; ce n'est pas *la proposition bat le connu*. *Correction* : aucune sur le statut ; garder la limite dans la table de synthèse, non seulement dans le corps.

### MANNING — tient

Vérifié sur les p. 1, 2, 4, 18 : hypothèses jugées contre aucun effet ; le connu (théorie des enchères, prédiction directe du modèle de langue) n'est qu'étalon de la méthode. Statuts ni trop forts ni trop faibles. Aucun constat.

### CHENDIM — tient avec réserves

Vérifié : aucune régression ni test d'apport des stratégies fouillées sur les stratégies publiées (recherche de `regress`, `correlat`, `spann`, `increment`, `beyond` : seulement p. 10, 13, 15, 17, sans rapport) ; paraphrases des p. 33, 36 et 43 conformes à l'extraction page à page.

- **CHENDIM-1 — majeur (outil de rejeu ; la lecture est correcte).** Le défaut dit par le lecteur est **confirmé** : ce PDF a 44 pages et se découpe en 49 segments ; les pages 28, 38, 39 et 40 contiennent chacune un saut de page de trop. Le programme de rejeu gelé numérote donc mal les pages au-delà de la 27. J'ai contrôlé les cinq autres PDF de ce lot : segments = pages + 1, aucune page à sauts multiples ; **leurs numéros de page ne sont pas touchés**. Conséquence : les éléments des p. 28-44 de CHENDIM sont des paraphrases non rejouées par programme (R7 plus faible, dit par le lecteur). *Correction proposée* : programme de rejeu sous un nom neuf (R12), numérotant par extraction page à page ; contrôle des rejeux déjà versés sur des PDF à figures (nœud 3 du lecteur, que j'appuie).
- **CHENDIM-2 — mineur.** *Rétrécissement vers zéro* : le texte cité ne le dit que pour le cas sans prévisibilité (p. 13) ; en général le rétrécissement va vers la loi latente ajustée de la famille (p. 8, 10, citées par le lecteur). *Correction* : *rétrécissement vers la loi latente de la famille, soit zéro quand il n'y a pas de prévisibilité*. Statut inchangé.

### CLZ — tient

Vérifié sur la section 3 et les citations rejouées : aucune composante prise ; l'annexe B.4 est un critère de tri par R², sans test du résidu — plus faible que le test d'alpha de AA, ce qui rend cohérents *voisin proche par la forme* (CLZ) et *pris sous forme fréquentiste restreinte* (AA). Aucun constat.

## 4. Constats d'ensemble

- **T-1 — majeur (synthèse ; nœud pour Lazar).** Après ces lectures, (ii) ne peut plus être dit *non trouvé* ni *voisin* sans qualification : (a) le nul *combinaison linéaire ajustée de stratégies connues de l'archive*, avec test, est publié hors modèle de langue (AA, 2023 ; appliqué par NMV à des signaux minés ; SEADS le porte sous forme de régression pour des propositions de modèle de langue, selon la note d'englobement) ; (b) la **forme** *mise en commun ajustée de lois prédictives proposées par un modèle de langue* est publiée (LLB, LLBSTACK), comme prédicteur et non comme nul. Ce qui reste non trouvé, dans les pièces lues et à la profondeur dite, est la **réunion** : lois prédictives de l'archive entière et croissante, mises en commun et ajustées avant le gel, employées comme nul d'une règle de promotion à garantie toujours valide, sur prédictions scellées. Les échelles de statut doivent être harmonisées entre notes (*pris sous forme…* pour AA, *sous forme de régression* pour SEADS, *voisin proche par la forme* pour CLZ). Rien n'est déclaré libre.
- **T-2 — mineur.** (iv-b) sans agents est libellé de quatre façons (*voisin* pour AA et CLZ, *voisin, au sens trivial* pour CHENDIM, *sans objet* pour ATLAS dans la note de priorité haute). *Correction* : une règle unique dans la table de synthèse (nœud 4 de CHENDIM).
- **T-3 — mineur.** Pistes nommées par les pièces et non lues, à ne pas perdre : pour (iii) et (iv-a), Marrow et Nagel 2024 (nommée par CHENDIM et par CLZ) ; pour (ii), Chen et Zimmermann 2020, Jensen, Kelly et Pedersen (nommés par CHENDIM et, pour le dendrogramme, par le code de AA, `runTestSignal.m` l. 85), Yao et al. 2018 ; pour P et (i), Li, Fox et Goodman 2024, le dépôt et la page des changements postérieurs d'AUTODISC ; l'article *Assaying Anomalies* lui-même, refusé. Tant qu'elles ne sont pas lues, la clause d'usage public de N-067 n'est pas satisfaite.

## 5. Ce que je n'ai pas pu vérifier

- **Aucun PDF n'est relu en entier** : vérification par termes et passages décisifs. Une occurrence décisive hors des termes cherchés m'échapperait comme aux lecteurs.
- **AA** : l'article (refusé) ; `runFamaMacBeth.m`, `makeFMBRes.m`, les méthodes de combinaison autres que les trois premières ; la préversion employée par NMV ; rien n'est exécuté.
- **AUTODISC** : le code hors des occurrences dites ; les statuts (iv-b) et (iii) du code sont pris sur les extraits rejoués du lecteur.
- **LLBSTACK** : code non cloné. **LLB** : code non publié selon la pièce. **MANNING, CHENDIM, CLZ** : code non lu.
- **CHENDIM** : p. 28-44 contrôlées sur trois pages seulement (33, 36, 43).
- Les références des pièces : aucune lue ; toute phrase sur leur contenu est celle de la pièce qui les cite.
- Les listes des lecteurs sont rejouées (présence à la page ou aux lignes dites), non jugées entrée par entrée pour leur sens.
