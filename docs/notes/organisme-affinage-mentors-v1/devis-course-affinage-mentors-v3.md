# Devis de la course d'affinage des idées des mentors par l'organisme d'idéation — v3 (non engagé)

- Écrit le 2026-11-18T06:54:53Z (`date -u`) par la session du compte organisme (modèle I). **Version 3** (R12 ; la v2, `2fb1c3cd…`, et la v1, `54dc947d…`, restent en place). Refait sur le prix d'un appel Claude, comme la v2 l'annonçait (§ 3, D3). **Aucune dépense engagée.** Plafond d'arrêt de la course : **150 USD** (GO-2026-11-18-14, mot de Lazar « oui aux deux », R-3215). Lancement depuis une session qui a la garde de calcul, sur les commandes exactes de `course-v1/commandes-exactes-course-affinage-v1.md`.
- Forme chiffrée : celle du préenregistrement `course-v1/preenregistrement-course-affinage-mentors-v1.md` — seize fils, un appel par fil et par espèce rendant deux cartes, un aiguilleur par carte, deux juges par carte, une seule génération, pas de passe « tableau », pas de fusion, pas de test de mort.

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
