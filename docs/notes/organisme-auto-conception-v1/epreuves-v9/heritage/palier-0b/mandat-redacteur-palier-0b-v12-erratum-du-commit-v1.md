VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement du palier 0b, version 12 (erratum du commit après le code v5) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-25 et les décisions de la mère R-4285 (13:53Z) : code v5 versé sur `main` au commit `e308b84d68a85416fab1a80b0c116858d24b85a5` ; décisions sur les silences n° 8, 14, 15, 16 ; ajouts et précisions retenus. Pièce décisive (classe A) : contre-lecture par un autre modèle, vérification des corrections par le même, scellement par la mère ; ensuite le GO de Lazar sur le palier et la pièce d'autorisation écrite par la mère.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement du palier 0b, ni aucun code, ni aucune vérification. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- La v11 : `P/preenregistrement-heritage-palier-0b-etage-processeur-v11.md` (`9faf31a3…`) ; son contrôle `P/controle-v11/controle-differentiel-palier-0b-v10-v11-v1.md` (`88c37d86…`, § 4 réserve 7, § 5 NE-3 et NE-4).
- Le rapport du code v5 : `P/code-v5/rapport-developpeur-code-palier-0b-v5.md` (`a2966a3c…`) : **§ 2 (les seize silences), § 6 (la liste de l'erratum, neuf points), § 7 (remarques), § 11 (table des empreintes)** ; la table extraite `P/table-empreintes-code-v5.txt` (`56bddae7…`).
- La vérification du code v5 : `P/verification-code-palier-0b-v5-v1.md` (`0e2c46bb…`), « Conforme » : silences, liste de l'erratum, ajouts facultatifs, précisions.
- Sur `main` (après `git -C /home/user/controle-ia-travail fetch origin main`) : `registres/go.md`, GO-2026-11-20-25 ; `registres/decisions.md`, R-4285 et les décisions qu'elle cite, **à la lettre** ; le commit `e308b84d68a85416fab1a80b0c116858d24b85a5` (vérifie qu'il est ancêtre de `origin/main` par `git merge-base --is-ancestor`, et que le rapport du code v5 y a la même empreinte).

## Ce que la v12 porte, et rien d'autre

Sous le nom neuf `preenregistrement-heritage-palier-0b-etage-processeur-v12.md`, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), un JSON écrit avec l'outil d'écriture de fichiers ; chaque ancre comptée par `grep -c -F -e` avant l'appel (règle R-4067) :

1. **Les neuf points du § 6 du rapport du code v5**, à la lettre, avec le commit **`e308b84d68a85416fab1a80b0c116858d24b85a5` de `main`** (jamais un commit de branche) à la ligne « Commit du code d'analyse », et la table des 58 empreintes du § 11 dans le premier bloc qui la suit, dans la forme exacte que le verrou lit (silence n° 4).
2. **Les deux ajouts de la vérification** : (a) l'erratum remplace la ligne « Commit du code d'analyse » et son premier bloc, et aucune autre ligne du texte ne commence par ce préfixe (contrôle par `grep -c -F -e` écrit au rapport) ; (b) il nomme la clé `non_departagees_sans_mention`, la valeur nulle de `seuil_d_arret` pour le contenu et les réunis, et les clés rendues par `lancer_etape_4`.
3. **Les trois précisions de la vérification** : n° 2 (la lecture de l'heure ne contrôle pas le jour de la semaine) ; n° 7 (une graine décisive dérivée directement par `Graines.g`, hors `lancer_famille`, n'est pas revérifiée par le verrou) ; n° 13 (la garde 27 compare l'identité d'objet de la source).
4. **Les décisions de la mère (R-4285)** : n° 8 — le champ commit du manifeste est comparé par la mère, à la main, à la ligne « Commit du code d'analyse » de la pièce d'autorisation, au contrôle du manifeste, comme pour la portée 200 ; n° 14 — la racine et le texte présentés des étapes 8 et 9 sont fixés dans la pièce d'autorisation de ces étapes ; n° 15 — la mère contrôle « sur main » (`git merge-base --is-ancestor`) et l'écrit dans la pièce d'autorisation ; n° 16 — reste en remarque (couches non décisives non verrouillées).
5. **Tenue** : statut, ligne de version, section « Contre-lecture » (contrôle de la v11 fait, « Conforme » ; code v5 vérifié « Conforme », chemin et empreinte), « Ordre des opérations » point 2, réserve 24 et « Ce qui demande un code v5 » qui disent encore le code à venir ; NE-4 seulement si la lettre de R-4285 ou d'une décision citée le demande, sinon en remarque.

Puis le différentiel `diff -u` v11 → v12, le compte des lignes qui commencent par « - Commit du code d'analyse : » (1 attendu), et un rapport court `rapport-redacteur-palier-0b-v12-v1.md` : remplacements, ancres comptées, tout point où la lettre ne suffit pas (en remarque, jamais tranché).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v12/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
