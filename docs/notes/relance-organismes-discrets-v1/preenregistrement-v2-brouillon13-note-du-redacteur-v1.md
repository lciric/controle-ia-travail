# Note du rédacteur — brouillon 13 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon13.md` (1 673 lignes ; empreinte au rapport de remise, calculée après cette note). Brouillon 12 inchangé (`8cc1157c6793346f90a6a9801d548bdb543b1f09f9c72e001777ac60465d50c6`, vérifié).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 12.
- **Objet** : écrire les règles de conception qui corrigent un défaut réel — dans le fichier des scores des deux moniteurs à modèle de langue, produit avant l'ouverture, les clés des actions portaient la condition en clair, et une aire se calculait sur ce seul fichier (point 4 de la reprise E du relecteur) ; inscrire la version 6 du lot du côté habilité ; remplir deux cases d'après les réponses du développeur habilité. Rien d'autre ne change.
- **Sources** : deux messages du coordinateur de la session de relance, d'après la session principale et son développeur habilité. **Aucune pièce empreintée ne porte ces règles ni ces réponses** : elles sont à verser et à citer en 14.25 avant le scellement, comme les précédentes.
- **Heures (UTC, `date -u`)** : début 2026-11-19T13:07:42Z ; fini et contrôlé à 2026-11-19T13:09:33Z selon la même horloge.
- **Interdits tenus** : les mêmes ; aucun module ni notice du côté habilité ouvert ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé ni scellé. Deux fichiers neufs : le brouillon 13 et cette note.
- **Contrôles faits** : validateur — deux problèmes attendus (marque dans huit cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; les quatre reprises A à D restent des sous-chaînes exactes (l'ajout fait à 3.5 (b) vient après la phrase de la reprise D, sans la couper) ; les huit textes des moniteurs et les six fiches restent à la lettre ; table d'en-tête, 95 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 12 ; plus aucune valeur citée pour le noyau d'attention.

## 1. Table de correspondance, brouillon 12 → brouillon 13

Numéros stables. Neuf : 14.25. Tout ce qui n'est pas listé est le texte du brouillon 12 à l'octet près.

| section | changements |
|---|---|
| titre, statut, en-tête | brouillon 13 ; date ; commit ; note ; une ligne à la table des pièces (brouillon 12) |
| 3.5 (b) | après la phrase de la reprise D : le fichier produit avant l'ouverture est écrit sous identifiants opaques ; l'exclusion vaut aussi pour qui ouvrirait la table identifiant-action ou le fichier des demandes avant les cinq lignes d'ouverture |
| 6.2 | nom `moniteurs` ajouté à la forme `opaq/{lot}` (clé `bras-a-v2/opaq/moniteurs`, côté habilité) ; compte à jour : quarante-deux clés côté habilité, vingt côté analyse ; `lec6/{tâche}` : tirée par l'étape de préparation, par le module des deux moniteurs à modèle de langue |
| 6.9 | le fichier des scores par unité porte la condition en clair à dessein : il n'est écrit qu'après les ouvertures, par la lecture commune, qui seule rouvre la table |
| 6.10 | précision des poids : `bfloat16` pour les deux moniteurs (case remplie) ; noyau d'attention : plus de valeur citée, à relever |
| 8.4 | ligne neuve « identifiants opaques des scores produits avant l'ouverture » (cas sain, cinq artefacts) ; sous la table : cinq règles de conception du fichier produit avant l'ouverture, étape de préparation, deux limites écrites |
| 12 | point 8 (xi) : précision et noyau d'attention accordés |
| 13.1 | case « module des cinq moniteurs » : version 6 (tête `79f2d6db`, `e8a0775c…`), quarante-deux clés ; case « moniteurs à modèle de langue : instrument » : précision et `lec6` remplies, noyau d'attention à relever ; case « renvoi de la base » : ce que le lecteur habilité vérifie dans la version 6 |
| 13.2 | lanceur de l'étape de discrétion : ordre en six étapes — garde de production ; table ; préparation ; production ; ouvertures ; lecture commune |
| 14 | 14.25 neuf |

## 2. Les règles écrites, et ce que j'en signale

Écrites comme transmises : identifiants opaques tirés par graine ; table identifiant-action scellée à part ; étape de préparation, seule à lire les textes et la table, qui remet un fichier scellé de demandes à trois champs (identifiant opaque, message, graine) ; production qui n'écrit que cinq champs (identifiant opaque, score, état de la balise, jointure, masse faible) et refuse toute clé non opaque ; empreinte de l'ouverture prise au manifeste scellé de la production ; comptes par condition après l'ouverture ; ordre du lanceur en six étapes. Limite écrite, comme demandé : le moniteur lit le texte de l'agent, et l'opacité ne cache pas ce que ce texte laisse voir.

Aucune de ces règles ne me semble fausse. **Trois points que je signale, sans rien changer** :

1. **Le champ « jointure »** n'est pas défini dans ce que j'ai reçu. S'il permet de rattacher un score à son action sans la table, l'opacité est vide. Vérification ajoutée à la case « renvoi de la base ».
2. **Un identifiant tiré par graine n'est pas un secret.** Qui tient l'entropie, la clé et la liste ordonnée des actions peut refaire la table sans l'ouvrir. L'opacité empêche qu'une aire se calcule sur le fichier seul ; elle ne remplace ni l'ordre gardé par les lignes d'ouverture, ni la règle d'exclusion. C'est écrit comme seconde limite en 8.4. Si l'on voulait plus, il faudrait une entropie propre à cette table, tenue hors de la configuration du bras jusqu'aux ouvertures : je ne l'ai pas écrit, ce serait une règle neuve.
3. **« La table n'est ouverte que par la lecture commune »** et « l'étape de préparation lit la table » se contredisaient à la lettre entre tes deux messages. J'ai écrit : la préparation la lit en l'écrivant, puis elle n'est **rouverte** que par la lecture commune, après les cinq lignes d'ouverture.

## 3. Cases encore « À REMPLIR » (section 13.1)

| case | ce qui manque | qui |
|---|---|---|
| lecteurs et juge des ancres | modèle Claude ; versions servies ; sortie maximale ; niveau d'effort ; réglages de `gemini-4-carbon` et de `gpt-6.2-astra` ; découpage des messages | Lazar, sur le rapport de l'essai de mesure |
| lecture du juge d'une autre lignée | 2 560 actions ou 6 400, sur un chiffrage à écrire | Lazar ; session principale |
| entropie | l'entier racine | session de relance |
| moniteurs à modèle de langue : instrument | **une seule chose** : le noyau d'attention du chargement de l'agent, à relever dans l'erratum de la note du développeur habilité | développeur habilité |
| code de la base | le programme d'extraction des six conditions | session principale |
| renvoi de la base | « vérifié » ou « non vérifié : discrétion non lue » ; vérifications ajoutées : unité de permutation ; unité de l'aire décisive ; classe honnête de l'aire conditionnelle ; ce que la base lit de la table B ; dans la version 6, cinq champs seulement, champ « jointure » sans rattachement possible, fichier des demandes sans la condition | lecteur habilité |
| commit du code de l'instrument et de l'analyse | commit et empreintes, après mise d'accord avec ce brouillon et contre-lecture | session de relance |
| module des cinq moniteurs, côté habilité | pour la version 6 : chemin du module, commit et empreinte entiers, tête des essais, notice scellée ; et la pièce versée qui porte les règles de ce brouillon | session principale |

Hors de 13.1 : la **contre-lecture 10**, sur le texte aux cases remplies.

## 4. Pour le code de la relance

Rien ne change : les identifiants opaques, la table, la préparation, la production et le lanceur de l'étape de discrétion sont tous du côté habilité. La garde « tirage sans clé » de la relance doit seulement reconnaître une clé de plus, `bras-a-v2/opaq/moniteurs`, sans la tirer.
