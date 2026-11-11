# Plan du dépôt tiers horodaté pour le bras d'attaque (nœud 7) — v1

Session-dépôt `session_01QPDgKgcLdggoVJfGC5cBw8`, 10 novembre 2026. Branche `claude/upbeat-cray-dmauvv`.
Statut : brouillon, à contre-lire. Il complète, sans la remplacer, l'infrastructure existante.

## 0. Pourquoi

La règle du jeu exige que « moniteurs gelés avant ouverture du coffre » soit prouvable à un tiers par une **date qu'on ne
peut plus changer** (règle du jeu, nœud 7). Un tiers (Open Science Framework) horodate une empreinte ; nous ne posons pas
la date, lui la pose. Ce que ça prouve : antériorité et intégrité, rien de plus (jamais que le contenu est juste).

## 1. Ce qui existe déjà

- Script `scripts/osf_depot_v1.py` (scellé, 8 tests, cas sain et artefact) : construit un manifeste d'empreintes **sans
  réseau**, puis dépose sur l'Open Science Framework ; idempotent ; masque le jeton ; refuse un manifeste différent sous
  le même nom (R12) ; `--public` rend public ; `--a-blanc` déjà joué le 5 novembre (jeton valide, rien créé).
- Manifeste v1 `livrables/osf-manifeste-v1/manifeste-v1.json` (`dd87b23e…`) + LISEZMOI : **118 fichiers** de `prereg/`,
  `docs/decisions/`, `docs/verdicts/`, lus sur `main` au commit `a364e947`. Projet **privé, non gelé**.
- Mode de preuve pour un tiers : adresse publique ; date `date_created` de l'interface ; empreinte SHA-256 relue ; pour un
  document donné, `git show <commit>:<chemin> | sha256sum` sur la copie expurgée publique ou un accès accordé.

## 2. Les deux manques (nœud 7)

1. **Couverture** : le manifeste v1 ne contient **ni l'index du bras d'attaque, ni N-062, ni les pièces d'intégration du
   bras** (règle du jeu, brief, note de choix, décisions N-053 à N-057). Il a été lu au commit `a364e947`, antérieur à ces
   pièces.
2. **Caractère figé** : le projet est privé et un fichier d'un projet est **supprimable** ; un tiers ne peut opposer une
   date que si le projet est **public**, et l'objection « fichier supprimable » ne tombe qu'avec une **registration** (gel
   du projet, identifiant pérenne, suppression impossible) — risque 2 du rapport OSF v1.

## 3. Le plan, en deux tranches

### Tranche A — avant l'entretien (ce qui existe peut être horodaté tout de suite)

1. **Audit des chemins (préalable dur).** Le manifeste expose des **chemins**, pas des contenus ; rendus publics, les
   chemins eux-mêmes deviennent publics. Avant toute régénération :
   - **n'inclure aucun chemin du coffre** : le manifeste ne lit que `prereg/`, `docs/decisions/`, `docs/verdicts/` (et les
     pièces d'intégration retenues) ; vérifier qu'aucune branche `donnees/*`, `docs/notes/bras-attaque/`, ni fichier sous
     embargo n'y figure ;
   - **relire chaque chemin ajouté** pour qu'aucun **nom** ne trahisse un mode tenu à l'écart ni une famille de pression.
     Les pièces d'intégration (`docs/notes/integration-bras-attaque-v1/…`, `registres/index-bras-attaque-v2.md`) ne portent
     que des noms neutres ; le vérifier à l'œil, chemin par chemin, avant de rendre public.
2. **Régénérer un manifeste v2** au commit courant de `main`, incluant les dossiers v1 **plus** : `registres/index-bras-attaque-v2.md`,
   `docs/decisions/decision-N-062-v1.md`, et les pièces d'intégration scellées (`regle-du-jeu…`, `brief-session-attaquant-informe-v1.md`,
   `choix-et-anteriorite…-brouillon3.md`). Nouveau nom (`manifeste-v2.json`, R12). Scellé par Lazar.
3. **Rendre le projet public** (`deposer --public`) : la date de dépôt du manifeste v2 devient opposable.
4. **Créer une registration** du projet (gel) : l'objection « fichier supprimable » tombe. Geste de Lazar dans l'interface ;
   le script v1 ne le fait pas (extension v2 possible si on veut l'automatiser).
5. Consigner dans `registres/etat.md` et la passation : identifiant du projet, adresse, date, empreinte du manifeste v2.

### Tranche B — à chaque scellement décisif (ce qui n'existe pas encore)

À chaque gel qui doit précéder une ouverture du coffre, un **nouveau manifeste** (v3, v4, …) est déposé et gelé **avant**
l'ouverture correspondante :
- gel des **moniteurs** (scellement 3 de la règle du jeu) : le manifeste qui le date est déposé **avant** que le bras
  informé reçoive une conception ;
- scellement de la **famille aveugle** (mode tenu à l'écart) : déposé avant la porte G1 ;
- **préenregistrement du bras** (scellement 1) : déposé avant tout run du bras.

C'est la preuve de l'ordre : la date du tiers sur le gel précède la date du tiers sur l'ouverture. Sans elle, « les
moniteurs étaient gelés avant » n'est qu'une affirmation interne.

## 4. Qui fait quoi

| Étape | Qui | Note |
|---|---|---|
| Audit des chemins | session-dépôt (ici) | à l'œil, chemin par chemin ; aucun nom de mode |
| Régénérer le manifeste v2 | session-dépôt | `python3 scripts/osf_depot_v1.py manifeste --ref main …` (sans réseau) |
| Sceller le manifeste v2 | Lazar | `… scellement sceller livrables/osf-manifeste-v2/…` |
| Déposer, rendre public | Lazar | le jeton `OSF_TOKEN` est le sien ; jamais sur la ligne de commande |
| Geler une registration | Lazar | geste dans l'interface ; identifiant pérenne |
| Consigner la date | session-dépôt | `registres/etat.md`, passation |

## 5. Ce que ce plan ne décide pas

- La **date exacte** du dépôt v2 : dès que l'audit des chemins est fait et le manifeste régénéré ; recommandation, avant
  l'entretien (règle du jeu, nœud 7, recommandation (a), confiance 0,7).
- L'**automatisation de la registration** (gel) : à la main pour la v1, extension possible du script.
- Le périmètre exact des pièces d'intégration à inclure : dépend du verdict de la contre-lecture R2 de la règle du jeu
  (en cours). Si cette contre-lecture change la règle, le périmètre de la tranche A suit.

## 6. Réserve

La vérification d'un tiers passe par la **copie expurgée publique** `lciric/controle-ia` : elle doit garder octet pour
octet les fichiers scellés dont l'empreinte est au manifeste, et des commits retrouvables. Une expurgation qui altère un
fichier scellé rend son empreinte invérifiable (pas fausse). À vérifier avant de publier le manifeste : les chemins du
bras d'attaque retenus survivent-ils à `scripts/depot_expurge.py` sans altération ? Si l'expurgation retire un de ces
fichiers, son empreinte au manifeste pointe un chemin absent de la copie publique — à traiter (garder le fichier, ou
l'exclure du manifeste public).
