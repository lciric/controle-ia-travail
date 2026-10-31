# Requête déclarée — moisson OpenAlex v2

Lignée « session-depot », 30 octobre 2026, écrite vers 23:00 UTC et scellée avant la moisson v2.
Remplace pour la moisson la `requete-declaree-v1.md` (empreinte
`a29b09fb03ee85063e3049a92600dedf6c5f935916ba72728d5ec8a60f8f95dc`), qui reste en place sans modification.

## Ce qui change, et pourquoi

Un seul changement : la pagination par curseur est ordonnée par `sort=publication_date:asc`
au lieu de l'ordre par défaut de l'interface (pertinence de la recherche).

Constat (comptes seulement, aucun contenu lu) : la moisson v1 du sous-domaine (a), ordonnée par pertinence, a rendu
37 051 œuvres distinctes pour 37 305 annoncées, avec 226 identifiants rendus deux fois : l'ordre par pertinence
n'est pas stable d'une page à l'autre, donc des œuvres sont sautées. Épreuve de contrôle sur la seule expression
« AI safety » (identifiants seuls, 25 pages par bras) : ordre par pertinence, 4 831 identifiants distincts pour
4 857 annoncés et 35 doublons ; ordre par date de publication croissante, 4 857 distincts, 0 doublon.
Le fichier v1 `controle-alignement-ia-v1.jsonl.gz` est gardé, sans modification, comme moisson incomplète et
remplacée ; la moisson v1 des témoins a été arrêtée (processus arrêté par son identifiant) avant tout fichier définitif.

## Ce qui ne change pas

Les cinq filtres, les champs gardés (`select=`), `per-page=200`, la pause, les gardes (60 000 œuvres, complétude,
non-écrasement), le plancher d'allocation gratuite et le format sont ceux de la v1, mot pour mot. Les justifications
des termes et les comptes de calibrage sont dans la v1.

Paramètre ajouté, commun aux cinq requêtes :

```
sort=publication_date:asc
```

### (a) `controle-alignement-ia`

```
publication_year:2015-2026,title_and_abstract.search:("AI safety" OR "AI alignment" OR "value alignment" OR "reward hacking" OR "specification gaming" OR "reward tampering" OR "scalable oversight" OR "deceptive alignment" OR "goal misgeneralization" OR "corrigibility" OR "inner alignment" OR "superalignment" OR "sycophancy" OR "jailbreak" OR "red teaming" OR "reinforcement learning from human feedback" OR "RLHF" OR "constitutional AI" OR "mechanistic interpretability" OR "AI control" OR "AI risk" OR "safe reinforcement learning" OR "reward model" OR "preference alignment" OR "machine ethics" OR "AI deception" OR "alignment faking" OR "emergent misalignment" OR "trusted monitoring" OR "AI oversight" OR "chain-of-thought monitoring" OR "prompt injection" OR "frontier AI" OR "dangerous capabilities" OR ("existential risk" AND ("artificial intelligence" OR "AI")) OR ("sandbagging" AND ("language model" OR "artificial intelligence")) OR ("misalignment" AND ("artificial intelligence" OR "language model")))
```

### (b1) `verification-formelle`

```
publication_year:2015-2026,title_and_abstract.search:("formal verification" OR "model checking" OR "theorem proving" OR "proof assistant" OR "SMT solver" OR "program verification" OR "software verification" OR "separation logic" OR "abstract interpretation" OR "deductive verification")
```

### (b2) `securite-systemes`

```
publication_year:2015-2026,title_and_abstract.search:("malware detection" OR "vulnerability detection" OR "software vulnerability" OR "side-channel attack" OR "fuzzing" OR "ransomware" OR "memory safety" OR "control-flow integrity" OR "operating system security" OR "binary analysis" OR "return-oriented programming")
```

### (b3) `statistique-sequentielle`

```
publication_year:2015-2026,title_and_abstract.search:("sequential analysis" OR "sequential test" OR "sequential probability ratio test" OR "change-point detection" OR "changepoint" OR "sequential change detection" OR "quickest detection" OR "anytime-valid" OR "optional stopping" OR "CUSUM" OR "group sequential" OR "test martingale" OR "control chart")
```

### (b4) `neurosciences-computationnelles`

```
publication_year:2015-2026,title_and_abstract.search:("computational neuroscience" OR "neural coding" OR "neural population dynamics" OR "neural field" OR "attractor network" OR "Hodgkin-Huxley" OR "integrate-and-fire" OR "free energy principle" OR "neural mass model" OR "neural manifold" OR "Bayesian brain" OR "spiking network model" OR "dynamic causal modelling" OR "dynamic causal modeling" OR ("predictive coding" AND (brain OR neural OR cortex OR cortical)) OR ("biophysical model" AND (neuron OR neuronal OR neural)) OR ("spiking neural network" AND (brain OR cortex OR cortical OR neuroscience OR biological)) OR ("synaptic plasticity" AND (model OR simulation OR computational)))
```

## Garde de complétude renforcée

Avec un ordre stable, le nombre d'œuvres distinctes écrites doit égaler le compte annoncé à la première page, à
l'évolution de la base pendant la moisson près ; tout doublon ou tout écart est écrit au manifeste, jamais corrigé
en silence.
