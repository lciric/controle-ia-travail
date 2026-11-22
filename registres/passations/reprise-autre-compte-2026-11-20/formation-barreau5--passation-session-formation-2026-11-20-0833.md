# Passation de la session de formation du barreau 5 — 2026-11-20 08:33 UTC

Session : formation du barreau 5 (plan « sabotage ou empreinte de l'adaptateur »), rôle du point 7, premier tiret, du texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (sha256 bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935). Mandat : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/formation/mandat-session-formation-v2.md` (sha256 83e5d7f8f115f5639b9bbbaa0bc09c5362eca4461b385609d3d8ffa5732ade3e). Mère : session `session_01XJ6Mgr8BN6UanALsQatc5E`. Écrite sur le mot de Lazar R-4165 relayé par la mère à 08:31Z. Aucun score, aucune sortie de marche lue.

## Fait
- Plan de marche v1 écrit, scellé, poussé (branche `formation-b5f/plan-de-marche-v1`, commit a65febd7, `plan-de-marche-session-formation-v1.md`, sha256 fbbc219185d688f16764d04971178e9503daac0fc395c62c7d2255b942302242).
- Instance de formation 6 (familles A1 et A2, trois membres, coupure 28 USD) créée sur le mot de Lazar GO-2026-11-20-02, accord de calcul cité `GO_ID=GO-2026-11-19-86` : identifiant du loueur 61552174, étiquette `b5f-formation-v1-6`, offre 29019285 (A100 SXM4 80 Go), 1,17 USD/h stockage compris, H = 2026-11-20T01:30:16Z, run 20261120-012937-b5f-formation-6. Lancement par un fichier joueur (ligne imprimée par le lanceur copiée octet pour octet), garde de calcul vérifiée sur son texte exact ; accepté une fois par la mère.
- Étapes « B5F » vues : minuterie lancée 01:31:01Z (échéance 2026-11-21T02:27:25Z) ; dépôt au commit de course, branche de sortie libre 01:31:05Z ; essais du paquet 235 passés 01:34:48Z ; modèle au cache, début de la marche (88535 s au plus) et marche lancée 01:36:50Z. Rien depuis.
- Veille de l'instance (outil `veille_b5f.py`) relancée après chaque limite de 2 h et après deux redémarrages du conteneur ; état gardé dans `veille-6-etat.json`.
- Signal de crédit envoyé à la mère à 06:07Z (autre instance du compte, 61582969, voulue, finie vers 07:25Z) ; erratum envoyé : « environ 20 h » était la borne haute de la marche, pas une estimation.
- Bloc-notes versé (R-3661) dans `versement-bloc-notes-session-formation-v1/` (inventaire `inventaire-v1.tsv` : 31 fichiers versés, 4520 fichiers d'essais locaux dans `essais-locaux.tgz`, 12 fichiers gardés hors du dépôt parce qu'ils portent des secrets ou des données personnelles du compte : listes du loueur, profil du compte, réponse de création ; seulement nom, taille, empreinte).

## Reste
- Veiller l'instance 6 jusqu'à sa fin ; à la fin : récupérer la branche de sortie `donnees/barreau5-familles-jumelles-v1-formation-instance-6`, vérifier la preuve du versement final (ligne « versement final prouvé … au commit » et `traces-b5f/inventaire-final.json`), détruire par l'identifiant avec le lanceur (`detruire`), puis `verifier-destruction` avec le témoin 60988826.
- Les six autres instances, ordre 1, 2, 3, 4, 5, 7, seulement sur le signal de la mère (crédit rechargé) ; fin des créations 2026-11-21T07:30:16Z (H + 30 h).
- Sel, noms opaques X-01 à X-30, table et ligne `ENGAGEMENT-B5F` : seulement sur le mot exprès de la mère, avant la création de l'instance de lecture.
- Ligne `SORTIES-FORMATION-B5F` : à rédiger plus tard, une seule ligne, format à fixer.

## Réserves
- Calcul de la veille : cumul = plus grand de (heures × prix) et (baisse du crédit + recharges constatées). La baisse du crédit a compté l'autre instance (≈ +12 USD), et la recharge de 5 USD de 07:05Z a été vue comme +4,09 USD : le cumul affiché (18,54 USD à 08:29Z) surestime la dépense propre de l'instance 6 (≈ 8,2 USD). Gardé tel quel sur le mot de la mère ; risque de refus à tort de la garde vers 15:00Z, que la mère revoit.
- À la borne de la marche, la dépense propre atteindrait ≈ 28,9 USD : la garde (cumul + un quart d'heure ≥ 28 USD) refuserait vers 2026-11-21T01:11Z, avant l'échéance d'arrêt. Consigne : ne rien détruire, écrire à la mère.
- Durée réelle de la marche inconnue de cette session (aucune sortie lue) ; seule la borne est connue.
- Incident de cloisonnement local : à 08:32Z, un comptage par motif dans le bloc-notes a affiché dans la sortie d'outil de cette session la valeur d'un jeton Hugging Face, présente dans les listes d'instances du loueur. Rien n'a quitté la session ; rien de tel n'est versé. Signalé à la mère ; rotation du jeton à décider par Lazar.
- Pièce de cette session sur `main` : une seule note sans interne qui dit où est le brief (mot de la mère de 08:31Z, qui prime ici sur « rien sur `main` » du mandat).

## Prochaine action
Relancer la veille si elle s'est arrêtée (commande dans le brief), puis attendre : ligne « B5F » neuve → l'écrire à la mère ; fin de marche → versement prouvé → destruction par l'identifiant → vérification ; refus de la garde, ARRÊT, SIGNAL, instance absente → ne rien détruire, écrire à la mère.

## Programmes et instances en cours (08:33Z)
| Quoi | Identifiant | État | Échéance |
|---|---|---|---|
| Instance de formation 6 | 61552174 (`b5f-formation-v1-6`) | en marche, 1,17 USD/h | arrêt de la marche 2026-11-21T02:12:25Z ; minuterie 02:27:25Z (détruit si versement prouvé, sinon « stopped » et SIGNAL) |
| Veille de cette session | tâche de fond locale, pas de 600 s | en marche, limite 2 h | — |
| Machines intouchables (arrêtées) | 58936096, 58936099, 58936100 | exited | ne jamais toucher |
| Témoin de destruction | 60988826 | exited | ne pas détruire |

Crédit 6,41 USD à 08:29Z ; recharge automatique de 5 USD sous 5 USD (mère, 06:08Z) ; Lazar accepte davantage après 08:00Z. Instances à créer avant 2026-11-21T07:30:16Z : 1, 2, 3, 4, 5, 7, sur signal de la mère.

## Pour reprendre ou récupérer
- Branche : `formation-b5f/plan-de-marche-v1` ; bloc-notes versé dans `versement-bloc-notes-session-formation-v1/` (outils `choisir_offre_b5f.py`, `veille_b5f.py`, `essai_garde3.py`, fichiers de la création de l'instance 6, état et journal de la veille).
- Le brief de lancement de la session qui succède : `brief-lancement-session-formation-v1.md`, même dossier.
