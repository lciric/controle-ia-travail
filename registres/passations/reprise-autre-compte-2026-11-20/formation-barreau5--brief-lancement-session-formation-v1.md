# Brief de lancement — session de formation du barreau 5, successeure (v1)

Écrit le 2026-11-20 vers 08:35 UTC par la session de formation sortante, sur le mot de Lazar R-4165. Tu reprends le rôle du point 7, premier tiret, du texte scellé du barreau 5, sur un autre compte. Langue : français. Aucun score, aucune sortie de marche, jamais.

## 1. Lis d'abord, dans cet ordre
1. `CLAUDE.md` du dépôt `lciric/controle-ia-travail` (routine de reprise ; interdits).
2. Ton mandat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/mandat-session-formation-v2.md` (sha256 83e5d7f8f115f5639b9bbbaa0bc09c5362eca4461b385609d3d8ffa5732ade3e), sur la branche `formation-b5f/plan-de-marche-v1`.
3. Du texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935), les seules sections permises par le mandat : « Objet et portée » (paragraphe « Périmètre »), « Plan d'analyse » points 1 à 7, 14 et 17 (point 3 à partir de son premier tiret), « Liste d'arrêt », « Données gardées », « Calcul et dépense », « Calendrier et chemin critique », « Lignes de registre », « Code neuf ». Rien d'autre.
4. Le plan de marche : `plan-de-marche-session-formation-v1.md` (sha256 fbbc219185d688f16764d04971178e9503daac0fc395c62c7d2255b942302242), même dossier.
5. La passation : `passation-session-formation-2026-11-20-0833.md`, même dossier ; puis l'inventaire `versement-bloc-notes-session-formation-v1/inventaire-v1.tsv`.
Vérifie chaque empreinte avant de t'en servir.

## 2. Cloisonnement
- Rien de la formation vers la mère ni vers `main`, hors pièces sans interne. À la mère : étapes « B5F », ARRÊT, SIGNAL, dépenses, identifiants d'instance, chemins et empreintes. Jamais : sel, table, lien entre un nom opaque et une famille ou un membre, score, épisode, coût d'action, mesure tirée des sorties.
- Ne lis aucun fichier de `diag/` hors de tes propres runs, aucun score, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis, aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ».
- Clés par leur nom seulement (`VAST_API_KEY`, `HF_TOKEN`, `CONTROLE_IA_GITHUB_TOKEN_2`), jamais affichées ni écrites. Attention : les listes d'instances du loueur (`show instances --raw`) et le profil du compte portent des jetons et des données personnelles ; ne les affiche pas, ne les verse pas, ne les fouille pas par motif affiché (n'utilise pas `grep -o`).
- N'écris dans aucun registre, ni dans tes lignes à la mère, l'identifiant de l'accord d'écart à R9 cité au point « Ton rôle » du mandat (jusqu'à nouvel ordre). Aucun sel ni table sans le mot exprès de la mère.
- Arrêts et destructions par l'identifiant seulement (R10), et seulement des instances étiquetées `b5f-formation-v1-<n>`. Machines 58936096, 58936099, 58936100 intouchables ; 60988826 ne se détruit pas (témoin). Aucune commande d'arrêt ou de recherche de processus par motif.
- Au premier refus d'outil : arrête-toi et écris à la mère. Au moindre doute : arrête sans détruire et écris-lui. Ne désactive jamais la vérification TLS.

## 3. Branche
Ta branche accordée : `formation-b5f/plan-de-marche-v1`. Branches de données des instances : `donnees/barreau5-familles-jumelles-v1-formation-instance-<n>`. Code de course : branche `course/barreau5-formation-v1`, commit 31fca83b0c26cd035fe9e660d123e690a41b6271 (racine des commandes du lanceur). Rien sur `main` sauf une note sans interne, si la mère le demande.

## 4. Accords en cours
- Accord de calcul de la formation : `GO_ID=GO-2026-11-19-86` (cité dans toute commande payante ; garde `.claude/hooks/garde_calcul.py`).
- Mot de Lazar de la nuit : GO-2026-11-20-02 — l'instance 6 seule, coupure 28 USD. Les autres instances attendent le signal de la mère (crédit rechargé), ordre 1, 2, 3, 4, 5, 7 ; fin des créations 2026-11-21T07:30:16Z. Plafond commun 200 USD.

## 5. Mise en place
- Deux environnements Python 3.11 : (a) `requirements-cpu.txt` du dépôt (torch compris) → `PYTHON_B5F` ; (b) `vastai==1.11.2` seul. Dans un conteneur à mandataire, le client du loueur ignore `REQUESTS_CA_BUNDLE` : remplace le `cacert.pem` de certifi de l'environnement (b) par le paquet d'autorités du mandataire (garde l'original à côté). Jamais `--insecure`.
- Outils : copie `versement-bloc-notes-session-formation-v1/outils/` dans ton bloc-notes ; corrige la variable `S` en tête de `veille_b5f.py` et le chemin de `LANCEUR` (arbre détaché au commit de course).
- Piège bash : `VAR=x cmd "$VAR"` développe `$VAR` avant l'affectation ; utilise une sous-coquille avec une affectation séparée. Pas de `python -c` en ligne pour les pièces.
- Lancement d'une création : le lanceur imprime une ligne de 35 Ko ; mets-la octet pour octet dans un fichier joueur (`export PATH=…` ; `GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` ; la ligne), vérifie la garde sur son texte exact (`essai_garde3.py`), joue `GO_ID=GO-2026-11-19-86 bash joueur.sh`, et envoie à la mère l'empreinte du joueur et de sa sortie.

## 6. Prochaine action exacte
1. Routine de reprise de `CLAUDE.md` (empreintes, état, inventaire des instances : liste par identifiant et étiquette seulement).
2. Vérifie que 61552174 (`b5f-formation-v1-6`) est « running » ; relance la veille :
   `PAS_VEILLE_S=600 $PYTHON_B5F -I outils/veille_b5f.py 61552174 6 3 2026-11-20T01:30:16Z 20.868202200856786 veille-6-etat.json veille-6.txt`
   (état de départ : copie de `versement-bloc-notes-session-formation-v1/b5f/veille-6-etat.json` ; la valeur de crédit initiale est celle du compte de l'instance, pas du tien : si ton compte de loueur diffère, le cumul par la baisse du crédit n'a plus de sens — dis-le à la mère avant de veiller).
3. Codes de sortie : 10 ligne d'étape → l'écrire à la mère, relancer ; 20 ARRÊT, SIGNAL ou fin → l'écrire ; à la fin, `git fetch` de la branche de sortie, preuve (« versement final prouvé … au commit » et `traces-b5f/inventaire-final.json` copié avec son `.sha256`), puis `GO_ID=GO-2026-11-19-86 bash scripts/lancer_b5f_formation_v1.sh detruire RACINE 61552174 6 LISTE.json INVENTAIRE.json COMMIT`, ligne de destruction jouée par l'identifiant, puis `verifier-destruction LISTE_NEUVE.json 61552174 60988826` ; 30 refus de la garde, 40 instance absente, 50 erreurs du loueur → ne rien détruire, écrire à la mère.
4. Sans versement prouvé : rien de détruit ; la minuterie de l'instance l'arrête à 2026-11-21T02:27:25Z et écrit un SIGNAL ; écris à la mère.
