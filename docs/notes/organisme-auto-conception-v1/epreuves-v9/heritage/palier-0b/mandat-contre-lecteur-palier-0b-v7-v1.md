VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU CITÉ DANS UNE PIÈCE. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du contre-lecteur — préenregistrement du palier 0b, différentiel v6 → v7 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Le contre-lecteur des versions précédentes n'est plus joignable dans cette session : tu es un contre-lecteur neuf, modèle O, qui n'a écrit ni le texte ni le code ; écart déclaré à la règle « même contre-lecteur ». Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` (noté P0B).

## Ce que tu contre-lis (vérifie chaque empreinte contre son compagnon)

- `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v7.md` (`2f0f928f291b65a98bff2680e6bb7172bcf279da7e76b16bd837193f0704f4f0`)
- `P0B/remplacements-preenregistrement-palier-0b-v6-v7.json` (`a20a925f…`), le journal de l'outil `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v7.md.journal-remplacements-v1.json`, le différentiel `P0B/differentiel-preenregistrement-palier-0b-v6-v7.diff` (`4dc998f4…`)
- `P0B/rapport-redacteur-palier-0b-v7-v1.md` (`c06c2870…`) et `P0B/table-empreintes-code-v3-extraite-du-rapport-v1.txt`

## Ce qui fait foi

- Le mandat du rédacteur : `P0B/mandat-redacteur-palier-0b-v7-erratum-du-commit-v1.md` (`9f948bb1…`) et les pièces qu'il nomme par leurs chemins : la v6 (`4aee136b…`) et son contrôle (`c079a89d…`) ; le code v2, sa contre-lecture (`3778fb39…`) et l'outil `bruit_nul_doses.py` ; le code v3 (`P0B/code-v3/`), son rapport (`5e3fa3e8…`) et sa vérification (`c5c211c7…`).

## Ce que tu vérifies

1. Le différentiel est exactement l'application des 30 remplacements (rejoue l'outil `391db990…` sur la v6, compare à l'octet).
2. Les trois remplacements de tenue du contrôle v6 sont portés à la lettre.
3. **Les trois règles des écarts** : écrites d'avance, sans viser de signe (R3), sans résultat lu (R1). Le rédacteur déclare avoir écrit les règles 2 et 3 en sachant qu'à la lettre de la v6 l'étape 3 s'arrêterait probablement : juge en toutes lettres si ces règles dépendent de cette attente (R1, R3, R4), et quelles options n'en dépendent pas. Refais le calcul à la main de la réserve 23 (exactitude vraie 0,60, arrêt une fois sur trois environ), au besoin par un petit programme écrit dans ton dossier et lancé par son chemin.
4. Les classements : écart 1 en proposition avec défaut ou nœud ; causes d'arrêt ajoutées (D8, D9, choix 6) et choix 11 en information ou nœud. Tout changement de valeur gelée, de seuil, de critère ou de prédiction est un nœud sans défaut.
5. Les dix silences inscrits, les choix 11 et 12, D5, D6, D8, D9 : justes au regard du code v3 (vérifie au moins `audit.py`, `constantes.py`, `graines.py` par fichier et ligne).
6. L'erratum du commit sous condition : le commit `3d332d2c` et la table des 51 empreintes sont justes (recalcule au moins dix empreintes sur `P0B/code-v3/`), et la liste de ce qui demande un code v4 est complète.
7. Les nœuds pour Lazar sont au format (annexe H et rapport § 8).
8. Aucun identifiant de modèle.

Verdict : « Conforme », « Conforme après corrections » (liste exacte, texte ancien et nouveau ; elles seront appliquées par un rédacteur de modèle F) ou « Non conforme ».

## Ce que tu rends

Dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v7/` : `controle-differentiel-palier-0b-v7-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Signe « contre-lecteur, modèle O ».

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun tirage, aucun étalonnage, aucun audit, aucun lancement du code de l'étage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
