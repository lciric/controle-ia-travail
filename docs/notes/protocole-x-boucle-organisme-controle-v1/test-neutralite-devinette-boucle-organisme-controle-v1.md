# Test de neutralité et test de devinette (étape 1, aveugle à la réponse du concepteur)

Portée : examen aveugle des quatre pièces neutres du dossier de la boucle « Organisme d'idéation ⇄ Contrôle de l'intelligence artificielle » avant toute lecture du devis ou des autres pièces du dépôt, accompagné du rejeu de la garde de motifs définie dans [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L552-L578).

---

## 1. Rejeu de la garde de motifs

Exécution directe de [`motifs_trouves`](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L571-L578) après lecture par [`lire_entree`](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L632-L641) sur chacun des quatre fichiers seuls, puis sur des invites assemblées au format de l'étage trois, tour un (`E3-T1`) avec le gabarit de préambule et la consigne correspondants :

| Fichier | Longueur (caractères) | Mots | Motifs détectés seul | Motifs sur invite assemblée |
|---|---:|---:|---|---|
| [faits-neutres-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/faits-neutres-boucle-organisme-controle-v1.md) | 4 979 | 749 | Aucun (`[]`) | — |
| [question-neutre-collisionneur-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/question-neutre-collisionneur-boucle-organisme-controle-v1.md) | 2 887 | 440 | Aucun (`[]`) | Aucun (`[]`, 10 587 caractères) |
| [question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md) | 2 598 | 394 | Aucun (`[]`) | Aucun (`[]`, 10 298 caractères) |
| [sous-question-organisme-boucle-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/sous-question-organisme-boucle-controle-v1.md) | 1 289 | 191 | Aucun (`[]`) | Aucun (`[]`, 8 989 caractères) |

Remarque factuelle : l'absence de déclenchement de la garde de motifs garantit l'absence de fuite technique de noms, de chemins, d'identifiants de session ou d'accords, mais ne mesure pas l'orientation épistémique du texte.

---

## 2. Test de devinette (ce qu'un lecteur extérieur devine de la thèse préférée du concepteur)

À la lecture exclusive des quatre fichiers, un candidat ou un évaluateur peut reconstruire avec une précision importante ce que le concepteur tient pour le cœur de la solution, l'architecture cible et l'ordre probable des priorités :

### 2.1 Thèse et architecture que l'on devine

1. **Architecture en triple séparation stricte et sas à sens unique à court terme** : on devine que le concepteur attend un découplage étanche entre trois sphères : (a) l'entraînement et la sélection interne de l'organisme sur des mondes à lois plantées et des bancs sur processeur, (b) les familles d'épreuve inédites à lecture unique pour les détecteurs du contrôle, et (c) la banque de validation finale lue une seule fois. Aucun score de moniteur ou de juge ne doit remonter comme signal d'optimisation vers l'agent ni vers l'organisme (sauf dans un bras d'attaque explicite et cloisonné).
2. **Entonnoir économique « filtre processeur amont avant épreuve sur cartes graphiques »** : on devine une thèse quantitative centrale : le budget sur cartes graphiques est le goulot d'étranglement et risque d'être gaspillé si l'organisme envoie trop de faux positifs. L'architecture attendue passe donc par un filtre amont bon marché sur processeur (mondes synthétiques datés, signatures de rôle, transport optimal, compression) et par un bilan reliant taux de faux candidats, coût du filtre et capacité matérielle.
3. **Mécanismes d'idéation privilégiés** : les faits et la question principale convergent pour désigner une préférence vers des **opérateurs structurels et hors alphabet** plutôt que de la simple proximité lexicale :
   - séparation entre distance de surface et alignement structurel (graphes typés, signatures de rôle, transport optimal de graphes) ;
   - détection d'obstructions et scission de concepts confondus (faux amalgames) ;
   - progrès de compression entre bassins éloignés et synthèse formelle ;
   - garde-fous de contamination temporelle lorsqu'un modèle pré-entraîné est utilisé.
4. **Limitation des mondes synthétiques et danger de sur-ajustement adaptatif** : on devine que le concepteur considère deux pièges comme décisifs : (a) la dégradation de la généralisation quand les mondes à lois plantées omettent une classe d'invariants du sabotage réel, et (b) l'épuisement de la validité statistique (sur-ajustement adaptatif et comparaisons multiples) quand on itère sur un banc fini partagé.
5. **Contrôles négatifs « doit mourir »** : on devine une exigence récurrente de falsification sur cas nuls (archives connues, absence d'effet réel, générateur synthétique à raccourci).

### 2.2 Rang de priorité que l'on devine

En observant l'application explicite de la formule `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` (où `1` correspond à un coût minimal sur processeur seul), la structure des textes oriente le classement des chantiers :
- **En tête (rangs 1 à 2)** : les chantiers exécutables sur **processeur seul** (coût `1` ou `2` au dénominateur, ce qui multiplie mécaniquement le score par `2,5` à `5` par rapport à un chantier sur cartes graphiques), en particulier :
  1. la formalisation des **invariants d'étanchéité de la boucle et du filtre de sélection** (cloisonnement des mondes et banque unique, contrôle du budget de calcul et des faux candidats, protocole « doit mourir » sur cas nul) ;
  2. les **opérateurs structurels sans fuite lexicale sur graphes et bancs publics datés sur processeur** (alignement par transport optimal ou signatures de rôle, scission de concepts confondus, compression inter-bassins), plus le protocole d'étanchéité temporelle.
- **Ensuite (rangs 3 à 5)** : l'ancrage concret vers le contrôle boîte blanche (transformation d'anomalies ou de faux amalgames en primitives testables, détection séquentielle avec nul par acte plutôt qu'une référence finie fixe, mesure de perte de transfert quand une classe de sabotage manque dans les mondes plantés) avant toute montée en charge lourde sur cartes graphiques.

### 2.3 Distinction importante : d'où vient l'orientation observée ?

- Une **grande partie** de cette lisibilité provient de `faits-neutres-boucle-organisme-controle-v1.md` (notamment la ligne 23 sur les pistes déjà inscrites pour le dégel de l'organisme, les lignes 13 à 16 sur les règles de séparation et de ressources, et les lignes 29 à 33 sur les risques identifiés). Or, dans un protocole à bras multiples (bras principal contre bras témoin), les faits sont communs aux deux bras, tandis que la question varie.
- Cependant, `question-neutre-collisionneur-boucle-organisme-controle-v1.md` va nettement plus loin que `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` : ses points 3 et 4 **pré-dessinent l'architecture attendue et nomment déjà les opérateurs et équations précis** (trois sens de couplage, équation de bilan filtre amont contre budget de cartes graphiques, borne de contamination sur banc partagé, dégradation sur mondes incomplets, « doit mourir », opposition intra-alphabet par réduction et séparation de concepts contre hors alphabet par compression inter-bassins ou synthèse formelle).
- Quant à `sous-question-organisme-boucle-controle-v1.md`, sa formulation en trois options fermées (« (1) ... ou (2) ... ou (3) ... ») décrit déjà explicitement le mécanisme attendu dans chacune des trois branches.

---

## 3. Scores d'orientation et verdict d'admission (seuil `< 0,50`)

Rappel de l'échelle : `0,00` = parfaitement neutre (pose le problème sans souffler l'architecture ni les termes de la réponse), `1,00` = souffle directement la réponse ou la thèse attendue. Seuil d'admission : `< 0,50`.

| Fichier | Score d'orientation | Admission (`< 0,50`) | Justification concise |
|---|---:|---|---|
| [question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md) | **0,18** | **Admis** | Pose le cadre (deux systèmes, boucle, rigueur, vérification, priorités selon la formule) sans prescrire les trois sens de couplage, ni les équations spécifiques, ni le contraste intra-alphabet contre hors alphabet. |
| [faits-neutres-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/faits-neutres-boucle-organisme-controle-v1.md) | **0,46** | **Admis (limite haute)** | Reste factuel et sans jargon interne ni verdicts chiffrés, mais les sections « Règles et contraintes », « Pistes déjà inscrites pour le dégel de l'organisme » (ligne 23) et « risques identifiés » (lignes 29 à 33) énumèrent déjà l'essentiel du vocabulaire d'architecture et des pistes méthodologiques que l'on retrouve dans la réponse attendue. |
| [question-neutre-collisionneur-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/question-neutre-collisionneur-boucle-organisme-controle-v1.md) | **0,68** | **Refusé (`≥ 0,50`, à retoucher)** | Les points 3 et 4 orientent fortement la réponse : ils imposent la décomposition exacte en trois flèches de couplage, soufflent les trois mécanismes théoriques précis (bilan filtre contre budget matériel, borne de contamination sur banc partagé, dégradation sur mondes incomplets), dictent la taxonomie « intra-alphabet contre hors alphabet » avec les noms mêmes des opérateurs (séparation de concepts, compression inter-bassins, synthèse formelle) et réintroduisent « doit mourir ». L'écart d'orientation avec la question témoin (`0,68` contre `0,18`) crée un biais de cadrage important entre les deux bras. |
| [sous-question-organisme-boucle-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/sous-question-organisme-boucle-controle-v1.md) | **0,64** | **Refusé (`≥ 0,50`, à retoucher)** | En guise de question ouverte, la seconde phrase énumère sous forme de choix « (1) ... ou (2) ... ou (3) ... » trois architectures déjà précises (séparation stricte des trois ensembles, transformation d'anomalies et faux amalgames en primitive sur processeur avant cartes graphiques, borne de perte de transfert par omission de classe), soufflant directement la structure et la conclusion souhaitée. |

---

## 4. Retouches exactes recommandées (pour descendre sous `0,50`)

### 4.1 Sur `question-neutre-collisionneur-boucle-organisme-controle-v1.md` (prioritaire)

Les points 1, 2, 5, 6 et 7 sont propres (le point 7 reflète le barème standard déjà aligné sur le témoin). L'excès d'orientation se concentre aux lignes 9 et 10 :

1. **Ligne 9 (point 3)** — texte actuel :
   > `3. **Architecture et invariants d'étanchéité de la boucle fermée.** Modélise distinctement les trois sens de couplage (de l'organisme vers les instruments du contrôle ; des échecs et corpus du contrôle vers l'orientation de l'organisme ; de l'organisme vers la génération de menaces adverses). Établis l'équation de bilan reliant le filtre amont sur mondes à lois plantées au budget d'épreuves sur cartes graphiques, la borne de contamination par sélection répétée sur banc partagé, et les conditions sous lesquelles optimiser sur des mondes incomplets dégrade la généralisation réelle. Donne les objets de contrôle négatifs (« doit mourir ») qui disqualifieraient une mauvaise boucle.`

   **Retouche exacte proposée** (ramène le point 3 à une exigence de méthode sans souffler les équations ni le découpage en trois flèches) :
   > `3. **Architecture et invariants de la boucle fermée.** Décris comment coupler l'organisme d'idéation et le programme de contrôle dans chaque sens utile, en précisant les conditions de validité statistique, d'allocation du budget de calcul et de transfert hors des mondes synthétiques. Précise les contrôles négatifs qui permettraient de disqualifier une boucle défaillante ou illusoire.`

2. **Ligne 10 (point 4)** — texte actuel :
   > `4. **Les méthodes, opérateurs et outils précis** pour augmenter le taux de découvertes véritablement exploitables en contrôle boîte blanche (en comparant les approches intra-alphabet par réduction et séparation de concepts aux approches hors alphabet par compression inter-bassins ou synthèse formelle), ainsi que le protocole d'étanchéité temporelle lorsque des modèles pré-entraînés interviennent.`

   **Retouche exacte proposée** (supprime l'opposition pré-mâchée « intra-alphabet contre hors alphabet » et la liste de méthodes soufflée) :
   > `4. **Les méthodes, opérateurs et outils précis** à privilégier pour augmenter le taux de découvertes véritablement exploitables en contrôle boîte blanche (en comparant plusieurs familles d'approches distinctes, leurs hypothèses et leurs modes d'échec), ainsi que la manière de garantir l'étanchéité temporelle lorsque des modèles pré-entraînés interviennent.`

3. **Effet attendu des deux retouches** : le bras principal garde son niveau d'exigence mathématique et technique (invariants, modèle quantitatif de bilan et de transfert, comparaison d'opérateurs, protocole temporel, contrôles négatifs) tout en cessant de dicter la réponse attendue ; son score d'orientation redescend vers environ `0,30` (admissible `< 0,50`) et redevient comparable à la question témoin tout en conservant le test de granularité du bras principal.

### 4.2 Sur `faits-neutres-boucle-organisme-controle-v1.md` (retouche recommandée pour abaisser sous `0,35`)

Bien que le score (`0,46`) soit juste sous le seuil `0,50`, deux passages concentrent l'orientation :

1. **Ligne 23** — texte actuel :
   > `- **Pistes déjà inscrites pour le dégel de l'organisme** : séparation entre distance de surface et alignement structurel sans fuite lexicale (graphes typés, signatures de rôle, transport optimal de graphes) ; détection d'obstructions et scission de concepts confondus ; mesure de progrès de compression entre bassins éloignés ; bancs publics datés sur processeur pour étalonner les heuristiques sans coût matériel lourd ; surveillance de la contamination temporelle lorsqu'un modèle pré-entraîné intervient.`

   **Retouche exacte proposée** (remplace le catalogue des pistes méthodologiques à défendre par un état neutre de l'état de l'organisme, sans suggérer les opérateurs précis) :
   > `- **Capacités et limites connues de l'organisme** : il compare des représentations par graphes et des archives textuelles datées, dispose de bancs publics exécutables sur processeur, et soulève des questions ouvertes sur l'alignement structurel sans proximité lexicale, la gestion des concepts confondus, la généralisation entre domaines éloignés et la contamination temporelle si un modèle pré-entraîné intervient.`

2. **Lignes 29 à 33** — texte actuel :
   > `Les risques identifiés dans la littérature sur les boucles adaptatives et l'évaluation de modèles sont :`
   > `- le sur-ajustement adaptatif lorsqu'un système itère sur un banc ou un évaluateur de taille finie ;`
   > `- la confusion entre raccourcis propres à un générateur synthétique et invariants réels transférables ;`
   > `- la perte d'utilité lorsque l'optimisation porte sur des mondes simplifiés qui manquent des classes d'invariants du domaine cible ;`
   > `- le gaspillage du budget de calcul sur cartes graphiques si le filtrage amont laisse passer trop de faux candidats.`

   **Retouche exacte proposée** (transforme ces quatre risques en questions ouvertes plutôt qu'en liste de réponses déjà prêtes pour le point 3) :
   > `Les questions ouvertes identifiées lors de la mise en boucle portent sur la validité statistique d'une itération répétée sur des bancs finis, sur la transférabilité des mécanismes découverts en environnement synthétique vers les modèles ouverts cibles, et sur l'arbitrage entre filtrage amont sur processeur et coût d'évaluation sur cartes graphiques.`

### 4.3 Sur `sous-question-organisme-boucle-controle-v1.md` (si destinée à un usage indépendant)

Texte actuel (ligne 1) : liste trois solutions candidates déjà rédigées en « (1) ... ou (2) ... ou (3) ... ».

**Retouche exacte proposée** :
> `Sous-question « boucle entre découverte automatisée et contrôle des menaces diffuses ». Lorsqu'un organisme d'idéation scientifique est chargé d'inventer des concepts mathématiques, des signatures ou des protocoles destinés à renforcer un programme de contrôle boîte blanche des menaces diffuses (détection séquentielle, résistance à la corruption du moniteur, coordination entre copies), comment coupler les deux systèmes sans que l'organisme ne sur-apprenne les biais des bancs d'essai ni ne contourne l'évaluation ? Propose un opérateur ou une architecture de couplage qui assure l'étanchéité entre sélection et validation, filtre efficacement les faux candidats à coût modeste sur processeur avant toute exécution sur cartes graphiques, et permette de mesurer ou de borner l'écart de transfert hors des mondes synthétiques. Pour chaque proposition : précise l'invariant qu'elle protège, le coût minimal d'un contrôle négatif sur un cas nul sans progrès réel, et le protocole d'étanchéité temporelle si un modèle pré-entraîné intervient.`

---

## 5. Synthèse finale de l'étape 1

- **Garde de motifs** : conforme sur les quatre fichiers (`0` motif détecté, seul et assemblé).
- **Décision sur la neutralité (seuil `< 0,50`)** :
  - `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` : **0,18 (admis)**
  - `faits-neutres-boucle-organisme-controle-v1.md` : **0,46 (admis à la limite, retouche conseillée)**
  - `question-neutre-collisionneur-boucle-organisme-controle-v1.md` : **0,68 (refusé en l'état, retouche nécessaire avant envoi)**
  - `sous-question-organisme-boucle-controle-v1.md` : **0,64 (refusé en l'état, retouche nécessaire avant envoi)**
