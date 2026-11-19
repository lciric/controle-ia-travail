# Brief de reprise — fille de la lecture par lentille neuronale (« Neuron Lens ») — v2

Écrit le 2026-11-18 par la session `session_01XJ6MgnoxfSYHdF6rpEqZ7w`, sur le mot de Lazar « session neuve ecris la passation ».
Remplace, pour la reprise, la v1 (`brief-reprise-neuron-lens-v1.md`, sur `prep/neuron-lens-v1`), qui reste valable pour l'outillage.
À lire en entier avant tout geste. **Rien de payant sans GO écrit et feu de la mère.**

## 1. Qui, où
- Mère : `session_01XJ6Mgr8BN6UanALsQatc5E` (R-3103). Toutes les demandes de go et toute dépense passent par elle (consigne de Lazar
  relayée le 2026-11-18 vers 03:40Z). Contact : outil `send_message` du serveur Claude Code Remote.
- Lis d'abord `docs/procedures/orientation-sessions-v1.md` (branche principale). **Ne fouille pas le dépôt et ne lis pas les autres
  sessions** pour trouver ton rôle ; il est ici.
- Branches :
  - `prep/neuron-lens-v1` (tête `45a81e08`) : historique de la fille jusqu'au 17 novembre (code, journaux, verdicts, devis v1 à v6) ;
    lecture seule ;
  - `claude/tender-meitner-iyxt5i` : le travail du 18 novembre ; poussée avant la passation, et reprise par la mère.
  Pousse sur la branche que ton harnais te donne, en avance rapide sur la branche principale, et donne chaque sommet à la mère. Jamais
  `registres/` ni la branche principale : propose les lignes à la mère.

## 2. État
- **Devis final** de la tranche de l'ajustement de nos lentilles (B-β) : `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md`
  (`41a4c1f6…`). Décisions de Lazar en tête (GO-2026-11-18-02) :
  - prix exigé 2,62 USD/h ;
  - plafond avec une relance de 75 USD : arrêt dur à 67,5 USD, compte rendu à 45,0 USD ;
  - lieu L1 : aucun rangement des lentilles ;
  - clé neuve ;
  - périmètre entier, lentilles R et S.
  **Rien ne s'engage** avant le préenregistrement scellé, les correctifs, la commande contre-lue, la clé neuve confirmée par Lazar, un
  relevé dans l'heure qui précède la création et le feu de la mère. Au plus tôt le 19, au plus tard le 25.
- **Préenregistrement de la tranche** :
  - brouillon 1, `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1-brouillon1.md` (`af6d4788…`) ;
  - sa contre-lecture, `docs/notes/neuron-lens-v1/contre-lecture-texte-gele-tranche-b-beta-v1-brouillon1.md` (`4d52c0be…`) : à corriger,
    2 bloquantes, 6 majeures, 13 mineures.
- **Prochaine action : le brouillon 2**, point par point sur ce rapport (liste dans la passation de 03:33Z), en commençant par :
  1. la bloquante 1 : séparation des corpus d'ajustement (lignes 0 à 999 de DCLM) et d'activations (à partir de la ligne 1 000,
     `05_act_corpus.py` `DCLM_SKIP`) ;
  2. l'inventaire des réglages de Llama dans le code voisin (M-5), à faire **avant** le scellement.
  Ensuite : contre-lecture du brouillon 2 par un agent neuf d'un autre modèle, scellement R1, remise à la mère. La mère conseille « deux
  versions solides plutôt que onze ».

## 3. Outils à recréer (conteneur neuf)
- `python3 -m venv .venv && .venv/bin/pip install -r requirements-cpu.txt pyarrow==26.0.1`.
- Arbre de lecture de la branche de la fille :
  `git fetch origin prep/neuron-lens-v1 && git worktree add --detach <carnet>/nl origin/prep/neuron-lens-v1`.
- Copie de lecture du code voisin, **jamais exécutée** :
  `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/stdlogits/neuron-lens /home/user/stdlogits/neuron-lens`, puis `fetch` et
  `checkout` du commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`.
- Outil du loueur, seulement pour des relevés en lecture seule :
  `python3 -m venv /home/user/vastai-env && /home/user/vastai-env/bin/pip install vastai==1.11.0` ; relevé par
  `docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v3.py`.
- Essais de la fille (depuis l'arbre de lecture) : 312 passés, 2 sautés.
- Clés par leur nom seulement, jamais affichées : `CONTROLE_IA_GITHUB_TOKEN_2`, `VAST_API_KEY`, `HF_TOKEN` (à révoquer : **n'en passer
  aucune à une machine**), `HCLOUD_TOKEN`.

## 4. Interdits (rappel)
Ceux du `CLAUDE.md` et du brief v1, § 8. En plus : nommer par ce que c'est et ce que ça fait, le sigle seulement en appui (R-3085) ;
déclarer à la mère toute lecture hors rôle (orientation, § 6).
