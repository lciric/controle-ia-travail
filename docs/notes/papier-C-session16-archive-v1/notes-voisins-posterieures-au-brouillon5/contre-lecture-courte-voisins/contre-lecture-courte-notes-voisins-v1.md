# Contre-lecture courte des quatre notes de voisins du brouillon 5 du papier C (règles R4 et R8) — v1

- **Qui** : contre-lecteur neuf, sous-agent de la session 16. Je n'ai écrit ni le brouillon 5, ni aucune note de voisins,
  contre-lecture ou traitement.
- **Heures** : 2026-10-21, de 00:27 à 00:40 UTC environ.
- **Consigne** : `…/papier-C/consigne-contre-lecture-courte-notes-voisins-v1.md`
  (`2ec99ec76a5fc0b0e376c6d3ac51c79e06a07e7d620d3643818b2760a0523356`, égale au compagnon), lue en entier.
- **Préfixe** : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5`
  (pour la consigne : son dossier parent `…/papier-C`) ; `R` = `/home/user/controle-ia-travail` (lecture seule).
  Mon dossier : `…/contre-lecture-courte-voisins/`.
- **Pages** : rang de la page dans le fichier PDF. Texte extrait par moi (`pdftotext -raw`, une page à la fois) sous
  `texte/<identifiant>/pNN.txt`, depuis les PDF déjà téléchargés, empreintes vérifiées.

## Pièces (empreintes vérifiées contre leur compagnon)

| pièce | empreinte | lecture |
|---|---|---|
| `…/voisins/lecture-voisins-joswin-huqu-v1.md` | `55222cdb3278f59810586b2097817114c74825cc34b9dd7a12ad2a051a90b84d` | en entier |
| `…/voisins-panin/lecture-voisins-panin-sept-v1.md` | `b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929` | en entier |
| `…/voisins-second-rang/lecture-voisins-second-rang-v1.md` | `8027bd53f6030d1b289c5ad84c3b501a8c646e22a72f31be6e30a2912a56f81f` | en entier |
| `…/voisins-cp02/lecture-voisins-cp02-v1.md` | `abbb5aaa8924b000d408cc606512afc78a083a8bd3d0a9151bf2c560f225cdac` | en entier |
| `R/docs/decisions/decision-N-005-N-006-v1.md` | `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0` | en entier |
| `R/docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` | en entier |
| `R/docs/decisions/decision-N-023-v1.md` | `1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d` | en entier |
| `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` | l. 60 à 80 (verrou 2, l. 67 à 75), l. 220 à 275 (énoncés et pièces revendiquées), l. 320 à 345, l. 420 à 442 |

Les quatre notes couvrent 2 + 7 + 9 + 5 = 23 papiers, plus le résumé de la version publiée de Kumaran et al.

## Ce que j'ai tenu

- Écriture seulement sous `…/contre-lecture-courte-voisins/`. Aucun réseau. Aucune commande git. Aucune recherche
  récursive. Aucun sous-agent, aucune dépense, aucune clé affichée. `python3 -I -B`, `PYTHONDONTWRITEBYTECODE=1`, scripts
  hors des dossiers de téléchargement, chemins passés en arguments.
- Jamais ouverts, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, tout fichier sous `R/donnees/`, `R/runs/`, `R/diag/`.
- **Écart déclaré, sans effet** : une commande qui écrivait un petit script de contrôle des ancres dans le bloc-notes de
  ma session, hors du dossier permis, a été refusée par la garde ; rien n'a été écrit. Le contrôle a été refait en
  lecture seule, sans fichier : chaque texte à remplacer cité par mes corrections figure une seule fois dans la note
  visée.
- Fichiers des autres sous-agents lus en plus des notes : trois pages de résumé et la page de l'éditeur (empreintes
  vérifiées contre les manifestes `sha256sums-voisins-second-rang-v1.txt` et `sha256sums-voisins-cp02-v1.txt`) ; une
  ligne du script `voisins-panin/outils/verifier_citations_panin_sept_v1.py` (l. 76) et de ses sorties (CV2-05).

## Tirage des trois papiers au hasard

- Script `tirage_trois_v1.py` (`856f41669a8e7f51ed48773ab0cbfad064756c0da1ac9eae870d76181ab53993`), sortie
  `tirage_trois_v1.sortie.txt` (`3cd56c80a96c82b842f9b511e3259202c2cd676ad708fccf5e5ced0230e39570`).
- Liste : les 20 identifiants restants hors 2507.03120, 2509.22830 et 2507.21509, sans numéro de version, triés comme
  chaînes ; Poonia et Jain sous l'identifiant de l'anthologie, `2025.findings-emnlp.1335` (rang 0 du tri).
- Méthode : `numpy.random.default_rng(numpy.random.SeedSequence(20261021)).choice(20, 3, replace=False)`, numpy 2.5.3.
- Indices tirés : 4, 15, 13 → **Wang Q. et al. 2504.09946v2**, **Robinson et al. 2602.21262v3**, **Barkett
  2601.17577v1**. Tous trois ont leur PDF : aucun n'est manquant.

## Sources relues sur PDF

| papier | fichier (sous `…/`) | empreinte (égale au compagnon et au manifeste de la note) | pages lues |
|---|---|---|---|
| Kumaran et al., préimpression 2507.03120v1 | `voisins-panin/pdf/2507.03120v1.pdf` | `5fa3b66737857f92fed9315adbdb4cbfb95e36d2366295c2a4f61a8448f0530c` | 1 à 21 en entier ; 24 à 27 ; 38 |
| Chang, Jun et Lee, ChatInject, 2509.22830v3 | `voisins-cp02/pdf/2509.22830v3/2509.22830v3.pdf` | `5663314dea6dbc4e91f801b5bb29b0564f45cdc87b54bc2c6f7f242442e4f76a` | 1 à 10 en entier ; 15 à 17, 19, 20 |
| Chen et al., 2507.21509v3 | `voisins-second-rang/pdf/2507.21509v3/2507.21509v3.pdf` | `2879ae0f9592d6b961ba13da7cfe43c6102774346b4fa60f22eb848e729c7b88` | 1 à 13 en entier ; 26, 31, 32, 60 à 62 ; mots clés sur le reste |
| Wang Q. et al., 2504.09946v2 | `voisins-second-rang/pdf/2504.09946v2/2504.09946v2.pdf` | `1d231bbea49dc80689e01aae8cc3a07a21f47111597370aa2b9d0aee5188d508` | 1 à 10 en entier ; 16 à 18 |
| Robinson et al., 2602.21262v3 | `voisins-panin/pdf/2602.21262v3.pdf` | `7bef1c8f2f34bd0af3cd78352abf30ed36ee4dbc2e0c91e09291bd39f1ed57a0` | 1 à 9 en entier ; 13 |
| Barkett, 2601.17577v1 | `voisins-panin/pdf/2601.17577v1.pdf` | `da8c454e7a6ae84ea8894f9f8110a515f9f57a076c9bf93c474e877c051789d7` | 1, 2, 5, 11 à 13, 17, 20, 31 |

## Verdict

**confirmé après corrections.**

Pour les six papiers relus, mon verdict est celui des notes : pas de collision avec les pièces revendiquées
(destination estimée librement ; nul de retour à la moyenne du corpus ; moniteur de contrôle sous attaque ; sonde de
l'agent auteur ; style de l'instructeur sans ordre). Dans aucun la destination n'est estimée : elle est imposée (option
conseillée, ordre de l'attaquant, réponse fausse injectée, note du partenaire). Aucun n'a de moniteur de contrôle dont on
lit le verdict sous attaque. Ce verdict ne vaut que pour ces six sources (R8) ; les 17 autres ne sont pas relues ici.
Mais le verrou 2 n'est pas levé : le corps publié de Kumaran et al., le voisin le plus proche, reste à lire (CV2-01,
majeur). Deux résumés portés sans PDF parlent de lecture interne, ce que la règle du verrou 2 vise en substance
(CV2-03). Le vocabulaire de R8 est tenu dans les quatre notes : partout « non trouvées dans les sources lues », jamais
« n'existe pas ».
Constats : 0 critique, 1 majeur, 3 mineurs, 1 de forme, 3 d'information.

| papier | ce que le papier mesure (moi) | verdict de la note | mon verdict |
|---|---|---|---|
| Kumaran 2507.03120v1 | choix binaire, conseil fictif d'exactitude annoncée de 50 % à 100 %, confiance lue par les logits, régressions, référence bayésienne ; direction imposée ; ni moniteur ni attaquant | pas de collision (préimpression) | pas de collision (préimpression) ; formes voisines non citées (CV2-02) ; version publiée à lire (CV2-01) |
| ChatInject 2509.22830v3 | ordres d'attaquant enveloppés dans les jetons de rôle du gabarit, dans la sortie d'un outil ; succès binaire d'agents ; détecteurs classifieurs, sans taux de détection | pas de collision ; précédent partiel du versant stylistique de HC3 | pas de collision ; d'accord sur le précédent partiel ; une comparaison mal attribuée (CV2-04) |
| Chen 2507.21509v3 | direction d'activation lue sur le modèle qui va répondre, suit le trait que la consigne induit ; juge GPT-4.1-mini non attaqué ; aucun moniteur, aucune attaque, aucun contrôle du style | pas de collision ; instrument voisin de HC2b | pas de collision ; d'accord |
| Wang Q. 2504.09946v2 | juges entre deux réponses ou dix options ; consensus et autorité forgés accolés à la mauvaise réponse, une intensité, sortie binaire | pas de collision | pas de collision ; d'accord |
| Robinson 2602.21262v3 | joueur de Sokoban conseillé par un modèle bienveillant ou malveillant ; issue binaire ; ni juge ni sonde | pas de collision | pas de collision ; d'accord |
| Barkett 2601.17577v1 | deux instances notent une critique de film de 0 à 1, puis voient la note du partenaire sous un statut donné ; taux binaire de déplacement vers la note du partenaire | pas de collision | pas de collision ; d'accord ; une virgule (CV2-05) |

## Citations refaites à la page (R5, R7)

- Script : `outils/verifier_citations_courte_v1.py`
  (`7f51efe30c886abe88d65160e5c664a07109287874ed2ff7290342515489f94f`). Pour chaque citation : empreinte du PDF égale à
  l'attendue ; citation présente, après normalisation des espaces et des guillemets, dans la note ; citation présente sur
  la page citée, texte extrait du PDF par le script lui-même. Aucun repli : un échec est écrit et le code de sortie vaut 1.
- Cas sain : `outils/citations_saines_v1.json` (`050125fb27268700c02895138df527033ba374898c3d2f7bf284903c7f43795d`) ;
  sortie `outils/verifier_citations_courte_v1.sortie.txt`
  (`3c8124efada4597f8b326e8f7bb4d07cd2175fc7d033f1b04c25f3311d1d1cc1`) : **70 citations, 1 échec** (Kumaran 12, ChatInject
  13, Chen 12, Wang Q. 14, Robinson 8, Barkett 11). L'échec est une virgule (CV2-05).
- Garde sur artefact : `outils/citations_artefact_v1.json`
  (`c17e2ecf4b4739282c62302d6309b1b42da251a324af37cf7d8552189aac4cef`) ; sortie
  `outils/verifier_citations_courte_v1.artefact.sortie.txt`
  (`b29f05b1cb58c478c27e2d58f08a9ca7d2872cc0a2b2f8c17be95b9c87025525`) : cas sain accepté ; chiffre altéré (2.58 en 2.85),
  bonne phrase à la mauvaise page, empreinte attendue altérée, phrase vraie mais absente de la note : quatre refusés, comme
  attendu.
- Résumés des papiers lus au seul résumé : `outils/extraire_resumes_courte_v1.py`
  (`c6cd2f950a84df59bda9da703ad44c007e9d652d59a027842313b3cf418c9600`), sortie
  `outils/extraire_resumes_courte_v1.sortie.txt` (`90cf82c317216ca1cc7b596a80e5a0072f892ecd96eb27d1af1513aaae89aabd`).

## Constats

Format : identifiant, gravité, où, ce qui est, ce qui devrait être, correction en mots exacts. Aucun constat ne change un
énoncé d'hypothèse ni une pièce revendiquée. Aucune collision, même partielle, n'est trouvée dans les six : aucun nœud
de Lazar n'est ouvert par cette lecture.

**CV2-01 — majeur — brouillon 5, verrou 2 (l. 67 à 75) ; note cp02, CQ-02 (l. 349 à 363) ; note Panin, CP-01 (l. 166 à
169) et CP-03 (l. 180).**
- Ce qui est : la version publiée de Kumaran et al. (Nature Machine Intelligence, 2026) est jugée « pas de collision au
  niveau du résumé » ; son corps, en accès libre et sans coût, n'est pas lu ; la note cp02 laisse la question ouverte
  (« Je ne tranche pas », l. 354). Or c'est le voisin le plus proche des 23. La préimpression, relue ici, régresse le
  changement d'avis sur des intensités graduées (exactitude annoncée, p. 8), lit la confiance par les logits (p. 4),
  régresse la confiance finale sur la confiance initiale (p. 18, p. 25) et compare la mise à jour à un profil bayésien
  selon la confiance initiale (p. 14, p. 15). Le résumé publié annonce en plus « Our computational modelling reveals that
  these two principles » (page de l'éditeur, `fa5dfe4a…`). La lettre de la règle du verrou 2 n'est pas déclenchée par ce
  résumé ; R8 (zone séduisante vérifiée plus durement) l'est.
- Ce qui devrait être : le corps publié est lu avant le scellement ; ce n'est plus une option laissée à la session.
- Correction, mots exacts : dans la phrase que CQ-02 propose pour remplacer celle de CP-01, remplacer « corps publié, en
  accès libre, non lu (R8). » par « corps publié, en accès libre, à lire avant le scellement (R8) : la préimpression du
  même travail régresse le changement d'avis sur l'exactitude annoncée du conseil, lit la confiance par les logits et
  régresse la confiance finale sur la confiance initiale (2507.03120v1, p. 4, p. 8, p. 14, p. 18 et p. 25) ; le résumé
  publié annonce une modélisation par le calcul. » ; dans le bloc de CP-03, remplacer « version publiée dans Nature
  Machine Intelligence, 2026, non lue » par « version publiée dans Nature Machine Intelligence, 2026, résumé lu, corps à
  lire avant le scellement ».

**CV2-02 — mineur — note Panin, CP-03 (l. 180), bloc « exactitude annoncée d'un conseiller fictif » ; contre-indices du
brouillon 5 (l. 325 à 344).**
- Ce qui est : la note cite la régression sur l'exactitude et le rapport à la mise à jour bayésienne. Elle ne cite pas
  les trois formes de Kumaran et al. les plus proches de la loi Δv = g · (ĉ − v₀) régressée sur v₀ : (i) une condition de
  base, « réponse cachée, conseil neutre », qui mesure la variance d'échantillonnage et la sensibilité au libellé (p. 3 :
  « The Answer Hidden - Neutral Advice condition can be considered a baseline condition » ; p. 8) ; (ii) la mise à jour
  absolue de la confiance tracée selon la confiance initiale et comparée au profil bayésien (p. 14, p. 15, figure 7) ;
  (iii) une régression bêta de la confiance finale sur la confiance initiale et sur l'exactitude signée du conseil, avec
  ordonnée à l'origine (p. 24 et p. 25, équation 2), où un point fixe est implicite, jamais estimé ni interprété.
- Ce qui devrait être : citées comme publiées, avec leurs limites (direction imposée, aucune destination estimée, aucun
  nul de moyenne du corpus, aucun moniteur). Elles ne prennent pas la pièce : ĉ n'y est ni libre ni testé.
- Correction, mots exacts : dans le bloc de CP-03, après « aucun moniteur de contrôle, aucun attaquant » (Kumaran et
  al.), insérer « ; condition « réponse cachée, conseil neutre » prise comme base (p. 3 et p. 8) ; mise à jour absolue de
  la confiance tracée selon la confiance initiale et comparée au profil bayésien (p. 14, p. 15, figure 7) ; confiance
  finale régressée sur la confiance initiale et l'exactitude signée du conseil, avec ordonnée à l'origine, en régression
  bêta (p. 24 et p. 25, équation 2) : un point fixe y est implicite, jamais estimé ni interprété ».

**CV2-03 — mineur — note second rang, l. 22 (« Trois ne la déclenchent pas »), verdicts l. 108 et l. 110 ; CS-01.**
- Ce qui est : trois verdicts reposent sur le seul résumé. Celui de Qu, Fu et Hu ne déclenche rien. Ceux de Wang K. et
  al. et de Poonia et Jain parlent de lecture interne sans dire « sonde » : « Through logit-lens analysis and causal
  activation patching » ; « models do not encode it internally » (Wang K. et al., `1dcd184f…`) ; « Using activation
  patching » ; « encode persona-specific information » (Poonia et Jain, `85de704a…`). La note lit la règle au sens strict
  de « sondes d'activations » sans l'écrire. Le risque de collision est faible : les deux lisent le modèle qui répond, pas
  un agent auteur, et aucun n'a de moniteur. Mais la règle vise ces lectures en substance, et CS-02 bâtit un
  contre-indice sur le résumé de Wang K. et al.
- Ce qui devrait être : les deux PDF sont lus avant le scellement, ou la session écrit qu'elle lit la règle au sens
  strict.
- Correction, mots exacts : l. 22, remplacer « Trois ne la déclenchent pas : Wang K. et al., Qu, Fu et Hu, Poonia et
  Jain. » par « Un ne la déclenche pas : Qu, Fu et Hu. Deux la déclenchent en substance, sans dire « sonde » : Wang K. et
  al. (« logit-lens analysis and causal activation patching » ; « models do not encode it internally ») et Poonia et Jain
  (« activation patching » ; « encode persona-specific information ») ; leurs PDF sont à lire avant le scellement (R8),
  sauf décision écrite de la session de lire la règle au sens strict. »

**CV2-04 — mineur — note cp02, CQ-03 (l. 375) et CQ-05 (l. 413 et 414).**
- Ce qui est : « les mêmes rôles écrits en texte brut n'apportent en moyenne qu'un gain modeste » ; « des rôles forgés
  en texte brut ajoutent peu en moyenne, les jetons natifs du gabarit beaucoup ». Dans ChatInject, la variante en texte
  brut (« Default Multi-turn ») ajoute un dialogue persuasif et des rôles en texte brut ; elle n'a pas le contenu de
  l'injection simple. Son « modest improvement » (13,8 % en moyenne, p. 5) mêle donc persuasion et format. La comparaison
  à contenu constant est 13,8 % (rôles en texte brut) contre 45,6 % (jetons natifs), même dialogue (p. 5). Aucune variante
  ne porte des rôles en texte brut autour du seul contenu de l'injection simple.
- Ce qui devrait être : la comparaison est attribuée à ce qu'elle compare.
- Correction, mots exacts : CQ-03, remplacer « les mêmes rôles écrits en texte brut n'apportent en moyenne qu'un gain
  modeste » par « à dialogue persuasif constant, des rôles écrits en texte brut (« role: content ») donnent un succès
  moyen de 13,8 %, contre 45,6 % avec les jetons natifs (p. 5 ; aucune variante n'isole les rôles en texte brut de la
  persuasion) » ; CQ-05, remplacer « des rôles forgés en texte brut ajoutent peu en moyenne, les jetons natifs du gabarit
  beaucoup » par « à dialogue persuasif constant, des rôles forgés en texte brut donnent un succès moyen de 13,8 % et les
  jetons natifs du gabarit 45,6 % ».

**CV2-05 — forme — note Panin, l. 143 (Barkett, p. 5).**
- Ce qui est : la note cite « as "senior expert and team leader" and the other as "junior trainee" ». La source porte
  « “junior trainee,” », virgule dans les guillemets. Le script de la note ne contrôlait qu'une forme tronquée, sans
  guillemet fermant (`voisins-panin/outils/verifier_citations_panin_sept_v1.py`, l. 76). Le sens ne change pas.
- Correction, mots exacts : remplacer « and the other as "junior trainee" » par « and the other as "junior trainee," ».

**CV2-06 — information — ChatInject, tableau 6 (p. 17), cité par CQ-03, CQ-04 et CQ-05.**
- Les succès sous gabarits rendus par homoglyphes valent exactement ceux de l'injection simple pour deux modèles sur
  trois (Qwen-3 : 17,5 ; GPT-oss : 0,3 ; tableau 1, p. 5), en décodage glouton (p. 19). C'est plausible (gabarit
  ignoré), ou c'est une colonne recopiée. « Presque aucun » se cite en qualitatif, avec cette réserve (R4) ; aucun chiffre
  dans une puissance ni un seuil.

**CV2-07 — information — R8 dans les quatre notes.**
- Chaque verdict est borné aux sources lues (« les pièces revendiquées ne sont pas trouvées dans les sources lues ») ;
  les titres non lus sont « une question, pas une occupation ». Aucun « n'existe pas ». Les phrases « La porte GC n'est
  pas déclenchée » sont des lectures proposées : la session les confirme.
- Hors des cas de CV2-01 et CV2-03, aucun « pas de collision » ne repose sur le seul résumé là où la règle demandait le
  PDF : les six relus ici l'ont été sur PDF, comme les notes le disent.

**CV2-08 — information — borne de cette contre-lecture.**
- Elle porte sur six papiers sur 23 (trois nommés, trois tirés). Elle confirme leurs verdicts et les citations refaites
  (70, une virgule). Elle ne dit rien des 17 autres au-delà du vocabulaire R8 et des niveaux de lecture déclarés.
