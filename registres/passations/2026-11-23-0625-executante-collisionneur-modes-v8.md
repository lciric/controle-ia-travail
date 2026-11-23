# Passation — exécutante du service de la question v8 au collisionneur — 2026-11-23 06:25 UTC

Session : session_013QMayoAh9DWhjuW2ivm76J (fille de la mère session_013QMayjbmQUdDuDs2S3i3XD). Écrite sur GO-2026-11-23-09. Classe C.

## Mandat
Servir une fois la question v8 servie v2 (f3f47c08…) au collisionneur, étage III, selon le devis v3 (55283f60…), accords GO-2026-11-23-03, -06, -07, plafond 26 USD ; verser les sorties scellées sur cette branche `service/collisionneur-modes-v8-sorties-v1` (jamais fusionnée sur main) ; écrire la note pédagogique de fin de dossier (Markdown et PDF) sur cette branche, pour Lazar seul ; à la mère : coûts, issue, commit et inventaire, AUCUN contenu. Ajout GO-2026-11-23-08 : Fable 5.2 et 5.1 par l'interface payante, plafond 20 USD.
Cloisonnement : ne lire aucune branche coffre/*, verdict/*, calcul/*, lecture/* ; ne pas lire la porte de tri v6.

## Fait
- Préalables tenus (`prealables/sortie-prealables-v2.txt`) : empreinte de la question, garde de motifs à zéro, garde de Google sans refus aux trois tours de l'étage III, réglages conformes au devis, clés présentes par leur nom.
- Engagement inscrit par la mère (R-5137 ; ajout de Fable R-5141).
- Service à cinq espèces, dossier `dossier-v8` (hors dépôt : scratchpad de la session). Moteur v8m (420394f9…) sous la voie de l'abonnement v6 (d99f3358…), extraits de `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…). `--branche` donnée = cette branche de sortie (écart déclaré au devis, qui nommait une branche de coffre).
  - E3-T1 Argon : fait, 0,83 USD. Carbon : fait, 1,13 USD. Neon : en cours depuis 06:18Z.
  - E3-T1 Opus : kit poussé sur `kits-abonnement/modes-v8-E3-T1-conception-A-v1` (cca1d3b3), session fille session_013QMayjy92MZW3X26Ww7deL, recueillie par recueil_session_v6 (réponse fa01f613…, fin end_turn).
  - Astra : crédit OpenAI épuisé (code 5), compté au pire 6,60 USD par le moteur, réel probablement nul. Décision de la mère R-5143 : absence acceptée aux trois tours (C) ; faux échec « jamais parti », relançable dans un dossier à part après recharge.
  - Cumul compté à 06:23Z : 8,56 USD sur 26.
- Ajout de Fable : dossier 1 (`dossier-v8-fable-max`, clé RR_ANTHROPIC_API_KEY_3) : crédit insuffisant au comptage, rien envoyé, faux échec « jamais parti ». Dossier 2 (`dossier-v8-fable-max-2`, clé RR_ANTHROPIC_API_KEY_LUC) : Fable 5.2 effort max → refusal (2,75 USD) ; Fable 5.1 effort max → refusal (0,31 USD). Classé refus du modèle ; clos à 3,06 USD par la mère (R-5144) : aucun autre effort essayé.
- Journal des faux échecs : `journaux/faux-echecs-v1.md`.

## Reste
1. Laisser finir le lancement 2 (tâche d'arrière-plan bl964mdk2) : Neon E3-T1 ; puis porte « kits en attente » au tour E3-T2 (code 2).
2. Pour chaque kit d'Opus (E3-T2, E3-T3) : pousser `kits-abonnement/modes-v8-<CID>-v1` (orpheline, un seul `texte-servi.md`), créer une session fille (Opus 5.5, effort high, source_revision = la branche, consigne système et invite fixes de `branches-kits-abonnement-v1.md`), attendre la fin, `list_events` limite 100 sans filtre, `recueil_session_v6.py PAGE DOSSIER CID SESSION --lecture-permise texte-servi.md --lignes N --commit-branche C --premier-tour --consigne-systeme "…"`, puis relancer la même commande (lancement 2, absences comprises).
3. À la fin : `verifier` du moteur sur le dossier (« tout tient »), versement complet ici, note pédagogique (Markdown + PDF par md_vers_pdf_v1.py), message à la mère (coûts, issue, commit, inventaire), commit de sortie au lecteur du coffre (session_013QMayk6v6fLDndg1jFjwdN).

## PROCHAINE ACTION exacte
Attendre la fin de la tâche bl964mdk2 (journal `journaux/lancement-2.txt`) ; si code 2 avec kit E3-T2-critique-croisee-A, faire l'étape 2 du « Reste ».
Commande de relance (depuis l'extraction de `runs/collisionneurs-reprise-v8d-v1`) :
`CLE_ANTHROPIC_FACTICE=factice PYTHONPATH=src python3 docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v6.py v8m --effort high --branche service/collisionneur-modes-v8-sorties-v1 -- etage3 --opus --argon --astra --carbon --neon --sortie-max --cle-anthropic CLE_ANTHROPIC_FACTICE --cle-openai OPENAI_API_KEY_2 --faits Q --question Q --sortie DOSSIER --plafond-usd 26 --ligne-usd 26 --accepter-absence E3-T1-conception-C --accepter-absence E3-T2-critique-croisee-C --accepter-absence E3-T3-reponse-C`
Reprise sur un autre compte : copier l'instantané versé ici comme DOSSIER (il garde son journal et ses sceaux) ; la cellule Neon E3-T1 en cours au moment de l'instantané sera relancée par le moteur (possible double dépense d'une cellule, à déclarer).

## Réserves
- Instantané pris pendant que Neon tourne : il n'en porte pas la réponse.
- Pire compté d'Astra (6,60) réduit la marge : restes au pire ≈ 18,9 sans relance contre 26 − 8,56 = 17,44 (Neon déjà en cours compris dans le compté ? non) : relances de Carbon à surveiller ; prévenir la mère avant le plafond.
- Critique croisée sans Astra ni Fable : quatre voix seulement (Opus, Argon, Carbon, Neon).
- Le classifieur de l'environnement a refusé une boucle d'essai des clés d'Anthropic ; non contourné.

## Actif
- Tâche d'arrière-plan bl964mdk2 (lancement 2 du moteur) dans ce conteneur. Aucune machine, aucun serveur, aucune tâche planifiée.
- Sessions : mère session_013QMayjbmQUdDuDs2S3i3XD ; session fille Opus E3-T1 session_013QMayjy92MZW3X26Ww7deL (finie) ; lecteur du coffre session_013QMayk6v6fLDndg1jFjwdN (pas encore contacté).
- Branches : `service/collisionneur-modes-v8-sorties-v1` (celle-ci) ; `kits-abonnement/modes-v8-E3-T1-conception-A-v1` (cca1d3b3).

## Versé ici
`runs/service-collisionneur-modes-v8-sorties-v1/instantane-2026-11-23T0623Z/` : dossier-v8, dossier-v8-fable-max, dossier-v8-fable-max-2, journaux, prealables (programmes et sorties), pages (page d'événements de la session Opus E3-T1). Compagnons .sha256 partout.
