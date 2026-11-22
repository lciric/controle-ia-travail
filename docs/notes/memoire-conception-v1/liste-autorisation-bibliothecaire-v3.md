# Liste d'autorisation de lecture de la bibliothécaire (v3)

- **Version 3** (22 novembre 2026, vers 13:40 UTC) : un seul ajout, sur la vérification des outils de l'épreuve (verification-outils-epreuve-v4-v1.md) : tout chemin dont un segment contient « ne-pas-lire » est exclu (banque de l'épreuve, réponses et verdicts des essais), pour tout lecteur, la bibliothécaire comprise.
- **Version 2** (22 novembre 2026, vers 12:50 UTC) : liste approuvée par la mère (12:13Z) ; règles provisoires confirmées par Lazar (`GO-2026-11-22-57`, « go recos » sur la réponse 32). Un seul ajout, accordé par la mère (12:45Z) : l'audit défensif d'octobre, `docs/notes/audit-controle-v1/audit-litterature-v1.md` (`29b32f62…`), origine de l'invariant N-053 (§ 1, point 8). La liste vaut pour toutes les questions, celles de Lazar comprises ; un fichier exclu se demande à la mère, qui l'ouvre elle-même.
- Date (v1) : 22 novembre 2026, vers 12:20 UTC. Auteur : session bibliothécaire (Claude Opus 5.5), fille de la session mère. Pièce de classe C (travail), proposée ; application provisoire des recommandations D1 à D5 de la réponse 32 de Fable (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-32/relecture-fable-api.md`, sur `main`), en attendant le mot de Lazar.
- Règle (D1, option (b)) : je ne lis que ce qui figure ci-dessous. Tout le reste est « hors périmètre » : je ne confirme ni n'infirme. La liste est alignée sur le rôle le plus restreint qui peut m'interroger, c'est-à-dire un concepteur de moniteurs ou de sondes tenu à l'écart du mode de sabotage réservé, des résultats chiffrés cloisonnés et des conceptions d'attaque ; les dérivés (transcriptions, résumés, comptes rendus d'agents) suivent la règle de leur source.
- État épinglé : la note v1 est bâtie sur `main` à `5b596acc` (branche `claude/bibliothecaire-v1`). Tout fichier versé depuis est « postérieur au scellé » jusqu'à la prochaine édition.

## 1. Autorisé

1. Les documents qui font foi : `CLAUDE.md`, `docs/brief-claude-code-programme-complet-v2.md`, `docs/programme-controle-ia-v2.md`, `docs/etat-de-l-art-controle-ia-v1.md`.
2. `docs/decisions/` en entier (décisions, errata, contre-lectures, vérifications, lignes pour `CLAUDE.md`), sous la réserve du § 3.
3. `docs/notes/seconds-regards-sabotage-inventaire-v1/` (l'inventaire et son compagnon).
4. `docs/notes/demandes-fable-api-2026-11-22-v1/` : les `demande-*.md`, les `question-neutre-*`, les consignes de méthode (`consigne-demande-approfondie-*`, `consigne-relecture-*`, `consigne-correction-*`), `contexte-programme-v1.md`, `copies-sans-nom-v1/`, et les `reponse-*/relecture-fable-api.md` et `compteurs.json` ; sauf la demande 24 et tout ce qui porte « 24 » ou « SEQUESTRE ».
5. Les notes de conception des 21 et 22 novembre nommées comme sources par l'inventaire ou par les décisions N-075 à N-077, lues comme textes de conception : `mecanisme-adjudant-hors-distribution-v1/`, `adjudant-opus-independant-v1/`, `science-de-la-detection-v1/`, `pince-hors-distribution-v1/` (étau solide, étau D-4 compris), `papier-dopamine-moniteur-v1/` (conception du moniteur de dissonance, sans aucun résultat), `protocole-x-*` (dommage, attaquant, contrôle diffus, boucle audit-recapture, dommages plantés par un tiers, marge asymétrique ; pas `protocole-x-programmation-de-poids-v1/` avant vérification qu'il ne décrit pas une attaque), `percee-controle-securite-v1/` (côté défense seulement : jamais le § 7.2 côté menace), `percee-apres-blindfold-v1/`, `attaquant-informe-v1/` et `asymetries-attaquant-v1/` (côté défense : épreuves, bases, règles ; jamais le détail d'une politique d'attaque), `avis-fable-noeuds-attaquant-v1/` (même réserve), `problematique-programme-v1/`, `note-problematiques-programme-v1/`, `couverture-de-l-oracle-v1/`, `percee-revue-v1/`.
6. `registres/` : `etat.md`, `rappels.md`, `go.md`, `decisions.md`, `veille*`, `passations/` ; ligne par ligne, sauf la ligne R-2059, et sans jamais recopier un chiffre cloisonné (§ 3).
7. L'historique git de `main` et de ma branche (messages de commit, dates), sans ouvrir par l'historique un fichier exclu.
8. `docs/notes/audit-controle-v1/audit-litterature-v1.md` (ajout v2).
9. Mes propres pièces sous `docs/notes/memoire-conception-v1/`, sauf tout dossier dont le nom contient « ne-pas-lire » (v3) et `epreuve-banque-ne-pas-lire-bibliothecaire-v1/` (banque de l'épreuve : jamais lue par la bibliothécaire, seulement ses comptes et empreintes).

## 2. Exclu (hors périmètre)

1. Tout fichier ou dossier dont le nom porte « consigne-privee », « conception-ii-b », « verite », « rendu », « scores », « SEQUESTRE ».
2. `brouillons/ii-b-saboteur-budget-v1/`, et tout chemin sous `archives-reponses-modeles/`, `quarantaine/`, `matiere-premiere/`.
3. Toute branche autre que `main` et `claude/bibliothecaire-v1` : en particulier `lot/compte-4-v1`, `matiere-premiere/*`, `sauvegarde/*` (dont `bloc-notes/` et `reponses-modeles-exclues/`).
4. Les transcriptions de sessions et d'agents, même caviardées, et leurs archives (dérivés non cloisonnés par nom).
5. Les résultats des expériences 7a, 7b, T0.6, de l'étape B, de l'étape B bis, de P3-bis, et tout score ou toute table du barreau 5 : donc `diag/`, `runs/`, et les notes de résultats (par exemple `P3-mesures-*`, `audit-symetrie-*`, `barreau5-*`, `barreau8-*`, `essais-dates-t06-v1/`, `lecture-sondes-bbis-par-lentilles-v1/`, `lentilles-sondes-p3-v1/`, `regeneration-sondes-p3-v1/`, `prealables-course-etape-b-bis-v1/`, `brainstorm-suite-P3-v1/`).
6. `prereg/` : hors périmètre par défaut (un préenregistrement peut décrire le mode tenu à l'écart) ; ouvert seulement sur mot de Lazar ou de la mère, fichier par fichier.
7. La demande 24 et la réponse 24 (nouveaux modes d'attaque) ; toute pièce dont l'objet est la conception d'un mode de sabotage ou d'une politique d'attaque.
8. Toute machine, tout appel à un modèle externe, toute dépense.

## 3. Règles d'usage

- Une ligne autorisée (registre, décision) qui cite un chiffre cloisonné : je dis qu'un résultat est consigné à tel endroit, sans le chiffre.
- Un renvoi d'un fichier autorisé vers un fichier exclu ne s'ouvre pas ; je le signale.
- Dans le doute, je n'ouvre pas et je le dis à qui m'interroge.
- Trois négatifs distincts : « non trouvé dans ce que j'ai lu » ; « hors périmètre, je ne confirme ni n'infirme » ; « trouvé, sources en désaccord ».
