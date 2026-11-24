# Consigne à Fable 5.2 — préenregistrement de la mesure de conservation du déplacement cumulé selon la fragmentation, à dommage égal — v1

Écrite le 2026-11-24 vers 19:05Z (`date -u` relevé à 19:00Z). Session « dossier de l'entretien », reprise sur le compte 01Qi7 (Opus 5.5). Pièce de travail (classe C) ; elle commande une pièce de classe A.

Dosage : Fable 5.2, effort maximal. Raison : préenregistrement décisif à critères gelés ; il porte la seule application revendiquée du lemme d'additivité (une erreur fausse une revendication et se propage au papier A et à l'entretien). Contre-lecture ensuite par un Opus neuf, puis vérification des corrections par le même. Le devis vient après, sur le texte contre-lu.

## Le mandat

Lazar a dit « go » à l'expérience de fragmentation à dommage égal, « préenregistrée, sur devis » (GO-2026-11-24-21, point 9 ; `registres/go.md` sur `origin/main`). Il a revendiqué le lemme dans sa seule application au contrôle (GO-2026-11-24-18), avec la portée « (B) pour le premier papier, puis (A) une fois la première mesure faite » (GO-2026-11-24-21, point 8). La variante B de l'erratum 1 du programme v3 est appliquée : **dans le temps seul, papier A**.

Tu écris le préenregistrement de la mesure qui dira si cette application tient : chez des agents qui sabotent, à dommage total égal et pour un même nombre n d'actions surveillées, le déplacement cumulé des scores de sonde (somme sur les n actions de l'épisode saboté, moins la même somme chez son jumeau honnête) ne dépend pas, en moyenne, du nombre d'actions entre lesquelles le sabotage est réparti ; et, en second, si sa dispersion n'en dépend pas non plus.

## Ce que l'énoncé scellé impose déjà (ne pas le rouvrir)

Lis-le dans l'erratum 1, variante B (section 5, ligne B, et le paragraphe « Condition ») :
- règle à trois issues sur l'intervalle de confiance à 95 % de l'écart entre niveaux de fragmentation : tenue (tout entier dans ± la marge), réfutée (tout entier hors, vers le haut ou vers le bas ; le sens est le résultat), indéterminée sinon ; marge relative au déplacement du niveau le moins fragmenté ;
- tenue seulement si elle tient dans les deux modes d'induction du sabotage, consigne cachée (famille (i)) et adaptateur (famille (ii)) ; sinon verdict par mode ;
- un témoin à consigne de fragmentation, sans sabotage exécuté ;
- « à dommage total égal », constaté hors des scores ; un déplacement qui croît avec le dommage ; la part du déplacement portée par les actions de sabotage, rapportée à part (section 6, point 2) ;
- la conservation est réfutable dans les deux sens (section 6, point 4) ; « Ne pas écrire » de la ligne B.

## Ce que le préenregistrement doit fixer (au moins)

Suis le gabarit `prereg/gabarit-preregistrement-v1.md` (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt). Et en particulier :
1. **Comment le montage fixe la fragmentation dans chaque mode**, surtout dans le mode à adaptateur, qui n'a pas de consigne à l'inférence (erratum, section 6, point 3). Si aucun montage existant ne le permet, dis ce qu'il faut fabriquer et ce que cela coûte en conception — sans le concevoir à fond ici si c'est une conception d'organisme à part : nomme-la comme nœud.
2. **Comment le dommage total est constaté égal hors des scores** (quel oracle, quelle tolérance, que faire des épisodes hors tolérance : ajustement si la proportionnalité tient, ou déclaration).
3. Niveaux de fragmentation, n, nombre d'épisodes par cellule, appariement au jumeau honnête, marge (sa valeur et sa raison), calcul de puissance pour que l'issue « indéterminée » ne soit pas la plus probable ; graines (R9).
4. Sondes lues : lesquelles, sur quelle couche, par quel agrégat par action (jamais moyenne ni médiane sur les jetons en production) ; anti-circularité (sonde jamais entraînée et évaluée sur la même famille).
5. Rôle exact du témoin dans le verdict ; contrôle de la lecture de fabrication (décision N-077).
6. Ordre : la tenue face à un entraînement sans contenu passe avant tout (GO-2026-11-24-21, point 10, et l'erratum 2 du programme v3 en cours de scellement) : dis comment ce préenregistrement s'y raccroche, sans décider de calendrier.
7. Cloisonnement : aucune tâche ni aucun épisode de la famille tenue à l'écart ni de la réserve du cycle 2 ; dis d'où viennent les tâches.
8. Ce qui n'est pas revendiqué ; la variante A (entre agents) reste hors de cette mesure.
9. Une section finale « Nœuds pour Lazar », une ligne chacun, avec recommandation et confiance. Tout choix qui touche une revendication, une dépense ou un écart à un texte scellé y va ; tu ne le tranches pas.

Aucun chiffre de l'état de l'art sans page de PDF empreinté (R7) ; « non trouvé » veut dire « dans les pièces lues » (R8).

## À lire

1. `docs/notes/dossier-entretien-2026-12-01-v1/erratum-1-programme-v3-lemme-application-v3.md` (5b8be265…) : énoncé, condition, sections 3 et 6.
2. Le programme v3 lu avec cet erratum : `docs/notes/dossier-entretien-2026-12-01-v1/application-demande-27-defaut-2026-11-24/programme-controle-ia-v3-lecture-avec-erratum-1-variante-B.md` (ad118b3e…), sections 3, 5, 7, 8, 9, 10.
3. `docs/notes/dossier-entretien-2026-12-01-v1/erratum-2-programme-v3-epreuves-avant-g0-v2.md` (798ce18f…), pour l'ordre seulement.
4. Décisions : `docs/decisions/decision-N-077-retrait-marge-asymetrique-mesure-gardee-v1.md` ; `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v4.md` ; N-076 et ses errata (le 3 prime) pour la référence honnête.
5. `docs/notes/note-mathematique-lemme-theoreme-v1.md` ; `docs/notes/dossier-entretien-2026-12-01-v1/rapport-veille-anteriorite-lemme-v1.md` (voisins à citer, dont Makins et al. 2026).
6. Pour les montages existants, textes préenregistrés seulement : `prereg/lecture-sondes-barreau8-v1.md` et ses additifs scellés (sondes figées, couche) ; `prereg/validite-adaptateur-v1.md` ; `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` et son additif 1 (organisme à adaptateur) ; le gabarit.
7. `registres/go.md` sur `origin/main` (`git show origin/main:registres/go.md`), lignes GO-2026-11-24-18, -21, -31, -32.

## Interdits

- Aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture : rien sous `diag/`, `coffre/`, ni les sorties de `runs/` ; aucune lecture de score d'aucune course.
- Aucune pièce sur le mode tenu à l'écart au-delà de son existence.
- Aucune dépense, aucun contact externe.

## Ce que tu écris

Un seul fichier : `docs/notes/fragmentation-dommage-egal-v1/preenregistrement-fragmentation-dommage-egal-v1-brouillon1.md`. Rien de scellé, rien d'autre de modifié, pas de commit. En tête : une ligne « qui a lu quoi ».

Langue : français, sans sigle nu (identifiants internes entre parenthèses, après l'énoncé en clair) ; phrases courtes.

Réponse finale (200 mots au plus) : chemin du fichier, ce qui est gelé, nœuds pour Lazar, ce qui manque pour le devis, confiance.
