# Contre-lecture 4 ciblée du volet A (pièces d'après la contre-lecture 3) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé après le commit e98497e9, rapport lu avant 12:23 UTC ; lecture seule (16 essais
passés : extraction v2, garde v2, lanceur v2 ; course v4 non relancée). Empreintes conformes. Remarques 2 à 11 de la contre-lecture 3
traitées ; 1 et 12 en partie ; aucune erreur bloquante nouvelle.

**Verdicts** : `volet_a_extraction_v2.py` **scellable en l'état** (crochet = `hidden_states[l+1]`, tenseur ou tuple, crochets internes
de `transformers` libérés par `finally`, égalité avec la v1 essayée) ; `volet_a_course_v4.py` **scellable en l'état** (indices de la
réutilisation corrects, base et retrait sur les mêmes exemples, audit (c) et sa règle, calcul par blocs égal au calcul direct,
`Ressources` identique en v3 et v4) ; `garde_depense_v2.py` après corrections mineures ; `volet_a_lancer_v2.py` après corrections
mineures ; `commande-volet-a-v2.md` après corrections (une moyenne) ; `depot_reduit_neuron_lens_volet_a_v3.py` **scellable en l'état**.

**Remarques**
5. Mineure — une exception de `lire_prix` (délai dépassé) fait mourir la garde : la rattraper, rendre NaN (le prix déclaré sert).
6. Info — sortie non JSON d'une instance détruite : vérification en échec à tort (code 4), sens prudent.
7. Info — état final rapporté deux fois.
8. Mineure — `MODULES` du lanceur sans `volet_a_course_v3.py` (importé par le chargement) : l'ajouter ou le déclarer.
9. Moyenne — `tmux` absent de l'image : `apt-get install -y git tmux`.
10. Mineure — devis optimiste : borne haute ≈ 5,5 h, ≈ 5 USD, jusqu'à 7 USD avec l'audit ; dire que le débit n'est pas mesuré.
11. Info — filtres, clone, contrôle de la carte, rappel, rapatriement, clé, arrêts par PID ou identifiant : traités et sûrs.
12. Info — empreintes des modules communs consignées, non comparées à des valeurs scellées : acceptable.
13. Info — le dépôt réduit contient tout ce que le lanceur et les essais importent.
