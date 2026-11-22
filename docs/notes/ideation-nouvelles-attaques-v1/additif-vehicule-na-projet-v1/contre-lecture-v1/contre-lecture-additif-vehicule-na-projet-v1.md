# Contre-lecture du projet d'additif du véhicule NA-1 — v1

Contre-lecteur Opus neuf (aucune pièce écrite), 2026-11-22. Processeur seul : aucun appel de modèle, aucun réseau, aucune dépense, aucune écriture dans un dépôt. Aucun refus d'outil ni de classifieur. Aucun fichier interdit lu (ni réponse 24, ni son renvoi de séquestre, ni matière première, ni quarantaine).

Pièce : `B/additif-vehicule-na-projet-v1/additif-vehicule-na-projet-v1.md`, `sha256` vérifiée contre son compagnon (OK).
Sources relues et empreintes recalculées, toutes égales à celles de la pièce : V9 `864f39a7…`, A1 `9f731795…`, CV `b4ef87dc…`, AC `ce76e0d6…`, DV `205e08f2…`, PS `4cd360ba…`, QN `02ad3d76…`, QA `8c54752f…`, go.md `459ce98e…`, GG `923679b5…`, CO `1b7f6822…`, NO `79b9d423…`, PL `f71451b9…`, VE `e7eb1682…` ; compagnons OK ; six pièces scellées présentes à `registres/scellements-v1.md`.
Copie de `main` relue : HEAD **`78955b61`** (« additif du véhicule, décisions Q3 à Q7 (R-4815) »), et non `da565ec1` cité par la pièce. `git diff da565ec1 HEAD` est vide pour P, QN, QA, go.md, GG et CLAUDE.md ; seul `registres/decisions.md` a changé (R-4812 à R-4815 ajoutées, l. 4951 à 4954 ; les lignes 4943 et 4946 citées sont inchangées).

## Verdict

**À corriger.** Six points bloquants pour Fable et le scellement (B1 à B6), dont deux qui fausseraient une décision de Lazar (B1 sur la définition du mode, B2 sur la dépense de la passe X). Les citations sont exactes ; les numéros d'arrêts neufs n'entrent en collision avec aucun numéro pris.

## 1. Citations (point 1 du mandat)

Trente-quatre citations vérifiées, exactes à la lettre : V9 l. 62, 65, 69, 73, 77 (deux), 82, 90, 92, 98, 99, 101, 156, 160, 235, 254, 325, 372, 373, 374, 376, 383 (deux), 384, 385, 386, 387, 392, 419 ; CV l. 116, 166 ; AC l. 72, 143 ; A1 l. 118 ; DV l. 380, 386 ; CO l. 225 ; go.md l. 722 (règle de repli, « arrêts n° 11, 12 et 27 inchangés », « écart déclaré … accordé par Lazar ») et l. 724 ; `CLAUDE.md` l. 60. Les renvois sans guillemets (V9 l. 63, 71, 107, 148, 177, 180, 360, 396, 402, 410 ; A1 l. 94, l. 161 ; CO l. 87, 227, 228, 230, 232, 419, 463, 536, 603 ; GG l. 80, l. 107 ; decisions.md l. 4943, 4946) visent le bon passage. Le décompte de 53 lieux est juste (6 + 4 + 5 + 20 + 2 + 11 + 2 + 3).

Inexactitudes mineures (à noter) :
- X-7 cite V9 l. 315 sans le gras de « **Les mesures** ».
- L-1 coupe AC l. 57 après « inchangée | » sans « […] » (la cellule « inchangé (complément v3, § 3) | » manque) ; R2 coupe V9 l. 98 avant « , qui vaut pour le refus d'un classifieur de sûreté » sans « […] ».
- R11 renvoie à « DV l. 382 » pour 5 et 1 dollars : 5 est à DV l. 381, 1 à l. 382.
- En-tête : HEAD à mettre à jour (`78955b61`) ; l. 55, réserve 1 et § 13, point 1 sont dépassés (voir § 5).

## 2. Bloquant pour Fable et le scellement

**B1 — § 8, D-2 et rubrique 3 : l'épreuve 4 est déjà fixée par une pièce scellée, que le projet ne cite pas.** CV l. 39, l. 94 (ligne 15) et § 8 (l. 187-189), scellé, sur GO-2026-11-20-57 (mot de Lazar) : « branche « avec », les quatre épreuves » ; « la branche « sans » ne vaut pas » ; « La liste de référence est écrite par la session à part et scellée avant toute lecture ». Le projet traite la branche et la liste comme ouvertes (D-2 ne cite que V9 l. 325 ; rubrique 3 : « la branche de la V9 l. 325-330 retenue ») et met la liste dans la pièce du § 8, écrite par un auteur qui ne doit avoir lu aucun candidat (rubrique 7), alors que la lettre scellée la donne à la session à part, qui lit les fiches. Effets : écart non déclaré à CV § 8 et à GO-57 ; contradiction interne avec K-1 et la rubrique 7. À écrire : D-2 cite CV § 8 ; la rubrique 3 devient « branche « avec », fixée (CV § 8) » ; la liste reste à la session à part, ou l'écart est porté à Lazar avec Q8. Si la pièce du § 8 change ou remplace les quatre épreuves, il faut déclarer aussi l'écart à V9 l. 257, l. 328, l. 358 et à CV § 8.

**B2 — X-10 et Q2 : la passe X n'est pas « hors des parts » sur les clés réelles.** Deux de ses cinq requêtes partent sur Minuit (espèce 3) et sur Luc (espèce 4) (X-1). Or :
- la part de Minuit, 156,56, est scellée comme « reste moins les 6 dollars des lignes à part » (AC § 2 ; CV l. 132). Une chaîne de passe X de 18,15 dollars au pire sur Minuit fait passer le reste sous la part : l'arrêt n° 11 refuse alors le départ, et il faut une version neuve ;
- sur Luc, à 136,04, la tolérance n'est que de 16,96 (PL l. 76), sous les 18,15 d'une chaîne.

Q2 doit donc dire sur quelle clé tombe le coût, dans quel ordre il passe par rapport à la pièce de relevés (avant ou après la passe X), et ce que devient l'arrêt n° 11. Il faut aussi corriger :
- l'option (b) de Q2 : elle est impossible quelle que soit la part de Luc, car il ne reste que 10,41 sous 450 à 125,63 (PL l. 76) ;
- l'écart, qui doit être écrit en toutes lettres : « écart déclaré » à V9 l. 172-173 (liste fermée des lignes à part), à DV l. 381-386 (plafond total de 456) et au montant de GO-30 (X-10 ne dit que « nœud ») ;
- le repère de 6,05 pour les trois espèces non Claude : il n'est pas un pire sous la garde Google (G-3). Il faut prendre le plus grand de 6,05 et de [PIRE-G-PROPOSEUR].

**B3 — R10, R8, R9 : la lecture marquée « lecture de la V9 » est la mauvaise.** Une fiche servie par repli est une fiche rendue (V9 l. 148, R8 le dit). La lettre scellée de M3, de M1 et de l'arrêt n° 5 (« parmi les fiches rendues ») est donc la lecture (b). La lecture (a), « espèces seules », est neuve. R10 inverse les deux lectures, donc le chiffre gelé. R9 retire de M4 de l'espèce le coût des tentatives servies par repli : c'est un changement de la lettre de V9 l. 156, non marqué « écart déclaré ». La phrase de R10 « aucune autre lecture gelée ne change » est fausse. Il faut dire aussi où va le coût de la première tentative refusée.

**B4 — R7-quater : la lettre neuve reste ambiguë.** Le « […] » laisse en place « donc hors du dénominateur de M3 et de la garde du coffre », alors que R8 (D-22.3) y fait entrer les fiches de repli de cet appel. Il faut écrire la phrase entière. V9 l. 101 (« Aucune de ces trois réponses n'est une fiche rendue ») doit aussi passer à « quatre » : c'est un écart à déclarer, oublié.

**B5 — K-2 et arrêt n° 36 : la règle, telle qu'écrite, arrêterait la course.** « Chaque requête assemblée », contrôlée « par empreinte, contre une liste fermée » de quatre pièces, refuserait toutes les requêtes de l'aiguilleur, des juges et de l'épreuve des témoins, qui portent les consignes D3 et des fiches. Une empreinte fixe ne peut pas non plus reconnaître des pièces variables : la partie servie remplie change par case, le registre servi par génération. Correction : borner K-2 aux requêtes de proposeur et de passe X, et contrôler par type de pièce, avec l'empreinte des seules pièces fixes (gabarit, synthèse, question fusionnée) et le contrôle de programme pour le registre (n° 19).

**B6 — Qui accorde les écarts qui ne viennent pas du repli.** Pour un préenregistrement scellé, un écart est un nœud de Lazar (hiérarchie de décision). GO-2026-11-22-29 n'ouvre que la routine. GO-35 couvre les écarts qui découlent du repli (D-i à D-iii, D-22.1 à D-22.3). Il ne couvre pas L-1 (part de Luc relevée, écart à V9 l. 235 et à CV l. 35, l. 106), accordée par la seule mère (R-4804, R-4807). D-K (règle neuve, arrêt n° 36) est dans le même cas. Il faut soit une ligne de GO, soit l'ajouter aux questions pour Lazar.

## 3. Cohérence interne (point 3) — à noter

1. **Numéros d'arrêts.** 31 à 38 n'entrent en collision avec rien : n° 1 à 23 (V9), 24 à 27 (A1 l. 64, l. 118), 28 à 30 (R-4603, decisions.md l. 4742), 31 et suivants réservés à l'additif (R-4603, R-4479). Les « n° 30 » et « n° 40 » de A1 l. 79, CV l. 185 et CO § 2.1 sont des **clés de tirage**, d'un autre espace de noms : écrire « clé de tirage n° 30 » au § 13, point 9. Restent à numéroter à l'assemblage : les onze refus écrits (CO l. 419) et A17 (CO l. 699, l. 812).
2. **Arrêt n° 31.** « Arrêt nommé de la course pour ce rôle » s'écarte de la lettre du mot 6 de la mère (CO l. 433, l. 700 : « arrêt nommé de la course, qui dit le rôle et la cause ; aucune suite avec un rôle arrêté ») ; le cas « modèle servi absent » manque. L'artefact de CO l. 700, « version servie d'un juge qui change entre deux fiches », lèverait le n° 31 sur tout verdict rendu par repli (R17, Q6) : c'est un écart à CO à déclarer. Il faut aussi dire si le portier rendu par repli émet son passeport (A17).
3. **Arrêt n° 35.** Avec « la course continue », il contredit V9 l. 368 (« une garde qui se déclenche arrête »). Mieux vaut une garde sans numéro, en refus écrit (CO l. 812, règle 4). La classe M6 d'un appel refusé avant l'envoi n'est pas dite (G-2 ne couvre que le retour).
4. **Double compte.** En M6, lecture (b), l'appel compte à l'espèce (classe neuve) et à la rubrique « servies par repli » (classe de la dernière tentative, R12). Il faut écrire que la rubrique est un détail et que le total par génération compte chaque appel une fois.
5. **R1 contre A7.** « Seul le champ du modèle du corps change » se heurte à A7 (réglages par modèle) : il faut écrire « le modèle et ses réglages non textuels A7 ».
6. **R12 et R7-bis.** « Servie » n'est pas défini, par exemple pour un repli qui rend une erreur de crédit ou une réponse coupée.
7. **R11.** « La course ne part pas, pour cette espèce » est ambigu : la course part-elle sans l'espèce ? Il faut dire comme au n° 27 : « la course ne part pas sans le mot de la mère sur une ligne neuve ».
8. **X-8.** Qui rend les classes de la passe X, sans portier (X-6) ? « Réponse rendue » est une classe neuve. La classe de requêtes (i) du périmètre d'antériorité (V9 l. 336-337) part de la case ; la passe X n'en a pas, et la règle est à adapter.
9. **X-7.** Il étend l'arrêt n° 15 à une autre question : c'est un écart à déclarer.
10. **Noms des lignes.** Les lignes « R1 à R17 » portent les noms des règles gelées R1 à R14 (« règle R5 » voisine de la ligne R5) : les renommer, par exemple P1 à P17.
11. **Nombre des classes.** R-4812 dit « quatrième classe d'issue », R7-bis dit « cinquième » : écrire « quatrième classe sans fiche, cinquième classe d'issue ». La mère n'a nommé d'écart qu'à V9 l. 160 et à R12. Les écarts à l. 92 et l. 101 qu'ajoute le projet sont à lui faire confirmer.
12. **A2.** Rejouer côté client « le repli que prévoit le fournisseur » (GO-35, colonne de note) est une lecture de GO-35 : la dire comme telle, accordée par D-N1.
13. **K-1.** Dire que la carte que A1 donne à l'instance du mode tenu à l'écart (A1 § 2, conditions a et d) n'est pas touchée, et qu'une proposition de la passe X n'est jamais une carte (elle n'a pas de case).
14. **Neon.** GO-2026-11-22-33, point 3 (Neon proposeur de l'organisme, sur devis à part) n'est pas cité. Écrire que Neon n'est pas dans cette course, qui garde ses cinq espèces (cohérent avec Q7).
15. **Limite de mots.** QN et QA n'ont pas de limite de mots, que vérifie la garde Google (contrôle 3, `CLAUDE.md` l. 66-67). Risque de fin en plafond de jetons sur les espèces 1 et 5.

## 4. Passe X, option (c), 54,45 dollars (point 4)

Le calcul est juste : 2 × (3 × 6,05) + 3 × 6,05 = 36,30 + 18,15 = 54,45. La forme (c) est bien posée pour la course scellée, qui ne change pas, et la question part mot pour mot. L'écart au plafond de 456 n'est **pas** écrit comme « écart déclaré » ; il ne l'est que comme nœud de dépense (B2). La pose financière est fausse sur les clés Minuit et Luc (B2). À ajouter à Q1 : `CLAUDE.md` l. 60 dit « fusionnée avec les autres questions ouvertes ». Sous (c), seule la fusion de QN et QA est faite, pas une fusion avec la question de la course. Lazar doit le savoir en choisissant. Réserve 3 : le pire réel de la passe X tient surtout à la sortie maximale, non à la taille de la requête. Il ne sera donc guère plus bas que 6,05.

## 5. Décisions neuves de la mère (R-4812, R-4815) : compatibilité et ce qu'il faut écrire

- D-22.1 à D-22.3 sont inscrites (R-4812, l. 4951). La l. 55, la réserve 1 et le § 13, point 1 sont à récrire. **Encore à inscrire** : D-K (règle d'ancrage), D-X (forme « mot pour mot, fusionnée »), la provenance de `garde_google_v3` (G-5), et D-L si B6 est tranché par une ligne.
- **Q3**, exception pour le registre servi : compatible. K-1 : « exception déclarée, accordée (R-4815) ».
- **Q4**, fusion sans les titres qui nomment un modèle : compatible avec X-3 (les deux titres nomment Fable). Écrire « R-4815 » à la place de « forme recommandée à Q4 ».
- **Q5**, hors de la borne de 60, comptée et rapportée à part : compatible avec X-8 et la rubrique 5. « Toutes lues » est l'ajout de l'auteur, à marquer comme tel.
- **Q6**, verdict du rôle, modèle servi consigné : compatible avec R17. « Audit de symétrie rendu deux fois » est l'ajout de l'auteur, à marquer. Voir aussi 3.2 (CO l. 700, A17).
- **Q7**, garde v3 telle quelle tant que Neon est en pause ; une espèce neuve exige sa ligne et une version neuve de la garde : à écrire à G-1 et G-5. C'est une précision de N4 (« jamais une copie ») pour ce seul cas.
- Q1, Q2, Q8 vont à Lazar : compatible.

## 6. Questions (point 5) : Q1 à Q8 sont justes ; il en manque

- **Q9 (Lazar, avec Q2)** : la clé qui paie la passe X, et l'ordre de la passe X, de la pièce de relevés et de l'arrêt n° 11 (B2).
- **Q10 (mère, puis Lazar)** : qui écrit la pièce du § 8. R-4815 nomme Q8 « décision 1 de la réponse 24 ». Or la réponse 24 est sous séquestre avec des candidats (R-4811) et la mère s'est déclarée exposée (titre de K1). La rubrique 7 et K-1 interdisent un auteur qui a lu un candidat. La décision 1 doit donc lui parvenir par un extrait sans candidat, vérifié, ou par un auteur autre que la mère.
- **Q11 (mère)** : les réponses de la passe X, qui répondent à la question même de la réponse 24, vont-elles en quarantaine de course (X-5) ou au séquestre de N-054, comme la réponse 24 ?
- **Q12 (Lazar)** : l'accord des écarts L-1 et D-K (B6).
- À ajouter à Q1 : le point « fusionnée avec les autres questions ouvertes » (§ 4).

## 7. Erreurs qui fausseraient une décision (point 6)

B1 : Lazar trancherait Q8 sans savoir que la branche et l'auteur de la liste sont déjà scellés par son propre mot (GO-57). B2 : Lazar accorderait Q2 comme « hors des parts » alors que la passe X peut empêcher le départ par l'arrêt n° 11 sur Minuit. B3 : la mauvaise lecture serait gelée comme lecture scellée.

— contre-lecteur Opus, 2026-11-22
