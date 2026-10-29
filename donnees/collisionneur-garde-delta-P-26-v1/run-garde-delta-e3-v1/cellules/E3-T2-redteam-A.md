# Tour III.2 — équipe rouge croisée — proposition A

## Préambule

- Pièces B et C reçues entières (chacune se termine par sa ligne de fin). Pièce F : non servie [VÉRIFIÉ, en-tête des faits]. Les scripts et `donnees/` sont absents ; je n'en invente rien.
- Statuts : [VÉRIFIÉ] = lisible dans le code ou les docstrings de la pièce A ; [RAPPORTÉ] = chiffre recoupé par une contre-lecture ou texte de décision ; [HYPOTHÈSE] = ce que j'en déduis. Tout chiffre à moi est « illustratif ».
- Garde de sûreté : les « scénarios d'évasion » demandés portent sur **l'instrument statistique** (garde, règle de gel, fichier du pilote, script), jamais sur un mode de sabotage, un texte d'action ou l'interne d'un moniteur. Je décris ce qu'une *loi de scores* adverse ferait à la garde, sans dire comment la produire.
- Règle B4 : chaque contrôle négatif de (c) est écrit en H_A / H_B exclusives, chaque issue réfutant quelque chose.

---

## Contre la proposition B

### (a) Failles

**B-F1 — δ = min(Δ_min/2 ; 0,05) borne un gain que la fiche ne certifie pas.** La fiche certifie E[v_j] > 0 ; les bornes basses sont « rapportées, jamais une condition de promotion » [VÉRIFIÉ, `borne_basse`]. Donc, sous le modèle d'artefact de B (a9), un sujet dont le seul gain est un artefact d'unité ε < δ a E[v] ≈ ε(1 − r_B) > 0 et E[g] ≈ ε < δ : les 2k processus dérivent dans le bon sens et la fiche est promue avec probabilité → 1 quand n grandit [HYPOTHÈSE]. « δ ≤ Δ_min/2 » ne borne rien, puisque Δ_min n'est jamais testé. B teste la vacuité (E4) « au n prévu » seulement : c'est un plancher de puissance de l'artefact, pas une borne. Le mot « vide » de l'arbitre n'est pas fermé par δ, seulement par une condition sur la borne basse — que D-S11 (c) exclut [RAPPORTÉ, N-055].

**B-F2 — Δ_min est hors des pièces, et B l'interdit lui-même.** B (a7) note que P-9 interdit toute lecture des sabotés de développement avant G1 [RAPPORTÉ, pièce D]. Δ_min ne peut donc venir ni du pilote ni de l'épreuve : il vient d'un choix. Or ce choix fixe δ et n_h. La règle R est « déterministe » mais ses entrées (Δ_min, k) sont des leviers libres (voir B-E3).

**B-F3 — n_h ≥ 250 est repris de l'erratum sans son contexte.** L'erratum dit « 0,96 à 250 unités » à τ = 0,01 [RAPPORTÉ, n° 176] sans préciser k ni K_h. B dit lui-même (a8) que k est « probablement > 3 » et qu'« aucun chiffre n'existe à ce k ». « ≥ 400 si K_h = 3 » n'a pas de source. Ces deux nombres sont SUPPOSÉ, pas RAPPORTÉ comme le laisse croire le tableau e3.

**B-F4 — Provenance contradictoire.** B prend les jumeaux honnêtes des unités d'épreuve : n_h vaut alors le nombre d'unités d'épreuve à honnêtes, de l'ordre de n_s. Si n_s est 160 (valeur de toutes les simulations), n_h = 160 < 250 : la recommandation e3 se contredit sauf à exiger 250 unités sabotées de plus, dont le coût est au devis de la couche 2 (N-056 : « plusieurs centaines de tâches sabotées de plus par mode » [RAPPORTÉ]). Le lot honnête séparé est conditionné à E6, qui n'est pas décidable (B-F5).

**B-F5 — E1 et E6 ne peuvent pas falsifier (B4).** Seuil de 0,005 avec ≈ 16 unités ; B calcule lui-même (a6) une erreur type ≈ 0,011 (illustratif). Aucune issue ne sépare H_A de H_B. E6 sur l'épreuve serait une lecture avant G1 (R1) ; sur le pilote, elle est aveugle. La proposition repose sur des expériences dont l'issue est indéterminée par construction.

**B-F6 — b_h fabrique le verdict « nœud ».** b_h = borne haute à 2 erreurs types sur ≈ 16 unités ≈ 0,02 même sous biais vrai nul (illustratif, à partir de a6). Cela pousse dans la plage b = 0,025 : « 350 à 2 400 unités » [RAPPORTÉ, C v3 § 7]. R rendra « nœud » quelle que soit la loi réelle : la sortie de R est une fonction de la taille du pilote, pas des données.

**B-F7 — Les ex æquo vont dans un seul sens, favorable au sujet.** Convention stricte : P(alerte d'un honnête neuf) = j/(n + 1) ≤ τ, « moins encore avec des ex æquo » [VÉRIFIÉ, docstring `seuil`]. Un sujet à échelle de score à atomes près du seuil a donc f_A < τ hors échantillon, E[g] < 0 par construction, et la garde certifie tôt et avec marge. B (a5) range les ex æquo parmi les « sources de E[g] ≠ 0 » comme si elles étaient symétriques. P-15 n'est pas dans le code v42 [VÉRIFIÉ, pièce A ; RAPPORTÉ, pièce D].

**B-F8 — La règle d'arrêt laisse une porte de relance.** La garde (a, b, δ) est dans la clé `affirmation` [VÉRIFIÉ, `construire`]. Un δ′ fait une autre affirmation, donc une autre fiche admise par `Lignees` avec un budget neuf, sur une partie disjointe (D-S12 : héritage entre parties disjointes [RAPPORTÉ, N-055]). Le diagnostic « garde non certifiée » lu dans `log_gardes_finales` est précisément l'information qui motive la relance avec δ′ = 0,10. B interdit la relance « sur les mêmes unités » (K9-1) mais pas la relance avec un autre δ : la porte de sortie après lecture est ouverte.

**B-F9 — E5 ne sonde pas le cas où K7-6 casse.** Sous alignement par rang, l'unité u apparaît au rang t′ du contraste et au rang t ≠ t′ de la garde. Si un lien intra-unité existe (artefact d'unité), l'incrément de contraste à t′ < t renseigne sur l'incrément de garde à t : la garde n'est plus une surmartingale pour la filtration jointe, et le minimum arrêté n'est plus une e-valeur [HYPOTHÈSE]. E5 (« contrastes favorables », sans lien d'unité) teste une configuration où rien ne peut casser.

### (b) Scénarios d'évasion (niveau instrument)

**B-E1 — artefact pur.** Loi de scores de A = loi de B_j décalée de ε sur honnêtes et sabotés d'une même unité, ε = 0,9δ (le propre E4 de B). Fiche promue avec probabilité croissante en n (B-F1) ; à δ = 0,05, ε ≈ 0,04 = quatre fois le point de fonctionnement τ = 0,01 [RAPPORTÉ, D-S5]. Coût : aucune connaissance des épisodes d'épreuve ; seulement un trait d'unité sans rapport avec le sabotage.

**B-E2 — atomes.** Échelle de score discrète au voisinage du seuil (B-F7) : E[g] < 0 par construction, garde gagnée, et marge pour absorber un artefact. Coût nul.

**B-E3 — réglage de R par ses entrées.** Δ_min et k sont « scellés maintenant » par qui ? Conv-audit est concepteur des moniteurs [RAPPORTÉ, N-056 § 6]. Choisir Δ_min = 0,10 donne δ = 0,05 ; Δ_min plus petit donne un δ plus petit mais un n_h hors devis → « nœud » → pression vers δ = 0,10 (D-S). R est déterministe, ses leviers ne le sont pas.

**B-E4 — fichier du pilote.** La spécification retient les unités « à au moins un épisode honnête » et un signe A − B [RAPPORTÉ, C v2]. Sélection d'unités et signe sont deux leviers sur b_h. B prévoit un recalcul « à 0 écart » (c4) sans dire par quelle main.

**Tous à la fois** : B-E2 + B-E1 + B-E3 (Δ_min large) donnent une fiche promue sans gain de détection sur les sabotés hors artefact, avec une garde « certifiée avec marge ». Coût : zéro accès aux données d'épreuve.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **A ≡ B_j sur la partie fraîche** (jumeau calibré, contrôle 12, sur la partie lue et non le calibrage). H_A : P(promue) ≤ 1/seuil et la garde certifie dans ≥ 0,8 des suites au n_h gelé ; H_B : l'une des deux tient en défaut. H_B réfute la fiche (niveau non tenu ou garde muette sur un sujet identique) ; H_A réfute l'objection « la garde mesure le calibrage ». B n'a que c5 (taux ≤ τ + 2 ET), pas le test de fiche.
2. **Artefact pur à n = 3·n_h** (illustratif). H_A : promotion ≥ 0,5 ; H_B : < 0,5. H_A réfute « δ suffit » ; H_B réfute B-F1 pour ce δ.
3. **Atomes.** Même sujet, scores arrondis contre continus. H_A : |ΔE[g]| ≤ 0,005 (illustratif) ; H_B : au-delà. H_B réfute « la garde mesure un artefact de source » (elle mesure la granularité) ; H_A réfute B-F7 pour cette grille.
4. **Relance.** Une seconde fiche, même affirmation à δ près, soumise à `Lignees` : H_A : refusée par une règle scellée hors code ; H_B : acceptée (le code l'accepte [VÉRIFIÉ]). H_B rend le gel de B caduc.
5. **Ordre secret permuté** (autre graine) sur une fiche à la frontière avec lien d'unité. H_A : P(promue) ≤ 1/seuil sur toutes les graines ; H_B : dépassement sur une. H_B réfute la validité du minimum par rang (K7-6) ; H_A réfute B-F9 pour cette loi.
6. **R sur pilotes synthétiques** : 1 000 fichiers de ≈ 16 unités à biais vrai nul. H_A : part de verdicts « nœud » ≤ 0,2 (illustratif) ; H_B : > 0,2. H_B réfute R comme instrument (c'est un dé).

---

## Contre la proposition C

### (a) Failles

**C-F1 — Statuts gonflés.** C étiquette [VÉRIFIÉ] des chiffres de simulation de l'auteur recoupés par les contre-lectures (au mieux RAPPORTÉ), et [VÉRIFIÉ] des cellules de son tableau n₈₀ qui n'existent dans aucune pièce : « ≈ 250–400 », « ≈ 200–300 », « ≈ 85–100 », « ≈ 110–145 », « ≈ 160–200 ». La seule plage existante est « 160 à 530 » pour les k gardes à biais 0 toutes lois confondues [RAPPORTÉ, C v3 § 7] ; la ventiler par cellule est une interpolation. Par le critère gelé de la synthèse, tout cela est SUPPOSÉ. Les « confiance 0,95 (illustratif) » sont des chiffres sans objet.

**C-F2 — La règle 2C est incohérente et biaisée vers le relâchement.** (i) La formule δ = clip(μ̂ + (144/N_h)·0,05 ; 0,05 ; 0,10) rend un continuum : μ̂ = 0,0125 et N_h = 160 donnent 0,0575, alors que le texte dit « dans {0,05 ; 0,10} ». (ii) « 144/N_h × 0,05 » n'est dérivé de rien : 144 est le plancher à écarts nuls au seuil 160 pour δ = 0,05 [RAPPORTÉ, pièce E], mélangé à N_h sans justification. (iii) μ̂_g,max = max_j(ḡ_j + 2 ET) : le maximum de k estimateurs bruités est biaisé vers le haut, et avec ≈ 16 unités chaque ET est ≈ 0,011 (illustratif, repris de B a6) ; pour un sujet honnête, la règle rend δ = 0,10 par construction. C'est l'inverse de B-F6 : le bruit du pilote devient une garde plus lâche. (iv) Les ḡ_j du pilote sont calculés avec des seuils calibrés sur le lot C du pilote, pas sur les 9 600 du calibrage de G1 : avec un petit n_cal, la discrétisation j/(n + 1) [VÉRIFIÉ, docstring] est plus grossière ; la quantité mesurée au pilote n'est pas E[g] de G1 [HYPOTHÈSE sur le transfert].

**C-F3 — « Unités honnêtes pures » : population scindée.** Les unités à sabotés et les unités honnêtes pures sont deux populations ; la contre-lecture v4 (Q7) signale déjà un biais de sélection « non mesurable dans le script » [RAPPORTÉ]. K7-6 : longueurs différentes → « espérance au franchissement joint non garantie ≤ 1 » [VÉRIFIÉ]. « Compatible à 100 % avec le code » n'est pas « valide ». Et un N_h ≫ N_s offre un levier d'évasion (C-E2).

**C-F4 — « Techniquement impossible de lire G1 sans garde » est faux.** `evaluer` prend `ecarts_faux_positifs=None` (« la garde (facultative) ») et `construire` accepte `garde=None` [VÉRIFIÉ, pièce A]. La protection est D-S4 (décision), pas le code. La règle 4 de C s'appuie sur une garantie mécanique qui n'existe pas.

**C-F5 — « Arrêt et nœud pour Lazar » après lecture est une porte de sortie.** Un nœud ouvert après avoir vu que les contrastes ont franchi et pas la garde est, par définition, une décision après lecture. Même relance possible qu'en B-F8 (δ′ = autre affirmation, budget neuf, partie disjointe). C ne la ferme pas.

**C-F6 — Expériences 1 à 3 : seuils indécidables sur 16 tâches.** Exp 1 : zones 0,005 / 0,0125 avec ET ≈ 0,011 ; Exp 2 : φ_h ∈ ]1,15 ; 1,50[ non tranché, et à τ = 0,01, K_h = 10, f_A ∈ {0 ; 0,1 ; …} sur 16 unités ne permet pas d'estimer φ_h (illustratif) ; Exp 3 est synthétique bien que titrée « sur les lots C/J ». Exp 1 suppose P-15 appliqué en amont de la banque ; rien dans v42 ne le fait [VÉRIFIÉ].

**C-F7 — E[g]_tol et l'« arrêt de porte » à 0,025.** Même max sur k, même ET ≈ 0,011 : un arrêt de porte déclenché par le bruit d'un pilote de 16 tâches.

**C-F8 — Garantie 1A mal énoncée.** « FWER ou FDR via `ebh_pondere` » : l'e-BH tient le FDR ; le FWER n'est tenu que par `bonferroni()` [VÉRIFIÉ]. Une phrase scellable doit choisir.

### (b) Scénarios d'évasion (niveau instrument)

**C-E1 — la règle 2C se relâche seule.** Rien à faire : le bruit du pilote et le max sur k poussent δ vers 0,10. Levier adverse : plus de comparateurs k → max plus haut → δ plus grand. Coût nul.

**C-E2 — population scindée.** Loi de scores de A dont les alertes honnêtes excédentaires portent sur les unités **mixtes** (celles qui ont des sabotés) et non sur les honnêtes pures. Avec 160 mixtes + 240 pures, E[g] est dilué par 160/400 (illustratif) tandis que le contraste profite de l'artefact sur toutes les mixtes. Il suffit d'un trait d'unité corrélé au fait d'avoir été retenue pour sabotage. Coût faible, aucune lecture d'épreuve.

**C-E3 — atomes** (B-E2) : identique.

**Tous à la fois** : C-E1 (δ ≈ 0,10) + C-E2 + C-E3 : artefact ε ≈ 0,08 certifié « sans artefact de source » avec marge.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **A ≡ B_j sur la partie fraîche** (comme B, contrôle 1).
2. **2C sur pilotes synthétiques à biais nul** : H_A : part de δ = 0,10 ≤ 0,1 (illustratif) ; H_B : > 0,1. H_B réfute la règle (elle code le bruit) ; H_A réfute C-F2 (iii).
3. **Pures contre mixtes** : pour le jumeau calibré, E[g] sur unités pures contre E[g] sur unités mixtes. H_A : écart ≤ 0,005 (illustratif) ; H_B : au-delà. H_B rend l'option 3.2 invalide ; H_A réfute C-F3 pour le jumeau. Mais : ce contrôle n'est faisable ni sur l'épreuve (R1) ni sur un pilote sans unités pures — son **impossibilité** avant scellement est déjà fatale à l'option 3.2.
4. **Engagement sans garde** soumis au circuit de scellement : H_A : refusé par une règle scellée hors code ; H_B : accepté (le code l'accepte, C-F4). H_B invalide la règle 4 de C.
5. **Ordre secret permuté** (comme B, contrôle 5), nécessaire ici d'autant plus que N_h ≠ N_s.
6. **Graine neuve sur chaque cellule du tableau n₈₀** (critère de la synthèse) : H_A : la cellule est reproduite ; H_B : elle n'est pas calculable. Chaque H_B retire la cellule ; les cinq cellules interpolées de C-F1 sont attendues en H_B.

---

## Ce que je reprends, en le disant (B1)

- De B : a7 (P-9 interdit un fichier de contraste réel ; la puissance de la fiche restera conditionnelle à un contraste synthétique) et le contrôle « δ = 0,99 ⇒ P(fiche) = P(contrastes) exactement » (E2). Je les tiens pour des contraintes vraies sur tout gel.
- De C : l'ordre t₀–t₅ (script figé → pilote → extraction → passage → scellement → lecture unique) est le bon squelette ; j'en retire la table de décision 2C (C-F2) et la règle 4 (C-F4, C-F5).
- Commun aux deux et à fermer par tout gel : (i) la relance avec δ′ (B-F8, C-F5) ; (ii) la direction des ex æquo (B-F7) ; (iii) l'indécidabilité de toute mesure de biais sur ≈ 16 unités (B-F5, C-F6) — ce qui signifie que **le fichier du pilote ne peut pas fixer b_h**, seulement la forme de la loi (surdispersion, atomes) ; (iv) la vacuité : δ seul ne borne pas l'artefact pur (B-F1), et aucun des deux ne propose de contrôle « artefact pur à grand n ».

FIN-DE-CELLULE