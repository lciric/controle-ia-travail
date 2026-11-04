# Rapport de rédaction de la relance v4 de R1 (code, addendum v4 brouillon 1, devis) — v1

- Auteur : concepteur-développeur neuf (sous-agent, Opus 5.5) ; je n'ai écrit ni R1, ni ses addenda, ni son code, ni le
  diagnostic. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/r1-v4-developpeur-code-et-addendum-prompt.md`
  (`059a564f…`, compagnon concordant) et son avenant `brouillons/reprise-fusionnee-2026-11-04/avenant-relances-v1.md`
  (`d4f14478…`), empreintes vérifiées par `sha256sum` avant lecture.
- Dates (UTC, `date -u`) : début 2026-11-04 01:34:51 ; redémarrage du conteneur vers 01:53 (aucun fichier perdu,
  reprise sans rien refaire) ; fin de rédaction : voir la dernière ligne.
- Arbre de travail `/home/claude/wt/r1-v4/`, branche locale `prep/r1-relance-v4` (tête `04bc323a`) ; **aucun commit,
  aucun `.sha256`, aucun fichier existant modifié, aucun `git fetch`/`checkout`/`stash`/`reset` dans cet arbre** ;
  aucun réseau, aucun modèle téléchargé, aucune carte, aucune dépense. Rien n'a été ouvert sous `donnees/` (les essais
  copient `donnees/` dans un dossier temporaire du banc de mutations pour les fixtures jouets, sans le lire).
- Interdits de lecture respectés : aucun tableau d'activations, aucun score, aucune sortie d'analyse ; exposition
  déclarée : le rapport Fable, lu en deuxième comme l'exige la consigne, cite des classes et écarts de détection de la
  v3 (son § 0, points 6 à 9 ; § 7) ; rien de cela n'entre dans le code ni dans l'addendum, qui déclare le signe connu
  sans le citer (V4-E2).

## 1. Fichiers neufs (sha256)

Voir la section 7.

## 2. Ce que fait le code

**`resolution_graine_lot_v2.py`** (réparation, témoin, table v4) :
- `generer_lot_multi` : `generer_lot` de P3 refait appel pour appel, **plusieurs lignes cibles** à la fois (un
  `ChoixCible` de la v1 par cible), **jusqu'à la fin de la dernière ligne** (forme exacte de P3, passes = la plus longue
  moins un) ; capture des activations de génération avec les crochets de P3 (`Crochets`, `relire_crochets_lot`,
  `empreinte_tableaux`) ; une cible en contradiction est déclarée et remplie d'un **jeton ordinaire** jusqu'à sa
  longueur (forme gardée).
- `rejouer_lot_multi` : les T pas d'un lot ; cibles, lignes exactes forcées et mesurées (`MesureLigne` de la v1, avec
  leur graine), lignes approchées (`forcee_approchee`) ; tirages exponentiels calculés **action par action** (mémoire :
  une action de 400 jetons pèse ≈ 205 Mo de tirages, calcul) ; rend, par cible, identifiants et empreinte de trajectoire.
- `lire_temoin` (lecture gelée, égalités exactes) ; `voie_de_reparation` (écrite d'avance : non exact → passe forcée) ;
  `captures_de_p3` (fiches : clés permises seulement ; échantillon d'équivalence **recalculé** depuis les graines et
  comparé) ; `connus_v4` (base identique ou table v3 appliquée, revérifiée) ; `cibles_v4` ; `exiger_comptes_attendus`.
- Étapes `temoin`, `reparation` (lot multi → lot à une cible de la v1 avec repli 272 → passe forcée du cœur 272 ; ou
  passe forcée seule), `table-v4` (`construire_table_v4`, `charger_table_v4`, `ecrire_table_v4`).

**`rejeu_activations_v4.py`** : copie de la v3 aux écarts marqués `# v4` : table version 4, empreinte citée ou
« construite-en-session », règle A étendue (`classer_episodes_v4`), non retrouvés déclarés hors de la règle B, sorties
`tokenisation` étendues ; contrôle négatif et méthodes de résolution importés de la v3.

**Scripts** : `scripts/r1_v4_instance_v1.sh` (une instance par session, `SESSION=temoin|reparation`) et
`scripts/amorce_instance_r1_v4_v1.sh` ; `scripts/banc_mutations_r1_v4_v1.py`.

**Configurations** (fichiers neufs, nécessaires aux scripts et cités par l'addendum) : `prereg/R1-reparation-v4-config-v1.json`
(configuration du complément, brouillon 2, plus les clés v4) et `prereg/R1-rejeu-config-v6.json` (v5 sauf la table).

## 3. Ce qui reprend la v3 et ce qui en diffère

Repris tels quels (importés, non modifiés) : choix contraint `ChoixCible`, mesure `MesureLigne`, moteur `MoteurLot`,
repli à une cible `resoudre_episode_lot` (v1 du lot) ; passe forcée `resoudre_avec_repli`, tirages, `Vocabulaire`,
`transcription`, `entree_identifiants`, `appliquer_entree_v3`, `verifier_entrees_v3` (cœur) ; rejeu v3 entier hors des
lignes marquées `# v4` (fidélité, tolérance, contrôle négatif, repli, agrégats, sorties). Diffère : cibles (les 89, sans
passage préalable du cœur ni table v2), plusieurs cibles par lot, forme complète du lot, capture recalculée, témoin et
voie écrite d'avance, remplissage ordinaire, table version 4 (règle A étendue, empreinte en session), règle B séparée
des non retrouvés, scripts à deux sessions. Les quatre endroits de code que le diagnostic nomme (§ 6.2) sont traités :
(1) cibles → `cibles_v4` ; (2) table → `construire_table_v4` ; (3) chargement → `charger_table_v4` ; (4) règle A →
`classer_episodes_v4`.

## 4. Essais et banc (sorties)

Voir la section 6.

## 5. Dix points pour un contre-lecteur neuf

1. **Lecture « exact » du témoin** : égalités exactes sur l'accord (argmax de p / q contre le jeton de P3), les choix
   contraints, la forme et les captures. L'accord n'est pas une égalité au bit des logits : seules les **8 captures du
   lot 2** sont des égalités au bit (le lot 13 n'en a aucune, diagnostic § 4.3). Est-ce assez pour abandonner ou garder
   la voie du lot ? (`lire_temoin`)
2. **Indépendance des lignes d'un lot** : le code suppose que les logits d'une ligne ne dépendent des autres lignes que
   par la forme (taille, longueur remplie, remplissage), d'où le remplissage d'une cible en échec par un jeton ordinaire.
   Vrai pour les noyaux usuels sur processeur (essai : les autres lignes gardent leurs logits au bit) ; à juger sur carte,
   où un noyau pourrait dépendre du contenu (le témoin ne l'éprouve pas, puisqu'il force toutes les lignes).
3. **Empreinte de la table v4 non citée d'avance** (V4-E5) : défendue par l'oracle de P3 (revérification au chargement)
   et la chaîne scellée ; alternative : troisième session sous texte neuf. Le choix est un nœud possible de Lazar.
4. **Règle B et non retrouvés** (V4-E7) : une cible non retrouvée garde le traitement de la v3 et n'entre pas dans le
   seuil de la règle B ; vérifier que cela ne change aucune lecture gelée.
5. **Ordre des voies dans la réparation** : lot multi → lot à une cible (v1, repli 272) → passe forcée (272). La v1 du
   lot arrête ses passes à la fin de sa cible (`arreter_apres_cible`) : forme partielle, sans effet sur la cible.
6. **Garde-fous de durée et de dépense** : délai externe 2 100 min par étape en session 2, plus court que les budgets
   internes (259 200 s) ; plafond d'amorce 2 200 min ; tâches planifiées à 45 et 57 USD (devis § 3) : cohérents ?
7. **Complément scellé illisible** : le commit `4b47db7b` n'existe pas sur la machine de rédaction ; C1 et C2 ont été lus
   dans le brouillon 2 (`41d5350e…`) ; à recouper avec le texte scellé.
8. **Tests attendus 358** : compte collecté sans le tokeniseur (beaucoup d'essais sautés ici) ; le nombre passé doit être
   établi au commit cité avec le tokeniseur de la révision de P3.
9. **Pré-vol sur les vraies pièces** non fait (sans modèle 8B ni lecture de `donnees/` dans cette tâche) : 89 cibles, 28
   lots, lots 2 et 13 entièrement connus, captures recalculées égales aux fiches — à faire avant le scellement.
10. **Session 2 et commit** : la session 2 part d'un commit qui ajoute au commit de scellement le run du témoin versé
    (hors de l'arbre gelé) ; `exiger_temoin` exige même configuration et même code (`exiger_meme_code`), le script exige
    le témoin présent, scellé, non arrêté.

**Fichiers à lire** : l'addendum `prereg/R1-addendum-relance-v4-brouillon1.md` ; les deux configurations ; les deux
modules neufs ; leurs essais ; les deux scripts ; le banc ; le devis ; ce rapport ; le diagnostic (`1c2dd25f…`) ;
l'addendum v3 (`88e262e2…`) ; le parent (`80c85a00…`) ; `resolution_graine_lot_v1.py` et `resolution_graine_v1.py`
(fonctions importées) ; `rejeu_activations_v3.py` (pour le diff avec la v4).

## 6. Sorties des essais

Commande de la consigne (`PYTHONPATH=src nice -n 10 python -I -B -m pytest -q -p no:cacheprovider`), sur les fichiers
neufs et voisins ; environnement : `.venv` de `/home/user/controle-ia-travail` (avenant) ; aucun téléchargement ; le
tokeniseur de Llama 3.1 est absent de ce poste, les essais qui le lisent sont sautés (tous dans des fichiers existants).

- **Essais neufs** : `tests/test_resolution_graine_lot_v2.py` **13 passés** ; `tests/test_rejeu_activations_v4.py`
  **3 passés** ; avec `test_resolution_graine_lot_v1.py`, `test_resolution_graine_v1.py`, `test_rejeu_activations_v3.py`,
  `test_runs_nuit_v2.py` : **49 passés, 18 sautés, 0 en échec** (560,6 s) — sortie `essais-relance-v4-sortie-v1.txt`.
  Ce qu'ils éprouvent (R5, cas sain et artefact pour chaque garde) : logits au bit et captures d'équivalence au bit du
  lot rejoué contre `jouer_episodes` ; témoin « exact » sain ; artefacts « non exact » : graine fausse, poids décalé d'une
  unité au dernier rang, capture altérée, un seul désaccord sur 400 pas ; plusieurs cibles retrouvées ensemble avec les
  identifiants vrais non canoniques, égales au résultat à une cible (v1) ; cibles plus courtes que le lot (forme
  complète, captures des lignes forcées inchangées) ; cible en échec seule (les autres retrouvées, contextes aux longueurs
  de P3, y compris sur une action sans fin et sous échéance dépassée) ; contrôle du texte décodé (artefact de décodage) ;
  gardes de la ligne approchée, de la voie, de la lecture ; `cibles_v4` ; captures recalculées (échantillon faux
  refusé) ; bout en bout jouet : témoin exact → voie du lot, 4 cibles sur 4 en un essai à plusieurs cibles ; témoin non
  exact (modèle décalé) → voie de la passe forcée, 4 sur 4 ; table v4 écrite, scellée, rechargée ; refus : identifiants
  falsifiés, autre configuration, table v3 au chargeur v4, empreinte fausse, R12, R3, témoin sur un lot sans identifiants
  connus, réparation sans témoin, comptes attendus faux, entrée `non_resolu` et cause recopiée ; rejeu v4 sain (table en
  session et citée) : 8 trajectoires sur 8, 16 actions conformes et en contexte exact, fidèles de la v4 ⊇ fidèles de la
  v3 et plus nombreux ; artefacts du rejeu : empreinte fausse (avant le manifeste), table v3 refusée, entrée retirée et
  entrée falsifiée (« echec », aucun fichier d'activations).
- **Banc de mutations** (`scripts/banc_mutations_r1_v4_v1.py`, copie hors de l'arbre, cas sain obligatoire ; sortie
  `banc-mutations-relance-v4-sortie-v1.txt`, toutes les passes) : passe 1 **fausse** (copie incomplète : six « tuées » par
  une erreur d'installation ; banc corrigé, déclaré) ; passe 2 : 9 tuées sur 15 ; passe 3 (essais renforcés) : 13 sur
  15 ; passe 4 : 14 sur 15 ; passe 5 (M06 seule, après l'essai « échéance dépassée ») : tuée. **Bilan : 15 mutations sur
  15 tuées** par les essais finaux (M06 dans la passe 5 ; les 14 autres dans la passe 4, avant l'ajout du dernier essai,
  qui ne fait qu'ajouter). Constat de la passe 4 : un remplissage par une fin autre que la fin de clôture garde la
  longueur à la dernière place d'une action ; seule une coupure en milieu d'action (échéance) le distingue.
- **Gardes d'avant l'installation des scripts** (copie : dépôt nu local, jetons factices ; sortie
  `essais-gardes-scripts-v4-sortie-v1.txt`) : cas sain (session 1) jusqu'à la poussée initiale, puis arrêt voulu aux
  essais ; huit artefacts arrêtés en code 2 : session 2 sans `TEMOIN_RUN`, témoin absent du commit, `DELAI_ETAPE_MIN`
  = 0, `SESSION` inconnue, branche existante, table v4 présente au commit, configuration du rejeu sans
  « construite-en-session », sceau de l'addendum faux. Non éprouvés ici : la suite complète au nombre exact (358, avec
  le tokeniseur), une répétition jouet de bout en bout des deux sessions sur l'instance (à faire, comme en v3).

## 7. Fichiers neufs et empreintes (sha256, fin de rédaction)

| fichier | sha256 |
|---|---|
| `src/controle_ia/runs_nuit/resolution_graine_lot_v2.py` | `501ab45308f2ffe5e3cf25b0352b0d2e7f8bca0bb2ba7cd897c3b2c39b704f87` |
| `src/controle_ia/runs_nuit/rejeu_activations_v4.py` | `d31dcec074b513b597a4920a5c6501326ee18c8cefe4bbd83d381f4ac4b25a08` |
| `tests/test_resolution_graine_lot_v2.py` | `56dcd66076ffdc9298770e81536ad2d0180de2be0e02989430f9f41668c30ac1` |
| `tests/test_rejeu_activations_v4.py` | `dc913d7ae2a335b1d3aef754454fec6ad0186d1bc8e1655f7313abf44a896d21` |
| `scripts/r1_v4_instance_v1.sh` | `e72cf7f248bd1b0f2064b824711a3a20f43bda748ea5cacf54a2d13b31fba1f9` |
| `scripts/amorce_instance_r1_v4_v1.sh` | `4785429077afd2fdf25a8d13c3824ad0ada1cdd128e6c119080fb7fc1c1df217` |
| `scripts/banc_mutations_r1_v4_v1.py` | `d22be91a52d524fcafdcc4d057673124605804091748bdaf92aadad09e74a6c7` |
| `prereg/R1-reparation-v4-config-v1.json` (canonique `a5a61077…`) | `8de2737d301623783c823fa5076079eb49936460a07f05a8f6d417d8e390e0ab` |
| `prereg/R1-rejeu-config-v6.json` (canonique `a3ef1bac…`) | `a9ebc6b0cd6c99e118ade7b304472b5452d2b43c63cc222d1adccd2ee4e95e75` |
| `prereg/R1-addendum-relance-v4-brouillon1.md` | `a16d555d185a5da68394480b0056c2eb6bde50508ae0abeeb84e7931897ff790` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/devis-relance-v4-v1.md` | `d8d223fab8083b7f91fabb86111af52a8ea752882f7f6a031c3b3580d0dcea78` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/essais-relance-v4-sortie-v1.txt` | `ae647a4af538c4b168d927b8e0e276faa375fb79cc45cdf03f87633a67093dfc` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/banc-mutations-relance-v4-sortie-v1.txt` | `e4e0dc82ba9e9b9db04d87315b45ffec19e78a8d159f98b6df8d98a1e4efc03d` |
| `docs/notes/runs-r1-r2-r4-v1/relance-v4/essais-gardes-scripts-v4-sortie-v1.txt` | `bc8a96f894e35df7de4f8dd84b6e37b0f45d394b7c72abd7eb1e8cd31ab519e7` |

Ce rapport : empreinte rendue à l'appelant (il ne peut pas se citer). Marqueur restant dans l'addendum : « À REMPLIR »
(commit du code d'analyse), aucun autre.

Fin de rédaction : 2026-11-04 06:03 UTC (`date -u`).
