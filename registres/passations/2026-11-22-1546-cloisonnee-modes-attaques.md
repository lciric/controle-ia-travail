# Passation — session cloisonnée du collisionneur « modes de sabotage » et « attaques » — 2026-11-22T15:46Z

Écrit à 2026-11-22T15:46:34Z (`date -u`). Classe C. Session opératrice cloisonnée (Opus 5.5), ouverte par la session mère. Mandat : `docs/notes/collisionneur-modes-et-attaques-v1/mandat-session-cloisonnee-modes-et-attaques-v1.md` (fa3e8e05478e59daa5eedf72ba53d495795fe2d1d35a200bf48f6a3058692859, vérifiée), sous GO-2026-11-21-08 (échéance le 28 novembre). Arrêt sur l'ordre de Lazar (15:43Z, relayé par la mère : « arrête tout et fais la passation … on n'a plus de crédits ici »). **Cloisonnement : aucune course n'a eu lieu, aucune sortie de modèle n'existe ; cette passation ne porte que des noms, des empreintes, des statuts et des montants.**

## Fait
- Pièces vérifiées par empreinte : mandat (fa3e8e05…), devis v4 (2073265f…), devis v3 (fadb7d09…), questions v3 (8a043ad3… ; a64d9b21…), moteur v8m (420394f9…), voie abonnement v5 (523bb5ac…), recueil v6 (432b20a3…), branches de kits (fafd6864…).
- Registres lus sur les points 1 à 15 du devis v3, § 6 (go.md, decisions.md).
- **Garde de motifs du moteur** (`garder_motifs` du v8m, sans dossier) : **REFUS des deux questions**, catégorie « chemin interne » seule. Questions « modes de sabotage » : 6 occurrences, première au caractère 421 ; questions « attaques » : 5 occurrences, première au caractère 498. Aucune autre catégorie. Arrêt selon le mandat (§ 2, point 2) et la condition de départ de GO-2026-11-21-08. Rien n'est réécrit.
- **Fable 5.1 en session fille : possible.** Essai neutre (« Réponds seulement par le mot : prêt. »), sans dépôt, effort xhigh, ajout système du mandat : session session_01XJ6MgqGVeYDLmGWfYmRXHD, **archivée**. Un seul modèle servi (claude-fable-5-1), end_turn, un tour, aucun outil, coût théorique 0,35 USD (abonnement, non facturé). Limite hebdomadaire de l'abonnement en avertissement (« allowed_warning »).
- **Épreuve de Carbon : non lancée.** Constat hors réseau (commande devis du moteur, clés retirées de l'environnement) : le moteur refuse une seule espèce (« au moins deux espèces », code 1) ; le pire cas d'un appel de Carbon au tour III.1 est de 2,33 USD, au-dessus du plafond propre de 2,20 du mandat (le 2,20 vient du devis v3, provision 32 768 ; le v8m porte 49 152). Options remises à la mère : (1) Carbon et Astra, plafond 2,90, recommandée ; (2) Carbon et Argon, plafond 4,00 ; (3) pas d'épreuve.
- Point 11 du devis v3, § 6 : deux options écrites à la mère, en deux lignes chacune, tirées du seul devis. Lecture des points 1, 10, 12, 13, 14 et 15 donnée à la mère, à confirmer par Lazar.
- `.venv` monté sans paquet (le moteur n'emploie que la bibliothèque standard et `src/`), non versé.

## Inventaire (tout ce qui existe)
| objet | lieu | taille | sha256 | statut |
|---|---|---|---|---|
| texte neutre de l'épreuve de Carbon (entrée, aucune question, aucun mode) | `docs/notes/collisionneur-modes-et-attaques-v1/epreuve-carbon-entree-neutre-v1/question-neutre-epreuve-carbon-v1.md` | 7 989 caractères, 8 249 octets | b00803af235bdf595c1ad01f774ebf93d296ccbfbcd051139a2bf1f3661c638e | versé, scellé ; garde de motifs passée ; jamais envoyé |
| programme de la garde des questions par le moteur | même dossier, `garde_questions_par_moteur_v8m_v1.py` | 764 octets | 758a845e2f310770fdc1ee01a68c35404f528e18e9c08e3394bee24ddfc5feb4 | versé, scellé (outil de travail, classe C) |
| copie hors dépôt du texte neutre | `~/collisionneur-modes-tenus-a-l-ecart-v1/epreuve-carbon-entree-neutre-20261122/` | même fichier | b00803af… | perdue avec le conteneur ; la copie versée fait foi |

Aucun dossier de passage, aucun kit, aucune branche `coffre/…`, aucune réponse de modèle, aucune fiche, aucune note de sortie.

## Dépense
- GEMINI_API_KEY : 0 USD. OPENAI_API_KEY_2 : 0 USD. Clé d'Anthropic : aucune employée. Abonnement : un essai neutre, 0,35 USD théorique, non facturé.

## Reste (dans l'ordre, après le mot de Lazar)
1. Questions v4 sans chemins (proposition de la mère : seuls les renvois « docs/… » remplacés par des mots neutres), contre-lues par un agent Opus neuf qui ne les a pas écrites, garde de motifs passée, devis rejoué. Rien n'est écrit avant son mot.
2. Point 11 du devis v3 tranché (option (a) ou (b)) ; si (a), ce couple entre dans les v4.
3. Épreuve de Carbon : option choisie parmi (1), (2), (3).
4. Puis le mandat à la lettre : inscription à la liste « qui a lu quoi », épreuve, deux passages, mot de Lazar **dans la session cloisonnée** pour pousser les branches de kits et le coffre, trieur, note de sortie, passation.

## Réserves
- Inscription à la liste « qui a lu quoi » non faite (elle se fait avant le lancement). Pour mémoire, cette session a lu : le mandat, les devis v3 et v4, les deux questions v3 (aucun mode dedans), le moteur, la voie abonnement, le recueil, les registres go.md et decisions.md, la note de périmètre des modes inédits v3. Aucune sortie de modèle de ce chantier ; aucun moniteur conçu.
- Le plafond de 2,20 USD de l'épreuve, repris par le devis v4, ne tient pas sous le v8m : à recalculer dans tout ordre neuf.
- Le script de vague (`vague_abonnement_v1.sh`) écrit son journal sous `docs/notes/…` dans le dépôt : pour une course cloisonnée, en prendre une copie qui journalise hors de l'arbre.

## Prochaine action
Attendre le mot de Lazar sur les points 1 à 3 du « Reste » ; une session cloisonnée neuve (ou celle-ci, si elle vit encore) reprend au point 4.

## Instances actives
Aucune instance de calcul. Sessions filles : une seule, l'essai neutre, archivée.
