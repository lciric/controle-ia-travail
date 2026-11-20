VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — course « nouvelles attaques » : question v5 (les deux couples de la note de périmètre v3) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-44 et GO-2026-11-20-46 (mot du directeur, 12:05Z : « go recos puis procede permis » ; point 1 (b) d'abord : une question v5 qui fait nommer le mode et **reste au niveau de l'idée** ; le procédé n'est demandé qu'ensuite, pour les seuls modes jugés inédits, ailleurs). Écart à un texte scellé (la question v4) : contre-lecture par un autre modèle, puis scellement par la mère.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version de la question, de la note de périmètre, de l'ordre de course, du préenregistrement court ni du devis. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (tire de `origin/main` après `git -C /home/user/controle-ia-travail fetch origin main` ; vérifie chaque empreinte)

- La question v4 scellée : `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v4.md` (`47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`), en entier.
- La note de périmètre v3 scellée : `prereg/ideation-nouvelles-attaques-v1/note-perimetre-modes-inedits-v3.md` (`dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580`), en entier : § 2 (les deux couples, à la lettre), § 1 (définition du mode), § 8 (les dix points).
- `registres/go.md`, lignes GO-2026-11-20-42, -44, -46, citées à la lettre.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu écris

1. `question-course-nouvelles-attaques-v5.md` (nom neuf), à partir de la v4, par l'outil contre-lu, un JSON écrit avec l'outil d'écriture de fichiers, chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Elle porte, et rien d'autre :
   - **le couple 1 et le couple 2** du § 2 de la note, « Avant » et « Après » mot pour mot ;
   - l'en-tête : la phrase qui dit le § 4 « égal à l'octet » à celui de la v3 retirée ou rendue juste (note, § 2, dernier alinéa) ;
   - la tenue : titre, statut, phrase de version (l'écart et sa source : GO-44, GO-46 point 1 (b), note v3 § 2).
   **Aucune règle de fond ne change** : la règle « niveau de l'idée, jamais du procédé » reste (GO-46, point 1 (b)) ; aucune case, aucun champ, aucun seuil, aucune règle de lecture. Aucun nom de personne, identifiant de registre, chemin ou empreinte n'entre dans les § 2 à 7 (partie qui peut être servie) : seul l'en-tête et le § 1 en portent.
2. Par un programme à toi (outil d'écriture de fichiers, lancé par son chemin, `python3 -B`), un relevé des motifs internes sur les § 2 à 7 de la v5 (nom et prénom du directeur, `session_`, `@`, `R-`/`N-` suivis de chiffres, `GO-20`, `lciric`, `github`, `controle-ia`, `docs/`, `prereg/`, `registres/`, `donnees/`, empreintes hexadécimales de 16 caractères et plus, `CLAUDE.md`, noms de clés en `_KEY`/`_TOKEN`) : 0 attendu, sortie écrite.
3. Le différentiel `diff -u` v4 → v5 et un rapport court `rapport-redacteur-question-v5-v1.md` : remplacements, relevé, ce que la v5 change pour les seuils (part « hors case », garde du coffre) et pour le préenregistrement court v7 (empreinte de départ de l'arrêt n° 14, sondes de refus, témoins), en remarque, jamais tranché.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-question-v5/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette** ; aucun nom ni énoncé de mode. Aucune valeur de clé. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
