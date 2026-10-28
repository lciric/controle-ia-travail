# Brief — boucle extérieure du pilote 4, v3 : traiter la contre-lecture (CLB-01 à CLB-19) et les faits nouveaux — v3

Écrit par la lignée conv-audit le 26 octobre 2026 à 04:28 UTC (heure lue sur `date -u`) pour un sous-agent neuf, qui n'a
écrit ni la v2 ni sa contre-lecture. Langue : français, sans acronymes, phrases courtes. Tu lis seulement
`/var/tmp/boucle-exterieure-pilote4-v3/fournis/` (empreintes : `../EMPREINTES-fournis-v1.txt`) et tu écris seulement dans
`/var/tmp/boucle-exterieure-pilote4-v3/sortie/`. Interdits : aucun `git`, aucun sous-agent, aucun réseau, aucune clé,
aucune recherche hors de `fournis/` ; **aucun score n'existe, n'en invente aucun** ; aucune hypothèse, aucun critère, aucune
stratégie de classement des tâches ; rien de ce que tu écris n'est servi à un organisme ; heure lue sur `date -u` dans la
commande même où tu l'écris.

## Ce que tu as
- La v2 (registre `registre-hypotheses-conception-pilote4-v2.md`, protocole `protocole-boucle-exterieure-pilote4-v1.md`,
  briefs `brief-agents-fin-de-course-v1.md`, `LISEZMOI-sortie-v2.md`) et le brief qui l'a produite (`brief-v2.md`).
- **La contre-lecture** `rapport-contre-lecture-boucle-exterieure-v1.md` : verdict « utilisable après corrections » ;
  CLB-01 à CLB-11 à corriger avant usage, CLB-12 à CLB-19 mineurs. **Traite chaque constat**, un par un, et dis pour chacun
  ce que tu as fait (table « constat → traitement » à la fin du LISEZMOI) ; un constat que tu refuses de traiter est
  déclaré avec le motif.
- Le texte v4 du pilote (`782b858c…`, qui prime), la contre-lecture 7, le brief du script de lecture et le **LISEZMOI du
  script écrit** (`LISEZMOI-script-lecture-v1.md` : ce que la sortie du script contient réellement — les agents ne voient
  que cette sortie), les hypothèses de (b), les synthèses « agents sur le noyau » et « littérature des boucles », la
  fiche de lecture des papiers (pour les gardes : journal des lectures, compteur, comparaisons A contre A, étalonnage des
  agents sur des paires à blanc avant tout droit d'éliminer, `test_final` lu une fois).

## Faits nouveaux (à appliquer partout)
1. **La v5.3 ne court pas** (mot de Lazar, R-492, 04:13 UTC) : la seconde course du pilote 4 est **le même organisme, la
   v6.2.1, sur la question S** (course `pilote4-gemini-v6-2-s-v1`), après la course M (`pilote4-gemini-v6-2-v1`, dossier
   réel `pilote4-gemini-v6-2-v1-tentative2`, partie à 03:51 UTC). Brouillon du texte v5 fourni
   (`pilote4-gemini-organisme-v5-brouillon.md`, non relu, marqueurs `[[…]]` et `<<…>>` à ignorer) : « aucune comparaison
   entre les deux courses » (mêmes tâches, même objet, questions différentes, une graine chacune). Toute fiche qui nomme
   la v5.3 est à réécrire ou à déclarer « indécidable par ce pilote » (la v5.3 reste l'objet de comparaison de (b), sur la
   banque v6) ; dis quelles fiches portent sur la course S et ce que la question S y change (rien n'est à supposer de ce
   que l'organisme répondra).
2. **Décisions de Lazar de 05:13 Paris** (`decision-N-taches-fraiches-et-lecture-test-final-v1.md`) : à la fin de chaque
   course, seuls les scores de `test` et les faits mécaniques s'ouvrent (après la décision sur les graines) ; **`test_final`
   se lit une seule fois, à la fin du compteur de rondes** ; la sortie du script sera séparée en deux fichiers par
   course. Les fiches tranchées par `test_final` le sont à la fin du compteur ; le protocole le dit, et dit ce qui se décide
   à chaque course sans `test_final`.
3. Le **relevé mécanique (B)** n'existe pas (CLB-02) : écris sa spécification exacte (champs, source dans l'extrait
   mécanique et `LANCEMENT.md`, ce qu'il ne porte jamais : aucun score, aucun texte) comme une pièce à produire par
   conv-audit et à essayer sur un cas sain et un artefact avant la première lecture ; la boucle ne démarre pas sans lui.
4. Les gardes venues des lectures (fiche et synthèses) : journal des lancements et des lectures avec attente chiffrée ;
   compteur et budget fixés d'avance avec l'issue « plateau » ; comparaisons A contre A avant tout droit d'éliminer ;
   `test_final` lu une fois ; un plafond de dépense des relances laissé à Lazar.

## Ce que tu écris (dans `sortie/`)
`registre-hypotheses-conception-pilote4-v3.md`, `protocole-boucle-exterieure-pilote4-v2.md`, `brief-agents-fin-de-course-v2.md`,
`specification-releve-mecanique-B-v1.md`, `LISEZMOI-sortie-v3.md` (ce que tu as fait ; table constat → traitement ; choix
faits seul ; points pour conv-audit et pour Lazar ; écarts déclarés), et le compagnon `.sha256` de chaque fichier
(format « empreinte, deux espaces, nom nu »). Versions dans les noms, jamais d'écrasement (R12). À la fin, réponds en
cinq lignes au plus : constats traités et refusés, fiches changées, points pour Lazar, empreintes.
