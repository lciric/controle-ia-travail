# Vérification : la v3 de la section sur le découplage géométrique porte-t-elle fidèlement la contre-lecture ?

Vérificateur : le contre-lecteur de la v2 (Opus 5.5). Date : 24 novembre 2026. Branche `papier-d/evasion-post-entrainement-v1`, commit `9b5581cb`.
Pièces lues : `papiers/D/theorie/decouplage-geometrique-v3.tex` et `decouplage-geometrique-v3-references.md`, empreintes vérifiées ; comparées à la v2 et au rapport versé sous `papiers/D/audits/contre-lecture-decouplage-geometrique-v1/`.
Contrôles de provenance : le rapport versé est identique à l'original au bit près. Les cinq scripts de `verif/` le sont aussi, empreintes concordantes.
Aucun fichier du dépôt n'a été modifié. La compilation s'est faite sur une copie, dans le bloc-notes.

## Verdict : **corrige fidèlement, avec réserves**

Les quatre défauts majeurs sont portés :
- M1, M2 et M4 sont corrigés ;
- M3 l'est en grande partie : les citations sont ajoutées sans chiffre, mais trois attributions sont à adoucir et il n'existe pas encore de fichier bibliographique.

Les mineurs m1 à m11 sont tous portés. Les chiffres que la v3 reprend de mon rapport sont justes, à quatre exceptions près :
- les « 48 tirages » sont attribués au réseau du papier, ce qui est faux (défaut 1) ;
- le 3e-6 est présenté sans ses conditions (défaut 6) ;
- la phrase sur l'aire réajustée en ReLU est inexacte (défaut 4) ; l'erreur vient de ma propre formulation ;
- l'exemple de la décroissance pure est trop général (défaut 7).

Il y a une affirmation mathématique nouvelle fausse : l'orthogonalité dans la métrique Σ et l'orthogonalité euclidienne ne coïncideraient « que si Σ est proportionnelle à l'identité » (défaut 2).

La section compile avec l'emballage minimal. Les seuls avertissements sont les quatorze citations non définies, faute de fichier `.bib`.

## Les défauts majeurs de la contre-lecture

| Défaut | État | Lignes de la v3 |
|---|---|---|
| **M1** : instrument inchangé, audit parmi les survivants non garanti | **Corrigé** | 15 (rôles des deux théorèmes), 71 (portée de la partie 1), 94 à 96 (remarque nouvelle et contre-exemple), 99 (deuxième point) |
| **M2** : surveiller ‖W_{:,S}‖, pas ‖Ww‖ | **Corrigé** | 78 (partie 4 énoncée avec W_{:,S}, moment croisé non centré), 91 (preuve), 99 (troisième point). Réserve : défaut 8 |
| **M3** : antériorité et citations | **Corrigé en grande partie** | 15 (aucune nouveauté revendiquée pour les outils), 37, 42, 46, 77, 82, 99 ; fichier des références. Réserves : défauts 3, 5 et 12 |
| **M4** : constats qui découlent de la construction | **Corrigé** | 102 (épisodes = entrées fixes), 104 (« check of the code, not a test that could have failed »), 107 (aire de Bayes 0,8556). Réserve : défaut 4 |

## Les mineurs de la contre-lecture

| Mineur | État | Lignes de la v3 |
|---|---|---|
| m1 : arrondi et erreur type | porté | 102 (1,2 ; erreur type grossière déclarée ; quadrature à 1e-10) |
| m2 : contre-exemple exact | porté | 57 (−0,0775 exact ; h = (x, x² − 1), Σ = diag(1, 2)) |
| m3 : formulations du paragraphe numérique | porté | 105 (« shift of the mean cheater score », « moved but not evaded ») |
| m4 : classe d'optimiseurs | porté | 66 (ε > 0, état nul, écrêtage global, rapports par couche, préconditionneurs pleins exclus) ; voir défaut 7 |
| m5 : décroissance des poids | porté | 64 et 66 (terme r_i, ∇r_i(m_i(0)) = 0), 85 (preuve) ; voir défaut 7 |
| m6 : partie 2 | porté | 72 (momentum, c(x) commun, Adam casse l'invariance) ; voir défaut 6 |
| m7 : intégrabilité, neurone mort, « generic » | porté | 73, 77, 89, 99 |
| m8 : cas de bord de la partie 3 | porté | 37 (Var s > 0), 40 (min{1, ·}), 42 et 53 (version resserrée par ρ*(s, g(Wh))) |
| m9 : deux orthogonalités | porté, mais avec une affirmation fausse | 46 ; voir défaut 2 |
| m10 : la partie 1 tient point par point en x | porté | 71 et 85 |
| m11 : forme | porté | `\cite{lancaster1957}` ; macros et `thm:selection` signalés en en-tête (ligne 8) |

Le mineur m12 portait sur le code (gardes non testées, commit du manifeste). Il est hors de la section et n'est pas traité ; rien d'anormal.

## Chiffres repris : contrôle un par un

Les chiffres justes, avec la valeur source :

| Chiffre de la v3 | Valeur source |
|---|---|
| 0,519 → 0,356 et 0,185 → 0,492 | `v4_contre_exemple_signe.py`, ReLU |
| 0,691 | 0,6914 |
| 0,359 → 0,415 | `v2_jouet.py`, ReLU, sonde disjointe |
| 5e-16 et 3,06 | 5,33e-16 et 3,0557 |
| 3,4e-3 | 3,362e-3 |
| −0,0775 | −0,077474 |
| 1,2 | 1,18 |
| 1,8e-15 | 1,776e-15 dans le JSON |
| 0,8556 | Φ(1,5/√2) = 0,85558 |

Les quatre exceptions :
- « 48 tirages » : bon nombre, mauvaise description (défaut 1).
- 3e-6 : bonne valeur, conditions omises (défaut 6).
- « the same holds almost exactly in the ReLU network » : inexact (défaut 4).
- « initial momentum of 10⁻³ » : c'était un premier moment d'Adam (défaut 7).

## Défauts relevés dans la v3

**1. Majeur : les « 48 tirages » sont mal décrits.**
Endroit : ligne 95, « On the companion network … did not decrease in any of 48 random draws ».

Ces tirages n'ont pas été faits sur le réseau du papier. Ce sont 12 graines × 2 tâches × 2 activations (`v3_moniteur_et_signe.py`) :
- deux tâches : la recette du papier et une variante où les tricheurs sont déplacés sur deux directions ;
- n = 2000 par classe, 600 pas d'entraînement ;
- « baisse » signifie une baisse de plus de 1e-3.

Le chiffre ne renvoie donc pas à ce qu'il décrit (règle R6).

Correction : « on the companion network the same quantity moves favourably (0.359 → 0.415, disjoint ReLU probe); in 48 further runs (12 seeds, the companion task and a two-direction variant, linear and ReLU, 600 steps) it never decreased by more than 10⁻³ ».

**2. Majeur : affirmation mathématique fausse.**
Endroit : ligne 46, « the two coincide only when Σ is proportional to the identity on the relevant directions ».

Les deux conditions WΣw = 0 et Ww = 0 sont équivalentes pour tout w dès que l'espace des lignes de W est invariant par Σ. C'est le cas, par exemple, quand Σ est diagonale par blocs adaptés à ker W, sans être proportionnelle à l'identité. Contre-exemple exact : Σ = diag(1, 2, 3) et W = e₁ ; l'équivalence tient pour tout w (vérifié en arithmétique exacte, `verif_v3_sigma.py` dans mon bloc-notes).

Correction : « the two coincide for every w when the row space of W is invariant under Σ (e.g. Σ ∝ I), and differ in general ».

**3. Mineur : attributions à adoucir.**

(a) Ligne 46, « Parts 1 and 2 are the classical selection formulas … ». La partie 1, hors du cas gaussien, est un fait élémentaire sur les indicatrices et non la formule de Pearson et Lawley. La partie 2 est une réécriture par l'identité de Stein d'une conséquence de cette formule.
Proposer : « Part 2 and the Gaussian case of Part 1 follow from the classical selection formulas … ».

(b) Lignes 15 et 82, « gradient masking ». En apprentissage antagoniste, ce terme désigne l'obfuscation des gradients, une autre notion : il prête à confusion.
Proposer : « masking of gradients, as in gradient routing [cloud2024] ».

(c) Ligne 99, « studies the same phenomenon in real models ». Ces travaux étudient l'évasion de moniteurs latents qu'on optimise contre eux, ou leur généralisation à d'autres sondes. Ce n'est pas exactement le cadre ici : filtre sur la tête de texte, sonde d'audit hors de la boucle.
Proposer : « studies related phenomena (evasion of latent-space monitors under optimization) ».

Aucune citation ne porte de chiffre : conforme à la demande.

**4. Mineur, venu de mon propre rapport : l'aire réajustée en ReLU.**
Endroit : ligne 107, « the same holds almost exactly in the ReLU network ».

En ReLU, l'aire réajustée vaut 0,832 avant et 0,833 à 0,835 après. C'est nettement sous la valeur de Bayes, 0,856 : la phrase est inexacte. Ma formulation, « presque en ReLU », était lâche ; je la corrige ici.

Proposer : « in the ReLU network the re-fitted area stays at its initial value (0.832 → 0.833–0.835), below the Bayes value, because the map h = ReLU(Mx) with d = 2p loses little information during training ».

Ajouter aussi « generically » à « h = Mx stays injective » (il faut que M reste de rang p).

**5. Mineur : le fichier bibliographique manque.**
Les quatorze clés sont citées, mais aucun `.bib` n'existe : la compilation laisse les quatorze citations non définies. Le fichier des références le dit lui-même : aucune n'a été vérifiée sur PDF ; pour `bailey2024`, seules les métadonnées ont été lues (règle R7). À faire avant toute diffusion. Rien à corriger dans le texte.

**6. Mineur : le chiffre de 3e-6 sans ses conditions.**
Endroit : ligne 72, « a drift … of order 3 × 10⁻⁶ is observed on the companion network ».

Ce chiffre vient de 200 pas d'Adam, avec un taux d'apprentissage de 1e-3, sur la sonde orthogonale partagée linéaire (`v2_jouet.py`). Ce n'est pas l'entraînement du papier : 1500 pas de descente de gradient, taux de 0,5.

Préciser les conditions, ou sortir ce chiffre de l'énoncé du théorème vers une note.

**7. Mineur : exemples de la classe d'optimiseurs.**
Endroit : ligne 66.

(a) « an initial momentum of 10⁻³ » : le test portait sur un premier moment d'Adam initial de 1e-3, qui donne une dérive de 7e-7. Écrire « a non-zero initial Adam first moment (10⁻³) ».

(b) « A pure decoupled decay multiplies the probe's rows by a common factor » : c'est vrai seulement sans ancrage d'activation sur ces neurones. Avec ψ_i = ν c(x)(h_i − h_i⁰)², la décroissance éloigne h_i de h_i⁰, l'ancrage produit un gradient, et ce n'est plus une simple homothétie : l'aire sous la courbe a bougé de 0,811592 à 0,811563 dans mon essai. Ajouter « absent activation anchoring on the probe's neurons, and with 1 − ηλ > 0 ».

**8. Mineur : la phrase « a probe supported on S and orthogonal to the rows of W(t)_{:,S} has W(t)w = 0 ».**
Endroit : ligne 91 ; chiffres en ligne 78.

La phrase est juste. Elle demande deux précisions :
- un tel w ≠ 0 n'existe que si |S| > rang de W(t)_{:,S} (ici 12 > 2) ;
- l'orthogonalité vaut à l'instant t seulement.

En ligne 78, « one can have » cache que la sonde a été choisie après coup, orthogonale à W(T)_{:,S}. Comme ni W ni M ne dépendent de w, cela reste légitime, mais il faut l'écrire : « for a probe chosen orthogonal to the rows of W(T)_{:,S} ».

**9. Mineur : le paragraphe numérique reste incohérent avec la nouvelle partie 4.**
Endroit : ligne 108.

Il ne rapporte que ‖Ww‖ de 0 à 0,62, la quantité que la v3 déclare insuffisante. Ajouter ‖W_{:,S}‖ de 0 à 3,06 (même valeur pour la sonde du papier, puisque W ne dépend pas de w ; `v2_jouet.py`). La figure trace aussi ‖Ww‖ : à signaler pour sa prochaine version.

**10. Mineur : la borne « attained ».**
Endroit : ligne 46.

Seule la première inégalité de `eq:robust-tpr` est atteinte. La seconde, en ½, ne l'est que pour P(s > t) = 1/2.

Écrire : « the first inequality in~\eqref{eq:robust-tpr} is attained ».

**11. Mineur : précisions de la remarque nouvelle.**
Endroit : ligne 95.

(a) « The quantity of the static regime (R2) is audit survival among the cheating episodes that survive the filter » vaut sous l'opérateur A. Sous l'opérateur B, la loi après entraînement est une inclinaison exponentielle, pas une pondération par la survie. Ajouter « under Operator A ».

(b) « one seen only by the filter and one only by the probe » force le trait. Dans `v4_contre_exemple_signe.py`, les neurones du filtre lisent aussi x₁ et ceux de la sonde aussi x₀. Écrire « mostly ».

(c) Le seuil de l'audit, au 95e centile des scores honnêtes avant entraînement, n'est pas dit. L'ajouter, avec le renvoi au script.

**12. Mineur : provenance incohérente entre l'en-tête et le mode d'emploi.**
Endroit : lignes 10 et 11 de l'en-tête.

L'en-tête range `v2_jouet.py` parmi les scripts « replayed by the daughter session ». Or `LISEZMOI-contre-lecture-decouplage-v1.md` dit qu'il n'a pas été rejoué, alors que la v3 en tire 0,359 → 0,415, 3e-6 et 10⁻³.

Le chiffre est juste : je l'ai obtenu avec ce script, identique au bit près à la version versée. Mais il faut aligner les deux pièces, ou rejouer `v2_jouet.py`.

## Ce qui tient

- **Preuves.** Les modifications des preuves sont justes :
  - terme ∇r_i(m_i) (ligne 85) ;
  - état d'optimiseur nul ;
  - c(x) dans la partie 2 (ligne 87) ;
  - restriction de la partie 4 aux colonnes de S (ligne 91) ;
  - version resserrée par ρ*(s, g(Wh)) (ligne 53) ;
  - min{1, ·}.
- **Classe d'optimiseurs élargie** (ligne 66). L'écrêtage par la norme globale et les rapports de confiance par couche satisfont bien la définition nouvelle, une mise à jour qui s'annule quand les gradients de m_i sont nuls. Les préconditionneurs pleins en sont bien exclus.
- **Partie 4 avec W_{:,S}.** L'énoncé est juste.
- **Pas de survente nouvelle.** Hors des défauts 1 à 3, la v3 ne survend pas. Elle réduit même la portée là où il le fallait : lignes 15, 71, 99 et 102 à 107, avec en ligne 99 « exact statements only in a toy architecture ».

## Commandes lancées

```
cd papiers/D/theorie && sha256sum -c decouplage-geometrique-v3*.sha256
cd papiers/D/audits/contre-lecture-decouplage-geometrique-v1/verif && sha256sum -c *.sha256 ; cmp avec mes copies (identiques)
cmp ../contre-lecture-decouplage-geometrique-v1.md <ma copie>   # identique
# compilation sur copie : emballage minimal (amsmath, amsthm, \E, \Var, \Cov, thm:selection factice), pdflatex deux passes
$S/venv/bin/python -I $S/verif_v3_sigma.py   # contre-exemple du défaut 2
```
Ici, `S` = `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad`. Les autres chiffres ont été contrôlés sur les sorties de mes exécutions de la contre-lecture, obtenues avec des scripts identiques au bit près à ceux versés.
