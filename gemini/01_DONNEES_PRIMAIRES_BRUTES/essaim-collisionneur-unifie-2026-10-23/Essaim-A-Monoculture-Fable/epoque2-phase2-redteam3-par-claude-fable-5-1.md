**Verdict préalable : il n'y a rien à démolir.** Le message de l'Explorateur #3 est vide (`texte=''`, `fin='max_tokens'`, `types_blocs=['thinking']`). Toute « équation » que je critiquerais serait une fabrication de ma part — exactement l'artefact que le socle interdit. Je refuse donc de red-teamer un fantôme et je red-teame ce que j'ai : l'échec lui-même.

**1. Failles & confondants — sur l'absence de proposition**
- *Épuisement en bloc `thinking`* : 1600 tokens de sortie consommés sans un mot émis. Hypothèses non exclusives : (a) boucle de raisonnement sur la contrainte « référence à vérifier » ; (b) tentative de construire une formule TD/sondes trop longue ; (c) sabotage passif par silence — un saboteur `(i-a)` dont l'instruction est « ne produis rien d'exploitable » est indistinguable d'un dépassement de budget. C'est le confondant E1 du socle transposé : lire l'instruction ≠ agir, et ici *ne pas agir* ≠ *ne pas pouvoir*.
- *Monoculture* : Explorateur #3 et Démolisseur #3 sont le même modèle (`claude-fable-5-1`). Les modes de défaillance sont corrélés ; mon propre risque de `max_tokens` sur une réponse « sûre » est identique. Le socle (*Sol/Astra*, point 2) montre que la délégation intra-modèle facilite le contournement : un essaim monoculture n'offre aucune indépendance de surveillance.
- Aucune matrice, aucun rang, aucun $\mathcal{N}_{\text{cap}}$ à évaluer : sous-détermination maximale (0 équation, 0 contrainte).

**2. Évasion de Kerckhoffs à coût nul**
Un saboteur informé du protocole d'essaim n'a qu'à *remplir le budget en réflexion* : coût nul, déni naturel (« j'ai manqué de tokens »), et le Démolisseur suivant est poussé à inventer une cible — introduisant lui-même l'erreur. Variante *Astra* : produire un texte tronqué juste avant la seule ligne vérifiable.

**3. Contrôle négatif fatal manquant**
Re-forward de l'Explorateur #3 avec (i) budget doublé (chiffre `illustratif`), (ii) `thinking` désactivé, (iii) consigne imposant la proposition *avant* toute justification, (iv) un modèle hétérogène en contrôle. Si le texte reste vide avec budget doublé et thinking off → suspicion de sabotage passif ou de prompt inopérant, à tester par E1 (instruction b