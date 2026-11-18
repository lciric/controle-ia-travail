# Brief de lancement — session de relance des organismes discrets, reprise sur un autre compte — v2

À coller tel quel comme premier message de la session neuve (dépôt `lciric/controle-ia-travail`). Écrit le 18 novembre 2026
à 15:16Z par la session sortante `session_01XJ6MgpChR1JWSMBxSQcf3c`, sur le mot de Lazar : « ecris la passation et brief de
lancement pour nouvelle session au tre compte ». v2 (15:22Z) : seule la section « Session mère » change ; la mère a déjà
changé de compte (la v1, `db9f7d43…`, est gardée, R12).

---

Tu reprends la **session de relance des organismes discrets** du programme de Lazar (directeur). Français, tutoiement,
aucun sigle sans son nom en clair. Le fichier `CLAUDE.md` du dépôt fait foi et prime sur ce brief.

## 1. Ton rôle

Tu fais tourner l'**organisme d'idéation** (orchestrateur du dépôt public `lciric/ideation-organism`) sur la question de
conception des organismes discrets. Les courses, leurs relais, leurs lanceurs et leurs pièces sont à toi. Les registres
(`registres/`, dont `go.md`, `etat.md`, `decisions.md`, `depenses.md`) sont **réservés à la session mère**. Tu tiens ton
propre journal, `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` (suite : OD-032), et
tes passations, sous `docs/notes/relance-organismes-discrets-v1/`.

**Session mère** : `session_013QMayjsoZJFBUCqcnvD5h1`, sur le compte neuf, inscrite sur `main` sous R-3284 (13:56Z) ; elle
tient `registres/etat.md` et les décisions à partir de R-3284 ; canaux : `registres/canaux-sessions-v3.md`. L'ancienne mère
`session_01XJ6Mgr8BN6UanALsQatc5E` n'écrit plus et ne décide plus rien : ne lui écris pas. Si la mère change encore, la
plus récente se trouve dans `registres/etat.md` sur `main`, ou demande à Lazar. Toute demande de GO passe par elle.
Toute dépense lui est signalée **avant**, avec la ligne de GO. Si tu ne la joins pas, consigne départs et coûts dans ta
passation : une mère neuve les lira dans le dépôt.

## 2. Démarrage

1. Récupère le travail : `git fetch origin claude/eloquent-tesla-e52a0b`, puis fusionne-le dans ta branche de session
   (`git merge --no-edit FETCH_HEAD`). Fusionne aussi `main`. Ne pousse jamais vers `main` sans mot exprès. Ne pousse
   jamais vers `lciric/controle-ia`.
2. Routine de reprise de `CLAUDE.md` (R14) :
   - vérifie les empreintes, `sha256sum -c` dans `docs/`, puis `python -m controle_ia.scellement verifier-arbre .` ;
   - lis `registres/etat.md` et, **avant tout**, `docs/notes/relance-organismes-discrets-v1/passation-2026-11-18-1516.md` ;
   - inventorie les instances (aucune n'est attendue de cette session) ;
   - lance `python -m pytest -q`.
3. Environnement :
   - `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src` ;
   - **toujours** `PYTHONDONTWRITEBYTECODE=1` et `python -B` : un dossier de cache dans le clone de l'orchestrateur fait
     refuser toute course.
4. Avant toute course seulement, prépare l'orchestrateur et vérifie les chemins :
   - clone `https://github.com/lciric/ideation-organism` sous `/home/user/lciric/ideation-organism` et place-toi au commit
     `a41b7b50` ;
   - vérifie `git -C /home/user/lciric/ideation-organism rev-parse HEAD:orchestrator` =
     `ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70` ;
   - les lanceurs exigent le dépôt à `/home/user/controle-ia-travail` et l'interpréteur `/usr/local/bin/python3` ; s'il
     manque, ne change aucun lanceur scellé : signale-le.
5. Clés, **par leur nom seulement**, jamais affichées : `RR_ANTHROPIC_API_KEY_MINUIT` (relais Claude), `OPENAI_API_KEY`
   (Astra), `GEMINI_API_KEY` (Carbon, Argon), `KIMI_API_KEY` (Kimi). Vérifie leur présence par le nom. Le compte neuf peut
   ne pas les avoir ; dans ce cas, le dire à Lazar.

## 3. Où on en est (détail et empreintes dans la passation)

Trois lignées sont **lisibles** : Carbon par lot (lanceur v12), Astra seconde (v13), Argon seconde (v14). Elles comptent
29 fiches validées, **aucune ouverte**, et environ 10,3 USD dépensés sous le plafond commun de 34 USD. Kimi est épuisé sous
GO-17 : Moonshot était surchargé. Aucun relais, aucun processus, aucune machine en marche.

## 4. Ce qui attend Lazar — ne rien lancer sans son mot

1. **Attestation de lecture** pour les juges externes différés de Carbon, Astra et Argon. Les consignes en attente sont
   `1d7b5dbb…`, `3f0c649e…` et `0601270c…`, chacune dans `copies/` de son run. Ensuite viennent les bras des juges
   externes, sur devis et ligne de GO de la mère. Le lanceur du bras
   (`scripts/lancer_bras_juge_ideation_organismes_discrets_v1.py`) est à revoir contre les lanceurs v12 à v14,
   contre-lecture comprise, avant tout usage.
2. **Kimi** : reprise par une ligne neuve quand Moonshot sera stable. Recommandation : trois sondes réussies de suite ;
   défaut : attendre.

## 5. Règles à tenir, apprises le 18 novembre

- **Aucune fiche ouverte** avant la lecture décidée par Lazar. Seuls se lisent la lecture des témoins, les comptes et les
  relevés.
- **Arrêts par PID (R10)**, jamais par motif. Lis `/relais/etat` avant d'arrêter un relais.
- Relais toujours lancés par `scripts/lancer_relais_local_v1.py` (procédure `docs/procedures/relais-persistants-v1.md`),
  journal hors dépôt. Après la course, verse au dépôt les journaux, états et consoles des relais : sans clé ni texte, ils
  sont scellés. Exemple : `relais-hors-depot-2026-11-18-v1/`.
- Réseau du conteneur : toute connexion muette plus de 300 s est coupée. Carbon synchrone à 8 192 jetons de pensée reste
  muet : il passe **par lot** (enveloppe Carbon v3, relais Gemini v4, port 8792). Argon synchrone répond en 92 à 150 s.
- **Garde de GO** des lanceurs : une seule ligne principale doit porter les trois expressions du périmètre, et pour les
  lanceurs v13 et v14, ne nommer aucune autre « lignée … ». Les lignes « extension » ne comptent pas.
- **Nouvelle version = nouveau nom (R12)** : un lanceur scellé ne se modifie jamais. Toute pièce neuve passe par essais,
  essai à sec, contre-lecture par un agent neuf (Opus, pas Fable ; un seul agent à la fois jusqu'au 22 novembre), puis
  scellement (`python -m controle_ia.scellement sceller …`).
- Commite et pousse ta branche à chaque étape, y compris les copies de runs et le journal.
- Messages à Lazar : verdict d'abord ; écris-lui seulement pour un prononcé, une réserve, une demande de GO ou une dépense.
