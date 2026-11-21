# Vérification du brouillon 42 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf. Je juge ; je ne corrige rien. Ni scellé ni committé. Écrit le 2026-11-21, vers 11:05Z (`date -u`).
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon42.md`, `c5dbd28eca7b2a244a494400ae0180bcace68b76d3861d7e35822decd68ef0de`, 2 479 lignes.
- **Pièces, compagnons vérifiés** (`python -m controle_ia.scellement verifier`, tous « OK ») :
  - la note du rédacteur, `preenregistrement-v2-brouillon42-note-v1.md`, `67f554f9eddc…` ;
  - le brouillon 41, `cb6ca087d3d4…` (2 452 lignes) ; la vérification du brouillon 41, `41332e20009b…` ;
  - les mots de Lazar : « b a b go » (`00af2aa83604…`) ; « 1a 2a 3b4c 5a » (`93cbc6f4c78d…`) ; « c go » (`6ebab24f009b…`) ;
  - les trois relevés : conditions d'envoi (`b959c4d0db2e…`), identifiant de Mistral (`b8163cc99290…`), identifiant de Google (`ac8bb15e1cfc…`).
- **Registre** : `git show origin/main:registres/go.md`, tête locale `e77fa0d9`, sans appel réseau ; 636 lignes ; empreinte de cette lecture `65ba1a9730ea…`. Par rapport à la tête `761710a7` lue par le rédacteur (630 lignes), six lignes sont ajoutées à la fin (631 à 636), rien d'autre ne change.
- **Journal** : pas de compagnon ; empreinte calculée `e221bd051bc7…` ; lignes 268 à 273 (OD-249 à OD-255).
- **Méthode** : différence des brouillons 41 et 42 par programme, section par section sous les 54 titres, puis mot par mot sur chaque ligne changée ; lecture entière du bloc 3.4 neuf (lignes 508 à 526), des cases changées de 13, 13.1 et 13.2, de 14.54 ; empreintes des consignes figées, marques, table d'en-tête restreinte, validateur, par programme ; chaque phrase neuve confrontée au mot de Lazar et au relevé.

## Verdict : **engageable après corrections**

- Le mot « b a b go » est porté, fidèlement, en 3.4, 13, 13.1, 13.2 et 14.54. Les trois corrections du brouillon 41 sont levées. Les dix mineurs sont traités.
- **Aucune règle de jugement, aucun seuil, aucune issue des sections gelées, aucune prédiction ne change.** Les contrôles de la note concordent, refaits par programme.
- Deux retouches restent : une constatation datée que le registre a dépassée, et un cas laissé ouvert dans le repli de Mistral sur le point d'accès global.

**Corrections :**
- **C-1. Les deux mots ont maintenant leur ligne au registre ; le texte dit le contraire.** À la tête `e77fa0d9` : GO-2026-11-21-32 porte « 1a 2a 3b4c 5a » (ligne 631, renvoi à `93cbc6f4…`) ; GO-2026-11-21-33 porte « b a b go » (ligne 632, renvoi à `00af2aa8…`). Toutes deux sont fidèles à leur pièce. Le texte écrit « aucune ligne ne les porte à la tête `761710a7` » : en-tête, ligne 8 ; case « lecteurs et juge des ancres » de 13.1, ligne 1438 (« sont à inscrire ici ») ; la note, partie 6, dit de même. C'était vrai à sa date ; ce ne l'est plus. Inscrire les deux identifiants, lus à la tête `e77fa0d9`, en 13.1 et à l'en-tête.
- **C-2. Repli de Mistral sur le point d'accès global : un cas reste sans issue écrite.** 3.4, ligne 513 : européen retenu « s'il rend le code 200 et le nom servi demandé » ; repli sur le global « s'il ne sert pas ce modèle ». Ligne 514 : en règle générale, « nom servi autre que l'identifiant demandé » est un nœud ; l'exception ne vise que « ne sert pas ».
  - Cas ouvert : le point d'accès européen rend le code 200 avec un autre nom servi (par exemple `mistral-large-4`, que la fiche affiche aussi). Repli sur le global, ou nœud ? Le texte ne le dit pas. La session choisirait après l'appel.
  - Aucun signe n'est fixé non plus pour « ne sert pas ce modèle » (code de retour, message d'erreur).
  - Écrire : (i) que ce cas est un nœud de Lazar, comme dans la règle générale. C'est la lecture étroite du mot « s'il sert `mistral-large-4-0` » ; elle n'étend pas le repli. (ii) Que le devis des essais fixe, avant tout appel, le signe qui dit « ne sert pas ce modèle ».

**Mineurs :**
- **m-1. La garde qui arrête le juge n'est pas dite éprouvée (R5) dans le texte.** La note (partie 6) veut que le programme des essais et celui des ancres portent l'arrêt sur un nom servi différent, éprouvé sur un cas sain et sur un artefact. Le texte ne le dit ni en 3.4 ni en 13.2. 8.4 est gelée : l'écrire en 3.4, ou à la case « version des modèles » de 13.2.
- **m-2.** 3.4, ligne 513 : l'exclusion de l'entraînement chez Mistral est dite « hors les retours et les modèles en aperçu ». Le relevé (ligne 12) écrit « retours, modèles « Labs » ou « Preview » ». Ajouter « Labs ». Aucun effet : Large 4 est en disponibilité générale.
- **m-3.** 3.4, ligne 510 : « que je n'ai pas rouverte ». Dans un texte qui sera scellé, écrire « que le rédacteur n'a pas rouverte ».
- **m-4. Note, question 1 : le défaut « (a), sans délai ».** Le format de décision veut un défaut sous 48 heures. Comme (a) n'écrit rien, mieux vaut dire qu'aucune décision n'est demandée maintenant (voir la question 5).

## 1. Fidélité au mot « b a b go », ni plus ni moins

**Choix 1 (b), essai d'admission du juge.**
- Porté en 3.4 (ligne 508 : source de chaque essai ; ligne 520 : règle 2), en 12 (marque ajoutée), au préambule de 13, en 13.1 et en 14.54.
- Huit lectures sur les huit entrées de l'ancienne file du juge ; huit sur huit de forme conforme ; sinon nœud (règle 5). C'est le mot.
- **C-3 est levée par le mot.** Le texte dit d'où vient chaque essai : celui du second lecteur, du mot « 1a 2a 3b4c 5a » et de GO-2026-11-20-43 ; celui du juge, au brouillon 41, d'une procédure de la session, désormais du choix 1 (b). Le texte reconnaît aussi que GO-2026-11-20-58 désigne le juge sans condition.

**Choix 2 (a), version du juge qui change pendant les ancres.**
- Écrit en 3.4 (ligne 510) et à la case « version des modèles » de 13.2 (ligne 1458) : la file du juge s'arrête ; aucune ancre jugée n'est lue ; nœud de Lazar. Issue de procédure, « ni une ligne de 8.2 ni de la liste d'arrêt ».
- **Aucune section gelée n'est touchée** : 6.3, 8.2, 8.4, 8.5 et la ligne A12 sont identiques au brouillon 41 (par programme). Le mot le veut.
- **C-2 du brouillon 41 est levée** :
  - 3.4 et 13.2 disent que 8.2 et A12 ne visent que les lecteurs ;
  - aucun renvoi du juge à 8.2 ou à A12 ne reste hors des phrases qui le nient et de l'histoire (recherche par programme : seules les lignes 3 et 510 associent le juge à 8.2 ou A12, pour dire qu'elles ne le visent pas).
- Le déclencheur est bien borné : nom servi à un appel du juge, à l'étape (d) ou (e′) de 6.3, autre que celui de la configuration. Ce sont les deux seules étapes où le juge est appelé (6.3, lu). Un changement survenu entre (d) et (e′) se voit au premier appel de (e′).

**Choix 3 (b), conditions d'envoi.**
- En 3.4 (ligne 513) et en 13.1 (ligne 1438), mot pour mot :
  - Google : offre payante (projet avec un compte de facturation actif), partage des journaux désactivé, journaux à 7 jours ;
  - Mistral : offre payante, refus de l'entraînement activé, point d'accès européen s'il sert `mistral-large-4-0`, sinon global, déclaré.
- Constatées et datées avant le premier envoi, essais compris ; réglages par Lazar ; aucune dépense ouverte. Options écartées rapportées.
- **Réserves du relevé, confrontées ligne à ligne** :
  - 3.4 les reprend toutes : conservation sans durée trouvée (relevé, ligne 7) ; aucune non-conservation (lignes 8 et 14) ; aucun choix de région chez Google (ligne 9) ; Large 4 sur le point d'accès européen non vérifié, données de gestion non couvertes, 1,1 fois le prix (ligne 15) ; réglage par défaut du bouton non trouvé (ligne 12) ;
  - exclusion de l'entraînement non opposable : dite. Seul écart : « Labs » omis (m-2) ;
  - 13.1 en reprend trois et renvoie à 3.4 : suffisant.

**Ce qui dépasse la lettre du mot.** Chaque ajout est une procédure qui le met en œuvre ; aucun n'est un choix neuf :
- constat « scellé » et inscrit en 13.1 : R6 ;
- réglages constatés avant la vérification de la clé, et non seulement avant le premier envoi : plus prudent ;
- point d'accès retenu inscrit et inchangé ensuite : supprime une liberté de la session ;
- marque en section 12 : elle n'ajoute rien que 3.4 ne porte. Le rédacteur la dit retirable ; je la tiens pour recevable.

**Ce qui manque.** Le cas de C-2 seulement.

## 2. Règles

**Contrôles refaits par programme :**

| contrôle | mon résultat | concorde avec la note ? |
|---|---|---|
| titres | 54 et 54 ; seul le titre de niveau 1 change (41 → 42) | oui |
| hypothèse, prédiction, métrique, seuil | identiques | oui |
| 7.1 à 7.8 | identiques | oui |
| 10, 9, 11 | identiques | oui |
| 6.1 à 6.12 | identiques (6.3 comprise) | oui |
| 8.1 à 8.7 | identiques (8.2, 8.4, 8.5 comprises) | oui |
| section 12 | 171 lignes sous le titre, 171 ; **une seule ligne changée** (1251 au brouillon 42, 1246 au 41) : l'ancienne ligne est un préfixe exact de la neuve (1 567 caractères, puis 600 ajoutés en fin, la « marque du brouillon 42 »). **Aucun mot existant changé ; aucune ligne neuve** : c'est un ajout à une ligne, non une ligne ajoutée | oui |
| autres sections | en-tête : 7 lignes changées et 5 neuves, plus le titre ; 3.4 : 8 lignes changées (494, 508, 510, 512, 513, 514, 520, 526) ; préambule de 13 : 2 ; 13.1 : 3 cases (1437, 1438, 1448) ; 13.2 : 2 cases (1458, 1465) ; 14 : 3 lignes de 14.53 et 22 neuves (14.54) ; contre-lecture : 2 | oui |
| consignes figées | 3.2, lignes 395 à 420 : `98a9bd34d280…` ; 3.3, lignes 442 à 476 : `ecf590eae0c0…` ; égales au brouillon 41 | oui |
| marques des cases | 7 lignes, 8 occurrences, toutes en 13.1 (1435, 1437, 1438, 1441, 1446, 1447, 1448 ×2) ; mêmes cases qu'au 41, décalées de 5 | oui |
| validateur `problemes()` | brouillons 41 et 42 : les deux mêmes problèmes (marque hors des sections exigées ; contre-lecture 10 sans ses deux empreintes) | oui |
| table d'en-tête | 246 lignes à empreinte entière (241 au 41, plus 5 neuves) ; seule la description de la ligne 189 change. **Recalculées, sous ma consigne restreinte : 181, toutes égales** (lignes de la relance, du dossier `prereg/T0.7-organismes-discrets-v-a-v2-*`, du dossier sans interne, et les six lignes 189 à 194). 1 absente du disque (ligne 179), vérifiée par `git show origin/main:` : `f7090b5d…`, égale. **64 non recalculées** par consigne (sources, configurations de T0.6, code, chemins cloisonnés, autres dossiers) | oui, sur ce que j'ai recalculé |

**Une règle de jugement, un seuil, une issue des sections gelées ou une prédiction change-t-il ? Non.**
- Hors d'elles, aucun seuil neuf. « Huit sur huit » existait au brouillon 41 ; il est maintenant un mot de Lazar.
- L'issue neuve du juge est une issue de procédure, écrite hors des sections gelées, sur le mot de Lazar. Elle n'entre dans aucune variable ni aucun verdict de l'expérience.

## 3. C-1 et les dix mineurs du brouillon 41

| point | où, au brouillon 42 | jugement |
|---|---|---|
| C-1 « n'existe » | 3.4, ligne 510 : « n'a été trouvé », avec la raison | **levée** |
| C-2 juge renvoyé à 8.2 et A12 | 3.4, ligne 510 ; 13.2, ligne 1458 | **levée** (partie 1) |
| C-3 essai du juge attribué à tort | 3.4, ligne 508 ; règle 2 ; 12, marque ; 13.1 | **levée par le mot** |
| m-1 « aucune liberté » | règle 8, ligne 526 : remise, et le retrait dit | fidèle |
| m-2 rien ne retenait la file du juge | règle 2, ligne 520 ; préambule de 13, ligne 1425 | fidèle ; le mot étant donné, la phrase dit ce qui reste : conditions, devis, ligne, clé |
| m-3 Neon admis sous 3 (b) | 3.4, ligne 510 ; 13.1 ; 13.2 | fidèle à `6ebab24f…`, ligne 9 (« plus faible que celle de Mistral et non absolue ») |
| m-4 réserves des relevés | 3.4, ligne 510 | fidèle aux relevés `b8163cc9…` (ligne 7) et `ac8bb15e…` (ligne 13) ; `mistral-large-4` repris de la vérification du 41, dit comme tel ; « je » à reprendre (m-3) |
| m-5 point d'accès européen | 3.4, ligne 513 ; 13.1, ligne 1438 | fidèle au mot ; voir C-2 |
| m-6 « cite » → « devra citer » | 13.1, ligne 1448 ; 14.53, ligne 2438 | fidèle |
| m-7 source de la décision du lanceur | 13.2, ligne 1465 : OD-237, et « Point à trancher » | fidèle |
| m-8 choix 5 (a) | 14.53, ligne 2436 | fidèle |
| m-9 GO-2026-11-20-58 au registre | en-tête, ligne 8 ; 3.4, lignes 494 et 508 ; 13.1, lignes 1437 et 1438 ; 12, marque | fidèle : la citation de la ligne 589 est à la lettre (vérifiée à `e77fa0d9`, ligne inchangée). Les quatre « selon la session principale, 13:30Z » restants (lignes 3, 8, 1251, 2417) sont de l'histoire du brouillon 41 : recevable |
| m-10 54 titres | note | fidèle |

## 4. Ajouts et réserves du rédacteur

| ajout | nature | jugement |
|---|---|---|
| **« modèle inconnu » sur le point d'accès européen : repli sur le global, sans nœud** | **procédure** | Le repli est dans le mot (« sinon point d'accès global, déclaré »). Le texte ne fait que dire comment « s'il sert » se constate. Le second « modèle inconnu », sur le global, reste un nœud : juste. Mais le cas « code 200, autre nom servi » sur le point d'accès européen n'est pas tranché : C-2. Une panne ou un refus de clé reste « cause corrigée, vérification refaite » : la règle générale le dit déjà, il n'y a rien à ajouter. |
| **point d'accès constaté à la vérification de la clé** | **procédure** | C'est la seule façon de constater « s'il sert ». La vérification n'envoie aucun texte d'essai ni de course. Le texte exige de plus que les réglages des comptes soient constatés avant elle : plus strict que le mot. Elle a sa ligne de calcul, et une ligne de plus en cas de repli : dit en 13 et dans la note. **La réserve 1 du rédacteur tient.** |
| **« aucune ancre jugée n'est lue », écrit « à partir de l'arrêt »** | **procédure, lecture nécessaire** | Une lecture faite avant l'arrêt ne se défait pas. Le texte ne restreint pas le mot : il nomme « ceux que le juge a rendus sous le nom inscrit compris ». Il dit la limite (étape (e′)) et la renvoie au nœud que le mot ouvre déjà. Ce n'est pas un choix neuf. |
| **règle 2 : ses conditions du brouillon 41 au-delà de « huit sur huit »** | **procédure** | Code 200, reprise unique, aucun refus, aucune fin par sortie maximale, plafond, et (règle 3) un seul nom servi. Ces conditions étaient au texte sur lequel Lazar a répondu ; elles sont celles de la règle 1 et du devis (7.2). Une réponse absente ou refusée n'est pas de forme conforme. Une réponse coupée par la sortie maximale pourrait l'être, sur le papier : la condition est donc un peu plus stricte que la lettre du mot. Mais elle est dans le sens de la prudence, et le texte n'attribue au mot que « huit sur huit ». Recevable. **Réserve 3 du rédacteur : je la partage.** |

Les autres réserves de la note :
- réserve 2 : recevable, sous C-2 ;
- réserves 4 et 5 : voir ci-dessus et la partie 2 ;
- réserves 6 à 8 : dites dans le texte ;
- réserve 10 : l'identifiant de session de l'en-tête. Je ne l'ai pas vérifié ; hors de ma question.

## 5. La question pour Lazar

**Bien posée sur le fond.**
- Le trou est réel. Par 6.3, l'étape (e) calcule et scelle ses critères « ancres de (d) comprises », avant (h1) puis (e′).
- Un arrêt à (e′) laisse donc des jugements d'ancre déjà employés par programme. Un arrêt à (d) n'en laisse aucun : (d) est scellée avant le premier appel d'un lecteur aux lots d'épreuve.
- Les trois options sont justes, et l'inconvénient de (b) est exact : décider d'avance toucherait 6.3 et la section 7, gelées.
- Une nuance sur l'option (c). Lazar a écarté « le rejugement de toutes les ancres sous la version neuve ». Un rejugement par un autre juge sur son mot est une chose voisine, non identique. La note le dit à peu près.

**« Ne rien écrire d'avance » est tenable.**
- Le mot 2 (a) ouvre déjà un nœud. Rien n'avance avant lui : la file du juge est arrêtée, et 6.3 interdit de passer à (f) avant le scellement de (e′).
- Tout ce que Lazar déciderait alors serait un écart à un texte scellé, donc un nœud par la hiérarchie de décision : rien ne se décide hors de lui.
- L'inconvénient, décider en connaissant les critères de (e), est réel mais borné. À ce point, seules sont connues les épreuves de l'instrument sur plans honnêtes et la garde de puissance. Ni les jumeaux, ni la distillation, ni la variable principale.
- Le cas est rare : 152 appels au plus, chiffre de 6.11, sur un nom dit stable.

**Ce que je changerais à la question** (m-4) : la présenter comme une information, sans décision demandée maintenant, plutôt qu'avec un défaut « sans délai ». (a) ne fait rien écrire ; poser une décision dont le défaut est de ne rien faire, c'est une ligne de plus pour Lazar sans enjeu présent.

## 6. Registre (tête `e77fa0d9`, sans appel réseau)

- **« 1a 2a 3b4c 5a » a-t-il une ligne ? Oui** : GO-2026-11-21-32.
- **« b a b go » a-t-il une ligne ? Oui** : GO-2026-11-21-33.
- **Une ligne nomme-t-elle GO-2026-11-19-97 hors la sienne ? Non** (seule la ligne 530).
- GO-2026-11-20-31, -38, -43, -48 et -58 : lignes 562, 569, 574, 579 et 589, inchangées depuis `761710a7` ; -58 citée à la lettre par le texte.
- Lignes 633 à 636 : d'autres chantiers. J'en ai lu le début, juste assez pour les écarter.
- Observation hors du texte : le journal saute de OD-252 (ligne 271) à OD-254 (ligne 272) ; aucune entrée OD-253.

## 7. Prêt pour la contre-lecture 10 ?

**Oui, une fois C-1 et C-2 faites** ; les mineurs peuvent suivre dans le même brouillon.

**Ce qui sépare encore le texte du scellement :**
- **Cases de 13.1 encore marquées** (7 lignes, 8 occurrences) :
  - « nœuds » : l'identifiant de la ligne du mot du 19 novembre, qui ne nomme pas GO-2026-11-19-97 ;
  - « familles » : la confrontation de `mistral-large-4-0` et `gemini-4-neon` à la liste, par le lecteur habilité ;
  - « lecteurs et juge des ancres » : les deux lignes GO-2026-11-21-32 et -33 (C-1) ; le constat daté et scellé des réglages des deux consoles, fait après les réglages de Lazar ; le devis des deux essais (tarifs, dont le point d'accès européen à 1,1 fois ; plafonds ; sortie maximale envoyée ; champs de jetons et de nom servi ; signe de « ne sert pas », C-2), sa contre-lecture par un agent d'un autre modèle, ses lignes de calcul (une par file, une par vérification de clé, une de plus si Mistral se replie sur le global) ; le fichier des règles scellé ; le programme qui conduit les essais, contre-lu, avec ses gardes éprouvées (m-1) ; le relevé des vérifications de clé et le point d'accès retenu ; les deux rapports techniques ; pour chaque rôle, nom servi, réglage, sortie maximale et comptes, ou le mot de Lazar qui pourvoit un rôle non tenu. Règle 6 : pas de scellement tant que les deux rôles ne sont pas pourvus ;
  - « entropie » : l'entier racine, tiré au scellement ;
  - « renvoi de la base » : le rapport du lecteur habilité ;
  - « commit du code » : le commit, par la session qui orchestre ;
  - « module des cinq moniteurs » : la livraison de la version 11 et ce que la case en exige.
- **Côté habilité** : la contre-lecture de la version 11 du module ; la configuration de l'analyse, qui doit citer la version 11 ; la version qui fait foi du lanceur de l'étape de discrétion (version 2, commit `848c17649` selon OD-247), son nom et son empreinte ; le renvoi de la base.
- **Programme des ancres à la course** : il porte l'arrêt du juge sur un nom servi différent, éprouvé sur un cas sain et sur un artefact (m-1).
- **Registre** : les deux lignes existent à `e77fa0d9` ; il reste la ligne du mot du 19 novembre si elle manque (case « nœuds »), et les lignes de calcul des essais.
- **Validateur** : ses deux problèmes attendus disparaissent quand les cases sont remplies et quand la contre-lecture 10 porte ses deux empreintes.

## Fichiers ouverts

- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon42.md` : par programme (différence, sections, empreintes des consignes, marques, table d'en-tête, validateur) ; lignes affichées : 494 (extrait), 508 à 526, 723 à 749 (6.3, lignes tronquées à 900 caractères), 1424, 1425, 1435, 1437, 1438, 1441, 1446 à 1448 (extraits), 1458, 1465 (différence), 2426, 2436, 2438, 2443 à 2464, 2476, 2477 ; en-tête : lignes 1, 3, 5, 6, 8, 9, 62, 189 à 194 (différence) ; recherches de chaînes dans ce seul fichier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon41.md` : par différence et par programme.
- En entier : la note du brouillon 42 ; la vérification du brouillon 41 ; les trois pièces des mots de Lazar ; les trois relevés.
- `docs/notes/relance-organismes-discrets-v1/journal-relance-organismes-discrets-v1.md` : lignes 268 à 273 ; une recherche des identifiants OD-249 à OD-259.
- Par `git show origin/main:` (tête `e77fa0d9`) : `registres/go.md`, lignes 530 (début), 562, 569, 574, 579 (débuts), 589, 631, 632 en entier, 633 à 636 (260 premiers caractères), recherches de chaînes ; différence de nombre de lignes avec `git show 761710a7:registres/go.md` ; `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md`, pour son empreinte seulement.
- Fichiers de la table d'en-tête : 181 lus en octets pour l'empreinte seulement, tous sous `docs/notes/relance-organismes-discrets-v1/`, `prereg/T0.7-organismes-discrets-v-a-v2-*` ou `docs/notes/bras-a-sans-interne-v1/`.
- `controle_ia.prereg` : exécuté, non lu ; noms publics et signature de `problemes` affichés par introspection. `controle_ia.scellement` : exécuté.

## Écarts

- **Aucun franchissement du cloisonnement.** Aucune empreinte prise sur une ligne de la table qui touche un chemin cloisonné, `docs/sources/` ou une configuration de T0.6. Aucun module de code ouvert. Aucun envoi ni aucune réponse d'essai ouverts.
- **Débord mineur, déclaré** : j'ai affiché le début des lignes 633 à 636 du registre, d'autres chantiers, pour les écarter ; je n'en tire rien.
- Aucun appel de modèle ni appel réseau, aucun sous-agent, aucune dépense. `registres/`, `.claude/` et le journal non touchés. Fichiers écrits : celui-ci, et des fichiers de travail dans le bloc-notes de la session (dont une copie du registre lu).
