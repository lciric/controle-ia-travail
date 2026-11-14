# Commande de location et de lancement du volet A de « Neuron Lens » — v6, sans ssh (proposée, **non exécutée**)

Remplace la v5 (`commande-volet-a-v5.md`, `112de376…`, archivée) après sa contre-lecture 7
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-7-commande-v5.md`, `4f05aa7f…`), faite et intégrée par la session de reprise
(autre compte, `prep/neuron-lens-v1`, passation de la fille du 14 novembre 13:07 UTC). Suites données aux remarques :
1 → coquille corrigée, tableau des empreintes ci-dessous ; 2 a → signalé (« Secrets ») ; 2 b → sortie de la création réduite par
`suivi_vast_v2 creation` ; 3, 4 b, 4 c → règle « instance sortie » de l'étape 11 ; 4 a → amorce v3, code 15 ; 5 → amorce v3 (exclusion
avant `git add`) ; 6 a-c, 6 d → amorce v3 ; 6 e → info, inchangé ; 6 f → étape 9 reformulée ; 7, 8, 9 a, 9 c-e → `suivi_vast_v2.py` et
son essai (28 passés) ; 9 b → inchangé (déjà correct) ; 10 → dépôt réduit v7 ; 11, 12 a, 12 b, 13 → essai à blanc v3 et son journal ;
l'essai à blanc v3 a trouvé un défaut de l'amorce v3 (au code 14, l'alarme « ne pas détruire » était écrite sans aucun résultat à
sauver) → amorce v4, dépôt réduit v8, essai à blanc v4 (les v3 et v7 restent archivées, scellées, non employées) ;
12 c → non éprouvé, déclaré ; fonctionnement fermé du balayage gardé (une sortie à secret est refusée entière, jamais expurgée : si les
journaux du loueur deviennent illisibles pour cette raison, le suivi passe par la branche des résultats seule, et la mère est prévenue).

La v5 remplaçait la v4 (`417ca3b4…`), qui remplaçait la v3 (`992e11ac…`), dont le feu (R-2749) est tombé : le conteneur de la session
ne peut pas joindre la machine par ssh (mandataire réseau limité au HTTPS). Décision de la mère R-2752 : commande sans ssh — branche
dédiée du dépôt réduit, script de démarrage de l'instance, résultats poussés sur une branche du dépôt de travail privé, suivi par les
journaux et l'état de l'instance, filtrés.

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans un **nouveau feu écrit de la
mère, avec le numéro de ligne**, citant cette v6 et ses empreintes. Toute heure consignée vient de `date -u` dans la même commande.
Jamais vers `main`, jamais vers `lciric/controle-ia`, rien dans `registres/`. Ne jamais toucher les instances 58936096, 58936099,
58936100, 60480302, 60599797, ni aucune instance ou serveur d'une autre session (inventaire du 14 novembre 13:50 UTC, lecture seule :
chez le loueur, 58936096, 58936099, 58936100 « exited » et 60480302 « running » ; deux serveurs Hetzner d'une autre session).

**Secrets** : `VAST_API_KEY` reste dans le conteneur, lue par son nom. Le seul secret passé à la machine est le jeton du programme :
`GH_TOKEN` reçoit la valeur de `CONTROLE_IA_GITHUB_TOKEN_2`, développée par le shell du lancement, jamais affichée ni écrite. Elle
figure (a) dans la configuration de l'instance chez le loueur jusqu'à sa destruction, (b) dans la ligne de commande du processus de
création de l'outil du loueur, le temps de l'appel (visible par `ps` dans le conteneur de la session), (c) sur la machine, dans
l'environnement du processus d'entrée et dans la ligne de commande de chaque `git` le temps de son exécution (en-tête
`-c http.extraHeader`, base 64). Aucun **fichier** de la machine ni des résultats poussés ne la contient (essayé à blanc, brute et
encodée) ; l'adresse du dépôt et la configuration git ne la contiennent pas ; la course tourne **sans** elle (`env -u GH_TOKEN`).
Le modèle et les lentilles sont publics.

**Suivi** : tout appel à l'outil du loueur dont la sortie pourrait porter la configuration passe par
`src/controle_ia/neuron_lens/suivi_vast_v2.py` (champs filtrés ; refus de toute sortie portant un secret, brut, encodé pour une
adresse ou en base 64 ; refus de tourner si `CONTROLE_IA_GITHUB_TOKEN_2` manque au shell). L'outil doit être sur le `PATH` du
Python lancé, ou désigné par `VASTAI_OUTIL=<chemin>` ; sinon le suivi rend « outil introuvable » (jamais une absence).

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `vastai` 1.11.0, installé dans un environnement à part de l'espace de travail ; clé lue par son nom ;
   `export VASTAI_OUTIL=<chemin de l'outil>`.
2. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; print(json.load(sys.stdin)["credit"])'` → **crédit relevé**
   (seul ce champ est imprimé), consigné au journal. Crédit < 12 USD → arrêt, message à la mère.
3. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt. (Ni le coût du
   trafic ni le critère « vérifié » du loueur ne sont dans le filtre ; le trafic est surveillé par la garde au prix total.)
4. **Dépôt réduit** au commit scellé de la course :
   `python scripts/depot_reduit_neuron_lens_volet_a_v8.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json` (commit
   réduit, empreinte de la liste, empreinte du paquet), paquet `neuron-lens-volet-a-reduit.bundle`. Le commit réduit est poussé sur la
   **branche dédiée** `course/neuron-lens-volet-a-reduit-v8` du dépôt de travail :
   `git fetch <paquet> course:refs/heads/course/neuron-lens-volet-a-reduit-v8 && git push origin course/neuron-lens-volet-a-reduit-v8` ;
   puis `git ls-remote origin refs/heads/course/neuron-lens-volet-a-reduit-v8` = commit réduit, et
   `git ls-remote origin refs/heads/calcul/neuron-lens-volet-a-v1` **vide** (branche des résultats absente ; sinon arrêt).

## 1. Location (une seule instance), minuterie, garde, rappel
5. Création (image `python:3.12-bookworm` : git, venv et coreutils compris ; `torch` installé par `pip` avec ses bibliothèques CUDA),
   sortie réduite à `success` et `new_contract` :
   ```
   GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 80 --label neuron-lens-volet-a \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-05 -e RUN_ID=<AAAAMMJJ-HHMMSS>-neuron-lens-volet-a -e CACHE_HF=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-volet-a-v1 -e PERIODE_POUSSE_S=1800" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-volet-a-reduit-v8 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_volet_a_v4.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v2 creation
   ```
   → **identifiant d'instance** (`new_contract`) et heure de création consignés. (Les `$` des arguments sont entre apostrophes :
   développés sur la machine, pas dans le conteneur ; seul `$CONTROLE_IA_GITHUB_TOKEN_2` de `--env` est développé par le shell du
   lancement. `--args` est une liste transmise telle quelle, `["-c", "<texte>"]`, d'après la source de l'outil 1.11.0 : lu, non éprouvé.)
   Sortie illisible ou sans `new_contract` → `… suivi_vast_v2 instances` pour savoir si une instance a été créée malgré tout ; arrêt.
6. **Minuterie de destruction par identifiant**, posée aussitôt (R10), durée comptée depuis la création :
   `D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>)`
   puis en arrière-plan `sleep $D; vastai destroy instance <ID>` (PID consigné).
7. **Garde de dépense** en arrière-plan (PID consigné) :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`
   → compte rendu à la mère à 60 % (6 USD, elle décide de la suite) ; destruction réessayée et vérifiée à 90 % (9 USD ; code 4 et
   message immédiat à la mère si elle échoue).
8. **Rappel indépendant** : `send_later` à 80 % de la durée de la minuterie, « vérifier et détruire l'instance <ID> ».

## 2. Sur la machine (script `scripts/amorce_neuron_lens_volet_a_v4.sh`, sans intervention)
9. Commit égal à `COMMIT_REDUIT` et arbre propre, sinon arrêt (code 10, visible dans les journaux seulement) ; environnement aux
   versions épinglées (`pip` 26.2.2 compris) ; carte graphique exigée (code 11) ; première poussée (« environnement pret ») impossible →
   arrêt (code 14 : la location court déjà depuis l'installation de `torch`, 5 à 10 min, mais aucune passe n'a commencé) ; essais
   rapides (liste de la v3), un échec, un essai sauté ou un arbre sali = arrêt (code 12) ; course `volet_a_lancer_v3` sans le jeton
   (`COMMANDE_COURSE` hors du mode jouet → code 13) ; poussée sur `calcul/neuron-lens-volet-a-v1` des `runs/<run_id>/`, `diag/<run_id>/`
   et d'un fichier d'état `etat-neuron-lens-volet-a.txt` à chaque étape, toutes les 30 min pendant la course, à la fin et à tout arrêt
   (sauf le code 10) ; un fichier de plus de 95 Mo est exclu de la poussée avant `git add` (il reste sur le disque de l'instance,
   journalisé) ; poussée finale persistante (10 essais espacés de 60 s, ≈ 10 min) ; si elle échoue alors que la course a été lancée :
   dernière ligne « POUSSEE FINALE EN ECHEC… » (code 15 si la course a réussi, sinon le code de la course) ; si aucune course n'a été
   lancée (codes 10 à 14) : dernière ligne « poussee finale en echec (aucune course lancee, aucun resultat a sauver) ». Le conteneur
   s'arrête à la fin du script.
10. Tout arrêt de la machine aux codes 10 à 14 (aucune course lancée, aucun résultat à sauver) : destruction par identifiant aussitôt
    lu, rapport à la mère. Course terminée ou en échec : étape 11, règle « instance sortie ».

## 3. Suivi, retour et destruction (conteneur de la session)
11. Suivi, **jamais par une sortie brute de l'outil du loueur** :
    `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v2 logs <ID> 40` (lignes `AMORCE …`) et
    `… suivi_vast_v2 instance <ID>` (champs `id`, `actual_status`, `dph_total`… ; un résultat `erreur` n'est jamais lu comme une
    absence) ; état de la course :
    `git fetch origin +refs/heads/calcul/neuron-lens-volet-a-v1:refs/remotes/origin/calcul/neuron-lens-volet-a-v1` puis
    `git show refs/remotes/origin/calcul/neuron-lens-volet-a-v1:etat-neuron-lens-volet-a.txt`.
    **Règle « instance sortie »** (« exited », stockage facturé) : avant toute destruction, lire l'état poussé et les journaux. Si l'état
    poussé est final (« course terminee », ou « arret code … ») et que la dernière ligne du journal n'est pas « POUSSEE FINALE EN
    ECHEC » : destruction aussitôt. Sinon (code 15, poussée en échec, état poussé non final) : **pas de destruction sans décision de la
    mère**, message immédiat (les résultats ne sont que sur le disque de l'instance) ; la minuterie et la garde à 90 % restent armées et
    la détruiront de toute façon à leur échéance : le signaler dans le message. De même, si la minuterie ou la garde tombent pendant la
    poussée finale (10 min), les résultats non poussés sont perdus : la durée de la minuterie, comptée sur le plafond, le rend improbable
    au devis (borne haute 7 USD sur 10) ; signalé.
12. Fin (« course terminee » ou arrêt) : récupération par cette branche ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ;
    fichiers exclus (plus de 95 Mo) relevés dans le journal ; copie dans `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
13. `vastai destroy instance <ID>` ; `… suivi_vast_v2 absente <ID>` → code 0 (absence prouvée seulement sur une liste lue sans erreur ;
    code 1 sinon, à reprendre) ; minuterie et garde arrêtées **par PID** ; rappel annulé ; crédit relevé de nouveau ; lignes proposées à
    la mère pour `registres/arrets.md` et `registres/depenses.md`.

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_v4.sh` ; journal complet versé (`docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v4.txt`,
empreinte au compagnon ; celui de la v3, qui a trouvé le défaut corrigé en v4, est versé aussi : `essai-a-blanc-amorce-v3.txt`). Joué
le 14 novembre à 13:59:57 UTC sur le commit source `d6821a29…` (commit réduit `fe3994c6…`, 73 fichiers, liste `98982cd5…`, paquet
`81495e13…` ; ces trois valeurs changeront au commit final de la course, qui porte aussi cette commande et ce journal) :
- cas nominal, **liste réelle** des essais rapides plus une sonde qui échoue si `GH_TOKEN` est dans l'environnement de pytest :
  62 passés ; course jouet sans jeton ; poussées périodiques ; fichier de 96 Mio exclu de la poussée (journalisé, resté sur le disque
  de la machine) ; état final « course terminee », code 0 ;
- artefacts (R5) : mauvais commit → 10 ; arbre non propre → 10 ; essai en échec → 12 ; essai sauté → 12 ; arbre sali par les essais →
  12 ; carte graphique absente (garde jouée en mode jouet) → 11 ; première poussée impossible → 14, dernière ligne « poussee finale en
  echec (aucune course lancee, aucun resultat a sauver) » ; poussée finale impossible après une course réussie → **15**, dernière ligne
  « POUSSEE FINALE EN ECHEC… » ; la sonde « sans jeton » jouée seule avec le jeton présent échoue (code 1) ;
- balayage du jeton factice sous 7 formes (brute, adresse, base 64 seule et en en-tête, trois alignements) sur les disques des
  machines d'essai, le dépôt distant et les journaux : **0 fichier**.
Non couverts, déclarés : le chemin réel de la machine (création de l'environnement, `pip`, carte réelle, vraie course), le code 13, le
clone HTTPS réel (le clone de l'essai est local : l'en-tête n'y sert pas), la sérialisation réelle de `--args` par l'outil du loueur.

## Jeton
Le jeton du programme permet l'écriture sur tout le dépôt de travail, `main` compris ; « jamais vers `main` » n'est garanti que par
l'amorce (poussée vers `refs/heads/calcul/neuron-lens-volet-a-v1` seulement). Si un jeton restreint à une branche existe, il est
préférable (point signalé à la mère, non tranché).

## Devis (inchangé depuis la v3, borne haute)
3,5 à 5,5 h, soit 3,2 à 5 USD à 0,90 USD/h, jusqu'à 7 USD si l'audit R4 « trop beau » se déclenche ; installation de `torch` et de ses
bibliothèques CUDA par `pip` en plus (≈ 5 à 10 min). Le débit réel n'est pas mesuré avant la course : la garde le surveille (6 USD
compte rendu, 9 USD arrêt dur). Si la version de CUDA de l'hôte ne convient pas à `torch` 2.14.1, l'amorce s'arrête au code 11 (quelques
minutes de location perdues).

## Empreintes des pièces citées
Toutes scellées (compagnon `.sha256`) ; la commande elle-même est au compagnon de ce fichier. Le commit réduit, la liste et le paquet
de la course sont rendus par le dépôt réduit v8 au commit final et cités dans la demande de feu.

| pièce | empreinte |
|---|---|
| `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-7-commande-v5.md` | `4f05aa7fcb5ede63244845afe86cf175d44867956778edb8e9d3c6a2c1d388af` |
| `scripts/amorce_neuron_lens_volet_a_v4.sh` | `26c78c11eee0dd506fc5669fde50da9af0a0fd00f195d0d8828c5a742e8125c8` |
| `src/controle_ia/neuron_lens/suivi_vast_v2.py` | `957ad4a633f18300e0551fad30b97b7db8a92d366728c2fa6218c2919bf02480` |
| `tests/test_neuron_lens_suivi_vast_v2.py` | `7e9a2c7982a5fb7f6800f74c32fb73fb82cd449d87ae2ec33c5484629f2dab03` |
| `scripts/depot_reduit_neuron_lens_volet_a_v8.py` | `dcabac908d52c6075daf477ccc489a79005c50b398c34c8c4b10973c04d24dbe` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v4.sh` | `33157763039e0761368b0243eebc4a3c3a85fcb085c694cf1e4834ed531553ef` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v4.txt` | `f3b66c09894c01b9d1fb1a632a4235853f273ffc12c015b2359000f908a76e4f` |
| `src/controle_ia/neuron_lens/garde_depense_v3.py` | `692fa80e842f18a54e7bc937b19c7cb9ff71678c02153eb0c46ec8e34b97cc3d` |
| `src/controle_ia/neuron_lens/volet_a_lancer_v3.py` | `a52506f897adf9f55e3dbce8b6a832d086b0d23866b1ab6d75e122fff906b036` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `requirements-neuron-lens-volet-a-v1.txt` | `f61477e91763fa251fbd45e93fb17819883c70c45a60fb5ebd90b01feaca2312` |
| archivées, non employées : `scripts/amorce_neuron_lens_volet_a_v3.sh` | `dceb7f7ed1bab0f2f91b1a89522294963bd573620d9709d62ba9959613ef7727` |
| `scripts/depot_reduit_neuron_lens_volet_a_v7.py` | `493f6b8741635e284afd2340bb91671ee0f2f91034c2d9392e73877ebb2bc88e` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v3.sh` | `4ab87223f6d8de34234ec67601041ab3709567912437180d4a04cb2ee1678ff0` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v3.txt` | `5cdf326d9cfa9d43c89f88e4fbafb30b74d22a0e0d340a916b69ace3a5c65f64` |
