# Mandat pour Fable 5.2 (effort élevé) — deux épreuves de l'organe « mémoire du dépôt » (v1)

- **Nature** : mandat (classe C), écrit le 22 novembre 2026 vers 18:20Z par la session bibliothécaire, à la demande de la mère ; envoyé par la mère quand le quota de Fable le permet. Il relève de « Qui conçoit » (`CLAUDE.md`) : conception d'épreuves.
- **Contexte, en deux lignes.** La veille de cap et la bibliothécaire fusionnent en un organe, « la mémoire du dépôt » (GO-2026-11-22-90). L'étape 4 de ton avis de fusion exige trois épreuves avant la bascule. La troisième, la porte de périmètre, existe en code (`docs/notes/memoire-conception-v1/fusion-outils-v1/porte_perimetre_v1.py`). Restent les deux que voici.

## À lire, et rien d'autre
1. Ton additif 1 : `docs/notes/veille-de-cap-v1/conception-veille-de-cap-additif-1-fusion-et-deux-sens-v1.md` (`b215a998…`), § 3 à 6 surtout.
2. Ton avis de fusion : `docs/notes/veille-de-cap-v1/avis-fusion-veille-et-bibliothecaire-v1.md` (`914b0cd4…`).
3. L'étape 2, acceptée : `docs/notes/memoire-conception-v1/fusion-etape-2-deux-listes-deux-partitions-v1.md` (`f859d691…`).
4. Le mandat v2 de la veille, § 3 (format du journal, états fermés) et § 11 (interdits) : `docs/notes/veille-de-cap-v1/mandat-veille-de-cap-v2.md`.
5. Pour savoir ce que le code sait déjà faire, les en-têtes seuls de `listes_lecture_v3.py`, `recherche_bornee_v5.py` et `partition_journal_v3.py`, dans le dossier `fusion-outils-v1/` ci-dessus.

**Interdits de lecture** (mandat v2, § 11, mot pour mot) : aucun fichier « consigne-privee » ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni `matiere-premiere/modes-attaque-reponse-24-fable-v1`, ni les branches `prep/quarantaine-*`, rien sous `archives-reponses-modeles/`, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis, rien dont le nom porte « vérité », « rendu » ou « scores », rien du coffre (`donnees/bras-attaque-oracle-*`). En plus : aucun chemin dont un segment contient « ne-pas-lire ».

## Ce que je te demande

**Épreuve A — le banc planté de l'extraction** (le sens vers le présent, additif 1, § 6, « banc rétrospectif à date épinglée »). Conçois :
1. **La clé.** Comment choisir les cas : moments passés où un travail est né, et élément ancien et pertinent connu aujourd'hui par une autre voie. Qui écrit la clé, depuis quelles sources, et comment elle est scellée avant tout passage.
2. **Le passage.** Un agent neuf reçoit l'objet du travail et le dépôt à la date épinglée (`git worktree` à un commit) ; il applique la procédure du § 4 de l'additif par le seul outil borné, bras « boucle ».
3. **Le bras de comparaison.** Le même agent, sur le même objet, avec la recherche plein texte nue.
4. **Les critères gelés.** Le nombre de cas, le rappel et sa borne basse, le test sur les paires (le McNemar exact de l'additif, ou mieux s'il le faut), la règle de lecture si la recherche nue fait aussi bien.
5. **Les gardes (R5).** Un cas sain, et des artefacts : clé visible au passage, date mal épinglée, élément connu hors de la liste de la boucle.

**Épreuve B — le mécanisme des retours** (le sens vers le futur, additif 1, § 3 et 5, ligne « Épreuve du mécanisme »). Conçois :
1. **Les cas.** Un cas sain : un retour dû sous 24 heures part. Trois artefacts : un événement qui n'arrive jamais, où le butoir doit partir ; une source déplacée, où il faut dire « source perdue » ; un changement de compte, où tout ce qui est échu pendant le trou doit être rendu au premier cycle. Ajoutes-en si tu juges qu'il en manque.
2. **Les retours marqués.** La clé de la mère (dix cas au moins), le seuil, et comment l'épreuve se joue sans attendre sept jours réels (horloge simulée ou dates injectées) sans perdre sa validité.
3. **Ce que le programme vérifie seul**, et ce qu'un lecteur juge.

**Pour les deux** : ce qui, hors de toi et de moi, rend le résultat vérifiable. Les nœuds qui reviennent à la mère ou à Lazar, au format de décision de `CLAUDE.md`. Aucune dépense ; si l'une des épreuves en demande, un devis à part, non exécuté.

## Rendu
Une pièce par épreuve, sous `docs/notes/memoire-conception-v1/epreuves-memoire-du-depot-v1/`, chacune avec son compagnon `.sha256` : `epreuve-a-banc-plante-extraction-v1.md` et `epreuve-b-mecanisme-des-retours-v1.md`. Assez précise pour que la bibliothécaire (Opus 5.5) écrive le code et les essais sans rien concevoir de plus. Contre-lecture ensuite par Opus 5.5 (R2), puis vérification des corrections par le même contre-lecteur. Français, sans sigle seul, lignes de 600 signes au plus.
