# Contre-lecture R2 indépendante (classe A) — Additif de commit `brouillon2.md` et checklist de lancement Hetzner `ccx63` (v1)

## Verdict en tête : `LISTE FERMÉE DE CORRECTIONS REQUISES` (`brouillon2.md` `CONFORME EN L'ÉTAT` ; `4` corrections fermées sur `remplir_additif_commit_sondes_v2_v1.py` et `checklist-et-commandes-lancement-hetzner-ccx63-v1.md` avant lancement `ccx63`)

- **Pièce 1 — `docs/notes/sondes-v2-effectifs-et-correspondance-v1/diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md` (`958bb6a2f4c708b86958f5f6dcc1e9bb8af32021bf1a00b6398a588aab1fb01b`) : `CONFORME EN L'ÉTAT` pour scellement.**
  - Les `26/26` empreintes SHA-256 du paquet `src/controle_ia/sondes_v2/` et de `tests/test_sondes_v2_*.py` correspondent à l'octet au commit `0ce9e35110d93dd916e85b1191a2613b101e772d` dans `/home/antigravity/worktrees/sondes-v2-code` (arbre propre, `0` écart).
  - `note-des-effectifs-sondes-v2-v1.md` (`7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5`), `contre-lecture-r2-note-effectifs-et-correspondance-v1.md` (`5d46ac878fd469dd33069fffd215a7799dcdd83958b302fc6d409e898a081e7a`) et `GO-2026-11-24-02` (`R-5222`, plafond `68 USD`, `45,05 USD` attendus en `25,85 h` sur `ccx63` à `hel1`, repli automatique sur `--mode etalon` seul `~6,70 USD`) sont cités exactement.
  - Compatible avec `R-5209` point 2 : le marqueur `<CLAUSE_TABLE_CORRESPONDANCE_BBIS>` (l. 13) et le § 3 « Étape 4 » (l. 113) permettent de sceller `brouillon2.md` sans attendre `correspondance-rejeu-croise-v2.json`.
  - *(Observation mineure non bloquante : l. 15, l'empreinte citée de `CLAUDE.md` est `0fee605beae8…` reprise du brouillon 1, alors que `main` porte `dcd1e7ceddf4…`.)*
- **Pièce 2 — `docs/notes/sondes-v2-effectifs-et-correspondance-v1/checklist-et-commandes-lancement-hetzner-ccx63-v1.md` (`ddcd8903ba2b957f9882fddecb4da32e6c736008c634a8d9e08705dc182088ae`) et script `remplir_additif_commit_sondes_v2_v1.py` (`91ec23f6…`) : `4 CORRECTIONS FERMÉES REQUISES` (dont 3 bloquantes sur le script `cloud-init` et 1 adaptation courte sur `remplir_additif_commit_sondes_v2_v1.py`).**

---

## Liste fermée des corrections requises

1. **[Bloquante lancement — Casse garantie de `pousser_sorties` après 22 h de calcul du mode `complet`, suivie d'auto-destruction `R10` (`checklist` l. 286, 288 et 300)]**
   - Ligne 286 écrit `journaux-gels.sha256` (référençant `journal-gels-*.jsonl`) dans `$pub/epreuve-plantee-v4/complet/`, où ces fichiers `.jsonl` ne sont **pas** copiés (seule l'archive `.tar.gz` ou ses morceaux `.part.*` y sont copiés). De même, ligne 288 écrit `journaux-gels-complet.tar.gz.sha256` dans `$pub/epreuve-plantee-v4/complet/` même lorsque `TAILLE_MO > 90` (branche l. 293–296 où l'archive `.tar.gz` n'y est pas copiée).
   - Or la ligne 300 lance `find . -type f -name "*.sha256" … sha256sum -c` sur tout `$pub/epreuve-plantee-v4` **avant** `git push` (l. 305). Elle échoue donc **inconditionnellement** dès que le mode `complet` produit des journaux de gels (`No such file or directory`), interrompt `pousser_sorties` sous `set -e` avant le `git push`, et déclenche `trap detruire_serveur EXIT`, détruisant le serveur avec les 22 h de calcul non rapatriées.
   - **Correction** : vérifier `journaux-gels.sha256` dans `$SORTIE/complet` (ou nommer les manifestes des fichiers archivés/découpés sans suffixe `.sha256` lu par la boucle l. 300, p. ex. `journaux-gels.manifeste.sha256.txt` et `journaux-gels-complet.tar.gz.manifeste.sha256.txt` dans la branche `else`), de sorte que la ligne 300 ne vérifie que des `.sha256` dont les cibles existent réellement dans `$pub`.

2. **[Bloquante sécurité — Fuite potentielle de `GITHUB_PUSH_TOKEN` dans `$LOG` poussé sur GitHub (`checklist` l. 211, 213, 299, 305, 306)]**
   - `REPO_URL="https://x-access-token:${GH_TOK}@github.com/lciric/controle-ia-travail.git"` est passé directement à `git clone`, `git push` et `git ls-remote` alors que stdout+stderr sont capturés dans `$LOG` (l. 189) puis copiés dans `$pub/epreuve-plantee-v4/journal-execution.log` (l. 299) et poussés sur GitHub. En cas d'erreur réseau/HTTP, `git` affiche l'URL complète avec le jeton en clair dans stderr/log (et l'écrit dans `$WORK/repo/.git/config`).
   - **Correction** : utiliser l'URL nue `https://github.com/lciric/controle-ia-travail.git` avec un script `GIT_ASKPASS` (`chmod 0700`, lisant `/root/.gh_token`) ou `git -c http.https://github.com/.extraheader="AUTHORIZATION: basic …"`, et vérifier/masquer toute occurrence de `$GH_TOK` ou `$HCLOUD_TOKEN` avant de copier `$LOG` dans `$pub`.

3. **[Bloquante garde-fou R10 — Plafond interne `31h30` inopérant (`checklist` l. 311–314)]**
   - `timeout 113400 bash -c 'true'` termine immédiatement sans encadrer `lancer_mode etalon` (l. 315) ni `lancer_mode complet` (l. 319) : la coupure interne de `31h30` est un no-op complet.
   - **Correction** : poser une minuterie interne effective (p. ex. `(sleep 113400; echo "PLAFOND INTERNE 31h30 ATTEINT"; kill -TERM $$) & TIMER_PID=$!` tuée en sortie normale, avec `trap` qui stoppe les fils et laisse `trap detruire_serveur EXIT` détruire l'instance, ou encapsuler les appels `lancer_mode` sous `timeout`).

4. **[Adaptation courte protocole `R-5209` point 2 — `remplir_additif_commit_sondes_v2_v1.py` (`91ec23f6…`) et § 1.2 de `checklist` (l. 19, 45–65)]**
   - `remplir_additif_commit_sondes_v2_v1.py` (l. 128–149) refuse `--mode-correspondance jonction_tardive` sans `--fichier-correspondance` et `--rapport-cl-correspondance` déjà existants et contre-lus. Or `correspondance-rejeu-croise-v1.json` a reçu 2 corrections R2 (`5d46ac87…`) et `correspondance-rejeu-croise-v2.json` n'existe pas encore ; utiliser `rejeu_non_calculable` contredirait `GO-2026-11-23-36` / `R-5209` point 2.
   - **Correction** : ajouter dans `remplir_additif_commit_sondes_v2_v1.py` un mode `--mode-correspondance jonction_tardive_ulterieure` (exigeant `--go-correspondance GO-2026-11-23-36` et refusant tout fichier de correspondance) qui écrit la clause exacte de `R-5209` point 2 (table des champs écrite sans lecture de score, contre-lue en classe B et scellée par pièce jointe ultérieure avant toute ouverture des données réelles), mettre à jour la commande § 1.2 de `checklist` en conséquence, et aligner les noms de fichiers divergents des lignes 63 (`…-sondes-v2-v1.md`) et 64 (`…-v1.md`). *(Note opérationnelle : sur la devbox mère, lancer le watchdog externe R10 l. 382–412 en démon persistant `IsDaemon: true`.)*

---

## Détail des contrôles vérifiés

1. **Contrôle 1 (`brouillon2.md` contre `/home/antigravity/worktrees/sondes-v2-code` @ `0ce9e35110d93dd916e85b1191a2613b101e772d`)** :
   - `26/26` fichiers du tableau (l. 72–95) vérifiés par `sha256` : `0` écart ; tous les fichiers non-`.sha256` de `src/controle_ia/sondes_v2/` et `tests/test_sondes_v2_*.py` y figurent.
   - Toutes les empreintes citées en en-tête et en « Documents qui font foi » (hors `CLAUDE.md` noté ci-dessus) concordent à l'octet, y compris `note-des-effectifs-sondes-v2-v1.md` (`7338a3dc…`), `contre-lecture-r2-note-effectifs-et-correspondance-v1.md` (`5d46ac87…`), `verites_mondes_plantes_v4.json` (`b310e1af…`), `remplir_additif_commit_sondes_v2_v1.py` (`91ec23f6…`), `brouillon1` (`c8364982…`) et les pièces Option A / erratum v4.
   - `GO-2026-11-24-02` (`R-5222`, `68 USD`, `45,05 USD` en `25,85 h` sur `ccx63` à `hel1`, repli `--mode etalon` seul) exact.
2. **Contrôle 2 (`R-5209` point 2 et `remplir_additif_commit_sondes_v2_v1.py`)** : `brouillon2.md` conforme ; adaptation mineure du script requise (correction 4) pour sceller immédiatement sans bloquer le départ `ccx63`.
3. **Contrôle 3 (script `cloud-init` / Hetzner `ccx63`)** :
   - Syntaxe `bash -n` vérifiée (`rc=0` sur le lanceur externe, le script interne `cloud-init` après expansion `EOF`, et le watchdog externe).
   - Versions Python épinglées (`numpy==2.4.6`, `scipy==1.17.1`, `scikit-learn==1.9.1`) vérifiées identiques au `.venv` local.
   - Repli propre si refus de quota 48 vCPU (`ccx33` en `etalon_seul`, `184,7 h / 8 ≈ 23,1 h < 32 h`, `~6,70 USD`, relecture du prix API `PRIX_EUR_ACTIF`), préservation de `depot_propre=True` via `/opt/entree/`, preuve de rapatriement `git ls-remote` avant `detruire_serveur` par `SERVER_ID` numérique : conformes une fois les corrections 1 à 3 portées.

---

## Ligne « qui a lu quoi » (format `registres/qui-a-lu-quoi-v22.md`)

| # | Agent / session et rôle | Environnement / compte | Modèle | Pièces lues (exhaustif) et pièces non lues | Mandat / décision | Traces / sorties produites | Exclusions |
|---|---|---|---|---|---|---|---|
| à attribuer | sous-agent `4e84ba3498ebc3f79912c51893fba31b` (fils de `ff6e9350-ef6c-4238-b52d-64a517f4205f`, **contre-lecteur R2 neuf de classe A** de `brouillon2.md` et de la checklist Hetzner `ccx63`, strictement distinct de `964974f3677d3fc11cecb850254d332a`) | compte Antigravity (lecture seule sur `/home/antigravity/lciric/controle-ia-travail` et `/home/antigravity/worktrees/sondes-v2-code` à `0ce9e3511`, `PYTHONDONTWRITEBYTECODE=1`) | modèle hérité du parent (`inherit`, sous `GO-2026-11-23-33` / `-38`) | **Lu sur `main`** : `docs/notes/sondes-v2-effectifs-et-correspondance-v1/{diagnostics-prealables-sondes-v1-additif-commit-v1-brouillon2.md,checklist-et-commandes-lancement-hetzner-ccx63-v1.md,remplir_additif_commit_sondes_v2_v1.py,note-des-effectifs-sondes-v2-v1.md,contre-lecture-r2-note-effectifs-et-correspondance-v1.md}`, extraits ciblés `R-5056`, `R-5198`, `R-5209`, `R-5218`, `R-5222` de `registres/decisions.md` et `GO-2026-11-23-18`, `-33`, `-36`, `-38`, `GO-2026-11-24-02` de `registres/go.md` ; hachage SHA-256 seul des pièces de méthode citées. **Lu sur `/home/antigravity/worktrees/sondes-v2-code` (`0ce9e3511`)** : `src/controle_ia/sondes_v2/programme_monde_plante_v4.py`, hachage SHA-256 seul des 26 fichiers du paquet et essais et des pièces de méthode citées. **Non lus (cloisonnement strict)** : rien sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, `consigne-privee*`. | contre-lecture R2 classe A (`GO-2026-11-23-33`, `GO-2026-11-24-02`, `R-5209`, `R-5222`) | `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/lancement-sondes-v2-hetzner/contre-lecture-r2-additif-commit-et-checklist-hetzner-v1.md` (+ `.sha256`) | **exclu (R2)** de rédiger les corrections des pièces contre-lues ; **habilité** à vérifier ces corrections après rédaction ; aveuglement strict intégralement conservé |
