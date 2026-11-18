# Devis de la course d'affinage des idées des mentors — v10 : plafond dur souple de l'étape « proposition » dit juste (non engagé)

- Écrit le 2026-11-18T22:56:24Z (`date -u +%FT%TZ`) par le modèle L', correctif v10 demandé par la session principale après la contre-lecture du correctif v9 (modèle K, `course-v9/contre-lecture-preenregistrement-course-affinage-mentors-v9.md`, `615ef93b…`, commit `74676380`, verdict « Scellable après corrections. »). **Version 10** (R12) : les devis v1 à v9 restent en place ; base : devis v9 (`devis-course-affinage-mentors-v9.md`, `23029a75acc7ab4ec2996b57e24c747d5216067c531da88f97dee0d25dbe567b`). Même composition (deux Claude, Argon, Astra, Carbon ; pas de Kimi), même configuration (v9, `e7378f89…`), même plafond d'arrêt (150 USD), même ligne de GO (GO-2026-11-18-14). Aucun appel ; aucun réseau.
- **Aucun chiffre du devis v9 ne change.** Ce qui change : le § 3 (constat 1 de la contre-lecture, majeur : le devis v9 annonçait un plafond dur de 60 USD qui couperait l'étape « proposition » ; ce mécanisme n'existe pas dans l'orchestrateur épinglé) et la table du § 3 (constat 3, mineur : le « haut » n'est pas une borne). Le § 3 bis est neuf ; il dit le mécanisme réel, vérifié dans le code de l'orchestrateur épinglé et rejoué avec sa vraie classe de budget.

## 1. Carbon : réglages, sortie retenue et pire cas d'un appel (inchangé depuis la v9)

Commande `commande_gemini_lot_v1.py` (`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`, épinglée, inchangée) : prix plein 8,3 et 41,5 USD par million, facteur du lot 0,5, **sortie maximale 32 768**, sortie minimale 4 096, **provision 28 672**, délai de lot 1 620 s, relevé toutes les 30 s, délai de requête 60 s (durée maximale 1 770 s, sous les 1 800 s de l'orchestrateur épinglé).

Garde avant envoi de la commande (l. 167-173), au prix plein, sous **3,00 USD** ; entrée gardée = caractères de la consigne servie / 3 × 1,05 (calcul du lanceur sur les seize fils ; recoupé en jouant hors réseau la vraie commande de `main`, essai `test_v9_arithmetique_recoupee_avec_la_vraie_commande_de_carbon`, porté en v10) :

| consigne servie | caractères | entrée gardée | **sortie retenue (demandée au fournisseur)** | pire cas minimal | **pire cas d'un appel, prix plein** | au prix du lot |
|---|---|---|---|---|---|---|
| fil le plus long | 7 478 | 2 618 | **32 768** | 1,3816 | **2,571489** | 1,285745 |
| fil le plus court | 4 250 | 1 488 | **32 768** | 1,3722 | **2,562110** | 1,281055 |

- **Sortie retenue : 32 768 jetons ≥ 24 500** (plus forte pensée observée 20 696 + plus forte réponse observée 3 410 = 24 106, arrondi) sur toutes les entrées : le lanceur le vérifie et refuse sinon.
- **Pire cas d'un appel de Carbon : 2,5715 USD au prix plein**, sous 3,00 ; c'est aussi ce que la commande rend sur un échec après la création du lot (codes 3, 5, 6, 7). Si la pensée compte dans la sortie maximale (documentation), la facture réelle d'un appel ne dépasse pas l'entrée + 32 768 jetons de sortie : 1,38 USD au prix plein, 0,69 au prix du lot ; la provision est alors une réserve de la garde.
- Une pensée au-delà de 28 672 jetons rend le code 7 (réponse refusée, pire cas compté) ; si pensée et réponse dépassent ensemble 32 768 jetons, la réponse est coupée (code 5).

## 2. Prix par appel (inchangé depuis la v9)

- Carbon, estimation : **0,4985 USD** (pensée 20 000, réponse 3 500, entrée 2 618, prix du lot ; la vraie commande rend 0,510575 avec les maxima observés exacts, écart d'arrondi de 0,19 USD sur seize appels, constat 7 de la contre-lecture v9) ; haut : **2,5715** (pire cas compté par la commande sur un échec).
- Claude, Argon, Astra : prix estimés et hauts du devis v6 inchangés (ils viennent des jetons, non du plafond). Le plafond de session de 3,00 USD élargit seulement ce qu'un appel **peut** coûter : Astra demande 32 768 jetons au plus, pire cas d'un appel 1,73 USD par la formule de sa commande (corps de 8 011 octets au plus) ; un proposeur Claude a un budget de session de 3,00 ; Argon remplit son plafond selon sa propre garde. Le coût de ces trois espèces **sous 3,00** n'est pas mesuré.

## 3. Totaux (composition déclarée, cinq espèces)

| poste | estimation | haut (convention mixte, **non une borne**) |
|---|---|---|
| proposeurs | 24,70 | 76,36 (59,21 + 16 × (2,5715 − 1,50)) |
| aiguilleur (première espèce Claude) | 4,96 | 21,12 |
| juges (première espèce Claude et Argon) | 11,47 | 31,24 |
| sous-total | **41,136** | 128,72 |
| marge de 10 % | 4,11 | 12,87 |
| **total** | **45,25** | **141,59** |

- **Le « haut » n'est pas une borne** (constat 3 de la contre-lecture v9). Il mélange deux conventions : Carbon y est compté au pire cas de sa commande (2,5715 USD par appel), les autres proposeurs aux hauts par jetons du devis v6 (0,400484 USD au plus pour un non-Claude), alors que leur plafond par appel est désormais 3,00 (Astra 1,73 au pire par la formule de sa commande, Argon et les sessions Claude jusqu'à 3,00). Une course peut donc dépenser au-delà du haut. **La borne est le pire cas : 150 USD**, plafond d'arrêt.
- **Estimation : 45,25 USD** (41,14 sans marge, inchangée depuis la v8) ; **haut : 141,59 USD** ; majoré de 25 % : 56,56 et 176,98.
- **Pire cas de la course : 150 USD** (plafond d'arrêt, S17, tenu par l'orchestrateur ; borne par les plafonds de session : 80 × 3,00 + 160 × 0,25 + 320 × 0,60 = 472 USD, au-dessus : seul le plafond d'arrêt borne).
- Base de l'écart au devis du manifeste de fin : 41,136 USD sans marge (inchangée).

## 3 bis. Plafonds des étapes : ce que fait l'orchestrateur épinglé (neuf en v10 ; remplace le dernier point du § 3 du devis v9)

Le devis v9 disait : « plafond dur de l'étape « proposition » : 60 USD ; le haut de la proposition (76,36) le dépasse ; l'orchestrateur coupe l'étape ». **C'est faux.** Les 60 USD de la configuration sont le **plafond de relais** de l'étape, non son plafond dur.

- **Lettre du code** (orchestrateur épinglé, commit `a41b7b50…`) : `pole/budget_v56.py` (`3a672ace…`), l. 19-23 et 46 — au lancement d'une étape **protégée**, « plafond dur = max(plafond de relais ; S17 − cumul − attendu aux bases des étapes restantes non retirées) », fixé au lancement, arrondi au centime inférieur ; l. 142-148 (`plafond_dur`) ; l. 177-190 (point 3 de la règle : une étape protégée n'est **pas lancée** si cumul + plafond de relais > S17, « non mesuré (budget) ») ; l. 191-196 (lancement) ; l. 209-217 (une étape protégée dont le coût atteint son plafond dur, ou que l'orchestrateur a dû couper faute de reste, est « non mesuré (budget) »). `pole/noyau_v56.py` (`eb5a003e…`), l. 147-161 et 262-263 : chaque appel est borné à min(plafond de session du rôle, reste sous le **plafond dur** de l'étape) ; un appel qui ne trouve plus de reste n'est pas lancé et l'étape est marquée coupée. Le plafond de relais ne sert qu'au point 3 et au drapeau `au_dela_du_plafond_de_relais` du journal (l. 219-220), jamais à couper l'étape.
- **Budget de la configuration v9** (inchangé depuis la v6) : proposition attendu 25, plafond de relais 60 ; aiguillage 6 et 30 ; juges 14 et 50 ; étiquettes 0 et 0 (protégées) ; passe « tableau » et fusions retirées (plafond de relais 151 > 150).
- **Plafond dur de la proposition au lancement : max(60 ; 150 − 0 − (6 + 14 + 0)) = 130 USD** (souple). C'est le chiffre écrit par l'orchestrateur au manifeste de fin de l'essai à blanc v9 (`plafond_dur_usd` 130,0 pour la proposition ; 135,2, 147,6 et 144,4 pour les étapes suivantes, au coût simulé) et par l'essai à blanc v10 (§ 7 du rapport du développeur v10).
- **Seuils qui en découlent** (règle d'A1, point 3) :
  - **aiguillage** lancé si et seulement si cumul + 30 ≤ 150, soit **coût de la proposition ≤ 120 USD** ;
  - **juges** lancés si et seulement si cumul + 50 ≤ 150, soit **coût de la proposition et de l'aiguillage ≤ 100 USD** ;
  - **proposition** elle-même « non mesuré (budget) » seulement si elle atteint ses 130 USD (un appel restant ne trouve plus de reste) ;
  - le premier « non mesuré (budget) » est un **nœud** (C13, O12) : la course ne continue pas, rien n'est lu de ce qui a été mesuré, l'orchestrateur rend un code non nul et le lanceur le code 6 ; rapporté tel quel.
- **Rejeu par la vraie classe `BudgetV56`** (lecture seule de l'orchestrateur, hors réseau, développeur v10 ; les mêmes chiffres que le rejeu de la contre-lecture v9) :

| coût de la proposition ; de l'aiguillage ; des juges | plafond dur reçu | issue |
|---|---|---|
| estimations : 24,70 ; 4,96 ; 11,47 | proposition 130,00 ; aiguillage 111,30 ; juges 120,34 | tout joué, cumul 41,13 |
| hauts du devis : 76,36 ; 21,12 ; 31,24 | 130,00 ; 59,64 ; 52,52 | tout joué, cumul 128,72 |
| 100,00 ; 0,00 ; 11,47 | 130,00 ; 36,00 ; 50,00 | tout joué, cumul 111,47 |
| 95,00 ; 6,00 ; — | 130,00 ; 41,00 ; — | juges **non mesuré (budget)** (101 + 50 > 150), nœud |
| 120,00 ; 4,96 ; — | 130,00 ; 30,00 ; — | juges non mesuré (budget), nœud |
| 120,01 ; — ; — | 130,00 ; — ; — | aiguillage **non mesuré (budget)**, nœud |
| 130,00, appel suivant sans reste | 130,00 | proposition **non mesuré (budget)**, nœud |

- **Lecture pour la course** : au haut du devis (76,36), **rien n'est coupé** et la course peut finir proprement. Le risque d'une étape non mesurée porte sur les **juges** (si proposition et aiguillage dépassent ensemble 100 USD), puis sur l'**aiguillage** (si la proposition dépasse 120 USD), dans le régime où la proposition dépense bien au-delà de son haut (Carbon seize fois au pire cas sans qu'A3 l'arrête, et les autres proposeurs près de 3,00 par appel : 80 appels × 3,00 = 240 USD possibles, bornés à 130 par le plafond dur). Ce régime est peu probable (A3 arrête un rôle après trois échecs consécutifs ; les estimations par jetons sont dix fois plus basses) ; il n'est pas exclu.
- **Aucun dollar au-delà de 150** : le point 3 garantit cumul + plafond dur ≤ 150 au lancement de chaque étape, et chaque appel est borné au reste du plafond dur.

## 4. Part au pire par clé (inchangé depuis la v9 ; règle R-3237 : 16 × plafond de session pour un relais de proposeur seul ; 150 pour un relais qui tient l'aiguilleur ou un juge)

| clé (nom de variable) | relais, rôles | estimation (marge comprise) | haut | **part au pire v10 (= v9)** | v8 |
|---|---|---|---|---|---|
| `RR_ANTHROPIC_API_KEY_MINUIT` | Claude : deux proposeurs, aiguilleur, premier juge | 20,65 | 74,62 | **150,00** | 150 |
| `GEMINI_API_KEY`, partagée par **Argon et Carbon** | Argon : proposeur, second juge ; Carbon : proposeur | 10,97 + 8,77 = **19,74** | 14,66 + 45,26 = **59,92** | **198,00** (150 + 16 × 3,00) | 174 |
| clé d'OpenAI, **injectée par le secret de réseau** (nom déclaré `OPENAI_API_KEY`) | Astra : proposeur | 4,86 | 7,05 | **48,00** (16 × 3,00) | 24 |
| clé de Kimi | — | — | — | non déclarée | — |

- **Une part dépasse ce que la ligne permet** : la clé de Google, **198 USD**, au-dessus du plafond de la ligne GO-2026-11-18-14 (150 USD). C'est une **borne écrite**, non une dépense possible de la course : la part au pire est la somme des bornes de deux relais, et la dépense réelle de toute la course, toutes clés comprises, reste bornée par le plafond d'arrêt de 150 USD. La clé part sous la dispense R-3237 (solde illisible) : la part n'est confrontée à aucun reste lu ; si son solde devenait lisible, le lanceur exigerait un reste au-dessus de 198 USD. Les parts d'Astra (48) et de Minuit (150) tiennent dans la ligne.
- Relais d'Astra lancé à `--plafond-usd 48` exactement (le lanceur exige l'égalité avec sa part) ; ce plafond n'ajoute aucune dépense possible au-delà de ce que seize appels à 1,73 USD au plus peuvent coûter (27,66).
- Somme des estimations par clé : 20,65 + 19,74 + 4,86 = 45,25.
- La sonde commune d'Astra du jour (au plus 0,05 USD, appel réel trivial, R-3273) est en sus, sur la clé d'OpenAI, hors du plafond de la course.

## 5. Plafond demandé

**150 USD**, plafond d'arrêt de toute la course, **inchangé** (GO-2026-11-18-14) : aucune ligne de GO neuve n'est demandée. Le plafond par appel des proposeurs reste 3,00 USD (configuration v9) ; il ne change aucune borne de la course entière.

## 6. Ce qui n'est pas établi

- La pensée de Carbon sur les consignes de l'affinage (2 600 jetons d'entrée au plus) n'est pas mesurée ; l'estimation repose sur trois lots d'une autre course.
- Lecture de la documentation du fournisseur faite par la session principale, non par ce devis (aucun réseau). Une note du dépôt (`commande_argon_v3d.py`, l. 260-261) dit avoir constaté, sur un appel synchrone d'Argon, que l'interface ne comptait pas les pensées dans la sortie maximale : les réglages tiennent dans les deux lectures (32 768 ≥ 24 500 et provision 28 672 ≥ 1,25 × 20 696).
- Le coût réel des sessions Claude, d'Argon et d'Astra sous un plafond de 3,00 n'est pas mesuré : leurs estimations sont celles du devis v6 ; c'est pourquoi le « haut » n'est pas une borne (§ 3).
- La probabilité du régime où la proposition dépasse 100 USD (juges non lancés) n'est pas chiffrée.
