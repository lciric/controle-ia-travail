# Additif du véhicule NA-1 — course « nouvelles attaques » à cinq espèces — projet v1

**Projet, non scellé.** Il part à une contre-lecture, puis à Fable. Ce n'est pas l'additif lui-même : il en prépare la lettre pour les écarts que portent les nœuds N1 à N4, la règle de repli de GO-2026-11-22-35, la part de Luc, le protocole X, la règle d'ancrage, et la place de la définition du mode et de l'épreuve de nouveauté.

- Auteur : Opus, 2026-11-22 ; relevé de `date -u` avant l'écriture : 09:04:43Z. Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue, aucune dépense, aucune écriture dans un dépôt.
- Ce que ce texte ne contient pas : aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucun candidat de mode, aucune case nommée, aucune valeur de clé. Les deux modèles de repli ne sont nommés que par leur rôle, « premier » et « second modèle de repli » ; leurs identifiants sont ceux de GO-2026-11-22-35 et vivent dans la configuration, non dans ce texte (V9 l. 51 ; complément l. 11).
- Hors de ce projet (consigne de la mère) : les lots qui attendent l'orchestrateur (lot 4 v2, lot 5 v2, lot 6 v4, lots 7, 8 et 9). Ce texte dit la règle et l'épreuve que chaque lot devra tenir, non leur code.
- Termes. « Dollars » : dollars des États-Unis (USD dans les textes scellés). « Empreinte » : empreinte SHA-256 (algorithme de hachage sécurisé, 256 bits). « Interface des messages » : l'interface de programmation des messages du fournisseur des clés Claude. « Raison d'arrêt » : le champ `stop_reason` de la réponse ; « catégorie » : le champ `category` de `stop_details`.

Abréviations de chemins : **B** = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/` (branche de travail) ; **M** = `/home/user/main-lecture/` (copie de `main`, HEAD `da565ec1e69f0b2e4399c8d6df86c7a9d3d8bc13`) ; **P** = `M/prereg/ideation-nouvelles-attaques-v1/`.

| sigle | pièce | empreinte (vérifiée contre son compagnon) |
|---|---|---|
| V9 | P/preenregistrement-court-course-nouvelles-attaques-v9.md (scellé) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| A1 | P/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md (scellé) | `9f731795cd8b…` (compagnon OK) |
| CV | P/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md (scellé) | `b4ef87dc6d5c…` (compagnon OK) |
| AC | P/additif-1-complement-valeurs-preenregistrement-court-v9-lot-1-v3-espece-3-sur-minuit-v2.md (scellé) | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` |
| DV | P/devis-course-nouvelles-attaques-v11.md (scellé) | `205e08f23ef9…` (compagnon OK) |
| PS | P/partie-servie-question-v5-v1.md (scellée) | `4cd360baea10…` (compagnon OK) |
| QN | M/docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-modes-attaque-servie-v1.md (1 152 octets) | `02ad3d76ae90648f2fbb8498bc109d4a51a9dddd8b965e03326013e9ee08c9b8` |
| QA | M/docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-modes-attaque-ajout-organisme-v1.md (374 octets) | `8c54752fef44683a7f25e079e22344589e3306130a69eb166333f870a8761669` |
| GO | M/registres/go.md : GO-2026-11-20-67 (l. 598), GO-2026-11-21-30 (l. 629), GO-2026-11-22-35 (l. 722), GO-2026-11-22-37 (l. 724) | `459ce98ec301da9bad69886c606e910ab15ec1dd879c53c69f8ec0737812d999` |
| CO | B/conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md (non scellée, contrôle « Conforme », R-4442) | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` |
| IN | B/inventaire-depart-v1/inventaire-depart-course-nouvelles-attaques-v1.md | compagnon OK |
| NO | B/noeuds-et-part-luc-v2/noeuds-ouverts-vehicule-na-v2.md | `79b9d423f662a3759a0f36037af1d0faae5e6757223d6c40c672d5e973c53032` |
| PL | B/noeuds-et-part-luc-v2/recalcul-part-luc-153-v2.md | `f71451b96dc9552ae8e41c01792ddfc8a7666cef5c0d79ab6c15ff480c59886e` |
| VE | B/noeuds-et-part-luc-v2/verification-v1/verification-noeuds-et-part-luc-v2.md (« Conforme avec réserves ») | `e7eb16826d38f05cb1c96daff6d98d81663a826ec5d9ece3acdd83776dc50cb9` |
| GG | M/src/controle_ia/garde_google_v3.py | `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` |

Les numéros de ligne renvoient à ces fichiers. Toute citation entre guillemets est recopiée du fichier ; « […] » marque une coupe.

## Verdict

Le projet passe en revue cinquante-trois lieux (A-1 à K-3), chacun avec sa citation, sa lettre neuve (ou « inchangée »), sa raison et la décision qui l'accorde ; ceux qui changent une lettre scellée sont marqués « écart déclaré ». Les trois points de la vérification sont résolus par les décisions neuves de la mère. Deux nœuds restent à Lazar avant que l'additif puisse être scellé : la forme du protocole X (Q1) et sa dépense (Q2). Deux mesures doivent être faites avant le scellement, et deux pièces scellées avant lui : la question fusionnée, puis la définition du mode et l'épreuve de nouveauté.

---

## 1. Décisions qui accordent les écarts

| repère | décision | source |
|---|---|---|
| D-N1, D-N2 | adaptateur Claude direct, exigences A1 à A7 ; refus pour crédit d'amont lu tel quel | mère, R-4804 (decisions.md l. 4943) ; NO § 1, § 2 |
| D-N3 | contrôle d'empreinte du code chargé, plus la réserve déclarée | mère, R-4804 ; NO § 3 |
| D-N4 | garde commune de `main`, `garde_google_v3`, telle quelle, une fois sa provenance inscrite | mère, R-4804 ; NO § 4 |
| D-35 | repli sur refus de classifieur, rejoué une fois sur le premier puis sur le second modèle de repli, consigné, compté, rapporté à part ; « écart déclaré aux textes scellés de la course, accordé par Lazar » | GO-2026-11-22-35 (go.md l. 722) |
| D-i, D-ii, D-iii | fiche servie par repli attribuée au modèle servi et rapportée à part ; repli aux lignes à part ; pire par tentative | mère, R-4804 ; NO en-tête |
| D-L | part de Luc relevable à 136,04 dollars au plus | mère, R-4804 lu par R-4807 (decisions.md l. 4946) |
| D-22.1 | quatrième classe sans fiche « refus par classifieur, servi par repli » accordée ; écart déclaré à la V9 l. 160 et à R12, R12 accordée en conséquence | mère, 2026-11-22, transmise par la coordinatrice (à inscrire) |
| D-22.2 | R11 récrite « non dite acceptante » | idem |
| D-22.3 | les fiches servies par repli comptent dans la garde du coffre (arrêt n° 5) | idem |
| D-X | la question des modes et son ajout, servis mot pour mot comme question fusionnée à l'organisme | GO-2026-11-22-37 (go.md l. 724) ; mère, transmise |
| D-1 | définition du mode et épreuve de nouveauté scellées avant le départ ; contenu d'une pièce à part | décision 1, **en attente du mot de Lazar** |
| D-K | règle d'ancrage : aucun candidat de mode, d'où qu'il vienne, servi aux proposeurs ni aux concepteurs de moniteurs | mère, transmise |

Les décisions de la mère transmises le 22 novembre (D-22.1 à D-22.3, D-X pour sa forme, D-K) ne sont pas encore au registre des décisions à la HEAD lue : la mère les inscrit avant le scellement (pièce 2 du § 12).

**Règle générale touchée.** V9 l. 419 : « Après le scellement de ce texte et de son complément, plus rien ne change : version, lanceur, additif, configuration, composition, tirage, plafonds (ordre, § 8). Tout changement est une version neuve et une course neuve. » L'additif du véhicule est prévu par la V9 (l. 402, point 1 ; l. 254) : il fixe des valeurs ouvertes sans écart. **Tout ce qui suit et qui change une lettre scellée est un écart déclaré**, accordé par la décision nommée à sa ligne ; il ne fait pas une course neuve, parce que l'accord le dit (GO-35 : « écart déclaré […] accordé par Lazar »). Pour le protocole X, l'accord d'écart n'est pas écrit à GO-37 : c'est la question Q1.

---

## 2. Adaptateur Claude direct (décisions N1 et N2)

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| A-1 | V9 l. 254 (valeur ouverte) | « (v7) la construction de l'identifiant neutre, les séparateurs et la borne en octets de la ligne de case ; l'enveloppe de la requête assemblée » | **Valeur fixée, sans écart** : pour les clés Claude, la requête assemblée part seule dans un message de rôle « user », sans champ système, par l'interface des messages, au travers du relais de la clé. Rien d'autre n'entre dans le corps que la requête assemblée et les réglages non textuels de A-7, nommés comme transport. | D2 de la conception (CO l. 87, l. 603) n'était pas tenue par l'outil : bloc « # Environment » de 1 052 à 1 080 octets, en-tête de facturation, phrase d'identité (NO § 1). | D-N1 |
| A-2 | V9 l. 73 | « *Rien d'autre de fixe* : ni le compte des cases, ni la famille tenue à l'écart, ni un renvoi interne (règle, décision, accord, chemin), ni le nom d'une personne. » | **Inchangée** ; elle est désormais tenue pour les clés Claude, ce que l'adaptateur de l'outil ne permettait pas (le bloc d'environnement portait un chemin). | constat | D-N1 |
| A-3 | V9 l. 77 | « Avant chaque envoi, et après la garde de motifs (arrêt n° 16), le véhicule écrit au journal de la course la taille et l'empreinte SHA-256 de la requête assemblée […] ; un appel dont la requête n'est pas journalisée ne part pas. » | **Inchangée.** Précision : l'égalité de l'essai à blanc porte sur la chaîne de la consigne extraite du corps reçu par le faux fournisseur, non sur les octets du corps (CO l. 230). | un relais resérialise le corps | D-N1 |
| A-4 | V9 l. 387 (arrêt n° 16) | « après elle, plus aucun octet ne change, et l'empreinte journalisée est celle de ce qu'elle a lu » | **Inchangée** ; tenue sans écart par l'adaptateur direct, qui n'ajoute aucun texte après la garde. | constat | D-N1 |
| A-5 | CO l. 225 (non scellée) | « adaptateur du même type pour le véhicule : il construit ses options comme `construire_options`, **sans texte système**, et garde le reste du transport tel quel (aucun outil, un tour, plafond de l'appel, aucun repli de modèle, bac à sable) » | **Écart à la conception, déclaré** : l'adaptateur est d'un type neuf, qui appelle l'interface des messages en direct, par le relais ; il n'emploie ni l'outil ni le kit pour le transport. Il remplace l'adaptateur `adaptateur_claude_na_v1.py` (`38baa206…`) pour les clés Minuit et Luc. « Aucun repli de modèle » devient : aucun repli du fournisseur ni du kit ; le seul repli est celui du véhicule (§ 5). | l'adaptateur du même type ne peut pas retirer le texte de l'outil | D-N1 ; D-35 |
| A-6 | V9 l. 384, arrêt n° 13 | « arrêt de la course, nommé, qui dit la clé ; aucune bascule ; Lazar prévenu (R-3237, si la dispense est redite). Épreuve : cas sain (réponse normale) ; artefact (refus pour crédit simulé par le faux fournisseur : arrêt nommé) » | **Lettre gardée.** L'adaptateur direct reçoit l'erreur d'amont telle quelle, avec son code et son type d'erreur de facturation, et lève l'arrêt n° 13 qui dit la clé. Aucun message n'est plus fabriqué par un outil. Une erreur d'amont d'un autre type reste « réponse illisible », sous-compte « cause non établie » (CO l. 232). Épreuve : refus pour crédit d'amont simulé par le faux fournisseur v2 : n° 13 levé ; erreur d'accès simulée : n° 13 non levé, « cause non établie ». | l'arrêt était impossible à lever par l'outil (NO § 2) | D-N2 |

**Les sept exigences de l'adaptateur direct**, écrites à l'additif comme règles, chacune avec son épreuve (règle R5) ; leur lettre est celle de NO § 1, table A1 à A7, reprise ici sans changement de sens :

- **A1, aucune relance cachée** : client construit avec `max_retries=0`, écrit et vérifié au départ ; toute relance est une tentative du véhicule, journalisée. Artefact : une erreur 529 simulée ne produit qu'une requête au faux fournisseur.
- **A2, aucun repli du fournisseur** : ni le paramètre de repli côté serveur ni son en-tête bêta ne sont envoyés ; le champ `model` de la réponse est comparé au modèle demandé **de la tentative**. Le « repli que prévoit le fournisseur » de GO-35 est rejoué côté client, visible et consigné. Artefacts : une requête qui porterait ce paramètre est refusée avant l'envoi ; une réponse d'un autre modèle lève l'arrêt n° 31 (§ 9).
- **A3, coût d'un refus compté** : au cumul de la clé, par son usage déclaré ; sans usage, au pire réservé de la tentative, jamais à zéro.
- **A4, réponses brutes conservées par tentative**, refus compris : corps brut, raison d'arrêt, catégorie, modèle servi, usage (V9 l. 396 ; CO l. 227). Conservation impossible : rien n'est rendu.
- **A5, catégorie** lue au champ de détail de la raison d'arrêt ; si elle manque (attendu sur les modèles de repli), la ligne dit « catégorie non lue », jamais un vide.
- **A6, liste fermée** : le repli ne s'ouvre que sur une raison d'arrêt lue égale à « refusal » ; un statut inconnu est une « réponse illisible », jamais rejouée.
- **A7, réglages non textuels par modèle** (effort admis, réflexion, plafond de sortie, flux obligatoire au plafond de 128 000 jetons) : écrits dans la configuration scellée, un jeu par (rôle, modèle), pour le modèle du rôle et pour chacun des deux modèles de repli ; contrôlés au départ. Un réglage non admis par un modèle refuse le départ, avec son nom (arrêt n° 32). Les valeurs admises se lisent sur la page du fournisseur, versée avec son empreinte ; aucune n'est écrite ici de mémoire.

---

## 3. Code chargé (décision N3)

| n° | texte, ligne | lettre | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| C-1 | aucune ligne scellée lue | — | **Règle neuve** : au départ et à chaque génération, le lanceur calcule l'empreinte du fichier source de chaque module chargé (pris dans `sys.modules`) et la compare à la table d'empreintes du paquet ; tout module hors table, ou d'une autre empreinte, refuse le départ ou la génération (arrêt n° 33). Aucun import hors table après le départ. Épreuve : cas sain, toutes les empreintes égales ; artefact, un module planté hors table refuse le départ. | réserve du lot 6 v3 (`a92d3d4a…`, l. 5 à 11) | D-N3 |
| C-2 | décision antérieure de la mère (réserve du lot 6, l. 11 : « séparation par processus […] prévue au lot suivant ») | — | **Écart à une décision antérieure, déclaré** : la séparation par processus n'est pas faite ; le contrôle C-1 la remplace pour cette course. | décision N3 | D-N3 |
| C-3 | — | — | **Réserve déclarée** : ce contrôle ne voit pas une modification en mémoire (le `__code__` échangé, la méthode de la colonne vidée : cas 3 et 4 de la réserve du lot 6). Elle accompagne la course et son rapport. | dit sans forcer | D-N3 |
| C-4 | V9 l. 392, arrêt n° 21 | « une exécution hors du banc de mesure scellé, ou sans ligne d'accord qui la cite » | **Inchangée**, et non citée comme source : que la course n'exécute aucun code rendu par un modèle est un **constat du lanceur** (aucun import hors table, aucun appel d'exécution d'un texte rendu), vérifié par l'épreuve de C-1. | contre-lecture des nœuds, 1.4 | D-N3 |

---

## 4. Appels servis par Google (décision N4)

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| G-1 | règle de `M/CLAUDE.md` l. 66-67 (GO-2026-11-21-71) | — (règle du dépôt, non scellée pour cette course) | Tout appel servi par le deuxième relais (juge de l'espèce 1, proposeurs des espèces 1 et 5 ; AC l. 143) passe, avant l'envoi et au retour, par `garde_google_v3` (GG), **telle quelle**, épinglée à son empreinte dans la table de C-1. Un envoi qu'elle refuse ne part pas : refus écrit, compté, jamais un appel. | les deux audits concluent « non tenue » (NO § 4) | D-N4 |
| G-2 | V9 l. 99, classe « réponse illisible » | « sortie vide sans motif, coupée, ou hors du contrat de sortie \| comptée (M6) ; non relancée » | **Inchangée** ; un défaut relevé par la garde au retour (zéro jeton de pensée, fin en plafond de jetons, en sûreté, en récitation, texte vide) tombe dans cette classe, sous-compte « défaut de la règle Google », jamais rejoué. | règle G-1 | D-N4 |
| G-3 | V9 l. 383, arrêt n° 12 ; CV l. 166 | « Le pire d'un appel de proposeur est de 6,05 USD ; celui du juge de l'espèce 1, sur le deuxième relais, est le pire d'un appel de juge, écrit au complément (ligne 4 de la table). » | Le pire d'un appel servi par Google est **mesuré sous les réglages de la garde** avant le scellement de l'additif et s'y écrit : proposeur, [PIRE-G-PROPOSEUR] dollars ; juge de l'espèce 1, [PIRE-G-JUGE] dollars. S'il dépasse 6,05 pour un proposeur, l'additif ne se scelle pas : une version neuve du complément s'écrit (CV, valeur ouverte du pire). | 6,05 n'est pas établi sous la garde (plafond de sortie relevé à réflexion plus 16 000 jetons) | D-N4 |
| G-4 | AC l. 143 | « part : 140,39 USD ; rôles : juge de l'espèce 1, proposeurs des espèces 1 et 5 » | **Inchangée** ; c'est un cas haut chiffré sans les réglages de la garde : réserve déclarée. Si la mesure de G-3 montre que le cas haut sous la garde dépasse 140,39, nœud de la mère, sans repli silencieux. | — | D-N4 |
| G-5 | — | — | **Provenance à inscrire** au registre des décisions avant l'épinglage (aucune ligne ne cite la v3) : `src/controle_ia/garde_google_v3.py`, empreinte `923679b5…f4afe91`, compagnon vérifié ; versée sur `main` au commit `25986189e` (« … collisionneur v8c et garde Google v3 … ») ; selon sa docstring, écrite le 21 novembre 2026 par Claude Opus 5.5, développeur du collisionneur v9 révision 8, copie de `garde_google_v2.py` (`9d39a749…`), seul changement : rapport de jetons par mot par espèce. | contre-lecture des nœuds, 1.3 | D-N4 ; inscription par la mère |

---

## 5. Règle de repli (GO-2026-11-22-35)

Le mot (go.md l. 722) : un appel Claude refusé par un classifieur de sûreté (raison d'arrêt « refusal ») est rejoué une fois sur le premier modèle de repli, puis, s'il est encore refusé, sur le second ; chaque repli consigné par appel (modèle demandé, modèle servi, catégorie), compté dans le devis, rapporté à part ; « arrêts n° 11, 12 et 27 inchangés ».

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| R1 | V9 l. 372, arrêt n° 1 | « le tour s'arrête ; consigné tel quel ; non relancé ; une reformulation plus étroite seulement sur le mot de Lazar (R-609) » | Une raison d'arrêt « refusal » lue d'une clé Claude ouvre une **chaîne** : la **requête assemblée identique** (même empreinte au sens de la V9 l. 77 ; seul le champ du modèle du corps change) est rejouée une fois sur le premier modèle de repli, puis une fois sur le second. L'arrêt n° 1 se lève après le troisième refus, avec sa portée (« appel » par défaut). Toute reformulation reste interdite sans le mot de Lazar. Ailleurs (commande externe, refus de contenu d'un autre fournisseur), le n° 1 garde sa lettre, sans repli. | GO-35 | D-35 |
| R2 | V9 l. 98, « refus du modèle » | « comptée (M6) ; non relancée, sans reformulation ; distincte de l'arrêt n° 1 » | **Inchangée** : un refus en prose n'est jamais rejoué. | la raison d'arrêt n'est pas « refusal » | D-35 |
| R3 | V9 l. 99, « réponse illisible » | « comptée (M6) ; non relancée » | **Inchangée** : crédit, accès, réponse coupée, raison inconnue (A6) ne sont jamais rejoués. | liste fermée | D-35 |
| R4 | V9 l. 383, arrêt n° 12 | « Le pire par appel est de 6,05 USD pour un proposeur (devis, § 3) ; celui de l'aiguilleur et du juge est écrit au complément de valeurs. » ; « **aucune bascule** vers une autre clé » | Chaque **tentative** repasse le n° 12 avec le pire de sa tentative, sur la même clé. Proposeur : 6,05 dollars à chaque tentative, non baissé au tarif des modèles de repli. Aiguilleur et juge : un pire par (rôle, modèle), mesuré avant le scellement et écrit ici : [PIRE-AIGUILLEUR-RÔLE], [PIRE-AIGUILLEUR-REPLI-1], [PIRE-AIGUILLEUR-REPLI-2], [PIRE-JUGE3-RÔLE], [PIRE-JUGE3-REPLI-1], [PIRE-JUGE3-REPLI-2]. Un (rôle, modèle) sans pire refuse le départ (arrêt n° 34). Le repli n'est pas une bascule de clé. | décision (iii) | D-35 ; D-iii |
| R5 | V9 l. 377 (n° 6) et l. 378 (n° 7), lues à cinq espèces (A1 l. 161 ; DV l. 380) | « plafond d'une génération (190 USD) ou de la course (570 USD) atteint, ou réservation impossible \| arrêt avant le poste » ; « seuils d'une génération (180, 175, 160 USD) » | Chaque tentative est une **réservation neuve** qui repasse les n° 6 et 7 (lus 150 ; 140, 135, 120 ; 450). Une tentative refusée par l'un d'eux arrête la chaîne par cet arrêt, non par le n° 1. | une réservation par appel | D-35 |
| R6 | V9 l. 77 et l. 387 | journalisation avant chaque envoi ; « plus aucun octet ne change » | Chaque tentative écrit sa ligne « envoi » (même empreinte de requête assemblée, rang neuf, modèle demandé), repasse la garde de motifs et l'égalité. Journal en version neuve (le journal v3 est fermé). | un envoi neuf est un envoi | D-35 |
| R7 | V9 l. 51 (espèces numérotées) ; A1 | une espèce, un modèle | Une fiche rendue par un modèle de repli s'attribue au **modèle servi**, sous la rubrique « servies par repli », à part ; elle n'est jamais comptée à l'espèce demandée. À l'espèce demandée, l'appel est compté **sans fiche à elle**, dans la classe neuve « refus par classifieur, servi par repli » (écart R7-bis ci-dessous). | décision (i) | D-i ; D-22.1 |
| R7-bis | **V9 l. 92** | « Chaque appel de proposeur reçoit une **classe d'issue d'appel**, parmi quatre, exclusives » | « […] parmi **cinq**, exclusives » : la cinquième est « **refus par classifieur, servi par repli** » : la première tentative est refusée par un classifieur et au moins une tentative de repli est lancée et servie. Elle compte l'appel à l'espèce demandée, sans fiche ; non relancée au-delà de la chaîne ; distincte de l'arrêt n° 1. **Écart déclaré.** | point 5 de VE | D-22.1 |
| R7-ter | **V9 l. 101** | « La classe « fiches rendues » est rendue par programme ; les trois autres sont rendues par le portier, par une étiquette fermée » | « […] les trois autres sont rendues par le portier […] ; la cinquième est rendue **par programme**, au journal des tentatives (raison d'arrêt de la première tentative et modèle servi de la dernière). » **Écart déclaré.** | elle ne demande aucun avis | D-22.1 |
| R7-quater | **V9 l. 160**, M6 | « compte des appels de proposeur selon leur classe d'issue d'appel […] : « réponse vide motivée », « refus du modèle », « réponse illisible » ; rapportés à part, jamais comptés comme fiches rendues, donc hors du dénominateur de M3 et de la garde du coffre » | « […] : « réponse vide motivée », « refus du modèle », « réponse illisible », « **refus par classifieur, servi par repli** » ; rapportés à part, jamais comptés comme fiches rendues **de l'espèce demandée** […]. Les fiches servies par repli sont comptées à la rubrique « servies par repli » et à la génération (R8). » **Écart déclaré.** | point 5 de VE | D-22.1 |
| R8 | V9 l. 155 (M3, « parmi les fiches rendues ») ; **V9 l. 376**, arrêt n° 5 | « strictement plus d'un quart des fiches rendues d'une génération au coffre » | **Les fiches servies par repli entrent dans le compte de l'arrêt n° 5**, au numérateur comme au dénominateur : ce sont des fiches rendues au sens de la V9 l. 148 (« une tentative reçue par le portier »), et la garde porte sur ce que la génération sert. M3 est rapportée deux fois : (a) espèces seules, sans fiche de repli ; (b) génération entière, fiches servies par repli comprises, en lignes à part par modèle servi. Aucun double compte : l'appel compte à l'espèce dans M6 (R7-quater), ses fiches comptent à la génération. | point 7 de VE, tranché | D-22.3 |
| R9 | V9 l. 156, M4 | « coût en USD par espèce et par rôle […] Le cumul par clé ne sert qu'aux arrêts n° 11 à 13 » | Le coût de toutes les tentatives, refusées comprises, va au **cumul de la clé** (arrêts n° 11 à 13, inchangés). **M4 de l'espèce demandée** ne porte ni le coût des tentatives servies par repli ni leurs fiches : ils vont à la ligne « replis », par modèle servi. Rien de la rubrique « servies par repli » n'est rendu à la composition (N-045 v2). | décision (i) | D-i |
| R10 | V9 l. 150-161, M1 à M7 | mesures gelées | **Mesure descriptive neuve « replis »** : comptes, coûts et fiches par rôle, modèle demandé, modèle servi, catégorie (ou « non lue »), issue. M1 à M7 rapportées deux fois : (a) espèces seules, sans fiche de repli (lecture de la V9) ; (b) avec la rubrique « servies par repli », en lignes à part, jamais additionnée à une espèce. **Écart déclaré** : la classe neuve de M6 (R7-quater) ; aucune autre lecture gelée ne change. | GO-35 « rapporté à part » | D-35 ; D-22.1 |
| R11 | V9 l. 373 (n° 2), l. 374 (n° 3) ; CV l. 120-132 | « une espèce refuse, à la sonde de refus, la partie servie remplie […] \| elle est retirée de tous les rôles, sans reformulation » ; « un témoin planté manqué à l'épreuve des témoins \| aucune course » | **Le repli vaut aux lignes à part.** À la sonde, une chaîne dont la première tentative est refusée par un classifieur et qu'un modèle de repli sert donne l'issue « refus par classifieur au modèle de l'espèce, servi par repli » : **l'espèce n'est pas dite acceptante** ; ce n'est pas un refus de la question au sens du n° 2, qui ne se lève pas ; la course ne part pas, pour cette espèce, sans le mot de la mère sur une ligne neuve, comme au n° 27 (A1 l. 118). Un refus en prose rendu par un modèle de repli n'est pas un refus de l'espèce au sens du n° 2. Trois refus : n° 1, et l'espèce n'est pas dite acceptante, même suite. À l'épreuve des témoins, un témoin servi par repli se lit contre la table des issues ; manqué, il lève le n° 3. Le coût de la chaîne tient dans le plafond de chaque ligne : 5 dollars (épreuve), 1 dollar (sonde) (DV l. 382). | point 6 de VE, tranché | D-ii ; D-22.2 |
| R12 | V9 l. 94-99, classes d'issue | classe d'un appel | **Lettre accordée à R7** : une chaîne reçoit **deux** classes, une par ligne de rapport. À l'**espèce demandée** : si une tentative de repli a été servie, « refus par classifieur, servi par repli », quelle que soit l'issue de la dernière tentative ; si les trois tentatives sont refusées, aucune classe de M6, l'arrêt n° 1 (comme à la V9, où le refus de classifieur n'est pas une classe de M6). À la **rubrique « servies par repli »**, au nom du modèle servi : la classe de la dernière tentative, parmi les quatre de la V9 l. 94-99, marquée « par repli ». **Écart déclaré à R12 de NO**, qui disait une seule classe. | point 5 de VE | D-22.1 |
| R13 | A1 l. 118, arrêt n° 27 ; go.md l. 722 | « la sonde n'est pas relancée, l'espèce n'est pas dite acceptante, et la course ne part pas sans le mot de la mère sur une ligne neuve » | **Inchangé** : le n° 27 ne vise pas le refus de classifieur. Le refus de classifieur à la sonde relève du n° 1, puis du repli de R11. | GO-35 « n° 27 inchangé » | D-35 |
| R14 | DV l. 380, l. 386 ; GO-30 (go.md l. 629) | « ligne de course, montant exact \| 450 » ; « plafond total \| 456 » | Le repli **n'ajoute aucun montant** : il est compté dans la ligne de 450 et dans les parts. Le devis final (V9 l. 410) porte une ligne « replis » : pire d'une chaîne de proposeur, 3 × 6,05 = 18,15 dollars (PL, clé `repli_GO_35`) ; pire d'une chaîne d'aiguilleur et de juge, la somme de ses trois pires mesurés (R4). Les repères de 3,38 et 2,03 dollars ne valent qu'à la génération 1 et ne sont jamais des pires. | GO-35 « compté dans le devis » | D-35 |
| R15 | CV l. 166 ; AC l. 72 | « Le pire d'un appel de proposeur est de 6,05 USD » | Lu comme pire de **chaque tentative** d'un proposeur. | décision (iii) | D-iii |
| R16 | CO (non scellée) : contrôle A2 ; configuration du lot 6, `a11_modeles: []` | un modèle servi par rôle | A2 admet, pour une tentative, le seul modèle demandé de cette tentative ; le rôle garde son modèle pour l'appel suivant. `a11_modeles` reste vide ; un champ neuf « modèles de repli » porte la liste fermée de GO-35. Tout repli du fournisseur ou du kit lève le n° 31. | décision N1 | D-35 ; D-N1 |
| R17 | V9 l. 101 (avis du portier) ; CO § 2.4, § 2.5 | le verdict du portier ou d'un juge est l'avis de son modèle | Un verdict du portier ou d'un juge rendu par un modèle de repli **vaut verdict du rôle**, pour router la fiche ; il est marqué « par repli » au journal et rapporté à part (comptes par rôle et modèle servi). L'audit de symétrie du portier (V9 l. 180) est rendu deux fois, avec et sans ces verdicts. Proposition de l'auteur : question Q6. | sans quoi une fiche resterait sans classe | D-35 ; Q6 |

**Épreuves de la règle de repli** (règle R5), à jouer au lot 9 en moteur simulé, avant toute ligne payante : cas sain, refus au modèle demandé, repli servi, fiche rangée sous « servies par repli », jamais sous l'espèce, et comptée dans le n° 5 ; artefacts, trois refus lèvent le n° 1 ; une tentative qui dépasse la part lève le n° 12 ; une réservation impossible lève le n° 6 ; un modèle servi différent lève le n° 31 ; un repli du fournisseur lève le n° 31 ; une raison inconnue ou un refus en prose ne déclenche aucun repli ; une reformulation est refusée ; à la sonde, une chaîne acceptée par repli ne dit pas l'espèce acceptante et ne lève pas le n° 2.

---

## 6. Part de Luc

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| L-1 | **AC l. 57** ; CV l. 35 et l. 106 ; V9 l. 235 | « \| Luc \| aiguilleur ; proposeur de l'espèce 4 \| 66,51 \| 124,35 \| 125,63 USD, inchangée \| » ; V9 : « Une fois fixée, une part ne change plus. » | La part de Luc **peut être relevée, à 136,04 dollars au plus** (ligne de course de 450 moins les parts des quatre autres clés ; PL § 4, option (e)). Sa valeur exacte s'écrit à la pièce de relevés, sur le reste déclaré par Lazar, daté, et l'état des lots ouverts sur Luc : [PART-LUC] ≤ 136,04. Réserve déclarée : à 136,04, l'engagement est de 456,00 ; il ne reste rien sous la ligne pour le deuxième relais ni pour une chaîne de repli entière d'un proposeur de Luc (18,15) ; la tolérance aux lots ouverts tombe à 16,96. **Écart déclaré** à la V9 l. 235. | R-4807 (borne corrigée de 142,04 à 136,04) | D-L |
| L-2 | CV l. 116 | « **Si la part tombait sous 124,35 USD, la répartition ne tiendrait plus : nœud de Lazar, sans repli silencieux.** » | **Inchangée.** | — | — |

---

## 7. Protocole X : la question fusionnée

**Le mot.** GO-37 : « la question des modes et son ajout transmis à l'organisme pour la course « nouvelles attaques » ». `M/CLAUDE.md` l. 60 : « puis la question, fusionnée avec les autres questions ouvertes, servie à l'organisme d'idéation ». Consigne de la mère : servies **mot pour mot**, comme question fusionnée, aux proposeurs.

**Ce que le mot ne dit pas.** Si la question fusionnée remplace la partie servie, s'y ajoute, ou part à part. Les trois lectures ne coûtent pas la même chose (table X-0). Ce projet écrit la lettre de la lecture **(c)**, recommandée à Q1 ; s'il en retient une autre, le § 7 se récrit.

| lecture | ce qu'elle touche | effet |
|---|---|---|
| (a) remplacer la partie servie | V9 l. 49, 59, 62, 69-77, 90, 92-101, 110, 148, 155-161, 268-269, 279-313, 375, 381 ; PS entière ; le contrat de fiche à douze champs (PS l. 19) ; le portier et ses consignes (D3) ; les témoins ; C1 et M7 | la question neutre n'a ni case ni champs : la course devient une autre course ; préenregistrement neuf |
| (b) adjoindre la question fusionnée à chaque requête de proposeur | V9 l. 62, 69, 77 ; DV l. 418 (tailles) ; le contrat de sortie | deux contrats dans une requête : « Pour ce cas » (QA) vise le cas d'application de QN, la case de PS vise une autre case ; les réponses en prose de QN 1 à 5 tombent « hors du contrat de sortie » (V9 l. 99) ; mesures M3 à M7 brouillées |
| **(c) une passe à part, « passe X »** | V9 l. 62, 69, 77, 82, 171-173, 315 ; DV l. 382-386 ; GO-30 | une requête par espèce proposeuse, la question fusionnée seule ; la course de trois générations ne change pas |

**Lettre de la lecture (c).**

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| X-1 | V9 l. 62 | « […] sous la forme gelée ci-dessous. Rien d'autre. » | Inchangée pour les requêtes des trois générations. **Une requête de plus**, hors des générations : la « passe X », une par espèce proposeuse (cinq), sur la clé et par le relais du proposeur de cette espèce, avec ses réglages de proposeur. **Écart déclaré.** | GO-37 | D-X ; Q1 |
| X-2 | V9 l. 69 ; l. 77 | « Deux pièces fixes partent chez les fournisseurs dans une requête de proposeur, et elles seules » ; « Pour un proposeur : […] Pour une sonde de refus : la partie servie remplie, seule. » | Ajout d'un troisième type de requête assemblée : « Pour la passe X : la **question fusionnée**, seule, à l'octet ; ni partie servie, ni ligne de case, ni synthèse, ni registre. » Elle est journalisée et gardée comme les autres (arrêts n° 14 et 16). **Écart déclaré.** | mot pour mot | D-X |
| X-3 | — (pièce neuve) | — | **La question fusionnée** est une pièce fixe, dérivée une fois par un programme versionné et son journal, rejoués par un autre modèle, scellée avec son empreinte (forme recommandée à Q4) : le corps de QN (l. 3 à 11), une ligne vide, le corps de QA (l. 3), chacun à l'octet, guillemets compris ; **titres exclus** (ils nomment une réponse et un modèle : la garde n° 16, famille « identité et dépôt », mordrait, et ce serait un renvoi interne au sens de la V9 l. 73). Aucun mot n'est changé, ajouté ni retiré dans les corps. Épreuve : la pièce passe la garde de motifs sans un refus ; si un motif mord sur un corps, la question n'est pas servie et la mère est saisie : le texte n'est jamais retouché. | V9 l. 71 (même méthode que la partie servie) | D-X ; Q4 |
| X-4 | V9 l. 385, arrêt n° 14 | « l'arrêt vaut pour **toute pièce fixe servie** — la partie servie, la synthèse d'antériorité servie, les témoins plantés — » | « […] et la **question fusionnée** ». Artefact : un octet changé dans la question fusionnée refuse la passe X. | — | D-X |
| X-5 | V9 l. 82 ; l. 396 | « les fiches « passées », les fiches « hors case » et les réponses brutes, **noms compris** » | Les réponses brutes de la passe X sont en quarantaine, noms compris, sous les mêmes règles (arrêts n° 17 et 18). Rien de la passe X n'est servi à personne : ni au registre servi, ni à une génération, ni au portier, ni aux juges. | quarantaine | D-X ; D-K |
| X-6 | V9 l. 65 | « toutes les fiches classées « passée » sont relues « aucune recette » après la troisième génération par **une session à part** » | Les réponses de la passe X sont relues de même, par la même session à part, après la troisième génération ; ce qui glisse vers le concret va au coffre. Aucun portier n'est appelé sur elles. | pas de fiche, pas de contrat | D-X |
| X-7 | V9 l. 315 ; l. 386 (n° 15) | « Les mesures […] sont lues une fois, après la troisième génération » ; « une sortie d'un modèle sur la question lue avant le scellement de ce texte » | La passe X est lue avec le reste, une fois, après la troisième génération. Une réponse de la passe X lue avant le scellement de l'additif, ou avant la fin de la troisième génération, lève le n° 15. | même règle | D-X |
| X-8 | V9 l. 150-161 | mesures gelées | **Mesure descriptive neuve « passe X »** : par espèce, la classe d'issue de l'appel (« réponse rendue », « refus du modèle », « réponse illisible », « refus par classifieur, servi par repli »), son coût ; par la session à part, en comptes seulement : le nombre de propositions de la question 6, « aucune » compté à part. Lecture de nouveauté de ces propositions par les deux lecteurs d'antériorité, sous l'épreuve scellée du § 8 (étendue : Q5). Rien n'en entre dans M1 à M7. | GO-37 | D-X ; Q5 |
| X-9 | repli | — | La passe X est une ligne à part au sens de la décision (ii) : le repli s'y applique (R1 à R12) ; une réponse servie par repli est attribuée au modèle servi et rapportée à part. | D-ii | D-ii |
| X-10 | V9 l. 171-173 ; DV l. 382-386 ; GO-30 (456 dollars) | « lignes à part, avant la course » ; « **plafond total** \| **456** » | Une **ligne à part neuve, « passe X »**, après les deux lignes à part et avant la génération 1, hors des parts des clés. Pire au repère de 6,05 par tentative : deux espèces sur clés Claude, trois tentatives chacune, plus trois espèces sur une tentative, soit 2 × 18,15 + 3 × 6,05 = **54,45 dollars** au plus ; plafond à chiffrer au devis final sur la mesure des consignes (taille réelle de la requête). Au-delà de 456 dollars : **dépense, nœud de Lazar** (Q2). Aucune passe X sans son mot. | GO-37 ne chiffre rien pour l'organisme | Q2 |
| X-11 | V9 l. 382-384, arrêts n° 11 à 13 | — | Valent pour la passe X, sur la clé de chaque espèce, au plafond de sa ligne (comme R11) ; un arrêt de la passe X n'arrête pas la course, sauf le n° 13, qui arrête la course par sa lettre. | — | D-X |

---

## 8. Définition du mode et épreuve de nouveauté : place et forme

Le contenu vient d'une pièce à part ; ce projet n'en écrit rien. Il fixe sa place, sa forme et sa garde.

| n° | texte, ligne | lettre scellée | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| D-1 | V9 l. 90 | « La définition de la note de périmètre v3, § 1, est reçue ici » | La définition de la course est celle de la pièce « **définition du mode et épreuve de nouveauté** », scellée avant le départ, citée ici par son chemin et son empreinte : [CHEMIN-DEF], [EMPREINTE-DEF]. La pièce dit elle-même si elle remplace la définition de la l. 90 ou la précise. **Écart déclaré**, s'il y a remplacement. | décision 1 | D-1 (Lazar) |
| D-2 | V9 l. 325 | « une seule vaudra, celle que son mot retient, portée par la mère au complément de valeurs avant toute lecture de fiche » | La branche retenue (« avec » ou « sans ») et, dans la branche « avec », la liste de référence sont dans cette pièce, **scellées avant le départ** (avant toute requête de la course et de la passe X), non au complément avant la lecture. **Écart déclaré** (le terme est avancé ; la lettre de la règle d'antériorité ne change pas). | décision 1 | D-1 |

**Forme exigée de la pièce** (sept rubriques, aucune vide) :
1. la définition, une seule, et son rapport à la V9 l. 90 ;
2. l'épreuve : des questions fermées, par oui ou non, leur ordre, qui y répond (chacun des deux lecteurs d'antériorité, à part), la règle qui mène des réponses à l'étiquette, la règle de désaccord ;
3. la branche de la V9 l. 325-330 retenue, et la liste de référence si la branche est « avec », scellée avec elle ;
4. les témoins qu'elle doit passer, issue connue d'avance : au moins le témoin « variante d'une famille connue » de la V9 l. 107, qui doit sortir « variante » ; un lecteur qui le manque voit ses étiquettes annulées (V9 l. 360) ;
5. son champ : les fiches des trois générations, et les propositions de la passe X (Q5) ;
6. ce qu'elle ne contient pas : aucun candidat de mode, aucun nom ni énoncé de mode, aucune case nommée, aucun identifiant de modèle ;
7. sa provenance : auteur, inventaire de ce qu'il a lu, avec chemins et empreintes, et sa déclaration écrite de n'avoir lu aucun candidat de mode (§ 9) ; sa contre-lecture ; le mot de Lazar.

**Jamais servie** : ni aux proposeurs, ni à la passe X, ni au portier, ni aux juges ; elle n'est donnée qu'aux deux lecteurs d'antériorité. Elle entre à la table de l'arrêt n° 14. **Arrêt n° 37** : la pièce manque, n'est pas scellée, a une autre empreinte, ou a été scellée après une requête de la course ou de la passe X : départ refusé.

---

## 9. Règle d'ancrage

| n° | texte, ligne | lettre | lettre nouvelle | raison | décision |
|---|---|---|---|---|---|
| K-1 | V9 l. 62, l. 69, l. 73 ; A1 § 2 | ce qui est servi ; « Rien d'autre » | **Règle neuve.** Aucun candidat de mode (nom, énoncé, résumé, ou pièce qui en porte un), d'où qu'il vienne (réponses de modèles à la question des modes ou à toute autre demande, dossiers du collisionneur, matière première, pièces séquestrées, notes de la mère), n'entre dans une requête servie à un proposeur, à la passe X comprise, ni dans les entrées d'une session qui conçoit sondes, agrégateurs, traits de texte ou seuils, ni dans celles de l'auteur de la pièce du § 8. Seule exception, lue de la V9 et à confirmer (Q3) : le **registre servi** aux générations 2 et 3, fait des fiches passées de cette course, sous sa forme gelée (V9 l. 63) et ses arrêts n° 9, 16 et 19. | décision de la mère | D-K ; Q3 |
| K-2 | — | — | **Mise en œuvre** : la composition de chaque requête assemblée est journalisée pièce par pièce, par empreinte, contre une liste fermée (partie servie remplie, synthèse servie, registre servi, question fusionnée). Une pièce hors liste refuse l'envoi (**arrêt n° 36**). Épreuve : cas sain, une requête des seules pièces de la liste part ; artefact, une requête qui porte un texte inerte planté hors liste est refusée, avec son nom. Pour les concepteurs, la règle est tenue par la quarantaine (arrêts n° 17, 18) et par les conditions de A1 § 2 ; l'inventaire scellé des entrées (condition (b) de A1) s'étend à toute session qui conçoit un moniteur après la course. | R5 | D-K |
| K-3 | — | — | **Ce que la règle ne fait pas** : le programme compare des empreintes, non un sens ; il ne voit pas un candidat qu'un proposeur redirait de lui-même ; il ne voit pas ce qu'un concepteur a lu par une autre voie (A1 l. 94, même réserve). | dit sans forcer | — |

---

## 10. Arrêts neufs proposés

Numéros à partir du n° 31 (R-4603), sans réemploi (R-4479). Proposés, à confirmer par la mère à l'assemblage de l'additif entier, où d'autres arrêts (par exemple les onze refus écrits d'un proposeur, CO l. 419) prendront les numéros suivants.

| n° | condition | action | épreuve : cas sain ; artefact |
|---|---|---|---|
| 31 | modèle servi d'une tentative différent du modèle demandé de cette tentative ; ou trace d'un repli du fournisseur ou du kit (A2, CO mot 6) | arrêt nommé de la course pour ce rôle, réponse non lue ; consigné | même modèle : lu ; autre modèle : arrêt ; paramètre de repli dans une requête : refusé avant l'envoi |
| 32 | réglage non textuel non admis pour un (rôle, modèle), dont les modèles de repli (A7) | départ refusé, avec le nom du réglage | réglages admis : départ ; un réglage non admis sur le second modèle de repli : refus |
| 33 | module chargé hors table, ou d'une autre empreinte (C-1) | départ ou génération refusé | table égale : départ ; module planté : refus |
| 34 | un (rôle, modèle) sans pire écrit (R4) | départ refusé | tous écrits : départ ; un pire de repli manquant : refus |
| 35 | (réservé) envoi Google refusé par la garde avant l'envoi (G-1) | refus écrit, compté, jamais un appel ; la course continue | corps conforme : envoyé ; réflexion implicite : refus |
| 36 | pièce hors de la liste fermée dans une requête assemblée (K-2) | envoi refusé ; consigné ; nœud de la mère | voir K-2 |
| 37 | pièce du § 8 absente, non scellée, d'autre empreinte, ou scellée après une requête | départ refusé | voir § 8 |
| 38 | question fusionnée qui ne passe pas la garde de motifs, ou d'autre empreinte | passe X refusée ; texte jamais retouché ; nœud de la mère | voir X-3, X-4 |

---

## 11. Valeurs qui attendent une mesure, avant le scellement

| valeur | règle | source |
|---|---|---|
| [PIRE-AIGUILLEUR-*], [PIRE-JUGE3-*] : six pires par (rôle, modèle) | mesure des consignes sans appel, à la plus grande fiche, à la sortie maximale de chaque jeu de A7 | CV l. 83 ; AC l. 72 ; R4 |
| [PIRE-G-PROPOSEUR], [PIRE-G-JUGE] | même mesure, sous les réglages de `garde_google_v3` | G-3 |
| relevé de l'adaptateur direct au faux fournisseur, derrière le vrai relais : aucun texte système reçu, consigne extraite égale à l'empreinte du journal | CO l. 228 ; A-1 | lot 4 v2 (hors additif) ; sortie scellée citée ici |
| [PART-LUC] ≤ 136,04 | pièce de relevés | L-1 |
| plafond de la ligne « passe X » | devis final, mot de Lazar | X-10 |

---

## 12. Questions qui restent, avec recommandation

**Q1 — à Lazar (nœud : écart à un préenregistrement scellé).** *Décision* : comment la question fusionnée est servie. *Enjeu* : GO-37 transmet la question « pour la course » sans dire la forme ni déclarer l'écart. *Options* : (a) remplacer la partie servie — fidèle à « la question de la course », mais c'est une autre course, préenregistrement neuf, départ repoussé ; (b) l'adjoindre aux requêtes des générations — une seule course, mais deux contrats dans une requête et des mesures brouillées ; (c) passe X à part — la course scellée ne change pas et la question part mot pour mot, mais une ligne de dépense de plus. *Recommandation* : (c), confiance 0,6. Aucun défaut : c'est un nœud.

**Q2 — à Lazar (dépense).** *Décision* : la ligne « passe X », au plus 54,45 dollars au repère de 6,05 par tentative, à chiffrer au devis final, au-delà des 456 dollars de GO-30. *Options* : (a) l'accorder sur le devis final ; (b) la mettre dans la ligne de course — impossible si la part de Luc est relevée à 136,04 (rien ne reste sous 450) ; (c) pas de passe X dans cette course. *Recommandation* : (a), confiance 0,7.

**Q3 — à la mère, puis à Lazar si elle change l'objet de la course.** *Décision* : la règle d'ancrage couvre-t-elle le registre servi ? *Enjeu* : lue à la lettre (« d'où qu'il vienne »), elle retire l'héritage, objet de la course (M1, M2). *Options* : (a) exception déclarée pour le registre servi de cette course ; (b) pas d'exception, une seule génération héritée de rien, version neuve. *Recommandation* : (a), confiance 0,75 ; défaut sous 48 heures : (a).

**Q4 — à la mère.** *Décision* : forme de la fusion. *Recommandation* : corps de QN, une ligne vide, corps de QA, à l'octet, guillemets compris, titres exclus, par programme rejoué par un autre modèle (X-3). Confiance 0,7 ; défaut sous 48 heures : cette forme.

**Q5 — à la mère.** *Décision* : les propositions de la passe X sont-elles lues pour la nouveauté, et dans la borne de 60 fiches (V9 l. 177) ? *Recommandation* : toutes lues, hors de la borne, comptées à part, sous l'épreuve du § 8. Confiance 0,6 ; défaut : cette recommandation.

**Q6 — à la mère.** *Décision* : un verdict du portier ou d'un juge rendu par repli vaut-il verdict du rôle (R17) ? *Recommandation* : oui, marqué et rapporté à part, audit de symétrie rendu deux fois. Confiance 0,65 ; défaut : oui.

**Q7 — à la mère (à vérifier sur pièce avant le lot 4 v2).** `garde_google_v3` ne connaît que les espèces de sa table (GG l. 80 et l. 107) ; si une espèce Google de la course n'y est pas, « telle quelle » ne tient pas et une v4 serait une copie, contraire à N4. *Recommandation* : vérifier d'abord ; si elle manque, nœud de la mère, rien de copié. Confiance 0,6.

**Q8 — à Lazar, déjà ouvert (décision 1).** Le mot sur la définition du mode et l'épreuve de nouveauté. Sans lui, la pièce du § 8 ne se scelle pas, l'arrêt n° 37 refuse le départ.

---

## 13. Pièces à sceller avant le départ, dans l'ordre

1. **Inscriptions au registre des décisions** (non scellées, préalables) : N1 à N4, (i) à (iii), D-22.1 à D-22.3, D-X, D-K, D-L ; la provenance de `garde_google_v3` (G-5).
2. **Mots de Lazar** : Q1, Q2, Q8 ; avant eux, rien ne se scelle de ce qui en dépend.
3. **Sortie de la mesure des consignes sans appel**, scellée : les huit pires du § 11 (avec le relevé de l'adaptateur direct au faux fournisseur).
4. **Question fusionnée**, son programme et son journal, rejoués, scellés ; son épreuve de garde de motifs consignée (X-3).
5. **Pièce « définition du mode et épreuve de nouveauté »**, contre-lue, scellée (§ 8).
6. **Additif du véhicule**, assemblé de ce projet et des autres valeurs ouvertes (CO § 5.2, § 5.3, § 9), contre-lu, revu par Fable, corrigé, vérifié, scellé par la mère ; il cite 3, 4 et 5 par empreinte.
7. **Configuration de course** (lot 6 v4), sur les valeurs de l'additif : modèles de repli, jeux de A7, table des rôles et des clés ; scellée avec l'additif (CO l. 536).
8. **Table d'empreintes du code chargé** (C-1), avec `garde_google_v3` épinglée.
9. **Tirage des cases et des clés n° 30 et n° 40**, joué deux fois, scellé.
10. **Consignes du portier et des juges** (D3) et **témoins plantés** avec leur table, scellés ; la liste des motifs est déjà scellée (lot 2 v5).
11. **Devis final** récrit (V9 l. 410), avec les lignes « replis » et « passe X ».
12. **Pièce de relevés, premier temps** ; puis les lignes à part (sonde, épreuve des témoins, passe X si accordée) ; puis **pièce de relevés, second temps**, scellée, avec [PART-LUC] ; puis la lettre de départ de la mère sous GO-30.

Les points 7 à 10 sont des pièces de lots ; ils restent hors de l'additif et sont listés pour l'ordre seulement.

---

## Réserves de l'auteur

1. Les décisions de la mère du 22 novembre sont portées sur la foi de la transmission de la coordinatrice ; je ne les ai pas lues au registre.
2. La lecture (c) du protocole X est la mienne ; ni GO-37 ni la consigne ne la donnent.
3. Le repère de 54,45 dollars suppose le pire de 6,05 par tentative, valable pour une requête de proposeur ; la requête de la passe X est plus courte, son pire réel est plus bas, à mesurer.
4. Je n'ai lu ni le code des lots, ni la configuration du lot 6, ni l'additif de la matière première (consigne) ; la compatibilité de la règle d'ancrage avec la colonne en « garde seule » est supposée (rien n'y est servi, CO l. 463), à vérifier à l'assemblage.
5. Les numéros d'arrêt 31 à 38 sont proposés ; un autre agent peut en avoir déjà pris.

— auteur Opus, 2026-11-22
