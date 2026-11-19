# Note du rédacteur — brouillon 15 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon15.md`, `a3526ec8884b4b7191e468dc0b50262d7b6e6a533468fe162742a47f8156ff58` (1 725 lignes). Brouillon 14 inchangé (`2b2f193a87e6ce77cb7bc22daba750b565235797c393ea207e52447079717cdb`, vérifié).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 14.
- **Objet** : porter les réponses du développeur habilité, écrites en phrases pour ce texte et déclarées sans interne de moniteur (`docs/notes/bras-a-moniteurs-v1/pour-le-texte-du-bras-a-sans-interne-v7.md`, `381036f2dec44c96f2e9ba1955e494ee9fc138e61fef0ac0d828f91d22b43382`, points 30 à 35), et l'erratum du noyau d'attention (`a-citer-au-texte-moniteurs-a-modele-de-langue-v1-erratum-1.md`, `d59b9d3a4dbc70f85b539ac98579464a0f940f7280af31cc9891e43319d626cc`). Rien d'autre ne change.
- **Fiches** : aucun fichier neuf. La fiche 7 (`decisions-bras-a-brouillon14-v1.md`, `01e5e26f…`) attend toujours Lazar ; elle cite l'empreinte du brouillon 14, et son texte est aussi celui du brouillon 15.
- **Heures (UTC, `date -u`)** : début 2026-11-19T13:44:27Z ; fini et contrôlé à 2026-11-19T13:46:45Z selon la même horloge.
- **Interdits tenus** : les mêmes ; ni le document de la base ni aucun module du côté habilité n'a été ouvert (le texte de la réserve R-BA2 est recopié de la note du développeur) ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé ni scellé. Deux fichiers neufs : le brouillon 15 et cette note.
- **Contrôles faits** : les sept citations entre guillemets de la note du développeur habilité, la limite et le texte de R-BA2b sont des sous-chaînes exactes du brouillon 15 (vérifié par programme) ; validateur — deux problèmes attendus (marque dans sept cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; reprises A à D et sept fiches à la lettre ; table d'en-tête, 101 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 14 ; plus aucune valeur `defaut` citée pour le noyau d'attention ; la clé `opaq/moniteurs` n'est plus nommée que pour dire qu'elle n'existe plus.

## 1. Table de correspondance, brouillon 14 → brouillon 15

Numéros stables. Neuf : 14.27. Tout ce qui n'est pas listé est le texte du brouillon 14 à l'octet près.

| section | changements | point de la note |
|---|---|---|
| titre, statut, en-tête | brouillon 15 ; date ; commit ; note ; trois lignes à la table des pièces (brouillon 14 ; note du développeur habilité, version 7 ; erratum) | — |
| 6.2 | ligne `opaq/moniteurs` retirée de la table des clés ; compte à jour : quarante et une clés côté habilité, vingt côté analyse ; la table des identifiants n'est tirée d'aucune clé de 6.2 (seule exception, voulue) | 31 |
| 6.9 | quatre comptes de la règle du 1 % (`n_permutations`, `permutations_degenerees`, `tirages`, `tirages_degeneres`), à la lettre ; forme exacte du fichier `scores-par-unite-moniteurs-bras-a.jsonl`, dix champs, à la lettre ; « deux fichiers, deux étapes », à la lettre | 33 ; 34 |
| 6.10 | noyau d'attention `sdpa` pour les deux moniteurs ; module en version 7 | 35 ; erratum |
| 7.7 | texte de la réserve R-BA2 et de sa voisine R-BA2b, à la lettre | 32 |
| 8.4 | ligne de garde des identifiants opaques réécrite (listes fermées ; engagement ; cinq artefacts de la table) ; sous la table : champ « jointure », à la lettre ; seconde limite réécrite, à la lettre ; entropie propre de la table, à la lettre ; écart à R9 déclaré | 30 ; 31 |
| 12 | point 8 (xi) : `sdpa` | erratum |
| 13.1 | cases « moniteurs à modèle de langue : instrument », « réserve R-BA2 » et « code de la base » : **remplies** ; case « module des cinq moniteurs » : version 7, remplie sauf l'épreuve par retrait et la notice ; case « renvoi de la base » : lettre mise à jour pour la version 7 | 35 ; 32 |
| 13.2 | lanceur de l'étape de discrétion : entropie propre à l'étape « table », engagement au manifeste de la production, contrôles de la lecture commune, nom du fichier des scores par unité | 31 ; 34 |
| 14 | 14.27 neuf | — |

## 2. Deux points que je signale

1. **L'entropie propre de la table est un écart à la règle gelée R9** (graines dérivées par `SeedSequence` de l'entropie du bras, consignées au manifeste). C'est moi qui ai proposé cette entropie au brouillon 13, et la session principale l'a retenue. Je l'ai écrit comme écart déclaré, avec ce qui le borne : elle ne tire aucune donnée d'analyse ; elle est consignée dans le fichier scellé de la table ; le tirage se rejoue à l'ouverture ; le manifeste de la course la porte après l'ouverture. **Un écart à une règle gelée appartient à Lazar** : s'il n'a pas été posé, c'est une ligne à lui poser avant le scellement.
2. **Le texte de la réserve R-BA2 n'est pas vérifié par moi contre le document de la base**, que je n'ouvre pas : il est recopié de la note du développeur habilité. La case le dit, et la vérification est ajoutée à la lettre de la case « renvoi de la base ».

## 3. Cases encore « À REMPLIR » (section 13.1)

Sept ; trois de moins qu'au brouillon 14.

| case | ce qui manque | qui |
|---|---|---|
| nœuds | mot de Lazar, ou défaut échu, sur le point 16 (fiche 7) ; date d'envoi | Lazar |
| lecteurs et juge des ancres | modèle Claude ; versions servies ; sortie maximale ; niveau d'effort ; réglages de `gemini-4-carbon` et de `gpt-6.2-astra` | Lazar, sur le rapport de l'essai de mesure |
| lecture du juge d'une autre lignée | 2 560 actions ou 6 400, sur un chiffrage à écrire | Lazar ; session principale |
| entropie | l'entier racine | session de relance |
| renvoi de la base | « vérifié » ou « non vérifié : discrétion non lue » ; le lecteur habilité, mandaté par la session principale sur la version 7, vérifie aussi l'unité de permutation, l'unité de l'aire décisive, la classe honnête de l'aire conditionnelle, ce que la base lit de la table B, l'opacité (cinq champs, listes fermées, entropie propre de la table, fichier des demandes sans la condition), et les textes de R-BA2 et de R-BA2b | lecteur habilité |
| commit du code de l'instrument et de l'analyse | commit et empreintes | session de relance |
| module des cinq moniteurs, côté habilité | l'épreuve par retrait de la version 7 et sa notice | session principale |

Remplies au brouillon 15 : moniteurs à modèle de langue (instrument) ; code de la base (programme d'extraction) ; réserve R-BA2. Hors de 13.1 : la **contre-lecture 10**, sur le texte aux cases remplies.

## 4. Pour le code de la relance

- **Fichier des scores par unité** : `scores-par-unite-moniteurs-bras-a.jsonl`, une ligne JSON par moniteur, dose et unité, dix champs dans l'ordre `moniteur`, `dose`, `cle`, `condition`, `tache`, `episode`, `pas`, `pli`, `etiquette`, `score` ; `pas` nul pour l'agrégateur ; `dose` écrite `dose-0.25` à `dose-1.00`. C'est ce que le code supposait ; à confronter champ par champ.
- **Règle du 1 %** : lire les quatre champs `n_permutations`, `permutations_degenerees`, `tirages`, `tirages_degeneres` (et non deux champs nommés par le développeur de la relance) ; ils peuvent être vides quand le moniteur n'est pas calculable pour une cause antérieure.
- **Graines** : la clé `bras-a-v2/opaq/moniteurs` n'existe plus ; la garde « tirage sans clé » ne doit plus la reconnaître.
- **Réserve R-BA2** : son texte et celui de R-BA2b sont maintenant au texte (7.7) ; le code n'a plus à les exiger de la configuration.
