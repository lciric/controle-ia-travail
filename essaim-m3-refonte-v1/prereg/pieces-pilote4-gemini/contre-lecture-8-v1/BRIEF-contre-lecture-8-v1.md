# Brief — contre-lecture 8 : texte v5 du pilote 4 (seconde course : la v6.2.1 sur la question S), lanceur v11, batterie v13 — v1

Écrit par la lignée conv-audit le 26 octobre 2026 à 04:43 UTC (heure lue sur `date -u`) pour un sous-agent neuf, qui n'a
écrit aucune des pièces (règle R2). Langue : français, sans acronymes. Tu lis seulement
`/var/tmp/contre-lecture-pilote4-v8/fournis/` (empreintes : `../EMPREINTES-fournis-v1.txt`) et tu écris seulement dans
`/var/tmp/contre-lecture-pilote4-v8/sortie/`. **Ton rôle est de chercher ce qui est faux, flou ou dangereux**, pas de
confirmer. Pilote de conception (R-473) : ni préenregistrement ni scellement au sens de R1 ; la relecture est gardée.

## Le fait
Mot de Lazar (R-492, 04:13 UTC) : la v5.3 ne court pas ; la seconde course du pilote 4 est le même organisme, la v6.2.1,
sur la question S (`question-S-v2.md`, `a54da93e…`, commit `4772b525`), mêmes bornes, après la course M (en cours,
dossier `pilote4-gemini-v6-2-v1-tentative2`, lanceur v10) et après un tour du collisionneur. Décisions de Lazar de 05:13
Paris (note `decision-N-taches-fraiches-et-lecture-test-final-v1.md`) : `test_final` lu une seule fois en fin de boucle.

## Ce que tu relis
1. **Le texte v5** `pilote4-gemini-organisme-v5.md` (empreinte `09227500e535cb02e18484a1566f636af3d5fafacf720c1e9e734adf1121f257`, telle qu'au moment de ce brief ; marqueurs
   `[[SERIE_V14]]`, `[[CL8]]`, `[[HASH_CL8_TEXTE]]` et `<<…>>` à ignorer : la série de la batterie n'a pas encore
   tourné — elle attend la fin de la course M — et les graines viennent après toi), différentiel sur la v4
   (`782b858c…`, fournie, qui prime avec P4v3 sur tout ce que la v5 ne dit pas). Vérifie : que chaque règle de la v4 qui
   nommait la v5.3 a un sort dans la v5 (table de correspondance, plan, liste d'arrêt) ; la ligne d'extension de GO et la
   ligne de dépense de la course S contre les `grep` du lanceur v11 (question `a54da93e`, arbre `4f13647a`, 16 premiers
   caractères du texte, banque ; dépense : nom, GO, empreintes de M `5ae4e801423bbef0`, empreintes de la course M) ; les
   deux lignes de graine (`v6-2-s` = enfant 0 de l'entropie de la v5 ; `v6-2` = 2334107546136117589, la graine de la v4,
   ligne entière) contre ce que le lanceur v11 lit (étapes 0 bis et 2) ; la copie de lancement (changement de tête après
   la fermeture de la course M) contre `PERMIS_APRES_CODE` et la porte ; le point 3 (lecture : `test_final` une fois) contre
   le point 3 de la v4 (permission, non obligation) ; « aucune comparaison entre les deux courses » contre P4C7-02 ; ce que
   la question S change ou ne change pas (servie à g001, sans effet sur le score) ; les bornes et le devis (150 USD pour les
   deux courses, marge du GO) ; le statut et « Ce qui a été lu » (aucun score).
2. **Le lanceur v11** contre la v10 (`diff-lanceur-pilote4-v10-vers-v11.txt`, `deriver_lanceur_pilote4_v11.py`, LISEZMOI
   du sous-agent qui l'a dérivé) : chaque remplacement est-il juste et suffisant ? Reste-t-il un chemin où la clé `v6-2` part
   en réel, où la question M sert à la course S, où la porte accepte une course M qui n'a pas tourné sous le v10, où la
   graine de la course M n'est pas comparée au texte ? Les variables `LANCEUR_V62_NOM` et `LANCEUR_V62_SHA` sont-elles bien
   fixées avant leur usage, dans les deux modes ? Le remplacement de `"$(basename "$0")"` dans l'appel Python ne
   casse-t-il pas l'ordre des arguments (`sys.argv[1:9]`) ? Toute ligne qui cite encore la v5.3 hors de « la v5.3 ne court
   pas ».
3. **La batterie v13** contre la v12 (`diff-essais-pilote4-v12-vers-v13.txt`, `deriver_essais_pilote4_v13.py`) : chaque cas
   de la v12 a-t-il un équivalent ; les cas ajoutés essaient-ils les gardes nouvelles sur un cas sain et sur un artefact
   (R5) ; les attentes (messages) correspondent-elles mot pour mot au lanceur v11 ; la copie « réelle » de la course M
   (`poser_v62_reel`) est-elle une imitation fidèle d'un LANCEMENT.md du v10 ; un cas peut-il passer pour une mauvaise
   raison. **N'exécute pas** la batterie ni le lanceur (`bash -n` permis).
4. **Les scripts** `sceller_pilote4_v5.py` (contre le v4 ; son journal d'essais), `verifier_scellement_pilote4_v3.py`,
   `verifier_depart_pilote4_v2.sh` (contre ce que le lanceur v11 vérifie réellement ; `python3 -I` permis sur des copies
   d'essai de ton cru, jamais sur les fichiers fournis).

## Interdits
Aucun `git`, aucun sous-agent, aucun réseau, aucune clé ; aucune exécution du lanceur, de la batterie ni du noyau ; aucun
score (il n'en existe aucun) ; aucun critère ni stratégie de classement des tâches ; tu n'écris que sous
`/var/tmp/contre-lecture-pilote4-v8/sortie/` ; heure lue sur `date -u` dans la commande même où tu l'écris.

## Ce que tu rends
`pilote4-gemini-organisme-v5-cl8.md` : constats numérotés P4C8-01, P4C8-02… (pièce et ligne ; gravité : « bloquant »,
« majeur », « mineur » ou « remarque » ; ce qui ne va pas ; correction proposée) ; verdict en une ligne : « lançable tel
quel », « lançable après corrections mineures », « non lançable » ; ce que tu n'as pas pu vérifier ; avec son compagnon
`.sha256`. À la fin, réponds en trois lignes : le verdict, les constats bloquants ou majeurs (numéros), l'empreinte du
rapport.
