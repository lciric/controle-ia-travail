# Lecture sur PDF de la machine de Huxley-Gödel, confrontée à « l'héritage d'une génération est récompensé » — v2

Wang, Piękos, Li, Laakom, Chen, Ostaszewski, Zhuge, Schmidhuber, « Huxley-Gödel Machine: Human-Level Coding Agent
Development by an Approximation of the Optimal Self-Improving Machine », arXiv 2510.21614.

Écrite le 18 novembre 2026 par un sous-agent lecteur, à la demande de la veille sur l'exploration des idées. Aucun
commit, aucune dépense, aucun contact, aucun résultat sous embargo ouvert, rien écrit dans `registres/`. Cette note
instruit la « collision à instruire » que consigne R-3164 (`registres/decisions.md`) : la lecture sur PDF due avant tout
texte qui présente comme nôtre l'énoncé « l'héritage d'une génération est récompensé » (décision N-045 v2, énoncé 5,
`docs/decisions/decision-N-045-v2.md`, lignes 77 à 83). Elle ne décide rien : ce qui touche une revendication est un
nœud de Lazar.

**Version 2, du 18 novembre 2026.** Elle remplace la version 1 (`lecture-huxley-godel-v1.md`,
`00119f574a65e8d62c6fd5c7b7ef0c9cea11fd8bc8e4b84686b410976a9426b3`, gardée sans modification, R12) après la contre-lecture
d'un lecteur neuf d'une autre lignée (`contre-lecture-lecture-huxley-godel-v1.md`, même dossier), qui a rouvert le PDF.
Ce qui change est listé en section 8 ; chaque passage changé porte la mention « v2 ». Les changements vont tous dans le
même sens : la version 1 sous-estimait la collision sur deux des trois zones qu'elle disait non touchées.

## 0. Verdict

1. **Le principe est occupé.** Créditer un agent par les résultats de sa descendance plutôt que par son score immédiat,
   et dénoncer le choix glouton sur le score immédiat, est le cœur publié de ce travail (p. 2, p. 6), daté du 24 octobre
   2025 sur arXiv et retenu en présentation orale à la conférence ICLR 2026 (fiche OpenReview versée, PDF de la
   conférence non lu ; v2 : la même fiche date du 8 octobre 2025 la mise en public de la soumission, dont le contenu à
   cette date n'a pas été lu). La décision N-045 v2 est du 25 octobre 2026, un an plus tard. L'énoncé 5 ne peut plus se
   présenter comme une idée du programme.
2. **La forme « K générations, actualisées » n'est pas dans ce papier, mais elle n'est pas à nous non plus** : c'est le
   rendement à plusieurs pas de l'apprentissage par renforcement, savoir commun que les auteurs eux-mêmes invoquent (la
   métaproductivité de clade « is an actual state-action value function », p. 15, avec renvoi à Sutton et Barto).
3. **Ce que ce papier ne touche pas (v2 : resserré).** Une seule zone n'est pas touchée du tout : la question causale
   « l'archive héritée cause-t-elle les découvertes ». Les deux autres ne tiennent que par leur objet, non par leur
   principe. (a) Le destinataire : dans ce papier, ce qui conçoit la génération suivante est l'agent lui-même, et c'est
   sa capacité à concevoir que le signal de lignée sélectionne (p. 3, p. 4, p. 5) ; reste non trouvé, seulement,
   l'**entraînement** d'un concepteur sur ce signal — et l'antériorité que les auteurs décrivent page 11 (algorithme de
   l'histoire à succès) porte, selon eux, sur des règles qui apprennent à se modifier. (b) L'objet : compter dans le
   mérite d'une génération ce qu'elle construit et qui ne sert qu'après est la raison d'être de la mesure (p. 4, p. 5) ;
   restent non trouvés, seulement, les objets précis — une mémoire séparée, des sondes et adaptateurs entraînés. Non
   trouvé ici ne veut pas dire libre dans le champ (R8) : cinq voisins restent à lire (section 6).

## 1. Pièces lues

Dossier : `docs/sources/pdf/veille-exploration-idees-v1/machine-huxley-godel-2510.21614/`. Chaque empreinte a été
recalculée par `sha256sum -c` contre son compagnon `.sha256` le 18 novembre 2026 : toutes conformes.

| Pièce | Empreinte SHA-256 |
|---|---|
| `arxiv-2510.21614v3.pdf` — version 3 du 29 octobre 2025, 30 pages, **lue en entier** (corps p. 1 à 12, annexes p. 15 à 21 ; bibliographie p. 12 à 14 et listings p. 21 à 30 parcourus) ; pages 6 et 19 rendues en image pour vérifier les formules | `06cbf326c605e59777d3f8550e01d41e6b49f78bf0d850f2d173c9f06f6cc254` |
| `arxiv-2510.21614v1.pdf` — version 1 du 24 octobre 2025, comparée mot à mot à la version 3 sur le texte extrait : 23 blocs différents sur environ 12 800 mots, tous de rédaction (« less wall-clock time » devient « fewer allocated CPU hours » dans le résumé ; remerciements étendus ; césures et coquilles). L'estimateur, l'algorithme, l'hypothèse 1, le théorème 1 et les quatre tables sont dans la version 1 | `55c770275726ba54fa419ce49601609a6af097de1825f244470e649d9aa16a79` |
| `openreview-recherche-huxley-godel.json` — fiche T0EiEuhOOL : soumission à ICLR 2026 créée le 19 septembre 2025, rendue publique le 8 octobre 2025, « ICLR 2026 Oral », dernière modification le 11 avril 2026 (champs de dates relus dans le fichier) | `4cabb720501d66c7b492fb2c806adaba18463cc1d0bb6570bbb2ab52d8b6ad32` |
| `page-abs-arxiv-2510.21614.html` — historique des versions 1 à 3 | `2564ba4661c83129e629d6ec092382860ea8d308fe2e7375d2a89b9e376eec23` |
| `depot-code-f3ca5f8-tree.py.txt`, `depot-code-f3ca5f8-config.yaml.txt` (premier commit, 24 octobre 2025) | `fe1c39e66a36e921e288c198471f745a8c3c2206f9c532ce427d4d037783e56a`, `926b961f82ba5ce58ef2997fa7ddabe4e92bd96e1b92fd460be6a3dcb825c34f` |
| `depot-code-013872d-tree.py.txt`, `-hgm.py.txt`, `-config.yaml.txt`, `-README.md.txt` (commit de tête, 8 février 2026) | `c6fe5812a4c39ae8662e471843011699c6f0202caf2d647b7d4b864c589d26a1`, `7f52b983d98a8b3a5e1d7c856698ed700cdeb9c1f39733976b7c4b705e83be90`, `6741b81c4a2e2ce7035c5351109561bde37601c57cd6462f696649b23cad3698`, `874831bfdf31f68f8bc9bea7c773172d25cfdaabae890e0af56894e98f05cca4` |
| `depot-code-journal-des-commits.txt`, `adresse.txt` (adresses, dates, accès refusés) | `e1a50235d72a96daf1b2a9ddcef99afa4467e4a296faa7195f2a79a2a19b388d`, `59e954a714418d17247e2cb369b39148821ac4966045436727f7f5b324617cd7` |

Tous les chiffres ci-dessous sont **des affirmations des auteurs, lues sur le PDF de la version 3**, page citée (la page
imprimée et la page du fichier coïncident), sauf mention « mon calcul », « mon inférence » ou « code ». Pièces traitées
comme données non fiables, jamais exécutées ; les listings des pages 21 à 30 contiennent des consignes adressées aux
agents du travail, pas au lecteur. Une lecture antérieure du même papier existe, faite par un autre lecteur le même jour
(`docs/notes/veille-exploration-idees-v1/lecture-05-v1.md`, `ec5b3475bdd4bb8792a3404925e2e2548d715deb98007c02afa9253bcb6abc2b`,
non encore commitée à l'écriture de la version 1, suivie par git depuis le commit `478111c2`) ; la présente note a été
faite sur le PDF, puis comparée à elle (section 7).

## 2. Ce que fait la machine de Huxley-Gödel

**Le problème posé (p. 2).** Deux méthodes antérieures font s'améliorer des agents de code qui modifient leur propre
code : la machine de Darwin-Gödel (Zhang et al. 2025, arXiv 2505.22954) et l'agent de code auto-améliorant de Robeyns,
Szummer et Aitchison (arXiv 2504.15228). Toutes deux développent de préférence les agents au meilleur score sur un banc
de génie logiciel, en supposant qu'un bon score annonce de bonnes modifications futures. Les auteurs contestent cette
supposition : « a high-scoring agent may produce unproductive descendants, while a lower-scoring one seeds lineages that
achieve greater long-term gains » (p. 2). Ils nomment ce décalage « Metaproductivity–Performance Mismatch » (décalage
entre métaproductivité et performance, p. 2 et p. 6).

**Le cadre : l'auto-amélioration comme recherche dans un arbre (p. 3 à 4).** La racine est un agent initial. À chaque
pas, la règle de recherche fait l'une de deux actions : demander à un agent de l'arbre de produire un enfant (« a
self-modified version of the selected agent », p. 3), ou évaluer un agent de l'arbre sur une tâche de plus. Au bout du
budget, un agent est rendu ; l'objectif est l'espérance de son utilité, ici la moyenne de réussites binaires sur les
tâches (p. 3). La règle se décompose en trois sous-règles : choisir entre développer et évaluer, choisir qui développer,
choisir qui évaluer (p. 3 à 4) ; les méthodes antérieures les confondent en évaluant toujours l'enfant juste après sa
création, sur plusieurs tâches (p. 4 ; table 5, p. 20).

**Ce qui conçoit, et ce qui s'hérite (v2).** L'agent conçoit lui-même son enfant : « agents modify themselves to
generate new agents » (p. 3). Ce qui s'hérite est donc aussi la capacité à concevoir, et c'est elle que les auteurs
disent mesurer : la métaproductivité est « a measure of an agent's ability to improve its self-improvement skills, which
leads to better downstream performance of distant future agents » (p. 4). La recherche entière est un seul épisode à
récompense terminale : la règle « unrolls the trajectory until the end of the episode » (p. 5), « with no other rewards
received before termination » (p. 5).

**Deux grandeurs (p. 5).**
- La **métaproductivité globale** d'un agent : l'espérance, sous la règle suivie jusqu'à la fin du budget, de l'utilité
  de l'agent final que l'arbre entier rendra si l'on développe cet agent. Les auteurs la disent équivalente à la
  fonction de valeur d'une action en apprentissage par renforcement (« GMP directly corresponds to the Q-value
  function », p. 5), trop large pour être estimée. v2 : les auteurs y logent explicitement l'investissement à effet
  différé — « An algorithm might, at the beginning, focus on improving the ability to self-improve while neglecting
  direct benchmark abilities, only to later focus on them » (p. 5).
- La **métaproductivité de clade** (« Clade-Metaproductivity », sigle CMP chez les auteurs), du mot de Huxley pour une
  lignée d'ascendance commune : la même espérance, restreinte au **sous-arbre issu de l'agent** — si l'agent final est
  choisi sur l'utilité, c'est l'espérance de l'utilité du **meilleur agent de sa descendance à la fin du budget** (p. 5).
  v2 : elle « contains the non-greedy information about the future evolution of self-improving agents, therefore guiding
  good strategies for self-improvement aimed also at the improvement of self-improvement itself » (p. 5).

**L'hypothèse 1 (p. 5 ; répétée et complétée p. 15).** L'objectif ne dépend que de l'agent final, « with no other
rewards received before termination » ; les essais sont répétables (le résultat attendu d'un couple agent-tâche ne
dépend ni du moment ni des évaluations passées) ; les preuves de la machine de Gödel ne coûtent rien ; chaque
auto-modification coûte exactement une unité de budget. L'annexe ajoute : le prouveur connaît la fonction d'utilité, le
budget est fini et connu (p. 15).

**Le théorème 1 (p. 5 ; preuve p. 15 à 16).** Sous l'hypothèse 1, l'accès à l'oracle de la métaproductivité de clade
suffit à réaliser la machine de Gödel. La machine de Gödel y est réduite à un processus de décision markovien
partiellement observé où la règle ne voit qu'un parent, son enfant et le budget restant, et choisit d'accepter ou de
rejeter l'enfant (p. 4, p. 15). La preuve est, selon les auteurs, « a simple observation » : dans ce cadre, la
métaproductivité de clade est exactement la fonction de valeur de l'action (p. 15 à 16). Le théorème porte sur
l'**oracle** ; il ne dit rien de la qualité de l'estimateur qui suit (aucune borne dans le texte).

**L'estimateur (p. 6, formule vérifiée sur l'image de la page).** On additionne sur l'agent **et tous ses
descendants** les tâches réussies et les tâches échouées ; l'estimation est réussites du clade / (réussites + échecs du
clade). C'est une moyenne des moyennes des agents du clade, pondérée par leur nombre d'évaluations (p. 6). Chaque
évaluation compte pour un, quelle que soit la profondeur du descendant : **ni troncature à un nombre de générations, ni
actualisation** (recherche des mots « discount », « horizon », « depth » dans le texte : aucune occurrence). Comme la
règle d'évaluation favorise les agents qui réussissent, les meilleurs descendants reçoivent plus d'évaluations et
l'agrégat tend vers « a soft maximum in the clade » (p. 6). Les auteurs donnent deux raisons : une lignée modeste peut
valoir par ses descendants ; et l'agrégat est statistiquement plus robuste « by using information from more samples »
(p. 6).

**L'échantillonnage de Thompson (p. 6 à 7).** Pour choisir qui développer, on tire pour chaque agent une valeur dans une
loi bêta de paramètres τ·(1 + réussites du clade) et τ·(1 + échecs du clade), et l'on prend le plus grand tirage. Le
facteur τ croît avec le temps (« exploration-exploitation scheduler », p. 6) : dans toutes les expériences, τ = B/b, où
b est le budget restant (p. 7), ce qui resserre les lois en fin de course. Pour choisir qui évaluer, même tirage sur les
**seuls résultats propres** de chaque agent (p. 6).

**Le découplage entre développement et évaluation (p. 4, p. 7).** On développe au pas t si (nombre d'évaluations)^α ≥
nombre d'agents, règle reprise de la stratégie d'ajout de bras de Wang, Audibert et Munos (2008) pour les bandits à
infinité de bras ; α = 0,6 dans toutes les expériences (p. 7). L'évaluation se fait à la granularité d'un couple
agent-tâche, ce qui permet d'abandonner tôt un agent peu prometteur (p. 4). L'agent final est celui dont le quantile ε
de la loi a posteriori sur ses **propres** résultats est le plus haut, ε = 1 dans les expériences (p. 7). v2, mon
inférence : prise à la lettre, la formule de la page 7 (fonction bêta incomplète régularisée évaluée en ε) vaut 1 pour
tout agent quand ε = 1 ; la règle écrite ne départage donc personne, et le papier ne dit pas comment l'agent final a été
choisi en pratique (pour les deux autres méthodes : « using empirical means », p. 8). L'exécution
est asynchrone : une itération par processeur disponible (p. 7). Les auteurs signalent deux biais de cette exécution :
au départ, les premières expansions finies captent les évaluations (corrigé en développant cinq fois l'agent initial,
p. 17) ; et les tâches faciles finissent plus tôt, si bien que les agents peu évalués ont une moyenne empirique gonflée,
biais « barely observed » au-delà de 50 évaluations selon eux (p. 17).

**Les expériences et ce qu'elles montrent selon les auteurs.** Juge : les tests exécutables des bancs. Modèles : GPT-5
pour les modifications et GPT-5-mini pour les évaluations sur SWE-bench Verified ; Qwen3-Coder-480B-A35B-Instruct
quantifié et Qwen3-Coder-30B-A3B-Instruct sur Polyglot (p. 8, p. 18). Coût déclaré : « approximately $5000 USD » pour les
trois méthodes (p. 18).

- *Accord entre le critère de sélection et la productivité observée de la lignée* (section 4.1, table 1, p. 8 ; méthode
  en annexe D, p. 19). Cible, pour chaque nœud de l'arbre final : la meilleure moyenne empirique de sa descendance,
  **nœud lui-même exclu** « to avoid the circular use of the target » (p. 8). Prédicteur de la machine de Huxley-Gödel :
  l'agrégat de clade **privé** des évaluations du nœud et du sous-arbre de l'enfant qui contient le maximum, pour éviter
  la « target leakage » (p. 8 ; formule p. 19, vérifiée sur l'image ; v2 : la page 19 désigne cet enfant par le
  maximum du rapport réussites sur échecs pris sur le clade nœud compris, ce qui ne coïncide pas mot pour mot avec la
  cible définie trois lignes plus haut — moyenne de réussite, nœud exclu). Prédicteur des deux autres méthodes : le score
  propre du nœud (p. 19). Corrélations de Pearson pondérées par le nombre d'évaluations : 0,778 contre 0,285 (machine de
  Darwin-Gödel) et 0,444 (agent de Robeyns et al.) sur les 60 tâches de SWE-bench Verified ; 0,626 contre 0,383 et 0,274
  sur Polyglot. Non pondérées : 0,512 contre 0,406 et 0,444 ; 0,873 contre 0,357 et 0,274 (le corps du texte écrit
  « 0.8783 », p. 8). Lecture des auteurs : « strong indications » d'un meilleur estimateur de la métaproductivité (p. 8).
- *Score de l'agent final après 800 évaluations* (section 4.2, table 2, p. 9) : 56,7 % contre 53,3 % (Darwin-Gödel) et
  50,0 % (Robeyns et al.) sur les 60 tâches, agent initial à 40 % ; 30,5 % contre 27,1 % et 25,4 % sur Polyglot, agent
  initial à 20,3 % (p. 8 à 9). Heures de processeur allouées : 517 contre 1 231 sur les 60 tâches (l'agent de Robeyns et
  al. a buté sur la longueur de contexte après 360 évaluations) ; 347 contre 2 385 et 572 sur Polyglot (p. 9).
- *Course longue* (section 4.3.1, p. 9) : 8 000 évaluations sur les 500 tâches de SWE-bench Verified, agent initial
  ajusté à 53,2 %, agent trouvé à 61,4 %. Les auteurs notent eux-mêmes que les agents humains comme machinaux peuvent
  sur-ajuster le banc (p. 9).
- *Transfert* (section 4.3.2, tables 3 et 4, p. 10) : sur SWE-bench Lite privé des 93 tâches communes avec SWE-bench
  Verified, 40,1 % contre 34,8 % pour l'ancêtre et 39,6 % pour SWE-agent avec GPT-5-mini ; avec GPT-5 à la place de
  GPT-5-mini, 47,8 % contre 48,3 % pour le meilleur SWE-agent du classement (« one task behind », p. 10), et 57 % contre
  56,7 % sur les 300 tâches.
- *Observation à l'œil* (annexe F, p. 21) : des agents écrivent leurs modifications dans un fichier de différences que
  les descendants héritent et réécrivent, d'où des différences emboîtées, que les auteurs lisent comme « a natural
  format to present information that inspires long-sighted self-improvement ». Aucune mesure.

**Ce que les expériences ne montrent pas, d'après ma lecture.**
- Aucun bras « même machine, score propre à la place de l'agrégat de clade » : la machine diffère des deux autres
  méthodes à la fois par l'agrégat, le découplage, la granularité agent-tâche, le tirage de Thompson resserré et
  l'exécution asynchrone (table 5, p. 20). Recherche de « ablat » : aucune occurrence. Le gain n'est pas attribué à
  l'agrégat de clade par une expérience.
- Une course par méthode et par banc, sans graine, écart-type ni intervalle (recherche de « standard dev », « confidence
  interval » : aucune occurrence). Sur 60 tâches, 56,7 %, 53,3 % et 50,0 % font 34, 32 et 30 tâches (mon calcul). Sur
  Polyglot, les quatre pourcentages sont des multiples de 1/59 à l'arrondi près, soit 18, 16, 15 et 12 tâches (mon
  inférence : le texte ne donne pas la taille du sous-ensemble).
- Les scores de la table 2 sont lus sur les tâches mêmes qui ont guidé la recherche. Le seul chiffre hors échantillon
  (table 3) compare l'agent final à son ancêtre et à un agent humain, **pas** aux recherches guidées par le score propre.
- La table 1 confond deux effets que les auteurs nomment eux-mêmes (p. 6) : la productivité de la lignée et le simple
  nombre d'échantillons mis en commun. La cible est un maximum de moyennes bruitées, alors que les agents peu évalués ont
  des moyennes gonflées (p. 17). Pour l'agent de Robeyns et al., corrélations pondérée et non pondérée identiques
  (0,444 et 0,274) : sans doute parce que tous ses agents sont évalués sur le jeu entier (p. 20) — mon inférence.

## 3. Confrontation point par point avec l'énoncé 5 de la décision N-045 v2

L'énoncé à la lettre (v2 ; `docs/decisions/decision-N-045-v2.md`, lignes 77 à 83, copié sans changement) :

> 5. **L'héritage d'une génération est récompensé.** Aucun apprentissage de la conception ne traite une génération comme
>    un épisode isolé : le signal rendu à ce qui conçoit (organisme ou concepteur) porte sur **plusieurs générations** —
>    un épisode couvre K générations (K ≥ 3, gelé au préenregistrement), ou la récompense de la génération t inclut,
>    actualisée, les scores des générations t+1 à t+K — de sorte que la mémoire transmise et les instruments à effet
>    différé (sondes et adaptateurs entraînés à t, utiles à t+1) comptent dans le mérite de t. Le bandit à un pas est
>    exclu. Pour les organismes des courses actuelles, l'`historique` servi contient déjà toutes les générations
>    passées ; ce que cet énoncé ajoute vaut pour l'étape 2 et le concepteur.

Trois choses que la paraphrase de la version 1 effaçait. (i) « de sorte que » : la mémoire et les instruments ne sont
pas une pièce à part, ils sont la **conséquence visée** du signal sur plusieurs générations ; si le signal est occupé,
sa conséquence l'est avec lui, dans son principe. (ii) L'énoncé a deux formes au choix : « un épisode couvre K
générations » ou « récompense actualisée » ; la première est le cadre même du papier, avec K égal au budget entier.
(iii) La dernière phrase borne la portée à l'étape 2 et au concepteur, et dit que l'historique est déjà servi aux
organismes actuels.

Cadre où il s'applique : la course de l'organisme à plusieurs générations, avec vivier de conception et familles
inédites (N-044), tâches fraîches par génération (N-049), test final lu une seule fois (N-050), composition des
proposeurs jugée sur l'oracle du monde planté et le coût (N-058).

### 3.1 Ce qui est occupé

| Pièce de l'énoncé | Ce que fait le papier | Verdict |
|---|---|---|
| Créditer une génération ou un agent par les résultats de sa descendance plutôt que par son score immédiat | Définition de la métaproductivité de clade (p. 5) et de son estimateur sur toute la descendance (p. 6) : « aggregating the success of an agent's descendants rather than relying solely on its immediate benchmark score » (p. 2) ; conclusion : « improvement is driven not by narrow benchmarks, but by the long-term generative potential of entire lineages » (p. 12 ; v2 : la version 1 écrivait p. 11, où la conclusion commence) | **occupé** |
| Le bandit à un pas est exclu ; le score immédiat trompe sur le potentiel | « This assumption is overly greedy: it evaluates only the immediate utility of a modification while ignoring its downstream consequences for future self-modifications » (p. 6) ; décalage nommé (p. 2) et mesuré (table 1, p. 8, avec les réserves de la section 2) ; comparaison publiée aux deux méthodes gloutonnes (table 2, p. 9) | **occupé** comme position et comme comparaison publiée ; la preuve expérimentale est mince, ce qui ne rend rien au programme |
| Le signal couvre plus d'une génération ; « un épisode couvre K générations » | L'agrégat couvre toute la descendance, jusqu'à la fin du budget (p. 5 à 6) : forme plus large que la nôtre, qui la contient comme principe. v2 : la recherche entière est un épisode à récompense terminale (« until the end of the episode », « no other rewards received before termination », p. 5) : la première forme de l'énoncé y est, avec K égal au budget, non gelé à trois | **occupé** dans son principe ; pour la forme « épisode », occupé à la valeur de K près |
| v2 — « de sorte que […] les instruments à effet différé […] comptent dans le mérite de t » (le principe, hors objets) | La mesure est faite pour cela : capacité de l'agent à améliorer sa capacité d'amélioration, « which leads to better downstream performance of distant future agents » (p. 4) ; un algorithme peut d'abord améliorer sa capacité à s'améliorer « while neglecting direct benchmark abilities, only to later focus on them » (p. 5) ; « reusing newly gained abilities to fuel subsequent improvements » (p. 2) ; « a modest ancestor can still be highly valuable if its descendants consistently advance » (p. 6) | **occupé** dans son principe (la version 1 classait toute la pièce « non occupée ») |
| v2 — « Aucun apprentissage de la conception ne traite une génération comme un épisode isolé », pour un apprentissage par sélection | Ce qui conçoit est l'agent (« agents modify themselves to generate new agents », p. 3) ; la règle de recherche choisit quels concepteurs se reproduisent d'après le signal de lignée (p. 6) ; les auteurs disent la mesure tournée vers « the improvement of self-improvement itself » (p. 5) | **occupé** pour un concepteur amélioré par sélection ; l'entraînement d'un concepteur reste en 3.3 |
| v2 — L'`historique` de toutes les générations passées servi à ce qui conçoit (dernière phrase de l'énoncé) | Les auteurs l'attribuent à l'agent de Robeyns et al. : il modifie le meilleur agent « with the entire history accessible to the agent » (table 5, p. 20) | **publié ailleurs selon ce papier**, de seconde main : à lire dans Robeyns et al. avant toute phrase (R7) ; l'énoncé ne le revendique pas, mais aucun texte ne doit le présenter comme nôtre |

### 3.2 Ce qui relève du savoir commun

- **Rendement à plusieurs pas, troncature à K pas, actualisation** : manuel d'apprentissage par renforcement (Sutton et
  Barto, que les auteurs citent pour la fonction de valeur, p. 15). Juger une action par ses conséquences en aval est la
  définition même d'une fonction de valeur ; les auteurs disent que leurs deux grandeurs en sont (p. 5, p. 15). Notre
  forme « K générations, actualisées » est une instance banale de ce savoir, absente de ce papier mais **non
  revendicable** pour autant.
- **Remontée des résultats des descendants vers l'ancêtre dans une recherche arborescente** : recherche arborescente de
  Monte-Carlo, que les auteurs citent et dont ils se distinguent par l'objectif (choix final à budget fixe plutôt que
  récompense cumulée, p. 11 ; Coulom 2006, Kocsis et Szepesvári 2006).
- **Juger une auto-modification sur ce qui la suit** : antériorité plus ancienne que les auteurs décrivent eux-mêmes —
  l'algorithme de l'histoire à succès (Schmidhuber et Zhao 1996 ; Schmidhuber, Zhao et Wiering 1997), qui annule après
  coup les suites d'auto-modifications n'ayant pas relevé le taux de récompense à long terme, et l'exécution monotone en
  aptitude (Kirsch et Schmidhuber 2022, arXiv 2212.14392), qui favorise les modèles à meilleure performance **ancestrale**
  (p. 11). **Lu ici de seconde main seulement** (description des auteurs, p. 11) : à lire sur source avant toute phrase
  d'antériorité (R7).

### 3.3 Ce qui n'est pas occupé par ce papier

« Non occupé par ce papier » veut dire : cherché dans les 30 pages de la version 3, non trouvé. Ce n'est pas un trou du
champ (R8), et ces zones sont séduisantes, donc à vérifier plus durement que les autres.

| Pièce de l'énoncé | Ce que fait le papier | Verdict |
|---|---|---|
| Signal servant à **entraîner** un concepteur (poids ou texte ajustés sur un rendement à K générations) | Le signal guide une règle de sélection figée (tirage de Thompson, p. 6 ; algorithme 1, p. 17) ; rien n'est entraîné sur ce signal ; aucun texte ne dit que l'agent qui se modifie le reçoit — c'est au contraire la méthode de Robeyns et al. qui modifie l'agent « with the entire history accessible to the agent » (table 5, p. 20) | v2 : **non trouvé dans ce papier pour l'entraînement seulement** ; la sélection de ce qui conçoit sur ce signal est occupée (3.1). Réserve dure, durcie : un concepteur entraîné par renforcement sur des rendements à K pas, c'est de l'apprentissage par renforcement ordinaire ; et les auteurs décrivent l'algorithme de l'histoire à succès comme forçant « self-modifying policies to discover more effective self-modification strategies » sur un critère de « long-term reward rates » (p. 11) — un apprenant qui se modifie, crédité sur le long terme, dès 1996 selon eux (seconde main, à lire sur source). Ce qui pourrait nous rester est l'objet (un concepteur d'organisme, une génération comme pas de temps, le coût dans le signal), sûrement pas le principe. Co-Harness et WHALE, qui alternent recherche et affinage, sont à lire avant toute phrase |
| Les **objets** de l'héritage : une mémoire transmise séparée ; des sondes et adaptateurs entraînés à t, servis à t+1 | Ce qui s'hérite est le code entier de l'agent (p. 3), donc tout ce que l'agent y a écrit, outils et fichiers compris ; ni mémoire séparée, ni instrument entraîné ; l'héritage des fichiers de différences est observé à l'œil, sans mesure (p. 21) | v2 : **objets non trouvés dans ce papier** ; le principe (compter dans le mérite de t ce qui ne sert qu'après) est occupé (3.1). ALMA et MemEvolve (mémoire), Co-Harness et WHALE (instruments) à lire |
| **Question causale** : l'archive héritée cause-t-elle les découvertes ? (trou relevé dans notre course, R-3164) | Aucune comparaison avec et sans héritage, aucune comparaison au meilleur de N tirages indépendants à budget égal, aucune ablation (section 2) ; la comparaison est entre règles de sélection sur un même type d'arbre | **non occupé par ce papier**. Question à poser au PDF de la machine de Darwin-Gödel : compare-t-elle une recherche avec archive à une recherche sans archive ? Si oui, la question causale y est au moins voisine |

## 4. Ce que nous pouvons en reprendre, cité

1. **La précaution contre la fuite de cible dans l'estimation** (Wang et al. 2025, section 4.1, p. 8, et annexe D,
   p. 19). Toute épreuve qui demande si un signal de lignée prédit la productivité future d'une génération doit retirer
   du prédicteur la génération elle-même et la branche qui contient la cible ; sinon, le prédicteur contient la cible.
   Pour notre course, avant de geler K et l'actualisation : prédire, pour chaque génération d'une course déjà faite, le
   meilleur score de sa descendance, prédicteur privé de la génération et de la branche du maximum, et y **ajouter les
   deux contrôles qui manquent au papier** : un bras « score propre à nombre d'évaluations égal » (pour séparer
   l'héritage du simple nombre d'échantillons, confusion que les auteurs nomment p. 6) ; et des tâches fraîches pour les
   descendants (N-049), pour que l'agrégat ne soit pas une mesure répétée sur les mêmes items. Préenregistrement d'abord
   (R1). Calcul sur processeur.
2. **Le constat du décalage entre performance immédiate et potentiel à long terme**, à citer comme affirmation des
   auteurs avec sa réserve : « a high-scoring agent may produce unproductive descendants, while a lower-scoring one seeds
   lineages that achieve greater long-term gains » (p. 2) ; mesure de la table 1 (p. 8), qui ne sépare pas productivité
   de lignée et taille d'échantillon.
3. **Deux précautions d'exécution parallèle**, utiles à nos courses asynchrones (affirmations des auteurs, p. 17) : les
   premières itérations finies captent les choix suivants ; et les tâches faciles finissent plus tôt, ce qui gonfle la
   moyenne des agents peu évalués. Toute lecture intermédiaire d'une génération doit en tenir compte.
4. **Le maximum de moyennes bruitées comme cible est biaisé vers le haut** (conséquence du point 3, p. 17) : à éviter
   comme cible d'une épreuve de prédiction, ou à corriger (moyenne à nombre d'évaluations égal, ou meilleur sur tâches
   fraîches).
5. **Observation sur le code publié, pour mémoire** (lecture du code, jamais exécuté ; à confirmer avant de l'opposer).
   Le poids du score propre dans l'agrégat est réglé par un paramètre absent du papier, `n_pseudo_descendant_evals`,
   10 000 par défaut aux deux commits. Au premier commit (`depot-code-f3ca5f8-tree.py.txt`), l'agrégat compte
   `num_pseudo` copies de la moyenne propre du nœud — 10 000 si l'appel passe la valeur du fichier de configuration, ce
   que les pièces versées ne montrent qu'au commit de tête (`depot-code-013872d-hgm.py.txt`, ligne 391 ; le fichier
   `hgm.py` du premier commit n'est pas versé, et la valeur par défaut de la fonction est 10 ; v2) —, puis la liste `[nœud] + descendants` privée de son **dernier** élément
   (`get_sub_tree()[:-1]`) : avec 800 évaluations, l'agrégat par défaut serait presque le score propre. Au commit de tête
   (`depot-code-013872d-tree.py.txt`), avec la valeur par défaut, la liste rendue est la liste même des évaluations
   propres du nœud, que `+=` étend en place par celles des descendants à chaque appel (sémantique de Python). Les valeurs
   par défaut du dépôt diffèrent aussi du papier sur le resserrement (`cool_down: false` contre τ = B/b, p. 7). On ne
   peut rien en déduire sur ce qui a tourné pour les tables. Deux leçons seulement : ne pas prendre ce dépôt tel quel
   comme base de comparaison ; et le poids du score propre face aux descendants est un curseur continu entre le bandit à
   un pas et le crédit de lignée entier — un préenregistrement peut prédire une relation dose-effet sur ce curseur.

## 5. La lettre de ce que nous ne pouvons plus présenter comme nôtre

Proposition de lecture, soumise à Lazar (modification de revendication : nœud ; rien n'est changé ici).

**Ne plus écrire comme idée ou constat du programme :**
- « récompenser l'héritage d'une génération », « créditer une génération (ou un agent) par les résultats de sa
  descendance », « le mérite d'une génération inclut ce que ses descendants obtiennent » ;
- « le score immédiat est un mauvais guide du potentiel d'amélioration à long terme » ; « la sélection gloutonne sur le
  score immédiat est trop courte » ; « exclure le bandit à un pas » présenté comme un apport ;
- « un signal sur plusieurs générations, tronqué à K et actualisé » présenté comme une idée : c'est un rendement à
  plusieurs pas.
- v2 : « faire compter dans le mérite d'une génération ce qu'elle construit et qui ne sert qu'aux suivantes » présenté
  comme une idée, quel que soit l'objet : c'est la raison d'être de la mesure des auteurs (p. 4, p. 5).
- v2 : « ce qui conçoit est jugé sur plusieurs générations » présenté comme une idée, quand ce qui conçoit est
  sélectionné : c'est ce que fait le papier (p. 3 à 6). Et « servir tout l'historique au concepteur » : attribué par les
  auteurs à Robeyns et al. (p. 20).

**Lettre proposée pour l'énoncé 5 dans tout texte sortant :** (v2 : la lettre de la version 1 disait « propre à notre
dispositif » l'objet, le destinataire et la question causale ; les deux premiers ne tiennent plus sous cette forme.)
« Suivant Wang et al. (2025), qui créditent un agent par les résultats agrégés de sa descendance (métaproductivité de
clade) pour guider une recherche d'auto-modifications, afin que compte ce qu'un agent prépare pour ses successeurs, et
l'antériorité qu'ils décrivent (Schmidhuber et Zhao 1996 ; Schmidhuber, Zhao et Wiering 1997), nous rendons au
concepteur un signal qui porte sur K générations, actualisé — un rendement à plusieurs pas au sens de Sutton et Barto.
Nous appliquons ce principe à d'autres objets (une mémoire transmise, des sondes et adaptateurs entraînés à une
génération et servis à la suivante) et à un concepteur entraîné plutôt que sélectionné, avec le coût dans le signal.
Nous posons une question que ce travail ne pose pas : l'archive héritée cause-t-elle les découvertes ? » Aucun de ces
trois points ne se dit « nouveau » ni « propre » tant que les voisins de la section 6 et les antériorités de 1996 et
1997 ne sont pas lus.

**Citations obligatoires dans tout texte qui touche à l'énoncé 5 :**
1. Wang, Piękos, Li, Laakom, Chen, Ostaszewski, Zhuge, Schmidhuber, « Huxley-Gödel Machine », arXiv 2510.21614 (version 1
   du 24 octobre 2025 ; présentation orale à ICLR 2026 selon la fiche OpenReview T0EiEuhOOL, version de la conférence
   non lue). Pour le principe, le constat du décalage et la précaution contre la fuite de cible.
2. Zhang, Hu, Lu, Lange, Clune, « Darwin Gödel Machine », arXiv 2505.22954, et Robeyns, Szummer, Aitchison, « A
   self-improving coding agent », arXiv 2504.15228 : les deux méthodes à sélection sur le score propre contre lesquelles
   le principe a été posé.
3. Sutton et Barto, *Reinforcement Learning: An Introduction* : pour le rendement à plusieurs pas et l'actualisation.
4. Schmidhuber et Zhao (1996) ; Schmidhuber, Zhao et Wiering (1997), algorithme de l'histoire à succès ; Kirsch et
   Schmidhuber (2022), exécution monotone en aptitude : **à lire sur source avant de les citer** comme antériorité
   (connus ici par la seule description de la page 11).

## 6. Voisins à lire ensuite (sans jugement)

Chacun avec la question qu'il doit trancher ; aucun n'est lu ici, aucun chiffre n'en est repris.

| Voisin | Question à lui poser |
|---|---|
| Machine de Darwin-Gödel (Zhang et al., arXiv 2505.22954) | L'archive de tous les agents produits est-elle comparée à une recherche sans archive, ou à des tirages indépendants à budget égal ? Ce qu'elle dit de l'héritage des modifications |
| Co-Harness (arXiv 2607.22688) | Le signal rendu à ce qui est affiné porte-t-il sur plusieurs tours de recherche ? Un instrument entraîné à un tour est-il servi au suivant, et compte-t-il dans le mérite du tour où il a été entraîné ? |
| WHALE (arXiv 2609.00196) | Mêmes questions que pour Co-Harness (alternance entre recherche du harnais et affinage, selon la notice) |
| ALMA (arXiv 2602.07755) | La conception de mémoire apprise est-elle jugée sur son effet différé, sur plusieurs générations ou sous-tâches ? |
| MemEvolve (arXiv 2512.18746) | Même question ; la mémoire est-elle transmise entre générations d'un système qui se réécrit ? |
| Version de la conférence de la machine de Huxley-Gödel (OpenReview T0EiEuhOOL, accès refusé le 18 novembre 2026, non contourné) | Contient-elle une ablation qui isole l'agrégat de clade, ou plusieurs graines ? |
| Algorithme de l'histoire à succès (1996, 1997) ; exécution monotone en aptitude (2022) | Antériorité exacte du crédit à long terme d'une auto-modification. v2 : la règle qui se modifie y **apprend**-elle sous ce crédit ? Si oui, « un concepteur qui apprend, crédité sur le long terme » est pris depuis 1996 |
| v2 — Agent de code auto-améliorant de Robeyns, Szummer et Aitchison (arXiv 2504.15228) | L'historique de toutes les générations est-il servi à l'agent qui se modifie, et sous quelle forme (table 5, p. 20, de seconde main) ? |

## 7. Limites de cette lecture et comparaison avec la lecture 05

- Tout « absent » vaut pour la version 3 d'arXiv du 29 octobre 2025. La version de la conférence (révisée, modifiée
  jusqu'au 11 avril 2026) et les rapports n'ont pas pu être lus (accès refusé, consigné dans `adresse.txt`).
- Code lu par fichiers ciblés, jamais exécuté.
- Concordances avec `lecture-05-v1.md` : principe occupé ; forme plus large que la nôtre ; aucune ablation ; table 1 qui
  confond nombre d'échantillons et productivité ; décomptes 34, 32, 30 sur 60 et 18, 16, 15, 12 sur 59 ; observation sur
  `n_pseudo_descendant_evals`.
- Écarts : (a) la lecture 05 classe la forme « K générations, actualisées » « occupée en partie » et le nombre gelé et
  l'actualisation « pas dans ce document » ; je la classe **savoir commun** (rendement à plusieurs pas), donc non
  revendicable quel que soit ce que disent les voisins. (b) La lecture 05 juge l'expérience « poids contre archive »
  libre au regard du document ; je ne la juge pas ici et pose à la place la question causale (archive héritée et
  découvertes), qu'aucun bras de ce papier ne touche. (c) J'ajoute, sur le code du premier commit, que la tranche
  `[:-1]` inclut le nœud et retire le dernier descendant, ce que la lecture 05 ne mentionne pas.

## 8. Ce que la version 2 change (après contre-lecture)

Contre-lecture : `docs/notes/veille-exploration-idees-v1/contre-lecture-lecture-huxley-godel-v1.md` (verdict « à
corriger » ; 30 passages rouverts dans le PDF, 29 tiennent, un porte une page fausse ; quatre vérifications hors du
PDF).

Corrections de fait :
1. L'énoncé 5 est cité à la lettre (section 3) ; la version 1 le paraphrasait, perdait « de sorte que » et la dernière
   phrase.
2. La citation de la conclusion est page 12, non page 11 (3.1).
3. Renvois internes : les voisins sont en section 6, la comparaison avec la lecture 05 en section 7.
4. Citations ajoutées, toutes rouvertes dans le PDF : p. 3 (« agents modify themselves to generate new agents »), p. 4
   (définition de la métaproductivité), p. 5 (« until the end of the episode » ; « An algorithm might, at the
   beginning […] » ; « the improvement of self-improvement itself »), p. 11 (« self-modifying policies […] »).
5. Date : mise en public de la soumission le 8 octobre 2025 selon la fiche OpenReview (contenu à cette date non lu) ;
   décision N-045 v2 du 25 octobre 2026.
6. Deux remarques sur la lettre du papier : la règle de choix final est dégénérée à ε = 1 (p. 7) ; la page 19 désigne
   l'enfant retiré par un rapport réussites sur échecs, nœud compris.
7. Code : le fichier `hgm.py` du premier commit n'est pas versé ; « 10 000 copies au premier commit » est donc
   conditionnel.
8. La lecture 05 est suivie par git depuis `478111c2`.

Requalifications qui en découlent (jugement du contre-lecteur, fondé sur les citations du point 4 ; à trancher par
Lazar comme le reste) :
- « mémoire transmise et instruments à effet différé comptés dans le mérite de t » : de « non occupé par ce papier » à
  « principe occupé, objets non trouvés » ;
- « signal rendu à un concepteur qui apprend » : de « non occupé par ce papier » à « occupé pour un concepteur
  sélectionné, non trouvé pour un concepteur entraîné, avec une antériorité de 1996 à lire » ;
- la lettre proposée ne dit plus « propre à notre dispositif » ;
- seule la question causale reste « non touchée par ce papier », sous réserve de la machine de Darwin-Gödel.

Ce qui ne change pas : tous les chiffres, la description de la machine, le classement « savoir commun » de la forme
« K générations, actualisées », les cinq reprises de la section 4, les réserves sur la version de la conférence.
