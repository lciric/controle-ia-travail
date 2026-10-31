# Vérification courte du brouillon 5 — épreuve semi-réelle des méthodes d'identification — v1

- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`). N'a écrit ni les brouillons 1 à 5, ni le script de règles, ni la contre-lecture CS4 (brouillon 4), ni CS2. **Réserve d'indépendance** : même modèle que les auteurs de CS2 et de CS4 (modèle différent d'Opus : exigence de R2 satisfaite), même dépôt, même chaîne de travail ; aucune lecture de leur raisonnement hors de leurs rapports.
- Date (UTC) : 2026-10-31, 11:51 à la fin de la lecture.
- Règles appliquées : R2, R3, R4, R5, R6 (empreintes), R1 (aucune lecture de données).
- Interdits respectés : rien lu sous `donnees/` ; aucun `git fetch` ; aucune moisson ; aucun commit ; aucun `.sha256` écrit ; aucun fichier existant modifié ; seul fichier créé dans le dépôt : ce rapport. **Écarts à signaler** : en plus du script de règles et du validateur (`python3 -I`, dossiers temporaires vides, `-B` pour le validateur), j'ai exécuté quelques calculs courts hors dépôt (`/tmp/vs5v`) : lois binomiales exactes, bornes de Wilson, un jouet de 20 lignes sur les moyennes résiduelles par environnement (VS5-01). Ils ne sont pas versionnés ; leur résultat est donné dans le constat.
- Empreintes (recalculées, chacune conforme à son compagnon `.sha256`) : brouillon 5 `435b16ef1ace0816951a28b039c0264c1eb6d1564a6ee2681c6f94b202259155` (956 lignes, lu en entier) ; script `…brouillon5.py` `de647c4998cc2c0b2a5b0dfe84f95dac94011bbda2665553877709c0ab8e1c76` (lu pour les paragraphes 26 à 31) ; sortie `…brouillon5.sortie.txt` `2ab37d3997eb3f878e72498e9844cac5991b09e646cb7b660fa2103c68dbccb3` ; contre-lecture CS4 `4a73e32a7b97b94f374a89367887a287264ee774b67ef28da6de4e492b3cfe00` (lue en entier) ; brouillon 4 `30f45ac5…` (empreinte seulement) ; `src/controle_ia/prereg.py` (lu).
- Non lus : `donnees/`, la moisson, les PDF, la synthèse v2, les cellules du collisionneur.

Échelle : **bloquant** = interdit le gel ; **majeur** = à corriger avant le gel (conception ou texte change) ; **moyen** = à corriger ou à écrire comme choix assumé ; **mineur** = à corriger en repassant sur le texte.

---

## Verdict

**Présentable après corrections.** Les 19 constats de CS4 sont tous traités, à la ligne indiquée ; la lignée de calcul est exacte (deux rejeux, octet pour octet) ; tous les chiffres du texte que j'ai recoupés concordent avec la sortie ; le validateur ne bloque que sur « Seuil » et « Contre-lecture ». Mais la correction du majeur CS4-01 (centrage intra-strate) a un effet de bord non examiné sur la prédiction invariante (M1), qui rend fausse la raison donnée à Lazar pour préférer l'option 1 de DL-12 ; et la puissance de l'étape d'estimation, bien recalculée, n'est garantie que pour une représentation supposée à 0,85 de corrélation alors que la Table Bθ qualifie dès 0,70.

**Compte : 0 bloquant, 1 majeur, 5 moyens, 8 mineurs (14 constats).**

**Le plus important** : VS5-01 (centrage et M1 : la raison d'être de κ disparaît, DL-12 est présentée avec une prémisse inexacte), puis VS5-03 (PUISθ ne garantit pas la puissance revendiquée) et VS5-02 (la moitié « trop propre » du déclencheur S14 (o) ne peut pas sonner).

---

## A. Réponse aux sept points

| # | Point | Résultat |
|---|---|---|
| 1 | Chaque constat CS4 traité, ligne citée | **Oui, 19 sur 19** ; tableau en B0. Défauts de détail : VS5-01 (effet de bord), VS5-04 (« couvert »), VS5-08 (Q8 périmé), VS5-09, VS5-10. |
| 2 | Rejeu et chiffres | **Conforme.** Deux rejeux `python3 -I` depuis `/tmp/vs5a` et `/tmp/vs5b` (vides) : sorties identiques entre elles et au fichier `…sortie.txt` (`2ab37d39…`), sortie d'erreur vide, 4 min 45 s par rejeu. Paragraphes 1 à 25 identiques au bit près à la sortie du brouillon 4 (`diff` vide). Chiffres demandés tous retrouvés : erreur C 0,113 → 0,013 pour 0,010 nominal (M § 26, strate à 10 %) ; rétrodiction redéfinie 0,000 à 0,013 sans fuite (R-b5 et M2-b5, trois conditions), 0,997 à 1,000 avec ; permutation exacte 0,010 au seuil 0,01 (M § 30) ; puissance 0,78 (3 env., 16 ans) à 0,90 (20 ans) et 0,88 (5 env., 12 ans) sous PUISθ, 0,45 à 0,73 dessous (M § 29). Rejeu de CS4 (M § 28) : lignes A à D identiques au caractère près à l'annexe A de CS4, ligne E (15 niches) « aucun monde utilisable » comme dans mon propre essai. |
| 3 | S11, S12, S13, PUISθ | **Cohérents en arithmétique, fragiles en hypothèse** : voir B, VS5-02 et VS5-03. Vérifié : Wilson 37/50 → borne basse 0,6045 (36/50 : 0,583) ; 2/50 → borne haute 0,1346 (3/50 : 0,162) ; règle tenue 0,889 (0,80), 0,328 (0,70), 0,922 et 0,986 (fausse détection 0,02 et 0,01), 0,112 (0,10) ; 0,825 et 0,52 à 0,535 pour 0,78 et 0,73 (parts non arrondies de M § 29 ; mes valeurs à parts arrondies : 0,806 et 0,51). Plancher S13 : 3 env. × 1 000 paires × (P − 8) ≥ 20 000 donne P ≥ 15, 4 env. P ≥ 13, 5 env. P ≥ 12 (M § 31 exact). PUISθ coupe entre 0,73 (P = 15, n(E₂) = 2 277) et 0,78 (P = 16, 2 656) : cohérent avec la grille. Ce que le texte cesse de revendiquer si PUISθ est faux : écrit en S11, S13, S21, Table Estimation-θ ligne 0, « n'autorise pas » (l. 370), Prédiction (l. 405, 424) : **cohérent** (réserve VS5-12). |
| 4 | Réserve de l'auteur (T1) et asymétrie R2 / R2⁻ | **T1 : acceptable comme limite déclarée, pas comme formulée** (VS5-04). **Asymétrie : acceptable pour les règles de la Table A, non pour le déclencheur S14 (i) ni pour la confiance de la prédiction de symétrie** (VS5-05). |
| 5 | DL-1 à DL-13, D1 à D3 | **Ouvertes** : 13 « État : À REMPLIR (décision de Lazar) » (l. 27, 34, 55, 62, 68, 77, 83, 89, 97, 103, 110, 117, 124) ; D1 à D3 « À REMPLIR au gel » (l. 153 à 155) ; aucun défaut appliqué. DL-12 (l. 122) et DL-13 (l. 129) portent « (option : demander au collisionneur) », comme DL-5 (l. 75) ; mais en parenthèse de la recommandation, non en option développée (VS5-13). |
| 6 | R3, R4, R5 | R3 : rien ne vise un signe positif ; l'élargissement de S12 (0,10 → 0,15) va dans le sens d'une qualification plus facile mais ses deux erreurs sont chiffrées (M § 32) : accepté. R4 : VS5-02 (moitié « trop propre » de (o) morte), VS5-03 (grille de r sans cas défavorable). R5 : les 13 gardes (b5) ont chacune un cas sain et un artefact (compte vérifié ligne par ligne, l. 891 à 937) ; réserve VS5-11 sur le seuil de la garde de centrage. |
| 7 | Validateur `problemes` | **Conforme** : exactement deux problèmes, « section vide ou à remplir : Seuil » et « … : Contre-lecture ». Sur copie temporaire (supprimée), ces deux sections débloquées, il ne reste que « marqueur À REMPLIR restant hors des sections exigées » (les 13 DL et D1 à D3, attendus). Aucun marqueur de gabarit `<<…>>`. Observation VS5-14. |

### B0. Traitement de CS4-01 à CS4-19 (ligne du brouillon 5)

| Constat | Traité ? | Où (brouillon 5) |
|---|---|---|
| 01 κ | Oui, par centrage (variante de l'option (i)) ; options (ii) et (i) en DL-12 | l. 196 ; Métrique l. 434 ; S4 l. 498–501 ; H-SR-A l. 295 ; Plan § 2 l. 642, § 10 l. 746 ; gardes l. 927–928 ; DL-12 l. 116–122. **Effet de bord : VS5-01.** |
| 02 rétrodiction | Oui ((i), (iii) acceptés ; (ii), (iv) remplacés, justifié) | l. 197 ; GF2 l. 284 ; Métrique l. 455 ; S14 (m) l. 550 ; S23 l. 593–596 ; garde l. 911 |
| 03 puissance | Oui (rejeu exact + extension + PUISθ + oracle) | l. 198 ; S11 l. 533–536 ; S13 l. 543–546 ; S21 l. 583–586 ; Table l. 813–827 ; DL-5, DL-8. **Réserves : VS5-02, VS5-03.** |
| 04 plancher S13 | Oui | l. 199 ; S13 ; « n'autorise pas » l. 369 ; garde l. 931 |
| 05 estimateur dyadique | Oui, autrement (permutation exacte) | l. 200 ; Métrique l. 474 ; S21 ; garde l. 910 ; nœud 5 (f) l. 164 |
| 06 hasard de S22 | Oui | l. 201 ; S22 l. 590 ; Métrique l. 465 ; garde l. 930 ; M § 33 |
| 07 caractéristiques | En partie, écrit | l. 202 ; GF6 l. 288 ; S12 l. 540–541 ; Plan § 9 l. 739 ; M § 32 |
| 08 garde-fous descriptifs | Oui | l. 203 ; Résumé 6 l. 16 ; l. 290 ; DL-13 l. 123–129 |
| 09 gardes manquantes | Oui | l. 204 ; l. 862–869 ; deux ensembles A / B l. 890 ; l. 932–937 |
| 10 symétrie, raison de S11 | Oui | l. 205 ; S14 (o) l. 550 ; Table l. 819–825 ; S11 raison l. 536. **Réserve : VS5-02.** |
| 11 fidélité à la synthèse | Oui, quatre glissements + limite des lignes 11 à 14 | l. 206 ; S16 l. 561 ; W4 l. 319 ; H-SR-A l. 295 ; Intégration § 2 l. 944 ; l. 368. Reste périmé : VS5-08. |
| 12 décisions câblées | Oui | l. 207 ; tableau l. 131–147 ; S7 l. 515 ; M § 35 |
| 13 années de plantation | Oui | l. 208 ; W5θ l. 322 ; Plan § 4 l. 658 ; S19 l. 575 ; Métrique l. 464. Reste : VS5-10. |
| 14 marqueur dans la prose | Oui, en partie (tableaux gardés jusqu'au gel) | l. 209 ; aucun « À REMPLIR » dans la prose (recoupé par `grep`) |
| 15 calendrier | Oui | l. 210 ; DL-2 l. 40–53 (dates recoupées : 2 novembre 2026 est un lundi ; 27 novembre est un vendredi ; marge 3 jours) |
| 16 T2b | Oui, confiance 0,25 | l. 211 ; l. 387 ; S17 l. 566 |
| 17 vocabulaire, définitions mortes | Oui | l. 212 ; l. 763 ; l. 768 |
| 18 plis | Oui | l. 213 ; l. 438, 663–664 |
| 19 R7 | Oui | l. 214 ; l. 306, 341, 757 |

---

## B. Constats

### Majeur

**VS5-01 — Majeur — Le centrage intra-strate de la sortie vide de sa substance le décalage de mécanisme κ pour la prédiction invariante (M1) ; la raison donnée pour l'option 1 de DL-12 est inexacte.**
- Lignes : DL-12 l. 119 (« la prédiction invariante garde la variation d'affectation entre environnements dont elle a besoin ») et l. 120 (option 2 : « la prédiction invariante perd la seule variation d'affectation ») ; S4 l. 501 (« les décalages κ sont le "décalage de mécanisme" dont la prédiction invariante a besoin ») ; Métrique l. 434 (« les environnements de M1 … sont inchangés : κ y garde la variation d'affectation ») ; S8 l. 520 (M1 teste l'égalité des **moyennes** et des variances des résidus entre environnements) ; PA-M1 l. 388 (recouvrement 0,2 à 0,8).
- Constat : les environnements de M1 (sous-domaine × bloc de cinq ans) sont des unions de strates (environnement × année). La sortie est centrée dans chaque strate : la moyenne de tout résidu d'une régression sans variable non centrée est donc **exactement nulle** dans chaque environnement de M1, pour tout ensemble candidat. C'est précisément le canal par lequel M1 reconnaît un parent omis : sans C, le résidu contient β·C dont la moyenne varie avec la prévalence κ ; le centrage de la sortie l'efface. À l'inverse, un ensemble qui contient C (binaire non centré) reçoit un résidu de moyenne −b_C·(π_s − π̄) ≠ 0 : le test de moyenne ne peut plus rejeter que l'ensemble qui contient la vraie cause. Mon jouet de contrôle (hors dépôt, `numpy.random.SeedSequence(5051, spawn_key=(1,))`, 3 environnements × 10 années × 800 paires, κ cyclique, β = 0,3) donne, par environnement de M1 : sans centrage, moyennes résiduelles de ±0,36 (niveau de strate : NT1, qui fait tout rejeter) ; avec centrage, **0,000 pour l'ensemble sans C et ±0,013 pour l'ensemble avec C**. Ordre de grandeur de ce que κ pouvait fournir même sans centrage : β·Δπ ≈ 0,2 × 0,05 σ_e = 0,01 σ_e contre une erreur type de l'ordre de 0,02 σ_e pour environ 2 000 paires-années par environnement (SUPPOSÉ, raisonnement) : le canal était déjà faible ; le centrage le supprime ou l'inverse. M § 26 ne simule qu'une régression linéaire de la sortie sur C (pas M1).
- Conséquences : (a) l'avantage de l'option 1 sur l'option 2 présenté à Lazar (« M1 garde sa variation ») est faux dans l'état ; les deux options font perdre à M1 la même chose, ce qui rapproche l'option 2 (κ = 1, aucune transformation, chemin supprimé à la source) de l'option 1 ; (b) PA-M1 (0,2 à 0,8, confiance 0,55) n'a plus de fondement ; (c) un échec de M1 à la ligne 7 de la Table A (« ne retrouve pas la cause plantée, même au hasard ») peut venir du prétraitement, non de la méthode.
- Correction proposée : (i) simuler dans un paragraphe nouveau (M § 36) une version approchée de la prédiction invariante linéaire (tests de moyenne et de variance des résidus par environnement de M1, 128 ensembles) sur le jouet de M § 26, avec κ cyclique centré, κ cyclique non centré (niveau de strate nul) et κ = 1 ; (ii) réécrire l'avantage et l'inconvénient des options 1 et 2 de DL-12 d'après ce résultat, et la phrase de S4 ; (iii) soit sortir M1 du centrage de la sortie (centrer seulement dans l'environnement de M1 : le niveau de strate à l'intérieur d'un environnement reste alors un défaut NT1 assumé), soit écrire que M1 est lue après centrage et abaisser PA-M1 ; (iv) l'écrire dans « n'autorise pas ».

### Moyens

**VS5-02 — Moyen — S14 (o) : la moitié « trop propre » ne peut pas sonner ; la moitié « trop mauvais » sonne par construction quand PUISθ est faux.**
- Lignes : S14 (o) l. 550 ; Table Estimation-θ l. 819–824 ; M § 34 (sortie l. 406–410) ; CS4-10 l. 115–116 (proposition : « 0/50 et 50/50 exactement »).
- Constat : « trop propre » = M4 « trouve » dans au moins 5 mondes de plus que l'oracle z₁ vrai sur les 50 mondes appariés. Or l'oracle « trouve » dans 0,97 à 0,99 des mondes sous PUISθ (M § 29, représentation parfaite) : il en compte 48 à 50 sur 50, M4 ne peut pas avoir 5 de plus. Calcul exact : probabilité que M4 ≥ oracle + 5, pour une part vraie de l'oracle de 0,97 et de M4 de 0,78 : 9·10⁻⁷ ; si M4 est aussi bon que l'oracle (0,97 contre 0,97) : 0,005 ; (0,97 ; 0,99) : 0,011. Le déclencheur ne protège donc de rien là où la table est lue ; il n'est pas non plus calibré (M § 34 le dit : « seuil de l'auteur, non calibré »). Côté « trop mauvais » : TROUVEθ(M4) faux alors que l'oracle réussit se produit avec 0,19 (1 − 0,806) pour un M4 sain à 0,78, et presque toujours quand PUISθ est faux (parts 0,45 à 0,73) ; le premier volet de (o) n'exige pas PUISθ vrai, alors que la ligne 0 a déjà écarté la table : audit demandé pour un manque de puissance annoncé.
- Correction proposée : exiger PUISθ vrai dans le premier volet ; remplacer le second par une condition qui peut sonner (par exemple « M4 : 50 sur 50 », ou « M4 dépasse l'oracle d'au moins 2 mondes **et** compte au moins 49 », avec sa probabilité sous M4 sain calculée dans M § 34).

**VS5-03 — Moyen — PUISθ ne garantit la puissance revendiquée que pour une représentation à 0,85 de corrélation (SUPPOSÉ), alors que la Table Bθ qualifie l'identification dès 0,70 ; la grille de M § 29 n'a pas de cas défavorable.**
- Lignes : PUISθ S13 l. 545–546 ; S11 l. 536 ; DL-5 l. 70 (« puissance ≈ 0,8 là où elle est revendiquée ») ; Table Estimation-θ ligne 2 l. 824 ; Table Bθ ligne 8 (IDVθ : r̃ ≥ 0,70 dans au moins 70 mondes sur 100) ; S21 l. 586 ; M § 29 (grille r ∈ {1 ; 0,85} seulement) ; M § 28 et 29 (bruit de la sortie : variable indépendante de variance 3), M § 30 (monde jouet à composantes persistantes de niche et de paire).
- Constat : (a) PUISθ ne compte que des paires-années. Si la représentation de M4 corrèle à 0,70 à 0,82 avec z₁ (qualifiée par la Table Bθ), l'effet est atténué ; en mettant à l'échelle le paramètre de non-centralité du point 0,78 à r = 0,85 (calcul de ma part, premier ordre, sans l'erreur de choix de k̂ qui aggraverait) : puissance 0,57 à r = 0,70, 0,65 à 0,75, 0,72 à 0,80, soit une règle « 37 sur 50 » tenue avec 0,01, 0,12 et 0,45. La ligne 2 (« latente identifiée, effet non retrouvé … non qualifiée ») sonnera alors pour un M4 que la Table Bθ vient de qualifier ; l'oracle (ligne 2a) ne le voit pas, puisqu'il reste à 0,97. Le texte le sait en partie (DL-5, inconvénient : « la puissance revendiquée suppose une corrélation de 0,85 ») mais les tables gelées le lisent comme un échec de l'étape. (b) Le bruit supposé en M § 28 et 29 est indépendant par paire-année ; M § 30 construit au contraire un bruit persistant ; ni S21 ni les prédictions ne l'écrivent. L'oracle couvre ce point (il subit le même bruit), ce qui est un bon choix, mais PUISθ « vrai » peut alors coexister avec une ligne 2a. (c) R4 : la grille de M § 29 est asymétrique (r = 1 et 0,85, jamais 0,70 ni 0,75) alors que la Table Bθ accepte 0,70.
- Correction proposée : ajouter à M § 29 les lignes r = 0,70, 0,75, 0,80 ; soit conditionner la ligne 2 à une valeur réalisée (par exemple r̃ médian de M4 en Bθv1 ≥ 0,85, sinon « non concluant (représentation partielle) »), soit écrire que la ligne 2 inclut l'atténuation ; écrire le modèle de bruit dans S21 ; reformuler DL-5 « sous r = 0,85 supposé ».

**VS5-04 — Moyen — Résidu de T1 : acceptable comme limite déclarée, mais « couvert par la garde et par l'audit d'équilibre » est inexact et « démontrée » excessif.**
- Lignes : DL-12 l. 119 (« fermeture démontrée pour une décision linéaire seulement … couvert par la garde et par l'audit d'équilibre de la validation ») ; nœud 5 (g) l. 164 ; Métrique l. 434 ; Plan § 10 l. 746 ; garde l. 927 ; M § 26.
- Constat : (a) l'audit d'équilibre porte sur S, D, A centrés entre C = 1 et C = 0 : la moyenne centrée est nulle dans chaque strate par construction, donc l'équilibre moyen est automatique ; il ne voit aucune interaction. La garde l. 927 teste une régression linéaire. Ni l'une ni l'autre ne couvre un résidu non linéaire d'une forêt (pentes de S, D, A différentes selon les strates, avec C inégalement réparti entre strates). (b) Seule une régression linéaire est simulée (M § 26) ; M1 (VS5-01), M2 et M3 ne le sont pas ; leur fermeture « au premier ordre » est un argument algébrique plausible (la dépendance moyenne à la strate est enlevée), non une démonstration. (c) La règle de T1 (importance supérieure à celle d'une sonde de bruit dans 9 répétitions sur 10) réagit à toute importance systématique même minuscule (raisonnement, non simulé).
- Réponse à la question posée : **acceptable tel que déclaré si** « couvert » est supprimé, « démontrée » devient « vérifiée par simulation pour une régression linéaire seulement », et la limite est répétée dans « n'autorise pas » (un échec de T1 aux lignes 4 ou 6 peut venir de ce résidu, non d'une confusion du leurre). Le risque est à sens unique (il ne peut que rétrograder T1) et T1 est prédite non qualifiée à la ligne 5 (l. 385, 424) : l'effet sur le verdict est borné. Correction peu coûteuse et préférable : une forêt sur le jouet de M § 26 avec des pentes de S qui diffèrent selon les strates (nouveau paragraphe, quelques minutes de calcul).

**VS5-05 — Moyen — Asymétrie R2 / R2⁻ par le collisionneur L : les règles tiennent, mais S14 (i) sonnera presque sûrement et la confiance de la prédiction de symétrie est contredite par le jouet de l'auteur.**
- Lignes : A-1 l. 215 ; Prédiction de symétrie l. 393 (confiance 0,6) ; S14 (i) l. 550 ; Table A ligne 7bis l. 784 ; AUDIT_EN_ATTENTE l. 767 ; M § 27 (P : R2 0,053, R3 0,993, R2⁻ 1,000).
- Constat : dans le jouet, une méthode linéaire qui conditionne sur L retrouve la cause avec 0,053 en R2 et 1,000 en R2⁻ : écart 0,95 pour un seuil de 0,30. T1, M2 et M3 conditionnent sur L (candidate commune) : l'audit de (i) est déclenché presque à coup sûr, et il conclura « aucun artefact » (le texte le dit). Coût : un audit scellé obligatoire (relecture du code par un sous-agent neuf, relance, recalcul) sur une marge de calendrier de 3 jours, pour un résultat connu d'avance. La prédiction « |R2 − R2⁻| ≤ 0,10, confiance 0,6 » est présentée comme « peu tranchante » mais l'auteur sait qu'elle est fausse pour ces trois méthodes.
- Sur les règles : acceptable. Une méthode biaisée par L perd en R2 (le biais va contre un effet positif) et gagne en R2⁻ ; la ligne 5 (erreur L) et la ligne 7 la rétrogradent avant la ligne 7bis ; aucune qualification n'est créée par l'asymétrie, qui ne peut que priver R2. La lecture de 7bis (« ne retrouve pas une cause de signe négatif ») devient sans objet pour ces méthodes. La comparaison de S23 (rétrodit sans L contre prospectif avec L) n'est pas homogène, mais elle ne peut pas se déclencher à tort puisque R3 (prospectif haut) est exigé en plus de R2.
- Correction proposée : exclure de (i) les méthodes dont l'ensemble de candidates contient L (ou calculer (i) sur la variante sans L) ; confiance de la prédiction de symétrie à 0,3 au plus pour T1, M2, M3, 0,6 pour M1 ; une ligne dans 7bis.

**VS5-06 — Moyen — Le « Résumé de dix lignes pour Lazar » n'est lisible ni en dix lignes ni sans les codes.**
- Lignes : l. 9–20 ; consignes du dépôt (CLAUDE.md : « quasi aucun acronyme, développe les termes » ; communication : verdict d'abord, une ligne par décision).
- Constat : environ 1 000 mots, dont plus de 50 renvois codés (GF, DL, S, M §, CS4, Q6, PCMCI, DirectLiNGAM, R2⁻, D5) ; l'élément 12 compte 1 058 caractères, l'élément 5 près de 1 000. Lazar doit trancher DL-1 à DL-13 et geler S1 à S23 ; il ne peut pas lire ce résumé sans le reste, et le reste fait 272 Ko.
- Correction proposée : un résumé de dix vraies lignes, en français courant, qui dit ce que l'épreuve mesure, ce qu'elle ne dit pas, et ce que chaque décision change (une ligne par décision, enjeu et recommandation) ; les codes restent dans le corps.

### Mineurs

**VS5-07 — Mineur — S12 passe à 0,15 mais les prédictions de M3 et M3b restent à 0,10.** Lignes : S12 l. 540 ; PA-M3 l. 390 (« ≤ 0,10 prédits ; au-delà : prédiction réfutée, artefact constaté ») ; PA-M3b l. 391 et HR-M3b l. 346 (« au-delà de 0,10 »). Entre 0,10 et 0,15 la prédiction est réfutée sans que S12 constate un artefact, et la sensibilité de M3b comme « témoin positif de la mesure d'échelle » est jugée à 0,10 alors que la mesure décide à 0,15. Aligner ou écrire la différence.

**VS5-08 — Mineur — Historique du brouillon 4, ligne Q8 (l. 232) : « le jumeau C⁰ la réalise déjà ».** Corrigé en W4 et au Résumé 3 (CS4-11 (b)), mais la ligne périmée reste dans un tableau que le lecteur croisera. Ajouter « corrigé au brouillon 5, CS4-11 ».

**VS5-09 — Mineur — Notation : « E × P ≥ 36 ≥ 22 » (S13 l. 546, DL-8 l. 94) emploie E pour le nombre d'environnements,** alors que E désigne partout ailleurs l'ensemble tenu hors de l'entraînement (50 % des paires). Écrire « nombre d'environnements × P ».

**VS5-10 — Mineur — La « base minimale » (3 environnements, 12 années, u₂ = 36) citée en DL-8 (l. 91–92) et S19 (l. 576, M § 15) ne passe plus le plancher de S13.** 3 × 1 000 × (12 − 8) = 12 000 < 20 000, et les « minima » de S13 (3 environnements, 12 années) ne peuvent pas être atteints ensemble ; les bases admissibles les plus petites sont 3 environnements à 15 ans, 4 à 13, 5 à 12 (M § 31). Réécrire les exemples et les minima en conséquence.

**VS5-11 — Mineur — Garde « centrage et κ » (l. 927) : le seuil « au plus 18 détections sur 1 000 » est calibré sur un niveau de 0,010 (fausse alarme 0,0069), mais le centrage donne 0,013 dans M § 26 (écart type de Monte-Carlo 0,006).** Si le niveau vrai est 0,013, la garde saine sonne avec 0,069 ; à 0,017 (erreur L à 10 %), avec 0,34. Calibrer sur le niveau mesuré de la base jouet, ou relever le seuil et recalculer la fausse alarme.

**VS5-12 — Mineur — Table Estimation-θ : la ligne 0 (« non PUISθ ») précède la ligne 1 (fausse détection), alors que la note l. 827 dit qu'« une fausse détection ne dépend pas de la puissance ».** Une méthode qui invente un effet n'est donc pas signalée quand PUISθ est faux. Choix défendable (rien n'est revendiqué), mais à écrire, ou à placer la fausse détection avant la puissance.

**VS5-13 — Mineur — « Demander au collisionneur » n'est qu'une parenthèse de la recommandation (DL-5 l. 75, DL-12 l. 122, DL-13 l. 129).** Format de décision du dépôt : options avec avantage et inconvénient ; ici ni délai (la marge est de 3 jours), ni coût, ni dire qui contacte (contact externe : tu rédiges, Lazar envoie). En faire une option numérotée ou la retirer.

**VS5-14 — Mineur — Validateur : l'entrée « Contre-lecture 3 » contient déjà deux empreintes de 64 caractères (script et sortie), donc la vérification « deux empreintes » passera même si le brouillon relu et le rapport ne sont pas cités.** À remplir par l'orchestrateur avec `435b16ef1ace0816951a28b039c0264c1eb6d1564a6ee2681c6f94b202259155` et l'empreinte de ce rapport (à calculer après écriture, non écrite ici).

---

## C. Points tenus (vérifiés, à ne pas toucher)

- Lignée de calcul : deux rejeux identiques, § 1 à § 25 identiques à b4, chiffres du texte = sortie (une trentaine recoupés ; arrondis des parts 0,78 et 0,73 expliqués en A3).
- Test par permutation dans les strates de u : exact sous l'hypothèse nulle de B-θ, parce que z est tiré indépendamment par paire-année sachant u, l'encodeur est commun mais entraîné hors de E et k̂ choisi sur E₁ ; S, D, A, g(Y) de l'année t ne dépendent pas de z_t (retard ℓ) ; la dépendance de la sortie entre paires d'une niche n'importe pas pour une permutation de ẑ seul. Point 3 des « points à attaquer » : **oui, exact** dans B-θ (pas en B-hors, écrit).
- Rétrodiction : définition de b5 sans mécanisme évident d'association avec le passé hors de κ, L et de la série renversée (point 2 des « points à attaquer ») ; le décalage de PCMCI conditionne uniquement sur des valeurs antérieures à l'année de la sortie décalée.
- Plancher de S13, PUISθ, S11, S12 : arithmétique exacte (A3).
- Oracle z₁ vrai (ligne 2a) : bon dispositif pour séparer manque de puissance de conception et échec du réseau.

## D. Traitement attendu

Pour chaque VS5-xx : accepté / refusé et pourquoi, dans l'entrée « Contre-lecture 3 » du brouillon suivant (R12) : identifiant `claude-sonnet-5-5`, empreinte du brouillon relu (`435b16ef…`), empreinte de ce rapport. Le majeur VS5-01 demande une simulation nouvelle (M § 36) et une réécriture de DL-12, S4 et PA-M1 ; VS5-02, VS5-03, VS5-04 et VS5-05 modifient S14, S13 ou S21, les Tables et M § 29 ; une relecture des seuls passages modifiés suffirait ensuite.
