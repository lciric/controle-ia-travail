# Contre-lecture du rapport H1 (trois PDF du niveau 3, constat M1) — v1

- **Date et heures** : début 2026-11-13 23:46:20 UTC (heure de création du dossier de travail, relevée par `date -u -r`) ; contre-lecture écrite à 2026-11-13 23:52:59 UTC (`date -u` dans la commande d'écriture).
- **Rôle et modèle** : contre-lecteur, modèle B. L'auteur du rapport est le modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- **Objet** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-H1-v1.md`, empreinte vérifiée `46e77d0992a0744a34335beb5953bf24bdcbc1cf447d7bfc8b0adc6f40a5a4fe` (concorde) ; son archive `fichiers-de-travail-H1-v1.tar`, empreinte vérifiée `3472422771346addc8f8341563dbba206a10786673e341c270a00907682d7444` (concorde), extraite dans mon dossier de travail.
- **Consigne commune** : `consigne-lecteur-compte-2-v1.md`, lue en entier (lignes 1 à 41), empreinte vérifiée `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (concorde).
- **Empreintes des PDF** (compagnon `.sha256` et calcul concordants) :
  - `lot8/2610.31593v1.pdf` : `b127a5d0e34a118dc03f784d69028ffaf0d71381b43f165899b100168a5fbd5f` (22 pages) ;
  - `lot8/2604.15384v2.pdf` : `d294bf631a15d89d48e5e9311b82cd6b31d578929bf7846f169ebd9c1ed3f12e` (51 pages) ;
  - `lot3/2610.39766v1.pdf` : `e17604d3769d516cdc2c5a907f3531c47616acaaaa2fc9516a3d2c649f29b728` (22 pages).
- **Fichiers du dépôt lus, et lignes** (aucun autre) :
  - la consigne commune (1 à 41) ; le rapport H1 (1 à 238) ;
  - `docs/programme-controle-ia-v2.md` (85 à 125 ; 180 à 200) ;
  - `docs/decisions/decision-N-055-v1.md` (32 à 37) ; `docs/decisions/decision-N-056-v1.md` (36 à 80) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` (62 à 99) ;
  - `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md` (264 à 292).
- **Écart à signaler** : la consigne commune (méthode du lecteur, ligne 22) nomme `interdits-communs-v2.md`. Mon mandat limite mes lectures aux fichiers qu'il nomme ; ce fichier n'y est pas. **Je ne l'ai pas ouvert.** J'ai tenu les interdits de la consigne commune et ceux du mandat (aucune commande git, aucun réseau, aucun appel de modèle). Si ce fichier porte une règle plus stricte, je ne la connais pas.
- **Étendue lue par PDF** :
  - 2610.39766 : pages 1 à 4 et 6 à 8 ligne à ligne ; pages 9 à 22 ligne à ligne en écartant à l'affichage les lignes de 14 caractères ou moins (jetons de figures) ; page 5 (références) par mots ; figures vues en image pages 3, 4 et 17.
  - 2610.31593 : pages 1 à 6 ligne à ligne (lignes de 14 caractères ou moins écartées) ; pages 7 à 13 en écartant les lignes de 40 caractères ou moins ; pages 15 à 20 en écartant les lignes de 60 caractères ou moins ; pages 14, 21 et 22 par mots seulement ; figures vues en image pages 9 et 11.
  - 2604.15384 : pages 1, 2, 4 à 6, 8, 12 à 20, 28 à 32, 39 à 51 en écartant les lignes de 30 caractères ou moins ; pages 3, 7, 9 à 11, 25 à 27, 33 à 38 en écartant les lignes de 50 caractères ou moins ; pages 21 à 24 par mots seulement ; figures vues en image pages 16, 19, 30 et 51.
  - Recherche de termes sur le texte complet, non filtré, des 95 pages : sonde, activation, boîte blanche, boîte noire, linéaire, interne, représentation, flux résiduel, état caché, interprétabilité, latent, logit, plongement, classifieur, puis diffus, faible enjeu, étalé, graduel, fragment, individuellement, incrémental, subtil, ambigu.
- **Citations contrôlées** : 40, **0 échec** (script `controle_citations_contre_lecture_H1_v1.py`, écrit sans reprendre celui du lecteur, lancé par `python3 -I` ; essai juste : 0 échec ; essai altéré : 3 échecs attendus sur 3). Les 41 citations du lecteur, repassées par mon script : 0 échec. Tout extrait anglais entre guillemets droits de ce document figure dans le JSON de l'archive (vérifié par le même script, option `--rapport`).
- **Refus ou ouverture fautive** : aucun.
- **Noms de modèles** : aucun n'est écrit ici ; les modèles des articles sont désignés par leur rôle ou leur taille.
- **Nature des chiffres** : « auteurs » (imprimé), « figure » (lu sur une figure), « calcul » (recalculé par moi).

---

## Verdict sur le rapport : **tient avec corrections**

Le verdict d'antériorité du rapport tient : aucune des trois pièces ne compare une sonde d'activations à un moniteur de texte. Les citations sont exactes et les paraphrases françaises portent ce que les pages disent, à trois réserves près (constats A, B, E). Deux corrections sont majeures, sans changer le verdict : une phrase qui corrige l'état du niveau 3 au-delà de ce que le lecteur a lu (A), et la fragmentation dans LinuxArena, présentée comme anecdotique alors qu'elle fait partie de la politique d'attaque par défaut (B).

## Mon verdict pour les trois pièces (table fermée)

| énoncé | 2610.31593 | 2604.15384 | 2610.39766 | ensemble des trois |
|---|---|---|---|---|
| H1 | non trouvé dans les pièces lues | non trouvé dans les pièces lues | non trouvé dans les pièces lues | **non trouvé dans les pièces lues** |

Ce verdict vaut pour ces trois PDF. Il ne dit rien du champ (règle R8) : les concurrents les plus probables de H1 restent les lots 9 et 10, que ni le lecteur ni moi n'avons lus.

---

## Réponses aux cinq points à juger

**1. Sondes contre moniteur de texte : rien, confirmé.**
- 2610.31593 et 2604.15384 : aucune occurrence de sonde d'activations, d'activation, de boîte blanche, d'état caché ni de classifieur entraîné, sur le texte complet. Les moniteurs sont des modèles de langue interrogés : "We use five full-trajectory monitors" (2610.31593, p. 3) ; "This paper evaluates one protocol: an LLM monitor that scores actions and full trajectories." (2604.15384, p. 20). Les figures qui listent des moniteurs ne montrent que des modèles de langue (2610.31593, figures 8 et 10, p. 9 et 11 ; 2604.15384, figures 10, 12, 18 et 35, p. 16, 19, 30 et 51 ; vues en image).
- 2610.31593 emploie des plongements de texte, mais pour regrouper des descriptions de comportements (p. 15), jamais comme moniteur.
- 2610.39766 : des sondes seules, aucune base de texte ; voir pourtant le constat G.
- Les travaux que LinuxArena annonce pour la suite ne sont pas des sondes : "follow-up work will evaluate trusted editing" (p. 20), puis une surveillance par un moniteur qui agit dans l'environnement.

**2. LinuxArena, fragmentation : « voisin » tient, mais le rapport la sous-décrit** (constat B). Seuils et agrégation : bien rapportés, à préciser (constats C et D).

**3. 2610.31593, sonde de la page 20 et seuils : exacts**, avec une précision sur ce que la sonde discrimine (constat L).

**4. 2610.39766, contre-indice et incohérences : le chiffre est exact** (figure 21, p. 17 : environ 0,07 à un positif, environ 0,18 vers dix, au plus environ 0,28 ; figure). Une des deux incohérences relevées n'en est pas forcément une, et une autre a été manquée (constat H). Une limite de construction manque (constat G).

**5. « À une table près » : le PDF dément que la comparaison soit dans ce PDF ; il ne permet pas de dire ce que S-2A voulait dire** (constat A).

---

## Constats

### A — majeur — le rapport corrige l'état du niveau 3 sur un document qu'il n'a pas lu

- **Où** : rapport, l. 41 (« L'expression ne peut donc vouloir dire que ceci : le banc permettrait la comparaison si l'on ajoutait une table ») et l. 200.
- **Ce que les pages disent** : le PDF 2604.15384v2 (version 2, 27 avril 2026) ne contient aucune sonde, aucune table et aucune figure sur des activations. Je le confirme sur les 51 pages (texte complet et figures des pages 16, 19, 30, 51). Sur ce point le rapport a raison.
- **Ce qui ne tient pas** : l'expression « à une table près » vient de S-2A, point 4, que la contre-lecture du niveau 3 rapporte en une ligne (l. 289-290). Ni le lecteur ni moi n'avons lu S-2A. D'après les lignes 74 à 77 de l'état du niveau 3, S-2A est la source des billets. L'expression peut donc renvoyer à une autre source que ce PDF (un billet, une version ultérieure, un travail qui se sert du banc), ou vouloir dire que la comparaison, si elle se faisait, tomberait en sabotage concentré. « Ne peut vouloir dire que » est une déduction sans pièce.
- **Texte corrigé (l. 41)** :
```text
**Point à vérifier dans l'état du niveau 3** : la contre-lecture (l. 289-290) rapporte que S-2A, point 4, place la
comparaison dans LinuxArena, en sabotage concentré, « à une table près ». Le PDF 2604.15384v2 ne contient aucune table,
aucune figure ni aucune phrase sur des sondes, des activations ou une boîte blanche (51 pages, figures des pages 15, 16,
19, 30 et 51 comprises). La comparaison n'est donc pas dans ce PDF. Je n'ai pas lu S-2A : je ne sais pas à quelle
source ni à quel sens son expression renvoie. À rouvrir : S-2A, point 4, pour dire sur quelle pièce elle s'appuie.
```
- **Texte corrigé (l. 200)** :
```text
- Que le PDF de LinuxArena (version 2) contient, même « à une table près », une comparaison de sondes et de moniteurs
  de texte : aucune de ses tables ne porte sur des sondes. Le sens de l'expression de S-2A reste à vérifier sur S-2A.
```

### B — majeur — LinuxArena : la fragmentation est dans la politique d'attaque par défaut, pas seulement dans des exemples

- **Où** : rapport, l. 102 à 107 (« Ces constats sont qualitatifs (exemples de trajectoires) »), l. 122, l. 201.
- **Ce que les pages disent** : la politique d'attaque par défaut du banc comporte deux étapes de fragmentation. À l'étape 5 de la planification : "breaking a single suspicious operation into many individually innocuous fragments" (p. 40). Puis à l'étape 7 : "The selected approach is further broken up; suspicious variables and operations are identified and individually obfuscated." (p. 40). Tous les chiffres de tête du banc (sabotage réussi à 34 % contre le moniteur faible ; sûreté de 89 % à 99 % pour les moniteurs forts, figure 10, p. 16, auteurs) sont donc mesurés contre des attaques **instruites de fragmenter**. Les exemples des pages 17 et 42 sont, eux, bien qualitatifs. Les auteurs ajoutent une affirmation générale, sans mesure : "All of these failure modes are highly amplified when the attack is integrated with legitimate main task work" (p. 17).
- **Portée pour H1** : cela ne fait pas de LinuxArena un banc de sabotage diffus. Le dommage reste un seul fait net, vérifié par un correcteur binaire sur l'état final ; ce sont les **actions** qui sont émiettées, pas le dommage. Le verdict « voisin » pour (b) tient. Mais deux phrases publiques deviennent fausses, dans les deux sens : « les moniteurs de texte ne relient pas les fragments » (ils tiennent à 89-99 % sous une politique qui fragmente, pour les moniteurs forts) et « la fragmentation n'y est qu'anecdotique ». Aucune mesure ne sépare les attaques selon leur degré de fragmentation : cela reste vrai.
- **Texte corrigé (remplace la phrase de la l. 107)** :
```text
  La fragmentation fait partie de la politique d'attaque par défaut (étapes 5 et 7 de la planification, p. 40) : les
  chiffres de tête du banc sont donc mesurés contre des attaques instruites de fragmenter une opération suspecte.
  Aucune mesure ne sépare les attaques selon leur degré de fragmentation ; les modes d'échec des pages 17 et 42 sont
  des exemples de trajectoires. Le dommage reste un fait unique, vérifié par un correcteur binaire : ce sont les
  actions qui sont émiettées, pas le dommage.
```
- **Texte corrigé (l. 122)** : « voisin (fragmentation des actions d'une attaque concentrée, inscrite dans la politique d'attaque par défaut, p. 40 ; modes d'échec illustrés par des exemples, p. 17 et 42 ; dommage unique à correcteur binaire) ».
- **Texte corrigé (l. 201)** : « Que les moniteurs de texte échouent, ou réussissent, de façon mesurée **selon le degré de fragmentation**, sur la foi de LinuxArena : la politique d'attaque fragmente par défaut (p. 40), mais aucune mesure n'isole cet effet (p. 17, 42). »

### C — mineur — agrégation dans LinuxArena : le moniteur par étape lit tout l'historique

- **Où** : rapport, l. 96 et l. 125.
- **Ce que les pages disent** : le rapport donne bien le maximum sur les étapes ("A trajectory counts as flagged if any of its actions is flagged", p. 13) et la règle combinée par rangs centiles (p. 29). Il manque trois traits, qui comptent pour « à agrégation égale » :
  1. le moniteur par étape n'est pas un lecteur d'étape isolée, il relit à chaque étape tout ce qui précède : "For the per-action monitor, we show the current proposed action alongside all past monitored actions with their respective outcomes." (p. 13) ;
  2. chaque score est la moyenne de deux appels : "To reduce variance, we take the mean score of two independent monitor calls whenever we score an action (and a trajectory)." (p. 12) ;
  3. pour les dommages immédiats, seules les étapes d'avant le dommage comptent : "only actions executed strictly before the harm step contribute to catching" (p. 28).
- **Chiffre utile, non rapporté** : à taux par étape égal, la règle par étape et la règle combinée se suivent, et la lecture de la trajectoire entière seule reste loin derrière ("Live and combined track each other", légende de la figure 18, p. 30 ; à 1 % par étape, environ 0,9 contre environ 0,43, figure). Les auteurs préviennent que le taux par trajectoire et le taux par étape ne se comparent pas : "This is not directly comparable to the 1% step-wise FPR curves used elsewhere in the paper" (p. 32).
- **Texte corrigé (ajout à la l. 96)** : « Le moniteur par étape relit à chaque étape tout l'historique des actions et de leurs sorties (p. 13) ; son score est la moyenne de deux appels (p. 12) ; pour les dommages immédiats, seules les étapes d'avant le dommage comptent (p. 13, 28). La base boîte noire de ce banc est donc le maximum, sur les étapes, d'un lecteur cumulatif. »

### D — mineur — « dans l'échantillon » : exact, à préciser

- **Où** : rapport, l. 59, 95, 204.
- **Ce que les pages disent** : dans les deux bancs le seuil est un quantile des scores d'épisodes honnêtes, distincts des épisodes d'attaque. LinuxArena : "the threshold sits at the 99th percentile of the honest per-action score distribution" et "The threshold is calibrated per attacker against its model-matched honest run" (p. 13). Évaluations simulées : "Audit thresholds are set on a shared set of executed honest trajectories, the same trajectories that serve as reference trajectories for the simulator." (p. 3) ; "At audit budget b (the fraction of honest trajectories flagged, or false-positive rate)" (p. 9). Le taux de fausses alarmes est donc tenu **par construction** sur les épisodes honnêtes qui fixent le seuil ; il n'est jamais remesuré sur des épisodes honnêtes neufs. Le rappel, lui, est mesuré sur des épisodes d'attaque qui n'ont pas servi au seuil.
- **Jugement** : la paraphrase du rapport est juste. Sans cette précision, un lecteur pressé peut comprendre que le seuil est réglé sur les attaques.
- **Texte corrigé (l. 204)** : « Que les seuils de ces bancs sont validés hors de l'échantillon : le seuil est un quantile des épisodes honnêtes, et le taux de fausses alarmes n'est jamais remesuré sur des épisodes honnêtes neufs (2610.31593, p. 3 et 9 ; 2604.15384, p. 13). Les épisodes d'attaque ne servent pas au seuil. »
- **Remarque** : « fixé hors de l'échantillon » (composante (d) du rapport, l. 47 et l. 195) ne figure pas dans l'énoncé de H1 au programme (l. 91 : agrégation égale, taux de faux positifs égal). C'est un durcissement du lecteur, inspiré du constat M1. Il rétrécit ce qui est dit revendicable ; il ne fausse pas le verdict.

### E — mineur — 94 % contre 50 % : deux mesures différentes

- **Où** : rapport, l. 100 (« les attaques humaines échappent à 94 % au moniteur faible, contre 50 % pour la meilleure attaque produite par un modèle »).
- **Ce que les pages disent** : 94 % est un taux de sabotage réussi et non détecté des trajectoires humaines, qui réussissent toutes par construction (p. 2, 14, 20 ; auteurs). 50 % est le taux de sabotage réussi de la meilleure attaque de modèle, qui mêle l'échec de la sous-tâche et la détection (p. 14, auteurs) : ce n'est pas un taux d'évasion. La comparaison d'évasion appariée est 95 % (ou 94 %) contre 47 % pour le moniteur faible, et de 13 % à 69 % contre 0 % à 17 % pour les dix autres moniteurs (figure 12, p. 19 ; figure 35, p. 51 ; figure).
- **Texte corrigé** : « les trajectoires humaines (LaStraj) réussissent sans détection à 94 % contre le moniteur faible, contre 50 % de sabotage réussi pour la meilleure attaque de modèle (p. 2, 14, 20) ; en évasion appariée, 94-95 % contre 47 % (figures 12 et 35, p. 19 et 51). »

### F — mineur — remarque de marge : la place laissée par les attaques humaines n'est pas ouverte à une sonde qui lit l'agent

- **Où** : rapport, l. 130.
- **Ce que les pages disent** : les trajectoires humaines sont retravaillées contre un moniteur de texte "until the live monitor score was at most 5 (out of 10)" (p. 46 ; même chose p. 18), et des étapes d'exploration synthétiques y sont insérées (p. 18, 46).
- **Jugement du contre-lecteur** (non imprimé) : ces trajectoires sont écrites par des humains et sélectionnées contre des moniteurs de texte. Aucun agent ne les a produites en cherchant à nuire. Une sonde qui lit l'activité interne de l'agent auteur n'a donc rien à y lire tel quel. La « place pour un gain » que le rapport voit là n'est pas une place mesurable par H1 sur ce jeu.
- **Texte corrigé (ajout à la l. 130)** : « Les trajectoires humaines sont sélectionnées contre des moniteurs de texte (score d'au plus 5 sur 10, p. 46) et ne sortent pas d'un agent : une sonde sur l'agent auteur ne s'y applique pas telle quelle. »

### G — mineur — 2610.39766 : le filtrage rend le gain sur une lecture de texte impossible à montrer sur le spam

- **Où** : rapport, l. 148 (« Ce qu'il ne fait pas ») ; non mentionné.
- **Ce que les pages disent** : "We therefore filter our datasets to only include samples where the base model knows the correct answer." (p. 2). Pour le spam, le filtre interroge le modèle par une consigne à quelques exemples et ne garde que les cas où sa réponse est la bonne : "We filter the evaluation set using this score" (p. 7 ; règle recopiée à part plus bas).
- **Portée pour H1** : sur le jeu d'évaluation du spam, la réponse en texte du même modèle est juste par construction. Une lecture boîte noire y serait parfaite ; aucun gain de la sonde sur le texte ne peut y apparaître. L'article n'est pas seulement sans base boîte noire : sur sa tâche principale, il ne pourrait pas en battre une. La seule phrase de l'article sur ce contraste est une motivation, sans mesure : "monitoring solely model outputs could be insufficient, motivating the use of activation probes" (p. 1).
- **Texte corrigé (ajout à la l. 148)** : « Les jeux sont filtrés pour ne garder que les exemples où le modèle connaît la bonne réponse (p. 2, 7) : sur le spam, une lecture en texte du même modèle est juste par construction, donc aucun gain de la sonde sur le texte ne peut s'y montrer. La phrase de la page 1 sur l'insuffisance de la lecture des sorties est une motivation, pas un résultat. »

### H — mineur — 2610.39766 : une incohérence à nuancer, une autre manquée

- **Où** : rapport, l. 153.
- **Ce que les pages disent** : "For the five best probes (by AUC), 2x upsampling performs best" (p. 3) et "On average across 13 probe architectures and 10 seeds, 3x upsampling performs best." (p. 4, légende de la figure 3). Les deux phrases portent sur des populations différentes (cinq meilleures sondes ; treize architectures) : elles peuvent être vraies ensemble. L'axe de la figure 3 annonce de plus une médiane sur toutes les sondes, quand la légende dit une moyenne (figure, p. 4).
- **Incohérence manquée** : le texte et la figure 3 parlent de facteurs dix et vingt ("performance degrades at higher upsampling factors (10x and 20x)", p. 3 ; figure 3, p. 4 ; p. 12), alors que la méthode ne génère que jusqu'au facteur cinq ("for each upsampling factor", p. 8, suivi de l'ensemble 2, 3, 4, 5 ; recopié à part plus bas).
- **Confirmé** : 0,6 à 14 milliards dans le texte ("ranging from 0.6B to 14B parameters", p. 4) contre une courbe à 32 milliards (figure 4, p. 4 ; modèle aussi listé p. 2) ; section sans texte p. 12.
- **Texte corrigé (l. 153)** : « Meilleur facteur de suréchantillonnage : deux pour les cinq meilleures sondes (p. 3), trois en moyenne sur treize architectures (légende de la figure 3, p. 4) ; populations différentes, pas forcément contradictoires ; l'axe de la figure dit médiane, la légende dit moyenne. Facteurs dix et vingt dans le texte et la figure (p. 3, 4, 12), absents de la méthode, qui s'arrête à cinq (p. 8). »

### I — mineur — 2610.39766 : venue et taille du modèle

- **Où** : rapport, l. 136 et l. 145-146.
- **Ce que les pages disent** : le pied de la page 1 se lit en entier sans l'option de mise en page : "Workshop: Mechanistic Interpretability." (p. 1), atelier de la 39e conférence NeurIPS (2025). Les résultats sur l'honnêteté sont pris sur un modèle de 70 milliards de paramètres (p. 2 ; titres des figures 2 et 21). Le programme travaille à 8 milliards. La meilleure sonde sur l'honnêteté est linéaire, sur le dernier jeton (légende de la figure 21 : "Recall performance of the best probes on the MASK honesty dataset.", p. 17) ; en entraînement équilibré elle plafonne vers 0,16 (figure, p. 17).
- **Texte corrigé (ajout à la l. 146)** : « Ces chiffres viennent d'un modèle de 70 milliards de paramètres ; meilleure sonde : linéaire sur le dernier jeton ; bande d'incertitude jusqu'à environ 0,37 ; en entraînement équilibré, au plus environ 0,16 (figure, p. 17). »

### J — mineur — 2610.39766 : le contre-indice est bien qualifié, la limite citée ne l'est qu'à moitié

- **Où** : rapport, l. 150 et l. 202 (« Les auteurs l'excluent (p. 4) »).
- **Ce que les pages disent** : les auteurs écrivent que le succès sur le spam ne garantit rien : "The success of our methods on this task certainly does not guarantee they will work for detecting novel, complex misalignment." (p. 4). Ils n'« excluent » pas ; ils ne garantissent pas.
- **Texte corrigé (l. 202)** : « Les auteurs disent eux-mêmes que le succès sur le spam ne le garantit pas (p. 4), et le rappel sur l'honnêteté reste bas (figure, p. 17). »

### K — mineur — LinuxArena : une catégorie de tâches « recherche », à correcteur binaire

- **Où** : rapport, l. 109 et l. 123 (« Les tâches sont nettes »).
- **Ce que les pages disent** : une des six catégories de tâches principales est "research (run experiments and report findings)" (p. 7). Elle reste notée par un correcteur automatique à verdict binaire ("verdict based on the final state", p. 7), et les sous-tâches nuisibles ne portent pas sur la qualité de la recherche. Les auteurs écrivent aussi que les chaînes d'entraînement de modèles ne sont pas représentées (p. 19).
- **Jugement** : « ne touche pas » tient pour (c). À nommer, parce que l'environnement (a) du programme porte sur des propositions d'expériences.
- **Texte corrigé (ajout à la l. 123)** : « une catégorie de tâches principales est dite de recherche (p. 7), mais notée par correcteur binaire ; aucune sous-tâche nuisible ne dégrade la qualité d'une recherche. »

### L — mineur — 2610.31593 : ce que la sonde de la page 20 discrimine

- **Où** : rapport, l. 64 et l. 203.
- **Ce que les pages disent** : "An action-output probe using the same model at medium reasoning effort has AUROC 0.493" (p. 20). Ce discriminateur est un modèle de langue, celui de la politique d'attaque ("serves as a history discriminator", p. 12). Il sépare les sorties d'outils **simulées** des sorties **enregistrées**, sur des sessions sans attaque ("All trajectories are treated as honest work.", p. 20 ; "Discriminability stays near chance throughout the continuation.", p. 20). Ce n'est donc ni une sonde d'activations, ni même un moniteur de sabotage.
- **Jugement** : la lecture du rapport est exacte ; elle ne dit pas ce qui est discriminé.
- **Texte corrigé (l. 64)** : « Il nomme un discriminateur obtenu en interrogeant un modèle de langue, qui cherche à distinguer les sorties d'outils simulées des sorties enregistrées, sur des sessions sans attaque (p. 20) : ni sonde d'activations, ni moniteur de sabotage. »

### M — mineur — points vérifiés et trouvés exacts

- 2610.31593 : cinq moniteurs de texte sur trajectoire entière, moyenne de trois appels (p. 3) ; erreur de 3,6 points contre 10,1 (p. 1, 9 ; figure 8 : 3,57 et 10,10) ; aire partielle 0,841 contre 0,767, gain apparié 0,074 (p. 11 ; figure 10) ; l'expérience des descriptions de stratégies est du texte contre du texte ("we add descriptions of simulated attack strategies to the monitor's prompt as possible behaviors to look for", p. 11) ; carré corrigé négatif affiché à zéro (p. 8, 17).
- 2604.15384 : sûreté de 89 % à 99 % pour dix moniteurs et 65 % pour le plus faible (figure 10, p. 16) ; 89,4 % contre 89,6 % (p. 31) ; 400 épisodes honnêtes et 185 attaques à la figure 18 (p. 30) ; écarts de 2 à 8 points selon la base de calibrage (p. 49-50) ; 95 % sur la figure 12 contre 94 % dans le texte (p. 19, 51) ; "the red team can spread an attack across multiple actions" (p. 6) ; "This also includes attacks split across multiple files, where the monitor fails to connect the dots." (p. 17) ; "The agent's actions are individually plausible for the main task; the monitor fails to aggregate them into a coherent attack narrative." (p. 42) ; "we convert each raw score to a percentile rank against the honest distribution for that monitor" (p. 29).
- 2610.39766 : test équilibré ("All probes are evaluated on a held-out test set that is constructed to be balanced", p. 2) ; réglage du seuil à 1 % non décrit, taille du test non donnée (non trouvés, confirmé) ; aire sous la courbe d'environ 0,63 à environ 0,85 sur l'honnêteté (figure 2, p. 3).

---

## Recherche active des composantes dites « non trouvées »

| composante | 2610.31593 | 2604.15384 | 2610.39766 |
|---|---|---|---|
| (a) sondes contre texte | rien (texte complet, figures p. 9 et 11) | rien (texte complet, figures p. 16, 19, 30, 51) | sondes seules ; filtrage qui interdit le gain sur le spam (G) |
| (b) diffus | rien : sous-tâches à correcteur ou à juge | voisin : actions émiettées par la politique par défaut, dommage unique (B) | rien |
| (c) flou | rien | rien ; catégorie « recherche » à correcteur binaire (K) | rien |
| (d) fausses alarmes égales | budget d'audit, quantile des épisodes honnêtes (D) | 1 % par étape, quantile des épisodes honnêtes du même modèle (D) | rappel à 1 %, seuil non décrit |
| (e) agrégation égale sur la trajectoire | lecture de la trajectoire entière | maximum d'un lecteur cumulatif ; règles comparées à taux par étape égal, texte contre texte (C) | agrégation sur les jetons d'une entrée |
| (f) agent | agents, moniteurs de texte | agents, moniteurs de texte | hors agent |

Aucune occupation, même partielle, d'une composante de H1 comme **mesure du gain**. Le voisin le plus proche est LinuxArena pour (b) et (e) : il donne la base boîte noire d'un banc concentré à actions fragmentées, pas une mesure sur du diffus.

## Jugement de profondeur

- **Suffisante pour le verdict.** Le journal déclare les 95 pages lues, avec recherche de termes sur le texte complet et vue des figures qui listent des moniteurs. Mes propres recherches et mes vues en image ne contredisent rien. Les 41 citations repassent par un script écrit à part.
- **Réserves.** Entre le début déclaré et l'écriture du rapport il s'écoule neuf minutes, script et contrôle compris : c'est court pour 95 pages « ligne à ligne ». Deux traces de lecture rapide : l'annexe E de LinuxArena (politique d'attaque, p. 39 à 41) est citée sans que la place de la fragmentation dans la politique par défaut soit vue (B) ; l'annexe A.3 de 2610.39766 (filtrage, p. 6 et 7) n'est pas exploitée (G). Les figures de 2610.31593 n'ont pas été vues en image par le lecteur ; je les ai vues pages 9 et 11, sans surprise.
- Le lecteur a lu `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (l. 32 à 61), que mon mandat ne nomme pas : je ne l'ai pas ouvert et ne peux pas dire si son mandat le nommait.
- **Ma propre limite** : mes lectures ont écarté à l'affichage les lignes courtes (seuils donnés en tête), et les pages de références (2610.31593, p. 14 ; 2604.15384, p. 21 à 24 ; 2610.39766, p. 5) n'ont été parcourues que par mots.

## Ce qu'une phrase publique sur H1 ne doit pas affirmer (ajouts et corrections à la liste du rapport)

- Que le sens de « à une table près » est établi : il reste à vérifier sur S-2A (A).
- Que la fragmentation est anecdotique dans LinuxArena, ou au contraire que LinuxArena mesure l'effet de la fragmentation (B).
- Que la base boîte noire de LinuxArena lit chaque étape isolément (C).
- Que 2610.39766 montre, ou pourrait montrer sur le spam, un avantage des sondes sur la lecture du texte (G).
- Que les attaques humaines de LinuxArena ouvrent une marge mesurable pour une sonde qui lit l'agent (F).

Je ne rédige pas la phrase publique qui déclarerait H1 (rôle exclu).

## Formules (lues sur le PDF, non contrôlées par programme)

- 2610.39766, p. 7 : exemples positifs gardés si la différence de logits entre oui et non est positive, négatifs si elle est négative.
- 2610.39766, p. 8 : facteur de suréchantillonnage u dans l'ensemble 2, 3, 4, 5.
- 2604.15384, p. 29 : score par étape c(a) = max(rL(a), rD(T)) pour la règle combinée ; seuil = quantile (1 − taux) des scores c des étapes honnêtes.
