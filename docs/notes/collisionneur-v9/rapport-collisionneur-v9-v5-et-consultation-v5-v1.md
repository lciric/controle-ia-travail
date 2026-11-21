# Rapport : collisionneur v9 v5 et consultation v5 (Neon, plafond large, clé d'OpenAI nommée)

Écrit le 21 novembre 2026 par un développeur neuf (Claude Opus 5.5). Demande : GO-2026-11-21-57, « ajoute Neon dans le collisionneur ». Pièce de classe B : un Fable contre-lit le code avant tout appel.

Ce que je n'ai pas fait :
- aucun appel de génération, aucun comptage de jetons ;
- aucune dépense ;
- aucune valeur de clé affichée ni écrite ;
- aucun commit ni aucune poussée ;
- rien lu ni écrit sous runs/, archives-reponses-modeles/ ou docs/notes/bras-attaque/ ;
- aucune suppression.

Ce qui est sorti sur le réseau :
- une seule requête à l'interface Gemini : la liste des modèles (GET v1beta/models), le 21 novembre 2026 à 13:49:04Z. La clé a été lue par son nom, GEMINI_API_KEY ;
- trois pages publiques de Google, à 13:49Z : les tarifs, la page de Neon, la page de la réflexion.

## 0. Deux écarts de nom à la demande, à trancher par la mère

1. **Le nom `collisionneur_v9_v4.py` est déjà pris.**
   - Il porte la version 4 du 20 novembre (`46f1d917…`) : provision de réflexion d'Argon et de Carbon montée à 49 152.
   - Fable l'a contre-lu « conforme après corrections » (R-4308).
   - R12 interdit d'écraser un fichier. Le script neuf s'appelle donc **`collisionneur_v9_v5.py`**.
   - Il part du v3 (`850df311…`), comme l'ordre le demande. Il ne reprend donc pas les provisions de la v4 : Carbon garde 32 768, Argon 8 192.
   - Si la mère veut les provisions de la v4, il faut porter deux lignes de la table et changer un essai, celui qui compare au v3. Ce n'est pas fait.
   - À mon avis, garder la base v3 tient mieux la règle du plafond large. Avec une provision de 32 768, Carbon garde 32 768 jetons de texte. Avec la v4, il n'en garde que 16 384.
2. **Le rapport s'appelle `rapport-collisionneur-v9-v5-et-consultation-v5-v1.md`**, et non « …-v9-v4-… ». Le nom demandé laisserait croire qu'il porte sur la v4 existante.

## 1. Neon : prix, identifiant, réglages

| quoi | valeur | source |
|---|---|---|
| prix, palier « Standard », payant | **3 USD par million en entrée, 15 en sortie**, pensées comprises | page publique https://ai.google.dev/gemini-api/docs/pricing, renvoyée vers https://aistudio.google.com/docs/pricing. Lue le **21 novembre 2026 à 13:49:18Z**. Versée : `docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html` (`40202cdd…`) |
| autres paliers, non demandés par les scripts | « Batch » et « Flex » : 1,50 et 7,50. « Priority » : 5,40 et 27 | même page |
| changement de prix daté | aucun n'est écrit pour Neon. Pour comparaison, Argon et Carbon passent de 2 et 10 à 4 et 20 au 1er décembre | même page |
| identifiant | `models/gemini-4-neon`, parmi 65 modèles listés. outputTokenLimit 65 536, inputTokenLimit 1 048 576, thinking vrai | liste des modèles de l'interface, lue à 13:49:04Z. Copie versée : `docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json` (`eeec19e8…`), clé absente du fichier, vérifié |
| plafond de sortie | « Max output 65,536 (default synchronous) / up to 1,048,576 (with long decode) » | page du modèle, versée : `docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html` (`2eadc192…`) |
| réflexion | niveaux low, medium, high, xhigh ; high par défaut. **Aucun budget de réflexion documenté** | page du modèle, et page de la réflexion (aistudio.google.com/docs/thinking, lue, non versée) |

J'ai trouvé le prix : le repli (le plus haut prix du catalogue pour la lignée Google, 10 et 50) n'a pas servi. Neon est compté au prix lu, et non à une borne haute comme Argon.

**Réglages de Neon dans le collisionneur.**
- Plafond de sortie : 65 536. Plafond de relance : 65 536.
- Provision : 32 768, comme Carbon. Il reste donc 32 768 jetons de texte au-delà de la réflexion.
- Délai : 5 400 s, comme Carbon.
- 2,5 caractères par jeton.
- Clé : GEMINI_API_KEY, lue par son nom.
- Ces réglages sont SUPPOSÉS : aucun envoi n'a été fait à Neon.

**Réglages de Neon dans la consultation.** Par défaut, 32 768 de réflexion et 32 768 de texte, soit 65 536 au total.

**Pire cas compté pour une cellule Neon du collisionneur**, même formule que le v3 (garde d'entrée au prix d'entrée, plus plafond et provision au prix de sortie) :

| garde d'entrée | pire cas | avec relance |
|---|---|---|
| 0 jeton | 1,4746 USD | 2,9491 USD |
| 29 800 jetons | 1,5640 USD | 3,1279 USD |
| 70 004 jetons | 1,6846 USD | 3,3691 USD |

Pour comparaison, Carbon à 29 800 jetons : 2,0853 USD, et 4,1706 USD avec relance.

## 2. Règle du plafond large (CLAUDE.md, GO-2026-11-21-47), appliquée à Carbon et à Neon

**Dans le collisionneur.** Une table neuve, `REGLE_TEXTE_MIN = {"carbon": 16000, "neon": 16000}`, porte la règle.
- **Réflexion bornée.** La provision doit être positive. Elle est envoyée comme budget à Google. La garde du v9 qui l'accompagne reste en place : une réflexion au-delà de la provision est arrêtée en `REFLEXION_HORS_PROVISION`, code 6.
- **Texte suffisant.** Le plafond moins la provision doit laisser au moins 16 000 jetons, pour le premier envoi comme pour la relance. C'est vérifié à deux moments :
  - à la composition : refus au code 1 ;
  - dans `executer_cellule`, avant le comptage et avant tout envoi : refus consigné au journal (`REGLE_TEXTE_MIN`), code 1. Rien n'est compté ni envoyé.
- **Arrêt en MAX_TOKENS sans texte.** Chez Carbon et Neon, c'est un défaut de réglage, pas une réponse.
  - Statut `MAX_TOKENS_SANS_TEXTE`, nouveau code 9.
  - Le coût réel est compté. Aucune cellule n'est écrite. **Il n'y a aucune relance au même réglage**, alors que le v3 relançait une sortie vide.
  - Ce statut ne vient qu'après les gardes de `juger`. Une réflexion au-delà de la provision reste donc au code 6.
- **Ce qui ne change pas.**
  - Argon n'est pas soumis à la règle et garde le comportement du v3. Un essai témoin le vérifie.
  - Un texte coupé (`TRONQUE`) chez Carbon ou Neon garde la relance du v3.
- **Les valeurs de Carbon tiennent déjà la règle** : 65 536 − 32 768 = 32 768.

**Dans la consultation.**
- Neon entre sous le plancher de 16 000 jetons de texte, comme Carbon et Argon dans le v4.
- Un « MAX_TOKENS » sans texte chez Carbon ou Neon reçoit le motif « défaut de réglage, pas une réponse ». Le code de sortie reste 3, comme dans le v4.

## 3. Option `--cle-openai NOM`

**Dans le collisionneur.**
- L'option existe pour les trois étages. Son défaut est OPENAI_API_KEY.
- Le nom est contrôlé par le même motif que `--cle-anthropic`.
- Il est porté par `MODELES[l]["nom_cle"]`, et lu pour l'envoi (`appeler_openai`) comme pour le comptage (`compter_openai`).
- Une variable absente est refusée par son nom, au code 1, avant toute écriture. La clé par défaut n'est jamais lue à sa place.
- Le nom de la clé n'entre pas dans `especes.json`. Un même run peut donc changer de clé entre deux commandes.
- Le nom n'est pas écrit au journal.

**Dans la consultation.**
- Même option, même contrôle.
- Un nom mal formé, par exemple une valeur collée par erreur, est refusé sans être répété.
- Le **nom** de la variable lue est écrit dans le JSON, au champ `variable_cle`.

## 4. Essais (R5), tous hors réseau

| suite | sur | résultat |
|---|---|---|
| essais v3 et complément 1, inchangés (copie dans le bloc-notes, essai du run neutralisé) | v3, référence | 156 passés, 1 sauté |
| mêmes essais, inchangés | **v5** | 155 passés, **1 en échec, voulu** (`test_identifiants_et_table_des_prix` : Neon en plus), 1 sauté |
| `test_collisionneur_v9_v5.py` (voir ci-dessous) | v5 | **186 passés, 1 sauté** |
| `essais_appel_modeles_externes_v4.py`, inchangé | consultation v4 | 10 passés |
| `essais_appel_modeles_externes_v5.py` (voir ci-dessous) | consultation v5 | **21 passés**, avec pytest et avec le lanceur du fichier |
| pour information : essais de la v4 du collisionneur | v5 | 154 passés, 12 en échec, 1 sauté |

**Ce que contient `test_collisionneur_v9_v5.py`.**
- La suite v3 et son complément, rejoués sur la v5, soit 156 essais. Il n'y a que trois écarts :
  - le chemin du script ;
  - l'essai qui lisait le run sous runs/ ne lit plus qu'une copie désignée par COPIE_RUN_DOPAMINE. Sans elle, l'essai est sauté, comme dans les essais de la v4 ;
  - l'essai des identifiants attend Neon et la page de prix.
- 30 essais neufs.

**Pourquoi les 12 essais de la v4 échouent sur la v5.** Ils fixent les valeurs de la v4 : provision 49 152, plafonds d'Argon 65 536, et l'essai des identifiants. C'est attendu, puisque la v5 part du v3 (section 0).

**Ce que contient `essais_appel_modeles_externes_v5.py`.** Les dix essais du v4, rejoués tels quels sur le v5, et 11 essais neufs.

**Essais neufs pour Neon et `--cle-openai`, avec leur cas sain et leur artefact.**
- **Cas sain.**
  - Collisionneur : adresse `gemini-4-neon`, budget 32 768, plafond 65 536, clé dans l'en-tête, comptage sur `gemini-4-neon:countTokens`, coût au prix 3 et 15. Le prix est contrôlé contre la page versée, l'identifiant contre la liste versée.
  - Consultation : même contrôle de l'envoi, champ `variable_cle`, coût.
- **Garde de dépense.**
  - Plafond juste sous le pire cas : aucun envoi. Juste au-dessus : l'envoi part.
  - La ligne de dépense, dans les deux sens.
  - Dans la consultation : un pire cas au-delà de 4 USD est refusé.
- **Budget de réflexion refusé par Google** (400) : échec, coût 0, un seul envoi, la clé n'est pas écrite.
- **Arrêt « MAX_TOKENS ».**
  - Sans texte, chez Neon et Carbon : code 9, un seul envoi, aucune cellule, coût réel compté. Dans la consultation : code 3, avec le motif « défaut de réglage ».
  - Témoin Argon : relance comme dans le v3.
  - Réflexion au-delà de la provision : code 6.
  - Texte partiel : relance comme dans le v3 dans le collisionneur ; texte écrit à part, en `.partiel.md`, dans la consultation.
- **Règle du plafond large.**
  - Cas sain, avec le bord : exactement 16 000 jetons de texte sont acceptés.
  - Refus à la composition, pour Carbon et Neon, sur le plafond et sur la relance.
  - Témoin Argon : pas de refus.
  - Réglage changé après la composition : refus avant tout comptage et tout envoi.
  - Plancher de Neon dans la consultation.
- **Clé d'OpenAI choisie par son nom.**
  - Cas sain : envoi et comptage portent la clé nommée, et la valeur n'apparaît dans aucun fichier ni aucune sortie.
  - Variable nommée absente : refus, sans repli sur OPENAI_API_KEY. Dans le collisionneur, essayé aux trois étages.
  - Nom mal formé : refusé sans être répété.
  - L'option est bien transmise par la ligne de commande. Dans la consultation, cet essai bloque le réseau et pose une clé par défaut factice.
  - Le nom de la clé n'entre pas dans le sceau de la composition.

**Mutations.** Elles ont été faites sur des copies, dans le bloc-notes, par `outils/mutations_v5.py`. Chacune fait échouer au moins un essai.

| mutation | essais en échec |
|---|---|
| collisionneur : code 9 retiré (relance d'une sortie vide) | 2 |
| collisionneur : règle retirée avant le comptage | 2 |
| collisionneur : règle retirée à la composition | 4 |
| collisionneur : plancher à 15 000 | 7 |
| collisionneur : Neon hors de la règle | 6 |
| collisionneur : envoi d'OpenAI sur OPENAI_API_KEY en dur | 2 |
| collisionneur : comptage d'OpenAI sur OPENAI_API_KEY en dur | 2 |
| collisionneur : nom de clé ignoré à la composition | 5 |
| collisionneur : `--cle-openai` non transmise | 4 |
| collisionneur : nom de clé non contrôlé | 1 |
| collisionneur : prix de Neon à 2 et 10 | 5 |
| collisionneur : provision de Neon à 49 152 | 6 |
| collisionneur : Neon avant Carbon dans l'ordre | 3 |
| collisionneur : identifiant de Neon faux | 9 |
| consultation : option ignorée à l'exécution | 3 |
| consultation : option non transmise par `main` | 1 |
| consultation : nom de clé non contrôlé | 1 |
| consultation : Neon hors du plancher de texte | 2 |
| consultation : Neon hors de la règle (motif) | 2 |
| consultation : prix de Neon à 2 et 10 | 3 |
| consultation : défaut de Neon à 32 768 + 16 000 | 3 |

**Relancer les essais :**

```
PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v5.py
PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/essais_appel_modeles_externes_v5.py
```

**Attention :** ne pas lancer `test_collisionneur_v9_v3.py` en place. Un de ses essais lit le run sous runs/, s'il existe.

## 5. Réserves

1. **Base v3 et non v4** (section 0). À trancher par la mère.
2. **Le budget de réflexion n'a jamais été envoyé à Neon.**
   - Google ne documente que des niveaux de réflexion pour Gemini 4.
   - La page de Vertex, lue le 20 novembre par la v4, dit qu'un budget sur Gemini 4 rend une erreur 400.
   - Dans ce cas : code 5, coût 0, aucun repli. C'est éprouvé.
   - Passer au niveau de réflexion serait un autre changement de code.
3. **La liste des modèles donne un outputTokenLimit de 32 768 pour Carbon et pour Argon.**
   - Le v3 envoie pourtant 65 536 à Carbon.
   - Au run du 20 novembre, Carbon a rendu 50 251 jetons de sortie (39 953 de réflexion et 10 298 visibles, rapport de la v4).
   - La limite listée ne semble donc pas appliquée, ou ne compte pas les pensées.
   - Rien n'est changé. Le défaut de Carbon dans la consultation (40 000) est dans le même cas.
4. **La relance d'un texte coupé chez Carbon et Neon** part au même plafond, 65 536. Elle a donc des chances d'être coupée de nouveau. Ce comportement du v3 est gardé, puisque l'ordre est de garder les gardes intactes ; c'était déjà la réserve 6 de la v4.
5. **Le budget est une limite souple** : Carbon l'a dépassé de 22 % au run.
   - Un tel dépassement est arrêté au code 6, après avoir été payé. C'est inchangé.
   - La règle des 16 000 jetons est tenue sur le réglage. Dans une cellule acceptée, la réflexion reste dans la provision, et le texte dispose d'au moins 32 768 jetons.
6. **Prix de Neon.**
   - Il est compté au prix lu, palier « Standard », et non à une borne haute.
   - Le palier « Priority » (5,40 et 27) n'est jamais demandé par les scripts.
7. **`streamGenerateContent` n'apparaît pour aucun modèle Gemini 4** dans la liste. Seuls y figurent generateContent, countTokens et batchGenerateContent. Carbon a pourtant été servi en flux au run.
8. **Le nom de la clé d'OpenAI n'est pas écrit au journal du collisionneur.** Il l'est dans le JSON de la consultation.

## 6. Pièces

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v5.py` | `697f01512ad24870ce1ee77671ac4ce9c249ed716bc3d598cc80d421c413d53d` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v5.py` | `624b522994f0f7c79d8c0ac8f70014fdf4b410f8163bcb5e6df59ce86ef4ddc9` |
| `docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json` | `eeec19e8040801300dce567f872525bfcf7df770971083c03199ee688ec12f96` |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v5.py` | `4c44b89ed9767aec007251b86abc5b27d97e180b379c78c8dbe781f8472ef3fd` |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/essais_appel_modeles_externes_v5.py` | `8a66f62fa72da25976c47c38404232251b8732cb40be8592af91b73c7bcb7838` |
| `docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html` | `40202cdd6fc4eb04984af6ba5426b234540a0b37d819ed0c1d9d34f1d38fd155` |
| `docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html` | `2eadc19280409f032e4a6cb5142ee834a03e8edf0aa5b3f45d978f6e09c368b1` |

Chacune a son compagnon `.sha256`.

Sources intactes, sceaux vérifiés avant la copie :
- `collisionneur_v9_v3.py`, `850df311…` ;
- `test_collisionneur_v9_v3.py`, `8c38dc2f…` ;
- le complément, `58ddaa24…` ;
- `appel_modeles_externes_v4.py`, `b31fecf2…` ;
- `essais_appel_modeles_externes_v4.py`, `f3181604…`.

Le v4 du collisionneur (`46f1d917…`) n'est pas touché.

Le dépôt exclut localement la plupart de ces fichiers neufs (`.git/info/exclude`, « à verser à leur remise »). La mère les verse.

## 7. Différentiels

### 7.1 Collisionneur : v9-v3 (`850df311…`) vers v9-v5 (`697f0151…`), différentiel unifié complet

```diff
--- collisionneur_v9_v3.py
+++ collisionneur_v9_v5.py
@@ -32,7 +32,19 @@
 #   (2) plafond de sortie de Fable relevé (calcul par `devis-reprise`) ; (3) ligne de dépense (--ligne-usd) ;
 #   (4) reprise d'un run commencé par un autre script, déclarée (--reprise) et reconnue par `verifier`.
 #   Détail : rapport-developpeur-collisionneur-v9-v3.md, même dossier.
-"""Collisionneur épistémique N×3 (N = nombre d'espèces activées, de deux à six), protocole v2 : orchestration déterministe,
+# v9-v5 (développeur neuf, Claude Opus 5.5, 21 novembre 2026, GO-2026-11-21-57 « ajoute Neon dans le collisionneur ») :
+#   copie du v9-v3 (850df311…, inchangé, R12), et NON du v9-v4 (46f1d917…, provision 49 152 d'Argon et de Carbon), sur
+#   l'ordre de la mère qui nomme le v9-v3 ; le nom v9-v4 étant pris, ce script porte le nom v9-v5. Changements, et seulement
+#   ceux-là : (1) espèce Neon (gemini-4-neon, fournisseur Gemini, clé GEMINI_API_KEY par son nom), au catalogue et en fin
+#   d'ordre (les lettres des compositions sans Neon ne bougent pas), option --neon ; (2) règle du plafond large de Carbon
+#   (CLAUDE.md, GO-2026-11-21-47), appliquée à Carbon et à Neon (REGLE_TEXTE_MIN) : réflexion bornée par la provision
+#   (budget envoyé, garde v9 gardée) et au moins 16 000 jetons de texte au-delà, sous chaque plafond (sortie et relance),
+#   vérifiés à la composition et avant le comptage de chaque cellule ; un arrêt en MAX_TOKENS sans texte chez elles est un
+#   défaut de réglage, pas une réponse : arrêt au code 9, sans relance au même réglage ; (3) option --cle-openai NOM
+#   (défaut OPENAI_API_KEY) : nom de la variable qui porte la clé d'OpenAI, lue pour l'envoi et pour le comptage, jamais
+#   affichée.
+#   Détail : rapport-collisionneur-v9-v5-et-consultation-v5-v1.md, même dossier.
+"""Collisionneur épistémique N×3 (N = nombre d'espèces activées, de deux à sept), protocole v2 : orchestration déterministe,
 sans agent.
 
 Corrige la v1 :
@@ -49,33 +61,42 @@
 L'étage III (v2.1) est ciblé : il soumet aux modèles une question écrite par l'arbitre. Il est volontairement ancré sur
 cette question ; c'est pourquoi il reste séparé des étages I et II, qui gardent leur émission à l'aveugle (règle B2).
 
-Usage (ESPÈCES : au moins deux options parmi --fable --opus --argon --kimi --astra --carbon, toujours écrites) :
-  python collisionneur_v9_v3.py devis   ESPÈCES --faits FAITS.md [--question QUESTION.md]
-  python collisionneur_v9_v3.py etage1  ESPÈCES [--cle-anthropic NOM] --faits FAITS.md --sortie DOSSIER [--plafond-usd 40]
-                                        [--ligne-usd MONTANT] [--reprise] [--accepter-absence ID]
-  python collisionneur_v9_v3.py etage2  ESPÈCES [--cle-anthropic NOM] --sortie DOSSIER --arbitrage ARBITRAGE.md [...]
-  python collisionneur_v9_v3.py etage3  ESPÈCES [--cle-anthropic NOM] --sortie DOSSIER --question QUESTION.md
-                                        [--faits FAITS.md] [--plafond-usd 40] [--ligne-usd MONTANT] [--reprise]
-  python collisionneur_v9_v3.py devis-reprise DOSSIER --ligne-usd MONTANT [--max-fable N]   (sans réseau)
-  python collisionneur_v9_v3.py verifier DOSSIER
-  python collisionneur_v9_v3.py jev-test
+Usage (ESPÈCES : au moins deux options parmi --fable --opus --argon --kimi --astra --carbon --neon, toujours écrites) :
+  python collisionneur_v9_v5.py devis   ESPÈCES --faits FAITS.md [--question QUESTION.md]
+  python collisionneur_v9_v5.py etage1  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --faits FAITS.md --sortie DOSSIER
+                                        [--plafond-usd 40] [--ligne-usd MONTANT] [--reprise] [--accepter-absence ID]
+  python collisionneur_v9_v5.py etage2  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
+                                        --arbitrage ARBITRAGE.md [...]
+  python collisionneur_v9_v5.py etage3  ESPÈCES [--cle-anthropic NOM] [--cle-openai NOM] --sortie DOSSIER
+                                        --question QUESTION.md [--faits FAITS.md] [--plafond-usd 40] [--ligne-usd MONTANT]
+                                        [--reprise]
+  python collisionneur_v9_v5.py devis-reprise DOSSIER --ligne-usd MONTANT [--max-fable N]   (sans réseau)
+  python collisionneur_v9_v5.py verifier DOSSIER
+  python collisionneur_v9_v5.py jev-test
 --ligne-usd MONTANT (v9-v3) : ligne de dépense ouverte au premier lancement qui la donne, consignée au journal ; tout envoi
 dont le pire cas ferait dépasser la ligne (dépense depuis son ouverture) est refusé avant l'envoi.
 --reprise (v9-v3) : déclare au journal qu'un run commencé par un autre script est repris par celui-ci ; sans elle, le
 script refuse un dossier dont les essais portent une autre empreinte de script.
 --cle-anthropic NOM : nom de la variable d'environnement qui porte la clé d'Anthropic (obligatoire avec --fable ou --opus) ;
 --nom-espace-anthropic NOM : nom de la variable de l'espace de travail, s'il en faut un (défaut ANTHROPIC_WORKSPACE_ID).
+--cle-openai NOM (v9-v5) : nom de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY), lue pour
+l'envoi et pour le comptage d'Astra ; la valeur n'est jamais affichée ni écrite.
 Option --jev (étages et devis) : Jev, de TypeSafe AI, audite chaque cellule valide, seule : il ne lit jamais deux
 propositions ensemble, ni les attaques d'une autre. Ses notes vont à l'arbitre, dans jev/notes-jev.md, à lire après les
 cellules, et n'entrent jamais dans un prompt des modèles. Aucun classement n'est produit. Un échec de Jev est consigné
 et n'arrête pas le run. Clé lue dans TYPESAFE_API_KEY.
-Clés lues par leur nom : celle d'Anthropic dans la variable nommée par --cle-anthropic, GEMINI_API_KEY, OPENAI_API_KEY ;
-jamais affichées ni écrites. Kimi passe par le relais local (KIMI_RELAIS_URL), sans clé ici.
+Clés lues par leur nom : celle d'Anthropic dans la variable nommée par --cle-anthropic, GEMINI_API_KEY (Argon, Carbon,
+Neon), celle d'OpenAI dans la variable nommée par --cle-openai (défaut OPENAI_API_KEY) ; jamais affichées ni écrites. Kimi
+passe par le relais local (KIMI_RELAIS_URL), sans clé ici.
 Codes de sortie : 0 fini, 1 usage ou vérification en échec, 2 arrêt à une porte, 3 modèle différent,
 4 plafond de dépense, 5 échec de l'API ou envoi interrompu (compté au pire), 6 garde de dépense en défaut (réflexion au-delà
 de la provision, total de jetons au-delà des champs lus, entrée au-delà de l'entrée gardée, usage absent), 7 refus de la garde
-de motifs (rien n'est envoyé), 8 (v9-v3) comptage des jetons d'entrée impossible ou invraisemblable (rien n'est envoyé).
-Le code 4 couvre aussi (v9-v3) la ligne de dépense : refus avant l'envoi, rien n'est envoyé.
+de motifs (rien n'est envoyé), 8 (v9-v3) comptage des jetons d'entrée impossible ou invraisemblable (rien n'est envoyé),
+9 (v9-v5) défaut de réglage chez une espèce sous la règle du plafond large (Carbon, Neon) : arrêt en MAX_TOKENS sans texte
+(coût réel compté, aucune relance au même réglage, aucune cellule écrite).
+Le code 4 couvre aussi (v9-v3) la ligne de dépense : refus avant l'envoi, rien n'est envoyé. Le code 1 couvre aussi (v9-v5)
+un réglage hors de la règle du plafond large (moins de 16 000 jetons de texte au-delà de la provision) : refus à la
+composition, ou avant l'envoi (consigné), rien n'est envoyé.
 """
 import argparse
 import datetime
@@ -95,7 +116,7 @@
 from dataclasses import dataclass, field
 from pathlib import Path
 
-VERSION = "collisionneur-v9-v3"
+VERSION = "collisionneur-v9-v5"
 
 # ---------- table des espèces ----------
 # Prix en USD par million de jetons (entrée, sortie), avec leur source :
@@ -115,7 +136,20 @@
 #   appel-astra-v1.json (« modele_servi »: « gpt-6.2-astra »).
 # - Carbon (gemini-4-carbon) : 4 / 20, RAPPORTÉ (registres/decisions.md, R-3676 : 2 / 10 jusqu'au 1er décembre, puis 4 / 20) ;
 #   compté au prix haut dès maintenant (devis v3, section 3).
+# - Neon (gemini-4-neon), v9-v5 : 3 / 15, tarif lu le 21 novembre 2026 à 13:49Z (palier « Standard », payant, sortie
+#   « including thinking tokens ») sur la page publique de Google https://ai.google.dev/gemini-api/docs/pricing (renvoi vers
+#   https://aistudio.google.com/docs/pricing), versée : docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html
+#   (40202cdd…). Aucun changement de prix daté n'y est écrit pour Neon (Argon et Carbon : 2 / 10 puis 4 / 20 au
+#   1er décembre). Le palier « Priority », 5,40 / 27, n'est pas demandé par ce script. Identifiant vérifié par la liste des
+#   modèles de l'interface (GET v1beta/models, sans génération), le 21 novembre 2026 à 13:49Z : « models/gemini-4-neon »,
+#   outputTokenLimit 65 536, thinking vrai ; copie : liste-modeles-gemini-20261121T134904Z.json (eeec19e8…), même dossier.
+#   Page du modèle (docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html, 2eadc192…) : « Max output 65,536
+#   (default synchronous) », réflexion « Supported (low, medium, high, xhigh) ». Aucun budget de réflexion n'y est documenté.
 # Plafonds de sortie, relance et provision de réflexion : devis v3, section 3 (Carbon : « réglages supposés »).
+# Neon (v9-v5) : sortie et relance 65 536 (plafond synchrone de la page du modèle et de la liste) ; provision 32 768, comme
+# Carbon, soit 32 768 jetons de texte au-delà, au-dessus du plancher de 16 000 de la règle (REGLE_TEXTE_MIN) ; délai 5 400 s,
+# comme Carbon (même compte : 65 536 + 32 768 jetons à 25 jetons par seconde, 3 932 s). Réglages SUPPOSÉS : aucun envoi à
+# Neon n'a été fait.
 # car_par_jeton : garde de l'entrée (caractères par jeton) ; 2,5 pour toutes les espèces depuis la v9-v2 (relevé CL11 chez
 # Google, devis v3, section 6, point 2, condition b ; décision de la mère sur C4 de la contre-lecture ; le v8 comptait 3).
 # delai_s : délai total d'un envoi, par espèce (condition d). Carbon : 65 536 + 32 768 = 98 304 jetons au plus ; à 25 jetons
@@ -138,11 +172,19 @@
               "max": 8000, "max_relance": 32000, "provision": 0, "car_par_jeton": 2.5, "delai_s": 3600},
     "carbon": {"id": "gemini-4-carbon", "fournisseur": "gemini", "prix": (4.0, 20.0),
                "max": 65536, "max_relance": 65536, "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400},
+    "neon": {"id": "gemini-4-neon", "fournisseur": "gemini", "prix": (3.0, 15.0),
+             "max": 65536, "max_relance": 65536, "provision": 32768, "car_par_jeton": 2.5, "delai_s": 5400},
 }
-# Ordre du catalogue : il donne les lettres (A, B, …) aux espèces activées, sans trou.
-ORDRE_CATALOGUE = ("fable", "opus", "argon", "kimi", "astra", "carbon")
-NOMS_CLES = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY", "kimi": None}
+# Ordre du catalogue : il donne les lettres (A, B, …) aux espèces activées, sans trou. v9-v5 : Neon en fin d'ordre.
+ORDRE_CATALOGUE = ("fable", "opus", "argon", "kimi", "astra", "carbon", "neon")
+NOMS_CLES = {"gemini": "GEMINI_API_KEY", "openai": "OPENAI_API_KEY", "kimi": None}  # v9-v5 : openai = défaut de --cle-openai
 MOTIF_NOM_VARIABLE = re.compile(r"^[A-Z_][A-Z0-9_]{0,99}$")
+# v9-v5 : règle du plafond large (CLAUDE.md, « Appels à Carbon », GO-2026-11-21-47 ; étendue à Neon, qui réfléchit, par
+# l'ordre de la mère sous GO-2026-11-21-57) : la réflexion est bornée par la provision (budget envoyé à Google, et garde
+# REFLEXION_HORS_PROVISION gardée), et chaque plafond de sortie (premier envoi et relance) laisse au moins ce nombre de jetons
+# de texte au-delà de la provision. Un arrêt en MAX_TOKENS sans texte chez ces espèces est un défaut de réglage, pas une
+# réponse (code 9, sans relance au même réglage).
+REGLE_TEXTE_MIN = {"carbon": 16000, "neon": 16000}
 
 # Composition du run : fixée par fixer_composition, à partir des options (ou du dossier, pour `verifier`). Vide au départ :
 # aucune espèce n'est implicite.
@@ -201,6 +243,7 @@
 CODE_FINI, CODE_USAGE, CODE_PORTE, CODE_MODELE, CODE_PLAFOND, CODE_ECHEC = 0, 1, 2, 3, 4, 5
 CODE_GARDE, CODE_MOTIF = 6, 7  # v9
 CODE_COMPTE = 8  # v9-v3 : comptage de l'entrée impossible ou invraisemblable, rien n'est envoyé
+CODE_REGLAGE = 9  # v9-v5 : MAX_TOKENS sans texte chez une espèce sous REGLE_TEXTE_MIN, défaut de réglage
 
 # v9-v3 : comptage des jetons d'entrée avant l'envoi. Documentation lue le 20 novembre 2026 :
 # - Anthropic, platform.claude.com/docs/en/build-with-claude/token-counting : POST /v1/messages/count_tokens, réponse
@@ -471,8 +514,26 @@
 
 # ---------- v9 : composition du run ----------
 
-def fixer_composition(especes, nom_cle_anthropic=None, nom_espace_anthropic="ANTHROPIC_WORKSPACE_ID"):
-    """Fixe MODELES et LETTRES à partir des espèces activées. Aucune espèce implicite ; deux au moins."""
+def ecart_regle_texte(m, max_tokens):
+    """v9-v5 : None si le plafond `max_tokens` tient la règle du plafond large pour l'espèce de `m` (ou si elle n'y est pas
+    soumise) ; sinon, le motif du refus. Règle : provision positive (réflexion bornée) et plafond − provision au moins
+    REGLE_TEXTE_MIN[espèce] jetons de texte."""
+    plancher = REGLE_TEXTE_MIN.get(m.get("espece"))
+    if plancher is None:
+        return None
+    if m["provision"] <= 0:
+        return f"{m['espece']} : provision de réflexion nulle ; la règle du plafond large exige une réflexion bornée"
+    if max_tokens - m["provision"] < plancher:
+        return (f"{m['espece']} : plafond de sortie {max_tokens} − provision {m['provision']} = "
+                f"{max_tokens - m['provision']} jetons de texte < {plancher} (règle du plafond large)")
+    return None
+
+
+def fixer_composition(especes, nom_cle_anthropic=None, nom_espace_anthropic="ANTHROPIC_WORKSPACE_ID",
+                      nom_cle_openai=None):
+    """Fixe MODELES et LETTRES à partir des espèces activées. Aucune espèce implicite ; deux au moins.
+    v9-v5 : `nom_cle_openai` (--cle-openai), nom de la variable qui porte la clé d'OpenAI (None : NOMS_CLES["openai"]) ;
+    règle du plafond large vérifiée sur les deux plafonds de chaque espèce qui y est soumise."""
     global MODELES, LETTRES
     inconnues = [e for e in especes if e not in CATALOGUE]
     if inconnues:
@@ -480,8 +541,9 @@
     choisies = [e for e in ORDRE_CATALOGUE if e in especes]
     if len(choisies) < 2:
         raise Arret(CODE_USAGE, "au moins deux espèces, chacune par son option (--fable --opus --argon --kimi --astra "
-                                "--carbon) ; aucune n'est implicite")
-    for nom in (nom_cle_anthropic, nom_espace_anthropic):
+                                "--carbon --neon) ; aucune n'est implicite")
+    nom_cle_openai = NOMS_CLES["openai"] if nom_cle_openai is None else nom_cle_openai
+    for nom in (nom_cle_anthropic, nom_espace_anthropic, nom_cle_openai):
         if nom is not None and not MOTIF_NOM_VARIABLE.match(nom):
             raise Arret(CODE_USAGE, "nom de variable d'environnement mal formé (lettres majuscules, chiffres, « _ »)")
     modeles = {}
@@ -489,10 +551,16 @@
         m = dict(CATALOGUE[espece], espece=espece)
         if m["fournisseur"] == "anthropic":
             m["nom_cle"], m["nom_espace"] = nom_cle_anthropic, nom_espace_anthropic
+        elif m["fournisseur"] == "openai":  # v9-v5
+            m["nom_cle"] = nom_cle_openai
         else:
             m["nom_cle"] = NOMS_CLES[m["fournisseur"]]
         if m["fournisseur"] == "gemini" and m["provision"] <= 0:
             raise Arret(CODE_USAGE, f"{espece} : provision de réflexion nulle ; la garde (a) l'exige")
+        for plafond in (m["max"], m["max_relance"]):  # v9-v5 : règle du plafond large
+            ecart = ecart_regle_texte(m, plafond)
+            if ecart:
+                raise Arret(CODE_USAGE, ecart)
         modeles["ABCDEFGHI"[i]] = m
     MODELES, LETTRES = modeles, tuple(modeles)
     return modeles
@@ -926,11 +994,12 @@
 def appeler_openai(m, prompt, max_tokens):
     """v9 : interface Responses d'OpenAI en mode d'arrière-plan (background, store), puis relevés par requêtes courtes, toutes
     les INTERVALLE_RELEVE_S secondes, jusqu'au délai de l'espèce. La création n'est jamais renvoyée (sauf 429) ; un relevé
-    manqué n'est pas un renvoi et se refait. Délai dépassé : annulation demandée, envoi compté au pire. Clé lue dans
-    OPENAI_API_KEY, jamais affichée."""
-    cle = os.environ.get("OPENAI_API_KEY")
+    manqué n'est pas un renvoi et se refait. Délai dépassé : annulation demandée, envoi compté au pire. Clé lue dans la
+    variable nommée par --cle-openai (v9-v5 ; défaut OPENAI_API_KEY), jamais affichée."""
+    nom_cle = m.get("nom_cle") or NOMS_CLES["openai"]  # v9-v5
+    cle = os.environ.get(nom_cle)
     if not cle:
-        return Reponse(echec="OPENAI_API_KEY absente")
+        return Reponse(echec=f"{nom_cle} absente (variable nommée par --cle-openai)")
     base, locale = base_openai()
     if base is None:
         return Reponse(echec="OPENAI_BASE_URL : boucle locale (essais hors réseau) ou adresse d'OpenAI seulement")
@@ -1146,10 +1215,11 @@
 
 def compter_openai(m, prompt):
     """POST /responses/input_tokens (interface Responses) : même modèle et même entrée que l'envoi ; même restriction
-    d'adresse que l'envoi (base_openai)."""
-    cle = os.environ.get("OPENAI_API_KEY")
+    d'adresse que l'envoi (base_openai). v9-v5 : clé lue dans la variable nommée par --cle-openai."""
+    nom_cle = m.get("nom_cle") or NOMS_CLES["openai"]  # v9-v5
+    cle = os.environ.get(nom_cle)
     if not cle:
-        raise RefusCompte("COMPTE_IMPOSSIBLE", "OPENAI_API_KEY absente")
+        raise RefusCompte("COMPTE_IMPOSSIBLE", f"{nom_cle} absente (variable nommée par --cle-openai)")
     base, locale = base_openai()
     if base is None:
         raise RefusCompte("COMPTE_IMPOSSIBLE", "OPENAI_BASE_URL : boucle locale ou adresse d'OpenAI seulement")
@@ -1253,6 +1323,9 @@
 
 # Statuts de la garde v9 et leur code d'arrêt.
 STATUTS_GARDE = {"USAGE_ABSENT", "REFLEXION_HORS_PROVISION", "ECART_TOTAL_JETONS", "ENTREE_HORS_GARDE"}
+# v9-v5 : statut d'un arrêt en MAX_TOKENS sans texte chez une espèce sous REGLE_TEXTE_MIN (code CODE_REGLAGE). Il ne vient
+# qu'après les gardes de juger : une réflexion au-delà de la provision reste REFLEXION_HORS_PROVISION (code 6).
+STATUT_REGLAGE = "MAX_TOKENS_SANS_TEXTE"
 
 
 def juger(m, rep, prompt, pire, garde=None):
@@ -1278,7 +1351,10 @@
         return "ECART_TOTAL_JETONS", c
     if rep.usage["entree"] > garde:  # v9-v2 (C4) : toutes les espèces ; v9-v3 : garde comptée avant l'envoi
         return "ENTREE_HORS_GARDE", c
-    return statut_reponse(m["fournisseur"], rep), c
+    statut = statut_reponse(m["fournisseur"], rep)
+    if statut == "VIDE" and rep.fin == "MAX_TOKENS" and m.get("espece") in REGLE_TEXTE_MIN:  # v9-v5 : défaut de réglage
+        return STATUT_REGLAGE, c
+    return statut, c
 
 
 # ---------- exécution d'une cellule ----------
@@ -1294,6 +1370,10 @@
     cid = id_cellule(tour, lettre)
     m = MODELES[lettre]
     garder_motifs(dossier, cid, prompt)  # v9 : avant tout envoi, refus nommé
+    for plafond_sortie in (m["max"], m["max_relance"]):  # v9-v5 : règle du plafond large, avant tout envoi et tout comptage
+        ecart = ecart_regle_texte(m, plafond_sortie)
+        if ecart:
+            refuser_avant_envoi(dossier, cid, "REGLE_TEXTE_MIN", ecart, CODE_USAGE)
     try:  # v9-v3 : jetons d'entrée comptés avant tout envoi ; un compte inutilisable arrête, rien n'est envoyé
         compte = compter_entree(m, prompt)
     except RefusCompte as e:
@@ -1345,6 +1425,11 @@
         if statut in STATUTS_GARDE:
             raise Arret(CODE_GARDE, f"{cid} : garde de dépense en défaut ({statut}) ; coût compté "
                                     f"{entree['cout_usd']:.2f} USD ; passage arrêté, la décision revient à l'arbitre")
+        if statut == STATUT_REGLAGE:  # v9-v5
+            raise Arret(CODE_REGLAGE, f"{cid} : arrêt en MAX_TOKENS sans texte ({rep.usage.get('reflexion', 0)} jetons de "
+                                      f"réflexion lus ; plafond {max_tokens}, provision {m['provision']}) : défaut de "
+                                      f"réglage, pas une réponse ; coût compté {entree['cout_usd']:.2f} USD ; aucune "
+                                      f"relance au même réglage, la décision revient à l'arbitre")
         if statut == "MODELE_DIFFERENT":
             raise Arret(CODE_MODELE, f"{cid} : modèle servi {rep.modele_servi!r} au lieu de {m['id']!r} ; arrêt")
         if statut == "OK":
@@ -1793,6 +1878,8 @@
         ajouter_options_especes(s)
         s.add_argument("--cle-anthropic", help="NOM de la variable d'environnement qui porte la clé d'Anthropic")
         s.add_argument("--nom-espace-anthropic", default="ANTHROPIC_WORKSPACE_ID")
+        s.add_argument("--cle-openai", default=NOMS_CLES["openai"],  # v9-v5
+                       help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY)")
         s.add_argument("--sortie", required=True)
         s.add_argument("--plafond-usd", type=float, default=PLAFOND_DEFAUT_USD)
         s.add_argument("--accepter-absence", action="append", default=[])
@@ -1858,7 +1945,7 @@
     dossier = Path(a.sortie)
     etage = {"etage1": 1, "etage2": 2, "etage3": 3}[a.commande]
     try:
-        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic)
+        fixer_composition(especes_demandees(a), a.cle_anthropic, a.nom_espace_anthropic, a.cle_openai)  # v9-v5
         verifier_cles()
         if etage == 1:
             verser_une_fois(dossier / "faits.md", a.faits, "--faits")
```

### 7.2 Consultation : v4 (`b31fecf2…`) vers v5 (`4c44b89e…`), différentiel unifié complet

```diff
--- appel_modeles_externes_v4.py
+++ appel_modeles_externes_v5.py
@@ -1,4 +1,19 @@
-"""Version 4 (21 novembre) de l'appel aux modèles externes. Remplace le v3 (8aee878d…, gardé sans modification, R12).
+"""Version 5 (21 novembre, GO-2026-11-21-57) de l'appel aux modèles externes : Neon, et clé d'OpenAI nommée.
+Remplace le v4 (b31fecf2…, gardé sans modification, R12). Changements, et seulement ceux-là :
+- espèce Neon (gemini-4-neon, flux continu Gemini, clé GEMINI_API_KEY par son nom) : prix 3 / 15 USD par million (palier
+  « Standard » de la page publique de Google lue le 21 novembre 2026 à 13:49Z, versée :
+  docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html, 40202cdd…) ; identifiant vérifié par la liste des modèles de
+  l'interface (docs/notes/collisionneur-v9/liste-modeles-gemini-20261121T134904Z.json, eeec19e8… : outputTokenLimit 65 536,
+  thinking vrai) ; défaut 32 768 de réflexion + 32 768 de texte = 65 536, le plafond synchrone documenté ;
+- règle du plafond large de Carbon (CLAUDE.md, GO-2026-11-21-47) appliquée à Neon, qui réfléchit : réflexion bornée par
+  `thinkingBudget` et au moins 16 000 jetons de texte au-delà (refus en dessous), comme Carbon et Argon dans le v4 ; un arrêt
+  en « MAX_TOKENS » sans texte chez Carbon ou Neon est dit « défaut de réglage, pas une réponse » (code 3 inchangé) ;
+- option --cle-openai NOM (défaut OPENAI_API_KEY) : nom de la variable qui porte la clé d'OpenAI (Astra) ; nom mal formé
+  refusé sans être répété ; la valeur n'est jamais affichée ni écrite ; le NOM de la variable lue est écrit dans le JSON.
+Essais hors réseau : essais_appel_modeles_externes_v5.py (les dix essais du v4, rejoués tels quels, et ceux du v5).
+
+Ce qui suit est l'en-tête du v4, inchangé.
+Version 4 (21 novembre) de l'appel aux modèles externes. Remplace le v3 (8aee878d…, gardé sans modification, R12).
 
 Pourquoi : le v3 a perdu deux échecs d'Astra (« failed » sans motif : il ne gardait ni l'identifiant de la réponse ni son
 objet d'erreur) et un échec de Carbon (« MAX_TOKENS » : la réflexion « high », non bornée, a mangé les 32 000 jetons de
@@ -15,25 +30,31 @@
 - aucun renvoi silencieux : tout échec est écrit dans le JSON et rend un code non nul (1 échec ou refus, 3 réponse
   tronquée ou incomplète — texte partiel écrit à part, en `.partiel.md`, jamais sous le nom de la réponse) ;
 - essais hors réseau : `essais_appel_modeles_externes_v4.py` (transport simulé).
-Usage : python -I appel_modeles_externes_v4.py {carbon|argon|astra} ENONCE SORTIE_MD SORTIE_JSON
-        [--reflexion N] [--texte N] [--efforts xhigh,high] [--plafond-usd X]
-Clés lues par leur nom seulement (OPENAI_API_KEY, GEMINI_API_KEY) ; jamais affichées ni écrites.
+Usage (v5) : python -I appel_modeles_externes_v5.py {argon|astra|carbon|neon} ENONCE SORTIE_MD SORTIE_JSON
+        [--reflexion N] [--texte N] [--efforts xhigh,high] [--plafond-usd X] [--cle-openai NOM]
+Clés lues par leur nom seulement (celle d'OpenAI dans la variable nommée par --cle-openai, défaut OPENAI_API_KEY ;
+GEMINI_API_KEY) ; jamais affichées ni écrites.
 """
 import argparse
 import hashlib
 import json
 import os
+import re
 import sys
 import time
 import urllib.error
 import urllib.request
 
 PLAFOND_APPEL_USD = 4.0
-PRIX = {"carbon": (4.0, 20.0), "astra": (10.0, 50.0), "argon": (10.0, 50.0)}
-MODELE = {"carbon": "gemini-4-carbon", "astra": "gpt-6.2-astra", "argon": "gemini-4-argon"}
-CLE = {"carbon": "GEMINI_API_KEY", "argon": "GEMINI_API_KEY", "astra": "OPENAI_API_KEY"}
-DEFAUTS = {"carbon": (24000, 16000), "argon": (24000, 16000), "astra": (32000, 16000)}  # (réflexion, texte)
+PRIX = {"carbon": (4.0, 20.0), "astra": (10.0, 50.0), "argon": (10.0, 50.0), "neon": (3.0, 15.0)}  # v5 : Neon
+MODELE = {"carbon": "gemini-4-carbon", "astra": "gpt-6.2-astra", "argon": "gemini-4-argon", "neon": "gemini-4-neon"}
+CLE = {"carbon": "GEMINI_API_KEY", "argon": "GEMINI_API_KEY", "astra": "OPENAI_API_KEY", "neon": "GEMINI_API_KEY"}
+DEFAUTS = {"carbon": (24000, 16000), "argon": (24000, 16000), "astra": (32000, 16000),
+           "neon": (32768, 32768)}  # (réflexion, texte) ; v5 : Neon, 65 536 au total, plafond synchrone documenté
 TEXTE_MIN_GEMINI = 16000
+ESPECES_GEMINI = ("carbon", "argon", "neon")  # v5 : espèces servies par le flux Gemini, sous le plancher de texte
+REGLE_PLAFOND_LARGE = ("carbon", "neon")  # v5 : règle de CLAUDE.md (GO-2026-11-21-47), étendue à Neon (GO-2026-11-21-57)
+MOTIF_NOM_VARIABLE = re.compile(r"^[A-Z_][A-Z0-9_]{0,99}$")  # v5 : --cle-openai, comme le collisionneur
 URL_OPENAI = "https://api.openai.com/v1/responses"
 URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/{}:streamGenerateContent?alt=sse"
 RELEVE_S = 20
@@ -225,8 +246,10 @@
     if statut == "STOP" and res["texte"] and not res["erreur_fournisseur"]:
         return CODE_OK, "complet"
     if statut == "MAX_TOKENS":
+        reglage = (" ; défaut de réglage, pas une réponse (règle du plafond large)"
+                   if espece in REGLE_PLAFOND_LARGE and not res["texte"] else "")  # v5
         return CODE_TRONQUE, (f"MAX_TOKENS : plafond de sortie atteint ({res['jetons_reflexion']} jetons de réflexion, "
-                              f"texte {'partiel' if res['texte'] else 'absent'})")
+                              f"texte {'partiel' if res['texte'] else 'absent'}){reglage}")
     return CODE_ECHEC, (f"statut {statut} ; erreur du fournisseur : {res['erreur_fournisseur']} ; "
                         f"détails : {res['details_incomplet']}")
 
@@ -235,7 +258,7 @@
     r0, t0 = DEFAUTS[espece]
     reflexion = r0 if reflexion is None else reflexion
     texte = t0 if texte is None else texte
-    if espece in ("carbon", "argon") and texte < TEXTE_MIN_GEMINI:
+    if espece in ESPECES_GEMINI and texte < TEXTE_MIN_GEMINI:  # v5 : Neon compris
         raise ValueError(f"texte {texte} < {TEXTE_MIN_GEMINI} jetons au-delà de la réflexion : refusé pour {espece}")
     if reflexion < 0 or texte <= 0:
         raise ValueError("réflexion et texte doivent être positifs")
@@ -250,11 +273,15 @@
 
 def executer(espece, chemin_enonce, sortie_md, sortie_json, reflexion=None, texte=None, efforts=None,
              plafond_usd=PLAFOND_APPEL_USD, environ=None, transport_json=http_json, transport_flux=http_flux,
-             dormir=attendre):
+             dormir=attendre, nom_cle_openai=CLE["astra"]):
     environ = os.environ if environ is None else environ
     if plafond_usd > PLAFOND_APPEL_USD:
         print(f"ARRET : plafond demandé {plafond_usd} > {PLAFOND_APPEL_USD} USD", file=sys.stderr)
         return CODE_ECHEC
+    if not isinstance(nom_cle_openai, str) or not MOTIF_NOM_VARIABLE.match(nom_cle_openai):  # v5 : nom jamais répété
+        print("ARRET : --cle-openai : nom de variable d'environnement mal formé (lettres majuscules, chiffres, « _ »)",
+              file=sys.stderr)
+        return CODE_ECHEC
     for chemin in (sortie_md, sortie_json, sortie_md + ".partiel.md"):
         if os.path.exists(chemin):
             print(f"ARRET : {chemin} existe déjà (on n'écrase jamais, R12)", file=sys.stderr)
@@ -269,7 +296,7 @@
     if pire > plafond_usd:
         print(f"ARRET : pire cas {pire:.4f} USD > plafond {plafond_usd} USD", file=sys.stderr)
         return CODE_ECHEC
-    nom_cle = CLE[espece]
+    nom_cle = nom_cle_openai if espece == "astra" else CLE[espece]  # v5 : --cle-openai
     cle = environ.get(nom_cle)
     if not cle:
         print(f"ARRET : variable {nom_cle} absente", file=sys.stderr)
@@ -282,7 +309,7 @@
         res = appeler_gemini(enonce, cle, reglage, journal, espece, transport_flux)
     code, motif = verdict(espece, res)
     pe, ps = PRIX[espece]
-    meta = {"version_script": "v4", "espece": espece, "modele_demande": MODELE[espece],
+    meta = {"version_script": "v5", "espece": espece, "modele_demande": MODELE[espece], "variable_cle": nom_cle,
             "modele_servi": res["modele_servi"], "id_reponse": res["id_reponse"], "fin": res["statut"],
             "verdict": "ok" if code == CODE_OK else ("tronque" if code == CODE_TRONQUE else "echec"),
             "motif": motif, "erreur_fournisseur": res["erreur_fournisseur"],
@@ -321,9 +348,12 @@
     p.add_argument("--texte", type=int, default=None, help="jetons de texte au-delà de la réflexion")
     p.add_argument("--efforts", default=None, help="Astra : efforts essayés dans l'ordre sur refus 400, ex. xhigh,high")
     p.add_argument("--plafond-usd", type=float, default=PLAFOND_APPEL_USD)
+    p.add_argument("--cle-openai", default=CLE["astra"],  # v5
+                   help="NOM de la variable d'environnement qui porte la clé d'OpenAI (défaut OPENAI_API_KEY)")
     a = p.parse_args(argv)
     efforts = tuple(x.strip() for x in a.efforts.split(",") if x.strip()) if a.efforts else None
-    return executer(a.espece, a.enonce, a.sortie_md, a.sortie_json, a.reflexion, a.texte, efforts, a.plafond_usd)
+    return executer(a.espece, a.enonce, a.sortie_md, a.sortie_json, a.reflexion, a.texte, efforts, a.plafond_usd,
+                    nom_cle_openai=a.cle_openai)
 
 
 if __name__ == "__main__":
```
