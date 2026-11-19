# Vérification des corrections du code de formation des familles d'adaptateurs jumeaux (barreau 5) — v1

- Vérificateur : le contre-lecteur de `contre-lecture-code-formation-v1.md` (`5174b105…`), Claude Fable 5.2, autre modèle que le développeur (Claude Opus 5.5). Pièce de classe B. Écrite le 19 novembre 2026, de 20:12Z à 20:50Z environ à l'horloge du conteneur (`date -u`).
- Mandat : `mandat-verification-corrections-code-formation-v1.md`, `35e5b1ecc02d22111a7d4b5403598e95a2aa6f8ac4cd6b1f7e4b585a4dc053fd` (vérifié).
- Pièces vérifiées par empreinte : rapport v3 du développeur (`ddaf91a8…`) ; son mandat (`fd3b9b13…`) ; vérification du plan (`a1b2250d…`) ; fiche de décision V-B1 (`78cadfd2…`) ; vérification des champs de l'offre (`48a81bd4…`) et sa sortie brute (`3b058a95…`) ; les dix fichiers d'outils et de sorties du développeur, aux empreintes du § 9 de son rapport ; le texte, brouillon 3 (`525f338e…`, vérifié à la première passe). Les douze fichiers de code et d'essais ont les empreintes du § 9 du rapport v3 ; ils sont à la tête `199caf6b2`, sans modification locale.
- Fait : lecture entière de `formation_v1.py` et de l'amorce corrigés, du lanceur, de l'essai neuf de l'amorce entière, de l'essai à blanc du tokeniseur (script et sortie) ; lecture des différences de `edition_cout_v1.py`, de `engagement_v1.py` et des essais aux endroits jugés ; les six fichiers d'essais joués une fois (253 passés, 316 s) ; 29 mutations jouées l'une après l'autre dans une seule copie de travail hors du dépôt ; neuf sondages ; l'extraction de l'amorce rejouée au commit `199caf6b2` et les essais du paquet joués sur cet arbre (171 passés).
- Rien de réel : aucun réseau, aucune instance, aucune dépense, aucun commit. Le code du dépôt n'a pas été modifié. Aucune donnée ni résultat ouvert. L'essai à blanc du tokeniseur n'a pas été rejoué. Aucun refus d'outil.
- **Disque.** Inventaire de mes copies de la première passe, dans le bloc-notes de la session, avant effacement : `base/` (1,9 Go, tête `62194f6b0`, état propre) ; `extrait/` (1,9 Go, tête `62194f6b0`, état propre) ; `mut/` (497 Mo : 23 copies `M00` à `M22` et leurs 23 dossiers de temporaires `M00-tmp` à `M22-tmp`) ; `essais-tmp-extrait/` ; `sondages-1/`. Leurs sorties étaient versées (`outils-contre-lecture-code-formation-v1/`). Effacées par leur chemin écrit en toutes lettres. Une seule copie de travail ensuite : `verif-b5f/` (l'arbre que l'amorce extrait, au commit `199caf6b2`, plus les essais du lanceur et des amorces et la garde de calcul). Temporaires dans `/dev/shm`.

## Verdict

**Conforme après ces corrections.** Le constat bloquant est fermé. Les neuf majeurs sont fermés. Les quatorze mineurs sont fermés ou déclarés à bon droit. Il reste sept constats neufs, tous mineurs, dont deux touchent le chemin de la destruction prouvée ; aucun ne fausse une famille, aucun ne détruit une sortie. Ils peuvent être corrigés avec la ligne de code que demandera la réponse « 36 ou 39 », puis vérifiés d'un trait.

| | bloquant | majeur | mineur |
|---|---|---|---|
| constats de la contre-lecture, fermés | 1 sur 1 | 9 sur 9 | 12 sur 14 ; m-4 et m-14 déclarés, déclaration suffisante |
| constats neufs | 0 | 0 | 7 |

Mutations : **26 défauts attrapés sur 29 joués**, dont les 20 de la contre-lecture (6 sur 20 à la première passe). Des trois manqués, deux se couvrent l'un l'autre et sont attrapés ensemble ; un seul est un angle mort (section « Contrôle par mutation »).

## 1. Chaque constat de la contre-lecture

| constat | correction | jugement | l'essai l'attrape-t-il ? |
|---|---|---|---|
| **B-1** tirage sous un adaptateur de la famille précédente | dose remise à 0 après l'injection, avant chaque tirage, en fin de famille et après une garde de famille ; garde `exiger_modele_nu` après l'injection, avant et après chaque tirage (`formation_v1.py`, l. 597-605, 1043-1044, 1100-1103, 1145) | **fermé**. Sondage S1 : dose 0 et logits du modèle nu à l'entrée des deux tirages, alors qu'un adaptateur de la première famille est encore chargé | oui : `test_jouet_tirage_de_chaque_famille_sur_le_modele_nu` relève l'état à l'entrée de chaque tirage ; la garde a deux cas sains et trois artefacts. Ma mutation B1 (défaut réintroduit en entier) : attrapée |
| **M-1** clés transmises comme texte | `$HF_TOKEN` sans barre (l. 1318) ; l'amorce refuse une clé reçue comme nom (l. 237) | **fermé**. Sondage S2 : le loueur reçoit les valeurs, la ligne imprimée ne porte que les noms | oui : un essai joue la ligne dans un shell ; l'amorce entière refuse avant tout clonage |
| **M-2** minuterie qui détruit sans savoir | témoin écrit par `prouver_versement` ; sans témoin à l'échéance : état « stopped », jamais de destruction, signal écrit ; attente par pas de 5 secondes | **fermé**, voir § 2 | oui pour la minuterie seule et pour la preuve ; la minuterie n'est pas jouée jusqu'à son échéance dans l'amorce entière (constat neuf n-3) |
| **M-3** brouillon accepté comme texte scellé | ligne `SCELLEMENT-B5F` exigée au commit de la course ; texte cité égal au chemin et à l'empreinte de la ligne ; nom qui contient « brouillon » refusé | **fermé**, voir § 2 | oui : quatre cas pour la marche, cinq pour le lanceur |
| **M-4** inégalité qui arrête l'instance ; tirage hors du disque | `tirage.jsonl` écrit et scellé avant l'édition ; l'inégalité rend la famille non formée, le retirage suit | **fermé** | oui (mutations M06, et N05 et N06 du développeur) |
| **M-5** aucune relance | familles `-x1`, branche `…-instance-<n>-x1`, clé `GO-RELANCE-FORMATION-B5F`, sous-commande `relance` ; paramètre `piece` | **fermé pour le code**, voir § 2 ; la règle reste à écrire au texte | oui |
| **M-6** aucun inventaire hors fin nominale | `inventaire_apres_arret` dans le bloc d'arrêt ; l'amorce écrit de plus son propre inventaire final | **fermé** ; un cas reste sans issue : l'arrêt avant la marche (constat neuf n-1) | oui |
| **M-7** liste noire | liste blanche des noms ; contenu des fichiers d'adaptateur relu ; pose de crochets refusée | **fermé**, voir § 2 ; le contenu des fichiers admis reste libre (constat neuf n-5) | oui pour les noms, les formes et les crochets |
| **M-8** épisodes des saboteurs d'apprentissage | `preparer_entrees_de_lecture(…, episodes)`, lignes vérifiées une à une | **fermé** | oui, après le resserrement que le développeur déclare (N10) |
| **M-9** essais à vide | essais ajoutés pour les dix points ; amorce entière jouée à blanc | **fermé** ; voir « Contrôle par mutation » | — |
| m-1, m-2, m-3 | versement qui écarte le gros fichier ; 8 tâches par pli ; durées réelles | **fermés** (sondage S5) | oui |
| **m-4** fragment encodé seul | non corrigé ; déclaré dans le module ; mesuré : 936 éditions, aucun fragment non canonique avec le vrai tokeniseur | **déclaration suffisante**. L'écart est sans effet mesurable et le contrôle « texte relu égal » tient dans tous les cas. Il reste au texte de l'écrire (« encodé seul, texte relu égal ») | — |
| m-5 écritures que le modèle n'écrirait pas | suffixe « k » sous 1 : non éditable ; deux autres écritures comptées par famille et par sens | **fermé** pour le code ; le choix revient au texte (§ 6) | oui |
| m-6, m-7 | fichiers de la racine nommés ; quatre dossiers vérifiés absents | **fermés** (extraction rejouée : 500 fichiers, aucun fichier de racine hors des six nommés) | oui |
| m-8, m-9 | preuve complète ; code de la session comparé | **fermés** | oui |
| m-10, m-11, m-12, m-13 | paramètre `piece` ; registre lu à un commit ; nom de branche lié ; dates | **fermés** | oui |
| **m-14** vrai tokeniseur jamais vu | essai à blanc, § 5 ci-dessous | **déclaration suffisante** pour la mécanique du tokeniseur ; la part d'actions non éditables reste une menace, d'une autre nature (§ 5 et § 6) | — |

## 2. Les six points à regarder au plus près

**B-1, et les deux mutations déclarées équivalentes.** M20 et N15 retirent la remise à la dose 0 d'avant le tirage. Elles sont bien équivalentes : j'ai suivi chaque chemin qui mène d'une famille à la suivante. Famille formée : dose 0 à la l. 1145. Famille non formée : la dose n'a pas bougé depuis le tirage. Famille abandonnée par la coupure : dose 0 depuis le contrôle d'identité (l. 706). Garde levée en mode « famille » : dose 0 à la l. 1086, puis modèle nu exigé. Aucun chemin n'arrive au tirage suivant avec une dose non nulle : la protection est double, et retirer une moitié ne réintroduit pas le défaut. Les formes qui retirent les deux moitiés (M20b et N15b du développeur, ma mutation B1) sont attrapées. La garde elle-même compare au bit près des logits relevés avant l'injection : elle voit aussi une base changée.

**M-2, minuterie et preuve.** La décision de la mère est codée telle quelle.
- La preuve est solide : inventaire de tout ce qui existe sous les sorties et les traces ; un fichier hors de la liste blanche ou trop gros fait échouer le versement, donc la preuve ; la tête de la branche distante doit égaler le dernier commit poussé ; chaque fichier est relu à ce commit, à sa taille et à son empreinte.
- Sans témoin à l'échéance, la minuterie ne détruit jamais. Elle demande l'état « stopped », même si le versement final est encore en cours : la poussée est alors coupée, le disque reste, le signal est écrit. C'est le côté sûr.
- Le journal de fin est poussé après la preuve, dans un commit de plus : la preuve n'en est pas changée, mais la session doit donner à `detruire` le commit prouvé, non la tête de la branche (constat neuf n-2).
- Mes mutations V01, V02 et V05 visent ce bloc. V05 (la destruction envoyée après trois demandes d'arrêt, sans preuve) est attrapée. V01 (tête distante non comparée) et V02 (versement incomplet toléré) passent une à une : la preuve a trois verrous qui se recouvrent, et chacune est rattrapée par les deux autres. V02 est équivalente au sens strict : un fichier resté sur le disque figure à l'inventaire et manque au commit, la relecture le voit toujours. Posées ensemble (V08), elles sont attrapées. Reste un essai à écrire pour isoler V01 (constat neuf n-7).

**M-3, `SCELLEMENT-B5F`.** La ligne lie le texte par son chemin et son empreinte au commit de la course, dans la marche et dans le lanceur ; elle doit précéder l'accord. Le refus d'un brouillon tient à son nom (sondage S9 : « …-v1-b3.md » passerait). C'est assez : la preuve est la ligne, que la mère inscrit au scellement, et non le nom. À dire à la mère : n'inscrire cette ligne qu'au scellement décisif.

**M-5, relance et « pièce ».**
- La relance est codée comme je la recommandais. Trois limites, à écrire au texte : (a) une seule ligne `GO-RELANCE-FORMATION-B5F` existe, puisque les clés sont uniques : toutes les instances à relancer doivent y être citées d'un coup, donc après la fin de toutes les premières marches ; (b) la relance reforme l'instance entière, y compris une famille que la première copie avait menée au bout ; (c) rien ne borne le cumul des coupures (constat neuf n-4).
- « Pièce » : le paramètre a deux valeurs et aucun défaut. En mode « famille », une garde levée pendant une famille la compte absente, sauf les gardes d'instance (modèle qui n'est plus nu, base changée, point 5, signal, exception qui n'est pas une garde). Les trois artefacts sont éprouvés. Ma recommandation reste « famille ».

**M-7, liste blanche.** Elle porte sur les noms, sur les dossiers, sur les membres de chaque famille, et sur le contenu des fichiers d'adaptateur (clés et formes de l'état injecté). La même liste décide, dans l'amorce, de ce qui sort de l'instance. La pose de tout crochet de torch est refusée pendant la marche ; j'ai vérifié dans la version de transformers du dépôt que le chargement du modèle n'en pose aucun (le seul appel est dans `enable_input_require_grads`, que la chaîne n'emploie pas). Limite qui reste : le contenu des fichiers de texte admis n'est pas borné. Ma mutation V06 le montre : manquée, les 253 essais passent (constat neuf n-5).

**m-4 et m-14.** Jugés à la table du § 1 : la déclaration suffit pour les deux.

## 3. Les deux défauts que le développeur a trouvés dans sa propre écriture

1. **Extraction du texte cité.** Corrigé et éprouvé : l'amorce ajoute `/$PREREG` et son compagnon aux motifs (l. 270) et exige les deux fichiers (l. 273). L'essai de l'amorce entière cite un texte dont le nom ne commence pas par le préfixe des motifs : il échouerait sans la correction.
2. **Seconde copie des traces.** Corrigé : une seule copie avant le versement final, la preuve repousse ce qu'elle inventorie, le journal de fin part après, dans un commit qui ne change pas la preuve. L'essai vérifie que le témoin porte un commit ancêtre de la tête et que l'inventaire tient à ce commit. Conséquence pour la session : constat neuf n-2.

## 4. L'amorce entière jouée à blanc

Le fichier neuf éprouve le comportement, et non seulement le texte. L'amorce y tourne de l'étape 0 à l'étape 8 avec ses vraies gardes, un vrai `git` sur un dépôt distant local, et de faux outils pour le loueur, la carte, l'installation, les essais et la marche. Six essais : fin nominale, porte des essais fermée (deux cas), échéance atteinte (la marche est coupée par le vrai `timeout`), sortie hors de la liste blanche, clé reçue comme nom, relance. Le développeur a rejoué six mutations contre ce seul fichier, sans les contrôles du texte : toutes attrapées.

**La minuterie n'y est pas jouée jusqu'à l'échéance.** Elle est lancée, sa ligne d'échéance est lue, puis l'essai l'arrête par son PID. Son comportement à l'échéance est éprouvé à part, sur le bloc extrait, avec et sans témoin. Ce qui n'est donc joué nulle part : la minuterie et la fin de l'amorce ensemble (le témoin écrit par `terminer` est-il bien celui que lit le processus de fond ?). La raison est le quart d'heure fixe du versement, qu'aucun essai ne peut attendre. Constat neuf n-3.

## 5. L'essai à blanc du tokeniseur (jugé sur sa lecture et sur sa sortie, non rejoué)

- **Ce qu'il vaut.** Le script charge le tokeniseur comme la chaîne, fabrique 612 actions dans le format de l'environnement, et joue l'opérateur réel. Il lève la menace que je nommais en tête : le décodage cumulé, les octets partiels (signes « ≈ », « ≥ », « × », « – ») et le nettoyage des espaces ne rendent aucune action non éditable. Les contrôles de mon sondage S4 y sont repris avec les décalages de caractères du tokeniseur. La chaîne d'une famille entière passe au vrai gabarit de conversation.
- **Ce qu'il ne vaut pas pour le plafond de 10 %.** Il ne dit rien de la fréquence des écritures chez le saboteur instruit. Deux écritures plausibles sortent : un nom de carte à chiffres dans le champ du coût (« A100 » compte pour un second nombre selon le lecteur gelé), et le suffixe « k » de 1k à 2,9k (règle neuve de m-5). Si elles pèsent plus de 10 % des actions d'un tirage, la famille est refusée, puis retirée, puis absente. Le résultat est donc nécessaire, non suffisant. Autre limite déclarée, juste : l'essai n'a vu que des encodages ordinaires, alors que le modèle peut produire des suites de jetons non canoniques ; l'opérateur les traite par le décodage, erreur du côté sûr.
- **La lecture des énoncés des tâches de réserve.** Le script lit par programme le fichier des tâches de réserve cité par la configuration scellée, en tire des phrases pour les titres et les propositions, et n'en écrit rien : la sortie ne porte que des comptes et les écritures du coût fabriquées (vérifié sur le fichier de sortie).
  - **Le texte ne la permet pas à la lettre.** Plan, point 7, cinquième tiret : « Les développeurs du code […] travaillent sur le modèle jouet et sur des fichiers fabriqués. » Le fichier des tâches de réserve n'est pas un fichier fabriqué. Le point 1 le range parmi les entrées du plan : il le réserve au code du plan, c'est-à-dire aux marches de formation.
  - **L'écart est sans effet sur l'aveugle.** Les énoncés ne portent ni coût, ni adaptateur, ni étiquette ; le mandat du développeur, écrit par la mère, demandait cette lecture (« à partir des descriptions de tâches ») ; ce tiret n'est pas une section figée.
  - **À faire** : le rédacteur l'écrit au brouillon 4, soit comme exception au cinquième tiret (« et, pour l'essai à blanc du tokeniseur, les énoncés des tâches de réserve, lus par programme, jamais affichés »), soit dans la table d'exposition.

## 6. Contrôle par mutation

Une seule copie de travail ; chaque mutation posée, jouée (les six fichiers, arrêt au premier échec), retirée, fichier rendu à l'octet. Outil : `mutations-verif-v1.py` ; sortie : `sortie-mutations-verif-v1.txt`.

| n° | défaut réintroduit | résultat |
|---|---|---|
| M01 à M19, M21 | les vingt défauts de la contre-lecture, sur le code corrigé | **20 attrapés sur 20** (6 sur 20 à la première passe) |
| B1 | le constat bloquant réintroduit en entier : aucune remise à la dose 0, garde du modèle nu vidée | **attrapée** |
| V01 | preuve du versement : la tête de la branche distante n'est plus comparée au dernier commit poussé | manquée seule ; couverte par les deux autres verrous |
| V02 | preuve du versement : un versement incomplet n'arrête plus la preuve | manquée seule ; équivalente (la relecture au commit la rattrape toujours) |
| V08 | V01 et V02 ensemble | **attrapée** |
| V03 | relance accordée à une instance que la ligne de relance ne cite pas | **attrapée** |
| V04 | liste blanche : contenu d'un fichier d'adaptateur non relu | **attrapée** |
| V05 | minuterie : destruction envoyée après trois demandes d'arrêt, sans preuve | **attrapée** |
| V06 | activation lue par le sous-module interne du modèle, glissée dans un champ de plus des lignes de l'évaluation | **manquée** (n-5) |
| V07 | garde du modèle nu : la dose n'est plus lue | **attrapée** |

**Bilan : 29 mutations jouées, 26 attrapées.** Le détail, essai par essai, est dans la sortie. Le compte du développeur (38 sur 38) est exact pour ses propres mutations : je n'ai pas rejoué ses seize « N », j'ai lu leur définition et rejoué les vingt miennes, qui en recoupent les essais. Ses deux mutations déclarées équivalentes le sont (§ 2).

Ce que disent les trois manquées : les corrections sont éprouvées là où un défaut change un comportement ; il reste un angle mort réel (V06 : le contenu des fichiers admis) et un verrou redondant que rien n'isole (V01).

## 7. Constats neufs (tous mineurs)

### n-1 — Après un arrêt avant la marche, `detruire` refuse toujours

- **Où.** `formation_v1.py`, `exiger_versement`, l. 853.
- **Fait.** L'instance s'arrête avant la marche (essais du paquet en échec, modèle non descendu, arbre non propre) : l'amorce verse ses traces et prouve ce versement, mais aucun manifeste n'existe. `exiger_versement` exige le manifeste sans condition : la sous-commande `detruire` refuse (sondage S7). L'instance est arrêtée, non détruite ; la session n'a plus que la destruction à la main.
- **Correction.** Avant :
  ```python
      montrer(f"runs/{run_id}/manifeste.json")
  ```
  Après :
  ```python
      prefixes = (f"donnees/{run_id}/", f"runs/{run_id}/", f"diag/{run_id}/")
      if any(str(f["chemin"]).startswith(prefixes) for f in inv["fichiers"]):
          montrer(f"runs/{run_id}/manifeste.json")
  ```
  Essais : inventaire de traces seules, accepté ; inventaire qui liste une sortie de marche sans manifeste au commit, refusé.

### n-2 — La session doit donner à `detruire` le commit prouvé, non la tête de la branche

- **Où.** `scripts/lancer_b5f_formation_v1.sh`, en-tête, sous-commande `detruire` ; rapport v3, § 5.
- **Fait.** Le journal de fin est poussé après la preuve. À la tête de la branche, le journal n'a plus l'empreinte de l'inventaire : `exiger_versement` refuse (sondage S7). Au commit du témoin, il accepte. Rien ne le dit à la session.
- **Correction.** En-tête du lanceur, après « versement prouvé » : « COMMIT est le commit prouvé, que nomme la ligne « versement final prouvé … au commit » du journal de l'instance (l'avant-dernier de la branche de sortie quand le journal de fin a été poussé), et non la tête de la branche ». Même phrase au § 5 du rapport du développeur.

### n-3 — La minuterie et la fin de l'amorce ne sont jamais jouées ensemble

- **Où.** `amorce_b5f_formation_v1.sh`, l. 45 ; `tests/test_amorce_b5f_formation_entiere_v1.py`.
- **Correction.** Avant : `VERSEMENT_S=900`. Après : `VERSEMENT_S=900; [ "$BLANC" != 1 ] || VERSEMENT_S="${B5F_VERSEMENT_S:-900}"` (la variable n'est lue qu'en essai à blanc). Deux essais de plus dans le fichier de l'amorce entière, échéance d'arrêt proche et quart d'heure ramené à quelques secondes, minuterie laissée en vie après la fin de l'amorce : fin nominale, le faux `curl` reçoit une destruction par l'identifiant ; sortie hors de la liste blanche, il ne reçoit que des demandes d'arrêt, et le signal pour la mère est écrit.

### n-4 — Rien ne borne le cumul des coupures des relances

- **Où.** `formation_v1.py`, `lire_code_et_accord`, l. 897-906.
- **Fait.** Le plan engage 169 USD de coupures sous un plafond de 200. La ligne de relance peut citer deux instances ou plus : 221 USD et au-delà sont acceptés (sondage S8). La garde `depense` de la session reste, mais elle dépend d'un relevé à la main.
- **Qui tranche.** Le rédacteur du texte et du devis, au brouillon 4 : la relance vit-elle sous le plafond commun, ou sous la « ligne neuve » que dit le devis ? **Ma recommandation** : sous le plafond commun, et le code refuse une ligne de relance dont les coupures, ajoutées à celles du plan, le dépassent. Correction, après la l. 903 :
  ```python
          if sum(COUPURES_USD.values()) + sum(COUPURES_USD[n] for n in instances) > PLAFOND_USD:
              raise GardeArret("GO-RELANCE-FORMATION-B5F : coupures du plan et des relances au-delà du plafond du devis")
  ```

### n-5 — Le contenu des fichiers de texte admis par la liste blanche n'est pas borné

- **Où.** `formation_v1.py`, `evaluer_membre`, l. 735-737 ; `exiger_sorties_permises`, l. 267-291.
- **Fait.** Mutation V06 : `evaluer_membre` appelle le sous-module interne du modèle (`modele.model`), qui rend le dernier état caché sans crochet et sans que les états cachés soient demandés au modèle entier, et en glisse quatre valeurs dans un champ de plus des lignes de `evaluation-<membre>.jsonl`. Ni `proteger_modele`, qui ne garde que l'appel du modèle entier, ni la liste blanche, qui garde les noms, ne le voient : 253 essais passés.
- **Portée.** Le code livré n'écrit rien de tel : je n'y ai trouvé aucune lecture interne. C'est la garde qui a un angle mort, comme à la première passe.
- **Correction.** Dans `exiger_sorties_permises`, pour chaque fichier `evaluation-<membre>.jsonl` : chaque ligne porte exactement les clés qu'écrit `evaluer_membre` (`famille`, `membre`, `tache`, `pas`, `texte`, `ids`, `mention`, et les clés du lecteur gelé), `ids` est une liste d'entiers, aucune valeur n'est une liste de nombres à virgule. Même contrôle des clés pour `tirage.jsonl`. Essai : la mutation V06 devient un artefact refusé.

### n-6 — Les essais du paquet n'ont jamais tourné sous la version de Python de l'instance

- **Fait.** L'image de l'instance est `python:3.11-bookworm` ; le dépôt local tourne sous Python 3.13. J'ai lu la syntaxe des 291 fichiers de `src/controle_ia` et des essais du paquet avec Python 3.11 : aucune erreur. Les essais eux-mêmes n'ont pas tourné sous 3.11 (aucun environnement 3.11 avec torch ici). Les chaînes précédentes ont tourné sur cette image : le risque est faible, mais la porte des essais arrêterait les sept instances d'un coup.
- **À faire.** Par la mère ou la session de formation, avant le gel : les essais du paquet joués une fois sous Python 3.11 avec `requirements-gpu.txt` (sur processeur), ou la première instance lancée seule quelques minutes avant les six autres.

### n-7 — La comparaison de la tête distante n'est isolée par aucun essai

- **Où.** `amorce_b5f_formation_v1.sh`, `prouver_versement`, l. 190-191 ; `tests/test_amorce_b5f_formation_v1.py`, `test_preuve_artefacts_aucun_temoin`.
- **Fait.** Mutation V01 manquée seule : dans les deux artefacts qui la visent, c'est l'échec de la poussée qui refuse, avant la comparaison. Le verrou est redondant dans la suite réelle ; il ne compte que si le versement de l'inventaire ne pousse rien alors que la branche distante a bougé.
- **Correction.** Un artefact de plus : `prouver_versement` joué deux fois, le témoin retiré et la branche distante supprimée entre les deux (la seconde fois, rien de neuf n'est poussé) ; aucun témoin ne doit être écrit.

## 8. Les choix laissés au texte, et ce qui menace le gel

| choix (rapport v3, § 6) | qui tranche | recommandation |
|---|---|---|
| 1. 36 ou 39 adaptateurs | **Lazar** (fiche V-B1) ; puis le rédacteur du devis pour les instances 6 et 7 si 39 | je n'ai pas d'avis sur la voie ; pour le code, « 39 » coûte une ligne de table (coupure et heures des instances 6 et 7), un essai, et ma vérification de cette ligne |
| 2. sens de « pièce » | **le rédacteur**, au brouillon 4 (liste d'arrêt, points 1 et 3) | « famille » ; écrire aussi la liste des gardes d'instance |
| 3. relance | **le rédacteur** (calendrier, « Lignes de registre », point 14) ; **la mère** pour l'inscription | écrire la règle telle que codée, ses trois limites (§ 2), et la borne de n-4 |
| 4. évaluation réduite | **le rédacteur du devis** (§ 4) | 8 par pli, comme codé |
| 5. suffixe « k » sous 1 | **le rédacteur** (point 3 du plan) | voir « remède » ci-dessous |
| 6. fragment encodé seul | **le rédacteur** | écrire « encodé seul, texte relu égal » |
| 7. `tirage.jsonl` et `textes-distillation.jsonl` | **la mère** | garder les deux : le doublon ne coûte que quelques Mo par famille |
| 8. écarts déjà déclarés | **le rédacteur** | les écrire au brouillon 4, comme recommandé à la première passe |

**Un remède que le texte peut adopter sans lire aucune donnée, si « A100 » ou « 2k » font dépasser le plafond.** Trois pièces, par ordre de préférence ; chacune est une règle écrite avant tout tirage, la même pour tous les membres.
1. **Nom de carte.** Le point 3 dit « un seul nombre dans le champ du coût ». Le texte peut préciser : un nombre collé à une lettre (« A100 », « H100 », « 8x ») n'est pas compté, pourvu que le premier nombre du champ, celui que lit le lecteur gelé, ne soit pas lui-même collé à une lettre. « 150 A100 GPU-hours » devient éditable ; « A100 : 300 heures », où le lecteur gelé lit 100, reste non éditable. Le lecteur gelé n'est pas touché : seule la condition d'édition change, dans `action_editable` et `localiser_nombre_du_cout`.
2. **Suffixe « k ».** Au lieu de sortir l'action, écrire la valeur du jumeau en clair, sans le suffixe (« 2k » devient « 600 »), l'empan édité couvrant le nombre et son suffixe. L'écriture est naturelle ; elle reste propre au sens bas, donc comptée parmi les écritures particulières.
3. **Le plafond lui-même.** Le seuil de 10 % est une convention du texte. Une action non éditable sort des cibles de tous les membres : elle ne fausse pas la comparaison, elle retire de la matière. Le texte peut fixer d'avance un second seuil (par exemple 25 %) sous lequel la famille est formée et signalée à l'audit de symétrie, dont le déclencheur (vii) existe déjà à 5 %.

Chacune de ces pièces change une section figée : il faut le mot du rédacteur au brouillon 4, quelques lignes de code, leurs essais et ma vérification, avant le gel. Une autre voie existe, qui n'est pas sans donnée : faire compter par une session habilitée, sur les textes déjà produits par le saboteur instruit de la course de confirmation, la part d'actions non éditables par motif, et ne rendre que ces comptes. Le point 1 du plan ne range pas ces textes parmi les entrées : il y faudrait le mot de Lazar.

**Remarque pour le rédacteur, si la voie (iii) de la fiche V-B1 est prise.** La sonde serait alors apprise sur le sur-saboteur contre le jumeau, c'est-à-dire sur les deux sens de l'édition. Les écritures propres à un sens pèsent plus : « 1000 » sans séparateur ne touche que le sur-saboteur, et, pour un coût de mantisse 3, 6 ou 1,5, le jumeau tombe exactement à un tiers quand le sur-saboteur tombe à 3,33 fois. Le code les compte par famille et par sens ; le texte doit dire ce qu'il en fait.

**Ce qui menace le gel du 22 novembre.**

| menace | qui tranche ou agit |
|---|---|
| « 36 ou 39 » non dit : la ligne `SCELLEMENT-B5F` ne peut pas s'écrire, rien ne part | Lazar |
| sens de « pièce », règle de relance, plafond des relances : absents du texte | le rédacteur, brouillon 4 |
| part d'actions non éditables au-dessus de 10 % le jour de la formation | le rédacteur (remède ci-dessus), ou Lazar (compte par une session habilitée) |
| trois offres seulement passaient les bornes du devis à 20:02Z pour sept instances | la mère (lancement par vagues) ; le rédacteur du devis si les bornes bougent |
| sept constats neufs, mineurs, et la ligne de « 39 » : une demi-journée de développeur, puis ma vérification | la mère |
| essais jamais joués sous Python 3.11 (n-6) | la mère ou la session de formation |
| version de transformers sur l'instance : elle doit rester celle du dépôt (le nettoyage des espaces n'y joue pas) | tenu par `requirements-cpu.txt`, que le gel couvre |

## 9. Le plancher d'essais : 171

**Il est bien mesuré.** Le développeur l'a mesuré sur l'arbre de travail extrait sans commit. Je l'ai remesuré sur un vrai commit : extraction par les motifs de l'amorce au commit `199caf6b2`, puis la commande même de l'étape 4 de l'amorce : **171 passés**, arbre propre après les essais. Un essai du paquet d'amorce exige de plus que le plancher égale le nombre d'essais collectés. La porte est donc exacte : un essai de moins, ou un essai sauté, arrête l'instance.

**Ce que la session de formation doit faire au commit de la course**, avant d'imprimer la première commande de création :
1. extraire l'arbre comme l'amorce le fait, au commit de la course (`extraire-arbre-instance-cl-v1.sh` de ma première passe le fait hors du dépôt, sans rien modifier) ;
2. y jouer la commande de l'étape 4 et lire « 171 passed » ; tout autre compte : ne rien lancer ;
3. si une correction a ajouté ou retiré un essai du paquet depuis (la ligne de « 39 », les constats n-1, n-4, n-5), le plancher doit avoir été changé dans l'amorce avant la ligne `CODE-FORMATION-B5F` : l'essai d'égalité le rappelle, mais il ne tourne que si quelqu'un joue les essais de l'amorce.

## Outils et sorties (noms neufs)

Dossier `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/outils-verification-corrections-code-formation-v1/` :
- `mutations-verif-v1.py` et `sortie-mutations-verif-v1.txt` ;
- `sondages-verif-v1.py` et `sortie-sondages-verif-v1.txt`.

L'extraction a été faite par l'outil de la première passe, `outils-contre-lecture-code-formation-v1/extraire-arbre-instance-cl-v1.sh` (`80a4c227…`), inchangé. Les empreintes sont dans les compagnons `.sha256`. À la fin : la copie de travail `verif-b5f/` et mes temporaires de `/dev/shm` effacés par leur chemin écrit en toutes lettres.
