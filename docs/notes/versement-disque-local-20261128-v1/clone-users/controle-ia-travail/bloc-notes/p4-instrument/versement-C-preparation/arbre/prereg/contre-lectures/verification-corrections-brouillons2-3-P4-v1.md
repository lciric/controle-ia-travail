# Contre-lecture 2 (R2) de P4-instrument — vérification des corrections des brouillons 2 et 3 — v1

## Verdict

**Scellable après corrections.** Trois constats majeurs, dix mineurs. Aucun ne touche le dessein, l'hypothèse ni la
métrique décisive.

- Les onze constats de la contre-lecture 1 (RP-01 à RP-11) et les sept de Gemini (GP4-01 à GP4-07) sont traités dans le
  brouillon 3. Neuf traitements laissent un reste dans le texte (RP-01, RP-02, RP-03, RP-06, RP-08, RP-10, GP4-04,
  GP4-06, GP4-07).
- Rien d'autre n'a changé : chaque différence mot à mot, de 1 à 2 et de 2 à 3, se rattache à un constat, à une question
  du plan ou à un fait neuf du registre.
- Liste neuve de B′ : la longueur et la structure tiennent (mesurées). Je valide « urban », « indoor », « outdoor » ; pas
  « elderly » ni « adult ».
- Les faits de code invoqués sont exacts. La puissance est juste.

Les trois majeurs :

- **VP3-01** : huit lignes du registre des GO, dont GO-2026-10-20-06 et 07, n'ont que quatre colonnes. Le crochet de
  garde gelé, que le lanceur de P3 rejoue avant la création, bloque donc aujourd'hui tout lancement. L'échéance prolongée
  et le plafond par lancement ne se lisent par aucune forme exacte.
- **VP3-02** : l'artefact (i) de l'épreuve de la tolérance (c) est sans effet si l'espace est inséré dans le texte : le
  gabarit de Llama 3.1 rogne les contenus. L'épreuve passerait sans rien éprouver (R5).
- **VP3-03** : « au-dessous » repose sur un plancher dit « symétrique par construction ». Sous l'agrégation par le
  maximum, ce n'est pas vrai : le score de −w est l'opposé d'un minimum, pas d'un maximum.

## Cadre

- Vérificateur : sous-agent neuf. Je n'ai écrit ni le brouillon 1, ni les brouillons 2 et 3, ni la contre-lecture 1, ni
  les traitements, ni P3 (texte, code, lecture, verdict), ni le brainstorm, ni l'addendum 2.
- Texte vérifié : `…/p4-instrument/P4-instrument-v1-brouillon3.md`,
  `2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c` (sceau compagnon égal). Le préfixe `…/` vaut
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- Pièces relues, empreintes vérifiées :
  - brouillon 1 `41e5f035…`, brouillon 2 `ab409206…`, contre-lecture 1 `108a8d1f…` ;
  - traitement R2 `876d1a66…`, traitement Gemini `a61cfd3c…`, plan `093d0b0d…` ;
  - réponse de Gemini 014 `5e6ac970…`, égale au fichier du commit `d943a3c` (clone `…/canal-gemini/depot`) ;
  - entropie `898291ae…`, égale à R-268.
- Dépôt lu en lecture seule, de `0e4164c` à `562fa39` (deux commits arrivés pendant la lecture : R-279, R-280). Arbre
  gelé (`CHEMINS_GELES`) égal à celui de `7a54d43` à `aa0ece4`, `903073d`, `34dbf1d`, `0e4164c` et `562fa39`. Arbre de
  travail propre.
- Lu :
  - la note du brainstorm, les réponses, les objections 1 et 2, la proposition C ;
  - le préenregistrement de P3 (l. 41, 228-236, 352-358) et son verdict ;
  - `registres/decisions.md` (R-217, R-256, R-259, R-261, R-262, R-264 à R-280, N-025 à N-029), `registres/go.md`,
    `registres/depenses.md` ;
  - le code cité : `premier_test_ia/{donnees,entrainement,empans,conditions,run,statistiques}.py`,
    `sondes/{evaluation,familles,temoins}.py`, `harnais/{episode,formats,sondes,modeles,validation_reelle}.py`,
    `environnements/{propositions,lancer_pilote_a}.py`, `.claude/hooks/garde_calcul.py`,
    `docs/procedures/P3-premier-test-v2/{lancer_p3_v1.sh,verifications_p3_v1.py}` ;
  - les clés, sans texte, de `episodes-p3.json`, `sondes-figees.json` et `manifeste.json` ; les noms et formes des
    colonnes de `scores-p3.npz` ;
  - les nombres déjà stockés de `lecture-p3.json` (clés `jeux.*.plancher_*`), sans recalcul ;
  - `puissance-p3-v1.txt` ; ABC l. 83 ; le constat du plancher apparié du projet précédent (R-279).
- Non lus : `prereg/P3-consignes-v1.md` ; le contenu des textes d'action (fichier seulement haché) ; aucune clé.
- Aucune grandeur de P3 ni de P4 calculée sur des données réelles. Trois mesures seulement, hors données :
  - l'encodage des phrases D, H, B et B′ par le tokeniseur de l'agent (`tokenizer.json`, `79e3e522…`) ;
  - le rendu du gabarit sur un message factice ;
  - une démonstration sur données synthétiques (pièces en fin de rapport).
- Validateur `controle_ia.prereg.problemes` : un seul point, attendu (« contre-lecture 2 sans ses deux empreintes »).
- Écrit : seulement dans `…/p4-instrument/verification/`. Aucune commande Vast.ai, aucun service payant, aucune
  écriture git.

## Réponses aux huit points

### 1. Traitement des constats ; décisions écrites ; rien d'autre n'a changé

| constat | traité dans le brouillon 3 ? |
|---|---|
| RP-01 | oui pour la ligne : L10 ne vaut que pour « ni au-dessus ni au-dessous », après les lignes de succès ; réserve en L6 et L7. Réserve discordante pour L8 et L9 (VP3-04). |
| RP-02 | oui dans la forme : L9 « signe inversé », L11 « à cette puissance », « aveugle » qualifié. Seuil fondé sur une symétrie fausse (VP3-03). |
| RP-03 | oui : bras B′, M6b sur B contre B′, B contre H en descriptif, L7 « spécificité non établie ». La garde d'affect de la liste d'arrêt ne nomme pas B′ (VP3-07). |
| RP-04 | oui, juste : présence du jeton de fin lue par `jetons − jetons_notes` ; critère (a) et MC-3 sans tolérance ; hypothèse `<|eot_id|>` déclarée ; artefact testé. |
| RP-05 | oui, juste (point 5) ; libellé à préciser (VP3-13). |
| RP-06 | oui sur le fond (GO-2026-10-20-06 et 07, R-269) ; inopérant en l'état du registre (VP3-01). |
| RP-07 | oui, juste : résumé écrit à tout arrêt ; L3 « s'ils sont calculés » ; L8 « référence non lue ». |
| RP-08 | oui pour le « nul trop propre » ; l'épreuve sur le modèle réel peut être sans effet (VP3-02). |
| RP-09 | oui au brouillon 2 ; à refaire au candidat : R-275 corrige R-266 (VP3-05) ; plages de nombres incomplètes (VP3-11). |
| RP-10 | oui : formes exactes de la révision, de la configuration et du module ; chemin du verdict complété en v2. La ligne de registre exigée reste cherchée en texte libre (VP3-09). |
| RP-11 | oui, juste. |
| GP4-01 | oui, juste : liste en « an », règle de longueur de H, artefact testé ; mesure confirmée (point 2). |
| GP4-02 | oui, juste : C1 au pas 0 en descriptif, graine `d/c1-pas0`. |
| GP4-03 | oui, juste : biais de la séparation repliée exact (σ·√(2/π)) et prudent ; Δ net ; L6 et « Ce que H-P4 n'affirme pas » resserrés. |
| GP4-04 | en partie : fait de conception exact ; rang en descriptif. Le plancher bilatéral annoncé n'est reconnu « haut » que par le quantile 0,95 (VP3-03). |
| GP4-05 | oui : critère (c) révisé dans le Seuil, la garde et les tests ; frontière des 95 % à compter et à tester (VP3-08). |
| GP4-06 | dans la table seulement ; absent de la liste des réserves ; texte de la réserve faux pour un signe inversé (VP3-04). |
| GP4-07 | non écrit : le traitement renvoie à « Métrique (Bras I) ; MC-2 », qui n'ont pas changé (VP3-12). |

- Douze questions du plan : 1, 2, 3, 6, 7, 8, 9, 10 et 12 sont écrites ; la 5 aussi, mise à jour par GP4-01. La 4
  (variante A5 exclue) et la 11 (mesures de conception admises au titre de R1) ne le sont pas. La décision « suite
  complète des tests sur l'instance » non plus (VP3-12).
- Différentiels mot à mot (pièces en fin de rapport) :
  - 1 à 2 : chaque changement se rattache à RP-01 à RP-11, aux questions du plan (1, 2, 6 à 10), ou à deux faits neufs
    (R-266, R-269) ;
  - 2 à 3 : chaque changement se rattache à GP4-01 à GP4-06, à l'en-tête ou à la section « Contre-lecture » ;
  - rien d'autre n'a changé. Trois mises à jour manquent : la garde d'affect pour B′ (VP3-07), la liste des réserves
    (VP3-04), le plan (VP3-10).

### 2. Liste neuve de B′

- Garde d'affect : aucun des cinq adjectifs ne commence par une racine de `RACINES_AFFECT` (`temoins.py` l. 38-40 ;
  règle l. 48-54). La phrase entière non plus.
- Longueur et structure, mesurées (encodage seul, sans jetons spéciaux) :
  - D, H et les cinq phrases en « an » font 14 jetons, 15 entre deux sauts de ligne ;
  - côté B, toutes aussi, sauf « left-handed » (15) ;
  - D et H diffèrent aux positions 5 et 6 (article, adjectif) ; « a tall » et « an urban » aussi ;
  - D et « a tall » ne diffèrent qu'en 6 ; H et « an urban » aussi.
- **L'appariement tient.** B (« a », positif) suit D (« a dishonest ») ; B′ (« an », négatif) suit H (« an honest »).
  Deux jetons changent, aux mêmes places, à longueur égale. La mesure dans le gabarit (MC-1) fait foi.
- Sens :
  - « urban », « indoor », « outdoor » : aucun lien avec l'honnêteté, la morale, les enjeux, le coût ou l'affect.
    **Validés.** « urban » a un emploi euphémique connu en anglais américain, sans lien lexical avec ces cinq domaines ;
    une contamination ne ferait que durcir M6, qui ne peut que restreindre.
  - « elderly » : vulnérabilité, victimes d'escroqueries (« elder fraud »), soins. Liens indirects avec la tromperie,
    les enjeux et l'affect. **Non validé.**
  - « adult » : sens « contenu pour adultes ». Lien avec la morale et la décence. **Non validé.**
- La liste a été écrite par la session. La réponse M6 (`reponses.md` l. 460) veut une consigne « écrite et scellée avant
  le run par un sous-agent neuf ». La liste retenue ici par un vérificateur neuf peut en tenir lieu : « urban »,
  « indoor », « outdoor », dans cet ordre (VP3-07).

### 3. Lignes de lecture L1 à L11

- **Mécaniques** : oui. La première ligne qui s'applique, de haut en bas.
- **Chevauchement** : aucun en pratique. Avec le seuil écrit (1 − quantile 0,95), « au-dessus » et « au-dessous » ne
  s'excluent que si ce quantile vaut au moins 0,5. Avec le quantile 0,05, ils s'excluent par construction (VP3-03).
- **Trous** : deux.
  - Une lecture de M5 en échec n'a pas de ligne : L3 ne dit que « non au-dessus ».
  - Une lecture refusée par une garde du mode décisif n'en a pas non plus. Or « la ligne qui s'applique est toujours
    calculée et écrite » (VP3-06).
- **« Au-dessous » sur un plancher symétrique (`evaluation.py` l. 79)** : non établi.
  - La ligne 79 rend w et −w également probables, rien de plus.
  - Avec le maximum sur les jetons (`harnais/sondes.py` l. 75-76), le score de −w vaut moins un minimum. Donc
    aire(−w) ≠ 1 − aire(w).
  - Démonstration synthétique : aire(w) + aire(−w) va de 0,934 à 1,070 selon les directions ; le quantile 0,05 et
    1 − quantile 0,95 diffèrent (0,488 contre 0,475 dans un cas). L'écart réel est inconnu, sans doute faible.
  - Le seuil doit être le quantile 0,05 du plancher (VP3-03).
- **Le plancher haut ne qualifie que le cas « non au-dessus »** : oui pour la ligne (L10 vaut seulement « ni au-dessus
  ni au-dessous »). Mais le Seuil écrit « C1 non au-dessus d'un plancher haut … (ligne L10) », alors qu'un « au-dessous »
  d'un plancher haut va en L9. Et la réserve « plancher haut » est attribuée à des lignes différentes selon cinq passages
  (VP3-04).
- **Angle mort** : pour C1, le plancher attendu est bilatéral (w et −w). Sa médiane reste près de 0,5. Seul « quantile
  0,95 > 0,80 » peut alors le dire haut. Cas synthétique (d) : 24 % des directions à |aire − 0,5| > 0,15, quantile 0,95
  à 0,691, médiane 0,495, donc « plancher non haut ». Si la sonde n'y est pas au-dessus, la ligne est L11 (« non
  détecté »), alors que des directions quelconques voient le contraste (VP3-03).

### 4. Faits de code

- **Jeton de fin** (`run.py` l. 274-276) : exact.
  - `jetons = len(a.ids)` ; `jetons_notes = max(0, fin − début)` ; `fin = a.fin − 1` si le dernier identifiant est dans
    `fmt.fins`. La différence vaut 1 si l'action finit par un jeton de `fmt.fins`, 0 sinon.
  - `fmt.fins` contient aussi le premier jeton de clôture (`lancer_pilote_a.py` l. 265).
  - Vérifié aussi : si une action de P3 avait fini par un autre jeton que `<|eot_id|>`, sa clôture complète suivait
    (`formats.py` l. 91-93). P4 aurait alors un jeton de moins ensuite. « Contextes suivants décalés d'un jeton » est
    exact.
- **Σ réunit les deux classes** : exact, citation courte.
  - `evaluation.py` l. 72-73 concatène les jetons et prend leur moyenne ; la covariance est l. 74.
  - « Deux classes » vient de `entrainement.py` l. 117-120 (`idx_e`) et l. 80-81 (les deux classes exigées).
  - Le préenregistrement de P3 (l. 228-236) ajoute : Σ de tromperie est de rang déficient (≈ 3 500 jetons pour 4 096
    dimensions) ; les directions vivent dans l'espace des jetons d'entraînement. Cela appuie GP4-04 (VP3-11).
- **Répétition de la phrase à chaque pas** : exact.
  - `propositions.py` l. 266-268 met l'indication sur sa propre ligne, juste avant « Your action: », pour chaque
    (agent, pas) de `indications_privees`.
  - `conditions.py` l. 82 la met à tous les pas.
  - Au pas k, le contexte (`episode.py` l. 217 et 254) en porte k + 1 occurrences.
- Autres citations relues, exactes : `donnees.py` l. 26-27, 53-56, 72-80, 83-95 ; `entrainement.py` l. 39-48, 51-53,
  62-74, 98-111 ; `empans.py` l. 23-38 ; `episode.py` l. 211-217, 252-255, 366-368 ; `run.py` l. 131, 207-215, 218-223,
  237, 443-444 ; `conditions.py` l. 78-79, 116-143 ; `statistiques.py` l. 110-125 ; `evaluation.py` l. 26-37, 40-63.
- Les dix données de la table ont l'empreinte écrite et un sceau égal. La révision `0e9e39f…` est celle du manifeste de
  P3. Les graines `tirage-enjeux`, `decoupage-tromperie` et `decoupage-enjeux` y sont.

### 5. Puissance

- Verdict de P3 (l. 296-299 ; SC-1-01, l. 386) : demi-largeurs 0,0435 = (0,6183 − 0,5313) / 2 et
  0,0444 = (0,5700 − 0,4813) / 2, sur des intervalles à 97,5 %.
- Erreur type = demi-largeur / z(0,9875) = 0,0435 / 2,2414 ≈ 0,0194 : **juste**.
- Aire minimale détectable = plancher + (1,96 + 0,84) × erreur type : **juste** pour la règle de P4 (borne basse de
  l'intervalle à 95 % au-dessus du plancher, puissance 80 %). 2,80 × 0,0194 ≈ 0,054 ; d'où 0,63 à 0,65 pour des
  planchers de 0,572 à 0,596, et ≈ 0,85 pour 0,80.
- Scénario de la simulation : conforme à `puissance-p3-v1.txt` (demi-largeurs 0,024 à 0,038 ; planchers 0,517 à
  0,528).
- Réserves de forme : le quantile du plancher y est traité comme une constante ; et ces chiffres sont une estimation
  pour P4, pas l'aire minimale détectable de P3 (VP3-13).

### 6. Autorité de dépense

- GO-2026-10-20-06 (`go.md` l. 33) : prolonge GO-2026-10-04-08 jusqu'au 2026-11-30, plafond inchangé. Conforme.
- GO-2026-10-20-07 (`go.md` l. 34) et R-269 (`decisions.md` l. 461) : délégation jusqu'au 2026-11-30, indépendante du
  mandat ; préenregistrement scellé et contre-lu ; 10 USD au plus par lancement ; consigné et rapporté. Conforme.
- R-270 (`decisions.md` l. 462) : mandat sans échéance fixe ; dépenses par R-269. Conforme.
- Borne de l'étape 5,41 USD (3,47 + 0,22 + 1,00 + 0,72) : juste, sous 10 USD. Crédit exigé 4,47 à 5,10 USD ; crédit
  relu 11,79 USD (`depenses.md`, 2026-10-20 à 06:07 UTC).
- Mais ces GO sont inscrits sur quatre colonnes au lieu de huit. La garde de calcul bloque, et les règles du lanceur ne
  se lisent pas (VP3-01).

### 7. Garde d'identité ; garde du verdict complété

- Critère (c) révisé : écrit à l'identique dans le Seuil (l. 327-330), la garde (l. 424-427) et les tests
  (l. 452-453). Les deux sondes principales sont parmi les 424 (vérifié : 400 directions de plancher et 30 sondes
  entraînées dans les 430 colonnes de `scores-p3.npz`, dont 6 Mahalanobis hors du fichier léger). « 95 % » se compte :
  403 sondes sur 424 au moins (VP3-08).
- Épreuve (i) : sans effet si l'espace passe par le texte (VP3-02).
- Épreuve (ii) : avec la règle des 95 %, une action échangée du même épisode peut passer (c), si son maximum tombe sur
  des jetons de format communs. Le repli écrit (niveau 2 désactivé, réserve) est prudent. À savoir, sans correction.
- Garde du verdict complété (Plan 2, liste d'arrêt, tests) : chemin v2, sceau, ligne du registre. Conforme à R-262 et
  R-264. La ligne du registre se cherche en texte libre (VP3-09).

### 8. Constats nouveaux

- **R1** : tenue. Les mesures de conception portent sur des propriétés des entrées, sans score ; la mesure de l'encodage
  par la session (R-274) aussi. Un a priori connu avant le candidat n'est pas déclaré : le plancher apparié du projet
  précédent (R-275, R-279 ; VP3-05).
- **R3** : tenue. Liste fermée, un seul run, aucun relancement. Les trois descriptifs neufs ne font jamais une ligne. Le
  nombre de comparaisons contre un plancher (sept) est rapporté.
- **Pare-feu** : tenu. Aucune aire de P3 sur ses actions, aucune condition instruite lue, rien ne règle T0.7. Un
  libellé de la puissance est à resserrer (VP3-13).
- **Coût** : B′ ajoute 60 passes et 600 actions notées, ≈ 2,3 minutes au rythme de P3 (108,4 s pour 240 passes ;
  ≈ 444,6 s pour 2 400 actions). « ≈ 3 minutes » est juste. L'épreuve ajoute deux passes. Attendu 1,5 à 2,3 USD, borne
  5,41 USD : juste.
- **Descriptifs neufs** :
  - C1 au pas 0 : bien défini. Chaque bloc de tâche porte une ligne D et une ligne H : aucun tirage dégénéré possible.
  - Δ net : bien défini. Il dit « séparations repliées des 200 directions » ; M6a et B contre H ne le disent pas
    (VP3-11).
  - Rang de la sonde : les ex aequo ne sont pas réglés, alors que la concordance des directions peut saturer à 1
    (VP3-11).

## Constats (le plus grave d'abord)

### VP3-01 — majeure — le registre des GO bloque le lancement ; les règles de dépense ne se lisent pas

- **Où** : en-tête, « GO et dépense » (l. 42-49) ; Plan d'analyse, point 7 (l. 393-406) ; Liste d'arrêt (l. 534-537) ;
  `registres/go.md` l. 28-35 ; plan, section 4.
- **Problème** :
  - Le registre impose huit colonnes (`go.md` l. 4). GO-2026-10-20-01 à 08 n'en ont que quatre : ni plafond, ni
    échéance, ni « accordé par », ni référence en colonne.
  - `garde_calcul.py` (`lire_go`, l. 54-59) bloque dès qu'une ligne de GO n'a pas huit colonnes, quel que soit le GO
    cité. J'ai appelé sa seule lecture du registre, sans lancement : « registre GO mal formé ligne 28 : 8 colonnes
    attendues, 4 trouvées », code 2.
  - Le lanceur de P3 rejoue ce crochet avant la création (`lancer_p3_v1.sh` l. 297-300, sous `set -euo pipefail` et un
    piège ERR, l. 36-37). Le plan garde cette étape. Le lanceur de P4 s'arrêterait donc avant la création.
  - Le crochet est dans l'arbre gelé. Il ne peut pas changer sans rompre « arbre égal à `7a54d43` ». Même blocage pour
    P3b et pour le pilote du papier C.
  - Le crochet ne lit que la ligne du GO cité. GO-2026-10-04-08 échoit le 2026-11-01 dans sa propre ligne. La
    prolongation ne servirait qu'à un GO-2026-10-20-06 cité lui-même ; la liste d'arrêt l'interdit (« GO autre que
    GO-2026-10-04-08 »).
  - « Refuse tout GO échu (… l'échéance du GO cité) » vise GO-2026-10-20-07, qui n'a pas d'échéance en colonne. Le
    plafond de 10 USD n'y est pas en colonne non plus. La chaîne de P3 n'admettait que des formes exactes, sans
    recherche en texte libre (`verifications_p3_v1.py` l. 12-15, 47-50, 76-78).
  - « Révocation présente » n'a pas de forme. Le plan ne fixe que GO-2026-10-04-08 et R-262 (l. 110) ; ni
    GO-2026-10-20-06, ni GO-2026-10-20-07, ni R-269.
- **Correction** :
  - Avant le candidat : remettre les huit lignes au format du registre, contenu inchangé (plafond, échéance, « Lazar »,
    référence, tirés du texte de chaque ligne). Consigner cette correction de forme par une ligne R-…. Si la session
    juge que « jamais modifiée » l'interdit : question à Lazar, en une ligne. Puis rejouer la seule lecture du registre
    (`lire_go`) : aucun blocage attendu.
  - Dans le texte, fixer les formes exactes :
    - GO cité dans la commande : GO-2026-10-04-08 jusqu'au 2026-11-01, puis GO-2026-10-20-06 jusqu'au 2026-11-30 ; ou
      écrire que le lancement a lieu avant le 2026-11-01 ;
    - plafond par lancement lu dans la colonne « plafond » de GO-2026-10-20-07 ;
    - révocation : ligne à huit colonnes de type « révocation » qui nomme GO-2026-10-04-08, GO-2026-10-20-06,
      GO-2026-10-20-07, R-262 ou R-269 ; ou ligne R-… qui commence par « **Révocation de R-262** » ou « **Révocation de
      R-269** ».
  - Garder le rejeu du crochet dans le lanceur ; ne jamais le contourner (R5).

### VP3-02 — majeure — l'artefact (i) de l'épreuve de la tolérance (c) peut être sans effet

- **Où** : Garde d'identité, « Épreuve de la tolérance (c) » (l. 431-438) ; Plan d'analyse, point 1.4 ; Tests
  (l. 448-455).
- **Problème** :
  - Le gabarit de Llama 3.1 rogne chaque contenu : `message['content'] | trim` dans le `tokenizer_config.json` du
    tokeniseur cité (`177c7b61…`, même dossier que `tokenizer.json`) ; `empans.py` l. 5 le dit aussi.
  - Un espace ajouté au début du texte du message de l'utilisateur du pas 0 disparaît donc au rendu. Mesuré sur un
    message factice : 51 identifiants dans les deux cas, identiques.
  - Le texte dit « un jeton d'espace inséré au début du message de l'utilisateur », sans dire où : dans le texte ou
    dans les identifiants. Fait dans le texte, l'artefact (i) ne décale rien. Il « passe (c) » sans rien éprouver, et le
    niveau 2 resterait actif sur une tolérance jamais éprouvée. C'est le repli silencieux que R5 interdit ; RP-08 ne
    serait traité qu'en apparence.
  - Le gabarit jouet ne rogne pas (`harnais/modeles.py` l. 52-53) : un test jouet passerait, le modèle réel non.
- **Correction** :
  - Insérer l'identifiant du jeton d'espace (220 dans `tokenizer.json` `79e3e522…`) dans les identifiants du contexte,
    juste après le `<|end_header_id|>` et les deux sauts de ligne du premier message de l'utilisateur, sans passer par
    le gabarit.
  - Garde : à chaque pas, le contexte de l'artefact compte exactement un identifiant de plus que celui du bras I, les
    autres égaux. Sinon : épreuve « non éprouvée », niveau 2 désactivé, réserve écrite.
  - Tests : cas sain, décalage d'un jeton constaté ; artefact, espace mis dans le texte d'un gabarit qui rogne, aucun
    décalage, refus.

### VP3-03 — majeure — « au-dessous » repose sur une symétrie du plancher qui n'est pas acquise

- **Où** : Seuil (l. 309-313) ; Prédiction, P4-C1 (l. 190) ; L9 (l. 506) ; Métrique, « Plancher » (l. 248-256) ;
  Plancher haut (l. 316-321) ; L10 et L11 (l. 507-508).
- **Problème** :
  - Le texte écrit : « le plancher est symétrique par construction, `w` et `−w` également probables, `evaluation.py`
    l. 79 ». La ligne 79 tire w ~ N(0, Σ) : les directions sont symétriques ; les aires ne le sont pas.
  - Avec le maximum sur les jetons (`harnais/sondes.py` l. 75-76) et le biais −w·μ (`evaluation.py` l. 81), le score de
    −w vaut −min_t(w·h_t − w·μ), non −max. Donc aire(−w) ≠ 1 − aire(w), et le quantile 0,05 du plancher n'est pas
    1 − quantile 0,95. La loi des aires n'est symétrique que si celle des activations par jeton l'est autour de sa
    moyenne. Rien ne le garantit (jetons à activations massives).
  - Démonstration synthétique (pièce en fin de rapport) : aire(w) + aire(−w) de 0,993 à 1,012 avec des jetons gaussiens,
    de 0,982 à 1,024 avec des jetons massifs de signe fixe, de 0,934 à 1,070 avec un déplacement plus fort ; quantile
    0,05 à 0,488 contre 1 − quantile 0,95 à 0,475 quand le déplacement ne touche qu'une partie des jetons. L'écart réel
    est inconnu, sans doute faible. L'affirmation reste fausse.
  - Conséquences :
    - le seuil 1 − quantile 0,95 ne compare pas la sonde aux 5 % des directions les plus basses ;
    - « au-dessus » et « au-dessous » ne s'excluent que si le quantile 0,95 vaut au moins 0,5 ;
    - si le plancher était symétrique par construction, « médiane hors de [0,45 ; 0,55] » ne partirait jamais, hors
      bruit ;
    - pour C1, le plancher attendu est bilatéral (le texte le dit, l. 254-256) ; sa médiane reste près de 0,5 ; le
      plancher haut ne se lit alors que par « quantile 0,95 > 0,80 ». Cas synthétique (d) : 24 % des directions à
      |aire − 0,5| > 0,15, quantile 0,95 à 0,691, médiane 0,495 : « plancher non haut ». Si la sonde n'y est pas
      au-dessus, la ligne est L11 (« non détecté »), alors que des directions quelconques voient le contraste. C'est le
      cas que O2-30 voulait écarter. GP4-04 n'est donc traité qu'en partie.
- **Correction** :
  - « Au-dessous » : borne haute strictement inférieure au **quantile 0,05** des 200 aires du plancher, sur les mêmes
    lignes (`numpy.quantile`, interpolation linéaire). Rapporter 1 − quantile 0,95 à côté, sans effet. Retirer
    « symétrique par construction ». Reporter le changement dans P4-C1 (colonne « réfutation »), le Seuil, L9 et les
    tests. « Au-dessus » et « au-dessous » s'excluent alors par construction.
  - Plancher haut, à trancher par la session (les seuils viennent de la note) : ajouter « ou quantile 0,05 au-dessous de
    0,20 », miroir de 0,80. À défaut, écrire que pour C1 seul le quantile 0,95 peut dire le plancher haut, et rapporter
    en descriptif la part des directions à |aire − 0,5| > 0,15.

### VP3-04 — mineure — réserve « plancher haut » : cinq passages discordants

- **Où** : Seuil (l. 316-321) ; Métrique, « Plancher » (l. 256) ; Plan d'analyse, point 5 (l. 389) ; L8 et L9
  (l. 505-506) ; Réserves (l. 510).
- **Problème** :
  - La réserve est attribuée à L6 à L8 (Seuil, point 5), à L6 et L7 (Métrique, liste des réserves), à L6, L7 et L9
    (table). L8 l'a selon deux passages, pas selon trois ; L9 l'a dans la table, pas dans la liste.
  - Son texte, « la sonde les dépasse », est faux en L9 (signe inversé).
  - Le Seuil dit « C1 non au-dessus d'un plancher haut … (ligne L10) » ; la table envoie « au-dessous d'un plancher
    haut » en L9.
  - Un verdict R13 appliquerait des critères gelés contradictoires.
- **Correction** : une règle unique. Plancher haut et ligne autre que L10 : réserve écrite. En L6 à L8 : « le contraste
  est vu par des directions quelconques ; la sonde les dépasse ». En L9 : « le contraste est vu par des directions
  quelconques ; la sonde est au-dessous d'elles, de signe inversé ». En L1 à L5 : aucune. Seuil : « C1 ni au-dessus ni
  au-dessous d'un plancher haut … (ligne L10) ». Mettre à jour les cinq passages.

### VP3-05 — mineure — R-275 et R-279 corrigent R-266, après le brouillon 3

- **Où** : Documents qui font foi (l. 83-85) ; « A priori externe » (l. 196-198) ; registres cités (l. 79-82).
- **Problème** :
  - Le texte écrit « R-266 : aucun plancher à confronter, la branche C3 de la note tombe ». R-275 (vers 11:15 UTC, après
    le brouillon 3) corrige : le projet précédent a un plancher apparié, versé par R-279
    (`donnees/P1-loi-attraction-v1/C4_plancher_apparie_blocC_2026-08-10.json`, `cd44c939…` ; constat
    `C4_plancher_apparie_blocC_2026-08-10.constat.json`, `0b430098…`). Médiane 0,66 (F2) à 0,89 (F1), contre 0,27 sur
    des items disjoints, par une direction commune des différences appariées. La branche C3 redevient possible.
  - R-275 dit aussi que ce fait « appuie l'a priori d'un plancher haut pour C1 ». Cet a priori interne n'est pas
    déclaré ; celui de Gemini l'est.
- **Correction** : remplacer la ligne par R-275 et R-279, chemins et empreintes. Dire que la recette diffère (cosinus de
  champs, permutation du signe) et ne touche pas P4. Ajouter cet a priori au paragraphe « A priori », non opposable.
  Relire et recopier les registres au candidat (au moins R-271 à R-280 et N-029).

### VP3-06 — mineure — deux trous dans la table de lecture

- **Où** : L3 (l. 500) ; « La ligne qui s'applique est toujours calculée et écrite » (l. 493) ; Liste d'arrêt
  (l. 518-519).
- **Problème** :
  - Une lecture de M5 (tromperie) en échec, motif écrit, n'est pas « non au-dessus ». Aucune ligne ne l'attrape, et C1
    serait lu comme si M5 passait. Cas rare (blocs de faits à deux classes), mais le texte ne l'exclut pas.
  - Une lecture refusée par une garde du mode décisif (module, configuration, donnée, entropie, run source) n'a pas de
    ligne.
- **Correction** : L3 : « … non au-dessus de son plancher sur sa validation, ou lecture de M5 en échec (motif écrit) ».
  L1 : ajouter « lecture refusée par une garde du mode décisif (motif écrit) ». Dire que l'attente du verdict complété
  de P3 est un report, pas une ligne.

### VP3-07 — mineure — liste de B′ et garde d'affect

- **Où** : Métrique, « Phrases », B′ (l. 228-233) ; Liste d'arrêt (l. 528-529).
- **Problème** :
  - « elderly » et « adult » ont des liens indirects avec la tromperie, les enjeux, la morale ou l'affect (point 2).
  - La liste a été écrite par la session, non par un sous-agent neuf (réponse M6, `reponses.md` l. 459-461).
  - La liste d'arrêt ne fait passer `exiger_concept_sans_affect` qu'à « l'adjectif de B ». B′ manque depuis le
    brouillon 2.
- **Correction** : liste fermée et ordonnée de B′ : « urban », « indoor », « outdoor », validée ici par un vérificateur
  neuf. Liste d'arrêt : « les adjectifs de B et de B′ passent `exiger_concept_sans_affect` ». Aucun effet attendu sur le
  choix : « an urban » fait déjà 14 jetons.

### VP3-08 — mineure — frontière des 95 % du critère (c)

- **Où** : Seuil (l. 327-330) ; Garde d'identité (l. 424-427) ; Tests (l. 452-453).
- **Problème** : 95 % de 424 vaut 402,8 ; le seuil réel est 403 sondes. Les tests à 94 % (≈ 398) et à 95 % laissent 399
  à 402 sans test. Une erreur d'arrondi ou de comparaison passerait.
- **Correction** : écrire « au moins 403 des 424 sondes légères (95 %, arrondi au-dessus) ». Tester 403 (garde) contre
  402 (exclut).

### VP3-09 — mineure — la ligne du registre qui annonce le verdict complété est cherchée en texte libre

- **Où** : Plan d'analyse, point 2 (l. 362-367) ; Tests.
- **Problème** : « une ligne du registre des décisions qui l'annonce par ce chemin » : toute ligne qui cite le chemin
  passerait, même une ligne qui ne fait que l'attendre. La chaîne de P3 n'admettait que des formes exactes
  (`verifications_p3_v1.py` l. 12-20 ; relecture RCh-01 à RCh-03).
- **Correction** : une forme exacte, par exemple une cellule de décision qui commence par « **Verdict complété de P3
  scellé** » et cite le chemin et l'empreinte. Exiger cette empreinte égale au sceau. Artefact testé.

### VP3-10 — mineure — le plan v1 contredit le brouillon 3

- **Où** : en-tête (l. 28, « plan, 3.1-3.2 ») ; Chaîne de lancement (l. 543) ; `plan-code-et-chaine-v1.md`.
- **Problème** : le texte renvoie au plan pour « détail, scripts et devis ». Le plan est resté au brouillon 1 :
  - `issue_p4` sur « lignes L1 à L9 » (l. 62, 95) ;
  - quatre bras et B seule (l. 60-61, 159) ;
  - « GO accepté : GO-2026-10-04-08 seul », révocation pour R-262 seulement (l. 110) ;
  - « R-217, ou R-185 hors mandat » (l. 125) ; échéance 2026-11-01 (l. 175-176) ;
  - ni l'épreuve sur le modèle réel, ni les descriptifs neufs.
  Le module s'écrit en parallèle (R-278).
- **Correction** : plan v2 (R12), aligné sur le texte, avant le candidat ; ou une ligne au texte : « le texte prime sur
  le plan v1 ; écarts : … ». Donner le texte au rédacteur du module comme seule source.

### VP3-11 — mineure — précision des citations et des nombres (R6)

- **Où** : Métrique (l. 252) ; Nombres de P3 déjà connus (l. 116-121) ; Données lues (l. 98, 101) ; M6a (l. 274-275) ;
  B contre H (l. 285-286) ; rang (l. 289-293) ; mesure préliminaire (l. 235-237).
- **Problème et correction** :
  - Σ : citer `evaluation.py` l. 72-74 (la covariance est l. 74) et `entrainement.py` l. 117-120 et 80-81 (« deux
    classes ») ; ajouter le rang déficient (P3 l. 228-236).
  - « Jeux à contexte changé, de 0,572 à 0,596 » : quatre jeux sur cinq ; mention contre honnête vaut 0,5117 (déjà dans
    O2-02). Le dire, avec les clés.
  - « Maximum … 0,7807, 0,7939 et 0,8067 selon le jeu » : trois jeux sur cinq. Écrire « sur trois des cinq jeux », avec
    les clés.
  - `scores-p3.npz` a 430 colonnes de sondes. Les 424 légères se choisissent par nom (`noms_sondes`) ; les 6 Mahalanobis
    sont écartées. L'écrire.
  - Clés de `sondes-figees.json` et de `episodes-p3.json` : sous `resultat.`.
  - Plancher d'une séparation (M6a, B contre H) : il se lit sur les séparations repliées des 200 directions, comme pour
    Δ net ; l'intervalle de M6a replie chaque tirage. L'écrire.
  - Rang de la sonde : fixer les ex aequo (par exemple 1 + nombre de directions de concordance strictement supérieure
    + moitié des égales).
  - Mesure d'encodage : citer le chemin du tokeniseur et son empreinte complète, ou s'en remettre à MC-1.

### VP3-12 — mineure — décisions des traitements non écrites

- **Où** : Mesures de conception (l. 123-132) ; Métrique, bras I ; Pare-feu ; Plan d'analyse, point 7.
- **Problème** : quatre décisions manquent au texte :
  - GP4-07 : « MC-2 le dira avant le scellement ; si les 60 épisodes passent le niveau 1, le candidat l'écrit ». Le
    traitement cite « Métrique (Bras I) ; MC-2 », qui n'ont pas changé ;
  - question 4 : variante « autre agent » (A5) exclue ;
  - question 11 : mesures de conception admises au titre de R1 (propriétés des entrées, aucun score) ;
  - économie refusée : la suite complète des tests tourne sur l'instance.
- **Correction** : une ligne chacune, à sa place.

### VP3-13 — mineure — la puissance pourrait se lire comme l'aire minimale détectable de P3

- **Où** : Plan d'analyse, point 5 (l. 376-382) ; Prédiction, P4-C1 (l. 190).
- **Problème** : « ≈ 0,63 à 0,65 … estimés pour le dessin de P3 ». Le verdict de P3 refuse de recalculer cette grandeur
  (« grandeur non écrite », l. 301). L'addendum 2 la traite : N-025, remarque 3 (« aire minimale détectable à la
  demi-largeur et au plancher observés, par sonde ») ; la note la garde non sortie (l. 51). Les objecteurs l'estiment
  déjà à 0,632 pour la tromperie (`objections-2.md` l. 37). Le nombre de P4 en est proche ; il ne doit pas passer pour
  celui de P3.
- **Correction** : « ordre de grandeur pour C1 de P4, sous l'hypothèse d'une erreur type égale à celle réalisée par P3 ;
  ce n'est pas l'aire minimale détectable de P3, qui relève de l'addendum 2 ; sans effet sur P3 ».

## Points vérifiés sans constat

- Empreintes : brouillons 1, 2 et 3 ; contre-lecture 1 ; deux traitements ; plan ; réponse de Gemini ; entropie
  (R-268) ; documents qui font foi, tous égaux ; dix données (empreinte et sceau égaux).
- Registres cités « au brouillon 2 » : `b702fa80…` est `decisions.md` au commit `1d872f3` ; `9c7fad43…` est `go.md` de
  `70546bf` à `bb7b006`. Ils ont bougé depuis ; « à relire au candidat » est écrit.
- Formes lues par les gardes : « Entropie : `…` » et « Révision du modèle : `…` » conformes à `validation_reelle.py`
  l. 74-75.
- Biais de la séparation repliée : σ·√(2/π), exact ; il abaisse Δ.
- Règle du témoin positif (ABC l. 83) et O2-30 (`objections-2.md` l. 198-201) : citées juste.
- R-262 : addendum 2 avant la lecture de P4, écrit comme une garde. Ordre des lancements et séparation de P3b :
  conformes à R-262 et à N-028.
- Bornes de temps : 3 600 s, 90 minutes, 150 minutes, création + 9 600 s, cohérentes entre elles.

## Pièces de la vérification

Sous `…/p4-instrument/verification/` :

- `diff-1-2-mots.txt` (`0c519c740a6947be6e35d25be89b924ab2057d4ccf7702c889fa513c1c1ca643`) et `diff-2-3-mots.txt`
  (`02ff3499bb956cc793028b784d00ab7dcc9f608a663749c7c4c69d65a0583162`) : différentiels mot à mot
  (`git diff --no-index --word-diff`, hors du dépôt).
- `demo-symetrie-plancher-v1.py` (`0ba209908c62230832c9fac6ec8c4f61fdad2c9bfdedae5a68c16323d29267cb`) et sa sortie
  `demo-symetrie-plancher-v1.txt` (`0a7d61e85ebbcc50aa4167b6d32500dc0dd1cbc9162740fac28da8005af0ac5a`) : données
  synthétiques seulement ; graines par `numpy.random.SeedSequence(20261020)`.
