# Devis — pilote « oracles plantés » — v3 (remplace le devis v2, `c857e62c…`)

Aucun GO demandé par ce texte. Montants en USD. Chaque chiffre vient de la sortie du script v2 (`724e2b79…`, bloc cité) ou est nommé « supposé ». La version 6 du code et sa vérification coûtent 0 USD d'appels.

## 1. Prix (entrée / sortie par million de jetons ; relevés du 22 novembre 2026, `a7d9073f…` ; bloc 0)
- `claude-opus-5-5` : 4 / 20.
- `gemini-4-argon` : 2 / 10 jusqu'au 30 novembre 2026, 4 / 20 dès le 1er décembre.
- `kimi-k3.1-pro` : 2 / 10.
- `gpt-6.2-astra` : 8 / 40. Au-delà de 272 000 jetons d'entrée, le prix n'est pas relevé : l'appel est refusé (A13).
- Cache non compté ; raisonnement compté comme sortie. Pages relevées sans compte.
- Machine : 0,28 l'heure observé, borne haute 1,30 (repris du v1, supposés).

## 2. Calcul
Profils de jetons : **supposés**, repris du v1, à remplacer par la mesure.

**Effectifs (bloc 1).** 432 propositions Opus, 144 Argon. 208 items par bras, soit **58 appels neufs** par rapport au v1, dont 48 énoncés neufs (les témoins) et 10 seconds services. 40 reformulations, 60 jugements.

**Coûts unitaires, bas / attendu / pire (bloc 2).**
- Proposition Opus : 0,042 / 0,10 / 0,32. Argon : 0,021 / 0,05 / 0,16 à 2 / 10, comme Opus à 4 / 20.
- Item S : 0,156 / 0,308 / 1,272. Le plafond de 1,50 borne l'agent seul ; il n'est atteint dans aucun scénario (agent au pire 1,20).
- Item N : 0,052 / 0,136 / 0,496.
- Reformulation Kimi : 0,028 / 0,042 / 0,096.
- Jugement Astra : 0,128 / 0,224 / 0,576.

**Fumée (bloc 3).** Un appel par modèle, quatre appels d'au plus 1 000 / 1 000 jetons. Borne haute 0,096 (Argon à 2 / 10) ou 0,108 (à 4 / 20). Les totaux gardent le forfait **supposé** de 0,10, à 0,008 près.

**Postes, bas / attendu / pire (bloc 4).**
- P1 connus : 8,80 / 15,12 / 38,40.
- P2 proposeurs : 21,17 / 50,40 / 161,28 (Argon à 2 / 10) ; 24,19 / 57,60 / 184,32 (à 4 / 20).
- P3 bras S : 32,45 / 64,06 / 264,58. Bras N : 10,82 / 28,29 / 103,17.
- **Total des appels, course finie le 30 novembre au plus tard : 73,33 / 157,97 / 567,52.**
- **Total des appels, dès le 1er décembre : 76,36 / 165,17 / 590,56.**
- Course à cheval sur les deux dates : entre les deux colonnes ; écart maximal 3,02 / 7,20 / 23,04.
- P4 machine : 3,36 / 6,72 / 62,40.
- Appels + machine : 76,69 / 164,69 / 629,92 (30 novembre) ; 79,72 / 171,89 / 652,96 (1er décembre).

**Repli R1, à l'attendu (bloc 5).**
- Astra échoue : juge Kimi, −10,08 ; reformulateur Argon, +0,00 à 2 / 10 et +1,68 à 4 / 20.
- Kimi échoue : +0,00 à 2 / 10, +7,50 à 4 / 20.
- Les deux échouent : total 142,85 (2 / 10) ou 155,88 (4 / 20).

**Lignes conditionnelles, attendu, Argon à 4 / 20 (bloc 7).**
- Banque de connus refaite : 15,12.
- Un monde régénéré et rejoué : 12,50.
- Attendu avec les deux : **192,79** (184,99 à 2 / 10).

## 3. Plafonds proposés (bloc 7)
- **Réserve des appels en vol : 5,93.** C'est la logique v1 : trois agents S au plafond avec leur relecteur au pire, deux propositions au pire, un jugement au pire.
- **Plafond d'appels** : 192,79 × 1,5 + réserve = 294,90 sur valeurs exactes (script), arrondi à la dizaine supérieure : **300**. Le plafond est le même avec l'une ou l'autre réserve (script). La coupure A6 joue avant le pire cas.
- **Plafond machine : 65**, soit 48 h × 1,30 = 62,40, arrondi aux 5 supérieurs (règle désormais écrite).
- Somme des plafonds : 365. Ce n'est pas un attendu.

## 4. Intervalle de P7
[115,39 ; 261,41]. Formule : (120 / 164,28) × 157,97 et (260 / 164,28) × 165,17 (bloc 8). Le bas, le pire et le plafond en sortent. L'attendu, les replis et l'attendu avec conditionnelles y tombent.

## 5. Machine et environnement
- La machine louée ne porte que l'orchestrateur du bras S et le bac (réseau coupé, dossier neuf par énoncé, identité dédiée).
- Ni clé, ni vérité, ni générateur, ni évaluateur n'y montent.
- Générateur, tests de mort, normaliseur, registre et analyse tournent chez le conteneur de confiance, à 0 USD.
- Les 12 / 24 / 48 heures sont l'enveloppe du v1, **non réestimée** alors que ces tâches en sortent : c'est une borne haute supposée.

## 6. Sensibilité, total des appels à l'attendu (bloc 6)
- Juge Astra : 157,97 (Argon à 2 / 10) ; 165,17 (à 4 / 20).
- Juge Kimi (R1) : 147,89 ; 156,77.
- Postes dominants : bras S, puis proposeurs, à l'attendu comme au pire.

## 7. Positions sur les écarts du rejeu
- **+0,84 du § 5 du v2** : accepté. La phrase était fausse ; le surcoût est 0,00.
- **Fumée** : accepté. Quatre modèles, borne 0,108, forfait nommé supposé.
- **Réserve** : accepté. 5,93 remplace 5,72, parce que la formule du v2 oubliait le relecteur.
- **294,91** : accepté. 294,90 sur valeurs exactes, sans effet sur le plafond.
- **Plafond machine** : accepté. La règle d'arrondi est écrite.
- **Arrondis au centime** : acceptés tels quels.
- **Incohérences 1 à 10** : toutes acceptées et corrigées.
  1. P7 a sa formule (§ 4).
  2. « 58 appels neufs », non « 58 énoncés neufs ».
  3. Le plafond par item borne l'agent seul et ne joue dans aucun scénario.
  4. Quatre appels de fumée, un par modèle.
  5. Les trois cas de R1 sont chiffrés.
  6. Les heures de machine ne sont pas réestimées, et c'est dit.
  7. La ligne « appels + machine » est rétablie.
  8. **Le bas prend le juge Astra** : il n'est pas comparable au bas du v1, qui prenait Kimi.
  9. Le profil bas du juge est « repris » du script v1, non « reconstitué ».
  10. La course à cheval est bornée.
- **Refusé : rien.**

## 8. Hors devis, et à vérifier avant le GO
- Hors devis : relecture humaine et temps des agents (comme au v1) ; protocole P, qui demande un devis s'il fait des appels.
- À vérifier avant le GO :
  1. rejeu de ce v3 par script ;
  2. profils de jetons sur un monde témoin ;
  3. le harnais compte les jetons, vérifie l'identifiant servi et applique A13 ;
  4. le plafond retenu.
