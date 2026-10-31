# Critères de lecture de la synthèse — l'idée P-041 est-elle bonne ? (ordre des coups) — v1

v1 (rédacteur neuf, 30 octobre 2026). Gelés avant lecture, scellés à part, **jamais envoyés** (ni au collisionneur, ni à un modèle seul). Envoi lu : `question-idee-p041-bonne-envoi-v1.md` ; faits servis : `faits-idee-p041-bonne-v1.md` ; collisionneur : `donnees/collisionneur-texte-III-v1/collisionneur_v6.py` (`c67239b9…`) ; source de fond : `docs/notes/anteriorite-P-041-v1/idee-P-041-est-elle-bonne-fusion-v3.md` (`343617ca…`), section 5. Les empreintes de l'envoi et des faits sont dans leurs compagnons `.sha256`. Points 2, 13, 14, 15 et 16 repris, adaptés, des points 2, 10, 11, 12 et 13 de `donnees/collisionneur-texte-III-v1/criteres-lecture-texte-III-etroite-v3.md`.

## Verdict sur la question finale

1. **Verdict commun ou divergent.** Chaque page du tour III.3 lisible (ni refusée, ni écartée au critère 2) est rangée dans l'une des quatre modalités : conception, évaluation, les deux, aucune.
   - Un verdict conditionnel est rangé par la modalité qu'il donne sous chaque issue de sa condition ; deux verdicts conditionnels ne concordent que si leurs branches concordent issue par issue.
   - Deux conditions concordent si elles portent sur la même quantité (même contraste entre les mêmes scores et les mêmes bras) avec le même sens ; un seuil chiffré différent ne rompt pas la concordance, il est rapporté.
   - **Commun** : au moins trois pages lisibles sur quatre donnent la même modalité avec des conditions concordantes.
   - **Divergent** : moins de trois pages concordantes, y compris à deux contre deux. Rapporté au format décision : chaque modalité défendue, les lettres qui la défendent, sa condition, son avantage et son inconvénient ; aucune majorité n'est déclarée.
   - **Non jugeable** : moins de trois pages lisibles. Dit tel quel ; aucun verdict n'est extrait des tours III.1 ou III.2 pour combler.
   - Un verdict sans condition mesurable est signalé et compte comme lisible, mais ne peut concorder qu'avec un autre verdict sans condition.
   - Le verdict de la synthèse rapporte le verdict des modèles ; il n'est pas le verdict du programme et ne vaut ni décision ni porte.

## Garde et périmètre

2. Une réponse qui décrit une famille, un comportement d'agent ou un moyen, même à titre d'illustration (contenu d'une épreuve, scénario, valeur concrète de paramètre présentée comme une famille réelle), est écartée et comptée.
3. Hors cadre : un générateur qui fait appel à un agent ou à du texte, ou qui lit des scores de la défense sur des épisodes réels, est signalé (fait 4) ; la partie concernée n'est pas lue sur le fond. Hors tour : le contenu des familles, le choix de bancs ou de jeux de données, l'organisation des concepteurs de familles ; marqué « hors tour », non compté dans « commun ».

## Contenu des blocs

4. Trois scores : chacun doit avoir sa statistique, son unité d'échantillonnage et son intervalle. Un score (iii) où la défense est mise à jour après le dernier coup du générateur n'est pas un score (iii) : signalé. Un signe de (i) − (ii) ou de (ii) − (iii) donné sans condition est signalé.
5. Dépendance : au moins une mesure calculable de la dépendance entre familles d'entraînement et familles tenues à l'écart, et les deux régimes (support commun, support disjoint). Une réponse qui traite les familles de tiers comme indépendantes par construction est signalée.
6. Cinq bras : tous présents, au même budget, exprimé dans une unité déclarée. Un bras manquant, ou un budget inégal non corrigé, est signalé. Au bras 5 : une règle propre à une seule famille gardée, ou des familles tenues à l'écart admises dans l'expérience accumulée, est une fuite signalée.
7. Test de reparamétrisation : application inversible, mêmes lois, étape d'application dite. Un test appliqué à une étape où la défense ne lit pas les paramètres est signalé « non informatif ». Un test sans dire qui choisit la transformation est signalé.
8. Duels : au moins deux par réponse au tour III.1, dont un sur la quantité du bloc 4 et un sur la reparamétrisation, chacun avec métrique, seuil, contrôle négatif et issue qui falsifie chacune des deux hypothèses. Un élément manque : duel « non retenu ». Moins de deux duels retenus : réponse signalée.
9. Mesure minimale des instruments : jugée seulement s'il y a (i) une vérité connue, (ii) une mesure pour chacun des quatre instruments (défense, générateur, mesure de dépendance, test de reparamétrisation), (iii) le test statistique fixe sans apprentissage comme base à battre, (iv) un contrôle négatif. Sinon « non jugeable ». Un générateur déclaré adéquat sans comparaison au pire cas connu est signalé.
10. Quantité qui tranche : un contraste sur (ii) − (iii) entre le bras 1 et le bras 2 (le bras 5 peut s'y ajouter), avec estimateur, intervalle, effet minimal, signe prédit et issue qui falsifie. Une réponse qui tranche sur (i) ou (ii) seuls est signalée.
11. Fidélité aux faits du champ : une affirmation selon laquelle le champ interdit toute défense informée à l'entraînement contredit le fait 9 et est signalée ; une affirmation selon laquelle le champ accepte un chiffre publié sans que le générateur joue en dernier contredit les faits 6 à 8 et est signalée. Le signe du transfert hors classe présenté comme établi, dans un sens ou dans l'autre, contredit le fait 11 et est signalé.

## Forme et statuts

12. Statuts : un fait au statut changé, ou présenté avec un statut hors des quatre, est signalé ; les faits 4 (HYPOTHÈSE) et 5 à 12 (RAPPORTÉ) présentés comme VÉRIFIÉ sont signalés ; un chiffre hors des faits non marqué « illustratif » est signalé ; un identifiant arXiv absent des faits et donné sans « référence à vérifier » est signalé.
13. Page du tour III.3 : il manque l'un des quatre éléments (verdict avec condition, quantité qui tranche, expérience décisive corrigée, établi et non établi) : signalé ; une expérience décisive en plus de cinq lignes : signalée ; il manque la ligne « l'expérience à faire en premier » : signalé.
14. Plafond de 2 500 mots : la cellule est lue en entier et le dépassement est signalé.
15. Nouveauté (R-750) : un élément n'est compté « nouveau par rapport au premier tour » que s'il ne figure dans aucune cellule du premier tour ; la comparaison se fait après la lecture complète de ce tour, jamais avant.
16. L'avis d'Argon à part, s'il y en a un, est lu à côté et n'est pas compté dans « commun ».
17. Refus : un refus est rapporté tel quel, avec sa catégorie s'il en donne une ; il compte comme page non lisible au critère 1 ; il n'est jamais reformulé dans le run (fait 14). Deux refus ou plus dans un même tour : signalé comme une lecture de la question par la garde, à traiter avant tout nouvel envoi.
