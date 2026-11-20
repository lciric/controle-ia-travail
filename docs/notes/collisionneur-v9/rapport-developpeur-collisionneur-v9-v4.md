# Rapport du développeur : collisionneur v9, version 4

Écrit le 20 novembre 2026 par un développeur neuf (Claude Opus 5.5). C'est une pièce de classe B : avant tout appel, un autre modèle doit contre-lire le code, puis le même contre-lecteur vérifie les corrections.

La demande vient du directeur : « donne plus de provision de réflexion à Carbon et Argon ».

Ce que je n'ai pas fait :
- aucun appel à un fournisseur, pas même un comptage ;
- aucune clé lue ;
- aucune dépense ;
- aucun commit ;
- aucune commande sur le run en cours.

Seules des pages publiques de documentation de Google ont été lues sur le réseau (section 2).

## Pièces

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v4.py` | `46f1d917a2d8634e78680b14415c97344db5bbc498be67ec449527aa610735f1` |
| `test_collisionneur_v9_v4.py` | `d732a1ab71c307ce3a79d15b2428e709a3035eb5753635bc35f2368f260bbbd2` |

Les pièces v3 sont intactes ; leurs sceaux ont été vérifiés avant la copie :
- le script, `850df311…` ;
- les essais, `8c38dc2f…` ;
- le complément d'essais, `58ddaa24…`.

## 1. Ce qui change

Seule la table des espèces change. Aucune formule, aucune garde, aucun délai.

| espèce | plafond de sortie | plafond de relance | provision de réflexion |
|---|---|---|---|
| Argon (`gemini-4-argon`), v3 | 18 000 | 32 000 | 8 192 |
| **Argon, v4** | **65 536** | **65 536** | **49 152** |
| Carbon (`gemini-4-carbon`), v3 | 65 536 | 65 536 | 32 768 |
| **Carbon, v4** | 65 536, inchangé | 65 536, inchangé | **49 152** |

Ce qui accompagne ce changement :
- deux constantes nommées, `PLAFOND_SORTIE_GEMINI_V4 = 65536` et `PROVISION_GEMINI_V4 = 49152` ;
- les commentaires de source dans la table ;
- `VERSION = "collisionneur-v9-v4"` ;
- le nom du script dans l'aide d'usage.

Le diff entre la v3 et la v4 ne touche que ces lignes.

Pourquoi le plafond d'Argon monte : chez Google, la réflexion compte dans la sortie. Avec une provision de 49 152, un plafond de 18 000 couperait la réponse.

Pourquoi celui de Carbon ne bouge pas : il est déjà au plafond synchrone documenté.

## 2. Borne documentée (lue le 20 novembre 2026)

| page | ce qu'elle dit |
|---|---|
| https://aistudio.google.com/docs/thinking (renvoi permanent depuis ai.google.dev/gemini-api/docs/thinking) | Argon et Carbon réfléchissent par **niveaux** : low, medium, high, et medium par défaut. **Aucun `thinkingBudget` n'y est documenté pour eux.** Sur `max_output_tokens` : « the maximum number of tokens a response can generate, including thought tokens » ; « a hard cutoff enforced by the infrastructure ». |
| https://aistudio.google.com/docs/models/gemini-4-argon (mis à jour en octobre 2026) et https://aistudio.google.com/docs/models/gemini-4-carbon (mis à jour en novembre 2026) | « Max output 65,536 (default synchronous) / up to 1,048,576 (with long decode) ». Réflexion « Supported (low, medium, high) ». Aucune borne de budget. |
| https://aistudio.google.com/api-reference/generate-content | `thinkingBudget` : « The number of thoughts tokens that the model should generate ». Aucune borne écrite. |
| https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking (Vertex AI, **un autre service que celui du script**) | Bornes du budget pour Gemini 2.5 seulement : Pro de 128 à 32 768, Flash de 1 à 24 576. Le budget est une « soft limit ». Il est « deprecated for Gemini 3 and later models ». « Setting thinking_budget on Gemini 4 models returns a 400: INVALID_ARGUMENT error ». |

**Ce que j'en conclus.**
- Google ne documente **aucun maximum du budget de réflexion pour Gemini 4**.
- Le plus grand budget documenté dans la famille Gemini est 32 768, mais il vaut pour Gemini 2.5 Pro, qui n'est plus la famille en cours.
- La seule borne documentée qui vaut pour Argon et Carbon est le **plafond de sortie synchrone, 65 536 jetons, pensées comprises**, appliqué comme une coupure ferme.

**Ma borne retenue est donc 65 536.** La provision doit laisser de la place à la réponse visible sous ce plafond.

Les copies des pages ne sont pas versées dans le dépôt : je n'ai que leurs citations, relevées par l'outil de lecture du web. Si la mère veut une source opposable au sens de R7, il faut verser et empreinter ces pages.

## 3. Réflexion relevée au run, et choix des provisions

Ces chiffres sont lus dans une **copie** du journal, faite à 14:50:22Z dans mon bloc-notes.

| cellule | espèce | provision | réflexion | réponse visible | fin |
|---|---|---|---|---|---|
| E3-T1-conception-C | Argon | 8 192 | 0 | 7 558 | STOP |
| E3-T2-critique-croisee-C | Argon | 8 192 | 0 | 11 770 | STOP |
| E3-T3-reponse-C | Argon | 8 192 | 0 | 7 186 | STOP |
| E3-T1-conception-E | Carbon | 32 768 | 22 712 | 9 904 | STOP |
| E3-T2-critique-croisee-E | Carbon | 32 768 | **39 953** | 10 298 | STOP, puis arrêt par `REFLEXION_HORS_PROVISION` |

Pour la critique de Carbon :
- 39 953 + 10 298 = 50 251 jetons de sortie, ce qui correspond au nombre annoncé ;
- la réflexion a dépassé le budget envoyé de 22 % : le budget est bien une limite souple.

Pour Argon :
- il ne rend **aucune pensée** : aucune partie `thought` dans les réponses ;
- son total vaut exactement l'entrée plus la sortie visible.

Le budget envoyé ne semble donc pas régler la réflexion d'Argon. Lui donner plus de provision ne garantit pas qu'il réfléchira davantage.

**Choix : provision = 65 536 − 16 384 = 49 152 pour les deux espèces.**
- **Place laissée à la réponse visible : 16 384 jetons.** C'est 1,39 fois la plus longue réponse visible relevée (11 770 jetons, Argon, critique du tour 2).
- **Marge sur la réflexion : 49 152 vaut 1,23 fois la plus haute réflexion relevée** (39 953 jetons). Ce rapport est du même ordre que le dépassement observé du budget (1,22).
- **La provision reste sous la borne documentée** : 49 152 + 16 384 = 65 536.
- Je n'ai pas pris plus haut : chaque millier de jetons de provision en plus retire la même place à la réponse visible, sous un plafond qui ne peut pas monter en mode synchrone.

## 4. Pire cas, par programme

Les deux scripts, dans mon bloc-notes, chargent la v3 et la v4 et lisent la copie du run :
- `outils/pire_cas_v4.py` ;
- `outils/pire_cas_v4_complement.py`.

Leurs sorties sont `pire-cas-v4-sortie.json` et `pire-cas-v4-complement-sortie.json`.

Prix comptés : Argon à 10 et 50 USD par million de jetons (borne haute de la table), Carbon à 4 et 20. La formule n'a pas changé : garde d'entrée au prix d'entrée, plus plafond de sortie et provision au prix de sortie.

**État de la ligne dans la copie.**
- Ligne : 25,90 USD, ouverte à 4,10 USD de dépense.
- Dépensé sur la ligne : **9,5562 USD** ; dépense du run : 13,65 USD.
- **Reste de la ligne : 16,3438 USD.**
- L'`etat.md` du run, en copie, date de 14:33Z et dit encore 6,03 USD. Il est périmé : j'ai pris le journal.
- Le registre `registres/etat.md`, en copie, ne mentionne pas cette ligne.

**Une cellule est en vol.** La réponse de Carbon au tour 3 est partie à 14:44:19Z sous la v3. Son pire cas projeté sous la v3 est 2,2461 USD. **Reste après elle, au pire : 14,0977 USD.**

**Pire cas d'une cellule, en USD.**

| cellule | v3 | v4 | v4 avec relance |
|---|---|---|---|
| Argon, à sa plus grosse garde d'entrée relevée (29 800 jetons) | 1,6076 | **6,0324** | 12,0648 |
| Carbon, à sa plus grosse garde relevée (27 426 jetons) | 2,0758 | **2,4035** | 4,8069 |
| Argon, à la garde projetée du tour III.3 (70 004 jetons) | n/a | 6,4344 | 12,8689 |
| Carbon, à la garde projetée du tour III.3 (70 004 jetons) | 2,2461 | 2,5738 | 5,1476 |

Ce qui tient dans le reste de 14,0977 USD :
- **Une cellule Argon et une cellule Carbon, sans relance, tiennent** : 8,4359 USD aux gardes relevées, 9,0082 USD aux gardes projetées.
- **Une cellule Argon avec sa relance tient seule** : 12,0648 USD, ou 12,8689 USD.
- **Les deux cellules avec leurs relances ne tiennent pas** : 16,8717 USD, ou 18,0164 USD, au-delà de 14,0977. Dans ce cas, la garde de ligne refuserait la seconde relance avant l'envoi (code 4), comme dans la v3. Rien ne serait dépensé au-delà de la ligne.

**Le pire cas d'Argon est multiplié par 3,75.** Il passe de 1,61 à 6,03 USD par cellule.

La formule compte la provision **en plus** du plafond de sortie. Or la documentation dit que le plafond contient déjà les pensées. La borne documentée d'une cellule Argon serait donc de 3,5748 USD, et celle d'une cellule Carbon de 1,4204 USD. Je n'ai pas changé la formule, qui reste prudente ; voir l'écart 3.

## 5. Essais

Lancés par `PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v4.py` : **166 passés, 1 sauté.**

L'essai sauté lit une copie du run, désignée par la variable `COPIE_RUN_DOPAMINE`. Lancé avec cette variable sur ma copie, il passe aussi.

Il n'y a aucun appel réseau : les doublures de la v3 sont reprises telles quelles, et toute connexion lève une erreur.

**Essais v3 adaptés aux valeurs neuves.** Sept essais ont changé :
- trois de la garde de réflexion ;
- un de l'entrée gardée ;
- deux de l'interruption comptée au plus grand du pire cas et de l'usage lu (120 000 pensées au lieu de 60 000) ;
- l'essai qui lisait le run réel en place. Il est **remplacé** par un essai qui ne lit qu'une copie, désignée par `COPIE_RUN_DOPAMINE`.

**Complément 1 de la v3**, versé en fin de fichier sans changement de fond : 6 essais.

**Essais neufs de la v4** (section en fin de fichier) :
- **la table** : seules la provision et les plafonds d'Argon et de Carbon diffèrent de la v3 ; les autres espèces et les constantes de garde sont identiques ; la provision plus 16 384 égale le plafond, qui ne dépasse pas 65 536 ;
- **cas sain** : réflexion de 49 152 et réponse de 16 384. Le statut est OK, le budget envoyé vaut 49 152, le plafond envoyé 65 536, et le coût réel est compté. L'essai est fait pour Argon et pour Carbon ;
- **artefact** : une réflexion de 49 153 donne `REFLEXION_HORS_PROVISION` (code 6), aucune cellule n'est écrite, un seul envoi part. Même essai pour Argon et pour Carbon ;
- **usage réel du tour 2 de Carbon** (27 122 en entrée, 39 953 de réflexion, 10 298 visibles) : la v3 l'arrête, c'est l'artefact ; la v4 le garde, c'est le cas sain ;
- **artefact du budget refusé par Google** (erreur 400) : échec, coût 0, un seul envoi, aucune relance ni aucun repli ; la clé n'apparaît pas au journal ;
- **pire cas d'Argon compté avant l'envoi** : un plafond juste sous le pire cas empêche tout envoi ; un plafond juste au-dessus le laisse partir ;
- **relance d'Argon** après une coupure : elle part au même plafond (65 536) et au même budget (49 152).

**Mutations**, faites sur des copies dans le bloc-notes :

| mutation | essais en échec |
|---|---|
| provision d'Argon ramenée à 8 192 | 10 |
| provision de Carbon ramenée à 32 768 | 10 |
| plafonds d'Argon ramenés à 18 000 et 32 000 | 8 |
| budget envoyé figé à 32 768 au lieu de la provision | 10 |

**Non-régression.** La suite v3 et son complément, rejoués sur la v3 inchangée, donnent 156 passés. J'en ai retiré l'essai v3 qui lit le run réel ; voir l'écart 1.

## 6. Écarts et réserves

1. **J'ai lu le run réel en place, une fois, sans copie.** Au premier lancement de la suite v4, l'essai v3 copié qui lit le run réel était encore actif : il appelle `devis_reprise` sur le run en cours.
   - Son graphe d'appels, relu par programme, ne contient aucune écriture.
   - Les dernières écritures du dossier datent de 14:44:19Z et viennent du run lui-même.
   - Rien n'a été lancé sur le run.
   - Cet essai ne lit plus qu'une copie dans la v4. **Dans la v3, il lit toujours le run réel** : il ne faut pas lancer `test_collisionneur_v9_v3.py` entier tant que le run tourne.
2. **Le budget de 49 152 n'a jamais été essayé chez Google.** Seuls 8 192 et 32 768 l'ont été, et l'interface Gemini les a acceptés. Vertex dit qu'un budget sur Gemini 4 rend une erreur 400.
   - Si l'interface Gemini refuse 49 152, l'envoi est un échec avant traitement : coût 0, arrêt au code 5, aucun renvoi, aucun repli. C'est l'artefact de la section 5.
   - La décision reviendrait alors à la mère : revenir à 32 768, ou passer au niveau de réflexion documenté, ce qui serait un autre changement de code.
3. **La formule du pire cas n'a pas changé.** Elle compte « sortie + provision » alors que, selon la documentation, la sortie contient déjà la réflexion. Elle surestime d'environ 2,46 USD par cellule Argon et 0,98 USD par cellule Carbon, aux prix comptés.
   - La corriger irait au-delà de la demande. C'est à décider pour une version suivante.
   - Effet secondaire, dans `pire_tours_2_3` : quand la critique d'Argon n'est pas écrite, sa projection vaut le plafond de sortie × 4,5 caractères, soit désormais 65 536 × 4,5. Les projections de reprise sont donc plus lourdes quand cette critique manque. Sur ce run, elle est valide, et rien ne change.
4. **Les délais ne changent pas.** Pour Argon, 3 600 s couvrent 65 536 jetons à 25 jetons par seconde (2 621 s). Le débit relevé au run est de 73 à 87 jetons par seconde. Si l'on compte « sortie + provision », soit 114 688 jetons, il faudrait 4 588 s à 25 jetons par seconde. Carbon, à 5 400 s, tient même sur ce compte.
5. **Le budget envoyé ne semble pas régler la réflexion d'Argon**, puisqu'il n'en rend aucune. La provision neuve peut ne rien changer à sa réflexion. Seul son pire cas compté augmente.
6. **La relance de Gemini part au même plafond que le premier envoi** : 65 536 pour les deux, ce qui est déjà le cas de Carbon dans la v3. Une sortie coupée au plafond a donc des chances d'être coupée de nouveau à la relance.
7. **Les pages de Google ont été lues par l'outil de lecture du web**, qui rend des citations et non la page entière. Elles ne sont ni versées ni empreintées : voir la réserve sur R7, en section 2.
