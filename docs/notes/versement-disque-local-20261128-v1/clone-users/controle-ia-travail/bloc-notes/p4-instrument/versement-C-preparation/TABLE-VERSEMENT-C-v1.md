# Table du versement C de P4-instrument — v1

Préparateur neuf, session 16, 2026-10-21 vers 00:45 UTC. Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (lien vers le bloc-notes).
Consigne : `…/consigne-preparateur-versement-C-v1.md` (`f6c6c1ec…`, sceau conforme). Dépôt `R` =
`/home/user/controle-ia-travail`, lu seulement (tête `0a44ee6139b14887fc38da8db429a46d41b300d4`, arbre suivi propre) ;
rien n'y a été écrit, aucune commande git d'écriture.

Lu pour établir la liste : `…/chaine-v3/sceller_p4_v1.sh`, `…/chaine-v3/controles_avant_depense_p4_v1.sh`,
`…/chaine-v3/verifications_p4_v1.py` (`RAPPORTS_NOMS`, `CHEMIN_MODULE`, `preuves`), `…/plan-code-et-chaine-v2.md`
(`7c65e4f6…`, sceau conforme), `…/P4-instrument-v1-candidat1.md` (`6422fb45…`, sceau conforme ; chemins cités),
`…/traitement-verification-fidelite-chaine-v2-P4-v1.md` (`dde35f6f…`, sceau conforme ; liste de 27 noms),
`…/traitement-verifications-chaine-v2-P4-v1.md` (sources des noms renommés), `R/src/controle_ia/scellement.py`
(format des sceaux, dossiers de `verifier-arbre`), `R/.gitignore`. `…/chaine-v3/NOTES-CHAINE-v3.md` et
`…/chaine-v3/RAPPORT-CORRECTION-v1.md` **n'existent pas** (`ls` du dossier nommé, R11) : rien à lire.

Arbre de préparation : `…/versement-C-preparation/arbre/` (chemins du dépôt). Pièce dont le nom final n'est pas
encore fixé : `…/versement-C-preparation/pieces-a-nommer/`. Liste des chemins prêts (pièces et sceaux) :
`…/versement-C-preparation/liste-chemins-C-prets-v1.txt`. État machine : `…/versement-C-preparation/etat-pieces-v1.json`.
Outils : `…/versement-C-preparation/outils/preparer_arbre_c_v1.py`, `…/versement-C-preparation/outils/ecrire_table_c_v1.py`.
Chaque copie a l'empreinte de sa source (relue après copie) et un sceau `<hex>  <nom final>` ; les 32 pièces de
l'arbre et la pièce à nommer passent `sha256sum -c` dans leur dossier.

## Ce que C contient

C = **58 pièces + 58 sceaux = 116 chemins** :

- `prereg/contre-lectures/` : les 27 noms de `RAPPORTS_NOMS` de la chaîne v4 (liste du traitement `dde35f6f…`) ;
- `docs/procedures/P4-instrument-v1/` : les six fichiers du module de P4 (`MODULE_P4`, lignes « Module de P4 ») et les
  21 scripts de la chaîne (`CHAINE` de `sceller_p4_v1.sh`), chacun avec son sceau (`scellement verifier` les exige ;
  `verifier-arbre` couvre `docs/` et `prereg/`) ;
- `donnees/P4-tokeniseur-v1/` : `tokenizer.json` (`79e3e522…`) et `tokenizer_config.json` (`177c7b61…`) avec leurs
  sceaux (bloc 10 des contrôles : `git show S:…` et `S:….sha256` égal à « `<hex>  <nom>` ») ;
- `brouillons/` : le texte relu (`CANDIDAT_RELU_CHEMIN` = `brouillons/P4-instrument-v1-candidat<k>.md`) et la
  configuration relue (`CONFIG_RELUE_CHEMIN` = `brouillons/P4-instrument-config-v1-candidat<k>.json`), avec leurs sceaux
  à la ligne exacte (le scellement et le bloc 5 les relisent ; la répétition jouet sur le vrai C répète ce candidat).

**État : 32 pièces prêtes dans l'arbre (64 chemins) ; 1 pièce prête de contenu mais sans nom final (la
configuration) ; 25 pièces en attente** (21 scripts de la chaîne v4, 3 rapports ou candidat, le texte final).

## Table

| # | chemin dans le dépôt | source dans le bloc-notes | empreinte | état | contrôle de la source |
|---|---|---|---|---|---|
| 1 | `prereg/contre-lectures/contre-lecture-R2-P4-instrument-brouillon1-v1.md` (+ `.sha256`) | `…/contre-lecture-R2-P4-instrument-brouillon1-v1.md` | `108a8d1ffd0a892c123608af237c824e2bc40545d4e54e5e5b7dcb9a37835420` | prêt | compagnon de la source : absent ; empreinte citée : égale |
| 2 | `prereg/contre-lectures/traitement-R2-P4-instrument-brouillon1-v1.md` (+ `.sha256`) | `…/traitement-R2-P4-instrument-brouillon1-v1.md` | `876d1a66c317ab662da1f63b1be76e764506fa3090da0eded7cee5ce2bcb253d` | prêt | compagnon de la source : conforme |
| 3 | `prereg/contre-lectures/traitement-gemini-014-P4-instrument-v1.md` (+ `.sha256`) | `…/traitement-gemini-014-P4-instrument-v1.md` | `a61cfd3c21b02be67408e44d50548b3984737fe8fffd58a3d1d6a7e699ffbb36` | prêt | compagnon de la source : conforme |
| 4 | `prereg/contre-lectures/verification-corrections-brouillons2-3-P4-v1.md` (+ `.sha256`) | `…/verification/verification-corrections-brouillons2-3-P4-v1.md` | `9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 5 | `prereg/contre-lectures/traitement-verification-P4-instrument-v1.md` (+ `.sha256`) | `…/traitement-verification-P4-instrument-v1.md` | `53e7c0f2e8e9867c42e603897a54bc4b895eaffc2b4d979c75379443f77228dd` | prêt | compagnon de la source : conforme |
| 6 | `prereg/contre-lectures/contre-lecture-3-P4-instrument-candidat1-v1.md` (+ `.sha256`) | `…/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` | `7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368` | prêt | compagnon de la source : conforme |
| 7 | `prereg/contre-lectures/relecture-chaine-depense-P4-instrument-v1.md` (+ `.sha256`) | `…/relecture-chaine-depense/relecture-chaine-depense-v1.md` | `b6e43dd7a981d3dabc214127787ea245f976731763963d8d31a59543794f3c5b` | prêt | compagnon de la source : conforme |
| 8 | `prereg/contre-lectures/relecture-chaine-donnees-P4-instrument-v1.md` (+ `.sha256`) | `…/relecture-chaine-donnees/relecture-chaine-donnees-v1.md` | `184b8926fe320f25f31014291fead8cd29b72efed5bd107ee97eacac5d9e7733` | prêt | compagnon de la source : conforme |
| 9 | `prereg/contre-lectures/relecture-chaine-fidelite-P4-instrument-v1.md` (+ `.sha256`) | `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md` | `923c71d87115cf114d16c8079adce4dd79aa3ca112bcf9224ad6b9088cb988c5` | prêt | compagnon de la source : conforme |
| 10 | `prereg/contre-lectures/traitement-CL3-et-relectures-chaine-P4-v1.md` (+ `.sha256`) | `…/traitement-CL3-et-relectures-chaine-P4-v1.md` | `4678a01b07bd8885169b8a77ac12381ab21763632bed48758da94a00f001b5d8` | prêt | compagnon de la source : conforme |
| 11 | `prereg/contre-lectures/verification-module-v2-contournement-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md` | `2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d` | prêt | compagnon de la source : conforme |
| 12 | `prereg/contre-lectures/verification-module-v2-fidelite-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md` | `ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196` | prêt | compagnon de la source : conforme |
| 13 | `prereg/contre-lectures/traitement-verifications-module-v2-P4-v1.md` (+ `.sha256`) | `…/traitement-verifications-module-v2-P4-v1.md` | `32d50abec952df70bd53980f28b93a5483e10c0c0f71d33a54a3006f5b2ba4b4` | prêt | compagnon de la source : conforme |
| 14 | `prereg/contre-lectures/verification-module-v3-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-module-v3/verification-module-v3-v1.md` | `86577f3d6d5b2c9edf7d893a041ebcd11d8322f2645c3337a545dfa5a881038f` | prêt | compagnon de la source : conforme |
| 15 | `prereg/contre-lectures/verification-chaine-v2-depense-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` | `488a7e717e6b2e96e28dca0c79ef062738e79defc9c08e4a0b4507119602a00a` | prêt | compagnon de la source : conforme ; empreinte citée : égale (préfixe) |
| 16 | `prereg/contre-lectures/verification-chaine-v2-donnees-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` | `16298dd2676e512bcfbca0b0c35d74312f87c2dae3a436e53ce40657dfb64b08` | prêt | compagnon de la source : conforme ; empreinte citée : égale (préfixe) |
| 17 | `prereg/contre-lectures/verification-chaine-v2-fidelite-P4-instrument-v1.md` (+ `.sha256`) | `…/verification-chaine-v2-fidelite/verification-chaine-v2-fidelite-v1.md` | `4e92c3deed0df22b76ebffd16997c8b9e0e471783b54567313385457c4392da4` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 18 | `prereg/contre-lectures/traitement-verifications-chaine-v2-P4-v1.md` (+ `.sha256`) | `…/traitement-verifications-chaine-v2-P4-v1.md` | `10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 19 | `prereg/contre-lectures/traitement-verification-fidelite-chaine-v2-P4-v1.md` (+ `.sha256`) | `…/traitement-verification-fidelite-chaine-v2-P4-v1.md` | `dde35f6f8def8a43c0def9ca98c432b34bb472893bc0c8a2602327ebc4c6c898` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 20 | `prereg/contre-lectures/verification-chaine-v4-P4-instrument-v1.md` (+ `.sha256`) | — | — | attend : vérification de la chaîne v4 | — |
| 21 | `prereg/contre-lectures/verification-candidat2-P4-instrument-v1.md` (+ `.sha256`) | — | — | attend : vérification du candidat 2 | — |
| 22 | `prereg/contre-lectures/P4-instrument-v1-brouillon1.md` (+ `.sha256`) | `…/P4-instrument-v1-brouillon1.md` | `41e5f035616e7cd3a233b680af06ba2a97c517a41d92f2042fde746aa85a48fd` | prêt | compagnon de la source : absent ; empreinte citée : égale |
| 23 | `prereg/contre-lectures/P4-instrument-v1-brouillon2.md` (+ `.sha256`) | `…/P4-instrument-v1-brouillon2.md` | `ab409206c90dd489cb4efcd032d2c81d6eeadc459f28fb8d6cedcdb94f25ff63` | prêt | compagnon de la source : conforme |
| 24 | `prereg/contre-lectures/P4-instrument-v1-brouillon3.md` (+ `.sha256`) | `…/P4-instrument-v1-brouillon3.md` | `2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 25 | `prereg/contre-lectures/P4-instrument-v1-brouillon4.md` (+ `.sha256`) | `…/P4-instrument-v1-brouillon4.md` | `32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6` | prêt | compagnon de la source : conforme |
| 26 | `prereg/contre-lectures/P4-instrument-v1-candidat1.md` (+ `.sha256`) | `…/P4-instrument-v1-candidat1.md` | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` | prêt | compagnon de la source : conforme |
| 27 | `prereg/contre-lectures/P4-instrument-v1-candidat2.md` (+ `.sha256`) | — | — | attend : candidat 2 relu | — |
| 28 | `docs/procedures/P4-instrument-v1/mesures_conception_p4_v1.py` (+ `.sha256`) | `…/module-v3/mesures_conception_p4_v1.py` | `483b8ac3aca65a9879b7d2f2a832cfd5478c48fd860c94a6fbdc041364cc8be7` | prêt | compagnon de la source : conforme |
| 29 | `docs/procedures/P4-instrument-v1/instrument_p4_v1.py` (+ `.sha256`) | `…/module-v3/instrument_p4_v1.py` | `000281d02c17779937b0033c2e1c724f05548b3f3eaf1ee3cfa94da74afafb8c` | prêt | compagnon de la source : conforme |
| 30 | `docs/procedures/P4-instrument-v1/lecture_p4_v1.py` (+ `.sha256`) | `…/module-v3/lecture_p4_v1.py` | `0b7a259bc95e8a7fb6c994076d2be72ada47a1d10e9f5d28597afbb14674682a` | prêt | compagnon de la source : conforme |
| 31 | `docs/procedures/P4-instrument-v1/test_instrument_p4_v1.py` (+ `.sha256`) | `…/module-v3/test_instrument_p4_v1.py` | `9d015be4ce2bbff4a4541387d5d19ef70497aa41f1a53b9c38724360d7a1dffd` | prêt | compagnon de la source : conforme |
| 32 | `docs/procedures/P4-instrument-v1/test_lecture_p4_v1.py` (+ `.sha256`) | `…/module-v3/test_lecture_p4_v1.py` | `305a2e9faf90dd09a48992f76c2ae1a96c8a79d86244b71cd27109698b87f384` | prêt | compagnon de la source : conforme |
| 33 | `docs/procedures/P4-instrument-v1/test_gardes_p4_v1.py` (+ `.sha256`) | `…/module-v3/test_gardes_p4_v1.py` | `014a9f85a663602bfeafac809ced04df7ce23ff864a432888822acf9ca397147` | prêt | compagnon de la source : conforme |
| 34 | `docs/procedures/P4-instrument-v1/verifications_p4_v1.py` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 35 | `docs/procedures/P4-instrument-v1/controles_avant_depense_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 36 | `docs/procedures/P4-instrument-v1/lancer_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 37 | `docs/procedures/P4-instrument-v1/sceller_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 38 | `docs/procedures/P4-instrument-v1/surveiller_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 39 | `docs/procedures/P4-instrument-v1/controle_cinq_minutes_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 40 | `docs/procedures/P4-instrument-v1/arreter_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 41 | `docs/procedures/P4-instrument-v1/recuperation_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 42 | `docs/procedures/P4-instrument-v1/controler_traces_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 43 | `docs/procedures/P4-instrument-v1/repetition_jouet_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 44 | `docs/procedures/P4-instrument-v1/repetition_finale_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 45 | `docs/procedures/P4-instrument-v1/essais_lanceur_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 46 | `docs/procedures/P4-instrument-v1/essais_controles_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 47 | `docs/procedures/P4-instrument-v1/essais_scellement_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 48 | `docs/procedures/P4-instrument-v1/essais_surveillance_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 49 | `docs/procedures/P4-instrument-v1/essais_arret_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 50 | `docs/procedures/P4-instrument-v1/essais_traces_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 51 | `docs/procedures/P4-instrument-v1/essais_verifications_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 52 | `docs/procedures/P4-instrument-v1/outils_essais_p4_v1.py` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 53 | `docs/procedures/P4-instrument-v1/amorce_instance_p4_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 54 | `docs/procedures/P4-instrument-v1/p4_instance_v1.sh` (+ `.sha256`) | — | — | attend : chaîne v4 | — |
| 55 | `donnees/P4-tokeniseur-v1/tokenizer.json` (+ `.sha256`) | `…/tokeniseur/tokenizer.json` | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` | prêt | compagnon de la source : conforme ; empreinte citée : égale |
| 56 | `donnees/P4-tokeniseur-v1/tokenizer_config.json` (+ `.sha256`) | `…/tokeniseur/tokenizer_config.json` | `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424` | prêt | compagnon de la source : absent ; empreinte citée : égale |
| 57 | `brouillons/P4-instrument-v1-candidat<k>.md` (+ `.sha256`) | — | — | attend : vérification du candidat 2 (texte final, postérieur au rapport ; nom k à fixer) | — |
| 58 | `brouillons/P4-instrument-config-v1-candidat<k>.json` (+ `.sha256`) | `…/P4-instrument-config-v1.json` | `76d10700d860e2fd99053fdb672a24fb6a80260cfbfbe331323c836d10ac270e` | prêt (contenu) ; nom k à fixer avec le texte final | compagnon de la source : absent |

Abréviations de la colonne « contrôle » : « compagnon de la source : conforme » = le `.sha256` posé à côté de la source
porte cette empreinte et le nom de la source ; « absent » = aucun compagnon à côté de la source (provenance par la seule
citation) ; « empreinte citée : égale » = égale à l'empreinte écrite par le candidat 1, un traitement ou la consigne.
Contrôles croisés faits en plus (préfixes cités) : `7f947de0` (contre-lecture 3), `b6e43dd7`, `184b8926`, `923c71d8`
(relectures de la chaîne v1) cités par `traitement-CL3-et-relectures-chaine-P4-v1.md` ; `2ce3d0af`, `ea12d4a2`,
`86577f3d` (vérifications du module) cités par `traitement-verifications-module-v2-P4-v1.md` ; `ab409206` (brouillon 2)
cité par le candidat 1 ; `32d821fb` (brouillon 4) et `6422fb45…` (candidat 1) cités par la contre-lecture 3. Les six
empreintes du module v3 sont celles que cite l'essai du candidat 2 (`…/candidat2/essai-candidat2-complet.md`).
Configuration : empreinte brute `76d10700…`, empreinte canonique (`config_canonique` du dépôt) `7905a18a…`, égale à
celle que citent le candidat 1 et l'essai du candidat 2.

## Hors de C (pour mémoire, aucune copie préparée)

- Déjà suivis à la tête de `main` : `docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json`,
  `…-v2-controle.json` et leurs sceaux (relus par les contrôles, blocs 8 à 10). Rien à verser.
- Après C, avant S (commit des preuves) : `docs/procedures/P4-instrument-v1/repetition-jouet-p4-v1.log`
  (`REPETITION_JOUET_CHEMIN`) et les huit journaux de `PREUVES_EXIGEES` (`banc-lanceur`, `banc-surveillance`,
  `banc-arret`, `banc-traces`, `banc-verifications`, `banc-controles`, `banc-scellement`, `repetition-finale`, tous
  `-p4-v1.log`), chacun avec son sceau : ils sont produits **sur** le vrai C. Les journaux `banc-*.log` et
  `repetition-jouet-p4-v1.log` de `…/chaine-v3/` sont ceux de la chaîne v3 : ni à verser, ni à réutiliser.
- Commit S (écrit par `sceller_p4_v1.sh`) : `prereg/P4-instrument-v1.md`, `prereg/P4-instrument-config-v1.json` et
  leurs sceaux. Ils ne doivent pas exister avant (R12 ; le scellement s'arrête sinon).

## Pièces manquantes ou ambiguës

1. **Texte final et 27ᵉ nom : deux fichiers distincts (point bloquant si on les confond).** Le bloc 7 des contrôles et le
   scellement exigent que le texte scellé cite chaque rapport sous la forme « `prereg/contre-lectures/<nom>`
   (`<empreinte>`) », y compris `P4-instrument-v1-candidat2.md`. Un texte ne peut pas citer sa propre empreinte : le
   fichier versé sous `prereg/contre-lectures/P4-instrument-v1-candidat2.md` est donc forcément **le candidat 2 vérifié**,
   et le texte relu épinglé (`brouillons/P4-instrument-v1-candidat<k>.md`, copié tel quel en `prereg/P4-instrument-v1.md`
   par S) est un **autre** fichier, postérieur au rapport `verification-candidat2-P4-instrument-v1.md` (règle écrite au
   traitement `dde35f6f…`). Son nom n'est fixé nulle part : `k` = 2 donnerait deux fichiers différents de même nom de base
   (`brouillons/` et `prereg/contre-lectures/`), contraire à l'esprit de R12 ; `k` = 3 (« texte final ») est la lecture
   la plus sûre. À trancher par une décision écrite avant les épingles. Le libellé « candidat 2 relu » de la consigne
   recouvre ces deux fichiers.
2. **Configuration relue : contenu prêt, nom absent.** `…/P4-instrument-config-v1.json` (`76d10700…`, sans compagnon à la
   source) doit être versée sous `brouillons/P4-instrument-config-v1-candidat<k>.json`, même `k` que le texte final ;
   copie faite sous `…/versement-C-preparation/pieces-a-nommer/P4-instrument-config-v1.json` avec un sceau à ce nom, à
   **resceller** sous le nom final (commandes, étape 0c). Si le candidat 2 ou le texte final change la configuration,
   cette copie ne vaut plus.
3. **Sources sans compagnon** (provenance par citation seulement, empreintes égales) : `…/contre-lecture-R2-P4-instrument-
   brouillon1-v1.md` (`108a8d1f…`, cité par le candidat 1), `…/P4-instrument-v1-brouillon1.md` (`41e5f035…`, cité par le
   candidat 1), `…/tokeniseur/tokenizer_config.json` (`177c7b61…`, cité par les contrôles et la consigne), la
   configuration (empreinte canonique égale à la citation). Aucune n'est ambiguë ; le sceau est écrit à la copie.
4. **Noms renommés au versement** (une seule source chacun, empreinte égale à la citation des traitements) : rapports 7 à
   9, 11, 12, 14 à 17 (`…/<dossier>/<nom>-v1.md` → `<nom>-P4-instrument-v1.md`). Aucune autre source de même rôle dans les
   dossiers nommés lus.
5. **Chaîne v3 encore à 26 noms.** `…/chaine-v3/verifications_p4_v1.py` porte `verification-chaine-v3-P4-instrument-v1.md`
   et 26 noms ; l'arbre suit la liste de 27 (v4). La chaîne v4 doit porter les 27 noms (et `RAPPORTS_CONNUS` de
   `outils_essais_p4_v1.py`) ; contrôle à l'étape 1c. Si une chaîne v5 vient, le nom 20 change par décision écrite.
6. **Module : empreintes du candidat 1 périmées.** Le candidat 1 cite pour `instrument_p4_v1.py`, `lecture_p4_v1.py`,
   `test_lecture_p4_v1.py` et `test_gardes_p4_v1.py` des empreintes (`6e0e026e…`, `51a25e30…`, `49441971…`,
   `f4f97029…`) autres que celles du module v3 versé (`000281d0…`, `0b7a259b…`, `305a2e9f…`, `014a9f85…`) ; attendu (le
   candidat 1 est versé comme pièce de contre-lecture, pas comme texte), mais le texte final doit citer les six empreintes
   v3 de l'arbre, sinon `exiger_module_cite` refuse.
7. **`donnees/` est ignoré par `R/.gitignore`** : `git add` simple refuse les deux fichiers du tokeniseur ; il faut
   `git add -f` sur ces seuls chemins (étape 4). `verifier-arbre` ne couvre pas `donnees/` : leurs sceaux ne sont relus
   que par les contrôles (bloc 10) et par l'étape 3.
8. **Non vérifié par consigne** : l'absence de `donnees/P4-tokeniseur-v1/` dans `R` (rien n'est lu sous `R/donnees/`) ;
   l'étape 1d le vérifie avant copie et arrête si un chemin existe. Les sous-dossiers de `R/prereg/contre-lectures/`
   (huit, tous nommés « …P3… ») n'ont pas été listés (consigne : `ls` de ce seul dossier) ; or les contrôles listent
   l'arbre de S **récursivement** (`git ls-tree -r`) : l'étape 1e le vérifie.
9. **Pièces non exigées, non copiées** : `…/module-v3/NOTES-MODULE.md`, `NOTES-MODULE-v2.md`, `NOTES-MODULE-v3.md`,
   `RAPPORT-CORRECTION-v1.md` (aucun script ne les exige ; le candidat 1 les nomme comme pièces à donner au
   contre-lecteur). Les verser est un choix de la session (sous `docs/procedures/P4-instrument-v1/`, avec sceaux ; sans
   effet sur la famille « P4 » de `prereg/contre-lectures/` ni sur `exiger_module_cite`, qui lit les lignes du texte).

## Conflits de noms sous `R/prereg/contre-lectures/`

`ls` de ce seul dossier : 274 entrées au premier niveau (fichiers et huit sous-dossiers), **aucune dont le nom contient
« P4 »** ; aucun des 27 noms n'existe déjà. Aucun conflit avec la famille « P4 » exigée par les contrôles et le
scellement (`grep -E '/[^/]*P4[^/]*$'` sur les noms). Réserve : sous-dossiers non listés (point 8).

## Commandes de versement (pour la session ; non jouées)

```bash
H=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument
PREP=$H/versement-C-preparation; A=$PREP/arbre; R=/home/user/controle-ia-travail
H4=$H/chaine-v4                       # dossier de la chaîne v4 vérifiée (à confirmer)
K=3                                   # k du texte final (décision écrite, point 1)
SRC_VC4=…/verification-chaine-v4-P4-instrument-v1.md         # sources à fixer à leur arrivée
SRC_VCAND2=…/verification-candidat2-P4-instrument-v1.md
SRC_CAND2=…/P4-instrument-v1-candidat2.md                    # candidat 2 vérifié (pas le texte final)
SRC_TEXTE=…/P4-instrument-v1-candidat$K.md                   # texte final
CHAINE="verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
 controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh repetition_jouet_p4_v1.sh
 repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh essais_scellement_p4_v1.sh
 essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh essais_verifications_p4_v1.sh
 outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh"
poser() {   # $1 source, $2 chemin dans le dépôt : copie sans écraser, sceau au nom final
    [ -e "$A/$2" ] && { echo "existe déjà : $2"; return 1; }
    mkdir -p "$A/$(dirname "$2")" && cp "$1" "$A/$2" && (cd "$A/$(dirname "$2")" && sha256sum "$(basename "$2")" > "$(basename "$2").sha256")
}

# (à jouer comme un script bash : chaque « exit 2 » arrête tout)
# 0. compléter l'arbre quand les pièces existent
for s in $CHAINE; do poser "$H4/$s" "docs/procedures/P4-instrument-v1/$s" || exit 2; done           # 0a
poser "$SRC_VC4" prereg/contre-lectures/verification-chaine-v4-P4-instrument-v1.md || exit 2         # 0b
poser "$SRC_VCAND2" prereg/contre-lectures/verification-candidat2-P4-instrument-v1.md || exit 2
poser "$SRC_CAND2" prereg/contre-lectures/P4-instrument-v1-candidat2.md || exit 2
poser "$SRC_TEXTE" "brouillons/P4-instrument-v1-candidat$K.md" || exit 2                              # 0c
poser "$PREP/pieces-a-nommer/P4-instrument-config-v1.json" "brouillons/P4-instrument-config-v1-candidat$K.json" || exit 2
cmp -s "$SRC_TEXTE" "$A/prereg/contre-lectures/P4-instrument-v1-candidat2.md" && { echo "texte final = candidat 2 versé : citation impossible (point 1)"; exit 2; }
L=$PREP/liste-chemins-C-v1.txt; [ -e "$L" ] && { echo "$L existe déjà"; exit 2; }                    # 0d
{ cat "$PREP/liste-chemins-C-prets-v1.txt"
  for s in $CHAINE; do printf 'docs/procedures/P4-instrument-v1/%s\ndocs/procedures/P4-instrument-v1/%s.sha256\n' "$s" "$s"; done
  for n in verification-chaine-v4-P4-instrument-v1.md verification-candidat2-P4-instrument-v1.md P4-instrument-v1-candidat2.md; do
      printf 'prereg/contre-lectures/%s\nprereg/contre-lectures/%s.sha256\n' "$n" "$n"; done
  for f in "brouillons/P4-instrument-v1-candidat$K.md" "brouillons/P4-instrument-config-v1-candidat$K.json"; do printf '%s\n%s.sha256\n' "$f" "$f"; done
} | sort -u > "$L"
[ "$(wc -l < "$L")" = 116 ] || { echo "liste : $(wc -l < "$L") chemins, 116 attendus"; exit 2; }

# 1. contrôles avant copie
while read -r f; do case $f in *.sha256) continue;; esac                                             # 1a sceaux de l'arbre
    (cd "$A/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || { echo "sceau KO : $f"; exit 2; }
done < "$L"
diff <(cd "$A" && find . -type f | sed 's|^\./||' | sort) "$L" || { echo "arbre ≠ liste"; exit 2; }   # 1b
python3 -B "$H4/verifications_p4_v1.py" rapports $(cd "$A/prereg/contre-lectures" && for f in *.md; do  # 1c 27 noms exacts
    printf '%s=%s ' "$f" "$(sha256sum "$f" | cut -d' ' -f1)"; done) || exit 2
cd "$R" || exit 2                                                                                     # 1d dépôt prêt
[ "$(git remote get-url origin)" = https://github.com/lciric/controle-ia-travail.git ] || [ "$(git remote get-url origin)" = https://github.com/lciric/controle-ia-travail ] || exit 2
git fetch -q origin main && [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] && [ -z "$(git status --porcelain --untracked-files=no)" ] || exit 2
while read -r f; do [ -e "$R/$f" ] && { echo "existe déjà dans le dépôt : $f"; exit 2; }; done < "$L"
[ -z "$(git ls-files prereg/contre-lectures/ | grep -E '/[^/]*P4[^/]*$')" ] || { echo "famille P4 déjà présente"; exit 2; }   # 1e

# 2. copie de l'arbre dans le dépôt (sans écraser)
while read -r f; do mkdir -p "$R/$(dirname "$f")" && cp -n "$A/$f" "$R/$f" || exit 2; done < "$L"

# 3. sceaux dans le dépôt, arbre scellé
while read -r f; do case $f in *.sha256) continue;; esac
    (cd "$R/$(dirname "$f")" && sha256sum -c --quiet "$(basename "$f").sha256") || { echo "sceau KO dans le dépôt : $f"; exit 2; }
done < "$L"
PYTHONPATH=src python -B -m controle_ia.scellement verifier-arbre . | tail -1 | grep -qx "arbre intact" || exit 2

# 4. git add des seuls chemins listés (donnees/ est ignoré : -f sur ces chemins seulement)
grep -v '^donnees/' "$L" | xargs git add --
grep '^donnees/' "$L" | xargs git add -f --
diff <(git diff --cached --name-only --no-renames | sort) "$L" || { echo "index ≠ liste"; exit 2; }
[ "$(git diff --cached --name-only --diff-filter=A | wc -l)" = 116 ] || { echo "un chemin n'est pas un ajout"; exit 2; }
# commit C (message de la session, attribution des consignes), puis poussée vers le dépôt de travail seulement :
# git commit -F <message> && git push origin HEAD:main
```
