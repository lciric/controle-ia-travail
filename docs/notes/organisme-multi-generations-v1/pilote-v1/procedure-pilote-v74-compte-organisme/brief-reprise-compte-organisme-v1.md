# Brief de reprise du compte organisme sur un autre compte Claude — v1

Pour une session neuve, ouverte sur un autre compte, qui reprend le travail du compte organisme (modèle A). Écrit le 15 novembre 2026,
à la demande de Lazar transmise par la session mère. **Le pilote v12 n'est pas lancé ; cette reprise ne le lance pas.** Langue :
français, tutoiement avec Lazar, quasi aucun acronyme.

## 1. Dépôt et branches

- Dépôt de travail : `https://github.com/lciric/controle-ia-travail` (privé). **Jamais `lciric/controle-ia`** (copie publique expurgée).
- **`lot/compte-organisme-v1`** : la branche de ce compte (on y pousse). Sommet à la passation : voir la passation
  `registres-provisoires/passation-compte-organisme-2026-11-15-1843.md`.
- `prep/pilote-mr2-compte-organisme-v1` (`5432ac56…`) : code du pilote v72 à v74, texte scellé candidat 6
  (`docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`,
  `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`).
- `main` : lu seulement (registres, lignes de GO, vérifications de la mère) ; **ce compte n'écrit jamais dans `registres/`** : ses faits
  vont à `registres-provisoires/compte-organisme-2026-11-14-vN.md` (PO-NNN ; dernier : v28, PO-072), un nom neuf par version (R12).
- Arbre de l'organisme : tête `605e0f60f3eed0948948e6a4eb15cb73de1d03de`, sans dépôt distant ; il se monte depuis le paquet
  `procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle` (`e3d83e47…`, histoire tronquée) :
  `git init arbre && cd arbre && git bundle unbundle ../arbre-organisme-complet-605e0f6.bundle && git checkout 605e0f60f3eed0948948e6a4eb15cb73de1d03de`.
- `git fetch` toujours avec une refspec nommée (jamais sans).

## 2. Routine de reprise (R14), dans cet ordre

1. Cloner le dépôt de travail ; `git fetch origin +refs/heads/main:refs/remotes/origin/main +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1 +refs/heads/prep/pilote-mr2-compte-organisme-v1:refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1` ;
   travailler sur `lot/compte-organisme-v1`.
2. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`.
3. Lire `registres/etat.md` (sur `main`), la passation ci-dessus, le dernier journal provisoire (v28) et le brief du compte
   (`docs/notes/plan-paquet-multi-comptes-v1/brief-compte-organisme-v2.md`, `fc0229ad…`).
4. Inventaire des instances : **ce compte n'en crée ni n'en arrête aucune** et ne fait **aucun appel au loueur** ; il demande l'état à
   la mère.
5. `python -m pytest -q`, puis reprendre à la « prochaine action » de la passation.
6. Fin de session : passation datée par `date -u`, scellée, poussée ; journal provisoire neuf.

## 3. État du pilote MR-2 (au 15 novembre, 18:43Z)

- Procédure **v12** sans ssh : `procedure-pilote-mr2-v74-machine-v12.md` (`d0d2c8e11b26037fe9188cac4e8a845737b1f1f8e254a7537c8009f08110689a`),
  pièces `sans-ssh-v2/` (amorce `93b9c50d…`, programme machine `4fa7d368…` et aide `8af383f9…`, outil de la session `7e66e421…` et aide
  `2455b3de…`), essais `sans-ssh-v2/essais/` (17 scénarios rapides, scénario intégral, outil 36 cas : conformes).
- Vérification du différentiel v11 → v12 par la mère (`main`, `verification-differentiel-procedure-pilote-mr2-v74-machine-v12-v1.md`,
  `bcdfe138…`) : « jouable après corrections », sans version nouvelle ; **en attente** :
  - **N1** : consigne de la mère « prix relu au-dessus de 0,17 USD/h → destruction aussitôt, nœud » (la relecture de l'outil v2 accepte
    encore 0,20, alors que l'échéance est à 17 h) ;
  - **C1** : lecture de la mère sur M5 (clés au plus 17 h dans la configuration de l'instance, au-delà de la fin de l'autonomie) et
    acteur de chaque geste après 22:39Z, consignés et dits à Lazar **avant** l'impression de la commande ;
  - **C2** : création jouée sous la seule forme de la section 2, point 7, crochet éprouvé (cas sain et artefact) ;
  - **M5** : porté à Lazar par la mère.
- Épreuve des clés : faite (code 0, 0,001164 USD) ; ne se rejoue pas.
- **Qui joue** : la mère ou une session exécutante, jamais ce compte (R-2812, option (a)). Ce compte écrit, éprouve sur processeur,
  remet commit et empreintes, et répond aux vérifications. Si une correction de code est demandée : pièces neuves (`sans-ssh-v3/`, R12),
  différentiel déclaré, essais rejoués.

## 4. Lignes de GO en cours et leurs bornes (lues sur `registres/go.md` de `main`)

- **GO-2026-11-14-13** (π1) : pilote, proposeurs `fable52` (part 12 USD) et `opus55` (part 8 USD), crédits de Claude, 20 USD.
- **GO-2026-11-14-14** (π2) : `argon` et `astra` (9,36 USD chacun), **machine jetable 3 USD** ; 21,72 USD ; échéance 2026-11-30.
- **GO-2026-11-15-02**, étendue par **GO-2026-11-15-05** : épreuve des clés, 0,10 USD — consommée.
- **GO-2026-11-15-03** : autonomie de toutes les sessions **jusqu'au 2026-11-15T22:39Z** ; exclus : porte, publication, contact
  externe, compte ou dépôt nouveau, modification d'hypothèse, écart non accordé, changement de modèle, instance d'une autre session.
- **GO-2026-11-15-04** : passage des clés à la machine louée (lettre : « retirée de l'environnement de la machine dès ce geste fait »).
- Une nouvelle session vérifie chaque ligne au registre de `main` le jour même ; aucune dépense sans ligne inscrite **et** mot de Lazar.

## 5. Clés et jetons (par leur nom seulement ; jamais une valeur)

`RR_ANTHROPIC_API_KEY_RIGAUD` (interface de Claude, par `env -i`, sans `ANTHROPIC_BASE_URL`, seulement sous une ligne de GO),
`GEMINI_API_KEY`, `OPENAI_API_KEY`, `CONTROLE_IA_GITHUB_TOKEN_2` (jeton des machines, jamais le jeton de session). Ce compte n'en a
besoin que pour un appel sous ligne de GO ; pour écrire et éprouver, aucune.

## 6. Environnement à recréer

- `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src`.
- Python 3.13 avec **numpy 2.5.3** dans le chemin réduit `/usr/local/bin:/usr/bin:/bin` (le lanceur v74 et ses essais l'exigent) ;
  git 2.43, OpenSSL 3.0 (chiffrement de la phrase), bash 5.2.
- Pour rejouer les essais : `ESSAI_DEPOT=<dépôt de travail>` (refs distantes du lot, de prep et de `main` récupérées), puis
  `sans-ssh-v2/essais/LISEZMOI.md`.
- Outil du loueur (chez la session qui lance seulement) : `/home/user/vastai-env/bin/vastai` 1.8.3.

## 7. Interdits en vigueur (brief, section 6 ; à recopier en tête de toute consigne de sous-agent)

Aucune dépense ni machine louée sans ligne de GO inscrite et mot de Lazar. Aucune valeur de clé : jamais `env`, `printenv`, `set` sans
argument, `export -p`, `/proc/*/environ`. Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`,
`donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur,
`scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2` ; jamais `donnees/bras-attaque*`,
`donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche
`claude/compassionate-meitner-d4ryyk` ; aucune recherche récursive qui traverse ces chemins (pas de `ls registres`, pas de `find` ni
de `grep -r` larges ; fichiers nommés seulement) ; jamais `runs/course-ideation-conception-propre-v1/`, ni
`docs/notes/organisme-conception-propre-v1/lecture-*` ni `…/attestations/`. Jamais d'heure écrite à la main (`date -u` dans la même
commande). Garde des secrets à 0 avant chaque commit (motifs `sk-ant-`, `sk-…`, `ghp_`, `hf_`, `AKIA`, `AIza`) et garde des identifiants
de modèle (aucun identifiant de modèle Claude dans une pièce versée : « modèle A », « modèle B ») ; les pièces brutes qui portent des
identifiants servis restent hors de `main` (R-2731). Jamais toucher une instance ou un serveur que la session n'a pas créé. Aucun refus
de permission, du crochet ou d'un classifieur contourné, reformulé ni confié à une autre session : arrêt, rapport à la mère. Prévenir
la mère avant un geste qui risque d'être bloqué par un classifieur (R-2864). Rien de publié, aucun contact extérieur. R12 : jamais
récrire une pièce scellée ; sceller chaque pièce (`python -m controle_ia.scellement sceller`).

## 8. Machines actives

Aucune créée par ce compte. Intouchables : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, serveurs `poste-temoin-bailey-*`
(175884265, 175967712), et toute instance ou tout serveur non créé par la session. L'état réel se demande à la mère.

## 9. Communication

Avec la mère, directement, par l'envoi de messages entre sessions (session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` ; si le nouveau compte
ne la voit pas, Lazar relaie). Format : verdict d'abord, puis erreurs, changements, décisions ; commit et empreintes à chaque remise.
