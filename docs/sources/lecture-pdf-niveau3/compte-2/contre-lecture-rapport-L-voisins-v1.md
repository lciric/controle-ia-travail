# Contre-lecture du rapport « L — deux voisins versés » (Ker ; Bash, Goeckel et Towsley) — v1

- Début du travail : 2026-11-14 06:44:52 UTC (heure de création du dossier de travail, relevée par `date -u -r`) ; ce fichier est écrit le 2026-11-14 06:52:14 UTC (relevée par `date -u` dans la commande qui l'écrit).
- Rôle : contre-lecteur, modèle B. L'auteur du rapport contre-lu est le modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- Consigne : `docs/sources/lecture-pdf-niveau3/compte-2/consignes-compte-2-v1/consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5` (vérifiée, lue en entier).
- Objet : `rapport-L-voisins-v1.md`, sha256 `cb5829539e3fba66e6916aebe79fa1a8a4e3bd320d2754311581fdf43ca2fbde` (vérifiée) ; archive du lecteur `fichiers-de-travail-L-voisins-v1.tar`, sha256 `ee87065d282c8b43d7329e356ac7d71f894aa3b48928dd5f6d7e6f210ec17023` (vérifiée), extraite dans mon dossier de travail.
- Pièces (empreinte vérifiée contre le compagnon `.sha256`, égalité) :
  - `ker-2006-batch-steganography-pooled-steganalysis.pdf` (17 pages) : `a6ab71a257034976636aad130fb9a7715a45d3dd06cb69cf046475f8f231a2aa`
  - `1202.6423v4.pdf` (27 pages) : `ab6caeadb380ec322fb6d9400cde5aa04d6e32ddbb55a869c7efd6f3eebd1c49`
  - lot 8, pour deux renvois bibliographiques seulement : `1906.08938v2.pdf` p. 15 (`3fbaedd9705420fff23cbadb9c7d3de2240c2714c23440cbf133718534194ea9`), `2605.16140v1.pdf` p. 34 (`1f70a3284a2eca0b62cded4dd43e6f88cc6930e3275349a17bee76850860a72a`).
- Citations contrôlées par mon programme (`controle_citations_contre_lecture_v1.py`, écrit par moi, distinct de celui du lecteur) : **44 citations, 0 échec**, dans `citations-contre-lecture-L-voisins-v1.json` (archive). Essai préalable : un cas juste accepté, deux cas altérés refusés (un mot changé ; bonne phrase, mauvaise page).
- Relecture indépendante du JSON du lecteur (`fc9b1e45…`) par mon programme : **67 citations, 0 échec**. Aucun extrait anglais du rapport du lecteur n'est hors de son JSON (contrôle par programme : 94 extraits entre guillemets, les 23 hors JSON sont tous français).
- Convention : tout extrait anglais entre « » est une citation contrôlée, suivie de [Cn] (numéro dans mon JSON). Les formules sont marquées « lu sur le PDF, non contrôlé par programme ». Nature des chiffres : « auteurs », « figure », « calcul ».

## Fichiers lus et étendue

1. La consigne commune, en entier.
2. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 53 à 77 ; `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 85.
3. `rapport-L-voisins-v1.md`, en entier ; `rapport-L-lot8-v2.md` (`8d9f2654f904454a7729f9f133bfd73a4ace916865a4efac7b90f5dba816bdc5`, vérifiée) : titres de sections (repérés par motif dans ce seul fichier), puis lignes 41 à 70 (occupations) et 179 à 262 (table, verdict, reste revendicable, phrase publique, voisins).
4. Ker : les 17 pages, texte extrait par `pdftotext -layout`, lues ligne à ligne, annexe comprise ; aux p. 13 et 14, graduations d'axes filtrées ; p. 13 (figure 4) vue en image.
5. Bash et collègues : les 27 pages, lues ligne à ligne ; à la p. 23 (dérivées de l'annexe A), seules les phrases ont été lues, les formules parcourues.
6. Recherche active par mots dans les textes extraits des deux PDF (dossier de travail seulement) : maximum, séquentiel, martingale, rupture, arrêt, Wald, dépendance, Markov, seuil, adaptatif, compensation, retard, ordre, total, réseau.
7. Lot 8 : aucune page lue à l'œil ; seulement le contrôle par programme des citations R1 à R7 du lecteur et de mes [C43], [C44].
8. Archive du lecteur : script, JSON, journaux. `ls` du seul dossier `compte-2/` (ni mon rapport ni mon archive n'existaient) ; `ls` des dossiers de pièces.

Non ouvert : les « interdits communs v2 » que la consigne nomme dans la méthode du lecteur. Mon mandat ne les nomme pas et borne mes lectures aux fichiers nommés ; j'ai tenu les interdits de la consigne et du mandat. Aucune ouverture fautive. Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucune suppression. Aucun refus.

## 1. Verdict

- **Sur le rapport : tient avec corrections.** La collision qu'il signale est réelle et doit remonter au directeur. Elle est mal comptée et, à deux endroits, mal attribuée : il y a **une** occupation partielle d'une composante revendiquée (l'invariance de L1, par Ker), pas deux ; et Bash et collègues n'occupent rien de L, même en partie.
- **Sur L (table fermée) : occupé en partie.** Pour la première fois, l'occupation touche une composante revendiquée : le cœur de L1.
- Constats : 6 majeurs (A à F), 6 mineurs (G à L), aucun bloquant.

## 2. Point 1 — L1 chez Ker

**Ce que Ker établit, relu sur les pages.**
- Modèle : pur décalage du score par objet (« the distribution of the detector response only depends on p in the form of a shift, so that the (additive) estimation error is independent of the true value. » [C3], p. 3). Charge totale fixée (« We also assume that the Steganographer wants to embed a fixed total amount of secret data » [C7], p. 4), répartie sur rN objets à la proportion p chacun, avec r·p = B (lu sur le PDF, non contrôlé par programme). Objets de même capacité (« all cover objects have the same capacity » [C5]), choisis au hasard (« the Steganographer has no control over the objects themselves, and chooses which to embed in at random. » [C6]).
- L'énoncé, p. 7, tient en une phrase, donnée sans preuve comme évidente : « It is immediate that » [C11] l'espérance vaut r·p, et « given the shift hypothesis, the distributional shape of » [C12] la moyenne « does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B. » [C13].
- Il est repris deux fois p. 14 : « Also, the average method cannot punish the Steganographer for using a suboptimal embedding strategy. » [C21] ; « Because performance of the average detector does not depend on r, we can pick only a single value of r and plot the false positive rate as N varies. » [C22].
- Portée exacte : toute loi ψ des scores (aucun théorème central limite pour l'invariance) ; N fini (avec exactement rN objets chargés, comme dans l'annexe : « and all are independent. » [C28], p. 17, la somme vaut la somme honnête plus N·B, trajectoire par trajectoire — calcul, le même que celui du lecteur, que je confirme) ; égalité **en loi** seulement dans le texte ; famille de répartitions à **deux valeurs** (0 ou p, la même pour tous les objets chargés) ; choix **non adaptatif** ; **aucun ordre temporel** ; un détecteur par objet fixé, des objets indépendants (hypothèse du lemme 1 : « Suppose that all Xi are independent and identically distributed » [C14]).
- La statistique moyenne de Ker est bien la statistique somme de L1 à un facteur 1/N près, et le budget de Ker est bien linéaire sur le décalage de la moyenne (le score estime la proportion chargée). Le budget total de L vaut N fois le B de Ker (constat D).

**Ce qui manque par rapport à L1.** Les valeurs inégales (« In future work we should consider allowing the Steganographer to vary the amount of data embedded in each object (this results in a larger mixture) » [C26], p. 15) ; la répartition adaptative ; l'énoncé trajectoriel écrit ; la fonction de puissance exacte à n fini (loi nulle ajustée ou asymptotique) ; toute lecture séquentielle (« This suggests the study of sequential embedding and tests. We reserve this topic for future work » [C9], p. 5).

**« Occupée en partie » : juste.** Ni trop fort ni trop faible, mais à lire durement dans les deux sens :
- *Pas « occupée »* : la lettre de L1 (toute répartition, valeurs inégales, adaptatif, trajectoriel) n'est pas chez Ker, qui renvoie lui-même les valeurs inégales à plus tard.
- *Pas « voisin »* : l'idée même de L1 — sous pur décalage et budget linéaire fixé, la loi de la statistique somme ne dépend pas de la répartition, donc l'attaquant n'a aucune raison de préférer une répartition — est imprimée, pour un attaquant qui répartit une charge cachée face à un détecteur qui agrège. Ce qui reste (valeurs inégales, adaptatif, trajectoire) est la linéarité de la somme : une ligne. **Le résidu ne peut pas porter une revendication d'originalité** (constat F).
- L'ordre dans le temps n'ajoute rien à L1 : la somme terminale est commutative. Le calendrier ne compte que pour L3.

## 3. Point 2 — L4 chez Ker

L4 (note v2, lignes 79-81) : pour une règle qui ne lit que les sommes aux frontières de pas, la répartition entre agents au même pas est invariante, y compris en lecture toujours valide. Son contenu propre, au-delà de L1, tient à trois choses : plusieurs pas, une lecture aux frontières, une garantie toujours valide.

Chez Ker il n'y a ni agents, ni pas, ni temps : N objets indépendants, un seul test à la fin (« we believe that the practice of sequential steganography and steganalysis may be rather different from the fixed-size batch problems studied here. » [C10], p. 5). Lire « N objets en même temps » comme « N agents au même pas » donne T = 1 ; or à T = 1, n₀ = N et **L4 est mot pour mot L1**. Le lecteur compte donc **deux fois la même phrase de Ker** (constat A). Les objets de Ker se liraient d'ailleurs aussi bien comme des pas ou des actions que comme des agents : rien dans l'article ne choisit.

Pesée : pour L4, Ker est un **voisin** ; il n'occupe que le cas dégénéré où L4 se confond avec L1. Dans l'autre sens : L4 à T quelconque n'est que L1 appliqué pas par pas, donc aussi élémentaire ; une phrase publique ne peut pas le présenter comme sans précédent, et le point 3 de la section 6 du lecteur reste bon.

## 4. Point 3 — Bash, Goeckel et Towsley

**Le calcul du lecteur est juste.** Pour un mot de code fixé, n·S/σ² suit une loi du khi-deux décentrée à n degrés de liberté, de paramètre la somme des carrés des symboles divisée par σ² (lu sur le PDF pour le modèle, p. 15-16 ; calcul pour la loi). La loi de S ne dépend donc que de l'énergie totale. Contre-calcul numérique local (`calcul_detecteur_puissance_v1.py`, n = 200, σ = 1, 200 000 tirages, niveau 0,05, énergie 40 ; nature : calcul) : puissance 0,585 (un seul symbole), 0,586 (étalée), 0,584 (dix symboles inégaux, signes alternés). L'article lui-même s'arrête aux deux premiers moments et à l'inégalité de Tchebychev (« We bound it using (13) and (14) with Chebyshev’s Inequality » [C37], p. 16) et annonce un résultat d'ordre : la puissance moyenne « determines its detectability by this detector, and that our result applies to all codewords with power of the same order. » [C36], pour un mot de code quelconque (« Suppose Alice employs an arbitrary codebook » [C34], p. 15). L'annexe B ne donne, comme le dit le lecteur, qu'une borne fonction du produit de la fraction de symboles utilisés par leur puissance (« This product is the average symbol power used by Alice. » [C39], p. 24), pas une égalité.

**Cela n'occupe pas L1, même en partie (constats B et C).**
- Le budget de Bash et collègues est une **énergie** (somme des carrés), celui de L est **linéaire** (somme des décalages). Le détecteur de puissance (« but he is oblivious to her signal properties and employs only a simple power detector. » [C35]) est une somme de carrés, pas la statistique somme de L1. L'invariance tient à la symétrie de rotation du bruit gaussien, pas à un pur décalage ; elle ne vaut pas pour une loi F₀ quelconque.
- Sous le budget de L, ce détecteur **n'est pas invariant** : à somme des décalages fixée, l'énergie vaut B²/m pour m décalages égaux. Même contre-calcul (B = 25, n = 200 ; nature : calcul) : puissance du détecteur de puissance 1,00 (m = 1), 0,87 (m = 10), 0,07 (m = 200), contre 0,549, 0,549 et 0,548 pour la somme (la note v2, ligne 76, donne 0,549). Le détecteur de Bash et collègues est, dans les termes de la note, une statistique du khi-deux de L5 : il **voit** la fragmentation.
- Le rapport v2 avait retiré à 2605.16140 le libellé « occupée en partie » au motif que sa borne est quadratique et non linéaire. Le même motif vaut ici ; le rapport contre-lu ne se l'applique pas.
- Pour « la puissance décroît avec n₀ à budget fixé » : l'article porte une loi d'ordre asymptotique sur un nombre de bits et une puissance moyenne par symbole, démontrée par la courbure locale de l'entropie relative (« both laws follow from the property that relative entropy is locally quadratic » [C33], p. 14 ; « is the Fisher information that an observation of noise carries about its power. » [C31], p. 8). Il n'énonce pas la décroissance de la puissance d'un test de la somme sous un budget linéaire de décalage. C'est l'**analogue d'échelle** que disait le rapport v2, qui avait raison pour cette pièce.

Case juste pour Bash et collègues : **voisin** (origine citée de la loi de la racine carrée ; invariance à la répartition sous budget d'énergie, propre au bruit gaussien). La décroissance en n₀ pour un test à horizon fixe est occupée **par Ker seul**, après un changement d'échelle d'une ligne et sous forme asymptotique (constats D et E).

## 5. Point 4 — ce qui reste non trouvé, recherché activement

- **L2 au seuil exact.** Non trouvé. Ker nomme le comptage au-dessus d'un seuil, cousin du maximum, et l'écarte volontairement : « the number of observations greater than 1 is quite sensitive to embedding at p = 1, although worthless for other batch parameters. » [C23] ; il évite « for example the pooling method of counting observations greater than some threshold » [C24] « because this leads to a game theoretical setup which can be intractable. » [C25] (p. 15). Le sens de L2 est donc dit en une phrase, sans seuil exact, sans plancher, sans n fini. C'est une limite reconnue, pas un trou du champ (constat G). Bash et collègues : rien (le mot du maximum n'y apparaît que pour le décodage et la preuve du fait 4).
- **L3** (borne invariante, coût du report, prix de la garantie toujours valide). Non trouvé. Ker réserve le séquentiel ([C9], [C10]). Chez Bash et collègues, fenêtre entière observée ; le seul mot de délai est une perspective (« under additional constraints such as delay should be analyzed. » [C38], p. 21).
- **Processus e cumulé contre détecteur de rupture.** Non trouvé ; aucun des mots martingale, rupture, arrêt, Wald dans les deux pièces.
- **Non-compensation.** Non trouvé. Ker ne parle que d'un biais honnête (p. 14-15).
- **Dépendance.** Non trouvé comme résultat. Deux pistes nommées : chez Ker, des objets chargés avec la même clé, d'où « there could be an amplification of the statistical traces, which we might exploit. » [C27] (p. 16) — dépendance entre objets sous attaque, exploitable par le guetteur, que le lecteur ne relève pas (constat H) ; chez Bash et collègues, « This result was extended to Markov » [C32] (p. 14), pièce listée par le lecteur.
- **Sondes internes.** Rien, dans aucune des deux pièces.

## 6. Point 5 — identités, années, voisins

- **Ker.** L'identification du lecteur est juste : la pièce versée est l'article d'atelier, « J. Camenisch et al. (Eds.): IH 2006, LNCS 4437, pp. 265–281, 2007. » [C1], et non la lettre que citent Bash et collègues (« A. D. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, Aug. » [C42], p. 27) et 2605.16140 (« A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [C44], p. 34). Mais les **deux** pièces portent l'année imprimée 2007 (« Springer-Verlag Berlin Heidelberg 2007 » [C2]) : « Ker 2006 » désigne l'année de l'atelier, pas celle de la parution (constat I). La lettre reste non lue ; son titre répond au souhait, exprimé par Ker p. 15, d'un résultat général de capacité (rapprochement par le seul titre).
- **Bash et collègues.** Identification juste : ni la pièce de 2014 ni celle de 2016. La version lue est la quatrième, « arXiv:1202.6423v4 [cs.IT] 20 Mar 2013 » [C29] ; « 2012 » ne vient que de l'identifiant ; la parution en revue (« Sel. Areas Commun., vol. 31, no. 9, pp. 1921–1930, Sep. 2013. » [C43], 1906.08938 p. 15) n'a pas été lue et son identité de contenu avec la version 4 n'est pas vérifiée (constat I).
- **Voisins nommés et absents de la section 8 du lecteur** (constat J) : « The square root law does not require a linear key » [C40] et « Reliable deniable communication: Hiding messages in noise » [C41] (Bash et collègues, p. 27) ; le livre de Fridrich, chapitre 13, source de la loi de la racine carrée en nombre de symboles modifiés (« symbols in covertext of size n may safely be modified » [C30], p. 2), qui est le voisin d'échelle le plus proche d'un budget linéaire.

## 7. Constats

constat | gravité | page | citation | texte corrigé proposé
---|---|---|---|---
A — | majeur | rapport § 0 point 4, § 3 ligne L4, § 4 ; Ker p. 5, 7 | [C10], [C13] | L4 est compté occupé en partie alors que le seul cas couvert (T = 1) est L1 lui-même. Écrire : « L4 — voisin : Ker n'a ni agents, ni pas, ni lecture aux frontières, ni garantie toujours valide ; son lot de N objets ne donne que le cas dégénéré T = 1, où L4 et L1 sont la même proposition. Une seule composante revendiquée est occupée en partie : l'invariance de L1. » Garder le point 3 de la section 6 (L4 ne se présente pas comme sans précédent).
B — | majeur | rapport § 0 point 3, § 2.2 verdict, § 3 ligne 1 ; Bash p. 15-16 | [C35], [C36], [C37] | « Occupée en partie » est trop fort : budget d'énergie et non linéaire, somme de carrés et non somme, invariance propre au bruit gaussien, résultat d'ordre par moments. Sous le budget linéaire de L ce détecteur dépend de la répartition (calcul : 1,00 ; 0,87 ; 0,07). Écrire : « voisin : pour le détecteur de puissance, la détectabilité d'un mot de code est gouvernée par sa seule énergie (p. 16) ; analogue sous budget quadratique, non transposable au budget linéaire de L ». Motif identique à celui qui a fait retirer « occupée en partie » à 2605.16140 dans la v2.
C — | majeur | rapport § 0 point 2, § 3 ligne 2, § 6 point 2 ; Bash p. 8, 14, 17 | [C31], [C33] | « Occupée (horizon fixe) » par Bash et collègues est trop fort : loi d'ordre asymptotique sur des bits et une puissance par symbole. Écrire : « voisin (analogue d'échelle ; origine citée de la loi de la racine carrée) ». La phrase « la v2 disait analogue d'échelle, c'est à corriger » ne vaut que pour Ker.
D — | majeur | rapport § 0 point 2, § 2.1 ; Ker p. 4, 7, 11 | [C8], [C17], [C18] | Le B de Ker est une proportion par objet (« is the proportionate bandwidth. » [C8]), pas le budget total de L : la charge totale est « The total amount of data hidden by the Steganographer is proportional to » [C17] B·N. À B de Ker fixé, la formule (3) dit que la détection **s'améliore** avec N. L'énoncé de L s'obtient en posant B(L) = N·B(Ker). Ker imprime la forme « capacité » (« To fix the risk of detection, we must » [C18] B ∝ N^(−1/2), lu sur le PDF), jamais « à charge totale fixée, la détection décroît avec N ». Sa métrique est le taux de faux positifs à 50 % de manqués, sa loi nulle est ajustée ou asymptotique. Écrire : « occupée pour un test à horizon fixe, sous forme asymptotique et après un changement d'échelle d'une ligne (B total = N × B de Ker) ».
E — | majeur | rapport § 3 ligne 2, § 5 (« se citent »), § 6 point 2 ; Ker p. 7, 11, 12 | [C16], [C19], [C20] | L'échelle en racine de N ne vaut que si l'indice de queue dépasse 2. Sinon l'exposant change : « in this case the discrimination of the average statistic increases only as a power law » [C19] ; et les données de Ker sont dans ce cas : « is well modelled by a t-distribution with ν = 1.61 » [C20]. Écrire partout : « échelle en N^(1/2) si la variance est finie, en N^(1−1/ν) pour un indice de queue ν entre 1 et 2 (Ker, p. 7 et 11) ». Ajouter aux interdits de la phrase publique : ne pas affirmer une échelle en √n₀ pour toute loi F₀.
F — | majeur | rapport § 5, première puce ; Ker p. 7, 15 | [C11], [C12], [C13], [C26] | La première puce range parmi ce qui « reste revendicable » l'extension aux décalages inégaux, adaptatifs et « ordonnés dans le temps ». Le rapport la dit lui-même élémentaire ; l'ordre temporel n'ajoute rien à une somme. Écrire : « L1 ne reste pas revendicable comme apport : son cœur est imprimé chez Ker (une phrase, donnée comme immédiate, deux valeurs de décalage, choix aléatoire non adaptatif) ; l'extension aux valeurs inégales et adaptatives et l'écriture trajectorielle sont une ligne de calcul, à énoncer comme remarque avec renvoi à Ker. Ker renvoie les valeurs inégales à des travaux futurs : zone à vérifier dans ses travaux suivants avant toute phrase. »
G — | mineur | rapport § 2.1 (L2), § 3 ligne L2 ; Ker p. 15 | [C23], [C24], [C25] | Ajouter que Ker nomme le comptage au-dessus d'un seuil et l'écarte volontairement (jeu difficile à résoudre) : limite reconnue, donc zone à vérifier plus durement dans les travaux suivants.
H — | mineur | rapport § 3 ligne « dépendance » (« aucune dépendance ») ; Ker p. 16 | [C27] | Écrire : « aucun résultat sous dépendance ; une piste nommée : objets chargés avec la même clé, traces amplifiées d'un objet à l'autre, exploitables par le guetteur (p. 16) ». Voisin à signaler aussi pour la co-élévation entre copies du papier B (hors de mon mandat ; à transmettre).
I — | mineur | rapport § 1, titres et tables ; Ker p. 1 ; Bash p. 1 | [C1], [C2], [C29], [C43] | Citer « Ker, atelier de 2006, actes parus en 2007 (volume 4437) » pour ne pas confondre avec la lettre d'août 2007 ; citer « Bash, Goeckel et Towsley, prépublication 1202.6423, version 4 du 20 mars 2013 » et dire que la version de revue (septembre 2013) n'est pas lue.
J — | mineur | rapport § 8 ; Bash p. 2, 14, 27 | [C30], [C40], [C41] | Ajouter trois voisins nommés et non lus : Ker 2010 (clé non linéaire), Che et collègues 2013, le livre de Fridrich (chapitre 13).
K — | mineur | rapport § 2.1 (« aucune réserve de propreté ») ; Ker p. 4, 7, 13 | [C4], [C15] | Deux points non relevés. Une coquille de Ker : la médiane de la moyenne « under the null hypothesis is approximately B. » [C15] — c'est sous l'alternative. Et l'hypothèse de décalage échoue aux fortes charges (« there is both a shape change and a negative bias for higher rates » [C4]), alors que la figure 4 va jusqu'à p = 1 : la courbe de la moyenne y est plate sur les panneaux à grand N, seulement à peu près plate à petit N (figure, ma lecture : panneaux B = 0,01, N = 10 et B = 0,001, N = 100). La platitude à p = 1 est un constat empirique hors de l'hypothèse, pas une conséquence du calcul.
L — | mineur | journal du lecteur ; rapport, « Fichiers lus » point 3 | — | Le journal dit « figures 1 à 5 lues par légendes » et n'enregistre pas la vue en image de la p. 13 que le rapport déclare. Les deux lectures intégrales (17 et 27 pages) y sont consignées à moins d'une minute d'écart chacune : la profondeur ne se juge pas sur le journal. Elle se juge sur le fond : 67 citations sur 67 retrouvées par mon programme, pages et sens exacts pour toutes celles que j'ai relues. Corriger le journal dans une version suivante.

## 8. Table composante × article (mon verdict)

| composante de L | Ker (atelier de 2006, actes de 2007) | Bash, Goeckel et Towsley (version 4, 2013) |
|---|---|---|
| L1 — égalité exacte, en loi et trajectorielle, toute répartition, adaptatif | **occupée en partie** : invariance en loi de la moyenne, à N fini et pour toute loi des scores, pour une répartition à deux valeurs, aléatoire, non adaptative, p. 7 et 14 [C12, C13, C21, C22] ; non fait : valeurs inégales [C26], adaptatif, trajectoire écrite, puissance exacte | voisin : détecteur de puissance gouverné par la seule énergie, p. 16 [C36] ; budget quadratique, bruit gaussien |
| L1 — la puissance décroît avec n₀ à B fixé | **occupée** pour un test à horizon fixe, asymptotique, après changement d'échelle (constat D) ; exposant selon l'indice de queue (constat E), p. 7, 11 [C16, C18, C19] | voisin (analogue d'échelle) |
| L4 — répartition entre agents au même pas, frontières de pas, toujours valide | voisin : cas dégénéré T = 1, identique à L1 | ne touche pas |
| L2 — maximum au seuil exact, plancher à n fini | voisin et contre-indice : comptage au-dessus d'un seuil nommé puis écarté, p. 15 [C23, C24, C25] ; signes et rapport de vraisemblance à grande charge punissent l'étalement | ne touche pas |
| L3 — borne invariante, coût du report, prix du toujours valide | ne touche pas (séquentiel réservé, p. 5 [C9]) | ne touche pas |
| Processus e cumulé contre détecteur de rupture | ne touche pas | ne touche pas |
| Non-compensation | ne touche pas | ne touche pas |
| Validité hors hypothèses, dépendance | voisin : biais honnête et étalonnage, p. 14-15 (lecteur, confirmé) ; piste de dépendance entre objets, p. 16 [C27] | ne touche pas ; pièce sur couvertures de Markov nommée, p. 14 [C32] |
| Scores de sondes internes | ne touche pas | ne touche pas |

## 9. Verdict sur L et suite

- **L, table fermée : occupé en partie.** Composantes : cœur de L1 occupé en partie (Ker) ; décroissance en n₀ occupée pour le test à horizon fixe (Ker) ; L4 non trouvé dans son contenu propre, voisin par son cas dégénéré ; L2 au seuil exact, L3, processus e contre détecteur de rupture, non-compensation, dépendance, sondes : non trouvés dans les pièces lues.
- **La collision remonte au directeur** : une zone revendiquée par N-003/N-004 (« invariances exactes ») est occupée en partie. Je ne tranche pas et ne rédige aucune phrase publique.
- **« Non trouvé » n'est pas « libre »** : Ker réserve en toutes lettres le séquentiel, les valeurs inégales et le comptage à seuil. Ses travaux suivants, dont la lettre de 2007, ne sont pas lus. La zone restante est séduisante et se vérifie plus durement.
- **Ce qu'une phrase publique ne doit pas affirmer, en plus de la liste du lecteur** : que deux composantes distinctes (L1 et L4) ont chacune un précédent ou chacune une nouveauté — c'est une seule proposition ; que Bash et collègues établissent une invariance à la répartition sous un budget linéaire, ou pour une statistique somme ; qu'un détecteur de puissance est aveugle à la fragmentation au sens de L ; que l'échelle est en √n₀ pour toute loi ; que Ker démontre l'invariance (il l'énonce comme immédiate) ou qu'il couvre l'adaptatif ; que la pièce lue est la lettre de 2007 ; que l'énoncé de Bash et collègues date de 2012 dans la forme lue.

## 10. Ce que je n'ai pas fait

- Aucune pièce non versée lue. Rien du lot 8 lu à l'œil.
- La preuve du lemme 2 de Ker et les dérivées de l'annexe A de Bash et collègues sont lues, non refaites.
- Mon contre-calcul est une simulation locale sur processeur, graines par `numpy.random.SeedSequence` (racine 20261114), sortie dans l'archive ; il ne porte sur aucune donnée du programme.

## Annexe — citations contrôlées (`citations-contre-lecture-L-voisins-v1.json`)

| id | pièce | page | citation exacte |
|---|---|---|---|
| C1 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | J. Camenisch et al. (Eds.): IH 2006, LNCS 4437, pp. 265–281, 2007. |
| C2 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 1 | Springer-Verlag Berlin Heidelberg 2007 |
| C3 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 3 | the distribution of the detector response only depends on p in the form of a shift, so that the (additive) estimation error is independent of the true value. |
| C4 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | there is both a shape change and a negative bias for higher rates |
| C5 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | all cover objects have the same capacity |
| C6 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | the Steganographer has no control over the objects themselves, and chooses which to embed in at random. |
| C7 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | We also assume that the Steganographer wants to embed a fixed total amount of secret data |
| C8 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 4 | is the proportionate bandwidth. |
| C9 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | This suggests the study of sequential embedding and tests. We reserve this topic for future work |
| C10 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 5 | we believe that the practice of sequential steganography and steganalysis may be rather different from the fixed-size batch problems studied here. |
| C11 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | It is immediate that |
| C12 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | given the shift hypothesis, the distributional shape of |
| C13 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | does not depend on r or p. Therefore, the Steganographer has no reason to select any particular value of r and p, as long as they multiply to his bandwidth constraint B. |
| C14 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | Suppose that all Xi are independent and identically distributed |
| C15 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | under the null hypothesis is approximately B. |
| C16 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 7 | As long as ν > 1, evidence does accumulate, but the rate at which this happens, as N increases, depends critically on whether ν is greater, or less, than 2. |
| C17 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | The total amount of data hidden by the Steganographer is proportional to |
| C18 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | To fix the risk of detection, we must |
| C19 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 11 | in this case the discrimination of the average statistic increases only as a power law |
| C20 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 12 | is well modelled by a t-distribution with ν = 1.61 |
| C21 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 14 | Also, the average method cannot punish the Steganographer for using a suboptimal embedding strategy. |
| C22 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 14 | Because performance of the average detector does not depend on r, we can pick only a single value of r and plot the false positive rate as N varies. |
| C23 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | the number of observations greater than 1 is quite sensitive to embedding at p = 1, although worthless for other batch parameters. |
| C24 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | for example the pooling method of counting observations greater than some threshold |
| C25 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | because this leads to a game theoretical setup which can be intractable. |
| C26 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 15 | In future work we should consider allowing the Steganographer to vary the amount of data embedded in each object (this results in a larger mixture) |
| C27 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 16 | there could be an amplification of the statistical traces, which we might exploit. |
| C28 | `ker-2006-batch-steganography-pooled-steganalysis.pdf` | 17 | and all are independent. |
| C29 | `1202.6423v4.pdf` | 1 | arXiv:1202.6423v4 [cs.IT] 20 Mar 2013 |
| C30 | `1202.6423v4.pdf` | 2 | symbols in covertext of size n may safely be modified |
| C31 | `1202.6423v4.pdf` | 8 | is the Fisher information that an observation of noise carries about its power. |
| C32 | `1202.6423v4.pdf` | 14 | This result was extended to Markov |
| C33 | `1202.6423v4.pdf` | 14 | both laws follow from the property that relative entropy is locally quadratic |
| C34 | `1202.6423v4.pdf` | 15 | Suppose Alice employs an arbitrary codebook |
| C35 | `1202.6423v4.pdf` | 15 | but he is oblivious to her signal properties and employs only a simple power detector. |
| C36 | `1202.6423v4.pdf` | 16 | determines its detectability by this detector, and that our result applies to all codewords with power of the same order. |
| C37 | `1202.6423v4.pdf` | 16 | We bound it using (13) and (14) with Chebyshev’s Inequality |
| C38 | `1202.6423v4.pdf` | 21 | under additional constraints such as delay should be analyzed. |
| C39 | `1202.6423v4.pdf` | 24 | This product is the average symbol power used by Alice. |
| C40 | `1202.6423v4.pdf` | 27 | The square root law does not require a linear key |
| C41 | `1202.6423v4.pdf` | 27 | Reliable deniable communication: Hiding messages in noise |
| C42 | `1202.6423v4.pdf` | 27 | A. D. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, Aug. |
| C43 | `1906.08938v2.pdf` | 15 | Sel. Areas Commun., vol. 31, no. 9, pp. 1921–1930, Sep. 2013. |
| C44 | `2605.16140v1.pdf` | 34 | A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. |
