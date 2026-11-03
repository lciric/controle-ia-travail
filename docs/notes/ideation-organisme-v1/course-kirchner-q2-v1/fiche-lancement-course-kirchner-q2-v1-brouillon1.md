# Fiche de lancement — course d'idéation sur la question 2 du mentor Kirchner — brouillon 1

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 10:18 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel n'a été fait pour l'écrire. Le kit
est celui de la course Heimersheim (`outils/course-heimersheim-v1`, version après contre-lecture : pièces v2, garde lexicale v2,
lanceurs Python v2 et shell v3), renommé et adapté à cette question.

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Spécification de conv-audit : `brouillons/ideation-kirchner-q2-v1/specification-kirchner-q2-v1.md` (branche
  `canal/conv-audit-n04`, `934f5dcb0bd442f0c17b2c1aada88041795ab7336e3b03d5fe1bd8bb7c068622`) ; protocole du rapport, gelé avant
  toute sortie : `protocole-rapport-idees-kirchner-v1.md` (`68919ec9a4afcbf8cae764df9cf04834c5c662b0bc62f8c7a515671c97c0a781`) ;
  copies à l'octet dans `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/`.
- Servis : question `question-ideation-kirchner-v1.md` (`291f91f882d9a130570b1da600212f07435ec19cb87b9e9d65380a5c4c650253`),
  quatre sections ; pièce « Kirchner » **v2** `piece-kirchner-v2.md` (`6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5`) ;
  pièce « nos résultats » `piece-nos-resultats-v1.md` (`d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c`).
  La moisson n'est pas servie (seule sa section « déjà pris », qui est dans la question).
- Mots de Lazar, cités tels quels : « go pas de plafond » (chez conv-audit, 09:24 heure de Paris, rapporté par la spécification) ;
  « je veux que Kirchner Q2 passe avant A1-v3 » (mot direct à session-depot, reçu vers 10:00 UTC). La ligne de GO sera
  `GO-2026-11-03-NN`, inscrite par session-depot sur son mot direct.
- Instrument : orchestrateur v56 (copie à l'octet vérifiée), génération de la mini-course (`course2_nuit_v1`, adaptateur
  `course2_nuit_v2`), au-dessus `course_kirchner_v1.py`. Une génération, une passe, **8 fiches par proposeur**.

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-kirchner-q2-v1-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | **lancement**, si Argon n'est utilisé par rien d'autre (jamais deux usages d'Argon à la fois, spécification § 2) |
| `configuration-course-kirchner-q2-v1-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | repli si Argon est pris |
| `configuration-course-kirchner-q2-v1-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue |

Rôles identiques : aiguilleur Opus 5.5 ; juges Opus 5.5 et Astra (unanimité) ; lecteurs Opus 5.5 et Astra ; metteur Fable 5.1 ;
Claude par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Astra 8807, Kimi 8804, Argon 8805 (cinq
espèces seulement) ; le lanceur refuse un port déjà pris. Chaque proposeur est un point de rupture unique (§ 5).

## 3. Déclarations

1. **Aucun témoin planté** dans la course (le noyau v56 n'en porte pas). Les deux « témoins publiés déguisés » du protocole
   (étape B) sont ajoutés après la course par un préparateur neuf, hors de ce kit.
2. **Consignes écrites pour cette question** : juge (K1 sous-estimé, K2 lié à ce que fait Kirchner, K3 première expérience
   faisable en jours, K4 résultat qui ferait changer d'avis énoncé d'avance avec signe et seuil, K5 niveau méthode, aucun
   identifiant inventé, chiffres cités ; tirés des quatre critères gelés du protocole ; le juge voit la question du mentor et la
   section « Ce qui est déjà pris », pas les pièces) ; aiguilleur (au niveau Heimersheim v2 : aucun exemple d'axe ; un protocole
   détaillé et des tricheries plantées décrites par classe et rôle sont `niveau_methode` ; « en cas de doute, concret » gardé,
   « détails opérationnels » restreints à ceux qui serviraient à tromper un moniteur ou une évaluation ou à masquer un
   comportement) ; lecteur (lit les champs de la fiche) ; metteur. Le classement ne se compare pas d'un axe à l'autre.
3. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée :
   46 concepts tirés des seuls textes servis (`pieces/concepts-kirchner-v1.json`). Source du substitut
   (`pieces/source-gu-krenn-kirchner-v1.json`) : 23 œuvres, une par source citée par les textes servis (les travaux réunis sur
   une même ligne de « déjà pris » forment une œuvre), concepts = ceux que les textes attribuent à cette source ; **aucun lien
   que les textes font eux-mêmes** (notes de moisson, rapprochements de la question) ; « rappel du moniteur » n'est porté par
   aucune source (la pièce dit qu'aucun rappel n'est lu) ; « tricheries plantées » par la seule banque réelle ; « sélection par
   classement » par la seule note de Mallen. Codage du rédacteur, non contre-lu. **Bras méta hors course** (annexe propre absente).
4. **Garde lexicale** (mode « prefixe », action « fiche exclue ») : celle de Heimersheim v2 **sans « argon »** :
   `exploratoire`, `fusion`, `bras méta`, `gu et krenn`, `gu krenn`, `bisociation`, `kimi`, `moonshot`, `gemini`, `fable`, `astra`,
   `openai`, `gpt 6`, `gpt6`, `gpt-6`, `chatgpt`. « argon » est retiré parce que la pièce « nos résultats » (§ 3) nomme Argon comme
   proposeur de l'attaque A1 : une fiche qui la cite serait exclue ; conséquence, comme pour « Claude » et « Opus » : une fiche
   d'Argon qui se nommerait passe la garde. « gpt » seul est refusé (GPT-2, GPT-J, GPT-4 passent ; « gpt-6-astra » reste
   attrapé). « exploratoire » et « fusion » attrapent aussi des mots courants (risque accepté). La garde lit la fiche servie puis
   l'entrée complète des juges, de l'aiguilleur et des lecteurs (liste fermée comprise) ; vérifié avant tout appel : aucune
   étiquette dans la question, les deux pièces, les consignes servies, la liste ni les concepts du substitut.
5. **Champs** : `titre`, `probleme`, `sous_estime`, `hypothese`, `axe`, `premiere_experience`, `changer_d_avis`, `test_de_mort`,
   `cout` — ce que la question exige (problème, pourquoi sous-estimé et comment le vérifier, hypothèse, effet prédit avec signe,
   mesure qui tue ; première expérience en jours ; résultat chiffré avec seuil qui ferait changer d'avis). **Axes** : les demandes
   1 à 4 « bienvenues » (`probleme_peu_couvert`, `rappel_apres_selection`, `transfert_hors_banc`, `lien_non_fait`) ; la demande 5
   vaut pour chaque fiche (champs `premiere_experience` et `changer_d_avis`), ce n'est pas un axe.
6. **Consigne du proposeur** : les quatre sections servies de la question, la pièce « Kirchner » v2 entière, la pièce « nos
   résultats » entière, dans cet ordre, à l'octet (vérifié avant tout appel) ; titre, provenance, « Lecture prévue » et « Pièces
   jointes prévues » non servis (la question le dit).
7. **Moissonneur** non appelé ; la moisson n'est pas servie.
8. **Plafond technique S17 = 245 USD** (portée « course », arrêt d'étape 220,5) : garde contre une boucle, sur le mot de Lazar
   « go pas de plafond » (spécification § 3 : « entier supérieur à 1,2 × pire cas du devis ») ; 1,2 × 203,93 = 244,72 (calcul).
   Un seul plafond pour la course (le tour du collisionneur a le sien, hors de ce kit). La ligne de GO porte **un seul montant :
   « 245 USD »**. Relais : Kimi 2 USD (≤ 5), Argon 3 USD (≤ 10), Astra et Claude le reste.

## 4. Devis (`kirchner/devis-course-kirchner-v1.txt`)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| cinq espèces | 317 + 5 | 24,20 USD | 203,93 USD | 0,29 / 0,83 | 0,28 / 1,75 |
| avec Kimi | 260 + 4 | 20,36 USD | 170,92 USD | 0,29 / 0,83 | — |
| sans Kimi | 203 + 3 | 16,51 USD | 138,83 USD | — | — |

Hypothèses : celles du devis Heimersheim (3,48 caractères par jeton, médiane mesurée au second tour ; sorties attendues
supposées ; pire cas = sortie maximale de chaque appel, toutes fiches admises ; prix Fable 10 / 50, Opus 4 / 20, Astra 10 / 50
supposé, Kimi 2 / 10, Argon 10 / 50 supposé) ; la consigne du proposeur est plus longue (30 452 caractères : deux pièces).
Repère : la course Heimersheim réelle a coûté 10,03 USD en 58 min (mot de session-depot) pour 23,61 attendus. Course à blanc :
nombre d'appels identique au plan dans les trois variantes (`kirchner/course-a-blanc-kirchner-v1.txt`).

## 5. Liste d'arrêt

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle ;
débordement de la garde de Kimi proposeur ; dépassement de réserve ; garde cumulée ; garde d'étape ; plafond propre d'un relais ;
plafond de l'étape ; **nœud C13 (A14 : plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec
suffit)** ; signal ; toute autre exception. **Tout arrêt ou nœud après la proposition ne rend ni fiches ni classement** ; restent
lisibles les journaux, manifestes, consommations, coffre et le journal de l'aiguillage ; les réponses brutes ne survivent pas.

## 6. Lecture prévue (spécification § 4 ; protocole Kirchner v1)

Sorties scellées avant lecture, copiées à l'octet sur le canal, sans clé ; rapport par lecteurs neufs au protocole Kirchner v1
(quatre critères gelés, témoins publiés déguisés, comparaisons par paires). **Écart au protocole § 1.2 à noter** : la course ne
rend dans `fiches.json` que les fiches munies d'un passeport ; les fiches `a_corriger`, `concret` ou exclues par la garde sont
comptées mais leur contenu n'est gardé nulle part (le noyau ne le copie jamais, R-575) : elles sont « comptées, non lues »,
comme le protocole le prévoit. Les sorties des juges de la course sont rapportées à part, jamais utilisées pour garder ou
écarter une idée (protocole § 1.2). Lazar écrit seul sa réponse.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau : 34 essais (`kirchner/test_course_kirchner_v1.py`) ; contre-épreuve par neuf mutations, toutes
détectées ; répétition par le vrai lanceur shell derrière de faux amonts : cinq essais conformes
(`kirchner/repetition/resultat-repetition-kirchner-v1.txt`). Non éprouvées : formats réels des interfaces (déjà éprouvés
réellement par la course Heimersheim, même chaîne) ; comportement de l'aiguilleur et de la garde sur des fiches de cette question ;
solde de Moonshot ; ligne de GO réelle.

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
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/EMPREINTES-orchestrateur-course-kirchner-q2-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `17945c647a70448c031111331127658f9090e232d5e74a7da26d107000625925` | vérification de la copie |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/calcul_devis_course_kirchner_v1.py` | `4ae982b0325e9ae0999feb7257fdbba78bb4495b1c0b64ea0dbb1276c0b24c16` | devis |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/commande_claude_kirchner_v1.py` | `5fef9408ca0f2f120226fe9ed28866d44952a485b3f25204fc78ab9fd81cf901` | commande |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v1-avec-kimi.json` | `60a3df3e398a32440084218f2590b4f299935a22d75c78f3ff22cfcc5d4c1868` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v1-cinq-especes.json` | `fa5cacc754462c0f4b0d58a7ad1c3c46b053ee24ad6c6607b58ea1f81690eb3d` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v1-sans-kimi.json` | `ecd4eabe8bebf92f0488d3937b0fd48f39cd63fb5b1a49eec49419c5612d5237` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/construire_consigne_proposeur_kirchner_v1.py` | `d0c4b66770e6ac78edbf3865ea6be7ce921440caaafac994ea3a9eea32e71f8a` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/course-a-blanc-kirchner-v1.txt` | `e637baa687f373863573c366c226b891cb0bf7188b29e8edf018d02595e8fe77` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/course_kirchner_v1.py` | `9a850f0a7e81d48e4013a2eaf9ad23bf5b0c43ff0119b99f265ac2d9b6a30876` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/devis-course-kirchner-v1.json` | `58c8816f8f6094aa7d2080c37b328a0045ad10c4d4040f978154f2d77f1e212b` | devis |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/devis-course-kirchner-v1.txt` | `7e3ca59cc318da84ad90e927088ce64e24e2f84a26dd3c2740066416d474d054` | devis |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/lancer-course-kirchner-v1.sh` | `a4c13b5b05afa45875349a6fa1915f5164d5373e8aa166f86a3e7b5a2fd1e49f` | lanceur |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/lancer_course_kirchner_v1.py` | `affc80f93feb51f681d2c8fafa9a63c8a3ea55234ffeb7c67edbaeae072f7e58` | lanceur |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/concepts-kirchner-v1.json` | `2d78923b2c6b1270ddf92676ed736d12a1fb9dc41f308ba900d0338f93ca7147` | liste fermée |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-aiguilleur-kirchner-v1.md` | `60ca1909d49bbebff1edd1d8f9782304985b8b55b45aa6ffe347502018794584` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-juge-kirchner-v1.md` | `539d712ad4d3c57e3fec4aa1b292a478884ed350222d311a939635325cd187a6` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-lecteur-kirchner-v1.md` | `897a16ea9770f58b78721d08a595a34cf225e2864d0631d3157d07de3fa516f6` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-metteur-kirchner-v1.md` | `9aa2b7e8d3a4444b66948e21aa9ec4f35ec5ac754645373f0b50f084e96f0f2a` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-proposeur-kirchner-v1.md` | `ae7109dc297cae429b280a58061a6f284de689d7b482a1b9e3db9075263e94b0` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/piece-kirchner-v2.md` | `6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/protocole-rapport-idees-kirchner-v1.md` | `68919ec9a4afcbf8cae764df9cf04834c5c662b0bc62f8c7a515671c97c0a781` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/question-ideation-kirchner-v1.md` | `291f91f882d9a130570b1da600212f07435ec19cb87b9e9d65380a5c4c650253` | question servie |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/specification-kirchner-q2-v1.md` | `934f5dcb0bd442f0c17b2c1aada88041795ab7336e3b03d5fe1bd8bb7c068622` | spécification de conv-audit |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/source-gu-krenn-kirchner-v1.json` | `a811be9d00d59b2a38356fec0280d353c0572332b1cf6ad733dfe305b7f25142` | source du substitut Gu-Krenn |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/repetition/repetition_complete_kirchner_v1.sh` | `3dc5364cd745419155e6c1fffc7293fe6ae53cc5a185539e9cdb21feacc7b55f` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/trace_agregee_course_kirchner_v1.py` | `56f0b6940f614a2a3eef85244b826c1089df5448945884b7aef72aeeb3c827d4` | trace agrégée |
| `donnees/course-kirchner-q2-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-kirchner-q2-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-kirchner-q2-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-kirchner-q2-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-kirchner-q2-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |

## 8. Écarts à la spécification de conv-audit (à trancher par conv-audit)

1. Pièce « Kirchner » servie : **v2** (section 1 remplacée par le texte exact de la page Pivotal), alors que la spécification § 1
   nomme `piece-kirchner-v1.md` (sur le mot de session-depot ; le protocole du rapport nomme la v2).
2. Aucun témoin planté dans la course (les témoins du protocole viennent après, étape B).
3. Consignes du juge, de l'aiguilleur, du lecteur et du metteur écrites pour la question (le kit Heimersheim est « à adapter »).
4. Bras méta hors course ; source du substitut écrite pour cette course à partir des seuls textes servis.
5. Garde lexicale « comme Heimersheim » sauf « argon », retiré (nommé par la pièce « nos résultats »).
6. Fiches non admises par l'aiguilleur non gardées (protocole § 1.2 : « comptées, non lues »).
7. Le tour du collisionneur v9 de la spécification n'est pas dans ce kit.
