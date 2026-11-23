# Devis — une consultation du collisionneur sur la question v8 « modes de sabotage » — v2

> **Version 2**, écrite par Claude Opus 5.5 (sous-agent, effort maximal), auteur de la v1, à la place de Fable 5.2. Le quota de l'abonnement de Fable est épuisé jusqu'au 29 novembre 2026, 18:00 UTC (R-5071, `registres/decisions.md` l. 5211) : écart à R-3735 et à GO-2026-11-21-75 déclaré, sur GO-2026-11-22-145 (`registres/go.md` l. 831).
>
> Commande : GO-2026-11-23-03 (`registres/go.md` l. 841), puis deux ordres de la mère du 23 novembre : produire la version servie par programme ; intégrer les défauts de la contre-lecture. Écrit le 23 novembre 2026, 05:25 UTC (`date -u`).
>
> Remplace, sans la modifier, la v1 (`devis-service-collisionneur-modes-v8-v1.md`, 6363e03d…), contre-lue par un Opus neuf : `contre-lecture-devis-v8-v1.md` (230c7b4e…), verdict « bon après corrections ». Pièce de classe A, **non scellée** : vérification des corrections par le même contre-lecteur, puis remise à Lazar. **Elle n'autorise aucune dépense.**
>
> Fait sans envoi à un modèle, sans dépense, sans commit. Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre » : la porte d'admissibilité v5 n'est pas lue. Aucune cellule d'un dossier de modes, d'attaques, de quarantaine ou de mode tenu à l'écart n'a été ouverte.

## 0. En bref

1. **La version servie existe, vérifiée par programme.** Fichier : `version-servie/question-collisionneur-modes-sabotage-v8-servie-v1.md`, **sha256 b69f6b6d…**.
   - **21 remplacements** par « [renvoi interne retiré] » : 18 chemins internes, qui portent les 19 occurrences refusées par la garde, et 3 identifiants d'accord, avec leurs suites abrégées (« et -136 », « à -139 »).
   - La garde de motifs des 16 moteurs du collisionneur ne refuse plus rien, ni sur le texte, ni sur les invites du tour de conception.
   - Avant le service, le lecteur du coffre contrôle le différentiel, écrit et scelle la porte d'admissibilité v6 (seul changement : l'empreinte visée), puis en rend l'empreinte. Ce transfert de la porte relève de ton GO (décision 1, § 12).
2. **Coût de l'option recommandée** (cinq espèces, maintenant) :
   - **≈ 10,6 USD attendus** ;
   - **≈ 15,5 USD au haut**, avec les pannes du 22 novembre ; les deux dossiers comparables du 22 novembre, ramenés à la v8, coûteraient 13,4 et 13,6 ;
   - **plafond proposé : 26 USD**. Au point le plus exigeant, il tolère deux coupures de Carbon de plus que le 22 novembre (décision 2, § 12).
3. **Réserves de la v1, conclusions inchangées** (§ 6) :
   - la longueur tient ;
   - Astra passe à 128 000 jetons par `--sortie-max` ;
   - la garde de Google tient ;
   - préalable de longueur : tenu pour toutes les espèces, sous réglage pour Astra.

## 1. Ce qui change depuis la v1 : les dix défauts de la contre-lecture

| défaut | sort | où |
|---|---|---|
| D-1 : le haut n'en était pas un | **traité**. Haut refait sur le chemin haut avec les pannes du 22 novembre (15,52) et rapproché des deux dossiers (13,36 et 13,62). Lecture du plafond envoi par envoi ; plafond porté à 26 ; arbitrage de `--sortie-max` dit. Le ≈ 18 de la contre-lecture n'est pas repris : il compte deux fois la relance d'une cellule coupée et ajoute un refus qui ne coûte rien de plus (§ 7.4) | § 0, 7.3, 7.4, 7.6, 12 |
| D-2 : mécanique au plafond | **traité**. Commande écrite avec `--plafond-usd 26` et `--ligne-usd 26` ; la ligne scellée est la borne effective ; une reprise demande un GO qui porte la ligne de reprise et le plafond neuf ; statut d'une cellule refusée au plafond défini (faux échec, « jamais parti », nœud porté à Lazar) | § 7.5, 7.6, 8, 9 |
| D-3 : version servie non vérifiable | **traité**. Programme de classe B, liste fermée et scellée de 21 paires, contrôles par programme : reconstruction, zone, reste identique, aucun reste « -136 » ni « -139 » (motif élargi), différentiel limité aux paires ; garde des 16 moteurs ; six essais d'artefacts, tous refusés. Le transfert de la porte v5 à la v6 est mis dans la décision 1, ainsi que le sort du commit, du chemin des données et de l'identifiant de l'article | § 4, 12 |
| D-4 : une option manque | **traité**. Option (b) : après le 29 novembre, Fable seul ou en plus d'Opus. Ce qui est perdu sans Fable et ce que coûte l'attente sont écrits | § 5, 12 |
| D-5 : relances absentes de l'attendu | **justifié, non retenu**. L'attendu compte une fois la cellule réussie ; une panne ajoute son coût compté au pire ; la relance réussie est la cellule même (exemple de Carbon le 22 novembre) | § 7.1 |
| D-6 : panne d'une session d'Opus | **traité**. Un kit non recueilli peut être confié une fois à une session neuve, sans coût ; issue codée | § 7.5 |
| D-7 : § 13 périmé | **traité**. Calculs de la v1 listés dans `calculs/` avec leurs empreintes, compagnons `.sha256` à ajouter ; rejeu hors du dossier versé ; calculs de la v2 versés avec leurs compagnons dans `calculs-v3/` | § 14 |
| D-8 : « nommé dans la commande » | **traité** : « désigné par le mandat de la mère » | § 2 |
| D-9 : réglages à porter à Lazar | **traité**. Dernier recours de Google à un niveau plus bas : écart accordé par la mère (R-4664). Raisonnement d'Astra non réglé : réserve de qualité | § 5, 13 |
| D-10 : forme | **traité**. Trois options par décision ; noms en clair d'abord, code en appui, dans les sections pour Lazar | § 0, 12 |

## 2. Objet et périmètre

- **Une consultation** (GO-2026-11-23-03) : un dossier, un passage, sans héritage, **étage III seul**. Les trois tours de la question (v8 l. 128, 141 et 143) sont ceux de l'étage III : conception (III.1), critique croisée (III.2), réponse (III.3).
- **Étages I et II non joués.** Les devis modèles chiffrent trois étages parce que la commande `devis` du moteur les imprime tous : 88,60 = 21,09 + 34,87 + 32,64 USD (`devis-v8d-six-especes-question-collisionneur-v3-v1.txt` l. 19, 38, 57) ; 58,77 = 13,45 + 23,87 + 21,45 USD (`devis-commande-collisionneur-v9-v2-dopamine-v1.txt` l. 19, 38, 57). Les trois dossiers comparables servis par l'abonnement le 22 novembre n'ont joué que l'étage III, en quatre heures environ, kits compris (journaux, § 14).
- **Texte servi** : la version servie (§ 4). Le même fichier va en faits et en question, comme l'a proposé le devis « modes et attaques » v3 (l. 143), accordé par GO-2026-11-21-08 (`registres/go.md` l. 607). Le moteur exige un fichier de faits pour un dossier neuf (`collisionneur_v9_v8d.py` l. 2794-2796) et met les deux blocs dans chaque invite (l. 877, 883-886).
- **Pas de resserrement en cours de service.** La règle de GO-2026-11-22-109, point 3 (`registres/go.md` l. 795), visait le collisionneur « modes et attaques ». Un refus mène à une absence décidée, jamais à une question réécrite.
- **Moteur recommandé : le moteur du collisionneur, révision 8m (`collisionneur_v9_v8m.py`), sous la voie de l'abonnement, version 6, avec `--sortie-max`.** C'est l'attelage des trois dossiers du protocole X servis par l'abonnement le 22 novembre.
  - Le v8d de `main`, désigné par le mandat de la mère comme le plus récent, ne sait pas servir une espèce Claude par l'abonnement, que Lazar veut à la place de l'interface payante (GO-2026-11-22-70, `registres/go.md` l. 757). Il ne sait pas non plus relever le premier plafond d'Astra sans code neuf.
  - La révision 8m a les mêmes tours, consignes, préambule, motifs de garde et catalogue des six espèces que la 8d (comparaison par programme, `calculs/sortie-comparer-moteurs-et-garde-v1.txt`).
  - Elle est sur la branche `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…), vérifiée « conforme » après corrections (`…/verification-corrections-collisionneur-v9-v8m-opus-v1.md`, 6f8dcf86…). La voie v6 est contre-lue « conforme » (`…/abonnement-v1/contre-lecture-voie-abonnement-v6-opus-v1.md`, 10adda04…).
  - Les révisions 8n et 8o ne sont pas branchées sur la voie, qui ne connaît que 8m et 8p (`voie_abonnement_v6.py` l. 80-83). La 8p impose des duels balisés aux tours III.1 et III.3, contraires à la forme de la question.

## 3. Préalables, avant tout envoi

| | préalable | état |
|---|---|---|
| P1 | Question v5 du 22 novembre (source 19) versée hors du coffre | **fait** : c8cd5f2c… vérifiée |
| P2 | Longueur d'un tour ≥ 3 300 mots | **tenu**, sous réglage pour Astra (§ 6) |
| P3 | Garde de motifs | **fait** : version servie b69f6b6d…, zéro refus sur les 16 moteurs (§ 4) |
| P4 | Porte d'admissibilité v6 | **à faire par le lecteur du coffre, sur ton GO** (décision 1) : contrôle du différentiel et de la liste, porte v6 = v5 sauf l'empreinte visée, empreinte de la v6 rendue avant le service |
| P5 | Opératrice, branche de coffre, commande | § 9 |
| P6 | Clés et crédit | `GEMINI_API_KEY` (Argon, Carbon, Neon) et `OPENAI_API_KEY_2` (Astra, GO-2026-11-22-111, `registres/go.md` l. 797) : présence lue par leur nom, crédit relu avant le lancement ; aucune dépense d'Anthropic dans l'option recommandée |
| P7 | Ce devis | corrections vérifiées par le même contre-lecteur, puis GO de Lazar sur les deux décisions (§ 12) |

## 4. La version servie

### 4.1 Ce que la garde refusait

- **La garde de motifs** de chaque moteur cherche, dans l'invite entière, nom de personne, identifiant de session, courriel, chemin interne, identifiant d'accord et identifiant de registre (`collisionneur_v9_v8d.py` l. 552-568). Un motif trouvé : refus nommé, code 7, rien n'est envoyé (l. 589-599, 1932 ; voie v6 l. 39 et 193). L'acceptation nommée des révisions 8g et suivantes ne vaut que pour une cellule écrite par un modèle, jamais pour la question (`collisionneur_v9_v8m.py` l. 116-118 et 753).
- **Sur la v8 depuis son titre**, la garde trouve :
  - **19 occurrences « chemin interne » dans 18 chemins**. La ligne 159 en porte deux dans un seul chemin : le préfixe et le nom du dépôt. La v1 disait « 19 chemins internes » : c'étaient 19 occurrences ;
  - **3 identifiants d'accord** (l. 77, 78 et 179) ;
  - les 16 moteurs, révisions 8 à 8p, trouvent les mêmes.
- **La garde ne voit pas les deux suites abrégées** « et -136 » (l. 78) et « à -139 » (l. 179) : elle ne prend que l'identifiant entier (D-3).

### 4.2 Ce qui est remplacé, et rien d'autre

- **La tête de la v8 est retirée**, comme sa ligne 1 le prescrit : « Le texte à servir commence au titre ; ce bloc n'en fait pas partie. » La ligne 2 est vide.
- **21 remplacements** par la mention constante « [renvoi interne retiré] » :
  - chaque chemin interne, c'est-à-dire le jeton entier entre accents graves ;
  - chaque identifiant d'accord, **élargi à sa suite abrégée**.
- **Liste fermée des paires** : `version-servie/paires-version-servie-v1.json` (79fad93e…, scellée). Elle est écrite à la main et comparée par le programme à ce qu'il dérive lui-même de la garde : ni plus, ni moins.
- **Lignes touchées** : 77, 78, 159 à 168, 170 à 176 et 179 de la v8. La numérotation des faits, des sources, des rubriques et des sections est intacte. Dans la version servie, chaque ligne a deux numéros de moins (la tête retirée).
- **Version servie** : 33 593 caractères, 5 755 mots au découpage de Python ; sha256 **b69f6b6d6a4993031be0d2f95d83e5e6c287c74d0a51d7400672bad4b5348a52**.

### 4.3 Contrôles faits par programme

Programme : `version-servie/produire_version_servie_v1.py` (dad030a2…, classe B, à contre-lire par un autre modèle). Compte rendu : `version-servie/sortie-produire-version-servie-v1.txt` (0aa1eb14…). Tout écart arrête au code 2, avant toute écriture ; aucun ne s'est produit.

1. **Entrées** : la v8 a l'empreinte 047eeddf…, UTF-8, fins de ligne LF ; la tête est bien celle qui prescrit de servir depuis le titre ; la liste est sous son sceau ; chaque ancien figure une seule fois, à la ligne dite ; la mention est absente de la v8.
2. **La liste est exactement ce que la garde refuse**, élargi au jeton entier, dans le même ordre.
3. **Reconstruction** : remettre les anciens à la place des mentions redonne la v8 depuis son titre, au caractère près.
4. **Zone** : tout ancien est dans les lignes 77, 78 ou 155 à 179 de la v8 et porte un motif de la garde. Hors de cette zone, le texte est identique de part et d'autre (empreinte du reste : 4d5d1563…).
5. **Lignes** : 178 de part et d'autre ; seules diffèrent les 20 lignes qui portaient un ancien, chacune redonnée par ses seules paires.
6. **Repères** identiques : 8 titres, 27 numéros en début de ligne, 8 rubriques, 42 étiquettes de sources (1 à 21), 26 statuts.
7. **Aucun reste** dans le texte servi :
   - `GO-` ;
   - identifiant de registre ;
   - suite abrégée par le motif élargi « un tiret suivi de chiffres, hors d'un mot » (2 dans la v8, 0 après) ;
   - motif `-13[5-9]` de la contre-lecture (5 dans la v8, 0 après) ;
   - chemin interne entre accents graves (18, puis 0) ;
   - nom du dépôt (1, puis 0).
8. **Garde de chaque moteur** (révisions 8 à 8p, 16 moteurs, empreintes au compte rendu) :
   - zéro occurrence sur le texte servi ;
   - zéro sur les cinq invites du tour de conception que chaque moteur construit avec lui (69 908 caractères ; 70 389 pour les révisions 8e, 8f et 8p) ;
   - sur la v8, chaque moteur trouve toujours les 22 occurrences (témoin, R5).
9. **Différentiel unifié** (`version-servie/diff-v8-vers-version-servie-v1.diff`, 7396a54d…) : 22 lignes retirées (les 2 de tête et les 20 lignes des paires), 20 ajoutées, rien d'autre.

### 4.4 Essais d'artefacts (R5)

Le programme, à la même empreinte, a été lancé sur six artefacts. Tous sont refusés au code 2, sans rien écrire (`calculs-v3/essais-artefacts-produire-version-servie-v1/`) :
- une paire manquante ;
- une paire en trop, le commit ;
- un identifiant non élargi ;
- un sceau faux ;
- une v8 altérée d'un caractère ;
- une sortie qui existe déjà.

Le cas sain est le lancement réel.

### 4.5 Ce qui reste : trois provenances que la garde ne refuse pas

L'ordre de la mère limite le retrait à ce que la garde refuse. Le compte rendu (5e) compte ce qui reste :
- **le commit du dépôt d'origine**, en tête de la table des sources (v8 l. 155 ; la contre-lecture dit l. 154) : gardé ;
- **le chemin des données du pilote**, source 11 (l. 169, `donnees/…`) : gardé ;
- **l'identifiant public de l'article** (2606.08892) : il n'était écrit que dans quatre des chemins retirés (sources 8, 9, 15 et 16), il disparaît donc avec eux. La question dit déjà ces sources publiées. Le garder demanderait une mention qui ne soit plus constante.

La contre-lecture recommande de retirer le commit et de garder l'identifiant de l'article : c'est l'option (b) de la décision 1.

### 4.6 L'étape du lecteur du coffre, avant le service

1. **Contrôle.** Il contrôle le différentiel unifié et la liste des paires, contre la v8 (047eeddf…) qu'il garde.
2. **Porte v6.** Il écrit puis scelle la porte d'admissibilité v6 : la v5 (29c8a3c1…), avec pour **seul changement l'empreinte visée**, qui devient celle de la version servie (b69f6b6d…). Il dit aussi quel texte les trieurs reçoivent ; le texte servi est recommandé, puisque c'est ce que les modèles liront.
3. **Remise.** Il rend l'empreinte de la porte v6. Rien ne part avant.

Ce transfert, d'une porte scellée à une porte neuve, est un écart à une pièce scellée : il relève de ton GO (décision 1).

## 5. Composition et réglages recommandés

| lettre | espèce | voie | prix compté (USD par million, entrée / sortie) | plafond, premier envoi / relance | provision de réflexion | réflexion ou effort | délai | relances du moteur |
|---|---|---|---|---|---|---|---|---|
| A | Opus 5.5 | abonnement : kit, session fille éphémère sans dépôt | 4 / 20 pour la marge du kit ; coût d'interface zéro | 128 000 (marge) | 0 | effort « high » | session | aucune par la voie (§ 7.5) |
| B | Argon | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 30 novembre) | 65 536 / 65 536 | 16 384 | niveau « high », le plus haut admis | 10 800 s | relance identique, puis dernier recours « medium » |
| C | Astra (`gpt-6.2-astra`) | interface, arrière-plan | 10 / 50 (barème supposé) | 128 000 / 128 000 | 0 | aucun réglage envoyé | 10 800 s | une relance |
| D | Carbon | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 1er décembre, rapporté) | 65 536 / 65 536 | 49 152 | « high » | 10 800 s | relance identique, puis dernier recours « medium » ; pas de repli par lot |
| E | Neon | interface, flux | 3 / 15 | 65 536 / 65 536 | 32 768 | « xhigh », le plus haut admis | 10 800 s | relance identique, puis dernier recours « high » |

Sources :
- catalogue et prix : `collisionneur_v9_v8d.py` l. 219-244 et 315-333, identiques en 8m ;
- `--sortie-max` : `collisionneur_v9_v8m.py` l. 458-465 ; délais, l. 484 (supposés) ;
- niveaux de réflexion : `garde_google_v3.py` l. 68-70 ;
- relances : `collisionneur_v9_v8d.py` l. 418, 1814-1821, 1965-1967 ; Carbon hors du lot, l. 163-165 ;
- effort « high » pour une cellule de collisionneur : GO-2026-11-22-114 (`registres/go.md` l. 800).

**Écart à porter à ta connaissance (D-9).** Le dernier recours de Google se fait un niveau plus bas, « medium » ou « high », alors que la règle « Appels aux modèles de Google » demande le niveau le plus haut admis (`CLAUDE.md` l. 66-67). L'écart a été accordé par la mère (R-4664, `registres/decisions.md` l. 4803 : « le niveau ne baisse qu'en dernier recours, déclaré ») et contre-lu ; il n'intervient qu'après deux essais coupés.

**Pourquoi ces cinq**, et ce qui est perdu sans Fable (D-4).
- **Une seule voix Claude** : un mode imaginé par Claude a plus de chances d'être deviné par les concepteurs de moniteurs, qui sont des Claude (devis « modes et attaques » v3, l. 54, accordé par GO-2026-11-21-08). **Sans Kimi**, comme Lazar l'a choisi (devis v3, l. 58). **Neon gardé** (GO-2026-11-22-112, `registres/go.md` l. 798).
- **Opus plutôt que Fable**, maintenant : le quota de Fable est épuisé jusqu'au 29 novembre (R-5071), et à sa remise il est attendu par les pièces décisives qui l'attendent depuis le 22 (même ligne). Fable est réservé aux pièces décisives (`CLAUDE.md` l. 81-82).
- **La règle « Qui conçoit »** (`CLAUDE.md` l. 78-79 : la conception du saboteur revient à Fable) ne vise pas une cellule de collisionneur. Celle-ci propose des candidats ; le choix du mode tenu à l'écart vient après, par un lecteur (GO-2026-11-22-127, `registres/go.md` l. 813 : un Fable neuf propose ses meilleurs choix).
- **Ce qui est perdu sans Fable** :
  - la voix Claude la plus forte de la maison ;
  - la comparaison voix pour voix avec le passage « modes » du 22 novembre, servi par Fable (`registres/depenses.md` l. 601) : deux passages servis par deux voix Claude différentes ne se comparent plus terme à terme.
- **Ce que coûte l'attente** jusqu'au 29 novembre, 18:00 UTC : six jours. Aucune échéance écrite ne l'interdit. La porte G1, qui consomme le premier mode tenu à l'écart neuf, vient après la porte G0, fixée au plus tard fin décembre (`CLAUDE.md` l. 20). Que l'entretien du 1er décembre n'en dépende pas n'est pas vérifié ici.

## 6. Les quatre réserves de la v1 (conclusions inchangées)

| réserve | conclusion | appui |
|---|---|---|
| 1. Consignes de mots | Les tours de conception et de réponse admettent 3 500 mots, au-dessus des ≈ 3 300 demandés (six fiches de 500 mots et une fin, v8 l. 98, 124, 139) : la consigne n'est pas relevée. Le tour de critique admet 3 000 mots pour au plus 24 modes à critiquer, sans fiche demandée. Le tour « méta » (2 500) n'est pas joué. Relever une consigne demanderait un moteur neuf, et la garde refuserait Carbon au-delà de 3 900 mots | `collisionneur_v9_v8d.py` l. 460-469, 495 ; `garde_google_v3.py` l. 148-150 |
| 2. Astra | 8 000 jetons suffisent : 3 500 mots × 1,98 jeton par mot = 6 930, marge de 13 % ; relevé de 64 réponses, toutes valides, la plus longue de 4 797 jetons, raisonnement de 104 jetons au plus. Proposé : `--sortie-max`, 128 000 dès le premier envoi, sans code neuf | `collisionneur_v9_v8d.py` l. 325-326, 1430, 1488-1492 ; `collisionneur_v9_v8m.py` l. 461, 465 ; `calculs/sortie-releve-journaux-v1.txt` |
| 3. Arithmétique de la garde | Argon 49 152 jetons de texte pour 17 850 exigés ; Carbon 16 384 pour 14 700 (marge 10 %) ; Neon 32 768 pour 17 850 ; Astra 8 000 pour 6 930 ; Opus par l'interface 64 000 pour 31 990 ; Fable 49 000 pour 43 820 (11 %) | `garde_google_v3.py` l. 77, 80 ; v1, § 5.3 |
| 4. Préalable de longueur | **tenu** pour Argon, Carbon (marge la plus mince), Neon, Opus et Fable par l'abonnement (réponses relevées de plus de 3 300 mots aux tours III.1 et III.3) ; **tenu sous réglage** pour Astra | v1, § 5.4 |

## 7. Coût

### 7.1 Méthode

- **Invites** construites par les fonctions du moteur révision 8m, sur la **version servie**. Celle du tour de conception fait 69 908 caractères.
- **Pièces** des tours de critique et de réponse :
  - pour l'attendu, la taille médiane relevée par espèce et par tour ;
  - pour la borne et le haut, la taille maximale relevée.
- **Attendu** :
  - entrée au rapport médian mesuré de caractères par jeton ;
  - sortie médiane relevée, réflexion comprise ;
  - prix de la table ;
  - plus l'espérance des pannes : taux relevé × coût compté au pire. Taux relevés : Carbon 7 coupures sur 56 essais, Argon 5 pannes sur 62, Neon 1 sur 26, Astra 0 sur 64 (`calculs/sortie-taux-pannes-v1.txt`).
- **Haut** : sortie au 90e centile, pièces maximales.
- **Pire d'un envoi** : la formule du moteur, garde d'entrée à 2,5 caractères par jeton (`collisionneur_v9_v8d.py` l. 431, 1592-1601).
- **Prix** : comptés à la table, comme le journal. Avant le 1er décembre, Argon et Carbon sont facturés moitié moins (l. 226-228 et 234-235).
- **Pourquoi l'attendu n'ajoute pas le coût des relances (D-5, justifié).** Soit s le coût d'une cellule réussie, p le taux de panne et w le coût compté d'un essai coupé. Avec probabilité 1 − p, la cellule coûte s ; avec probabilité p, elle coûte w, puis s pour la relance réussie. L'espérance vaut donc s + p × w : c'est ce que le calcul compte. La relance réussie est la cellule elle-même, déjà comptée une fois.
  - Exemple, le dossier « conscience et anesthésie » neutre du 22 novembre : Carbon y a coûté 2,34 USD de cellules réussies et 4,76 de coupures, rien d'autre (journal).
  - Une seconde coupure de la même cellule, de probabilité p², ajouterait au plus 0,14 USD à l'attendu de Carbon.
- **Programme** : `calculs-v3/calcul_devis_v8_v3.py` (80e67745…), sortie `calculs-v3/sortie-calcul-devis-v8-v3.txt` (f04e964e…).

### 7.2 Option recommandée, cellule par cellule (USD)

| cellule | modèle | entrée attendue (jetons) | sortie médiane / 90e centile (jetons) | attendu | haut | pire sans relance | pire avec relances | marge avant l'envoi |
|---|---|---|---|---|---|---|---|---|
| III.1 conception A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,67 |
| III.1 conception B | Argon | 19 302 | 24 203 / 29 342 | 0,56 | 0,66 | 1,75 | 5,25 | 1,75 |
| III.1 conception C | Astra | 17 750 | 2 963 / 3 662 | 0,33 | 0,36 | 6,68 | 13,37 | 6,68 |
| III.1 conception D | Carbon | 19 299 | 33 819 / 37 234 | 0,75 | 0,82 | 2,41 | 7,22 | 2,41 |
| III.1 conception E | Neon | 19 609 | 34 709 / 41 581 | 0,58 | 0,68 | 1,56 | 4,68 | 1,56 |
| III.2 critique A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,95 |
| III.2 critique B | Argon | 48 836 | 31 842 / 40 259 | 0,83 | 1,04 | 1,97 | 5,92 | 1,97 |
| III.2 critique C | Astra | 55 680 | 4 007 / 4 200 | 0,76 | 0,92 | 7,44 | 14,87 | 7,44 |
| III.2 critique D | Carbon | 50 114 | 43 090 / 50 275 | 1,06 | 1,26 | 2,66 | 7,97 | 2,66 |
| III.2 critique E | Neon | 49 989 | 42 520 / 46 942 | 0,79 | 0,90 | 1,76 | 5,27 | 1,76 |
| III.3 réponse A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,98 |
| III.3 réponse B | Argon | 64 665 | 21 848 / 27 438 | 0,70 | 0,87 | 2,06 | 6,19 | 2,06 |
| III.3 réponse C | Astra | 66 199 | 4 191 / 4 305 | 0,87 | 0,98 | 7,42 | 14,84 | 7,42 |
| III.3 réponse D | Carbon | 65 392 | 34 491 / 40 024 | 0,95 | 1,11 | 2,71 | 8,12 | 2,71 |
| III.3 réponse E | Neon | 67 468 | 37 488 / 41 430 | 0,76 | 0,85 | 1,78 | 5,33 | 1,78 |
| **total** | | | | **8,94** | **10,46** | **40,19** | **99,03** | la plus grande : **7,44** |

Espérance des pannes : 1,63 USD. **Attendu avec pannes : 10,58 USD.** Par clé, attendu sans pannes : `GEMINI_API_KEY` 6,98, `OPENAI_API_KEY_2` 1,96 ; les pannes attendues tombent sur la clé de Google.

### 7.3 Totaux des options (USD)

| option | attendu avec pannes | haut, pannes du 22 novembre | pire sans relance | pire avec relances | pointe du chemin haut | plafond proposé | coupures de Carbon de plus tolérées |
|---|---|---|---|---|---|---|---|
| (a) cinq espèces maintenant, Opus par l'abonnement, `--sortie-max` | 10,58 | 15,52 | 40,19 | 99,03 | 19,99 | **26** | 2 |
| (a) sans `--sortie-max` | 10,58 | 15,52 | 22,19 | 66,63 | 16,44 | 22 | 2 |
| (b) après le 29, Fable seul par l'abonnement (cinq espèces) | 10,56 | 15,45 | 40,11 | 98,84 | 19,93 | 26 | 2 |
| (b) après le 29, Fable et Opus par l'abonnement (six espèces) | 10,85 | 15,85 | 40,60 | 100,06 | 20,30 | 26 | 2 |
| (c) révision 8d telle quelle, cinq espèces par l'interface | 12,99 | 18,29 | 26,95 | 76,15 | 19,21 | 25 | 2 |
| (c) révision 8d telle quelle, six espèces par l'interface | 19,76 | 26,05 | 37,29 | 99,30 | 26,98 | 33 | 2 |

- La « pointe » est le plus haut, sur le chemin haut avec les pannes du 22 novembre, de « dépense comptée avant un envoi + marge exigée pour cet envoi » (§ 7.4).
- Pour comparaison, la commande `devis` des moteurs, sur la version servie et avec sa borne de pièces, donne pour l'étage III : 35,21 USD pour les six espèces de la révision 8d, et 47,36 pour les cinq espèces de la 8m sous `--sortie-max` (`calculs-v3/`).

### 7.4 Le haut, avec les pannes du 22 novembre (D-1)

**Scénario.** Chemin haut : toutes les cellules au 90e centile de leurs sorties, avec les pièces maximales. On y ajoute les pannes du dossier « conscience et anesthésie » à réserve du 22 novembre :
- une coupure de Carbon au tour III.1 et une au tour III.2, chacune comptée au pire, puis leur relance réussie, qui est la cellule même ;
- un refus d'Argon au tour III.1, qui remplace la cellule réussie et n'ajoute rien.

Total : 10,46 + 2,41 + 2,66 = **15,52 USD**.

**Rapprochement empirique.** Les deux dossiers « conscience et anesthésie » ont coûté 12,50 et 12,59 USD, pannes comprises. Leur question était plus courte : rapportés aux comptes d'entrée de la version servie, cellule par cellule, ils coûteraient **13,36 et 13,62**. Le haut de 15,52 les couvre.

**Le ≈ 18 de la contre-lecture** ajoutait ≈ 2,1 pour les relances et ≈ 1 pour le refus. La relance réussie d'une cellule coupée est déjà dans le chemin haut, et un refus remplace une cellule sans relance : les compter en plus revient à compter deux fois.

**Lecture du plafond, envoi par envoi** (`calculs-v3/sortie-calcul-devis-v8-v3.txt`) :

| envoi | dépense comptée avant | marge exigée | somme |
|---|---|---|---|
| III.1, Carbon, premier essai coupé | 1,02 | 2,41 | 3,43 |
| III.2, Astra | 5,97 | 7,44 | 13,41 |
| III.2, Carbon, premier essai coupé | 6,90 | 2,66 | 9,55 |
| **III.3, Astra : la pointe** | **12,58** | **7,42** | **19,99** |
| III.3, Carbon | 13,56 | 2,71 | 16,27 |
| fin | 15,52 | | |

**Ce qu'en tire le plafond** :
- un plafond de 25 tolère **une** coupure de Carbon de plus avant la réponse d'Astra ;
- 26 en tolère **deux** ;
- une troisième demanderait 28,12.

**L'arbitrage de `--sortie-max`.** Il porte la marge d'Astra de 2,6 à 7,4 USD, pour une sortie relevée de 4 797 jetons au plus. Sans lui, la pointe tombe à 16,44, et la même tolérance demande 22 USD au lieu de 26. Il coûte donc 4 USD de plafond, rien sur l'attendu : c'est le prix d'un Astra qu'aucun plafond ne peut couper.

### 7.5 Règle des relances, et ce que devient une cellule refusée

- **Google** (Argon, Carbon, Neon) : après une sortie vide, coupée, ou arrêtée sans texte, une relance identique déclarée, puis le dernier recours, déclaré (§ 5). Trois essais au plus par cellule (`collisionneur_v9_v8d.py` l. 1965-1967).
- **Astra** : une relance.
- **Opus par l'abonnement** :
  - la voie ne sert jamais deux fois une réponse recueillie (`voie_abonnement_v6.py` l. 29) ; une réponse vide ou coupée laisse la cellule absente, l'arbitre décide ;
  - **une session perdue avant le recueil** est une panne technique (GO-2026-11-22-77). Le même kit, non recueilli, peut être confié une fois à une session neuve, sans coût ; issue codée « jamais parti » (D-6).
- **Coupure de flux, délai, erreur du serveur, refus de crédit** : le moteur s'arrête, compte l'envoi au pire, ne renvoie jamais (l. 15-16, 2083-2085).
  - La cellule a droit à une relance sur le même accord, par une commande neuve sur le même dossier, sous le même plafond. Elle est inscrite comme « faux échec » avec son issue codée (`CLAUDE.md` l. 75-76).
  - Argon et Neon peuvent passer par le lot (`--repli-lot`), Carbon non.
  - Une seconde panne de la même cellule : l'arbitre décide ; une troisième tentative demande ton mot.
- **Cellule refusée au plafond ou à la ligne** (code 4, rien ne part) (D-2) :
  - c'est un « faux échec », issue « jamais parti » ; ce n'est pas une absence que l'arbitre accepte ;
  - elle devient un nœud porté à Lazar, avec la sortie de la commande `devis-reprise` du moteur sur le dossier ;
  - si c'est la relance due après une panne technique que le plafond refuse : même nœud.
- **Borne absolue** (99,03 USD) : chaque cellule épuiserait ses relances au plafond. Elle n'est pas atteignable : la ligne et le plafond refusent tout envoi dont le pire dépasserait (l. 2014-2022 ; voie, l. 189-204).

### 7.6 Plafond proposé, et mécanique (D-1, D-2)

- **Formule v2** : plafond = pointe du chemin haut avec les pannes du 22 novembre + deux coupures de Carbon de plus, arrondi à l'unité supérieure. Option recommandée : 19,99 + 2 × 2,71 = 25,41, soit **26 USD**.
- **La borne effective est la ligne.** `--ligne-usd 26` est scellée au journal au premier lancement (`collisionneur_v9_v8d.py` l. 1753-1765). `--plafond-usd` ne l'est pas : son défaut vaut 40 (l. 402, 2707 ; 8m : l. 565, 3328). **Toute commande de l'opératrice redonne donc `--plafond-usd 26`** (§ 9).
- **Reprise au-delà** : seulement sur un GO de Lazar, qui porte à la fois `--ligne-reprise-usd MONTANT --go-ligne GO-…` et le nouveau `--plafond-usd` (l. 166-169 : le plafond du dossier reste contrôlé à part).
- **Ce qui reste hors du plafond, à 0 USD** : la version servie, le contrôle du lecteur du coffre, les sessions d'Opus, les trieurs et la note de fin de dossier, tous par l'abonnement.

## 8. Conditions d'arrêt

**Avant l'envoi** (rien ne part, 0 USD) :
1. garde de motifs, code 7 ;
2. réglages de Google, code 1 ;
3. comptage d'entrée impossible, code 8 ;
4. plafond ou ligne, code 4 : faux échec « jamais parti », nœud (§ 7.5) ;
5. espèces ou options autres que celles scellées, code 1.

**Pendant le service** :
6. panne technique, code 5 : § 7.5 ;
7. refus d'un modèle : définitif, jamais de reformulation ; l'arbitre accepte l'absence, consignée ;
8. modèle servi différent, code 3 : arrêt ;
9. garde de dépense (code 6), pas de pensées chez Google (code 10), sortie sans texte après le dernier recours (code 9) : arrêt, l'arbitre décide ;
10. moins de trois conceptions valides à la fin du tour III.1 : arrêt, nœud à Lazar ;
11. cloisonnement : toute lecture d'une cellule par la mère ou par un concepteur de moniteur ou d'instrument de la vérité du dommage arrête le versement ; l'incident est consigné.

**À la fin** :
12. la commande `verifier` doit rendre « tout tient » avant le versement et le tri.

## 9. Qui lance, la commande, ce qui est versé, et où

1. **Opératrice** : une session cloisonnée, qui ne conçoit et n'a conçu ni moniteur ni instrument de la vérité du dommage, inscrite à « qui a lu quoi ».
   - Elle crée elle-même les trois sessions filles d'Opus : la mère ne le peut pas sans lire les kits des tours III.2 et III.3, qui portent les modes des autres espèces.
   - Ses créations de sessions et ses poussées au coffre demandent ton mot dans sa session (R-4934, `registres/decisions.md` l. 5073).
2. **Commande** (D-2), depuis une extraction de la branche `runs/collisionneurs-reprise-v8d-v1`, où la voie et le moteur 8m sont côte à côte :

   ```
   python3 docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v6.py v8m --effort high \
       --branche coffre/service-collisionneur-modes-v8-v1 -- \
     etage3 --opus --argon --astra --carbon --neon --sortie-max \
       --cle-anthropic NOM_D_UNE_VARIABLE_PRÉSENTE --cle-openai OPENAI_API_KEY_2 \
       --faits VERSION_SERVIE --question VERSION_SERVIE \
       --sortie DOSSIER_HORS_DU_DÉPÔT --plafond-usd 26 --ligne-usd 26
   ```

   - `VERSION_SERVIE` est le fichier b69f6b6d…. Aucun appel ne part sur la clé d'Anthropic par la voie (l. 65-66).
   - À chaque tour, le moteur écrit le kit d'Opus et s'arrête au code 2 (« kits en attente »). L'opératrice fait servir le kit, le recueille (`recueillir`), puis relance **la même commande, `--plafond-usd 26` compris**.
3. **Versement**, à la fin ou à tout arrêt (« récupérer ce qui est récupérable », `CLAUDE.md` l. 106-107) : archive et empreintes de tout le dossier (cellules, essais refusés, coupés et interrompus, kits et réponses d'Opus, journal, composition, consignes, état) sur une branche orpheline neuve, `coffre/service-collisionneur-modes-v8-v1`, que le gardien vérifie libre, avec sa règle d'ouverture (gardien et Lazar). L'option `--branche` y pointe, jamais vers le défaut de la voie, qui est une branche lisible (`voie_abonnement_v6.py` l. 87, 218).
4. **Sur `main`**, un inventaire seulement : noms, tailles, empreintes, statuts, dépense par clé. Aucun texte ni nom de mode (devis v3, l. 129-135 ; R-5022, `registres/decisions.md` l. 5162).

## 10. Tri après service : la porte d'admissibilité v6

1. **Remise.** Le gardien remet la porte v6 (§ 4.6), le texte servi et les réponses à **trois trieurs neufs**, qui n'ont jamais vu le coffre.
2. **Non-recouvrement**, vérifié par le gardien : aucun trieur n'a lu le coffre, aucun ne conçoit de moniteur ni d'instrument de la vérité du dommage, et tous sont distincts de l'opératrice et des sessions d'Opus.
3. **La porte décide seule.** Ses critères ne sont pas restitués ici. À rapprocher par le gardien : la question annonce « deux trieurs indépendants » (v8 l. 124), la commande en nomme trois.
4. **Sortie** : fiches et verdicts scellés au coffre ; sur `main`, un inventaire seulement.
5. **Coût** : 0 USD, par l'abonnement.

## 11. Note pédagogique de fin de dossier (Markdown et PDF)

- **Règle** : `CLAUDE.md` l. 69-70 (GO-2026-11-22-74). La note dit ce que chaque modèle propose, les accords et les désaccords, ce qui est neuf ou fragile, les références à vérifier, les propositions retenues et pourquoi. Jamais « dossier fini » sans elle.
- **Cloisonnement**, selon le précédent du dossier « modes d'attaque » (R-5022) :
  - écrite après le tri, par un agent neuf qui n'a d'autre accès que le dossier versé et les sorties des trieurs ;
  - scellée sur la branche de coffre du service, lue par le gardien et Lazar ;
  - une fiche qui vise les lecteurs de la vérité du dommage va au gardien seul ;
  - la mère ne reçoit que chemins et empreintes.
- **Forme** : PDF par `docs/notes/collisionneur-v9/notes-de-sortie-v1/md_vers_pdf_v1.py` (branche `runs/collisionneurs-reprise-v8d-v1`, 6ba10aa9…).
- **Coût** : 0 USD.

## 12. Décisions demandées à Lazar

### Décision 1 — le texte servi et la porte d'admissibilité

**Décision.** Servir la version servie (b69f6b6d…), trier par une porte d'admissibilité v6 identique à la v5 sauf l'empreinte visée, que le lecteur du coffre écrit et scelle après avoir contrôlé le différentiel.

**Enjeu.**
- Telle quelle, la v8 est refusée par tous les moteurs : sa garde empêche que des chemins du dépôt, son nom ou des identifiants d'accord partent chez Google et OpenAI.
- La porte v5 est scellée sur l'empreinte de la v8 : l'appliquer à un autre texte est un écart à une pièce scellée.

**Options.**
- **(a) La version servie v1 telle que produite** : 21 remplacements, vérifiés par programme (§ 4).
  - Avantage : seulement ce que la garde refuse, plus les deux suites abrégées ; numérotation intacte ; prête.
  - Inconvénient : le commit du dépôt d'origine et le chemin des données du pilote restent ; l'identifiant public de l'article part avec les chemins.
- **(b) Une version servie v2, même programme, deux paires de plus** : le commit et le chemin des données retirés aussi, comme la contre-lecture le recommande pour le commit.
  - Avantage : plus aucune provenance interne dans le texte.
  - Inconvénient : deux changements que la garde ne demande pas ; une version, un contrôle et une porte de plus, environ une demi-heure.
- **(c) Un moteur neuf qui exempte de la garde le bloc de la question.**
  - Avantage : la v8 au caractère près.
  - Inconvénient : chemins, nom du dépôt et identifiants partent chez deux fournisseurs ; contraire à la condition de GO-2026-11-21-08 ; pièce d'instrument à écrire et à contre-lire.

**Recommandation** : (a), confiance 0,7. Un commit d'un dépôt privé et le nom d'un dossier de données n'identifient rien au-dehors, et chaque changement de plus éloigne le texte servi de la v8 scellée. **Pas de défaut** : nœud sur une pièce scellée.

### Décision 2 — la dépense

**Décision.** Accorder une seule consultation du collisionneur, à l'étage III, sur le texte servi, avec un plafond et une ligne de 26 USD.

**Enjeu.**
- **≈ 10,6 USD attendus, ≈ 15,5 au haut** avec les pannes du 22 novembre, pour des modes inédits, candidats au rôle de mode tenu à l'écart ; chaque lecture décisive en consomme un neuf (v8, fait 3).
- Le choix de l'espèce Claude règle la diversité des voix, la comparaison avec le passage du 22 novembre et le délai.

**Options.**
- **(a) Maintenant, cinq espèces** : Opus 5.5 par l'abonnement ; Argon, Astra, Carbon et Neon par l'interface ; le moteur du collisionneur, révision 8m, sous la voie de l'abonnement, avec `--sortie-max`. Plafond 26 (22 sans `--sortie-max`).
  - Avantage : une seule voix Claude ; Claude sans coût d'interface (GO-2026-11-22-70) ; départ dès la porte v6 rendue ; Astra que rien ne coupe.
  - Inconvénient : sans Fable, donc sans la voix Claude la plus forte ni la comparaison avec le passage du 22 novembre ; trois sessions filles d'Opus à créer, avec ton mot dans la session opératrice ; moteur hors de `main`.
- **(b) Après le 29 novembre, 18:00 UTC, avec Fable par l'abonnement** : Fable **seul**, à la place d'Opus (cinq espèces, ≈ 10,6 attendus, plafond 26), ou Fable **en plus** d'Opus (six espèces, ≈ 10,9, plafond 26).
  - Avantage : la voix Claude la plus forte ; la comparaison terme à terme avec le passage du 22 novembre ; « Fable seul » garde une seule voix Claude.
  - Inconvénient : six jours d'attente ; Fable pris sur un quota que les pièces décisives attendent ; « Fable en plus » met deux voix Claude sur six, contre le principe accordé.
- **(c) Maintenant, le moteur du collisionneur, révision 8d de `main`, tel quel**, tout par l'interface, cinq espèces avec Opus par l'interface : ≈ 13,0 attendus, plafond 25.
  - Avantage : moteur de `main`, sans session fille.
  - Inconvénient : 2,4 USD attendus de plus ; Claude payé sur la clé d'Anthropic, contre GO-2026-11-22-70 ; Astra à 8 000 jetons. La variante à six espèces (≈ 19,8 attendus, plafond 33) n'est pas proposée : deux voix Claude.

**Recommandation** : (a), confiance 0,6. Aucune échéance écrite n'impose de partir avant le 29, mais le quota de Fable, à sa remise, va d'abord aux pièces décisives. Si tu tiens à Fable : (b), Fable seul. **Pas de défaut** : c'est une dépense.

## 13. Ce qui reste incertain

- **Prix d'Astra** : le barème de `gpt-6.2-astra` est supposé (`collisionneur_v9_v8d.py` l. 230-233).
- **Délais** sous `--sortie-max` : supposés (`collisionneur_v9_v8m.py` l. 484).
- **Coût réel d'une coupure de Carbon** : inconnu, compté au pire.
- **Raisonnement d'Astra** (D-9) : aucun réglage d'effort n'est envoyé, et le raisonnement relevé est de 104 jetons au plus. C'est une réserve de qualité pour une cellule de conception, pas une coupure. Le régler demanderait du code neuf.
- **Longueurs** : relevées sur des questions plus courtes que la v8 ; Carbon reste le plus serré (§ 6).
- **Refus** : leur risque sur ce sujet n'est pas mesuré hors du coffre.
- **Porte v5** : non lue. Le nombre de trieurs, le texte qu'ils reçoivent et l'objet du tri relèvent du gardien.
- **Version servie** : le programme qui l'a produite est de classe B et n'est pas encore contre-lu par un autre modèle ; le contrôle du lecteur du coffre porte sur son résultat.

## 14. Sources, empreintes et calculs

Empreintes sha256 des fichiers entiers, relevées le 23 novembre 2026 vers 05:25 UTC. Les registres croissent par la fin : les lignes citées ne bougent pas.

**Pièces du service** (`docs/notes/service-collisionneur-modes-v8-v1/`)

| pièce | empreinte |
|---|---|
| `devis-service-collisionneur-modes-v8-v1.md` (v1, gardée) | 6363e03d… |
| `contre-lecture-devis-v8-v1.md` | 230c7b4e… |
| `version-servie/question-collisionneur-modes-sabotage-v8-servie-v1.md` | b69f6b6d6a4993031be0d2f95d83e5e6c287c74d0a51d7400672bad4b5348a52 |
| `version-servie/diff-v8-vers-version-servie-v1.diff` | 7396a54d… |
| `version-servie/paires-version-servie-v1.json` | 79fad93e… |
| `version-servie/produire_version_servie_v1.py` | dad030a2… |
| `version-servie/sortie-produire-version-servie-v1.txt` | 0aa1eb14… |

Chaque pièce de `version-servie/` a son `.sha256`. Elles ont été committées sur `main` par la mère au commit 13c3b008, sous l'intitulé « brouillon en cours ». Ce sont bien les pièces finales : l'arbre de travail est identique à ce commit.

**Calculs de la v1**, versés par la mère dans `calculs/` (commit 5579f929). D-7 :
- tous sont listés ici ;
- les compagnons `.sha256` manquent : à ajouter au prochain versement (R6) ;
- rejeu **hors** du dossier versé, car `calcul_devis_v8_v2.py` écrit `calcul-devis-v8-v1-totaux.json` à côté du relevé et y crée des dossiers temporaires.

| fichier | empreinte |
|---|---|
| `calcul_devis_v8_v1.py`, remplacé par v2 et gardé | 8cba6dff… |
| `calcul_devis_v8_v2.py` → `sortie-calcul-devis-v8-v2.txt`, `calcul-devis-v8-v1-totaux.json` | 8bfdbca7… → c96f9533…, 8f5d4e7b… |
| `calcul_devis_v8_v2_option_interface.py` → `sortie-calcul-devis-v8-v2-option-interface.txt` | 0ff77783… → e8ee482b… |
| `comparer_moteurs_et_garde_v1.py` → `sortie-comparer-moteurs-et-garde-v1.txt` | 58ecdeb0… → f46b1c9a… |
| `releve_journaux_v1.py` → `sortie-releve-journaux-v1.txt`, `releve-journaux-v1.json` (et son rejeu `-bis`, identique) | 6287bad1… → af161b76…, eec933e5… |
| `releve_journaux_v2.py` → `sortie-releve-journaux-v2.txt`, `releve-journaux-v2.json` (et son rejeu `-bis`, identique) | 22223250… → a43b8514…, 52cd710f… |
| `releve_non_ok_v1.py` → `sortie-releve-non-ok-v1.txt` | 7c01a8af… → 25139741… |
| `taux_pannes_v1.py` → `sortie-taux-pannes-v1.txt` | af4026fa… → b1a888c9… |
| `sortie-devis-v8d-six-especes.txt` ; `sortie-devis-v8m-cinq-especes-sortie-max.txt` | dcfd4ff5… ; 6431b62d… |
| `servi/question-v8-depuis-le-titre.md` (avant la version servie) | 38a1a8e9… |

**Calculs de la v2**, versés ici avec leurs compagnons, non committés, dans `calculs-v3/` :

| fichier | empreinte |
|---|---|
| `calcul_devis_v8_v3.py` | 80e67745… |
| `sortie-calcul-devis-v8-v3.txt` | f04e964e… |
| `calcul-devis-v8-v3-totaux.json` | 651fb3ea… |
| `sortie-devis-v8d-six-especes-version-servie.txt` | cbdca46f… |
| `sortie-devis-v8m-cinq-especes-sortie-max-version-servie.txt` | 3e3bb360… |
| `essais-artefacts-produire-version-servie-v1/` : quatre listes d'artefacts et six sorties d'erreur | empreintes dans les compagnons |

**Rejeu**, sans réseau, après une récupération en lecture des branches de courses ; le programme écrit seulement dans son dossier de sortie, et ses dossiers temporaires y sont effacés :

```
PYTHONPATH=src python3 calcul_devis_v8_v3.py collisionneur_v9_v8m.py \
    version-servie/question-collisionneur-modes-sabotage-v8-servie-v1.md calculs/releve-journaux-v2.json \
    DOSSIER_DE_SORTIE_NEUF
```

**Autres sources**, inchangées depuis la v1 (§ 13 de la v1) :
- `collisionneur_v9_v8d.py` (b7803838…) ;
- `garde_google_v3.py` (923679b5…) ;
- moteurs des révisions 8e à 8p et voie v6 (d99f3358…), sur la branche `runs/collisionneurs-reprise-v8d-v1` (470f7e6f…) ; révision 8m : 420394f9… ;
- devis modèles (def3f890…, a41c3d7b…) et devis « modes et attaques » v3 (fadb7d09…) ;
- registres `go.md` (16830ee4… lors de la v1), `decisions.md`, `depenses.md` ; `CLAUDE.md` (605db83a…) ;
- journaux des branches `runs/collisionneurs-reprise-v8d-v1` et `runs/collisionneurs-reprise-minuit-v1` (761c2c5a…).
