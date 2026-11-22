# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHVhwpnJqPUiaUe8BGvz`
- Heure (UTC) : 2026-11-22T06:34:16Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-14-reduire-cout-essaim-organisme-v1.md` — sha256 d4f3831381896108a4e96ec3c123f479d13ed84ba413a8668b8f35ca9ddeee45 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/organisme-essaim-conception-fable-v1.md` — sha256 dd60dd678b215326d16cd46e1fb180a522d3f82ec8ba15e9519edd9d42277a0c (compagnon : vérifié)
- Empreinte de l'invite envoyée : e10a06f6d72be2c98ad6e21b6aadacb96a41689c45abdfcd5a071b405d489dd9
- Jetons : entrée 12731, sortie 23381 (dont réflexion 14325), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.037088 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 14 — réduire le coût de l'essaim : demande approfondie et réponse

Convention : [FAIT RAPPORTÉ] renvoie aux pièces fournies, [HYPOTHÈSE] est à tester, [PROPOSITION] est un choix de conception. Je n'ai pas vu le devis en dollars, seulement les chiffres cités dans la demande. Mes ordres de grandeur sont donc des hypothèses, à refaire sur le devis brut. La consigne interdit les noms de personnes : pour les antériorités je donne titre et année, les auteurs sont à relever sur les documents sources.

## A. Méthode « demande approfondie »

### A.1 Ce qu'un expert ferait et qui n'est pas demandé

- [FAIT RAPPORTÉ] Les tests de mort et les objets de contrôle font 70 à 80 % du devis ; la section D ne pèse que 469 à 2 343 dollars sur 2 366 à 8 380. [PROPOSITION] **La part non réduite borne le gain.** Supprimer entièrement ces deux postes ne divise le total que par 3,6 à 5 ; rabattre seulement les proposeurs ne le divise que par 1,25 à 1,4. Un ordre de grandeur exige d'agir sur les deux.
- [PROPOSITION] **Séparer deux natures de dépense.** Les objets de contrôle sont une mesure de la chaîne : ils n'entrent ni dans l'archive ni dans la couverture, donc on peut les échantillonner. Les tests de mort font partie du traitement : ils façonnent l'archive servie aux agents. Les « échantillonner » change l'organisme, ce n'est pas une économie de mesure.
- [FAIT RAPPORTÉ] La recherche gloutonne atteint 0,69 de couverture médiane mais ne trouve que 3 des 14 composantes conditionnelles. [HYPOTHÈSE] **La couverture globale est donc dominée par les composantes ordinaires**, qu'un programme gratuit trouve seul. La marge utile est sur les conditionnelles (environ 0,21 pour la base gloutonne). Il n'y en a qu'un peu plus d'une par monde, ce qui rend chaque monde presque binaire et peu informatif.
- [PROPOSITION] **Raisonner en coût par unité d'information**, non en coût par monde : densifier les composantes conditionnelles par monde augmente la puissance sans dépense.
- [PROPOSITION] **Renforcer la base sans modèle avant de payer** : une recherche gloutonne à un niveau de condition. Si elle trouve les conditionnelles, la famille ne demande pas de modèle et doit être durcie.
- [PROPOSITION] **Mesurer les tailles réelles** par un essai de fumée de deux courses de bras. [FAIT RAPPORTÉ] Les 6 000 jetons de sortie sont un devis, non une mesure.
- [PROPOSITION] **Borner le pire par construction** : plafond de sortie par appel et plafond par tranche appliqués par le noyau. Le pire devient alors un produit calculable (appels × plafonds × prix), ce qui répond au contre-lecteur.
- [HYPOTHÈSE] Le poste hors section D triple quand l'espèce des proposeurs change (environ 1 900 contre 6 000 dollars). Si le test de mort était tenu par un modèle fixe, il ne devrait pas bouger. C'est une question à poser au devis.

### A.2 Données brutes de départ

[PROPOSITION]
- Le devis ligne à ligne : unités, tailles et prix par rôle, avec la source datée de chaque prix.
- La définition exécutable du test de mort : ce qu'il lit, s'il appelle un modèle, si son verdict dépend de l'archive.
- Les sorties brutes de la base gloutonne sur les 12 mondes, composante par composante.
- Les relevés de jetons de la course v67 et de l'essai de fumée.
- Le texte en vigueur des conditions d'abonnement et des programmes de crédits, lu à la source et non résumé par moi.

### A.3 Méthodes et outils

[PROPOSITION]
- Recalcul du devis par un script, à partir d'un tableau d'unités gelé et d'une table de prix.
- Puissance par simulation avec les proposeurs synthétiques, sur la métrique conditionnelle.
- Pour les objets de contrôle, la « règle de trois » : zéro faute sur n objets borne le taux de faute à environ 3/n, à 95 %.
- Double échantillonnage : un test de mort bon marché partout, le test coûteux sur un échantillon, l'accord entre les deux mesuré.
- Analyse intermédiaire de futilité, gelée d'avance.
- Test exact apparié sur les discordances, pour comparer agent et base gloutonne composante par composante.
- Serveur d'inférence à lots continus, si un modèle ouvert est hébergé.

### A.4 Ce qui vérifie le résultat, hors du directeur et de Claude

[PROPOSITION]
1. La facture du fournisseur, rapprochée du journal après l'essai de fumée.
2. Le script de devis rejoué par un tiers.
3. La borne mécanique du pire.
4. La loi plantée lue par programme et la seconde écriture de l'oracle, déjà prévues.
5. Les bases sans modèle, dont la base renforcée.
6. Pour l'abonnement et les crédits : une réponse écrite du fournisseur, non mon souvenir.

## B. Demande reformulée

[PROPOSITION] « À partir du devis brut et de tailles mesurées, trouver la conception la moins chère qui garde identifiable l'effet de la communication sur les composantes conditionnelles. Distinguer ce qui est mesure (échantillonnable) de ce qui est traitement (à geler). Borner le pire par construction, payer par tranches, et ne franchir chaque tranche que sur un critère écrit d'avance. Dire ce que chaque économie coûte en validité. N'utiliser que des moyens de calcul permis, tracés et rejouables par un tiers. »

## C. Réponse

### C.1 Les leviers

Les facteurs portent sur le poste indiqué. Ce sont des [HYPOTHÈSE] d'ordre de grandeur.

| Levier | Gain sur son poste | Coût de validité |
|---|---|---|
| 1. Objets de contrôle une fois par monde, plus des lots sentinelles au début, au milieu et à la fin | ÷ 6 à ÷ 20 | Faible si la chaîne est sans état et la version gelée ; on perd la localisation d'une faute par bras |
| 2. Test de mort par programme en monde planté (réplication sur données tenues à l'écart, sans lire la loi) | poste ramené à environ zéro | Moyen : le résultat vaut « sous ce juge programmé » ; accord avec le test par modèle à mesurer sur un échantillon |
| 3. Cache de verdicts par forme canonique et par monde, partagé entre bras | ÷ 1,5 à ÷ 3 | Nul, voire favorable : la même forme reçoit le même verdict dans les trois bras |
| 4. Traitement par lots | ÷ 2 sur ce qui est différable | Nul sur les sorties si le modèle servi est identique ; la course s'étale sur plusieurs jours |
| 5. Cache du préfixe d'entrée | 10 à 20 % des proposeurs | Nul |
| 6. Sorties bornées (deux cartes en schéma strict, réflexion plafonnée) | ÷ 2 à ÷ 3 sur les proposeurs | Moyen : risque de plancher ; résultat valable « à cet effort » |
| 7. Une seule comparaison principale, les autres en séquence fixe | environ −25 % de mondes à puissance égale | Faible : les autres comparaisons ne se lisent que si la première passe |
| 8. Densifier les conditionnelles (3 à 4 par monde) | puissance accrue à coût égal | Règle de garde à revérifier par simulation |
| 9. Périmètre réduit (familles inédites reportées, contrôle sur deux bras, instruments sur 8 mondes) | 200 → environ 85 courses de bras confirmatoires | Portée réduite, dite d'avance |
| 10. Arrêt de futilité à mi-course | jusqu'à ÷ 2 si l'effet est nul | Légère perte de puissance ; pas d'inflation du risque |
| 11. Modèle ouvert sur carte graphique louée | coût marginal de quelques dizaines de dollars | Portée limitée à cette espèce ; risque de plancher ; reproductibilité meilleure |

Précisions :

- **Levier 1.** [FAIT RAPPORTÉ] La conception sert le même jeu dans chaque bras et dans chaque lignée de (b), soit six passages par monde. [PROPOSITION] Si le verdict ne dépend pas de l'archive, un passage par monde suffit. Avec 60 objets sans faute sur toute la course, le taux de faute de la chaîne est borné à 5 % ; avec 300, à 1 %. C'est la « puissance qui reste », à comparer au seuil que le directeur juge tolérable.
- **Levier 2.** [PROPOSITION] Le programme ne doit lire que des données, jamais la loi plantée. Sinon le juge devient l'oracle et la vérité fuit par l'archive.
- **Levier 3.** [FAIT RAPPORTÉ] 9 cartes sur 23 répétaient une forme dans v67. Le cache absorbe aussi les « tests de mort dupliqués » des archives privées.
- **Levier 4.** [FAIT RAPPORTÉ, de mémoire, non vérifié] Le rabais par lots est d'environ moitié chez Anthropic, et la lecture de cache coûte environ un dixième du prix d'entrée. Je ne connais pas l'offre du fournisseur de Kimi.
- **Levier 5.** [HYPOTHÈSE] Le gain est faible parce que la sortie fait environ les trois quarts du coût des proposeurs (30 millions de jetons de sortie à rapport 5, contre 45 d'entrée).
- **Générations.** [PROPOSITION] Ne pas descendre sous trois : la communication n'agit qu'entre générations, et en retirer une coupe l'effet cherché.
- **Levier 11.** [HYPOTHÈSE] Une fois les autres leviers appliqués, la conception réduite coûte déjà environ 150 dollars de proposeurs sur Kimi par l'interface payante. L'hébergement économiserait une centaine de dollars et coûterait des jours de mise au point. Son intérêt réel est la reproductibilité (poids gelés, graines, aucun changement de version silencieux), non le prix.

[HYPOTHÈSE] Effet cumulé, par rapport au cas attendu :
- proposeurs sur Kimi : 2 366 → 150 à 400 dollars (÷ 6 à ÷ 15) ;
- proposeurs Claude : 8 380 → 500 à 900 dollars (÷ 9 à ÷ 17) ;
- deux ordres de grandeur ne s'atteignent qu'en cumulant le test de mort par programme, une espèce bon marché et le périmètre réduit, ou en s'arrêtant au pilote.

### C.2 Les sessions sur abonnement comme moyen de calcul

**Ce que je sais, et sa limite.** [FAIT RAPPORTÉ, de mémoire, non vérifié] Les conditions d'un abonnement individuel réservent l'usage à l'abonné, dans les applications d'Anthropic, dont Claude Code. L'accès automatisé hors des voies explicitement prévues y est exclu. Les quotas sont des fenêtres glissantes et des plafonds hebdomadaires, sans valeur contractuelle en jetons et révisables. Mon souvenir est qu'une précision a exclu l'emploi des identifiants d'abonnement dans d'autres outils ou dans la trousse de développement d'agents. Je ne peux pas connaître le texte en vigueur à la date de la demande : il faut le lire, ou poser la question par écrit.

**Faisabilité technique.** [HYPOTHÈSE] Oui : Claude Code a un mode non interactif et des sessions filles qui exécutent des consignes.

**Pourquoi ce n'est pas sain comme calcul de mesure, même si c'était permis.** [PROPOSITION]
1. **Ce n'est pas le modèle nu.** La session ajoute sa consigne système, ses outils et son contexte. Le test de mort ne serait plus le même objet que par l'interface payante.
2. **Les réglages échappent** : échantillonnage, plafond de sortie, et surtout le modèle servi, qui peut changer d'alias ou se replier à l'approche du quota. La conception exige « aucun repli ».
3. **Les quotas brisent l'appariement** : les trois bras ne tournent plus dans la même fenêtre de temps, et un monde peut être coupé au milieu.
4. **Aucune facture à rapprocher.** Le coût n'est pas réduit, il est masqué. La comparaison « à coût égal » (N-045) perd son appui.
5. **Risque de fuite.** Une session lit les fichiers du dépôt et sa mémoire de projet, là où vivent les lois plantées et l'oracle.
6. **Un tiers ne peut pas rejouer** la course dans les mêmes conditions.
7. **Tout ou rien.** Les objets de contrôle n'attestent la chaîne que s'ils passent par le même canal que les vraies cartes. Faire passer les contrôles par l'abonnement et les tests de mort par l'interface payante rendrait les contrôles muets.

**Ce qui est permis et sain, à mon avis.** [PROPOSITION]
- Utiliser l'abonnement pour ce à quoi il sert : le travail de développement de l'abonné. Cela couvre le noyau, la seconde écriture de l'oracle, la base renforcée, la simulation de puissance, la relecture du devis et le débogage de la chaîne sur quelques cartes de calibration (étiqueté instrument, jamais versé aux chiffres).
- Ne pas faire piloter par l'organisme des milliers d'appels automatisés, ne pas multiplier les comptes, ne pas étaler la charge pour passer sous les quotas. Ce serait contourner.

**Crédits offerts.** [PROPOSITION] C'est la voie propre : même interface, mêmes modèles, mêmes journaux, facture à zéro. Trois conditions :
- respecter l'objet et l'échéance du programme ;
- compter les appels au prix public pour l'égalisation ;
- déclarer la source dans le rapport.

[FAIT RAPPORTÉ, de mémoire, non vérifié] Il existe des programmes de crédits pour la recherche chez Anthropic et des crédits de jeunes entreprises chez les fournisseurs d'informatique en nuage qui servent Claude. Les identifiants de version et l'accès aux lots peuvent y différer, donc l'appariement des versions est à vérifier.

### C.3 Le plus petit pilote

**Doit-il battre la base gloutonne ?** [PROPOSITION] Oui, sur les composantes conditionnelles et non sur le 0,69 global. Sur la couverture globale la marge n'est que de 0,31 et un programme gratuit en fait l'essentiel. Si l'agent seul ne trouve pas de conditionnelles que la base manque, il y a deux lectures : le modèle est au plancher, ou la tâche n'a pas besoin de modèle. Dans les deux cas un essai payé sur la communication n'a pas de valeur de décision.

**Palier 0, gratuit.**
- Devis brut recalculé.
- Base gloutonne renforcée.
- 24 mondes de calibration engendrés, densifiés si la décision 5 le retient.
- Test de mort par programme.
- Puissance simulée.
- Essai de fumée de deux courses de bras (5 à 25 dollars) pour mesurer les tailles.

**Palier 1, porte « agent contre base ».**
- Bras (c) seul, 24 mondes, une course chacun.
- Critère gelé : l'agent trouve plus de conditionnelles que la base renforcée, au test exact sur les discordances, sans excès de formes fausses.
- [HYPOTHÈSE] Avec 28 composantes, une base à 0,2 et un agent à 0,6, on attend environ 13 discordances contre 2, ce qui est nettement détectable. Avec les 14 actuelles ce serait marginal, d'où 24 mondes plutôt que 12.
- Coût : 24 courses de bras, soit 25 à 55 dollars sur Kimi d'après le coût unitaire du devis (environ 2,3 dollars par course de bras en section D), et 100 à 280 sur Claude (environ 11,7).

**Palier 2, bruit et futilité.**
- Bras (a) et (b), 12 mondes, deux répétitions : 48 courses de bras, 50 à 110 dollars sur Kimi.
- Il rend l'écart-type apparié, l'écart test–retest et les tailles par rôle.
- Il ne confirme rien. Il peut seulement arrêter, si la borne haute de l'intervalle sur (a) − (b) est sous l'effet minimal, ou si l'écart-type rend cet effet indétectable au nombre de mondes finançable.

**Modèle.** [PROPOSITION] Kimi par l'interface payante : aucune mise au point, coût de l'ordre de la centaine de dollars. Si Kimi échoue au palier 1, une sonde du bras (c) avec l'espèce Claude sur 12 mondes (40 à 140 dollars) avant de conclure, car un échec sur une espèce ne dit rien de l'autre.

**Total du pilote.** [HYPOTHÈSE] 80 à 190 dollars, soit 12 à 30 fois moins que le cas attendu le moins cher.

### C.4 Conception à coût réduit recommandée

[PROPOSITION]
- **Chaîne** : juge statistique et test de mort par programme. Le test de mort par modèle reste un instrument sur un échantillon de 60 cartes, pour mesurer l'accord. Cache de verdicts partagé. Objets de contrôle une fois par monde, plus des lots sentinelles.
- **Appels** : sorties bornées, plafond de sortie strict, lots quand ils existent, les trois bras dans le même lot.
- **Statistique** : (a) − (b) sur la famille MR-2 densifiée, métrique conditionnelle, comme seule comparaison principale. (a) − (c) et (b) − (c) suivent en séquence fixe.
- **Taille** : 20 mondes × 3 bras, avec une analyse de futilité à 10 mondes. Famille de contrôle sur 8 mondes × 2 bras. Placebo de communication sur 8 mondes. Familles inédites et seconde espèce reportées.
- **Paiement** : par tranches, plafond dur par tranche, rapport et retour devant le directeur à chaque porte.

[HYPOTHÈSE] La puissance est à refaire par simulation. Avec une seule comparaison principale il faut environ 8/d² mondes au lieu de 10,5/d². Vingt mondes voient donc un effet standardisé d'environ 0,65 à 0,7.

Devis en ordre de grandeur [HYPOTHÈSE] :

| Tranche | Courses de bras | Kimi | Claude |
|---|---|---|---|
| Palier 0 et essai de fumée | 2 | 5 | 25 |
| Pilote (paliers 1 et 2) | 72 | 80 à 190 | 300 à 800 |
| Confirmatoire réduit | 84 | 90 à 200 | 300 à 500 |
| Instrument « test de mort par modèle » | — | 10 à 50 | 50 à 150 |
| **Total** | **environ 160** | **200 à 450** | **700 à 1 500** |

Le pire est borné par les plafonds de tranche, que le directeur fixe. Par exemple, le double de la colonne retenue.

### C.5 Antériorité

Tout est **rapporté de mémoire, non vérifié sur document source**, sans chiffre opposable.

- « FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance » (2023) : cascades de modèles.
- « AI Agents That Matter » (2024) : évaluation d'agents à coût contrôlé.
- « Reasoning in Token Economies » (2024) : déjà citée.
- « tinyBenchmarks: evaluating LLMs with fewer examples » (2024) : évaluation par échantillon.
- « Prediction-Powered Inference » (2023) : mesure bon marché corrigée par un petit échantillon coûteux.
- « A multiple testing procedure for clinical trials » (1979) : analyses intermédiaires.
- « Efficient Memory Management for Large Language Model Serving with PagedAttention » (2023) : service à lots continus.
- « LLM-SR: Scientific Equation Discovery via Programming with Large Language Models » (2024) et « LLM-SRBench » (2025) : proposeurs à modèle contre recherche sans modèle sur des lois à retrouver.

[HYPOTHÈSE] La comparaison entre proposeurs à modèle et recherche symbolique est une zone occupée. La question de la communication dans ce cadre, à coût égal et avec un oracle indépendant du juge, reste une question.

## D. Décisions qui reviennent au directeur

**1. Décider si le test de mort devient un programme en monde planté.**
- Enjeu : c'est le premier poste du devis, et il façonne l'archive.
- Option A, programme, avec le test par modèle en instrument sur échantillon : poste presque nul et verdicts déterministes ; le résultat vaut « sous ce juge ».
- Option B, modèle, avec cache de verdicts, lots et contrôles une fois par monde : fidèle à l'organisme réel ; le poste n'est divisé que par 3 à 6.
- Option C, inchangé : aucune révision ; le devis reste au niveau actuel.
- Recommandation : A. Confiance 0,65, car je n'ai pas vu la définition exécutable du test.

**2. Décider de l'usage de l'abonnement et des crédits.**
- Enjeu : validité de la mesure et respect des conditions d'usage.
- Option A, abonnement pour le développement seul, mesure par l'interface payante, crédits de recherche sollicités : traçable et rejouable ; délai de la demande de crédits.
- Option B, question écrite au fournisseur puis abonnement pour des instruments de débogage seulement : économie marginale ; frontière à surveiller.
- Option C, abonnement comme calcul de la chaîne : dépense visible nulle ; appariement, facture, étanchéité et reproductibilité perdus, permission douteuse.
- Recommandation : A. Confiance 0,85.

**3. Fixer la porte du pilote.**
- Enjeu : ne pas payer un essai sur une tâche sans marge.
- Option A, l'agent seul bat la base renforcée sur les conditionnelles, sur 24 mondes : vise la marge réelle ; demande de densifier ou d'engendrer des mondes.
- Option B, battre 0,69 en couverture globale : simple ; plafond proche, signal dominé par les composantes faciles.
- Option C, pas de porte : rapide ; risque de payer un résultat nul par construction.
- Recommandation : A. Confiance 0,75.

**4. Choisir l'espèce du pilote.**
- Enjeu : coût, plancher et portée.
- Option A, Kimi par l'interface payante : environ cent dollars, aucune mise au point ; versions moins maîtrisées.
- Option B, modèle ouvert hébergé : poids gelés, coût marginal minime ; jours de mise au point, risque de plancher.
- Option C, Claude : espèce de l'organisme ; trois à cinq fois plus cher.
- Recommandation : A, avec la sonde Claude du bras (c) en cas d'échec au palier 1. B seulement si la reproductibilité par un tiers devient une exigence. Confiance 0,6.

**5. Décider de reparamétrer MR-2 pour densifier les conditionnelles.**
- Enjeu : l'information par monde payé.
- Option A, 3 à 4 conditionnelles par monde, garde revérifiée par simulation : puissance gratuite ; la famille n'est plus celle déjà mesurée.
- Option B, famille inchangée et plus de mondes : continuité ; coût proportionnel.
- Option C, archive amorcée par la base gloutonne dans tous les bras : jetons concentrés sur la marge ; la question devient « communication par-dessus la base ».
- Recommandation : A. Confiance 0,55.

**6. Engager les tranches.**
- Enjeu : la dépense maximale réellement exposée.
- Option A, payer maintenant le palier 0 et le pilote seulement, sous plafond dur, et décider le confirmatoire sur l'écart-type mesuré : exposition d'environ 200 dollars ; un aller-retour de plus.
- Option B, engager toute la conception réduite : un seul passage ; quelques centaines de dollars exposés avant de connaître le bruit.
- Option C, garder la conception d'origine avec les seuls leviers techniques : portée complète ; plusieurs milliers de dollars.
- Recommandation : A. Confiance 0,8.

FIN DE LA RÉPONSE
