# Contre-lecture du collisionneur v9-v8k (cc886ae7…), v1

**Verdict : à corriger.** Cinq bloquants, dont quatre viennent des décisions de l'arbitre. Sans option, rien ne change par rapport à la v8j. Les gardes de la v8d couvrent bien Mistral et Kimi direct.

Essais : 455 passés, 11 sautés, sans aucune clé dans l'environnement.

**Ce qui tient :**
- **Sans option :** sur les 120 compositions des sept anciennes espèces, les réglages et le devis sont ceux de la v8j, au chiffre près. Seuls s'ajoutent les champs « effort high » et « appel relais ». L'entrée de journal neuve ne gêne ni le suivi des scripts ni le calcul de la dépense.
- **`--sortie-max` :** le pire cas est exact. Exemple : Fable 5.2, 50 000 jetons d'entrée et 128 000 de sortie donnent 6,90 USD.
- **Valeurs confirmées sur les pages publiques :** Opus 4.6 (identifiant, 5 / 25 USD, 128K), Fable 5.1 (10 / 50), Astra (128 000 jetons ; prix lu 8 / 40, la table reste plus haute), Mistral (identifiant, 0,7 / 2,1, comptage, fins), Moonshot (`max_completion_tokens` jusqu'à 1 048 576, morceau d'usage à `choices: []`).

## Bloquants

1. **Plafond de Kimi (l. 443).** Sous `--sortie-max`, Kimi monte à 1 048 576 jetons. L'arbitre fixe 128 000. Le pire cas d'un envoi passe alors de 10,49 à 1,28 USD, plus l'entrée.
2. **Délais inchangés sous `--sortie-max` (l. 369-404).** Produire 128 000 jetons en 3 600 s suppose 35,6 jetons par seconde. Pour Kimi, en 2 000 s, il en faut 64. Aucun fournisseur ne documente de débit.
   - Correction : une table des délais sous `--sortie-max`, ajoutée aux valeurs exigées. Une valeur manquante donne le refus nommé « valeur à fixer ». Une valeur posée est déclarée supposée, avec sa source, et journalisée.
   - Astra passe par l'arrière-plan d'OpenAI : son délai est l'échéance des relevés.
   - Une coupure est déjà traitée comme un défaut : code 2, comptée au pire, aucune cellule écrite.
3. **Opus 4.6 part sans réflexion (l. 1317).** La documentation d'Anthropic le dit : sans champ de réflexion, Opus 4.6 ne réfléchit pas ; il faut demander la réflexion adaptative. L'effort `max` y est documenté.
   - Correction : ajouter `"thinking": {"type": "adaptive"}` au corps de la seule espèce Opus 4.6.
   - Essai : le corps d'Opus 4.6 porte ce champ ; les autres corps restent ceux de la v8j.
4. **Astra sous `--effort-max` : rien n'est déclaré.** La page du modèle ne liste pas les niveaux d'effort de raisonnement. Le guide renvoie à cette page et dit seulement que `none` est rejeté.
   - Correction : déclarer l'absence (champ `effort_absent`), à l'écran, au journal du lancement et dans chaque essai. Rien n'est envoyé. Un essai à l'appui.
5. **Deux gardes d'argent sans essai (mutations survivantes).**
   - l. 1752 : un usage avec `prompt_tokens` mais sans `completion_tokens` doit donner « usage absent », compté au pire.
   - l. 2109 : garde d'entrée de Kimi direct avec un compte au-dessus de la longueur du texte divisée par deux. Elle doit valoir ⌈1,01 × compte⌉ + 32.

## Non-bloquants

- **N1.** L'usage est lu sur n'importe quel morceau du flux. Il faudrait ne l'accepter qu'au morceau de fin ou après.
- **N2.** Défaut ancien, sur tous les chemins. `urllib` suit une redirection 301, 302 ou 303 d'un envoi POST, et garde l'en-tête `Authorization` vers n'importe quel hôte (vérifié dans la bibliothèque). Correction : refuser les redirections dans `ouvrir`.
- **N3.** `--cle-anthropic` n'a pas de préfixe. Il peut donc nommer la variable de la clé de Mistral, de Kimi ou d'OpenAI. Correction : refuser les préfixes des autres fournisseurs.
- **N4.** Kimi K3.1 Pro documente `reasoning_effort` (défaut `max`). Avec `--kimi-direct --effort-max`, l'envoyer explicitement.
- **N5.** Les prix de Kimi ne sont pas relus : les tables de la page n'ont pas été rendues.
- **N6.** `--sortie-max` n'est pas scellé, et `devis-reprise` l'ignore.
- **N7.** Sans option, le texte du devis change ; ses chiffres, non.
- **N8.** Survivants sans enjeu d'argent :
  - modèle servi lu sur le dernier morceau seulement ;
  - refus d'un effort absent, branche inatteignable et non éprouvée (R5) ;
  - préfixe de la clé revérifié à l'appel.

## Points ouverts du rapport

| Point | Jugement |
| --- | --- |
| 1 | Conforme à l'arbitre ; écrire « déclaré absent » dans le refus |
| 2 et 3 | Sans objet tant que Mistral est absent |
| 4 | Bloquants 1 et 2 |
| 5 | Bloquant 3 |
| 6 | N6 |
| 7 et 8 | Acceptés |

## Mutations

16 mutants, dont 11 pris et 5 survivants.

**Pris :**
- délai total du flux ;
- garde de sortie, chez Kimi direct et chez Mistral ;
- interruption ;
- envoi et comptage de Kimi vers le serveur de Mistral ;
- second plafond ;
- chemin d'appel absent de l'essai ;
- délai d'inactivité ;
- usage final de Moonshot ;
- flux de Mistral.

**Survivants :**
- les deux du bloquant 5 ;
- les trois de N8.

Programme : `verif-v8k/mutations_v1.py`.
