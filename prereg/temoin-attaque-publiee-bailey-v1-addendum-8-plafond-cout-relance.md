# Addendum 8 au préenregistrement du témoin de Bailey — plafond de coût de l'offre de la relance de la confirmation

18 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. Choix de Lazar : « B » (mot relayé par la session mère, note
`registres/passations/2026-11-18-…-mot-lazar-bailey-addendum-8-B.md`). Brouillons 1 à 4 gardés tels quels dans
`brouillons/` (R12) ; l'option A des brouillons 2 à 4 (heures d'arrêt au taux du stockage) n'est pas retenue. Le texte
(`fb6c2f34…`) et les addenda 1 à 7 restent tels quels ; en cas de conflit, le texte prime et l'écart est un nœud.
**Écrit et scellé avant toute lecture** : aucune note de sonde ni de juge du témoin n'a été lue, par aucune session.
**Correction postérieure au constat** : cet écart est décidé après que la session a constaté que la règle du texte, au
plafond de coût de l'addendum 7, pouvait donner à la relance K < 71 (table du § 1) ; ce constat ne repose que sur des
champs techniques (création, c, t, D, B), jamais sur un résultat.

## 1. Pourquoi
La confirmation (addendum 7, `554a74d0…`) s'est interrompue le 17 novembre : compte Vast sans crédit, instance 61049303
arrêtée par Vast ; conduite finie à 17:44Z, instance gardée, « reprise requise »
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v15/bilan-conduite-v5.json`). Sous 20 tours complets (établi par la
reprise), la liste d'arrêt permet une relance (texte l. 371), par le chemin de l'addendum 5 (addendum 7, § 2.1), sur le
même poste de dépense (D cumulée, même B = 85 ; texte l. 252-254 et 371 ; addendum 7, § 2.1 et 2.2).

La règle de la relance (`lanceur_v21.Conduite._relance_seule`) recalcule K = `analyse_v3.nombre_de_tours(85, D, c,
1265.0215)`, D compté selon le texte (l. 252-254 : chaque instance « à son taux réel × heures écoulées de sa création à sa
destruction », heures d'arrêt comprises). Une confirmation n'est retenue qu'à K′ ≥ 71 (addendum 7, § 3). K selon l'heure
de la destruction de 61049303 par la reprise et le coût c de l'offre (D à l'horloge, plus 0,75 h de mise en place à c) :

| destruction vers | 1,33 USD/h | 1,40 | 1,45 | 1,50 | 1,60 (plafond de l'addendum 7) |
|---|---|---|---|---|---|
| 09:00Z | 72 | 72 | 72 | 70 | 65 |
| 10:00Z | 72 | 72 | 70 | 67 | 63 |
| 12:00Z | 71 | 68 | 65 | 63 | 59 |

Au plafond de 1,6 USD/h, la relance pouvait donc tourner sans pouvoir être retenue.

## 2. Écart (décidé par Lazar : « B »)
Pour la seule relance de la confirmation : le coût de l'offre choisie, carte et 110 Go de stockage (grandeur `cout` du
choix d'offre), est d'au plus **1,40 USD/h** au lieu de 1,6 (addendum 7, § 2.4). Le reste du § 2.4 est inchangé (filtre du
poste v12, `cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, offre la moins chère qui passe, fenêtre de 24 h sans offre
conforme bornée à 23 h 45 : « relance non courue (aucune offre) »). B, la garde B − 2, R, le GO (`GO-2026-11-17-07`),
le comptage de D et toutes les règles de lecture de l'addendum 7 sont inchangés.

Mise en œuvre : générateur de relance de version neuve (`docs/notes/reproduction-attaque-publiee-v1/
generer-pieces-relance-confirmation-bailey-v3.py`, option B ; la v2 reste telle quelle, R12), contre-lu (R2) ; seule
différence due à cet addendum dans les pièces : la ligne `d = [o for o in d if cout(o) <= 1.6]` du poste devient
`cout(o) <= 1.4` (une seule occurrence exigée). La conduite de relance vérifie, avant toute création, l'empreinte de cet
addendum.

Avec une destruction de 61049303 avant ≈ 10:50Z le 18 novembre, la règle donne K ≥ 71 pour toute offre conforme ; à une
destruction plus tardive, K peut tomber sous 71 même à 1,40 USD/h : la session le constate au calcul de la règle (champ
technique) et la relance est lue selon le texte et l'addendum 7 (régime réduit si 20 ≤ K′ ≤ 70, non retenue).

## 3. Risques déclarés
- Aucune offre à 1,40 USD/h ou moins dans les 24 h : relance non courue ; verdict retenu : celui à 36 tours (§ 3 de
  l'addendum 7).
- Moins d'offres conformes qu'à 1,6 : délai possible avant la création, qui abaisse K (≈ 1,3 USD par heure d'attente dans D).
- La relance reste comptée au plein taux pour les heures d'arrêt de 61049303 (texte), ce qui surestime D de ≈ 18 USD
  pour une destruction vers 09:00Z ; règle de prudence gardée telle quelle.

## 4. Contre-lecture
À venir (R2), par un agent neuf d'un autre modèle que l'auteur (N-052).
