Tu es un contre-lecteur neuf (règle R2 du programme de Lazar : chaque préenregistrement est contre-lu par un sous-agent qui
ne l'a pas écrit). Tu n'as écrit ni ce texte, ni ses pièces, ni les contre-lectures 5 et 6. Langue : français, sans
acronymes (développe les termes). Tu es la **contre-lecture 7, courte**, du préenregistrement du quatrième pilote
descriptif `pilote4-gemini-organisme-v4.md` : elle ne relit que **l'écart** entre la version lue par la contre-lecture 6
et la version à sceller, c'est-à-dire le traitement des constats de la contre-lecture 6 par l'instance nouvelle de
conv-audit. Environ 25 minutes.

## Ce qu'on attend de toi

Un rapport `/var/tmp/contre-lecture-pilote4-v7/pilote4-gemini-organisme-v4-cl7.md` (et son compagnon `.sha256`, au format
« empreinte, deux espaces, nom nu », écrit à la fin) : en-tête (textes relus et leurs empreintes vérifiées sur disque par
`sha256sum` avant lecture ; qui tu es ; heure de début et heure d'écriture, **lues sur `date -u` au moment où tu les
écris — n'écris jamais une heure de fin d'avance**) ; ce que tu as lu ; **verdict** (« scellable », « scellable après
corrections mineures », « scellable après corrections », « non scellable ») ; constats numérotés **P4C7-01, …**,
qualifiés (majeur, mineur, remarque, conforme), avec le fait (fichier, lignes) et la correction proposée, rédigée.

## Fichiers à lire (chemins absolus ; aucun `git`)

`PR` = `/home/claude/pilote4/essaim-m3-refonte-v1/prereg` ; `PC` = `PR/pieces-pilote4-gemini`.

1. La version lue par la contre-lecture 6 : `PC/contre-lecture-6-v1/pilote4-gemini-organisme-v4-lu-par-cl6-51752266.md`
   (empreinte `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34`, 469 lignes).
2. La version à sceller : `PR/pilote4-gemini-organisme-v4.md` (empreinte attendue
   `4c20ca317b496feb2893cb4a6f7ff2403a394d945dd5295e6639c2c743a697d8`, 576 lignes) ; sa copie
   `PC/contre-lecture-7-v1/pilote4-gemini-organisme-v4-lu-par-cl7-4c20ca31.md` a la même empreinte. Fais toi-même le
   `diff` des deux ; un `diff -u` est aussi versé : `PC/traitement-cl6-v1/diff-texte-51752266-vers-4c20ca31-v1.txt`.
3. Le rapport de la contre-lecture 6 : `PR/contre-lectures/pilote4-gemini-organisme-v4-cl6.md`
   (`35fe0067ec7477c2e6e82500321bbe23a0683e20f2bbb6de36c55d4103dc7559`) : ses constats P4C6-01 à P4C6-09 et les
   corrections qu'il rédige ; et la façon dont le texte dit traiter chacun (§ Contre-lecture, paragraphe
   « Contre-lecture 6 », et la note `PC/traitement-cl6-v1/LISEZMOI-traitement-cl6-v1.md`).
4. Le relevé verbatim des mots de Lazar, v6 : `PC/objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v6.md` (`2e6387b9…`) ; la v5
   (`mots-de-lazar-2026-10-25-26-v5.md`, `c5fe20921285a7992f4236c867e981b13b7a55c47122be1afe16ad989a4c32c8`) ; le script
   qui a construit la v6 : `PC/traitement-cl6-v1/outils/faire_releve_v6_v1.py` (à lire, pas à exécuter). Les trois messages
   ajoutés viennent de la passation `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/passation-conv-audit/passation-conv-audit-2026-10-26-v1.md`
   (`e4f47910bdc3b2f38ebb816387bacd20499740f34642dffa69fa5241d5322779`, § 5, « Messages de Lazar après le relevé v5 ») ; les
   lignes R-473 à R-478 du registre : `/home/claude/controle-ia-travail/registres/decisions.md` (lis seulement ces lignes,
   par `grep`), et la ligne GO-2026-10-26-01 de `/home/claude/controle-ia-travail/registres/go.md` (par `grep`).
5. La liste des pièces v8 : `PC/EMPREINTES-pieces-pilote4-v8.txt` (`b2a9ea387ef97e812abaee96c0bcabe0c2f54f7cbe98473aa2ae70e9873d79bc`,
   646 entrées) et la v7 (`PC/EMPREINTES-pieces-pilote4-v7.txt`, `220768458e7a6778426b37f0b39aeabdfb2bebd4e385a36d31ede5e364573550`,
   621 entrées).
6. Au besoin : `PR/pilote4-gemini-organisme-v3.md` (« P4v3 » : § Plan, points 3 et 4 (l. 386–420), § Hypothèse (l. 340–343),
   liste d'arrêt, dernière ligne (l. 460)) ; `PR/pilote2-gemini-organisme-v5-2-v2.md` (« T2 », critères gelés l. 518–520) ;
   la règle de la banque `/home/claude/banque-v2/essaim-m3-refonte-v1/banque/LISEZMOI-v9.md`, § 4, point 3 (références
   0,75 et 0,6944 ; 0,8056 et 0,8333) — **dans ce dossier, ne lis que ce fichier** ; le script de scellement
   `PC/sceller_pilote4_v4.py` ; le lanceur `PC/lancer_pilote4_gemini_v10.sh` (l. 495–560, ce qu'il lit du texte) ; le message
   n° 58 de session-depot `/home/claude/lecture-session-depot/brouillons/canal-reprise-releve-v1/messages/session-depot_2026-10-26_n58.md`
   (point 1 : la levée confirmée vers 01:19 UTC).

## Ce que tu vérifies

1. **Chaque constat de la contre-lecture 6 (P4C6-01 à P4C6-08) est traité comme le texte le dit**, et comme le rapport le
   demandait, ou l'écart est déclaré et justifié ; aucune correction n'introduit de contradiction avec P4v3, T2, le reste
   du texte ou les décisions de Lazar (relevé v6).
2. **Les cinq choix du point 4 bis** (P4C6-05 (a) à (e)) et le choix « verdicts des agents = pièces à part » (P4C6-01) sont
   des choix de conv-audit, non du rapport : sont-ils **calculables** à partir de ce que la liste fermée et le secret de la
   banque rendent (d'après P4v3), **cohérents** avec la règle de la banque (maximum des références) et avec les règles de
   lecture gardées, et **sans comparaison entre les deux objets** ? En particulier (a) : la combinaison des bornes de Wilson
   de chaque classe au niveau 97,5 % bilatéral par leur moyenne donne-t-elle bien une couverture d'au moins 95 % nominal
   pour l'exactitude équilibrée (borne de l'union) ? Dis si tu vois un choix meilleur, mais ne le fais pas appliquer sans
   le qualifier (mineur ou remarque).
3. **Le relevé v6 reprend la v5 mot pour mot** (`diff` : seules les trois lignes remplacées — titre, phrase d'en-tête,
   en-tête de section — sont ôtées) ; les trois messages ajoutés sont ceux de la passation, verbatim ; les lignes R-473 à
   R-478 sont rendues fidèlement au registre ; les heures de Paris et UTC sont cohérentes (Paris = UTC + 1).
3 bis. **La liste v8** passe `sha256sum -c` dans `PC` (**après** contrôle de ses noms : aucun `-cle.json`, `-secret.json`,
   `donnees/`, `runs/`, `diag/`, `ferme.tar.gz`, `reponse-question`, `P3-consignes`, `textes-actions`) ; aucune entrée de la
   v7 n'est ôtée ni changée ; les 25 entrées nouvelles sont `contre-lecture-6-v1/`, le relevé v6 et son compagnon,
   `traitement-cl6-v1/`, la liste v7 et son compagnon ; elle couvre tout ce que porte `PC` à son écriture, sauf
   elle-même, son compagnon et `contre-lecture-7-v1/` (créé après).
4. **Rien d'autre ne change** que ce que le paragraphe « Contre-lecture 6 » du § Contre-lecture et le statut annoncent :
   liste des passages modifiés.
5. **Le scellement acceptera le texte** : une seule ligne « entropie E = » (sans nombre), deux lignes « graine de la course
   … = » (celles des marqueurs), les quatre marqueurs `<<…>>` une fois chacun, aucun marqueur `[[…]]` ; la ligne de GO et
   les lignes de dépense du § Plan, point 1, sont **inchangées** depuis la version relue par la contre-lecture 6 (`diff`).
   Le paragraphe « Contre-lecture 7 » du texte dit que ta ligne y sera inscrite avant le script : ton rapport ne doit
   porter ni ligne « entropie E = », ni ligne « graine de la course … = », ni marqueur `<<…>>` ou `[[…]]`.

## Interdits (sans exception)

- N'ouvre, ne lis, ne hache aucun fichier dont le nom finit par `-cle.json` ou `-secret.json` ; aucun dossier `donnees/`,
  `runs/`, `diag/` ; aucun fichier `P3-consignes-v1.md`, `textes-actions-…`, `ferme.tar.gz`, `reponse-question*`,
  `journal-appels*`, `extrait-mecanique*` des pilotes réels. Dans `/home/claude/banque-v2/…/banque/`, seul `LISEZMOI-v9.md`.
- Aucun `git`, aucun sous-agent, aucune recherche récursive dans les dépôts ; n'écris que sous
  `/var/tmp/contre-lecture-pilote4-v7/` ; n'exécute ni lanceur, ni batterie, ni script de scellement, ni code d'un
  organisme (`diff`, `sha256sum`, `grep` sur un fichier nommé, et ton propre code en lecture seule par
  `/opt/venv-essaim-sim-v1/bin/python -I` sont permis).
- N'affiche, n'écris, ne demande jamais une clé ou un jeton. Ne lis aucun score.

À la fin, réponds par trois lignes : le verdict, le nombre de constats par qualité, le chemin et l'empreinte du rapport.
