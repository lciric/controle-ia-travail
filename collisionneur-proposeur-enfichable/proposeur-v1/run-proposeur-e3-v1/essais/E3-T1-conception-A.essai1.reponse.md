# Cellule A — tour III.1 : « proposeur enfichable » devant notre juge

## 0. Pièces reçues

C, S, E1, E2, D4a, D4b, D, N, M, K : toutes présentes et complètes selon leurs balises. K est explicitement servie en partie 1 seulement ; M est « position de conv-audit, non vérifiée » et son premier mot est coupé (signalé dans la pièce). Aucun contenu inventé pour les parties absentes. Je ne connais rien de « Agentic Scientist v3 » (S, M) hors de ce que ces pièces en rapportent ; je ne connais aucun chercheur automatique « de 2026 » : tout ce que j'écris sur la littérature est RAPPORTÉ de mémoire, à vérifier sur les PDF, sans identifiant arXiv (règle 3).

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| A1 | « Ce que les chercheurs publiés font mieux que nous, c'est proposer » | HYPOTHÈSE | Aucune pièce ne mesure un étage de proposition isolé. Les mesures publiées (voir (c), instrument P) portent sur des **papiers de bout en bout**, c'est-à-dire sur proposition × exécution × relecteur-modèle. La position de conv-audit rejette le relecteur mais crédite la proposition d'une valeur mesurée **à travers** ce relecteur : c'est une attribution non identifiable. |
| A2 | L'étage de proposition est **séparable** | HYPOTHÈSE | Dans les systèmes que je connais, la génération d'idées est couplée à un gabarit de code (AI Scientist v1), à une recherche arborescente (v2), à un tournoi noté par modèle (co-scientist). Séparer l'étage retire la boucle qui le sélectionne ; ce qui reste peut valoir moins que le tout, ou que rien. |
| A3 | Notre juge peut juger ce que ces étages produisent | RAPPORTÉ (K, partie 1 ; chiffres non opposables) | K lit dans le code que le juge ne sait juger qu'une loi catégorielle p(issue \| z, g) contre une bibliothèque aveugle aux traits, sur K = 3, d = 2, traits gaussiens. Une idée en texte libre n'est pas de cette forme ; la question le reconnaît (point 2) mais suppose qu'une traduction existe. Rien dans les faits ne la code. |
| A4 | « Le juge est figé, le proposeur ne peut pas apprendre à plaire » | HYPOTHÈSE | K relève deux canaux de texte non traités : les « leçons » de synthèse servies à tous les proposeurs/recombineurs de la génération suivante, et les fichiers libres copiés vers le vérificateur. Un juge figé n'empêche pas l'enfermement si le canal de rétroaction est le texte. |
| A5 | « Fiches promues par dollar » mesure le proposeur | HYPOTHÈSE | La promotion dépend de la puissance du juge, qui dépend du nombre de tirages et de traits : E1, T3 ε = 0,05, puissance 0,196 à 200 tirages sous v1 contre 0,909 sous v0 (VÉRIFIÉ en simulation) ; D4a, 0,53 → 1,00 selon traits et tirages. Le même proposeur change de score si l'on change la configuration du juge. De plus K lit que l'aptitude vaut −ln α pour toute survivante : « promue » est un bit, pas une mesure. |
| A6 | Le premier lancement réel (D, option a) informe le choix du proposeur | RAPPORTÉ (D, K) | Option (a) est un monde tautologique (K : « le monde **est** la loi de la fiche ») et la génération 0 vient d'un fichier (`--population`) : aucun rôle de formulation n'y tourne. Ce lancement mesure la plomberie, pas la proposition. Attendre son résultat pour décider du proposeur, c'est attendre une mesure qui n'existera pas. |
| A7 | Un vérificateur « d'un autre modèle » suffit | RAPPORTÉ (C, N, K) | C exige « une autre famille de modèles » ; N-053 (point 4) exige « une autre lignée » ; la contrainte de Lazar (question, 14:17) limite le côté Claude à Opus 5.5 et Fable 5.1 ; K lit que `valider` n'exige que deux **noms** différents. Si Opus et Fable sont de même lignée, la contrainte C/N n'est satisfaite que par un modèle hors Claude (N-053 cite Qwen2.5-7B comme juge d'autre lignée, RAPPORTÉ). |
| A8 | « Agentic Scientist v3 est écarté parce que ses agents héritent des clés » | RAPPORTÉ (S, M) | Je ne peux ni confirmer ni infirmer ; et l'argument est contingent : avec un modèle ouvert servi en local sur 127.0.0.1 (D, relais), il n'y a plus de clé à hériter ; reste le réseau. L'exclusion tient pour un déploiement, pas pour la catégorie « chercheur publié ». |
| A9 | « Hybride insensé = prendre leur relecteur » | HYPOTHÈSE | Leur relecteur est inutilisable comme **critère** (inflation, conscience d'évaluation : RAPPORTÉ dans la position, non chiffré ici). Mais comme **trieur avant le juge**, il pourrait économiser des tirages, qui dans l'option (c) coûtent des appels (K : coût du monde non budgété). Sa valeur de triage est une question empirique (expérience P5), pas une évidence. |

## (b) Expériences décisives (inférence forte, chaque issue falsifie)

Toutes sont faisables sur le monde à vérité connue des pièces (banque cachée, juge v1 + nul v2) et, pour celles qui exigent un espace d'idées réel, sur l'option (b) de D (rétrodiction arXiv 2003-2016, issues = années tenues à part). Les seuils sont **illustratifs** sauf mention ; chaque duel est précédé d'un étalonnage A/A (deux courses identiques) qui fixe le plancher de bruit, comme S le prescrit pour le critère de sélection.

### P1 — La valeur d'un proposeur de la littérature survit-elle à l'ablation de son relecteur ?

- **H_A** : l'étage de proposition isolé (idées brutes, sans son tournoi ni sa relecture) produit, sous notre juge et à budget égal, un taux de **classes promues non redites** par fiche gelée supérieur à celui d'un proposeur maison à même consigne.
- **H_B** : l'avantage mesuré dans les publications tient à la sélection par relecteur-modèle ; isolé, l'étage ne bat pas le nul (idées tirées au hasard de la mémoire, reformulées par le même traducteur).
- **Métrique** : classes distinctes promues (après fusion par la mémoire) / fiches gelées ; secondaire : fécondité (filles promues issues des fiches du bras à la génération suivante).
- **Seuil (illustratif)** : écart entre bras supérieur à deux fois l'écart A/A, et au moins 10 points de taux ; avec des taux de l'ordre de 0,30 contre 0,15, n ≈ 100 fiches gelées par bras (illustratif, à recalculer sur le bruit A/A).
- **Contrôle négatif** : un bras **mécanique sans modèle** (mutation de survivantes : permutation des traits, changement d'un coefficient) traduit par le même gabarit. Si ce bras égale les deux proposeurs, le juge et l'espace de traits dominent, et le choix du proposeur est sans objet.
- **Falsification** : H_A tombe si l'étage isolé ≤ nul + bruit ; H_B tombe s'il bat le nul et le maison. Issue annexe : si le bras mécanique égale tout le monde, l'hypothèse A1 et la métrique A5 tombent ensemble.

### P2 — La traduction idée → fiche conserve-t-elle l'idée ?

- **H_A** : une fiche traduite est ré-identifiable : un lecteur neuf (autre lignée) qui reçoit la fiche (loi, espace d'instances, prédiction signée) et k idées candidates (la source et k−1 leurres du même proposeur, même domaine) retrouve la source bien au-dessus de 1/k ; et les signatures prédictives des fiches issues d'idées distinctes sont distinctes.
- **H_B** : la traduction est un goulot : des idées différentes s'écrasent sur un petit nombre de lois (la mémoire les fusionne comme redites), ou la ré-identification est au hasard.
- **Métrique** : exactitude de ré-identification à k = 5 ; taux de fusion par la mémoire entre fiches issues d'idées distinctes (fausses fusions) ; taux de fusion entre paraphrases d'une même idée (vraies fusions, calibration).
- **Seuil (illustratif)** : ré-identification ≥ 0,70 à k = 5 ; fausses fusions ≤ 0,05 par fiche (le seuil que D4b vise) ; vraies fusions ≥ 0,90.
- **Contrôle négatif** : fiches produites par le gabarit **sans idée** (loi par défaut) : la ré-identification doit tomber à 1/k ; sinon le lecteur devine sur le style, pas sur le contenu.
- **Falsification** : H_A tombe si exactitude ≤ 1/k + bruit ou fausses fusions > 0,05 ; H_B tombe si les deux seuils tiennent. Comparer trois traducteurs (gabarit mécanique ; agent maison ; étage externe sous consigne) : la question 2 est une ablation, pas une opinion.

### P3 — Le proposeur apprend-il à plaire au juge par les canaux de texte ?

- **H_A** : avec le canal « leçons » ouvert, la population promue dérive sur les générations vers des lois proches des membres de la bibliothèque (divergence faible à 𝓛), à domaine étroit (couverture faible) ou à prédiction couverte ; sans le canal, pas de dérive au-delà du bruit A/A.
- **H_B** : aucune dérive mesurable dans les deux cas : le juge figé suffit, et les leçons peuvent rester.
- **Métrique** : par génération, médiane de la divergence déclarée à la référence × couverture (le « contenu » de S) des fiches promues ; part des fiches rejetées par le contrôle « pari couvert ».
- **Seuil (illustratif)** : pente négative du contenu sur cinq générations dépassant deux fois l'écart A/A.
- **Contrôle négatif** : leçons remplacées par du texte neutre de même longueur (placebo) ; et un bras où les leçons sont **structurées** (champs fixes, pas de texte libre).
- **Falsification** : H_A tombe si la pente avec leçons ne diffère pas du placebo ; H_B tombe si elle en diffère. Dans ce cas, N-053 point 5 (aucun score de moniteur dans un signal de sélection, « il vaut aussi pour la piste organisme ») impose de fermer le canal, pas de le régler.

### P4 — Les fiches jumelles contournent-elles la mémoire ?

- **H_A** : des jumelles construites pour ne différer de fiches archivées qu'**hors** de la sonde de la mémoire (K : 256 instances gaussiennes) sont refusées à ≥ 0,95.
- **H_B** : elles passent ; la mémoire mesure la loi sur un sous-espace et le proposeur peut vivre dans le complément.
- **Métrique** : taux de refus des jumelles plantées ; taux de refus de vraies filles neuves (fausses fusions).
- **Contrôle négatif** : copies exactes (D4b : « une copie exacte reste reconnue », RAPPORTÉ) ; vraies filles neuves à quatre traits (D4a : 5 à 6 refus sur 23 à 24).
- **Falsification** : symétrique. Si H_B, la signature doit être prise sur les instances **du plan gelé** (celles que `selection_divergence` choisit), pas sur une sonde fixe.

### P5 — Leur relecteur vaut-il comme trieur avant notre juge ?

- **H_A** : le score du relecteur-modèle (ou l'Elo du tournoi) sur l'idée source prédit la promotion par notre juge (aire sous la courbe ≥ 0,70, illustratif) ; utilisé comme filtre au quantile 0,5, il économise la moitié des tirages pour une perte de classes promues ≤ 10 %.
- **H_B** : aire ≈ 0,5 : le relecteur n'est pas corrélé à la vérité jugée par tirages frais.
- **Contrôle négatif** : un score aléatoire ; un trieur mécanique (longueur, nombre de citations trouvées).
- **Falsification** : symétrique. Cette expérience réfute directement « hybride insensé = prendre leur relecteur » : il est insensé comme critère (par construction), pas forcément comme trieur.

## (c) Instruments nommés : la mesure minimale de fonctionnement

| Instrument | Ce qui est déjà mesuré (statut) | Mesure minimale manquante | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Juge à mise** (inférence universelle, 1/α, ordre secret, urne) | E1 : 18 fatales à 0 ou 1 sur 1 000 (borne 0,0045) ; puissance 0,958 à ε = 0,2 ; 0,196 à ε = 0,05 (VÉRIFIÉ en simulation, K = 3, d = 2, 200 tirages) | Fausses alertes et puissance sur **témoins de domaine** avec de vrais agents : le devis D plante 2 témoins par génération, ce qui ne mesure aucun taux ; il en faut ≥ 20 vrais et ≥ 20 faux par course (illustratif) pour une borne de Wilson utilisable | Mêmes fiches jugées sous v0 (ordre naturel) et sous v1 : écart attendu nul sur banque figée (K : l'urne protège contre le temps, sur une banque il n'y en a pas) | Le sélecteur par score moyen (bras 3 de S) ; et le juge v0 sur banque figée, qu'il faut **ne pas** battre si l'urne est inutile là |
| **Nul des filles v2** | E2 : 13 fatales à 0 sur 1 000 ; fille neuve 0,988 ; « parent + loi aveugle » passe à 0,421 sous v1 (VÉRIFIÉ en simulation) ; M : coût de l'option stricte ≈ 10 points à deux traits, nul à quatre (RAPPORTÉ, non vérifié) | Taux de promotion de filles « sans idée » que des **agents réels** écrivent (pas les sept tricheurs scriptés) ; E2 note déjà que « ou exclusif » passe à 0,963 : est-ce une découverte ? | Filles neuves écrites par agent sur monde à vérité connue, appariées par parents | Concaténation et mise en commun linéaire (déjà fermées, E2) |
| **Mémoire à empreinte prédictive** | D4a : 0 découverte en double avec héritage, 11 sans mémoire ; 31 à 39 fausses fusions à deux traits ; D4b : seuil à 5 % par fiche calibré sur softmax 1,5 (RAPPORTÉ, limite reconnue) | P4 ; et la distribution des divergences entre fiches **réellement distinctes** de l'archive (K : n'existe pas) | Paraphrases d'une même idée (doivent fusionner) contre idées distinctes du même domaine (ne doivent pas) | Jaccard sur 3-grammes à 0,5 (K : garde textuelle existante) ; si la signature ne bat pas Jaccard sur ces paires, elle est inutile |
| **Vérificateur d'un autre modèle** | Aucune mesure avec agents réels (D : but du premier lancement) ; C exige autre famille, N-053 autre lignée, K : seulement deux noms | Détection de tricheries plantées **par un agent** (contournement de la mesure, fichier `tirages.json` retouché, note persuasive dans le dossier) ; fausses alertes sur expérimentateurs honnêtes | Même fiche, même code, un bras honnête et un bras planté, verdicts à l'aveugle | Le rejeu par le noyau + empreinte d'ordre (K : dans l'option a le vérificateur n'est qu'une formalité) ; il doit attraper ce que le rejeu mécanique manque, sinon il coûte 3 USD par génération (D) pour rien |
| **Étage de proposition de la littérature (P)** | Rien dans les faits ; mes connaissances : RAPPORTÉ de mémoire, à vérifier | Part d'idées **gelables** (traduisibles en loi sur un espace déclaré) ; taux de redite par rapport à la mémoire ; P1 | Même domaine, même consigne, même traducteur que le maison | Mutation mécanique de survivantes (P1, bras sans modèle) |
| **Traducteur** | Rien | P2 | Idées appariées source/leurres | Gabarit sans idée (plancher 1/k) |
| **Métrique « fiches promues par dollar »** | Rien | Sa corrélation avec une vérité connue et avec la fécondité ; sa sensibilité à la configuration du juge (A5) | Même population jugée à 120 et 500 tirages : si le classement des proposeurs change, la métrique mesure le juge | Nombre de fiches gelées par dollar (ce qu'un proposeur qui fait du volume maximise) |

### Ce que je sais des candidats (question 1) — tout RAPPORTÉ de mémoire, à vérifier sur les PDF et les dépôts

| Système | Référence (à vérifier) | Étage de proposition séparable ? | Clés / réseau | Licence (HYPOTHÈSE, à lire sur le dépôt) | Valeur rapportée |
|---|---|---|---|---|---|
| AI Scientist v1 | Lu, Lu, Lange, Foerster, Clune, Ha, 2024, *The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery* | Oui, je crois : un script de génération d'idées prend un gabarit (code + idées graines) et rend des idées en JSON avec auto-scores (intérêt, faisabilité, nouveauté) ; contrôle de nouveauté par recherche bibliographique en ligne | Appel d'API de modèle ; réseau pour la bibliographie | Apache 2.0 (à vérifier) | Coût rapporté de l'ordre de 15 USD par papier (à vérifier) ; relecteur-modèle calibré contre des relectures humaines ; aucune mesure de l'étage d'idées seul à ma connaissance |
| AI Scientist v2 | Yamada, Lange, Lu, Hu, Lu, Foerster, Clune, Ha, 2025, *The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search* | Idéation séparable en principe ; l'exécution est une recherche arborescente | Idem | Apache 2.0 (à vérifier) | Un papier accepté à un atelier (rapporté, à vérifier) ; pas de mesure isolée de la proposition |
| Co-scientist (Google) | Gottweis et al., 2025, *Towards an AI co-scientist* | L'étage « génération » existe, mais la valeur vient du tournoi Elo jugé par modèle ; isoler la génération retire ce qui est publié | Pas de code ouvert à ma connaissance | Fermé | Validations biologiques rapportées (repositionnement de médicaments, mécanismes) ; non reproductible sans accès |
| Agent Laboratory | Schmidgall et al., 2025, *Agent Laboratory: Using LLM Agents as Research Assistants* | Phases séparées (revue, plan) ; le plan est un texte | API ; réseau pour la revue | Référence à vérifier (dépôt ouvert, licence à lire) | Réductions de coût rapportées (à vérifier) ; évaluation par relecteur humain et modèle |
| CodeScientist | Jansen et al., 2025, *CodeScientist: End-to-End Semi-Automated Scientific Discovery with Code-based Experimentation* | Oui : idéation par combinaison papier × bloc de code, avec classement humain possible | API | Apache 2.0 (à vérifier) | Un petit nombre de « découvertes » retenues après lecture manuelle sur quelques dizaines d'expériences (chiffres à vérifier) |
| Robin (FutureHouse) | Ghareeb et al., 2025, *Robin: A multi-agent system for automating scientific discovery* (référence à vérifier) | Génération d'hypothèses par agents de littérature, classement par tournoi | API ; réseau fort (littérature) | Ouvert (à vérifier) | Un candidat thérapeutique rapporté ; la valeur tient aux agents de lecture, pas à un étage isolé |
| Kosmos (Edison) | Référence à vérifier (2025) | Non séparable à ma connaissance ; produit fermé | Fermé | Fermé | Taux d'exactitude d'énoncés jugé par experts, rapporté, à vérifier |
| Zochi, AI-Researcher | Références à vérifier | Inconnu / dépôt ouvert pour AI-Researcher (à vérifier) | — | — | Je ne sais rien d'opposable |

Deux conséquences. (1) **Aucun** de ces étages ne rend une loi prédictive sur un espace d'instances : tous rendent du texte, parfois avec auto-scores que notre juge doit ignorer (R3). (2) Le seul candidat dont je crois l'étage réellement **détachable en code ouvert** est la génération d'idées d'AI Scientist v1/v2 et l'idéation de CodeScientist ; leur contrôle de nouveauté en ligne doit être remplacé par notre mémoire (sans réseau) — ce qui est précisément ce que P4 doit éprouver.

### Le proposeur maison (question 3) — ce que je recommande de mesurer, pas de croire

- **Entrées** : survivantes et éliminées (archive complète, C § 1) ; redites refusées avec leur classe ; moisson de littérature par un rôle lecteur **servi par le noyau** (moissonnage borné, C) ; **pas** les leçons en texte libre tant que P3 n'a pas tourné.
- **Diversité imposée** : quota par domaine et par opérateur (le tirage diversifié de C § 1.5, appliqué à la proposition et non seulement à la recombinaison) ; rejet mécanique des fiches dont la signature est à moins du seuil effectif d'une fiche de la même génération (jumelles intra-génération, que la mémoire ne voit pas puisqu'elles ne sont pas encore archivées — HYPOTHÈSE à lire dans le code).
- **Où tricher malgré le juge figé** : paris couverts et domaine étroit sont visés par le contrôle de contenu (S) mais non courus (S : « écrits, non courus ») ; lois collées à la marginale : sévérité nulle, donc non promues, mais **gelées et payées** (coût sans promotion, invisible à « fiches promues par dollar », visible au coût) ; jumelles hors sonde (P4) ; **volume** : beaucoup de fiches vraies évidentes à grand ε (promotion facile, E1 : 0,958) — la mémoire n'arrête que les redites de la même loi, pas les redécouvertes du connu sur une partition neuve des traits (E2 : « ou exclusif » 0,963).

### La métrique (question 4)

« Fiches promues par dollar » compte mal : (i) le volume d'évidences vraies ; (ii) les doubles, seulement si la mémoire les voit (P4) ; (iii) le coût de traduction et le coût du monde (K : non budgété) ; (iv) rien de la fécondité. Métrique proposée : **contenu promu net par dollar total** = Σ sur classes promues non fusionnées de (divergence déclarée × couverture), plus un terme de fécondité (filles promues issues de la classe à la génération suivante, à poids déclaré avant la course), divisé par dollars (agents + traduction + issues du monde). Duel à budget égal : trois bras (maison, littérature, nul = idées tirées au hasard de la mémoire sous la même consigne et le même traducteur), même juge, même configuration (tirages et traits fixés avant), étalonnage A/A d'abord. Seuil : un bras « n'apporte rien » si sa métrique ≤ nul + deux écarts A/A ; taille : n ≈ 100 fiches gelées par bras (illustratif, à recalculer après l'A/A). Le monde : option (b) de D (rétrodiction arXiv), le seul des faits qui ait à la fois un espace d'idées réel et une vérité tenue à part.

## (d) Ancrage matériel

- **Juge, mémoire, nul des filles** : processeur seul ; E1 : 1 000 répétitions × 70 lignes en 14 minutes sur un cœur ; E2 : 0,11 s par évaluation de fille (VÉRIFIÉ en simulation). P4 et l'A/A de P1 ne coûtent rien.
- **Modèles ouverts** : pour la contrainte « autre lignée » (A7), Qwen2.5-7B est déjà nommé par N-053 comme juge d'autre lignée (RAPPORTÉ) ; un 7B servi en local sur 127.0.0.1 règle aussi A8 pour le bras littérature (plus de clé à hériter ; reste à couper le réseau du conteneur). Un vérificateur 7B qui ne bat pas le rejeu mécanique (table (c)) serait un résultat, pas un échec.
- **Premier lancement (D)** : plafond 17,80 USD, attendu 5 à 10 (RAPPORTÉ) ; il ne mesure pas le proposeur (A6).
- **Duel P1 (illustratif)** : 3 bras × 100 fiches × (expérimentateur ≤ 1 USD + vérificateur ≤ 0,5 + traduction ≤ 0,3, barèmes du devis D) ≈ 540 USD au pire ; attendu 150 à 300. Les devis de M (10, 60, 60 USD conditionnels) sont une position non vérifiée. P2 : ≤ 50 USD (illustratif) : 100 ré-identifications par un lecteur 7B local sont gratuites, par Fable quelques dizaines de cents chacune. P3 : cinq générations × deux bras sur le monde simulé : processeur si agents scriptés, mais P3 n'a de sens qu'avec de vrais agents : ≈ 2 × devis D ≈ 40 USD plafond (illustratif).
- **Carte graphique** : aucune pour (a) et (b) ; (c) exige le harnais du programme (K : heures de carte, hors devis) et n'est pas le bon terrain pour trancher le proposeur.

## Recommandation (question 5)

Décider **maintenant** une seule chose, gratuite : rendre le rôle « proposeur » enfichable **et le rendre existant** (K : aucun rôle de formulation aujourd'hui ; la génération 0 vient d'un fichier). Ne pas décider maintenant entre maison et littérature : le lancement (a) ne peut pas informer ce choix (A6) ; c'est P2 d'abord (si la traduction détruit l'idée, aucun proposeur externe n'a de sens et il faut un proposeur natif de la fiche), puis P1 sur l'option (b). Ce qui me ferait changer d'avis : un bras mécanique sans modèle égalant les deux proposeurs dans P1 (alors la question est vide et l'argent va aux tirages) ; une aire ≥ 0,70 dans P5 (alors « leur relecteur » rentre, comme trieur déclaré) ; une dérive dans P3 (alors la question du proposeur passe après la fermeture des canaux de texte, N-053 point 5).

FIN-DE-CELLULE