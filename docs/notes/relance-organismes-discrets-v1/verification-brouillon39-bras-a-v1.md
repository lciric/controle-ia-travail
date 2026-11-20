# Vérification du brouillon 39 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 38. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon39.md`, `4425e9e922044a749a6d1357f2fadbc9e212d8f4843e954b704792840ae23b61`, 2 364 lignes.
- **Pièces jointes, compagnons vérifiés** (`python -m controle_ia.scellement verifier`) :
  - la note du rédacteur, `3dec1b9a4d03…` ;
  - le brouillon 38, `16545485b0ff…` ;
  - la vérification du brouillon 38, `50229101836f…` ;
  - la pièce des mots de Lazar du 20 novembre, `2845ca37e793…` ;
  - les pièces sans interne citées par le brouillon : `lecture-habilitee-sans-interne-v8-v1.md` (`91b4bcd35690…`), `reponses-sans-interne-demandes-v8-v3.md` (`6c0f71f6a6b0…`), `verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md` (`cb23f4efaec9…`) ;
  - pour les contrôles : le brouillon 20 (`b076e3f942d6…`) et la pièce des demandes au développeur en version 8 (`ba81227fcea1…`).
  - **Le journal de la relance n'a pas de compagnon** : la vérification s'arrête sur « empreinte compagnon absente ». Je l'ai lu sans empreinte vérifiée, pour le contexte seulement (`ebcbd1440a84…`, calculée par moi).
- **Méthode** :
  - comparaison des brouillons 38 et 39 par programme, ligne par ligne puis mot par mot (26 blocs changés) ;
  - comparaison section par section, sous les 54 titres ;
  - lecture des passages touchés, et des trois pièces sans interne en entier ;
  - recalcul des empreintes de la table d'en-tête, **hors lignes cloisonnées et hors modules de code** ;
  - validateur `problemes()` lancé, sans ouvrir son module ;
  - registre des GO lu par `git show origin/main:registres/go.md`, référence locale `75d8c76a`, sans appel réseau.

## Verdict : **engageable après corrections**

- Les trois corrections et les neuf mineurs de la vérification du brouillon 38 sont traités, ni plus ni moins, à une demi-réserve près (m-1).
- **Aucune règle de jugement, aucun seuil, aucune issue, aucune prédiction ne change.** Les gardes neuves de 8.7 sont des procédures.
- Les contrôles de la note concordent tous, refaits par programme.
- **Une correction**, connue de la session et hors de la portée du rédacteur (texte écrit avant le mot de Lazar sur Carbon) :
  - **C-1** : le texte nomme encore `gemini-4-carbon` comme second lecteur, alors que GO-2026-11-20-31 l'en retire. Il nomme aussi `gpt-6.2-astra` comme juge des deux ancres, rôle que la lecture de la relance (OD-230) touche, sans confirmation de Lazar. Le brouillon 40 doit porter ce changement, aux endroits de la partie 5. Je ne propose aucune règle de remplacement.
- **Six mineurs** :
  - **m-1** : « posée à Lazar avec cette réponse » n'est pas dans la pièce ;
  - **m-2** : en 8.4, la ligne du point 20 garde un arrêt « refusé » sans dire quel programme le refuse ;
  - **m-3** : « qui confirme quoi » n'est pas complet ;
  - **m-4** : l'objet de l'attestation de la version 7 à la version 10 est à préciser auprès du lecteur habilité ;
  - **m-5** : en 13.2, la contre-lecture de la configuration ne renvoie pas à 8.7 ;
  - **m-6** : le compte des lignes cloisonnées de la note est à préciser (14 ou 15).

## 1. Traitement de la vérification du brouillon 38

| point | où, au brouillon 39 | jugement |
|---|---|---|
| **C-1** — attestation de la version 7 à la version 10 | 13.1, case du module, ligne 1404, reste (a) : « elle est à écrire à part, par le côté habilité, sur la version 10 ; rien n'en tient lieu, sauf si le lecteur habilité écrit qu'une autre pièce suffit » | **fidèle.** La substitution retirée (« l'épreuve par retrait et la notice […] en tiennent lieu si la session principale l'écrit ») n'apparaît plus. C'est ce que disent la lecture habilitée, demande 24 (a), et la vérification de la version 10, ligne 15. Voir m-4 sur l'objet de l'attestation. |
| **C-2** — refus de 8.4 que le code arrêté ne fait pas | Conventions, ligne 261 : « **aucun programme ne la refuse** », renvoi à 8.7. En 8.4, ligne 1066 (point 19) : le refus d'un arrêt levé pour l'intervalle impossible devient « n'est pas éprouvé ici […] garde de procédure (8.7) ». En 8.4, ligne 1070 (point 20) : la configuration « module corrigé » ou « en attente » est retirée. En 8.7, ligne 1160 : garde neuve. | **fidèle.** Les cinq valeurs de 8.7 sont celles des conventions. La garde a un porteur (la session de relance), deux traces (la configuration scellée, le manifeste de course) et deux vérificateurs (le contre-lecteur de la configuration et celui du manifeste). Reste la ligne du point 20 (m-2). |
| **C-3** — formules du sous-échantillon en 7.4 et 7.7 | 7.4, ligne 972 : « Le juge lit toutes les actions (case « lecture du juge d'une autre lignée », 13.1). » La suite « faute de puissance… » est retirée. 7.4, ligne 978 (ligne C4) : « sur toutes les actions » seul. 7.7, ligne 1003 (ligne C6) : crochet retiré. | **fidèle**, aux trois endroits. Rien n'est ajouté que la ponctuation de la parenthèse. |
| m-1 — mots du 20 novembre cités par leur pièce | 14 mentions de la pièce, sur les lignes 3, 174, 261, 804, 850, 1349, 1391, 1395, 2317, 2332. Le chemin du journal n'apparaît plus (11 fois au 38). OD-217 n'apparaît plus. OD-220 ne reste qu'une fois, ligne 5, dans l'histoire de ce que le brouillon 38 a ouvert. | **presque fidèle.** « Réexpliquée » est bien repris de la pièce (point 1). Mais trois phrases écrivent aussi que la décision a été « **posée à Lazar avec la réponse du développeur** » : 6.9, ligne 804 ; 12, ligne 1349 ; 13.1, ligne 1391. La pièce ne le dit pas (m-1). |
| m-2 — `effectifs` | 13.1, ligne 1404 : « fait d'entiers, ou `null` quand un pli n'a aucune unité » | **fidèle** (réponses v3, demande 14) |
| m-3 — une valeur par dose | 13.1, ligne 1404 : « une seule valeur par dose […] un nombre, ou `null` au cas B, où l'aire n'est pas calculable » | **fidèle** (réponses v3, demande 17) |
| m-4 — qui confirme quoi | 13.1, ligne 1404, « **Qui confirme quoi** » | **fidèle dans son principe, incomplet dans sa liste** (m-3 ci-dessous) |
| m-5 — clé `lec6` | 6.2, ligne 660 : « elle n'est tirée par aucun programme » | **fidèle**. Le refus non éprouvé disparaît. |
| m-6 — positions du juge dans une paire | 6.9, ligne 801 : « toutes les positions des deux épisodes sont offertes à la lecture, et une action non appliquée y est non lue (6.10) » | **fidèle.** Le renvoi à 6.10 est juste : la règle est en 6.10, ligne 862. **Ma vérification du 38 disait « 6.11 » à tort.** |
| m-7 — stratification du sous-échantillon | 13.2, ligne 1412 : « sans objet depuis qu'il lit toutes les actions » | **fidèle.** La section 12 n'est pas touchée. |
| m-8 — demande 25 et table B | 14.51, ligne 2346 : avis versé. 8.7, ligne 1161 : garde neuve sur la table B. | **fidèle** à la lecture habilitée, demande 25 (a) et (b), et demande 22, ligne 4. Le versement est dit « avis » ; aucune règle n'en dépend. |
| m-9 — anomalie bornée | 6.9, ligne 814 : « Dans la lecture commune des cinq moniteurs, plus aucun cas n'est tenu pour une anomalie […] — l'anomalie de l'audit de symétrie, ligne A11, demeure — » | **fidèle** |

**Ni plus ni moins.** Hors de ces douze points, le brouillon ne change que :
- le titre et le statut ;
- l'en-tête (rédacteur, heures, registre relu, note) ;
- quatre lignes neuves de la table d'en-tête ;
- la mention de 14.51 dans la numérotation (ligne 246) ;
- la section 14.51 ;
- la ligne de contre-lecture.

## 2. Contrôles de la note, refaits par programme

| contrôle (note, partie 2) | mon résultat | concorde ? |
|---|---|---|
| 7.1 à 7.8 : 3 lignes changées sur 102 | Lignes 911 à 1012 : 102. Changées : 972 (7.4), 978 (7.4, C4), 1003 (7.7, C6). Retraits seuls, plus « ( » et « , » dans la parenthèse de la ligne 972. 7.1, 7.2, 7.3, 7.5, 7.6 et 7.8 identiques. | **oui** |
| section 12 : 1 ligne sur 172 | 1 ligne (1349, marque du point 19). Les 171 autres sont identiques, fiches comprises. | **oui** |
| section 10 identique | identique | **oui** |
| hypothèse au seuil ; 6.3 à 6.8 ; 8.1 à 8.3 ; 8.5 et 8.6 ; 9 et 11 identiques | Tous identiques. Le sont aussi 0 à 4, 3.1 à 3.5, 6.1, 6.11, 6.12 et le titre de 13. | **oui** |
| sections changées | 6.2 (1), 6.9 (3), 6.10 (1), 7.4 (2), 7.7 (1), 8.4 (2), 8.7 (2 lignes neuves), 12 (1), 13.1 (3), 13.2 (1), 14 (14.51 neuve et la ligne de 14.50), contre-lecture (1) | conforme à la partie 1 de la note |
| titres | 54 ; seul le titre de niveau 1 change (« 38 » devient « 39 ») | **oui** |
| consignes figées 3.2 et 3.3 | Mesurées selon la règle de 13.1 (lignes entre les bornes du bloc, jointes par LF, sans saut de ligne final) : `98a9bd34d280…` et `ecf590eae0c0…`. Égales à celles du brouillon 20 et à celles que 13.1 inscrit. | **oui** |
| marques des cases | 5 lignes, toutes en 13.1 : 1391 (nœuds), 1397 (entropie), 1402 (renvoi de la base), 1403 (commit du code), 1404 (module). Six occurrences de la chaîne dans ces cinq lignes, comme au 38. | **oui** |
| validateur `problemes()` | 38 et 39 : les deux mêmes problèmes attendus (marque hors des sections exigées ; contre-lecture 10 sans empreintes) | **oui** |
| citations du brouillon 38 | Mon compte porte sur les textes entre guillemets français : 1 425 occurrences, 541 distinctes (la note compte 1 396 par une autre méthode). **2 absentes**, les mêmes que celles de la note : « sur un sous-échantillon de 2 560 actions » et la phrase permise de C6, récrite sans son crochet. Quatre citations neuves : la C6 récrite, et trois libellés de 14.51. | **oui** |
| mots du 20 novembre | Plus aucune citation par le journal seul | **oui** (voir m-1 pour le fond) |
| table d'en-tête : 212 recalculées, 14 sautées | 226 lignes à empreinte. **187 recalculées, toutes égales**, dont les 4 neuves. 24 lignes de code non recalculées (consigne : aucun module ouvert). **15 lignes cloisonnées sautées**, aucune empreinte prise : les 14 de la demande 23, plus la ligne 62, une pièce sans interne rangée sous `docs/notes/bras-a-moniteurs-v1/`. | **en partie** : 187 + 24 + 15 = 226 = 212 + 14. Le rédacteur a donc recalculé la ligne 62, que mon cloisonnement range parmi les lignes interdites (m-6). |
| registre relu | voir partie 4 | **oui** |

## 3. Règles

**Aucune règle de jugement, aucun seuil, aucune issue, aucune prédiction ne change.**
- L'hypothèse, la prédiction chiffrée, la métrique et le seuil sont identiques octet pour octet.
- 7.2, 7.3, 7.5 et 7.6 (tables A et B, issues, audit) sont identiques. En 7.4 et 7.7, ne reste que la branche déjà retenue en 6.10 au brouillon 38 : c'est le report d'un choix, non une règle.
- 6.9 : trois reformulations exactes. L'unité de la permutation et la règle de la valeur p ne changent pas.
- 6.2 : un énoncé trop fort (« refusé ») devient exact. Aucune garde n'est perdue, car aucune n'existait.

**Les gardes neuves sont des procédures, non des règles.**

| garde | nature | pourquoi |
|---|---|---|
| 8.7, ligne 1160 : la configuration ne porte que la valeur que le texte garde pour chacun des cinq choix | **procédure** | Elle ne change ni les valeurs ni ce que chaque valeur fait lire. Elle dit qui empêche une configuration hors du texte : la session de relance, le contre-lecteur de la configuration et le contre-lecteur du manifeste. Les conventions disaient déjà qu'une valeur écartée est « un écart au préenregistrement ». |
| 8.4, ligne 1066 : le refus devient « non éprouvé ici », renvoyé à 8.7 | **procédure** | Le texte ne prétend plus qu'un programme refuse ce cas. Sous la valeur gardée, l'issue « repère » ou « indécis » est inchangée. |
| 8.4, ligne 1070 : la configuration « module corrigé » ou « en attente » est retirée des refus | **procédure** | même raison |
| 8.7, ligne 1161 : personne n'ouvre la table B du côté habilité | **procédure** | La lecture habilitée, demande 22, ligne 4, le dit en ces termes. Le texte n'en fait dépendre aucune lecture. |

## 4. Registre (référence locale `75d8c76a`, sans appel réseau)

- **GO-2026-11-20-19** : citée correctement, **oui**. Elle renvoie seule à `mot-de-lazar-go-recos-bras-a-2026-11-19-v1.md` (`1fcfae81…`), comme l'écrivent 13.1 (ligne 1391) et la section 12.
- **GO-2026-11-20-20** : citée correctement, **oui**. Elle renvoie à `mot-de-lazar-a-a-bras-a-2026-11-20-v1.md` (`ae279572…`) et à son erratum 1 (`964027bc…`), comme l'écrit 13.1.
- **Une ligne nomme-t-elle GO-2026-11-19-97 ?** **Non**, hors sa propre ligne (ligne 530 du registre).
- Les deux mots du 20 novembre n'ont pas encore de ligne : aucune ligne ne cite la pièce `2845ca37…`. C'est ce que disent le brouillon (ligne 8) et la note.
- Le brouillon dit les lignes -19 et -20 « lues au commit `462b8e5e6` », et le registre relu au commit `c1725862f`. Ces deux commits sont absents de mon dépôt local. Je ne peux donc comparer qu'à `75d8c76a`, où les deux lignes disent ce que le texte leur fait dire.

## 5. Ce que le brouillon 39 ne porte pas encore : Carbon lecteur, Astra juge des ancres

**Contexte** :
- GO-2026-11-20-31 : `gemini-4-carbon` cesse d'être l'un des deux lecteurs de l'oracle de couverture ; le remplaçant est à choisir par Lazar.
- OD-230 : Lazar dit « prends le meilleur des deux sur les bancs d'essais correspondants », entre Mistral et DeepSeek. La relance lit que l'autre modèle jugerait les ancres à la place d'Astra, mais Lazar ne l'a pas confirmé.

Je ne propose aucune règle. Numéros de ligne du brouillon 39, trouvés par recherche de « carbon », « Carbon » et « Astra », puis de « Google », « OpenAI » et « lecteur 2 ».

**A. Carbon nommé comme second lecteur (ou son essai, sa clé, son coût)**

| section | ligne | ce que l'endroit commande |
|---|---|---|
| conventions | 248 | **définition** : « le lecteur 2 est `gemini-4-carbon` », partout dans le texte |
| 3.4 Qui lit | 474 | **choix des lecteurs** : un modèle Claude et `gemini-4-carbon` (famille Google) ; trois familles distinctes hors Llama et Qwen ; GO-2026-11-19-13 |
| 3.4 | 478 | **réglages** de `gemini-4-carbon` (température 0, budget de réflexion, sortie maximale, appels synchrones) |
| 3.4 | 480 | **essai de mesure** : file Carbon, GO-2026-11-19-35, plafond 6 USD |
| 3.4 | 483 | **essai de mesure** : `gemini-4-carbon` aux budgets 1 024 et 2 048 ; 176 appels en tout |
| 3.4 | 484 | **règle de choix** scellée `regle-de-choix-claude-carbon-v1.json` (projection du lecteur 1) |
| 3.4 | 486 (2 fois) | **règle de choix** (« `gemini-4-carbon` au budget 1 024 s'il tient, sinon 2 048, sinon nœud ») et **choix retenu par Lazar** (budget 1 024, sortie maximale 8 192) |
| 6.2 Graines | 636 | **clés de graine** : `{lecteur}` vaut `carbon` pour le lecteur 2 (entropie, R9) |
| 6.11 Dépense | 886 | **essai** : file Carbon, 48 appels, plafond 6 USD |
| 6.11 | 889 | **projection du devis** par la règle `…claude-carbon-v1.json` : lecteur 2, ≈ 97,0 USD |
| 13 (avant 13.1) | 1379 | **lignes de calcul de l'essai** : GO-2026-11-19-35 (Carbon, 6 USD) |
| 13 | 1381 | **nœuds tranchés** : budget de réflexion de `gemini-4-carbon` (case « lecteurs et juge des ancres ») |
| 13.1, familles | 1393 | **fiche des familles** : « les trois familles retenues (Claude, Google, OpenAI) sont distinctes » |
| 13.1, lecteurs et juge des ancres | 1394 (5 fois) | **case remplie** : lecteur 2 `gemini-4-carbon`, budget 1 024, 24 conformes sur 24, rapport de la file Carbon ; choix de Lazar sur ce réglage et sur la sortie maximale |
| en-tête | 3, 8, 54, 56 | **histoire et pièces** : brouillon 16 ; lignes de GO de l'essai ; règle de choix et rapport de la file Carbon dans la table d'en-tête |
| 14 | 1620, 1698, 1977, 1982 | **histoire** des traitements (14.x, 14.28) |

**B. Astra nommé comme juge des deux ancres**

| section | ligne | ce que l'endroit commande |
|---|---|---|
| 3.4 Qui lit | 474 | **choix du juge** : `gpt-6.2-astra` (famille OpenAI), un item par appel ; GO-2026-11-19-11 et -13 |
| 3.4 | 478 | **réglages** de `gpt-6.2-astra` |
| 3.4 | 480 | **essai** : file GPT (juge des ancres), GO-2026-11-19-36, 2,50 USD (Astra n'est pas nommé, mais c'est sa file) |
| 3.4 | 483 | **essai** : `gpt-6.2-astra`, 8 appels |
| 6.3 Ordre d'exécution | 688 | **étape des ancres** : juge `gpt-6.2-astra`, écart déclaré à « ancre humaine » |
| 6.11 Dépense | 885 | **dépense** : ancres jugées par `gpt-6.2-astra`, 152 appels au plus |
| 6.11 | 886 | **essai** : file GPT, 8 appels |
| 12, nœud 1 | 1208 | **fiche tranchée** : γ, `gpt-6.2-astra` juge les deux ancres (section 12 : fiche à ne pas réécrire, la marque seule peut changer) |
| 13.1, familles | 1393 | **fiche des familles** : famille OpenAI |
| 13.1, lecteurs et juge des ancres | 1394 (2 fois) | **case remplie** : juge des ancres `gpt-6.2-astra`, sans température, 8 192, 8 conformes sur 8, rapport de la file GPT |
| 14 | 1548, 1620, 1983 | **histoire** |

**Remarques sans règle** :
- Les sections 3.2 et 3.3 (consignes figées) ne nomment aucun des deux modèles.
- Les tables de 7 parlent de « lecteur 1 » et « lecteur 2 » sans nom de modèle.
- La règle de choix et les rapports de l'essai sont des pièces scellées au nom de Carbon. Les remplacer relève de l'essai, du devis et des lignes de GO (3.4, 6.11, 13.2), non du texte seul.
- La case « familles » (ligne 1393) et 3.4 (ligne 474) devront dire la famille du remplaçant. La liste des familles exclues est cloisonnée : je ne l'ai pas ouverte.

## 6. Corrections et mineurs

**Correction :**
- **C-1.** Porter GO-2026-11-20-31 aux endroits de la partie 5 (A), puis, selon la confirmation de Lazar, aux endroits de la partie 5 (B). C'est un nœud de Lazar : le remplaçant n'est pas choisi, et son rôle de juge des ancres n'est pas confirmé. Brouillon 40.

**Mineurs :**
- **m-1.** 6.9 (ligne 804), marque du point 19 en 12 (ligne 1349) et 13.1 (ligne 1391) écrivent que la décision a été « posée à Lazar avec la réponse du développeur ». La pièce `2845ca37…` dit seulement que Lazar n'a pas compris la décision et que la session la lui a réexpliquée. Il faut soit retirer « posée avec cette réponse », soit citer la pièce qui le dit. Dans la ligne 804, « comme le dit la pièce de ses mots » ne doit couvrir que « réexpliquée ».
- **m-2.** 8.4, ligne 1070 (point 20) : « un arrêt de la lecture levé pour ce motif » reste « refusé ». Au point 19, le même refus a été renvoyé à 8.7. Il faut dire quel programme refuse cet arrêt sous la valeur gardée, et par quel essai, ou le traiter comme au point 19. Je ne peux pas trancher sans le code.
- **m-3.** 13.1, « qui confirme quoi ». La vérification de la version 10 confirme aussi les réponses 2 (forme du cas E) et 3 (au cas C, l'aire et les aires des plis sont rendues), ainsi que le schéma de permutation (réponse 1). La liste ne les nomme pas, sauf à les lire sous « la version et sa forme ». La pleine précision des nombres (réponses 5 et 32) ne figure dans aucune des deux listes : c'est la parole du développeur, éprouvée par l'artefact de l'épreuve de forme.
- **m-4.** Reste (a). Selon la lecture habilitée, demande 24 (a), l'échange dans chaque paire est du code neuf depuis la version 7. Une attestation qu'« aucun calcul de moniteur ne change » de la version 7 à la version 10 ne peut donc pas valoir pour les valeurs p. Par ailleurs, ce que l'attestation devait couvrir, d'après l'histoire de la case (point 2), est l'épreuve par retrait et la notice ; elles sont refaites pour la version 10 (réponse 16, confirmée). Il faut demander au lecteur habilité ce que l'attestation doit porter, ou s'il écrit qu'une autre pièce suffit. La porte est déjà écrite. Aucune règle ne change.
- **m-5.** 13.2, ligne de la configuration (ligne 1413) : la contre-lecture « par un agent d'un autre modèle » ne renvoie pas à la tâche neuve de 8.7, confronter les cinq choix. Ajouter le renvoi (réserve 1 de la note).
- **m-6.** Note, partie 2 : la ligne 62 de l'en-tête vise une pièce sans interne, rangée sous `docs/notes/bras-a-moniteurs-v1/`. Le rédacteur en a recalculé l'empreinte ; pour moi, elle est cloisonnée. Dire, dans la prochaine note, pour qui cette ligne est permise.

## 7. Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon39.md` : par différence et par passages.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon38.md` : par différence et par programme.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md` : par programme (blocs de 3.2 et 3.3).
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon39-note-v1.md` : en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-brouillon38-bras-a-v1.md` : en entier.
- `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md` : en entier.
- `docs/notes/bras-a-sans-interne-v1/lecture-habilitee-sans-interne-v8-v1.md`, `reponses-sans-interne-demandes-v8-v3.md`, `verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md` : en entier. Pour `reponses-sans-interne-demandes-v8-v1.md`, compagnon vérifié seulement.
- `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v8.md` : table des numéros et demandes 1 à 3 (pièce citée par le brouillon).
- `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` : entrées OD-222 à OD-230.
- `registres/go.md` par `git show origin/main:` (référence locale) : lignes 530, 550 à 552 et 562.
- Fichiers de la table d'en-tête : 187 lus en octets pour l'empreinte seulement, hors code et hors cloisonnement.
- `controle_ia.prereg.problemes` et `controle_ia.scellement` : exécutés, non lus (j'ai seulement affiché la signature de `problemes`).

## 8. Écarts

- **Aucun franchissement du cloisonnement.** Je n'ai pris l'empreinte d'aucune des 15 lignes cloisonnées et n'ai ouvert aucun module de code. Rien sous `bases/`, `sondes/`, `t07*/` ni T0.8 ; aucun interne de moniteur.
- **Deux débords mineurs, déclarés :**
  - une recherche dans le journal a affiché les 80 premiers signes des lignes OD-217 à OD-221 et OD-231 (identifiant, heure, début du titre), hors de la plage permise. Je n'en ai rien tiré ;
  - j'ai lu en entier la pièce sans interne dont le nom contient « autres-moniteurs-v10 ». Elle est sous le dossier permis et citée par le brouillon. Je l'ai jugée hors du motif `autres_moniteurs_v*`, qui vise les modules.
- Aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. `registres/`, `.claude/` et le journal ne sont pas touchés. Un seul fichier écrit, celui-ci : ni scellé ni committé.
