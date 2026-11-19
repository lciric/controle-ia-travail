# Vérification de la ligne 3, version 5 — compte rendu d'un vérificateur arrêté au premier refus d'outil — v1

**Provenance.** Le vérificateur (agent neuf du modèle O, qui n'a écrit aucune version) s'est arrêté au premier refus d'un outil, comme son mandat le demandait, et n'a pas écrit sa pièce. Ce texte recopie son compte rendu final, sans rien changer au fond, par la session du compte organisme (2026-11-19, vers 16:45Z). **Ce n'est pas une vérification scellable** : le verdict est provisoire, deux contrôles ne sont pas faits.

**Le refus.** Sa dernière commande groupait trois contrôles : l'empreinte de `registres/go.md` au commit `2ec5da6c…`, la tête de main, et l'empreinte du fichier des cartes sous `archives-reponses-modeles/`. La garde l'a refusée pour accès non autorisé. Calculer l'empreinte du fichier des cartes allait contre son mandat (« rien sous archives-reponses-modeles/ ») ; il le reconnaît comme sa faute. Aucun contenu n'a été lu ni affiché ; il n'a pas réessayé. Les deux autres contrôles de cette commande ne sont donc pas faits.

## Fait avant le refus (lecture seule, processeur seul)

- **Empreintes** : les cinq pièces à vérifier et toutes les références sont égales aux préfixes donnés ; les 28 compagnons du dossier répondent « OK ».
- **Différentiel par programme** : 24 morceaux pour le préenregistrement, 8 pour le devis, comme le dit le rapport du rédacteur. Hors un point (correction 3), chacun vient d'une des neuf corrections, des quatre conditions, des deux décisions de Lazar, ou d'un ajout déclaré. Le devis est propre.
- **Neuf corrections** : vérifiées par programme ; chaque texte neuf présent une fois, l'ancien disparu (seules restent des citations historiques dans les tables) ; justes.
- **Calcul des prédictions** : joué deux fois ; sorties égales entre elles et à l'octet à la sortie versée (`2cf1eba7…`) ; le calcul v1 rejoué rend sa sortie (`d0ea8984…`) ; clé par clé, rien de retiré, « version » changée, une clé ajoutée.
- **Deux bascules recalculées** par un programme à lui, sur des formules écrites à la main : 0,38527 (suiveur séduisant) et 0,54375 (lecteur séduit), concordantes avec 0,3853 et 0,5438.
- **Décisions de Lazar** : portées comme le dit GO-2026-11-19-77 (Q4, lecture par colonne ; devis § 6 bis).
- **Conditions de cloisonnement (1) à (4)** : écrites (garde de recouvrement, Q3, liste d'arrêt, annexe A) ; la condition (4) suit la lecture confirmée par la mère.

## Verdict provisoire, non scellable : « Scellable après corrections »

1. **Repli sur les sept cartes** (section « Garde de recouvrement », puce « Repli » ; Q3 ; liste d'arrêt). Les trois conditions de la mère manquent, et les trois endroits ne disent pas le même déclencheur. Remplacer la puce par : « Repli, écrit d'avance. Il se déclenche par une règle mécanique, sans que personne ni aucun agent regarde une carte : refus écrit de la mère avant le scellement de la banque, ou contrôle du (4) rendu « non conforme » par le vérificateur du code de la banque sur un point propre à l'entrée des 94 cartes. Il ne vaut que pour les sept cartes nommées à l'en-tête, extraites du même fichier par le même programme, aux mêmes règles : empreinte du fichier vérifiée, lecture par programme seulement, champ `meta` retiré au chargement, aucun bardeau ni texte de carte écrit, sortie à la même liste fermée. L'écart (garde sur sept cartes au lieu de 94, et sa cause) est déclaré au manifeste et au rapport de la garde. Empreinte du fichier autre que `ba65c411…` : ni garde ni repli ; la banque n'est pas scellée et la mère est saisie. » À Q3, la phrase « Si l'une de ces conditions ne peut pas être tenue, ou si la mère refuse … écart écrit au manifeste. » devient : « Si la règle de repli écrite à « Garde de recouvrement » se déclenche, la garde est jouée sur les sept cartes nommées, aux mêmes règles de lecture, écart déclaré au manifeste. » À la liste d'arrêt, « (Q3) » devient « (règle de repli, « Garde de recouvrement ») ».
2. **Trou de la condition (3)** : rejouer la garde sans limite sur un témoin récrit en fait un oracle d'appartenance sur des phrases des cartes. Ajouter à la fin du (3) : « Le nombre de rejeux de la garde est au rapport ; au-delà de cinq rejeux, aucun rejeu de plus sans le mot de la mère, saisie avec les seuls comptes. » Ajouter à la liste du (4), après « d'un texte de carte » : « , messages d'erreur et traces d'exception compris ».
3. **Morceau non déclaré** (en-tête, auteur). La citation de la règle de l'allègement a été changée de « par le même contre-lecteur » en « par le modèle du contre-lecteur » ; ce changement ne vient pas de la correction 9 et n'est pas à la table du différentiel. Rétablir : « (règle de l'allègement, classe A : contre-lecture, puis vérification des corrections par le même contre-lecteur ; ici par un agent neuf du même modèle, écart déclaré) ».
4. **Forme** (P5 quater). Sur la grille, le mot change entre deux pas. Remplacer « à δ = 0,385 » par « entre δ = 0,385 et 0,386 (bascule 0,3853) », et « à δ = 0,544 » par « entre δ = 0,543 et 0,544 (bascule 0,5438) ».

**Ajouts non demandés** : les artefacts de cloisonnement, la phrase sur ce que sait le rédacteur des fragments et le rappel du § 10 sont utiles et gardés ; le repli est gardé sous la correction 1.

## Non fait

L'empreinte de `registres/go.md` au commit `2ec5da6c…` et la tête de main. La pièce de vérification elle-même. Une vérification complète reste à faire, par un agent qui ne touche pas à `archives-reponses-modeles/`.
