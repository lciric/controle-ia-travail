# Mandat du rédacteur du plan : brouillon 4, voie (iii), 39 adaptateurs (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 21:55Z. Pièce de travail. Destinataire : le rédacteur Fable 5.2 qui a écrit les brouillons 2 et 3, la fiche V-B1 et les couples du code.

---

## Ce que Lazar a tranché (GO-2026-11-19-79, `registres/go.md`)
Ta fiche V-B1 est tranchée selon tes recommandations :
- **39 adaptateurs** : un sur-saboteur par famille d'apprentissage ;
- **voie (iii)** pour le texte ;
- **formation le 23 novembre**, même si le texte n'est scellé que le 22 ou le 23. Le code exige le texte scellé (ligne `SCELLEMENT-B5F`) avant toute création d'instance : le scellement doit donc précéder le lancement du 23.

Rien n'est dépensé : l'accord de calcul de la formation se demandera sur ton devis final.

Restent en attente de Lazar. Écris le texte de façon qu'il tienne sous l'une ou l'autre réponse :
- le plafond si 39 adaptateurs : (a) garder 200 USD, défaut sous 48 heures, ou (b) 205 ;
- l'accord d'avance de la relance : une dépense, sans défaut ;
- le comptage facultatif : défaut (b), non.

## Ce que tu écris
Le brouillon 4 du texte, de son devis, et la table de ses corrections. Il intègre :
1. **La voie (iii)** de ta fiche (`fiche-decision-v-b1-lazar-v1.md`, `78cadfd2…`) :
   - la sonde est apprise sur le sur-saboteur contre le jumeau ;
   - l'épreuve à poussée égale oppose les deux membres édités ;
   - l'étalon de la poussée est le saboteur ;
   - réécris l'hypothèse, les épreuves, les critères de lecture et la phrase que le mot dirait au jury ;
   - garde les deux réserves communes déclarées : la trace propre au sens de l'édition, et les produits des déplacements moyens.
2. **Les couples de la vérification du brouillon 3** (`verification-plan-brouillon3-v1.md`, `a1b2250d…`), tous ceux qui valent sous la voie (iii), dont le constat majeur V-M1. Dis lesquels la voie (iii) rend sans objet.
3. **Tes couples du code** (`couples-du-code-pour-brouillon4-v1.md`, `1e929542…`), groupes 1 et 2 : 39 adaptateurs est acquis.
4. **La vérification des corrections du code** (`code-formation/verification-corrections-code-formation-v1.md`, `3517677f…`), § 7 et § 8 :
   - **Remèdes au plafond des actions non éditables.** Ses remèdes 1 (« un nombre collé à une lettre n'est pas compté », sans toucher au lecteur gelé) et 2 (« 2k » écrit en clair) diffèrent des tiens (deux paliers ; « k » non éditable). Choisis et motive. Les deux peuvent aussi se combiner.
   - **Borne des relances (n-4).** Il recommande que la relance vive sous le plafond commun, et que le code refuse ce qui le dépasse. Ton couple C-2b la met hors du plafond, à la coupure de l'instance remplacée. Tranche, motive, et dis ce que cela demande à Lazar en dépense.
   - **Sa remarque sur la voie (iii)** : les écritures propres à un sens (« 1000 » sans séparateur chez le sur-saboteur ; mantisses 3, 6 et 1,5) pèsent plus quand la sonde s'apprend sur les deux sens. Dis ce que le texte en fait.
5. **Le rapport v4 du développeur**, en cours ; la mère te donnera son empreinte dès qu'il sera scellé. Il décrit ce que le code fait déjà, et ce qu'il faudrait changer, pour : les paliers, la copie `-x1`, la borne des relances, les remèdes « A100 » et « 2k », et les instances 6 et 7 à trois membres.
   - Commence par ce qui n'en dépend pas : l'hypothèse et les épreuves de la voie (iii).
   - Marque chaque phrase qui suppose un comportement du code « [à confirmer par le rapport v4] » jusqu'à ce que tu l'aies lu.
6. **Écart à déclarer** : la mère a fait lire au développeur des corrections, par programme, les énoncés des tâches de réserve, pour l'essai à blanc du tokeniseur (R-3953). Ton point 1 et ton point 7, cinquième tiret, ne le permettaient pas à la lettre. Rien n'a été affiché ni gardé. Écris-le dans le texte comme écart déclaré, à l'endroit qui convient.
7. **Le nom final.** Le texte scellé portera un nom sans « brouillon », par exemple `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` ; le code refuse un nom qui contient « brouillon ». Écris le texte pour ce nom final. Le brouillon 4, lui, garde son nom de brouillon.
8. **Les rôles.** La liste « qui a lu quoi », version 13 (`registres/qui-a-lu-quoi-v13.md`, `ffc4420e…`, lignes 262 à 312 et réserve 24), dit qui a lu des résultats de l'étape B bis. Les rôles de ton texte (lecteurs, juges, ouverture du 26) doivent rester attribuables : nomme les exclusions, ne nomme pas de personne.

## Sorties (scellées, non commises)
- `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-brouillon4.md`
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/table-corrections-plan-brouillon4-v1.md` : chaque changement, avec sa source (couple, constat, voie).
- Tes simulations neuves, s'il en faut, sous des noms neufs dans le même dossier, avec leurs sorties.
- `docs/notes/barreau5-resolution-v1/plan-avant-entretien/fiche-v4-lazar-v1.md`, une page, qui donne :
  - les décisions qui restent à Lazar, chacune avec son défaut ;
  - le devis final résumé, pour l'accord de calcul de la formation.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.

## Règles
- Les mêmes que tes mandats précédents.
- Aucune donnée ni aucun résultat : rien de `diag/`, aucun score, aucune transcription, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ou de P3-bis.
- Aucun fichier « consigne-privee » ou « conception-ii-b » ; rien sous `/root/.claude/`.
- Aucun réseau ni aucune dépense.
- **Tes fichiers seulement par les outils d'écriture et d'édition**, programmes de calcul compris. Tu as dérogé une fois à cette règle : ne le refais pas.
- Aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande.
- Au premier refus d'outil, arrête-toi et dis-le.
- Aucun nombre de résultat d'expérience close dans ton rendu.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Tes sorties, avec leurs empreintes.
3. Dix lignes au plus :
   - ce que la voie (iii) change ;
   - tes choix sur les remèdes et sur la borne des relances ;
   - les phrases encore marquées « à confirmer » ;
   - ce qui menace le scellement avant le 23.
