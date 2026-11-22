# Devis — pilote « oracles plantés » — v2 (remplace le devis v1, `6f485216…`)

Aucun GO demandé par ce texte : le GO se prend sur cette v2 contre-lue. Montants en USD. Aucun script n'a été lancé : les formules ci-dessous sont à rejouer par script avant la contre-lecture.

## 1. Prix (entrée / sortie par million de jetons ; relevés du 22 novembre 2026, `a7d9073f…`)

| modèle | identifiant | prix |
|---|---|---|
| Opus 5.5 | `claude-opus-5-5` | 4 / 20 |
| Gemini 4 Argon | `gemini-4-argon` | 2 / 10 jusqu'au 30 novembre 2026 ; 4 / 20 dès le 1er décembre |
| Kimi K3.1 Pro | `kimi-k3.1-pro` | 2 / 10 |
| GPT-6.2 Astra | `gpt-6.2-astra` | 8 / 40 (au-delà de 272 000 jetons d'entrée : non relevé ; appel refusé, garde A13) |

- Cache non compté ; raisonnement compté comme sortie.
- Pages relevées sans compte : le prix d'un compte donné peut différer.
- Machine : 0,28 l'heure observé, borne haute 1,30 (devis v1, non relevés à neuf).

## 2. Calcul
Coût d'un appel = (entrée × prix d'entrée + sortie × prix de sortie) / 10⁶. Profils de jetons : **supposés**, repris du devis v1, à remplacer par la mesure.

**Effectifs**
- Propositions Opus : 12 × (12 + 24) = 432. Propositions Argon : 12 × 12 = 144.
- Bras S et N : 150 + 48 témoins (garde A4) + 10 redoublés = **208 items par bras**. Les 58 items ajoutés sont neufs par rapport au v1.
- Reformulations : 40. Jugements : 60.

**Coûts unitaires (bas / attendu / pire)**
- Proposition (3k/1,5k ; 10k/3k ; 20k/12k) : Opus 0,042 / 0,10 / 0,32. Argon à 2/10 : 0,021 / 0,05 / 0,16. Argon à 4/20 : 0,042 / 0,10 / 0,32.
- Item S, agent Opus et relecteur Kimi : 0,156 / 0,308 / 1,272. Ces chiffres sont repris de la sortie v1 (23,40, 46,20 et 190,80 divisés par 150), les prix des deux modèles étant inchangés. Plafond par item : 1,50.
- Item N : 0,052 / 0,136 / 0,496 (même reprise).
- Reformulation Kimi : 0,028 / 0,042 / 0,096.
- Jugement Astra : 0,128 / 0,224 / 0,576. L'attendu et le pire sont les chiffres v1 multipliés par 0,8 (les deux prix baissent de 10/50 à 8/40). Le bas est **supposé** : profil 6k/2k reconstitué du bas v1 (jugement Kimi 0,032, quatre fois moins cher), avec la reformulation à 4k/2k.
- Appels de fumée : 0,10. **Supposé** : quatre appels d'au plus mille jetons en entrée et en sortie.

**Postes**

| poste | formule | bas | attendu | pire |
|---|---|---|---|---|
| P1 connus | 40 × reformulation + 60 × jugement | 8,80 | 15,12 | 38,40 |
| P2 proposeurs, Argon à 2/10 | 432 × Opus + 144 × Argon | 21,17 | 50,40 | 161,28 |
| P2 proposeurs, Argon à 4/20 | idem | 24,19 | 57,60 | 184,32 |
| P3 bras S | 208 × item S | 32,45 | 64,06 | 264,58 |
| P3 bras N | 208 × item N | 10,82 | 28,29 | 103,17 |
| fumée | | 0,10 | 0,10 | 0,10 |
| **total des appels, course finie le 30 novembre au plus tard** | | **73,33** | **157,97** | **567,52** |
| **total des appels, dès le 1er décembre** | | **76,36** | **165,17** | **590,56** |
| P4 machine | 12 / 24 / 48 h × 0,28 (pire à 1,30) | 3,36 | 6,72 | 62,40 |

**Repli R1 (attendu)**
- Juge Kimi : 60 × 0,056 = 3,36 au lieu de 13,44, soit −10,08.
- Reformulateur Argon à 4/20 : 40 × 0,084 = 3,36 au lieu de 1,68, soit +1,68.

**Lignes conditionnelles (attendu, Argon à 4/20)**
- Banque de connus refaite une fois : 15,12.
- Un monde régénéré et rejoué : 48 × 0,10 + (208 / 12) × 0,444 = 12,50.
- **Attendu avec lignes conditionnelles : 192,79.**

## 3. Plafonds proposés
- **Réserve des appels en vol** : 3 × 1,50 + 2 × 0,32 + 0,576 = **5,72**.
- **Plafond d'appels** : 192,79 × 1,5 + 5,72 = 294,91, arrondi à la dizaine supérieure : **300** proposé. La coupure A6 joue avant le pire cas ; la course s'arrête alors par blocs de mondes complets.
- **Plafond machine** : 65 (48 h × 1,30 ; minuterie de destruction à 48 heures).
- **Somme des plafonds** : 365. Ce n'est pas un attendu.

## 4. Machine et environnement (corrigé par l'erratum 1, point 1)
La phrase du devis v1 sur le générateur dans le bac est fausse.

- La machine louée ne porte que l'orchestrateur du bras S et le bac. Le bac n'exécute que le code écrit par le modèle du bras S : réseau coupé, dossier neuf par énoncé, identité dédiée. La machine n'a de sortie que vers le relais.
- **Ni clé, ni vérité, ni générateur, ni évaluateur n'y montent.** Elle rend des sorties scellées, puis inventaire, versement et destruction par identifiant.
- Le générateur, les six tests de mort, le normaliseur, le registre et l'analyse tournent chez le conteneur de confiance, sur processeur, à 0 USD.
- Les 12 / 24 / 48 heures restent une enveloppe.

## 5. Sensibilité (total des appels, attendu)

| | juge Astra | juge Kimi (repli R1) |
|---|---|---|
| Argon à 2/10 | 157,97 | 147,89 |
| Argon à 4/20 | 165,17 | 156,77 |

- La colonne Kimi compte le reformulateur Argon (+0,84 à 2/10, +1,68 à 4/20).
- Si la course chevauche le 1er décembre, chaque appel Argon est compté au prix de son jour.
- Postes dominants : le bras S (plafond par item), puis les proposeurs.

## 6. Relecture humaine, temps des agents, hors devis
Inchangés (devis v1, § 6 et § 7).

Ajouts, non chiffrés ici :
- la version 5 du code et sa vérification (0 USD d'appels) ;
- la lecture d'antériorité sur la méthode (protocole P) : hors devis ; elle demande un devis si elle fait des appels.

## 7. À vérifier avant le GO
1. Rejeu par script des calculs du § 2.
2. Appels de fumée (accès à Astra et à Kimi), dans le plafond, après le GO.
3. Profils de jetons, sur un monde témoin.
4. Le harnais compte les jetons par appel, vérifie l'identifiant servi et applique A13.
5. Le plafond retenu par le directeur.
