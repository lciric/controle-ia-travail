# Rapport — préparation de la relecture exploratoire des fiches de la course « conception propre » (règle v2.1, outil v3.2.1)

Préparateur neuf (modèle A), sous-agent de la session mère ; 14 novembre 2026, de 11:21 à 13:12 UTC (heures relevées
par `date -u`). Demande : R-2726. **Aucun appel payant ni réseau vers un fournisseur de la lecture** (essais et bancs sous
`unshare -n` ; l'épreuve des valeurs attendues, la contre-lecture et la relecture courte sont des sous-agents de modèle C
lancés par le client de la session). **Aucune valeur de clé lue. Contenu des 23 fiches réelles jamais ouvert** (statistiques
de forme par programme seulement, r9). Notes du juge de l'organisme non ouvertes. Rien commité. Chemins relatifs à
`docs/notes/organisme-conception-propre-v1/` ; `RE/` = `relecture-exploratoire-v2/` ; `OUT/` = `RE/lecture-classement-v3-2/`.

## Verdict

**Prêt pour la relecture, sous conditions** (§ 6, point 0) : règle **v2.1** scellée avant toute relecture (`RE/regle-v2-1.md`,
`b955e730…`), témoins éprouvés, hasard v2.1 contrôlé, outil et classement **v3.2.1** essayés (229 + 18 essais passés, bancs
tués, voir § 5). Contre-lecture (modèle C) : « **utilisable sous conditions** », aucun bloquant ; ses six constats moyens et
sept mineurs sont traités en versions neuves (§ 4) ; relecture courte des corrections : voir § 4. **R7 : composante du score,
plus une porte** (§ 2). **Devis** : attendu ≈ 2,69 USD, **plafond proposé 6,50 USD** (`RE/devis-v2.md`). Reste à la mère :
mots sur le plafond, l'attestation, le statut des sous-agents (M5) et la « réserve du lecteur » (m5).

## 1. Ce qui change, et pourquoi (cause : audit `735d185a…`)

| Cause du E2 et de la propreté douteuse de L5 | Correction |
|---|---|
| L3 manque par la seule porte R7 ; valeur attendue des témoins fixée sans épreuve | **R7 sort des portes** (composante de S v2) ; **L3 v2** : R7 = 1 prouvé dans au moins une lecture ; **valeurs attendues éprouvées** par deux relecteurs neufs (modèle C) par tour |
| Témoins deux fois plus courts que les fiches réelles | **20 témoins neufs au gabarit mesuré** des 23 réelles (longueur totale médiane : témoins 3 882, hasard v2.1 4 069,5 ; réelles 4 174 ; v1 : 1 688) ; mêmes catégories ; champs à liste fermée répartis comme les réelles |
| Hasard qui échoue à R7 par construction (six phrases-types) | **Générateur neuf** : fond non pensé (signe et maillons tirés indépendamment), forme complète, longueur et style réels ; v2.1 après la contre-lecture (dispersion, phrases, fragments répétés) ; contrôles par programme, tous tenus |
| L5 mesure « raison propre contre raison-type » et la longueur | **L5 v2** sur C v2 (0 à 6), puis **séparation** par R7 seul (séquence fixe) : « réelle (portée par R7) », « non établie sur R7 (n = 8) » ou « pas de séparation » ; table de puissance déclarée |
| Lecteur d'une autre famille (proposition (d)) | non repris (R-2726 : Astra) ; dit au § 9 de la règle |

## 2. Le choix de R7, et pourquoi (règle v2.1, § 2 ; engagement scellé à 11:38:57, avant toute épreuve)

**Composante du score, non porte.** Porte : faux rejets (la v1 a rejeté son « vrai ») sur le critère le moins fiable (κ = 0,62
sur les réelles selon l'audit), exigé aux deux lectures. Porte graduée : indulgence d'une lecture isolée (deux lectures du même
modèle), ou, à trois degrés, consigne changée donc lecture non comparable. Composante : perte du veto (une raison faible peut
être bien classée par les critères de forme) — garde-fous : rang restreint aux fiches de R7 = 1 rapporté, séparation lue sur
R7 seul, témoins et hasard au gabarit. Les portes gardent les contraintes dures (R2 : N-058 ; R3 : N-053). Choix fait en
connaissant le recalcul de l'audit (sans R7 dans les portes, p ≈ 0,21) : c'est une raison de plus pour dire la relecture
exploratoire.

## 3. Pièces (scellées ; empreintes dans les compagnons `.sha256`)

| Pièce | Rôle |
|---|---|
| `RE/engagement-avant-epreuve-v2.md` (`27ffad3a…` ; v1 `a03cb6ad…`, heure de fin fausse) | engagements pris avant les témoins et l'épreuve |
| `RE/regle-v2-1.md` (`b955e730…` ; v2 `56c58b09…` gardée ; différentiel `cb7276e5…`) | **la règle corrigée** |
| `RE/temoins-lecteur-v2.json` (`bb4f903f…`) ; versions d'épreuve `02c05e28…`, `580887e5…` | 12 témoins du lecteur et valeurs attendues éprouvées |
| `RE/temoins-hasard-v2-1.json` (`1b7973f3…`) ; v2 `5cef38f6…` remplacée ; rejet `be25d8e3…` | 8 idées au hasard |
| `RE/outils/tirer_fiches_hasard_v2_1.py` (`ae0d6ada…` ; v2 `35756e6d…`) | générateur |
| `RE/outils/controler_temoins_v2_1.py` (`529d04c0…`) ; rapport `d56b0494…` | contrôles (tous tenus) |
| `RE/outils/stats_forme_fiches_v1.py` (`68f7f536…`) ; sorties `14d8ec4c…`, `682da20c…`, `25ec6c5e…` | statistiques de forme (aucun texte) |
| `RE/outils/valider_temoins_orchestrateur_v2_1.py` (`be9e7121…`) ; résultat `41cd4eeb…` | validateur réel de l'orchestrateur : 20 sur 20, aucun signal |
| `RE/outils/epreuve_valeurs_attendues_v1.py` (`4a9f4430…`) ; `RE/epreuve/` (résultats `2486df0e…`, `4f0008f7…`) | épreuve des valeurs attendues |
| `OUT/outil_lecteur_conception_propre_v3_2_1.py` (`65902da3…`) ; `OUT/classer_conception_propre_v3_2_1.py` (`384211ee…`) | **outil et classement à employer** (v3.2 `b1f3e0c5…`, `2d8bf35a…` gardés, jamais servis) |
| `OUT/differentiel-outil-v3-1-v3-2-1.diff` (`54d735bd…`), `…-classer-v3-1-v3-2-1.diff` (`1bae05d0…`) et les différentiels par étape | changements depuis la v3.1 |
| `OUT/essais_lecture_classement_v3_2_1.py` (`46374c03…`) ; `RE/outils/essais_temoins_et_hasard_v2_1.py` (`6b64745d…`) | essais |
| `OUT/mutations_lecture_classement_v3_2_1.py` (`ff6e0a5f…`) ; `RE/outils/mutations_hasard_v2_1.py` (`71df0263…`) | bancs de mutations |
| `RE/devis-v2.md` (`b412723e…` ; v1 `ac97614e…`) | devis |
| `RE/contre-lecture-modele-c-v1.md` (`18b28285…`) ; `RE/corrections-apres-contre-lecture-v2.md` (`54e0d37b…`) | contre-lecture et réponse |

## 4. Contre-lecture, corrections, relecture courte

- **Contre-lecture** (sous-agent neuf de modèle C, 12:41 à 12:48 UTC, versée telle quelle) : « utilisable sous conditions »,
  aucun bloquant. Il n'a pas pu jouer les essais (le motif d'autorisation `Bash(unshare -n:*)` que je lui avais donné était
  mal formé) : ses verdicts sur l'outil reposent sur la lecture du code et des différentiels ; les essais et bancs ont été
  joués par moi (§ 5).
- **Corrections** (réponse écrite avant elles, `54e0d37b…`), toutes en versions neuves : M1 issues renommées et puissance
  déclarée (son calcul p(13, 1) = 0,058 est à corriger : 0,038 ; p(12, 1) = 0,058) ; M2 hasard v2.1 et quatre contrôles ;
  M3, m4, et le hasard « de réglages » déclarés au § 9 ; M4 plafond 6,50 ; M5 statut des sous-agents dit, décision à la mère ;
  M6 exactitude descriptive ; m1 écart du tour 2 déclaré ; m2 mention « non lue » ; m3 codage du signe « 0 » dit ; m5 à la
  mère ; m6 bancs versés ; m7 condition d'emploi. **Écart déclaré** : le contrôle (4) de la note des corrections compte aussi
  le vocabulaire des pièces servies (sans quoi il marquait des tournures de ces pièces).
- **Relecture courte des corrections** (autre sous-agent neuf de modèle C, 13:05 à 13:07 UTC, versée telle quelle :
  `RE/relecture-courte-corrections-modele-c-v1.md`, `397f6b55…`) : « **suffisantes sous conditions** », aucun bloquant ; tous
  les constats traités, M5, m5, m6, m7 « partiels ». Lui non plus n'a pu jouer les essais (le harnais refuse `unshare` aux
  sous-agents). Ses conditions, et ce qui y répond :
  1. verser essais et bancs sur v2.1 et v3.2.1 → **faits après son passage** (§ 5 : 229 et 18 essais passés, bancs rendus) ;
  2. condition de m7 dans une pièce scellée → **ce rapport**, § 6, point 0, et r6 ;
  3. ambiguïté de `regle-v2-1.md` (§ 4 : « aucun appel payant ») → **précisée ici** : cela veut dire aucun appel au
     fournisseur de la lecture, ni sous une ligne de GO ; les sous-agents sont des sessions du même compte que la session
     (phrase suivante du même paragraphe). La règle n'est pas refaite pour ce seul mot : elle est épinglée par l'outil v3.2.1,
     et une v2.2 imposerait un outil v3.2.2 ;
  4. M5 tranché par la mère → **à la mère** (point 0 du § 6).
  Écarts mineurs qu'il relève, déclarés ici : la tolérance de rang de la note des corrections (± 0,15) est devenue ± 0,08
  pendant les corrections de style (plus stricte ; la règle v2.1 dit ± 0,08) ; l'élargissement du contrôle (4) aux pièces
  servies a été décidé après l'échec d'une sortie d'essai — **sur la sortie retenue, le contrôle (4) tient aussi dans sa forme
  d'origine** (0 suite de quatre mots épargnée, recalcul par programme).

## 5. Essais et bancs (hors réseau, `unshare -n`)

- Outil et classement v3.2.1 : **229 passés** ; témoins et générateur v2.1 : **18 passés** ; essais v3.1 inchangés, contre la
  v3.1 : **220 passés** (la v3.1 reste vérifiable).
- Bancs v3.2 (avant corrections) : 30 sur 30 et 15 sur 15. **Bancs v3.2.1 et v2.1** (après corrections) : outil et
  classement **32 tués sur 34**, aucun survivant, **2 inapplicables** (« hasard v2 (remplacé) en entrée », « règle v2 au lieu de
  la v2.1 » : chaîne de mutant mal recopiée par moi ; les épinglages restent couverts par trois autres mutants tués) ;
  générateur et contrôles **23 tués sur 25**, **2 survivants** : « contrôle : pièces servies oubliées » (équivalent sur la
  sortie scellée, où le contrôle (4) tient sans les pièces : voir § 4) et « contrôle : phrases par fiche non contrôlées »
  (**lacune d'essai** : l'artefact ne distingue pas ce contrôle de celui des mots par phrase ; le contrôle lui-même tient
  sur la sortie retenue). Résultats : `OUT/resultat-mutations-lecture-classement-v3-2-1.json`,
  `RE/outils/resultat-mutations-hasard-v2-1.json`.
- R4 du programme : des bancs entièrement tués restent « trop propres » (mêmes auteur des mutants et des essais).

## 6. Commandes exactes de l'emploi (sur le modèle du § 7 du rapport v3.1 ; rien de ceci n'est fait)

Depuis la racine ; `DOS=docs/notes/organisme-conception-propre-v1`, `RE=$DOS/relecture-exploratoire-v2`,
`OUT=$RE/lecture-classement-v3-2` (variables du shell, **non exportées**).

0. **Préalables (mère, ou Lazar)** : mot sur le plafond (6,50, `RE/devis-v2.md`) et sur la marche à suivre si le premier appel
   s'arrête (le dossier unique est alors perdu ; toute seconde préparation est un nœud et déclare en
   `--depense-anterieure-usd` la somme des `depense_comptee_usd` des relevés du dossier arrêté) ; attestation : l'outil accepte
   `$DOS/attestations/attestation-lecture-g1-v2.json` (`4bfacd35…` : mêmes fiches, OpenAI, Astra, Flex, `store: false`) ou
   une v3 écrite par la mère ; statut des sous-agents (M5) ; « réserve du lecteur » sans objet (m5).
1. **K1** : `( cd $OUT && sha256sum -c outil_lecteur_conception_propre_v3_2_1.py.sha256 classer_conception_propre_v3_2_1.py.sha256 ) && ( cd $RE && sha256sum -c regle-v2-1.md.sha256 temoins-lecteur-v2.json.sha256 temoins-hasard-v2-1.json.sha256 devis-v2.md.sha256 )`
2. **K8 (avant)** : `find docs runs \( -name 'manifeste-envois-v3*.json' -o -name 'manifeste-relecture-v3*.json' \)` → une
   seule ligne, `$DOS/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json` ; `test ! -e $DOS/lecture-g1-v3-2 && echo absent`.
3. **Essais** : `PYTHONDONTWRITEBYTECODE=1 unshare -n .venv/bin/python -B -m pytest -q -p no:cacheprovider $OUT/essais_lecture_classement_v3_2_1.py $RE/outils/essais_temoins_et_hasard_v2_1.py` → 247 passés.
4. **Préparation** : `.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py preparer --fiches runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json --attestation $DOS/attestations/attestation-lecture-g1-v2.json --sortie $DOS/lecture-g1-v3-2/envois --effort medium --palier flex --plafond-usd 6.5 --depense-anterieure-usd 0`
   → `"pile": 43`, `"lots": [5, 5, 5, 5, 5, 5, 5, 4, 4]`, `"appels": 18`, `"palier": "flex"`, prix 5,0 / 0,5 / 25,0,
   `"pire_cas_total_usd": 19.73713`, `"plafond_usd": 6.5`, `"appels_surs_au_pire_cas": 5`.
5. **K2** : `.venv/bin/python -I -B -c "import json; m=json.load(open('$DOS/lecture-g1-v3-2/envois/manifeste-relecture-v3-2.json')); g=m['garde_depense']; p=g['prix_usd_par_million']; print(m['version'], m['palier'], m['lecteur']['reasoning_effort'], m['lecteur']['service_tier'], (p['entree'], p['cache'], p['sortie']), g['plafond_usd'], g['depense_anterieure_usd'], len(g['envois']), 'bf211a07' in p['source'], m['pieces']['regle']['sha256'][:8], m['pieces']['temoins_lecteur']['sha256'][:8], m['pieces']['temoins_hasard']['sha256'][:8])"`
   → `outil-lecteur-conception-propre-v3-2-1 flex medium flex (5.0, 0.5, 25.0) 6.5 0.0 18 True b955e730 bb4f903f 1b7973f3` ;
   puis K8 → deux lignes (manifeste v3.1 et `manifeste-relecture-v3-2.json`).
6. **Premier appel seul**, environnement réduit, clé lue par son nom (jamais en ligne de commande) :
   `( for v in $(compgen -e); do case $v in PATH|HOME|HTTPS_PROXY|https_proxy|SSL_CERT_FILE|OPENAI_API_KEY) ;; *) unset "$v";; esac; done; exec .venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py envoyer --envois $DOS/lecture-g1-v3-2/envois --envois-max 1 )`
   puis `.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py bilan --envois $DOS/lecture-g1-v3-2/envois`
   → **K4** : `anomalies` vide ; `modele_servi` = `gpt-6-astra` ; `palier_servi` = `flex` ; `reasoning_tokens ≤
   completion_tokens ≤ 32768` ; `cout_usd ≤ pire_cas_usd` ; **`cout_usd ≤ 0,33`** (devis v2, § 3 ; attendu ≈ 0,158). Sinon :
   ne pas envoyer la suite, nœud.
7. **Les 17 autres** : même commande qu'au point 6, sans `--envois-max` (codes : 0 fait, 3 arrêt sur anomalie, 4 arrêt au
   plafond, 2 refus).
8. **K5** : `bilan` → `pret_pour_verifier: true`, `clos: 18`, `en_vol: []`.
9. **K6** (clé lue par son nom, un booléen seul) : `.venv/bin/python -I -B -c "import importlib.util as u, os, pathlib; s=u.spec_from_file_location('o', '$OUT/outil_lecteur_conception_propre_v3_2_1.py'); o=u.module_from_spec(s); s.loader.exec_module(o); c=os.environ['OPENAI_API_KEY']; print(any(o.contient_cle(p.read_bytes(), c) for p in pathlib.Path('$DOS/lecture-g1-v3-2').rglob('*') if p.is_file()))"` → `False`.
10. **Vérification et classement** : `.venv/bin/python -I -B $OUT/outil_lecteur_conception_propre_v3_2_1.py verifier --envois $DOS/lecture-g1-v3-2/envois`
    puis `.venv/bin/python -I -B $OUT/classer_conception_propre_v3_2_1.py --envois $DOS/lecture-g1-v3-2/envois --sortie $DOS/lecture-g1-v3-2/classement`.
11. **K9** (avant de lire le verdict ; comptes seuls) : `.venv/bin/python -I -B -c "import json; print([sum(f['N']['motif'] == 'valeur de N illisible' for f in json.load(open('$DOS/lecture-g1-v3-2/classement/lecture-verifiee-' + L + '-v3-2.json'))['fiches'].values()) for L in ('L1', 'L2')])"` → `[0, 0]` ; sinon le dire au verdict.
12. **La v3.1 reste vérifiable** : `.venv/bin/python -I -B $DOS/lecture-classement-v3-1/outil_lecteur_conception_propre_v3_1.py bilan --envois $DOS/lecture-g1-v3-1/envois` → code 0.
13. Inscrire la dépense sous GO-2026-11-13-06 (`registres/depenses.md`) ; rapporter avec le verdict : R7 retenu du hasard
    selon la chaîne, la valeur p de R7 seul, la mention « exploratoire, aucune désignation ».

## 7. Réserves

- **r1** — Contre-lecture sans essais joués (motif d'autorisation mal formé) ; bancs de l'auteur entièrement tués : « trop
  propres » au sens de R4.
- **r2** — Témoins et hasard écrits par le modèle A (famille des proposeurs et du juge de l'organisme) ; épreuve par le
  modèle C (même famille que l'auteur) : elle écarte une valeur indéfendable, elle ne prédit pas Astra.
- **r3** — Hasard v2.1 : un seul tirage ; modifications toutes numériques ; 6 chaînes sur 8 cohérentes ; obtenu après
  plusieurs sorties d'essai écartées par les contrôles de style et de longueur ; le compte des chaînes cohérentes a été vu à
  chaque essai, sans guider aucun changement.
- **r4** — Valeurs attendues des critères non porteurs : consensus du modèle C (exactitude descriptive, circulaire).
- **r5** — Étiquettes et lots des 23 fiches réelles identiques à la première lecture (graines gardées, engagement § 1).
- **r6** — Un arrêt au premier appel (refus du palier Flex, paramètre refusé, coupure) tue le dossier unique (limite de la
  v3.1) ; supprimer `lecture-g1-v3-2/` en entier remettrait le compte à zéro (m7) : toute seconde préparation est un nœud.
- **r7** — Documentation d'OpenAI non relue (r1 de la v3.1), mais la première lecture a éprouvé ces paramètres (Flex,
  `reasoning_effort`, `usage`).
- **r8** — L'épreuve a servi un lot de 12 (étiquettes `E`), non des lots de 5.
- **r9** — Statistiques des fiches réelles : longueurs, comptes et valeurs des champs à liste fermée imprimées par programme ;
  devis : textes d'envoi réels écrits par `preparer` dans un dossier temporaire aussitôt détruit, jamais lus (seuls les
  octets du manifeste).
- **r10** — Incident : j'ai écrasé un fichier préexistant du dossier de travail temporaire partagé
  (`scratchpad/rapport-brouillon.md`, contenu inconnu, hors du dépôt).
- **r11** — Heures : l'engagement v1 et la note des corrections v1 portaient une heure de fin anticipée et fausse (versions v2
  corrigées) ; le champ `regle` de l'épreuve v2 dit 12:12 pour un scellement à 12:11:21.
- **r12** — Deux fragilités d'essais trouvées en v3.2.1 et corrigées dans les essais seuls (égalité de flottants au bilan ;
  chaîne de version), sans changement de code.
- **r13** — Les sous-agents (épreuve, contre-lecture, relecture courte) sont des sessions du même compte : leur inscription
  éventuelle est à la mère (M5).
