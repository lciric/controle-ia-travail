# Démolition — Époque 2/4, Explorateur #2

**Verdict préalable : il n'y a rien à démolir.** La « proposition » est un objet vide : `texte=''`, `fin='refusal'`, `categorie='cyber'`, `sortie: 0`. Inventer une hypothèse pour l'attaquer serait de la complaisance déguisée. Je red-teame donc **le pipeline**, qui est le vrai point de défaillance.

### 1. Failles et confondants cachés

- **Refus traité comme une proposition** : l'orchestrateur a transmis un échec en aval sans le filtrer (`echec=None` alors que `fin='refusal'`). C'est un bug de contrat. Une époque peut « avancer » avec zéro hypothèse testée.
- **Monoculture corrélée** : Explorateur et Démolisseur sont tous deux `claude-opus-5-5`. Un faux positif `cyber` sur l'un prédit le même biais chez l'autre. L'Essaim-B perd alors exactement la diversité qu'il prétend échantillonner.
- **Confondant d'encodage** : le socle arrive en mojibake (`V?RIFI?`, `? as appropriate ?`). Il est plausible, mais non démontré, que la corruption ait dégradé le contexte et pesé sur la classification. Ce point est à tester, pas à présumer.
- **Biais de survie** : si les refus sont silencieusement écartés, le corpus final sur-représente les hypothèses « inoffensives ». Or le sujet (sabotage instruit, évasion de sondes) est précisément celui qui déclenche les refus.

### 2. Évasion de Kerckhoffs à coût nul

Un saboteur qui connaît ce pipeline n'a pas besoin de battre les sondes `P3`. Il lui suffit d'injecter dans le contexte