# Question au collisionneur — nœuds de décision v12, tour 2 : attaque des recommandations — v1

session-depot (instance 3), 31 octobre 2026. Second envoi prévu par la question v12 (`question-noeuds-decisionnels-collisionneur-v12.md`,
`a7fac44b…`, section « Déroulé en deux tours »). Les faits servis avec cette question sont la **synthèse du tour 1** (lecteur neuf,
critères scellés `criteres-lecture-noeuds-v12-tour1-v1.md`, `22edbf47…`) : elle rapporte, par nœud et par espèce, les options du
tour 1, les pires cas, les gardes, les options manquantes, les pièces qui trancheraient, les divergences non résolues et les
accords jugés trop propres. Les faits du tour 1 (45 811 mots) ne sont pas resservis : toute affirmation chiffrée que vous
reprenez renvoie à la synthèse ou à la question v12 ; toute référence non lue est SUPPOSÉ. Niveau méthode ; aucun contenu du bras
d'attaque ; aucune donnée de `donnees/`. Le collisionneur ne décide rien ; le directeur tranche ensuite.

## Ce qui est demandé

Pour **chaque recommandation** de l'annexe ci-dessous (une par nœud ; pour N6, une par décision DL-1 à DL-13), un verdict parmi :
« tenue » ; « tenue sous condition (écrire la condition) » ; « renversée (écrire l'option qui la remplace) » ; « aucune option ne
tient » ; « indécidable sans la pièce X (nommer la pièce et ce qu'elle doit montrer) ». Chaque verdict donne : la raison en
une à trois phrases ; le pire cas si la recommandation est suivie et la garde qui le ferme ; si votre avis du tour 1 (rapporté
dans la synthèse) change, dites-le et pourquoi. Puis, pour les **divergences non résolues** et les **accords trop propres** listés
par la synthèse (section « questions pour le tour 2 ») : votre position, en une ligne chacune. Enfin : l'ordre dans lequel le
directeur gagne à trancher, s'il diffère de celui que vous avez donné au tour 1.

Une confiance d'auteur n'est pas un argument : la recommandation d'un auteur se juge sur les faits de la synthèse et de la
question v12, pas sur sa confiance.

## Annexe du tour 2 — recommandations des auteurs des pièces — v5 (conv-audit, servie telle quelle)


À servir **après** réception des réponses du tour 1 à `question-noeuds-decisionnels-collisionneur-v12.md`. conv-audit, 31 octobre 2026, ≈ 12:59 UTC. **v5 = v4 + N11** (v4 gardée ; son en-tête portait « ≈ 13:10 UTC », heure écrite en avance, vraie heure 12:45 UTC, R-1001). La v4 remplaçait la v3 (gardée) : couvre N9 et N10 (défaut 3 du n° 224 de session-depot) ; N3 réduit à D-j ; N6 porté au semi-réel brouillon 5.

- **N1** : B, confiance 0,6 (conv-audit ; sa recommandation précédente, « corriger le générateur », 0,7 — option C de la question —, a été retirée par son auteur après le diagnostic).
- **N2** : retiré (tranché : 50 / 45 souple, GO-2026-10-31-03).
- **N3** : D-j oui, confiance 0,7 (auteur du brouillon 10 du pré-pilote, l. 732). Le substitut S31 porte une confiance d'auteur de 0,4 (brouillon 10, table des seuils). D-g, D-h, D-i : tranchés par Lazar (R-718, R-719 de la branche conv-audit).
- **N4** : (a), confiance 0,5 (conv-audit) ; CA1-04 : non tranché.
- **N5** : (a), confiance 0,7 (contre-lecture CL19, qui écrit aussi « mieux que l'amendement : ne pas lire », c'est-à-dire l'option (b)).
- **N6** (auteur du semi-réel brouillon 5) : DL-1 (2) 0,65 ; DL-2 (2) 0,55 ; DL-3 (1) 0,6 ; DL-4 (1) 0,85 ; DL-5 (1) 0,55, avec la mention « option : demander au collisionneur » ; DL-6 (1) 0,7 ; DL-7 (2) 0,7 ; DL-8 (4) 0,7 ; DL-9 (1) 0,55 ; DL-10 (1) 0,55 ; DL-11 (1) 0,6 ; DL-12 (1) 0,6, « option : demander au collisionneur » (la vérification VS5-01 conteste l'avantage prêté à cette option ; le brouillon 6 en cours révise l'analyse) ; DL-13 (1) 0,55, « option : demander au collisionneur ».
- **N7** : retiré (tranché : suspension jusqu'à E2′, R-878).
- **N8** : retiré (tranché : GO-2026-10-31-01).
- **N9** : (a), recommandée par session-depot (préenregistrement Gu-Krenn v2) : population à fin 2022, fenêtre du 1er janvier 2023 au 30 septembre 2026.
- **N10** : (b), confiance 0,55 (conv-audit) : poser la robustesse adaptative en génération 2, avec Bailey et collègues et les résultats du pilote dans les pièces.
- **N11** (décision du directeur : (b) et (c), collisionneur consulté avant ; les propositions des auteurs portent sur le « comment ») : **session-depot** (n° 228, confiance 0,65) : par bras, rendement sur l'oracle (structures retrouvées, vrais promus, faux rejetés, proches et surfaces) et coût par vrai trouvé, intervalles par rééchantillonnage des mondes ; retrait seulement si dominé avec confiance (borne haute du bras sous la borne basse du meilleur, sur le rendement par dollar), sinon reconduit ; part minimale d'exploration ; calcul de puissance d'abord, issue « non concluant, tous reconduits » écrite d'avance ; même règle sur le score de rétrodiction inversée d'E1′. **conv-audit** (n° 294, confiance 0,6) : la course 2 n'a pas d'oracle pour les fusions ; la règle va aux préenregistrements de la bisociation v3 (mondes synthétiques) et d'E1′, la course 2 restant descriptive par bras ; les ponts plantés (option (c)) rouvrent le texte que le pré-pilote éprouve.
