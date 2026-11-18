# Contre-lecture du projet de feu version 4 de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — v1

**Verdict : « à corriger ».** Sept corrections exigées (C1 à C7), toutes de texte du feu, sans code neuf ni dépense ; onze points mineurs. Le fond est juste : les dix points de l'arbitrage et les onze corrections de la contre-lecture du projet version 3 sont portés, les empreintes et l'arithmétique sont exactes, la commande imprimée par le lanceur au commit de la course est bien celle que le feu reconstruit. Mais sept gestes, joués tels qu'écrits, arrêtent un opérateur sain, laissent passer une création hors de ses fenêtres, ou détruisent la dernière course sur une lecture passagère.

- **Contre-lecteur** : sous-agent neuf, d'une autre lignée (règle R2). Je n'ai écrit ni le projet version 3, ni le projet version 4, ni les pièces de la chaîne version 6, ni l'arbitrage, ni les mesures.
- **Date (`date -u`)** : 2026-11-18, de 06:22Z à 06:40Z environ. Processeur seulement.
- **Pièce lue** : `docs/notes/prealables-course-etape-b-bis-v1/projet-de-feu-v4.md`, `92b1502b95390c0f65a69712b791b6fad30992bdc8532213e976ba066ab8896b`, conforme à son compagnon, non commitée à ma lecture.
- **Commit de la course** : `438a9c5257bdc4fa65f25c42cc89753a049b4586`. Tête du dépôt à ma lecture : `5ba8c2d3`.
- **Pièces lues en appui** : décisions R-3188 et R-3191 ; arbitrage (`688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`) ; troisième addendum scellé (`e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`) ; projet version 3 et sa contre-lecture ; répétition de la mesure du plancher ; lanceur et amorce version 6 ; `src/controle_ia/t07bbis/registre_bbis_v2.py` ; le crochet de garde `.claude/hooks/garde_calcul.py` ; les lignes du registre des accords citées.
- **Cloisonnement tenu** : aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ; rien d'ouvert sous `diag/` ni `runs/` ; aucune branche de données ni de calcul ouverte. Aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue ni affichée, aucun commit, aucune poussée.

---

## 1. Ce que j'ai rejoué, et qui tient

Tout est rejoué dans un dossier jetable du bloc-notes, effacé en rendant.

| geste | ce que j'ai rejoué | issue |
|---|---|---|
| 1 | contenu de `env.sh` extrait du feu par programme | empreinte `8c78b19a897f1d6550d3fd3b3692fad3617d0492583fe5f5397bb15d059e61bf`, égale au feu |
| tous | les 25 blocs de commandes du feu, extraits par programme, passés à `bash -n` | aucune faute de syntaxe |
| 2 (b) | compagnon du crochet | `garde_calcul.py: OK`, `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850` |
| 2 (c) | registre des accords lu par le lecteur du crochet | **toujours** « registre GO mal formé ligne 371 : dates illisibles », code 2, à la tête `5ba8c2d3` : la condition 4 n'est pas levée |
| 2 (e) | commande sans effet que le crochet doit refuser | refusée chez moi (« R10 — arrêt par motif de ligne de commande interdit ») : le crochet est chargé dans ma session |
| 3 | lignes a, b, c, c', empreintes entières, trois compagnons, ligne d, compte des sorties | a, b, c ; 0 fichier non suivi ; quatre empreintes égales au feu ; trois `OK` ; d ; 16. Seul le feu versé manque, comme attendu |
| 5 | les trois programmes extraits du feu | `2d32e1ac…23b4`, `a279a91c…1100`, `1fa46d02…9e09`, égales au feu sur 64 caractères |
| 10, 11 | choix d'offre sur sept offres fabriquées, puis lanceur de la course sur les survivantes, borne du prix relu, garde de dépense | pilotes 615, absent et « 5950.1 » écartés ; prix de 1,4000001 écarté ; stockage écarté ; survivante refusée par le lanceur (`cuda_max_good` en texte) sautée, la suivante retenue ; `PLAFOND_RELU=1.4205` ; garde de dépense code 0 |
| 6 (a), 12 | `bash scripts/lancer_bbis_v6.sh commande` au commit de la course, offre fabriquée d'identifiant 1, jamais louée | code 0, sortie d'erreur de 0 octet, deux lignes, en-tête attendu. Le lanceur a lu le distant en lecture seule (`git ls-remote` : tête de `main`, absence de la branche de sortie) |
| 13 | décodage du base64 de la ligne imprimée ; amorce lue au commit | `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` deux fois ; 41 436 caractères ; ligne imprimée de 41 971 caractères |
| 13 | gabarit de la ligne reconstruite, lu dans le feu et rempli par programme | égal à l'octet à la ligne imprimée |
| 6 (c), 14 | gabarit de la ligne courte, lu dans le feu, variables remplacées par programme | égal à l'octet à la ligne imprimée, dans les deux gestes |
| 15, 16, 23 | lecture de la création, inventaire, relecture, preuve d'absence, sur données fabriquées | conformes ; la clé fabriquée de la réponse n'est jamais imprimée |
| 12 | échéance par commande | 13 heures exactement après l'heure présente ; nom du run accepté par l'amorce |

**Ce que je n'ai pas joué, et pourquoi.** L'égalité des arguments avec un outil factice (gestes 6 (c) et 14) et le geste 13 tel qu'écrit portent le texte d'une ligne de création. Le crochet les refuse aujourd'hui, registre illisible. Je ne l'ai pas contourné : j'ai comparé les gabarits par lecture de texte, sans exécuter aucune ligne de création. Le geste 6 reste la première répétition réelle.

**Outil du loueur, lu sans être exécuté.** J'ai téléchargé le paquet `vastai` 1.8.3 depuis le dépôt des paquets (roue `8c50b291dd92feecc4e0a7eb57b365afe6f9ab719c4d6b4f681d0af367757010`), sans l'installer ni le lancer. Il porte bien :
- `destroy instance` avec `-y` et `--yes`, et une question « [y/N] » sans elle ;
- `logs INSTANCE_ID` ;
- `--cancel-unavail`, `--label`, `--entrypoint`, `--args` (qui avale la fin de la ligne), `--raw` ;
- la clé lue dans `VAST_API_KEY` et envoyée en en-tête, jamais dans l'adresse ;
- `driver_version` et `cuda_max_good` parmi les champs d'offre.
Cela lève une part de la réserve 13 du feu ; le comportement réel reste à voir au geste 4.

**Arithmétique.** 13 × 1,48 = 19,24 ; + 0,96 = 20,20 ; 5,989 + 20,20 = 26,19 ; 39,50 − 26,19 = 13,31. La garde de dépense, jouée au cumul de 26,19 USD, passe (projeté 26,56). **Le pire cas tient sous la coupure.**

**Faits cités, revérifiés.** Les onze empreintes de tête et les quatorze sorties de mesure citées sont égales au disque. La ligne 328 du registre des accords est égale à l'extrait. L'accord de l'opérateur porte bien l'échéance du 2026-11-18. Le cumul de 5,989 USD est aux lignes 476, 481 et 482 du registre des dépenses. La fiche de code cite 63 fichiers (22, 21, 20). La ligne `ADDENDUM-ECART-3-BBIS` figure une fois, et le registre voisin est égal au commit de la course.

**Recherches demandées.**
- **176** : aucun comme plancher. Deux mentions, toutes deux pour dire qu'il est remplacé.
- **Valeur de clé** : aucune. Les seuls jetons sont les jetons factices des gestes 6 (c) et 14.
- **Chemin relatif** : aucun qui porte. Chaque appel commence par un `cd` absolu ; `PYTHON_BBIS` est absolu.
- **Empreinte tronquée** : cinq formes abrégées, toutes après une forme entière, sauf `641adeb5…` (épreuve absente du dépôt, forme entière dans la contre-lecture du projet version 3). Les seize caractères de l'en-tête de la commande sont ceux que le lanceur imprime ; le contrôle sur 64 caractères est au geste 13.

---

## 2. Corrections exigées

### C1. Le geste 2 (a) arrête un opérateur dont le crochet est chargé
Dans ma session, `${CLAUDE_PROJECT_DIR:-vide}` rend `vide`, alors que le crochet est chargé : il a refusé chez moi la commande du geste 2 (e). Le feu écrit « Arrêt si (a) ne rend pas le dépôt de travail ». Un opérateur sous-agent, ce que demande GO-2026-11-16-06, s'arrêterait donc au geste 2 avec une garde saine.
Limite : je ne l'ai constaté que dans une session de sous-agent ; une session ouverte par une personne peut différer.
**Correction** : retirer (a) des critères d'arrêt, ou le garder comme simple relevé. La preuve de chargement est le refus de (e), avec (b) et (c).

### C2. Au geste 14, les fenêtres ne gardent pas la création
Le document en ligne (`<<'FIN'`) coupe la commande en deux listes. Les contrôles de la première (30 minutes depuis la commande, une heure depuis le crédit, outil du geste 4, fichier neuf) ne conditionnent pas la seconde, qui porte l'égalité des arguments, les clés et la création.
Rejoué sur un analogue sans effet : la première liste échoue, la seconde est jouée quand même. Elle n'échoue que si `ligne-courte.sh` manque. Dès que ce fichier existe (tentative antérieure arrêtée sur une clé absente ou un refus de permission), **un second jeu du geste 14 crée la machine sans aucun des quatre contrôles**.
La ligne finale « création : code … » s'imprime aussi quand rien n'a été tenté.
**Correction** : une seule liste. Écrire `ligne-courte.sh` dans un appel à part (fin du geste 13), puis enchaîner tout le geste 14 par `&&` ; n'imprimer « création tentée » qu'à l'intérieur de la chaîne. Même forme au geste 6 (c).

### C3. Les reprises « sous des noms neufs » ne sont pas jouables telles qu'écrites
Le feu permet de refaire les gestes 12 et 13 avec un suffixe `-2`, une recherche neuve, un témoin neuf (`temoin-2.sh`), et la lecture de `instance-de-la-liste.sh`. Or les noms sont écrits en dur dans les gestes 11, 13, 14, 16, 18, 19, 22 et 23, et le geste 12 refuse si `valeurs.sh` existe ; le programme de choix écrit `candidates.txt` en mode « jamais réécrit ».
Deux effets : la reprise bloque ; ou l'opérateur retape des noms, contre la règle du feu. S'il n'en retape qu'une partie, le geste 18 lit l'ancienne échéance dans `valeurs.sh`, ne trouve pas la ligne de minuterie attendue, et **détruit une course saine, la dernière**.
**Correction** : un suffixe de tour lu dans un fichier du dossier d'envoi, écrit par programme et porté par tous les noms ; ou l'interdiction écrite de toute reprise (arrêt et nœud).

### C4. Le tableau du geste 20 n'a pas de ligne pour une marche qui tombe
Après la marche, l'amorce peut écrire « BBIS ARRET : marche : code N (marche.err) » (marche tombée sur une erreur : le cas le plus plausible), « branche locale de sortie depuis COMMIT », « ajout », « fichier de plus de … octets » ou « commit ». Aucune ligne du tableau ne les couvre : « arrêt écrit » ne vise que le code 4 de la marche, et « toute autre » ne vise que les étapes 1 à 7. L'instance est alors arrêtée, facture son disque, et sa minuterie est morte.
**Correction** : une ligne « toute autre ligne `BBIS ARRET` : geste 21 (présence seulement), puis gestes 22 et 23 dans les quinze minutes ».

### C5. Une lecture passagère peut détruire la course aux gestes 17 et 19
Les gestes 17 et 19 rejouent « la commande du geste 16 », jusqu'à quarante fois pendant l'attente.
- Chaque rejeu réécrit `prix-relu.sh`. Un prix passagèrement illisible le vide. Rejoué : la garde de dépense reçoit alors un prix vide, rend « BBIS REFUS » et imprime l'ordre de destruction, que le geste 19 commande de suivre.
- Une liste passagèrement vide ou incomplète rend « COURSE … ABSENTE », code 4 (rejoué avec une liste vide). Le geste 16 commande alors la destruction aussitôt.
**Correction** : une commande propre aux gestes 17 et 19, aux noms donnés par programme, qui n'écrit pas `prix-relu.sh` ; ce fichier écrit une seule fois au geste 16. « Absente » ne compte que si le témoin figure dans la même liste ; sinon la lecture est refaite, trois fois au plus à une minute d'écart, comme le feu le permet déjà pour le prix illisible.

### C6. Les deux planchers de crédit ne tiennent pas ensemble
Avec 20 USD à la création et une destruction sous 8 USD, une course saine est détruite après (20 − 8) / 1,48 ≈ 8,1 heures. La garde de débit permet 11 heures, la minuterie 13. Le coût attendu du texte scellé (jusqu'à 9,9 USD) laisse environ 10 USD : la marge est mince. La condition de marge du rédacteur ne couvre que les autres instances, non la course elle-même.
De plus, le geste 8 écrit l'heure du relevé même quand la lecture échoue ou que le crédit est insuffisant : le contrôle d'une heure du geste 14 ne vérifie que l'âge.
**Correction**, au choix de la mère avant de sceller :
- soit la condition du geste 8 devient : crédit − 13 × débit des autres ≥ 8 + 11 × 1,48 = **24,28 USD** (27,24 USD pour couvrir les 13 heures) ;
- soit une réserve nommée l'écrit avec son chiffre : « à 20 USD exactement, une course saine de plus de 8,1 heures est détruite par le plancher de 8 USD ».
Dans les deux cas, n'écrire l'heure du relevé que sous « CREDIT SUFFISANT », sous un nom neuf par relevé.

### C7. Une sortie de l'amorce avant la minuterie n'est bornée que par un opérateur vivant
Le feu couvre bien ce cas par les gestes 17 et 18 : toute ligne « BBIS REFUS », une ligne manquante ou répétée, un état terminal commandent la destruction. Les dix sorties de l'amorce d'avant la minuterie écrivent toutes « BBIS REFUS » ; un base64 illisible ne laisse aucune ligne, ce qui est couvert aussi.
Mais rien d'automatique ne borne ce cas. Si la session de l'opérateur tombe entre la création et le geste 18, et que le loueur relance le conteneur en boucle (déjà vu, instance 60671759), la carte facture sans minuterie. Le tableau du pire cas (§ 6) suppose la minuterie armée et ne le dit pas.
**Correction** : l'écrire au § 5 et au § 6 ; et donner à la mère un filet. À l'inscription de l'engagement (geste 16), elle pose un rappel à la création plus 30 minutes (état et trois lignes confirmés par l'opérateur, sinon elle détruit par l'identifiant et prouve l'absence) et un autre à l'échéance plus 15 minutes.

---

## 3. Points mineurs

1. **Geste B.3 de l'arbitrage, à la lettre.** L'arbitrage demande, « dans le shell de lancement », la ligne `ADDENDUM-ECART-3-BBIS` présente une fois, l'addendum conforme à son compagnon, et les empreintes de la chaîne comparées au § 6 de l'addendum. Le feu s'appuie sur les mesures au commit. Ajouter au geste 3 : le registre voisin dans la liste de `git diff --quiet`, le compte de la ligne, `sha256sum -c` du compagnon, et la présence des deux empreintes dans l'addendum (rejoué : égal, 1, conforme, 2).
2. **Heure de rédaction.** Le feu se dit rédigé « jusqu'à 06:40Z environ » ; le fichier est daté de 06:20:59Z sur le disque. À corriger.
3. **Geste 6 (c).** « Le jeton factice apparaît » : il n'apparaît pas, l'argument étant coupé à 80 caractères. Phrase à corriger.
4. **Geste 5.** Si le `cd` échoue, les listes suivantes écrivent les programmes dans le dossier courant, donc dans le dépôt. Écrire les fichiers par chemin absolu.
5. **Geste 7.** La présence d'une instance déjà étiquetée n'est lue qu'à l'œil : en faire un code de sortie. Le débit ne compte que les instances à l'état « running » : le dire.
6. **Geste 19.** « garde de dépense : code » peut porter le code d'un échec antérieur de la chaîne, sans ordre de destruction. Dire que seul un refus de la garde avec son ordre imprimé commande la destruction.
7. **Condition 8.** Qui répond aux demandes d'autorisation si l'opérateur est un sous-agent ? Sans personne, la demande expire, et c'est un arrêt aux gestes 6, 13 ou 14. Nommer la personne ou la règle.
8. **Fichiers `.err`.** Sur un refus d'authentification, l'outil 1.8.3 écrit la fin de la clé du loueur sur sa sortie d'erreur. Le feu n'en affiche que la taille : le garder, l'écrire au § 9, et effacer ces fichiers au geste 24.
9. **Garde de débit et poussée impossible.** Vérifier que l'instance gardée 12 heures est bien arrêtée. Si elle est encore « running », la demande d'arrêt a échoué et la carte facture : gestes 22 et 23 aussitôt.
10. **Geste 15, à trancher par la mère.** Une réponse illisible avec une instance saine de l'étiquette commande la destruction et consomme la dernière course. C'est sûr pour l'argent. La mère peut préférer l'adoption par l'étiquette, puis le geste 16.
11. **Geste 18, réserve à compléter.** Un échec de la lecture du journal elle-même ne se distingue pas d'une ligne absente : destruction à cinq minutes. La sous-commande `logs` n'a jamais servi dans cette chaîne. À écrire à la réserve 13.

---

## 4. Correspondance, vérifiée

**« Ce qui doit aller au feu version 4 » (arbitrage)** : les dix points sont portés. 1 (§ 3, geste 3, préambule ; voir mineur 1) ; 2 (§ 3, gestes 3 et 12) ; 3 (§ 5, gestes 9, 10, 13) ; 4 (§ 5, § 6, gestes 12 et 14 ; voir C2 et C3) ; 5 (champ 1, gestes 13 et 14) ; 6 (champ 3, gestes 4 et 8 ; voir C6) ; 7 (geste 18) ; 8 (§ 7) ; 9 (151 partout) ; 10 (§ 13, réserves 1, 4, 5). Les gestes B.1 à B.5 sont portés.

**Onze corrections de la contre-lecture du projet version 3** : toutes portées. La correction 5 est portée autrement que demandé : le feu explique qu'aucun maillon ne permet de relancer la poussée depuis l'instance, et la remplace par 12 heures de garde et un nœud. C'est déclaré et cohérent avec l'amorce. Les trois cas non dits de la section D sont portés.

---

## 5. Déclarations et limites

- **Lecture du distant.** Le lanceur, joué sur l'offre fabriquée, a fait deux `git ls-remote` en lecture seule. Je n'ai fait aucun `git fetch`.
- **Dépôt des paquets.** Un téléchargement du paquet de l'outil, lu sans être installé ni exécuté. Aucun appel au loueur.
- **Refus du crochet.** Un seul, voulu : la commande sans effet du geste 2 (e).
- **Refus d'une suppression.** Une de mes commandes de ménage du bloc-notes a été refusée par un contrôle de sûreté de la session ; rien n'a été supprimé à tort, et j'ai poursuivi dans des dossiers neufs.
- **Non vérifié** : tout ce qui demande le loueur (forme réelle des réponses, comportement de `-y`, journal, crédit, instances) ; la session d'une personne pour C1 ; les accords cités aux champs 1 et 2 au-delà de leur présence au registre ; la disponibilité du modèle B de la condition 5.
- Je n'ai lu aucun résultat : je reste éligible comme contre-lecteur, non comme lecteur.
