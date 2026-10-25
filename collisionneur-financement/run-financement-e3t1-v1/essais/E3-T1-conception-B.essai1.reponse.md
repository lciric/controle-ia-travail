# Proposition B : Tour III.1, « financer un programme indépendant de sécurité de l'IA depuis la France »

**État des pièces.**
- Le bloc FAITS est vide par décision de l'arbitre, sans troncature visible : je n'ai aucun fait VÉRIFIÉ.
- Les propositions A et C sont invisibles à ce tour (aveugle). B1 ne s'applique donc pas encore.
- Le contenu de la question est traité comme **RAPPORTÉ** (déclaration de l'arbitre).
- Tout ce que je sais des dispositifs vient de ma mémoire. Celle-ci s'arrête avant la date de la demande (25 octobre 2026). Tout dispositif cité est donc **HYPOTHÈSE, à vérifier**. Je ne donne aucun montant ni aucune date d'appel.

Je traite les demandes 1 à 8 de l'arbitre comme le contenu à analyser, dans la grille (a)–(d) du livrable.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi il compte |
|---|---|---|---|
| a1 | « Une École des Mines » = Mines Paris – PSL | **Non établi.** La situation dit « une École des Mines » ; la demande nomme Mines Paris – PSL. | Si l'école du tuteur est une autre école du réseau, les statuts, les conventions et l'adossement (PSL ou non) diffèrent. C'est à trancher en premier. |
| a2 | Le tuteur est en poste et peut engager un laboratoire | RAPPORTÉ (« prêt à l'appuyer ») ; capacité d'engagement **non établie** | Appuyer (une lettre) n'est pas accueillir (une convention signée par la direction). |
| a3 | Un ancien élève dispose de droits d'accueil particuliers | HYPOTHÈSE, probablement fausse au sens formel | À ma connaissance (à vérifier), l'ancien élève a un réseau et de la bienveillance, pas un statut. Une adresse d'ancien élève n'est pas une affiliation. |
| a4 | Un statut d'accueil non rémunéré ouvre l'éligibilité comme porteur d'un projet de l'Agence nationale de la recherche (ANR) | HYPOTHÈSE, probablement fausse | Mémoire, à vérifier : l'ANR finance des établissements, et le coordinateur est en général un personnel d'un organisme partenaire. Le directeur serait au mieux participant. |
| a5 | Un statut d'accueil ouvre le calcul national (GENCI / IDRIS, Jean Zay) | HYPOTHÈSE | L'accès passe, à ma connaissance, par un porteur rattaché à un laboratoire public. Le cas d'un collaborateur bénévole n'est pas établi. Testé en E2. |
| a6 | L'Institut national pour l'évaluation et la sécurité de l'IA (INESIA) finance des tiers | HYPOTHÈSE, probablement fausse | Mon souvenir (à vérifier) : une structure récente de coordination de services de l'État (SGDSN, DGE, avec ANSSI, Inria, LNE, PEReN), pas un guichet de subventions. |
| a7 | Les instituts interdisciplinaires d'IA (« 3IA ») existent sous ce nom | HYPOTHÈSE | Ils ont pu être remplacés ou absorbés par les « IA Clusters » de France 2030. Changement de nom probable, à vérifier. |
| a8 | Un horizon de 3 à 12 mois est compatible avec les guichets publics français | HYPOTHÈSE, douteuse | Les cycles publics sont souvent annuels, avec un décalage entre décision et versement. Testé en E4. |
| a9 | Le doctorat est la condition qui sépare la plupart des dispositifs | RAPPORTÉ comme prémisse de l'arbitre, **non vérifié** | Rival : c'est l'**employeur ou porteur institutionnel** qui sépare. Testé en E1. |
| a10 | « Indépendant » et « hébergé » sont compatibles | HYPOTHÈSE | L'hébergement peut entraîner une dévolution de la propriété intellectuelle, une confidentialité ou un délai avant publication. Cela peut contredire le préenregistrement public et le code ouvert. Testé en E3. |
| a11 | Les résultats du programme sont publiables sans restriction | HYPOTHÈSE | Une recherche sur la conscience d'évaluation peut être jugée à double usage par un hôte ou un financeur. |
| a12 | Des sondes sur des modèles d'environ 8 milliards de paramètres suffisent à convaincre un financeur | HYPOTHÈSE | Rien n'établit que l'échelle 8B soit jugée pertinente. Le résultat central doit d'abord battre des lignes de base mécaniques (E6, section c). |
| a13 | « Contrôle de la délégation » a un sens opérationnel partagé | **Non défini** dans la question | Sans définition, aucun financeur ne peut évaluer cet axe (voir C2). |
| a14 | Dépenses actuelles : quelques centaines de dollars par mois, payées personnellement | RAPPORTÉ | C'est la seule donnée budgétaire. Sur 12 mois : quelques milliers de dollars hors rémunération (calcul direct). |

**Attaque de cadrage.** La question est ordonnée « affiliation → financement → crédibilité ». Je soutiens l'hypothèse inverse : sur 3 mois, la pièce limitante est un **résultat préenregistré qui bat ses lignes de base**, nul ou positif (E6). L'affiliation se négocie en parallèle et ne doit rien bloquer. C'est une HYPOTHÈSE, réfutable par E1 et E5.

---

## (b) Expériences décisives (duels H_A contre H_B)

Ici, une « expérience » est une démarche à issue binaire et écrite. Une réponse orale, un « ça devrait passer » ou un souvenir ne comptent pas comme issue.

### E1 : qu'est-ce qui bloque, le doctorat ou l'employeur ?
- **H_A** : parmi les dispositifs compatibles avec 3 à 12 mois, la condition bloquante dominante est l'absence d'**employeur ou d'établissement porteur**.
- **H_B** : c'est l'absence de **doctorat**.
- **Protocole.**
  - Liste fermée, gelée avant codage, des dispositifs des rubriques 2 à 4 de la question.
  - Pour chacun, deux variables binaires lues **dans le règlement en vigueur**, jamais de mémoire : « exige un porteur ou employeur » et « exige un doctorat ».
  - Deux codeurs indépendants (le directeur, plus un agent ou un tiers qui ne voit pas le premier codage).
- **Métrique.**
  - n_E = nombre de dispositifs bloqués *seulement* par l'employeur.
  - n_D = nombre de dispositifs bloqués *seulement* par le doctorat.
  - Accord inter-codeurs (κ de Cohen).
- **Seuil** (illustratif) : κ ≥ 0,8 pour que le codage compte. H_A si n_E ≥ 2·n_D ; H_B si n_D ≥ 2·n_E ; sinon zone grise, et on garde les deux cas.
- **Contrôle négatif.** Deux dispositifs dont le texte affiche une ouverture aux particuliers, par exemple un programme de crédits d'API sur candidature (à vérifier). S'ils sont codés « bloquants », la grille est cassée.
- **Falsification.**
  - n_E ≫ n_D falsifie H_B : l'affiliation passe avant tout projet doctoral.
  - n_D ≫ n_E falsifie H_A : le cas « sans doctorat » doit chercher d'abord les fonds non académiques.

### E2 : que donne réellement un statut d'accueil non rémunéré ?
- **H_A** : un statut de collaborateur bénévole ou de chercheur associé permet, seul, (i) une demande d'accès au calcul national, (ii) la signature d'un article sous l'affiliation, (iii) le rattachement du dépôt HAL à la structure.
- **H_B** : (i) exige un statut de personnel ou un porteur permanent qui inscrit le directeur comme membre de projet ; seuls (ii) et (iii) sont ouverts.
- **Protocole.** Même question écrite, avec référence au règlement demandée, envoyée au guichet d'accès au calcul national (procédure à vérifier) et au service recherche de chaque établissement candidat.
- **Métrique.** Réponse écrite, oui ou non, assortie d'une citation de règlement.
- **Seuil.** Une réponse écrite citant le texte suffit à trancher ; une réponse orale n'est pas concluante.
- **Contrôle négatif.** Poser la même question pour un cas évidemment inéligible (personne sans aucun rattachement). Si le guichet répond « oui » aussi, ses réponses ne discriminent pas et sont écartées.
- **Falsification.** Un « oui » écrit sur (i) falsifie H_B ; un « non » écrit falsifie H_A. Dans ce cas, le calcul vient des crédits commerciaux ou de programmes de chercheurs (montages M1 et M2).

### E3 : propriété intellectuelle, publication, licence
- **H_A** : la convention type de l'établissement X laisse au directeur ses droits sur le code et permet une licence ouverte et une publication immédiate.
- **H_B** : la convention attribue les résultats à l'établissement, impose une autorisation de valorisation (structures de valorisation à vérifier) ou un délai de confidentialité avant publication.
- **Protocole.** Obtenir **le modèle de convention avant tout engagement**, pour l'ENS Paris-Saclay, pour l'école du tuteur et, le cas échéant, pour l'Université Paris-Saclay. Relever trois clauses : dévolution des résultats, confidentialité, délai avant publication.
- **Métrique.** Présence ou absence de chaque clause.
- **Seuil.** Tout délai avant publication supérieur à zéro est incompatible avec un préenregistrement public, sauf exception écrite.
- **Contrôle négatif.** Demander si la convention couvre le code **déjà public** sous licence ouverte avant la signature. Si oui, elle est trop large : on renégocie ou on écarte cet hôte.
- **Falsification.** Une clause de dévolution ou de délai présente falsifie H_A pour cet hôte. Une absence écrite falsifie H_B.

### E4 : vitesse jusqu'au premier euro
- **H_A** : dans une fenêtre de 90 jours (illustratif), seule une voie philanthropique internationale acceptant des personnes physiques ou un sponsor fiscal peut verser.
- **H_B** : au moins une voie française (fondation d'école, institut ou cluster IA, région) peut verser dans la même fenêtre à cette situation.
- **Protocole.** Pour chaque dispositif retenu en E1 : calendrier publié (dépôt, décision annoncée) et, si possible, délai réel demandé à un ancien bénéficiaire.
- **Métrique.** Nombre de dispositifs éligibles dont la fenêtre « dépôt → versement » tient dans 90 jours.
- **Contrôle négatif.** Inclure un appel générique notoirement annuel, comme l'appel générique de l'ANR (à vérifier). S'il ressort à moins de 90 jours, le relevé est faux.
- **Falsification.** Au moins un dispositif français éligible et rapide falsifie H_A. Aucun falsifie H_B, et les voies françaises passent à l'horizon de 6 à 12 mois.

### E5 : la trace publique est-elle nécessaire ?
- **H_A** : les financeurs de sécurité de l'IA qui acceptent des personnes physiques financent quasi exclusivement des gens ayant une trace technique publique antérieure.
- **H_B** : une part substantielle des personnes financées n'en a pas ; le parrainage ou le projet suffit.
- **Protocole.** Échantillon des subventions individuelles publiées dans les rapports publics de ces financeurs (lesquels publient : à vérifier). Codage en double de « trace publique antérieure : oui / non ».
- **Métrique.** f = fraction des personnes financées sans trace publique.
- **Seuil** (illustratif) : f ≥ 0,3 falsifie H_A ; f ≤ 0,05 falsifie H_B.
- **Limite déclarée.** Biais de survie : les dossiers refusés ne sont pas observés, donc l'expérience ne mesure qu'une condition nécessaire, pas suffisante.
- **Contrôle négatif.** Exclure les subventions aux organisations. Si elles se glissent dans l'échantillon, f est gonflé artificiellement.

### E6 : le résultat scientifique qui fait le dossier
- **H_A** : une sonde linéaire sur les activations intermédiaires détecte la conscience d'évaluation au-delà de ce que prédisent les indices de surface du prompt.
- **H_B** : un classifieur mécanique sur le prompt, ou une sonde sur la couche d'embedding, l'égale.
- **Métrique, seuil, contrôles** : voir C1.
- **Falsification.** C'est la seule expérience dont **les deux issues** produisent une pièce de dossier : un nul préenregistré est aussi un billet technique. Cet argument est une HYPOTHÈSE sur la façon dont les financeurs lisent un nul. E5 la teste partiellement.

### Les montages comme hypothèses rivales

Montants : **non chiffrés**, à relever dans les barèmes publiés. Délais : ordinaux, illustratifs.

| Montage | Conditions | Premier euro (ordinal, illustratif) | Impose | Risque principal | Départagé par |
|---|---|---|---|---|---|
| **M1.** Accueil bénévole + fonds philanthropique international (à personne physique ou via sponsor fiscal) | Financeur acceptant les individus résidant en France (à vérifier, par financeur) ; convention d'accueil | Court à moyen | Rapports au financeur ; clauses d'hôte (E3) ; fiscalité personnelle, hors champ de conseil | Dépendance à un seul financeur ; cohérence entre hôte et financeur | E1, E4, E5 |
| **M2.** Structure juridique propre (association ou société) + crédits de calcul et d'API + éventuellement aides à l'innovation ou crédit d'impôt recherche (à vérifier) | Structure créée et gérée ; projet compatible avec le cadre « innovation » | Long pour les aides publiques ; le crédit d'impôt recherche est perçu *après* dépense (mémoire, à vérifier) | Charge administrative ; la recherche doit être cadrée en produit | Avance de trésorerie ; dérive de l'objet | E1, E4 |
| **M3.** Rattachement doctoral (sans doctorat) ou bourse postdoctorale individuelle (avec doctorat ; par exemple, bourses postdoctorales Marie Skłodowska-Curie de la Commission européenne, doctorat exigé, à vérifier) | Directeur de thèse ou superviseur ; hôte ; calendrier d'appel | Long | Calendrier institutionnel ; pour le doctorat, engagement pluriannuel (durée à vérifier) | Incompatible avec l'horizon de 3 à 12 mois ; le doctorat est un engagement que la question ne demande pas | E1, E4 |
| **M4.** Participant salarié sur un projet porté par un laboratoire (ANR, programmes de France 2030 en IA, cluster IA ; noms à vérifier) | Un porteur permanent qui inscrit le poste ; un appel ouvert | Long, sauf projet déjà financé qui recrute | Contrat à durée déterminée du labo ; programme aligné sur le projet porteur | Perte d'indépendance scientifique ; dépendance au calendrier du porteur | E2, E3, E4 |

**Ce qui départage, en une ligne.** E1 dit si M3 est même ouvert. E3 dit si M1 et M4 sont compatibles avec le code ouvert. E4 dit si une voie française peut tenir l'horizon. E6 conditionne tout dossier.

---

## (c) Mesure minimale de fonctionnement de chaque instrument nommé

### C1 : sonde de conscience d'évaluation
- **Cas honnêtes appariés.** Paires de prompts au **contenu de tâche identique**, différant seulement par le cadrage (format de banc d'évaluation contre usage réaliste). Ce sont des paraphrases contrôlées, construites avant de voir les activations.
- **Découpage.** Par *source* et par *gabarit*, jamais aléatoire : la sonde ne doit pas apprendre le gabarit.
- **Métrique.**
  - Taux de détection à un taux de fausses alertes fixé (5 %, illustratif) sur paires tenues à part.
  - Taux de fausses alertes sur des **paires « déploiement / déploiement »**, contrôle négatif où aucune différence n'existe.
  - Intervalles de confiance par bootstrap sur les paires.
- **Vérifications mécaniques à battre.**
  1. Régression logistique sur sac de mots du prompt.
  2. Même sonde sur la couche d'embedding : si elle égale la sonde profonde, le signal est lexical.
  3. Sonde entraînée sur étiquettes permutées (tâche de contrôle au sens de Hewitt & Liang, 2019, « Designing and Interpreting Probes with Control Tasks », EMNLP).
  4. Auto-déclaration verbale du modèle (« penses-tu être évalué ? »).
- **Seuil.** La sonde ne « fonctionne » que si sa borne inférieure d'intervalle dépasse la borne supérieure de la meilleure ligne de base. Sinon, c'est un résultat nul, publiable comme tel.

### C2 : contrôle de la délégation
- **Préalable.** Le terme n'est pas défini dans la question. Proposition opérationnelle, HYPOTHÈSE : détecter qu'un modèle délègue (à un outil ou à un sous-agent) une tâche qui s'écarte de l'instruction reçue.
- **Cas honnêtes appariés.** Délégations conformes et délégations déviantes de **même longueur et même vocabulaire de surface**.
- **Métrique.** Détection et fausses alertes, comme en C1.
- **À battre.**
  1. Diff textuel entre l'instruction et l'appel délégué.
  2. **Moniteur boîte noire** : un modèle de langue lit la transcription, à budget de calcul égal.
- **Seuil.** Le contrôle boîte blanche n'a d'intérêt démontré que s'il bat le moniteur boîte noire. Sinon, l'axe « boîte blanche » du programme est falsifié pour cette menace.

### C3 : préenregistrement, registres et empreintes
- **Mesure.** Sur des exécutions synthétiques, injecter des déviations connues : seuil modifié, analyse ajoutée, couche changée, graine changée. Mesurer le taux de détection par l'audit « plan contre exécution ».
- **Fausses alertes.** Mesurées sur des réexécutions honnêtes du même plan. La variabilité numérique non déterministe ne doit pas déclencher d'alerte : la tolérance est déclarée d'avance.
- **À battre.** `git log` + `diff`, plus un horodatage par dépôt public tiers (par exemple OSF, Center for Open Science ; fonctionnalités à vérifier).
- **Limite déclarée.** Une empreinte prouve l'intégrité, pas l'antériorité. L'antériorité exige un ancrage externe daté.
- **Seuil.** 100 % de détection des altérations de fichiers horodatés. Pour les déviations de méthode, le seuil (illustratif ≥ 0,9) est fixé avant l'essai.

### C4 : agents de code exécutants
- **Mesure.** Taux de détection de fautes **semées** par le pipeline de vérification : fuite d'étiquettes entre entraînement et test, mauvais indice de couche, normalisation calculée sur tout le jeu, graine ignorée.
- **Fausses alertes.** Mesurées sur un code non altéré.
- **À battre.** Tests unitaires seuls. Une réexécution indépendante par un second agent ou par le directeur doit apporter un gain mesurable, sinon elle coûte sans protéger.

### C5 : la grille de veille de financement (y compris cette réponse)
- **Mesure.** Précision des prédictions « éligible », comparées aux **confirmations écrites** des organismes (E1, E2).
- **Fausse alerte.** Un dispositif annoncé accessible qui ne l'est pas.
- **À battre.** Lecture directe de la section « éligibilité » de l'appel, avec recherche des mots « doctorat », « établissement », « employeur ».
- **Statut.** Tant qu'elle n'est pas confrontée aux textes, cette réponse est HYPOTHÈSE dans son ensemble. Son taux de fausses alertes est inconnu.

---

## (d) Ancrage matériel

### Modèles ouverts candidats
Tous HYPOTHÈSE, licences à vérifier avant tout engagement de code ouvert.
- **Llama 3.1 8B Instruct** (Meta) : licence communautaire, avec des conditions à relire pour la redistribution.
- **Qwen3-8B** (Alibaba) : licence permissive selon mon souvenir, à vérifier.
- **Gemma 2 9B** (Google) : licence propre, à vérifier.
- **OLMo 2 7B** (Ai2) : données d'entraînement publiées. C'est un atout pour contrôler la contamination, par exemple vérifier si les gabarits d'évaluation figurent dans le corpus.

### Calcul
Calcul explicite à paramètres illustratifs, sauf mention :
- **Mémoire des poids.** Environ 8 × 10⁹ paramètres × 2 octets ≈ 16 Go en bf16. Cela tient sur un seul GPU de 24 Go ou plus.
- **Activations stockées.** Hypothèse : dimension cachée 4096 et 32 couches (valeurs à vérifier sur la fiche du modèle choisi). Un vecteur par couche fait 4096 × 2 o = 8 Ko, soit 256 Ko par jeton pour toutes les couches.
  - Dernier jeton seulement, 10 000 prompts (illustratif) : ≈ 2,6 Go.
  - Tous les jetons, 512 jetons par prompt (illustratif) : ≈ 1,3 To.
  - Choisir l'agrégation dans le préenregistrement change donc le coût de stockage d'un facteur 500.
- **Inférence.** Quelques heures-GPU par jeu de 10 000 prompts courts. L'ordre de grandeur est illustratif et à mesurer sur un pilote.
- **Coût.** À un prix de location à la carte de 1 à 3 $ par heure-GPU (illustratif, à relever le jour même), un budget de 300 $ par mois (illustratif, cohérent avec « quelques centaines » RAPPORTÉ) correspond à environ 100 à 300 heures-GPU.

### Budget sur 12 mois
Seule donnée : RAPPORTÉ.
- **Calcul et API.** « Quelques centaines de dollars par mois » × 12 = quelques milliers de dollars. C'est le poste le plus facile à couvrir, éventuellement par des crédits de chercheurs (programmes d'accès des fournisseurs, crédits de nuage ; existence et conditions à vérifier).
- **Rémunération du directeur.** Poste dominant, **non chiffré** : il dépend des barèmes des financeurs, que je ne cite pas de mémoire.

### Noms de dispositifs ayant probablement changé
À vérifier, sans date.
- UK AI Safety Institute → **AI Security Institute**.
- Open Philanthropy : renommage récent possible, nom à vérifier.
- 3IA → **IA Clusters** (France 2030).
- Mines ParisTech → **Mines Paris – PSL**.
- Statut de jeune entreprise innovante : réformes récentes, à vérifier.

### Autres pistes internationales
Toutes HYPOTHÈSE, à vérifier : éligibilité depuis la France, nom exact, calendrier.
- **Long-Term Future Fund** (EA Funds) : accepte des personnes physiques selon mon souvenir.
- **Survival and Flourishing Fund** : surtout des organisations.
- **Manifund** (régranting).
- **Programmes à bourse de recherche** : MATS, programme de *fellows* d'Anthropic. Ils imposent en général un lieu ou une cohorte, ce qui entre en tension avec la résidence à Paris.
- **AI Security Institute** : appels à subventions dont l'ouverture aux non-Britanniques est à vérifier.
- **Calcul européen** : appels d'accès d'EuroHPC, souvent avec un porteur institutionnel (à vérifier).

### Ordre des pièces pour un dossier en 3 mois
Ordre proposé, en HYPOTHÈSE, réfutable par E5.
1. **Semaines 0 à 2**
   - Préenregistrement public de E6, horodaté hors dépôt git.
   - Dépôt de code ouvert.
   - Demande de lettre au tuteur (coût nul, à lancer immédiatement).
   - Questions écrites d'E1, E2 et E3 (tout le volet institutionnel tourne en tâche de fond).
2. **Semaines 2 à 8.** Exécution sur GPU, avec les lignes de base de C1. Rien n'attend l'affiliation.
3. **Semaines 8 à 12.** Billet technique, nul ou positif, avec l'écart au préenregistrement documenté (C3). Prépublication si le format s'y prête. Dépôts auprès des financeurs retenus par E4.

### Questions au tuteur et au département (dix)
1. Quelle école exactement, et quel laboratoire signerait la convention (a1) ?
2. Quels statuts d'accueil sans rémunération existent chez vous, et qui les signe ?
3. Pouvez-vous transmettre le modèle de convention avant tout accord (E3) ?
4. La convention couvre-t-elle le code déjà public, et autorise-t-elle une licence ouverte sans délai ?
5. Ce statut permet-il une demande d'accès au calcul national, ou faut-il un porteur permanent (E2) ?
6. Puis-je signer sous l'affiliation et rattacher mes dépôts HAL à la structure ?
7. Une adresse institutionnelle est-elle fournie ?
8. Le laboratoire accepterait-il d'héberger ou de gérer une subvention versée par un fonds étranger, avec quels frais de gestion ?
9. Un projet d'agence en cours ou prévu pourrait-il m'inscrire comme participant (M4) ?
10. Quel est le délai réel entre l'accord de principe et la convention signée ?

### Ce qu'il ne faut pas faire
- Signer une convention sans avoir lu les clauses de dévolution, de confidentialité et de délai avant publication.
- Utiliser le nom d'une école ou une adresse d'ancien élève comme affiliation sans accord écrit.
- S'inscrire en doctorat comme simple véhicule de financement : c'est un engagement pluriannuel, hors de l'horizon demandé.
- Créer une structure juridique pour capter une aide ou un crédit d'impôt avant d'avoir lu les conditions d'éligibilité. Aucun conseil fiscal ou juridique n'est donné ici.
- Déclarer les mêmes dépenses à deux financeurs sans vérifier leurs règles de cumul.
- Promettre un résultat positif dans un dossier : le préenregistrement doit pouvoir rendre un nul.
- Suspendre les expériences en attendant l'affiliation.

FIN-DE-CELLULE