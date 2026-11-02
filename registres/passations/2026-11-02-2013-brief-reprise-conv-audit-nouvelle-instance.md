# Brief de reprise — instance neuve de conv-audit, sur un autre compte — 2 novembre 2026, rédaction commencée à 20:13 UTC (21:13 Paris ; heure relevée par `date -u` ; heure de scellement au compagnon `.sha256` et au commit)

**Ce brief fait foi pour l'exécution.** Il remplace celui du matin (`2026-11-02-0605-brief-reprise-conv-audit-nouvelle-instance.md`, archivé sans modification ; sa copie est aussi à la racine de l'ancienne machine). Lis-le en entier avant toute action. Ensuite :
- l'état vivant, `registres/etat.md` ;
- les registres `registres/decisions.md` (jusqu'à **R-1287** ; ta première ligne sera **R-1288**) et `registres/go.md` (jusqu'à **GO-2026-11-02-32**) ;
- la passation courte `registres/passations/2026-11-02-2013.md` ;
- la passation de session-depot, `registres/passations/2026-11-02-2006.md` sur `main` (commit `1c40dafc`, sha256 `3aad52dd…`).

En cas d'écart entre ce brief et un autre document, ce brief prime et l'écart se signale à Lazar.

**Pourquoi ce transfert.** Lazar change de compte, ce soir. L'ancienne session s'est arrêtée parce que les crédits d'usage étaient épuisés : un sous-agent a été coupé à 20:04 UTC pour cette raison. Session-depot change de compte en même temps (son n° 292). Tout vit dans deux dépôts GitHub ; rien ne vit dans la mémoire d'une conversation. Trois choses ne passent pas d'un compte à l'autre (§ 9) :
- les tâches planifiées ;
- le bloc-notes de l'ancienne session (sa partie utile est archivée dans le dépôt) ;
- les sous-agents.

---

## 0. Messages à coller par Lazar

### 0.1 Une seule instance (recommandé)
> Tu reprends le rôle de **conv-audit** dans mon programme de contrôle de l'IA (je suis Lazar, le directeur). L'instance précédente s'est arrêtée le 2 novembre 2026 vers 20:30 UTC, faute de crédits. Tout est sur le dépôt privé GitHub `lciric/controle-ia-travail`, branche `canal/conv-audit-n04`, et sur le dépôt public `lciric/ideation-organism`, branche `main`. Ajoute les deux dépôts à ta session (accès en écriture). Clone le privé **sans récupérer les refs `donnees/*`** (brief § 2) et le public normalement. Lis dans cet ordre : `CLAUDE.md`, puis `registres/passations/2026-11-02-2013-brief-reprise-conv-audit-nouvelle-instance.md` (il prime), puis `registres/passations/2026-11-02-2013.md` et `registres/etat.md`. Fais la routine de reprise (§ 3) et reprends exactement à la « prochaine action » (§ 4). Mène en parallèle, par sous-agents, la candidature Pivotal (§ 5), l'organisme d'idéation (§ 6) et le programme de contrôle (§ 7). Français, tutoiement, presque aucun sigle (développe chaque code) ; verdict d'abord ; aucune heure écrite sans `date -u`. Quand je reformule un texte, garde mes mots exacts, corrige seulement le fond et dis chaque correction en une ligne.

### 0.2 Deux instances (si Lazar préfère séparer la candidature)
Coller 0.1 dans chacune, en ajoutant « **Tu tiens la candidature Pivotal seule** » (§ 5) ou « **Tu tiens l'idéation et le contrôle** » (§ 6 et § 7).

Règles de cohabitation :
- Les deux poussent sur `canal/conv-audit-n04`, avec des commits par chemins nommés (`git commit -- chemins`) et un `git pull --rebase origin canal/conv-audit-n04` avant chaque poussée.
- Seule l'instance « idéation et contrôle » tient le canal avec session-depot et le registre des GO.
- Les lignes `R-` se prennent dans l'ordre d'arrivée, après un `git pull --rebase`.

---

## 1. Qui tu es (régime, non négociable)

Tu es **conv-audit**, la lignée d'audit et de conception.

**Ce que tu ne fais jamais :**
- écrire sur `main` du dépôt privé (seule **session-depot** y écrit, et seule sa **fille**, porteuse des clés, lance ce qui dépense) ;
- dépenser quoi que ce soit sans devis et GO (`registres/go.md`, 8 colonnes) ;
- lire, afficher ou demander une clé ;
- **pousser vers `lciric/controle-ia`**.

**Avant chaque poussée**, cette commande doit rendre 0 :
`git diff --cached | grep -cE 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE KEY|sk-proj-'`
Les canaris `…FACTICE…` et `…FAUX…` des essais de caviardage sont attendus.

**Règles en plus de R1 à R14 :**
- **R-486** : un contenu arrêté par un classifieur ne se rejoue pas, même reformulé.
- **R-743** : au troisième arrêt sur un même sujet, il revient à Lazar.
- **R-1111** : toute heure écrite se relève par `date -u`. L'ancienne instance a écrit trois fois une heure d'en-tête avant de la relever ; elles ont été corrigées.
- Contre-lecture (R2) et verdict (R13) par un sous-agent **neuf**, qui n'a pas écrit le texte, avec la liste exacte des fichiers à lire.
- Sous-agents : aucun commit, aucun `.sha256`, aucun fichier existant modifié sauf ceux qu'on leur nomme, rien sous `donnees/`, aucun `git fetch`, aucun appel de réseau ni de modèle, `nice -n 10`.

**Commits :**
- `-c user.name="Lazar Ciric" -c user.email="lciric@ens-paris-saclay.fr"`, avec les lignes d'attribution que donne ton environnement ;
- **pousser après chaque rendu** : une limite d'usage peut couper d'un coup, et c'est ce qui vient d'arriver ;
- dans le dépôt public, messages de commit en anglais ; tout changement du README recopie son empreinte dans `MANIFEST.md`.

**Interdits de lecture :**
- **Branches `calcul/…`** : interdites jusqu'au mot de Lazar.
- **Refs `donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*`** : ce sont nos tests à l'aveugle, les voir les détruit. Les autres `donnees/*` ne se récupèrent pas non plus.
- **`bras-attaque-v1/`** : ne s'ouvre pas au-delà de son LISEZMOI ; les textes II et III ne s'ouvrent pas.
- Après toute récupération : `git for-each-ref refs/remotes | grep -c donnees` doit valoir **0**.

**Règle de Lazar sur ses reformulations** (permanente) : garder ses mots exacts, corriger seulement le fond, dire chaque correction en une ligne. Exceptions :
- s'il demande « bien rédigée », on rédige proprement, à contenu égal ;
- pour **Heimersheim Q1**, la consigne du mentor est « 100% human-written » : on vérifie les faits sans réécrire.

**Fichier parasite connu** : `/a-blanc-essai-kimi-v3c.sortie.txt` (135 octets, à la racine de l'ancienne machine), laissé par un sous-agent. Il n'existe pas sur la nouvelle machine ; rien à faire.

---

## 2. Installation (une fois)

### 2.1 Dépôt privé
```
git clone --no-checkout --single-branch --branch canal/conv-audit-n04 https://github.com/lciric/controle-ia-travail.git controle-ia-travail
cd controle-ia-travail && git checkout canal/conv-audit-n04
```
**Quarantaine** : jamais de `git fetch` sans refspec. On récupère seulement par refspecs explicites, par exemple :
`git fetch origin +refs/heads/canal/session-depot-reprise-n119:refs/remotes/origin/canal/session-depot-reprise-n119`

Branches utiles :
- `main` (session-depot) ;
- `canal/session-depot-reprise-n119` (dernière, n° 292) ;
- `prep/r1-relance-v3` (tête `145da951`) ;
- `prep/r1-complement-v1-instantane-2005` (`3ef8e816`) ;
- `prep/r1-relance-addendum-v1` (`c2a8b6e1`).

Pour lister les branches : `git ls-remote origin | grep -v donnees`.

### 2.2 Dépôt public
`git clone https://github.com/lciric/ideation-organism.git`, branche `main`, tête **`53aef4a`** au moment de ce brief.

### 2.3 Environnement
- Privé : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src`.
- Public : Python 3.13, numpy, scipy ; les essais disent ce qui manque. Le bac réel (`bwrap`) sert aux tests de mort ; certains essais se sautent avec `POLE_ESSAI_BAC_REEL_NON_JOUE=1`, et `TMPDIR=/tmp` est requis pour le bac.

### 2.4 Bloc-notes archivé
L'archive est `brouillons/passation-conv-audit-2026-11-02-soir/travail-interrompu/bloc-notes-selection-2026-11-02-soir.tar.gz` (sélection de 351 fichiers). On la décompresse **dans un dossier neuf et vide**, et on n'y exécute rien depuis l'intérieur.

---

## 3. Routine de reprise (R14)
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt`, puis `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`. Il y a 193 échecs anciens connus (`brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/ecart-etape-G-verifier-arbre-v1.md`) ; un échec **nouveau** est une réserve.
2. `python -m pytest -q` sur le dépôt privé.
3. Défauts échus : rien n'échoit avant le 4 novembre. Exception : les deux nœuds d'aujourd'hui (§ 8) ont un défaut sous 48 heures, à compter de leur envoi à Lazar, qui reste à faire.
4. Instances de calcul : **aucune** chez conv-audit. Chez session-depot, aucune instance Vast à 20:05 UTC (n° 292). Le **collisionneur** tourne chez la fille depuis 19:26:20 UTC ; ce sont des appels de modèles, pas une instance.
5. Relève du canal (§ 9.1).

---

## 4. Prochaine action (reprends exactement ici)

1. **Routine** (§ 3).
2. **Tâches planifiées neuves sur ton compte** (§ 9.1) :
   - ta boîte « CANAL · boîte conv-audit », liée à ta session, avec la même consigne et l'échéance du 30 novembre 2026 à 12:00 UTC ;
   - une relève horaire.
3. **Canal.** Lis le n° 293 de la nouvelle instance de session-depot s'il est arrivé. Réponds par ton **n° 389**, avec l'identifiant de ta boîte ; le n° 388, celui de l'ancienne instance, annonce le transfert. Plus aucune sonnette n'est possible vers l'ancien compte.
4. **Candidature Pivotal (§ 5)** : c'est le plus urgent si Lazar remplit le formulaire ce soir. Applique ses reformulations à mesure qu'elles arrivent, selon sa règle. Quand il dit que c'est fini :
   - PDF des questions-réponses **v10** ;
   - LISEZMOI **v69**, avec les versions finales.
5. **En parallèle, sans dépense :**
   - (a) A1-v3 : appliquer les 42 couples ; le nœud B1 va à Lazar (§ 8.1) ;
   - (b) tour fermé : appliquer les couples T101 à T112, et demander à session-depot la configuration v3 et la vérification A.6 bis (§ 6.4) ;
   - (c) nul v9 : courte vérification neuve du changement de description et des essais B1, puis scellement du brouillon 4 et validation hors ligne (§ 6.3). **À lancer au plus tard le 3 novembre** : la Q1 de Kirchner v41 écrit « the test runs tomorrow » ;
   - (d) juges v2 : relancer le développeur coupé (§ 6.5) ;
   - (e) contrôle : concordances de l'addendum v3 et du complément fusionné (§ 7), puis P3-bis et T0.6 (§ 7.4).
6. Prévenir Lazar seulement pour : prononcé, réserve, divergence, demande de GO ou de décision (§ 8), dépense.

---

## 5. Candidature Pivotal (mentors du premier trimestre 2027) — état exact

### 5.1 Où sont les pièces
Tout est dans `brouillons/candidature-pivotal-v16/`. Le dernier LISEZMOI figé, `LISEZMOI-envoi-final-v68.md` (18:54 UTC), est **dépassé pour les mentors** : la liste ci-dessous prime.

| Pièce | Version à envoyer | Note |
|---|---|---|
| Formulaire commun, sections 1 à 10 | `reponses-formulaire-v18.md` | inchangé depuis la v68 |
| CV | `Lazar_Ciric_CV_2026-11-02_v17_universel.pdf` | variantes v17 `persona-sycophancie`, `interpretabilite`, `controle-recherche-automatisee` ; source `cv-v17/construire_cv_v17.py` ; deux pages |
| Writing sample 1 | `Lazar_Ciric_writing_sample_1_essay_v1.pdf` | — |
| Writing sample 2 | `Lazar_Ciric_writing_sample_2_control-proposal-extract_v21.pdf` | — |
| Mémo de carrière | `Lazar_Ciric_career_memo_2026-11-02_v6.pdf` | — |
| **Ibrahim** | `mentors/mentor-1-ibrahim-v28.md` | Q2 = texte de Lazar de la v27, avec six corrections ; Q1 avec la phrase des deux intensités |
| **Kirchner** | `mentors/mentor-2-kirchner-v41.md` | voir ci-dessous |
| **Heimersheim** | `mentors/mentor-3-heimersheim-v25.md` | paragraphe « Evidence that would satisfy me » de Lazar ; Q1 sous la règle « 100% human-written » |
| **Scheurer** | `mentors/mentor-4-scheurer-v16.md` | passages de Lazar, trois corrections |
| **Colognese et Ward** | `mentors/mentor-5-colognese-ward-v17.md` | phrase de Lazar sur la crainte |
| **Jang et Feng** | `mentors/mentor-6-jang-feng-v22.md` | — |
| Tilli | `mentors/mentor-7-tilli-v10.md` | — |
| Jain et Jacob | `mentors/mentor-8-jain-jacob-v10.md` | — |
| PDF des questions-réponses | `Lazar_Ciric_Pivotal_questions-reponses-mentors_v9.pdf` | **dépassé** : à rebâtir en v10 (`construire-questions-reponses-v10.py`, copie de la v9 pointée sur les versions ci-dessus) quand Lazar aura fini |

**Kirchner v41 en détail :**
- Q1 est la v41 : la dernière reformulation de Lazar (20:15 UTC), corrigée sur le fond (16 corrections, 463 mots). Versions antérieures au choix de Lazar :
  - la v40, « bien rédigée », 423 mots ;
  - la v39, ses mots précédents corrigés, 487 mots.
- **Engagement pris dans la Q1 v41** : « the test runs tomorrow ». La validation du nul v9 (§ 6.3) doit donc **partir le 3 novembre** (processeur, sans dépense). « The fix ran its preregistered validation check today » n'est vrai que si Lazar soumet le 2 novembre.
- Q2 vient de la v37 (537 mots) : « Underrated / Overrated », expérience 1 (martingale de test contre le nul « référence + toutes les méthodes acceptées », Ville, Ladder en référence), réfutations.
- L'historique complet des corrections est dans l'en-tête de chaque version : le fichier v41 liste v41 → v13.
- Deux réserves sont déjà dites à Lazar :
  - la validation du juge v9 n'a pas commencé, d'où « runs next » ;
  - le code est écrit par des instances de Claude, donc « scripted », et non « handmade ».

**Liens publics cités :**
- R1 : `https://github.com/lciric/ideation-organism/tree/main/resultats/controle-r1-blanche-noire` ;
- A1 : `…/resultats/attaque-goodhart-v2` ;
- sycophancie : `github.com/lciric/sycophancy-psychophysical-law`, Zenodo v2026.11.4, DOI 10.5281/zenodo.23892810.

### 5.2 Ce qui attend
1. **Reformulations de Lazar**, mentor par mentor. Il a dit « même chose pour les autres réponses » (19:46 UTC). Les recommandations du lecteur neuf, qu'il a reçues, sont dans `brouillons/passation-conv-audit-2026-11-02-soir/rapports-lecteurs-pivotal/lecteur-neuf-cinq-mentors-rapport.md`. Changements minimaux proposés :
   - **Ibrahim** : deux personas entraînées puis le **même** renforcement à récompenses vérifiables, sinon « shape or get overwritten » n'est pas tranché ;
   - **Heimersheim** : la question 2 renvoie à ses travaux sur les plateaux ; en question 1, que seul Lazar écrit, « plateau » devient « saturates » ;
   - **Scheurer** : un énoncé de pente pour la tendance 1, et la phrase « All code was written by AI agents following guidelines I created. » ;
   - **Colognese et Ward** : « never includes the hack » devient « almost never mentions the hack » (93 % d'après leur billet) ;
   - **Jang et Feng** : une accroche « greffe et causalité » à la place de « superpowers… toolbelt », et la lecture exacte d'arXiv 2609.36490 (le contexte seul déplace les activations dans le bon sens mais pas assez ; l'évasion efficace vient d'un adaptateur de rang 1).
   Le rapport du lecteur sur la Q2 de Kirchner est dans le même dossier ; ses trois ajouts sont acceptés depuis la v33.
2. **Fond à surveiller dans toute réponse :**
   - **Sur R6** : la loi d'attraction ne vaut pas pour toutes les familles. Elle tient pour Llama ; Qwen montre un déplacement uniforme ; Gemma ne bouge que sous la critique ; chez Mistral, le régime change avec la formulation. Pour Llama, sous la critique, le gain ne croît pas avec l'intensité ; seul Llama refuse.
   - **Sur R7** : rien n'est publié (préenregistré, archivé, en cours chez l'instance sycophancie).
   - **Sur « 27 scripted cheaters »** : ce n'est pas un compte. Le banc v7 numérote T01 à T27 avec 19 codes ; le banc v8 joue 18 lignes sur 15 scénarios.
   - **Sur les juges modèles de langage** : ils sont « maxed out », ils ne trichent pas.
   - **Sur les données réelles** : aucune loi n'y a été acceptée, et on ne sait pas s'il y en a.
3. **Correction publique datée de « 27 scripted cheaters »**, dans le README de `ideation-organism` et la page d'A1. Elle reste à faire, sous le GO de publication des pages (GO-2026-11-02-09 et -10, même objet ; à confirmer d'un mot par Lazar si doute).
4. Quand Lazar a fini : PDF v10, LISEZMOI v69, zip `candidature-pivotal-v17.zip` (nom neuf), puis une ligne R-.
5. L'échéance de soumission est celle que Lazar donne ; ne pas la supposer.

---

## 6. Organisme d'idéation (dépôt public `ideation-organism`) — état exact par chantier

**Règle d'ordre** : le relais Argon (port 8805) est **monofil**. A1-v3, puis A1-v4, ne tournent **jamais en même temps** que tout autre usage d'Argon. Les juges v2 et le tour fermé utilisent aussi Argon : on les met en série.

### 6.1 A1, attaque de Goodhart contre le juge v8 (fait)
- Verdict scellé et publié : W1 non jugeable (instrument en défaut, plafond d'étape commun) ; W2 brèche dans la classe que le juge déclare non couverte, portée par Argon.
- Page : `resultats/attaque-goodhart-v2/` ; décision GO-2026-11-02-16.

### 6.2 A1-v3, reprise propre (GO-2026-11-02-21, calcul, 400 USD)
- **Plan** : Argon seul, un fil, 24 cartes par monde, `relais_perdu_h: aucun`, 72 h, ordre des issues 2, 6, 1, 3, 4, 5.
- **Devis** : maximum 190,46 USD ; durée haute attendue 25,12 h, pire 35,78 h.
- **Code** : v3 à `e58cfec` (cœur `pole/attaque_goodhart_v3.py` `b821bdb7…`, lanceur `demonstrations/attaque_goodhart_v3.py` `ff8aa180…`).
- **Texte** : brouillon 3 `prereg/preenregistrement-attaque-goodhart-v3-brouillon3.md` (`e2c28eed…`, commit `08b1f17`).
- **Contre-lecture neuve rendue** (commit `53aef4a`) :
  - `prereg/contre-lecture-preenregistrement-attaque-goodhart-v3-v1.md` (`01a2041a…`) ;
  - `prereg/couples-contre-lecture-attaque-goodhart-v3-v1.json` (`e5f669e4…`, 42 couples ; appliqués à la suite, ils donnent `5507536934dfb733…`, accepté par `lire_preenregistrement`).
- **Verdict de la contre-lecture** : scellable après les 42 couples, **si le prix du bloquant B1 est accepté par écrit** (§ 8.1). Rapport complet : `brouillons/passation-conv-audit-2026-11-02-soir/rapports-sous-agents/contre-lecture-a1-v3-brouillon3-rapport.md`.
- **Importants** :
  - I1 : le code 5 compte aussi les refus du proposeur ;
  - I2 : des tentatives perdues dans les suites jouées réduisent la pression ;
  - I3 : le délai de l'orchestrateur est de 1 800 s, pas 1 750 ;
  - I4 : la ligne GO-21 cite `d15f489`, alors que le texte gèle `e58cfec` ; une ligne de précision est à inscrire avant scellement ;
  - I5 : une seconde course n'est prévue qu'après un arrêt ;
  - I6 : des écarts manquent en 0.4 ;
  - I7 : trois vérifications du relais avant la course (plafond propre, taille de requête face aux 90 363 octets, rendu sur erreur de quota) — à demander à session-depot.
- **M10** (question) : R-1276 demande des témoins plantés dans chaque course ; A1-v3 n'a pas de témoin négatif planté. Il faut l'en dispenser par écrit, ou le coder.
- **Suite** :
  1. décision B1 ;
  2. couples ;
  3. ligne de précision du GO (I4) ;
  4. texte final `prereg/preenregistrement-attaque-goodhart-v3-v1.md` ;
  5. scellement, commit, poussée ;
  6. **commande exacte** avec d'abord `--verifier-seulement` (code 0), chemin hors clone `/home/user/hors-clone-a1-v3/` ;
  7. demande de course à session-depot, lancée par la fille sur le go permanent (R-1059 chez lui, n° 288) ;
  8. sortie scellée avant lecture ;
  9. audit, puis verdict d'un lecteur neuf ;
  10. page `resultats/attaque-goodhart-v3/`.
- **Vérificateur du lanceur `e58cfec` chez session-depot** : non rendu, à relancer par sa nouvelle instance (n° 292).
- **Réplication par Kimi** : GO-2026-11-02-25 (150 USD), après A1-v3.

### 6.3 Nul v9 (juge corrigé) : validation hors ligne, puis attaque v4
- **Code** à `5e352ec`, puis `516feca` : `pole/nul_v9.py` `7ae450df…`, essais `essais/test_nul_v9.py` `d42a50eb…`, mutations `essais/mutations_nul_v9.py` `f004dba6…`, banc `demonstrations/banc_tricheurs_v9.py` `7e4bff59…` (mode décisif 48 h).
- **Texte** : `prereg/preenregistrement-validation-nul-v9-brouillon4.md` (`02dfbb7b…`, commit `516feca`, aucun jeton). Il lève B1 (mode décisif essayé sur un cas sain et deux artefacts), I1 à I7 et 23 couples de la contre-lecture `41f4f56d…` (`87f98fb`).
- **Essais** (rejoués par l'ancienne instance à 20:05 UTC) : 64 réussis et 108 sous-essais (nul v9 et attaque v4 ensemble). Banc du développeur : 43 mutations sur 43 tuées.
- **Non contre-lu** : le changement de `nul_v9.py` porte sur la **description seulement** (`NON_COUVERT_V9` réduit aux 4 trous ; `HORS_DU_NUL_PAR_CHOIX_V9`, `HORS_DU_NUL_PAR_NATURE_V9`, `RESERVES_V9`, `description_publique()` ; aucun calcul changé, arbres syntaxiques comparés). Il faut une **courte vérification neuve** de ce changement et des essais B1 avant de sceller.
- **Suite** :
  1. vérification courte ;
  2. scellement du brouillon 4 sous le nom final `…-v1.md` ;
  3. commit ;
  4. **validation sur processeur chez toi**, sans dépense (31 lignes, 1 000 répétitions, garde de 48 h ; graines de l'empreinte du texte) ;
  5. sortie scellée ;
  6. verdict d'un lecteur neuf ;
  7. page `resultats/nul-v9-validation/`.
- **Attaque v4** (GO-2026-11-02-22, 200 USD) :
  - code `pole/attaque_goodhart_v4.py` `0077a647…`, essais `350423da…`, mutations `2dd378f6…` (33 sur 33), rapport `504577e6…` ;
  - texte `prereg/preenregistrement-attaque-goodhart-v4-brouillon2.md` (`7be8589e…`), avec deux jetons à lever : empreinte de configuration, empreintes du code au commit ;
  - les courses à blanc A, B et C ont tourné avec l'ancienne description (dit au rapport) ;
  - suite : contre-lecture neuve, scellement, course **après** A1-v3, jamais en même temps.

### 6.4 Tour fermé, étage 1 (GO-2026-11-02-23, calcul, 50 USD : Kimi 44, Argon 6)
- **Code** v63 à `a12713a` : 87 essais, 72 mutations sur 72.
- **Texte** : `prereg/preenregistrement-tour-ferme-v1-brouillon5.md` (`c81aa6ef…`), un seul marqueur `<<CASE_CONFIGURATION_V3>>`. L'annexe A, l. 745-871, donne chaque clé de configuration.
- **Contre-lecture courte neuve rendue** (commit `171b856`) :
  - `prereg/contre-lecture-courte-preenregistrement-tour-ferme-v5.md` (`3b525f9e…`) ;
  - `prereg/couples-contre-lecture-tour-ferme-v5.json` (`40bb0d17…`, couples T101 à T112, texte seulement).
  - Verdict : **scellable après les couples**, plus la case de configuration ; aucun bloquant.
- **I32** : les commandes des relais n'ont jamais joué les rôles de l'étage ni ses plafonds de session (le vérificateur reçoit 0,1 USD). L'annexe A.6 bis (couples T111 et T112) demande à session-depot de vérifier ses deux commandes **en lisant leur code**, sans appel. Points précis (dans le rapport privé, pas dans le fichier public) :
  - la configuration du 1er novembre (`4ae5a1e0`) met déjà Kimi et Argon en `commande_externe`, avec `plafonds_session.proposeur` = 1,8 ;
  - options de sortie selon le rôle : `--max-sortie-court` 16 000 pour Kimi et 4 000 pour Argon ; `--sortie-min-jetons` 4 096 et 1 000 ; `--delai-s` 1 750.
- **Mineurs** :
  - 39 et 40 : effet de la borne par carte ; seuil de la garde de 24 h ;
  - 41 : arrêt pour dépense vers 55 cartes testées, asymétrie à déclarer ;
  - 42 : la ligne GO-23 cite `af92034` et « ≈ 3,3 à 12 USD », alors que le code gelé est `a12713a` et le devis va jusqu'à ≈ 23,6 USD (26,1 si chaque carte atteint sa borne) — une ligne de précision du directeur suffit ;
  - 43, 44 : sans effet, ou phrases qui deviennent fausses au scellement.
  - Rapport : `…/rapports-sous-agents/contre-lecture-courte-tour-ferme-b5-rapport.md`.
- **Décision pour Lazar** : durée 24 h → 72 h (§ 8.2).
- **Configuration v3** : pas encore écrite par session-depot (n° 292 : sa nouvelle instance la fera d'après l'annexe A). Contraintes :
  - Kimi par la commande externe, rôles `proposeur_ideation` et `experimentateur_test` ;
  - `plafonds_session.proposeur` ≥ 0,50 ;
  - parts 44 et 6 ;
  - `budget.plafond_usd` = 50 ;
  - `TMPDIR=/tmp` ;
  - `{REGISTRE}` et `--plafond-cumule-usd` dans les commandes.
- **Suite** :
  1. couples ;
  2. empreinte de la configuration v3, qui lève la case ;
  3. scellement ;
  4. commande exacte (`--verifier-seulement`) ;
  5. course ;
  6. verdict ;
  7. page `resultats/tour-ferme-etage-1/`.

### 6.5 Juges modèles de langage v2 (GO-2026-11-02-32, calcul, 60 USD ; la ligne GO-24 n'est pas utilisée)
- **Protocole** : comparaisons par paires à l'aveugle dans les deux ordres, force de Bradley-Terry avec terme de position, ancres de qualité connue, au plus un quart « notable », preuves citées vérifiées. Juges **Argon et Astra** (Kimi exclu), **15 bons et 15 mauvais témoins plantés par classe**, bras « ancien protocole sans dossier », garde de 48 h ; parts 24 USD Argon et 36 USD Astra.
- **Code et brouillon 1** à `c15a073`. La contre-lecture `1dc3c194…` (`87f98fb`) est **non scellable** :
  - B1 : témoins séparables sans tables ;
  - B2 : statuts du relais lus comme réponses ;
  - B6 : choix des juges ;
  - B7 : sept gardes sans essai sur un artefact ;
  - puissance de 0,73 à 10 contre 10.
- **Le développeur du brouillon 2 a été coupé à 20:04 UTC** (crédits épuisés). Son travail partiel sur `pole/juges_idees_v2.py` (+562 −109 lignes, **non commité**, non vérifié) est sauvé en `brouillons/passation-conv-audit-2026-11-02-soir/travail-interrompu/juges_idees_v2-partiel-sur-516feca.patch` (base : commit noté dans `juges_idees_v2-commit-de-base.txt`). Ses derniers mots : « Maintenant le plan (bras sans dossier), le compteur avec parts, les statuts du relais et le jeu des étapes. »
- **Suite** : relancer un développeur avec la consigne `…/prompts-sous-agents/juges-idees-v2-developpeur-brouillon2-prompt.md`, en lui donnant le patch (reprendre ou recommencer, à son jugement, en vérifiant tout) ; puis contre-lecture neuve des changements, scellement, course chez la fille (Astra : commande 8807 à éprouver), verdict, page `resultats/juges-idees-v2/`.

### 6.6 Collisionneur (GO-2026-11-02-31, 40 USD)
- Lancé chez la fille à 19:26:20 UTC sur le prompt de Lazar (`brouillons/canal-reprise-releve-v1/envois/conv-audit/PROMPT_brainstorm_instance_neuve_2026-11-02_v1.md`, `6a12dc71…`).
- Version `collisionneur_v9.py`, B = `claude-opus-5-5`, 15 cellules ; devis 17 à 20 USD attendus, 36,33 au pire.
- La sortie sera scellée et copiée sur le canal par session-depot ; **à transmettre à Lazar** dès réception, sans lecture sélective.

### 6.7 État des résultats pour Pivotal
Le tableau est dans `brouillons/candidature-pivotal-v16/etat-resultats-pivotal-v1.md` (18:48 UTC), à mettre à jour à chaque verdict. Il ne contient aucun chiffre sans verdict scellé.

---

## 7. Programme de contrôle (dépôt privé) — état exact

### 7.1 Rejeu à graine (fait)
- Verdict scellé `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md` (`64fab1a5…`) : 7 épisodes sur 7 résolus, table de tokenisation v3 complète (`ead8a668…`).
- Validation : 54 sur 147 seulement, « méthode non transposée », parce que le budget d'étape (2 400 s) a coupé.

### 7.2 Complément de validation (GO-2026-11-02-30, 40 USD ; GO-26 inutilisé)
- Il rejoue les 147 avec `combinaisons_max` 272, `duree_max_episode_s` 14 400 et `duree_max_s` 259 200 (gardes seulement).
- Texte fusionné chez session-depot, **non scellé** : instantané `prep/r1-complement-v1-instantane-2005` (`3ef8e816`), texte `98d5f043…`, configuration = notre brouillon 2 `1b6f943c…` (canonique `70b0b771…`).
- Notre brouillon 2 : `brouillons/preuves-mentors-v1/complement-validation-rejeu-v1/` (`41d5350e…`).
- Garde de dépense : alerte à Lazar à 30 USD, arrêt par identifiant à 39,5 USD.
- **Suite** : ta concordance (lecteur neuf, même méthode que `concordance-addendum-r1-v1.md`), scellement chez session-depot, course, réception scellée, verdict.

### 7.3 Relance de R1 sur la table v3 (GO-2026-11-02-27, 60 USD)
- Addendum v3, brouillon 1, sur `prep/r1-relance-v3` (`145da951`) : texte `prereg/R1-addendum-relance-v3.md` (`382ba627…`), configuration v5 `acad6253…` (canonique `1cfb7fba…`), 329 essais, pré-vol 22/22.
- **Réserve pour la fiche de réception** : le champ `tokenisation.addendum` vaut encore `prereg/R1-addendum-relance-v2.md` (E16).
- **Suite** : contre-lecture neuve chez session-depot, ta concordance, scellement, course, fiche de réception scellée avant récupération, lectures principale et secondaire (déjà scellées), verdicts, mise à jour de la page R1.
- Les branches `calcul/r1-r2-reel-v1` et `calcul/r4-dose-reel-v1` restent interdites sans le mot de Lazar.

### 7.4 P3-bis, témoin positif planté (GO-2026-11-02-29, 80 USD) et T0.6, organisme v0 et test croisé d'étiologie (GO-2026-11-02-28, 200 USD)
- Un sous-agent préparait les deux préenregistrements. Il tournait encore à 20:13 UTC ; sa consigne est `…/prompts-sous-agents/preparation-p3-bis-et-t06-prompt.md`.
- Ce qu'il a déjà écrit :
  - `brouillons/P3-bis-temoin-positif-v1/` (`puissance_p3_bis_v1.py`, `puissance-p3-bis-v1.txt`) ;
  - peut-être `brouillons/T0.6-organismes-v0-*.md`, plus anciens, à vérifier par date.
- La dernière passation courte dit s'il a rendu. Sinon, relance-le avec la même consigne, en lui donnant ce qui existe.
- **Suite** : contre-lectures neuves, scellement, courses chez la fille, verdicts.

### 7.5 Autres
- La lecture « par épisode » de R1-R2 (GO-2026-11-02-05) attend la relance de R1.
- Sycophancie :
  - R6 publié (dépôt public `lciric/sycophancy-psychophysical-law`, commits `9d2a280`, `ad64b72`, `73be119`) ;
  - R7 (déférence des moniteurs, sept Qwen2.5 de 0,5B à 72B) préenregistré, archivé, en cours chez **l'instance sycophancie**, qui n'est pas la nôtre. Ses résultats arrivent par Lazar (fichiers « POUR_INSTANCE_PIVOTAL… »).
- Porte G0 : au plus tard fin novembre, critères inchangés.

---

## 8. Décisions qui attendent Lazar (format : décision ; enjeu ; options ; recommandation ; défaut)

### 8.1 A1-v3, nœud B1
**Décision** : accepter par écrit que la garde du registre puisse arrêter la course avant 400 USD en cas de panne de l'interface.

**Enjeu** : environ 103 à 123 tentatives perdues en code 3, au pire cas (≈ 1,6 USD chacune), épuisent la marge. Ensuite tout est refusé en code 4, et la course finit avec des cases vides (issue 6).

**Options :**
- (a) accepter et déclarer, par les couples seuls ; la course part dès le scellement ;
- (b) code 3.1 qui attend aussi sur le code 3 et lit le refus de la garde comme un arrêt au plafond (quelques heures : code, essais, banc, brouillon 4, contre-lecture) ;
- (c) faire reprendre les erreurs passagères par le relais, chez session-depot.

**Recommandation du contre-lecteur, que je reprends** : (a), après la réponse de session-depot sur (c) ; (b) pour les courses suivantes. Confiance 0,6.

**Défaut sous 48 heures** : (a). Plus M10 : dispenser A1-v3 du témoin négatif planté, par écrit ; recommandé, puisque le témoin négatif de cette course est le bras sans retour.

### 8.2 Tour fermé, durée de garde
**Décision** : passer la garde de 24 h à 72 h.

**Enjeu** : la garde coupe toute la course si elle mord, et son seuil tombe à ≈ 81 s par session vers 60,7 cartes testées.

**Options :** (a) 72 h, sans coût en dollars, comme A1-v3 ; (b) garder 24 h.

**Recommandation** : (a), confiance moyenne. **Défaut** : (b).

### 8.3 Précisions du registre des GO (routine du directeur, à lui dire d'une ligne)
- GO-21 : code `e58cfec`, et non `d15f489`.
- GO-23 : code `a12713a` ; devis jusqu'à ≈ 23,6 USD.

### 8.4 Fille de session-depot (décision posée par session-depot, sa passation § 0.3)
La fille, porteuse des clés, reste sur l'ancien compte : la nouvelle instance de session-depot ne peut pas lui écrire. Option posée : relais à la main par Lazar, puis fille recréée sur le nouveau compte.

**Toutes les courses payantes de ce brief en dépendent.**

### 8.5 Candidature
- Version de la Q1 de Kirchner : v41 (ses derniers mots, corrigés), v40 (rédigée) ou v39.
- Reformulations des autres mentors.
- Correction publique de « 27 ».

---

## 9. Ce qui ne passe pas d'un compte à l'autre

### 9.1 Tâches planifiées de l'ancien compte
Elles sont inutilisables depuis le nouveau compte ; Lazar peut les retirer.
- Ma boîte `trig_01AmvKFA6aju3NNEpRYmTLGV`, liée à l'ancienne session.
- Ma relève `trig_01MV1Hd9CfQCGj8JjdhG9dzx` (20:50 UTC, une fois).
- La boîte de session-depot `trig_012ZGpoLpReu5m21DvFLUigd`, qui cessera de répondre à la fin de sa session.
- Sa relève `trig_01GSWjh4jdgFhUG8C869TGbU`.

**À faire à la reprise :**
1. Créer ta boîte « CANAL · boîte conv-audit » : une tâche liée à ta session, sans horaire propre, échéance 30 novembre 2026 12:00 UTC. Consigne : « si ce message arrive avant le 30 novembre, c'est une sonnette de session-depot : `date -u` ; lister ses branches par `git ls-remote origin | grep -v donnees | grep session-depot-reprise` ; récupérer la dernière par refspec explicite ; lire son dernier message ; vérifier son empreinte ; consigner (R-) ; répondre par le message suivant, scellé, committé, poussé ; ré-armer et dire le nouvel identifiant. Rien de `calcul/…` ni de `donnees/*` sans le mot de Lazar. »
2. Créer une relève horaire, ré-armée à chaque passage.
3. Donner l'identifiant de la boîte à session-depot par ton n° 389.

**Format du canal :**
- nos messages : `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-02_nNNN.md` + `.sha256` ;
- les siens : `session-depot_…_nNNN.md`, sur `canal/session-depot-reprise-nNNN` ;
- un message = écrit, scellé, committé, poussé, puis sonnette (si tu as son identifiant de boîte).

### 9.2 Bloc-notes de l'ancienne session (7,6 Go, perdu)
La sélection utile est archivée, scripts compris (§ 2.4) : `juges-v2`, `cl-juges-v2`, `validation-b4`, `attaque-v4`, `nul-v9`, `tour-ferme-clc5`, `contre-lecture-nul-v9`, `a1-v3-texte-b3`, scripts `go-*.py` et `pivotal-*.py`, messages `n2*.md`. Les sorties des contre-lecteurs sont citées par empreinte dans leurs rapports publics.

Le reste n'a pas de valeur pour la suite : copies d'arbres extraits, `concordance-rejeu-graine-b3` (4,6 Go, recalculable depuis la sortie du rejeu sur le canal), `copie-21a6e583`, `mesure`.

### 9.3 Sous-agents
- Rendus et committés :
  - contre-lecture A1-v3 (`53aef4a`) ;
  - contre-lecture tour fermé (`171b856`) ;
  - nul v9 brouillon 4 et attaque v4 brouillon 2 (`516feca`) ;
  - lecteurs Pivotal (rapports dans `…/rapports-lecteurs-pivotal/`).
- **Coupé** : développeur des juges v2 (§ 6.5).
- **En cours au moment du brief** : préparation P3-bis et T0.6 (§ 7.4).
- Toutes les consignes sont dans `brouillons/passation-conv-audit-2026-11-02-soir/prompts-sous-agents/`.

---

## 10. GO en vigueur (registre `registres/go.md`, à relire tel quel ; ne jamais nommer un autre GO de calcul dans une ligne neuve ; seules les lignes de type « révocation » révoquent)

| GO | Objet | Plafond | État |
|---|---|---|---|
| GO-2026-11-02-21 | A1-v3 | 400 USD | texte à finir (§ 6.2) |
| -22 | A1-v4 (attaque contre v9) | 200 USD | après A1-v3 |
| -23 | tour fermé, étage 1 | 50 USD | couples et configuration (§ 6.4) |
| -25 | réplication d'A1-v3 par Kimi | 150 USD | après A1-v3 |
| -27 | relance de R1 sur la table v3 | 60 USD | addendum v3 (§ 7.3) |
| -28 | T0.6 et test croisé | 200 USD | préparation (§ 7.4) |
| -29 | P3-bis | 80 USD | préparation (§ 7.4) |
| -30 | complément de validation | 40 USD | concordance (§ 7.2) |
| -31 | collisionneur | 40 USD | en cours (§ 6.6) |
| -32 | juges v2 | 60 USD | brouillon 2 à refaire (§ 6.5) |

Lignes remplacées et non utilisées : -17 (191 USD, remplacé par -21), -19 (remplacé par -23), -24 (remplacé par -32), -26 (remplacé par -30). Décisions du jour : -15, -16, -18, -20.

Le lanceur exige que le plafond du texte scellé soit **exactement** égal au montant du GO.

---

## 11. Réserves ouvertes
1. « 27 scripted cheaters » reste écrit dans le README public, la page A1 et le texte scellé d'A1 ; une correction datée est due.
2. Le changement de description du nul v9 n'a pas été contre-lu (§ 6.3).
3. Les courses à blanc de l'attaque v4 ont tourné avec l'ancienne description.
4. Le développeur des juges v2 a été coupé ; son travail partiel n'est ni vérifié ni commité.
5. Le vérificateur de `e58cfec` chez session-depot n'a pas rendu.
6. La fille reste sur l'ancien compte (§ 8.4).
7. Les lignes R-1282 à R-1287 ont été écrites en fin de session, d'après les commits ; leurs heures sont les heures des commits.

## 12. Fin de chaque session
- Passation `registres/passations/AAAA-MM-JJ-HHMM.md` (heure par `date -u`), scellée, jamais réécrite.
- Mise à jour de `registres/etat.md`.
- Commit et poussée sur `canal/conv-audit-n04`.
- Si tu passes la main à une autre instance, un brief comme celui-ci.
