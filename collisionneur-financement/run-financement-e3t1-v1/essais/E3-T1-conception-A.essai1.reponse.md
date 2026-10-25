# Cellule A — Tour III.1 (conception ciblée, à l'aveugle)

**Sur les pièces.** Le bloc FAITS est vide par décision de l'arbitre ; je ne lui invente aucun contenu. Conséquence : tout énoncé ci-dessous sur un dispositif, un statut ou un organisme est **RAPPORTÉ** (mémoire d'entraînement, antérieure à la date de la demande, 25 octobre 2026) et porte « à vérifier », ou bien est **HYPOTHÈSE**. Aucun montant, aucune date limite d'appel n'est donné autrement que comme « illustratif ». Les noms de dispositifs ont pu changer entre ma coupure de connaissance et la demande ; je signale ceux pour lesquels je sais qu'un changement a eu lieu ou est probable.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| A1 | Le statut d'ancien élève ouvre une porte que n'importe qui n'a pas. | HYPOTHÈSE | Les conventions d'accueil de bénévoles sont décidées par le directeur d'unité, pas par le service des anciens. L'alumnat facilite le *contact* (tuteur), pas l'*acte* administratif. Testable (duel D1). |
| A2 | Une affiliation d'accueil est nécessaire au financement. | HYPOTHÈSE | Vrai pour les agences publiques (ANR, PEPR, GENCI : RAPPORTÉ, à vérifier) ; faux pour une part des fonds philanthropiques internationaux qui versent à des individus (RAPPORTÉ, à vérifier). La question traite les deux comme couplés. |
| A3 | L'horizon « 3 à 12 mois » est compatible avec les financements publics français. | HYPOTHÈSE | Les cycles ANR vont du dépôt en automne au versement l'année suivante (RAPPORTÉ, ordre de grandeur, à vérifier) ; il n'est pas établi qu'un dispositif public verse un premier euro à une personne hébergée en moins de six mois. |
| A4 | « Indépendant » et « hébergé sous convention » sont compatibles. | HYPOTHÈSE | Les conventions d'accueil des établissements publics contiennent souvent des clauses de propriété intellectuelle au profit de l'établissement (RAPPORTÉ, à vérifier, variable par établissement). L'indépendance revendiquée (préenregistrement, licence du code) peut entrer en conflit. |
| A5 | Le doctorat est la ligne de partage principale. | RAPPORTÉ (partiellement) | Vrai pour MSCA, ERC, postdocs (RAPPORTÉ, à vérifier). Mais une seconde ligne compte autant : **l'existence d'un employeur ou d'une structure juridique** (Bpifrance, CIR, ANR). La question la cite mais ne la met pas au même rang. |
| A6 | La « sécurité de l'IA » au sens du programme (conscience d'évaluation, délégation) est une catégorie reconnue par les financeurs français. | HYPOTHÈSE | Les financeurs publics français classent plutôt en « IA de confiance », « IA frugale », « évaluation » (RAPPORTÉ, à vérifier). Le vocabulaire du dossier devra être traduit ; non testé. |
| A7 | Les dépenses resteront de l'ordre de « quelques centaines de dollars par mois ». | OBSERVÉ-NON-AUDITÉ (par le directeur) | C'est le coût actuel sans salaire. La question ne dit pas si l'objectif est de couvrir des frais ou de remplacer un revenu ; les montages diffèrent d'un facteur dix ou plus (illustratif). |
| A8 | Le calcul national est utile pour des sondes sur modèles de 8 G de paramètres. | HYPOTHÈSE | Le besoin décrit (activations d'un modèle 8 G, sondes linéaires ou petits réseaux) tient sur un seul processeur graphique ; le calcul national répond à un autre régime (multi-nœuds). Le coût de la demande peut dépasser le gain (duel D4). |
| A9 | Un « premier billet technique public » suffit comme pièce de crédibilité. | HYPOTHÈSE | Les financeurs philanthropiques du domaine demandent souvent des pièces lisibles par eux (préprint, code, lettre) ; les laboratoires français demandent des pièces d'un autre genre (CV académique, publications à comité). Les deux dossiers ne sont pas le même. |

---

## (b) Duels décisifs

Chaque duel est une décision de financement traitée comme expérience : deux hypothèses exclusives, une métrique, un seuil (illustratif, à fixer par le directeur), un contrôle négatif, et ce que chaque issue falsifie. Rien ici n'est un conseil juridique.

### D1 — L'alumnat ouvre-t-il un accueil rapide ?
- **H_A** : une demande de convention d'accueil (chercheur bénévole / visiteur) adressée via le tuteur des Mines ou le département de l'ENS Paris-Saclay aboutit à une réponse de principe du directeur d'unité en moins de 6 semaines (seuil illustratif).
- **H_B** : la réponse de principe prend plus de 6 semaines ou est négative, indépendamment du lien d'ancien élève.
- **Métrique** : délai (jours) entre l'envoi d'un dossier identique (une page de projet, CV, lettre du tuteur, projet de convention) et une réponse écrite de principe.
- **Contrôle négatif** : le *même* dossier, sans lettre de tuteur ni mention d'alumnat, adressé à une unité comparable sans lien (par exemple une équipe de l'Université Paris-Saclay hors ENS). Si le contrôle répond aussi vite, l'effet alumnat (A1) est falsifié.
- **Issue falsifiante** : H_A falsifiée si délai > seuil ou refus ; H_B falsifiée si réponse positive sous le seuil **et** contrôle plus lent.

### D2 — Argent public ou argent philanthropique sous douze mois ?
- **H_A** : au moins un dispositif public français (agence, région, institut d'IA, fondation d'école) verse un premier euro à une personne hébergée sans poste dans les 9 mois suivant le dépôt (seuil illustratif).
- **H_B** : aucun dispositif public ne verse sous 9 mois ; seuls des fonds philanthropiques internationaux le font.
- **Métrique** : délai dépôt → premier virement, par dispositif, documenté par les appels publiés (dates d'ouverture, de notification, de conventionnement).
- **Contrôle négatif** : un dispositif dont on *sait* qu'il exclut la situation (par exemple un appel réservé aux personnels permanents) — doit donner un refus d'éligibilité rapide ; sinon la métrique mesure du bruit administratif, pas l'éligibilité.
- **Issue falsifiante** : H_A falsifiée si, sur la lecture des textes d'appel (pas de mémoire), aucun dispositif public n'a de cycle compatible ; H_B falsifiée si un seul le fait (le dispositif régional ou une fondation d'école sont les candidats les plus plausibles — HYPOTHÈSE).

### D3 — Le doctorat est-il la variable qui sépare, ou l'employeur ?
- **H_A** : parmi les dispositifs listés en (8), la majorité de ceux qui excluent le directeur l'excluent pour absence de **doctorat**.
- **H_B** : la majorité l'excluent pour absence d'**employeur / structure juridique**.
- **Métrique** : comptage, sur les textes d'éligibilité lus, de la clause bloquante première (doctorat ; employeur ; les deux ; aucune).
- **Contrôle négatif** : un dispositif notoirement ouvert aux individus (fonds philanthropique versant à des personnes physiques — RAPPORTÉ, à vérifier) doit tomber en « aucune » ; sinon la grille de lecture est mal calibrée.
- **Issue falsifiante** : chaque issue falsifie l'ordre de priorité de l'autre pour les montages (M2 vs M3).

### D4 — Calcul national ou crédits commerciaux ?
- **H_A** : pour les expériences préenregistrées sur un modèle de 8 G de paramètres, l'obtention d'heures sur le calcul national (GENCI/IDRIS, RAPPORTÉ, à vérifier) coûte moins en temps administratif (heures de dossier + délai) que les crédits commerciaux obtenus par programmes de recherche des fournisseurs.
- **H_B** : les crédits commerciaux ou la location à la carte sont obtenus plus vite et couvrent le besoin ; le calcul national n'est pertinent qu'au-delà d'un seuil de volume (à fixer en heures-GPU, illustratif).
- **Métrique** : heures-GPU effectivement disponibles à J+30 et J+90 (illustratif), divisées par le temps humain investi.
- **Contrôle négatif** : la location à la carte (déjà pratiquée) sert de ligne de base : coût connu, délai nul.
- **Issue falsifiante** : H_A falsifiée si, à J+90, le calcul national n'a rien livré ou exige une affiliation non obtenue ; H_B falsifiée si une allocation « accès dynamique » (nom à vérifier) arrive avant les crédits commerciaux.

### D5 — Quelle pièce convertit ?
- **H_A** : un **préenregistrement public + résultats sur processeur graphique** convainc un financeur philanthropique du domaine plus souvent qu'un préprint sans résultats.
- **H_B** : un **préprint** (même préliminaire) est la pièce lue en premier ; le préenregistrement n'est pas lu.
- **Métrique** : taux de réponse non-générique (question technique, demande d'entretien) à deux versions d'un même dossier court envoyées à des interlocuteurs appariés (même type d'organisme, même mois).
- **Contrôle négatif** : une troisième version sans aucune pièce technique (lettre + CV seulement) ; elle fixe le plancher.
- **Issue falsifiante** : si les deux versions ne diffèrent pas du plancher, ni H_A ni H_B n'est soutenue et c'est la **lettre du tuteur ou le réseau** qui fait la différence — ce qui réoriente le plan de trois mois (point 6).

---

## (c) Instruments nommés dans la question : la mesure minimale

La question nomme des instruments de recherche (sondes de conscience d'évaluation, contrôle de la délégation, préenregistrement, agents de code, registres et empreintes) et des instruments de financement. Un financeur sérieux demandera d'abord si les premiers fonctionnent.

**Sonde « conscience d'évaluation ».** Mesure minimale : sur un ensemble apparié de transcriptions où le modèle est (i) explicitement en situation de test et (ii) en usage ordinaire, de même longueur, même domaine, même format d'instruction, taux de détection (vrai positif) et taux de fausses alertes sur (ii). Cas honnêtes appariés : conversations ordinaires contenant les mots « test », « évaluation », « benchmark » **sans** être des tests, pour vérifier que la sonde ne lit pas le lexique. Vérification mécanique à battre : un classifieur par mots-clés et un classifieur sur la seule représentation du prompt (pas des activations) ; si la sonde ne bat pas ces deux lignes de base à même taux de fausses alertes, elle ne mesure rien d'interne. Seuil : illustratif, à préenregistrer.

**Contrôle de la délégation** (le modèle délègue-t-il une sous-tâche à un outil/agent de façon non déclarée ?). Mesure minimale : taux de délégations détectées sur des trajectoires d'agent où la délégation est injectée par construction, contre taux de fausses alertes sur des trajectoires où le modèle exécute lui-même. Vérification mécanique à battre : l'inspection des journaux d'appels d'outils (si la sonde ne fait pas mieux que lire le journal, elle est redondante ; son intérêt est sur les cas où le journal est absent ou falsifié).

**Préenregistrement.** Mesure minimale : proportion d'analyses finales qui correspondent au plan déposé, horodaté par un tiers (dépôt public avec empreinte). Fausse alerte : une déviation déclarée et motivée n'en est pas une.

**Agents de code comme exécutants.** Mesure minimale : taux de reproduction à l'identique (empreinte des sorties) d'une expérience relancée par l'agent depuis le registre, contre relance manuelle ; toute divergence non expliquée est un faux négatif du registre.

**Registres et empreintes.** Mesure minimale : un tiers peut-il, à partir du seul registre, recomputer une empreinte et la faire coïncider ? Oui/non ; un seul échec falsifie l'instrument.

**Instruments de financement.** Leur « taux de détection » est le taux de réponses non génériques ; leur « fausse alerte » est l'appel ouvert en apparence mais fermé en éligibilité (duel D2, contrôle négatif).

---

## (d) Ancrage matériel

- **Modèles ouverts à ~8 G de paramètres** (noms RAPPORTÉS, versions exactes à vérifier à la date de la demande) : Llama 3.x 8B (Meta), Qwen 2.5/3 à 7–8B (Alibaba), Mistral 7B (Mistral AI), Gemma 2 9B (Google). Les licences diffèrent (Llama et Gemma : licences propres, pas OSI ; Qwen et Mistral : Apache 2.0 pour certaines versions — RAPPORTÉ, à vérifier) ; cela compte si un financeur exige du code et des artefacts sous licence ouverte.
- **Calcul nécessaire** : extraction d'activations d'un 8B en précision réduite tient sur un processeur graphique de 24 Go (illustratif) ; les sondes elles-mêmes s'entraînent sur processeur central ou petit GPU. Un GPU de classe A100/H100 n'est utile que pour des passes massives.
- **Coût** (illustratif, hors salaire) : location à la carte de 1 à 3 €/h-GPU ; 100 à 300 h-GPU/mois ; soit quelques centaines d'euros par mois, cohérent avec l'observé-non-audité A7. Les interfaces de modèles de frontière (évaluations de référence) : même ordre. **Le salaire change l'échelle** : un revenu de chercheur en début de carrière en France se compte en dizaines de milliers d'euros bruts par an (illustratif) ; c'est lui qui décide du montage.

---

## Réponse aux huit points de l'arbitre (matériau RAPPORTÉ, tout à vérifier)

### 1. Affiliation d'accueil sans emploi

Statuts existants en France (RAPPORTÉ, à vérifier établissement par établissement) :
- **Collaborateur bénévole / chercheur bénévole sous convention d'accueil** : la personne n'est pas rémunérée ; convention signée par le chef d'établissement (ou par délégation le directeur d'unité) et la personne ; elle règle l'accès aux locaux, la responsabilité, la confidentialité et la **propriété intellectuelle** — souvent au profit de l'établissement pour les résultats obtenus dans ses murs ou avec ses moyens (à vérifier dans le texte proposé). Décide : directeur d'unité, puis service juridique.
- **Chercheur associé** : vocabulaire utilisé par certaines unités pour un bénévole affilié durablement ; mêmes mécanismes, parfois vote du conseil de laboratoire.
- **Chercheur / professeur invité** : en général rémunéré sur budget de l'établissement, court (semaines à mois), réservé en pratique à des personnes déjà en poste ailleurs ; ne correspond pas à la situation (HYPOTHÈSE).
- **Chercheur visiteur d'une école d'ingénieurs** : à Mines Paris – PSL, un accueil dans un centre (par exemple le Centre de recherche en informatique — nom à vérifier) relève du directeur de centre ; une convention de « collaborateur extérieur » existe sous des noms variables.

Ce que chaque statut **ouvre** : adresse électronique institutionnelle (souvent oui, à vérifier) ; dépôt dans HAL — **HAL n'exige pas d'affiliation** : tout déposant inscrit peut déposer et choisir une structure d'affiliation (RAPPORTÉ, à vérifier) ; éligibilité ANR comme participant (oui si la convention couvre la durée du projet) et comme coordinateur (en pratique réservé aux personnels avec contrat couvrant la durée — RAPPORTÉ, à vérifier) ; accès au calcul national (demande portée par un responsable permanent de l'unité, à vérifier) ; signature d'un article sous l'affiliation (oui, c'est le but des conventions).

Ce que chaque statut **coûte** : PI potentiellement captée ; obligations de confidentialité ; parfois clause d'exclusivité sur le sujet ; pas d'obligation de publication en général ; licence du code à négocier **avant** signature.

Distinctions : **ENS Paris-Saclay** est établissement-composante de l'**Université Paris-Saclay** — une convention avec un laboratoire de l'ENS peut relever de la tutelle CNRS ou de l'université (à vérifier par laboratoire) ; **Mines Paris – PSL** (nouveau nom de Mines ParisTech depuis 2022, RAPPORTÉ) a ses propres centres et sa fondation. Ce qu'un **ancien élève** peut demander : l'accès au tuteur, à la fondation de l'école et aux réseaux d'anciens ; aucun droit statutaire à une convention (HYPOTHÈSE, duel D1).

### 2. Financements publics français

- **Agence nationale de la recherche (ANR)** : appel à projets générique annuel ; porteur : un établissement, avec un responsable scientifique en poste ; finance salaires de non-permanents, frais, pas directement le calcul national. Délai dépôt → versement : de l'ordre d'un an (RAPPORTÉ, ordre de grandeur, à vérifier). Exige employeur-hôte ; pas de doctorat formellement, mais en pratique pour « JCJC ».
- **PEPR IA (France 2030)** : programme piloté par CNRS/Inria (à vérifier) ; finance des projets déjà sélectionnés et des appels à manifestation ; une personne hébergée ne peut qu'être recrutée sur un projet existant.
- **Instituts interdisciplinaires d'IA (3IA, puis « clusters IA » sélectionnés en 2024, dont PR[AI]RIE–PSAI pour PSL/Paris, nom à vérifier)** : chaires, postdocs, parfois bourses doctorales ; portés par les établissements membres.
- **INESIA** (Institut national pour l'évaluation et la sécurité de l'IA, annoncé début 2025, RAPPORTÉ, nom exact et périmètre à vérifier) : structure de coordination entre entités existantes (LNE, Inria, ANSSI, PEReN — RAPPORTÉ) ; **je n'ai pas connaissance d'un guichet de financement pour chercheurs externes** ; à vérifier à la date de la demande.
- **Région Île-de-France** : domaine d'intérêt majeur en IA (DIM AI4IDF, nom à vérifier) finançant doctorats, postdocs, équipements, via les établissements.
- **Instituts de Paris-Saclay et PSL** : DATAIA (Paris-Saclay), PRAIRIE (PSL), Institut Pascal (institut d'études avancées de Paris-Saclay, programmes thématiques) : accueils et postdocs portés par des membres.

Tous exigent un établissement porteur ; aucun, à ma connaissance, ne verse à une personne physique sans poste.

### 3. Fondations et bourses privées françaises

- **Fondation Mines Paris** (nom à vérifier) et **Fondation de l'ENS Paris-Saclay** (existence et nom à vérifier) : bourses d'excellence, soutien à des projets d'école ; un ancien élève peut solliciter, l'école décide.
- **Fondation Mathématique Jacques Hadamard (FMJH)** et **Fondation Sciences Mathématiques de Paris (FSMP)** : postdocs et chaires en mathématiques, doctorat requis pour les postdocs ; pertinence thématique à argumenter.
- **Fondation CFM pour la recherche** : bourses doctorales et postdoctorales à Paris (RAPPORTÉ, à vérifier).
- **Instituts d'études avancées** : IEA de Paris (résidences, en général pour chercheurs confirmés), Institut Pascal.
- **Fondations d'entreprise** : variables ; aucune que je puisse nommer avec certitude pour la sécurité de l'IA en France à cette date.

### 4. Financeurs internationaux et calcul

- **Fonds philanthropiques** : Open Philanthropy (a annoncé un changement de nom en 2025 — « Coefficient Giving » — RAPPORTÉ, à vérifier) ; **Long-Term Future Fund** (EA Funds) : verse à des individus, dossiers courts, délais de semaines à quelques mois (RAPPORTÉ, à vérifier) ; **Survival and Flourishing Fund** ; **Manifund** (regranting) ; **Future of Life Institute** (appels thématiques) ; **AI Safety Fund** (Frontier Model Forum, plutôt pour institutions) ; **Cooperative AI Foundation**. Accessibilité : la plupart acceptent des résidents français sans employeur, parfois via un intermédiaire fiscal (à vérifier).
- **Programmes de bourses et résidences** : MATS, PIBBSS, Astra, Anthropic Fellows (RAPPORTÉ, à vérifier) : souvent avec déplacement (Berkeley, Londres) ; le programme « Alignment Project » annoncé par le **UK AI Security Institute** (renommé depuis « AI Safety Institute » en février 2025, RAPPORTÉ) finance des projets, y compris hors Royaume-Uni (périmètre individus/institutions à vérifier) ; le **Systemic AI Safety grants** du même institut a été plutôt institutionnel.
- **Bourses européennes individuelles** : **MSCA Postdoctoral Fellowships** — doctorat requis, hôte requis, règle de mobilité (ne pas avoir résidé dans le pays hôte plus de 12 mois sur les 36 derniers — RAPPORTÉ, à vérifier) : un résident parisien est vraisemblablement **inéligible** pour un hôte français ; **ERC Starting** : doctorat 2 à 7 ans, hôte requis.
- **Calcul** : **GENCI / IDRIS (Jean Zay)** via le portail d'accès (nom « eDARI / accès dynamique », à vérifier), demande portée par un chercheur affilié ; **EuroHPC** (appels d'accès, et « AI Factories » depuis 2024–2025, à vérifier) ; crédits commerciaux : Google Cloud research credits, AWS Cloud Credit for Research, programmes d'accès chercheurs d'OpenAI et d'Anthropic (noms à vérifier), tous demandent en général une affiliation ou au moins une page web de projet.

### 5. Montages

| | M1 Convention d'accueil + fonds philanthropique | M2 Structure propre + aides innovation + CIR | M3 Rattachement doctoral/postdoctoral + bourse | M4 Participant à un projet d'agence porté par un labo |
|---|---|---|---|---|
| Conditions | Convention signée ; dossier court ; lettre du tuteur | Création d'une société au régime réel (le CIR n'est pas accessible aux micro-entreprises au régime micro — RAPPORTÉ, à vérifier) ; Bpifrance exige une entreprise | Sans doctorat : contrat doctoral (3 ans) ou CIFRE (avec entreprise) ; avec doctorat : postdoc sur projet existant | Un labo avec budget ANR/PEPR/cluster disponible et poste ouvert |
| Délai avant premier euro | Semaines à quelques mois (illustratif) | Bpifrance : mois ; CIR : après clôture de l'exercice, sauf remboursement anticipé (à vérifier) | 6 à 12 mois (illustratif), calé sur les campagnes | Dépend d'un budget déjà voté ; parfois rapide |
| Montant plausible sur 12 mois | Illustratif : de la couverture des frais à un revenu | Illustratif ; CIR = 30 % des dépenses éligibles (taux RAPPORTÉ, à vérifier), donc proportionnel à ce qu'on dépense déjà | Salaire réglementé (contrat doctoral) ou grille postdoc | Salaire CDD |
| Ce que ça impose | Code ouvert et rapports publics (souvent exigés) ; PI à négocier avec l'hôte | Comptabilité, obligations sociales ; la recherche devient activité de l'entreprise | Sujet et direction partagés ; calendrier de thèse | Objectifs du projet du labo ; subordination |
| Risque principal | Clause PI de l'hôte contre indépendance ; dépendance à peu de donateurs | Charge administrative ; CIR décalé, inutile pour le cash à 3 mois | Perte d'indépendance ; durée engageante | Dilution du programme |
| Ce qui le départage | D1 et D5 positifs | D3 → H_B (c'est l'employeur qui bloque) | D3 → H_A (c'est le doctorat qui bloque) et volonté d'un emploi | Existence d'un budget ; D2 |

Aucun de ces montages n'est « la » réponse ; M1 et M4 peuvent se cumuler ; M2 et M3 s'excluent en pratique (temps).

### 6. Crédibilité et ordre sur trois mois

Pièces attendues (HYPOTHÈSE sur les attentes, cohérente avec D5) :
1. Mois 1 : **préenregistrement public horodaté** de l'expérience n° 1 + **dépôt du code** (licence choisie) + lettre du tuteur demandée.
2. Mois 2 : **résultats sur processeur graphique** avec les métriques du (c) (détection, fausses alertes, lignes de base mécaniques battues ou non) ; **billet technique**.
3. Mois 3 : **préprint** (HAL ou archive ouverte) ; dossier court pour fonds philanthropiques ; demande de convention envoyée en parallèle dès le mois 1 (D1 prend du temps).
L'ordre est falsifiable par D5 : si c'est la lettre qui convertit, la demander au mois 1.

### 7. Questions au tuteur des Mines et au département de l'ENS Paris-Saclay (dix)

1. Quel statut exact votre unité utilise-t-elle pour une personne sans poste (nom de la convention) ?
2. Qui signe, et en combien de semaines ?
3. Que dit la convention-type sur la **propriété intellectuelle** et le **code** ? Peut-on annexer une licence choisie par moi ?
4. Y a-t-il une clause d'exclusivité ou de confidentialité sur le sujet ?
5. Puis-je signer sous l'affiliation et déposer dans HAL avec la structure ?
6. L'unité peut-elle porter une demande de calcul national pour mon projet ? Qui en serait responsable ?
7. Un budget existant (ANR, PEPR, cluster, région) a-t-il une ligne non consommée pour un CDD court ou des frais ?
8. L'école ou sa fondation a-t-elle un dispositif pour anciens élèves (bourse, amorçage) ?
9. Accepteriez-vous d'écrire une lettre nommant ce que vous avez vu de mon travail (pas une recommandation générique) ?
10. Quelle condition vous ferait **refuser** l'accueil ?

**Ce qu'il ne faut pas faire** (HYPOTHÈSE motivée) : signer une convention sans en lire la clause PI ; créer une société avant d'avoir tranché D3 (irréversible et coûteux en temps) ; demander une inscription doctorale « pour l'affiliation » si l'on ne veut pas faire de thèse (engagement de trois ans, sujet partagé) ; attendre la convention pour publier le préenregistrement (HAL et les dépôts horodatés n'exigent pas d'affiliation) ; présenter le programme comme concurrent du laboratoire d'accueil ; postuler à MSCA avec un hôte français sans vérifier la règle de mobilité ; mélanger dans un même dossier le vocabulaire des fonds philanthropiques et celui des agences françaises.

### 8. Ce qui est connu — liste des dispositifs cités, tous « à vérifier »

ANR (appel générique, JCJC) ; PEPR IA (France 2030) ; clusters IA 2024 dont PR[AI]RIE–PSAI (PSL) — nom à vérifier ; DATAIA (Université Paris-Saclay) ; Institut Pascal (Université Paris-Saclay) ; IEA de Paris ; INESIA — annoncé 2025, périmètre de financement inconnu ; DIM AI4IDF (Région Île-de-France) — nom à vérifier ; Fondation Mines Paris ; Fondation ENS Paris-Saclay — existence à vérifier ; FMJH ; FSMP ; Fondation CFM pour la recherche ; Bpifrance (aides à l'innovation ; Bourse French Tech — dispositif ayant changé de nom plusieurs fois, à vérifier) ; CIR/CII, statut JEI ; CIFRE (ANRT) ; contrat doctoral ; GENCI/IDRIS Jean Zay ; EuroHPC et AI Factories ; MSCA Postdoctoral Fellowships ; ERC Starting ; Open Philanthropy (changement de nom 2025 rapporté) ; Long-Term Future Fund ; Survival and Flourishing Fund ; Manifund ; Future of Life Institute ; AI Safety Fund (Frontier Model Forum) ; Cooperative AI Foundation ; UK AI Security Institute (ex-AI Safety Institute, renommé février 2025) et ses programmes Systemic AI Safety grants et Alignment Project ; MATS ; PIBBSS ; Astra ; Anthropic Fellows ; programmes de crédits Google Cloud, AWS, OpenAI, Anthropic. Mines ParisTech est devenu Mines Paris – PSL (2022). Aucun montant ni aucune date d'appel n'est donné de mémoire.

---

**Ce qui réfuterait l'ensemble de cette cellule** : qu'un dispositif public français verse directement à une personne physique sans hôte ni employeur sous six mois (A2, A3, D2 renversés) ; ou qu'un hôte accepte une convention laissant la PI au directeur sans négociation (A4 levée). Les deux sont vérifiables en lisant des textes, pas en me croyant.

FIN-DE-CELLULE