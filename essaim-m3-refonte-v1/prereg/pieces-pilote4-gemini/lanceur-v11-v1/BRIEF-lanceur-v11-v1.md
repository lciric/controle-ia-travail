# Brief — lanceur v11 du pilote 4 (seconde course : la v6.2.1 sur la question S) et sa batterie d'essais v13 — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 04:20 UTC (heure lue sur `date -u`) pour un sous-agent neuf. Langue :
français, sans acronymes. Tu lis seulement `/var/tmp/lanceur-v11-v1/fournis/` (empreintes : `../EMPREINTES-fournis-v1.txt`)
et tu écris seulement dans `/var/tmp/lanceur-v11-v1/sortie/`. **Interdits** : aucun `git` (le lanceur en contient, tu ne
l'exécutes pas), aucune exécution du lanceur ni de la batterie (c'est conv-audit qui la lance), aucun sous-agent, aucun
réseau, aucune clé, aucune recherche hors de `fournis/`. Permis : `python3 -I` sur tes scripts de dérivation, `bash -n`
(syntaxe seule), `diff`, `sha256sum`. Heure lue sur `date -u` dans la commande même où tu l'écris.

## Le fait (décision de Lazar, R-492, 26 octobre, 04:13 UTC, verbatim : « pas besoin de faire v5.3, en revanche ppose la question de la structure de l'organsime S »)

Le pilote 4 fait tourner la v6.2.1 sur la question M (course `v6-2`, partie à 03:51 UTC sous le lanceur v10,
`lancer_pilote4_gemini_v10.sh`, `0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952`, dossier réel
`pilotes/pilote4-gemini-v6-2-v1-tentative2`). **La v5.3 ne court pas.** La seconde course est **le même organisme, la
v6.2.1** (commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`,
26 fichiers), **sur la question S** : `question-S-v2.md` fourni, dans le dépôt
`brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md`,
commit `4772b525081342a6a30ba8823733aa5770a888a8`, sha256 `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289`
(la question de la course S du second pilote). Mêmes bornes (4 générations, 6 rondes de conception à 3 USD et 900 s,
75 USD par course, segments à 3 400 s), même GO (`GO-2026-10-25-02`), après une course M saine. Un texte v5 du pilote
(différentiel sur la v4) est écrit en parallèle par conv-audit ; il citera l'empreinte du lanceur v11, portera une entropie
nouvelle et la ligne `graine de la course v6-2-s = <N>` (enfant 0 de `SeedSequence(E).spawn(2)`), et restituera la ligne
`graine de la course v6-2 = 2334107546136117589` (graine de la course M, texte v4) pour la porte « course précédente ».

## Ce que tu écris (dans `sortie/`), sur le modèle exact des pièces fournies

1. `deriver_lanceur_pilote4_v11.py` : dérive `lancer_pilote4_gemini_v11.sh` de la v10 par **remplacements exacts au nombre
   attendu** (comme `deriver_lanceur_pilote4_v10.py`), refuse si l'empreinte source n'est pas celle de la v10, si une
   occurrence n'est pas au nombre attendu, si un reste interdit subsiste, ou si la sortie existe. Puis exécute-le et
   rends `lancer_pilote4_gemini_v11.sh` et `diff-lanceur-pilote4-v10-vers-v11.txt` (`diff -u`). **Changements, et rien
   d'autre** :
   - clé de course `v5-3` → `v6-2-s` partout (variable `COURSE`, `case`, messages, commentaires, en-tête) ; dans la
     branche `v6-2-s)` : `NOM="pilote4-gemini-v6-2-s-v1"`, `INDICE_GRAINE=0`, organisme = la v6.2.1 (commit, arbre, 26
     fichiers, comme la branche `v6-2`), `LIGNEE="gemini-organisme-v6-2-s"` ;
   - la question devient **par course** : les trois constantes `COMMIT_QUESTION`, `CHEMIN_QUESTION`, `SHA_QUESTION` passent
     dans chaque branche du `case` — M (`a15809b816b6c967b6c3cf21877e350bfe676dca`, chemin et `8b1c7511…` actuels) pour
     `v6-2` ; S (commit, chemin et empreinte ci-dessus) pour `v6-2-s` ; la surcharge d'essai `[ "$ART" = commit ] &&
     COMMIT_QUESTION=…` reste après le `case` et garde son effet ;
   - juste après le `case` : en mode réel, `COURSE=v6-2` est refusée (`refus_tot`) : la course M a tourné sous le
     lanceur v10 (R-490) ; ce lanceur v11 ne lance en réel que `v6-2-s` (R-492) ; en simulation, `v6-2` reste permise (la
     batterie en a besoin pour produire la course précédente) ;
   - porte « course précédente » (`PRECEDENTE_V62`) : conditionnée sur `v6-2-s` au lieu de `v5-3` ; messages « v5.3 ne
     part qu'après… » → « la course S ne part qu'après… » ; **le lanceur attendu pour la course précédente** devient deux
     variables définies avant la porte : en mode réel `LANCEUR_V62_NOM=lancer_pilote4_gemini_v10.sh` et
     `LANCEUR_V62_SHA=0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952` (la course M a tourné sous la v10) ;
     en simulation, le nom et l'empreinte de ce lanceur-ci (`basename "$0"`, `SHA_LANCEUR`), pour que la batterie produise
     la course précédente avec le lanceur sous essai ; l'appel du contrôle Python passe ces deux variables à la place de
     `"$SHA_LANCEUR"` et `"$(basename "$0")"` ; les autres paramètres (`gemini-organisme-v6-2`, `v6-2`,
     `pilote4-gemini-v6-2-v1`, le GO) ne changent pas ;
   - contrôle de la graine de la course précédente (`GRAINE_V62_MANIFESTE`) : conditionné sur `v6-2-s` ;
   - message de la ligne de dépense « de v5.3 » → « de la course S » ;
   - en-tête : v11 dérivé de la v10 (empreinte, script, motif R-492, écart consigné) ; usage : `COURSE=v6-2-s …
     PRECEDENTE_V62=<dossier de la course M de ce pilote, pilote4-gemini-v6-2-v1[-tentativeN]>` ; une ligne dit que la
     v5.3 ne court pas (R-492) et que la clé `v6-2` ne sert plus qu'en simulation.
   Vérifications finales du script : aucun `v5-3` ni `v5.3` ne subsiste hors de la phrase « la v5.3 ne court pas » ;
   `6251ab21` et `4ecba58` absents ; `a54da93e` présent une fois dans le code ; `8b1c7511` présent une fois ;
   `lancer_pilote4_gemini_v10.sh` présent exactement là où la porte l'attend et dans l'en-tête.
2. `deriver_essais_pilote4_v13.py` : dérive `essais_lanceur_pilote4_v13.sh` de la v12 (même mécanique, mêmes refus) :
   chaque cas de la v12 garde un équivalent (`v5-3` → `v6-2-s`, noms, lignée, messages attendus, question S dans les
   lignes de GO d'essai : une ligne saine porte `8b1c7511…`, `a54da93e…` et `4f13647a…` ; `6251ab21…` n'est plus
   requis) ; ajoute au moins : (i) en mode réel, `COURSE=v6-2` refusée (« a tourné sous le lanceur v10 ») ; (ii) en
   simulation, la course `v6-2-s` refusée si la ligne de GO porte `8b1c7511` et non `a54da93e` ; (iii) la course
   `v6-2-s` saine de bout en bout après une `v6-2` saine produite par ce lanceur en simulation ; (iv) un cas où le
   `LANCEMENT.md` de la course précédente cite un autre lanceur (refus « n a pas tourné sous ce lanceur ») — s'il existe
   déjà, garde-le. L'en-tête de la batterie dit ce qui change. Exécute la dérivation, pas la batterie. Si un remplacement
   exact est impossible sans réécriture, écris-le dans le LISEZMOI, avec le cas concerné.
3. `LISEZMOI-lanceur-v11-v1.md` : ce que tu as fait ; la liste des remplacements ; les cas ajoutés ; les choix faits seul
   (une ligne chacun) ; ce que tu n'as pas pu vérifier sans exécuter ; les empreintes de tes fichiers (compagnons
   `.sha256`, format « empreinte, deux espaces, nom nu »). `bash -n` sur le lanceur et la batterie.

À la fin, réponds en quatre lignes : les empreintes du lanceur v11 et de la batterie v13, le nombre de cas (v12, v13), ce
qui n'a pas pu être fait par remplacement exact, ce qui reste incertain.
