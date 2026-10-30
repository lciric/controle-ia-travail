# Contre-lecture 2 (R2) — Préenregistrement du pré-pilote d'étalonnage de la course 2, brouillon 2

- Contre-lecteur : sous-agent neuf (règle R2), n'ayant écrit aucune des pièces et n'ayant pas fait la contre-lecture 1 ; n'a lu ni témoin, ni consigne de juge, ni rien sous `donnees/` ou `quarantaine/`, ni le texte II « avec pistes », ni le texte III, ni rien du bras d'attaque. Aucune dépense, aucun réseau, aucune opération git.
- Modèle : Fable 5.1 (`claude-fable-5-1`) ; l'auteur du brouillon 2 est un Opus 5.5 neuf (R-599), la session qui l'a commandé un Opus 5.5 (conv-audit).
- Date (UTC) : 2026-10-30, 16:21 (`date -u` : Fri Oct 30 16:21:21 UTC 2026).
- Pièce relue : `preenregistrement-pre-pilote-course-2-brouillon2.md`, empreinte `8afb556f5f96e69bdb7ff57cf19ff053c581f71d08274e0e6fc44fd0fd7eb8f9` (les sept compagnons `.sha256` du dossier vérifiés par `sha256sum -c` : tous conformes).
- Script relu : `calcul-puissance-pre-pilote-course-2-v2.py` `92c0e60d…` ; sortie `calcul-puissance-pre-pilote-course-2-v2.sortie.txt` `1c0e702d…`. **Réexécuté** (`python3 -I`, python 3.13.18, numpy 2.5.3, scipy 1.18.1, 50 s) : sortie **identique octet pour octet** (`diff` vide). Tous les chiffres du brouillon que j'ai confrontés à la sortie y figurent (0,88 / 0,71 / 0,52 / 0,20 / 0,05 ; 0,77 / 0,47 / 0,23 / 0,37 / 0,39 / 0,17 ; 0,96 / 0,63 / 0,20 → 0,23 ; 25,7 / 8,1 / 8,8 ; 0,47 / 0,75 ; 0,03 / 0,42 ; 0,37 / 0,53 / 0,72 ; 0,088 / 0,74 ; 0,14 / 0,88 ; 0,09 / 0,12 ; 1,41 / 2,83 / 11,3 / 17,0).
- Contexte lu : contre-lecture 1 (`96cf300b…`, conforme) ; brouillon 1 (`8d6142eb…`, conforme) ; décisions R-552 à R-604 (`registres/decisions.md` de l'arbre de travail) ; texte I fusion v5 (`a7501449…`, conforme ; l. 44, 46, 63, 87, annexe 3 l. 150-152) ; gabarit (`8cad4371…`) et validateur (`3b2e3ee5…`) conformes. Non relus : R-811, R-818 à R-827 et les devis sur `origin/main` (repris par la contre-lecture 1), le préenregistrement scellé de bisociation v2 (seule la forme du score est citée).
- Validateur `controle_ia.prereg.problemes` sur le brouillon 2 : un seul problème, « section vide ou à remplir : Seuil » (les 26 marqueurs À REMPLIR, attendus avant le gel) ; aucun marqueur de gabarit `<<…>>`. Un `__pycache__` existait déjà sous `src/controle_ia/` avant cette session (horodaté 16:15:48 UTC, avant mon départ 16:16:09) ; je n'en ai créé aucun (`-I`, `-B`) et n'y ai pas touché.

Gravité : **majeur** = bloque le gel ; **moyen** = à corriger avant le gel, sans changer la structure ; **mineur** = précision ou reformulation.

## Verdict (une ligne)

**Corrections majeures, courtes** : les 27 constats de la contre-lecture 1 sont traités (25 en entier, 2 en partie) et la structure est saine ; mais la probabilité que la **porte entière** s'ouvre aux valeurs prédites n'est pas calculée (≈ 0,15 à 0,20 selon mon estimation, non 0,37), l'issue attendue (nœud, pas de départ) et ce qu'on fait alors ne sont pas écrits, et deux chemins de décision sortent de la table « Porte » (réfutation d'ensemble (ii) ; mesures non mesurées pour cause de budget).

## (a) Traitement des constats CP1-01 à CP1-27

| Constat | État | Endroit et remarque |
|---|---|---|
| CP1-01 (majeur) | **traité** | « Métrique » (classes, témoin non ambigu), table des classes dans « Rôles ». Vérifié littéral contre le texte I : N1 ↔ K1 et axe 4 (a) « issues écrites » (l. 63) ; N2 ↔ K2 seconde branche (l. 46) ; N3 ↔ K3 et M « aire (rapportée, jamais seule) » (l. 87) ; N4 ↔ K4 (l. 46). Réserve restante (CP2-05) : la condition (a) contre la consigne figée (DEP2) reste à faire au gel, et N4 a une nuance. |
| CP1-02 | traité | S19, indices imposés par fond, A7. |
| CP1-03 | traité | couples de défaut, interdiction de liaison, question « défaut encore là ? » (Rôles, S6, A5). |
| CP1-04 | traité | M1 (spécificité = rappel sur N ; G sur l'étage 1 ; 0 % des P, N, C signalées). |
| CP1-05 (majeur) | traité | M2 descriptive, k et points de X écrits, alarme S5 hors porte, script v2 (modèle par item). |
| CP1-06 | traité | tiers T, Δsév sans Opus, B_cc, D-f ; algèbre vérifiée (B_croisé = Δstyle − Δsév ; B_cc = Δstyle sous le modèle du script). |
| CP1-07 | traité | P4 (+6 points, raison écrite). |
| CP1-08 (majeur) | **partiel** | table « Porte » à 13 conditions, ligne M4 « à corriger », estimation ponctuelle, S18 non évaluée, règle du complément : faits. Restent deux chemins hors table (CP2-02) et un mot non défini (CP2-07). |
| CP1-09 | traité | probabilité jointe de la porte des juges et du complément (Seuil, résumé l. 3, script) ; mais seulement pour M1 (CP2-01). |
| CP1-10 | traité | bornes et erreurs tolérées aux effectifs réels ; lecture par niveau de M3 descriptive. |
| CP1-11 | traité | seuils paramétrés, versions et racine imprimées, flottants ; un effectif faux introduit dans la v2 (CP2-13). |
| CP1-12 (majeur) | traité | É4 aiguilleur avant É7 juges, sur tout ce qui atteint un juge ; A17 ; ordre de sacrifice. |
| CP1-13 | traité | trois instances distinctes, consigne de l'aiguilleur empreintée en É0, A9 étendu, second lecteur aveugle, comptes auto-rapportés déclarés. Voir CP2-04 sur le compte retenu. |
| CP1-14 | traité | réserves écrites (en-tête, Rôles). |
| CP1-15 | traité | « non étalonné » = nœud (C7), « à corriger » (table M4), classes non écrites. |
| CP1-16 | traité | lignes M5 et « Ce que le pré-pilote ne dit pas ». |
| CP1-17 | traité | deux passes sans condition, 20 fiches, 0,14 / 0,88, non identiquement distribuées. |
| CP1-18 | **partiel** | plafond 6,0, bases, reprises comprises, tâches de réduction : faits ; la somme des plafonds est fausse (CP2-14). |
| CP1-19 | traité | table R5 à 16 lignes ; lacunes nouvelles en CP2-09. |
| CP1-20 | traité | A14 « non mesuré (technique) ». |
| CP1-21 | traité | paraphrases des rendus en É8, paires traversantes écartées, « table seule » = Opus. |
| CP1-22 | traité | trois indices, Wilcoxon, garde grossière, limite sur Argon. |
| CP1-23 | traité | A7 : deux versions, le rédacteur ne voit que les cibles. |
| CP1-24 | traité | audit R4, « un juge ≥ 0,97 ». |
| CP1-25 | traité | tâches de réduction, versions dans la sortie. |
| CP1-26 | traité | SUPPOSÉ sur l'erreur-type du kappa ; conversion retirée (vérifié : « 1,8 sur 15 » ne reste que dans la citation de R-827). |
| CP1-27 | traité | A2 reformulée. |

Aucun constat refusé par l'auteur ; l'écart déclaré sur CP1-01 (classe V retirée plutôt que gardée en descriptif) est justifié (sans item de l'étage 2, elle ne mesurerait rien).

## (b) et (c) Constats sur le brouillon 2

### Puissance et issue attendue (c)

**CP2-01 (majeur) — La probabilité de la porte entière n'est pas calculée, et le résumé laisse lire 0,37 comme si c'était elle.** Le script et la section « Seuil » calculent la « porte M1 » (Kimi et Argon étalonnés, Opus non défaillant) : 0,37 aux valeurs prédites. Le résumé l. 3 place ce chiffre sous « Porte (CP1-08) : une conjonction unique de 13 conditions », et R-604 le porte à Lazar sous la même forme. Or la porte a douze autres conditions, dont plusieurs ont, aux valeurs prédites, une probabilité nettement inférieure à 1 : C7 (M4 « étalonné » direct à rappel vrai 0,92 : 11 sur 12 ET aucun oubli en C1-C2 ≈ 0,56, relevé par le chemin « à corriger ») ; C5 (S19 à aire prédite 0,55, erreur-type 0,12 : respectée ≈ 0,80 par version ; S18 à 0,62 : ≈ 0,81) ; C8 (taux 0,05 sur 20 fiches, observé ≤ 0,10 : ≈ 0,92) ; C10 (voir CP2-11). Produit grossier, juges indépendants des autres instruments : **≈ 0,15 à 0,20**. À titre de comparaison, M6 « étalonnée » aux valeurs prédites (9 sur 9 inventées à 0,95 ; ≥ 7 sur 9 altérées à 0,70 ; ≤ 2 sur 22 à 0,08) ne vaut que ≈ 0,22, mais C9 accepte « non concluant », ce qui est cohérent et à dire. **Correction** : (i) faire calculer par le script la probabilité de la conjonction entière aux valeurs prédites et aux cas « tous à 0,90 / 0,85 », avec les hypothèses de chaque condition écrites ; (ii) écrire dans le résumé « porte des juges (C1-C2) » et non « porte » ; (iii) corriger R-604 par une ligne nouvelle.

**CP2-02 (majeur) — L'issue attendue n'est pas écrite, ni ce qu'on fait alors.** Le texte dit clairement, en chiffres, que la porte des juges s'ouvre avec 0,37 (résumé l. 3, « Seuil »). Mais nulle part il n'est écrit que **l'issue la plus probable du pré-pilote, aux valeurs que l'auteur prédit lui-même, est un nœud sans départ** (probabilité ≈ 0,6 pour les juges seuls, ≈ 0,8 pour la porte entière). La seule suite écrite est le complément (0,39, qui porte à ≈ 0,63 un juge à 0,80) et « sinon : nœud de Lazar, auquel sont transmis la table remplie, les conditions non satisfaites et les réserves ». Rien ne dit quelles **options** le nœud offrira, alors que toute option qui touche un seuil après lecture (abaisser S1, relire sur la note graduée) serait un seuil choisi après résultat. Note aussi que P1 met Kimi exactement à S1 = 0,80 : pour Kimi, le pré-pilote est, par construction, une pièce jouée à pile ou face (0,52), et le brouillon ne le dit pas en ces termes. **Correction** : un paragraphe « Issue attendue » dans « Critères de lecture gelés » : (1) probabilités de « porte ouverte », « complément », « nœud » aux valeurs prédites ; (2) liste **fermée, écrite maintenant**, des options qui seront proposées au nœud selon la condition en défaut (par exemple : C1 non concluant → complément ; C1 défaillant pour Kimi → course avec Argon et Opus seuls juges, ou Kimi juge « en lecture seule, non comptée », ou second pré-pilote sur témoins neufs ; C7 → consigne v+1 et nouvel essai sur GO ; C10 → devis refait), avec la règle « aucun seuil de ce préenregistrement n'est modifié après lecture ; une option qui en change un passe par un préenregistrement nouveau (R12) » ; (3) une phrase dans le résumé l. 1 : « issue la plus probable : nœud ».

### Porte, cas non réglés, critères à interprétation (b)

**CP2-03 (moyen) — Deux chemins de décision sortent de la conjonction « si et seulement si ».** (i) « Réfutation d'ensemble (ii) : tous les juges rejettent les C comme les N → audit R4 et nœud » n'est dans aucune ligne C1 à C13 : la porte peut être « ouverte » par la table et fermée par ce paragraphe ; de plus « rejettent les C comme les N » n'a pas de seuil (la ligne R4 dit « égal », exact ?). (ii) L'ordre de sacrifice dit « si une étape protégée ne tient pas : non lancée, non mesuré, porte fermée », et M6 peut n'être « non mesurée » que par budget ; or C13 ne compte que « non mesurée (technique) » et C9 n'a pas de ligne pour M6 non mesurée. Même question pour l'audit R4 : « un résultat qui déclenche l'audit n'est pas lu avant que l'audit soit rendu », mais rien ne dit ce que la porte fait d'un audit qui conclut à un artefact. **Correction** : une condition C14 « aucun déclencheur d'audit R4 ouvert, ou audit rendu sans artefact » ; seuil pour (ii) : « rejet des C ≥ spécificité moyenne sur N − 0,10 chez les trois juges » ; état « non mesuré (budget) » ajouté à C13 avec la même conséquence que « technique » (nœud).

**CP2-04 (moyen) — M5 : le compte retenu (signalée par les deux lecteurs) est le plus indulgent pour un instrument de sécurité.** Une fiche signalée par l'aiguilleur seul ou par le second lecteur seul n'entre pas dans le taux ; à 20 fiches, un vrai débordement vu par un seul des deux abaisse le taux vers « conforme ». La contre-lecture 1 demandait l'accord pour l'indépendance, pas pour la lecture du seuil. **Correction** : taux primaire = union (signalée par l'un ou l'autre), accord et désaccords rapportés ; ou, à défaut, « conforme » exige l'union ≤ S12 et « dépassement » se lit sur l'intersection, le cas intermédiaire étant « non concluant (réserve) ».

**CP2-05 (moyen) — Témoin non ambigu : la sélection par un relecteur de la famille Claude, et la nuance de N4.** Le relecteur (D-f : Fable 5.1) applique la consigne figée et filtre les témoins primaires ; Opus 5.5, de la même famille, est jugé sur les témoins où un Claude a lu comme le rédacteur : la réserve écrite (« retire les témoins les plus difficiles ») ne nomme pas ce biais de famille, qui favorise Opus en M1 et en accord. Sur N4 : K4 admet un « étage sur carte : devis et GO par fiche » ; une fiche dont la première expérience est une location de carte chiffrée viole bien « première expérience sur processeur seul », mais « sans devis ni GO » n'est pas un champ de la fiche : un juge peut lire K4 comme satisfait si la fiche annonce un devis. **Correction** : nommer la réserve de famille (ou prendre un relecteur d'un autre fournisseur, par exemple Argon, qui n'est pas juge des mêmes témoins… mais il l'est ; sinon, garder Fable et l'écrire) ; pour N4, planter le défaut sur la contradiction interne « coût : carte en dollars » contre « première expérience : sur processeur seul » déclarée dans un autre champ, ce qui est une incohérence entre deux champs au sens strict.

**CP2-06 (moyen) — S5 est écrit « 20 points » alors qu'il dépend de k (DEP2, inconnu).** La raison de S5 est « le pas de X à k = 5 » ; si la consigne figée a k = 8, 20 points valent 1,6 item. **Correction** : S5 = 100 / k points (un item par fiche), k lu au gel ; même remarque pour les chiffres de résolution de M2 (script à rejouer avec K lu).

**CP2-07 (mineur) — Mots à interprétation dans la porte.** C13 « aucun arrêt de la liste ouvert » : A5, A7, A8 sont des reprises, A6 et A7 des arrêts « avant les juges » suivis d'une réécriture ; rien ne dit quand un arrêt est « clos ». A6 (« classe fausse sur plus de 15 % des rendus », soit 5 sur 28) et S20 (« 4 ambigus tolérés sur 23 ») se recouvrent sans être identiques. C5 « non évaluée faute de 6 fiches de Kimi non aiguillées » : le 6 n'est pas un seuil numéroté. **Correction** : définir « arrêt clos » (reprise faite dans le plafond, version suivante empreintée) ; fondre A6 dans S20 ; numéroter le 6 (ou le rattacher à S20).

**CP2-08 (moyen) — M4 « à corriger » : lecture du nouvel essai à préciser.** « Nouvel essai sur 3 témoins neufs par classe en défaut ; aucun oubli → étalonné » : le rappel global est-il recalculé sur 12 + 3 ou le nouvel essai seul décide-t-il ? Quand le cas est « aucun oubli en C1-C2 et 0,75 ≤ rappel < S10 », la classe en défaut (C3 ou C4) est implicite. Un seul nouvel essai sur 3 témoins à rappel vrai 0,92 passe avec 0,78 : à écrire. **Correction** : « le verdict se lit sur les 3 témoins neufs seuls ; aucun oubli → étalonné avec réserve “consigne v+1 non éprouvée sur les autres classes” ».

### Table R5, tableau minimal, bisociation (b)

**CP2-09 (moyen) — Table R5 : trois gardes sans ligne, un artefact non défini.** Manquent : le **moissonneur** (cas sain : référence réelle trouvée ; artefact : référence inventée « non trouvée » ; c'est lui qui fonde « 9 inventées ») ; les **lecteurs d'étiquettes** (artefact : étiquette hors de la liste fermée, à rejeter ; cas sain : étiquette de la liste) ; le **relecteur** (cas sain : rendu fidèle d'une N, défaut vu ; artefact : rendu où le programme a retiré une chaîne du couple, « défaut absent » attendu). Ligne 7 : « sous t* provisoire » — t* n'existe pas avant le calibrage ; fixer une valeur provisoire d'essai (par exemple 0,90) écrite au gel. Ligne 13 : la garde des cloisons vérifie des **étiquettes** de case ; une entrée réelle mal étiquetée à la source passerait ; à déclarer (« la garde vérifie l'étiquette, pas la provenance ; la provenance tient au constructeur, empreinté »). Ligne 10 : artefact « décrit par classe seulement », inévitable (R-575), mais à marquer « auto-rapporté » comme M4.

**CP2-10 (moyen) — Bisociation : D-e dégénère dans une case unique, Jaccard non défini, S22 hors périmètre, S24 et nœud.** (i) Dans la case (texte I, bras de défense), toutes les fiches partagent la case : avec domaine = [axe, case], cos ∈ {0,5 ; 1} et (1 − cos²)^8,5 ∈ {0,087 ; 0} ; avec axe seul, cos ∈ {0 ; 1}. La règle N se réduit donc à « deux axes différents, Jaccard des étiquettes le plus haut » : exact, mais à écrire, sinon « domaine » semble mesuré. (ii) κ_concept et l'accord S24 sont des Jaccard : non définis si un lecteur ne pose aucune étiquette (règle : 0, ou fiche exclue). (iii) **S22 (k = 2 dans la course)** est un paramètre de la course 2, pas du pré-pilote : le geler ici fait porter à ce préenregistrement une décision d'un autre préenregistrement (v53) ; le garder en recommandation à Lazar, hors des marqueurs de gel. (iv) La ligne M9 « accord < S24 → chaîne conforme, D-e à reprendre (nœud) » et C12 « l'accord n'entre pas dans la porte » coexistent : dire explicitement que ce nœud porte sur D-e et n'empêche pas de demander le GO de la course (ou le contraire). (v) Les deux fusions sont écrites par Kimi à partir de fiches de Kimi et notées par Kimi : auto-préférence maximale, comptées à part : à dire dans « Ce que le pré-pilote ne dit pas ».

**CP2-11 (moyen) — C10 peut fermer la porte presque à coup sûr.** « devis de la course ≤ 110 USD − dépense réelle du pré-pilote » : à 26,6 USD de pré-pilote, la course doit tenir en 83,4 ; le devis v3 donnait ≈ 70 attendus avant le tableau et la bisociation (≈ 11 à k = 2) : la marge est de quelques dollars, et un seul poste à ×1,3 ferme C10. Ce n'est pas une erreur, mais c'est une cause de nœud à écrire dans « Issue attendue » (CP2-02), et le chiffre 110 doit renvoyer à GO-2026-10-30-07 (chemin et empreinte, R6).

**CP2-12 (mineur) — S18 / S19 : la réécriture répond parfois au bruit.** À aire vraie 0,5, S19 est dépassée avec ≈ 0,11 par version (erreur-type 0,12) ; réécrire les témoins corrige alors un hasard, pas un défaut ; deux versions bornent le coût, mais dire que « dépassée après deux versions » à ces effectifs peut être un faux positif de garde (≈ 0,01) et qu'il est accepté.

### Script, chiffres, forme

**CP2-13 (mineur, script) — Effectif faux dans la v2.** Lignes « fausses alertes vraies … sur 34 fiches » : `stats.binom.cdf(int(36 * S11), 36, fa)` utilise 36 au lieu de 34 (0,51 affiché contre 0,55 réel à 0,10 ; 0,05 contre 0,07 à 0,20). Sans effet sur un seuil ; corriger et rejouer au gel (la sortie fait foi).

**CP2-14 (mineur) — Somme des plafonds.** 3,2 + 2,8 + 1,9 + 6,0 + 2,0 + 7,0 + 12,4 + 1,0 + 6,0 = **42,3**, non 41,3 (sans effet : borné à 32). L'attendu 26,6 est juste (recalculé poste par poste). Chiffres de la sortie v2 repris dans le texte : tous conformes.

**CP2-15 (mineur) — Graines (R9) : conforme.** Racine 20261101, dérivation `cle_de_tache` identique à celle du script (même construction que `manifeste.py`, vérifiée par la contre-lecture 1), tâches nommées, réduction comprise. Le script de puissance utilise la racine 20261031, déclarée.

**CP2-16 (mineur, R3 / R4) — Conforme.** Aucune prédiction visée comme positive ; audit « trop propre » symétrisé ; l'alarme S5 déclenche l'audit dans les deux sens.

## Récapitulatif par gravité

- Majeurs (2) : CP2-01 (probabilité de la porte entière absente, 0,37 présenté comme la porte), CP2-02 (issue attendue « nœud » et options pré-écrites absentes).
- Moyens (8) : CP2-03 (deux chemins hors table, seuil de (ii), « non mesuré (budget) »), CP2-04 (M5 : compte par intersection trop indulgent), CP2-05 (biais de famille du relecteur ; N4), CP2-06 (S5 = 100/k), CP2-08 (nouvel essai de M4), CP2-09 (table R5 : trois gardes manquantes, t* provisoire), CP2-10 (bisociation : D-e dégénéré, Jaccard non défini, S22 hors périmètre, nœud de S24), CP2-11 (C10 et le 110).
- Mineurs (6) : CP2-07, CP2-12, CP2-13, CP2-14, CP2-15, CP2-16.

## Ce que je n'ai pas pu vérifier

- La consigne figée des juges (DEP2 : items, k) n'existe pas : la condition (a) des témoins non ambigus, S5 et la résolution de M2 restent à vérifier au gel par le contre-lecteur du préenregistrement de gel.
- Les coûts par unité (0,114 ; 0,079 ; 0,057 ; 0,25 ; 0,40) sont repris du devis v3 et de R-578 sans recalcul sur `registres/depenses.md`.
- Aucun témoin, squelette, fiche de Kimi ni rien du bras d'attaque : conforme au mandat.

## (d) Verdict

**Corrections majeures (courtes)** : soumettable au gel après un brouillon 3 qui (1) calcule et écrit la probabilité de la porte entière et l'issue attendue avec la liste fermée des options du nœud (CP2-01, CP2-02) ; (2) ferme les deux chemins hors table et l'état « non mesuré (budget) » (CP2-03) ; (3) lit M5 sur l'union (CP2-04) ; (4) écrit S5 en 100/k (CP2-06) ; (5) corrige les points moyens restants (CP2-05, 08, 09, 10, 11) et les trois chiffres (CP2-13, 14) ; puis une contre-lecture courte de ces seuls changements par un sous-agent neuf.
