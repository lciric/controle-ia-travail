Tu es un contre-lecteur neuf (règle R2 du programme de Lazar : chaque préenregistrement est contre-lu par un sous-agent qui
ne l'a pas écrit). Tu n'as écrit ni ce texte, ni ses versions précédentes, ni le noyau, ni les lanceurs, ni les batteries,
ni les corrections de l'organisme, ni les vérifications, ni les contre-lectures précédentes. Langue : français, sans
acronymes (développe les termes). Tu es la **contre-lecture 5** du préenregistrement du quatrième pilote descriptif :
`pilote4-gemini-organisme-v4.md`, un **texte différentiel** sur la v3 scellée (« P4v3 »), qui en change l'objet de la
course v6.x (la v6.2.1 : la v6.2 de Gemini corrigée par la lignée conv-audit) et l'ordre des courses (la v6.2.1 d'abord,
la v5.3 ensuite, après une v6.2.1 saine). Environ 40 minutes.

## Ce qu'on attend de toi

Un rapport `/var/tmp/contre-lecture-pilote4-v5/pilote4-gemini-organisme-v4-cl5.md` (et son compagnon `.sha256`, écrit à
la fin), sur le modèle des contre-lectures 3 et 4 (fichiers n° 4 de la liste) : en-tête (texte relu et son empreinte
vérifiée sur disque avant lecture ; qui tu es ; heure de début et heure d'écriture, **lues sur `date -u` au moment où tu
les écris — n'écris jamais une heure de fin d'avance**) ; ce que tu as lu, pas lu, exécuté ; **verdict** (« scellable »,
« scellable après corrections mineures », « scellable après corrections », ou « non scellable ») ; tes constats numérotés
**P4C5-01, …**, chacun qualifié (majeur, mineur, remarque, conforme), avec le fait (fichier, lignes) et la correction
proposée ; une section « conforme ».

## Fichiers à lire (chemins absolus ; tout est sur disque, aucun `git` n'est nécessaire)

Abréviations : `PR` = `/home/claude/pilote4/essaim-m3-refonte-v1/prereg` ; `PC` = `PR/pieces-pilote4-gemini` ;
`R` = `/home/claude/pilote4/essaim-m3-refonte-v1` ; `O` = `PC/objet-v6-2-1-v1`.

1. `PR/pilote4-gemini-organisme-v4.md` — **le texte relu** (empreinte attendue : `efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e`). Les marqueurs
   `[[CONTRE_LECTURE]]`, `[[CONTRE_LECTURE_DETAIL]]`, `<<ENTROPIE>>`, `<<GRAINE_V53>>`, `<<GRAINE_V6X>>` et
   `<<EMPREINTE_PIECES>>` restent à dessein (les deux premiers remplis à la main avant le script de scellement, les
   autres par le script) ; la ligne de GO porte `<empreinte du texte scellé>` à dessein, et les lignes de dépense
   `<date du jour>`, `<16 premiers caractères>` et `<nom de la course>`.
2. `PR/pilote4-gemini-organisme-v3.md` — **P4v3**, scellé (`de7a5559…`) : lis-le en entier, pour juger si le texte
   différentiel transpose ou remplace **tout** ce que P4v3 dit de la v6.1 et tout ce qui dépend de l'ordre des courses.
3. Objet : `O/` — `livraison-gemini-v6-2-recue-2026-10-25-2309-v1.txt` (rapport de livraison de Gemini) ;
   `verification-v6-2-3bbb78c-v1/LISEZMOI-v1.md` (vérification de la v6.2 de Gemini) ; `CORRECTIONS-v5-copie-du-commit-7ea3270.md`
   (corrections C-14 à C-17) ; `diff-organisme-3bbb78c-vers-7ea3270-v1.txt` (l'écart de l'organisme) ;
   `essais-corrections-v1/` (journaux des essais en isolation et des témoins, dans l'ordre a, b, c, d) ;
   `verification-v6-2-1-7ea3270-v1/LISEZMOI-v1.md` (vérification de la v6.2.1 par un sous-agent neuf) ;
   `comparaison-lignes-v61-v621-v1/` (les lignes de code que P4v3 cite pour la v6.1, comparées à celles de la v6.2.1) ;
   `mots-de-lazar-2026-10-25-26-v2.md` (les décisions de Lazar, verbatim, et les mots que le registre de session-depot
   recopie ; la v1 en est le début). L'organisme extrait du commit `7ea3270` :
   `/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/extraction-v621-7ea32705c5437d91ed071dd95fb3209bb0b0035e/organisme/`
   celui de `3bbb78c` : `/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/organisme-v62-3bbb78c/organisme/`
   et celui de la v6.1 `a9d8eb5` : `/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/organisme-v61-a9d8eb5/organisme/`
   (lecture seule ; **n'exécute jamais leur code** hors de ce que le § Interdits permet).
4. Contre-lectures précédentes : `PR/contre-lectures/pilote4-gemini-organisme-v3-cl3.md` et `-v3-cl4.md` (modèles, et
   ce qu'elles ont vérifié).
5. Lanceurs (dans `PC`) : `lancer_pilote4_gemini_v6.sh` (le dernier essayé sous P4v3), puis `…_v7.sh`, `…_v8.sh`,
   `…_v9.sh`, `…_v10.sh` (**le lanceur de ce texte**), leurs scripts `deriver_lanceur_pilote4_v7.py` à `_v10.py` et leurs
   écarts `diff-lanceur-pilote4-v6-vers-v7.txt` à `-v9-vers-v10.txt`.
6. Batteries (dans `PC`) : `essais_lanceur_pilote4_v8.sh`, puis `…_v9.sh` à `…_v12.sh` (**la batterie de ce texte**) et
   leurs dérivations `deriver_essais_pilote4_v9.py` à `_v12.py` ; journaux `essais-lanceur-pilote4-v13.log` et
   `.heures.txt` (série v13, sur la v12) ; relevé `releves-serie-v13-v1/` (script et sortie `releve-serie-v13-v1.txt`) ; pour comparer, `essais-lanceur-pilote4-v9.log`.
7. Scellement : `PC/sceller_pilote4_v3.py`, `PC/sceller_pilote4_v4.py`, `PC/deriver_scellement_pilote4_v4.py`,
   `PC/essais_scellement_pilote4_v4.sh` et ses journaux ; `PC/verifier_scellement_pilote4_v2.py`.
8. `PC/EMPREINTES-pieces-pilote4-v6.txt` (`d010123d9fe3bc923611a691ce27b8b169850942dcb35fb42cc41ee9d996ac0c`, 502 entrées,
   et son compagnon) : `sha256sum -c` depuis `PC`.
9. Au besoin : le noyau `R/essaim_m3/noyau/boucle.py`, `R/essaim_m3/noyau/contrat.py` ; les dossiers de cas de la série
   v13 (simulations, permis ; lecture seule) :
   `/tmp/claude-0/-home-claude/3a0c40e9-6f33-50d1-9582-1a2bbc0655c7/scratchpad/pilote4/serie-v13/essais/`.

## Ce que tu vérifies, au moins

1. **Le texte différentiel est complet** : chaque énoncé de P4v3 propre à la v6.1 (objet, lignes de code citées, canal (d),
   bornes des rondes, devis, liste d'arrêt, essais, cas sains) et chaque règle qui dépend de l'ordre des courses (porte,
   lignes de dépense, ligne de GO, repli « seule la v5.3 part », moment de lecture, critère 3, liste d'arrêt) est transposé
   ou remplacé, sans contradiction.
2. **L'objet** : les faits du § Objet contre les deux vérifications, `CORRECTIONS-v5`, l'écart et le code (lignes, au
   moins par sondage) ; les corrections font-elles ce qu'elles disent, et rien d'autre ? L'essai hérité adapté est-il
   justifié et non affaibli au-delà de ce qu'exige C-15 ? Les choix gardés (C-14, C-16) sont-ils dits avec leurs raisons ?
3. **Les dérivations** : redérive dans ton dossier les lanceurs v7 à v10 (chacun du précédent), les batteries v9 à v12, le
   script de scellement v4 et le relevé v3, et compare octet pour octet ; lis les écarts : l'inversion de l'ordre (lanceur
   v9, batterie v11) est-elle juste et complète (porte, graine de la précédente, ligne de dépense, cas réels, segments) ?
4. **La série v13** : complète et conforme ; les nombres du § Essais (cas, heures, appels par unité, reprises) sont-ils
   ceux du journal et du relevé ?
5. **Le plan** : la ligne de GO et les lignes de dépense passent-elles les `grep` du lanceur v10 ; « rien ne part » si le
   mot de Lazar ne nomme pas la v6.2.1 est-il vrai du code ? Le scellement acceptera-t-il le texte (une seule ligne
   d'entropie, deux lignes de graine, marqueurs attendus) ?
6. **Les décisions de Lazar** (pièce verbatim) : sont-elles rendues fidèlement, et le texte tient-il dans chaque issue de
   la décision encore ouverte (`[[LECTURE_POUR_B]]` : le moment où les scores de ce pilote peuvent être lus pour écrire les
   hypothèses d'un pilote décisif suivant) ? La « règle de ce texte » qui y est écrite (l'option (1) par défaut ; (2) ou
   (2') sur un mot de Lazar inscrit avant la fin de la dernière course) tient-elle avec R1 et avec P4v3 ? Le texte et
   la ligne de GO sont-ils cohérents avec les mots R-445 et R-448 (objets, bornes, forme, « exactement sous la forme
   qu'il donne ») ?

## Interdits (sans exception)

- N'ouvre, ne lis, ne hache **aucun** fichier dont le nom finit par `-cle.json` ou `-secret.json` ; aucun dossier
  `donnees/`, `runs/`, `diag/` ; aucun fichier `P3-consignes-v1.md` ni `textes-actions-…` ; aucune archive `ferme.tar.gz` ;
  aucun fichier `reponse-question*`, `journal-appels*` ou `extrait-mecanique*` **des pilotes réels** (ceux des simulations
  sont permis).
- Aucun `git`, aucun sous-agent, aucune recherche récursive dans les dépôts (lis les fichiers nommés ; `grep` sur un
  fichier nommé, `ls` d'un dossier nommé et `sha256sum -c` sur un fichier d'empreintes sont permis).
- N'écris que sous `/var/tmp/contre-lecture-pilote4-v5/` (crée-le ; tes copies d'essai dans des sous-dossiers neufs).
- N'exécute ni un lanceur, ni une batterie, ni le code d'un organisme. Tu peux exécuter : `sha256sum`, `diff`, les scripts
  de dérivation (sorties dans ton dossier), ton propre code en lecture seule (analyse de l'arbre syntaxique comprise).
- N'affiche, n'écris, ne demande jamais une clé ou un jeton. Ne lis aucun score.

À la fin, réponds par trois lignes : le verdict, le nombre de constats par qualité, le chemin et l'empreinte du rapport.
