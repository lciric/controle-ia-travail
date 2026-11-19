# Passation du compte organisme — complément — version 2

Écrite à 2026-11-19T15:28:28Z (`date -u`). Elle complète la passation v1 (`registres-provisoires/passation-compte-organisme-2026-11-19-1453-v1.md`, `011879e0…`), qui reste en place (R12). La nouvelle mère tourne sur un autre compte (`session_01XJ6Mgr8BN6UanALsQatc5E`) et écrit seule les registres de `main` ; la mère sortante n'écrit plus dans `registres/`. Ce compte verse tout sur `lot/compte-organisme-v1` ; toute décision passe par Lazar.

## Ce qui a changé depuis la v1

| chantier | fait | pièce (branche `lot/compte-organisme-v1`) | reste |
|---|---|---|---|
| Orchestrateur v68 | contre-lu **« Conforme. »** (Sonnet 5.5 en repli, refus de Fable écrit en tête) ; précision non bloquante : le refus du moteur réel couvre `--course-2` ; sans cette option, le lanceur passe la main au v8 inchangé | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/contre-lecture-orchestrateur-v68-v1.md`, `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325` (`304b770e`) | lanceur v11, additif des interrupteurs ; fiche unique des quatre décisions pour Lazar (activation ; ce qui est servi ; champs de fiche ; machine jetable) : **à la nouvelle mère** (R-3894) |
| Statistique de famille | contre-lue **« Scellable. »** (Sonnet en repli) ; 29 essais | `…/juge-selection/contre-lecture-statistique-famille-rejeu-v3-v1.md`, `e10aa0ed8561cd9bb5dd263d7f84207d40caebb91fd98e1e59941fc0495b0fdc` (`223cfadc`) | seuil 0,05, minimum de 3, Holm : « à confirmer » par le rédacteur Fable ; la mère écrit la correspondance et lance le programme après le rejeu v3 |
| Ligne 1, code du banc A | écrit (`43bb7deb`, fusion `831a7fc2`), 42 essais, fumée 45 s ; contre-lu **« Conforme. »** (Sonnet en repli) | code sous `…/ligne-1-effort-recherche/code/` ; rapport `…/code-v1/rapport-developpeur-banc-a-v1.md` (`af2fc6d6…`) ; commande `…/code-v1/commande-lancement-banc-a-ligne1-v1.md` (`98405802…`) ; contre-lecture `…/code-v1/contre-lecture-banc-a-ligne1-v1.md`, `056465db863f9821606a1d4e13cf351445acbde1bb2202a344f5bce165119fe2` (`a236efd7`, fusion `3de85da9`) | **ADDENDUM COURT AU PRÉENREGISTREMENT PAR LE RÉDACTEUR FABLE** (R-3901) fixant les cinq choix non fixés (rapport § 4.1 à 4.5 ; avis du contre-lecteur : tous gardables tels que codés, aucun ne change une règle ; **4.4 à confirmer d'abord**, seul choix qui change les sorties au bit près) et la réserve de la porte A15 (écart attendu 0,086 pour une porte à 0,1, arrêt improbable ; si elle tire : arrêt nommé, retour à la mère, sans modification du code) ; scellement de l'addendum par la mère ; puis lancement détaché (≈ 1 h sur 4 processus) ; journaux ≈ 400 Mo compressés selon R-3851, un morceau à la fois |

## Réserves du contre-lecteur du banc A, à porter au lancement (aucune ne touche le code)

1. Écrire `>> "$D/lanceur.log"` plutôt que `>` (une reprise tronquerait le journal du lanceur).
2. Avant toute reprise, vérifier que les PID de `pid-*.txt` ne vivent plus (rien n'empêche deux lanceurs simultanés).
3. Pour l'audit de symétrie, recalculer M1-nul des courses 0, 300 et 599 depuis les décisions du journal (le rejeu A16 réexécute les fonctions sans relier le journal à la sortie brute).
4. Les gardes A7 et A11 passent par la ligne 0 de la table (leurs classes d'exception ne sont jamais levées) : à dire dans l'addendum.

## Écarts déclarés par les agents depuis la v1

Heredocs sans effet de fichier (un chez le développeur du banc A, deux chez le contre-lecteur du banc A, deux chez le contre-lecteur de la v68), chacun écrit dans sa pièce. Aucune dépense, aucun appel externe, aucun refus de permission.

## Plus rien ne tourne dans l'ancienne session

Les agents du banc A et des contre-lectures ont tous versé. La file de conception attend Fable (remise annoncée le 22 novembre à 18:00 UTC) ou une session sur un compte où Fable a des crédits.
