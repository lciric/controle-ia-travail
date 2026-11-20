# Reste net comptable par clé d'appel aux modèles, au 2026-11-20 — v1

- Auteur : comptable, modèle O (agent neuf, demande de la session mère de 12:14Z, R-4249 point 3).
- **Ceci est une estimation, pas un relevé.** Aucun solde n'est lisible par programme (R-3222, R-4249) ; aucune clé n'a été lue ni appelée ; aucune dépense. Chaque reste ci-dessous est « dernière borne ou dernier relevé connu, moins les dépenses inscrites depuis ». Seul un relevé de facturation de Lazar fait foi.
- Sources, tirées de `origin/main` au commit `7f93401a9` (fetch du 2026-11-20 vers 12:20Z) :
  - `registres/depenses.md` (`32ca82cebe55e7b7d95a1549431717490fbd151ff2e748cf0138dc48c383ca10`) ;
  - `registres/go.md` (`ab26e18cc9fd0a9ad08a78a7c15a5cd20dd85db9f1fae0b5c83de758bb30b58d`) ;
  - `registres/decisions.md` jusqu'à R-4249 (`c4334526eec2b974128bd4b78385e5dcd3e92731190d0039ace6f1a0b2ae55d2`). Relu ensuite au commit `81950c45` : seules R-4250 à R-4252 s'ajoutent, sans montant ni relevé ; les deux autres registres sont inchangés.
  - Pour les engagements : devis v4 de la course « nouvelles attaques » (`docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v5/devis-course-nouvelles-attaques-v4.md`, `620de3692d3454f08d32832ca471551bb9a8439f80122b716b13474d9a6d363e`, scellé R-4206) ; devis v3 du collisionneur sur les modes de sabotage et les attaques (`docs/notes/collisionneur-modes-et-attaques-v1/devis-collisionneur-modes-et-attaques-v3.md`, `fadb7d09caedc49bbcd1b6ed24effc5e902b59200183164e3d2879e8a5449bf5`) ; devis v7 de l'étage payant de la ligne 3 (`prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md`, `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`).
- Sommes faites par programme : `calcul/somme_reste_net_v1.py` (`6d2ec3116e721967135450c15cb9ff79fb26ae0d2d2b0e20e4f63a4196f1e3c4`), sortie `calcul/sortie-somme-reste-net-v1.json` (`4841c6a2a54e5e76058b43f1e1916420f919ab4003a8ad3609720aed1aab8467`), dans ce même dossier. « l. N » renvoie à la ligne N de `registres/depenses.md` à ce commit.

## Tableau résumé

| clé (nom de variable) | dernière borne ou relevé | dépenses inscrites depuis | reste net estimé | incertitude principale |
|---|---|---|---|---|
| Claude « Minuit » (`RR_ANTHROPIC_API_KEY_MINUIT`) | 200 USD déclarés par Lazar, 18 nov vers 06:59Z (R-3228) | 37,44 USD | **162,56 USD** | usage non inscrit d'une autre session non exclu (variable commune, R-3754) |
| Claude « Luc » (`RR_ANTHROPIC_API_KEY_LUC`) | 214 USD dits par Lazar, 20 nov vers 05:02Z (R-4088, heure R-4093) | 0,000002 USD | **214,00 USD** | le chiffre de Lazar est-il un solde lu ou un souvenir ? |
| Claude « Rigaud » (`RR_ANTHROPIC_API_KEY_RIGAUD`) | 124 USD déclarés par Lazar, 18 nov vers 06:49Z (R-3224) | 76,50 (lecture du registre) ou 59,79 (lecture corrigée) | **≈ 47,50 (registre) à ≈ 64,21 (corrigée)**, avant deux lots en cours d'au plus 45 USD ; **après ces lots : ≈ 2,50 à ≈ 19,21** | erreur probable de 17,64 USD dans le compte de R-3611 ; lots de R-4170 non chiffrés ; recharge de GO-2026-11-20-34 faite ou non, montant inconnu |
| Kimi, Moonshot (`KIMI_API_KEY`) | solde **lu** 32,24463 USD, 18 nov 09:21Z (R-3277, l. 512) | aucune | **≈ 32,24 USD** | rien depuis deux jours ; seul relevé lu par programme du lot |
| OpenAI, Astra (secret réseau de `OPENAI_API_KEY_2`) | 30 USD « crédités », mot de Lazar rapporté, 18 nov 18:06Z (R-3356) | 18,49 USD (≤ 21,09 avec deux appels coupés) | **≈ 11,51 USD (≈ 8,91 au bas)** | mot rapporté, non relu ; quelle clé paie dans l'environnement du nouveau compte de la mère ; recharge automatique (R-2822) éventuelle |
| Google, Argon et Carbon (`GEMINI_API_KEY`) | **aucune borne ni relevé** (R-3222) | 61,90 USD comptés depuis le 18 nov (+ ≤ 1 d'appels coupés), pour information | **inconnu** | aucun solde, aucune borne ; le compte a déjà rendu « crédit épuisé » (HTTP 402) le 24 octobre |
| Autres clés Claude (`RR_ANTHROPIC_API_KEY`, `_2`, `_3`) | aucun relevé | — | inconnu, hors usage (R-2037) | — |

Total Claude des trois clés en usage, avant les lots de Rigaud : **≈ 424,06 USD** (lecture du registre) ou **≈ 440,77 USD** (lecture corrigée). La borne retenue par GO-2026-11-20-16 et -22 est 423,56 USD (Rigaud arrondi à 47).

## 1. Par clé

### 1.1 Claude « Minuit »

- Borne : 200 USD déclarés (R-3228 ; « Minuit » 200 USD, R-3339 : « vient de recevoir 200 dollars sur une clé autre que rigaud »).
- Dépenses comptées depuis : vérification de la clé 0,000108 (l. 528, GO-2026-11-19-06, R-3617) ; épreuve des témoins v9, part Minuit 0,980399 (l. 532, GO-2026-11-19-20) ; course d'auto-conception v9, part Claude 36,457056 (l. 536, GO-2026-11-19-19). Somme 37,437563.
- **Reste net : 162,562437 USD**, égal au chiffre de R-4082 et du devis v4 (§ 6). Aucune ligne postérieure sur Minuit dans les deux registres.
- Incertitude : R-3754 — la variable est commune à l'environnement par défaut ; un usage non inscrit par une autre session n'est pas exclu. La course d'affinage des idées des mentors (GO-2026-11-18-14, 150 USD, échéance 25 nov), réservée jadis à Minuit, n'a jamais été jouée (R-3616).

### 1.2 Claude « Luc »

- Borne : 214 USD, réponse de Lazar à la question sur le solde (R-4088, heure corrigée par R-4093 : vers 05:02Z).
- Dépense depuis : sonde 0,000002 (l. 548, GO-2026-11-20-13, R-4091), faite après le mot.
- **Reste net : 213,999998 USD.**
- Incertitude : la règle de R-2037 (« jamais _LUC ») n'a été levée que pour la course « nouvelles attaques » (GO-2026-11-20-12) ; aucun autre usage n'est inscrit. Il n'est pas écrit si « 214 » est un solde lu à la console ou un chiffre de mémoire.

### 1.3 Claude « Rigaud »

- Borne : 124 USD déclarés par Lazar (R-3224, « on a 124 doollars de credits claude sur la cle rigaud »). Les dépenses sur Rigaud antérieures (crédits du 12 novembre) sont absorbées par cette déclaration.
- Chaîne inscrite :
  - bornes hautes jusqu'au 18 nov 15:58Z (R-3304 : 6,48) et témoins v4 (R-3342 : 0,999689) : 7,479689 ;
  - course d'auto-conception v4, part Claude : 24,789486 (l. 522) ; cumul 32,269175, égal au compte de R-3479 ;
  - témoins v6 : 0,972429 (l. 525) ; reste 90,76, égal à R-3554 ;
  - course d'auto-conception v6, part Claude : 24,716609 (l. 526).
  - Somme de la chaîne : **57,958213**.
- Le compte de l'organisme, repris par R-3611, écrit « ≈ 75,6 déjà comptés ». L'écart à la chaîne vaut 17,641787. **Lecture du comptable, à confirmer** : 32,269175 + 0,972429 + 42,36 = 75,601604, c'est-à-dire que la course v6 a été comptée entière (42,36), part hors Claude comprise ; or l. 526 dit que 17,64 de ces 42,36 sont Google et OpenAI. Si c'est le cas, Rigaud porte ≈ 17,64 USD de plus que le registre ne le dit.
- Depuis R-3611 : vérification de la clé dans la relance 0,0000015 (l. 534) ; essai de mesure du bras A, file Claude 0,904303 (l. 546).
- Non attribué par la chaîne : « Raisons ou regard ? », appels Opus 4.6 sur Rigaud, 0,93 (R-3536, 18 nov 23:45Z), ni dans les 6,48 de R-3304 ni dans les 75,6.
- **Reste net, deux lectures** :
  - A, lecture du registre (R-3611, R-4089, GO-2026-11-20-16) : 124 − 75,6 − 0,904 = **47,495696** ;
  - B, lecture corrigée (chaîne seule, 0,93 de « Raisons ou regard ? » ajoutés) : **64,207482**.
- **En cours** : R-4170 (20 nov 08:38Z) — « deux lots en cours sur la clé Rigaud (au plus 45 USD) ». Le registre ne dit ni à quelle session ils appartiennent, ni s'ils sont finis, ni ce qu'ils ont coûté. Ils sont nommés dans la même ligne que la passation de « Raisons ou regard ? » ; c'est une lecture, non un fait établi. Après ces lots au plus : **A ≈ 2,50 ; B ≈ 19,21**. Après la réserve de 8,35 du bras A en plus : **A ≈ −5,85 ; B ≈ 10,86**.
- **Recharge** : GO-2026-11-20-34 (vers 08:47Z) dit que Lazar recharge Rigaud ; GO-2026-11-20-49 (vers 12:14Z) arrête toute recharge « jusqu'à nouvel ordre ». Aucun registre ne dit si la recharge a été faite entre les deux, ni son montant (le devis v4, § 6, et le devis du collisionneur, § 4, l'attendent encore). Tout ce qui précède est **avant recharge**.

### 1.4 Kimi (Moonshot)

- Relevé : solde **lu sur le compte** à 32,25354 puis 32,24463 USD, 18 nov vers 09:21Z (R-3277, l. 512). C'est le seul solde lu par programme de ce lot.
- Dépenses depuis : aucune ligne (la course v9 n'avait pas de proposeur Kimi, R-4085 ; Kimi refusé dans l'affinage v7, R-3339).
- **Reste net : ≈ 32,24 USD.**
- Incertitude : deux jours sans relevé ; Moonshot permet de relire le solde (R-3222).

### 1.5 OpenAI (Astra)

- Borne : un secret réseau pour l'interface d'OpenAI, avec la variable `OPENAI_API_KEY_2`, « créditée de 30 USD selon le mot de Lazar rapporté », remplace la clé de **toutes** les requêtes vers OpenAI des sessions de cet environnement (R-3356, 18 nov 18:06Z).
- Dépenses depuis (somme 18,49368) : course v4, Astra 7,30824 (l. 522 ; course de 17:19 à 19:30Z, comptée entière, une part a pu passer sur l'ancienne clé) ; bras du juge d'Astra 0,2903 (l. 521, 18:32Z) ; second bras 0,3979 (l. 524) ; course v6, OpenAI 4,80336 (l. 526) ; sonde d'Astra 0,00041 (l. 532) ; course v9, Astra 4,74571 (l. 536) ; bras A, file GPT 0,48776 (l. 537, compteur) ; revendication 14, Astra 0,46 (l. 550).
- Deux appels coupés de la revendication 14 : facturation inconnue, au pire ≈ 2,6 (R-4204).
- **Reste net : ≈ 11,51 USD ; ≈ 8,91 si les appels coupés sont facturés.**
- Incertitudes : le 30 est un mot rapporté par la relance, non relu à la source ; la mère est passée sur un autre compte le 20 vers 10:07Z (R-4175) — que le secret réseau s'applique aussi dans l'environnement de ce compte n'est pas écrit ; le compte OpenAI d'origine « se recharge seul » (R-2822, 14 nov) — si la recharge automatique vaut aussi pour cette clé, elle contredit GO-2026-11-20-49, et le reste serait autre.

### 1.6 Google (Argon et Carbon, une seule clé)

- Aucune borne, aucun relevé : « aucun appel de solde connu chez Google » (R-3222). Le compte a rendu « crédit épuisé » (HTTP 402) le 24 octobre (état du 24-25 octobre), donc il fonctionne sur crédit ; son montant n'est écrit nulle part.
- Pour information, dépenses Google comptées depuis le 18 nov : **61,90 USD** (témoins v3 et v4 0,34 ; course v4 12,68 ; témoins v6 0,21 ; course v6 12,84 ; sonde de Carbon 1,36 ; témoins v9 0,20 ; course v9 31,30 ; bras A, file Carbon 0,60 ; revendication 14 0,43 ; « Raisons ou regard ? », Gemini 1,95), plus ≤ 1 d'appels coupés (R-4204), plus les parts Google mêlées des courses de la relance du 18 au matin (≤ ≈ 6, non séparées).
- **Reste net : inconnu.**

## 2. Engagements en attente, par clé

### 2.1 Course « nouvelles attaques » (organisme d'idéation, six espèces)

Devis v4 scellé (R-4206) ; ligne demandée **570 USD**, plafond total 576,01 (témoins 5, sonde de refus des espèces 1 à 5 : 1, sonde de Kimi 0,01). Accord en vigueur : 450 USD (GO-2026-11-20-08) ; la ligne de 570 attend le mot de Lazar ; à recalibrer sur les soldes (R-4248). Répartition Claude de GO-2026-11-20-22. Parts sur la course (devis v4, § 3 et § 6) :

| clé | rôle | bas | haut | borne ou pire |
|---|---|---|---|---|
| Minuit | juge de l'espèce 3 | 24,70 | 126,06 | part = 162,56 |
| Luc | aiguilleur, proposeur de l'espèce 4 | 69,26 | 136,63 | part = 214 |
| Rigaud | proposeur de l'espèce 3 | 22,29 | 26,61 | part = solde relu − 8,35 ; pire du rôle 199,65 |
| Google (relais 2) | juge et proposeur de l'espèce 1, proposeur de l'espèce 5 | 95,35 | 147,77 | 570 (ligne) |
| OpenAI (relais 3) | proposeur de l'espèce 2 | 14,25 | 17,01 | 199,65 |
| Kimi (relais 4) | proposeur de l'espèce 6, coût non mesuré (règles du rédacteur) | 35,19 | 88,55 | 199,65 (+ 0,01 de sonde) |

L'épreuve des témoins (5) et la sonde de refus (1) ne sont pas attribuées à une clé dans le devis ; à la course v9, les témoins sont passés sur Minuit (0,98) et Argon.

### 2.2 Collisionneur, questions « modes de sabotage » et « attaques »

Devis v3 (`fadb7d09…`), base à cinq espèces avec Kimi (GO-2026-11-20-31) ; plafond demandé **52,16 USD** (48,13 sans Kimi) ; aucune dépense avant le mot sur le devis (GO-2026-11-20-36 (4)) ; version neuve du script en cours (R-4208, R-4251).

| clé | espèce | bas | haut | pire (deux questions) |
|---|---|---|---|---|
| Rigaud | Fable 5.1 | 6,00 | 8,42 | 29,43 |
| Google | Carbon et Argon | 9,40 | 22,19 | 48,58 + épreuve de Carbon 2,16 |
| OpenAI | Astra | 2,66 | 4,22 | 15,63 |
| Kimi | Kimi | 1,22 | 2,28 | 6,58 |

Le collisionneur sur le papier « dopamine » (GO-2026-11-20-45, six espèces dont Opus 5.5 et Fable 5.2) n'a pas de devis inscrit ; non chiffré ici.

### 2.3 Ligne 3, étage 2 à 200 témoins

GO-2026-11-20-26 : au plus 88,36 USD (cas haut 44,78) ; juge Opus « payé par la clé qui aura du crédit au relevé du départ » (GO-2026-11-20-49) ; aucun appel payant avant que Lazar dise l'état des clés (R-4246). Le devis v7 (§ 6) ne donne la part par clé qu'à 100 témoins (Claude 10,84 / 14,75 / 29,10 ; Argon 5,69 / 7,74 / 15,27) ; **à 200, extrapolation du comptable à la même proportion** :

| clé | estimation | haut | pire |
|---|---|---|---|
| clé Claude à désigner (juge Opus) | 21,58 | 29,37 | 57,95 |
| Google (juge Argon) | 11,32 | 15,41 | 30,41 |

### 2.4 Clé Rigaud : lots et réserves

- Deux lots en cours, au plus 45 USD (R-4170, 08:38Z) ; propriétaire, fin et coût non inscrits.
- Réserve de l'essai de mesure du bras A : **8,35 USD** (GO-2026-11-20-22 ; 9,25 − 0,904 de GO-2026-11-19-34, dont l'échéance était le 20 nov).
- Bras A, course de lecture : devis non écrit ; part Claude sur Rigaud éventuelle, non chiffrée (GO-2026-11-20-16 : « à garder pour le bras A selon son devis »).

### 2.5 Autres lignes de GO ouvertes qui touchent ces clés

| ligne | plafond, échéance | clé | état lu dans les registres |
|---|---|---|---|
| GO-2026-11-18-14, affinage des idées des mentors | 150 USD, 25 nov | Minuit à l'origine | jamais jouée ; « sur le reste ou sur une recharge » (R-3616) |
| GO-2026-11-12-01 à -05, « crédits de Claude » (juge-tournoi 235 ; oracle de couverture, lecteur Opus, clé Rigaud 45 ; contre-lectures 70 ; collisionneur 40 ; mondes plantés 45) | 30 nov | Rigaud (crédits du 12 nov) | ouvertes nominalement ; seul le collisionneur (-04) a des dépenses, toutes avant la déclaration des 124 USD. Aucun engagement courant n'est inscrit ; je ne les compte pas, mais elles ne sont pas closes |
| GO-2026-11-18-16 (commun 34 USD avec -11, -19, -22, -23, -31, -32, -33, -54) et -17 (Kimi, 11,3) | 22 nov | Claude, Google, OpenAI, Kimi | ≈ 11,9 consommés sur 34 ; lignée Kimi épuisée (R-3277, R-3444) ; aucune course annoncée |
| GO-2026-11-18-27, appels hors Claude et loueur | 80 EUR, 22 nov | Google, OpenAI, Moonshot | enveloppe de budget, pas une borne de clé |
| GO-2026-11-19-66, ligne 3 étage payant | 25 USD, 27 nov | Claude et Google | remplacé pour l'étage 2 par GO-2026-11-20-26 ; aucune dépense inscrite |
| GO-2026-11-20-37, revendication 14 | 10 USD, 22 nov | Google, OpenAI | 0,89 dépensés + ≤ 3,6 d'appels coupés ; fait |
| GO-2026-11-20-43, -48, bras A (second lecteur Mistral ou DeepSeek ; juge des ancres gpt-6.2-sol, 152 appels au plus) | aucune dépense avant devis, 30 nov | clés neuves (Mistral, DeepSeek) ; OpenAI pour gpt-6.2-sol | non chiffré ; le bras A tiendra un registre propre pour ses clés neuves (R-4252) |

Le crédit du loueur de cartes (5,25 USD à 12:14Z, R-4249) n'est pas une clé d'appel aux modèles ; hors de ce relevé.

## 3. Ce qui tient et ce qui ne tient pas (sans trancher)

Les verdicts suivants sont mécaniques (sortie du programme, section `verifications`) ; ils supposent les restes estimés ci-dessus.

**Tient**
- Minuit : la part haute de la course « nouvelles attaques » (126,06) tient (marge 36,50). Avec en plus le juge Opus de l'étage 2 au cas haut (29,37) : tient de justesse (marge 7,13).
- Luc : la part haute de la course (136,63) plus le juge Opus de l'étage 2 au cas haut : tient (marge 48,00).
- Rigaud, **si les deux lots de R-4170 n'ont rien coûté** : réserve de 8,35 et part haute de la course (26,61) tiennent en lecture A (marge 12,54) ; avec en plus le collisionneur au cas haut (8,42), soit 43,38 : tient en lecture B (marge 20,83) et, de justesse, en lecture A (marge 4,12).
- Kimi : le collisionneur seul (2,28 haut ; 6,58 pire) tient.
- OpenAI : le collisionneur seul (4,22 haut) tient, même si les appels coupés sont facturés (marge 4,69).

**Ne tient pas**
- Minuit ou Luc : la part bornée de la course (162,56 ou 214) **plus** le pire du juge Opus de l'étage 2 (57,95) sur la même clé ne tient pas (manque ≈ 57,95). La part bornée prend tout le reste ; le juge de l'étage 2 n'a de place que si la course coupe avant sa borne.
- Rigaud, **si les deux lots vont à 45** : la réserve de 8,35 et la part basse de la course (22,29) ne tiennent ni en lecture A (manque 28,14) ni en lecture B (manque 11,43). Avec la part haute et le collisionneur haut, lecture B : manque 24,17. Sans recharge, Rigaud ne porte pas tout ce qui lui est promis.
- Kimi : **même la part basse** de l'espèce 6 dans la course (35,19 + 0,01) dépasse le reste lu (32,24) : manque 2,96. Au cas haut, avec le collisionneur : manque 58,60. Réserve : le cas bas de l'espèce 6 est une règle du rédacteur (moyenne des cinq autres proposeurs), non une mesure ; au tarif noté de Kimi, le devis lui-même le dit « sans doute large ».
- OpenAI : **même la part basse** d'Astra dans la course (14,25) dépasse le reste estimé (11,51 ; 8,91 au bas) : manque 2,74 à 5,34. Au cas haut avec le collisionneur : manque 9,72.
- Total Claude au pire de la ligne : la ligne de 570 dépasse la borne des trois clés (415,21 avant recharge) de 154,79 (devis v4, § 6) ; l'arrêt nommé « part d'une clé épuisée » tient cet écart.

**Indécidable sur les registres**
- Google : aucun reste. La course demande 95,35 à 147,77 (pire : la ligne), le collisionneur 9,40 à 22,19 (pire 50,74), l'étage 2 11,32 à 30,41.
- Rigaud après recharge : montant et date inconnus.

## 4. Ce que seul un relevé vrai de Lazar peut dire

1. Le solde réel de Minuit, Luc et Rigaud à la console d'Anthropic (« 214 » est-il un solde lu ?) ; s'il y a des usages non inscrits (variables communes à l'environnement, R-3754).
2. Si la recharge de Rigaud (GO-2026-11-20-34) a été faite avant l'arrêt des recharges (GO-2026-11-20-49), et de combien.
3. Ce que sont les deux lots en cours sur Rigaud (R-4170), à qui ils appartiennent, s'ils sont finis et ce qu'ils ont coûté ; et si les 17,64 USD que je crois comptés à tort sur Rigaud (R-3611) l'ont été.
4. Le crédit réel de la clé OpenAI qui paie (seconde clé, 30 USD rapportés), si la recharge automatique y est active, et laquelle des clés OpenAI sert dans l'environnement du nouveau compte de la mère.
5. Le crédit ou la limite du compte Google (Argon, Carbon) : aucun chiffre n'existe dans les registres.
6. Le solde Moonshot du jour (lisible par la session qui tient `KIMI_API_KEY`, comme le 18).
7. Si la recharge automatique annoncée « sur toutes les clés » le 25 octobre (état, R-404) vaut encore, ce qui changerait le sens de « reste » pour chaque clé.
