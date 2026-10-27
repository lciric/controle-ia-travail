# Avis de l'instance sortante de conv-audit sur la « Boucle d'or » de Gemini (v6.3.0) — v1

Écrit le 27 octobre 2026 à partir de 08:18 UTC (heure lue sur `date -u`). Pièce lue : la réponse de Gemini relayée par
Lazar (09:16 heure de Paris), fichier joint d'empreinte `2784138902c62532602fa9e3f738d58c7ab7ed7e52c4f7cd422f7fc19f3acb1e`
(non versée ; son script PowerShell n'est pas exécuté ici). Exploratoire, non opposable.

## Verdict

Les deux idées valent d'être éprouvées : une fenêtre non monotone sur la distance entre parents, et une allocation du
budget d'expériences selon le gain d'information. Mais la simulation de Gemini ne prouve rien : elle est construite
pour passer. Ne pas l'adopter sur ce chiffre. Gemini a vérifié le commit `52d4b2f7` (huit empreintes, **avant
l'addendum**), pas `ce22a89` : il n'a pas vu la rétrodiction (la marche « à la Swanson » ne bat pas l'allocation de
ressources), et sa brique 1 se branche encore sur cette marche. Envoyer le texte PowerShell v2 (neuf « OK »).

## Pourquoi la simulation ne prouve rien

1. **Circulaire** : les mondes rangent les hypothèses en trois strates par bandes de similarité de domaine
   (0,50-0,80 / 0,12-0,26 / 0-0,015) ; la fenêtre de l'allocateur est centrée dans la bande du milieu ; la mémoire de
   calibration lui est **donnée** avec les taux de survie mêmes du monde (18/20, 10/20, 1/20) ; les triviales ne
   comptent jamais comme découvertes, les chimères presque jamais (3 %). Le facteur « × 2,5 » découle de l'arithmétique de la construction
   (environ 0,5 découverte par dollar pour la strate du milieu, environ 0,17 au hasard) ; l'essai qui exige « > 1,8 fois »
   vérifie que le monde a été construit comme prévu.
2. **Bandit de paille** : le bonus « UCB » ne dépend que de l'indice du monde, le même pour toutes les hypothèses ; c'est
   un tri glouton sur la probabilité de survie, récompensé par la survie et non par la découverte. Un vrai bandit récompensé
   par les découvertes (par exemple un échantillonnage de Thompson par strate) apprendrait les mêmes strates.
3. **Prémisse fausse pour notre juge** : Gemini assimile « triviale » à « survit à 90 % ». Chez nous, une fille sans contenu
   nouveau est dans son propre nul : elle survit au plus à α. Ce n'est pas l'allocateur qui écarte les triviales, c'est le
   juge. L'objectif juste est l'espérance de découvertes vraies par dollar, plus la valeur d'apprendre la calibration ;
   l'entropie du verdict (maximale à p = 0,5) n'en est qu'un substitut, utile surtout au début. Le score
   H₂(p) × 4p(1−p) × pénalité compte deux fois la même chose et n'a pas de fondement.

## Uzzi et collègues (2013)

Référence juste : *Science* 342, 468-472 ; 17,9 millions d'articles du Web of Science ; conventionnalité = z médian des
paires de revues citées ensemble, nouveauté = z au 10ᵉ centile. Taux de « hits » (5 % les plus cités) :
**9,11 pour 100** pour les articles à forte conventionnalité et forte nouveauté, contre 5 pour 100 en moyenne ; **5,33 pour
100** pour faible conventionnalité et forte nouveauté (lu par transcription du PDF de Kellogg, page 469 ; à revérifier sur
PDF empreinté avant tout usage, R7). Deux inexactitudes chez Gemini : les proportions « 85-90 % d'ancrage, 10-15 % de
nouveauté » ne sont pas dans l'article ; les articles très atypiques ne « s'effondrent » pas, ils restent au niveau de la
moyenne. Surtout, la transposition est inventée : Uzzi mesure les paires de revues dans les références d'**un** article,
pas la similarité entre **deux** articles parents ; le centre de la fenêtre (0,18 dans le code, 0,22 dans le texte) et sa
largeur ne sont étalonnés sur rien.

## Le test qui pourrait échouer (proposé, dans l'orchestrateur, sur processeur)

- L'allocateur apprend la calibration **en ligne** (rien n'est donné) ; ses concurrents : hasard, échantillonnage de
  Thompson récompensé par les découvertes, tri par espérance de découverte par dollar.
- Mondes où la valeur **ne suit pas** la fenêtre (monotone, ou maximale aux bords) : la fenêtre doit y perdre (contrôle
  « monde inversé », comme pour les ponts plantés).
- Mesure : découvertes vraies par dollar sur les témoins, promues par le juge v1 ; seuil préenregistré.
- Pour la fenêtre d'Uzzi sur données réelles : il faut les citations (OpenAlex avec une clé : décision de Lazar).
