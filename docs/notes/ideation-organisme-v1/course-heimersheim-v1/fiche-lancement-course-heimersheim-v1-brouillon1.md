# Fiche de lancement — course d'idéation sur la question 1 du mentor Heimersheim — brouillon 1

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 07:50 UTC (`date -u`). **Brouillon non scellé** : session-depot
la fait contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du
rapport à la ligne « Contre-lecture » ci-dessous. Le lanceur v1 exige ce texte scellé, sans marqueur de remplissage, citant
l'empreinte de sa contre-lecture, et dont la table « Pièces gelées » couvre ce qu'il nomme (configuration, consignes,
question, pièce, commandes, relais, lanceurs, garde du dépôt). Aucune dépense, aucun appel réel n'a été fait pour l'écrire.

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course

- **Course NON décisive** : démonstration de l'organisme d'idéation et matière à réflexion pour Lazar ; aucune porte, aucune
  revendication, aucun chiffre opposable n'en sort (R7 : rien n'entre dans la candidature sans vérification en source).
- Spécification de conv-audit (session d'audit), scellée : `brouillons/ideation-heimersheim-v1/specification-course-ideation-heimersheim-v1.md`
  (branche `canal/conv-audit-n04`, `0e2fd5bcdbb644fda55b7ccccb5be4b397e7a1e6d93d3ae7b4c721beaa1e40de`), copie à l'octet dans le kit :
  `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/`.
- Question servie : `question-ideation-heimersheim-v1.md` (`e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007`) ;
  pièce servie : `piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` (`6445fd6f9dae33500b628bdeff354ed2c7b75bd50d05cbd2aef08c3e6ce49162`) ;
  mêmes chemins, mêmes empreintes, copies du kit.
- Instrument : orchestrateur v56 du second tour réel (copie à l'octet vérifiée, `VERIFICATION-COPIE-orchestrateur-v56-v1.txt`),
  génération de la mini-course (`course2_nuit_v1`, adaptateur `course2_nuit_v2`), au-dessus `course_heimersheim_v1.py`
  (contrôles propres, manifeste). Une génération, une passe, **8 fiches par proposeur**, pas de passe « tableau ».
- Lazar : GO direct « sans plafond » pour cette course (mot rapporté par la spécification) ; l'identifiant de la ligne de GO
  (`GO-2026-11-03-NN`) sera inscrit par session-depot après le devis.

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-heimersheim-v1-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | **lancement** si Argon est libre au lancement (A1-v3 arrêtée, mot de session-depot 07:25 UTC) |
| `configuration-course-heimersheim-v1-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | repli si Argon n'est pas libre (Moonshot rechargé, mot de session-depot 07:18 UTC) |
| `configuration-course-heimersheim-v1-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue (HTTP 429 faute de solde, par exemple) |

Rôles identiques dans les trois : aiguilleur Opus 5.5 ; juges Opus 5.5 et Astra (agrégation « unanimité », comme le second
tour) ; lecteurs d'étiquettes Opus 5.5 et Astra ; metteur en combinaison Fable 5.1. Claude : un seul relais 8806 (Fable 5.1
et Opus 5.5 permis), `--effort high --reflexion adaptative` pour tous les rôles, identiques au relais et à la commande (refus
409 sinon) ; aucune bascule de modèle (pas de `fallbacks`). Astra : relais 8807. Kimi : relais 8804 (`relais_kimi_v3.py`).
Argon : relais 8805 (`commande_argon_v56_nuit_v2.py servir`), seulement dans la variante cinq espèces ; le lanceur refuse un
port déjà pris (jamais toucher au relais d'une autre course).

## 3. Déclarations

1. **Aucun témoin planté** : la course v56 n'en porte pas et le second tour réel n'en avait aucun (constat de session-depot) ;
   aucun code de témoins n'est ajouté. Écart à la spécification § 1 (« témoins plantés : ceux du second tour réel ») : il n'y
   en a pas à réutiliser ; les juges ne sont donc lus par aucun témoin ici.
2. **Écart du juge** (à trancher par conv-audit) : la spécification dit « consigne figée inchangée » ; celle de la mini-course
   juge des statistiques de détection et ne peut pas servir. La consigne du juge est réécrite pour cette question, même
   mécanique (une fiche, items vrai/faux K1 à K5, note de 0 à 10, même bloc JSON) : K1 prédiction chiffrée avec signe ;
   K2 mesure qui tue ; K3 épreuve testable sur Llama-3.1-8B-Instruct en quelques jours, coût chiffré ; K4 distingue « croyance
   retirée / registre déplacé » ou « effet spécifique / effet générique de même norme », ou apporte une raison d'échec absente
   des quatre déjà écrites ; K5 niveau méthode, nouveauté posée comme question, chiffres repris cités. Le juge voit la question
   du mentor (texte exact) et la liste des quatre raisons déjà écrites, pas la pièce entière (déclaré). Aiguilleur, lecteur et
   metteur sont réécrits de même pour cette question.
3. **Bras réellement joués** : `gu_krenn` en mode « substitut » (seul permis en v56) et `basique`, quatre paires par bras
   (k = 4 : au moins trois mariages par bras, une paire de marge pour une fusion inachevée ; vingt-quatre à quarante fiches
   donnent de 276 à 780 paires possibles, calcul). **Première exécution réelle des deux bras** sur une question de recherche.
   - Source du substitut : `pieces/source-gu-krenn-heimersheim-v1.json`, **version minimale écrite pour cette course** (déclarée) :
     une œuvre par source citée par la pièce servie (11), ses concepts = ceux que la pièce lui attribue, pris dans la liste fermée ;
     « jamais reliées » = jamais attribuées ensemble par la pièce ; codage du rédacteur, non contre-lu (à trancher par conv-audit) ;
     dates en bornes déclarées, sans effet sur les notes avec les fenêtres retenues.
   - Bras basique : exposant 8,5 et décalage 0,05 (ceux de la mini-course) ; liste fermée `pieces/concepts-heimersheim-v1.json`
     (37 concepts tirés de la question et de la pièce) ; axes = les cinq demandes « particulièrement bienvenues » de la question.
   - **Bras méta hors course** : il exige une annexe scellée propre à la question (grille des niches, tables de communication
     et d'éloignement, structures, bande, jeu de non-vacuité), un brouillon relu et un rapport de contre-lecture dont les deux
     empreintes sont citées, et une approbation de Lazar `R-NNN` ; l'annexe existante (`annexe-bras-meta-v1-brouillon6.md`)
     porte sur la question de la course 2 et ses champs de contre-lecture et d'approbation portent encore le marqueur de remplissage. Écrire ces
     valeurs serait inventer du contenu scientifique et une approbation. Ce qu'il faudrait : une annexe Heimersheim (niches tirées
     des objets de la pièce, tables justifiées), sa contre-lecture par un lecteur neuf, le mot de Lazar, puis une configuration v2.
4. **Garde lexicale** (mode « prefixe », action « fiche exclue », comme la mini-course) : la garde lit la fiche servie puis
   l'entrée complète (consigne comprise) de chaque juge, de l'aiguilleur et des lecteurs, et les fiches servies au metteur ;
   la consigne du proposeur n'y passe pas. Liste : celle de la mini-course **moins « témoin »** (écart déclaré : la pièce servie
   l'emploie quatre fois et il n'y a aucun témoin planté à cacher ; le garder exclurait presque toute fiche), plus « fable »,
   « astra », « openai », « gpt », « chatgpt ». « claude », « opus », « anthropic » et « sonnet » ne sont pas ajoutés (la pièce
   cite Claude Sonnet 4.5, Opus 4.6 et Anthropic). Vérifié par programme avant tout appel : aucune étiquette de la liste
   n'apparaît dans la question, la pièce, les consignes servies, la liste fermée ni le vocabulaire du substitut.
5. **Champs des fiches** : `titre`, `hypothese`, `axe`, `epreuve`, `controle`, `prediction`, `test_de_mort`, `cout` — ce que
   la question exige de chaque fiche (hypothèse, effet prédit, mesure qui la tue), l'épreuve et le contrôle (effet spécifique
   contre effet générique) qu'elle demande de distinguer, et le coût « en quelques jours » ; `temoin` est un nom réservé par le
   noyau v56, d'où `controle`. Axes : `raison_echec_absente`, `evaluation_contre_registre`, `residu_non_verbalise`,
   `lien_objets_non_relies`, `prediction_chiffree_8b`.
6. **Consigne du proposeur** : elle enchâsse à l'octet les sections « La question… », « Ce qu'on attend des proposeurs » et
   « Règles d'intégrité » de la question, puis la pièce entière ; le titre et le paragraphe de provenance de la question et sa
   section « Lecture prévue de la sortie » ne sont pas servis (déclaré). Vérifié par programme avant tout appel.
7. **Moissonneur** non appelé (nouveauté non cherchée).
8. **Plafond technique** S17 = **244 USD** (portée « course », arrêt d'étape 219,6) : garde contre une boucle, **pas** un
   plafond de Lazar ; règle : l'entier supérieur à 1,2 fois le plus grand pire cas des trois variantes (203,15 USD, cinq espèces).
   La ligne de GO doit porter **un seul montant, « 244 USD »** (le lanceur la relit par la garde du dépôt puis par
   `verifier_go_v56`). Relais : Kimi 2 USD (≤ 5), Argon 3 USD (≤ 10), Astra et Claude le reste (somme = S17).

## 4. Devis (calcul : `heimersheim/devis-course-heimersheim-v1.txt`)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| cinq espèces | 317 + 5 | 23,61 USD | 203,15 USD | 0,28 / 0,76 | 0,23 / 1,69 |
| avec Kimi | 260 + 4 | 19,89 USD | 170,28 USD | 0,28 / 0,76 | — |
| sans Kimi | 203 + 3 | 16,12 USD | 138,35 USD | — | — |

Hypothèses : jetons d'entrée attendus = caractères / 3,48 (médiane mesurée sur Argon au second tour réel) ; sorties attendues
supposées (proposeur 12 000, juge 2 000, lecteur et aiguilleur 1 500, metteur 6 000 ; Kimi et Argon proposeurs : mesure du
second tour × 8 / 6) ; pire cas = sortie maximale de chaque appel (64 000 / 16 000 Claude, 32 000 / 16 000 Astra, 65 536 / 16 000
Kimi, 32 000 / 4 000 Argon) et toutes les fiches admises. Prix : Fable 10 / 50, Opus 4 / 20, Astra 10 / 50 (SUPPOSÉ haut), Kimi
2 / 10, Argon 10 / 50 (SUPPOSÉ). Course à blanc (moteur simulé) : nombre d'appels identique au plan, étape par étape et
modèle par modèle, dans les trois variantes (`heimersheim/course-a-blanc-heimersheim-v1.txt`).

## 5. Liste d'arrêt (codée, avant ou pendant la course)

Modèle servi différent du modèle demandé ; trois échecs consécutifs d'un rôle ; débordement de la garde de Kimi proposeur ;
dépassement de réserve ; garde cumulée ; garde d'étape des commandes ; plafond propre d'un relais (HTTP 402 ou 429) ; plafond
de l'étape atteint (noyau) ; signal reçu ; toute autre exception ; avant la course : un contrôle d'avant course en échec.

## 6. Lecture prévue (§ 4 de la spécification)

Lazar lit les fiches et les mariages comme matière à sa réflexion ; la réponse au mentor doit être écrite par lui et ne pas
suivre de près un texte écrit par une machine ; l'usage le plus sûr est la partie « expériences et épreuves » et la mise à
l'épreuve de ses trois raisons. Un lecteur neuf de conv-audit relit la sortie scellée : redites avec la pièce, fiches hors
niveau méthode, chiffres inventés (toute fiche qui cite un chiffre absent de la pièce est marquée). Classement des juges
rapporté avec sa réserve (au second tour : plafond, κ = 0) ; ici aucun témoin pour lire les juges. Sortie : dossier neuf hors
du clone, manifeste de départ scellé avant le premier appel, sortie scellée avant toute lecture.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau (essais : `heimersheim/test_course_heimersheim_v1.py`, 30 ; contre-épreuve par neuf mutations ;
répétition par le vrai lanceur derrière de faux amonts, cinq essais) : voir le LISEZMOI. **Non éprouvées** : le format réel
des réponses d'Anthropic, d'OpenAI (gpt-6-astra), de Moonshot et de Google (le faux mandataire imite leur format supposé) ;
les vrais jetons et la vraie durée des appels à effort « high » ; le comportement réel de la garde lexicale et de l'aiguilleur
sur de vraies fiches ; la tenue de l'appel de contrôle de Fable 5.1 et d'Astra sous 0,05 USD (≈ 1 000 jetons de sortie : une
réflexion plus longue ferait échouer le contrôle, donc aucune course, sans autre dépense) ; le solde réel de Moonshot.

### Pièces gelées

| pièce (chemin depuis la racine du dépôt) | sha256 | rôle |
|---|---|---|
| `.claude/hooks/garde_calcul.py` | `84512d4a1bef0403668000942cf5f5d383aab280bf5a58f6aec328e77f807d59` | garde du dépôt |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/collisionneur_v8.py` | `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` | relais (appel de l'interface) |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_astra_a1bis_v1.py` | `6e9e48e0fc0a0528183a26d019d69d51f9bb9b8c1791c6ae487b59a4466a1815` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_claude_a1bis_v1.py` | `7da79a5c34449dd7629aa3d1721c76058a34b56b43f2bd46c9dbfc94e20ef2c5` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_pole_v56_commun_v1.py` | `1f56e466f5e80f82a25ccccbb5784fa0fa6dc34046dc99d887ec87f713c7eaed` | commande |
| `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bce54f5c89e9f078d1a03b5d8159894d6565ae560c3601c1e63ca76239` | relais |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/EMPREINTES-orchestrateur-course-heimersheim-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `aff5d875743177ac03d6a6fb5bdb0785d557d31f68b6602560a9a411672ff86c` | vérification de la copie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/calcul_devis_course_heimersheim_v1.py` | `b76fee86a2b3bec92855ea1c53ee3a8d8e02b9e8c9951aef15a46d8a3d6cbfc4` | devis |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/commande_claude_heimersheim_v1.py` | `393b79c09b46348b4767ed72cab150b9af63680ab4ea8fb68f2c67df727999a6` | commande |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v1-avec-kimi.json` | `1bf96855a0e359f795258806ac6a6e1e450d307bd2bead91342df554a1182287` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v1-cinq-especes.json` | `e9e83bdfa6f7a386a8590d78821bd5536f51779c7621069554eed87f93d04eca` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v1-sans-kimi.json` | `9847451289dd3dab2f0465b301cd6cc5cb300cd8e4384b619df726fc0d84dd22` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/construire_consigne_proposeur_heimersheim_v1.py` | `74fbd1201516d812d7329035bf2b31665b04c77811663cda7bd01474b36586a0` | pièce |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/course_heimersheim_v1.py` | `a1b8a8baf32ff2dfeb4faf748fc77e18c7ac625ef17c8dad9ab119e2d79f5c41` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/devis-course-heimersheim-v1.json` | `a483556de0f56205f7df0d6e266cb8294746b4a089115e4f1af625f4132470c2` | devis |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/devis-course-heimersheim-v1.txt` | `6298856c84b30c5140dd530ce366672b1998790d8ad0ffb0a2dfc505e281cca2` | devis |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/lancer-course-heimersheim-v1.sh` | `4a143dd9a20d92553f36d2316c19e919ff3ef564d869525f6a9ae5c4430d09d4` | lanceur |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/lancer_course_heimersheim_v1.py` | `6601fc378edc3e3b56d57511e10ac3ca41fbe3d24dc58289eaf982268237ded6` | lanceur |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/concepts-heimersheim-v1.json` | `1a80a32b284c8fa476df12337b8e0986efebd31b0b812df4d201f7c590713734` | liste fermée |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-aiguilleur-heimersheim-v1.md` | `28c765b1dbcf0826a202221176927472d8a13355a117bb21ab7af0d29ecfc361` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-juge-heimersheim-v1.md` | `3ecae1dcffad00c54f973cff6edf8e22383b01405b3a3c54089778dc94dfed17` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-lecteur-heimersheim-v1.md` | `4879ed96d0cd3cdcea98c0f6e3ea07ea6c3f2da0cbc3f04cf90123f5770d9322` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-metteur-heimersheim-v1.md` | `0135b2fef863edbd0263ce76cd8d5f7e424c9930cf55a86999900899a3bb62f6` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-proposeur-heimersheim-v1.md` | `5eb778ebbcf6975dcc05a929238cbe04258d941f171bfe944240838a118a8ffa` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` | `6445fd6f9dae33500b628bdeff354ed2c7b75bd50d05cbd2aef08c3e6ce49162` | pièce servie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/question-ideation-heimersheim-v1.md` | `e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007` | question servie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/specification-course-ideation-heimersheim-v1.md` | `0e2fd5bcdbb644fda55b7ccccb5be4b397e7a1e6d93d3ae7b4c721beaa1e40de` | spécification de conv-audit |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/source-gu-krenn-heimersheim-v1.json` | `3d00c1955f96e0eca422ac80ccdbf431e0356dfa666b50bad930c4fcdded34a1` | source du substitut Gu-Krenn |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/trace_agregee_course_heimersheim_v1.py` | `3af62dd8415619b1d092464c248dbcc52a33c4502cf272f46f70d28c55b5a3ee` | trace agrégée |
| `donnees/course-heimersheim-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-heimersheim-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-heimersheim-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-heimersheim-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-heimersheim-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |

## 8. Écarts à la spécification de conv-audit (à trancher par conv-audit)

1. Aucun témoin planté (§ 1 : « ceux du second tour réel ») : il n'y en avait pas.
2. Consigne du juge réécrite pour la question (§ 1 : « consigne figée inchangée ») ; aiguilleur, lecteur, metteur aussi.
3. Bras méta hors course (§ 1 : « trois bras ») : annexe propre à la question, contre-lecture et approbation absentes.
4. Source du substitut Gu-Krenn écrite pour cette course à partir de la seule pièce servie (version minimale déclarée).
5. « témoin » retiré de la garde lexicale (§ 1 : « garde lexicale inchangée »).
6. Question servie par trois sections (titre, provenance et « Lecture prévue » non servis).
7. Plafond technique 244 USD au lieu de 60 (§ 2 : « à relever sur son mot si le devis le dépasse ») : le pire cas le dépasse.
8. Copie au canal (fiches, mariages, classement, coûts) et rapport : à la charge de session-depot après la course ; la
   « lecture des témoins » est sans objet.
