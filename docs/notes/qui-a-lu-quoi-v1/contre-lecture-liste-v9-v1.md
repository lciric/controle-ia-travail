# Contre-lecture de la liste « qui a lu quoi » version 9 — v1

Contre-lecteur neuf (règle R2), qui n'a écrit aucune version de la liste, ni le mandat, ni aucune contre-lecture antérieure. Objet : `registres/qui-a-lu-quoi-v9.md` (`a30b756138bb4e91febaa40c199220a1d5ed36832a16045188a5eab3ed4d5cc1`, compagnon conforme, vérifié) contre `registres/qui-a-lu-quoi-v8.md` (`5ab419da4ee5d42f08ba2a2ba53495320a8e1d10cd2423a3e89a1388695d1c66`, vérifié) et le mandat `docs/notes/qui-a-lu-quoi-v1/mandat-redacteur-liste-v9-v1.md` (`3348eb3b08c118f4b3fa6b2b65f3a28bd6702973625115e7e0a12353f0eb3364`, compagnon conforme, vérifié).

## Verdict

**En vigueur possible.** Aucun bloquant. Sept mineurs, à corriger dans une version 10 ou par une note de la mère, sans empêcher la mise en vigueur.

## 1. Recopie de la version 8 (par programme)

`diff` : 2 lignes retirées, 15 ajoutées (décompte égal à celui de R-3305). Opérations rejouées avec `difflib` : remplacement de la ligne 1 (titre), remplacement de la ligne 3 par 2 lignes (puce de la version 9 ; puce de la version 8), insertion de 9 lignes de tableau (196 à 204) après la ligne 194 de la version 8, insertion de 2 lignes (réserve 21 et ligne vide), insertion de 1 ligne de fin. Chaque ligne confrontée aux changements annoncés (1) à (6) de la puce « Version 9 » : tout est annoncé. La puce de la version 8 est la ligne 3 de la version 8 avec le seul remplacement « (ce fichier) » par « (version précédente) », vérifié par programme (égalité exacte). Aucun changement non annoncé.

## 2. Exclusions (comparaison de la colonne « exclu de », par programme)

- Ligne 196 égale à l'octet à la ligne 190 : oui.
- Ligne 198 égale à l'octet à la ligne 191 : oui.
- Ligne 199 commence par l'octet exact de la ligne 184 et y ajoute seulement « (comme la ligne 184, opérateur de la création de la machine de l'étape B bis) » : oui.
- Ligne 197 : non égale à l'octet à la ligne 194, et ce n'est pas attendu (elle renvoie à la ligne 196 au lieu de la ligne 190, et cite « ligne 194 » à la place de la phrase sur le terme de la question posée à Lazar). Contenu : « celles de la ligne 196 » (égales à la ligne 190) + celles de la ligne 187 + tout rôle de lecteur du premier test boîte blanche bis (témoin positif) : même ensemble que la ligne 194, rien retiré. Les lignes 200 à 203 portent « aucune exclusion déclarée », ce qui est la règle du mandat (les lignes remplacées, 192 et 193, n'en portaient pas).

## 3. Colonnes « a lu » et « source », lignes 196 à 204

Sources lues : les cinq passations de l'hôte par `git show origin/claude/happy-gauss-x45o3o:…` (empreintes recalculées, égales à celles du mandat, à celles de la colonne « source » de la ligne 196 et à leurs compagnons sur la branche ; commits porteurs `505510e5`, `2c5ccbf6`, `50e5ca57`, `d3bd64ce`, `e3fc9343` retrouvés par `git log -- chemin`, nouveau pic de la branche `9c370e88`) ; R-3284 à R-3305 par leur numéro ; registre des canaux v3 (`b49ac90c…`, vérifié).

- Ligne 196 : tous les faits retrouvés dans les passations (H3N-001 à H3N-015, verbatim des mots de Lazar, heures, branche, empreintes) ; lettre du modèle, « rapporté, non vérifié » : R-3286 le dit. Rien d'inventé. L'écart H3N-004 a omis le détail « sauf la branche de l'attaquant informé, filtrée » : sans conséquence.
- Ligne 198 : R-3284 (ouverture 13:43Z, passation 1045, intermédiaire 13:23Z), R-3291 à R-3297 (gestes 1 à 18 joués, GO-2026-11-18-25 et -28), R-3286/3288/3294/3298 (messages des sœurs), canaux v3 (autrice). « Brief de reprise » et « état » : mandat seul (voir mineur 4).
- Ligne 199 : R-3289, R-3290, R-3291 ; correct.
- Ligne 200 : R-3286 et canaux v3 pour le rôle, la branche, la tête, le seuil de 2,6 USD ; la colonne « a lu » ne vient que du mandat (voir mineur 4).
- Ligne 201 : R-3288, R-3294, canaux v3 ; « a écrit la note » est une inférence (voir mineur 5).
- Lignes 202 et 203 : R-3294, R-3298, R-3300 pour les compléments ; faits retrouvés (v39 à v44, `1b0dc94e…`, `f8335e8c`, `ae3a365f`, clone `a41b7b50`, spécification `2ddb1117…`, `a50da905`, page de prix `35a04829…`, passation `5f8c8037…`).
- Ligne 204 : cohérente avec le mandat et avec la réserve 21 (j).

Aucun fait sans source ; aucune source qui dise autre chose que la ligne.

## 4. Mots portant un état, une issue ou un score

Parcours par mots-clés des 15 lignes ajoutées (état, refus, conforme, marge, crédit, code, adoptée, verdict, score, aire) et lecture : aucun mot des pièces porteur d'un état, d'une issue ou d'un score n'est recopié. Les faits d'exploitation de l'apprentissage des sondes sur la tâche (H3N-003, H3N-010) sont dits « non recopiés ». Les « sujets d'états de l'étape B » ne sont pas cités. Réserve : voir mineur 2.

## 5. Convention d'identifiant, attestation

L'identifiant entier de l'hôte et ses douze premiers caractères (`013QMayiv5x2`) n'apparaissent que dans la ligne 196 (un seul compte pour chaque motif, vérifié par `grep -c`).

Programme `docs/procedures/lecture-7b-etape-b-compte-3-v1/attestation_qui_a_lu_quoi_compte_3_v3.py` (`a20f137c…`), joué avec la cellule « exclu de » de la ligne 196, code 0 :

`ATTESTATION : CONFORME — session session_013QMayiv5x2aD8SXQW1vMvP : aucune mention hors des lignes admises, préfixe compris (qui-a-lu-quoi-v9.md, a30b756138bb…) ; lignes du compte 3 : 4 sans exclusion, 2 d'une autre session identifiée : « 134 » (session_016QhUrrSUMEzEqWPnQYxjHB); « 190 » (session_01XJ6MgqbSRXu3sBZqYjT9VV) ; lignes de l'hôte admises : 1`

Ce qu'il ne voit pas : la ligne 197 (ses colonnes « session » et « compte » ne nomment ni l'hôte ni le compte 3 ; elle est donc sautée, et son contenu d'exclusions n'est vérifié par rien d'autre que cette contre-lecture, faite ci-dessus) ; les colonnes « a lu », « source », « modèle », « rôle » de toutes les lignes ; les lignes 198 à 204 (elles ne nomment pas le compte 3) ; tout mot porteur d'un état ; toute exclusion retirée d'une autre ligne ; la vérité des faits.

## 6. Points signalés par le rédacteur

(a) Prédécesseur des lentilles : la ligne 201 dit « remplace la session de la ligne 192 ; le registre des canaux v3 lui donne un autre prédécesseur, réserve 21 », ce qui est exact (ligne 192 : `session_01XJ6MgnoxfSYHdF6rpEqZ7w`, reprise de 01:16Z ; canaux v3 : `session_01XJ6MgpKJHG5ue54rCpu4Ny`). La lecture de la mère (R-3305 : deux reprises successives, les deux sont prédécesseurs) est postérieure au texte de la version 9 et n'y figure pas ; la ligne n'est pas fausse, elle est incomplète (mineur 6).
(b) Changement « (ce fichier) » en « (version précédente) » : annoncé, au (3) de la puce, comme initiative du rédacteur hors mandat, et par analogie avec la version 8. Admis.
(c) Lecture hors plage (numéro, heure et début du titre de R-3280 à R-3283, 80 caractères) : déclarée dans la ligne 204 et en réserve 21 (j). Admis.
(d) Ligne de la mère, gestes 19 à 24 : la réserve 21 (f) dit que c'est « une règle que la mère se déclare, non un fait constaté ». Dans la cellule elle-même, la formule est « en lit, aux gestes 19 à 24 (…, en cours ou à venir à l'heure de cette version, R-3297), les seules lignes `BBIS` … selon le mandat de ce rédacteur » : l'attribution au mandat et le « à venir » sont là, mais le verbe est au présent ; mineur 1.

## 7. Heures

Heure unique de la version 9 : 2026-11-18T15:58:01Z. Commit qui la verse : `99492b8534d52c949603878945d9e632b8ddc739`, 2026-11-18T15:59:13+00:00 (R-3305 : 15:59:12Z). L'heure est antérieure. Arbre propre (`git status`, rien à signaler pour ces fichiers).

## Mineurs

1. Ligne 198, « a lu » : « en lit, aux gestes 19 à 24 » au présent ; écrire « doit lire, d'après la règle qu'elle s'est déclarée » (la réserve 21 (f) le dit déjà, la cellule non). Les types de lignes `BBIS` listés (marche, poussé, FIN, ARRET) sont des noms d'étapes, non des contenus ; à garder tels quels, mais la fin et l'arrêt sont par nature des états : la présence de ces lignes dit déjà quelque chose de la course.
2. Ligne 198, même cellule : les deux sources de la règle sont le mandat (déclaration de la mère) et R-3297 ; aucune pièce ne montre ce que la mère a effectivement lu aux gestes 19 à 24 : à rectifier dans une version 10 une fois la course finie.
3. Ligne 196, « rôle » : « aucune commande jouée à ce jour » sans date ; la colonne « a lu » est datée de la passation de 15:30Z ; ajouter la date dans le rôle.
4. Lignes 198 (« brief de reprise », « état », identifiant du prédécesseur `session_01XJ6Mgr8BN6UanALsQatc5E`) et 200 (toute la colonne « a lu ») : sources = le mandat, c'est-à-dire la déclaration de la mère ; la colonne « source » et la réserve 21 (e) le disent. Le message de l'attaquant informé n'est pas dans les sources permises et n'a pas été vérifié ici. À faire confirmer par la session concernée avant de s'en servir comme preuve de non-lecture.
5. Ligne 201 : « a écrit la note du mot de Lazar » n'est que ce que R-3294 laisse entendre (la note est dans la branche de la session) ; écrire « note de sa branche ».
6. Ligne 201 et réserve 21 (d) : versions à compléter avec la lecture de la mère de R-3305 (deux reprises successives, deux prédécesseurs) dans la version 10.
7. Ligne 197 et réserve 19 : l'attestation ne voit pas la ligne 197 ; l'égalité de ses exclusions avec la ligne 194 a été vérifiée par cette contre-lecture à la main et ne l'est par aucun programme. Point à porter à Lazar avec le programme d'attestation (réserves 14 et 19).

## Lectures hors périmètre

Aucune. Lu : la version 9, la version 8, le mandat, les cinq passations de l'hôte (par `git show`), les lignes R-3284 à R-3305 de `registres/decisions.md` par leur numéro (l'extrait de R-3305 est inclus car la mère le cite pour la version 9), le registre des canaux v3, le programme d'attestation, `git log` de la branche de l'hôte (heures et identifiants courts, sans sujet) ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, aucune branche `calcul/` ni `donnees/`, aucune recherche récursive. Les lignes R-3301 à R-3303, lues avec la plage, portent des états de travaux (barreaux 6 à 8, organismes discrets) sans résultat ; déclarées par prudence.
