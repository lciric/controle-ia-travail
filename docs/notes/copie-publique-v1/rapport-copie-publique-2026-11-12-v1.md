# Copie publique expurgée de `lciric/controle-ia` — 12 novembre 2026 (v1)

Agent neuf, sur consigne de la session mère, après le mot de Lazar R-2433 (option 2). Aucune écriture dans `registres/`.

## Verdict

Copie expurgée construite par `scripts/depot_expurge_v6.py` sur `origin/main` `549588593ae0bed37a9fac1a4e7ac3d3f138e662`, poussée sur `lciric/controle-ia`, branche `main`, en commit neuf **`a043767723dea9073d4a1589f6876d0e217821b3`** par-dessus `fc9acdee` (aucune poussée forcée ; branche `claude/new-session-7qxayx` non touchée). Arbre publié identique à l'arbre construit (arbre git `ec2ffb2a5cad5346afb721eaa1d4f6bf270a54e9` des deux côtés).

## Construction

- Script : `scripts/depot_expurge_v6.py` (sha256 `cbd1a632a856dfe8…`), v5 inchangée (R12) ; essais `tests/test_depot_expurge_v6.py` (`02dd7c3be5b343ed…`) : 19 passés (13 de la v5 rejoués, 6 neufs, chacun avec cas sain et artefact) ; `tests/test_depot_expurge_v5.py` : 13 passés.
- Ajouts de la v6 : embargo par nom (jamais lu : ni contenu, ni empreinte, ni taille ; compté sans chemin dans `EXPURGE.md`) ; textes de tiers hors `docs/sources/pdf/` ; candidature TAIF ; formes de clés `sk-…` et `AKIA…` (une clé `sk-…` marquée factice n'arrête pas ; la comparaison aux valeurs de l'environnement reste entière) ; garde des données personnelles (adresse de Lazar, adresse IP publique hors liste de valeurs relevées, chemin personnel hors comptes techniques) ; paquet git incrémental refusé comme format non examiné ; README public fourni par `--readme`.
- Cinq constructions : la première arrêtée sur quatre paquets git incrémentaux (code publié dans `lciric/ideation-organism`, retirés) ; la deuxième sur neuf clés factices `sk-…` (toutes marquées FAUX, FACTICE, essai ou cle-fa ; aucune valeur de l'environnement) ; la troisième sur un chemin d'exemple (`/Users/alice`) ; la quatrième et la cinquième passent (la cinquième avec le README final).
- Bilan : 18 511 fichiers gardés (≈ 380 Mo), 3 037 retirés et listés avec empreinte (≈ 2,34 Go), 92 sous embargo comptés seulement, 94 archives examinées à toute profondeur.

## Omissions par motif (fichiers)

| motif | fichiers |
|---|---|
| relève de Gemini (dossier, journaux et rapport de la racine) | 1 510 + 7 + 1 |
| PDF de tiers (`docs/sources/pdf/`, dont sous-dossiers) | 469 + 167 |
| registres de travail, copies et archives qui les contiennent | 324 + 2 + 2 + 1 |
| sortie de l'extraction (`donnees/`) | 287 |
| essais et archives de l'orchestrateur à clés factices (R-1574) | 99 + 11 |
| **sous embargo jusqu'au verdict de P3-bis** | **92** |
| pages ou textes extraits de papiers de tiers, fichiers de travail de lecteurs | 33 + 4 + 2 + 1 + 1 + 1 + 3 + 1 |
| candidatures (autre fonds, AFFINE, TAIF) | 26 + 16 + 10 |
| pages, textes, documents de sites de tiers (R-2433) | 20 + 8 + 2 + 1 + 1 + 1 + 2 (cartes de modèles) |
| articles de tiers hors arXiv (Nature, co-scientist) : PDF et pages | 5 + 5 |
| paquets git incrémentaux | 4 |
| adresse électronique de Lazar (anciens README, brouillon de page, ordre) | 2 + 2 + 1 + 1 |
| chemin personnel d'un poste de Lazar | 2 |
| adresse IP d'un serveur loué | 2 |

Le détail par motif et par chemin est dans `EXPURGE.md` de la copie (sauf l'embargo).

## Contrôles sur l'arbre construit

- Garde des secrets du script : 0. Recherche indépendante `sk-ant-…|sk-…{20,}|ghp_…|hf_…|AKIA…|AIza…` sur les 18 512 fichiers et dans les archives : 13 jetons marqués factices et 3 jetons `AIza…` dans des chaînes nommées `cle-factice` (essais de `lancement-v1` et `lancement-v2`), forme relevée masquée ; 0 valeur des 19 variables de clés de l'environnement.
- Embargo : 0 chemin sous embargo dans l'arbre (motifs nommés et `registres/`, `donnees/`, `gemini/`).
- Données personnelles : 0 au sens de la garde, sauf l'adresse de contact de Lazar dans le README public, gardée parce que la consigne garde ce README (publiée depuis le 9 octobre). 34 adresses de tiers déjà publiées (auteurs de papiers cités, mainteneurs de paquets) restent, comptées.
- README : README public de `fc9acdee` gardé en tête, avec une section « Status, 12 November 2026 » (sans chiffre ; renvoie à `EXPURGE.md` et aux registres, R-2433).

## Réserves

1. L'embargo filtre par nom : un fichier gardé qui cite ou résume le contenu sous embargo (procédures de 7b, notes de T0.6, contre-lectures) n'est pas détecté. Choix de périmètre : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/` et `audit-ecart-dt4-7a*` mis sous embargo (sorties de 7a) ; les ordres et consignes de 7b, et l'épreuve de l'étiqueteur phase 1 (verdict scellé, dépôt sur l'Open Science Framework), gardés.
2. L'historique public n'est pas réécrit : le commit `cd8f5f16` du 9 octobre porte encore les pages extraites `TRACE-AcMAS/*_pages.txt` et les anciens README avec l'adresse de Lazar ; la branche publique `claude/new-session-7qxayx` (copie du 5 novembre, script v5) n'a pas été examinée ni touchée.
3. La variable `CONTROLE_IA_GITHUB_TOKEN` est absente de l'environnement ; la poussée a utilisé `CONTROLE_IA_GITHUB_TOKEN_2` (droits lus avant : `push` vrai), passée par l'environnement de git, jamais affichée.
4. Les copies d'outils tiers sous licence libre (par exemple `sources-externes/` des lentilles de sondes) et les en-têtes HTTP des pages retirées restent.
