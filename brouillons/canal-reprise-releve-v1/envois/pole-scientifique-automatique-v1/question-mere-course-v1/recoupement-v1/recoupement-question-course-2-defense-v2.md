# Recoupement — question de la course 2, volet défense (axes 1, 2, 3, 4, 5, 7 et boucle) — v2 (v1 + synthèse du collisionneur)

Sous-agent neuf (Sonnet 5.5), relevé `date -u` du 29 octobre 2026, 23:34 UTC ; n'a écrit ni la v1 ni aucune entrée. Critères : § 3 de `question-mere-course-ideation-v3.md`
(`1b08e17f…`), à la lettre. Entrées, empreintes recalculées égales à leurs compagnons `.sha256` : recoupement v1 (`1a5d4ffa…`), fusion v1 (`f89e0791…`),
synthèse du collisionneur `entrees/synthese-collisionneur-question-mere-v2-v1.md` (`25e2d351…`). Les réponses de conv-audit [CA], d'Opus neuf [ON], de session-depot [SD]
et d'Argon [AR] ne sont relues que par les passages cités dans le recoupement v1 et par quelques vérifications ponctuelles (SD, ON). **Hors périmètre, sauté : l'axe 6.**
**Limite** : je n'ai lu que la **synthèse** (rédigée par un sous-agent qui n'a écrit aucune cellule), non les neuf cellules du collisionneur ni la question qui lui fut servie ;
les renvois « l. n » sont ceux de la synthèse, non vérifiés ici. Rien n'est scellé ; non contre-lu (R2).
**Règle v2** : le collisionneur compte comme **un** répondant (trois modèles : A = Fable 5.1, B = Opus 5.5, C = Gemini Argon). Un élément est **commun** s'il est donné par le
collisionneur et par au moins un autre répondant compté (CA, ON, SD) avec la même définition opérationnelle ; sinon **divergent**. L'accord interne est noté (3/3, A+B, A+C) ;
un accord entre A et B seuls, ou entre le collisionneur et le modèle de même famille (A avec CA, B avec ON), pèse moins (réserve 10 du collisionneur). Aucun passage à « commun »
ci-dessous ne repose sur C seul. L'avis d'Argon séparé [AR] reste lu à côté, non compté. Statuts comme en v1 (commun, divergent → Dn, écarté, circulaire, non jugeable, imposé).

## A.1 Éléments de la v1 que le collisionneur change (les autres sont inchangés : liste en fin de section)
| Id v1 | Ce que dit le collisionneur | Statut v2 |
|---|---|---|
| F5 | « 0,38 n'est qu'un repère » ; battre HELIOS = battre la base « dernier état » rejouée sur notre banc (3/3) | commun renforcé ; texte : « repère et non seuil » |
| P6 | Aucune donnée de calibrage ou d'évaluation de G1 servie ; partition tierce, intersection vide (3/3) | commun renforcé ; G1 ajouté aux exclusions du texte |
| P7 | Même exigence de tiers et d'intersection vide, mais A : verdict seul ; B : aucune tranche ; C : tranche isolée avec exécution | divergent maintenu → **Q2** ; défaut : tranche D4 retirée |
| P8 | A : verdict seulement, « jamais les vecteurs » (après la critique de C) ; contre CA | **commun** (ON, A) ; D9 clos en (a) |
| P5 | B, C : l'analyseur programmé décide à l'étage 1 ; ON, réserve 1 : par programme quand c'est possible | principe commun (N14a) ; le contrôle des pages d'HELIOS reste ON seul → D10 |
| J1, J2 | Les trois convergent sur un gabarit de champs vérifiés mécaniquement | commun renforcé |
| J3 | 1 % par action vaut environ 26 % par épisode à 30 actions (T2-A) : fausses alertes comptées par épisode | commun maintenu ; glossaire réécrit |
| J4 | A : liste fermée plus clause (contrôle de présence) ; C : une ressource absente des pièces annule la fiche ; B : un fait des pièces en plus | **commun** (ON, A, C) ; K2 gagne « pièce et page à l'appui » |
| J5 | Les trois tiennent « décisif » et « inédit » pour interprétatifs (reco 5) | non jugeable confirmé ; K2 reste un contrôle de présence |
| J6 | B, C : le juge à pari apparié ne note pas le texte ; C a concédé son « juge à mise appliqué à des fiches » | divergent → D8 ; option (b) d'Argon affaiblie |
| J7 | Étalonner avant tout lancement, avec témoins négatifs (creuses, paraphrases, forme sans fond, avantage faux) (3/3) | imposé maintenu ; extension divergente N1 → **Q1** |
| A1.5 | A, C : plancher au maximum de K tirages (B : autre règle) | commun maintenu ; extension N13 → D14 |
| A1.9 | Idem F5 | commun renforcé (CA, ON, collisionneur) ; couches → D4 |
| A1.15 | Séparer m1 (exécution) de m2 (lisibilité) avant l'axe 1 (3/3) ; ON : facultatif | m1/m2 devient **commun** (N4) ; « jouable par le juge figé » reste ON seul → D10 |
| A1.4 | Plan 2 × 2 « grain des jetons × accumulation », hors de G1 (3/3) ; SD : accès × agrégation | divergent maintenu (plans voisins, non identiques ; N10) → D10 |
| A4.2 | Reste ouvert : l'étiquetage des familles scellées par un tiers n'a aucun mécanisme contre la fuite (T2-B l. 141) | commun maintenu ; réserve nouvelle (3) |
| A4.4 | Fausses alertes par épisode, à tout instant, trois jeux disjoints (3/3) ; seuil unique scellé (A, C) | commun maintenu ; précisions N2b, N12 |
| A4.7 | Variance du seuil à 1 % (environ 3 dépassements sur 300), loi jointe, multiplicité, effet minimal, témoin positif, pseudo-réplication (3/3) | commun maintenu pour puissance et multiplicité ; ajouts N7, N8, N9 → D14 |
| A4.8 | Consigne bénigne de longueur appariée ; « rien de la consigne à la position lue » | divergent maintenu (ON seul) ; voisins N3 et N11 → D14 |
| A5.2 | C a concédé la critique « Lean avec `sorry` » (interdits, test de non-vacuité) | commun maintenu ; ajout N16 → D14 |
| A7.2 | A, B : la lecture « axes libres » n'est pas une vérité de terrain ; occupants tirés de plusieurs documents ; vérification sans accès au dépôt | commun renforcé (CA, ON, collisionneur) ; statut « non réfuté par [procédure] à [date] » → **Q4** |
| A7.3, A7.14 | A : au moins dix revendications d'au moins trois sources ; B : environ cinq documents, strates « dans » et « hors » le dossier | divergents maintenus (définitions différentes de celle d'ON) → D10 |
| A7.5 | Voir J4 (liste fermée) | **commun** (ON, A) |
| A7.8 | Mémoire anti-redite étalonnée sur paraphrases plantées par un tiers, plongement nommé et figé (3/3) | non jugeable → réécrit : filtre mécanique étalonné (D7 (a)) ; N6 |
| A7.13 | Vérification étalonnée par échantillon de revendications (A : E7) | commun maintenu ; l'étalonnage → consigne d'orchestrateur |
| B1 | A : compté, pas noté jusqu'au test ; B : testé si l'effet détectable est d'au plus 0,35, sinon choix de Lazar ; C : obligatoire dès la 2e génération | divergent → **Q3** (premier répondant compté ; aucun commun possible) |
| B5 | Seuil de similarité : se fixe par étalonnage sur paraphrases plantées (N6) | non jugeable tant que non étalonné |
| B6 | A, B : mesure consignée seulement | imposé confirmé (commun avec la question-mère) |
| B7 | A, B : mesure tant que l'association nouveauté / survie n'est pas établie sur deux générations ; C : règle fondée sur la survie | divergent → **Q6** ; la règle « deux générations sans neuf » (v0) quitte le texte |
| M1 | B : stérile si l'ensemble noté R est vide (R non défini dans la synthèse) ; A : meurt si l'examen des juges (E6) donne H_B, lu comme « instrument invalide » | M1 divergent maintenu ; étalonnage → M5 |
| M2 | Scindé : **M2a** après vérification sur PDF aucune notable ne garde son élément (ON, CA axe 7, B) ; **M2b** toutes reformulent les huit questions (CA ; A dit : deux générations sans fiche hors des huit fiches de référence, objet voisin) ; **M2c** aucun préenregistrement scellable (ON seul) | M2a **commun** ; M2b, M2c divergents → D13 |
| M5 | A : la course meurt si l'examen des juges donne H_B (même lecture) | imposé maintenu, étendu |
| V3 | Voir A5.2 | commun maintenu |
**Inchangés (collisionneur muet ou sans effet)** : F1 (A et C confirment le texte unique), F2, F3, F4, P1–P4, P9, J8, J9, A1.1–A1.3, A1.6–A1.8, A1.11–A1.14, A1.16, A1.17 (circulaire confirmé), A2.1–A2.7, A3.1–A3.8,
A4.1, A4.3, A4.5, A4.6, A4.9–A4.12, A5.1, A5.3–A5.6, A7.1, A7.4, A7.6, A7.7, A7.9–A7.12, V1, V2, V4, V5, M6, B2 (silence), B8, B9. Le collisionneur n'écarte rien, ne demande ni mode ni recette.

## A.2 Éléments nouveaux apportés par le collisionneur
| Id | Élément (définition opérationnelle) | Appui | Statut |
|---|---|---|---|
| N1 | Pré-pilote d'étalonnage avant tout lancement : analyseur et juges sur témoins plantés, négatifs compris ; rejet de 15 fiches défectueuses sur 20 (verrou de C) | 3/3 ; ON : témoin positif seul | divergent → **Q1** |
| N2a | Fausse alerte tenue à tout instant | SD (tout horizon), ON (borne valide à tout instant), 3/3 | **commun** |
| N2b | Fausses alertes comptées par épisode ; calibrage, seuil et vérification sur trois jeux disjoints | 3/3 | divergent → D14 |
| N3 | Contrôle par consigne bénigne de longueur appariée | 3/3 | divergent → D14 |
| N4 | Séparer exécution (m1) et lisibilité (m2) | ON ; AR à côté ; 3/3 | **commun** (obligatoire pour le collisionneur, facultatif pour ON → D4) |
| N5 | Aucune donnée de G1 servie ; partition tierce, intersection vide | ON, CA, 3/3 | **commun** (= P6) |
| N6 | Mémoire anti-redite étalonnée ; plongement nommé et figé | 3/3 | divergent ; consigne d'orchestrateur (routine) |
| N7 | Variance du seuil à 1 % propagée dans la borne | 3/3 | divergent → D14 |
| N8 | Axe 4 : loi jointe, taille d'effet minimale, témoin positif à effet connu | 3/3 | divergent → D14 |
| N9 | Pas de pseudo-réplication : randomisation par session, corrélation intra-classe | 3/3 | divergent → D14 |
| N10 | Plan 2 × 2 grain des jetons × accumulation, hors de G1 | 3/3 | divergent → D10 (voisin d'A1.4) |
| N11 | Préalable « rien de la consigne à la position lue » ; l'organisme (ii) entre au duel s'il existe | A, B | divergent → D10 (voisin d'A4.8) ; « organisme (ii) » non défini dans la synthèse |
| N12 | Seuil unique scellé ; issue « non jugeable par puissance » | A, C (sans C : non) | divergent → D14 |
| N13 | Plancher au maximum de K tirages | A, C (sans C : non) | divergent → D14 |
| N14a | Contrôles mécaniques d'abord (analyseur programmé décide) | ON ; B, C | **commun** |
| N14b | Modèle-juge limité à la cohérence entre champs ; le juge à pari apparié ne note pas le texte | B ; B, C | divergent (mineur) |
| N15 | Conditionner l'axe 1 à l'établissement du signal à 8 milliards (reco 4, 0,75) | 3/3 | divergent → **Q5** |
| N16 | Preuve sans `sorry`, hypothèses non vides | C | divergent → D14 |
Consignes de dépense, hors texte : expériences à plusieurs courses (158, 211, 264 dollars) hors du devis actuel (reco 8) ; lecture du registre pour lever la contradiction « S6 » avant l'expérience à 8 milliards (reco 9, 0,7).

## B. Divergences D1–D14 mises à jour (défaut appliqué sous 48 heures)
- **D1** inchangé (le collisionneur ne dit rien). Interaction : si Q3 (b), une sous-session neuve de l'axe 7 ne voit pas les failles de la même génération.
- **D2** inchangé.
- **D3** inchangé, mais le collisionneur chiffre les expériences à plusieurs courses (158 à 264 dollars) et deux générations jusqu'à 105,60 dollars : un plafond de 300 dollars (b) admettrait une telle expérience par fiche. Renforce (a) ; confiance 0,75.
- **D4** partiellement tranché : la lecture d'HELIOS rejouée et la séparation m1/m2 passent au minimum commun ; restent (b) sonde nulle, couches séparées, hyperparamètres hors épreuve, et (c) comparateur gradué. Recommandation (b), confiance 0,7.
- **D5** inchangé.
- **D6** inchangé ; réserve ajoutée : l'étiquetage des familles par un tiers n'a pas de garantie contre la fuite.
- **D7** (a) maintenu et précisé : les deux filtres (table de substitution, bardeaux de mots) sont étalonnés sur des paraphrases plantées des huit questions (3/3). Confiance 0,75.
- **D8** tranché en (a) : le juge à mise sur des fiches a été critiqué puis concédé dans le collisionneur. Confiance 0,75.
- **D9** clos en (a) : commun (ON, A). Confiance 0,9.
- **D10** réduit : P8 et la partie m1/m2 d'A1.15 (N4) en sortent ; P7 passe à Q2. Reste le lot (P5, P9, A1.4 et N10, N11, A1.12, A1.13, A1.15 jouable, A2.4–A2.6, A3.5, A3.6, A4.8, A5.5, A5.6, A7.3, A7.10, A7.14, pièces G, H, I de SD). Recommandation (a), 0,6.
- **D11** inchangé ; rappel du collisionneur : la grille et ses cases « déjà couvertes » ne sont pas une vérité de terrain (A7.2).
- **D12** scindé. Statut du vis-à-vis → Q3. Arrêt → Q6. Ce que g + 1 reçoit et l'étiquette d'héritage : le collisionneur est muet, option (a) de la v1 maintenue (fiches anonymes, verdict, classement, étiquette d'héritage), confiance 0,5.
  Le collisionneur est désormais le **premier répondant compté** sur la boucle ; avec un seul, aucun « commun » n'est possible.
- **D13** scindé : M2a et M5 étendu sont communs. Reste à Lazar : M1 (version d'ON, moins de trois axes), M2b, M2c, M6 en réserves. (a) maintenu, 0,7. **Nouveau** : le critère (514 caractères, 532 octets) sort du texte servi et passe à l'annexe 3 de la fusion, le plafond de 12 000 étant tenu en octets (`wc -m` en locale POSIX compte des octets, comme la mesure de la v1) ; si le plafond se lit en caractères, il peut y revenir (11 997 caractères).
- **D14 (nouveau). Adopte-t-on les ajouts de méthode donnés par le collisionneur seul ?** Enjeu : biais de sélection, puissance, pseudo-réplication, contre fiches plus lourdes et moins de notables.
  (a) Les huit, tels que dans le texte (N2b, N3, N7, N8, N9, N12, N13, N16 ; texte à 11 946 octets, 11 482 caractères) : plus rigoureux ; plus d'obligations par fiche. (b) Seuls ceux de la recommandation 2 du collisionneur (N2b, N3, N7, N8, N9) :
  plus léger ; laisse le plancher non apparié à la sélection. (c) Aucun. Recommandation : (a), confiance 0,6. Défaut : (a).

## C. Les six questions du collisionneur pour Lazar (points « proposer avec recommandation », aucun n'est une porte)
**Q1. Étalonnes-tu les instruments de la course (analyseur, juges, mémoire anti-redite, vérification d'antériorité) sur des témoins plantés avant d'écrire et de lancer la question ?**
Enjeu : sans cela, la note d'une fiche n'a pas d'issue falsifiable. Options : (a) pré-pilote fondu en un préenregistrement (étalonnage de l'analyseur, signal à 8 milliards, rejet de 15 fiches défectueuses sur 20) : coût annoncé : au plus 4 dollars (C), quelques dollars (B), 10 à 30 dollars (A), non vérifié ;
sûr, mais retarde la course ; (b) course v1 qui sert d'expérience sur sa propre forme : plus rapide ; notes non fiables ; (c) lancement tel quel : contraire à l'avis des trois modèles. Recommandation : (a), confiance 0,8. Défaut : (a) **préparé** (préenregistrement scellé et contre-lu, devis rédigé) ;
aucune dépense ni aucun lancement sans GO sur devis ; la question reste non servie jusqu'au verdict.
**Q2. Quelles données sert-on aux proposeurs ?** Enjeu : fuite vers G1, circularité. Options : (a) le verdict du test nul seulement : sans fuite ; pauvre ; (b) une tranche isolée avec exécution : riche ; partition tierce et dépense ; (c) rien. Recommandation : (a), confiance 0,65.
Défaut : (a) ; la tranche D4 sort de la liste D, les notations brutes ne se servent que sur copies disjointes, les chiffres de P3 se servent comme verdict seul.
**Q3. Le vis-à-vis angle ↔ faille est-il une règle de notation ?** Enjeu : couplage voulu par la question-mère contre fiches creuses. Options : (a) compté et publié, ni noté ni condition de K1 jusqu'à un test : prudent ; le point 8 reste sans règle de notation ; (b) obligatoire dès la 2e génération : fidèle au point 8 ;
risque de remplissage vide ; (c) choix de conception non testé, tranché par toi. Recommandation : (a), confiance 0,6 (le collisionneur donne 0,65) ; remplace l'option (a) de D12 en v1. Défaut : (a).
**Q4. Comment note-t-on « inédit » ?** Enjeu : un dossier fermé ne prouve pas « non occupé ». Options : (a) note provisoire, puis définitive après une vérification ouverte étalonnée : solide ; coûte des appels ; (b) une citation des 23 papiers et une distance de plongement : bon marché ; dit seulement « non réfuté dans le dossier » ;
(c) statut « non réfuté par [procédure] à [date] », sans note. Recommandation : (c) jusqu'à la lecture de l'étalonnage, puis (a), confiance 0,7. Défaut : (c).
**Q5. Le signal à 8 milliards s'établit-il sur processeur ou sur trois tailles ?** Enjeu : « de meilleures sondes » n'a de sens que si le signal existe. Options : (a) sur processeur, avec les vecteurs existants, après lecture du registre pour la contradiction S6 : gratuit ; limité à la lisibilité ;
(b) sur 3, 8 et 70 milliards, stratifiés par le dommage : sépare m1 de m2 ; demande un GO, un changement de modèle (interdit sans GO) et un 70 milliards supposé disponible. Recommandation : (a), puis (b) sur devis si (a) est nul, confiance 0,7. Défaut : (a) ; l'axe 1 n'est servi qu'après verdict.
**Q6. Y a-t-il une règle d'arrêt de la boucle ?** Enjeu : la question-mère impose une mesure consignée d'abord. Options : (a) mesure seulement : sûre ; sans arrêt automatique ; (b) règle fondée sur la survie, comparée au plancher de deux sous-courses : automatique ; non étalonnée.
Recommandation : (a), confiance 0,75. Défaut : (a).

## D. Comptes et réserves
**Comptes v2** (v1 : 102 éléments ; v2 : 122 avec 18 éléments nouveaux et M2 scindé en trois) : **commun 52** (44 + J4, A7.5, P8 + N2a, N4, N5, N14a, M2a) ; **divergent 53** (41 − J4, A7.5, P8 − M2 + M2b, M2c + 14 nouveaux) ; écarté 2 ; circulaire 2 ; non jugeable 5 ; imposé 7 ; Argon seul 1.
Hors compte : aucune antériorité n'entre dans le texte ; la liste « à vérifier sur PDF » de la v1 est inchangée ; le collisionneur ne cite que des pièces du dossier.
**Réserves.** (1) Reste ouverte, entre A et C : les 240 épisodes de P3 appartiennent-ils au calibrage ou à l'évaluation de G1 ? Les « chiffres de P3 » restent en pièces, comme verdict seul ; à vérifier chez session-depot (cf. réserve 1 de la v1). (2) L'axe 4 sur familles scellées consomme du matériau d'épreuve avant G1 (réserve 2 de la v1, inchangée).
(3) Étiquetage des familles par un tiers sans garantie contre la fuite. (4) Je n'ai pas lu les cellules : un passage à « commun » qui reposerait sur une lecture erronée de la synthèse se corrige par la lecture des cellules (branche exclue de mon périmètre). (5) Les accords A avec CA (Fable 5.1) et B avec ON (Opus 5.5) sont des accords de même modèle.
