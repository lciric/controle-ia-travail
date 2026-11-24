# Contre-lecture du correctif 2 du manuscrit v4 (normalisation de la récompense sous pénalité ; procédures qui réalisent chaque opérateur)

Contre-lecteur neuf. Pièces lues : `manuscrit-arxiv/main-v4-correctif-2.tex` (empreinte b5e96987…, conforme à son `.sha256`), diff avec `main-v4-correctif-1.tex`, note, script et JSON (empreintes conformes). Aucun fichier du dépôt modifié. Le script a été relancé sur une copie (bloc-notes) : mêmes résultats, aucun défaut. Le manuscrit compile (pdflatex, deux passes) sans référence indéfinie.

## Verdict

**Accepté avec corrections.** Les mathématiques annoncées sont justes (translation, condition d'inversion générale, lois des trois réalisations de A, lot écarté). Je n'ai trouvé aucun défaut bloquant. Les défauts sont des ambiguïtés de convention sur C, deux hypothèses implicites non dites dans la remarque sur le lot écarté (dont un cas voisin, le lot rempli par rééchantillonnage, qui ne réalise pas A et pas B au même η), et un script qui teste moins que le texte ne le laisse entendre.

## Défauts

1. **À corriger — deux conventions pour C dans la même section.**
   Emplacement : `main-v4-correctif-2.tex`, sec:reward (ligne 66), puis rem:algos (ligne 102).
   Constat : la phrase « Throughout, C is therefore the gap between the honest task reward and the score of an intercepted trajectory » fixe C comme écart. La phrase suivante, « with an honest reward R0 ≠ 0, every statement on Operator B holds with C replaced by R0 + C », prend C pour l'opposé brut du score d'interception (C_brut = −score). Si C est déjà l'écart, remplacer C par R0 + C compte R0 deux fois. Même mélange dans rem:algos : « C = 0 under the normalization, and C = R0 otherwise » est une convention d'écart (le score brut vaut 0, donc l'écart vaut R0), alors que « Operator B at C = −b » est une convention brute (l'écart vaut R0 − b si R0 ≠ 0). Sous la normalisation R_h = 0 tout coïncide, mais le texte parle justement du cas R0 ≠ 0.
   Correction : nommer les deux objets. Par exemple : « Let s_int = −C_raw be the score of an intercepted trajectory and R0 the honest reward; the quantity that enters is the gap C_gap = R0 + C_raw, which equals C under the normalization R0 = 0. » Écrire ensuite la condition avec C_raw ou C_gap, et dire dans rem:algos de quelle convention relèvent « C = R0 » (écart) et « C = −b » (brut ; écart R0 − b).

2. **À corriger — remarque rem:algos, cas du lot écarté : hypothèses implicites, et variante par rééchantillonnage non traitée.**
   Emplacement : ligne 102, « So does simply discarding them from an on-policy batch… ».
   Constat, en trois points.
   (a) Le gradient attendu ∇E_π[βR] est exact pour la partie récompense. Le terme de régularisation doit en outre porter sur toute la politique (calcul exact, ou sur tout le lot). Si la pénalité KL est ajoutée à la récompense de chaque échantillon puis écartée avec lui, la partie KL est pondérée par β et l'objectif n'est plus de forme Gibbs vers π0. Le script suppose le KL exact sur toute la politique et ne le dit pas.
   (b) Le texte précise « normalized by the full batch size », ce qui est juste, mais le rééchantillonnage, que l'abstract et l'opérateur A nomment « discard and try again », donne autre chose. Si l'on remplit le lot de survivants (normalisation par le nombre de survivants), le champ de gradient de la récompense devient ∇E[βR]/E_π[β]. Vérifié numériquement (point p = (0,85 ; 0,14 ; 0,01), β = (0,9 ; 0,2 ; 0,6), η = 1,5, ΔR = 1, montée de gradient exacte avec KL exact) : le point fixe est π ∝ p·exp(η·βR/E_π[β]), c'est-à-dire B à C = 0 mais à une pression effective η/E_{π*}[β], auto-cohérente. Ce n'est ni A (écart de 0,054 sur la strate honnête) ni B à C = 0 au même η (écart de 0,02). Le texte « belongs to Operator B, not A » reste vrai à une réserve près : B à un autre η.
   (c) La proposition prop:limits parle déjà de « zero-penalty halting without resampling (C = 0 in Operator B) ». La remarque devrait s'y raccorder et dire que le lot écarté sans rééchantillonnage en est la réalisation.
   Correction : ajouter « (with the KL term evaluated on the whole policy, not on retained samples only) » et une phrase : « If the batch is instead refilled with survivors, i.e. normalized by their number, the reward gradient is rescaled by 1/E_π[β]; in the model this gives Operator B at C = 0 with a self-consistent pressure η/E_π[β] (checked numerically on one example; not claimed in general), still not Operator A. » À défaut, restreindre l'énoncé aux « batches normalized by the full batch size, the KL term being exact ».

3. **À corriger — domaine C ≥ 0 de l'opérateur B.**
   Emplacement : lignes 66 et 102 ; définition de l'opérateur B et théorème (C ≥ 0 partout, partie 1 qui utilise ΔR + C > 0, « negative penalty » en 4(b)).
   Constat : « C = −b » avec b > 0 (ligne de base usuelle = récompense moyenne) donne C < 0, hors du domaine de l'opérateur B tel que défini. La forme de Gibbs reste valable, mais les énoncés du théorème qui supposent C ≥ 0 ne s'y appliquent pas tels quels. De même, « C remplacé par R0 + C » peut sortir du domaine si R0 < 0 et que l'on lit l'écart.
   Correction : écrire « (C may be negative here; the Gibbs form still holds, but statements of Theorem 1 that assume C ≥ 0, resp. ΔR + C > 0, apply to the gap only when it is non-negative, resp. positive) ».

4. **Mineur — réalisation du filtrage itéré : « fine-tune on the survivors ».**
   Emplacement : ligne 104.
   Constat : l'affinage supervisé sur les survivants donne π_{t+1} ∝ β π_t, donc π_T ∝ β^T π0 sans terme de récompense (vérifié : trois tours exacts = β³ p). Le π_T de rem:modelA contient e^{Tη1R}, c'est-à-dire un pas d'apprentissage par renforcement régularisé par rapport à la politique courante à chaque tour. L'énoncé est exact seulement si l'étape est un pas régularisé vers la politique courante, ce qui est aussi le point qui sépare π_T de A (ancrage sur la politique courante à chaque tour contre ancrage unique sur π0).
   Correction : « Iterating "filter on-policy samples, then take a KL-regularized reinforcement-learning step relative to the current policy" realizes π_T (supervised fine-tuning on survivors alone gives β^T π0, the case η1 = 0)… ».

5. **Mineur — « Both operators are exact optima of KL-regularized objectives with reference π0 ».**
   Emplacement : ligne 101, première phrase de rem:algos.
   Constat : pour A, c'est vrai seulement avec le bonus η⁻¹ log β (rem:modelA) ; la définition prend π0^acc comme référence, et la réalisation (ii) utilise cette référence filtrée, pas π0.
   Correction : « Operator B is the optimum relative to π0; Operator A is the optimum relative to π0^acc, equivalently relative to π0 once the bonus η⁻¹ log β is added ».

6. **Mineur — conditions des trois réalisations de A.**
   Emplacement : ligne 103.
   Constat : (i) suppose que la décision du moniteur est une épreuve de probabilité β indépendante à chaque tentative, ou que β est la fraction d'acceptation homogène par strate. (ii) « fitting the reference on monitor-accepted samples » n'est exact qu'à l'idéal (conditionnement). (iii) exige β > 0 ; or le modèle autorise β_v = 0 (hypothèses du théorème, prop:limits partie 2), cas où la récompense corrigée vaut −∞ : c'est une contrainte de support, non une récompense. Le texte du correctif écrit déjà « β(π) > 0 » mais ne relie pas ce point au cas β_v = 0.
   Correction : une demi-phrase : « (iii) requires β > 0; for β_v = 0 it degenerates into a support constraint (reward −∞ on Π_v) ».

7. **Mineur — script : ce qui est réellement testé.**
   Emplacement : `verifier_correctif_2_v1.py` ; phrase de la ligne 105 du manuscrit.
   Constat :
   - Les tests 2 et 3 sont faits en un seul point de paramètres (p, β, η, ΔR, C).
   - Le test 3 écrit le score effectif β_i(R_i − b) à la main : la revendication « le gradient attendu du lot écarté vaut ∇E[βR] » est posée, non vérifiée. Aucune énumération des événements accepté/intercepté. Aucune normalisation par les survivants (défaut 2b) ni KL sur survivants (défaut 2a). J'ai vérifié par échantillonnage (2·10⁶ tirages) que l'estimateur à normalisation par la taille totale a bien pour espérance π_i(β_i(R_i − b) − moyenne) : le texte est juste, mais le script ne le montre pas.
   - Le test 4 réutilise les formes closes de A et B (même formule que dans le texte), avec ΔR_v = ΔR_f. La grille n'a aucun point près du seuil (marge minimale |condition| = 0,021 ; 107 cas vrais, 181 faux, donc les deux signes sont bien couverts). Il ne teste pas ΔR_f ≠ ΔR_v ni C < 0. Le calcul est donc surtout une vérification algébrique, ce qui est légitime mais moins fort que « against direct computation ».
   - Les réalisations (i), (ii) et le filtrage itéré (d) ne sont pas testés par le script ; le texte ne le prétend pas (il cite « (iii) » et le lot écarté), ce qui est honnête.
   - Tolérances : 1e-12 (translation), 1e-9 (optimiseurs), contre des écarts observés de 1e-15 : saines. Le test négatif (translation naïve détectée, écart à A de 0,041) est bien posé.
   - « 288 parameter points » est écrit en dur dans le manuscrit : si la grille change, le texte devient faux.
   Correction : ajouter au script des points à ±1e-6 du seuil et un tirage ΔR_f ≠ ΔR_v, C ∈ [−2, 4] (mon propre fuzz de 200 000 tirages avec ces degrés de liberté n'a donné aucun désaccord) ; énumérer ou simuler l'événement d'interception pour le test 3 ; et écrire dans le texte « on a grid of parameter points » plutôt qu'un nombre en dur, ou citer le JSON.

8. **Mineur — porter.** La note dit que le billet et la page de dépôt ne sont pas retouchés. Cela reste cohérent, mais leur condition d'inversion n'a plus la normalisation (valable sous R0 = 0 seulement). À reporter si ces pièces doivent circuler avec le correctif 2 ; hors périmètre de la pièce contre-lue.

## Ce qui a été vérifié et tient

1. **Translation (point 1 de la mission).** β(R + R0) − (1−β)C = βR − (1−β)(C + R0) + R0 : exact (développement à la main). Donc à score d'interception −C fixé, translater R de R0 revient sous B à C → C + R0, le terme R0 constant disparaissant dans la normalisation. A (∝ β e^{ηR}) et π_no (∝ e^{ηR}) multiplient leurs poids par e^{ηR0} : invariants. Soustraire une constante à tous les scores, interceptés compris, ajoute une constante à l'exposant de B : sans effet. Le script confirme (écarts de 1e-16 ; translation naïve à C inchangé : 0,03 à 0,09).
2. **Condition d'inversion (point 2).** En niche parfaite (β_f = β_h = 1 > β_v > 0), π_A(f) et π_B(f) ont le même numérateur p_f e^{η(R0+ΔR_f)} ; π_B(f) > π_A(f) équivaut à Z_B < Z_A, soit à un poids visible plus petit sous B : exp(η[β_v(R0+ΔR_v) − (1−β_v)C]) < β_v e^{η(R0+ΔR_v)}, ce qui donne η(1−β_v)(R0+ΔR_v+C) > log(1/β_v). L'équivalence est exacte, sans hypothèse de signe : si R0+ΔR+C ≤ 0, le membre de gauche est ≤ 0 < log(1/β_v), et la condition échoue d'elle-même (la « condition de sens » R0+ΔR+C > 0 est donc implicite et automatique). Cohérence avec eq:inversion : pour R0 = 0, diviser par 1−β_v > 0 redonne η(ΔR+C) > log(1/β_v)/(1−β_v). Fuzz indépendant de 200 000 tirages (p de Dirichlet, R0 ∈ [−3, 3], ΔR_v ≠ ΔR_f, C ∈ [−2, 4]) : zéro désaccord ; la condition ne fait intervenir que ΔR_v (la furtive se simplifie), ce qui est compatible avec l'hypothèse ΔR_v = ΔR_f du théorème. Cas limites : β_v = 0 (condition jamais vraie, cohérent avec prop:limits partie 2) ; β_v = 1 (égalité des lois) ; tous deux hors du domaine 0 < β_v < 1. L'équivalence ne casse nulle part dans le domaine.
3. **rem:algos (point 3), ce qui est juste :**
   - (a) Masquer la récompense des interceptés : score 0, donc C_brut = 0, C_écart = R0 ; signe et convention justes sous la réserve du défaut 1.
   - (b) Lot écarté, normalisé par la taille totale, sans ligne de base : espérance ∇E_π[βR] (vérifiée par tirage) ; B à C = 0 ; avec ligne de base constante b retranchée aux seuls retenus, E[β(R−b)] = E[βR] − bE[β], et B à C brut vaut E[βR] + C·E[β] − C : donc C = −b (signe correct). La ligne de base doit être une constante (une moyenne du lot ne l'est qu'asymptotiquement).
   - (c) Réalisations de A : (i) π_no × β ∝ β e^{ηR} π0 ; (ii) π0^acc ∝ β π0, puis e^{ηR} : même loi ; (iii) optimum de R + η⁻¹ log β avec KL vers π0 : même loi (cohérent avec rem:modelA). Le script confirme (iii) à 7e-15.
   - (d) Le filtrage itéré réalise π_T de rem:modelA (réserve du défaut 4) et non A : correct.
4. **Remarque de régularisation à π0.** Le correctif dit « relative to π0 » pour B et les réalisations de A ; la nuance « politique courante » n'apparaît que pour π_T. Voir défauts 4 et 5.
5. **LaTeX (point 5).** Références `sec:reward`, `eq:inversion`, `rem:modelA`, `rem:algos`, `thm:selection` toutes résolues ; label placé sur la sous-section ; le diff ne montre que trois changements (notice d'auteur, paragraphe de la sous-section, nouvelle remarque ; le `\end{remark}` ajouté est un artefact du diff). Rien d'autre n'est modifié. Anglais clair ; « corrective 2 » cohérent avec le titre du fichier.
6. **Empreintes.** Les `.sha256` compagnons du script, du JSON, de la note, du .tex et du .pdf correspondent aux fichiers ; le `script_sha256` du JSON égale celui du script du dépôt.
