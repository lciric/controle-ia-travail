# Consigne du lecteur de l'issue du pilote MR-2 (procédure v14) — v4

Version 4, 2026-11-16T14:33:58Z (`date -u`, lue juste avant l'écriture et le scellement) : corrections du tour 1 de la contre-lecture de la v3 appliquées (section « Contre-lecture », en fin de pièce) ; la v3 (`f06f46b3…`), la v2 (`0e12acbd…`) et la v1 (`5189c442…`) restent intactes dans ce dossier.

Préparée par le compte organisme (modèle A), **auteur du texte scellé et du code : il ne lit pas l'issue**. À remettre telle quelle,
avec les seules pièces nommées ci-dessous, à **un sous-agent neuf** qui n'a écrit ni le texte scellé, ni le code, ni la conception v4
(texte scellé, « Plan d'analyse », point 3 ; R13). Le lecteur est choisi et lancé par la mère, après l'état `fini` de la machine et la
récupération de la branche de sortie (procédure v14, section 9). Le compte organisme n'ouvre aucune des pièces d'issue.

## Ce que le lecteur reçoit, et rien d'autre

1. **Le texte scellé** : `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`
   (branche `prep/pilote-mr2-compte-organisme-v1`), `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` ; il en
   applique les sections « Métrique », « Seuil », « Plan d'analyse », « Critères de lecture gelés », « Audit de symétrie (R4) » et
   « Liste d'arrêt », et rien d'autre.
2. **La copie de la branche de sortie** `calcul/pilote-mr2-v74-sortie-v14` faite par la session mère (`$OUTIL recuperer`), à son sommet
   final (`etape=fini` dans `etat.txt`) ; la mère ne remet aucune pièce de la copie qui n'est pas nommée ci-dessous ; elle remet :
   - `rapatrie-reel/lecture-pilote-v70.json` et son compagnon (sortie de `lire --ecrire` : l'issue, champ `regle`) ;
   - `remis-au-sous-agent/sortie-lire-non-ouverte.txt` (sortie de `lire`, jamais ouverte par la session qui lance) ;
   - `rapatrie-reel/sortie-mesure-pilote-v70.json`, `rapatrie-reel/mesure-pilote-v70.json` (pièce de liaison), le manifeste
     `rapatrie-reel/manifeste-pilote-v70.json`, le relevé `rapatrie-reel/releve-pilote-v70.json`, `rapatrie-reel/CARTES.json`, avec
     leurs compagnons ; `journal-10-mesurer.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `journal-09-reel.txt` (ou `…-reel-2`),
     `engagement-mondes.json`, `etat.txt`, `lancements.jsonl`, `code-06-generer.txt`, `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-11-rapatrier.txt`, `secret-sha256.txt`, `phrase-sha256.txt`, `rapatrie-reel/liste-rapatriement-pilote-v70.json`, `rapatrie-reel/journal-relais-fable52.jsonl`, `…-opus55.jsonl`, `…-argon.jsonl`, `…-astra.jsonl` (point 4 du plan), et les dossiers `rapatrie-reel/monde-N/PROPOSEUR/` (réponses brutes, corps des relais, témoins d'isolement : lus pour leurs empreintes, leur présence et l'audit du point 7, jamais recopiés). Les journaux, les `code-*.txt` et `etat.txt` sont à la racine de la copie. `rapatrie-blanc/` (essai à blanc, proposeurs factices) ne sert pas à l'issue et n'est jamais confondu avec `rapatrie-reel/`.
3. **Le registre des inscriptions** sur `main` (`registres/pilote-mr2-v74-v14-inscriptions-v1.md`, au commit le plus récent) : empreintes
   du secret, de la phrase, des mondes `H` et `S1` à `S4`.
4. **La dépense**, calculée par le compte organisme avec `depense_pilote_v14_v1.py` (empreinte `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, dossier `…/lecture-depense-pilote-v14-compte-organisme/` de la branche `lot/compte-organisme-v1`, copié par la mère avec la copie de sortie) : le programme ne lit que `releve-pilote-v70.json` et `journal-relais-*.jsonl`. Le lecteur reçoit sa **sortie JSON scellée** (nom donné par la mère) et les arguments `--machine` (prix horaire, heures de création et de destruction) et `--autre` tels que la mère les a donnés ; il les rapporte sans pouvoir les vérifier. Il vérifie l'empreinte du programme et recoupe lui-même, par lecture, les sommes du relevé et des journaux. Les prix de la configuration ne sont pas remis (le programme ne les lit pas) ; il ne recalcule aucun coût.

Les mondes, le secret et la phrase ne sont pas sur la branche et ne lui sont jamais donnés.

## Ce qu'il fait (plan d'analyse du texte scellé, dans l'ordre)

0. **Arrêts (« Liste d'arrêt »), avant toute ouverture de `lecture-pilote-v70.json` et de `remis-au-sous-agent/sortie-lire-non-ouverte.txt`**
   (ces deux pièces s'ouvrent en dernier, après les points 0 et 1 ; avant cela, `sortie-mesure-pilote-v70.json` ne s'ouvre que pour `hors_corps` et `corps.mondes_sha256`, jamais pour `corps.regle`, `corps.principale` ni `corps.audit_R4`, ni le relevé ni le manifeste pour autre chose que leurs champs de contrôle ; une issue aperçue avant la fin des points 0 et 1 est écrite au rapport). Il lit à la racine de la copie : `etat.txt` (`etape=fini`, aucun
   `arret (A)`, `noeud, machine gardee` ni `sortie inattendue` ; le champ `exclus_balayage=` ne nomme aucune pièce remise ici) ; `code-06-generer.txt`,
   `code-07-preparer.txt`, `code-08-blanc.txt`, `code-09-reel.txt`, `code-10-mesurer.txt`, `code-10-lire.txt`, `code-11-rapatrier.txt` : tous
   à 0 (un code 3 vaut arrêt) ; `lancements.jsonl` : une seule ligne ; `rapatrie-reel/liste-rapatriement-pilote-v70.json` : `"aucun_monde": true`
   et pas de `CARTES-partiel.json` ; relevé et manifeste complets (`partiel` faux et `arret` vide, `null`, dans chacun ; `appels_complets_illisibles` à 0 dans le relevé) ; les 16 appels ont une réponse brute et un témoin
   d'isolement scellés ; dans la dépense remise (point 4 des pièces) : aucun appel au-dessus de son pire cas (`journal_au_dessus_du_pire_cas` à 0 pour chaque proposeur) et aucune part atteinte (le coût du relevé et celui des journaux de chaque proposeur strictement inférieurs à sa part, même si `sous_la_part` est vrai ; la machine, de même, strictement sous 3 USD). Tout
   écart (empreinte, code, état, compte, part) : arrêt, rapport, **aucune issue lue, pas même P-0** (texte scellé, « Liste d'arrêt ») ; un contrôle qu'il
   ne peut faire (pièce absente ou illisible) est aussi un arrêt aux points 0 à 2, écrit « non fait » avec sa cause, jamais sauté en silence (R5) ; au point 7 seul, il est écrit « non fait » sans arrêt.

1. **Empreintes** : chaque pièce qui a un compagnon égale à son compagnon (les journaux, `etat.txt`, `lancements.jsonl` et `remis-au-sous-agent/` n'en ont pas) ; le texte scellé lu égal à `8aa33014…` ; `secret-sha256.txt`, `phrase-sha256.txt` et `engagement-mondes.json` égaux aux empreintes du secret, de la phrase (empreinte du fichier de la phrase, retour à la ligne final compris : procédure v14, section 5, point 5), de `H` et de `S1` à `S4` du registre (la valeur hexadécimale est celle que porte le fichier, après son nom de champ éventuel) ; `fichier_mondes_sha256` du manifeste égal à `H` inscrit, et les quatre
   empreintes de mondes égales à `S1` à `S4` (la liste `corps.mondes_sha256` de la sortie de mesure est triée : comparer comme ensemble) ; `programme_sha256` de `mesure-pilote-v70.json` et `hors_corps.script_sha256` de la sortie de mesure égaux à `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365` ;
   `cartes_sha256` de la pièce de liaison égal à l'empreinte de `CARTES.json` ; liste `hors_corps.modules_importes` de la sortie de mesure comparée au bloc
   gelé du texte (S-c). Tout écart : arrêt, rapport, aucune issue lue.
2. **Mesure** : faite une seule fois sur la machine (code 0 attendu : `code-10-mesurer.txt`, `journal-10-mesurer.txt`) ; il ne la refait pas ; code non nul, exception ou refus nommé : arrêt (« Liste d'arrêt », erreur du programme de la mesure), aucune issue lue.
3. **Issue** : lue au champ `regle` de `lecture-pilote-v70.json` (`regle.issue` vaut `P-0`, `P-1` ou `P-2` ; « P-2 avec réserve » est `P-2` dont `regle.noeuds_avant_banc` n'est pas vide, chaque nœud nommé ; « P-2 » sans réserve a cette liste vide) ; il **applique la table « Critères de lecture gelés »** (la première ligne
   qui s'applique : P-0, P-1, P-2 avec réserve, P-2), en vérifiant que le champ `regle` et les comptes de la sortie mènent bien à cette
   ligne ; il rapporte l'issue, les nœuds qu'elle appelle et « ce qui suit », mot pour mot.
4. **Coûts** : rapprochement par fournisseur (`depense_usd` et coûts des appels du relevé, somme des `cout_usd` des journaux des relais, parts de 12, 8, 9,36 et 9,36 USD ; π1 contre 20 USD, π2 contre 21,72 USD ; une part dépassée est déjà un arrêt du point 0 ; le code de sortie 3 du programme n'est pas dans sa sortie JSON : la mère le donne, sinon il se déduit de `sous_la_part` (chaque proposeur et `machine`), `pi1_sous_la_ligne` et `pi2_sous_la_ligne`, qui doivent tous être vrais ; la machine contre 3 USD, comprise dans les 21,72 USD de π2) ; écarts rapportés ; la console fait
   foi pour les montants facturés (R-2803).
5. Aucune autre exclusion que celles de « Métrique » ; aucune analyse en sous-groupe ne décide.
6. Le rapport dit : « P_VUE = 0,25 supposée, non mesurée » ; « p_c ne vaut que pour ce gabarit » ; tous les taux d'erreur du texte (section « Prédiction chiffrée et signe attendu », dont : course refusée à tort 0,20 si p vaut 0,02 ; permise à tort 0,26 si p vaut 0,051 ; à 12 et 14 appels répondus, refusée à tort 0,22 et 0,21, permise à tort 0,29 et 0,27) et, si l'issue est P-2, la phrase « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les conditionnelles ».
7. **Audit de symétrie (R4)**, tel que le texte le gèle : il lit `corps.audit_R4` de la sortie de la mesure. « déclenché : x = 0 » : il relit toutes
   les cartes refusées au gardien, au-delà de six ou non évaluables, et 3 cartes par appel tirées au hasard (graine : `SeedSequence` de
   l'entier g des 16 premiers octets, lus gros-boutiste, de l'empreinte sha256 (32 octets) du fichier `CARTES.json` tel que remis ; générateur `numpy.random.default_rng(numpy.random.SeedSequence(g))`, un seul pour tout l'audit ; appels pris par monde croissant puis par nom de proposeur dans l'ordre alphabétique ; pour un appel de k cartes (toutes celles que `CARTES.json` lui attribue, refusées comprises, dans l'ordre où il les liste), tirage `rng.choice(k, size=3, replace=False)` (indices comptés à partir de 0 dans cet ordre) ; toutes les cartes si k ≤ 3, sans tirage (le générateur n'avance pas) ; sans `numpy` (version 1.25 au moins), le tirage est écrit « non fait », avec sa cause ; la version de `numpy` employée et, pour chaque appel, les indices tirés sont écrits au rapport, pour que la mère puisse rejouer le tirage),
   vérifie que les épisodes servis contiennent les traits et que les témoins disent le gabarit servi. « déclenché : x ≥ 3 » : il relit les cartes
   qui portent, vérifie qu'aucune pièce servie ne décrit la famille ou une condition et l'isolement (témoins), relit aussi les cartes refusées et
   non évaluables. « non déclenché », ou champ absent (issue P-0 : la sortie s'arrête avant de le calculer) : aucun audit. L'audit ne change pas l'issue, il la commente (réserve écrite) ; un contrôle qui exige une
   pièce non remise est écrit « non fait ».

## Ce qu'il rend

Un verdict écrit, **scellé** (`python -m controle_ia.scellement sceller`), en français, sans identifiant de modèle Claude ni identifiant
servi (« modèle A », « modèle B » si besoin ; R-2731), sur une branche de travail désignée par la mère, dans un fichier neuf au nom donné par elle (R12), rien d'autre n'étant écrit : issue (P-0, P-1, P-2 avec
réserve, P-2), ligne appliquée, comptes, empreintes vérifiées, écarts, dépense rapprochée, contrôles d'arrêt, audit R4 (déclenché ou non, fait ou non fait), les phrases du point 6, nœuds de Lazar appelés. Le verdict est soumis à Lazar par la
mère (R13). Le lecteur ne lance ni la mesure, ni le pilote, ni aucun programme qui écrit hors de son fichier de verdict (il lit et additionne les pièces remises), ne dépense rien, n'ouvre aucun chemin interdit (hors des pièces nommées ci-dessus : ni `prive/`, ni les mondes, ni la branche d'entrée `calcul/pilote-mr2-v74-entree-v14`, ni aucune clé ni variable d'environnement), ne recopie aucune réponse
brute.

## Contre-lecture

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-tour1-v1.md` (même dossier), empreinte
  `14725e82ff9e8d6a7dc0f11457dcb6131c45a69d69d2085965c3fad430e2c8ea` ; verdict « corrections » (cinq majeures, sept mineures).
- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la v1, ni le texte scellé, ni le code, par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v2.py` (même dossier) : empreinte de la v1 vérifiée, chaque « ancien »
  présent une seule fois, cible jamais écrasée. Noms des pièces citées vérifiés présents dans la copie de sortie (noms et tailles
  seulement, aucune pièce ouverte : 16 réponses brutes, 16 témoins d'isolement, quatre dossiers `monde-N`, aucun `CARTES-partiel.json`).
- **Réponse point par point** :
  - C1 (arrêts, nouveau point 0) : appliquée mot pour mot.
  - C2 (P-2 contre P-2 avec réserve) : appliquée mot pour mot ; `regle.issue` et `regle.noeuds_avant_banc` relus sur
    `mesure_pilote_v4.py` (`676d5f37…`).
  - C3 (pièces manquantes) : appliquée mot pour mot ; la note du rapport « à adapter si un de ces noms change » est hors du nouveau
    texte et n'est pas recopiée ; tous les noms existent aujourd'hui.
  - C4 (audit de symétrie) : appliquée mot pour mot. **Levé au tour 2** : la formule de la graine, proposée au tour 1, est confirmée et complétée par le rédacteur des corrections
    (modèle A) : ordre des appels, ordre des cartes, générateur (voir le point 7) ; le texte scellé dit seulement « graine dérivée de
    l'empreinte de `CARTES.json` ».
  - C5 (dépense, deux couples) : appliquée mot pour mot ; parts et lignes (12, 8, 9,36, 9,36 ; 20 ; 21,72 USD) relues égales à celles du
    programme `9866e611…`.
  - C6, C8 : appliquées mot pour mot ; `hors_corps.script_sha256`, `hors_corps.modules_importes` et le tri de `mondes_sha256` relus sur
    `mesure_pilote_v4.py`.
  - C7 (compagnons, texte, secret, phrase) : appliquée mot pour mot. **Levé au tour 2** : la parenthèse sur la nature de `phrase-sha256.txt` s'adressait à l'auteur, non au lecteur ;
    elle est retirée. La procédure v14 (section 5, point 5) dit que la machine pousse `phrase-sha256.txt` après avoir vérifié l'empreinte du
    fichier déchiffré égale à celle du feu, qui est celle que le registre inscrit (« empreinte du fichier de la phrase (retour à la ligne
    final compris) ») ; le contre-lecteur du tour 2 l'a vérifié et le rédacteur des corrections (modèle A) a retiré la parenthèse.
  - C9 : supprimée par le contre-lecteur, intégrée à C3 ; sans objet.
  - C10, C11, C13 : appliquées mot pour mot.
  - C12 (taux d'erreur) : appliquée **avec une correction de chiffres**. Le nouveau proposé disait « mêmes taux à 12 et 14 appels
    répondus » ; le texte scellé (« Prédiction chiffrée et signe attendu ») donne d'autres taux à 12 et 14 appels répondus : refus à
    0,02 de 0,22 et 0,21, acceptation à 0,051 de 0,29 et 0,27. Ces chiffres remplacent « mêmes taux » ; le reste du couple est mot pour
    mot.
  - Remarques facultatives R1 à R4 : non appliquées (non exigées), laissées à l'auteur ; R1 (« brief, section 6 », document que le
    lecteur ne reçoit pas) mérite d'être tranchée avant la remise.

### Tour 2

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-tour2-v1.md` (même dossier), empreinte
  `8c020f418de840403f666c501bdf05e07e1e57cef0b0735421bef89675fe5293` (égale à son compagnon) ; verdict « corrections » (deux
  majeures, sept mineures) ; pièce lue : la v2, `0e12acbd6ea72bf2318c809d13be20382b6e6864041ce0e20a56365425c8e30b`.
- **Application** : par un rédacteur neuf (modèle A), par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v3.py` (même dossier) : empreintes de la v2 et du rapport vérifiées,
  chaque « ancien » présent une seule fois, cible jamais écrasée. Noms des pièces citées revérifiés présents dans la copie de sortie
  (noms et tailles seulement, aucune pièce de la copie ouverte). Noms de champs (`exclus_balayage=` de `etat.txt` ; `partiel`, `arret`,
  `appels_complets_illisibles` du relevé ; `partiel`, `arret` du manifeste ; `corps` et `hors_corps` de la sortie de mesure ;
  `appels` et `cartes` de `CARTES.json`) relus sur la procédure v14 et sur les pièces de la répétition locale versées au commit
  `2d35cafa` (`…/procedure-pilote-v74-compte-organisme/repetition-locale/rapatrie/`), non sur les pièces réelles.
- **Réponse point par point** :
  - M1 (a) (nature de `phrase-sha256.txt`) : appliquée mot pour mot ; procédure v14, section 5, points 4 et 5, et ligne du registre
    (« empreinte du fichier de la phrase (retour à la ligne final compris) ») relues : même nature.
  - M1 (b) (graine) : appliquée, **avec trois précisions** pour qu'aucun choix ne reste au lecteur : un seul générateur pour tout
    l'audit ; indices comptés à partir de 0 dans l'ordre de `CARTES.json` ; aucun tirage, le générateur n'avançant pas, pour un appel à
    au plus 3 cartes (zéro compris). La phrase du rapport « sans `numpy`, le tirage est « non fait » » est portée dans le texte
    (avec la version 1.25 au moins, R9). Le texte scellé ne définit que « graine dérivée de l'empreinte de `CARTES.json` » : c'est une
    précision, non un écart.
  - M1 (c) (deux « points ouverts ») : appliquée ; une adaptation : « l'auteur (modèle A) » du couple devient « le rédacteur des
    corrections (modèle A) », parce que ce rédacteur n'est pas le compte organisme ; même adaptation au troisième couple (« l'auteur a
    retiré la parenthèse » devient « le rédacteur des corrections (modèle A) a retiré la parenthèse »). La puce « Application » du
    tour 1 (« modèle C ») est gardée telle quelle : sa rectification est un point pour la mère du rapport, non une correction exigée.
  - M1 (d) (puce du tour 2) : cette sous-section.
  - M2 (sortie de mesure avant la fin des points 0 et 1) : appliquée mot pour mot.
  - m1 (contradiction du point 0) : appliquée mot pour mot (deux couples).
  - m2 (« seules pièces nommées ») : appliquée mot pour mot.
  - m3 (noms de champs, chemins `corps.`) : appliquée, quatre couples ; au deuxième, « `arret` nul » et « `appels_complets_illisibles`
    nul » sont écrits selon le type du champ (« `arret` vide, `null` » ; « `appels_complets_illisibles` à 0 »), le reste mot pour mot.
  - m4 (code 3, part de la machine) : appliquée mot pour mot ; relue sur `depense_pilote_v14_v1.py` (`9866e611…`) : code 3 si l'un
    de `sous_la_part` (chaque proposeur, `machine`), `pi1_sous_la_ligne`, `pi2_sous_la_ligne` est faux ; `MACHINE = 3.0`.
  - m5 (`audit_R4` absent si P-0) : appliquée mot pour mot.
  - m6 (« trois phrases ») : appliquée mot pour mot.
  - m7 (« brief, section 6 ») : appliquée mot pour mot ; elle tranche la remarque facultative R1 du tour 1.
  - Remarques facultatives F1 à F5 : non appliquées (non exigées).

### Tour 1 de la v3

- **Rapport** : `contre-lecture-consigne-lecteur-issue-pilote-v14-v3-tour1-v1.md` (même dossier), empreinte
  `27269e9275f2fb094c5e4b4f88e182974d96a1bb49f3485426af94797253af4c` (égale à son compagnon) ; verdict « corrections » (aucune
  majeure, trois mineures) ; pièce lue : la v3, `f06f46b31944f88b62ea2de08b8b95d06ce92fd906b52e2856c10479942034c8`.
- **Application** : par un rédacteur neuf (modèle C), qui n'a écrit ni la consigne, ni le texte scellé, ni le code, par le programme
  `appliquer-corrections-consigne-lecteur-issue-pilote-v14-v4.py` (même dossier) : empreintes de la v3 et du rapport vérifiées,
  chaque « ancien » présent une seule fois, cible jamais écrasée. `diff` v2 → v3 relu : les corrections du tour 2 y sont appliquées
  fidèlement, avec les adaptations déclarées. Noms des pièces citées revérifiés présents dans la copie de sortie (noms et tailles
  seulement, aucune pièce de la copie ouverte). Champs `journal_au_dessus_du_pire_cas`, `sous_la_part` (comparaison `≤` à la part)
  et `MACHINE = 3.0` relus sur `depense_pilote_v14_v1.py` (`9866e611…`) ; « Dépense d'un fournisseur atteignant sa part → arrêt »
  et la version de `numpy` du bloc gelé relues dans le texte scellé (`8aa33014…`).
- **Réponse point par point** :
  - m1 (point 6, liste de taux non exhaustive) : appliquée mot pour mot.
  - m2 (point 0, champs du pire cas et part atteinte au sens strict) : appliquée mot pour mot.
  - m3 (point 7, version de `numpy` et indices tirés écrits au rapport) : appliquée mot pour mot.
  - Remarques facultatives F1 à F3 : non appliquées (non exigées) ; F3 (mention « modèle C » de la puce « Application » du tour 1)
    est laissée telle quelle, comme au tour 2 : elle relève des points pour la mère.
