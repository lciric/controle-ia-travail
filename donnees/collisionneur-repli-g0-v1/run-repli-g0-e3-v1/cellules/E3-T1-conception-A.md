# Cellule A — Tour III.1 — règle de repli si G0 échoue

## 0. État des pièces transmises

- Pièce B est coupée en fin (« il est fini » sans suite). Pièce C commence au milieu d'une phrase et contient un fragment isolé (« d'octobre, section 8), organismes de 70 milliards… ») : son contexte est perdu, je ne le reconstruis pas.
- La date « 1er décembre » pour le début du financement externe n'apparaît dans aucune pièce servie ; elle vient de la question seule. Statut : RAPPORTÉ (par l'arbitre).

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Conséquence pour la règle |
|---|---|---|---|
| A1 | Il existe un préenregistrement de l'*évaluation* de G0 (quelle preuve scellée vaut pour chaque critère), contre lequel le sous-agent R13 prononcerait son verdict. | SUPPOSÉ — les pièces ne montrent que les huit critères (pièce A) et les règles R1–R13 (pièce D) ; aucun protocole d'évaluation de G0 n'est cité. Les critères 6 et 7 préenregistrent G1 et le papier C, pas G0. | Sans ce document, « verdict scellé contre son préenregistrement » n'est pas applicable fin novembre. C'est la première chose à écrire (point 4). |
| A2 | « Échec » et « non concluant » sont des états possibles de la porte. | HYPOTHÈSE. La pièce A ne connaît que deux états : tous les critères remplis avec preuves scellées, ou non. « Presque fini » n'y existe pas. | Toute règle qui fait d'un état intermédiaire un franchissement partiel est hors cadre. La distinction n'est licite qu'au niveau de *ce qu'on fait ensuite*, pas de la porte. |
| A3 | Le financement externe commence le 1er décembre et est conditionné (ou non) à G0. | RAPPORTÉ (question). La pièce C dit seulement « avant le début du financement », sans date, et « aucune règle de repli écrite sur le palier financé ». | Le lien G0 → tirage des fonds n'est pas écrit. La règle doit le fixer, ou dire au fonds qu'il ne l'est pas. |
| A4 | Le papier C ou « un résultat négatif publiable » ne dépendent pas des critères manquants. | SUPPOSÉ. Le critère 7 (préenregistrement du papier C) est lui-même ouvert ; rien ne dit de quoi dépendent HC1–HC3. | L'option (c) n'est utilisable que si l'on établit maintenant, par liste de dépendances, ce qui ne dépend pas des critères 2–4. |
| A5 | Un second report de l'échéance est compatible avec N-027. | VÉRIFIÉ sur la lettre de N-027 : ce qui est gelé, ce sont les critères (P-007) ; la date « au plus tard fin novembre » est une décision GO, modifiable par un nouveau nœud. Mais N-027 *est déjà* un report (du 1er novembre à fin novembre). | Un report fin novembre serait le deuxième. La borne doit donc compter N-027 comme le premier, ou dire explicitement pourquoi non. |
| A6 | Le coût pour fermer 2, 3 et 4 est atteignable. | OBSERVÉ-NON-AUDITÉ : pièce B, « banque complète de l'ordre de 300 à 1 400 USD, au-delà des 90 accordés » ; « aucun organisme saboté n'existe » au 29 octobre. | Un report sans devis est une porte de sortie déguisée : il faut un critère mécanique de faisabilité avant d'autoriser le report. |
| A7 | Le critère 2 peut échouer « négativement » (organisme sans dose-réponse). | RAPPORTÉ : pièce B, R-680, « absence de dose diffuse avec dommage = arrêt de la banque ». | Il existe déjà une conséquence écrite pour un négatif sur le critère 2. La règle de repli doit s'y raccorder, non la doubler. |

## 1. Ce qui déclenche le repli

**Options.**

- O1.1 *Tout ou rien* : la porte est « non franchie » dès qu'un critère manque, sans état intermédiaire. Avantage : c'est la lettre de la pièce A ; aucune réinterprétation. Inconvénient : ne dit rien sur la suite ; le repli devient une décision après lecture.
- O1.2 *Trois états par critère, deux états pour la porte* : la porte reste binaire, mais le verdict R13 classe chaque critère dans un des trois états suivants, définis mécaniquement : **E1 — rempli** (preuve scellée, empreinte au registre, critère satisfait) ; **E2 — négatif constaté** (preuve scellée, critère non satisfait : par exemple sondes v0 au plancher aléatoire, ou organisme sans dose-réponse) ; **E3 — non atteint** (aucune preuve scellée). Avantage : la porte ne bouge pas ; la différence E2/E3 est la seule information que le repli a besoin de lire, et elle est constatable sans jugement. Inconvénient : exige que le protocole d'évaluation (A1) définisse d'avance la preuve attendue pour chaque critère.
- O1.3 *État « presque fini »* : un quatrième état sur le degré d'avancement. Inconvénient : non mécanique, laisse une décision au lecteur ; c'est exactement l'option (c) de N-027 (« critère 3 réécrit ») sous un autre nom. Hors cadre.

**Recommandation : O1.2**, confiance ≈ 0,7. La seule notion d'« en cours » admise est documentaire et antérieure à la lecture : un critère E3 est dit **engagé** si et seulement si son préenregistrement (R1) est scellé et contre-lu (R2) avant la date du verdict et qu'aucun résultat n'a été lu. Ce n'est pas un état de la porte, c'est un fait de registre.

**Qui prononce.** Le sous-agent neuf de R13, contre le protocole d'évaluation de G0 (à écrire, point 4), produit un verdict en deux parties : (i) porte franchie / non franchie ; (ii) le vecteur d'états E1/E2/E3 et le drapeau « engagé » pour chaque critère. Il ne choisit pas le repli : la règle le déduit du vecteur. Lazar donne le GO (R13) ; s'il s'écarte de la règle, c'est un nœud consigné comme dérogation, pas une lecture de la règle.

## 2. Les options de repli

**(a) Report unique et borné, critères inchangés.**
Autorise : poursuivre le travail sur les critères E3, sans entrer en phase 1 ; aucune lecture de G1 (P-9, pièce B). Interdit : tout nouveau report, tout changement de critère, tout engagement de calcul de phase 1. Coût : le calcul nécessaire aux critères 2–4 (non chiffré pour G0 dans les pièces ; voir (d)). Risque de dérive : élevé si la condition d'accès au report est molle ; faible si elle est mécanique (tous les critères manquants sont E3 *et* engagés, aucun E2). Compatibilité : R1 oui (les préenregistrements sont la condition d'entrée) ; R4 oui si le second verdict est aussi R13 ; R13 oui ; N-027 : la date est modifiée par nœud, les critères non (P-007). Au fonds : « G0 not passed on 30 November; one bounded extension to [date], criteria unchanged; phase 1 not started; phase-1 budget not drawn. »

**(b) Franchissement partiel interdit, travail continu, sans phase 1, sans date.**
Autorise la même chose que (a) sans borne. Inconvénient décisif : sans borne, la porte cesse d'être une porte ; c'est « on verra ». Risque de dérive maximal. Non scellable au sens des critères de lecture, sauf si une borne est ajoutée — auquel cas c'est (a).

**(c) Bascule vers ce qui ne dépend pas des critères manquants.**
Deux sous-cas à séparer. (c1) Un critère est **E2** (négatif constaté) : le résultat négatif est lui-même un livrable préenregistré (critère 2 : la conséquence R-680 est déjà écrite). (c2) Papier C : dépend de A4 (SUPPOSÉ). Autorise : rédaction et soumission des parties dont les dépendances listées sont toutes E1. Interdit : présenter la bascule comme un franchissement ; démarrer G1. Coût : faible en calcul, élevé en rédaction. Risque de dérive : moyen — « publier le négatif » peut devenir un prétexte pour ne pas fermer un critère atteignable ; d'où la condition : (c) n'est accessible qu'en présence d'un E2, jamais depuis un E3 seul. Compatibilité : R1, R4 (un négatif trop propre subit le même audit), R13, N-027 : oui. Au fonds : « a prerequisite failed on sealed evidence; the pre-registered negative is reported; phase 1 not started. »

**(d) Arrêt et rapport.**
Autorise : clôture de la phase 0 avec un rapport scellé ; réouverture seulement par un nouveau programme, nouvelle porte, nouveau préenregistrement — jamais par « G0 franchie plus tard ». Interdit : tout tirage de fonds de phase 1. Coût : perte du travail non encore converti en livrable. Risque de dérive : nul sur la porte ; risque inverse d'arrêt prématuré si (d) est atteint depuis un simple retard. Compatibilité : toutes. Au fonds : « phase 0 closed; report available; no phase-1 funds drawn. »

## 3. La règle recommandée (clause scellable)

**Clause principale.** « Si, à la date du verdict de G0 (au plus tard le 30 novembre 2026), le sous-agent R13 prononce "G0 non franchie", le repli est déterminé par le seul vecteur d'états (E1/E2/E3, drapeau "engagé") de son verdict scellé, selon l'ordre ci-dessous, sans décision après lecture ; les huit critères restent ceux de la pièce A ; la phase 1 ne commence pas et aucun fonds affecté à la phase 1 n'est tiré tant que G0 n'est pas franchie. »

**Ordre de préférence (évalué dans cet ordre, le premier cas vrai s'applique).**

1. **Un critère au moins est E2** → option (c1) : le négatif préenregistré est rapporté ; pour le critère 2, la conséquence R-680 s'applique (arrêt de la banque). Aucun report de G0. Si un critère E2 est 2, 3 ou 4, la porte G0 est close par rapport (d), parce que ces critères conditionnent l'existence même de l'objet de G1 ; la réouverture passe par un nouveau programme. Si le critère E2 est 6, 7 ou 8 (document contre-lu rejeté), il est traité comme E3 engagé.
2. **Tous les critères manquants sont E3 et tous sont "engagés"** (préenregistrement scellé et contre-lu avant le 30 novembre, aucun résultat lu) **et** le devis de calcul nécessaire pour les fermer est consigné au registre avant le verdict, avec une source de financement identifiée hors phase 1 → option (a) : **un seul report**, jusqu'au **31 décembre 2026** (date illustrative, à fixer maintenant), second verdict R13 par un sous-agent distinct du premier.
3. **Sinon** (un critère manquant n'est pas engagé, ou le devis n'est pas consigné) → option (d) : rapport d'arrêt de la phase 0, scellé, soumis à Lazar.

**Borne.** Au plus un report après le 30 novembre. Au second verdict : franchie, ou (d) ; aucune troisième lecture ; aucun nœud « nouvelle prolongation » recevable sur G0. N-027 est compté comme le premier report ; celui-ci serait le dernier.

**Confiance** ≈ 0,6 sur la structure ; ≈ 0,45 sur la date du 31 décembre (dépend de A6, non audité).

**Pourquoi cet ordre.** Un négatif constaté est une information et doit être lu avant tout report (sinon le report sert à le cacher). Le report n'est accordé que sur des faits de registre existant *avant* la lecture (préenregistrements scellés, devis consigné) : c'est ce qui le rend scellable. L'arrêt est le défaut, pas l'exception : c'est la seule façon que la porte garde un sens sans que personne ait à la « faire échouer » activement.

## 4. Ce qui doit être décidé maintenant

| Décision | Options | Recommandation | Confiance |
|---|---|---|---|
| D1 Écrire et sceller le **protocole d'évaluation de G0** : pour chaque critère, le chemin et l'empreinte de la preuve attendue (R6), et le test mécanique E1/E2/E3. | Document unique ; ou par critère. | Document unique, contre-lu (R2), avant le 15 novembre (date illustrative). Sans lui, R13 n'est pas applicable et la règle non plus. | 0,8 |
| D2 Fixer la **date du report** et la **source de fonds hors phase 1** qui le couvre. | 31 décembre ; 15 janvier ; aucune. | 31 décembre (illustratif) ; la source est à nommer par Lazar — SUPPOSÉ qu'elle existe ; sinon la branche 2 est morte et la règle se réduit à (c)/(d), ce qu'il faut dire au fonds. | 0,5 |
| D3 Définir **« engagé »** par critère : préenregistrement scellé + contre-lu + manifeste de run (R9) pour 2, 3, 4 ; brouillon versionné (R12) avec empreinte pour 6, 7, 8. | Idem ou plus strict (run lancé). | « Scellé et contre-lu » suffit ; exiger « run lancé » ajoute un état lisible après coup. | 0,65 |
| D4 Lister les **dépendances du papier C** (HC1–HC3) et de tout « résultat négatif publiable » sur les critères 1–8. | Liste maintenant ; ou laisser à (c). | Maintenant ; sinon (c2) est non scellable. | 0,7 |
| D5 Raccorder la règle à **R-680** : le pilote d'organismes est-il le test du critère 2 ? Si oui, son arrêt vaut E2 sur le critère 2. | Oui / non. | Oui, écrit dans D1. | 0,6 |
| D6 Décider ce que dit le programme d'entretien au fonds : **la règle une fois scellée**, ou « no fallback rule is written yet ». | L'un ou l'autre ; jamais une règle non scellée présentée comme règle. | Tant que D1 et D2 ne sont pas scellés, dire la phrase de la pièce C telle quelle. | 0,85 |
| D7 Confirmer que le second verdict est prononcé par un **sous-agent distinct** du premier (R13 + R4). | Même agent / distinct. | Distinct. | 0,8 |

## (b) Expériences décisives (inférence forte)

**X1 — La règle est-elle mécanique ?**
H_A : donné le protocole D1 et un dossier de preuves, N instances neuves du sous-agent R13 produisent le même vecteur E1/E2/E3 et le même repli. H_B : les vecteurs divergent sur au moins un critère sans que le dossier soit ambigu. Métrique : accord inter-instances sur le vecteur (8 critères × 3 états) et sur la branche de repli ; seuil : accord parfait sur la branche de repli pour 100 % des dossiers d'épreuve, accord ≥ 0,95 par critère (seuils illustratifs, à sceller). Contrôle négatif (R5) : un dossier où une preuve est volontairement absente ou dont l'empreinte ne correspond pas doit être classé E3 par toutes les instances ; un dossier où tout est propre doit être E1. Issue : H_A faux → la règle n'est pas scellable en l'état, D1 est à réécrire ; H_B faux → l'agent n'apporte rien au script (voir (c)), et le verdict peut être un script contre-lu, ce qui est une économie, pas une perte.

**X2 — La distinction E2/E3 change-t-elle quelque chose ?**
H_A : sur l'espace des états possibles au 30 novembre (6 critères ouverts × 3 états × drapeau engagé, énumérable), la règle à trois états choisit une branche différente de la règle à deux états (franchie / non franchie → report) dans une fraction non nulle de configurations *plausibles*, « plausible » étant défini par une liste scellée (par exemple : critère 2 E2 et autres E3). H_B : jamais, ou seulement dans des configurations exclues d'avance. Métrique : nombre de configurations plausibles où les branches diffèrent ; seuil : ≥ 1. Contrôle négatif : configuration « tous E1 » → les deux règles donnent « franchie ». Issue : H_A faux → supprimer la distinction, règle plus simple ; H_B faux → la distinction est nécessaire et doit rester dans D1. Coût : un script, aucune mesure sur modèle.

**X3 — Le report est-il faisable, ou est-ce une porte de sortie ?**
H_A : le devis de calcul et de temps pour amener 2, 3 et 4 de E3 à E1 tient dans la source de fonds nommée en D2 et dans l'intervalle 30 novembre–31 décembre. H_B : il ne tient pas. Métrique : devis consigné au registre (unités d'épreuve, exécutions, prix unitaire, empreinte), comparé à la somme disponible ; seuil : devis ≤ fonds disponibles et durée estimée ≤ intervalle, avec marge écrite d'avance (illustratif : facteur 1,5). Contrôle négatif : le même devis calculé pour G1 (288 unités par mode, K_h = 10, pièce B) doit sortir au-dessus de 90 USD, sinon la méthode de devis est fausse. Issue : H_A faux → la branche 2 de la règle est inopérante, la règle devient (c)/(d) et le fonds doit l'entendre ; H_B faux → le report est un report, pas un alibi.

**X4 — Le verdict R13 résiste-t-il au « trop beau » (R4) ?**
H_A : un dossier synthétique où les huit critères passent avec des preuves anormalement propres (même graine partout, dose-réponse parfaitement linéaire, zéro variance) déclenche la réserve d'audit chez l'agent neuf. H_B : il est classé E1 sans réserve. Métrique : présence de la réserve ; seuil : réserve sur 100 % des dossiers « trop propres » et sur 0 % des dossiers sains appariés (illustratif). Contrôle négatif : dossier sain. Issue : H_A faux → R4 n'est pas opérant au niveau de la porte ; ajouter un test de propreté mécanique à D1 ; H_B faux → le protocole est symétrique.

## (c) Instruments nommés et mesure minimale

Les instruments de la question sont de gouvernance ; je transpose « détection / fausse alerte » au sens propre : l'événement à détecter est « critère non rempli ».

| Instrument | Détection | Fausse alerte | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| **Verdict R13 sur G0** (sous-agent neuf + protocole D1) | Taux de critères réellement non remplis classés E2/E3 ; cible 100 % sur dossiers synthétiques | Taux de critères remplis classés E2/E3 ; cible 0 % (illustratif) | Paires de dossiers identiques à une preuve près (présente et valide / absente ou empreinte fausse) | Script : pour chaque critère, existence du fichier, correspondance `.sha256` (R6, R11), ligne de registre. Si l'agent ne fait pas mieux que le script sur les paires, l'agent est remplacé par le script contre-lu. |
| **Règle de repli** (fonction vecteur → branche) | Branches 1 et 3 choisies dans 100 % des configurations qui les exigent | Branche 2 (report) choisie alors qu'un E2 existe ou qu'un critère n'est pas engagé : cible 0 | Énumération complète des configurations (X2) | Table de vérité calculée par script ; l'agent doit la reproduire. |
| **Drapeau « engagé »** | Critère sans préenregistrement scellé classé « non engagé » : 100 % | Critère avec préenregistrement scellé et contre-lu classé « non engagé » : 0 | Paires scellé / non scellé avec même contenu de brouillon | Script sur le registre des scellements (empreinte + date + mention de contre-lecture R2). |
| **Détecteur « trop beau »** (R4 au niveau porte) | X4 | X4 | Dossiers sains appariés | Tests mécaniques de variance nulle, graines répétées (R9), empreintes dupliquées. |

Mesure minimale avant scellement : au moins une paire par critère (16 dossiers) pour le verdict, la table complète pour la règle, une paire par critère ouvert pour « engagé ». Chiffres illustratifs.

## (d) Ancrage matériel

- **Pour la règle elle-même (X1–X4)** : aucun modèle de recherche, aucun GPU. Des exécutions d'agents neufs sur des dossiers synthétiques et des scripts de registre. Coût : de l'ordre de quelques dizaines d'USD d'appels d'agents (illustratif) ; quelques jours de travail de session.
- **Pour que la branche 2 (report) ait un sens** : il faut fermer les critères 2, 3, 4 sur le modèle réel. Les pièces donnent : harnais validé « sur le modèle réel » (pièce B, OBSERVÉ-NON-AUDITÉ) ; un fragment coupé mentionnant « organismes de 70 milliards » (pièce C, contexte perdu — je ne l'interprète pas au-delà de : un modèle ouvert de cet ordre de taille est envisagé, SUPPOSÉ) ; « banque complète de l'ordre de 300 à 1 400 USD, au-delà des 90 accordés » (pièce B, OBSERVÉ-NON-AUDITÉ) ; « aucun organisme saboté n'existe » (pièce B). Les tailles d'échantillon citées (288 unités par mode, K_h = 10, n_h ≥ max(288 ; n80)) sont des dimensionnements de **G1**, pas de G0 ; rien dans les pièces ne dimensionne la dose-réponse du critère 2 ni le plancher aléatoire apparié du critère 3. Le devis de X3 est donc à produire ; tout chiffre que je donnerais ici serait inventé. Je n'en donne pas.
- **Ce qui est vérifiable sans fonds** : critères 6, 7, 8 (documents, contre-lecture, état de l'art sur PDF empreinté, R7). Ils devraient être E1 ou E3-engagé au 30 novembre quoi qu'il arrive ; s'ils ne le sont pas, la branche 3 (arrêt) est atteinte sur des critères qui ne coûtaient rien, ce qui est un signal sur le programme, pas sur le calcul.

## Ce que cette proposition ne fait pas

Elle ne touche aucun des huit critères. Elle ne crée pas d'état intermédiaire de la porte. Elle laisse à Lazar le GO et une seule décision de contenu (D2 : date et source du report) à prendre *avant* la lecture. Elle est réfutable par X1 (si deux instances neuves lisent le même dossier différemment, la règle n'est pas scellable) et par X3 (si le report ne peut pas être financé, la branche 2 doit être retirée et le fonds doit l'entendre tel quel).

FIN-DE-CELLULE