# Contre-lecture (R2) des pièces de reprise de la confirmation de Bailey — v1

Workflow `contre-lecture-reprise-confirmation-bailey`, run `wf_7c154116-383`, un contre-lecteur neuf, sur le commit `58352b5f`
(`poste-hetzner-reprise-v4.sh`, `construire-donnees-demarrage-reprise-v4.py`, générateur v1). Retour consigné tel quel.

## Traitement

- Verdict « scellable après corrections », aucun bloquant.
- Points 1 et 2 (« à corriger ») appliqués tels quels par le générateur v2 : instance exigée arrêtée ; journal des listes sans repli silencieux.
- Remarques reprises : 3 (garde de crédit avant la reprise, texte proposé), 4 (dossiers de reprise antérieurs au poste non listés, texte proposé),
  7 (commentaires), 8 (provenance de l'étiquette : `vastai show instance 61049303` rend l'étiquette `temoin-bailey-c6-40eb0b51dade4963`, état
  `exited` ; la ligne de création de `conduite-v5.jsonl` porte l'identifiant 61049303 ; seuls ces champs ont été lus), 6 (scellement).
- Remarque 5 (veilleur d'arrêt sur la machine de reprise) : consignée ; avant toute reprise suivante, la machine du poste de reprise v4 est
  détruite par son identifiant (R10) ou ses veilleurs constatés finis.
- Gardes éprouvées : boucle des listes (dossiers antérieurs non listés, dossier neuf listé, compagnon écrit) ; garde de crédit (cas sain, deux
  artefacts). Les textes appliqués sont ceux du contre-lecteur, mot pour mot : pas de nouvelle passe.

## Retour — verdict : scellable après corrections

Aucun bloquant. J'ai relancé le générateur dans un dossier temporaire : il rend à l'octet les deux pièces v4. Toutes les différences entre v3 et v4 sont nécessaires et justes :
- sortie `sortie-conduite-v15` ;
- `lanceur_v21 reprendre`, dont les arguments réels sont vérifiés : `--sortie`, `--etiquette` avec le préfixe `temoin-bailey-c6-`, `--go-id`, `--depot` ;
- identifiant 61049303 et étiquette `temoin-bailey-c6-40eb0b51dade4963` dans l'inventaire et l'appel ;
- GO-2026-11-17-07 aux deux endroits ; la ligne existe sur `origin/main`, échéance 2026-11-30, lue 2026-11-30T22:59:59Z ;
- manifeste v7, dont le compagnon donne OK ;
- garde du commit a904aa39 sur ses deux lignes ; le commit est présent et le `src/` de la tête de branche lui est identique ;
- noms v4 et listes `repertoires-sortie-conduite-v15--reprise-v10*` absents de la branche (récupérée à 58352b5f). `sortie-conduite-v15/reprise-v10` est absent aussi : la reprise écrira `reprise-v10/`.

La garde « conduite v15 finie » (`poste-fini-v13.json`, absent aujourd'hui) tient.

Points vérifiés :
- **Boucle des listes.** Jouée dans un dossier temporaire avec des répertoires vides, `reprise-v10`, `reprise-v10-2` et une liste déjà présente. Elle suit le § 3 mot pour mot (commande `find` identique à la référence, compagnons `sha256sum -c` OK). Les noms sont `repertoires-sortie-conduite-v15--reprise-v10-v1.txt` et `…--reprise-v10-2-v1.txt`. Elle ne réécrit jamais une liste existante. Les listes sont poussées avec leur compagnon avant la marque de fin.
- **Syntaxe.** `bash -n` passe sur la pièce et sur le script une fois les secrets remplacés. `py_compile` passe.
- **Constructeur v4 avec des secrets factices.** Il rend le nom `poste-temoin-bailey-reprise-v4` et l'étiquette `temoin-bailey-reprise-v4`. L'empreinte du script sans secrets est c8bd998b…, égale à celle du fichier.
- **Essais du code a904aa39 sur la reprise.** Extrait hors du dépôt : 17 passés.
- **Dépense et destruction.** Aucune voie hors GO : le redémarrage est borné par B − marge (lu dans `poste-v5.json`) et par l'échéance du GO. La destruction se fait par identifiant, seulement après un transfert complet aux empreintes égales. Le poste ne fait qu'un `vastai show instances`.

Corrections demandées avant le scellement :
- L'inventaire R10 ne vérifie pas que l'instance est arrêtée, alors que son commentaire le dit. Une instance en marche passe (essai joué).
- Le journal du poste écrit « liste écrite » sans vérifier que la liste existe. Il ne dit rien quand aucun dossier de reprise n'existe (R5).

Le reste est en remarques :
- garde de crédit avant la reprise ;
- veilleur d'arrêt qui resterait vivant sur la machine v4 ;
- listes qui pourraient porter sur des dossiers déjà venus par git ;
- commentaires périmés ;
- scellement des pièces et du générateur ;
- provenance de l'étiquette.

J'ai respecté les cloisons. Du journal de la conduite, je n'ai lu que les champs commande, code et sondage : les étapes jusqu'à `principal` sont lancées, et le sondage est en échec. Je n'ai ouvert ni `registres/etat.md`, ni aucune note, ni aucun autre fichier sous `sortie-conduite-v15`.

Rien n'a été modifié ni créé dans le dépôt, à une exception près, corrigée aussitôt : un `.pyc` posé par `py_compile` dans `runs/temoin-bailey-v1-20261111/__pycache__/`, un dossier ignoré, a été effacé. `git status` est propre et le dossier temporaire est nettoyé.

### 1. à corriger — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 96 et 103

**Constat.** Le commentaire dit « l'instance à reprendre doit exister, arrêtée », mais la garde ne vérifie que l'identifiant et l'étiquette. Essai joué : une instance 61049303 en `running` donne le code 0. La garde « une seule instance du témoin, arrêtée » n'est donc pas tenue par le poste. Ce n'est pas bloquant : la branche « running » de `Reprise` reste bornée par B − marge et par l'échéance, et ne détruit rien sans transfert. Mais si une commande est encore en cours, l'instance tournerait (et coûterait) jusqu'à la borne de budget, sans rien transférer.

**Correction proposée.** Remplacer la ligne 103 par : `ok = len(t) == 1 and str(t[0]["id"]) == "61049303" and t[0].get("label") == "temoin-bailey-c6-40eb0b51dade4963" and t[0].get("actual_status") in ("exited", "stopped")`. Puis remplacer, à la ligne 107, `etat "inventaire conforme : 61049303 seule instance du témoin"` par `etat "inventaire conforme : 61049303 seule instance du témoin, arrêtée"`. Faire la même modification dans le générateur, sur la ligne passée à `rep(...)` aux lignes 31-32.

### 2. à corriger — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 128-136

**Constat.** La ligne d'état « liste des répertoires écrite : $L » s'écrit même si la commande `cd`/`find` a échoué ou n'a rien écrit. Quand aucun dossier `reprise-v10*` n'existe (la reprise s'est arrêtée avant `mkdir`), rien n'est consigné. Le poste v13, lui, consignait le nombre d'entrées et l'absence de la sortie. C'est un repli silencieux (R5), et le § 3 demande que l'absence d'une liste soit constatée.

**Correction proposée.** Remplacer les lignes 128-135 par :
`N=0`
`for R in "$BASE"/sortie-conduite-v15/reprise-v10*; do`
`  [ -d "$R" ] || continue`
`  L="repertoires-sortie-conduite-v15--$(basename "$R")-v1.txt"`
`  [ -e "$BASE/$L" ] && { etat "liste déjà présente, laissée telle quelle : $L"; continue; }`
`  (cd "$R" && find . -mindepth 1 -type d -printf '%P\n' | LC_ALL=C sort > "$BASE/$L")`
`  (cd "$BASE" && [ -f "$L" ] && LC_ALL=C sha256sum "$L" > "$L.sha256")`
`  N=$((N+1)); etat "liste des répertoires : $L ($(wc -l < "$BASE/$L" 2>/dev/null || echo absente) entrées ; compagnon $([ -s "$BASE/$L.sha256" ] && echo écrit || echo absent))"`
`done`
`[ "$N" -gt 0 ] || etat "aucun dossier de reprise neuf : aucune liste des répertoires"`
Les deux commandes du § 3 restent mot pour mot. Reporter la modification dans le générateur, aux lignes 48-57.

### 3. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 94-107

**Constat.** Le relevé de 17:14Z donne un compte Vast à `credit` 0 et `billing_failed` vrai. La reprise v2 a déjà échoué ainsi (« redémarrage refusé, compte Vast sans crédit »). Lancé trop tôt, le poste v4 consommerait ses noms (R12) : il faudrait une v5. `_remettre_a_l_arret` laisserait en plus un veilleur d'arrêt à échéance immédiate, qui retente l'arrêt sans fin tant qu'aucun arrêt n'est accepté (voir `VeilleurArret._passage`). Ce n'est pas bloquant : ni dépense ni destruction.

**Correction proposée.** Insérer avant la ligne 96 :
`vastai show user --raw > /root/compte-avant.json || { etat "compte Vast illisible : rien ne tourne"; pousser "compte illisible"; exit 3; }`
`python3 - <<'EOF3' || { etat "crédit Vast nul ou recharge en échec : rien ne tourne"; pousser "crédit absent"; exit 3; }`
`import json, sys`
`u = json.load(open("/root/compte-avant.json"))`
`print("compte :", {k: u.get(k) for k in ("credit", "billing_failed", "has_billing", "autobill_threshold", "autobill_amount")})`
`sys.exit(0 if not u.get("billing_failed") and float(u.get("credit") or 0) > 0 else 1)`
`EOF3`
À défaut, ne lancer le poste qu'après un relevé de la session qui montre `billing_failed` faux et un crédit positif.

### 4. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 128

**Constat.** La boucle liste tous les dossiers `reprise-v10*` présents sur le disque du poste, y compris ceux venus par git d'une reprise antérieure qui serait morte avant d'écrire sa liste. Ces dossiers n'ont plus leurs répertoires vides : leur liste serait scellée sans être celle du dossier réel. Le cas ne se présente pas pour la v4 : aucun `reprise-v10*` sous `sortie-conduite-v15` sur la branche, et le PID v4 interdit un second passage. Il deviendrait réel pour une v5.

**Correction proposée.** Avant la ligne 113, ajouter `AVANT=$(cd "$BASE/sortie-conduite-v15" && ls -d reprise-v10* 2>/dev/null | tr '\n' ' ')`. Puis, dans la boucle après `[ -d "$R" ] || continue`, ajouter `case " $AVANT " in *" $(basename "$R") "*) etat "dossier antérieur au poste, non listé : $(basename "$R")"; continue;; esac`.

### 5. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh (procédure de la session)

**Constat.** `Reprise._arreter_veilleurs_precedents` n'arrête que les veilleurs de la même machine : les battements sont ignorés par git et les PID sont locaux. Si la v4 échoue en laissant un veilleur d'arrêt vivant sur sa machine Hetzner, ce veilleur arrêterait l'instance pendant une reprise v5 lancée depuis une autre machine.

**Correction proposée.** Consigner dans la passation : avant toute reprise suivante, la machine Hetzner du poste de reprise v4 est détruite par son identifiant (R10), ou ses veilleurs sont constatés finis dans son journal d'état.

### 6. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 80

**Constat.** Les compagnons `poste-hetzner-reprise-v4.sh.sha256` et `construire-donnees-demarrage-reprise-v4.py.sha256` sont absents (pièces non scellées). Sans eux, le poste s'arrête à « empreinte en échec ». Le générateur, lui non plus, n'a pas de compagnon (R6).

**Correction proposée.** Après les corrections : `python -m controle_ia.scellement sceller` sur `runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh`, `runs/temoin-bailey-v1-20261111/construire-donnees-demarrage-reprise-v4.py` et `docs/notes/reproduction-attaque-publiee-v1/generer-pieces-reprise-confirmation-bailey-v1.py`. Le compagnon du script doit porter le nom relatif `poste-hetzner-reprise-v4.sh`, comme celui de la v3. Committer et pousser avant de créer le poste. L'empreinte attendue du script sans secrets est c8bd998b… si le texte reste inchangé.

### 7. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v4.sh 9 et 44

**Constat.** Deux commentaires sont périmés. Ligne 9 : « `reprendre` écrit dans `reprise-v10-2/` » est vrai pour la sortie v11, mais ici la reprise écrira `sortie-conduite-v15/reprise-v10/`. Ligne 44 : « fichiers de la sortie v5 ».

**Correction proposée.** Ajouter à l'en-tête v4 : « `reprendre` écrit ici dans `sortie-conduite-v15/reprise-v10/` (ou `reprise-v10-<n>`), jamais d'écrasement ». Remplacer, ligne 44, « de la sortie v5 et du poste » par « de la sortie de la conduite v15, des listes des répertoires de reprise et du poste ».

### 8. remarque — docs/notes/reproduction-attaque-publiee-v1/generer-pieces-reprise-confirmation-bailey-v1.py 31-37

**Constat.** Aucune pièce lisible hors des cloisons ne cite la provenance de l'étiquette `temoin-bailey-c6-40eb0b51dade4963`. On ne la trouve que dans le générateur et dans le poste v4 (git grep, `sortie-conduite-v15` et `registres/etat.md` exclus). Je ne l'ai pas vérifiée dans le journal de la conduite, faute d'y avoir accès au-delà des champs commande, code et sondage. Une étiquette fausse échoue sans dommage : inventaire non conforme, rien ne tourne. Un identifiant différent de celui du journal donne un nœud dans `Reprise`.

**Correction proposée.** Avant le scellement, faire vérifier par la session, par programme, que l'étiquette et l'identifiant sont ceux de la ligne de création de `conduite-v5.jsonl` (ou d'un relevé `vastai show instances`). Citer cette provenance dans l'en-tête v4, par exemple « étiquette relevée dans … (empreinte …) ».
