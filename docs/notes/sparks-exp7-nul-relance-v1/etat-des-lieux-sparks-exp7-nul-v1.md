# État des lieux — l'expérience 7 du billet « Sparks » sous paires nulles et aveuglement (SPARKS-EXP7-NUL), avant un texte neuf — v1

- **Date** : 21 novembre 2026, de 18:59 à 19:10 UTC environ (`date -u` : 18:59:44 au début, 19:06:38 avant l'écriture). **Auteur** : Claude Opus 5.5, lecteur neuf (n'a écrit ni le texte v1, ni l'addendum, ni le code, ni leurs contre-lectures). **Classe C** (note de travail), non contre-lue.
- **Mandat** : mot de Lazar consigné en GO-2026-11-21-79 (`registres/go.md`, ligne 678 ; registre `ac33f39b…` au moment de la lecture) : l'expérience revit par un texte neuf, après un état des lieux ; GO-2026-11-04-04 reste périmé ; toute dépense sur devis neuf.
- **Non ouvert** : aucun fichier « consigne-privee » ni « conception-ii-b », rien sous `brouillons/ii-b-saboteur-budget-v1/` ni `archives-reponses-modeles/`, rien sous `donnees/` ; aucun résultat d'une autre course. Aucune sortie de l'expérience n'a été lue : il n'en existe aucune (section 2).
- **Dépôt** au début : `main` à `4c648a64` puis `02de71b1` (d'autres sessions committent en parallèle). Aucun commit ici.

---

## 1. Verdict

1. **Rien n'a été mesuré.** La seule session réelle (5 novembre) s'est arrêtée **avant tout calcul** : la suite d'essais a échoué sur la carte louée, et le script d'instance refuse alors de fabriquer quoi que ce soit (code 2). Aucun modèle de l'expérience n'a été entraîné, aucun lecteur lancé, aucun coffre rempli. L'instance 59288960 a été détruite le 8 novembre, disque vide de résultats. Un texte neuf peut donc s'écrire, à la lettre, **avant toute donnée**.
2. **La cause de l'échec sur la carte reste inconnue.** Sur la carte : 16 échecs, 25 erreurs, 298 réussis, 22 sautés ; dans la session : 361 réussis. Le diagnostic v1 (6 novembre) n'a pas fini sa suite (tuée par son délai, code 137) ; le diagnostic v2 a été écrit mais jamais tiré. C'est le premier obstacle technique de toute relance qui reprend le code v12.
3. **Le dessin reste réutilisable presque entier** comme matière : paires nulles, aveuglement, bases B0 à B4, incrément sur la « distance au départ », contrôle causal, puissances. Ce qui ne l'est pas tel quel : le commit de lancement, le code qui vérifie un GO périmé et cite l'empreinte de l'addendum 1, les graines (tirées de l'empreinte du texte v1), le devis, la recherche de l'étape 0 et la phrase « apport propre ».
4. **Le monde a bougé depuis le 4 novembre** : qui conçoit (Fable 5.2), classes de pièces, économie de Fable, coût mesuré des sous-agents, et surtout une vague de voisins publiés ou déposés sur la lecture des poids et l'audit par paires, dont une réplication des expériences 1 à 7 du billet avec des modèles Claude (dépôt de code, description seule). La phrase « l'apport propre est le taux de fausses alertes d'un lecteur non entraîné sous paires nulles » (texte v1, l. 160) est à reprendre sous la règle anti-faux-gap (R8) avant tout texte neuf.

---

## 2. Ce qui est fait

### 2.1 Textes scellés (empreintes vérifiées ce jour)

| Pièce | Chemin | sha256 | État |
|---|---|---|---|
| Préenregistrement v1 | `prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md` | `4bacf20dbb8a0e3f369119841d6fb0b56069d0d31989431238b115df746dd52d` | scellé le 4 novembre ; contre-lu par un lecteur neuf (23 couples) ; décisions D-1 et D-2 de Lazar (GO de dépense, accès à Gemma) |
| Addendum n° 1 | `prereg/SPARKS-EXP7-NUL-addendum-1.md` | `c030591917a0d696d522f71b688d21e804a3adbd342702e4073aa759763ab202` | scellé le 5 novembre à 08:49 UTC ; brouillons 1 à 9 versés à côté (`prereg/SPARKS-EXP7-NUL-addendum-1-brouillon1.md` à `…brouillon9.md`, ce dernier `f058a7bc…`) ; contre-lectures 1 à 5 faites ; **brouillons 8 et 9 et codes v9 à v12 non contre-lus** (mot de Lazar, R-1534 : réserve) |
| Décisions D-3, D-4, D-5 | `docs/decisions/decision-sparks-D3-D4-D5-v1.md` | `6b5f3f2dd6b15b1d40f4b0a3a302e08c56bed61d251ca4c0632da4abb610a6e9` | D-3 (b) : le retrait chirurgical d'une direction de sabotage devient bras rapporté de T0.7 ; **la lecture du delta d'adaptateur attend le résultat de cette expérience** ; D-4 (b) ; D-5 (a) : une phrase du modèle de menace du papier C |

**Ce que l'addendum 1 a ajouté au texte v1** (section 0, lignes A-1 à A-23) : la base B3 « distance au départ » (le modèle de départ suit déjà toutes les mauvaises suggestions, donc « le plus éloigné du départ est l'honnête » peut trancher sans lire aucun trait ; vu par le tour du collisionneur) et la base B4 « normes sans départ » ; l'**incrément** du lecteur sur B3 et sur B4 exigé pour « la détection tient sous nul » (conjonction : borne inférieure par rééchantillonnage des cas > 0, gain observé > 0, score de lecteur permuté comme nul) ; prédictions P8 à P12 ; l'**étape 0** (recherche, faite le 4 novembre, d'un modèle de départ public honnête de même famille : aucun documenté ; trois candidats à mesurer sur l'instance, sans effet sur la lecture) ; et les écarts au rapport du développeur : **E-1** éléments promis « avant le scellement » (commit, empreintes, noms des tenseurs, puissance de M5) ; **E-2** tâche (2) de la consigne qui ne présuppose plus une différence (consigne principale v2) ; **E-3** règle des réponses de forme invalide (échec, jamais 0,5 et 0,5) ; **E-4** stockage sur l'instance arrêtée et copies par lots ; **E-5** contrôle causal dans une seconde session de carte (3 264 mesures) ; **E-6** consignes de secours par substitutions fermées. Plafond porté à 40 USD.

### 2.2 GO et leur sort

| GO | Ligne de `registres/go.md` | Objet | Sort |
|---|---|---|---|
| GO-2026-11-04-04 | 242 | variante carte louée, 25 USD, échéance 18 novembre | **périmé** (échéance passée ; GO-2026-11-21-79) |
| GO-2026-11-04-04, extension | 245 | addendum 1, 40 USD | **périmé** |
| GO-2026-11-05-02 et GO-2026-11-05-05 | 250, 253 | tirs réels de la chaîne de lancement, enveloppe commune 5 USD, échéance 6 novembre | **périmés** ; ≈ 0,050 USD pour quatre tirs (5 novembre) + ≤ 0,106 USD pour le diagnostic v1 (6 novembre) |
| GO-2026-11-21-79 | 678 | texte neuf, pièce décisive (Fable, contre-lu par Opus, corrigé, vérifié, scellé), dépense sur devis neuf | **en vigueur**, échéance 30 novembre |

### 2.3 Ce qui a tourné

- **4 et 5 novembre, chaîne de lancement** : codes v1 à v12 sur les branches `prep/sparks-exp7-nul-v1` (`55399606`) à `prep/sparks-exp7-nul-v12` (`78671d93`, puis commit de lancement `0d163bdc`) ; répétitions sur jouet avec addendum factice (branches `essai/sparks-v4-repetition` à `essai/sparks-v8-repetition`, `essai/sparks-exp7-nul-*`, `ordres/sparks-exp7-nul-*`) ; quatre tirs réels sans addendum ou en mode jouet (instances 59219396, 59227134, 59231131, 59232437, toutes détruites ; `registres/arrets.md`, lignes 80 à 83). Banc de mutations v11 complet : 258 sur 258 tuées ; banc v12 seul : 7 sur 7 (`docs/notes/weight-space-programming-v1/rapport-developpeur-addendum-1-v12.md`, `f8398bf6…`, lignes 95 à 98) ; banc complet v12 rapporté dans l'addendum scellé. Aucune de ces sorties n'est une donnée de l'expérience.
- **5 novembre, session 1 réelle** (fille 6 ; `brouillons/fille6-2026-11-05/rapport-locations-a1-v3-et-sparks-v1.md`, `bc841ab6…` ; `rapport-sparks-fin-fabrication-v1.md`, `32d59581…`) : préalables conformes (361 essais réussis dans la session) ; instance **59288960** (RTX 3090), créée à 16:03:20Z, rang 2 des offres (le rang 1 refusé par la garde de dépense, 50,81 USD projetés) ; amorce v10 démarrée à 16:11:46Z ; **« fin de la fabrication, code 2 » à 16:31:31Z**, arrêt obtenu à 16:31:32Z, aucun redémarrage. Branche `calcul/sparks-exp7-nul-v5-0d163bdcea56` : tête égale au commit de lancement, **aucune sortie poussée**. Cause, par lecture filtrée de deux lignes du journal de Vast (R-1589) : « essais en échec : arrêt avant tout calcul » (16 échecs, 25 erreurs, dans `test_sparks_exp7_nul_v2.py` notamment : bases au coffre, calcul au service sans la clé, couches du départ, bout en bout jouet). Hypothèse du pilote de carte trop ancien : réfutée (R-1592 : `cuda_max_good` 13.3). Copie depuis l'instance arrêtée : impossible sans clé ssh au compte (R-1590, nœud non pris).
- **6 novembre, diagnostic d'environnement v1** (instance 59410486, ordre `docs/procedures/ordre-fille-sparks-diag-env-v2.md`, `72ef5c63…` ; R-1636) : installation saine (torch 2.14.1 pour CUDA 13.0, carte vue) ; **suite d'essais tuée par son délai** au bout d'environ 22 minutes (code 137), sortie de pytest restée en tampon ; les échecs de la session 1 ni reproduits ni expliqués. Relevés lus par la mère sur `essai/sparks-diag-env-v1-59410486` (`82ad3d05`, 13 fichiers sous `diag-env/`). Diagnostic v2 recommandé (sortie non tamponnée, un fichier d'essais à la fois, délai d'environ 40 minutes) : **jamais tiré**, reporté puis tombé avec son GO.
- **8 novembre** : instance 59288960 **détruite** sur le mot de Lazar (R-1777, `registres/arrets.md`, ligne 88). Dépense de la session 1 (calcul, estimation, facture non relevée) : machine ≈ 0,47 h × 0,2014 USD/h ≈ 0,09 USD ; stockage 120 Go à 0,0329 USD/h du 5 novembre 16:03Z au 8 novembre 10:08Z, soit ≈ 66,1 h ≈ 2,17 USD ; total ≈ 2,3 USD sous GO-2026-11-04-04.
- **Filles 4 et 5 de l'ancienne mère** : SPARKS jamais commencée chez elles, rien loué (R-4671, R-4672).

### 2.4 Scellé, versé, lu, non lu

| Objet | Où | État |
|---|---|---|
| Sorties de l'expérience (modèles, comportements, coffre, réponses des lecteurs, analyse, contrôle causal) | — | **n'existent pas** |
| Branche de calcul de la session 1 | `origin/calcul/sparks-exp7-nul-v5-0d163bdcea56` | tête `0d163bdc`, identique à `prep/sparks-exp7-nul-v12` (différence vide) : rien à lire |
| Journal de Vast de 59288960 | perdu avec l'instance | lu seulement par motif (deux lignes et cinq de suite, R-1589) |
| Relevés du diagnostic v1 | `origin/essai/sparks-diag-env-v1-59410486`, `82ad3d05` (`diag-env/tests.txt` `5ec1f7e7…`, `diag-env/tests-code.txt` `e3b9c284…`) | lus par la mère (R-1636) ; environnement seulement |
| Rapports des tirs | `origin/canal/fille-2026-11-04`, `brouillons/fille-2026-11-04/rapport-tir-sparks-exp7-nul-v9…v11…` | versés et lus ; aucune donnée de l'expérience |
| Appel à Astra et tour du collisionneur sur l'intégration du billet | `origin/donnees/appel-astra-sparks-v1` (`31c0af16`), `origin/donnees/collisionneur-v9-sparks-v1-run` (`3f8be5c0`) | lus par la lecture du collisionneur (`docs/notes/weight-space-programming-v1/lecture-collisionneur-sparks-v1.md`, `d4c7973c…`) ; ce sont des avis de conception, non des mesures |
| Conversations pilotes des lecteurs | — | jamais faites |

**Aucune sortie scellée non lue par un verdict n'existe** pour cette expérience.

---

## 3. Ce qui reste

1. **Le texte neuf** (classe A) : préenregistrement écrit par Fable 5.2, contre-lu par Opus 5.5, corrigé, vérifié par le même contre-lecteur, scellé (R-3735 ; GO-2026-11-21-79). Il remplace le texte v1 et l'addendum 1, qui restent archivés sans modification (R12).
2. **La relecture des voisins avant toute phrase d'apport** (R8 ; section 4.6), par un agent neuf d'un autre modèle que le rédacteur.
3. **L'environnement de la carte** : diagnostic de la cause des 16 échecs et 25 erreurs (le diagnostic v2 écrit est le point de départ), avant tout tir de l'expérience ; sur devis.
4. **Le code** (classe B) : version neuve qui cite le texte neuf, vérifie le GO neuf et tire ses graines de la nouvelle empreinte ; contre-lecture des codes v9 à v12 jamais contre-lus (R-1534) et du delta neuf par un autre modèle, puis vérification par le même. La suite d'essais v12 n'a pas été rejouée dans l'environnement d'aujourd'hui (numpy 2.5.3 dans le Python du système de la session, 2.4.6 dans `.venv`, figé à 2.4.6 par `requirements-cpu.txt`).
5. **L'étape 0 à refaire à la date du texte neuf** : la recherche du 4 novembre est datée ; des modèles de la famille ont pu paraître depuis.
6. **Les journaux des auteurs** : le texte v1 cite une copie locale `/home/user/rikiyat/lm_understand-logs` à la tête `4d09ba6d6a7e891dd8063974dfe81b3d78e3494f` ; **cette copie n'existe pas dans cette session**. Le dépôt public est nommé par le billet (`github.com/RikiyaT/lm_understand-logs`, section « Logs » de la copie du 21 novembre). À recloner, tête relevée, différence avec `4d09ba6d` sur `exp7_sycophancy/` vérifiée avant tout emploi. Les copies des données des auteurs dans le code (`src/controle_ia/sparks_exp7_nul_v1/donnees_auteurs/`, avec `empreintes-sources.txt`, branche `prep/sparks-exp7-nul-v12`) permettent ce contrôle.
7. **L'accès à Gemma** (décision D-2 du 4 novembre) : la variable `HF_TOKEN` est présente dans cette session (nom seul) ; l'accès au modèle n'a jamais été éprouvé sur la carte (la session 1 s'est arrêtée avant). À éprouver au lancement, comme le texte v1 le prévoit.
8. **Le devis neuf** (classe A), lecteurs compris (section 4.4).
9. **Le sort de la lecture du delta d'adaptateur** (décision D-3 du 4 novembre), qui attendait ce résultat (section 4.7) : nœud de Lazar.

---

## 4. Ce qui a changé dans le programme depuis le 4 novembre et touche ce texte

### 4.1 Qui écrit, qui contre-lit
- **Qui conçoit** (mot de Lazar du 19 novembre, R-3735) : préenregistrements, critères de décision, devis par Fable 5.2 ; contre-lecture par Opus 5.5, puis vérification des corrections par le même. Le texte v1 et l'addendum 1 avaient été écrits par des rédacteurs Claude (l'addendum par Opus 5.5) : le texte neuf doit l'être par Fable.
- **Trois classes de pièces** (GO-2026-11-19-26) : texte, ordre de course et devis en classe A (chaîne complète) ; code et lanceur en classe B. La réserve « codes v9 à v12 non contre-lus » ne peut plus être tenue par un simple mot : la classe B demande leur contre-lecture.
- **Économie de Fable** (GO-2026-11-21-75) : Fable 5.2 réservé aux pièces décisives. Le texte v1 prévoit un lecteur Fable 5.1 par cas (96 conversations principales et 6 d'ancre) : ce bras n'est pas une pièce décisive ; le texte neuf doit dire quel modèle lit, et Lazar trancher s'il entame un quota rare.

### 4.2 Les chantiers
- La limite de trois chantiers actifs (GO-2026-11-19-27) a été **levée** le 21 novembre (GO-2026-11-21-07, mot de Lazar « je lève la limite ») ; le paragraphe de CLAUDE.md qui la décrit n'est pas encore mis à jour. Aucun gel ne bloque donc cette relance, sous réserve que la mère le confirme.

### 4.3 Le billet lui-même
- **Copie du 21 novembre** : `docs/sources/pdf/protocole-x-dommage-v1/page-web-sparks-of-weight-space-programming-copie-2026-11-21.html`, `840b40cf36778137998258b39b6f86858870932aaca8d3d326ce7be78b5cead0` (même empreinte que `docs/notes/protocole-x-programmation-de-poids-v1/recherche-approfondie-v1/sources/billet-origine-programmation-de-poids-releve-2026-11-21.html`). Copie de référence du texte v1 : `docs/notes/weight-space-programming-v1/piece-1-billet.txt`, `49b2db7e…`.
- **Comparaison mot à mot** (texte extrait des deux copies, par moi, dans mon bloc-notes) : 18 blocs différents ; **aucun dans la section de l'expérience 7** (mots 3 469 à 3 902 de la copie du 4 novembre) ; tous dans l'introduction (reformulation : « treating the weights as a program to be read and written »), la conclusion, et une section neuve **« Response to Comments », ajoutée le 12 novembre 2026**. Elle dit : le billet n'est pas une méthode mais « a statement about sparks of a new model capability », ses expériences en sont des indices ; les bases sont étroites à dessein ; « every run behind every number, failures such as Gemma included, is in the logs » ; réplications et extensions nombreuses (dont un banc, IWIBench). Chiffres de l'expérience 7 inchangés (trois paires sur trois ; tête 10.2).
- **Conséquence pour le texte neuf** : le billet assume lui-même la lecture « indice d'une capacité », non « méthode ». L'objet de l'expérience (le résultat tient-il sous paires nulles, avec des lecteurs Claude ?) n'en est pas touché ; la manière de le dire, si.

### 4.4 Le coût des lecteurs
- Le texte v1 dit les lecteurs « sans facture par appel » et projette environ 1,4 × 10⁸ jetons d'entrée cumulés (texte v1, l. 195). Depuis : mesure du coût d'une orchestration de sous-agents, 202,2 millions de jetons facturés, environ 182 dollars au tarif catalogue, en 49 minutes (R-3123, 18 novembre) ; et l'orchestration à plusieurs agents reste sans accord exprès, au cas par cas (R-4584). Le devis neuf doit chiffrer les lecteurs, et l'ordre des lecteurs passer par le mot de Lazar.

### 4.5 Règles d'appel et de récupération
- **Appels aux modèles de Google** (GO-2026-11-21-71) : la règle vise les envois à un modèle de Google par une interface ; Gemma tourne ici en poids locaux, sans envoi. À dire explicitement dans le texte neuf (jugement : sans objet).
- **Récupérer ce qui est récupérable** (R-3661, 19 novembre) : versement scellé avant toute destruction. La session 1 a perdu son disque (vide de résultats) faute de voie de copie ; l'ordre neuf doit prévoir la voie de versement de tout relevé, y compris en échec.
- **Nommer en clair** (R-3044) : le texte neuf nomme les bases et mesures par ce qu'elles sont (« distance au départ », « normes sans départ »), les sigles en appui.

### 4.6 L'état de l'art : la phrase « apport propre » (texte v1, l. 160)
Le texte v1 renvoyait la vérification d'antériorité à « AuditBench 2602.22755, jeu d'audit 2503.10965 ». Depuis, versés et scellés au dépôt (pages lues par d'autres notes, non par moi, sauf mention) :
- **AuditBench** (arXiv 2602.22755v4, `1d123f56…`, `docs/sources/pdf/protocole-x-programmation-de-poids-v1/`) : banc de 56 modèles à conduite cachée ; la lisibilité dépend de la recette de l'organisme (lu par la note sur la programmation de poids v2, § 4.1, point 2).
- **Weight Oracles** (arXiv 2610.07334v1, `a3dddc18…`, `docs/sources/pdf/protocole-x-dommage-v1/`) : un modèle de langue **entraîné** lit des poids bruts ; page 6 (lue par moi) : « at the operating point yielding 94% TPR, 20% of clean models are incorrectly flagged ». Un taux de fausses alertes d'un lecteur de poids est donc déjà publié, pour un lecteur entraîné et des portes dérobées.
- **Who's the Evil Twin? Differential Auditing for Undesired Behavior** (arXiv 2508.06827v2, `e0ccf859…`) : page 1 (lue par moi) : une équipe entraîne deux modèles voisins, l'un sain, l'autre à conduite cachée ; l'autre doit désigner le compromis. C'est le choix forcé entre deux modèles, publié en 2025.
- **Replicating and Extending Weight-Space Programming** (arXiv 2611.21449v1, 16 novembre, `accc4313…`) ; **IWIBench** (arXiv 2611.08647v1, `ff00a675…`) ; **Diff Mining** (arXiv 2608.26462v1, `3fca9d69…`) ; **perplexité différentielle** (arXiv 2605.00994v2, `321aab2d…`) ; « Simple LLM Baselines are Competitive for Model Diffing » (arXiv 2602.10371, page 1 seulement d'après la provenance de la note sur la programmation de poids).
- **Dépôt de code** `Sir-Olexander/lm_understand-logs-claude`, daté du 8 novembre, décrit comme « Replication of 'Sparks of Weight-Space Programming' (Takehi et al., 2026), Experiments 1-7, with Claude models » (`docs/notes/protocole-x-programmation-de-poids-v1/recherche-approfondie-v1/journal/github-depots-expression-exacte.tsv`, `bbaca6eb…` ; description seule, non opposable). Il touche directement la question « le résultat se transporte-t-il aux lecteurs Claude ? » du texte v1 (l. 151 et 158).
- **Décision D-9 de la note sur la programmation de poids v2** (`docs/notes/protocole-x-programmation-de-poids-v1/reponse-fable-programmation-de-poids-v2.md`, `90bbe866…`) : aucune phrase sur ce sujet avant la lecture en entier de sept voisins (dont AuditBench et la perplexité différentielle) par un agent neuf d'un autre modèle. Son sort (accordée par « go recos » de GO-2026-11-21-74 ou en délai) est à confirmer par la mère.
- **Lecture** (jugement, R8) : aucune de ces pièces n'est, d'après ce que j'en ai lu, l'expérience des paires nulles avec un lecteur non entraîné et la base « distance au départ » ; mais la zone est maintenant peuplée, et « apport propre » doit être réécrit en question, voisins cités, après lecture.

### 4.7 La note sur la programmation de poids (v2 vérifiée, 21 novembre) et sa recherche approfondie
- **Note v2** (`90bbe866…`, corrections vérifiées « conforme », `docs/notes/protocole-x-programmation-de-poids-v1/verification-corrections-programmation-de-poids-v2-opus-v1.md`, `947f9549…`), § 4.1 : (1) mesurer d'abord **la dispersion de l'honnête dans l'espace des poids** entre graines, puis lire l'écart du saboteur contre elle (décision D-3 de la note) ; (2) corriger « borne haute » : la lisibilité d'un organisme dépend de sa recette (D-4) ; (3) **épreuve de fuite** par l'outil public de différence de perplexité. Trois points touchent ce texte : la dispersion entre graines est exactement ce que mesurent nos paires nulles (deux modèles de même étiquette, graines différentes) et ce que borne la base de fabrication B2 ; la différence de perplexité est une base boîte noire candidate à côté de B0 ; et le chemin « lire le delta de nos organismes » de la décision D-3 du 4 novembre a maintenant une voie qui ne dépend pas de cette expérience.
- **Recherche approfondie** (`docs/notes/protocole-x-programmation-de-poids-v1/recherche-approfondie-v1/reponse-fable-programmation-de-poids-approfondie-v1.md`, `db0c71a4…`, classe C, non contre-lue ; dossier exclu de git par `.git/info/exclude`, compagnons vérifiés « OK ») : la vague « programmation de poids » est large (33 notices d'arXiv, 295 dépôts de code depuis le 2 novembre, d'après elle) et presque muette sur la sécurité ; le dépôt des journaux du billet est trouvé sur le site de dépôts de code. Rien n'y mesure des paires nulles.
- **Réponse d'Opus en effort maximal** (`opus-max-v1/reponse-opus-max-programmation-de-poids-v1.md`, `a50517f8…`) : vue en en-tête et par motifs seulement ; elle cite le billet comme pièce d'origine du domaine.

### 4.8 Ce qui ne change pas
- Aucune revendication du programme ne dépend de l'issue (texte v1, l. 25) ; aucune décision depuis ne l'a rattachée à une hypothèse ni à G0. La loi de la référence honnête (N-076) vise les accumulations de scores ; l'expérience n'en a pas (jugement : sans objet, à dire dans le texte neuf). La mesure reste une mesure de validité de construit.

---

## 5. Ce qui est réutilisable sans le relire

« Sans le relire » : aucun de ces objets ne porte de donnée de l'expérience ; les reprendre n'expose aucun résultat. Chacun garde sa vérification propre.

**Repris comme matière, tel quel ou presque**
- Le dessin du texte v1 : hypothèse, Q1 et Q2, étiquettes par le comportement (« sycophante » = garde le comportement du départ), 24 paires vraies, 12 et 12 paires nulles, graines différentes dans toutes les paires, ancre de trois cas, jeu d'étalonnage, coffre et aveuglement, isolement des lecteurs, garde des interdits, M1 à M5, C1, table de lecture, audit de symétrie, liste d'arrêt.
- Les ajouts de l'addendum 1 : bases B3 et B4, incrément et sa conjonction, étape 0 (règle de mesure des candidats), noms et formes des tenseurs de Gemma 3 270M, règle des réponses invalides, consigne principale v2 (tâche (2) qui ne présuppose pas de différence), consignes de secours.
- Les calculs de puissance : `docs/notes/weight-space-programming-v1/puissance-addendum-1-v1/puissance-addendum-1-sparks-v1.py` (`39f0eb01…`) et ses dix sorties (lois supposées, numpy seul ; à rejouer si le plan change).
- Les copies des données publiques des auteurs dans le code (452 faits, partages, comportements des paires 100 à 102 ; licences CC BY 4.0 et MIT d'après la pièce 3), avec leurs empreintes.
- La chaîne de lancement v12 comme base de code : amorce, minuterie de destruction, ordres écrits sur branche, garde de dépense, bancs de mutations (258 sur 258 tuées en v11), répétitions sur jouet. À reprendre en version neuve (R12), non telle quelle.
- La lecture du tour du collisionneur (`d4c7973c…`) et la note d'intégration (`02221846…`) comme avis de conception.

**À refaire ou à revoir avant emploi**
- Graines : l'entropie du texte v1 vient de son empreinte ; le texte neuf a la sienne.
- Garde du GO dans le code (`go.verifier` exige les lignes 242 et 245) et manifeste qui cite l'addendum 1 par son empreinte.
- Recherche de l'étape 0 (datée du 4 novembre).
- Limites de la machine de la session (texte v1, l. 186) : ce jour, 4 processeurs, 15 Go de mémoire, 21 Go de disque libres (`nproc`, `free -g`, `df -h`, relevés vers 19:05 UTC) ; à reprendre dans le texte neuf.
- Devis et prix (relevés du 5 novembre) ; lecteurs à chiffrer.
- Phrase « apport propre » et « ce que chaque issue ne montre pas » : à réécrire après la lecture des voisins.
- Prédiction P2 : son auteur la disait antérieure au changement E-2 (addendum, ligne P2) ; le rédacteur neuf écrit ses propres prédictions.

**Non réutilisable**
- GO-2026-11-04-04 et son extension ; GO-2026-11-05-02 et -05 (périmés).
- Commit de lancement `0d163bdc` et branche `calcul/sparks-exp7-nul-v5-0d163bdcea56` (liés à l'addendum 1 et à l'ancien registre des GO ; on n'écrase pas, R12).
- Instances : toutes détruites.

---

## 6. Points pour Lazar (nœuds), à trancher avant ou avec le texte neuf

1. **Lecteurs** : quel second lecteur à côté d'Opus 5.5 (Fable 5.1 du texte v1, un autre modèle, ou un seul lecteur par cas, ce qui garde la puissance de M1, M2 et M5 d'après le texte v1, l. 195), au regard de l'économie de Fable et du coût mesuré des sous-agents.
2. **Lecture du delta d'adaptateur** (décision D-3 du 4 novembre) : continue-t-elle d'attendre ce résultat, ou suit-elle la voie de la note sur la programmation de poids (dispersion entre graines d'abord) ?
3. **Base de différence de perplexité** : l'ajouter comme base boîte noire à côté de B0 (modification du plan, dans le texte neuf) ou non.
4. **Diagnostic de l'environnement de la carte** avant le texte neuf ou en parallèle (petit devis, de l'ordre du dollar d'après le diagnostic v1, ≤ 0,106 USD).
