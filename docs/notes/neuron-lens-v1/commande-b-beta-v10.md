# Commande de location et de lancement du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), variante B (la course rejouée, plus le rangement), sur une H100 SXM 80 Go — v10, sans ssh (proposée, **non exécutée**)

**v10** (2026-11-22, un développeur neuf, sous le mandat
`docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-corrections-lanceur-v4-v1.md`, `10dddebf…`) = v9
(`commande-b-beta-v9.md`, `a51b50cf…`, gardée sans modification) corrigée selon sa contre-lecture
(`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/contre-lecture-lanceur-v4-commande-v9-v1.md`, `2b223595…`), et cela seul :
- **C-1 (bloquante)** : code de course v5 — lanceur `b_beta_lancer_v5.py`, rangement `rangement_lentilles_v2.py` (attente de **60 s**
  avant le deuxième essai d'un même fichier, **300 s** avant le troisième ; borne d'attente cumulée de **1 200 s par appel** : une
  reprise qui la dépasserait reste à la clôture, nœud N-5), amorce v6, dépôt réduit v6, essais `…_b_beta_lancer_v5.py`,
  `…_etapes_b_beta_v7.py`, `…_montage_b_beta_v5.py` ; essai à blanc v5 refait, **liste du dépôt réduit neuve** (étape 5) ;
- **C-2** : ligne neuve de la table de destruction (inventaire clos sans fichier à ranger : relecture sans objet, code 4) ;
- **C-3** : libellé de la vérification sur la machine (« empreinte déclarée par l'envoyeur, relue ») ; relecture en flux maintenue ;
- **C-5** : récupération des commits des deux manifestes avant **tout** rejeu des essais du programme de comparaison v4 (étape 14) ;
- **C-6** : préfixe de la clé restreinte aussi pour la garde de priorité, si elle est armée (étape 10 bis) ;
- **C-7, C-8** : écrits aux réserves (un commit par fichier envoyé ; aucun délai propre sur un envoi qui pend).
Partout ci-dessous, « lanceur v4 », « amorce v5 », « dépôt réduit v5 », « module de rangement » et « essai à blanc v4 » se lisent dans
leurs versions neuves là où le texte les nomme comme pièces à jouer ; les mentions de l'histoire (v8, course du 18) restent telles.
N-2 n'est pas tranché ici (la mère le tranche) : comportement inchangé.

Texte de la v9, corrigé en place aux seuls endroits ci-dessus :

Rédigée le 2026-11-22 par un développeur neuf, sous le mandat
`docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md` (`6ed54244…`), pour la
session des lentilles (`session_01Qi7Gr3vedYVukbyqBbHd7z`), branche `claude/brave-galileo-jhp684`. **v9** = v8 (`commande-b-beta-v8.md`,
`3fa56f83…`, jouée le 18 novembre, archivée sans modification) changée selon le devis du réajustement v9
(`docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md`, `064e735a…`), sous le critère d'identité v8
(`critere-identite-reajustement-lentilles-v8.md`, `541bb86b…`, qui prime), et le mot de Lazar du 22 novembre (« go pour le réajustement de
nos lentilles go autonomie », `mot-lazar-go-reajustement-autonomie-2026-11-22-v1.md`, `ed47f2e3…` : variante B, prix exigé 2,62 USD/h,
plafond 62 USD, rangement L2, clé neuve à droits restreints, pas d'essai court, croquis numérique oui). **Texte autonome.**

**Changements avec la v8, et eux seuls** (tout le reste — image `python:3.12.16-bookworm`, exigences
`requirements-neuron-lens-b-beta-v2.txt`, roue de Drowse, carte `HBM3`, préambule P, intouchables, outil de suivi, minuterie et garde de
dépense v4 — est gardé) :
1. **Code de course v5** (v10) : lanceur `b_beta_lancer_v5.py` (= v4, items (a) à (m) du devis v9, § 5, point 5, plus l'attente de
   C-1), module de rangement `rangement_lentilles_v2.py`, amorce v6, dépôt réduit v6, essais du lanceur v5 ; essai à blanc v5 refait
   (fin de ce texte).
2. **Ligne de GO** : `<GO_ID>`, de la forme `GO-AAAA-MM-JJ-NN`, **lue en argument** : la ligne de calcul n'existe pas encore, la mère
   l'inscrit dans `registres/go.md` sur le mot de Lazar (type « calcul », variante B, prix exigé, plafond 62 USD, échéance, coût mensuel du
   stockage privé en chiffre). Le lanceur v4 refuse une ligne antérieure au 2026-11-22 et les deux lignes de la course du 18.
3. **Branche de résultats** `calcul/neuron-lens-reajustement-v1` ; branche du dépôt réduit `course/neuron-lens-reajustement-reduit-v1`.
4. **Plafond 62 USD** ; compte rendu **37,2 USD** (60 %) ; arrêt dur **55,8 USD** (90 %) ; frais fixes **2,3 USD** ; minuterie
   **73 511 s** (20,42 h) au prix exigé ; prix au relevé dans **[1,49 ; 2,62] USD/h** stockage de 200 Go compris (borne basse : la
   minuterie v4 ne va pas au-delà de 129 600 s, (55,8 − 2,3) / 36 = 1,49).
5. **Clé** : la clé gardée `HF_TOKEN` du conteneur de la session **ne va pas** à la machine ; la clé neuve à droits restreints, créée par
   Lazar, est lue dans le conteneur sous le nom **`HF_TOKEN_RANGEMENT`** et passée à la création sous le nom `HF_TOKEN` (le nom que lisent
   la bibliothèque de la plateforme et le balayage de la machine) ; elle reste sur la machine toute la course (copies, clôture).
6. **Rangement L2** : dépôt privé de la plateforme de modèles, créé par Lazar sous son compte, nommé **`<DEPOT_RANGEMENT>`** (« compte/nom »,
   passé en argument ; jamais écrit dans le code) ; copies au fil de l'eau sur la machine, relecture par la session (étape 14 bis).
7. **Fin de course** (devis v9, § 5, point 3) : inventaire au fil de l'eau ; clôture sur la machine ; relecture au lieu de rangement par la
   session avant la destruction ; **ligne neuve de la table de destruction** : copie ou relecture en échec → pas sans la mère.
8. **Garde de priorité d'une autre étape** (étape 10 bis de la v8, pour l'étape B bis du 18) : **non armée par défaut** ; armée
   seulement si la mère nomme, ce jour-là, une instance prioritaire d'une autre session et son seuil (nœud N-1).

## Rien ne part sans (préalables du devis v9, § 5, tous sans dépense)
- la **ligne de GO de calcul** `<GO_ID>` inscrite par la mère (point 1) et le **nœud de l'entrée des lentilles** (point 2) ;
- le **dépôt de rangement** créé et privé, la **clé restreinte** créée par Lazar et sa portée vérifiée (lecture du modèle à accès contrôlé,
  écriture sur le seul dépôt de rangement), sinon la décision 3 est à reposer (points 3 et 4) ;
- les **relevés de la plateforme** (point 9 : coût et quota du stockage privé, débit en écriture, licence des poids dérivés rangés en privé,
  **nature de l'empreinte rendue pour un gros fichier** ; durée et trafic d'une relecture en flux mesurés sur un fichier d'essai) ;
- le **programme de comparaison v4** et le **critère v8** scellés (point 6, fait) ; le **statut de la seconde mesure** et le **plan de sa
  lecture** scellés et contre-lus (point 7) ;
- ce texte, le lanceur v5, le module de rangement v2, l'amorce v6 et leurs essais **contre-lus par un agent neuf d'un autre modèle**
  (v10 : la contre-lecture du lanceur v4 est faite ; celle des corrections reste à faire) ; le **nœud N-2 tranché par la mère** ;
- le **feu écrit de la mère** ; la **recharge** d'au moins 62 USD plus les autres lignes ouvertes ce jour-là sur le même compte (point 8,
  décision 5) ; le relevé de prix dans l'heure.

## Demande de feu (résumé)
| objet | valeur |
|---|---|
| ligne | `<GO_ID>` (type « calcul », à inscrire) ; variante **B** ; rangement **L2** |
| plafond | **62 USD** ; compte rendu **37,2 USD** ; arrêt dur **55,8 USD** ; trafic réservé **2,3 USD** (frais fixes) |
| coût attendu | ≈ **31,6 USD** à 2,37 USD/h (13,3 h) ; pire cas ≈ **50,1 USD** au prix exigé (19,1 h), **52,4 USD** avec les frais fixes |
| durée | attendue **13,3 h** ; pire cas **19,1 h** ; arrêt dur de la garde à **20,42 h** au prix déclaré de 2,62 (marge 1,3 h) |
| carte et prix | **H100 SXM 80 Go** (« NVIDIA H100 80GB HBM3 »), machine vérifiée ; **≤ 2,62 et ≥ 1,49 USD/h** stockage de 200 Go compris ; trafic ≤ 0,04 USD/Go chacun ; débit montant ≥ 200 Mbit/s |
| crédit | recharge d'au moins 62 USD plus les autres lignes du jour (décision 5) ; `can_pay`, `has_billing` vrais, `billing_failed` faux ; crédit relu à chaque contrôle, **< 1 USD → arrêt** |
| stockage privé | coût mensuel relevé (point 9), en chiffre dans la ligne de GO ; hors des plafonds ci-dessus |
| perte acceptée d'avance | la garde de dépense, la minuterie et la garde de crédit détruisent la machine même si une lentille n'est pas copiée ; la perte est écrite à l'inventaire, au verdict d'identité (« R non réajustée » ou « S non réajustée ») et au billet. **Lazar lit cette ligne avant d'accorder.** |

## Pièces qui font foi (branche `claude/brave-galileo-jhp684`)
Les empreintes complètes sont dans les compagnons `.sha256` et dans
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/empreintes-lanceur-v4-v2.txt` (scellé ; v10).
| pièce | chemin |
|---|---|
| devis du réajustement v9 ; critère d'identité v8 ; mot de Lazar | `docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md` ; `…/critere-identite-reajustement-lentilles-v8.md` ; `docs/notes/neuron-lens-v1/mot-lazar-go-reajustement-autonomie-2026-11-22-v1.md` |
| texte gelé de la tranche, addendum partie 1 v3, devis v12 (revérifiés par `preparer`, inchangés) | voir la commande v8 (mêmes chemins, mêmes empreintes) |
| lanceur v5 ; module de rangement v2 | `src/controle_ia/neuron_lens/b_beta_lancer_v5.py` ; `src/controle_ia/neuron_lens/rangement_lentilles_v2.py` |
| lanceur v3 (constantes lues par la partie 2 v3), partie 2 v3, contrôles v2 | inchangés (commande v8) |
| amorce v6 ; dépôt réduit v6 | `scripts/amorce_neuron_lens_b_beta_v6.sh` ; `scripts/depot_reduit_neuron_lens_b_beta_v6.py` |
| essais embarqués | `tests/test_neuron_lens_{verdicts_b_beta_v4,controles_b_beta_v2,b_beta_lancer_v5,etapes_b_beta_v7,montage_b_beta_v5,grandeurs_b_alpha_v1,verdicts_b_alpha_v3,balayage_arbre_v1}.py` |
| programme de comparaison v4 et ses essais (lancés par la mère après la course) | `src/controle_ia/neuron_lens/comparer_reajustement_v4.py` (`4a0f3b2c…`) ; `tests/test_neuron_lens_comparer_reajustement_v4.py` (`e1708b39…`) |
| garde de dépense v4, minuterie v4, suivi v6, balayage v1 | inchangés (commande v8) |
| essai à blanc v5 et son journal | `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v5.sh` ; `docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/essai-a-blanc-amorce-b-beta-v5.txt` |
| corrections de la contre-lecture (v10) | `docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/corrections-contre-lecture-lanceur-v4-v1.md` |

## Préambule P, intouchables, règles
**P** (le shell ne garde rien d'un appel à l'autre) : `cd /home/user/controle-ia-travail && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&`
**Intouchables** : ceux de la commande v8, et **toute instance d'une autre session**. **Jamais** de `vastai show … --raw` imprimé hors
l'étape 3 (champs du compte seulement) : tout passe par `suivi_vast_v6`. Secrets lus par leur nom seulement. **Préavis d'une ligne à la
mère** avant tout geste à risque de refus (création avec les secrets, destruction manuelle). Tout refus d'une permission, du crochet ou du
classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère. **Registre des GO** de la branche principale fusionné dans
la branche de travail avant la création (le crochet de calcul le lit).
**Sortie du suivi balayée avec la clé restreinte** : l'outil de suivi v6 balaie les secrets par leurs noms (`HF_TOKEN` parmi eux), et la
clé restreinte s'appelle `HF_TOKEN_RANGEMENT` dans le conteneur ; chaque appel à `suivi_vast_v6` de cette commande est donc préfixé par
`HF_TOKEN="$HF_TOKEN_RANGEMENT"` (la clé gardée ne va jamais au loueur ni à la machine : elle ne peut pas paraître dans leurs sorties).

## 0. Avant la location (conteneur de la session)
1. Outil du loueur (commande v8, étape 1, inchangée).
2. **Secrets présents, par leur longueur, et distincts** :
   `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ] && [ ${#HF_TOKEN_RANGEMENT} -ge 8 ] && [ "$HF_TOKEN_RANGEMENT" != "${HF_TOKEN:-}" ] && echo secrets-ok`
   (aucune valeur imprimée) ; sinon arrêt, message (la clé gardée ne part jamais à la place de la clé restreinte). **Dépôt de
   rangement** : `<DEPOT_RANGEMENT>` donné par Lazar, de la forme `compte/nom`. **Suivi prêt** : `HF_TOKEN="$HF_TOKEN_RANGEMENT"
   PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 verifier` → code 0 ; `… instances` → code 0, liste consignée.
3. **Crédit** (commande v8, étape 3, même commande) : `can_pay`, `has_billing` vrais, `billing_failed` faux ; **crédit ≥ 62 USD plus les
   autres lignes ouvertes ce jour-là** (décision 5 ; montant des autres lignes chiffré par la mère) ; sinon rien ne part. Consigné.
4. **Relevé de prix dans l'heure qui précède la création** (commande v8, étape 4, même script `releve_prix_h100_v3.py`, nom de sortie
   neuf `releve-prix-vast-h100-<AAAAMMJJTHHMMSSZ>-v5.tsv`, scellé, versé). **Offre retenue**, lue dans les colonnes du relevé
   (`prix_avec_200_go`, `inet_up_cost_usd_go`, `inet_down_cost_usd_go`, `inet_up_mbit`, `verification`), jamais dans ses colonnes
   d'options : la moins chère dont le prix avec 200 Go est **≤ 2,62 et ≥ 1,49 USD/h**, trafic ≤ 0,04 USD/Go chacun, débit montant
   ≥ 200 Mbit/s, machine vérifiée ; aucune → rien ne part, message.
5. **Dépôt réduit v6** : `.venv/bin/python scripts/depot_reduit_neuron_lens_b_beta_v6.py <COMMIT_SOURCE> <dossier neuf>` →
   `rapport.json`, `liste-fichiers.sha256`, paquet. **Liste attendue : `c20d3bac2af2b7158e547d6b064a95734e1779dabca3f7c6f1ef7c54ab69d5c6`**
   (87 fichiers, celle de l'essai à blanc v5 ; une autre liste exige un nouvel essai à blanc ; la liste `302b50fd…` de la v9 ne vaut plus). `<COMMIT_SOURCE>` = commit de la branche qui porte cette
   commande. Branche `course/neuron-lens-reajustement-reduit-v1` poussée (`git fetch <paquet> course:refs/heads/course/neuron-lens-reajustement-reduit-v1
   && git push origin course/neuron-lens-reajustement-reduit-v1`) ; `git ls-remote origin refs/heads/course/neuron-lens-reajustement-reduit-v1`
   = commit réduit ; `git ls-remote origin refs/heads/calcul/neuron-lens-reajustement-v1` **vide** (sinon arrêt). Le commit réduit est
   celui que portera le manifeste de la course : poussé ainsi, il est lisible dans le dépôt de travail (critère v8, préalables « K2 »).
6. **RUN_ID** fixé une fois pour toutes : `<AAAAMMJJ-HHMMSS>-neuron-lens-b-beta` (heure UTC de cette étape ; même suffixe que le 18 :
   les noms des pièces que le programme de comparaison lit sont inchangés), le même à chaque relance.

## 1. Location (une seule instance), minuterie, garde, rappels
7. **Préavis d'une ligne à la mère** (offre, prix au relevé), puis P et :
   ```
   date -u +%FT%TZ   # <ISO_CREATION>, relevée dans la même commande
   GO_ID=<GO_ID> vastai create instance <OFFRE> --raw --image python:3.12.16-bookworm --disk 200 --label neuron-lens-reajustement \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e HF_TOKEN=$HF_TOKEN_RANGEMENT -e DEPOT_RANGEMENT=<DEPOT_RANGEMENT> -e VARIANTE=B -e COMMIT_REDUIT=<COMMIT_REDUIT> -e COMMIT_SOURCE=<COMMIT_SOURCE> -e GO_ID=<GO_ID> -e RUN_ID=<RUN_ID> -e HF_HOME=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-reajustement-v1 -e PERIODE_POUSSE_S=600 -e CARTE_ATTENDUE=HBM3" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; [ -d depot/.git ] || git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-reajustement-reduit-v1 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_b_beta_v6.sh' \
     2>&1 | HF_TOKEN="$HF_TOKEN_RANGEMENT" PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 creation
   ```
   `<COMMIT_REDUIT>` et `<COMMIT_SOURCE>` **lus par programme** dans `rapport.json` ; `<GO_ID>` lu dans la ligne inscrite par la mère ;
   `<DEPOT_RANGEMENT>` donné par Lazar ; aucun n'est retapé à la main. Les secrets ne sont développés que par le shell du lancement (et
   figurent, le temps de la création, dans les arguments du processus de l'outil dans le conteneur, et dans la configuration de
   l'instance chez le loueur : déclaré). → `echo "$(date -u +%FT%TZ) instance <ID> creation <ISO_CREATION> prix <PRIX>" >> docs/notes/neuron-lens-v1/pids-reajustement-v1.txt`.
   Échec (pas de `new_contract`, ou `success` faux) → `instances`, destruction éventuelle (étape 15), message. **Toute branche d'échec
   des étapes 7 à 10 : destruction immédiate** (étape 15).
8. **Instance relue** : `HF_TOKEN="$HF_TOKEN_RANGEMENT" … suivi_vast_v6 instance <ID>` → `dph_total` **≤ 2,62 et ≥ 1,49** ; `gpu_name`
   H100 SXM ; `dph_total` à 5 % près du prix avec 200 Go de l'offre au relevé ; sinon destruction et message. Ce prix lu est <PRIX>.
   Lecture en échec deux fois : destruction.
9. **Minuterie v4** par identifiant, aussitôt (R10), comptée depuis la création (P, puis) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --minuterie-seulement --prix-h <PRIX> --plafond 62 --frais-fixes 2.3 --debut <ISO_CREATION>)
   [ -n "$D" ] || { echo "duree vide : arret"; exit 1; }
   F=docs/notes/neuron-lens-v1/pid-minuterie-reajustement-v1.txt; rm -f "$F"
   setsid nohup bash scripts/minuterie_destruction_neuron_lens_v4.sh <ID> "$D" /home/user/vastai-env/bin/vastai "$F" \
     >> docs/notes/neuron-lens-v1/minuterie-reajustement-v1.log 2>&1 < /dev/null &
   sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep minuterie_destruction_neuron_lens_v4 && echo "$(date -u +%FT%TZ) minuterie PID $P duree $D s instance <ID>" >> docs/notes/neuron-lens-v1/pids-reajustement-v1.txt
   ```
   Durée totale = (55,8 − 2,3) / prix lu × 3 600, tronquée : **73 511 s** (20,42 h) à 2,62 ; 81 265 s (22,57 h) à 2,37 ; 129 261 s à
   1,49 (borne de la v4 : 129 600 s) — moins le temps écoulé depuis la création. PID lu dans le fichier, **jamais** `$!`. Non armée →
   destruction, message.
10. **Garde de dépense v4**, détachée, son PID écrit par elle-même avant `exec` (P, puis) :
    ```
    F=docs/notes/neuron-lens-v1/pid-garde-reajustement-v1.txt; rm -f "$F"
    setsid nohup bash -c 'echo $$ > "$0"; exec env PATH=/home/user/vastai-env/bin:$PATH PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v4 --instance <ID> --prix-h 2.62 --plafond 62 --debut <ISO_CREATION> --frais-fixes 2.3 --journal docs/notes/neuron-lens-v1/journal-depense-reajustement-v1.jsonl' "$F" \
      >> docs/notes/neuron-lens-v1/garde-reajustement-v1.log 2>&1 < /dev/null &
    sleep 2; P=$(cat "$F") && ps -p "$P" -o pid=,args= | grep garde_depense_v4 && echo "$(date -u +%FT%TZ) garde PID $P instance <ID>" >> docs/notes/neuron-lens-v1/pids-reajustement-v1.txt
    ```
    **Prix déclaré à la garde : le prix exigé, 2,62 USD/h** (devis v9, § 3) : la garde compte au plus grand du prix déclaré et du prix
    lu ; au prix déclaré, l'arrêt dur tombe à 20,42 h, **après** le pire cas de 19,1 h (marge 1,3 h). Compte rendu à **37,2 USD**
    (attendu en course normale, vers 13,3 h : il ne signale rien à lui seul), destruction réessayée et vérifiée à **55,8 USD**.
10 bis. **Garde de priorité d'une autre étape** : **non armée**, sauf si la mère nomme ce jour-là une instance prioritaire d'une autre
    session et un seuil ; alors la commande v8, étape 10 bis, est jouée telle quelle avec cet identifiant et ce seuil, ses fichiers
    renommés `…-reajustement-v1` (nœud N-1). **v10 (C-6)** : chacun de ses appels à l'outil de suivi v6 est préfixé, comme au
    préambule, par `HF_TOKEN="$HF_TOKEN_RANGEMENT"` (son balayage par noms cherche ainsi la clé restreinte).
11. **Rappels** (`send_later`) : (a) à **13,3 h** de location, compte rendu en durée (attendu) ; (b) à **80 % de D** (16,3 h, 58 809 s,
    au prix exigé exact), rappel « vérifier » : minuterie et garde vivantes, avancement, la mère décide (pas de destruction : le pire
    cas de 19,1 h est au-delà) ; (c) à **19,1 h**, rappel du pire cas : sans fin de course, la mère décide. Puis commit et poussée de
    `pids-reajustement-v1.txt`. **Veille** : celle de la commande v8, étape 11, avec les fichiers `pid-{minuterie,garde}-reajustement-v1.txt`
    et le journal `veille-reajustement-v1.log` (la garde de priorité seulement si elle est armée). Une ligne « MORTE » → réarmement
    aussitôt par les étapes 9 et 10 **sur la même échéance absolue** (D recomptée depuis `<ISO_CREATION>`), message à la mère (leçon du
    19 novembre, devis v9, § 5, point 10).

## 2. Sur la machine (amorce `scripts/amorce_neuron_lens_b_beta_v6.sh`, sans intervention)
12. Gardes d'entrée de la v8 (commit réduit, arbre propre, RUN_ID et GO_ID, première poussée, carte avant pip, python 3.12.16), plus
    `VARIANTE` A ou B et `DEPOT_RANGEMENT` de la forme `compte/nom` (code 17) ; `pip` 26.2.2 puis les versions épinglées
    (`requirements-neuron-lens-b-beta-v2.txt`, **aucun paquet changé ni ajouté** : `versions` du manifeste aux clés et aux valeurs du
    18, hors `plateforme`), roue de Drowse vérifiée (code 18), installation **bornée à 7 200 s** (code 16) ; carte vue par `torch` ;
    essais embarqués (code 12) ; puis les étapes du lanceur `b_beta_lancer_v5`, une par appel, dans l'ordre de `ETAPES` :
    `preparer` (manifeste : GO lu, variante, `depot_propre` vrai) → **`materiel`** (pièce à part : modèle de carte, pilote, versions de la
    machine ; contrôle K3) → `telecharger-tokeniseur` (**clé**) → `b0` → `telecharger-poids` (**clé**) → `corpus-ajustement` →
    `partie2-b0` → `banc` → `ajustement-R` → `export` → **`copie-R`** (**clé**, en ligne : fichier d'ajustement de R et les trois exports,
    empreintes recalculées et égales à celles des résultats, dépôt exigé privé, taille rendue et empreinte déclarée par l'envoyeur
    relues à l'arrivée (v10, C-3 : la plateforme ne la recalcule pas, ce n'est pas une preuve ; la relecture en flux de l'étape 14 bis
    l'est), révision notée, deux reprises au plus par fichier, **la première après 60 s, la seconde après 300 s** (v10, C-1), attente
    cumulée bornée à 1 200 s par appel (au-delà, la reprise est remise à la clôture, sans être comptée) ; un échec est consigné et
    n'arrête pas la course) → `ajustement-S` → **`copie-S`** (**clé**) →
    **`croquis`** (sur le processeur, borné à 15 minutes ; un échec est noté et n'arrête rien) → `corpus-activations` → … → `verdicts`
    (la suite de la v8, inchangée). **Après chaque étape faite** : inventaire neuf (`diag/<RUN_ID>/inventaire/inventaire-NNN.json`,
    scellé : noms, tailles, empreintes, et pour chaque gros fichier copié ou non et révision du dépôt), **poussé aussitôt**, avant
    l'étape suivante. **La clé reste dans l'environnement de l'amorce toute la course** : le balayage des secrets avant chaque poussée
    (et toutes les dix minutes) la cherche à toutes les étapes ; les étapes « sans clé » et les processus enfants ne la reçoivent pas.
    **Fin de course lancée** : (0) inventaire poussé ; (1) **clôture** (`cloture`, clé, en ligne : copie de ce qui ne l'est pas encore,
    fichiers des étapes faites seulement, dans la limite des deux reprises, avec les mêmes attentes de 60 s et 300 s et la même borne de
    1 200 s par appel ; puis inventaire **clos**) ; puis la poussée finale. Une
    copie restée en échec : dernière ligne « COPIE EN ECHEC : … », code 23. Fichiers de plus de 95 Mo exclus de la branche (ils sont
    au lieu de rangement, ou perdus avec la machine).

## 3. Suivi, retour, relecture et destruction (conteneur de la session)
13. Suivi : celui de la commande v8, étape 13 (journal, instance, état poussé, PID ; course figée ; crédit relu, **< 1 USD → arrêt** ;
    dépassement du pire cas d'une étape → compte rendu), chaque appel au suivi préfixé comme dit au préambule. **La session ne lit aucun
    résultat de mesure** : seulement l'état poussé, les arrêts, les relevés de la partie 2, l'**existence** du fichier de verdicts, et
    **l'inventaire** (noms, tailles, empreintes, état des copies : aucune mesure).
    **Règle de destruction**, sur la **dernière ligne** du journal, l'**état poussé** et l'**inventaire clos** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » ou `fatal:` de git sans ligne `AMORCE` | aucun | aussitôt (étape 15) |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt |
    | « fin : arret code N (…) », course non lancée (N = 10, 11, 12, 13, 14, 16, 17, 18, 19) | « arret code N … », `exclus=0` | aussitôt |
    | « fin : course terminee » ou « fin : arret code 2x (course en echec …) », sans « copie en echec » | égal, inventaire clos poussé, `exclus` = fichiers lourds attendus seulement | **après l'étape 14 et la première relecture tenue (14 bis)** |
    | « etat final deja atteint : … ; attente sans calcul » | final | après l'étape 14 et la relecture tenue (14 bis) |
    | toute ligne ci-dessus | `exclus` portant un fichier **de résultats** (`diag/…/b-beta-*`, partie 2, grandeurs, résumés, verdicts, intervalles, inventaire) | **pas sans la mère** |
    | « COPIE EN ECHEC : … » (code 23) | final, inventaire clos avec `non_copies` | **pas sans la mère**, message immédiat ; la machine attend, au prix de l'heure, dans la limite de l'arrêt dur |
    | **inventaire clos sans fichier à ranger** (`prevus` vide, `non_copies` vide : course arrêtée avant la fin de l'ajustement de R) : **relecture sans objet** (étape 14 bis : code 4, sortie « sans_objet » versée ; v10, C-2) | celui des lignes ci-dessus | selon la dernière ligne du journal (lignes ci-dessus), **sans attendre de relecture** ; « R non réajustée » et « S non réajustée » à l'inventaire et au billet |
    | **relecture au lieu de rangement en échec** (étape 14 bis : code 1 ou 2), quelle que soit la ligne | quelconque | **pas sans la mère**, message immédiat ; la machine attend, dans la limite de l'arrêt dur (devis v9, § 5, point 3, temps (2)) |
    | « POUSSEE FINALE EN ECHEC : … » | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

14. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque `diag/<RUN_ID>/b-beta-*.json` ; compagnons des pièces
    de la v8 vérifiés ; **pièce du matériel** (`b-beta-materiel.json`), **résultats de copie** (`b-beta-copie-R.json`, `b-beta-copie-S.json`,
    `cloture-*.json`), **croquis** (`b-beta-croquis.json`) et **inventaire clos** (le dernier `inventaire-NNN.json`, `"clos": true`)
    vérifiés par leur sceau ; copie sur la branche de la tranche ; commit ; poussée. **La lecture reste à un lecteur neuf, sur le plan
    scellé de la seconde course** ; la comparaison d'identité est lancée par la mère ou un agent neuf (critère v8, § 8), jamais par la
    session des lentilles, avec le commit de la branche de résultats lu **après** la destruction (contrôle K1). Le dépôt donné au
    programme doit contenir les commits des deux manifestes : `git fetch origin course/neuron-lens-b-beta-reduit-v3
    course/neuron-lens-reajustement-reduit-v1 calcul/neuron-lens-reajustement-v1` d'abord (relevé le 2026-11-22 : dans un arbre de travail
    qui ne les a pas, les essais du programme v4 manquent le commit `5e5cb65b…` du 18 et échouent ; le distant le porte).
    **v10 (C-5)** : la même récupération précède **tout rejeu** des essais du programme de comparaison v4
    (`tests/test_neuron_lens_comparer_reajustement_v4.py`, 311 essais), **y compris avant la création** (vérification des pièces), et pas
    seulement la comparaison : avant la création, `git fetch origin course/neuron-lens-b-beta-reduit-v3` suffit
    (`git cat-file -e 5e5cb65b4daf8726ebe1c4032a836b850de7ea2f` au code 0 exigé avant de lancer ces essais ; sinon leurs échecs ne disent
    rien du programme).
14 bis. **Première relecture au lieu de rangement** (devis v9, § 5, point 3, temps (2) ; critère v8, § 4, point 5), clé de la machine
    encore valide, **avant la destruction** :
    ```
    PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.rangement_lentilles_v2 relire --inventaire <inventaire clos> \
      --cle-nom HF_TOKEN_RANGEMENT --sortie docs/notes/neuron-lens-v1/devis-reajustement/relecture-rangement-1-<AAAAMMJJTHHMMSSZ>-v1.json
    ```
    Mode **en flux** par défaut (téléchargement passé directement au calcul d'empreinte, rien d'écrit sur le disque) ; `--mode plateforme`
    seulement si les relevés du point 9 établissent que la plateforme recalcule les empreintes à la réception. Code **0** exigé (toutes
    les empreintes et tailles égales à celles de l'inventaire clos, à la révision notée), ou **4** quand l'inventaire clos ne prévoit
    aucun fichier à ranger (relecture sans objet, v10, C-2 : ligne de la table) ; sinon **pas de destruction sans la mère**
    (table ci-dessus). Sortie scellée et versée, révision du dépôt notée. Sans ssh, la machine ne peut pas recevoir l'ordre de refaire
    une copie : les reprises sont faites sur la machine, au plus deux par fichier, quand la vérification à l'arrivée échoue (nœud N-2).
15. **Préavis d'une ligne à la mère, puis destruction** (sauf si la minuterie ou la garde l'ont faite), **sans attendre Lazar**, seulement
    après l'inventaire clos poussé et la première relecture tenue : journaux de la minuterie et de la garde lus ;
    `vastai destroy instance <ID> -y < /dev/null` ; `HF_TOKEN="$HF_TOKEN_RANGEMENT" … suivi_vast_v6 absente <ID> --non-vide` au code 0
    exigé ; minuterie et garde arrêtées **par PID** après `ps -p <PID> -o args=`, mortes 2 s après ; rappels annulés ; journaux et
    fichiers de PID commités ; crédit relevé ; lignes proposées à la mère pour `registres/arrets.md` et `registres/depenses.md` ;
    **révocation de la clé restreinte demandée à Lazar** (geste de Lazar).
16. **Seconde relecture**, après la révocation, avec la clé gardée de la session (lecture seule), à la même révision :
    ```
    PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.rangement_lentilles_v2 relire --inventaire <inventaire clos> \
      --cle-nom HF_TOKEN --revision <révision de la première relecture> --sortie docs/notes/neuron-lens-v1/devis-reajustement/relecture-rangement-2-<AAAAMMJJTHHMMSSZ>-v1.json
    ```
    Code 0 attendu ; sinon nœud de Lazar (la mention d'identité décrirait un fichier qui n'existe plus : critère v8, § 4, point 5).

## Essai à blanc (sans location), refait
**v10** : `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v5.sh` (`41459df6…`), joué le 2026-11-22 sur le commit source `2355c9bd7`
(dépôt réduit v6 : 87 fichiers, **liste `c20d3bac…`**, commit réduit `1558dbbf`, paquet `354875ca…`), journal
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/essai-a-blanc-amorce-b-beta-v5.txt` (empreinte au compagnon) :
**conforme, 0 écart** ; essais réels du cas nominal « 256 passed, 3 deselected » (les trois essais `copie_reelle`, écartés sur la
machine) ; mêmes cas que la v4 ci-dessous, faux lanceur égal au lanceur v5 (étapes, « jeton », en ligne). Les deux premières lignes du
journal (« fatal: expected 'acknowledgments' … », « warning: push negotiation failed … ») sont des messages de git à la première
poussée vers le dépôt nu local, déjà présents dans le journal v4 ; la poussée réussit (sinon l'essai s'arrêterait au code 3).
Le transport réel du rangement et donc les vraies attentes ne sont pas joués (le faux lanceur n'appelle pas le rangement) : les
attentes sont essayées par les essais embarqués (E5) et le banc v5.
Texte de la v9 pour mémoire : `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v4.sh` (`ab284ebe…`), joué le 2026-11-22 vers 05:28Z sur le commit source `c9fcd30c4`
(dépôt réduit v5 : 87 fichiers, **liste `302b50fd…`**, commit réduit `34dfa3a8`, paquet `d5cd0342…`), journal
`docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/essai-a-blanc-amorce-b-beta-v4.txt` (empreinte au compagnon) :
**conforme, 0 écart** ; essais réels du cas nominal « 247 passed, 2 deselected » (les deux essais `copie_reelle`, écartés sur la
machine). Le libellé « v3 » de la ligne de tête du journal est le texte resté de l'essai v3. La v3 de l'essai, jouée sur `443bd8d3f`
avec l'amorce v4, était **non conforme** (12 écarts au seul cas nominal : un essai embarqué importait le programme de comparaison,
absent de l'arbre réduit) : `essai-a-blanc-amorce-b-beta-v3.txt`, versé. Cas joués : nominal (27 étapes, clé présente aux quatre étapes « jeton » et à la clôture, absente
ailleurs, un inventaire poussé par étape, dans son propre commit, inventaire final clos), relance après la fin, reprise après un arrêt
brutal pendant la passe, échec d'une étape (20), clôture en échec (23, dernière ligne « COPIE EN ECHEC »), **quatorze formes des deux
secrets écrites à l'étape du croquis, après les copies, toutes refusées par le balayage**, gardes d'entrée (10, 12, 13, 14, 16, 17 dont
VARIANTE et DEPOT_RANGEMENT, 19), carte (H100 HBM3 passe ; H100 PCIe, A100, H200 : 11). Non couverts, déclarés : le code 18 ; la vraie
course, le vrai pip, la vraie carte, le clone réel, le vrai transport du rangement et la vraie plateforme de modèles.

## Réserves
- **Transport réel du rangement non essayé** (aucune requête permise à l'écriture) : `upload_file`, `get_paths_info`, `repo_info` et la
  lecture en flux de `huggingface_hub` 1.33.0 sont appelés par leurs signatures lues dans la bibliothèque installée, jamais joués.
  Avec la bibliothèque `hf_xet` présente, l'envoi passe par elle : qu'elle n'écrive aucune copie du fichier sur le disque n'est **pas
  établi** (à relever avec le point 9) ; l'empreinte que rend la plateforme pour un gros fichier (`lfs.sha256`) peut n'être que celle que
  l'envoyeur déclare : d'où la relecture en flux par défaut.
- Durée et trafic de la relecture en flux (≈ 31 Go) **non mesurés** ; le disque du conteneur n'est pas touché ; l'hôte de la plateforme
  doit être permis au réseau du conteneur de la session (à vérifier avant le GO).
- La clé restreinte figure dans la configuration de l'instance chez le loueur et dans le processus d'entrée de l'amorce, toute la course
  (elle n'est plus retirée après le téléchargement) : exposition déclarée au devis (§ 5, point 4) ; parade : dépôt exigé privé, chaque
  copie vérifiée à l'arrivée, révision notée, révocation par Lazar après la copie.
- L'inventaire recalcule l'empreinte de tout fichier changé de `voisin/data` à chaque étape (les gros fichiers, une fois chacun) : quelques
  minutes au plus sur la course, non mesurées.
- Le croquis relit les deux fichiers d'ajustement (≈ 17 Go) et les vérifie par empreinte ; durée réelle non mesurée, bornée à 15 minutes.
- Le relevé de prix garde le script v3 et ses colonnes d'options du 18 (non lues) ; la borne basse de 1,49 USD/h est calculée ici.
- **v10, C-3** : la « vérification à l'arrivée » sur la machine relit la taille rendue et l'empreinte que l'envoyeur a lui-même déclarée
  (recalcul par la plateforme non établi) ; elle attrape une coupure ou un fichier tronqué, pas une altération à la réception. La seule
  vérification propre est la relecture en flux de l'étape 14 bis, gardée par défaut.
- **v10, C-1, coût des attentes** : au pire 360 s d'attente par fichier, bornées à 1 200 s par appel ; S n'a qu'un fichier (≤ 360 s par
  appel) ; au pire sur la course ≈ 20 + 6 (copies) + 20 + 6 (clôture) = **52 minutes**, dans la marge de 1,3 h du pire cas. Une
  coupure plus longue que les attentes perd la copie sur la machine (N-2 inchangé).
- **v10, C-7 (risque, non corrigé)** : un commit par fichier envoyé (`upload_file`) ; le nombre de fichiers des trois exports n'est pas
  écrit dans les pièces lues ; les limites de débit par commit ne sont pas publiées (relevés de la plateforme, § 4 : quotas par fenêtre
  de 5 minutes). Les attentes de 60 et 300 s l'amortissent (la seconde dépasse une fenêtre). Regrouper les exports en un commit
  (`create_commit` à plusieurs ajouts) changerait le transport, qu'on ne peut pas essayer ici : non fait, à relever avec le point 9
  (nombre de fichiers des exports, limite de commits).
- **v10, C-8 (risque, non corrigé)** : aucun délai propre sur un envoi ou une relecture qui pend (la lecture en flux a un délai de
  600 s par lecture, l'envoi n'en a pas) ; seuls la garde de dépense et la minuterie bornent la course. Un délai par envoi exigerait un
  processus enfant ou un fil par appel, non essayable sur le vrai transport ici : non fait.
- Réserves de la commande v8 gardées : aucun essai du code voisin ni de Drowse dans le conteneur ; mémoire vive `cpu_ram>=64` ; disque
  200 Go (les copies ne dupliquent rien) ; `pytest` et PyYAML sans version exigée.

## Nœuds (écrits le 2026-11-22, le reste continué)
- **N-1** — garde de priorité d'une autre étape : la v8 l'armait pour l'étape B bis du 18 ; aucune pièce de mon mandat ne dit qu'une
  autre étape prioritaire tourne le jour de la course. Choix : non armée par défaut, armée sur le seul mot de la mère (identifiant et seuil).
- **N-2** — refaire une copie après une relecture de la session en échec : sans ssh, aucun canal n'existe ; choix : reprises sur la machine
  seulement (vérification à l'arrivée), puis « pas sans la mère ». Une voie (la machine attend un signal sur la branche de résultats) est
  possible mais n'est pas écrite.
  **v10** : non tranché ici ; à trancher par la mère avant la création (contre-lecture, § 6) ; comportement inchangé.
- **N-5** (v10, écrit le 2026-11-22) — borne d'attente cumulée de **1 200 s par appel** de copie : la contre-lecture demandait l'attente
  (60 s puis 300 s) sans borne ; sans borne, une coupure longue pendant `copie-R` retiendrait la course 6 minutes par fichier des
  exports (nombre non écrit), au risque de passer la marge de 1,3 h. Choix : borne de 1 200 s par appel, reprise au-delà remise à la
  clôture (essai non compté, donc encore permis) ; la mère peut la changer (constante `ATTENTE_MAX_APPEL_S` du rangement v2, nouvelle
  version) avant la création.
