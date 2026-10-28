# Brief — script de lecture contre le bruit du pilote 4, v3

De : conv-audit, le 2026-10-26 à 05:48:09 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).
À : l'auteur des v1 et v2 du script (toi, relancé). Les briefs précédents restent valables sauf ce que celui-ci change.

## 1. Ce qui est demandé

Écrire, sous `/var/tmp/lecture-pilote4-v3/` seulement : `lire_pilote4_v3.py`, `essais_lire_pilote4_v3.py`, le journal
`essais-lire-pilote4-v3.log`, `LISEZMOI-script-lecture-v3.md` (avec une table « constat → traitement » pour RSL2-01 à
RSL2-08 et pour les points du § 3 ci-dessous), chacun avec son compagnon `.sha256`. La v2 reste intacte. Les calculs de
la v2 ne changent pas (ils sont jugés justes deux fois) ; ne touche aux fonctions de calcul que si un point ci-dessous
l'exige, et dis-le.

## 2. Pièces

Dans `fournis/` :

- `rapport-relecture-script-lecture-v2-sur-v2-v2.md` (`3cdf052c…`) : la seconde relecture, « utilisable après
  corrections », RSL2-01 à RSL2-08. **À lire en entier.** Ses outils et journaux sont sous
  `/var/tmp/relecture-script-lecture-pilote4-v2/` (`outils/`, `journaux/`) : tu peux les lire et reprendre ses paires de
  non-interférence.
- `rapport-verification-boucle-exterieure-v3.md` (`1a7873e2…`) : la vérification de la boucle extérieure. Te concernent
  CLB3-01, CLB3-06 et CLB3-07 (b) ; le reste est pour l'auteur de la boucle.
- `pilote4-gemini-organisme-v5.md` (`1943f39a…`) : le texte du pilote, qui prime (table de correspondance, § Plan, points
  3 et 4).

Ta v2 est sous `/var/tmp/lecture-pilote4-v2/`.

## 3. Décisions de conv-audit, à appliquer telles quelles

1. **Sorties** (CLB3-01). Plus aucun mode « provisoire » : il est retiré, avec ses fichiers. La v3 écrit :
   - pour une course, à sa fin : `lecture-<dossier>-test-v3.{json,md}`, la part `test` seule ;
   - à la fin de la course S, pour **chacune** des deux courses : `lecture-<dossier>-test-final-holm-quatre-v3.{json,md}`,
     **une course par fichier**, Holm sur les quatre tests (deux par course), **aucune valeur de l'autre course** : ni
     compte, ni proportion, ni borne, ni valeur p, ni libellé, ni signalement ;
   - si la course S ne court pas ou ne finit pas saine (option `--sans-seconde-course`) :
     `lecture-<dossier de M>-test-final-holm-deux-v3.{json,md}`.
   Le mode `test` lit une course et n'écrit que son fichier `test` ; le mode `test_final` lit les deux courses (ou M seule
   avec l'option) et n'écrit que les fichiers `test_final`. Forme des commandes : la tienne, écrite au LISEZMOI.
2. **Ce qu'un fichier `holm-quatre` porte pour chacun de ses deux tests (iii)** : la valeur p brute de ce test, son sens
   (point 4), et son libellé sous Holm à quatre (« rejeté au niveau 0,05, famille de quatre » ou « non rejeté »). **Jamais**
   la valeur p ajustée (elle peut égaler un multiple de la valeur p d'un test de l'autre course), ni le rang du test parmi
   les quatre, ni le seuil appliqué (il donne le rang). Les autres éléments de `test_final` (intervalles, cellules,
   sous-ensembles) sont ceux de la course seule, comme en v2.
3. **Séparation entre courses, essayée** (R5) : paires de non-interférence, sur données synthétiques à valeurs disjointes
   par construction : (a) faire varier la part `test_final` de S sans changer les libellés de Holm de M → fichier
   `holm-quatre` de M identique, hors de l'heure et des empreintes ; et la réciproque pour S ; (b) l'union des deux fichiers
   rend les lignes (iii) du calcul joint (libellés et valeurs p brutes) ; (c) artefact : une valeur de l'autre course
   plantée dans le contenu d'un fichier avant son écriture → refus (le script vérifie, avant d'écrire, qu'aucune valeur
   propre à l'autre course n'apparaît : comptes b et c, valeurs p, exactitudes, bornes ; dis comment tu évites les
   coïncidences de valeurs, par exemple en ne cherchant que les valeurs qui diffèrent entre les deux courses).
4. **Libellés de `test_final`** (CLB3-06 a) : pour chaque test (iii), le **sens du rejet** : « génération 3 au-dessus de
   la génération 0 » (b > c), « génération 3 au-dessous de la génération 0 » (b < c), ou « sans objet (non rejeté) » ; et,
   par cellule de `test_final`, **« aucune tâche sans réponse »** : oui ou non.
5. **Phrase (iv)** (RSL2-01, CLB3-06 d), mot pour mot, dans les deux fichiers : « tout le reste est « dans le bruit » : à
   une graine par course, le bruit entre graines n'est pas mesuré ; aucune comparaison entre les deux courses n'est faite
   (mêmes tâches, même objet, questions différentes : un écart entre elles tient à la question, à la graine ou au bruit,
   sans moyen de les séparer ; les verdicts des agents de la boucle extérieure restent tenus par cet interdit) ; un
   changement au-delà du bruit des tâches dans une course peut tenir à sa graine ». Citer le texte v5 à côté de « point
   4 bis du texte v4 ».
6. **Ligne d'état** (RSL2-02, CLB3-07 b) : ne compter que les signalements du fichier `test` : « signalements (fichier
   test) : N ». Réponse à la question de RSL2-02 : **tous** les signalements qui touchent `test_final` (écart avec le noyau
   sur `test_final`, `score-final.json` absent, illisible ou sans la famille, test (iii) impossible, générations de la
   seconde course) restent dans les fichiers `test_final` seulement ; aucun n'est rangé avec les signalements communs. Le
   mode `test` ne lit `score-final.json` pour rien. Adapter l'essai qui exigeait le mélange.
7. RSL2-03 : compter les entrées écartées par part ; les identifiants inconnus à part (signalement commun).
8. RSL2-04 : dans le fichier `test`, remplacer l'empreinte de `reponses-lues.json` (et du repli) par celle de la seule
   projection `test` des réponses (JSON canonique des entrées de `test`, règle écrite au LISEZMOI) ; l'empreinte du fichier
   entier va aux fichiers `test_final`.
9. RSL2-05, RSL2-06, RSL2-07, RSL2-08 : comme le dit le rapport (chemin ajouté à `definitifs` avant d'écrire ; dire que
   l'écriture est faite ; documentation exacte de ce que la séparation et ses essais couvrent ; paires de non-interférence
   et drapeaux d'ouverture lus dans la trace).
10. Le libellé de la délégation sur `test` reste, mot pour mot, « impossible par construction (référence égale à 1) ».
11. Le Markdown de chaque fichier `test_final` garde en tête « à ne pas afficher avant la fin du compteur de rondes de la
    boucle extérieure ».

## 4. Commandes pour session-depot (LISEZMOI, § 5)

Aux dossiers réels de la copie de lancement : course M `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-v1-tentative2` ;
course S `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1` (sans suffixe de tentative, R-497). Trois commandes,
écrites telles qu'il les lancera (`python3 -I -B`, chemins par variables nommées) : `test` de M ; `test` de S ;
`test_final` des deux, à la fin de la course S ; et la variante `--sans-seconde-course`. Chaque commande écrit dans un
dossier de sortie nouveau ; sa sortie standard n'est pas affichée (session-depot la redirige dans un fichier qu'il pousse
sans le lire).

## 5. Essais

Ceux de la v2, adaptés ; ceux du § 3 ; sous Python 3.11, 3.12 et 3.13 ; journal avec les heures lues sur `date -u`. Les
essais de la v2 qui portaient sur le mode provisoire sont retirés et listés comme tels.

## 6. Interdits (inchangés)

Aucun fichier de données de la banque, aucune archive ni pièce d'un pilote réel ouvert, lu ou haché ; aucun dossier
`donnees/`, `runs/`, `diag/`, `pilotes/` ; aucun `git`, réseau, sous-agent ni clé ; aucun score réel ; données synthétiques
seulement ; écrire seulement sous `/var/tmp/lecture-pilote4-v3/` ; heures lues sur `date -u` dans la commande qui les
écrit ; Python avec `-I`.

## 7. Fin

Réponse finale en quelques lignes : ce qui est fait, ce qui reste, écarts déclarés, empreintes des pièces.
