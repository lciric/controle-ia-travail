# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v2` (empreinte du module c8e8506f8d7cb9487173090aa9a000c1ab217377946f55cb338a45f07ca3d7f3)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGngLtXXHgVnRNu1PZR3`
- Heure (UTC) : 2026-11-21T21:50:21Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/consigne-relecture-v1.md` — sha256 43386bfb0e4ddf89812b2820d3314e7711454db7e0dc85ace4eccfd7cb0def4e (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/SPARKS-EXP7-NUL-preenregistrement-v2-brouillon2.md` — sha256 35e432cee7f605fa102942aa4809c4def4327af28aba8ae731d731173a3df32d (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/calculs-preenregistrement-v2-brouillon2-v1.py` — sha256 6abcbed85fb278637b23fb85685d1d015b7b0aeb518c88fff634c85581a28b21 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/calculs-preenregistrement-v2-brouillon2-v1.txt` — sha256 28884adb2e3f2edc8ee1f55925233726223f56e3e98742957056820024ba9244 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/contre-lecture-sparks-v2-brouillon1-opus-v1.md` — sha256 20cb7befaec9262320157697b266af4c00bb3f30ef88537d9fad10cfaaf61ffd (compagnon : vérifié)
  - avant : `docs/notes/relecture-fable-api-v1/envois/2-sparks-exp7-nul/SPARKS-EXP7-NUL-preenregistrement-v2-brouillon1.md` — sha256 59f952321910ca1ae59941055e922c6d12f96038576fe10046c2c9d0d29351f4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 81e552aa34ed160fcc6ed96e3c768729e6a6f8c60b8a054f2204cc0e03359aed
- Jetons : entrée 111290, sortie 119934 (dont réflexion 115199), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 5.687680 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**à corriger**

Peu de chose. Les dix-huit remarques sont portées, aucune n'est déformée sur le fond, et le seul choix que la contre-lecture laissait (I-4, point iv) est resté ouvert. Les calculs que j'ai refaits sont justes. Il reste trois reprises : une phrase de « Seuil » que I-1 (a) rend fausse, quelques mots ajoutés au-delà des remarques, et trois points à inscrire comme ouverts.

Je n'ai ni l'addendum, ni le texte v1, ni la lecture factuelle du billet : ce qui en est repris reste à confirmer par qui les a lus. Hors des lieux que liste la table « Corrections du brouillon 2 », je n'ai trouvé aucune différence entre les deux brouillons.

## Corrections, avec leur texte

**1. « Seuil », puce de la marque (suite de I-1 a, non portée).** La phrase « Elle ne change aucun verdict » est restée, alors que la marque change maintenant le nom de deux verdicts et leur réponse à Q1. Remplacer « Elle ne change aucun verdict ; elle borne ce que la scission montre (section « Critères de lecture gelés »). » par :

> Elle ne fait passer aucun verdict d'une ligne à une autre ; posée, elle entre dans le nom du verdict des lignes 1 et 2 et dans leur parenthèse de Q1, avec « scission non probante » ; elle borne ce que la scission montre (section « Critères de lecture gelés »).

Table des corrections, ligne I-1 (a), colonne « Lieu », ajouter : « ; « Seuil », marque ».

**2. Trois ajouts à ramener à la lettre de la remarque.** Si le contre-lecteur les confirme sur la source, les garder et le dire à leur ligne de la table.

- **m-12**, « Ce que ce texte change », en tête. « sur les options de la contre-lecture de l'addendum » n'est pas dans la remarque. Texte : « Les quatre décisions prises sur l'addendum, par conv-audit et non par le directeur (ad1, l. 17), sont gardées : la base … » (suite inchangée).
- **m-13**, trois lieux. « gabarits de » n'est pas dans la remarque.
  - Base d'attention scriptée : « Sur les mêmes 16 textes, tirés de faits **absents de tous les partages** (v1, l. 70) : pour chaque tête, … ».
  - Table du réemploi : « … aucun entraînement n'a eu lieu ; tirés de faits absents de tous les partages (v1, l. 70) : c'est leur raison d'être ».
  - Table des corrections : « Les seize textes sont dits tirés de faits absents de tous les partages (v1, l. 70) ».
- **m-7**, esquisse de devis. La source « p3, l. 42 (4 tentatives sur 3 paires sans l'outil) » n'est pas dans la remarque.
  - Colonne « Source » : « p3, l. 108 ».
  - Table des corrections : « … dont 12 sans l'outil d'attention (p3, l. 108) ».

**3. Trois lignes à ajouter sous « Nœuds ouverts par la correction, non tranchés par le correcteur ».**

> - **C-3 et la raison « économie de Fable »** (m-1). La remarque nomme C-3 et ne donne de texte que pour le nœud 1, option (d). La raison de C-3 reste telle quelle. Au rédacteur.
> - **« Par lecteur » et générateur de la marque** (m-10). L'addendum avait deux lecteurs, ce texte un : « par lecteur » est rendu par le second lecteur, s'il est accordé ; c'est une lecture du correcteur. La remarque donne `dispersion-reechantillonnage` avec un point d'interrogation ; il est nommé ici. Les deux sont à confirmer par le rédacteur.
> - **Qui vérifie les corrections.** C-2 et l'étape (1) de l'ordre de scellement disent : le même contre-lecteur. GO-2026-11-21-84 dit : Fable 5.2 par l'API. Aucune remarque ne vise ces lignes ; elles restent telles quelles. Au rédacteur ou au directeur.

**4. Facultatif.** Sous « mes calculs », dire qui a écrit la version 2 : « au brouillon 2, version du correcteur, `calculs-preenregistrement-v2-brouillon2-v1.py`, … ».

## Remarque par remarque

| Remarque | Portée exactement ? | Note |
|---|---|---|
| I-1 (a) | Oui, au lieu dit | Laisse « Seuil » en contradiction : correction 1 |
| I-1 (b) | Oui | Option, source et coût : les mots de la remarque |
| I-1 (c) | Oui | |
| I-1 (d) | Oui | C-6 et le nœud 5 (b) gardent « 0,107 » sans réserve ; la remarque ne vise que la section des bases |
| I-2 | Oui pour ses trois éléments | Quatre précisions de plus : « `recette.py` : l. 231 », « mêmes valeurs que des copies servies », « sans effet s'il est publié en bf16 », « float64 ». Justes si c'est la lettre de l'addendum, l. 650, que je n'ai pas |
| I-3 | Oui pour ses deux éléments | De plus : `bases.seuil_exactitude_equilibree`, la règle « +1 si l'aire… », « descriptive ». Même réserve, l. 651 |
| I-4 (i) à (iii) | Oui, mot pour mot | |
| I-4 (iv) | Laissée ouverte, comme il se doit | Le marqueur neuf bloque le scellement |
| I-5 | Oui | Table et lecture mot pour mot ; les huit valeurs recalculées |
| m-1 | Oui au nœud 1 (d) | C-3, que la remarque nomme, ni touchée ni signalée : correction 3 |
| m-2, m-3, m-6, m-11 | Oui | |
| m-4 | Oui, aux deux lieux | |
| m-5 | Oui | Option « retirer », la seule ouverte à qui ne lit pas d'autre page |
| m-7 | Oui, avec un ajout | L'ancienne mention reste devant le repère ; elle reste vraie (« par conversation »). Source ajoutée : correction 2 |
| m-8 | Oui | Les deux branches du « ou » sont faites ; 21,0 h est exact |
| m-9 | Oui | L'ampleur jointe à la liste vaut aussi « sur l'étalonnage », un peu plus que la remarque ; sans effet de fond, à garder |
| m-10 | Oui, avec deux lectures | Correction 3. L'ordre de l'addendum (l. 712) et « aucune clé de tâche de plus » ne sont pas vérifiables ici |
| m-12 | Oui, avec un ajout | Correction 2 |
| m-13 | Oui, aux deux lieux, avec un mot de plus | Correction 2 |
| Inscription | Hors remarque, déclarée, nécessaire | |

## Ajouts hors des remarques

- **Déclarés, à garder :**
  - la section « Corrections du brouillon 2 », l'en-tête, le pied et l'inscription de la contre-lecture ;
  - la version 2 du script et le renvoi de « calc, X » vers elle, que I-5 impose ;
  - le bloc I du script : m-8 ne le demande pas, mais il donne au « 21 h » une source rejouable.
- **Non déclarés :** ceux de la correction 2, et les précisions de I-2, I-3 et m-10 notées dans la table.

Tant qu'ils restent, « Rien n'est changé hors de la table » (en-tête) et « rien d'autre » (table) ne sont pas tout à fait exacts.

## Nœuds ouverts : recommandation et confiance, sans trancher

**Relances et ligne des 10 % (marqueur neuf).**
- **Les relances comptent-elles ?** Recommandation : non ; elles sont comptées et rapportées à part. Confiance 0,7.
  - La ligne vise les conversations dont l'issue est un échec imputé. Une relance qui aboutit donne une réponse valide ; une seconde interruption devient « coupée » par (iii) et compte déjà.
  - Je changerais d'avis si la liste des signaux (i), une fois écrite, ne séparait pas nettement panne et coupure du fournisseur.
- **Dénominateur.** Recommandation : 48, numérateur et dénominateur sur le bras principal, l'ancre comptée à part. Confiance 0,6.
  - La ligne marque « non concluant » la lecture principale, qui porte sur ces 48 cas ; l'ancre est lue après, sous une autre consigne.
  - Avec 48, la ligne sonne à la cinquième conversation comptée (5/48 = 0,104) ; avec 51, à la sixième (5/51 = 0,098).
  - À vérifier avant de choisir : ce que compte la source (v1, l. 172).

**Nœud 5.** Recommandation : (a). Confiance 0,65, contre 0,75 pour le rédacteur.
- Je baisse parce que le rédacteur donne 0,6 à la marque posée (P13). Dans ce monde, (a) rend un verdict « scission non probante » : elle nomme le défaut, elle ne l'ôte pas.
- L'option (d) est la seule qui vise la cause. Mais rien ici ne montre que des paires nulles à données permutées égalisent l'ampleur, et elle change la fabrication.
- Je ne l'examinerais que si l'étalonnage montre une séparation et si le directeur veut une scission probante.
- Pour le rédacteur : la marque ne lit que l'aire « vraie contre nulle ». Si les types se rangent « deux sycophantes, puis vraie, puis deux honnêtes », cette aire reste près de 0,5 alors que les types se séparent. C'est possible si les sycophantes bougent peu du départ, comme P8 le prédit.

**Nœud 1.** Recommandation : celle du rédacteur, (a) par défaut, (b) si le directeur veut un verdict qui tranche. Confiance 0,6. Les corrections m-1 et m-2 ne changent pas la balance : (c) ne se chiffre pas tant que le modèle n'est pas nommé, (d) attend le mot du directeur sur le quota, et aucune des deux n'ajoute de puissance.

**Nœud 7, option (c), touchée par m-3.** La correction lui retire un appui : la suite n'est pas montrée verte sur une telle machine. La recommandation (c) tient encore, un peu moins fort. Confiance 0,55.

**Les trois points de la correction 3.**
- **C-3 :** borner la raison à ce que dit la règle, qui réserve Fable 5.2. Confiance 0,7.
- **« Par lecteur » :** garder la lecture du correcteur. Confiance 0,7.
- **Générateur de la marque :** garder `dispersion-reechantillonnage` ; c'est le même intervalle que celui de la dispersion entre graines. Confiance 0,85.
- **Qui vérifie :** garder la vérification par le contre-lecteur, au moins pour ce que je n'ai pas pu confronter aux sources. Confiance 0,75.

**Huit marqueurs du brouillon 1.** Aucune remarque ne les ferme : c'est exact.

## Calculs refaits

Refaits à la main, par sommes binomiales exactes, sans exécuter le script.

- **Bloc H (I-5) :** les huit valeurs sont justes, égales à la table de la contre-lecture et à celle du texte.
- **Bloc I (m-8) :** 26 × 1 632 / 2 016 = 21,05, soit « 21,0 » et « environ 21 h ».
- **Reste de la sortie :** chaque valeur des blocs A à K retombe sur le fichier. Par exemple, les 53 cas sur 495 du bloc F se retrouvent par décompte, et les quatre bornes de Clopper-Pearson par encadrement.
- **Dans le texte :** 53 et 99 fois la moyenne donnent 70,8 et 132,2 millions ; P15 somme à 1 ; 1 − 0,490 = 0,51.

## Ce que je n'ai pas pu vérifier

- Tout ce qui est repris de l'addendum (l. 17, 650, 651, 712), du texte v1 (l. 70, 71, 190) et de la lecture factuelle (l. 42, 108).
- « Seuls ajouts » au script : le script du brouillon 1 n'est pas joint.
- Le rejeu sous deux Python, les empreintes, les simulations de l'addendum et calc96.

## Vu en passant, hors de la correction

- `dispersion-reechantillonnage` tire plusieurs intervalles sans ordre d'emploi écrit. Celui de la marque entre maintenant dans un nom de verdict : l'ordre mérite d'être écrit (R9).
- Goworek et al. : le brouillon place « how far each poisoned model is from the clean one » page 14, la contre-lecture page 13.
- Contre-lecture, § 5, point 3 : deux « [P] » y sont dits « des choix ». Ce n'est pas porté, à bon droit, car hors des sections 3 et 4. Au rédacteur.
