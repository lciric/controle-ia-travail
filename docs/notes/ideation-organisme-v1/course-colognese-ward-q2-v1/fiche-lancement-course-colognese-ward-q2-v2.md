# Fiche de lancement — course d'idéation sur la question 2 des mentors Colognese et Ward — v2 scellée (kit v2, variantes sans Opus)

Version scellée écrite par session-depot le 3 novembre 2026 (heure lue par `date -u` à 15:21:27) : brouillon 2 (`247b76c755f7025b56b9c970604c4280d723fc560be942435f2155bf4a0e28e0`) avec les quatre constats mineurs de sa contre-lecture traités au § 9 ; aucun code, aucune configuration, aucune pièce changés. Rédigée par un sous-agent de session-depot le 3 novembre 2026, 15:16 UTC (`date -u`). **Brouillon** : session-depot le fait
contre-lire par un lecteur neuf (R2), puis en écrit la version scellée sous un nom neuf (R12), qui cite l'empreinte du rapport à
la ligne ci-dessous. Le lanceur exige ce texte scellé, sans marqueur de remplissage, citant l'empreinte de sa contre-lecture, et
dont la table « Pièces gelées » couvre ce qu'il nomme. Aucune dépense, aucun appel réel pour l'écrire. Kit : Colognese-Ward Q2 v2
(branche `outils/course-colognese-ward-q2-v1`, au-dessus de `f56beeee`), sur le modèle exact du kit Jang-Feng v2 ; la fiche
scellée v1 (`docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/fiche-lancement-course-colognese-ward-q2-v1.md`,
`cd4f53a5…`) reste celle des trois variantes v1, inchangées.

Contre-lecture : `docs/notes/ideation-organisme-v1/course-colognese-ward-q2-v1/contre-lecture-fiche-lancement-course-colognese-ward-q2-v1-brouillon2.md`, `6f586bd05b8af953dd8c0c66f0ff5b1aef383094dff1c5b25ecffe1620c35220` (« scellable après quatre corrections mineures », aucun bloquant, aucun majeur).

## 1. Le premier run, arrêté ; sources ; mots de Lazar

- **Course NON décisive** : matière à réflexion pour Lazar ; aucune porte, aucune revendication, aucun chiffre opposable (R7).
- **Premier run** (variante cinq espèces, `GO-2026-11-03-11`) : arrêté en nœud C13 après la proposition, **sans aucune fiche**.
  Sortie : branche `donnees/course-colognese-ward-q2-v1-run`, commit `53baefe6` ; rapport de la fille
  `rapport-course-colognese-ward-q2-v1.md` (`00535656658447b9a99a0e640a63ef4124c117a45c495abdab318cb936cd8d02`, compagnon vérifié),
  seul fichier lu de cette sortie. Selon ce rapport : relais Claude, Opus au statut **REFUS**, Fable OK ; Argon, Kimi et Astra ont
  répondu ; dépense réglée 2,729272 USD (registre). **Réserve** : le refus d'Opus n'est lu qu'au statut du relais, pas au journal de
  proposition (non lu) ; le rapport attribue aussi 6 fiches « refusées au format » sans les rapporter à une espèce.
- Fable n'ayant pas refusé, un repli sans Opus est permis (session-depot : R-1161 n'exclut que le refus des deux modèles Claude).
  Le refus d'Opus n'est pas rejoué à Opus (R-486).
- Spécification et pièces : celles du kit v1, inchangées (spécification `711fcf52…` ; question `06d83795…`, deux sections ; pièce
  Colognese et Ward `7533e4b5…` ; nos résultats `d6fa8011…` ; juge du n° 419 plus K4 ; garde lexicale sans « openai »).
- Mot de Lazar, **direct** (R-1149) : « go courses Scheurer, Colognese-Ward Q2, Jang-Feng, dans cet ordre ; pas de plafond ». Lignes
  de GO (plafonds techniques S17, aucun n'est un plafond de Lazar), une par variante neuve, inscrites par session-depot
  sur `main` à `c266f6a2` : **`GO-2026-11-03-15`, 198 USD**, pour `sans-opus` ; **`GO-2026-11-03-16`, 237 USD**, pour
  `sans-opus-argon`. Les trois variantes v1 restent sous `GO-2026-11-03-11` (198 USD).

## 2. Variantes, lignes de GO, règle de lancement

| Variante | Proposeurs | Aiguilleur, juges, lecteurs | S17 | Ligne de GO (`GO_ID` et 2ᵉ argument du lanceur) |
|---|---|---|---|---|
| `configuration-course-colognese-ward-q2-v1-sans-opus-argon.json` (neuve, `9aa94613a196d478…`) | Fable 5.1, Argon, Kimi, Astra | **Fable 5.1**, Astra | 237 | `GO-2026-11-03-16` |
| `configuration-course-colognese-ward-q2-v1-sans-opus.json` (neuve, `696b9e97e51143e7…`) | Fable 5.1, Kimi, Astra | **Fable 5.1**, Astra | 198 | `GO-2026-11-03-15` |
| `configuration-course-colognese-ward-q2-v1-cinq-especes.json` (v1) | Fable 5.1, Opus 5.5, Argon, Kimi, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-11` (premier run, arrêté) |
| `configuration-course-colognese-ward-q2-v1-avec-kimi.json` (v1) | Fable 5.1, Opus 5.5, Kimi, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-11` |
| `configuration-course-colognese-ward-q2-v1-sans-kimi.json` (v1) | Fable 5.1, Opus 5.5, Astra | Opus 5.5, Astra | 198 | `GO-2026-11-03-11` |

Metteur : Fable 5.1 partout. Claude par un seul relais 8806, `--effort high --reflexion adaptative`, aucune bascule. Lanceur :
`colognese/lancer-course-colognese-v2.sh` (accepte les cinq configurations ; le lanceur v1 reste gelé). **Le lanceur ne vérifie
qu'une ligne** : celle de son deuxième argument, égal à `GO_ID`, passé en `--go-attendu` au lanceur Python, dont le montant doit être
exactement le S17 de la configuration (un mauvais appariement est refusé avant tout appel, essai `test_v2_go_attendu_par_variante`).

**Règle de lancement, déclarée d'avance.**
1. **Second run** (le premier est arrêté, § 1), dans un **dossier de run neuf** : `sans-opus-argon` si Argon est libre au départ
   (aucun tour ni autre course ne l'utilise ; session-depot le vérifie ; le refus de port pris ne voit que l'hôte local), sous
   `GO-2026-11-03-16` ; sinon `sans-opus`, sous `GO-2026-11-03-15`.
2. **Si Fable refuse à son tour** (C13 à la proposition, ou trois échecs consécutifs ou C13 à un rôle de Fable), la course s'arrête
   **sans aucune relance** (R-1161 : refus des deux modèles Claude ; rien n'est rejoué, ni à Fable, ni à d'autres modèles).
3. Chaque run a son registre cumulé et son S17 ; la dépense du premier run (2,729272 USD) reste au sien.

Contrôles d'avant course : le lanceur contrôle toujours Opus et Fable (« réponds seulement par le mot OK », sans la question), y
compris dans les variantes sans Opus : un appel d'environ 0,003 USD, qui ne porte pas la question.

## 3. Déclarations

1. **Aucun témoin planté**. Juge, aiguilleur, lecteur, metteur, champs, axes, bras, liste fermée, source, garde lexicale, consigne
   du proposeur : ceux du kit v1 (fiche v1, § 3), consignes gelées à leurs empreintes.
2. **Fable aux rôles d'Opus** (aiguilleur, premier juge, premier lecteur) dans les deux variantes neuves : Fable est aussi
   proposeur ; les sorties des deux juges (Fable, Astra) sont rapportées à part.
3. **Plafonds techniques S17, par variante** : le plus grand de 198 et de l'entier supérieur à 1,2 × le pire cas de la variante
   (calcul). `sans-opus` : 198 (1,2 × 159,53 = 191,4) ; `sans-opus-argon` : 237 (1,2 × 196,92 = 236,3). Fable aux rôles d'Opus coûte
   plus cher (10 / 50 contre 4 / 20 USD par million) : d'où le pire cas plus haut. Relais : `sans-opus` Claude
   130.7, Astra 65.3, Kimi 2.0 ; `sans-opus-argon` Claude
   148.3, Astra 83.7, Kimi 2.0, Argon 3.0 (USD). Plafonds de
   session des variantes neuves : aiguilleur 0,9 (Fable, pire cas 0,8465) ; ceux des configurations v1 sont inchangés.
4. **Marge d'appels** : 2 × plan + 5 ; fiches en trop tolérées (calcul) : `sans-opus` 23 (Claude 203 pour 99 au plan, Astra 133 pour
   64) ; `sans-opus-argon` 29 (Claude 251 pour 123, Astra 169 pour 82). Au-delà : arrêt à l'étape des étiquettes, sans fiche.
5. **Risque de refus de Fable** : Opus a refusé cette question ; Fable, même famille, l'a acceptée au premier run (proposeur, statut
   OK au relais) ; il ne l'a éprouvée ni comme aiguilleur, ni comme juge, ni comme lecteur. Un refus de Fable arrête la course (§ 2.2).

## 4. Devis (`colognese/devis-course-colognese-v2.txt`, `bbf02d2cd301d3d54fccaa5f97f7dbe4084e5765a3df2e9769b4bbb2111a3c80` ; le devis v1 reste gelé)

| Variante | Appels (course + contrôles) | Attendu | Pire cas | S17 | Part Kimi (att. / pire) | Part Argon (att. / pire) |
|---|---|---|---|---|---|---|
| sans Opus, avec Argon | 204 + 5 | 22,58 USD | 196,92 USD | 237 | 0,22 / 0,79 | 0,21 / 1,72 |
| sans Opus | 161 + 4 | 18,37 USD | 159,53 USD | 198 | 0,22 / 0,79 | — |
| cinq espèces (v1, premier run) | 247 + 5 | 19,03 USD | 164,64 USD | 198 | 0,22 / 0,79 | 0,21 / 1,72 |
| avec Kimi (v1) | 204 + 4 | 16,17 USD | 139,47 USD | 198 | 0,22 / 0,79 | — |
| sans Kimi (v1) | 161 + 3 | 13,30 USD | 115,24 USD | 198 | — | — |

Hypothèses : celles du devis v1. Course à blanc v2 : nombre d'appels identique au plan dans les cinq variantes
(`colognese/course-a-blanc-colognese-v2.txt`, `2cf69798d3c22ca44ab925a9f04c258dc5c9c0f555a369e7839f70913c23b5fb`).

## 5. Liste d'arrêt, lecture

Celles de la fiche v1 (C13 ; trois échecs consécutifs d'un rôle, un refus compte comme un échec ; garde de Kimi ; gardes de
dépense ; plafond propre d'un relais ; signal ; codes 124, 6, 7). Tout arrêt après la proposition ne rend ni fiches ni classement.
Lecture au protocole des « mentors du soir », par extension ; le rapport dit que le second run a tourné sans Opus.

## 6. Gardes éprouvées et non éprouvées

57 essais (`colognese/test_course_colognese_v2.py`, gelé ; dont : les deux variantes neuves, rôles Fable, empreintes inchangées des
trois configurations v1, appariement de la ligne de GO au S17) ; dix mutations, toutes détectées
(`colognese/resultat-mutations-colognese-v2.txt`, `b0fc658112036d3ec491503b122cced6504a24fc2a0d12bcd2398961ae10c93b`) ; répétition v2 derrière de faux
amonts à **8 fiches par proposeur** : cinq essais conformes (`colognese/repetition/resultat-repetition-colognese-v2.txt`,
`88bf49ee1fa22370f10877329baee338b30a7efa4fa403a3bae82062f32abd11`) ; `sans-opus-argon` au bout (code 0, 32 fiches, 8 fusions ; Claude 155
appels sur 251, Astra 106 sur 169) sous une ligne factice à 237 ; `kill -TERM` (code 130), contrôle en échec (code 3) et plafond de
session bas (code 2) sur `sans-opus` sous une ligne factice à 198.
Non éprouvés : Fable comme aiguilleur, juge et lecteur sur cette question ; lignes de GO réelles GO-15 et GO-16.

## 7. Commandes exactes (en arrière-plan ; dossier du run NEUF, hors du clone)

```
cd /home/user/controle-ia-travail/donnees/course-colognese-ward-q2-v1/orchestrateur/colognese
mkdir -p /home/user/runs-course-colognese-ward-q2-v1
RUN=/home/user/runs-course-colognese-ward-q2-v1/run-$(date -u +%Y%m%d-%H%M)-sans-opus
```
Argon libre :
```
GO_ID=GO-2026-11-03-16 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-colognese-v2.sh lancer \
  GO-2026-11-03-16 configuration-course-colognese-ward-q2-v1-sans-opus-argon.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```
Argon pris :
```
GO_ID=GO-2026-11-03-15 PY_RELAIS_CLAUDE=/home/user/venv-relais-claude/bin/python nohup bash lancer-course-colognese-v2.sh lancer \
  GO-2026-11-03-15 configuration-course-colognese-ward-q2-v1-sans-opus.json "$RUN" FICHE_SCELLEE RAPPORT_SCELLE > "$RUN.demarrage.log" 2>&1 &
```

## 8. Écarts (à trancher par conv-audit)

Ceux de la fiche v1 (§ 8), plus : (a) second run sans Opus après un refus d'Opus, Fable à ses rôles ; (b) S17 et ligne de GO par
variante ; (c) contrôle d'Opus gardé au départ (« OK », sans la question).

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
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/EMPREINTES-orchestrateur-course-colognese-ward-q2-v1.txt` | `de9b57688cef1cc968f5e5fa94ed4368d0d8eca83f2b34c57a8ba841a535e3cd` | empreintes de la copie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/VERIFICATION-COPIE-orchestrateur-v56-v1.txt` | `0454d253acdc8a89b92f1b898e1caa03dfbf930b97d499f37c0cbf1cb0238c79` | vérification de la copie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/argon/collisionneur_v7.py` | `c9725f025407c3ece3e8c16d19cfdfdec078f084a811f0a3b6ea3209be5d98dc` | relais (appel de l'interface) |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/calcul_devis_course_colognese_v1.py` | `03a2f19ee7eed8b96a66dd207519af4f22ac831c7368a586d372052786e45cd4` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/calcul_devis_course_colognese_v2.py` | `786b3bef2f2f28084a278b3953bd536f2fd812a6930ab0148f14f1d048e00ecd` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/commande_claude_colognese_v1.py` | `a20b91f0fa88c03a2488649a9ba7469c08e2e9986d919d5dc493c98dc5b01bca` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-avec-kimi.json` | `608768c6bec42747d223b59124630ce07a001462f5f85d8018efad713aef34c2` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-cinq-especes.json` | `63e48ad943b60d6381e40b6eec4fcbcf650e52382f86c6f58f2a7997a06e5e22` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-sans-kimi.json` | `a38c6759e9899805405659b0410b77b87101fa7305853e91a1da893517d38518` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-sans-opus-argon.json` | `9aa94613a196d4786e11aac0a0fc73a7117acf0cda5b1bf7adaeae961983beaf` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/configuration-course-colognese-ward-q2-v1-sans-opus.json` | `696b9e97e51143e7b547eeb300e57e6619547562b03e7ab900dfef8d822a5897` | configuration |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/construire_consigne_proposeur_colognese_v1.py` | `49aeb992058902a500b08d55b0b682d144ccb6686ed5bafdbd7dfdda63ab5787` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course-a-blanc-colognese-v1.txt` | `9b7c47c605e16ccf254e2942bb42bb47c8aa495c4624b43df3c87af93d8cb436` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course-a-blanc-colognese-v2.txt` | `2cf69798d3c22ca44ab925a9f04c258dc5c9c0f555a369e7839f70913c23b5fb` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course_a_blanc_colognese_v2.py` | `46e00a0c0d15f94cae29f60cd58bab190343b29985932befc370f57b212b2e75` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course_colognese_v1.py` | `d7ca1db13943fa44833b1235710c7e18cc2ef22ef210e173824ec6fbc9868276` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/course_colognese_v2.py` | `87c29e75475b4e81f11f0dd952c83464bbb0ec66707df0546292128d60b92914` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v1.json` | `882bafa3b8889ee4417a0f928a4fddb09e7864ea911a99455817b8c7153a422e` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v1.txt` | `4d1be7689eea96a704ae5c6206f3e6ec069bef297d83046939353d6314363a54` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v2.json` | `6fe490118221629d097d485e91d33f564b39aef128410257ffe4dcd07357855f` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/devis-course-colognese-v2.txt` | `bbf02d2cd301d3d54fccaa5f97f7dbe4084e5765a3df2e9769b4bbb2111a3c80` | devis |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer-course-colognese-v1.sh` | `5e28568686555107b5d1a3ee74eda811da1c3a03e86857f4ec0c232645582449` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer-course-colognese-v2.sh` | `43ea777e0dac9568801b7399abce7ec7f558343422aa39522d665c7456bfdcbe` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer_course_colognese_v1.py` | `0657794db7f1e564ca0e66c2de2b811844c181077aabf91e532de0c3c51fb39d` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/lancer_course_colognese_v2.py` | `861f0d4a989228a9b6403b3d74722f64f96a90ad59657f06476c930e7b6ff0ab` | lanceur |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/mutations_colognese_v1.py` | `e13d7539542ddee68a10e7f682067e29299ed532ad76de220bc6e54aaa19f695` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/mutations_colognese_v2.py` | `23f9cb6de4f9baed6d43e7c0124d85c2b31657c21708db549c241fcc028cb737` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/concepts-colognese-v1.json` | `0279ff3df2271e8127926f4ebdb7ab854ba9fdf80324f1fbcfbec3730789cbd9` | liste fermée |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-aiguilleur-colognese-v1.md` | `5e2ed12b05b0775917ee777ad2329ce48aee21ef092ec29bf0c5ba071c6f25cf` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-juge-colognese-v1.md` | `d518aad3d86f91174531d96ad9bdde0be362c65a94cfc5ff59cc370825eb99df` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-lecteur-colognese-v1.md` | `6c38ce813e9fa78236375e5b104de394508255f50a31dd94acb226b1db969eaa` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-metteur-colognese-v1.md` | `714ac8dd31b1bf9d2f547ed329eeeb59af2e4084c106fa7a4a901df7d0d1290d` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/consigne-proposeur-colognese-v1.md` | `ca31eddca070fa0ba234b9adb1215c553cdd97806d625b72247e22bab85cf391` | consigne |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/conv-audit_2026-11-03_n419.md` | `75aedf2ea88361e7b76cd990791f445466c17ac4c87943f96da9efcf9266834b` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/piece-colognese-ward-v1.md` | `7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/piece-nos-resultats-v1.md` | `d6fa8011d9b5680d4ec58b262b6440e0e61e9c9987f0ac79a51cb5bca7b27e3c` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/protocole-rapport-mentors-soir-v1.md` | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/question-collisionneur-colognese-ward-v1.md` | `06d837952cfe066a1414710fadda80f2624ac944c1d5c428b9073bb44686d6af` | question servie |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/conv-audit/specification-course-colognese-ward-v1.md` | `711fcf528ec09a2cc031457b8c64093e867c28f95e8344828408f5abb2e16922` | spécification de conv-audit |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/pieces/source-gu-krenn-colognese-v1.json` | `911827cfdcf79b967071c01b3dfd4ea4f4c45a39be130cd8c42d0055a44e1500` | source du substitut Gu-Krenn |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/autorite_factice_colognese_v1.sh` | `7a4a6dd49035d43193dbb1d7855a4f2e67452b78674d8f90024651f3dc71c8a0` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/faux_mandataire_tls_colognese_v1.py` | `e848382595597ddeae26ff276750ccf76abdf14af8ad3b8905523f20ecb6ab99` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/repetition_complete_colognese_v1.sh` | `ea8d434d8e48701806fba42dbb31a1937e26f9c91acb0ee58b425f83b1b5c7da` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/repetition/repetition_complete_colognese_v2.sh` | `630b338bc047c187f735a0318f59d946bad6121953be7a04151a70081d17b82a` | pièce |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/test_course_colognese_v1.py` | `f44882b26d56fb61d135b1be0a8ad4b5164c1900e5e4873ebfadc8e33b877295` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/test_course_colognese_v2.py` | `34a5016e02f3606998f8fe717c24d89c3d56194ac1d5d24bd472944ea2e5de1f` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/colognese/trace_agregee_course_colognese_v1.py` | `a7a92eb68bb608a58e267ebcc4db4fa6d327411a7e16e90033982b49370f8602` | trace agrégée |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/chercher_cles_v1.py` | `5d6f82fc5cc95f9998877852c08835b83df1ba572597303f447cb983cf97cf61` | recherche des clés |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610681ed47bf66fbfef21d583006aa3e09a3147e22227faacd98622b851` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/commande_kimi_v2.py` | `644dbb39003f234db7b5fc295c6b061a0e84720e01ba08322ae1fe7936d9dcbe` | commande |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/nuit/registre_depense_cumulee_v1.py` | `8ba92066b358ffb8206dea9e70251388c30620484fab1ac578778d9f21e578ff` | registre cumulé |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_nuit_v1.py` | `b0506f7eb8ed384d0284b6b3335d93f31fb67c040fa53a932043ab44f1d33286` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_nuit_v2.py` | `5d15660eca9f23b9480cb6bf7a05379859255294d377652231d944170fe69032` | génération |
| `donnees/course-colognese-ward-q2-v1/orchestrateur/pole/course2_v56.py` | `14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1` | génération |

## 9. Traitement de la contre-lecture du brouillon 2 (par session-depot, version scellée)

| Constat | Gravité | Traitement |
|---|---|---|
| CLC2-01 GO-15 et GO-16 dites « à inscrire » | mineur | corrigé : inscrites sur `main` à `c266f6a2` (§ 1) |
| CLC2-02 perte probable des fiches de Kimi | mineur | déclarée : au premier run, 6 fiches refusées au format, très probablement toutes celles de Kimi (R-1155 ; non vérifié au journal de proposition) ; même perte possible ici ; elle ne compte pas comme un arrêt et ne déclenche aucune relance ; rapportée par espèce |
| CLC2-03 le lanceur ne lit que le montant | mineur | déclaré : `sans-opus` passerait aussi sous GO-11 ou GO-14 (198 USD) ; la seule protection est la commande exacte du § 7 (GO-15 pour `sans-opus`, GO-16 pour `sans-opus-argon`), que session-depot écrit dans l'ordre à la fille et qu'elle vérifie avant le lancement |
| CLC2-04 le contrôle d'Opus reste un point de rupture | mineur | déclaré : le lanceur contrôle Opus (« réponds seulement par le mot OK », sans la question) même dans les variantes sans Opus ; un échec de ce contrôle (technique ou refus) arrête la course avant tout appel de course ; dans ce cas, pas de relance sans message de session-depot |
