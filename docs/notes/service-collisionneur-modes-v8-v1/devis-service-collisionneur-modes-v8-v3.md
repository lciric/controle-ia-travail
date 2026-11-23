# Devis — une consultation du collisionneur sur la question v8 « modes de sabotage » — v3

> **Version 3**, écrite par Claude Opus 5.5 (sous-agent, effort maximal), auteur des v1 et v2, à la place de Fable 5.2. Le quota de l'abonnement de Fable est épuisé jusqu'au 29 novembre 2026, 18:00 UTC (R-5071, `registres/decisions.md` l. 5211) : écart à R-3735 et à GO-2026-11-21-75 déclaré, sur GO-2026-11-22-145 (`registres/go.md` l. 831).
>
> Commande : GO-2026-11-23-03 (`registres/go.md` l. 841), puis les ordres de la mère du 23 novembre. Le dernier suit la vérification des corrections et porte une décision de la mère (étage 2) : retirer aussi le chemin des données du pilote et le commit. Écrit le 23 novembre 2026, 05:40 UTC (`date -u`).
>
> Remplace, sans la modifier, la v2 (`devis-service-collisionneur-modes-v8-v2.md`, 51142200…), elle-même vérifiée par le contre-lecteur de la v1 : `verification-corrections-devis-v8-v1.md` (64045cf7…), « bon après deux corrections légères ». Pièce de classe A, **non scellée** : vérification par le même contre-lecteur, puis remise à Lazar. **Elle n'autorise aucune dépense.** Le plafond reste de **26 USD**.
>
> Fait sans envoi à un modèle, sans dépense, sans commit. Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre » : la porte d'admissibilité v5 n'est pas lue. Aucune cellule d'un dossier de modes, d'attaques, de quarantaine ou de mode tenu à l'écart n'a été ouverte.

## 0. En bref

1. **Le texte à servir est la version servie v2, vérifiée par programme.** Fichier : `version-servie/question-collisionneur-modes-sabotage-v8-servie-v2.md`, sha256 **f3f47c08…**.
   - **23 remplacements** par « [renvoi retiré] » :
     - 21 dérivés de la garde de motifs : 18 chemins internes, qui portent les 19 occurrences refusées, et 3 identifiants d'accord, suites abrégées comprises ;
     - 2 retraits nommés hors de la garde, sur la décision de la mère : le chemin des données du pilote (un chemin interne au sens de GO-2026-11-21-08) et le commit du dépôt d'origine.
   - La garde des 16 moteurs du collisionneur ne refuse plus rien. Les essais du programme passent : 26 sur 26 (un cas sain, 19 artefacts et 6 mutants).
   - Avant le service, le lecteur du coffre contrôle le différentiel, écrit et scelle la porte d'admissibilité v6, qui vise f3f47c08… et ne change rien d'autre, puis en rend l'empreinte. Ce transfert relève de ton GO (décision 1, § 12).
2. **Coût de l'option recommandée** (cinq espèces, maintenant) :
   - **≈ 10,6 USD attendus** ;
   - **≈ 15,5 USD au haut**, avec les pannes du 22 novembre ; les deux dossiers comparables du 22 novembre, ramenés à ce texte, coûteraient 13,35 et 13,61 ;
   - **plafond inchangé : 26 USD**. Au point le plus exigeant, il tolère deux coupures de Carbon de plus que le 22 novembre (décision 2, § 12).
3. **Réserves de la v1, conclusions inchangées** (§ 6) :
   - la longueur tient ;
   - Astra passe à 128 000 jetons par `--sortie-max` ;
   - la garde de Google tient ;
   - préalable de longueur : tenu pour toutes les espèces, sous réglage pour Astra.

## 1. Ce qui change depuis la v2

Les défauts D-1 à D-10 de la contre-lecture sont traités dans la v2 (§ 1) et jugés corrigés par la vérification, sauf D-7, qui était en partie corrigé et que la v3 complète. Le contre-lecteur admet ses erreurs sur D-5 et sur le « ≈ 18 » de D-1 (64045cf7…, § 1).

| point de la vérification | sort | où |
|---|---|---|
| N-1 : option (b) de la décision 1 mal décrite | **traité** par un programme v2. Il prend, en plus de ce que la garde dérive, une liste fermée et scellée de paires supplémentaires nommées, chacune trouvée exactement une fois. C'est désormais le texte recommandé | § 4, 12 |
| N-2 : le chemin `donnees/` face à GO-2026-11-21-08 | **traité**. Retiré, ainsi que le commit, par décision de la mère (étage 2). Le trou de la garde des moteurs est signalé à part | § 4, 12, 13 |
| N-3 : faux sceau sous un nom ordinaire | **traité**. Renommé `d-sceau-faux.json.sceau-faux-essai`. Les essais v2 créent leurs faux sceaux dans un dossier de travail qu'ils effacent | § 4.4, 14 |
| N-4 : contrôles jamais mis en échec ; moteurs non fixés ; liste malformée | **traité**. Empreintes des 16 moteurs fixées dans le programme ; forme des listes contrôlée (arrêt nommé) ; 26 essais, dont 6 mutants qui éprouvent les contrôles redondants et le désaccord entre moteurs | § 4.3, 4.4 |
| N-5 : mention lourde | **traité** : « [renvoi retiré] » | § 4.2 |
| D-7 : compagnons de `calculs/` | **complété**. 23 compagnons `.sha256` écrits ; `verifier-arbre` rend « arbre intact » sur le dossier du service | § 14 |

## 2. Objet et périmètre

- **Une consultation** (GO-2026-11-23-03) : un dossier, un passage, sans héritage, **étage III seul**. Les trois tours de la question (v8 l. 128, 141 et 143) sont ceux de l'étage III : conception (III.1), critique croisée (III.2), réponse (III.3). Les étages I et II ne sont pas joués : les devis modèles les chiffrent parce que la commande `devis` les imprime tous (v1, § 1).
- **Texte servi** : la version servie v2 (§ 4). Le même fichier va en faits et en question, comme l'a proposé le devis « modes et attaques » v3 (l. 143), accordé par GO-2026-11-21-08 (`registres/go.md` l. 607 ; `collisionneur_v9_v8d.py` l. 2794-2796, 877, 883-886).
- **Pas de resserrement en cours de service.** Un refus mène à une absence décidée, jamais à une question réécrite.
- **Moteur recommandé : le moteur du collisionneur, révision 8m, sous la voie de l'abonnement, version 6, avec `--sortie-max`.**
  - C'est l'attelage des trois dossiers du protocole X servis par l'abonnement le 22 novembre.
  - Il a les mêmes tours, consignes, préambule, motifs et catalogue que la révision 8d de `main`, désignée par le mandat de la mère comme la plus récente (`calculs/sortie-comparer-moteurs-et-garde-v1.txt`).
  - Il est vérifié « conforme » (`…/verification-corrections-collisionneur-v9-v8m-opus-v1.md`, 6f8dcf86…, branche `runs/collisionneurs-reprise-v8d-v1`, 470f7e6f…).

## 3. Préalables, avant tout envoi

| | préalable | état |
|---|---|---|
| P1 | Question v5 du 22 novembre (source 19) versée hors du coffre | **fait** (c8cd5f2c…) |
| P2 | Longueur d'un tour ≥ 3 300 mots | **tenu**, sous réglage pour Astra (§ 6) |
| P3 | Garde de motifs | **fait** : version servie v2 f3f47c08…, zéro refus sur les 16 moteurs ; 26 essais sur 26 (§ 4) |
| P4 | Porte d'admissibilité v6 | **à faire par le lecteur du coffre, sur ton GO** (décision 1) : contrôle du différentiel et des deux listes ; porte v6 = v5 sauf l'empreinte visée, f3f47c08… ; empreinte de la v6 rendue avant le service |
| P5 | Opératrice, branche de coffre, commande | § 9 |
| P6 | Clés et crédit | `GEMINI_API_KEY` et `OPENAI_API_KEY_2` (GO-2026-11-22-111, `registres/go.md` l. 797) : présence lue par leur nom, crédit relu avant le lancement |
| P7 | Ce devis | vérifié par le même contre-lecteur, puis GO de Lazar sur les deux décisions (§ 12) |

## 4. La version servie v2

### 4.1 Ce que la garde refuse, et ce qu'elle ne voit pas

- **La garde de motifs** de chaque moteur refuse tout envoi qui porte un nom de personne, un identifiant de session, un courriel, un chemin interne, un identifiant d'accord ou un identifiant de registre (`collisionneur_v9_v8d.py` l. 552-568, 589-599, 1932 ; voie v6 l. 39 et 193).
- **Sur la v8 depuis son titre**, elle trouve 19 occurrences « chemin interne », dans 18 chemins (la ligne 159 en porte deux), et 3 identifiants d'accord (l. 77, 78 et 179). Les 16 moteurs, révisions 8 à 8p, trouvent les mêmes.
- **Elle ne voit pas** :
  - les suites abrégées « et -136 » (l. 78) et « à -139 » (l. 179) ;
  - le chemin `donnees/…` de la source 11 (l. 169) : ses motifs ignorent le préfixe `donnees/` (§ 13) ;
  - le commit du dépôt d'origine (l. 155).

### 4.2 Ce qui est remplacé, et rien d'autre

- **La tête de la v8 est retirée**, comme sa ligne 1 le prescrit (« Le texte à servir commence au titre ; ce bloc n'en fait pas partie »). La ligne 2 est vide.
- **Mention constante, plus légère (N-5)** : « [renvoi retiré] ». La v1 de la version servie portait « [renvoi interne retiré] ».
- **Liste de la garde** : `version-servie/paires-garde-version-servie-v2.json` (72af6fc1…, scellée). Ce sont les 21 anciens de la v1, chemins entiers entre accents graves et identifiants d'accord élargis à leur suite abrégée. Le programme exige qu'elle soit exactement ce qu'il dérive lui-même de la garde.
- **Liste supplémentaire, fermée et nommée (N-1)** : `version-servie/paires-supplementaires-version-servie-v2.json` (fb3cf82a…, scellée). Chaque paire a un nom et une raison :
  1. **commit du dépôt d'origine** (l. 155) : l'empreinte d'un état du dépôt privé, retirée par cohérence avec les chemins ;
  2. **chemin des données du pilote** (source 11, l. 169) : un chemin interne au sens de la condition de GO-2026-11-21-08, « aucun chemin interne, aucun nom ».
- **Lignes touchées** : 77, 78, 155, 159 à 176 et 179 de la v8, soit 22 lignes. La numérotation des faits, des sources, des rubriques et des sections est intacte ; dans la version servie, chaque ligne a deux numéros de moins.
- **Version servie v2** : 33 365 caractères, 5 736 mots au découpage de Python ; sha256 **f3f47c08bfb1885a1a277fc5af33b6ac115fa88fc9aaa16d61b9e93cd54da4f7**.

### 4.3 Contrôles faits par programme

Programme : `version-servie/produire_version_servie_v2.py` (1d705d8d…, classe B, à contre-lire). La v1 (dad030a2…) est gardée. Compte rendu : `version-servie/sortie-produire-version-servie-v2.txt` (ccfd4c4d…). Tout écart arrête au code 2 avant toute écriture ; aucun ne s'est produit.

1. **Entrées.** La v8 a l'empreinte 047eeddf…, UTF-8, fins de ligne LF ; la tête est conforme ; la mention est absente de la v8. Les deux listes sont sous leur sceau et contrôlées dans leur forme : une liste malformée est un arrêt nommé, jamais une trace. Chaque ancien est trouvé exactement une fois, à la ligne dite.
2. **Moteurs à empreinte fixée dans le programme** (N-4). Au moins les révisions 8d et 8m sont exigées ; les 16 ont été données.
3. **Liste de la garde** : exactement ce que la garde refuse, élargi au jeton entier. **Paires supplémentaires** : aucune ne porte un motif de la garde, aucune ne chevauche un jeton de la garde.
4. **Reconstruction** : remettre les anciens à la place des mentions redonne la v8 depuis son titre, au caractère près.
5. **Zone** : tout ancien est dans les lignes 77, 78 ou 155 à 179. Hors de la zone, le texte est identique de part et d'autre (empreinte du reste : 4d5d1563…).
6. **Lignes** : 178 de part et d'autre ; seules diffèrent les 22 lignes porteuses, chacune redonnée par ses seules paires.
7. **Repères** identiques : 8 titres, 27 numéros, 8 rubriques, 42 étiquettes de sources (1 à 21), 26 statuts.
8. **Aucun reste**, avant puis après :
   - `GO-` : 3, puis 0 ;
   - identifiant de registre : 0, puis 0 ;
   - suite abrégée par le motif élargi : 2, puis 0 ;
   - motif `-13[5-9]` : 5, puis 0 ;
   - chemin d'une racine du dépôt entre accents graves : 19, puis 0 ;
   - tout chemin entre accents graves, forme générale : 19, puis 0 ;
   - empreinte de commit de 40 caractères : 1, puis 0 ;
   - nom du dépôt : 1, puis 0.

   Compté seulement : l'identifiant public de l'article, 4 puis 0. Il n'était écrit que dans quatre chemins retirés, et la question dit déjà ces sources publiées.
9. **Garde de chaque moteur** (16) :
   - zéro sur le texte servi ;
   - zéro sur les cinq invites du tour de conception qu'il construit avec lui (69 452 caractères ; 69 933 pour les révisions 8e, 8f et 8p) ;
   - 22 occurrences sur la v8 (témoin, R5).
10. **Différentiel unifié** (`version-servie/diff-v8-vers-version-servie-v2.diff`, 068f17c8…) : 24 lignes retirées (les 2 de tête et les 22 lignes porteuses), 22 ajoutées, rien d'autre.

### 4.4 Essais : un cas sain, des artefacts et des mutants (R5, N-3, N-4)

Programme d'essais : `version-servie/essais_produire_version_servie_v2.py` (6f4f0461…, classe B). Compte rendu : `version-servie/sortie-essais-produire-version-servie-v2.txt` (3857cdc3…). Moteurs : révisions 8d et 8m. Chaque essai tourne dans un dossier de travail neuf, effacé ensuite : aucun faux sceau ne reste dans le dépôt (N-3). **26 sur 26 donnent le résultat attendu** :

- **cas sain** : code 0 et version servie f3f47c08…, identique à celle versée ;
- **19 artefacts**, tous arrêtés au code 2, sans rien écrire :
  - liste de la garde : paire manquante, paire en trop, identifiant non élargi, faux sceau, paire sans ancien, liste qui n'est pas une liste ;
  - liste supplémentaire : ancien absent, ancien présent deux fois, paire sans nom, paire qui porte un motif de la garde, paire hors de la zone, faux sceau, autre mention ;
  - entrées : v8 altérée, sortie déjà présente ;
  - moteurs : moteur inconnu, empreinte fausse, révisions exigées absentes ;
  - reste : une v8 témoin qui porte « -137 » hors des jetons est arrêtée par le contrôle des restes, qui n'avait jamais été mis en échec (N-4) ;
- **6 mutants**, copies du programme où un contrôle antérieur est neutralisé et une faute injectée, chaque substitution exigée une seule fois. Chacun est arrêté par le contrôle qu'il vise : reste identique hors zone, ligne changée hors des paires, ligne porteuse altérée, différentiel, garde résiduelle sur le texte servi, désaccord entre deux moteurs (moteur mutant admis par une copie du programme).

**N-3** : le faux sceau volontaire de la v1 est renommé `calculs-v3/essais-artefacts-produire-version-servie-v1/d-sceau-faux.json.sceau-faux-essai`, contenu inchangé. `sha256sum -c *.sha256` passe désormais dans ce dossier.

### 4.5 Ce qui reste dans le texte servi

Plus aucun chemin, aucun identifiant d'accord ou de registre, aucun commit. Restent :
- les empreintes sha256 des sources, qui servent à la provenance et ne désignent rien au-dehors ;
- la mention « lignes 821 à 825 » d'un registre qui n'est plus nommé.

### 4.6 L'étape du lecteur du coffre, avant le service

1. **Contrôle.** Il contrôle le différentiel unifié et les deux listes, contre la v8 (047eeddf…) qu'il garde. Il peut rejouer le programme v2.
2. **Porte v6.** Il écrit puis scelle la porte d'admissibilité v6 : la v5 (29c8a3c1…), avec pour **seul changement l'empreinte visée**, qui devient **f3f47c08…**. Il dit quel texte reçoivent les trieurs ; le texte servi est recommandé.
3. **Remise.** Il rend l'empreinte de la porte v6. Rien ne part avant.

Ce transfert relève de ton GO (décision 1).

## 5. Composition et réglages recommandés

Inchangés depuis la v2 (§ 5).

| lettre | espèce | voie | prix compté (USD par million, entrée / sortie) | plafond, premier envoi / relance | provision de réflexion | réflexion ou effort | délai | relances du moteur |
|---|---|---|---|---|---|---|---|---|
| A | Opus 5.5 | abonnement : kit, session fille éphémère sans dépôt | 4 / 20 pour la marge du kit ; coût d'interface zéro | 128 000 (marge) | 0 | effort « high » | session | aucune par la voie (§ 7.5) |
| B | Argon | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 30 novembre) | 65 536 / 65 536 | 16 384 | « high » | 10 800 s | relance identique, puis dernier recours « medium » |
| C | Astra (`gpt-6.2-astra`) | interface, arrière-plan | 10 / 50 (barème supposé) | 128 000 / 128 000 | 0 | aucun réglage envoyé | 10 800 s | une relance |
| D | Carbon | interface, flux | 4 / 20 (facturé 2 / 10 jusqu'au 1er décembre, rapporté) | 65 536 / 65 536 | 49 152 | « high » | 10 800 s | relance identique, puis dernier recours « medium » ; pas de repli par lot |
| E | Neon | interface, flux | 3 / 15 | 65 536 / 65 536 | 32 768 | « xhigh » | 10 800 s | relance identique, puis dernier recours « high » |

Sources :
- catalogue et prix : `collisionneur_v9_v8d.py` l. 219-244 et 315-333 ;
- `--sortie-max` et délais : `collisionneur_v9_v8m.py` l. 458-465 et 484 ;
- niveaux de réflexion : `garde_google_v3.py` l. 68-70 ;
- relances : `collisionneur_v9_v8d.py` l. 418, 1814-1821, 1965-1967, 163-165 ;
- effort « high » : GO-2026-11-22-114 (`registres/go.md` l. 800).

**Écart à porter à ta connaissance.** Le dernier recours de Google descend d'un niveau de réflexion. C'est un écart à la règle « Appels aux modèles de Google » (`CLAUDE.md` l. 66-67), accordé par la mère et contre-lu (R-4664, `registres/decisions.md` l. 4803).

**Une seule voix Claude**, Opus maintenant. Le principe est accordé (devis « modes et attaques » v3, l. 54 ; GO-2026-11-21-08) : sans Kimi (l. 58), avec Neon (GO-2026-11-22-112, `registres/go.md` l. 798).
- **Ce qui est perdu sans Fable** : la voix Claude la plus forte, et la comparaison terme à terme avec le passage « modes » du 22 novembre, servi par Fable (`registres/depenses.md` l. 601).
- **La règle « Qui conçoit »** (`CLAUDE.md` l. 78-79) ne vise pas une cellule de collisionneur, qui propose des candidats. Le choix du mode tenu à l'écart vient après, par un lecteur Fable (GO-2026-11-22-127, `registres/go.md` l. 813).
- **L'attente jusqu'au 29 novembre** n'est interdite par aucune échéance écrite : la porte G1 vient après la porte G0, au plus tard fin décembre (`CLAUDE.md` l. 20). Mais à sa remise, le quota de Fable va d'abord aux pièces décisives (R-5071).

## 6. Les quatre réserves de la v1 (conclusions inchangées)

| réserve | conclusion | appui |
|---|---|---|
| 1. Consignes de mots | Les tours de conception et de réponse admettent 3 500 mots, au-dessus des ≈ 3 300 demandés : la consigne n'est pas relevée. Le tour de critique admet 3 000 mots, sans fiche demandée. Le tour « méta » n'est pas joué | `collisionneur_v9_v8d.py` l. 460-469, 495 |
| 2. Astra | 8 000 suffisent : 3 500 × 1,98 = 6 930, marge 13 %. Proposé : `--sortie-max`, 128 000 dès le premier envoi | `collisionneur_v9_v8m.py` l. 461, 465 ; `calculs/sortie-releve-journaux-v1.txt` |
| 3. Arithmétique de la garde | Argon 49 152 pour 17 850 exigés ; Carbon 16 384 pour 14 700 (10 %) ; Neon 32 768 pour 17 850 ; Astra 8 000 pour 6 930 | `garde_google_v3.py` l. 77, 80, 148-150 |
| 4. Préalable de longueur | **tenu** ; **sous réglage** pour Astra | v1, § 5.4 |

## 7. Coût

### 7.1 Méthode

Inchangée depuis la v2 (§ 7.1), appliquée à la **version servie v2** :
- **attendu** : sorties médianes relevées, pièces médianes, plus l'espérance des pannes, s + p × w ;
- **haut** : 90e centile des sorties, pièces maximales ;
- **pire** : la formule du moteur ;
- **prix** de la table.

L'invite du tour de conception fait 69 452 caractères. Programme : `calculs-v3/calcul_devis_v8_v3.py` (80e67745…, inchangé), rejoué dans un dossier neuf, `calculs-devis-v3/` : sortie 00e7ff2e…, totaux ffbd7f2a….

### 7.2 Option recommandée, cellule par cellule (USD)

| cellule | modèle | entrée attendue (jetons) | sortie médiane / 90e centile (jetons) | attendu | haut | pire sans relance | pire avec relances | marge avant l'envoi |
|---|---|---|---|---|---|---|---|---|
| III.1 conception A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,67 |
| III.1 conception B | Argon | 19 177 | 24 203 / 29 342 | 0,56 | 0,66 | 1,75 | 5,25 | 1,75 |
| III.1 conception C | Astra | 17 635 | 2 963 / 3 662 | 0,32 | 0,36 | 6,68 | 13,36 | 6,68 |
| III.1 conception D | Carbon | 19 173 | 33 819 / 37 234 | 0,75 | 0,82 | 2,41 | 7,22 | 2,41 |
| III.1 conception E | Neon | 19 481 | 34 709 / 41 581 | 0,58 | 0,68 | 1,56 | 4,68 | 1,56 |
| III.2 critique A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,95 |
| III.2 critique B | Argon | 48 708 | 31 842 / 40 259 | 0,83 | 1,04 | 1,97 | 5,92 | 1,97 |
| III.2 critique C | Astra | 55 553 | 4 007 / 4 200 | 0,76 | 0,92 | 7,43 | 14,87 | 7,43 |
| III.2 critique D | Carbon | 49 986 | 43 090 / 50 275 | 1,06 | 1,26 | 2,65 | 7,96 | 2,65 |
| III.2 critique E | Neon | 49 861 | 42 520 / 46 942 | 0,79 | 0,90 | 1,76 | 5,27 | 1,76 |
| III.3 réponse A | Opus, abonnement | — | — | 0,00 | 0,00 | 0,00 | 0,00 | 2,98 |
| III.3 réponse B | Argon | 64 527 | 21 848 / 27 438 | 0,70 | 0,87 | 2,06 | 6,19 | 2,06 |
| III.3 réponse C | Astra | 66 061 | 4 191 / 4 305 | 0,87 | 0,98 | 7,42 | 14,83 | 7,42 |
| III.3 réponse D | Carbon | 65 255 | 34 491 / 40 024 | 0,95 | 1,11 | 2,71 | 8,12 | 2,71 |
| III.3 réponse E | Neon | 67 328 | 37 488 / 41 430 | 0,76 | 0,85 | 1,78 | 5,33 | 1,78 |
| **total** | | | | **8,93** | **10,45** | **40,18** | **99,00** | la plus grande : **7,43** |

Espérance des pannes : 1,63 USD. **Attendu avec pannes : 10,57 USD.** Par clé, attendu sans pannes : `GEMINI_API_KEY` 6,98, `OPENAI_API_KEY_2` 1,95 ; les pannes attendues tombent sur la clé de Google.

### 7.3 Totaux des options (USD)

| option | attendu avec pannes | haut, pannes du 22 novembre | pire sans relance | pire avec relances | pointe du chemin haut | plafond proposé | coupures de Carbon de plus tolérées |
|---|---|---|---|---|---|---|---|
| (a) cinq espèces maintenant, Opus par l'abonnement, `--sortie-max` | 10,57 | 15,51 | 40,18 | 99,00 | 19,99 | **26** | 2 |
| (a) sans `--sortie-max` | 10,57 | 15,51 | 22,18 | 66,60 | 16,43 | 22 | 2 |
| (b) après le 29, Fable seul par l'abonnement (cinq espèces) | 10,55 | 15,44 | 40,10 | 98,81 | 19,93 | 26 | 2 |
| (b) après le 29, Fable et Opus par l'abonnement (six espèces) | 10,84 | 15,84 | 40,58 | 100,03 | 20,29 | 26 | 2 |
| (c) révision 8d telle quelle, cinq espèces par l'interface | 12,98 | 18,27 | 26,94 | 76,12 | 19,20 | 25 | 2 |
| (c) révision 8d telle quelle, six espèces par l'interface | 19,74 | 26,03 | 37,27 | 99,26 | 26,96 | 33 | 2 |

Pour comparaison, la commande `devis` des moteurs, avec sa borne de pièces, donne pour l'étage III sur la version servie v2 : 35,19 USD pour les six espèces de la révision 8d, et 47,35 pour les cinq espèces de la 8m sous `--sortie-max` (`calculs-devis-v3/`).

### 7.4 Le haut, avec les pannes du 22 novembre

**Scénario.** Chemin haut, plus les pannes du dossier « conscience et anesthésie » à réserve : deux coupures de Carbon, aux tours III.1 et III.2, comptées au pire ; un refus d'Argon, qui remplace une cellule et n'ajoute rien. Total : 10,45 + 2,41 + 2,65 = **15,51 USD**.

**Rapprochement.** Les deux dossiers comparables, ramenés à ce texte : **13,35 et 13,61 USD**.

**Lecture du plafond, envoi par envoi** (`calculs-devis-v3/sortie-calcul-devis-v8-v3.txt`) :

| envoi | dépense comptée avant | marge exigée | somme |
|---|---|---|---|
| III.1, Carbon, premier essai coupé | 1,02 | 2,41 | 3,43 |
| III.2, Astra | 5,97 | 7,43 | 13,40 |
| III.2, Carbon, premier essai coupé | 6,89 | 2,65 | 9,55 |
| **III.3, Astra : la pointe** | **12,57** | **7,42** | **19,99** |
| III.3, Carbon | 13,55 | 2,71 | 16,26 |
| fin | 15,51 | | |

**Ce qu'en tire le plafond** :
- 25 tolère une coupure de Carbon de plus avant la réponse d'Astra ;
- **26 en tolère deux** ;
- une troisième demanderait 28,12.

**L'arbitrage de `--sortie-max`** : sans lui, la pointe tombe à 16,43, et la même tolérance demande 22 USD. Il coûte donc 4 USD de plafond, rien sur l'attendu.

### 7.5 Règle des relances, et ce que devient une cellule refusée

Inchangée depuis la v2 (§ 7.5) :
- **Google** : relance identique, puis dernier recours déclaré.
- **Astra** : une relance.
- **Opus par l'abonnement** :
  - une réponse recueillie n'est jamais servie deux fois ;
  - une session perdue avant le recueil est une panne technique : le même kit peut être confié une fois à une session neuve, sans coût, issue codée « jamais parti ».
- **Coupure, délai, erreur du serveur, refus de crédit** : une relance sur le même accord, sous le même plafond, inscrite comme « faux échec » ; une seconde panne de la même cellule, l'arbitre décide ; une troisième tentative demande ton mot.
- **Cellule refusée au plafond ou à la ligne** (code 4) : faux échec « jamais parti », nœud porté à Lazar avec la sortie de `devis-reprise` ; ce n'est pas une absence que l'arbitre accepte.
- **Borne absolue** (99,00 USD) : inatteignable, la ligne et le plafond refusent tout envoi dont le pire dépasserait.

### 7.6 Plafond proposé, et mécanique

- **Plafond : 26 USD**, inchangé. Il vaut la pointe du chemin haut avec les pannes du 22 novembre, plus deux coupures de Carbon de plus : 19,99 + 2 × 2,71 = 25,41, arrondi à 26.
- **La borne effective est la ligne** `--ligne-usd 26`, scellée au premier lancement (`collisionneur_v9_v8d.py` l. 1753-1765). `--plafond-usd` n'est pas scellé, et son défaut vaut 40 (l. 402, 2707 ; 8m : l. 565, 3328) : **toute commande redonne `--plafond-usd 26`**.
- **Reprise au-delà** : seulement sur un GO qui porte à la fois `--ligne-reprise-usd MONTANT --go-ligne GO-…` et le nouveau `--plafond-usd`.
- **À 0 USD, hors du plafond** : la version servie, le lecteur du coffre, les sessions d'Opus, les trieurs et la note de fin de dossier.

## 8. Conditions d'arrêt

Inchangées depuis la v2 (§ 8).

**Avant l'envoi** (rien ne part) :
- garde de motifs, code 7 ;
- réglages de Google, code 1 ;
- comptage, code 8 ;
- plafond ou ligne, code 4, faux échec et nœud ;
- espèces ou options autres que celles scellées, code 1.

**Pendant le service** :
- panne technique, code 5 ;
- refus : définitif, absence acceptée par l'arbitre ;
- modèle différent, code 3 ;
- gardes, codes 6, 9 et 10 ;
- moins de trois conceptions valides à la fin du tour III.1 : nœud ;
- cloisonnement rompu : arrêt du versement, incident consigné.

**À la fin** : la commande `verifier` doit rendre « tout tient ».

## 9. Qui lance, la commande, ce qui est versé, et où

1. **Opératrice** : une session cloisonnée, qui ne conçoit ni moniteur ni instrument de la vérité du dommage, inscrite à « qui a lu quoi ». Elle crée elle-même les trois sessions filles d'Opus ; ses créations de sessions et ses poussées au coffre demandent ton mot dans sa session (R-4934, `registres/decisions.md` l. 5073).
2. **Commande**, depuis une extraction de `runs/collisionneurs-reprise-v8d-v1` :

   ```
   python3 docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v6.py v8m --effort high \
       --branche coffre/service-collisionneur-modes-v8-v1 -- \
     etage3 --opus --argon --astra --carbon --neon --sortie-max \
       --cle-anthropic NOM_D_UNE_VARIABLE_PRÉSENTE --cle-openai OPENAI_API_KEY_2 \
       --faits VERSION_SERVIE_V2 --question VERSION_SERVIE_V2 \
       --sortie DOSSIER_HORS_DU_DÉPÔT --plafond-usd 26 --ligne-usd 26
   ```

   - `VERSION_SERVIE_V2` est le fichier f3f47c08….
   - Après chaque arrêt au code 2 (« kits en attente »), l'opératrice relance **la même commande, `--plafond-usd 26` compris**.
3. **Versement** de tout le dossier, à la fin ou à tout arrêt, sur la branche orpheline neuve `coffre/service-collisionneur-modes-v8-v1`, que le gardien vérifie libre, avec sa règle d'ouverture. `--branche` y pointe, jamais vers le défaut de la voie.
4. **Sur `main`**, un inventaire seulement, sans texte ni nom de mode.

## 10. Tri après service : la porte d'admissibilité v6

1. **Remise.** Le gardien remet la porte v6 (§ 4.6), le texte servi et les réponses à trois trieurs neufs, qui n'ont jamais vu le coffre.
2. **Non-recouvrement**, vérifié par le gardien.
3. **La porte décide seule.** À rapprocher par le gardien : la question annonce « deux trieurs indépendants » (v8 l. 124), la commande en nomme trois.
4. **Sortie** : fiches et verdicts scellés au coffre ; sur `main`, un inventaire.
5. **Coût** : 0 USD.

## 11. Note pédagogique de fin de dossier (Markdown et PDF)

Inchangée depuis la v2 (§ 11) : `CLAUDE.md` l. 69-70.
- Écrite après le tri, par un agent neuf qui n'a d'autre accès que le dossier versé et les sorties des trieurs.
- Scellée au coffre, lue par le gardien et Lazar ; une fiche qui vise les lecteurs de la vérité du dommage va au gardien seul.
- PDF par `md_vers_pdf_v1.py` (branche `runs/collisionneurs-reprise-v8d-v1`, 6ba10aa9…).
- Coût : 0 USD.

## 12. Décisions demandées à Lazar

### Décision 1 — le texte servi et la porte d'admissibilité

**Décision.** Servir la version servie v2 (f3f47c08…) et trier par une porte d'admissibilité v6, identique à la v5 sauf l'empreinte visée, que le lecteur du coffre écrit et scelle après avoir contrôlé le différentiel et les deux listes.

**Enjeu.**
- Telle quelle, la v8 est refusée par tous les moteurs : sa garde empêche que des chemins du dépôt, son nom ou des identifiants d'accord partent chez Google et OpenAI.
- La condition de GO-2026-11-21-08 est plus large que la garde : « aucun chemin interne, aucun nom ».
- La porte v5 est scellée sur l'empreinte de la v8 : l'appliquer à un autre texte est un écart à une pièce scellée.

**Options.**
- **(a) La version servie v2** : 23 remplacements, dont deux retraits nommés hors de la garde, décidés par la mère ; vérifiée par programme ; 26 essais.
  - Avantage : plus aucun chemin interne ni commit, la condition de GO-2026-11-21-08 est tenue à la lettre ; mention plus légère ; prête.
  - Inconvénient : un écart à « servie telle quelle » et à une porte scellée, que toi seul accordes.
- **(b) La version servie v1** (b69f6b6d…, 21 remplacements).
  - Avantage : seulement ce que la garde refuse.
  - Inconvénient : elle garde le chemin des données du pilote, un écart à la condition « aucun chemin interne » de GO-2026-11-21-08, et le commit.
- **(c) Un moteur neuf qui exempte de la garde le bloc de la question.**
  - Avantage : la v8 au caractère près.
  - Inconvénient : chemins, nom du dépôt et identifiants partent chez deux fournisseurs ; contraire à GO-2026-11-21-08 ; pièce d'instrument à écrire et à contre-lire.

**Recommandation** : (a), confiance 0,8. **Pas de défaut** : nœud sur une pièce scellée.

### Décision 2 — la dépense

**Décision.** Accorder une seule consultation du collisionneur, à l'étage III, sur la version servie v2, avec un plafond et une ligne de 26 USD.

**Enjeu.**
- **≈ 10,6 USD attendus, ≈ 15,5 au haut** avec les pannes du 22 novembre, pour des modes inédits, candidats au rôle de mode tenu à l'écart ; chaque lecture décisive en consomme un neuf (v8, fait 3).
- Le choix de l'espèce Claude règle la diversité des voix, la comparaison avec le passage du 22 novembre et le délai.

**Options.**
- **(a) Maintenant, cinq espèces** : Opus 5.5 par l'abonnement ; Argon, Astra, Carbon et Neon par l'interface ; le moteur du collisionneur, révision 8m, sous la voie de l'abonnement, avec `--sortie-max`. Plafond 26 (22 sans `--sortie-max`).
  - Avantage : une seule voix Claude ; Claude sans coût d'interface (GO-2026-11-22-70) ; départ dès la porte v6 rendue ; Astra que rien ne coupe.
  - Inconvénient : sans Fable, donc sans la voix Claude la plus forte ni la comparaison avec le passage du 22 novembre ; trois sessions filles à créer, avec ton mot dans la session opératrice ; moteur hors de `main`.
- **(b) Après le 29 novembre, 18:00 UTC, avec Fable par l'abonnement** : Fable **seul**, à la place d'Opus (cinq espèces, ≈ 10,6 attendus, plafond 26), ou Fable **en plus** d'Opus (six espèces, ≈ 10,8, plafond 26).
  - Avantage : la voix Claude la plus forte ; la comparaison terme à terme avec le passage du 22 novembre ; « Fable seul » garde une seule voix Claude.
  - Inconvénient : six jours d'attente ; Fable pris sur un quota que les pièces décisives attendent ; « Fable en plus » met deux voix Claude sur six.
- **(c) Maintenant, la révision 8d de `main` telle quelle**, tout par l'interface, cinq espèces avec Opus par l'interface : ≈ 13,0 attendus, plafond 25.
  - Avantage : moteur de `main`, sans session fille.
  - Inconvénient : 2,4 USD attendus de plus ; Claude payé sur la clé d'Anthropic, contre GO-2026-11-22-70 ; Astra à 8 000 jetons.

**Recommandation** : (a), confiance 0,6. Si tu tiens à Fable : (b), Fable seul. **Pas de défaut** : c'est une dépense.

## 13. Ce qui reste incertain, et ce qui est signalé à part

- **Prix d'Astra et délais** sous `--sortie-max` : supposés (`collisionneur_v9_v8d.py` l. 230-233 ; `collisionneur_v9_v8m.py` l. 484).
- **Coût réel d'une coupure de Carbon** : inconnu, compté au pire.
- **Raisonnement d'Astra** : aucun réglage d'effort n'est envoyé ; raisonnement relevé de 104 jetons au plus. C'est une réserve de qualité, pas une coupure.
- **Longueurs** relevées sur des questions plus courtes ; Carbon reste le plus serré.
- **Refus** : leur risque n'est pas mesuré hors du coffre.
- **Porte v5** : non lue. Le nombre de trieurs, le texte qu'ils reçoivent et l'objet du tri relèvent du gardien.
- **Programmes de la version servie et de ses essais** : classe B, pas encore contre-lus par un autre modèle. Le contrôle du lecteur du coffre porte sur leur résultat.
- **Signalé à part, hors de ce devis (N-2) : un trou dans la garde des moteurs.** Le motif « chemin interne » des révisions 8 à 8p ne connaît pas six racines du dépôt : `brouillons/`, `donnees/`, `gemini/`, `rapports/`, `tests/`, `traces/`, ni `src/` hors de `src/controle_ia/` (`collisionneur_v9_v8d.py` l. 560-565). Un chemin vers ces racines partirait chez un fournisseur sans refus. À corriger dans une révision future du moteur.

## 14. Sources, empreintes et calculs

Empreintes sha256 des fichiers entiers, relevées le 23 novembre 2026 vers 05:40 UTC.

**Pièces du service** (`docs/notes/service-collisionneur-modes-v8-v1/`)

| pièce | empreinte |
|---|---|
| `devis-service-collisionneur-modes-v8-v1.md` ; `…-v2.md` (gardés) | 6363e03d… ; 51142200… |
| `contre-lecture-devis-v8-v1.md` ; `verification-corrections-devis-v8-v1.md` | 230c7b4e… ; 64045cf7… |
| `version-servie/question-collisionneur-modes-sabotage-v8-servie-v2.md` | **f3f47c08bfb1885a1a277fc5af33b6ac115fa88fc9aaa16d61b9e93cd54da4f7** |
| `version-servie/diff-v8-vers-version-servie-v2.diff` | 068f17c8… |
| `version-servie/paires-garde-version-servie-v2.json` | 72af6fc1… |
| `version-servie/paires-supplementaires-version-servie-v2.json` | fb3cf82a… |
| `version-servie/produire_version_servie_v2.py` → `sortie-produire-version-servie-v2.txt` | 1d705d8d… → ccfd4c4d… |
| `version-servie/essais_produire_version_servie_v2.py` → `sortie-essais-produire-version-servie-v2.txt` | 6f4f0461… → 3857cdc3… |
| version servie v1 et ses pièces (gardées) : texte, différentiel, liste, programme, compte rendu | b69f6b6d… ; 7396a54d… ; 79fad93e… ; dad030a2… ; 0aa1eb14… |

Toutes les pièces de `version-servie/` ont leur `.sha256` ; `sha256sum -c` passe sur les treize.

**Calculs.**
- **`calculs/`** (v1) : les 23 fichiers ont désormais leur compagnon `.sha256` (D-7) ; empreintes listées au § 14 de la v2.
- **`calculs-v3/`** (v2) : compagnons présents ; le faux sceau d'essai est renommé (N-3).
- **`calculs-devis-v3/`** (v3, neuf), avec ses compagnons :

| fichier | empreinte |
|---|---|
| `sortie-calcul-devis-v8-v3.txt` | 00e7ff2e… |
| `calcul-devis-v8-v3-totaux.json` | ffbd7f2a… |
| `sortie-devis-v8d-six-especes-version-servie-v2.txt` | 00caaccf… |
| `sortie-devis-v8m-cinq-especes-sortie-max-version-servie-v2.txt` | 90b8153a… |

`python -m controle_ia.scellement verifier-arbre docs/notes/service-collisionneur-modes-v8-v1` rend « arbre intact ».

**Rejeu**, sans réseau, hors du dossier versé (les moteurs 8e à 8p s'extraient de `runs/collisionneurs-reprise-v8d-v1`, 470f7e6f…) :

```
PYTHONPATH=src python3 version-servie/produire_version_servie_v2.py --v8 V8 \
    --paires-garde version-servie/paires-garde-version-servie-v2.json \
    --paires-supplementaires version-servie/paires-supplementaires-version-servie-v2.json \
    --sortie DOSSIER_NEUF --temp DOSSIER_DE_TRAVAIL --moteur v8d CHEMIN --moteur v8m CHEMIN [...]
PYTHONPATH=src python3 version-servie/essais_produire_version_servie_v2.py --programme version-servie/produire_version_servie_v2.py \
    --v8 V8 --paires-garde … --paires-supplementaires … --moteur v8d CHEMIN --moteur v8m CHEMIN \
    --empreinte-attendue f3f47c08bfb1885a1a277fc5af33b6ac115fa88fc9aaa16d61b9e93cd54da4f7 \
    --temp DOSSIER_DE_TRAVAIL --compte-rendu FICHIER_NEUF
PYTHONPATH=src python3 calculs-v3/calcul_devis_v8_v3.py collisionneur_v9_v8m.py \
    version-servie/question-collisionneur-modes-sabotage-v8-servie-v2.md calculs/releve-journaux-v2.json DOSSIER_NEUF
```

**Autres sources**, inchangées (§ 14 de la v2) :
- `collisionneur_v9_v8d.py` (b7803838…) ; `garde_google_v3.py` (923679b5…) ;
- moteur révision 8m (420394f9…) et voie v6 (d99f3358…) ;
- devis modèles et devis « modes et attaques » v3 (fadb7d09…) ;
- registres et `CLAUDE.md` (605db83a…) ; journaux des deux branches de courses.
