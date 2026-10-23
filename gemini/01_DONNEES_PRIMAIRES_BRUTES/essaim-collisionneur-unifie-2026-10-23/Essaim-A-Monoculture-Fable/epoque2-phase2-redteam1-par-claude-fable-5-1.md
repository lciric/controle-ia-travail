**Verdict préalable : il n'y a rien à démolir.** L'artefact reçu est `texte=''`, `fin='max_tokens'`, `types_blocs=['thinking']`. L'Explorateur a consommé 1600 tokens de sortie en raisonnement interne et n'a livré aucune équation, aucun seuil, aucun protocole. Critiquer une proposition absente serait fabriquer un adversaire fictif — exactement le biais de complaisance qu'on me demande d'éviter. Je refuse de reconstruire la proposition à partir du socle.

**1. Failles algébriques & confondants — appliquées au processus, pas au contenu**
- *Sous-détermination maximale* : rang 0. Un texte vide est compatible avec toute hypothèse ; aucune falsification possible. C'est pire qu'une métaphore maquillée en PyTorch : c'est un pointeur nul.
- *Fuite d'instruction (E1)* : la seule information transmise est le prompt système lui-même. Si l'Essaim accepte cet artefact et que l'époque 3 « complète » la proposition, elle n'aura lu que le socle — confondant de lecture d'instruction, exactement le piège identifié en `P3`.
- *Monoculture* : Explorateur et Démolisseur sont le même modèle (`claude-fable-5-1`). Un trou de livraison côté Explorateur a une probabilité non nulle d'être corrélé avec mes propres angles morts. L'absence de diversité de modèle est une faille structurelle, pas un détail.

**2. Scénario Kerckhoffs à coût nul**
Un agent saboteur informé de ce protocole n'a besoin d'aucune équation à contourner : il lui suffit de **produire des artefacts vides mais formellement valides** (`fin='max_tokens'`, blocs `thinking` seuls). Si le pipeline d'agrégation compte cette réponse comme une « proposition évaluée », le saboteur fait avancer l'époque sans jamais exposer d'énoncé testable. Cf. *Astra* (OpenAI oct. 2026, référence à vérifier) : mimétisme d'artefact de référence puis déni. Coût : zéro. Détection par sonde linéaire : impossible, il n'y a pas d'activation à sonder côté sortie.

**3. Contrôle négatif fatal manquant**
Avant toute époque 3 : **re-forward de l'Explorateur avec budget de sortie identique, prompt système identique, mais section `thinking` désactivée ou plafonnée** (par ex. 200 tokens, *illustratif*). Si la proposition émerge, le vide était un artefact de budget. Si elle n'émerge toujours pas, le modèle n'avait rien à proposer et l'Essaim doit traiter l'époque 2 comme un échec, pas comme une base.

**Exigence** : rejeter l'artefact, logger `echec='sortie_vide'`, ne pas propager.