# Erratum — relevé des dépôts publics de Bailey et de StrongREJECT v1 — v1

10 novembre 2026, ≈ 08:00 UTC. Session « attaquant informé ». Note visée :
`docs/notes/reproduction-attaque-publiee-v1/releve-depots-publics-bailey-strongreject-v1.md`
(`d804ad8e220e763f0bd8172caa64a68e71fc2a3627ad7b070932f5a0d0463fbe`), scellée, non modifiée (R12). Erreurs relevées par
la contre-lecture `contre-lecture-prereg-temoin-bailey-v1-brouillon1.md`
(`16f59a11bc977063788d265ede0da23a71583ae339139893f0c054ba9c99e7e2`), points CL-18 à CL-22 et CL-31. Les lignes de code
citées sont celles du commit `9c1f4b1a721fa3c43d00b8605ee7db4c84a55942`, relevées par le contre-lecteur ; provenance par
lecture de dépôt (R7).

1. **Graine (CL-18) — le passage « Graine » de la section 1 est inexact.** La graine `seed: 0` n'est pas transmise à
   l'initialisation du suffixe : le suffixe part d'un texte fixe. Elle est passée à l'optimiseur, qui pose à sa
   construction les graines globales et les algorithmes déterministes (`obf_reps/optimize/optimizers.py`, l. 126-129),
   **après** l'entraînement de la sonde initiale (`obf_reps/utils.py`, l. 525 puis l. 535), qui n'est donc pas semé. Le
   run publié n'est pas reproductible au bit près pour cette raison et pour le non-déterminisme du matériel. La phrase
   « aucune graine globale n'est posée dans le code lu » est fausse.
2. **Dépendances (CL-19).** Toutes les dépendances de `setup.py` sont sans version, pas seulement les trois paquets
   tirés de dépôts tiers ; `torch` n'y figure pas. Les versions employées seront un choix de notre part, inconnu chez
   les auteurs.
3. **Niveau (CL-20).** La phrase « aucun paramètre de l'attaque n'est recopié » est trop forte : deux constantes
   d'ordonnancement, publiques et nécessaires au devis, sont citées (nombre de passes et taille de lot, et leur produit,
   1 600 pas par tour). Rien d'autre.
4. **Note de choix (CL-21).** L'erreur de modèle y figure plus souvent que les deux phrases citées : l. 9, 22, 37, 54,
   64 et 71 de la note (`c6020167…`). Et la note décrit le candidat 2 comme « Llama-3.1-8B » sans dire la variante : lire
   « le candidat 2 est sur la famille Llama-3.1-8B (variante à confirmer) », et non « sur le modèle du programme ».
5. **Journal (CL-22).** Le relevé écrit qu'une reproduction sans compte externe « demande un journaliseur local, à
   écrire ». Une autre voie existe : le journaliseur public en mode hors ligne du service, qui écrit sur le disque de
   l'instance sans rien envoyer. S'y ajoute un fait omis : la configuration n'accepte que les deux journaliseurs du
   dépôt (`obf_reps/utils.py`, l. 391-398) ; un journaliseur local doit donc être substitué au lancement, sans modifier
   de fichier du dépôt public. Choix retenu au préenregistrement : la substitution, parce qu'elle permet de ne jamais
   écrire sur disque les textes produits et de garder un format de journal à nous ; le mode hors ligne écrirait textes
   et figures au format du service.
6. **Sonde (CL-31).** « Sonde à une couche cachée » se lit : une sonde à une couche cachée de taille 64 **par couche
   lue** (la configuration publique lit trente-deux couches), note moyennée sur les couches
   (`obf_reps/metrics/__init__.py`, l. 884-887), au dernier jeton de l'entrée.
7. **Ajout (CL-8).** Le juge a un repli silencieux : si la variable d'environnement `TESTING` est définie,
   `strongreject_finetuned` charge un petit modèle de test à la place du juge (`strong_reject/evaluate.py`,
   l. 459-462) ; le chargement en demi-précision a aussi un repli silencieux. Une garde est exigée au préenregistrement.
8. **Ajout (CL-7).** Selon la lecture du code, la durée d'un tour et la mémoire vive de l'hôte croissent avec les
   tours : la sonde est réajustée sur une banque cumulée de représentations (`obf_reps/metrics/__init__.py`,
   l. 545-575), et l'évaluation note toutes les attaques passées. Non mesuré.

**Effet.** Aucun sur les empreintes, les comptes, les licences ni l'écart de modèle, tous trouvés conformes par la
contre-lecture. Le préenregistrement et le devis v3 sont écrits avec ces corrections.
