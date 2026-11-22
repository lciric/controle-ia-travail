# Plan de lecture de la seconde course du réajustement de nos lentilles R et S (lecture par lentille neuronale, Llama 3.1 8B Instruct), variante B — v1, brouillon 2

## Différences avec le brouillon 1 (correcteur neuf, brouillon 2)
- Correcteur : sous-agent neuf de la session des lentilles (`session_01Qi7Gr3vedYVukbyqBbHd7z`), sur le mandat
  `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-correcteur-textes-variante-b-v1.md`
  (`125a59ff1fb4e4add1331aa816326a428b364f5260c9ebf4fef8ca70eb4800c1`, vérifiée). Il n'a écrit ni le brouillon 1, ni la
  contre-lecture, ni aucun document qui fait foi. Écrit sur le commit `08896fd25`, à partir de 2026-11-22T05:17:35Z (`date -u`).
- Source des corrections : `contre-lecture-textes-variante-b-opus-v1.md`
  (`a92149e88c7cadaaffefa28d99e370935500da1508bd7eb19b6b780b5a76980f`), texte exact suivi là où elle en donne un.
- Hors corrections, une seule chose change : le titre (« brouillon 1 » → « brouillon 2 ») et ce bloc. L'en-tête du rédacteur et sa
  déclaration sont ceux du brouillon 1 (sauf ce que changent les corrections) ; ils décrivent le brouillon 1.
- **Réserve de la contre-lecture, recopiée** : elle est du même modèle que le rédacteur et ne remplit pas l'exigence « d'un autre
  modèle » ; la contre-lecture de ce brouillon 2 par un autre modèle reste à faire avant le scellement d'une version finale.
- Brouillon 1 corrigé : `plan-lecture-seconde-course-reajustement-v1-brouillon1.md` (`ed802f8da81aee8af9255f4ffb2d25cbe851c46dbb556f5d6b5f276dcdfba457`), inchangé (R12).

| correction | ce qui change | lignes du brouillon 1 → lignes de ce brouillon 2 |
|---|---|---|
| P-1 (§ 7) | § 7, « Qui lit » : règle d'aveuglement du lecteur rendue tenable (verdict d'ensemble seul connu, lectures permises nommées) | 178-179 → 218-221 |
| P-1 (§ 10) | § 10, troisième ligne : condition d'arrêt alignée sur le § 7 | 250 → 300 |
| P-2 (a) | « Déclaration », deuxième puce : libellés, valeurs et couches du 18 retirés, renvoi à la déclaration à part | 40-46 → 81-85 |
| P-2 (b) | § 5.2, dernière puce : couches du 18 retirées | 152 → 191 |
| P-2 (c) | § 6 : valeurs des deux marges du devis v9, § 2, retirées | 170-171 → 211 |
| P-3 (étape 0) | § 7, étape 0 : du verdict d'identité, seuls mention, commit K1 et identifiant de course, sur un extrait scellé | 191-193 → 237-240 |
| P-3 (étape F) | § 7, étape F : le verdict d'identité entier lu à l'étape F | 202 → 250 |
| P-4 | § 6 : la lentille concernée par un désaccord définie, mesure par mesure | 165 → 206-207 |
| P-5 | § 6, première phrase : la même lecture des ambiguïtés prise des deux côtés | 155 → 194-195 |
| P-6 (§ 8) | § 8, ligne « palier 1, aucun désaccord » : cas mixte du critère v8, § 5, ajouté | 219 → 268 |
| P-6 (§ 1) | § 1, puce « palier 1 » : cas mixte ajouté | 53-54 → 93 |
| P-7 | § 10 : la ligne contradictoire remplacée par deux lignes (avant, après le scellement de l'étape S) | 251 → 301-302 |
| P-8 (§ 8) | § 8, audit de symétrie : le contrôle des sorties brutes ne manque plus sur le cas sain égal au bit | 231 → 280-281 |
| P-8 (étape A) | § 7, étape A : l'audit de symétrie essayé sur un cas sain et un artefact (R5) | 197 → 244-245 |
| P-8 (étape F) | § 7, étape F : pièces du 18 de l'audit de symétrie lues à l'étape F | 203 → 251-252 |
| P-9 (choix 7 et 8) | § 11 : choix 7 (toutes les cibles pour Λ) et 8 (rang 5, exclusions sur « non reproduit ») ajoutés | 271 → 325-331 |
| P-9 (choix 5) | § 11, choix 5 : la ligne de la clé et le mot de Lazar au moment de la commande | 270 → 321-323 |
| P-10 | § 7, « Pièces » : suite d'une pièce manquante ou renommée fixée | 185 → 229-231 |
| P-11 (K1) | § 7, « Pièces » : définition du commit K1 recopiée | 184 → 227 |
| P-11 (mandat) | § 7, « Pièces » : le mandat du lecteur recopie l'autorisation | 185 → 229 |
| P-11 (second lecteur) | § 7, « Qui lit » : le second lecteur tenu à la même règle sur le 18 | 180 → 222 |
| P-12 | § 12 : modèle de la contre-lecture nommé ; contre-lecture du même modèle déclarée comme telle | 274 → 334 |

**Corrections non faites telles quelles** : aucune. Toutes sont faites mot pour mot ; seules les coupures de ligne
diffèrent (texte recoupé à la largeur du document). Aucun nœud ouvert par une correction.

Plan de lecture aux sections du gabarit `prereg/gabarit-preregistrement-v1.md` (R1), sur le modèle du plan de lecture de la tranche
(`docs/notes/neuron-lens-v1/lecture-b-beta/plan-de-lecture-b-beta-v2.md`). **Pièce de classe A**, à contre-lire (R2) puis à sceller
**avant la création de la machine** (devis v9, § 5, point 7) : rien de ce qu'il fixe n'est décidé après avoir vu la seconde course.
Ce brouillon est scellé tel quel ; une correction est un brouillon neuf (R12). **Aucun critère nouveau** : seuls ceux de la tranche,
recopiés avec leur source ; les choix qu'impose leur application à une seconde course sont nommés et soumis à la contre-lecture (§ 11).

- Rédacteur : rédacteur neuf, sous-agent de la session des lentilles (`session_01Qi7Gr3vedYVukbyqBbHd7z`), sur le mandat
  `docs/notes/neuron-lens-v1/devis-reajustement/mandats/mandat-redacteur-statut-et-plan-seconde-mesure-v1.md` (`26af6c39…`, vérifiée) ;
  modèle servi : celui que nomme le mot de Lazar du 22 novembre pour les pièces délicates écrites en autonomie. Il n'a écrit ni le texte
  gelé, ni l'addendum, ni le plan de lecture de la tranche, ni le verdict du 18, ni le devis, ni le critère, ni le code, ni les
  commandes, ni aucune course ; il a écrit le statut de la seconde mesure (même dossier) dans la même séance.
- Heure (`date -u`) à l'ouverture du travail : 2026-11-22T04:56:13Z ; l'heure du scellement est celle du fichier compagnon.
- Branche `claude/brave-galileo-jhp684`, écrit sur le commit `33371746d`. Aucun code d'analyse écrit : le script du lecteur est écrit
  par le lecteur (§ 7, étape A).

### Documents qui font foi (empreintes recalculées par le rédacteur, égales à celles que citent le mot de Lazar, le devis et le plan v2)
| pièce | chemin | empreinte SHA-256 |
|---|---|---|
| texte gelé de la tranche | `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` | `f5d46860525f12f8ad0483e56afc0847ab7db25ecae55edcc279b61316b7a454` |
| addendum, partie 1 v3 (pièce du texte gelé) | `docs/notes/neuron-lens-v1/addendum-texte-gele-tranche-b-beta-v1-partie1-v3.md` | `bd8067dcd04ae32bb5960dc95bef89384b3b914a1a35e918107411f43d1c95f1` |
| plan de lecture de la tranche v2 | `docs/notes/neuron-lens-v1/lecture-b-beta/plan-de-lecture-b-beta-v2.md` | `391c3b1a642d0d96ccef2c982594b334dd1e2e57c398b9cde21436f661bbe14d` |
| sa contre-lecture | `docs/notes/neuron-lens-v1/lecture-b-beta/contre-lecture-plan-de-lecture-b-beta-v1.md` | `bf3e2d7572b85df806d5841a0b8a7342829893a86503738fbb153721e33ec4e7` |
| verdict du 18 (accepté) | `docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md` | `3a9b947e0757dd7f5fe7ecb418b047b94fb274fed84672accabc48926660bb78` |
| accord de Lazar sur ce verdict | `docs/notes/neuron-lens-v1/lecture-b-beta/accord-lazar-verdict-b-beta-v1.md` | `8469add5f178d9fcf4e79020c60d8d906f59ce5cd867c52073fee00e1c686d6b` |
| critère d'identité v8 (prime sur ce plan) | `docs/notes/neuron-lens-v1/devis-reajustement/critere-identite-reajustement-lentilles-v8.md` | `541bb86b15088c5cea5a291a294cccdd1067fe39be995b7f9014661f96cb3940` |
| devis v9 | `docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md` | `064e735a8b98cb1bd76916d2514d98f6e5cf7d57e367b5b2dcfc6f0222b6bb41` |
| mot de Lazar du 22 novembre (décisions 1 à 7) | `docs/notes/neuron-lens-v1/mot-lazar-go-reajustement-autonomie-2026-11-22-v1.md` | `ed47f2e3c15a9aaa92fc2fcae9a0faba17dfd820e91a41955c86371f75065172` |
| décision posée sur l'entrée des lentilles | `docs/notes/neuron-lens-v1/decision-entree-lentilles-programme-v1.md` | `6aaf54e7a701554dd8e05f495961b4ff2e97a58662072ee008d702f73bb5b4bd` |
| statut de la seconde mesure | `docs/notes/neuron-lens-v1/devis-reajustement/textes-variante-b/statut-seconde-mesure-reajustement-v1-brouillon1.md` (ou la version scellée qui le remplace) | compagnon `.sha256` |
| pièces d'ajustement du 18 (lues à l'étape F seulement) | `diag/20261118-164930-neuron-lens-b-beta/b-beta-ajustement-R.json` ; `…/b-beta-ajustement-S.json` | `129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab` ; `2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297` (critère v8, § 2) |

### Déclaration : ce que je savais avant d'écrire (R4)
- Lu en entier : `CLAUDE.md`, le mot de Lazar, le devis v9, le critère v8, le texte gelé, le plan de lecture de la tranche v2 et sa
  contre-lecture, **le verdict du 18** et l'accord de Lazar, la décision posée sur l'entrée des lentilles, le gabarit ; les lignes 1 à 60
  de l'addendum (§ 1.1 et 1.2). Noms de fichiers seulement des dossiers `docs/notes/neuron-lens-v1/`, `devis-reajustement/` et
  `lecture-b-beta/`. Rien de `diag/`, `runs/`, `docs/verdicts/`, des branches `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*`, ni des
  pièces interdites par le mandat.
- **Je connais le verdict du 18**, mesure par mesure, et les couches que la règle des couches stables du critère v8, § 5, en exclut
  d'avance ; ils sont écrits dans la déclaration à part
  `docs/notes/neuron-lens-v1/devis-reajustement/textes-variante-b/declaration-redacteur-textes-variante-b-v1.md`, que le lecteur ne
  lit qu'à l'étape F. La règle de rang que je propose (§ 5, P2-3) admettrait la classe du verdict d'ensemble du 18 : je le déclare
  (§ 11, choix 8).
- Aucune seconde course n'existe ; aucune valeur d'elle n'est connue.

## 1. Hypothèse (objet de la lecture)
**Aucune hypothèse n'est testée** ; ce plan ne porte aucune revendication. Il fixe comment un lecteur neuf lit la seconde course de la
variante B (la commande de la tranche rejouée entière sur une autre machine, avec les changements du devis v9, § 5, point 5, qui ne
touchent pas les étapes de mesure) et ce qui en est écrit, lentille par lentille, selon son verdict d'identité (critère v8) :
- **palier 1** : une seconde mesure de la même lentille, rapportée à côté du verdict du 18, qui reste celui de la tranche (statut,
  règle 1) ; dans le cas mixte, seules les mesures du 18 faites sur cette lentille la décrivent (critère v8, § 5) ;
- **palier 2** : la seule mesure de la lentille rangée ; ce plan fixe d'avance sur quels critères gelés de la tranche elle est dite
  lisible, et à quelles couches (§ 5) ;
- autres verdicts d'identité : la seconde course est lue et rapportée comme fait, rien n'est prononcé sur la lentille.
Portée reprise du texte gelé (l. 61-65) : hors programme ; aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un préenregistrement
du programme sans nœud de Lazar ; aucune donnée réservée ni sonde du programme employée.

## 2. Prédiction chiffrée et signe attendu
R3 : aucune course ne vise un signe. **Aucune prédiction nouvelle** : ce plan ne porte pas d'hypothèse. Les prédictions de l'autrice du
texte gelé (« Prédiction chiffrée et signe attendu », l. 89-105) sont rapportées pour la seconde course, réfutées ou non telles
qu'écrites, **sans effet** sur aucun verdict ni sur la lisibilité (comme au plan v2, § 3.9).

## 3. Métrique et seuils : les critères gelés appliqués à la seconde course (recopiés avec leur source)
Le lecteur applique à la seconde course **le texte gelé et son addendum tels qu'ils sont écrits**, par la procédure du plan de lecture de
la tranche v2 (§§ 2 à 4), avec ses lectures en vigueur (§ 3.0, addendum § 1.1, l. 22-50), ses ambiguïtés tranchées (T-1 à T-6) et
ouvertes (O-1 à O-11, verdict sous chaque lecture, jamais arbitrées) et ses réserves (R-1, R-2). Sections appliquées : « Métrique »,
M.1 et M.2 (l. 107-164) ; « Seuil » (l. 166-189) ; « Chaîne en défaut », (a) à (s) (l. 191-253) ; « Critères de lecture gelés »
(l. 485-529) ; « P.7 Lecture » (l. 478-483). Les règles qui portent la lisibilité du palier 2 (§ 5) sont recopiées ici :

| règle | texte recopié | source |
|---|---|---|
| couche lisible | « n ≥ 48 pour la cible considérée ; une bande dont plus du quart des couches est non lisible rend la mesure « partielle » pour cette bande » | texte gelé, l. 125-126 |
| couche 31 | « la cible `out` de notre lentille R s'arrête à la couche 30 […] à la couche 31, notre R est **exactement** la lentille des logits dans `score` […] : ce n'est pas une mesure de lentille » | l. 122-124 |
| couches 28 à 31 | « Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3 » | l. 253 |
| B-1, grandeur | « `‖moyenne paire − moyenne impaire‖ / ‖moyenne‖` par cible et par couche, recalculée par notre code sur la machine, non arrondie » ; R : `out` 0 à 30, `mid` 0 à 31 ; S : `mid` et `out` 0 à 31 | l. 131-134 |
| B-1, seuils | « reproduit » : « différence entre moitiés ≤ 0,10 à chaque couche et chaque cible des deux lentilles **et** accord du premier jeton ≥ 0,80 aux six couches lues » ; « non reproduit » : « une couche d'une cible à plus de 0,20, **ou** un accord sous 0,60 à l'une des six couches » | l. 174 |
| B-2 | « reproduit » : `r_med` ≥ 0,40 (8–15), ≥ 0,60 (16–23), ≥ 0,85 (24–27) ; `pass` ≥ 0,90 (8–27) ; témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, à aucune hors de ±0,10 ; « non reproduit » : `pass` < 0,50 à plus de 6 des 12 couches 16–27, ou `r_med` < 0,30 à plus de 4 des 8 couches 16–23 | l. 175 |
| B-3 | « reproduit » : `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15 ; « non reproduit » : écart ≤ 0 à plus de 6 des 12 couches 4–15 | l. 176 |
| B-5 | « reproduit » : `read_S` ≥ 0,60 à la couche 0 **et** moyenne sur 1 à 7 au moins 0,10 au-dessus de la moyenne sur 12 à 23 ; B-5 lisible ; « non reproduit » : `read_S` < 0,30 à la couche 0, **ou** moyenne sur 1 à 7 au plus égale à la moyenne sur 12 à 23 ; B-5 lisible | l. 178 |
| B-5, lisibilité | « B-5 est « non lisible » (donc « partiel », jamais « reproduit » ni « non reproduit ») si la part silencieuse dépasse 0,40 à la couche 0, ou si sa moyenne sur les couches 1 à 7 dépasse 0,50 » | l. 158-161 |
| B-4, B-6 | rapportées, non décisives ; B-6 « accord », « intermédiaire », « désaccord » | l. 177, 179 |
| B-7 | « reproduit » : `r_med` < 0,25 à chaque couche 0–15 et ≥ 0,50 à chaque couche 26–29 ; « non reproduit » par le haut ou par le bas ; lue « pour un moniteur », hors verdict d'ensemble | l. 180, 507-513 |
| autre | « Toute mesure ni « reproduit » ni « non reproduit » est « autre » » | l. 182 |
| verdict d'ensemble | rang 1 chaîne en défaut (« aucun verdict de mesure ») ; rang 2 « non conclu » (« verdict final de la tranche ») ; rang 3 B-2 ou B-3 « non reproduit » → « non reproduit avec nos lentilles », réserve « défaut dans notre lentille » ; rang 4 B-1, B-2, B-3, B-5 « reproduit » → « reproduit avec nos lentilles » ; rang 5 « partiel », mesure par mesure | l. 487-497 |
| portée d'un « reproduit » | « Un « reproduit » dira que la lentille lit ce qu'une direction **pousse en moyenne**, pas qu'elle nomme le concept d'une invite donnée » | l. 496-497 |
| couches stables au palier 2 | « une couche n'est tenue pour stable que si `diffs` est au plus 0,10 **dans les deux ajustements** ; en variante B s'y ajoutent les limites que fixe la lecture de la seconde course » | critère v8, § 5 (l. 378-379) |
| grandeur qui décide de la stabilité | « `diffs` est la valeur que lisent les seuils de stabilité » | critère v8, § 4 (l. 266-268) |

**Ce qui n'est pas un critère de lecture et ne s'applique pas tel quel** : les conditions d'exécution de la liste d'arrêt du texte gelé
propres à la course du 18 (ligne GO-2026-11-18-02, plafond de 75 USD, fenêtre du 19 au 25 novembre, clé selon R-3151, relevé de prix,
gardes recalculées pour ce plafond et le lieu L1 ; l. 536-539 et 541 ; lieu L1, l. 395-396 et 571). L'addendum (l. 540) s'applique :
sa partie 1 est scellée, la partie 2 de la course neuve lui est comparée.
La seconde course part sous les décisions 1 à 3 du mot de Lazar du 22 novembre, le devis v9 (§ 3, § 5) et la commande v9 ; le lecteur
range un manquement à ces conditions comme le plan v2 range les arrêts de montage (§ 2.5 : écart à la liste d'arrêt, non le rang 1), en
citant la commande v9. Les arrêts de montage de la tranche qui portent sur la mesure (banc à 23,6 s, 932 documents, 466 et 466,
`rows_sha256` `a6afd972…`, Drowse 6.1.4 `673ed2b4…`, empreintes et licence, l. 542-547) s'appliquent tels quels.

## 4. Seconde course complète, ou arrêtée avant la fin de ses mesures
- **Complète** : la course a passé l'étape B6 du texte gelé (verdicts sur la machine, P.3, étape 7, l. 389-394) et, au commit des
  résultats noté au verdict d'identité (contrôle K1 du critère v8), les sorties de P.6 (l. 467-476) qui portent les sept mesures sont
  versées : sortie JSON de `score` (B-2, B-3, B-4, B-6, B-7 et les gardes calculées sur elle), grandeurs par pôle (n), sortie non arrondie
  de `lens_compare.py` (accord de B-1), sortie JSON de `reads_at_firings.py` avec la part silencieuse (B-5), résultats d'ajustement de R
  et de S (différences entre moitiés de B-1).
- **Arrêtée avant la fin de ses mesures** : l'une de ces sorties manque, ou la course s'est arrêtée (garde de dépense, minuterie, garde
  de crédit, perte de machine, arrêt de montage) avant l'étape B6. Alors (statut, § 3 ; critère v8, § 5) : la lentille du palier 2
  **reste sans mesure propre et est traitée comme en variante A** (aucune lecture sans nœud de Lazar) ; pour une lentille du palier 1, le
  verdict du 18 reste ; ce qui a été mesuré est rapporté comme information, sans aucune lisibilité prononcée.
- **Fichier des verdicts de la course absent, sorties présentes** : le lecteur calcule ses verdicts sur les sorties, rapporte
  l'absence en réserve (la comparaison de P.7 ne peut pas se faire) et ouvre un nœud de Lazar ; la lentille du palier 2 n'est pas dite
  lisible avant le mot de Lazar.
- Un audit déclenché non joué suit la règle de rang 2 du texte gelé (l. 491, 526-529) ; il n'est pas une course incomplète.

## 5. Palier 2 : sur quels critères gelés une lentille est dite lisible, et à quelles couches (fixé d'avance)
« Dite lisible » veut dire **seulement** : la lentille peut entrer dans un texte de lecture neuf, contre-lu, sous l'accord GO-2026-11-19-33
(critère v8, § 5), qui recopie son verdict d'identité et ses chiffres, le verdict de la seconde course, l'ensemble Λ de ses couches, les
désaccords et le mot de Lazar sur chacun. Ce n'est ni une identité, ni une qualité, ni une entrée dans le programme.

### 5.1 Conditions, toutes exigées, lentille par lentille
| n° | condition | source |
|---|---|---|
| P2-1 | verdict d'identité de cette lentille « palier 2 », écrit et scellé par la mère (critère v8, § 4 et § 8) | critère v8 |
| P2-2 | seconde course complète (§ 4) | statut ; critère v8, § 5 |
| P2-3 | verdict d'ensemble de la seconde course au rang 3, 4 ou 5 ; ni rang 1 (« aucun verdict de mesure » : la lentille n'a pas de mesure propre), ni rang 2 (« non conclu », verdict final) | texte gelé, l. 490-491 |
| P2-4, pour R | ni B-2 ni B-3 « non reproduit » (le rang 3 porte la réserve « défaut dans notre lentille ») | l. 492 |
| P2-4, pour S | B-5 ni « non reproduit » ni « non lisible » (B-5 est la seule mesure décisive propre à S) | l. 158-161, 178 |
| P2-4, pour les deux | B-1 non « non reproduit » (seuil écrit « des deux lentilles ») | l. 174 |
| P2-5 | aucun désaccord entre courses en attente du mot de Lazar (§ 6 ; statut, règle 4) | statut |
| P2-6 | aucune ambiguïté ouverte du plan v2 (O-1 à O-11) dont les lectures rendent des issues différentes pour P2-3, P2-4 ou Λ ; sinon les issues sous chaque lecture sont rapportées et un nœud de Lazar est ouvert | plan v2, § 4.2 |
| P2-7 | Λ non vide (§ 5.2) | — |

Une condition manquée : la lentille **n'est pas dite lisible** ; elle reste rangée avec sa mention ; aucune lecture sans nœud de Lazar ;
le lecteur écrit laquelle manque. Aucune condition ne peut être rattrapée par une autre ni par un audit.

### 5.2 Couches : l'ensemble Λ
- **Lentille R** : Λ(R) est l'ensemble des couches l de 0 à 30 telles que (i) `diffs` de R est au plus 0,10 pour la cible `out` **et**
  pour la cible `mid` à la couche l, **dans l'ajustement du 18 et dans celui de la seconde course** (critère v8, § 5 ; seuil de B-1,
  l. 174) ; (ii) la couche l est lisible dans la seconde course pour la cible « steer 1x » de notre R (n ≥ 48, l. 125). La couche 31
  n'appartient jamais à Λ(R) (l. 122-124).
- **Lentille S** : Λ(S) est l'ensemble des couches l de 0 à 31 telles que `diffs` de S est au plus 0,10 pour la cible `mid` **et** pour la
  cible `out` à la couche l, dans les deux ajustements. (S n'est pas notée par `score` ; sa lisibilité de mesure est celle de B-5, en
  P2-4.)
- `diffs` décide (critère v8, § 4) ; `diffs_float64` est rapportée à côté, couche par couche, et toute couche où les deux grandeurs
  tombent de côtés différents de 0,10 est nommée (sans effet sur Λ).
- **Limites portées avec Λ, sans restreindre Λ** : pour chaque couche de Λ, le texte de lecture recopie quelles bandes des mesures
  décisives la couvrent et leur libellé dans la seconde course (B-3 : 4–15 ; B-2 : 8–15, 16–23, 24–27 ; B-5 : 0, 1–7, 12–23 ; B-7, lu
  pour un moniteur : 0–15, 26–29) ; qu'aux couches 28 à 30 aucun verdict de B-2 ni de B-3 ne porte (l. 253) ; qu'une couche sans bande
  décisive (R : couches 0 à 3 hors B-1) n'a pour mesure que B-1 ; la portée d'un « reproduit » (l. 496-497) ; B-4 et B-6, rapportées non
  décisives.
- Rappel déclaré (R4) : le rédacteur connaît les couches que le 18 exclut ainsi de Λ d'avance (déclaration à part).

## 6. Désaccord entre la seconde course et le 18 : défini d'avance, sans seuil
Un **désaccord entre courses** existe si, sous au moins une lecture des ambiguïtés ouvertes, la même lecture étant prise des deux côtés (là où le verdict
du 18 ne distingue pas les lectures, son libellé unique vaut pour chacune), l'un de ces libellés des critères gelés
diffère entre le verdict du 18 (`3a9b947e…`) et le verdict du lecteur sur la seconde course :
- (a) le verdict d'ensemble (rang et libellé, l. 487-494) ;
- (b) le libellé d'une mesure : B-1, B-2, B-3, B-5 (« reproduit », « non reproduit », « autre » ; pour B-5 aussi « non lisible »), B-7
  (« reproduit », « non reproduit » par le haut ou par le bas, « autre »), B-6 (« accord », « intermédiaire », « désaccord ») ;
- (c) la présence d'une réserve des critères gelés (« défaut dans notre lentille », « écart de corpus », « écart d'ajustement ») ;
- (d) l'ensemble des chaînes en défaut constatées, ou l'ensemble des audits déclenchés, ou l'issue d'un audit joué.
**N'est jamais un désaccord** : une différence de valeur à libellés égaux, quelle qu'en soit la taille ; B-4 (sans libellé) ; une réserve
du lecteur hors critères gelés (par exemple les gardes sans trace complète, ambiguïté O-7). Ces différences sont **rapportées à côté**,
sans qualificatif.
**Tout désaccord est un nœud de Lazar** (statut, règle 4) : listé un par un, avec les valeurs des deux courses ; le lecteur ne le tranche
pas ; la lentille concernée par un désaccord est celle que lit la mesure en cause : R pour B-2, B-3, B-6 et B-7 ; S pour B-5 ; les
deux pour B-1, pour le verdict d'ensemble (a), pour les réserves (c) et pour les chaînes et audits (d) ; aucun texte de lecture qui emploie la lentille concernée n'est scellé avant le mot de Lazar. Pour une lentille du palier 1, le
verdict du 18 reste pendant le nœud ; pour une lentille du palier 2, elle n'est pas dite lisible pendant le nœud (P2-5).
**Ce qui est rapporté à côté, aux deux paliers** : la table du verdict du 18 (mesure, verdict, valeurs décisives et marges aux seuils)
refaite pour la seconde course, ligne pour ligne, avec la différence (seconde − 18) de chaque valeur comparée à un seuil, couche par
couche, sans tolérance ni qualificatif ; les deux marges que nomme le devis v9, § 2 (`pass` de B-2 à la couche 8 ; compte des couches de B-6) y figurent comme les autres, sans règle propre. Les grandeurs rapportées sans
critère du plan v2, § 2.4, le sont aussi.

## 7. Plan d'analyse : qui lit, quelles pièces, dans quel ordre
**Qui lit** : un lecteur neuf, sous-agent lancé par la mère ou par la session des lentilles sur un mandat écrit avant toute ouverture ;
il n'est ni auteur (du texte gelé, de l'addendum, du plan v2, de ce plan, du statut, du devis, du critère, du code de course, du
lanceur v4, des commandes v8 et v9) ni opérateur (de la session des lentilles ou de la course), ni l'agent qui a appliqué le critère
d'identité. Il déclare en tête ce qu'il savait avant de lire (R4) ; **avant l'étape F, il ne connaît du 18 que son
verdict d'ensemble, que porte le critère v8 (§ 1 et § 5) ; il n'a lu ni le verdict du 18, ni aucun libellé de mesure ni aucune valeur du
18.** Il ne lit, du critère v8, que son § 5 ; il ne lit ni le devis v9, ni les autres paragraphes du critère v8, ni les chiffres et
tables du verdict d'identité avant l'étape F. Un désaccord de lecture (son verdict contre le fichier des verdicts de la seconde course) est tranché par un second lecteur
neuf, sans nouvelle mesure (texte gelé, l. 480-481), avant l'étape F ; ce second lecteur est tenu à la même règle que le premier sur le
18.

**Pièces** : celles de la course neuve, aux noms de la tranche (plan v2, § 2.1 : catégorie 1, sorties brutes ; catégorie 2a, résultats
d'étape, journaux, manifeste ; catégorie 2b, verdicts et déclencheurs), lues **au commit des résultats noté au verdict d'identité**
(contrôle K1 du critère v8) — la tête de la branche de résultats lue après la destruction de la machine (critère v8, § 7, K1) — sur
la branche de résultats `calcul/neuron-lens-reajustement-v1`, et ce commit seulement ; la série repère
`bd57d519…` (garde (j)). Ce plan autorise cette lecture-là, et aucune autre de `calcul/*`. Le mandat du lecteur la recopie. Une pièce manquante ou
renommée est relevée ; une sortie du § 4 manquante rend la course « arrêtée avant la fin de ses mesures » ; une pièce renommée n'est
pas lue avant le mot de Lazar (nœud).
Les nouvelles pièces versées par le lanceur v4 (pièce du matériel, inventaire, croquis numérique) ne portent aucune mesure de la
tranche : la pièce du matériel est recopiée (carte, pilote, versions ; elle répond à la réserve 2 du 18), le croquis n'est pas lu.

**Ordre** :
- **Étape 0** — vérifier les empreintes de ce plan et du statut (compagnons), du texte gelé, de l'addendum, du plan v2, du critère v8 ;
  vérifier qu'un verdict d'identité scellé existe pour chaque lentille, et n'en lire que la mention de chaque lentille, le commit K1 et
  l'identifiant de course, sur un extrait scellé que la mère remet avec le mandat ; les chiffres et les tables du verdict d'identité (qui
  portent les écarts de `diffs` entre les deux courses, donc des valeurs du 18) ne sont lus qu'à l'étape F. Un écart, un verdict
  d'identité absent ou un extrait absent : arrêt, rien n'est ouvert.
- **Étape A** — le lecteur écrit son script (Python, processeur, lecture `json`), sans importer ni relire le code des verdicts de la
  course ni aucun script de lecture du 18 ; il l'essaie (R5) sur les cas gelés de P.4 rejouables sur des tables, comme le plan v2,
  étape A, **et** sur des cas faits à la main pour les §§ 5 et 6 (un sain et au moins un artefact pour chaque condition P2-1 à P2-7, pour
  Λ, et pour chacun des cas (a) à (d) du désaccord, et pour l'audit de symétrie entre courses (un cas sain
  égal au bit de provenance neuve, un artefact qui relit les pièces du 18)). Sortie de l'essai scellée.
- **Étapes B, C, D, E** — celles du plan v2 (§ 2.3), appliquées aux pièces de la course neuve, avec la procédure « structure d'abord »
  (§ 2.2), chaque sortie scellée avant l'étape suivante.
- **Étape S** — **verdict du lecteur sur la seconde course, scellé** (verdict d'ensemble, sept mesures, chaînes, audits, réserves,
  ambiguïtés sous chaque lecture, prédictions de l'autrice rapportées), avant toute ouverture d'une pièce du 18.
- **Étape F** — seulement ensuite : le verdict du 18 (`3a9b947e…`), le verdict d'identité entier et, pour Λ, les champs `diffs` et `diffs_float64` des deux pièces
  d'ajustement du 18 (`129c43b0…`, `2dce646e…`), et, pour l'audit de symétrie (§ 8), l'identifiant de course, l'empreinte du
  manifeste et les compagnons des sorties brutes du 18 ; le script calcule la table rapportée à côté, les désaccords (§ 6), les conditions
  P2-1 à P2-7 et Λ (§ 5) pour chaque lentille du palier 2. Sortie scellée.
- **Étape G — rendu** : `docs/notes/neuron-lens-v1/lecture-reajustement/verdict-lecture-seconde-course-reajustement-v1.md`, scellé
  (dossier neuf ; les pièces des étapes A à F à côté, chacune scellée) : verdict d'abord ; par lentille, verdict d'identité recopié,
  ce que la seconde course est pour elle (statut, § 3), au palier 2 lisible ou non, laquelle des conditions manque, Λ ; désaccords, chacun
  avec son nœud ; table rapportée à côté ; réserves ; mentions du plan v2, § 2.7. Le verdict est rapporté à Lazar par la mère.

**Graines** : aucun tirage dans la lecture ; les graines de la course sont celles du texte gelé (P.5), recopiées du manifeste neuf.
**Comparaisons multiples** : règles de seuils couche par couche, sans test d'hypothèse, aucune correction ; intervalles rapportés sans
servir au verdict (texte gelé, l. 481-483). **Aucun rejeu** d'audit, de mesure ni de calcul qui demande les lentilles ou une machine.

## 8. Critères de lecture gelés (issue → ce qui est écrit)
| issue | ce qui est écrit |
|---|---|
| verdict d'identité absent ou non scellé | rien n'est ouvert |
| lentille « différente », « non comparable », mention suspendue, non réajustée | la seconde course est lue et rapportée comme fait ; « elle n'est pas lue ici » (critère v8, § 5) ; aucune lisibilité |
| palier 1, aucun désaccord | phrase du palier 1 du statut, § 4, et « la seconde course rend les mêmes libellés que le 18 » ; table rapportée à côté ; le verdict du 18 décrit la lentille (critère v8, § 5) ; si l'autre lentille n'est pas au palier 1, seules les mesures du 18 faites sur cette lentille la décrivent, et ni le verdict d'ensemble ni B-1 ne se transportent tels quels ; phrase du palier 1, une seule lentille, du statut, § 4 |
| palier 1, désaccord | phrase du palier 1 ; liste des désaccords ; nœud de Lazar ; le verdict du 18 reste ; aucun texte de lecture qui l'emploie n'est scellé avant le mot |
| palier 2, seconde course complète, P2-1 à P2-7 tenues | « lentille [R \| S] dite lisible, aux couches Λ = […], dans les limites de cette lecture » ; phrase du palier 2 du statut et du critère v8, § 5 |
| palier 2, désaccord | conditions calculées et rapportées ; nœud de Lazar ; lisibilité non prononcée avant le mot (P2-5) |
| palier 2, une condition manquée | « non dite lisible : [condition] » ; rangée avec sa mention ; aucune lecture sans nœud de Lazar |
| palier 2, seconde course arrêtée avant la fin de ses mesures | « sans mesure propre ; traitée comme en variante A » ; le billet le dit |
| ambiguïté ouverte qui change une issue des §§ 5 ou 6 | issues sous chaque lecture ; nœud de Lazar ; rien n'est arbitré |
| désaccord de lecture (lecteur contre fichier des verdicts) | second lecteur neuf, sans nouvelle mesure, avant l'étape F |

**Audit de symétrie entre courses (R4), le même dans les deux sens** : si **toutes** les valeurs comparées sont égales au bit entre les
deux courses, ou si **tous** les libellés diffèrent, le lecteur vérifie, avant tout rendu, que les pièces lues sont celles de la course
neuve : identifiant de course et empreinte du manifeste différents de ceux du 18, pièces égales à l'octet aux fichiers du commit K1,
empreintes des sorties brutes des deux courses relevées et rapportées (leur égalité, seule, n'est pas un contrôle
manqué). Un contrôle manqué : arrêt, rien n'est rendu, nœud de Lazar. Sinon l'issue
tient et l'observation est rapportée en réserve (trop propre ou tout différent). À l'intérieur de la course, les audits A1 à A6 du
texte gelé s'appliquent tels quels.

## 9. Ce qui n'est jamais conclu
- Que la lentille du palier 2 est celle du 18, lui est « proche », « équivalente », ou que le verdict du 18 la décrit (critère v8, § 5).
- Que la seconde course « confirme », « infirme », « révise » ou « consolide » le verdict du 18 ; qu'une mesure est « robuste » ou
  « stable » au changement de machine ; un effet du matériel en général (une seule paire de courses).
- Qu'une lentille dite lisible est « bonne » au-delà des libellés gelés ; qu'un « reproduit » nomme le concept d'une invite (l. 496-497) ;
  qu'une lecture par lentille blanchit une sonde (règle du texte gelé v6 : elle peut ajouter un soupçon, jamais blanchir).
- Quoi que ce soit pour le programme, une hypothèse ou une revendication (T0.7, T0.8, G0, G1, préenregistrements : nœud de Lazar).
- Une moyenne, une fusion ou un choix « meilleur » entre les deux courses.

## 10. Liste d'arrêt
| condition | action |
|---|---|
| ce plan ou le statut non contre-lus ou non scellés avant la création de la machine | la variante B ne part pas (devis v9, § 5, point 7) |
| empreinte d'un document qui fait foi différente | arrêt à l'étape 0 ; rien n'est ouvert |
| verdict d'identité non scellé | rien n'est ouvert |
| lecteur qui n'est pas neuf, ou qui a lu avant l'étape F le verdict du 18, un libellé de mesure ou une valeur du 18 hors de ce que permet le § 7 | il ne lit pas ; un autre lecteur neuf est lancé |
| pièce du 18 ouverte avant le scellement de l'étape S | déclarée ; ce lecteur ne rend aucun verdict ; un autre lecteur neuf est lancé |
| pièce du 18 ouverte après le scellement de l'étape S, hors de l'ordre de l'étape F | déclarée ; le verdict de l'étape S déjà scellé reste |
| lecture d'une branche, d'un commit ou d'un chemin hors du § 7 ; toute lecture touchant P3, P3-bis, T0.6, T0.7, l'apprentissage des sondes sur la tâche, ou un chemin interdit par le mandat du lecteur | interdit ; arrêt ; nœud |
| rejeu, mesure ou calcul qui demande les lentilles, le fichier `-causal.pt` ou une machine | interdit ; aucune reprise sans devis neuf et mot de Lazar |
| audit de symétrie entre courses (§ 8) en échec | arrêt ; rien n'est rendu ; nœud |
| refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; déclaré ; arrêt ; nœud |
| envie d'écart à ce plan | écrite, datée, version nouvelle (R12), contre-lue, **avant** toute ouverture d'une pièce de la seconde course ; après ouverture, aucun écart : le plan s'applique tel quel, et un cas qu'il ne règle pas est un nœud de Lazar |

## 11. Choix du rédacteur, nommés pour la contre-lecture (aucun ne crée de seuil)
1. **Désaccord sur les seuls libellés gelés** (§ 6). Sans définition écrite, « tout désaccord » serait jugé après coup ; une tolérance sur
   les valeurs serait un critère nouveau (le devis v2 a retiré le seuil de 0,03, remarque M-2).
2. **Exclusions par le rang et par mesure** (P2-3, P2-4). Alternative : n'exclure sur aucun libellé et porter seulement les limites,
   comme au palier 1. Retenue parce que les rangs 1 et 2 ne laissent pas de mesure conclue, et que le rang 3 nomme un « défaut dans notre
   lentille » ; l'exclusion de S sur B-5 et des deux lentilles sur B-1 suit la même règle, appliquée aux mesures décisives propres.
3. **Λ fixé par la stabilité et la lisibilité, non par les bandes** (§ 5.2). Restreindre Λ aux couches des bandes « reproduit »
   transformerait un critère de bande en critère de couche : refusé ; les bandes sont portées comme limites.
4. **Cible « steer 1x »** pour la lisibilité des couches de R : c'est celle des mesures décisives B-2 et B-3 ; les n des autres cibles
   sont rapportés.
5. **Conditions d'exécution** de la liste d'arrêt du 18 remplacées par celles du devis v9 et de la commande v9 (§ 3), sous le mot de
   Lazar du 22 novembre (décisions 1 à 3) ; aucun critère de lecture n'est touché. Si la contre-lecture y voit un écart au texte gelé
   scellé, c'est un nœud de Lazar avant la création. La ligne de la
   clé (texte gelé, l. 538, R-3151) est tenue par la décision 3 et par la création de la clé restreinte par Lazar ; la mère consigne, au
   moment de la commande, le mot de Lazar qui la passe à la machine, ou ouvre le nœud.
6. **Lecture de la branche de résultats au seul commit K1** (§ 7), que le plan v2 n'autorisait pas pour sa propre course sans mandat.
7. **Toutes les cibles au plus 0,10** pour Λ (§ 5.2) : le critère v8, § 5, ne nomme pas la cible ; la lecture « chaque cible » est celle
   du seuil de B-1 (texte gelé, l. 174).
8. **Rang 5 admis, exclusions sur « non reproduit » et non sur « autre »** (P2-3, P2-4) : au palier 1, le critère v8, § 5, écrit avant
   ce plan, laisse les mesures du 18 décrire la lentille « avec leurs limites (verdict « partiel », couches stables du 18) » ; admettre le
   rang 5 au palier 2 est la même règle ; « autre » est le libellé des mesures partielles que le rang 5 admet. Choix fait en connaissant
   les libellés du 18 (déclaration à part), soumis comme tel à la contre-lecture. L'exclusion des deux lentilles sur B-1 « non
   reproduit » peut retenir S pour un défaut de R ; elle est gardée parce que le libellé gelé porte sur les deux lentilles.

## 12. Contre-lecture
À faire par un sous-agent neuf d'un autre modèle (le mot de Lazar nomme Sonnet 5.5 ; une contre-lecture par le modèle du rédacteur ne
remplit pas cette exigence et est déclarée comme telle) (mot de Lazar du 22 novembre, « Écart d'usage déclaré »), sur ce brouillon et sur le
statut, avec les documents qui font foi ci-dessus ; empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque
remarque (acceptée, refusée et pourquoi) dans le brouillon suivant.
