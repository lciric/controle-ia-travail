# Contre-lecture du préenregistrement du crible (iii), brouillon 7 (variante « crédits de Claude au maximum ») — tour 1 de la lecture du brouillon 7 — v1

- Lecteur : sous-agent neuf du modèle C (R2), qui n'a écrit aucune des pièces ; auteur de la pièce et rédacteur des corrections à venir : modèle A. Rédigé le 2026-11-16 de 15:08Z à 15:17Z (`date -u`).
- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon7.md`,
  `8be79b00430f06a3f74f5abe9d0985d8246036565c92220c202689d3d004a7fd` (égale à son compagnon).
- Comparée : brouillon 6, `f377e927aab482b39ccda892adc178a1cbfaac7a8042bf9215047f303f72189d` ; rapport du tour 3 de la lecture du brouillon 4,
  `99fb10247b295f053a8ecfa8b6464c0f4b445146cc7f67f970a0de514ec70e2e` (recalculée) ; programme `appliquer-corrections-crible-iii-brouillon7.py`.
- Non lu, par consigne : sortie du pilote MR-2 v14, `diag/`, `runs/`, `donnees/`, 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque, dossiers jetables du premier contre-lecteur.

## Verdict

**« corrections »** : 1 majeure (la ligne d'arrêt « mondes complets + mondes non commencés < 16 », telle qu'écrite, se déclenche à l'instant 0 avec cinq files ; trois couples A1 à A3) et 7 mineures (B1, B2 et B3, C1 à C4, D1 ; onze couples en tout). La conception tient : la variante répond à la question de la note aussi bien que la forme fidèle, aucun défaut ne rend la pièce à refaire. Recommandation de forme : **la variante**, confiance 0,65 (section 3).

## 1. Corrections du tour précédent et différentiel (brouillon 6 vers 7)

- Le tour 3 n'exigeait aucune correction ; le brouillon 7 est une réécriture voulue (R-2992, point 1). Contrôle : les 64 couples de `appliquer-corrections-crible-iii-brouillon7.py`, appliqués en mémoire au brouillon 6 (chaque « ancien » une seule fois), redonnent le brouillon 7 **à l'octet** (comparaison faite) ; le texte n'est donc rien d'autre que ces couples. Le validateur `controle_ia.prereg.problemes` rend `[]` sur le brouillon 7.
- Décisions de la mère retrouvées dans la pièce : R-2977 (mondes séparés de (v) ; dollars au prix public en principal, prix de la configuration en sensibilité, vide ici ; ablation de la frontière aux critères gelés, étage 5 ; GO pour l'essai, non pour l'adoption ; B sur les ensembles de D ; égalités par l'ordre des noms) ; R-2992 (variante ; N = 20 dans tous les cas, ce qui **remplace** la règle « 24 si le taux du pilote est sous 0,95 » : son absence n'est donc pas un défaut ; enveloppe du point 3 ; code neuf du point 5). Le point 2 de R-2992 (étage 5 hors critères gelés) vise (v) seul : voir la section 5.
- Aucun identifiant de modèle (recherche de motifs ; restent les clés de configuration `opus55`, `fable52`, `argon` permises par R-2690). Aucun mot « lettre C » en dehors des entrées historiques.

## 2. Vérifications faites (points 1 à 9 de la consigne)

1. **R1** : hypothèse, prédictions chiffrées avec signe, métrique, seuils, plan d'analyse, critères de lecture à neuf étages, liste d'arrêt, graines : présents. Portes de sortie après lecture : aucune hors la règle III-7 (B1) et la ligne de minimum (A1 à A3). Le texte se déclare lui-même non scellable avant les trois valeurs processeur et la table de mise à jour : le dernier tour (différentiel) reste obligatoire.
2. **R3** : la statistique principale Δ_R = R_D − R_S est défendue avant toute donnée (toujours définie, ρ_DS rapporté seulement) ; elle est de plus cohérente avec III-1 (Δ_R ≤ 0 si et seulement si ρ_DS ≤ 1). Marge de 0,5 : 10 à 17 % de 3 à 5 composantes (juste), choix déclaré. Recompte de puissance de P2 (loi normale, deux bras 97,5 % bilatéral, z = 2,241, n = 20) : à + 0,5, 0,35 (écart-type 1,2) à 0,50 (1,0) ; à + 0,25, 0,10 à 0,13 ; seuil de « sans perte notable » : δ observé sous − 0,10 à − 0,001 : tous égaux à la pièce. Égalités par l'ordre des noms : le générateur permute les traits par monde (`rng.permutation(D)`, `monde_riche_v4.py`, `4b165847…`), donc pas de biais d'indice ; justifié. Bras B : texte servi égal à l'octet à celui de D (garde et mutation), passe 1 payée dans chaque bras, H tiré d'une graine `(r, 40)` indépendante : les bras sont comparables sans fuite. La puissance de P1 n'est pas donnée (à calculer par la simulation écrite ; sans objet pour le scellement tant que la simulation précède).
3. **Forme et crédits** : section 3.
4. **Devis, recompté** : appels 5 × 20 = 100 (Pr-4 : S, H, D = 60 ; Pr-2 : passe 1, B = 40). Attendu 60 × 1,60 + 40 × 0,80 = 128,00 sur crédits, plus 0,30 de machine = 128,30. Pire : 60 × 3,00 + 40 × 2,00 = 260,00, plus 3,00 = 263,00 ; parts 180 et 80 égales. Plafonds de session : 2,00 (`opus55`) et 3,00 (`fable52`) lus au bloc gelé du texte scellé du pilote (`8aa33014…`, lignes de bloc, `git show`) ; les 2,34 sont ceux d'`argon` et d'`astra`, qui ne servent pas ici (ils servent seulement à la forme fidèle : 40 × 2,34 + 60 × 2,00 + 3 = 216,60, juste). Règle du pire cas : (53 024) × 8 + 64 000 × 40 = 2,984 ; (53 024) × 4 + 89 000 × 20 = 1,992 : justes. Fourchettes au prix public : 94,40 à 120,24, plus machine 94,90 à 121,04 : justes ; sonde des gabarits 2,08 à 2,73, au pire 6,96 arrondi à 7,00 : justes. Enveloppe 123 + 483 + 243 + 196,60 + 263 = 1 308,60 : juste (1 315,60 avec la sonde : C3). Ligne GO-2026-11-15-06 (`registres/go.md` à `377a2a0c`, empreinte `4bcec4a0…` recalculée) : l'enveloppe de 1 275 est dépassée par la somme des pires cas (dit par la pièce, nœud de Lazar). Probabilités du minimum (0,5149 ; 0,8586 ; 0,2249 ; 0,0427 à N = 20 ; 0,9276 ; 0,9961 ; 0,7091 ; 0,2943 à N = 24) : recomptées, justes.
5. **Durée** : la pièce fixe **les deux** : cinq files de quatre mondes (monde r vers la file r modulo 5, fixé d'avance) et des bornes de 3 000 s par appel et 7 200 s par monde ; pire cas d'une file 4 × 7 200 s = 8 h, garde de départ 10 h, sous la minuterie de 17 h ; deux étapes en série ≤ 6 000 s < 7 200 s : cohérent. **Faisabilité** : le code du pilote **ne suffit pas**, et la pièce le dit nettement (« le code du pilote ne sert pas tel quel : lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles et mesure sont neufs ») ; la configuration v12 des relais reste inchangée, mais les parts (80 et 180 au lieu de 8 et 12), la garde de départ (10 h au lieu de 12 h 30), la procédure de machine (noms neufs) et un essai à blanc à cinq files sont neufs ; R-2992 (point 5) le confirme (lancement visé du 21 au 24 novembre). Deux réserves : C1 (libellé « deux tours ») et D1 (l'essai à blanc, à relais scriptés, ne peut pas éprouver la limite de débit réelle du fournisseur).
6. **Liste d'arrêt (R5)** : chaque ligne a un essai sain et un artefact ; graines par `numpy.random.SeedSequence` avec clés `(r, 40)`, `(12, r, t)`, `(99, b)`, `(97, k)`, `(96, s)` sans collision ; minimum de 16 mondes complets sur 20 écrit avec sa règle, **mais cette ligne est défectueuse** (A1 à A3). Garde de taille du texte servi absente pour G1 et G2 (B2, B3).
7. **Ablation de la frontière** : B est bien définie (Pr-2 écrit sur les ensembles de D, texte égal à l'octet) et lue à l'étage 5 ; N-045 point 3 (« ablation rapportée, hors des critères gelés ») reste vrai pour les courses et la pièce le dit. Réserve de vocabulaire : B ne retire pas la frontière (C2) ; asymétrie avec (v) : section 5.
8. **R7 et R8** : aucun chiffre de l'état de l'art ; antériorités listées « à chercher » ou « à vérifier » (FunSearch, AlphaEvolve, LLM-Select, LLM-SR, cascades, Jaccard glouton, CADS non lu) ; citations obligatoires de N-064 et N-067 présentes, empreintes des quatre PDF et de la fiche Co-Scientist recalculées justes.
9. **Empreintes** : toutes les empreintes entières de la pièce recalculées par `sha256sum` : justes pour les 46 listées (celles des branches par `git show` : procédure v14 `20355627…`, texte du pilote `8aa33014…`, lecture des prix `b88253b8…`, registre `4bcec4a0…`) ; les deux programmes de l'annexe A et leurs sorties (`f06bcfe7…`, `5d53092e…`, `8c0432df…`, `319fa358…`) **ne sont pas dans le dépôt** mais se rejouent : les programmes recopiés ont bien ces empreintes et les sorties rejouées (quelques millisecondes, bibliothèque standard) ont bien celles de la pièce (C4). La section « Contre-lecture » porte, pour chacune des six entrées, les deux empreintes entières, toutes justes.

## 3. Forme du crible et crédits

- **Forme fidèle** (Pr-1 `argon` choisit, Pr-2 écrit) : 58,30 attendus, dont 10,30 hors crédits ; 216,60 au pire, dont 96,60 hors crédits. **Variante** (Pr-2 choisit, Pr-4 écrit) : 128,30 attendus, dont 0,30 hors crédits ; 263 au pire, dont 3 hors crédits.
- **Laquelle répond à la question de la note en mettant le plus possible sur crédits de Claude** : la variante (99,8 % de l'attendu, 98,9 % du pire sur crédits, contre 82 % et 55 % pour la forme fidèle). Elle garde la structure (un choisisseur moins cher, un écrivain plus cher, quatre bras, filtre, mesures) et le contraste de prix de 2 aux deux barèmes ; la forme fidèle ne tient ce contraste qu'au prix public promotionnel d'`argon` (2 / 10 jusqu'au 30 novembre, 4 / 20 ensuite, égal alors au prix d'`opus55`) et le perd au barème de la configuration (`argon` 10 / 50, plus cher qu'`opus55`).
- **La variante change-t-elle la question ?** Oui, un peu, et la pièce le dit sans trancher : la question « choisir pas cher, écrire cher, par dollar » est la même ; mais « le cher est-il nécessaire ? » porte sur deux paliers d'une même maison, non sur une autre maison ni sur l'instrument local (QO1 au sens complet n'est jouée dans aucune des deux formes). Gain : une question de composition plus actionnable pour l'organisme (quel palier pour quel rôle, N-045 point 1). Perte : la diversité d'espèces.
- **Coût réel du choix** : la variante épargne 10 USD hors crédits à l'attendu (93,60 + 3 au pire) mais consomme 80 USD de crédits de Claude en plus (128 contre 48 attendus ; 260 contre 120 au pire) : « crédits au maximum » est tenu, mais la consommation de crédits quasi triple ; le solde est à vérifier par la mère (point 13 de la pièce).
- **Recommandation nette** : retenir la variante (déjà tranchée par R-2992), **confiance 0,65**, à condition que le solde de crédits couvre 260 + 7 USD au pire en plus des autres usages ; sinon, la forme fidèle se joue plus tard pour 58 USD attendus. Aucune des deux ne change un critère de la pièce.

## 4. Corrections exigées (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans le brouillon 7, vérifié ; appliqués en mémoire, le validateur rend `[]`)

- **A1** (majeure)
  - ancien : `| mondes complets obtenus + mondes non commencés < 16, **quelle qu'en soit la cause** (fournisseur, tronquage, coupure, minuterie) |`
  - nouveau : `| mondes complets obtenus + mondes en cours (comptés comme pouvant devenir complets) + mondes non commencés < 16, **quelle qu'en soit la cause** (fournisseur, tronquage, coupure, minuterie) ; évalué à chaque fin de monde ; à l'instant 0 : 20 |`
- **A2** (majeure)
  - ancien : `| panne d'un appel : continue |`
  - nouveau : `| démarrage (0 complet, 5 en cours, 15 non commencés) : continue ; panne d'un appel : continue |`
- **A3** (majeure)
  - ancien : `| 0 | une ligne d'arrêt déclenchée ; la mesure en erreur |`
  - nouveau : `| 0 | une ligne d'arrêt déclenchée, **sauf** la ligne « mondes complets + mondes en cours + mondes non commencés < 16 », dont l'issue est celle de l'étage 1 ; la mesure en erreur |`
- **B1** (mineure)
  - ancien : `Tout autre chiffre reste celui de ce texte, **hors** trois valeurs`
  - nouveau : `**III-7 se refait par une règle écrite ici** : $_D/$_S = 1 + (coût moyen d'un appel de passe 1 de Pr-2 lu à la sonde des gabarits, au prix public) / (coût moyen d'un appel de Pr-4 lu au pilote, au prix public), donné en fourchette de ± 0,05 ; sans sonde jouée, III-7 reste 1,05 à 1,25 ; aucune autre prédiction ne se refait. Tout autre chiffre reste celui de ce texte, **hors** trois valeurs`
- **B2** (mineure)
  - ancien : `| empreinte différente : texte, monde, gabarit G0, G1 ou G2, configuration, programme, module importé |`
  - nouveau : `| empreinte différente : texte, monde, gabarit G0, G1 ou G2, configuration, programme, module importé ; texte servi de G1 ou de G2 de plus de 53 000 octets (le pire cas de Pr-2 et celui de Pr-4 atteignent leur plafond de session à 53 976 octets) |`
- **B3** (mineure)
  - ancien : `| un octet changé dans G2 : refus nommé |`
  - nouveau : `| un octet changé dans G2 : refus nommé ; un texte de G2 de 53 001 octets : refus nommé |`
- **C1** (mineure)
  - ancien : `borne par monde 7 200 s (deux tours : S, H et passe 1, puis D et B)`
  - nouveau : `borne par monde 7 200 s (deux étapes en série : passe 1, puis D et B ; S et H courent en même temps, sans que D et B les attendent)`
- **C2** (mineure)
  - ancien : `l'ablation (B) est ici aux critères gelés (étage 5)`
  - nouveau : `la comparaison d'écrivains (B), nommée « ablation de la frontière » par R-2977, est ici aux critères gelés (étage 5) ; elle ne retire pas la frontière (B est écrit par Pr-2, autre espèce de frontière)`
- **C3** (mineure)
  - ancien : `brouillon 4 : 123 + 483 + 243 + 196,60 + 263).`
  - nouveau : `brouillon 4 : 123 + 483 + 243 + 196,60 + 263 ; avec les 7 USD de la sonde des gabarits, 1 315,60).`
- **C4** (mineure)
  - ancien : `Résumé de sa sortie : 4 à 6 composantes`
  - nouveau : `Résumé de sa sortie (programme et sortie à verser au dépôt, avec leurs empreintes compagnons, avant le scellement ; il en va de même du programme 1 et de sa sortie) : 4 à 6 composantes`
- **D1** (mineure)
  - ancien : `refuse la concurrence (erreurs de limite de débit à l'essai à blanc), arrêt avant tout appel et nœud de la mère (procédure neuve)`
  - nouveau : `refuse la concurrence (erreurs de limite de débit scriptées à l'essai à blanc, qui éprouve le lanceur et non la limite réelle du fournisseur), arrêt avant tout appel et nœud de la mère (procédure neuve) ; la concurrence réelle chez le fournisseur n'est éprouvée qu'au premier tour des files, sous la ligne « limite de débit » (risque dit au point 13 de « Choix et doutes »)`

Motifs : **A1 à A3** (majeure) : avec cinq files, cinq mondes sont toujours en cours ; la somme « complets + non commencés » vaut 15 à l'instant 0 (0 + 15), donc sous 16 : la ligne s'arrête avant tout appel alors que son propre essai sain dit « continue » (R5 en défaut) ; même en milieu de course, la somme reste 15 tant que tous les mondes finis sont complets. A3 : l'étage 0 dit « non jugeable (arrêt) » pour toute ligne d'arrêt, alors que cette ligne dit « non concluant » (étage 1). **B1** : la pièce refait III-7 d'après le pilote sans écrire comment (R1) ; la règle donne la formule. **B2, B3** : le pire cas de session (1,99 et 2,98) est calculé pour 52 000 octets ; G2 ajoute près de 1 000 octets ; le plafond de Pr-2 (2,00) n'est tenu que jusqu'à 53 976 octets : sans garde de taille sur G1 et G2, un texte un peu long ferait un coût au-dessus du pire cas. **C1** : « deux tours » se lit comme une barrière ; l'ordre des appels (D part à la réponse de la passe 1) dit l'inverse. **C2** : l'étage 5 n'est pas une ablation de la frontière ici. **C3** : la sonde de 7 USD s'ajoute à l'enveloppe. **C4** : R6 : programmes et sorties de l'annexe non versés. **D1** : relais scriptés et limite de débit réelle.

## 5. Remarques facultatives (non exigées)

- **P2 et son étiquette** : « sans perte notable » n'est atteignable qu'avec δ_DB observé sous environ − 0,05 (de − 0,10 à 0), soit B au moins aussi bon que D dans l'échantillon ; la pièce le dit dans « Taille » ; l'étiquette peut se lire comme une équivalence : un libellé du type « B écrit au moins aussi bien » serait plus honnête. Laissé tel quel (R1 : libellé gelé).
- La fourchette de la machine (0,50 à 0,80) est calculée sur la durée en série (10 à 15 h) ; à cinq files la machine tourne moins longtemps. Sans effet sur le pire cas.
- La puissance de P1 manque ; elle viendra de la simulation avant scellement.

## 6. Points pour la mère

1. **Ligne d'arrêt du minimum (A1 à A3)** : défaut majeur, à corriger avant tout ; refait la lecture de l'étage 0.
2. **Gel de III-6** : aucune ligne de `registres/decisions.md` (jusqu'à R-2992) ne le confirme ; il doit être inscrit, daté à l'heure, **avant** que le lecteur neuf du pilote rende sa lecture.
3. **Étage 5 de (iii) contre (v)** : R-2992 point 2 a mis l'ablation de (v) hors critères gelés (conforme à N-045 point 3) ; pour (iii), R-2977 la garde aux critères gelés. Avec la variante, B n'est plus une ablation de la frontière : à confirmer que le gel de B reste voulu, ou à passer en « rapporté sans verdict » comme (v).
4. **Fragilité du minimum à N = 20** : sans reprise d'appel, un taux de réussite par appel de 0,95 donne 49 % de « non concluant » (78 % à p = 0,93) ; un seul échec de limite de débit parmi les dix à quinze premiers appels arrête tout le crible. L'essai à blanc, à relais scriptés, n'éprouve pas la limite réelle du fournisseur (D1) : la concurrence de vingt sessions n'est éprouvée qu'au réel. Option à trancher : démarrage échelonné des files, ou accepter le risque (recommandation : l'accepter avec le texte corrigé, puisque N = 20 est décidé).
5. **Enveloppe** : 1 308,60 USD (1 315,60 avec la sonde) contre 1 275 : nœud de Lazar si le dernier crible n'y tient pas ; solde de crédits de Claude à vérifier (260 + 7 au pire).
6. **Code neuf** (lanceur à cinq files, filtre, G1, G2, mesure, procédure de machine) : environ deux jours d'agents, lancement visé du 21 au 24 novembre, au-delà de l'autonomie (17 novembre 11:47Z, prolongeable au 18) ; mot de Lazar et phrase de Lazar requis ; GO-2026-11-15-06 expire le 30 novembre.
7. **Scellement** : la version qui fera foi recevra trois valeurs processeur, la table de mise à jour d'après le pilote et le taux de réussite recopié : un dernier tour sur le différentiel reste obligatoire.
8. Rien du pilote MR-2 v14 n'a été lu ; la règle « 24 mondes si le taux est sous 0,95 » de la consigne de ce tour est remplacée par R-2992 (N = 20) et n'a pas à figurer.

## Incidents (de ma main)

- Aucun appel de modèle, aucune dépense, aucune machine, aucun `pytest`, aucun clone ; un `git fetch` à refspec (branche `lot/compte-organisme-v1`) ; lectures par `git show` du texte du pilote (branche `prep/pilote-mr2-compte-organisme-v1`) et de la procédure v14 au commit `2d35cafa…` ; rien lu sous `diag/`, `runs/`, `donnees/`, ni de la branche de sortie du pilote.
- Calculs légers faits : les deux programmes de l'annexe A rejoués (bibliothèque standard, quelques millisecondes, `nice`) ; lecture seule des douze sorties scellées `sorties-v4` par le programme 2 ; quelques recomptes de probabilités ; copies de travail sous le bloc-notes de session (pas dans le dépôt). Aucun fichier existant modifié.
