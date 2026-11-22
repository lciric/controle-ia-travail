# Rapport du développeur : collisionneur v9-v8n (v1)

Pièce de classe B. Développeur : Claude Opus 5.5, 22 novembre 2026.

Cette version est une copie de la v8m (`420394f9…`), qui reste inchangée. La vérification de la v8m est en cours : rien
n'est scellé ni commité avant ses corrections éventuelles. Aucun fournisseur n'a été appelé, aucun processus n'a été
touché.

## Fichiers

| Fichier | sha256 | Contenu |
| --- | --- | --- |
| `collisionneur_v9_v8n.py` | `4bd86e650893fcaa6b1fea5c8149dd5043176c6f828c1199f6e86e788433c191` | la v8n |
| `fabriquer_v8n_depuis_v8m_v1.py` | `3b1fd5a1…` | remplacements exacts ; l'empreinte de la v8m est contrôlée |
| `test_collisionneur_v9_v8n.py` | `77b3e7be…` | copie des essais de la v8m, un seul accord (la version), et 19 essais neufs |

## Usage

Commande pour la cible, Fable 5.1 sur un dossier fini à six espèces :

```
etage3 --fable --opus --argon --kimi --astra --carbon --cle-anthropic NOM --sortie DOSSIER \
       --espece-ajoutee fable51 [--ligne-usd X] [--plafond-usd Y] [--reprise]
```

- Les options d'origine doivent être redonnées exactement : espèces, `--sortie-max`, `--effort-max`.
- `--reprise` est nécessaire si le dossier a été fini sous un autre script, ce qui est la règle de la v3.
- `--faits` et `--question` sont inutiles : les fichiers déjà scellés servent.

## Ce que fait la v8n

1. **Contrôles avant toute écriture** :
   - l'espèce est connue, et absente de la composition scellée ;
   - les options données sont égales à celles de `especes.json` ;
   - l'étage III est fini au sens de la v8d : chaque cellule III d'origine est valide, ou son absence est acceptée au
     journal ;
   - le dossier n'a pas déjà d'ajout d'une autre espèce ;
   - seule la clé de l'espèce ajoutée est contrôlée.
2. **Composition** : `especes.json` reste tel quel. La description scellée exclut l'espèce ajoutée.
   - L'ajout est scellé à part dans `espece-ajoutee.json` : espèce, identifiant, lettre suivante (G), lettres d'origine,
     empreinte de `especes.json`, options.
   - Il est journalisé une fois (`espece_ajoutee`). Les commandes `verifier` et `devis-reprise` le relisent.
3. **Cellules de l'espèce ajoutée** :
   - III.1 : servie comme aux autres, avec les mêmes blocs de faits, de question et de consigne. Le préambule est calculé
     sur sept propositions, A à F étant les « autres ». C'est un choix ; il est dit ici.
   - III.2 : elle reçoit les six conceptions III.1 d'origine.
   - III.3 : elle reçoit sa conception, les six critiques d'origine, et six pièces absentes déclarées (« … n'a pas lu sa
     conception »). Ces pièces passent par `bloc_absent` et sont marquées `absence_declaree_ajout` au journal.
   - Seule la lettre G est lancée. Jev n'audite que G. Les absences d'origine acceptées au journal sont reprises.
4. **Marque** : chaque essai porte le champ `ajoutee_apres_coup`, et `etat.md` a une colonne « Ajoutée après coup ».
   `verifier` liste à part les cellules ajoutées. Il contrôle aussi la cohérence de la marque, l'empreinte de la
   composition d'origine, et l'absence de toute cellule de l'espèce hors de l'étage III.
5. **Dépense** : le plafond porte sur la dépense totale du dossier. `--ligne-usd` ouvre une ligne neuve
   (`ligne_ajout`), qui part de la dépense du moment ; elle borne les envois de l'ajout, et la ligne d'origine reste
   seule de son type.

## Essais et mutations

Lancés sous `env -u` de toutes les clés : **537 passés, 11 sautés**.

Les essais neufs, sains et artefacts, couvrent :
- **origine intacte** : empreinte de chaque fichier d'origine avant et après l'ajout ; journal seulement allongé ; trois
  envois exactement ;
- **invites** : contenu des trois invites de G ;
- **refus avant toute écriture** : étage non fini, espèce déjà là, autres options ou espèces, espèce inconnue, clé de
  l'espèce ajoutée absente ;
- **relance** : une relance identique ne change rien ; un second ajout est refusé ;
- **dépense** : plafond sur la dépense totale, en essai sain et en artefact ; ligne neuve ;
- **le reste** : Jev, absence d'origine acceptée, vérification d'une marque falsifiée.

16 mutations, toutes prises. Programme :
`/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations_v8n.py`.

## Points ouverts

- La commande `devis` ne calcule pas le coût de l'ajout. `devis-reprise` le compte dans les tours III.2 et III.3 restants.
- `--accepter-absence` ne vise que des cellules d'origine (contrôle de la v7).
