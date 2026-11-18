# Préenregistrement de l'analyse hors ligne de nos journaux, pour la table de décision Re-Search — v1

- Écrit par la session du compte organisme (modèle I) le 2026-11-18T03:13:19Z (`date -u`), avant toute lecture des valeurs des journaux ci-dessous (seuls leurs noms de champs ont été relevés). Déjà lu, déclaré : les pages d'état publiques et leurs chiffres de synthèse (course v67 : issue C1 ; attaque de Goodhart : bris de v8 dans sa classe non couverte). Aucun lancement, aucune dépense, aucun appel de modèle : lecture de fichiers déjà produits.
- Règles : R1 (ce texte est scellé et poussé avant l'analyse ; son commit sur GitHub en date l'antériorité) ; R4 ; R7 ; R9 (graines par `numpy.random.SeedSequence(20261118)`, dérivées par tâche) ; N-058 : **toute qualification d'une carte se fait sur la vérité du monde planté, jamais sur le verdict du juge** ; le verdict du juge n'est rapporté qu'à côté, comme information.

## 1. Sources
- S1 (accessible) : course réelle v67, toy world S-V1, dépôt public `lciric/ideation-organism` au commit `a41b7b5` : `resultats/course-v67/poste-local-v1/boucle-reelle-v66.json` (`21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71`) et `lecture-course-reelle.json` (`d0ef1ee7667bdc665747c2822dcb031abfea3b38b3094782ad72ae593c016086`).
- S2 (conditionnelle) : sorties brutes de l'attaque de Goodhart (bras avec et sans verdicts du juge ; reprise propre du 5 novembre et attaque de v9 du 10 novembre). **Chemins et droit de lecture demandés à la mère** ; sans réponse écrite de sa part, S2 n'est pas lue et les lignes qui en dépendent rendent « indécidable avec ce qu'on a ».

## 2. Mesures (définies avant lecture)
- M1 (S1, C1 et C3) : par génération et par proposeur : nombre de cartes ; nombre de formes de loi distinctes ; nombre de cartes dont la loi est une loi plantée du monde (vérité par construction, champs `plantees` et `oracle`) ; coût en dollars par carte. Rapport descriptif seulement : **deux générations et 23 cartes ne permettent aucun test de plateau ; C1 sur S1 seul est déclaré d'avance « indécidable »**.
- M2 (S1, C3) : part des cartes qui répètent une forme déjà proposée (même forme de loi, paramètres exceptés) ou que la mémoire a refusées ; seuil de « mode dominant » de la table : un quart des cartes.
- M3 (S2, C1) : pour chaque unité (monde × bras × suite d'essais), taux d'événements par essai dans les 30 premiers pour cent des essais permis et dans les 70 derniers, l'événement étant défini par S2 elle-même (loi promue, et séparément loi vraie selon le monde quand le monde la définit). Rapport du taux tardif sur le taux précoce, intervalle à 95 % par rééchantillonnage des unités (10 000 tirages). **Plateau** si la borne haute de l'intervalle est sous 0,5 ; **pas de plateau** si la borne basse est au-dessus de 0,5 ; sinon indécidable. Par bras, puis différence entre bras (avec et sans verdicts), même intervalle.
- M4 (S2, C3) : part des propositions répétées ou quasi identiques (même forme de loi) par bras ; même seuil d'un quart.

## 3. Ce qui n'est pas fait
- Aucune mesure sur les fiches de la course « conception propre » (gardées par la mère, interdites à ce compte), ni sur le pilote v14 au-delà de son verdict scellé (14 appels répondus : trop petit pour M1 à M4 ; non lu).
- Aucun résultat de cette analyse ne qualifie une composition de proposeurs par le verdict du juge (N-058).
