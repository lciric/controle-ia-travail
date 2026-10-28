# Brainstorm — encoder la mémoire du pôle pour qu'elle améliore les propositions et empêche les redites — v1

Lignée conv-audit (instance nouvelle), écrit le 27 octobre 2026 à partir de 08:26 UTC (heure lue sur `date -u`), sur le mot
de Lazar de 09:17 heure de Paris. Exploratoire (R-522) ; rien n'est mesuré ici ; les trois pistes de la fin se testent en
simulation. Pièces : relais de l'instance sortante (`0aa24f55…`, piste « signature prédictive ») ; mémoire v0
(`orchestrateur-v0/pole/memoire.py`) ; juge v1 (`orchestrateur-pole-v2/`).

## Verdict

1. **L'unité de mémoire n'est pas le texte : c'est la loi prédictive que la fiche engage**, ramenée à ce qu'elle dit des
   traits, **modulo les transformations aveugles** (mélange avec une loi aveugle, biais par issue, changement d'échelle,
   renommage). Deux fiches qui ordonnent pareil les instances d'une sonde fixe disent la même chose.
2. **Une redite ne doit pas être refusée, elle doit hériter du dossier de preuve de sa classe.** Les e-valeurs se
   multiplient quand les tirages sont frais : chaque classe d'hypothèses porte sa richesse cumulée, et une redite repart de
   là, pas de 1. Plus de « réessayer jusqu'à la chance », et une hypothèse vraiment plus forte peut encore gagner.
3. **Pour améliorer les propositions**, servir peu, structuré et mesurable : une archive qualité-diversité indexée par la
   signature, les causes d'échec écrites par le juge lui-même (le membre du nul qui a gagné), les survivantes comme
   marchepieds, et viser les cases à chance de survie intermédiaire. Pas de leçons en texte libre.

## 1. Pourquoi le texte ne suffit pas

- Le Jaccard des 3-grammes ne voit ni la copie renommée, ni le jargon rare, ni le changement d'échelle : par construction.
- Les plongements sémantiques voient la paraphrase, pas la prédiction : deux énoncés proches peuvent prédire l'inverse,
  deux énoncés lointains la même chose.
- La mémoire spectrale de l'autre organisme était aveugle sur textes réels (génération 0, rappel 0,000).
- Ce matin, « parent + loi aveugle » passe aussi le critère des filles du juge : ni le texte ni le juge ne voient une
  redite modulo l'information aveugle. C'est le même trou, vu de deux côtés.

## 2. L'encodage d'une entrée

| champ | encodage | sert à | comment il échoue |
|---|---|---|---|
| identité | **signature invariante** : sur une sonde fixe de 256 instances du domaine, pour chaque paire d'issues, le rang des instances selon la log-cote prédite (invariant aux biais par issue et aux mélanges aveugles, presque exactement) | redite, classe | deux fiches de même ordre mais d'effets très différents tombent dans une classe : d'où l'héritage plutôt que le refus |
| contenu brut | signature prédictive brute (loi sur la sonde) et sa distance à la classe | marchepied, mesure de « ce qui change » | trompée par tout mélange aveugle |
| preuve | **log-richesse cumulée de la classe**, tests et tirages | redites, mérite | s'empoisonne si un tirage n'est pas frais (le juge l'interdit déjà) |
| cause | membre du nul dominant à la fin du test (« urne », « parent:A », « mélange des parents »…) | dire au proposeur pourquoi c'est tombé | grossière : un nom de membre, pas une explication |
| descripteurs | domaines, opérateurs, variables, signe, parents | archive qualité-diversité, recherche | à figer d'avance, sinon le pôle choisit ses propres cases |
| protocole | gabarit et sévérité | expérimentateurs | — |

La sonde est tirée une fois par domaine et gardée hors de la vue des agents : sinon un agent pourrait ajuster sa loi pour
s'éloigner de la classe sur la sonde seulement.

## 3. Qu'est-ce qu'une redite, et que faire

- Redite = même classe invariante. Trois politiques : (a) **refus** (v0) — tue aussi la version plus forte d'une bonne
  idée mal calibrée ; (b) **« déclarer ce qui change »** (v0) — contournable par un mot ; (c) **héritage de la preuve** —
  la redite d'une éliminée part d'une richesse sous 1 et doit la remonter ; celle d'une survivante est une réplication :
  elle peut confirmer ou faire tomber la survivante, jamais compter comme découverte.
- Sous le nul, le produit des e-valeurs d'une classe reste une e-valeur : Ville borne la promotion par α sur **toute** la
  suite des retentatives. Ce que coûte une fausse fusion : une perte de puissance (la vraie hypothèse part de plus bas),
  pas un refus définitif.

## 4. Ce qui améliore les propositions

- **Archive qualité-diversité** : cases = descripteurs figés ; dans chaque case, la meilleure survivante (par
  log-richesse), les éliminées avec leur cause. Le proposeur reçoit k entrées choisies par pertinence et par
  sous-exploration, pas l'archive entière.
- **Viser l'intermédiaire** (la piste « Boucle d'or » de Lazar, prise par le bon bout) : là où la chance de survie estimée
  est proche de la moitié, un test apprend le plus ; mais l'objectif reste les découvertes vraies par dollar sur les
  témoins (l'essai en cours le dira).
- **Mérite pondéré par la preuve** (log-richesse, pas la survie binaire), réplications avant de servir une survivante comme
  marchepied (contre l'empoisonnement par un faux positif), budget d'exploration réservé par génération (contre
  l'effondrement de la diversité), témoins plantés dans chaque génération.

## 5. La preuve qu'elle aide

- Avec de vrais agents seulement (les agents simulés ne lisent rien) : mémoire, sans mémoire, **mémoire placebo** (celle
  d'une autre course), même budget ; mesure : découvertes vraies sur témoins par dollar ; seuil écrit avant.
- En simulation, on peut mesurer la **valeur de l'information** que porte chaque encodage, avec un proposeur scripté qui
  l'utilise ; c'est ce que font les trois pistes ci-dessous.

## 6. Les trois pistes à essayer en simulation (dans `orchestrateur-pole-v2`, exploratoire)

1. **Détecteurs de redite**, sur une batterie de transformations : Jaccard du texte (v0) ; signature brute (piste de
   l'instance sortante) ; signature invariante. Mesures : redites manquées (copie renommée, jargon, échelle, mélange
   aveugle, biais par issue) et hypothèses vraiment différentes tuées à tort (même gabarit de texte, autre dépendance aux
   traits ; même ordre, effet plus fort).
2. **Registre de preuve contre refus contre rien**, avec un proposeur qui retente ses éliminées : taux de fausses
   découvertes sur témoins faux, et puissance sur les vraies hypothèses mal calibrées au premier essai.
3. **Proposeur scripté** qui lit la mémoire (archive qualité-diversité, visée intermédiaire) contre sans mémoire et contre
   mémoire placebo : découvertes vraies par dollar, redites, diversité.

Les seuils et lectures de chaque piste seront écrits et poussés avant son lancement, comme pour l'essai « Boucle d'or ».
