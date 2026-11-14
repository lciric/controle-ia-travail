# Copie publique `lciric/controle-ia` régénérée sans `brouillons/pain-axis-*` — préparation, 14 novembre 2026 (v1)

Agent neuf, sur consigne de la session mère, après les mots de Lazar R-2672 (écart constaté) et R-2679 (« go »). **Rien n'est poussé, rien n'est supprimé, aucun historique n'est réécrit.** Aucune écriture dans `registres/`, aucun commit dans le dépôt de travail. Heures par `date -u` : travail de 09:14 à 09:50 UTC.

## Verdict

La copie est prête à pousser : commit local **`35ed2bc1ae42021af749687ab90c7ca2d33a3819`**, posé sur le commit public actuel `a043767723dea9073d4a1589f6876d0e217821b3`, arbre git `d2b189846db6e8be52a409dfd8610f20b0d8750b`, tiré du même commit source que la copie en ligne (`549588593ae0bed37a9fac1a4e7ac3d3f138e662`, 12 novembre). Par rapport à la copie en ligne : **103 fichiers retirés, tous `brouillons/pain-axis-*`, 1 fichier modifié (`EXPURGE.md`), 0 ajouté**. Les trois preuves par ensembles tiennent, avec une exception à (c) qui demande un mot de Lazar (deux chemins `docs/decisions/proposition-P-013-…pain-axis…` gardés). Deux constats d'historique pèsent plus que la régénération : ces brouillons sont publics **depuis le 5 novembre** (ancienne branche), et ils **restent dans l'historique de `main`** après la poussée.

## 1. Script et essais

- `scripts/depot_expurge_v7.py` (sha256 `ed5d73e6f74951990d9bbb8fde7bc0076aa98e88334d89fd5db6d9d03dcdbbb1`, scellé), nom neuf (R12) ; la v6 est intacte (`cbd1a632…`, relue avant et après).
- Ajouts de la v7 :
  1. **Retraits par nom**, jamais lus (ni contenu, ni empreinte, ni taille), comptés par motif dans `EXPURGE.md` sans chemin : `brouillons/pain-axis-*` (dossiers à toute profondeur, fichiers posés dans `brouillons/`, compagnons) ; `docs/notes/regard-ou-raisons-*` et `docs/notes/collisionneur-regard-ou-raisons-*` (aucun fichier au commit source ; 6 à la tête actuelle de `main`). Le retrait par nom passe avant les retraits de la v6 : le fichier `…/voisin-where-empathy/extrait-texte-v1.txt`, que la v6 lisait pour en lister l'empreinte, n'est plus lu.
  2. **Garde des copies par identifiant d'objet git** : les identifiants des fichiers retirés par nom sont lus dans l'arbre du commit (`git ls-tree`, sans lire les fichiers) ; un fichier gardé, ou un membre d'archive gardée à toute profondeur, qui porte un de ces identifiants arrête le script.
  3. **Garde des noms dans les archives** : un membre d'archive dont le chemin porte `pain-axis` ou `regard-ou-raisons` (casse ignorée, où que soit le dossier) arrête le script.
  4. **Garde des noms hors des dossiers visés** : un chemin gardé qui porte un de ces noms arrête le script, sauf s'il figure dans la liste nommée `GARDES_SIGNALES` (les deux chemins de P-013, voir 3 (c)) ; ces chemins sont rapportés dans le bilan. Aucun repli silencieux.
  5. `EXPURGE.md` dit que le script est postérieur au commit source et donne son empreinte.
- Défaut trouvé par les essais avant toute régénération : `correspond` lit à la lettre le préfixe d'un motif qui finit par `/**` ; `brouillons/pain-axis-*/**` n'aurait visé aucun dossier. Le retrait par nom s'apparie par `_segments`, comme l'embargo. La v6 n'a aucun motif de cette forme : elle n'est pas touchée.
- `tests/test_depot_expurge_v7.py` (sha256 `e1a686ee685afa6a8fc9de776bb251c168858930e130bbd2e5c925002371408b`, scellé) : **30 passés** = les 19 essais de la v6 rejoués sur la v7 (texte inchangé, seul le script chargé change) + 11 neufs, chaque retrait et chaque garde avec cas sain et artefact (R5) : retrait `pain-axis` ; retrait de l'autre projet ; noms dans une archive ; identifiant git ; copie de bout en bout saine (une clé factice posée dans un fichier retiré par nom : la copie passe, preuve qu'il n'est pas lu) ; cinq copies refusées (nom hors de `brouillons/`, nom hors de `docs/notes/`, copie renommée, copie dans une archive, nom dans une archive) ; noms du dépôt réel tous visés ou nommés.
- `tests/test_depot_expurge_v6.py` sur la v6 : 19 passés. Essais des versions 1 à 5 : 62 passés.
- Suite complète du dépôt (6 224 essais) : lancée, arrêtée par son identifiant de tâche après 12 minutes et environ 10 % (trop longue pour cette tâche). 7 échecs vus, étrangers à ce travail et présents sans lui : `tests/test_cibles_invisibles_v1.py` et `_v2.py` (2 chacun : modules de `src/controle_ia/` non inventoriés) et `tests/test_corpus_arxiv.py` (3 : module `pypandoc` absent de l'environnement). À la mère de les relire.

## 2. Régénération

Procédure du rapport du 12 novembre, même commit source, même README public (repris de `a043767`, sha256 `ddc18ad3…`, aucune mention de ces brouillons), sortie hors du dépôt :

    .venv/bin/python scripts/depot_expurge_v7.py 549588593ae0bed37a9fac1a4e7ac3d3f138e662 SORTIE --readme README-public-a043767.md

Une seule construction, code 0, 2 min 20 s. Bilan (`pieces-2026-11-14-v1/bilan-regeneration-v7-sans-liste-v1.json`, `b7d4e743…`) :

| | copie en ligne (v6) | régénération (v7) |
|---|---|---|
| fichiers gardés (hors `EXPURGE.md`) | 18 511 | **18 408** |
| retirés et listés avec empreinte | 3 037 | 3 036 |
| sous embargo, comptés seulement | 92 | 92 |
| retirés par nom, comptés seulement | — | **104** |
| archives examinées | 94 | 94 |
| adresses de tiers déjà publiées, comptées | 34 | 34 |

104 = les 103 fichiers de la copie en ligne + le fichier d'extrait que la v6 retirait déjà (d'où 3 037 → 3 036). Paquet `controle-ia-expurge-5495885.bundle` : sha256 `46f28432d63f37399d7d1f1222479946ebde717278e1d4048cb87eb760801f06`. Rien de postérieur au 12 novembre n'entre : tout fichier de l'arbre neuf vient du commit source à l'identique, sauf `README.md` (README public, identique à celui en ligne) et `EXPURGE.md`.

## 3. Preuve par ensembles

Par programme, sur les sorties de `git ls-tree -r` (noms, modes, identifiants d'objets) : `pieces-2026-11-14-v1/preuve_ensembles_v1.py` (`d4530867…`), résultat `preuve-ensembles-v1.json` (`54e94e0d…`). Rejouée à l'identique sur le commit local `35ed2bc`.

- **(a) Inclusion.** Arbre public `a043767` : 18 512 fichiers ; arbre neuf : 18 409. Chemins neufs absents du public : **0**. Fichiers gardés de même mode et de même identifiant d'objet : **18 408**. Différents : **1**, `EXPURGE.md` (`ae106612…` → `18609ee0…`), régénéré par le script. `README.md` : identique (`d78b2c99…`). Différentiel de `EXPURGE.md` (`pieces-2026-11-14-v1/differentiel-EXPURGE-a043767-vers-regeneration-v1.txt`, `c36d72e8…`) : 5 lignes ôtées, 4 posées — nom du script et son empreinte, phrase sur les retraits par nom, compte (« 18408 kept, 3232 omitted : 3036 listed, 92 under embargo, 104 withheld by name »), une ligne de motif neuve (104), la ligne de motif et la ligne de chemin du fichier d'extrait ôtées, un titre.
- **(b) Différence.** Public moins neuf : **103 chemins**, ensemble **égal** à celui des chemins `brouillons/pain-axis-*` du public (103 ; hors de cet ensemble : 0 ; restés dans le neuf : 0). 52 sont des compagnons `.sha256`. Par premier niveau : `pain-axis-canal-v1` 36, `pain-axis-programme-fusionne-v1` 31, `-v2` 8, `-v3` 8, `-v4` 6, `pain-axis-brainstorm-v1` 8, `pain-axis-creatif-v1` 4, et deux fichiers posés dans `brouillons/`. Les 103 ont le même identifiant qu'au commit source. Empreinte de la liste triée des 103 chemins : `8d91905d…`. Le compte de la mère (103) est confirmé.
- **(c) Noms.** Chemins de l'arbre neuf qui contiennent `pain-axis` : **2, pas 0** : `docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md` et son compagnon. Ils sont hors du retrait commandé, déjà en ligne depuis le 12 novembre, et inchangés. C'est une proposition de décision de 18 lignes (témoins de concept dans le préenregistrement de T0.7) qui cite le remue-méninges `brouillons/pain-axis-brainstorm-v1.md` et nomme des directions ; son nom ne figure pas dans les interdits, l'agent en a lu l'en-tête seulement. Gardés et signalés : les retirer changerait l'ensemble commandé en (b). Chemins contenant `regard-ou-raisons` : 0. Fichier gardé de même identifiant d'objet qu'un fichier visé : 0. Interdits nommés par la mère (`bras-attaque`, `mode-tenu-a-l-ecart`, `anteriorite-bras-informe`, `registres/`, `donnees/`, `diag/` et `runs/` de 7a et 7b) : 0 chemin.
- Autres noms gardés qui évoquent le sujet, signalés sans avis : `docs/notes/lecture-voisin-where-empathy-v1.md`, le dossier `docs/notes/voisin-where-empathy-v1-sources/` (dont une archive de fichiers de travail), `docs/sources/pdf/provenance-voisin-where-empathy-v1.md` (lecture d'un papier voisin cité par N-023). Et un nom qui évoque l'embargo sans être visé par ses motifs : `docs/procedures/brief-session-attaquant-informe-v1.md` (en ligne depuis le 12 novembre ; non lu).

## 4. Historique public, par noms seulement

Références distantes le 14 novembre à 09:30 UTC (`git ls-remote`) : `HEAD` et `refs/heads/main` seulement, tous deux `a043767`.

| commit de `main` | date du commit | fichiers | `brouillons/pain-axis-*` | autres noms `pain-axis` |
|---|---|---|---|---|
| `cd8f5f16e35154fd91a5ed56b826a20ce3f0ae13` | 2026-10-09T10:37:08+02:00 | 2 100 | 0 | 0 |
| `fc9acdee59b5c211b45d57945a4bddaa1631a378` | 2026-11-08T10:23:18+01:00 | 2 100 | 0 | 0 |
| `a043767723dea9073d4a1589f6876d0e217821b3` | 2026-11-12T14:46:50+00:00 | 18 512 | **103** | 2 (P-013) |

- **Sur `main`** : publics depuis le commit `a043767`, poussé le 12 novembre vers 14:47–14:49 UTC (R-2437). Après la poussée du commit neuf, ils disparaissent de la tête de `main` mais **restent lisibles dans `a043767`**, ancêtre du commit neuf.
- **Branche `claude/new-session-7qxayx`** : absente du distant aujourd'hui (encore présente le 12 novembre à 20:29 UTC, R-2452). Elle ne peut plus être examinée. Calcul par nom sur son commit source privé (`44929945`, script v5, R-1579) : la v5 garde 12 095 chemins, le compte du registre, dont **les 104 chemins `brouillons/pain-axis-*`** (le fichier d'extrait compris) et les deux de P-013. Ces brouillons étaient donc, selon ce calcul, **publics depuis le 5 novembre vers 16:18 UTC** sur cette branche. Inférence par nom, non vérifiée sur la branche elle-même. Un commit dont la branche est supprimée peut rester servi par GitHub à qui en connaît l'identifiant (tête `56fdb15a`).
- Non vérifié : copies dérivées du dépôt, étoiles, demandes de fusion. L'interface de GitHub a refusé la lecture (dépôt non ouvert à la session, HTTP 403) ; non contourné.

Retirer ces fichiers de l'historique demande une poussée forcée de `main` ou la suppression du dépôt, puis éventuellement une demande à GitHub pour les commits orphelins : décision de Lazar. Rien n'a été fait en ce sens.

## 5. Garde des secrets sur l'arbre neuf

- Garde du script (valeurs des variables de clés de l'environnement, formes connues, archives à toute profondeur) : **0**, sinon le paquet n'aurait pas été écrit.
- Recherche indépendante (`pieces-2026-11-14-v1/garde_secrets_independante_v1.py`, `1b5f4201…` ; résultat `garde-secrets-arbre-neuf-v1.json`, `84683ba8…`), mêmes formes que la garde du dépôt (`sk-ant-…`, `sk-…`, `ghp_…`, `hf_…`, `AKIA…`, `AIza…`), sur 18 409 fichiers et 6 087 membres de 94 archives ; aucun jeton n'est affiché ni écrit : **5 jetons de la forme `sk-…`, tous marqués factices** (cinq fichiers d'essais) ; 0 pour les cinq autres formes ; **0 valeur des 19 variables de clés de l'environnement** ; 0 chemin sous embargo.
- Passe à formes élargies (longueurs minimales abaissées ; `garde_secrets_independante_large_v1.py`, `3ec34e2e…` ; résultat `e4a13ab9…`) : 31 occurrences, dont 25 marquées factices dans le jeton ou dans la ligne, et 6 mentions du seul préfixe public d'une forme de clé (13 caractères, vérifié par programme), sans clé. Le rapport du 12 novembre comptait 13 et 3 avec d'autres formes : les nombres ne se comparent pas un à un.

## 6. Commit local et commande de poussée

- Clone de travail du dépôt public, sans contenu des anciens fichiers : `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/clone-public-travail` (bloc-notes de l'agent, non durable).
- Commit : **`35ed2bc1ae42021af749687ab90c7ca2d33a3819`**, parent `a043767…`, arbre `d2b18984…`, auteur « controle-ia (copie expurgée) » comme le 12 novembre, daté `2026-11-14T09:28:10+00:00`, message : « Copie expurgée de controle-ia-travail au commit 549588593ae0bed37a9fac1a4e7ac3d3f138e662 (12 novembre 2026), régénérée le 14 novembre 2026 sans brouillons/pain-axis-* ». Aucune ligne d'attribution : le message de la consigne, tel quel, pour un dépôt public.
- Vérifié : arbre du commit égal à l'arbre régénéré (noms, modes, identifiants) ; `a043767` ancêtre (avance rapide) ; différence avec `a043767` : 103 suppressions, toutes `brouillons/pain-axis-*`, 1 modification. Répétition locale de la sélection d'objets d'une poussée, sans réseau d'écriture : **4 objets** partiraient (le commit, l'arbre racine, l'arbre `brouillons`, `EXPURGE.md`). Le contenu des 103 fichiers visés n'a jamais été téléchargé dans ce clone (0 objet présent, vérifié après la pose du commit, après la répétition et à 09:33 UTC).
- Commande de poussée. Le rapport du 12 novembre dit la manière (« passée par l'environnement de git, jamais affichée », jeton `CONTROLE_IA_GITHUB_TOKEN_2`) sans consigner la ligne ; celle-ci suit cette manière avec la forme d'aide de `scripts/amorce_instance_p3bis.sh`. Le jeton est présent dans l'environnement (vérifié par son nom, valeur non lue).

      CLONE=/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/clone-public-travail
      # avant : doit rendre a043767723dea9073d4a1589f6876d0e217821b3
      git ls-remote https://github.com/lciric/controle-ia.git refs/heads/main
      # poussée en avance rapide, sans --force
      GIT_TERMINAL_PROMPT=0 GIT_CONFIG_COUNT=2 \
      GIT_CONFIG_KEY_0=credential.helper GIT_CONFIG_VALUE_0= \
      GIT_CONFIG_KEY_1=credential.helper \
      GIT_CONFIG_VALUE_1='!f() { echo username=x-access-token; echo "password=${CONTROLE_IA_GITHUB_TOKEN_2}"; }; f' \
      git -C "$CLONE" push https://github.com/lciric/controle-ia.git 35ed2bc1ae42021af749687ab90c7ca2d33a3819:refs/heads/main
      # après : doit rendre 35ed2bc1ae42021af749687ab90c7ca2d33a3819
      git ls-remote https://github.com/lciric/controle-ia.git refs/heads/main

  Non essayée (aucune poussée, même à blanc). Dans ce clone, ne lancer ni `git show`, ni `git diff`, ni `git log -p` sur `a043767` : git téléchargerait le contenu des fichiers visés (voir 7.1).
- Si le bloc-notes est vidé : cloner (`git clone --filter=blob:none --no-checkout`), rejouer la régénération (section 2), importer le paquet (`git fetch PAQUET main:refs/copie/regeneration-v7`), puis `git commit-tree d2b189846db6e8be52a409dfd8610f20b0d8750b -p a043767723dea9073d4a1589f6876d0e217821b3 -m "…"` avec le même auteur et la même date : le même identifiant de commit doit sortir.

## 7. Écarts de l'agent

1. **Contenu téléchargé sans être lu.** Dans le premier clone « sans contenu » (`…/scratchpad/public/sans-contenu`), la commande `git show -s --format=%cI` sur `a043767` a fait calculer par git la différence avec le commit parent, et git a téléchargé d'un coup les objets des fichiers ajoutés (un paquet de 14 306 objets, 81,6 Mo, à 09:16:10 UTC), dont ceux des 103 fichiers visés. L'agent n'a ouvert ni affiché aucun de ces contenus ; ils sont identiques à ceux du dépôt de travail privé (mêmes identifiants). Ce clone n'a servi qu'aux listes de noms ; il reste en place, non supprimé : à supprimer par la mère. Le clone de travail de la section 6 n'a pas ce défaut.
2. **Une commande interdite, sans sortie.** Une ligne de reste a exécuté `printenv -0` redirigé vers `head -c0` : rien n'a été affiché ni écrit, mais la lettre de l'interdit est enfreinte.
3. **Refus non contourné** : lecture des métadonnées du dépôt public par l'interface de GitHub (HTTP 403).

## 8. Réserves et nœuds pour Lazar

1. **P-013** (`docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md` et compagnon) reste dans la copie : la retirer ou la garder. Une ligne à ôter de `GARDES_SIGNALES` et un retrait à écrire dans une version 8 si elle sort.
2. **Historique** : `a043767` garde les 103 fichiers ; l'ancienne branche les a portés depuis le 5 novembre. La poussée préparée ne retire rien de l'historique.
3. Le retrait est par nom : un fichier gardé qui cite ou résume ces brouillons sous un autre nom n'est pas détecté (seules les copies exactes le sont, par identifiant). Même limite que l'embargo du 12 novembre.
4. Le script v7, ses essais et ce rapport portent les noms `pain-axis` et `regard-ou-raisons` ; une fois versés, ils entreront dans les copies publiques futures, comme la v6 porte les noms de l'embargo.
5. Les pièces du dépôt de travail créées ici ne sont ni committées ni poussées : la mère verse.

## Pièces et empreintes

| pièce | sha256 |
|---|---|
| `scripts/depot_expurge_v7.py` | `ed5d73e6f74951990d9bbb8fde7bc0076aa98e88334d89fd5db6d9d03dcdbbb1` |
| `tests/test_depot_expurge_v7.py` | `e1a686ee685afa6a8fc9de776bb251c168858930e130bbd2e5c925002371408b` |
| `pieces-2026-11-14-v1/preuve_ensembles_v1.py` | `d4530867f16b375a6fadcca132f221141de96dbc9184850e976aec57452e4a61` |
| `pieces-2026-11-14-v1/preuve-ensembles-v1.json` | `54e94e0de97a3a72a139e5a0e5a2d99d140d3e7c5cbeeb78703161db9294fad6` |
| `pieces-2026-11-14-v1/bilan-regeneration-v7-sans-liste-v1.json` | `b7d4e743dd3b5bdb82bdf29345244d461f056d0e1bc530efce4e3eebb74fb154` |
| `pieces-2026-11-14-v1/differentiel-EXPURGE-a043767-vers-regeneration-v1.txt` | `c36d72e8e2699df63c61a697de8025222ea7ef4e8a0e6c11ad9b77361e15e8a8` |
| `pieces-2026-11-14-v1/garde_secrets_independante_v1.py` | `1b5f4201abe0d0ac0f6cf1c83b70fe62d44bbc693a61e660b458dd6fc715954b` |
| `pieces-2026-11-14-v1/garde-secrets-arbre-neuf-v1.json` | `84683ba86bc611e871b4d0b13b96ad8f3e30e47dfb06cd82e453fa565639c0db` |
| `pieces-2026-11-14-v1/garde_secrets_independante_large_v1.py` | `3ec34e2e0e3a97ae9e551608bacd132102fe3a2391b6c6eb8bcde8bf8b148c01` |
| `pieces-2026-11-14-v1/garde-secrets-arbre-neuf-large-v1.json` | `e4a13ab9002fe1cddccd5e29f5aefd5877fc70edda38db73925f129e48757e21` |
| hors dépôt : `EXPURGE.md` de la régénération | `51f00bf06160d2458789b4ffbf376234cc8ad60cb3abda3e489361493338d776` |
| hors dépôt : `bilan.json` complet de la régénération | `2ad3f605c91d0a8d2fc5ddda5526c7d57b78d45844bf34f00713b4ecd92e04ee` |

Les pièces `pieces-2026-11-14-v1/` sont dans `docs/notes/copie-publique-v1/`. Listes rejouables : `git ls-tree -r a043767723dea9073d4a1589f6876d0e217821b3` dans un clone sans contenu du dépôt public, `git ls-tree -r 549588593ae0bed37a9fac1a4e7ac3d3f138e662` dans le dépôt de travail, `git ls-tree -r HEAD` dans l'arbre régénéré ; puis `python3 -I preuve_ensembles_v1.py LISTE_PUBLIC LISTE_NEUF LISTE_SOURCE`.
