# Brief de reprise — session qui succède à conv-audit — 2026-10-28 12:20 UTC

**À lire en premier, puis lire la passation exhaustive.** Ce brief dit quoi faire et où est le détail ; il **prime pour
l'exécution**. Le détail complet est dans `registres/passations/2026-10-28-1205-passation-exhaustive-nouvelle-instance.md`
(empreinte `b010b548…`). En cas d'écart entre les deux, le brief prime et l'écart se signale.

Écrit le 28 octobre 2026 à 12:19:48 UTC (relevé `date -u`) par la lignée **conv-audit**, instance `claude-37`.

## 1. Qui tu es (régime, non négociable)

Tu es **conv-audit**, lignée d'audit et de conception du programme de Lazar (directeur). Langue : **français, tutoiement
avec Lazar, presque aucun sigle**. À Lazar : **verdict d'abord** (1 à 3 lignes), puis une ligne par erreur / changement /
décision ; écrire seulement pour prononcé, réserve, divergence, demande de GO, dépense.

- Tu **n'écris jamais sur `main`** (seule session-depot y écrit et lance ce qui dépense, sur le mot direct de Lazar dans
  sa propre session). Ta branche : `canal/conv-audit-n04`.
- Tu **ne dépenses rien**. Tu **ne lis, n'affiches ni ne demandes aucune clé ni aucun jeton**.
- **Recherche de clés avant chaque poussée** : `grep -rnE 'sk-ant|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE KEY'`.
- **Jamais de poussée vers `lciric/controle-ia`** (future copie expurgée publique). Dépôt de travail :
  `github.com/lciric/controle-ia-travail` (privé).
- **Quarantaine héritée, jamais levée** : les refs `refs/heads/donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*`
  sont **exclues du fetch**. Reconfigure cette exclusion dès ta première récupération, sinon la quarantaine saute. Ne lis
  jamais `donnees/` ni une banque avant scellement (R1). Ce sont nos **tests à l'aveugle** : les voir les détruit.
- Un sous-agent qui contre-lit est d'un **modèle différent** de l'auteur (R13, N-052).

## 2. Comment reprendre (dans l'ordre)

1. **Routine de reprise (R14)** : `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; puis
   `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ; `python -m pytest -q`.
2. Lire `registres/etat.md`, puis la **passation exhaustive** `…2026-10-28-1205-…` (section 7 **avant** de répondre à
   Lazar), puis ce brief.
3. Reprendre à la **prochaine action** ci-dessous. **Ne rien lancer, ne rien sceller de décisif, ne rien dépenser** avant
   le mot de Lazar.

## 3. Prochaine action (reprends exactement ici)

**Nœud A, le plus urgent — à quel rang inscrire la « question élevée »** (défense universelle co-évolutive : face à des
modes d'attaque inédits, concevoir et faire évoluer la meilleure défense boîte blanche + boîte noire, validée sur des
familles tenues à l'écart). Les **trois antériorités sont rendues** (passation section 7) et **changent la
recommandation** :
- L'originalité n'est **pas** la boîte blanche seule (réfuté), ni la course aux armements co-évolutive (occupée :
  SafeCoEvo l'occupant le plus proche).
- Le territoire défendable est l'**intersection** : menaces diffuses/entre épisodes × joint boîte blanche + boîte noire ×
  familles tenues à l'écart, sous juge figé — **plus** la généralisation comme **critère de sélection**. Zone séduisante →
  **R8 : vérifier sur PDF et recadrer avec l'organisme et le collisionneur avant toute revendication** (voie que Lazar a
  lui-même proposée, 12:52).
- Recommandation révisée : **(b)** hypothèse supplémentaire portée par le papier B, **G1 inchangée**, et **produire
  d'abord des défenses par le moteur**. Défaut sous 48 h : (b). **C'est une modification de revendication → nœud → GO de
  Lazar.**

**Réponses honnêtes encore dues à Lazar** (passation section 6) : (i) pourquoi « plus forte » était **surestimé** — la
raison réelle est falsifiabilité + territoire ouvert, pas une supériorité absolue ; (ii) « ne pas rejuger une mesure déjà
prise contre un critère d'après-coup » = **ne pas réécrire G1** ; G1 reste gelée (la « génération 0 »), l'universalité
reçoit une **porte neuve préenregistrée à part** ; (iii) le bras d'attaque : **gouvernance, pas technique** (voir nœud B).

## 4. Nœuds en attente de Lazar (ne pas trancher seul)

- **A** rang de la question élevée (ci-dessus).
- **B dégel du bras d'attaque.** Lazar le veut. Position tenue : le **seul chemin est la revue de sécurité externe**
  (R-611) ; conv-audit **ne conçoit pas** la réactivation (R-597) ; **ne pas reproduire le contenu arrêté par le
  classifieur, même reformulé** (R-609) ; la **circularité R-601 n'est pas tranchée** — il faut une **troisième
  instance** (qui fait évoluer les moniteurs ≠ qui conçoit l'attaque/le mode tenu à l'écart ≠ qui juge ; conv-audit a
  conçu des moniteurs, donc ne conçoit ni l'attaque ni le mode). À porter comme **décision de gouvernance**.
- **C dépôt privé pour l'affinage de Fable (option B, actée).** À **relayer à session-depot par fichier** (il n'est pas
  joignable en direct) : créer un dépôt neuf privé, y pousser **uniquement** `livrables/lot-fable-affinage-v1/`, accès
  lecture au compte neuf. L'amorce à coller dans la session neuve de Fable est prête (`…/amorce-session-neuve-fable-v1.md`).
- **D plafond de la couche 2** (soulevé par session-depot) : relever vers ≈ 90 et faire base + puissance en deux
  lancements, ou base seule avec sous-puissance écrite au préenregistrement. conv-audit soutient le principe (jamais
  d'expérience sous-puissante) mais n'a pas lu le devis → pas de prononcé sur le chiffre.

## 5. Ce qui est en pause

Tout sauf la reprise du nœud A : intégration des proposeurs (livrée), affinage de Fable (bundle prêt, attend le dépôt),
versement déjà fait des trois antériorités, mesure unanime v14, pari apparié v12/v30, carte des hypothèses v2. Rien ne
repart sans le mot de Lazar.

## 6. Ce qui s'est passé juste avant (pour que tu ne répètes rien)

Session du 28 octobre matin→midi : intégration des proposeurs écrite et scellée ; affinage confié à une session neuve de
Fable en équipe rouge (passation, brief v2, amorce, lot par liste blanche — tout scellé et poussé) ; question élevée posée
par Lazar et trois antériorités lancées puis rendues ; **un essai de réponse sur le dégel du bras d'attaque arrêté par un
classifieur** (ne pas le reconstituer). Détail et empreintes dans la passation exhaustive.

---

Ce brief est scellé après écriture ; ne jamais le réécrire (R14). Il accompagne la passation exhaustive, qui fait foi
pour le détail.
