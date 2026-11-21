# Contrôle du différentiel v6 → v7 — fiche des quatre décisions sur l'orchestrateur v68 — v1

- Signé : contre-lecteur, modèle O. J'ai écrit la contre-lecture de la v1, la vérification de la v2 et les contrôles des v3, v4 et v6, dont `controle-differentiel-fiche-orchestrateur-v68-v6-v1.md` (`86a80de15fedcacbc906befb6c0b5aee8d3ecdd47d34f540dd857268db7d7398`). Je n'ai écrit ni la v7, ni ses remplacements, ni son rapport, ni son mandat. Contrôle fait le 2026-11-20, vers 00:52Z à 00:58Z (`date -u` : 00:54:46Z).
- Lecture seule du dépôt : `git fetch origin lot/compte-organisme-v1`, tête `78c2b7c4f`, arbre propre. Une seule exécution : l'outil contre-lu `scripts/remplacer_texte_exact_v1.py` (`391db990…`), lancé par son chemin, sortie dans mon bloc-notes. Aucun code en ligne passé à un interpréteur, aucune écriture dans le dépôt, aucune commande sur le dossier d'archives interdit. Aucun refus d'outil.

## Verdict

**Conforme.** Le différentiel v6 → v7 est exactement l'application des cinq remplacements, D1 à D3 sont à la lettre de mon texte, la ligne de version est juste et rien d'autre ne change. Les deux écarts de forme signalés par le rédacteur tiennent pour une pièce qui va à Lazar. La v7 peut partir à la mère.

## 1. Pièces (empreintes recalculées, toutes égales à leur compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| fiche v7 | `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac` |
| remplacements v6 → v7 (5) | `bcc896934189ebcb4da255ee15791fc76f0746301c4a9e4a0de3dfcdb6c9b29e` |
| journal de l'outil | `52cd37d7b5b262b2e7bf8c2712549cc006f5a5823dece95dee44c42664f385c7` |
| différentiel v6 → v7 | `a3a11bf7d3c15b5f4065ab8615e40ac4f8267b023ddead95bc67eb98d43f34e3` |
| rapport du rédacteur de la v7 | `b4aac455982de786283185ce864fd47c348018317a433a10329cd5df1578654f` |
| mandat de la v7 | `aa1cee5b3afe04b5ef0e38b9f909fe9be4a5142388d000f40f28dfcb0352c04a` |
| fiche v6 ; mon contrôle de la v6 | `9c43d54a…` ; `86a80de1…` |

## 2. Les cinq points

**(1) Le différentiel est l'application des remplacements : établi.**
- J'ai rejoué l'outil contre-lu sur la v6 du dépôt avec le fichier de remplacements versé. Il rend « 5 remplacement(s) » et une sortie d'empreinte `5ddfae18…`, égale à l'octet à la v7 versée.
- J'ai refait un `diff -u` entre la v6 et la v7 : son corps a la même empreinte que celui du différentiel versé (`2e2e458e…`). Il compte trois blocs : l'en-tête et les deux endroits de la décision 2.

**(2) D1, D2 et D3 sont fidèles à mon texte : oui, à l'octet.** Le fichier de remplacements porte exactement les couples A → B de mon contrôle de la v6 (§ 4). D2 cite le rapport du rédacteur de la v1 par son chemin et son empreinte (`49df651b…`), que j'ai recalculée.

**(3) La ligne de version est juste.**
- Empreintes : v6 `9c43d54a…`, mon contrôle `86a80de1…`, verdict « Conforme après corrections ».
- Elle localise correctement les trois corrections (D1 dans les sources ; D2 et D3 dans l'enjeu et l'option (a) de la décision 2) et renvoie au différentiel joint, qui existe.
- Son statut (« différentiel v6 → v7 non encore contrôlé ») est exact à l'heure de l'écriture ; le présent contrôle le complète.
- Elle décrit correctement le reste de l'en-tête : la ligne de la v6, puis celles de la v4.
- Elle n'affirme rien de faux et ne contient aucun identifiant de modèle.

**(4) Rien d'autre ne change : oui.** Selon le rejeu, l'outil et les trois blocs du différentiel, tout le reste est égal à l'octet à la v6 : verdict, les quatre décisions, options, confiances, tableaux, réserves et sections de différentiel de fin de fiche.

**(5) La fiche est prête pour Lazar, avec la question posée sans être tranchée : oui.**
- Le verdict, point 3 (« **deux de tes mots divergent** »), et la phrase de la décision 2 (« laquelle vaut pour la lecture de la v68 ? ») sont présents et inchangés.
- La recommandation (a), confiance 0,5, ne tranche pas la divergence.
- Les deux renvois de la décision 2 mènent maintenant au bon rapport.
- Il n'y a aucun identifiant de modèle dans la v7 (recherche faite) et aucun chiffre neuf sans chemin ni empreinte.

## 3. Les deux écarts de forme signalés

1. **La quatrième occurrence de « rapport joint »**, dans le tableau du différentiel v2 → v3 (« rapport joint de la v3 »), tient. Ce tableau décrit ce qu'a fait la v3, dont le rapport était alors le rapport joint ; c'est exact en son temps et c'est un relevé historique, pas un renvoi qu'un lecteur doit suivre. La changer réécrirait l'histoire de la pièce. L'occurrence de la ligne 3 est dans la ligne de version de la v7, qui cite les mots entre guillemets pour dire ce qu'ils désignaient : elle est juste.
2. **La ligne « Version 6 » dit encore « différentiel v4 → v6 non encore contrôlé »**, et les lignes de la v4 disent « v4 non revérifiée ». Cela tient : la ligne de la v7, en tête, dit que la suite de l'en-tête parle des versions précédentes, et elle cite mon contrôle de la v6 avec son verdict. Le lecteur sait donc que ce différentiel a été contrôlé. Réécrire ces lignes ferait de la fiche une pièce sans trace de ses états successifs, ce que la règle R12 évite. La mère peut, dans son message à Lazar, citer le présent contrôle comme état final.

## 4. Remarques sans correction

- L'en-tête de la fiche est long (quatre lignes de version empilées). C'est le prix de la traçabilité ; le message de la mère à Lazar, court, en tiendra lieu.
- Mes pièces de rejeu sont dans `controle-fiche-v4/rejeu-v7/` de mon bloc-notes, non versées.
