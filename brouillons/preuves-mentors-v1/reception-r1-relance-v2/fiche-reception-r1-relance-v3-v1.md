# Fiche de réception de la relance de R1 sur la table de tokenisation v3 (addendum v3 de R1) — v1

- **Ce document** : la fiche de réception de conv-audit, c'est-à-dire son document de contrôles (règle C-1 de notre
  concordance `8482b4cd…` ; addendum v3, E8 (e), étape 3 et « Liste d'arrêt » ; GO-2026-11-02-27). Il est distinct des
  deux fiches JSON de nos analyses scellées (`prereg/fiche-reception-principale-r1-r2-v1.json`,
  `prereg/fiche-reception-blanche-noire-v3.json`), qui s'écrivent après le versement, par le même script en mode
  « après le versement », qui relit cette fiche.
- **Écrite par** `ecrire_fiches_reception_v2.py` (sha256 `d4701213e20b08b9dc9cab45e318c869c1f5ec0ee1fe36cb29ac723caea4c7b3`), mode « avant la récupération », le 2026-11-03 à 06:23:34 UTC (horloge du système,
  temps universel), pour : sous-agent développeur neuf (Claude Opus 5.5) pour la session conv-audit, consigne reception-r1-relance-v3-v2-developpeur-prompt.md.
- **Moment du scellement : avant toute récupération des sorties de la course** par session-depot (C-1). La session la
  scelle (`python -m controle_ia.scellement sceller`), la commite, la pousse, puis envoie au canal son chemin et son
  empreinte ; session-depot vérifie l'empreinte (compagnon `.sha256` égal) ; sans ce message, rien n'est récupéré. La
  création de l'instance n'en dépend pas (addendum v3, E8 (d)). Étape 0 de la procédure de réception v2.
- **Constat à l'écriture** : 17 références lues dans le dépôt ; aucune `calcul/…` ; aucune dont
  le nom contient `donnees`. Aucune sortie de la course n'existe ici ; rien n'en a été lu. Commits résolus : scellement
  `139a81d37fbd2255aff8d27698f84b47b9433221`, principale `83ce7a91f681b36668a9f91424d53ebd632b50b1`, secondaire
  `7a238666630a6d6dca064e8da6b309320060200d`, tête de la branche de travail `2bd8147d409ab277c312c62012045875e66c165e`.
- **Gardes passées par le script** : recuperation, config-table, canonique, table, ligne-104, attentes-texte, piece, compagnon.

## 1. Textes qui encadrent la réception (lus par `git show <commit>:<chemin>`, empreintes recalculées)

| pièce | chemin | commit | sha256 | sceau |
|---|---|---|---|---|
| addendum_v3 — texte qui gouverne la course | `prereg/R1-addendum-relance-v3.md` | `139a81d37fbd` | `88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4` | compagnon égal au même commit |
| configuration_v5 — configuration du rejeu | `prereg/R1-rejeu-config-v5.json` | `139a81d37fbd` | `acad6253f3c9f4d93c45a453ae8f5dcb122049a979cf43000d47c5f9c1edd4b8` | compagnon égal au même commit |
| table_v3 — table de tokenisation v3 | `prereg/R1-table-tokenisation-v3.json` | `139a81d37fbd` | `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423` | compagnon égal au même commit |
| parent — préenregistrement parent | `prereg/R1-R2-rejeu-p3-v1.md` | `139a81d37fbd` | `80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea` | compagnon égal au même commit |
| module_v3 — module de la relance (sans compagnon, en-tête de l'addendum v3) | `src/controle_ia/runs_nuit/rejeu_activations_v3.py` | `139a81d37fbd` | `0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc` | sans compagnon (déclaré) |
| manifeste_py — écriture du manifeste (sans compagnon ; concordance § 0) | `src/controle_ia/manifeste.py` | `139a81d37fbd` | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` | sans compagnon (déclaré) |
| script_instance — script d'instance v3 | `scripts/r1_relance_instance_v3.sh` | `139a81d37fbd` | `24744794808832e30cb8fa47c45a19de5a530d5ce06db1bd0557a17d3e35e4eb` | compagnon égal au même commit |
| amorce — amorce v3 | `scripts/amorce_instance_r1_relance_v3.sh` | `139a81d37fbd` | `82f386876d3e606e6d8d7d6c388e42a822266d7cf899d448991b8af456badef7` | compagnon égal au même commit |
| principale — analyse principale scellée | `prereg/analyse-principale-r1-r2-v1.md` | `83ce7a91f681` | `8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537` | compagnon égal au même commit |
| secondaire — analyse secondaire scellée | `prereg/analyse-blanche-noire-v3.md` | `7a238666630a` | `1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9` | compagnon égal au même commit |
| par_episode — lecture par épisode scellée | `prereg/analyse-par-episode-v1.md` | `2bd8147d409a` | `26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4` | compagnon égal au même commit |
| concordance_b2 — notre concordance sur le brouillon 2 (R-1 à R-5) | `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md` | `2bd8147d409a` | `8482b4cd39348104e80187b1470001f71fc6d857fc75344a32529b6dd37ade0b` | compagnon égal au même commit |
| verdict_graine — verdict du rejeu à graine (réserve HG-2) | `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md` | `2bd8147d409a` | `64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68` | compagnon égal au même commit |
| procedure_v1 — procédure de réception v1 (arrêt de la première course) | `brouillons/preuves-mentors-v1/reception-r1-relance-v1/procedure-reception-lecture-r1-relance-v1.md` | `2bd8147d409a` | `d85bd5e467ef9a735db05afb661093e5513db7925eb9d1a573154c4fc13ff01b` | compagnon égal au même commit |
| reserve_n2 — réserve N2 (lecteur de la secondaire) | `brouillons/preuves-mentors-v1/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md` | `2bd8147d409a` | `c82b4d009cbfcdf34ceeaeb5870fb8b5f76dbfc40bb4cfce90a792f1b12aae42` | compagnon égal au même commit |

- Configuration v5 : empreinte canonique `1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4` (JSON aux clés triées, séparateurs
  compacts : règle de `manifeste.config_canonique`) ; elle cite la table v3 (chemin et empreinte), le parent (chemin et
  empreinte), `nom_sortie` = `activations-p3-rejeu-v1`, couches [7, 15, 23],
  `seuil_non_conformes` = 10 (sans effet, E3), mode `reel`.
- Table v3 (structure et comptes seulement) : version 3 ; 240 épisodes,
  151 conformes en longueur, 129 identiques à la
  base, 22 signalés, 22 corrections vérifiées,
  151 trajectoires identiques après la table, `non_resolu` =
  0 ; méthodes : fins 1, une_paire 12, deux_paires 2, trois_paires 1, fenetre 2, identifiants 4 ;
  fins du format [128001, 128008, 128009] ; `resultat_graine_sha256` = `674825453a8ce34c8bb6f8cb59a054b37af76d24f5e8b44b06f2c5e59d396079` ;
  `table_v2_sha256` = `5f6cf489eb971c195f7263cb738bc5f9de4bdf5cfd0f55658fd3977d3f4b55e2`.
- Code : commit cité par l'addendum v3 `f921fcec10539f1565fab410624a926efdfec12e` ; le script ne voit que le commit de scellement (empreintes
  ci-dessus) ; l'identité de l'arbre `src`, `tests`, `scripts` entre les deux est vérifiée par la procédure v2 (étape 0).
  `manifeste.py` l. 104 au commit de scellement : `"preenregistrement": prereg_info,` (clé réelle du texte qui gouverne).
- Les « Attentes de réception » de l'addendum v3 (étape 3), son en-tête (entropie, empreintes, chemins, commit du code),
  E16 et la section « R2 » portent mot pour mot les valeurs des sections 3 à 5 (garde `attentes-texte`).
- Concordance de conv-audit sur la **version scellée** : condition du lancement chez session-depot (chemin et empreinte
  consignés dans `docs/notes/runs-r1-r2-r4-v1/concordance-relance-v3-consignee-v1.md`) ; non citée ici, elle est la
  précondition P2 de la procédure v2, vérifiée avant l'étape A.

## 2. Ce qui sera lancé, puis versé (rappel du texte scellé ; constaté à la réception)

- GO-2026-11-02-27 (plafond 60 USD, échéance 2026-11-16) ; commit lancé = commit de scellement `139a81d37fbd2255aff8d27698f84b47b9433221` ;
  course poussée sur `calcul/r1-relance-v3-reel-v1` (ou `calcul/r1-relance-v3-reel-v2` après une reprise
  E21) ; puis versement à l'octet sur `calcul/r1-r2-reel-v1` par un commit neuf, en avance rapide, sans réécriture.
- Voie de réception de conv-audit : la seule refspec
  `+refs/heads/calcul/r1-r2-reel-v1:refs/remotes/origin/calcul/r1-r2-reel-v1` ; jamais de `git merge` d'une
  branche `calcul/…` ; `git for-each-ref refs/remotes | grep -c donnees` = 0 après la récupération.
- Run lu : le seul nommé par le message de versement de session-depot, de la forme `AAAAMMJJ-HHMMSS-r1-rejeu-reel`,
  autre que la première course `20261102-002114-r1-rejeu-reel` (arrêtée ; son `arret.json`, haché par un tube et jamais
  ouvert, doit rester `c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07`). Juges : ceux déjà versés, non relancés (section 5).

## 3. Manifeste du rejeu `runs/<run>/manifeste.json` (sceau vérifié ; tout écart arrête)

| clé | attendu | garde |
|---|---|---|
| `run_id` | le run nommé par le fournisseur | `rattachement` |
| `commande` | `python -m controle_ia.runs_nuit.rejeu_activations_v3` | `commande` |
| `decisif` | `true` | `decisif` |
| `preenregistrement` (clé réelle, `manifeste.py` l. 104) | `{"chemin": "prereg/R1-addendum-relance-v3.md", "sha256": "88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4"}` | `texte` |
| `config_sha256` | `1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4`, égal au recalcul canonique de `config` | `configuration` |
| `config.chemin_table_tokenisation`, `config.table_tokenisation_sha256` | `prereg/R1-table-tokenisation-v3.json`, `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423` | `configuration` |
| `commit` | `139a81d37fbd2255aff8d27698f84b47b9433221` (commit de scellement lancé) | `commit` |
| `depot_propre`, `reserves` | `true`, `[]` | `commit` |
| `graines.fidelite.entropie` | `36410133060804533274328900142752730279` (même entropie, aussi après une reprise E21) | `entropie` |

## 4. Résultat `diag/<run>/rejeu-activations.json` (sceau, rattachement au manifeste ; tout écart arrête)

| clé | attendu |
|---|---|
| `run_id`, `manifeste_sha256` | le run ; l'empreinte du fichier du manifeste (garde `rattachement`) |
| `resultat.verdict_fidelite` | « conforme » ; sinon le run porte `arret.json` (section 7) |
| `resultat.tokenisation.table_sha256` | `ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423` : **comparée, refus sinon** (garde `table-comparee`) |
| `resultat.tokenisation.addendum` | `prereg/R1-addendum-relance-v2.md` **à l'identique** : provenance de la table v3 (E16), jamais le texte qui gouverne, qui se lit dans `preenregistrement` du manifeste (section 3) ; toute autre valeur signale un autre code : arrêt (garde `provenance`) |
| `resultat.fichiers` | les empreintes des trois `.npz` versés, égales à leurs compagnons |
| `resultat.empreintes_p3.episodes` | `240` |
| `resultat.empreintes_p3.trajectoires_identiques` | `151` |
| `resultat.fidelite_toutes.actions` | `2400` |
| `resultat.fidelite_toutes.conformes_longueur` | `2236` |
| `resultat.fidelite_toutes.contextes_conformes` | `1782` |
| `resultat.tokenisation.version_table` | `3` |
| `resultat.tokenisation.corrections_verifiees_au_chargement` | `22` |
| `resultat.tokenisation.trajectoires_identiques_base` | `129` |
| `resultat.tokenisation.signales` | `22` |
| `resultat.tokenisation.corrections_par_methode` | `{"fins": 1, "une_paire": 12, "deux_paires": 2, "trois_paires": 1, "quatre_paires_meme_action": 0, "copie": 0, "fenetre": 2, "fenetre_et_paire": 0, "deux_fenetres": 0, "fin_et_paire": 0, "fin_et_fenetre": 0, "fin_et_deux_paires": 0, "deux_fins_et_paire": 0, "identifiants": 4}` |
| `resultat.tokenisation.par_methode_resolution` | `{"v1": 15, "v2": 3, "identifiants": 4, "aucune": 218}` |
| `resultat.tokenisation.episodes_non_resolus` | `[]` |
| `resultat.tokenisation.actions_non_resolues` | `0` |
| `resultat.tokenisation.fideles_parmi_non_resolues` | `0` |
| `resultat.tokenisation.seuil_non_conformes` | `10` |

Les comptes ci-dessus sont fixés par la table et la configuration (et le pré-vol pour 2 236 et 1 782), quasi certains :
un écart signale une autre course ou une autre table (garde `comptes`) : arrêt, nœud de Lazar.

## 5. Fichiers attendus (noms exacts, empreintes égales aux compagnons ; un nom en plus ou en moins arrête)

- `runs/<run>/manifeste.json` ; `diag/<run>/rejeu-activations.json` (ou `diag/<run>/arret.json` seul, sans `donnees/<run>`) ;
  `donnees/<run>/activations-p3-rejeu-v1.npz`, `donnees/<run>/activations-p3-rejeu-v1-maximum.npz`,
  `donnees/<run>/activations-p3-rejeu-v1-complement-hors-cout.npz` ; chacun avec son compagnon `.sha256`.
- Juges (R2 ne se relance pas ; addendum v3, « R2 ») : `donnees/20261102-004328-r2-juge3b-reel/scores-juge3b-p3-v1.npz`
  = `10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354` ; `donnees/20261102-005048-r2-juge8b-reel/scores-juge8b-p3-v1.npz`
  = `1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b` ; avec leurs `runs/<juge>/manifeste.json` et `diag/<juge>/juge-actions.json`
  (garde `juges`). Aucun `.npz` n'est ouvert par la réception.

## 6. Non lu avant les analyses (valeurs observées de P-R5 et lectures de l'instrument)

- Clés du résultat jamais gardées, écrites ni affichées par le script : `fideles`, `notees`, `fideles_parmi_contextes_conformes`, `notees_contextes_conformes`, `egalite_exacte`, `ecart_max`, `ecart_mediane`, `part_fideles_parmi_notees`, `p_r5_au_moins_90_pour_cent`, `fidelite_echantillon`, `controle_negatif`, `activations_identiques_au_bit`, `lecture`, `regle_repli_appliquee` (sous `resultat`,
  `resultat.fidelite_toutes`, `resultat.tokenisation`, `resultat.empreintes_p3`). Elles sont lues par nos analyses
  scellées elles-mêmes, après le scellement de nos fiches JSON.
- Ni la session ni le script n'ouvrent les traces de l'instance (`traces/…/r1-rejeu.json` y recopie la sortie standard
  du module, P-R5 comprise), ni la ligne de journal `etape=fin fideles=… notees=…`. Le message de versement ne doit pas
  la relayer ; s'il le fait, la session le déclare au registre (« vu avant les analyses ») et aux lecteurs R13.

## 7. Règles

- **Épisodes non inversibles déclarés : aucun** (liste vide fixée : E2, E19). **N-A : sans objet** pour le lecteur R13 de
  la principale (E19 ; concordance `8482b4cd…` § 7 ; aucune décision nouvelle de Lazar).
- **Réserve sur HG-2** (addendum v3, « Hypothèse » et ligne ajoutée des critères gelés ; verdict `64fab1a5…`) : rapportée
  à côté des résultats, sans changer aucune classe.
- **Arrêt de la course** : `diag/<run>/arret.json` seul (aucun `donnees/<run>`) ; seuls `verdict_fidelite` (motif fermé :
  « non conforme » → `rejeu_non_conforme`, « echec » → `rejeu_en_echec`) et le rattachement sont lus ; fiches `R1: null`
  avec ce motif ; les contrôles du manifeste (section 3) valent aussi pour un run arrêté.
- **Reprise E21** (une seule, erreur d'infrastructure, aucun fichier d'activations écrit) : le message de versement nomme
  la course arrêtée, l'empreinte de son `arret.json` s'il existe et le message d'annonce de la reprise, fait avant la
  création ; la branche source est alors `calcul/r1-relance-v3-reel-v2` ; la course arrêtée est notée dans
  les fiches JSON, rien n'en est ouvert ; on lit la seule course nommée ; mêmes commit et entropie (section 3) ; les
  lignes `etape=fidelite lecture=…` et `etape=controle_negatif lecture=…` de son journal, si elles existent, vont aux
  lecteurs R13, rapportées à côté (réserve d'instrument si elles diffèrent).
- **Tout écart** à cette fiche arrête la réception : rien n'est lancé, rien n'est corrigé à la main, Lazar est prévenu
  (écart au texte scellé ou autre course : nœud). Une fiche scellée ne se réécrit pas : version nouvelle, nom nouveau.

## 8. Bloc d'attendus (lu par le mode « après le versement » ; mêmes valeurs que les sections 3 à 7)

<!-- attendus-machine : debut -->
```json
{
 "N_A": "sans objet (E19 de l'addendum v3 ; concordance § 7)",
 "arret_premiere_course_sha256": "c6671d2c9534463f82da90c21eba80f29a2bce04e898643b59a0caa4c9a9eb07",
 "branche_versement": "calcul/r1-r2-reel-v1",
 "branches_source": {
  "course": "calcul/r1-relance-v3-reel-v1",
  "reprise_e21": "calcul/r1-relance-v3-reel-v2"
 },
 "episodes_non_inversibles_declares": [],
 "fichiers_rejeu": {
  "complement": "activations-p3-rejeu-v1-complement-hors-cout.npz",
  "maximum": "activations-p3-rejeu-v1-maximum.npz",
  "moyenne": "activations-p3-rejeu-v1.npz"
 },
 "format": "attendus-reception-r1-relance-v3-v1",
 "interdits": [
  "fideles",
  "notees",
  "fideles_parmi_contextes_conformes",
  "notees_contextes_conformes",
  "egalite_exacte",
  "ecart_max",
  "ecart_mediane",
  "part_fideles_parmi_notees",
  "p_r5_au_moins_90_pour_cent",
  "fidelite_echantillon",
  "controle_negatif",
  "activations_identiques_au_bit",
  "lecture",
  "regle_repli_appliquee"
 ],
 "juges": {
  "juge3b": {
   "fichier": "scores-juge3b-p3-v1.npz",
   "run": "20261102-004328-r2-juge3b-reel",
   "sha256": "10838eea884baefd1921aa7fb6f603b288fd02d46ed177845ebbda6291cdd354"
  },
  "juge8b": {
   "fichier": "scores-juge8b-p3-v1.npz",
   "run": "20261102-005048-r2-juge8b-reel",
   "sha256": "1ebbeff89fe7ff4a6da834651b0701b0cfde8cce9781ca6e2318224d872e8d4b"
  }
 },
 "manifeste": {
  "chemin_table_tokenisation": "prereg/R1-table-tokenisation-v3.json",
  "commande": "python -m controle_ia.runs_nuit.rejeu_activations_v3",
  "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
  "config_sha256": "1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4",
  "decisif": true,
  "depot_propre": true,
  "entropie": "36410133060804533274328900142752730279",
  "preenregistrement": {
   "chemin": "prereg/R1-addendum-relance-v3.md",
   "sha256": "88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4"
  },
  "reserves": [],
  "table_tokenisation_sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
 },
 "resultat": {
  "comptes": {
   "empreintes_p3.episodes": 240,
   "empreintes_p3.trajectoires_identiques": 151,
   "fidelite_toutes.actions": 2400,
   "fidelite_toutes.conformes_longueur": 2236,
   "fidelite_toutes.contextes_conformes": 1782,
   "tokenisation.actions_non_resolues": 0,
   "tokenisation.corrections_par_methode": {
    "copie": 0,
    "deux_fenetres": 0,
    "deux_fins_et_paire": 0,
    "deux_paires": 2,
    "fenetre": 2,
    "fenetre_et_paire": 0,
    "fin_et_deux_paires": 0,
    "fin_et_fenetre": 0,
    "fin_et_paire": 0,
    "fins": 1,
    "identifiants": 4,
    "quatre_paires_meme_action": 0,
    "trois_paires": 1,
    "une_paire": 12
   },
   "tokenisation.corrections_verifiees_au_chargement": 22,
   "tokenisation.episodes_non_resolus": [],
   "tokenisation.fideles_parmi_non_resolues": 0,
   "tokenisation.par_methode_resolution": {
    "aucune": 218,
    "identifiants": 4,
    "v1": 15,
    "v2": 3
   },
   "tokenisation.seuil_non_conformes": 10,
   "tokenisation.signales": 22,
   "tokenisation.trajectoires_identiques_base": 129,
   "tokenisation.version_table": 3
  },
  "tokenisation.addendum": "prereg/R1-addendum-relance-v2.md",
  "tokenisation.table_sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423",
  "verdict_fidelite": "conforme"
 },
 "run_premiere_course": "20261102-002114-r1-rejeu-reel",
 "textes": {
  "addendum_v3": {
   "chemin": "prereg/R1-addendum-relance-v3.md",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "88e262e26ea38a30e8acdf0cdf204cbdaba381baf3dbc352b4333d1fe6b299a4"
  },
  "amorce": {
   "chemin": "scripts/amorce_instance_r1_relance_v3.sh",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "82f386876d3e606e6d8d7d6c388e42a822266d7cf899d448991b8af456badef7"
  },
  "concordance_b2": {
   "chemin": "brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/concordance-addendum-r1-v3-brouillon2-v1.md",
   "commit": "2bd8147d409ab277c312c62012045875e66c165e",
   "sha256": "8482b4cd39348104e80187b1470001f71fc6d857fc75344a32529b6dd37ade0b"
  },
  "configuration_v5": {
   "chemin": "prereg/R1-rejeu-config-v5.json",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "acad6253f3c9f4d93c45a453ae8f5dcb122049a979cf43000d47c5f9c1edd4b8",
   "sha256_canonique": "1cfb7fba9518ff81484153e0e9cc6dd974941b7d985775f026e61a80687627d4"
  },
  "manifeste_py": {
   "chemin": "src/controle_ia/manifeste.py",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d"
  },
  "module_v3": {
   "chemin": "src/controle_ia/runs_nuit/rejeu_activations_v3.py",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "0581cf9a32e054e5044809f80078e3d33e3de27a22830e40ca8aa45a03ca2adc"
  },
  "par_episode": {
   "chemin": "prereg/analyse-par-episode-v1.md",
   "commit": "2bd8147d409ab277c312c62012045875e66c165e",
   "sha256": "26a3ff72e3a39636d3bdb965971fd1b237a04acc133a31a42f9a695d6d5970a4"
  },
  "parent": {
   "chemin": "prereg/R1-R2-rejeu-p3-v1.md",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "80c85a0085f444dc10f36e4e226d015802d2e20294c4fff2ae67adb0aca4ddea"
  },
  "principale": {
   "chemin": "prereg/analyse-principale-r1-r2-v1.md",
   "commit": "83ce7a91f681b36668a9f91424d53ebd632b50b1",
   "sha256": "8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537"
  },
  "procedure_v1": {
   "chemin": "brouillons/preuves-mentors-v1/reception-r1-relance-v1/procedure-reception-lecture-r1-relance-v1.md",
   "commit": "2bd8147d409ab277c312c62012045875e66c165e",
   "sha256": "d85bd5e467ef9a735db05afb661093e5513db7925eb9d1a573154c4fc13ff01b"
  },
  "reserve_n2": {
   "chemin": "brouillons/preuves-mentors-v1/analyse-blanche-noire-v3/reserve-N2-bras-moyenne-v1.md",
   "commit": "2bd8147d409ab277c312c62012045875e66c165e",
   "sha256": "c82b4d009cbfcdf34ceeaeb5870fb8b5f76dbfc40bb4cfce90a792f1b12aae42"
  },
  "script_instance": {
   "chemin": "scripts/r1_relance_instance_v3.sh",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "24744794808832e30cb8fa47c45a19de5a530d5ce06db1bd0557a17d3e35e4eb"
  },
  "secondaire": {
   "chemin": "prereg/analyse-blanche-noire-v3.md",
   "commit": "7a238666630a6d6dca064e8da6b309320060200d",
   "sha256": "1f6a6da2c551060a5f90ff3358b0aaf276dd9f336a5b953e6d93233c8c581fa9"
  },
  "table_v3": {
   "chemin": "prereg/R1-table-tokenisation-v3.json",
   "commit": "139a81d37fbd2255aff8d27698f84b47b9433221",
   "sha256": "ead8a66851b2af5dfa02635297056872032878fbd2987ba780fb6c9096766423"
  },
  "verdict_graine": {
   "chemin": "brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md",
   "commit": "2bd8147d409ab277c312c62012045875e66c165e",
   "sha256": "64fab1a5854deba0ad669d0c4840b6736e9cb680a22928d548c63093bb273e68"
  }
 }
}
```
<!-- attendus-machine : fin -->
