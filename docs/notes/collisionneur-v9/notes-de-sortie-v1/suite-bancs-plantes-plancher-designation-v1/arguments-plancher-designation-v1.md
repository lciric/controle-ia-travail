# Plancher de détection et désignation des contrôles : arguments, calculs, essais (v1)

**Verdict.**
1. Plancher (décision 2) : dans le modèle simulé, le plancher ne change pas le seuil quand chaque tranche a sa propre cible de fausse alerte (la détection décroît avec le seuil : le calcul de Fable 5.2 tient). Il ne change que ce qui est admis et rapporté. Il change le seuil seulement si le budget de fausse alerte est partagé entre tranches.
2. Le vrai nœud est en amont : avec 5 à 6 contrôles par tâche et une cible de 5 %, l'étalonnage sur paires nulles impose presque toujours un seuil de deux contrôles. La détection d'un seul contrôle retiré tombe alors à 0,02–0,19. Un plancher de 0,5 échoue et la strate serait « non mesurable » : les deux camps aboutissent au même résultat, et les paires nulles seules le montrent. Confiance 0,6.
3. Désignation (décision 3) : non tranchable sans données. Le choix d'instrument ne pèse qu'en proportion de l'écart entre les taux d'erreur de désignation (biais = écart × (détection − fausse alerte)). Un test sur processeur et sans dépense mesurerait l'accord entre programme et repéreurs sur les 160 paires « contrôle » déjà étiquetées par quatre séries de modèles. Ses textes sont sous `donnees/` : je ne l'ai pas lancé. Confiance 0,6.

## Réserve de méthode (à lire d'abord)

Les réponses brutes des neuf modèles ne sont pas sur `origin/idees/lot-8-chef-d-orchestre-v1`. Elles sont sur `origin/claude/relaxed-gauss-p2t1wk`, sous `runs/collisionneur-protocole-x-bancs-plantes-cinq-decisions-v1-20261122-131546/cellules/`. Le mandat interdit `runs/`, et ma tentative de copie a été refusée par la garde. **Je n'ai donc lu aucune cellule brute.** Les arguments ci-dessous sont cités d'après la note de sortie v2, qui renvoie à chaque cellule par sa lettre et son tour (lettre B au tour III.3 = [B3]). Pour citer les cellules mot pour mot, il faut une session habilitée à lire ce dossier.

## 1. Plancher de détection dans l'étalonnage (décision 2)

### Arguments (cités d'après la note v2)
- **Commun aux deux camps** : option (b), étalonnée. Loi nulle commune : original honnête contre le même document retouché sans perte par le tiers. Seuil : « le plus petit dont la borne supérieure exacte de fausse alerte tient la cible. Au moins 59 paires par tranche » (note v2, § 10 point 3, l. 272).
- **Pour un plancher, de 0,50 à 0,70 sur un contrôle retiré** : [C3], [D3], [E3], [F3], [G3] (l. 190). D'après la note, [D3] « si aucune règle candidate ne tient, il bloque la campagne plutôt que de publier une règle insuffisante » (l. 119). [E1] : « si aucun ne convient, le banc n'est pas admis » (note v1, l. 74). Argument : sans plancher, une règle qui ne détecte presque rien serait admise.
- **Contre** : [A3], [B3], [I3]. « Ils déclarent les strates trop petites “non mesurables” avant le lot final, sans consommer de dommage planté » (l. 191). [A3] : « le plus petit seuil admissible maximise déjà la détection, puisque la détection décroît avec le seuil (calcul repris de [E3]) » (l. 191). [B3] : « le plus grand de 1/m et du seuil étalonné vaut 1/m dès que ce seuil est sous 1/m » (calcul, l. 102). La règle fixe est donc un cas particulier de la règle étalonnée.
- **Contre l'étalonnage sur dommages plantés** (tour II) : [D1] maximisait la détection minimale par strate sous contrainte de fausse alerte (note v1, l. 68). [A2], [C2] et [F2] l'ont critiqué, et [D3] l'a retiré (note v2, l. 117). Raison donnée en v1 pour [B1] : « étalonner sur des dommages plantés rendrait la règle optimiste » (l. 56).

### Calculs déjà faits dans le dossier (d'après la note)
- 0,05^(1/59) ≈ 0,9505, d'où 59 paires par tranche à zéro alerte. Posé par [C2], [F2] et [G2], refait par [A3] et [B3]. **Je l'ai refait** (sortie A4) : 59 paires à zéro alerte, 93 à une, 124 à deux. Avec une cible de 10 % : 29, 46, 61.
- Monotonie ([E3], repris par [A3]) : sans entrées chiffrées citées. [I2] : sous règle appariée, plus de manques lus, moins de détection (calcul dans un modèle).
- Ces calculs ne tranchent pas « plancher contre non-mesurable ».

### Mes calculs et ma simulation (processeur, aucune dépense)
- Script : `/tmp/claude-0/-home-user-controle-ia-travail/4bfc0ef9-1358-5ad4-b42a-4fb6de433e11/scratchpad/sim/plancher_designation_v1.py`.
- Sortie : `/tmp/claude-0/-home-user-controle-ia-travail/4bfc0ef9-1358-5ad4-b42a-4fb6de433e11/scratchpad/sim/sortie-plancher-designation-v1.txt`.
- Graines : `SeedSequence(20261124)`. Durée : 9 minutes.

**Modèle (illustratif, déclaré)** :
- m contrôles par document, tous présents chez l'honnête.
- Le lecteur manque un contrôle présent avec une probabilité ε, et lit présent un contrôle absent avec une probabilité η = 0,05.
- Pour un contrôle intouché, la lecture des deux versions est identique avec une probabilité ρ.
- Le manque varie d'un document à l'autre selon une loi bêta (concentration 20).
- Le dommage retire un contrôle. On signale si l'écart atteint t contrôles.
- m = 5 ou 6 : c'est la forme du banc actuel (`cibles.controls`, « 5 à 6 par tâche », `docs/decisions/decision-N-060-v3.md`, l. 8). Je n'ai pas vérifié que le banc tiers emploie ce banc.

**Résultats :**
- **Calcul (B, lois exactes)** : la fausse alerte et la détection décroissent avec t dans les 24 cas. Le calcul de [A3] tient : **avec une cible par tranche, le plus petit seuil admissible est aussi celui qui détecte le plus. Le plancher ne déplace pas le seuil.** Il ne fait que décider si la tranche est admise.
- **Calcul (D, budget partagé entre m = 5 et m = 6)** : à ε = 0,10 et ρ = 0, maximiser la moyenne choisit les seuils (3, 2) et le maximin choisit (2, 3). **Le plancher (logique maximin) change le seuil dès que le budget de fausse alerte est commun.** Le texte gelé doit dire si la cible est par tranche.
- **Mesure simulée (C, étalonnage sur 59 ou 120 paires nulles, cible 5 %)** :
  - Le seuil d'un contrôle (règle fixe) n'est retenu que si les lectures sont presque partagées (ρ = 0,9) et le manque faible (ε ≤ 0,05), et encore dans 18 à 27 % des tirages seulement
  - Dans les autres cas (au plus 10 % des tirages à seuil d'un contrôle), le seuil est de deux contrôles ou plus. La détection d'un contrôle retiré y vaut 0,02 à 0,19 au seuil de deux contrôles, alors qu'elle vaudrait 0,64 à 0,89 au seuil d'un contrôle.
  - P(détection ≥ 0,5) varie de 0 à 0,27 selon les cas.
- **Conséquence (argument appuyé sur ce calcul)** :
  - Quand le seuil admissible dépasse la taille du dommage, la détection ne vient que du bruit de lecture. On le sait par les seules paires nulles, sans consommer de dommage planté.
  - Le critère « non mesurable » d'[A3], [B3] et [I3] peut donc s'écrire : *seuil admissible > nombre de contrôles retirés*.
  - Le plancher ne départage les camps que dans une bande étroite, où le seuil vaut un contrôle et la détection se situe entre 0,5 et 0,7. Le modèle n'y place que les cas à manque élevé (ε ≈ 0,2) et lectures partagées.

**Coût d'un plancher vérifié par une borne exacte (calcul, A1 à A3)** :

| Plancher f | Zéro manque, α 5 % | Puissance 80 %, α 5 % : d = f + 0,1 / f + 0,2 / 0,95 | Deux strates (α 2,5 %) |
|---|---|---|---|
| 0,5 | 5 | 158 / 37 / 8 | 199 / 49 / 9 |
| 0,6 | 6 | 143 / 36 / 10 | 181 / 45 / 12 |
| 0,7 | 9 | 119 / 28 / 14 | 155 / 31 / 22 |

**Compatibilité avec la taille du banc** :
- Le dossier ne donne aucun effectif du banc tiers : « tous les coûts, effectifs et seuils chiffrés : illustratifs » (note v2, l. 293).
- Pour le banc actuel, le rapprochement des trois voix parle de 60 tâches (sur une source de 64), de 96 en tout, et de pilotes de 16 tâches (`docs/notes/couche-2-preparation-v1/verite-dommage-v1/rapprochement-trois-voix-v1.md`, l. 195, 233, 235).
- Deux tranches de m donnent donc environ 30 à 48 documents par tranche. C'est déjà sous les 59 paires nulles, sauf à mettre plusieurs paires par document, ce qui crée des grappes que la borne exacte ne couvre pas.
- Un plancher de 0,5 est vérifiable si la détection vraie dépasse 0,7 (37 à 49 dommages par tranche). Un plancher de 0,7 ne l'est que si elle dépasse 0,9.
- Tout cela s'ajoute aux 59 paires nulles et doit se faire dans un lot distinct du lot final.

**Ce qui tranche** :
- Le calcul tranche la forme : sous cible par tranche, plancher et « non mesurable » choisissent le même seuil. Ils ne diffèrent que sur trois points : faut-il des dommages plantés avant le lot final ; un banc sous plancher est-il bloqué ([D3]) ou publié avec ses strates marquées non mesurables ([A3], [B3], [I3]) ; la cible est-elle par tranche.
- **Proposition (argument)** : écrire, avant le gel, la règle « strate non mesurable si seuil admissible > taille du dommage », calculée sur les seules paires nulles. Y ajouter un plancher **déclaratif** lu une fois sur le lot final avec sa borne exacte, sans blocage. Cette combinaison garde l'apport des deux camps.

**Essai suivant (sans dépense, session habilitée)** : rejouer la section C avec ε et ρ estimés sur des relectures existantes de plans honnêtes.

## 2. Qui désigne les passages qui portent un contrôle (décision 3)

### Arguments (d'après la note v2)
- **Programme mesuré** ([A3], [B3], [E3], [H3]) : « Le repéreur n'est pas mieux établi que le programme (argument) » (l. 193). [E3] change l'unité de l'audit : « des documents entiers tirés au sort, où des annotateurs cherchent tous les contrôles, y compris ceux que ni le programme ni le repéreur n'ont trouvés » (l. 125). [A1] prédit que les erreurs du recouvrement de mots tombent là où loge le dommage : « un contrôle affaibli garde ses mots, un contrôle paraphrasé les perd » (note v1, l. 51).
- **Repéreur audité** ([C3], [F3], [G3], [I3]) : « Mesurer le biais ne répare pas les dommages mal plantés hors échantillon (argument) » (l. 194). [C3] impose des familles de modèles disjointes par rôle (l. 110), et [F3] passe à quatre familles (l. 131). [G3] abandonne sa cascade lexicale : « un leurre lexical et une paraphrase du vrai contrôle la court-circuite » (l. 137).
- **Hybride** : [D3] (l. 72).
- **Commun** : audit humain à l'aveugle par deux personnes, tirage incluant les accords et les passages non désignés, leurres, édition factice, bascule décidée sur une moitié et confirmée sur l'autre (l. 283). L'argument de coût ne départage plus : l'annotation domine, d'environ 13 à 25 heures selon [B1] et [I3] (l. 209).
- Aucun calcul du dossier ne tranche. Seul celui de [F2] est cité : sans audit des cas d'accord, les erreurs communes échappent par construction (l. 168).

### Calcul de sensibilité (fait, section E)
- **Calcul** : si une part e des dommages comptés plantés n'a en fait rien retiré, la détection mesurée vaut (1 − e) × détection vraie + e × fausse alerte. Simulé à m = 6 et t = 1 : 0,751 à e = 0, puis 0,723 / 0,695 / 0,637 / 0,578 pour e = 0,05 / 0,10 / 0,20 / 0,30.
- **Calcul** : la différence entre deux instruments vaut |e₁ − e₂| × (détection − fausse alerte). Un écart de 0,05 entre taux d'erreur coûte environ 0,04 de détection, sous la demi-largeur d'une borne exacte à 50 dommages par tranche (environ 0,12).
- **Argument** : **le choix ne pèse que si les taux d'erreur diffèrent d'au moins 0,10 à 0,15.** Le biais peut aussi jouer à la hausse, si la retouche ôte un second contrôle (note v1, l. 97).
- **Calcul** : mesurer e à ± 0,05 demande environ 150 à 200 documents audités (intervalle exact sur 200 documents : [0,062 ; 0,150]).

### Tests proposés, sans annotation ou avant elle

| Test | Ce qu'il tranche | Ce qu'il ne tranche pas | Coût | Données |
|---|---|---|---|---|
| **(i) Accord du programme avec les repéreurs existants** : recouvrement de mots sur les 160 paires « contrôle » du pilote, contre les quatre séries d'étiquettes de modèles | Si κ ≥ 0,8 et que l'accord sur les positifs est élevé, le choix importe peu sur ce banc. Si κ est bas, le programme manque les paraphrases : bascule vers repéreur ou hybride | La validité : les quatre séries viennent d'un même fournisseur, donc un biais commun reste possible. Le transfert aux documents retouchés par le tiers | Processeur, quelques minutes | Étiquettes sans texte au dépôt (`brouillons/T0.5-pilote-double-etiquetage-v1/`, `brouillons/T0.5-pilote-etiquetage-autres-modeles-v1/`). **Mesure existante** : κ de 0,81 à 0,98 entre les modèles sur les contrôles ; κ de 0,15 à 0,17 pour le 8B. Les textes des paires sont sous `donnees/` : **non lancé par moi** |
| (ii) Banc synthétique où l'emplacement des contrôles est connu par construction | Le rappel du programme selon la part de paraphrases | Si les paraphrases sont gabaritées, le programme est favorisé par construction (règle R4). Si un modèle les écrit, l'appel est payant | Processeur pour le programme ; repéreur payant, ou petit modèle local lent | À construire |
| (iii) Sensibilité de la mesure finale (fait, section E) | L'écart de taux d'erreur à partir duquel le choix compte (environ 0,10) | Les taux réels | Nul | Aucune |
| (iv) Accord du programme avec les extraits cités par les lecteurs de l'oracle (`src/controle_ia/verite_dommage/artefacts_v1.py` désigne le retrait par « l'autre lignée de lecteurs ») | Accord avec un instrument déjà codé | Ce désigneur est un juge, ce que l'accord de la note v2 interdit (l. 169) : **divergence entre code et accord, à signaler** | Processeur | Lectures hors de ma portée |

**Ce que j'ai lancé** : la section E (sensibilité). Le test (i) est faisable en moins de vingt minutes, mais seulement par une session habilitée à lire `donnees/t05-pilote-v1/`. **Recommandation** : le lancer avant l'audit humain. Il réduit la question si l'accord est très haut, et il oriente le tirage de l'audit vers les désaccords dans le cas contraire.

## Confiances
- Monotonie et absence d'effet du plancher sur le seuil sous cible par tranche : 0,9 (calcul).
- Effet du budget partagé : 0,85 (calcul).
- « Seuil de deux contrôles dans la plupart des cas réalistes » : 0,6, car cela dépend de ε et de ρ, inconnus.
- Choix de désignation de second ordre si l'écart des taux d'erreur est sous 0,1 : 0,75 (calcul). Que cet écart soit sous 0,1 sur le banc : non estimé.

## Fichiers lus
- `origin/idees/lot-8-chef-d-orchestre-v1` : `docs/notes/collisionneur-v9/questions-servies-v1/question-cinq-decisions-bancs-plantes-v2.md` ; `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-bancs-plantes-v1.md` ; `docs/decisions/decision-N-060-v3.md` (l. 1–60) ; `docs/notes/couche-2-preparation-v1/verite-dommage-v1/rapprochement-trois-voix-v1.md` (lignes trouvées par recherche) ; `docs/notes/couverture-de-l-oracle-v1/reponse-fable-couverture-oracle-v2.md` (lignes trouvées par recherche) ; `brouillons/T0.5-pilote-double-etiquetage-v1/{accord.py, accord.json, resultat.md}` ; `brouillons/T0.5-pilote-etiquetage-autres-modeles-v1/resultat.md`.
- `origin/claude/relaxed-gauss-p2t1wk` : `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-bancs-plantes-v2.md`.
- Copie locale : `src/controle_ia/verite_dommage/artefacts_v1.py` (l. 1–70).
- Non lus (interdits) : les cellules sous `runs/…cinq-decisions-v1-20261122-131546/`, et `donnees/`.
