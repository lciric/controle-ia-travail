# Commande de location et de lancement de la tranche B-α de « Neuron Lens » — v1, sans ssh (proposée, **non exécutée**)

Pièce 7 du § 6 du devis B-α v2 (`devis-b-alpha/devis-tranche-b-alpha-v2.md`, `61c394f5…`). Écrite par la fille « Neuron Lens » le
2026-11-15, sur l'accord de la mère (R-2863) ; **aucune location ni dépense avant son feu**. Reprend la commande v14 du volet A
(`commande-volet-a-v14.md`, `14fe6383…`), jouée le 14 novembre, aux points que B-α change : ligne GO-2026-11-14-06 (12 USD, échéance
2026-11-30), second secret `HF_TOKEN` (GO-2026-11-15-04), RTX 4090 à prix lu ≤ 0,80 USD/h, bornes en durée, minuterie v4, amorce B-α v3,
lanceur `b_alpha_lancer_v1`, entrée idempotente. Rien de la v14 n'est retiré sans être dit.

**Préambule P** (le shell ne garde rien d'un appel à l'autre) :
`cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`
**Intouchables** (jamais arrêtées, jamais détruites) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*`, et
toute instance d'une autre session. **Jamais** de `vastai show … --raw` imprimé (la configuration porte les deux secrets) : tout passe par
`suivi_vast_v6`. Secrets lus **par leur nom** seulement ; aucune valeur affichée, écrite ni versée.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur `vastai` 1.11.0 à `/home/user/vastai-env/bin/vastai` (le créer s'il manque, comme en v14) ; avec P :
   `vastai show user --raw > /dev/null` au code 0 exigé (sortie jetée).
2. **Secrets présents, par leur longueur** : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ] && [ ${#HF_TOKEN} -ge 8 ]` (le suivi v6 balaie
   les deux : sans `HF_TOKEN` dans la session, sa forme ne serait pas balayée). Sinon arrêt, message à la mère.
   **Suivi prêt** : `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 verifier` → code 0 ;
   `… suivi_vast_v6 instances` → code 0, liste consignée (identifiants et états) ; un **témoin** d'une autre session qui doit durer
   (60480302 ou 60670453) est noté pour l'étape 13. Sinon aucune création.
3. **Crédit** : `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print({k: d.get(k) for k in ("credit", "can_pay", "has_billing", "billing_failed", "autobill_threshold", "autobill_amount")})'`
   → `can_pay` vrai, `has_billing` vrai, `billing_failed` faux exigés (champ absent ou nul = arrêt) ; consigné (R-2788, R-2795).
4. **Prix du jour** (devis v2, § 2 ; aucun repli, M4) :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=150 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.80 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA et **prix du trafic** (`inet_up_cost`, `inet_down_cost`)
   consignés. **Aucune offre → rien ne part**, message à la mère (nœud : autre carte, mot de Lazar).
5. **Dépôt réduit** au commit scellé de la course :
   `.venv/bin/python scripts/depot_reduit_neuron_lens_b_alpha_v4.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json`, paquet
   `neuron-lens-b-alpha-reduit.bundle` ; **liste attendue : celle de l'essai à blanc** (voir plus bas ; une liste différente exige un
   nouvel essai à blanc). Branche dédiée du dépôt de travail : `course/neuron-lens-b-alpha-reduit-v4`
   (`git fetch <paquet> course:refs/heads/course/neuron-lens-b-alpha-reduit-v4 && git push origin course/neuron-lens-b-alpha-reduit-v4`) ;
   `git ls-remote origin refs/heads/course/neuron-lens-b-alpha-reduit-v4` = commit réduit ; `git ls-remote origin
   refs/heads/calcul/neuron-lens-b-alpha-v1` **vide** (branche des résultats absente ; sinon arrêt).
6. **RUN_ID** fixé ici une fois pour toutes (`<AAAAMMJJ-HHMMSS>-neuron-lens-b-alpha`, heure UTC de cette étape) : le même à chaque relance
   du conteneur par le loueur (entrée idempotente).

## 1. Location (une seule instance), minuterie, garde, rappels
7. Création (image `python:3.12-bookworm` ; disque 150 Go), sortie réduite par le suivi :
   ```
   date -u +%FT%TZ   # <ISO_CREATION>, relevée dans la même commande
   GO_ID=GO-2026-11-14-06 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 150 --label neuron-lens-b-alpha \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-06 -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-b-alpha-v1 -e PERIODE_POUSSE_S=600" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-b-alpha-reduit-v4 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_alpha_v3.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   Les deux secrets ne sont développés que par le shell du lancement (dans `--env`) ; les `$` entre apostrophes le sont sur la machine.
   **Entrée idempotente** : à une relance, le clone est sauté (`[ -d depot/.git ]`, leçon du volet A : « depot already exists » en
   boucle) et l'amorce relit son état (attente sans calcul après l'état final ; reprise sinon). → identifiant et heure consignés
   (`echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v1.txt`).
   Échec (pas de `new_contract`, ou `success` faux) → comme en v14 : `instances`, destruction éventuelle selon l'étape 13, message.
8. **Prix lu sur l'instance** (m9) : `… suivi_vast_v6 instance <ID>` → `dph_total` (stockage compris) **≤ 0,80 exigé**, sinon
   destruction selon l'étape 13 et message. C'est ce prix lu (<PRIX>) qui sert aux étapes 9 et 10.
9. **Minuterie v4** par identifiant, posée aussitôt (R10), comptée depuis la création (P, puis dans la même commande) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 12 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-b-alpha-v1.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-b-alpha-v1.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v4 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-b-alpha-v1.txt
   ```
   D = 90 % du plafond au prix lu (48 600 s à 0,80 ; 85 506 s à 0,4547) ; bornes de la v4 : 600 à 129 600 s. PID lu dans le fichier
   écrit par la minuterie, **jamais** `$!`. Non armée → destruction selon l'étape 13, message.
10. **Garde de dépense v4**, détachée, comme en v14, avec `--plafond 12` (compte rendu à la mère à **7,20 USD**, destruction réessayée et
    vérifiée à **10,80 USD**), journal `journal-depense-b-alpha-v1.jsonl`, sortie `garde-b-alpha-v1.log`, PID dans
    `pid-garde-b-alpha-v1.txt` écrit par elle-même.
11. **Rappels** (`send_later`) : (a) à **4,9 h** de location, compte rendu en durée à la mère (haut de l'attendu, M3) ; (b) à **9,1 h**,
    pire cas de la course : la mère décide ; (c) à **80 % de D** : « vérifier et détruire l'instance <ID> » ; puis commit et poussée de
    `pids-b-alpha-v1.txt` sur `prep/neuron-lens-v1`. **Veille** en tâche de fond qui réarme minuterie et garde après un redémarrage du
    conteneur de la session (leçon du volet A : deux redémarrages), PID relus dans les fichiers, arguments vérifiés.

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_alpha_v3.sh`, sans intervention)
12. Commit égal à `COMMIT_REDUIT` (code 10) ; arbre propre au premier départ (code 10) ; RUN_ID et GO_ID valides (code 17) ; première
    poussée vérifiée (code 14, avant l'environnement) ; `pip` 26.2.2 puis les versions épinglées (`requirements-neuron-lens-b-alpha-v1.txt`),
    **verbeux, sous `timeout` 3 600 s** (code 16 ; durée journalisée) ; carte (code 11) ; essais de nos modules (139, code 12 sur échec,
    essai sauté ou arbre sali) ; puis les étapes du lanceur dans l'ordre de `suite` : `preparer` (correctifs appliqués, empreintes avant
    et après, manifeste R9) → `telecharger-tokeniseur` (**clé**) → `b0` → `telecharger-poids` (**clé** ; ensuite retirée de la course,
    vérifiée par son nom) → `corpus` (en ligne, sans clé) → `partie2` (scellée sur la machine ; tout écart = arrêt) → `fumee` (refusée
    sans la partie 2 sans écart) → `passe` → `b3` → `measure` → `score` → `grandeurs` (fidèles à `score`) → `verdicts` → audits R4 s'ils
    sont requis (même machine). Poussées vérifiées sur `calcul/neuron-lens-b-alpha-v1` toutes les 10 min, à la fin et à tout arrêt ;
    **balayage** des deux secrets (sept formes) avant chaque commit : une forme trouvée = rien n'est poussé ; fichiers de plus de 95 Mo
    exclus (`-causal.pt`, les activations et les tables restent sur l'instance, M6) ; état poussé : étape en cours, étapes faites,
    durée de la location, fin du journal de `pip`. Poussée finale persistante (10 essais à 60 s) ; état final écrit (`fin-b-alpha.txt`)
    pour qu'une relance n'en refasse rien.

## 3. Suivi, retour et destruction (conteneur de la session)
13. Suivi comme en v14 (`suivi_vast_v6 logs <ID> 40`, `instance <ID>`, état poussé de la branche des résultats ; `ps -p` sur les PID) ;
    **course figée** (R-2800) : `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite sans nouvelle poussée → arrêt ;
    **crédit** relu à chaque contrôle (< 1 USD en cours de course → arrêt) ; dépassement du pire cas d'une étape (champ
    `depassement_pire_cas` du résultat d'étape, ou étape en cours depuis plus que son pire cas dans l'état poussé) → compte rendu.
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
15. Journaux de la minuterie et de la garde lus ; `vastai destroy instance <ID> -y < /dev/null` ; `… suivi_vast_v6 absente <ID> --temoin
    <témoin>` code 0 exigé ; minuterie et garde arrêtées **par PID** après `ps -p <PID> -o args=` (minuterie v4, garde v4), mortes 2 s après ;
    rappels annulés ; journaux et fichiers de PID commités ; crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et
    `registres/depenses.md` ; **révocation de la clé `HF_TOKEN`** recommandée à Lazar (devis v2, § 5).

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v4.sh`, journal versé `devis-b-alpha/essai-a-blanc-amorce-b-alpha-v4.txt`.
Joué le 2026-11-15 à 09:07:28Z sur le commit source `53ca8e6b…` (dépôt réduit v4 : commit réduit `d4e6450b…`, 347 fichiers dont 276 du
dépôt voisin, **liste `6c1a9f6e354a6270091395ca3094db6c0a19d05f249bf0e147d1634612e52520`**, paquet `22d9f42a…`) : **verdict automatique :
conforme, 0 écart**. La liste ne dépend que du contenu de l'arbre : elle est la **liste attendue** de l'étape 5 (le commit réduit et le
paquet changent avec le commit source, que le message du commit réduit porte).
- nominal : 139 essais réels de nos modules passés ; 13 étapes, dans l'ordre ; clé aux deux seules étapes « jeton », hors-ligne aux neuf
  étapes « hors-ligne », ni `GH_TOKEN` ni `HUGGING_FACE_HUB_TOKEN` à aucune ; clé retirée après `telecharger-poids` (journalisé) ; 13
  résultats et l'état poussé (étapes faites, durée) sur la branche ; état final écrit ; code 0 ;
- relance après l'état final : attente sans calcul, aucun appel du lanceur ;
- reprise : machine tuée (`kill -9` du groupe, vérifié mort, zombies exclus) pendant `passe`, relancée **avec la clé de nouveau dans
  l'environnement** : reprise journalisée, essais non refaits, appels d'après : `passe b3 measure score grandeurs verdicts` (étapes faites
  non rejouées, `passe` rejouée), clé absente de tous ;
- étape en échec → 20, état « arret code 20 » poussé ; **sept formes de chacun des deux jetons** écrites par la course dans un journal :
  14 cas, chacun refusé par le balayage, code 15, forme absente des objets du dépôt distant et du journal de l'amorce ;
- gardes : mauvais commit → 10 ; arbre non propre → 10 ; RUN_ID invalide → 17 ; COMMANDE_LANCEUR hors jouet → 13 ; `pip` sous délai → 16 ;
  première poussée impossible → 14 ; essai en échec → 12 ; essai sauté → 12 ;
- balayage final des deux jetons (14 formes du suivi v6) : témoins 14 sur 14 ; 0 fichier ; 0 ligne dans les objets du dépôt distant ;
  aucun processus restant.
Trois versions avant celle-ci, toutes archivées : l'essai v1 a trouvé un **défaut réel de l'amorce v2** (`env … lanceur` ne peut pas
appeler une fonction du shell : la course ne partait pas), corrigé en v3 ; les essais v2 et v3 avaient deux défauts **de l'essai**
(`&` sur toute la liste, donc rien de tué ; zombies comptés vivants).
Non couverts, déclarés : vraie course et vrai lanceur sur la machine (essayé dans le conteneur à part : `preparer` réel sur une copie du
dépôt réduit, correctifs appliqués, manifeste, `suite`, refus de `b0` sans préalable), `pip` complet, carte réelle, clone HTTPS réel,
sérialisation réelle de `--args` par l'outil du loueur, signaux autres que l'arrêt brutal.

## Jetons
- Jeton du programme : écriture sur tout le dépôt de travail ; « jamais vers `main` » n'est garanti que par l'amorce (réserve inchangée).
- `HF_TOKEN` : exposition résiduelle déclarée (devis v2, § 5, M5) : configuration de l'instance chez le loueur jusqu'à la destruction,
  environnement du processus d'entrée et du shell principal de l'amorce pendant toute la location (pour le balayage), retour à chaque
  relance ; `env -u` ne la retire qu'aux enfants. Recommandation (mère → Lazar) : clé neuve, lecture seule, limitée à ce modèle, révoquée
  après la course.

## Devis (v2, inchangé)
Attendu ≈ 1,2 à 2,5 USD ; pire cas complet 13,4 h × 0,80 = 10,72 USD, sous l'arrêt dur de 10,80 ; plafond 12 USD.

## Empreintes des pièces citées
| pièce | sha256 |
|---|---|
| `docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v2.md` | `61c394f570a15a58067488b338ca46ade5734bf9f7446964100933e7a458de13` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `docs/notes/neuron-lens-v1/addendum-empreintes-v3.md` | `e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82` |
| `docs/notes/neuron-lens-v1/commande-volet-a-v14.md` | `14fe638334ece83a5f5f6927b49e1e1aaea2a74953b6f3747ba01c76bd1eb26a` |
| `docs/notes/neuron-lens-v1/correctifs/causal_lens-graine-v1.diff` | `c8e53f7d265f3d2912b2fffec3869e94e398194b9423537aaeb3116951daa469` |
| `docs/notes/neuron-lens-v1/correctifs/correctif-causal_lens-graine-v1.md` | `95c715c2ab813a5a6d6700103f9d56d7580088977d5bc7802c7cfc6a44f9c0d0` |
| `docs/notes/neuron-lens-v1/correctifs/essai-causal_lens-graine-v1.py` | `ede719f65640d6af90e6999ad5bdd07d291522754b6e48f58ddeeae21b962b4b` |
| `docs/notes/neuron-lens-v1/correctifs/essai-crochets-causal_lens-llama-v1.py` | `6a9fe088cc47529bc87f2fce4aaaf9690a830766c12e1dc6bdb4969ad26f9c66` |
| `docs/notes/neuron-lens-v1/correctifs/note-essai-crochets-causal_lens-llama-v1.md` | `8cf35756ac92513f76fbdddd43bccc3f2c954da5158d94ce28118fd98929f382` |
| `docs/notes/neuron-lens-v1/correctifs/pre-essai-crochets-harnais-v1.py` | `20ac07385ae38a2517e8864da1337c81e0f9fc52d002e7b34f5e26ef9f3d6ea2` |
| `docs/notes/neuron-lens-v1/correctifs/pre-essai-crochets-harnais-v1.txt` | `7339da764077ea024053eb58939e0550dd61272213cda4d1b4130c2586fa6e97` |
| `src/controle_ia/neuron_lens/grandeurs_b_alpha_v1.py` | `6336a08945fd5078276985d1b2eef0910ecd5c3d02a2685e226dcb08364b2b8f` |
| `tests/test_neuron_lens_grandeurs_b_alpha_v1.py` | `7408862fe078f0c23c49fc462eca5d2e9ab44615413834917205a1d12b55d8fc` |
| `src/controle_ia/neuron_lens/addendum_partie2_b_alpha_v1.py` | `1cedde7e3e82330a985f397f64197b9aee8e161574b549984e34938102e9b6ac` |
| `tests/test_neuron_lens_addendum_partie2_b_alpha_v1.py` | `e208abc9093329fd1f34e2ee89480297b0d6f1cbbafabf1877cec042997a50ec` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/lecture-config-credit-neuronpedia-v1.md` | `90e2d7ef23b7ce107035f2a6814ce93a12457aec869316c6da4951b0ac65357b` |
| `src/controle_ia/neuron_lens/b_alpha_lancer_v1.py` | `99a3eb9db1d6956c2db42ccde560b006a5470950a6e71c70ba2cbd57dcfe79f9` |
| `tests/test_neuron_lens_b_alpha_lancer_v1.py` | `71111bd719db647a61da8d51f494162a160cedced2b1b3d4d99f17c2787c86a3` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/note-lanceur-b-alpha-v1.md` | `30c4e8a56d419e3eca890f4d1f7ba9746eee133bc6f6605c947fc89fae1656d6` |
| `scripts/amorce_neuron_lens_b_alpha_v3.sh` | `ffe371c88e0a5b23fcfe9a00352ff8601c40334f4212b20d4f9fba003aa68196` |
| `scripts/minuterie_destruction_neuron_lens_v4.sh` | `4511368311b557b89803ff41900d3139a4c2a898212e8ef28a178e38fa7e3082` |
| `scripts/essai_minuterie_neuron_lens_v4.sh` | `7beb0ed822ef4cce7858c50c7babc01b8fdcfbc6e69b52f4f193a15010b8d567` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/essai-minuterie-v4.txt` | `8c101459bb42277e1fd70a12fc4f48af8a00f044f07ada7a170c74d68e3d79c0` |
| `scripts/depot_reduit_neuron_lens_b_alpha_v4.py` | `d2f85d1970bdb1bed63974e46046c608a9560f042aaf8c3566e614efff7524f3` |
| `src/controle_ia/neuron_lens/balayage_arbre_v1.py` | `81e09317821bd64e576810bd8246ac92537ed40d3f6204fe8497ae2f65784f28` |
| `tests/test_neuron_lens_balayage_arbre_v1.py` | `114296ee095b4af9d965f445cde254d9f8e4398bb63ede35a91c7e48bb63f781` |
| `requirements-neuron-lens-b-alpha-v1.txt` | `ef184e589a24f293356880419636d4b909ae8b76d0a95a50e0b50483338a2887` |
| `src/controle_ia/neuron_lens/garde_depense_v4.py` | `6a98d816a0917b7e3a7029ce105a3f0047a765f494b5ec07032b05836a1a0310` |
| `src/controle_ia/neuron_lens/suivi_vast_v6.py` | `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f` |
| `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v4.sh` | `64720ccac1cf93736265b264b9c9dcee111b118fcd8d62121af748394f524bab` |
| `docs/notes/neuron-lens-v1/devis-b-alpha/essai-a-blanc-amorce-b-alpha-v4.txt` | `bee5a709364bd3ac43d4a84853cd9924b41bce0c54ceed4ccd848cc6114367b7` |
