# Reprise par segments du noyau — v1 (25 octobre 2026)

Lignée « conv-audit », branche `outils/noyau-reprise-segments-v1`, à partir de `b1c7f4b6` (le noyau des pilotes 2 à 4).
Décision de Lazar (25 octobre 2026, 20:23 Paris, dans la session de conv-audit) : « b) Attendre la reprise par
segments » — le pilote 4 ne part pas avant que le noyau sache continuer une course en plusieurs commandes de fond
(chacune bornée à 7 200 s chez session-depot).

## 1. Ce que fait la reprise

- Une course arrêtée par `STOP` **entre deux unités** (une unité = une ronde de conception ou une génération d'une
  lignée ; le noyau ne lit `STOP` qu'entre deux unités, jamais pendant) écrit son état dans `course/reprise/etat-vN.json`,
  scellé (compagnon `.sha256`), protégé (dossier 0700, fichiers 0600), jamais réécrit (R12 : un arrêt de plus, un `vN`
  de plus). Aucun événement n'est ajouté par l'écriture : l'état compte les événements de la course, arrêt compris.
- `Noyau.reprendre()` (à appeler à la place d'`amorcer()`, sur un noyau neuf construit avec les mêmes paramètres, puis
  `boucler()`) continue la course **à la première unité qui n'a pas tourné** : les lignées, la dépense, le nombre
  d'appels, le numéro de ronde, l'avancement de la conception et la ronde en cours (son ordre tiré, ses lignées faites,
  sa vue figée en mémoire partagée) sont relus de l'état ; les graines sont celles de la course (même entropie, mêmes
  lignées, même indice de lignée) ; rien n'est rejoué ni sauté. Un événement `reprise` consigne le segment, l'état relu
  (nom, empreinte), la ronde en cours, la dépense relue, et ce qui est propre à ce lancement (heure, machine, extrait du
  registre des GO, chemins des pièces servies). Le manifeste du rapport reste celui de la course ; le rapport dit le
  numéro du segment (`segments`) et les reprises (`reprises`).
- Un STOP lu pendant la conception arrête la course là : aucune génération notée ne part dans ce segment, même si le
  STOP disparaît entre-temps. Un STOP posé pendant la **dernière** unité (plus aucune lignée active ensuite) ne laisse
  rien à reprendre : la course finit « aucune lignée active », sans état ni segment de plus (comme la course continue).

## 2. Refus (rien n'est écrit)

`reprendre()` lève `Arret` : sur un noyau déjà amorcé ; sans état ; état qui ne correspond pas à son compagnon, d'une
autre version, ou d'un arrêt autre que STOP ; `STOP` encore dans la course (le lanceur le retire avant) ; course qui a
bougé depuis l'état (nombre d'événements — donc **jamais deux reprises du même état** —, dernier événement autre que
l'arrêt sur STOP, manifeste, index de l'archive) ; lancement qui diffère de la course sur un champ de `CHAMPS_REPRISE`
(bornes, graine, banque, mission, code et commit, versions, isolation, espace des organismes, clés présentes, sources de
moisson, question, vivier, traits…) ou sur les organismes imposés (famille, empreinte d'arbre ; leur chemin peut
changer) ; ronde en cours illisible ou incohérente ; vue figée introuvable (mémoire partagée) ; organisme d'une lignée
hors de la course (course déplacée ou état altéré) ou introuvable ; crédit d'un fournisseur épuisé pendant la course ;
plafond total atteint.

## 3. Entrée de commande

`python -m essaim_m3 simuler|lancer … --reprendre` : mêmes arguments que la course (refus sinon), `--sortie` de la course
existante, `STOP` retiré ; sans `--graine`, l'entropie de la course est relue de son manifeste. Codes : 8 — course
existante sans `--reprendre` (une course n'est jamais relancée par-dessus elle-même), `--reprendre` sans course, ou avec
`--depuis` ; 9 — reprise refusée par le noyau (motif sur la sortie d'erreur).

## 4. Fichiers changés

- `essaim_m3/noyau/boucle.py` : `CHAMPS_REPRISE`, `_projection_reprise`, état du segment dans `__init__`,
  `_tourner_ronde` (une ronde se continue, jamais ne se retire), `concevoir` et `boucler` (rondes en cours, arrêt et état
  sur STOP), `_ecrire_etat_reprise`, `reprendre`, `_reprises`, `segments` et `reprises` au rapport.
- `essaim_m3/noyau/cli.py` : `--reprendre`, `_refus_reprise`, `_entropie_de_la_course`.
- `tests/test_reprise_segments.py` : 28 essais (voir § 5).

Rien d'autre du noyau ne change : contrat des organismes, contexte servi, graines, juge, archive, extrait mécanique.
Une course sans STOP est inchangée (les 141 essais de `b1c7f4b6` passent tels quels).

## 5. Essais

Course continue de référence contre la même course en segments (espèces simulées dont la réponse ne dépend que de la
consigne) : même journal (graines, rondes et leur ordre, unités, fins), même archive (empreintes des organismes
comprises), même rapport, dépense jamais comptée deux fois — STOP après la ronde de conception 1, après la ronde 2
(conception finie constatée à la reprise), après la génération 0, après la génération 1, trois arrêts dans la même
course ; STOP posé **pendant** une unité (elle finit et s'archive) ; deux lignées avec STOP après la première lignée de
chaque ronde (ronde continuée sans nouveau tirage, en mémoire privée et partagée) ; STOP retiré juste après l'arrêt de
la conception (aucune génération dans le segment) ; STOP pendant la dernière unité (aucun segment de plus). Artefacts :
chaque refus du § 2, journal et rapports inchangés après chaque refus ; entrée de commande (codes 8 et 9, entropie
relue). Contrôle des essais (R4) : douze mutations volontaires du noyau (ronde en cours non rétablie, conception déclarée
faite après STOP, dépense non relue, ronde sautée, garde du journal retirée, ordre des lignées inversé, lignées faites
rejouées, numéro de ronde décalé, STOP ignoré dans la ronde, état non écrit, conception suivie de générations, STOP
honoré sans unité restante) : **chacune fait échouer les essais** (`mutations-v1.txt`, `mutations-v2.txt` ; le fichier
d'origine est rétabli et vérifié par empreinte après chaque mutation).

Suite complète : `suite-complete-v1.txt`.

## 6. Ce que le lanceur doit faire (pour le pilote 4)

Le minuteur pose `STOP` ; le noyau finit l'unité en cours, écrit l'état, rend le code 0. Au segment suivant, le lanceur
vérifie l'état (compagnon, arrêt sur STOP), retire `STOP`, relance la même commande avec `--reprendre`, et ne ferme
l'archive qu'à la fin de la course. Borne de temps : une unité dure au plus `temps_max_s` + `ATTENTE_FILS_S` (900 s
d'attente des appels en vol) + le dépôt ; l'échéance du minuteur doit laisser cette durée, plus la fermeture, sous les
7 200 s de la commande de fond.
