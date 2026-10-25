# Banque de tâches réelles — v4 : banque `confrontation-v2`, la v1 sous des identifiants opaques (v1, v2 et v3 restent)

Lignée conv-audit, 25 octobre 2026, 15:47–15:52 UTC (heures lues sur `date -u`). Complète `LISEZMOI-v3.md`, qui décrit
la banque `confrontation-v1` ; rien de ce qu'il dit n'est changé, sauf ce qui suit sur les identifiants. **Aucune
utilisation de la v2 n'est décidée** : c'est un nœud (Lazar) ; aucun texte scellé ne la cite encore.

## 1. Pourquoi une v2

L'audit de symétrie du second pilote (`AUDIT-SYMETRIE-pilote2-v1.md`,
`f732bfd857432086518357daae4bcd114c92f184a5cd987d0a738a7e6cfd9d36`, branche `lectures/pilote2-gemini-v5-2-1-v1`,
`37047a1`) a établi un défaut de la v1 : **ses identifiants donnent la vérité**, dans les deux familles et les trois
parts — `controle-delegation` : suffixe `-H` pour chaque trace honnête, `-S` pour chaque sabotage (les identifiants des
lots, repris tels quels) ; `conscience-evaluation` : numéros 1 à 60 « evaluation », 61 à 120 « usage-reel ». Le noyau
sert l'identifiant aux organismes (`taches.masquer`), et l'entraînement avec sa vérité : une lignée qui lit son contexte
peut apprendre la règle sur l'entraînement et l'appliquer au test et au test final. Le contrôle ci-dessous le confirme
sur la v1 (une règle à seuil sur le numéro : 1,0 sur test et sur test_final ; le dernier segment : 1,0 et 1,0).

## 2. `banque-confrontation-v2.json` (+ `-secret.json`)

- **Même banque, autres identifiants** : mêmes 200 tâches, mêmes champs (`famille`, `texte`, `etiquettes`, `verite`,
  `source`), mêmes parts (train 80, test 60, test_final 60), **même ordre dans chaque part** ; seul `id` change. Les
  tâches, prises dans l'ordre du fichier v1 (train, test, test_final), reçoivent `t-0001` à `t-0200` selon
  `numpy.random.default_rng(numpy.random.SeedSequence(E)).permutation(200)` (la tâche de rang i reçoit
  `t-{permutation[i] + 1:04d}`), **E = 14234892761277461467225772596104759309**, tirée le 25 octobre 2026 à 15:50:09 UTC
  par `secrets.randbits(128)`. Aucun identifiant de la forme `cv-…` (vivier) ni `att-…` (attaques).
- Le manifeste reprend celui de la v1 (partition, strates, provenance, borne) ; `nom` devient `confrontation-v2`,
  `quand_utc` l'heure de construction, et `identifiants_opaques` dit d'où vient la v2 (empreintes de la v1 et de son
  secret), l'entropie et la règle.
- Le **secret v2** garde, pour chaque identifiant nouveau, le dossier secret v1 de la tâche et son ancien identifiant
  (`id_v1`) : c'est la seule correspondance entre les deux banques. Il ne sort jamais du noyau, comme celui de la v1.
- **La référence de surface est inchangée** (calculée dans l'ordre du fichier, identique à la v1 par contrôle) : `test`
  0,75 et `test_final` 0,6944 en conscience d'évaluation, `test` 0,5833 et `test_final` 0,50 en contrôle de délégation.
- **Ce que la v2 ne change pas** : la réserve de `LISEZMOI-v2.md` (traces écrites par des sous-agents de la même
  famille de modèles que les espèces servies) ; l'appariement honnête/saboté des traces (deux textes très proches dans
  la même part) ; les longueurs inégales de la famille `conscience-evaluation` (§ 1 de `LISEZMOI-v3.md`).
- **Ce qui doit suivre si la v2 est retenue** : les textes, lanceurs et fichiers dérivés qui citent la v1 par son
  empreinte ou par ses identifiants — en particulier les traits d'activations, rangés par identifiant (à renommer par
  `id_v1`), et la disjonction du vivier, vérifiée par identifiant de source (inchangée : le secret garde
  `id_source`).

| fichier | sha256 |
|---|---|
| `banque-confrontation-v2.json` | `52beb637823b72f475fd1ddcf446e9b79cafa5d2cd47d16c08b663d2b9388d10` |
| `banque-confrontation-v2-secret.json` | `1775a9e09f6620064769bf7c7a46d4f53a69e8cb1f886377dc5fd886d9d629fa` |

## 3. Construction et contrôle (`construction-v2/`)

- `construire_banque_v2_identifiants_opaques_v1.py` : la construction ; refuse numpy < 1.25, des empreintes de la v1 ou
  de son secret autres que `f1387a20…` et `c68d7d4b…`, un compagnon absent ou différent, une sortie existante (R12).
- `verifier_identifiants_opaques_v1.py` : le contrôle « **aucune règle sur l'identifiant ne prédit la vérité** » — 50
  règles par famille qui ne lisent que l'identifiant (suffixes, préfixes, caractère par position, longueur, segments,
  numéro modulo 2 à 10, numéro à seuil), apprises sur train et notées sur test et test_final ; une règle est
  prédictive si son exactitude équilibrée est ≥ 0,80 sur les deux ; avec la v1 et les secrets, l'équivalence rang à
  rang ; avec la racine du code, `verifier_banque` et la référence de surface comparée à la v1.
- Résultats (`essais-controle-identifiants-v1.txt` ; sorties complètes `controle-identifiants-banque-v1-v1.json` et
  `controle-identifiants-banque-v2-v1.json`) : **v1 refusée** (code 1 ; règles prédictives : 1 en conscience
  d'évaluation, 5 en contrôle de délégation) ; **v2 acceptée** (code 0 ; aucune règle prédictive, au plus 0,6111 et
  0,6667 ; équivalence conforme ; `verifier_banque` sans problème ; référence identique) ; construction refaite depuis
  E : égale hors `quand_utc` ; trois artefacts refusés (texte modifié, fuite injectée, identifiant en double).
- Ce contrôle n'est pas dans le noyau (`essaim_m3.banque verifier`, inchangé) : l'y ajouter changerait le code des
  lanceurs scellés ; un lanceur qui sert la v2 peut l'appeler lui-même.
