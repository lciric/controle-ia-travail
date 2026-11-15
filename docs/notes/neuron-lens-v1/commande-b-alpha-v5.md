# Commande de location et de lancement de la tranche B-α de « Neuron Lens » — v5, sans ssh (proposée, **non exécutée**)

v5 = v4 (`commande-b-alpha-v4.md`, `f54d5ec3…`, archivée ; feu R-2892 jouée le 2026-11-15 : instance 60773264, B0, partie 2, fumée et
passe faits, `measure` arrêté par mémoire de carte épuisée à l'ablation, détruite, absence prouvée, ≈ 0,71 USD ; journal
`journal-course-b-alpha-v2.md`). Décision de la mère R-2901, option (a). Différentiel :
- **Code** : lanceur **v3** (`measure --ctx-batch 16` aux graines 0 et 1 ; 52 essais), amorce **v5**, dépôt réduit **v6** ;
  `essai_environnement_b0_v2.py` (appels de `measure` contrôlés par programme) ; essai à blanc **v8** : conforme, 0 écart, **liste
  `0293f4e1…`** ;
- **Écart de lot déclaré** : `--ctx-batch 16` au lieu du défaut 64 (l. 379 de la copie, hors des défauts gelés des l. 374 à 377) ;
  mémoire de pointe estimée (`devis-b-alpha/memoire-measure-b-alpha-v1.md`) : ≈ 16,5 GiB alloués, marge ≈ 4,7 GiB ; aucune autre partie
  n'a de lot trop gros sur la carte ; si l'ablation échoue encore par mémoire : destruction immédiate, rapport, aucune relance sans mot de
  la mère ;
- **Branches et fichiers** : dépôt réduit sur `course/neuron-lens-b-alpha-reduit-v6` ; résultats sur **`calcul/neuron-lens-b-alpha-v3`**
  (la v2 porte ceux de la relance) ; fichiers de suivi en `-b-alpha-v3` ;
- **Mineurs de la relecture R-2892 portés** : préambule et étape 10 en « préavis d'une ligne, sans attendre » (point 9) ; « 143 » essais
  à l'étape 12 ; fondement de l'étape 15 : R-2883. (Le défaut `calcul/neuron-lens-b-alpha-v1` codé dans l'amorce, l. 47, est sans effet :
  la commande passe `BRANCHE_RESULTATS`.)
Le reste est la v4, inchangée. **Ces retouches n'ont pas été relues par un contre-lecteur (déclaré).**

v4 = v3 (`commande-b-alpha-v3.md`, `eaa88cc6…`, archivée) avec un seul changement, demandé par la mère après la première course :
l'essai à blanc cité est le **v6** (`essai_a_blanc_amorce_neuron_lens_b_alpha_v6.sh`, journal `devis-b-alpha/essai-a-blanc-amorce-b-alpha-v6.txt`),
qui ajoute le contrôle de l'**environnement exact des essais de B0** (`scripts/essai_environnement_b0_v1.py` : vrai `preparer`, vrai
`etape_b0` avec un enregistreur à la place de pytest ; pour chacun des quatre essais : variables lues ou écrites à l'usage présentes,
chemins existants, empreintes écrites résolues dans l'arbre préparé, modèle, hors-ligne, aucun secret ; artefact : le lanceur v1 est
pris en défaut sur `NEURON_LENS_ORIG`, la cause de l'échec du 2026-11-15). Code, dépôt réduit v5 et liste `0863f9c7…` inchangés.


v3 = v2 (`commande-b-alpha-v2.md`, `cf437d95…`, archivée ; feu R-2887 jouée le 2026-11-15 : instance 60770175, arrêtée à B0 par un
défaut du lanceur v1, détruite, absence prouvée, ≈ 0,06 USD ; journal `journal-course-b-alpha-v1.md`). Différentiel :
- **Code** : lanceur **v2** (`b_alpha_lancer_v2.py`) : `preparer` garde, avant les correctifs, la copie du script d'activations d'origine
  (`151d1196…`, sous `originaux/`) et `b0` la passe à l'essai du correctif (1) par `NEURON_LENS_ORIG`, comme son usage l'exige (cause
  de l'échec du 2026-11-15) ; essais v2 : 50, dont l'environnement de `b0` et `etape_partie2` de bout en bout avec l'environnement de
  l'amorce (avec et sans `COMMIT_SOURCE` : vérification courte, mineur 18) ; amorce **v4** (lanceur v2, essais v2) ; dépôt réduit **v5** ;
  essai à blanc **v5** (contrôle des processus restants rétabli) : conforme, 0 écart, **liste `0863f9c7…`** ;
- **Branches** : dépôt réduit sur `course/neuron-lens-b-alpha-reduit-v5` ; résultats sur **`calcul/neuron-lens-b-alpha-v2`** (la v1 porte
  ceux de la première course) ; fichiers de suivi de la session en `-b-alpha-v2` (ceux de la première course restent en `-v1`) ;
- **Consignes du feu R-2887 portées dans le texte** : prix lu **≤ 0,73 USD/h** (minuterie au prix lu, formule de la garde v4) ; P1
  (destruction immédiate dans toute branche d'échec des étapes 7 à 9, préavis d'une ligne) ; R1 (commits lus par programme dans
  `rapport.json`) ; R4 (vérification par PID à chaque réveil, réarmement sur la même échéance absolue) ; création sur préavis sans
  attendre ; destruction finale sur préavis sans attendre ;
- **Devis** : pire cas complet par les bornes codées 14,7 h × 0,73 = 10,73 USD, sous l'arrêt dur ; dépense déjà faite ≈ 0,06 USD.
Le reste est la v2, inchangée. **Ces retouches n'ont pas été relues par un contre-lecteur (déclaré).**

Pièce 7 du § 6 du devis B-α v2 (`devis-b-alpha/devis-tranche-b-alpha-v2.md`, `61c394f5…`). Écrite par la fille « Neuron Lens » le
2026-11-15, sur l'accord de la mère (R-2863) ; **aucune location ni dépense avant son feu**. Reprend la commande v14 du volet A
(`commande-volet-a-v14.md`, `14fe6383…`), jouée le 14 novembre, aux points que B-α change : ligne GO-2026-11-14-06 (12 USD, échéance
2026-11-30), second secret `HF_TOKEN` (GO-2026-11-15-04), RTX 4090 à prix lu ≤ 0,73 USD/h (v3), bornes en durée, minuterie v4, amorce B-α v5,
lanceur `b_alpha_lancer_v3` (`measure --ctx-batch 16`, v5), entrée idempotente. Rien de la v14 n'est retiré sans être dit.

**Préambule P** (le shell ne garde rien d'un appel à l'autre) :
`cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`
**Intouchables** (jamais arrêtées, jamais détruites) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*`, et
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
   `… suivi_vast_v6 instances` → code 0, liste consignée (identifiants et états) ; un **témoin** d'une autre session qui doit durer
   (60480302 ou 60670453) est noté pour l'étape 15. Sinon aucune création.
3. **Crédit** : `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print({k: d.get(k) for k in ("credit", "can_pay", "has_billing", "billing_failed", "autobill_threshold", "autobill_amount")})'`
   → `can_pay` vrai, `has_billing` vrai, `billing_failed` faux exigés (champ absent ou nul = arrêt) ; consigné (R-2788, R-2795).
4. **Prix du jour** (devis v2, § 2 ; aucun repli, M4) :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=150 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.73 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA et **prix du trafic** (`inet_up_cost`, `inet_down_cost`)
   consignés. **Aucune offre → rien ne part**, message à la mère (nœud : autre carte, mot de Lazar).
5. **Dépôt réduit** au commit scellé de la course :
   `.venv/bin/python scripts/depot_reduit_neuron_lens_b_alpha_v6.py <COMMIT_SOURCE> <dossier neuf>` (`<COMMIT_SOURCE>` : le commit
   complet, 40 caractères, de `prep/neuron-lens-v1` choisi pour la course ; il est aussi passé à la machine, étape 7) → `liste-fichiers.sha256`, `rapport.json`, paquet
   `neuron-lens-b-alpha-reduit.bundle` ; **liste attendue : celle de l'essai à blanc** (voir plus bas ; une liste différente exige un
   nouvel essai à blanc). Branche dédiée du dépôt de travail : `course/neuron-lens-b-alpha-reduit-v6`
   (`git fetch <paquet> course:refs/heads/course/neuron-lens-b-alpha-reduit-v6 && git push origin course/neuron-lens-b-alpha-reduit-v6`) ;
   `git ls-remote origin refs/heads/course/neuron-lens-b-alpha-reduit-v6` = commit réduit ; `git ls-remote origin
   refs/heads/calcul/neuron-lens-b-alpha-v3` **vide** (branche des résultats absente ; sinon arrêt). Code voisin : quatre fichiers de
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
   GO_ID=GO-2026-11-14-06 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 150 --label neuron-lens-b-alpha \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN -e COMMIT_REDUIT=<COMMIT_REDUIT> -e COMMIT_SOURCE=<COMMIT_SOURCE> -e GO_ID=GO-2026-11-14-06 -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-b-alpha-v3 -e PERIODE_POUSSE_S=600" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-b-alpha-reduit-v6 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_alpha_v5.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   `<COMMIT_REDUIT>` et `<COMMIT_SOURCE>` sont **lus par programme dans `rapport.json`** du dépôt réduit, dans la même commande, et
   leur longueur (40) vérifiée ; jamais retapés (feu R-2887, R1). Les deux secrets ne sont développés que par le shell du lancement (dans `--env`) ; les `$` entre apostrophes le sont sur la machine.
   Ils figurent aussi, le temps de la création, dans les arguments du processus de l'outil dans le conteneur de la session (déclaré).
   `COMMIT_SOURCE` est hérité par l'amorce et par ses appels du lanceur, qui ne le retirent pas (vérifié par le lecteur, simulation de la
   partie 2 : 0 écart avec, arrêt sans).
   **Entrée idempotente** : à une relance, le clone est sauté (`[ -d depot/.git ]`, leçon du volet A : « depot already exists » en
   boucle) et l'amorce relit son état (attente sans calcul après l'état final ; reprise sinon). → identifiant et heure consignés
   (`echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v3.txt`).
   Échec (pas de `new_contract`, ou `success` faux) → comme en v14 : `instances`, destruction éventuelle selon l'étape 15, message.
   **Dans toute branche d'échec des étapes 7, 8 et 9, la destruction est immédiate** : préavis d'une ligne à la mère au moment du geste,
   sans attendre de signal (feu R-2887, P1) ; si une attente devait survenir, poser d'abord les automates manquants (minuterie puis
   garde, au prix lu, à défaut au prix de l'offre).
8. **Prix lu sur l'instance** (m9) : `… suivi_vast_v6 instance <ID>` → `dph_total` (stockage compris) **≤ 0,73 exigé** (feu R-2887), sinon
   destruction selon l'étape 15 et message. C'est ce prix lu (<PRIX>) qui sert aux étapes 9 et 10.
9. **Minuterie v4** par identifiant, posée aussitôt (R10), comptée depuis la création (P, puis dans la même commande) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 12 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-b-alpha-v3.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-b-alpha-v3.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v4 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v3.txt
   ```
   D = 90 % du plafond au prix lu (53 260 s à 0,73 ; 82 216 s à 0,4728) ; bornes de la v4 : 600 à 129 600 s. PID lu dans le fichier
   écrit par la minuterie, **jamais** `$!`. Non armée → destruction selon l'étape 15, message.
10. **Garde de dépense v4**, détachée, son PID écrit par elle-même avant `exec`, l'outil trouvé par le `PATH` passé explicitement
    (P, puis) :
    ```
    F=docs/notes/neuron-lens-v1/pid-garde-b-alpha-v3.txt; rm -f "$F"
    setsid nohup bash -c 'echo $$ > "$0"; exec env PATH=/home/user/vastai-env/bin:$PATH PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --instance <ID> --prix-h <PRIX> --plafond 12 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-b-alpha-v3.jsonl' "$F" \
      >> docs/notes/neuron-lens-v1/garde-b-alpha-v3.log 2>&1 < /dev/null &
    sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep garde_depense_v4 && echo "$(date -u +%FT%TZ) garde PID $P instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v3.txt
    ```
    → vivante et portant la garde exigé (sinon destruction selon l'étape 15, sur préavis d'une ligne) ; compte rendu à la mère à
    **7,20 USD** (60 %), destruction réessayée et vérifiée à **10,80 USD** (90 % ; code 4 et message immédiat si elle échoue).
11. **Rappels** (`send_later`) : (a) à **4,9 h** de location, compte rendu en durée à la mère (haut de l'attendu, M3) ; (b) à **9,2 h**,
    pire cas de la course : la mère décide ; (c) à **80 % de D** : « vérifier et détruire l'instance <ID> » ; puis commit et poussée de
    `pids-b-alpha-v3.txt` sur `prep/neuron-lens-v1`. **Veille** en tâche de fond (2 h au plus, relancée à chaque contrôle), P puis :
    ```
    for i in $(seq 1 24); do
      for n in "minuterie minuterie_destruction_neuron_lens_v4" "garde garde_depense_v4"; do set -- $n
        P=$(cat docs/notes/neuron-lens-v1/pid-$1-b-alpha-v3.txt 2>/dev/null)
        if [ -n "$P" ] && ps -p "$P" -o args= | grep -q "$2"; then s=vivante; else s=MORTE; fi
        echo "$(date -u +%FT%TZ) veille $1 PID ${P:-absent} $s" >> docs/notes/neuron-lens-v1/veille-b-alpha-v3.log
      done; sleep 300
    done
    ```
    Une ligne « MORTE » (redémarrage du conteneur de la session : deux fois au volet A) → réarmement aussitôt, par les étapes 9 et 10,
    **sur la même échéance absolue** (la durée D est recomptée depuis `<ISO_CREATION>`), PID relus dans les fichiers, arguments vérifiés ;
    message à la mère. À chaque réveil de la session, minuterie et garde sont vérifiées par leur PID (feu R-2887, R4).

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_alpha_v5.sh`, sans intervention)
12. Commit égal à `COMMIT_REDUIT` (code 10) ; arbre propre au premier départ (code 10) ; RUN_ID et GO_ID valides (code 17) ; première
    poussée vérifiée (code 14, avant l'environnement) ; `pip` 26.2.2 puis les versions épinglées (`requirements-neuron-lens-b-alpha-v1.txt`),
    **verbeux, sous `timeout` 3 600 s pour chacun des deux appels** (code 16 ; durée journalisée ; pire cas 2 h, contre 1,5 h au devis : déclaré) ; carte (code 11) ; essais de nos modules (143, code 12 sur échec,
    essai sauté ou arbre sali) ; puis les étapes du lanceur dans l'ordre de `suite` : `preparer` (correctifs appliqués, empreintes avant
    et après, manifeste R9) → `telecharger-tokeniseur` (**clé**) → `b0` → `telecharger-poids` (**clé** ; ensuite retirée de la course,
    vérifiée par son nom) → `corpus` (en ligne, sans clé) → `partie2` (scellée sur la machine ; tout écart = arrêt) → `fumee` (refusée
    sans la partie 2 sans écart) → `passe` → `b3` → `measure` (**`--ctx-batch 16`**, écart de lot déclaré, R-2901) → `score` → `grandeurs` (fidèles à `score`) → `verdicts` → audits R4 s'ils
    sont requis (même machine) ; **pour l'audit « tout négatif », le champ `lecture` du résultat est une lecture proposée, non tranchée :
    aucun verdict après cet audit sans la décision de Lazar (point (b), nœud de Lazar)** ; les écarts `logit`, `J` et `hub` sont versés
    tous les trois. La partie 2 est **scellée avant la fumée** (garde du lanceur) et **poussée au plus 10 min après** (poussée
    périodique) : le lanceur n'attend pas la poussée. Poussées vérifiées sur `calcul/neuron-lens-b-alpha-v3` toutes les 10 min, à la fin et à tout arrêt ;
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
    la garde lus ; `vastai destroy instance <ID> -y < /dev/null` ; `… suivi_vast_v6 absente <ID> --temoin
    <témoin>` code 0 exigé ; minuterie et garde arrêtées **par PID** après `ps -p <PID> -o args=` (minuterie v4, garde v4), mortes 2 s après ;
    rappels annulés ; journaux et fichiers de PID commités ; crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et
    `registres/depenses.md` ; **révocation de la clé `HF_TOKEN`** recommandée à Lazar (devis v2, § 5).

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v8.sh`, journal versé `devis-b-alpha/essai-a-blanc-amorce-b-alpha-v8.txt`.
Joué le 2026-11-15 sur le commit source `09425238…` (dépôt réduit v6 : commit réduit `b09e29cd…`, 347 fichiers, **liste
`0293f4e19b5f9fc422470ee91be6705aa3b39fc9b6b9cf8b3929e70af75971b1`**, paquet `7640465d…`) : **verdict automatique : conforme, 0 écart** ;
cas de l'essai v6 (nominal avec **143** essais réels, relance, reprise après arrêt brutal, échec 20, 14 formes, gardes, balayage, 0
processus restant ; environnement exact des essais de B0 : conforme) et, neuf (`essai_environnement_b0_v2.py`), les **appels de `measure`
contrôlés par programme** : `measure --ctx-batch 16` et `measure --ctx-batch 16 --seed 1`, aucun autre paramètre de mesure, hors ligne,
sans secret ; artefact : le lanceur v2 est pris en défaut (`--ctx-batch 16` absent aux deux graines). La liste attendue de l'étape 5 est
cette liste-ci. Avant lui, l'essai v7 avait un défaut d'essai (son compte des appels prenait aussi les lignes d'artefact), corrigé en v8.
Non couverts, déclarés : comme en v3 ; la mémoire de pointe à `--ctx-batch 16` est estimée, non mesurée
(`devis-b-alpha/memoire-measure-b-alpha-v1.md` : ≈ 16,5 GiB alloués, marge ≈ 4,7 GiB contre 23,57 GiB).

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
  épinglé dans les exigences (mineur 9, à la prochaine version) ; `INSTANCE_ID` vide dans la partie 2 (identifiant consigné dans
  `pids-b-alpha-v3.txt`) ; empreinte de la lentille J de Qwen3-8B consignée sans référence (audit « tout négatif ») ; intervalles pour
  `npR` et `logit` (« steer 1x ») seulement, les grandeurs par pôle versées permettant les autres ; avertissement de git (« push
  negotiation failed ») à la poussée vers le dépôt nu de l'essai, sans effet ; aucun essai ne joue `etape_partie2`,
  `etape_telecharger_tokeniseur` réel ni `releve_partie2` avec l'environnement de l'amorce (c'est par là qu'est passé M1 : à la prochaine
  version du lanceur).
- Point (a) : `corpus` en ligne sans clé, accepté par la mère (écart à la lettre du devis seulement ; accès anonyme aux jeux publics, un
  refus pour excès de requêtes arrêterait l'étape sans fuite). Point (c) : convention de capture de J non nommée par ses fichiers, à
  écrire au rapport de B-4 et à la partie 2. Point (d) : `test_cibles_invisibles_v4`, avant toute fusion dans `main`.

## Devis (v2 ; pire cas recompté par la vérification courte)
Attendu ≈ 1,2 à 2,5 USD ; pire cas de la course 9,2 h au devis ; pire cas complet par les bornes codées 14,7 h (relecture du
différentiel de la v2, R2) × 0,73 = 10,73 USD, sous l'arrêt dur de 10,80 ; plafond 12 USD. Déjà dépensé sur la ligne : ≈ 0,85 USD
(première course, instance 60770175, ≈ 0,06 ; relance, instance 60773264, ≈ 0,71 plus ≈ 0,1 de trafic).

## Empreintes des pièces citées
| pièce | sha256 |
|---|---|
| `docs/notes/neuron-lens-v1/commande-b-alpha-v4.md` | `f54d5ec38c989f278f9fba8799068890ee71c01f52b69ed8c1efed6c75a7da8e` |
| `docs/notes/neuron-lens-v1/journal-course-b-alpha-v2.md` | `48f55ea88a6299c238726e13caef98391a2c9f468a383a3df00253e4eb16bebc` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/memoire-measure-b-alpha-v1.md` | `423d79553ae6bca71098623ff1c45033598efbe45c6abb604871cc20ff870da5` |
| `src/controle_ia/neuron_lens/b_alpha_lancer_v3.py` | `44bba9c04b55287037b5283402173a5f0f1cd02320eac652a43651735991cda2` |
| `tests/test_neuron_lens_b_alpha_lancer_v3.py` | `0b1fb66f50e29c7b5fb806393962043ee08efb0bed2b6ecbfad4119f3ec463a6` |
| `scripts/amorce_neuron_lens_b_alpha_v5.sh` | `085c9d071988de0c5712f11981550cb94d5a6cf5f829111c4c972f142d0af341` |
| `scripts/depot_reduit_neuron_lens_b_alpha_v6.py` | `97c41abff21b060bf738ba9244dd93b0a927f4712e6e5f0c7bc48115a1e298a8` |
| `scripts/essai_environnement_b0_v2.py` | `1e7ed65b5c980c4d6ce725261ebb3f8e8dcdd4cade1ba6aad9661d6670106706` |
| `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v8.sh` | `723674fa26f35bd6c64dfb0eacd001c8c6b799a37ca94f7a1f8a75322e4e4324` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/essai-a-blanc-amorce-b-alpha-v8.txt` | `ece58ca4ea753732ddb458be1e6761682c5f8150b6cbf2422e1cced61340a816` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md` | `61c394f570a15a58067488b338ca46ade5734bf9f7446964100933e7a458de13` |
| `src/controle_ia/neuron_lens/garde_depense_v4.py` | `6a98d816a0917b7e3a7029ce105a3f0047a765f494b5ec07032b05836a1a0310` |
| `src/controle_ia/neuron_lens/suivi_vast_v6.py` | `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f` |
| `scripts/minuterie_destruction_neuron_lens_v4.sh` | `4511368311b557b89803ff41900d3139a4c2a898212e8ef28a178e38fa7e3082` |
| `requirements-neuron-lens-b-alpha-v1.txt` | `ef184e589a24f293356880419636d4b909ae8b76d0a95a50e0b50483338a2887` |
