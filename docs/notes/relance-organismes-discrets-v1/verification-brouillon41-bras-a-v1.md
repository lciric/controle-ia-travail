# Vérification du brouillon 41 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je juge ; je ne corrige rien. Ni scellé ni committé. Écrit le 2026-11-20, vers 13:50Z (`date -u`).
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon41.md`, `cb6ca087d3d4c46dcd70e2a2f2f41ea765d05891f36a5fc1747f5cab2b088df4`, 2 452 lignes.
- **Pièces, compagnons vérifiés** (`python -m controle_ia.scellement verifier`, tous « OK ») :
  - la note du rédacteur, `preenregistrement-v2-brouillon41-note-v1.md`, `2314abb5a25c…` (143 lignes) ;
  - le brouillon 40, `b4670b88b8ab…` (2 414 lignes) ; la vérification du brouillon 40, `a8e2fa688560…` ;
  - les mots de Lazar : `mots-de-lazar-second-lecteur-et-juge-des-ancres-bras-a-2026-11-20-v1.md` (`8189dcec0f83…`), `mots-de-lazar-cinq-choix-lecteur-bras-a-2026-11-20-v1.md` (`93cbc6f4c78d…`), `mots-de-lazar-juge-des-ancres-neon-bras-a-2026-11-20-v1.md` (`6ebab24f009b…`) ;
  - les trois relevés documentaires : Mistral (`b8163cc99290…`), OpenAI (`ab277adfe0cd…`), Google (`ac8bb15e1cfc…`).
- **Lus par `git show origin/main:`**, référence locale `7b436f06`, sans appel réseau :
  - `registres/go.md` (empreinte de cette lecture : `a70e220a3e0e…`, 591 lignes) ;
  - la pièce sans interne `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` : empreinte recalculée `e2f246ebb533…`, égale ;
  - la recherche de la session principale `lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md` : empreinte `f7090b5d52b6…`, égale à la ligne 179 du texte ; une recherche de chaînes seulement.
- **Le journal de la relance n'a pas de compagnon** (`f9f05381c70b…`, calculée par moi) : lignes 253 à 267 (OD-234 à OD-248).
- **Méthode** :
  - différence des brouillons 40 et 41 par programme, ligne par ligne puis mot par mot ;
  - comparaison section par section, sous les 54 titres ;
  - lecture entière du bloc neuf de 3.4 (lignes 503 à 524) et des lignes changées ;
  - empreintes des consignes figées, des marques, de la table d'en-tête, validateur `problemes()`, par programme ;
  - confrontation de chaque phrase neuve sur les relevés, les mots de Lazar et la pièce du développeur à leur source.

## Verdict : **engageable après corrections**

- Les mots de Lazar sont portés : DeepSeek sort partout, Mistral Large 4 est seul essayé pour le second lecteur, `gemini-4-neon` juge les ancres, et rien n'admet plus un alias.
- **Aucune règle de jugement, aucun seuil, aucune prédiction ne change dans les sections gelées.** Les contrôles de la note concordent, refaits par programme.
- La correction 1 du brouillon 40 est levée. Les corrections 2 et 3 sont traitées.
- Mais trois points demandent une retouche. Le texte dit plus qu'un relevé n'établit. Il affirme pour le juge une issue que la liste d'arrêt n'écrit pas. Et il range sous les mots de Lazar un essai d'admission du juge qui n'y est pas.

**Corrections :**
- **C-1. Une phrase dit plus que le relevé de Google.** 3.4, ligne 505 : « aucun identifiant numéroté n'existe pour ce modèle ». Le relevé (`ac8bb15e…`, ligne 10) écrit : « Non trouvé : […] des identifiants numérotés pour ces modèles ». « Non trouvé » n'est pas « n'existe pas ». Écrire « aucun identifiant numéroté n'a été trouvé ».
- **C-2. Pour le juge des ancres, le texte affirme une issue qui n'est pas écrite.**
  - 3.4, ligne 505 : « Si le nom servi diffère de celui que la configuration inscrit : c'est l'issue que ce texte prévoit déjà — 8.2, « version », pour un lot ; ligne A12 […] ». La phrase vaut pour les deux modèles. 13.2, ligne 1453, dit de même pour « le second lecteur et le juge des deux ancres ».
  - Or 8.2, ligne « version » (texte, ligne 1061), ne nomme que des lots de lecteurs : lot décisif, lot d'épreuve de l'appariement, lot d'épreuve de la couverture. A12 (ligne 982) ne nomme qu'« un lecteur ». Le jugement des ancres, étape (d) de 6.3, n'est ni l'un ni l'autre. Aucune issue n'est écrite si le nom servi du juge change pendant les ancres.
  - Le défaut vient du brouillon 40, où la même phrase valait pour « chaque modèle ». Il n'a pas été relevé alors. La réserve 4 du rédacteur n'en voit qu'une partie : le retrait entre les deux parties des ancres.
  - Ajouter une issue, ce serait allonger 8.2, section gelée. Ce n'est donc pas au rédacteur. Il faut : (i) dire en 3.4 et en 13.2 que l'issue de 8.2 vaut pour les lecteurs, et qu'aucune issue n'est écrite pour le juge des ancres ; (ii) poser à Lazar la question manquante (voir la question 7).
- **C-3. L'essai d'admission du juge est attribué aux mots de Lazar, qui ne le portent pas.**
  - 3.4, ligne 503, cite pour « deux essais d'admission » les pièces `93cbc6f4…` et `6ebab24f…`, GO-2026-11-20-43 et GO-2026-11-20-58. Les conventions (ligne 263) et la marque du nœud 1 (ligne 1246) écrivent « `gemini-4-neon`, s'il tient au sien ».
  - Or « c go » (`6ebab24f…`, ligne 7) dit seulement « `gemini-4-neon` (Google) juge les deux ancres ». GO-2026-11-20-58 (ligne 589) aussi, sans condition. La pièce `93cbc6f4…` ne parle pas d'un essai du juge. La note dit que « la commande » demandait huit lectures. Cette commande est celle de la session, non un mot de Lazar.
  - L'ajout ne retire rien à Lazar : « ne tient pas » lui rend la décision. Mais un seuil de huit sur huit peut défaire sa désignation pour une seule réponse mal formée. L'essai lui-même, et non seulement son seuil, est donc un choix à lui poser.
  - Il faut dire en 3.4 que l'essai d'admission du juge et sa règle sont une procédure de la session, absente du mot « c go » et de GO-2026-11-20-58. Et la question 2 doit offrir l'option « pas de règle d'admission » (voir la question 7).

**Mineurs :**
- **m-1.** Règle 8 de 3.4 (ligne 521) : « la session n'y a aucune liberté » a disparu. Ce retrait n'est déclaré nulle part. La correction C-2 du brouillon 40 ne visait que « sans choix de la session », à la ligne des réglages. Après le premier envoi, la phrase reste vraie. La remettre, ou dire pourquoi elle part.
- **m-2.** Question 2 : la note donne pour défaut « la file du juge ne part pas avant ton mot ». Le texte ne le dit pas. Le préambule de 13 (ligne 1419) range bien le seuil parmi ce qui manque de Lazar, mais aucune phrase ne retient la file. L'écrire en 3.4, règle 2, ou dans l'ordre du préambule de 13 (ligne 1420).
- **m-3.** `gemini-4-neon` et le choix 3 (b). L'admission (i) exige « son identifiant figé » (ligne 507) ; 13.2 écrit « l'identifiant figé demandé » pour les trois modèles. Pour Neon, le relevé ne donne qu'un nom « stable », avec « usually ». C'est Lazar qui l'a admis, par « c go », en connaissant cette réserve (`6ebab24f…`, ligne 9). Le texte doit le dire : sinon, (i) semble constaté par la session.
- **m-4.** Réserves des relevés non reprises :
  - Mistral (`b8163cc9…`, ligne 7) : l'identifiant n'apparaît que dans l'adresse de la page ; la même page porte un texte « mistral-large-4+2 », non interprété ;
  - la recherche `f7090b5d…` (ligne 13) note que la fiche affiche aussi `mistral-large-4`, qui est une forme d'alias selon le relevé (ligne 6) ;
  - Google (`ac8bb15e…`, ligne 13) : Neon est sorti le 18 novembre 2026, et il est absent des tables de Vertex AI.
  - Aucune règle n'en dépend : la vérification de la clé tranche. Mais la question demande « avec leurs réserves ».
- **m-5.** La case de 13.1 (ligne 1433) fixe pour Mistral « le service de Mistral, par son point d'accès européen ». Ce point fait partie de la condition d'envoi, encore posée à Lazar (question 1). Écrire « si la condition écrite en 3.4 est retenue ».
- **m-6.** Case du module, 13.1 (ligne 1443) : « la configuration de l'analyse cite la version 11 ». La pièce `e2f246eb…` (ligne 11) écrit « À changer dans la configuration de l'analyse ». Écrire « doit citer » ou « est à changer ».
- **m-7.** Case du lanceur, 13.2 (ligne 1460) : la « décision de la session principale » sur la ligne de configuration de la base n'a pas de source. La pièce `e2f246eb…` (ligne 25) dit « Point à trancher ». La décision n'est attestée qu'au journal (OD-237, ligne 256). Citer OD-237.
- **m-8.** 14.53, ligne m-6 (ligne 2431) : « le banc de 24 entrées, que Lazar a confirmé par le choix 5 (a) ». Le choix 5 (a) nomme les 24 entrées comme base du compte des réponses étayées ; il ne confirme pas le banc comme tel. Écrire « que le choix 5 (a) nomme ».
- **m-9.** En-tête, conventions et 3.4 : GO-2026-11-20-58 est citée « selon la session principale, 13:30Z ». Elle est maintenant sur la référence locale (`7b436f06`, ligne 589). La citer d'après le registre. Elle dit aussi « second lecteur mistral-large-4-0 », sans condition, ce que le texte ne rapporte pas. Ce n'est pas une contradiction : GO-2026-11-20-43 exige l'essai.
- **m-10.** Note seulement, partie 5 : « 55 » titres. J'en compte 54 dans chacun des deux brouillons, comme la vérification du brouillon 40.

## 1. Fidélité aux mots de Lazar

**DeepSeek est retiré partout.** 24 mentions sur 17 lignes : 3, 8, 179, 263, 489, 503, 506, 508, 519, 1246, 1432, 1433, 2394, 2399, 2416, 2417, 2431. Chacune est de l'histoire, le nom de fichier de la recherche, une phrase qui dit « hors du bras » ou une interdiction (règle 6, ligne 519). Aucune ne fait lire ni juger DeepSeek. 6.11 (ligne 924) n'a plus de file DeepSeek.

**L'essai d'admission sur la seule file Mistral est fidèle.**
- GO-2026-11-20-43 veut un essai sous une règle scellée avant lecture. La pièce `93cbc6f4…` (ligne 18) lit : « second lecteur s'il « tient » à l'essai de mesure sur sa seule file, sous le critère inchangé ». Le texte écrit exactement cela : règle 1, 24 lectures, au moins 22 conformes, le critère du devis, section 7.2.
- Le choix 5 (a) n'a plus de départage à faire. Le compte des réponses étayées est mesuré et rapporté, hors de toute règle (ligne 512). C'est la lecture de la pièce (ligne 19).
- « Ne tient pas » rend le rôle à Lazar (règle 5). Fidèle.

**Identifiant figé (3 (b)).**
- Plus rien n'admet un alias. « alias » ne reste qu'aux lignes 3, 505, 1453 (pour dire qu'aucun n'est admis), 2401 et 2422 (histoire). « version affichée » ne reste qu'en 14.52 (ligne 2401). La version « constatée » sur une page du service est retirée.
- **Aucun déclencheur neuf ne reste sous 8.2, A10, A12 ou A17 pour les lecteurs.** Le nom servi relevé à chaque appel est la « chaîne de version » que 8.2 compare déjà à la configuration. C'est un report de 8.2, non un déclencheur neuf. A10, A12, A17 et 8.2 sont identiques au brouillon 40 (section 7.2 et 8.2 inchangées, par programme). La pièce `93cbc6f4…` (ligne 11) veut que « version figée et inscrite » et A12 restent telles quelles : c'est le cas (lignes 493 et 982).
- **La correction 1 du brouillon 40 est levée** pour les lecteurs.
- Reste le juge : voir C-2. Et l'admission de Neon sous 3 (b) repose sur « c go », à dire (m-3).

**Neon juge des ancres est porté partout où il le faut, et seulement là.** 32 mentions sur 20 lignes : en-tête (3, 8, 185), conventions (263), 3.4 (489, 493, 503 à 505, 515, 518, 522), 6.3 (d) (725), 6.11 (922), 12 (1246), préambule de 13 (1419), 13.1 (1432, 1433), 14.53 (2412, 2420). Il ne prend aucun rôle de lecteur. La déclaration « de la famille de Carbon, sans concevoir de modes » est celle de la pièce `6ebab24f…` (ligne 9). Mais « s'il tient au sien » n'est pas dans les mots (C-3).

**Ce que le texte dit des relevés.**

| point | relevé | texte | jugement |
|---|---|---|---|
| forme « majeure et mineure fixées » | Mistral, ligne 6 | ligne 505 | fidèle |
| « Silent updates: No » | Mistral, ligne 6 | ligne 505 | fidèle |
| aucune garantie écrite sur les poids | Mistral, lignes 6 et 13 | ligne 505 | fidèle |
| non essayé contre l'API | Mistral, ligne 10 | ligne 505 ; vérification de la clé | fidèle |
| identifiant dans l'adresse seulement ; « mistral-large-4+2 » | Mistral, ligne 7 | absent | m-4 |
| `reasoning_effort` à `high`, le plus haut | recherche `f7090b5d…`, ligne 17 (non dans le relevé) | lignes 493, 504, 1433 | fidèle à la recherche |
| nom « stable », « usually don't change » | Google, lignes 6 et 13 | ligne 505 | fidèle |
| « aucun identifiant numéroté n'existe » | Google, ligne 10 : « non trouvé » | ligne 505 | **plus que le relevé** (C-1) |
| `thinking_level` le plus haut, `xhigh` | Google, ligne 15 | lignes 493, 504 | fidèle |
| température ignorée | Google, ligne 15 | ligne 493 : non envoyée | fidèle |
| offre payante | Google, ligne 14 | lignes 493, 504 | fidèle |
| sortie le 18 novembre ; absent de Vertex AI | Google, ligne 13 | absent | m-4 |
| non opposables (R7) | les trois | lignes 185 à 188, 493, 505, 1433 | dit partout |

## 2. Règles

**Contrôles de la note, refaits par programme :**

| contrôle | mon résultat | concorde ? |
|---|---|---|
| hypothèse, prédiction, métrique, seuil | identiques | oui |
| 7.1 à 7.8 | identiques | oui |
| section 10 | identique | oui |
| section 12 | 1 ligne changée sur 171 (sans le titre) : 1246, marque ajoutée en fin de ligne ; le reste de la ligne, la fiche, l'option γ et la marque du brouillon 40, mot pour mot | oui (la note compte 172 avec le titre) |
| 6.3 | 1 ligne (725) : le nom du juge à l'étape (d) ; l'ordre ne change pas | oui |
| 8.4 | 1 ligne (1108) : la phrase sur le programme retirée ; « n'est pas éprouvé ici » et le renvoi à 8.7 restent | oui |
| autres sections | en-tête et conventions (10 lignes changées, 9 neuves) ; 3.4 (480, 484, 485 changées ; bloc de 19 lignes devenu 22) ; 6.11 (3) ; préambule de 13 (2) ; 13.1 (3 cases) ; 13.2 (4 cases) ; 14 (26 neuves) ; contre-lecture (2). Toutes les autres : identiques | oui |
| titres | 54 et 54 ; seul le titre de niveau 1 change | oui (la note écrit 55 : m-10) |
| consignes figées | blocs de 3.2 (lignes 390 à 415) et de 3.3 (lignes 437 à 471) : `98a9bd34d280…` et `ecf590eae0c0…`, égales au brouillon 40 et à 13.1 (ligne 1435) | oui |
| marques des cases | 7 lignes, toutes en 13.1 (1430, 1432, 1433, 1436, 1441, 1442, 1443), 8 occurrences ; mêmes cases qu'au brouillon 40, décalées de 12 | oui |
| validateur `problemes()` | brouillons 40 et 41 : les deux mêmes problèmes attendus (marque hors des sections exigées ; contre-lecture 10 sans ses deux empreintes) | oui |
| table d'en-tête | 241 lignes à empreinte entière. 15 sautées par mon filtre, la ligne de la pièce sans interne comprise (relue par `git show` : égale). 24 de code non recalculées (aucun module ouvert). 1 absente du disque (ligne 179), vérifiée par `git show` : `f7090b5d…`, égale. **201 recalculées, toutes égales.** Voir « Écarts » pour la ligne 209 | oui, à l'écart près |

**Une règle de jugement, un seuil, une issue ou une prédiction change-t-il ?**
- Dans les sections qui en portent : **non**.
- Hors d'elles, deux seuils neufs de procédure : « huit sur huit » pour le juge (règle 2), et « un seul nom servi sur la file » (règle 3). Ni l'un ni l'autre n'entre dans une variable, un seuil ou un verdict de l'expérience. Le premier est posé à Lazar ; voir C-3.
- Une phrase prête au texte une issue qu'il n'a pas, pour le juge des ancres (C-2). Elle ne change aucune issue, mais elle dit que l'une existe.

## 3. Les corrections 2 et 3 du 40, et les mineurs

| point | où, au brouillon 41 | jugement |
|---|---|---|
| C-2 : sortie maximale envoyée, compteurs | 3.4, ligne 511 : fixés au devis des essais, contre-lu, avant tout envoi ; « réflexion comprise » ; fin par sortie maximale lue sur le motif de fin ; rien ne change après le premier envoi ; règle 7 : ce que la sortie maximale du service borne, constaté au devis. « sans choix de la session » retiré (ligne 493) | **fidèle** (voir m-1 pour la règle 8) |
| C-3 : vérification de la clé | 3.4, ligne 509 : appel minimal sous sa ligne ; saine si code 200 et nom servi égal à l'identifiant ; un échec n'est pas « ne tient pas » ; cause corrigée, vérification refaite sous une ligne neuve ; règle 4 : « ne tient pas » ne se dit que d'une file partie ; clés `MISTRAL_API_KEY` et `GEMINI_API_KEY` | **fidèle.** `GEMINI_API_KEY` est bien la variable de la file Carbon dans la configuration de l'essai de mesure (`e047c502…`). Après une vérification saine, une panne au premier envoi donne encore « ne tient pas » (règle 1) ; l'effet est un nœud, non un autre modèle : acceptable |
| m-1 | 8.4, ligne 1108 | **fidèle** |
| m-2 | 13.1, ligne 1443 | **sans objet, vraiment** : la formule a disparu ; l'attestation est rendue ; il reste, de prudence, que le lecteur habilité dise si elle lui suffit (réserve 7 du rédacteur). Je garderais ce reste : l'attestation est écrite par l'auteur du code |
| m-3 | en-tête, ligne 8 | **fidèle** : GO-2026-11-20-38 et la phrase principale de GO-2026-11-20-43, avec « deux clés », sont à la lettre (vérifié par programme contre les lignes 569 et 574) |
| m-4 | 13.2, ligne 1450 | **fidèle** ; le coût projeté n'est plus un critère, il est rapporté (ligne 512) |
| m-5 | — | **sans objet, vraiment** : « ordre fixe » ne reste qu'en 14.52 (ligne 2396) |
| m-6 | note, partie 4 | **sans objet pour l'essentiel** : les trois questions sont tranchées par « 1a 2a 3b4c 5a » ; la condition d'envoi couvre Mistral et Google ; le banc de huit entrées du juge, lui, est neuf et non confirmé (C-3, m-8) |

## 4. Les ajouts du rédacteur

| ajout | nature | jugement |
|---|---|---|
| **essai d'admission du juge, huit lectures, huit sur huit** | **choix neuf, qui demande le mot de Lazar** | Ni « c go » ni GO-2026-11-20-58 ne le portent (C-3). Les huit entrées sont bien celles de la file GPT : six d'appariement, deux de couverture (configuration `e047c502…`, `files.gpt.entrees`). Les huit lectures servent de toute façon à la règle 7 et au chiffrage ; c'est la **règle** qui est neuve. Elle ne mesure que la forme, sous les consignes des lecteurs. |
| **nom servi autre que l'identifiant, à la vérification de la clé : nœud** | **procédure**, juste | C'est la lecture stricte de 3 (b) : l'identifiant figé n'est établi contre le service que si le service le rend. Dire qu'un autre nom « revient au même » serait un choix ; le nœud le rend à Lazar. Risque réel : la fiche de Mistral affiche aussi `mistral-large-4` (recherche `f7090b5d…`, ligne 13). Pas de trop. |
| **un seul nom servi sur toute la file** | **procédure**, report de 8.2 à l'essai | Le brouillon 40 portait déjà « une seule chaîne de version », jugé recevable. Pas de trop. |
| **modèle non admis : file non partie, nœud** | **procédure** | Plus juste que « ne tient pas » depuis C-3 ; même effet. |
| **condition d'envoi des textes, en case** | **choix neuf, qui demande le mot de Lazar**, bien rangé | Posé (question 1). Le préambule de 13 exige le mot de Lazar avant les files. Une phrase de 3.4, « s'il en veut une autre, elle remplace celle-ci », pourrait laisser croire qu'elle vaut sans réponse ; l'ordre de 13 le corrige. |

**La réserve 4 du rédacteur.**
- Il a raison de ne rien ajouter seul : une issue neuve allonge 8.2, section gelée.
- Mais le trou est plus large que le retrait entre les deux parties des ancres. Tout changement du nom servi du juge pendant les ancres est sans issue écrite. Et 3.4 et 13.2 disent le contraire (C-2).
- Ce n'est pas né au brouillon 41 : la même phrase valait pour Astra, puis pour le candidat non retenu.
- Il faut le poser à Lazar, avec une recommandation. La plus prudente : le jugement des ancres s'arrête, rien n'est lu, nœud.

## 5. Réponses du développeur habilité

Confrontées à la pièce `e2f246eb…`, par `git show` seulement.

| point | pièce | texte (ligne) | jugement |
|---|---|---|---|
| module v11, préparation v3 | lignes 9 à 11 : v11 `e1130dad…`, essais `92711976…`, préparation v3 `c0021298…` ; seule l'empreinte inscrite change ; v2 tirait 32 positions sur 80 ; le juge lit toutes les actions ; au plus 6 400 | 1443 | **fidèle**, sauf « cite » pour « à changer » (m-6). La contre-lecture habilitée de la v11 est un reste du rédacteur, dit comme tel |
| attestation v7 à v10 | ligne 42 | 1443 | **fidèle, en moins** : « au bit près (douze lectures) » et « quelle que soit la statistique retenue » sont omis ; rien n'est ajouté |
| lanceur en trois sous-commandes | ligne 25 | 1460 | **fidèle** ; la phrase « il enchaîne… » gardée à la lettre, avec sa lecture |
| version qui fait foi, v1 comme histoire | non dans la pièce ; journal OD-247 (ligne 266) : v2 en vérification chez le lecteur habilité, v1 gardée comme histoire | 1460 | **fidèle au complément de 13:30Z**, cité comme tel |
| décision sur la ligne de configuration de la base | pièce : « Point à trancher » ; journal OD-237 (ligne 256) : « décision de la mère » | 1460 | **fidèle sur le fond** ; source à citer (m-7) |
| dossier des rangs | lignes 33 à 35 | 1443, 1460 | **fidèle** ; le « si » de la ligne 35 est levé par la relecture de la garde, OD-237 |

**Aucun interne de moniteur n'est passé dans le texte par le brouillon 41.** Les lignes neuves ne portent que des chemins et des empreintes de pièces internes, comme la pièce les donne, et ce que la pièce dit en clair. Aucun seuil, trait, vocabulaire, poids ni texte de consigne.

## 6. Registre (référence locale `7b436f06`, sans appel réseau)

- **GO-2026-11-20-58** (ligne 589) : **présente.** Citée correctement : `gemini-4-neon` juge les deux ancres, remplace GO-2026-11-20-48, renvoie à la pièce `6ebab24f…`. Heure de la ligne : « c go » lu à la source à 13:27:26Z. Elle dit aussi « second lecteur mistral-large-4-0 » et « DeepSeek n'est plus utile au bras A » (m-9).
- GO-2026-11-20-31 (ligne 562), -38 (ligne 569), -43 (ligne 574), -47 (ligne 578), -48 (ligne 579) : citées correctement. -38 et -43 sont à la lettre (programme).
- **Le mot « 1a 2a 3b4c 5a » n'a pas de ligne.** Aucune ligne ne porte « 3b4c », la pièce `93cbc6f4…`, ni « cinq choix ». Le texte laisse cet identifiant à inscrire (ligne 1433) : juste.
- **Une ligne nomme-t-elle GO-2026-11-19-97 hors la sienne ? Non** (seule la ligne 530).

## 7. Les deux questions pour Lazar

| question | options | recommandation | jugement |
|---|---|---|---|
| 1. condition d'envoi des textes à Mistral et à Google | (a), (b), (c), avec avantage et inconvénient | (b), confiance moyenne ; défaut : nœud | **bien posée.** Deux précisions à ajouter : (i) le texte exige la condition avant même les essais d'admission, qui n'envoient que des textes synthétiques ; Lazar peut vouloir laisser partir les essais avant ; (ii) pour Google, aucun relevé ne dit encore que l'offre payante exclut l'entraînement : c'est un constat à faire. |
| 2. seuil de l'essai du juge | (a) 8 sur 8, (b) 7 sur 8, (c) 24 entrées, 22 sur 24 | (a), (c) aussi bonne ; défaut : nœud | **bien posée pour le seuil, mais incomplète.** Elle tient l'essai pour acquis. Il manque l'option : pas de règle d'admission ; huit lectures pour la sortie maximale et le chiffrage seulement, comme pour Astra ; Neon juge par « c go » (C-3). « Quelques dollars au pire » pour (c) n'a pas de source chiffrée : donner le calcul. |

**Manque-t-il une question ? Oui : le changement de version du juge pendant les ancres** (C-2). Options possibles : (a) arrêt du jugement des ancres, rien lu, nœud ; (b) rien n'est écrit, le changement est rapporté ; (c) un juge retiré est remplacé sur mot de Lazar, les ancres rejugées sous un addendum. Elle touche 8.2, section gelée : c'est à Lazar.

## Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon41.md` : par différence et par programme ; lignes 503 à 524, 1432, 1433, 1450, 1453, 1457, 2412 à 2437, 2449 et 2450 (début), 209, 210, 247 et 34 (texte de la ligne seulement), 1057 à 1069, des extraits des lignes 1443 et 1460, et des recherches de chaînes dans ce seul fichier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon40.md` : par différence et par programme ; lignes 494 à 512.
- En entier : la note du brouillon 41 ; la vérification du brouillon 40 ; les trois pièces des mots de Lazar ; les trois relevés documentaires.
- `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` : lignes 253 à 267 ; une recherche des seuls identifiants OD-2xx, qui a affiché leurs numéros de ligne.
- Par `git show origin/main:` : `registres/go.md`, lignes 465, 530 (début), 562 (début), 569, 574, 578 à 591, et des recherches de chaînes ; `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md`, en entier ; `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md`, une recherche de chaînes (lignes 13, 17, 19, 21, 22, 36 à 38, 68, 69, 74, 83, 86, 103, 119, 121, 148, 162, 163 affichées, en partie).
- `docs/notes/relance-organismes-discrets-v1/essai-mesure-lecteurs-bras-a-v1/configuration-essai-mesure-lecteurs-bras-a-v1.json` (`e047c502…`) : les blocs `files.gpt` (relais, modèles, réglages, entrées) et les arguments du relais de `files.carbon`, par programme ; une recherche de « env », « cle », « key », qui a affiché les lignes 42, 70, 157 à 159, 162, 180, 181, 192 et 216.
- Fichiers de la table d'en-tête : 201 lus en octets pour l'empreinte seulement.
- `controle_ia.prereg` : exécuté, non lu ; noms des constantes et signature de `problemes` affichés par introspection. `controle_ia.scellement` : exécuté.

## Écarts

- **Un franchissement, déclaré.** Ligne 209 de la table d'en-tête : `docs/sources/invites-2606.08892-v1/derivees/H12-par-action-v1.txt`, « consigne des deux moniteurs à modèle de langue ». Le chemin n'est pas dans la liste cloisonnée, mais c'est un interne de moniteur ; sa copie, ligne 207, est sous `docs/notes/bras-a-moniteurs-v1/`. Mon filtre ne l'a pas sautée : **j'en ai pris l'empreinte, en octets**, égale à celle du texte. Rien n'est affiché ni lu. C'est sans doute la seizième ligne sautée par le rédacteur : mon compte de 15 sautées et 201 recalculées s'explique par elle.
- **Débords mineurs, déclarés** :
  - j'ai pris aussi en octets l'empreinte de la ligne 247, `prereg/T0.6-organismes-config-7b-v1.json`, qui touche T0.6 sans être dans la liste ; et celles des lignes 34 et 210, des textes transmis par la session principale, rangés dans le dossier de la relance ;
  - un `sha256sum` par motif a pris l'empreinte d'une pièce que la tâche ne nommait pas, `mots-de-lazar-juge-et-point-19-bras-a-2026-11-20-v1.md` (`2845ca37…`), dans le dossier de la relance, sans la lire ;
  - j'ai lu deux fichiers non nommés par la tâche, hors cloisonnement : la recherche de la session principale (par `git show`, recherche de chaînes) et la configuration de l'essai de mesure (blocs nommés plus haut). C'était pour vérifier `reasoning_effort`, les huit entrées et `GEMINI_API_KEY`.
- Aucun accès à un autre chemin cloisonné. Aucun module de code ouvert. Aucune réponse ni aucun envoi d'essai ouvert.
- Aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. `registres/`, `.claude/` et le journal ne sont pas touchés. Fichiers écrits : celui-ci, et des fichiers de travail dans le bloc-notes de la session.
