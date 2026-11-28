# Contre-lecture R2 du brouillon 7 du papier C — lentille « texte » (contre-lecture 9) — v1

- **Qui** : relecteur neuf (R2), sous-agent de la session 16. Je n'ai écrit ni les brouillons 1 à 7, ni leur
  configuration, ni aucune contre-lecture, note, projet de traitement ou traitement du papier C.
- **Heures** : le 2026-10-21, de 02:38 à 02:53 UTC environ (`date -u`).
- **Consigne** : `…/consigne-contre-lectures-brouillon7-v1.md`
  (`364aef04617b1684d246eb60902507c802c278ee0b6c2b7972683fa1331f81e4`, égale à son compagnon) : partie commune et
  lentille « texte » seulement. La lentille « méthode » (contre-lectures 8 et 10) est confiée à un autre relecteur.
- **Préfixe** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail`, lu en lecture seule.

## Pièces (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | empreinte | lecture |
|---|---|---|
| brouillon 7, `…/brouillon7/papier-C-preenregistrement-HC1-HC3-v1-brouillon7.md` | `541f1511583bd9ace20e91c0dc0551afa9e8bf6ee4a3e5ff2989a7966dd2e6f5` | en entier (1 569 lignes) |
| configuration brouillon 4, `…/brouillon7/papier-C-config-v1-brouillon4.json` | `6734fbd0a608e9bd2c7624286cfd2654ca524c5262e0854619705c72b70ebc3a` | par chemins, longueurs et empreintes ; champs de règles changés seulement, chaque caractère qui recoupe sur 12 caractères un texte de formulation, de témoin, de consigne, de fente, d'insertion, de contenu neutre, de paragraphe de bras ou du gabarit du constat nu remplacé par « ▒ » ; vivier par comptes |
| table `…/brouillon7/table-traitement-brouillon7-v1.md` | `351ab375ef75a55a34043351a56ffc162253844b068685a06c70eda4b1c34a1d` | en entier |
| sortie `…/brouillon7/problemes-brouillon7-v1.txt` | `6bf526b2d514e7ff15a7026859c4ce390244bdf249470c5f16be3b3b261ac67b` | en entier, rejouée |
| outils `…/brouillon7/travail/` (cinq fichiers, leurs journaux, `essais/essai1.md`) | compagnons conformes (`sha256sum -c`) | journal de construction et `enonces_b6_b7_v1.py` lus ; autres : empreintes |
| rapports appliqués : texte `…/contre-lectures-brouillon6/texte/contre-lecture-R2-brouillon6-texte-v1.md` ; vérification courte de méthode `…/contre-lectures-brouillon6/methode-courte/contre-lecture-R2-brouillon6-methode-courte-v1.md` | `68fc0dc9f6f0f5305587cc09d1a2762e5cfbf90c8701d2a19cdddea66599b3a9` ; `45a0d87569d883c72af7720081278e67298c3a2f9daaecf03c197b909431fd46` | en entier |
| consigne du rédacteur `…/consigne-redacteur-brouillon7-v1.md` | `e8bfb03bab6b81b882b9cd85f7dcdde3ed209af420159a14fd21596d2d22b48e` | en entier |
| base de comparaison : brouillon 6 (`fadc74c3…`) et configuration brouillon 3 (`85173b22…`) sous `…/brouillon6/` ; `R/brouillons/` : brouillon 3 du texte (`3cc25dcd…`) et configuration brouillon 2 (`77252564…`) | égales aux empreintes citées | comparaison mécanique |
| empreintes citées par le brouillon 7 et revérifiées sur disque : script et journal de la configuration brouillon 4 (`1b3dc311…`, `e0b058b0…`), manifeste des essais « texte » du brouillon 6 (`da5bbad0…`), `personne_grammaticale_vivier_v2.py` et sa sortie (`49f96efb…`, `9a2a3654…`), manifeste des simulations courtes (`368f3ec8…`), sorties U1 (quatre), U2 (deux), U3 citées | toutes égales | — |
| `R/registres/decisions.md` (`f5a6693d…`, lu à 02:40 UTC) : lignes P-020, P-021, P-022, R-312, R-316 ; `R/src/controle_ia/prereg.py` (`3b2e3ee5…`) | — | lignes citées ; validateur en entier |

Le projet de traitement du brouillon 5 (section 6.3) et `R/docs/decisions/` n'étaient pas nécessaires à cette lentille
(empreinte du projet vérifiée seulement). Projet : `c65aa83a…`, conforme.

## Ce que j'ai tenu ; écarts

- Écriture seulement sous `…/contre-lectures-brouillon7/texte/` : ce rapport, son sceau, et `essais/` (manifeste
  `essais/sha256sums-essais-texte-b7-v1.txt`, `ca05995cde1c7341317f5a3023c1d86924faba72d9f17e3c4db73e30620d6c48`).
- Aucun réseau, aucune commande git, aucun sous-agent, aucune dépense, aucune clé affichée ; `python3 -B -I` avec
  `PYTHONDONTWRITEBYTECODE=1` (Python 3.13.16 ; aucun `__pycache__` créé). Aucune recherche récursive : dossiers nommés
  listés un à un (`ls`), `grep` sur des fichiers nommés.
- Non lus, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`.
- Configuration : aucun texte de formulation, de témoin, de fente, de consigne ni de paragraphe de bras affiché ni
  recopié. Écart déclaré : un premier filtre (`voir_regles_b4_v1.py`) masquait des champs entiers et comptait des champs
  de règles du constat nu comme sensibles ; remplacé par `voir_regles_b4_v2.py` (masque caractère par caractère). Les
  caractères masqués (au plus 24 par champ) tombent dans des tournures courantes ; aucune conclusion n'en dépend.
- La comparaison ligne à ligne du brouillon 6 au brouillon 7 a été lue à l'écran (52 blocs changés, autant que les 52
  remplacements du journal), sans être écrite dans `essais/`. `versions_retenues_b7_v1.sortie.txt` contient des extraits
  du brouillon 7 (dont la forme à fentes du constat nu, déjà citée par la réserve 16) : à garder dans la zone privée,
  comme le brouillon.

## Verdict

**Scellable après corrections.**

Le brouillon 7 applique tous les constats des deux contre-lectures du brouillon 6 en mots exacts (31 segments retrouvés
chacun une fois, dix anciens textes absents) ; les écarts E-01 à E-12 sont exacts et suffisent à expliquer chaque
différence. Les quatre décisions de la session sont écrites (réserve 17 mot pour mot ; constat nu lu au pilote au point
1.4, sous le marqueur de P-022 ; page de l'éditeur ; voisins nommés, Jiang et al. et Wang K. et al. compris). P-020,
P-021 et P-022 ne sont pas tranchées (2, 6 et 9 en-têtes ; configuration « en attente » dans les trois champs). Énoncés
de HC1 à HC3 et « Pièces revendiquées » égaux au brouillon 3 (et 6). Configuration : vivier (5 familles × 16), seize
témoins, règle des témoins, fentes, insertion, consignes, contenus neutres, gardes, graines, juges, contrôle de rédaction
égaux à la configuration brouillon 3 (vivier, témoins, fentes, consignes égaux aussi au brouillon 2) ; seuls changent
`version`, `statut`, `stabilite_rang` et deux champs de `constat_nu`, plus une clé ajoutée sous `etape2.loi_nette`.
Sortie de `problemes` rejouée : identique octet pour octet à celle versée.

Un constat majeur bloque : les versions de repli (B) et (C) de P-021, produites par script selon le verrou 1 tel qu'il
est écrit, ne sont pas complètes (CB7-texte-01). Les autres constats sont mineurs : amorces « Version recommandée » et
renvois au verrou 1 qui ne survivent pas au scellement, passages hors des blocs qui dépendent d'une option retirée,
description périmée de la contre-lecture 9.

## Textes produits option par option

Script `essais/versions_retenues_b7_v1.py` (sortie `versions_retenues_b7_v1.sortie.txt`) : sept sites (point 5, point
1.4, bloc P-021 de la « Prédiction », bloc P-020, TC.1, réserve 9, bloc P-021 des « Critères »), dix-sept en-têtes ;
pour chaque option de chaque décision (les deux autres à leur défaut), en-têtes entre crochets et marqueurs retirés,
versions écartées retirées, exception de P-021 appliquée telle qu'écrite ; puis recherche de « en attente », « de
repli », « Version recommandée », « verrou 1 », marqueurs, « établie », passages du constat nu et du bras d'usurpation.

| décision, option | reste au texte |
|---|---|
| P-022 (b) | propre ; seule l'amorce « Version recommandée (…) » reste (point 5, TC.1 ; CB7-texte-02) |
| P-022 (a), (c) | blocs propres (CB6-texte-02 tient) ; hors des blocs, « Confidentialité » et la liste d'arrêt 11 citent une insertion que le texte ne lit plus (CB7-texte-03) |
| P-020 (a) | propre, amorce « Version recommandée (…) » à part |
| P-020 refusée | propre ; les phrases conditionnelles hors du bloc (« si P-020 est refusée ») se lisent sous les deux options |
| P-021 (A) | propre, amorces « Version recommandée (…) » à part ; « Clause de repli mécanique » est un nom, pas un reste |
| P-021 (B) | ligne C-P3b des deux tableaux « remplacée par la version (B) » sans mots écrits ; renvois « tableau de la version recommandée, gardé (verrou 1) » vers un nom qui ne reste pas (CB7-texte-01) |
| P-021 (C) | valeurs p par rééchantillonnage centré non définies ; « établie » gardé dans « Trois lectures » et « Sans le bras … » ; mêmes renvois (CB7-texte-01) ; la contre-lecture 8 renvoie à une clause retirée (CB7-texte-03) |

Les corrections proposées ci-dessous ont été appliquées en mémoire (`essais/corrections_essai_b7_v1.py` : 17
remplacements, chacun trouvé une seule fois, espaces et sauts de ligne indifférents) puis l'exception corrigée rejouée :
sous (A), (B) et (C), aucun reste « en attente », « de repli » (hors du nom de la clause), « version recommandée »,
« verrou », marqueur ni en-tête ; « ci-dessus » renvoie chaque fois au tableau gardé juste au-dessus.

## Constats

Corrections en mots exacts ; les anciens textes sont cités espaces et sauts de ligne normalisés (le texte les coupe en
fin de ligne).

### CB7-texte-01 — majeur — P-021 : les versions (B) et (C) ne sont pas complètes

- **Où** : verrou 1, exception P-021 (l. 140-144) ; bloc P-021 de la « Prédiction » (tableau l. 624-628, « Trois
  lectures » l. 630-637, « Sans le bras … » l. 648-650, (B) l. 652-655, (C) l. 657-661) ; bloc P-021 des « Critères de
  lecture gelés » (l. 1377-1394).
- **Ce qui est.**
  1. Sous (B), « leur ligne C-P3b étant remplacée par la version (B) » : aucun mot n'est écrit pour cette ligne. Lue
     comme une suppression, elle emporte la définition des écarts intra-famille et de leur valeur p par
     rééchantillonnage centré, que la version (B) suppose (« τ des écarts intra-famille et τ des quinze valeurs, calculés
     sur la loi nette avec leurs valeurs p »). Lue comme un remplacement, le texte scellé porterait des mots qu'aucune
     contre-lecture n'a lus. Gardée telle quelle, elle contredit (B) (« concordant : p unilatéral ≤ 0,05 »).
  2. Sous (C), le tableau est « réduit à ses colonnes « id » et « grandeur » » : la colonne « établie », qui définit la
     valeur p par rééchantillonnage centré de C-P3a (W* sur les rangs des écarts) et celle de C-P3b (τ* entre les écarts
     intra-famille), disparaît ; (C) dit pourtant « avec leurs valeurs p ». Restent au contraire, dans « Trois lectures »
     et « Sans le bras … », « « établie » seulement si les trois lectures concluent » et « établie seulement si W = 1 »,
     sans objet sous (C), qui écrit « sans lecture « établie » ni réfutation ».
  3. Sous (B) et (C), les versions renvoient au « tableau de la version recommandée, gardé (verrou 1) ». Or l'amorce
     « Version recommandée (P-021, … ; clause de repli mécanique. » n'est pas parmi les passages gardés : le nom
     « version recommandée » ne reste nulle part dans le texte scellé. Et le verrou 1 ne peut pas rester tel quel au
     scellement : il nomme les trois marqueurs `<<TRANCHER_…>>`, que `problemes` refuse (CB7-texte-02).
  Les versions ne sont donc pas « complètes et remplaçables en mots exacts » (consigne du rédacteur ; CB6-texte-01).
  La configuration, elle, tient : `repli_si_refus.C` renvoie aux champs `C_P3a`, `C_P3b`, `C_P3c`, qui gardent leurs
  définitions.
- **Ce qui devrait être** : chaque option donne un texte scellé lisible seul, aux mots déjà contre-lus.
- **Correction (mots exacts)** :
  1. Verrou 1 : remplacer « leur ligne C-P3b étant remplacée par la version (B) » par « avec deux changements dans la
     ligne C-P3b du tableau de la section « Prédiction » : « concordant : p unilatéral ≤ 0,05 par rééchantillonnage
     centré » y devient « sans verdict : p unilatéral rapporté, par rééchantillonnage centré », et « aucune ; p > 0,05 :
     « non établie » » y devient « aucune » ; la ligne C-P3b du tableau des « Critères de lecture gelés » est retirée ».
  2. Verrou 1 : remplacer « sous (C), seul le tableau de la section « Prédiction » reste, réduit à ses colonnes « id » et
     « grandeur », avec le paragraphe « Trois lectures » et la phrase « Sans le bras … ». » par « sous (C), seul le
     tableau de la section « Prédiction » reste, entier, avec le paragraphe « Trois lectures » et la phrase « Sans le
     bras … », dont la version (C) dit que les seuils ne sont pas lus. »
  3. Prédiction, (B) : remplacer « comme au tableau de la version recommandée, gardé (verrou 1), trois lectures » par
     « comme au tableau ci-dessus, trois lectures ».
  4. Prédiction, (C) : remplacer « les statistiques définies à la colonne « grandeur » du tableau de la version
     recommandée, gardé (verrou 1) (W de C-P3a, » par « les statistiques définies au tableau ci-dessus (W de C-P3a, » ;
     et remplacer « sont écrites sans lecture « établie » ni réfutation. » par « sont écrites sans lecture « établie » ni
     réfutation. Leurs valeurs p sont celles que le tableau définit (loi exacte ; rééchantillonnage centré) ; les seuils
     du tableau, la condition « « établie » seulement si les trois lectures concluent » et la règle « établie seulement
     si W = 1 » ne sont pas lus. »
  5. Critères, (B) : remplacer « C-P3a et C-P3c comme au tableau de la version recommandée, gardé (verrou 1) ; » par
     « C-P3a et C-P3c comme au tableau ci-dessus ; ».
  Configuration : aucun changement requis. Vérifié en mémoire (`corrections_essai_b7_v1.sortie.txt`) : sous (B), la
  ligne C-P3b du tableau de la « Prédiction » garde sa grandeur et sa valeur p, sans seuil ; le tableau des critères
  garde C-P3a et C-P3c.

### CB7-texte-02 — mineur — Amorces « Version recommandée » et renvois au verrou 1 au texte scellé

- **Où** : amorces des versions recommandées : P-021 (l. 618-622 et l. 1377), P-020 (l. 1091-1093), P-022 (l. 781 et
  l. 1122-1124) ; verrou 1 (l. 133-144) ; « Documents qui font foi », registre (l. 324).
- **Ce qui est.** Le verrou 1 retire « les en-têtes entre crochets et les marqueurs », pas l'amorce qui suit. Sous
  l'option retenue, le texte scellé garderait donc « Version recommandée (P-021, … recommandation de la session,
  confiance ≈ 60 %, corrigée par la session : trois lectures, verrou 1 ; transmise … ; défaut (A) le 2026-10-23 vers
  00:30 UTC) : », alors qu'aucune autre version ne reste. Le verrou 1 lui-même cite `<<TRANCHER_P021>>`,
  `<<TRANCHER_P020>>` et `<<TRANCHER_P022>>` : tant qu'il reste écrit ainsi, `problemes` refuse le scellement ; il sera
  donc réécrit, et les renvois « verrou 1 » du corps (amorce de P-021, « Documents » : « et sa ligne de correction,
  verrou 1 ») perdront leur objet. Rien ne dit comment.
- **Correction (mots exacts)** :
  1. Verrou 1, après « la décision est écrite aux champs du scellement et dans la configuration. », ajouter : « Sous la
     version retenue, l'amorce « Version recommandée » et sa parenthèse deviennent « Version retenue (champs du
     scellement, « Décisions ») » ; sous (B) ou (C) de P-021, l'amorce de la version recommandée de la section
     « Prédiction », jusqu'à « clause de repli mécanique. », est retirée avec son en-tête. Au scellement, le texte de ce
     verrou est remplacé par « Décisions de Lazar P-021, P-020 et P-022 : écrites aux champs du scellement
     (« Décisions ») et dans la configuration ; correction de P-021 : `<<LIGNE_CORRECTION_P021>>`. » »
  2. « Documents qui font foi » : remplacer « et sa ligne de correction, verrou 1) » par « et sa ligne de correction,
     `<<LIGNE_CORRECTION_P021>>`) ».

### CB7-texte-03 — mineur — Passages hors des blocs qui dépendent d'une option retirée ; « en attente » au présent

- **Où et ce qui est** :
  - « Confidentialité » (l. 13-15) : « insertion remplie du constat nu, pour les deux corpus (Métrique, point 5) » ; sous
    P-022 (a) ou (c), le point 5 ne la cite plus.
  - Liste d'arrêt 11 (l. 1451) : la garde vise « l'insertion du constat nu (bloc P-022) », qui n'existe pas sous (a) ou
    (c).
  - Contre-lecture 8 (l. 1560) : « déclenche, le cas échéant, la clause de repli du bloc P-021 » ; sous (C), la clause
    est retirée.
  - Seuil, C-P3 (l. 935) : « rééchantillonnage centré pour son verdict (et pour celui de C-P3a, …) » ; sous (B), C-P3b n'a
    pas de verdict, sous (C) aucune des trois.
  - « Ce que change le brouillon 7 » (l. 52) et rappel du brouillon 6 (l. 80 et l. 88) : « restent en attente »,
    « Décision de Lazar en attente » : vrais pour ce brouillon, faux au texte scellé, où ces paragraphes restent comme
    historique.
- **Correction (mots exacts)** :
  - remplacer « insertion remplie du constat nu, pour les deux corpus (Métrique, point 5) » par « insertion remplie du
    constat nu, pour les deux corpus (Métrique, point 5 ; option (b) de P-022 seulement) » ;
  - remplacer « ou l'insertion du constat nu (bloc P-022) » par « ou l'insertion du constat nu (bloc P-022, option
    (b)) » ;
  - remplacer « déclenche, le cas échéant, la clause de repli du bloc P-021. » par « déclenche, le cas échéant, la
    clause de repli du bloc P-021 (options (A) et (B)). » ;
  - remplacer « rééchantillonnage centré pour son verdict (et pour celui de C-P3a, avec la loi exacte) » par
    « rééchantillonnage centré pour sa valeur p (et pour celle de C-P3a, avec la loi exacte) » ;
  - remplacer « restent en attente, sous leurs marqueurs. » par « étaient en attente à l'écriture de ce brouillon, sous
    leurs marqueurs. » ; « Décision de Lazar en attente, versions de repli écrites. » par « Décision de Lazar alors en
    attente, versions de repli écrites. » ; « décision de Lazar en attente (P-022), versions de repli écrites. » par
    « décision de Lazar alors en attente (P-022), versions de repli écrites. »

### CB7-texte-04 — mineur (processus) — La contre-lecture 9 est décrite comme celle du brouillon 6

- **Où** : verrou 6 (l. 238-239) ; section « Contre-lecture », entrée 9 (l. 1562-1564) ; verrou 7 (l. 241-243).
- **Ce qui est.** Le texte cite déjà la contre-lecture « texte » du brouillon 6 et sa réponse à R-309 (« Contre-lectures
  du brouillon 6 », l. 1546-1553 ; « Ce que change le brouillon 7 »), mais garde l'entrée 9 « à venir » comme « lentille
  « texte » du brouillon 6 … question explicite : la déclaration de la réserve 14 suffit-elle ». La présente
  contre-lecture, que la consigne nomme contre-lecture 9, porte sur le brouillon 7 : si son rapport remplit les
  marqueurs de l'entrée 9, la description sera fausse. Le verrou 7 attend encore une réponse déjà donnée (« la
  déclaration suffit ; repli (b) non déclenché », constat accepté par la session).
- **Correction (mots exacts)** :
  - verrou 6 : remplacer « Contre-lecture « texte » du brouillon 6 (contre-lecture 9, avec la question : la déclaration
    de la réserve 14 suffit-elle ?) » par « Contre-lecture « texte » du brouillon 7 (contre-lecture 9 ; la question de
    R-309 a reçu sa réponse de la contre-lecture « texte » du brouillon 6 : la déclaration suffit) » ;
  - entrée 9 : remplacer « **Contre-lecture 9** — lentille « texte » du brouillon 6 (application du traitement ; question
    explicite : la déclaration de la réserve 14 suffit-elle, R-309 ?) » par « **Contre-lecture 9** — lentille « texte »
    du brouillon 7 (constats du brouillon 6 et décisions de la session appliqués ; versions de P-020, P-021 et P-022
    produites option par option ; énoncés ; configuration par indices ; sortie de `problemes` rejouée) » ;
  - verrou 7, si la session le lève (sa décision) : remplacer le point 7 par « 7. **Déclaration de la réserve 14
    (R-309)** : levé ; la contre-lecture « texte » du brouillon 6 (`68fc0dc9…`) juge la déclaration suffisante, repli (b)
    de R-309 non déclenché (constat accepté par la session : consigne du rédacteur du brouillon 7, `e8bfb03b…`). »

### CB7-texte-05 — information — points pour la session

- Défaut de P-021 : le texte écrit « défaut (A) le 2026-10-23 vers 00:30 UTC » pour une option (A) corrigée, dont la
  ligne de correction n'est pas encore au registre (`<<LIGNE_CORRECTION_P021>>`, E-02). Si le délai de 48 heures court
  de la correction, la date de l'amorce et du verrou 1 change (question déjà posée par la table, section 5).
- Registre : R-316 n'écrit ni les noms des voisins ajoutés (le texte les donne, l. 290-295) ni la portée de la décision
  sur la page de l'éditeur au corps (« vaut pour le résumé et le corps ») ; la ligne P-020 garde « à transmettre ».
  Lignes nouvelles (R12), comme la table le demande.
- Constat nu au pilote (point 1.4, version (b)) : la conséquence d'un échec de lisibilité n'est pas répétée dans le
  bloc ; la liste d'arrêt 6 (« critère du pilote non tenu après choix de la variante : nœud ») la couvre.
- Verrou 5 : les outils de contrôle du rédacteur (`structure_config_v1.py`, `voir_regles_masquees_v1.py`,
  `enonces_b6_b7_v1.py`, `essais/essai1.md`) et `problemes-brouillon7-v1.txt` ne sont pas dans la liste des versements ;
  `essais/` de ce rapport non plus (à verser avec lui, zone privée pour `versions_retenues_b7_v1.sortie.txt`).

### CB7-texte-06 — information — ce qui a été vérifié et tient (R4)

- Mots exacts (`essais/mots_exacts_b7_v1.py`, sortie à côté) : CB6-texte-01 points 1 à 5, -02 (cinq phrases), -03
  (réserve 17 entière), -04, -05 (point 1.4 et TC.1), -06, -07 (trois phrases) ; CB6-methode-courte-01 points 1 à 4 et 6
  (et l'en-tête du rappel du brouillon 6), -02, -03, -04, -06 ; décisions 3 et 4 de la session : chacun présent une fois.
  Anciens textes remplacés : absents. Configuration : `repli_si_refus.B` et `.C`, `trois_lectures`,
  `lecture_recommandee`, `clause_repli`, `C_P3a`, `C_P3b` (formule de p), `etape2.loi_nette.lecture_rho_sur_r`,
  `statut`, `constat_nu.pilote` et `.gardes` conformes aux rapports, lecture E-01 comprise.
- Écarts E-01 à E-12 : chacun vérifié sur le texte et la configuration (E-01 « trois lectures » aux six endroits dits ;
  E-02 marqueur au verrou 1 et mention aux « Documents » ; E-03 verrou 6 et entrées 8 et 10 ; E-04 position et mots ;
  E-05 cinq occurrences ; E-06 ; E-07 phrase finale de la réserve 17 et chemin de la sortie ; E-08 ajouts de
  provenance, empreintes complètes vérifiées sur disque ; E-09 trois endroits ; E-10 champs figés égaux par empreinte,
  aucune clé de graine neuve ; E-11 ; E-12 marqueurs 2, 6, 9, plus un chacun au verrou 1).
- Décisions de la session (consigne du rédacteur ; R-316) : réserve 17 (texte du rapport, étiquette descriptive, jamais
  facteur ni critère, vivier inchangé) ; constat nu lu au pilote au point 1.4 pour la lisibilité seulement, hors du choix
  des formulations, sous le marqueur de P-022, configuration `constat_nu.pilote` à l'avenant ; page de l'éditeur (mots de
  la consigne, l. 169-171) ; voisins nommés (l. 290-295 ; liste égale aux voisins cités à leurs pages dans le corps :
  Robinson et al., Khan et al., Pan et al., Qu, Fu et Hu, Yang et al., Wu et al., Poonia et Jain n'y sont cités qu'aux
  verrous et à la section « Contre-lecture »).
- Énoncés (`essais/enonces_b3_b6_b7_v1.py`) : HC1 (deux lignes), HC2, HC2b, HC3 (acquis, composantes 1 et 2 jusqu'à
  « l'agent auteur. ») égaux aux brouillons 3 et 6 ; « Pièces revendiquées » égal au brouillon 6 (absent du brouillon 3).
- Configuration (`essais/diff_config_b3_b4_v1.py`, `essais/vivier_comptes_b2_b3_b4_v1.py`) : un chemin retiré
  (`stabilite_rang.deux_lectures`), deux ajoutés (`stabilite_rang.trois_lectures`, `etape2.loi_nette.lecture_rho_sur_r`),
  douze changés, tous dans `version`, `statut`, `preenregistrement`, `stabilite_rang` et `constat_nu` (`pilote`,
  `gardes`) ; tout le reste égal par empreinte.
- `problemes` rejoué (`PYTHONPATH=R/src PYTHONDONTWRITEBYTECODE=1 python3 -B -c "from controle_ia.prereg import
  problemes; print(problemes('<brouillon 7>'))"`) : sortie égale à la dernière ligne de `problemes-brouillon7-v1.txt`
  (`essais/problemes_rejoue_b7_v1.txt`) ; marqueurs restants : scellement, contre-lectures 7 à 10, ligne de correction
  de P-021, trois décisions en attente.

## Essais (`essais/`, manifeste `sha256sums-essais-texte-b7-v1.txt`, `ca05995c…`)

| script | objet | sortie |
|---|---|---|
| `versions_retenues_b7_v1.py` (`1be179ed…`) | texte de chaque option de P-020, P-021, P-022 selon le verrou 1 écrit ; recherche des restes | `versions_retenues_b7_v1.sortie.txt` |
| `corrections_essai_b7_v1.py` (`749efd93…`) | corrections de ce rapport appliquées en mémoire ; options de P-021 rejouées | `corrections_essai_b7_v1.sortie.txt` |
| `mots_exacts_b7_v1.py` (`359fb604…`) | corrections des rapports du brouillon 6 présentes ; anciens textes absents | `mots_exacts_b7_v1.sortie.txt` |
| `enonces_b3_b6_b7_v1.py` (`834a14b1…`) | énoncés et pièces revendiquées | `enonces_b3_b6_b7_v1.sortie.txt` |
| `diff_config_b3_b4_v1.py` (`d168240d…`) ; `vivier_comptes_b2_b3_b4_v1.py` (`791a3bb0…`) | configuration par chemins, longueurs, empreintes ; vivier par comptes | sorties à côté |
| `voir_regles_b4_v1.py` (écarté) ; `voir_regles_b4_v2.py` (`b0c52c75…`) | champs de règles changés, masqués | `voir_regles_b4_v2.sortie.txt` |
| — | `problemes` rejoué | `problemes_rejoue_b7_v1.txt` |
