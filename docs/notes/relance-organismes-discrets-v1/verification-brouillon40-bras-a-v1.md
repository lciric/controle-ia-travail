# Vérification du brouillon 40 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je juge ; je ne corrige rien. Ni scellé ni committé.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon40.md`, `b4670b88b8abb73b2a40c61fb5d1cf17bb513b52b710ba9b06b22b0e4304db89`, 2 414 lignes.
- **Pièces, compagnons vérifiés** (`python -m controle_ia.scellement verifier`, tous « OK ») :
  - la note du rédacteur, `preenregistrement-v2-brouillon40-note-v1.md`, `60987d89bba8…` (153 lignes) ;
  - le brouillon 39, `4425e9e92204…` (2 364 lignes) ;
  - la vérification du brouillon 39, `df82b2f3fe51…` ;
  - la pièce des mots de Lazar sur le second lecteur et le juge des ancres, `8189dcec0f83…` ;
  - le devis de l'essai de mesure, `devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, `533ad5b15e6d…` (section 7) ;
  - deux pièces sans interne : `verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md` (`cb23f4efaec9…`) et `lecture-habilitee-sans-interne-v8-v1.md` (`91b4bcd35690…`).
- **Lus par `git show origin/main:`**, référence locale `3c2b1436`, sans appel réseau :
  - `registres/go.md` (empreinte de cette lecture : `a13f3b1d6599…`), lignes 455, 530, 550, 551, 562, 569 et 574 ;
  - la recherche de la session principale, `lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md` : empreinte recalculée `f7090b5d52b6…`, égale à son compagnon et à la ligne 179 du texte.
- **Le journal de la relance n'a pas de compagnon** (`7bf92aff1656…`, calculée par moi) : lu pour le contexte, lignes 247 à 253 (OD-228 à OD-234).
- **Méthode** :
  - différence des brouillons 39 et 40 par programme, ligne par ligne puis mot par mot ;
  - comparaison section par section, sous les 54 titres ;
  - lecture entière du bloc neuf de 3.4 (lignes 494 à 512) et des lignes changées ;
  - empreintes des consignes figées, des marques, de la table d'en-tête, et validateur `problemes()`, par programme ;
  - code : les seules lignes citées (question 5).

## Verdict : **engageable après corrections**

- Le remplacement de Carbon et d'Astra est porté partout où il le faut, et seulement là. Les six mineurs du 39 sont traités.
- **Aucune règle de jugement, aucun seuil, aucune prédiction ne change dans le texte des sections gelées.** Les contrôles de la note concordent, refaits par programme.
- **Mais l'admission d'un alias non figé étend, hors des sections gelées, deux lignes gelées** (A10, A12) à un cas qu'elles ne nomment pas. C'est la correction C-1.

**Corrections :**
- **C-1. Version figée ou alias.** 3.4, ligne 484 (inchangée) : « version figée et inscrite ». Ligne A12 (7.2, gelée, ligne 970) : « version **figée** d'un lecteur retirée ». Le bloc neuf (ligne 500) admet un alias qui « ne fige rien » et range son changement sous 8.2, A10, A12 et A17. C'est une contradiction interne, et une extension de lignes gelées à un cas neuf. Le risque est réel : la recherche dit que l'alias proposé a changé deux fois en deux mois ; un changement pendant le lot décisif donne A10 (« rien n'est conclu ») ; entre les épreuves et le lot décisif, A12 (le bras s'arrête). Admettre un alias non figé est donc un choix de Lazar. La question 1 ne le pose pas comme tel. Il faut soit exiger un identifiant figé (DeepSeek n'est alors admis qu'avec un tel identifiant), soit poser ce choix à Lazar, avec ses conséquences, et le dire en 3.4, en 8.2 et en 14.52.
- **C-2. Ce que l'essai comparatif envoie n'est pas fixé, alors que le texte dit « sans choix de la session »** (ligne 484). Ne sont fixés ni la sortie maximale envoyée à l'essai, qui décide du « sans fin par sortie maximale » du point 1, ni les compteurs de jetons de chaque service pour `C` et pour le point 7. Le devis, section 7.3, point 7, dit « réflexion comprise » ; le texte, lignes 508 et 1421, ne le reprend pas. Ce sont des choix d'avant lecture, non d'après. Il faut les fixer dans le texte, ou dire qu'ils sont fixés au devis, avant tout envoi, et retirer « sans choix de la session ».
- **C-3. « Non joignable » est sans retour pour une cause logistique.** Point 1 (ligne 502) : accès refusé, ou premier envoi et sa reprise sans code 200, et le candidat « ne tient pas ». Point 2 (ligne 503) : une file n'est jouée qu'une fois. Une clé fausse ou non approvisionnée, une limite de débit ou une panne au départ désigneraient donc l'autre modèle sans comparaison. Ce n'est pas « le meilleur des deux ». Il faut une vérification de chaque clé avant sa file, comme pour la clé Claude (GO-2026-11-19-32), dont l'échec n'est pas un « ne tient pas » mais une file non partie. L'admission doit aussi nommer les deux clés (GO-2026-11-20-38 : « Lazar crée la clé » ; GO-2026-11-20-43 : « deux clés, une chez chaque fournisseur »).

**Mineurs :**
- **m-1.** 8.4, ligne 1096 : « un arrêt de la lecture levé pour ce motif est ce que le programme fait sous une autre valeur de ce choix ». C'est un fait sur le code, que le rédacteur n'a pas vérifié (sa réserve 4). Dire seulement que cet arrêt n'est pas éprouvé ici, et renvoyer à 8.7, sans dire ce que fait le programme.
- **m-2.** 13.1, case du module, ligne 1431 : « la question lui est posée ». Elle n'est pas encore posée : la note la range parmi les tâches de la session principale (partie 8). Écrire « est à poser ».
- **m-3.** En-tête, ligne 8 : GO-2026-11-20-38 est résumée sans « sur les bancs d'essais publics qui correspondent à la tâche du lecteur ». GO-2026-11-20-43 est résumée sans « deux clés ». La note (partie 3) écrit que GO-2026-11-20-43 précise GO-2026-11-20-38 « dans ce sens » ; la ligne dit seulement « Précise GO-2026-11-20-38 : deux clés ». C'est la phrase principale de GO-2026-11-20-43 qui fixe l'essai comparatif. Citer les deux lignes telles qu'elles sont.
- **m-4.** Point 3 (c), ligne 504 : « le tarif le plus haut quand un service en publie plusieurs selon l'heure » ne couvre pas le point d'accès européen de Mistral (prix courant fois 1,1, selon la recherche). Écrire « le tarif de la voie d'accès retenue, et le plus haut selon l'heure ».
- **m-5.** Les « partis pris » (ligne 511) ne nomment pas l'ordre fixe « Mistral d'abord ». C'est un choix du rédacteur, même s'il suit l'ordre des mots de Lazar.
- **m-6.** Questions de la note : la question 2 ne porte que sur DeepSeek, alors que l'admission (ii) exige un mot de Lazar pour chaque fournisseur ; la question 3 ne demande pas de confirmer le banc lui-même. La pièce des mots dit pourtant : « les « bancs d'essais correspondants » sont à fixer dans le texte, puis à confirmer ». Voir la question 7.

## 1. Fidélité aux mots de Lazar

**Le remplacement est porté partout où il le faut.**

| endroit (brouillon 40) | ce qui est écrit | jugement |
|---|---|---|
| conventions, ligne 254 | lecteur 2 : celui des deux candidats que désigne la règle de 3.4 ; le juge est l'autre | fidèle |
| 3.4, ligne 480 | second lecteur à désigner entre Mistral « le chonk » et DeepSeek ; juge des ancres : celui des deux qui n'est pas désigné ; Carbon et Astra ne lisent ni ne jugent plus | fidèle à la pièce `8189dcec…` et à GO-2026-11-20-43 |
| 3.4, ligne 484 | réglages : effort le plus haut (GO-2026-11-20-38) | fidèle ; voir C-1 et C-2 |
| 3.4, lignes 494 à 512 | l'essai comparatif et sa règle | voir plus bas |
| 6.2, ligne 661 | clé `carbon` gardée | question 5 |
| 6.3 (d), ligne 713 | juge désigné en 3.4 | fidèle ; seul le nom change |
| 6.11, lignes 910, 912, 915 | juge désigné ; ligne neuve de 48 appels ; la projection de 97,0 USD tombe | fidèle ; aucune dépense |
| 12, nœud 1, ligne 1234 | marque ajoutée en fin de ligne ; fiche et option γ mot pour mot | fidèle à la règle de la section 12 |
| 13, lignes 1407 et 1408 | ce qui manque de Lazar ; ordre de l'essai | fidèle |
| 13.1, lignes 1420 et 1421 | familles Claude, Mistral, DeepSeek ; case remplie pour le lecteur 1 seulement | fidèle |
| 13.2, lignes 1438, 1441, 1445 | devis à trois modèles ; version à la course ; dossier de l'essai | fidèle ; voir C-1 |

**Et seulement là.** Il reste 51 mentions de Carbon ou d'Astra, sur 32 lignes : 3, 8, 54, 56, 179, 254, 480, 485, 486, 489, 490, 492, 495, 507, 661, 713, 910, 911, 915, 1234, 1405, 1407, 1421, 1576, 1648, 1726, 2005, 2010, 2011, 2382, 2383, 2391. Le compte est celui de la note. Chacune est de l'histoire (en-tête, section 14, récit de l'essai joué, lignes de calcul passées), une phrase qui dit qu'ils ne lisent plus, ou la fiche gelée du nœud 1. Aucune ne les fait lire ou juger.
- Les gardes de famille restent compatibles : 8.4, ligne 1139, refuse un juge de la famille d'un lecteur ; Mistral et DeepSeek sont deux familles. L'agent est de la famille Llama (ligne 879), exclue.
- Les tables de 7 ne nomment aucun modèle.

**La règle de désignation (3.4, lignes 501 à 509) est-elle fermée ?**

| cas | écrit | fermé ? |
|---|---|---|
| critère « tient » | celui du devis, section 7.2 (vérifié : identique), plus une seule chaîne de version et la même version affichée avant et après la file | oui, à C-2 près (sortie maximale envoyée) |
| égalités | étayées, puis forme conforme, puis coût au centime, puis Mistral | oui ; voir m-4 et m-5 |
| un seul tient | il lit ; juge non désigné : nœud | oui |
| aucun ne tient | nœud | oui |
| non joignable | ne tient pas | oui, mais voir C-3 |
| version qui change | à l'essai : ne tient pas ; à la course : 8.2 | oui à l'essai ; voir C-1 pour la course |
| une file jouée une fois | point 2 | oui |
| après lecture | point 8 : par programme, sur les compteurs ; aucun changement après le premier envoi | oui |

**Laisse-t-elle un choix à la session après lecture ? Non.**
- Tout ce qui reste ouvert se fixe avant le premier envoi : sortie maximale envoyée, compteurs, tarifs, plafonds (C-2).
- Un seul point demande un jugement pendant l'essai : la « version affichée » lue sur une page des mises à jour (ligne 500). Si c'est la session qui la lit, c'est une interprétation. Il faut dire quel programme la relève, et sur quel champ (C-1).

**« Un seul tient → juge non désigné, nœud de Lazar » (réserve 2 du rédacteur).**
- À la lettre, les mots disent : « le modèle des deux qui n'est pas retenu comme second lecteur devient juge des deux ancres » (pièce `8189dcec…`, point 2). Ils ne prévoient pas le cas d'un modèle qui ne tient pas.
- La règle **ajoute** un arrêt. Elle ne donne aucun choix à la session et ne retire rien à Lazar : le nœud lui rend la décision. Elle suit l'interdit « changer de modèle sans GO » (CLAUDE.md). Le cas compte : un modèle non admis ou non joignable ne peut pas juger ; un modèle sous 22 conformes sur 24 rendrait des jugements sans forme.
- **Jugement : ajout prudent, compatible avec les mots, à déclarer comme tel.** Le texte le déclare en partie (point 6) ; 14.52 le range sous « règle de désignation ». Le poser à Lazar d'avance est permis, non nécessaire : le défaut est déjà le nœud.

## 2. Règles

**Contrôles de la note, refaits par programme :**

| contrôle | mon résultat | concorde ? |
|---|---|---|
| hypothèse, prédiction, métrique, seuil | identiques octet pour octet | oui |
| 7.1 à 7.8 | identiques | oui |
| section 10 | identique | oui |
| section 12 | 2 lignes changées sur 171 (sans le titre) : 1234 (marque ajoutée en fin de ligne, fiche intacte) et 1375 (formule de m-1) | oui |
| 6.3 | 1 ligne (713) : le nom du juge, et « (famille OpenAI) » retiré | oui |
| 6.9 | 1 ligne (829) : la formule de m-1 | oui |
| 8.4 | 1 ligne (1096) : m-2 | oui |
| autres sections | en-tête et conventions (9 lignes changées, 6 neuves) ; 3.4 (3 changées, 19 neuves) ; 6.2 (1) ; 6.11 (2 et 1 neuve) ; préambule de 13 (1, devenue 2) ; 13.1 (4) ; 13.2 (3 et 1 neuve) ; 14 (22 neuves) ; contre-lecture (1). 6.1, 6.4 à 6.8, 6.10, 6.12, 8.1 à 8.3, 8.5 à 8.7, 9, 11 : identiques | oui |
| titres | 54 et 54 ; seul le titre de niveau 1 change | oui |
| consignes figées | blocs de 3.2 (lignes 381 à 406) et de 3.3 (lignes 428 à 462), règle de 13.1 : `98a9bd34d280…` et `ecf590eae0c0…`, égales au brouillon 39 et à 13.1 | oui |
| marques des cases | 7 lignes, toutes en 13.1 (1418, 1420, 1421, 1424, 1429, 1430, 1431), 8 occurrences | oui |
| validateur `problemes()` | brouillons 39 et 40 : les deux mêmes problèmes attendus (marque hors des sections exigées ; contre-lecture 10 sans ses deux empreintes) | oui |
| table d'en-tête | 232 lignes à empreinte. 15 cloisonnées. 24 de code non recalculées (aucun module ouvert). 1 absente du disque (ligne 179), vérifiée par `git show` : `f7090b5d…`, égale. **192 recalculées hors cloisonnement, toutes égales.** 192 + 24 = 216, le compte de la note | oui (voir « Écarts » pour une ligne) |

**Une règle de jugement, un seuil, une issue ou une prédiction change-t-il ?**
- Dans le texte des sections qui en portent : **non**.
- **Réserve 1 du rédacteur — report ou règle neuve ? Règle neuve, au sens d'un déclencheur neuf d'une issue existante.**
  - Pour un identifiant figé (Mistral), le relevé de la version affichée ne fait que doubler la chaîne de version de chaque réponse : c'est un report de 8.2.
  - Pour un alias, c'est neuf. La chaîne de 8.2 est celle « que rend le service, relevée à chaque appel » (3.4, ligne 484). Une page des mises à jour en est une autre source. Un changement vu sur cette page, sans changement dans les réponses, invalide un lot que 8.2 seul n'aurait pas invalidé.
  - Et l'issue rattachée passe par A12, ligne gelée, écrite pour une « version **figée** retirée ». Le cas d'un alias qui bouge n'y est pas.
  - L'issue elle-même ne change pas, et le sens est prudent. Mais la liste d'arrêt s'allonge hors de 8.2, et une ligne gelée reçoit un cas neuf. La formule « aucune issue ne change » de la note (partie 4) et du statut (ligne 3) est donc trop forte pour ce point. Il revient à Lazar avec C-1.
- **Les autres ajouts de 3.4 sont des procédures de désignation**, hors des variables, des seuils et des verdicts. Le texte le dit (ligne 512).

## 3. Les ajouts du rédacteur

| ajout | nature | pourquoi |
|---|---|---|
| **le compte des réponses étayées, premier critère** (ligne 504 (a) ; définition, ligne 499) | **choix neuf, qui demande le mot de Lazar** | Il définit « meilleur », le cœur des mots de Lazar. Il retourne un choix du devis : sa section 7.1 range l'étayage dans « la qualité des lecteurs », que seules les épreuves jugent, et l'essai de mesure ne relevait pas la vérification des extraits. Il fixe aussi qui juge les ancres : le moins étayé. La question 3 le pose ; elle doit nommer ce retournement (m-6). Le parti pris est déclaré (ligne 511). La recherche de la session principale propose elle-même un essai pilote « avec vérification des citations par programme » (partie 4, point 3) : le choix est défendable. |
| **la condition d'admission sur l'envoi des textes** (ligne 497, (ii)) | **choix neuf, qui demande le mot de Lazar**, bien rangé en condition | Elle touche les données de la course (actions d'épisodes, items des ancres, référence cachée) et, pour DeepSeek, un contact externe (refus de l'entraînement par courriel). La question 2 la pose. Elle doit couvrir les deux fournisseurs (m-6). |
| **« non joignable = ne tient pas »** (ligne 502) | **procédure**, nécessaire pour fermer la règle | Mais sa portée logistique doit être bornée par une vérification de clé (C-3). |
| **l'ordre fixe, Mistral en dernier recours** (ligne 504 (d)) | **procédure** de bris d'égalité | C'est l'ordre des mots (OD-230 : « mistral le chonk », puis « et deepseek j'oubliais »). Une égalité entière, coût au centime compris, est improbable. À déclarer parmi les partis pris (m-5). |
| version constatée, seule chaîne de version, même version avant et après la file | procédure à l'essai ; règle neuve à la course pour un alias | partie 2, et C-1 |

## 4. Les six mineurs du 39

| mineur | où, au brouillon 40 | jugement |
|---|---|---|
| m-1 | 6.9, ligne 829 ; 12, ligne 1375 ; 13.1, ligne 1418 | **fidèle.** « Réexpliquée » seul est attribué à la pièce `2845ca37…` ; la réponse du développeur est « citée en 6.9 », où elle l'est (`91b4bcd3…`, demande 7). La formule retirée ne reste que dans 14.52 et le statut, comme objet traité. |
| m-2 | 8.4, ligne 1096 | **traité comme au point 19**, mais avec une phrase de trop sur ce que fait le programme (m-1 ci-dessus) |
| m-3 | 13.1, ligne 1431 | **fidèle.** Réponses 1, 2 et 3, puis 13, 15, 16, 17 et 31, du côté confirmé : c'est la liste de la vérification de la version 10 (`cb23f4ef…`, ligne 15). Réponses 5 et 32 du côté du développeur. |
| m-4 | 13.1, ligne 1431 | **fidèle sur le fond** : l'échange dans chaque paire est du code neuf depuis la version 7 (`91b4bcd3…`, demande 24 (a)) ; les deux objets possibles sont nommés ; aucune règle n'en dépend. « Est posée » est inexact (m-2 ci-dessus). |
| m-5 | 13.2, ligne 1440 | **fidèle** : le contre-lecteur « confronte chacun des cinq choix à la valeur de ce texte » ; renvoi à 8.7 |
| m-6 | en-tête, ligne 62 | **fidèle** : ligne qualifiée, empreinte reprise et non recalculée. Je ne l'ai pas recalculée non plus. |

## 5. Code arrêté

**Lignes vues, et seulement elles :**
- `src/controle_ia/organismes_discrets/graines_bras_a_v4.py` (`5a66d8c57682…`, calculée par moi), ligne 57 : `LECTEURS = ("claude", "carbon")  # lecteur 1, lecteur 2 (conventions ; 6.2)` ;
- `tests/test_graines_bras_a_v12.py` (`7fdde38d3bde…`, calculée par moi) : ligne 32, une liste de clés qui contient `…/e7/carbon` ; ligne 136, `g.cle_retrait("t", 0, "carbon")` finit par `/e0/carbon` ; ligne 140, la clé `astra` dans une liste de refus attendus.

**Jugement : vrai, sur ces lignes.** La clé du lecteur 2 est la chaîne `carbon`. Aucun identifiant de modèle n'entre dans la clé. Remplacer le modèle ne change donc ni les clés ni les tirages.
- **Limite** : le module en vigueur est la version 12 (lignes 161 et 1430 du texte), non la version 4. Je n'ai pas vu comment la version 12 obtient la clé : l'essai de la version 12 le montre, sans que j'aie vu sur quel module il porte. La note dit que la version 12 ne porte pas la chaîne. C'est cohérent avec un import, non vérifié par moi.
- **Le texte le dit clairement** : 6.2, ligne 661 (« nom de clé hérité, qui ne désigne plus un modèle ; il est gardé pour que ni les tirages ni le code arrêté ne changent ») ; conventions, ligne 254 ; 14.52, ligne 2391.

**À écrire hors du texte :**
- **devis de l'essai comparatif** : tarifs relevés et datés des deux modèles, voie d'accès comprise (point d'accès européen de Mistral) ; plafond par file ; sortie maximale envoyée, réflexion comprise ; champs de jetons de chaque service pour `C` et le point 7 ; manière dont chaque service rend sa version ; contre-lecture par un agent d'un autre modèle ; une ligne de calcul par file ;
- **vérification de chaque clé** avant sa file, sous une ligne de GO (C-3) ;
- **chef de l'essai, version neuve** : `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` nomme les files Carbon et GPT (note, partie 7). Files Mistral et DeepSeek ; compte des réponses étayées par les programmes de vérification des extraits de l'instrument, version citée ; relevé de la version affichée par un programme ; refus de tout message système et de tout outil ; contre-lu ;
- **configuration de l'essai, version neuve** : l'actuelle nomme `carbon`, `gpt`, `reglages_carbon` et les motifs de fin de Google et d'OpenAI ; motifs de fin des deux services neufs ; forme du brouillon en vigueur, non celle du brouillon 5 ;
- **un relais par fournisseur** ;
- **fichier de la règle**, copie de 3.4, scellé avant le premier envoi, qui cite l'empreinte du brouillon en vigueur ;
- **configuration de la course** : identifiants, réglages, chaînes de version, relevé de la version affichée par lot, et **la correspondance écrite entre la clé `carbon` et le modèle désigné**, reprise au manifeste ;
- **garde des familles** (8.4, lignes 1071 et 1139) : vérifier, dans le lanceur ou la configuration, comment la famille d'un lecteur et du juge est reconnue. La recherche de chaînes du rédacteur ne portait que sur `carbon`, `astra`, `gemini` et `gpt-6`. Je n'ai ouvert aucun module ;
- **courriels** rédigés par la session, envoyés par Lazar, si la question 2 le demande : refus de l'entraînement chez DeepSeek ; non-conservation chez Mistral ;
- **lignes du registre** par la session principale.

## 6. Registre (référence locale `3c2b1436`, sans appel réseau)

- **GO-2026-11-20-31** (ligne 562) : **citée correctement.** « Carbon sort des lecteurs du bras A et reste concepteur de nouveaux modes ».
- **GO-2026-11-20-38** (ligne 569) : **citée en partie.** Le texte omet « sur les bancs d'essais publics qui correspondent à la tâche du lecteur », et ce que la ligne confie à la mère (comparer, recommander) et à Lazar (créer la clé). « Effort maximal » et « meilleur modèle de la famille » sont bien repris. Voir m-3.
- **GO-2026-11-20-43** (ligne 574) : **citée correctement** pour l'option (a), la pièce `8189dcec…` et l'absence de dépense. « Deux clés, une chez chaque fournisseur » n'est pas repris (m-3, C-3).
- **Une ligne nomme-t-elle GO-2026-11-19-97 hors la sienne ? Non** (seule la ligne 530).
- Le commit `2286114ee`, cité ligne 8, existe dans mon dépôt (« mot « a go reco » … consigné et scellé ; journal OD-233 »).

## 7. Les trois questions pour Lazar

| question | options | ce que chaque réponse change | recommandation | jugement |
|---|---|---|---|---|
| 1. identifiants et voies d'accès | **aucune option écrite** : « confirmer » | non dit | confirmer, confiance moyenne, deux réserves | **mal posée.** Elle mêle trois choix : (a) « le chonk » est-il Mistral Large 4 ? (b) pour DeepSeek, Flash ou V4 Pro ? GO-2026-11-20-38 dit « meilleur modèle de la famille » ; DeepSeek nomme V4 Pro son « vaisseau amiral », et le seul chiffre commun sur les textes longs le met devant ; (c) un alias non figé est-il admis, avec le risque A10 ou A12 (C-1) ? Chacun demande ses options et ses conséquences. |
| 2. envoi des textes à DeepSeek | (a), (b), (c) | écrit pour chacune ; (c) laisse le juge à nommer par Lazar | (b), confiance moyenne | **bien posée pour DeepSeek.** Elle doit aussi demander le mot pour Mistral, que l'admission exige (m-6), avec ses mesures (point d'accès européen, refus dans la console, non-conservation sur demande) |
| 3. réponses étayées en premier | (a), (b), (c) | implicite | (a), confiance moyenne | **bien posée**, mais elle doit dire que le devis rangeait l'étayage dans la qualité réservée aux épreuves, et demander de confirmer le banc lui-même (24 entrées synthétiques, un réglage, 48 appels), que la pièce des mots dit « à confirmer » |

**Manque-t-il une question ?**
- **Oui : la version non figée** (C-1), si elle n'est pas séparée dans la question 1.
- **Facultatif** : « un seul tient » (le défaut est déjà le nœud) ; les clés ne sont pas une question, mais une action de Lazar à rappeler (GO-2026-11-20-38).

## Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon40.md` : par différence, par programme, et lignes 476 à 512, 829, 970, 971, 974, 1045 à 1057, 1096, 1163 à 1172, 1186, 1375, 1418, 1421, 1423, 1431, 1440, 216 et 238 (texte de la ligne seulement), et des extraits par recherche de chaînes dans ce seul fichier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon39.md` : par différence et par programme ; ligne 1394.
- `docs/notes/relance-organismes-discrets-v1/preenregistrement-v2-brouillon40-note-v1.md` : en entier.
- `docs/notes/relance-organismes-discrets-v1/verification-brouillon39-bras-a-v1.md` : en entier.
- `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-second-lecteur-et-juge-des-ancres-bras-a-2026-11-20-v1.md` : en entier.
- `docs/notes/relance-organismes-discrets-v1/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md` : titres, et section 7 (lignes 186 à 220).
- `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` : lignes 247 à 253 ; plus la recherche des seuls identifiants OD-228, OD-234 et OD-235, qui a affiché leurs numéros de ligne.
- `docs/notes/bras-a-sans-interne-v1/verification-habilitee-autres-moniteurs-v10-sans-interne-v1.md` : en entier.
- `docs/notes/bras-a-sans-interne-v1/lecture-habilitee-sans-interne-v8-v1.md` : lignes 57 à 70, et la recherche de « Demande 24 ».
- Par `git show origin/main:` : `registres/go.md`, lignes 455, 467 à 469 (début seulement), 530 (début seulement), 550, 551, 562, 569, 574 ; `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md`, en entier.
- `src/controle_ia/organismes_discrets/graines_bras_a_v4.py`, ligne 57 ; `tests/test_graines_bras_a_v12.py`, lignes 32, 136 et 140.
- Fichiers de la table d'en-tête : 193 lus en octets pour l'empreinte seulement.
- `controle_ia.prereg.problemes` et `controle_ia.scellement` : exécutés, non lus (signature de `problemes` affichée).

## Écarts

- **Un franchissement, déclaré.** Ma recherche des lignes cloisonnées de la table d'en-tête en a trouvé 14. La quinzième, ligne 216, vise `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, « code source de la base ». Elle touche la base « mots et coût », cloisonnée. **J'en ai pris l'empreinte, en octets**, égale à celle du texte. Aucun contenu affiché ni lu. Je n'en tire rien d'autre que ce compte : 15 cloisonnées, comme la note.
- **Un débord mineur** : un `ls` du dossier `docs/notes/relance-organismes-discrets-v1/`, réduit à un compte de noms (427), pour vérifier que le nom de ce rapport était libre. Aucun nom affiché.
- Aucun autre accès à un chemin cloisonné ; aucun module de code ouvert hors des lignes permises ; aucune réponse d'essai ; rien sous `runs/essai-mesure-lecteurs-bras-a-v1/**/envois/`.
- Aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. `registres/`, `.claude/` et le journal ne sont pas touchés. Un seul fichier écrit, celui-ci.
