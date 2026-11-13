# Rapport du préparateur — lanceur v3 de l'atelier d'idées sur les bassins étroits — v3

Préparateur (Claude Opus 5.5), repris avec son contexte, 13 novembre 2026, de 15:35 à 16:36 UTC (heures relevées par
`date -u`). Demande de la mère reçue en cours de session, après la génération 1 en défaut. Lu : `operation-g1-v1.md`
(`3beef39eadae46939967c21cd8bb76662c617023caa94d1e7109d2c09df16040`, vérifiée), `verification-courte-lanceur-v2-v1.md`
(`ff33dd9988f5337eaef8872c818aa2c4f8ea77c289392e1c671d877d42b61d85`, vérifiée), le dossier de run
`runs/course-ideation-bassins-etroits-v2/20261113-152926-course-ideation-bassins-etroits-v2-g1/` (manifestes de départ et de fin)
et le dossier de sortie hors dépôt (code scellé, tentative de contrôle scellée, journal d'erreur de l'orchestrateur), et, pour
établir la cause, l'adaptateur du kit de l'orchestrateur (`pole/adaptateurs.py`, `construire_options`), `pole/relais.py`
(`variables_agent`) et la fusion d'environnement du kit (`claude_agent_sdk/_internal/transport/subprocess_cli.py`).
**Aucune dépense, aucun appel de modèle, aucun réseau hors de la boucle locale d'un espace réseau isolé, aucune opération git,
`.claude/` ni lu ni touché.** Aucun refus de permission ni de classifieur.

## Verdict

**Cause établie sans dépense** : la variable d'hôte **`CLAUDE_CODE_REMOTE`**, héritée de la session et transmise par le v2,
fait présenter par le kit d'agent un `Authorization: Bearer` de l'hôte au lieu du jeton factice du relais en `x-api-key` ;
le relais rend 401, le kit rend un message au modèle « <synthetic> ». La retirer seule suffit ; l'environnement du v3 (liste
de noms permis, HOME neuf) présente le jeton factice. **Lanceur v3 prêt pour une vérification courte** : essais **139
passés** ; mutations : **13 tuées sur 13** (contrôle de l'outil : 139 passed in 55.98s).

## 1. La cause, établie sans dépense

Outil : `preparateur-outils-v3/eprouver_authentification_kit_v1.py` (`06ed8d4eb6413083d55d34d1173f453236f6e2e77272f74f6c22705f2c317889`), résultat
`resultat-eprouver-authentification-kit-v1.json` (`c485ab1fdf8d643f6da93143605521584e6fe8be7a16ee2b1dba004451dd1061`). Chaque essai tourne dans `bwrap --unshare-net` (espace
réseau neuf, seule sa boucle locale existe : rien ne sort du conteneur), `/tmp` neuf (la prise de messagerie de la session
hôte est cachée), avec un **faux amont** local qui rend 401 à tout et ne note que les **noms** des en-têtes et l'**égalité** de
`x-api-key` ou d'`Authorization` au jeton factice public (`relais-local-sans-cle`) ; aucune valeur n'est écrite. Le kit
(`claude_agent_sdk` 0.2.172 et l'outil qu'il embarque) reçoit les options de l'orchestrateur pour un contrôle Claude
(`ANTHROPIC_BASE_URL` = le faux amont, `ANTHROPIC_API_KEY` = le jeton factice, sans repli de modèle, `setting_sources=[]`,
aucun outil). Le kit fusionne l'environnement hérité et ces options (`{**os.environ, …, **options.env}`) : les noms hérités
qui ne sont pas dans les options passent.

| Environnement hérité | Appels de modèle au faux amont | Authentification présentée |
|---|---|---|
| **A** : celui du v2 (session moins les noms de clé) | 1 | `Authorization: Bearer` (non factice), plus `GET /v1/code/agent-proxy/ca-cert` → **401** |
| A moins `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` ; moins `CLAUDE_CODE_USE_CCR_V2` ; moins `ANTHROPIC_*` ; moins `CCR_*` | 1 | Bearer non factice |
| A moins chacune des cinq autres `CLAUDE_CODE_REMOTE_*` | 1 à 3 | Bearer non factice |
| **A moins `CLAUDE_CODE_REMOTE` seule** | 1 | **`x-api-key` = jeton factice** ; le kit rend « AssistantMessage <synthetic> » sur le 401 du faux amont, comme le 13 novembre |
| A moins tous les `CLAUDE*` | 14 (relances du kit) | jeton factice |
| **B** : minimal (PATH, HOME, LANG) | 14 | jeton factice |
| **V3** : celui du lanceur v3 (fonction `environnement_permis`, HOME neuf) | 14 | **jeton factice** |

Avec `/root` vide (tmpfs) comme avec le vrai `/root` en lecture seule, mêmes issues pour A, B, V3 et « A moins
`CLAUDE_CODE_REMOTE*` » : le contenu de `/root/.claude` n'y est pour rien. Le « modèle servi '<synthetic>' » de l'orchestrateur
est le message que le kit fabrique sur une erreur d'authentification, pas un modèle servi. **Ce que l'épreuve ne prouve
pas** : qu'un vrai relais, avec la vraie clé, accepte ensuite la requête (la génération 1 relancée le montrera ; le premier
contrôle Claude coûte au plus 0,2 USD par modèle).

## 2. Point par point (demande de la mère)

| Point | Issue | Où (lanceur v3) | Essai qui le prouve |
|---|---|---|---|
| **1** cause sans dépense | établie : `CLAUDE_CODE_REMOTE` | outil `eprouver_authentification_kit_v1.py` | résultat scellé (tableau ci-dessus) |
| **2** environnement par liste de noms permis | `NOMS_PERMIS` = PATH, LANG, LC_ALL, TZ, TMPDIR ; HOME (dossier neuf hors dépôt, par course et par bras), GO_ID, PYTHONPYCACHEPREFIX fixés par le lanceur ; tout `ANTHROPIC_*`, `CLAUDE*`, `CCR_*`, mandataires, `NODE_OPTIONS`, clés : exclus ; aucune valeur lue hors des noms permis ; noms transmis, fixés et exclus au manifeste de départ ; un nom interdit dans la liste permise → refus. Le relais factice n'exige rien du lanceur (l'orchestrateur pose lui-même `ANTHROPIC_BASE_URL` et le jeton factice dans les options du kit) | `environnement_permis`, `executer`, `executer_bras` | `test_trois_generations_bout_en_bout` (noms vus par le faux orchestrateur, valeurs d'hôte absentes du manifeste), `test_environnement_permis`, `test_environnement_permis_artefact_nom_interdit`, `test_environnement_permis_prefixe_d_essai` ; mutant W10 |
| **3** relance étroite | une fois, si la course précédente a fini proprement (code scellé, manifeste de fin), sans aucune fiche (sortie absente, ou les trois listes scellées et vides), dépense lisible (comptée), sans bras ; jamais après des fiches ; deux courses par génération au plus ; le run du v2 est lu comme première tentative (`ANTERIEURS`) | `relance_permise`, `fiches_produites`, `runs_du_lanceur`, `depense_course` (lisible) | `test_relance_unique_apres_defaut_au_controle`, `test_relance_puis_succes`, `test_pas_de_relance_apres_des_fiches`, `test_relance_refusee_si_depense_illisible`, `test_v3_seuil_mutation_deux_courses_au_plus`, `test_fiches_produites` (5 cas), `test_run_anterieur_v2_compte_comme_premiere_tentative`, **`test_run_reel_du_v2_reconnu`** (dépôt réel : 0,275477 USD, lisible, aucune fiche, relance permise) ; mutants W2, W3, W4, W11, W12 |
| **4a** verrou (R1) | `fcntl.flock` exclusif non bloquant sur `<sorties>/.verrou-lanceur-bassins-etroits`, pris avant la lecture de l'état, rendu à la sortie (libéré même sur mort brutale, jamais hérité par le superviseur) | `prendre_verrou`, `principal` | `test_r1_verrou_deux_invocations`, `test_r1_verrou_non_herite_par_le_superviseur` ; mutant W7 |
| **4b** orphelin (R2) | le superviseur écrit l'heure de départ du processus de l'orchestrateur ; superviseur mort et orchestrateur vivant → clôture « ORCHESTRATEUR ENCORE VIVANT (PID …) », commande d'arrêt par PID, **code 4** ; ensuite, tant qu'il vit, code 4, rien ne part | `orchestrateur_orphelin`, `orphelins_vivants`, `cloturer`, `executer` | `test_r2_orchestrateur_orphelin` ; mutants W8, W9 |
| **5** quatre mutations survivantes | zombie (V2), seuil (V3), bras mort compté (V10), bras sans code scellé (V16) : essais ajoutés | — | `test_v2_zombie_tenu_pour_mort`, `test_v3_seuil_mutation_deux_courses_au_plus`, `test_v10_v16_bras_mort_compte_et_verrouille` ; mutants W1, W2, W5, W6 |
| **6** pièces épinglées inchangées ; devis | question `c188fa9a…`, faits `d19b5400…`, témoins v2 `f1ddcef9…`, enveloppe et commande d'Argon inchangés ; recoupement et son attestation lus aux mêmes chemins ; devis v3 (cumul de départ 0,275477) | `PIECES` | `test_pieces_sain_depot_reel` |
| R3 (vérification courte) | non corrigé : la fenêtre entre le détachement et le manifeste de départ reste ; tout est alors refusé (« état inconnu »), sans dépense de plus | — | — |
| R4 | corrigé : exception au détachement du bras = refus ; préfixe du cache et HOME du bras uniques | `executer_bras` | `test_r4_exception_au_detachement_du_bras` ; mutant W13 |
| R9 | corrigé : orphelins, compte rendu et clôture avant les gardes d'entrée (GO, orchestrateur, pièces) | `executer` | `test_r9_compte_rendu_apres_echeance_du_go` |
| R5 à R8 | R5 : point 5 ; R6, R7 : inchangés (témoins et attestation de relecture : pièces de la mère, déjà écrites) ; R8 : texte de la règle ci-dessous | — | — |

Essai d'emploi seulement : le faux orchestrateur lit ses réglages dans des noms `FAUX_*` ; `Reglages.prefixe_essais` (None
en production, seul « FAUX_ » admis) les laisse passer dans les essais.

## 3. Mutations du v3 (outil `preparateur-outils-v3/mutations_lanceur_v3.py`)

| Mutant | Garde affaiblie | Issue | Essais en échec (extrait) |
|---|---|---|---|
| base | aucune (contrôle de l'outil) | contrôle : tous passés |  |
| W1-zombie-tenu-pour-vivant | V2 : zombie tenu pour vivant | tué | `test_v2_zombie_tenu_pour_mort` |
| W2-courses-par-generation-non-bornees | V3 : plus de deux courses par génération | tué | `test_relance_unique_apres_defaut_au_controle`, `test_run_anterieur_v2_compte_comme_premiere_tentative` |
| W3-relance-apres-fiches | relance après des fiches | tué | `test_pas_de_relance_apres_des_fiches` |
| W4-relance-depense-illisible | relance après dépense illisible | tué | `test_relance_refusee_si_depense_illisible` |
| W5-bras-mort-non-compte | V10 : bras mort non compté | tué | `test_v10_v16_bras_mort_compte_et_verrouille` |
| W6-bras-sans-code-non-verrouillant | V16 : bras sans code scellé | tué | `test_v10_v16_bras_mort_compte_et_verrouille` |
| W7-verrou-retire | R1 : verrou | tué | `test_r1_verrou_deux_invocations` |
| W8-orphelin-ignore | R2 : orphelin ignoré | tué | `test_r2_orchestrateur_orphelin` |
| W9-orphelin-jamais-vu | R2 : orphelin jamais détecté | tué | `test_r2_orchestrateur_orphelin` |
| W10-environnement-entier | environnement entier transmis | tué | `test_environnement_permis`, `test_trois_generations_bout_en_bout` |
| W11-runs-v2-ignores | runs du v2 non lus | tué | `test_run_reel_du_v2_reconnu` |
| W12-relance-sans-fin-propre | relance sans fin propre | tué | `test_relance_refusee_sans_fin_propre_au_manifeste` |
| W13-exception-bras-non-gardee | R4 | tué | `test_r4_exception_au_detachement_du_bras` |

W12 avait survécu à une première passe (garde redondante avec « dépense lisible ») ; l'essai `test_relance_refusee_sans_fin_propre_au_manifeste` l'éprouve seule ; seconde passe : tué.

## 4. Différentiel v2 → v3

`preparateur-outils-v3/differentiel-lanceur-v2-v3.diff` (`b2951d174ee9e2e44788325638d420ff224a9d47657b6b8c72b59ea3309f43c2`, `diff -u`). Changé : en-tête ; constantes (version,
dossiers `…-v3`, `ANTERIEURS`, verrou, `MAX_COURSES_PAR_GENERATION`, `NOMS_PERMIS` ; `SEUIL_SANS_DEPENSE_USD` retiré) ;
superviseur (heure de départ de l'orchestrateur) ; `Reglages` (`anterieurs`, `prefixe_essais`) ; `environnement_sans_cles` →
`environnement_permis` ; `runs_du_lanceur` (+ `_runs_de`, versions antérieures) ; `depense_course` (rend aussi « lisible ») ;
`depense_run` ; neuves `fiches_produites`, `relance_permise`, `orchestrateur_orphelin`, `orphelins_vivants`,
`prendre_verrou` ; `etat_generation` (règle de relance) ; `cloturer` (orphelin) ; `executer` (ordre R9, code 4, HOME,
environnement) ; `executer_bras` (environnement, R4) ; `principal` (verrou). Inchangé : tout le reste du v2 (gardes de GO,
d'orchestrateur, de pièces, de sommes, de taille, règle de passage, attestations, commandes).

## 5. Épingle et règle proposées pour le v3 — génération 1 seulement (non écrites ; la mère les écrit)

Dans `.claude/settings.json`, **sous une clé `"permissions"`** au premier niveau, à côté de `"hooks"` (R8) :

```json
"permissions": {
  "allow": [
    "Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1)"
  ],
  "deny": [
    "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v3.py)",
    "Edit(//home/user/controle-ia-travail/scripts/lancer_course_ideation_bassins_etroits_v3.py.sha256)",
    "Edit(//home/user/controle-ia-travail/.claude/hooks/garde_calcul.py)"
  ]
}
```

Épingle au crochet `.claude/hooks/garde_calcul.py`, fonction sœur de `garder_lanceur_v3` (même forme), appelée dans
`decider` après elle : toute commande qui cite `lancer_course_ideation_bassins_etroits_v3` (motif borné, pour que
`tests/test_lancer_…_v3.py` n'en soit pas une) est bloquée **sauf** si elle est **exactement**
`/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v3.py 1`, lancée depuis
`/home/user/controle-ia-travail`, fichier présent et non lien, empreinte égale à la constante `3fabd71e63bf9f3e830ed5128cd6a92f04ca91c0b13dabcc0ac7d316e5f44b36` **et** au compagnon
`.sha256`. Essais du crochet : cas sain ; argument `2` (bloqué) ; octet changé ; compagnon faux ; deux arguments ; autre
interpréteur ; autre dossier. Commande du crochet passée en `python3 -I -B` (m11). Les règles du v2 (s'il y en a) sont à
retirer : le v2 relancé verrouillerait la génération 1 et rejouerait le 401. Arrêt d'une course : `kill -TERM <PID>` hors de
la règle (demande une permission ; à ne pas élargir).

## 6. Ce qui reste

Vérification courte du v3 ; règle et épingle ; relais Claude et Gemini relancés ; la génération 1 relancée (seconde et
dernière course permise) ; sonde de la garde refus-question si la mère la prescrit.

## Pièces (scellées)

| Pièce | Empreinte SHA-256 |
|---|---|
| `scripts/lancer_course_ideation_bassins_etroits_v3.py` | `3fabd71e63bf9f3e830ed5128cd6a92f04ca91c0b13dabcc0ac7d316e5f44b36` |
| `tests/test_lancer_course_ideation_bassins_etroits_v3.py` | `6ab6ec5dfd28bdb975fa998f42f90deee596112f6452f7b8f860aa08214936a6` |
| `docs/notes/organisme-bassins-etroits-v1/devis-organisme-bassins-etroits-v3.md` | `7c340c445a99cfed3b35a3a127bf5b1dd5039bab5d7f0196aa3865a0f731cd43` |
| `…/preparateur-outils-v3/eprouver_authentification_kit_v1.py` | `06ed8d4eb6413083d55d34d1173f453236f6e2e77272f74f6c22705f2c317889` |
| `…/preparateur-outils-v3/resultat-eprouver-authentification-kit-v1.json` | `c485ab1fdf8d643f6da93143605521584e6fe8be7a16ee2b1dba004451dd1061` |
| `…/preparateur-outils-v3/mutations_lanceur_v3.py` | `6d7d6c09473d9bd04eb867814385ea5d19a59827e712b4187f2e9b865b655105` |
| `…/preparateur-outils-v3/resultat-mutations-lanceur-v3.json` | `379c57aeeb08bacee10e7d84b530062ebaa0d6b23c26fde4d73e3db71ed39a40` |
| `…/preparateur-outils-v3/differentiel-lanceur-v2-v3.diff` | `b2951d174ee9e2e44788325638d420ff224a9d47657b6b8c72b59ea3309f43c2` |
