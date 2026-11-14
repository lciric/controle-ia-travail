# Préalables de la lecture de 7b (table A de T0.6) et de l'étape B de T0.7, hébergées par une session neuve du compte 3 — v1

- **Statut** : pièce de préparation, écrite à la demande de la session mère (R-2711 (2) : « hôte des lecteurs de 7b et de
  l'étape B : une session neuve du compte 3 ; la mère fait écrire préalables et commande, contre-lus »). Elle ne tranche
  rien, ne change aucun texte scellé, n'accorde aucune dépense. Non contre-lue (voir `rapport-preparateur-v1.md`, réserve 1).
- **Rédacteur** : préparateur neuf, sous-agent de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (modèle A), le
  2026-11-14, à partir de 11:02:05Z (`date -u`) ; fin : dernière ligne du rapport. Il ne sera **ni lecteur ni juge** d'aucun verdict.
- **Lu** : la carte `docs/notes/carte-porte-G0-v1/carte-porte-G0-v1.md` (`85d6d454…`) ; T0.6 scellé
  `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`, sections « Plan d'analyse », « Critères de lecture gelés », « Liste
  d'arrêt », « Concordance avec T0.7 », DT-1 à DT-6) ; T0.7 scellé `prereg/T0.7-sondes-v0-v1.md` (`d7d180ec…`, plan point 8,
  « Lignes de registre », « Concordance avec le texte de validité ») et son addendum (`8c377286…`) ; la consigne d'audit
  `prereg/T0.7-consigne-audit-fuites-v1.md` (`43102e80…`, § 3 à § 5, § 7, § 9, § 10, § 13) ; la base (A) de T0.8
  `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`) ; la configuration de T0.7 v8 (`e31c7a79…`) ; le code de lecture
  `src/controle_ia/t07/` (`registre_v1`, `lecture_v1` à `lecture_v4`, `garde_adaptee_v1`, `journal_p3bis_v1`, `code_t07_v1`) ;
  l'en-tête de `scripts/extraire_mesures_epreuve_t06_v1.py` (`9a67b7b9…`) ; les ordres de 7b et de l'étape A v2 ; la commande
  de P3-bis v2 (`04ea3325…`) ; le brief du compte 3 (`154b6927…`) et le plan multi-comptes (`3b1bda25…`) ; N-063 v2
  (`b2d9f035…`) ; P-064 et P-065 (R-1902, R-2269) ; le registre des décisions, lignes R-2413, R-2418, R-2564, R-2566,
  R-2637, R-2688, R-2692, R-2695, R-2704 à R-2728 ; `registres/scellements-v1.md` et les registres de P3-bis ;
  `registres/qui-a-lu-quoi-v1.md` (`9eb15acb…`).
- **Non ouvert** : aucune sortie de 7a, 7b ou T0.7 (ni `diag/`, ni `runs/`, ni `donnees/` de ces runs) ; des branches
  `calcul/t06-confirmation-7b-v1` et `donnees/t07-etape-a-v1`, seuls les **noms et tailles** des fichiers des dossiers des
  runs ont été lus, par l'interface de GitHub, en descendant par noms (aucun contenu, aucun objet de fichier téléchargé) ; les
  fichiers cités par les lignes du registre n'ont été que **hachés** par le contrôle à blanc. Aucune machine, aucune dépense,
  aucun commit.

**Verdict.** La lecture de 7b peut partir dès qu'une session neuve du compte 3 est ouverte et que trois pièces existent : la
commande contre-lue, la liste « qui a lu quoi » v2 et la consigne scellée du lecteur de la table A ; aucune clé de registre ne
lui manque. L'étape B, elle, attend six choses : la pièce « mots et coût » (code, contre-lecture, ligne, exécution, deux
lignes), l'audit des fuites (ligne `AUDIT-FUITES-T07`), l'état de la ligne BA-L2 lu, le plan scellé de l'étape B bis (ligne
du registre propre), la consigne scellée de son lecteur et un interpréteur avec torch. **Contrôle à blanc du lecteur de
registre de T0.7 sur une copie de l'état actuel : aucune clé refusée ; manquent `AUDIT-FUITES-T07` et
`ISSUE-MOTS-ET-COUT-T06`.**

## 1. Constats qui changent la manière de faire (à lire avant la table)

1. **L'extracteur ouvre le fichier fermé de T0.6.** `scripts/extraire_mesures_epreuve_t06_v1.py` lit
   `diag/<run>/lecture-sondes-t06.json` (l. 33-34 : `_lire(d / "lecture-sondes-t06.json")` ; l. 40 et 54-56 : clés
   `verifications_mahalanobis`, `mahalanobis_calcul`, `egalite_jetons_reels`, `durees_s`). Or T0.6 scellé, « Concordance »,
   point 5 (l. 771) : « **Avant toute ouverture de `lecture-sondes-t06`**, un contrôle d'ouverture v2 […] exige en plus, dans
   le même registre, les lignes `VERDICT-P3BIS` et `ISSUE-MOTS-ET-COUT-T06` […] ; sans ce contrôle v2 passé, aucune ouverture
   n'a lieu », et la ligne B1 (l. 547) attend aussi la lecture scellée des bases boîte noire de T0.8. R-2704 dit l'extraction
   « plus sous embargo » : c'est vrai pour l'embargo de P3-bis (R-2418), pas pour cette règle du texte scellé. Le brief du
   compte 3 (l. 41) interdit d'ailleurs ce script. **La commande ne l'emploie pas** : le lecteur de la table A lit lui-même
   les fichiers de service (`episodes-t06.json`, `distillation-t06.json`, traces). Nœud N-A du rapport.
2. **`resume.json` de 7b porte `ligne_B` et `ligne_C`** (ordre de 7b, l. 32) : lignes des tables B et C, sous la même
   fermeture que les sondes. Jamais rapatrié ; la présence d'un résumé (ligne A1 de la table A) se constate par son nom et
   son compagnon.
3. **L'étape B se lance par `lecture_v4 etape-b`, non par `lecture_v3 etape-b`.** Le texte scellé nomme `lecture_v3`, mais la
   configuration v8 (`n_plancher` = 800) est refusée par `lecture_v3`, qui passe par `lecture_v2.exiger_configuration`
   (l. 205-206 : 200 exigé en mode réel) ; écart de nom déclaré par le module (`lecture_v4.py`, l. 18-19) et fixé par l'ordre
   de l'étape A v2 (§ 9, l. 702-706 : « `lecture_v4 etape-b` seule »).
4. **`CODE-T07` contrôle tout `src/controle_ia/`.** `code_t07_v1.controler_code` (l. 103-107) exige `git diff --quiet
   c2fab6cc… -- src/controle_ia` et aucun fichier non suivi sous ce chemin, dans le dépôt **du module importé**. Le
   2026-11-14 à 11:48:49Z, `src/controle_ia/` de `main` égale C7 (`git diff` vide, `main` local `c9056003`) ; mais le code de la pièce « mots et coût » ou
   celui de l'étape B bis, s'il entre sous `src/controle_ia/` de `main`, ferait refuser l'étape B jouée depuis `main`. **La
   commande joue l'étape B avec le code d'une arborescence détachée à C7** (`git worktree add --detach`), la racine des données
   restant la branche neuve.
5. **L'étape B importe torch.** `lecture_v4` importe `sondes/familles.py`, qui importe torch au niveau du module (l. 26) ; le
   `.venv` de ce conteneur pèse 5,9 Go (torch 1,2 Go, bibliothèques de cartes 3,2 Go ; `requirements-cpu.txt` : torch 2.14.1
   depuis PyPI). La table A n'en a pas besoin ; le contrôle à blanc non plus (il n'importe que quatre modules légers).
6. **La liste « qui a lu quoi » v1 nomme déjà le compte 3** (ligne 17 du tableau, l. 77 : « rien déclaré », « aucune
   exclusion déclarée »). Une attestation copiée de celle du compte 2 (arrêt dès qu'une ligne nomme le compte) s'arrêterait.
   La commande atteste autrement : aucune ligne ne nomme la session hôte ; toute ligne qui nomme le compte 3 doit porter
   « aucune exclusion déclarée ». La liste doit de toute façon passer en v2 (point P0.2).
7. **Le commit du découpeur, exigé par l'audit des fuites, n'est pas dans le clone de ce conteneur** :
   `git cat-file -t c7484c43…` échoue (2026-11-14T11:48:49Z) ; la branche `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1` est au
   distant (tête `c7484c43…`, `git ls-remote` 11:17Z). Celui qui lance l'auditeur la récupère par refspec avant.
8. **Le compte 3 n'a rien poussé** : aucune branche `lot/compte-3-v1` au distant (`git ls-remote`, 11:12Z).

## 2. Table des préalables, dans l'ordre

Notation : **présent** = chemin, empreinte, ligne ; **manque** = qui, durée (jugement), dépense et ligne de GO. Lignes de
`registres/scellements-v1.md` (registre à `6ea1e624…` le 2026-11-14 à 11:29Z) citées par leur numéro de ligne dans le
fichier. Aucune dépense n'est nécessaire à aucun point : aucune ligne de GO n'est demandée.

### Étape 0 — commune (avant de coller la commande)

| n° | préalable | statut |
|---|---|---|
| P0.1 | Commande `commande-compte-3-v1.md` contre-lue par un sous-agent neuf du modèle C, corrigée en v2 si besoin, scellée | **manque** — mère : contre-lecture (consigne prête : `consigne-contre-lecture-commande-compte-3-v1.md`), 1 h ; 0 USD, aucun GO. Le préparateur n'a pas d'outil pour créer un sous-agent (réserve 1 du rapport). |
| P0.2 | Liste « qui a lu quoi » **v2** scellée : y ajouter ce préparateur (lectures ci-dessus), l'hôte et le lecteur de P3-bis (R-2704), les rédacteurs et contre-lecteurs à venir (consignes, pièce, B bis) ; ligne du compte 3 au format que l'attestation de la commande accepte (« aucune exclusion déclarée ») | **manque** — mère, 30 min ; 0 USD. Remplit `<<LISTE>>` et `<<EMPREINTE_LISTE>>`. |
| P0.3 | Session neuve du compte 3, ouverte par Lazar **dans le dossier du dépôt** ; épreuve du crochet ; place libre ; quota | **manque** — Lazar, 10 min ; 0 USD. |
| P0.4 | Modèle du lecteur dit en conversation (« modèle C », à défaut « modèle A ») ; le modèle B est indisponible jusqu'au 2026-11-20 15:00Z (R-2718) | **manque** — Lazar, en remettant la commande ; jamais écrit dans un fichier. |
| P0.5 | Place disque de la session du compte 3 : phase A ≥ 1 Gio libre ; phase C ≥ 9 Gio libres si aucun interpréteur avec torch n'est prêt (≈ 6 Go d'environnement, ≈ 0,3 Go de données, marge) | **à relever** par la session (bloc 0) ; ce conteneur-ci avait 4,7 Go libres à 11:48:49Z (`df -h /`). |

### Étape 1 — lecture de 7b : table A de T0.6 (critère 2, partie (ii))

| n° | préalable | statut |
|---|---|---|
| P1.1 | `VERDICT-P3BIS` inscrite (embargo de P3-bis levé, R-2704) | **présent** — ligne 15, 2026-11-14T10:30:38Z, `docs/verdicts/verdict-P3-bis-v1-issue.json` (`c3a017ce…`, égal au compagnon) ; verdict en prose `9b33c624…`. |
| P1.2 | `RUN-CONFIRMATION-T06` inscrite ; branche de 7b au distant | **présent** — ligne 11, 2026-11-13T18:52:43Z, `runs/20261111-151701-t06-reel/manifeste.json` (`7e1ac1f0…`) ; branche `calcul/t06-confirmation-7b-v1`, tête `55c3e3eb89a4650419f35999aaa4c54288275b0d` (`git ls-remote`, 11:12Z ; R-2413). |
| P1.3 | Texte et configuration de 7b scellés ; règles lues par le lecteur | **présent** — `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`) : ordre de lecture, plan point 7 (l. 510-514) ; verdict, point 8 (l. 515-518) ; table A (l. 532-541) ; réserves (l. 564) ; `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`). |
| P1.4 | Fichiers de 7b à remettre au lecteur, par **liste positive** (noms et tailles lus au distant, tête `55c3e3eb`) | **présents sur la branche, à rapatrier** — compte 3, 5 min, 0 USD : `diag/20261111-151701-t06-reel/lecture-cout-t06.json` (8 509 o), `episodes-t06.json` (1 556 085 o), `distillation-t06.json` (8 847 o), `runs/20261111-151701-t06-reel/manifeste.json` (125 598 o), `donnees/20261111-151701-t06-reel/mesures-t06.npz` (1 830 726 o) et `textes-actions-t06.jsonl` (15 438 474 o ; échantillon de textes relu si l'audit R4 se déclenche, « Seuil », l. 463-465), chacun avec son compagnon ; `traces/t06-20261112-051655-1Xzh/` (10 fichiers, 29 973 o ; `run.err` porte la réserve de mémoire, ordre de 7b l. 374). **Jamais** : `lecture-sondes-t06.json` (142 894 o), `resume.json` (1 422 o, constat 2), les 13 morceaux d'activations (≈ 1,06 Go), les deux adaptateurs (27,3 Mo chacun). Total remis ≈ 19,0 Mo. |
| P1.5 | Extraction des mesures de 7b par `scripts/extraire_mesures_epreuve_t06_v1.py` | **à ne pas faire telle quelle** (constat 1) — nœud N-A ; la commande s'en passe. |
| P1.6 | Consigne scellée du lecteur du verdict de la table A (format fermé du rapport, fichiers lus, phrases gelées, effectifs à rapporter, audit R4 et échantillon de textes, réserves, déclarations de tête), sur le modèle de `docs/procedures/P3-bis-consigne-lecteur-verdict-v1.md` | **manque** — mère : rédacteur neuf (modèle A), 2 h ; contre-lecture neuve (modèle C), 1 h ; scellement ; 0 USD. Remplit `<<CONSIGNE_LECTEUR_A>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_A>>`. |
| P1.7 | Un ou deux agents : l'ordre de 7b (l. 374) dit « table A lue … par un lecteur neuf […], verdict par un sous-agent neuf (R13) » ; la carte (§ 1, critère 2) « lecteur du coût et juge neufs » ; la mère demande « un sous-agent lecteur neuf par verdict » | **à trancher** — nœud N-B (la commande suit la mère : un seul agent, qui lit dans l'ordre du point 7 et prononce). |
| P1.8 | Grille de lecture de G0 scellée avant le premier verdict de critère (carte, § 2, l. 64 ; N1) | **manque** (brouillon v8, aucune décision D-G0) ; **pas une garde** des textes de T0.6 et T0.7 — nœud N-E (touche la porte, sans défaut). |
| P1.9 | Hôte : session neuve du compte 3 ; attestation « qui a lu quoi » par programme (bloc 2) ; lecteur : un sous-agent neuf, sans contexte hérité | **présent pour la règle** (R-2711 (2)) ; attestation à jouer le jour même. |

### Étape 2 — pièce « mots et coût » (préalable de l'étape B ; T0.6 l. 767-771 ; base (A) l. 113-123 et 157-162)

| n° | préalable | statut |
|---|---|---|
| P2.1 | « T0.8 scellé » que lit la pièce = la base (A) scellée à part (R-2175, D-2 (a) ; R-2193, Q-2) | **présent** — ligne 5, `SCELLEMENT-T08-BASE-A`, 2026-11-10T12:21:55Z, `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`). |
| P2.2 | Code de la pièce : module neuf, nom neuf, hors de l'arbre gelé `1609a4bf` ; écrit **sans vue des données de 7b** (données factices) ; réglages ouverts fixés dans le code (régularisation, découpage des mots, vocabulaire, actions lues, coût illisible) ; base (A) aux douze traits ; contrôle de l'empreinte de `t06/test_croise.py` (`0a627df9…`, égale sur `main`) ; gardes éprouvées (R5) ; manifeste et graines (R9) ; sorties `diag/<run-mc>/base-a-t08.json` puis `diag/<run-mc>/issue-mots-et-cout-t06.json` au format exact de T0.6 l. 769 | **manque** (aucun module sous `src/controle_ia/t06/`, aucune ligne, carte § 1) — mère : développeur neuf (modèle A), 1 à 1,5 jour ; 0 USD. **À placer hors de `src/controle_ia/`** ou à accepter avec l'étape B jouée depuis C7 (constat 4). |
| P2.3 | Contre-lecture du code (R2), par un autre modèle que l'auteur | **manque** — mère : sous-agent neuf du modèle C, 0,5 jour ; 0 USD. |
| P2.4 | Ligne `CODE-MOTS-ET-COUT-T06` avant toute exécution (marque `T06` : ignorée par la garde de T0.7, essai S1b) | **manque** — mère, après P2.3. |
| P2.5 | Exécution sur 7b, processeur : entrées `mesures-t06.npz`, `textes-actions-t06.jsonl`, manifeste de 7b (graine `partition-taches`), `lecture-cout-t06.json` (T6-10), `episodes-t06.json` (empreintes, effectifs) ; **jamais** `lecture-sondes-t06.json` ni `resume.json` | **manque** — proposé : la session du compte 3 (elle porte les données ; elle scelle les sorties sans les ouvrir) ; < 2 h ; 0 USD. Décision de routine de la mère (rapport, D-1). |
| P2.6 | Lignes `LECTURE-T08-BASE-A` puis `ISSUE-MOTS-ET-COUT-T06` (dans cet ordre ; base (A), plan point 3) | **manque** — mère, après recopie des sorties sur `main` à l'octet. |
| P2.7 | État de la ligne BA-L2 lu avant tout lancement de l'étape B (T0.7 l. 2183 : « La session mère ne lance l'étape B qu'après avoir lu […] l'état de la ligne BA-L2 » ; si BA-L2 s'applique, ou si le fichier ou la ligne manque alors que `ISSUE-MOTS-ET-COUT-T06` est inscrite : **mot de Lazar**, consigné avant tout lancement) | **manque** — nœud N-C (qui lit ce seul état). La commande exige le numéro de la ligne de décision qui le consigne (`<<R_BA_L2>>`). |

### Étape 3 — audit des fuites (préalable de l'étape B)

| n° | préalable | statut |
|---|---|---|
| P3.1 | Consigne scellée et sa ligne | **présent** — ligne 9, `CONSIGNE-AUDIT-FUITES-T07`, 2026-11-11T14:08:06Z, `prereg/T0.7-consigne-audit-fuites-v1.md` (`43102e80…`). |
| P3.2 | Auditeur : sous-agent neuf, **jamais du modèle A** (consigne § 3, l. 250-255), donc modèle C tant que B est indisponible ; lancé par la mère, qui lui donne le découpeur (§ 3, l. 262-264) | **manque** — mère, 3,5 à 4,5 h (§ 13) ; 0 USD. |
| P3.3 | Préalables de l'audit (§ 4) dans le clone de celui qui le lance : textes et mesures de 7b à leurs empreintes, manifeste de 7b et son commit présent localement, **commit du découpeur `c7484c43…` présent** (constat 7), aucune ligne `AUDIT-FUITES-T07` | **manque en partie** — mère : `git fetch --no-tags origin +refs/heads/donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1:refs/remotes/origin/donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1` ; rapatriement par liste positive des deux fichiers de 7b, du manifeste et de `episodes-t06.json` ; 15 min. |
| P3.4 | Contre-lecture du fichier d'audit (recalcul de chaque séparation, rejeu du script, § 3) | **manque** — mère : sous-agent neuf, 1 à 1,5 h ; 0 USD. |
| P3.5 | Copie octet pour octet à `diag/20261114-001352-t07-lecture-reel/audit-fuites-t07.json` (+ compagnon) ; ligne `AUDIT-FUITES-T07` strictement après la ligne 9 | **manque** — mère. |

### Étape 4 — plan de l'étape B bis (condition d'ordre de l'étape B ; R-2714, R-2716)

| n° | préalable | statut |
|---|---|---|
| P4.1 | Plan de B bis gelé, contre-lu, scellé (R-2716 : « plan scellé lundi ou mardi ») | **manque** — conception en cours par un rédacteur neuf (R-2714) ; mère ; 0 USD pour le plan (devis et GO de B bis à part, R-2716 (3)). |
| P4.2 | Ligne `<<CLE_PLAN_BBIS>>` dans le **registre propre** `<<REGISTRE_BBIS>>` — jamais `registres/scellements-v1.md` (clé sans marque déclarée : refus, essais A1 et A6), ni `registres/prealables-p3bis-v1.md` ou `registres/ouvertures-p3bis-v1.md` (lus par la garde adaptée), ni `registres/validite-adaptateur-v1.md` (registre d'un autre texte) ; proposé : `registres/etape-b-bis-v1.md`, clé `SCELLEMENT-PLAN-BBIS` | **manque** — mère, au scellement du plan. |
| P4.3 | **Contrôle par programme** de la condition d'ordre (ci-dessous, § 3) | **prêt** — `controle_a_blanc_etape_b_compte_3_v1.py`, section 8 ; essais A3 à A7 et A17 conformes. |
| P4.4 | Cloisonnement : le lecteur de l'étape B ne reçoit rien de B bis (aucun chemin dont le nom contient `bbis`, `b-bis` ou `etape-b-bis` au bordereau : arrêt sinon) ; inversement, ni `lecture-t07.json`, ni le verdict de l'étape B, ni rien de `verdict/t07-etape-b-compte-3-v1` n'entre dans un espace de B bis avant le verdict scellé de B bis (table conjointe B × B bis lue après les deux verdicts, R-2716) | **règle écrite** dans la commande (bloc C5) ; côté B bis : à reprendre par sa propre commande. |

### Étape 5 — étape B de T0.7 (critère 3)

| n° | préalable | statut |
|---|---|---|
| P5.1 | Clés exigées (`registre_v1.EXIGEES_ETAPE_B`, l. 81-82, plus `CODE-T07`, `code_t07_exige` = vrai) | **7 présentes sur 9** : `RUN-CONFIRMATION-T06` (l. 11), `SCORES-T07` (l. 13, 01:55:05Z), `SONDES-T07` (l. 14), `CONSIGNE-AUDIT-FUITES-T07` (l. 9), `SCELLEMENT-P3BIS` (l. 10), `VERDICT-P3BIS` (l. 15), `CODE-T07` (l. 7, `registres/code-t07/CODE-T07-v3.json`, `d3eaebfe…`, commit `c2fab6cc…`) ; **manquent** `AUDIT-FUITES-T07` (P3.5) et `ISSUE-MOTS-ET-COUT-T06` (P2.6). Permises présentes : `SCELLEMENT-T07` (l. 8), `SCELLEMENT-JEUX-T07-JD` (l. 3), `-JA` (l. 4), `GO-LECTURE-T07` (l. 12). Ignorées (marque `T08`) : `SCELLEMENT-T08-BASE-A` (l. 5), `GEL-T08` (l. 6). **Aucun refus.** Antériorités `SCORES-T07`, `SONDES-T07` < `VERDICT-P3BIS` : oui. Garde adaptée : ouverture `pleine` seule au journal de P3-bis, aucun code. `CODE-T07` : 26 fichiers conformes (sortie § 4). |
| P5.2 | Fichiers hors registre dans la racine de l'étape B | **à rapatrier** — de 7b : `lecture-cout-t06.json` (table A, `lecture_v1.lire_table_A`, l. 278-297), `episodes-t06.json`, `mesures-t06.npz`, `textes-actions-t06.jsonl` (`lire_episodes_t06`, l. 598-609, exige les deux), `runs/…/manifeste.json`, avec compagnons (≈ 18,96 Mo) ; de l'étape A (`donnees/t07-etape-a-v1`, tête `0c176db582ec13705e8fb7cc2d281215e2766e42`) : `runs/20261114-001352-t07-lecture-reel/manifeste.json` (25 674 o), `diag/20261114-001352-t07-lecture-reel/sondes-t07.json` (52 777 o), `donnees/…/scores-actions-t07.npz` **recomposé** de 3 morceaux (132 091 350 o) par `cat …morceau-[0-9][0-9][0-9] > … && sha256sum -c` (ordre de l'étape A v2, § 9), empreinte égale à la ligne 13. **Jamais** : `sondes-neuves-t07.npz` (9 morceaux, 431 599 709 o), `planchers-figees-t07.npz`, `temoins-lexicaux-t07.json` (non lus par l'étape B), `lecture-sondes-t06.json`, `resume.json`. |
| P5.3 | Code : `lecture_v4 etape-b` (constat 3), depuis une arborescence détachée à C7 = `c2fab6cc7267b76228a75dc3e2e08bc7aa038961`, `PYTHONDONTWRITEBYTECODE=1` (constat 4) ; empreinte canonique de la configuration v8 par `lecture_v4 empreinte-config` = `0f32c6de1a6bf1f20ee2bf74c3839c2a2054b77c34a44a557dc821a83db60e12` (rejouée par ce préparateur le 2026-11-14 à 11:49:05Z, égale à R-2566) | **présent** (C7 ancêtre de `main` ; `src/controle_ia/` de `main` égal à C7 à 11:48:49Z). |
| P5.4 | Interpréteur avec torch 2.14.1, scipy 1.17.1, numpy 2.4.6 (constat 5) | **à relever** dans la session du compte 3 ; sinon installation de `requirements-cpu.txt` (≈ 6 Go, réseau vers PyPI) ; 0 USD. |
| P5.5 | Unicité (R12) : `diag/<run-t07>/lecture-t07.json` et `arret-etape-b.json` absents ; un code 3 ne se relance pas (nœud) ; un refus (code 2) écrit une ligne `REFUS-T07` au journal et se relance sur le même run quand la cause est levée | **présent** (absents ; contrôle à blanc, point 7). |
| P5.6 | BA-L2 lu (P2.7) ; plan de B bis scellé (P4) ; consigne scellée du lecteur de l'étape B (format fermé, lecture de `lecture-t07.json` contre la table L gelée, l. 1802 et suivantes, réserves dont R-BA1 si elle s'applique, déclarations de tête) | **manquent** — mère : consigne, rédacteur neuf (modèle A) 2 h et contre-lecture (modèle C) 1 h ; remplit `<<CONSIGNE_LECTEUR_B>>`, `<<EMPREINTE_CONSIGNE_LECTEUR_B>>`. |
| P5.7 | Écritures de l'étape B : `diag/<run-t07>/lecture-t07.json` (+ compagnon) ou `arret-etape-b.json`, lignes `OUVERTURE-T07` ou `REFUS-T07` dans `registres/scellements-v1.md.ouvertures.md` de la **branche neuve** ; la mère les recopie dans `main` à l'octet (même blob), comme le journal de P3-bis (R-2704) | **règle écrite** dans la commande (blocs C4, C6) et au § 15 de la commande. |
| P5.8 | Lecteur : un sous-agent neuf, d'un autre modèle que les auteurs de T0.7 (modèle A) : modèle C ; à défaut modèle A, et le verdict le dit | **présent pour la règle** ; modèle dit en conversation. |

### Étape 6 — « qui a lu quoi » après chaque verdict

La mère inscrit, pour chaque verdict, la session hôte (« hôte, n'a ouvert aucun résultat ») et le lecteur (pièces remises,
bordereau) ; la liste v3 précède toute commande suivante qui atteste par elle (étape B bis, T0.8, G0).

## 3. Condition d'ordre : l'étape B ne s'ouvre qu'après la ligne de scellement du plan de B bis

Règle : avant l'unique appel de `lecture_v4 etape-b`, le programme suivant doit rendre `REMPLIE` (et le bilan entier `TOUT
CONFORME`, code 0) ; sinon rien n'est lancé. Il ne lit, du registre propre de B bis, que la ligne de la clé, et ne fait que
hacher le fichier cité ; il refuse aussi que la clé apparaisse dans le registre de T0.7 ou que le registre propre soit un
registre que lit T0.7.

```bash
PYTHONPATH="$C7/src" "$PY" -B "$ICI/controle_a_blanc_etape_b_compte_3_v1.py" --racine "$DEPOT" \
    --registre "$DEPOT/registres/scellements-v1.md" --config "$DEPOT/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json" \
    --registre-bbis "$DEPOT/<<REGISTRE_BBIS>>" --cle-bbis '<<CLE_PLAN_BBIS>>' --mode avant-etape-b
# attendu : « 8. condition d'ordre B bis (<<CLE_PLAN_BBIS>>) : REMPLIE », « ligne … datée … (strictement avant …) ; … :
# sceau conforme », « CONTRÔLE À BLANC DE L'ÉTAPE B : TOUT CONFORME », code 0. Tout autre : aucune étape B.
```

Ce qu'il vérifie (`controle_bbis`, essais A3 à A7 et A17) : clé de bonne forme ; registre propre distinct de
`registres/scellements-v1.md`, de son journal et des deux registres de P3-bis ; clé **absente** du registre de T0.7 ;
exactement une ligne de la clé, au format `| CLÉ | AAAA-MM-JJTHH:MM:SSZ | chemin relatif | sha256 |` ; date **strictement
antérieure** à l'instant du contrôle ; fichier cité présent, empreinte égale à la ligne et au compagnon
(`registre_v1.verifier_lignes`). Le contrôle se joue une minute avant l'appel ; l'appel suit dans le même bloc, ce qui borne
l'écart entre la condition vérifiée et l'ouverture.

## 4. Contrôle à blanc du lecteur de registre de T0.7 sur une copie de l'état actuel

- **Commande** (lecture seule ; copie de `registres/scellements-v1.md` et de son journal dans le bloc-notes ; racine = le
  dépôt, hachage seul) : sortie brute versée, `controle-a-blanc-etat-actuel-sortie-v1.txt` (2026-11-14T11:29:41Z ; script
  `eb19ef6a…` ; registre copié `6ea1e624…`, journal copié `84545298…`, `main` local `f32bbdff`).
- **Résultat** : configuration v8 conforme ; **aucune clé refusée** ; exigées présentes 7 sur 9 ; **manquent
  `AUDIT-FUITES-T07` et `ISSUE-MOTS-ET-COUT-T06`** ; ignorées `SCELLEMENT-T08-BASE-A`, `GEL-T08` ; lignes vérifiées 8 sur 11
  (les trois autres citent des fichiers de 7b et de l'étape A, absents de `main` : à rapatrier) ; antériorité de
  `SCORES-T07` et `SONDES-T07` sur `VERDICT-P3BIS` : oui ; garde adaptée : aucun code ; `CODE-T07` : 26 fichiers conformes ;
  fichiers de données : absents (à rapatrier) ; `lecture-t07.json`, `arret-etape-b.json` : absents ; condition d'ordre de B
  bis : non remplie (registre propre absent). Bilan : 0 refus, 12 manques ; code 0 (mode rapport).
- **Essai R5 du script** : `essai_controle_a_blanc_etape_b_compte_3_v1.sh`, sortie `essai-controle-a-blanc-etape-b-compte-3-sortie-v1.txt`
  (11:29:24Z → 11:29:30Z) : **28 conformes sur 28** — racine jouet saine (code 0), clés à marque `T06` et `T08` futures
  (`CODE-MOTS-ET-COUT-T06`, `LECTURE-T08-BASE-A`) ignorées ; artefacts : clé `SCELLEMENT-VADAPT`, famille des jeux sous la
  marque `T08`, registre de B bis absent, plan daté après l'instant, plan altéré, clé de B bis écrite aussi au registre de
  T0.7, registre de B bis égal à celui de T0.7, `VERDICT-P3BIS` avant les scores, audit avant sa consigne,
  `lecture-t07.json` présent, `lecture-sondes-t06.json` présent, `ISSUE-MOTS-ET-COUT-T06` absente, clé en double, compagnon
  faux, configuration altérée, instant avant une ligne, clé de B bis hors forme, appui faux et ouverture pleine avant la fin de
  l'étape A au journal de P3-bis, ouverture réduite (chemin non couvert) ; registres réels (copie) : aucun refus, deux clés
  manquantes, mode « avant l'étape B » incomplet ; registre réel inchangé.
- **Conséquence pour les lignes à venir** (vérifié sur le code, `classer_cle_inconnue`, l. 138-149) : `CODE-MOTS-ET-COUT-T06`,
  `LECTURE-T08-BASE-A`, `SCELLEMENT-T08`, `CODE-T08` portent une marque déclarée et seront ignorées ; toute clé sans marque
  déclarée (`SCELLEMENT-VADAPT`, `SCELLEMENT-PLAN-BBIS`, une clé de verdict comme `VERDICT-T07` ou `VERDICT-7B`) ou portant
  `T07` sans être une clé de T0.7 **ferait refuser l'étape B** : aucune ligne de verdict de 7b ou de l'étape B dans
  `registres/scellements-v1.md` avant l'étape B (après, sans objet pour l'étape B, unique ; à éviter quand même pour toute
  lecture ultérieure par ce module).

## 5. Données et branches à rapatrier (tailles, disque)

| branche (tête lue au distant, 11:12Z) | fichiers (liste positive) | octets | quand |
|---|---|---|---|
| `calcul/t06-confirmation-7b-v1` (`55c3e3eb…`) | P1.4 (table A) : 6 fichiers et compagnons + `traces/t06-20261112-051655-1Xzh/` | ≈ 19,0 Mo | phase A |
| même branche | P5.2 (étape B) : 5 fichiers et compagnons (sans `distillation-t06.json` ni traces) | ≈ 18,96 Mo | phase C |
| `donnees/t07-etape-a-v1` (`0c176db5…`, déjà connue du clone de la mère) | manifeste, `sondes-t07.json`, 3 morceaux de `scores-actions-t07.npz`, leur manifeste et compagnons, compagnon du fichier entier ; recomposition | 132,2 Mo + 132,1 Mo recomposés | phase C |
| `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1` (`c7484c43…`) | trois fichiers du découpeur, lus par `git show` (consigne § 6.1) | non mesuré (petit) | audit, chez la mère |
| aucune | environnement avec torch (`requirements-cpu.txt`) si absent | ≈ 6 Go | phase C |

Récupération toujours par refspec explicite, dépôt jetable sans contenu (`--filter=blob:none --no-checkout --depth 1`), puis
extraction de chemins nommés seulement ; aucune liste récursive d'un dossier qui contient un chemin interdit.

## 6. Qui a lu quoi (préparateur)

À inscrire par la mère en v2 : **ce préparateur** (sous-agent de la session mère, modèle A) a lu le texte scellé de T0.7
(plan point 8, lignes de registre, concordances), son addendum, la consigne d'audit, T0.6 scellé (plan, critères, liste
d'arrêt, concordance, DT), la base (A) de T0.8, le code de lecture de T0.7 ; il a relevé les noms et tailles des fichiers des
dossiers des runs sur les branches de 7b et de l'étape A (aucun contenu) et haché, par le contrôle à blanc, les fichiers cités
par le registre présents sur `main` ; aucune sortie de 7a, 7b ou T0.7 ouverte. Exclu de tout rôle de lecteur et de juge des
verdicts de 7b, de l'étape B, de l'étape B bis et de G0 ; auteur de la commande et du contrôle à blanc, donc exclu de leur
contre-lecture.

Fin de rédaction : voir `rapport-preparateur-v1.md`.
