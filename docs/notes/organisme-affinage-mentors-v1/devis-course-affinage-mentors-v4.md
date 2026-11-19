# Devis de la course d'affinage des idées des mentors par l'organisme d'idéation — v4 (non engagé)

- Écrit le 2026-11-18T07:09:15Z (`date -u`) par la session du compte organisme (modèle I). **Version 4** (R12 ; la v3, `6aa86555…`, la v2, `2fb1c3cd…`, et la v1, `54dc947d…`, restent en place). Mêmes prix, mêmes hypothèses et mêmes totaux que la v3 ; ajout : **répartition par clé** (§ 6), sur la consigne de la mère R-3228. **Aucune dépense engagée.** Plafond d'arrêt de la course : **150 USD** (GO-2026-11-18-14, mot de Lazar « oui aux deux », R-3215). Lancement depuis une session qui a la garde de calcul, sur les commandes exactes de `course-v2/commandes-exactes-course-affinage-v2.md`.
- Forme chiffrée : celle du préenregistrement `course-v2/preenregistrement-course-affinage-mentors-v2.md` — seize fils, un appel par fil et par espèce rendant deux cartes, un aiguilleur par carte, deux juges par carte, une seule génération, pas de passe « tableau », pas de fusion, pas de test de mort.

## 1. Prix relevés, avec leur source

| poste | prix retenu | source (fichier lu, empreinte) | statut |
|---|---|---|---|
| première espèce Claude (proposeur, aiguilleur, juge) | 4,00 USD par million de jetons d'entrée ; 20,00 en sortie | barème `BAREME_USD_PAR_MILLION` du relais de clé de l'orchestrateur, `/home/user/ideation-organism/orchestrator/pole/relais_reel_v2.py` l. 62-70 (sha256 `98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7`, commit `a41b7b5`), « barème officiel […] lu le 27 octobre 2026 » ; même barème dans `pole/relais_reel.py` l. 49-54 | prix d'un barème écrit dans le code, lu par une autre session sur la page officielle ; non revérifié ici (aucun réseau) |
| seconde espèce Claude (proposeur) | 10,00 et 50,00 | même ligne du même barème | idem |
| Argon (proposeur, juge) | 8,3 USD par million d'entrée ; 41,5 en sortie | enveloppe `rapports/fille-ideation-1-v1/appel-argon-v5.sh` (`37c0205e…`), réglages figés après `"$@"` ; commande `commande_argon_v3d.py` l. 345-346 : entrée « borne lue par Lazar (R-718) », sortie « SUPPOSÉ » | sortie supposée |
| proposeur hors Claude (Argon, Kimi, Astra, Carbon), par appel | 0,276 USD (moyenne) ; 0,400484 (pire appel) | course réelle v67, `resultats/course-v67/poste-local-v1/boucle-reelle-v66.json` (`21bc75f4…`), relevé par le devis v2 (§ 1) | mesuré pour Argon et Kimi, à environ six cartes par appel ; **supposé** pour Astra et Carbon (prix à relever) |
| appel court d'Argon (juge) | 0,0347 USD (moyenne) ; 0,04326 (pire) | même course v67, `appels_etage` (devis v2, § 1) | mesuré sur un lecteur ; supposé pour un juge |

Les coûts réels des courses v5 à v7 des organismes discrets (R-3100 à R-3102) n'en donnent aucun : v5 et v6 ont échoué au code 2 avant tout appel, v7 a tourné sans aucun modèle Claude (proposeurs et juges internes factices) et a fini au code 4 (« témoins échoués chez un juge », classement marqué illisible) ; ses manifestes ne portent aucun coût.

## 2. Hypothèses de jetons (déclarées, non mesurées)

Quatre caractères par jeton (convention du code de l'orchestrateur). Consigne du proposeur : environ 3 800 caractères ; texte d'un fil : 300 à 6 000 caractères ; une carte : 9 000 caractères au plus (consigne).

| appel | entrée (estimation ; haut) | sortie (estimation ; haut) | première espèce Claude | seconde espèce Claude |
|---|---|---|---|---|
| proposeur (deux cartes) | 5 250 ; 20 000 jetons | 6 000 ; 16 000 | 0,141 ; 0,400 USD | 0,3525 ; 1,000 USD |
| aiguilleur (une carte) | 6 250 ; 23 000 | 300 ; 2 000 | 0,031 ; 0,132 | — |
| juge (une carte) | 6 250 ; 23 000 | 600 ; 3 000 | 0,037 ; 0,152 | — |

Le haut de l'entrée compte un préambule inconnu du kit d'agent (jusqu'à environ 15 000 jetons) ; il n'a pas été mesuré.

## 3. Devis, sans et avec Carbon

Sans Carbon : cinq espèces de proposeurs (deux Claude, Argon, Kimi, Astra), 80 appels de proposeur, 160 cartes, 160 aiguillages, 320 jugements (560 appels). Avec Carbon : six espèces, 96 appels, 192 cartes, 192 aiguillages, 384 jugements (672 appels).

| poste | sans Carbon : estimation | sans Carbon : haut | avec Carbon : estimation | avec Carbon : haut |
|---|---|---|---|---|
| proposeurs | 21,14 | 41,62 | 25,56 | 48,03 |
| aiguilleur (première espèce Claude) | 4,96 | 21,12 | 5,95 | 25,34 |
| juges (première espèce Claude et Argon) | 11,47 | 31,24 | 13,77 | 37,49 |
| **sous-total** | **37,58** | **93,98** | **45,28** | **110,87** |
| marge de 10 % (appels refaits, écarts de jetons) | 3,76 | 9,40 | 4,53 | 11,09 |
| **total** | **41,33** | **103,38** | **49,81** | **121,95** |

- **Borne par les plafonds de session** (chaque appel est arrêté à son plafond : proposeur 1,50 ; aiguilleur 0,25 ; juge 0,60 USD) : 352,00 USD sans Carbon, 422,40 avec. Elle dépasse le plafond d'arrêt : **la seule borne dure est le plafond d'arrêt de 150 USD**, tenu par l'orchestrateur (règle d'A1, plafond dur fixé au lancement de chaque étape et transmis à chaque relais) et vérifié par le lanceur avant et après.
- **Majoration de 25 %** (proposition du devis v2, § 4) : estimation × 1,25 = 51,66 (sans) et 62,26 (avec) ; haut × 1,25 = 129,23 (sans) et **152,44 (avec)**. Avec Carbon, le haut majoré dépasse 150 : si la course atteint ce régime, le plafond d'arrêt coupe une étape (« non mesuré (budget) ») et la course s'arrête proprement, en écrivant ce qui a été fait. Lazar a retenu 150 (R-3215) ; rien n'est changé ici.
- Plan de dépense de l'orchestrateur (configuration fixe) : attendu 25 / 6 / 14 USD et plafonds de relais 60 / 30 / 50 USD pour la proposition, l'aiguillage et les juges (somme 140 ≤ 150) ; passe « tableau » et fusions retirées par construction (plafond de relais 151 > 150).

## 4. Règle des clés (GO-2026-11-18-13, R-3209 point 2)

- Avant la course : le lanceur lit le relevé du crédit de chaque clé employée (fichier du jour, écrit par la session d'exécution depuis l'interface de facturation ou le compteur ; aucune valeur de clé). « Non lisible » arrête le départ, sauf dispense écrite de la mère. Un reste sous un cinquième du crédit **ou sous 150 USD** écrit une alerte pour la mère et arrête le départ : comme la course ne peut pas dépenser plus de 150 USD, une clé qui a au moins 150 USD ne peut pas atteindre zéro pendant la course.
- Après la course : coût réel par relais (consommations de l'orchestrateur), écart au devis par rôle, reste estimé par clé, alerte si un reste estimé passe sous les mêmes seuils ; relevé de confirmation par l'interface de facturation, à faire par la session d'exécution.

## 5. Préalables (rappel du devis v2 et de la décision)

- Inscription par la mère des montants absents du registre des dépenses (relevé d'ensemble § 3.4, environ 41,82 USD), avant toute nouvelle dépense de l'organisme sur cette matière (texte de décision, section 2).
- Contre-lecture scellée du préenregistrement et du lanceur, au verdict « Scellable » sans réserve (le lanceur la vérifie).
- Pour Carbon : relais et nom de clé nommés dans la déclaration des relais (l'inscription est faite : R-3217, GO-2026-11-18-15) ; sinon la course part sans Carbon, au devis « sans Carbon ».

## 6. Répartition par clé (v4, R-3228)

- **Tous les appels Claude** (les deux espèces Claude de proposeurs, l'aiguilleur, le premier juge) passent par un seul relais, tenu sur la clé **`RR_ANTHROPIC_API_KEY_MINUIT`** (crédit déclaré par Lazar : 200 USD, R-3228). La clé `RR_ANTHROPIC_API_KEY_RIGAUD` (124 USD, R-3224) **n'est pas employée** par cette course ; le lanceur refuse tout relais configuré sur elle, et toute autre clé de la famille Claude.
- Part Claude du devis : **sans Carbon** 18,78 USD estimé (20,65 avec la marge de 10 %), 67,84 haut (74,62) ; **avec Carbon** 20,95 estimé (23,05), 76,93 haut (84,62). Détail : proposeurs Claude 7,90 estimé et 22,40 haut ; aiguilleur 4,96 / 21,12 (sans) ou 5,95 / 25,34 (avec) ; premier juge 5,92 / 24,32 (sans) ou 7,10 / 29,18 (avec).
- Borne dure de la clé Minuit : le plafond d'arrêt, 150 USD, que le relais Claude tient aussi (`--plafond-usd 150`). Reste minimal après la course : 200 − 150 = 50 USD, au-dessus du cinquième (40 USD) : la clé ne peut pas atteindre zéro. Si la course dépense plus de 50 USD sur Minuit, le reste passe sous 150 USD : alerte « après » pour la mère, qui prévient Lazar avant toute course suivante sur cette clé.
- **Autres clés** (Argon, Kimi, Astra, Carbon) : nommées par la session d'exécution dans la déclaration des relais ; même règle (reste au moins égal à un cinquième du crédit et à 150 USD, sinon arrêt au départ). Soldes connus au registre : Moonshot 32,25 USD (R-3224, sous 150 : une course avec Kimi s'arrêterait au départ) ; Google et OpenAI illisibles (R-3222 : départ seulement avec une dispense écrite de la mère pour ces clés).
- Relevé avant et après : par l'interface de facturation si elle le rend ; sinon, pour Minuit, **compte au prix relevé** — crédit déclaré 200 USD moins la dépense antérieure déclarée, puis moins la dépense comptée par l'orchestrateur au barème du relais (§ 1).
