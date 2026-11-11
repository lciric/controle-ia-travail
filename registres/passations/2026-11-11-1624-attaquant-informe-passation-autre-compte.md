# Passation — session « attaquant informé » successeur → nouvelle session sur un autre compte — 11 novembre 2026, 16:24 UTC

Session `session_013QMaykGXY4fZmZNX5fm1K4`, branche `claude/compassionate-meitner-d4ryyk`, tête `f00a7155`. Quota
hebdomadaire de ce compte en zone d'alerte. Mot de Lazar, verbatim : « on va le lancer depuis un autre compte now, fais
la passation a une nouvelle session sur un autre compte ». Ne se réécrit pas (R12). Complète les passations d'étape du
10 novembre (12:31, 14:34) et du 11 novembre (`c0075ed9…`).

## Ce que la nouvelle session fait d'abord : lancer le témoin de Bailey

**Toutes les conditions de lancement sont remplies** (addendum 2, § 5) : préenregistrement `fb6c2f34…` ; addendum 1
`6f7eda73…` et addendum 2 de la règle du bras `73c8de01…` déposés chez le tiers (2026-11-11T15:46:02Z) ; **addendum 2 du
témoin** `prereg/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome.md`
(`f79459c712a0f12ecbf55c9ea787f67032031e9672e6db002b84725286c96e13`, commit `f00a7155`, pas encore déposé chez le tiers :
s'il ne l'est pas au lancement, l'ordre de lancement dit qu'il n'est daté que par son commit) ; GO `GO-2026-11-10-10`
amendé par `GO-2026-11-11-01` (licence) et `GO-2026-11-11-02` (modèle), sur `main` ; mot de lancement de Lazar (« go
lancement bailey ») ; lancement par la session qui hérite de ce rôle.

**Code** : commit `4988f3f442c670887a0e8ad15ddfbac68a173d03` ; `lanceur_v13.py` (`9257266f…`) sur le poste local ;
`instance_v12.py`, `lecture_v8.py` et les modules v3 sur l'instance (liste `lanceur_v13.CHEMINS_ARCHIVE`). Essais :
`tests/test_temoin_bailey_condition6_v13.py` (139) et `tests/test_temoin_bailey_analyse_v3.py` (36), tous passés.

**Procédure** (à vérifier contre le code avant d'agir ; l'addendum 2 fait foi) :
1. Routine R14 ; `.venv` avec `requirements-cpu.txt`, plus `hydra-core`, `pandas` et `vastai` (1.11.0) ; `git fetch` de
   `main` avec refspec explicite ; relire `GO-2026-11-10-10`, `-11-01`, `-11-02` sur `origin/main`.
2. Accès : `VAST_API_KEY` et `HF_TOKEN` (noms seulement, jamais les valeurs) dans l'environnement du compte ; `vastai
   show instances` (inventaire R14 ; 58936096, 58936099, 58936100 : arrêtées, intouchables sans mot écrit de Lazar).
3. Manifeste : `lanceur_v13.manifeste_depuis_versions_figees(<sortie>/manifeste.json,
   docs/notes/reproduction-attaque-publiee-v1/versions-figees-temoin-bailey-v1.json, commit_code="4988f3f4…" (complet),
   b=75, go_id="GO-2026-11-10-10")`.
4. Offre Vast : A100 80 Go SXM4, au moins 128 Go de mémoire vive (128 × 10⁹ octets, garde à la mise en place), au moins
   200 Go de disque, fiabilité élevée (≈ 1,1 à 1,3 USD de l'heure relevé le 11 novembre ; lecture seule par `vastai
   search offers`). Image : doit fournir Python 3.11 (versions figées), `git` et le pilote CUDA ; **vérifier contre
   `lanceur_v13.script_amorce`** avant de choisir (non éprouvé sur une vraie instance).
5. Lancement : un court script Python qui construit `lanceur_v13.Conduite(fournisseur=FournisseurVast(),
   manifeste_local=…, sortie=<dossier neuf, chemin absolu>, go_id="GO-2026-11-10-10", texte_go=texte_go_main(dépôt),
   offre=<id d'offre>, image=<image>, depot_local=<dépôt>, instances_anterieures=[])` et appelle `.conduire()`, sous
   `GO_ID=GO-2026-11-10-10` et `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`. La garde de calcul
   (`.claude/hooks/garde_calcul.py`) exige `GO_ID` sur toute commande de création. **Lancer ce script détaché**
   (`setsid nohup … &`, PID consigné) : un outil d'arrière-plan est coupé après 2 heures. Consigner l'ordre de
   lancement (GO, B, taux relevé, étiquette, `DEPOT_URL`, commit du code) dans `registres/` avant la création.
6. Pendant le run (deux à trois jours) : la session doit rester vivante ; se reprogrammer (`send_later`) au plus
   toutes les 90 minutes (le chien de garde arrête l'instance si le pilotage est muet 7 200 s) ; à chaque reprise :
   PID de la conduite vivant, bilan et journal `conduite-v5.jsonl`, dépense D. Ne jamais lire de note de sonde ni de
   juge avant la fin du run principal et le scellement de ses journaux (R1, préenregistrement).
7. Après une coupure de la session : `python -m controle_ia.temoin_bailey.lanceur_v13 reprendre --sortie <même chemin
   absolu> --etiquette <étiquette du poste> --go-id GO-2026-11-10-10 --depot <dépôt>` (lecture 38 ; même chemin absolu :
   A-1).
8. Fin : transferts comparés et scellés, instance détruite par identifiant (R10), dépense dans `registres/depenses.md`
   et `registres/arrets.md` ; verdict par un **lecteur neuf** (R13) avec `lecture_v8.valider` puis `lire`, sur les
   critères gelés ; verdict scellé, remis à Lazar.

**Risques déclarés** (addendum 2, § 4 ; lecture 22) : poste local éteint et chien mort en même temps ; arrêt par la clé
d'instance non éprouvé sur la facturation ; destructions sans transfert dans les seuls cas listés.

## Autre travail ouvert
- Pièce 3 (catalogue) : défaut (b) de la question 4 le 12 novembre vers 12:00 UTC, puis scellement final du brouillon 3
  (`dd43742c…`).
- Pièce 4 : plan et courriel v3 à remplir par Lazar.
- Courbe dose-réponse de l'organisme : attend les journaux scellés de la course réelle (`docs/notes/organisme-boucle-
  reelle-v1/course-v66/`).
- Limites connues de l'analyse (`analyse_v3`) : déclarées (addendum 1), à corriger à la prochaine version du code.

## Erreurs et expositions consignées (11 novembre)
- Note `…-1240-…` du 10 novembre : heure réelle ≈ 12:32. Message du commit `47772e37` : la v11 contient bien la borne
  budgétaire. Un scellement prématuré de l'addendum 2 de la règle (10 novembre) : retiré avant tout commit.
- Mauvaise lecture « non go dépenses », corrigée par Lazar (« go dépenses »).
- Un refus de classifieur, consigné (`…-refus-classifieur-bailey.md`) ; sa suite n'est pas reprise.

## Autres sessions
Mère : `session_01VJdZpSMxSdk2SJ1ScmdfNv` ; dépôt : `session_013QMaymMAdDjNfPoz8ySwTc` (index du bras v10, 224 pièces ;
addendum 2 du témoin en file F-003). Même compte que cette session-ci ; depuis un autre compte, le relais passe par
Lazar.

## Instances actives
Aucune créée par cette session. Aucune dépense.
