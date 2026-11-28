# Jury de l'addendum de P3 — angle : fidélité au brouillon 1 et au verrou unidirectionnel

Juge neuf. Je n'ai écrit ni le brouillon ni aucun candidat. Texte de référence : brouillon 1
(`P3-addendum-lecture-complementaire-v1-brouillon1.md`), comme le demande la consigne.

## Verdict

- Gagnant : **b** (8,5/10). Le plus fidèle à la lettre : noms des réserves, population de A8, garde du second
  passage, arrêt écrit après le manifeste, lecture décisive lue sans valeur devinée, verrou contrôlé sur la sortie.
- **a** (7/10) : noyau statistique aussi juste. Il est meilleur sur deux points : aucun repli silencieux, et A5 qui lit la
  vraie règle de `lire_action`. Il s'écarte de la lettre sur une dizaine de points, tous réparables.
- **gemini** (0/10) : fichier de tests absent (règle de la consigne : note 0). De plus, le module ne s'analyse pas :
  `IndentationError` à la ligne 332 (`base = {` décalé d'une espace). Une seule fonction vaut une greffe.

## Ce que j'ai fait

- J'ai lu en entier le brouillon 1, les deux modules, les deux fichiers de tests et le noyau de Gemini. J'ai relu le code
  gelé utile : `lecture.py`, `statistiques.py`, `conditions.py`, `notation.agreger_par_jeton` et
  `propositions.lire_action`.
- Empreintes de b vérifiées : module `8f2410f5…6dc9`, tests `7a3684e1…1e25`, égales à celles annoncées.
- J'ai lancé les tests sans les modifier. Je n'ai écrit ni cache ni bytecode, et les fichiers temporaires sont restés dans
  `rapports/jury-fidelite-essais/`. Résultats : a, 61 réussis en 107 s ; b, 60 réussis en 299 s.
- J'ai écrit trois sondes, sous `rapports/jury-fidelite-essais/` (`sonde_replis.py`, `sonde_lecture.py`,
  `sonde_lecture_b.py`). Leurs constats sont reproduits ci-dessous.
- Durées annoncées par les candidats, que je n'ai pas remesurées : a, 438 s pour 2 400 actions, 430 sondes et 2 000
  tirages ; b, 332 s. Les deux restent sous les 30 minutes.

## Notes

| Candidat | Note | En une ligne |
|---|---|---|
| b | 8,5 | Fidèle à la lettre presque partout ; verrou vérifié sur la sortie ; liste d'arrêt complète et testée. |
| a | 7 | Noyau juste, aucun repli silencieux, A5 plus juste que le texte ; plusieurs écarts à la lettre. |
| gemini | 0 | Tests absents ; module qui ne s'importe pas ; noyau A1 à A4 sans réserves ni verrou. |

## Analyse par analyse (a contre b)

Sur les points suivants, les deux candidats sont conformes : clés de graines `addendum/<analyse>/<sonde>/<objet>`,
effectif minimal de 10 de chaque côté, plus de 1 % de tirages dégénérés écrit « échec », intervalles percentiles,
`np.quantile` par défaut, et score d'empan toujours par `agreger_par_jeton`. Jamais de moyenne ni de médiane sur les
jetons d'une action. Les moyennes que l'on trouve portent sur des aires de répliques (A2 (b), en descriptif) ou sur des
actions (A8), jamais sur des jetons.

- **A1.** Conformes tous les deux. Ils couvrent les cinq jeux, T1 et T4 (tranches de la lecture, figées puis prises dans
  le tirage). Niveau : 97,5 % pour saboteur contre honnête, 95 % sinon. La règle de réserve est câblée dans les deux sens
  (« Δ_bas ≤ 0 » sur les jeux qui doivent être au-dessus, « Δ_bas > 0 » sur témoin contre honnête et mention contre
  honnête), et chaque cible est la bonne : sonde retenue, P3-P4, T3, T1, T4.
- **A2.** Conformes : (a) aire du champ du coût par `intervalle_blocs` ; (b) répliques R = 50, départs uniformes, tout le
  pré-coût si c ≤ L, réplique b mod R ; (c) et (d) en descriptif.
  - (d) : b compare l'aire du coût au quantile du plancher, ce que dit le texte. a compare la borne basse.
  - a n'écrit la réserve « non lue » que si aucun contrôle n'est contraire. b écrit chaque sous-contrôle non lu.
  - Les deux lisent A2 à 95 %. Le texte est ambigu sur ce point (constat RA-08) ; les deux candidats le sont de la même
    façon.
- **A3.** Conformes : mêmes tâches tirées, 95 %, et les bornes hautes de la lecture sont reprises en descriptif.
- **A4.**
  - (a) Conformes : tranches recalculées dans chaque tirage. Réserve si « borne basse interne ≤ quantile observé » ou si
    « Δ_T4,bas ≤ 0 ».
  - (b) Les deux restent exposés au poids k² d'une tâche tirée k fois (RA-06), que le texte ne règle pas. a tire
    seulement parmi les tâches mixtes : aucun tirage n'est alors sans paire, et la clause « au plus 1 % de tirages sans
    paire » ne peut jamais jouer. b tire parmi toutes les tâches de T1 : la clause a un sens, et un test l'exerce. Sur ce
    point, b est plus fidèle.
  - (c) Conformes. b prend la référence exacte `10 ** cout_de_tache()['valeur']`, la fonction gelée (RA-22).
- **A5.**
  - Le texte prête à `lire_action` une règle fausse (RA-01, bloquant). b applique cette règle à la lettre et ajoute en
    descriptif les désaccords de *présence* du champ selon le vrai `lire_action`. Il manque les désaccords de *position*
    (par exemple « *COST: » ouvert, suivi d'une seconde ligne COST).
  - a calcule trois positions : `bornes_champs`, la vraie règle de `lire_action` (avec une garde : la valeur lue est
    égale à `lire_action`) et la règle du texte. Il compte une divergence selon l'une ou l'autre. Son T2_propre exclut
    donc un peu plus que la lettre, mais il couvre la vraie source d'écart.
  - Sort de T2_propre quand il n'est pas lu. b : « non calculable » donne `reserve_A5_bornes_T2` et « échec » donne
    `reserve_A5_non_lue`, à la lettre. a range les deux sous `reserve_A5_bornes_T2`.
- **A6.** Conformes : textes valides ; les actions invalides gardent le coût de la table, la population est donc
  inchangée (prudent face à RA-09). Les deux visent P3-P2 et la mention par une conclusion « sans gonflement » lue dans
  la lecture (borne basse ≤ 0). C'est une interprétation commune et raisonnable d'un texte muet sur la cible.
- **A7.** Conformes et identiques. Prédicteurs ajoutés, marge à la borne basse si l'aire de la sonde dépasse 0,5,
  corrélation de rangs chez l'honnête ≥ 0,50, réserve seulement sur un jeu à l'état « au-dessus ».
- **A8.** Le texte dit « pour chaque action notée et localisée ». b applique la règle de `lecture._localisation` et exige
  10 actions de chaque côté. a prend toutes les actions notées (sonde : 1 600 sur 1 600) et ne prend la part par champ
  que sur les bornes lisibles. C'est un écart à la lettre, même s'il évite la sélection signalée par RA-18.
- **A9.** Conformes : descriptive, aucune réserve possible, six paires de conditions. Chaque candidat a un artefact qui
  vérifie qu'aucune réserve n'est levée.

## Synthèse mécanique et verrou

Aucune voie de promotion chez a ni chez b. Une réserve sur une conclusion non établie est refusée par construction : chez
a dans `_Entree._ajouter` et `_synthese`, chez b dans `exiger_verrou`. Un contrôle favorable à une conclusion non établie
n'est écrit qu'en descriptif.

- **Noms des réserves.** Le texte nomme `reserve_<analyse>_non_lue`, et le brouillon 3 garde ce nom. b le respecte. a
  écrit `reserve_<analyse>_non_lu`, vérifié par sonde. Un sous-agent du verdict qui cherche le nom écrit ne trouverait
  pas les réserves de a. Tous les autres noms sont exacts chez les deux.
- **`issue_primaire_inchangee`.** Copie, puis comparaison canonique, chez les deux. Les deux testent la garde avec une
  copie altérée : b remplace `_copie_issue` ; a altère la sortie, puis fait toucher l'issue par une analyse. Aucun des
  deux ne recalcule la ligne d'issue à partir des états (RA-04 reste ouvert).
- **Verrou vérifié sur la sortie.** b relit chaque conclusion de sa table et vérifie que son état est celui de la lecture,
  et qu'aucune conclusion non établie n'est qualifiée. C'est plus mécanique que la liste `promotions: []` de a, qui ne
  peut que rester vide (RA-05).
- **Risque de lecture « robuste » (RA-23).** b écrit pour chaque conclusion établie sans réserve « établie au sens de la
  lecture décisive ; aucune réserve de l'addendum ». Le texte ne prévoit pas cette mention. a n'écrit rien dans ce cas.
  Point mineur contre b.
- **Réserve générale.** Unité : a compte les entrées (analyse par sonde) entièrement en échec ; b compte les analyses qui
  ont au moins un sous-contrôle en échec. b colle à « plus de la moitié des analyses » ; le texte reste flou (RA-19).
- **Composition.** b propage les réserves des composantes (T1 à T4 et le jeu saboteur contre mention vers « intention » ;
  le jeu saboteur contre honnête vers la sonde retenue). Utile au verdict ; absent chez a.

## Clés lues dans la lecture décisive (« aucune valeur devinée »)

- b vérifie le type : un booléen attendu qui n'en est pas un, un état inconnu ou un jeu sans `aire`, `bas`, `haut` et
  `plancher_quantile` arrêtent l'addendum (sonde : `GardeArret`).
- a lit `etabli = "oui"` comme faux, sans arrêt (sonde). C'est une valeur devinée : elle supprime une réserve. Un jeu
  sans `aire` fait lever `KeyError`, au lieu d'une garde avec son motif (sonde).
- Concordance de la lecture avec le run source (RA-03, en partie). b recalcule l'aire et le quantile du plancher de
  chaque jeu, de T1 et de T4, et les compare à ceux de la lecture à 1e-9 près (14 contrôles, écart ≤ 1e-12 sur le cas
  sain). a ne le fait pas. En revanche, a vérifie que sa localisation est égale à celle de `lecture._localisation`
  (lignes, pré-coût, coût), ce que b ne fait pas.

## Liste d'arrêt

| Garde du texte | a | b |
|---|---|---|
| Run source ou lecture non vérifiables : arrêt sans sortie | oui | oui |
| Entropie autre (fonction pure et ligne de commande) | oui | oui, plus l'entropie citée par le préenregistrement de P3 |
| Préenregistrement de l'addendum non scellé ou non conforme | oui (non testé de bout en bout) | oui, testé |
| Module autre que celui cité | empreinte présente dans le texte | chemin et empreinte, et module à son chemin ; testé avec un module modifié |
| Code gelé de P3 modifié | oui (non testé) | oui, testé (« arbre gelé ») |
| État introuvable : arrêt | oui, sauf jeu sans `aire` (`KeyError`) et booléen deviné | oui, typé |
| Échec d'une analyse écrit, réserve générale au-delà de la moitié | oui | oui |
| Second passage sur le même run : nœud de Lazar | clé (run source, lecture) : même run source et autre lecture accepté (sonde) | clé run source, conforme ; mais un manifeste illisible est sauté sans motif (sonde) |
| Arrêt après le manifeste, motif écrit | non : manifeste laissé sans sortie ni motif | oui, `arret-addendum-p3` scellé, testé |
| Nom du run de l'addendum `AAAAMMJJ-HHMMSS-addendum-p3` | garde présente | absente |

**Replis silencieux** (règle du programme) :
- b : `_vers_json` change une valeur non finie en `None` sans motif (sonde) ; la garde du second passage saute un
  manifeste illisible.
- a : une valeur non finie dans la sortie devient un « échec » écrit avec son motif ; un manifeste illisible arrête.

## Tests demandés par la consigne

- Sain, artefact, dégénéré et verrou pour A1 à A9 : présents chez les deux. Chez a, les artefacts de A3 et de A4
  (tranches) sont des artefacts « de lecture » (conclusion forcée). b produit plus souvent un vrai artefact de données
  (A4 tranches, A8 saturation, A2 longueur). Les deux forcent la lecture pour A3.
- Transverses :
  - Déterminisme octet pour octet : les deux. Entrées non modifiées : b vérifie le run source et la lecture ; a seulement
    la lecture.
  - Entropie refusée dans la fonction pure et dans la ligne de commande : les deux.
  - Issue inchangée et garde sur copie altérée : les deux.
  - Score d'empan au maximum : les deux.
  - Aire vectorisée à 1e-12 près, ex aequo compris, contre `aire_sous_courbe` et `aire_stratifiee` : les deux.
  - R5 pour chaque garde, sur un cas sain et un artefact :
    - b couvre le run source, la lecture, la cohérence lecture contre source, les textes, l'agrégation, le verrou, le
      tokeniseur par caractères et la garde d'import.
    - a couvre le run source, la lecture, les textes, l'agrégation et le verrou. Il n'a pas de cohérence lecture contre
      source.
  - Ligne de commande de bout en bout dans un dépôt git jetable :
    - b fait les quatre volets : gardes d'avant le manifeste sans sortie, passage scellé et rattaché, second passage
      refusé, arrêt après le manifeste avec son motif.
    - a fait les trois premiers. Il n'a pas l'arrêt après le manifeste. Il ne teste ni le préenregistrement non scellé,
      ni le module modifié, ni l'arbre gelé modifié, ni le run source altéré.
- Données : b relit toutes les mesures par `mesures_action`, comme le demande la consigne. a relit seulement le coût, le
  coût aux milliers joints et la validité ; les autres mesures restent celles de `_source`.

## Greffes utiles pour la synthèse (base : b)

1. **a `_localisation`** : la garde d'égalité avec `lecture._localisation` (lignes, pré-coût, coût). Elle prouve que A2,
   A5 et A7 portent sur les actions mêmes de T2 décisif (R5, RA-13).
2. **a `_propre`** : remplacer `_vers_json`. Une valeur non finie devient une garde avec son chemin, jamais `None` en
   silence.
3. **a `exiger_premier_passage`** : un manifeste illisible arrête. Garder la clé de b (même run source, `commande` du
   module).
4. **a `position_cout_lire_action` et `_vers_brut`** : position réelle du champ du coût selon `lire_action` gelé, avec
   une garde d'égalité de la valeur. À ajouter à A5 de b comme second compte de divergence. Il couvre RA-01, que la
   lettre du brouillon 1 ne couvre pas.
5. **a `RUN_ADDENDUM`** et la vérification du manifeste du run source (décisif, mode réel) dans `executer`.
6. **a, tests `test_verrou_controle_contraire_sans_conclusion_etablie`** (paramétré sur tous les artefacts) **et
   `test_verrou_controle_favorable_a_une_conclusion_non_etablie`** (paramétré sur A1 à A8, lecture où rien n'est
   établi). Ils vérifient le verrou de façon systématique.
7. **gemini `_verifier_params_bootstrap`** : gardes des paramètres (tirages ≥ 1, niveau et quantile dans ]0, 1[, part de
   tirages dégénérés dans [0, 1]). Ni a ni b ne les ont. À tester sur un cas sain et sur un artefact (R5).

À corriger dans b sans greffe :
- retirer la qualification « aucune réserve de l'addendum », ou la remplacer par une mention neutre (RA-23) ;
- compter aussi les désaccords de position du vrai `lire_action` (voir la greffe 4).

## Constats R2 qui touchent le code, et qui les traite

| Constat | a | b |
|---|---|---|
| RA-01 (règle de `lire_action`) | traité (trois règles) | lettre seule, présence en descriptif |
| RA-03 (lecture décisive, même run source) | en partie | en partie, plus la concordance des aires ; unicité et antériorité ouvertes chez les deux |
| RA-04 (garde de l'issue) | testée par copie altérée | testée par copie altérée ; recalcul de l'issue absent chez les deux |
| RA-05 (verrou sans forme) | garde interne, liste vide | table des conclusions vérifiée sur la sortie |
| RA-06 (poids k² en A4 (b)) | ouvert ; clause du 1 % vidée | ouvert ; clause du 1 % lue |
| RA-11 (empreinte du module) | empreinte | chemin et empreinte |
| RA-13 (alignement des textes) | traité | traité |
| RA-14 (second passage) | clé trop étroite | conforme |
| RA-19 (échec borné) | seules les gardes sont rattrapées | seules les gardes sont rattrapées |
| RA-23 (« robuste » par défaut) | rien n'est écrit | mention positive à retirer |

Point ouvert hors de mon angle : la synthèse suivante doit s'aligner sur le brouillon 3. Celui-ci garde
`reserve_<analyse>_non_lue` et la règle du second passage. Le reste, je ne l'ai pas comparé ici.
