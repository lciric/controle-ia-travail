# Devis de la passe X rallongée — course « nouvelles attaques » — v2

Pièce de travail, non scellée. Elle part à la vérification du même contre-lecteur.
- Auteur : Opus, l'auteur de la v1, le 2026-11-22.
- Processeur seul : aucun appel de modèle, aucun réseau, aucune clé lue, aucune dépense, rien écrit dans un dépôt.

**Version.** La v2 remplace la v1 : `devis-passe-x-v1.md`, `8222fef35f4e913a…`, archivée sans changement. Elle fait suite à la contre-lecture `C/devis-passe-x-v1/contre-lecture-v1/contre-lecture-devis-passe-x-v1-v2.md`, verdict « À corriger », points B1 à B4 et « à noter ». Elle porte aussi deux messages de la coordination : les décisions de la mère sous GO-2026-11-22-48, et la sortie maximale de Claude 4.6 lue sur la page officielle.

**Programme.** `calcul_devis_passe_x_v2.py`, dans ce dossier, avec sa sortie `calcul-devis-passe-x-v2.json`. Il a été joué deux fois ; les deux sorties sont égales à l'octet (`cmp`). Il porte **neuf contrôles, tous calculés** (J l. 2-12, `nombre_de_controles` l. 458) ; aucun n'est écrit en dur ni vrai par construction. Chaque fichier a son compagnon `.sha256`.

**Sigles.**
- **J** : la sortie JSON du programme.
- **C** : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.
- **AV** : `C/additif-vehicule-na-projet-v2/additif-vehicule-na-projet-v2.md` (`6e9bb88e680211b1…`).
- **V9**, **CV**, **AC**, **DV**, **PL**, **PJ**, **LQ**, **TK**, **RQ** : comme en v1.
- **AN** : `/home/user/controle-ia-travail/docs/sources/tarifs/anthropic-2026-11-22/lecture-modeles-anthropic-v1.md` (`3cfae6e0561ecbbd…`).
- **GO** : `/home/user/main-lecture/registres/go.md`, relu à jour (734 lignes, `7cdfb9e83f9ceeea…`). GO-45 y est à la l. 732, GO-46 à la l. 733.
- **GO-48 n'est pas dans ce fichier** : aucune occurrence de « GO-2026-11-22-48 ». Ses décisions sont portées sur la transmission de la coordination et marquées « (GO-48, transmis) ». Il faut le réancrer avant le scellement.

## Résumé (moins de 300 mots)

**Pire de la passe X : 96,80 USD, sous les 200 USD de GO-46, marge 103,20 (J l. 189, l. 360-365). Rien à couper.**

1. **Pièce** : dix-sept corps, chacun précédé de « [Pièce k sur 17] », séparateur déclaré à l'enveloppe ; 20 235 signes ; entrée au pire 21 413 jetons (J l. 1275-1284). Retirer les neuf titres est un écart déclaré à X-3.
2. **Sortie** : 96 000 jetons. Elle tient sous les 128 000 vérifiés d'Opus et de Sonnet 4.6 (AN l. 7-8). Toute tentative reste sous 6,05 USD jusqu'à 116 717 jetons. Les autres sorties maximales sont à relever.
3. **Coût** : attendu 8,76 ; pire calculé 44,43 ; pire de lettre 96,80, soit seize tentatives à 6,05. Par clé : Luc 72,60 ; Google 12,10 ; OpenAI 6,05 ; Kimi 6,05. P_X = 84,70 + 2 × max(6,05 ; pire Google mesuré sous la garde), sous 200 tant que ce pire reste sous 57,65.
4. **Luc** porte tout Anthropic (R-4852, sous GO-46). Lu en compte payant à recharge (GO-42, GO-48 transmis), il engage au pire 325,64 USD : part de la course 136,04, Fable au moins 117 (GO-45), passe X 72,60. La recharge doit payer 172,64 au-delà du reste de 153. Sans cette lecture, la part tombe à 36,00 : nœud L-2.
5. **Moment** : avant la course ou sans elle, d'ici le 30 novembre. Je recommande sans elle (confiance 0,6).
6. **L'espèce 3 payée sur Luc** est un écart au n° 12, seconde clause, accepté par la mère.
7. **Pour la suite** : lieux de l'additif au § 5 ; liste du complément neuf au § 6.

**Réserve** : GO-48 et R-4852 ne sont pas lus. GO-48 est absent de `go.md` (`7cdfb9e8…`).

## 1. La pièce fusionnée

**Règle de formation.** Les dix-sept fichiers sont pris dans l'ordre de la liste fermée de GO-46 (l. 733) : les sept pièces servies, le lot, puis les huit pièces jamais servies. Chaque pièce donne une ligne de séparateur, une ligne vide, puis son corps à l'octet. Une ligne vide sépare deux pièces ; une fin de ligne termine le tout.

**Séparateur et numérotation (« à noter », § 2 de la contre-lecture ; décision de la mère).**
- Le séparateur `[Pièce k sur 17]` est une pièce de l'enveloppe, déclarée à K-2 (5) (AV l. 229). Il n'appartient à aucun corps, et aucun mot d'un corps n'est changé : le « mot pour mot » de GO-37 (l. 724) tient.
- Le contrôle 4 vérifie que chaque corps se retrouve intact dans la pièce (J l. 6).
- La numérotation est celle des pièces. Les listes internes ne sont pas renumérotées : cinq pièces repartent à 1 (pièces 1, 4, 7, 9 et 15 ; J l. 367).
- Un point se désigne donc « pièce k, point n ». La question 6 de QA devient « pièce 2, point 6 », sans ambiguïté avec le point 6 de la pièce 4.

**Titres retirés : écart déclaré à X-3.**
- X-3 (AV l. 186) ne retire que « les titres qui nomment un modèle ». Ici, les neuf titres sont retirés (J l. 1590).
- Quatre d'entre eux ne nomment aucun modèle : billet-drapeau, cœurs, étau-équipe-rouge, théorème négatif (J l. 1591).
- Raison : ces titres décrivent l'histoire des correctifs du test de devinette et l'origine des notes ; ils ne font pas partie de la question.
- Cet écart est accordé par la mère (GO-48, transmis).

**Tailles.**

| | signes | octets | entrée (attendu ; haut ; pire, en jetons) | source |
|---|---|---|---|---|
| **avec séparateurs (recommandée)** | 20 235 | 20 901 | 6 916 ; 10 374 ; 21 413 | J l. 1275-1284 ; empreinte `39fb4e93f26f6447…` |
| sans séparateurs (v1) | 19 921 | 20 570 | 6 811 ; 10 217 ; 21 082 | J l. 1286-1294 |

**Rapports signes par jeton.** Ce sont des règles, non des mesures :
- 3 signes par jeton pour l'attendu (LQ l. 34) ;
- 2 signes par jeton pour le haut, plus prudent que les 2,5 de DV l. 211 ;
- 1 jeton par octet pour le pire (DV l. 210).

L'enveloppe est bornée à 512 octets, une valeur à geler à K-2 (5).

**Le mot « quarantaine ».** Il est absent de tout corps (contrôle 5). Il n'était que dans le titre de la pièce du lot (§ 5, X-3).

## 2. Le plafond de sortie

Je propose **96 000 jetons par tentative, réflexion comprise**, en jeu A7 propre à la passe X (AV l. 82).

Le besoin, justifié comme en v1 :
- environ 32 000 jetons de texte, soit à peu près 1 900 par question ;
- une réserve de réflexion du double, parce que Kimi a déjà pris 32 765 jetons de raisonnement sur 32 768 (RQ l. 52) ;
- au-delà de **116 717 jetons**, une tentative au tarif de 10 / 50 dépasse 6,05 USD. Le contrôle 7 l'établit des deux côtés de la borne (J l. 1550).

| modèle | sortie maximale | 96 000 tient-il ? | source |
|---|---|---|---|
| Opus 4.6 | 128 000, interface synchrone | oui (contrôle 9) | AN l. 7, l. 10 |
| Sonnet 4.6 | 128 000 ; la crainte d'un plafond à 64 000 est levée | oui | AN l. 8, l. 12 |
| espèces 1 et 5 (Google), espèce 2, espèces 3 et 4, Kimi | **à relever** | inconnu | J l. 1572 (paramètre `SORTIE_MAX` du programme) |

**Si une sortie maximale est plus basse.** Le plafond de ce modèle devient sa sortie maximale. Chez Google, la réflexion vaut au plus la sortie maximale moins 32 000 jetons. Par exemple, à 65 536 jetons, la réflexion est bornée à 33 536 (J l. 1551 et suivantes ; c'est une table d'information, non un contrôle).

**La règle de Google** (réflexion + 16 000 jetons de texte) est tenue dans la lettre. Elle ne s'éprouve que contre la sortie maximale relevée et la mesure sous la garde.

**Le pire Google.** Les 4,17 USD sont un calcul. G-3 (AV l. 108) exige que le pire d'un appel Google soit **mesuré sous `garde_google_v3`**, avec `mots=None` (G-6) et au jeu A7 de la passe X : c'est la valeur [PIRE-G-PROPOSEUR-X].

**Quand il est mesuré, P_X se recalcule** : P_X = 14 × 6,05 + 2 × max(6,05 ; [PIRE-G-PROPOSEUR-X]). Exemples :
- 96,80 si ce pire est à 6,05 ;
- 100,70 s'il est à 8 ;
- 108,70 s'il est à 12.

P_X reste sous 200 tant que ce pire ne dépasse pas 57,65 (J l. 1265-1273).

**Flux.** De mémoire, et non opposable : à ce plafond, le kit d'Anthropic peut exiger le flux. C'est un réglage A7 à fixer et à éprouver au faux fournisseur. AN l. 10 parle de l'interface synchrone.

**Réserve.** Une fin en plafond de jetons chez Google ou chez Kimi est un défaut journalisé, jamais rejoué (G-2).

## 3. Devis

**Tarifs** (J l. 1582 et suivantes) :
- Google et OpenAI : comme en v1, cités (RQ l. 25-31) ;
- espèces 3 et 4 : 10 / 50, leur identité n'étant pas dans les pièces lues ;
- Kimi : 2 / 10, vérifié (TK l. 10-11) ;
- **Opus 4.6 : 5 / 25 et Sonnet 4.6 : 3 / 15, vérifiés sur la page officielle gardée** (AN l. 7-8). Leurs identifiants viennent de la référence de l'outil (AN l. 11).

**Règles des cas** : inchangées depuis la v1. La chaîne de GO-35 est lue à la lettre.

| proposeur | clé | pire par tentative calculé | attendu | haut | pire calculé | tentatives au pire | **pire de lettre** |
|---|---|---|---|---|---|---|---|
| espèce 1 | deuxième relais | 4,17 | 0,40 | 1,58 | 4,17 | 1 | 6,05 |
| espèce 2 | troisième relais | 5,02 | 1,99 | 3,95 | 5,02 | 1 | 6,05 |
| espèce 3 | **Luc, R-4852 sous GO-46** | 5,02 ; 2,51 ; 1,51 | 1,99 | 5,92 | 9,03 | 3 | 18,15 |
| espèce 4 | Luc, R-4852 | 5,02 ; 2,51 ; 1,51 | 1,99 | 5,92 | 9,03 | 3 | 18,15 |
| espèce 5 | deuxième relais | 4,17 | 0,40 | 1,58 | 4,17 | 1 | 6,05 |
| ajout Kimi | `KIMI_API_KEY`, par son nom | 1,01 | 0,40 | 0,79 | 1,01 | 1 | 6,05 |
| ajout Opus 4.6 | Luc, R-4852 | 2,51 ; 2,51 ; 1,51 | 1,00 | 3,95 | 6,52 | 3 | 18,15 |
| ajout Sonnet 4.6 | Luc, R-4852 | 1,51 ; 2,51 ; 1,51 | 0,60 | 1,19 | 5,52 | 3 | 18,15 |
| **total** | | | **8,76** | **24,85** | **44,43** | **16** | **96,80** |

Les détails par proposeur sont à J l. 187-366.

**Par clé** (J l. 190) :

| clé | attendu | pire calculé | pire de lettre |
|---|---|---|---|
| Luc | 5,57 | 30,09 | 72,60 |
| deuxième relais (Google) | 0,80 | 8,33 | 12,10 |
| troisième relais (OpenAI) | 1,99 | 5,02 | 6,05 |
| Kimi | 0,40 | 1,01 | 6,05 |

La somme des clés égale le total (contrôle 8).

**Autre lecture.** Si l'on saute un modèle de repli déjà tenté, le pire de lettre vaut 78,65, dont 54,45 sur Luc (J l. 13-186).

**Options** (pire de lettre et marge sous 200) :

| option | pire de lettre | marge | source |
|---|---|---|---|
| sortie de 64 000 | 96,80 | 103,20 | J l. 1084 |
| sortie de 128 000 | 98,50 | 101,50 | J l. 904 ; à 10 / 50, une tentative dépasse 6,05 : P4 demande alors une version neuve |
| sans les deux ajouts Claude | 60,50 | 139,50 | J l. 762 |
| les cinq espèces seules | 54,45 | 145,55 | J l. 460 ; on retrouve X-10 |
| deux requêtes de 64 000 | 193,60 | 6,40 | J l. 582 |

**Recommandation** : P_X = 96,80 USD tant que [PIRE-G-PROPOSEUR-X] ne dépasse pas 6,05 ; sinon, la formule du § 2. Confiance 0,7.

## 4. Luc, et les moments de la passe X (B1 à B4)

**B1 — La clé.**
- Tout appel d'Anthropic de la passe X, replis compris, se paie sur **Luc**. La base est R-4852, la décision de la mère sous GO-46 ; je ne l'ai pas lue au registre des décisions, qui n'est pas dans ma liste.
- GO-45 (l. 732) ne couvre que les appels à Fable. **Minuit n'est pas appelée.**
- Les rôles de la **course** (juge et proposeur de l'espèce 3, lignes à part payées par Minuit) restent sur Minuit et sont **bloqués** jusqu'au mot du directeur (GO-48, transmis).

**B2 — La charge de Fable sur Luc (GO-45, l. 732).**

| demande | plafond (USD) |
|---|---|
| demande 27 | 8 |
| relance des demandes 22, 23 et 24 | 17 |
| mathématiques | 50 |
| banc | 24 |
| chantiers | 18 |
| **total** | **au moins 117** |

Les demandes 28 à 30 n'ont pas de plafond écrit : elles ne sont pas comptées (J l. 404-413). Pour les mathématiques, **GO-45 prime sur GO-43** (« pas d'appels API ») : elles sont sur Luc (GO-48, transmis).

**Lecture retenue : compte payant à recharge** (GO-42, l. 729 : « la laisser agir » ; GO-48, transmis).
- Cette lecture remplace « aucune recharge supposée » de GO-30 (l. 629).
- Le reste déclaré ne borne plus ; c'est l'engagement au pire qui compte (J l. 414-425).

| part de la course sur Luc | engagement au pire | au-delà de 153 | dont hors passe X |
|---|---|---|---|
| 125,63 | 315,23 | 162,23 | 89,63 |
| 136,04 | 325,64 | **172,64** | 100,04 |

Le montant « au-delà de 153 » est ce que la recharge doit payer. Sur Luc, la passe X ajoute 72,60 au pire de lettre, 30,09 au pire calculé et 5,57 en attendu.

**Lecture scellée, sans compte payant**, donnée pour mémoire. La part vaut le reste moins le pire des lots non clos (R-4289 ; CV l. 111). Le nœud L-2 se lève sous 124,35 (CV l. 116). Résultats (J l. 426-448) :

| lots ouverts sur Luc | part | arrêt n° 11 contre 125,63 |
|---|---|---|
| Fable seule | 36,00 | manque 89,63 |
| Fable et passe X avant la course, au pire de lettre | −36,60 | manque 162,23 |
| Fable et passe X avant la course, au pire calculé | 5,91 | manque 119,72 |

Dans les trois cas, c'est le nœud L-2. Cette lecture ne tient qu'avec le complément neuf du § 6.

**Correction de la v1.** Les 16,96 USD sont le reste **si la part de 136,04 est consommée en entier**. Au cas haut des rôles de Luc, le reste vaut 28,65 (J l. 454-455).

**B3 — La seconde clause de l'arrêt n° 12** (V9 l. 383 : « un appel d'un rôle se présente sur une autre clé que la sienne »).
- Dans la passe X, l'espèce 3 se paie sur Luc, alors que son rôle de course est sur Minuit.
- **C'est un écart déclaré, accepté par la mère** (GO-48, transmis).
- Lettre : « Pour la passe X, la clé d'un proposeur est celle de la table de X-11, non celle de son rôle de course. La seconde clause du n° 12 se lit contre cette table : un appel de passe X présenté sur une autre clé que la sienne est refusé, sans bascule. »
- Épreuve, sur un cas sain et sur un artefact (R5). Cas sain : l'espèce 3 de la passe X, sur Luc, part. Artefact : la même requête présentée sur Minuit est refusée.

**B4 — Le moment.** L'échéance de GO-46 passe du 26 novembre (l. 733) au **30 novembre** (GO-48, transmis) ; GO-30 échoit le 27 novembre (l. 629). La passe X se lit une fois et se rapporte à part.

| moment | arrêt n° 11 | arrêt n° 12 | lecture (X-7, n° 15) |
|---|---|---|---|
| **(A) avant la course** | Celui de la course n'est pas touché pour le départ de la passe X. Mais ses dépenses s'inscrivent sur Luc avant le départ de la course. Avec un compte payant, le n° 11 de Luc ne refuse pas pour le reste, et le complément neuf doit le dire. Sinon, la part de Luc tombe : manque de 119,72 à 162,23 (§ 4, B2). | Pour la passe X : sous-parts par clé de X-10, avec la seconde clause lue comme en B3. Celui de la course n'est pas touché, la passe X étant comptée contre P_X. | Réponses en quarantaine stricte, non lues avant la fin de la génération 3. Si la course ne part pas avant le 30 novembre, la lecture se fait sous (B). |
| **(B) sans la course** | Celui de la course est sans objet. Un contrôle de ligne propre à la passe X tient : reste relu ou statut payant de chaque clé, contre sa sous-part. | Sous-parts de X-10, seconde clause comme en B3. | Lue une fois, après la dernière réponse de la passe X ; tri de X-5 par la session à part. C'est un **écart à X-7** : la lecture n'attend plus la génération 3. |
| (C) après la course (Q9 (a) de la v1) | — | — | **Écarté.** La course est bloquée sur Minuit, et la fin de la génération 3 au 27 novembre est incertaine. |

**Recommandation : (B), sans la course.** La passe X ne dépend pas d'une course bloquée, et elle n'expose ni le n° 11 ni le n° 12 de la course. Confiance 0,6. Choisir (A) si le directeur veut que la course parte d'abord.

## 5. Les lieux de l'additif à récrire

La lettre de la v1 (§ 4) vaut, avec les corrections suivantes.

| lieu (AV) | lettre proposée ou correction |
|---|---|
| § 7, lectures (l. 171-180) | « Lettre de la lecture (d) », retenue par GO-42 et étendue par GO-46. |
| X-1 (l. 184) | Huit proposeurs : cinq espèces et trois proposeurs ajoutés, sans numéro d'espèce. Jeu A7 de la passe X : 96 000 jetons ; réflexion Google au plus 64 000 ; aucune limite de mots. |
| X-2 (l. 185) | La question fusionnée seule, avec l'enveloppe de K-2 (5), qui comprend les séparateurs « [Pièce k sur 17] ». |
| X-3 (l. 186) | Dix-sept corps dans l'ordre de GO-46 (l. 733), chacun précédé de son séparateur. **Écart déclaré** : les neuf titres sont retirés, et non les seuls titres qui nomment un modèle. Chaque pièce passe la garde de motifs (n° 38) avant la fusion. Phrase à ajouter : « **La question du lot en quarantaine est servie aux proposeurs sur le mot du directeur (GO-2026-11-22-46) ; le lot lui-même reste fermé.** Elle est servie par son corps seul, titre retiré, avec la réserve « orientée faiblement au test de devinette » (GO-2026-11-22-37) et « orientée au test de devinette, servie avec réserve sur le mot de Lazar » (GO-2026-11-22-46). » |
| K-1 (l. 228), réponse à LQ l. 28 | « Le corps de la pièce du lot pose une question de méthode sur un ensemble tenu à l'écart. Il n'en porte ni le contenu, ni l'identité, ni un candidat de mode : K-1, qui vise les candidats de mode, n'est pas en cause. Le cloisonnement de la matière première tient, puisqu'aucune pièce de cette matière n'entre dans la requête (K-2). » |
| X-4 (l. 187) | L'empreinte vaut celle de la pièce scellée (`39fb4e93…` à cet ordre). |
| X-5 (l. 188) | Une réponse à la pièce du lot n'ouvre aucun accès au lot. Elle va en quarantaine (arrêts n° 17 et 18) ; le séquestre de N-054 reçoit toute réponse qui décrit une façon de dégrader. |
| X-7 (l. 190) | Selon B4 : (A) inchangée ; (B) écart déclaré, lecture unique après la dernière réponse. |
| X-8 (l. 191) | Les comptes se rangent « par pièce », grâce au séparateur ; la question des modes devient « pièce 2, point 6 ». Les proposeurs ajoutés forment une ligne à part. |
| X-9 (l. 192), P1 (l. 126) | La chaîne de GO-35 est lue à la lettre pour les ajouts Claude. Kimi n'a aucun repli. |
| X-10 (l. 193) | P_X = 14 × 6,05 + 2 × max(6,05 ; [PIRE-G-PROPOSEUR-X]), soit **96,80** à 6,05. Sous-parts : Luc 72,60 ; deuxième relais 2 × max(6,05 ; G) ; troisième relais 6,05 ; Kimi 6,05. Ce montant remplace « au moins 54,45 » et la ligne de 55 USD (GO-46 « remplace »). |
| X-11 (l. 194) | Table des clés de la passe X : Anthropic sur Luc (R-4852) ; Google et OpenAI sur leurs relais ; Kimi sur sa clé. Luc est lu comme compte payant à recharge (GO-42, GO-48). Seconde clause du n° 12 : l'écart de B3. Le n° 13 vaut tel quel. |
| G-1 et G-6 (l. 106, l. 111) | Toute requête de passe X des espèces 1 et 5 passe par `garde_google_v3`, avec `mots=None`. |
| G-3 (l. 108) ; § 11 (l. 251-259) | Ajouter [PIRE-G-PROPOSEUR-X] à mesurer, et P_X avec sa table des clés. La valeur de l'enveloppe, 512 octets, est à geler. |
| A1 à A7 (l. 77-83) pour Kimi | Ces exigences valent pour Kimi : aucune relance cachée ; champ du modèle servi comparé au modèle demandé (n° 31) ; une fin « longueur » donne « réponse illisible » ; un refus en prose est classé « refus du modèle » par la session à part ; jeu A7 propre à Kimi. |
| TK l. 31 | La règle selon laquelle le compte Kimi « ne sert à rien d'autre pendant la course » visait l'espèce 6, retirée (DV l. 29). Pour la passe X, toute autre dépense simultanée sur Kimi (pilote de l'essaim, GO-39) est comptée à sa propre ligne et lue au contrôle de ligne. |
| P4 et P15 (l. 129, l. 143) | Inchangés : 6,05 par tentative, jamais baissé. |
| P5, P7, P9, P11 à P14 | Lettre de la v1, inchangée. |
| Q2 (l. 275) | Répondue : GO-43 (55 USD), puis GO-46 (au plus 200). |
| Q9 (l. 277) | Récrite selon B1 et B4 ; les options chiffrées sur Minuit tombent. |
| L-1 (l. 162) | Le « point bloquant » de la v1 tombe : les rôles de la course restent sur Minuit. L-1 renvoie au complément neuf (§ 6). |
| Appariement | Les huit proposeurs reçoivent la même requête. Une réponse servie par repli qui double celle d'un ajout est gardée à part, jamais fusionnée. |

## 6. Ce que le complément de valeurs neuf doit changer

Je ne l'écris pas : la liste seule suit.

1. Le statut de Luc : compte payant à recharge (GO-42, GO-48), au lieu de « aucune recharge supposée » (GO-30).
2. La lecture du n° 11 pour Luc (V9 l. 382) qui en découle.
3. La règle de la part de Luc, R-4289 (CV l. 111-116) : lots de Fable de GO-45 (au moins 117), demandes 28 à 30 à chiffrer, et nœud L-2.
4. Le libellé fixe de Luc dans la pièce de relevés (AC l. 141 : « reste calculé »).
5. La part de Luc : 125,63, ou relevée à 136,04 (AV L-1).
6. La sous-part de passe X sur Luc (72,60), distincte de la part de la course.
7. Le blocage des rôles de Minuit, jusqu'au mot du directeur : juge et proposeur de l'espèce 3 (AC l. 56), lignes à part (CV l. 120-130).
8. La table des clés de la passe X et l'écart B3 au n° 12.

## Réserves

1. GO-48 et R-4852 ne sont pas lus. GO-48 est absent de `go.md` lu ; le registre des décisions est hors de ma liste.
2. Les tarifs de Google et d'OpenAI sont cités, non vérifiés. Le tarif et l'identité des espèces 3 et 4 sont supposés à 10 / 50.
3. Les sorties maximales sont à relever, sauf pour Claude 4.6.
4. Les rapports signes par jeton sont des règles.
5. Les demandes 28 à 30 sur Luc ne sont pas chiffrées.

## Différence avec la v1

| point | v1 | v2 |
|---|---|---|
| B1 | clé de la passe X : « Luc (GO-45) » ; GO-45 et GO-46 pris au mandat | Luc par R-4852, sous GO-46 ; `go.md` réancré (`7cdfb9e8…`, l. 732-733) ; Minuit non appelée, rôles de la course bloqués |
| B2 | charge de Fable absente ; « point bloquant » sur l'espèce 3 de la course | au moins 117 de Fable ; effet chiffré avec et sans compte payant ; le point bloquant tombe ; liste du complément neuf |
| B3 | écart au n° 12 non déclaré | déclaré et accepté (GO-48), avec sa lettre et son épreuve |
| B4 | passe X après la génération 3 | avant la course ou sans elle, d'ici le 30 novembre ; effets sur les n° 11 et 12 ; (B) recommandée |
| contrôles | « sept », en fait cinq, dont un en dur et deux tautologiques | neuf, tous calculés ; la tautologie de la règle Google sortie des contrôles |
| fusion | sans séparateur ; « 6 » ambigu | séparateur « [Pièce k sur 17] » à l'enveloppe ; points désignés « pièce k, point n » |
| titres | présentés comme lettre de X-3 | écart déclaré, dont quatre titres qui ne nomment aucun modèle |
| sorties maximales | Claude 4.6 non relu | 128 000 vérifiés (AN) ; les autres sont un paramètre « à relever » |
| tarifs de Claude 4.6 | non relus | vérifiés (AN l. 7-8) |
| pire Google | calcul seul | [PIRE-G-PROPOSEUR-X] à mesurer sous la garde ; P_X en fonction de cette valeur |
| additif | lieux manquants | G-1, G-3, G-6, § 11, enveloppe, A1 à A7 pour Kimi, TK l. 31, K-1 face à LQ, deux réserves citées |
| GO-43 et GO-45 | — | GO-45 prime pour les mathématiques |
| chiffres | 8,75 ; 44,40 ; entrée au pire 21 082 | 8,76 ; 44,43 ; entrée au pire 21 413 (séparateurs) ; 96,80 inchangé |
