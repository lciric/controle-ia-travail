Tu es un lecteur expert neuf. Tu n'as écrit ni l'organisme d'idéation, ni ses textes, ni les réponses de candidature. Français, sans sigle non développé ; toute heure vient de `date -u`.

## La demande de Lazar (3 novembre 2026, 09:57 heure de Paris), mot pour mot
« Dix échecs d'alignement : Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner, « Automated Researchers Can Reliably Mitigate Alignment Failures », arXiv 2608.28945 (août 2026). […] Cinq chercheurs automatiques par échec, un classement, un banc tenu à l'écart, Petri, et un moniteur de triche (§7 ; annexes F et G). : on peut s'inspirer de leurs méthodes pour une partie de l'organisme ? va lire le papier en détail »

## 1. Lis le papier en entier, annexes comprises
Sources, dans cet ordre (par `WebFetch`, par tranches avec `offset` jusqu'au bout de chaque page) :
- `https://arxiv.org/html/2608.28945` (essaie aussi `…/2608.28945v1` et `…v2` : la version HTML d'arXiv contient souvent les annexes que la conversion du PDF coupe) ;
- `https://arxiv.org/pdf/2608.28945` ;
- la version blog `https://alignment.anthropic.com/2026/automated-alignment-researchers/` ;
- le PDF d'Anthropic `https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf` ;
- le billet compagnon « Automated Weak-to-Strong Researcher » `https://alignment.anthropic.com/2026/automated-w2s-researcher/` et l'annonce `https://www.anthropic.com/news/automated-alignment-researchers`.
Les lecteurs précédents n'ont pas pu lire les **annexes F et G** (moniteur de triche ; G.1 règle de notation, G.2 invite) ni la **figure 32** : la conversion du PDF s'arrêtait au début de l'annexe D, la version blog au milieu de E.1. Essaie toutes les voies (HTML d'arXiv, ancres de section de la version blog, autres versions) et dis exactement ce que tu as pu lire et ce que tu n'as pas pu. Cherche aussi le **harnais ouvert** que Kirchner mentionne sur sa page (« experiments extending the open-source harness ») : lien, licence, ce qu'il contient (`WebSearch`, puis `WebFetch`).

## 2. Lis l'organisme, pour comparer
- `https://github.com/lciric/ideation-organism` n'est pas lisible par `WebFetch` : lis la copie locale `/home/claude/ideation-organism/README.md` (sections 1 à 4 et 6 ; la figure 1 donne le parcours d'une idée : proposer, aiguiller, mémoire, juges croisés, bisociateur, nouveauté, pari et juge statistique, tests de mort, sélection) et les pages `resultats/attaque-goodhart-v2/README.md`, `resultats/controle-p3-premier-test/README.md` du même dossier.
- Ce qui ne va pas aujourd'hui dans l'organisme (faits publics du README) : les juges de modèles de langage au plafond (11 fiches sur 12 « notables », κ = 0) ; l'étage des tests de mort et la boucle de génération à génération jamais joués pour de vrai ; l'attaque A1 (brèche par la classe que la nulle ne couvre pas).

## 3. Ce que tu produis
Un rapport `/home/claude/scratch/kirchner-2608-lecture/lecture-2608-28945-pour-organisme-v1.md` :
1. **Le papier, méthode par méthode** (avec section, page ou figure, et chiffres exacts ; une citation de moins de quinze mots au plus par source) : la tâche et ses dix échecs ; le harnais (agents, budget, forum partagé, outils, classement, métrique de score, banc tenu à l'écart, Petri, modèles plus grands) ; la sélection de la méthode finale ; le moniteur de triche (avant exécution et après coup ; modèle ; règle ; taux ; catégories) ; les gardes de capacité ; les modes d'échec déclarés et les remèdes ; ce que le billet faible-vers-fort ajoute (plafonds de resoumission, triche observée).
2. **Ce que l'organisme peut prendre**, par étage de l'organisme (proposer, aiguiller, mémoire, juges, bisociateur, nouveauté, juge statistique, tests de mort, sélection, boucle) : leur méthode ; ce qu'elle changerait chez nous, concrètement (fichier ou étage du README) ; ce qu'elle coûte ; **ce qui la rendrait dangereuse chez nous** (un classement qui récompense un score est exactement ce que notre juge statistique veut empêcher de gonfler : dis pour chaque emprunt s'il réintroduit une boucle que l'on peut optimiser) ; une priorité (haute / moyenne / basse) avec sa raison.
3. **Ce que l'organisme a et que leur harnais n'a pas** (avec preuve dans leurs textes : par exemple l'absence de rappel publié du moniteur, la règle de promotion par richesse contre une nulle qui contient les acceptations) — utile pour la question 2 de Kirchner.
4. **Le harnais ouvert** : peut-on y faire tourner une première expérience de quelques jours (par exemple mesurer le rappel de son moniteur sur des tricheries plantées avant et après sélection par le classement, ou brancher notre juge statistique à la place du maximum du classement) ? Ce qu'il faudrait, ce que cela coûterait (marqué « calcul » ou « supposé »).
Réponse finale : les cinq emprunts les plus utiles (une ligne chacun, avec leur danger), ce que tu n'as pas pu lire, le chemin et le sha256 du rapport.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch` ; aucun appel de modèle autre que toi ; `WebFetch` et `WebSearch` pour les sources nommées et le harnais seulement ; n'invente aucun identifiant, chiffre ou citation.
