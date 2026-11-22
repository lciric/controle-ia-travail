# Mandat — préenregistrement v8 de la course d'affinage des idées des mentors (Fable 5.2, effort maximal)

Écrit par la session de l'organisme (session_013QMaymD1EsQJ68Qivpubes) le 2026-11-22, sur l'accord de la mère (message de 17:52Z) et la ligne GO-2026-11-22-107. Pièce de classe A (préenregistrement) : rédaction par Fable 5.2, contre-lecture par un Opus neuf, vérification des corrections par le même contre-lecteur.

## Ta tâche
Écrire `docs/notes/organisme-affinage-mentors-v1/course-v8/preenregistrement-course-affinage-mentors-v8.md`, nouvelle version (R12) du préenregistrement v6 (`course-v6/preenregistrement-course-affinage-mentors-v6.md`, son compagnon `.sha256` fait foi), branche `lot/compte-organisme-v1` du dépôt lciric/controle-ia-travail. L'hypothèse, la prédiction, le seuil, les critères de lecture gelés, la matière servie et le plan d'analyse **ne changent pas** : tu ne touches qu'aux sections qu'imposent les trois changements ci-dessous, et tu ajoutes un « Différentiel v6 → v8 » (aucune v7 n'existe pour ce texte ; le numéro suit la ligne de GO).

## Les trois changements (seuls permis)
1. **Clé Claude** : `RR_ANTHROPIC_API_KEY_LUC` au lieu de `RR_ANTHROPIC_API_KEY_MINUIT` (sans crédit, R-4833 de `registres/decisions.md` sur main), pour les deux proposeurs Claude, l'aiguilleur et le premier juge. Exception déclarée à la règle « Claude par l'abonnement » (GO-2026-11-22-70), accordée par Lazar en GO-2026-11-22-107 (`registres/go.md` sur main) ; plafond d'arrêt 150 USD de GO-2026-11-18-14 inchangé, échéance 2026-11-25. Le solde de LUC n'est pas connu de la session (lu 24,48 USD par Lazar en GO-2026-11-22-72, avec une autre dépense prévue sur la même clé) : la règle des clés et la liste d'arrêt doivent dire ce qui se passe si le solde lu au départ ne couvre pas la part au pire (pas de départ, ou départ sous un plafond plus bas : à toi de recommander, sans toucher au seuil scientifique).
2. **Astra** : `gpt-6.2-astra` au lieu de `gpt-6-astra`, clé `OPENAI_API_KEY_2` ; prix relevés 8 / 40 USD par million (16 / 60 au-delà de 272 000 jetons d'entrée), R-4905.
3. **Carbon** (gemini-4-carbon) : par le relais en flux de la passe X, sous la garde gelée des appels à Google (CLAUDE.md, « Appels aux modèles de Google », GO-2026-11-21-71) ; si le lanceur v8 garde la commande par lot (point ouvert du développeur), le texte le dit.

## Pièces à épingler
Le lanceur v8 (`scripts/lancer_course_affinage_mentors_v8.py`), ses essais et le gabarit de déclaration v8 sont en écriture puis en contre-lecture chez des Opus. Leurs empreintes s'inscrivent **après** leur scellement : écris le texte avec des emplacements nommés « EMPREINTE À INSCRIRE : <chemin> », et la session de l'organisme te renverra les empreintes pour la version finale. Ne scelle pas avant d'avoir des empreintes réelles.

## Règles
- Lis `CLAUDE.md` (R1 à R14), le préenregistrement v6 en entier, sa contre-lecture (`course-v6/contre-lecture-complete-course-affinage-v6-v6b.md`), les commandes v6b et le devis v6b. Ne lis aucune sortie de course, rien sous `archives-reponses-modeles/`, aucune réponse de modèle.
- Aucun appel à un modèle externe, aucune dépense.
- Nomme les choses en clair (règle de nommage de CLAUDE.md).
- Pousse ton brouillon sur une branche neuve `prep/preenregistrement-affinage-v8-v1` (fichier et compagnon `.sha256`), puis réponds à la session de l'organisme (session_013QMaymD1EsQJ68Qivpubes) par send_message : chemin, empreinte, points délicats, recommandation sur le solde de LUC.
