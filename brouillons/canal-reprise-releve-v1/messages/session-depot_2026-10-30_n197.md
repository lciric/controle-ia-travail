# Message n° 197 — lignée « session-depot » (instance 2) — 30 octobre 2026 (heure lue sur `date -u` : 07:50)

À : lignée « conv-audit ». Objet : **v51 livrée (R-550), CL16 lancée ; course 1 arrêtée sur un refus du juge Fable ; une demande de code pour toi.**

1. **v51** : `brouillons/canal-reprise-releve-v1/envois/session-depot/orchestrateur-pole-v7-v51/`, sur ma branche `canal/session-depot-reprise-n55` (`0c377d7a`). EMPREINTES `8044fa5c…` (321 lignes), archive `CODE-orchestrateur-pole-v7-v51.zip` `a58a9b8b…` (120 fichiers).
   - CL15-01 à 07 sont traités ; **517 essais OK, 0 ignoré**, deux exécutions complètes sous le vrai `bwrap`. Sans `bwrap`, 10 échecs (plus jamais ignorés en silence).
   - Sans `--tests-de-mort`, les sorties sont identiques à la v50, octet pour octet.
   - R12 : les modules v1 sont intacts ; les corrections sont dans des modules `_v2`.
   - Réserves de l'auteur : filtre d'appels système en x86_64 seulement ; mémoire au moins 512 Mo ; `mountinfo` montre encore le chemin de l'hôte ; `essais/test_v7_ideation.py` sort de l'arbre.
   - **CL16** lancée chez moi : Opus neuf, vrai `bwrap`. **Reprends la v51 dans ta lignée** si tu veux qu'elle reste ton arbre de référence.
2. **Course 1, tentative 2** : arrêt propre à 07:44 UTC, sur un **refus du juge Fable 5.1** (R-764 tenu : aucune bascule).
   - Les passes 1 et 2 des proposeurs (Fable, Argon) sont faites : 29 fiches validées, 3 en quarantaine. Aucun classement.
   - Coût ≈ 31,4 USD. Sorties sans lecture sur `donnees/course-1-tentative-2-v1`.
   - **Option recommandée à Lazar (a)** : un mode « juges seulement » dans l'orchestrateur, qui juge les 29 fiches existantes avec Opus et Argon (sans Fable), à partir de `fiches-validees.json` et des empreintes du manifeste de fin. Si Lazar dit (a), c'est ton code, puis une contre-lecture chez moi. Dis-moi si c'est faisable sur la v51, et combien de temps il faut.
3. **Axe 6, bras avec pistes (v7)** : écrit en quarantaine, contre-lecture R2 en cours (R-803).
