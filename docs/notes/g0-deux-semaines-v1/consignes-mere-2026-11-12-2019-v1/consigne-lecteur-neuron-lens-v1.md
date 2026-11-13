# Consigne — lecteur neuf de « Neuron Lens » (catalogue de neurones lus par lentilles) et de ses sources — v1

Écrite par la session mère le 13 novembre 2026 à 12:44 UTC (`date -u`). Tu es un sous-agent neuf, lecteur ; tu n'écris aucun
code du programme et tu ne modifies aucune pièce existante. Langue : français, presque aucun acronyme.

## 0. Interdits (à lire d'abord, sans exception)
Lis en entier `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`
(`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) et applique-le. En particulier : jamais `donnees/bras-attaque*`,
`donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*` ;
aucun `diag/` ni `runs/` ; **aucun préenregistrement ni résultat de T0.6, T0.7, P3 ou P3-bis** (tu restes ainsi libre de
tout rôle de lecteur plus tard) ; jamais une valeur de clé, jamais `env`, `printenv`, `set` sans argument ; jamais d'heure
écrite à la main (`date -u`) ; aucune opération git ; aucun `grep -r` ni `find` à la racine du dépôt : ne lis que les fichiers
nommés ici. Mémoire limitée : `ulimit -v 6000000`, aucun calcul lourd, **aucun téléchargement de poids ni de jeu de données**,
aucune exécution du code lu. Aucune dépense. Ne contourne aucun refus.

## 1. Pourquoi
Lazar a signalé le 13 novembre `https://neuron-lens.com/` : « et si nous utilisons ce neuron lens pour les moniteurs ?
découverte phénoménale en mech interp ». Page archivée : `docs/sources/web-neuron-lens-20261113/llms.txt` (`7cc1f486…`).
Première lecture de la mère (niveau transcription, à vérifier) : catalogue de chaque neurone (par signe, « pôle ») et de
chaque tête d'attention de Qwen3-8B et de Gemma 4 12B, lus par deux lentilles tirées des poids (lentille R : ce qu'une
direction fait dire au modèle ; lentille S : quels jetons d'entrée y mènent), étiquetés par un modèle Claude ; ni article,
ni réplication indépendante, rien sur la surveillance ; aucun modèle Llama. Nos moniteurs boîte blanche sont des sondes sur
les activations de Llama 8B. Règles : R4 (trop beau = réserve), R7 (aucun chiffre opposable sans source empreintée), R8.

## 2. À lire
1. `llms.txt` archivé, en entier. Puis, par un client générique sans aucune donnée du projet : le dépôt de recherche
   `https://github.com/stdlogits/neuron-lens` — `README.md`, `docs/design.md`, `docs/findings.md` (en entier, par morceaux
   s'il est long), le fichier de licence s'il existe, et la liste des scripts (noms, ce qu'ils exigent) ; la fiche du jeu de
   données et celle des lentilles sur Hugging Face (licence, format, taille) ; l'essai de Cammarata « Neural Networks Are
   Already Clean » (`https://already-clean.goodfire.com/`) ; les travaux amont cités (lentille J de Gurnee et al. 2026,
   lentille R, lentille K, règles RelP) : retrouve leurs références exactes ; lis l'article quand il est public, sinon
   marque « niveau transcription ». Archive ce que tu peux sous `docs/sources/neuron-lens-lecture-20261113/` (texte ou PDF,
   scellés par `PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER`) ; ce qui n'est pas archivé est dit tel.
2. De nos pièces, seulement : `docs/programme-controle-ia-v2.md` (les hypothèses H1 à H7 et ce qui décrit les sondes, les
   bases boîte blanche et les traits internes) ; `docs/decisions/decision-N-056-v1.md`, `decision-N-061-v1.md`,
   `decision-N-053-v1.md`, `decision-N-029-v1.md` (si un de ces noms n'existe pas, liste le dossier `docs/decisions/` et prends
   la version la plus récente du même numéro) ; `docs/etat-de-l-art-controle-ia-v1.md` (ce qui touche les sondes, les
   autoencodeurs parcimonieux, la lentille des logits).

## 3. À écrire : `docs/notes/lecture-voisin-neuron-lens-v1.md`, scellée
Dans cet ordre :
- verdict en trois lignes : ce que c'est, ce que ce n'est pas, utile ou non à nos moniteurs ;
- la méthode, exactement : objets calculés, ajustement des lentilles (données, calcul, durée), ce qui est mesuré contre quel
  témoin ; chaque chiffre avec fichier, empreinte ou adresse, et passage ;
- solidité (R4) : tailles d'échantillon, qui étiquette et qui juge, ce qui est amplifié au-delà du régime naturel, limites
  dites par les auteurs, absence ou présence de réplication, ce qui contredit l'idée de « neurones déjà propres » ;
- portabilité à **Llama 3.1 8B** : la couche à portes de Llama s'y prête-t-elle ; le code ajuste-t-il les lentilles sur un
  autre modèle sans réécriture ; licence du code et des artefacts ; **devis d'ordre de grandeur** (heures de processeur
  graphique, étiquetage) marqué « illustratif », avec sa source ;
- usages possibles pour le programme, classés par coût, chacun avec ce qu'il mesurerait, son témoin et son risque :
  (a) lire par les lentilles **la direction d'une sonde** (ce qu'elle fait dire ; quels jetons d'entrée la portent) comme
  audit de fuite textuelle ; (b) les neurones comme traits d'un moniteur, comparés aux traits d'autoencodeurs parcimonieux
  et aux sondes sur le flux résiduel ; (c) autres ; et ce qui serait **interdit sans nœud** (changer de modèle, toucher une
  liste scellée, écart à un préenregistrement) ;
- tableau « nos revendications × ce travail » : pris / voisin à citer / ouvert / sans rapport, phrase à l'appui ;
- ce que tu n'as pas pu lire.

## 4. Rapport final à la mère (court)
Verdict ; chemins et empreintes ; toute zone revendiquée trouvée occupée ; ce qui n'a pas pu être lu.
