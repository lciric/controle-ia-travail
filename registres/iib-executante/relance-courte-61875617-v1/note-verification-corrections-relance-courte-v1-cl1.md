# Vérification des corrections : relance courte de la machine 61875617 (contre-lecteur 1, classe B)

Contre-lecteur : Claude Opus 5.5, le même que la contre-lecture 1. Heure : 2026-11-22, vers 11:50Z. Aucun appel au vrai loueur, rien poussé.

## Verdict

**Jouable après une seule correction, R1 (deux lignes du script, ci-dessous) ; non jouable en l'état.** Tous les points de la contre-lecture 1 sont corrigés, dans le texte comme dans le script. J'ai rejoué moi-même les essais à blanc, avec mon propre faux outil : ils sont conformes. Reste un retard possible sur le chemin critique de l'arrêt (R1).

## Empreintes (vérifiées, conformes à l'annonce)

- `texte-relance-courte-61875617-v1-brouillon2.md` : `9910804f985248c8497d4bf8081d8fbee8457953701c22d6fc67d92a2a058df0`
- `relance-courte-61875617-v1.sh` : `60ab98446da60e9eb4662bd88a8416589f32911f481eaff6bbb84e83fb70295c` (même valeur citée dans le texte, l. 6 et 80)
- `essais-blanc-relance-courte-v1.txt` : `12080c540cab00e8cca81b23cc9861466c9d9f7a3c433d93374563841e54ece3`
- `differences-brouillon1-vers-2.md` : `3750ccee7f10845730b1d55766dd9f0cbd486484eb07d5c1618b3dacbaf5c0a4`

## Points de la contre-lecture 1

| point | texte | script | état |
|---|---|---|---|
| B1.1 — code de sortie de `logs` lu ; illisible si code non nul, fichier vide ou masquage en échec | § 4 | l. 75-80 | corrigé |
| B1.2 — trois illisibles de suite : arrêt | § 4 | l. 17, 86 | corrigé |
| B1.3 — état lu à chaque tour ; `running` vu sans ligne « DEMARRAGE 2 » après 60 s : arrêt ; 900 s pour la seule mise en marche | § 4 | l. 13-14, 81-83, 87-88 | corrigé |
| B1.4 — un relevé toutes les 5 s | § 4 | l. 12, 91 | corrigé |
| B1.5 — essais j7 et j8 | § 5 | — | joués (voir plus bas) |
| M1 — plus d'arrêt à la tentative 1 ; ordre : poussée faite, poussée impossible, refus, chemins, calcul | § 4, § 10 (l. 211), N2 | l. 23-29 (motif « tentative » absent) | corrigé |
| M2 — préalable P10 (latence d'arrêt mesurée à 12:54Z, au-delà de 90 s : mot de Lazar) et nœud N7 | l. 74, 197, 208 | — | corrigé |
| M3 — méthode inchangée | — | — | conforme |
| m1 — `mkdir "$D2"` sans `-p` | l. 59 | l. 60 (refus si `D2` absent) | corrigé |
| m2 — essais isolés, faux outil, `D2` propre à chaque essai | § 5 | — | corrigé |
| m3 — traces et inventaire limités aux chemins ajoutés | l. 179-182 | — | corrigé |
| m4 — interprète `$DEPOT/.venv/bin/python` | l. 169 | — | corrigé |
| m5 — inventaire brut réduit par le lecteur (`_remplacer`), supprimé en échec | — | l. 32-36 | corrigé |
| m6 — P7 dit de quel jeton il s'agit | l. 71 | — | corrigé |

## Script relu ligne par ligne

- Les appels au loueur sont `start`, `logs`, `stop` et `show instances`. `start`, `logs` et `stop` visent tous la constante `ID_ATTENDU=61875617` ; `show instances` est une lecture sans identifiant, réduite par le lecteur à la seule machine 61875617.
- Aucun `destroy`. `ID` ≠ 61875617 ou identifiant intouchable : refus (l. 58-59).
- Un seul `start`, gardé par `start-fait` (l. 61, 66). Deux `stop` au plus (l. 41, 50). Aucune boucle de relance.
- Bornes tenues : 900 s pour la mise en marche, 60 s en marche sans ligne « DEMARRAGE 2 », 1080 s pour l'issue, 2100 s au total. L'heure limite (19:40Z le 23/11) n'est remplaçable que par une variable d'essai (l. 11).
- Le code de retour dit si l'arrêt est confirmé (l. 85-96). La garde des secrets n'imprime qu'un nombre (l. 98-111).

## Essais à blanc rejoués (dossier neuf `scratchpad/verif-cl1-essais/`, mon propre faux outil)

Le faux outil note chaque appel, refuse `destroy` et tout identifiant autre que 61875617, et rejoue des états et des journaux par appel. Tous les essais sont lancés avec `PAS_S=0`. Résultats :

| essai | résultat | appels |
|---|---|---|
| A, sain | arrêt confirmé sur « poussée faite », code 0 | 1 start, 1 stop |
| A, second `jouer` | refus, code 2 | aucun appel neuf |
| B, tentative 1 refusée puis poussée | relevé 2 `DEMARRAGE`, relevé 3 arrêt sur « poussée faite » | — |
| C, `logs` en code 1 trois fois | arrêt sur trois illisibles | 3 logs, 1 stop |
| D, en marche, pas de démarrage 2, `BORNE_RUN_S=0` | arrêt | — |
| E, ligne de poussée de la branche v5 | pas reconnue, arrêt sur la borne totale | — |
| F, poussée impossible, arrêt jamais confirmé | arrêt non confirmé, code 1 | exactement 2 stop |
| G, identifiant 58936096 | refus | aucun appel |
| H, `running` avant le start | refus | aucun start |
| Garde des secrets, fichier sain | 0 | — |
| Garde des secrets, faux `ghp_` | 1, code 1 | — |

Aucun appel interdit sur l'ensemble des essais. Les résultats concordent avec `essais-blanc-relance-courte-v1.txt`.

## Reste

- **R1 (à corriger avant de jouer)** : dans la boucle, `etat` (`show instances`, délai de 120 s) est appelé **avant** l'arrêt décidé sur `L` (l. 81 puis l. 85). Une lenteur du loueur au relevé de la poussée retarde l'arrêt jusqu'à 120 s, sur une fenêtre de 180 s. Correction exacte :
  1. insérer `case "$L" in ARRETER*) echo "$(date -u +%FT%TZ) relevé $n : $L" >> "$D2/veille.txt"; arreter "$L"; RC=$?; break;; esac` juste après l. 80 ;
  2. passer `timeout -k 5 120` à `timeout -k 5 30` pour l'appel `show instances` de la boucle (par exemple un argument de délai à `etat`, 30 dans la boucle, 120 ailleurs) ;
  3. passer `timeout -k 5 60` à `timeout -k 5 30` pour `logs` (l. 75 ; l'outil abandonne de lui-même vers 9 s).

  Cela fait rejouer A, B, C et F.
- R2 (mineur, à la discrétion de la mère) : des illisibles pendant la mise en marche (`scheduling`) arrêtent et consomment le start unique. C'est sans perte (le conteneur n'a pas tourné), mais la relance est perdue. Correction possible : ne compter `ILL` qu'une fois `RUN_VU` posé ; avant, la borne de 900 s suffit.
