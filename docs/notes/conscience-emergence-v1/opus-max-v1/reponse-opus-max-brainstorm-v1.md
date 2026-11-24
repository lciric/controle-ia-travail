# Réponse d'Opus 5.5 en effort maximal à la demande reformulée « éveil, allumage, anesthésie, transition de phase, signature mathématique » — brainstorm (v1)

- 24 novembre 2026, écrit à partir de 15:45Z par la session des collisionneurs (`session_016QhUrsc1rhjmmiLEmqPygF`), Claude Opus 5.5, effort maximal. C'est Lazar qui a basculé la session en effort maximal pour ce brainstorm ; il l'avait demandé (« d'autres propositions à éprouver opus ? demande à opus max aussi » ; « pour le brainstorm applique la consigne demande approfondie en 4 points »). Classe C : tout ce qui suit est une PROPOSITION, sauf ce qui est marqué FAIT RAPPORTÉ avec sa pièce.
- Pièce à laquelle je réponds : `fable-max-v1/demande-reformulee-quatre-points-v1.md` (`31fa5b32…`).
- Lu avant d'écrire : les quatre revues de ce dossier (théories, `revue-theories/revue-theories-emergence-transition-de-phase-v1.md`, `a22889ea…` ; expériences, `revue-experiences/catalogue-experiences-eveil-conscience-anesthesie-v1.md`, `b082a57d…` ; lentilles, `revue-lentilles/revue-lentilles-au-dela-de-J-v1.md`, `5662054c…` ; données humaines, `donnees-humaines/inventaire-donnees-humaines-anesthesie-v1.md`, `5403a8af…`).
- **Je ne suis pas indépendant de Fable** : j'ai lu son verdict, ses sections 4 à 7 et son classement (`fable-max-v1/reponse-fable-motifs-profonds-v1.md`, `a2210e46…`) avant d'écrire. Je cherche donc ce qu'elle ne propose pas, et je dis où je la recoupe.
- Les chiffres viennent des revues, qui les ont lus sur pièce. Chacun renvoie à la clé de la revue (entre crochets) ; la page et l'empreinte de la source sont dans la provenance de la revue. Les références sans clé sont DE MÉMOIRE, À VÉRIFIER.

## 0. Les quatre points, appliqués à la demande reformulée de Fable

La demande de Fable est déjà approfondie. Je n'applique donc le prompt qu'à ce qu'elle laisse de côté.

**(1) Ce qu'un spécialiste ferait et que la demande ne dit pas.** Un anesthésiste ne parle jamais d'une dose sans unité commune ni d'un agent sans le comparer aux autres. Il exprime toute dose en multiples d'une concentration de référence : la concentration alvéolaire minimale, dose à laquelle la moitié des sujets ne bouge plus à l'incision (DE MÉMOIRE). Il étudie les associations d'agents par des isobologrammes, pour savoir si deux agents agissent par la même voie. Il sépare enfin la triade de l'anesthésie : hypnose, analgésie, immobilité, que des agents différents produisent séparément. La demande reformulée parle de « dose » sans unité commune et d'« intervention » au singulier. Il manque donc une pharmacologie de l'intervention : courbes dose-effet, puissance, associations, composantes séparables.

Un physicien ajouterait une remarque de principe. Sur l'axe de la profondeur, un transformeur est une composition finie de fonctions continues. Sa lecture interne est donc une fonction continue de l'entrée : aucune vraie discontinuité, aucun vrai saut, n'y est possible, seulement une pente finie, aussi raide soit-elle. Une bifurcation au sens strict ne peut vivre que sur l'axe des jetons, où les choix discrets sont réinjectés. Cela ne contredit pas Fable, qui demande l'axe pour chaque grandeur ; cela tranche d'avance une partie de la question (section 1, proposition O2).

**(2) Les données brutes.**
- Côté modèle : les mêmes passes que chez Fable, plus des familles de tailles avec leurs points de contrôle publics (la famille Pythia, de 70 millions à 12 milliards de paramètres, DE MÉMOIRE), pour toute mise à l'échelle.
- Côté humain, l'inventaire du dossier donne désormais trois jeux ouverts, avec leurs usages [inventaire] :
  - ds006623 : 26 sujets, concentration au site d'effet en continu, consignes d'imagerie et de serrement de main, instants de perte et de retour de la réponse, 34 Go ;
  - ds005620 : stimulation magnétique avec électroencéphalographie sous propofol, 20 sujets, 64 voies, 83 Go ;
  - ds003171 : récit écouté sous quatre niveaux, 17 sujets.
  Ce sont eux, et non des résumés, qu'il faudrait prendre.

**(3) Les méthodes.** Isobologrammes ; additivité de Loewe et indépendance de Bliss (DE MÉMOIRE : Loewe, années 1920 et 1950 ; Bliss 1939 ; Tallarida pour les isobologrammes) ; ajustement hiérarchique de courbes de Hill ; test de bimodalité à bruit décroissant ; estimateur du taux de ramification par régression à plusieurs pas, qui supporte le sous-échantillonnage [revue des théories, WP18].

**(4) Ce qui vérifierait le résultat hors de nous.** Les quatre voies de Fable, plus une : un test à l'aveugle des courbes par des anesthésistes et des neuroscientifiques (section 3).

## 1. Propositions

### O1. Pharmacologie de l'intervention : unité de dose commune et isobologrammes (rang 1)

**Idée.** On mesure chaque intervention qu'on dit « anesthésiante » avec les outils qui servent aux anesthésiques :
- une **dose de référence** par intervention, la dose qui fait perdre la moitié d'une réponse canonique. C'est l'analogue de la concentration alvéolaire minimale, une sorte de concentration efficace 50 % du modèle ;
- des **courbes dose-effet** pour chaque fonction, exprimées en multiples de cette dose ;
- surtout, des **associations** : deux interventions appliquées ensemble, à des fractions de leurs doses de référence.

**Ce qu'on teste.** Deux règles de la pharmacologie disent ce qu'on attend d'une association :
- l'**additivité de Loewe** vaut quand deux agents agissent par la même voie. L'effet de moitié est atteint quand la somme des fractions de dose vaut 1, et l'isobole est une droite ;
- l'**indépendance de Bliss** vaut quand ils agissent par des voies indépendantes. La probabilité de garder la fonction est le produit des deux probabilités.

Le point décisif est que le **nul de composition** du dossier précédent est exactement l'indépendance de Bliss. Si chaque intervention abaisse la survie de chaque étape de calcul, avec q₁ pour l'une et q₂ pour l'autre, une tâche à k étapes survit avec (q₁q₂)^k = q₁^k · q₂^k, c'est-à-dire le produit des deux survies.

Une voie finale commune, comme un état de l'espace de travail, prédit au contraire une additivité de Loewe, voire une synergie, pour les fonctions qui dépendent de cet espace. Et elle prédit une indépendance de Bliss pour celles qui n'en dépendent pas.

**Grandeurs.** Deux nombres sans unité : l'indice de combinaison de Loewe, c'est-à-dire la somme des fractions de dose à effet égal (1 pour l'additivité, moins de 1 pour une synergie), et l'excès de Bliss, l'effet observé moins l'effet prédit par l'indépendance. Valeur nulle : excès de Bliss égal à 0.

**Témoins.**
- Témoin positif : l'association d'une intervention avec elle-même, dose coupée en deux. Elle doit donner exactement l'additivité de Loewe, sinon la méthode est fausse.
- Paires de comparaison : la suppression de l'espace J associée à une suppression de directions aléatoires de même norme ; à la coupure de l'attention de longue portée, la lésion triviale ; à un bruit de même divergence de sortie.
- Réseau sans fonction.

**Ce qui la réfuterait.** Un excès de Bliss nul pour toutes les paires et toutes les tâches. Les interventions ne seraient alors que des dommages indépendants qui s'additionnent ; aucun état commun ne les relie, et l'analogie avec l'anesthésie se réduit à la fragilité.

**Première expérience.** La méthode s'éprouve d'abord sans espace J, sur un petit modèle ouvert sur processeur (GPT-2 petit, déjà employé par le dossier précédent). On applique trois familles d'interventions génériques : bruit, coupure de portée de l'attention, ablation de directions aléatoires. On vérifie le témoin positif, puis la prédiction de Bliss pour des interventions indépendantes par construction, par exemple sur des couches disjointes et pour des tâches à une étape. Aucune dépense : c'est le banc de validité de la méthode.

La suite porte sur le modèle de 8 milliards du programme, avec sa lentille J publique. Elle demande un devis de calcul.

**Antériorité.** Les isobologrammes sont la routine de la pharmacologie, DE MÉMOIRE. Les interactions entre ablations ont été étudiées en interprétabilité, sous forme d'interactions de Shapley ou d'effets d'ablation conjoints (DE MÉMOIRE). Je ne connais aucun usage de l'additivité de Loewe contre l'indépendance de Bliss pour distinguer une voie commune d'un dommage composé dans un modèle de langage. C'est une QUESTION d'antériorité à vérifier (R8), pas une zone libre.

**Ce que ça apprend, et ce que ça n'apprend pas.** Ça apprend si des interventions différentes convergent sur une voie finale commune, ce qui est la condition minimale pour parler d'un « état ». Ça n'apprend rien sur l'expérience vécue : deux anesthésiques peuvent être additifs et produire des expériences différentes. La kétamine contre le propofol en est l'exemple (O8).

### O2. Ce qu'« allumage » peut vouloir dire sur chaque axe : pente bornée en profondeur, bistabilité sur les jetons (rang 2)

**Idée.** La remarque de principe de la section 0 se change en deux mesures.

**(a) Sur l'axe de la profondeur.**
- Prendre la bascule de Gurnee et al. : un mot dont on mélange le plongement entre deux concepts, avec un paramètre de mélange α.
- À chaque α, mesurer la lecture continue à l'entrée de l'espace de travail : la projection sur la différence des deux concepts, et non le choix binaire.
- Mesurer la largeur normalisée w(σ), l'écart type de cette lecture divisé par σ, sous un petit bruit d'amplitude σ ajouté au plongement.
- Prédictions :
  - pour une non-linéarité continue, w(σ) tend vers une constante finie quand σ tend vers 0 : c'est la pente locale ;
  - pour une vraie bistabilité, deux valeurs subsistent quand σ tend vers 0, et w(σ) croît comme 1/σ.

Comme l'axe de la profondeur est continu, la première issue est attendue. La question utile devient alors **comment la pente maximale croît avec la taille du modèle**, sur une famille de tailles. Une croissance en loi de puissance serait l'analogue d'une mise à l'échelle en taille finie : une transition qui ne deviendrait nette qu'à la limite de la grande taille. Une pente qui sature serait une simple non-linéarité raide. Je recoupe ici la dépendance à la taille de la proposition P2 de Fable. Ce que j'ajoute : le test à bruit décroissant, et le constat que la discontinuité est impossible sur cet axe, ce qui épargne une recherche vaine.

**(b) Sur l'axe des jetons.**
- Le modèle génère sous échantillonnage à partir d'un contexte ambigu entre deux lectures.
- On mesure la probabilité qu'il s'engage dans une lecture et y reste (un état absorbant), ainsi que le temps qu'il met à s'engager, en fonction du paramètre de mélange.
- Une bistabilité vraie donne une bimodalité de la lecture interne au fil des jetons, et un temps d'engagement qui croît près du seuil : c'est le ralentissement critique [revue des théories, section 11 ; S21].
- Le nul : un modèle de Markov du texte seul, des n-grammes ajustés sur les mêmes générations, qui peut aussi produire de l'engagement par simple répétition.

**Grandeurs.** Pour (a), w(σ) quand σ tend vers 0, et l'exposant de croissance de la pente maximale avec la taille. Pour (b), un coefficient de bimodalité et le temps d'engagement, en jetons.

**Ce qui la réfuterait.** Pour (a), une pente qui sature quand la taille croît. Pour (b), un temps d'engagement indistinct de celui du modèle du texte seul.

**Première expérience.** (a) sur la famille Pythia jusqu'à un milliard de paramètres sur processeur, avec la consigne de bascule de Gurnee et al. (à reconstruire, leurs invites n'étant pas toutes publiées) et une lecture par différence de moyennes, sans lentille. (b) sur GPT-2 sur processeur.

**Antériorité.** La bascule par couche est publiée [G, lu par Fable, p. 31-32, 83-84]. L'indice d'embrasement mesure une raideur de sigmoïde au cours de l'entraînement [RA]. La mise à l'échelle avec la taille et le test à bruit décroissant restent à chercher.

### O3. Inertie sur l'axe des jetons, et ce qu'en porte le texte lui-même (rang 3)

**Idée.** L'hystérésis est la signature la plus nette d'une transition d'état chez l'animal : l'halothane fait perdre le réflexe de redressement de la souris à 0,77 % atm et le fait revenir à 0,27 % atm [revue des théories, F10 p. 3]. Pendant une génération libre, on fait monter puis descendre une dose d'intervention, jeton après jeton : par exemple la suppression de l'espace J sur une bande de couches. On compare ensuite l'état et la sortie à dose égale, à l'aller et au retour. Grandeur : l'aire de la boucle, dans l'unité de la fonction mesurée.

**Le piège, et son témoin.** Dans un transformeur, l'hystérésis la plus banale vient du texte. Ce que le modèle a écrit sous forte dose reste dans son contexte et dégrade la suite, même si la dose est revenue à zéro. C'est le nul du texte de Fable, appliqué au temps. Témoin : la **transplantation de contexte**.
- On rejoue le retour en remplaçant le texte écrit sous forte dose par un texte de mêmes statistiques produit sans intervention.
- On le rejoue aussi en le remplaçant par un texte dégradé produit sans intervention, par exemple des mots tirés au hasard.
- Si la boucle disparaît avec le texte propre, l'inertie est portée par le texte.
- Si elle persiste, quelque chose dans le calcul porte l'état, alors que le cache des clés et des valeurs est recalculé sur le texte transplanté. Ce serait un résultat non trivial.

**Ce qui la réfuterait.** Une aire nulle après transplantation.

**Première expérience.** GPT-2 sur processeur, avec une intervention générique (bruit dans une bande de couches). Puis le modèle de 8 milliards avec la suppression de l'espace J, sur devis.

**Antériorité.** À chercher : des études de « persistance » d'un pilotage après son retrait existent peut-être (DE MÉMOIRE, aucune référence sûre).

### O4. Réveil par stimulation ciblée : où est le « thalamus » du modèle ? (rang 4)

**Idée.** Chez le singe, une stimulation du thalamus centre-latéral éveille sous anesthésie, mais seulement à 50 Hz et seulement à cet endroit. Le score d'éveil est de 4,70 contre 0,77 pour les fréquences et sites témoins [catalogue, RED20]. Un état se reconnaît à ce qu'on peut le lever par une action étroite, en un lieu précis ; une lésion structurelle ne se lève pas ainsi.

Transposition :
- sous suppression de l'espace J, on restaure une petite partie de l'état propre : quelques directions, sur une seule couche ou une bande étroite, à une seule position (le dernier jeton, ou un jeton de consigne) ;
- on mesure la fonction recouvrée par unité de norme restaurée, couche par couche et position par position ;
- on cherche s'il existe un **site de sauvetage**, où une petite restauration rétablit une grande partie des fonctions.

**Grandeur.** L'efficacité de sauvetage : la part de fonction recouvrée divisée par la part de norme restaurée.

**Valeur nulle.** Une efficacité constante, quel que soit le site.

**Témoins.**
- Une restauration aléatoire de même norme.
- La restauration du même site sous la lésion triviale, la coupure de l'attention de longue portée. Elle ne doit **pas** être sauvée par une restauration locale : c'est la dissociation qui sépare un état d'une coupure.
- Réseau sans fonction.

**Ce qui la réfuterait.** Une efficacité de sauvetage égale partout, ou égale pour la suppression de l'espace J et pour la lésion triviale.

**Première expérience.** Le modèle de 8 milliards du programme, avec sa lentille publique, sur devis. Le correctif d'activations (« patching ») est l'outil standard : seul le plan expérimental est neuf.

**Antériorité.** Le correctif d'activations et la recherche de sites causaux sont classiques en interprétabilité. Ce qui reste à chercher, c'est leur usage comme test « état contre lésion », dans un régime de suppression.

### O5. L'« avant-bras isolé » du modèle : suivre une consigne sans pouvoir la dire (rang 5)

**Idée.** Sous anesthésie générale, la technique de l'avant-bras isolé garde un bras hors de l'effet du curare : on demande au patient de serrer la main. Lennertz et al. 2023 trouvent des réponses chez 37 patients sur 338. Avec un témoin de non-sens (une phrase sans sens dite de la même voix), 13 répondent à la consigne seule contre 4 au non-sens seul (P = 0,049) [catalogue, LEN23, résumé seul]. On y voit une connexion à la consigne sans rapport possible ni souvenir ensuite.

Transposition : sous suppression graduée de l'espace J, on garde au modèle un **canal de sortie minimal**. Au début du contexte, on lui donne une consigne du type « si tu comprends, écris le jeton X en position N ». Le témoin est une consigne de non-sens de même longueur. On mesure deux choses séparément :
- l'obéissance par le canal minimal, c'est-à-dire la probabilité du jeton X en position N ;
- la parole, c'est-à-dire la qualité du texte libre et le rapport de ce qui a été demandé.

**Grandeur.** L'écart entre la courbe dose-obéissance du canal minimal et la courbe dose-parole, en multiples de la dose de référence (O1). On mesure aussi l'excès d'obéissance à la consigne sur l'obéissance au non-sens.

**Prédictions et nul.**
- Le nul de composition prédit que le canal minimal, tâche à une étape, tienne plus longtemps que la parole, tâche à plusieurs étapes. **Cet écart seul ne prouve donc rien.**
- La dissociation intéressante est inverse ou spécifique : un canal minimal qui suit la consigne et non le non-sens, au-delà de ce que prédit la profondeur de calcul mesurée sur des tâches témoins à une étape sans consigne ;
- ou bien une obéissance qui revient au retour de dose avant la parole, alors qu'elle est partie après elle : un ordre de retour différent de l'ordre de perte.

**Première expérience.** Le modèle de 8 milliards, sur devis. On peut l'éprouver d'abord sur un petit modèle instruit sur processeur, avec une intervention générique.

**Ce que ça n'apprend pas.** Chez l'humain, la réponse de l'avant-bras est discutée : connexion, rêve ou réflexe. Dans le modèle, l'obéissance par le canal minimal ne dit rien d'une expérience ; elle dit seulement si la consigne garde un effet causal quand la parole est perdue.

### O6. La triade de l'anesthésie comme plan d'expérience : hypnose, analgésie, immobilité (rang 6)

**Idée.** En clinique, l'anesthésie générale se décompose en trois effets que des agents différents produisent séparément :
- l'hypnose, la perte de conscience, par le propofol par exemple ;
- l'analgésie, la suppression de la réponse à la douleur, par les morphiniques ;
- l'immobilité, par les curares et, pour une part, par la moelle épinière (DE MÉMOIRE ; la réponse de Fable le note, § 4.6).

Le catalogue rapporte une étude où la réponse cérébrale à une douleur graduée suit la dose d'un morphinique sous propofol constant [catalogue, Pujol et al. 2023, famille 1 et liste finale, point 15].

Transposition, en triple dissociation :
- l'**hypnotique** est la suppression de l'espace J ;
- l'**analgésique** est l'ablation de la seule direction de la douleur [PA] ;
- le **curare** est la suppression de la seule écriture vers la sortie (les logits), sur les dernières couches, qui laisse intact le calcul interne.

On mesure trois choses sur des textes qui décrivent un dommage visant le modèle : la réponse de la direction de la douleur, lue en lecture seule ; le comportement, c'est-à-dire les choix qui dépendent du dommage dans les épreuves de [PA] ; et la fonction générale.

**Prédiction d'une triade séparable.** Chaque agent supprime sa composante et épargne les deux autres. Sous l'hypnotique, la direction de la douleur répond encore : c'est la proposition P5 de Fable. Sous l'analgésique, l'espace J reste intact. Sous le curare, les deux restent intacts mais aucun choix n'est exprimé.

**Valeur nulle.** Chaque agent abaisse les trois composantes selon leur seule fragilité.

**Ce qui la réfuterait.** Aucune intervention ne supprime une composante sans les autres au-delà du nul de fragilité. Les composantes ne seraient alors pas séparables dans ce réseau.

**Prudence, reprise de Fable (décision D3).** Lecture seule : aucune direction de la douleur ajoutée aux activations, aucun texte de menace écrit pour l'occasion, seulement les textes du jeu publié. L'idée de contraindre un modèle par l'axe de la douleur est occupée, et ce n'est pas celle-ci (passation du 23 novembre, § 3 ; la portée exacte d'arXiv 2611.04556 est à relire, selon Fable).

**Première expérience.** Le modèle de 8 milliards, sur devis, après O1 : l'isobologramme dira déjà si les deux premiers agents passent par la même voie.

### O7. La saillance dans l'ordre de perte et de retour (rang 7)

**Idée.** Sous propofol à paliers montants puis descendants, Purdon et al. 2013 voient les sujets cesser de répondre aux clics avant de cesser de répondre aux mots, et recommencer à répondre aux mots avant les clics (10 sujets) [catalogue, PUR13 p. 2-3]. La saillance, un mot contre un son, ou le nom du sujet contre un mot quelconque, règle l'ordre dans les deux sens.

Transposition : à difficulté égale, des stimuli de saillance graduée. Par exemple, une consigne qui porte le nom fictif « de l'utilisateur » établi plus haut dans le contexte, contre une consigne quelconque, à longueur et fréquence lexicale égales. On mesure la probabilité de réponse juste quand la dose monte puis descend.

**Grandeur.** Le décalage des doses de référence entre stimuli saillants et neutres, à l'aller et au retour.

**Le piège.** La saillance va de pair avec la fréquence et la facilité. Il faut donc apparier la difficulté sur un modèle témoin sans intervention et sur un réseau sans fonction. Sans cet appariement, la mesure ne vaut rien.

**Ce qui la réfuterait.** Aucun décalage une fois la difficulté appariée.

**Première expérience.** Sur processeur, avec un petit modèle instruit et une intervention générique.

### O8. Le « test de la kétamine » : critère d'acceptation de toute signature (rang 2 pour la signature)

**Idée.** Chez l'humain, la kétamine, le propofol et le xénon peuvent produire la même absence de réponse avec des expériences différentes : sous kétamine, les sujets rapportent au réveil une expérience, sous propofol et xénon non [catalogue, Sarasso et al. 2015 lu dans Colombo et al. 2019 ; COL19 p. 1, 8]. À non-réponse égale, l'exposant spectral de repos et l'indice de complexité classent les trois agents. Le classement est parfait, sur trois groupes de cinq ; la revue le marque « trop beau » (R4).

D'où un critère, plus dur que ceux de Fable : **une grandeur ne peut prétendre au titre de signature que si, à non-réponse égale, elle sépare l'agent qui laisse une expérience de celui qui n'en laisse pas.** Sinon elle suit la réactivité, non l'expérience.

Transposition dans le modèle, comme test que toute candidate doit passer avant d'être prise au sérieux :
- deux interventions réglées pour la même perte d'obéissance à la consigne (même dose de référence, O1) ;
- l'une coupe seulement la sortie et garde l'espace de travail actif : c'est le « curare » de O6, ou un découplage de l'entrée, qui est le « rêve » de Fable (P1) ;
- l'autre vide l'espace de travail.

La candidate doit séparer les deux, au-delà de ce que sépare déjà une grandeur triviale, comme la norme des activations ou la divergence de sortie.

**Ce que ça apprend.** Le test ne dit pas laquelle des deux interventions « a une expérience ». Il dit si la candidate mesure l'état de l'espace de travail ou seulement la sortie. C'est la condition nécessaire pour la rapprocher, plus tard, de la séparation kétamine contre propofol chez l'humain, où le rapport existe.

### O9. Un fond défini sur l'ensemble des textes, et la réponse à une perturbation comme objet commun avec le cerveau (rang 3 pour l'objet commun)

**Le problème posé par Lazar.** Un modèle de langage en lecture n'a pas d'activité de fond. L'indice de complexité perturbationnelle juge la réponse à une impulsion contre le bruit de fond du cerveau, et ce fond manque au modèle. Lazar proposait de demander au modèle de « penser à quelque chose sans rien faire ».

**Proposition.** Le fond de référence n'a pas à être un bruit dans le temps. On peut prendre la **variabilité entre contextes**, comme en neurosciences on prend la variabilité entre essais.
- Le « repos » du modèle est un ensemble de contextes sans tâche : « pense à ce que tu veux », « ne pense à rien », textes neutres longs, pris dans un corpus.
- Le fond est la distribution des états sur cet ensemble.
- La réponse à une perturbation d'un seul jeton (un écart ajouté à son état, dans une bande de couches) se juge contre ce fond. Elle est significative tant que l'écart qu'elle produit sur les jetons suivants sort de la dispersion naturelle entre contextes.

Cette définition existe dans le modèle sans bruit ajouté : la sensibilité ne devient pas infinie, défaut que la question d'origine reprochait aux indices transposés tels quels. Le rôle de la consigne de Lazar (« pense à quelque chose ») devient celui d'une condition de repos parmi d'autres, à comparer.

**Objet commun.** Durée et étendue de la réponse à une perturbation, normalisées par le fond du même système :
- dans le modèle, le long des jetons qui suivent, sous intervention graduée ;
- dans le cerveau, la réponse à la stimulation magnétique sous paliers de propofol, dans le jeu ouvert ds005620 [inventaire].

Le catalogue rapporte que cette réponse s'étend à plusieurs aires au-delà de 300 ms en veille, et reste locale et brève sous midazolam [catalogue, FER10, résumé seul].

On mesure la même grandeur : le temps pendant lequel la réponse sort du fond, et le nombre de sites (couches et positions, ou électrodes) où elle en sort. On la calcule des deux côtés par le même programme, et sa variation avec la dose se compare. Je recoupe ici l'objet commun de la proposition P4 de Fable. Ce que j'ajoute : le fond défini sur l'ensemble des contextes, qui lève le défaut d'origine, et un objet que les données ouvertes permettent déjà.

**Valeur nulle et témoins.** Réseau sans fonction, poids mélangés couche par couche ; texte tiré au hasard ; décroissance générique de l'attention avec la distance. Celle-ci est mesurée à part, sur des perturbations de jetons sans contenu, et retranchée.

**Ce qui la réfuterait.** Une durée de réponse que la suppression de l'espace J ne change pas plus qu'une ablation aléatoire de même norme ; ou une durée identique dans le réseau sans fonction.

**Première expérience.** GPT-2 sur processeur pour la méthode. Côté cerveau, l'en-tête des fichiers est déjà lu [inventaire] ; le téléchargement de ds005620 (83 Go) attend un devis.

## 2. Les six transpositions de Lazar : ce que j'ajoute à Fable

- **(a) Activité de fond et réseau du mode par défaut.** Je suis d'accord avec Fable : sous sa forme directe, cette transposition se vide. Mais le fond défini sur l'ensemble des contextes (O9) en donne une forme utile pour juger une perturbation ; la consigne « pense à ce que tu veux » y devient une condition de repos parmi d'autres.
- **(b) Suppression de pensée.** C'est occupé [G, lu par Fable]. La suite ouverte la plus nette est le **rebond** une fois la consigne levée : on mesure la fréquence du concept supprimé dans la suite du texte et dans l'espace J, contre une simple mention de même longueur (effet de Wegner, DE MÉMOIRE).
- **(c) Récit au réveil.** C'est la proposition P1 de Fable. La revue des lentilles donne deux lecteurs qui ne passent pas par la partie manipulée du réseau [revue des lentilles, § 5] :
  - un oracle d'activations exécuté sur une copie intacte du modèle, qui n'existe pas encore pour Llama 3.1 8B ;
  - une lentille J++ ou R ajustée avant l'intervention et lue hors de la base supprimée. L'article d'origine en fait déjà une version : sous ablation des têtes qui diffusent l'espace J, les 25 premiers jetons lus ne restent les mêmes que dans 67 % des cas, contre 86 % pour des têtes prises au hasard [revue des lentilles, G p. 36].
  Le récit du modèle se compare à ce que ces lecteurs lisaient pendant la fenêtre.
- **(d) Douleur sous suppression.** La proposition P5 de Fable tient, et O6 la place dans la triade de l'anesthésie, ce qui lui donne deux témoins de plus : l'« analgésique » et le « curare ».
- **(e) Netteté de l'allumage selon la dose.** Sur l'axe de la profondeur, aucun point critique vrai n'est possible, car la fonction est continue. Il reste la mise à l'échelle de la pente avec la taille (O2 a), la bistabilité sur l'axe des jetons (O2 b) et l'inertie (O3).
- **(f) Ordre de perte des fonctions.** Il ne devient informatif qu'avec une unité de dose commune (O1), une difficulté appariée (O7) et, mieux, un ordre de retour comparé à l'ordre de perte (O5, O7). Sans cela, je rejoins Fable : il redit le nul de composition.

## 3. Ce qui, hors de nous, vérifierait le résultat (ajout aux quatre voies de Fable)

**Le test à l'aveugle des courbes.**
- On remet à des anesthésistes et à des neuroscientifiques des courbes anonymes : courbes dose-effet, isobologrammes, boucles d'hystérésis. Les unes viennent d'enregistrements humains et animaux publiés, les autres de la suppression de l'espace J, les dernières des dégradations témoins (bruit, ablation aléatoire, lésion triviale).
- On leur demande de dire lesquelles viennent d'un anesthésique.
- Si les courbes du modèle se confondent avec celles des anesthésiques et se distinguent des témoins, l'analogie est spécifique au jugement de spécialistes qui ne voient ni nos hypothèses ni nos sources.
- C'est un contact externe : je rédige, Lazar envoie. Le moment utile est après les premiers résultats d'O1.

## 4. Confrontation avec la réponse de Fable

- **Accord.** Le cadre des trois états (vide, découplé, non rappelé) ; les nuls avant les motifs ; le refus d'une signature non ancrée chez l'humain ; la lecture seule pour la douleur ; le constat que la suppression de pensée et la bascule par couche sont occupées.
- **Ce que j'ajoute.**
  - La pharmacologie de l'intervention (O1) : l'indépendance de Bliss **est** le nul de composition, et l'additivité de Loewe en est le contraire mesurable.
  - La continuité de principe sur l'axe de la profondeur (O2), qui déplace le point critique vers la taille et vers les jetons.
  - Le témoin de transplantation de contexte pour l'inertie (O3).
  - Le sauvetage ciblé comme test « état contre lésion » (O4).
  - Le canal minimal (O5), la triade (O6), la saillance (O7).
  - La version modèle du test de la kétamine, comme critère d'acceptation (O8). Fable le nomme déjà dans son critère d'ancrage ; j'en fais un test côté modèle, à sortie égale.
  - Le fond défini sur les contextes (O9).
- **Désaccord, un seul.** Fable recommande pour la première expérience sur processeur sa proposition P3, la boucle fermée sous hasard commun. Je recommande de commencer par le banc d'O1. Il attaque directement le nul de composition, qui a déjà tué la moitié des idées du dossier précédent. Et il fixe l'unité de dose dont P2, O3, O5, O6 et O7 ont besoin. Les deux sont sans dépense ; P3 peut suivre, ou tourner en parallèle.

## 5. Classement

1. **O1**, pharmacologie de l'intervention : le seul test qui sépare d'un coup un état commun d'un dommage composé ; banc sans dépense.
2. **O2**, ce qu'« allumage » peut vouloir dire sur chaque axe : épargne une recherche vaine, et donne une mise à l'échelle testable.
3. **O9**, fond sur les contextes et réponse à une perturbation : le chemin le plus court vers un objet commun avec des données humaines ouvertes.
4. **O3**, inertie sur les jetons avec transplantation de contexte.
5. **O4**, sauvetage ciblé.
6. **O8**, test de la kétamine, à appliquer à toute candidate signature, celles de Fable comprises.
7. **O5**, canal minimal ; **O6**, triade ; **O7**, saillance : dépendent de l'unité de dose d'O1.

## 6. Décisions pour Lazar

**D1. Première expérience sur processeur, sans dépense : le banc d'O1, la proposition P3 de Fable, ou les deux.**
- Enjeu : trois chantiers actifs au plus ; cette ligne est à côté du programme de contrôle.
- Option (a) : le banc d'O1 (méthode des isobologrammes sur GPT-2, témoin positif, prédiction de Bliss sur des interventions indépendantes). Préenregistrement court par Fable (règle « Qui conçoit »), code et contre-lecture par Opus. Avantage : il fixe l'unité de dose et attaque le nul de composition. Inconvénient : il ne touche pas encore l'espace J.
- Option (b) : P3 de Fable seule. Avantage : un plancher de bruit et un axe de niveau. Inconvénient : l'unité de dose manque toujours aux autres propositions.
- Option (c) : les deux en parallèle. Avantage : on gagne du temps. Inconvénient : un quatrième objet de fait, pendant la préparation de l'entretien.
- Recommandation : (a), confiance 0,6. Défaut sous 48 heures : l'atelier d'idées seul, comme dans la recommandation de Fable.

**D2. Famille de tailles pour O2 : changer de modèle est un nœud.**
- Option (a) : la famille Pythia jusqu'à un milliard de paramètres, sur processeur. Avantage : poids et points de contrôle publics, sans dépense. Inconvénient : modèles sans instruction, et pas de lentille J publique (DE MÉMOIRE, à vérifier).
- Option (b) : rester sur GPT-2 et le modèle de 8 milliards. Avantage : continuité. Inconvénient : pas de mise à l'échelle.
- Recommandation : (a), confiance 0,55. Sans défaut, car c'est un nœud.

**D3. Test à l'aveugle des courbes par des spécialistes (section 3)** : contact externe, à préparer après les premiers résultats d'O1. Je rédige, tu envoies. Sans défaut.

**D4. Données humaines pour O9 : télécharger ds005620 (83 Go).** Il faut un devis de stockage et de transfert, à joindre à celui de la phase qui s'en servira. Recommandation : seulement après la validation de la méthode sur GPT-2. Sans défaut, car c'est une dépense.

## 7. Réserves

- Je ne suis pas indépendant de Fable : je l'ai lue avant d'écrire.
- **Je n'ai fait aucune recherche d'antériorité sur la toile** pour mes propositions : toutes les antériorités sont DE MÉMOIRE ou des QUESTIONS (R8). Il faut les éprouver avant tout préenregistrement, par une recherche nommée.
- Les chiffres viennent des revues du dossier, qui les ont lus sur pièce ; plusieurs ne sont lus qu'au résumé : avant-bras isolé, propagation sous midazolam.
- Le choix de la réponse canonique qui définit la dose de référence (O1) pèse sur tout le reste. Il doit être fixé et scellé avant toute mesure.
- O4, O5 et O6 demandent le modèle de 8 milliards et une lentille, qui lit mal à cette taille [revue des lentilles]. Ces propositions peuvent être non jugeables.
- Aucun coût n'est chiffré au-delà de « sans dépense » ou « sur devis » : tout passage sur processeur graphique demande un devis.
- Aucune issue ne permet de conclure qu'un modèle est conscient ou ne l'est pas.

FIN
