# Vérification des corrections : erratum 1 v2 et lignes descriptives v2 de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Vérificateur** : le contre-lecteur des v1, Claude Opus 5.5 (rapport `docs/notes/entretien-g0-priorites-v1/contre-lecture-erratum-et-lignes-descriptives-bbis-v1.md`, `e2ef776856c084b470e670d92665c9997249493cb1683c4df35e9c09477d1bb6`). Il n'a écrit aucune des pièces vérifiées.
- **Date (UTC)** : 2026-11-19, vers 11:40Z.
- **Méthode** : `diff` des v1 contre les v2 ; programme qui compare les suites de nombres à trois ou quatre décimales des v1 et des v2 ; lecture des § 1 et § 6 de l'audit de symétrie pour la phrase L6.

## Conclusions

| pièce | empreinte (égale au compagnon) | conclusion |
|---|---|---|
| `docs/verdicts/verdict-T0.7-etape-B-bis-v1-erratum-1-v2.md` | `1f3da53c4c4d6a17bae2c7a047746d1de301e454064ab77582b91d69c2fdc7c4` | **bon tel quel** |
| `docs/notes/entretien-g0-priorites-v1/lignes-descriptives-bbis-pour-dossier-v2.md` | `44436eec1dda42f488a590a41eeffaa54d62168736540adfe6fd365ec2edec69` | **bon tel quel** |

Les v1 sont intactes (`d1b94f11…`, `47df64a9…`, recalculées).

## 1. Erratum 1, v2

- **Différence avec la v1** : le titre (« v1 » → « v2 »), un paragraphe « Ce qui change depuis la v1 » ajouté, la ligne de date, et la seule phrase « Après » du § 1. Rien d'autre : le tableau du § 2, ses champs, et le § 3 sont identiques.
- **E1 portée comme écrite** :
  - avant : « à la dose 0,5 seulement, elle bat les trois lecteurs du texte et atteint la séparation à texte égal, sans aller au bout »
  - après : « à la dose 0,5 seulement, elle bat les trois lecteurs du texte ; à cette dose, elle sépare aussi à texte égal, sans aller au bout »
- **Chiffres** : les 42 nombres de la v1 se retrouvent, dans le même ordre, dans la v2. Aucun nombre n'est ajouté ni retiré.
- Le paragraphe ajouté décrit fidèlement la correction et cite le rapport de contre-lecture par son empreinte exacte.

## 2. Lignes descriptives, v2

- **Différence avec la v1** : le titre, un paragraphe « Ce qui change depuis la v1 » ajouté (L1 à L6, chacune avec sa raison), la ligne de date, les corrections L1 à L5 et la phrase de la section 8. Rien d'autre ne change.
- **L1 à L5** : portées mot pour mot telles que mon § 4.4 les écrit (titre de colonne « deux plis réunis » et garde de la section 1 ; phrase en clair de la section 5 ; citation de BB-P12 complétée ; titre, phrase et règle de la section 7.4 ; section 7.4 bis ajoutée).
- **Chiffres** : les 197 nombres de la v1 se retrouvent, dans le même ordre, dans la v2. Les cinq nombres ajoutés sont ceux de L1 et L2 (0,687 ; 0,4704 ; 0,6231 ; 0,8067 ; 0,8279), contrôlés dans ma contre-lecture : contre le texte pour 0,687 (BB-P10), contre le fichier de lecture pour les quatre autres.
- **Section 8** :
  - avant : « Elle n'a pas été contre-lue (pièce de travail, classe C) ; l'audit de symétrie dû (demande (i) du même accord) n'est pas son objet. »
  - après : « Sa v1 a été contre-lue par un autre modèle (Claude Opus 5.5 ; rapport cité en tête) ; les corrections de cette v2 restent à vérifier par le même contre-lecteur. L'audit de symétrie dû (demande (i) du même accord) n'est pas son objet ; rendu depuis (`docs/notes/audit-symetrie-bbis-v1/audit-symetrie-bbis-v1.md`, `eb42aefb…`, conclusion « transmissible avec réserve »), sa réserve accompagne au dossier les chiffres de cette note : […] (§ 6 de l'audit, réserves 1 et 3). »
  - La réécriture de la première phrase est juste, puisque la phrase de la v1 était devenue fausse.
- **L6 contre l'audit** (`eb42aefbe4d404347ab64e879e591f3ef831971861cd02d03f8317aa4a7bee47`, égale au compagnon) :
  - La conclusion « transmissible avec réserve » est celle du § 1 de l'audit.
  - « 8 épisodes sur 64 par cas, au modèle nu et à la dose 1 seulement » et « le chemin neuf aux doses 0,25, 0,5 et 0,75 n'étant comparé à aucune série d'origine » reprennent la réserve 1 du § 6.
  - « elle ne peut pas être rejouée après coup, les activations de la course n'ayant pas été gardées » reprend presque mot pour mot la conclusion du § 1 de l'audit (« elle ne peut pas être rejouée après coup, parce que les activations n'ont pas été gardées »), que précise sa réserve 3.
  - La phrase ne dit rien de plus que l'audit. L6 omet les réserves 2, 4, 5 et 6 de l'audit ; c'est un choix déclaré (« réserves 1 et 3 »), non une erreur.

## 3. Ce que cette note ne fait pas

Elle ne lit aucun score. Elle ne modifie aucune pièce et ne commet rien.
