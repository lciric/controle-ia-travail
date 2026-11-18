# Commande de location et de lancement de la tranche de l'ajustement de nos lentilles (lecture par lentille neuronale, Llama 3.1 8B Instruct, nos lentilles R et S), sur une H100 SXM 80 Go — v4, sans ssh (proposée, **non exécutée**)

Session `session_01XJ6MgpKJHG5ue54rCpu4Ny` (lecture par lentille neuronale ; mère `session_01XJ6Mgr8BN6UanALsQatc5E`, R-3103), branche
`claude/lentilles-b-beta-course-v1`, 2026-11-18. **v4** = v3 (`commande-b-beta-v3.md`, `3dd57cc4…`, archivée, jamais jouée) corrigée selon sa vérification courte
(`correctifs-b-beta/verification-courte-commande-b-beta-v3.md`, `af7966c8…` : à corriger légèrement, 1 majeur, 4 mineurs ; reprise en fin) ;
prix déclaré à la garde = prix plafond de la commande (mère, 07:17Z). **v3** = v2 (`commande-b-beta-v2.md`, `1e33efdf…`, archivée, jamais jouée) corrigée selon
sa vérification par un agent neuf (`correctifs-b-beta/verification-code-de-course-b-beta-v2.md`, `4d24a10a…` : commande à corriger, 4 majeurs,
6 mineurs ; table de reprise en fin) ; **texte autonome** : rien n'est renvoyé à une autre commande. Forme reprise de la commande v8 de la
tranche des lentilles publiques (`prep/neuron-lens-v1`, contre-lue deux fois) ; valeurs du devis v12 et du texte gelé de cette tranche.

**Rien ne part sans** : ce texte vérifié ; le **feu écrit de la mère** (« pas de départ sans mon mot », 07:16Z) ; la **condition de crédit**
(§ 0, point 3) ; le relevé de prix dans l'heure ; le **mot explicite de Lazar sur la clé** au moment de la commande (R-3151), relayé par la
mère ; la ligne de calcul de GO-2026-11-18-02 inscrite par la mère, dans la fenêtre du 19 au 25 novembre (budget du 19 à partir de 23:00 UTC
le 18) ; l'ordre de Lazar (GO-2026-11-18-18) : **après le départ de l'étape B bis**.

## Demande de feu (résumé)
| objet | valeur |
|---|---|
| plafond (ligne GO-2026-11-18-02, lieu L1, « avec une relance ») | **75 USD** ; compte rendu à **45,0 USD** (60 %) ; arrêt dur à **67,5 USD** (90 %) ; trafic réservé 1,0 USD |
| coût attendu | ≈ **35 USD** au haut de l'attendu (12,9 h × 2,62 + 1,0) ; pire cas **64,1 USD** (24,1 h) ; arrêt dur à 67,5 |
| durée | attendue **jusqu'à 12,9 h** (haut de l'attendu avec L1, devis v12 § 4) ; pire cas **24,1 h** ; minuterie 25,38 h au prix exigé exact |
| carte et prix plafond | **H100 SXM 80 Go** (« NVIDIA H100 80GB HBM3 »), machine vérifiée ; **≤ 2,62 USD/h stockage de 200 Go compris**, **≥ 1,85 USD/h** ; trafic ≤ 0,04 USD/Go chacun ; débit montant ≥ 200 Mbit/s |
| condition de crédit | crédit lu − (pire cas restant de l'étape B bis + témoin de Bailey + disques des autres sessions) − 75 ≥ **8 USD** ; sinon départ après la fin de l'étape B bis, crédit relu ; et `can_pay`, `has_billing` vrais, `billing_failed` faux |

## Pièces qui font foi (branche `claude/lentilles-b-beta-course-v1`)
| pièce | chemin | empreinte |
|---|---|---|
| texte gelé de la tranche, scellé | `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` |
| addendum partie 1, v3 | `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` |
| devis v12 | `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md` | `41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1` |
| code des verdicts v4 et ses essais (82) | `src/controle_ia/neuron_lens/verdicts_b_beta_v4.py` ; `tests/test_neuron_lens_verdicts_b_beta_v4.py` | `8c07434f…` ; `1b63c8cb…` |
| contrôles v2 | `src/controle_ia/neuron_lens/controles_b_beta_v2.py` | `ddc36c55a6b9bdc7…` (compagnon) |
| lanceur v2 | `src/controle_ia/neuron_lens/b_beta_lancer_v2.py` | `65081931e19ee493…` |
| partie 2 v2 | `src/controle_ia/neuron_lens/addendum_partie2_b_beta_v2.py` | `9baaea3577527a69…` |
| amorce v2 | `scripts/amorce_neuron_lens_b_beta_v2.sh` | `a50a0eb54e93f1cd…` |
| dépôt réduit v2 | `scripts/depot_reduit_neuron_lens_b_beta_v2.py` | `36ee3a5bf02874ce…` |
| exigences v2 | `requirements-neuron-lens-b-beta-v2.txt` | `8c9016c2ab658844…` |
| essais embarqués | `tests/test_neuron_lens_{controles_b_beta_v2,b_beta_lancer_v2,etapes_b_beta_v2,montage_b_beta_v2}.py` | `2201f998…`, `3a244015…`, `896846b0…`, `ea38f6b7…` |
| essais complémentaires, joués dans le conteneur, non embarqués | `tests/test_neuron_lens_etapes_b_beta_v3.py` ; `…_v4.py` | `64ed82b6…` ; compagnon |
| essai à blanc de l'amorce v2 et son journal | `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v1.sh` ; `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-b-beta-v1.txt` | `4de3be54…` ; `5ccc3383…` |
| relectures | contre-lecture du code v1 `2276477b…` ; vérification du code v2 et de la commande v2 `4d24a10a…` | — |
Les empreintes complètes sont dans les compagnons `.sha256` ; le lanceur revérifie à `preparer` celles du texte gelé, de l'addendum, du
devis, de la série repère, du code des verdicts et de ses essais, des correctifs et des essais de B0.

## Déclarations de forme (aucun seuil, aucune mesure, aucune issue du texte gelé touchés ; tout ajout est un arrêt dans le sens sévère)
1. **Drowse 6.1.4 installé sans ses dépendances** (R-3198) : sa métadonnée demande `transformers>=5.22` ; l'addendum (§ 5) fixe 5.18.0.
   La roue est téléchargée seule et son empreinte (`673ed2b4…`) vérifiée **avant** installation (amorce, code 18), installée `--no-deps` ;
   le lanceur revérifie version et empreinte à B0. Les modules employés par le code voisin importent torch et safetensors, et PyYAML par
   `drowse.lens.sources` (sur le chemin de `save_lens` et `load_local_lens`) : PyYAML est écrit aux exigences (sans version exigée,
   relevée en partie 2) ; un processus enfant importe à B0 exactement ce que le code voisin emploie (arrêt sur tout échec, avant
   l'ajustement).
2. **Code voisin cloné sur la machine** au commit `849bfe16` (arbre `b22006e9…` exigé) par `preparer` : l'essai du correctif (4) lit
   `git show HEAD:` ; correctifs (1) à (4) et (6) appliqués **sans commit**, empreintes avant et après exigées.
3. **Artefacts de la garde (d) joués à B0** sur deux copies de l'essai du Llama miniature (un test marqué sauté ; le signe de
   l'estimation inversé **dans l'assertion** de l'essai, non dans un terme de l'estimateur) : chacun doit être vu en défaut, sinon arrêt.
4. **Nombres exigés** (écart = arrêt) : tests passés par essai de B0 (7, 13, 8, 4, 10, 11) et **82** essais du code des verdicts (addendum,
   § 4) ; **33** tables des pilotes (32 couches et les têtes) ; **28 672** pôles par couche à la comparaison des lentilles (M.2) ; contrôle
   des moitiés d'A2 et A3 exigé **à chacune des 31 couches** `out` (le texte dit « exports des moitiés d'empreintes différentes » ;
   lecture plus stricte, déclarée).
5. **Corpus d'activations comparé dès `05_act_corpus.py`** (même condition que la partie 2, § 3, constatée plus tôt).
6. **Points fixes de la permutation (A4)** recalculés par notre code (même générateur, graine et ordre que `reads_at_firings.py`).
7. **Banc à trois documents par lentille, le deuxième lu** (R-3220, décidé par la mère) : `02_fit.py` écrit le fichier (≈ 8,4 Gio) avant
   d'imprimer le temps du dernier document ; le troisième absorbe l'écriture. Temps lu à une décimale (23,64 s s'imprime « 23.6 »).
8. **Aller-retour d'un export de Drowse dans la copie du banc, avant l'ajustement** : `04_export_rlens.py`, `load_lens`, garde (o) ; échec =
   arrêt avant l'ajustement.
9. **Export entre les deux ajustements** (P.3 : « à la fin de chaque ajustement […] → export »).
10. Gardes (a) à (c), (e), (j) jugées dès l'étape des grandeurs ; garde (s) au premier lancement seulement (à une relance de la machine,
   des sorties de cette course-ci : arrêt simple, nœud — forme permissive déclarée) ; différences entre moitiés par `Accumulator.split_half`
   du dépôt lui-même (la recopie versée à côté) ; contrôle (2) d'A1 et A5 lu « dose de pilotage strictement positive » ; un export
   interrompu (sans manifeste) est supprimé et refait à la reprise (non consigné au résultat : déclaré) ; un arrêt entre l'écriture du
   fichier de verdicts et celle du fichier des intervalles laisse la course finie sans intervalles (rapportés, sans critère : déclaré).
11. Trois écarts de forme de la vérification de la différence entre le brouillon 3 et le texte scellé (R-3176).
12. **Non essayés avant la course, déclarés** : le code 18 de l'amorce (roue de Drowse d'une autre empreinte ; pas jouable en mode d'essai ;
   le contrôle du lanceur à B0 l'est) ; un artefact isolé de la garde (h) à l'export (couvert avec (e) et (o)) ; le vrai code voisin et le
   vrai Drowse (R-2710 : seulement sur la machine).

## Préambule P, intouchables, règles
**P** (le shell ne garde rien d'un appel à l'autre) : `cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`
**Intouchables** (jamais arrêtées, jamais détruites) : 58936096, 58936099, 58936100 (N-009) ; 60988826 ; 61049303 et le serveur
`sauvegarde-temoin-bailey-v2` ; `poste-temoin-bailey-*` ; 60480302, 60599797, 60670453 ; **toute instance d'une autre session**, dont celles
de l'étape B bis et de l'organisme. **Jamais** de `vastai show … --raw` imprimé (la configuration porte les secrets) : tout passe par
`suivi_vast_v6`. Secrets lus par leur nom seulement. **Préavis d'une ligne à la mère** avant tout geste à risque de refus (création avec les
secrets, destruction manuelle), sans attendre de signal (R-2864, R-2883) ; tout refus d'une permission, du crochet ou du classifieur : ni
rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère. **Registre des GO** : `registres/go.md` de la branche principale (réparé,
`081bc453` ou plus récent) fusionné dans la branche de travail avant la création (la garde de calcul du crochet le lit).

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : s'il manque, `python3 -m venv /home/user/vastai-env && /home/user/vastai-env/bin/pip install -q vastai==1.11.0` ;
   P, puis `vastai --version` = 1.11.0 et `vastai show user --raw > /dev/null` au code 0 (sortie jetée).
2. **Secrets présents, par leur longueur** : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ] && [ ${#HF_TOKEN} -ge 8 ]` ; sinon arrêt, message.
   **Suivi prêt** : `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 verifier` → code 0 ; `… instances` → code 0,
   liste consignée (identifiants et états seulement ; aucune instance de cette tranche attendue).
3. **Crédit** : `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print({k: d.get(k) for k in ("credit", "can_pay", "has_billing", "billing_failed")})'`
   → `can_pay` vrai, `has_billing` vrai, `billing_failed` faux (champ absent ou nul = arrêt) ; **condition de la mère** :
   `credit − (pire cas restant de l'étape B bis + témoin de Bailey + disques) − 75 ≥ 8` ; les trois montants entre parenthèses sont
   **donnés par la mère** dans le feu (la session ne lit pas l'étape B bis) ; sinon rien ne part, attente de la fin de l'étape B bis et
   nouveau mot de la mère. Consigné.
4. **Relevé de prix dans l'heure qui précède la création** :
   `PYTHONPATH=src .venv/bin/python docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v3.py docs/notes/neuron-lens-v1/devis-b-beta/releve-prix-vast-h100-<AAAAMMJJTHHMMSSZ>-v4.tsv`
   (lecture seule ; filtre complet du devis v12 § 3) ; le relevé est scellé (`python -m controle_ia.scellement sceller <tsv>`) et versé.
   **Offre retenue**, lue dans les colonnes du relevé (`prix_avec_200_go`, `inet_up_cost_usd_go`, `inet_down_cost_usd_go`, `inet_up_mbit`,
   `verification`) et non dans les colonnes d'options du script (calculées pour d'autres couples prix-plafond, dont 72 USD) : la moins chère
   dont le prix avec 200 Go est ≤ 2,62 et ≥ 1,85 USD/h, trafic sortant et entrant ≤ 0,04 USD/Go, débit montant ≥ 200 Mbit/s, machine
   vérifiée ; aucune → rien ne part, message (nœud : autre carte). **Le trafic est celui de l'offre au relevé** (la même machine ; l'outil de
   suivi ne restitue pas ces champs de l'instance, et `show … --raw` n'est jamais imprimé) : relevé dans l'heure, il fait foi.
5. **Dépôt réduit** : `.venv/bin/python scripts/depot_reduit_neuron_lens_b_beta_v2.py <COMMIT_SOURCE> <dossier neuf>` → `rapport.json`,
   `liste-fichiers.sha256`, paquet. **Liste attendue : `791af13d9f248cabf69d337d20d0dfe9734d77c31061c6ba6c04b86a1df624c4`** (83 fichiers,
   celle de l'essai à blanc ; une autre liste exige un nouvel essai à blanc) ; `<COMMIT_SOURCE>` = commit de la branche qui porte cette
   commande, ses pièces de course identiques à `43627705` (la liste le prouve). Branche `course/neuron-lens-b-beta-reduit-v2` poussée
   (`git fetch <paquet> course:refs/heads/course/neuron-lens-b-beta-reduit-v2 && git push origin course/neuron-lens-b-beta-reduit-v2`) ;
   `git ls-remote origin refs/heads/course/neuron-lens-b-beta-reduit-v2` = commit réduit ; `git ls-remote origin
   refs/heads/calcul/neuron-lens-b-beta-v1` **vide** (sinon arrêt).
6. **RUN_ID** fixé une fois pour toutes : `<AAAAMMJJ-HHMMSS>-neuron-lens-b-beta` (heure UTC de cette étape), le même à chaque relance.

## 1. Location (une seule instance), minuterie, garde, rappels
7. **Préavis d'une ligne à la mère** (offre, prix au relevé), puis P et :
   ```
   date -u +%FT%TZ   # <ISO_CREATION>, relevée dans la même commande
   GO_ID=GO-2026-11-18-02 vastai create instance <OFFRE> --raw --image python:3.12.16-bookworm --disk 200 --label neuron-lens-b-beta \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN -e COMMIT_REDUIT=<COMMIT_REDUIT> -e COMMIT_SOURCE=<COMMIT_SOURCE> -e GO_ID=GO-2026-11-18-02 -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-b-beta-v1 -e PERIODE_POUSSE_S=600 -e CARTE_ATTENDUE=HBM3" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-b-beta-reduit-v2 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_beta_v2.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   Image **épinglée** `python:3.12.16-bookworm` (l'étiquette existe au registre public, relevée le 2026-11-18 ; l'amorce exige python
   3.12.16, code 19 sinon). `<COMMIT_REDUIT>` et `<COMMIT_SOURCE>` **lus par programme** dans `rapport.json` (40 caractères vérifiés),
   jamais retapés. `CARTE_ATTENDUE=HBM3` : valeur sans espace (passée dans `--env`) ; le nom attendu est « NVIDIA H100 80GB HBM3 », la
   recherche ne rend que des H100 SXM (`gpu_name=H100_SXM`). Les secrets ne sont développés que par le shell du lancement (et figurent, le
   temps de la création, dans les arguments du processus de l'outil dans le conteneur : déclaré). Entrée idempotente : à une relance, le
   clone est sauté et l'amorce relit son état. → `echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-b-beta-v1.txt`.
   Échec (pas de `new_contract`, ou `success` faux) → `instances`, destruction éventuelle (étape 15), message.
   **Toute branche d'échec des étapes 7 à 10 : destruction immédiate** (étape 15), préavis d'une ligne au moment du geste ; si une attente
   devait survenir, poser d'abord la minuterie puis la garde.
8. **Instance relue** : `… suivi_vast_v6 instance <ID>` → `dph_total` (stockage compris) **≤ 2,62 et ≥ 1,85** ; `gpu_name` H100 SXM ;
   identifiant de machine égal à celui de l'offre retenue (trafic de l'étape 4) ; sinon destruction et message. Ce prix lu est <PRIX>. Si la lecture échoue deux fois : destruction.
9. **Minuterie v4** par identifiant, aussitôt (R10), comptée depuis la création (P, puis) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 75 --frais-fixes 1.0 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-b-beta-v1.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-b-beta-v1.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v4 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-beta-v1.txt
   ```
   L'outil imprime la **durée restante** depuis `<ISO_CREATION>` : D totale = (67,5 − 1,0) / prix lu × 3 600, tronquée — **91 374 s**
   (25,38 h) à 2,62, 129 405 s à 1,85 (bornes de la v4 : 600 à 129 600 s) — moins le temps écoulé depuis la création.
   PID lu dans le fichier écrit par la minuterie, **jamais** `$!`. Non armée → destruction, message.
10. **Garde de dépense v4**, détachée, son PID écrit par elle-même avant `exec` (P, puis) :
    ```
    F=docs/notes/neuron-lens-v1/pid-garde-b-beta-v1.txt; rm -f "$F"
    setsid nohup bash -c 'echo $$ > "$0"; exec env PATH=/home/user/vastai-env/bin:$PATH PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --instance <ID> --prix-h 2.62 --plafond 75 --debut <ISO_CREATION> --frais-fixes 1.0 --journal docs/notes/neuron-lens-v1/journal-depense-b-beta-v1.jsonl' "$F" \
      >> docs/notes/neuron-lens-v1/garde-b-beta-v1.log 2>&1 < /dev/null &
    sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep garde_depense_v4 && echo "$(date -u +%FT%TZ) garde PID $P instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-beta-v1.txt
    ```
    **Prix déclaré à la garde : le prix exigé, 2,62 USD/h** (tranché ici, devis v12, décision 1 et § 5 ; choix de la v9, m-8) : la garde
    estime la dépense au plus grand du prix déclaré et du prix lu ; une lecture en échec retombe sur 2,62, la borne des 67,5 USD tient donc
    pendant une panne de lecture pour tout prix réel ≤ 2,62 ; au prix déclaré, l'arrêt dur tombe à 25,38 h, **après** le pire cas de 24,1 h
    (marge 1,3 h ; la troncature décrite au devis ne valait qu'à 3,00 USD/h et 82 USD). Une offre moins chère n'allonge pas la course
    au-delà de 25,38 h (la garde arrête ; la minuterie, plus longue, reste le filet). Compte rendu à **45,0 USD**, destruction réessayée et
    vérifiée à **67,5 USD** (code 4 et message immédiat si elle échoue).
11. **Rappels** (`send_later`) : (a) à **12,9 h** de location, compte rendu en durée (haut de l'attendu avec L1) ; (b) à **80 % de D**
    (20,3 h, 73 099 s, au prix exigé exact), rappel « vérifier » : minuterie et garde vivantes, avancement, la mère décide (pas de
    destruction : le pire cas de 24,1 h est au-delà) ; (c) à **24,1 h**, rappel du pire cas : sans fin de course, la mère décide. Puis commit et
    poussée de `pids-b-beta-v1.txt`. **Veille** en tâche de fond (2 h au plus, relancée à chaque contrôle), P puis :
    ```
    for i in $(seq 1 24); do
      for n in "minuterie minuterie_destruction_neuron_lens_v4" "garde garde_depense_v4"; do set -- $n
        P=$(cat docs/notes/neuron-lens-v1/pid-$1-b-beta-v1.txt 2>/dev/null)
        if [ -n "$P" ] && ps -p "$P" -o args= | grep -q "$2"; then s=vivante; else s=MORTE; fi
        echo "$(date -u +%FT%TZ) veille $1 PID ${P:-absent} $s" >> docs/notes/neuron-lens-v1/veille-b-beta-v1.log
      done; sleep 300
    done
    ```
    Une ligne « MORTE » (redémarrage du conteneur de la session) → réarmement aussitôt par les étapes 9 et 10 **sur la même échéance
    absolue** (D recomptée depuis `<ISO_CREATION>` : `garde_depense_v4 --minuterie-seulement` avec la même `--debut`), PID relus dans les
    fichiers, arguments vérifiés ; message à la mère. À chaque réveil de la session, minuterie et garde vérifiées par leur PID.

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_beta_v2.sh`, sans intervention)
12. Commit égal à `COMMIT_REDUIT` (code 10) ; arbre propre au premier départ (code 10) ; RUN_ID et GO_ID valides (code 17) ; première
    poussée vérifiée (code 14) ; carte lue par `nvidia-smi` avant `pip` (code 11) ; **python 3.12.16 lu avant `pip`** (code 19) ; `pip`
    26.2.2 puis les versions épinglées (`requirements-neuron-lens-b-beta-v2.txt`), roue de Drowse téléchargée seule et vérifiée (code 18),
    installée sans dépendances (code 16 sur échec ou délai de 3 600 s) ; carte vue par `torch` (code 11) ; essais de nos modules (code 12
    sur échec, essai sauté ou arbre sali) ; puis les étapes du lanceur `b_beta_lancer_v2` dans l'ordre de `suite` (`ETAPES`) :
    `preparer` (en ligne : clone du voisin, correctifs sans commit, copie à part pour le banc, manifeste R9) → `telecharger-tokeniseur`
    (**clé**) → `b0` (essais et leurs nombres, artefacts de (d), lentilles de Neuronpedia, Drowse : version, empreinte, **import**) →
    `telecharger-poids` (**clé** ; ensuite retirée de la course, vérifiée par son nom) → `corpus-ajustement` (en ligne ; garde (i) ; P.1 :
    932, 466 et 466, `a6afd972…`) → `partie2-b0` (écart = arrêt avant l'ajustement) → `banc` (copie à part ; trois documents, le deuxième
    lu : > 23,6 s arrêt, > 14,2 s compte rendu ; **aller-retour de Drowse**) → `ajustement-R` → **`export`** (gardes (e), (h), (n), (o)) →
    `ajustement-S` (gardes (q), (g), (h) à chaque ajustement) → `corpus-activations` (en ligne ; fichiers comparés à la partie 1 ; garde (i))
    → `comptes-jetons` (une seule fois ; jeton de début) → `partie2-corpus` (écart = arrêt) → `lens-compare` (garde (r) ; 28 672 pôles) →
    `fumee` → `passe` → `pilotes` (gardes (k) hub, (r), (p) ; 33 tables) → `measure` (garde (i) de nouveau, (p)) → `score` → `grandeurs` (n
    recalculé, fidèle à `score` ; gardes (a) à (c), (e), (j)) → `reads` (garde (s), liens durs du correctif (5), (k) nos noms, (r)) →
    `declencheurs` → **`audits-controles`** (A2, A3, A4) puis **`audit-relance`** (A1, A5) s'ils sont déclenchés, dans l'heure réservée
    (« non joué » sinon) → `verdicts` (fichier de verdicts unique, puis le fichier des intervalles). **Toute chaîne en défaut** écrit le
    fichier de verdicts « chaîne en défaut » puis arrête (code 20). Poussées vérifiées sur `calcul/neuron-lens-b-beta-v1` toutes les 10
    minutes, à la fin et à tout arrêt ; balayage des secrets avant chaque commit ; fichiers de plus de 95 Mo exclus (ajustements, exports,
    activations, `-causal.pt` restent sur la machine et disparaissent avec elle : lieu L1).

## 3. Suivi, retour et destruction (conteneur de la session)
13. Suivi : `… suivi_vast_v6 logs <ID> 40`, `… instance <ID>`, état poussé de la branche des résultats, `ps -p` sur les PID ; **course
    figée** (devis v12 § 4 ; l'outil de suivi ne restitue pas l'usage de la carte) : l'état poussé n'avance plus depuis **30 minutes** et la
    fin du journal (`logs <ID> 40`) est inchangée entre deux contrôles distants d'au moins 30 minutes → arrêt (étape 15, préavis) ;
    **crédit** relu à chaque contrôle : **< 1 USD → arrêt** (devis v12 § 5) ; crédit qui ne laisserait plus 8 USD au-dessus du pire cas
    restant de l'étape B bis (montants donnés par la mère) → message immédiat à la mère, qui décide ; dépassement du pire cas d'une étape (`depassement_pire_cas`,
    ou étape en cours depuis plus que son pire cas) → compte rendu ; la durée de location se compte depuis `<ISO_CREATION>`. **La session ne
    lit aucun résultat de mesure** : seulement l'état poussé, les arrêts (`arret-*.json`, message court), les relevés de la partie 2 (écarts)
    et l'**existence** du fichier de verdicts, sans l'ouvrir.
    **Règle de destruction**, sur la **dernière ligne** du journal et l'**état poussé** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » ou `fatal:` de git sans ligne `AMORCE` | aucun | aussitôt (étape 15) |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt |
    | « fin : arret code N (…) », course non lancée (N = 10, 11, 12, 13, 14, 16, 17, 18, 19) | « arret code N … », `exclus=0` | aussitôt |
    | « fin : course terminee » ou « fin : arret code 2x (course en echec …) » | égal, `exclus` = fichiers lourds attendus seulement | aussitôt, après l'étape 14 |
    | « etat final deja atteint : … ; attente sans calcul » | final | aussitôt, après l'étape 14 |
    | toute ligne ci-dessus | `exclus` portant un fichier **de résultats** (`diag/…/b-beta-*`, partie 2, grandeurs, résumés, verdicts, intervalles) | **pas sans la mère** |
    | « POUSSEE FINALE EN ECHEC : … » | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

14. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque `diag/<run_id>/b-beta-*.json` ; compagnons vérifiés :
    deux relevés de la partie 2, grandeurs (graine 0 et, s'il y a lieu, graine 1), résumés de `score`, comparaison des lentilles,
    `reads_at_firings`, **fichier de verdicts** et **fichier des intervalles** ; copie sur la branche de la tranche ; commit ; poussée.
    **La lecture reste à un lecteur neuf, sur un plan scellé** (P.7).
15. **Préavis d'une ligne à la mère, puis destruction** (sauf si la minuterie ou la garde l'ont faite) : journaux de la minuterie et de la
    garde lus ; `vastai destroy instance <ID> -y < /dev/null` ; `… suivi_vast_v6 absente <ID> --non-vide` au code 0 exigé ; minuterie et
    garde arrêtées **par PID** après `ps -p <PID> -o args=`, mortes 2 s après ; rappels annulés ; journaux et fichiers de PID commités ;
    crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et `registres/depenses.md` ; révocation de la clé `HF_TOKEN`
    recommandée à Lazar.

## Essai à blanc (sans location), fait
`scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v1.sh` (`4de3be54…`), joué le 2026-11-18 vers 06:40Z sur le commit source `43627705`
(dépôt réduit v2 : 83 fichiers, **liste `791af13d…`**, commit réduit `6af1172a`), journal `essai-a-blanc-amorce-b-beta-v1.txt`
(`5ccc3383…`) : **conforme, 0 écart** — nominal (217 essais réels, 23 étapes appelées et poussées), relance après la fin, reprise après
arrêt brutal pendant la passe (seules la passe et les suivantes rejouées), échec (20), 14 formes de secrets refusées, gardes d'entrée
(10, 12, 13, 14, 16, 17), **python** (19), carte (H100 HBM3 passe ; H100 PCIe, A100, H200 : 11). Non couverts, déclarés : code 18 ; vraie
course, vrai pip, vraie carte, clone réel.

## Réserves
- Aucun essai du code voisin ni de Drowse n'a tourné dans le conteneur (R-2710) : tout se constate à B0 et au banc.
- Les essais complémentaires des étapes (`test_neuron_lens_etapes_b_beta_v3.py`, 13 essais) jouent le câblage neuf de la v2 dans le
  conteneur (gardes aux grandeurs, cas sain jusqu'au fichier de verdicts, temps réservé, jeton de début, moitiés égales, chaîne de
  l'aller-retour) ; ils ne sont pas embarqués (le dépôt réduit et l'essai à blanc restent ceux de la liste `791af13d…`).
- Mémoire vive : `score`, les grandeurs et la comparaison des lentilles chargent plusieurs lentilles (32 à 48 Gio estimés) : `cpu_ram>=64`.
  Disque (estimé) : ≈ 17 Gio d'ajustements, ≈ 21 Gio dans la copie du banc (ajustements de trois documents et un export), 8,5 Gio de
  fichier temporaire, ≈ 13 Gio d'exports, 16 Gio de poids, 3 Gio de lentilles publiques, activations et mesures : 200 Go suffisent.
- `pytest` et PyYAML sans version exigée (relevés en partie 2 pour PyYAML ; pytest sert aux seuls essais).
- `HF_TOKEN` : exposition résiduelle (configuration de l'instance chez le loueur, processus d'entrée de l'amorce) ; révocation recommandée.

## Reprise de la vérification de la v2 (`4d24a10a…`)
| point | traitement |
|---|---|
| C-M1 étape 12 à l'ordre v1 | levé : ordre de `ETAPES` (export entre les ajustements ; contrôles avant la relance), aller-retour du banc, code 19 |
| C-M2 texte non autonome | levé : P, crédit, minuterie, garde, veille, table de destruction (codes 18 et 19) écrits ici ; essai à blanc à jour ; pièces et empreintes ; liste attendue citée |
| C-M3 image flottante | levé : `python:3.12.16-bookworm` |
| C-M4 prix déclaré à la garde | levé : le prix exigé, 2,62, avec ses raisons |
| C-m1 PyYAML | levé (déclaration 1) |
| C-m2 nombres et arrêts ajoutés | levé (déclaration 4 ; export partiel en 10) |
| C-m3 banc décidé ; intervalles à l'étape 14 | levé |
| C-m4 disque du banc | levé (réserves) |
| C-m5 trafic vérifié à l'étape 8 | levé (étape 4) |
| C-m6 80 % de D chiffré | levé (20,3 h, 73 099 s ; rappel sans destruction, le pire cas étant au-delà) |
| code : N-M1, N-m2, N-m7 | essais complémentaires `test_neuron_lens_etapes_b_beta_v3.py` (non embarqués) |
| code : N-m1 | laissé : l'essai périmé passe et lit un journal à deux documents ; `test_banc` couvre les trois documents |
| code : N-m3, N-m4, N-m6, N-m8 | déclarés (déclarations 4, 10, 12) |
| code : N-m5 | déclaré (réserves) |
| code : N-m9 | laissé : sans effet (le compte rendu de dépassement porte sur le pire cas de l'étape, 0,3 h) |

## Reprise de la vérification courte de la v3 (`af7966c8…`)
| point | traitement |
|---|---|
| V-M1 champs que le suivi ne rend pas | levé, option (a) : trafic lu sur l'offre du relevé (étapes 4 et 8, machine identique exigée) ; course figée par le critère du devis § 4 (état poussé immobile 30 min et journal inchangé) |
| V-m1 essai « moitiés égales » sans pouvoir discriminant | levé : `tests/test_neuron_lens_etapes_b_beta_v4.py` (lentilles tirées des sommes de chaque moitié ; sommes distinctes → matrices distinctes, sommes égales → égales et vues par A2) ; l'essai de la v3 reste, déclaré faible |
| V-m2 crédit en cours de course | levé : < 1 USD → arrêt ; plancher de l'étape B bis → message à la mère |
| V-m3 scellement du relevé ; colonnes d'options | levé (étape 4) |
| V-m4 durée imprimée par la minuterie | levé (étape 9 : durée restante) |
| outil du loueur absent du conteneur | étape 0.1 : création s'il manque |
