# Passation — session « attaquant informé » → session neuve d'un autre compte — témoin de Bailey, relance en cours — 14 novembre 2026

Session sortante `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas
(R12). Mot de Lazar, verbatim : « fais la passation a une nouvelle instance d'un autre compte et envoie le brief de
lancement ». Brief de lancement : `registres/passations/2026-11-14-0929-brief-lancement-session-neuve-temoin-bailey.md`. Aucune note de sonde ni de juge lue par cette
session ; les notes des deux exécutions du run principal restent scellées sans lecture.

## Fait (12-14 novembre)
- Série 3 (addendum 4, code v17 au commit `8d1c541e`) : pilote réussi (3 tours, aucune garde tombée, ≈ 1 316 s par
  tour) ; règle K = 72 ; run principal interrompu à K′ = 8 (compte Vast vidé, carte sans fonds, recharge automatique sans
  effet) ; reprise faite (lecture 38) : `runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2/`, transfert
  complet, scellé, instance 60417353 détruite.
- Relance seule (addendum 5, code `lanceur_v20`, commit `f60c2620` ; addendum 6, condition 9′ crédit + recharge
  automatique) : poste Hetzner v12 175967712 (09:43:45Z le 13) ; instance Vast **60480302** (A100 SXM4, Suède,
  1,172 USD/h) ; mise en place (8 gardes passées, identique à la série 3 : 1 600 pas, suffixe 13, écart 10 vrai) et
  contrôle du juge tenus ; `relance_seule` : D = 14,7733, K = 72, t = 1 315,9926 ; **`principal-relance` lancé le
  13 novembre à 10:05:32Z**.
- Essais : `tests/test_temoin_bailey_condition6_v20.py` 220 passés, 1 sauté ; `tests/test_temoin_bailey_reprise_relance_v1.py`
  (reprise d'une relance coupée, assemblage, lecture) 2 passés ; suite complète du dépôt : bilan dans
  `…/2026-11-13-0258-bilan-suite-essais-code-v17.md`.

## État au 14 novembre, 09:27Z
- Relance en cours depuis ≈ 23 h 20 (≈ 60 à 64 tours d'après les durées, non lu) ; fin attendue **≈ 12:25 à 14:20Z** ;
  le poste v12 pousse ses journaux toutes les 10 min (dernier : 09:23Z) ; journal de conduite
  `sortie-conduite-v13/conduite-v5.jsonl` : 13 lignes, dernière « principal-relance lancée ».
- D estimé ≈ 42,5 USD (compte prudent), B = 75, garde B − 2.
- Crédit Vast 6,58 USD ; recharge automatique 5 USD sous 5 USD ; paiements des 13-14 novembre : 15 (10:04Z), 15 (19:22Z),
  puis 5 USD à 03:31, 04:31, 05:31, 06:01, 06:31, 07:01, 07:46, 08:16, 08:46, 09:16Z.
- **Alerte** (envoyée à Lazar à 09:27Z) : instance **60599797** « rr-a3_e4-20261114-052621 », autre chantier, en marche
  depuis 05:26Z à **8,23 USD/h** : la carte est tirée ≈ 10 USD/h. Non touchée (pas de ce poste). Si la carte s'épuise,
  le compte se vide et Vast arrête aussi 60480302 : après 20 tours, run tronqué (l. 338, 372), lu après reprise.
- Autres instances du compte : 58936096, 58936099, 58936100 (« R8 »), arrêtées, non touchées.
- Postes Hetzner en marche : 175967712 (v12, pilote la relance) ; 175884265 (v9, sans tâche, gardé sur consigne de Lazar).
- Surveillance : mes rappels ont été déclenchés avec retard (≈ 2 h le 13, puis rien entre 16:35Z le 13 et 09:26Z le 14) :
  la nuit n'a pas été surveillée. Aucun rappel de cette session n'est en attente.

## Reste (dans l'ordre)
1. Surveiller la fin de la relance (poste, journal de conduite, crédit, inventaire).
2. À la fin : vérifier `poste-fini-v12.json`, `bilan-lancement-v13.json`, `sortie-conduite-v13/bilan-conduite-v5.json`
   (`detruite`, `transfert_complet`, `arret`) ; inventaire Vast (aucune instance `temoin-bailey-c6-*`) ; détruire le
   poste 175967712 par son identifiant (R10) ; consigner `registres/arrets.md`, `registres/depenses.md`.
3. Si l'instance n'est pas détruite ou le transfert incomplet : reprise (lecture 38) par un poste de reprise neuf (modèle :
   `runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v3.sh`, `--sortie` = chemin absolu de `sortie-conduite-v13`,
   `--etiquette` relevée dans le journal de conduite) ; il faut alors des clés (voir le brief).
4. Assemblage (`lanceur_v20.assembler_lecture`, sur processeur) : première =
   `runs/temoin-bailey-v1-20261111/sortie-conduite-v11/reprise-v10-2`, relance = `runs/temoin-bailey-v1-20261111/sortie-conduite-v13`
   (ou son dossier de reprise), cible neuve ; sceller ; pousser.
5. Verdict (R13) : un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse, applique les critères gelés
   (`lecture_v8.valider`, puis `lecture_v8.lire` avec `analyse_v3.graines()["reechantillonnage"]`, et l'audit de symétrie
   R4 du texte) sur le dossier assemblé ; verdict scellé ; soumis à Lazar pour GO. Aucune note lue avant.
6. Passation à la fin de la session neuve (R14).

## Réserves
- Condition 7 de la série 3 tenue sur une lecture de la session (addendum 4, § 6) ; mots exprès de Lazar pour la relance
  (« lance la relance », note `…-0944-…`).
- Heures fausses dans les noms de deux notes scellées (`2026-11-12-2320-decision-lazar-bailey-autonomie-10h-mot-de-lancement.md`,
  commitée à 22:50:48Z ; `2026-11-12-2312-ordre-lancement-temoin-bailey-serie-3.md`, commitée à 23:07:45Z) et une minute
  d'avance sur `2026-11-13-0944-ordre-lancement-temoin-bailey-relance.md` (commit 09:43:38Z) : contenus justes, consigné.
- Pièces jamais tournées gardées (R12) : conduites v10, v12 ; `lanceur_v18`, `lanceur_v19`.
- Défauts de la session corrigés et consignés : garde du poste de reprise v1 ; deux docstrings doublées.
- `registres/etat.md` non lu ni mis à jour par cette session (cloison) : à faire par la mère.
- À relayer par Lazar à la mère : dépôt chez le tiers des addenda 3 à 6 ; ligne Hetzner (5 USD) ; GO du collisionneur
  (50 EUR) ; licence de Luke Bailey ; instance 60599797 (8,23 USD/h) ; retrait de la clé `ssh` Vast 1864483 et de la clé de
  déploiement du poste à la fin du témoin ; révocation du jeton GitHub laissé dans une conversation du 12 novembre.

## Instances actives
Vast 60480302 (relance, en marche) ; Hetzner 175967712 (poste v12), 175884265 (poste v9, sans tâche).

## Prochaine action
Session neuve : routine de reprise (R14), puis l'étape 1 ci-dessus. Cette session n'agit plus après cette passation.
