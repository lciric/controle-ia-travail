# Note du rédacteur — brouillon 41 du texte neuf du bras A des organismes discrets — v1

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même rôle que pour les brouillons 21 à 40. Je conçois ; je ne consigne pas au registre et je ne committe pas.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon41.md`, `cb6ca087d3d4c46dcd70e2a2f2f41ea765d05891f36a5fc1747f5cab2b088df4`, scellé comme brouillon. 2 452 lignes.
- **Point de départ** : le brouillon 40 (`b4670b88b8abb73b2a40c61fb5d1cf17bb513b52b710ba9b06b22b0e4304db89`), inchangé.
- **Heures (UTC, relevées par `date -u`)** : commencé vers 13:28Z (premier relevé : 2026-11-20T13:30:37Z) ; texte scellé à 13:37:52Z ; note finie à 2026-11-20T13:39:30Z.
- **Méthode** : 44 remplacements exacts, chacun sur une ancre trouvée une seule fois ; quatre d'entre eux remplacent un passage borné par deux ancres uniques. Texte construit dans le bloc-notes, contrôlé, posé une fois sans écrasement, comparé octet pour octet, puis scellé.
- **Pièces traitées** :
  - la vérification du brouillon 40, `docs/notes/relance-organismes-discrets-v1/verification-brouillon40-bras-a-v1.md`, `a8e2fa68856082d4f94b81ed0c6474f61da9679ea73a63d116b34545dc2bc0d1` ;
  - le mot de Lazar « 1a 2a 3b4c 5a », `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md`, `93cbc6f4c78d00c5b91ca29e5b300bef345cd7aa46c89db2be6bff95a46d5beb` ;
  - le mot de Lazar « c go », `docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-des-ancres-neon-bras-a-2026-11-20-v1.md`, `6ebab24f009bbb7587eb14c22ae832f3d93ce5911e832cce087e4afa7c6f9cf2` ;
  - trois relevés documentaires, provenances par transcription, non opposables (R7) : Mistral (`b8163cc992903311e07b6fd60c36db413dda2bbbded8ae4d6c4a750a3278130f`), OpenAI (`ab277adfe0cde40480424c2d36c8a195eebe0ca1160592e21a7ede786f5b6cee`), Google (`ac8bb15e1cfc137e958775c46c4196e120fa46f4981625ce6a67f17ab6fc6ba2`) ;
  - le registre des GO, par `git show origin/main:registres/go.md`, tête locale `b0a6981e`, sans appel réseau : lignes GO-2026-11-19-32, GO-2026-11-20-38, -43, -47 et -48 ;
  - la pièce sans interne des réponses du développeur habilité aux demandes 18, 19 et 24 (a), `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md`, `e2f246ebb533ce8a28f4a54c8068723cd30340059c68ff5cf34fc7edd965330b`, par `git show origin/main:` seulement ;
  - deux compléments de la session principale, reçus à 13:30Z par la session de relance : la ligne GO-2026-11-20-58 ; la version 2 du lanceur de l'étape de discrétion.
- **Aucune fiche n'est ajoutée.**

## 1. Points traités

| point | ce que le texte écrit | où |
|---|---|---|
| **DeepSeek hors du bras A** | par le choix 3 (b) et par le choix 4 (c), chacun suffisant | conventions ; 3.4 ; 6.11 ; 13.1 |
| **essai d'admission du second lecteur** | la seule file Mistral, 24 appels sur les 24 entrées synthétiques ; Mistral Large 4 (`mistral-large-4-0`) est second lecteur s'il tient, au critère du devis de l'essai de mesure, section 7.2, inchangé ; sinon nœud de Lazar | 3.4 ; 6.11 ; 13 ; 13.1 |
| **règle à deux candidats** | retirée, avec son ordre fixe et son départage ; l'histoire tient en une phrase | 3.4 |
| **réponses étayées (choix 5 (a))** | mesurées et rapportées, sans verdict ; elles n'entrent dans aucune des deux règles | 3.4 |
| **identifiant figé (choix 3 (b))** | « version figée et inscrite » et la ligne A12 gardées telles quelles ; tout ce qui admettait un alias est retiré, avec la version « constatée » et le déclencheur rangé sous 8.2, A10, A12 et A17 ; ce que la documentation établit est écrit pour Mistral et pour Neon, avec les réserves des relevés ; nom servi relevé par programme à chaque appel ; s'il diffère, issue de 8.2 telle qu'elle est | 3.4 ; 13.2, case « version des modèles » |
| **juge des deux ancres** | `gemini-4-neon`, à la place du « non retenu » du brouillon 40 ; fiche du nœud 1 et option γ inchangées, une marque ajoutée | conventions ; 3.4 ; 6.3 (d) ; 6.11 ; 12 ; 13.1 |
| **essai d'admission du juge** | huit lectures, les huit entrées que la configuration de l'essai de mesure donnait à la file GPT ; règle fermée (partie 2) ; réglages : `thinking_level` à `xhigh`, température non envoyée, offre payante | 3.4 ; 6.11 |
| **envoi des textes** | condition d'admission pour Mistral et pour Google, sous la case de 13.1 ; question 1 | 3.4 ; 13.1 |
| **C-1 de la vérification** | levée par le choix 3 (b) | 3.4 ; 13.2 |
| **C-2** | sortie maximale envoyée et champs de jetons renvoyés au devis des essais d'admission, contre-lu, avant tout envoi ; le texte fixe « réflexion comprise » ; « sans choix de la session » retiré | 3.4 |
| **C-3** | clé de chaque fournisseur vérifiée avant sa file par un appel minimal ; un échec au départ n'est pas « ne tient pas » ; « ne tient pas » ne se dit que d'une file partie ; clés citées par `MISTRAL_API_KEY` et, pour Google, par la variable que lit le programme (`GEMINI_API_KEY` dans la configuration de l'essai de mesure) | 3.4 ; 13.1 |
| m-1 | la phrase sur ce que fait le programme est retirée de 8.4 ; il reste « non éprouvé ici » et le renvoi à 8.7 | 8.4 |
| m-2 | sans objet : l'attestation rendue répond à la question ; la case le dit | 13.1, case du module |
| m-3 | GO-2026-11-20-38 et -43 citées telles qu'elles sont | en-tête, « commit du dépôt lu » |
| m-4 | « le tarif de la voie d'accès retenue, et le plus haut selon l'heure » ; le coût projeté n'est plus un critère, il est rapporté | 13.2, case « tarifs » ; 3.4 |
| m-5 | sans objet : l'ordre fixe est retiré | — |
| m-6 | sans objet pour DeepSeek ; les trois questions du brouillon 40 sont tranchées (1 a, 2 a, 3 b, 4 c, 5 a) et retirées de cette note ; la condition d'envoi couvre les deux fournisseurs qui restent | 3.4 ; partie 4 |
| **module des cinq moniteurs, version 11** | `autres_moniteurs_v11.py`, `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` ; seule l'empreinte inscrite de la préparation change (préparation en version 3, `c0021298…`) ; la configuration cite la version 11 (`piece_source.sha256`) ; la version 10 reste dite vérifiée conforme ; la contre-lecture habilitée de la version 11 est dite à faire, sauf si le lecteur habilité écrit que le différentiel suffit | 13.1, case du module |
| **préparation** | confirmation reçue, avec la version 3 : plus aucune position tirée pour le juge | 13.1, case du module |
| **attestation de la version 7 à la version 10** | rendue : aucun calcul de moniteur ne change ; l'échange dans chaque paire est un calcul neuf (version 8), dont viennent les valeurs p ; ce qui est rendu change, non ce qui est calculé | 13.1, case du module |
| **lanceur de l'étape de discrétion** | écrit ; trois sous-commandes, la session principale verse entre elles ; « une seule exécution » ne vaut que pour l'étape de discrétion ; le lanceur inscrit lui-même la ligne de configuration de la base et refuse si la clé existe ; la citation « il enchaîne… » reste à la lettre, avec une phrase qui dit comment elle se lit ; **la version 1 est gardée comme histoire, et la version qui fait foi est celle que la contre-lecture habilitée rendra conforme**, chemin et empreinte à inscrire (complément de 13:30Z) | 13.2, case du lanceur ; 13.1 |
| **dossier du fichier des rangs** | `donnees/bras-a-v2-discretion/rangs-par-unite`, disjoint de la sortie, fixé par la configuration scellée ; couvert par la garde statique de la relance, par fragment de nom pour le fichier et par motif pour les dossiers `bras_a_v2_habilite_*` ; écrit comme relu par la session (journal, OD-237), module non ouvert par moi | 13.2, case du lanceur ; 13.1 |
| **GO-2026-11-20-58** | citée « selon la session principale, 13:30Z » ; non lue par moi : elle n'est pas sur la référence locale | en-tête ; 3.4 ; 12 ; 13.1 ; 14.53 |

## 2. Les deux règles d'admission, telles qu'écrites en 3.4

1. **Mistral Large 4 tient** : 24 réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, 22 de forme conforme au moins. C'est le critère du devis de l'essai de mesure, section 7.2, inchangé. Une file arrêtée à son plafond ne tient pas.
2. **`gemini-4-neon` tient** : huit réponses de code 200, reprise unique comprise, sans refus, sans fin par sortie maximale atteinte, **les huit de forme conforme**. Seuil choisi d'avance, non étalonné (question 2).
3. Pour les deux : toutes les réponses de la file portent le nom servi relevé à la vérification de la clé. Une file coupée par le service après son premier envoi ne tient pas.
4. Une file n'est jouée qu'une fois ; elle est partie dès son premier envoi. Avant, rien n'est « ne tient pas ».
5. Qui tient prend son rôle. Qui ne tient pas : nœud de Lazar ; l'autre rôle n'en dépend pas.
6. Aucun autre modèle sans un mot de Lazar ; le texte n'est pas scellé tant que les deux rôles ne sont pas pourvus.
7. Sortie maximale à la course : la règle du devis de l'essai de mesure, section 7.3, point 7, sur ce que la sortie maximale du service borne.
8. Règles appliquées par programme, scellées avec le brouillon ; fichier de règles scellé avant le premier envoi.

**Vérification de la clé.** Saine si le code de retour est 200 et si le nom servi est l'identifiant demandé. Clé refusée, compte non approvisionné, limite de débit, panne : la file ne part pas, la cause est corrigée, la vérification se refait sous sa ligne. Modèle inconnu, ou nom servi autre que l'identifiant demandé : nœud de Lazar.

## 3. Sections de jugement touchées

**Aucune règle de jugement, aucun seuil, aucune issue, aucune prédiction ne change.**

| section | lignes changées | ce qui change |
|---|---|---|
| hypothèse, prédiction, métrique, seuil | 0 | — |
| 7.1 à 7.8 | 0 | — |
| 10 | 0 | — |
| 12 | 1 sur 172 | fiche du nœud 1 : une marque du brouillon 41 ajoutée en fin de ligne, qui nomme `gemini-4-neon` ; la fiche, l'option γ et la marque du brouillon 40 restent mot pour mot |
| 6.3 (ordre d'exécution, gelé) | 1 sur 27 | étape (d) : le nom du juge des ancres. L'ordre ne change pas |
| 8.4 | 1 sur 105 | mineur m-1 : une phrase sur ce que fait le programme est retirée ; le renvoi à 8.7 reste |
| 6.1, 6.2, 6.4 à 6.10, 6.12, 8.1 à 8.3, 8.5 à 8.7, 9, 11 | 0 | — |

Sections sans jugement qui changent : en-tête et conventions (19 lignes changées, dont 9 lignes neuves à la table) ; 3.4 (41 lignes au lieu de 38 : le bloc de l'essai comparatif, 19 lignes, devient un bloc de 22, et trois autres lignes changent) ; 6.11 (3) ; préambule de 13 (2) ; 13.1 (3 cases) ; 13.2 (4 cases) ; 14 (14.53, 26 lignes neuves) ; contre-lecture (2).

## 4. Questions pour Lazar

**Question 1 — à quelle condition envoie-t-on les textes de la course à Mistral et à Google ?**
- Enjeu : les lectures de la course portent des actions d'épisodes, les items des ancres et, pour la couverture, la référence cachée. Le choix 4 (c) ne tranche que DeepSeek. Les essais d'admission, eux, n'envoient que des textes synthétiques.
- Options :
  - (a) sans condition. Avantage : rien à constater. Inconvénient : la référence cachée part sans garde écrite ;
  - (b) la condition écrite au texte : offre payante ; usage pour l'entraînement refusé au réglage du compte ou exclu par les conditions de l'offre ; point d'accès européen pour Mistral ; chaque point constaté, daté, versé. Avantage : se constate sans contact externe. Inconvénient : les textes restent conservés selon les règles du fournisseur ;
  - (c) (b), plus une demande de non-conservation à chaque fournisseur. Avantage : la garde la plus forte. Inconvénient : contact externe, que je rédige et que tu envoies ; délai inconnu.
- **Recommandation : (b).** Confiance : moyenne. C'est aussi la recommandation de la session (pièce du mot « 1a 2a 3b4c 5a »).
- Défaut : nœud, sans défaut de 48 heures ; aucune file ne part avant ton mot.

**Question 2 — quel seuil pour l'essai d'admission du juge ?**
- Enjeu : Neon n'a été mesuré nulle part. La commande demandait huit lectures, comme pour Astra, qui n'avait pas de règle. Il en faut une, écrite d'avance.
- Options :
  - (a) huit lectures, huit sur huit de forme conforme (le texte). Avantage : court ; c'est le plus petit compte sur huit qui tienne la proportion de 22 sur 24. Inconvénient : une seule réponse mal formée te rend la décision ;
  - (b) huit lectures, sept sur huit. Avantage : tolère un accident. Inconvénient : seuil plus lâche que celui du lecteur ;
  - (c) les 24 entrées, 22 sur 24, le critère même du second lecteur. Avantage : aucun seuil neuf, et un chiffrage mieux fondé. Inconvénient : 16 appels de plus, quelques dollars au pire.
- **Recommandation : (a), tel qu'écrit, par fidélité à la commande ; (c) me paraît aussi bonne, et la seule sans seuil neuf.** Confiance : moyenne. Passer de (a) à (c) change trois lignes de 3.4 et une de 6.11, avant tout envoi.
- Défaut : nœud ; la file du juge ne part pas avant ton mot.

## 5. Contrôles par programme

| contrôle | résultat |
|---|---|
| titres | 55, identiques hors le titre de niveau 1 |
| sections changées | celles de la partie 3, et rien d'autre |
| consignes figées (3.2 et 3.3) | égales à celles du brouillon 40 : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`, `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` |
| marque des cases | 7 lignes, toutes en 13.1, 8 occurrences : les mêmes cases qu'au brouillon 40 |
| table d'en-tête | 241 lignes à empreinte entière (232, plus 9 neuves). **224 recalculées, toutes égales**, les modules de code compris (octets seulement, aucun ouvert). **16 sautées, aucune empreinte prise** : les 15 du brouillon 40, la ligne du code de la base « mots et coût » comprise, reprises telles quelles ; et la ligne neuve de la pièce sans interne, dont l'empreinte vient de la seule lecture permise, par `git show`. 1 absente du disque : la recherche de la session principale, vérifiée par `git show` (`f7090b5d…`, égale) |
| validateur `problemes()` | les deux problèmes attendus, les mêmes qu'au brouillon 40 |
| mots retirés | « version affichée » ne reste que dans 14.52, histoire ; « alias » ne reste que pour dire qu'aucun n'est admis, et dans l'histoire ; « comparatif » ne reste que dans l'histoire |

## 6. Ce qui reste hors du texte

- **Devis des deux essais d'admission** : tarifs relevés et datés par la voie d'accès retenue ; plafond par file et par vérification de clé ; sortie maximale envoyée à chaque modèle ; champs de jetons et champ du nom servi de chaque service ; ce que la sortie maximale de chaque service borne ; sa contre-lecture par un agent d'un autre modèle.
- **Lignes de calcul** : une par file, une par vérification de clé.
- **Constat de la condition d'envoi** pour Mistral et pour Google, daté et versé, après la question 1.
- **Programme qui conduit les essais**, version neuve : files Mistral et du juge ; compte des réponses étayées ; nom servi comparé à celui de la vérification ; refus de tout message système et de tout outil ; contre-lu. **Sa configuration**, neuve, à la forme du brouillon en vigueur. **Un relais par fournisseur.** **Le fichier des règles**, scellé avant le premier envoi.
- **Configuration de la course** : identifiants figés, réglages, noms servis, et la correspondance écrite entre la clé de graine `carbon` et `mistral-large-4-0`.
- **Garde des familles** (8.4) : vérifier comment le lanceur ou la configuration reconnaît la famille Mistral et la famille Google.
- **Registre**, par la session principale : la ligne du mot « 1a 2a 3b4c 5a » ; la confrontation de GO-2026-11-20-58 à ce texte.
- **Côté habilité** : la contre-lecture de la version 11 du module ; la version conforme du lanceur, son chemin et son empreinte ; la configuration scellée du lanceur ; la confrontation des deux identifiants à la liste des familles ; le mot du lecteur habilité sur l'attestation.
- **Code arrêté en version 13 : rien à changer.**

## 7. Réserves

1. **Deux ajouts de ma main à la vérification de la clé et à la règle.** (i) Un nom servi autre que l'identifiant demandé, à la vérification de la clé, est un nœud de Lazar : si Mistral rend son nom sous une autre forme, la file attendra un mot. (ii) Le point 3 des règles — un seul nom servi sur toute la file — s'ajoute au critère « inchangé » de la section 7.2 ; le brouillon 40 le portait déjà. Ce sont des procédures d'admission, hors des sections de jugement. Au vérificateur de dire si l'une est de trop.
2. **« Huit sur huit » est un seuil neuf**, de procédure. Je le pose à Lazar (question 2).
3. **Un modèle non admis** n'est plus compté « ne tient pas », comme au brouillon 40 : sa file ne part pas, et c'est un nœud. L'effet est le même ; le mot est plus juste depuis la correction C-3.
4. **La ligne A12 ne nomme qu'un lecteur.** Le texte ne dit pas ce qui arrive si le nom du juge est retiré entre les deux parties des ancres, hors l'arrêt du lot par 8.2. Je n'ai rien ajouté : ce serait une issue neuve.
5. **GO-2026-11-20-58** n'a pas été lue par moi.
6. **Lanceur** : je n'ai ni le nom ni l'empreinte de la version 2. La case le dit.
7. **Attestation** : j'ai écrit un reste, que le lecteur habilité dise si l'attestation du développeur lui suffit. La pièce ne le demande pas ; c'est une prudence, à retirer si elle gêne.
8. **L'identifiant de session** de l'en-tête du texte (ligne « Sessions ») n'est pas celui des pièces des mots de Lazar. Je n'y ai pas touché.
9. **Les relevés documentaires** sont des transcriptions par un outil qui résume. Les phrases citées de Mistral et de Google en viennent, non des pages.
10. **Je n'ai pas relu le texte en entier.**

## 8. Fichiers ouverts, et débords

- Le brouillon 40, par passages et par programme ; sa note et sa vérification, en entier.
- Les deux pièces scellées des mots de Lazar et les trois relevés documentaires, en entier ; le journal de la relance, lignes 253 à 265 (OD-234 à OD-246).
- Par `git show origin/main:`, sans appel réseau : le registre des GO, lignes 465, 569 et 574 à 579 ; la pièce sans interne des réponses du développeur habilité, en entier ; la recherche de la session principale, pour son empreinte seulement.
- Le devis de l'essai de mesure, lignes 186 à 222, et une recherche de chaînes dans ce seul fichier.
- La configuration de l'essai de mesure : les blocs des files Carbon et GPT (variable de clé, huit entrées), par numéros de lignes.
- `scripts/chef_essai_mesure_lecteurs_bras_a_v1.py` : une recherche de noms de variables de clé, dans ce seul fichier ; rien n'en est tiré.
- `src/controle_ia/prereg.py` : la constante de la marque et la signature du validateur ; validateur exécuté.
- **Franchissement, déclaré** : la pièce sans interne est rangée sous `docs/notes/bras-a-moniteurs-v1/`. Je l'ai lue par `git show` seulement, comme permis, et j'en ai pris l'empreinte sur cette lecture. Aucun des fichiers internes qu'elle nomme n'est ouvert ; leurs empreintes sont transcrites.
- **Aucun autre débord.** Aucune recherche n'a parcouru un dossier. Aucune empreinte prise sur une ligne de la table qui touche un chemin cloisonné.
- **Non ouverts** : aucun module du code ; aucun interne de moniteur, aucun module habilité, rien de la branche habilitée ; rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ; aucune réponse ni aucun envoi de l'essai de mesure ; aucune clé. Aucun appel de modèle, aucun sous-agent, aucune dépense, aucun appel réseau. Rien de committé ; `registres/`, `.claude/` et le journal non touchés.
