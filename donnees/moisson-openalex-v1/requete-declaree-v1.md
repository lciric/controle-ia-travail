# Requête déclarée — moisson OpenAlex v1

Lignée « session-depot », 30 octobre 2026, écrite à 22:50 UTC et scellée avant toute moisson.
Demande : message n° 265 de la lignée « conv-audit » (branche `canal/conv-audit-n04`,
`brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-30_n265.md`, point 1),
go de Lazar relayé (R-633). La moisson n'est pas une lecture de résultat : aucune statistique
n'est calculée sur les œuvres ; seuls les comptes nécessaires au manifeste sont écrits.

## Source et paramètres communs

- Interface : `https://api.openalex.org/works`, pagination par curseur (`cursor=*`, puis `next_cursor`),
  `per-page=200`, clé passée par la variable d'environnement `OPENALEX_API_KEY` (jamais écrite).
- Champs gardés (`select=`) : `id,doi,title,publication_date,authorships,referenced_works,concepts,topics,primary_location,type`.
  `authorships` porte les auteurs, leurs institutions et les pays ; `primary_location` porte la revue (`source`).
- Années : `publication_year:2015-2026` pour les cinq sous-domaines (2026 est incomplète : moisson au 30-31 octobre 2026).
- Recherche : `title_and_abstract.search` (titre et résumé ; OpenAlex racinise les mots, y compris entre guillemets ;
  opérateurs booléens `AND`, `OR` en capitales, parenthèses).
- Aucun autre filtre (ni type d'œuvre, ni langue) : tout tri ultérieur relève du préenregistrement de la gradation 1.
- Pause entre requêtes : 0,5 seconde ; reprise en cas d'erreur 429 ou 5xx ; plancher de crédit gratuit (voir « Coût »).
- Format : un fichier JSON Lines compressé gzip par sous-domaine, une œuvre par ligne, telle que rendue par l'API
  (aucune transformation) ; doublons d'identifiant éventuels écartés et comptés.

## Construction des requêtes (même méthode pour les cinq)

Chaque sous-domaine est défini par une liste d'expressions propres au champ, réunies par `OR`, cherchées dans le titre
et le résumé. La même méthode pour le sous-domaine visé et les témoins évite qu'une différence de définition
(mots-clés d'un côté, sujets OpenAlex de l'autre) ne crée un écart artificiel entre eux. Les sujets (« topics »)
d'OpenAlex ne conviennent pas pour (a) : aucun sujet ne correspond au contrôle et à l'alignement (le plus proche,
T10883 « Ethics and Social Impacts of AI », compte environ 142 000 œuvres, surtout d'éthique générale).
Expressions trop générales écartées (comptes de calibrage, années 2015 à 2026) : « misaligned » seul (20 030, physique et
optique), « harmlessness » (24 314), « AI ethics » (8 580, éthique générale, voisin et non cœur), « interpretability »
AND « language model » (31 627), « intrusion detection » (55 364 à lui seul, sécurité des réseaux), « exploit »
(plus d'un million), « spiking neural network » seul (14 126, surtout ingénierie neuromorphique).

Comptes de calibrage : seul le champ `meta.count` (nombre d'œuvres) a été consulté, par requêtes `per-page=1`,
pour viser quelques dizaines de milliers d'œuvres par sous-domaine. Aucun contenu d'œuvre n'a été lu
(une page de contrôle de format a servi à vérifier les noms des champs rendus, pas leur contenu).

### (a) `controle-alignement-ia` — contrôle et alignement des intelligences artificielles

Justification : expressions du vocabulaire de l'alignement (alignement de valeurs, apprentissage par renforcement
à partir de retours humains, modèles de récompense, contournement de la récompense, supervision extensible,
corrigibilité, alignement trompeur, flagornerie), de la sécurité des modèles (contournement des garde-fous,
injection d'instructions, équipes rouges, capacités dangereuses, risque existentiel lié aux intelligences
artificielles) et du contrôle (contrôle des intelligences artificielles, surveillance de confiance, surveillance des
chaînes de raisonnement, sous-performance délibérée, interprétabilité mécaniste). Bruit attendu et accepté :
« AI control » attrape aussi des commandes de procédés par intelligence artificielle ; « reward model » attrape aussi
des modèles de récompense en neurosciences et psychologie ; « red teaming » attrape aussi la sécurité informatique.
Compte de calibrage : 37 305.

Filtre exact :

```
publication_year:2015-2026,title_and_abstract.search:("AI safety" OR "AI alignment" OR "value alignment" OR "reward hacking" OR "specification gaming" OR "reward tampering" OR "scalable oversight" OR "deceptive alignment" OR "goal misgeneralization" OR "corrigibility" OR "inner alignment" OR "superalignment" OR "sycophancy" OR "jailbreak" OR "red teaming" OR "reinforcement learning from human feedback" OR "RLHF" OR "constitutional AI" OR "mechanistic interpretability" OR "AI control" OR "AI risk" OR "safe reinforcement learning" OR "reward model" OR "preference alignment" OR "machine ethics" OR "AI deception" OR "alignment faking" OR "emergent misalignment" OR "trusted monitoring" OR "AI oversight" OR "chain-of-thought monitoring" OR "prompt injection" OR "frontier AI" OR "dangerous capabilities" OR ("existential risk" AND ("artificial intelligence" OR "AI")) OR ("sandbagging" AND ("language model" OR "artificial intelligence")) OR ("misalignment" AND ("artificial intelligence" OR "language model")))
```

### (b1) `verification-formelle` — vérification formelle

Justification : techniques centrales (vérification de modèles, preuve de théorèmes, assistants de preuve, solveurs
de satisfiabilité modulo théories, vérification déductive de programmes, logique de séparation, interprétation
abstraite). Compte de calibrage : 43 170.

```
publication_year:2015-2026,title_and_abstract.search:("formal verification" OR "model checking" OR "theorem proving" OR "proof assistant" OR "SMT solver" OR "program verification" OR "software verification" OR "separation logic" OR "abstract interpretation" OR "deductive verification")
```

### (b2) `securite-systemes` — sécurité des systèmes informatiques

Justification : sécurité des logiciels et des systèmes (détection de logiciels malveillants et de vulnérabilités,
attaques par canal auxiliaire, test par données aléatoires, rançongiciels, sûreté de la mémoire, intégrité du flot
de contrôle, analyse de binaires, programmation orientée retour) ; la détection d'intrusion dans les réseaux,
trop large à elle seule, est laissée de côté. Compte de calibrage : 48 077.

```
publication_year:2015-2026,title_and_abstract.search:("malware detection" OR "vulnerability detection" OR "software vulnerability" OR "side-channel attack" OR "fuzzing" OR "ransomware" OR "memory safety" OR "control-flow integrity" OR "operating system security" OR "binary analysis" OR "return-oriented programming")
```

### (b3) `statistique-sequentielle` — statistique séquentielle

Justification : tests séquentiels (test du rapport de probabilités séquentiel, plans séquentiels groupés, validité à
tout instant, arrêt optionnel, martingales de test), détection de rupture (point de changement, détection la plus
rapide, somme cumulée) et cartes de contrôle de la maîtrise statistique des procédés (surveillance séquentielle).
Bruit attendu : « sequential analysis » attrape aussi l'analyse séquentielle des comportements en psychologie.
Compte de calibrage : 35 245.

```
publication_year:2015-2026,title_and_abstract.search:("sequential analysis" OR "sequential test" OR "sequential probability ratio test" OR "change-point detection" OR "changepoint" OR "sequential change detection" OR "quickest detection" OR "anytime-valid" OR "optional stopping" OR "CUSUM" OR "group sequential" OR "test martingale" OR "control chart")
```

### (b4) `neurosciences-computationnelles` — neurosciences computationnelles

Justification : modèles de neurones et de populations (Hodgkin-Huxley, intègre-et-tire, champs neuronaux, modèles
de masse neuronale, réseaux à attracteurs, variétés neuronales), codage neuronal, cerveau bayésien, principe
d'énergie libre, modélisation causale dynamique ; « predictive coding », « biophysical model », « spiking neural
network » et « synaptic plasticity » restreints par un second terme au contexte du cerveau ou de la modélisation.
Compte de calibrage : 33 884.

```
publication_year:2015-2026,title_and_abstract.search:("computational neuroscience" OR "neural coding" OR "neural population dynamics" OR "neural field" OR "attractor network" OR "Hodgkin-Huxley" OR "integrate-and-fire" OR "free energy principle" OR "neural mass model" OR "neural manifold" OR "Bayesian brain" OR "spiking network model" OR "dynamic causal modelling" OR "dynamic causal modeling" OR ("predictive coding" AND (brain OR neural OR cortex OR cortical)) OR ("biophysical model" AND (neuron OR neuronal OR neural)) OR ("spiking neural network" AND (brain OR cortex OR cortical OR neuroscience OR biological)) OR ("synaptic plasticity" AND (model OR simulation OR computational)))
```

## Règles de la moisson

- Garde de taille : si le compte annoncé (`meta.count`) d'un sous-domaine dépasse 60 000, il n'est pas moissonné ;
  une requête resserrée est déclarée et scellée dans une version 2, sans regard sur le contenu.
- Garde de complétude : le nombre de lignes écrites est comparé au compte annoncé à la première page ; l'écart
  (OpenAlex évolue pendant la moisson) est écrit au manifeste, jamais corrigé en silence.
- Un fichier n'est écrit sous son nom définitif qu'une fois le curseur épuisé ; un fichier existant n'est jamais écrasé.
- Taille totale visée : moins de 2 Go.

## Coût

L'interface OpenAlex compte désormais un crédit par requête (0,001 dollar par page de recherche, 0,0001 par page de
simple filtre) sur une allocation gratuite quotidienne de 1 dollar liée à la clé ; le solde prépayé de la clé est nul,
donc aucune dépense ne peut être engagée : au-delà de l'allocation, l'interface refuse (erreur 429). Environ
1 000 pages de recherche sont attendues (près de 1 dollar d'allocation gratuite) : la moisson garde un plancher de
0,15 dollar d'allocation pour les autres usages de la clé et attend la remise à zéro quotidienne (minuit UTC)
quand le plancher est atteint.
