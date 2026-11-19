# Contre-lecture — préenregistrement de la ligne 1 (effort de recherche compté dans le seuil de promotion), brouillon 1 — v1

- Contre-lecteur : agent neuf, « modèle O », qui n'a pas écrit le texte relu (règle R2). Rédacteur du texte relu : « modèle F ».
- Heure (temps universel, `date -u`) : 2026-11-19T13:20:58Z au début de l'écriture.
- Branche `lot/compte-organisme-v1` ; commit du brouillon lu : `a0633b0be1e847973215db3a0370468dbefa0273` (présent sur la branche distante ; tête locale à la lecture : `8fc6e083fd25e81f7e2dd0f86b582a4364ca699b`).
- Rien n'est écrit dans le texte relu ni ailleurs, hors ce fichier et son compagnon. Aucun appel de modèle, aucune dépense, aucun tirage de l'épreuve. Deux gestes de calcul : l'extraction des cinq cartes nommées (programme ci-dessous) et un chronométrage sans issue lue (constat 11).

## Empreintes lues (sha256, complètes)

| pièce | empreinte | contrôle |
|---|---|---|
| `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/preenregistrement-ligne-1-effort-recherche-v1.md` (branche) | `ca5b2b7f3b08ba9201c7c85719c99de6ccb2a4303eb98a1831f8f5f5d7fa7dc1` | conforme au compagnon `.sha256` |
| `prereg/gabarit-preregistrement-v1.md` (`main`) | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` | conforme au texte relu |
| `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md` (`main`) | `a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856` | conforme |
| `docs/notes/organisme-auto-conception-v1/course-v2/criteres-choix-cartes-v9-v1.md` (`main`) | `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326` | conforme |
| `docs/notes/organisme-auto-conception-v1/course-v2/lecture-course-v9-v1.md` (`main`) | `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` | conforme (empreinte seule ; contenu non requis par les constats) |
| `docs/decisions/decision-N-067-v1.md` (`main`) | `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` | conforme |
| `docs/decisions/decision-resserrement-juge-au-nul-v1.md` (N-071, ligne R-3187 de `registres/decisions.md` sur `main`) | `9700fe6fce74840d383e3cbbf2e0f87f7914887759df3c0aa0fea687b433c184` | conforme |
| `docs/decisions/decision-N-073-revendications-apres-veille-exploration-idees-v1.md` (`main`) | `b95688df5e695da7dc32ce71321ba205f44debcc0b7410e598c78c2180733ecd` | conforme |
| N-073, compléments 1, 2, 3 (`main`) | `61903909e8aaaa70d6f1aa26a8025104aa3513244b6723daac529048267d4478`, `5707dbd8bdd8ccc224578be480107723fad6e5054484082c1a1c38d8fa588e8e`, `4ca0ce7b040b917d9be145134b2b28755a862bfa7a41e4f16d22893129bb03e5` | conformes |
| `docs/decisions/decision-N-064-v1.md`, `docs/decisions/decision-N-059-v1.md` (`main`) | `387c9d4eda5a1b3d0e8ec61def715bb88c1bf9883081d5796ea291879be63f97`, `41aff854c38bed3a43aced62bd0c1b3af782c5a5f6174f335a175847b407e687` | conformes |
| `registres/go.md`, ligne GO-2026-11-19-55 (`main`, lue par `git show`) | — | mandat : option (c), « les 5 lignes plus la question de l'heritage », préenregistrement par le rédacteur, contre-lecture par l'autre modèle |
| `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` (branche) | `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481` | conforme ; lues par programme les **seules** cartes `f169420b8d1d8`, `f1373c384a771`, `fb45c8739b3d2`, `f01d286e78e83`, `f9a517d00f493`, champ `meta` retiré |
| code de l'organisme, dépôt `ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, `orchestrator/pole/` : `a_blanc_v59.py`, `selection_pari.py`, `nul_filles_v2.py`, `nul_v8.py`, `cycle.py`, `memoire_v53.py`, `boucle_fermee_v59.py`, `proposeurs_references_v59.py` | les huit empreintes citées par le brouillon, ligne 18 | les huit conformes (lues par `git show` au commit, sans y écrire) |

Programmes du contre-lecteur (bloc-notes de la session, hors dépôt) : extraction des cartes `contre_lecture_l1_cartes.py` (vérifie l'empreinte de `fiches.json` avant toute lecture, n'extrait que les cinq identifiants, retire `meta`) ; chronométrage `contre_lecture_l1_chrono.py`, `4414e1eae16aac9d96c4e0628cfb6d3792c459b2e8d752e58ce32876d9b2d6aa`. Leurs chiffres sont des ordres de grandeur du contre-lecteur, non opposables (règle R6).

## Réponses aux cinq questions du rédacteur

1. **La remarque de conception du § 0 est juste dans les mondes sans effet.** Vérifié au code : le nul standard contient `marginale_mv` (`selection_pari.py`, l. 38-42), dont la trajectoire est la log-vraisemblance de la marginale du maximum de vraisemblance calculée après coup (l. 303-308) ; la richesse est, à chaque instant, le numérateur moins le meilleur membre (`nul_filles_v2.evaluer_v2`, l. 215-221). La log-richesse est donc bornée par le log du rapport de vraisemblance de la carte contre la marginale vraie du monde, martingale sous un monde sans effet : e-valeur valide, arrêtée ou non. Les tirages sont liés à l'empreinte de l'engagement (`a_blanc_v59.juger_carte`, l. 176-178) et indépendants de la tranche exploratoire. **Elle ne vaut pas pour les cartes « fausses » des mondes à effet** (constat 2).
2. **La garantie du bras d tient**, pour le nul du juge : pour chaque génération g, V_g/ΣR ≤ V_g/R_g (et V_g = 0 quand R_g = 0), d'où un taux de fausses découvertes de la course au plus égal à la somme des taux par génération, soit 6 × 0,05/6 = 0,05 ; la validité par génération tient conditionnellement au passé parce que les tirages de la génération g sont frais. Le même argument donne au bras **a′ la même garantie de 0,05 sur la course, par construction** (constat 1), et au bras a une borne de 6 × 0,05 = 0,30 seulement.
3. **Les bras b et c sont une lecture fidèle** de la proposition (§ 3.1) et de la carte porteuse ; b demande une définition plus nette de son e-valeur (constat 8).
4. **Le niveau « sur la course » est défendable** (la carte porteuse dit « dans la génération et dans la course »), mais il est voisin d'une distinction publiée, et c'est lui seul qui peut faire dépasser le bras a sur ce banc (constats 1 et 9).
5. **L'étalonnage des lois tranchantes est compatible avec la règle R3** (graines disjointes, aucun bras lu, règle de choix gelée, rôle de témoin positif), à condition que le texte soit scellé **avant** l'étalonnage (constat 3).

## Constats et corrections

### Bloquants

**1. Un « oui » serait mal attribué : sur ce banc, seul le nombre de générations peut faire dépasser le bras a, et le budget par course suffit à le corriger, sans le compte des essais refusés.** Le § 0 le dit à moitié : les variantes refusées ne touchent jamais les tirages frais, donc le compte des essais refusés ne peut pas être nécessaire à la validité. Le seul chemin par lequel a peut dépasser 0,05 sur la course est l'addition de six générations (borne 0,30), commune aux deux classes ; et a′ (budget 0,05/6, sans registre) tient 0,05 par construction (réponse 2). La ligne 4 de la table (« oui : la multiplicité entre cartes est un trou réel, bouchable par le registre ») peut donc être remplie alors que le registre n'apporte rien que le budget par course n'apporte déjà, et que l'écart ne vient pas des « nombreuses variantes ». La mention obligatoire sur a′ ne suffit pas : elle accompagne un « oui » qu'elle contredit.
- Correction (a) : ajouter une quantité de décision, Δa = M1(a, « beaucoup ») − M1(a, « peu »), écart apparié (constat 7), borne basse unilatérale à 97,5 %.
- Correction (b) : insérer avant la ligne « oui » une ligne « a dépasse (classe « beaucoup »), a′ tient dans les deux classes → **non — quatrième branche** : ce qui tient le niveau est le budget par course ; le compte des essais refusés n'est pas requis sur ce banc ». Le « oui » exige en plus : a′ ne tient pas dans la classe « beaucoup » **et** borne basse de Δa strictement au-dessus de 0.
- Correction (c) : écrire dans le § 0 et sous « Hypothèse » que, par la théorie, ce « oui » corrigé n'est atteignable que si le code ou le banc est fautif ; l'épreuve devient une vérification et une mesure du coût en puissance du registre (P4, P5). La prédiction d'ensemble devient « non, première ou quatrième branche ».
- Pour la mère : cette correction affine la lecture du « oui » de la proposition (§ 3.1) sans changer le choix de la ligne ; si elle juge qu'elle change ce choix, retour à Lazar selon la lettre de GO-2026-11-19-55.

**2. La vérité de l'oracle n'est pas le nul du juge dans les mondes à effet.** Une variante d'une lignée vraie dont le gain sur la marginale du monde est nul ou négatif (puissance 1,6, inclinaison défavorable, bruit sur les poids) est « fausse » pour l'oracle, mais le nul du juge (aucun lien entre traits et issues) y est faux : sa promotion n'est pas une erreur de première espèce de la règle e-BH, et aucune garantie (ni de a, ni de a′, ni de d) ne la borne. Le bras d peut alors « dépasser » pour une raison étrangère au compte, ce qui déclencherait la ligne 1 (« le compte des essais est mal défini ») et la garde A11 à tort.
- Correction : la métrique de décision du niveau devient **M1-nul** : fausses découvertes = promotions dans les lignées des mondes sans effet (où le nul du juge est vrai), sur toutes les promotions de la course. Les promotions de cartes fausses pour l'oracle dans les mondes à effet sont rapportées à part (**M1-oracle**), sans verdict, et dans M2 et M3.
- Dire comment les cartes « indéterminées » entrent dans M1 (proposé : hors du numérateur, dans le dénominateur, puisqu'elles sont des promotions) ; mesurer, sur les graines d'étalonnage, la part des cartes « indéterminées » et des cartes « fausses en monde à effet » parmi les cartes jugées, et faire de A7 une **porte d'étalonnage** (arrêt avant la course décisive), pas seulement une garde de lecture qui jetterait la course après coup.

**3. Ordre des gestes contraire à la règle R1 et à N-073, § 4.** L'audit du générateur (étape 2) et l'étalonnage (étape 3) sont faits avant le scellement (étape 4) ; N-073, § 4, exige un audit « sous préenregistrement », et la règle R1 interdit toute lecture d'issue avant scellement. Le texte pourrait changer après avoir vu l'étalonnage.
- Correction : (1) code et essais du banc, contre-lus ; (2) scellement du préenregistrement par la mère, commit du code et empreintes portés ; (3) audit du générateur ; (4) étalonnage ; les sorties de (3) et (4) scellées dans un fichier à part, au nom neuf, cité par le manifeste, dont le contenu ne fait que remplir les paramètres que les règles gelées déterminent (forces, couple (s, c), portes) ; (5) course décisive ; (6) analyse ; (7) lecture par un agent neuf. Aucune ligne du texte scellé ne change après (3).

**4. L'audit du générateur (garde A8) tirera par construction.** Deux traits de la liste portent la vérité sans être des raccourcis du générateur : (i) le rang de la variante dans l'appel est l'ordre du gain sur la tranche, signal légitime du proposeur, corrélé à la vérité à l'intérieur des lignées vraies ; (ii) la longueur du texte porte le type de loi (`si_sinon` contre `transformee`), et toute carte `si_sinon` est fausse. L'aire sous la courbe sortira de [0,45 ; 0,55] et la course s'arrêtera sans défaut du banc. De plus l'audit ne reprend pas deux des trois éléments de N-073, § 4 (chercheur non paramétrique bon marché sur les mondes à vérité négative ; deux étiquettes de vérité, conception et effet).
- Correction : retirer le rang dans l'appel des traits audités et le déclarer comme signal du proposeur ; calculer l'aire à type de loi égal (cartes `transformee` seules), sur les traits identifiant, rang de la lignée, longueur, numéro au registre ; rapporter les deux étiquettes (rôle de la lignée ; vérité de l'oracle) et leur table croisée ; dire que le chercheur bon marché sur mondes sans effet est la famille tranchante étalonnée (ou l'ajouter), sinon écrire pourquoi l'élément ne s'applique pas. Garder l'artefact de A8 (rôle écrit dans l'identifiant).

### Majeurs

**5. La mémoire anti-redite sur des textes de gabarit n'est pas bornée.** Toutes les cartes sortent d'un même gabarit et ne diffèrent que par des nombres arrondis ; la mémoire refuse à 0,6 contre « toute carte de la course », y compris celles des autres lignées. Le taux de refus est inconnu : la classe « peu » peut finir sous 2 cartes jugées par appel quand « beaucoup » en garde 2 (m_s et puissance différents entre classes), et des refus d'une lignée par une autre rendent le sort d'une carte dépendant du rôle de ses voisines.
- Correction : fixer l'appel exact (`memoire_v53`, méthode « bardeaux », bardeaux de 3 mots, seuil 0,6) ; mesurer à l'étalonnage le nombre moyen de cartes jugées par appel dans chaque classe et la part des refus entre lignées ; ajouter une garde (nouvelle A15) : écart de cartes jugées par appel entre classes au-delà de 0,1, ou refus entre lignées au-dessus de 5 % des essais, → arrêt avant la course décisive. Ou bien restreindre la comparaison aux cartes de la même lignée, en le disant comme écart à la proposition.

**6. La porte de prise (0,005 par carte tranchante) est trop basse pour que le témoin T0 dépasse.** Ordre de grandeur du contre-lecteur, non opposable : deux lignées tranchantes, au plus 12 cartes jugées chacune sur six générations, à 0,005 par carte, donnent environ 0,12 fausse promotion par course contre deux à quatre vraies, soit un taux de T0 sur la course vers 0,03 à 0,06 : la ligne 3 (« banc sans prise ») deviendrait l'issue probable pour une raison de réglage.
- Correction : exprimer la porte sur la quantité qui décide de la prise : T0 seul, sur au moins 200 courses d'étalonnage de la classe « beaucoup », borne basse de son taux sur la course au-dessus de 0,05 ; sinon arrêt avant tout tirage décisif. À défaut, relever le seuil par carte avec un calcul écrit qui le justifie.

**7. Les classes ne sont pas appariées.** La tâche des graines porte « classe | course | lignée | génération | objet » : les mondes, tranches, hypothèses et rôles diffèrent entre classes, et l'écart P4 comme Δa (constat 1) sont non appariés.
- Correction : retirer « classe » des tâches du monde, de la tranche, du rôle, de l'hypothèse de lignée, de la marginale d'entraînement et du plan ; ne la garder que pour la génération des variantes. Les écarts entre classes se lisent alors par rééchantillonnage apparié des courses.

**8. Définitions de bras à préciser.**
- Bras a : la promotion est l'appartenance à `retenues` rendue par `cycle.appliquer_multiplicite` ; l'écrire. Elle équivaut ici au verdict « survit » de l'organisme (une carte retenue a franchi 1/α, aucune marge `delta0` dans ce banc) ; un essai le vérifie.
- La fonction **modifie ses arguments** (`cycle.py`, l. 760-777 : `verdict_final`, `motif`, `pari.multiplicite`) : chaque bras reçoit une copie profonde des issues ; l'essai 2 le couvre.
- Bras b : « e-valeur arrêtée » à définir : promue si la trajectoire atteint log(6·m_s/0,05) à l'un des huit instants de lecture (arrêt à son propre seuil, comme `appliquer_multiplicite`, l. 746-753 ; valide par l'inégalité de Ville).
- Bras c : écrire que les 100 tirages de tri sont les 100 premiers des tirages partagés, et que le lot de confirmation est tiré d'un engagement neuf, graine dérivée de son empreinte.

**9. Voisins publiés de la lecture « sur la course » non dits (règle R8).** N-067, § 6, range PACE (arXiv 2606.08106) avec la note « garantie par décision, non par course (p. 5, 8) », et, § 3, Sargsyan (arXiv 2511.06701) pour un « taux de fausses découvertes en ligne » (p. 1, 15-16) : le contrôle à travers des générations successives est le cadre du contrôle en ligne, et le partage 0,05/6 des bras b, c, d et a′ en est une forme fruste (dépense fixe du niveau).
- Correction : le dire sous « Hypothèse » et en réserve 7, pages citées d'après N-067 (non relues) ; dire comme limite qu'aucune règle de contrôle en ligne publiée n'est un bras (la proposition n'en demande pas ; l'ajouter serait un écart).

**10. Règle R5 : la garde A14 n'a pas d'artefact, et l'essai 4 ne couvre que A1 à A13.**
- Correction : artefact de A14 = un manifeste planté où l'horodatage d'une dérivation de graine décisive précède celui du scellement ; l'essai 4 couvre A1 à A14 et les gardes ajoutées (A15, portes des constats 2 et 6).

**11. Règle R6 et durée.** Le chiffre « 0,013 seconde par jugement » renvoie à un programme hors dépôt, sans empreinte. Mesure du contre-lecteur (même machine, 4 cœurs, programme `4414e1ea…`, aucune issue lue) : l'oracle de `a_blanc_v59` coûte environ 0,043 seconde par carte à 4 000 instances (il recalcule la loi du monde à chaque appel), soit environ 43 minutes pour 60 000 cartes sur un cœur, au lieu de 15 à 25 ; 400 évaluations de loi coûtent environ 0,0013 seconde, ce qui confirme l'ordre du poste « tri sur tranche ». Le compte « environ 240 000 jugements » suppose un partage des jugements entre six bras qui n'est pas écrit.
- Correction : verser le programme de chronométrage avec son empreinte (`161a306f14a7d6e19b12c53cfcb1144a6dd4b21755c13991b75480af8492ece1` au moment de la lecture) et sa sortie, ou retirer le chiffre ; écrire que les jugements sont mis en cache par (tâche, empreinte de l'engagement), communs aux bras, et que la loi du monde est calculée une fois par monde dans l'oracle ; refaire le devis. Faisabilité sur processeur seul : **tenue** (ordre de 2 à 3 heures sur un cœur, sous le plafond de 6 heures, moins sur quatre).

**12. Règle R4 : l'audit de symétrie ne se déclenche que d'un côté.** Il part sur « trop propre » et sur le démenti de P1, P3, P6, mais ni sur un « oui », ni sur un taux très haut.
- Correction : rendre l'audit (trois courses rejouées à la main, empreintes, calcul de la vérité) **inconditionnel**, puisqu'il ne coûte rien ; à défaut, ajouter comme déclencheurs tout « oui », toute « quatrième branche », M1-nul de a au-dessus de 0,15 et M1 de T0 au-dessus de 0,5.

### Mineurs

**13. M1 contre M2.** La carte porteuse et la proposition prennent pour oracle la part des lois fausses promues, avec sa borne haute (M2). Le choix de M1 (taux de fausses découvertes) comme métrique de décision est juste — c'est ce que la règle e-BH borne, pas M2 — mais c'est un écart à la lettre : l'écrire comme tel, avec sa raison, et garder M2 et sa borne parmi les mentions obligatoires.

**14. Table de lecture, ligne 3** : écrire « T0 tient ou est indécis » au lieu de « T0 ne le dépasse pas ».

**15. P5** : signe « négatif » et intervalle attendu « −0,15 à +0,05 » ne s'accordent pas ; écrire « entre −0,15 et 0 », ou dire le signe « négatif ou nul ».

**16. Gabarit.** Le validateur `controle_ia.prereg.problemes` rend, sur le brouillon : « section Contre-lecture sans les deux empreintes exigées (brouillon relu et rapport) » — attendu pour un brouillon. La version scellée porte l'empreinte du brouillon relu (`ca5b2b7f…`) et celle de ce rapport, le traitement de chaque constat, et passe le validateur. Le lieu (`prereg/` selon le gabarit, ou le dossier de l'épreuve) est à fixer par la mère.

**17. Garantie de d** : recopier dans le texte l'argument de la réponse 2 (sous-additivité, validité conditionnelle par génération), et dire qu'il vaut pour le nul du juge, non pour la vérité de l'oracle (constat 2).

### Tenus (sans correction)

- Sections du gabarit présentes ; prédictions P1 à P8 chiffrées, signées, avec leur réfutation ; seuils, tailles (600 courses par classe), racines de graines (R9, `boucle_fermee_v59.graine_de_tache`, `SeedSequence`) et liste d'arrêt écrits avant tout tirage ; aucune relance ni choix de graine après lecture (R3).
- Fidélité au mandat et à la proposition : les deux classes au même nombre d'appels, les quatre bras (a, b, c, d), l'oracle et les trois branches du « non » sont repris ; a′ et T0 sont des ajouts de diagnostic et de témoin, déclarés ; la part « jetons » (`f1373c384a771`, `fb45c8739b3d2`) et le « second temps » (`f01d286e78e83`, `f9a517d00f493`) sont dits hors de l'étage, ce que la proposition permet. Rien n'est dépensé.
- Aucune revendication neuve, aucune zone dite libre ou vierge, aucune nouveauté ni priorité (R8) ; les voisins des cartes sont « non vérifiés » (R7), avec l'écart 210.0 / 210.1 relevé.
- Citations obligatoires : les quinze pièces de N-064, point 4, et de N-067, § 6, sont nommées ; les contre-indices de N-067, § 7, sont repris ; l'attribution à Wang et Ramdas (2022) est dite non vérifiée.
- N-073 : l'héritage n'est pas touché ; aucune phrase des listes « Ne plus écrire » (§ 1) ni « Ne pas écrire » (complément 3) ; le mot « archive de découvertes » n'apparaît pas.
- Aucun identifiant de modèle dans le texte relu.

## Verdict

Scellable après corrections.

Les corrections 1 à 4 sont nécessaires avant tout scellement : sans elles, un « oui » serait mal attribué (1), la garantie lue ne serait pas celle que la règle donne (2), l'ordre des gestes violerait la règle R1 (3) et l'audit arrêterait la course par construction (4). Les corrections 5 à 12 sont nécessaires avant la course décisive ; 13 à 17 sont de forme. Aucune ne change la ligne choisie ni la dépense (nulle) ; la correction 1 affine la lecture du « oui » de la proposition et doit être montrée à la mère, qui juge si elle relève d'un retour à Lazar (GO-2026-11-19-55). La version suivante (nom neuf, règle R12) porte le traitement de chaque constat ; une relecture courte des seuls changements par un agent neuf est recommandée avant le scellement.
