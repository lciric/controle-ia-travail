# Spécification — table de correspondance des champs du rejeu croisé (v2)

- **Pour** : la session habilitée qui écrit, « sans résultat », la table de correspondance des champs par laquelle le chargeur lit les scores gardés de l'apprentissage des sondes sur la tâche (texte scellé `prereg/diagnostics-prealables-sondes-v1.md`, `e8dca00b…`, Plan d'analyse, « Données du rejeu croisé » ; erratum 1 de la consigne, § 4).
- **Écrite par** le concepteur des sondes v2 (`session_013QMayjWQwDkaT8Hd9Aqvjb`), 2026-11-23. **Remplace** la v1 (`2b360049…`, gardée), après la contre-lecture (`d20bb4c0…`, défaut 9 et § 4, point 1). **Classe B** : la table qu'elle décrit est exigée par le plan d'analyse d'une ligne du texte scellé. **Aucun résultat.**
- **Calendrier** : le texte scellé veut cette table « jointe avant le scellement » ; il a été scellé sans elle. Sa jonction avec l'additif de commit attend le mot de Lazar (décisions v2, § 6, point 2) ; s'il l'accepte, aux conditions de la contre-lecture : la session qui l'écrit atteste n'avoir lu aucune colonne de score ; la table est contre-lue (classe B) ; elle est scellée et inscrite avant l'épreuve plantée et avant le verdict du test sur les adaptateurs jumeaux.

## 1. Ce que la session habilitée lit, et rien d'autre

Le fichier de la table des scores gardés (empreinte vérifiée), ses noms de colonnes, et les valeurs distinctes des seules colonnes de plan : dose, pli externe, source du texte, poids qui lisent, chemin (s'il existe), tâche tenue à l'écart (s'il existe), famille de sonde et couche (s'il y en a plusieurs). **Jamais** la colonne des scores, ni une statistique qui en dérive. Elle n'ouvre ni activations, ni verdict, ni table de l'ouvreur.

## 2. Ce qu'elle écrit

Un fichier JSON `correspondance-rejeu-croise-v1.json`, scellé (compagnon `.sha256`), avec une courte note Markdown d'attestation à côté.

```json
{
 "format": "correspondance-rejeu-croise-v1",
 "redigee_par": "<identifiant de session>",
 "date_utc": "AAAA-MM-JJTHH:MM:SSZ",
 "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
 "table_source": {"chemin": "<chemin>", "sha256": "<64 hexadécimaux>", "ligne_registre": "<SCORES-BBIS …>",
                  "format_fichier": "jsonl | csv"},
 "selection": {"<colonne>": "<valeur retenue>"},
 "colonnes": {
  "dose": "<colonne>",
  "pli": "<colonne>",
  "source": "<colonne>",
  "poids": "<colonne>",
  "chemin": "<colonne> | {\"regle\": \"quatre_cases_du_texte_scelle\"}",
  "tache": "<colonne>",
  "cle": "<colonne>",
  "score": "<colonne>",
  "longueur": "<colonne> | {\"absente\": true}",
  "pas": "<colonne> | {\"absente\": true}",
  "valeur_declaree": "<colonne> | {\"absente\": true}",
  "tache_tenue": "<colonne> | {\"constante\": true}"
 },
 "valeurs": {
  "source": {"<valeur brute>": "saboteur | honnete"},
  "poids": {"<valeur brute>": "adaptateur | nu"},
  "chemin": {"<valeur brute>": "origine | relu"},
  "tache_tenue": {"<valeur brute>": "true | false"}
 }
}
```

## 3. Règles

- **Douze champs internes**, ceux de `statistiques_v1.CHAMPS_TABLE` : chacun reçoit une colonne, ou l'une des trois règles permises ci-dessous ; aucun autre recodage.
- **`selection`** : si la table mêle plusieurs familles de sonde, couches ou courses, une seule est retenue, celle que nomme la ligne SCORES-BBIS du registre (la sonde du pli, sous laquelle le texte scellé lit les quatre cases). Le choix se fait sur le registre, jamais en regardant des scores.
- **`chemin`** : une colonne, ou la règle `quatre_cases_du_texte_scelle` (origine pour adaptateur sur textes du saboteur et pour modèle nu sur textes honnêtes ; relu pour les deux autres), permise seulement si la note atteste que la table ne porte que ces quatre cases, chacune par un seul chemin. Avec la règle, aucune action n'est à la fois en origine et en relu : le contrôle du chemin sera « absent ».
- **`tache_tenue`** : une colonne, ou `constante: true` si la table ne garde que des scores d'actions tenues à l'écart de la sonde de leur pli (attesté).
- **`longueur`, `pas`, `valeur_declaree`** : `absente: true` permis ; une variable absente sort de la régression des prédicteurs triviaux et la sortie la nomme (texte scellé : « variables présentes »).
- **`valeurs`** : recodage exhaustif ; une valeur brute non prévue arrête (garde nommée), jamais un repli. Les doses et les plis sont lus comme textes, sans recodage.
- **`cle`** : la même clé désigne la même action sous l'adaptateur et sous le modèle nu, dans un même pli et une même source ; le chargeur apparie sur (pli, source, clé).
- **`score`** : le score brut de l'action sous la sonde gelée de son pli (maximum sur les jetons), non réduit ; la réduction par pli et par dose est faite par le code.

## 4. Ce que le développeur ajoute

`charger_table_bbis(chemin_table, chemin_correspondance)` : vérifie les deux empreintes ; lit la table ; applique `selection`, `colonnes`, règles et `valeurs` ; rend des lignes aux noms internes ; appelle `charger_table_scores` avec la correspondance identité ; écrit dans la sortie du rejeu les deux empreintes, les règles employées et les variables absentes. Prédicteurs triviaux : `_interaction_residuelle` retire les colonnes absentes ou constantes. Gardes, chacune éprouvée sur un cas sain et sur un artefact (fichiers fabriqués) : empreinte fausse ; colonne nommée absente du fichier ; valeur brute non prévue ; règle des quatre cases employée alors que la table porte une ligne hors de ces cases ; clé sans sa jumelle sous l'autre poids (comptée, et la tâche sort si une source y manque, comme le texte le dit).
