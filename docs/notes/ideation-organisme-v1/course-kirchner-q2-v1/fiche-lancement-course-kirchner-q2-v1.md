# Fiche de lancement — course d'idéation sur la question 2 du mentor Kirchner — brouillon 2

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 10:35 UTC (`date -u`). Brouillon 2 = brouillon 1 (gardé, R12)
corrigé après sa contre-lecture (`docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/contre-lecture-fiche-lancement-course-kirchner-q2-v1.md`,
`b70b0ec7…`, « scellable après corrections », aucun bloquant) : source Gu-Krenn v2, aiguilleur v2, configurations v2, lanceur shell
v2, table des pièces gelées v2 ; traitement constat par constat en § 9. **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel n'a été fait pour l'écrire. Le kit
est celui de la course Heimersheim (`outils/course-heimersheim-v1`, version après contre-lecture : pièces v2, garde lexicale v2,
lanceurs Python v2 et shell v3), renommé et adapté à cette question.

Contre-lecture : `docs/notes/ideation-organisme-v1/course-kirchner-q2-v1/contre-lecture-fiche-lancement-course-kirchner-q2-v1.md`, sha256 `b70b0ec7748b48cca3d5da7db973df97323c811aaa81317ea5f481dd66cac580` (lecteur neuf, rendu sur le brouillon 1 ; « scellable après corrections », traité au § 9). Version scellée écrite par session-depot le 3 novembre 2026 à partir du brouillon 2, sans autre changement que cette ligne

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
- Mots de Lazar, à la lettre (CLK-03) : **mot direct** à session-depot, « je eux que Kirchner Q2 passe avant A1-v3 » (verbatim,
  avec la faute ; reçu entre 09:33:19 et 10:06:47 UTC, `registres/decisions.md`, R-1121) ; **mot rapporté** par conv-audit,
  « go pas de plafond » (09:24, heure de Paris, spécification). Le mot direct ne dit rien du montant : le plafond technique de
  245 USD s'appuie sur le mot rapporté et sur l'ordre direct. Il est inscrit dans **GO-2026-11-03-05** (déjà au registre
  `registres/go.md`, un seul montant : 245 USD).
- Instrument : orchestrateur v56 (copie à l'octet vérifiée), génération de la mini-course (`course2_nuit_v1`, adaptateur
  `course2_nuit_v2`), au-dessus `course_kirchner_v1.py`. Une génération, une passe, **8 fiches par proposeur**.

## 2. Variantes (une seule est lancée)

| Variante | Proposeurs | Quand |
|---|---|---|
| `configuration-course-kirchner-q2-v2-cinq-especes.json` | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | **lancement**, si Argon n'est utilisé par rien d'autre : ni le tour du collisionneur v9 (espèce C), ni la seconde course d'A1-v3 ne tournent avec Argon, ce que session-depot vérifie par l'état de la fille et du relais 8805 (le refus de port pris ne voit que l'hôte local) (CLK-07) |
| `configuration-course-kirchner-q2-v2-avec-kimi.json` | Fable 5.1, Opus 5.5, Kimi, Astra | repli si Argon est pris |
| `configuration-course-kirchner-q2-v2-sans-kimi.json` | Fable 5.1, Opus 5.5, Astra | repli si le contrôle de Kimi échoue ; seule variante sans la garde de débordement de Kimi (§ 5) |

Rôles identiques : aiguilleur Opus 5.5 ; juges Opus 5.5 et Astra (unanimité) ; lecteurs Opus 5.5 et Astra ; metteur Fable 5.1 ;
Claude par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Astra 8807, Kimi 8804, Argon 8805 (cinq
espèces seulement) ; le lanceur refuse un port déjà pris. Chaque proposeur est un point de rupture unique (§ 5). Lanceur :
`kirchner/lancer-course-kirchner-v2.sh` (n'accepte que les configurations v2).

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
   **Aiguilleur v2 (CLK-02)** : « en cas de doute, concret » gardé ; une fiche qui propose de planter des tricheries, des
   tricheurs scriptés ou des lois déplacées pour éprouver un moniteur, décrits par classe, rôle de mesure et difficulté visée,
   est dite `niveau_methode` ; seule la recette opérationnelle pour tromper un moniteur réel est `concret`. Biais de forme
   déclarés (CLK-09) : K3 ajoute le coût chiffré, que le critère gelé 3 ne demande pas ; K5 « nouveauté posée comme question »
   tire contre K1 ; « aucun identifiant inventé » n'est pas vérifiable sans les pièces (le juge ne les voit pas : il peut tenir
   2608.28945, 2407.13692 ou 2605.06390 pour inventés) ; K1 note une affirmation de la fiche, pas une moisson ; l'exemple du
   metteur oriente les fusions vers les axes 2 et 3. Les sorties des juges restent à part (protocole § 1.2).
3. **Bras joués** : `gu_krenn` (substitut) et `basique` (exposant 8,5, décalage 0,05), quatre paires par bras. Liste fermée :
   46 concepts tirés des seuls textes servis (`pieces/concepts-kirchner-v1.json`). Source du substitut **v2**
   (`pieces/source-gu-krenn-kirchner-v2.json`, CLK-01) : 23 œuvres, une par source citée par les textes servis ; concepts =
   ceux que les textes attribuent à cette source ; aucun lien des notes de moisson ni des rapprochements de la question.
   Corrections : retirés « banc tenu à l'écart » de Yudelson (les textes parlent de moniteurs tenus à l'écart), « optimisation
   contre un moniteur » de MacDermott (rapprochement de la note de moisson), « moniteur de triche après coup » de Kale (la pièce
   lui attribue l'échafaudage), « tricheries plantées » de la banque réelle (ses lois plantées sont des témoins de puissance, pas
   des tricheries : la raison du brouillon 1 était fausse) ; ajoutés « seuil de Ville » et « tricheries plantées » au nul v8
   (nos résultats § 1 et § 2) et « sélection par classement » à 2608.28945 (pièce § 2.5, § 3). Choix déclarés : Yudelson garde
   « optimisation contre un moniteur » (la question le range sous cette ligne) ; « rappel du moniteur » n'est porté par aucune
   source (la pièce dit qu'aucun rappel n'est lu) : il est hors du vocabulaire du bras Gu-Krenn, donc jamais lu par ses lecteurs
   — le concept central de la demande 2 ne compte que dans le bras basique (CLK-08). Codage contre-lu une fois.
   **Bras méta hors course** (annexe propre absente).
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
supposé, Kimi 2 / 10, Argon 10 / 50 supposé) ; la consigne du proposeur est plus longue (30 452 octets, 29 581 caractères : deux pièces) (CLK-04).
Repère : la course Heimersheim réelle a coûté 10,026275 USD (08:31:19 → 09:29:11Z) pour 23,61 attendus (`registres/decisions.md`,
R-1120 ; sortie copiée au canal `canal/session-depot-reprise-n139`, commit `93928ba8`) (CLK-05). Les consignes v2 n'allongent
que l'aiguilleur (≈ 400 caractères) : pire cas + 0,02 USD au plus (calcul), S17 inchangé ; plafonds vérifiés avant tout appel. Course à blanc :
nombre d'appels identique au plan dans les trois variantes (`kirchner/course-a-blanc-kirchner-v1.txt`).

## 5. Liste d'arrêt

Avant la course : un contrôle d'avant course en échec. Pendant : modèle servi différent ; trois échecs consécutifs d'un rôle ;
débordement de la garde de Kimi proposeur ; dépassement de réserve ; garde cumulée ; garde d'étape ; plafond propre d'un relais ;
plafond de l'étape ; **nœud C13 (A14 : plus de 25 % d'appels inexploitables pour un rôle ; pour un proposeur, un seul échec
suffit)** ; signal ; toute autre exception. **Tout arrêt ou nœud après la proposition ne rend ni fiches ni classement** ; restent
lisibles les journaux, manifestes, consommations, coffre et le journal de l'aiguillage ; les réponses brutes ne survivent pas.
Arrêts propres au lanceur (CLK-06) : **124** délai de 12 h (course arrêtée par signal : manifestes et sceau écrits, aucune fiche) ;
**6** clé trouvée dans une sortie (pas de copie au canal ; la sortie reste scellée, lisible sur place) ; **7** trace refusée ou
sceau en échec (la sortie de la course reste ; la trace manque). **Risque propre à cette question (CLK-02)** : la demande 2 appelle
des tricheries plantées ; au-delà de 4 fiches `concret` sur 8 chez Kimi (S12 = 0,5), la course s'arrête après l'aiguillage sans
aucune fiche ; `avec-kimi` et `cinq-especes` portent ce point de rupture, `sans-kimi` non. Le rapport d'après course donne le
nombre de fiches **par classe et par espèce** (journal de l'aiguillage, identifiants des fiches, trace).

## 6. Lecture prévue (spécification § 4 ; protocole Kirchner v1)

Sorties scellées avant lecture, copiées à l'octet sur le canal, sans clé ; rapport par lecteurs neufs au protocole Kirchner v1
(quatre critères gelés, témoins publiés déguisés, comparaisons par paires). **Écart au protocole § 1.2 à noter** : la course ne
rend dans `fiches.json` que les fiches munies d'un passeport ; les fiches `a_corriger`, `concret` ou exclues par la garde sont
comptées mais leur contenu n'est gardé nulle part (le noyau ne le copie jamais, R-575) : elles sont « comptées, non lues »,
comme le protocole le prévoit. Les sorties des juges de la course sont rapportées à part, jamais utilisées pour garder ou
écarter une idée (protocole § 1.2). Lazar écrit seul sa réponse.
Préparateur du rapport (CLK-11) : il voit `fiches.json` (fiches à passeport et fusions complètes) et l'archive des fusions
inachevées (`fusions-inachevees.json`, contenu quand il existe : « inachevées comprises ») ; il ne voit ni le coffre (clés,
verdicts, paires et clé des bras : ouverts par session-depot seulement, pour les comptes de mariages par bras), ni les sorties des juges.

## 7. Gardes éprouvées et non éprouvées

Éprouvées hors réseau : 34 essais sur les configurations v2 (`kirchner/test_course_kirchner_v2.py`, gelé ci-dessous) ;
contre-épreuve par neuf mutations sur le kit v1, toutes détectées (`kirchner/resultat-mutations-kirchner-v1.txt`, `a8afc15a…`, gelé) ;
répétition v2 par le vrai lanceur v2 derrière de faux amonts : cinq essais conformes
(`kirchner/repetition/resultat-repetition-kirchner-v2.txt`, `ff1fbd22977efdcd60f5449a62d3aea64aeb0cffa208522b3d806bf16dd04895`).
Marge mince à la proposition (CLK-13) : plafond de l'étape 8,8 USD pour un pire cas de 8,79 (8,73 à la formule des commandes) ;
la durée de Kimi (jusqu'à 65 536 jetons en 1 750 s) n'est pas éprouvée avec cette consigne plus longue : un délai dépassé chez un
proposeur donne le nœud C13, donc aucune fiche. Non éprouvées : formats réels des interfaces (déjà éprouvés
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
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v2-avec-kimi.json` | `88836df4ffc1d8f73a289c9ed1f66fc89bfbdd8cade3bfa683cc5aa5e192339e` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v2-cinq-especes.json` | `4211e9bac2cefcf3ed845fbeacb2558a5328655b8d6eaa42b49cd0a917e3d9d1` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/configuration-course-kirchner-q2-v2-sans-kimi.json` | `561625286d51c0586ce2521798645fd7fb66da1ea63a299fe16f97af51e7ecc7` | configuration |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/construire_configurations_kirchner_v2.py` | `90a337dc7bd13777dc56bba1d74064c078b0f1010072de8948691ecef3fe80ec` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/construire_consigne_proposeur_kirchner_v1.py` | `d0c4b66770e6ac78edbf3865ea6be7ce921440caaafac994ea3a9eea32e71f8a` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/course-a-blanc-kirchner-v1.txt` | `e637baa687f373863573c366c226b891cb0bf7188b29e8edf018d02595e8fe77` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/course-a-blanc-kirchner-v2.txt` | `468cf0717f70568ca882a6372b4c653f957d3d1304f3dffe74055c0ba09bb5da` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/course_kirchner_v1.py` | `9a850f0a7e81d48e4013a2eaf9ad23bf5b0c43ff0119b99f265ac2d9b6a30876` | génération |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/devis-course-kirchner-v1.json` | `58c8816f8f6094aa7d2080c37b328a0045ad10c4d4040f978154f2d77f1e212b` | devis |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/devis-course-kirchner-v1.txt` | `7e3ca59cc318da84ad90e927088ce64e24e2f84a26dd3c2740066416d474d054` | devis |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/lancer-course-kirchner-v1.sh` | `a4c13b5b05afa45875349a6fa1915f5164d5373e8aa166f86a3e7b5a2fd1e49f` | lanceur |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/lancer-course-kirchner-v2.sh` | `2840b238b358a32938b7ebf7520fe40589beee14a39c19ce5abc5050a1deeb9a` | lanceur |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/lancer_course_kirchner_v1.py` | `affc80f93feb51f681d2c8fafa9a63c8a3ea55234ffeb7c67edbaeae072f7e58` | lanceur |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/concepts-kirchner-v1.json` | `2d78923b2c6b1270ddf92676ed736d12a1fb9dc41f308ba900d0338f93ca7147` | liste fermée |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-aiguilleur-kirchner-v2.md` | `7514666ee8a0f46149f4ad3a541f2a77c0945e5b7ef8b825c894e3dd7ad5569b` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-juge-kirchner-v1.md` | `539d712ad4d3c57e3fec4aa1b292a478884ed350222d311a939635325cd187a6` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-lecteur-kirchner-v1.md` | `897a16ea9770f58b78721d08a595a34cf225e2864d0631d3157d07de3fa516f6` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-metteur-kirchner-v1.md` | `9aa2b7e8d3a4444b66948e21aa9ec4f35ec5ac754645373f0b50f084e96f0f2a` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/consigne-proposeur-kirchner-v1.md` | `ae7109dc297cae429b280a58061a6f284de689d7b482a1b9e3db9075263e94b0` | consigne |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/piece-kirchner-v2.md` | `6e7fb1c56cb292aa97667f11093959f775f940b06dc85d8038e728813e4203f5` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/protocole-rapport-idees-kirchner-v1.md` | `68919ec9a4afcbf8cae764df9cf04834c5c662b0bc62f8c7a515671c97c0a781` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/question-ideation-kirchner-v1.md` | `291f91f882d9a130570b1da600212f07435ec19cb87b9e9d65380a5c4c650253` | question servie |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/conv-audit/specification-kirchner-q2-v1.md` | `934f5dcb0bd442f0c17b2c1aada88041795ab7336e3b03d5fe1bd8bb7c068622` | spécification de conv-audit |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/pieces/source-gu-krenn-kirchner-v2.json` | `5a8ede4d9241061dce4a8311dbd27420eb1f594bde2eb206d31eee993d8ac45a` | source du substitut Gu-Krenn |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/repetition/repetition_complete_kirchner_v1.sh` | `3dc5364cd745419155e6c1fffc7293fe6ae53cc5a185539e9cdb21feacc7b55f` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/repetition/repetition_complete_kirchner_v2.sh` | `c6563cf4ffc2fce65dcdd7ea683a362d496f368b5113d877066bd0964b32a0f5` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/resultat-mutations-kirchner-v1.txt` | `a8afc15ac584997116b31e809fcd37172ec48dfb1d9a0e74960b12896e661357` | pièce |
| `donnees/course-kirchner-q2-v1/orchestrateur/kirchner/test_course_kirchner_v2.py` | `4c19431e6aa6737355d7c2827e64e3614396eba7dfa6bd80b6b3f89fb0b47a80` | génération |
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
8. Plafond technique de 245 USD appuyé sur le mot rapporté « go pas de plafond » et l'ordre direct (la spécification demandait
   que le mot direct soit redit) ; inscrit dans GO-2026-11-03-05.
6. Fiches non admises par l'aiguilleur non gardées (protocole § 1.2 : « comptées, non lues »).
7. Le tour du collisionneur v9 de la spécification n'est pas dans ce kit.

## 9. Traitement de la contre-lecture (rapport `b70b0ec7…`)

| Constat | Traitement | Où, et pourquoi |
|---|---|---|
| CLK-01 (majeur) liens Gu-Krenn faux dans les deux sens | **corrigé** | source v2 (retraits et ajouts), § 3.3 ; essais : paires retirées non reliées, paires des textes reliées |
| CLK-02 (majeur) aiguilleur poussé vers `concret`, risque d'arrêt par Kimi | **corrigé et déclaré** | aiguilleur v2 (planter pour éprouver = `niveau_methode` ; seule la recette opérationnelle = `concret` ; « doute → concret » gardé) ; § 5 (risque, variante `sans-kimi` sans ce point de rupture, nombres par classe et par espèce au rapport) |
| CLK-03 (majeur) montant sur mot rapporté ; citation inexacte | **corrigé** | § 1 (deux mots à la lettre, heures, GO-2026-11-03-05) ; § 8.8 |
| CLK-04 (mineur) octets et caractères | **corrigé** | § 4 |
| CLK-05 (mineur) chiffres sans empreinte | **corrigé** | § 4 (R-1120, `93928ba8`) ; § 7 (résultats cités par empreinte ; essais et mutations gelés) |
| CLK-06 (mineur) arrêts du lanceur | **corrigé** | § 5 (124, 6, 7 et ce qui reste lisible) |
| CLK-07 (mineur) exclusivité d'Argon | **corrigé** | § 2 (tour v9 et seconde course d'A1-v3 nommés ; vérification par session-depot) |
| CLK-08 (mineur) « rappel du moniteur » hors du vocabulaire Gu-Krenn | **déclaré** | § 3.3 |
| CLK-09 (mineur) biais de forme du juge et du metteur | **déclaré** | § 3.2 ; consignes du juge et du metteur inchangées |
| CLK-10 (mineur) numéro de GO en remplissage | **corrigé** | § 1 : GO-2026-11-03-05 |
| CLK-11 (mineur) statut du coffre, fusions inachevées | **corrigé** | § 6 |
| CLK-12 (mineur) chemins internes dans les textes servis | **laissé, signalé** | fidélité à l'octet exigée ; information pour conv-audit |
| CLK-13 (mineur) marge mince, délai de Kimi | **déclaré** | § 7 |
| CLK-14 (mineur) cosmétique du kit | **laissé** | aucun effet à l'exécution ; à corriger dans une version suivante (R12) |
