# Commande de location et de lancement du volet A de « Neuron Lens » — v13, sans ssh (proposée, **non exécutée**)

v13 = v12 (`commande-volet-a-v12.md`, `71e1f182…`, archivée) après sa contre-lecture 12
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-12-commande-v12.md`), qui avait **une bloquante** (S-1). Changements :
- S-1 (bloquante) → suivi **v6** (`suivi_vast_v6.py`) : balayage du texte entier **avant** toute troncature (la v5 tronquait `error`,
  `msg` et la dernière ligne d'erreur à 200 caractères avant de balayer : un secret à cheval sur la coupure sortait en partie) ;
  sortie bornée à 2000 caractères seulement après balayage ; 67 essais, dont le secret à cheval sur l'ancienne coupure dans quatre
  champs, et l'artefact qui montre la fuite de la v5 ;
- S-6 → minuterie **v3** : suivi v6 et absence prouvée sur une liste **non vide** (`--non-vide`) ; une liste vide n'est plus une preuve
  (échec fermé, code 6) ; essai v3 conforme, 0 écart, cas « liste vide » compris ;
- S-3 → « destruction aussitôt » écrit partout « destruction selon l'étape 13 (avec `-y`, absence prouvée) » ;
- S-4 → étape 3 : un champ absent ou nul vaut arrêt ;
- S-7 → étape 13 : lire le journal de la minuterie (`minuterie-volet-a-v1.log`) et celui de la garde ;
- S-12 → étape 6 : en cas d'échec, l'identifiant et l'heure sont écrits dans `pids-volet-a-v1.txt` ;
- S-2 → cet en-tête annonce aussi les changements du **tableau des empreintes**, refait en entier à chaque version (pièces employées en
  tête, archives ensuite ; seules les pièces citées par la commande en cours y figurent ; les contre-lectures antérieures à la 11 et les
  commandes antérieures à la v11 n'y sont plus, elles restent scellées dans le dépôt) ;
- S-5, S-8, S-9 → info (voir « Réserves ») ; S-10 → la docstring de `garde_depense_v4.py` cite encore la destruction sans `-y` : écart de
  texte seul, le code passe `-y` (l.125), laissé tel quel (déclaré) ; S-11 → réserve.
Dépôt réduit, amorce, essai à blanc v7, liste `801b0202…` **inchangés**. Texte de la v12 ci-dessous, retouché aux seuls endroits listés.

**Réserves (contre-lecture 12)** : S-5 — le crédit n'est plus borné (R-2788) ; un crédit épuisé en cours de course, avant le
rechargement automatique, pourrait faire arrêter l'instance par le loueur avant la poussée finale (non traité ; à la mère et à Lazar) ;
la cause du `success: false` du 14 novembre reste inconnue (un nouvel échec au même point est possible, sans danger : fermé, coût
≈ 0,02 USD). S-11 — la garde v4 vérifie l'absence par `vastai show instance <id> --raw`, non éprouvé sur le vrai outil pour une instance
détruite : au pire fausse alerte (code 4) ou sortie « instance_absente » prématurée ; la minuterie v3 reste alors seule filet automatique.


v12 = v11 (`commande-volet-a-v11.md`, `e18da708…`, archivée ; feu R-2782, puis mot de Lazar R-2788) corrigée après la tentative du
14 novembre 2026 (journal `docs/notes/neuron-lens-v1/journal-course-volet-a-v1.md`) : création rendue `success: false` (instance
60669495 créée à l'arrêt), première destruction **abandonnée en silence** (l'outil 1.11.0 demande une confirmation [y/N], abandonne
sans entrée et rend le code 0), destruction refaite avec `-y`, absence prouvée ; aucune minuterie ni garde lancées ; coût ≤ 0,02 USD.
Changements, et seulement eux :
- **toute destruction** se fait avec `-y`, entrée fermée, et n'est tenue pour faite que si l'absence est prouvée
  (`suivi_vast_v6 absente`), jamais sur le code de sortie de l'outil : minuterie v2 (`scripts/minuterie_destruction_neuron_lens_v2.sh`,
  essai v2 conforme, 0 écart, qui reproduit le défaut sur la v1), garde de dépense v4 (`garde_depense_v4.py`, `-y`, entrée fermée,
  sortie vide de la lecture du prix = illisible ; 13 essais), étapes 6 et 13 ;
- **étape 3** selon R-2788 (mot de Lazar « vast se recharge seul go ») : la condition « crédit sous 12 USD → arrêt » devient « paiement
  possible et facturation active au relevé (`can_pay` vrai, `has_billing` vrai, `billing_failed` faux), sinon arrêt » ; crédit, seuil
  et montant du rechargement automatique relevés et journalisés ;
- **étape 6** : `suivi_vast_v6 creation` garde aussi `error` et `msg` (balayés) et rend le code 1 si `success` est faux, même avec un
  `new_contract` : arrêt, instance éventuellement créée détruite (`-y`) et absence prouvée, message à la mère avec la raison lue ;
- suivi `suivi_vast_v6` partout à la place de la v4 (62 essais).
Le dépôt réduit, l'amorce, l'essai à blanc v7 et la liste `801b0202…` sont **inchangés** (la garde, la minuterie et le suivi ne vont pas
sur la machine). Texte de la v11 ci-dessous, retouché aux seuls endroits listés.


v11 = v10 (`commande-volet-a-v10.md`, `7be3b223…`, archivée) avec une seule correction : dans le tableau des empreintes, la
contre-lecture 11 était marquée à tort « archivée, non employée » (filtre de la session sur le suffixe `v9.md`). Aucun autre changement.

v10 = v9 (`commande-volet-a-v9.md`, `39b65361…`, archivée) avec les corrections de texte de sa contre-lecture 11, ciblée
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-11-commande-v9.md`), qui conclut « bloquant pour la location : non »
(minuterie v1, son essai, son journal, essai de survie et pièce `pip` v2 « scellables en l'état » ; v9 « après corrections mineures ») :
R-1 → étape 6 : heure de création relevée par `date -u` dans la commande même de la création ; R-2 → étape 6 : ligne « instance,
création, prix » écrite dans `pids-volet-a-v1.txt` ; R-3 → étape 13 : « mort » après 2 s, un état `Z` (zombie) compte comme mort ;
R-4 → étape 13 : arguments du PID vérifiés avant tout arrêt ; R-5 → étape 13 : `sleep` orphelin mentionné ; R-6 → étape 5 :
`.venv/bin/python` ; R-7 → étape 13 : journaux de la minuterie et de la garde et fichiers de PID commités avec les résultats.
**Ces retouches sont appliquées telles que proposées et n'ont pas été relues par un contre-lecteur après coup (déclaré).**

Texte de la v9 (en-tête compris), retouché aux seuls endroits ci-dessus :

Remplace la v8 (`commande-volet-a-v8.md`, `afb08ad0…`, archivée) après sa contre-lecture 10, ciblée
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-10-commande-v8.md`), qui a trouvé deux points **bloquants** dans les étapes
7 et 8 de la v8 (le reste : amorce v6, suivi v4, dépôt réduit v10 « scellables en l'état »). Suites données :
- Q-1 (bloquante) → la minuterie n'est plus écrite en ligne : script scellé `scripts/minuterie_destruction_neuron_lens_v1.sh`
  (chemin absolu de l'outil, durée bornée, PID écrit par le processus lui-même, destruction réessayée), lancé détaché ; la durée est
  calculée et contrôlée dans la même commande, hors de toute liste mise en arrière-plan ; essai `scripts/essai_minuterie_neuron_lens_v1.sh`
  conforme (0 écart) ;
- Q-2 (bloquante) → l'état du shell ne persistant pas d'un appel d'outil à l'autre, chaque commande des étapes 1 à 13 commence par le
  **préambule P** ci-dessous (chemin concret de l'outil) ; la minuterie reçoit le chemin absolu ; la garde reçoit le `PATH` par
  `exec env PATH=…` ;
- Q-3 → essai gratuit de survie fait (`essai-survie-processus-detaches-v1.txt`) : minuterie détachée lancée dans un appel d'outil, vivante
  dans le suivant, échéance atteinte et faux outil appelé dans un troisième ; `PATH` transmis au processus détaché ; et constat :
  `$!` n'est **pas** le PID du processus détaché (le shell a le contrôle des tâches, `setsid` se duplique) — seuls les PID écrits par
  les processus eux-mêmes comptent ;
- Q-4 → PID, durée, identifiant et heure de création versés dans `docs/notes/neuron-lens-v1/pids-volet-a-v1.txt` ; `ps -p` exigé
  vivant (étapes 7, 8) puis mort (étape 13) ;
- Q-5 → durée bornée par la minuterie (600 à 108000 s : 90 % de 10 USD entre 0,30 et 0,90 USD/h), hors bornes = non armée, arrêt ;
- Q-6 → branches non jouées ajoutées aux « Non couverts » ; Q-7 → liste nominative des artefacts à refus ; contrôle du `grep` des objets
  dans l'essai v7 déclaré non fait (limite) ; Q-8 → pièce `pip` v2 (`verification-pip-26-2-2-v2.txt`, roue `fd7f4dfa…`) ; Q-9 → info
  (l'en-tête de l'amorce v6 cite encore la v7 ; `journaux()` du suivi v4 n'est plus appelée par `main` ; un nom de fichier exclu
  contenant une espace serait ambigu), inchangés.

Suites de la contre-lecture 9 (v8), gardées : P-1 → outil sur un chemin connu, `vastai show user` au code 0 ; P-2, P-3 → artefacts
« lsremote », « findko », « findmuet », « cpko », « index », « etat » joués à blanc (essai v7) ; P-4 → objets lus comptés, erreurs
comptées, témoin empaqueté ; P-5 → `--non-vide` ; P-6 → `exclus_fichiers=` ; P-7 → codes 1 sur erreur ; P-8 → table annotée ; P-9 →
« Secrets » reformulé, pièce `pip` ; P-10 → amorce v6 ; P-11 → info.

Raison de « pour un jeton de lettres, chiffres, `_` et `-`, la base 64 standard ne contient ni `+` ni `/` » (contre-lecture 9) : un tel
caractère demande un groupe de 6 bits commençant par cinq 1 ; ces octets ont le bit fort à 0 ; seul `_` porte cinq 1 consécutifs, à une
position impaire, alors que les groupes commencent aux positions paires. La sécurité n'en dépend pas : les deux familles de formes
sont produites pour tout secret.

Historique : v8 ← contre-lecture 9 ; v7 ← contre-lecture 8 ; v6 ← contre-lecture 7 ; v5 ← contre-lecture 6 ; v4 et v3 (`992e11ac…`, dont le feu R-2749 est
tombé : pas de ssh depuis le conteneur). Décision de la mère R-2752 : commande sans ssh — branche dédiée du dépôt réduit, script de
démarrage de l'instance, résultats poussés sur une branche du dépôt de travail privé, suivi filtré. Consigne de la mère R-2772 (nouveau
compte) : rien ne part avant la commande contre-lue et scellée, puis la demande de feu citant la commande, le commit réduit, la liste et
l'empreinte du paquet ; une seule instance.

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans un **nouveau feu écrit de la
mère, avec le numéro de ligne**, citant cette v13 et ses empreintes. Toute heure consignée vient de `date -u` dans la même commande.
Jamais vers `main`, jamais vers `lciric/controle-ia`, rien dans `registres/`. Ne jamais toucher les instances 58936096, 58936099,
58936100, 60480302, 60599797, ni les serveurs `poste-temoin-bailey-*`, ni aucune instance ou serveur d'une autre session (inventaire
du 14 novembre 13:50 UTC, lecture seule : chez le loueur, 58936096, 58936099, 58936100 « exited » et 60480302 « running » ; deux
serveurs Hetzner `poste-temoin-bailey-v9` et `-v12`).

**Secrets** : `VAST_API_KEY` reste dans le conteneur, lue par son nom. Le seul secret passé à la machine est le jeton du programme :
`GH_TOKEN` reçoit la valeur de `CONTROLE_IA_GITHUB_TOKEN_2`, développée par le shell du lancement, jamais affichée ni écrite. Elle
figure (a) dans la configuration de l'instance chez le loueur jusqu'à sa destruction (et dans ce que le loueur en écrit sur la machine,
non vérifié), (b) dans la ligne de commande du processus de création de l'outil du loueur, le temps de l'appel (visible par `ps` dans le
conteneur de la session), (c) sur la machine, dans l'environnement du processus d'entrée et dans la ligne de commande de chaque `git`
le temps de son exécution (en-tête `-c http.extraHeader`, base 64). Aucun fichier de l'arbre de travail, aucun résultat poussé, aucun
journal et aucun objet git des dépôts de l'essai ne la contient (essayé à blanc, sous 7 formes, avec témoins positifs) ; l'adresse du
dépôt et la configuration git ne la contiennent pas ; la course tourne **sans** elle (`env -u GH_TOKEN`). Le modèle et les lentilles
sont publics.

**Suivi** : tout appel à l'outil du loueur dont la sortie pourrait porter la configuration passe par
`src/controle_ia/neuron_lens/suivi_vast_v6.py` (champs filtrés ; refus de toute sortie portant un secret, brut, encodé pour une
adresse ou en base 64 ; refus de tourner si `CONTROLE_IA_GITHUB_TOKEN_2` manque au shell ; sortie vide = erreur ; code 1 sur erreur).
Un résultat `erreur` n'est jamais lu comme une absence. Le fonctionnement est fermé : une sortie à secret est refusée entière, jamais
expurgée ; si les journaux du loueur deviennent illisibles pour cette raison, le suivi passe par la branche des résultats seule, et la
mère est prévenue.

**Préambule P** (au début de **chaque** commande des étapes 1 à 13 ; l'état du shell ne persiste pas d'un appel d'outil à l'autre) :
`cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`

**Fichier des identifiants** : `docs/notes/neuron-lens-v1/pids-volet-a-v1.txt` (identifiant d'instance, heure de création, prix, durée
de la minuterie, PID de la minuterie et de la garde, avec l'heure de chaque ligne), écrit au fur et à mesure, commité et poussé sur
`prep/neuron-lens-v1` à l'étape 9 : une reprise de session y retrouve de quoi arrêter par PID et détruire par identifiant.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `vastai` 1.11.0, dans l'environnement à part `/home/user/vastai-env` (à créer s'il manque :
   `python3 -m venv /home/user/vastai-env && /home/user/vastai-env/bin/pip install -q vastai==1.11.0`) ; clé lue par son nom ; avec le
   préambule P : `command -v vastai` = `/home/user/vastai-env/bin/vastai` et `vastai show user --raw > /dev/null` au code 0 exigés
   (sortie jetée). Sinon arrêt.
2. **Suivi prêt** (gratuit) : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ]` (longueur seule, jamais la valeur) ;
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 verifier` → code 0 exigé ;
   `… suivi_vast_v6 instances` → code 0 exigé, liste consignée (identifiants et états seulement) ; une instance d'une autre session qui y
   figure et doit durer (60480302, « running » au relevé) sert de **témoin** à l'étape 13. Un échec, une forme inattendue ou un refus →
   **aucune création**, message à la mère.
3. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; d=json.load(sys.stdin); print({k: d.get(k) for k in ("credit", "can_pay", "has_billing", "billing_failed", "autobill_threshold", "autobill_amount")})'`
   → seuls ces champs sont imprimés, consignés au journal ; **`can_pay` vrai, `has_billing` vrai et `billing_failed` faux exigés**
   (un champ absent ou nul vaut arrêt), sinon arrêt, message à la mère (R-2788 ; le crédit n'a plus de seuil : rechargement automatique). (Relevé du 14 novembre 16:33:48Z :
   `can_pay` vrai, `has_billing` vrai, `billing_failed` faux, rechargement automatique de 5 USD sous 5 USD, crédit 4,99 USD.)
4. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt. (Ni le coût du
   trafic ni le critère « vérifié » du loueur ne sont dans le filtre ; le trafic est surveillé par la garde au prix total.)
5. **Dépôt réduit** au commit scellé de la course :
   `.venv/bin/python scripts/depot_reduit_neuron_lens_volet_a_v10.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json` (commit
   réduit, empreinte de la liste, empreinte du paquet), paquet `neuron-lens-volet-a-reduit.bundle` ; liste attendue `801b0202…` (celle
   de l'essai à blanc v7 ; une liste différente exige un nouvel essai à blanc ; le commit réduit et le paquet changent avec le commit
   source, dont le message du commit réduit porte le nom). Le commit réduit est poussé sur la **branche dédiée**
   `course/neuron-lens-volet-a-reduit-v10` du dépôt de travail :
   `git fetch <paquet> course:refs/heads/course/neuron-lens-volet-a-reduit-v10 && git push origin course/neuron-lens-volet-a-reduit-v10` ;
   puis `git ls-remote origin refs/heads/course/neuron-lens-volet-a-reduit-v10` = commit réduit, et
   `git ls-remote origin refs/heads/calcul/neuron-lens-volet-a-v1` **vide** (branche des résultats absente ; sinon arrêt).

## 1. Location (une seule instance), minuterie, garde, rappel
6. Création (image `python:3.12-bookworm` : git, venv et coreutils compris ; `torch` installé par `pip` avec ses bibliothèques CUDA),
   sortie réduite à `success` et `new_contract` :
   ```
   date -u +%FT%TZ   # heure de création (<ISO_CREATION>), relevée dans la même commande que la création
   GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 80 --label neuron-lens-volet-a \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-05 -e RUN_ID=<AAAAMMJJ-HHMMSS>-neuron-lens-volet-a -e CACHE_HF=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-volet-a-v1 -e PERIODE_POUSSE_S=1800" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-volet-a-reduit-v10 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_volet_a_v6.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   → **identifiant d'instance** (`new_contract`, éventuellement « extrait par motif ») et heure de création (la sortie de `date -u`
   ci-dessus, jamais une heure de mémoire) consignés, puis, dans l'appel suivant (préambule P) :
   `echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-volet-a-v1.txt`. (Les `$` des
   arguments sont entre apostrophes : développés sur la machine, pas dans le conteneur ; seul `$CONTROLE_IA_GITHUB_TOKEN_2` de `--env`
   est développé par le shell du lancement. `--args` est une liste transmise telle quelle, `["-c", "<texte>"]`, d'après la source de
   l'outil 1.11.0 : lu, et éprouvé le 14 novembre : l'instance 60669495 a été créée avec cette entrée.) Code non nul (aucun
   `new_contract`, ou `success` faux) → arrêt : `… suivi_vast_v6 instances` pour savoir si une instance a été créée malgré tout ; si oui,
   `vastai destroy instance <ID> -y < /dev/null` puis `… suivi_vast_v6 absente <ID> --temoin <témoin>` code 0 exigé (relancer sinon) ;
   identifiant et heure écrits dans `docs/notes/neuron-lens-v1/pids-volet-a-v1.txt` ; message à la mère avec `error` et `msg` lus.
7. **Minuterie de destruction par identifiant**, posée aussitôt (R10), durée comptée depuis la création. Préambule P, puis dans la
   **même commande** (aucune liste mise en arrière-plan : seul le lancement détaché porte un `&`) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-volet-a-v1.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v3.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-volet-a-v1.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v3 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-volet-a-v1.txt
   ```
   → PID lu dans le fichier écrit par la minuterie (**jamais** `$!`), vivant et portant le script, exigé ; durée hors bornes (600 à
   108000 s), outil absent, fichier impossible : la minuterie n'est pas armée (journal) → destruction selon l'étape 13 (avec `-y`, absence prouvée), message à la mère. C'est
   ce PID qu'on arrête (avant l'échéance, l'arrêt empêche la destruction ; essayé).
8. **Garde de dépense**, détachée, son PID écrit par elle-même avant `exec`, l'outil trouvé par le `PATH` passé explicitement.
   Préambule P, puis :
   ```
   F=docs/notes/neuron-lens-v1/pid-garde-volet-a-v1.txt; rm -f "$F"
   setsid nohup bash -c 'echo $$ > "$0"; exec env PATH=/home/user/vastai-env/bin:$PATH PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl' "$F" \
     >> docs/notes/neuron-lens-v1/garde-volet-a-v1.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep garde_depense_v4 && echo "$(date -u +%FT%TZ) garde PID $P instance <ID>" >> docs/notes/neuron-lens-v1/pids-volet-a-v1.txt
   ```
   → vivante et portant la garde exigé (sinon destruction selon l'étape 13, avec `-y` et absence prouvée, message à la mère) ; compte rendu à la mère à 60 % (6 USD, elle
   décide de la suite) ; destruction réessayée et vérifiée à 90 % (9 USD ; code 4 et message immédiat à la mère si elle échoue).
9. **Rappel indépendant** : `send_later` à 80 % de la durée `D` de l'étape 7, « vérifier et détruire l'instance <ID> (PID dans
   docs/notes/neuron-lens-v1/pids-volet-a-v1.txt) » ; puis commit et poussée de `pids-volet-a-v1.txt` sur `prep/neuron-lens-v1`.
   Limite déclarée : la minuterie et la garde vivent dans le conteneur de la session ; s'il est récupéré (longue inactivité), elles
   meurent avec lui ; le rappel réveille la session et le fichier versé permet de reprendre ; la session reste active pendant la
   course.

## 2. Sur la machine (script `scripts/amorce_neuron_lens_volet_a_v6.sh`, sans intervention)
10. Commit égal à `COMMIT_REDUIT` et arbre propre, sinon arrêt (code 10, visible dans les journaux seulement) ; première poussée
    (« commit verifie ») impossible → arrêt (code 14, avant l'installation de l'environnement : 19 s à blanc, sans délai réseau) ;
    environnement aux versions épinglées (`pip` 26.2.2 compris) ; carte graphique exigée (code 11) ; essais rapides (liste de la v3), un
    échec, un essai sauté ou un arbre sali = arrêt (code 12) ; course `volet_a_lancer_v3` sans le jeton (`COMMANDE_COURSE` hors du mode
    jouet → code 13) ; poussée sur `calcul/neuron-lens-volet-a-v1` des `runs/<run_id>/`, `diag/<run_id>/` et d'un fichier d'état
    `etat-neuron-lens-volet-a.txt` (`run_id`, `etat`, `heure`, `commit_reduit`, `exclus`, `exclus_fichiers`) à chaque étape, toutes
    les 30 min pendant la course, à la fin et à tout arrêt (sauf le code 10) ; une poussée n'est déclarée faite (« pousse : … ») que si
    chaque étape de sa préparation a réussi et si la tête distante égale la tête locale ; un fichier de plus de 95 Mo est exclu avant
    `git add` (il reste sur le disque de l'instance ; s'il avait déjà été poussé plus petit, cette version reste à la tête) ; poussée
    finale persistante après une course (10 essais espacés de 60 s, ≈ 10 min) ; si elle échoue : code 15 si la course a réussi, sinon
    le code de la course. Le conteneur s'arrête à la fin du script.

## 3. Suivi, retour et destruction (conteneur de la session)
11. Suivi, **jamais par une sortie brute de l'outil du loueur** :
    `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 logs <ID> 40` (lignes `AMORCE …`) et
    `… suivi_vast_v6 instance <ID>` (code 1 sur erreur) ; minuterie et garde vivantes : `ps -p` sur les PID du fichier ; état de la course :
    `git fetch origin +refs/heads/calcul/neuron-lens-volet-a-v1:refs/remotes/origin/calcul/neuron-lens-volet-a-v1` puis
    `git show refs/remotes/origin/calcul/neuron-lens-volet-a-v1:etat-neuron-lens-volet-a.txt`.
    **Règle de destruction** d'une instance sortie (« exited », stockage facturé) ou arrêtée, lue sur la **dernière ligne** du journal
    (`logs`) et sur l'**état poussé** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » (code 10, ou autre échec avant l'arbre : `rev-parse`, `git worktree`) | aucun | aussitôt |
    | message `fatal:` de git sans aucune ligne `AMORCE` (échec du clone d'entrée) | aucun | aussitôt |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt |
    | « fin : arret code N (…) », course non lancée (codes 11 à 14, ou 1, 2, 127 : `pip`, environnement…) | « arret code N … », `exclus=0` | aussitôt |
    | « fin : course terminee » ou « fin : arret code N (course en echec …) » | égal à la dernière ligne, `exclus=0` | aussitôt, après l'étape 12 |
    | toute ligne ci-dessus | `exclus` non nul | **pas sans la mère** |
    | « POUSSEE FINALE EN ECHEC : … » (code 15 ou course en échec) | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, variables exigées absentes, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

    « Pas sans la mère » : sans ssh, un fichier exclu ou des résultats non poussés sont **irrécupérables** ; garder l'instance ne fait
    que payer le stockage le temps qu'elle décide. La minuterie et la garde à 90 % restent armées et la détruiront à leur échéance : le
    dire dans le message. Si elles tombent pendant la poussée finale (≈ 10 min), les résultats non poussés sont perdus ; la durée de la
    minuterie, comptée sur le plafond, le rend improbable au devis (borne haute 7 USD sur 10, supposé : `garde_depense_v4` = v3 contre-lue lors
    des contre-lectures 3 à 5, plus la destruction confirmée).
12. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ; fichiers exclus lus
    dans l'état poussé (`exclus_fichiers`) et le journal ; pour un fichier qui a grossi, c'est la version déjà poussée qui est à la tête
    de la branche ; copie dans `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
13. Lire `docs/notes/neuron-lens-v1/minuterie-volet-a-v1.log` et `garde-volet-a-v1.log` (une destruction en échec de la minuterie,
    code 6, ou de la garde, code 4, n'avertit personne d'autre) ; `vastai destroy instance <ID> -y < /dev/null` (sans `-y`, l'outil
    abandonne en silence, code 0 : constaté) ; `… suivi_vast_v6 absente <ID> --temoin <témoin de l'étape 2>` → code 0 exigé ; si le témoin a
    disparu entre-temps, `absente <ID> --non-vide` ; si plus aucune instance n'existe sur le compte, `absente <ID>` sur la liste `[]`, et
    le dire ; minuterie et garde arrêtées **par PID** (lus dans
    `pids-volet-a-v1.txt`), chacun **après** `ps -p <PID> -o args=` montrant `minuterie_destruction_neuron_lens_v3` ou `garde_depense_v4` (sinon le PID a
    pu être réattribué : ne pas l'arrêter, le dire) ; puis, 2 s après, `ps -p` exigé « mort » pour chacun (un état `Z`, zombie, compte
    comme mort) ; le `sleep` orphelin de la minuterie reste vivant jusqu'à son terme, sans effet (essayé) ; rappel annulé ; journaux de la
    minuterie et de la garde (`minuterie-volet-a-v1.log`, `garde-volet-a-v1.log`, `journal-depense-volet-a-v1.jsonl`) et fichiers de PID
    commités avec les résultats sur `prep/neuron-lens-v1` (jusque-là, ils salissent l'arbre de travail de la session, sans effet sur la
    machine) ; crédit relevé de nouveau ; lignes proposées à la mère pour
    `registres/arrets.md` et `registres/depenses.md`.

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_v7.sh` ; journal complet versé (`docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v7.txt`,
empreinte au compagnon). Joué le 14 novembre à 14:48:22 UTC sur le commit source `2851f10e…` (commit réduit `54b36c48…`, 73 fichiers,
liste `801b0202…`, paquet `6c99249c…`) ; **verdict automatique : conforme, 0 écart** ; chaque cas avec son code attendu :
- nominal : liste réelle des essais rapides plus une sonde qui échoue si `GH_TOKEN` est dans l'environnement de pytest, 62 passés ;
  course jouet sans jeton ; fichier de 96 Mio exclu, resté sur le disque de la machine, `exclus=1`, `exclus_fichiers` renseigné ;
  « course terminee », code 0 ;
- artefacts (R5) : mauvais commit → 10 ; arbre non propre → 10 ; essai en échec → 12 ; essai sauté → 12 ; arbre sali → 12 ; carte
  absente → 11 ; première poussée impossible → 14 ; poussée finale impossible → 15 ; commit refusé par un crochet → 15 ; fichier déjà
  poussé qui grossit → version de 1 Mio gardée à la tête, `exclus_fichiers=diag/r-grossit/g.bin`, code 0 ; **tête distante falsifiée
  → 14** ; **`find` en échec → 14** ; **`find` muet et fichier de 96 Mio → second contrôle, 15, fichier absent de la branche** ;
  **copie impossible → 15** ; **index verrouillé → 15** ; **état non inscriptible → 15** ; pour chacun des sept artefacts à refus (`crochet`,
  `lsremote`, `findko`, `findmuet`, `cpko`, `index`, `etat`), aucune ligne « pousse » après le premier refus ; sonde « sans jeton » jouée seule avec le jeton présent → code 1 ;
- balayage du jeton factice sous 7 formes (pour ce jeton, brute = adresse) : témoins 7 sur 7 ; dépôt témoin empaqueté (1 paquet) :
  blob et message détectés ; **0 fichier** et **0 ligne d'objet git** sur 18 dépôts, chacun avec des objets lus.
Observé : la poussée initiale du dépôt réduit vers le dépôt nu de l'essai affiche un avertissement de négociation de git (« push
negotiation failed; proceeding anyway »), sans effet (la poussée a réussi : tous les clones l'ont lue).
Non couverts, déclarés : le chemin réel de la machine (création de l'environnement, `pip`, carte réelle, vraie course), le code 13, le
clone HTTPS réel (le clone de l'essai est local : l'en-tête n'y sert pas), la sérialisation réelle de `--args` par l'outil du loueur,
les signaux et l'abandon par `set -e`, la restauration impossible de la version déjà poussée d'un fichier qui grossit, et, dans
l'amorce v6, les branches « tete locale illisible », « liste des fichiers indexes impossible », « taille illisible », « fichier
temporaire impossible » et « copie de runs impossible » (celle de `diag` est jouée) ; les formes réelles des sorties de l'outil (seule
`instances` est essayée avant la location, étape 2) ; dans l'essai v7, l'erreur éventuelle du `grep` qui compte les formes dans les
objets git n'est pas contrôlée (seule la lecture des objets l'est). La survie de la minuterie et de la garde détachées et leur accès à
l'outil sont éprouvés à part (`essai-survie-processus-detaches-v1.txt`) ; la minuterie v3 a son essai (`essai-minuterie-v3.txt`, 0
écart ; v1, v2 et leurs essais restent archivés).

## Jeton
Le jeton du programme permet l'écriture sur tout le dépôt de travail, `main` compris ; « jamais vers `main` » n'est garanti que par
l'amorce (poussée vers `refs/heads/calcul/neuron-lens-volet-a-v1` seulement). Si un jeton restreint à une branche existe, il est
préférable (point signalé à la mère ; elle le porte à Lazar avec la demande de feu, R-2772).

## Devis (inchangé depuis la v3, borne haute)
3,5 à 5,5 h, soit 3,2 à 5 USD à 0,90 USD/h, jusqu'à 7 USD si l'audit R4 « trop beau » se déclenche ; installation de `torch` et de ses
bibliothèques CUDA par `pip` en plus (≈ 5 à 10 min). Le débit réel n'est pas mesuré avant la course : la garde le surveille (6 USD
compte rendu, 9 USD arrêt dur). Si la version de CUDA de l'hôte ne convient pas à `torch` 2.14.1, l'amorce s'arrête au code 11 (quelques
minutes de location perdues).

## Empreintes des pièces citées
Toutes scellées (compagnon `.sha256`) ; la commande elle-même est au compagnon de ce fichier. Dépôt réduit de la course inchangé :
commit source `3a470fa4`, commit réduit `799a8a32eae5039526fdc53f8c4f849f6a014204`, liste `801b0202…`, paquet
`cf64f75dea99eb24a413d61433e143aa98443a867245b773484051f6959cb287` ; branche `course/neuron-lens-volet-a-reduit-v10` = `799a8a32` au
distant.

| pièce | empreinte |
|---|---|
| `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-12-commande-v12.md` | `16539485ccdf95461e6b8ecac9cedd64045dddf4c038b72614cd2f9c228b537c` |
| `src/controle_ia/neuron_lens/suivi_vast_v6.py` | `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f` |
| `tests/test_neuron_lens_suivi_vast_v6.py` | `4df84c0e058e35beb3483b846f2bc8edc0ff3eaf13eeef0ad02511686f9c5761` |
| `scripts/minuterie_destruction_neuron_lens_v3.sh` | `e23032775e14a6d4628f449237f53b90d39b87060540df47a65c594bc0571c4f` |
| `scripts/essai_minuterie_neuron_lens_v3.sh` | `56c29bf46c656f3cb68b1bd788ed63dfe982f2978a1a2b83d9d8f7d0cbe05f8a` |
| `docs/notes/neuron-lens-v1/essai-minuterie-v3.txt` | `fe604e0a5be9bd1a919fcf10840091963cc544c54a62865a5eaeb1cf71de11db` |
| `src/controle_ia/neuron_lens/garde_depense_v4.py` | `6a98d816a0917b7e3a7029ce105a3f0047a765f494b5ec07032b05836a1a0310` |
| `tests/test_neuron_lens_garde_depense_v4.py` | `3d48393a98dfdac1ca467b3d5924713dc83e056abd3639a712491578bdcf4a31` |
| `docs/notes/neuron-lens-v1/journal-course-volet-a-v1.md` | `8a54a6a94172d4e6fc1d4d26e25fc472c3641dd366a3696df8d2ac60d9fbf92e` |
| `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-11-commande-v9.md` | `0c29e1c176f9dff5cbad3157dbea4002931fbac9cbde7cd86b1a3a9f785bca3d` |
| `docs/notes/neuron-lens-v1/essai-survie-processus-detaches-v1.txt` | `2b5903223fcdf226fe6328e3c217662c7f086fa71f760aaecca579bb36baf06e` |
| `scripts/amorce_neuron_lens_volet_a_v6.sh` | `986bc1328334bb6dd02633322408a48fe3641b2ad42aed40dbd8d15f4dbe2cdb` |
| `scripts/depot_reduit_neuron_lens_volet_a_v10.py` | `177b94db10cf8c53bc077e013ba48bc5b1049a709142ba7b5f40c02bf48f1628` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v7.sh` | `ad7be61ec60857e82745577e6fb4278d510b9789ab6b8b7204e84c2c425e49d6` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v7.txt` | `179726b7d2212208a6b65fadc003cc1c2e6c9f78f8ca754a361c42d9bd2b6b26` |
| `docs/notes/neuron-lens-v1/depot-reduit-volet-a-v10-3a470fa4/liste-fichiers.txt` | `801b0202a95b33f5a28fca646f517400d2dfde9b17395b1a5cf4b574d60f4c4c` |
| `docs/notes/neuron-lens-v1/depot-reduit-volet-a-v10-3a470fa4/rapport.json` | `d6496bfcc5bbe2b0dbb282b984be609563235c7faf28d9e3de177b059dc41cee` |
| `docs/notes/neuron-lens-v1/verification-pip-26-2-2-v2.txt` | `e35e585ba0e67433084efaef09c8d1f6829e5fed7b85af66f185e9b6cc83230b` |
| `src/controle_ia/neuron_lens/volet_a_lancer_v3.py` | `a52506f897adf9f55e3dbce8b6a832d086b0d23866b1ab6d75e122fff906b036` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `requirements-neuron-lens-volet-a-v1.txt` | `f61477e91763fa251fbd45e93fb17819883c70c45a60fb5ebd90b01feaca2312` |
| archivées, non employées : `docs/notes/neuron-lens-v1/commande-volet-a-v12.md` | `71e1f182279e656e4128a3afe20da9d2483abb3caf57dff300ba27588b05ad52` |
| `docs/notes/neuron-lens-v1/commande-volet-a-v11.md` | `e18da708bfd5c7a04be72a7daa8ec2ad98fcb228a56f1e982d25c1995c869333` |
| `src/controle_ia/neuron_lens/suivi_vast_v5.py` | `349065ed2fbcde7b22f5005621150cabc441894e0b11e70cd62509ce64022755` |
| `scripts/minuterie_destruction_neuron_lens_v2.sh` | `c2690961b6796d52b29144d1ab5ed03565bf4d6626167281cfdbea4eb4e1a0ff` |
| `scripts/essai_minuterie_neuron_lens_v2.sh` | `ed41ec5e031825976e7d5e7e7baa47ecde5aa4c92404189bd1fd1fe0afd15086` |
| `docs/notes/neuron-lens-v1/essai-minuterie-v2.txt` | `1091d5e52754654dd5789688a90fe952896174a90ed251ed36d6e0f9817d6704` |
| `scripts/minuterie_destruction_neuron_lens_v1.sh` | `25b615a07dc0b25b67e0511dc0c7cf61c840d5b21cf5255c35085ea7ac75f802` |
| `src/controle_ia/neuron_lens/garde_depense_v3.py` | `692fa80e842f18a54e7bc937b19c7cb9ff71678c02153eb0c46ec8e34b97cc3d` |
| `src/controle_ia/neuron_lens/suivi_vast_v4.py` | `73dc8c46a505db32e0003afee6bae140b19058d6ab84334e1ef9bd52a2bec550` |
