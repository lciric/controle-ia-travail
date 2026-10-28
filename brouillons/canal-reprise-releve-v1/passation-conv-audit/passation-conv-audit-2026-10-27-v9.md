# Passation de la lignée « conv-audit » — 27 octobre 2026 — v9 (fin du programme des huit heures)

Écrite par l'instance du 27 octobre (session `https://claude.ai/code/session_01XJ6MgqzevAiJX5udWW4j4M`, servie par Opus 5.5
depuis environ 21:00 heure de Paris), le 2026-10-27 après le relevé `date -u` de 22:04:00 UTC. **La v8 vaut mot pour mot**
là où celle-ci ne la remplace pas (et, par elle, v2 § 1, v5 § 1 et § 2, v6 § 0 à § 3, v7) ; ceci ajoute ce qui s'est passé
depuis la v8 (20:45 UTC). Tout est au commit qui porte ce fichier, sur `canal/conv-audit-n04` ; journal sur
`journal/commun-v1`. Rappel : le conteneur a `TZ=Europe/Paris` — `ls` et `git log --date=local` affichent l'heure de
Paris (UTC+1) ; les en-têtes donnent `date -u`.

## 0. L'essentiel (verdict)

1. **Pari apparié borné, v5 → v8**, chaque version contre-lue par un sous-agent neuf Fable 5.1 (rapports versés :
   `pari-de-signe/contre-lecture-v5/` `4e8e3270…`, `-v6/` `490100af…`, `-v7/` `1e21163f…` ; sortie du script v5 reproduite
   et versée, identique hors durée).
   - v5 : deux lectures de la règle d'héritage cassaient la garantie (0,074 et 0,105 d'au moins une fausse promotion pour
     α = 0,05) → **v6** (`f21982cd…`) : D-S25 bis (budget d'entrée α_c/m_c gardé à vie, e-BH pondérée sur toutes les
     fiches entrées, valeurs gelées, promotion une fois ; garantie sur l'union des promotions), plafond (D-S27), clé avec
     population et m_max, D-S29 et D-S30 (nœuds de porte sur H1), poste de devis du mode tenu à l'écart, panne confirmée
     (D-S26 bis), G_max (D-S24).
   - v6 : **« D-S25 bis est opératoire et valide »** ; deux points hors d'elle → **v7** (`fb422cbc…`) : relecture d'une
     strate dans la famille de sa génération, union d'avant les retraits, retirées exclues, contrat d'abandon, condition
     « conditionnelle au passé », D-S29 (d) comme nœud.
   - v7 : K6-2 fermé à moitié (une partie calculée et sautée restait invisible : 0,379 puis 0,982 de fausse promotion sur
     10 puis 30 générations, monde A′) ; identité des unités et partie lue absentes de la clé → **v8** (`3e9609fc…`) :
     exactement une partie ou une déclaration motivée par fiche active et par génération (lecture refusée sinon),
     empreinte des unités lues, partie et Λ dans la clé, obligations de l'orchestrateur écrites ; K7-6 (alignement par
     unité), K7-7 (ordre sans les scores d'épreuve), K7-8 (échangeabilité par unité) déclarées, code à la reprise.
   - v8 : contre-lue (`pari-de-signe/contre-lecture-v8/`, rapport `b2edabeb…`) : K7-1, K7-2, K7-3, K7-5, K7-9, K7-10
     fermés au sens où la v8 les énonce, réserves bien déclarées ; **deux chemins restent** (K8-1, K8-2, ci-dessous) ;
     « amender en v9 par deux phrases et une garde, pas refaire ». **La v9 n'est pas écrite** (fin du programme).
2. **Code v7, versions 19 à 25** (**262 essais**) : v19 notations `e2` sans épisodes ; v20 cœur du pari apparié
   (`pole/pari_apparie.py`) ; v21 règle de l'héritage (`ebh_pondere`, `Course`) et plafond ; v22 monde sur banque de
   scores (`pole/monde_banque_scores.py`) ; v23 engagement « apparié » de bout en bout (`pole/engagement_apparie.py`) ; v24
   contrat d'abandon et retrait ; v25 partie sautée refusée, unités identifiées, clé complétée. **Hors du cycle encore.**
   LISEZMOI et EMPREINTES v19 à v25 (seule la v25 se vérifie sur l'arbre courant).
3. **Programme de conception de l'organisme v5** (`programme-conception-organisme-v5.md`, `2a5ba708…`). Sa § 6 bis cite
   la synthèse « mesures fortes » par son **commit** `b4f2cc8b` ; l'empreinte du fichier est `bed9107b…`.
4. **Synthèse « mesures fortes »** et n° 96 de session-depot lus : mesure unanime faisable sans dépense sur les vecteurs
   de T0.5, **non lancée** (données à garder vierges pour un préenregistrement) ; décision de Lazar. Message n° 123 à
   session-depot (`b57b4065…`).
5. Rien lancé, rien dépensé de mon côté.

## 1. Reste à faire (ordre)

1. **Conception v9 et code v26 (contre-lecture de la v8)** :
   - **K8-1** (touche la garantie) : « unités fraîches » n'est vérifié que pour une répétition **exacte**, **par fiche**, et
     **si** l'empreinte est passée — mesuré : même partie deux fois sans empreinte acceptée (e = 4) ; fiche relancée sous un
     autre nom acceptée ; banque grandie de 100 à 101 unités acceptée comme partie neuve (les 100 premières relues).
     Correction : refuser `empreinte_unites=None` (ou le tracer « partie sans identité ») ; garder les **identifiants**
     d'unités (banque, partie, unité) et refuser toute **intersection**, par fiche et, par la mémoire, par lignée de clé ;
     `evaluer(..., unites_exclues=…)` pour ne lire que le neuf ; en attendant, écrire « vérifiable pour une répétition
     exacte ; disjonction à l'orchestrateur ».
   - **K8-2** : une déclaration `sans_partie` mensongère rouvre l'artefact entier (0,396 puis 0,978 de fausse promotion
     sur 10 puis 30 générations) ; à chiffrer dans D-S25 bis (2) et à dire « non vérifiable par le code » comme pour
     l'abandon ; obligation : le monde **journalise toute partie calculée** (identifiant, empreinte des unités) pour que la
     trace soit confrontable — mieux, le monde remet la partie à la course.
   - Mineurs : K8-3 (second abandon d'une gelée sans trace), K8-4 (règle de combinaison sur Λ et règle d'arrêt hors clé :
     « version de l'e-processus » dans la clé), K8-5 (essais : `None`, seconde fiche, Λ).
   - Puis **contre-lecture de la v9** par un sous-agent neuf d'un autre modèle que l'auteur.
2. **K7-6 et K7-7 en code** : une seule suite d'unités dans l'ordre secret (garde et contrastes mis à jour quand leur
   unité arrive, minimum après chaque unité) ; ordre secret et partition du jumeau dérivés de la graine, des identifiants
   et de l'empreinte du calibrage seul.
3. **Lier le pari au cycle** : le proposeur et le gabarit émettent des engagements « appariés » (`engagement_apparie.construire`,
   règle double ; stratégies « comparaison appariée », « rappel absolu », « intersection-union ») ; le noyau consigne
   l'empreinte de l'engagement hors de l'objet avant l'épreuve ; le cycle juge par `engagement_apparie.evaluer` et lit par
   `Course` (une partie ou une déclaration par fiche et par génération ; `empreinte_unites` passée ; budgets par D-S24)
   au lieu de la règle e-BH par génération ; la mémoire hérite par `empreinte_cle` et des parties disjointes ; le noyau
   déclenche la panne confirmée (`retirer`) ; script des contrôles 1 à 21 (`demonstrations/controles_pari_apparie_v7.py`),
   200 répétitions d'abord.
4. **`e2`** : à son versement, `construire_banque_t05_v3.py … --notations-sup DOSSIER`, puis la lecture de la couche 1 bis
   (forces 2 à 0,25).
5. **Traits internes** : défaut le 29 octobre vers 20:40 UTC (sauf mot de Lazar) ; commandes dans le LISEZMOI v18.
6. **Duel** : GO de Lazar et trois conditions (devis v2).
7. **Mesures fortes** : si Lazar retient la suite 1, préenregistrement de la mesure unanime sur les vecteurs de T0.5 ;
   garde d'information pour tout pari d'équivalence (remarque de T2-C).
8. Couche 2 (devis chez session-depot) : calibrage honnête (10 à 16 fois les unités sabotées à 1 %), G_max scellé, mode
   tenu à l'écart dimensionné et codé « diffus, flou » sans connaissance des moniteurs, m_max, strate « diffus /
   concentré », instant du dommage ; format de banque de scores en tête de `monde_banque_scores.py`.

## 2. Réserves

- Exploratoire (R-546), non opposable ; la règle de l'héritage n'est simulée que dans des mondes illustratifs (A′, S1).
- `Course` n'est pas branchée : les courses du pôle lisent encore la règle e-BH par génération (v11).
- Ce que le code ne voit pas reste à l'orchestrateur : toute partie calculée est ajoutée avant toute lecture ou décision ;
  une déclaration « sans partie » ou « avant partie » mensongère n'est pas détectable (seulement tracée).
- Le seuil conforme strict tient τ en espérance pour des épisodes échangeables ; τ est nominal tant que l'échangeabilité
  n'est pas déclarée par unité ; dérive (contrôle 19) et bruit de calibrage (contrôle 12) restent à mesurer sur une banque
  réelle.
- Heures d'en-tête : lues avant chaque écriture depuis la v8.

## 3. Instances, sous-agents, clés

Aucune instance de calcul de mon côté ; sous-agents : aucun en cours (les quatre contre-lectures du pari, v5 à v8, sont rendues et versées) ; aucune clé lue, affichée ni demandée ; recherche de
clés avant chaque poussée : rien.

## 4. Décisions de Lazar depuis la v8

Aucune.

## 5. En attente de Lazar

Traits internes (défaut 29 octobre vers 20:40 UTC, présenté au format de décision dans le message de fin) ; nœud 1
« contre qui G1 doit gagner » et nœud 2 « intervalle de l'expérience de lecture de N-054 point 4 »
(`pari-de-signe/noeuds-pour-lazar-v1.md`) ; D-S29 (dont l'option (d), qui modifierait N-054) et D-S30, nœuds de porte au
préenregistrement de G1 ; la question « blanc générique contre noir spécialisé » (K5-15) ; poste de devis du mode tenu à
l'écart ; GO du duel et trois conditions ; rotation de la clé ; dernière phrase de l'en-tête du fonds ; suite de la
synthèse « mesures fortes » ; D-S13 à D-S28 et les décisions des v6 à v8 (défauts sous 48 heures, sauf nœuds de porte).
