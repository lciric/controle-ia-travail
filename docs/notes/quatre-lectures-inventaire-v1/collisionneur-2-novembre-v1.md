# Collisionneur à cinq espèces du 2 novembre — sélection d'une génération à l'autre et vérification non circulaire du bac à sable : comparaison et fusion avec Argon seul et Kimi seul — v1

Lecteur : sous-agent neuf (Opus 5.5, `claude-opus-5-5`), lancé par la session mère sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170). Je n'ai écrit ni les questions, ni les faits servis, ni aucune cellule, ni les avis d'espèce seule, ni leurs lectures vérifiées. Écrit le 2026-11-18 entre 04:08 et 04:40 UTC (`date -u`). Aucune dépense, aucun appel de modèle, aucune clé lue, aucun commit, aucune poussée.

Cette note **compare et fusionne des avis** ; elle ne tranche rien. Chaque position est celle d'une espèce, dans une cellule nommée : c'est un avis, jamais un fait. Les chiffres que les espèces tirent des pièces servies sont rapportés comme elles les rapportent ; tout chiffre ou toute référence de l'état de l'art qu'elles avancent est **non vérifié** (R7) ; toute zone qu'elles disent vierge est une question (R8).

## Sources

**Collisionneur** — branche `donnees/collisionneur-v8-runs-v2`, commit `0e7b3e5` (versé scellé sans lecture, R-1039), extrait seul sous `…/scratchpad/quatre-lectures/extrait/collisionneur-v8-runs-v2/`. Chemins dans la branche :

- `donnees/collisionneur-v8-runs-v1/selection-generations-v1/` — question `question.md` (`c899221888d1…`, égale à GO-2026-11-01-07 et à R-959), faits `faits.md` (`7c3404f477c7…`, égale à GO-2026-11-01-07) ; cellules sous `run-selection-generations-v1-e3-v1/cellules/` (abrégé **sél/** ci-dessous).
- `donnees/collisionneur-v8-runs-v1/bac-a-sable-v1/` — question `question.md` (`26f2db15e6ab…`, égale à GO-2026-11-01-08 et à R-959), faits `faits.md` (`24064c98d197…`, égale à GO-2026-11-01-08) ; cellules sous `run-bac-a-sable-v1-e3-v1/cellules/` (abrégé **bac/**).

Les cinq espèces du collisionneur (lettres anonymes dans le protocole, modèle servi lu au journal de chaque cellule) : **A** Fable 5.1 (`claude-fable-5-1`) ; **B** Opus 4.6 (`claude-opus-4-6`) ; **C** Argon (`gemini-4-argon`) ; **D** Kimi (`kimi-k3.1-pro`) ; **E** Astra (`gpt-6-astra`). Trois tours : conception (`E3-T1-conception-X.md`), critique croisée (`E3-T2-critique-croisee-X.md`), réponse aux critiques (`E3-T3-reponse-X.md`).

**Au dépôt** (`main`, commit `ae97fea4`) : `docs/notes/reponses-especes-seules-2026-11-01-v1/` — lecture vérifiée « sélection » v2 (`lecture-verifiee-selection-generations-v2.md`, `79e17284…`, Argon seul et Kimi seul) ; lecture vérifiée « bac à sable » v2 (`lecture-verifiee-bac-a-sable-v2.md`, `d7e19d88…`, Argon seul) ; lecture vérifiée de l'avis de Kimi seul sur le bac à sable (`lecture-verifiee-bac-a-sable-kimi-v1.md`, `ef98275d…`, arrivée après, R-973). Registres : R-959, R-973, R-975, R-1039, R-1049, R-1050 de `registres/decisions.md` ; inventaire `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc246…`, §§ A, B, E).

**Critères de lecture écrits et scellés avant l'ouverture des cellules** : `docs/notes/quatre-lectures-inventaire-v1/criteres-lecture-collisionneur-2-novembre-v1.md` (`4f5604b5c2bf…`), conformément à l'option (a) du nœud 2 de l'inventaire.

## Ce que j'ai vérifié avant toute lecture

- **Empreintes** : les 133 fichiers de l'extrait ont chacun un compagnon `.sha256`, et les 133 concordent (0 écart, 0 compagnon manquant). Aucun fichier « EMPREINTES » n'est présent dans l'extrait ; les empreintes de la question et des faits de chaque tour égalent celles que citent GO-2026-11-01-07/-08 et R-959, et la copie servie au tour (`question-etage3.md`, `faits.md` du dossier de run) égale l'original.
- **Journal de chaque tour** (`journal.jsonl`) recoupé par script contre les cellules : pour les 30 cellules, l'empreinte du texte au journal égale celle de la cellule et celle de l'essai retenu ; modèle servi = modèle demandé ; marqueur de fin présent ; aucune catégorie de refus.
- **Cellules absentes, refusées ou invalides : aucune.** Un essai a échoué : sélection, critique croisée de D (Kimi), essai 1, `HTTP 429` « engine overloaded », 0 USD ; repris en essai 2 (OK) par le lanceur « suite » (écart déclaré en R-1039). Coût inscrit aux états : 16,38 USD (sélection) et 16,24 USD (bac), soit 32,62 USD, **estimation haute** : Opus 4.6 y est compté au barème de 15/75 USD, environ trois fois son tarif (R-1049), jamais rapprochée d'une facture (inventaire § D).

## Ce que j'ai lu, et pas lu

- **Lu en entier** : les deux questions ; les dix cellules de réponse aux critiques (troisième tour), qui portent la position finale de chaque espèce ; les trois lectures vérifiées d'espèce seule.
- **Lu en partie** : les conceptions du premier tour, par sections (suppositions, réponses aux questions, avis propre, ordre) — sélection : A l. 5-24, B l. 180-fin, C l. 32-45, D l. 1-30, E l. 25-88 et 192-fin ; bac : A l. 93-fin, B l. 174-fin, C l. 29-115, D l. 7-23 et 105-fin, E l. 7-78 et 153-fin.
- **Pas lu** : les dix critiques croisées (deuxième tour ; je n'en connais que ce que les réponses en rapportent) ; les faits servis au-delà de leurs titres ; les invites des essais (au-delà des 3 000 premiers caractères d'une seule, sélection A) ; les journaux et états du relais de Kimi, `balayage-faits.txt`, les appels de contrôle, les scripts et lanceurs. Les réponses brutes d'Argon seul et de Kimi seul ne sont pas relues : je m'appuie sur leurs lectures vérifiées.
- **Cloisonnement** : rien ouvert sous `diag/`, aucune autre branche `calcul/` ni `donnees/`, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis ; je n'ai ouvert aucune autre branche extraite à côté.

## Exclusions de cloisonnement

Aucune cellule entière ne relève des deux familles exclues. Quatre passages en sont proches ; je les ai rencontrés en lisant, ne les résume ni ne les reformule, et les note par prudence :

| passage | famille | chemin (dans la branche) | taille de la cellule |
|---|---|---|---|
| contenu des corpus de « sondes » écrites pour éprouver les détecteurs du bac (consigne du sondeur, cibles nommées) et liste de sondes dépendant du noyau | 2 (bras d'attaque contre nos détecteurs) | bac/`E3-T3-reponse-C.md`, expériences 1 et 3 corrigées | 29 151 octets |
| liste des traits passifs de l'expérience « opacité du bac » | 2 (proche) | bac/`E3-T3-reponse-B.md`, expérience 2 corrigée ; bac/`E3-T1-conception-B.md` l. 40-59, non lue | 19 921 et 23 894 octets |
| « famille 3 » de sondes hors système de fichiers | 2 (proche) | bac/`E3-T3-reponse-A.md`, E3' | 20 244 octets |
| dessin de l'opérateur de recombinaison « au pire cas » qui exploite les scores, et du « générateur capable d'exploiter le retour » | 2 (attaque de Goodhart du juge, classée en famille 2 par l'inventaire, § C) | sél/`E3-T3-reponse-C.md`, E2 corrigée ; sél/`E3-T3-reponse-E.md`, expérience « réutilisation » | 26 465 et 20 571 octets |

Je ne garde de ces passages que leur rôle de méthode, sans contenu : « un témoin positif écrit par une main qui ignore le détecteur », « un contrôle positif d'adaptation ». Je ne recopie pas non plus les noms et emplacements de canaris proposés (bac/`E3-T1-conception-C.md`, Q5) : un leurre décrit dans un document que lisent les agents ne leurre plus.

## Réserves sur la comparaison

1. **L'espèce B a servi Opus 4.6, pas Opus 5.5** (identifiant codé en dur, `collisionneur_v8.py:71`, hérité du v6 autorisé « pour ce tour seulement », R-830) : écart déclaré, runs gardés tels quels par la décision de Lazar (R-1049, R-1050). Toute position de B est celle d'Opus 4.6.
2. **Sept sources, cinq modèles.** C et Argon seul sont le même modèle ; D et Kimi seul aussi. Un accord C + Argon seul, ou D + Kimi seul, ne compte pas comme deux voix indépendantes ; je le signale à chaque fois.
3. **Les positions du collisionneur ne sont plus indépendantes au troisième tour** : chaque espèce a lu les quatre autres conceptions et leurs critiques. Plusieurs accords quasi unanimes ci-dessous sont nés de la critique croisée ; ils valent moins qu'un accord au premier tour (R4 : une convergence trop propre est une réserve).
4. **Les formats diffèrent.** Argon seul et Kimi seul ont répondu aux questions Q1 à Q7 (option, confiance, pire cas, option manquante, pièce qui trancherait). Le collisionneur, à l'étage III, a écrit des suppositions et des expériences en duel exclusif (H_A contre H_B). Le rangement des expériences sous chaque question est **le mien**.
5. **Les faits servis datent du 1er novembre.** Depuis, le programme a changé (N-068, N-069, N-070 : H9 retirée des hypothèses revendiquées) et la course à plusieurs générations a avancé (conception v4, préenregistrement au brouillon 3, R-3051 ; pilote d'une génération, R-2501 ; bras « oublier » demandé, R-2528). Je n'ai lu ni cette conception ni ce brouillon : la fusion dit ce qui **pourrait** y servir, pas ce qui y manque.
6. **Le lecteur est de la famille d'A** (Claude) : biais de lecture possible sur A et B.
7. La réponse propre de conv-audit (« C » des lectures vérifiées, `…/scratchpad/relecture/…`) n'est pas une colonne : je la cite à part quand un accord la rejoint.

---

## 1. Sélection d'une génération à l'autre

### Q1 — Règle de survie et contrôle des fausses découvertes

| source | position (avis) | où |
|---|---|---|
| A (Fable 5.1) | La conjonction « survit au test de mort **et** promue » est une règle d'**extinction**, pas de sélection : 85 à 95 % des fiches ne seraient jamais jugées. Le pôle prévoit « indécise → test plus puissant, ou retirée après deux essais », ce qui contredit « une non-concluante ne passe pas » : la question impose l'une sans le dire. Trois états obligatoires. Préalable : courbe de puissance de la procédure de Benjamini et Hochberg sur e-valeurs à petit nombre de fiches (5 à 50), sur processeur, 0 USD ; puis épreuve fraîche avec quatre classes de témoins (vrais à trois forces, faux par permutation, lois bien formées à effet nul, vrais mal calibrés), cette dernière disant si le « pari à fraction » est un préalable. | sél/`E3-T1-conception-A.md` S5-S7 ; sél/`E3-T3-reponse-A.md` P0, E1' |
| B (Opus 4.6) | Les dents du pôle sont le verrou : au moins 1 témoin vrai promu sur 5, sur 5 moniteurs distincts, avec deux bras de témoins (confirmés sur le développement, à force nominale) et un contrôle « connu + 0 ». La conjonction n'est jugée qu'après, sur fiches à vérité connue ; une fiche vraie sans épreuve doit sortir « différée », jamais « éliminée ». | sél/`E3-T3-reponse-B.md` E1, E3 |
| C (Argon) | Quatre états : promue (couche 1) ; gelée en attente (couche 3 ou théorie, sans être comptée confirmée) ; indécise ou non traduisible (retirée, ne passe pas) ; réfutée (archivée). Tester une pondération de la procédure sur e-valeurs par la richesse de développement, poids gelés avant l'épreuve et de somme égale au nombre de fiches, en plan 2 × 2 avec le filtre du test de mort. | sél/`E3-T1-conception-C.md` Q1 ; sél/`E3-T3-reponse-C.md` E1b, (c) 2.1 |
| D (Kimi) | Trois états **administratifs**, pas une troisième issue scientifique : éliminée, promue (seule à se reproduire et transmettre une preuve), différée (scellée hors de la population reproductrice, sans preuve héritée, ne revient qu'avec des données ou un test neufs). Un test de mort exploratoire ne devient pas un filtre confirmatoire sans geler rôle, multiplicité et données. | sél/`E3-T1-conception-D.md` « Conséquence de conception » ; sél/`E3-T3-reponse-D.md` (c) |
| E (Astra) | Quatre états : réfutée, en attente, promue, **invalide techniquement** (fuite, panne, violation : aucun verdict). Seules les promues sont parents ; une reprise exige un engagement neuf. Procédure appliquée à **toutes** les lois admissibles de la génération ; un filtre appliqué après elle n'hérite pas de son contrôle : il faut justifier l'ensemble finalement annoncé. Pas de petites familles artificielles. Le contrôle par génération n'est pas un contrôle cumulé ; pour le premier essai, budgets d'erreur bornés sur toute la campagne. | sél/`E3-T1-conception-E.md` B ; sél/`E3-T3-reponse-E.md` règles communes |
| Argon seul | Deux états stricts, ou trois avec **file de dormance** réinjectée en g + k ; procédure par génération, ou pondérée a priori par la sévérité du test de mort ; le signal « sans dents » suspend la lecture négative. | lecture vérifiée sélection v2, § 1.2 |
| Kimi seul | Deux axes, empirique × testabilité ; survivante héréditaire = test de mort survécu, promue **et** correspondance fiche-loi démontrée ; non testable archivée hors du dénominateur ; aucune conversion des verdicts des juges ou des tests de mort en e-valeurs ; par génération ≠ cumulé. Confiance 0,88. | lecture vérifiée sélection v2, § 2.2 |

- **Accord (six sources sur sept, B en creux)** : plus de deux états ; « réfutée » distincte de « en attente » ; seule la promue se reproduit.
- **Accord** : le contrôle par génération ne protège pas l'archive cumulée (D, E, Argon seul, Kimi seul).
- **Divergence** : le sort de la non-concluante. Retirée (C), différée et réadmissible avec données neuves (D, E), dormante puis réinjectée (Argon seul) ; A relève que la conception du pôle et la règle de Lazar se contredisent.
- **Divergence** : la pondération. Pour : C et Argon seul (même modèle), et E sous condition de validité démontrée. Contre la conversion des verdicts en e-valeurs : Kimi seul.
- **Propre à une espèce** : l'état « invalide techniquement » (E) ; la courbe de puissance à petit nombre de fiches comme préalable (A) ; le témoin « vrai mal calibré » (A, pris d'une critique de C) ; « filtrer après la procédure n'hérite pas du contrôle » (E).

### Q2 — Fuite entre générations

| source | position (avis) | où |
|---|---|---|
| A | Simulation décisive, essai réel exploratoire : plan 2 × 2 × 2, épreuve réutilisée ou fraîche × mémoire transmise ou vide × ordre des lots ; filles de parents tirés au sort **avant** tout verdict ; au moins 200 témoins par bras (0 appel). La mémoire est un second canal, partagé par tous les bras. | sél/`E3-T3-reponse-A.md` E2' |
| B | Lois **figées** sans retour, évaluées sur l'épreuve partagée et sur une fraîche ; différence normalisée des log-richesses ; simulation d'abord. | sél/`E3-T3-reponse-B.md` E4 |
| C | Par défaut, une tranche fraîche d'au moins 300 épisodes par génération ; simulation sous nul hétérogène où les meilleures reproduisent même sous le seuil (sinon l'extinction masque la fuite) ; une fuite constatée rend « épreuve neuve à chaque génération » obligatoire. | sél/`E3-T3-reponse-C.md` (c) 2.2, E2 |
| D | Plan factoriel épreuve × sélection × mémoire, nul global puis mélange ; la banque réelle fraîche viendra en confirmation séparée ; aucune « preuve générale à venir » pour sauver un résultat. | sél/`E3-T3-reponse-D.md` E2 |
| E | Banque croissante, lots disjoints attribués après gel ; un lot consommé peut devenir développement, jamais redevenir confirmation ; sélection et mémoire manipulées séparément ; sans contrôle positif d'adaptation, aucune conclusion de sûreté. | sél/`E3-T1-conception-E.md` B ; sél/`E3-T3-reponse-E.md` |
| Argon seul | Partition fraîche par génération (coût G × 144 à 300 épisodes), ou budget d'erreur divisé entre générations ; option « révélation bruitée ». | lecture vérifiée v2, § 1.2 |
| Kimi seul | Partie jamais vue par génération ; banque croissante si seul le segment neuf sert d'épreuve ; rotation insuffisante ; réutilisation exploratoire seulement. Confiance 0,93. | lecture vérifiée v2, § 2.2 |

- **Accord unanime** : une épreuve jamais vue par génération pour confirmer ; la réutilisation n'est qu'exploratoire.
- **Accord** (A, B, C, D) : trancher d'abord en simulation sur processeur, à 0 USD.
- **Accord** (A, D, E ; critique de B rapportée par A) : la **mémoire transmise** est un canal de fuite à manipuler à part de l'épreuve.
- **Propre à une espèce** : « filles de parents tirés avant verdict » comme niveau non sélectionné (A) ; « lot consommé → développement, jamais confirmation » (E) ; révélation bruitée (Argon seul).

### Q3 — Héritage

| source | position (avis) | où |
|---|---|---|
| A | À trancher par un essai à quatre bras appariés en longueur (survivantes seules ; plus éliminées avec raison exacte ; sans raison ; raisons permutées), vérité des redites scellée par un metteur en forme tiers ; sans gain, les éliminées vont à la mémoire seulement, jamais aux proposeurs. | sél/`E3-T3-reponse-A.md` E3' |
| B | La mémoire anti-redite est à éprouver sur quatre croisements (paraphrase ; même loi, mots disjoints ; autre loi, mots partagés ; contrôle), au moins 40 paires par classe, sur processeur. | sél/`E3-T3-reponse-B.md` E6 |
| C | Par défaut, servir aux proposeurs les seules survivantes, anonymisées, **avec leur gain de richesse** ; la mémoire mécanique garde les mortes ; essai à appels fixes, texte neutre de même longueur, canoniseur tiers gelé. | sél/`E3-T3-reponse-C.md` (c) 2.2, E3 |
| D | Canoniseur tiers indépendant des bras ; bras codes minimaux, motifs complets, texte neutre, motifs permutés ; transmettre le rang risque une sélection par jugement détournée. | sél/`E3-T1-conception-D.md` ; sél/`E3-T3-reponse-D.md` E3 |
| E | Transmettre engagement, domaine, preuves, incertitude, provenance, données consommées, raison d'échec ; **pas de rang** par défaut ; la mémoire interdit le même engagement sur le même domaine, pas le voisinage lexical. | sél/`E3-T1-conception-E.md` B |
| Argon seul | Dissociation : survivantes et agrégats aux proposeurs, éliminées au noyau ; option : servir l'arbre syntaxique canonisé ; transmet le classement dans sa variante A. | lecture vérifiée v2, § 1.2 |
| Kimi seul | Archive probatoire complète conservée, vue servie réduite ; rang = métadonnée d'audit ; éliminées en vue minimale ; « même engagement réfuté » ≠ « domaine interdit ». Confiance 0,76. | lecture vérifiée v2, § 2.2 |

- **Accord** : archive complète au noyau, vue réduite aux proposeurs ; risque d'ancrage par le texte intégral des mortes (A sous condition, C, D, E, Argon seul, Kimi seul).
- **Accord** (A, B, C, D) : l'héritage se tranche par un essai à longueur et appels appariés, avec un canoniseur ou une vérité de redites **tiers**, jamais la mémoire qu'on évalue.
- **Accord** (E, Kimi seul ; B par son « piège lexical ») : refuser le même engagement, pas le vocabulaire voisin.
- **Divergence** : le rang ou le score. Non transmis : D, E, Kimi seul. Transmis : Argon seul (classement), C (gain de richesse servi aux proposeurs). Servir un score du juge aux proposeurs touche l'invariant « aucun score de moniteur dans l'entraînement de l'agent » (N-053) ; A note que ce pare-feu protège l'affinage, pas la sélection entre générations (sél/`E3-T1-conception-A.md` S8). C'est un point à trancher par Lazar, pas par cette note.
- **Propre à une espèce** : vérité des redites scellée par un metteur en forme tiers (A) ; contrôle « éliminées sans raison » complété par un texte de catalogue apparié (A). À rapprocher du bras « héritage réduit au meilleur » ou « oublier » que Lazar a demandé (R-2528) : aucune espèce ne le propose sous ce nom.

### Q4 — Sortie vers le programme

| source | position (avis) | où |
|---|---|---|
| A | Grille à quatre états (redite d'une hypothèse ; l'affine ; neuve dans le périmètre ; hors périmètre) ; mesure primaire = exactitude sur témoins scellés (reparamétrisations, paraphrases, voisines réellement distinctes, hors périmètre ; prévalence plantée ≈ 0,5), accord entre lecteurs en second ; « décisive pour une porte » n'a pas d'estimateur. | sél/`E3-T3-reponse-A.md` E5' |
| B | Aucun critère mécanique de nouveauté n'est décrit dans les pièces : la règle reste une hypothèse. | sél/`E3-T3-reponse-B.md` (c) |
| C | Lecteur neuf (R13) sur trois critères : distance prédictive non nulle aux hypothèses, porte nommée avec seuil chiffré, coût sous le plafond de la porte ; hypothèses existantes reformulées comme témoins **négatifs** ; une hypothèse tenue à part comme témoin positif. | sél/`E3-T1-conception-C.md` Q4 ; sél/`E3-T3-reponse-C.md` (a) 1 |
| D | Banc à vérité connue pour la porte de sortie (paraphrases, reparamétrisations, nouveautés réelles, nouveautés triviales) ; sortie seulement après nouveauté documentée, porte nommée, coût borné **et GO de Lazar**. | sél/`E3-T3-reponse-D.md` |
| E | Contrat en cinq points : tableau de différences avec toutes les hypothèses et leurs décisions modificatives (HC6, L, T, Tr compris) ; antériorité la plus proche ; porte ; branche favorable et défavorable, chacune avec une décision différente ; protocole confirmatoire indépendant, coût, arrêt. Lecteur neuf avant la dépense, R13 après le résultat ; un résultat exploratoire ne reçoit jamais de préenregistrement rétroactif. | sél/`E3-T1-conception-E.md` B |
| Argon seul | Quatre portes (survie double, nouveauté externe et interne, décisivité, coût) ; table formelle des signatures des hypothèses ; les lois du programme comme nul informé. | lecture vérifiée v2, § 1.2 |
| Kimi seul | Identité probatoire, nouveauté revendicable, porte nommée **avant** l'expérience avec une règle pour chaque issue, coût borné ; le lecteur R13 n'établit pas la nouveauté bibliographique ; la sortie peut être une restriction ou une réfutation d'une hypothèse existante. Confiance 0,82. | lecture vérifiée v2, § 2.2 |

- **Accord** : un contrat écrit à plusieurs conditions (nouveauté contre le référentiel entier, porte nommée, coût borné), lu par un lecteur neuf ; la promotion seule ne suffit pas.
- **Accord** (A, C, D) : éprouver ce lecteur sur des **témoins à vérité scellée**, reformulations d'hypothèses existantes comprises.
- **Accord** (E, Kimi seul) : décisions écrites pour chaque issue avant l'expérience.
- **Propre à une espèce** : grille « hors périmètre » contre le défaut de case (A, pris d'une critique de C) ; « jamais de préenregistrement rétroactif » (E) ; sortie comme restriction ou réfutation (Kimi seul).
- **Remarque du lecteur, pas des espèces** : le référentiel du 1er novembre n'est plus celui d'aujourd'hui (HC2 reformulée par N-068, papier B resserré par N-069, H9 retirée par N-070). Le témoin positif « H9 tenue à part » proposé par C n'a plus le même sens.

### Q5 — Diversité et coût

| source | position (avis) | où |
|---|---|---|
| A | Simulation sur 10 générations, 3, 10 ou 30 lignées initiales, référence = concentration sous **reproduction neutre** sur le même graphe de parenté (crédit à E) ; contribution d'un demi par parent ; la perte de diversité commence avant toute sélection (17 idées pour 29 fiches en course 1, d'après les pièces) ; séparer rendement et héritabilité. | sél/`E3-T1-conception-A.md` S10 ; sél/`E3-T3-reponse-A.md` E6' |
| B | Peu sur la diversité ; coût de l'ablation dimensionnée ≥ 60 USD (illustratif). | sél/`E3-T3-reponse-B.md` |
| C | Grille de niches axe du programme × famille d'opérateur, au plus 2 parents par cellule (illustratif) ; coût complet amorti par découverte vérifiée, par couche. | sél/`E3-T1-conception-C.md` Q5 |
| D | Garde contre plafond simple contre rien ; concentration et couverture en diagnostic, jamais en critère ; reproduction neutre ; descripteurs permutés. | sél/`E3-T3-reponse-D.md` E4 |
| E | La diversité règle l'allocation, jamais la vérité ; places par mécanisme et domaine, pas par fournisseur ni vocabulaire ; **ne pas fabriquer de survivantes pour remplir un quota** ; coûts comptés à part (appels, heures, données, traduction, témoins, échecs, temps humain) ; coût principal = par hypothèse distincte confirmée indépendamment ; sans confirmation, publier coût total et rendement nul. | sél/`E3-T1-conception-E.md` B |
| Argon seul | Quotas par niche axe × opérateur et plafond de descendance, ou pénalisation par lignée ; coût amorti par survivante neuve ; pire cas : famine budgétaire par réservation. | lecture vérifiée v2, § 1.2 |
| Kimi seul | Garde généalogique et fonctionnelle, descripteurs gelés avant ; trois ratios, numérateur complet ; coût par élimination correcte. Confiance 0,72. | lecture vérifiée v2, § 2.2 |

- **Accord** : niches fonctionnelles (axe, mécanisme, opérateur) avec plafond de descendance (C et Argon seul, même modèle ; E ; Kimi seul ; D en diagnostic).
- **Accord** (A, D, E) : juger la garde contre une **reproduction neutre** de même graphe de parenté.
- **Accord** : numérateur complet, échecs et banques compris, dénominateur en hypothèses distinctes confirmées (A, C, E, Argon seul, Kimi seul).
- **Propre à une espèce** : « ne pas fabriquer de survivantes » et « publier le rendement nul » (E) ; « la diversité se perd avant la sélection » (A) ; coût par élimination correcte (Kimi seul).

### Q6 — Ablation « génération 2 avec et sans filtre du pôle »

| source | position (avis) | où |
|---|---|---|
| A | **En l'état, non jugeable** : conditionnelle aux dents du pôle et à au moins 3 populations indépendantes par bras. Cinq bras à nombre égal de filles : promues, éliminées du pôle, **sorties du pont sans verdict du juge** (la critique « la plus lourde », reçue de C : ce qui s'hérite peut n'être que la traduisibilité), juges-modèles restreints aux fiches passées par le pont, aléatoire. Confirmation terminale à horizon fixe sur épreuve fraîche, **contre le nul informé** ; part de filles confirmées et coût rapportés séparément. | sél/`E3-T3-reponse-A.md` E4' |
| B | Audit final commun ; quatre bras (avec pôle, sans pôle, traduisibles non jugées, parents aléatoires) ; témoins « creux mais conformes » ; sous-dimensionné sous 40 fiches par bras (puissance ≈ 0,55 à 40, illustratif). | sél/`E3-T3-reponse-B.md` E5 |
| C | Bassins tous conditionnés sur l'admissibilité au pont (pôle, juges-modèles, aléatoire, pôle inversé) ; audit terminal à deux critères (procédure par bras, et test de permutation à horizon fixe sur le score prédictif) ; si l'héritage utile est réfuté, **arrêt de la reproduction sur plusieurs générations** au profit d'une génération 1 élargie. | sél/`E3-T3-reponse-C.md` E4 |
| D | Deux comparaisons : mécanisme (effectifs fixés) et politique (budget égal) ; audit confirmatoire **indépendant** de la sélection, le juge du pôle en robustesse seulement ; la persistance demande plusieurs générations. | sél/`E3-T3-reponse-D.md` E5 |
| E | Contraste causal à volume fixé, promues contre parents aléatoires admissibles ; contraste économique à budget égal, séparé ; option manquante : une **allocation indépendante** des tests jusqu'à démonstration d'une fécondité héritée ; un résultat indécis au plafond garde l'allocation indépendante « sans prétendre avoir réfuté l'héritabilité ». | sél/`E3-T1-conception-E.md` ; sél/`E3-T3-reponse-E.md` |
| Argon seul | Deux bras, adjudication commune sur épreuve fraîche ; jugeable si au moins 3 promues en génération 1 ; « par euro » biaisée contre le bras filtré. | lecture vérifiée v2, § 1.2 |
| Kimi seul | Répétitions de la boucle entière ; adjudication commune ; bras **filtre aléatoire de même sélectivité** ; zéro survivante partout = non concluant. Confiance 0,86. | lecture vérifiée v2, § 2.2 |

- **Accord unanime** : audit terminal commun sur données jamais vues, gelé avant, jamais utilisé pour choisir les parents.
- **Accord** (A, B, C, D, E, Kimi seul) : un bras de **parents aléatoires** (ou de même sélectivité) à effectifs appariés.
- **Accord** (A, B, C, D) : séparer l'effet du juge de celui de la **traduisibilité** par le pont.
- **Accord** (A, D, E, Argon seul, Kimi seul) : « survivantes neuves par euro » ne peut pas être la mesure primaire ; mécanisme et rendement sont deux questions.
- **Accord** (A, B, C, Argon seul) : non jugeable à l'effectif actuel.
- **Divergence** : le nul de l'audit. Garder le nul informé du pôle (A, E : en changer change la question) contre une procédure indépendante, le juge du pôle en robustesse seulement (D) ; C prend les deux en co-primaires.
- **Divergence** : le repli si l'héritage n'est pas montré. Arrêt du multi-générations (C) ; allocation indépendante provisoire (E).

### Q7 — Ce qui existe

Toutes les sources donnent POPPER pour le voisin le plus proche, à lire en premier sur PDF (A, B, C, Argon seul, Kimi seul ; D et E disent « références à vérifier ») ; aucune ne reprend un système entier ; aucune ne revendique une zone vierge (D : « je ne revendique donc aucun vide bibliographique »). **Toutes ces références sont non vérifiées (R7)** ; les lectures vérifiées signalent un titre suspect de POPPER chez Kimi seul et un couple titre-identifiant suspect chez Argon seul. **Affirmation à ne pas reprendre** : C écrit que « la littérature … montre que passer l'archive négative brute dans la fenêtre de contexte d'un LLM crée un biais d'ancrage lexical » (sél/`E3-T1-conception-C.md` Q3) sans source vérifiable : c'est une hypothèse, que les expériences d'héritage de A, C, D et E proposent précisément de tester.

### Première expérience proposée (sélection)

| A | B | C | D | E |
|---|---|---|---|---|
| courbe de puissance à petit nombre de fiches et simulation de diversité (0 USD), puis dents du pôle sur épreuve fraîche ; nœud : devis de l'épreuve fraîche | mémoire et fuite en simulation (0 USD), puis pont (≤ 5 USD), puis devis de l'épreuve fraîche, puis dents | fuite en simulation (0 USD) et pont étalonné (2 à 5 USD), puis deux tranches d'épreuve fraîches (25 à 45 USD, illustratif) | fidélité et couverture du pont contre l'extracteur mécanique, sans carte graphique | « pont fidèle et utile », et préparer en parallèle l'épreuve fraîche |

- **Accord** (B, C, D, E) : qualifier le **pont** avant toute sélection. **Accord** (A, B, C, E) : le **devis d'une épreuve fraîche** est le nœud qui commande le reste. Le registre rapporte depuis une épreuve fraîche du pont jugée « inutile en l'état » (0 fiche traduite sur 15, `registres/etat.md` l. 316, R-990) : la priorité « pont d'abord » du collisionneur précède ce constat.

---

## 2. Vérification non circulaire du bac à sable

### Q1 — Base de confiance et ce que change une machine virtuelle légère

| source | position (avis) | où |
|---|---|---|
| A | Sans oracle de correction par fiche, la vérification ne peut porter que sur **quatre propriétés** : identité (hachage hors machine), portabilité (rejeu), dépendance à la donnée (tranche jumelle), confinement. La **correction** est hors de portée de tout ce qui est proposé ; le verdict « survit » doit être libellé « identique, portable, dépendant de la donnée, confiné », jamais « correct ». « L'empreinte n'est qu'un index ; la vérification est le rejeu. » | bac/`E3-T1-conception-A.md` (e) ; bac/`E3-T3-reponse-A.md` (c) |
| B | La v48 sépare déjà producteur et vérificateur ; la circularité d'Avalon « ne s'applique pas directement ». Trois menaces à ne pas mêler : sondage accidentel ; script qui trompe délibérément (question de préenregistrement, pas de bac) ; entraînement en boucle sur le vérificateur (hors portée tant que l'organisme ne s'entraîne pas). | bac/`E3-T1-conception-B.md` ; bac/`E3-T3-reponse-B.md` (c) |
| C | Base : matériel et hyperviseur du loueur, noyau hôte, démon de hachage hors du bac, canal d'archives ; exclus : interpréteur, bibliothèques, code de l'agent, dossier de travail. Machine virtuelle légère ou gVisor changent la classe ; `bwrap` durci suffit (0,85) si le vérificateur est la session ; option manquante : WebAssembly. Deux menaces : d'infrastructure, et **épistémique** — un script parfaitement confiné peut imprimer un chiffre sans lire les données ; ni hachage, ni attestation, ni second bac, ni tiers ne le détectent. | bac/`E3-T1-conception-C.md` Q1 ; bac/`E3-T3-reponse-C.md` (c) 1 |
| D | Séparer provenance, confinement, correction, détection ; une empreinte externe lie des octets **reçus**, pas l'entrée exécutée : capture par un composant indépendant **avant** exécution ; l'analyseur d'entrée entre dans la base. | bac/`E3-T1-conception-D.md` (a) |
| E | Une base par propriété (confinement, provenance, correction) ; le producteur **et son auto-déclaration de réussite** en sont exclus ; une machine virtuelle change le confinement, pas la validité ; réception et décodage dans un environnement limité, pas sur le poste de Lazar. | bac/`E3-T1-conception-E.md` B ; bac/`E3-T3-reponse-E.md` C |
| Argon seul | Trois lieux (hôte vérificateur, canal, hôte d'exécution) ; la machine virtuelle légère change la classe ; déporter le vérificateur suffit à briser la circularité même sous `bwrap` (0,85) ; WebAssembly. | lecture vérifiée bac v2, § 1.2 |
| Kimi seul | Tout ce dont l'altération change sans détection l'exécution, les preuves ou le verdict ; la machine virtuelle légère déplace la frontière sans supprimer le besoin d'une racine indépendante ; quatre propositions : identité, provenance, non-ingérence, validité sémantique. | lecture vérifiée Kimi v1, § 2 |

- **Accord unanime** : une machine virtuelle légère change le **confinement**, pas la circularité ni la validité.
- **Accord** (A, C, D, E, Kimi seul) : séparer les propriétés (identité ou provenance, confinement, correction) et ne jamais appeler « vérifié » ce qui n'est que provenant.
- **Accord nouveau du collisionneur, absent des avis d'espèce seule** : le chiffre décisif imprimé par le script de l'agent (ligne `RESULTAT:`) est une **auto-déclaration** que le confinement ne vérifie pas. A (correction hors de portée, verdict libellé), C (politique triviale, menace épistémique), D (expérience de correction), E (producteur et auto-déclaration exclus), B (scénario 2, laissé au préenregistrement). Les lectures vérifiées notaient qu'Argon seul et Kimi seul n'avaient pas traité ce point, central dans la réponse propre de conv-audit (lecture bac v2 § 1.5 ; lecture Kimi v1 § 5). Réserve 3 : cet accord s'est formé après la critique croisée.
- **Divergence** : B tient la circularité d'Avalon pour non directement applicable à la v48 ; A, C, D, E la tiennent pour présente sous sa forme épistémique.
- **Propre à une espèce** : libellé du verdict par ce qu'il engage (A) ; capture avant exécution (D) ; décodage de l'archive hors du poste de Lazar (E) ; WebAssembly (C et Argon seul, même modèle).

### Q2 — Séparer produire et vérifier : le canal

| source | position (avis) | où |
|---|---|---|
| A | Le **dossier de travail partagé** par les trois exécutions d'une fiche est un canal intra-fiche que la question ne nomme pas ; la v48 n'interdit pas un cache entre exécutions : question de contrat à Lazar (interdire par remise à zéro, ou déclarer). Avant tout essai entre générations, comparer octet à octet deux transcriptions de même verdict : tout champ variable non déclaré est un canal. Essai 1 exécution contre 3, à retours aléatoires de même quota. | bac/`E3-T3-reponse-A.md` thèmes 16-17, E5', E6 |
| B | Essai « opacité du bac » en priorité (contenu non repris, voir exclusions) ; fixer le modèle de menace. | bac/`E3-T3-reponse-B.md` |
| C | Garde d'**arrêt au premier succès** : la fiche se clôt à la première exécution valide ; en cas d'erreur, ne rendre que le nom de l'exception et la ligne, jamais une valeur tirée des données ; un désaccord du lecteur valant « non concluant », une injection de texte ne peut que saboter, pas faire survivre. | bac/`E3-T1-conception-C.md` Q2 ; bac/`E3-T3-reponse-C.md` (a) 2, (c) 3 |
| D | L'hypothèse « l'optimiseur ne voit que le verdict » est contraire à la v48 servie ; un verdict binaire répété reste un canal ; essai de l'exploitation du retour à exécution unique, sans retour, à retours aléatoires de même quota. | bac/`E3-T1-conception-D.md` (a) ; bac/`E3-T3-reponse-D.md` E3, E9 |
| E | Le producteur ne reçoit ni traces du vérificateur, ni diagnostics riches ; essai retour fidèle / placebo / aucun / non adaptatif, à opportunités égales ; enregistrer **ce que voit effectivement le producteur**. | bac/`E3-T1-conception-E.md` B ; bac/`E3-T3-reponse-E.md` |
| Argon seul | Boucle intra-fiche large, boucle entre générations étroite (≈ 2 bits par test) ; gabarit strict des retours ; option : un seul tour. | lecture vérifiée bac v2, § 1.2 |
| Kimi seul | Une empreinte calculée dans le bac n'est qu'une déclaration ; tableau générique des fuites (contenu, métadonnées, temps, ressources, verdict répété, état partagé). | lecture vérifiée Kimi v1, § 2 |

- **Accord** (A, C, D, E, Argon seul) : le canal qui compte est la **boucle de retour dans la fiche** (exécutions répétées, sorties servies) ; il se teste contre un placebo ou des retours aléatoires de même quota.
- **Accord** (A, C, Argon seul) : réduire à une exécution ou s'arrêter au premier succès est une option sérieuse.
- **Accord** (A, D, E) : auditer la transcription réellement visible, pas le contrat déclaré.
- **Propre à une espèce** : le **dossier de travail partagé** comme canal et sa question de contrat (A) ; erreurs rendues sans valeur numérique (C). Kimi seul nommait l'« état partagé » dans un tableau générique, sans le rattacher au dossier de la v48.

### Q3 — Attestation

- **Accord unanime** : l'attestation matérielle vise une autre menace (l'opérateur du nuage) et **peut attendre** (A, B, C : confiance 0,10 sur elle contre la menace d'Avalon, D, E, Argon seul, Kimi seul).
- **Accord** (A, B, D, Argon seul, Kimi seul) : un journal d'appels système ne vaut que par son point d'observation et sa couverture mesurée. B retire son instrument de journal, jugé vide de cas positifs sous un montage en lecture seule (bac/`E3-T3-reponse-B.md`) ; A n'admet le journal au verdict qu'au-dessus d'une couverture mesurée (0,95, illustratif).
- **Accord** (D, E, Kimi seul) : identité des octets, liaison à une exécution et correction sont trois affirmations distinctes.
- **Propre à une espèce** : preuve que le script a **lu** les fichiers de données déclarés au préenregistrement, contrôlée hors du bac (C, bac/`E3-T1-conception-C.md` Q3) ; dépendance du résultat à la donnée par **tranche jumelle** de même schéma (A, E1b) : deux mécanismes différents pour le même défaut (un chiffre produit sans regarder les données) ; épinglage des paquets par empreinte dans l'amorce (A).

### Q4 — Redondance diverse

- **Accord unanime** : nulle contre une erreur commune ou sémantique (même chiffre faux rendu par les deux bacs) ; témoin obligatoire « même bac deux fois » pour la variance propre ; un désaccord vaut « non concluant », jamais un vote (D).
- **Accord** (A, B, C, D, E, Argon seul) : elle peut attendre qu'un besoin soit montré.
- **Divergence** : quelle diversité. Diversité d'infrastructure (`bwrap` sur deux images chez A, `bwrap` contre gVisor chez B et C, sélective sur les seules « survit » chez Argon seul) ; contre **diversité des données** (C : rejouer sur une tranche dont la cible est permutée ; tient que cela apporte plus que deux bacs, 0,80). A objecte qu'une seule permutation rejette un test honnête avec probabilité α ; C répond par une batterie de 19 permutations par blocs avec deux conditions (bac/`E3-T3-reponse-C.md` (a) 3) — dessin non éprouvé, chiffres illustratifs.
- **Propre à une espèce** : « l'optimiseur peut apprendre le prédicat d'acceptation conjoint des deux bacs » (Kimi seul) ; le second environnement doit détecter au moins une erreur étiquetée de l'extérieur que manquent le bac seul et sa duplication (D).

### Q5 — Mesurer le sondage : les canaris

- **Accord unanime** : un canari mesure des **contacts** avec des leurres, pas le sondage ; zéro contact ne s'écrit jamais « aucun sondage » ; il faut le comparer à une télémétrie ou une **liste blanche** d'accès sans leurre (A en prérequis, B, C, D, E, Argon seul, Kimi seul).
- **Accord du collisionneur (cinq sur cinq)** : corpus de calibration et corpus de test **disjoints**, seuil et canaris gelés avant le corpus réservé ; témoins positifs écrits par une main qui ignore l'emplacement des détecteurs.
- **Divergence** : les fausses alertes. « Théoriquement nulles » chez Argon seul ; estimées sur un corpus honnête réservé avec une borne (Clopper et Pearson) chez Kimi seul et les cinq espèces du collisionneur. C, qui donnait au premier tour 0 % de fausses alertes après soustraction du profil de base, passe à une borne mesurée sur 100 scripts réservés au troisième tour (bac/`E3-T1-conception-C.md` Q5 ; bac/`E3-T3-reponse-C.md` (a) 4).
- **Propre à une espèce** : une classe de sondes **hors système de fichiers**, dont la non-détection est attendue et comptée comme couverture manquante (A) ; alerte sur ouverture de fichier seulement, jamais sur simple listage (C) ; oracle fonctionnel tenu en réserve et mutations contrôlées du vérificateur (Kimi seul).

### Q6 — Suites publiques d'étanchéité

- **Accord unanime** : mêmes candidates (suite de bubblewrap, essais d'appels système de gVisor, essais de Firecracker, Linux Test Project, kselftest ou runtime-tools), **liens et révisions à vérifier** ; un succès est une condition nécessaire d'hygiène, jamais une preuve ; une suite éprouve l'outil, pas notre ligne de commande ; un échec arrête. Aucune espèce ne propose une suite de rejeu de failles. C nomme « Linux Test Project, `containers` et `syscalls` » sans en restreindre le sous-ensemble : à vérifier au choix.
- **Propre à une espèce** : D (Kimi) demande d'éprouver la **sensibilité** de la suite elle-même : toute ablation préclassée d'une garde couverte doit faire tomber le vert, une ablation fantôme doit le laisser ; un vert après une ablation non couverte réfute « vert ⇒ toutes les gardes présentes » (bac/`E3-T3-reponse-D.md` E6). Kimi seul proposait déjà des mutations du vérificateur : c'est le même modèle.

### Q7 — Ordre et coût

- **Accord unanime** : rien avant que S0 et S1 aient réellement tourné ; la v48 n'a exercé aucun `bwrap` réel (A, B, D, E le disent vérifié dans les pièces) ; machine virtuelle légère, attestation et redondance systématique attendent.
- **Accord** (D, E, Kimi seul ; A par son libellé) : **fixer d'abord ce que le verdict veut dire**.
- **Accord** (D, E) : les verdicts restent exploratoires et **ne deviennent jamais un signal de récompense** tant que le portail n'est pas éprouvé.
- **Divergence sur la première expérience** :

| A | B | C | D | E |
|---|---|---|---|---|
| S1 augmentée : rejeu de ≈ 20 scripts honnêtes et des sondes déjà écrites, même environnement deux fois et autre image, plus l'artefact témoin du dossier partagé ; < 0,2 USD au-delà de S1 (illustratif) | essai d'opacité du bac sur S0, < 1 USD ; séquence complète ≈ 35 à 45 USD (illustratif) | pendant S1 : liste blanche gelée puis corpus réservés, et batterie de permutations ; < 0,08 USD (illustratif) ; trois gardes mécaniques à ajouter au lanceur | geler la liste des contrôles et une petite banque indépendante, puis portail minimal en S0 et S1 réels ; capture avant exécution ensuite ; expérience de correction avant toute prétention de correction | « contrat vérifiable » sur une classe restreinte de fiches, avant diversité, canaris ou attestation ; 20 USD illustratifs ; mesurer d'abord le temps d'écriture d'un contrat |

---

## 3. Fusion : ce qui sert directement la course de l'organisme à plusieurs générations

Ce qui suit est une **mise en ordre des avis**, préenregistrable, attribuée ; ce n'est ni une décision ni une recommandation chiffrée. Je n'ai pas lu la conception v4 ni le brouillon 3 du préenregistrement (R-3051) : chaque point est à confronter à ces pièces.

### 3.1 Sélection entre générations

1. **États de fiche** (accord, six sources) : au moins « réfutée », « en attente ou différée », « promue », plus « invalide techniquement » (E). Seule la promue engendre. À trancher par Lazar, car les avis divergent : le sort de la non-concluante (retirée, C ; différée avec retour sur données neuves, D et E ; dormante, Argon seul), et la contradiction relevée par A entre la conception du pôle et la règle « une non-concluante ne passe pas ».
2. **Contrôle des fausses découvertes** : appliquer la procédure à toutes les lois admissibles de la génération, nombre fixé avant l'issue ; ne pas filtrer après sans justifier l'ensemble annoncé (E) ; écrire qu'aucune garantie ne couvre l'archive cumulée (D, E, Argon seul, Kimi seul). La pondération reste ouverte (C et Argon seul pour, Kimi seul contre).
3. **Préalable sur processeur, 0 USD** (A) : courbe de puissance à 5, 10, 20 et 50 fiches, deux lois vraies, trois forces. Elle dit si une génération de cette taille peut promouvoir quoi que ce soit ; c'est la question que A, B et C posent sous trois formes.
4. **Épreuve** (accord unanime) : jamais vue par génération pour confirmer ; lot consommé → développement, jamais confirmation (E) ; la mémoire transmise est un second canal de fuite, à manipuler séparément (A, D, E). Le dessin qui le tranche (simulation 2 × 2 × 2, ou épreuve × sélection × mémoire) se joue sur processeur (A, B, C, D).
5. **Héritage** : archive complète au noyau, vue réduite aux proposeurs ; la mémoire refuse le même engagement sur le même domaine, pas le vocabulaire ; l'essai qui tranche apparie longueurs et appels et prend sa vérité de redites d'un tiers (A, B, C, D, E). **À trancher par Lazar** : servir ou non aux proposeurs un rang ou un gain de richesse (C et Argon seul oui, D, E et Kimi seul non) au regard de l'invariant de N-053. Le bras « héritage réduit au meilleur » demandé par Lazar (R-2528) peut prendre place dans le même plan que les bras de A.
6. **Diversité** : niches fonctionnelles et plafond de descendance, garde jugée contre une reproduction neutre de même graphe ; ne pas fabriquer de survivantes (E).
7. **Ablation** : non jugeable aujourd'hui (A, B, C, Argon seul) ; quand elle le sera : audit terminal commun à horizon fixe, bras de parents aléatoires, bras « sorti du pont sans verdict du juge », mécanisme et budget séparés. Restent ouverts le nul de l'audit (A et E contre D) et le repli (C contre E).
8. **Comptabilité** : numérateur complet (échecs, banques, témoins, temps humain), dénominateur en hypothèses distinctes confirmées ; publier le rendement nul (E, Kimi seul).
9. **Sortie** : contrat écrit (E) éprouvé sur témoins à vérité scellée (A, C, D), contre le référentiel d'**aujourd'hui** (après N-068 à N-070), décisions pour chaque issue gelées avant (E, Kimi seul), GO de Lazar (D).

### 3.2 Tests de mort dans le bac à sable

1. **Le verdict « survit » n'est pas « correct »** (accord du collisionneur, nouveau par rapport aux deux espèces seules) : le libeller par ce qu'il engage (A) et garder ces verdicts exploratoires, hors de tout signal de récompense (D, E), tant qu'aucun contrôle de dépendance aux données ni de correction n'est éprouvé.
2. **Deux gardes peu coûteuses contre le chiffre produit sans regarder les données**, à éprouver sur un cas sain et sur un artefact (R5) : la tranche jumelle (A) et la preuve de lecture des fichiers déclarés (C). La batterie de permutations (C) est un troisième candidat, plus discuté.
3. **Fermer ou déclarer le canal du dossier de travail partagé** entre exécutions (A) : question de contrat posée à Lazar ; l'artefact témoin qu'A décrit en fait un essai de régression hors réseau.
4. **Réduire la boucle de retour dans la fiche** : arrêt au premier succès et erreurs rendues sans valeur (C), ou exécution unique ; à éprouver contre placebo ou retours aléatoires de même quota (A, D, E).
5. **Canaris** seulement avec une liste blanche, des corpus de calibration et de test disjoints et des fausses alertes bornées sur corpus réservé (accord du collisionneur, Kimi seul) ; emplacements jamais écrits là où un agent peut les lire.
6. **Suites publiques** : candidates communes, révisions figées, et éprouver leur sensibilité par ablation des gardes (D).
7. **Ce qui attend** (accord) : machine virtuelle légère, attestation matérielle, redondance systématique.

### 3.3 Ce que la fusion ne dit pas

Aucun de ces avis n'a été joué ; tous les seuils, effectifs et coûts des espèces sont illustratifs ; aucune référence n'est vérifiée sur PDF. Les accords du collisionneur ont été formés au troisième tour, après lecture mutuelle, et deux couples de sources partagent un modèle. Ces avis précèdent la conception v4 de la course, que je n'ai pas lue.

## 4. Points pour Lazar (sans recommandation de ma part)

- Sort de la fiche non concluante entre générations (retirée, différée, dormante) : les avis divergent ; la conception du pôle et la règle du 1er novembre se contredisent (A).
- Servir ou non aux proposeurs un rang ou un score du juge (C et Argon seul contre D, E et Kimi seul), au regard de l'invariant de N-053.
- Cache entre exécutions d'une même fiche dans le bac : l'interdire ou le déclarer (A).
- Le libellé du verdict des tests de mort (« identique, portable, dépendant de la donnée, confiné »), plutôt que « survit », tant que la correction n'est pas éprouvée (A, appuyé par C, D, E).
