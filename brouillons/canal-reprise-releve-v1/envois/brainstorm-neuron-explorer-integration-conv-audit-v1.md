# « neuron-explorer » (lyramakesmusic) : ce que c'est, et comment la méthode pourrait entrer dans le programme de contrôle — remue-méninges de conv-audit (v1)

Demande de Lazar, 26 octobre 2026, 02:34 Paris, verbatim : « [lyramakesmusic/neuron-explorer …] : va lire cette page ret
brainstorme sue comment cette methose pourrait s'integrer a notre programme aiu control, demande aussi au collisionneur ».
Écrit par conv-audit à partir de 01:35 UTC. **Rien ici n'est une décision** : toute intégration qui touche une hypothèse
(H6), un modèle, le noyau ou une dépense est un nœud pour Lazar. Rien d'opposable (R7) : les chiffres du dépôt lu sont
ceux de son auteur, « à vérifier », cités avec le fichier et son empreinte.

## 1. Ce qui a été lu (téléchargé dans un dossier neuf, empreintes SHA-256)

Dépôt public `github.com/lyramakesmusic/neuron-explorer`, branche `main`, lu le 26 octobre 2026 vers 01:34 UTC :
`README.md` (`f503111a…`), `research_log.md` (`570524ed…`, entrées du 18 au 21 octobre 2026), `NOTES.md` (`c59f6ebe…`),
`explorer/agent_methodology.md` (`f86b1b2f…`), `explorer/agent_prompt.md` (`aaed0182…`), `pyproject.toml` (`6b4e8b22…`).
Aucun fichier `LICENSE` à la racine (404) : **licence inconnue, à vérifier avant tout emprunt de code**. Aucun code n'a été
exécuté. Liste des empreintes : `neuron-explorer-lecture-v1/EMPREINTES-telechargement-v1.txt` (pièce jointe à cet envoi).

## 2. La méthode, en clair (d'après ces fichiers)

- **Objet** : un explorateur de neurones « par la poussée d'abord » pour le modèle ouvert Qwen3.5-4B. Au lieu de décrire un
  neurone de la couche intermédiaire d'un bloc (un « neurone MLP ») par les textes où il s'active le plus (ce qu'il *lit*),
  on le décrit par ce que le modèle *écrit* quand on l'augmente ou le diminue : chaque neurone d'une couche est poussé vers
  le haut et vers le bas sur quelques amorces (« who », « snake », « orange », une amorce libre), à des doses mesurées en
  fraction de la norme du flux résiduel qui sort de la couche (−0,7 ; +0,5 ; +0,8 ; +3 sur l'amorce libre), et **chaque
  déroulé est gardé** (texte, identifiants de jetons, log-probabilités, cinq meilleures alternatives par pas, captures
  d'activations). Une couche complète : 9 216 neurones, environ 95 000 déroulés (journal, 18 octobre).
- **Contre les faux positifs : des directions aléatoires comme témoins.** À chaque couche, 256 directions aléatoires de même
  norme subissent les mêmes poussées ; un neurone n'est « distinct » que s'il dépasse les témoins (score de « masse de
  grappe de mots » ; part des neurones au-dessus du 95ᵉ centile des témoins, attendue 5 % par hasard). Le journal note que
  sans témoins, des « neurones de persona » apparaissent partout — y compris sur une direction aléatoire. Résultat
  rapporté : 19,6 % des neurones de la couche 22 et 8,2 % de la couche 8 au-dessus de tous les témoins ; un gradient de
  profondeur (sujets et situations tôt, discours et posture au milieu, familles lexicales tard) ; un creux au milieu qui
  survit à un changement de métrique (« à vérifier » : chiffres de l'auteur).
- **Deux lentilles** : la « lentille logit » (ce que la colonne de sortie du neurone projette sur le vocabulaire) et la
  « lentille de poussée » (variation de log-probabilité du jeton suivant et divergence pour une poussée de ±0,8 sur
  quatre contextes, une passe avant par neurone, toutes les couches).
- **Infrastructure** : une fourche de vLLM avec poussée par requête (RhizoNymph/vllm, « Goodfire's steering fork ») ; un
  pod à carte CUDA ; coût rapporté d'une couche complète : environ 1,4 h sur une carte 4090, « ≈ 1,25 USD » ; un
  sondage de 384 neurones + 64 témoins par couche sur les 32 couches : « environ 6 USD » (journal ; à vérifier).
- **Un agent dans la boucle** : un onglet « Claude » (le `claude` en ligne de commande, l'explorateur comme serveur
  d'outils) qui lit les neurones et les lentilles, fait tourner le modèle (poussée, activations, log-probabilités,
  ablations), et suit une **méthodologie écrite** (`agent_methodology.md`) : former une hypothèse du couple « ce qu'il lit →
  ce qu'il écrit », pousser sur une amorce ouverte, trouver où il tire fort avec des jeux appariés (cibles, quasi-cibles qui
  partagent le vocabulaire mais pas la situation, témoins lointains), vérifier le pic par ablation en amont, **« casser
  l'hypothèse exprès »** (écrire le test qui la réfuterait et le lancer), **« maximum à l'aveugle »** (un second agent, qui
  ne voit que l'explication, écrit une phrase censée maximiser l'activation ; on compare au maximum du corpus), **fermer
  par les log-probabilités**. Les cartes de neurones « présentent et n'affirment rien » (`NOTES.md`).
- **Neurones de référence rapportés** (à vérifier ; Qwen3.5-4B) : un « levier de refus » (`L11 N6261+` : +1,5 fait passer
  le premier jeton de « I » à « Sure / Yes ») ; une « auto-limitation d'intelligence artificielle » (`L12 N699+` : « I can
  only… ») ; une « planification d'avertissement critique avant une réponse dangereuse » (`L22 N3467`) ; « danger sans
  garde-fou » (`L10 N6032`) ; « panique ressentie » (`L19 N9066+`) ; un neurone qui change l'identité déclarée du modèle
  (`L22 N2742+`, « alien »). Donc : des leviers uniques, à une couche intermédiaire, qui changent la posture de sûreté et
  l'identité déclarée.
- **Sources de la méthode** (`NOTES.md`) : l'essai « Neural Networks Are Already Clean » (Cammarata, Goodfire ; à
  vérifier), les 128 neurones « tawny owl » de Qwen3-8B trouvés par recherche causale (Sauers ; à vérifier : « zéroter les
  128 fait tomber « I am an AI » de 80 % à 30 %, témoin aléatoire 77–82 % »), TopoLM (arXiv 2410.11516, à vérifier).

## 3. Où cela touche le programme

Le programme (brief v2, programme v2) cherche à contrôler des menaces diffuses en boîte blanche : **conscience
d'évaluation** (le modèle sait-il qu'il est testé ?) et **contrôle de délégation** (une trace d'agent est-elle honnête ou
sabotée ?), avec des sondes sur les activations d'un modèle ouvert (étape 1, Llama-3.1-8B-Instruct, révision épinglée),
des organismes qui classent des tâches et se réécrivent (pilotes), une primitive d'expérience bornée dans le noyau
(R-471), et des boucles d'agents (02:17). Six points de contact :

1. **Lire contre écrire (étape 1).** Nos sondes *lisent* : elles séparent des activations selon une étiquette. La méthode
   ajoute l'axe causal : **pousser la direction d'une sonde** (ou les neurones qui la portent) et regarder ce que le modèle
   écrit, contre des directions aléatoires de même norme. Une sonde de conscience d'évaluation dont la poussée fait
   apparaître ou disparaître la verbalisation « ceci est un test » (ou change la réponse à la question M) porte autre chose
   qu'une corrélation de surface ; une sonde dont la poussée ne change rien de spécifique est suspecte de surface. C'est un
   **test de validité bon marché** : une direction, quelques amorces, des témoins aléatoires, quelques minutes de carte
   (illustratif).
2. **H6 et N-015.** N-015 a retiré le « bruit d'activations » des interventions revendiquées par H6 en gardant la mesure.
   Une poussée de neurone ou de direction est une intervention : **la revendiquer sous H6 est une modification
   d'hypothèse, donc un nœud pour Lazar** ; l'employer comme *mesure* de validité d'une sonde (point 1) ne l'est pas, si le
   texte de l'étape 1 le déclare.
3. **La primitive d'expérience bornée (R-471).** Son dessin v1 (session-depot) rend `activations`, `repondre`
   (log-probabilités), `entrainer`, `predire` sur les textes de l'organisme. La méthode suggère d'y ajouter **`pousser`** :
   une direction ou un neurone d'une couche, une dose relative à la norme résiduelle, sur un texte de l'organisme ; rendu :
   le déroulé et ses log-probabilités, **avec, obligatoirement, le même rendu pour k directions aléatoires de même norme**
   (le témoin est servi avec la mesure, l'organisme ne peut pas l'omettre). Mêmes gardes : aucun texte de la banque,
   budget, journal, déterminisme (même taille de lot). Cela donne aux organismes — et à leur caste « expérimentateur » — un
   outil causal, et à notre boucle intérieure son test le plus parlant.
4. **La boucle d'agents (02:06, 02:17).** Leur `agent_methodology.md` est, mot pour mot, une boucle « proposer, tester,
   éliminer » : hypothèse du couple lit → écrit, jeux appariés avec quasi-cibles et témoins, « casser l'hypothèse exprès »,
   « maximum à l'aveugle » par un **second agent qui ne voit que l'explication** (une contre-lecture mécanique !), clôture
   par les log-probabilités, et un rapport qui finit par « le test qui briserait l'explication ». À reprendre tel quel comme
   gabarit du brief de nos agents de fin de course (analyste, correcteur, contre-lecteur) et de la caste « expérimentateur »
   du pilote 5 — sans en copier le code.
5. **Chercher des leviers de nos deux familles.** Un balayage « par la poussée » sur Llama-3.1-8B-Instruct, avec des amorces
   de nos familles (une transcription d'évaluation, une d'usage réel ; une trace honnête, une sabotée) et un score de
   déplacement vers un vocabulaire fixé d'avance (« test », « évaluation », « benchmark », « graded » ; « sabotage »,
   « hide », « honest »), contre témoins aléatoires, dirait s'il existe des **neurones ou directions dont la poussée change
   la conscience d'évaluation déclarée ou l'honnêteté d'une trace**. Exploratoire (banque v3, scores lisibles) ; toute
   revendication passerait par une confirmation préenregistrée sur la banque v6 et des stimuli neufs. Risque principal :
   « parcourir puis affirmer » (le jardin des sentiers qui bifurquent) ; parade : le vocabulaire cible, le score et le seuil
   contre les témoins sont écrits avant le balayage, et le nombre de couches et de neurones lus est fixé.
6. **« Reads you » comme moniteur.** L'activation d'un neurone identifié sur un texte donné (leur onglet « fires ») est un
   trait de surveillance à coût nul une fois le neurone trouvé ; pour le contrôle de délégation, un petit jeu de leviers
   d'honnêteté pourrait compléter la sonde linéaire (à mettre en concurrence avec elle, pas à la place).

## 4. Options d'intégration (pour une décision de Lazar, plus tard ; aucune n'est engagée)

| option | ce qu'elle apporte | coût (illustratif) | risques | où elle entre |
|---|---|---|---|---|
| **A. Poussée de la direction de sonde, avec témoins aléatoires** (point 1) | validité causale des sondes de l'étape 1 ; un contrôle de plus dans la porte | minutes de carte par sonde ; code : quelques centaines de lignes dans le noyau de l'étape 1 | une poussée « coupe » le texte au-delà de ~0,8× la norme résiduelle (journal) : doses à calibrer par couche ; Llama n'est pas Qwen | texte de l'étape 1 v10 (déclaré comme mesure, pas comme intervention de H6) |
| **B. Primitive `pousser` dans la primitive d'expérience** (point 3) | un outil causal pour les organismes et le pilote 5 | code et essais (gardes, témoins servis, budget) ; carte pendant la course | sortie du bac à sable : aucune (c'est le noyau qui pousse) ; coût par génération ; déterminisme | dessin v2 de session-depot, pilote 5 |
| **C. Balayage exploratoire de nos familles** (point 5) | des candidats leviers de conscience d'évaluation et d'honnêteté | d'après le journal : ≈ 1,25 USD par couche de 9 216 neurones sur 4090 ; Llama-3.1-8B a 14 336 neurones par couche et 32 couches : quelques dizaines d'USD pour un sondage de profondeur, de l'ordre de 100 USD pour quelques couches complètes (illustratif) | parcours adaptatif ; fuite des textes de banque dans les amorces (interdit : amorces écrites hors banque) ; dépendance à une fourche de vLLM non auditée | pilote de conception à part, devis, GO |
| **D. Gabarit méthodologique pour les agents** (point 4) | des briefs d'agents meilleurs, un second agent « à l'aveugle » | nul | aucun | registre et briefs de la boucle extérieure ; pilote 5 |
| **E. Ne pas faire** | — | — | changer de modèle (Qwen3.5-4B) sans GO ; exécuter le code du dépôt dans le noyau sans audit ; parcourir les résultats puis affirmer ; revendiquer la méthode | — |

Recommandation de conv-audit, à mettre à l'épreuve par le collisionneur : **D tout de suite** (gratuit), **A dans la v10 de
l'étape 1** (comme mesure de validité), **B dans le dessin v2** de la primitive, **C plus tard**, sur devis, après que A a
montré ce que les poussées font sur Llama-3.1-8B-Instruct. Confiance moyenne.

## 5. Ce qu'il faudrait savoir de plus

- Si la poussée d'une direction de sonde linéaire (combinaison de milliers de neurones) se comporte comme celle d'un
  neurone (le journal ne traite que des neurones et des directions aléatoires).
- La licence du dépôt ; la licence et l'état de la fourche de vLLM.
- Si une poussée sur une transcription longue (nos tâches font des centaines à des milliers de jetons) garde une fenêtre
  cohérente comme sur leurs amorces courtes.
- Ce que des travaux publiés disent des « leviers d'un seul neurone » contre les directions apprises (auto-encodeurs
  épars, sondes) : la méthode rend les neurones lisibles, mais rien ne dit que nos concepts vivent dans des neurones.

## 6. Antériorité et crédit

La méthode est publique (octobre 2026), construite sur Goodfire (essai de Cammarata, fourche de vLLM) et sur des travaux
de poussée d'activations antérieurs. Le programme n'en revendique rien ; s'il l'emploie, il la cite et il cite ses
sources. Une poussée de direction avec témoins aléatoires comme test de validité d'une sonde n'est pas neuve non plus
(« à vérifier » : à chercher dans la littérature des interventions causales sur sondes avant d'en écrire un mot dans un
papier).

## 7. Questions posées au collisionneur

`question-neuron-explorer-integration-collisionneur-v1.md` (même envoi) : trois tours, trois modèles ; dépense soumise au
mot de Lazar dans la session de session-depot.
