# Fiche de lancement — course d'idéation sur la question des mentors Feng et Jang, variante sans Claude (kit v3) — brouillon 1

Rédigée par un sous-agent de session-depot le 3 novembre 2026, 14:59 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : Jang-Feng v3
(branche `outils/course-jang-feng-v1`), au-dessus du kit v2 (`9f9ad98e`, gelé) ; la fiche scellée v2 (`docs/notes/ideation-organisme-v1/course-jang-feng-v1/fiche-lancement-course-jang-feng-v1.md`) reste celle des
cinq variantes v1 et v2, inchangées.

Contre-lecture : <<EMPREINTE_RAPPORT>>

## 1. Pourquoi cette variante, sources, mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- Constat de session-depot (son dernier message) : la course Scheurer en variante sans Opus s'est arrêtée en nœud C13 après la
  proposition, sans aucune fiche ; le relais Claude est au statut REFUS (Fable 5.1, seul proposeur Claude, a très probablement
  refusé la question). Les deux variantes sans Opus de Jang-Feng gardent Fable (proposeur, aiguilleur, juge, lecteur) : elles sont
  fragiles aussi, la pièce Feng et Jang partageant des sources avec la pièce Scheurer (fiche v2, § 2). La variante neuve n'emploie
  **aucun modèle Claude**.
- Pièces servies et règles : celles du kit v1, inchangées (question `d68c6c5c…`, deux sections ; pièce Feng et Jang `1f423643…` ; nos
  résultats `d6fa8011…` ; juge du n° 419 plus K4 ; garde lexicale d'Ibrahim entière).
- Mot de Lazar, **direct** (R-1149) : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de plafond ». Ligne
  de GO : **`GO-2026-11-03-12`, 198 USD** (plafond technique S17, pas un plafond de Lazar), déjà inscrite ; passée au lanceur comme
  `GO_ID` et comme deuxième argument (le lanceur ne vérifie que cette ligne, dont le montant doit être le S17 de la configuration).

## 2. La variante et sa place dans la règle de lancement

| Configuration | Proposeurs | Aiguilleur | Juges (unanimité) | Lecteurs | Metteur | S17 | GO |
|---|---|---|---|---|---|---|---|
| `configuration-course-jang-feng-v1-sans-claude.json` (`f05d9016ec829488f824df07201ac081a10b68ff8b5c6a106fc26418a4f78c18`) | Argon, Kimi, Astra | Astra | Astra, Argon | Astra, Argon | Astra | 198 | `GO-2026-11-03-12` |

**Second repli, déclaré d'avance** (règle de la fiche v2 complétée) : premier run en cinq espèces si Argon est libre, sinon avec
Kimi ; si Opus refuse, repli dans un dossier de run neuf en `sans-opus-argon` (GO-13) ou `sans-opus` (GO-12) ; **si Fable refuse
aussi** (C13 ou trois échecs consécutifs d'un rôle Fable), la course s'arrête, rien n'est rejoué à Fable (R-486), et l'on relance
dans un **troisième dossier de run neuf** en `sans-claude` (GO-12). `sans-claude` peut aussi être le **premier run**, si Lazar le
décide. Ce repli est déclaré ici : ce n'est pas un écart.

**Répartition, au plus près d'Ibrahim** (celle du kit Scheurer v2, acceptée par session-depot) : chaque rôle de Claude passe à
Astra (aiguilleur, premier juge, premier lecteur, metteur), chaque rôle d'Astra passe à Argon (second juge, second lecteur) ; Kimi
reste **proposeur seulement** (R-1155). Le relais 8806 **ne démarre pas** ; aucune clé Anthropic n'est exigée ; le contrôle d'avant
course ne joue que les modèles employés. Lanceur : `jangfeng/lancer-course-jangfeng-v3.sh` (accepte les six configurations ; pour
les cinq autres, son comportement est celui du lanceur v2).

## 3. Déclarations et écarts

1. **Aucun juge de la famille Claude** ; juges et lecteurs ne sont que **deux lignées**, Astra et Argon, et **Astra est aussi
   proposeur** (et aiguilleur et metteur) : les sorties des deux juges sont rapportées à part.
2. **Lecteurs d'autres lignées** (Astra et Argon au lieu de Claude et Astra) : étiquettes non comparables d'une course à l'autre.
3. **Plafond propre du relais Argon : 20.7 USD**, au-dessus de la règle « Argon ≤ 10 USD » (accepté par
   session-depot pour la variante sans Claude de Scheurer ; même raison ici) : Argon est second juge et second lecteur, part au pire
   cas 17.1963 USD (64 appels au plan, contrôle compris).
   **La dépense d'Argon est lue au registre cumulé à la fin de la course.**
4. **S17 = 198 et non 130** : la règle du kit v2 (S17 = le plus grand de 198 et de l'entier supérieur à 1,2 × le pire cas) garde la
   ligne GO-12 déjà inscrite ; 198 ≥ 1,2 × 107.88 = 129.46 (calcul). Le relais Astra prend le reste de
   S17 (175.3 USD), au-dessus de sa part au pire cas (89.8938 USD).
5. Argon répond aux rôles courts avec au plus 4 000 jetons de sortie ; une réponse tronquée compte comme un échec du rôle.
6. Le reste est celui des kits v1 et v2 : aucun témoin planté ; deux bras ; six fiches par proposeur ; consignes, liste fermée et
   source identiques ; garde lexicale identique ; exemples de témoin de K4 et axe `comparaison_a_la_boite_noire`, choix du rédacteur.
7. Code (plus petit changement, fichiers neufs v3, comme Scheurer v2) : jeu de rôles par variante, metteur compris ; fournisseurs
   exigés = ceux des proposeurs et des rôles ; réglages Claude exigés seulement si Claude est employé ; borne propre des relais par
   variante ; reste de S17 au relais Astra sans Claude ; le lanceur shell ne démarre Claude, n'exige sa clé et ne le contrôle que si
   la configuration l'emploie.

## 4. Devis (`jangfeng/devis-course-jangfeng-v3.txt`, `a0107b24ccb472295f0832935d3558d7eb2457fab93408fb647249b59acd4fbc`)

- Appels : 161 de course + 3 contrôles ; attendu **18.07 USD** ; pire cas
  **107.88 USD** ; S17 = 198 ; arrêt d'étape 178,2.
- Par fournisseur (attendu / pire cas) : Astra 11.49 / 89.89 ;
  Argon 6.36 / 17.20 ;
  Kimi 0.22 / 0.79.
- Relais : Astra 175.3 USD (201 appels au plus) ; Argon 20.7 USD
  (133) ; Kimi 2.0 USD (9) ; marge d'appels 2 × plan + 5 ; une fiche
  de plus coûte 4 appels Astra et 3 appels Argon : **23 fiches de trop tolérées** (calcul).
- Plafonds de session : proposeur 3,5 ; aiguilleur 0,9 ; juge 0,9 ; lecteur 0,9 ; fusion 3,5. Course à blanc v3 : nombre d'appels
  identique au plan dans les six variantes (`jangfeng/course-a-blanc-jangfeng-v3.txt`, `bbab059d598492a29ee9aa7279145f39383301d8ddcb065d8c54a4e6957d6883`).

## 5. Liste d'arrêt, lecture

Celles des fiches v1 et v2 (C13 ; trois échecs consécutifs d'un rôle, un refus compte comme un échec ; garde de Kimi ; gardes de
dépense ; plafond propre d'un relais ; signal ; codes 124, 6, 7). Tout arrêt après la proposition ne rend ni fiches ni classement.
Lecture au protocole des « mentors du soir », par extension ; le rapport dit que la course a tourné sans aucun modèle Claude.

## 6. Gardes éprouvées et non éprouvées

66 essais (`jangfeng/test_course_jangfeng_v3.py`, gelé ; dont : aucun Claude dans la configuration, rôles attendus, artefacts
« fournisseur Claude ajouté » et « metteur Claude » refusés, lanceur sans relais Claude, ligne de GO au S17, configurations v1 et v2
inchangées) ; douze mutations, toutes détectées (`jangfeng/resultat-mutations-jangfeng-v3.txt`,
`6633e2b27d9d874d78570e23d26fe7305c07ac116f8ac64412b1cf86e52b7da5`) ; répétition v3 à **8 fiches par proposeur** : cinq essais conformes
(`jangfeng/repetition/resultat-repetition-jangfeng-v3.txt`, `e83f6660aa5120eaec75f1944246ea20b121c35e8ffbd546a8116f03941a1526`) ; course
complète au bout (code 0, 24 fiches, 8 fusions ; Astra 122 appels sur 201, Argon 82 sur 133, Kimi 2 sur 9 ; aucun appel vers
l'interface Anthropic) ; `kill -TERM` : code 130.
Non éprouvés : Argon et Astra comme juges et lecteurs réels ; ligne de GO réelle pour ce run.

## 7. Commande exacte (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-jang-feng-v1/orchestrateur/jangfeng
mkdir -p /home/user/runs-course-jang-feng-v1
RUN=/home/user/runs-course-jang-feng-v1/run-$(date -u +%Y%m%d-%H%M)-sans-claude
GO_ID=GO-2026-11-03-12 nohup bash lancer-course-jangfeng-v3.sh lancer \
  GO-2026-11-03-12 configuration-course-jang-feng-v1-sans-claude.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
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
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/EMPREINTES-orchestrateur-course-jang-feng-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `53f1c79ecad0b4de60651af12d75c59349f3b73cde63cf006c9f1ab04bb3852e` | vérification de la copie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/calcul_devis_course_jangfeng_v1.py` | `8a43ffba4ffdbdfcc6e9bbd0b09773c1af7e01763d1bbd292c5bc01d1887f7bf` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/calcul_devis_course_jangfeng_v2.py` | `bcc1423ace71d8cd6519203957b280c133217b3f685a8529ac2d64b8ad6d56a7` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/calcul_devis_course_jangfeng_v3.py` | `17294a8e83037766f018aa5358a6250de2ec540a4567aefaa23637b9973bd4b7` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/commande_claude_jangfeng_v1.py` | `67e31e04b69d6ba65334acd8ee7d62453e581a16775748f8301927b748bf0396` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-avec-kimi.json` | `b3501965b7054685bbf2722495854ebfccf2144781f4b5678fb258c05c9ead15` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-cinq-especes.json` | `073528ebe0d361a5158027080b75454fe4000fca03c9e77d0f2b9682b49e575c` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-claude.json` | `f05d9016ec829488f824df07201ac081a10b68ff8b5c6a106fc26418a4f78c18` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-kimi.json` | `c4270524b26336c08f9ec2625d612750f651d554ea17db16e5ac54931c587bf6` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-opus-argon.json` | `b2baa681a4ed94de75fb663194dbc939826b9c82397821ca2eb73133bd864fed` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/configuration-course-jang-feng-v1-sans-opus.json` | `fccdac4f71f99ccd12aebe1a7036ab763d518ef12148906ae39895d2cd113698` | configuration |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/construire_consigne_proposeur_jangfeng_v1.py` | `b501130d9a6bef70cc0b1ed647724f31f12a54fa13fa8f52b4ea14d87800e18d` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course-a-blanc-jangfeng-v1.txt` | `767dcd340162db6a04b3b1aa8d5e17c4ca695a7740bff007e9410f0b2149a2d2` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course-a-blanc-jangfeng-v2.txt` | `9f580bf4d0f9e2e765f40373bd8b2b53d786dae07f344f1749f35693fac51878` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course-a-blanc-jangfeng-v3.txt` | `bbab059d598492a29ee9aa7279145f39383301d8ddcb065d8c54a4e6957d6883` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_a_blanc_jangfeng_v3.py` | `6da9e200b0174b5f7ace58c3959c44820bcffa57a7e3d1cf360ed3154af7473e` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_jangfeng_v1.py` | `bcd6e65344e571d9261c04aa738c3321f95cd370961efedc7f73e454c3da5a5f` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_jangfeng_v2.py` | `c50467431a47c98cd9b4c560f950173f8d00bf5ab17bf8a682b3fad5114a98cb` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/course_jangfeng_v3.py` | `d932f0af7b1af4d338d841433004b1aeab48faabdce13f67036f3f2705c04f71` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v1.json` | `62c43f596c7d99a16d140f7cc382bcfe8a55546a79bf985aa9caa91942aafe17` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v1.txt` | `b32042190908cfabe987ad1bdbb0546d8a43a71aa82809d5af0c01d4f24121ce` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v2.json` | `3380dd95094fd31d3fa792d23a63669e89f239aee6970d26ae9bf5bc33ddfba7` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v2.txt` | `9eeb769e454f0cf59bdabf94a05cee943ee5577d2f71144977fcd4178975ded1` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v3.json` | `39947cd720cb92e7844f75fd6049ccb8d72a9fe9a7a679f1dcf0ebbc61058ef9` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/devis-course-jangfeng-v3.txt` | `a0107b24ccb472295f0832935d3558d7eb2457fab93408fb647249b59acd4fbc` | devis |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer-course-jangfeng-v1.sh` | `0e46449daa19159eee9e7e574ac2f3d4c4abcbb3037429e1574d08db42e5d665` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer-course-jangfeng-v2.sh` | `13d08682ac7c9364a746f8dd193ee9b758fab1b9c5dd252e945da9f7d2bfe8d8` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer-course-jangfeng-v3.sh` | `2fd1eac426da0765be77dddeac7d7c3171d17590e6652e74d19bab25b7230525` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer_course_jangfeng_v1.py` | `37d4abe356a916cc5a332caa8687421969fb5d364cc9e7180488043b6899025d` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer_course_jangfeng_v2.py` | `d273c9cd38ee221f0d88ef63f3002f9727fd35b6f6f4cd9dc2d30baba859b1b2` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/lancer_course_jangfeng_v3.py` | `0a1773bd70cba8084b9497dc12cd5717948b959cd54aecf425b5889f402457af` | lanceur |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/mutations_jangfeng_v1.py` | `a7007635a5f67ec72648ae85e2e744854d837d1bf80680f3d5e49d6a26d3569c` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/mutations_jangfeng_v2.py` | `480daaec3a83f84e8fa590eb384ac567f483e155b8612e27b5061b23d1fa5826` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/mutations_jangfeng_v3.py` | `af6d583c616401ef55457ca35316b99da6881fb5980de9d549776e78c49ac2ea` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/concepts-jangfeng-v1.json` | `60fb405787cf3f3d2988833114f0fcc782767fba930da5e5d4a276593a4a7714` | liste fermée |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-aiguilleur-jangfeng-v1.md` | `f1cd9072f0f911c5a0aa7ac1fdc0b4555d5f19c813566566d83298beeda7fd78` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-juge-jangfeng-v1.md` | `0d8413989ecebc10b8b694687a90a6170f00e5bb40797224879b937b8d2c8497` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-lecteur-jangfeng-v1.md` | `d698aa88f8791f4a4159f26de523a899bcf71e005b4487bbd32491d214c49a38` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-metteur-jangfeng-v1.md` | `93f75632e1e2e364f2f058d6ff79d696e8883b48c67ce485beea7065de4bbd4a` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/consigne-proposeur-jangfeng-v1.md` | `d42df37e03e12e208ca03e19afe1b3c7345c361f2b0991afb6abae7d8134b6b8` | consigne |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/piece-jang-feng-v1.md` | `1f42364322988bf591ead6ce41842dd389ab179b11bc27853d66750ab5196774` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/conv-audit/question-course-jang-feng-v1.md` | `d68c6c5ca567c2a867c9a0eb0e64d7b7340af0414e0f382c19416d67ab63c10e` | question servie |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/pieces/source-gu-krenn-jangfeng-v1.json` | `0bac077695d20cf424e988d57ceb5eeb857c1d7c815ecddfb7b40f15a60b4b97` | source du substitut Gu-Krenn |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/autorite_factice_jangfeng_v1.sh` | `2a12cec752b7e76d3200a72eb485eaed4c98f01705830ffb5422a84f55a5751d` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/faux_mandataire_tls_jangfeng_v1.py` | `6da0dfe69afa948e79fdf7f97e3a47404d220261b659ae2e7a5d085fc7ac8fb1` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/repetition_complete_jangfeng_v1.sh` | `0864a1febc2bce2997b9d48e064baef58d897ef277e651646db5c50a6bd399ed` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/repetition_complete_jangfeng_v2.sh` | `2632e1c2d516eae9751b4459f778241e612c66fb916c6ca262eccbb025938f46` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/repetition/repetition_complete_jangfeng_v3.sh` | `6f4e421b6343934eff9701874ffe1413b68ac85c30bb925edb76a1b063af7e72` | pièce |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/test_course_jangfeng_v1.py` | `3745fbc9d585424067b944a228eddcb2f3243e64cc9874a361c3f086216a9fdb` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/test_course_jangfeng_v2.py` | `1bd968e2c098626944de3af8d53d24ee83e795a6f8271cb02ae1053c86b4b4f1` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/test_course_jangfeng_v3.py` | `0efae841d2ea8e4d6d3024d85b0e1377870698bb12081a2d96b8141b89c77093` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/jangfeng/trace_agregee_course_jangfeng_v1.py` | `23289dc03915b9c0447cdeb2017f5c896453566585a6a6184b0466889998d662` | trace agrégée |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-jang-feng-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-jang-feng-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |
