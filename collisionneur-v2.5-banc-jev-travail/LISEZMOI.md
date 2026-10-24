# Collisionneur v2.5 et banc de calibration de Jev : état du chantier au 24 octobre 2026

Branche orpheline `outils/collisionneur-v2.5-banc-jev-travail` du dépôt de travail. Elle porte l'outil personnel de Lazar, hors du programme, pour que la session qui reprend le chantier puisse continuer : le collisionneur 3×3 v2.5 et le banc de calibration de Jev en cours.
- Rien de cette branche n'entre dans `main`.
- Aucun de ces fichiers ne s'exécute contre une API sans que Lazar le lance lui-même, avec ses clés, sur sa machine.

## Empreintes

| Fichier | sha256 | État |
|---|---|---|
| `collisionneur_v2.py` | `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` | v2.5, livré à Lazar le 22 octobre ; inchangé |
| `test_collisionneur_v2.py` | `26b5e41715f6a2e09e17a672d033c439ed18cd6a0572d4d4a4b8cd3031a2ae49` | 58 tests, sans réseau |
| `banc_jev.py` | `3dff585333db4c42151a82bdcf3a01e9ae7613b8781f9fbcaea2d081a51830e1` | brouillon v1 contre-lu ; **à refondre avant tout lancement** |
| `test_banc_jev.py` | `204fe66a651b94bf4babcd3054ee79f6f64edff9a50a412fdfffd5d7442b1738` | 29 tests, 15 mutations toutes attrapées |
| `BLOC-banc-jev-v1.md` | `862b8f63057e32b2cbe93e5cb262f88c724481ba56fe1e60073ab1d3ac6e828d` | guide PowerShell, brouillon ; à régénérer avec les chiffres finaux |
| `question-pince-gabarit-v2.md` | `007e960d51d24790cc7984d0f4c3aedca73e02879e27c9fb03a9fc0748e8127d` | question de l'étage III, v2 : place de Jev dans la pince (questions 2, 6, 7, 8) |

Le gabarit de faits v2.3, la question de l'essaim, le gabarit d'arbitrage et le bloc v2.5 sont ceux du paquet livré le 22 octobre. Tests : `python -m pytest -q` dans ce dossier ; 87 tests passaient.

## Ce que Lazar a approuvé

Le 22 octobre, Lazar a répondu « oui » à la question : « Veux-tu que j'écrive le banc de calibration de Jev ? Il plante des défauts, garde des versions saines, ajoute une phrase parasite, et fixe les seuils avant de lire les résultats. » Il lui reste à lancer le banc lui-même.

Deux nuances, que Lazar connaît :
- **Le nombre d'appels.** Il était annoncé à « quelques dizaines ». Le plan actuel en compte 276, et la refonte en compte environ 394, soit 400 000 jetons d'entrée au plus. Une option `--bases 3` en fait la moitié.
- **Le rôle calibré.** Le banc mesure Jev comme auditeur de la rigueur des propositions, pas comme mâchoire de la pince (moniteur de code). Le banc de la mâchoire est la proposition P-026 : défaut (a) le 24 octobre vers 17:43 UTC.

## La refonte à faire

Elle suit la contre-lecture indépendante, `contre-lecture-banc-jev-v1-2026-10-22.md`, et doit être faite avant tout lancement. Elle était conçue, pas encore écrite.

1. **Cas durs** (constat 1). Pour chaque question, deux familles de cas, rapportées à part et assorties de critères propres :
   - des défauts qui gardent les indices de forme d'un texte conforme ;
   - des versions conformes écrites sans ces indices, plus une version entièrement paraphrasée par base.
2. **Six tournures par question au lieu de trois** (constats 8 et 20), réparties par carré latin sur les 6 bases, avec le défaut tantôt en hypothèse 1 et expérience 1, tantôt en hypothèse 2 et expérience 2. Résultats rapportés par tournure.
3. **Vérité terrain** (constats 2 à 4) :
   - H2 et H3 réécrits sans vocabulaire de certitude ;
   - les références plantées écrites en simples renvois ;
   - « (illustratif) » sur les nombres des contrôles ;
   - la base 6 remplacée par un thème sans lien, longueur des phrases et traduction automatique ;
   - les variantes de surface retirées des fausses alertes des autres questions ;
   - l'exclusion « superlatifs hors de H » gardée.
4. **Une non-réponse compte comme un échec** de son critère (constat 5).
5. **Répétition jugée sur les décisions** (constat 6) : un échantillon stratifié de 18 textes (saines, surfaces, défauts durs), au plus 1 décision changée par question.
6. **Découpage** (constat 7) : rang tournant, cas durs, deux items croisés par question. Le facteur confondu (phrase de contexte de la question H) est consigné.
7. **Injection** (constat 19) : trois tournures (français en fin de texte, anglais en fin de texte, français au milieu), plus une phrase neutre témoin, en descriptif.
8. **Verdict** (constats 9, 11, 13) :
   - « NON CONCLUANT » par question si le run est invalide ou incomplet ;
   - INVALIDE si plusieurs modèles ont été servis ;
   - la phrase sur la surface restreinte aux duels et aux contrôles.
9. **Intégrité** (constats 12, 14, 15, 16) :
   - pire cas compté si une réponse n'a pas d'usage, et plafond non fini ou nul refusé ;
   - journal scellé en fin de run ;
   - sceaux hachés sur les octets ;
   - `verifier` régénère le corpus et compare le code ;
   - erreurs système consignées, code 6 pour l'interruption, sous-commande `clore`.
10. **Descriptifs** (constat 23) : aire sous la courbe, fausses alertes par catégorie, note `rigor` par type.
11. **Avant de figer les seuils** (constats 22 et 24) :
    - faire étiqueter à l'aveugle environ 30 variantes × 5 questions par deux lecteurs neufs, et sortir des critères les items contestés ;
    - inscrire aux registres les empreintes des seuils et du manifeste.
12. **À proposer à Lazar** (constat 21) : préciser le critère « false » de la question H du collisionneur, « verified » seulement avec une source citée. Cela changerait le collisionneur, donc une v2.6.

Ce qui reste valable pour la suite :
- les observations de la relève de Gemini sur Jev (une sortie vide mieux notée, `negative_controls` à 0,67 sur du « lorem ipsum ») sont des hypothèses que le banc refondu doit mesurer ;
- voir aussi l'audit de la relève, `docs/notes/audit-releve-gemini-2026-10-24-v1.md` sur `main` (`ba399ea6…`).
