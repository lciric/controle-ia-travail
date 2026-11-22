# Lecteur habilité — lanceur de l'étape de discrétion v2 et configuration de course v1 — rapport interne v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `docs/notes/bras-a-contre-lecture-habilitee-v1/lanceur-discretion-v2-et-configuration-sans-interne-v1.md` (écrite sur `main` sans commit ; la mère la scelle).

Écrit par un lecteur habilité (Opus 5.5, agent neuf), le 2026-11-22 vers 21:48Z (`date -u`), sous le mandat `docs/notes/bras-a-contre-lecture-habilitee-v1/mandat-lecteur-habilite-lanceur-discretion-v2-et-configuration-v1.md` (`e65415a7b46cb44490a6fbb74ed2fdf000684fd8bc93da9540992aa2a6e24d13`, compagnon égal), restes (b) et (c). Classe B. Arbre de travail à moi, branche `claude/bras-a-habilite-developpeur-v1`, tête de départ `483a5d442`. Aucun appel payant, aucune clé, aucune sortie de course ouverte ; rien lu sous `archives-reponses-modeles/`, aucune consigne privée, aucune conception ii-b, ni `lot/compte-4-v1`.

## (b) Lanceur de l'étape de discrétion, version 2

| | chemin | commit | empreinte |
|---|---|---|---|
| lanceur v2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py` | `848c17649d3c324461747daa99fb8784c88a8baa` | `c3840745ccaad9b889b676ff7ac2450397f60192b72391e2c42ec37eb5e5ca7e` (compagnon égal) |
| ses essais | `tests/test_bras_a_v2_habilite_lanceur_discretion_v2.py` | idem | `7729f5bdd09c99af56170663b37899365ef985395d61ec3363b1c9e9141e7760` |

Le lanceur n'a pas changé depuis `848c17649` (aucun commit ne le touche jusqu'à `483a5d442`) ; aucune version 3 n'existe dans son dossier.

**Réserve C9 : non levée.** Les réglages de déterminisme ne sont toujours versés au manifeste qu'après la boucle de production (`manifeste.contenu["determinisme"] = getattr(charger, "reglages", None)` juste après `for m in A.PRODUCTEURS:` dans `discretion`) ; la boucle n'est pas enveloppée d'un `try/finally`. Une panne en production laisse donc `determinisme: null` au manifeste d'arrêt (que `principal` scelle sous `arret`), alors que la carte a été réglée. La correction de la vérification habilitée (`docs/notes/bras-a-moniteurs-v1/verification-habilitee-lanceur-discretion-v2-v1.md`, partie 2) reste à faire à la prochaine version ; comme elle le dit, aucun score, aucune garde ni aucun ordre n'en dépend, et je ne tiens pas la course à elle. Si la mère veut la lever avant la course : version 3 du lanceur (R12), deux lignes, un essai à panne en production qui exige des réglages non nuls au manifeste d'arrêt, puis contre-lecture classe B.

Rejoué : lanceur v2 et essais de la configuration ensemble, `37 passed` (30 + 7).

## (c) Configuration de course, version 1

| | chemin | empreinte |
|---|---|---|
| configuration | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-v2-course-v1.json` | `1e0907d88d534b3578d2380842ebe145a86af55168de62e42c48e5c56ec583ce` |
| ses essais | `tests/test_bras_a_v2_habilite_config_lanceur_discretion_v2_course_v1.py` | `d3f9b613f06a7ddb063c71a86bd2016765894ed0f67007b9fa0284411b6312d5` |

Construite depuis le gabarit v2 (`9a944d74…`), dont elle ne diffère que par une clé : `texte_scelle` = `{"chemin": "prereg/T0.7-organismes-discrets-v-a-v2.md", "sha256": "EMPREINTE_TEXTE_V2_BRAS_A"}`. Le dossier des rangs est `donnees/bras-a-v2-discretion/rangs-par-unite` (celui proposé, déjà au gabarit), disjoint de la sortie `donnees/bras-a-v2-discretion/sortie-lecture-commune` et des cinq autres dossiers. Les treize modules sont cités à leur empreinte (les douze présents sur la branche égaux à leur fichier ; le module d'entrée à `cb668bb9…`, sur la branche de la relance seulement).

Le marqueur `EMPREINTE_TEXTE_V2_BRAS_A` y figure une seule fois. Il est refusé deux fois : par la garde `exiger_marqueur_remplace` du fichier d'essais, et par le lanceur lui-même (`_fichier_cite` exige 64 caractères hexadécimaux minuscules ; motif « texte scellé »).

Essais, **7 passés sur 7** :
1. compagnon égal, clés dans l'ordre du lanceur, seule différence au gabarit : le texte scellé ; mode réel, 2 000 et 2 000 ;
2. dossier des rangs fixé ; dossiers disjoints (cas sain), sortie placée dans les rangs refusée (artefact) ;
3. modules à leur empreinte ;
4. marqueur unique, au seul texte scellé ;
5. garde du marqueur : copie avec marqueur refusée, configuration versée refusée (artefacts) ; marqueur remplacé par une empreinte entière admis (cas sain) ; empreinte en majuscules refusée ;
6. lanceur : les clés laissées à fixer reçoivent des valeurs factices ; avec le marqueur, refus sur le texte scellé (artefact) ; marqueur remplacé, configuration admise en ligne de commande (cas sain) ;
7. la configuration versée reste refusée par le lanceur (valeurs nulles).

Retrait éprouvé : la condition du marqueur retirée de la garde, l'essai 5 échoue ; fichier remis à l'identique (`d3f9b613…`).

## Écarts et points pour la mère

1. **Chemin du texte scellé supposé.** Le nom final du texte du bras A n'existe pas encore ; j'ai pris `prereg/T0.7-organismes-discrets-v-a-v2.md` (suite des noms `…-v-a-v1.md`, `…-v-a-v2-brouillon5.md`). S'il diffère, le chemin est à changer en même temps que le marqueur.
2. **Remplacement du marqueur en version neuve (R12).** Les essais 1, 4, 5 et 7 portent sur le fichier v1 tel que versé. Le remplacer sur place les ferait échouer et changerait une pièce scellée : je recommande d'écrire la configuration remplie sous `…-course-v2.json`, scellée, la v1 gardée.
3. **Sept valeurs restent nulles**, que le mandat ne me donne pas et que je n'ai pas inventées : registre des accords figé, rejeu, configuration du bras, tâches, statistique de l'agrégateur, réglages de la lecture, jetons de fin du moniteur boîte noire (ces derniers par `relever-fins`). Tant qu'elles le sont, le lanceur refuse la configuration (essai 7). Elles sont à fixer dans la même version neuve, avant la contre-lecture prévue par le mandat.
4. La garde du marqueur vit dans le fichier d'essais, pas dans le lanceur (le lanceur n'est pas changé) ; le lanceur la double par sa propre garde de format.
