# Contre-lecture (R2) — essai d'invariance au lot de l'ablation de `measure`, v1

Lecteur neuf : n'a rien écrit des pièces. Pièces lues : préenregistrement (avec § 7), `audit_invariance_lot_v1.py`, ses essais, l'amorce (diff avec la v7), le dépôt réduit v10 (diff avec v9), l'essai à blanc (diff avec v11), le lanceur v5 en entier pour les tables et les étapes touchées, et `measure` du dépôt voisin à 849bfe16 (l. 107-257) ainsi que le correctif de graine. Rien exécuté du dépôt voisin ; les sept essais du module passent (7 passed, processeur). Aucun résultat sous `diag/` ouvert.

**Verdict : à corriger.** La boucle d'ablation est fidèle ; deux défauts de la règle de lecture (non-déterminisme du lot 64 non couvert ; aucun témoin que l'ablation agit sur la carte) et quelques défauts de traçabilité de l'amorce et du manifeste sont à corriger avant de sceller, puis resceller (module, essais, préenregistrement, dépôt réduit).

## Réponses courtes
(a) Fidèle, sans écart caché sur la boucle. Comparé ligne à ligne à `measure` (l. 216-246 à 849bfe16) : tenseurs `ids` et `attn` construits sur le processeur puis envoyés, complément de zéros à droite, lignes impaires ablatées, `rows`/`pos_t`/`neu_t` créés sur le périphérique, crochet avant `down_proj` avec `clone` puis mise à zéro, fenêtre `pos:min(pos+1+8, len)` (donc 9 positions), `lm_head` en bf16 puis `.float()` puis `log_softmax`, différence propre moins ablatée, `inference_mode`, retrait du crochet. `arch.cap` est l'identité pour ce modèle (le plafond n'existe que pour une autre famille ; `cap` rend `logits` inchangé si `final_logit_softcapping` est absent). Chargement : `from_pretrained(…, dtype=bfloat16).to("cuda").eval()`, `requires_grad_(False)`, `decoder_stack` : identique. Le correctif de graine (`causal_lens-graine-v1.diff`) ne touche pas la boucle d'ablation. Aucun réglage global de torch (précision de matmul, déterminisme) dans le code voisin importé (`grep` fait). Écarts réels mais déclarés ou sans effet : jetons aléatoires sans jeton de début, trois couches sur 32, tâches sans doublon de neurone consécutif. Écarts non déclarés : voir M3, m1.
(b) Non sain en l'état : B1 et M1.
(c) Sûr, sous réserve de M2 (manifeste) et m4.
(d) Chiffres justes (voir détail) ; une incohérence mineure m5.
(e) Voir M4, M5, m6, m7.

## Bloquantes

**B1. Une issue « invariance réfutée » peut venir d'un non-déterminisme propre au lot 64, que C3 ne couvre pas.**
- Fichier : `src/controle_ia/neuron_lens/audit_invariance_lot_v1.py`, l. 114-127 (rejeu seulement au lot `lots[0]`, soit 16) et l. 131-146 (`lire_issue`) ; préenregistrement § 3 (C3) et § 4, ligne « invariance réfutée ».
- Écrit : C3 = « le lot 16 rejoué donne les mêmes empreintes » ; « réfutée » si C1 et C3 tenus et une tâche du lot 64 diffère du lot 16.
- Problème : un noyau qui n'est pas déterministe seulement aux grandes formes (128 lignes × 256 jetons : algorithme de produit matriciel découpé, réductions atomiques) ferait différer le lot 64 de lui-même, alors que C3 (lot 16 contre lot 16) passerait. L'issue serait lue « réfutée », avec la conséquence lourde écrite au § 4 (série au lot 64 suspecte, verdict de B-7 ne remplace plus celui de la troisième course) et une attribution fausse (« l'effet du lot ») pour ce qui serait une instabilité d'exécution.
- Devrait être : ajouter un rejeu du lot 64 (une passe de 128 lignes par couche, coût négligeable) comme témoin C3b, et lire : « réfutée » seulement si C3 et C3b tenus ; si C3b est en défaut, issue « indéterminé (instabilité du lot 64 sur lui-même) », rapportée avec le nombre de tâches instables. Ajouter l'artefact correspondant aux essais (modèle dont la sortie change d'un appel à l'autre à forme donnée, au lot 64 seulement) : il faut « indéterminé » et non « réfutée ».

## Majeures

**M1. Aucun témoin, sur la carte, que l'ablation agit (et que « établie » ne vient pas d'une mesure sans effet).**
- Fichier : `audit_invariance_lot_v1.py` l. 120-127 ; préenregistrement § 3 (témoins).
- Écrit : C1 (formes), C2 (une perturbation de jeton se voit), C3 (rejeu).
- Problème : C2 protège indirectement (si la différence était identiquement nulle, la perturbation ne la changerait pas, C2 tomberait), mais ce n'est pas écrit comme tel et rien ne borne la taille de l'effet. De plus C1 est vrai par construction (la première dimension, 2×lot, diffère toujours) : il ne montre pas que le lot change le calcul interne, seulement qu'il change la forme d'entrée.
- Devrait être : un témoin C4 chiffré et rapporté, par couche : écart maximal absolu de `lc - la` par tâche strictement positif sur au moins 90 % des tâches (valeur à fixer au préenregistrement, avant la course) et son minimum, médian et maximum rapportés ; un défaut d'un témoin donne « indéterminé ». Pour la sensibilité au lot, rapporter aussi l'écart du lot 1 et du lot 7 au lot 16 (déjà calculé) en disant que si tous les écarts sont nuls, l'essai ne distingue pas « invariant » de « noyau insensible aux formes essayées » ; ou ajouter un témoin positif de variance au lot sur la carte (par exemple un produit matriciel bf16 de la même forme à 2 et à 128 lignes) afin que « établie » soit lue contre un cas où la carte varie réellement.

**M2. Le manifeste de la course porte la tranche B-α, le texte gelé B-α et l'entropie de B-α, pas l'essai.**
- Fichier : `b_alpha_lancer_v5.py` l. 393-399 (`configuration`) et l. 401-448 (`etape_preparer`, appel `creer_manifeste(… entropie=ENTROPIE, decisif=True, prereg=…texte-gele…)`), réutilisés tels quels par `audit_invariance_lot_v1.installer` (l. 180-186).
- Écrit : `tranche: "B-α"`, `prereg` = texte gelé de B-α (`34b88243…`), entropie 20261114, tâches `b-alpha-intervalles` et `b-alpha-intervalles-lot64`, `decisif: true`.
- Problème : le préenregistrement de l'essai (`6836df51…`) et l'entropie 20261117 n'apparaissent dans aucun manifeste (R1, R6, R9) ; l'entropie n'est que dans le fichier de détail. Un lecteur du manifeste croirait à une course de B-α.
- Devrait être : une étape `preparer` propre à l'essai (ou un remplacement de `base.configuration` et de l'appel de manifeste) qui consigne le préenregistrement de l'essai comme `prereg`, l'entropie 20261117, des tâches nommées pour l'essai, et `tranche: "audit-invariance"` ; sinon, au minimum, le dire dans le préenregistrement (§ 3 ou § 6) et dans le résultat de `audit-invariance` (champ `manifeste_declare_b_alpha`), et ajouter le chemin et l'empreinte du préenregistrement de l'essai au résultat de l'étape.

**M3. Le chemin de chargement réel (`charger is None`) n'est essayé nulle part avant la location.**
- Fichier : `audit_invariance_lot_v1.py` l. 149-163 ; `tests/test_neuron_lens_audit_invariance_lot_v1.py` (`test_etape_sur_contexte` passe `charger=`) ; essai à blanc (faux lanceur).
- Problème : `from_pretrained(base.<constante du modèle>)`, `.to("cuda")`, `sys.path.insert(voisin)`, `from neuron_lens.transport import decoder_stack`, `get_device_name` ne sont exécutés qu'une fois, sur la machine payante ; un défaut y fait échouer l'étape, d'où destruction et « aucune relance sans mot de la mère » (§ 5). Le code voisin importé n'a que `torch` et `functools` en tête de `transport.py`, donc le risque est faible mais il existe (chemin du voisin, `NEURON_LENS_MODEL`, nom du dossier du voisin).
- Devrait être : factoriser le chargement en une fonction paramétrée par le dépôt voisin, le nom du modèle et le périphérique, essayée sur le processeur avec un modèle miniature enregistré dans un dossier temporaire et un faux `neuron_lens/transport.py` calqué sur `decoder_stack` (sans exécuter le vrai code voisin), pour couvrir `sys.path`, la lecture de `config`, et l'écriture du détail ; et vérifier dans l'essai à blanc que `main` réel (`suite`, `jouer --etape preparer` sur le dépôt réduit) tourne, pas seulement le faux lanceur.

**M4. Valeur par défaut dangereuse de la branche des résultats, et nom d'exécution B-α imposé.**
- Fichier : `scripts/amorce_neuron_lens_audit_invariance_v1.sh`, l. 55 et l. 72 ; préenregistrement § 7 (branche `calcul/neuron-lens-audit-invariance-v1`).
- Écrit : `BRANCHE_RESULTATS=${BRANCHE_RESULTATS:-calcul/neuron-lens-b-alpha-v1}` ; `RUN_ID` doit finir par `-neuron-lens-b-alpha`.
- Problème : oubli de la variable = tentative de poussée vers la branche des résultats de la course B-α (refusée par divergence d'historique, mais l'amorce se prendrait alors le code 14 après avoir payé le montage) ; le nom d'exécution suggère une course B-α.
- Devrait être : défaut `calcul/neuron-lens-audit-invariance-v1` ; expression régulière de `RUN_ID` `…-neuron-lens-audit-invariance$` (et la même dans l'essai à blanc, l. ~64 et `lancer`, qui passe `RUN_ID="…-neuron-lens-b-alpha"`), à moins que la commande ne tienne au nom actuel : dans ce cas l'écrire au préenregistrement. L'essai à blanc devrait vérifier que l'amorce refuse la branche B-α.

## Mineures

**m1. Fenêtre de 9 positions et non de 8.** Préenregistrement § 3 (« fenêtre de 8 ») et module l. 38, 56 : la tranche `pos:pos+9` a 9 positions (`pos` plus 8 suivantes), comme `measure`. Devrait être : « fenêtre de 8 positions après la position ablatée, soit 9 lignes ». Effet sur la mémoire : voir d).

**m2. Citation de lignes inexacte.** Préenregistrement l. 18 et module l. 14, 56 : « l. 213-235 de la copie publiée ». À 849bfe16 la boucle d'ablation est aux l. 216-246 (crochet l. 229-233, passe l. 234-245) ; la copie corrigée par le correctif de graine est décalée de 8 lignes. Devrait être : « l. 216-246 du fichier à 849bfe16 (avant correctif) ». Même remarque pour « l. 256 de la copie » (§ 1) : l. 256 avant correctif, l. 264 après.

**m3. Comparaison au bit près en float32 seulement.** La course a produit des moyennes arrondies en demi-précision (`.half()`) et résumées après ; si l'essai trouve des écarts de float32, il ne dit pas si la course (au grain fp16) les aurait vus. Devrait être : rapporter aussi, par lot, la part des tâches identiques après arrondi en demi-précision de la différence, sans l'inclure dans le critère.

**m4. Étapes inutiles dans `telecharger-tokeniseur`.** `b_alpha_lancer_v5.py` l. 482-515 télécharge et contrôle aussi trois lentilles publiques de 1,04 Go chacune, sans lien avec l'essai : ≈ 3 Go de plus, deux échecs possibles de plus (hub Neuronpedia, empreintes), temps loué. Devrait être : le dire au devis (le poste 0,1 h le couvre mal) ou les retirer par une étape dédiée de l'essai.

**m5. Échéances du module et devis incohérents.** Module l. 33-34 : attendu 0,05 + 0,1 + 0,2 + 0,3 = 0,65 h, pire 1,8 h ; devis : attendu 0,3 à 0,5 h, pire 3,8 h (le pire cas du devis inclut l'installation, qui est dans l'amorce et non dans une étape). Sans conséquence sur la garde (`depassement_pire_cas` est informatif) mais le « attendu » des étapes dépasse celui du devis. Devrait être : aligner les deux, ou noter l'écart au § 7.

**m6. Essai à blanc : tables non comparées.** `essai_a_blanc_amorce_neuron_lens_audit_invariance_v1.sh` l. 61-62 et 87-90 : seule la liste d'étapes du faux lanceur est comparée à `audit_invariance_lot_v1.ETAPES` ; ses `JETON` et `EN_LIGNE` (codés en dur) ne sont pas comparés à `base.JETON` et `base.EN_LIGNE`, et le message « audits exceptés » est périmé (plus d'audits). Devrait être : comparer aussi ces deux tables, retirer la mention.

**m7. Textes périmés de l'amorce.** `amorce_neuron_lens_audit_invariance_v1.sh` l. 21 (« étapes du lanceur `b_alpha_lancer_v5` »), l. 154 (message de commit « Neuron Lens, B-α : … »), et fichiers d'état nommés `…-b-alpha` : cosmétique, mais ils brouillent la lecture de la branche de résultats. `CARTE_ATTENDUE` est facultative dans l'amorce (comme en B-α) ; l'étape ne vérifie pas la carte : le champ `carte` du résultat permet un contrôle a posteriori, à rappeler dans la commande (code 11 exige que la variable soit posée).

**m8. Essais trop larges.** `tests/test_neuron_lens_audit_invariance_lot_v1.py` l. 74 : pour `Sourd`, l'issue acceptée est « indéterminé » ou « réfutée » ; elle doit être exactement « indéterminé » (C2 en défaut, lot 64 identique). Il manque aussi l'artefact « le lot est ignoré par `differences` » (C1 doit tomber) et celui du non-déterminisme (B1).

## Détail de (b) : classements possibles
- « Établie à tort si le lot n'agit pas » : C1 couvre le cas où `lot` ne change pas la forme ; il ne couvre pas un noyau insensible à la forme (c'est alors la vraie réponse de l'essai, mais voir M1 pour la lire contre un témoin positif). Un crochet inactif est attrapé par C2 seulement par ricochet (M1).
- « Réfutée à tort par non-déterminisme » : oui pour le lot 64 (B1) ; non pour le lot 16 (C3).
- `lire_issue` suit le tableau du § 4 : indéterminé si C1 ou C3 en défaut ; établie si identique et C2 tenu ; réfutée sinon. « Réfutée » est lue même si C2 est en défaut, ce que le § 4 prévoit (C1 et C3 seulement). À garder, mais B1 ajoute C3b à la condition.
- Les trois couches sont exigées par `all(...)` : cohérent avec le § 4.

## Détail de (c) : remplacement des tables du lanceur v5
Vérifié, sans défaut propre :
- `installer` rebinde `ETAPES`, `PREREQUIS`, `ECHEANCES`, `AUDITS`, `ETAPE_FONCTIONS` dans l'espace de noms de `b_alpha_lancer_v5` ; toutes les fonctions du lanceur les lisent comme globales à l'appel (`verifier_environnement`, `suite`, `exiger_prerequis`, `jouer`, `main` avec `choices=ETAPES`), donc le remplacement prend effet. `AUDITS = {}` rend `suite` et `exiger_prerequis` sans audit. Réappel de `installer` idempotent.
- Prérequis : `telecharger-poids` dépend de `telecharger-tokeniseur` ; l'étape lit seulement `ctx.lire("telecharger-tokeniseur")["attendus"]` : aucune lecture de B0. `audit-invariance` dépend de `telecharger-poids`.
- Environnement : `audit-invariance` n'est ni dans `JETON` ni dans `EN_LIGNE` : sans clé et `HF_HUB_OFFLINE=1`, comme l'exige l'essai `test_installer_quatre_etapes` ; `GO_ID`, `NEURON_LENS_MODEL` et `HF_HOME` posés par l'amorce (`appel`). `EN_LIGNE` garde `corpus` et `audit-tout-negatif` : inoffensif. `suite` imprime `jeton`/`en-ligne` comme l'attend la boucle `courir`.
- Chargement hors ligne : `from_pretrained(base.<constante du modèle>)` sans révision explicite passe par le cache épinglé (`epingler` écrit `refs/main`), comme `measure`.
- Réserve : M2 (manifeste et `preparer` inchangés) et m4 (étapes de lentilles).

## Détail de (d) : devis
- Durée de l'essai : ≈ 177 000 jetons passés par couche (lot 16 : 3 séries × 4 passes de 32 lignes ; lot 64 : 1 passe de 128 lignes ; lot 1 : 64 passes de 2 lignes ; lot 7 : 10 passes de 14 lignes), ≈ 530 000 jetons sur trois couches, soit environ 8 pétaflops pour un modèle de 8 milliards ; quelques minutes sur une A100 (hors chargement des poids, 1 à 3 minutes). L'attendu 0,1 à 0,3 h et le pire cas 1,0 h sont conservateurs ; juste.
- Mémoire vive : une série = 64 × 9 positions × 128 256 × 4 octets ≈ 296 Mo (9 et non 8, m1). Par couche : 6 séries conservées (4 lots, rejeu, perturbée) ≈ 1,8 Go ; au passage de couche, `ref`, `rejeu` et `pert` de la couche précédente restent vivantes pendant que les quatre nouvelles séries se construisent : pic ≈ 2,1 Go, plus quelques temporaires de 5 Mo. Aucun risque vis-à-vis de la mémoire d'une instance ; mémoire de la carte : poids 16 Go plus, au lot 64 (128 lignes × 256), un crochet qui clone 0,94 Go et l'attention à masque ; sous 40 Go. Les empreintes hachent ≈ 25 Go au total (quelques dizaines de secondes) ; négligeable.
- Totaux du § 7 : attendu 0,1 + 0,1 + (0,1 à 0,3) = 0,3 à 0,5 h ; pire 2,2 + 0,6 + 1,0 = 3,8 h ; coût 0,19 à 0,31 USD (écrit 0,2 à 0,3) ; pire cas 3,8 × 0,62 = 2,36 USD, au-dessus du plafond, donc tronqué par la garde (écrit). Plafond 2 USD, compte rendu 1,20, arrêt dur 1,80 : 1,80 / 0,73 = 2,47 h ; minuterie à 90 % de 2 USD au prix 0,73 : 1,8 / 0,73 = 2,47 h (≈ 2,5 h, écrit). Le pire cas de 3,8 h ne peut donc pas être atteint : la minuterie coupe à ≈ 2,5 h ; l'amorce, avec deux installations sous 3 600 s chacune, peut consommer 2 h avant l'essai ; il resterait alors ≈ 0,5 h, ce qui reste suffisant. Ligne GO : 3,4 à 4,0 plus 2 = 5,4 à 6,0 sur 12 (écrit ≈ 5,8) : juste.
- L'attendu du montage (0,1 h = 6 minutes pour pip de torch avec ses bibliothèques CUDA, les essais et la carte) est serré ; un attendu de 0,15 à 0,2 h serait plus réaliste (coût : quelques centimes). Mineur.
- À vérifier côté mère (hors pièces) : la ligne `GO-2026-11-14-06` du registre, telle que lue dans cette branche, parle d'une RTX 4090 à 0,90 USD/h au plus ; l'usage d'une A100 à ≤ 0,73 USD/h doit être couvert par l'avenant que cite la commande (le `GO-2026-11-17-04` n'est pas dans `registres/go.md` de cette branche).

## À faire avant scellement
B1, M1, M2, M3, M4 ; m1, m2, m6, m8 faciles ; ensuite regénérer le dépôt réduit (v11 si le module change : R12, nouveau nom) et rejouer l'essai à blanc.
