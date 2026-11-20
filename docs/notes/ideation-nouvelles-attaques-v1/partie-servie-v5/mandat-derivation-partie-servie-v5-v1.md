VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat — dérivation de la partie servie de la question v5 (course « nouvelles attaques ») et son journal — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-44 point 1 (« (b) dérivée ») et GO-2026-11-20-46 (points 2 et 7, recommandations de la note de périmètre v3 retenues : la dérivation part de la v5 ; partie servie = option (b) du point 7), et la décision de la mère (12:07Z) sur le gabarit. Ensuite : rejeu de l'extraction et lecture entière par un contre-lecteur d'un autre modèle, puis scellement par la mère.

## Qui

Un dériveur neuf, modèle F, qui n'a écrit aucune version de la question, de la note de périmètre, ni l'avis sur la partie servie. Tu signes « dériveur neuf, modèle F ».

## Ce qui fait foi (tire de `origin/main` après `git -C /home/user/controle-ia-travail fetch origin main` ; vérifie chaque empreinte)

- La question v5 scellée : `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v5.md` (`eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`), en entier.
- La note de périmètre v3 scellée : `prereg/ideation-nouvelles-attaques-v1/note-perimetre-modes-inedits-v3.md` (`dd6fea0e…`), § 7 et § 8, point 7 ; et son compagnon `avis-partie-a-servir-v2.md` s'il est sur main (chemin tiré de la note).
- L'avis de Fable sur la forme : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/question-v4/avis-partie-servie-question-v4-v1.md` (`e052b7a9…`).
- `registres/go.md`, lignes GO-2026-11-20-44 et -46.

## La règle (point 7 (b), retenu)

Servir : le § 4 (texte de la v5), la liste des champs d'une fiche (§ 5, le contrat de sortie), **la seule case tirée du proposeur**, et en légende les noms des trois axes et la liste des valeurs de chaque axe **sans la colonne « source »** ; ne servir ni le compte des cases, ni la famille tenue à l'écart, ni aucun renvoi interne (règle, décision, GO, chemin). Décision de la mère sur le gabarit : extraction **à l'octet**, zones données par leurs lignes, mises bout à bout dans l'ordre, sans transformation ; **un seul emplacement de case**, nommé, unique et balisé (par exemple une ligne propre `{{CASE}}` — dis ton choix et pourquoi il ne peut pas apparaître ailleurs) ; le véhicule le remplit par un identifiant neutre de la case, jamais un nom de fichier ni une graine ; la garde de motifs s'applique à la requête assemblée.

**Si une zone voulue n'est pas extractible à l'octet** (par exemple une table dont il faut retirer une colonne), ne transforme rien en silence : dis-le, propose la plus petite opération écrite et rejouable (retrait d'une colonne nommée, par programme), et marque-la comme le seul écart à « sans transformation », à trancher par la mère.

## Ce que tu écris

1. `deriver_partie_servie_v5_v1.py` (outil d'écriture de fichiers ; bibliothèque standard) : il lit la v5, vérifie son empreinte, extrait les zones (lignes de début et de fin, en constante), insère l'emplacement de case à sa place, écrit `partie-servie-question-v5-v1.md` et le journal ; aucune autre opération.
2. `partie-servie-question-v5-v1.md` : le gabarit, sans en-tête.
3. `journal-derivation-partie-servie-v5-v1.json` : empreinte de la source, zones (lignes, empreinte de chaque zone), emplacement de case, empreinte de sortie, commande exacte, version de Python.
4. Un relevé des motifs internes sur le gabarit (nom et prénom du directeur, `session_`, `@`, `R-`/`N-` suivis de chiffres, `GO-20`, `lciric`, `github`, `controle-ia`, `docs/`, `prereg/`, `registres/`, `donnees/`, empreintes hexadécimales de 16 caractères et plus, `CLAUDE.md`, noms de clés en `_KEY`/`_TOKEN`, et « famille tenue à l'écart », « tenue à l'écart », « source », compte des cases) : 0 attendu, sortie écrite.
5. Un rapport court `rapport-derivation-partie-servie-v5-v1.md` : zones choisies et pourquoi (par la règle), ce qui n'est pas servi, l'emplacement de case, le relevé, la taille en octets du gabarit (pour le devis et la sonde de l'espèce 6), écarts et remarques.

Joue le programme deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN`), sorties égales à l'octet. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/derivation-partie-servie-v5/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucune recette** ; tu ne récris pas le texte. Aucune valeur de clé. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
