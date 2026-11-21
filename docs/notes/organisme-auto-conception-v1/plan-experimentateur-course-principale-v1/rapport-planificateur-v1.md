# Rapport du planificateur — branchement de l'expérimentateur et des tests de mort sur la course principale — v1

- Auteur : planificateur du branchement de l'expérimentateur, modèle F. Je n'ai écrit aucun orchestrateur, aucune conception de véhicule, aucune pièce du palier 1.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:07:01Z.
- Mandat : `docs/notes/organisme-auto-conception-v1/mandat-planificateur-experimentateur-tests-de-mort-course-principale-v1.md`, `e4ca4586cd603fbf79486752604158fca8c5595d51e6af26e0309ce0f35d80d0`, égale à son compagnon ; lu en entier.
- Processeur seul : aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune machine louée, aucun code lancé, aucune écriture dans un dépôt, aucun commit. Rien n'a été ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`.
- **Aucun refus de permission, de classifieur ni de garde n'a été rencontré.**
- **La note de conception générale n'est pas arrivée** avant la fin du travail : le plan est rendu « en attente de la note ».

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/planificateur-experimentateur-course-principale/`. Chaque pièce a son compagnon `.sha256`.

| pièce | objet |
|---|---|
| `plan-experimentateur-tests-de-mort-course-principale-v1.md` | les six parties demandées |
| `rapport-planificateur-v1.md` | ce rapport |
| `table-empreintes-planificateur-v1.md` | les empreintes des pièces lues et du plan |

Exclues du versement : `lecture-registre-origin-main.md` et `lecture-go-origin-main.md`.

## 2. Pièces lues

Empreintes entières à la table jointe ; toutes recalculées par moi.

| pièce | lecture |
|---|---|
| `registres/go.md`, `origin/main` au commit `332080c5…` | l. 508, 536, 541, 600 à 615 ; recherches par mot |
| `registres/decisions.md`, même commit | l. 4020, 4173 à 4204, 4221, 4229, 4269, 4501, 4505 à 4524 ; recherches par mot |
| additif des interrupteurs v69, v4 (`cb352811…`) | en entier ; égale à R-4131 |
| cadre de la v70, v3 (`b1822613…`) | en entier ; égale à R-4131 |
| rapport du développeur de la v68 (`ad42b722…`) | en entier |
| contre-lecture de la v68 (`d2cfeac1…`) | en-tête et constats 1 et 2 |
| fiche des quatre décisions v7 (`5ddfae18…`) | décisions 3 et 4 en entier ; le reste par ses titres |
| conception du véhicule NA-1 (`675f8d39…`, égale à son compagnon) | en entier |
| rapport du concepteur de NA-1 (`ceffd7aa…`) | l. 1 à 60 |
| lanceur de course v10 (`f4196ec5…`) | l. 1 à 140 et 526 à 625 |
| `etage_entre_generations_v57.py` (`e4bf3681…`) et `ideation_v59.py` (`5419137c…`) | en entier ; empreintes égales à celles qu'épingle le lanceur v10 |
| devis de l'héritage v5 (`30c87fa6…`) | lignes rendues par une recherche de mots (§ 5 surtout) |
| verdict de la course v67 (`d7902432…`) | quatre lignes (dépense, durée) |

**Empreinte seule, non ouvertes** : le manifeste du paquet v68, `course2_v68.py`, le résumé de l'essai à blanc, les lanceurs v9, l'épreuve des témoins v9, `tests_de_mort_v5.py`, `tour_ferme_v64.py`, la configuration v5, le préenregistrement v2, l'additif v2i, la configuration des interrupteurs, l'ordre de passage v3, les rapports du rang 0, le rapport du palier 0a.

## 3. Ce que la lettre ne fixe pas

1. **Ce qu'un test de mort éprouve sur une carte d'auto-conception.** Aucune pièce lue ne le dit ; la fiche v7 écrit qu'il n'existe aucune tranche de données pour cette course. Plan, § 2.1 et D2.
2. **Si la ligne GO-2026-11-21-16 étend le régime à la course principale.** Elle l'étend à la course « seuil et moniteurs » et dit une priorité. Plan, D1.
3. **Si (3a), « champs de fiche inchangés », tient encore.** Plan, D2.
4. **Le nombre de générations de la course principale** avec étage. J'ai pris trois pour le devis, en le disant.
5. **Comment l'héritage d'une génération est récompensé et quel coût est rendu au signal** (N-044, N-045) : aucune pièce lue ne le fixe pour cette course.
6. **Si les juges et l'aiguilleur restent joués** sur la course principale quand l'étage tourne.
7. **Le nom de version.** Plan, D3.
8. **Le chantier des mathématiques nouvelles**, que nomme le même mot de Lazar : hors de ce plan, par la précision de la mère.

## 4. Écarts

1. **Note non intégrée.** Son chemin ne m'a pas été envoyé. Je n'ai rien cherché sous `docs/notes/experimentateurs-et-tests-de-mort-v1/`, faute de nom de fichier.
2. **Conception « seuil et moniteurs » non ouverte.** Le mandat ne donne que son dossier ; aucune commande de liste n'est permise. J'ai essayé sept noms probables par `sha256sum` et par l'outil de lecture, tous absents, puis j'ai arrêté. J'en tiens ce que dit R-4377.
3. **Chemin de l'additif trouvé hors du registre.** Le registre donne l'empreinte (R-4131), non le chemin. Je l'ai tiré de la table d'empreintes du concepteur de NA-1 (qui nomme la v1), puis vérifié par `sha256sum` sur le nom de la v4 : `cb352811…`, égale.
4. **Plusieurs chemins dans une seule commande `sha256sum`**, trois fois (une fois pour des noms à essayer). Une commande simple, sans joker ni liste, mais plusieurs arguments.
5. **Commandes `grep` et `wc` sur un fichier nommé**, jamais récursives, pour relever des chemins et des tailles.
6. **Prix non relevés.** Le devis du bac repose sur un tarif cité par la fiche v7, que je n'ai pas revérifié dans le registre des dépenses.
7. **Heure.** `date -u` rend 07:07:01Z, soit quatre minutes après la dernière ligne du registre lue (R-4386, 07:03:03Z).

## 5. Pour la mère

- Le plan pose sept décisions ; D2 commande E2 et E3 et attend la note.
- Recommandation d'ordre (D5) : le sommet d'étage du palier 1 écrit d'abord, pour N générations dès l'écriture, puis cette course sur ce socle.
- Dès que la note arrive : une v2 du plan la cite, lui confronte le § 2.1, D2 et les lots E2 et E3, et dit ce qui change.

— planificateur du branchement de l'expérimentateur, modèle F
