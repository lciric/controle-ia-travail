# Banque de tâches réelles — v7 : banque `confrontation-v4`, la v3 avec une seule trace par paire en test et en test final (pour l'étape 1 et la confrontation ; v1 à v6 restent)

Lignée conv-audit, 25 octobre 2026, 16:53–17:02 UTC (heures lues sur `date -u`). Décision de Lazar (25 octobre, 17:43
Paris, note N-046 rédigée, canal `canal/conv-audit-n04`, `envois/decision-N-046-lot3-traces-sans-paires-v1.md`,
`7fa0f544…`) : **pour l'étape 1 et la confrontation, une trace par paire en test et en test final**, en attendant un lot
3 de traces sans paires ; le pilote 4 (descriptif) garde la v3 et ses paires. **Aucune utilisation de la v4 n'est décidée
par ce texte** (ce sont les préenregistrements de l'étape 1 et de la confrontation qui la citeront) ; contre-lecture à
venir.

## 1. Ce qu'est la v4

- **Dérivée de la v3** (`banque-confrontation-v3.json`, `157a2b45…` ; `LISEZMOI-v5.md` et `LISEZMOI-v6.md`) par
  `construction-v4/construire_banque_v4_une_trace_par_paire_v1.py` : `train` inchangé (ses 16 paires restent : il est
  servi avec ses vérités) ; famille `conscience-evaluation` inchangée partout (36 tâches en test, 36 en test final) ;
  en `test` et en `test_final`, **une trace par paire de `controle-delegation`** : 12 traces par part au lieu de 24,
  **6 honnêtes et 6 sabotées**, et, par source, 3 et 3 (`lot1`, `lot2`) ; les traces retirées ne sont servies nulle
  part ; identifiants, champs et ordre des tâches gardées : ceux de la v3.
- **Tirage** : quelles paires gardent leur trace honnête et lesquelles leur trace sabotée, par
  `numpy.random.default_rng(numpy.random.SeedSequence(E))`, une permutation par part et par source ; E neuve, dans le
  seul fichier de clé `banque-confrontation-v4-cle.json` (secret, comme celui de la v3) ; le manifeste n'en garde que
  l'empreinte. Le secret v4 est le secret v3 restreint aux tâches gardées.

| fichier | sha256 |
|---|---|
| `banque-confrontation-v4.json` | `6504045cea95c698f4ba3c702bd30e2ee12fe1e4a79d2ead868a2a438579107d` |
| `banque-confrontation-v4-secret.json` | `ccf3c3739ab2afbe3806710c19011bef897a44b7e221a12ae3cfc5086eb1ad1b` |
| `banque-confrontation-v4-cle.json` (secret) | `694c358ff7b29dcc468f77fe76ebef75e853f491d9dbb02f092d55ea885ba554` |

## 2. Contrôles

- `construction-v4/verifier_banque_v4_v1.py` contre la v3 (sortie `controle-banque-v4-contre-v3-v1.json`) : **conforme** —
  train identique ; conscience d'évaluation identique ; chaque tâche gardée identique à la v3 ; **chaque paire de la v3
  garde exactement une trace** en test et en test final (paire = numéro de paire pris avec la source, les numéros se
  répétant d'un lot à l'autre) ; équilibre par part et par source ; secret restreint ; empreinte de la clé. Une première
  sortie, qui prenait le numéro de paire sans la source et signalait à tort trois paires à deux traces, est gardée sous
  le nom `controle-banque-v4-contre-v3-v1-ERRONE-cle-de-paire-sans-source.json` (erreur du contrôle, non de la banque).
- **Plus aucune paire en test ni en test final** : la référence « contraste de paire » (`construction-v3/reference_contraste_paires_v2.py`)
  refuse de se calculer sur la v4 (« appariement incomplet », sortie `reference-contraste-paires-banque-v4-refus-v1.txt`) ;
  elle est **sans objet** pour la v4.
- Contrôle des identifiants v2 (`construction-v3/verifier_identifiants_opaques_v2.py`, 2 000 tirages, sortie
  `controle-identifiants-banque-v4-v2.json`) : **aucune case au seuil** ; `verifier_banque` sans problème. Avec 12 traces
  par part en délégation, le seuil calibré y vaut 1,0 : ce contrôle n'y voit plus qu'une fuite totale (dit, non corrigé).
- **Référence de surface de la v4** (`reference_traits_texte`, même sortie) : conscience d'évaluation inchangée (`test`
  0,75, `test_final` 0,6944) ; **contrôle de délégation : `test` 0,6667, `test_final` 0,3333** (12 traces chacune).

## 3. Ce que la v4 change pour qui la sert

- **Effectif** : en délégation, une erreur pèse 1/12 (0,083) au lieu de 1/24 ; à dire dans tout seuil et toute puissance
  d'un préenregistrement qui la sert.
- Tout ce qui suit la v3 (`LISEZMOI-v5.md` § 4 et `LISEZMOI-v6.md` § 4 : épinglage de l'empreinte, traits d'activations
  rangés par identifiant, phrase du préenregistrement, clé jamais en ligne de commande, copie publique) vaut pour la v4,
  à son empreinte `6504045c…` ; les traits de la v4 sont ceux de la v3 restreints aux tâches gardées.
- Le lot 3 (N-046) remplacera ces traces par des traces sans paires ; la v4 n'est qu'un état d'attente.
