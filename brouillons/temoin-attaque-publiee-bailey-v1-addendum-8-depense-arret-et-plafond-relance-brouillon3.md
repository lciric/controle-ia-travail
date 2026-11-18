# Addendum 8 au préenregistrement du témoin de Bailey — dépense des heures d'arrêt de 61049303 et plafond de coût de la relance de la confirmation — brouillon 3

18 novembre 2026. Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`). **Brouillon : sans effet tant que
Lazar n'a pas choisi et donné son mot (écart à un préenregistrement scellé : nœud).** Brouillons 1 et 2 gardés tels quels
(R12) ; le brouillon 3 applique la vérification adverse du brouillon 2 (deux relecteurs neufs, run `wf_dbe9e067-a3f`).
Le texte (`fb6c2f34…`) et les addenda 1 à 7 restent tels quels ; en cas de conflit, le texte prime et l'écart est un
nœud. **Écrit avant toute lecture** : aucune note de sonde ni de juge du témoin n'a été lue, par aucune session.

## 1. Pourquoi
La confirmation (addendum 7, `554a74d0…`) s'est interrompue le 17 novembre : compte Vast sans crédit, instance 61049303
arrêtée par Vast ; conduite finie à 17:44Z, instance gardée arrêtée, « reprise requise »
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v15/bilan-conduite-v5.json`). Le run principal compte moins de
20 tours complets (≈ 16 attendus ; établi par la reprise). La liste d'arrêt permet une relance (texte l. 371), par le
chemin de l'addendum 5 (addendum 7, § 2.1), sur le même poste de dépense (D cumulée, même B = 85 : texte l. 252-254 et
371 ; addendum 7, § 2.1 et 2.2) ; le garde-fou d'entrée de l'addendum 5 s'applique sans changement.

Le texte définit (l. 252-254) : « c : taux réel de l'instance en cours, carte et stockage ; D : dépense du poste […],
toutes instances comprises, chacune comptée à son taux réel × heures écoulées de sa création à sa destruction, à
l'horloge » (CL3-2, accepté mot pour mot). Le code suit ce texte (`lanceur_v21.Poste.depense`, l. 709-712 : un c par
entrée ; la conduite v15 a écrit une seule entrée pour 61049303). Les heures où 61049303 est arrêtée sont donc comptées au
taux de marche (1,3248 USD/h), alors que Vast ne facture alors que le stockage : `storage_total_cost` 0,1528 USD/h,
`intended_status` « stopped » (relevé `runs/temoin-bailey-v1-20261111/releve-stockage-61049303-20261118-0152.txt`,
`002b9f58…` ; 110 Go à 1,0 USD par Go et par mois de 720 h). Règle de prudence pensée pour une instance en marche : sur les
heures d'arrêt, elle compte ≈ 8,7 fois la dépense de carte et de stockage.

K de la relance (`_relance_seule` : `analyse_v3.nombre_de_tours(85, D, c, 1265.0215)`, D arrondi à 4 décimales ; une
confirmation n'est retenue qu'à K′ ≥ 71, addendum 7, § 3) :

| D compté | c de l'offre (USD/h) | reprise vers 09:00Z | vers 12:00Z | vers 18:00Z |
|---|---|---|---|---|
| texte actuel (plein taux à l'arrêt) | 1,33 | 72 | 71 | 57 |
| texte actuel | 1,40 | 72 | 68 | 54 |
| texte actuel | 1,60 (plafond du § 2.4) | 65 | 59 | 47 |
| A ci-dessous | 1,33 à 1,60 | 72 | 72 | 72 |

(D de 61049303 compté de sa création à sa destruction, prise à l'heure de la reprise, plus 0,75 h de mise en place au
taux c. Ligne A : arrêt daté à 17:41:51Z et reprise en marche d'au plus 1 h. Sans A, K ≥ 71 jusqu'à une reprise vers
12:23Z à 1,33 USD/h, 10:50Z à 1,40 et 06:23Z à 1,60.)

## 2. Écarts proposés (Lazar choisit A, B, A et B, ou aucun : relance au texte actuel ; son choix est consigné avant la génération des pièces de relance et avant la création de l'instance)
**A (recommandé). Heures d'arrêt de 61049303 au taux du stockage.** Pour la seule instance 61049303 (première exécution
de la confirmation) et pour le seul calcul de D par les pièces de la relance (garde B − 2, seuil local, veilleur, chien
de garde, règle de `_relance_seule`), D compte 61049303 en trois intervalles, chacun à son taux × ses heures à
l'horloge :
1. de sa création (1794907209.2755258, `poste-v5.json`) à T_a, au taux c de sa création (1,3247777777777778 USD/h, celui de
   la règle) ;
2. de T_a à T_r, au taux du stockage s ;
3. de T_r à sa destruction (`bilan-reprise-v10.json`, champ `destruction`), au taux c.

T_a = 1794937311.9679263 (17 novembre, 17:41:51Z) : champ `t` de la dernière ligne de
`sortie-conduite-v15/conduite-v5.jsonl`, écrite par `_finir` après la lecture du statut « exited » (alerte du bilan) :
premier instant où l'arrêt est établi ; le premier sondage en échec (17:12:11Z) ne date pas l'arrêt et n'est pas retenu.
T_r : champ `redemarrage.debut` du bilan scellé de la première reprise qui la redémarre (`bilan-reprise-v10.json`, écrit
avant l'ordre de démarrage), retenu seulement si le champ `statut` de ce bilan vaut « stopped » ou « exited ». s : le plus
haut des relevés de `storage_total_cost` de 61049303 consignés avant le scellement de cet addendum (relevé cité au § 1 :
0,1528 USD/h), avec `intended_status` « stopped ». D reste une borne prudente de la dépense de carte et de stockage :
l'arrêt est daté au premier instant où il est établi (avant, 61049303 est comptée à c), le redémarrage avant l'ordre de
démarrage, le taux de stockage relevé chez le loueur. Toute autre heure de 61049303 (reprises suivantes, nouveaux
arrêts), toute heure de toute autre instance du poste (instance de la relance comprise, même arrêtée) et la borne de
budget de la reprise (`Reprise._borne_budget`) restent comptées selon le texte (l. 252-254). Si T_a ou T_r ne peut être
établi ainsi, si T_a ≥ T_r, ou si s n'est pas consigné avec sa source, A ne s'applique pas : plein taux, comme le texte.

Mise en œuvre : pièces neuves contre-lues (R2), seules changées : générateur
`docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v3.py` (la v2 reste telle quelle,
R12), qui écrit `lancer-conduite-v16.py`, `poste-hetzner-v14.sh` et `construire-donnees-demarrage-v14.py` (la v2 n'en a
produit aucun dans `runs/`). Il écrit trois entrées de même identifiant dans les instances antérieures, dans l'ordre
chronologique, toutes de B = 85 : (`61049303`, c, création, T_a), (`61049303`, s, T_a, T_r), (`61049303`, c, T_r,
destruction) ; la conduite v16 vérifie, avant toute création, la contiguïté des trois intervalles, T_a contre la dernière
ligne de `conduite-v5.jsonl`, T_r, le statut et la destruction contre le bilan scellé de la reprise, et `poste-v5.json`
(entrée unique : création, c, destruction du bilan de la reprise). Aucun module de `src/` ne change :
`instances_du_poste` accepte plusieurs entrées de même identifiant ; `verifier_relance_seule` lit la dernière (au c de la
règle) et sa borne d'entrée tient (11,08 USD de marche avant T_a, contre 10,53 USD au plus pour K′ = 19) ;
`Poste.depense` et `Poste.d_avant` somment les entrées.

Seuils inchangés (B = 85, B − 2, seuil de secours B − 0,5, R, échéance). Effet déclaré : D de 61049303 est compté plus
bas de (c − s) × (T_r − T_a), ≈ 18 USD pour une reprise vers 09:00Z (≈ 21,5 USD vers 12:00Z) ; la garde B − 2, le seuil
local, le veilleur et le chien de garde arrêtent donc la relance plus tard qu'au texte : desserrement de fait de la garde
de dépense de la relance, déclaré ici. La dépense réelle de carte et de stockage du poste reste sous D ≤ B − 0,5 =
84,5 USD (addendum 7, § 2 bis).

**B (en option).** Pour la seule relance : coût de l'offre (carte et 110 Go, grandeur `cout` du choix d'offre) d'au plus
1,40 USD/h au lieu de 1,6 (addendum 7, § 2.4). Mise en œuvre : le générateur v3 remplace, une seule occurrence exigée,
la ligne `d = [o for o in d if cout(o) <= 1.6]` du poste par `cout(o) <= 1.4` ; le reste du § 2.4 est inchangé (24 h,
offre la moins chère qui passe). B ne s'applique que si Lazar le choisit ; si Lazar choisit A seul et que A ne s'applique
pas, B ne s'applique pas. Avec A, B n'est plus nécessaire pour K ; il réduit la dépense attendue et le nombre d'offres
conformes.

Tout le reste du texte et des addenda 1 à 7 s'applique sans changement : graines, critères gelés, liste d'arrêt, règles
de lecture de l'addendum 7 (aucune note lue avant la clôture ; lecture par `lecture_scellee_v3`).

## 3. Risques déclarés
- A est un écart à une définition du texte (D, l. 252-254) et, par elle, à la ligne « Dépense du poste, comptée comme D,
  ≥ B − 2 USD » de la liste d'arrêt (l. 368 ; CL3-2), décidé avant toute lecture ; il ne joue que sur la dépense et le
  nombre de tours, jamais sur la lecture ; il est rapporté comme écart avec le verdict de la confirmation.
- D reste une borne de la dépense de carte et de stockage, comme dans le texte ; la bande passante n'y entre pas. Après
  la destruction de 61049303, la session relève la facture de cette instance chez le loueur et la consigne dans
  `registres/depenses.md`, sans effet sur la conduite.
- Sans A, la relance n'est plus retenable (K < 71) pour une reprise après ≈ 10:50Z à 1,40 USD/h (≈ 12:23Z à 1,33 ;
  ≈ 06:23Z à 1,60) ; la session la proposerait alors à Lazar comme non lancée.
- Aucune offre conforme dans les 24 h (avec B : ≤ 1,40 USD/h) : relance non courue ; verdict retenu : celui à 36 tours.

## 4. Contre-lecture
Vérification adverse du brouillon 2 : run `wf_dbe9e067-a3f` (deux relecteurs ; deux bloquants : datation de l'arrêt,
segments ; points à corriger : périmètre, mise en œuvre, effet sur la garde, source du taux, table, seuils, B). Tout est
repris ; écart : pour les trois entrées, l'identifiant commun (relecteur « mise en œuvre », vérifié dans le code) est
retenu plutôt que des identifiants distincts (relecteur « texte et règles »). Contre-lecture (R2) du brouillon 3 à faire,
puis scellement après le mot de Lazar.
