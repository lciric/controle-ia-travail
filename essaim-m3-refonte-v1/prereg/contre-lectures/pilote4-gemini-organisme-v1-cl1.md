# Contre-lecture 1 du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v1.md`) — v1

- **Texte relu** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v1.md`,
  `312c999353f8c103321b972b9cafa515d721a38945d6c594f14e072e1953f09e` (empreinte vérifiée sur disque avant lecture).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit, 25 octobre 2026, environ 18:15–18:50
  UTC (heure lue sur `date -u` ; l'horloge de la machine est en heure de Paris, UTC+1 ce jour-là). Je n'ai écrit ni ce
  texte, ni P3, ni T2, ni le lanceur, ni la batterie.
- **Lu** : le texte en entier ; P3 (`57c8535a…`) en entier ; T2 (`d2944654…`) l. 1–633 (dont plan, critères gelés, liste
  d'arrêt) ; le lanceur `lancer_pilote4_gemini_v3.sh` en entier, sa dérivation v3, sa configuration, les deux écarts, la
  batterie v4 (parties utiles) et le journal de la série v5 en entier, `simulation-lanceur-v3/` (manifeste et événements
  de l'extrait de simulation v5.3), `sceller_pilote4_v1.py`, `EMPREINTES-pieces-pilote4-v2.txt` ; le lanceur v2 de P3 ;
  `banque/LISEZMOI-v5.md` (parties citées), `LISEZMOI-v6.md` en entier, `reference-contraste-paires-banque-v3-v2.json`,
  la contre-lecture de la banque v3 (parties citées) ; la vérification de la v6.1 (parties citées) ; le code extrait de
  la v6.1 et de la v5.3 (lignes citées et voisines) ; la demande de v6.2 et la note N-046 ; le noyau (`boucle.py`,
  `cli.py`, `contrat.py`, `question.py`, `archive.py`, `extrait_mecanique.py` : lignes utiles).
- **Non lu** (consignes) : aucun fichier `…-cle.json` ni `…-secret.json`, aucun dossier `donnees/`, `runs/`, `diag/`,
  aucun `P3-consignes-v1.md` ni fichier `textes-actions-…`, aucun registre (`registres/` n'était pas dans ma liste).
- **Exécuté** : `sha256sum` sur les pièces ; une recopie autonome de `boucle.empreinte_arbre` (lecture de fichiers
  seulement, `outils/empreinte_arbre_v1.py`) sur les deux dossiers extraits ; le script de dérivation du lanceur, sur le
  lanceur v2 de P3, avec la configuration du texte, sortie sous mon dossier (`lanceur-rederive-v1.sh`). **Rien** du code
  des organismes, ni la batterie, ni le noyau, ni le script de scellement. Rien écrit hors de
  `/var/tmp/contre-lecture-pilote4-v1/`.

## Verdict

**Scellable après corrections.** Quatre constats majeurs : la ligne d'extension du GO, « de la forme exacte », nomme la
banque v2 au lieu de la v3 (P4C1-01) ; la borne de deux heures n'est plus tenue au pire cas, et le cas attendu n'a
presque aucune marge (P4C1-02) ; le devis ignore la dépense de la v5.3 au pilote 3, qui laisse prévoir le plafond de
60 USD atteint, donc la v6.1 arrêtée (P4C1-03) ; la condition (i) du moment de lecture, héritée de P3, est périmée depuis
R-443 (P4C1-04). Sept mineurs et quatre remarques suivent. Le lanceur fait ce que dit le texte et rien d'autre : je l'ai
redérivé à l'identique.

**Une seconde contre-lecture est nécessaire** après corrections. Quatre constats sont majeurs, et la règle que P3 s'est
donnée (P3, l. 47–49) arrête le pilote sur des corrections majeures que personne n'a relues. Elle peut être courte :
texte corrigé, écart au présent texte et, si le lanceur ou la batterie changent (P4C1-02 option c, P4C1-06), le nouveau
lanceur, sa dérivation et le journal de la nouvelle série.

## Constats

### P4C1-01 — majeur — La ligne d'extension du GO nomme la banque v2

- **Fait.** Plan, point 1 (l. 176), forme exacte : « … ; banque confrontation-v2
  52beb637823b72f475fd1ddcf446e9b79cafa5d2cd47d16c08b663d2b9388d10 ; … ». Or la course sert la v3
  (`157a2b45…`, l. 66 et 214 ; lanceur l. 130, 362 et 644). Le texte dit que le GO « porte … la banque v3 » (l. 52) et
  que « la v2 (52beb637…) n'est jamais servie » (l. 119). Le lanceur ne lit pas la banque sur la ligne de GO
  (l. 431–434 : `calcul`, `8b1c7511`, arbre de l'objet, 16 premiers caractères du texte). Une ligne recopiée telle quelle
  laisserait donc partir les deux courses, et la dépense consentie par Lazar serait liée à une banque jamais servie.
- **Correction.** Remplacer par « banque confrontation-v3
  157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d ». Demander à session-depot de vérifier la ligne
  poussée par les mêmes `grep` que le lanceur, plus l'empreinte de la banque, comme T2 le faisait pour la sienne
  (l. 287).

### P4C1-02 — majeur — Le temps : la borne de deux heures n'est plus tenue au pire cas, et le texte ne le dit pas

- **Fait 1, pire cas.** T2 garantissait que la commande ne serait pas coupée : « ≈ 180 s d'essais + 2 × (2 400 + 10 +
  900) s + ≈ 60 s ≈ 6 900 s, sous la borne » (T2 l. 236–244). Sa liste d'arrêt le reprend : « pire cas d'un appel du
  lanceur ≈ 6 900 s < 7 200 s » (l. 556). Le présent texte incorpore cette liste « ligne à ligne » par P3 et ne remplace
  pas cette ligne. Or il y a désormais jusqu'à 6 rondes (5 pour la v5.3, par son propre critère) et 4 générations. Chaque
  unité est bornée à 2 400 s (manifeste de simulation : `budget_conception.temps_max_s` 2400), plus l'attente des appels
  en vol, jusqu'à 900 s (T2 l. 239). Le pire cas vaut donc ≈ 180 + 10 × 3 310 + 60 ≈ 33 300 s (≈ 9 h). Sans aucune ronde,
  4 × 3 310 = 13 240 s dépassent déjà la borne.
- **Fait 2, cas attendu** (l. 151–157). Le texte compte 4 générations à 40–65 minutes (durées de M et de S, v5.2.1) et
  6 rondes à moins de 8 minutes, soit jusqu'à 113 minutes. Avec ≈ 3 minutes d'essais et l'archive, on arrive à
  ≈ 117–118 minutes : 2 à 3 minutes de marge au haut de la fourchette. Trois éléments manquent au calcul :
  - les durées réelles de g000 et g001 de la v5.3 au pilote 3. C'est le même objet, et sa course était finie avant la fin
    de l'écriture (le texte cite sa dépense, l. 53). C'est la mesure la plus proche.
  - le contenu d'une ronde (P4C1-08) : moisson avec appel de formulation, jusqu'à 6 recherches et 3 téléchargements, une
    induction, quatre vérifications. Le noyau compte au pire cas 25 s par recherche et 25 + 120 s par téléchargement
    (`temps_pire_cas`, `boucle.py` l. 56–67), soit 885 s de travail permis par ronde.
  - la génération qui porte la question (S : 965 s à g001).
- **Conséquences non écrites.** Une commande coupée perd la course après le manifeste, sans archive, avec jusqu'à 60 USD
  dépensés (T2 l. 556), et la v6.1 ne part pas. Le texte ne dit pas que faire des processus restés (R10 : par PID). Il ne
  dit pas non plus ce qu'il advient d'une ronde ou d'une génération lente sans coupure : à 2 400 s, statut
  `DELAI_DEPASSE`. Pour une génération de la v5.3, la liste close échoue (la v6.1 ne part pas) et le critère 1 déclenche
  l'audit (R4).
- **Correction** (a, b et e au minimum avant scellement) :
  - (a) écrire que la garantie de T2 ne tient plus, et remplacer sa ligne dans la liste d'arrêt ;
  - (b) refaire le cas attendu avec les durées réelles de la v5.3 au pilote 3 (fait mécanique, lisible ; chemin et
    empreinte), et dire la marge ;
  - (c) option sans coût : `--temps-max-conception 900`. La garde du noyau l'accepte (885 s ≤ 900 s) ; c'est une borne
    technique, pas une décision de Lazar ; elle ramène le pire cas d'une ronde de 3 310 à 1 810 s ;
  - (d) préenregistrer la conduite à tenir face à une course lente : la laisser courir et accepter la perte, ou poser
    `STOP` comme incident technique à une heure fixée d'avance. Dans le second cas, la course ferme son archive à la fin
    de la génération en cours, et la v6.1 ne part pas ;
  - (e) faire porter au mot direct de Lazar qui étend le GO l'acceptation explicite de ce risque. C'est un nœud de
    dépense : jusqu'à 60 USD peuvent être perdus sans archive.

### P4C1-03 — majeur — L'argent : le devis n'utilise pas la mesure la plus proche ; le plafond de 60 USD par course n'est pas discuté

- **Fait.** Le texte écrit « pilote 3 : 30,23 USD dépensés » (l. 53 et l. 176), sans chemin ni empreinte (R6). La v6 du
  pilote 3 est retirée. Si ce chiffre est la dépense de la seule course v5.3 du pilote 3 (deux générations, même objet),
  il fait ≈ 15 USD par génération, deux fois M (14,92 USD pour deux générations, P3 l. 255). Or ce sont les coûts de M et
  de S (6,67 à 8,63 USD par génération) qui fondent le devis (l. 159–160).
- **Conséquence.** À ce rythme, quatre générations font ≈ 60 USD, plus les rondes (≤ 3 USD chacune) : le plafond total est
  atteint à g003 ou avant. Le noyau rabat alors le budget de la génération à ce qui reste (`boucle.py` l. 625) et refuse
  des appels (`PLAFOND`). Les tâches refusées comptent comme des erreurs. Une génération à plus de 20 % d'appels hors
  `OK`, ou une g003 non servie, fait échouer la porte : la v6.1 ne part pas (l. 211 et 213).
- **Correction.**
  - Citer la dépense du pilote 3 avec sa source (ligne de `registres/depenses.md`, heure, empreinte), et ses coûts par
    génération s'ils ont été lus.
  - Refaire l'ordre de grandeur et dire la probabilité d'atteindre le plafond, avec ses conséquences.
  - Soumettre à Lazar, nœud de dépense : (a) garder 60 USD par course, en sachant que la v6.1 peut ne pas partir ; ou (b)
    relever le plafond par course et le GO d'autant.
  - Si 30,23 USD n'est pas la dépense de la seule v5.3, dire ce que c'est.

### P4C1-04 — majeur — Le moment de lecture : la condition (i), héritée de P3, est périmée depuis R-443

- **Fait.** P3 fixe la condition (i) ainsi : « le préenregistrement de l'étape 1 qui part scellé (à ce jour sa v9,
  R-418) » (P3 l. 297–298). Le présent texte ne change que la condition (ii) (l. 185–188). Or R-443 dit : « Aucune course
  décisive de l'étape 1 ni de la confrontation ne part sur la v1 ; les textes qui citent f1387a20… passent en version
  nouvelle » (l. 40–42). La note N-046 met l'étape 1 et la confrontation sur une banque dérivée de la v3, à une trace par
  paire (note, l. 36–38). Et le texte dit que la v3 sert ces traces « aux mêmes textes » (l. 216, BC4-02).
- **Risque.** Si (i) se lit « v9 scellée », elle est déjà remplie et ne protège plus rien. Les scores de ce pilote, par
  famille, sur des textes que la banque décisive reprend, après quatre générations de sondage du `test`, pourraient alors
  être lus avant que la version de l'étape 1 qui partira soit scellée.
- **Correction** (§ Plan, point 3). « (i) se lit : la version du préenregistrement de l'étape 1 qui part effectivement, sur
  la banque à une trace par paire, scellée (chemin et empreinte cités au rapport de lecture) ; la v9 ne la remplit pas. »
  Dire de même, pour la confrontation, la version qui servira la banque décisive.

### P4C1-05 — mineur — La déclaration « Ce qui a été lu avant ce texte » n'est ni exacte ni complète

- **(a)** « Aucun score du pilote 3 n'existe encore à cette heure » (l. 18). La v5.3 du pilote 3 part à 15:36:52 UTC
  (l. 13), l'écriture commence à 16:05 UTC, et la g000 de M a duré 751 s : un score de g000 existait très
  probablement. Le texte cite d'ailleurs un fait d'après la course (sa dépense) : à la fin de l'écriture, la course était
  finie et ses scores existaient dans son archive fermée. Pour R1, compte la lecture, pas l'existence.
- **(b)** Les faits mécaniques du pilote 3 lus (dépense ; peut-être le `LANCEMENT.md`, l'extrait, des durées) ne sont pas
  déclarés.
- **(c)** « … vient de trois sources, et d'aucun score » : la source (i), l'audit de symétrie, a été déclenchée par les
  scores de M et de S et les a lus. C'est légitime (R4), mais « d'aucun score » est inexact.
- **Correction.** Dater la déclaration au scellement. Lister ce qui a été lu du pilote 3 (mécanique seulement, chemins et
  empreintes), et dire que ses scores existent, fermés et non lus. Écrire, par exemple : « d'aucun score du pilote 3 ; la
  banque change sur un défaut d'instrument établi par l'audit de symétrie que les scores du second pilote ont déclenché ».

### P4C1-06 — mineur — La garde de la banque n'a pas d'artefact (R5)

- **Fait.** La ligne de la garde a changé : chemin `banque-confrontation-v3.json`, empreinte `157a2b45…` (lanceur l. 130 et
  362 ; dérivation, § 3). « Valent par identité des lignes » (l. 244–245) ne s'applique donc pas à elle. Le côté sain est
  montré : les cas sains partent. Mais ni la batterie v4 (valeurs de `ESSAI_ARTEFACT` : organisme, nombre, question,
  junit-…, imprevu, famille, commit, archive, appel-vieux) ni le journal v5 n'ont de cas qui refuse une banque autre que
  la v3. Le crochet existe pourtant (lanceur l. 133). `LISEZMOI-v6.md` (§ 1, BC2-02) exige que tout lanceur refuse toute
  autre banque.
- **Correction.** Ajouter le cas à la batterie : banque v1 ou v2 copiée au chemin de la v3 et committée, ou
  `ESSAI_ARTEFACT=banque`. Refaire la série (nouveau journal, R12) ou, au moins, jouer ce cas et le citer.

### P4C1-07 — mineur — Trois inexactitudes sur ce que font les objets

- **(a) La stagnation est unilatérale.** Le texte dit « à partir de g2 si les deux derniers scores rendus diffèrent de
  0,01 au plus » (l. 106–107). Le code teste `scores[-1] - scores[-2] <= 0.01` (v6.1 `principal.py` l. 929, condition
  l. 932) : toute baisse, quelle que soit sa taille, déclenche la mutation. Écrire : « si le dernier score ne dépasse pas
  l'avant-dernier de plus de 0,01, toute baisse comprise ». Le même test se trouve dans `mitose_spectrale.py` l. 75 et
  117.
- **(b) La mitose ne peut pas agir.** Le texte dit que le retour arrière et la mitose « peuvent agir » (l. 112–113). C'est
  vrai du retour arrière (deux générations notées, écart > 0,03 : v5.3 `memoire_isvd.py` l. 117–129). La mitose, elle,
  lit deux scores à partir de g2, mais son résultat ne peut pas changer. Pour les tâches, `nb_castes_cible =
  min(max(1, budget_par_tache), …)` vaut 1 avec un budget d'une caste par tâche (l. 77 ; P3 l. 239), quelle que soit la
  pression. Pour la question, posée seulement à g001, il n'y a qu'un score.
- **(c) La « correction de P3 » cite mal P3** (l. 109–111). La citation « que si `autoriser_mutation_code` est vrai »
  n'est pas dans P3. P3 écrit (l. 196–201) : « n'est tentée qu'en phase de conception (…), si `autoriser_mutation_code`
  est vrai (…), ou à partir de g1 en cas de « stagnation » ». C'est une énumération, qui peut se lire comme la même
  disjonction. Citer P3 exactement et le dire ambigu. J'ai vérifié la disjonction dans la v6.1 (l. 932), pas dans la v6
  (absente de ma liste).

### P4C1-08 — mineur — Ce qui tourne en conception n'est pas dit au-delà du critère d'arrêt

- **Fait.** En conception, la v5.3 fait :
  - une moisson avec appel de formulation (`principal.py` l. 1593–1606, `autoriser_appel_formulation=(phase ==
    "conception")`), le noyau servant 6 recherches et 3 téléchargements par ronde (manifeste de simulation,
    `budget_conception`) ;
  - une induction ;
  - quatre vérifications sur l'entraînement (l. 1644).

  Le score interne qui décide de la fin est la moyenne d'au plus quatre scores de ces vérifications (l. 1793–1797).
  En simulation, c001 = 1 formulation, 1 induction, 4 appels `calibrateur_interne`, plus 1 mutation pour la v6.1. De plus,
  la v5.3 inscrit dans sa mémoire la génération que le noyau lui sert, soit 0 en conception (`boucle.py` l. 617 ;
  `principal.py` l. 1507 et 1769 ; `memoire_isvd.py` l. 148, 188, 229, 238). Après g0, toutes ces entrées reçoivent donc
  le score de g0 (`memoire_isvd.py` l. 108–111) et peuvent être choisies comme « meilleur ancêtre » par le retour
  arrière. Pour la v6.1, la même boucle reste à vérifier.
- **À transposer et à dire.**
  - Par course, jusqu'à 6 × 6 + 4 × 6 = 60 recherches (≈ 10 sur la source web) et 30 téléchargements, contre « au plus 12
    recherches, dont 2 web » et « 4 recherches web au plus pour les deux courses (coût nul sur la parole de Lazar) » dans
    T2 (l. 225–226).
  - Les « expositions dites et acceptées » de T2 (documents moissonnés dans les consignes de tâche, l. 437–446) sont
    multipliées d'autant.
  - Le critère de fin repose sur quatre tâches au plus.
  - Le retour arrière peut restaurer un état de ronde.

  Tout cela est rapporté tel quel, sans lecture.

### P4C1-09 — mineur — Des transpositions silencieuses de P3 deviennent fausses ou incomplètes

- **(a) Ligne de mutation de P3.** P3 dit, pour un appel `architecte_mutation_endogene` : « à g1, aucun effet sur la course
  (son successeur ne tourne pas) » (P3 l. 341). Reprise « aux noms de ce pilote », la ligne devient fausse : g2 et g3 sont
  servies. La remplacer : « rapporté ; son successeur valide tourne à la ronde ou à la génération suivante ; invalide : en
  conception, l'organisme reste (contrat § 5, `contrat.py` l. 144–149) ; en génération, relance selon T2 ».
- **(b) Journal consulté pendant la course.** P3 donne le chemin `…/gNNN.noyau/journal-appels.jsonl` (P3 l. 307–308). Pour
  une ronde, c'est `…/cNNN.noyau/journal-appels.jsonl` (`archive.py` l. 76–78, `boucle.py` l. 596–599).
- **(c) Copie de lancement.** Le paragraphe de P3 (l. 154–160) n'est pas transposé : branche
  `outils/pilote4-gemini-travail`, `git fetch` de `canal/gemini-organisme-v6-1` (et de la v5.3, du canal, de `main`),
  commits de la banque v3 (`8856100`, `cfd030a`) atteignables, copie autre que celle du pilote 3.
- **(d) Rondes et porte « v5.3 précédente ».** La porte ne lit que les générations notées (lanceur l. 223,
  `not g.get("phase")`) : une ronde de la v5.3 hors `OK` n'arrête pas la v6.1. Le dire dans la liste d'arrêt, ou
  l'ajouter à la porte.

### P4C1-10 — mineur — Mots de Lazar, heures et défaut

- **Heures.** Le 25 octobre 2026, Paris est en UTC+1 (fin de l'heure d'été à 03:00). Les heures du texte sont cohérentes
  entre elles : 16:27 Paris = 15:27 UTC, avant le départ de la v5.3 du pilote 3 (15:36:52 UTC) ; 17:43 Paris = 16:43
  UTC (note N-046, l. 3) ; la vérification de la v6.1 a eu lieu de 15:25 à 15:45 UTC, et la série v5 du lanceur de
  18:04 à 18:13 UTC. La citation de 17:43 est exacte (N-046, l. 26–27).
- **(a)** « la course v6 de P3 est retirée (mot de Lazar, 16:27 Paris) » (l. 14). Les mots cités (« je veux mesurer la v6
  1 et v5 3 si pas chère ») ne retirent pas la v6, et la liste d'arrêt de P3 exige un « mot de Lazar qui retire … une
  course de ce pilote » (P3 l. 340). Citer ces mots ou leur inscription (`registres/decisions.md`, R-…).
- **(b)** « défaut de la décision soumise à Lazar à 17:48 Paris » avec échéance à 19:00 Paris (l. 94) : un défaut
  72 minutes après la soumission n'est pas le défaut à 48 heures de la hiérarchie de décision. Il est aussi en tension
  avec « il faut toutes les lever » (16:53). Citer les mots par lesquels Lazar a fixé cette échéance, ou dire que c'est
  son mot d'extension du GO, qui nomme `a9d8eb5`, qui tranche pour la v6.1 avec ses points ouverts.
- **(c)** Les 3 USD par ronde ne sont pas dans les mots cités (17:15, « go » sur « (b) 6 rondes au plus maintenant… »).
  Citer le texte de l'option, ou s'en remettre au mot d'extension, qui les porte.
- **(d)** L. 53 : « pour l'ensemble du GO … pour l'ensemble des courses du GO », doublon.

### P4C1-11 — mineur — La séparation d'avec les banques décisives : sa garde est hors de ce texte

- **Fait.** La dernière ligne de la liste d'arrêt (l. 216) confie la garde aux « lanceurs de l'étape 1 et de la
  confrontation », qui ne relèvent pas de ce texte. Le noyau, avec `--depuis`, garde déjà la banque de la course d'origine
  (`cli.py` l. 123). Les voies qui comptent sont donc `--organisme-impose`, avec un dossier tiré de l'archive de ce
  pilote, et l'import de rondes. « Contre-lecture de la banque v4, BC4-02 » est citée sans chemin ni empreinte (R6).
- **Rien n'est dit de Gemini.** L. 27 dit qu'aucun score de M, de S ni du premier pilote n'a été servi à Gemini ; rien ne
  dit qu'aucune pièce fermée de ce pilote (mémoire, archive, réponses aux tâches) ne sera servie à Gemini, concepteur des
  organismes, avant le moment de lecture. La demande de v6.2 le promet pour la v6.2 (§ 4).
- **Correction.** Écrire la séparation comme une condition à inscrire dans ces textes et dans leurs listes d'arrêt ; citer
  BC4-02 avec chemin et empreinte ; étendre la l. 27 au pilote 3 et à ce pilote.

### P4C1-12 — remarque — Référence « contraste de paire » : chiffres justes, deux limites à dire

Les chiffres sont justes (`reference-contraste-paires-banque-v3-v2.json`, `556d6398…`) : maximum 1,0 sur `test` et 0,75
sur `test_final` ; longueur 1,0 et 0,75 ; mots des lignes propres 1,0 et 0,75 ; le nombre de mots donne aussi 1,0 sur
`test`. Deux limites, dites par la contre-lecture de la banque v3 (BC2-01) :
- le maximum est pris sur les parts notées elles-mêmes : c'est une enveloppe haute choisie sur ces parts ;
- l'appariement est calculé part par part, alors que le noyau sert `test` et `test_final` mêlés.

Comme aucune différence n'est calculée, rien ne change à la lecture ; il suffit de le dire.

### P4C1-13 — remarque — Un canal nouveau dans les pièces lisibles

L'extrait porte l'événement de fin de conception (ronde, nombre d'exemplaires), mais pas le score interne : je l'ai
vérifié dans l'extrait de simulation, où `score_interne_bregman_tsallis` est absent de la déclaration. Le nombre de rondes
et la ronde de la déclaration disent pourtant quel seuil (0,65 ou 0,78) le score interne a franchi, sur au plus quatre
tâches d'entraînement. C'est un canal sur l'entraînement seul ; le dire et l'accepter.

### P4C1-14 — remarque — Pièces et scellement

- **(a) Script de scellement.** Sa chaîne de documentation dit encore « banque v2 ». Son empreinte (`eb054f0b…`) n'est pas
  citée au § Pièces ; elle entrera dans le fichier d'empreintes. Comme dans P3 (P3C2-03), il n'exige aucune contre-lecture
  présente. Il n'a été essayé ni sur un cas sain ni sur un artefact (copie du texte, marqueur restant).
- **(b) En-tête du lanceur v3.** Il se dit « — v1 » (l. 4) et son usage nomme `lancer_pilote4_gemini_v1.sh` (l. 22) ;
  le commentaire l. 93 (« 120 USD au plus ») date d'avant le GO à 155. C'est sans effet : `LANCEMENT.md` consigne
  `basename "$0"`.
- **(c) Textes à insérer.** Ceux qui rempliront les deux marqueurs de contre-lecture (l. 4 et 265) ne doivent contenir :
  - aucun marqueur entre doubles crochets ou doubles chevrons, que le script et le lanceur refusent ;
  - aucune ligne « entropie E = » suivie de chiffres avant la l. 179, car le lanceur prend la première occurrence
    (l. 399) ;
  - aucune ligne « graine de la course … = » suivie de chiffres.

  Ce rapport n'en contient pas.
- **(d) Lignes de P3 pour la v6.** Elles ne valent pas pour la v6.1 : l'exemple de format est à la l. 740 de la v6.1, et
  les dix mêmes requêtes de réserve sont aux l. 86–95.
- **(e) Marge du GO.** 155 − 30,23 − 120 ≈ 4,77 USD. La dire comme couvrant les tests de dépense et le frein « juste mais
  pas étanche » du noyau (T2 l. 310–314) ; un dépassement arrête tout (R-439).

### P4C1-15 — remarque (conforme) — Ce que j'ai trouvé conforme

- **Empreintes.** Toutes celles que cite le texte correspondent : texte, P3, T2, lanceur v3 `73d318b9…`, dérivation
  `e376d769…`, configuration `2f425291…`, écarts `67950a3b…` et `3326198e…`, lanceurs v1 et v2, batterie `8e82d9ca…`,
  journal v5 `a41ddd56…` et journaux v1 à v4, dérivation des essais `b320bb6b…`, `EMPREINTES-pieces-pilote4-v2.txt`
  `a0e6f3b5…` (69 lignes sur 69 vérifiées), lanceur de P3 `add695a9…`, banque v3, `EMPREINTES-banque-v3-v1`,
  contre-lecture de la v3, vérification de la v6.1 `f9b3646d…`, demande de v6.2 `3d4c74e3…`, note N-046 `7fa0f544…`.
- **Arbres des objets.** Recalculés : v6.1 `ae331d1d…`, 24 fichiers ; v5.3 `6251ab21…`, 22 fichiers.
- **Lanceur.** Redérivé du lanceur v2 de P3 par la dérivation v3 et la configuration du texte, il est identique octet à
  octet au lanceur v3 (30 remplacements, tous déclarés). Il passe au noyau `--generations 4 --rondes-conception-max 6
  --usd-max-conception 3 --plafond-total 60`, la banque v3 épinglée, la question à g001 (l. 630–635 et 644). Le manifeste
  de simulation le confirme : 6 rondes, 3 USD, 160 appels, 2 400 s par ronde, 4 générations, cible `g001`.
- **Gardes du lanceur.**
  - Porte « M de référence » inchangée ; porte « v5.3 précédente » à [0, 1, 2, 3] (l. 223–224).
  - Ligne de GO liée aux 16 premiers caractères du texte, exigés en réel (l. 393 et 430–434), avec cas sain et artefact
    (`go-sans-texte`).
  - Lignes de dépense conformes aux formes du texte (l. 436–442).
  - Graines recalculées, enfants 0 et 1 (l. 396–405).
  - Chemins permis (l. 140), avec cas sains et refus (`commit-banque-v4`, etc.).
  - Journaux g000 à g003 et c001 à c006 recopiés et poussés (l. 675–683 et 730).
- **Batterie.** 150 cas sur 150, dont les 21 artefacts de la v5.3 précédente.
- **Noyau.** Aucune tâche de `test` en conception (`boucle.py` l. 607). La question à `g001` n'est pas posée en `c001`
  (`question.py` l. 81–90). L'historique porte les rondes avec un score nul, que les organismes écartent (v6.1 l. 928 ;
  `memoire_isvd.py` l. 102–108).
- **Critères de fin de conception** (lignes exactes). v5.3 l. 1800–1804 : 0,65 dès la ronde 1, fin au plus tard à la
  ronde 5 sur 6. v6.1 l. 1986–1990 : 0,65 à partir de la ronde 2, fin à la ronde 6. Mutation tentée à chaque ronde en
  v6.1 (l. 932).
- **Banque, vérification, note.** Chiffres de la banque v3 justes (maxima 0,625 à 0,6667, seuils de 0,75 à 0,84, surface
  0,75 / 0,6944 / 0,5833 / 0,50, refus à tort 2,45 %) ; sondage du `test` par l'historique dit (BC1-10) ; faits de la
  vérification de la v6.1 justes (45 essais, graines 0, 1 et 2, V6-01 corrigé ; réserves 1, 3, 4 et 7 en partie, 5 et 9
  non levées) ; point 9 de la demande de v6.2 rapporté justement.
- **Lecture et devis.** Critère 1 étendu aux rondes, audit R4 par un sous-agent neuf, phrase du critère 3 ; aucune
  comparaison, aucune prédiction, aucun jugement anticipé dans le texte. Arithmétique du GO (30,23 + 120 + tests ≤ 155 ;
  reste ≥ 60 USD avant chaque course) juste.
