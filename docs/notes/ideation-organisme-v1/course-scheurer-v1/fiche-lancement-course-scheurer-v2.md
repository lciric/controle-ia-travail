# Fiche de lancement — course d'idéation sur la question du mentor Scheurer, variante sans Claude (kit v2) — v2 scellée

Version scellée écrite par session-depot le 3 novembre 2026 (heure lue par `date -u` à 18:28:11) : brouillon 1 (`67fa274dfb086c152bba856e5b19d121477dffd15814b1a65bb73abba2efeb9f`) avec les constats de sa contre-lecture traités au § 9 (CLS2-01 tranché par la décision R-1170 de session-depot) ; aucun code, aucune configuration, aucune pièce changés ; la note de retrait `retrait-variante-sans-claude-v1.md` est levée par `levee-retrait-variante-sans-claude-v1.md`. Rédigée par un sous-agent de session-depot le 3 novembre 2026, 14:55 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : Scheurer v2
(branche `outils/course-scheurer-v1`), au-dessus du kit v1 (`c4797620`, gelé) ; la fiche v1 (`docs/notes/ideation-organisme-v1/course-scheurer-v1/fiche-lancement-course-scheurer-v1-brouillon1.md`) reste celle des cinq
variantes v1.

Contre-lecture : `docs/notes/ideation-organisme-v1/course-scheurer-v1/contre-lecture-fiche-lancement-course-scheurer-v2-brouillon1.md`, `926ed6ff3232d693e97e1690ee3dc32ceb2963e6ec77746ec54ecaec007e4f62` (« bloquant en l'état, pour une raison de règle et non de technique » ; kit jugé conforme ; bloquant tranché au § 9).

## 1. Pourquoi cette variante, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Constat de session-depot (son dernier message) : la course Scheurer en variante `sans-opus-argon` s'est arrêtée en nœud C13
  après la proposition, **sans aucune fiche** ; le relais Claude est au statut REFUS : Fable 5.1, seul proposeur Claude, a très
  probablement refusé la question, comme Opus au tour du collisionneur (catégorie « cyber »). Argon, Kimi et Astra sont OK
  (rapport `donnees/course-scheurer-v1-run/rapport-course-scheurer-v1.md`, branche `donnees/course-scheurer-v1-run`, `04ab7367` ;
  rapport `6b2da5f52634717989a672fc5436eb400473ffe44a22a272af342443ad7c2364` ; réserve : le refus de Fable n'est lu qu'au statut du
  relais, non vérifié au journal de proposition). La variante neuve n'emploie **aucun modèle Claude** : rien n'est rejoué à Claude.
  Règle en jeu : la consigne gelée « ne contourne jamais un refus d'un filtre de sûreté », bornée par la R-468 (5) aux cas où l'on
  chercherait à obtenir un contenu dangereux visé par le refus ; la R-486 avait refusé une course dont le fond (« contournements »)
  était en cause. Ici, session-depot a lu le texte servi et juge le fond sans danger (décision R-1170, § 9).
- Pièces servies et règles : celles du kit v1, inchangées (question `edb1d5f1…`, deux sections ; pièce Scheurer `2d0e60fc…` ;
  nos résultats `d6fa8011…` ; juge du n° 419 plus K4 ; garde lexicale sans « gemini » ni « openai » ; spécification
  `specification-course-scheurer-v1.md`, `97c67ec1…`, à laquelle les écarts du kit v1 restent déclarés).
- Mots de Lazar, **directs** : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de plafond » (R-1149), puis,
  sur cette variante, « oui : Scheurer à trois espèces, Ibrahim à cinq » (vers 18:24 UTC, R-1170). Ligne de GO : **`GO-2026-11-03-17`,
  130 USD** (plafond technique S17, pas un plafond de Lazar), inscrite sur `main` à `6fed644e` ; elle est
  passée au lanceur comme `GO_ID` et comme deuxième argument (le lanceur ne vérifie que cette ligne, dont le montant doit être le
  S17 de la configuration).

## 2. La variante

| Configuration | Proposeurs | Aiguilleur | Juges (unanimité) | Lecteurs | Metteur | S17 | GO |
|---|---|---|---|---|---|---|---|
| `configuration-course-scheurer-v1-sans-claude.json` (`ff8e5dd2c0e12fb898551e2340bc1b53df02da3b3164809477b64a551473c4b2`) | Argon, Kimi, Astra | Astra | Astra, Argon | Astra, Argon | Astra | 130 | `GO-2026-11-03-17` |

**Répartition, au plus près d'Ibrahim** (acceptée par session-depot) : chaque rôle de Claude passe à Astra (aiguilleur, premier
juge, premier lecteur, metteur), chaque rôle d'Astra passe à Argon (second juge, second lecteur) ; Kimi reste **proposeur
seulement** (sortie de format fragile, R-1155). Le relais 8806 **ne démarre pas** ; aucune clé Anthropic n'est exigée ; le contrôle
d'avant course ne joue que les modèles employés (Astra, Kimi, Argon). Lanceur : `scheurer/lancer-course-scheurer-v2.sh` (accepte
les six configurations ; pour les cinq configurations v1, son comportement est celui du lanceur v1).

## 3. Déclarations et écarts

1. **Aucun juge de la famille Claude** ; les juges et les lecteurs ne sont que **deux lignées**, Astra et Argon, et **Astra est aussi
   proposeur** (et aiguilleur et metteur) : un juge peut noter des fiches de sa propre espèce ; les sorties des deux juges sont
   rapportées à part, le classement ne se lit pas comme un jugement indépendant des proposeurs.
2. **Lecteurs d'autres lignées que dans les kits précédents** (Astra et Argon au lieu de Claude et Astra) : les étiquettes ne se
   comparent pas d'une course à l'autre.
3. **Plafond propre du relais Argon : 20.7 USD**, au-dessus de la règle « Argon ≤ 10 USD » (accepté par
   session-depot pour cette seule variante) : Argon y est second juge et second lecteur, sa part au pire cas est de
   17.1951 USD (64 appels au plan, contrôle compris) ;
   plafond = 1,2 × cette part, arrondi au dixième supérieur. **La dépense d'Argon est lue au registre cumulé à la fin de la course.**
4. Argon répond aux rôles courts avec au plus 4 000 jetons de sortie (option de sa commande) ; une réponse de juge ou de lecteur
   tronquée compte comme un échec du rôle (trois échecs consécutifs ou C13 : arrêt sans fiche).
5. Le reste est celui du kit v1 (déclarations § 3 de la fiche v1) : aucun témoin planté ; bras `gu_krenn` (substitut) et `basique` ;
   six fiches par proposeur ; consignes, liste fermée et source gelées identiques (mêmes empreintes) ; garde lexicale identique.
6. Code (plus petit changement, fichiers neufs v2) : jeu de rôles par variante, metteur compris ; fournisseurs exigés = ceux des
   proposeurs et des rôles ; réglages Claude exigés seulement si Claude est employé ; borne propre des relais par variante ; le
   reste de S17 va au relais Astra quand Claude est absent ; le lanceur shell ne démarre Claude, n'exige sa clé et ne le contrôle
   que si la configuration l'emploie.

## 4. Devis (`scheurer/devis-course-scheurer-v2.txt`, `167f87d3ec8f896adb658d4caa8e9f9bd060352ed94361ab76907b06f8460a89`)

- Appels : 161 de course + 3 contrôles ; attendu **18.10 USD** ; pire cas
  **107.86 USD** ; S17 = 130 (entier supérieur à 1,2 × 107.86 = 129.43, calcul) ;
  arrêt d'étape 117.
- Par fournisseur (attendu / pire cas) : Astra 11.51 / 89.88 ;
  Argon 6.37 / 17.20 ;
  Kimi 0.22 / 0.79.
- Relais : Astra 107.3 USD (201 appels au plus) ; Argon 20.7 USD
  (133) ; Kimi 2.0 USD (9) ; marge d'appels 2 × plan + 5 ; une fiche
  de plus coûte 4 appels Astra et 3 appels Argon : **23 fiches de trop tolérées** (calcul).
- Plafonds de session : proposeur 3,5 ; aiguilleur 0,9 ; juge 0,9 ; lecteur 0,9 ; fusion 3,5, chacun au-dessus du pire cas d'un
  appel de son rôle sur toutes les variantes. Hypothèses : celles du devis v1 (prix Astra 10 / 50 et Argon 10 / 50 supposés).
- Course à blanc v2 : nombre d'appels identique au plan dans les six variantes (`scheurer/course-a-blanc-scheurer-v2.txt`,
  `1cfea9488d2d5ceefcb15265d31211eaa497129d85ed0ae101ebc70172476c6b`).

## 5. Liste d'arrêt

Celle du kit v1 : un contrôle d'avant course en échec ; modèle servi différent ; trois échecs consécutifs d'un rôle (un refus
compte comme un échec) ; débordement de la garde de Kimi proposeur ; dépassement de réserve ; garde cumulée ; garde d'étape ;
plafond propre d'un relais (HTTP 402 ou 429, nombre d'appels épuisé compris) ; plafond de l'étape ; **nœud C13** (pour un
proposeur, un seul échec suffit) ; signal ; toute autre exception. Tout arrêt après la proposition ne rend ni fiches ni
classement. Codes : 124 délai de 12 h ; 6 clé trouvée ; 7 trace refusée ou sceau en échec.

## 6. Lecture prévue

Comme le kit v1 : sortie scellée avant lecture, copiée à l'octet ; rapport au protocole « mentors du soir » par extension ; Lazar
écrit seul sa réponse. Le rapport dit que la course a tourné sans aucun modèle Claude.

## 7. Gardes éprouvées et non éprouvées

64 essais (`scheurer/test_course_scheurer_v2.py`, gelé ; dont : aucun Claude dans la configuration, rôles et proposeurs attendus,
artefacts « fournisseur Claude ajouté » et « metteur Claude » refusés, lanceur sans relais Claude, ligne de GO au S17) ; douze
mutations, toutes détectées, dont M11 (relais Claude démarré sans Claude) et M12 (Claude toujours exigé)
(`scheurer/resultat-mutations-scheurer-v2.txt`, `ebfdafafe7917bb1834f84488d8bd57a27b909bfa9f3ee15d1ddcd01ba9713e0`) ; répétition v2 derrière de faux
amonts à **8 fiches par proposeur** : cinq essais conformes (`scheurer/repetition/resultat-repetition-scheurer-v2.txt`,
`79170b2b6331d3cf5a8963a834f12bfaf448ae5d85f7ae0fae261d6abe3723f7`) ; course complète au bout (code 0, 24 fiches, 8 fusions ; Astra 122
appels sur 201, Argon 82 sur 133, Kimi 2 sur 9 ; **aucun appel vers l'interface Anthropic**) ; `kill -TERM` : code 130. Un premier
passage avait rendu un écart à l'essai 2 (clé factice d'Argon non passée par le script), corrigé et rejoué en entier.
Non éprouvés : la tenue d'Argon et d'Astra comme juges et lecteurs réels (formats, troncatures) ; Argon en lecteur a servi à la
mini-course de nuit, Argon en juge jamais dans ces kits ; ligne de GO réelle.

## 8. Commande exacte (en arrière-plan ; dossier du run NEUF, hors du clone ; après le mot de Lazar et l'inscription de GO-17)

```
cd /home/user/controle-ia-travail/donnees/course-scheurer-v1/orchestrateur/scheurer
mkdir -p /home/user/runs-course-scheurer-v1
RUN=/home/user/runs-course-scheurer-v1/run-$(date -u +%Y%m%d-%H%M)-sans-claude
GO_ID=GO-2026-11-03-17 nohup bash lancer-course-scheurer-v2.sh lancer \
  GO-2026-11-03-17 configuration-course-scheurer-v1-sans-claude.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```

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
| `donnees/course-scheurer-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-scheurer-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-scheurer-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-scheurer-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-scheurer-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/EMPREINTES-orchestrateur-course-scheurer-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `5fb1b202f3cb637c9e4aa72b826f654dc46f963ad18631eb8806ba1d53a3fb84` | vérification de la copie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/calcul_devis_course_scheurer_v1.py` | `61ec99e4242cb6f6d4613ad24cd801427a1c6685d9904517f5d2b19c679ab442` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/calcul_devis_course_scheurer_v2.py` | `8bd9c71b68b3ed1d19f895a30947a99d15a0e9c34548b9144dfd3fc70de656fd` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/commande_claude_scheurer_v1.py` | `efcb2c0a41bdaa76870b889c9badcc8f3307fe3226f5354be9ddad32e34f6ca3` | commande |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-avec-opus.json` | `916aff7059ec829c26e57af85b792b357481a3498ba474c7395c2df6b00745ca` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-claude.json` | `ff8e5dd2c0e12fb898551e2340bc1b53df02da3b3164809477b64a551473c4b2` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-argon.json` | `364f2c91bcfe904734625c2f3382fcc8da2630eb169f8b097c5b1eab121fe258` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-juges-opus.json` | `02a36104ce9847275bba2d408883acbb180cba3dc7ff2ca295c799540499871d` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus-sans-kimi.json` | `46d5025f3ef3cd22bffabcbc8cf6f3c90dfb3163b633687513ae500032ef0dbd` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/configuration-course-scheurer-v1-sans-opus.json` | `e6e739d7c70b262b9fec7c26681ed1cc1b089fe11ac72c7a7f1b07db52f1ca23` | configuration |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/construire_consigne_proposeur_scheurer_v1.py` | `2f61e503e57e259c31eeb98f71e14a41ebb65f3ea7909a1aaf0abf121f134e4a` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course-a-blanc-scheurer-v1.txt` | `88a62108c25c63e4551ebc8023aa5fdca0fc2e9c0ab551fcd1e559d6c8c7246a` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course-a-blanc-scheurer-v2.txt` | `1cfea9488d2d5ceefcb15265d31211eaa497129d85ed0ae101ebc70172476c6b` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course_a_blanc_scheurer_v2.py` | `824fe2f72f157cf518959d8c42937906c40d0a938f6cc331c8954b97a3013381` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course_scheurer_v1.py` | `abe9a5422129dd064c40ab172eb751f7f4b0eef6ecaf7322dda0c689b15681a4` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/course_scheurer_v2.py` | `4703032352920284ebc020503bbe9171f07ccf0a599c73ca6417e284b05aeb05` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v1.json` | `fdcb91ef6305d6e321c7506821edebce2e6feb1c1392ad80c0f6c5e0f240567e` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v1.txt` | `2b16851202d2be39090014a3f9b11f34458e44184434c0b89c65f4af6ea163db` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v2.json` | `73e3a08b320c5315b126948084a31a4bb497c4ed814b2beffb1b79d02b6a869f` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/devis-course-scheurer-v2.txt` | `167f87d3ec8f896adb658d4caa8e9f9bd060352ed94361ab76907b06f8460a89` | devis |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer-course-scheurer-v1.sh` | `8683cc240306a31d47920c7d7c1bf4fcbd32d25fcc1e85203f446b1363083ec1` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer-course-scheurer-v2.sh` | `9391a28df334658a581d41937daec3e0dca68fe0dbd6c246724d8258427c0bb8` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer_course_scheurer_v1.py` | `1f551d925fb9a4f3336d10d341523282b2521d7ea44dd0bbdae3e674bc2cfb38` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/lancer_course_scheurer_v2.py` | `40577c90c8f9e096881ed06861958942b7b2a0f0ac83a66f43bd7eadb6f84030` | lanceur |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/mutations_scheurer_v1.py` | `6630dd8c378e37ea32bfa2fb55885d59cd0de1b4b06f3ba1a5004173d83bf946` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/mutations_scheurer_v2.py` | `b26d9045ad647d94366274dc4f86dfa7bbaa2d4c2e5c7beb48c30793ae14a7cf` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/concepts-scheurer-v1.json` | `a169ce62506f06004cd8ed5470d96041f6993e18db98fb210fe20f72d192d3a7` | liste fermée |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-aiguilleur-scheurer-v1.md` | `38ca7c012f31b53b813cde50f0387a695642f27cfb4bbe70d7f00b35f3bc8cc7` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-juge-scheurer-v1.md` | `8215d020969cfbd2a0e751997d628056cdea06b487b3743bf4d1a092fa2493ff` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-lecteur-scheurer-v1.md` | `7bc3e6dd87265f50a1f930badd2a2b51d5a3e1498f17be52b48d66ef59bc83e3` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-metteur-scheurer-v1.md` | `0549b7677e2bd12c1efde1b289aa21fba124df77f1a4008cea624f82f0795c40` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/consigne-proposeur-scheurer-v1.md` | `ab203b3789778b888df5a1a403b58ca8fb3b4efc94dbb09cb3a233c2bfced004` | consigne |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/piece-scheurer-v1.md` | `2d0e60fc78e5930fb4ad1fe60d6fba8f2a17f4a03729570ea896db0c339f3796` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/conv-audit/question-collisionneur-scheurer-v1.md` | `edb1d5f130c9e60cfc35b12ba6a4fb83ce2c9805cd8ad91085d5c1f1aab5f930` | question servie |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/pieces/source-gu-krenn-scheurer-v1.json` | `b8e0ccbc2b250a3cdeec3587e5d1e7a33766aa4a8e37a4dfc474f14cfccea15a` | source du substitut Gu-Krenn |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/autorite_factice_scheurer_v1.sh` | `083b3031344ff158ae763e33dd0275db41567cf3f68e4debde8087526d110698` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/faux_mandataire_tls_scheurer_v1.py` | `3c33de3998e27b294d73896e0a61c1e249b4ea1e5ddf67dedb4966aaa8f26057` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/repetition_complete_scheurer_v1.sh` | `6a45fccdbb044f41fe9162aa36085ef2d2cf2f931bbebc31512074a0fe3787bf` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/repetition/repetition_complete_scheurer_v2.sh` | `ed8fa47e7e13f1148d2c2d8e75114f274c65d6e3af5b0c3bcf7c0f4d2db3dd16` | pièce |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/test_course_scheurer_v1.py` | `3288dca6cfeb7e349e26a90ee6f97fb581489bd2c951b66d07ab7446f26e71ac` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/test_course_scheurer_v2.py` | `d90908f27edf96b503f400074d2bbead496a21a4752accd1d4fde415f7ac5cb7` | génération |
| `donnees/course-scheurer-v1/orchestrateur/scheurer/trace_agregee_course_scheurer_v1.py` | `1815d1b5cbce182b6c6a280de493baa4cdcabb7c9c5759cfa6d9f750d6ff331b` | trace agrégée |

## 9. Traitement de la contre-lecture du brouillon 1 (par session-depot, version scellée)

| Constat | Gravité | Traitement |
|---|---|---|
| CLS2-01 la fiche citait la R-486 à contresens ; la variante sert à d'autres lignées une question refusée par Opus et Fable | bloquant (de règle) | § 1 récrit avec le sens exact de la R-486 et de la R-468 (5). **Décision de session-depot (R-1170)**, prise après lecture du texte servi (question `edb1d5f1…`, pièce `2d0e60fc…`) : question publique du mentor sur une tendance d'échelle du désalignement ou de la surveillance, faits de papiers publiés, règle d'intégrité qui interdit tout mode d'emploi pour tromper un moniteur ; le fond n'est pas dangereux, le double refus est très probablement un faux positif ; servir ce texte à Argon, Kimi et Astra ne fait rien produire à Claude et ne vise aucun contenu dangereux : ce cas diffère de la R-486. Mot direct de Lazar sur ce point : « oui : Scheurer à trois espèces, Ibrahim à cinq ». La note de retrait est levée par une note scellée neuve |
| CLS2-02 auto-évaluation d'Astra non rapportée à part | mineur | déclaré : dans le rapport de la fille, les notes données par Astra juge aux fiches d'Astra proposeur sont comptées à part de celles données aux autres espèces (comptes seulement, sans lecture des textes) ; le classement ne se lit pas comme un jugement indépendant |
| CLS2-03 premier run cité sans l'empreinte de son rapport ni sa réserve | mineur | corrigé (§ 1 : `6b2da5f5…`, refus de Fable lu au statut du relais seulement) |
| CLS2-04 Argon tient la moitié des juges et lecteurs, jamais éprouvé comme juge (4 000 jetons au plus) | mineur | déclaré : point de rupture le plus probable ; une réponse tronquée compte comme un échec du rôle (§ 3.4) ; trois échecs consécutifs ou C13 : arrêt sans fiche, **aucune relance** |
| (ajout) numéro de la ligne de GO | — | la GO-15 a été prise par la relance Colognese-Ward : cette variante passe sous `GO-2026-11-03-17` (130 USD), partout dans ce texte |
