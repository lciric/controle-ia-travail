# Traitement de la contre-lecture 3 et des trois relectures de la chaîne de P4-instrument — v1

Session 14, 2026-10-20 vers 19:40 UTC. La session n'a écrit ni le module, ni la chaîne, ni aucun rapport traité.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

Rapports traités :
- contre-lecture 3 (candidat 1 et module) : `…/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md`
  (`7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368`), « scellable après corrections » : 1 majeur,
  5 mineurs, 7 de forme ;
- relecture « dépense et arrêts » : `…/relecture-chaine-depense/relecture-chaine-depense-v1.md`
  (`b6e43dd7a981d3dabc214127787ea245f976731763963d8d31a59543794f3c5b`), « conforme après corrections » : 2 majeurs,
  7 mineurs, 2 informations ;
- relecture « données et fuites » : `…/relecture-chaine-donnees/relecture-chaine-donnees-v1.md`
  (`184b8926fe320f25f31014291fead8cd29b72efed5bd107ee97eacac5d9e7733`), « conforme après corrections » : 6 mineurs,
  4 informations ;
- relecture « fidélité au texte » : `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md`
  (`923c71d87115cf114d16c8079adce4dd79aa3ca112bcf9224ad6b9088cb988c5`), « conforme après corrections » : 2 majeurs,
  6 mineurs, 4 informations.

| constat | décision | où |
|---|---|---|
| CL3-01 (majeur) et RC-fidelite-02 (même défaut) : lecture sans `--prereg` d'un run décisif ou réel | accepté : refus sans rien écrire ; cas sain et artefacts ; ligne de la liste d'arrêt et des tests | module v2 (orchestration `wf_2bfa5159-a89`) ; candidat 2 (paires du module) |
| CL3-03 : table `LIGNES` du code non alignée (L1, L4) | accepté : cellules recopiées mot pour mot ; garde de lecture qui compare au texte scellé | module v2 |
| CL3-02, CL3-04 à CL3-12 | acceptés, mots exacts du rapport | `…/ecrire_candidat2_v1.py` (paires fixes) |
| CL3-06 : population des 38 épisodes | accepté ; nombres recomptés par la session sur `1454d084…` (10 sur 380 contre 33 sur 220 ; 90e centile 266 contre 400 ; médiane 205 contre 222,5) | idem |
| CL3-13 : 0,5118 ou 0,5117 | relu par la session : `lecture-p3.json` (`c221d955…`), clé `…mention-honnete.plancher_quantile` = 0,51179542 ; arrondi au plus proche : 0,5118 ; le texte est juste, aucun changement | — |
| RC-fidelite-01 et notes de la chaîne T1 à T3 (bloquants) | acceptés : commit en 40 signes, « Tests attendus : `N` », empreintes des scripts de l'instance, ligne « Lancement » | `ecrire_candidat2_v1.py` |
| RC-depense-01 (majeur) et RC-fidelite-06 : arrêt non exécuté ni vérifié | accepté : script d'arrêt par identifiant, étiquette entière relue, état relu, appelé par la surveillance (FIN, PLAFOND) et le contrôle à cinq minutes en échec | chaîne v2 (orchestration `wf_39fd80e7-8c7`) |
| RC-depense-03 (majeur), -08, -09, RC-fidelite-03 : révocations sous formes voisines, fenêtre pendant l'appel, sous-chaîne | accepté : détection des formes voisines (arrêt, jamais passage silencieux), frontières de mot, contrôle rejoué juste avant la création | chaîne v2 |
| RC-depense-02, -04, -05, -06, -07, -10, -11 ; RC-fidelite-04, -05, -07, -08, -09, -12 | acceptés, selon les corrections des rapports (détail dans la consigne de l'orchestration) | chaîne v2 ; phrases du candidat 2 |
| RC-donnees-01 à -06, -08, -09 | acceptés (fenêtres glissantes brutes et échappées ; chemin des traces seules ; masquer avant tronquer ; schéma fermé ; contrôle des traces de session ; liste gelée lue dans `7a54d43` ; tokeniseur versé sous `donnees/P4-tokeniseur-v1/`) | chaîne v2 |
| RC-donnees-07 | information : version suivante (contrôle des fuites sur l'instance avant la poussée) ; noté | — |
| RC-fidelite-10, -11 | information, rien à faire | — |

Ordre de la suite : module v2 vérifié et chaîne v2 vérifiée → candidat 2 (script, paires du module et de la chaîne, section
« Contre-lecture ») → vérification neuve du candidat 2 → versement des préalables → répétition jouet sur le vrai C,
épingles, bancs, répétition finale → scellement S → contrôles → accord du jour → lancement.
