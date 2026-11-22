# Devis — pilote « oracles plantés » — v4 (remplace le devis v3, `5c8a0f68518c1f335851c79d09a768b7b99d61c15b6406937cbd79b9fff9abe8`)

Aucun GO demandé par ce texte. Montants en USD. Chaque chiffre vient de la sortie du script v4 (`prereg/mathematiques-nouvelles-v1/calculs-v4/sortie-calculs-devis-pilote-generation-v4.txt`, `8194b015cd0a481824ee591db77a18d0933c27fb5ef59557828293ad1e2781f0`, blocs cités « v4-n »), ou, quand il n'a pas changé, de la sortie du script v3 (`efcbc21f768a2f558a967d1cd6ec1c39dad1daf67fce13ffec8bb09cd3f8eb74`, blocs « v3-n »), ou est nommé « supposé » avec sa formule. Le script v4 est du concepteur : à rejouer par le vérificateur du devis. Périmètre : celui du brouillon 4 du préenregistrement (bras S et N courus), scellé avec ce texte.

## 1. Prix (entrée / sortie par million de jetons ; relevés du 22 novembre 2026, `a7d9073f…` ; v4-0)
- `claude-opus-5-5` : 4 / 20.
- `gemini-4-argon` : 2 / 10 jusqu'au 30 novembre 2026, 4 / 20 dès le 1er décembre.
- `kimi-k3.1-pro` : 2 / 10.
- `gpt-6.2-astra` : 8 / 40. Au-delà de 272 000 jetons d'entrée, le prix n'est pas relevé : l'appel est refusé (A13).
- Cache non compté ; raisonnement compté comme sortie. Pages relevées sans compte.
- Machine : 0,28 l'heure observé, borne haute 1,30 (repris du v1, supposés).

## 2. Calcul
Profils de jetons : **supposés**, repris du v1. La garde de projection (§ 3) les remplace par la mesure dès le premier bloc.

**Effectifs (v4-1).** 432 propositions Opus, 144 Argon. 208 items par bras. 40 reformulations. 60 jugements : 40 connus et 20 énoncés faux de mondes.

**Coûts unitaires, bas / attendu / pire (v4-2).**
- Proposition Opus : 0,042 / 0,10 / 0,32. Argon : 0,021 / 0,05 / 0,16 à 2 / 10, comme Opus à 4 / 20.
- Item S : 0,156 / 0,308 / 1,272. Le plafond de 1,50 borne l'agent seul ; il n'est atteint dans aucun scénario (agent au pire 1,20 ; v3-2).
- Item N : 0,052 / 0,136 / 0,496. Son schéma de sortie passe à celui de S (trois instances au plus) : le profil supposé n'est pas changé.
- Reformulation Kimi : 0,028 / 0,042 / 0,096.
- Jugement Astra : 0,128 / 0,224 / 0,576.

**Fumée (v3-3).** Un appel par modèle, quatre appels d'au plus 1 000 / 1 000 jetons. Borne haute 0,096 (Argon à 2 / 10) ou 0,108 (à 4 / 20). Les totaux gardent le forfait **supposé** de 0,10, à 0,008 près.

**Postes, bas / attendu / pire (v4-4).** Le bas prend le juge Astra.
- P1 connus : 8,80 / 15,12 / 38,40.
- P2 proposeurs : 21,17 / 50,40 / 161,28 (Argon à 2 / 10) ; 24,19 / 57,60 / 184,32 (à 4 / 20).
- P3 bras S : 32,45 / 64,06 / 264,58. Bras N : 10,82 / 28,29 / 103,17.
- **Total des appels, Argon au prix de novembre : 73,33 / 157,97 / 567,52.**
- **Total des appels, Argon au prix de décembre : 76,36 / 165,17 / 590,56.**
- Écart d'un prix d'Argon à l'autre : 3,02 / 7,20 / 23,04. Le brouillon 4 interdit une course à cheval pour Argon (un seul prix).
- P4 machine : 3,36 / 6,72 / 62,40.
- Appels + machine : 76,69 / 164,69 / 629,92 (novembre) ; 79,72 / 171,89 / 652,96 (décembre).

**Repli R1, à l'attendu (v3-5).**
- Astra échoue : juge Kimi, −10,08 ; reformulateur Argon, +0,00 à 2 / 10 et +1,68 à 4 / 20.
- Kimi échoue : +0,00 à 2 / 10, +7,50 à 4 / 20 ; total 157,97 ou 172,68.
- Les deux échouent : total 142,85 (2 / 10) ou 155,88 (4 / 20).

**Lignes conditionnelles, attendu, Argon à 4 / 20 (v4-5).**
- Banque de connus refaite : 15,12. Elle couvre aussi les reformulations infidèles refaites une fois.
- Un monde régénéré et rejoué : 12,50.
- Attendu avec les deux : **192,79** (184,99 à 2 / 10 ; v3-7).

## 3. Plafonds proposés et gardes de dépense (v4-7, v4-9)
- **Réserve des appels en vol : 6,50.** Créneaux tenus par le harnais (A6) : trois items S, deux autres appels, un jugement. Formule : 3 × 1,644 + 2 × 0,496 + 0,576. Un item S au pire : agent au plafond 1,50 et relecteur au pire, repli R1 compris (0,144). Un autre appel au pire : l'item N (0,496), qui dépasse la proposition (0,32) et la reformulation. Un jugement au pire : Astra (0,576). Elle remplace 5,93, qui ne comptait ni item N en vol ni relecteur de repli.
- **Plafond d'appels** : 192,79 × 1,5 + 6,50 = 295,68, arrondi à la dizaine supérieure : **300**. Avec l'ancienne réserve, 295,11 (et non 294,90) ; le plafond est le même. Il vaut 1,82 fois l'attendu simple de décembre ; le pire vaut 3,58 fois cet attendu : la coupure A6 joue avant le pire cas.
- **Plafond machine : 65**, soit 48 h × 1,30 = 62,40, arrondi aux 5 supérieurs.
- Somme des plafonds : 365. Ce n'est pas un attendu.
- **Garde de projection (A14).** Douze blocs d'un monde. À la fin de chaque bloc : projection = dépense + Σ par poste (unités restantes × coût unitaire moyen mesuré) ; arrêt avant le bloc suivant si elle dépasse plafond − réserve = 293,50. Dépense à la fin du premier bloc : 7,62 / 15,69 / 54,00. La projection tolère des coûts unitaires jusqu'à 1,78 fois l'attendu. Si le profil « pire » se révèle, la course s'arrête à 54,00 au lieu d'aller à 300 sur des données tronquées : 246,00 d'économie.

## 4. Intervalle de P7 (v4-8)
[115,39 ; 261,41]. Formule : (120 / 164,28) × 157,97 et (260 / 164,28) × 165,17. Le bas, le pire et le plafond en sortent. L'attendu, les replis et l'attendu avec conditionnelles y tombent (v3-8).

## 5. Machine et environnement
- La machine louée ne porte que l'orchestrateur du bras S et le bac (réseau coupé, dossier neuf par énoncé, identité dédiée).
- Ni clé, ni racine, ni vérité, ni générateur, ni évaluateur n'y montent.
- Générateur, tests de mort, normaliseur, registres et analyse tournent chez le conteneur de confiance, à 0 USD. Le bras N passe par le harnais d'appels, sans machine.
- Les 12 / 24 / 48 heures sont l'enveloppe du v1, **non réestimée** : c'est une borne haute supposée.

## 6. Sensibilité, total des appels à l'attendu (v3-6)
- Juge Astra : 157,97 (Argon à 2 / 10) ; 165,17 (à 4 / 20).
- Juge Kimi (R1) : 147,89 ; 156,77.
- Postes dominants : bras S, puis proposeurs, à l'attendu comme au pire.

## 7. Protocole P d'antériorité — ligne à part, hors du plafond de 300 (v4-10)
Profils **supposés**. Lecteur `gpt-6.2-astra` (8 / 40) ; second lecteur `kimi-k3.1-pro` (2 / 10) sur les pièces dites « collision » ou « doute ». La moisson, les téléchargements et le contrôle des extraits sont du code : 0 USD d'appels.
- Pièces lues : au plus 8 par question, soit 40 ; avec au plus 2 citants par question, 50.
- Lecture d'une pièce par Astra, bas / attendu / pire : 0,24 / 0,44 / 1,44, pour 20 000 / 2 000, 40 000 / 3 000 et 150 000 / 6 000 jetons d'entrée et de sortie.
- Requêtes et tri : 2 appels par question, soit 10 ; 0,112 / 0,20 / 0,48 par appel, pour 4 000 / 2 000, 10 000 / 3 000 et 30 000 / 6 000 jetons.
- Second lecteur, par pièce : 0,06 / 0,11 / 0,36 ; 0, 10 ou 50 pièces relues (supposé).
- **Total : 10,72 / 25,10 / 94,80.** Formules : 40 × 0,24 + 10 × 0,112 ; 50 × 0,44 + 10 × 0,20 + 10 × 0,11 ; 50 × 1,44 + 10 × 0,48 + 50 × 0,36.
- **Plafond proposé : 40** (25,10 × 1,5 = 37,65, dizaine supérieure). Coupure : dépense + pire cas du prochain appel (1,44) > 40 ⇒ plus de lancement.
- Variantes à l'attendu : Astra seul, 24,00 ; Kimi seul, 6,00.
- Par un humain ou par une session de l'abonnement : 0 USD d'appels.

## 8. Options de périmètre soumises au directeur (v4-11 ; Argon à 4 / 20 ; même règle de plafond)

| option | appels, bas / attendu / pire | attendu avec conditionnelles | réserve | plafond d'appels | plafond machine |
|---|---|---|---|---|---|
| (a) brouillon 4 : S et N courus | 76,36 / 165,17 / 590,56 | 192,79 | 6,50 | 300 | 65 |
| (b) sans le bras N | 65,54 / 136,88 / 487,40 | 162,14 | 6,15 | 250 | 65 |
| (c) sans les bras S et N | 33,09 / 72,82 / 222,82 | 92,74 | 1,22 | 150 | 0 |

Économie attendue : 28,29 pour (b), 92,35 pour (c). Les bras S et N font 0,559 de l'attendu de (a). Ce devis et le brouillon 4 sont écrits pour (a) ; (b) ou (c) demanderaient un brouillon 5 en différences.

## 9. Échéance et prix d'Argon
Le doublement d'Argon au 1er décembre ne touche que 144 propositions : 7,20 à l'attendu, 23,04 au pire (v4-4). Il ne justifie pas de presser la chaîne ; le plafond est calculé au prix de décembre.

## 10. Positions sur la contre-lecture du brouillon 3 (remarque 19) et sur le rejeu du v3
- **« 192,79 × 1,5 + réserve = 294,90 »** : accepté. Avec 5,93 le calcul donne 295,11 ; il est refait ici avec la réserve v4 : 295,68.
- **En-tête renvoyant à la sortie du script v2** : accepté. Renvoi aux sorties v3 et v4, empreintes entières.
- **« Le bas prend le juge Astra » absent du § 2** : accepté, écrit au § 2.
- **Changé de mon chef** : réserve 5,93 → 6,50 (§ 3) ; garde de projection ; ligne du protocole P ; options de périmètre ; totaux « Kimi échoue » écrits ; l'essai des profils « sur un monde témoin » avant le GO est retiré, parce qu'il serait une dépense sans GO : le premier bloc de la course en tient lieu.
- **Refusé : rien.**

## 11. Hors devis, et à vérifier avant le GO
- Hors devis : relecture humaine et temps des agents ; liste des connus, consignes, lot B3 (0 USD d'appels).
- À vérifier avant le GO :
  1. rejeu de ce v4 par le vérificateur ;
  2. le harnais compte les jetons, vérifie l'identifiant servi, tient les créneaux de A6 et applique A13 et A14 ;
  3. le périmètre (§ 8), le plafond et l'échéance retenus par le directeur ;
  4. les prix, relus sur les pages publiques la veille de la fumée ; un écart à ce devis demande un devis v5 avant tout appel.
