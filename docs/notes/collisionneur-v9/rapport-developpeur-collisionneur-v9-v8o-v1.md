# Rapport du développeur : collisionneur v9-v8o (v1)

La v8o est une pièce de classe B, écrite par Claude Opus 5.5 le 22 novembre 2026. C'est une copie de la v8n
(`4bd86e65…`, inchangée), corrigée selon `verification-collisionneur-v9-v8n-opus-v1.md`. Rien n'est scellé ni commité.
Aucun fournisseur n'a été appelé.

## Fichiers

| Fichier | sha256 | Rôle |
| --- | --- | --- |
| `collisionneur_v9_v8o.py` | `81c1ca2212eab4b65164b2b1afac6edc37c854da6e43223091a1fb91cb8cf9bd` | script corrigé |
| `fabriquer_v8o_depuis_v8n_v1.py` | `24d5ba37…` | remplacements exacts, empreinte de la v8n contrôlée |
| `test_collisionneur_v9_v8o.py` | `5d325ddb…` | copie des essais de la v8n (`77b3e7be…`), quatre accords marqués « v9-v8o », section v9-v8o en fin de fichier |

Les quatre accords :
- la version ;
- `--ligne-usd 40` ajouté là où un essai lance l'ajout (aide `ajouter`, essai de Jev) ;
- les champs du parseur ajoutés dans l'appel direct de `preparer_ajout`.

## Changements

1. **Bloquant 1.** Avec `--espece-ajoutee`, les options `--rejuger-essai`, `--accepter-absence` et `--accepter-motif`
   sont refusées (code 1). Le refus a lieu dans `preparer_ajout`, avant toute écriture. Il y a un essai par option, avec
   les empreintes du dossier comparées avant et après.
2. **Bloquant 2.** `--ligne-usd` est exigé avec `--espece-ajoutee` (code 1), avant toute écriture. L'ajout ne dépense
   donc jamais sur la ligne du run d'origine.
3. **Préambule.** L'invite de l'espèce ajoutée reçoit une ligne juste après le préambule, avant les faits : « La
   proposition G est ajoutée après coup : les propositions A, B, C, D, E, F ont écrit leurs tours III sans la connaître. »
   Les invites d'origine ne la reçoivent pas.
4. **Devis.** `devis --espece-ajoutee ESPECE` chiffre les trois cellules III de l'ajout (`devis_ajout`).
   - La borne est celle de `devis`. On y ajoute les balises des six pièces absentes de III.3.
   - Le total avec relances suit `nombre_relances` (deux chez Anthropic sous `--effort-max`).
   - Pour Fable 5.1 sur les six espèces, avec des faits courts : 8,66 USD au pire sans relance, 19,58 USD avec une
     relance par cellule.
   - Sans l'option, le devis est celui de la v8n.
5. **Verifier.** Deux contrôles ont maintenant leur essai : l'empreinte d'origine (N11) et une cellule de G hors de
   l'étage III (N13).

Sans `--espece-ajoutee`, rien ne change par rapport à la v8n.

## Essais et mutations

Lancés sous `env -u` de toutes les clés : **545 passés, 11 sautés**.

| Mutation | Prise |
| --- | --- |
| R1 : options d'origine admises | oui |
| R2 : rejugement seul admis | oui |
| R3 : ligne non exigée | oui |
| R4 : préambule sans la ligne d'ajout | oui |
| R5 : devis sans l'ajout | oui |
| R6 : devis de l'ajout sans relances | oui |
| N11 : empreinte d'origine non contrôlée | oui |
| N13 : cellule hors de l'étage III admise | oui |

Les huit mutations sont prises. Le témoin non muté passe : 27 essais sur les sections v9-v8n et v9-v8o.

Programme : `/tmp/claude-0/-home-user-controle-ia-travail/cf01708e-9b7d-5868-b0e7-26f697d45137/scratchpad/mutations_v8o.py`.

## Points ouverts

- Une porte fermée sur une cellule de G reste sans issue, puisque `--accepter-absence` est refusé avec l'ajout. Il faut
  alors un nouveau dossier, ou un mot de l'arbitre.
- Même sans l'option, `etat.md` porte la colonne « Ajoutée après coup », et chaque essai le champ `ajoutee_apres_coup`
  à faux, comme dans la v8n.
