# Préenregistrement — P3-bis, addendum 3 : relance à l'aveugle après une fin anormale par épuisement du crédit, garde du crédit d'origine rétablie, par écart (R-2492) — v1 — brouillon 1

- Auteur : développeur-rédacteur neuf (sous-agent, Claude Opus 5.5), consigne
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-p3bis-ecart3-v1.md`
  (`09311f1c4aed6db0fa01c6b2737e07c57c5f3b924f3559cc3abbd0fb387a75ba`, vérifiée, égale à son compagnon). Il n'a écrit
  ni P3-bis, ni sa chaîne, ni les écarts 1 et 2, ni leurs addendums. Il n'a ouvert aucun fichier de T0.7, ni la branche
  `calcul/p3bis-reel-v1`, ni aucun résultat de P3-bis. Du texte scellé, il a lu les lignes 1-30, 1404-1414, 1835-1850,
  1898-1970, 2140-2320 et 2440-2480, plus des recherches par motif dans ce seul fichier ; des addendums 1 et 2, le texte
  entier.
- Date (UTC) : brouillon 1, 2026-11-13, de 08:00 à 08:11 (`date -u`). Au scellement, la date du commit de scellement
  fait foi.
- Texte scellé complété : `prereg/P3-bis-temoin-positif-v1.md`
  (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`), commit de scellement
  S = `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0`. Les numéros de ligne « l. » sans autre précision sont ceux de ce fichier.
- Addendum 1 : `prereg/P3-bis-addendum-1-garde-credit-v1.md`
  (`4e188814b52736edb6f690931b25e6c0d9cdaede20b23490d50aa5461c5ca537`, R-2407), cité « A1 l. ». **Sa règle du crédit
  est retirée par cet addendum** ; sa réserve au verdict reste.
- Addendum 2 : `prereg/P3-bis-addendum-2-telechargement-controle-v1.md`
  (`c23b2eb0beb5de34db4359b9b97624df09c9b076d5ebe3d20c5b74e257ec9444`, R-2457), cité « A2 l. ». **Il reste en vigueur**,
  lu comme dit plus bas.
- Registres cités, au commit `f1b6b9fa46e05c953b48bb2182e166a723d7299c` (branche de la session mère, tête à 07:48:57Z le
  13 novembre ; `main` local est plus ancien et ne porte pas ces entrées) :
  - `registres/decisions.md` (`bba739409e2a9d1d823fd47d05883caac8ae0c9649e55aef0c8204b1ef2d5357`), entrées R-2463,
    R-2479, R-2480, R-2489, R-2490, R-2491, R-2492, R-2493 ;
  - `registres/depenses.md` (`c79537bab79f8fc5fc68e6e750aa15d6d6fd7f5c8d7d414d500d4aca7e6db51a`), l. 419, 420, 431, 433,
    434, 435, 436 ;
  - `registres/arrets.md` (`3b9cb6ae7b64e689cf38779827f8b74142118836e02f6e8fc97d77add98a2093`), l. 109, 110 ;
  - `registres/go.md` (`405e4b56a4836716f2e05833b25a9d3097d88eaeb903671703eac7a40b16b341`), l. 217, 292.
- **Nœud tranché par Lazar** : écart au préenregistrement scellé, R-2492 (2026-11-13 vers 07:47 UTC), option (b) du
  nœud R-2490, mis à jour par R-2491.
- **Code de l'écart** : branche `prep/p3bis-ecart3-v1`, commit `02017d3252eca3c76c0a815e1124a023909aa96b`, tiré de
  `444645bbde329e05a5738e9a40a8ad48c8c28eb4` (tête de `prep/p3bis-ecart2-v1` : S, écart 1, addendum 1, écart 2,
  addendum 2). Rapport du développeur :
  `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-p3bis-ecart3-v1.md`.
- Contre-lecture (R2) : **à faire**, par un lecteur neuf d'un autre modèle (R-2493 : Claude Fable 5.2), sur le code de
  l'écart 3 et sur ce brouillon.
- Statut : brouillon 1, non scellé. Suite : contre-lecture, brouillon 2 s'il le faut, puis scellement comme les
  addendums 1 et 2 (R-2407, R-2457) : compagnon `.sha256`, versement sur `main` et, dans un commit postérieur au commit
  du code, sur la branche `prep/p3bis-ecart3-v1` ; une entrée au registre des décisions ; **aucune clé** dans
  `registres/scellements-v1.md` (l. 2009-2011). **Non décisif** : il ne touche ni à la lecture, ni à l'issue, ni au
  verdict, sinon par les réserves écrites plus bas.

## Objet

Faits datés, tous tirés des registres cités (aucun n'est relevé par le rédacteur) :
- **2026-11-13, 01:38:55Z** : instance **60432755** créée par l'enchaîneur v5, sous les écarts 1 et 2, tentative N = 1,
  branche `calcul/p3bis-reel-v1`, A100 SXM4 à 1,12 USD de l'heure ; dépense antérieure passée 0,68 USD (R-2479 ;
  `registres/depenses.md` l. 435). Crédit du compte à la création : **7,05 USD** (R-2491). Contrôle à cinq minutes
  d'écart 2 conforme (R-2480).
- **Entre 04:23:42Z et 04:25:45Z** : l'instance passe **seule** à `exited`/`stopped` (`status_msg=success`), vue deux fois
  de suite ; dernier `PROGRES` à 04:22:30Z, étape des épisodes, **lot 19 sur 30** ; aucune ligne de fin d'amorce, aucune
  erreur visible. Arrêt par l'identifiant demandé par la surveillance à 04:27:52Z, motif ÉTAT TERMINAL (R-2489 ;
  `registres/arrets.md` l. 109). Dépense de la course au dernier relevé : 5,79 USD (antérieure 0,68, calcul 3,11,
  majorant de téléchargement 2,00 ; `registres/depenses.md` l. 436).
- **Diagnostic en lecture seule de la fille** (R-2490) : journal du loueur sans erreur, trace, mémoire, disque, signal ni
  fin d'amorce ; cause non déterminable sur l'instance ; **`calcul/p3bis-reel-v1` égale à S (`8f8df8b2`), aucun résultat
  poussé** ; récupération non lancée, aucun paquet ouvert (R-2489).
- **07:30Z** : mot de Lazar, « vast n'a plus de credits » ; relevé de la mère en lecture seule : **crédit 0, solde
  −0,93 USD** ; 60432755 et 60417353 (témoin Bailey, autre session) toutes deux arrêtées. Consommation du compte
  ≈ 2,46 USD de l'heure (P3-bis 1,12 ; Bailey 1,342) : 7,05 USD épuisés vers 04:30Z, ce qui concorde avec l'arrêt vu.
  **Cause probable : épuisement du crédit de location. La recharge automatique, prémisse de l'écart 1 (R-2399, A1
  l. 46-48), n'a pas joué** (R-2491).
- **07:47Z** : mot de Lazar, option (b) (R-2492). **07:48:11Z** : 60432755 détruite par son identifiant par la mère ;
  absence relue (R-2493 ; `registres/arrets.md` l. 110).

**Pourquoi un écart.** La ligne 1 des critères (l. 1844) ne permet une relance sous ce texte que « si aucun épisode n'a
été joué » ; le devis le redit (l. 2468). Dix-neuf lots d'épisodes ont été joués : sans écart, aucune relance (R-2490). Le
risque résiduel écrit par l'addendum 1 s'est réalisé tel quel (A1 l. 178-180 : « Si elle [la recharge automatique] fait
défaut pendant la course, le compte peut s'épuiser et l'instance être arrêtée par le loueur »).

Cet addendum, **pour la course de P3-bis sous ce texte et sous GO-2026-11-10-02** : (1) permet une relance à l'aveugle
malgré les épisodes joués, sous quatre conditions ; (2) retire l'écart 1 et rétablit la garde du crédit d'origine ;
(3) remplace l'enchaîneur v5 par l'enchaîneur v6. Rien d'autre.

## Mot de Lazar (verbatim)

- R-2492 (≈ 07:47 UTC) : « Recommandation : (b), confiance 0,65 : go; ».
- L'option (b), telle que le registre la consigne (R-2492, point (1)) : « écart 3 au texte scellé (relance à l'aveugle
  sur `calcul/p3bis-reel-v2` malgré les épisodes joués, rien n'ayant été lu ni poussé ; garde du crédit rétablie, la
  recharge automatique ayant échoué), destruction de 60432755 par son identifiant, relance sous GO-2026-11-10-02
  (création au plus tard le 18 novembre) ; **recharge du compte Vast par Lazar exigée avant la relance** ».
- R-2491 met à jour le nœud : « option (b) exige d'abord une recharge par Lazar et une garde du crédit rétablie (crédit
  ≥ coût attendu de la course plus marge, comme le texte d'origine) ».

## Ce qui change

### R1 — règle de relance (écart 3)

**Règle.** Malgré des épisodes joués, une relance est permise sous ce texte quand les quatre conditions suivantes sont
toutes constatées par la session, chacune avec l'heure relevée par `date -u` :
- **(i) cause externe.** L'arrêt vient d'une cause externe à la chaîne et aux résultats, établie par le registre : ici,
  l'épuisement du crédit de location (R-2491 : crédit 0, solde −0,93 USD ; consommation et heure d'épuisement concordantes
  avec l'arrêt vu ; journal sans erreur, R-2490). Une panne de la chaîne, du run ou de la machine n'est pas une cause
  externe au sens de cette règle ;
- **(ii) rien de poussé.** Rien n'a été poussé au-delà de S : la branche de calcul de la tentative arrêtée est égale à S
  (R-2490 : `calcul/p3bis-reel-v1` = `8f8df8b2`) ;
- **(iii) rien de lu.** Aucune lecture ni ouverture n'a eu lieu : récupération non lancée, aucun paquet ouvert, aucun
  fichier d'issue écrit (R-2489, R-2490). Le journal de l'instance, relu par la surveillance et par le diagnostic de la
  fille, ne porte par construction que des comptes, des durées et l'aire de validation générique (l. 1410-1411 : « aucune
  aire sur les épisodes de P3-bis ne sort avant la lecture ») ;
- **(iv) code inchangé.** Le code cité n'a pas changé (même lecture que A1, (b), l. 204-212, et A2 l. 398-401) : l'écart 3
  n'ajoute que des fichiers sous `docs/procedures/P3-bis-temoin-positif-v1/` et sous `brouillons/` (relevé du commit du
  code, section « Pièces »).

**Portée.** La règle vaut pour **la seule relance qui suit l'arrêt de 60432755** : tentative **N = 2**, branche neuve
**`calcul/p3bis-reel-v2`**, sous GO-2026-11-10-02, création **au plus tard le 18 novembre 2026** (borne de l'en-tête,
l. 1941-1942 ; constante `BORNE_CREATION` du lanceur). La relance est **à l'aveugle** : les 19 lots joués par 60432755
ne sont ni récupérés, ni lus, ni comptés ; la relance rejoue la course entière sous ce texte, mêmes graines, mêmes
critères. Une relance de plus (N = 3) n'est permise que par la ligne 1 telle qu'elle est écrite (aucun épisode joué) ou
par un nouveau mot de Lazar.

**Ce que la règle ne relâche pas.** La ligne 1 reste entière pour tout autre cas ; « **aucun fichier d'issue tant qu'une
relance est possible** » (l. 1844) vaut ; le fichier « non lu » n'est toujours écrit que sur un nœud tranché sans relance
(l. 1844). La règle « Relance après une instance gardée ou arrêtée » (l. 1949-1954) a joué : le mot de Lazar qu'elle exige
est R-2492, qui choisit la destruction par l'identifiant, faite (R-2493).

### R2 — écart 1 retiré, garde du crédit d'origine rétablie

**Règle.** La création n'est permise que si le crédit présent, lu dans la réponse de l'outil de location, est **au moins
20 USD plus 10 heures du prix des instances nommées en marche**, au centime (l. 1936-1937 ; plan, point 6 (ii),
l. 2150-2152 ; module commun d'origine `verifications_p3bis_v2.py`, sous-commande `credit`, `1524df5f…`, égal à S).
C'est la garde du texte scellé, sans changement.

**Écart 1 retiré.** La règle neuve de A1 (l. 46-51 : recharge automatique active et crédit présent > 0) et sa lecture des
l. 1936-1937 et 2150-2152 (A1 l. 55-56) **ne valent plus** pour aucune création sous ce texte. Motif : sa prémisse, la
recharge automatique constatée par Lazar (A1 l. 39-42, 171-172), a échoué (R-2491). C'est le « mot contraire de Lazar »
que A1 prévoyait (condition 4, l. 171-172 : « retour à la garde scellée, ou nœud ») : retour à la garde scellée.
Le lanceur d'écart 1 (`lancer_p3bis_v2_ecart1_v2.sh`, `2e294e5a…`) reste au dossier, tel quel (R12), et **n'est plus
jamais joué** pour une création de cette course.

**Lanceur joué.** Le lanceur d'origine scellé `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh`
(`029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08`, cité l. 2174-2175, égal à sa copie versée à S),
appelé par l'enchaîneur v6. Son bloc 2 compare lui-même son propre fichier (`$0`) et les quatorze autres scripts de la
chaîne à leurs copies versées à S.

### R3 — enchaîneur v6

`docs/procedures/P3-bis-temoin-positif-v1/enchaineur_p3bis_v6.sh`
(`1b49b701253b89fd42cad589097f700697dd38de0a178b1fadda168dbd7f521f`) = enchaîneur v5 (`34131eaf…`, A2 l. 213-235 et
454), **dont le seul changement de logique est le lanceur appelé** : le lanceur d'origine scellé, son empreinte épinglée
(`E_LANCEUR=029bdb5c…`, v6 l. 35) et vérifiée avant tout appel (l. 47-49), au lieu du lanceur d'écart 1. Hors
commentaires, trois lignes diffèrent de v5 (cas V-01 du banc) : l'épingle du lanceur, le nom dans l'usage, l'étiquette
du journal « enchaîneur p3bis v6 ». Le contrôle à cinq minutes, la surveillance et le module d'écart 2, leurs épingles,
l'attente de la création + 181 s, l'ordre « contrôle puis surveillance quel que soit le code du contrôle » (R-2393), la
dépense antérieure en cinquième argument, le jeton, le journal et les codes sont ceux de v5. Usage :
`setsid nohup bash enchaineur_p3bis_v6.sh S DOSSIER_NEUF EN_MARCHE 2 DEPENSE_ANTERIEURE_USD`, PID noté, arrêt seulement
par ce PID (R10).

**Essais R5** (banc `essais_ecart3_p3bis_v1.sh`, journal `essais-ecart3-p3bis-v1.log`, section « Pièces ») : sur un faux
outil de location, aucun appel réel ni dépense :
- **cas sain** : tentative N = 2, branche v1 présente au distant factice et égale à S, crédit 50 : lanceur d'origine
  appelé, ligne officielle « crédit 50.00 USD ; minimum 20.00 USD », aucune ligne d'écart 1, une création sur
  `calcul/p3bis-reel-v2`, étiquette `p3bis-v2`, contrôle d'écart 2 conforme, surveillance d'écart 2 jusqu'à FIN
  (E6-01) ; seuil au centime, 20,00 (E6-03) ; avec une instance nommée en marche à 1,342 USD de l'heure, 33,42 (E6-07) ;
- **artefacts** : crédit sous le minimum, **aucune création** : 19,99 (E6-02) ; **7,05, le crédit de la création de
  60432755** (E6-04) ; 0 et −0,93, le relevé du 13 novembre (E6-05, E6-05c) ; 33,41 avec l'instance nommée (E6-06) ;
  outil en échec avec une réponse lisible, crédit illisible (E6-09, E6-10) ; instance d'autrui arrêtée sur le compte
  (E6-08) ; **lanceur d'origine modifié** : refus de v6 avant tout appel (E6-11), et refus du lanceur lui-même si
  l'épingle de v6 était contournée (E6-12) ; lanceur absent (E6-13) ; **tentative N = 2 sans la branche v1 au distant :
  refus** (E6-14) ; branche v2 déjà présente (E6-15) ; N = 1 avec la branche v1 présente (E6-16) ;
- **témoin (R4)** : l'enchaîneur v5 et le lanceur d'écart 1, au même crédit de 7,05 USD, créent (E6-04T) ;
- **aval inchangé** : échec d'amorce, contrôle en code 1, la surveillance suit (E6-17) ; pièce d'écart 2 modifiée,
  refus (E6-18) ; arguments (E6-19 à E6-21) ;
- **bancs existants rejoués** : banc du lanceur d'origine, lignes de verdict égales au journal canonique versé à S
  (R-01) ; banc de l'écart 2, mêmes 132 cas et mêmes verdicts que le journal versé (R-02) ; quinze scripts d'origine
  égaux à S (R-03) ; enchaîneur v5, lanceur d'écart 1 et pièces d'écart 2 inchangés (R-04).

## Passages du texte scellé lus sous l'écart

Chaque passage est cité tel qu'il est écrit (sauts de ligne ôtés). « Nouveau » est la lecture qui vaut sous l'écart 3.
Le texte scellé n'est pas réécrit (R12).

**Q1 — Critères, ligne 1, l. 1844.**
- Ancien : « relance sous ce texte, sur une branche neuve (`calcul/p3bis-reel-v2`, puis `…-v3`), si aucun épisode n'a été
  joué, si le code cité n'a pas changé et si la création tombe dans la borne de création de l'en-tête […] et si aucune
  instance de P3-bis arrêtée ou gardée n'est sur le compte hors `ARRETEES_TOLEREES` »
- Nouveau : mêmes mots, puis : « ou, pour la seule relance qui suit l'arrêt de 60432755 (tentative N = 2,
  `calcul/p3bis-reel-v2`), malgré des épisodes joués, si l'arrêt est d'une cause externe à la chaîne et aux résultats
  établie par le registre (épuisement du crédit, R-2491), si rien n'a été poussé au-delà de S ni lu, et si aucune lecture
  ni ouverture n'a eu lieu (addendum 3, R1) ». Les autres conditions de la phrase (code cité inchangé, borne de création,
  aucune instance de P3-bis arrêtée ou gardée hors `ARRETEES_TOLEREES`) valent telles quelles.

**Q2 — Devis, « Relances », l. 2468-2471.**
- Ancien : « la ligne 1 ne permet de relancer sous ce texte que si aucun épisode n'a été joué. […] Pire cas de la course,
  deux tentatives avortées puis une complète au pire : ≈ 2 × 9,5 + 22 ≈ **41 USD**. »
- Nouveau : première phrase lue avec Q1. Le pire cas se relit sur les tentatives réelles : dépense antérieure
  ≈ 6,07 USD (préalable 4, calcul indicatif) plus une tentative complète au pire, ≈ 22,2 USD (l. 2467), soit
  **≈ 28,3 USD**, sous le plafond de 80 USD ; attendu ≈ 6,07 + 4,5 à 7,5 ≈ **10,6 à 13,6 USD** (l. 2465).

**Q3 — Liste d'arrêt, « Avant la création », l. 1936-1937 et 1947** ; **plan, point 6 (ii), l. 2150-2152.**
- Ancien : « un crédit sous 20 USD plus 10 heures du prix des instances nommées en marche ; […] : aucune création » ;
  « crédit exigé à la création : ≥ 20 USD plus 10 heures du prix des instances nommées en marche, recharge automatique
  du compte (`registres/depenses.md` l. 91) ».
- Nouveau : **la lecture d'origine revient** ; la lecture de A1 (l. 55-56) est retirée (R2). Dans la phrase du point 6
  (ii), « recharge automatique du compte » est une information sur le compte, non une garde (écart 8, l. 2285) ; elle ne
  dispense de rien.

**Q4 — Écarts du lanceur portés au texte, 8, l. 2285.**
- Ancien : « recharge automatique du compte : non lisible par la chaîne, non contrôlée par elle ; »
- Nouveau : mêmes mots ; s'y ajoute le constat daté de R-2491 : la recharge automatique n'a pas joué le 13 novembre ;
  la chaîne ne s'y fie plus (R2), la recharge est faite par Lazar avant la relance (préalable 2).

**Q5 — Écarts du lanceur portés au texte, 11, l. 2289-2291.**
- Ancien : « numéro de tentative (1 à 3) en argument ; une relance exige la branche de la tentative précédente ;
  « aucun épisode joué, code inchangé » reste vérifié par la session (critères, ligne 1) ; »
- Nouveau : mêmes mots ; pour la relance N = 2 sous l'écart 3, la session vérifie à la place de « aucun épisode joué »
  les conditions (i) à (iii) de R1, et « code inchangé » (iv). Le lanceur exige toujours, par lui-même, la branche v1 au
  distant et la branche v2 absente (`lancer_p3bis_v2.sh` l. 146-153 ; cas E6-14, E6-15).

**Q6 — Liste d'arrêt, « Dépense cumulée de la course », l. 1962-1963.**
- Ancien : « (calcul, disque, téléchargement, toutes tentatives et relances comprises, sous GO-2026-11-02-29 et
  GO-2026-11-10-02 ensemble, non cumulés) »
- Nouveau : mêmes mots ; la dépense de 60432755 (calcul, téléchargement, stockage jusqu'à sa destruction) entre dans la
  dépense antérieure (préalable 4) ; le plafond de **80 USD** et le calcul de l'addendum 2 ne changent pas.

**Q7 — Plan, point 6 (a), chaîne v2 citée par empreinte, l. 2174-2175.**
- Ancien : « `docs/procedures/P3-bis-temoin-positif-v1/lancer_p3bis_v2.sh`
  (`029bdb5c114a6166a21fa93724d71a2bf6158dc9686993424f6fbe8462352b08`) ; »
- Nouveau : la citation reste telle quelle, et **c'est de nouveau ce lanceur qui est joué** (R2) ; il n'est plus « lu
  sous l'écart 1 » (A2 l. 296-297).

## Addendum 1, lu sous l'écart 3

- **A1 l. 46-51** (règle neuve) et **l. 53-58** (table des lectures, lignes 1937 et 2151) : **retirées** (R2). Les
  lignes 1128 et 2285 de la même table restent lues comme A1 les lit (historique ; information).
- **A1 l. 164-172**, conditions d'emploi 1 à 4 : **sans objet** pour la course désormais (le lanceur d'écart n'est plus
  joué). La condition 4 (l. 171-172) est celle qui joue : mot contraire de Lazar, retour à la garde scellée.
- **A1 l. 176-177**, réserve au verdict « garde du crédit levée par écart, R-2399 » : **reste**, et vaut pour les
  créations faites sous l'écart 1 (60286945, 60370121, 60432755).
- **A1 l. 178-185**, risque résiduel : réalisé le 13 novembre (R-2491) ; les règles qu'il cite ont joué telles quelles
  (instance vue arrêtée deux fois, arrêt par l'identifiant, R-2489 ; nœud de Lazar, R-2490 à R-2492 ; dépense bornée).

## Addendum 2, lu sous l'écart 3

L'addendum 2 **reste en vigueur** (D1 téléchargement, D2 contrôle à cinq minutes ; leurs pièces sont appelées par v6
avec les mêmes épingles). Ce qui se lit autrement :
- **A2 l. 453-461, « Fixés pour la course »** :
  - Enchaîneur : `enchaineur_p3bis_v6.sh` (`1b49b701…`) au lieu de v5, seul outil de lancement de la course ;
  - Lanceur : `lancer_p3bis_v2.sh` (`029bdb5c…`) au lieu du lanceur d'écart 1, appelé par v6, qui en épingle
    l'empreinte ;
  - Contrôle, surveillance, module : inchangés (les trois pièces d'écart 2) ;
  - Branche : `prep/p3bis-ecart3-v1`, commit `02017d3252eca3c76c0a815e1124a023909aa96b`, ou un commit postérieur de cette branche qui n'ajoute
    que des fichiers **hors** du dossier de la chaîne (à vérifier par `git diff --name-status 02017d3252eca3c76c0a815e1124a023909aa96b <commit>` :
    ajouts seulement, aucun sous `docs/procedures/P3-bis-temoin-positif-v1/`).
- **A2 l. 296-297** (P5 : « Le lanceur cité l. 2174-2175 (`029bdb5c…`) se lit déjà sous l'écart 1 ») : se lit « est joué
  tel quel » (Q7).
- **A2 l. 302-304** (P6) : « cinquième argument de `enchaineur_p3bis_v5.sh` » se lit `enchaineur_p3bis_v6.sh`.
- **A2 l. 311-318** (P7) : s'ajoutent, sous l'écart 3, sous `docs/procedures/P3-bis-temoin-positif-v1/` seulement :
  `enchaineur_p3bis_v6.sh`, le banc `essais_ecart3_p3bis_v1.sh` et ses sorties.
- **A2 l. 351-357** (lecture de A1 l. 167-169) : l'arbre exigé est celui de la branche `prep/p3bis-ecart3-v1`, qui porte
  les branches des écarts 1 et 2 ; « le lanceur d'origine ne [sont] toujours jamais joué[s] pour une création » est
  **renversé** pour le lanceur d'origine, qui est joué ; le lanceur v1 et le lanceur d'écart 1 v2 ne le sont jamais.
- **A2 l. 358-359** (conditions 1, 3 et 4 de A1 « ne changent pas ») : retirées avec l'écart 1.
- **A2 l. 361-385**, lignes d'information de `lancement.txt` : le lanceur d'origine écrit les mêmes deux lignes (le
  lanceur d'écart 1 en était la copie, A1 l. 86-87 et 116) ; elles se lisent comme A2 le dit. Le lanceur d'origine n'écrit plus la
  ligne fixe d'écart 1 (cas E6-01c).
- **A2 l. 514-516** (préalable 5) : empreintes à vérifier : `enchaineur_p3bis_v6.sh` et `lancer_p3bis_v2.sh` (préalable 6
  ci-dessous).
- **A2 l. 517-519** (préalable 6) : extraction de `prep/p3bis-ecart3-v1` (préalable 7 ci-dessous).
- **A2 l. 520-522** (préalable 7, « crédit présent > 0 et recharge automatique (A1) ») : remplacé par la garde
  d'origine (R2) et la recharge par Lazar (préalable 2).
- **A2 l. 526-535**, condition d'emploi 1 : les trois cas où l'enchaîneur finit après une création sans surveillance sont
  les mêmes ; lignes de v6 : code 4 du lanceur l. 65-68 ; traces illisibles l. 69-74 ; empreinte autre avant la
  surveillance l. 87-90.
- **A2 l. 536-546**, conditions d'emploi 2 (contrôle bloqué) et 3 (destruction après la surveillance d'écart) :
  inchangées.
- **A2 l. 552-554**, réserve au verdict « écart 2 (…), R-2450 » : **reste**.

## Ce qui ne change pas

- Le cœur de l'expérience : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture
  gelés.
- Toute la liste d'arrêt, hors les lectures Q1 à Q6 : contrôles avant dépense, bornes de l'offre, **liste fermée des
  instances**, GO, borne de création du 18 novembre 2026, révocations, processus mort, motifs de fin de la surveillance,
  second paquet, garde d'ouverture.
- Le **plafond de 80 USD** (sous GO-2026-11-02-29 et GO-2026-11-10-02 ensemble), sa projection et l'arrêt par
  l'identifiant ; le GO (GO-2026-11-10-02, échéance le 23 novembre 2026, `registres/go.md` l. 292) ; la date du rendez-vous
  (2026-11-20T12:00:00Z, l. 1999-2000) ; la ligne unique `SCELLEMENT-P3BIS` (l. 2009-2011).
- **Le code cité** : l'écart 3 n'ajoute que des fichiers sous `docs/procedures/P3-bis-temoin-positif-v1/` et
  `brouillons/` ; aucun fichier existant n'est modifié (section « Pièces »).
- Les pièces non touchées : lanceur d'origine (joué tel quel), lanceur d'écart 1 v2 (non joué), enchaîneur v5 (non joué),
  contrôles avant dépense, contrôle, surveillance et module d'écart 2 et d'origine, récupération, destruction, scripts de
  l'instance et de l'amorce, configuration, consignes.
- L'addendum 2 entier, lu comme ci-dessus ; les réserves des écarts 1 et 2.

## Préalables du lancement

Avant la relance, dans cet ordre, chacun constaté avec l'heure relevée par `date -u` :
1. **Addendum 3 scellé** : contre-lecture faite par un lecteur neuf d'un autre modèle ; compagnon `.sha256` ; versé sur
   `main` et sur `prep/p3bis-ecart3-v1` ; entrée au registre des décisions.
2. **Recharge du compte de location par Lazar** (R-2492), au minimum de la garde plus le coût attendu de la course, plus
   la dette du solde. Calcul :
   - minimum de la garde au moment de la création : M = 20 + 10 × P USD, P étant la somme des prix de l'heure des
     instances nommées en marche (l. 1936-1937) ;
   - coût attendu de la course, haut de la fourchette : K = 7,5 USD (devis, l. 2465 : « ≈ 4,5 à 7,5 USD ») ;
   - dette : D = 0,93 USD (solde −0,93 USD à 07:30Z, R-2491) ;
   - recharge ≥ M + K + D, relevée au crédit présent juste avant le lancement ;
   - **sans autre instance en marche (P = 0)** : 20 + 7,5 + 0,93 = **28,43 USD** ;
   - **avec 60417353 relancée et nommée (P = 1,342, prix de R-2491)** : 20 + 13,42 + 7,5 + 0,93 = **41,85 USD** ;
   - variante prudente, pire cas d'une tentative au lieu de l'attendu (K = 22,2 USD, l. 2467), avec 60417353 :
     20 + 13,42 + 22,2 + 0,93 = **56,55 USD**.

   La garde n'est lue qu'à la création : d'autres instances du compte consomment le crédit entre la recharge et le
   lancement, puis pendant la course. La session relit le crédit (lecture seule) juste avant le lancement et l'écrit au
   registre ; le lanceur refuse lui-même sous le minimum (code 3, cas E6-02, E6-04, E6-06).
3. **Instances du compte** (liste fermée, l. 1937-1940 ; module commun, sous-commande `instances`) : 60432755 détruite
   (R-2493) ; **60417353** (témoin Bailey, autre session, arrêtée le 13 novembre faute de crédit, R-2491) ferait refuser
   toute création tant qu'elle reste arrêtée sur le compte (cas E6-08) : elle doit être soit relancée par sa session et
   nommée en `EN_MARCHE` avec le GO de sa course (son prix entre alors dans M), soit détruite par sa session ou par Lazar.
   Ce choix n'appartient ni à la chaîne ni à cet addendum. Inventaire relu juste avant le lancement.
4. **Dépense antérieure relevée** au registre des dépenses, puis passée en cinquième argument de l'enchaîneur v6. Règles
   de A2 l. 508-512 (stockage 0,08 USD de l'heure faute de facture ; majorant compté tant qu'une facture ne le remplace pas ;
   arrondi au centime supérieur). Calcul indicatif du rédacteur, sur les registres cités, à refaire par la session :
   - 60286945 : 0,220 USD (facture, `registres/depenses.md` l. 434) ;
   - 60370121 : 0,458 USD (facture, l. 433) ;
   - 60432755 : calcul 3,11 USD et majorant de téléchargement 2,00 USD (l. 436), plus le stockage de 04:23:42Z (dernier
     relevé où elle tournait, R-2489 ; borne prudente) à la destruction, 07:48:11Z (`registres/arrets.md` l. 110) :
     12 269 s × 0,08 / 3 600 ≈ 0,273 USD ;
   - total ≈ 0,220 + 0,458 + 3,11 + 2,00 + 0,273 = 6,061, soit **6,07 USD** au centime supérieur. La facture de
     60432755, si elle est lisible, remplace le majorant et le stockage estimé.
5. **Rien de poussé, rien de lu** (R1 (ii) et (iii)) : constat de R-2489 et R-2490 relu au registre ; la tête de
   `calcul/p3bis-reel-v1` relue égale à S juste avant le lancement, par son empreinte seule (`git ls-remote`, sans
   `fetch` ni extraction) ; aucun fichier d'issue de P3-bis au dépôt.
6. **Empreintes vérifiées par la session**, écrites avec l'heure : `enchaineur_p3bis_v6.sh` égal à
   `1b49b701253b89fd42cad589097f700697dd38de0a178b1fadda168dbd7f521f` (il ne vérifie pas la sienne) ;
   `lancer_p3bis_v2.sh` égal à `029bdb5c…` (v6 le vérifie aussi). Toute empreinte autre : aucun lancement.
7. **Jeu depuis le dossier de la chaîne d'une extraction de la branche** `prep/p3bis-ecart3-v1` (commit ci-dessus), où les
   scripts d'origine sont égaux à S (le bloc 2 du lanceur l'exige) ; dossier neuf inexistant (R12) ; `HF_TOKEN` exporté ;
   détaché par `setsid nohup`, PID noté, arrêt seulement par ce PID (R10).
8. **Refspec restreint du clone local de lancement, comme R-2463** : le lanceur d'origine fait
   `git -C /home/user/controle-ia-travail fetch -q origin` sans refspec (`lancer_p3bis_v2.sh` l. 88 et 92, mêmes lignes que
   le lanceur d'écart 1, l. 105 et 109) ; le refspec par défaut de ce clone est restreint à `main` et
   `prep/p3bis-ecart3-v1` (branches nommées, jamais un motif), pour qu'aucune branche interdite, dont
   `calcul/p3bis-reel-v1`, ne soit rapatriée. Aucun script, aucune empreinte, aucun argument ne change.
9. **Conditions du texte, inchangées** : date du jour au plus tard le 18 novembre 2026 ; GO-2026-11-10-02 non révoqué ;
   `EN_MARCHE` relevé juste avant ; **N = 2** ; branche `calcul/p3bis-reel-v2` absente du distant (le lanceur le vérifie).

## Conditions d'emploi

1. Seul outil de lancement : `enchaineur_p3bis_v6.sh`. L'enchaîneur v5 et le lanceur d'écart 1 ne sont plus joués pour
   cette course.
2. Les conditions d'emploi 1 à 3 de A2 (l. 526-546) valent, aux lignes de v6 dites plus haut.
3. L'écart 3 vaut pour la seule relance N = 2 (R1, « Portée »), dans la borne de création de l'en-tête.
4. Tout mot contraire de Lazar suspend l'écart : retour aux pièces scellées, ou nœud.

## Réserves au verdict et risque résiduel

- **Réserves écrites au verdict de P3-bis**, transmises au lecteur R13, **à côté de celles des écarts 1 et 2**
  (« garde du crédit levée par écart, R-2399 », A1 l. 176 ; « écart 2 (dépense de téléchargement, fenêtre du contrôle à
  cinq minutes), R-2450 », A2 l. 552-554) :
  - « **écart 3 (relance après épisodes joués, arrêt par épuisement du crédit), R-2492** » ;
  - « **recharge automatique non tenue (écart 1)** ».

  Elles valent pour toute la course dès la première création faite par l'enchaîneur v6.
- **Risque résiduel** :
  - **épuisement du crédit pendant la course** : la garde n'est lue qu'à la création. Des instances d'autres courses
    peuvent démarrer après la création, sans être nommées, et consommer le crédit. La marge M + K + D du préalable 2 le
    borne sans l'exclure. S'il se réalise : arrêt vu par la surveillance (ÉTAT TERMINAL), nœud de Lazar ; l'écart 3 ne
    couvre pas une seconde relance ;
  - **relance à l'aveugle d'une course déjà jouée en partie** : les 19 lots de 60432755 ne sont ni récupérés ni lus ;
    aucune information n'en sort qui puisse orienter la relance (R1 (iii)). La relance rejoue les mêmes graines : elle
    reproduit la course, elle n'en tire pas une seconde ;
  - **cause de l'arrêt « probable »** : R-2491 établit l'épuisement par le solde, la consommation et l'heure ; le loueur
    n'a rendu aucune raison d'arrêt (R-2490). La condition (i) repose sur ce constat du registre ;
  - **dépense antérieure** : saisie par la session ; l'enchaîneur n'en vérifie que la forme (A2 l. 568).

  La surveillance, le plafond de 80 USD, la liste d'arrêt et la règle de relance s'appliquent tels quels. L'écart ne
  relâche aucune autre règle.

## Pièces, par chemin et empreinte

Branche `prep/p3bis-ecart3-v1`, commit **`02017d3252eca3c76c0a815e1124a023909aa96b`** (commit du code), premier commit au-dessus de
`444645bbde329e05a5738e9a40a8ad48c8c28eb4` ; le commit suivant de la branche n'ajoute que ce brouillon et son compagnon,
sous `brouillons/`. Tout sous `docs/procedures/P3-bis-temoin-positif-v1/`, chaque fichier scellé
par son compagnon `.sha256` :

| Pièce | sha256 | Rôle |
|---|---|---|
| `enchaineur_p3bis_v6.sh` | `1b49b701253b89fd42cad589097f700697dd38de0a178b1fadda168dbd7f521f` | enchaîneur détaché v6 (R3) |
| `essais_ecart3_p3bis_v1.sh` | `56659e9d498ade34b9d00578433f2eb0f00bea1184de25fd9aebb1e878d6bf81` | banc des essais R5 |
| `essais-ecart3-p3bis-v1.log` | `06e2aeca127f4c886d3fd891e141623097a84eebc21fddc7823d269981d8436a` | journal du passage final, 2026-11-13T08:03:54Z → 08:09:55Z, 71 cas, 0 non conforme |
| `rapport-developpeur-p3bis-ecart3-v1.md` | `e0ecb1322439b47cbaccb9fb2edfa461c62c1deddcf2ce62952a34a71af269d1` | rapport du développeur |
| `sorties-essais-ecart3-v1/enchaineur-E6-01-sain-relance-2.txt` | `b5393d377bc036c163b669aa31a02eebba15e828c71e57e418c167bc48f3192a` | journal de v6, cas sain |
| `sorties-essais-ecart3-v1/lancement-E6-01-sain-relance-2.txt` | `790e5a6fbc04f9d2248162b22aaf71b7067a06e4d80bd2c1cccae5b1f6b27ed2` | `lancement.txt` du cas sain (garde d'origine, branche v2) |
| `sorties-essais-ecart3-v1/console-lanceur-E6-04-credit-7-05.txt` | `0dca705a47abb17867f90c7a7888e589d01a33856bb693b0f8f0d5e29abb2f63` | refus à 7,05 USD |
| `sorties-essais-ecart3-v1/lancement-E6-04T-temoin-v5-ecart1-credit-7-05.txt` | `8e6988c6a592c33e142f180cbe7fc7856373aeb6ea406767edc679ed80e7141b` | témoin : v5 et l'écart 1 créent à 7,05 USD |
| `sorties-essais-ecart3-v1/console-E6-11-lanceur-modifie.txt` | `2315589397ccb04d83eb4bf1a081d67aa7b71358d468d7af7b529fb3a8d36717` | refus de v6, lanceur modifié |
| `sorties-essais-ecart3-v1/console-lanceur-E6-12-epingle-contournee.txt` | `a6029606ea041ad24b6d3c1e423c92e3d1fa8fcf005be5b0bc1415e997e772f5` | refus du lanceur lui-même, épingle contournée |
| `sorties-essais-ecart3-v1/console-lanceur-E6-14-relance-2-sans-branche-v1.txt` | `3bb7024c0ce874afb0363eb7f9f39bfa484a97039cc0b4a53d247cf73518839d` | refus, N = 2 sans la branche v1 au distant |

Relevé `git diff --name-status 444645bb 02017d3252eca3c76c0a815e1124a023909aa96b` : 22 ajouts (onze fichiers et leurs compagnons), tous sous `docs/procedures/P3-bis-temoin-positif-v1/`, aucun fichier modifié ; `git diff --name-status 8f8df8b2 02017d32 -- scripts src tests prereg` ne montre que les addendums 1 et 2 et leurs compagnons (ajouts).
