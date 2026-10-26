Tu es un contre-lecteur neuf (règle R2 du programme de Lazar : chaque préenregistrement est contre-lu par un sous-agent qui
ne l'a pas écrit). Tu n'as écrit ni ce texte, ni ses pièces, ni la contre-lecture 5. Langue : français, sans acronymes
(développe les termes). Tu es la **contre-lecture 6, courte**, du préenregistrement du quatrième pilote descriptif
`pilote4-gemini-organisme-v4.md` : elle ne relit que **l'écart** entre la version lue par la contre-lecture 5 et la
version à sceller. Environ 25 minutes.

## Ce qu'on attend de toi

Un rapport `/var/tmp/contre-lecture-pilote4-v6/pilote4-gemini-organisme-v4-cl6.md` (et son compagnon `.sha256`, écrit à la
fin) : en-tête (textes relus et leurs empreintes vérifiées sur disque avant lecture ; qui tu es ; heure de début et heure
d'écriture, **lues sur `date -u` au moment où tu les écris — n'écris jamais une heure de fin d'avance**) ; ce que tu as lu ;
**verdict** (« scellable », « scellable après corrections mineures », « scellable après corrections », « non scellable ») ;
constats numérotés **P4C6-01, …**, qualifiés (majeur, mineur, remarque, conforme), avec le fait (fichier, lignes) et la
correction proposée.

## Fichiers à lire (chemins absolus ; aucun `git`)

`PR` = `/home/claude/pilote4/essaim-m3-refonte-v1/prereg` ; `PC` = `PR/pieces-pilote4-gemini`.

1. La version lue par la contre-lecture 5 : `PC/contre-lecture-5-v1/pilote4-gemini-organisme-v4-lu-par-cl5-efb13feb.md` (empreinte `efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e`).
2. La version à sceller : `PR/pilote4-gemini-organisme-v4.md` (empreinte attendue `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34`). Fais toi-même le `diff`
   des deux.
3. Le rapport de la contre-lecture 5 : `PR/contre-lectures/pilote4-gemini-organisme-v4-cl5.md` (`914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240`), et la façon dont
   le texte dit traiter chacun de ses constats (§ Contre-lecture du texte à sceller).
4. Le relevé verbatim des mots de Lazar : `PC/objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md` (lignes de 01:37 à 02:17
   surtout, et la section des mots dans la session de session-depot, R-466 à R-472) ; la synthèse du collisionneur qu'ils citent :
   `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/synthese-collisionneur-lecture-pilote-conv-audit-v1.md`
   (`a8e1ed64…`).
5. Au besoin : `PR/pilote4-gemini-organisme-v3.md` (« P4v3 », § Plan, point 3 : moment de lecture) ; le lanceur
   `PC/lancer_pilote4_gemini_v10.sh` ; le script de scellement `PC/sceller_pilote4_v4.py`.

## Ce que tu vérifies

1. Chaque constat de la contre-lecture 5 est corrigé comme le texte le dit, ou son refus est justifié ; aucune correction
   n'introduit de contradiction.
2. **Les décisions de Lazar de 01:48 à 02:17 Paris** (§ Décisions du texte, relevé v5) sont rendues fidèlement et sans
   contradiction interne : 01:48 et 01:52 — (3+), puis la banque v6 pour (b) : les hypothèses de (b) s'écrivent sans aucun
   score de ce pilote, aucune course de ce pilote n'est versée dans (b), les options (2) et (2') n'existent plus ; 01:56 —
   pilote de conception : préenregistrement et scellement levés pour lui, relecture gardée, scores lisibles **dès la fin de
   chaque course** (jamais pendant), confirmations sur la banque v6 ; ce qui remplace la fermeture « pour tout usage » de
   01:48 et le point 3 de P4v3 (le texte doit le dire sans se contredire) ; 01:54 — lecture contre le bruit, point 4 bis
   (vérifie que ce qu'il promet est calculable à partir de ce que la liste fermée et l'extrait rendent, d'après P4v3, et
   qu'il ne compare jamais les deux objets) ; 02:05 — graines de plus : décision pendante, une course par objet pour ce
   texte ; 02:06 à 02:17 — boucle extérieure retenue (agents neufs à la fin de chaque course, registre d'hypothèses avant
   tout score, relance sur le mot de Lazar), boucle intérieure tranchée chez session-depot (R-471) : le texte doit n'en
   dépendre en rien (ses courses partent telles quelles, noyau inchangé). Le texte tient-il avec P4v3 et avec lui-même ?
3. **Rien d'autre ne change** que ce que l'écart annonce : liste des passages modifiés.
3 bis. **Les pièces annoncées existent** : `PC/EMPREINTES-pieces-pilote4-v7.txt` (`220768458e7a6778…`, 621 entrées) passe
   `sha256sum -c` dans `PC` ; il couvre `contre-lecture-5-v1/`, `simulation-lanceur-v10/`, `releves-serie-v11-v1/`,
   `objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v3.md` à `-v5.md` ; aucune entrée ne porte un nom en `-cle.json` ni
   `-secret.json`. Le § Contre-lecture du texte dit juste ce que contient `contre-lecture-5-v1/` (brief, rapport, relevés,
   copie du texte relu). La v5 du relevé reprend-elle la v3 (`757f30a3…`) mot pour mot (diff) ?
4. Le scellement acceptera-t-il le texte : une seule ligne « entropie E = » (sans nombre), deux lignes « graine de la course
   … = » (celles des marqueurs), les quatre marqueurs `<<…>>` une fois chacun, aucun marqueur `[[…]]` ; la ligne de GO et les
   lignes de dépense passent-elles toujours les `grep` du lanceur v10 (lignes 536 à 552) ?

## Interdits (sans exception)

- N'ouvre, ne lis, ne hache aucun fichier dont le nom finit par `-cle.json` ou `-secret.json` ; aucun dossier `donnees/`,
  `runs/`, `diag/` ; aucun fichier `P3-consignes-v1.md`, `textes-actions-…`, `ferme.tar.gz`, `reponse-question*`,
  `journal-appels*`, `extrait-mecanique*` des pilotes réels.
- Aucun `git`, aucun sous-agent, aucune recherche récursive dans les dépôts ; n'écris que sous
  `/var/tmp/contre-lecture-pilote4-v6/` ; n'exécute ni lanceur, ni batterie, ni code d'un organisme (`diff`, `sha256sum`,
  `grep` sur un fichier nommé, et ton propre code en lecture seule par `/opt/venv-essaim-sim-v1/bin/python -I` sont permis).
- N'affiche, n'écris, ne demande jamais une clé ou un jeton. Ne lis aucun score.

À la fin, réponds par trois lignes : le verdict, le nombre de constats par qualité, le chemin et l'empreinte du rapport.
