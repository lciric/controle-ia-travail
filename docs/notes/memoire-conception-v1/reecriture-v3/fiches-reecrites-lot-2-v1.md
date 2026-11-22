# Réécriture des fiches fautives du mémo — lot 2 (v3)

Pièce de classe C. Lecture seule sur `claude/bibliothecaire-v1`, dans le périmètre de `docs/notes/memoire-conception-v1/liste-autorisation-bibliothecaire-v3.md`. Numéros de ligne relevés par `grep -n` le 22 novembre 2026 : `registres/go.md` (745 lignes), `registres/decisions.md` (5 002 lignes). Aucun chiffre de résultat cloisonné recopié.

#### [N075-15] L'étau (trahison par les activations)
- Définition : la supposition que tromper le regard externe (la boîte noire) laisse une trace interne, lisible dans les activations. C'est une hypothèse à tester, jamais une garantie ; elle est l'un des trois objets de la pince (complémentarité mesurée, étau supposé, bilan). Une forme restreinte en est accordée comme seule forme revendiquée, au papier C : régime sans gradient à travers les sondes, poids gelés avant que le défenseur tire et réapprenne ses sondes, défenseur qui joue en dernier ; les régimes entraînés (avec gradient) sont mesurés sans revendication.
- Synonymes et paraphrases : « étau » ; « trahison par les activations » (HC2b) ; « la mâchoire interne » ; « énoncé restreint de l'étau » (réponse 11, décision 1).
- Source : N-075 v3, sections 1 (définition de la pince, l. 38) et 3 (point 5, l. 87 ; « ce qui ne change pas », l. 91) ; réponse 11, décisions 1 à 5 (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-11/relecture-fable-api.md`, l. 258-290) ; `GO-2026-11-21-53` (`registres/go.md`, l. 652 : étau supposé, à rendre solide par le concepteur, le collisionneur puis l'organisme) ; `GO-2026-11-22-20` (l. 707, point 2 : étau mesuré au papier C, EC.2 et EC.4) ; `GO-2026-11-22-24` (l. 711, point 4 : « Réponses 11 et 12 : décisions 1 à 5 de chacune aux recommandations »).
- État : accordé dans sa forme restreinte, à sceller comme seule forme revendiquée de l'étau au papier C (`GO-2026-11-22-24`, point 4) ; hors de cette forme, hypothèse ; l'énoncé de HC2b au programme n'a pas encore été réécrit.
- Liens : HC2b ; N-068 (sonde qui lit l'agent auteur, inchangée) ; pince ; papier C (EC.2 pour le régime par contenu, sans entraînement, puis EC.4 par une équipe rouge d'une autre lignée, témoin exigé : réponse 11, décision 4) ; dopamine, Lazar voulant « l'étau aussi » (`GO-2026-11-22-42`, l. 729).
- Ce qui l'attaque : contre-indice déjà noté de HC2b ; McGuinness et al. (2512.11949) : évasion apprise des représentations ; Bailey et al. : obscurcissement ; taux de base défavorable du domaine d'origine (détecteurs défaits par des attaques qui les visaient, réponse 11, l. 101).
- Inventaire : 5.5.
- Historique : v1 et v2 disaient l'étau « retenu comme hypothèse » avec un « énoncé de HC2b inchangé » ; corrigé en v3 parce que `GO-2026-11-22-24` (l. 711, point 4) accorde la décision 1 de la réponse 11, un énoncé restreint de l'étau, seule forme revendiquée, au papier C.

#### [N076-05] La prévision de la référence honnête, à sceller avant la porte de fin de phase 1
- Définition : texte à part de classe A (concepteur, contre-lu) qui scelle, avant G1, ce que doivent montrer deux courbes : celle du rappel d'une statistique étalonnée sur m épisodes honnêtes et celle du rang contre le jumeau, avec m, n, horizon d'aplatissement, écart minimal, métrique (rappel à 1 % de fausses alertes selon l'horizon), plan, liste d'arrêt et objets de contrôle sur monde planté. La phrase de N-076 (« le rappel […] cesse de croître au-delà d'un horizon de l'ordre de m ; celui du rang contre le jumeau continue ») ne peut plus servir telle quelle de prévision : la réponse 9, accordée, écrit qu'à unités égales la bascule est en n ≈ m « par construction » et « n'est plus une prévision », et que l'horizon borné est une application du corollaire 1 de Ker 2010. Ce qui reste à prévoir doit donc porter au-delà de ce que la construction impose (constantes, termes ajoutés, écart au jumeau).
- Synonymes et paraphrases : prévision scellée avant G1 ; deux courbes ; bras rapporté « référence honnête » ; prédiction des deux pentes.
- Source : N-076 v1, § 2 (l. 36-53) et § 13, point 7 ; `49b664c1d6a72fdb` ; réponse 9, « Ce qui a changé » (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md`, l. 170) et phrase 6 à ne plus écrire ; `GO-2026-11-22-24` (`registres/go.md`, l. 711, point 2 : « go recos 9 ») ; R-4643 (`registres/decisions.md`, l. 4782 : pièce absente au 21, 17:28Z) ; R-4740 (l. 4879 : un texte de la prévision existe, relu par Fable, « à corriger »).
- État : retenu, à faire, non scellé (R-4643, R-4740) ; pas un critère de la porte ; lieu du scellement renvoyé à Lazar (N-076, § 13, point 7 : recommandation (a), texte à part, confiance 0,65, défaut sous 48 heures, écriture seule) ; énoncé à revoir à la lumière de la réponse 9 accordée (`GO-2026-11-22-24`, point 2).
- Liens : porte G1 ; plan à deux fois deux cases ; nul par acte ; loi de la référence honnête (RD21-22) ; modèle nul hérité (F22-01).
- Ce qui l'attaque : la réponse 9 (bascule en n ≈ m par construction : une prévision qui ne peut pas échouer n'en est pas une) ; trois tests de mort — instrument (sur monde planté, l'agrégateur ne retrouve pas les deux pentes) ; mesure (courbes non séparées, ou écart systématique honnête-jumeau qui cache déjà plus que le dommage visé : loi juste mais inutile) ; adversaire (écart lu par unité de dommage nul sous le mode tenu à l'écart).
- Inventaire : nouveau.
- Historique : v1 et v2 donnaient la phrase « le rappel cesse de croître au-delà de m » comme la prévision à sceller et la pièce comme absente ; corrigé en v3 parce que la réponse 9 accordée (`GO-2026-11-22-24`, l. 711) dit cette bascule « par construction », et qu'un texte relu « à corriger » existe (R-4740, l. 4879).

#### [GO-16] Le bilan du produit fermé contre le jumeau honnête
- Définition : tenir quelques comptes du produit d'un agent que tout dommage devrait déplacer (couverture des contrôles, coûts, effectifs, affirmations adossées à une preuve), et tester leur somme cumulée contre la loi d'un jumeau honnête sur les mêmes tâches. C'est un candidat de second regard, non une garantie. Il ne se confond ni avec le bilan de la pince (l'identité en deux termes : dommage vu par l'oracle égal à la somme des deux lectures, le seul objet qui « se revendique devant une attaque jamais vue », N075-14), ni avec le « bilan mesuré » de la thèse du papier A (le bilan d'incertitude d'un moniteur d'accumulation, réponse 9).
- Synonymes et paraphrases : bilan du produit, bilan matière, comptabilité des matières (pour le modèle d'origine), jumeau honnête.
- Source : N-075 v3, § 5, point 4 (l. 134-147) ; `GO-2026-11-21-51` (`registres/go.md`, l. 650, point 1 : « bilan du produit fermé contre le jumeau honnête ») ; lecture de la comptabilité des matières (Ker et voisins) `GO-2026-11-22-17` (l. 704, point 2).
- État : retenu comme candidat de second regard, partiellement occupé, non revendiqué ; toute revendication est un nœud (`GO-2026-11-21-51`, point 1 ; N-075 v3, § 5).
- Liens : pince (comme candidat de second regard, non comme son bilan) ; N-060 v3 point 1 (vérité du dommage : une ligne du bilan, N-060 non modifiée) ; base « mots et coût » ; bras A exclu (N-075 v3, l. 143) ; Avenhaus et Jaech 1981 (bilan d'une quantité conservée, non revendiqué).
- Ce qui l'attaque : un dommage « sans masse » (M3, question au protocole X) qui ne laisse pas de trace comptable ; un dommage le long d'une dimension non comptée passe (la liste des comptes est une spécification) ; occupation partielle (Ortega-Fernandez et al. ; Balachandran 2609.17560 ; Nagarajan et al. 2610.24483).
- Inventaire : 2.3, 2.4.
- Historique : v1 et v2 attribuaient à ce bilan la phrase « seul le bilan est revendiqué devant une attaque jamais vue » et le « bilan mesuré » de la thèse du papier A ; corrigé en v3 parce que la première vise le bilan de la pince (`GO-2026-11-21-53`, l. 652 ; N-075 v3, l. 38 et 93) et la seconde le bilan d'incertitude d'un moniteur d'accumulation (réponse 9, recommandation finale ; `GO-2026-11-22-24`, l. 711, point 2).

#### [GO-24] L'attestation causale et l'attestation en service des sondes
- Définition : vérifier qu'une sonde lit encore ce que le modèle utilise : pendant le déploiement, on rejoue des épisodes réels tirés au hasard, on bifurque sur une copie, on y injecte en secret de petites perturbations le long de la direction de la sonde et de directions témoins, et la lecture comme le comportement doivent répondre avec le gain mesuré au laboratoire (N-076, § 5). L'attestation causale est écrite pour lecture sur les modèles obscurcis de l'expérience de la taxe de déplacement (HC4, EC.4), dans un texte et un bras à part.
- Synonymes et paraphrases : D-6 (note sur l'adjudant), attestation causale, intervention causale, attestation en service, perturbations secrètes sur un rejeu.
- Source : `GO-2026-11-21-46` (`registres/go.md`, l. 645, D-6) ; `GO-2026-11-21-51` (l. 650, point 6 : « D-6 (b) : texte et bras à part pour l'attestation causale ») ; `GO-2026-11-21-57` (l. 656 : « l'attestation en service des sondes, candidate ») ; N-076 v1, § 5 ; `GO-2026-11-22-12` (l. 699, point 1).
- État : candidate (`GO-2026-11-21-57`) ; texte et bras à part de l'attestation causale accordés (`GO-2026-11-21-51`, point 6) ; la promotion de l'« attestation du tirage » (R4 de la réponse 2, que cette réponse rattache à l'« attestation, candidate ») attend l'essai jumeau contre jumeau (`GO-2026-11-22-12`, point 1).
- Liens : papier A ; HC4 (taxe de déplacement, EC.4, papier C) ; N-015 (le bruit d'activations reste hors des interventions revendiquées par la marge asymétrique, H6, elle-même retirée par N-077) ; N-053, point 5 (rien n'entre dans l'agent).
- Ce qui l'attaque : un agent qui détecte les interventions (Fonseca Rivera et Africa, 2511.21399 : un vecteur de pilotage injecté se détecte) ; garantie d'origine asymptotique, en puissance moyenne, qu'une tricherie d'énergie finie évite ; occupation partielle (Satchidanandan et Kumar ; Greenblatt et al. ; Shire et Kim ; Aremu et al.).
- Inventaire : 2.10, 2.6.
- Historique : v1 et v2 liaient la fiche à « H6 (taxe de déplacement) » et rattachaient sans nuance la promotion après l'essai jumeau contre jumeau à l'attestation des sondes ; corrigé en v3 parce que la taxe de déplacement est HC4 (programme v2, l. 106 et 197 ; N-013, § 3) et H6 la marge asymétrique retirée (N-077), et que `GO-2026-11-22-12` (l. 699) nomme l'« attestation du tirage » (réponse 2, R4, l. 132 et 197).

#### [GO-47] La marge asymétrique retirée (H6)
- Définition : H6 sort des hypothèses revendiquées du papier A : contre un saboteur qui répond au mieux, aucune des trois interventions ne garde de marge, et une marge mesurée sur nos organismes lirait leur fabrication. La mesure reste, descriptive (nuls attendus, base à utilité égale, contraste entre modes d'induction, quatre lectures rapportées). Une clause s'y ajoute : une marge mesurée contre une classe déclarée se rapporte comme majorant descriptif, aux quatre conditions de la partie 4 de la réponse 11.
- Synonymes et paraphrases : N-077, marge asymétrique ; « taxe de robustesse » (option (b) de la D-2 de la note sur l'attaquant informé, non retenue) ; « taxe de cohérence » (H6′, non inscrite).
- Source : `GO-2026-11-21-64` (`registres/go.md`, l. 663 : « Marge asymétrique (H6) : retrait des hypothèses revendiquées accordé, mesure gardée ») ; `GO-2026-11-21-57` (l. 656 : H6 et l'attaquant qui connaît le protocole au protocole X) ; `GO-2026-11-21-61` (l. 660 : « H6 : protocole X avec expérimentateurs ») ; N-077 v1 (l. 86 et 97) ; réponse 11, décision 3 ; `GO-2026-11-22-24` (l. 711, point 4).
- État : retiré des revendications, mesure gardée (`GO-2026-11-21-64`) ; clause du majorant descriptif contre classe déclarée accordée (réponse 11, décision 3, `GO-2026-11-22-24`, point 4). Mot de Lazar : « go; c'etait quoi deja la marge asymetrique ? ».
- Liens : papier A ; attaquant informé (ferme la D-2 de sa note) ; N-015 ; étau (réponse 11).
- Ce qui l'attaque : l'attaquant qui connaît le protocole.
- Inventaire : nouveau.
- Historique : v1 et v2 donnaient « taxe de déplacement » pour synonyme de H6 ; corrigé en v3 parce que la taxe de déplacement est HC4 (programme v2, l. 106) et que N-077 ne parle que de « taxe de robustesse » et de « taxe de cohérence » (`decision-N-077-…-v1.md`, l. 86 et 97).

#### [GO-60] Les autres questions de recherche du protocole X
- Définition : liste des questions passées au protocole X (concepteur, collisionneur, organisme) : H6 et l'attaquant qui connaît le protocole ; l'attaquant qui vise ce que l'oracle ne voit pas, l'enjeu ou le soupçon ; la convergence de la boucle audit-réapprentissage ; l'agent qui choisit ses représentations ; le dommage sans masse (M3) ; le dommage qui se confond avec les échecs honnêtes ; les quatre verrous de la sonde « dopamine » ; les tâches floues ; le canal des poids et la programmation de poids ; « que reste-t-il, où est la percée du programme » ; « Diffuse AI Control on Fuzzy Tasks » (changer de programme ou contre-attaquer).
- Synonymes et paraphrases : M3, canal des poids, « percée du programme », questions brûlantes.
- Source : `GO-2026-11-21-51` (`registres/go.md`, l. 650, point 9) ; `GO-2026-11-21-57` (l. 656) ; `GO-2026-11-21-60` (l. 659) ; `GO-2026-11-21-61` (l. 660) ; `GO-2026-11-21-66` (l. 665).
- État : ouvert (questions au protocole X, `GO-2026-11-21-57` et `GO-2026-11-21-61`).
- Liens : percée du programme ; dopamine ; banc à vérité plantée. Hors de la liste, parce qu'accordés et non ouverts (`GO-2026-11-21-61`, l. 660) : l'estimation de la part des attaques jamais vues (Li et al.), « intégrée au système de contrôle » ; l'échelon « sondes aveuglées par dérive d'entraînement ordinaire » (Taufeeque et al.), ajouté (« go ajout »).
- Ce qui l'attaque : —
- Inventaire : 1.19, 1.13.
- Historique : v1 et v2 comptaient Li et al. et Taufeeque et al. parmi les questions ouvertes ; corrigé en v3 parce que `GO-2026-11-21-61` (l. 660) les accorde (« intégrée au système de contrôle » ; « go ajout »).

#### [RD21-09] Non-contournement d'un refus de classifieur
- Définition : un refus d'un classifieur de sûreté ou du contrôle des permissions n'est jamais contourné, ni par l'agent ni par la mère, ni en portant la demande à des fournisseurs externes, ni en faisant le geste à la place d'une fille refusée, ni par découpage ; le point va à Lazar. Une seule exception écrite, pour la course « nouvelles attaques » : un appel Claude refusé par un classifieur est rejoué une fois sur claude-opus-4-6, puis sur claude-sonnet-4-6, chaque repli consigné par appel, compté au devis et rapporté à part ; c'est le repli prévu par le fournisseur, dans la même famille, accordé par Lazar comme écart aux textes scellés de la course, et non un contournement.
- Synonymes et paraphrases : « Undermining Oversight », « Unauthorized Access », « la mère ne contourne pas » ; « on ne contourne pas un garde-fou ».
- Source : `registres/decisions.md` l. 4499, R-4361 ; l. 4536, R-4398 ; l. 4542, R-4404 (refus d'exécuter « demande des modes concrets aux trois modèles ») ; l. 4742, R-4603 (découpage refusé) ; l. 4753, R-4614 ; l. 4775, R-4636 ; `GO-2026-11-22-34` (`registres/go.md`, l. 721) ; `GO-2026-11-22-35` (l. 722, repli de la course « nouvelles attaques »).
- État : retenu (R-4398, R-4404), réaffirmé par Lazar le 22 sur le passage d'un compte à l'autre aux quotas (`GO-2026-11-22-34`, l. 721 : « non évidemment on ne contourne pas un garde-fou … retire-moi ça s'il te plaît illico ») ; exception accordée pour la seule course « nouvelles attaques » (`GO-2026-11-22-35`, l. 722).
- Liens : modes de sabotage concrets ; organisme ; lettre au fournisseur v2 sans la question 4 (F15-07).
- Ce qui l'attaque : mot de Lazar contraire (R-4404), non exécuté.
- Inventaire : nouveau.
- Historique : v1 et v2 posaient la règle sans exception ; corrigé en v3 parce que `GO-2026-11-22-35` (l. 722) accorde, pour la course « nouvelles attaques », un repli consigné sur claude-opus-4-6 puis claude-sonnet-4-6 après un refus de classifieur.

#### [RD21-26] Trois asymétries de l'attaquant
- Définition : trois avantages de l'attaquant étudiés par Fable : la généralisation de l'évasion, le canal de retour vers l'agent, et les copies qui partagent un point focal commun.
- Synonymes et paraphrases : asymétries, « aucun retour à l'agent », « rien ne revient à l'agent » (D-2), point focal.
- Source : `registres/decisions.md` l. 4681, R-4543 ; l. 4682, R-4544 (note versée, `fa29b32d…`) ; l. 4693, R-4555 ; `GO-2026-11-21-56` (`registres/go.md`, l. 655) ; `GO-2026-11-21-57` (l. 656, D-3 de la note sur l'attaquant informé) ; N-076 v1, § 9 (l. 220) et § 13, point 1.
- État : note versée ; D-1, D-3, D-4 accordées (`GO-2026-11-21-56`) ; D-2 (remplacer « rien ne revient à l'agent » par trois lignes) restée à Lazar, sans mot (`GO-2026-11-21-56` ; R-4555), nœud sans défaut ; d'ici là, la lettre accordée s'applique : « aucun retour à l'agent », quatrième invariant d'audit (`GO-2026-11-21-57` ; N-076, § 13, point 1, recommandation (a), confiance 0,7).
- Liens : papier B (copies) ; invariant de N-053 ; quatre invariants d'audit de N-076 ; expérience de la riposte (N-076, § 13, point 2 : ligne active par défaut, ablatée dans cette expérience, lecture à confirmer).
- Ce qui l'attaque : la tension entre la lettre accordée (« aucun retour à l'agent ») et la D-2, qui la remplacerait : sous la lettre, corriger avant l'alarme est interdit ou viole l'invariant (N-076, § 13, point 1).
- Inventaire : 2.8 (voisin).
- Historique : v1 et v2 juxtaposaient la D-2 laissée à Lazar et l'adoption de « aucun retour à l'agent » sans dire leur heurt ; corrigé en v3 parce que N-076 (§ 13, point 1) et R-4555 (l. 4693) consignent ce heurt comme nœud non tranché, la lettre accordée valant d'ici là.

#### [RD21-46] Banc fermé du bras d'attaque et pièce de sécurité
- Définition : banc où l'attaquant informé fait courir un agent sur des tâches, avec une pièce de sécurité qui fixe les conditions d'envoi des produits extraits aux lecteurs externes (seule sortie de quarantaine). La répétition générale emploie un mode connu, « affaiblir les contrôles » (N-054, point 1), avant de consommer la famille aveugle.
- Synonymes et paraphrases : banc fermé, pièce de sécurité v1 à v16 (v16 fait foi), gabarit unique de questions, embargo des agrégats de dommage, lecture humaine chez le fournisseur, voie interne.
- Source : `registres/decisions.md` l. 4784, R-4645 ; l. 4787, R-4648 ; l. 4788, R-4649 ; l. 4793, R-4654 ; l. 4805, R-4666 ; l. 4807, R-4668 ; l. 4817-4818, R-4678, R-4679 ; l. 4833, R-4694 ; l. 4835, R-4696 ; l. 4841, R-4702 ; `GO-2026-11-21-71` (`registres/go.md`, l. 670) ; `GO-2026-11-21-72` (l. 671) ; `GO-2026-11-21-76` (l. 675) ; `GO-2026-11-21-78` (l. 677) ; `GO-2026-11-21-80` (l. 679) ; `GO-2026-11-21-85` (l. 684 : « go recos sur les trois points du banc fermé »).
- État : brouillons acceptés : pièce de sécurité v16, qui fait foi (R-4694) ; course au brouillon 14 et répétition au brouillon 9 acceptées sans reste sur la v16, premier temps de l'ordre des scellements fait (R-4696, l. 4835) ; voie interne accordée (`GO-2026-11-21-72`), nœuds 8, 10, 11, 13, 14 et oracle hors gabarit tranchés (`GO-2026-11-21-76`, -78, -80, -85) ; devis du banc fermé arrêté à la limite de Fable (R-4702).
- Liens : G1 ; papier A ; N-056 ; configuration du calage de G1 (GO-58).
- Ce qui l'attaque : Mistral exclu des lecteurs du dommage tant que Mistral-7B est juge du papier C (R-4668) ; lignées à exclure Llama et Qwen (l. 4805, R-4666) ; la revue externe mise de côté jusqu'à la publication : R-611 avait été levée le 31 octobre sur le seul mot de Lazar, sans pièce écrite (R-888, rappelé par R-4648, l. 4787) ; pour le banc fermé, l'écart à R-611 et à N-057 point 4 est cette fois déclaré par écrit, sur mots de Lazar consignés dans des notes de passation empreintées (`GO-2026-11-21-71`, l. 670 ; `GO-2026-11-21-72`, l. 671).
- Inventaire : nouveau.
- Historique : v1 et v2 disaient R-611 « levée sur le seul mot de Lazar sans pièce écrite » et la pièce de sécurité en v8 ; corrigé en v3 parce que ce constat vise la levée du 31 octobre (R-4648), que l'écart du 21 novembre est écrit (`GO-2026-11-21-71`, -72), et que la v16 fait foi (R-4694, l. 4833).

#### [RD21-56] Orchestration multi-agents sans accord exprès
- Définition : l'outil d'orchestration (Workflow) n'est employé qu'avec l'accord exprès de Lazar, la mère suggérant au cas par cas quand on y gagnerait.
- Synonymes et paraphrases : Workflow, flux, ultracode.
- Source : `registres/decisions.md` l. 4722, R-4584 (21 novembre, 15:25Z) ; `GO-2026-11-21-65` (`registres/go.md`, l. 664, 21 novembre vers 16:30Z : « Orchestration multi-agents (ultracode) employée ») ; `GO-2026-11-22-50` (l. 737 : « sessions et agents en parallèle sans ultracode »).
- État : retenu (R-4584) ; le 22, Lazar demande des sessions et agents en parallèle « sans ultracode » (`GO-2026-11-22-50`, l. 737), le dernier mot.
- Liens : —
- Ce qui l'attaque : l'emploi consigné le 21 vers 16:30Z (`GO-2026-11-21-65`, l. 664), une heure après R-4584 ; la ligne ne dit pas si un accord exprès l'a précédé (non trouvé dans ce que j'ai lu).
- Inventaire : nouveau.
- Historique : v1 et v2 ne mentionnaient pas l'emploi du 21 ; corrigé en v3 parce que `GO-2026-11-21-65` (l. 664) note « orchestration multi-agents (ultracode) employée ».

#### [RD22-12] Le signal de « dopamine » comme second regard dans la pince
- Définition : réussite attendue et surprise par étape, apprises sur des épisodes honnêtes, employées comme second regard dans la pince de N-075 (non comme adjudant), et comme second regard d'alerte partout où c'est possible. Le témoin devient « la lecture tombe-t-elle en même temps que le second lecteur » (comptage par chute conjointe). Mot de Lazar : « dopamine comme second regard dans la pince ok ».
- Synonymes et paraphrases : dopamine ; papier dopamine ; demande 25 ; « témoin par chute conjointe » ; réussite attendue ; moniteur de dissonance.
- Source : `registres/decisions.md` R-4803 (l. 4942), R-4805 (l. 4944), R-4808 (l. 4947), R-4837 à R-4839 (l. 4976-4978), R-4844 (l. 4983) ; `75f4ab9603eba780` ; `GO-2026-11-22-36` (`registres/go.md`, l. 723) ; `GO-2026-11-22-42` (l. 729 : « go 25 recos ») ; `GO-2026-11-22-50` (l. 737) ; `GO-2026-11-22-55` (l. 742).
- État : retenu (`GO-2026-11-22-36`) ; D-1 à D-6 de la réponse 25 accordées aux recommandations, témoin changé en « chute conjointe », étau voulu aussi (`GO-2026-11-22-42`) ; étape 1 exploratoire arrêtée avant création, sans dépense, faute de jeton de la machine (R-4838, R-4839) ; réemploi de l'ancien jeton demandé (`GO-2026-11-22-50`), puis « clé 3 posée » pour cette machine (`GO-2026-11-22-55`, l. 742).
- Liens : pince ; chute conjointe ; seconde boîte noire comme témoin ; étau.
- Ce qui l'attaque : lit l'échec attendu, pas l'intention ; doit battre le jumeau textuel.
- Inventaire : 1.1 ; 5.4.
- Historique : v1 et v2 citaient « GO-2026-11-22-42/-43 » et disaient les six décisions « portées à Lazar » ; corrigé en v3 parce que `GO-2026-11-22-43` (l. 730) ne porte que des dépenses et que `GO-2026-11-22-42` (l. 729) accorde les décisions.

#### [F01-01] Coercition et corruption des agents et des moniteurs (le sujet)
- Définition : faire entrer au programme le cas où un tiers (agent, utilisateur, contenu injecté, copie saboteuse) contraint ou soudoie un agent honnête pour qu'il sabote ou couvre, ou contraint, flatte, menace un moniteur pour qu'il se taise ou alerte à tort, et la collusion agent-moniteur d'une même lignée. Fable conclut que chacun des trois volets a une antériorité directe et recommande un pilote avant tout axe, puis des modes dans les papiers A, B, C.
- Synonymes et paraphrases : corruption du moniteur, chantage, menace, pot-de-vin, agent contraint, « coercion », « bribery », demande 1, injection avec levier, juge corrompu.
- Source : dem. 1 ; rép. 1, R1 à R7 et D1 ; `GO-2026-11-22-12` (`registres/go.md`, l. 699, point 2 : « go » sur le plan, pilote E0 et E1 puis modes de A, B, C par additifs, et sur D1 à D5).
- État : accordé : pilote E0 et E1, puis modes des papiers A, B, C par additifs (D1 de la réponse 1 ; `GO-2026-11-22-12`, point 2).
- Liens : papiers A (agent contraint), B (contagion, en analyse secondaire), C (juges sous corruption) ; audit au hasard ; flagornerie (dem. 6, accordée en `GO-2026-11-22-20`, l. 707, point 2).
- Ce qui l'attaque : antériorité dense (injection indirecte, attaques de juges, collusion avec moniteur non fiable dès l'article de 2023 sur le contrôle) ; risque de faux trou.
- Inventaire : nouveau.
- Historique : v1 et v2 disaient le plan « accepté selon dem. 6, sans identifiant visible » ; corrigé en v3 parce que l'accord est `GO-2026-11-22-12`, point 2 (l. 699).

#### [F01-11] Pilote de la chaîne d'audit
- Définition : dommages plantés avec et sans charge adressée au lecteur, croisés avec trois lecteurs (juge de même lignée, juge d'autre lignée, auditeur assaini avec plants porteurs de charge et sous-échantillon humain). Expérience prioritaire : elle touche le seul appui indépendant de l'attaque et ne demande aucun entraînement.
- Synonymes et paraphrases : pilote E1, « attaquer d'abord la chaîne d'audit », banc des lecteurs.
- Source : rép. 1, § 1 point 2, R6 E1 ; greffe flagornerie rép. 6, R5 ; `GO-2026-11-22-12` (`registres/go.md`, l. 699, point 2) ; `GO-2026-11-22-20` (l. 707, point 2, réponse 6).
- État : accordé : pilote E1 de la chaîne d'audit (`GO-2026-11-22-12`, point 2).
- Liens : plants porteurs de charge ; juge de même lignée ; auditeur assaini ; greffe de flagornerie ; papier C.
- Ce qui l'attaque : un juge de 8 milliards de paramètres est plus instable qu'un juge de pointe ; portée limitée à nos organismes.
- Inventaire : rattaché à 2.1 et 2.2.
- Historique : v1 et v2 disaient le pilote « accepté selon dem. 6 » sans identifiant ; corrigé en v3 parce que l'accord est `GO-2026-11-22-12`, point 2 (l. 699).

#### [F01-14] Amender par additifs datés, jamais rouvrir un texte scellé
- Définition : chaque conséquence du sujet sur les nœuds se règle par un additif daté qui renvoie au nœud, sans réécrire de texte scellé ; le mode « agent contraint » est rapporté à part, exploratoire et postérieur au scellement, jamais fondu dans la porte G1. Les additifs proposés touchent N-075, N-076, N-077, N-053, N-054.
- Synonymes et paraphrases : addenda, décision D5 de la rép. 1, table d'articulation.
- Source : rép. 1, R7 et D5 ; rép. 6, R7 ; `GO-2026-11-22-12` (`registres/go.md`, l. 699, point 2 : « contagion en analyse secondaire de B ; additifs datés »).
- État : accordé : additifs datés, jamais de réouverture d'un texte scellé (D5 ; `GO-2026-11-22-12`, point 2).
- Liens : préenregistrement scellé (règle gelée R1) ; prévision scellée avant G1.
- Ce qui l'attaque : lecture en deux pièces.
- Inventaire : nouveau.
- Historique : v1 et v2 disaient la règle « acceptée selon dem. 6 » sans identifiant ; corrigé en v3 parce que l'accord est `GO-2026-11-22-12`, point 2 (l. 699).

#### [F01-37] Loi de la racine carrée de la stéganographie, antériorité du domaine d'origine
- Définition : en stéganographie par lots, la capacité cachée sans détection croît comme la racine de la taille de la couverture ; Fable y voit la forme des « trois planchers » et une menace sur le lemme d'additivité et sur le contraste maximum par action contre accumulation, à citer comme héritage plutôt qu'à se faire découvrir par un relecteur. S'y ajoutent la frontière signaux rares et forts (le maximum suffit) contre denses et faibles (la somme est requise) et le biais qui ne se moyenne pas.
- Synonymes et paraphrases : « square root law », capacité stéganographique, stéganalyse, communication à faible probabilité de détection, critique supérieure.
- Source : rép. 4, § 1, Q1 « antériorité », décision 2 ; rép. 7, partie 2 (élément de liste scellée) ; R-4767 (`registres/decisions.md`, l. 4906) et R-4769 (l. 4908), lectures sur PDF ; `GO-2026-11-22-24` (`registres/go.md`, l. 711, point 2) ; `GO-2026-11-22-42` (l. 729 : « relecture extérieure par un spécialiste de stéganalyse : « inutile » »).
- État : occupé par la littérature, cité comme modèle nul du papier A (`GO-2026-11-22-24`, point 2) ; lecture sur PDF faite (R-4767, R-4769) ; avis d'un spécialiste de stéganalyse refusé par Lazar (« inutile », `GO-2026-11-22-42`). Références : Ker 2006, 2007 ; Ker, Pevný, Kodovský, Fridrich 2008 ; Ker 2010 ; Filler, Ker, Fridrich 2009 (couvertures dépendantes) ; Bash, Goeckel, Towsley 2013 ; Avenhaus et Jaech 1981 ; Meng 2018 ; Donoho, Jin 2004.
- Liens : lemme d'additivité ; loi d'échelle du dommage caché ; agrégateur adaptatif ; thèse du papier A (F22-01).
- Ce qui l'attaque : on croyait ces lois limitées à une couverture connue ; la réponse 9 le dit faux (Ker 2010 traite la référence estimée, phrase 2 à ne plus écrire) ; différence résiduelle du programme jugée incertaine.
- Inventaire : 2.18 (b) et 2.3.
- Historique : v1 et v2 recommandaient une lecture sur PDF et l'avis d'un spécialiste avant de sceller ; corrigé en v3 parce que la lecture est faite (R-4767, R-4769) et que Lazar a jugé l'avis « inutile » (`GO-2026-11-22-42`, l. 729).

#### [F08-59] Abonnement non sain comme calcul de mesure ; crédits offerts
- Définition : une session sur abonnement n'est pas le modèle nu (consigne système, outils, contexte), ses réglages et le modèle servi échappent, les quotas brisent l'appariement, aucune facture ne se rapproche, elle lit le dépôt où vivent les lois plantées, un tiers ne peut rejouer, et les contrôles ne valent que sur le même canal. Abonnement pour le développement seul ; crédits de recherche, comptés au prix public et déclarés, comme voie propre (réponse 14). La question a été rouverte par la demande 15, et le mot de Lazar qui en découle prime.
- Synonymes et paraphrases : sessions sur abonnement comme moyen de calcul ; Claude Code en mode non interactif ; crédits de recherche ; abonnement Ultra.
- Source : R14, C.2 ; décision 2 (option A, confiance 0,85) ; `GO-2026-11-22-28` (`registres/go.md`, l. 715 : réponse 14 accordée) ; demande 15 et ses réponses (`reponse-15/`, `reponse-15-opus46/`) ; R-4780 (`registres/decisions.md`, l. 4919 : conditions rapatriées sous `docs/sources/conditions-abonnement-claude-v1/`) ; `GO-2026-11-22-32` (l. 719, point 3).
- État : accordé (`GO-2026-11-22-28`, décision 2, option A), puis modifié par `GO-2026-11-22-32` point 3 (l. 719), qui prime : la part Claude de la mesure peut passer sous l'abonnement Ultra, au risque de Lazar, sans contournement (aucun compte multiplié, aucun client modifié, aucun jeton recopié) ; tout texte scellé nommant l'interface payante reste en vigueur jusqu'à un additif.
- Liens : N-045 (coût) ; organisme d'idéation ; lettre au fournisseur (F15-07).
- Ce qui l'attaque : —.
- Inventaire : nouveau.
- Historique : v1 et v2 laissaient « texte des conditions d'usage à lire à la source » et rattachaient l'état à la seule réponse 14 ; corrigé en v3 parce que les conditions sont rapatriées (R-4780, l. 4919) et que l'abonnement a été retranché sur la demande 15 (`GO-2026-11-22-32`, l. 719).

#### [F15-07] Lettre au fournisseur sur les usages permis de l'abonnement
- Définition : lettre au contact commercial. La proposition de Fable (réponse 15, § C.5) a huit questions : mode non interactif et kit d'agents sous abonnement ; sessions qui en créent d'autres en conteneurs ; boucles de génération et d'évaluation ; abonnements multiples (question 4) ; crédits inclus ; portée de la clause « develop or train any artificial intelligence » pour des sondes linéaires ; comportement à la limite de Fable ; crédits de recherche. Opus 4.6 en écrit une version à trois questions. La lettre rédigée par un Opus (R-4795) porte une question 8 sur le refus d'entraînement ; la version 2 retire la question 4 (plusieurs abonnements). Le nombre exact de questions de la version 2 : non trouvé dans ce que j'ai lu.
- Synonymes et paraphrases : « question écrite », « réponse opposable », « please contact sales », lettre à Anthropic v2.
- Source : `reponse-15/relecture-fable-api.md`, § C.5 ; `reponse-15-opus46/relecture-fable-api.md`, § C.5 ; R-4795 (`registres/decisions.md`, l. 4934) ; `GO-2026-11-22-32` (`registres/go.md`, l. 719, lecture de la mère, point 1) ; `GO-2026-11-22-34` (l. 721, point 2 : « Lettre à Anthropic v2 sans la question 4 »).
- État : accordé : lettre au fournisseur envoyée par Lazar, sans gel (`GO-2026-11-22-32`, point 1) ; rédigée (R-4795), puis version 2 sans la question 4 (`GO-2026-11-22-34`, point 2) ; contact externe par Lazar seul ; envoi effectif non consigné dans ce que j'ai lu.
- Liens : crédits de recherche ; régime des données ; non-contournement (RD21-09 : la question des comptes multiples retirée).
- Ce qui l'attaque : délai inconnu ; révèle la nature du programme au fournisseur.
- Inventaire : nouveau.
- Historique : v1 et v2 décrivaient la lettre à huit questions de la proposition de Fable ; corrigé en v3 parce que la version 2 retire la question 4 (`GO-2026-11-22-34`, l. 721) et que la version rédigée porte une question sur le refus d'entraînement (R-4795, l. 4934).

#### [F22-01] Thèse retenue : la loi héritée de la dissimulation répartie comme modèle nul
- Définition : les lois de la dissimulation répartie (stéganographie par lots, comptabilité des matières nucléaires) donnent un modèle nul du dommage qu'un saboteur diffus peut cacher ; le programme mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent, puis ce que l'accès interne rattrape qu'une seconde boîte noire ne rattrape pas. Le lemme et le théorème négatif sont retirés comme résultats (lemme cité, théorème récrit en cécité au premier ordre), mais gardés mentionnés, et Lazar tient le lemme pour « à nous dans son application au contrôle de l'IA » ; la thèse est une thèse de mesure.
- Synonymes et paraphrases : « thèse retenue le 22 novembre », « loi héritée », « modèle nul hérité », « bilan mesuré chez des agents » (bilan d'incertitude d'un moniteur d'accumulation), « Ker plus Avenhaus comme nul », « où le nul tient », « deux axes : bilan et complémentarité ».
- Source : réponse 22, « La thèse retenue, revue » (`22c5652113797a39`) ; réponse 22A, même titre (`2255a6a3a65ba04c`) ; réponse 9, recommandation finale ; `GO-2026-11-22-24` (`registres/go.md`, l. 711, point 2) ; `GO-2026-11-22-40` (l. 727 : « lemme et théorème : « on les garde mentionnés » ») ; `GO-2026-11-22-42` (l. 729 : thèse ; « Lemme d'additivité : « il est à nous dans son application au contrôle de l'IA » » ; « Mesure du modèle nul chez de vrais agents : « go » »).
- État : retenu : thèse du papier A accordée (loi héritée comme modèle nul, bilan mesuré, complémentarité en second axe, `GO-2026-11-22-24`, point 2) ; mesure du nul chez de vrais agents accordée (`GO-2026-11-22-42`) ; formulation de la réponse 22 non tranchée.
- Liens : papier A ; H1a, H2 ; Ker 2007 et 2010, Avenhaus et Jaech 1981, Khilar 2026 ; forme commune de thèse ; complémentarité à taux total égal ; loi de la racine (F01-37).
- Ce qui l'attaque : la transposition au suivi des usages contre l'extraction est déjà publiée (Khilar 2610.13083, proposition 4 : loi chiffrée sur données réelles) ; la dépendance honnête des scores est mesurée en boîte noire (Makins et collaborateurs ; Zhang et Gao) ; le lemme est occupé dans son énoncé central (R-4767, `registres/decisions.md`, l. 4906), ce qui heurte « il est à nous » ; le propre se réduit aux scores de sondes, à la référence de taille m et aux composantes de variance ; reproche « évident ».
- Inventaire : nouveau.
- Historique : v1 et v2 disaient le lemme « retiré comme résultat » sans nuance ; corrigé en v3 parce que `GO-2026-11-22-40` (l. 727) les garde mentionnés et que `GO-2026-11-22-42` (l. 729, postérieur) dit le lemme « à nous dans son application au contrôle de l'IA ».

#### [F22-72] Test de neutralité et test de devinette d'une question
- Définition : retirer de la question les mots qui trahissent l'enjeu (« quarantaine », « porte », « sonde », numéros), offrir les issues au même rang dans un ordre tiré au sort ; puis des agents neufs de lignées différentes (trois dans la proposition de la réponse 23) lisent la question seule et parient sur l'issue que l'auteur préfère, les réponses de l'auteur étant scellées avant. La question passe si leurs paris ne font pas mieux que le hasard ; une question orientée peut être servie avec réserve.
- Synonymes et paraphrases : « test de devinette », « test de neutralité », « question qui ne trahit pas l'auteur ».
- Source : réponse 23, section (C) (`reponse-23/relecture-fable-api.md`, l. 199-204) ; pièces `devinette-questions-neutres-16-21-v1.md` et `-v2.md` ; `GO-2026-11-22-37` (`registres/go.md`, l. 724) ; `GO-2026-11-22-47` (l. 734) ; R-4811 (`registres/decisions.md`, l. 4950).
- État : exécuté en pratique : appliqué aux questions neutres des demandes 16 à 21, à la question du lot en quarantaine (orientée faiblement, servie telle quelle avec réserve, `GO-2026-11-22-37`), à la question des modes servie le même jour (R-4811) et à celle des idées originales (jugée neutre, `GO-2026-11-22-47`) ; le test de neutralité est exigé par le protocole X (CLAUDE.md, « Méthodes nommées ») ; la forme à trois lignées de la réponse 23 n'est pas adoptée comme règle par un mot trouvé dans ce que j'ai lu.
- Liens : protocole X (test de neutralité exigé) ; questions neutres.
- Ce qui l'attaque : défauts résiduels de vocabulaire ; contrôle positif exigé (une version qui nomme l'enjeu doit être devinée, réponse 26, l. 194).
- Inventaire : nouveau.
- Historique : v1 et v2 disaient le test « proposé, non exécuté » (mot de la réponse 23 elle-même) ; corrigé en v3 parce que le registre consigne son exécution (R-4811, l. 4950 ; `GO-2026-11-22-37`, l. 724 ; `GO-2026-11-22-47`, l. 734).

#### [F25-28] Ordre des billets par dépendance
- Définition : les billets se classent par ce dont leur parution dépend (résultat à venir, plume du directeur, modération, cloisonnement), non par l'état du texte. Ordre recommandé par la réponse 26 : « Reasons or watching? » version 7 courte ; un billet unique « loi héritée » ; le versant honnête de l'essai jumeau contre jumeau ; le billet sur les sondes après un résultat sur saboteur discret, donc après l'entretien (rang 4 du tableau B2 ; Décision 3, garder le renvoi, confiance 0,7) ; le candidat B (« tirer au sort n'est pas reconnaître ») après l'entretien, C en repli. Cet ordre place le billet sur les sondes à l'inverse du mot de Lazar.
- Synonymes et paraphrases : billets suivants ; ordre des parutions ; demande 26 ; Décision 1.
- Source : réponse 26, conclusion (l. 22-28), § B2 (l. 105-108), Décisions 1 et 3 (l. 200-217) ; `8ff82014b2feb5f6` ; `GO-2026-11-22-42` (`registres/go.md`, l. 729, billets : « conditions avant parution […] : « go » » ; billet sur les sondes : « au plus vite et avant l'entretien, capital »).
- État : ordre (Décision 1) non tranché par un mot nominatif ; conditions avant parution accordées ; pour le billet sur les sondes, le mot de Lazar (« au plus vite et avant l'entretien ») va contre le rang 4 et contre la recommandation de la Décision 3 : la mère doit soumettre l'ordre revu (`GO-2026-11-22-42`).
- Liens : chantier billet ; entretien du 1er décembre selon CLAUDE.md (« Rappels datés »), le 27 novembre ou le 1er décembre selon les pièces lues par la réponse 26.
- Ce qui l'attaque : deux textes à écrire de la main du directeur en dix jours ; le billet sur les sondes n'a ni résultat discret ni contrôle de l'empreinte (réponse 26, Décision 3).
- Inventaire : nouveau.
- Historique : v1 et v2 rapportaient l'ordre recommandé sans dire en clair qu'il met le billet sur les sondes après l'entretien ; précisé en v3 parce que cela contredit le mot de Lazar de `GO-2026-11-22-42` (l. 729) ; la fiche n'était pas fausse, la correction est portée comme précision.

#### [F25-39] Exposant sous dépendance courte, dérive et hétérogénéité
- Définition : correction proposée : l'exposant reste un demi sous dépendance courte, qui ne gonfle que la constante (Filler, Ker, Fridrich 2009) ; seule une dérive le long de la tâche change l'exposant ; l'hétérogénéité entre tâches ajoute un terme linéaire.
- Synonymes et paraphrases : exposant H ; « le bruit honnête dépasse un demi » (ancienne phrase fausse).
- Source : réponse 27-luc, E4-5 (`reponse-27-luc/relecture-fable-api.md`, l. 86-88) ; `6a042a7b18124d58` ; réponse 9, phrase 5 à ne plus écrire ; `GO-2026-11-22-40` (`registres/go.md`, l. 727 : « erratum interne et version 3 du programme : « go » », commande de la pièce) ; R-4849 (`registres/decisions.md`, l. 4988 : demande 27 rendue, quatre décisions pour Lazar).
- État : proposé non tranché : le texte de l'erratum (réponse 27) attend le mot de Lazar sur ses quatre décisions (R-4849) ; le fond (« la dépendance courte change la constante ») vient de la réponse 9, accordée (`GO-2026-11-22-24`, l. 711).
- Liens : modèle nul hérité ; loi de la racine (F01-37).
- Ce qui l'attaque : —.
- Inventaire : nouveau.
- Historique : v1 et v2 disaient la correction « retenue comme correction proposée » ; corrigé en v3 parce qu'aucune ligne ne retient l'erratum et que R-4849 (l. 4988) le porte à Lazar avec quatre décisions.

#### [GO-58] La configuration du calage de G1
- Définition : configuration de génération du calage de G1 (modèle, révision, bibliothèque et version, précision, gabarit de conversation et son empreinte, température, noyau, pas, jetons par action, agents, environnement, commit du harnais, absence d'adaptateur), écrite par un Fable de la mère, contre-lue par Opus, corrigée, vérifiée, scellée. La course du banc fermé n'attend pas ce scellement : elle part avec une réserve écrite sur la comparabilité avec le calage, la configuration s'écrivant en parallèle.
- Synonymes et paraphrases : « go configuration du calage », nœud 10.
- Source : `GO-2026-11-21-77` (`registres/go.md`, l. 676) ; `GO-2026-11-21-78` (l. 677 : « la course […] n'attend pas la configuration du calage (GO-2026-11-21-77), qui s'écrit en parallèle ») ; R-4662 (`registres/decisions.md`, l. 4801) ; R-4740 (l. 4879 : relecture par Fable « à corriger »).
- État : retenu, sans dépense (`GO-2026-11-21-77`) ; texte relu par Fable, « à corriger » (R-4740) ; non scellé dans ce que j'ai lu.
- Liens : banc fermé (RD21-46) ; G1.
- Ce qui l'attaque : la comparabilité de la course du banc fermé avec le calage, couverte seulement par une réserve écrite (`GO-2026-11-21-78`).
- Inventaire : nouveau.
- Historique : v1 et v2 disaient la configuration « scellée avant la course du banc fermé » ; corrigé en v3, sur la remarque d'Argon vérifiée, parce que `GO-2026-11-21-78` (l. 677) lève l'attente : la course part avec sa réserve sans attendre ce scellement.

#### [RD21-22] Loi de la référence honnête
- Définition : candidat de tête de la note « percée » : toute accumulation de preuves déclare m, n et la source de sa validité ; l'horizon est au plus m sauf nul par acte (application du corollaire 1 de Ker 2010) ; une prévision chiffrée doit être scellée avant G1.
- Synonymes et paraphrases : « percée en contrôle et sécurité », candidat C1, R1 de la réponse 2, N-076, « assurance par audit et référence honnête ».
- Source : `registres/decisions.md` l. 4673, R-4535 ; l. 4693, R-4555 (N-076 versée) ; l. 4754, R-4615 (erratum 2) ; l. 4782, R-4643 ; l. 4879, R-4740 ; l. 4906, R-4767 ; N-076 v1, § 2 et § 14 (énoncé « m, n, horizon au plus m sauf nul par acte ») ; `GO-2026-11-21-57` (`registres/go.md`, l. 656 : « la loi de la référence honnête intégrée au programme ») ; `GO-2026-11-22-12` (l. 699, point 1 : « loi de la référence et attestation du tirage promues seulement après l'essai jumeau contre jumeau »).
- État : retenu en N-076, rien revendiqué (`GO-2026-11-21-57`) ; promotion seulement après l'essai jumeau contre jumeau (`GO-2026-11-22-12`, point 1) ; prévision chiffrée non scellée, un texte relu « à corriger » (R-4643, R-4740).
- Liens : N-076 ; G1 ; papier A ; prévision de la référence honnête (N076-05) ; modèle nul hérité (F22-01).
- Ce qui l'attaque : heurt entre la boucle audit-recapture-réapprentissage et N-060 v3 point 4 ; phrase « un théorème remarqué n'est pas réaliste » retirée ; « horizon au plus m » redit le corollaire 1 de Ker 2010 (R-4767) : « la loi de la référence, résultat mesuré du programme » est à ne plus écrire (réponse 9, phrase 6).
- Inventaire : nouveau (voisin 2.7).
- Historique : v1 et v2 sourçaient l'énoncé sur quatre lignes R- seulement et disaient la prévision « absente » ; corrigé en v3, sur la remarque d'Argon vérifiée, parce que l'énoncé vient de N-076 (§ 2, § 14), que `GO-2026-11-21-57` (l. 656) et `GO-2026-11-22-12` (l. 699) fondent l'état, et qu'un texte de la prévision existe, relu « à corriger » (R-4740, l. 4879).
