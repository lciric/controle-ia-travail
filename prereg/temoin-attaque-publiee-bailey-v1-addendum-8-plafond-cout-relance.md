# Addendum 8 au préenregistrement du témoin de Bailey — plafond de coût de l'offre de la relance de la confirmation

18 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`), branche
`claude/compassionate-meitner-d4ryyk`. Choix de Lazar : « B » (mot relayé par la session mère, note
`registres/passations/2026-11-18-0209-mot-lazar-bailey-addendum-8-B.md`, `cf188651…`). Brouillons 1 à 4 gardés tels quels dans
`brouillons/` (R12) ; l'option A des brouillons 2 à 4 (heures d'arrêt au taux du stockage) n'est pas retenue. Le texte
(`fb6c2f34…`) et les addenda 1 à 7 restent tels quels ; en cas de conflit, le texte prime et l'écart est un nœud.
**Écrit et scellé avant toute lecture** : aucune note de sonde ni de juge du témoin n'a été lue, par aucune session.
**Correction postérieure au constat** : cet écart est décidé après que la session a constaté que la règle du texte, au
plafond de coût de l'addendum 7, pouvait donner à la relance K < 71 (table du § 1) ; ce constat ne repose que sur des champs techniques (création, c, t, D, B, état de l'instance, heure de sa
destruction), jamais sur un résultat. Effet déclaré : l'écart ne change que c, donc K ; il rend plus probable une
confirmation retenue (K′ ≥ 71, addendum 7, § 3) plutôt que le verdict à 36 tours. Son seul objet est que la relance
puisse atteindre K ≥ 71, donc que la confirmation puisse être retenue, quel que soit son verdict ; aucun des deux verdicts
n'est lu ni connu ; aucun seuil, métrique, population ni règle de lecture ne change ; il ne vise aucun signe (R3 : aucun
résultat ne motive l'écart). Le rapport de l'étape 1 cite cet écart, sa cause et le K calculé par la règle (addendum 7,
§ 3, première puce).

## 1. Pourquoi
La confirmation (addendum 7, `554a74d0…`) s'est interrompue le 17 novembre : compte Vast sans crédit, instance 61049303
arrêtée par Vast ; conduite finie à 17:44Z, instance gardée, « reprise requise »
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v15/bilan-conduite-v5.json`). Si la reprise établit moins de 20 tours complets (sinon pas de relance, texte l. 372), la liste d'arrêt permet une relance
(texte l. 371), par le chemin de l'addendum 5 (addendum 7, § 2.1), sur le
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
Pour la seule relance de la confirmation (texte l. 371 ; addendum 7, § 2.1), c'est-à-dire pour toute création d'instance
faite pour elle, mise en place refaite (l. 363) comprise, et pour rien d'autre : le coût de l'offre choisie, carte et 110 Go de stockage (grandeur `cout` du
choix d'offre), est d'au plus **1,40 USD/h** au lieu de 1,6 (addendum 7, § 2.4). Le reste du § 2.4 est inchangé : filtre du poste v12, `cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, offre la moins chère
qui passe, disque 110 Go ; aucune offre conforme dans les 24 h qui suivent le lancement du poste : rien ne tourne (le poste
v13, repris tel quel, arrête son attente 23 h 45 après son début, l. 144). Pour la relance, cette cause est nommée
« relance non courue (aucune offre) » ; elle se lit comme la cause « aucune offre (§ 2.4) » du § 3 de l'addendum 7.
Aucun retour au plafond de 1,6 USD/h ni autre plafond sans nouveau mot de Lazar et nouvel addendum (nœud). Le mot « B »
ne vaut pas mot de lancement de la relance : celui-ci reste requis (addendum 7, § 2.1 ; addendum 5, condition 7) ; il est
donné par le mot de Lazar du 18 novembre vers 01:56Z, « relance tout »
(`registres/passations/2026-11-18-0157-mot-lazar-bailey-credit-relance-tout.md`, `1406cca6…`). B, la garde B − 2, R, le GO (`GO-2026-11-17-07`),
le comptage de D et toutes les règles de lecture de l'addendum 7 sont inchangés.

Mise en œuvre : générateur de relance de version neuve (`docs/notes/reproduction-attaque-publiee-v1/
generer-pieces-relance-confirmation-bailey-v3.py`, option B ; la v2 reste telle quelle, R12), contre-lu (R2) ; deux différences dues à cet addendum dans les pièces, et aucune autre : (i) dans le poste, la ligne
`d = [o for o in d if cout(o) <= 1.6]` devient `d = [o for o in d if cout(o) <= 1.4]` (une seule occurrence de
`cout(o) <= 1.6` exigée) ; l'en-tête ajouté au poste de relance dit que le plafond est de 1,4 USD/h par cet addendum et que
les commentaires d'origine qui citent 1,6 ne sont pas mis à jour ; le lecteur des pièces vérifie qu'aucune ligne
exécutable ne porte plus 1.6 ; (ii) dans la conduite de relance, une garde d'entrée de plus, jouée avant toute création :
cet addendum scellé, à l'empreinte fixée à la génération, sinon « rien ne tourne » ; garde éprouvée sur un cas sain et sur
un artefact (R5). Les gardes d'entrée de l'addendum 7 (empreinte de l'addendum 7, GO qui la cite) restent telles quelles.
Aucun module de `src/` ne change.

Indication, sans valeur de règle : avec une destruction de 61049303 avant ≈ 10:50Z le 18 novembre, la règle donne K ≥ 71
si elle est calculée au plus 0,75 h après la création de l'instance neuve et si le taux relevé c est d'au plus
1,40 USD/h (le plafond porte sur `cout` de l'offre, non sur c relevé ; à 1 h de mise en place, le seuil tombe à ≈ 10:34Z ;
une mise en place refaite, texte l. 363, abaisse K d'autant) ; à une
destruction plus tardive, K peut tomber sous 71 même à 1,40 USD/h : la session le constate au calcul de la règle (champ
technique) et la relance est lue selon le texte et l'addendum 7 (régime réduit si 20 ≤ K′ ≤ 70, non retenue).

## 3. Risques déclarés
- Aucune offre à 1,40 USD/h ou moins dans les 24 h : relance non courue ; verdict retenu : celui à 36 tours (§ 3 de
  l'addendum 7).
- Moins d'offres conformes qu'à 1,6 : délai possible avant la création. Ce délai n'entre pas dans D et n'abaisse pas K
  (61049303 est détruite avant le lancement du poste de relance ; rien ne court entre sa destruction et la création de
  l'instance neuve ; `Poste.depense`) ; il consomme la fenêtre de 23 h 45 et rapproche l'échéance du GO. Seul un retard de
  la destruction de 61049303 abaisse K (≈ 1,32 USD par heure dans D).
- La relance reste comptée au plein taux pour les heures d'arrêt de 61049303 (texte), ce qui surestime D de ≈ 18 USD
  pour une destruction vers 09:00Z (≈ 15,3 h d'arrêt depuis 17:41:51Z, à 1,3248 − 0,1528 USD/h ; relevé
  `runs/temoin-bailey-v1-20261111/releve-stockage-61049303-20261118-0152.txt`, `002b9f58…`) ; règle de prudence gardée
  telle quelle.

## 4. Contre-lecture
Deux agents neufs du modèle Fable 5.2, autre que l'auteur (N-052), sur le commit `f7cef9ba` (workflow
`contre-lecture-addendum-8-bailey`, run `wf_0f91ed95-f16`) : angles « fidélité et méthode » et « calculs et mise en
œuvre » ; verdicts « scellable après corrections », aucun bloquant. Vérifié par eux : fidélité au mot « B » (A non retenu,
rien d'autre sur le fond) ; correction déclarée postérieure au constat ; constat fait des seuls champs techniques ;
défendable sous R3 (resserrement du filtre, ne vise aucun signe), avec la réserve de rapporter l'écart et sa cause ;
table du § 1 recalculée, quinze cases exactes, seuil de 10:50Z exact sous ses hypothèses ; une seule occurrence de
`cout(o) <= 1.6` dans le poste v13. Corrections reprises avec leurs textes : délai d'attente hors de D (§ 3) ; deux
différences dans les pièces, dont la garde d'entrée de la conduite (§ 2) ; reste du § 2.4 sans lui prêter la borne de
23 h 45 ; hypothèses du seuil de 10:50Z ; effet sur le verdict retenu et objet déclarés (en-tête) ; périmètre (mise en
place refaite, aucun retour à 1,6, mot de lancement distinct) ; remarques : condition « moins de 20 tours », commentaires
périmés du poste, source du « ≈ 18 USD ». Non vérifié par eux (cloisons) : `lancer-conduite-v15.py`, le générateur v3 (à
contre-lire à part) et l'heure 17:44Z. Aucun constat écarté.
