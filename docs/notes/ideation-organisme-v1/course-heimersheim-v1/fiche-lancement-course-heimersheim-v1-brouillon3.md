# Fiche de lancement — course d'idéation sur la question 1 du mentor Heimersheim — brouillon 3

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 08:23 UTC (`date -u`). Brouillon 3 = brouillon 2 (gardé, R12)
corrigé après sa contre-lecture (`docs/notes/ideation-organisme-v1/course-heimersheim-v1/contre-lecture-fiche-lancement-course-heimersheim-v1.md`,
`18e7c5011a175305fd7975437679c0730b9f024f641a3fedad03d006ad73db17`, « scellable après corrections », aucun bloquant) : pièces v2
(aiguilleur, lecteur, source du substitut), garde lexicale v2, configurations v2, lanceur Python v2, lanceur shell v3, table des
pièces gelées v3 ; traitement constat par constat en § 9. **Brouillon** : session-depot le fait contre-lire au besoin puis en
écrit la version scellée sous un nom neuf, qui cite l'empreinte du rapport à la ligne ci-dessous. Le lanceur (v1, v2 comme v3)
exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et dont la table « Pièces
gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel n'a été fait pour l'écrire.

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Nature de la course

- **Course NON décisive** : démonstration de l'organisme d'idéation et matière à réflexion pour Lazar ; aucune porte, aucune
  revendication, aucun chiffre opposable n'en sort (R7 : rien n'entre dans la candidature sans vérification en source).
- Spécification de conv-audit, scellée : `brouillons/ideation-heimersheim-v1/specification-course-ideation-heimersheim-v1.md`
  (branche `canal/conv-audit-n04`, `0e2fd5bcdbb644fda55b7ccccb5be4b397e7a1e6d93d3ae7b4c721beaa1e40de`), copie à l'octet :
  `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/`.
- Question servie : `question-ideation-heimersheim-v1.md` (`e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007`) ;
  pièce servie : `piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` (`6445fd6f9dae33500b628bdeff354ed2c7b75bd50d05cbd2aef08c3e6ce49162`).
- Instrument : orchestrateur v56 du second tour réel (copie à l'octet vérifiée), génération de la mini-course (`course2_nuit_v1`,
  adaptateur `course2_nuit_v2`), au-dessus `course_heimersheim_v2.py`. Une génération, une passe, **8 fiches par proposeur**.
- Mots de Lazar, cités tels quels : « **pas de plafond** » (chez conv-audit, 07:45 heure de Paris, rapporté par la
  spécification) ; « go lance heimersheim dès que le devis est prêt » (rapporté par session-depot). « Sans plafond » est le mot
  de session-depot. Le chiffre du plafond technique (244 USD, § 3.8) a été dit à Lazar à ≈ 08:00 UTC (session-depot).

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-heimersheim-v2-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | si Argon est libre au lancement (A1-v3 arrêtée : mot de session-depot, 07:25 UTC ; le rapport de la fille que la spécification demande n'est pas cité ici, chemin et empreinte à ajouter par session-depot) |
| `configuration-course-heimersheim-v2-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | repli si Argon n'est pas libre (Moonshot rechargé, mot de session-depot, 07:18 UTC) |
| `configuration-course-heimersheim-v2-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue |

Chaque proposeur est un point de rupture unique (§ 5) : la variante à cinq espèces en a cinq, dont deux interfaces au format non
éprouvé ici (Moonshot, Google) ; le choix reste à session-depot et Lazar. Rôles identiques dans les trois : aiguilleur Opus 5.5 ;
juges Opus 5.5 et Astra (unanimité) ; lecteurs Opus 5.5 et Astra ; metteur Fable 5.1. Claude : un seul relais 8806 (Fable 5.1 et
Opus 5.5), `--effort high --reflexion adaptative` pour tous les rôles, aucune bascule de modèle. Astra 8807, Kimi 8804, Argon 8805
(cinq espèces seulement) ; le lanceur refuse un port déjà pris. Lanceur : `heimersheim/lancer-course-heimersheim-v3.sh`.

## 3. Déclarations

1. **Aucun témoin planté** : la course v56 n'en porte pas et le second tour réel n'en avait aucun ; les juges ne sont lus par
   aucun témoin ici.
2. **Consignes réécrites pour la question** (écart à « consigne figée inchangée », à trancher par conv-audit) : juge (K1 à K5,
   note 0 à 10), aiguilleur (**v2**), lecteur (**v2**), metteur. K1 et K3 demandent à toute fiche une prédiction chiffrée et
   une épreuve sur Llama-3.1-8B, ce que la question ne demande qu'en 5 : **ne pas comparer le classement d'un axe à l'autre**
   (biais de forme, CLH-06). Le juge voit la question du mentor et les quatre raisons déjà écrites, pas la pièce entière.
   Aiguilleur v2 (CLH-02) : l'exemple « un axe qui ne correspond pas à son contenu » est retiré de `a_corriger` (les axes se
   recoupent par construction : un axe discutable n'est pas un défaut) ; un protocole d'expérience détaillé (modèle, couches,
   doses, lectures, nombre de tirages) est dit `niveau_methode` ; « en cas de doute, concret » est gardé, mais « détails
   opérationnels » ne vise plus que ceux qui serviraient à tromper une évaluation ou à masquer un comportement. Lecteur v2
   (CLH-11) : il lit les champs `hypothese`, `epreuve`, `controle`, `prediction`, `test_de_mort`.
3. **Bras réellement joués** : `gu_krenn` (substitut) et `basique`, quatre paires par bras ; **première exécution réelle**.
   - Source du substitut **v2** (`pieces/source-gu-krenn-heimersheim-v2.json`, CLH-05) : le lien « incohérence hors variété »
     attribué à la réplication GLM-5 est retiré (la pièce, A3, ne dit que « incohérent au-delà de 0,025 » ; « hors variété » est
     l'explication de Wurgaft, B9). Choix de codage déclarés (CLH-10) : « fenêtre de dose » attribuée à Heimersheim et Mendel
     seuls (B7 parle des trois sources ensemble : « fenêtre de dose » × « exposant p » reste donc « jamais reliée ») ;
     « réinférence de la croyance à chaque jeton » attribuée à Hua seul (B10 la relie aussi, de sa propre voix, aux plateaux) ;
     « marqueur de registre » chez Hua est la lecture de la pièce (B5) ; la règle « une œuvre par source » ne code **aucun** lien
     posé par la pièce elle-même (B10, C). Codage du rédacteur, contre-lu une fois (CLH-05, CLH-10).
   - Bras basique : exposant 8,5, décalage 0,05 ; liste fermée de 37 concepts ; axes = les cinq demandes de la question.
   - **Bras méta hors course** : annexe propre à la question, contre-lecture et approbation `R-NNN` absentes (brouillon 1 § 3.3).
4. **Garde lexicale v2** (mode « prefixe », action « fiche exclue ») : elle lit la fiche servie puis l'entrée complète de chaque
   juge, de l'aiguilleur et des lecteurs (consigne **et liste fermée** comprises), et les fiches servies au metteur ; la consigne
   du proposeur n'y passe pas. Liste : `exploratoire`, `fusion`, `bras méta`, `gu et krenn`, `gu krenn`, `bisociation`, `kimi`,
   `moonshot`, `argon`, `gemini`, `fable`, `astra`, `openai`, `gpt 6`, `gpt6`, `gpt-6`, `chatgpt`.
   - CLH-03 : « gpt » est remplacé par « gpt 6 », « gpt6 », « gpt-6 » ; vérifié par la fonction du noyau (`fiches_v54.trouver`) :
     « GPT-2 », « GPT-J », « GPT-4 » passent, « gpt-6-astra » reste attrapé (aussi par « astra ») ; « GPT-60 » serait attrapé.
   - « témoin » est retiré de la liste de la mini-course : la liste fermée servie à chaque lecteur le contient trois fois et une
     étiquette dans une entrée servie est un arrêt (CL18-12) ; aucun témoin planté n'est à cacher (CLH-08).
   - **Risque accepté** : « exploratoire » et « fusion » attrapent aussi des mots courants (« étude exploratoire », « fusionner les
     deux directions ») ; ils protègent la marque et l'origine des fusions ; une fiche qui les emploie est exclue.
   - « claude », « opus », « anthropic », « sonnet » et « gpt » sont refusés dans la liste (la pièce cite Claude Sonnet 4.5,
     Opus 4.6, Anthropic ; « gpt » exclurait GPT-2). Conséquence déclarée (CLH-09) : « écrit par Claude Opus 5.5 » ou « Google
     DeepMind » passent la garde ; seule la consigne du proposeur interdit de nommer l'auteur.
   - Vérifié avant tout appel : aucune étiquette n'apparaît dans la question, la pièce, les consignes servies, la liste fermée ni
     les concepts du substitut (le `_lisez_moi` de la source, qui contient « Gu et Krenn », n'est jamais servi).
5. **Champs des fiches** : `titre`, `hypothese`, `axe`, `epreuve`, `controle`, `prediction`, `test_de_mort`, `cout` (`temoin` est
   réservé par le noyau). Axes : `raison_echec_absente`, `evaluation_contre_registre`, `residu_non_verbalise`,
   `lien_objets_non_relies`, `prediction_chiffree_8b`.
6. **Consigne du proposeur** (inchangée, v1) : trois sections de la question et pièce entière enchâssées à l'octet ; titre,
   provenance et « Lecture prévue de la sortie » non servis.
7. **Moissonneur** non appelé.
8. **Plafond technique S17 = 244 USD** (portée « course », arrêt d'étape 219,6) : garde contre une boucle ; **relevé de 60 à
   244 USD sur le mot de Lazar** (spécification § 2 : « à relever sur son mot si le devis le dépasse ») : « pas de plafond »
   (07:45, heure de Paris) et « go lance heimersheim dès que le devis est prêt », le chiffre de 244 lui ayant été dit à ≈ 08:00
   UTC (CLH-04) ; ce mot est à citer dans la ligne de GO (texte et heure). Règle du chiffre : l'entier supérieur à 1,2 fois le
   plus grand pire cas (203,15 USD ; 203,16 avec les consignes v2, calcul). La ligne de GO porte **un seul montant : « 244 USD »**.
   Relais : Kimi 2 USD (≤ 5), Argon 3 USD (≤ 10), Astra et Claude le reste.

## 4. Devis (`heimersheim/devis-course-heimersheim-v1.txt`, inchangé)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|
| cinq espèces | 317 + 5 | 23,61 USD | 203,15 USD | 0,28 / 0,76 | 0,23 / 1,69 |
| avec Kimi | 260 + 4 | 19,89 USD | 170,28 USD | 0,28 / 0,76 | — |
| sans Kimi | 203 + 3 | 16,12 USD | 138,35 USD | — | — |

Les consignes v2 allongent l'entrée de l'aiguilleur et du lecteur de quelques centaines de caractères : pire cas total + 0,013 USD
au plus (calcul) ; attendu, plafonds de session, relais et S17 inchangés (vérifiés par `course_heimersheim_v2` avant tout appel).
Course à blanc des configurations v2 : nombre d'appels identique au plan, étape par étape et modèle par modèle
(`heimersheim/course-a-blanc-heimersheim-v2.txt`).

## 5. Liste d'arrêt (codée, avant ou pendant la course) — complétée (CLH-01)

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle ;
débordement de la garde de Kimi proposeur (plus de 4 fiches sur 8 hors `niveau_methode`) ; dépassement de réserve ; garde cumulée ;
garde d'étape des commandes ; plafond propre d'un relais (HTTP 402 ou 429) ; plafond de l'étape atteint ; **nœud C13 (A14 : plus de
25 % d'appels sans sortie exploitable pour un rôle dans une étape ; pour un proposeur, qui ne fait qu'un appel, un seul échec
suffit — réponse illisible, coupée, délai de 1 750 s dépassé ; pour le metteur, trois fusions sur huit)** ; signal reçu ; toute
autre exception.

## 6. Lecture prévue (§ 4 de la spécification)

- **Ce que Lazar lira** : `fiches.json` ne contient que les fiches munies d'un passeport (classe `niveau_methode`) et les fusions
  complètes. Les fiches exclues par la garde, classées `a_corriger` ou `concret`, ou refusées par l'aiguilleur sont comptées mais
  **leur contenu n'est gardé nulle part** : le noyau ne copie jamais ce contenu (R-575, journal de l'aiguillage : identifiant,
  empreinte, classe) et le garder demanderait du code neuf (non fait, CLH-02). Rapporter les nombres par classe (journal de
  l'aiguillage, trace : passeports, refus, exclusions) et les fiches proposées par espèce (trace).
- Lazar lit les fiches et les mariages comme matière à sa réflexion ; la réponse au mentor est écrite par lui et ne suit pas de
  près un texte de machine ; l'usage le plus sûr est la partie « expériences et épreuves ». Un lecteur neuf de conv-audit relit la
  sortie scellée (redites, fiches hors niveau méthode, chiffres absents de la pièce). Classement des juges rapporté avec sa
  réserve, sans comparaison d'un axe à l'autre (§ 3.2). Sortie : dossier neuf hors du clone, manifeste de départ scellé avant le
  premier appel, sortie scellée avant toute lecture.

## 7. Gardes éprouvées et non éprouvées

- **Tout arrêt ou nœud survenu après la proposition ne rend ni `fiches.json` ni classement** (ils ne s'écrivent qu'en fin de
  génération) (CLH-01). Restent alors lisibles dans le run scellé : journaux des relais (sans texte), registre cumulé,
  `consommations.json`, manifestes de départ et de fin, coffre (verdicts et lectures d'étiquettes par identifiant, paires et clé
  des bras), journal de l'aiguillage, archive des fusions inachevées. **Les réponses brutes des proposeurs ne survivent pas** : la
  commande externe n'écrit rien dans les dossiers de session, que le noyau retire vides ; les relais ne journalisent aucun texte.
- Marge mince à l'étape « proposition » (CLH-13) : plafond dur 8,53 USD pour une somme des pires cas de 8,525 ; au pire, le
  dernier proposeur reçoit ≈ 1,645 USD pour un pire cas de 1,641 (calcul) : pas d'arrêt, mais sans marge.
- Éprouvées hors réseau : 34 essais (`test_course_heimersheim_v3.py`), contre-épreuve par neuf mutations (sur la v1, dont la v2 ne
  change que la garde lexicale), répétition par le vrai lanceur v3 derrière de faux amonts : cinq essais conformes
  (`repetition/resultat-repetition-heimersheim-v3.txt`).
- **Non éprouvées** : format réel des réponses des quatre interfaces ; vrais jetons et durées à effort « high » ; tenue des
  contrôles de Fable 5.1 et d'Astra sous 0,05 USD (≈ 1 000 jetons de sortie) ; garde lexicale et aiguilleur sur de vraies fiches ;
  solde réel de Moonshot ; la ligne de GO réelle.

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
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v2-avec-kimi.json` | `7ab45958bba64dca82e36f9009d4b949cbe923a4d9745aeb45e9a2a2bf53cb53` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v2-cinq-especes.json` | `5eb0f1af48f176c0599a7a79acb554df43d90e1acac4f84a699af129da589788` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/configuration-course-heimersheim-v2-sans-kimi.json` | `cb81afc5f5ee39fd74da72691412a73a1488668bd4ba704ea384ea9390b10d4b` | configuration |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/construire_configurations_heimersheim_v2.py` | `026cd160e843439c8f68d511f89b2a60709e9d6b777fccc922a66124e38a033b` | pièce |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/construire_consigne_proposeur_heimersheim_v1.py` | `74fbd1201516d812d7329035bf2b31665b04c77811663cda7bd01474b36586a0` | pièce |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/course-a-blanc-heimersheim-v2.txt` | `259ce1048a5276e86294aca87fbea9c48af212c9e64f412df17cc485230478c8` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/course_heimersheim_v1.py` | `a1b8a8baf32ff2dfeb4faf748fc77e18c7ac625ef17c8dad9ab119e2d79f5c41` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/course_heimersheim_v2.py` | `a07b3675c1e476ab2fe0938269f9ccf7e088811b45ace2275621c37a24a76cbc` | génération |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/devis-course-heimersheim-v1.json` | `a483556de0f56205f7df0d6e266cb8294746b4a089115e4f1af625f4132470c2` | devis |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/devis-course-heimersheim-v1.txt` | `6298856c84b30c5140dd530ce366672b1998790d8ad0ffb0a2dfc505e281cca2` | devis |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/lancer-course-heimersheim-v3.sh` | `337e91949a1a8bbbcc6443748a24c591312ec9d8f9fb92d2862c7aa2376a0fdd` | lanceur |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/lancer_course_heimersheim_v2.py` | `2fefd8fd3f5f8350d05b13e19b6d209d8b6ed73ae79cf1d98ddb998bc3458ac6` | lanceur |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/concepts-heimersheim-v1.json` | `1a80a32b284c8fa476df12337b8e0986efebd31b0b812df4d201f7c590713734` | liste fermée |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-aiguilleur-heimersheim-v2.md` | `a52b0b844abdbc51b90424f0da4bf9a4b3c1934564acbcbd55c9456fccd7fd09` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-juge-heimersheim-v1.md` | `3ecae1dcffad00c54f973cff6edf8e22383b01405b3a3c54089778dc94dfed17` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-lecteur-heimersheim-v2.md` | `fac1c9256ae8045a3f9c4a5b1768374f850e7631df32d8cf2397195e5de787f9` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-metteur-heimersheim-v1.md` | `0135b2fef863edbd0263ce76cd8d5f7e424c9930cf55a86999900899a3bb62f6` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/consigne-proposeur-heimersheim-v1.md` | `5eb778ebbcf6975dcc05a929238cbe04258d941f171bfe944240838a118a8ffa` | consigne |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/piece-etat-de-l-art-pilotage-conscience-evaluation-v1.md` | `6445fd6f9dae33500b628bdeff354ed2c7b75bd50d05cbd2aef08c3e6ce49162` | pièce servie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/question-ideation-heimersheim-v1.md` | `e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007` | question servie |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/conv-audit/specification-course-ideation-heimersheim-v1.md` | `0e2fd5bcdbb644fda55b7ccccb5be4b397e7a1e6d93d3ae7b4c721beaa1e40de` | spécification de conv-audit |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/pieces/source-gu-krenn-heimersheim-v2.json` | `dbb1922c77e395caaafc30abf20a117be6b4959d51e6ebeb44f835e2816d49b9` | source du substitut Gu-Krenn |
| `donnees/course-heimersheim-v1/orchestrateur/heimersheim/repetition/repetition_complete_heimersheim_v3.sh` | `ac63202b9cef75434fbbae06c5bc75e81ef6a2fe572178f5571e3bd4d31ff14d` | pièce |
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
2. Consignes du juge, de l'aiguilleur, du lecteur et du metteur réécrites pour la question (§ 1 : « consigne figée inchangée »).
3. Bras méta hors course (§ 1 : « trois bras »).
4. Source du substitut Gu-Krenn écrite pour cette course à partir de la seule pièce servie (v2, choix de codage au § 3.3).
5. Garde lexicale changée (§ 1 : « inchangée ») : « témoin » retiré ; « fable », « astra », « openai », « gpt 6 », « gpt6 »,
   « gpt-6 », « chatgpt » ajoutés (CLH-08).
6. Question servie par trois sections.
7. Kimi et Argon entrent comme proposeurs (la spécification les excluait pour ce tour), sur les mots de session-depot (07:18,
   07:25 UTC).
8. Copie au canal et rapport après la course : à la charge de session-depot ; « lecture des témoins » sans objet.
(Le plafond technique de 244 USD n'est plus rangé ici : il revient au mot de Lazar, § 3.8, CLH-04.)

## 9. Traitement de la contre-lecture (rapport `18e7c501…`)

| Constat | Traitement | Où, et pourquoi |
|---|---|---|
| CLH-01 (majeur) nœud C13 / A14 hors liste d'arrêt, aucune fiche après un arrêt | **déclaré** | § 5 (nœud ajouté, un seul échec de proposeur suffit), § 7 (rien n'est rendu après un arrêt ; ce qui reste lisible ; réponses brutes perdues), § 2 (cinq points de rupture uniques en cinq espèces) ; aucun code changé (noyau v56 tel quel) |
| CLH-02 (majeur) seules les fiches à passeport sont lisibles ; pentes vers l'écart | **corrigé et déclaré** | consigne de l'aiguilleur v2 (exemple d'axe retiré, protocole détaillé = `niveau_methode`, « détails opérationnels » restreints, « doute → concret » gardé), § 3.2 ; § 6 (sortie lisible = fiches à passeport ; fiches écartées non gardées : le noyau ne le permet pas sans code neuf) |
| CLH-03 (majeur) « gpt » exclut GPT-2, GPT-J | **corrigé** | garde lexicale v2 (« gpt 6 », « gpt6 », « gpt-6 », « chatgpt » gardé ; « gpt » refusé par le contrôle) ; vérifié par la fonction du noyau ; « exploratoire » et « fusion » : risque accepté, § 3.4 |
| CLH-04 (majeur) relèvement à 244 USD : mot de Lazar | **corrigé** | § 3.8 et § 1 (mots cités tels quels, heure du chiffre dit) ; retiré des écarts § 8 |
| CLH-05 (majeur) lien GLM-5 – « incohérence hors variété » absent de la pièce | **corrigé** | source du substitut v2 ; essai : la paire n'est plus « reliée » |
| CLH-06 (mineur) K1 et K3 imposent la forme de la demande 5 | **déclaré** | § 3.2 : ne pas comparer le classement d'un axe à l'autre ; consigne du juge inchangée (déjà contre-lue, changement de fond non demandé) |
| CLH-07 (mineur) citation inexacte | **corrigé** | § 1 : « pas de plafond » (Lazar), « sans plafond » (session-depot) |
| CLH-08 (mineur) écart de garde incomplet, raison inexacte | **corrigé** | § 3.4 (raison opérante : liste fermée servie ; `_lisez_moi` jamais servi) et § 8.5 (ajouts déclarés) |
| CLH-09 (mineur) noms d'auteur Claude, Google passent | **déclaré** | § 3.4 ; liste non étendue (« claude », « opus » sont dans la pièce ; extension non demandée, à rééprouver si faite) |
| CLH-10 (mineur) autres choix de codage de la source | **déclaré** | § 3.3 et `_lisez_moi` de la source v2 |
| CLH-11 (mineur) le lecteur cherche un « témoin » | **corrigé** | consigne du lecteur v2 (champ `controle`) |
| CLH-12 (mineur) lanceur v1/v2 ; rapport de la fille pour Argon | **corrigé / laissé à session-depot** | en-tête (« le lanceur, v1, v2 comme v3 ») ; § 2 : rapport de la fille à citer par session-depot (je n'en ai ni le chemin ni l'empreinte) |
| CLH-13 (mineur) marge mince à la proposition | **déclaré** | § 7 ; rien changé (le relever demanderait une configuration et un devis neufs) |
