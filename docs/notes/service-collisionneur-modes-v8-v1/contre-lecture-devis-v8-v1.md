# Contre-lecture du devis du service de la question v8 au collisionneur — v1

> Contre-lecteur neuf : Claude Opus 5.5 (sous-agent), qui n'a pas écrit le devis. 23 novembre 2026. Pièce lue : `docs/notes/service-collisionneur-modes-v8-v1/devis-service-collisionneur-modes-v8-v1.md`, empreinte 6363e03d…, sceau vérifié (concorde avec son `.sha256`). Dépôt au commit 5579f9294. Rien lu sous une branche `coffre/*` ni dans un chemin qui contient « coffre ». Aucun envoi à un modèle, aucune dépense, aucun commit. Rejeux faits dans le bloc-notes de la session, hors du dépôt. Les moteurs du collisionneur, révision 8m, et la voie abonnement v6 ont été extraits en lecture de `origin/runs/collisionneurs-reprise-v8d-v1` (470f7e6f…) : empreintes 420394f9… et d99f3358…, conformes au devis.

## Verdict

**Bon après corrections.** Tous les chiffres se retrouvent au centime en rejouant les calculs. Les réglages passent la garde de Google pour toutes les espèces, à toutes les étapes des relances. Le préalable des ≈ 3 300 mots est tenu pour chaque espèce. Aucun défaut ne remet en cause la recommandation. Quatre défauts moyens touchent ce que Lazar doit savoir avant son GO : la valeur haute présentée, la mécanique quand le plafond est atteint, la vérification par programme de la version servie, et les options de la décision 2. Six défauts mineurs suivent.

## 1. Rejeu des chiffres (point 1 de la commande)

| contrôle | résultat |
|---|---|
| Empreintes des 23 fichiers de `calculs/`, comparées au § 13 | toutes concordent (8bfdbca7…, 22223250…, 52cd710f…, c96f9533…, etc.) |
| `releve_journaux_v2.py`, rejoué | json identique (52cd710f…), sortie identique au caractère près |
| `calcul_devis_v8_v2.py`, rejoué sur le moteur révision 8m et le texte servi | sortie identique au caractère près : attendu 8,95, pannes 1,63, **attendu avec pannes 10,59**, haut sans pannes 10,47, donc **haut 12,10**, **pire sans relance 40,21**, **pire avec relances 99,07**, plus grande marge 7,44 ; sans `--sortie-max` 22,21 / 66,67 / 2,71 ; option (b) 10,86 / 12,41 / 40,61 / 100,10 / 7,54 ; option (c) à six espèces 19,78 / 23,13 / 37,32 / 99,37 / 4,32 |
| `calcul_devis_v8_v2_option_interface.py`, rejoué | identique : 13,01 ; haut 13,24 + 1,82 = 15,06 ; 26,97 ; 76,20 ; 2,71 |
| `taux_pannes_v1.py`, rejoué | identique : Carbon 7 sur 56, Argon 5 sur 62, Neon 1 sur 26, Astra 0 sur 64 |
| `comparer_moteurs_et_garde_v1.py` (sortie versée relue) | 19 chemins internes, 3 identifiants d'accord ; révisions 8d et 8m identiques (tours, consignes, préambule, motifs, catalogue) |
| Commande `devis` des moteurs, rejouée sans réseau | révision 8d, six espèces : 35,24 à l'étage III, sortie identique ; révision 8m, cinq espèces sous `--sortie-max` : 47,38, sortie identique |
| Plafonds proposés | (a) 12,10 + 7,44 + 2 × 2,71 = 24,96, soit 25 ; sans `--sortie-max` 20,23, soit 21 ; (b) 12,41 + 7,54 + 2 × 2,75 = 25,45, soit 26 ; (c) à cinq espèces 23,19, soit 24 ; (c) à six espèces 32,95, soit 33 : tous conformes à la formule |
| Marges du § 5.3 | Carbon 1 684 / 16 384 = 10,3 % ; Astra 1 070 / 8 000 = 13,4 % ; Fable 5 180 / 49 000 = 10,6 % ; ⌈3 900 × 4,2⌉ = 16 380 < 16 384 : exact |
| Lecture du § 6.5 | dépense attendue avant la réponse d'Astra : 6,36 hors pannes, ≈ 7,5 avec : exact |
| Lignes citées | `CLAUDE.md` (605db83a…) l. 63-67, 69-70, 75-76, 81-82, 106-107 ; `registres/go.md` (16830ee4…) l. 757, 764, 800, 831, 838, 841 ; `registres/depenses.md` l. 601 et 604 ; `registres/decisions.md` l. 5211 : vérifiées |

## 2. Défauts

### D-1 (moyenne) — la valeur haute de 12,10 USD n'est pas une valeur haute

- **Constat.** Le haut ne compte que l'espérance des pannes (1,63). Or deux des trois dossiers comparables du 22 novembre ont coûté 12,50 et 12,59 USD, au-dessus de ce haut, avec des questions plus courtes. Leurs pannes valaient 4,76 et 5,12 USD (§ 6.2 du devis lui-même).
- **Effet sur le plafond.** Sur le chemin haut (90e centile des sorties, pièces maximales), on a dépensé 7,51 USD avant la réponse d'Astra (rejeu cellule par cellule). Ajoutons le schéma de pannes du 22 novembre : deux coupures de Carbon aux tours III.1 et III.2, comptées 5,07, leurs relances, ≈ 2,1, et un refus d'Argon, ≈ 1. On arrive à ≈ 15,7, plus la marge de 7,42 exigée avant l'envoi d'Astra : ≈ 23,1. Le plafond de 25 tient, mais **une seule coupure de plus de Carbon empêche la réponse d'Astra de partir**. Le « environ quatre pannes de plus » du § 6.5 est lu sur le chemin attendu. Sur ce chemin haut, la marge n'est que d'une panne.
- **Correction.**
  - Donner au § 0 et dans l'enjeu de la décision 2 un haut avec un nombre de pannes haut, par exemple celui du 22 novembre (≈ 18 USD), à côté des 10,6 attendus.
  - Refaire la lecture du § 6.5 sur ce chemin.
  - Dire à Lazar l'arbitrage que cela révèle : `--sortie-max` porte la marge d'Astra de 2,6 à 7,4 USD pour une sortie relevée de 4 797 jetons au plus. À plafond égal, il retire donc la place de deux pannes de Carbon environ. Proposer soit 25 USD, ce risque étant dit, soit ≈ 28 USD.

### D-2 (moyenne) — que se passe-t-il au plafond : la mécanique décrite est incomplète

- **Constat 1.** `--plafond-usd` n'est pas scellé dans le dossier. Chaque commande le redonne, et le défaut vaut 40 USD (`collisionneur_v9_v8d.py` l. 402 et 2707). C'est la ligne (`--ligne-usd`) qui est scellée au premier lancement (l. 1753-1765) : elle seule borne vraiment à 25.
- **Constat 2.** Une ligne de reprise remplace la ligne pour la garde par envoi, mais « le plafond du dossier reste contrôlé à part » (l. 166-169). La phrase « rien ne repart sans une ligne de reprise accordée par Lazar » est juste pour la ligne. Elle oublie que la reprise demande aussi de redonner un `--plafond-usd` plus haut.
- **Constat 3.** Le plafond est sous le pire sans relance (40,21). Le devis dit le code 4, mais pas le statut de la cellule refusée, ni la suite de la consultation. Il ne dit pas non plus comment un refus au plafond se concilie avec le droit à une relance après panne technique (GO-2026-11-22-77).
- **Correction.**
  - Écrire au § 6.5 : la ligne scellée de 25 USD est la borne effective. Toute commande de l'opératrice redonne `--plafond-usd 25`. Une reprise au-delà demande un GO de Lazar portant à la fois `--ligne-reprise-usd` avec `--go-ligne` et le nouveau `--plafond-usd`.
  - Une cellule refusée au plafond est un « faux échec », issue « jamais parti ». Elle n'est pas une absence que l'arbitre accepte. Elle devient un nœud porté à Lazar avec la sortie de la commande `devis-reprise`.
  - La relance due après une panne technique se fait sous le même plafond. Si le plafond la refuse, même nœud.

### D-3 (moyenne) — décision 1 : bornée en intention, pas encore vérifiable par programme

- **Constat.** Le § 3, point 4, promet des remplacements « à texte exact par programme, le diff versé, la garde repassée ». Rien ne vérifie par programme que la différence se limite aux chemins et aux identifiants. Une garde à zéro refus le prouve encore moins. Trois trous :
  - la garde ne voit pas les restes « et -136 » (fait 17, l. 78) et « à -139 » (source 21, l. 179) : rejoué, `motifs_trouves("GO-… à -139")` ne prend que l'identifiant entier ;
  - la ligne de provenance « au commit 2cd13d45… » du « dépôt d'origine » (l. 154 de la v8) n'est prise par aucun motif, et le devis n'en dit rien ;
  - effacer les chemins des sources 8, 9, 15 et 16 efface aussi l'identifiant public de l'article (2606.08892). Cette provenance est publique et utile aux modèles. La garde ne la refuse pas.
- **Correction.** Écrire au § 3 une vérification par programme, de classe B, contre-lue :
  1. une liste scellée de paires (ancien, nouveau), où chaque ancien apparaît exactement une fois ;
  2. appliquer les paires à la v8 (047eeddf…), lignes 1 et 2 retirées, doit redonner le texte servi octet pour octet ;
  3. tout ancien tombe dans les lignes 77, 78 et 154 à 179 de la v8, et porte un motif de la garde, un chemin `donnees/` ou un reste d'identifiant ;
  4. hors de ces lignes, le texte est identique, empreinte du reste à l'appui ;
  5. après remplacement, aucun reste par expression régulière : `GO-`, `-13[5-9]\b`, les chemins entre accents graves commençant par `docs/`, `src/`, `prereg/` ou `donnees/`, et `controle-ia`. La garde des deux moteurs rend zéro.
  - Trancher dans la décision le sort du commit (recommandé : retiré, car c'est une provenance interne) et de l'identifiant de l'article (recommandé : gardé, il est public).
- **Porte v5.** Elle est scellée en visant l'empreinte de la v8. Dire qu'elle s'applique au texte servi, c'est un écart à une pièce scellée : un nœud. Le devis le confie au gardien (§ 3, point 5). Il faut l'écrire dans la décision 1 elle-même : Lazar accorde que la porte v5 s'applique au texte servi, le gardien vérifie et dit ce que reçoivent les trieurs.

### D-4 (moyenne) — décision 2 : une option manque, et ce qui est perdu n'est pas dit

- **Constat 1.** L'option (b) ajoute Fable à Opus : deux voix Claude sur six. Le devis invoque lui-même le principe accordé « une seule espèce Claude » (§ 4, devis v3 l. 54, GO-2026-11-21-08). L'option qui le respecte manque : **(b′) cinq espèces après le 29 novembre, 18:00 UTC, Fable par l'abonnement à la place d'Opus**. Son coût est celui de (a) à quelques centimes près, puisque l'abonnement est à 0 USD et que la marge du kit de Fable reste sous celle d'Astra.
- **Constat 2.** Ce qui est perdu sans Fable n'est pas dit :
  - la voix Claude la plus forte de la maison ;
  - la continuité avec le passage « modes » du 22 novembre, servi par Fable : le devis présente le changement comme un gain de diversité, mais deux passages servis par deux voix Claude différentes ne se comparent plus ;
  - la règle « Qui conçoit » (`CLAUDE.md` l. 79) : la conception du saboteur revient à Fable. Le devis doit dire pourquoi une cellule de collisionneur n'en relève pas : elle propose des candidats, le choix du mode tenu à l'écart vient après.
- **Constat 3.** Le coût de l'attente de six jours n'est pas chiffré. Aucune échéance n'est citée : premier besoin d'un mode tenu à l'écart neuf, entretien du 1er décembre, porte G0 fin décembre.
- **Correction.** Ajouter (b′) en remplaçant (b), ou à côté. Écrire en une ligne ce qui est perdu et ce que coûte l'attente. Garder la recommandation (a) si l'échéance la justifie.

### D-5 (mineure) — l'espérance des pannes oublie la relance qu'elles entraînent

Chaque panne technique ouvre droit à une relance (§ 6.4). L'attendu compte la panne au pire, mais pas le coût de la relance qui suit. Il manque environ 0,6 USD : Carbon 0,125 × 2,76, Argon 0,081 × 2,09, Neon 0,038 × 2,14. L'attendu passe donc de ≈ 10,6 à ≈ 11,2. **Correction** : l'ajouter, ou dire en une ligne que l'attendu l'omet.

### D-6 (mineure) — panne d'une session d'Opus

- Le devis dit : aucune relance par la voie, l'arbitre décide (§ 6.4). Mais une session de l'abonnement perdue avant le recueil est une panne technique au sens de GO-2026-11-22-77.
- La voie interdit de servir deux fois une réponse déjà recueillie. Elle n'interdit pas de confier le même kit, non recueilli, à une session neuve, une fois, à coût nul.
- **Correction** : l'écrire au § 6.4, avec l'issue codée.

### D-7 (mineure) — § 13 périmé, empreintes compagnons absentes, rejeu qui écrase

- Les calculs sont versés dans `calculs/`, et non dans le `calculs-v1/` annoncé. Le § 13 les dit encore « non versés, dans /tmp ».
- Quatre fichiers versés ne sont pas listés : `calcul_devis_v8_v1.py`, `calcul-devis-v8-v1-totaux.json`, `releve-journaux-v1-bis.json` et `releve-journaux-v2-bis.json`.
- Aucun fichier de `calculs/` n'a son `.sha256` compagnon (R6).
- `calcul_devis_v8_v2.py` écrit toujours `calcul-devis-v8-v1-totaux.json` sous le même nom, à côté du relevé, et y laisse des dossiers temporaires. Rejoué dans `calculs/`, il écraserait la pièce versée (R12). Le rejeu doit se faire hors du dossier versé : à dire au § 13.

### D-8 (mineure) — provenance de « le v8d, nommé dans la commande »

La ligne GO-2026-11-23-03 (`registres/go.md` l. 841) ne nomme aucun moteur. **Correction** : citer la pièce qui le nomme (mandat de la mère), ou retirer « nommé dans la commande ».

### D-9 (mineure) — à porter à la connaissance de Lazar sur les réglages

- **Dernier recours de Google.** Il se fait un niveau plus bas : « medium » pour Argon et Carbon, « high » pour Neon. C'est un écart à « niveau le plus haut admis » (`CLAUDE.md`, « Appels aux modèles de Google »), accordé par la décision de la mère R-4664 et contre-lu. Le citer au § 4 ou au § 6.4.
- **Astra.** Aucun réglage d'effort de raisonnement n'est envoyé, et le raisonnement relevé est de 104 jetons au plus. C'est une réserve de qualité pour une cellule de conception, pas de coupure. L'ajouter au § 12.

### D-10 (mineure) — forme de la décision demandée

- **Format** (`CLAUDE.md`, « Communication avec Lazar ») : décision en une phrase, enjeu, options avec avantage et inconvénient, recommandation et confiance, défaut ou « pas de défaut » motivé. Il est **conforme** pour les deux décisions.
- Mais l'option (c) de la décision 2 porte deux variantes chiffrées, à cinq et à six espèces : en tout quatre options pour une règle qui en veut 2 ou 3. Avec (b′) de D-4, regrouper.
- La section destinée à Lazar emploie des codes seuls : « v8m », « III.1 », « P2 ». Les nommer en clair d'abord, code en appui (R-3044, R-3085). Par exemple « le moteur du collisionneur, révision 8m » ou « le tour de conception (III.1) ».

## 3. Réponses aux points de la commande

1. **Chiffres** : tous retrouvés en rejouant (§ 1 ci-dessus).
2. **Plafond de 25 USD** : cohérent avec la formule et avec la règle des relances. Il est sous le pire sans relance, ce que permet la garde avant chaque envoi. Ce qui se passe quand il est atteint est dit, mais incomplètement (D-2). Sur un chemin haut réaliste, la marge n'est que d'une panne (D-1).
3. **Réglages de Google et de Carbon** : rejoués par `verifier_reglages_google` (garde v3) sur les corps construits par le moteur, pour Argon, Carbon et Neon, aux trois tours et aux trois étapes du plan (premier envoi, relance identique, dernier recours). Tout passe :
   - réflexion explicite, au niveau le plus haut admis : Argon et Carbon « high », Neon « xhigh » ;
   - plafond de 65 536, au moins égal à la provision plus 16 000 : 49 152, 16 384 et 32 768 jetons de texte ;
   - limite de mots tenue : Carbon ⌈3 500 × 4,2⌉ = 14 700 < 16 384.
   - **Astra** : 128 000 dès le premier envoi sous `--sortie-max` (moteur révision 8m l. 461 et 465), contre 4 797 relevés au plus. Il ne sera pas coupé par le plafond. Délai de 10 800 s, supposé.
4. **≈ 3 300 mots** : tenu pour chaque espèce. Argon, Carbon (marge de 10 %) et Neon sont vérifiés par la garde. Astra a 13 % de marge à 8 000, sans objet à 128 000. Opus par l'abonnement n'a pas de plafond d'interface. Fable aussi, dans les options (b) et (c). Le tour de conception et le tour de réponse admettent 3 500 mots. Astra écrit plus court, ce qui n'est pas une troncature.
5. **Décision 1** : bornée dans son principe et nécessaire. Le refus de la garde est rejoué : 19 chemins et 3 identifiants. Elle n'est pas encore vérifiable par programme (D-3).
6. **Décision 2** : arguments justes sur le coût et sur la voix Claude unique. Une option manque, et la perte n'est pas écrite (D-4).
7. **Format** : conforme, réserves de forme en D-10.

## 4. Ce qui n'a pas été vérifié

- Le barème de `gpt-6.2-astra` et les délais sous `--sortie-max` sont supposés, comme le devis le dit.
- La porte v5 et la question v8 au coffre n'ont pas été lues. Seul le texte servi versé dans `calculs/servi/` l'a été, pour la table des sources et les faits 16 et 17.
- Le contenu des cellules des journaux n'a pas été lu : seules les sorties des programmes de relevé l'ont été.
