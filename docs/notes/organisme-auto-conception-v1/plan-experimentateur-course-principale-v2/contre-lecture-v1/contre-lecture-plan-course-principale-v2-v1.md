# Contre-lecture du plan v2 — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v1

- Contre-lecteur neuf (règle R2), modèle O. Je n'ai écrit ni le plan, ni la note de conception générale, ni le véhicule NA-1, ni aucune pièce du palier 1.
- Date (UTC) : 2026-11-21 ; `date -u` : 07:55:55Z, après les lectures, avant l'écriture.
- Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucune branche de quarantaine ni de matière première.
- **Incident, sans effet** : trois sorties de commande trop longues ont été rangées d'office par l'outil sous `/root/.claude/` ; je ne les ai pas ouvertes. Aucun refus de permission, de classifieur ni de garde.

## Pièces contrôlées

Toutes à l'empreinte annoncée et égales à leur compagnon quand il existe.

| pièce | empreinte recalculée | compagnon |
|---|---|---|
| mandat du planificateur | `e4ca4586cd603fbf79486752604158fca8c5595d51e6af26e0309ce0f35d80d0` | égal |
| plan v2 | `7cf3c78d3ebbacec42b86dfb506642e2c0af5f2af71ead0c8654e0e6891bbfb4` | égal |
| différentiel v1 → v2 | `e16df4dde1c97697b464cec951d7a3bf60c7d6ecd03b91db9b60f07bac156922` | égal |
| rapport v2 | `3b542fec6690cefe665057476f39b842fb79bab4d6a1cf4c73e257f3cc6ad7a8` | égal |
| table v2 | `ed7a76f65299444006a464aa51c73bdba8579de3af97f51ecd849ca378b94fd9` | égal |
| plan v1 | `0bb27bc0a1f262daa41ad1f7746c34a2d423a90354e834d6f6874eee1f80d8e7` | — |

Sur `origin/main` (après `git fetch origin main`, tête `9d07c9f93` au fetch, `e04285cc` à la relecture ; le contenu se tient par les empreintes) :

| pièce | empreinte | compagnon |
|---|---|---|
| note de conception générale | `4f3ae86f…` | égal |
| calculs de la note, script et sortie | `301c0f52…`, `9b66cc78…` | égaux |
| plan du pilier mathématique | `1616e709…` | égal |
| devis du pilote du pilier | `6f485216…` | — |
| manifeste du paquet v68 | `4ed9fd8e…` (aussi sur le disque) | — |
| lanceurs v9 et v10 | `1b47c1cf…`, `f4196ec5…` | — |
| additif v69 v4 | `cb352811…` (sur `main` sous `prereg/…/orchestrateur-v69/`, et sur le disque sous `docs/notes/…/epreuves-v9/orchestrateur-v69/`) | — |
| verdict de la course v67 | `d7902432…` | — |
| définition scellée de « mieux » | `4eae96bc…` | — |
| `registres/go.md`, `registres/decisions.md` | copies `lecture-go-origin-main.md`, `lecture-registre-origin-main.md` | — |

Dépôt de l'orchestrateur, lecture seule : tête `a41b7b50…` ; `tour_ferme_v64.py` `35a8294e…`, `etage_entre_generations_v57.py` `e4bf3681…`.

## Verdict : **À corriger**

Le plan est fidèle à la note sur le fond : N1 à N7 recopiés juste (options, recommandations, confiances, défauts), D2 retirée proprement, E2 et E3 récrits sur la note, C1 à C3 aux heures de la note. Tous les chiffres recalculés sont justes. Les quatre faits demandés tiennent à leur source. Mais six points demandent une correction avant que le plan serve de base : D5 et D6 se contredisent et D6 n'est plus au format ; D8 n'est pas posée sur le modèle des exceptions accordées ; le coût en appels oublie le lecteur témoin, et celui du barreau 2 n'est pas dit « propositions seules, sous hypothèse » ; le lieu du rejeu du barreau 1 n'est pas dit ; le lanceur « 11 » heurte l'additif scellé et le nom AC-1 ; une règle neuve (§ 8) n'est pas posée comme proposition.

## 1. Fidélité à la note

1. **D2 retirée au profit de N1** : juste. N1 (a), (b), (c) et la recommandation (a) à 0,7 sans défaut sont ceux de la note (§ 6). L'appui à 0,65 est dit comme écart du planificateur.
2. **N2 à N7** : options, recommandations, confiances et défauts égaux à la note, ligne à ligne (N5, N6, N7 avec défaut sous 48 heures, aucun pour une dépense).
3. **E2 et E3 récrits** : contenu conforme à la note (§ 2.2, § 2.3, § 3.1). E3 à 8 à 15 heures, E2 à 3,75 « comme au plan » : conformes à la note, § 3.3.
4. **C1, C2, C3** : contenu et heures conformes (C1 3,5 à 39 heures par texte, classe A ; C2 2 à 3 ; C3 1 à 2 en plus de E1). M1 et S1 laissés à leurs chantiers : juste (« en révise deux et en ajoute cinq »).
5. **Une reprise incomplète.** Plan, § 2.1, ligne « issue » : « sans gain si l'écart apparié ne passe pas le seuil ». La note dit : écart apparié **au témoin, au placebo et à la base**. Les trois comparaisons sont à écrire dans la ligne, puisque C1 la reprendra.
6. **Une règle neuve non posée comme proposition.** Plan, § 8, point 1 : « deux cartes de même fiche et de même greffon sont une seule tentative. À écrire au texte de la porte. » La note ne porte pas cette règle. Elle touche le compte des tentatives, et « même greffon » dépend de ce qu'écrit l'expérimentateur. À marquer « proposition », adressée au rédacteur de C1.
7. **Deux étiquettes neuves sans le dire.** « Régime étage seul » pour le premier emploi (E8) : la note ne le nomme pas pour cette course ; GO-2026-11-21-16 l'accorde à la seule course « seuil et moniteurs », et le lanceur v10 refuse « les tests de mort seuls » (l. 14 à 16). C'est un régime neuf, qui demande son additif et le mot de Lazar (D1). À dire comme tel. « Un seul programme de vérification d'extrait ; deux gabarits » (E2) est aussi une proposition, dite comme un fait.
8. **Ordre des pas.** La note (§ 4.1, pas 1) veut le compte des cartes avant tout devis (« sans ce compte, aucun devis »). Le plan met bien le compte avant le premier dollar (§ 4.2), mais son horloge (§ 5) écrit « une issue par carte : après la mesure, et après D8 ». Cela laisse croire que la mesure sur les témoins peut partir sans le compte. À trancher dans le texte : soit la mesure attend D8, comme le veut la note ; soit le plan propose de la séparer, et le dit comme proposition.
9. **Exclusion de la note non reprise.** La note, § 4.1, dernier alinéa : les épreuves déjà engagées (lignes 1 et 3, héritage) gardent leur texte scellé ; la porte commune ne vaut que pour les cartes qui n'en ont pas. Le plan compte partout « 94 cartes ». À dire : 94 est une borne haute, moins les cartes déjà sous un texte scellé.
10. **Une ambiguïté de la note, à faire remonter.** La note met le rejeu du greffon « du côté de la machine » (§ 3.1, point 2 : « seul code neuf du côté de la machine »). Elle met aussi le banc et la vérité chez la mère, et l'issue « sur processeur » (§ 2.5, § 4.1). Le plan reprend la seconde lecture (E3 : « le banc et la vérité ne montent jamais sur la machine ») sans dire où tourne le barreau 1. Or ce barreau rejoue, à chaque génération du banc, du code écrit par un modèle, sur tous les mondes et tous les bras. Si c'est chez la mère, il faut un bac local entre le greffon et la vérité, comme au palier 0a, et le dire (N6). Si c'est sur la machine, la vérité y monte ou le banc s'y coupe en deux. Dans les deux cas, la durée de ce rejeu n'est pas au devis.

## 2. Les faits, vérifiés à leur source

1. **v68 en moteur simulé seulement** : vrai. Manifeste `4ed9fd8e…` : `simulation_v68.py`, « moteur simulé » ; `ideation_v68.py`, « options des interrupteurs (éteints par défaut) […] moteur réel refusé par construction ». Versée sur `main` (R-4383, R-4385).
2. **L'additif v69 v4 « ne touche pas la course d'auto-conception »** : vrai, § 8, l. 256 : « Il ne touche pas la course d'auto-conception : ses champs de fiche restent ceux de sa configuration (GO-2026-11-20-05, 3a). » Son § 0, point 1 : un seul régime, une seule épreuve (palier 1, une génération, aucun bras), tout le reste refusé en réel.
3. **Lanceur v10, interrupteur éteint** : vrai. L. 8 et 9 (`tests_de_mort_reels`, « éteints (défaut) ») ; l. 566 ; état éteint l. 602 à 604 ; moteur réel refusé par construction, cinq blocages l. 606 à 619, que la v1 cite aux bonnes lignes ; additif d'interrupteurs « à venir », `(None, None)`, l. 573 à 575.
4. **Étage v57 joué une fois en réel (course v67)** : vrai, au sens « avec de vrais modèles ». `tour_ferme_v64.py` importe `jouer_etage_v57` (l. 116) et l'appelle (l. 880). Le verdict v67 (§ 4.4) relève 14 tests dans un vrai bac, sur machine louée. Le palier 0a l'a joué aussi dans un vrai bac local, mais avec un expérimentateur écrit par programme (R-3882). Au passage, la question 3 du lot E0 de la v1 (« quelle version de l'étage la v67 a-t-elle jouée ») a sa réponse : la v57, par le tour fermé v64.
5. **Coût relevé à la v67** : vrai. 1,13813 USD de relais côté expérimentateur et 0,85618 côté vérificateur, chacun divisé par 14 : 0,081 et 0,061 USD, appels de proposeur compris (verdict, l. 148 à 151 et 164).
6. **D3 et D4 accordées** : la ligne existe. R-4394 (07:12:53Z) : « Mère : AC-1, rien de servi ». Le plan dit « ligne de registre non lue par moi » : à remplacer par ce renvoi.
7. **Pièces citées du pilier** : vérifiées. Plan du pilier, § 5, point 2 : « un calcul exact dans le bac » ; lot E1 : erratum ; « H+48 au plus tôt (23 novembre) » ; script lu à `8223c37f…`. Devis du pilote, l. 15 : 0,28 USD de l'heure (0,22692 EUR), borne haute 1,30.
8. **Seuils de la définition scellée** (réserve (i) du plan, § 2.4) : je l'ai ouverte. Les cas A et B portent des seuils chiffrés : A, « au moins deux fois le niveau annoncé », ramené au niveau en gardant « au moins quatre cinquièmes » des vraies ; B, « au moins un quart de lois vraies promues en plus, en relatif », ou le même rappel pour la moitié du budget. Le cas C renvoie au seuil de B « à la dernière génération jouée », contre un placebo de même forme. Il ne se lit donc que sur un banc à plusieurs générations, ce que le barreau 1 permet. À écrire au texte de la porte. Ces seuils sont des tailles d'effet, à joindre au test exact des rangs signés.

## 3. Les treize lots

1. **Compte et nature** : treize lots (E0 à E9, C1 à C3), justes. M1 et S1 hors du plan, juste.
2. **La table du § 4.2 contredit le § 4.1 sur trois dépendances.** E2 dépend aussi de E3 (liste fermée des points de greffe, § 4.1). E3 dépend aussi du comparateur du palier 0b et de la lecture de la définition scellée (§ 4.1). E8 dépend aussi de C1 (table des épreuves : banque, table d'admission) et de N4. À porter dans la table.
3. **C2 « remplace le cœur du E4 »**, mais E4 reste compté à 2,75 heures. Ce n'est pas faux, juste prudent ; à dire, ou à réduire.
4. **Chemin critique** : « le texte de la porte » (C1) est celui de la note. Il tient tant que C1 approche sa borne haute : le chemin du code jusqu'au premier dollar (E0, E1, C3, E8, E9) fait de 17,25 à 18,25 heures. À la borne basse de C1 (3,5 heures), c'est le code qui est critique. Le plan doit dire les deux.
5. **Partages, à mettre à jour** (pièces versées avant la v2, l'auteur ayant relevé `date -u` à 07:42Z) :
   - NA-1 : le relevé du lot 0 est rendu (R-4411, `10ac79ec…`), avec deux contradictions qui touchent les relais et l'adaptateur. Son calendrier est passé à 48 à 60 heures (R-4415, R-4427). E0 doit lire ce relevé, et la question de la place du modèle F se relit avec ce calendrier.
   - « Seuil et moniteurs » : l'ordre est scellé en v4 (`390af604…`, R-4425), une v5 est en écriture, et le mandat des mondes plantés est confié à un auteur de la troisième lignée (R-4426, `75f0acd3…`). Le partage de la vérification d'extrait doit renvoyer à la v4 scellée, non à la v2 (`1fbd04c3…`). Le module commun « graines, disjonction, clé scellée » est à proposer à ce mandat, sinon il s'écrira deux fois.
6. **Pilier** : emprunts et dettes justes. Les trois écarts sont exacts, et la mère a annoncé deux erratums (R-4428).
7. **Lanceur.** Le plan reprend de la note « une table des épreuves dans le lanceur 11 » (§ 3, ligne § 2.3). L'additif scellé, § 7, point 5, fait du lanceur version 11 celui du seul palier 1 : « Tout autre jeu d'options est refusé par le lanceur version 11 lui-même ». Avec D3 accordée (AC-1), le lanceur de cette course porte un nom de la série AC-1. Sinon, le lanceur 11 demanderait un additif de plus. À corriger dans le plan, et à signaler à l'auteur de la note.

## 4. Calendrier et devis

**Recalculs, tous justes.**
- Code : 37,75 − 3,75 + (8 à 15) + (2 à 3) + (1 à 2) = 45 à 54. Premier emploi, sans E5 (4,75) ni E6 (3,75) : 36,5 à 45,5. Textes : 20 + (3,5 à 39) = 23,5 à 59. Somme : 68,5 à 113.
- Bac. Bas : 106 tentatives au plus × 3,25 min (v67 : de 14:21:52 à 15:07:22, soit 45,5 min pour 14 tests) + 1 h, soit 6,7 h, arrondies à 7. Haut : 106 × 9 min + 10 h = 25,9, soit 26. Location : 7 h donnent 0,51 / 1,96 / 9,10 USD ; 26 h donnent 1,91 / 7,28 / 33,80 ; 48 h donnent 3,52 / 13,44 / 62,40. Seuil du plafond : 15 / 48 = 0,3125 USD de l'heure.
- Appels : 4 × 0,08 = 0,32 ; 12 × 4 = 48 ; 94 × 0,08 = 7,52 ; 94 × 4 = 376. Barreau 2 : 10 × 58,64 = 586,4 ≈ 590 ; 10 × 8,92 = 89,2 ≈ 90. Cinq paires pour le test exact unilatéral à 5 % : 1/32 = 0,031 < 0,05, alors que quatre paires donnent 1/16 = 0,0625 (juste).

**Ce qui n'est pas dit comme non mesuré, ou dit trop court.**
1. **§ 0, point 5** : « de 0,51 à 13,44 USD selon la machine » tait la colonne à 1,30 USD de l'heure (9,10 à 62,40) et ne dit pas « aucun prix relevé aujourd'hui ». Le § 6 le dit ; le § 0 doit le dire aussi.
2. **Le lecteur témoin est hors du coût en appels.** L'étage v5, « sans un octet changé », sert la fiche à un lecteur témoin (additif, § 9, réserve 1 (c) ; N4 le nomme). À la v67, il coûtait 0,061 USD par test. La borne basse par greffon serait donc d'environ 0,14 USD, non 0,08 (environ 13 USD pour 94 cartes, au lieu de 7,5), sauf si le régime de cette course retire le lecteur. Dans ce cas, il faut le dire, et c'est un écart à l'étage tel quel. À écrire en clair dans le § 6.3 et dans le § 0.
3. **Barreau 2** : « de l'ordre de 590 USD par carte » est un coût **de propositions seules**, tiré d'un devis (devis de l'héritage v5, § 2), non d'une mesure. La note le dit « de propositions » ; R-4422 le marque « hypothèse ». Le plan (§ 0, § 2.1, § 6.3) l'écrit sans ces deux mots, et sans les appels de l'étage dans la boucle. À ajouter partout.
4. **Le devis du bac mêle deux dépenses.** Les cas du § 6.2 comptent les témoins et les 94 cartes, alors que D6 (changée par la mère) ne demande d'abord que les témoins, et que les 94 cartes attendent D8 puis un second devis. À séparer : ligne 1, les témoins (quelques heures de machine, 0,32 à 48 USD d'appels plus le lecteur) ; ligne 2, les cartes, après le compte.
5. **« Une issue par carte, sur processeur »** (§ 5) : le verdict se calcule sur processeur, mais chaque carte coûte une session d'expérimentateur et deux traductions. À dire : seconde dépense, sur devis.
6. **Textes « 20, inchangés »** : ce total vient de la v1, à dix lots et sans pont. Il ne compte ni les consignes des deux traducteurs, ni le gabarit « mécanisme », ni le mandat de l'agent de compte, ni un additif par épreuve, ni trois mandats de lot de plus. La borne basse de 23,5 heures est donc probablement basse. À dire comme estimation non revue.
7. Les hypothèses du planificateur (douze témoins, huit heures de mise au point, 48 heures de durée maximale) sont dites comme telles (§ 6.2, § 9) : conforme.

Les dates ne sont pas jugées ici : la mère les lira après le mot de Lazar sur l'ordre des pilotes.

## 5. Le premier emploi sur les 94 cartes de la v9

1. **Avec la note** : cohérent. La note, § 4.1, met les pas 1 à 4 sur les cartes existantes, et la génération neuve au pas 5 seulement. E5 et E6 sortent bien du chemin critique, et D4 (rien de servi) est sans objet au premier emploi, faute de génération suivante. Une phrase est inexacte : § 0, point 2, « les quatre premiers pas portent sur les 94 cartes ». Le pas 3 porte sur les seuls témoins. Écrire plutôt : « n'exigent aucune génération neuve ».
2. **Avec la règle du dossier d'archives** : le premier emploi dépend entièrement de D8, et D8 n'a pas de défaut. Le plan ne dit pas ce qu'il devient si Lazar retient D8 (c) : le premier emploi se réduit à la mesure sur les témoins, et E5 et E6 reviennent sur le chemin critique. À écrire.
3. **D8 n'est pas posée sur le modèle accordé.** La mère la veut sur le modèle de GO-2026-11-20-15 et -28. Or ces deux lignes disent « un agent neuf, qui **ne lit aucune carte** », un programme écrit ou contre-lu par la mère, et des sorties réduites à des identifiants, des comptes ou des noms de clés. Le plan cite à la place GO-2026-11-21-04 (une copie sans ouverture). Son option (a) fait **ouvrir** les cartes par un agent, et la note demande un compte de nature (« combien changent l'épreuve, une règle, la conduite de modèles »), qu'aucun programme ne rend seul. D8 est donc plus large que tous les précédents. Elle doit le dire, et nommer :
   - (i) qui lit, par quel programme, et ce qui sort (comptes et fiches à champs fermés seulement) ;
   - (ii) que les deux traducteurs, qui reçoivent chaque carte entière, sont une seconde lecture du même dossier, servie hors de la maison, donc une seconde exception et une dépense ;
   - (iii) que la mère n'y entre pas ;
   - (iv) une option de plus, à vérifier : un premier compte tiré des pièces déjà sur `main`, qui classent les cartes sans rouvrir le dossier. La proposition `a2cd45ad…` (GO-2026-11-19-55 à -60), la lecture descriptive `0306adf7…` (la note en tire 42 et 34 mentions) et la relecture des 22 cartes sous la définition scellée (GO-2026-11-19-60). Ce compte servirait au moins de borne pour le devis.

## 6. Les quatorze décisions

1. **Le compte** : 7 + 6 + 1 = 14, juste.
2. **N1 à N7** : condensés en table, au format par renvoi à la note, où chacun a enjeu, options avec avantage et inconvénient, recommandation et confiance. Acceptable ainsi. Aucun défaut pour une dépense (N1, N2, N4 sans défaut).
3. **D1** : au format (v1). À compléter du régime « étage seul sur cartes archivées » (point 1.7) : D1 doit nommer cette variante, sinon le mot de Lazar ne la couvre pas.
4. **D5 et D6 se contredisent.** D5 (a), recommandée avec un défaut sous 48 heures pour l'écriture, dit « palier 1 d'abord […], cette course ensuite ». D6, changée par la mère, met la mesure sur les témoins de cette course **avant** le palier 1, avec l'essai du bac et le sommet d'étage écrits pour elle. Le plan dit D5 « renforcée » : c'est faux. D5 est à récrire au format, avec l'ordre qui découle de D6, et son défaut à redire sur ce texte neuf.
5. **D6 n'est plus au format.** La recommandation neuve (« la mesure sur les seuls témoins ») ne figure parmi aucune des options (a), (b), (c) de la v1. À récrire : décision en une phrase ; enjeu ; deux ou trois options avec avantage et inconvénient (par exemple, mesure sur les témoins seuls ; attente du palier 1 ; devis sur les bornes, avec plafond d'arrêt) ; recommandation et confiance ; **aucun défaut**. L'absence de défaut est déjà dite : conforme.
6. **D7** : « absorbée en partie par N2 et N3 ». À dire ce qui en reste à décider : le texte neuf de la course pour les suivantes.
7. **D8** : au format (options, avantage, inconvénient, recommandation 0,6, aucun défaut). À récrire sur le fond (point 5.3).
8. **D3 et D4** : marquées accordées, juste ; source R-4394 (point 2.6).

## Corrections demandées, en une liste

1. § 7.2 : récrire D6 au format complet, avec l'option retenue par la mère parmi ses options, sans défaut.
2. § 7.2 : récrire D5 au format, accordée à D6 (ordre des écritures et du premier allumage), retirer « renforcée », et redire son défaut sur le texte neuf.
3. § 7.2 : récrire D8 sur le modèle de GO-2026-11-20-15 et -28, en disant en quoi elle les dépasse (lecture du contenu ; traducteurs) ; ajouter l'option du compte tiré des pièces déjà sur `main`, à vérifier ; dire ce que devient le premier emploi sous D8 (c).
4. § 0, § 2.1, § 6.3 : barreau 2 dit « de propositions seules, tiré d'un devis, hypothèse », hors appels de l'étage.
5. § 0, § 6.3 : coût en appels avec ou sans le lecteur témoin, dit en clair (environ 0,061 USD par test à la v67) ; les traducteurs, non chiffrés.
6. § 0, point 5 : donner la colonne à 1,30 USD de l'heure et « aucun prix relevé aujourd'hui ».
7. § 6.2 : séparer la ligne des témoins (première dépense) de celle des 94 cartes (après D8, second devis) ; § 5 : « une issue par carte » est une seconde dépense.
8. § 3 et § 4.2 : lieu du rejeu du barreau 1 (bac local chez la mère, ou machine), son coût en temps, et l'ambiguïté de la note, § 3.1, point 2, à faire remonter.
9. § 3 : lanceur de la série AC-1, non « lanceur 11 » (additif scellé, § 7, point 5).
10. § 8, point 1 : marquer « proposition » la règle « même fiche, même greffon, une seule tentative » ; § 4.1 : idem pour « un seul programme de vérification d'extrait » ; E8 : « étage seul » dit régime neuf, sous D1.
11. § 2.1 : « sans gain » contre le témoin, le placebo **et** la base.
12. § 4.2 : dépendances de E2 (E3), E3 (comparateur du palier 0b, définition scellée), E8 (C1, N4) ; chemin critique dit aux deux bornes de C1.
13. § 4.1, E2 et E3 : renvoyer à l'ordre v4 scellé de « seuil et moniteurs » (`390af604…`) et au mandat des mondes plantés (`75f0acd3…`) ; E0 : lire le relevé du lot 0 de NA-1 (`10ac79ec…`).
14. Partout : « 94 cartes » est une borne haute, moins les cartes déjà sous un texte scellé (note, § 4.1).
15. § 5 : ordre du compte des cartes et de la mesure sur les témoins, à trancher (note : le compte d'abord).
16. § 7.2, D3 et D4 : citer R-4394. § 2.4, réserve (i) : seuils de A et B chiffrés, C sur plusieurs générations (point 2.8). § 0, point 2 : « aucune génération neuve » plutôt que « portent sur les 94 cartes ».

## Pour la mère

1. **D5 et D6** : la D6 que tu as changée défait l'ordre de D5 (a). Le défaut de D5 sous 48 heures ne doit pas courir sur l'ancien texte.
2. **Note de conception, une ambiguïté** : le rejeu du greffon est « côté machine » (§ 3.1, point 2), mais la vérité et le banc sont chez toi. À faire préciser par son auteur avant E3 et C1, avec N6.
3. **La note veut une table des épreuves dans le lanceur 11**, que l'additif scellé de la v69 réserve au palier 1 : à corriger à la source, ou à loger sous AC-1.
4. **Coût du lecteur témoin** : relevé par la note (§ 1 : 0,061 USD par test à la v67), mais absent de ses bornes par greffon (0,08 à 4 USD) comme de celles du plan. Il relève la borne basse des appels d'environ 75 %.

## Pour Lazar

1. **D8 est plus large que les exceptions déjà accordées** (GO-2026-11-20-15 et -28, où aucun agent ne lit de carte) : un agent lirait le contenu des cartes, et deux traducteurs de deux autres lignées recevraient chaque carte. Ce sont deux exceptions et une dépense. Une voie plus étroite reste à vérifier : un premier compte tiré des classements déjà sur `main`.
2. **N1 à N4, D1, D6, D8** restent sans défaut ; la première dépense (mesure de l'expérimentateur sur les témoins) n'a pas encore de devis, et son coût en appels va de 0,32 à 48 USD, lecteur témoin non compris.

## Ce que je n'ai pas lu

La conception du véhicule NA-1, le paquet v68 au-delà de son manifeste, le code du palier 0b, le banc de la ligne 1, le préenregistrement du pilote du pilier, la proposition `a2cd45ad…` et la lecture descriptive `0306adf7…` (citées ici comme pistes, non vérifiées), l'ordre v4 de « seuil et moniteurs », le relevé du lot 0 de NA-1 (cités par le registre seul).

— contre-lecteur du plan de la course principale, modèle O
