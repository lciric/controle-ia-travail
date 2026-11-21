# Note de vérification courte — correctifs 0008, distillateur, 0009 du code de l'organisme retenu v5 — cl1

Date : 2026-11-21. Classe B. Même contre-lecteur (Claude Opus 5.5), même mandat (`47b53672…`). Périmètre : l'étalonnage seul. Rien poussé, aucune dépense, aucune machine, aucun appel à un loueur, aucun refus d'outil.

**Verdict : étalonnage autorisable.** Le code ne laisse plus de reste. Avant de sceller la configuration de l'étalonnage, il faut le mot de Lazar sur la première action dans la perte (`gardee` dans le gabarit) : c'est un nœud, et la section est scellée avec l'étalonnage. L'ordre doit écrire le risque « :\n ».

- **Arbre** : `arbre-final`, branche locale `cl-v5-final-local`. Correctifs appliqués dans l'ordre : 0001 à 0008, les trois du distillateur, puis 0009, tous sans conflit, compagnons vérifiés. **Même arborescence que la tête du développeur** 45f9ba7a : arbre `9917b13f3c57…` des deux côtés.
- **R1 levé.** La règle de coupe de la version 1 est reprise. Sur le tokeniseur réel (`sorties/sortie-sonde-coupe-tokeniseur-reel-v2.txt`) :
  - `**COST:** 4` : coupe conforme, coût lu 4 ;
  - `**COST**: 4`, `COST: 4` et `COST:4` : conformes ;
  - `COST:\n…` : toujours non conforme, comme le texte scellé le prévoit (risque à écrire dans l'ordre) ;
  - clé précédée d'une puce : aucun champ, c'est le lecteur de l'environnement.
- **R2 levé : la répétition locale jouée par moi**, liste figée v4 (`sorties/sortie-repetition-locale-liste-figee-cl-v1.txt`), code 0 :
  - lanceur de session v3 (outil, contrôles, création imprimée et jamais exécutée, après-création, surveillance) ;
  - amorce v5 en essai local : **267 essais réussis en 7 min**, 32 marques de progrès relayées, étalonnage jouet en 28 lots poussés ;
  - trois refus de destruction : attestation « aucune intouchable », liste vide, identifiant d'une autre machine ;
  - la destruction par identifiant (R10) ; la machine de l'autre chantier n'est pas touchée et aucune création n'est faite ;
  - conditions de départ et désignation (issue P, 12 tours), puis second passage refusé.
- **Mineurs n1 et n2 levés.** L'attestation est supprimée, et la répétition l'a éprouvé. Le calendrier est lu comme « 2026-11-27T00:00Z exclu », d'où dernier jour de création le 26 et fin de ligne au 2026-12-01T00:00Z : c'est la lecture prudente, juste.
- **Gabarit v4** (`config-iib-organisme-retenu-v5-gabarit-v4.json`, sceau vérifié). Il ne diffère du v3 que par deux clés :
  - `noeud_7`, à 3 830 actions hors tours, conforme à l'erratum 2 du texte et à l'erratum 1 du devis ;
  - `distillation_evaluation`, aux constantes de la conception d'origine.
  
  Le reste est conforme au texte scellé, à ses errata 1 et 2 et au devis scellé avec son erratum 1 : règle ×6 et 1,757 pour N, ×4 et 1,366 pour P ; nœuds à leur défaut, nœud 7 en (b′) ; fichier d'entrées vérifié à 45, 6,90 et 1,38 (coût fixe inchangé selon l'erratum 1) ; ligne de 60, coupure à 55 ; A100 SXM4 à 1,30 et stockage à 0,08. Liste figée de 23 fichiers, d'empreinte `342ee21d…`, égale à celle écrite dans l'amorce.
- **L'ordre remplit encore** : pièces, empreintes et marqueurs de consigne, accord cité, intouchables, fichier d'entrées scellé à 3 830. Il porte `TESTS_ATTENDUS=267`.
- **Consignes privées.** La recherche par programme sur 0008 et 0009 (`scripts/recouvrement-consignes-0008-0009-v1.py`, `sorties/recouvrement-consignes-0008-0009-v1.txt`) touche quatre lignes génériques ; aucun fragment.
- **Geste à déclarer.** J'ai modifié par erreur `scripts/recouvrement-consignes-distillateur-v1.py`, un script déjà rendu, pour en tirer la copie neuve. Je l'ai remis à l'identique, et son compagnon est vérifié OK.
