PROJET DE FEU ÉCRIT DE LA SESSION MÈRE — version 4
Course de l'étape B bis de l'épreuve des sondes entraînées sur la tâche (T0.7)

**projet, non en vigueur ; champs à remplir par la mère : accord de Lazar sur les clés, accord de Lazar sur le plafond au lanceur, relevé de crédit**

Rédigé le 2026-11-18, de 05:55Z à 06:40Z environ (`date -u`), par un sous-agent de la session mère, qui n'a écrit ni le texte scellé, ni ses trois addenda, ni la chaîne de lancement, ni le projet de feu version 3, ni sa contre-lecture, ni l'arbitrage, ni les mesures. Il remplace le projet version 3 (`projet-de-feu-v3-non-en-vigueur.md`, `cad1883f765d9b425e50b0c2d00ee08f406f0f0db03c497f0cb04f228959d5fb`, gardé intact, R12), qui n'a jamais été versé ni mis en vigueur. Une fois en vigueur, il remplace aussi, pour la suite, le feu du 2026-11-17T11:13:33Z (`registres/t07-etape-b-bis/feu-bbis-v2.txt`, `33912cbe418f25c25ea3108572fa9cc07ee1b6bbecc236b9b934ff43cb21760b`), qui reste archivé sans modification. Le nom `feu-bbis-v3.txt` n'a jamais servi et ne sert pas : la mère verse ce feu sous `registres/t07-etape-b-bis/feu-bbis-v4.txt`.

Sources qui fondent ce texte : décisions R-3188 et R-3191 (`registres/decisions.md`) ; arbitrage des quatre contre-lectures de la chaîne version 6 (`arbitrage-contre-lecture-amorce-v6-v1.md`, `688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`), sections B et « Ce qui doit aller au feu version 4 » ; troisième addendum scellé (`e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`) ; projet version 3 et sa contre-lecture (`contre-lecture-projet-de-feu-v3.md`, `1d60a69bae14ecb8a70bfe55df31f66bd706c46adb2ebc6098e229480ae08e96`, onze corrections) ; répétition de la mesure du plancher (`repetition-mesure-plancher-py311-py313-v1.md`, `550c7d99e4c9dfcf420554bc1b77ac43948a83f646aedffa99bbe54125ce86de`) ; mesures définitives au commit de la course (`mesures-definitives-commit-course-v1.md`, `527ab727cf8edc8789352cb908293705236d1a9661540dd3ecff4cce9bba0fbc`) ; lignes GO-2026-11-14-09, GO-2026-11-16-06, GO-2026-11-16-11, GO-2026-11-16-12, GO-2026-11-18-03 à GO-2026-11-18-07 de `registres/go.md`. Tous ces fichiers sont sous `docs/notes/prealables-course-etape-b-bis-v1/` sauf mention contraire.

---

## § 0 — CE FEU N'EST PAS EN VIGUEUR À SA RÉDACTION

Il n'autorise aucune création de machine et aucun appel au loueur. Les gestes de la phase A (§ 10, gestes 1 à 6) ne touchent pas le loueur ; ils sont permis dès que ce feu est scellé, versé et inscrit, même avant les champs 1 à 3. Les gestes 7 et suivants ne sont permis que lorsque **toutes** les conditions ci-dessous sont levées, chacune par une pièce versée et scellée, ou par un mot écrit de Lazar inscrit au registre des accords. Un opérateur qui lit ce feu sans elles s'arrête au geste 6, ne crée rien, et le dit en une ligne.

**Champs à remplir par la mère** (le feu n'entre pas en vigueur tant qu'un champ est vide) :

1. **Passage des deux clés : accord de Lazar requis, cité ici quand donné.**
   Les deux clés sont le jeton GitHub des machines, `CONTROLE_IA_GITHUB_TOKEN_2`, passé comme `GH_TOKEN`, et le jeton de la plateforme de modèles, `HF_TOKEN`. Elles passent **par leur nom seulement**, dans le seul shell de lancement, pour cette seule course. Aucune valeur n'est lue, affichée ni copiée. GO-2026-11-18-05 laisse ce passage à Lazar.
   Accord cité : `________________` (identifiant de GO, heure d'inscription, verbatim de Lazar).
   À la rédaction, la branche `main` porte, après le commit de la course, la ligne GO-2026-11-18-06 (R-3195, verbatim « oui cles, je n'ai plus de budget pour recharger avant qq heures au moins »). La mère la vérifie et la recopie ici.
2. **Plafond de prix de 1,40 USD/h tenu aussi par le lanceur : accord de Lazar requis, cité ici quand donné.**
   Ce plafond va contre la lettre de GO-2026-11-18-03 (3), « tenu hors du code ». C'est une garde plus stricte, sans effet sur les résultats.
   Accord cité : `________________` (identifiant de GO, heure d'inscription, verbatim de Lazar).
   À la rédaction, `main` porte GO-2026-11-18-07 (R-3196, verbatim « plud de recharge jusqu a nouvel ordre, oui a la limite jusqu a nouvel ordre , quand le credit sera recharge on poura la lever »). La mère la vérifie et la recopie ici. Si Lazar lève plus tard ce plafond, le lanceur version 6 le tient quand même : seul un lanceur version 7 pourrait le retirer, et ce n'est pas cette course.
3. **Relevé de crédit du loueur** : `______ USD`, relevé à `____-__-__T__:__:__Z` par le geste 8. Ce relevé doit dater de moins d'une heure avant la création. Il faut :
   - un crédit d'au moins **20,00 USD** (GO-2026-11-18-03 (2)) ;
   - **et** la condition de marge du geste 8 : crédit relevé moins 13 heures du débit des autres instances en marche, au moins 20,00 USD.
   À la rédaction, GO-2026-11-18-07 interdit toute recharge « jusqu'à nouvel ordre », et le dernier crédit inscrit est sous le plancher. Ce feu attend donc une recharge que seul Lazar peut décider.

**Conditions à lever par la mère, sans champ** :

4. **Registre des accords lisible par le crochet de garde.** À la rédaction, il ne l'est pas. Le crochet (`.claude/hooks/garde_calcul.py`) lit tout `registres/go.md` avant toute commande qui contient une création d'instance. Il s'arrête sur la ligne 371 (GO-2026-11-18-07), dont l'échéance « jusqu'à nouvel ordre » n'est pas une date : « registre GO mal formé ligne 371 : dates illisibles ».
   Conséquence : toute commande de création est refusée aujourd'hui, pour toutes les sessions du programme.
   Constat : le rédacteur a lancé une simulation locale, sans loueur. Elle contenait le texte d'une ligne de création, et le crochet l'a refusée. Le rédacteur ne l'a ni reformulée ni contournée (§ 15). La cause a été confirmée par le lecteur même du crochet, joué en lecture seule.
   Le crochet n'admet « — » comme échéance que pour une ligne qui n'est pas de type « calcul ». La forme de la correction revient à la mère.
   Preuve exigée : la sortie du geste 2 (c).
5. **Accord de l'opérateur valide le jour de la création.** GO-2026-11-16-06 (opérateur sous-agent du modèle A) porte l'échéance 2026-11-18. Au-delà, la mère écrit sous quel accord l'opérateur agit (R-2883 (2) demande le modèle B, disponible à partir du 2026-11-21T04:00Z), ou demande un mot à Lazar.
6. **Mesures définitives versées et suivies.** Il faut le compte rendu `mesures-definitives-commit-course-v1.md` (`527ab727…`, non commité à la rédaction) commité sur `main`, avec ses seize sorties scellées (déjà prises par le commit `478111c2`). Preuve : geste 3 (d).
7. **Vérification courte de ce feu par un lecteur neuf**, sur les seuls points de l'arbitrage (« Une vérification courte […] du feu version 4 par un lecteur neuf […] précède […] le feu »), rendue sans bloquant. Puis :
   - les champs remplis ;
   - le feu scellé et versé sous `registres/t07-etape-b-bis/feu-bbis-v4.txt`, avec son compagnon ;
   - le feu inscrit par une ligne du registre des décisions, **jamais au registre propre** (celui-ci n'admet que les huit clés du texte scellé ; correction de la phrase « inscrit au registre propre » du projet version 3) ;
   - le tout commité et poussé sur `main`.
8. **Opérateur neuf**, dans une session interactive :
   - ouverte avec le dépôt de travail `/home/user/controle-ia-travail` comme dossier d'origine (R-3114 : le crochet ne se charge qu'ainsi) ;
   - capable de répondre aux demandes d'autorisation que déclencheront les gestes 6, 13 et 14 (l'étiquette `bbis-t07-v1` n'est pas accordée d'avance dans `.claude/settings.json`) ;
   - qui n'a lu aucun résultat de l'étape B, de 7a, de 7b, de T0.6 ni de P3-bis.
9. **Budget du jour.** La dépense du jour, comptée à l'heure de Paris de 23:00Z à 23:00Z, recharges comprises, plus le pire cas de cette course (20,20 USD, § 6), doit rester sous 100 euros (≈ 108 USD au taux déclaré). Règle de R-3124, maintenue par GO-2026-11-18-03 (2). La mère le vérifie au registre des dépenses et l'écrit.

**Conditions du projet version 3, désormais levées** :

- **Nœud « entropie » (N-1).** L'écart d'entropie est couvert par GO-2026-11-18-03 (1). Celui de l'épreuve de niveau et sa clause d'antériorité sont couverts par le troisième addendum, accordé par la mère sous GO-2026-11-18-05 et R-3170 (8) (R-3191).
- **Nœud « recharge » (N-2).** GO-2026-11-18-03 (2) maintient le plancher de 20 USD, en plus du budget de 100 euros par jour, recharges comprises.
- **Trace du pilote de la commande.** Remplacée par le geste 6, au commit de la course.
- **Outil du loueur.** Geste 4.
- **Portillon des essais.** Levé par les mesures définitives : 151 et 25, sous Python 3.13 et 3.11.
- **Crochet.** Son compagnon d'empreinte est désormais présent ; sa preuve de chargement est le geste 2.
- **Nombre de relances.** Fixé ici (§ 7).

---

## § 1 — LIGNES D'ACCORD

- **Ligne d'accord de calcul : GO-2026-11-14-09** (type « calcul », 40,00 USD, échéance 2026-11-22). Elle porte :
  - une A100 seulement, une relance au plus ;
  - une garde de débit ;
  - un feu écrit de la mère portant ce numéro avant toute location ;
  - l'arrêt et la destruction par identifiant (R10).
  Extrait fidèle : `registres/t07-etape-b-bis/go-bbis-v2.txt` (`33f38e675ca2114674b6f7dd96727b222fae613ecb53b57ef16240b74aca8e62`), égal à la ligne 328 de `registres/go.md`, inscrit au registre propre (ligne `GO-BBIS`).
- **Course supplémentaire, une seule : GO-2026-11-16-11** (second addendum, contrôle carte-processeur).
- **Mesure de la dispersion des aires entre deux ordres de calcul : GO-2026-11-16-12.**
- **Opérateur : GO-2026-11-16-06.** La machine est créée par un sous-agent opérateur. Arrêt au premier refus de permission, du crochet ou du classifieur, sans rejeu, reformulation, découpage ni contournement. Préavis d'une ligne à Lazar au moment du geste. Échéance 2026-11-18 : voir § 0, condition 5.
- **Accord de lancement et de dépense de Lazar**, 2026-11-18 vers 02:14Z, verbatim « Billet sur le contrôle de l'IA — un seul run manque : la course de l'étape B bis. : go » (R-3129). Il ne dispense ni des préalables ni de ce feu.
- **Trois décisions de l'étape B bis : GO-2026-11-18-03** (R-3149) :
  - (1) écart d'entropie couvert, réserve nommée au verdict ;
  - (2) plancher de 20 USD de crédit maintenu, en plus du budget de 100 euros par jour, recharges comprises ;
  - (3) plafond de 1,40 USD/h écrit au feu et prix relu après création ; le verdict dira que ce plafond tenait à un opérateur.
- **Amorce corrigée : GO-2026-11-18-04** (R-3162).
- **Autonomie de 24 heures : GO-2026-11-18-05** (R-3170).
  - R-3170 (8) : accord de la mère sur le troisième addendum, donné et inscrit (R-3191).
  - Le passage d'une clé à une machine reste à Lazar (champ 1).
  - Dépenses, chacune avec un devis écrit au registre avant le lancement : le devis de cette course est le § 6 de ce feu.
- **Passage des deux clés** : champ 1 (à la rédaction, GO-2026-11-18-06).
- **Plafond au lanceur ; plus aucune recharge jusqu'à nouvel ordre** : champ 2 (à la rédaction, GO-2026-11-18-07).

## § 2 — TEXTES QUI FONT FOI, À CITER DANS LE VERDICT

- **Texte scellé** : `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`. Ligne `SCELLEMENT-BBIS` du registre propre, 2026-11-14T12:30:30Z.
- **Premier addendum d'écart** : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7`. Ligne `ADDENDUM-ECART-1-BBIS`.
- **Second addendum d'écart** (contrôle carte-processeur à deux horizons) : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`, `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26`. Ligne `ADDENDUM-ECART-2-BBIS`.
- **Troisième addendum d'écart** : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md`, `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872`. Il porte :
  - la chaîne version 6, hors de la fiche de code ;
  - l'entropie changée ;
  - l'épreuve de niveau rejouée et sa clause d'antériorité ;
  - la lecture déclarée de la liste d'arrêt.
  Ligne `ADDENDUM-ECART-3-BBIS`, présente une fois à la l. 9 du registre voisin au commit de la course, 2026-11-18T05:46:36Z.
- **Registre propre** : `registres/t07-etape-b-bis-v1.md`. Lignes : `SCELLEMENT-BBIS`, `ABSENCE-B-BBIS`, `CODE-BBIS` version 1 (remplacée), `CODE-BBIS` version 2 (en vigueur), `GO-BBIS`. Jamais `registres/scellements-v1.md` : une clé de l'étape B bis dans ce registre partagé ferait refuser la création.
- **Registre voisin des addenda** : `registres/t07-etape-b-bis-v1-addenda-v1.md`. Aucun code ne le lit. **Un verdict qui ne cite pas les trois lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS` et `-3-BBIS` n'est pas scellé.**

## § 3 — CODE DE LA COURSE, COMMIT, MESURES SCELLÉES

- **Commit de la course, fixé une fois** : `438a9c5257bdc4fa65f25c42cc89753a049b4586`. Il porte le troisième addendum scellé et sa ligne `ADDENDUM-ECART-3-BBIS`. Il est présent sur `origin/main`, et le commit de la fiche `05cd22aa15382f61eb62b9e7817890dde728dd5f` en est un ancêtre (relevé par le rédacteur, à rejouer au geste 3). **Branche de code passée à l'amorce : `main`.** Toute mesure et toute commande de ce feu portent ce commit exact.
- **Fiche de code en vigueur** : `registres/t07-etape-b-bis/code-bbis-v2.json`, `4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb`. Elle cite 63 fichiers au commit de la fiche `05cd22aa…` : 22 sous `src/controle_ia/t07bbis/`, 21 scripts, 20 essais. La garde d'entrée de la marche les contrôle sur la machine.
  - Entropie : `149084685129585384182032033013812122656`. Elle est changée par rapport à la première fiche (TA-3 du troisième addendum, GO-2026-11-18-03 (1)).
  - Épreuve de niveau rejouée : `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json`, `da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919`. Niveau décisif retenu : 0,99.
  - Le second addendum épinglait l'épreuve `641adeb5…` de la première fiche ; elle est absente du dépôt. Cet écart et la clause d'antériorité (épreuve versée le 2026-11-17 à 11:03:40Z, après la course du 16 novembre qui avait relu les données de 7b sans écrire de score) sont couverts par TA-4, TA-5 et le § 0 du troisième addendum (correction 1 de la contre-lecture du projet version 3).
- **Chaîne de lancement version 6**, hors de la fiche, rattachée par le § 6 du troisième addendum. Empreintes **entières** :
  - amorce `scripts/amorce_bbis_v6.sh` : `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` (31 075 octets, 41 436 caractères en base64) ;
  - lanceur `scripts/lancer_bbis_v6.sh` : `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` ;
  - essais de la chaîne `tests/test_chaine_bbis_v6_v1.py` : `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca`.
  Elle a été contre-lue sous quatre angles par des agents neufs, avec arbitrage (`688abea5…`, R-3188). Le projet version 3 citait la chaîne version 5 et son plancher 176 : c'est remplacé.
- **Lanceur joué depuis la racine du dépôt**, `PYTHON_BBIS` posé en chemin absolu, `/home/user/controle-ia-travail/.venv/bin/python`, pour toutes ses sous-commandes. Un chemin relatif rend un faux refus dans `essais-du-commit` (répétition, § 3).
- **Mesures scellées au commit exact** (`mesures-definitives-commit-course-v1.md`, `527ab727cf8edc8789352cb908293705236d1a9661540dd3ecff4cce9bba0fbc`, verdict « tout conforme ») :
  - **Plancher d'essais, geste B.2.**
    - Sous Python 3.13.18 : code 0, « 151 passed, 25 skipped, 4 warnings », 516 fichiers, liste `d48e74d31bce24bfb0774e9d8ae24bf4325058a47152d5d3abb3c7117a49edc0`, sortie d'erreur vide.
    - Sous Python 3.11.18 : code 0, « 151 passed, 25 skipped », mêmes 516 fichiers, même liste.
    - Sorties : `commande-1-…-sortie-lanceur.txt` `35805d014b504c3e6c88d39eb41e20b6897d6e5f1eedde4b1c897ed65449f3e7`, `commande-1-…-essais.txt` `f6b483ef0e18f050d73aaaea99b2a9247ab4302a5eadcfcffcbd9c434ced35bc`, `commande-2-…-sortie-lanceur.txt` `acc5c4abe1b2de06c4bd79801d2dbe51339146e455d61e4fc3c726024dd0964c`, `commande-2-…-essais.txt` `762e561a244ad6a295c6461af94e9417c94ac1e833ddeb982ac1539beffa1f49`.
    - **Plancher de l'amorce : 151, partout dans ce feu (et non 176).**
  - **Code hors de la fiche, geste B.4.**
    - `git diff --quiet 05cd22aa 438a9c52… -- src requirements-gpu.txt pyproject.toml tests/conftest.py 'tests/test_t07bbis_*' 'tests/aide_t07bbis_*'` : code 0 (`commande-3-…`, `bce8326b86e8bfede07dc8bec63902be7f7c8917b42116fdb16cd2e3a7fad697`).
    - Fichiers réutilisés de la l. 19 du texte scellé : 11 sur 11 conformes (`commande-4-…`, `f2b4d3c9ef8e60f026a239c63a33bbacf19fb2d739fe7fb0bdc7eb3e42a8e130`).
    - Racine : 35 entrées aux deux commits, liste égale (`commande-5-…`, `b37b2d0f6abf57a9698adaf426a8b41064fe7ee40a25069c603c629469e83199`).
  - **Chaîne et addendum, geste B.3 hors loueur.**
    - Empreintes de la chaîne au commit, égales en entier au § 6 de l'addendum (`commande-6-…`, `25bbbbd40e0b1a9b9d10a784b1e3d07976df41e2be5fa4fa66f993ca74c33de5`).
    - Ligne `ADDENDUM-ECART-3-BBIS` présente une fois, chemin et empreinte entiers (`commande-7-…`, `7e352de624efdc55a085df2077468c6e3d0163e8d7cc9bc2c18f2eb48d84c6c3`).
    - Addendum conforme à son compagnon (`commande-8-…`, `6ccd117866c4780da038581783bac8c7d7d5e290dd9426c802cda3b556263059`).
  - **Ce qui reste à faire au feu** : le décodage du base64 de la commande imprimée. C'est le geste 13.
  - Toutes ces sorties sont sous `mesures-definitives-commit-course-v1/`, chacune avec son compagnon (seize compagnons conformes, revérifiés par le rédacteur).
- **Remarque des mesures, reprise** : un seul fichier de la racine diffère, par son contenu, entre `05cd22aa` et le commit de la course : `CLAUDE.md`, sur 3 lignes. Ni le code de la course, ni ses essais, ni l'amorce ne le lisent. Ce n'est pas un écart aux critères écrits.
- **LE CODE DE LA COURSE EST GELÉ.** La garde de création exige exactement deux lignes `CODE-BBIS` pour deux relances. Une troisième fiche ferait refuser la création. Aucune retouche n'est possible avant cette course.

## § 4 — DONNÉES

- **Branche d'entrée** : `calcul/t06-confirmation-7b-v1` ; course de 7b `20261111-151701-t06-reel`. Tête `55c3e3eb89a4650419f35999aaa4c54288275b0d`, relevée par le projet version 3 et **non relue par le rédacteur**, qui ne touche aucune branche de calcul. L'amorce n'en extrait que des fichiers nommés.
- **Branche de sortie**, neuve et exigée **absente** du distant avant la course : `donnees/t07-etape-b-bis-v2`. Le lanceur refuse si elle existe (« nouveau nom exigé ») et refuse si le distant est muet (« absence de la branche de sortie non prouvée »). Aucun repli silencieux (R5).
- **Dépôt de travail et lui seul** : `https://github.com/lciric/controle-ia-travail.git`. Jamais `lciric/controle-ia`, qui sera la copie expurgée publique.

## § 5 — MACHINE ET OFFRE

- **Carte et ressources** :
  - une seule carte A100 SXM4 80 Go, aucune H200 (mot de Lazar seulement) ;
  - au moins 16 cœurs effectifs, au moins 128 000 Mo de mémoire vive, disque de 150 Go ;
  - stockage au plus 0,08 USD/h (clé `storage_cost` × 150 / 730).
- **Hôte** :
  - version CUDA servie par l'hôte (`cuda_max_good`, recopiée telle quelle de la recherche) d'au moins 13.0 ; clé absente ou illisible : refus ;
  - **pilote de série 595 ou 580** : `driver_version` commence par `595.` ou `580.` (bloquant de machine levé au feu, arbitrage, point 1). Il est recopié tel quel au registre des dépenses. Une offre sans cette clé ne peut pas être retenue.
  - Raison : l'amorce ne lit que « CUDA Version: ». Les pilotes des séries 610 à 620 affichent « CUDA UMD Version: ». L'instance 60952525 s'est arrêtée ainsi le 16 novembre, sur le pilote 615.71.09.
  - La série 595 est la seule éprouvée sur une vraie machine de cette chaîne (595.91.07 : instances 60760941 et 60953606). La série 580 ne l'a jamais été (réserve).
- **Prix de carte au plus 1,40 USD/h**, clé `dph_total` de l'offre. Il est tenu trois fois :
  - par le programme de choix de l'opérateur (geste 10) ;
  - par le lanceur version 6 (`PRIX_MAX_USD_H=1.40`, champ 2) ;
  - par le prix relu après création (geste 16).
- **Image** : `python:3.11-bookworm`, exigée par son nom par le lanceur version 6 (`IMAGE_COURSE`) et contrôlée par programme sur la ligne imprimée (geste 13, correction 7). Elle est nommée, non épinglée par un condensé (réserve).
- **Étiquette** : `bbis-t07-v1`, fixée par le texte scellé.
- **Choix de l'offre par programme, dans la sortie brute de la recherche, jamais retapée** (gestes 9 et 10). Le programme écarte les pilotes hors série et les prix au-dessus du plafond. Puis la sous-commande `offre-depuis-recherche` du **lanceur de la course** est jouée sur chaque survivante, de la moins chère à la plus chère. La première acceptée est retenue.
  - La sous-commande `offre` de `scripts/repetition_carte_bbis_v3.py` est **interdite ici** : elle exige l'étiquette de la répétition et 60 Go de disque, et refuserait l'offre de la course pour une raison étrangère au prix (correction 2).
- **Échéance de la minuterie : 13 heures**, calculée par commande au geste 12, `ECH=$(( $(date +%s) + 46800 ))`. Elle est refaite, avec les gestes 12 et 13, si la création attend plus de 30 minutes après la commande.
  - L'amorce refuse une échéance hors de l'intervalle ]maintenant ; maintenant + 24 h]. Elle exige la clé d'interface du conteneur (par son nom) avant d'armer la minuterie.
  - La minuterie demande ensuite la destruction toutes les 60 secondes, sans jamais juger le code de retour, et demande l'état « arrêtée » après cinq essais.
  - **Réserve** : la minuterie vit dans le conteneur et meurt avec lui. Une instance arrêtée facture son disque sans minuterie. La destruction finale reste un geste de session.
  - L'opérateur lit la ligne « minuterie lancée » au journal dans les cinq minutes (geste 18, correction 6).

## § 6 — DEVIS, PRIX, DÉPENSE, CRÉDIT

**Devis de la course** (exigé par GO-2026-11-18-05 avant le lancement) :

| | montant | source |
|---|---|---|
| coût attendu | 5,6 à 9,9 USD | texte scellé |
| coût attendu, mesure de dispersion comprise | 5,8 à 6,6 USD | second addendum |
| plafond horaire de carte | 1,40 USD/h | stockage ≤ 0,08 USD/h en plus |
| pire cas sous la minuterie | 13 h × (1,40 + 0,08) = **19,24 USD** | |
| pire cas avec 12 h de disque après un arrêt de débit | ≈ **20,20 USD** | ≤ 0,96 USD de disque, section 6 du second addendum (correction 3) |
| coupure de la garde de dépense | 39,50 USD | inclusive |
| plafond de la ligne d'accord | 40,00 USD | |

**Cumul de la ligne et marges** :

- Cumul déjà dépensé sous GO-2026-11-14-09 : **5,989 USD**. Il se compose des répétitions (0,749), de la première création du 16 novembre (0,10) et de la relance unique (5,14) (`registres/depenses.md`, l. 476, 481 et 482). Aucune dépense depuis sous cette ligne.
- C'est **ce** cumul, celui de la ligne, que l'opérateur passe à la garde de dépense.
- Cumul de la ligne au pire après cette course : 5,989 + 20,20 = **26,19 USD** sur 40.
- Reste sous la coupure après ce pire cas : 39,50 − 26,19 = **13,31 USD**.
- Aucune autre course n'est permise après celle-ci (§ 7).

**Garde de dépense** (`bash scripts/lancer_bbis_v6.sh depense CUMUL PRIX`) :

- C'est une calculette, sans guetteur, sans boucle, sans lecture du vrai cumul chez le loueur.
- Elle refuse dès que le cumul relevé plus un quart d'heure de carte atteint 39,50 USD, et imprime alors la commande de destruction.
- Elle est rejouée une fois avant la création (geste 11), puis à chaque heure de marche (geste 19), avec cumul = 5,989 + heures écoulées depuis la création × prix relu.
- **Garde de débit**, dans le code : arrêt si la marche projetée dépasse 11,0 h.

**Crédit du loueur** (le code de la course ne contrôle pas le crédit : la règle est tenue par l'opérateur et par ce feu) :

- **avant la création** : au moins 20,00 USD, relevé dans l'heure (champ 3, geste 8) ;
- **condition de marge, ajoutée par le rédacteur** : crédit relevé − 13 × débit horaire des autres instances en marche du compte ≥ 20,00 USD.
  - Motif : le crédit est commun ; une autre instance en marche le consomme pendant la course. Avec la relance du témoin de Bailey à ≈ 1,22 USD/h, il faudrait ≈ 35,9 USD.
  - C'est plus strict que GO-2026-11-18-03 (2) ; voir réserve 10 ;
- **pendant la course**, à chaque rejeu horaire (correction 4) : crédit relevé par la sous-commande `credit` du lanceur de la répétition, qui ne lit que le champ du crédit et n'affiche aucune clé. **Sous 8,00 USD, l'opérateur détruit proprement par l'identifiant et rend compte.** Un arrêt côté loueur perdrait la poussée, donc toute la dépense.
- La recharge automatique du loueur (5 USD sous 5 USD) était encore configurée à 05:54Z, contre l'ordre de GO-2026-11-18-07 (R-3196, R-3197). L'opérateur ne compte pas sur elle et ne la déclenche jamais.

**Prix relu après création** (geste 16) :

- C'est la clé `dph_total` de l'instance. Elle a jusqu'ici valu le prix de carte de l'offre plus son stockage (par exemple 1,2547 + 0,0164 ≈ 1,2700 USD/h le 15 novembre).
- Règle : prix relu au-dessus de **1,40 + stockage de l'offre retenue (`stockage_usd_h`, au plus 1,48)** : destruction aussitôt par identifiant, puis nœud. Lecture déclarée : réserve 12.

## § 7 — RELANCES ET ÉCHÉANCES

- **Nombre passé à la garde de création : 2**, en onzième argument de la sous-commande `commande`. Ce nombre n'est dérivé d'aucune pièce : la garde ne contrôle que la valeur qu'on lui passe.
- **Motif** : la relance unique de l'accord original est consommée :
  - premier départ perdu sur la garde du pilote, instance 60952525, ≈ 0,10 USD ;
  - relance unique, instance 60953606, ≈ 4,23 h, ≈ 5,14 USD, arrêtée sur le contrôle carte-processeur, aucun score écrit.
  La course de ce feu est la course supplémentaire de GO-2026-11-16-11 : la seconde relance au sens de la garde, et **la dernière course accordée**.
- **Une perte au démarrage la consomme** (pilote, image, clé, journal muet, machine qui ne démarre pas). Après elle, aucune autre course sans un mot neuf de Lazar : la garde refuse toute troisième relance.
- Trois branches de sortie de courses antérieures existent sur le distant (`calcul/t07bbis-repetition-v1`, `-v2`, `-v4`). Elles ne sont pas ouvertes.
- **Aucune création après le samedi 2026-11-21 à 12:00:00Z** (la garde refuse une relance au-delà ; c'est un nœud, et le billet sort sans l'étape B bis). **Aucune création après 2026-11-22T23:59:59Z** (échéance de l'accord, contrôlée par la garde).
- Échéance dure du programme : le verdict scellé de l'étape B bis est dû au plus tard le dimanche 2026-11-22.

## § 8 — JAMAIS DÉTRUITES PAR CETTE COURSE

- **Règle** : aucune instance n'est détruite par cette course hormis celle dont l'identifiant est lu au geste 15. Ni aucun serveur.
- **Connues à la rédaction** (registres, non vérifiées par le rédacteur) :
  - 58936096, 58936099, 58936100 (arrêtées) ;
  - 60988826 (jeu de l'idée du poids du nul, arrêtée, non détruite) ;
  - **61170458** (relance du témoin de Bailey, autre session, en marche) ;
  - le serveur `sauvegarde-temoin-bailey-v2` chez l'hébergeur allemand.
- 61049303 a été détruite le 18 novembre vers 02:38Z. 60480302, 60599797 et 60670453 restent refusées par le code du lanceur (`INSTANCES_D_AUTRES_SESSIONS`), qu'elles existent encore ou non.
- **Témoin de destruction** : une instance de la liste lue au geste 7, autre que celle de la course, choisie par programme. Si elle a disparu au geste 23, un témoin neuf est pris dans une liste neuve.

## § 9 — CE QUE L'OPÉRATEUR LIT, ET CE QU'IL NE LIT JAMAIS

- **Liste blanche des entrées de la marche** : point 1 du plan d'analyse du texte scellé (l. 98), tenue par le code. **Liste « Jamais »** : même point. L'ouverture par la chaîne d'un de ces fichiers est un arrêt de la liste d'arrêt (l. 191).
- **L'opérateur lit seulement** :
  - les sorties des gestes de ce feu ;
  - au journal de la machine, les seules lignes `BBIS` d'étapes : minuterie, empreinte de l'amorce, pilote, carte, dépôt, essais du paquet, marche (début et code), poussé, traces, FIN, fin, ARRET, MINUTERIE, REFUS.
- **Il ne lit jamais** :
  - rien sous `diag/`, `runs/` ni `donnees/` ;
  - le contenu d'aucune branche `donnees/` ou `calcul/` (il ne relève que la présence de la branche de sortie, geste 21) ;
  - la réponse brute de la création, qui peut porter la clé propre à l'instance (R-3004) ;
  - la liste brute des instances, qui peut porter des clés d'autres sessions (R-2829) ;
  - aucune valeur de clé.
- **Pas de `env`, pas de `printenv`.**

---

## § 10 — GESTES NUMÉROTÉS

**Conventions** :

- Chaque appel au shell commence par le **préambule P**, `cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh &&`. Il fixe `R`, `C`, `D`, `PYTHON_BBIS` (chemin absolu), `VASTAI_BBIS`, `PATH`, `umask 077` et `set -o pipefail`. Le shell ne garde rien d'un appel à l'autre ; les valeurs passent par des fichiers du dossier d'envoi, écrits par programme, jamais retapés.
- Tout fichier est écrit sous un nom neuf (R12). Toute sortie est gardée dans le dossier d'envoi pour le compte rendu.
- **Arrêt** veut dire : rien de plus n'est lancé ; si une instance existe, gestes 22 et 23 ; puis compte rendu d'une ligne à la mère.
- Tout refus d'une permission, du crochet (hors le refus attendu du geste 2 (e)) ou du classifieur arrête au premier refus, sans rejeu, reformulation, découpage ni contournement (GO-2026-11-16-06).

### Phase A — préparatifs, aucun appel au loueur

**Geste 1. Dossier d'envoi neuf et préambule.**
```bash
cd /home/user/controle-ia-travail && test ! -e /home/user/bbis-course-envoi-feu-v4 && mkdir -m 700 /home/user/bbis-course-envoi-feu-v4 && cat > /home/user/bbis-course-envoi-feu-v4/env.sh <<'FIN'
R=/home/user/controle-ia-travail
C=438a9c5257bdc4fa65f25c42cc89753a049b4586
D=/home/user/bbis-course-envoi-feu-v4
export PYTHON_BBIS=/home/user/controle-ia-travail/.venv/bin/python
export VASTAI_BBIS=/home/user/vastai-env-bbis-feu-v4/bin/vastai
export PATH=/home/user/vastai-env-bbis-feu-v4/bin:$PATH
umask 077
set -o pipefail
FIN
sha256sum /home/user/bbis-course-envoi-feu-v4/env.sh; date -u +%FT%TZ
```
Sortie attendue : `8c78b19a897f1d6550d3fd3b3692fad3617d0492583fe5f5397bb15d059e61bf  /home/user/bbis-course-envoi-feu-v4/env.sh`, puis l'heure.
Arrêt si : le dossier existe déjà (la mère donne un nom neuf), ou si l'empreinte diffère.

**Geste 2. Session de l'opérateur : crochet chargé, compagnon, registre des accords lisible.**
(a) `echo "dossier de projet : ${CLAUDE_PROJECT_DIR:-vide}"` — attendu `dossier de projet : /home/user/controle-ia-travail`.
(b) `cd /home/user/controle-ia-travail/.claude/hooks && sha256sum -c garde_calcul.py.sha256 && sha256sum garde_calcul.py` — attendu `garde_calcul.py: OK`, puis `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850  garde_calcul.py` (correction 10 : le compagnon est désormais présent).
(c) Le registre des accords, lu par le lecteur même du crochet, en lecture seule :
```bash
cd /home/user/controle-ia-travail && /home/user/controle-ia-travail/.venv/bin/python -I -c 'import sys; sys.path.insert(0, "/home/user/controle-ia-travail/.claude/hooks"); import garde_calcul as g; r = g.lire_go(g.REGISTRE_GO); x = r["GO-2026-11-14-09"]; print("registre lisible :", len(r), "accords ;", x["type"], x["accorde"], x["echeance"], x["par"])'; echo "code $?"
```
Attendu : `registre lisible : <n> accords ; calcul 2026-11-14 2026-11-22 Lazar`, puis `code 0`. À la rédaction, la sortie est `GARDE (registres/go, R10) — commande bloquée : registre GO mal formé ligne 371 : dates illisibles`, `code 2` : c'est la condition 4 du § 0.
(d) Cas sain : `echo crochet-cas-sain` — attendu `crochet-cas-sain`.
(e) Artefact, **refus attendu et prévu par ce feu** (il ne compte pas comme premier refus ; c'est la seule preuve de comportement que le crochet est chargé) : `echo crochet-artefact ; : pkill` — attendu : un refus du crochet portant « R10 — arrêt par motif de ligne de commande interdit ». La commande est sans effet si elle passe (`:` ne fait rien).
Arrêt si : (a) ne rend pas le dépôt de travail ; (b) diffère ; (c) ne rend pas `code 0` ; (e) imprime `crochet-artefact` (crochet non chargé) ; ou tout autre refus.

**Geste 3. Commit de la course, disque de la session, mesures scellées.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && git cat-file -e "$C^{commit}" && git fetch -q origin main && git merge-base --is-ancestor "$C" origin/main && echo "a. commit de la course sur main distant" && git merge-base --is-ancestor 05cd22aa15382f61eb62b9e7817890dde728dd5f "$C" && echo "b. commit de la fiche ancêtre du commit de la course" && git diff --quiet "$C" -- scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh scripts/lancer_repetition_bbis_v3.sh scripts/repetition_carte_bbis_v3.py src/controle_ia/t07bbis src/controle_ia/gardes.py src/controle_ia/scellement.py src/controle_ia/manifeste.py registres/t07-etape-b-bis-v1.md registres/t07-etape-b-bis/code-bbis-v1.json registres/t07-etape-b-bis/code-bbis-v2.json registres/t07-etape-b-bis/go-bbis-v2.txt registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md && echo "c. fichiers lus par la session égaux au commit de la course" && echo "c'. fichiers non suivis : $(git status --porcelain --untracked-files=all -- src/controle_ia/t07bbis scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh scripts/lancer_repetition_bbis_v3.sh scripts/repetition_carte_bbis_v3.py | grep -c .)" && sha256sum scripts/amorce_bbis_v6.sh scripts/lancer_bbis_v6.sh tests/test_chaine_bbis_v6_v1.py prereg/T0.7-etape-B-bis-v1-addendum-ecart-3-v1.md registres/t07-etape-b-bis/feu-bbis-v4.txt && ( cd registres/t07-etape-b-bis && sha256sum -c feu-bbis-v4.txt.sha256 ) | sed 's/^/c". /' && cd docs/notes/prealables-course-etape-b-bis-v1 && sha256sum -c mesures-definitives-commit-course-v1.md.sha256 arbitrage-contre-lecture-amorce-v6-v1.md.sha256 repetition-mesure-plancher-py311-py313-v1.md.sha256 && git ls-files --error-unmatch mesures-definitives-commit-course-v1.md > /dev/null && echo "d. compte rendu des mesures suivi par git" && cd mesures-definitives-commit-course-v1 && for f in *.sha256; do sha256sum -c "$f"; done | grep -c ': OK$'
```
Sortie attendue, dans l'ordre :
- les lignes a, b et c ;
- `c'. fichiers non suivis : 0` ;
- les empreintes, chacune sur 64 caractères :
  - `26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5` pour l'amorce ;
  - `3224ce14dc3fefe7cc46774072f65288a39c3fe760f325e311c5f948c45344b7` pour le lanceur ;
  - `f36571bd7fb7f5693f8e45433f44c7826722b9baf995ce219038923d486b49ca` pour les essais ;
  - `e5604cbdce509958e1f3e3bc3a36c8d17a78c8900b5f93a2102fff9b51d07872` pour l'addendum ;
  - pour le feu, l'empreinte inscrite par la mère au registre des décisions (comparée à l'œil, sur 64 caractères) ;
- `c". feu-bbis-v4.txt: OK` ;
- trois lignes `: OK` ;
- la ligne d ;
- `16`.
Arrêt si : une ligne manque, une empreinte diffère, un fichier non suivi existe, ou le compte n'est pas 16.

**Geste 4. Outil du loueur réinstallé, version inscrite, option `-y` éprouvée sans réseau.**
(a) Installation dans un environnement dédié neuf (réseau des paquets seulement) :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && test ! -e /home/user/vastai-env-bbis-feu-v4 && /usr/bin/python3 -m venv /home/user/vastai-env-bbis-feu-v4 && /home/user/vastai-env-bbis-feu-v4/bin/pip install -q --no-cache-dir -r requirements-pilotage.txt && /home/user/vastai-env-bbis-feu-v4/bin/pip show vastai | sed -n 1,2p | tee "$D/g4-outil.txt" && echo "outil appelé : $(command -v vastai)" | tee -a "$D/g4-outil.txt" && for s in "search offers" "show instances" "show user" "destroy instance" "logs"; do "$VASTAI_BBIS" $s --help > /dev/null 2>&1; echo "aide de « $s » : code $?"; done | tee -a "$D/g4-outil.txt" && "$VASTAI_BBIS" destroy instance --help 2>&1 | grep -n -e ' -y' -e '--yes' | tee -a "$D/g4-outil.txt"
```
Attendu :
- `Name: vastai` et `Version: 1.8.3` (version figée par `requirements-pilotage.txt` ; à inscrire au compte rendu) ;
- `outil appelé : /home/user/vastai-env-bbis-feu-v4/bin/vastai` ;
- cinq lignes `code 0` ;
- au moins une ligne d'aide qui nomme `-y` ou `--yes`.

(b) Option `-y` éprouvée sur un cas sain, et sur un artefact, **sans réseau** (`unshare -n -r`). Aucune demande ne peut partir, rien n'est détruit, rien n'est dépensé ; l'identifiant 1 n'est pas une instance du compte.
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && unshare -n -r "$VASTAI_BBIS" destroy instance 1 -y < /dev/null > "$D/g4-y-sain.txt" 2>&1; echo "cas sain : code $? ; demandes de confirmation : $(grep -c -i -e '\[y/n\]' -e 'y/n' "$D/g4-y-sain.txt")"; unshare -n -r "$VASTAI_BBIS" destroy instance 1 < /dev/null > "$D/g4-y-artefact.txt" 2>&1; echo "artefact : code $? ; demandes de confirmation : $(grep -c -i -e '\[y/n\]' -e 'y/n' "$D/g4-y-artefact.txt")"; head -c 400 "$D/g4-y-sain.txt"; echo; head -c 400 "$D/g4-y-artefact.txt"
```
Attendu :
- cas sain : `demandes de confirmation : 0`, et une erreur de connexion (aucune question posée, demande tentée) ;
- artefact : `demandes de confirmation : 1` ou plus (la version demande une confirmation sans `-y`, défaut de R-2789).
- Si l'artefact ne montre aucune demande, la version ne confirme pas : c'est inscrit, ce n'est pas un arrêt, car la destruction n'est jamais jugée par un code de sortie mais par l'absence prouvée (geste 23).

Arrêt si : l'installation échoue ; la version n'est pas 1.8.3 ; une aide ne rend pas le code 0 ; aucune ligne d'aide ne nomme `-y` ; le cas sain montre une demande de confirmation ; `unshare` est indisponible (l'option n'est alors pas éprouvée : compte rendu, la mère décide).

**Geste 5. Programmes de l'opérateur, écrits et vérifiés par empreinte.**
```bash
cd /home/user/bbis-course-envoi-feu-v4 && umask 077 && test ! -e choisir_offre.py && cat > choisir_offre.py <<'PY'
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
L = d.get("offers") if isinstance(d, dict) else d
if not isinstance(L, list):
    print("ARRET : sortie de la recherche illisible"); sys.exit(2)
def n(x):
    if isinstance(x, bool):
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None
garde = []
for o in L:
    if not isinstance(o, dict) or isinstance(o.get("id"), bool) or not isinstance(o.get("id"), int):
        continue
    dv = o.get("driver_version")
    pr, st, cu = n(o.get("dph_total")), n(o.get("storage_cost")), n(o.get("cuda_max_good"))
    m = []
    if not (isinstance(dv, str) and (dv.startswith("595.") or dv.startswith("580."))):
        m.append("pilote %r" % (dv,))
    if o.get("gpu_name") != "A100 SXM4" or n(o.get("num_gpus")) != 1 or not (n(o.get("gpu_ram")) or 0) >= 79000:
        m.append("carte")
    if cu is None or cu < 13.0:
        m.append("cuda_max_good %r" % (o.get("cuda_max_good"),))
    if pr is None or not 0 < pr <= 1.40:
        m.append("prix %r" % (o.get("dph_total"),))
    if st is None or st * 150 / 730 > 0.08:
        m.append("stockage %r" % (o.get("storage_cost"),))
    if not (n(o.get("cpu_cores_effective")) or 0) >= 16:
        m.append("coeurs")
    if not (n(o.get("cpu_ram")) or 0) >= 128000:
        m.append("memoire vive")
    if not (n(o.get("disk_space")) or 0) >= 150:
        m.append("disque")
    print("offre %s | prix %s | stockage %s USD/Go/mois | pilote %s | cuda %s | %s" % (
        o["id"], o.get("dph_total"), o.get("storage_cost"), dv, o.get("cuda_max_good"),
        "RETENABLE" if not m else "ecartee : " + ", ".join(m)))
    if not m:
        garde.append((pr, o["id"], dv))
garde.sort()
with open(sys.argv[2], "x", encoding="utf-8") as f:
    f.write("".join("%s %s\n" % (i, dv) for _, i, dv in garde))
print("CANDIDATES %d" % len(garde))
sys.exit(0 if garde else 2)
PY
test ! -e inventaire.py && cat > inventaire.py <<'PY'
import json, math, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
L = d.get("instances") if isinstance(d, dict) else d
if not isinstance(L, list) or any(not isinstance(i, dict) or "id" not in i for i in L):
    print("ARRET : liste des instances illisible"); sys.exit(2)
a = sys.argv[2:] + ["-", "-", "-"]
mien = None if a[0] == "-" else a[0]
plafond = None if a[1] == "-" else float(a[1])
sortie = None if a[2] == "-" else a[2]
def prix(i):
    p = i.get("dph_total")
    return float(p) if isinstance(p, (int, float)) and not isinstance(p, bool) else None
autres, course, debit = [], [], 0.0
for i in L:
    ident, lab, st = str(i["id"]), i.get("label"), i.get("actual_status")
    print("instance %s | etiquette %s | etat %s | prix %s" % (ident, lab, st, prix(i)))
    if lab == "bbis-t07-v1":
        course.append(ident)
    elif ident != mien:
        autres.append(ident)
        if st == "running":
            p = prix(i)
            debit += p if p is not None else float("nan")
print("INSTANCES %d ; ETIQUETTE bbis-t07-v1 : %s ; AUTRES %s ; DEBIT DES AUTRES EN MARCHE %.4f USD/h" % (
    len(L), course, autres, debit))
if math.isnan(debit):
    print("ARRET : prix illisible sur une autre instance en marche"); sys.exit(2)
if sortie is not None:
    if not autres:
        print("ARRET : aucune autre instance, aucun temoin possible"); sys.exit(2)
    with open(sortie, "x", encoding="utf-8") as f:
        f.write("TEMOIN=%s\nDEBIT_AUTRES=%.4f\n" % (autres[0], debit))
code = 0
if mien is not None:
    vues = [i for i in L if str(i["id"]) == mien]
    if len(vues) != 1:
        print("COURSE %s ABSENTE" % mien); sys.exit(4)
    i = vues[0]
    p, dv = prix(i), i.get("driver_version")
    print("COURSE %s | etat %s | prix relu %s | etiquette %s | carte %s | pilote %s" % (
        mien, i.get("actual_status"), p, i.get("label"), i.get("gpu_name"), dv))
    if plafond is not None:
        m = []
        if p is None or p > plafond:
            m.append("prix relu %r au-dessus de %.4f ou illisible" % (p, plafond))
        if i.get("label") != "bbis-t07-v1":
            m.append("etiquette %r" % (i.get("label"),))
        if dv is not None and not (isinstance(dv, str) and (dv.startswith("595.") or dv.startswith("580."))):
            m.append("pilote %r" % (dv,))
        print("RELECTURE " + ("CONFORME" if not m else "HORS BORNES : " + " ; ".join(m)))
        code = 0 if not m else 3
sys.exit(code)
PY
test ! -e lire_creation.py && cat > lire_creation.py <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1], encoding="utf-8"))
except Exception as e:
    print("CREATION ILLISIBLE (%s)" % type(e).__name__); sys.exit(2)
s = d.get("success") if isinstance(d, dict) else None
c = d.get("new_contract") if isinstance(d, dict) else None
ok = isinstance(c, int) and not isinstance(c, bool) and c > 0
print("success %r ; new_contract %s" % (s, c if ok else "illisible"))
if s is True and ok:
    with open(sys.argv[2], "x", encoding="utf-8") as f:
        f.write("ID=%d\n" % c)
    sys.exit(0)
sys.exit(2)
PY
sha256sum choisir_offre.py inventaire.py lire_creation.py
```
Sortie attendue :
```
2d32e1ace8f4539f3201997de103a64a9f3d4bba6fc524d008d0a012254b23b4  choisir_offre.py
a279a91c27ad2a0e1f8b94dccc007524255fee7f60d331b914fb8d283c171100  inventaire.py
1fa46d02def8602a2bf026d70072535c056c4a23770049b93667aceafce29e09  lire_creation.py
```
Arrêt si : une empreinte diffère (le fichier est effacé et réécrit, une fois ; second écart : arrêt).
Ces trois programmes ont été éprouvés par le rédacteur sur des données fabriquées, cas sain et artefacts. Le programme de choix écarte bien les pilotes 615, 620 et 570, la carte de 40 Go, le prix de 1,45, le stockage de 0,50 et le pilote absent, puis classe les survivantes par prix. L'inventaire refuse un débit illisible, l'absence de témoin, un prix relu au-dessus du plafond, un pilote 615, et une instance absente. La lecture de la création refuse `success` faux et une réponse illisible, et n'imprime jamais la clé de l'instance.

**Geste 6. Répétition à blanc de la commande et de l'égalité des arguments, sur une offre fabriquée — aucune création.**
Ce geste demande que le registre des accords soit lisible (§ 0, condition 4). Les commandes (c) contiennent le texte d'une ligne de création, que le crochet contrôle. Il peut aussi venir une demande d'autorisation.
(a) Commande imprimée pour l'offre fabriquée d'identifiant 1, jamais louée :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && mkdir "$D/pilote" && printf '{"carte": "A100 SXM4 80GB", "coeurs": 32.0, "cuda_max_good": 13.2, "disque_go": 150.0, "etiquette": "bbis-t07-v1", "id": 1, "memoire_vive_mo": 257000.0, "prix_usd_h": 1.2, "source": "offre fabriquée du pilote, jamais louée", "stockage_usd_h": 0.03}\n' > "$D/pilote/offre-fabriquee.json" && ECH=$(( $(date +%s) + 46800 )) && RUN_BBIS=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1 && printf 'OFFRE_ID=1\nRUN_BBIS=%s\nECH=%s\nT_COMMANDE=%s\n' "$RUN_BBIS" "$ECH" "$(date +%s)" > "$D/pilote/valeurs.sh" && FEU_TEXTE="feu-bbis-v4 $(sha256sum < registres/t07-etape-b-bis/feu-bbis-v4.txt | cut -c1-64) GO-2026-11-14-09 GO-2026-11-16-11" && git fetch -q origin main && bash scripts/lancer_bbis_v6.sh commande "$R" "$D/pilote/offre-fabriquee.json" 1 "$C" main 20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 "$RUN_BBIS" "$ECH" "$FEU_TEXTE" 2 python:3.11-bookworm > "$D/pilote/commande-imprimee.txt" 2> "$D/pilote/commande.err"; echo "commande : code $? ; sortie d'erreur : $(wc -c < "$D/pilote/commande.err") octets"; sed -n 1p "$D/pilote/commande-imprimee.txt"
```
Attendu : `commande : code 0 ; sortie d'erreur : 0 octets`, puis `BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce 26f954e9e9783bf9) :`. **La ligne imprimée n'est jamais jouée.**
(b) Le geste 13, joué avec `X="$D/pilote"` au lieu de `X="$D"`. Mêmes sorties attendues.
(c) L'égalité des arguments, avec un outil factice seulement. Dans un environnement vidé (`env -i`), `vastai` est une fonction qui imprime ses arguments, et les deux jetons sont des valeurs factices. Aucune clé réelle n'est présente, et aucun outil réel n'est sur le chemin :
```bash
cd /home/user/bbis-course-envoi-feu-v4/pilote && umask 077 && test ! -e ligne-courte.sh && cat > ligne-courte.sh <<'FIN'
GO_ID=GO-2026-11-14-09 vastai create instance "$OFFRE_ID" --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=$RUN_BBIS -e ECHEANCE_UTC_S=$ECH -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo $(cat amorce.b64) | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"
FIN
env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-imprimee.sh' > argv-imprimee.bin && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-courte.sh' > argv-courte.bin && cmp argv-courte.bin argv-imprimee.bin && echo "ARGUMENTS EGAUX A LA LIGNE IMPRIMEE" && tr '\0' '\n' < argv-courte.bin | cut -c1-80 | head -n 22
```
Attendu : `ARGUMENTS EGAUX A LA LIGNE IMPRIMEE`, puis les arguments, coupés à 80 caractères : `GO_ID=GO-2026-11-14-09`, `create`, `instance`, `1`, `--raw`, …, `-c`, `echo …`. Le jeton factice apparaît, jamais une vraie clé.
Arrêt si : (a) rend autre chose que le code 0 ; un « BBIS REFUS » est imprimé ; (b) ou (c) diffère. Compte rendu, rien n'est créé. Un refus du lanceur ici aurait arrêté le geste 12 : c'est la raison de cette répétition.

### Phase B — jour de la création (toutes les conditions du § 0 levées)

**Geste 7. Inventaire des instances et témoin** (premier appel au loueur, en lecture).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && F="$D/liste-g7.json" && ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); echo "lecture : code $?"; "$PYTHON_BBIS" -I "$D/inventaire.py" "$F" - - "$D/temoin.sh" | tee "$D/g7-inventaire.txt"; echo "inventaire : code $?"; rm -f -- "$F"; cat "$D/temoin.sh"
```
Attendu :
- `lecture : code 0` ;
- une ligne par instance (identifiant, étiquette, état, prix ; rien d'autre) ;
- `INSTANCES n ; ETIQUETTE bbis-t07-v1 : [] ; AUTRES [...] ; DEBIT DES AUTRES EN MARCHE x USD/h` ;
- `inventaire : code 0` ;
- `TEMOIN=<identifiant>` et `DEBIT_AUTRES=<x>`.
La liste brute est effacée aussitôt.
Arrêt si :
- la lecture échoue ;
- une instance porte déjà l'étiquette `bbis-t07-v1` (nœud) ;
- aucune autre instance n'existe (aucun témoin : la preuve d'absence serait impossible ; nœud) ;
- un prix est illisible sur une autre instance en marche.

**Geste 8. Crédit relevé — champ 3.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/temoin.sh" && v=$(bash scripts/lancer_repetition_bbis_v3.sh credit | tee -a "$D/g8-credit.txt" | sed -n 's/^BBIS REPETITION CREDIT \([0-9][0-9.]*\) USD.*$/\1/p'); h=$(date -u +%FT%TZ); printf 'T_CREDIT=%s\n' "$(date +%s)" > "$D/credit-heure.sh"; echo "crédit relevé $v USD à $h ; débit des autres en marche $DEBIT_AUTRES USD/h" | tee -a "$D/g8-credit.txt"; awk -v v="$v" -v d="$DEBIT_AUTRES" 'BEGIN { ok = (v != "" && v + 0 >= 20 && v - 13 * d >= 20); print (ok ? "CREDIT SUFFISANT" : "CREDIT INSUFFISANT"); exit !ok }' | tee -a "$D/g8-credit.txt"
```
Attendu :
- `BBIS REPETITION CREDIT <v> USD : suffisant (au moins 4 USD)` ;
- `crédit relevé <v> USD à <heure>` ;
- `CREDIT SUFFISANT`.
La mère recopie `<v>` et `<heure>` au champ 3.
Arrêt si : la lecture du crédit échoue ou est illisible ; `CREDIT INSUFFISANT`. Rien n'est créé ; le relevé est inscrit.

**Geste 9. Recherche d'offres** (sortie brute écrite dans un fichier, jamais retapée).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && test ! -e "$D/recherche.json" && ( vastai search offers 'gpu_name=A100_SXM4 num_gpus=1 cpu_cores_effective>=16 cpu_ram>=128 disk_space>=150 cuda_max_good>=13.0' -o 'dph_total' --raw < /dev/null > "$D/recherche.json" 2> "$D/recherche.err" ); echo "recherche : code $?"; sha256sum "$D/recherche.json"
```
Attendu : `recherche : code 0`, puis l'empreinte du fichier (inscrite).
Arrêt si : le code n'est pas 0.

**Geste 10. Choix de l'offre par programme.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && "$PYTHON_BBIS" -I "$D/choisir_offre.py" "$D/recherche.json" "$D/candidates.txt" | tee "$D/g10-choix.txt"; echo "choix : code $?"; while read -r id dv; do bash scripts/lancer_bbis_v6.sh offre-depuis-recherche "$D/recherche.json" "$id" "$D/offre-$id.json" | tee -a "$D/g10-choix.txt" && { printf 'OFFRE_ID=%s\nPILOTE=%s\n' "$id" "$dv" > "$D/offre-retenue.sh"; break; }; done < "$D/candidates.txt"; cat "$D/offre-retenue.sh"
```
Attendu :
- une ligne par offre, `RETENABLE` ou `ecartee : <motifs>` ;
- `CANDIDATES k` (k ≥ 1) et `choix : code 0` ;
- pour la première candidate acceptée par le lanceur : `BBIS OFFRE ECRITE …/offre-<id>.json : offre <id>, A100 SXM4 80GB, <prix ≤ 1,40> USD/h, stockage <≤ 0,08> USD/h, CUDA de l'hôte <≥ 13>` ;
- `OFFRE_ID=<id>` et `PILOTE=595.…` ou `580.…`. Le pilote est recopié tel quel au registre des dépenses.
Arrêt si : `CANDIDATES 0` (code 2) ; aucune candidate n'est acceptée par le lanceur (pas de `offre-retenue.sh`). Rien n'est créé. Une nouvelle recherche n'est permise que sous des noms neufs, une fois.

**Geste 11. Plafond relu et garde de dépense avant la création.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/offre-retenue.sh" && "$PYTHON_BBIS" -I -c 'import json, sys; o = json.load(open(sys.argv[1], encoding="utf-8")); print("PLAFOND_RELU=%.4f" % (1.40 + o["stockage_usd_h"])); print("PRIX_OFFRE=%.4f" % (o["prix_usd_h"] + o["stockage_usd_h"]))' "$D/offre-$OFFRE_ID.json" > "$D/plafond.sh" && cat "$D/plafond.sh" && . "$D/plafond.sh" && bash scripts/lancer_bbis_v6.sh depense 5.989 "$PRIX_OFFRE"; echo "garde de dépense : code $?"
```
Attendu : `PLAFOND_RELU=1.4xxx` (au plus 1,48), `PRIX_OFFRE=…`, puis `BBIS DEPENSE {'cumul': 5.989, 'projete': …, 'coupure': 39.5}` et `garde de dépense : code 0`.
Arrêt si : le code n'est pas 0.

**Geste 12. Échéance, nom du run, commande de création imprimée.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/offre-retenue.sh" && test ! -e "$D/valeurs.sh" && ECH=$(( $(date +%s) + 46800 )) && RUN_BBIS=$(date -u +%Y%m%d-%H%M%S)-bbis-t07-v1 && printf 'OFFRE_ID=%s\nRUN_BBIS=%s\nECH=%s\nT_COMMANDE=%s\n' "$OFFRE_ID" "$RUN_BBIS" "$ECH" "$(date +%s)" > "$D/valeurs.sh" && cat "$D/valeurs.sh" && echo "échéance de la minuterie : $(date -u -d "@$ECH" +%FT%TZ)" && FEU_TEXTE="feu-bbis-v4 $(sha256sum < registres/t07-etape-b-bis/feu-bbis-v4.txt | cut -c1-64) GO-2026-11-14-09 GO-2026-11-16-11" && git fetch -q origin main && bash scripts/lancer_bbis_v6.sh commande "$R" "$D/offre-$OFFRE_ID.json" "$OFFRE_ID" "$C" main 20261111-151701-t06-reel calcul/t06-confirmation-7b-v1 "$RUN_BBIS" "$ECH" "$FEU_TEXTE" 2 python:3.11-bookworm > "$D/commande-imprimee.txt" 2> "$D/commande.err"; echo "commande : code $? ; sortie d'erreur : $(wc -c < "$D/commande.err") octets"; sed -n 1p "$D/commande-imprimee.txt"
```
Attendu :
- les quatre valeurs ;
- une échéance à 13 heures de l'heure présente ;
- `commande : code 0 ; sortie d'erreur : 0 octets` ;
- `BBIS COMMANDE (à jouer par la mère, après le feu écrit ; empreinte de l'amorce 26f954e9e9783bf9) :`.
Le lanceur a alors contrôlé, sans rien créer :
- l'offre et son identifiant ;
- l'image ;
- le prix ≤ 1,40 USD/h ;
- l'amorce en essai local ;
- la garde de création (registre propre, feu portant les deux numéros, deux relances, échéances) ;
- le commit de la fiche ancêtre du commit de la course ;
- le commit de la course joignable sur `main` ;
- la garde d'entrée de la marche rejouée sur l'arbre extrait au commit ;
- la branche de sortie absente.
Arrêt si : le code n'est pas 0 ; ou toute ligne « BBIS REFUS » (motif recopié au compte rendu).

**Geste 13. Vérification de la ligne imprimée** (geste B.3 de l'arbitrage, partie qui demande la commande ; les quatre premières sorties portent sur 64 caractères ou à l'octet).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && X="$D" && . "$X/valeurs.sh" && test "$(grep -c '' "$X/commande-imprimee.txt")" = 2 && grep -c "empreinte de l'amorce 26f954e9e9783bf9) :" "$X/commande-imprimee.txt" && sed -n 2p "$X/commande-imprimee.txt" > "$X/ligne-imprimee.sh" && git show "$C:scripts/amorce_bbis_v6.sh" | base64 -w 0 > "$X/amorce.b64" && base64 -d < "$X/amorce.b64" | sha256sum && wc -c < "$X/amorce.b64" && printf 'GO_ID=GO-2026-11-14-09 vastai create instance %s --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=%s -e ECHEANCE_UTC_S=%s -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo %s | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"\n' "$OFFRE_ID" "$RUN_BBIS" "$ECH" "$(cat "$X/amorce.b64")" > "$X/ligne-reconstruite.sh" && cmp "$X/ligne-reconstruite.sh" "$X/ligne-imprimee.sh" && echo "LIGNE IMPRIMEE EGALE A LA LIGNE RECONSTRUITE" && test "$(grep -o 'echo [A-Za-z0-9+/=]* | base64 -d' "$X/ligne-imprimee.sh" | grep -c '')" = 1 && grep -o 'echo [A-Za-z0-9+/=]* | base64 -d' "$X/ligne-imprimee.sh" | sed 's/^echo //; s/ | base64 -d$//' | base64 -d | sha256sum
```
Sortie attendue :
```
1
26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5  -
41436
LIGNE IMPRIMEE EGALE A LA LIGNE RECONSTRUITE
26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5  -
```
La ligne reconstruite est bâtie indépendamment, depuis les valeurs de ce feu et depuis l'amorce lue au commit. Son égalité à l'octet prouve en une fois :
- l'identifiant de l'offre ;
- l'image `python:3.11-bookworm` ;
- le disque de 150 Go et l'étiquette ;
- le commit et la branche de code `main` ;
- le run et la branche de 7b ;
- le nom du run de la course et l'échéance ;
- le numéro d'accord ;
- **les deux clés passées par leur nom seulement** (`$HF_TOKEN`, `$GH_TOKEN`, jamais une valeur) ;
- l'amorce embarquée, à l'octet.
Le base64 décodé de la ligne imprimée est l'amorce version 6.
Arrêt si : une sortie diffère. Rien n'est créé.

**Geste 14. Création — ligne courte, égalité des arguments, clés par leur nom.**
- **Seul écart de forme permis** : la ligne jouée est la « ligne courte » ci-dessous, et non la ligne imprimée de 41 900 caractères environ. La ligne courte lit l'amorce encodée dans `amorce.b64` (geste 13), et les valeurs dans `valeurs.sh`, écrits par programme. Elle évite ainsi la recopie d'un base64 de 41 436 caractères (réserve R-1 du 16 novembre, « risque de copie »).
- Le même appel prouve, avant de jouer, que les arguments qu'elle passe à l'outil sont **égaux à l'octet** à ceux de la ligne imprimée. L'épreuve se fait avec un outil factice et des jetons factices, dans un environnement vidé.
- Le crochet voit le texte de la création et son numéro d'accord, et les contrôle.
- Préavis d'une ligne à Lazar, porté par la mère au moment du geste (GO-2026-11-16-06) : « création de la machine de la course de l'étape B bis, offre <id>, <prix> USD/h, échéance <heure> ».
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && cd "$D" && . ./valeurs.sh && . ./credit-heure.sh && test $(( $(date +%s) - T_COMMANDE )) -le 1800 && test $(( $(date +%s) - T_CREDIT )) -le 3600 && test "$(command -v vastai)" = "$VASTAI_BBIS" && test ! -e ligne-courte.sh && cat > ligne-courte.sh <<'FIN'
GO_ID=GO-2026-11-14-09 vastai create instance "$OFFRE_ID" --raw --image python:3.11-bookworm --disk 150 --cancel-unavail --label bbis-t07-v1 --env "-e COMMIT=438a9c5257bdc4fa65f25c42cc89753a049b4586 -e BRANCHE_CODE=main -e RUN_7B=20261111-151701-t06-reel -e BRANCHE_7B=calcul/t06-confirmation-7b-v1 -e RUN_BBIS=$RUN_BBIS -e ECHEANCE_UTC_S=$ECH -e GO_ID=GO-2026-11-14-09 -e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" --entrypoint bash --args -c "echo $(cat amorce.b64) | base64 -d > /root/amorce_bbis_v6.sh && bash /root/amorce_bbis_v6.sh"
FIN
env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-imprimee.sh' > argv-imprimee.bin && env -i PATH=/usr/bin:/bin HF_TOKEN=JETON-FACTICE-HF GH_TOKEN=JETON-FACTICE-GH bash -c 'vastai() { printf "GO_ID=%s\0" "$GO_ID"; printf "%s\0" "$@"; }; . ./valeurs.sh; . ./ligne-courte.sh' > argv-courte.bin && cmp argv-courte.bin argv-imprimee.bin && echo "ARGUMENTS EGAUX A LA LIGNE IMPRIMEE" && export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" && test -n "$GH_TOKEN" && test -n "${HF_TOKEN:-}" && test -n "${VAST_API_KEY:-}" && echo "trois clés présentes, par leur nom" && printf 'T_CREATION=%s\n' "$(date +%s)" > t-creation.sh && ( . ./ligne-courte.sh < /dev/null > creation.json 2> creation.err ); echo "création : code $? à $(date -u +%FT%TZ)"
```
Attendu : `ARGUMENTS EGAUX A LA LIGNE IMPRIMEE`, `trois clés présentes, par leur nom`, `création : code <c> à <heure>`. Le code n'est pas jugé ; la réponse est lue au geste 15. La réponse brute n'est jamais affichée.
Arrêt sans création si :
- plus de 30 minutes depuis la commande (refaire les gestes 12 et 13 sous des noms neufs : `valeurs.sh` et la commande imprimée se renomment avec un suffixe `-2`, une fois) ;
- plus d'une heure depuis le relevé du crédit (refaire le geste 8) ;
- l'outil appelé n'est pas celui du geste 4 ;
- les arguments diffèrent ;
- une clé est absente ;
- tout refus de permission, du crochet ou du classifieur.

**Geste 15. Lecture de la création et identifiant de l'instance.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && "$PYTHON_BBIS" -I "$D/lire_creation.py" "$D/creation.json" "$D/instance.sh"; c=$?; rm -f -- "$D/creation.json"; echo "lecture de la création : code $c ; sortie d'erreur de la création : $(wc -c < "$D/creation.err") octets"; cat "$D/instance.sh" 2>/dev/null
```
Attendu : `success True ; new_contract <ID>`, `lecture de la création : code 0`, `ID=<ID>`. La réponse brute est effacée aussitôt : elle peut porter la clé de l'instance.
Si le code n'est pas 0 (cas « créée malgré tout », R-2789), lire la liste :
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && F="$D/liste-g15.json" && ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); "$PYTHON_BBIS" -I "$D/inventaire.py" "$F" | tee "$D/g15-liste.txt"; rm -f -- "$F"; sed -n "s/^INSTANCES .* ETIQUETTE bbis-t07-v1 : \['\([0-9][0-9]*\)'\] ; AUTRES.*$/ID=\1/p" "$D/g15-liste.txt" > "$D/instance-de-la-liste.sh"; cat "$D/instance-de-la-liste.sh"
```
- Une instance de l'étiquette existe : son identifiant est écrit, puis gestes 22 et 23 aussitôt (en lisant `instance-de-la-liste.sh` au lieu de `instance.sh`). La course est consommée ; nœud.
- Aucune : rien n'a été créé, rien n'a été consommé selon le loueur, mais la mère juge (nœud) avant tout nouvel essai.

**Geste 16. Relecture de l'instance : prix, étiquette, pilote.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/instance.sh" && . "$D/plafond.sh" && F="$D/liste-g16.json" && ( vastai show instances --raw < /dev/null > "$F" 2> "$F.err" ); "$PYTHON_BBIS" -I "$D/inventaire.py" "$F" "$ID" "$PLAFOND_RELU" | tee "$D/g16-relecture.txt"; echo "relecture : code $?"; rm -f -- "$F"; sed -n 's/^COURSE [0-9]* | etat [^|]* | prix relu \([0-9][0-9.]*\) | .*$/PRIX_RELU=\1/p' "$D/g16-relecture.txt" | tail -n 1 > "$D/prix-relu.sh"; cat "$D/prix-relu.sh"
```
Attendu : `COURSE <ID> | etat … | prix relu <p> | etiquette bbis-t07-v1 | carte A100 SXM4 | pilote 595.… ou 580.…` (le pilote peut manquer sur la fiche de l'instance : ce n'est pas un refus), `RELECTURE CONFORME`, `relecture : code 0`, `PRIX_RELU=<p>`.
Puis la mère inscrit l'**engagement** au registre des dépenses, sous GO-2026-11-14-09. Il porte :
- l'instance, l'offre, le prix relu, le pilote (`PILOTE` du geste 10) ;
- l'échéance, la création, le crédit relevé ;
- le cumul de la ligne avant la course (5,989 USD) et le pire cas (20,20 USD).
Arrêt si :
- `RELECTURE HORS BORNES` (code 3 : prix relu au-dessus de 1,40 + stockage de l'offre, étiquette autre, pilote hors série) ;
- `COURSE … ABSENTE` (code 4) ;
- prix relu illisible après trois lectures espacées d'une minute.
Dans les trois cas : gestes 22 et 23 aussitôt, puis nœud.

**Geste 17. Attente de l'état « running ».** Toutes les 30 à 60 secondes, au plus 20 minutes après `T_CREATION`, la commande du geste 16 est rejouée sous des noms neufs (`liste-g17-1.json`, `liste-g17-2.json`, …, sortie `g17-etat.txt` en ajout). Elle attend `COURSE <ID> | etat running`. L'attente se fait par l'outil d'attente de la session, sans pause muette.
Arrêt si :
- l'état « running » n'est pas lu dans les 20 minutes (la machine ne démarre pas : aucun journal ne viendra, ni l'empreinte ni la minuterie ne peuvent alerter ; correction D de la contre-lecture) ;
- ou un état terminal est lu (`exited`, `offline` ou autre que `loading`, `created`, `running`).
Dans les deux cas : gestes 22 et 23, la course est consommée, nœud.

**Geste 18. Lecture du journal dans les cinq minutes qui suivent l'état « running ».**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/valeurs.sh" && . "$D/instance.sh" && J="$D/journal-g18-$(date -u +%H%M%S).txt" && ( vastai logs "$ID" < /dev/null > "$J" 2> "$J.err" ); echo "journal : code $?"; ISO=$(date -u -d "@$ECH" +%FT%TZ); a=$(grep -a -c "BBIS minuterie lancée (PID [0-9][0-9]*, échéance $ISO)" "$J"); b=$(grep -a -c -E 'BBIS amorce v6 : empreinte 26f954e9e9783bf95a5149db9e848e1bd207dc8b027e6027d879363be2dfbbb5([^0-9a-f]|$)' "$J"); p=$(grep -a -c -E 'BBIS CUDA servie par le pilote : [0-9]+\.[0-9]+ \(au moins 13\.0\)' "$J"); r=$(grep -a -c -e 'BBIS REFUS' -e 'BBIS ARRET' "$J"); echo "minuterie $a ; empreinte $b ; pilote $p ; refus ou arrêt $r (attendu : 1 ; 1 ; 1 ; 0)"; grep -a -e 'BBIS minuterie lancée' -e 'BBIS amorce v6' -e 'BBIS CUDA servie' -e 'BBIS carte' -e 'BBIS REFUS' -e 'BBIS ARRET' "$J"
```
Attendu : `minuterie 1 ; empreinte 1 ; pilote 1 ; refus ou arrêt 0`, et les trois lignes exigées :
- « minuterie lancée (PID …, échéance <l'échéance du geste 12>) » ;
- « amorce v6 : empreinte » égale aux 64 caractères `26f954e9…dbbb5` ;
- « CUDA servie par le pilote : … (au moins 13.0) ».
Les lignes peuvent tarder de quelques dizaines de secondes. La lecture est refaite sous des noms neufs jusqu'à cinq minutes après l'état « running », pas au-delà.
Arrêt si, à cinq minutes, une ligne manque, apparaît plus d'une fois (conteneur relancé en boucle), ou qu'une ligne `BBIS REFUS` ou `BBIS ARRET` est lue (toute sortie de l'amorce avant la minuterie). Alors : destruction par l'identifiant avec `-y` (geste 22), absence prouvée contre un témoin (geste 23), compte rendu. La course est consommée.

### Phase C — marche

**Geste 19. Suivi horaire** (toutes les heures depuis `T_CREATION`, et avant toute décision).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/instance.sh" && . "$D/t-creation.sh" && . "$D/prix-relu.sh" && CUMUL=$(awk -v t="$T_CREATION" -v n="$(date +%s)" -v p="$PRIX_RELU" 'BEGIN { printf "%.3f", 5.989 + (n - t) / 3600 * p }') && echo "$(date -u +%FT%TZ) cumul de la ligne estimé $CUMUL USD" | tee -a "$D/g19-suivi.txt" && bash scripts/lancer_bbis_v6.sh depense "$CUMUL" "$PRIX_RELU" | tee -a "$D/g19-suivi.txt"; echo "garde de dépense : code $?" | tee -a "$D/g19-suivi.txt"; v=$(bash scripts/lancer_repetition_bbis_v3.sh credit | tee -a "$D/g19-suivi.txt" | sed -n 's/^BBIS REPETITION CREDIT \([0-9][0-9.]*\) USD.*$/\1/p'); awk -v v="$v" 'BEGIN { ok = (v != "" && v + 0 >= 8); print (ok ? "CREDIT AU-DESSUS DE 8 USD" : "CREDIT SOUS 8 USD OU ILLISIBLE"); exit !ok }' | tee -a "$D/g19-suivi.txt"; J="$D/journal-g19-$(date -u +%H%M%S).txt"; ( vastai logs "$ID" < /dev/null > "$J" 2> "$J.err" ); grep -a -e 'BBIS essais du paquet' -e 'BBIS marche' -e 'BBIS poussé' -e 'BBIS traces' -e 'BBIS FIN' -e 'BBIS fin, code' -e 'BBIS ARRET' -e 'BBIS MINUTERIE' "$J" | tail -n 20
```
L'état de l'instance est relu par la commande du geste 16, sous un nom neuf.
Attendu :
- `garde de dépense : code 0` ;
- `CREDIT AU-DESSUS DE 8 USD` ;
- au journal, dans l'ordre : `essais du paquet : code 0, ligne de compte : 151 passed, …` (l'amorce s'arrête elle-même sous 151), `marche : début (run <RUN_BBIS>)`.
Arrêt si :
- la garde de dépense refuse (destruction par la commande qu'elle imprime, gestes 22 et 23) ;
- le crédit est sous 8,00 USD ou illisible (destruction propre, gestes 22 et 23, compte rendu : la course est perdue, nœud) ;
- le prix relu passe au-dessus de `PLAFOND_RELU` (gestes 22 et 23, nœud).
**Heure manquée** : la garde est rejouée dès que possible et l'écart est inscrit à la minute près au compte rendu. Rien ne permet de laisser filer au-delà de l'échéance de la minuterie.

**Geste 20. Issues lues au journal, et suite.**

| ligne lue | ce que l'opérateur fait |
|---|---|
| « BBIS FIN : marche menée au bout » puis « BBIS fin, code 0 » | gestes 21, 22 et 23 dans les quinze minutes |
| « BBIS ARRET : garde de débit » (code 3 ; relecture et journal poussés, instance arrêtée) | instance gardée au plus 12 heures, nœud de Lazar (variante (r1) ou (r2)) ; sans mot dans les 12 heures, gestes 22 et 23 |
| « BBIS ARRET : marche : arrêt écrit » (code 4) | gestes 21 (traces), 22 et 23 dans les quinze minutes |
| « BBIS ARRET : poussée « … » impossible » (poussée en échec après ses trois essais ; correction 5) | **ne pas détruire tout de suite** : l'instance est arrêtée, ses résultats sont sur son disque, et la minuterie est morte avec le conteneur. Aucun maillon de la chaîne ne donne d'accès à l'instance pour relancer la poussée, et la redémarrer rejouerait l'amorce, qui s'arrêterait (« existe déjà », R12). Donc compte rendu d'une ligne aussitôt : course perdue sauf décision de Lazar, nœud ; instance gardée au plus 12 heures (disque ≤ 0,96 USD, déjà compté au pire cas), puis gestes 22 et 23 sans mot. Rien n'est relancé. |
| toute autre « BBIS ARRET » avant la branche prête (étapes 1 à 7) | gestes 22 et 23 dans les quinze minutes |
| « BBIS MINUTERIE : échéance atteinte » | geste 23 ; instance encore listée dix minutes après : geste 22, puis 23 |

### Phase D — destruction et preuve

**Geste 21. Branche de sortie vue sur le distant** (présence seulement, aucun contenu ouvert).
`cd /home/user/controle-ia-travail && git ls-remote origin refs/heads/donnees/t07-etape-b-bis-v2 | grep -c .`
Attendu : `1`. Un `0` après « FIN » : relire le journal (lignes `poussé`) ; s'il n'y a aucune ligne `poussé`, appliquer la ligne « poussée impossible » du geste 20.

**Geste 22. Destruction par l'identifiant, avec `-y`** (R10, jamais par motif).
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/instance.sh" && bash scripts/lancer_bbis_v6.sh detruire "$ID" | tee "$D/g22-destruction.txt" && GO_ID=GO-2026-11-14-09 vastai destroy instance "$ID" -y < /dev/null >> "$D/g22-destruction.txt" 2>&1; echo "destruction demandée à $(date -u +%FT%TZ) (code jamais jugé)"
```
Attendu : `GO_ID=GO-2026-11-14-09 vastai destroy instance <ID> -y`, la ligne « BBIS PUIS … verifier-destruction », puis l'heure. La commande jouée est celle que le lanceur imprime, l'identifiant étant lu dans `instance.sh` au lieu d'être retapé.
Arrêt si : le lanceur refuse l'identifiant (non numérique ou d'une autre session : nœud, rien n'est détruit).

**Geste 23. Absence prouvée contre un témoin.**
```bash
cd /home/user/controle-ia-travail && . /home/user/bbis-course-envoi-feu-v4/env.sh && . "$D/instance.sh" && . "$D/temoin.sh" && bash scripts/lancer_bbis_v6.sh verifier-destruction "$ID" "$TEMOIN" | tee "$D/g23-verification.txt"; echo "vérification : code $?"; L=$(sed -n 's/^BBIS liste des instances gardée : \(\/tmp\/[^ ]*\)\/instances\.json$/\1/p' "$D/g23-verification.txt"); case "$L" in /tmp/?*) rm -rf -- "$L" && echo "liste brute effacée";; esac
```
Attendu : `BBIS DESTRUCTION PROUVEE <ID> : absente de la liste, témoin <TEMOIN> présent, n instance(s) listée(s)`, `vérification : code 0`, `liste brute effacée`.
Si le témoin a disparu : nouveau geste 7 sous des noms neufs (`liste-g23.json`, `temoin-2.sh`), puis vérification avec le nouveau témoin.
Si l'instance est toujours listée : geste 22 une fois de plus, puis 23.
« Absence non prouvée » une seconde fois : arrêt, compte rendu, nœud ; l'instance est signalée comme vivante.

**Geste 24. Inscriptions et compte rendu.**
- Au registre des arrêts : l'instance, l'heure de destruction et l'absence prouvée (témoin).
- Au registre des dépenses : le prix relu, la durée (destruction moins `T_CREATION`), la dépense (durée × prix relu), le nouveau cumul de la ligne, le pilote, le crédit avant et après (geste 19, dernière ligne).
- Compte rendu de l'opérateur à la mère : une ligne par événement ; versions et empreintes des gestes 1, 3, 4 et 5 ; les sorties gardées dans le dossier d'envoi. Aucune mesure, aucun score, aucune aire.
- Après : seuls les fichiers non secrets restent dans le dossier d'envoi. `creation.json` et les listes brutes ont été effacés aux gestes 7, 15, 16 et 23.

---

## § 11 — CE QUI ARRÊTE TOUT, SANS REJEU, SANS REFORMULATION, SANS CONTOURNEMENT

- Refus d'une permission, du crochet (hors le refus attendu du geste 2 (e)) ou du classifieur : arrêt au premier refus, compte rendu en une ligne, rien de relancé.
- Registre des accords illisible par le crochet (geste 2 (c)) : rien n'est créé.
- Refus du lanceur sur l'offre, l'image, le prix, la branche de sortie, l'ancêtre, le commit joignable, le commit de la course, le registre ou la garde de création : arrêt.
- Une empreinte de la chaîne, de l'addendum ou du feu différente sur 64 caractères ; la ligne imprimée différente de la ligne reconstruite ; le base64 décodé différent de `26f954e9…dbbb5` ; les arguments de la ligne courte différents de ceux de la ligne imprimée : arrêt, rien n'est créé.
- Aucune offre de pilote 595 ou 580 sous 1,40 USD/h acceptée par le lanceur : arrêt, rien n'est créé.
- Crédit sous 20,00 USD ou condition de marge non tenue avant la création ; relevé de plus d'une heure : rien n'est créé.
- Prix relu au-dessus de 1,40 + stockage de l'offre : destruction aussitôt, nœud.
- Pas d'état « running » en 20 minutes, ou état terminal : destruction, nœud.
- Journal sans l'une des trois lignes exigées dans les cinq minutes, ou avec une ligne `REFUS` ou `ARRET` : destruction, absence prouvée, compte rendu.
- Garde de dépense déclenchée : destruction par la commande qu'elle imprime.
- Crédit sous 8,00 USD pendant la course : destruction propre, compte rendu.
- Garde de débit déclenchée : instance arrêtée par l'amorce, gardée au plus 12 heures, nœud de Lazar, puis destruction.
- Poussée impossible : voir geste 20 ; rien n'est relancé.
- Échéance de la minuterie atteinte : absence vérifiée, destruction par la session si besoin.
- Portillon des 151 essais non franchi sur la machine : l'amorce s'arrête à son étape 5 ; destruction.
- Contrôle du pilote de la carte en échec : arrêt avant l'installation des paquets ; destruction.
- Arrêts de la liste d'arrêt du texte scellé, lue sous le texte, ses deux addenda et le troisième addendum : contrôle d'identité à dose 0, artefact non vu à dose 1, chemin de l'état imposé, texte décodé ou clé différents, garde d'équivalence de la série d'origine, contrôle carte-processeur au-delà de 10⁻⁴ à 3 époques, déterminisme au bit près non tenu à 300 époques sur la carte, tâche du pli lu dans un apprentissage, moyenne ou médiane sur les jetons, aire ou résumé de score écrit sur l'instance, ouverture d'un fichier de la liste « Jamais ».
- Absence de destruction non prouvée deux fois : arrêt, compte rendu, nœud.
- Création après le 2026-11-21 à 12:00:00Z, ou après le 2026-11-22 à 23:59:59Z : nœud, rien n'est créé.
- Toute instance ou tout serveur de ce programme sans tâche en cours : arrêté par son identifiant, consigné au registre des arrêts.

## § 12 — APRÈS LA COURSE

- Destruction explicite par l'identifiant numérique, avec `-y`, dans les quinze minutes qui suivent la fin ou l'arrêt (hors garde de débit et poussée impossible : 12 heures au plus). Puis absence prouvée contre un témoin, puis inscriptions (geste 24).
- La session de la course ne lit aucune mesure, aucun score, aucune aire. La lecture se fait sur processeur, par un lecteur neuf, sur le plan scellé. Ce lecteur n'a lu ni le verdict de l'étape B ni son fichier de lecture avant de sceller le sien. Le fichier de lecture de l'étape B n'entre qu'après les deux verdicts, pour la seule table conjointe.
- Avant cette lecture (et non avant la course) : la preuve d'antériorité, rejouée depuis un clone à histoire complète et inscrite à part ; le journal des ouvertures du registre propre, créé.
- La mère inscrit `SCORES-BBIS` au registre propre, d'après la ligne « FIN » du journal (chemin seulement).
- Verdict prononcé par un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse. Il cite les trois lignes `ADDENDUM-ECART-1-BBIS`, `-2-BBIS` et `-3-BBIS`, sous peine de n'être pas scellé, et porte les réserves nommées du § 13 (1 à 5). Puis il est soumis à Lazar.

## § 13 — RÉSERVES

**Réserves nommées, à porter au verdict** :

1. **Plafond de prix** : tenu par le lanceur version 6 (hors de la fiche de code) **et** par l'opérateur. Cela va contre la lettre de GO-2026-11-18-03 (3) ; c'est couvert par le champ 2 s'il est rempli. Le verdict dit que ce plafond tenait au lanceur et à l'opérateur, non au code de la fiche.
2. **Prédiction perdue** : la prédiction écrite avant la course, qui s'appuyait sur la reprise de l'entropie, a perdu son appui (GO-2026-11-18-03 (1), TA-3).
3. **Épreuve de niveau rejouée** après la course du 16 novembre : la clause « lue avant toute ouverture de données de 7b » n'est pas tenue à la lettre. L'épreuve n'a lu que des données fabriquées, et le niveau reste 0,99 (troisième addendum).
4. **Image** exigée par son nom, non par un condensé : le contenu servi sous ce nom peut changer.
5. **Amorce embarquée** de 41 436 caractères en base64, taille jamais éprouvée chez le loueur. La lecture du journal (geste 18) la couvre, mais une perte consomme la dernière course.

**Réserves d'exécution** :

6. **Plancher à marge nulle** : 151 passés pour un plancher de 151. Le Python 3.11 de l'image peut ne pas être 3.11.18, et les dépendances non figées de `requirements-gpu.txt` seront résolues de nouveau sur la machine. Rien n'a tourné sur une carte dans les mesures.
7. **Pilote de série 580** : permis par l'arbitrage, jamais éprouvé sur une vraie machine de cette chaîne. Seule la série 595 l'a été.
8. **Ligne courte** (geste 14) : c'est le seul écart de forme à la ligne imprimée, prouvé avant de jouer par l'égalité à l'octet des arguments, et contrôlé par le crochet. Si la mère préfère la ligne imprimée elle-même, elle remplace le geste 14 par ceci :
   - recopier la ligne de `ligne-imprimee.sh` dans un document en ligne (`cat > copie.sh <<'FIN' … FIN`) ;
   - `cmp copie.sh ligne-imprimee.sh` ;
   - jouer `copie.sh` dans le même appel, avec les clés par leur nom.
   Elle accepte alors une recopie de près de 41 900 caractères.
9. **Refus volontaire du crochet au geste 2 (e)** : prévu par ce feu, il ne compte pas comme le « premier refus » de GO-2026-11-16-06. Si la mère ne l'admet pas, la preuve de chargement se réduit au geste 2 (a) et au refus réel que le crochet opposerait à une commande de création sans accord, preuve que ce feu n'exige pas.
10. **Condition de marge sur le crédit** (§ 6, geste 8) : ajoutée par le rédacteur. Elle est plus stricte que GO-2026-11-18-03 (2) et peut retarder la course tant qu'une autre instance tourne (≈ 35,9 USD avec la relance du témoin de Bailey). Sans elle, le plancher de 8 USD en cours de course risque d'arrêter la marche. La mère la garde ou la retire avant de sceller.
11. **Recharge automatique** encore configurée chez le loueur contre l'ordre de GO-2026-11-18-07 (R-3196, R-3197) : une recharge peut survenir pendant la course. L'opérateur ne la compte pas et ne la déclenche pas.
12. **Lecture du prix relu** : le plafond de 1,40 porte sur la carte (arbitrage, correction 3). Le prix relu de l'instance comprenant jusqu'ici le stockage, la borne relue est 1,40 + stockage de l'offre retenue, au plus 1,48. Une lecture à la lettre (« relu au-dessus de 1,40 : destruction ») détruirait une machine saine à 1,38 + 0,03.
13. **Clés de l'outil du loueur** non vérifiées par le rédacteur, faute d'accès au loueur : la présence de `driver_version` dans la recherche (déjà lue le 16 novembre, R-3003), la sous-commande `logs` et le comportement de `-y` dans la version 1.8.3. Le geste 4 vérifie les aides et `-y`. Une clé absente de la recherche écarte l'offre, sans rien deviner.
14. **Fichiers lus sur le disque par la session** : le lanceur, ses gardes et le registre propre sont lus dans l'arbre de travail, non au commit. Le geste 3 prouve qu'ils sont égaux au commit de la course. `main` avance plusieurs fois par heure : le geste 3 se rejoue si plus de deux heures séparent le geste 3 du geste 12.

## § 14 — CORRESPONDANCE AVEC LES PIÈCES

**Les onze corrections de la contre-lecture du projet version 3** :

| correction | où elle est portée |
|---|---|
| 1. écart double (entropie, épreuve épinglée) | § 3 ; couvert par TA-3 à TA-5 du troisième addendum ; § 13, 2 et 3 |
| 2. plafond jouable, sous-commande `offre` de la répétition interdite | § 5 ; gestes 10, 12 et 16 ; plafond aussi dans le lanceur version 6 |
| 3. pire cas avec le stockage et le disque après arrêt de débit | § 6 : 19,24 et 20,20 USD ; cumul pire 26,19 USD |
| 4. crédit surveillé pendant la course, plancher de 8 USD | § 6 ; geste 19 ; § 11 |
| 5. poussée impossible | geste 20 ; § 11 |
| 6. ligne « minuterie lancée » lue | geste 18 |
| 7. image relue | contrôlée par programme (geste 13) et par le lanceur version 6 |
| 8. nœud de la recharge | tranché par GO-2026-11-18-03 (2) ; § 0 |
| 9. portillon sur un environnement installé | mesures définitives, Python 3.13 et 3.11 (§ 3) |
| 10. compagnon du crochet | présent, vérifié au geste 2 (b) |
| 11. étiquette de la répétition désalignée | sans effet : le lanceur de la répétition ne sert qu'à sa sous-commande `credit`, en lecture ; il ne crée rien |
| section C, renvoi au point 1 du plan | § 9 |
| section D, cas non dits | geste 17 (machine qui ne démarre pas), geste 19 (heure manquée), § 5 (minuterie et garde de débit) |

**« Ce qui doit aller au feu version 4 » (arbitrage)** :

| point | où il est porté |
|---|---|
| 1. chaîne version 6, empreintes entières, lanceur depuis la racine avec `PYTHON_BBIS` | § 3 ; geste 3 ; préambule (chemin absolu) |
| 2. commit de la course, branche `main`, mesures scellées, code hors de la fiche | § 3 ; gestes 3 et 12 |
| 3. offre par programme, pilote 595 ou 580, `cuda_max_good` ≥ 13.0, carte ≤ 1,40, stockage ≤ 0,08, image | § 5 ; gestes 9, 10 et 13 |
| 4. échéance par commande à 13 heures, refaite après 30 minutes ; pire cas avec le stockage ; cumul de la ligne | § 5, § 6 ; gestes 12 et 14 |
| 5. clés par leur nom, accord cité | § 0, champ 1 ; gestes 13 et 14 |
| 6. crédit ≥ 20 USD dans l'heure ; outil réinstallé, `-y` éprouvée | § 0, champ 3 ; gestes 4, 8 et 14 |
| 7. journal dans les cinq minutes, trois lignes, sinon destruction et absence prouvée | geste 18 |
| 8. deux relances, dernière course, perte au démarrage consommée | § 7 |
| 9. plancher 151 partout | § 3 ; § 11 ; geste 19 |
| 10. réserves (plafond au lanceur, image par son nom, base64 de 41 436 caractères) | § 13, 1, 4 et 5 |

## § 15 — RÉDACTION ET LIMITES

- **Rédaction** : sous-agent de la session mère, 2026-11-18 de 05:55Z à 06:40Z environ.
  - Processeur seulement. Aucune machine, aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue ni affichée, aucun commit, aucune poussée.
  - Rien d'ouvert sous `diag/`, `runs/` ni `donnees/`, aucune branche de données ni de calcul, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis.
  - Lus : les pièces citées en tête, le lanceur et l'amorce version 6 au commit de la course, `registre_bbis_v2.py`, `lancer_repetition_bbis_v3.sh` et la sous-commande `credit` de `repetition_carte_bbis_v3.py`, le crochet de garde et `.claude/settings.json`, les registres (accords, décisions, dépenses, arrêts, état).
- **Incident déclaré — refus du crochet.** Pour éprouver la reconstruction de la ligne et l'égalité des arguments, le rédacteur a lancé une simulation locale : outil factice, valeurs fabriquées, aucun loueur. Le texte de la commande contenait une ligne de création, et le crochet l'a refusée : « registre GO mal formé ligne 371 : dates illisibles ».
  - Le rédacteur ne l'a ni reformulée ni contournée. Il a confirmé la cause par le lecteur même du crochet, en lecture seule (§ 0, condition 4).
  - Conséquence : **la reconstruction (geste 13) et l'égalité des arguments (gestes 6 et 14) n'ont pas été jouées par le rédacteur.** Le geste 6 en est la première répétition, sur une offre fabriquée, avant toute création.
  - Les trois programmes du geste 5 et les règles de crédit ont été éprouvés hors ligne sur des données fabriquées, cas sain et artefacts. Les dossiers jetables du rédacteur sont effacés.
- **Ce projet devient le feu** quand la mère :
  - remplit les champs 1 à 3 ;
  - lève les conditions 4 à 9 ;
  - remplace la ligne de tête par « en vigueur depuis <heure>, sous GO-2026-11-14-09 » ;
  - le verse sous `registres/t07-etape-b-bis/feu-bbis-v4.txt` avec son compagnon, et l'inscrit.
  Ce fichier-ci reste tel quel (R12).
