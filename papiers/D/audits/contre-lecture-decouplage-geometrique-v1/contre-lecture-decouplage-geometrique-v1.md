# Contre-lecture : découplage géométrique entre filtre de chaîne de pensée et sonde d'audit (v2)

Contre-lecteur neuf (Opus 5.5) ; aucune pièce lue n'est de lui. Date : 24 novembre 2026. Branche `papier-d/evasion-post-entrainement-v1`, au commit `e528e725`.
Pièce : `papiers/D/theorie/decouplage-geometrique-v2.tex`, empreinte vérifiée. Code, tests et résultats : `papiers/D/code/experience_jouet_decouplage_sonde_v1.py`, `papiers/D/code/test_experience_jouet_decouplage_sonde_v1.py`, `papiers/D/resultats/decouplage-v1/`. Toutes les empreintes compagnons ont été vérifiées.
Aucun fichier du dépôt n'a été modifié. Toutes les exécutions ont eu lieu sur une copie, dans le bloc-notes.

## Verdict : **tient avec réserves**

J'ai refait les preuves des deux théorèmes. Elles sont justes sous leurs hypothèses écrites : pas d'erreur de signe ni de constante. Le facteur 1/2 est juste, et la borne de robustesse est atteinte. La formule de dérive au premier ordre se vérifie numériquement à 2e-12 près. Tous les chiffres du paragraphe « Numerical check » se retrouvent dans le JSON, et la relance donne un JSON identique, au bit près, hors manifeste. Un seul chiffre est mal arrondi.

Les réserves portent surtout sur ce que le texte fait dire aux théorèmes :
- Le second théorème garantit que la fonction de score de la sonde ne bouge pas. Il ne garantit pas la grandeur que l'introduction annonce, la dépendance entre la survie au filtre et la survie à l'audit. J'en donne un contre-exemple constructif.
- La remarque recommande de surveiller ‖Ww‖. Cette surveillance ne suffit pas, et la partie 3 du même théorème le montre. Contre-exemple exact à l'appui.
- Les résultats classiques ne sont pas cités.
- Deux constats de l'expérience jouet découlent de sa construction, et le texte ne le dit pas.

## Défauts

### Majeurs

**M1. Le second théorème ne règle pas la dépendance entre survie au filtre et survie à l'audit, alors que l'introduction l'annonce.**
Endroit : `decouplage-geometrique-v2.tex`, ligne 6 (« The results below say which geometric conditions … create or remove that dependence ») et ligne 82 (remarque, premier point : « a probe on disjoint neurons is provably untouched »).

La partie 1 du second théorème donne l'invariance de la fonction x ↦ s(x). Pendant l'entraînement, la survie au filtre β_loop(x) = 1 − σ(aᵀW h(x) − b) change. Le poids de sélection de l'opérateur A change donc aussi, et avec lui la loi de s chez les tricheurs qui survivent au filtre. Or c'est cette loi qui définit la grandeur du régime de découplage statique (R2) : la covariance entre survie au filtre et survie à l'audit, qui donne la survie à l'audit sous la loi pondérée par β_loop.

Contre-exemple constructif : `verif/v4_contre_exemple_signe.py`, réseau ReLU, sonde sur des neurones disjoints de ceux du filtre. Les lignes de M lues par la sonde restent identiques au bit près, et l'aire sous la courbe de la sonde vaut 0,6914 avant comme après. Pourtant :

| Grandeur | Avant l'entraînement | Après l'entraînement |
|---|---|---|
| Taux de capture de l'audit parmi les survivants du filtre | 0,519 | 0,356 |
| Évasion conjointe (le tricheur passe le filtre et l'audit) | 0,185 | 0,492 |

Le mécanisme : il y a deux sous-types de tricheurs. Le filtre voit le type A, la sonde voit le type B. L'entraînement fait survivre davantage de tricheurs de type A, que la sonde ne voit pas.

Sur le réseau du papier, cette grandeur bouge aussi, quoique dans le sens favorable :
- ReLU, sonde disjointe : capture parmi les survivants de 0,359 à 0,415 ; covariance de −0,002 à −0,042.
- Réseau linéaire : la covariance passe de +0,014 à −0,006, donc change de signe.

Sur 48 tirages du jouet tel qu'il est construit, la capture parmi les survivants n'a jamais baissé (`verif/v3_moniteur_et_signe.py`). Le jouet ne met donc pas ce risque à l'épreuve. Il ne mesure d'ailleurs que l'aire sous la courbe sur tous les tricheurs, jamais sur les survivants.

Le premier théorème montre déjà, pour la sélection, que la condition pertinente est l'indépendance de s et de Wh. En gaussien, cela revient à WΣw = 0, une orthogonalité dans la métrique Σ et non une disjonction de neurones. Une sonde disjointe en neurones mais corrélée à Wh par l'entrée commune reste donc exposée à la sélection.

Correction proposée :
- Ligne 6 : écrire que le premier théorème caractérise la dépendance sous sélection, et que le second ne dit que l'invariance de l'instrument (la fonction de score), pas celle de sa survie parmi les survivants du filtre.
- Ligne 82 : ajouter que la disjonction de neurones protège l'instrument contre la dérive par gradient. La sélection du premier théorème continue de jouer sur la loi des épisodes qui survivent, et son effet se recalcule à chaque étape avec le β_loop courant.
- Dans l'expérience, rapporter aussi le taux de capture de l'audit pondéré par la survie au filtre, avant et après.

**M2. Surveiller ‖Ww‖ ne détecte pas le recrutement des neurones de la sonde. La partie 4 et la remarque sont en contradiction avec la partie 3.**
Endroit : ligne 67 (partie 4) et ligne 82 (troisième point : « monitor the coupling ‖Ww‖ »).

La partie 1 cesse de s'appliquer dès que W_{:,S} ≠ 0, et non dès que Ww ≠ 0. La partie 3 montre précisément qu'une sonde avec Ww = 0 qui partage des neurones avec la tête dérive.

Contre-exemple exact (`verif/v3_moniteur_et_signe.py`) : la dynamique de (M, W) ne dépend pas de w. Je prends donc la sonde, fixée d'avance sur les neurones S, orthogonale aux lignes de W_{:,S}(T). On obtient :
- ‖W(T)w‖ = 5e-16 ;
- ‖W(T)_{:,S}‖ = 3,06 ;
- dérive maximale du score de la sonde : 3,4e-3.

Un auditeur qui suit ‖Ww‖ ne voit rien. Dans une variante où seule la dérivée initiale de Ww est nulle (c·w = 0 au départ), on trouve ‖Ww‖ = 0,27 contre ‖W_{:,S}‖ = 3,06.

Deux précisions sur la partie 4 :
- « Neuron-disjointness is not preserved » se démontre par dW_{:,S}/dt = −E[∇_zℓ h_S(x)ᵀ], pas par d(Ww)/dt.
- « correlation » devrait être « moment croisé non centré » E[∇_zℓ s(x)].

Correction proposée : énoncer la partie 4 avec W_{:,S}, et faire surveiller ‖W_{:,S}‖, ou Σ_{i∈S} |w_i| ‖W_{:,i}‖, la quantité que la partie 3 désigne. ‖Ww‖ ne sert qu'au cas linéaire.

**M3. Antériorité : aucune citation, et l'essentiel est classique.**
Endroit : tout le fichier ; aucun `\cite`. La seule référence est « Lancaster, 1957 », en texte libre, ligne 42.

Ce qui est classique :
- Les parties 1 et 2 du premier théorème : effet sur une variable gaussienne d'une sélection faite sur d'autres variables. C'est la formule de sélection de Pearson, Aitken et Lawley ; la version par l'identité de Stein est un lemme connu.
- La partie 3 : la borne de Cauchy–Schwarz en χ² (type Chapman–Robbins), combinée à la corrélation maximale de Hirschfeld, Gebelein et Rényi. Ce sont des outils standard des inégalités de traitement de l'information.
- Pour le second théorème : la partie 1 dit qu'un gradient nul par construction laisse les paramètres fixes, un fait élémentaire, voisin de l'acheminement des gradients (« gradient routing »). La partie 3 est un calcul de noyau tangent neuronal restreint à la première couche. La partie 4 est un calcul direct.
- La remarque « Uncorrelated is not enough » est un fait de manuel.

Le texte ne se dit pas nouveau, mais « sharpens » (ligne 82) et l'absence de toute source le laissent croire.

Correction proposée : présenter ces résultats comme des applications de résultats connus au cadre du filtre et de l'audit, et citer les sources (liste à vérifier en fin de rapport). Avant toute formulation de contribution, situer le texte face aux travaux voisins sur l'évasion de sondes d'activations sous entraînement : activations obfusquées, obfuscation sous apprentissage par renforcement, et modèles qui échappent à des sondes inconnues (règle R8).

**M4. Deux constats de l'expérience jouet découlent de sa construction (règle R4, résultat trop propre), et le paragraphe les présente comme des vérifications.**
Endroit : ligne 85.

(a) « probe scores unchanged to machine precision » (sonde disjointe). La variation est exactement 0.0, au bit près. Les lignes de gradient des neurones de la sonde sont nulles par construction : W[:,12:24] = 0, U[12:24,:] = 0, et l'ancrage s'annule tant que M ne bouge pas. Ce constat vérifie le code, pas une prédiction qui aurait pu échouer. De même, l'orthogonale linéaire bouge de 1,8e-15 parce que w ᵀ(M − M0) reste nul à l'arrondi près, ce que garantit la partie 2.

(b) « a re-fitted probe keeps an area under the curve of about 0.83–0.86 ». Dans le réseau linéaire, la valeur 0,856 est l'aire sous la courbe de Bayes sur les entrées, Φ(1,5/√2) = 0,8556. Les entrées sont fixes, la triche est une étiquette d'entrée, et h = Mx reste injectif : l'analyse discriminante réajustée ne peut pas perdre cette information. Le constat est donc tautologique en linéaire, et presque en ReLU (d = 32 > p = 16).

Le jouet ne montre pas non plus que la séparabilité « survit » dans un cadre où l'épisode lui-même dépend de la politique : ici, les entrées ne dépendent pas de l'entraînement.

Correction proposée : écrire que l'invariance exacte et l'aire réajustée sont des conséquences de la construction, données comme contrôle du code. Dire que les épisodes sont des entrées fixes, de sorte que seule la représentation est entraînée et non le comportement.

### Mineurs

**m1. Un écart mal arrondi, et une erreur type mal calibrée.**
Endroit : ligne 85 (« 0.5, 1.1 and 1.1 »), et le calcul de l'erreur type dans le code, ligne 93.

Les écarts valent 0,49, **1,18** et 1,06 erreurs types : le deuxième s'arrondit à 1,2.

L'erreur type du code est « crude » (c'est le commentaire de la ligne 92) : std((wt − 1)s)/√n. Elle n'est pas centrée sur s et ignore que la prédiction est estimée sur le même échantillon. Par 40 répétitions à n = 4e5, l'écart type réel de (décalage simulé − prédiction) vaut 1,70, 0,85 et 0,81 fois l'erreur type du code (`verif/v1_selection.py`). En unités correctes, les écarts deviennent environ 0,3, 1,4 et 1,3.

La conclusion ne change pas : par quadrature exacte, l'identité de Stein tient à 1e-10 près (décalage exact −0,93581 pour la sonde alignée, −0,011220 pour la sonde au hasard).

Correction proposée : corriger 1,1 en 1,2 ; donner une erreur type par la méthode delta sur la différence, ou par répétition ; mieux encore, comparer à la valeur exacte par quadrature unidimensionnelle (g ne dépend de h que par u = aᵀWh).

**m2. Le contre-exemple de la remarque se calcule exactement.**
Endroit : ligne 46.

Par quadrature, le décalage vaut **−0,07747**. La simulation donne −0,0782, à 1,25 erreur type. « about −0.078 » est acceptable, mais la valeur exacte est meilleure.

Il faut aussi dire que l'exemple rentre dans le cadre linéaire : h = (x, x² − 1), W = (1, 0), w = (0, 1), Σ = diag(1, 2), d'où WΣw = 0.

**m3. Formulations du paragraphe numérique.**
Endroit : ligne 85.
- « mean cheater score −0.058 » est un décalage du score moyen des tricheurs, pas un score.
- La sonde orthogonale partagée en ReLU « bouge » (0,78), mais son aire sous la courbe monte légèrement (0,7485 → 0,7500) : elle n'est pas éludée. Il faut l'écrire, sinon le lecteur confond « déplacée » et « éludée ».

**m4. Classe d'optimiseurs : quatre cas de bord.**
Endroit : ligne 55.
- Adam avec ε = 0 et moments nuls donne 0/0. La mise à jour ne « s'annule » pas : elle vaut NaN (`verif/v2_jouet.py`). Il faut exiger ε > 0.
- « momentum » doit être, comme pour Adam, à tampon initialisé à zéro. Un état d'optimiseur repris d'un entraînement antérieur fait bouger les neurones de la sonde : dérive de 7e-7 constatée avec un premier moment initial de 1e-3.
- L'écrêtage par la norme globale et les rapports de confiance par couche (LAMB, LARS sans décroissance) sortent de la lettre de la définition, « gradients with respect to m_i only », mais gardent la conclusion. Élargir la définition : une mise à jour de m_i, fonction de tous les gradients passés, qui s'annule quand ceux de m_i sont nuls.
- Les préconditionneurs pleins (gradient naturel complet) sont exclus, à juste titre ; à dire.

**m5. Décroissance des poids.**
Endroit : ligne 55.

L'exclusion est juste : constaté, la décroissance simple déplace la sonde (dérive maximale 1e-2). Mais la décroissance centrée sur les poids initiaux, que le texte admet, est une pénalité sur les paramètres et non un terme ψ_i(h_i(x), x).

Correction proposée : ajouter Σ_i r_i(m_i) avec ∇r_i(m_i(0)) = 0 à l'équation `eq:train-objective`.

On peut aussi noter qu'une décroissance découplée pure est, sur les neurones de la sonde, un facteur commun (1 − ηλ)^t. Pour une activation positivement homogène, elle change les scores et donc un seuil fixe, mais pas l'aire sous la courbe.

**m6. Partie 2 du second théorème.**
Endroit : ligne 61.
- Le momentum la préserve aussi, puisqu'il est linéaire. Adam, lui, la casse : constaté, wᵀ(M − M0) atteint 3e-6 (`verif/v2_jouet.py`). La restriction est donc nécessaire, et il vaut la peine de le dire.
- ν doit être commun à tous les neurones. Le jouet ancre seulement sur les épisodes honnêtes, soit ψ_i = ν c(x)(h_i − h_i⁰)², ce que la preuve couvre mais que l'énoncé n'écrit pas. Énoncer ce cas.

**m7. Partie 3 du second théorème : hypothèses d'intégrabilité cachées.**
Endroit : lignes 66 et 76.

Pour que k_i(·, x′) ∈ L²(𝒟) et k_i ∈ L²(𝒟⊗𝒟), il faut E‖x‖² < ∞ et φ′ bornée (ou à croissance contrôlée). Un neurone ReLU mort donne k_i ≡ 0 et viole l'indépendance linéaire : à dire.

« moved by the filter gradient » (ligne 82) vaut génériquement, ou pour une perte de filtre bien choisie, pas pour toute perte.

**m8. Partie 3 du premier théorème : cas de bord.**
Endroit : lignes 28 à 33.
- ρ* n'est pas défini si s est presque sûrement constant (wᵀΣw = 0) ; la borne est alors triviale. À dire.
- La borne en ½ρ*√χ² dépasse 1 dès que χ² > 4ρ*⁻², et devient alors vide. Ajouter min(1, ·), ou rappeler la borne par la variation totale.
- On peut resserrer la borne en remplaçant ρ*(s, Wh) par ρ*(s, g(Wh)), qui est plus petit par traitement de l'information.

La borne exacte, elle, est atteinte (s = z, g = 1{z ≤ t}, ρ* = 1 : changement = borne ; `verif/v5_borne.py`).

**m9. Sélection et entraînement n'emploient pas la même orthogonalité.**
Endroit : lignes 17 et 61.

Le premier théorème demande WΣw = 0, le second Ww = 0. Une sonde Ww = 0 est invariante sous gradient dans le réseau linéaire, mais pas sous sélection, sauf si Σ ∝ I sur les directions concernées. Le dire en une phrase, sinon « Euclidean orthogonality suffices » se lit comme une garantie générale.

**m10. Champ de la partie 1 du second théorème.**
Endroit : ligne 60.

La preuve tient point par point en x, donc aussi pour des données qui dépendent de la politique ; c'est une force à écrire. La loi de s sur les épisodes, elle, change avec la loi des entrées : retour à M1.

**m11. Forme.**
- `Lancaster (1957)` est en texte libre, ligne 42 : passer à `\cite`.
- Les macros `\E`, `\Cov` et `\Var` doivent exister dans le papier qui reçoit la section.
- `\ref{thm:selection}` (ligne 33) pointe vers le manuscrit du régime statique : vérifier que l'étiquette existera dans le papier D.

**m12. Instrument (classe B).**
- Les quatre gardes de `main()` (lignes 270 à 280 du script) ne sont pas exercées sur un artefact par les tests (règle R5). Les tests vérifient des conditions analogues, mais seule la garde « placement inconnu » est testée en échec.
- Le manifeste du JSON donne le commit `f2dcac18`, antérieur au commit qui introduit le script (`47d484af`). La provenance tient par l'empreinte du script, qui concorde ; ajouter un indicateur d'arbre modifié.
- La figure n'a pas été régénérée, faute de matplotlib dans l'environnement fourni ; seule son empreinte a été vérifiée.

## Ce qui a été vérifié et tient

- **Premier théorème, partie 1.** Équivalence entre invariance pour tout g admissible et indépendance (les indicatrices suffisent) ; cas gaussien par la covariance croisée WΣw.
- **Premier théorème, partie 2.** L'identité de Stein s'applique : g > 0, de classe C¹, E‖∇g‖ < ∞, et Σ peut être singulière. Le signe logistique est juste : ∇ log(1 − σ(u)) = −σ(u)a. Le sens « vers le côté honnête » quand ⟨Wᵀa, w⟩_Σ > 0 est juste. Contrôle exact par quadrature : la formule de Stein et la régression gaussienne coïncident à 1e-10.
- **Premier théorème, partie 3.** ΔE_g[φ] = Cov(φ, g)/E g ; χ² = Var g/(E g)² ; sd(1{s > t}) = √(p(1 − p)) ; facteur 1/2 juste ; borne atteinte. Formule de la corrélation multiple juste. Le lien avec le régime R2 sous l'opérateur A est juste : une sonde à seuil donne exactement le changement de survie à l'audit.
- **Second théorème, partie 1.** Gradient par ligne juste ; récurrence juste ; hypothèse « ancrage stationnaire à l'initialisation » nécessaire et suffisante pour annuler le troisième terme ; mini-lots couverts, car l'annulation a lieu point par point. Adam (ε > 0, moments nuls) : constaté sans mouvement (`verif/v2_jouet.py`).
- **Second théorème, partie 2.** Juste pour une descente de gradient simple (constaté : wᵀ(M − M0) = 2e-17).
- **Second théorème, partie 3.** Formule `eq:ntk-drift` juste : écart relatif de 2e-12 à γ = 1e-3, sur la sonde orthogonale partagée en ReLU. Réciproque juste sous indépendance linéaire et intégrabilité ; réduction au cas linéaire juste.
- **Second théorème, partie 4.** Calcul de d(Ww)/dt juste ; la portée est corrigée en M2.
- **Introduction (ligne 6).** Elle est conforme au théorème 2 (R2) et à la remarque « Placement is not covariance » du manuscrit `main-v4-correctif-1.tex` (lignes 226 à 231 et 257 à 258).
- **Relance de l'expérience.** JSON identique au bit près hors manifeste (numpy 2.5.5 contre 2.5.3) ; 6 tests passés.
- **Chiffres du paragraphe, tous retrouvés dans le JSON.** 4×10⁶ tirages ; d = 32 ; 1500 pas ; lot complet ; tête de texte de dimension 2 ; 0,507 → 0,316 ; 0,78 (0,7765) ; −0,058 ; 0,749 → 0,750 ; 0,708 → 0,657 ; 0,565 → 0,435 ; aire réajustée de 0,832 à 0,856 ; 0,507 → 0,0003 (3,5e-4) ; ‖Ww‖ de 0 à 0,62 (0,6195) ; 4,5e-3 (4,513e-3) ; −0,078 et 5e-4. Seul écart : 1,1 au lieu de 1,2 (m1).
- **Le passage de v1 à v2** porte bien la correction sur le placement : l'introduction et la remarque disent dépendance, pas placement.

## Références à vérifier sur PDF (règle R7 ; aucune n'a été vérifiée ici)

- Lancaster 1957 (corrélation maximale de la loi normale bivariée). L'extension au cas vectoriel, corrélation canonique, est à sourcer : Kolmogorov et Rozanov 1960, ou une autre source.
- Hirschfeld 1935 ; Gebelein 1941 ; Rényi 1959 ; Witsenhausen 1975.
- Stein 1981 (lemme de Stein) ; Pearson 1903, Aitken 1934, Lawley 1943 (sélection sous normalité multivariée).
- Chapman et Robbins 1951 (borne en χ²).
- Jacot, Gabriel et Hongler 2018 (noyau tangent neuronal).
- Cloud et al. 2024 (« Gradient Routing »).
- Bailey et al. 2024 (activations obfusquées) ; Gupta et Jenner 2025 (« RL-Obfuscation ») ; McGuinness et al. 2025 (« Neural Chameleons »), titre et auteurs à confirmer.
- Baker et al. 2025 et Korbak et al. 2025 (déjà cités dans le manuscrit statique).

## Commandes lancées

Dans ces commandes, `S` désigne `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad`.

```
# empreintes (lecture seule)
cd papiers/D && sha256sum -c theorie/*.sha256 code/experience_jouet_*.sha256 code/test_experience_jouet_*.sha256 resultats/decouplage-v1/*.sha256

# copie et relance
cp papiers/D/code/{experience,test_experience}_jouet_decouplage_sonde_v1.py $S/copie/
cd $S/copie && PYTHONDONTWRITEBYTECODE=1 $S/venv/bin/python -I experience_jouet_decouplage_sonde_v1.py --out $S/sortie --no-figures
$S/venv/bin/python -I $S/compare_json.py papiers/D/resultats/decouplage-v1/resultats-decouplage-v1.json $S/sortie/resultats-decouplage-v1.json   # aucun écart
cd $S/copie && PYTHONDONTWRITEBYTECODE=1 python3 -I -m pytest -q -p no:cacheprovider test_experience_jouet_decouplage_sonde_v1.py           # 6 passed

# vérifications propres
$S/venv/bin/python -I $S/verif/v1_selection.py $S/copie <json>   # Stein exact par quadrature, contre-exemple exact, calibrage de l'erreur type
$S/venv/bin/python -I $S/verif/v2_jouet.py $S/copie              # survivants, Bayes 0,8556, optimiseurs, Adam en linéaire, eq:ntk-drift
$S/venv/bin/python -I $S/verif/v3_moniteur_et_signe.py $S/copie  # ‖Ww‖ nul et recrutement ; signe sur 48 tirages
$S/venv/bin/python -I $S/verif/v4_contre_exemple_signe.py $S/copie  # capture parmi survivants 0,519 -> 0,356, sonde disjointe
$S/venv/bin/python -I $S/verif/v5_borne.py                       # borne eq:robust-tpr atteinte
git merge-base --is-ancestor f2dcac18 47d484af                   # provenance du manifeste
```

Scripts de vérification : `S/verif/`. Sorties de la relance : `S/sortie/`.
