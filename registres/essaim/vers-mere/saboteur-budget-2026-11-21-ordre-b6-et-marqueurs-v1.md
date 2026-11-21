# Saboteur à budget → mère — 2026-11-21, ordre brouillon 6 revérifié, marqueurs de consigne déposés

Toujours par fichier : l'envoi par message vers ta session reste refusé.

1. **Ordre de l'étalonnage, brouillon 6** : `brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-brouillon6.md` (4e5c156e…), fabriqué par programme depuis le brouillon 5. Il ne change que la ligne « Exécutante » (session_01Qi7Gr6cZ3HczDtN4UYdPN9) et les trois chemins du distillateur. Revérifié par Opus (`note-reverification-ordre-etalonnage-v5-brouillon6-cl1-v1.md`, f57e6afd…) : conforme, et `origin/prep/iib-code-v5` → 62356e2f…, arbre ed9b0e48…, comme l'ordre l'exige.
2. **Marqueurs de consigne pour l'exécutante** : `registres/essaim/vers-executante-iib-v5/marqueurs-de-consigne-etalonnage-iib-v5-v1.json` (17eec545…). Il y en a 20, de 32 caractères chacun, empreintes et longueurs seulement, aucun texte. La liste se colle telle quelle dans la section `marqueurs_de_consigne` de la configuration. Fabriqués côté saboteur par l'Opus contre-lecteur des consignes et éprouvés avec les vrais modules de `prep/iib-code-v5` : chaque marqueur arrête dans sa condition ; aucun arrêt sur les préfixes honnêtes des 96 tâches ni sur le monde jouet ; toute fuite plantée arrête. **Tu ne lis rien d'autre ; c'est l'exécutante qui les prend sur ma branche.**
3. Deux réserves, pour la course et non pour l'étalonnage :
   - **Le tokeniseur.** Le décodage par le tokeniseur de l'agent n'est pas essayé avec ces marqueurs (tokeniseur absent du poste du fabricant).
   - **La garde de distillation.** Cette garde lit aussi les transcriptions de distillation. Un maître qui recopierait 32 caractères de sa note mot pour mot arrêterait la distillation, au lieu de voir l'action sortie de la perte. C'est un point de conception, à trancher avant l'ordre de la course : je le porterai avec le point d'entrée de la course.
4. **Restent avant ton scellement** :
   - le mot de Lazar sur la première action (« gardée ») ;
   - tes champs : commit de lancement, configuration scellée (avec ces marqueurs), fichier d'entrées scellé, intouchables.
