# Contre-lecture du collisionneur v9, version 4

Écrite le 20 novembre 2026 par un contre-lecteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5, selon son rapport). Pièce de classe B (instrument).

Ce que je n'ai pas fait : aucun appel à un fournisseur, pas même un comptage ; aucune valeur de clé lue ; aucune dépense ; aucun commit ; aucun fichier du dépôt modifié hors cette pièce et son sceau. Seules des pages publiques de documentation de Google ont été lues sur le réseau (section 2).

## Verdict

**Conforme après corrections.**

Le script `collisionneur_v9_v4.py` fait ce que le directeur demande et ce que son rapport dit. **Je ne demande aucun changement de son texte.** Les essais tiennent.

Les corrections portent sur le rapport, par erratum (C1), et sur ce qui doit précéder tout appel (C2). Une réserve de fond, que le développeur n'a pas écrite, est à porter à la mère avant le premier envoi : la réserve 1.

Pièces relues, empreintes recalculées et égales aux compagnons :

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v4.py` | `46f1d917a2d8634e78680b14415c97344db5bbc498be67ec449527aa610735f1` |
| `test_collisionneur_v9_v4.py` | `d732a1ab71c307ce3a79d15b2428e709a3035eb5753635bc35f2368f260bbbd2` |
| `rapport-developpeur-collisionneur-v9-v4.md` | `60ec797a014a728919a4177dd265638343a94181f6fd4568dba6cf1f6bc565cf` |
| `collisionneur_v9_v3.py`, inchangé | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |

Les vingt compagnons `.sha256` du dossier sont justes, ceux de la contre-lecture et de la vérification de la v3 compris.

## 1. Le différentiel entier : rien d'autre que la table et la version

Différentiel complet entre la v3 et la v4, lu ligne à ligne. Il contient, et seulement :

- un paragraphe de commentaire d'en-tête (lignes 35 à 40) ;
- le nom du script dans l'aide d'usage, sept lignes ;
- `VERSION = "collisionneur-v9-v4"` ;
- une phrase ajoutée au commentaire des délais ;
- un bloc de commentaire de source et deux constantes, `PLAFOND_SORTIE_GEMINI_V4 = 65536` et `PROVISION_GEMINI_V4 = 49152` ;
- les deux lignes de la table : Argon passe de (18 000, 32 000, 8 192) à (65 536, 65 536, 49 152) ; Carbon de (65 536, 65 536, 32 768) à (65 536, 65 536, 49 152).

Aucune formule, aucune garde, aucun délai, aucun prix, aucune autre espèce ne change. La demande est tenue, sans plus.

## 2. Le choix de 49 152 contre la documentation de Google

J'ai relu trois des pages citées, le 20 novembre 2026, par l'outil de lecture du web.

| page | ce que j'y lis | accord avec le rapport |
|---|---|---|
| `aistudio.google.com/docs/thinking` (renvoi 301 depuis `ai.google.dev/gemini-api/docs/thinking`, constaté) | Aucune mention de `thinkingBudget`. La réflexion se règle par niveaux ; Carbon et Argon sont à « medium » par défaut. Le plafond de sortie fixe « the maximum number of tokens a response can generate, including thought tokens » et « acts as a hard cutoff enforced by the infrastructure ». | oui |
| `aistudio.google.com/docs/models/gemini-4-carbon` | « Max output 65,536 (default synchronous) / up to 1,048,576 (with long decode) » ; réflexion « Supported (low, medium, high) » ; mise à jour « November 2026 ». | oui |
| `docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking` (Vertex AI, autre service) | Bornes pour Gemini 2.5 seulement : Pro 128 à 32 768, Flash 1 à 24 576. « The thinking budget is a soft limit. » « The thinking_budget parameter is deprecated for Gemini 3 and later models. » « Setting thinking_budget on Gemini 4 models returns a 400: INVALID_ARGUMENT error ». | oui |

Ce que j'en tire :

- Le rapport cite juste. Aucun maximum du budget de réflexion n'est documenté pour Argon ni pour Carbon.
- **49 152 n'est donc pas une valeur documentée.** C'est une valeur calculée sous la seule borne documentée, le plafond de sortie de 65 536 jetons, pensées comprises. Le calcul (65 536 − 16 384) est juste.
- Le budget lui-même est un réglage que Google ne documente pas pour ces deux modèles. L'interface du script l'a accepté au run à 8 192 et à 32 768 ; à 49 152, personne ne l'a essayé.
- Même limite que le développeur : l'outil rend des extraits choisis par un petit modèle, pas la page. Rien n'est versé ni empreinté. Ces citations ne sont pas opposables au sens de R7.

**Si Google refuse le budget.** Lu dans le code et éprouvé :

- Une erreur HTTP 400 est classée « échec avant traitement » (`envoyer`, lignes 702 à 711). `appeler_gemini` rend une réponse en échec. `juger` rend le statut `ECHEC` et un coût de 0. La cellule s'arrête au code 5. La boucle des deux passes est quittée par l'arrêt : aucune relance, aucun autre budget, aucun autre modèle.
- L'essai `test_v4_artefact_budget_refuse_par_google_echec_sans_renvoi` le tient, pour Argon et pour Carbon. Mes retraits 2 et 5 (section 4) le font échouer.
- **Un cas voisin n'est pas « sans coût » au registre.** Si le refus arrivait dans le flux, après un code HTTP 200, il serait classé « envoi interrompu » : compté au pire cas (6,03 USD pour Argon), arrêt au code 5, aucun repli. Rien ne serait dépensé pour de vrai, mais la ligne serait chargée de ce montant. C'est prudent et déjà le cas dans la v3. Je ne demande pas de changement.

## 3. Le pire cas par cellule, refait par mon programme

Mon programme charge la v3 et la v4 et lit **ma copie** du run, faite après sa fin. Prix de la table : Argon 10 et 50 USD par million de jetons, Carbon 4 et 20.

| cellule | garde d'entrée | v3 | v4 | v4 avec relance | borne documentée | surestimation |
|---|---|---|---|---|---|---|
| Argon, critique du tour 2 | 29 800 | 1,6076 | 6,0324 | 12,0648 | 3,5748 | 2,4576 |
| Argon, réponse du tour 3 | 28 152 | 1,5911 | 6,0159 | 12,0318 | 3,5583 | 2,4576 |
| Argon, garde projetée | 70 004 | 2,0096 | 6,4344 | 12,8689 | 3,9768 | 2,4576 |
| Carbon, critique du tour 2 | 27 426 | 2,0758 | 2,4035 | 4,8069 | 1,4204 | 0,9830 |
| Carbon, réponse du tour 3 (relevée) | 42 420 | 2,1358 | 2,4634 | 4,9269 | 1,4804 | 0,9830 |
| Carbon, garde projetée | 70 004 | 2,2461 | 2,5738 | 5,1476 | 1,5907 | 0,9830 |

Tous les chiffres du rapport que je peux refaire sont justes : 6,0324 ; 2,4035 ; 12,0648 ; 4,8069 ; 6,4344 ; 2,5738 ; 3,5748 ; 1,4204 ; le facteur 3,75 ; les surestimations de 2,46 et 0,98 USD.

**L'état de la ligne dans le rapport est périmé.** Le run a fini à 14:52:01Z, après la copie du développeur (14:50:22Z). Sur ma copie, par les fonctions du script :

- dépensé sur la ligne : 10,3510 USD ; dépense du run : 14,4471 USD ;
- **reste de la ligne : 15,5490 USD**, et non 14,0977 ;
- aucune cellule n'est en vol ;
- la réponse de Carbon au tour 3 a été comptée à une garde de 42 420 jetons (et non 70 004), a coûté 0,7948 USD, avec 22 944 jetons de réflexion et 8 400 visibles, fin STOP.

Les conclusions du rapport tiennent avec le reste juste : une cellule Argon avec sa relance tient (12,06 USD) ; les deux cellules avec leurs deux relances ne tiennent pas (16,87 USD contre 15,55). La garde de ligne refuserait alors la seconde relance avant l'envoi.

### La surestimation doit-elle être corrigée ? Non, pas dans la v4.

Raisons :

1. **Elle sort de la demande.** Le directeur demande plus de provision. Corriger la formule changerait une garde de dépense, qui demande son cas sain et son artefact (R5) et sa propre contre-lecture.
2. **La borne qui la justifierait n'est pas établie pour ces modèles.** La phrase « pensées comprises » vient d'une page qui ne connaît pas le budget ; le budget est un réglage non documenté pour Gemini 4, et une limite souple. Au run, aucune sortie de Gemini n'a été coupée au plafond : la coupure ferme n'a jamais été vue. Le plus haut total relevé est 50 251 jetons, sous 65 536, ce qui ne prouve rien.
3. **L'excès ne coûte pas d'argent.** Il retient de la place sur la ligne, cellule par cellule et non en cumul : la garde compare la dépense faite plus le pire cas du **prochain** envoi. Il ne bloque un envoi que si le reste tombe sous 6,03 USD (Argon) ou 2,40 USD (Carbon).
4. **Mon retrait 3 le montre** : retirer la provision de la formule fait échouer quatre essais. La formule est tenue par les essais ; la changer est un chantier, pas une retouche.

Ce que l'excès demande en revanche : tout devis présenté à Lazar doit donner les deux chiffres, le pire cas compté et la borne documentée (C2).

Pour une version suivante, la correction ne devient défendable qu'après une preuve : une sortie de Gemini coupée (`MAX_TOKENS`) dont la réflexion plus la réponse visible égalent le plafond envoyé.

## 4. Les essais

Suite v4 rejouée par `PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider docs/notes/collisionneur-v9/test_collisionneur_v9_v4.py`, sans la variable `COPIE_RUN_DOPAMINE` : **166 passés, 1 sauté.** L'essai sauté est celui qui lit le run. Avec la variable posée sur ma copie : **167 passés**, copie inchangée à l'octet avant et après.

Aucun essai de la v4 ne nomme le run réel. Le réseau est fermé par doublure (toute connexion lève une erreur).

Cinq retraits de mon choix, chacun sur une copie dans mon bloc-notes, aucun n'étant ceux du développeur :

| retrait | essais en échec |
|---|---|
| 1. garde de réflexion relâchée (seuil au double de la provision) | 3 |
| 2. repli silencieux : après un refus de Google, renvoi sans budget de réflexion | 4 |
| 3. pire cas compté sans la provision | 4 |
| 4. relance d'Argon portée à 131 072 jetons | 2 |
| 5. erreur 400 classée « envoi interrompu » (comptée au pire) | 4 |

Chaque retrait est pris, et par au moins un essai neuf de la v4. Je ne demande aucun essai de plus.

## 5. Le run réel n'est pas touché

- La v4 ne contient aucun chemin vers `runs/collisionneur-dopamine-v1-20261120-122457/`. Seuls des commentaires nomment « collisionneur-dopamine-v1 ».
- Je ne l'ai lu qu'en copie : une copie entière, faite une fois, dans mon bloc-notes ; aucun fichier « consigne-privee » ni « conception-ii-b » n'y figure.
- Liste des 107 fichiers du run, avec tailles et dates de modification, relevée avant et après mon travail : identique. Dernière écriture : `etat.md`, 14:52:01Z, par le run lui-même.
- Aucun processus du collisionneur ne tourne.
- Effet à connaître, sans gravité : sur une copie du run, le devis de reprise de la v4 compte la critique de Carbon au tour 2 comme « à faire » (2,4840 USD au pire, 4,9680 avec relance). L'arbitre a accepté son absence ; la v4 ne la relancerait pas sans décision.

## Corrections

### C1. Rapport : état de la ligne périmé (par erratum, le rapport scellé n'est pas réécrit)

Fichier neuf, `rapport-developpeur-collisionneur-v9-v4-erratum-1.md`, même dossier. Texte :

```
# Erratum 1 du rapport du développeur, collisionneur v9, version 4

Le rapport (60ec797a…) a été écrit sur une copie du journal faite à 14:50:22Z. Le run a fini à 14:52:01Z. Cet erratum prime sur la section 4, « État de la ligne dans la copie » et « Une cellule est en vol », et complète la section 3.

- Aucune cellule n'est en vol. La réponse de Carbon au tour 3 est écrite : garde d'entrée de 42 420 jetons (et non 70 004 projetés), pire cas compté 2,1358 USD sous la v3, coût réel 0,7948 USD, 22 944 jetons de réflexion, 8 400 visibles, fin STOP.
- Dépensé sur la ligne : 10,3510 USD ; dépense du run : 14,4471 USD. Reste de la ligne : 15,5490 USD, et non 14,0977.
- Ce qui tient dans ce reste : une cellule Argon et une cellule Carbon sans relance (8,4359 USD) ; une cellule Argon avec sa relance (12,0648 USD). Les deux cellules avec leurs deux relances ne tiennent pas (16,8717 USD) : la garde de ligne refuserait la seconde relance avant l'envoi.
- Écart 1 : le run ne tourne plus. L'essai de la v3 qui lit le run en place le lit toujours en place : ne lancer `test_collisionneur_v9_v3.py` entier que sur décision de la mère.
- Section 2 : 49 152 n'est pas une valeur documentée par Google. C'est une valeur calculée sous le plafond de sortie documenté.
```

### C2. Avant tout appel avec la v4 (bloquante, sans changement du script)

Aucune commande de lancement de la v4 ne m'a été donnée : je n'en ai contre-lu aucune. Avant le premier envoi :

1. La commande est écrite, versée et contre-lue, comme la commande de reprise de la v3.
2. Le devis présenté à Lazar donne, pour chaque cellule de Gemini, les deux chiffres. Texte à reprendre : « Argon : 6,03 USD comptés au pire par envoi (12,06 avec relance), soit 3,75 fois la version 3 ; borne documentée 3,57 USD. Carbon : 2,40 USD comptés au pire par envoi (4,81 avec relance) ; borne documentée 1,42 USD. Ces montants valent pour une entrée d'environ 30 000 jetons. »
3. La réserve 1 est tranchée par la mère : envoyer le budget à 49 152, ou plus bas.

### Non exigé

Le commentaire des essais v4 (lignes 872 et 873) dit « le run réel tourne » : périmé, sans effet. À corriger à la prochaine version des essais, pas avant.

## Réserves

1. **Le budget envoyé à Google est aussi le seuil de la garde, alors que le budget est une limite souple.** C'est la réserve principale ; le rapport ne la dit pas.
   - Au tour 2, Carbon a dépassé son budget de 22 % (39 953 jetons pour 32 768 envoyés).
   - Le rapport lit 49 152 comme « 1,23 fois la plus haute réflexion relevée ». Cela suppose que la réflexion ne monte pas quand le budget monte. Rien ne l'établit.
   - Si Carbon dépasse le budget neuf dans la même proportion, il réfléchit 59 930 jetons : la garde arrête la cellule (code 6), après paiement, et il ne reste que 5 606 jetons à la réponse visible sous le plafond, moins que les 8 400 à 11 770 relevés.
   - Sur les deux autres cellules de Carbon, la réflexion est restée à 22 712 et 22 944 jetons sous un budget de 32 768 : elle semble dépendre de la tâche plus que du budget. Le risque est réel sans être le cas probable.
   - Le remède serait de séparer le budget envoyé du seuil de la garde (par exemple 40 960 envoyés, 49 152 gardés). C'est un changement de code et de conception : il revient à la mère et au concepteur, pas à cette contre-lecture.
2. **La provision neuve peut ne rien changer pour Argon.** Il n'a rendu aucune pensée sur trois cellules. Seul son pire cas compté monte, de 1,61 à 6,03 USD. Le développeur le dit (écart 5) ; je confirme sur ma copie.
3. **Le délai d'Argon s'appuie sur la borne documentée, le coût sur la borne prudente.** À 25 jetons par seconde, 3 600 s couvrent 65 536 jetons, pas 114 688 (4 588 s). Au débit relevé, de 70 à 87 jetons par seconde, 114 688 jetons prennent au plus 1 640 s : le délai tient. Un délai dépassé serait compté au pire, avec arrêt.
4. **Une relance de Gemini part au même plafond que le premier envoi.** Une sortie coupée a des chances de l'être de nouveau, et la relance est comptée 6,03 USD au pire pour Argon. Le développeur le dit (écart 6).
5. **Le budget de 49 152 n'a jamais été envoyé à Google**, et Vertex annonce une erreur 400 pour tout budget sur Gemini 4. Le premier envoi est un essai du réglage. S'il est refusé : arrêt au code 5, coût 0, décision à la mère.
6. **Sources non opposables** (R7) : pages lues par extraits, ni versées ni empreintées.

## Limites

Aucun appel réel. Le comportement de Google à 49 152 n'est connu que par la documentation. Mes programmes (`pire_cas.py`, `retraits.py`) et ma copie du run sont dans mon bloc-notes, qui n'est pas durable. Ce bloc-notes est partagé avec d'autres agents de la session : ma copie s'est logée dans un dossier `copie-run` qui y existait déjà ; je n'y ai rien supprimé.
