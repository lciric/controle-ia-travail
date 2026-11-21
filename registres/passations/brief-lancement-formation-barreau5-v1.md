# Brief de lancement — session de formation du barreau 5, successeure (v1 du 2026-11-21)

Écrit le 2026-11-21 par la session de formation sortante (`session_01QPDgKjCQYmTHUEjN63ThC8`), sur la demande de la mère. Tu reprends le rôle du point 7, premier tiret, du texte scellé du barreau 5. Dépôt `lciric/controle-ia-travail`. Langue : français. **Aucun score, aucune sortie de marche, jamais.**

## 0. Où en est le rôle
Toutes les marches de la formation sont finies, versées et prouvées ; toutes leurs instances sont détruites. **Aucune instance ne tourne.** Il reste : la ligne `SORTIES-FORMATION-B5F` (rédigée, contrôlée, envoyée à la mère, inscription par elle), puis, sur le mot exprès de la mère seulement, sel, table et `ENGAGEMENT-B5F` ; puis la relecture et la répétition générale. Voir la passation `registres/passations/2026-11-21-1453-formation-barreau5.md`.

## 1. Lis d'abord, dans cet ordre (branche `formation-b5f/plan-de-marche-v1` sauf mention)
1. `CLAUDE.md` (routine de reprise ; interdits ; « Qui conçoit »).
2. Le mandat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/mandat-session-formation-v2.md` (sha256 83e5d7f8f115f5639b9bbbaa0bc09c5362eca4461b385609d3d8ffa5732ade3e).
3. Du texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935), les seules sections permises par le mandat : « Objet et portée » (paragraphe « Périmètre »), « Plan d'analyse » points 1 à 7, 14 et 17 (point 3 à partir de son premier tiret), « Liste d'arrêt », « Données gardées », « Calcul et dépense », « Calendrier et chemin critique », « Lignes de registre », « Code neuf ». Rien d'autre.
4. Le plan de marche : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/plan-de-marche-session-formation-v1.md` (sha256 fbbc219185d688f16764d04971178e9503daac0fc395c62c7d2255b942302242).
5. Les additifs scellés : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/relance-six-instances-v1/additif-1-relance-six-instances-v3.md` (20e862a3…), `additif-2-recreation-relances-v6.md` (3562d5a1…), `additif-3-branches-de-traces-seules-v2.md` (d4f9c24c…) ; et l'additif 1 au devis : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/scellement-additif-1-v2-devis-v1.md` (sur main ; GO-2026-11-21-42 et -45).
6. La passation `registres/passations/2026-11-21-1453-formation-barreau5.md`, puis la dernière passation détaillée `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/passation-session-formation-2026-11-21-1455.md`, et la pièce `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/sorties-formation-b5f-v1.md` (sha256 41e51f99…).
7. Le registre propre `registres/barreau5-familles-jumelles-v1.md` sur main, et la règle du canal `registres/essaim/regle-du-canal-essaim-v1.md` sur main.
Vérifie chaque empreinte (`.sha256` compagnon) avant de t'en servir.

## 2. Cloisonnement (à la lettre)
- Rien de la formation vers la mère ni vers `main`, hors pièces sans interne. À la mère : étapes « B5F », ARRÊT, SIGNAL, dépenses, identifiants d'instance, chemins et empreintes. Jamais : sel, table, lien entre un nom opaque et une famille ou un membre, score, épisode, coût d'action, mesure tirée des sorties.
- Ne lis aucun fichier de `diag/` hors de tes propres runs, aucun score, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis, aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». N'ouvre pas les sorties des marches de la formation (`donnees/<marche>/`, `diag/<marche>/`, `runs/<marche>/`) : tu ne manipules que leurs noms, tailles, empreintes et commits.
- Clés par leur nom seulement (`VAST_API_KEY`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2`), jamais affichées ni écrites. Les listes d'instances du loueur (`show instances --raw`), le profil du compte et les journaux d'instance portent des jetons ou des données personnelles : ne les affiche pas, ne les verse pas, ne les fouille pas par motif affiché (pas de `grep -o`) ; lis-en seulement des champs nommés (`outils/lire_champ.py` : id, label, cur_state).
- N'écris dans aucun registre, ni dans tes messages à la mère, l'identifiant de l'accord d'écart à R9 cité au point « Ton rôle » du mandat (jusqu'à nouvel ordre). Aucun sel ni table sans le mot exprès de la mère.
- Arrêts et destructions par l'identifiant seulement (R10), et seulement des instances étiquetées `b5f-formation-v1-<n>`. Machines 58936096, 58936099, 58936100 intouchables ; 60988826 ne se détruit pas (témoin). Aucune commande d'arrêt ou de recherche de processus par motif.
- Au premier refus d'outil : arrête-toi et écris à la mère. Au moindre doute : arrête sans détruire et écris-lui. Ne désactive jamais la vérification TLS. Rien sous `/root/.claude/`.
- Canal : `send_message` vers la mère quand il passe ; sinon un fichier scellé dans `registres/essaim/vers-mere/AAAA-MM-JJ-HHMM-formation-b5f.md` sur ta branche (règle du canal sur main). Tu ne lis que `registres/essaim/vers-formation-b5f/`. Aucun message direct à une autre session de rôle cloisonné (par exemple l'attaquant informé) : tout passe par la mère.

## 3. Branches et commits
- Ta branche : `formation-b5f/plan-de-marche-v1` (passations, pièces, versements du bloc-notes, canal). Rien sur `main`.
- Code de course : branche `course/barreau5-formation-v1` ; commit de course des relances 4bdf0d22e4246b4fe431bd8754e26fea4ccd037f (lanceur `scripts/lancer_b5f_formation_v1.sh`, sous-commandes `detruire`, `verifier-destruction`, `depense`, `relance`) ; code des relances d116bf78bb2084b2d4f406535a6c6f0a23179efe ; code des premières marches ef80086821db08ffab42e23310a0b880ec72b9a4 ; code de lecture figé c76e79169eee337ce66c7d88f62d039e853eebfc.
- Branches de sortie : `donnees/barreau5-familles-jumelles-v1-formation-instance-<k>` pour k = 1-x1, 2-x1, 3-x1, 4-x1, 5-x1, 6, 7-x1 (commits prouvés dans la pièce des sorties). Branches de traces : `traces/barreau5-relance-<1|2|3|4>-premiere-tentative`, jamais réunies à la formation. Après une suppression puis recréation d'une branche, toute référence locale se rafraîchit par un fetch forcé (`+refs/heads/…:refs/remotes/origin/…`).

## 4. Accords
- Calcul : `GO_ID=GO-2026-11-19-86` (plafond commun 200 USD, coupures du devis scellé dc886195… : relecture 21 USD, répétition 8 USD ; échéance 2026-11-30), cité dans toute commande payante (garde `.claude/hooks/garde_calcul.py`).
- Relances et recréations : GO-2026-11-20-51, -59, -60 ; GO-2026-11-21-01 ; GO-2026-11-21-03. Registre propre, voie (c) : GO-2026-11-21-47 (toute clé inconnue du code figé s'écrit sous la table, sans barre de tête ; avant toute ligne de table, faire lire le registre candidat par le lecteur figé). Additif 1 au devis : GO-2026-11-21-42 et -45.
- Lazar a donné son « go » pour que la session de formation écrive à la mère sans demander à chaque fois (21 novembre).

## 5. Mise en place
- Deux environnements Python 3.11 : (a) `requirements-cpu.txt` du dépôt → `PYTHON_B5F` ; (b) `vastai==1.11.2` seul. Dans un conteneur à mandataire, remplace le `cacert.pem` de certifi de (b) par le paquet d'autorités du mandataire (garde l'original). Jamais `--insecure`.
- Outils : les plus récents sont dans `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/versement-bloc-notes-session-formation-v10/outils/` (copie complète) ; corrige la variable `S` en tête de chaque outil. Arbres utiles : un arbre détaché au commit de course 4bdf0d22… (lanceur), une extraction du code de lecture figé (`git archive` de c76e7916…), pour `controler_registre_candidat_v1.py REGISTRE_CANDIDAT(chemin absolu) ARBRE_COURSE ARBRE_LECTURE`.
- Destruction après une fin : commit prouvé lu dans la ligne « versement final prouvé … au commit » du journal (`vastai logs ID`, seule cette ligne, par programme) ; `traces-b5f/inventaire-final.json` et son `.sha256` extraits au commit ; `GO_ID=GO-2026-11-19-86 bash scripts/lancer_b5f_formation_v1.sh detruire RACINE ID N LISTE.json INVENTAIRE.json COMMIT` ; ligne imprimée mise dans un joueur, éprouvée par `essai_garde3.py`, jouée ; puis `verifier-destruction LISTE_NEUVE.json ID 60988826`.

## 6. Prochaine action exacte
1. Routine de reprise de `CLAUDE.md` ; inventaire des instances du loueur par identifiant et étiquette seulement : aucune `b5f-formation-v1-<n>` ne doit exister (sinon, n'y touche pas et écris à la mère).
2. Relève `registres/essaim/vers-formation-b5f/` sur main et tes messages ; écris à la mère que tu reprends le rôle.
3. Selon sa réponse : ajuste la forme de `SORTIES-FORMATION-B5F` (contrôle par le lecteur figé avant toute ligne de table) ; ne fais sel, table et `ENGAGEMENT-B5F` que sur son mot exprès.
