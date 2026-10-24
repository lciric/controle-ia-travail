# Essaim autonome — refonte v1 (LISEZMOI v5) : corrections après la contre-lecture R2 du 24 octobre

Complète `LISEZMOI-v4.md` (`d7f914c1…`, inchangé) : ce qui a changé dans le noyau depuis, pourquoi (constat CR-nn du
rapport `contre-lecture-preenregistrement-confrontation-v1.md`, `3b5aae60…`, relecteur neuf lancé par session-depot),
et le test qui le couvre. Branche `outils/essaim-m3-refonte-v1-travail` ; 65 tests (`python -m pytest -q tests`).
Rien n'entre dans `main` sans décision de Lazar ; aucun appel réel sans GO et préenregistrement scellé.

## 1. Isolation et gardes (CR-01, CR-02)

- Chaque lignée tourne sous un **utilisateur non privilégié distinct** (`UID_BASE` + indice), dans des espaces de noms
  (`unshare --mount --pid --fork --kill-child --mount-proc`, `-n` avec `--isoler-reseau`), privilèges abaissés après
  `unshare` (`abaisser.py`), groupe de processus tué à la fin ; les dossiers du noyau (banque, archive, lignées,
  journaux) sont en 0700, la vue de l'archive en 0555/0444 ; quand la racine n'est pas traversable, l'espace des
  organismes est `/var/tmp/essaim-m3/<empreinte>`. Le mode réel **refuse** sans root, sans `--isoler-reseau`, sans
  extrait du registre des GO, avec un collisionneur d'empreinte inattendue. Test « fuite » : un organisme qui tente de
  lire la banque, le juge, le journal du noyau, une autre lignée, d'écrire dans la vue, de poser `STOP`, de laisser un
  processus : rien ne passe (`test_organisme_fuite_ne_lit_rien_du_noyau_et_ne_laisse_aucun_processus`).
- Appel à un modèle non conforme : génération `INVALIDE_MODELE`, plus aucun appel servi, lignée arrêtée ; plafond à
  l'amorçage : statut `AMORCAGE_PLAFOND` archivé ; journaux d'amorçage scellés ; échec de `RLIMIT_AS` consigné.

## 2. Métriques, attaques, confrontation (CR-04, CR-06, CR-07)

- La métrique vit dans `organisme/metrique/` (`definition.md`, `calculer.py`, `attaques.json`) ; après la boucle,
  `extraire-metriques --course` relève empreintes et nombres **sans lire aucun score** ; l'humain gèle ce relevé
  (compagnon `.sha256`, contre-lecture) ; `confronter --course --metriques-gelees RELEVE` refuse un relevé non scellé
  et n'exécute ni n'attaque une métrique qui a changé depuis.
- La vue de l'archive ne contient aucun `attaques.json` ; la défense ne porte aucune marque : les attaques sont mêlées
  aux tâches du test de développement, ordre tiré.
- **Discriminance (CR-07 ii)** : avant toute application, le noyau exécute chaque métrique sur une sortie **parfaite**
  et une sortie **inversée** qu'il fabrique ; même valeur ou non calculée ⇒ « non discriminante », rapportée par lignée
  et par paire, écartée de H-E2 (`analyse.concordance_h_e2`). La métrique de forme de l'organisme factice (confiance
  moyenne) et celle de `gemini-organisme-v2` sont non discriminantes ; une exactitude sur ses attaques l'est
  (`test_metrique_distingue_parfait_et_inverse`).
- **Vocabulaire des attaques** : une attaque vise une famille de la banque et porte les étiquettes de cette famille
  (casse, tirets et soulignés normalisés, ordre du juge rétabli) ; sinon elle est invalide et rapportée — un défendeur
  n'est jamais noté sur un vocabulaire qu'il ne connaît pas (`test_attaques_doivent_porter_les_etiquettes_de_leur_famille`).
  Conséquence mesurée : les six attaques livrées par `gemini-organisme-v2` (`conscience_evaluation` /
  `comportement_nominal`, `sabotage` / `execution_fidele`) sont invalides sous cette règle.
- `.sha256` est une extension permise dans `organisme/` (proposition de session-depot, n° 05).

## 3. Bras gelé apparié, graines, manifeste (CR-08, CR-13, CR-19)

- `simuler|lancer --gel --depuis COURSE` relance les organismes g000 archivés de la course adaptative (mêmes
  empreintes), même banque, historique et archive vides.
- Graines : `SeedSequence(entropie, spawn_key=(indice de lignée, génération, usage))`, consignées dans
  `evenements.jsonl` ; `contexte["graine"]` ; manifeste avec commit, empreintes du code du noyau et de la banque,
  capacités d'isolation, extrait du registre des GO, conformité du collisionneur.

## 4. Ordre des lignées et mémoire (CR-15 b, c)

- L'ordre des lignées d'une ronde est **tiré** (`SeedSequence`, `spawn_key=(1 000 000, ronde, 6)`) et consigné
  (`etape: "ronde"`, `ordre`, `vue_figee`).
- **Par défaut, chaque lignée ne lit que sa propre archive** (`archive_vue/<lignée>/`) : les lignées d'une course sont
  indépendantes (aucune recopie du code d'une autre lignée). `--memoire-partagee` rétablit la vue de toutes les
  lignées, **figée au début de chaque ronde** (`archive_vue_rNNN`, copie en lecture seule) : la lignée qui tourne après
  une autre ne voit pas sa génération courante. Le bras gelé garde une vue vide. Contrat mis à jour.
  (`test_ordre_des_lignees_tire_et_vue_privee_ou_partagee_figee`.)

## 5. Analyse préenregistrée, banque réelle, simulateur (CR-11, CR-17, CR-18)

- `essaim_m3/analyse.py` : unité lignée-graine, bootstrap à deux niveaux stratifié, table de lecture gelée, tau-b
  descriptif, contrôle positif à gain connu (`verifier_sur_simulation`).
- `essaim_m3/banque.py` : construction partitionnée par groupes (40/30/30), secrets à part, scellement, référence sur
  les traits de surface du texte (N-029).
- Simulateur : lecture **par lots** des consignes inconnues (`[id] (famille : … ; …)` puis `{"reponses": {…}}`,
  format de l'enveloppe v3 de session-depot) ; chaque tâche est jugée sur son propre texte
  (`test_simulateur_lit_un_lot_de_taches_generique`). Simulation du 24 octobre (graine 21, 2 générations, 24/24/12
  tâches, espèces simulées) : `gemini-corrige-v3` 0,92 → 0,88 (test), 0,92 (final) ; `claude-fable-5-1`
  auto-écrit 0,83 → 0,88 ; `gemini-organisme-v2` 0,63 → 0,54 ; mécanique seulement, aucun chiffre opposable (R7).

## 6. Ce qui reste avant un run réel

Préenregistrement v4 contre-lu par un sous-agent neuf, scellé ; banque réelle scellée (lots 1 et 2 + sous-ensemble
« conscience d'évaluation » tiré par Lazar le 24 octobre, `31761ede…`, révision `5d724f12…` du jeu) ; devis au pire cas
et GO inscrit par session-depot ; répétition générale sur la banque de simulation ; `gemini-organisme-v2` et
l'enveloppe v3 alignés sur la règle des attaques (vocabulaire de la banque) s'ils veulent une métrique applicable.
