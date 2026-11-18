# Addendum 8 au préenregistrement du témoin de Bailey — plafond de coût de l'offre de la relance de la confirmation — brouillon 1

18 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`). **Brouillon : non contre-lu, non
scellé, sans effet tant que Lazar n'a pas donné son mot (écart à un préenregistrement scellé : nœud).** Le texte
(`fb6c2f34…`) et les addenda 1 à 7 restent tels quels. **Écrit avant toute lecture** : aucune note de sonde ni de juge
du témoin n'a été lue, par aucune session.

## 1. Pourquoi
La confirmation (addendum 7, `554a74d0…`) s'est interrompue le 17 novembre vers 17:12Z : compte Vast sans crédit,
instance 61049303 arrêtée par Vast (`runs/temoin-bailey-v1-20261111/sortie-conduite-v15/bilan-conduite-v5.json`,
« reprise requise »). Le run principal comptait environ 16 tours complets (à établir par la reprise). Sous 20 tours, la
liste d'arrêt permet une relance (texte l. 371), par le chemin de l'addendum 5 (addendum 7, § 2.1).

La règle de la relance (`lanceur_v21.Conduite._relance_seule`) recalcule K sur le budget restant : même B = 85, D du
poste, c de l'instance neuve, t du pilote (1 265,02 s). D compte 61049303 au taux de marche (1,3248 USD/h) de sa création
à sa destruction par la reprise, heures d'arrêt comprises. Avec une reprise vers 09:00Z le 18 novembre, la règle donne
K = 72 jusqu'à c = 1,45 USD/h, mais K = 70 à 1,50 et 65 à 1,60, plafond du § 2.4 de l'addendum 7 ; vers 10:00Z, K = 72
jusqu'à 1,40 seulement. Or une confirmation n'est retenue qu'à K′ ≥ 71 (addendum 7, § 3). Au plafond actuel, la relance
pourrait donc tourner (≈ 34 USD) sans pouvoir être retenue.

## 2. Écart (décidé par Lazar, à son mot)
Pour la seule relance de la confirmation (conduite v16, poste v14) : le coût de l'offre choisie, carte et 110 Go de
stockage (grandeur `cout` du choix d'offre), est d'au plus **1,40 USD/h** au lieu de 1,6 (addendum 7, § 2.4). Le reste du
filtre (`cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, filtre du poste v12), la fenêtre de 24 h sans offre conforme
(« relance non courue (aucune offre) »), B, la garde B − 2, le GO (`GO-2026-11-17-07`) et toutes les règles de lecture
de l'addendum 7 sont inchangés. Seule différence dans les pièces : la borne `cout(o) <= 1.4` dans `choisir_offre.py` du
poste v14 (générateur de relance, version neuve).

## 3. Risques déclarés
- Aucune offre à 1,40 USD/h ou moins dans les 24 h : pas de relance ; la confirmation est rapportée sans verdict retenu,
  et le verdict retenu est celui à 36 tours (addendum 7, § 3).
- Une reprise après ≈ 10:00Z fait tomber K sous 71 même à 1,40 USD/h (K = 68 vers 12:00Z) : la relance n'est alors
  plus retenable ; la session la propose comme non lancée, sur le mot de Lazar.
- Le plafond n'est pas établi comme optimal : il découle de la table ci-dessus, calculée avant toute lecture.

## 4. Contre-lecture
À faire (R2), après le mot de Lazar.
