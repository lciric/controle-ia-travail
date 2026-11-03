# Classement D — question 2 (facultative) de Paul Colognese et Francis Rhys Ward — v1

Écrit le 3 novembre 2026 à partir de 14:57 en temps universel coordonné (`date -u`), par le classeur neuf de l'étape D. Aveugle à la provenance des fiches ; aucune recherche ; aucun appel de modèle autre que le classeur ; aucun commit, aucun `.sha256`, aucun fichier existant modifié.

**Pas de témoin déguisé (échéance) : l'axe d'originalité n'est pas contrôlé.**

Question du mentor (texte exact) : « (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why? »

## 0. Entrées (empreintes vérifiées avant lecture)
| Entrée | sha256 | Contrôle |
|---|---|---|
| consigne `soir-classeur-D-colognese-ward-q2-v1.md` | `b3a183d280e9f51351724865afd368ff68feb7b84d5ce9f42c8ca973e77169d4` | égale à l'annonce |
| protocole `protocole-rapport-mentors-soir-v1.md` (étape D) | `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347` | égale à l'annonce |
| ancres `ideation-heimersheim-v1/protocole-rapport-idees-v1.md` (section 5) | `942b93241b6e033e34cc7cb035fe1d70f6e944a8a98bc4c556b83b0d7fdbad18` | aucune annonce ; relevée |
| fiches `prep-v1/fiches-servies-v1.json` | `ad1fa0a97ea8d23cf3eb444946b948f18435aa3ebb8867bf5284049e6673d943` | égale à l'annonce |
| moisson `moisson-C/moisson-fusionnee-v1.json` | `f5a066bbf2d5d985c27a6589210836a5dc09b796c1f6a6207cba98c368b229d3` | égale à l'annonce |
| pièce `piece-colognese-ward-v1.md` (section 1 pour le troisième critère) | `7533e4b58f03a5b8928ca2c411d8c29ee48f86e15e744afaf4b07e8a9b8f91b2` | aucune annonce ; relevée |

Chemins complets : `notes-v1.json`, champ `entrees_verifiees`.

## 1. Porte
- **Dans le sujet, classées : 22** — CW-02, CW-03, CW-04, CW-07 à CW-25.
- **Hors sujet : 3** — CW-01 (courbe dose–réponse de la sycophantie de Llama-3.1-8B-Instruct), CW-05 (sonde de sycophantie projetée sur un autoencodeur épars), CW-06 (syntaxe des doses de pression) : aucune ne porte sur le billet ni sur ce qu'il aurait fallu y faire.

## 2. Notes (0 à 3) — raisons d'une ligne dans `notes-v1.json`
Lectures déclarées avant toute note : *testable* plafonne à 2, car la pièce ne cite ni code ni jeu de données des mentors (sections 1 et 4) ; 2 = renotation de l'archive du billet, seuil clair, sans renforcement ; au plus 1 dès qu'il faut renforcer ou distiller. *Outil* : 2 et non 3 pour une réplication à plus grande échelle, une recombinaison de grandeurs rapportées, une vérification que le billet a faite en partie, ou un instrument extérieur dont l'outil du mentor n'est que le comparateur.

| Fiche | Originalité | Testable | Outil | Somme | Drapeau |
|---|---|---|---|---|---|
| CW-04 | 1 | 2 | 3 | **6** | non |
| CW-15 | 1 | 2 | 3 | **6** | non |
| CW-17 | 1 | 2 | 3 | **6** | oui |
| CW-18 | 1 | 2 | 3 | **6** | non |
| CW-19 | 1 | 2 | 3 | **6** | oui |
| CW-21 | 1 | 2 | 3 | **6** | oui |
| CW-22 | 1 | 2 | 3 | **6** | non |
| CW-16 | **2** | 1 | 2 | 5 | oui |
| CW-02 | 1 | 1 | 3 | 5 | oui |
| CW-03 | 1 | 2 | 2 | 5 | oui |
| CW-07 | 1 | 2 | 2 | 5 | oui |
| CW-09 | 1 | 1 | 3 | 5 | non |
| CW-14 | 1 | 1 | 3 | 5 | oui |
| CW-23 | 1 | 2 | 2 | 5 | oui |
| CW-08 | 1 | 1 | 2 | 4 | non |
| CW-10 | 1 | 1 | 2 | 4 | oui |
| CW-11 | 1 | 1 | 2 | 4 | non |
| CW-12 | 1 | 1 | 2 | 4 | non |
| CW-20 | 1 | 1 | 2 | 4 | non |
| CW-24 | 1 | 1 | 2 | 4 | non |
| CW-13 | 1 | 1 | 1 | 3 | oui |
| CW-25 | 1 | 0 | 2 | 3 | non |

## 3. Les huit premières
Sept fiches à 6 entrent d'office. La huitième place se joue entre les sept fiches à 5 ; départage par l'originalité : CW-16, seule « voisin lointain » de la moisson (2), devant six fiches à 1. Aucune égalité ne reste. Le script recalcule cette sélection depuis les notes et s'arrête si elle diffère (champ `selection_des_huit`).

**Les huit : CW-04, CW-15, CW-16, CW-17, CW-18, CW-19, CW-21, CW-22.**

## 4. Comparaisons par paires
- Question gelée : « laquelle ferait une réponse à cette question plus juste, plus originale et plus mémorable pour ce mentor, sur ces trois critères ? »
- e = entier des 16 premiers hexadécimaux du sha256 des fiches = `0xad1fa0a97ea8d23c` = 12474866142674473532.
- Liste canonique : les 28 paires (a, b) de `itertools.combinations` des huit triées ; indices 0 à 27 = a présenté en premier, 28 à 55 = b en premier. Ordre de présentation : `numpy.random.default_rng(numpy.random.SeedSequence(e)).permutation(56)` (numpy 2.5.3).
- 56 jugements écrits en six lots, de 14:52:34 à 14:53:29 en temps universel, dans l'ordre tiré ; chaque ligne est contrôlée à l'écriture contre la permutation (`paires-v1.jsonl`).

## 5. Forces de Bradley-Terry (script numpy, sans modèle)
Le maximum de vraisemblance **n'existe pas** : CW-22 gagne ses 14 comparaisons et CW-15 perd les siennes (graphe des victoires non fortement connexe). Le script le refuse explicitement et donne le maximum a posteriori sous une loi gaussienne centrée d'écart type 2 sur les log-forces (déclarée). Stabilité : 2 000 rééchantillonnages des 28 paires, graine `SeedSequence(e).spawn(3)[0]`.

| Rang | Fiche | Log-force ± erreur type | Victoires sur 14 | Rang moyen rééchantillonné | Part au rang 1 | Part aux rangs 1 à 3 |
|---|---|---|---|---|---|---|
| 1 | CW-22 | 3,39 ± 1,19 | 14 | 1,21 | 0,82 | 1,00 |
| 2 | CW-04 | 2,23 ± 1,05 | 12 | 2,05 | 0,16 | 0,98 |
| 3 | CW-18 | 1,28 ± 0,99 | 10 | 2,95 | 0,02 | 0,88 |
| 4 ex aequo | CW-16 | 0,00 ± 0,97 | 7 | 4,48 | 0 | 0,07 |
| 4 ex aequo | CW-19 | 0,00 ± 0,97 | 7 | 4,49 | 0 | 0,06 |
| 6 | CW-17 | −1,28 ± 0,99 | 4 | 6,10 | 0 | 0,00 |
| 7 | CW-21 | −2,23 ± 1,05 | 2 | 6,94 | 0 | 0 |
| 8 | CW-15 | −3,39 ± 1,19 | 0 | 7,78 | 0 | 0 |

- **Égalité CW-16 = CW-19** : sept victoires chacune, face-à-face 1–1, log-forces égales, 49,95 % des rééchantillonnages dans chaque sens. Départagées par l'originalité (2 contre 1), règle de la consigne pour la sélection, reprise ici et déclarée ; la somme des notes (5 contre 6) donnerait l'ordre inverse.
- Écarts voisins (probabilité de Bradley-Terry ; part des rééchantillonnages où l'ordre tient) : CW-22 > CW-04 0,76 ; 0,83 — CW-04 > CW-18 0,72 ; 0,82 — CW-18 > CW-16 0,78 ; 0,91 — CW-19 > CW-17 0,78 ; 0,93 — CW-17 > CW-21 0,72 ; 0,80 — CW-21 > CW-15 0,76 ; 0,83.
- Sensibilité à l'écart type (1, 2, 4) : même ordre hors de l'égalité. **Défaut déclaré** : la liste de sensibilité de la sortie n'applique pas le départage ; à écart type 1, elle montre CW-19 avant CW-16 par bruit d'arrondi dans une égalité exacte. La sortie n'est pas réécrite.
- Gardes éprouvées au lancement, toutes conformes (champ `epreuves_des_gardes`) : trois cas sains (jeu bien formé ; cohérence connue 0,75 ; forces connues retrouvées, rang de Spearman 1,00, écart maximal 0,16) et douze artefacts (ligne en double, ligne manquante, gagnant hors paire, identifiant étranger, ordre qui ne suit pas la graine, mauvaise graine, auto-comparaison, raison vide, paire vue deux fois dans le même ordre, ordre total demandé au maximum de vraisemblance, juge qui donne toujours raison au premier présenté, sortie existante).

## 6. Cohérence
**27 paires sur 28 concordent : 0,964.** Seule discordante : CW-16 contre CW-19 — au rang 20, CW-16 présentée en premier l'emporte ; au rang 34, CW-19 présentée en premier l'emporte. Quasi-égalité tranchée par l'ordre de présentation ; au rang 34, le classeur a vu que le mécanisme de CW-16 (apparition × renforcement de la première triche) reprend en partie l'analyse que Paul Colognese donne dans son commentaire (pièce §3.5). Part des 56 jugements gagnés par la fiche présentée en premier : 29/56 = 0,52 (pas de biais d'ordre général).

**Réserve** : au-dessus de 0,8, mais presque parfaite d'un juge unique (seuil déclaré 0,95). Le classeur avait noté les fiches avant les paires et garde la mémoire de ses jugements : les deux ordres ne sont pas indépendants, et la cohérence mesure la stabilité d'une seule lecture, non l'accord entre juges.

## 7. Drapeaux de risque devant ce mentor (les huit)
- **CW-22 — non** : chiffres conformes à la pièce ; la prédiction vient de 2601.21112 du mentor ; seul appui contraire, extérieur au mentor : 2602.16741 (commentaires adverses sans effet significatif), à citer.
- **CW-04 — non** : 93 % et 89 % conformes (Summary) ; même appui contraire extérieur (2602.16741).
- **CW-18 — non** : conforme à 2601.21112 ; la fiche borne elle-même ce qu'elle identifie ; créditer 2601.21112 et 2608.00583 (réécriture à actes identiques).
- **CW-16 — oui** : la triche délibérée de l'étape 89 vient d'un décompte de la graine 2 que la pièce n'a pas réconcilié (§3.5, §4), et l'auteur du commentaire est le mentor lui-même ; la lecture « donnée censurée » tient sans ce décompte.
- **CW-19 — oui** : la réécriture se fait dans la réponse (§3.3, §4.2) ; un diff des fichiers de test ne la verrait pas ; « la vérification d'intégrité voit cette classe » suppose une ré-exécution isolée des tests.
- **CW-17 — oui** : les auteurs ont trouvé les triches silencieuses en lisant les ratés de leurs moniteurs (§2.5) ; affirmer « aucune validation humaine » peut être contredit.
- **CW-21 — oui** : la prémisse (des honnêtes anti-triche qui verbalisent leur tentation) se heurte à A.1.3 (raisonnement en mode Nemotron de base, sans caractère visible, à l'étape 0) et au balayage de seuils (§2.4).
- **CW-15 — non** : « sans étiquettes humaines » est dans la pièce (§2.5) ; 2510.17057 affaiblit l'intérêt sans contredire.

## 8. Réserves
1. Originalité : 21 des 22 fiches dans le sujet sont « voisin proche » ; le critère ne départage que CW-16, sur la seule foi de la moisson (règle anti-faux-gap : « lointain » est un verdict de moisson, non une zone vierge établie).
2. Testabilité plafonnée à 2 : aucune archive publique citée ; les 2 supposent l'archive des auteurs (quelques jours pour eux) ou une reconstruction sur modèles ouverts (une à deux semaines).
3. Même famille en tête : CW-22 et CW-04 testent la même trouvaille (le commentaire « inoffensif ») par deux plans ; CW-18 les généralise. Les trois premières disent toutes « le moniteur lit ce que l'agent écrit ». Fusionner ou non relève du directeur.
4. La lecture 2 contre 3 du troisième critère est celle du classeur, déclarée dans les notes ; elle décide de l'entrée de CW-15 et de l'absence de CW-07 et CW-23.
5. Héritées de la pièce : valeurs des figures 5 à 10 absentes du texte ; décompte de la graine 2 non réconcilié ; limites 2 à 6 de §4.4 non lues.
6. Déroulement : un outil d'ajout avec contrôle à l'écriture, `/tmp/classeur-d-outils/ajout.py` (sha256 `699199a110e5c9b837df7f3814a2284c42be9316e867ccf163ae1e73f2b87a7b`), placé hors du dossier de rendu et gardé pour audit ; la tolérance de convergence du script a été ajustée une fois avant sa première exécution, aucune sortie n'existait alors.

## 9. Ordre final
**CW-22, CW-04, CW-18, CW-16 = CW-19 (ex aequo ; CW-16 devant par l'originalité), CW-17, CW-21, CW-15.**

## 10. Fichiers du rendu
| Fichier | sha256 |
|---|---|
| `notes-v1.json` | `3185a1a30376ec3c66b2a2aa7182777ca2639115695b8c4312935625352ab242` |
| `paires-v1.jsonl` | `45afc7c5a8076fff8589b419833713bd804715713a00ad4a0be8c1236fbd8124` |
| `bradley_terry_colognese_ward_q2_v1.py` | `601292b4975fbd6902fd228bbfe87fb7e02bfff6df527e54c5d849dac34ea224` |
| `bradley_terry_colognese_ward_q2_v1-sortie.json` | `547987db9d910c2b3730a38fdb78b58bca9f1dc6f4647da6404d51d7503a261c` |
| `classement-v1.md` (ce fichier) | dans la réponse finale du classeur |
