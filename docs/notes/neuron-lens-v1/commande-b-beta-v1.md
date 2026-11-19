# Commande de location et de lancement de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct, nos lentilles R et S), sur une H100 SXM 80 Go — v1, sans ssh (proposée, **non exécutée**)

Écrite le 2026-11-18 par la session `session_01XJ6MgpKJHG5ue54rCpu4Ny` (reprise de la lecture par lentille neuronale ; mère
`session_01XJ6Mgr8BN6UanALsQatc5E`, R-3103), branche `claude/lentilles-b-beta-course-v1`. Reprend la forme de la commande v8 de la
tranche des lentilles publiques (`prep/neuron-lens-v1`, `commande-b-alpha-v8.md`, contre-lue deux fois) et les valeurs du devis v12 et du
texte gelé de cette tranche. **Rien ne part sans** : ce texte contre-lu ; le code de course employable après sa contre-lecture ; le relevé
de prix dans l'heure ; le mot explicite de Lazar sur la clé au moment de la commande (R-3151) ; la ligne de calcul inscrite par la mère sur
GO-2026-11-18-02 et son **feu écrit** ; le budget du 19 novembre (à partir de 23:00 UTC le 18) ; la fenêtre du 19 au 25 novembre.

## Pièces qui font foi
| pièce | chemin (branche `claude/lentilles-b-beta-course-v1` sauf mention) | empreinte |
|---|---|---|
| texte gelé de la tranche, scellé | `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` |
| addendum partie 1, v3 (avant toute donnée) | `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` |
| devis v12 (décisions de Lazar en tête) | `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md` | `41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1` |
| code des verdicts v4 (employable) | `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` | `8c07434f9db0e35e10eb806218da320bc0d6e404e41c4f60c495b35906d88b87` |
| code de course v1 (contrôles, lanceur, partie 2, amorce, dépôt réduit) | voir « Empreintes » en fin | — |
| ligne de décision | GO-2026-11-18-02 (`registres/go.md`, branche principale) ; R-3151 (clé) ; R-3171 (écarts au devis, routine) | — |

## Déclarations de forme (aucun seuil, aucune mesure, aucune issue du texte gelé touchés)
1. **Drowse 6.1.4 installé sans ses dépendances** (option (a) proposée à la mère le 2026-11-18, défaut sous 48 heures) : sa métadonnée
   demande `transformers>=5.22` ; l'addendum partie 1 (§ 5) fixe 5.18.0. La roue est téléchargée seule, son empreinte (`673ed2b4…`)
   vérifiée **avant** installation par l'amorce (code 18 sinon), installée `--no-deps` ; le lanceur revérifie version et empreinte à B0
   (arrêt sinon) ; les modules employés par le code voisin (`drowse.lens.store`, `jlens`, `key`) n'importent au chargement que torch et
   safetensors (graphe relevé sur le texte du paquet, sans l'exécuter) ; l'aller-retour de l'export (garde (o)) tranche sur la machine.
2. **Le code voisin est cloné sur la machine** au commit `849bfe16` (arbre `b22006e9…` exigé) par l'étape « preparer » du lanceur, au lieu
   d'être mis dans le dépôt réduit : l'essai du correctif (4) lit `git show HEAD:` et exige un vrai dépôt git à ce commit ; les correctifs
   (1) à (4) et (6) y sont appliqués **sans commit** (empreintes avant et après exigées).
3. **Artefacts de la garde (d) joués sur la machine à B0** (R-2710 interdit d'exécuter le code voisin dans le conteneur) : deux copies de
   l'essai du Llama miniature, l'une avec un test marqué sauté, l'autre avec le signe de l'estimation inversé ; chacune doit être vue en
   défaut, sinon arrêt.
4. **Nombre de tests exigé par essai** à B0 (écart = arrêt, sens sévère, sans effet en marche normale) : 7, 13, 8, 4 (essais repris de la
   tranche précédente, comptes relevés à sa partie 2), 10 (correctif (4)), 11 (Llama miniature) ; partie 1, § 4.
5. **Corpus d'activations comparé dès `05_act_corpus.py`** (mineure de la vérification de la partie 1) : même condition que la partie 2
   (§ 3), constatée plus tôt pour ne pas payer les comptes de jetons ; l'arrêt reste un nœud à la mère.
6. **Lecture des points fixes de la permutation (audit A4)** : recalculée par notre code (même générateur, même graine, même ordre que
   `reads_at_firings.py`), sans le code voisin.
7. Les trois écarts de forme notés par la vérification de la différence entre le brouillon 3 et le texte scellé (R-3176) : « scellé vers
   04:30 » pour 04:22:35Z ; la clause de licence de Drowse ajoutée sur demande de la mère ; le second lecteur qui s'est cru du même modèle.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur `vastai` 1.11.0 à `/home/user/vastai-env/bin/vastai` ; `vastai show user --raw > /dev/null` au code 0 (sortie jetée).
2. **Secrets présents, par leur longueur seulement** : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ] && [ ${#HF_TOKEN} -ge 8 ]` ; la clé
   d'accès au modèle n'est passée à la machine **que sur le mot explicite de Lazar au moment de la commande** (R-3151), relayé par la mère
   dans le feu ; sans ce mot, rien ne part. **Suivi prêt** : `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6
   verifier` (code 0) ; `… instances` (code 0, liste consignée : identifiants et états ; aucune instance de cette tranche).
3. **Crédit** (devis v12, § 5) : `can_pay` vrai, `has_billing` vrai, `billing_failed` faux (champ absent = arrêt) ; **crédit au moins égal
   au plafond de 75 USD en plus des autres lignes ouvertes** ; consigné.
4. **Relevé de prix dans l'heure qui précède la création** : `.venv/bin/python docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v3.py`
   (lecture seule, filtre complet du devis v12, § 3 : `gpu_name=H100_SXM num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200
   inet_down>=300 inet_up>=200 reliability>0.98 cuda_max_good>=13.0 rentable=true`) ; relevé versé avec son heure. **Offre retenue** : la
   moins chère dont le prix **avec 200 Go de stockage** (`dph_total + storage_cost × 200 / 720`) est **≤ 2,62 USD/h**, trafic sortant et
   entrant **≤ 0,04 USD/Go** chacun, et prix ≥ **1,85 USD/h** (règle du refus de la minuterie : sous lui, la minuterie dépasserait sa
   borne haute de 129 600 s ; armement à la borne haute non retenu) ; aucune → rien ne part, message à la mère (nœud : autre carte).
5. **Dépôt réduit** au commit de la course : `.venv/bin/python scripts/depot_reduit_neuron_lens_b_beta_v1.py <COMMIT_SOURCE> <dossier neuf>`
   → `rapport.json`, `liste-fichiers.sha256`, paquet ; **liste attendue : celle de l'essai à blanc** (une autre liste exige un nouvel essai) ;
   branche dédiée `course/neuron-lens-b-beta-reduit-v1` poussée (`git fetch <paquet> course:refs/heads/course/neuron-lens-b-beta-reduit-v1
   && git push origin course/neuron-lens-b-beta-reduit-v1`), `git ls-remote` égal au commit réduit ; `git ls-remote origin
   refs/heads/calcul/neuron-lens-b-beta-v1` **vide** (sinon arrêt).
6. **RUN_ID** fixé ici une fois pour toutes : `<AAAAMMJJ-HHMMSS>-neuron-lens-b-beta` (heure UTC de cette étape), le même à chaque relance.

## 1. Location (une seule instance), minuterie, garde, rappels
7. **Préavis d'une ligne à la mère** (offre, prix lu au relevé), puis création (image `python:3.12-bookworm` ; disque 200 Go) :
   ```
   date -u +%FT%TZ   # <ISO_CREATION>
   GO_ID=GO-2026-11-18-02 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 200 --label neuron-lens-b-beta \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN -e COMMIT_REDUIT=<COMMIT_REDUIT> -e COMMIT_SOURCE=<COMMIT_SOURCE> -e GO_ID=GO-2026-11-18-02 -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-b-beta-v1 -e PERIODE_POUSSE_S=600 -e CARTE_ATTENDUE=HBM3" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-b-beta-reduit-v1 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_beta_v1.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   `<COMMIT_REDUIT>` et `<COMMIT_SOURCE>` **lus par programme** dans `rapport.json` (40 caractères vérifiés), jamais retapés. Les secrets ne
   sont développés que par le shell du lancement (dans `--env`). Identifiant et heure consignés dans
   `docs/notes/neuron-lens-v1/pids-b-beta-v1.txt`. Échec de création → `instances`, destruction éventuelle (étape 15), message.
   **Toute branche d'échec des étapes 7 à 10 : destruction immédiate**, préavis d'une ligne au moment du geste.
8. **Prix lu sur l'instance** : `… suivi_vast_v6 instance <ID>` → `dph_total` (stockage compris) **≤ 2,62** et **≥ 1,85** exigés ; trafic
   relu ≤ 0,04 USD/Go ; carte H100 SXM (`gpu_name`) ; l'amorce exige « HBM3 » dans le nom de la carte (valeur sans espace, passée dans `--env` ; nom attendu « NVIDIA H100 80GB HBM3 ») ; sinon destruction (étape 15) et message. Ce prix lu (<PRIX>) sert aux étapes 9 et 10.
9. **Minuterie v4** par identifiant, aussitôt (R10), comptée depuis la création :
   `D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 75 --frais-fixes 1.0 --debut <ISO_CREATION>)`
   (D = (67,5 − 1,0) / prix lu, tronquée à la seconde : 91 374 s au prix exigé exact) ; lancement détaché de
   `scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai <fichier PID>` comme à la commande v8, PID lu
   dans le fichier écrit par la minuterie (jamais `$!`), vérifié par `ps -p … -o args=` ; non armée → destruction, message.
10. **Garde de dépense v4** détachée : `garde_depense_v4 --instance <ID> --prix-h <PRIX> --plafond 75 --debut <ISO_CREATION> --frais-fixes 1.0
    --journal docs/notes/neuron-lens-v1/journal-depense-b-beta-v1.jsonl` (PID écrit par elle-même avant `exec`, comme à la v8) ; compte rendu
    à la mère à **45,0 USD** ; destruction réessayée et vérifiée à **67,5 USD** ; trafic réservé 1,0 USD (lieu L1).
11. **Rappels** (`send_later`) : à **12,9 h** de location, compte rendu en durée (haut de l'attendu avec L1) ; à **24,1 h**, rappel (pire cas
    avec L1) ; à **80 % de D** : « vérifier et détruire l'instance <ID> ». **Veille** des PID de la minuterie et de la garde toutes les
    5 minutes (comme à la v8) ; une ligne « MORTE » → réarmement sur la même échéance absolue et message.

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_beta_v1.sh`, sans intervention)
12. Commit égal à `COMMIT_REDUIT` (code 10) ; arbre propre au premier départ (code 10) ; RUN_ID et GO_ID valides (code 17) ; première
    poussée vérifiée (code 14) ; carte lue par `nvidia-smi` avant `pip` (code 11) ; `pip` 26.2.2 puis les versions épinglées
    (`requirements-neuron-lens-b-beta-v1.txt`), roue de Drowse téléchargée seule et vérifiée (code 18), installée sans dépendances (code 16
    sur échec ou délai de 3 600 s) ; carte vue par `torch` (code 11) ; essais de nos modules (code 12 sur échec, essai sauté ou arbre
    sali) ; puis les étapes du lanceur `b_beta_lancer_v1`, dans l'ordre de `suite` (texte gelé, P.3) :
    `preparer` (en ligne : clone du voisin, correctifs sans commit, copie à part pour le banc, manifeste R9) → `telecharger-tokeniseur`
    (**clé**) → `b0` (essais, artefacts de (d), lentilles de Neuronpedia, Drowse) → `telecharger-poids` (**clé** ; ensuite retirée de la
    course, vérifiée par son nom) → `corpus-ajustement` (en ligne ; garde (i) ; P.1 : 932, 466 et 466, `a6afd972…`) → `partie2-b0` (écart =
    arrêt avant l'ajustement) → `banc` (copie à part ; > 23,6 s : arrêt ; > 14,2 s : compte rendu) → `ajustement-R` → `ajustement-S` (gardes
    (q), (g), (h)) → `export` (gardes (e), (h), (n), (o)) → `corpus-activations` (en ligne ; fichiers comparés à la partie 1 ; garde (i)) →
    `comptes-jetons` (une seule fois) → `partie2-corpus` (écart = arrêt) → `lens-compare` (garde (r)) → `fumee` → `passe` → `pilotes`
    (gardes (k) hub, (r), (p)) → `measure` (garde (i) de nouveau, (p)) → `score` → `grandeurs` (n recalculé, fidèle à `score`) → `reads`
    (liens durs du correctif (5), gardes (s), (k) nos noms, (r)) → `declencheurs` → `audit-relance` (A1, A5) et `audits-controles` (A2,
    A3, A4) s'ils sont déclenchés, dans l'heure réservée → `verdicts` (fichier unique, intervalles). **Toute chaîne en défaut** écrit le
    fichier de verdicts « chaîne en défaut » puis arrête (code 20). Poussées vérifiées sur `calcul/neuron-lens-b-beta-v1` toutes les
    10 minutes, à la fin et à tout arrêt ; balayage des secrets avant chaque commit ; fichiers de plus de 95 Mo exclus (ajustements,
    exports, activations, `-causal.pt` restent sur la machine et disparaissent avec elle : lieu L1).

## 3. Suivi, retour et destruction (conteneur de la session)
13. Suivi comme à la v8 (`logs`, `instance`, état poussé ; PID de la minuterie et de la garde) ; **course figée** → arrêt ; **crédit** relu
    à chaque contrôle ; dépassement du pire cas d'une étape → compte rendu. **La session ne lit aucun résultat de mesure** ; elle lit
    seulement les fichiers d'état, les arrêts (`arret-*.json`, message court) et l'existence du fichier de verdicts (sans l'ouvrir).
    Règle de destruction : celle de la v8 (table de la dernière ligne du journal et de l'état poussé), avec « b-beta » pour « b-alpha » ;
    **pas sans la mère** si la poussée finale échoue ou si un fichier de résultats a été exclu.
14. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque `diag/<run_id>/b-beta-*.json` ; compagnons de la
    partie 2, des grandeurs, des résumés de `score`, de `lens_compare`, de `reads_at_firings` et du fichier de verdicts vérifiés ; copie
    sur la branche de la tranche ; commit ; poussée. **La lecture reste à un lecteur neuf, sur un plan scellé** (P.7).
15. **Préavis d'une ligne à la mère, puis destruction** : `vastai destroy instance <ID> -y < /dev/null` ; `… suivi_vast_v6 absente <ID>
    --non-vide` au code 0 ; minuterie et garde arrêtées **par PID** après `ps -p <PID> -o args=` ; rappels annulés ; journaux et fichiers de
    PID commités ; crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et `registres/depenses.md`. Intouchables (devis
    v12, § 5) jamais touchés.

## Essai à blanc (sans location), à faire avant la demande de feu
À écrire et jouer : l'amorce v1 en mode jouet sur le dépôt réduit, faux lanceur (étapes égales à celles du lanceur v1), cas nominal,
relance, reprise après arrêt brutal, arrêt 20, garde de carte (cas sain « NVIDIA H100 80GB HBM3 » ; artefacts « NVIDIA H100 PCIe »,
« NVIDIA A100-SXM4-80GB »), garde de la roue de Drowse (cas sain ; roue d'une autre empreinte : code 18). **Non fait à ce jour.**

## Réserves
- Aucun essai du code voisin n'a tourné dans le conteneur (R-2710) : tout se constate à B0, sur la machine.
- Les étapes réelles du lanceur qui touchent la machine (ajustement, export, mesure, score, lectures) ne sont essayées qu'avec des doubles ;
  leurs appels au code voisin sont vérifiés par lecture seulement.
- Mémoire de l'ajustement de Llama non mesurée (devis v12, § 6 : 80 Go laissent une marge large).
- `HF_TOKEN` : exposition résiduelle déclarée comme à la v8 (configuration de l'instance chez le loueur, processus d'entrée de l'amorce) ;
  révocation recommandée à Lazar après la course.

## Empreintes
Remplies à la version employable du code de course (après sa contre-lecture) : contrôles, lanceur, partie 2, amorce, dépôt réduit, essais.
