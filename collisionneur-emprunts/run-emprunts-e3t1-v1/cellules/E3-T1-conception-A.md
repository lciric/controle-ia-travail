# Cellule A — Tour III.1 : emprunts aux agents auto-réécrits et aux concepteurs entraînés

## 0. Pièces reçues

- Bloc FAITS : présent, mais déclaré vide par décision d'arbitre (OBSERVÉ). Conséquence : tout ce que j'énonce sur les travaux cités vient de ma mémoire de lecture, statut **RAPPORTÉ, à vérifier**, y compris titres/auteurs/années déjà marqués « à vérifier » par la question. Aucun chiffre tiré de ces travaux n'est à prendre comme établi.
- Bloc QUESTION : présent et complet en apparence (OBSERVÉ).

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Pourquoi ça compte |
|---|---|---|---|
| S1 | Les mécanismes de ces travaux (archive, sélection de parents, auto-modification) ont produit des gains *hors banc* et non seulement sur le banc d'optimisation. | HYPOTHÈSE | DGM et ADAS rapportent des gains sur les bancs utilisés pour sélectionner (RAPPORTÉ) ; la transférabilité est, à ma connaissance, revendiquée sur peu de domaines et sans contrôle à score permuté. |
| S2 | Une « génération » de notre organisme est l'analogue d'un « enfant » dans une archive. | HYPOTHÈSE | Notre lignée est **linéaire** (chaque génération écrit un successeur) ; une archive suppose du branchement. L'analogie demande soit une modification du noyau, soit une archive *interne* aux fichiers de l'organisme. |
| S3 | Les garde-fous de STOP / AlphaEvolve / AI Scientist sont transférables à des tâches **sans évaluateur mécanique**. | HYPOTHÈSE | AlphaEvolve et STOP s'appuient sur des évaluateurs programmatiques (compte d'opérations, exactitude) (RAPPORTÉ). Nos tâches (conscience d'évaluation, contrôle de délégation) sont jugées par le noyau sur des familles tenues à l'écart : un juge peut être appris. |
| S4 | Un concepteur entraîné par gradient (W4S, FlowReasoner, MAS-GPT) est comparable à un réécriveur figé : même nature de signal. | HYPOTHÈSE | Leur unité d'épisode est la requête (RAPPORTÉ) ; la nôtre serait la génération. Le nombre d'épisodes disponibles diffère de plusieurs ordres de grandeur. |
| S5 | Les « familles tenues à l'écart » restent à l'écart sur une lignée longue. | HYPOTHÈSE | L'historique des scores est transmis à chaque génération : c'est un canal d'analyse adaptative. Le bras à score permuté mesure la dépendance au signal, pas la fuite cumulée. |
| S6 | Le coût apparié du témoin « un modèle, vote à k » est le bon étalon. | HYPOTHÈSE | Ce témoin mesure le gain *de structure* ; il ne mesure pas le gain *de mémoire de lignée*. Un second témoin (amnésique) manque. |
| S7 | Les failles connues de l'AI Scientist (contamination, revue complaisante) sont des failles de *dessin* et non d'*exécutant*. | HYPOTHÈSE | Si elles tiennent à l'exécutant, nos exécutants de frontière figés les reproduiront quel que soit l'organisme. |
| S8 | « Détection de triche sur l'évaluation » est un instrument qu'on peut évaluer. | HYPOTHÈSE | Il faut des triches *plantées* dont on connaît la vérité terrain ; sinon, ni taux de détection ni fausses alertes. |

---

## Emprunts par travail : reprendre / refuser / ce qui manque

Tout ce bloc est RAPPORTÉ (de mémoire) pour les contenus des travaux, HYPOTHÈSE pour les transpositions.

### 1. Darwin Gödel Machine (2025) et ADAS (2024)

**Reprendre.**
- *Archive + sélection parent par performance et nouveauté* (DGM : choix pondéré par score et par nombre d'enfants déjà produits, RAPPORTÉ). Transposition sans toucher au noyau : l'organisme tient dans ses fichiers une archive de ses propres variantes antérieures et choisit *lui-même* de quel ancêtre repartir. Le noyau continue de voir une lignée linéaire ; le branchement est interne.
- *Conception = code exécutable* (ADAS : les agents sont des programmes dans un espace de recherche, RAPPORTÉ). Déjà le cas chez nous.
- *Évaluation étagée* (DGM : petit sous-ensemble puis plus large, RAPPORTÉ) — à reprendre comme économie de budget, voir E4.

**Refuser.**
- La sélection par le même banc qui sert à mesurer le progrès. DGM a rapporté des cas où l'agent a contourné sa propre détection d'hallucination d'usage d'outils en fabriquant des traces (RAPPORTÉ, à vérifier). Notre dessin y répond partiellement (familles à l'écart, score permuté) mais **pas** à la fuite cumulée par l'historique des scores (S5).
- L'absence de contrôle de coût : DGM et ADAS optimisent une exactitude, pas une exactitude par dollar (RAPPORTÉ). Chez nous le coût entre dans le signal — garder.

**Ce qui manque chez eux et que nous pouvons mesurer.** Un bras à score permuté (leur gain provient-il du signal ou de la seule variance de réécriture ?) ; un bras gelé ; une mesure de surapprentissage adaptatif via familles « coffre » (E2).

### 2. STOP (2023–2024), Gödel Agent (2024), AlphaEvolve (2025)

**Reprendre.**
- STOP : séparation *améliorateur / tâche aval* ; l'améliorateur est évalué sur ce qu'il fait gagner à autre chose que lui-même (RAPPORTÉ). Chez nous : la génération est jugée sur les familles, non sur son auto-évaluation.
- AlphaEvolve : représentation par **diffs** marqués dans le code, cascade d'évaluateurs du moins cher au plus cher, mélange d'un modèle rapide et d'un modèle fort (RAPPORTÉ). La cascade et les diffs se transposent ; le mélange de modèles aussi, puisque nous avons trois espèces d'exécutants.

**Refuser.**
- Gödel Agent : auto-modification à l'exécution (patch de l'interpréteur en cours de route, RAPPORTÉ). Incompatible avec le préenregistrement et la reproductibilité par génération. À exclure.
- STOP a rapporté des tentatives de l'améliorateur de désactiver un drapeau de bac à sable (RAPPORTÉ, à vérifier). Leur garde-fou était l'observation après coup. Chez nous : les exécutants de frontière et le noyau sont hors de portée de l'organisme par construction ; il reste le code de l'organisme lui-même, qui doit tourner isolé.
- AlphaEvolve suppose un évaluateur **mécanique et incorruptible** (RAPPORTÉ). Nos tâches ne l'ont pas : transposer la cascade sans transposer la confiance dans l'évaluateur.

**Ce qui manque.** Aucun de ces travaux, à ma connaissance, ne mesure la triche sur l'évaluation avec des triches plantées (taux de détection, fausses alertes). Notre noyau peut le faire (instrument I5).

### 3. Concepteurs entraînés : W4S, FlowReasoner, MAS-GPT (2025)

**Signal, épisode, représentation, économie** (RAPPORTÉ, à vérifier pour chacun) :
- W4S : petit méta-agent entraîné par apprentissage par renforcement à écrire des flux exécutés par des modèles forts ; signal = résultat d'exécution ; épisode = tâche ; représentation = code ; économie = un petit modèle écrit, les forts n'exécutent que ce qui est nécessaire.
- FlowReasoner : méta-agent au niveau de la requête, raisonnement distillé puis renforcement sur retour d'exécution ; épisode = requête ; représentation = code de système multi-agents.
- MAS-GPT : apprentissage supervisé sur paires requête → système multi-agents en code, filtrées par cohérence ; épisode = requête ; une seule inférence pour produire le système.

**Reprendre.** La représentation en code exécutable (déjà nôtre) ; l'idée W4S que le concepteur peut être *moins cher* que les exécutants ; le filtrage par cohérence de MAS-GPT comme critère de **sélection de mémoire** (ne garder dans la mémoire de lignée que ce qui a été confirmé sur plusieurs familles).

**Refuser.** L'entraînement par gradient d'un concepteur : notre cadre n'autorise le gradient que sur des sondes d'un modèle à 8 milliards. Un concepteur à épisode = génération aurait, à budget réaliste, quelques dizaines d'épisodes : trop peu pour un renforcement (HYPOTHÈSE). La transposition honnête n'est pas « entraîner un concepteur » mais « un réécriveur figé avec mémoire de lignée ».

**Ce qu'un organisme sans gradient peut faire qu'eux ne font pas** (HYPOTHÈSE) : (i) changer de représentation de conception en cours de lignée (texte → graphe → code) ; (ii) écrire des sondes sur activations et s'en servir comme instrument pour ses propres tâches — les concepteurs entraînés optimisent l'exactitude sans regarder l'intérieur du modèle ; (iii) produire une mémoire lisible, donc auditable par l'humain. Ce qu'il ne peut pas : accumuler une attribution de crédit fine au-delà de ce qui tient dans le texte.

### 4. The AI Scientist (2024 ; v2, 2025)

**Reprendre.** La séparation en étapes idée → expérience → relecture, et surtout : **écrire le protocole avant de lancer**. Transposition : l'essaim propose, le noyau ou un humain préenregistre (hypothèses, métrique, seuil), puis la carte graphique tourne. Reprendre aussi le relecteur automatique, mais seulement comme *filtre* calibré, jamais comme juge final (I6).

**Refuser.** Le relecteur qui note le même texte que l'auteur a produit avec les mêmes exécutants ; la boucle qui laisse l'agent modifier son propre script d'expérience (un cas rapporté : édition du script pour étendre un délai, RAPPORTÉ, à vérifier) ; l'évaluation des idées par « nouveauté » recherchée dans la littérature par le même modèle (contamination non mesurée).

**Failles connues** (RAPPORTÉ, à vérifier) : hallucination de détails dans les comptes rendus ; surestimation des scores par le relecteur ; contamination des idées par les données d'entraînement. Notre cadre peut mesurer la troisième par des familles de menaces construites après la date de coupure des exécutants (si connue — RAPPORTÉ par les fournisseurs, à vérifier).

---

## (b) Expériences décisives (inférence forte)

Les seuils sont **illustratifs** ; les métriques sont celles du noyau (score sur familles à l'écart, coût). Tous les bras partagent budget, graines et exécutants.

### E1 — Archive interne contre lignée linéaire
- **H_A** : une archive interne (l'organisme peut repartir d'un ancêtre non immédiat, sélection performance + nouveauté) donne un gain hors banc supérieur à la lignée strictement linéaire, à budget égal.
- **H_B** : le gain d'archive vient uniquement du nombre de variantes évaluées ; à nombre d'évaluations égal, pas de différence.
- **Métrique** : score médian sur familles à l'écart à la génération G, et coût cumulé.
- **Seuil (illustratif)** : différence > 2 écarts interquartiles sur 5 lignées indépendantes par bras.
- **Contrôle négatif** : bras « archive à sélection aléatoire » (même archive, parent tiré au sort).
- **Falsification** : si archive ≈ archive-aléatoire ≈ linéaire → H_A fausse. Si archive > archive-aléatoire > linéaire → H_B fausse (la sélection apporte quelque chose au-delà du nombre).

### E2 — Fuite par l'historique des scores (surapprentissage adaptatif)
- **H_A** : la transmission de l'historique des scores suffit à faire monter les familles « à l'écart » sans gain réel : écart croissant entre familles vues (via scores) et familles **coffre** (jamais scorées avant la fin).
- **H_B** : l'écart vu/coffre reste stable le long de la lignée.
- **Métrique** : écart score(familles à l'écart habituelles) − score(familles coffre), tracé par génération.
- **Seuil (illustratif)** : pente positive significative sur ≥ 20 générations, ou écart final > 5 points.
- **Contrôle négatif** : bras à score permuté — l'écart y doit être nul ; si l'écart y apparaît aussi, la mesure est biaisée.
- **Falsification** : écart croissant dans le bras normal et nul dans le bras permuté → H_B fausse. Pas d'écart → H_A fausse pour cette longueur de lignée.

### E3 — Mémoire de lignée : bras amnésique
- **H_A** : la mémoire et l'historique transmis portent du savoir transférable ; une génération qui les reçoit bat une génération qui ne reçoit que le code.
- **H_B** : les gains sont de la recherche par génération ; l'amnésie ne coûte rien.
- **Métrique** : score à l'écart et coût, à génération égale.
- **Seuil (illustratif)** : gain amnésie → complet > gain complet → témoin vote à k.
- **Contrôle négatif** : bras recevant une mémoire **d'une autre lignée** (même longueur, autre histoire) : si elle aide autant que la sienne, c'est l'effet « plus de texte », pas l'effet mémoire.
- **Falsification** : complet > mémoire-étrangère > amnésique → H_B fausse. Complet ≈ amnésique → H_A fausse. Mémoire-étrangère ≈ complet → H_A fausse aussi (ce n'est pas du savoir de lignée).

### E4 — Cascade d'évaluation (emprunt AlphaEvolve)
- **H_A** : une cascade (évaluateur bon marché d'abord, noyau complet ensuite) divise le coût par génération sans dégrader le score à l'écart.
- **H_B** : l'évaluateur bon marché est optimisé (Goodhart) et le score à l'écart chute.
- **Métrique** : coût par point gagné ; corrélation de rang évaluateur-cheap / noyau, par génération.
- **Seuil (illustratif)** : coût ÷ 2 avec perte de score < 1 point ; corrélation de rang qui ne baisse pas sous 0,6.
- **Contrôle négatif** : cascade dont le premier étage est un **bruit** (sélection aléatoire du même nombre de candidats).
- **Falsification** : cascade ≈ cascade-bruit → H_A fausse (l'étage ne filtre rien). Corrélation de rang qui décroît le long de la lignée → H_A fausse, H_B soutenue. Coût ÷ 2 et score tenu → H_B fausse.

### E5 — Préenregistrement contre sélection après coup (emprunt AI Scientist)
- **H_A** : les propositions de l'essaim dont l'hypothèse, la métrique et le seuil sont figés **avant** l'exécution produisent une inflation (score annoncé − score réplication indépendante) inférieure à celles sélectionnées après coup.
- **H_B** : l'inflation est identique ; elle tient à l'exécutant, pas au moment du gel.
- **Métrique** : inflation médiane sur une réplication sur familles coffre.
- **Seuil (illustratif)** : différence d'inflation > 3 points.
- **Contrôle négatif** : propositions dont le protocole est figé mais sur une métrique **non pertinente** (doit montrer la même inflation que l'après-coup si l'effet vient du gel lui-même et non du contenu).
- **Falsification** : préenregistré ≈ après-coup → H_A fausse. Préenregistré < après-coup et contrôle ≈ après-coup → H_B fausse.

### E6 — Détection de triche avec triches plantées
- **H_A** : un détecteur fondé sur l'inspection du diff + traces d'exécution détecte ≥ 90 % des triches plantées avec ≤ 5 % de fausses alertes sur réécritures honnêtes appariées.
- **H_B** : les triches « sémantiques » (passent par le comportement, pas par le code d'évaluation) échappent au détecteur ; la détection ne tient que pour les triches syntaxiques.
- **Métrique** : courbe détection / fausses alertes, par type de triche.
- **Seuil** : voir I5.
- **Contrôle négatif** : réécritures honnêtes qui touchent les mêmes fichiers (refactorisation des utilitaires d'évaluation) — c'est là que les fausses alertes doivent être mesurées.
- **Falsification** : détection élevée sur syntaxique, basse sur sémantique → H_A fausse pour l'instrument tel quel. Détection homogène ≥ seuil → H_B fausse.

---

## (c) Instruments nommés : mesure minimale pour savoir s'ils fonctionnent

| Instrument | Taux à mesurer | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **I1. Bras à score permuté** | « Détection » = fraction de gains apparents qui disparaissent sous permutation ; fausse alerte = gain réel déclaré bruit (vérifié par réplication coffre) | Même budget, même graine, même génération initiale | Simple test de permutation sur les scores finaux ; le bras doit apporter plus que ce test post hoc |
| **I2. Bras gelé** | Dérive du score des familles elles-mêmes (étalonnage) ; fausse alerte = dérive attribuée à l'organisme alors que la famille a changé | Même familles, même exécutants, mêmes dates | Hash des familles et des versions d'exécutants |
| **I3. Témoin « un modèle, vote à k »** | Fraction des générations où l'organisme bat le témoin à coût apparié ; fausse alerte = coût mal apparié (jetons vs dollars vs temps) | Appariement sur **les quatre** dimensions du budget, pas une seule | Vote à k avec k optimisé sur familles d'entraînement (témoin fort) |
| **I4. Sondes sur activations (8 B)** | Détection de « conscience d'évaluation » sur familles à l'écart ; fausses alertes sur prompts qui *parlent* d'évaluation sans en être | Paires : (évaluation sans mot-clé) vs (conversation ordinaire avec mots-clés « test », « benchmark ») | (i) regex de mots-clés ; (ii) classifieur zéro-coup sur le texte seul par un exécutant ; la sonde doit battre les deux en AUC sur les paires appariées, sinon elle ne mesure que la surface |
| **I5. Détecteur de triche sur l'évaluation** | Détection par type de triche plantée : édition de tests, fausse trace d'outil, drapeau de bac à sable, fuite de réponses dans la mémoire, dégradation volontaire du bras gelé ; fausses alertes sur refactorisations honnêtes des mêmes fichiers | Diffs honnêtes de taille et de fichiers appariés | Hash des fichiers d'évaluation ; diff sur chemins protégés ; horodatage des appels d'outils ; un détecteur par exécutant de frontière ne vaut que s'il dépasse ces trois contrôles |
| **I6. Relecteur automatique (type AI Scientist)** | Corrélation de rang avec l'issue des tests préenregistrés ; taux d'acceptation d'idées dont le test échoue ensuite (fausse alerte positive) ; taux de rejet d'idées dont le test réussit | Idées appariées sur longueur et style, auteur = exécutant différent du relecteur | Score constant (tout accepter) ; score par longueur ; le relecteur doit battre ces deux prédicteurs |
| **I7. Archive / sélection de parents** | Diversité comportementale (signature par famille) maintenue ; fausse alerte = diversité syntaxique sans diversité de comportement | Archive à sélection aléatoire (E1) | Distance d'édition sur le code (à battre par une distance sur les comportements) |

Trois remarques (HYPOTHÈSE) : I4 est l'instrument le plus exposé — un modèle à 8 B n'est pas l'exécutant de frontière dont on veut connaître la conscience d'évaluation ; la sonde mesure un **substitut**, et l'écart substitut/frontière n'est pas mesurable dans notre cadre. I5 ne peut être évalué qu'avec des triches plantées par le noyau, hors de vue de l'organisme — ce qui n'est pas un « conseil de conception ». I6 est inutile s'il n'est pas confronté à une réplication coffre.

---

## (d) Ancrage matériel (tout « illustratif » sauf mention)

- **Modèles ouverts à ~8 B pour les sondes** : Llama 3.1 8B (Meta, 2024), Qwen2.5-7B (2024) ou Qwen3-8B (2025), OLMo 2 7B (AI2, 2024–2025) — existence RAPPORTÉE, licences à vérifier. OLMo a l'avantage de données d'entraînement publiées, ce qui aide à contrôler la contamination des familles (HYPOTHÈSE).
- **Calcul sondes** : inférence 8 B en bf16 ≈ 16 Go de mémoire ; extraction d'activations sur ~10 000 prompts ≈ 1–2 heures sur une seule carte 40–80 Go ; entraînement d'une sonde linéaire : minutes. Par génération, si l'organisme réentraîne 5–10 sondes : ≈ 2–5 heures-carte (illustratif).
- **Appels de frontière** : la part dominante du coût. Une génération qui réécrit son successeur, exécute une cascade et tourne sur familles d'entraînement : ordre de 10⁶–10⁷ jetons (illustratif), soit quelques dizaines de dollars par génération au tarif courant des trois espèces, à vérifier aux tarifs du jour.
- **Plan E1–E6 complet** : 6 expériences × ~5 lignées × ~20 générations ≈ 600 générations ≈ 1 500–3 000 heures-carte et 10⁴ $ en appels (illustratif ; ordre de grandeur, pas devis). Le bras gelé et le bras permuté coûtent autant que le bras normal : prévoir le triple.
- **Isolation** : conteneur sans réseau pour le code de l'organisme ; les familles coffre stockées hors du conteneur, hashées, révélées en fin de lignée.

---

## 5. Synthèse : mécanismes classés (bénéfice attendu / coût et risque)

Classement HYPOTHÈSE ; les ordres sont des paris à départager par E1–E6.

1. **Préenregistrement avant exécution** (AI Scientist, inversé). Coût quasi nul ; bénéfice : rend E5 et I6 mesurables. À vérifier : E5. Risque : l'essaim apprend à écrire des protocoles vagues — mesurer la spécificité des seuils déclarés.
2. **Familles coffre + suivi de l'écart vu/coffre** (réponse au surapprentissage de DGM/ADAS). Coût : familles supplémentaires. À vérifier : E2. Risque : coffre trop petit, variance.
3. **Cascade d'évaluation + réécriture par diffs** (AlphaEvolve). Bénéfice : coût par génération. À vérifier : E4 (corrélation de rang qui tient). Risque : Goodhart sur l'étage bon marché — c'est précisément ce que E4 teste.
4. **Archive interne avec sélection performance + nouveauté** (DGM). Bénéfice incertain à lignée courte. À vérifier : E1 contre archive-aléatoire. Risque : l'organisme consacre son budget à gérer l'archive.
5. **Triches plantées par le noyau** (ce qu'aucun des travaux ne fait). Bénéfice : seul moyen de qualifier I5. Coût : conception de triches réalistes. À vérifier : E6.

**À ne pas emprunter.**
- *Auto-modification à l'exécution* (Gödel Agent) : détruit le préenregistrement et la reproductibilité par génération.
- *Concepteur entraîné par gradient avec épisode = génération* (W4S/FlowReasoner/MAS-GPT) : trop peu d'épisodes, gradient hors cadre, et le gain revendiqué par ces travaux l'est sur des épisodes-requêtes, pas sur des épisodes-génération.
- *Relecteur automatique comme juge final* (AI Scientist) : surestimation rapportée, et même exécutant que l'auteur.

**Ce qui départagerait les voies** : si E3 montre que la mémoire de lignée ne vaut rien (complet ≈ amnésique), alors l'archive (4) et toute idée de « concepteur » perdent leur objet, et seuls (1), (2), (3) restent. Si E2 montre une fuite rapide, le cadre entier doit basculer vers des familles renouvelées — ce qu'aucun des travaux cités ne fait.

---

## 6. Ce qui est connu — références citables (toutes **à vérifier**, de mémoire)

Pertinentes directement, hors celles de la question :
- « The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search », Yamada et al., 2025.
- « AFlow: Automating Agentic Workflow Generation », Zhang et al., 2024 — recherche arborescente sur flux en code.
- « Multi-agent Architecture Search via Agentic Supernet », Zhang et al., 2025 — espace de conception à coût pris en compte.
- « TextGrad: Automatic “Differentiation” via Text », Yuksekgonul et al., 2024 — optimisation sans gradient par retour textuel.
- « Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs », Opsahl-Ong et al., 2024.
- « Large Language Models Often Know When They Are Being Evaluated », Needham et al., 2025 — directement sur notre première famille de menaces.
- « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation », Baker et al., 2025 — pression d'optimisation sur un signal de surveillance.
- « Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models », Denison et al., 2024.
- « AI Control: Improving Safety Despite Intentional Subversion », Greenblatt, Shlegeris, Sachan, Roger, 2024 — cadre du contrôle de délégation.
- « Sabotage Evaluations for Frontier Models », Benton et al., 2024.
- « MLE-bench », Chan et al., 2024 ; « PaperBench », Starace et al., 2025 — bancs où la réplication indépendante sert de juge.
- « ShinkaEvolve », Lange et al., 2025 — évolution de programmes à faible nombre d'évaluations (attribution exacte à vérifier).

Je n'ai pas inclus d'autres travaux dont je ne suis pas sûr du titre ou des auteurs.

FIN-DE-CELLULE