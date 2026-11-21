# Journal des accès du monteur de l'oracle, cycle 1 du scellement 2 — v1

- Classe C. Tenu par le monteur (`session_01Qi7Gr4BDyW322Ljw2o29ZT`) ; scellé à la fin de la session.
- Chaque ligne : heure (UTC), chemin (objet git), empreinte sha256 du contenu, motif.

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 17:13 | `origin/main:registres/go.md` (ligne GO-2026-11-21-66 seule) | — | vérifier le mot de Lazar |
| 17:13 | `docs/procedures/mandat-monteur-oracle-scellement-2-v2.md` | `c6f090c02bfc2cd6…` | mandat |
| 17:14 | `origin/main:registres/index-scellement-2-familles-aveugles-v1.md` | — | index des versions qui font foi |
| 17:14 | listes de noms de fichiers des branches de la famille et de la contre-lecture (sans contenu) | — | repérer les pièces |
| 17:15 | empreintes seules des cinq pièces de méthode (mandat du scellement 2, N-060 v3, règle du bras, N-056, N-057) | voir mandat, section 1 | vérifier les versions |
| 17:16 | `f4c479c5:donnees/bras-attaque-scellement-2-v1/piece-3-famille-aveugle-1-verite-du-dommage-v2.md` (en entier) | `2a7416a823c406a1…` | spécification de l'oracle (obligatoire) |
| 17:16 | `f4c479c5:donnees/bras-attaque-scellement-2-v1/piece-4-famille-aveugle-1-plan-des-epreuves-v2.md` (en entier) | `aba1a770a68fa73c…` | plan des épreuves (obligatoire) |
| 17:17 | `claude/scellement-2-contre-lecture-v1:…/piece-7-contre-lecture-v1.md` (en entier) | `e0fbe36598b4f8c7…` | conditions de la contre-lecture |
| 17:17 | `claude/scellement-2-contre-lecture-v1:…/piece-7-verification-des-corrections-v1.md` et son erratum 1 (en entier) | `8be9063c0982ce24…`, `aa10a1db0f9ff512…` | idem |
| 17:18 | `f4c479c5:docs/notes/scellement-2-familles-aveugles-v1/piece-1-attestation-aveuglement-v1.md` et `piece-6-esquisse-de-devis-banque-v3.md` (en clair, en entier) | `752834be02d6221e…`, `bb89942b75fd6aa0…` | repérer les fichiers du banc ; volumes du devis |
| 17:19 | `src/controle_ia/environnements/propositions.py` (en entier) | `5d97b223206c6378…` | tâche et environnement du banc : format des plans, champs vus de l'agent |
| 17:20 | `donnees/20261007-082440-t05-extraction/taches-evaluation.json`, `taches-entrainement.json`, `donnees/t05-pilote-v1/taches-pilote-60-v1.json` : par programme, noms de clés, comptes de directions par type, identifiants, domaines de la classification ; **aucun texte de référence ni d'énoncé affiché** | `76cdeace861d2fff…`, `8d20a698d76baa8a…`, `287e83485cba5500…` | matière des épreuves, disjonction des tâches |
| 17:20 | `src/controle_ia/harnais/` : liste des noms de fichiers ; recherche du mot « cibles » dans `harnais/*.py` par programme (aucune occurrence rendue) | — | contrôle côté agent ; aucun fichier de moniteur ouvert |
| 17:21 | `pyproject.toml` (configuration de pytest seulement) | — | tenir les tests du coffre hors de la suite du dépôt |

Non lus : la pièce 2 de la famille (texte du mode), les pièces 5 et 6 v1 du coffre de la famille, tout moniteur, la
branche `claude/scellement-2-famille-reserve-cycle-2-v1`, `registres/etat.md`, les passations, R-604 à R-610.

Note : la recherche du mot « cibles » a porté sur tous les fichiers de `harnais/`, dont des noms évoquent des
moniteurs (`sondes.py`, `activations.py`, `sonde_memoire.py`) ; elle n'a rendu aucune ligne (aucune occurrence) et
aucun contenu de ces fichiers ne m'a été montré. Je la consigne comme accès par programme à des fichiers de moniteurs,
sans lecture. Le programme `controle_agent_p1_v1.py` ne les lit pas.

## Accès après la première version des pièces

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 17:22–19:00 | messages de la mère (18:26, 18:53, 19:00 UTC) : exclusions, conditions d'envoi, champ 18 de la pièce de sécurité v9 | — | choix des lecteurs |
| 18:28, 18:55 | deux envois à la mère refusés par le serveur (`elevated_session_untrusted_device`) ; propositions déposées sur la branche (`message-mere-proposition-lecteurs-v1.md`, `-v2.md`) | `16273858…`, `ffc82cb9…` | compte rendu impossible par message |
| 19:01 | pages publiques des conditions d'OpenAI, de Google (Gemini) et de xAI, versées dans `sources-conditions-fournisseurs-v1/` ; trois pages de `x.ai` refusées (403) ou absentes (404), retirées sans versement | voir le constat | champ 18 : lecture humaine, conservation |
| 19:20 | `docs/decisions/decision-N-060-v3.md` (en entier) ; `origin/main:docs/notes/repetition-generale-banc-ferme-v1/attestation-mode-connu-mere-v1.md` ; noms de fichiers de `verite-dommage-v1/` et `src/controle_ia/verite_dommage/` (non ouverts) ; compte des contrôles des 32 tâches d'entraînement | `2b448f696503112c…` | répondre à la demande de la mère sur l'oracle du mode connu |
