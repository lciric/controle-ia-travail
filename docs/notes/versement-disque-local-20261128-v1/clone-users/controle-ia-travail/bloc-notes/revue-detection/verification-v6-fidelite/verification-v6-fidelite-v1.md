# Vérification de la synthèse v6 « comment détecter » — angle « fidélité des remplacements v5 → v6 » — v1

- **Vérificateur neuf.** Je n'ai écrit ni la revue (v1 à v6), ni ses extractions, ni ses vérifications, ni leurs
  traitements, ni les outils du correcteur v6. 2026-10-21, de 00:28 à 00:45 UTC environ. Consigne :
  `…/consigne-verification-v6-fidelite-v1.md` (`d185a539a2ad28b479a55f67ab76c05f679832fff43dbf47eba118c92e3a0c6a`,
  compagnon égal).
- **Conventions.** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection` ;
  `R` = `/home/user/controle-ia-travail`. « l. » = ligne de la v6, sauf mention. « VV6-fidelite-NN » = constat de ce
  rapport. Les anciens textes des corrections sont cités blancs ramenés à une espace (retours à la ligne de la v6 omis).
- **Pièces, empreintes complètes recalculées, toutes égales à leur compagnon et à la consigne.**
  - v5 `…/synthese-comment-detecter-v5.md` (`17069e06f2f4d1a50f556c097a9278af3b2fc0d951b4d4cdd754998db3ab413d`, 566 lignes) ;
  - v6 `…/synthese-comment-detecter-v6.md` (`124d06f821f5780dbc810d710d08a3d00239ae34e8545fe69c3ea683177511e8`, 695 lignes) ;
  - traitement `…/traitement-verifications-v5-par-correcteur-v1.md` (`aabed8bca47cd9fe7cf7e530267afef121b7e9fa75973ec40b53cf44c386d7ab`) ;
  - vérification « fidélité » `…/verification-v5-fidelite/verification-v5-fidelite-v1.md` (`054720926c0f…`), ses 18
    sceaux de `travail/` égaux ; vérification « sens » `…/verification-v5-sens/verification-v5-sens-v1.md`
    (`e3e4a650c9f2…`), sa liste d'empreintes égale ;
  - dossier du correcteur `…/correction-v6/` : six outils et cinq sorties, sceaux égaux ; `pdf/` : dix PDF, compagnons
    égaux ; consigne du correcteur `…/consigne-correcteur-v6-v1.md` (`dc3db50a…`, compagnon égal), lue pour le cadre.
- **Lecture seule hors de mon dossier.** Écrit seulement sous `…/verification-v6-fidelite/`. Dépôt lu par chemin :
  document de P-015, brouillon de T0.6, P-011, [P] (`prereg/P3-premier-test-i-a-v1.md`, lignes citées), PDF de
  `R/docs/sources/pdf/` ; registres par `git show 9ecd952:…` (lecture seule). Bloc-notes lu par chemin :
  `brainstorm-outils-p3/reponse-claude-prompt-unique-v1.md`, trois fichiers de `p3b/` (consignes et note, aux lignes
  citées), `extraction/pdf-anthropic/2503.10965/` et `extraction/pdf-representations/` (listes et provenance).
  Non ouverts : `R/prereg/P3-consignes-v1.md`, fichiers `textes-actions-*`, `R/donnees/`, `R/runs/`, `R/diag/`,
  `R/traces/` ; [NB] (`proposition-D.md`), qui porte des valeurs de T1, T2 et T4. Aucune recherche récursive, aucun
  réseau, aucune commande git d'écriture, aucun sous-agent, aucune dépense, aucune clé affichée. Scripts lancés par
  `python3 -I -B`, `PYTHONDONTWRITEBYTECODE=1` : aucun `__pycache__`.
- **Écart déclaré.** Le chemin du bloc-notes est un lien. Une première épreuve de garde a écrit dans sa sortie le chemin
  résolu (cible du lien) ; épreuve refaite avec le chemin du lien, sortie remplacée ; aucun chemin résolu ne reste dans
  mes fichiers (contrôlé).

## Verdict

**conforme après corrections**

- **(1) Les 20 constats appliqués le sont comme le dit le traitement**, à la ligne qu'il annonce (54 lignes de
  `sortie-localiser-v6.txt` relues contre le différentiel). 33 corrections en mots exacts, sans écart ; les 8 écarts
  sont déclarés et justifiés à la source. VV5-fidelite-07 (2) : le compagnon du PDF de MA **existe** sur disque, au
  chemin exact `…/extraction/pdf-anthropic/2503.10965/2503.10965v2.pdf.sha256` (83 octets, contenu
  `6cea87ef…  2503.10965v2.pdf`, égal à la table et au PDF retéléchargé ; créé le 2026-10-20 à 23:03:07 UTC, avant la
  vérification « fidélité » de la v5) : l'écart du correcteur est juste, le rapport v5 se trompait. VV5-fidelite-08 et
  VV5-sens-14 visent d'autres fichiers ; leurs corrections sont consignées au traitement en mots exacts.
- **(2) Rien n'a changé hors des corrections déclarées.** Rejeu du script : v6 identique octet pour octet. 37 blocs de
  différentiel, tous rattachés aux 54 remplacements déclarés ; blancs mis à part, rien d'autre ; lignes vides (32), lignes
  de table (59) et barres par ligne de table inchangées. **Mais trois jonctions ou voisinages changent le sens d'un
  texte non touché** (VV6-fidelite-01 à 03), et la convention neuve « P-015 l. N » contredit une ligne non touchée
  (VV6-fidelite-04).
- **(3) Contrôles à la page : conformes.** Rejeu des outils du correcteur sur copies : sorties identiques
  (291 trouvés, 26 artefacts rejetés, gardes conformes). Mes contrôles, outil indépendant : 26 phrases et lignes de
  table à la page citée, 42 renvois de ligne, tous trouvés ; 13 artefacts, tous rejetés ; garde d'empreinte éprouvée
  (un cas sain, quatre artefacts arrêtés). **Les dix PDF retéléchargés sont identiques à ceux de la v1** : empreinte
  complète égale à `citations-synthese-v1.json` (`21868605…`), au compagnon et à la table du traitement ; nombre de
  pages égal.
- **(4) Points laissés à Lazar : conformes.** P-015 et (b′), P-017, nœud « Revendication », N-030 : chacun porte sa
  mention « **[Décision de Lazar en attente : …]** » (15 mentions au total), aucun n'est écrit comme décidé.
- **4 constats : 0 critique, 0 majeur, 0 moyen, 1 mineur, 3 de forme.** Toutes les corrections sont locales ; aucune ne
  change un pouvoir, une confiance, une recommandation ni un nœud. Après correction, aucune nouvelle vérification n'est
  nécessaire : un rejeu de `essai_corrections_vv6.py` suffit.

## Méthode

1. **Empreintes.** Toutes les pièces, contre leur compagnon et la consigne. Les dix PDF de `…/correction-v6/pdf/`
   contre la v1, leur compagnon et la table du traitement (`travail/pdf_c6_contre_v1.py`).
2. **Rejeu.** Copie des six outils du correcteur dans `travail/rejeu/`. `extraire_corrections.py` : JSON identique à
   `corrections-v5-extraites.json` (41 paires, compte vérifié dans les rapports : 9 et 32 « remplacer »).
   `appliquer_corrections_v6.py` : `v6-rejouee.md` identique à la v6 (`cmp`), journal identique. `verifier_v6.py` et
   `localiser_v6.py` : sorties identiques, 0 faute. `controles_v6.py` : seule modification, le dossier d'épreuve de la
   section G déplacé dans mon dossier (consigne : écrire seulement ici) ; sortie identique ligne pour ligne.
3. **Différentiel.** Mon différentiel ligne à ligne v5 → v6 (`travail/differentiel-lignes-v5-v6.txt`), lu en entier ;
   comptes de lignes vides, de lignes de table et de barres par ligne. Le contrôle du correcteur compare les textes
   blancs normalisés : il ne voit pas une fusion de paragraphes ; mes comptes la verraient (aucune).
4. **Jonctions.** 160 caractères avant et après chaque texte neuf (`travail/jonctions_v6.py`), relus un à un.
5. **Pages et lignes.** Outil indépendant `travail/pages_fidelite_v6.py` : garde d'empreinte complète (compagnon et
   référence v1) ; pdftotext, recherche insensible à **tous** les blancs (pagev6 réduit les blancs à une espace) ;
   lignes de table cherchées par motif sur une même ligne en mise en page, colonne comprise ; fichiers lus après
   empreinte complète. Épreuve R5 : `travail/epreuve_garde_v6.py` (dossier d'épreuve supprimé après usage).
6. **Mentions d'attente.** Relevé de toutes les mentions, de « (b') », « (C') », N-030, « Revendication », P-017 et P-015,
   avec leur ligne ; lecture du contexte de chacune.
7. **Corrections proposées.** Chaque ancien texte ci-dessous est trouvé une seule fois dans la v6, puis appliqué sur une
   copie en mémoire ; un artefact (mot changé) est rejeté (`travail/essai_corrections_vv6.py`).

Reproduire : `python3 -I -B …/verification-v6-fidelite/travail/<outil>` (arguments dans l'en-tête de chaque outil).

## Constats, le plus grave d'abord

### Mineur

**VV6-fidelite-01 — mineur — Nœud « Revendication », option (c) : la parenthèse « (avantage … ; inconvénient … ») change
de référent.**
- **Où.** l. 460-462 (section 5, nœud « Revendication et voie de R-262 (2) », options).
- **Ce qui est.** VV5-sens-08 (7), appliqué en mots exacts, insère « ; la lecture « double comptabilité », décidée
  (GO-2026-10-20-10), reste sous toutes les options » juste avant la parenthèse non touchée « (avantage : rien de déjà
  vu ; inconvénient : pas de plancher au champ) ». Dans la v5, cette parenthèse qualifiait l'option (c). Elle se lit
  désormais comme l'avantage et l'inconvénient de la lecture « double comptabilité ». Le sens devient faux :
  GO-2026-10-20-10 (`go.md` l. 38, `1a392407…`) donne à cette lecture un plancher (« directions tournées au hasard à
  covariance égale ; permutation des conditions dans la tâche »). Même défaut que VV5-fidelite-02 (une parenthèse qui
  change de référent). Le traitement ne le signale pas ; le texte vient des mots exacts du rapport « sens ».
- **Ce qui devrait être.** La parenthèse suit l'option (c) ; la lecture « double comptabilité » est dite à part, pour
  toutes les options.
- **Correction (mots exacts).** l. 460-462, remplacer « (c) P3b sans les bras du champ, avec l'oracle et la manipulation
  du nombre ; la lecture « double comptabilité », décidée (GO-2026-10-20-10), reste sous toutes les options (avantage :
  rien de déjà vu ; inconvénient : pas de plancher au champ). Recommandation : (a), confiance ≈ 65 %. » par « (c) P3b
  sans les bras du champ, avec l'oracle et la manipulation du nombre (avantage : rien de déjà vu ; inconvénient : pas de
  plancher au champ). La lecture « double comptabilité », décidée (GO-2026-10-20-10), reste sous toutes les options.
  Recommandation : (a), confiance ≈ 65 %. ».

### Forme

**VV6-fidelite-02 — forme — Table E1, « contrôle obligatoire » : l'item (vi) inséré sépare « chaque bras de production »
de sa suite non touchée.**
- **Où.** l. 397, première cellule de E1.
- **Ce qui est.** VV5-sens-08 (5) place l'item (vi) après « T4 sur chaque bras de production ; ». La suite non touchée,
  « nombres avant le champ et coûts déjà déclarés : contrôle mécanique, puis (a), (b) ou (c) des règles communes ; »,
  n'a pas d'étiquette : elle se lit désormais comme la fin de (vi), qui vient de dire « coûts déjà déclarés : premier
  pas, ou (b), (c) des règles communes ». Rien de faux pour (vi), mais un doublon, et la règle des bras de production
  perd son rattachement visible.
- **Correction (mots exacts).** l. 397, remplacer « coûts déjà déclarés : premier pas, ou (b), (c) des règles communes ;
  nombres avant le champ et coûts déjà déclarés : contrôle mécanique » par « coûts déjà déclarés : premier pas, ou (b),
  (c) des règles communes ; bras de production : nombres avant le champ et coûts déjà déclarés : contrôle mécanique ».

**VV6-fidelite-03 — forme — « Décisions », puce R-295 (1) : « La revue emploie T4 « à coût déclaré égal » » ne vaut plus
dans la v6.**
- **Où.** l. 605-606.
- **Ce qui est.** Phrase non touchée : « La revue emploie T4 « à coût déclaré égal » comme contrôle du nombre écrit
  (sections 4 et 5) : il est touché ». Depuis VV5-sens-07 (1) et (2) et VV5-sens-05 (1), les sections 4 et 5 de la v6
  écrivent T4 résiduel (l. 337-345, 368-369, 430) ; « à coût déclaré égal » n'apparaît plus qu'ici. La fin de la
  phrase, neuve, dit « la revue suit (règles communes) » : la phrase dit à la fois qu'elle emploie l'ancien T4 et
  qu'elle l'a quitté. Le correcteur a corrigé le cas voisin (« la table E1 ne l'a pas » devenu « l'a depuis la v6 »),
  pas celui-ci.
- **Correction (mots exacts).** l. 605-606, remplacer « La revue emploie T4 « à coût déclaré égal » comme contrôle du
  nombre écrit (sections 4 et 5) : il est touché » par « La v5 employait T4 « à coût déclaré égal » comme contrôle du
  nombre écrit (sections 4 et 5) : il est touché ».

**VV6-fidelite-04 — forme — Convention neuve des Sources : « P-015 l. N » renvoie « partout » au document, mais une
ligne non touchée des Sources écrit « P-015 l. 392 » pour la ligne du registre.**
- **Où.** Convention, l. 89-92 (ajout v6, au titre de VV5-fidelite-06) ; ligne « v5 » des Sources, l. 81 (non touchée) :
  « R-283 l. 483, P-015 l. 392 ; ».
- **Ce qui est.** La convention dit « « P-015 l. N » ou « P-015, l. N » renvoie partout, section « Décisions prises
  depuis la v4 » comprise, au document de P-015 (`6e74c6cb…`) ». À la l. 81, « P-015 l. 392 » est la ligne du registre
  (`registres/decisions.md` à `e8b73c64…`) ; le document n'a que 174 lignes. Pas d'erreur de lecture possible, mais la
  règle écrite est fausse pour cette occurrence (R6 : un renvoi doit dire quel fichier il lit).
- **Correction (mots exacts).** l. 90-91, remplacer « renvoie partout, section « Décisions prises depuis la v4 »
  comprise, au document de P-015 (`6e74c6cb…`) ; » par « renvoie partout, section « Décisions prises depuis la v4 »
  comprise, au document de P-015 (`6e74c6cb…`), sauf « P-015 l. 392 » dans la liste « v5 » des Sources (ligne du
  registre) ; ».

## (1) Constat par constat, et les 8 écarts

Chaque ligne annoncée par le traitement a été relue dans la v6 et dans mon différentiel. Toutes justes.

| constat | appliqué (l. de la v6) | mots exacts | contrôle | ici |
|---|---|---|---|---|
| VV5-fidelite-01 | 431-433 | oui | [BX] p. 8 (0.5 ; « re-training probes »), p. 5 (0.81), p. 6 (0.63) ; [PAR] p. 7, Full Averaging (Pairs) 5e colonne 0.964 | — |
| VV5-fidelite-02 | 393 | fusion avec VV5-sens-06 | les deux segments de 02 présents ; « (sinon … [KU p. 5]) » suit l'incitation | — |
| VV5-fidelite-03 | 393 | oui | « deux jeux, chacun pour sa position » | — |
| VV5-fidelite-04 | 627-628 | oui | R-293, l. 493 à `9ecd952` : chaîne v2 de P4, module v3 de l'addendum 2 | — |
| VV5-fidelite-05 | 602-603 | oui | R-299 l. 499 : « Corrections de R-295 » | — |
| VV5-fidelite-06 | 394 ; 397 | oui | document de P-015 l. 36-39, 41-44 | 04 (convention) |
| VV5-fidelite-07 | 631 ; 635-637 | deux écarts | voir ci-dessous | — |
| VV5-fidelite-08 | traitement seulement | mots du rapport | fichier hors du périmètre d'écriture du correcteur | — |
| VV5-sens-01 | 412-419 ; 478-497 | oui, plus deux mentions | P-015 l. 18-19, 65-66, 78, 121, 124, 147 ; [P] l. 123, 330-331 ; GO-2026-10-20-07 | — |
| VV5-sens-02 | 406-411 ; 394 ; 476-477 | oui | brouillon de T0.6 l. 28, 75 ; P-015 l. 33-34 | — |
| VV5-sens-03 | 578-591 ; 499-500 ; 372-373 | oui, plus une mention | réponse `f9aa1655…` l. 57-62 ; consigne de P3b l. 23-26 ; P-017 l. 394 | — |
| VV5-sens-04 | 195 ; 202 | oui | [BX] p. 6 (phrase, rappel à 1 %, table 1 colonne « Score » 0.03) ; [DYL] p. 28 (table 9, Varied Deception), p. 11, p. 7 | — |
| VV5-sens-05 | 429-431 ; 437-441 | oui | P-015 l. 36-39, l. 50 (bases boîte noire : la règle du coût déclaré) | 03 |
| VV5-sens-06 | 393 | oui | [P] l. 238-240 ; P-011 l. 35, 63 ; P-015 l. 138-141 | — |
| VV5-sens-07 | 337-345 ; 368-369 ; 606-608 | oui, plus une mention | [P] l. 249-253 ; réponse l. 104, 128 ; consigne de P3b l. 36 | 03 |
| VV5-sens-08 | 393-397 ; 460-461 ; 212-216 ; 575-576 | oui ; (8) paragraphe gardé | `go.md` l. 38 ; R-295 l. 495 ; R-296 l. 496 | 01, 02 |
| VV5-sens-09 | 612-621 | oui | R-306 l. 506 ; consigne de P3b l. 54 ; note `23c742be…` ; contre-lecture l. 15-16 | — |
| VV5-sens-10 | 302 | oui | [AP] p. 18 (deux moitiés de la phrase), p. 5 (témoin Alpaca) | — |
| VV5-sens-11 | 133-134 | oui | [DYL] p. 7 (questions témoins : âge ou couleur des cheveux), p. 8, p. 11 | — |
| VV5-sens-12 | 304 ; 394 | oui | [PAR] p. 7 : Backdoors en 3e colonne ; 0.832, 0.849, 0.768, 0.844 ; [DYL] p. 28 : Qwen3-8B 0.74/0.69, Qwen3-4B 0.64/0.68, Apollo avant la sonde de question | — |
| VV5-sens-13 | 564-567 | oui | R-303 l. 503 ; P-015 l. 40 | — |
| VV5-sens-14 | traitement seulement | mots du rapport | registre hors du périmètre d'écriture | — |

**Les 8 écarts aux mots exacts : tous justifiés à la source.**

| écart | justification vérifiée |
|---|---|
| VV5-fidelite-02, fusion avec VV5-sens-06 | même passage ; les deux anciens textes se recouvrent ; le texte de 06 contient la correction de 02 (« (sinon … [KU p. 5]) » après l'incitation) ; seul « (comme T1) » devient « , comme T1 ([P] l. 238-240 : …) » |
| VV5-fidelite-07 (1), complété « ; v6 : … » | les PDF sont retrouvés (consigne du correcteur, point 4) ; les 24 PDF lus par les contrôles ont l'empreinte attendue |
| VV5-fidelite-07 (2), fait contraire | compagnon de MA présent au chemin exact, contenu égal à la table, créé avant la vérification v5 (R11, contrôlé ici) |
| VV5-sens-08 (8), paragraphe gardé | la v5 a une ligne vide avant « **Ce qu'a fait Anthropic.** » (l. 174-176) ; le rapport cite ses anciens textes sans retours à la ligne (son en-tête, l. 38-39) ; dans la v6, la ligne vide est gardée |
| VV5-sens-01 (2) et (3), VV5-sens-03 (2), VV5-sens-07 (1) : mentions | demandées par la consigne du correcteur, point 3 ; texte du rapport intact de part et d'autre de chaque mention |

## (2) Différentiel v5 → v6

- 37 blocs, chacun rattaché à un remplacement déclaré : 41 corrections des rapports (dont la fusion), 14 ajouts
  déclarés au traitement (titre ; en-tête ; Sources et convention ; R7 ; section 3, deux lignes ; rang 8 ; quatre
  mentions hors constats ; section 6 ; fichiers ; jonction « la table E1 l'a depuis la v6 »).
- Hors de ces remplacements, seuls des retours à la ligne changent (lignes touchées repliées à 120 caractères ; jamais
  une ligne de table ni un titre). 32 lignes vides de part et d'autre ; 59 lignes de table, même nombre de barres
  chacune ; titres en même nombre.
- Jonctions relues : 54. Trois changent le sens d'un texte voisin non touché ou le rendent inexact (VV6-fidelite-01, 02,
  03) ; une règle neuve contredit une ligne non touchée (VV6-fidelite-04). Aucune autre. Lue sans constat : la
  fusion VV5-fidelite-01 et VV5-sens-05 (1) (« sauf sur l'organisme affiné de [BX] (…), mais avec un texte faux … ») :
  « mais » se rattache à « restent au-dessus du hasard », comme le voulait le rapport.

## (3) Contrôles à la page

- **Rejeu du correcteur** (`travail/rejeu/sortie-rejeu-controles.txt`) : identique à `sortie-controles-v6.txt`,
  sections A à G comprises : 291 trouvés, 0 absent, 26 artefacts rejetés, gardes conformes. Comptes de la ligne R7 de
  la v6 justes (55 dont 21 sur PDF de `[N]` et `[X]` ; 32 dont 11 sur DYL, LB, BU et AU ; 2 ; 119 ; 24 ; 59 ; 26).
- **Mes contrôles** (`travail/sortie-pages-fidelite-v6.txt`) : 15 PDF à empreinte égale au compagnon et à la référence
  v1 ; 18 phrases et 8 lignes de table à la page citée, toutes trouvées (phrases changées de VV5-fidelite-01, VV5-sens-04,
  06, 10, 11, 12) ; 42 renvois de ligne (document de P-015, brouillon de T0.6, P-011, [P], réponse `f9aa1655…`,
  consigne et note de P3b, registres et `go.md` à `9ecd952`), tous trouvés. Épreuve R5 : 13 artefacts (chiffre changé,
  mot changé, page ou ligne voisine, colonne voisine, colonnes permutées, mauvaise clé), tous rejetés. Garde
  d'empreinte (`travail/sortie-epreuve-garde-v6.txt`) : copie saine acceptée ; compagnon faux, octets ajoutés avec
  compagnon recalculé, nom faux dans le compagnon, compagnon absent : arrêtés (code 3).
- Lu à la page en plus des phrases : [BX] table 1, p. 6 : colonnes « Base, Content, Score » (0.03 = « Score
  Filtering ») ; [DYL] table 9, p. 28 : colonnes « AA, Apollo, DYL Probe » (0.74 = Apollo, 0.69 = sonde de question).
- **Dix PDF retéléchargés** (`travail/sortie-pdf-c6-contre-v1.txt`) : AU, BU, CC, DYL, FQ, K, LB, LIAR, MA, RH ;
  empreinte complète égale à la v1, au compagnon et à la table du traitement ; nom de fichier égal à celui de la v1 ;
  nombre de pages égal à la table. `[N]` (`pdf-nouveaux/`) absent du disque ; `[X]pdf-representations/` ne garde que
  sa provenance, dont les empreintes de BU, LIAR et FQ sont égales.

## (4) Points laissés à Lazar

| point | mentions (l.) | écrit comme décidé ? |
|---|---|---|
| P-015 et ajout d'une condition à T0.6, proposition (b′) | 38, 50, 394, 405, 418, 475, 481, 596 | non : « (b') » trois fois (l. 50, 480, 481), toujours « proposition du vérificateur », « pas de la session » ; défaut de P-015 dit « non tranchée » |
| P-017 | 51, 504, 588 | non : « divergence non résolue », options (A), (B), (C), (C') ; « défaut (A) » dit comme défaut |
| nœud « Revendication » | 393, 394, 402-403 | non : le nœud (l. 444-463) garde « Recommandation : (a) … Pas de défaut (nœud) » |
| N-030 | 345 | non : puce l. 599 « nœud, non tranché » ; T4 résiduel dans T0.7 « seulement si tu retiens N-030 (B) » |

Les quatre portent leur mention là où une phrase suppose la décision. La liste du traitement (neuf points) concorde
avec la v6.

## Remarques (non comptées ; pour la session)

- Les puces N-030 (l. 599) et le nœud « Revendication » lui-même (l. 444) n'ont pas de mention, alors que la puce P-015
  (l. 596) en a une. Rien n'y est écrit comme décidé ; une mention de plus rendrait la lecture uniforme.
- L'en-tête v6 (l. 50-51) range « options (A), (B), (C), (C') de P-017 » parmi « les propositions du vérificateur
  « sens » » : (A) à (C) viennent de P-017 (registre l. 394) ; seuls (C′) et la mise en options sont du vérificateur.
- La section « Décisions » garde le point de vue de la v5 (« Le corps de la v5 garde … », l. 555-556 ; « cette v5 vient d'un
  correcteur neuf », l. 623-624) : vrai comme histoire, à dater si la section est reprise.
- Une note v2 de transmission à P3b existe depuis 00:27 UTC (`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b/a-transmettre-contre-lecture-P3b-v2.md`), après
  la v6 ; la v6 cite la v1, ce qui était juste à son heure.
- La vérification « fidélité » de la v5 disait le dossier de MA « vide (ni PDF ni compagnon) » : faux pour le
  compagnon. Sa recherche par nom visait les PDF seuls.

## Limites

- Angle « fidélité » : le fond des corrections (pouvoirs, confiances, recommandations) n'est pas rejugé, sauf là où un
  remplacement rend faux un texte voisin.
- Téléchargement depuis arxiv.org : non vérifiable ici ; seule l'égalité des empreintes avec la v1 l'est.
- [NB] non ouvert (valeurs de T1, T2 et T4) : « [NB] `proposition-D.md` l. 81-99 », repris dans la puce P-017, est
  hérité de la section 4 de la v5 (l. 321), non revérifié ici.
- Ni suite de tests ni `verifier-arbre` (lecture seule ; hors de la consigne).

## Fichiers écrits (sous `…/verification-v6-fidelite/`)

- `verification-v6-fidelite-v1.md` (ce rapport) et son sceau `verification-v6-fidelite-v1.md.sha256`.
- `travail/` : outils `pages_fidelite_v6.py`, `epreuve_garde_v6.py`, `jonctions_v6.py`, `pdf_c6_contre_v1.py`,
  `essai_corrections_vv6.py` ; sorties `sortie-pages-fidelite-v6.txt`, `sortie-epreuve-garde-v6.txt`,
  `sortie-jonctions-v6.txt`, `sortie-pdf-c6-contre-v1.txt`, `sortie-essai-corrections-vv6.txt`,
  `differentiel-lignes-v5-v6.txt` ; `rejeu/` (copies des outils du correcteur, `controles_v6-epreuve-deplacee.py`,
  `corrections-rejouees.json`, `v6-rejouee.md`, sorties `sortie-rejeu-*.txt`).
- Empreintes de tous ces fichiers : `empreintes-travail-v6-fidelite.sha256` (format `sha256sum`, noms relatifs) et son
  sceau.
