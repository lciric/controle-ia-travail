# Rapport du développeur sur la répétition sur carte de l'étape B bis de T0.7 (modèle A), v1

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` du dépôt de travail ; aucune machine, aucun appel réseau, aucune dépense ; aucun vrai outil `vastai` appelé (faux outil
seulement) ; aucune location : la mère lance après contre-lecture et feu écrit. Lus pour les tailles : `devis-etape-b-bis-v3.md`
(`9431d300…`, l. 15-17 : ≈ 143 000 jetons × 4 096 dimensions par apprentissage, prix A100) et, de la configuration scellée de 7b,
la seule clé `"fils"` (`prereg/T0.6-organismes-config-7b-v1.json`, `b7a5c1ba…` : 1).

- **Auteur** : « modèle A ». **Date (UTC, `date -u`)** : 2026-11-14, jusqu'à 22:55.
- **Objet** : mot de Lazar **R-2802** (écart déclaré au texte scellé) : courte répétition sur carte, sur données synthétiques
  seulement, **avant `CODE-BBIS`**, sous la ligne GO-2026-11-14-09, plafond 3 USD, une seule machine.
- **Commits** (branche `prep/t07bbis-code-v1`, jamais poussée par moi) : code et essais `02d377369cfaf7daef58fb623d06095b57df48c6` ;
  cette note et la sortie des essais : commit suivant. La vérification courte de m-A et des destructions (modèle C,
  `f4427fb6`, « scellable avec mineurs ») est lue : ses mineurs m-E (témoin indispensable) et m-F (forme réelle de la liste) sont
  repris ici (§ 3, geste 9).
- **Le code de la course ne change pas** : quatre fichiers neufs seulement (`git diff --stat 36d555bd 02d37736` : aucun fichier de
  la course) ; la liste des 90 fichiers de la fiche, `MIN_ESSAIS = 86` et l'extraction partielle sont inchangés (simulés de nouveau
  au commit `02d37736` : 86 passés, 22 sautés).

## 1. Fichiers neufs

| fichier | rôle | empreinte |
|---|---|---|
| `scripts/repetition_carte_bbis_v1.py` | partie carte (sous-commande `carte`) et gardes de session (`offre`, `garde-commande`, `depense`, `identifiant`, `absence`) ; **appelle tel quel** le code de la course (`apprentissage_carte_v1.LotCarte`, `entrainer`, `controle_carte_processeur`, `harnais.modeles.regler_determinisme`, `registre_bbis_v1.garde_depense` à la coupure de 3 USD, `registre_bbis_v1.exiger_absence`, constantes de la garde de débit) | `9a01d36a74ab3e427e74003d94b912c5f24549101e0d50f2f47c4480a59b3758` |
| `scripts/amorce_repetition_bbis_v1.sh` | amorce de répétition, à part de celle de la course | `c56c9cc9153a8df313ad68efb269c1ff886388b1bbbb924c724c6e9337f62e8e` |
| `scripts/lancer_repetition_bbis_v1.sh` | chaîne de session (contrôle et impression des commandes ; ne crée, n'arrête ni ne détruit rien) | `7a02afc4f3bcb0cbe5049f0bfb903f20ca32699ac6d9c4bda69ac4db20074ac8` |
| `tests/test_repetition_bbis_v1.py` | 9 essais (§ 4) ; hors du motif `tests/test_t07bbis_*` : n'entre ni dans les essais de l'instance de la course ni dans `MIN_ESSAIS` | `b05cbde3e3c0dd9763aaac73693a6fe73976e705d9e753bc6ab58b4c4efc1bfd` |

## 2. Ce que fait la machine (amorce de répétition), et ses codes fermés

0. Arguments (`COMMIT`, `BRANCHE_CODE`, `ECHEANCE_UTC_S` dans les 3 h, `GO_ID` = GO-2026-11-14-09, `SCRIPT_SHA256`, `CONTAINER_ID`) ;
   **minuterie de destruction armée avant toute passe** (même texte que celle de la course : `DELETE` par l'identifiant, jamais
   jugé par son code, refait toutes les 60 s tant que l'instance vit, « stopped » au 5ᵉ essai).
1. Machine : outils, `GH_TOKEN` par son nom, `nvidia-smi` (A100 exigée, celle de la course).
2. Clone de `BRANCHE_CODE` seule (`--filter=blob:none --no-checkout --single-branch`) ; branche de sortie
   `calcul/t07bbis-repetition-v1` **absente** du dépôt distant (R12 ; dès lors tout arrêt pousse ses traces) ; **extraction
   partielle réelle** : les `MOTIFS` lus dans `scripts/amorce_bbis_v1.sh` **au commit** (une définition exactement) ; tête =
   COMMIT ; **aucune entrée de 7b** : aucune autre branche récupérée, `runs/`, `diag/`, `donnees/`, `essai/` absents de l'arbre,
   sinon arrêt ; le script de la répétition est pris au commit **hors de l'arbre** (`git show`), empreinte = `SCRIPT_SHA256`.
3. Paquets : `python3 -m venv`, `pip install -v -r requirements-gpu.txt` **verbeux**, borné par `timeout -k 30 3600`, durée écrite
   au journal, journal verbeux gardé (début et fin, `pip-verbeux.txt`) ; **code 5** au-delà du délai, **code 6** en échec ; torch
   doit voir la carte ; `pip freeze`.
4. Essais de l'arbre de l'instance par **la commande même de la course** (`tests/test_t07bbis_*.py`, `-rs`), compte lu par la
   fonction `compte_passes` **de l'amorce de la course** et **`MIN_ESSAIS` de la course** (86, lu au commit) : échec ou moins de
   86 passés → **code 7** ; les essais ne doivent rien écrire sous `src` ni `tests`.
5. Carte (`repetition_carte_bbis_v1.py carte`, `CUBLAS_WORKSPACE_CONFIG=:4096:8`) : `regler_determinisme(1, "cuda")` (un fil comme
   la course ; algorithmes déterministes) ; jeu synthétique **de la taille de la course** : 640 actions (32 tâches × 20), longueurs
   150 à 297 jetons (≈ 143 000 jetons), 4 096 dimensions, plus 256 actions de contrôle ; six apprentissages entrelacés (linéaire,
   attention ; couche 15 ; l2 10⁻³, 10⁻², 10⁻¹), durée de chacun ; **déterminisme** : premier réglage de chaque famille réappris,
   paramètres égaux au bit près ; **contrôle carte-processeur** des deux familles au seuil du texte (10⁻⁴), durée de chacun ;
   projection de la garde de débit (§ 5). **Code 8** : erreur d'apprentissage (torch compris), **code 9** : contrôle au-delà de
   10⁻⁴ ou non-déterminisme, **code 2** : garde ; sortie `repetition-carte.json` écrite dans tous les cas, **aucune aire**.
6. Traces (`traces/bbis-t07-repetition-v1/` : journal, `nvidia-smi.txt`, `pip-verbeux.txt`, `pip-freeze.txt`, `essais.txt`,
   `essais.err`, `carte.txt`, `carte.err`, `carte-resume.txt`, `repetition-carte.json`) poussées sur
   `calcul/t07bbis-repetition-v1` par un commit des seules traces posé sur COMMIT ; « stopped » demandé ; code 0.

## 3. Commande de la répétition pour la mère (gestes numérotés)

Dans `/home/user/controle-ia-travail`, `PY=.venv/bin/python`, `PYTHONPATH=src`. Le préfixe `GO_ID=GO-2026-11-14-09` porte toute
commande de location (garde de calcul). **Avant le geste 1** : contre-lecture de ce code et **feu écrit de la mère** portant
GO-2026-11-14-09 et R-2802 ; ligne d'engagement de la répétition au registre des dépenses (≤ 3 USD sous GO-2026-11-14-09).

0. **Le code sur le dépôt distant** (l'instance clone `controle-ia-travail`, jamais `controle-ia`) :
   `git push origin prep/t07bbis-code-v1` (ou fusion dans `main` poussée, alors `BRANCHE_CODE=main`) ;
   `COMMIT=$(git rev-parse prep/t07bbis-code-v1)` ; `git ls-remote origin refs/heads/prep/t07bbis-code-v1` doit rendre `$COMMIT` ;
   `git ls-remote --exit-code origin refs/heads/calcul/t07bbis-repetition-v1; echo $?` doit rendre **2** (branche neuve).
1. **Crédit et paiement** : `vastai show user --raw > /tmp/repetition-utilisateur-avant.json` ; relever le crédit disponible (et le
   moyen de paiement) : au moins 4 USD (plafond 3 USD + marge), sinon aucune location ; relever le cumul déjà dépensé sous
   GO-2026-11-14-09 (registre des dépenses).
2. **Offre** : `vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=60 reliability>0.98' -o 'dph_total' --raw > /tmp/repetition-offres.json`
   (forme de requête à confirmer par `vastai search offers --help` sur l'outil 1.11.0) ; retenir la moins chère, prix du jour au
   plus 1,40 USD/h (attendu 1,09 à 1,30) ; écrire `OFFRE.json` = {`id`, `carte`, `coeurs`, `memoire_vive_mo`, `disque_go`,
   `stockage_usd_h`, `prix_usd_h`, `etiquette`: `bbis-t07-repetition-v1`} ;
   `bash scripts/lancer_repetition_bbis_v1.sh offre OFFRE.json ID P` → « BBIS REPETITION OFFRE ACCEPTEE ».
3. **Échéance de la minuterie** (destruction à l'échéance quoi qu'il arrive) :
   `DMAX=$($PY -c "import importlib.util as u; s = u.spec_from_file_location('r', 'scripts/repetition_carte_bbis_v1.py'); m = u.module_from_spec(s); s.loader.exec_module(m); print(int(m.duree_max_h($P) * 3600) - 600)")` ;
   `ECH=$(( $(date +%s) + DMAX ))` (au plus 3 h ; (durée + ¼ h) × prix + 0,40 USD < 3 USD ; 10 min de marge pour la création :
   à 1,30 USD/h, 95 min ; à 1,09, 118 min ; à 1,40, 86 min).
4. **Création** : `bash scripts/lancer_repetition_bbis_v1.sh commande . OFFRE.json ID "$COMMIT" prep/t07bbis-code-v1 "$ECH" "$P" "<feu écrit>" <image de la course> > /tmp/repetition-commande.txt`
   (contrôles : offre, feu portant GO-2026-11-14-09 et R-2802, échéance, COMMIT présent et portant l'amorce de la course, cette
   amorce et le script, amorce en essai local sur un dossier jetable) ; jouer **la dernière ligne** imprimée
   (`GO_ID=GO-2026-11-14-09 vastai create instance ID --raw … --label bbis-t07-repetition-v1 …`, jetons par leur nom) ; relever
   l'identifiant de l'instance (`new_contract`) et l'heure.
5. **Minuterie armée** : `vastai logs <instance> | grep 'BBIS REPETITION'` ; la première ligne utile doit être « minuterie lancée
   (PID …, échéance …), avant toute passe », avec l'échéance de `ECH`. Rien au journal 15 min après l'état « running » : geste 9.
6. **Garde de dépense à 3 USD**, toutes les 15 minutes : cumul relevé (heures facturées × prix, plus stockage) ;
   `bash scripts/lancer_repetition_bbis_v1.sh depense CUMUL P` ; refus (cumul + ¼ h de carte ≥ 3 USD) → geste 9 aussitôt.
7. **Suivi** (`vastai logs <instance>`), lignes attendues dans l'ordre : carte A100 et disque ; dépôt au commit, extraction par
   les MOTIFS de la course, aucune entrée de 7b, script à l'empreinte attendue ; installation « code 0, N s » ; essais « code 0,
   ligne de compte : 86 passed, 22 skipped … ; minimum de la course : 86 » ; « carte : code 0 » puis le résumé (état reussie ;
   jetons ≈ 143 000 ; déterministe {linéaire : True, attention : True} ; médiane ; projeté ; écarts ≤ 10⁻⁴) ; « FIN : répétition
   menée au bout » ; « traces poussées : … (parent COMMIT, branche calcul/t07bbis-repetition-v1) » ; « fin, code 0 ».
8. **Récupération** : `git fetch origin calcul/t07bbis-repetition-v1` ; `git rev-parse FETCH_HEAD^` = `$COMMIT` ;
   `git show FETCH_HEAD --stat` : `traces/bbis-t07-repetition-v1/` seulement ; lire `repetition-carte.json` (états, durées,
   `garde_de_debit`, `controle_carte_processeur`, `deterministe`, `determinisme` : carte, pilote, CUDA, réglages relus),
   `essais.txt`, `pip-verbeux.txt` (durée), `nvidia-smi.txt`, `pip-freeze.txt`.
9. **Destruction** (dès le geste 8, ou à tout arrêt) : `bash scripts/lancer_repetition_bbis_v1.sh detruire <instance>` ; jouer la
   ligne imprimée `GO_ID=GO-2026-11-14-09 vastai destroy instance <instance> -y` ; puis
   `bash scripts/lancer_repetition_bbis_v1.sh verifier-destruction <instance> 60480302` (ou **60670453** si 60480302 n'est plus
   listée) → « BBIS DESTRUCTION PROUVEE » ; code 2 (« absence non prouvée » : instance listée, témoin absent, liste illisible ou
   lecture en échec) → refaire destruction et vérification, compte rendu. Une liste de forme inattendue rend « illisible »,
   jamais un faux « prouvée » : c'est la confirmation de m-F. **Jamais** 58936096, 58936099, 58936100, 60480302, 60599797,
   60670453 (refusés par l'outil comme cibles ; permis comme témoins).
10. **Consigner** : dépense (`vastai show user --raw` après), arrêt (`registres/arrets.md`), résultats (médiane mesurée contre le
    seuil de la garde de débit ; écarts ; durée de l'installation) et les suites du § 6.

**Ce qui arrête** :

| code (journal « ARRET : … ») | sens | suite |
|---|---|---|
| 2 | garde : arguments, carte autre qu'une A100, `GH_TOKEN` absent, clonage, branche de sortie déjà présente, MOTIFS illisibles, entrée de 7b dans l'arbre, empreinte du script, torch sans carte, compte ou minimum de la course illisibles, essais écrivant sous `src`/`tests`, garde de la partie carte | geste 9 ; lire le motif |
| 5 | installation au-delà de 60 min | geste 9 ; la course (même délai, `timeout -k 10 3600`) s'arrêterait aussi : § 6 |
| 6 | installation en échec | geste 9 ; `pip-verbeux.txt` |
| 7 | essais en échec ou moins de 86 passés sur l'image réelle | geste 9 ; la course s'arrêterait à son étape 5 : § 6 |
| 8 | erreur d'apprentissage sur la carte (torch compris) | geste 9 ; la course tomberait en arrêt écrit (M2) : § 6 |
| 9 | contrôle carte-processeur au-delà de 10⁻⁴, ou apprentissage non déterministe | geste 9 ; erreur de chaîne de la course : § 6 |
| 4 | autre (poussée des traces impossible, code inattendu) | geste 9 |
| — | garde de dépense (geste 6) ; échéance (minuterie) | geste 9 |

## 4. Essais (cas sain et artefact)

`tests/test_repetition_bbis_v1.py`, 9 essais : partie carte sur processeur à petite taille (sain : réussie, entrelacée,
déterministe, écarts ≤ 10⁻⁴, projections 2 460 et 1 240, un fil, aucune clé d'aire ; artefacts : sortie présente → 2, tolérance
relâchée à 10⁻³ → 2, tolérance plus stricte que l'écart réel → 9 avec motif, erreur « CUDA » simulée → 8 avec pile, apprentissage
perturbé au réapprentissage → 9 « non déterministe », carte demandée absente → 2) ; amorce en essai local (aucune écriture ;
arguments fautifs refusés ; aucune récupération de 7b dans le texte ; minuterie avant le clonage) ; lecture des MOTIFS de la course
(égaux à ceux de la course ; deux définitions ou aucune → refus) et garde « aucune entrée de 7b » sur une extraction réelle
(chacun de `runs`, `diag`, `donnees`, `essai` présent → refus) ; lecture du compte et de `MIN_ESSAIS` de la course (égaux ; deux
minimums ou bloc absent → refus) et résumé de la carte ; installation bornée (faux python : réussite 0, durée au-delà du délai 5,
échec 6) ; traces poussées sur COMMIT (sain : parent COMMIT, traces seules ; avant le contrôle de la branche : rien) ; minuterie
(corps identique à celle de la course ; six `DELETE` « 200 » sans effet, un `PUT stopped`) ; lanceur (offre : cinq fautes ;
commande saine sur un dépôt jetable — ligne `GO_ID=… vastai create instance`, étiquette, disque 60, `SCRIPT_SHA256`, jeton par son
nom, aucun `HF_TOKEN`, dossier jetable retiré ; artefacts : feu sans R-2802, échéance trop lointaine pour le prix, commit absent,
amorce du commit autre, script absent ; dépense : 2,0 + 0,325 accepté, 2,7 + 0,325 refusé avec destruction annoncée) ; destruction
contre un **faux `vastai`** (sain : ligne imprimée avec `-y`, jouée, puis « PROUVEE » avec le témoin 60670453 ; **cas du
2026-11-14** : sans `-y`, « Aborted. », code 0, puis « absence non prouvée », code 2 ; témoin absent → 2 ; les six instances
d'autres sessions refusées comme cibles, en `detruire` et en `verifier-destruction`).

Comptes : **117 passés** (108 de la course + 9) sur l'arbre complet ; arbre de l'instance simulé au commit `02d37736` : **86
passés, 22 sautés** ; `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-repetition-carte-v1.txt` (`877c8b17…`). La commande de
création a aussi été imprimée sur le vrai commit `02d37736` (essai, rien créé).

## 5. Devis de la répétition

| poste | attendu | haut |
|---|---|---|
| démarrage, image, clonage partiel | 5–10 min | 15 min |
| installation (pip verbeux) | 5–15 min | 47 min observées ce jour sur une autre course ; borne 60 min (code 5) |
| essais de l'arbre de l'instance | 2 min (1 min 50 s simulé ici) | 5 min |
| partie carte : jeu synthétique (≈ 1 min) ; 8 apprentissages sur la carte (2 à 4 s chacun selon le devis de B bis, **non mesuré** : la répétition le mesure) ; deux contrôles sur processeur à un fil (≈ 4,6 et 8,9 min, extrapolés × 9,7 des 28,7 s et 55,1 s mesurés ici au dixième de la taille) | ≈ 15 min | 30 min (hôte deux fois plus lent) |
| traces, arrêt | 1 min | 3 min |
| **total** | **≈ 30 à 45 min** | ≈ 100 min, **borné par l'échéance** |

Prix A100 SXM4 80 Go : 1,09 à 1,30 USD/h attendu, au plus 1,40 (devis de B bis, l. 16). **Coût attendu ≈ 0,9 à 1,4 USD** (carte
0,5 à 1,0 ; stockage ≤ 0,08 USD/h et téléchargements ≈ 5 Go à ≤ 0,05 USD/Go : ≤ 0,40). **Pire cas < 3 USD par construction** :
l'échéance de la minuterie est fixée pour que (durée + ¼ h) × prix + 0,40 < 3 USD, et la garde de dépense arrête au cumul + ¼ h
≥ 3 USD.

**Garde de débit de la course** (lue dans `repetition-carte.json`, `garde_de_debit`) : 2 460 apprentissages ; elle se déclenche si
la médiane dépasse **≈ 12,1 s** (relecture 0,55 h ; 11 h, facteur 1,2, marge 0,6 h) ; variante (r1) : 1 240. Les durées sont
prises au lot entier de 640 actions (sonde finale, nul, ENC) ; la validation interne apprend sur 480 : la projection est prudente.

## 6. Réserves, et ce qui demanderait un changement du code de la course (dit, non fait)

- **Instance 60670453 absente de la liste de la course** : `registre_bbis_v1.INSTANCES_D_AUTRES_SESSIONS` (cinq identifiants) ne la
  porte pas ; `lancer_bbis_v1.sh detruire 60670453` imprimerait une destruction. La répétition la refuse (liste à six) ; **pour la
  course, ajouter 60670453 avant `CODE-BBIS`** (une ligne et son essai) : changement du code de la course, à décider.
- **Selon l'issue** : code 5 (installation > 60 min) → le délai de la course (`timeout -k 10 3600`, pip silencieux, sans code
  dédié ni durée écrite) serait à relever ; code 7 → l'image réelle ou les essais diffèrent de la simulation ; codes 8 ou 9 →
  `apprentissage_carte_v1` à corriger ; dans ces cas, **avant `CODE-BBIS`**. Une projection au-delà de 11 h ne demande aucun
  changement : c'est le nœud (r1) de Lazar.
- **Ce que la répétition ne prouve pas** : la relecture forcée (modèle et jetons de 7b), la descente du modèle (`HF_TOKEN` non
  passé), la sortie de 7b, le commit local des entrées et la marche elle-même ; la boucle de copie des fichiers cités par le
  registre propre n'est pas jouée (tous les fichiers cités à ce jour sont dans les motifs).
- **Budget de la ligne** : la répétition (≤ 3 USD) se compte sous GO-2026-11-14-09 (40 USD) ; le pire cas de la course au devis
  (≈ 37,5 USD, relance comprise) plus 3 USD dépasse la coupure de 39,5 USD : dans ce pire cas, la garde de dépense de la course
  arrêterait plus tôt. L'attendu de la course (5,6 à 9,9 USD) n'est pas touché.
- **Choix déclarés** : machine = A100 SXM4 80 Go (« carte équivalente » lue comme le même modèle que la course) ; disque 60 Go (ni
  modèle ni données) ; taille de la course par défaut (`ACTIONS_REPETITION` réduit le nombre d'actions, fraction écrite dans la
  sortie) ; contrôle carte-processeur des deux familles (la course en joue un) ; un fil comme la course ; graines par
  `SeedSequence` d'une entropie fixe écrite dans le script (répétition non décisive) ; la garde de création de la course
  (`CODE-BBIS` exigée) ne peut pas passer avant `CODE-BBIS` : la répétition a sa garde propre (feu portant R-2802).
- **m-D** (vérification courte) : une instance « stopped » non détruite reste facturée en stockage jusqu'au geste 9.
