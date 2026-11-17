# Devis de la machine du crible (iii) — v1

- **Objet** : la part hors crédits du crible (iii), ligne κiii2 proposée par la pièce qui fera foi (`crible-iii-version-foi-v1.md`,
  `91b4bf30…`, « Lignes de GO proposées ») : **machine jetable seule, 3 USD au plus** ; ce devis ne change ni ce plafond ni aucun
  autre chiffre de la pièce (les attendus de la pièce restent les siens : 0,07 USD attendus pour la machine, § 5 de sa sortie de
  devis) ; il dit ce que la procédure `procedure-machine-crible-iii-v1.md` fait de ces 3 USD, et pourquoi l'attendu y est plus haut
  que celui de la pièce (la pièce ne compte que la file de quatre mondes et le temps hors appels du pilote).
- **Écrit** : 2026-11-17 (`date -u`), sans aucun appel au loueur ni à un fournisseur ; durées locales mesurées sur le conteneur de la
  session (chargé par d'autres sessions, quatre processeurs) ; aucune dépense.

## 1. Bornes (gardes de la procédure)

| poste | borne | garde qui la tient |
|---|---|---|
| offre | prix garde (prix total + stockage de 20 Go) ≤ 0,15 USD/h ; au moins 4 cœurs, 8 Go, 20 Go, 100 Mb/s, fiabilité ≥ 0,98, amd64, carte admise et inutilisée | `garde_session_crible_iii_v1.py offre-depuis-recherche` (chaque offre jouée, la moins chère acceptée) |
| prix relu après création | ≤ 0,17 USD/h, sinon destruction aussitôt | `relire` |
| durée | minuterie à 17 h après l'impression de la commande (l'amorce refuse au-delà de 17 h 05) ; destruction par la session dès un état final, au plus tard à l'échéance plus cinq minutes | amorce (minuterie), § 4 geste 18 |
| dépense | chaque heure : cumul + une heure au prix relu ≥ 3 USD → destruction | `depense` |
| **pire cas** | **17 h × 0,17 USD/h = 2,89 USD**, sous la part de 3 USD | — |

Trafic réseau : prix du réseau de l'offre lus et consignés au geste 7 ; octets du crible : quelques dizaines de Mo (paquet de l'arbre,
dépôt partiel, `pip`, poussées) ; à 0,0 à 0,02 USD/Go (offres ordinaires), sous le centime.

## 2. Attendu

| phase | durée attendue | pire (bornes de la procédure) | source |
|---|---|---|---|
| mise en place (création, `pip`, pièces, arbre) | 10 min | 25 min | pilote v14 ; `pip` borné à 900 s |
| barrière 1 (phrase de Lazar) | 15 min | 60 min | attente bornée de la machine |
| vingt mondes (quatre processus) | 20 à 45 min | ≈ 2 h 30 sur un hôte chargé | quatre mondes de développement générés ici, un processus, `nice` : 185, 138, 186 et 507 s (le dernier après deux tirages refusés) ; moyenne 254 s ; 20 × 254 s / 4 ≈ 21 min |
| barrière 2 | 5 min | 20 min | attente bornée |
| préparation et essai à blanc sur les vrais mondes | 3 min | 15 min | essai à blanc local : `preparer` de 3 s pour quatre devis distincts ; 100 appels factices en 10,6 s à cinq files |
| barrière 3 | 5 min | 20 min | attente bornée |
| crible réel | ≈ 36 min (28 à 44) | 8 h (4 × 7 200 s) | pièce, « Mise à jour d'après le pilote, appliquée » |
| mesure, lecture, rapatriement, poussée | ≈ 30 min (mesure ≈ 25 min : étiquettes C8 de vingt devis en quatre processus, attribution d'≈ 500 cartes ; lecture, rapatriement, poussée ≈ 5 min) | 2 h (marge comprise dans la garde de départ de 10 h) | essai à blanc local (§ 3) |
| **total** | **≈ 2 h 10** | 17 h (minuterie) | |

**Attendu** : ≈ 0,11 USD au prix relu au pilote (0,052222 USD/h × 2 h 10), ≈ 0,33 USD à la borne de l'offre (0,15 USD/h) ; la pièce attend 0,07 USD (file de quatre mondes et temps hors appels du pilote seulement : ni la génération des vingt mondes, ni les barrières, ni la mesure) — information, le plafond de 3 USD tient. **Pire** : 2,89 USD. La garde de départ (10 h avant l'échéance au départ du crible réel) laisse 7 h aux
phases qui précèdent (pire ci-dessus : 25 + 60 + 150 + 20 + 15 + 20 min ≈ 4 h 50) ; la fin la plus tardive (≈ 4 h 50 + 8 h + 2 h = 14 h 50) tient sous les 17 h.

## 3. Mesures locales reprises

- Génération de quatre mondes de développement (graine `graine_monde_crible`, secret nul, phrase publique, empreinte nulle ; un
  processus, `nice -n 19`, conteneur chargé par d'autres sessions) : 185,2 s, 137,8 s, 185,8 s, 507,1 s (deux tirages refusés
  en C6 avant le troisième) ; empreintes des devis `cb6bbc51…`, `77b4196f…`, `62b65dab…`, `d6b5e0c8…` ; ces mondes ne servent
  qu'aux essais.
- `preparer` sur vingt mondes (quatre devis distincts, chacun servi cinq fois) : 2,9 s ; G0 de 48 584 à 48 662 octets, G1 de
  48 510 à 48 588, pire G2 de 49 159 à 49 237 (sous 53 000).
- Crible à blanc complet (relais factices, commande et gardien du pilote, cinq files) : 100 appels en 8 à 11 s.
- Mesure du crible à blanc (quatre devis distincts, 480 cartes, C8 en quatre processus) : ≈ 8 min 40 s ; à vingt devis
  distincts, la part C8 est ≈ cinq fois plus longue : ≈ 25 min estimées sur quatre processeurs.

## 4. Ce que ce devis ne couvre pas

- La part sur crédits (κiii1 : 260 USD au pire, 160,87 attendus ; κiii0 : 7 USD au pire, 3,03 attendus) : inchangée, celle de la
  pièce.
- La latence et la limite de débit chez le fournisseur à vingt sessions à la fois (le pilote a joué en série) : la ligne « limite de
  débit » de la liste d'arrêt la garde ; une concurrence refusée allonge le crible sans changer la borne de 8 h.
- Le prix réel facturé : console du loueur, lue par Lazar.
