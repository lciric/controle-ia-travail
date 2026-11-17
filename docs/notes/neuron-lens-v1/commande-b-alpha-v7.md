# Commande de location et de lancement de la recourse de la lecture contre ablation (B-7) de la tranche B-α de « Neuron Lens », sur une A100 SXM4 40 Go, aux lots 16 et 64 — v7, sans ssh (proposée, **non exécutée**)

v7 = v6 (`commande-b-alpha-v6.md`, `71d4c5b1…`, archivée, jamais jouée) corrigée selon sa contre-lecture neuve
(`contre-lectures/contre-lecture-commande-b-alpha-v6-v1.md` : « à corriger », bloquantes B1 et B2, majeures M1 à M5, 16 mineures).
Différentiel :
- **Code** : lanceur **v5** (`b_alpha_lancer_v5.py` : le motif « B-7 par le haut » requiert l'audit « trop beau » de sa série, B1 ;
  bascule idempotente et contrôle d'empreinte avant tout déplacement, mesure au lot 64 interrompue reprise, M5 ; 77 essais, dont le vrai
  calcul des verdicts aux deux séries, `essais_ok` faux, les gardes de fichier absent et l'ordre des audits par série, M3) ; amorce **v7**
  (carte lue par `nvidia-smi` avant `pip`, puis par `torch`, B2) ; addendum **v2** (`addendum-texte-gele-v6-recourse-b7-a100-v2.md` :
  procédure de l'audit de B-7, statut du verdict de B-7, aucune autre série sans Lazar, M1, M2) ; dépôt réduit **v8** ; essai à blanc **v11**
  (garde de carte essayée : cas sain et artefacts) ;
- **Devis v2** (`devis-b-alpha/devis-recourse-b7-a100-v2.md`) : scénario des deux audits chiffré, ordre des séries pesé, origine du
  plafond de 8,5 USD et du compte de 2,1 USD (M4, mineures 6, 7) ; rappels à 4,8 h, 6,9 h et 9,0 h ;
- **Mineures** : témoin 60480302 retiré de l'étape 2 (mineure 2) ; la machine 60988826 est intouchable sur consigne de la mère (session
  d'une autre fille ; mineure 3) ; prix de recherche distingué du prix lu (mineure 5) ; ordre réel des audits à l'étape 12 (M4) ; ligne
  GO-2026-11-14-06 : elle dit « une RTX 4090 », l'écart de carte est accordé par GO-2026-11-17-04, inscrit par la mère sur `main`
  (`registres/go.md`, l. 360-361, relu par le contre-lecteur du devis B-β ; mineure 12).
Le reste est la v6.

v6 = v5 (`commande-b-alpha-v5.md`, `423b74b4…`, archivée ; feu R-2904 jouée le 2026-11-15 : instance 60783204, course terminée, verdict
R-2915 « partielle » ; journal `journal-course-b-alpha-v3.md`). Demande de la mère sur GO-2026-11-17-03 (R-3046) et GO-2026-11-17-04
(mot de Lazar : **A100 SXM4 40 Go** sous la ligne GO-2026-11-14-06 ; ablation jouée deux fois sur la même carte, lots 16 et 64). Écarts
déclarés et lecture des deux séries : `addendum-texte-gele-v6-recourse-b7-a100-v1.md` (`11671826…`). **Aucune location avant le feu
écrit de la mère.** Différentiel :
- **Carte** : `gpu_name=A100_SXM4`, `gpu_ram<=45` (la variante de 40 Go ; celle de 80 Go est écartée), prix lu ≤ **0,73 USD/h** stockage
  compris (borne R-2887 gardée) ; l'amorce reçoit `CARTE_ATTENDUE=A100-SXM4-40GB` et s'arrête au code 11 si `torch` lit une autre carte ;
- **Code** : lanceur **v4** (`b_alpha_lancer_v4.py`, `c598b787…` : après les verdicts du lot 16, `bascule-lot64` met de côté les
  fichiers de `measure` du lot 16, empreinte vérifiée, puis `measure-lot64` (`--ctx-batch 64`), `score-lot64`, `grandeurs-lot64`,
  `verdicts-lot64`, `audit-trop-beau-lot64` s'il est requis ; `essais_ok` lu des résultats de B0, B.3 et de la fumée, constat porté ;
  65 essais), amorce **v6**, dépôt réduit **v7** (l'addendum et la note de mémoire y entrent, scellés) ; `essai_environnement_b0_v3.py`
  (appels de `measure` aux lots 16 et 64, vraie bascule ; artefact : lanceur v3 pris en défaut) ; essai à blanc **v10** (la v6 écrivait « v9 », coquille, mineure 1) ;
- **Branches et fichiers** : dépôt réduit sur `course/neuron-lens-b-alpha-reduit-v8` ; résultats sur **`calcul/neuron-lens-b-alpha-v5`**
  (absente, à prouver) ; fichiers de suivi en `-b-alpha-v4` ; étiquette de l'instance `neuron-lens-b-alpha-b7` ;
- **Dépense** : déjà faite sur la ligne ≈ 2,1 USD (compte large des trois courses) ; **plafond de la garde pour cette course 8,5 USD** :
  compte rendu à **5,10 USD** (60 % ; ≈ 7,2 USD sur la ligne, son seuil de 60 %), arrêt dur et destruction vérifiée à **7,65 USD** (90 % ;
  ≈ 9,75 USD sur la ligne, sous son arrêt dur de 10,80) ; minuterie D = 90 % de 8,5 au prix lu (37 726 s à 0,73 ; 44 419 s à 0,62) ;
- **Rappels** en durée : (a) **4,8 h** (attendu par les bornes codées), (b) **8,0 h** (la mère décide), (c) 80 % de D ;
- **Devis et relevé** : `devis-b-alpha/devis-recourse-b7-a100-v1.md` et `devis-b-alpha/releve-prix-vast-a100-20261117T003231Z-v1.tsv`.
Le reste est la v5, inchangée, aux noms près. Le texte de la v5 suit, mis à jour ; ce qui n'est pas dit au différentiel n'a pas changé.

**Préambule P** (le shell ne garde rien d'un appel à l'autre) :
`cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`
**Intouchables** (jamais arrêtées, jamais détruites) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, la machine 60988826, `poste-temoin-bailey-*`, et
toute instance d'une autre session. **Jamais** de `vastai show … --raw` imprimé (la configuration porte les deux secrets) : tout passe par
`suivi_vast_v6`. Secrets lus **par leur nom** seulement ; aucune valeur affichée, écrite ni versée.
**Règle R-2864** (mot de Lazar par la mère) : avant tout geste à risque de refus par le classifieur (création avec les deux secrets,
bloc encodé de l'entrée, destruction manuelle, effacement de clés), **préavis d'une ligne à la mère, sans attendre de signal** (R-2883, R-2887 ; lecture R-2892, point 9) ; ne jamais contourner
ni reformuler un refus. Les automates déjà armés (minuterie, garde) ne sont pas concernés : ils détruisent à leur échéance.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur `vastai` 1.11.0 à `/home/user/vastai-env/bin/vastai` (le créer s'il manque, comme en v14) ; avec P :
   `vastai show user --raw > /dev/null` au code 0 exigé (sortie jetée).
2. **Secrets présents, par leur longueur** : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ] && [ ${#HF_TOKEN} -ge 8 ]` (le suivi v6 balaie
   les deux : sans `HF_TOKEN` dans la session, sa forme ne serait pas balayée). Sinon arrêt, message à la mère.
   **Suivi prêt** : `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 verifier` → code 0 ;
   `… suivi_vast_v6 instances` → code 0, liste consignée (identifiants et états) ; l'absence finale se prouve par `--non-vide` (étape 15 ;
   le témoin 60480302 n'existe plus). Sinon aucune création.
3. **Crédit** : `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print({k: d.get(k) for k in ("credit", "can_pay", "has_billing", "billing_failed", "autobill_threshold", "autobill_amount")})'`
   → `can_pay` vrai, `has_billing` vrai, `billing_failed` faux exigés (champ absent ou nul = arrêt) ; consigné (R-2788, R-2795).
4. **Prix du jour** (devis v2, § 2 ; aucun repli, M4) :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 gpu_ram<=45 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=150 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.73 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA et **prix du trafic** (`inet_up_cost`, `inet_down_cost`)
   consignés. Ce `dph_total` de recherche **ne compte pas le stockage** (≈ 0,04 à 0,08 USD/h pour 150 Go) : la borne qui décide est celle du
   **prix lu sur l'instance**, stockage compris (étape 8) ; une offre trop proche de 0,73 à la recherche sera détruite à l'étape 8. **Aucune offre → rien ne part**, message à la mère (nœud : autre carte, mot de Lazar).
5. **Dépôt réduit** au commit scellé de la course :
   `.venv/bin/python scripts/depot_reduit_neuron_lens_b_alpha_v8.py <COMMIT_SOURCE> <dossier neuf>` (`<COMMIT_SOURCE>` : le commit
   complet, 40 caractères, de `prep/neuron-lens-v1` choisi pour la course ; il est aussi passé à la machine, étape 7) → `liste-fichiers.sha256`, `rapport.json`, paquet
   `neuron-lens-b-alpha-reduit.bundle` ; **liste attendue : celle de l'essai à blanc** (voir plus bas ; une liste différente exige un
   nouvel essai à blanc). Branche dédiée du dépôt de travail : `course/neuron-lens-b-alpha-reduit-v8`
   (`git fetch <paquet> course:refs/heads/course/neuron-lens-b-alpha-reduit-v8 && git push origin course/neuron-lens-b-alpha-reduit-v8`) ;
   `git ls-remote origin refs/heads/course/neuron-lens-b-alpha-reduit-v8` = commit réduit ; `git ls-remote origin
   refs/heads/calcul/neuron-lens-b-alpha-v5` **vide** (branche des résultats absente ; sinon arrêt). Code voisin : quatre fichiers de
   différences appliqués par `preparer` — les trois correctifs du texte gelé et le dépôt de la provenance « chat » déclaré à l'addendum
   v3, § 4 (écart 14 du texte gelé, qui dit « trois correctifs »).
6. **RUN_ID** fixé ici une fois pour toutes (`<AAAAMMJJ-HHMMSS>-neuron-lens-b-alpha`, heure UTC de cette étape) : le même à chaque relance
   du conteneur par le loueur (entrée idempotente).

## 1. Location (une seule instance), minuterie, garde, rappels
7. **Préavis d'une ligne à la mère** (offre, prix), **puis création sans attendre de réponse** (feu R-2887, consigne 5 ; R-2883) ; tout refus
   d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère. Création (image `python:3.12-bookworm` ; disque 150 Go), sortie réduite
   par le suivi :
   ```
   date -u +%FT%TZ   # <ISO_CREATION>, relevée dans la même commande
   GO_ID=GO-2026-11-14-06 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 150 --label neuron-lens-b-alpha-b7 \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN -e COMMIT_REDUIT=<COMMIT_REDUIT> -e COMMIT_SOURCE=<COMMIT_SOURCE> -e GO_ID=GO-2026-11-14-06 -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-b-alpha-v5 -e PERIODE_POUSSE_S=600 -e CARTE_ATTENDUE=A100-SXM4-40GB" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-b-alpha-reduit-v8 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_alpha_v7.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   `<COMMIT_REDUIT>` et `<COMMIT_SOURCE>` sont **lus par programme dans `rapport.json`** du dépôt réduit, dans la même commande, et
   leur longueur (40) vérifiée ; jamais retapés (feu R-2887, R1). Les deux secrets ne sont développés que par le shell du lancement (dans `--env`) ; les `$` entre apostrophes le sont sur la machine.
   Ils figurent aussi, le temps de la création, dans les arguments du processus de l'outil dans le conteneur de la session (déclaré).
   `COMMIT_SOURCE` est hérité par l'amorce et par ses appels du lanceur, qui ne le retirent pas (vérifié par le lecteur, simulation de la
   partie 2 : 0 écart avec, arrêt sans).
   **Entrée idempotente** : à une relance, le clone est sauté (`[ -d depot/.git ]`, leçon du volet A : « depot already exists » en
   boucle) et l'amorce relit son état (attente sans calcul après l'état final ; reprise sinon). → identifiant et heure consignés
   (`echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v5.txt`).
   Échec (pas de `new_contract`, ou `success` faux) → comme en v14 : `instances`, destruction éventuelle selon l'étape 15, message.
   **Dans toute branche d'échec des étapes 7, 8 et 9, la destruction est immédiate** : préavis d'une ligne à la mère au moment du geste,
   sans attendre de signal (feu R-2887, P1) ; si une attente devait survenir, poser d'abord les automates manquants (minuterie puis
   garde, au prix lu, à défaut au prix de l'offre).
8. **Prix lu sur l'instance** (m9) : `… suivi_vast_v6 instance <ID>` → `dph_total` (stockage compris) **≤ 0,73 exigé** (feu R-2887), sinon
   destruction selon l'étape 15 et message. C'est ce prix lu (<PRIX>) qui sert aux étapes 9 et 10.
9. **Minuterie v4** par identifiant, posée aussitôt (R10), comptée depuis la création (P, puis dans la même commande) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 8.5 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-b-alpha-v5.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-b-alpha-v5.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v4 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v5.txt
   ```
   D = 90 % du plafond de 8,5 au prix lu (37 726 s à 0,73 ; 44 419 s à 0,62) ; bornes de la v4 : 600 à 129 600 s. PID lu dans le fichier
   écrit par la minuterie, **jamais** `$!`. Non armée → destruction selon l'étape 15, message.
10. **Garde de dépense v4**, détachée, son PID écrit par elle-même avant `exec`, l'outil trouvé par le `PATH` passé explicitement
    (P, puis) :
    ```
    F=docs/notes/neuron-lens-v1/pid-garde-b-alpha-v5.txt; rm -f "$F"
    setsid nohup bash -c 'echo $$ > "$0"; exec env PATH=/home/user/vastai-env/bin:$PATH PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --instance <ID> --prix-h <PRIX> --plafond 8.5 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-b-alpha-v5.jsonl' "$F" \
      >> docs/notes/neuron-lens-v1/garde-b-alpha-v5.log 2>&1 < /dev/null &
    sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep garde_depense_v4 && echo "$(date -u +%FT%TZ) garde PID $P instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v5.txt
    ```
    → vivante et portant la garde exigé (sinon destruction selon l'étape 15, sur préavis d'une ligne) ; compte rendu à la mère à
    **5,10 USD** (60 % de 8,5), destruction réessayée et vérifiée à **7,65 USD** (90 % ; code 4 et message immédiat si elle échoue).
11. **Rappels** (`send_later`) : (a) à **4,8 h** de location, compte rendu en durée à la mère (attendu codé sans audit) ; (a') à **6,9 h**,
    compte rendu (attendu codé avec les deux audits) ; (b) à **9,0 h** : la mère décide (avant la minuterie) ; (c) à **80 % de D** : « vérifier et détruire l'instance <ID> » ; puis commit et poussée de
    `pids-b-alpha-v5.txt` sur `prep/neuron-lens-v1`. **Veille** en tâche de fond (2 h au plus, relancée à chaque contrôle), P puis :
    ```
    for i in $(seq 1 24); do
      for n in "minuterie minuterie_destruction_neuron_lens_v4" "garde garde_depense_v4"; do set -- $n
        P=$(cat docs/notes/neuron-lens-v1/pid-$1-b-alpha-v5.txt 2>/dev/null)
        if [ -n "$P" ] && ps -p "$P" -o args= | grep -q "$2"; then s=vivante; else s=MORTE; fi
        echo "$(date -u +%FT%TZ) veille $1 PID ${P:-absent} $s" >> docs/notes/neuron-lens-v1/veille-b-alpha-v5.log
      done; sleep 300
    done
    ```
    Une ligne « MORTE » (redémarrage du conteneur de la session : deux fois au volet A) → réarmement aussitôt, par les étapes 9 et 10,
    **sur la même échéance absolue** (la durée D est recomptée depuis `<ISO_CREATION>`), PID relus dans les fichiers, arguments vérifiés ;
    message à la mère. À chaque réveil de la session, minuterie et garde sont vérifiées par leur PID (feu R-2887, R4).

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_alpha_v7.sh`, sans intervention)
12. Commit égal à `COMMIT_REDUIT` (code 10) ; arbre propre au premier départ (code 10) ; RUN_ID et GO_ID valides (code 17) ; première
    poussée vérifiée (code 14, avant l'environnement) ; `pip` 26.2.2 puis les versions épinglées (`requirements-neuron-lens-b-alpha-v1.txt`),
    **verbeux, sous `timeout` 3 600 s pour chacun des deux appels** (code 16 ; durée journalisée ; pire cas 2 h, contre 1,5 h au devis : déclaré) ; carte (code 11) ; essais de nos modules (156, code 12 sur échec,
    essai sauté ou arbre sali) ; puis les étapes du lanceur dans l'ordre de `suite` : `preparer` (correctifs appliqués, empreintes avant
    et après, manifeste R9) → `telecharger-tokeniseur` (**clé**) → `b0` → `telecharger-poids` (**clé** ; ensuite retirée de la course,
    vérifiée par son nom) → `corpus` (en ligne, sans clé) → `partie2` (scellée sur la machine ; tout écart = arrêt) → `fumee` (refusée
    sans la partie 2 sans écart) → `passe` → `b3` → `measure` (**`--ctx-batch 16`**, R-2901) → `score` → `grandeurs` (fidèles à `score`) → `verdicts` → audits du lot 16 s'ils
    sont requis par lui, dans l'ordre « trop beau » (requis aussi par B-7 « par le haut ») puis « tout négatif » → **`bascule-lot64`** →
    **`measure-lot64` (`--ctx-batch 64`)** → `score-lot64` → `grandeurs-lot64` → `verdicts-lot64` → audit « trop beau » du lot 64 s'il est
    requis → audit « tout négatif » s'il est requis par le seul lot 64 (même machine ; ordre essayé par le lanceur v5) ; après l'audit de
    B-7 « par le haut », la lecture de B-7 est **proposée**, non tranchée (addendum v2, § 4) ; **pour l'audit « tout négatif », le champ `lecture` du résultat est une lecture proposée, non tranchée :
    aucun verdict après cet audit sans la décision de Lazar (point (b), nœud de Lazar)** ; les écarts `logit`, `J` et `hub` sont versés
    tous les trois. La partie 2 est **scellée avant la fumée** (garde du lanceur) et **poussée au plus 10 min après** (poussée
    périodique) : le lanceur n'attend pas la poussée. Poussées vérifiées sur `calcul/neuron-lens-b-alpha-v5` toutes les 10 min, à la fin et à tout arrêt ;
    **balayage** des deux secrets (sept formes) avant chaque commit : une forme trouvée = rien n'est poussé ; fichiers de plus de 95 Mo
    exclus (`-causal.pt`, les activations et les tables restent sur l'instance, M6) ; état poussé : étape en cours, étapes faites,
    durée de la location, fin du journal de `pip`. Poussée finale persistante (10 essais à 60 s) ; état final écrit (`fin-b-alpha.txt`)
    pour qu'une relance n'en refasse rien.

## 3. Suivi, retour et destruction (conteneur de la session)
13. Suivi comme en v14 (`suivi_vast_v6 logs <ID> 40`, `instance <ID>`, état poussé de la branche des résultats ; `ps -p` sur les PID) ;
    **course figée** (R-2800) : `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite sans nouvelle poussée → arrêt ;
    **crédit** relu à chaque contrôle (< 1 USD en cours de course → arrêt) ; dépassement du pire cas d'une étape (champ
    `depassement_pire_cas` du résultat d'étape, ou étape en cours depuis plus que son pire cas dans l'état poussé) → compte rendu ; la
    durée de location se compte depuis `<ISO_CREATION>` (le `location_s` de l'état poussé repart de zéro à chaque relance de l'amorce).
    **Lectures de la session dès qu'ils sont poussés** (sans lire de résultat de mesure) : `b-alpha-b0.json` — un défaut (e) (matrice
    identité) n'arrête pas la course (texte gelé : « chaîne en défaut ») mais est **rapporté aussitôt à la mère**, qui peut arrêter avant
    les passes payantes ; `addendum-partie2-b-alpha-v1.md` — jetons de début de la tranche « chat » : rendue par le gabarit de Llama, chaque
    document en porte deux (gabarit et tokeniseur) ; un document à un seul jeton de début signale un rendu en texte nu (sans gabarit) →
    message immédiat à la mère, arrêt avant `measure` si elle le dit.
    **Règle de destruction**, sur la **dernière ligne** du journal et l'**état poussé** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » ou `fatal:` de git sans ligne `AMORCE` | aucun | aussitôt, selon l'étape 15 |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt, selon l'étape 15 |
    | « fin : arret code N (…) », course non lancée (10, 11, 12, 13, 14, 16, 17) | « arret code N … », `exclus=0` | aussitôt, selon l'étape 15 |
    | « fin : course terminee » ou « fin : arret code 2x (course en echec …) » | égal, `exclus` = fichiers lourds attendus seulement | aussitôt, après l'étape 14, selon l'étape 15 |
    | « etat final deja atteint : … ; attente sans calcul » (relance après la fin) | final | aussitôt, après l'étape 14, selon l'étape 15 |
    | toute ligne ci-dessus | `exclus` portant un fichier **de résultats** (`diag/…/b-alpha-*`, partie 2, grandeurs, résumés) | **pas sans la mère** |
    | « POUSSEE FINALE EN ECHEC : … » | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

14. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque `diag/<run_id>/b-alpha-*.json` ; vérification des
    compagnons de la partie 2, des grandeurs et des résumés ; copie dans `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
    **La machine pousse le brut ; la lecture reste à un lecteur neuf** (m8).
15. **Préavis d'une ligne à la mère, puis destruction sans attendre** (R-2883 ; feu R-2887), sauf si la minuterie ou la garde l'ont déjà faite. Journaux de la minuterie et de
    la garde lus ; `vastai destroy instance <ID> -y < /dev/null` ; `… suivi_vast_v6 absente <ID> --non-vide` (le témoin 60480302 n'existe plus ; leçon de la troisième course) code 0 exigé ; minuterie et garde arrêtées **par PID** après `ps -p <PID> -o args=` (minuterie v4, garde v4), mortes 2 s après ;
    rappels annulés ; journaux et fichiers de PID commités ; crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et
    `registres/depenses.md` ; **révocation de la clé `HF_TOKEN`** recommandée à Lazar (devis v2, § 5).

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v10.sh`, journal versé `devis-b-alpha/essai-a-blanc-amorce-b-alpha-v10.txt`.
Joué le 2026-11-17 sur le commit source `42e16e7f8118ca8376bebe50eaeb8d6075af5434` (dépôt réduit v7 : commit réduit
`548b451bce6d4a5777125a2f47b2f5cd9a78b0fb`, 351 fichiers, **liste `fcf9f3a01b83dea1b74d3acf1c48e7a852dbde4b6d7746486928ff58f56e5b98`**,
paquet `525ffec4…`) : **verdict automatique : conforme, 0 écart**. Cas de la v8 (nominal avec **156** essais réels, relance, reprise
après arrêt brutal, échec 20, 14 formes, gardes d'entrée, balayage final, 0 processus restant) et, neufs : étapes du faux lanceur égales à
celles du lanceur v4 (audits exceptés), lues par programme ; nominal à **18** appels et 18 résultats poussés ; reprise qui rejoue la
seconde série ; environnement exact v3 : `measure --ctx-batch 16` et `--seed 1` au lot 16, `--ctx-batch 64` et `--seed 1` au lot 64,
vraie bascule (fichiers du lot 16 renommés, empreintes), vraie `etape_measure_lot64` (un appel, `--ctx-batch 64`), hors ligne, sans
secret ; artefact : le lanceur v3 est pris en défaut (6 écarts). L'essai v9 avait un seul écart, de l'essai lui-même (compte des résultats
poussés resté à 13 ; journal `essai-a-blanc-amorce-b-alpha-v9.txt`), corrigé en v10. **La liste attendue de l'étape 5 est celle-ci** ;
le commit source de la course est le commit qui porte cette commande (ses pièces de course sont identiques à `42e16e7f`, la liste le
prouve).
Non couverts, déclarés : comme en v8 ; le contrôle `CARTE_ATTENDUE` de l'amorce v6 n'est pas joué (aucune carte dans le conteneur ;
relu seulement) ; la mémoire de pointe au lot 64 sur l'A100 est estimée, non mesurée (marge ≈ 15,5 GiB).

## Jetons
- Jeton du programme : écriture sur tout le dépôt de travail ; « jamais vers `main` » n'est garanti que par l'amorce (réserve inchangée).
- `HF_TOKEN` : exposition résiduelle déclarée (devis v2, § 5, M5) : configuration de l'instance chez le loueur jusqu'à la destruction,
  environnement du processus d'entrée et du shell principal de l'amorce pendant toute la location (pour le balayage), retour à chaque
  relance ; `env -u` ne la retire qu'aux enfants. Recommandation (mère → Lazar) : clé neuve, lecture seule, limitée à ce modèle, révoquée
  après la course.

## Réserves et limites (reprises de la v14 et de la vérification courte)
- S-5 (v14) : un crédit épuisé en cours de course, avant le rechargement automatique, peut faire arrêter l'instance par le loueur.
- S-11 (v14) : la garde v4 lit l'absence par `vastai show instance <id> --raw` (sortie jamais imprimée), non éprouvé sur une instance
  détruite : au pire fausse alerte ; la minuterie reste le filet. T-5 : la minuterie exige une liste non vide ; si le compte n'avait plus
  d'autre instance, elle rendrait 6 sur une destruction réussie (les témoins sont ceux d'une autre session). T-1, T-6 : secrets avec `"`,
  `\`, saut de ligne ou tabulation non reconnus par le balayage ; hors d'atteinte pour les secrets de la session.
- Échéances du lanceur pour `b3`, `score`, `grandeurs`, `verdicts` : 1,0 h au pire contre 0,8 h au devis (rapport, mineur 6) ; `pytest` non
  épinglé dans les exigences (mineur 9, constat porté, toujours ouvert : les exigences v1 sont reprises telles quelles) ; `INSTANCE_ID` vide dans la partie 2 (identifiant consigné dans
  `pids-b-alpha-v5.txt`) ; empreinte de la lentille J de Qwen3-8B consignée sans référence (audit « tout négatif ») ; intervalles pour
  `npR` et `logit` (« steer 1x ») seulement, les grandeurs par pôle versées permettant les autres ; avertissement de git (« push
  negotiation failed ») à la poussée vers le dépôt nu de l'essai, sans effet ; aucun essai ne joue `etape_partie2`,
  `etape_telecharger_tokeniseur` réel ni `releve_partie2` avec l'environnement de l'amorce (c'est par là qu'est passé M1 : à la prochaine
  version du lanceur).
- Point (a) : `corpus` en ligne sans clé, accepté par la mère (écart à la lettre du devis seulement ; accès anonyme aux jeux publics, un
  refus pour excès de requêtes arrêterait l'étape sans fuite). Point (c) : convention de capture de J non nommée par ses fichiers, à
  écrire au rapport de B-4 et à la partie 2. Point (d) : `test_cibles_invisibles_v4`, avant toute fusion dans `main`.

## Devis
`devis-b-alpha/devis-recourse-b7-a100-v1.md` : attendu ≈ 2,7 à 3,0 h, **≈ 1,8 à 2,3 USD** trafic compris ; pire cas codé ≈ 17 h, tronqué
par l'arrêt dur de la garde à **7,65 USD** ; ligne GO-2026-11-14-06 après la course ≈ 3,9 à 4,4 USD attendus, ≈ 10,05 USD au pire, sous
son arrêt dur (10,80). Déjà dépensé sur la ligne : ≈ 2,1 USD (trois courses). Relevé du jour : `devis-b-alpha/releve-prix-vast-a100-20261117T003231Z-v1.tsv`
(quatre offres sous 0,73 USD/h stockage compris, la moins chère ≈ 0,62).

## Empreintes des pièces citées
| pièce | sha256 |
|---|---|
| `docs/notes/neuron-lens-v1/commande-b-alpha-v5.md` | `423b74b43920788060d8ddb21bbeba0ae32ef5588ea63f7b2db511df27e38bb6` |
| `docs/notes/neuron-lens-v1/journal-course-b-alpha-v3.md` | `edd37d374204a0e889d72f1646dbc783ddabe79189cc29734e35e9cd8ef3421e` |
| `docs/notes/neuron-lens-v1/addendum-texte-gele-v6-recourse-b7-a100-v1.md` | `116718269d1c20e05c21e261d9ce385afaca2f63821247d9f76209297c4f98df` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/memoire-ablation-lot64-rtx4090-v1.md` | `b67f90a9a007f287fd857ed064fcc98950877378cefcc855755a54b9ffe40324` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/memoire-measure-b-alpha-v1.md` | `423d79553ae6bca71098623ff1c45033598efbe45c6abb604871cc20ff870da5` |
| `src/controle_ia/neuron_lens/b_alpha_lancer_v4.py` | `c598b78755b373008420b846754992700801d8695676fd6ae68d31b43a310a34` |
| `tests/test_neuron_lens_b_alpha_lancer_v4.py` | `0126acbd46469231225b07294cfe124edc7a9ed4569beadefced9bb16224b252` |
| `scripts/amorce_neuron_lens_b_alpha_v7.sh` | `17972c842cc531e9df21f8cdf651f6228122c854fa04a9baeea35af6e98f1f4f` |
| `scripts/depot_reduit_neuron_lens_b_alpha_v8.py` | `72f18c67becac924147c145de943d2d7c3e50da4d1464662975d29d214823168` |
| `scripts/essai_environnement_b0_v3.py` | `bf34497f20192f03887fa3771f4748d89509049ac3af8874e9e2c4bc1d22371d` |
| `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v10.sh` | `431e0645ef19556f519ba4ef996518fd93dc38b83a9890b380796626c205affc` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/essai-a-blanc-amorce-b-alpha-v10.txt` | `b8611d53b802b352c6d5609840a60c29b7f5e30e7f65c87ae5c042bea7f57d67` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/releve-prix-vast-a100-20261117T003231Z-v1.tsv` | `a3bce297995e402067c00f5cb759d2f4547ab8a32ed26d2ce731ce2fe3481aac` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `src/controle_ia/neuron_lens/garde_depense_v4.py` | `6a98d816a0917b7e3a7029ce105a3f0047a765f494b5ec07032b05836a1a0310` |
| `src/controle_ia/neuron_lens/suivi_vast_v6.py` | `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f` |
| `scripts/minuterie_destruction_neuron_lens_v4.sh` | `4511368311b557b89803ff41900d3139a4c2a898212e8ef28a178e38fa7e3082` |
| `requirements-neuron-lens-b-alpha-v1.txt` | `ef184e589a24f293356880419636d4b909ae8b76d0a95a50e0b50483338a2887` |
