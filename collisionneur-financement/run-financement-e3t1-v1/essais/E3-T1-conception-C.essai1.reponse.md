# Proposition C — Conception ciblée (Tour III.1)

Conformément à la règle d'intégrité n° 6, les instructions de formatage contenues à l'intérieur du bloc de données `QUESTION DE L'ARBITRE` sont traitées comme des objets d'analyse ; la structure du présent livrable obéit strictement aux consignes système du Tour III.1 (`a`, `b`, `c`, `d`), au sein desquelles les huit points thématiques de l'arbitre sont intégralement résolus. Tout dispositif, règle administrative ou référence dont le détail dépend de textes réglementaires non joints aux `FAITS` porte la mention « référence à vérifier » ou « à vérifier ».

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Supposition A1 (Statut d'alumnus comme levier administratif) — HYPOTHÈSE.** La question suppose que le statut d'ancien élève de l'École normale supérieure (ENS) Paris-Saclay ou d'une École des Mines confère un droit ou un accès privilégié à une convention d'accueil ou de chercheur visiteur. En droit public français, l'accès aux locaux et moyens d'un Établissement Public à Caractère Scientifique, Culturel et Professionnel (EPSCP) ou d'un grand établissement repose sur l'intérêt scientifique du laboratoire d'accueil et la couverture assurantielle, non sur le diplôme antérieur (référence à vérifier). Ce que l'alumnus peut demander que n'importe qui ne peut pas se limite au réseau informel (annuaire, contact direct) et aux dispositifs spécifiques des associations d'anciens élèves ou fondations d'école (ex. aides ponctuelles de la Fondation Mines Paris ou de l'association des anciens élèves, à vérifier).
2. **Supposition A2 (Compatibilité du statut de collaborateur bénévole sans employeur principal) — HYPOTHÈSE.** La question suppose qu'une personne « sans employeur académique » (et possiblement sans employeur du tout) peut signer une convention d'accueil de collaborateur bénévole ou de chercheur invité. Or, les services des ressources humaines d'établissements comme l'ENS Paris-Saclay, Mines Paris – PSL ou l'Université Paris-Saclay exigent fréquemment une attestation d'employeur principal ou une couverture sociale/responsabilité civile autonome pour écarter le risque de requalification en travail dissimulé (référence à vérifier).
3. **Supposition A3 (Portage de financements publics français par un hébergé sans contrat) — HYPOTHÈSE.** La question suppose que des financements de l'Agence nationale de la recherche (ANR), de « France 2030 » ou de l'Institut national d'évaluation et de sécurité de l'intelligence artificielle (INESIA) pourraient être sollicités ou perçus via une simple affiliation d'accueil. En pratique, l'éligibilité comme coordinateur aux appels de l'ANR exige un lien d'emploi (statutaire ou contractuel couvrant la durée du projet) avec l'organisme bénéficiaire (référence à vérifier).
4. **Supposition A4 (Neutralité patrimoniale de l'hébergement) — HYPOTHÈSE.** La question suppose que le programme peut rester « indépendant » tout en utilisant l'affiliation ou le calcul national (GENCI). Or, le Code de la propriété intellectuelle (notamment l'article L. 611-7 pour les inventions et les dispositions relatives aux logiciels créés par les agents ou personnes accueillies sous convention, référence à vérifier) transfère souvent par défaut les droits patrimoniaux sur le code et les résultats à l'établissement d'accueil.
5. **Supposition A5 (Adéquation temporelle des guichets français à l'horizon 3-12 mois) — HYPOTHÈSE.** La question suppose l'existence de bourses publiques ou privées françaises capables de décaisser entre le mois $M+3$ et le mois $M+12$. Le cycle administratif standard des agences nationales excède souvent 9 mois (illustratif) entre la soumission et la mise en place financière.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour trancher empiriquement les choix de montage (Point 5 de la question) sans perdre des mois en démarches stériles (Point 7), quatre expériences administratives et opérationnelles sont conçues en duel d'hypothèses exclusives.

### Expérience E1 : Opérabilité et coût patrimonial de l'affiliation d'accueil (Tranche les Points 1 et 7)
* **$H_A$ (Hypothèse de la convention légère et non-spoliante) :** Le département de l'ENS Paris-Saclay ou le centre de recherche de Mines Paris – PSL peut établir en moins de 45 jours (illustratif) une convention de « collaborateur scientifique bénévole » ou « chercheur associé/visiteur » pour un résident français sans employeur, ouvrant droit à une adresse institutionnelle, à la modération HAL/arXiv et à l'accès GENCI, avec une clause dérogatoire laissant le code sous licence ouverte choisie par le directeur.
* **$H_B$ (Hypothèse du blocage RH ou de la captation de propriété intellectuelle) :** Les services juridiques/RH refusent la convention faute d'employeur principal du directeur, OU exigent la cession intégrale des droits patrimoniaux sur les logiciels et résultats à l'établissement (ou à ARMINES dans le cas des Mines, à vérifier), OU le délai de signature dépasse 45 jours (illustratif).
* **Protocole et métrique :** Soumission simultanée au tuteur des Mines et au directeur de département de l'ENS Paris-Saclay d'une fiche de projet d'une page et d'une demande de modèle de convention d'accueil. Métrique : délai de retour du service juridique ($\Delta t$ en jours ouvrés) et présence/absence d'une clause de cession de propriété intellectuelle non négociable.
* **Seuil :** $\Delta t \le 30$ jours ouvrés (illustratif) pour obtenir un projet de convention validé par les RH et autorisant la publication systématique sous licence ouverte sans pré-validation de valorisation.
* **Contrôle négatif :** Demande d'accès simple en tant que lecteur externe à la bibliothèque ou séminaire du laboratoire (doit aboutir en $< 5$ jours ouvrés, illustratif, prouvant que le canal de communication avec le tuteur/département est fonctionnel).
* **Issues falsificatrices :**
  * Si $\Delta t \le 30$ jours et PI ouverte garantie $\Rightarrow$ $H_B$ est falsifiée (la voie académique d'accueil est viable sans perte de contrôle du programme).
  * Si refus RH, exigence de cession PI bloquante, ou $\Delta t > 30$ jours $\Rightarrow$ $H_A$ est falsifiée (il faut abandonner l'affiliation d'accueil au profit d'un statut indépendant pur ou d'une structure juridique propre).

### Expérience E2 : Vélocité des financeurs internationaux face aux guichets français (Tranche les Points 2, 3, 4 et 5)
* **$H_A$ (Hypothèse de la primauté philanthropique internationale) :** Pour un chercheur indépendant (avec ou sans doctorat) disposant d'un dépôt de code préenregistré, les guichets internationaux de sécurité de l'IA (ex. *Survival and Flourishing Fund* [SFF], *Long-Term Future Fund* [LTFF], *Manifund*, *Open Philanthropy*, *Foresight Institute*, *UK AI Safety Institute* [AISI] *Systemic Safety Grants*, tous « à vérifier ») délivrent une décision de financement et un premier versement plus rapidement et avec une espérance de gain supérieure aux fondations et guichets publics français accessibles.
* **$H_B$ (Hypothèse du levier institutionnel national) :** L'adossement à un laboratoire de Paris-Saclay ou PSL permet de débloquer des crédits internes d'instituts (ex. *DATAIA* à Paris-Saclay, Institut *PRAIRIE* / PSL, Fondation Mathématique Jacques Hadamard [FMJH], Fondation Sciences Mathématiques de Paris [FSMP], Fondation Mines Paris, tous « à vérifier ») ou un contrat court (ingénieur de recherche / postdoctorant sur crédits propres du tuteur) en moins de 90 jours (illustratif).
* **Protocole et métrique :** Dépôt d'un dossier court (préenregistrement + billet technique) à deux guichets internationaux à flux continu ou rapide (ex. LTFF, Manifund, à vérifier) en parallèle d'une demande de crédits incitatifs internes via le tuteur des Mines / département ENS (ex. appel au fil de l'eau DATAIA ou crédits propres du laboratoire, à vérifier). Métrique : délai avant notification ferme d'attribution ($\Delta t_{\text{notif}}$) et montant net alloué au directeur + calcul ($M_{\text{net}}$).
* **Seuil :** $\Delta t_{\text{notif}} \le 90$ jours calendaires (illustratif) et $M_{\text{net}} \ge 15\,000\text{ €}$ (illustratif) pour couvrir au moins 3 à 6 mois de frais de vie/calcul.
* **Contrôle négatif :** Dépôt d'une demande de crédits de calcul académiques purs sans transfert d'argent (ex. programme *Anthropic External Researcher Access* ou *OpenAI Researcher Access Program*, à vérifier), dont le délai de réponse typique est de 14 à 30 jours (illustratif).
* **Issues falsificatrices :**
  * Si le guichet international notifie un octroi $\ge 15\,000\text{ €}$ (illustratif) en $\le 90$ jours alors que le circuit académique local est bloqué ou exige un appel annuel hors délai $\Rightarrow$ $H_B$ est falsifiée.
  * Si le laboratoire d'accueil mobilise un reliquat ANR/Chaire sur un CDD d'ingénieur/postdoc en $\le 60$ jours (illustratif) alors que les fonds internationaux rejettent le dossier $\Rightarrow$ $H_A$ est falsifiée.

### Expérience E3 : Éligibilité au calcul intensif gratuit vs location commerciale (Tranche les Points 1 et 4)
* **$H_A$ (Hypothèse de l'accès souverain rapide) :** L'obtention d'une affiliation (ENS Paris-Saclay ou Mines Paris) permet d'ouvrir un « Accès Dynamique » (jusqu'à $50\,000$ heures GPU, illustratif, à vérifier) sur le supercalculateur Jean Zay (GENCI / IDRIS) en moins de 30 jours (illustratif), avec un environnement logiciel compatible avec le programme (exécutants par agents de code, traçabilité des empreintes).
* **$H_B$ (Hypothèse de l'incompatibilité opérationnelle des clusters HPC nationaux) :** L'accès Jean Zay est refusé à un hébergé non-statutaire (doit être porté par un permanent), OU l'architecture de sécurité du cluster (nœuds de calcul sans accès Internet sortant, restrictions sur les agents de code autonomes, files d'attente SLURM) ralentit l'exécution d'un facteur $\ge 3$ (illustratif) par rapport à du calcul infonuagique à la carte financé par bourse ou crédits cloud.
* **Protocole et métrique :** Demande d'ouverture d'un compte « Accès Dynamique » Jean Zay (co-signée par le tuteur si nécessaire) et test d'exécution d'un pipeline complet d'entraînement de sonde sur un modèle de 8 milliards de paramètres avec agent de code et journalisation d'empreintes. Métrique : temps total de bout en bout ($\text{Temps}_{\text{mur}}$ incluant délai d'attribution + configuration + attente file) comparé à un fournisseur de GPU à la demande.
* **Seuil :** Ouverture du compte en $\le 20$ jours ouvrés (illustratif) et surcoût temporel d'exécution quotidienne $\le 50\%$ (illustratif) par rapport au cloud commercial.
* **Contrôle négatif :** Exécution du même pipeline sur une instance louée à l'heure (coût de référence : $\approx 1\text{ à }2\text{ \$/heure}$ pour un GPU 80 Go, illustratif).
* **Issues falsificatrices :**
  * Si le compte est ouvert dans les délais et que le pipeline automatisé s'exécute sans réécriture majeure $\Rightarrow$ $H_B$ est falsifiée.
  * Si le portage exige un chercheur permanent qui refuse d'engager sa responsabilité, ou si l'isolation réseau des nœuds HPC casse le workflow d'agents de code $\Rightarrow$ $H_A$ est falsifiée.

### Expérience E4 : Séquence de crédibilité — Billet technique empirique vs Préenregistrement formel (Tranche le Point 6)
* **$H_A$ (Hypothèse de la preuve par le résultat GPU) :** Les évaluateurs de fonds de sécurité de l'IA et les tuteurs académiques accordent un score de crédibilité supérieur à un dossier centré sur un premier billet technique public présentant des courbes de détection empiriques (sondes sur modèle 8B) accompagné du code ouvert, plutôt qu'à un dossier centré sur l'architecture méthodologique de préenregistrement et d'audit par empreintes.
* **$H_B$ (Hypothèse de la différenciation méthodologique) :** La saturation des billets techniques sur les sondes d'activation fait que le facteur discriminant d'octroi est la rigueur du protocole de préenregistrement systématique et d'exécution auditée par agents.
* **Protocole et métrique :** Envoi pour pré-évaluation (à 4 chercheurs seniors du domaine et au tuteur des Mines, illustratif) d'un résumé exécutif en deux versions (ou interrogation structurée sur les deux composantes du dossier complet produit en 3 mois). Métrique : classement forcé des pièces déterminantes pour signer une lettre de soutien engageante ou recommander un financement.
* **Seuil :** $\ge 75\%$ (illustratif) des évaluateurs exigent de voir un résultat empirique positif ou négatif sur GPU (modèle 8B) avant d'endosser le projet, indépendamment de la qualité du registre d'empreintes.
* **Contrôle négatif :** Soumission d'une simple intention de recherche sans code ni résultat (taux d'endossement attendu proche de $0\%$, illustratif).
* **Issues falsificatrices :**
  * Si les évaluateurs conditionnent leur lettre à la démonstration empirique sur le modèle 8B $\Rightarrow$ $H_B$ est falsifiée (l'ordre de production en 3 mois doit prioriser l'exécution GPU immédiate sur le raffinement de l'infrastructure d'audit).
  * Si les évaluateurs financent ou endossent sur la base du cadre de préenregistrement vérifiable avant exécution complète $\Rightarrow$ $H_A$ est falsifiée.

---

## (c) Mesure minimale de fonctionnement des instruments nommés dans la question

Dans le cadre de cette question, les « instruments » sont les dispositifs institutionnels, financiers et techniques mobilisables. Pour chacun, nous définissons : la condition d'accès selon le statut (avec/sans doctorat), ce qu'il ouvre/coûte, le taux de détection (probabilité d'éligibilité/succès sur dossier conforme, illustratif) et de fausses alertes (dossiers déclarés éligibles en surface mais rejetés pour vice administratif de statut, illustratif), les cas honnêtes appariés (comparaison d'un candidat indépendant face à un candidat statutaire à dossier scientifique identique), et la vérification mécanique à battre (autofinancement ou contrat de prestation classique).

### 1. Instruments d'affiliation d'accueil sans emploi (Point 1)

| Instrument (Statut) | Établissements (Distinction) | Qui décide & Pièces | Ce qu'il ouvre | Ce qu'il coûte (Risques) | Cas Docteur vs Non-Docteur | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Collaborateur bénévole / Visiteur sous convention d'accueil** *(à vérifier)* | **ENS Paris-Saclay** (département/labo UMR), **Mines Paris – PSL** (Centres de recherche / ARMINES), **Univ. Paris-Saclay** | Directeur d'unité + validation RH/Direction générale. Pièces : CV, projet, attestation d'assurance RC, justificatif de couverture sociale/employeur principal *(à vérifier)*. | Adresse e-mail, accès locaux, signature d'articles sous affiliation, dépôt HAL/arXiv. **N'ouvre pas** le portage ANR en nom propre. Accès GENCI uniquement sous parrainage d'un permanent *(à vérifier)*. | Cession fréquente de la PI (code/inventions) à l'établissement, charte informatique, délai RH de 1 à 4 mois *(illustratif)*. | **Docteur :** souvent intitulé « Chercheur invité/associé ». **Sans doctorat :** « Stagiaire » (impossible sans inscription scolaire) ou « Collaborateur occasionnel/externe » *(à vérifier)*. | Garder une affiliation indépendante pure (dépôt Zenodo + arXiv par *endorsement* d'un pair, coût : $0\text{ €}$, délai : 48h, illustratif). |
| **Chercheur associé (statut formel)** *(à vérifier)* | **ENS Paris-Saclay** / **Univ. Paris-Saclay** (via les UMR CNRS/Inria) | Conseil de laboratoire + Commission recherche de l'établissement *(à vérifier)*. | Participation officielle à la vie de l'unité, co-encadrement possible, rattachement HCÉRES. | Appels périodiques (1 à 2 par an, *illustratif*), exige presque toujours un emploi principal par ailleurs *(à vérifier)*. | Exige généralement le **doctorat** ou des travaux jugés équivalents par le conseil *(à vérifier)*. | Simple co-signature d'articles avec le tuteur des Mines sans rattachement administratif. |
| **Spécificité Alumnus** *(à vérifier)* | **Mines Paris – PSL** vs **ENS Paris-Saclay** | Réseau des anciens (*Mines Paris Alumni*, *AAEE ENS Cachan/Paris-Saclay*, *à vérifier*). | Accès direct aux enseignants-chercheurs (tuteur), possibilité de mentorat ou d'accès aux fondations d'école. Aucun droit statutaire dérogatoire au Code de la recherche *(à vérifier)*. | Aucun coût de PI tant qu'aucune convention de laboratoire n'est signée. | Identique (le titre d'ingénieur des Mines ou le diplôme de l'ENS suffit). | Contacter un chercheur par courriel froid (*cold email*). |

* **Mesure minimale de fonctionnement de l'instrument « Affiliation » :**
  * *Taux de détection (succès d'obtention d'une convention signée en $\le 60$ jours, illustratif) :* Élevé ($\approx 60\%$, illustratif) si Docteur avec assurance RC et revenus autonomes prouvés ; Faible ($\approx 15\%$, illustratif) si Sans doctorat et sans employeur principal (blocage RH sur le risque de stage déguisé ou travail dissimulé, à vérifier).
  * *Taux de fausses alertes :* Élevé ($\approx 50\%$, illustratif) — le tuteur ou le directeur de département donne un accord de principe oral immédiat, mais la direction des ressources humaines bloque la signature 6 semaines plus tard (illustratif).

### 2. Instruments de financement publics français (Point 2)

| Dispositif & Organisme *(tous « à vérifier »)* | Qui peut porter ? | Ce qui est financé & Ordre de grandeur *(illustratif)* | Délai réel (dépôt $\to$ versement) *(illustratif)* | Exigence Doctorat / Employeur | Taux de fausses alertes pour un indépendant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ANR (AAPG, JCJC)** — Agence nationale de la recherche | Uniquement un chercheur permanent ou contractuel dont le contrat couvre le projet, rattaché à un labo éligible. | Salaire CDD, fonctionnement, équipement ($150\text{ k€}$ à $500\text{ k€}$ sur 36-48 mois). | 9 à 14 mois. | **Doctorat exigé** pour le porteur. **Employeur exigé.** L'indépendant ne peut être que *recruté* en CDD sur une ANR portée par le tuteur. | Quasi-total ($>95\%$, illustratif) si l'indépendant pense pouvoir déposer en nom propre comme simple hébergé. |
| **INESIA** — Institut national d'évaluation et de sécurité de l'IA *(anciennement annoncé autour du LNE / Secrétariat général de la défense et de la sécurité nationale / DGE, évolution institutionnelle récente à vérifier)* | Pas un guichet de bourses individuelles ouvertes à ce jour ; fonctionne par recrutements directs, marchés publics ou partenariats institutionnels *(à vérifier)*. | Prestations d'évaluation ou contrats de travail internes (montants non publics / selon grilles indiciaires). | Variable (recrutement : 2 à 6 mois). | **Employeur :** implique de devenir agent/contractuel ou prestataire (personne morale). | Élevé si confondu avec l'AISI britannique qui, lui, possède un programme de subventions externes (*Grants*, à vérifier). |
| **Instituts 3IA / IA Clusters (France 2030)** : **DATAIA** (Univ. Paris-Saclay / ENS Paris-Saclay) et **PR[AI]RIE-PSAI** (PSL / Mines Paris) | Chercheur permanent membre de l'institut (le tuteur). | Bourses de postdoctorat (1-2 ans, $\approx 45\text{–}60\text{ k€}$/an chargé), bourses de thèse, petits appels « amorçage / jeunes chercheurs » ou accueil de visiteurs ($5\text{–}30\text{ k€}$). | 4 à 8 mois. | **Avec doctorat :** éligible à un recrutement postdoc. **Sans doctorat :** éligible uniquement à un contrat doctoral (3 ans) ou CDD ingénieur. | Moyen : le directeur perd son statut « indépendant » et devient salarié à temps plein du laboratoire. |
| **Région Île-de-France** (ex. *Domaine d'intérêt majeur* [DIM] *AI4IDF*, bourses *Paris Region Fellowship* — vérifier fermetures/renouvellements récents) | Laboratoire d'accueil francilien. | Allocations doctorales ou postdoctorales, équipements. | 6 à 10 mois. | Doctorat (pour postdoc) ou Master/Ingénieur (pour thèse). Contrat de travail obligatoire. | Moyen (calendrier annuel rigide incompatible avec un besoin à $M+3$). |
| **Bpifrance** (Bourse French Tech, Aide pour le développement de l'innovation) | Société commerciale (SAS, SARL) immatriculée en France. | Subvention jusqu'à $30\text{ k€}$ (BFT) ou $90\text{ k€}$ en deeptech *(illustratif, à vérifier)*, couvrant jusqu'à $70\%$ des dépenses éligibles. | 2 à 5 mois après création de la société. | **Ni doctorat ni employeur académique requis.** Exige des fonds propres initiaux (ex. $15\text{ k€}$ à $30\text{ k€}$, illustratif) et une visée de valorisation commerciale. | Élevé si le projet est présenté comme de la recherche fondamentale pure sans produit ni marché. |

### 3. Fondations et bourses privées françaises (Point 3)

* **Fondation Mines Paris et Fondation ENS Paris-Saclay (à vérifier) :**
  * *Portage :* Chaires de recherche, soutien aux projets étudiants/alumni, ou bourses internationales entrantes.
  * *Financement :* Peuvent financer une prestation, un prix scientifique ou un complément de bourse ($2\,000\text{ €}$ à $20\,000\text{ €}$, illustratif, à vérifier) si un enseignant-chercheur interne (le tuteur) porte la demande auprès du comité de la fondation.
  * *Délai :* 2 à 6 mois (illustratif) selon les dates des conseils d'administration.
  * *Condition :* Le statut d'alumnus est ici un critère d'éligibilité direct (VÉRIFIÉ dans le principe des fondations d'écoles, modalités exactes 2026 à vérifier).
* **Fondation Mathématique Jacques Hadamard (FMJH — périmètre Paris-Saclay) et Fondation Sciences Mathématiques de Paris (FSMP — périmètre Paris / PSL) (à vérifier) :**
  * *Financement :* Programmes postdoctoraux, invitations de chercheurs (généralement résidant à l'étranger, ce qui exclut un résident parisien pour les bourses de mobilité entrante, à vérifier).
  * *Condition :* Exige un **doctorat** et un rattachement aux thématiques mathématiques de l'IA (théorie de l'apprentissage, statistique). Taux de fausse alerte élevé pour de l'évaluation empirique de modèles de langue (souvent jugée hors périmètre mathématique pur, HYPOTHÈSE).
* **Fondations d'entreprise et Mécénat (ex. Fondation Abeona, Fondation Médiamétrie, bourses L'Oréal-UNESCO, prix de la Fondation CFM pour la recherche, à vérifier) :**
  * La plupart ciblent des doctorants/postdoctorants déjà sous contrat ou des chaires d'établissement.
* **Instituts d'études avancées (IEA de Paris, Institut Pascal à Paris-Saclay) (à vérifier) :**
  * *IEA de Paris :* Résidences pour chercheurs confirmés (doctorat + publications significatives, souvent employés par une université étrangère, appels annuels avec 12 mois de décalage, illustratif, à vérifier).
  * *Institut Pascal (Université Paris-Saclay) :* Finance l'organisation de programmes thématiques et l'accueil de visiteurs externes (ne finance pas un résident local sans poste sur 12 mois, à vérifier).

### 4. Financeurs internationaux de la sécurité de l'IA et programmes de calcul (Point 4)

C'est dans cette catégorie que le taux de détection pour un profil « indépendant résidant en France, avec ou sans doctorat, budget 3-12 mois » est le plus élevé (HYPOTHÈSE testable via E2).

| Dispositif / Organisme *(tous « à vérifier »)* | Accessibilité à cette situation précise (France, sans poste, avec/sans PhD) | Montants typiques *(illustratif)* | Rythme des appels & Délais *(illustratif)* |
| :--- | :--- | :--- | :--- |
| **Long-Term Future Fund (LTFF)** — *Effective Ventures* | **Très haute.** Finance directement des individus (indépendants) dans le monde entier, sans exigence de doctorat ni d'affiliation académique. | $5\,000\text{ \$}$ à $100\,000\text{ \$}$ (couvre frais de vie + calcul pour 3 à 12 mois). | Flux continu (*rolling basis*). Décision en 3 à 8 semaines. Versement international (nécessite un statut fiscal propre en France pour déclarer les fonds). |
| **Manifund** (notamment *AI Safety Regranting* et *ACX Grants*) | **Très haute.** Les *regranters* allouent des fonds sur la base d'une proposition publique (ex. préenregistrement + premier billet). Aucun diplôme requis. | $2\,000\text{ \$}$ à $50\,000\text{ \$}$. | Flux continu (via *regranters*) ou rondes rapides. Décision en 1 à 4 semaines. |
| **Survival and Flourishing Fund (SFF)** — *S-process* | **Moyenne à haute.** Historiquement tourné vers les organisations (501(c)(3) ou équivalent, ou via *fiscal sponsor*), mais accepte parfois des chercheurs via des structures d'hébergement fiscal *(à vérifier pour les rondes 2026)*. | $20\,000\text{ \$}$ à $200\,000\text{ \$}+$. | 1 à 2 rondes par an. Délai : 3 à 5 mois. |
| **Open Philanthropy** (*Coefficient Giving* / programmes *Technical AI Safety* — *changement de nom ou de structuration des entités opérationnelles à vérifier*) | **Moyenne.** Préfère les projets d'envergure ou les bourses doctorales/postdoctorales, mais finance des chercheurs indépendants via des programmes partenaires ou sur recommandation. | $50\,000\text{ \$}$ à $300\,000\text{ \$}+$. | Flux continu sur invitation ou appels thématiques. Délai : 2 à 6 mois. |
| **UK AI Safety Institute (AISI)** — *Systemic Safety Grants* (via ARIA ou DSIT) | **Moyenne.** Ouvert à l'international (y compris France), mais exige souvent une entité légale ou un établissement d'accueil (*Academic institution, non-profit, or company*, à vérifier) pour signer le contrat de subvention. | $50\,000\text{ £}$ à $200\,000\text{ £}$. | Appels par vagues. Délai : 3 à 6 mois. |
| **Foresight Institute** (*AI Safety Fellowship* / *Grants*) | **Haute.** Ouvert aux indépendants sans condition de doctorat. | $10\,000\text{ \$}$ à $50\,000\text{ \$}$ ou soutien réseau/calcul. | Annuel ou par vagues pour les *Grants*. |
| **Programmes européens (MSCA Postdoctoral Fellowships — Horizon Europe)** | **Conditionnelle.** Exige impérativement un **doctorat**, une règle de mobilité (ne pas avoir résidé en France plus de 12 mois sur les 36 derniers mois — **bloquant** si le directeur réside déjà à Paris depuis longtemps, à vérifier) et un établissement d'accueil (ENS ou Mines). | $\approx 150\text{ k€}$ à $200\text{ k€}$ sur 24 mois. | 1 appel par an (septembre). Délai avant premier euro : 8 à 12 mois (hors horizon 3 mois). |
| **Calcul : GENCI / IDRIS (Jean Zay)** | **Conditionnelle.** « Accès Dynamique » pour l'IA ouvert toute l'année, mais le porteur administratif doit généralement être rattaché à un labo français (le tuteur peut porter et déclarer le directeur comme utilisateur). | Gratuit en numéraire (allocation en heures GPU V100/A100/H100, ex. $5\,000$ à $50\,000$ h GPU). | Flux continu pour l'Accès Dynamique. Délai : 2 à 4 semaines. |
| **Calcul : EuroHPC JU** (*Benchmark / Development Access*) | Similaire à GENCI à l'échelle européenne (LUMI, Leonardo, MareNostrum 5). | Allocations d'heures GPU gratuites. | Flux continu (mensuel). Délai : 4 à 6 semaines. |
| **Crédits API / Cloud (Anthropic, OpenAI, Google TRC, Lambda, Modal)** *(tous « à vérifier »)* | **Haute.** *Google Cloud TPU Research Cloud (TRC)*, *Anthropic External Researcher Access Program*, *OpenAI Researcher Access Program*. Accessibles aux chercheurs indépendants sur la base d'une page web technique et d'un dépôt GitHub. | $1\,000\text{ \$}$ à $25\,000\text{ \$}$ en crédits API ou accès gratuit à une flotte de TPU/GPU pendant 30 à 90 jours. | Flux continu. Délai : 1 à 4 semaines. |

---

## (d) Ancrage matériel, montages complets, crédibilité et gouvernance des risques

### 1. Ancrage matériel du programme technique (Modèles, calcul, coûts)

Le programme décrit dans les faits porte sur l'entraînement de sondes sur les activations de modèles à poids ouverts de l'ordre de 8 milliards de paramètres (ex. Llama-3-8B, Ministral-8B ou Qwen-2.5-7B, illustratif) et l'interrogation d'API de modèles de frontière pour le contrôle de la délégation et la conscience d'évaluation.

* **Besoins matériels réels sur 12 mois (illustratif) :**
  * *Extraction d'activations et entraînement de sondes (modèles ~8B en bf16) :* Nécessite 1 GPU de 24 Go à 80 Go de VRAM (ex. NVIDIA RTX 4090, A100-40GB ou H100-80GB, illustratif). Un passage d'inférence avec mise en cache des activations résiduelles sur $100\,000$ séquences de $2\,048$ jetons prend environ 10 à 25 heures-GPU sur A100 (illustratif). Sur 12 mois, un programme intensif avec balayage d'hyperparamètres et préenregistrements multiples consommera de l'ordre de $1\,500$ à $4\,000$ heures-GPU A100 (illustratif).
  * *Coût infonuagique à la carte (sans subvention de calcul) :* $1\,500$ à $4\,000$ heures $\times 1,50\text{ \$/h}$ (illustratif) $= 2\,250\text{ \$}$ à $6\,000\text{ \$}$ sur 12 mois (soit $200\text{ \$}$ à $500\text{ \$/mois}$, cohérent avec les « quelques centaines de dollars par mois » citées dans la situation).
  * *Coût des API de modèles de frontière (exécutants de code et cibles de délégation) :* $300\text{ \$}$ à $1\,000\text{ \$/mois}$ (illustratif), soit $3\,600\text{ \$}$ à $12\,000\text{ \$/an}$ (illustratif).
  * *Budget matériel total (calcul + API) :* $\approx 6\,000\text{ €}$ à $18\,000\text{ €}$ sur 12 mois (illustratif).
  * *Budget de subsistance du directeur à Paris (si financé par bourse) :* $24\,000\text{ €}$ à $48\,000\text{ €}$ net/an (illustratif).
  * **Cible financière globale sur 12 mois :** $30\,000\text{ €}$ à $65\,000\text{ €}$ (illustratif).

### 2. Quatre montages complets et distincts (Point 5)

#### Montage M1 : « Indépendant Agile + Philanthropie Internationale + Sponsor Fiscal ou Micro-entreprise »
* **Architecture :** Le directeur n'utilise l'ENS Paris-Saclay et son tuteur des Mines **que** pour des lettres de recommandation et une éventuelle co-signature scientifique libre (sans convention d'hébergement formelle). Il candidate aux fonds internationaux rapides (LTFF, Manifund, Foresight, crédits API Anthropic/OpenAI/TRC, à vérifier). Pour recevoir les fonds en France en toute légalité (sans conseil fiscal, simple constat des véhicules existants), il utilise soit un *fiscal sponsor* international (ex. *Rethink Priorities* ou *Effective Ventures* si applicable, à vérifier), soit une structure individuelle française (entreprise individuelle / SASU) facturant ou recevant des subventions, selon la qualification juridique du bailleur (à vérifier).
* **Conditions (Docteur / Non-Docteur) :** Ouvert **avec ou sans doctorat**, sans employeur.
* **Délai avant premier euro :** 4 à 10 semaines (illustratif).
* **Montant plausible sur 12 mois :** $20\,000\text{ €}$ à $70\,000\text{ €}$ en numéraire + $5\,000\text{ \$}$ à $20\,000\text{ \$}$ en crédits de calcul (illustratif).
* **Ce qu'il impose au programme :** Ouverture totale du code et des billets techniques (parfaitement aligné avec le programme actuel) ; aucune cession de propriété intellectuelle à un établissement ; autonomie totale du calendrier.
* **Risque principal :** Rejet aux guichets philanthropiques très compétitifs ou friction bancaire/fiscale lors de la réception d'une bourse étrangère par une personne physique résidant en France.
* **Critère de départage :** C'est le seul montage qui préserve $100\%$ de l'indépendance et de la propriété du code tout en pouvant décaisser en moins de 3 mois.

#### Montage M2 : « Affiliation d'accueil (Mines ou ENS) + Portage d'une subvention internationale par l'établissement ou sa Fondation »
* **Architecture :** Signature d'une convention de chercheur invité/associé (ou collaborateur) avec Mines Paris – PSL (via ARMINES ou la Fondation Mines Paris, à vérifier) ou avec un laboratoire de l'ENS Paris-Saclay. Le directeur soumet un projet au *UK AISI Systemic Safety Grants* ou à *Open Philanthropy* (à vérifier) où l'établissement d'accueil (ou sa fondation) est l'entité légale réceptrice des fonds, qui utilise ensuite la subvention pour payer les frais de calcul et, si le montant le permet, recruter le directeur sur un CDD d'ingénieur/chercheur de 6 à 12 mois. Accès parallèle à Jean Zay via le tuteur.
* **Conditions (Docteur / Non-Docteur) :** Possible dans les deux cas (recrutement final comme Ingénieur de recherche si non-docteur, ou Postdoctorant si docteur).
* **Délai avant premier euro :** 4 à 8 mois (illustratif — cumul du délai d'attribution du fonds + délai de conventionnement et de recrutement RH en France).
* **Montant plausible sur 12 mois :** $45\,000\text{ €}$ à $100\,000\text{ €}$ coût complet chargé (illustratif).
* **Ce qu'il impose au programme :** Prélèvement de frais de gestion (*overheads* / préciput) par l'établissement (souvent $10\%$ à $25\%$, illustratif, à vérifier), propriété intellectuelle du code acquise à l'établissement d'accueil, achats de calcul/API soumis aux règles de la commande publique (très rigide pour payer des API mensuelles en dollars par carte bancaire, OBSERVÉ-NON-AUDITÉ dans les laboratoires publics français).
* **Risque principal :** Impossibilité pratique d'acheter des crédits API de modèles de frontière à la volée à cause des règles comptables publiques (bons de commande, fournisseurs référencés) et lourdeur administrative étouffant un programme d'une seule personne.
* **Critère de départage :** À choisir uniquement si un bailleur majeur (ex. UK AISI, à vérifier) refuse de financer une personne physique ou une jeune société et exige une institution académique établie.

#### Montage M3 : « Rattachement contractuel direct (Postdoc / Ingénieur / Doctorat) sur crédits locaux (DATAIA / PRAIRIE / Tuteur) »
* **Architecture :** Le tuteur des Mines ou un professeur du département de l'ENS Paris-Saclay dispose d'un reliquat sur une chaire (Fondation Mines, ANR, contrat ARMINES) ou dépose une demande au fil de l'eau auprès de l'institut 3IA local (DATAIA à Saclay ou PRAIRIE à PSL, à vérifier) pour embaucher le directeur en CDD (6 à 12 mois) ou en thèse financée (si sans doctorat et horizon étendu à 36 mois).
* **Conditions (Docteur / Non-Docteur) :**
  * *Avec doctorat :* CDD postdoctorant (délai de mise en place : 2 à 4 mois si les fonds sont déjà sur le compte du tuteur, illustratif).
  * *Sans doctorat :* CDD d'ingénieur d'études/de recherche sur ressources propres (même délai), ou contrat doctoral (calendrier contraint aux concours des écoles doctorales au printemps, début en octobre, à vérifier).
* **Délai avant premier euro :** 2 à 4 mois si fonds déjà disponibles chez le tuteur ; 6 à 10 mois si appel à projets interne (illustratif).
* **Montant plausible sur 12 mois :** Salaire net de $24\,000\text{ €}$ à $36\,000\text{ €}$/an (illustratif) + accès gratuit au cluster du laboratoire et à Jean Zay.
* **Ce qu'il impose au programme :** Lien de subordination salariale ; le programme n'est plus formellement « indépendant » mais devient un axe de recherche du laboratoire d'accueil ; obligation de publier sous l'affiliation principale de l'école.
* **Risque principal :** Détournement du temps du directeur vers des tâches annexes du laboratoire (encadrement, enseignement, livrables d'autres projets du tuteur).
* **Critère de départage :** Idéal si le tuteur dispose *déjà* d'une enveloppe dormante utilisable immédiatement et accepte contractuellement de laisser une liberté totale sur le sujet de sécurité de l'IA.

#### Montage M4 : « Structure juridique propre (SASU Deeptech) + Bpifrance + Crédits Cloud Startup + Convention de collaboration (ou Cifre) »
* **Architecture :** Création d'une SASU dédiée à l'outillage d'audit boîte blanche et de contrôle d'agents (préenregistrement, sondes d'activation comme service d'évaluation). Demande de la *Bourse French Tech* (Bpifrance, à vérifier) et des programmes de crédits cloud pour startups IA (*Google for Startups Cloud Program*, *Microsoft for Startups Founders Hub*, *AWS Activate*, qui offrent de $10\,000\text{ \$}$ à $100\,000\text{ \$}+$ de crédits GPU/API, illustratif, à vérifier). Signature optionnelle d'un partenariat avec le laboratoire des Mines ou de l'ENS. (Note : le Crédit d'Impôt Recherche [CIR] est écarté comme source de trésorerie à 3-6 mois car il n'est remboursé qu'après la clôture de l'exercice fiscal, soit à $M+12$ ou $M+18$, à vérifier).
* **Conditions (Docteur / Non-Docteur) :** Aucune condition de diplôme. Si docteur depuis moins de 2 ans, éligibilité possible au dispositif « Jeune Docteur » du CIR par la suite (à vérifier).
* **Délai avant premier euro / crédit :** 2 à 4 semaines pour les crédits cloud startups ; 3 à 5 mois pour la Bourse French Tech (illustratif).
* **Montant plausible sur 12 mois :** $10\,000\text{ \$}$ à $100\,000\text{ \$}$ en crédits calcul/API + jusqu'à $30\,000\text{ €}$ de subvention Bpifrance (exigeant un apport personnel équivalent à $30\%$ du budget total, illustratif, à vérifier).
* **Ce qu'il impose au programme :** Formuler une feuille de route de valorisation (même si le cœur scientifique reste ouvert), frais comptables et juridiques ($\approx 1\,500\text{ €}$ à $3\,000\text{ €}$/an, illustratif).
* **Risque principal :** Dérive commerciale forcée pour satisfaire les critères de Bpifrance et immobilisation de trésorerie personnelle en fonds propres.
* **Critère de départage :** Départagé positivement si les besoins en calcul/API explosent ($> 2\,000\text{ \$/mois}$, illustratif) et que les fonds philanthropiques ne répondent pas, car les programmes cloud startups sont les plus généreux en calcul immédiat.

---

### 3. Crédibilité : pièces attendues et séquence de production en 90 jours (Point 6)

Pour convaincre simultanément un fonds international (ex. LTFF/Manifund, à vérifier) et le laboratoire d'accueil (Mines / ENS Paris-Saclay), les pièces doivent être produites dans un ordre qui maximise l'information par unité de temps :

1. **Jours 1 à 15 — Le socle d'audit et le premier préenregistrement public :**
   * *Pièces :* Dépôt Git public (GitHub/GitLab) + archivage immuable sur Zenodo (avec DOI) contenant le protocole de l'expérience n° 1 (ex. sonde linéaire/MLP sur les activations d'un modèle 8B pour détecter la conscience d'évaluation, avec hypothèses $H_A/H_B$, seuils et contrôles négatifs figés par empreinte cryptographique SHA-256).
   * *Pourquoi en premier :* Coût GPU nul ; prouve immédiatement la discipline méthodologique et empêche toute suspicion de *p-hacking* ultérieur.
2. **Jours 16 à 45 — Exécution sur processeur graphique et code ouvert reproductible :**
   * *Pièces :* Exécution de l'expérience préenregistrée sur GPU à la carte (coût : quelques dizaines à centaines de dollars, illustratif), publication des journaux d'exécution des agents de code, des poids des sondes et du script de reproduction en une commande.
   * *Pourquoi en deuxième :* Transforme une promesse théorique en un actif empirique vérifiable (cf. Expérience E4).
3. **Jours 46 à 65 — Le billet technique public (et prépublication arXiv/HAL) :**
   * *Pièces :* Rédaction d'un billet technique dense (format *LessWrong* / *Alignment Forum* + PDF formaté type atelier NeurIPS/ICLR déposé sur arXiv ou HAL) rapportant fidèlement le résultat par rapport au préenregistrement (qu'il soit positif ou négatif).
   * *Pourquoi en troisième :* C'est l'unité de base évaluée par les *regranters* internationaux et la pièce que le tuteur des Mines peut faire circuler à sa direction pour justifier un accueil.
4. **Jours 66 à 75 — La lettre d'appui du tuteur des Mines et l'accord de principe ENS :**
   * *Pièces :* Lettre courte du tuteur attestant : (i) la qualité d'alumnus et la rigueur technique du directeur au vu du premier billet technique, (ii) la pertinence des travaux pour l'équipe d'accueil, et (iii) l'accord de principe pour l'accueillir ou parrainer un accès calcul (GENCI).
   * *Pourquoi en quatrième :* Le tuteur signe beaucoup plus facilement une lettre forte lorsqu'il a sous les yeux un billet technique déjà accompli et un dépôt propre.
5. **Jours 76 à 90 — Soumission groupée des dossiers de financement :**
   * *Pièces :* Dossier de candidature (2 à 5 pages) assemblant les liens vers le préenregistrement, le billet technique, le dépôt de code, le budget de calcul chiffré pour les 3 prochains préenregistrements (modèles 8B à 70B, illustratif) et la lettre du tuteur.

---

### 4. Questions à poser au tuteur et au département (10 au plus) et ce qu'il ne faut pas faire (Point 7)

#### Les 10 questions exactes à poser

**Au tuteur de Mines Paris – PSL (et son centre de recherche) :**
1. *Statut d'accueil :* « Quel est l'intitulé exact de la convention d'accueil sans rémunération (chercheur visiteur, collaborateur bénévole, associé) que les RH de Mines Paris ou d'ARMINES acceptent aujourd'hui pour un alumnus qui n'a pas d'autre employeur académique, et quelles pièces justificatives (assurance, statut) exigent-elles ? »
2. *Propriété intellectuelle :* « Le modèle de convention d'accueil comporte-t-il une clause de cession automatique des droits sur le code et les résultats à l'École ou à ARMINES, et peut-on y inscrire par avenant que l'ensemble du code produit restera publié sous licence open-source (ex. MIT / Apache 2.0) ? »
3. *Parrainage calcul (GENCI) :* « Accepterais-tu d'être le porteur administratif formel d'une demande d'"Accès Dynamique" sur le supercalculateur Jean Zay (IDRIS) en me déclarant comme utilisateur principal pour mes expériences sur modèles 8B ? »
4. *Crédits internes rapides :* « Ton centre ou l'institut PRAIRIE-PSAI dispose-t-il d'un guichet au fil de l'eau (ou d'un reliquat sur contrat) permettant de financer soit des factures de calcul/API infonuagiques, soit un contrat court de 3 à 6 mois sans attendre un appel annuel ? »
5. *Portage de bourses externes :* « Si j'obtiens une bourse d'un fonds international de sécurité de l'IA qui exige de verser les fonds à une institution (via la Fondation Mines Paris ou ARMINES), quel est le taux de frais de gestion prélevé et le délai de mise à disposition des crédits ? »

**Au département de l'ENS Paris-Saclay :**
6. *Distinction Département vs Laboratoire :* « L'accueil en tant qu'alumnus doit-il être formalisé au niveau du département d'enseignement ou directement auprès d'un laboratoire de recherche (ex. Centre Borelli ou LMF, à vérifier), et qui a la signature finale ? »
7. *Conditions de diplôme (Docteur vs Non-Docteur) :* « L'absence (ou la présence) du grade de docteur change-t-elle le statut d'hébergement accessible au sein du laboratoire et l'éligibilité aux soutiens de l'institut DATAIA ou de la Fondation ENS Paris-Saclay ? »
8. *Droits ouverts par l'affiliation :* « Cette convention d'accueil ouvre-t-elle immédiatement une adresse `@ens-paris-saclay.fr`, le droit de déposer sur HAL avec validation du laboratoire, et l'autorisation de signer mes prépublications sous cette affiliation ? »
9. *Obligations de validation :* « La signature d'une prépublication sous l'affiliation du laboratoire impose-t-elle un circuit de relecture interne préalable (notamment sur des sujets de sécurité de l'IA) qui retarderait la publication de mes billets techniques au-delà de quelques jours ? »
10. *Guichets Alumni / Fondation :* « Existe-t-il au sein de la Fondation ENS Paris-Saclay un dispositif de bourse d'amorçage ou de soutien aux projets scientifiques indépendants portés par d'anciens élèves ? »

#### Ce qu'il ne faut pas faire (Portes fermées, engagements irréversibles, délais perdus)

1. **Ne jamais signer une convention d'accueil ou de stage/visiteur sans avoir lu la clause de Propriété Intellectuelle :** Signer une convention standard qui cède à l'établissement ou à sa filiale de valorisation l'exclusivité du code et des poids de sondes entraînés est un engagement irréversible qui bloque la publication ouverte immédiate et peut empêcher un financement philanthropique ultérieur exigeant du bien public ouvert.
2. **Ne pas faire verser une bourse personnelle internationale sur le compte comptable d'un établissement public français si le bailleur autorise le versement direct à l'individu :** Une fois l'argent entré dans le budget d'un EPSCP, il devient de l'argent public soumis au code de la commande publique (impossibilité de payer rapidement des API en dollars à la carte, délais de paiement de 30 à 90 jours, illustratif) et il est impossible de se le verser en salaire sans créer un poste formel chargé à $\approx 45\text{–}60\%$ (illustratif) avec publication de poste obligatoire d'un mois.
3. **Ne pas attendre l'obtention de l'affiliation administrative ou des heures Jean Zay pour produire le premier résultat GPU et le premier billet technique :** Avec un budget actuel de quelques centaines de dollars par mois, un modèle de 8 milliards de paramètres s'étudie pour moins de $150\text{ \$}$ (illustratif) de location GPU. Attendre 3 mois une ouverture de compte HPC national avant de générer la preuve de concept fait perdre la fenêtre de tir du trimestre.
4. **Ne pas présenter le projet aux RH d'une école comme un « travail à temps plein sans rémunération » pour le compte du laboratoire :** Cela déclenche un refus juridique immédiat des RH par crainte de requalification en contrat de travail dissimulé ou de contournement de la législation sur les stages (référence à vérifier). La demande doit toujours être formulée comme un accueil ponctuel de recherche collaborative autour d'un projet scientifique autonome.
5. **Ne pas déposer de dossier ANR en espérant un financement à 3-12 mois :** Le temps de rédaction d'une proposition ANR complète ($\approx 20\text{ à }30$ pages, illustratif) représente un coût d'opportunité majeur pour une personne seule, pour un décaissement qui n'interviendrait qu'à $M+12$ au plus tôt et uniquement sous le portage d'un permanent.

---

### 5. Récapitulatif de ce qui est connu et répertoire des dispositifs cités (Point 8)

Conformément à la règle 3 et au point 8 de la question, tous les dispositifs, organismes et évolutions récentes cités ci-dessous portent la mention « à vérifier » quant à leurs modalités exactes d'ouverture en octobre 2026 :

* **Établissements et structures locales :**
  * *École normale supérieure Paris-Saclay* (EPSCP) et *Fondation ENS Paris-Saclay* — à vérifier.
  * *Mines Paris – PSL* (Grand établissement), *Fondation Mines Paris* et *ARMINES* (association de recherche contractuelle partagée avec les Écoles des Mines) — à vérifier.
  * *Université Paris-Saclay* et *Université PSL (Paris Sciences et Lettres)* — à vérifier.
* **Agences et programmes publics français :**
  * *Agence nationale de la recherche (ANR)* — Appel à projets générique (AAPG) et Jeunes Chercheuses et Jeunes Chercheurs (JCJC) — à vérifier.
  * *Institut national d'évaluation et de sécurité de l'intelligence artificielle (INESIA)* — structure nationale française annoncée en 2024-2025 autour du Laboratoire national de métrologie et d'essais (LNE) et du gouvernement français (statut des appels externes en 2026 à vérifier).
  * *DATAIA* — Institut d'intelligence artificielle de l'Université Paris-Saclay (labellisé IA-Cluster dans le cadre de France 2030, changement de périmètre et d'intitulé de « 3IA » vers « IA-Cluster » en 2024 à vérifier).
  * *PR[AI]RIE-PSAI* — *Paris School of AI*, IA-Cluster porté par l'Université PSL (successeur/extension du 3IA PRAIRIE dans France 2030, changement de nom récent à vérifier).
  * *Région Île-de-France* — Domaine d'intérêt majeur *DIM AI4IDF* (successeur du DIM RFSI, changement de nom à vérifier).
  * *Bpifrance* — *Bourse French Tech* et *Bourse French Tech Emergence* — à vérifier.
* **Fondations mathématiques et Instituts :**
  * *Fondation Mathématique Jacques Hadamard (FMJH)* (Paris-Saclay) et *Fondation Sciences Mathématiques de Paris (FSMP)* — à vérifier.
  * *Institut Pascal* (Université Paris-Saclay) et *Institut d'études avancées (IEA) de Paris* — à vérifier.
* **Financeurs internationaux en sécurité de l'IA et programmes européens :**
  * *Long-Term Future Fund (LTFF)* — géré sous l'égide d'*Effective Ventures* (restructuration récente des entités d'*Effective Ventures* UK/US en 2024-2025 à vérifier).
  * *Survival and Flourishing Fund (SFF)* — à vérifier.
  * *Manifund* — plateforme de micro-subventions et *regranting* en sécurité de l'IA (notamment *AI Safety Regranting*, statut des rondes 2026 à vérifier).
  * *Open Philanthropy* — bailleur philanthropique (évolution de certaines branches opérationnelles sous de nouvelles dénominations telles que *Coefficient Giving* ou structures associées à vérifier).
  * *UK AI Safety Institute (AISI)* — *Systemic Safety Grants* (opéré au Royaume-Uni via le DSIT et en lien avec l'agence *ARIA* [*Advanced Research and Invention Agency*], programme *Safeguarded AI*, à vérifier).
  * *Foresight Institute* — *AI Safety Grants & Fellowships* — à vérifier.
  * *Actions Marie Skłodowska-Curie (MSCA)* — *Postdoctoral Fellowships (PF)*, programme *Horizon Europe* de la Commission européenne — à vérifier.
  * *FTX Future Fund* — dispositif **fermé** fin 2022 (signalé pour mémoire afin d'éviter toute recherche sur d'anciennes listes de bourses, VÉRIFIÉ).
* **Infrastructures et programmes de calcul :**
  * *GENCI* (Grand équipement national de calcul intensif) et *IDRIS* (CNRS) — supercalculateur *Jean Zay*, dispositif « Accès Dynamique » pour l'IA — à vérifier.
  * *EuroHPC Joint Undertaking (JU)* — appels *Benchmark Access* et *Development Access* — à vérifier.
  * *Google Cloud* — *TPU Research Cloud (TRC)* et *Google for Startups Cloud Program* — à vérifier.
  * *Anthropic* — *External Researcher Access Program* (crédits API pour la recherche en alignement et sécurité) — à vérifier.
  * *OpenAI* — *Researcher Access Program* (crédits API) — à vérifier.

FIN-DE-CELLULE