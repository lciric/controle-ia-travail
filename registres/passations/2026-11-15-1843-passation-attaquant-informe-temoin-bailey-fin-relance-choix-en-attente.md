# Passation — session « attaquant informé » (compte neuf) — témoin de Bailey : relance finie, assemblage fait, choix de Lazar en attente — 15 novembre 2026, 18:43 UTC

Session sortante `session_016QhUrudziqEQujXt4ofM8u`, branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas
(R12). Demande reçue à 18:42Z par message de la session `session_016QhUrtmLyFWJP6Cy7rgfXH` (« demande de Lazar,
transmise par la session mère » ; identifiant différent de la mère nommée au brief, `session_01VJdZpSMxSdk2SJ1ScmdfNv` :
non vérifiable d'ici, signalé à Lazar). Brief de lancement de la suite :
`registres/passations/2026-11-15-1843-brief-lancement-session-neuve-temoin-bailey-choix-et-verdict.md`.
**Aucune note de sonde ni de juge lue par cette session.**

## Fait (14 novembre 23:32Z → 15 novembre 18:43Z)
- Routine de reprise : empreintes de `docs/` justes ; `verifier-arbre` : 113 problèmes (111 compagnons absents sous
  `runs/temoin-bailey-v1-20261111/`, 2 sous `docs/notes/`), consignés, non corrigés ; essais du témoin 219 passés,
  4 sautés (`hydra` absent de l'environnement ; `configs/` public non fourni).
- Surveillance de la relance (veille en lecture seule, 10 puis 5 min) ; crédit Vast jamais sous 4 USD.
- Diagnostic en lecture seule de 60480302 (mots de Lazar « A », « A′ go », « go Hetzner ») : `ssh` impossible depuis la
  session (mandataire HTTPS seul ; note `…/2026-11-14-2344-diagnostic-ssh-impossible-temoin-bailey.md`, `bee80e1f…`) ;
  fait par serveur Hetzner jetable 176183969 (détruit) : sortie
  `runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt` ; le run avançait (≈ 1 h 50 par tour au tour 32).
- Mot « garde la garde à B − 2, go » ; mot « option 3 go » (prolonger à 72 tours) **non exécutable** : B = 75 est figé
  dans la mémoire du processus d'exécution (`instance_v16.py` l. 815-822) et du journaliseur (`journaliseur_v3.py`
  l. 302-303) ; rien n'a été touché.
- Sauvegarde en lecture seule des sondes et paramètres (mot « go ») : serveur v1 176186695 détruit (défaut `ssh` sans
  `-n`) ; serveur v2 **176187199** : 74 fichiers (sondes et paramètres des tours 0 à 36), empreintes en accord ; listes
  `runs/temoin-bailey-v1-20261111/sauvegarde-sondes-v2/liste-passage-01…09.tsv` ; fichiers sur le disque du serveur
  (`/root/sauvegarde`).
- Conception de la continuation (mot « prépare la continuation à froid, go ») : v1 (`eb26b686…`), contre-lecture R2
  (`contre-lecture-conception-continuation-v1.md`, `1da5b75f…`, 7 bloquants), v2 (`conception-continuation-relance-v2.md`,
  `6651a07f…`), non contre-lue ; recommandation : pas de continuation.
- **Fin de la relance** (15 novembre, ≈ 11:52Z) : garde « dépense » ; `sortie-conduite-v13/bilan-conduite-v5.json` :
  `detruite` vrai, `transfert_complet` vrai, D = 73,026 USD, **36 tours complets**, aucune garde tombée ; journal du
  chien non transféré (`CalledProcessError`). Poste v12 175967712 détruit par son identifiant (11:58Z). Clés Vast de
  session 1900274, 1902919, 1903144 toutes supprimées du compte.
- **Assemblage** : `lanceur_v20.assembler_lecture` → `runs/temoin-bailey-v1-20261111/lecture-assemblee-v1/`
  (`assemblage-v1.json` et compagnon ; 44 fichiers scellés vérifiés).
- Registres : `registres/arrets.md`, `registres/depenses.md` à jour pour 176183969, 176186695, 60480302, 175967712.

## Reste
1. **Choix de Lazar, en attente, à faire avant toute lecture du verdict** (R1, R4) : 1 = verdict à 36 tours au régime
   réduit et fin ; 2 = run neuf de 72 tours préparé à froid ; 3 = continuation v2. Recommandation : 1 (confiance
   moyenne). Pour 2 ou 3 : addendum scellé et contre-lu **avant** le verdict R13.
2. Choix 1 : verdict R13 par un sous-agent neuf sur `lecture-assemblee-v1` (`lecture_v8.valider`, puis
   `lecture_v8.lire(v, analyse_v3.graines()["reechantillonnage"])`, audit de symétrie R4), scellé, soumis à Lazar ;
   puis destruction du serveur 176187199 par son identifiant (sauvegarde sans objet) et consignation.
3. Choix 2 ou 3 : garder 176187199 ; addendum, contre-lecture, GO hors enveloppe sur `main` (mère), code.

## Réserves
- Le ralentissement n'est pas expliqué : durées des tours de 36 min (tour 0) à 2 h 13 (tour 32), puis 67, 45, 47 min
  (tours 33 à 35) ; l'hypothèse « banque qui grossit » ne tient pas seule ; les devis de la v2 sont fragiles.
- Garde de calcul du dépôt : elle bloque `vastai create ssh-key` (motif prévu pour les lancements) ; clés posées par
  l'interface web de Vast, consigné.
- `registres/etat.md` non lu ni mis à jour (cloison) ; la ligne « go c » (postes Hetzner) reste à inscrire par la mère ;
  le `registres/go.md` de cette branche ne contient pas la ligne GO-2026-11-10-10 (elle est sur `main`).
- Clé de déploiement GitHub `diag-temoin-bailey-depot-20261115` (écriture) : à retirer par Lazar après la décision sur
  la sauvegarde (le serveur 176187199 l'utilise pour pousser).

## Instances et serveurs actifs
Vast : aucune instance du témoin (les trois « R8 » d'un autre chantier sont arrêtées, non touchées). Hetzner :
**175884265** `poste-temoin-bailey-v9` (sans tâche, gardé sur consigne de Lazar) ; **176187199**
`sauvegarde-temoin-bailey-v2` (garde la sauvegarde, ≈ 0,006 EUR/h). La mère n'y touche pas.

## Prochaine action
Session neuve : brief `registres/passations/2026-11-15-1843-brief-lancement-session-neuve-temoin-bailey-choix-et-verdict.md`.
Cette session n'agit plus après cette passation, sauf mot de Lazar.
