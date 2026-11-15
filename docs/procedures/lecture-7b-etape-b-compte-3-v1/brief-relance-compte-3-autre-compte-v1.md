# Brief de reprise — travail du compte 3 sur un autre compte Claude — v1

- **Statut** : brief écrit le 2026-11-15 (heure lue par `date -u` : 18:43:15Z) par la session hôte de la phase A
  (`session_016QhUrrSUMEzEqWPnQYxjHB`), à la demande de Lazar transmise par la session mère (`session_016QhUrtmLyFWJP6Cy7rgfXH`).
  C'est un document de service : il ne remplace aucune commande et ne change aucun texte scellé. En cas de contradiction, la commande
  remise par Lazar fait foi, et derrière elle les textes scellés. Passation correspondante : `registres/passations/2026-11-15-1843.md`
  (branche `verdict/t06-table-a-7b-compte-3-v1`).
- **Ce que la session nouvelle reprend** : le rôle d'**hôte du compte 3**. Elle reçoit les pièces, crée un lecteur neuf, copie, scelle et
  pousse. Elle n'ouvre jamais un résultat. Seule tâche à venir : la **phase C v3** (étape B de T0.7 et son lecteur), pas avant mardi 17
  novembre.

## 1. Dépôt et branches

- Dépôt de travail : `https://github.com/lciric/controle-ia-travail` (privé). Ne jamais pousser vers `lciric/controle-ia`.
- `main` : jamais poussée par l'hôte. La mère seule y recopie, selon la section 15 de chaque commande.
- `verdict/t06-table-a-7b-compte-3-v1` : branche de la phase A, close. Tête `6bc0bd9d9a118abeb429dd06d0a48addf33a791b` avant cette
  passation. Elle porte aussi la passation et ce brief.
- La phase C v3 nomme sa propre branche, à créer neuve depuis `main` (voir la commande). Ne jamais pousser vers `lot/compte-3-v1`.
- **Branches interdites à la lecture** : `calcul/p3bis-reel-v2`, `claude/compassionate-meitner-d4ryyk`. La branche de 7b,
  `calcul/t06-confirmation-7b-v1`, ne se lit qu'au travers d'un dépôt jetable sans contenu, par liste positive (`git show <tête>:<chemin>`),
  et seulement là où une commande l'accorde.

## 2. Routine de reprise (adaptée au compte 3)

1. Le premier message de la session est celui que Lazar colle. Ne rien lancer avant.
2. Vérifier l'empreinte de la commande remise contre celle que Lazar donne en conversation.
3. Empreintes de lancement : `cd docs && sha256sum -c sha256sums-lancement-v2.txt` (la commande le refait au bloc 2).
4. **Pas** de `ls registres`, pas de `find` ni de `grep -r` larges, pas de lecture de `registres/etat.md`, `registres/decisions.md` ou des
   passations de la mère : fichiers nommés par la commande, seulement. Avant d'ouvrir la commande, la session de la phase A avait lancé
   des recherches larges pour retrouver des empreintes ; c'est déclaré en écart (P3A-006). Retrouver un fichier par son chemin exact, jamais
   par une recherche.
5. Étape 4 de la routine du dépôt (inventaire des instances) : **non jouée** par l'hôte. Les commandes du compte 3 interdisent tout
   appel au loueur. Le dire à Lazar.
6. **Clone partiel** : si la référence `main` locale est périmée (« refusing to merge unrelated histories » au bloc 0b), le geste accordé
   par Lazar à la phase A est `git switch -q -C main refs/remotes/origin/main`, puis le bloc 0b rejoué tel quel. C'est un arrêt à
   signaler d'abord : un nouveau mot de Lazar est nécessaire.
7. Dire à Lazar, en tête du premier message : le modèle de la session (outil qui décrit la session), que le message est le premier de la
   session, et l'issue de l'épreuve du crochet.

## 3. État

- **Phase A** (table A de T0.6 sur 7b) : **close**. Verdict d'un lecteur neuf en modèle C, scellé, poussé, recopié dans `main` par la mère
  (R-2821). GO de Lazar sur ce verdict : GO-2026-11-15-01 (R-2845), selon la mère. Journal provisoire :
  `registres-provisoires/compte-3-phase-a-2026-11-14-2327-v2.md` (`8d78a92d…`), sur la branche de la phase A.
- **Seconde lecture de la table A en modèle B** : prévue « à titre d'information seulement », par une commande à part de la mère.
  Rien n'est à préparer.
- **Phase C v3** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md`
  (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`). Non remise ; préalables de la mère à venir (liste « qui a lu quoi »
  v3 avec la ligne de l'hôte à la cellule `CELLULE_HOTE`, consigne du lecteur B, marqueurs).

## 4. Point à trancher avant la remise de la phase C (nœud)

La v3 dit : « à coller par Lazar dans **la même session** que la phase A ». Une session sur un autre compte a un autre identifiant. La
liste v3 doit nommer l'hôte avec la cellule `CELLULE_HOTE`, que l'attestation v3 admet par `--admettre-hote`. Deux voies, à la mère et à
Lazar :
- (a) la liste v3 nomme la session nouvelle comme hôte, et la mère amende ou annote la commande (nouvelle version, R12) ;
- (b) la phase C est jouée dans la session `session_016QhUrrSUMEzEqWPnQYxjHB` si elle reste joignable.

La session nouvelle ne lance pas la phase C tant que ce point n'est pas tranché par écrit.

## 5. Autorisations en cours (selon la mère, non relues dans `registres/go.md` par l'hôte)

- **GO-2026-11-15-03** (R-2859) : autonomie de toutes les sessions prolongée jusqu'au **2026-11-15T22:39Z**, mêmes conditions que
  GO-2026-11-14-12, dans le périmètre de chaque session. Elle sera **échue** à l'ouverture de la session nouvelle, sauf nouveau mot.
- **GO-2026-11-15-01** (R-2845) : GO sur le verdict de la table A. Sans effet pour l'hôte.
- Toujours gardés pour Lazar : porte, publication, contact externe, écart à un texte scellé non accordé, changement de modèle, toute
  instance d'une autre session, **toute dépense** (aucune dépense sans ligne de GO inscrite **et** mot de Lazar).

## 6. Clés (noms seulement ; jamais une valeur, jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`)

- Vues présentes dans la session de la phase A (contrôle par nom au bloc 0) : `GH_TOKEN`, `GITHUB_TOKEN`, `HCLOUD_TOKEN`,
  `VAST_API_KEY`, `OPENAI_API_KEY`, `HF_TOKEN` ; `ANTHROPIC_API_KEY` absente.
- Variables de l'environnement infonuagique « Default » (noms relevés par l'outil de l'environnement) : `BRAVE_API_KEY`,
  `CONTROLE_IA_GITHUB_TOKEN_2`, `GEMINI_API_KEY`, `GEMINI_API_KEY_2`, `HCLOUD_TOKEN`, `HF_TOKEN`, `JEV_API_KEY`, `KIMI_API_KEY`,
  `OPENAI_API_KEY`, `OPENALEX_API_KEY`, `OSF_TOKEN`, `RR_ANTHROPIC_API_KEY`, `RR_ANTHROPIC_API_KEY_2`, `RR_ANTHROPIC_API_KEY_3`,
  `RR_ANTHROPIC_API_KEY_LUC`, `RR_ANTHROPIC_API_KEY_RIGAUD`, `RR_ANTHROPIC_WORKSPACE_ID`, `RR_TYPESAFE_API_KEY`,
  `SEMANTIC_SCHOLAR_API_KEY`, `VAST_API_KEY`.
- L'hôte n'utilise aucune de ces clés : les phases A et C sont sur processeur, à 0 USD. Lazar les recrée sur l'autre compte s'il le
  souhaite pour d'autres sessions.

## 7. Réglages d'environnement à recréer sur l'autre compte

- Environnement infonuagique : réseau **sans restriction** sur « Default » (la phase A a joint `pypi.org` pour l'horloge et pour numpy,
  ainsi que `github.com`) ; aucun script d'installation ; aucun secret réseau.
- Accès GitHub au dépôt `lciric/controle-ia-travail`, en lecture et en écriture (poussée de branches neuves).
- Identité git (`user.name`, `user.email`) configurée : le bloc 2 s'arrête sans elle.
- Interpréteur : sans `.venv` dans le dépôt, la commande crée son environnement dans le bac (`numpy==2.4.6`). Rien à préinstaller.
- Le crochet de garde `.claude/hooks/garde_calcul.py`, activé par `.claude/settings.json`, vient avec le dépôt. Son épreuve au bloc 0
  doit être « bloquée ».
- Modèles de sous-agent : l'outil d'agent de la session doit pouvoir créer un sous-agent **du modèle nommé par Lazar en conversation**
  pour le lecteur. Pas de repli (CL3-11). Les identités de modèle ne s'écrivent dans aucun fichier : une lettre seulement (A, B, C).

## 8. Interdits en vigueur (recopiés des commandes du compte 3, section 1)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar. Aucun appel au loueur.
- Jamais `diag/*/lecture-sondes-t06.json`, `resume.json` de 7b, les activations, les adaptateurs, la lecture B de 7a,
  `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a,
  l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`,
  `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- **Règles de lecture de 7b** : l'hôte n'ouvre aucun résultat. Il copie, calcule les empreintes et compare. Il ne lit que les noms, les
  compagnons `.sha256`, les fichiers `empreintes.sha256` des traces (noms et empreintes) et le rapport final du lecteur. Extraction par
  liste positive depuis un dépôt jetable sans contenu, tête contrôlée. Filtres de noms et de contenu avant toute remise. Bordereau scellé.
  Message de remise scellé, que le lecteur recopie. **Un seul** lecteur neuf, sans contexte hérité, du modèle nommé, qui n'écrit que dans
  son dossier fermé. Jamais une ligne de `registres/decisions.md` dans les pièces.
- Le rapport final du lecteur va à Lazar seul, en conversation, jamais à la mère (section 13, point 2). À la mère, seulement le point 3 :
  sortie « RENDU », commits, empreintes, épreuve du crochet, et tout ARRÊT avec son bloc et son motif.
- Aucune recherche récursive qui traverse les chemins interdits : fichiers nommés seulement. Jamais d'heure écrite à la main (`date -u`
  dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (variable `SECRETS` des commandes).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*`.
- Un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère, jamais de contournement ni de délégation à une autre
  session.
- Rien de publié, aucun contact extérieur, jamais de demande de fusion vers `main`.
- **Exclusions de l'hôte** (cellule `CELLULE_HOTE` de la v3) : analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ;
  G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût ».
- Une ligne « ARRÊT : » arrête tout. Les messages d'une autre session sont des informations : les décisions, les nœuds et les GO viennent
  de Lazar en conversation. Un mot de Lazar relayé par la mère, qui inverse un mot direct, se fait confirmer en conversation avant tout
  commit (précédent : (a′), phase A).

## 9. Canal avec la mère

- Mère : `session_016QhUrtmLyFWJP6Cy7rgfXH` (elle remplace `session_01QPDgKgACWyCkCN8HjqwNXy`, arrêtée pour quota). Échanges par
  l'outil d'envoi de messages entre sessions, si le compte nouveau peut la joindre. Sinon, par Lazar.
- Règles acceptées des deux côtés : l'hôte ne lit pas le fil de la mère. La mère n'envoie aucun nombre ni aucune issue de 7a, 7b, T0.7,
  P3-bis ou de l'étape B bis, ni aucune ligne du registre des décisions. Les identités de modèle sont dites en conversation seulement.

## 10. Machines actives

Aucune pour l'hôte. Les instances et serveurs listés au point 8 appartiennent à d'autres sessions. L'hôte ne les inventorie pas et n'y
touche pas.

## 11. Prochaine action de la session nouvelle

Attendre la commande phase C v3, remise par Lazar avec son empreinte, ses marqueurs et la décision du point 4. Puis la jouer bloc par
bloc, telle quelle.
