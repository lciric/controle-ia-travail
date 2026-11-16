# Contre-lecture du crible (v), tour 6 de la numérotation de la pièce (tour 3 de ce lecteur) — brouillon 6

- Lecteur : sous-agent neuf, modèle C. Je n'ai écrit ni la pièce, ni ses brouillons, ni les corrections, ni les rapports précédents.
- Lecture de 14:47:29Z à 14:52Z (`date -u`). Aucun appel de modèle, aucune dépense, aucune machine ; rien lu sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote non ouverts ; issue et taux du pilote non lus ; dossiers jetables du premier lecteur non touchés.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-v-brouillon6.md`, empreinte `08b430d7ec9cc4b7435dd46c772b0e56cc92a1630e945e38f46d1ec7d97624d6` (égale à son compagnon `.sha256`).
- Version précédente : `crible-v-brouillon5.md`, `c28731169bb25537441e5b3c8918ad3871f961afa7027e9a57ee432246c70118`. Rapport précédent : `contre-lecture-crible-v-b4-tour2-v1.md`, `0152b7f4baceb9d089651287ede102c7bafda05a4c87e92d0aece7efa5207c2a` (empreinte vérifiée, égale à celle que la pièce cite).

## Verdict

**corrections.** L'application des sept couples B5-01 à B5-07 est **fidèle** et le différentiel ne contient **rien d'autre** que les couples propres que la pièce nomme. Aucune majeure : la conception tient et aucune porte ne s'ouvre après lecture du crible. Mais les trois réserves que le rédacteur de la pièce a lui-même relevées « pour le tour 6 » sont de vraies lacunes d'écriture dans des règles gelées (sources des durées du budget, mesure du placebo, durée « relevée » de l'attendu), et la tolérance de Pr-1 est mise dans la mauvaise ligne de GO. **0 majeure, 6 mineures (D6-01 à D6-06), 4 remarques facultatives.**

## 1. Application du tour précédent

- Les sept couples du rapport (B5-01, B5-02, B5-03, B5-04, B5-05, B5-06, B5-07) ont été extraits du rapport par programme et appliqués au brouillon 5 : chaque « ancien » figure **une seule fois** (comptes 1 1 1 1 1 1 1), aucun chevauchement. Le texte obtenu comparé au brouillon 6 par `diff` ne laisse que les couples propres déclarés : titre, ligne « Brouillon 6 » de l'en-tête, statut et statut-tour, validateur, tête de la section « Contre-lecture », entrée « Contre-lecture 5 ». Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt. **Application fidèle, rien d'autre.**
- L'entrée « Contre-lecture 5 » cite l'empreinte entière du rapport (`0152b7f4…`, vérifiée par `sha256sum`) et celle du brouillon 5 relu (`c2873116…`, vérifiée) ; ses comptes (2 majeures, 5 mineures, 3 facultatives) sont ceux du rapport.
- Écart de rôle à R-2982 (corrections appliquées par un rédacteur du modèle C), **déclaré** dans la pièce ; voir point pour la mère 2.

## 2. Points que les corrections ont pu déranger, refaits

- **Validateur** : `controle_ia.prereg.problemes` rendu sur la pièce : liste vide (aucun défaut). Aucun identifiant de modèle (seules les clés de configuration `opus55` et `fable52`, déclarées comme noms gelés par l'empreinte de la configuration, comme aux tours précédents).
- **Empreintes citées** : les 16 pièces citées qui sont sur la branche courante (note des idées originales `2f6a69dd…`, décisions N-044, N-045, N-053, N-058, N-067, relevé, catalogue, question de la course, faits du collisionneur, verdict de v67, conception du monde riche v4, deux préenregistrements modèles, gabarit, validateur) ont leur empreinte égale à celle de la pièce par `sha256sum` ; les quatre programmes et sorties de comptes (points 11 et 12 de l'annexe A) aussi. Procédure v14 au commit `2d35cafa…` : empreinte `2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a`, égale à celle citée.
- **Étage 0 (B5-03)** : les 21 lignes de la liste d'arrêt ont maintenant chacune une case (arrêt, défaut, run invalide, refus avant tout dossier, interdit à l'étage 0 ; trois exclusions nommées ; « exception de la mesure » couverte par « mesure en erreur »). D'accord.
- **Devis recompté** : 80 appels (96 à 24) ; plafonds du bloc gelé 2,34 ; 2,00 ; 2,34 ; 3,00 (la procédure v14 donne les parts du pilote 9,36 ; 8 ; 9,36 ; 12 pour 4 mondes, soit ces plafonds par session : d'accord) ; pires cas 46,80 ; 40,00 ; 46,80 ; 60,00 ; machine 3,00 (0,15 USD/h × 17 h = 2,55 ; 2,89 à 0,17 : sous 3,00) ; crédits 100,00 ; hors crédits 96,60 ; total 196,60 ; à 24 : 56,16 ; 48,00 ; 56,16 ; 72,00 ; 120,00 ; 115,32 ; 235,32. Part sur crédits 50,86 % (51,0 % à 24). Avec la sonde neuve : 104,39 et 100,28 (+ 4,39 ; + 3,68 : montants cohérents avec la correction B5-05) ; total 204,67. GO-2026-11-15-06 (ligne l. 339) : 247,20 attendus, 1 275 au pire pour les cinq, crédits de Claude au maximum, une ligne « calcul » par crible sur devis refait et contre-lu, « essayés, non adoptés », échéance 30 novembre : la pièce s'y conforme ; (v) seul est à 196,60 (235,32 à 24 ; 204,67 avec la sonde), (iii) à 216,60 selon R-2977 : les deux font 413,20 au pire, loin sous 1 275. Les deux comptes des dollars sont dits (prix public principal ; prix de la configuration en sensibilité ; part de GO jugée sur le compte de la configuration).
- **Décisions de R-2977** (ligne relue) : archive réduite à K1, mondes séparés, dollars au prix public, GO valable pour l'essai non l'adoption, partie A permise et descriptive sur données déjà vues sans verdict du juge, 24 mondes sous 0,95, tension avec N-058 à dire à Lazar : toutes présentes dans la pièce (« Choix et doutes », « Écarts », partie A).
- **Annexe A, point 12 (B5-07)** : la phrase ajoutée dit bien le sens de l'erreur (l'illustration ne triple que la génération ; la règle donnerait moins de cases lançables). D'accord ; voir F-D6-1 pour ce que cela implique en chiffres.
- **Texte de la ligne `**`** : la correction B5-04 (recopiée du rapport précédent, donc faute de mon prédécesseur et non du rédacteur) a laissé un `**` d'ouverture sans fermeture dans la phrase du budget de durée (19 marques `**` sur la ligne : nombre impair) : cosmétique mais dans un texte gelé (D6-06).

## 3. R1, R3, N-058, partie A, R7 et R8 (relus en entier)

1. **R1** : hypothèse H-v, H-v-a ; prédictions V1 à V7 avec signe, chiffre, zone de réfutation, confiance ; métrique ; seuils (0,25 ; 0,05 ; W_min ; k_R) ; plan d'analyse et table de verdicts par étage ; liste d'arrêt ; critères gelés ; règles écrites d'avance pour ce qui se refait d'après le pilote (B_a, M, N, montants, tolérance de Pr-1, V1 et V6). Aucune porte de sortie après lecture du crible. Les règles d'avance sont maintenant fermées, sauf les trois lacunes D6-01 à D6-03.
2. **R3** : les deux seuils posés par l'auteur (S_R ≥ 0,25 ; « perte établie » dès W_min = 4 de 16 à 22 mondes, 5 à 23-24 : borne basse de Clopper-Pearson au-dessus de 0,05) sont dits « choix de ce texte, non déduits d'une donnée », posés avant toute donnée, avec leur puissance chiffrée (0,13 ; 0,59 ; 0,80 à p = 0,10 ; 0,20 ; 0,26 sur 20 mondes à risque ; 0,68 sous k_R = 3 ; recomptés par programme, annexe A points 6 et 11 : égaux). Aucune voie vers un signe positif : les deux issues sont chacune une information (N-045 point 3, QO1). Le cas dégénéré (k_R < 4) est défini, gelé et dit en tête (point 7 de « En dix lignes », lecture de H-v, étage 4) : « non éprouvée au crible », jamais « réfutée » ; l'issue « non éprouvable » a sa définition (4 ≤ k_R ≤ n_c − 4) ; le bras à archive enrichie est écarté par la mère (R-2977, point 4 (a)), avec deux sensibilités sans appel de plus. La distance dirigée (de la carte vers K1, non le plus petit des deux sens) est un **écart déclaré** au regroupement de [V3], avec sa raison (« Écarts », « Métrique ») : acceptable comme écart déclaré ; il est contre-lu. Le crible reste informatif : il éprouve surtout l'ablation (H-v-a), ce que la pièce dit en tête.
3. **N-058** : le crible est borné à la génération 1 sur {K1}, aucun verdict du juge n'entre dans la règle ; la dépendance indirecte au-delà est dite (Écarts, point 11) et renvoyée à Lazar pour toute adoption.
4. **Partie A** : déclarée descriptive, sur données déjà vues, sans verdict du juge, sans seuil touché ; l'exception de la liste des retenues est dite et gardée par une ligne d'arrêt (essai sain et artefact). Je n'ai pas ouvert le relevé.
5. **R7, R8** : aucun chiffre de l'état de l'art ; antériorités listées « à chercher » (FrugalGPT, AutoMix, RouteLLM, FunSearch, AlphaEvolve ; voisins [CAT] C9 et CADS), zone dite séduisante donc à vérifier plus durement.
6. **Graines** : `numpy.random.SeedSequence`, racine = entier de l'empreinte, clés `(r, 30)`, `(67, g, 30)`, `(99, b)`, `(97, k)`, `(98, w)` : sans collision ; le placebo sans graine (énumération exacte). R5 : chaque ligne de la liste d'arrêt a son essai sain et son artefact, y compris la branche « tolérée » de la ligne du coût d'un appel, désormais écrite (B5-02, appliquée fidèlement) ; D6-04 corrige seulement l'endroit où elle est dite aux lignes de GO.
7. **Durée** (question de la mère) : la pièce dit sans détour que **le lanceur du pilote est écrit pour 4 mondes et 16 appels, que le lanceur, la mesure, la lecture et la procédure de la machine sont du code neuf, et que la date de lancement en dépend** ; pas de configuration neuve (v12 gardée). Borne par appel B_a (jamais 10 800 s), M mondes à la fois (1 ou 2), budget de pire cas sous 17 h chiffré dans une table et ligne de la règle, « non lançable » en clair. C'est l'ordre B_a, taux, N, M qui reste à jouer sur le pilote.

## 4. Corrections exigées

Chaque « ancien » figure **une seule fois** dans le brouillon 6 (vérifié par programme). Ce sont des écritures, aucune n'ouvre une porte après lecture du crible.

### Mineures

**D6-01 — Sources des durées que le budget lit au pilote.** La règle de B5-01 fait lire au pilote les durées de mise en place, de mesure et de rapatriement (« journal d'états de la machine du pilote »), mais la liste des « Points à remesurer » ne les nomme pas (elle ne nomme que les appels, les mondes et la génération) : la liste des champs permis au lecteur du pilote serait donc plus étroite que la règle gelée. Réserve (1) du rédacteur de la pièce, reprise.

`D6-01`
```
ANCIEN: (6) taille réelle du texte servi ; (7) durée de génération des mondes et prix de l'offre.
NOUVEAU: (6) taille réelle du texte servi ; (7) durée de génération des mondes et prix de l'offre ; (8) durées de la mise en place, de la mesure et du rapatriement, lues dans le journal d'états de la machine du pilote (sans lire aucune issue), chacune prise entre les deux états consécutifs du journal qui la bornent, états nommés dans le texte qui fera foi ; sans état qui la borne, la durée n'est pas relevée et le budget de la section « Devis » est « non lançable », mot de la mère.
```

**D6-02 — Mesure par programme de l'énumération exacte du placebo : ni étape, ni cas mesuré.** B5-01 exige cette mesure « avant le scellement sur N mondes simulés » mais aucune étape ne la porte et « N mondes simulés » laisse le choix de k_R (la durée de l'énumération vaut C(n_c, k_R) : triviale à k_R = 3, 2 704 156 ensembles à k_R = 12 et n_c = 24) : un choix resterait ouvert pour fixer un pire cas. Réserve (2) du rédacteur.

`D6-02`
```
ANCIEN: **Essais** : cas sain et artefact pour chaque ligne de la liste d'arrêt (R5).
NOUVEAU: **Essais** : cas sain et artefact pour chaque ligne de la liste d'arrêt (R5). **Mesure de l'énumération exacte du placebo** (processeur seul, sans appel ni dépense, avant le scellement du texte qui fera foi) : durée du programme de mesure sur N mondes simulés, pour N = 20 et pour N = 24, avec n_c = N et k_R = ⌊N/2⌋ (pire cas de l'énumération : 184 756 et 2 704 156 ensembles), deux lancements, le plus long retenu, sur la machine de développement (le facteur trois de la section « Devis » couvre l'écart avec l'offre de la machine) ; le nombre retenu s'écrit dans le texte qui fera foi.
```

**D6-03 — « Durée relevée au pilote » des appels dans l'attendu de la machine : laquelle ?** La règle (b) du devis refait (B5-06) multiplie ⌈N/M⌉ par « leur durée relevée au pilote » sans dire laquelle (moyenne des appels, plus long appel, plus long appel d'un monde) : un choix resterait ouvert après lecture du pilote. Réserve (3) du rédacteur. Je propose le plus long des quatre appels d'un monde (les quatre partent ensemble), moyenné sur les mondes du pilote.

`D6-03`
```
ANCIEN: et avec les appels à ⌈N/M⌉ fois leur durée relevée au pilote, × prix horaire relu
NOUVEAU: et avec les appels à ⌈N/M⌉ fois la durée moyenne, sur les mondes du pilote, du plus long des quatre appels d'un monde (un appel au-delà de B_a pris égal à B_a), × prix horaire relu
```

**D6-04 — La tolérance de la réflexion de Pr-1 est écrite pour la mauvaise ligne de GO.** La correction B5-02 dit que les lignes « κv1 et κv2 le disent ». Or Pr-1 est sur la ligne κv2 (part hors crédits : `argon`, `astra`, machine) ; κv1 porte `opus55` et `fable52`, pour lesquels la tolérance ne s'applique pas (« appel de Pr-1 » seulement) : lui faire dire « sauf la réflexion de Pr-1 » serait faux. Et κv2 renvoie aujourd'hui à κv1 par « mêmes conditions », ce qui reprendrait « coût au-dessus du pire cas = arrêt » sans exception. Deux couples.

`D6-04a`
```
ANCIEN: et les lignes κv1 et κv2 le disent (« coût au-dessus du pire cas = arrêt, sauf la réflexion de Pr-1 tolérée jusqu'à X fois son plafond »)
NOUVEAU: et la ligne κv2 (part hors crédits, celle de Pr-1) le dit (« coût au-dessus du pire cas = arrêt, sauf la réflexion de Pr-1 tolérée jusqu'à X fois son plafond »), la ligne κv1 restant sans exception
```

`D6-04b`
```
ANCIEN: mêmes conditions que la ligne κv1
NOUVEAU: mêmes conditions que la ligne κv1, sauf « coût au-dessus du pire cas = arrêt », qui reçoit pour Pr-1 la tolérance de la réflexion si la règle de la ligne « coût d'un appel » de la liste d'arrêt la retient
```

**D6-05 — Les lignes de GO proposées ne portent que la branche « sans sonde neuve ».** La règle d'avance (a) dit maintenant que les montants passent à N et à la décision sur la sonde neuve, mais la phrase qui suit les lignes (et les lignes elles-mêmes, 100 et 96,60) ne le dit pas : le lecteur des lignes se tromperait de montant dans la branche « sonde exigée ». Réserve de B5-05 non couverte (« À dire, pour que le lecteur des lignes ne se trompe pas de montant »).

`D6-05`
```
ANCIEN: montants : pires cas (plafonds × N), inchangés par le pilote (règle d'avance du devis refait, section « Devis »).
NOUVEAU: montants : pires cas (plafonds × N), inchangés par le pilote (règle d'avance du devis refait, section « Devis ») ; **les montants ci-dessous sont ceux de la branche « sonde neuve non exigée »** : si elle est exigée (décision écrite avant le scellement), κv1 passe à 104,39 et κv2 à 100,28 USD à 20 mondes (124,39 et 119,00 à 24).
```

**D6-06 — Marque de gras ouverte et jamais fermée dans la phrase du budget de durée (19 marques `**` sur la ligne).**

`D6-06`
```
ANCIEN: M = 1 et M = 2, **plus la ligne de la B_a
NOUVEAU: M = 1 et M = 2, plus la ligne de la B_a
```

(Après ce couple, la marque d'ouverture « **chiffré dans une table » se ferme à « formule** » : 18 marques, nombre pair.)

## 5. Remarques facultatives (non exigées)

- **F-D6-1 — La règle de B5-01 resserre fortement la durée.** Avec les durées que l'annexe suppose (mise en place 0,5 h ; génération 1,0 h à 20 mondes et 1,2 h à 24 ; mesure 1 h ; rapatriement 0,5 h ; barrières 100 minutes) **et le facteur trois sur chacune**, mes comptes à la main (aucune donnée du pilote, hors du programme de l'annexe) donnent : N = 20, M = 1 : B_a au plus 1 140 s, donc 900 s en multiple de 300 s ; N = 20, M = 2 : 2 280 s, donc 2 100 ; N = 24, M = 1 : 860 s, donc 600 ; N = 24, M = 2 : 1 720 s, donc 1 500 (avant la mesure du placebo, qui retranche encore). Comme B_a vaut au moins 1,5 fois le plus long appel répondu, et que v67 a vu 861 s et 1 099 s pour deux appels d'un proposeur (pièce citée, verdict § 4.1), B_a serait de l'ordre de 1 500 à 1 800 s : **M = 2 nécessaire à 20 mondes, et 24 mondes probablement « non lançable »**. La pièce le dit déjà en général (« non lançable » et mot de la mère) ; l'illustration de l'annexe A, point 12, est plus généreuse que la règle, comme B5-07 le dit maintenant.
- **F-D6-2** : l'expression « la règle suivante » désigne deux règles différentes dans la même phrase du budget (B_a, taux, N, M puis la règle des cinq termes) : à renommer à la version qui fera foi.
- **F-D6-3** (reprise de F-B5-1) : le risque qu'un appel de Pr-1 dépasse X fois son plafond (arrêt code 3, verdict « non jugeable » pour 20 mondes payés), avec X fixé sur quatre appels du pilote, n'est pas chiffré ; une phrase donnant ce risque par programme d'après le plus grand rapport mesuré aiderait la mère à décider de la tolérance.
- **F-D6-4** (reprise de F-B5-2 et F-B5-3 et de F-1 à F-5 du tour 4) : V1, V3 et V5 sont des comptes absolus (à 24 mondes ils ne sont plus à l'échelle) ; règle de pertinence après lecture du témoin positif du pilote ; seuil sur k_R quand n_c vaut 16 à 19 ; partie A sans le champ des retenues (la liste des retenues de la génération 1 serait « toutes les cartes », donc l'exception pourrait disparaître). Non exigées.

## 6. Points pour la mère

1. **Sceller telle quelle : non** ; six mineures d'écriture (D6-01 à D6-06), aucune majeure. Après correction, un contrôle limité aux couples (différentiel par `diff`, sans nouvelle lecture entière) suffirait avant scellement ; il reste que le dernier tour a trouvé des défauts, dont deux issus de couples recopiés d'un rapport précédent : la règle de « nouveau écrit par le lecteur » ajoute des défauts que seul un lecteur suivant voit. Un rédacteur du modèle A pour appliquer ces couples (R-2982) vaudrait mieux que le modèle C : **l'écart de rôle, déclaré à chaque tour, est à régulariser**.
2. **Rôles** : la pièce est de A ; les tours 2, 4, 5 et 6 ont été appliqués par un rédacteur de C ; je suis de C. À la mère de dire si cela suffit.
3. **24 mondes** : la règle R-2977 (24 si le taux par appel du pilote est sous 0,95) ne donne **aucun gain de puissance** (0,79 contre 0,80 à p = 0,26) pour + 20 % de coût, et d'après F-D6-1 le budget de durée y devient probablement « non lançable » ; je recommande N = 20 dans tous les cas, confiance 0,6 : écart à R-2977 qui demande son mot (déjà demandé aux tours 3 à 5).
4. **Date de lancement** : fixée par le code neuf (lanceur à N mondes, M mondes à la fois, mesure, lecture, procédure de la machine, essais, banc de mutations, contre-lecture du code, addendum), non par le préenregistrement ; fenêtre du GO au 30 novembre ; le prix public de Pr-1 double le 1er décembre. Il n'y a pas de configuration neuve.
5. **Tolérance de la réflexion de Pr-1** : règle écrite d'avance, existant seulement si un dépassement est observé au pilote ; risque restant d'un arrêt non chiffré (F-D6-3).
6. **Étage 5 (ablation) aux critères gelés** : point 10 bis encore ouvert, défaut (a) à 48 heures ; **si le défaut s'applique, le texte change** (étage 5, ligne V4, lecture de H-v-a) avant scellement : la mère doit trancher avant le scellement.
7. **Points 1, 3, 7, 8, 10 et 10 bis de « Choix et doutes »** : à trancher avant scellement ; confirmer que « recommandations de l'auteur sauf mention » (R-2977) vaut pour les points 1 et 3.
8. **Enveloppe des cinq cribles et lecteur du pilote** : (v) 196,60 USD au pire (235,32 à 24 ; 204,67 avec la sonde neuve) ; le compte des cinq (1 275) est à refaire sur les coûts mesurés avant d'inscrire une ligne. Le lecteur du pilote ne doit rendre que les comptes d'appels répondus, tronqués et en échec, les durées (dont celles de D6-01), les coûts et le seul champ du témoin positif ; si la mère veut que V1 et V6 restent des prédictions à l'aveugle, il faut retirer la ligne « Le témoin positif du pilote » des points à remesurer.
9. **Après correction** : ajouter à « Contre-lecture » une entrée « Contre-lecture 6 » avec l'empreinte entière de ce rapport (lue dans son compagnon `.sha256`) et celle du brouillon 6 relu (`08b430d7…`), mettre à jour le statut, nommer les couples propres.

## Incidents de ma main

- Aucun fichier écrit hors de ce rapport et de son compagnon d'empreinte, et de deux fichiers jetables dans le bloc-notes de ma session (programme de contrôle des couples, brouillon 5 avec les sept couples appliqués, copie de la procédure v14 tirée par `git show`). Aucune pièce existante modifiée.
- `git fetch` par refspec de la seule branche `lot/compte-organisme-v1` (met à jour sa référence distante locale) ; aucun clone.
- `grep`/`sed` de `registres/go.md` (ligne 339) et de `registres/decisions.md` (ligne R-2977 seule). Aucun taux ni coût du pilote lu.
- Calculs : comptes de sous-chaînes et d'empreintes par `python3` (bibliothèque standard), validateur `controle_ia.prereg.problemes` (lecture seule). Aucun `pytest`, aucun calcul lourd.
