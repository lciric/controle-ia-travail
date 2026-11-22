# Vérification des brouillons 2 des deux textes de la variante B (statut de la seconde mesure, plan de lecture de la seconde course) — v1

- Vérificateur : sous-agent neuf, Sonnet 5.5 (`claude-sonnet-5-5`), branche `claude/brave-galileo-jhp684`, tête `aad8e9b3b`. Je n'ai écrit aucune des pièces ; je ne suis ni le modèle de leurs auteurs (Opus 5.5) ni celui de leur premier contre-lecteur.
- Empreintes recalculées par `controle_ia.scellement verifier` : toutes OK et égales à celles de la demande : statut brouillon 2 `42ca377a…`, plan brouillon 2 `93a3dd33…`, déclaration `57c98aa5…`, gabarit `2705b3ad…`, brouillons 1 `561e8ac2…` et `ed802f8d…`, contre-lecture `a92149e8…`, consigne `5499ffeb…`.
- Méthode : `diff` brouillon 1 contre brouillon 2 de chaque texte, comparé à chacune des 19 corrections ; recopie de la déclaration comparée par programme (espaces normalisés) aux brouillons 1 ; lecture des documents qui font foi (devis v9 § 4 et § 5 point 7 et décision 4 ; critère v8 § 5 ; plan de la tranche et texte gelé par les lignes que les textes citent).

## Verdicts
- Statut, brouillon 2 : **bon à sceller**, avec une correction non bloquante (nom du plan).
- Plan, brouillon 2 : **à corriger** : une correction bloquante (le lecteur n'est pas empêché d'ouvrir les pièces du dossier qui portent des valeurs du 18, dont le brouillon 1 du statut que le plan nomme lui-même) et quatre non bloquantes.

## Point 1 — les 19 corrections
Toutes faites, telles quelles ; le `diff` ne montre aucune autre différence que le titre et le bloc « Différences avec le brouillon 1 » (annoncés par le correcteur) et les coupures de ligne.
- Statut : S-1 (§ 3 ligne palier 1, cas mixte) faite ; S-2 (deux phrases du palier 1, avec la parenthèse anglaise) faite ; S-3 faite ; S-4 (puce de la déclaration, renvoi à la déclaration à part ; règle 1 « Le verdict du 18 ») faite ; S-5 faite ; S-6 faite ; S-7 faite.
- Plan : P-1 (§ 7 et ligne de § 10) faite ; P-2 a, b, c faites ; P-3 (étape 0 et étape F) faite ; P-4 faite ; P-5 faite ; P-6 (§ 8 et § 1) faite ; P-7 (une ligne remplacée par deux) faite ; P-8 (§ 8, étapes A et F) faite ; P-9 (choix 5, 7, 8) faite ; P-10 faite ; P-11 (K1, mandat, second lecteur) faite ; P-12 faite.
- Le tableau de lignes des deux blocs « Différences » est exact sur les points sondés (S-1 l. 92, P-9 l. 325-331, etc.) et la mention « Corrections non faites telles quelles : aucune » est vraie.
- Remarque de forme, non bloquante : P-1 écrit que le lecteur connaît le verdict d'ensemble que porte le critère v8 « § 1 et § 5 » mais ne lui fait lire que le § 5 ; c'est le texte exact de la contre-lecture, laissé tel quel ; sans effet.

## Point 2 — consigne, points 1 à 6, sur les brouillons 2
1. Conformité (devis v9 § 4 et § 5 point 7, décision 4, critère v8 § 5) : **tenu** pour les deux textes. Le cas mixte du palier 1, la fin de phrase du palier 2 pour une course arrêtée, la définition de la lentille concernée sont conformes au § 5 du critère. Les deux textes recopient « le verdict du 18 reste ; la seconde course est rapportée à côté ; tout désaccord est un nœud de Lazar ».
2. Aucun critère ni seuil neuf : **tenu**. Aucun chiffre ajouté ; les ajouts (cible, rang 5, exclusions) sont nommés au § 11 du plan comme choix (7 et 8) et soumis à contre-lecture.
3. Tout fixé d'avance : **tenu** après P-4, P-5, P-7, S-7 (lentille concernée, lecture identique des deux côtés, ligne d'arrêt non contradictoire).
4. Rien de plus que le texte gelé : **tenu** (S-2, S-5, § 9 du plan).
5. Cohérence : **à corriger, non bloquant**. (a) le plan, § 8, ligne « palier 2, arrêtée… », dit « le billet le dit » sans renvoyer à la fin de phrase que S-6 fixe dans le statut ; (b) les deux brouillons 2 se désignent l'un l'autre par le nom du brouillon 1 (plan : tableau des documents, ligne « statut » ; statut : § 1, plan) ; pour le plan c'est aussi un défaut d'aveuglement (point 4 ci-dessous).
6. Autre écart bloquant : le chemin d'exposition du point 4.

## Point 3 — ajout du correcteur (§ 4 de la déclaration à part)
**Acceptable.** Les deux marges retirées du plan par P-2 (c) portent des valeurs du 18 ; la contre-lecture ne dit pas où elles vont, la déclaration à part est précisément le lieu de ce que le lecteur ne lit qu'à l'étape F, et l'ajout est annoncé, signalé comme non demandé et justifié. Aucune valeur nouvelle n'est exposée (elles sont déjà dans le brouillon 1 et dans la contre-lecture). Je confirme par programme que les quatre blocs de la déclaration sont recopiés mot pour mot des brouillons 1 (statut l. 25-27 ; plan l. 40-46, 152, 170-171). Le gabarit de l'extrait ne porte aucun chiffre et colle à l'étape 0 révisée (mention, commit K1, identifiant de course).

## Point 4 — chemin d'exposition : le plan ne le ferme pas
Le § 7 (« Qui lit ») limite le lecteur au § 5 du critère v8, sans le devis v9 et sans les chiffres du verdict d'identité, mais **ne ferme pas les autres fichiers du dossier** `textes-variante-b/` : brouillons 1 (statut l. 25-27, plan l. 40-46, 152, 170-171 : libellés, valeurs, couches), contre-lecture (rappelle les marges chiffrées et que B-1 et B-2 étaient « autre » le 18), déclaration à part, relectures. La seule fermeture écrite est « un chemin interdit par le mandat du lecteur » (§ 10), qui renvoie à un mandat non encore écrit. Pire, le tableau des documents du plan nomme comme statut à lire `statut-…-brouillon1.md`, qui porte les valeurs du 18. Correction demandée : C-1 et C-2 ci-dessous.

## Corrections demandées (à faire mot pour mot dans un brouillon 3 du plan, et du statut pour C-5)
- **C-1 (bloquante, plan).** § 7, « Qui lit », après la phrase finissant par « …tenu à la même règle que le premier sur le 18. » insérer : « Du dossier `docs/notes/neuron-lens-v1/devis-reajustement/textes-variante-b/` et de `docs/notes/neuron-lens-v1/lecture-b-beta/`, il ne lit que les versions scellées de ce plan et du statut ; il ne lit ni leurs brouillons, ni la contre-lecture, ni les relectures et leurs consignes, ni la déclaration du rédacteur (qu'il ne lit qu'à l'étape F), ni aucun autre fichier de ces dossiers avant l'étape F ; le mandat du lecteur recopie cette liste. » Et § 10, ligne « lecteur qui n'est pas neuf… » : remplacer « hors de ce que permet le § 7 » par « , ou un fichier de ces dossiers hors de ce que permet le § 7 ».
- **C-2 (bloquante, plan).** Tableau « Documents qui font foi », ligne « statut de la seconde mesure » : remplacer « `…/statut-seconde-mesure-reajustement-v1-brouillon1.md` (ou la version scellée qui le remplace) » par « la version scellée du statut de la seconde mesure, dans ce dossier (`statut-seconde-mesure-reajustement-v1.md` ou le nom qu'elle prend, d'après son compagnon `.sha256` ; aucun brouillon) ». Même ligne du tableau pour « accord de Lazar » et « verdict du 18 » : ajouter en fin de ligne « (non lu par le lecteur avant l'étape F) ».
- **C-3 (non bloquante, plan).** § 8, ligne « palier 2, seconde course arrêtée… » : remplacer « le billet le dit » par « le billet le dit (statut, § 3, ligne « arrêtée avant la fin de ses mesures ») ».
- **C-4 (non bloquante, plan).** § 7, étape 0 : après « sur un extrait scellé que la mère remet avec le mandat » insérer « (forme : `gabarit-extrait-verdict-identite-v1.md`, `2705b3ad…`) ».
- **C-5 (non bloquante, statut).** § 1 : remplacer « `plan-lecture-seconde-course-reajustement-v1-brouillon1.md`, dans ce dossier, ou la version scellée qui le remplace » par « la version scellée du plan de lecture de la seconde course, dans ce dossier (aucun brouillon) ».
- Hors ces corrections, à la mère avant le scellement final : retirer des versions finales le bloc « Différences avec le brouillon 1 » (ils décrivent des brouillons) ; la contre-lecture par un autre modèle que le rédacteur est celle-ci ; elle ne vaut pas relecture par Fable (confirmation annoncée après le 24 novembre).

## Point 5 — autres écarts bloquants
Aucun autre.

## Exposition du vérificateur (R4)
J'ai lu les deux diffs (donc les libellés et valeurs du 18 que portaient les brouillons 1 : couches, `pass`, marges), la déclaration à part en entier, la contre-lecture en entier, les deux brouillons 2 en entier, les passages cités du critère v8 (§ 5), du devis v9 (§ 4, § 5 point 7, début) et de la consigne. Je n'ai ouvert ni le verdict du 18, ni l'accord de Lazar, ni `diag/`, `runs/`, `docs/verdicts/`, ni aucune branche `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*`, ni aucune pièce interdite par la demande ; aucune requête réseau ; aucun refus d'outil. Je n'ai pas relu le texte gelé ligne à ligne : les lignes qu'il cite ont été jugées d'après les citations et la contre-lecture, sauf pour la correspondance au critère v8, § 5, que j'ai lu.
