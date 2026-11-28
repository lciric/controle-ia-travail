# Vérification de la synthèse v5 « comment détecter » — angle « fidélité des remplacements v4 → v5 » — v1

- **Vérificateur neuf.** Je n'ai écrit ni la revue (v1 à v5), ni ses extractions, ni ses vérifications, ni leurs
  traitements, ni le script de la v5. Du 2026-10-20 vers 23:39 UTC au 2026-10-21 vers 00:10 UTC.
- **Objet.** v5 `…/revue-detection/synthese-comment-detecter-v5.md`
  (`17069e06f2f4d1a50f556c097a9278af3b2fc0d951b4d4cdd754998db3ab413d`, 565 lignes), comparée à la v4
  (`fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a`, 421 lignes).
- **Pièces, empreintes recalculées, toutes égales à leur compagnon et à la commande.** Vérification « fidélité » de la v4
  (`982ed742…`, 12 constats) ; vérification « sens » de la v4 (`84d549f7…`, 16 constats) ; traitement du correcteur
  (`21e1d56c…`) ; script `correction-v5/appliquer_corrections_v5.py` (`a1bf805a…`), `controles_v5.sh` (`e2583fe6…`),
  `pagev5.py` (`032fe9c7…`), `sortie-controles-v5.txt` (`2843b7a4…`) ; consigne du correcteur lue pour le cadre.
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad` ; `R` = `/home/user/controle-ia-travail`.
- **Lecture seule.** Aucune écriture dans `R`. Git en lecture seule (`git show`, `git log`, `git status`). Tête lue :
  `9ecd952` (registres `e8b73c64…` et `1a392407…`, ceux que cite la v5). Aucun service payant, aucun réseau, aucun
  sous-agent. Scripts lancés par `python3 -I -B`.
- **Écart à la commande, déclaré.** Pour établir l'absence des PDF de `[N]` et `[X]` (R11), j'ai lancé deux fois
  `find / -name "<nom>.pdf"` (noms 2606.12618v2 et 2407.12831v2). Cette recherche a parcouru tout le système de
  fichiers, dépôt de travail compris (`donnees/`, `runs/`, `diag/`, `prereg/`) : par nom de fichier seulement, aucun
  contenu lu ni affiché, aucune correspondance. C'est une recherche récursive dans le dépôt, que la commande interdit.
  Les autres lectures du dépôt nomment leurs fichiers.
- **Non ouverts.** `R/prereg/P3-consignes-v1.md`, fichiers `textes-actions-*`, `R/donnees/`, `R/runs/`, `R/diag/`, clés ;
  verdict v2 de P3 (cité par la v5 via R-303, comparé à R-303 seulement). De [V] (`0c8ecbdf…`, empreinte égale), seule
  la présence de « 0,8878 » aux l. 204 et 209 a été lue (`grep -n -o`). De [P] (`d975e981…`), les l. 236-253 et 270-280.
- **Conventions.** « l. » = ligne de la v5, sauf mention. « VV5-fidelite-NN » = constat de ce rapport.

## Verdict

**conforme après corrections**

- **(1) Les 28 constats sont appliqués comme le dit le traitement.** Chaque passage annoncé est à la ligne annoncée.
  Les 13 écarts aux mots exacts sont déclarés et justifiés : chacun évite une ambiguïté ou une erreur vérifiée à la source
  (brouillon de T0.6 l. 78, document de P-015 l. 16-17, [AP] p. 18, [BX] p. 3-4). Aucun ne change le sens visé par le
  constat. La colonne « écart » est remplie pour 14 constats : VV4-sens-04 n'est pas un écart (VV5-fidelite-08).
- **(2) Le script, rejoué sur une copie de la v4, redonne la v5 octet pour octet** (`17069e06…`) : 48 remplacements,
  chacun trouvé une fois dans le texte courant, sans recouvrement. Le n° 4 porte sur le texte que pose le n° 3.
- **(3) Rien n'a changé hors des 48 remplacements.** Sections 2.1 et 2.2 identiques ligne à ligne ; section 6 identique,
  plus 4 lignes ajoutées. Dans les remplacements, chaque mot changé se rattache à un constat ou à un ajout déclaré.
  Deux jonctions changent pourtant le sens d'un texte voisin non touché (VV5-fidelite-02, 03).
- **(4) Aucun chiffre neuf sans source.** Les 55 contrôles du correcteur rejoués : sortie identique (55 trouvés,
  6 artefacts rejetés). J'en ajoute 32 à la page, sur des phrases changées (32 trouvés ; 7 artefacts, 7 rejetés), et 21
  dans le dépôt (21 trouvés ; 2 artefacts, 2 rejetés). Tous les nombres neufs de la v5 viennent des deux rapports, du
  registre ou du document de P-015. Mais une phrase fusionnée contredit le typage que la v5 fait elle-même
  (VV5-fidelite-01).
- **(5) Section « Décisions prises depuis la v4 » : ses 17 renvois au registre (16 lignes) et ses 3 renvois à `go.md`
  sont exacts dans `e8b73c64…` et `1a392407…`.** Les phrases citées entre guillemets sont mot pour mot dans les lignes citées. Deux
  imprécisions de forme : R-293 rangé sous « tâches du papier C » ; R-295 (1) cité sans dire que R-299 (5) corrige
  deux autres de ses affirmations (VV5-fidelite-04, 05).
- **8 constats : 0 critique, 0 majeur, 0 moyen, 2 mineurs, 6 de forme.** Toutes les corrections sont locales. Aucune ne
  change un pouvoir, une confiance, une recommandation ni un nœud.

## Méthode

1. **Empreintes.** Les cinq pièces et les quatre fichiers du correcteur, contre leur compagnon. PDF de `R/docs/sources/pdf/`
   cités : empreinte complète égale au compagnon `.sha256` du dépôt (AP, PAR, OA, CA, YS, BX, AG, KU, MK, GM, EM, RO).
   PDF de `[N]` et `[X]` (K, LB, AU, DYL, RH, CC, MA, BU, LIAR, FQ) : absents du disque, vérifié par recherche du nom sur
   tout le système de fichiers (R11) ; leurs pages sont lues sur les extraits texte, sans empreinte du PDF (limite).
2. **Rejeu.** Copie de la v4 et du script dans `travail/`, puis `python3 -I -B appliquer_corrections_v5-copie.py`.
   Sortie `travail/v5-rejouee.md`, comparée par `cmp` à la v5.
3. **Différentiel.** `git diff --no-index --word-diff=plain` v4 → v5 (`travail/differentiel-mot-a-mot-v4-v5.txt`,
   30 blocs) ; différentiel mot à mot de chaque remplacement, ancien contre nouveau (`travail/diff-par-remplacement.txt`) ;
   position de chaque ancien texte dans la v4 (`travail/sortie-analyse-remplacements.txt`) ; 160 caractères de part et
   d'autre de chaque texte neuf, pour lire les jonctions (`travail/sortie-contextes.txt`).
4. **Mots exacts.** Chaque segment entre guillemets des corrections des deux rapports, cherché dans la v5 (espaces
   normalisés) : `travail/sortie-mots-exacts.txt`. Chaque absence relue : ancien texte retiré, segment à points de
   suspension, ou écart déclaré.
5. **Pages.** Rejeu des 55 contrôles du correcteur sur une copie (`travail/rejeu-controles/`). Puis mon outil
   indépendant `travail/verif_pages_v5.py` : pdftotext lu directement (brut puis mise en page), après empreinte complète
   égale au compagnon ; extraits texte pour `[N]` et `[X]` ; épreuve R5 de ses deux gardes sur cas sain et artefact
   (`travail/sortie-epreuve-garde.txt`).
6. **Dépôt.** Chaque renvoi de ligne des registres, dans la version que la v5 épingle (`git show`) :
   `travail/renvois_depot_v5.py` (55 lignes, plus un artefact décalé d'une ligne, rejeté). Document de P-015
   (`6e74c6cb…`, compagnon égal) l. 10-48, 84-130, 148-160 ; brouillon de T0.6 (`e212fb35…`) l. 72-82 ; registres
   l. 388-400, 460, 483, 486-509 ; `go.md` l. 28-42.

Reproduire : `python3 -I -B …/verification-v5-fidelite/travail/verif_pages_v5.py` ; `… renvois_depot_v5.py` ;
`… analyse_remplacements.py SCRIPT V4` ; rejeu : `cd travail/rejeu-controles && sh controles_v5.sh`.

## Constats, le plus grave d'abord

### Mineurs

**VV5-fidelite-01 — mineur — Confiance de 15 à 25 % : la phrase fusionnée dit que « les analogues publiés de T1 restent
au-dessus du hasard », alors que la v5 type T1 le 0,5 de [BX], au hasard.**
- **Où.** l. 368-369 (section 5, confiance) ; à confronter à l. 129-130 (section 1, point 2) et l. 260 (rang 3).
- **Ce qui est.**
  - l. 368-369 : « Les analogues publiés de T1 restent au-dessus du hasard (0,81 et 0,63 sur ce même modèle, sonde
    générique [BX p. 5-6] ; 0,964 en moyenne, sonde Pairs, à 70 milliards [PAR table 3]), mais … ».
  - l. 129-130 (VV4-fidelite-09, appliqué dans la même v5) : « Le 0,5 de [BX] (type T1 : aucune consigne, p. 4) vient
    d'un organisme affiné ». Rang 3 : « 0,5 (type T1) seulement sur organisme affiné [BX p. 8] » ; colonne « pouvoir » :
    « le hasard en aire ne vient que de l'organisme affiné ».
  - [BX] p. 8 : « from almost perfect detection 0.94 to chance performance 0.5 » (contrôlé à la page, PDF à l'empreinte).
  - La phrase de VV4-sens-05 a été écrite sur la v4, où le 0,5 n'avait pas de type. VV4-fidelite-09 lui donne le type T1.
    La fusion juxtapose les deux sans les accorder ; le traitement ne le signale pas. « publiés » étend en outre aux
    publications une phrase qui ne vaut que pour les travaux lus (R8).
- **Ce qui devrait être.** La phrase dit l'exception que la v5 type elle-même, et se limite aux travaux lus.
- **Correction (mots exacts).** l. 368-369, remplacer « Les analogues publiés de T1 restent au-dessus du hasard (0,81 et
  0,63 sur ce même modèle, sonde générique [BX p. 5-6] ; 0,964 en moyenne, sonde Pairs, à 70 milliards [PAR table 3]),
  mais » par « Les analogues lus de T1 restent au-dessus du hasard (0,81 et 0,63 sur ce même modèle, sonde générique
  [BX p. 5-6] ; 0,964 en moyenne, sonde Pairs, à 70 milliards [PAR table 3]), sauf sur l'organisme affiné de [BX] (0,5,
  sondes réentraînées sur lui, p. 8), mais » (dans le fichier, saut de ligne après « (0,81 et »). Ni chiffre ni page neufs : 0,5, « sondes réentraînées sur lui » et p. 8 sont
  déjà aux l. 129-130. Confiance inchangée (la phrase plaide pour une confiance plus haute ; la corriger ne la relève pas).

**VV5-fidelite-02 — mineur — E3, jeu (2) : le texte neuf de VV4-sens-06 s'insère devant « (sinon la sonde apprend le
régime d'incitation, [KU p. 5]) », qui change de référent.**
- **Où.** l. 338, table E3, ligne « quoi », jeu (2).
- **Ce qui est.**
  - v4 : « incitation présente chez les positifs **et** les négatifs (mêmes contextes, actes différents) : lecture
    **avant le champ** `COST` (sinon la sonde apprend le régime d'incitation, [KU p. 5]) ». « Sinon » renvoie à
    l'incitation présente des deux côtés.
  - v5 : « … : lecture **avant le champ** `COST` ; jamais sur des paires écrites qui ne diffèrent qu'au champ (avant le
    champ, à texte égal, les activations sont égales : modèle causal) (sinon la sonde apprend le régime d'incitation,
    [KU p. 5]) ; ». Le remplacement s'arrête à « `COST` » (mots exacts de VV4-sens-06) ; la parenthèse suivante, non
    touchée, se lit désormais comme la suite de « jamais sur des paires écrites ». Le sens devient faux : des paires qui ne
    diffèrent qu'au champ donnent, avant le champ, des activations égales, pas un régime d'incitation.
- **Ce qui devrait être.** La parenthèse suit l'incitation, son référent dans la v4.
- **Correction (mots exacts).** l. 338, remplacer « incitation chez les positifs **et** les négatifs, étiquette par le
  coût écrit ensuite (comme T1) : lecture **avant le champ** `COST` ; jamais sur des paires écrites qui ne diffèrent
  qu'au champ (avant le champ, à texte égal, les activations sont égales : modèle causal) (sinon la sonde apprend le
  régime d'incitation, [KU p. 5]) ; » par « incitation chez les positifs **et** les négatifs (sinon la sonde apprend le
  régime d'incitation, [KU p. 5]), étiquette par le coût écrit ensuite (comme T1) : lecture **avant le champ** `COST` ;
  jamais sur des paires écrites qui ne diffèrent qu'au champ (avant le champ, à texte égal, les activations sont égales :
  modèle causal) ; ».

### Forme

**VV5-fidelite-03 — forme — E3 : « deux jeux de paires » ne vaut plus pour le jeu (2).**
- **Où.** l. 338, même cellule : « concept 4 de P-011 en mode coût, sur les 32 tâches de réserve, deux jeux de paires,
  chacun pour sa position ».
- **Ce qui est.** Après VV4-sens-06, le jeu (2) est fait d'« actions **générées par le modèle** », étiquetées « par le
  coût écrit ensuite » ; ce ne sont plus des paires.
- **Correction (mots exacts).** Remplacer « deux jeux de paires, chacun pour sa position » par « deux jeux, chacun pour sa
  position ».

**VV5-fidelite-04 — forme — « Décisions prises depuis la v4 » : R-293 rangé sous « tâches du papier C ».**
- **Où.** l. 514 : « R-293, R-294 et GO-2026-10-20-09 (tâches du papier C) ».
- **Ce qui est.** R-293 (`registres/decisions.md` `e8b73c64…`, l. 493) : « Erreur de la session : deux écrivains sur la
  chaîne v2 de P4 ; addendum 2 de P3 : module v3 rendu, vérification neuve lancée ; P4 : module v2 vérifié, module v3
  lancé ». Seuls R-294 (l. 494) et GO-2026-10-20-09 (`go.md` l. 37) portent sur les tâches du papier C. R-293 reste sans
  effet direct sur la revue.
- **Correction (mots exacts).** Remplacer « R-293, R-294 et GO-2026-10-20-09 (tâches du papier C) » par « R-293 (chaîne et
  modules de P4 ; module v3 de l'addendum 2), R-294 et GO-2026-10-20-09 (tâches du papier C) ».

**VV5-fidelite-05 — forme — R-295 (1) est cité sans dire que R-299 (5) en corrige deux autres affirmations.**
- **Où.** l. 499 : « - **R-295 (1)** (l. 495) : faits énoncés par la session : … » ; R-299 est classé l. 514 « sans effet
  direct ».
- **Ce qui est.** R-299 (l. 499 du registre), point (5), « Corrections de R-295 » : la ligne 161 du brief est exacte,
  « aucun nœud » ; la réponse de Gemini à la requête 020 est « complète », « non tronquée ». Les deux faits que la v5
  reprend de R-295 (1) (T4 confondu par le coût de la tâche ; mention et J-lens) ne sont pas corrigés. Mais qui lit
  R-295 sur la foi de la v5 doit savoir que la ligne est en partie corrigée.
- **Correction (mots exacts).** Remplacer « - **R-295 (1)** (l. 495) : faits énoncés par la session : » par « - **R-295
  (1)** (l. 495 ; deux autres de ses affirmations, sur le brief l. 161 et sur la réponse de Gemini, sont corrigées par
  R-299 (5), l. 499, pas celles-ci) : faits énoncés par la session : ».

**VV5-fidelite-06 — forme — Lignes du document de P-015 citées sans chemin ni empreinte (R6), dans E2.**
- **Où.** l. 339 (E2, tranche) : « (P-015, l. 36-39, l. 91-94) » ; l. 342 (E2, contrôle) : « obligatoires dans P-015,
  l. 41-44) ».
- **Ce qui est.** Ce sont des lignes du document `docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`
  (`6e74c6cb…` ; vérifiées : « Diffus », l. 36-40 ; règle de l'étape 1, l. 91-92 ; étape 2, l. 94 ; conditions de
  référence obligatoires, l. 41-44). Ailleurs dans la même v5, « P-015 » sert aussi pour la ligne du registre
  (`registres/decisions.md` l. 392, à la l. 340, cellule voisine). Le chemin du document est aux Sources (l. 63-64) et
  aux l. 340 et 434, mais aux l. 339 et 342 « P-015, l. … » ne dit pas lequel des deux fichiers est lu.
- **Correction (mots exacts).** Remplacer « (P-015, l. 36-39, l. 91-94) » par « (document de P-015, `6e74c6cb…`,
  l. 36-39, l. 91-94) » ; remplacer « obligatoires dans P-015, l. 41-44) » par « obligatoires dans le document de P-015,
  `6e74c6cb…`, l. 41-44) ».

**VV5-fidelite-07 — forme — Section 6 : le titre « empreintes vérifiées ce jour » et « présents … pour MA » ne valent plus
pour la v5.**
- **Où.** l. 517 et l. 521.
- **Ce qui est.** La v5 dit elle-même (l. 80-82 et l. 564-565) que les PDF de `[N]` et de `[X]` manquent au bloc-notes
  restauré. Vérifié sur disque : aucun des dix (K, LB, AU, DYL, RH, CC, MA, BU, LIAR, FQ) ; le dossier de MA,
  `extraction/pdf-anthropic/2503.10965/`, est vide (ni PDF ni compagnon) ; `pdf-nouveaux/` n'existe pas. Le titre et la
  l. 521, repris de la v4, disent le contraire.
- **Correction (mots exacts).** Remplacer « ## 6. Table des clés (empreintes vérifiées ce jour) » par « ## 6. Table des
  clés (empreintes vérifiées pour la v4 ; v5 : `[D]` seulement, PDF de `[N]` et `[X]` absents) » ; remplacer
  « Compagnons `.sha256` (R6) : présents pour `[D]` et pour MA ; » par « Compagnons `.sha256` (R6) : présents pour `[D]` ;
  pour MA, présent à la v4, absent du bloc-notes restauré comme son PDF ; ».

**VV5-fidelite-08 — forme — Traitement : « 13 appliqués avec un écart déclaré », mais la colonne « écart » est remplie
pour 14 constats.**
- **Où.** `traitement-verification-v4-par-correcteur-v1.md`, « Bilan » et ligne VV4-sens-04.
- **Ce qui est.** Colonne « écart » non vide pour VV4-fidelite-01, 02, 03, 04, 08, 12 et VV4-sens-01, 02, 04, 05, 07, 12,
  13, 16. Pour VV4-sens-04 : « au nœud E2, la phrase unique est composée des mots du constat ». Ce n'est pas un écart :
  le constat demande « Même ajout, en une phrase, au nœud E2, option (a) ». Le compte de 13 est donc juste, mais la table
  ne le montre pas.
- **Correction (mots exacts).** Dans une v2 du traitement (R12 : la v1 reste telle quelle), colonne « écart » de
  VV4-sens-04 : « aucun (le constat demande une phrase ; elle est faite de ses mots) ».

## (1) Constat par constat : appliqué comme le dit le traitement

| constat | gravité | appliqué (v5, lignes) | mots exacts | contrôle | ici |
|---|---|---|---|---|---|
| VV4-fidelite-01 | moyen | 368-371 | fusion déclarée | « rien de publié » absent de la v5 ; [YS] p. 3 : Llama-3.1-8B-Instruct, 0,606 | 01 |
| VV4-fidelite-02 | mineur | 55-60 ; 340 | placement et « recalculée » déclarés | lignes de `cc1b108d…` et `05e7fccd…` exactes ; `e212fb35…` recalculée : égale | — |
| VV4-fidelite-03 | mineur | 340 ; 431-435 | déclaré | document de P-015 l. 115-125 : 2 à 3, 7 à 9, 15 USD ; R-283 l. 483 : « on attend la recharge » | 06 |
| VV4-fidelite-04 | mineur | 348 ; 396 ; 417 ; 426 | « aucune de ces extensions », déclaré | — | — |
| VV4-fidelite-05 | mineur | 103-106 | oui | [DYL] p. 5, phrase à la page | — |
| VV4-fidelite-06 | mineur | 263 | oui | — | — |
| VV4-fidelite-07 | mineur | 114 | oui | — | — |
| VV4-fidelite-08 | mineur | 97-99 ; 261 ; 339 | fusion déclarée | [AP] p. 18 (B.3), p. 5 | — |
| VV4-fidelite-09 | mineur | 129, 133-134 ; 260 | oui | [BX] p. 4 ; [AU] p. 6 | 01 (conséquence) |
| VV4-fidelite-10 | forme | 20-26 ; 364 | oui | — | — |
| VV4-fidelite-11 | forme | 366-367 | oui | — | — |
| VV4-fidelite-12 | forme | 295-296 ; 109, 125, 132, 138 ; 118-119 | (b) étendu, déclaré | [BX] p. 3-4 : Llama 3.1 8B Instruct ; [PAR] p. 9 | — |
| VV4-sens-01 | majeur | 339 ; 349-357 ; 401-413 | deux versions, déclaré | document de P-015 l. 36-44, 91-94, 153-155 ; [V] l. 204 : 0,8878 | 06 |
| VV4-sens-02 | moyen | 97-99 ; 131-133 ; 137-142 ; 260-261 ; 339 | fusion et rang 3 déclarés | [AP] p. 5, p. 18 ; [BX] p. 6, table 1 ; [KU] p. 4, 5, 9 ; [PAR] p. 9 | — |
| VV4-sens-03 | moyen | 90-95 ; 261 ; 339 | oui | [DYL] p. 5, 8, 11 ; [PAR] table 3 (colonnes vérifiées) | — |
| VV4-sens-04 | moyen | 339 ; 401-403 | oui (phrase composée, demandée) | [PAR] table 3 : 0,832, 0,849, 0,768, 0,844 | 08 |
| VV4-sens-05 | moyen | 368-371 | fusion déclarée | [BX] p. 5 (REPE), [PAR] p. 5 (70B) | 01 |
| VV4-sens-06 | moyen | 338 ; 340 | oui | — | 02, 03 |
| VV4-sens-07 | mineur | 121-127 ; 260 | clés en entier, déclaré | [DYL] p. 8 ; [YS] p. 2 ; [BU] p. 10 ; [BX] p. 4 ; [PAR] p. 4 ; [P] l. 238-239 | — |
| VV4-sens-08 | mineur | 88-90 ; 261 ; 339 | oui | [OA] p. 5 ; [CA] p. 6 | — |
| VV4-sens-09 | mineur | 100-108 ; 262 | oui | [CA] p. 8, p. 25 ; [DYL] p. 10, 12, table 9 (les cinq modèles d'indice 9 à 14) ; [LB] table 6 (quatre lignes) | — |
| VV4-sens-10 | mineur | 339 | oui | [CA] p. 8 | — |
| VV4-sens-11 | mineur | 282-284 | oui | [P] l. 275-278 | — |
| VV4-sens-12 | mineur | 338 ; 316-317 | « [P] l. 242 » gardé, déclaré | [P] l. 242, 249-253 | — |
| VV4-sens-13 | mineur | 342 ; 433-435 | deux écarts déclarés | brouillon l. 78 ; document de P-015 l. 16-17, 41-44, 99-100, 125 | 06 |
| VV4-sens-14 | mineur | 383-384 | oui | — | — |
| VV4-sens-15 | forme | 297 ; 338 ; 340 ; 381 ; 387-388 ; 398 ; 427-432 ; 445-448 | oui | chaque renvoi, dans sa version (partie (5) ci-dessous) | 06 |
| VV4-sens-16 | forme | 375 ; 445 ; 142, 259, 266, 271 ; 111, 261 | ordre des mots, déclaré | [AP] p. 23 | — |

« ici » : constat de ce rapport qui touche le même passage. Les lignes données par le traitement sont justes (33 lignes
relues une à une).

## (1 bis) Les écarts aux mots exacts : justifiés ?

| constat | écart | évite une erreur ? | sens changé ? |
|---|---|---|---|
| VV4-fidelite-01 et VV4-sens-05 | fusion ; « un contraste de ce type » devient « T1 » ; raison non déclarée comme jugement de la session | évite deux phrases contradictoires sur le même point ; la raison vient désormais des rapports | non, sauf l'oubli de l'exception que pose VV4-fidelite-09 (VV5-fidelite-01) |
| VV4-fidelite-02 | placé après la l. 54 ; « non recalculée ici » devient « recalculée pour la v5 : égale » | oui : la l. 34 de la v4 coupait l'énumération des l. 30-39 ; l'empreinte `e212fb35…`, recalculée ici, est égale | non |
| VV4-fidelite-03 et VV4-sens-13 | l. 340 : mots du constat plus l'estimation du document ; l. 433-435 : version de VV4-sens-13 | oui : le constat demande l'estimation « si le document … en donne une » (l. 115-125, vérifiée) ; « peut dépasser 10 USD par lancement » est contredit par P-015 (b) (l. 99-100) | non ; « nœud de dépense possible » reste à la l. 340 |
| VV4-fidelite-04 | « ni l'une ni l'autre » devient « aucune de ces extensions » | oui : trois objets après le titre neuf | non |
| VV4-fidelite-08 et VV4-sens-02 | fusion ; au rang 4 et dans E2, « la même sonde » devient « la sonde de question apprise sur « Roleplaying » » | oui : sans antécédent dans la cellule ; [AP] p. 18, section B.3 « Train on Roleplaying: Follow-up question », « Again, we trained this using 90% of the Roleplaying dataset », puis la phrase des 99 % | non |
| VV4-fidelite-12 (b) | « ce même modèle » remplacé aussi aux l. 109, 125, 138 | oui : après l'ordre neuf, l'antécédent devenait les modèles de [DYL] table 9 (l. 109) ou le Llama-3-8B de [BU] (l. 125) ; [BX] p. 3-4 : « Llama 3.1-8B », « Llama 3.1 8B Instruct » | non |
| VV4-sens-01 | mots répartis en deux versions ; version 2 sans recommandation | demandé par la consigne (point 3 : « ne tranche pas ») | non |
| VV4-sens-02 (rang 3) | « rappel 0,03 » sort aussi de « type P3-P3 » dans la colonne « littérature » | oui : sinon la colonne gardait le mélange que le constat retire de la colonne « pouvoir » | non |
| VV4-sens-04 | « phrase unique composée des mots du constat » | pas un écart (VV5-fidelite-08) | non |
| VV4-sens-05 | « aucun ne mesure » devient « aucun travail lu ne mesure » ; confiance gardée | oui (R8) ; la confiance gardée suit VV3-sens-09 (« Seule l'addition de T1 justifie la baisse »), déclaré à l'en-tête | non |
| VV4-sens-07 | clés écrites en entier au rang 3 ([DYL p. 8], [YS p. 2]) | oui : une cellule de table n'a pas d'antécédent | non |
| VV4-sens-12 | « (T2 » garde « [P] l. 242 » | ajoute un renvoi exact ([P] l. 242 : T2 = saboteur contre honnête) | non |
| VV4-sens-13 | « absents du brouillon » non repris ; « le plafond » devient « le plafond de 10 USD par lancement » | oui, deux erreurs évitées : le brouillon a un « témoin instruit » (l. 78) ; P-015 l. 16-17 : « 10 USD au plus par lancement … dépasserait plusieurs fois ce plafond » | non |
| VV4-sens-16 | « faux positif sur P3-P3 » devient « prédit sur P3-P3 un « au-dessus » qui lirait la consigne, pas l'acte, et non un nul » ; aussi dans « ce qui a changé » (l. 271) | oui : le remplacement littéral donnait « pas l'acte sur P3-P3, pas un nul » | non ; la l. 271 réécrit le résumé de la v4, et la l. 276 le dit |

## (2) Rejeu du script

- Copie de la v4 (`fba703f9…`, contrôlée par le script) → `travail/v5-rejouee.md` :
  « 48 remplacements appliqués ; sortie 17069e06… » ; `cmp` avec la v5 : identique.
- Chaque ancien texte est trouvé une seule fois dans le texte courant ; dans la v4 d'origine, 47 sur 48 sont trouvés une
  fois, sans recouvrement. Le n° 4 (puce « v5 ») s'appuie sur la fin du n° 3 : il s'applique au texte du n° 3, ce que
  l'ordre du script garantit (`travail/sortie-analyse-remplacements.txt`).

## (3) Différentiel complet v4 → v5

- Lignes 1-99 de la v4 → 1-149 de la v5 : en-tête et section 1 (remplacements 1 à 8).
- Section 2 (v4 l. 100-199 → v5 l. 150-249) : **identique ligne à ligne**. La v5 le dit (« Le fond change en sections 1,
  3, 4 et 5 »).
- Sections 3, 4, 5 : remplacements 9 à 46. Section neuve « Décisions prises depuis la v4 » (n° 47). Section 6 : identique,
  plus quatre lignes (n° 48).
- Mot à mot, dans chaque remplacement : tout mot retiré ou ajouté se rattache au constat nommé par l'entrée du script, ou
  à un ajout déclaré au traitement (« Ajouts de la v5 hors constats » : en-tête, R7, section 3, section neuve, renvois
  vers elle au nœud E2 et à la dépense, fin du document). Hors constats, deux retraits de mise en forme : le gras de
  « **taille ou la capacité du modèle** » (texte réécrit par VV4-sens-09) et « présente » dans « incitation présente »
  (mots exacts de VV4-sens-06).
- Jonctions : 48 relues. Deux changent le sens d'un texte voisin non touché : VV5-fidelite-02 et 03 (l. 338). Aucune
  autre.

## (4) Ajouts : sources et contrôles à la page

- **Nombres neufs.** Tout nombre de la v5 absent de la v4 a été cherché dans les deux rapports, le registre, `go.md` et le
  document de P-015 : tous y sont. Nombres de la littérature neufs : 79 %, 99 %, 99,9 % (rapports ; [BU] p. 10, [AP]
  p. 18, [PAR] p. 9). Nombres du dépôt : 0,6315, 0,5966, 0,5809 (R-303, l. 503) ; 2 à 3, 7 à 9, 15 USD (document de
  P-015, l. 123-125) ; numéros de ligne (tous exacts).
- **Rejeu des 55 contrôles du correcteur** (`travail/rejeu-controles/sortie-rejeu-controles-v5.txt`) : sortie identique à
  `sortie-controles-v5.txt`, à la ligne d'en-tête près (commentaire ajouté par le correcteur). 55 trouvés ; les 6
  artefacts rejetés. Limite de l'outil : `pagev5.py` compare 8 caractères de l'empreinte à la table des clés ; j'ai
  vérifié les empreintes complètes contre les compagnons du dépôt : toutes égales.
- **Mes 32 contrôles à la page, sur des phrases changées** (`travail/sortie-verif-pages-v5.txt`, section A), dont :
  - [AP] p. 18 : la sonde des « 99 % » est la sonde de question apprise sur « Roleplaying » (section B.3) ;
    l'hypothèse Instructed-Pairs est donnée contre Alpaca (B.1) ; [AP] p. 23 : « Both probes were trained on the
    Roleplaying dataset », sonde apprise sur les dernières positions ; [AP] p. 9 : rappel à 1 % de faux positifs sur le
    témoin ;
  - [PAR] table 3, p. 7 : colonnes « Backdoors » et « Sandbagging » ; p. 5 : LLaMa-3.3-70B-Instruct ; p. 3 :
    « Backdoors » hors politique ;
  - [DYL] p. 8 : réglage de couche et de classifieur sur la validation « Varied Deception » ; sonde apprise au jeton de
    réponse à « did you lie in the last message? » ; p. 11 : « Gender Secret » remis sur sa consigne d'origine ;
    p. 28 : titre de la table 9 ;
  - [LB] table 6, p. 54 : lignes Llama 3.3 70B, Mistral 3.1 24B, Gemma 3 27B (colonne ID : 0,95 ; 0,69 ; 0,58) ;
  - [BX] p. 3 et p. 4 : Llama 3.1 8B Instruct ; MMLU contre WMDP ; p. 8 : « chance performance 0.5 » ;
    [YS] p. 3 : Llama-3.1-8B-Instruct ;
  - [BU] p. 10 : Llama-3-8B-Instruct, jeux de rôle, dernier jeton, 93,8 (TTPD) ;
  - [CA] p. 8 : « 0.613–0.760 on Nemotron-3 Nano », « far lower on the smallest model of each family » ; p. 25 :
    « 30B-A3B » ; p. 6 : classes positive et négative ; [OA] p. 5 : code « programmatically-generated hardcoded » ;
    [KU] p. 5 ; [AU] p. 6.
  - Résultat : 32 trouvés sur 32. Épreuve R5 : 7 artefacts (chiffre changé, mot changé, page voisine, colonnes
    permutées, mauvaise clé), 7 rejetés. Gardes de l'outil (empreinte du PDF, empreinte du registre) : cas sain accepté,
    artefact arrêté, pour chacune.
- **Dépôt, 21 contrôles à la ligne citée** (section C) : R-303, R-295 (1), P-016, P-017, N-030, R-302, R-304, `go.md`
  l. 38-40, document de P-015 (l. 16, 38, 41, 100, 124), brouillon de T0.6 l. 78, [P] l. 278 : 21 trouvés ; 2 artefacts
  (ligne voisine, chiffre changé), 2 rejetés.
- **R8.** « rien de publié » et « seule comparaison publiée » ont disparu. Reste « Les analogues publiés de T1 restent
  au-dessus du hasard » (VV5-fidelite-01). Hors des remplacements, une phrase de la v4 non touchée : voir « Remarques ».

## (5) Section « Décisions prises depuis la v4 »

- **Renvois de ligne : tous exacts** dans `registres/decisions.md` `e8b73c64…` (tête `9ecd952`) : R-290 l. 490, R-295
  l. 495, R-296 l. 496, R-297 l. 497, R-298 l. 498, R-300 l. 500, R-302 l. 502, R-303 l. 503, R-304 l. 504, R-305 l. 505,
  R-306 l. 506, P-015 l. 392, P-016 l. 393, P-017 l. 394, P-018 l. 395, N-030 l. 396 ; et dans `registres/go.md`
  `1a392407…` : GO-2026-10-20-10 l. 38, -11 l. 39, -12 l. 40 (et -05 à -12 aux l. 33 à 40, comme le disent les Sources).
  Renvois du corps aux versions épinglées : `38579d98…` (l. 446, 453, 456, 457, 461, 468, 469), `94ebe409…` (l. 32, 34,
  35), `cc1b108d…` (l. 392, 477 et les lignes décalées de VV4-fidelite-02), `05e7fccd…` (l. 33 à 36) : tous exacts
  (`travail/sortie-renvois-depot-v5.txt`).
- **Citations mot pour mot** : « aucune sonde générique au-dessus du plancher sur (i-a) », « non détecté à cette
  puissance », « aire minimale détectable à 80 % : 0,6315 et 0,5966, contre au plus 0,5809 aux hypothèses écrites »
  (R-303) ; « partition de P3b 20/40 » (P-016) ; « B plus le rejeu contrefactuel 2 × 2 » (P-017) ; « le test à coût
  égal corrigé du coût de la tâche » (N-030) ; « T4 tel qu'écrit est confondu par le coût de la tâche (test résiduel) »
  et « une mention amorce le concept presque autant qu'une consigne » (R-295) ; « sa réserve éventuelle s'y recopie »
  (R-262, l. 460). Échéances et défauts (P-015 le 22 vers 14:30 ; P-016 à P-018 le 22 vers 21:15 ; GO-2026-10-20-11
  échéance le 21) : exacts. Recommandation de la session sur P-017 : (B), ≈ 55 % : exacte.
- **Couverture** : R-290 à R-305, GO-2026-10-20-09 à -12, P-015 à P-020 et N-030 sont tous nommés. Classements « sans
  effet direct » : justes, sauf l'étiquette de R-293 (VV5-fidelite-04). R-295 (1) : VV5-fidelite-05.

## Remarques (non comptées ; pour la session ou pour Lazar)

- **Registre modifié pendant cette vérification.** Vers 23:57 UTC, `registres/decisions.md` de l'arbre de travail a
  changé (`436fdfb6…`, non commité ; passation `2026-10-20-2355` non suivie). La garde de mon outil a arrêté la lecture
  (empreinte différente de celle que cite la v5) ; j'ai relu par `git show 9ecd952`. Les renvois de la v5 valent pour
  `e8b73c64…` : à garder épinglés si des lignes sont insérées avant la l. 503.
- **R-306** (l. 506) relance le rédacteur de P3b sur sa « consigne `f8305c0e…` inchangée ». Les constats VV4-sens-04,
  11 et 12, que le traitement demande de lui transmettre (point 5), n'y sont sans doute pas (consigne non lue ici) :
  à vérifier avant le scellement de P3b.
- **R8, texte de la v4 non touché** : rang 8, l. 265, « notre 0,57 ne se compare à aucun chiffre publié ». Forme R8 :
  « à aucun chiffre des sources lues ».
- **[N] et [X]** : les contrôles du correcteur et les miens sur DYL, LB, BU, AU reposent sur des extraits texte sans
  empreinte du PDF. À refaire sur PDF empreinté avant tout versement (R7, R6).
- `registres/depenses.md` l. 88 (coût de P3, section 4) reste cité sans version ; le brouillon de T0.6 n'a pas de
  compagnon `.sha256` dans le dépôt.

## Limites

- Angle « fidélité des remplacements » : le fond des corrections (pouvoirs, confiances, recommandations) n'est pas rejugé,
  sauf là où un remplacement contredit le texte voisin.
- Pages lues aux phrases contrôlées et à quelques voisines ; aucun chiffre recalculé à partir des données des auteurs.
- Verdict v2 de P3 non ouvert : ses faits sont comparés à R-303 et GO-2026-10-20-12.
- Ni suite de tests ni `verifier-arbre` (lecture seule ; hors de la commande).

## Fichiers écrits (chacun avec son compagnon `.sha256`)

- `…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md` (ce rapport).
- `…/revue-detection/verification-v5-fidelite/travail/` :
  - outils : `verif_pages_v5.py`, `renvois_depot_v5.py`, `analyse_remplacements.py`, `diff_par_remplacement.py`,
    `contextes.py`, `mots_exacts.py`, `epreuve_garde.py` ;
  - sorties : `sortie-verif-pages-v5.txt`, `sortie-renvois-depot-v5.txt`, `sortie-analyse-remplacements.txt`,
    `diff-par-remplacement.txt`, `differentiel-mot-a-mot-v4-v5.txt`, `sortie-contextes.txt`, `sortie-mots-exacts.txt`,
    `sortie-epreuve-garde.txt` (le dossier d'épreuve, copie d'un PDF et compagnon faux, est supprimé après usage) ;
  - rejeu : `v4-copie.md`, `appliquer_corrections_v5-copie.py`, `v5-rejouee.md` (égale à la v5) ;
    `rejeu-controles/` (`pagev5.py`, `controles_v5.sh`, copies ; `sortie-rejeu-controles-v5.txt`).
- Scripts lancés par `python3 -I -B` : aucun `__pycache__`.
