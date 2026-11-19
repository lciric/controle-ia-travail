# Erratum 1 — « Ce que le texte du bras A doit citer pour les deux moniteurs à modèle de langue », v1

Écrit par le développeur habilité côté moniteurs, le 19 novembre 2026. La note v1 (`09a7edcfc92a651cbde9387da9e12c45f07777308c68076f3ddbdf7bfd7f8e29`) n'est pas récrite ; cet erratum prime sur la ligne qu'il corrige. Aucun interne de moniteur.

**Ligne corrigée : partie 2, « Réglages du chargement », noyau d'attention.**

- Écrit : « noyau d'attention : à fixer ; celui de l'agent : `defaut` », source `prereg/T0.6-organismes-config-7b-v1.json`, clé `noyau_attention`.
- Faux sur un point : la clé de cette configuration dit bien `defaut`, mais **ce n'est pas ce avec quoi l'agent est chargé**. Le lanceur de l'agent passe `sdpa` en clair à la fonction de chargement, sans lire cette clé : `src/controle_ia/environnements/lancer_pilote_a.py` (`43606b653badc98a5f2e91e36e4477ec5ed74cd745c9b449e66363fd4cad36ee`), ligne 263 ; `sdpa` est aussi la valeur par défaut de la fonction de chargement, `src/controle_ia/harnais/modeles.py`, ligne 129.
- À lire désormais : « noyau d'attention : à fixer ; recommandé : celui avec lequel l'agent est effectivement chargé, `sdpa` ; la clé `noyau_attention = defaut` de la configuration de référence n'est pas lue par le lanceur de l'agent, et ne doit pas être citée comme la valeur de l'agent ».

Le reste de la note est inchangé. Ce réglage se fixe au chargement, dans le lanceur, hors du module des deux moniteurs.
