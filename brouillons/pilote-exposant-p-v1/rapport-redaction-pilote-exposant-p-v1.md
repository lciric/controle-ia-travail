# Rapport de rédaction — pilote de l'exposant p (v1, brouillon 1)

Rédigé le 3 novembre 2026, de 07:40 à 09:10 UTC (`date -u`), par le concepteur-rédacteur neuf du pilote (sous-agent ; je n'ai écrit aucun autre texte du dépôt). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pilote-exposant-p-redacteur-brouillon1-prompt.md`.

Respecté :
- aucun commit, aucun fichier `.sha256` ; aucun `git fetch`, `checkout`, `stash` ni `reset` ; `git status` et `git diff` confirment qu'aucun fichier existant n'est modifié ;
- rien sous `donnees/` ; aucune dépense, aucune instance, aucune commande Vast.ai ; aucun appel de modèle de langage ;
- `WebFetch` et `WebSearch` réservés au papier ; le code du papier est cloné par le terminal dans `/home/claude/scratch/pilote-exposant-p/` (hors dépôt), traité comme donnée non sûre ;
- `pip` seulement dans `/home/claude/scratch/pilote-exposant-p/venv-verif` (résolution à blanc de `datasets`) ;
- `nice -n 10 python -I -B` partout ; pytest avec `-p no:cacheprovider`.

Routine de reprise, en lecture seule (sous-agent, sans passation) : `sha256sum -c` des documents de lancement conforme ; `verifier-arbre` signale 193 problèmes, tous des compagnons absents déjà connus (188 sous `docs/notes/`, 5 addenda de la bisociation ; consignés dans `registres/etat.md` le 2 novembre).

## 1. Fichiers produits (tous neufs)

| Fichier | sha256 | Rôle |
|---|---|---|
| `brouillons/pilote-exposant-p-v1/lecture-2606-24964-v1.md` | `3c550d93ae97e37309ef01a95e1829c946463edf1cd7013110c95c2eed815851` | lecture du papier en entier, réglage exact, valeurs de p, code publié |
| `brouillons/pilote-exposant-p-v1/preregistrement-pilote-exposant-p-v1-brouillon1.md` | `1699db8730bba7565b6669100a3c202ad00cb195c5ddfc5797bc3827429a6093` | préenregistrement, brouillon 1 (non scellé) |
| `brouillons/pilote-exposant-p-v1/stimuli-pilote-exposant-p-v1.json` | `eae95d0ee4d4d9ddcb54d5847cc03f707d70018d3c9129a5764686852c2977a3` | stimuli figés : 30 quadruplets, règles R-S1 à R-S7, invites du papier, cadrages de l'échelle v2 |
| `brouillons/pilote-exposant-p-v1/config-pilote-exposant-p-v1.json` | `18b724d2e22e23c66a658aeaf5225bbebb38fb61d87b6ca4686f83ee6f80598c` | configuration figée (et section jouet) |
| `brouillons/pilote-exposant-p-v1/puissance-pilote-exposant-p-v1.json` | `35dc3bdf5cb02d28737f85331a13b532a0b28a4abb88bfdcd507cd2f13dba29f` | sortie de la simulation de puissance |
| `brouillons/pilote-exposant-p-v1/devis-pilote-exposant-p-v1.md` | `165930e5a77e731d5ca1f105bf590c759430502e0b670a04f49ca4beef69f427` | devis |
| `scripts/pilote_exposant_p_instance_v1.sh` | `6c12eebe647d0166e7a7653446b09cab547bf8d6d538fd8f3aedb94b1489aeab` | script d'instance (jamais lancé) |
| `src/controle_ia/pilote_exposant_p/__init__.py` | `cfd8f7bc20311e23ad206416f7e55debddd6e55558f5216c1e8104c83d81e3d5` | paquet |
| `src/controle_ia/pilote_exposant_p/ajustement.py` | `8eba82e0cf3d56bd3f3c16f190737e8370e33e5312800840290c434d34ef7f64` | p d'un plan au protocole du papier, rééchantillonnages |
| `src/controle_ia/pilote_exposant_p/analyse.py` | `86a619348b0b937ed5eef3c99868e7067ff7008fe22877f9ec9bcce0fc949429` | critères gelés, contrôles de l'instrument, audit de symétrie |
| `src/controle_ia/pilote_exposant_p/ancres.py` | `44d62bf97c0c39ae864ebc0c571cf94a8ba25edd5638f5ce456fa49e4dbc28af` | réserve FineWeb-edu (instance) et réserve jouet |
| `src/controle_ia/pilote_exposant_p/balayage.py` | `424480fe2c415569a7b8ea82906b897825461f299f0a269e62b53ab504c57323` | activations et balayage d'un plan par crochets |
| `src/controle_ia/pilote_exposant_p/directions.py` | `17a3dcdedcea781839b9c823fd5d675757e8a4b1f14d1cf39287c41e55f74aa8` | différences de moyennes, différences aléatoires, isotropes, règle du cosinus |
| `src/controle_ia/pilote_exposant_p/puissance.py` | `b78f36defe944719a0019d20d649d94a11324287c53d529a262f1d046acc0743` | simulation de puissance |
| `src/controle_ia/pilote_exposant_p/references.py` | `793d70dc2a98b409ecfd08001c20c8c77fef7238b9a617f725279c2c18f638f8` | lecteur restreint des caches publiés, conversion |
| `src/controle_ia/pilote_exposant_p/run.py` | `8965c55c191a9b2ebfa449a614d68fbc3f475e01cdff5bdcb94884397575a6b8` | lanceur (gardes, manifeste, blocs, analyse, sorties scellées ; mode jouet) |
| `src/controle_ia/pilote_exposant_p/stimuli.py` | `a53baf021e2f226a1a1867fbd565d2fdf29d90215b10174fbebacef29240e6bb` | validation des stimuli, paires |
| `src/controle_ia/pilote_exposant_p/requirements-instance-v1.txt` | `b53f94e58338cf7432b9085c50b8ae770ddb644656ba6e99a7454b74d2e5c72e` | `datasets` 5.1.0 et dépendances, sous contrainte |
| `src/controle_ia/pilote_exposant_p/amont/__init__.py` | `c1626211e3a0748cdc3d088b91055364709535cd745c7edffbd236084ae4db8d` | vérification de la copie amont |
| `src/controle_ia/pilote_exposant_p/amont/PROVENANCE.json` | `938fc38b0f32a2a975b8ea5153228fc042594ad8dee768f84dfc9c47ba808a24` | provenance (dépôt, commit, empreintes) |
| `src/controle_ia/pilote_exposant_p/amont/parametrize.py` | `35e855f048daeccdb6406a66658effd2401d12cafb83322297c55ff06d183303` | copie à l'identique (MIT) |
| `src/controle_ia/pilote_exposant_p/amont/superellipse.py` | `47d19c99147577d6670f5727eb23a8de5336f5677d3d2f6c342974d20dd0da0d` | copie à l'identique (MIT) |
| `src/controle_ia/pilote_exposant_p/amont/LICENSE-fsec-paper` | `3d9685342ea6ef1a6e2f4a58cabba83b856c75623ed8862470aff97037aceb48` | licence MIT recopiée |
| `src/controle_ia/pilote_exposant_p/references_publiees/references-publiees-v1.json` | `b594ee86b6d5ee1e6355203eca416815fc87e0e4c55eaf7f8b4b66675516375a` | valeurs publiées et recalculées, provenance |
| `src/controle_ia/pilote_exposant_p/references_publiees/grilles-publiees-v1.npz` | `c30a014a2e03aed0ce69dc43ea80488a7a47c0eb013f558c59c36f574ece9fbe` | grilles publiées de Llama (Wealth × Gender, deux isotropes) |
| `src/controle_ia/pilote_exposant_p/references_publiees/directions-publiees-v1.npz` | `ced98c6285e0a6f7c0dd31189d2a00916b38fd764410fb32d9891821990380b0` | sept directions publiées de Llama, couche 2 |
| `tests/test_pilote_exposant_p_v1.py` | `686e879af8761c6b12b28e1a43cf4f9180046347efc5c9ee816d53a758d83a66` | 34 essais |

Hors dépôt (non versés), sous `/home/claude/scratch/pilote-exposant-p/` : clone du code publié (`code-tiers/fsec-paper`), outils d'exploration (`outils/`), assembleur des stimuli (`outils/assembler_stimuli.py`), extraction en lecture seule de l'échelle v2, répétition jouet manuelle (`repetition-jouet-1/`).

## 2. Essais

Commande (celle du script d'instance) : `nice -n 10 .venv/bin/python -I -B -m pytest -q -p no:cacheprovider --color=no tests/test_pilote_exposant_p_v1.py tests/test_manifeste.py tests/test_scellement.py tests/test_prereg.py`, de 08:57:52 à 08:59:38 UTC :

```
..............................................................           [100%]
62 passed in 104.38s (0:01:44)
```

Les plus longs : répétition jouet de bout en bout 101 s ; isotropes sur transformeur aléatoire 15 s ; direction plantée 8,5 s. La suite entière du dépôt n'a pas été relancée ; aucun fichier existant n'est touché.

Valeurs relevées par les essais (processeur, aucun téléchargement) :
- **p connu, données synthétiques** (superellipse exacte, grille 31 × 31) : 2,0 → 1,998 ; 2,5 → 2,496 ; 3,0 → 2,992 ; 4,0 → 3,988 ; résidus ≤ 0,02 %. Sous bruit d'ancres, 2,5 se distingue de 2,0 (écart > 0,2).
- **Grille publiée** : re-ajustement de Wealth × Gender sur Llama = 3,0030827, égal au p publié à 10⁻⁶ près, intercepts à 10⁻⁴ près. Les deux grilles isotropes publiées donnent p dans (1,7 ; 2,3).
- **Isotropes, petit Llama aléatoire** (6 blocs, largeur 64) : 1,881 ; 2,125 ; 1,831.
- **Direction privilégiée plantée** (correction d'erreur à zone morte sur deux directions, devant le bloc 2) : p(traits) = 2,931 contre p(aléatoires) = 1,863 dans le même jouet.
- **Passage par crochets** : égal **exactement** aux états cachés du modèle (couches 0, 2, 4). La convention décalée d'une couche est détectée. Le remplacement par l'activation elle-même ne change rien ; la causalité tient (positions précédentes inchangées).
- **Graines** : différences aléatoires, rééchantillonnages et grilles rejouées à l'identique ; isotropes du papier reproduits **à l'identique** (empreinte des 33 × 4096 valeurs publiées) ; graine 43 : empreinte différente.
- **Gardes, chacune sur un cas sain et sur un artefact (R5)** :
  - copie amont altérée ; pickle piégé refusé par le lecteur restreint ;
  - quatre règles de stimuli violées et invites du papier altérées ;
  - configuration incohérente ; stimuli d'une autre empreinte ; run réel sans préenregistrement ;
  - témoin positif, isotropes et directions publiées hors tolérance ;
  - table gelée des issues ; déclencheurs de symétrie dans les deux sens.
- **Répétition jouet de bout en bout** : manifeste, plans, sorties, lecture et résumé écrits puis vérifiés par `verifier_resultat` ; grilles scellées.
- Répétition manuelle à la taille jouet complète (34 plans, 4 min 25 s sur deux cœurs chargés) : issue gelée « exclu » (cos(E, R) = −0,12 sur ce modèle aléatoire) ; lignes `PROGRES` au format du relais de P3.

## 3. Ce qui est repris du papier, ce qui s'en écarte

**Repris.**
- Code amont : `parametrize.py` et `superellipse.py`, copiés à l'identique, licence MIT recopiée, empreintes vérifiées à chaque run.
- Protocole :
  - couche 2, mesure au bloc n − 2, dernier jeton, réponse L2 ;
  - grille 31 × 31 sur [0, 60°], seuil par paire f = 0,5 sur la grille médiane, fenêtre de 60°, normalisation géodésique exacte, p borné dans [0,5 ; 10] ;
  - 30 ancres FineWeb-edu de 5 jetons (`sample-10BT`, mélange graine 42, tampon 10 000) ;
  - différences aléatoires `k_avg = 30` ; isotropes à graine 42 de torch (reproduits) ; règle d'exclusion |cos| < 0,1 ;
  - invites du papier (Gender, Wealth, Age, Tense, Sentiment, registres), recopiées et contrôlées par leurs empreintes publiées.
- Valeur publiée du témoin : Wealth × Gender sur Llama-3.1-8B, p = 3,003.

**Écarts** : quinze, déclarés un par un au préenregistrement (E-01 à E-15). Les principaux :
- modèle Instruct (témoin positif sur le modèle de base) ;
- directions E et R neuves, en plan 2 × 2, 60 paires chacune ;
- 32 sous-ensembles de 30 ancres pour le plan lu ;
- 60 paires disjointes de différences aléatoires tirées par `SeedSequence` ;
- 17 isotropes ;
- intervalle par rééchantillonnage conjoint des sous-ensembles et des plans ;
- passage avant par crochets sur le modèle complet, en lots de 961 points.

La lecture (§5) relève aussi sept écarts entre le texte du papier et son code, non tranchés ; le principal est le double filtre de recouvrement de la colonne Llama de l'audit.

## 4. Simulation de puissance (calcul)

`src/controle_ia/pilote_exposant_p/puissance.py` ; sortie `puissance-pilote-exposant-p-v1.json`.
- Générateur : superellipses par ancre, exposant, angles et amplitude hétérogènes, plancher numérique relevé ; calage prudent (σ_p = 0,40, σ_a = 0,30) sur les écarts types publiés.
- Banques : 400 tirages par p vrai, pas 0,05 ; 400 répétitions par cas ; durée 908 s.

| Plan | Δ détectable à 80 % | Δ = 0 → « égal » | faux « au-dessus » / « au-dessous » à Δ = 0 |
|---|---|---|---|
| **S = 32, M = 60 (retenu)** | **0,20** (90,7 % ; 0,15 → 72,0 %) | **86,8 %** | 2,8 % / 3,0 % |
| S = 16, M = 60 | 0,30 (0,20 → 78,7 %) | 59,5 % | 2,5 % / 2,5 % |
| S = 8, M = 30 | 0,40 | 17,0 % | 2,2 % / 5,0 % |
| S = 4, M = 60 | non atteint à 0,4 | 18,0 % | 4,0 % / 11,7 % |
| S = 32, M = 30 | 0,30 | 62,5 % | 2,8 % / 4,3 % |
| S = 32, M = 60, τ = 0,10 ; τ = 0,25 | 0,20 ; 0,20 | 89,5 % ; 77,2 % | — |

Constat : avec un seul jeu de 30 ancres (le réglage du papier), un plan isolé n'est lisible qu'au-delà de ≈ 0,7 d'écart (écart type par ancres ≈ 0,22 à 0,33 ; calcul). D'où les 32 sous-ensembles.

## 5. Dix points pour un contre-lecteur neuf

1. **Stimuli, sens et confusion résiduelle.** Lire les 120 phrases : chaque membre « évaluation » parle-t-il d'une évaluation de l'assistant, et chaque membre « déploiement » d'un besoin réel ? Les fins d'évaluation portent des mots techniques (« benchmark », « graders », « rubric »), celles de déploiement des mots personnels (« my kid », « my boss »). Cela peut recréer un registre lexical à l'intérieur de E, même à registre de phrase apparié. Les règles R-S1 à R-S7 suffisent-elles ?
2. **Statistique principale.** La moyenne des 32 ajustements du plan lu est comparée à la moyenne des plans de référence sur le seul sous-ensemble 0. L'argument (même estimateur à 30 ancres, bruit d'ancres propre à chaque plan, corrélation ≈ 0 relevée sur les grilles publiées) tient-il ? Faut-il moyenner aussi la référence sur plusieurs sous-ensembles ?
3. **Règle à trois issues.**
   - δ = 0,2 (moitié de l'écart publié de 0,37) ;
   - préséance de « au-dessus » quand l'intervalle est dans (0 ; 0,2) ;
   - taux simulés de 2,8 % et 3,0 %, légèrement au-dessus de 2,5 %.
4. **Témoin positif.**
   - Empreinte des ancres par la norme moyenne (10⁻³ relatif) : suffit-elle à dire « ancres identiques » ?
   - Tolérances ±0,15 et ±2° (supposées).
   - Si les ancres diffèrent, l'intervalle [2,420 ; 3,702] est large : un instrument légèrement faux passerait.
5. **Isotropes** sur le modèle lu, [1,75 ; 2,25] : tolérance qui ne vient pas du papier ; le repère du modèle de base, 1,930, est un calcul sur 17 paires.
6. **Plans mixtes** (E, rd) et (R, rd) : jamais mesurés par le papier. Ma lecture idéalisée (p(trait, aléatoire) ≈ p vrai) n'est pas validée ; les témoins mixtes (Gender, rd) et (Wealth, rd) ne sont que descriptifs. Le vocabulaire gelé est-il assez prudent ?
7. **Portée.**
   - Couche 2, dernier jeton, ancres de 5 jetons, invites brutes sur un modèle Instruct.
   - L'argument de Lazar vise des couches moyennes et des contextes longs (Hua et coll., couches 10 à 30).
   - Le pilote répond-il à la question ? Faut-il un bloc descriptif à une couche moyenne ? (Non inclus ; décision « proposer avec recommandation ».)
8. **Code.**
   - Passage par crochets contre passage bloc à bloc du papier : égalité vérifiée sur un petit modèle seulement.
   - Référence en lot de 1 contre points en lots de 961 (arrondis de `bfloat16`).
   - La branche réelle de `run.py` (chargement Hugging Face, flux FineWeb-edu, vérification du tokeniseur) n'a jamais tourné : seul le mode jouet a tourné.
9. **Simulation de puissance.**
   - Le calage vient de rééchantillonnages d'ancres sur grilles publiées : c'est une approximation de l'écart type d'échantillonnage.
   - τ vient de Gemma ; l'estimateur est biaisé vers le bas, d'où le raisonnement sur l'échelle mesurée.
   - Banque arrondie au pas de 0,05.
   - Le caractère « prudent » est-il démontré ?
10. **Provenance (R7).**
    - Les chiffres du texte sont de niveau transcription : `WebFetch`, sans page, PDF non empreinté.
    - Les valeurs par modèle de Llama viennent de l'audit du code (fichier et sha256), pas du texte, et dépendent d'un double filtre que le texte ne décrit pas.
    - Licence du jeu FineWeb-edu non vérifiée ; les textes des 30 ancres du sous-ensemble 0 sont versés dans les sorties.

## 6. Fichiers que le contre-lecteur doit lire

- Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/pilote-exposant-p-redacteur-brouillon1-prompt.md` ; `CLAUDE.md` ; `prereg/gabarit-preregistrement-v1.md`.
- Pièces du pilote : `brouillons/pilote-exposant-p-v1/` — préenregistrement brouillon 1, lecture, stimuli, configuration, sortie de puissance, devis, ce rapport.
- Code : `src/controle_ia/pilote_exposant_p/`, en priorité `analyse.py`, `ajustement.py`, `balayage.py`, `run.py`, `stimuli.py`, `directions.py`, `puissance.py`, `references.py`, `amont/PROVENANCE.json`, `references_publiees/references-publiees-v1.json` ; essais `tests/test_pilote_exposant_p_v1.py`.
- Script : `scripts/pilote_exposant_p_instance_v1.sh`, à comparer avec `scripts/p3_instance.sh` et `scripts/amorce_instance_p3.sh`.
- Contexte : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-heimersheim-v1.md` (point prioritaire A) et `relecture-fable-brouillon-q1-heimersheim-v1.md` (lignes 27 à 38, correction 7).
- Sources : le papier, `https://arxiv.org/pdf/2606.24964`, en entier ; le code, `https://github.com/FranciscoHS/fsec-paper` au commit `a9355d4` : `README.md`, `results/thrpair_audit.md`, `scripts/sweep_2d.py`, `scripts/fit_pairs.py`, `scripts/lib/`, `scripts/random_diff_directions.py`, `src/data.py`, `src/model.py`.

## 7. Réserves et ce qui n'est pas fait

- Pas d'amorce Vast.ai (`amorce_instance_…`) : le script d'instance seul est écrit ; l'amorce bornée reste à décliner de celle de P3.
- La branche réelle du lanceur n'a jamais tourné (aucune carte graphique) ; une répétition jouet sur l'instance est prévue par le script (`MODE=jouet`).
- L'accès Hugging Face doit couvrir les **deux** dépôts Llama (le modèle de base sert au témoin positif) ; le script le vérifie avant tout téléchargement lourd.
- Le préenregistrement garde ses marqueurs `<<…>>` (commit de scellement, contre-lecture) : le validateur refuse de le sceller en l'état, comme prévu.
- Rattachement au programme : aucune hypothèse H1 à H9 testée ; voisinage de la section 11 et de H8 ; toute inscription au programme est un nœud de Lazar.
