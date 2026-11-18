# Addendum 8 au préenregistrement du témoin de Bailey — dépense des heures d'arrêt et plafond de coût de la relance de la confirmation — brouillon 2

18 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`). **Brouillon : non contre-lu, non
scellé, sans effet tant que Lazar n'a pas choisi et donné son mot (écart à un préenregistrement scellé : nœud).** Le
brouillon 1 (`…-addendum-8-plafond-cout-relance-brouillon1.md`) reste tel quel (R12). Le texte (`fb6c2f34…`) et les
addenda 1 à 7 restent tels quels ; en cas de conflit, le texte prime et l'écart est un nœud. **Écrit avant toute
lecture** : aucune note de sonde ni de juge du témoin n'a été lue, par aucune session.

## 1. Pourquoi
La confirmation (addendum 7, `554a74d0…`) s'est interrompue le 17 novembre vers 17:12Z : compte Vast sans crédit,
instance 61049303 arrêtée par Vast ; conduite finie à 17:44Z, instance gardée arrêtée, « reprise requise »
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v15/bilan-conduite-v5.json`). Le run principal compte moins de
20 tours complets (≈ 16 attendus ; établi par la reprise). La liste d'arrêt permet une relance (texte l. 371), par le
chemin de l'addendum 5 (addendum 7, § 2.1), sur le même poste de dépense (D cumulée, même B = 85 ; addendum 7, § 2.2).

Le texte définit (l. 252-254) : « c : taux réel de l'instance en cours, carte et stockage ; D : dépense du poste […],
toutes instances comprises, chacune comptée à son taux réel × heures écoulées de sa création à sa destruction, à
l'horloge ». Le code suit ce texte (`lanceur_v21.Poste.depense`, l. 709-712 : un seul c par instance). Il compte donc les
heures où 61049303 est **arrêtée** au taux de marche (1,3248 USD/h), alors que Vast ne facture alors que le stockage :
`storage_total_cost` 0,1528 USD/h (110 Go à 1,0 USD par Go et par mois ; relevé en lecture seule par la session mère le
18 novembre à 01:41Z, et par cette session à 01:11Z). Règle de prudence pensée pour une instance en marche : sur les
heures d'arrêt, elle compte ≈ 8,7 fois la dépense réelle.

Conséquence sur la relance (`_relance_seule` : K recalculé sur B − R − D, t = 1 265,02 s du pilote de la confirmation ;
une confirmation n'est retenue qu'à K′ ≥ 71, addendum 7, § 3) :

| D compté | c de l'offre | reprise vers 09:00Z | vers 12:00Z | vers 18:00Z |
|---|---|---|---|---|
| texte actuel (plein taux à l'arrêt) | 1,33 | 72 | 71 | < 71 |
| texte actuel | 1,40 | 72 | 68 | < 68 |
| texte actuel | 1,60 (plafond du § 2.4) | 65 | 59 | < 59 |
| heures d'arrêt au taux du stockage | 1,33 à 1,60 | 72 | 72 | 72 |

(D calculé à l'horloge, avec 0,75 h de mise en place au taux c ; calcul de la session, `analyse_v3.nombre_de_tours`.)

## 2. Écarts proposés (Lazar choisit A, B, ou A et B)
**A (recommandé). Heures d'arrêt au taux du stockage.** Pour une instance du poste arrêtée par le loueur ou par la
conduite (statut `exited` ou `stopped`) et gardée en vue d'une reprise, les heures écoulées entre l'arrêt et le
redémarrage, ou la destruction, sont comptées dans D au taux du stockage de cette instance relevé chez le loueur
(`storage_total_cost`), et non à c. Pour 61049303 : arrêt à l'heure du premier sondage en échec consigné par la conduite
(`conduite-v5.jsonl`, champ technique), taux 0,1528 USD/h, relevé consigné avec sa source ; les heures de marche de la
reprise (redémarrage pour le seul transfert) restent comptées à c. D reste une borne prudente : arrêt daté par la
conduite (au plus tôt), taux de stockage relevé. Mise en œuvre : la conduite de relance reçoit, dans ses instances
antérieures, la dépense de 61049303 calculée ainsi (deux segments), au lieu d'un seul segment au taux c ; aucun autre
code ne change, aucune garde n'est desserrée (B, B − 2, R, échéance inchangés).

**B (en option ou à défaut de A). Plafond de coût de l'offre de la relance.** Pour la seule relance : coût de l'offre
(carte et 110 Go, grandeur `cout` du choix d'offre) d'au plus 1,40 USD/h au lieu de 1,6 (addendum 7, § 2.4). Avec A, B
n'est plus nécessaire pour K, mais il réduit la dépense attendue.

Tout le reste du texte et des addenda 1 à 7 s'applique sans changement : graines, critères gelés, liste d'arrêt, règles
de lecture de l'addendum 7 (aucune note lue avant la clôture ; lecture par `lecture_scellee_v3`).

## 3. Risques déclarés
- A est un écart à une définition du texte (D), décidé avant toute lecture ; il ne joue que sur la dépense et le nombre
  de tours, jamais sur la lecture. Il est rapporté comme écart avec le verdict de la confirmation.
- Si l'arrêt de 61049303 ne peut pas être daté par la conduite, A ne s'applique pas : plein taux, comme le texte.
- Sans A, et avec une reprise après ≈ 10:00Z à 1,40 USD/h, la relance ne serait plus retenable ; la session la
  proposerait alors comme non lancée.
- Aucune offre conforme (B : ≤ 1,40 USD/h) dans les 24 h : relance non courue ; verdict retenu : celui à 36 tours.

## 4. Contre-lecture
À faire (R2), puis vérification adverse, avant le scellement et après le mot de Lazar.
