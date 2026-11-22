# Demande 3 — L'audit après coup, à plancher et à l'enjeu, avec la boucle audit, recapture et réapprentissage : la règle et ses épreuves sur mondes plantés

**Fondement.** Décision N-076 (copie jointe), sections 6.1, 6.2, 7, 8 et 9, lue avec son erratum 1 ; la réponse sur la boucle audit-recapture v2 (copie jointe) : sa règle, ses treize épreuves, l'échelle des échelons, les étapes et les décisions D-1 à D-6. Matière : la note sur l'attaquant informé, question 6 et blocs de calcul A à D ; la réponse 17 (le bilan de l'audit au hasard, zones 3, 5 et 6).

**Énoncés retenus, à ne pas changer.**
- Règle d'audit : le tirage se fait après la fin de l'épisode, le jugement porte sur une copie, hors ligne. La probabilité d'audit vaut un plancher, plus une part proportionnelle à l'enjeu, plus une part qui suit le soupçon. Elle n'est jamais nulle ; le soupçon peut la monter, jamais la descendre sous le plancher. Chaque probabilité est consignée, et les estimations sont pondérées par son inverse.
- Les quatre invariants d'audit, dans leur lettre accordée : audit après coup ; plancher indépendant du score ; part selon l'enjeu ; aucun retour à l'agent.
- La table du seuil au taux d'audit, à deux régimes (signature, excès), séparée du lemme d'additivité.
- Les scores orientent l'audit sous un plancher, avec son test de mort : un agent qui sait faire baisser son score se place au plancher.
- **Points ouverts chez le directeur, sans défaut, à respecter dans leur lettre actuelle** : aucune sonde n'est réapprise sur des verdicts de l'oracle, et la boucle ne vit que sur mondes plantés (règle « b′ » non tranchée) ; aucune correction observable par l'agent et venue d'un audit avant l'alarme (ligne « aucun retour à l'agent » contre les trois lignes de la note « asymétries », non tranchée).

**Ce que je te demande de concevoir.**
1. **Le simulateur commun de la règle d'audit**, sur mondes plantés : épisodes, enjeu fixé avant l'épisode, score de soupçon, dommage vrai, oracle de couverture q et de délai donnés, tirage et consignation, estimateur pondéré par l'inverse, alerte. Les paramètres, les grandeurs rapportées (la décomposition du budget en trois parts, la courbe sécurité-utilité à budget d'audit, la latence) et la loi de chaque estimation.
2. **La famille plantée « attaque choisie »** : le dommage est placé où le soupçon est bas et l'enjeu haut. Les trois attentes sont à écrire d'avance et à chiffrer : la borne du plancher tient ; l'audit des seuls plus suspects meurt ; l'audit uniforme perd le rapport de l'enjeu maximal à l'enjeu moyen. Pour chacune : cas sain, artefact, test de mort.
3. **Le score trompeur planté** pour la règle « les scores orientent l'audit sous un plancher » : la validité doit tenir et le délai rester dans la borne du tirage au hasard, sinon mort ; et « sans gain » sur une famille tenue à l'écart simulée.
4. **La table du seuil en instrument** : à partir du seuil toléré, du régime, de q et du délai, l'outil rend le taux d'audit exigé et dit, quand il dépasse le budget d'étiquettes, « le plancher n'y sert pas de garantie ».
5. **Les treize épreuves de la boucle en instruments** : l'ordre d'écriture, en commençant par la troisième (recapture aveugle), la quatrième (audit orienté) et la sixième (témoins), comme le recommande D-2 de la boucle v2 ; ce que chacune réemploie du simulateur commun ; ce que les prototypes de calcul de la boucle v2 donnent déjà, et ce qui reste à concevoir. Pour les épreuves qui supposent un harnais réel (lignée et rôle, ordre, versions closes), conçois-les sur un harnais simulé.
6. **Les gardes de code des quatre invariants**, là où un harnais les implémente : pour chacune, un cas sain et un artefact.
7. **Ce que l'étape 1 de la boucle demanderait** (étiquettes de construction sur organismes, au taux du plancher) : une esquisse de devis, non chiffrée comme accordée.
8. **La classe de chaque pièce** : instrument, ou expérience décisive à préenregistrer.

**Ce qui ne change pas.** Le plancher est une base nommée et citée, jamais une revendication. L'audit qui suit le score ne porte pas la borne. L'unité auditée est celle où le dommage se forme ; l'oracle lit ce que le harnais a enregistré, jamais le récit de l'agent. Aucun banc d'une autre équipe n'est employé : tout se joue sur les mondes plantés que tu conçois ici.
