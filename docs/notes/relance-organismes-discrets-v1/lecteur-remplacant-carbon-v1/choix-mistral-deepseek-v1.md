You are powered by the model named Opus 5.5.

# Choix du modèle « lecteur » : Mistral ou DeepSeek (v1)

Recherche faite le 20 novembre 2026 sur le web, pages officielles d'abord. Aucune clé utilisée, aucun compte créé, aucune dépense.
Toutes les pages ont été lues par un outil de lecture automatique, qui résume la page. Quand une page n'a pas pu être ouverte, c'est dit.
« Non trouvé » veut dire : cherché, pas trouvé. Rien n'est deviné.

## 1. Le meilleur modèle de chaque famille, par l'interface de programmation, au 20 novembre 2026

### Mistral : Mistral Large 4

- Identifiant d'API : `mistral-large-4-0`. C'est l'identifiant que donne la page officielle sur le raisonnement. La fiche du modèle affiche aussi `mistral-large-4`. Version v26.10.
- Statut : la fiche officielle porte l'étiquette « GA » (disponibilité générale), avec une date du 5 novembre 2026. Avant, le modèle était en « préversion publique » (depuis le 6 octobre 2026).
- Pourquoi c'est le meilleur de la famille : c'est le premier des « modèles mis en avant » de la page des modèles. Mistral Medium 3.5 est classé parmi les modèles dépréciés. Mistral Small 4 est un modèle plus petit.
- Fenêtre de contexte : 1 million de jetons. Longueur maximale de sortie : non indiquée sur la fiche officielle.
- Raisonnement : paramètre `reasoning_effort`, valeurs `low`, `medium`, `high`. Le maximum est `high`, qui est aussi le défaut. Réglage : `reasoning_effort="high"` dans l'appel à `/v1/chat/completions`. Échantillonnage conseillé par Mistral : `temperature=1.0`, `top_p=0.95`.
- Sortie structurée : oui (« Structured Outputs »).
- Prix par million de jetons : 0,70 dollar en entrée ; 0,07 dollar en entrée mise en cache ; 2,10 dollars en sortie. Aucun prix à part pour le raisonnement n'est indiqué : les jetons de raisonnement sont, à ma connaissance, comptés comme sortie, mais la page ne le dit pas. Le traitement par lots coûte 50 % de moins (page des prix). Les points d'accès régionaux (Europe, États-Unis) coûtent 1,1 fois le prix courant.
- Sources :
  - https://docs.mistral.ai/models/mistral-large-4-0 (fiche officielle : contexte, prix, statut, date)
  - https://docs.mistral.ai/capabilities/reasoning (paramètre et valeurs)
  - https://docs.mistral.ai/models/overview (liste des modèles et statut de Medium 3.5)
  - https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B (valeurs de raisonnement, échantillonnage conseillé)
  - https://mistral.ai/pricing (remise de 50 % par lots)
  - https://docs.mistral.ai/inference/regional-inference (points d'accès régionaux)

### DeepSeek : DeepSeek V4.1 Flash, version du 17 octobre (DeepSeek-V4.1-Flash-1017)

- Identifiant d'API : `deepseek-flash` (adresse de base `https://api.deepseek.com`). Il sert aujourd'hui DeepSeek-V4.1-Flash-1017.
- L'autre candidat de la famille est `deepseek-v4-pro` (DeepSeek-V4-Pro-0813), le « vaisseau amiral » nommé ainsi par DeepSeek. Je retiens pourtant le Flash 1017 comme le meilleur :
  - DeepSeek dit lui-même que V4.1 Flash dépasse V4 Pro (annonce du 10 septembre 2026).
  - Les deux classements indépendants qui notent les deux modèles le mettent devant (voir la partie 2 : indice d'Artificial Analysis 33 contre 23 ; indice de Vals 61,26 % contre 52,97 %).
  - Réserve : sur la lecture de longs textes, le seul chiffre commun publié par DeepSeek (LongBench v2, sur les modèles de base, avant l'affinage) met V4 Pro devant (51,5 contre 45,2).
- Fenêtre de contexte : 1 million de jetons. Sortie maximale : 384 000 jetons.
- Raisonnement : activé par défaut, effort par défaut `high`. Valeurs de l'effort : `low`, `high`, `max`.
  - Pour l'effort maximal, au format compatible OpenAI : `reasoning_effort="max"`. Le mode « pensée » se force avec `extra_body={"thinking": {"type": "enabled"}}` dans le kit OpenAI (c'est déjà le défaut).
  - Au format compatible Anthropic : `output_config={"effort": "max"}`.
  - En mode pensée, `temperature`, `presence_penalty` et `frequency_penalty` n'ont aucun effet (pas d'erreur, mais pas d'effet).
  - Sortie JSON : prise en charge.
- Prix par million de jetons (dollars) :

| | Heures creuses | Heures pleines |
|---|---|---|
| Entrée, en cache | 0,003 | 0,006 |
| Entrée, hors cache | 0,15 | 0,30 |
| Sortie (raisonnement compris, pas de prix à part indiqué) | 0,60 | 1,20 |

  - Heures pleines : de 01 h à 04 h et de 06 h à 10 h (temps universel coordonné), du lundi au vendredi, hors jours fériés chinois. Tout le reste est en heures creuses, au demi-tarif.
  - Pour comparaison, `deepseek-v4-pro` : 0,66 / 1,98 dollar en heures creuses, 1,32 / 3,96 dollars en heures pleines.
- Sources :
  - https://api-docs.deepseek.com/quick_start/pricing (modèles, contexte, prix, heures pleines)
  - https://api-docs.deepseek.com/guides/thinking_mode (réglage du raisonnement)
  - https://api-docs.deepseek.com/updates (historique des versions)
  - https://api-docs.deepseek.com/news/news260910 (annonce de V4.1 Flash)
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash (tableau de comparaison avec V4 Pro)

## 2. Bancs d'essais publics qui correspondent au rôle

Constat principal : je n'ai trouvé **aucun banc indépendant qui note les deux modèles** sur la lecture de longs textes, le suivi de consigne ou la citation fidèle. Les chiffres du rôle sont donc soit publiés par le fournisseur lui-même, soit absents. Les seules comparaisons indépendantes directes sont des indices composites.

Dans la table, « ML4 » veut dire Mistral Large 4 ; « Flash 1017 » veut dire DeepSeek V4.1 Flash 1017 ; « V4 Pro » veut dire DeepSeek V4 Pro.

### 2.1 Bancs qui correspondent au rôle

| Banc (ce qu'il mesure) | Mistral Large 4 | DeepSeek V4.1 Flash 1017 | DeepSeek V4 Pro (pour mémoire) | Date | Source |
|---|---|---|---|---|---|
| MRCR à 1 million de jetons (retrouver une information dans un long contexte) | non trouvé | non trouvé | 83,5 (effort maximal), publié par DeepSeek | avril 2026 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro |
| CorpusQA à 1 million de jetons (questions sur un corpus long) | non trouvé | non trouvé | 62,0 (effort maximal), publié par DeepSeek | avril 2026 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro |
| LongBench v2 (lecture de longs textes), modèle de base seulement, une seule démonstration | non trouvé | 45,2 (modèle de base), publié par DeepSeek | 51,5 (modèle de base), publié par DeepSeek | 2026 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash |
| Classement public de LongBench v2 | absent | absent | absent | dernière mise à jour du classement : 6 mai 2025 | https://longbench2.github.io/ |
| RULER (longs contextes synthétiques) | non trouvé | non trouvé | non trouvé | — | — |
| Fiction.LiveBench (compréhension de longues histoires) | non trouvé | non trouvé | non trouvé | — | https://epoch.ai/benchmarks/fictionlivebench |
| AA-LCR (raisonnement sur longs contextes, Artificial Analysis) | non trouvé | non trouvé | non trouvé | page lue le 20 novembre 2026 | https://artificialanalysis.ai/evaluations/artificial-analysis-long-context-reasoning |
| IFEval / IFBench (suivi de consigne) | non trouvé | non trouvé | non trouvé | page lue le 20 novembre 2026 | https://artificialanalysis.ai/evaluations/ifbench |
| FACTS Grounding (réponse fidèle à un document fourni) | non trouvé | non trouvé | non trouvé (seulement « FACTS Parametric » sur le modèle de base : 62,6, qui mesure la mémoire du modèle et non la fidélité à la source) | — | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro |
| Usage comme juge (JudgeBench, RewardBench) | non trouvé | non trouvé | un article de 2026 cite des paires de chiffres pour V4 Pro sur JudgeBench, sens non vérifié ; je ne les retiens pas | — | — |

### 2.2 Comparaisons indépendantes directes (indices composites, pas propres au rôle)

| Banc | Mistral Large 4 | DeepSeek V4.1 Flash 1017 | DeepSeek V4 Pro 0813 | Date | Source |
|---|---|---|---|---|---|
| Indice d'intelligence d'Artificial Analysis, version 5.0.1 (neuf épreuves ; aucune de longs contextes ni de suivi de consigne ; une sur les hallucinations) | 26 (effort `high`) | 33 (effort maximal) | 23 (effort maximal) | pages lues le 20 novembre 2026 | https://artificialanalysis.ai/models/mistral-large-4 ; https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017 ; https://artificialanalysis.ai/models/deepseek-v4-pro |
| Jetons de sortie pour passer cet indice (mesure de la verbosité) | 107 millions | 174 millions | 119 millions | idem | idem |
| Coût par tâche de cet indice | 2,06 dollars | 0,60 dollar | 1,77 dollar | idem | idem |
| Indice de Vals (tâches professionnelles) | 45,09 % (version préliminaire, effort `high`) | 61,26 % ±1,05 (effort maximal) | 52,97 % ±1,04 (effort maximal) | pages lues le 20 novembre 2026 | https://vals.ai/models/mistralai_mistral-large-4 ; https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017 ; https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813 |
| Indice juridique de Vals (lecture de documents juridiques) | 65,61 % ±1,63 | 71,86 % ±1,82 | 69,01 % ±1,77 | idem | idem |
| Recherche juridique de Vals (Legal Research Bench) | 31,73 % ±3,23 | 45,19 % ±3,46 | 40,87 % ±3,42 | idem | idem |
| Agent financier de Vals (Finance Agent v2.1) | 61,38 % ±2,02 | 62,93 % ±2,03 | 57,12 % ±2,08 | idem | idem |

Réserves sur ces chiffres :
- Vals a noté la **version préliminaire** de Mistral Large 4, pas la version générale du 5 novembre. Mistral annonce un net progrès entre les deux sur une épreuve de code (Terminal-Bench 4.0 : 28 % puis 41 %). L'écart de Vals pourrait donc se réduire.
- Les pages de Vals se contredisent parfois d'une capture à l'autre. Exemple : un extrait de recherche donnait 56,58 % pour le Flash 1017, la page lue donne 61,26 %. J'ai gardé la page lue.
- Ces indices mesurent surtout le raisonnement et le travail d'agent. Ils ne mesurent ni la lecture de 50 000 jetons ni la citation littérale.

## 3. Ce qui compte hors des scores

### Données envoyées

| Point | Mistral | DeepSeek |
|---|---|---|
| Entraînement sur les données de l'API | Offre payante : « Customers retain full control over this processing and have the right to opt out at any time ». Offre gratuite : Mistral « may use your data (input and output) to train ». Pour refuser : console, menu Admin, « Privacy », désactiver « Data usage for improving our services ». Le réglage par défaut de l'offre payante n'est pas écrit sur la page lue. | La politique de confidentialité (mise à jour du 10 février 2026) cite parmi ses finalités « to train and improve our technology », avec les « User Input ». Droit de refus : par courriel à privacy@deepseek.com. Aucun bouton de refus documenté. Les conditions de la plateforme (en vigueur depuis le 29 avril 2026) ne disent ni oui ni non sur l'entraînement avec les données de l'API. |
| Lieu de stockage | Point d'accès européen `api.eu.mistral.ai` : centres de données de l'Union européenne et de l'Association européenne de libre-échange (+10 % de prix). Le point d'accès global ne s'engage sur aucun lieu. | « we directly collect, process and store your Personal Data in People's Republic of China ». Conditions soumises au droit de la République populaire de Chine (article 10.1). |
| Conservation | Sans option : 30 jours glissants pour la surveillance des abus. Source : mémo d'Open Terms Archive sur les conditions de Mistral (2024) ; la page officielle n'a pas pu être ouverte (erreur 404). | « as long as necessary to provide our Services ». Aucune durée fixe. |
| Option de non-conservation | Oui : « Zero Data Retention », offre à l'usage, sur demande au support, accordée au cas par cas. Ne couvre que les appels sans état (dont `chat/completions`) ; ne couvre ni les fichiers ni les agents. | Non trouvée. |
| Sources | https://help.mistral.ai/en/articles/323757-do-you-use-my-user-data-to-train-your-artificial-intelligence-models ; https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training ; https://docs.mistral.ai/admin/monitor-comply/zero-data-retention ; https://docs.mistral.ai/inference/regional-inference ; https://opentermsarchive.org/en/memos/mistral-ai-retains-api-prompts-and-outputs-for-30-days/ | https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html ; https://cdn.deepseek.com/policies/en-UK/deepseek-open-platform-terms-of-service.html |

### Stabilité de l'API

**DeepSeek :**
- Le nom `deepseek-flash` suit toujours « the latest model ». Le modèle a changé le 10 septembre 2026, puis le 17 octobre 2026, sans changement de nom.
- Les anciens noms (`deepseek-v4-flash`) sont redirigés vers le nouveau modèle.
- Aucun identifiant figé par version n'est documenté pour le Flash.
- Pour une mesure scellée, c'est un risque réel : le modèle peut changer pendant la course.
- Les prix ont aussi bougé : le passage aux heures pleines et creuses le 16 août 2026 a multiplié le prix par plus de 10 pour certains modèles (InfoWorld). Le prix a ensuite baissé le 10 septembre.
- Source : https://api-docs.deepseek.com/updates

**Mistral :**
- L'identifiant porte un numéro de version (`mistral-large-4-0`, v26.10).
- Mistral publie un tableau des dépréciations avec des dates d'arrêt plusieurs mois à l'avance. Exemple : Mistral Large 2.1 déprécié le 27 février 2026, retiré le 31 mai 2026.
- Je n'ai pas vérifié que `mistral-large-4-0` reste figé si Mistral publie une mise à jour.
- Source : https://docs.mistral.ai/models/overview

### Limites de débit

**DeepSeek :**
- 2 500 requêtes simultanées pour `deepseek-flash` (500 pour `deepseek-v4-pro`), par compte et non par clé.
- Au-delà : erreur 429.
- Une requête qui n'a pas commencé après 10 minutes est fermée par le serveur.
- Une hausse de la limite peut être demandée, sans frais.
- Source : https://api-docs.deepseek.com/quick_start/rate_limit

**Mistral :**
- Limites par palier d'usage : requêtes par seconde et jetons par minute ou par mois.
- Les valeurs chiffrées ne sont visibles que dans la console, une fois connecté.
- Ajouter du crédit ne relève pas les limites. Les lots ne comptent pas dans les limites en temps réel.
- Sources : https://docs.mistral.ai/resources/known-limitations ; https://docs.mistral.ai/admin/workspaces/usage-limits.md

### Ordre de grandeur du coût

Calcul indicatif. Les hypothèses sont à moi, ce n'est pas une mesure : 3 000 épisodes, 50 000 jetons en entrée par épisode (hors cache), 10 000 jetons de sortie (raisonnement compris).
- DeepSeek Flash : environ 40 dollars en heures creuses, environ 81 dollars en heures pleines.
- Mistral Large 4 : environ 168 dollars au prix courant, environ 84 dollars par lots.
- Le Flash est plus bavard (174 millions de jetons de sortie contre 107 millions sur l'indice d'Artificial Analysis). Même en multipliant sa sortie par 1,6, il reste le moins cher.

## 4. Recommandation

**DeepSeek V4.1 Flash (`deepseek-flash`, version DeepSeek-V4.1-Flash-1017), avec `reasoning_effort="max"`. Confiance : 0,6.**

Pourquoi :
- La consigne du directeur est de prendre le meilleur sur les bancs. Sur toutes les comparaisons indépendantes qui notent les deux modèles, le Flash 1017 passe devant Mistral Large 4 :
  - indice d'Artificial Analysis : 33 contre 26 ;
  - indice de Vals : 61,26 % contre 45,09 % ;
  - indice juridique de Vals (lecture de documents) : 71,86 % contre 65,61 %.
- Il coûte environ 2 à 4 fois moins cher.
- Il a la même fenêtre d'un million de jetons.

Pourquoi la confiance n'est que de 0,6 :
- Aucun banc indépendant propre au rôle (longs contextes, consigne, citation littérale) ne note les deux modèles.
- Mistral Large 4 n'a été noté par Vals qu'en version préliminaire.

Ce qui ferait changer pour **Mistral Large 4** (`mistral-large-4-0`, `reasoning_effort="high"`, point d'accès européen) :
1. **Les données.** Si les transcriptions ne doivent pas être stockées en Chine, ni pouvoir servir à l'entraînement sans un refus écrit et confirmé, Mistral l'emporte. Mistral offre l'Europe, un bouton de refus et la non-conservation sur demande. DeepSeek n'offre ni lieu au choix, ni non-conservation. C'est à Lazar de trancher, et c'est à mes yeux le risque principal.
2. **La reproductibilité.** Si la mesure exige un modèle figé du premier au dernier épisode, l'alias `deepseek-flash`, qui suit toujours la dernière version, pose problème. DeepSeek l'a déjà changé deux fois en deux mois. Si on garde DeepSeek, il faut consigner la version affichée avant et après la course, et surveiller la page des mises à jour.
3. **Un essai pilote.** Un essai sur une vingtaine d'épisodes, avec vérification des citations par programme, mesurerait directement le taux de citations littérales exactes et le respect du format à deux champs. Si Mistral Large 4 y fait nettement mieux, on bascule. L'essai est payant, donc il faut un devis et un GO.
4. **Un nouveau chiffre.** Une publication indépendante (Artificial Analysis, Vals, classement de MRCR ou de FACTS) qui mettrait Mistral Large 4 devant sur les longs contextes ou la fidélité à la source ferait aussi changer.

## 5. Créer une clé d'API chez DeepSeek (seulement ce que dit la documentation officielle)

1. **Console :** https://platform.deepseek.com
   - La documentation lue ne décrit pas les étapes d'inscription elles-mêmes. Elle renvoie seulement à la plateforme.
2. **Crédit prépayé :** page « Top up », https://platform.deepseek.com/top_up (lien donné par la page des codes d'erreur).
   - Moyens de paiement cités par la foire aux questions officielle : PayPal, carte bancaire, Alipay, WeChat Pay.
   - Le solde rechargé n'expire pas. Le solde offert a une date d'expiration, visible sur la page « Billing ».
   - Ces trois points viennent d'un extrait de la foire aux questions vu dans la recherche. La page elle-même a renvoyé une erreur 403 à l'ouverture.
   - La facturation prend d'abord le solde offert, puis le solde rechargé (page des prix).
3. **Création de la clé :** page des clés, https://platform.deepseek.com/api_keys. Puis placer la clé dans la variable d'environnement `DEEPSEEK_API_KEY` (première page de la documentation).
4. **Plafond de dépense :** aucune option de plafond n'est documentée.
   - Le solde prépayé borne de fait la dépense : quand il est épuisé, l'API répond par l'erreur 402 « Insufficient Balance ».
   - On ne recharge donc que le montant du devis.
   - Le solde se lit par `GET https://api.deepseek.com/user/balance` (vu dans la recherche, page non ouverte directement).
5. **Avant tout appel :** la politique de confidentialité indique que le refus de l'entraînement se fait par courriel à privacy@deepseek.com. Ce courriel est un contact externe : Lazar l'envoie.

Sources :
- https://api-docs.deepseek.com/
- https://api-docs.deepseek.com/quick_start/error_codes
- https://api-docs.deepseek.com/quick_start/pricing
- https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html
