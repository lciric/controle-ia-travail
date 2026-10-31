# Relecture indépendante (Opus) de la synthèse du tour 1 — collisionneur « protocelles » — v1

31 octobre 2026. Relecteur neuf (Opus 5.5, sous-agent de la lignée conv-audit), sur la demande du directeur : « Opus relis les réponses qui vont arriver ». Je n'ai écrit ni la question, ni les critères, ni la synthèse, ni aucune relecture antérieure du papier. Lecture au processeur seulement : aucune cellule lue (elles sont sous `donnees/`), aucun `git fetch`, aucun appel de modèle ni de réseau, aucun fichier existant modifié. **Confidentiel** : le papier n'est pas publié ; il est cité par page et ligne.

## Pièces (empreintes recalculées)

| Pièce | Chemin | Empreinte (égale au compagnon) |
|---|---|---|
| Synthèse | `origin/main:docs/notes/protocelles-collisionneur-v1/synthese-protocelles-tour1-v1.md` | `dfd0d168ab1acbc8e90dd63019cf907b13ccfdf507dc51a0f1e7009cc15683fb` |
| Critères gelés | `origin/main:docs/notes/protocelles-collisionneur-v1/criteres-lecture-protocelles-tour1-v1.md` | `aed5f5933150a3ce786dad556e00dbc98c130ff1a7d1f82a5e0843a32baa9896` |
| Question v3 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/papier-protocelles-idees-v1/question-collisionneur-protocelles-v3.md` | `0aa60557d291e71e454cb779d92068506dd9fd7a9da843a7d1f6eeecc8d836da` (celle que cite la synthèse) |
| Papier v0.19.4 | `docs/sources/pdf/Ciric-protocells-fecundity-complete-v0.19.4.pdf` | `ba59c2541a31a94f15ee943ec15353609b6d3d0a61748b0d80655d294167cc61` |
| Note de conv-audit (règle citée au point e) | même dossier que la question, `idees-conv-audit-papier-protocelles-v1.md` | `da93800c674eb045978c2dab2e399f781975db6fd4a43ab297c3e2f1b56ee444` |

R11 : le nom donné dans la commande (`…-Nature-complete-v0.19.4.pdf`) n'existe pas sur disque ; le seul fichier v0.19.4 est celui du tableau, dont l'empreinte est celle que cite la question.

**Renvois.** « p. N » = page du PDF. « l. L » = ligne du fichier servi `faits-protocelles-v2.md`, que je n'ai pas lu : numérotation reconstruite (ligne du texte brut de `pdftotext` + 2 × page + 4). Contrôle : les 57 renvois de la synthèse testés retombent tous sur la phrase citée (à deux lignes près), ainsi que plus de quarante renvois nouveaux de cette relecture.

## Verdict

**Fidèle pour l'essentiel, inexacte dans le détail.** Le verdict principal (aucune application terme à terme ; ni pince ni arène), la réponse sur les fusions inachevées et l'ordre des travaux tiennent sur le PDF, et les quatre inexactitudes majeures des espèces sont confirmées. Mais seules 14 des 20 affirmations relevées tiennent ; la liste « vérifiée » contient une erreur propre à la synthèse (le seuil exact donné pour n = 3 est celui de n = 2) ; les conditions du verdict sont mal bornées ; les points (a) et (f) et la citation de la règle de (e) sont omis ou tronqués. À corriger avant tout scellement ; rien n'empêche le tour 2.

## 1. Les vingt affirmations, revérifiées sur le PDF

**Confirmées : 14 (13 inexactes et 1 non trouvée), dont les 4 majeures.**

| N° | Verdict de ce relecteur | Pièce |
|---|---|---|
| I1 | confirmée, mineure | θ′ est relatif à la réplicase (p. 8, l. 701) ; coude à θ′ = 2 (l. 720-722) |
| I2 | confirmée « non trouvée » ; la Fig. 7B la contredit même : sous θ′ = 2, forte pente pour n = 10 et 20 | p. 10, l. 935-937 et figure |
| I3 | confirmée, mineure ; λ*(p) est en l. 5028 plutôt qu'en l. 5024-5025 | p. 68 |
| I4 | confirmée, **majeure** ; de plus, à U = 0,3, la loi repose sur (H2) même asymptotiquement | p. 35, l. 2538 ; p. 40, l. 2788-2789 ; p. 2, l. 155-156 |
| I8 | confirmée | p. 40, l. 2759-2766 |
| I9 | confirmée | p. 12, l. 1135 et 1146-1147 |
| I10 | confirmée, **majeure** (1,32 < e^0,3 = 1,35 < 2,08) | comme I4 |
| I11 | confirmée, **majeure** : extinction si M_D < 1, condition nécessaire seulement ; atteinte pour le tri partiel à y = 0 | p. 68, l. 4990-4991 ; p. 69, l. 5095-5100 |
| I12 | confirmée, **majeure** ; nuance : la phrase du papier (« plus viable que des copies perdues ») invite la lecture de C, le comparateur n'est donné qu'à la ligne suivante | p. 59, l. 4280-4281 ; p. 10, l. 863 ; p. 56, l. 4048-4049 |
| I13 | confirmée | p. 21, l. 1782-1783 |
| I14 | confirmée | p. 19, l. 1688-1690 |
| I17 | confirmée, mineure (ajustement recalculé : 0,351 ; la demi-chute près de y ≈ 3,1 place ψ(3) au-dessus de ln 2/2 = 0,3466) | p. 8, l. 676 ; p. 9 |
| I18 | confirmée, mineure | p. 28, l. 2109 et 2122-2123 |
| I19 | confirmée, mineure | p. 33, l. 2427-2428 |

**Contestées : 3.**
- **I15** : le motif est faux. Le papier calcule n = 5 (Fig. 7B, p. 10, l. 935) ; à θ′ = 2 on y lit nτc ≈ 1,6 à n = 5 et 1,85 à n = 10 (τc ≈ 0,32 et 0,185, lecture graphique) : 0,25 à 0,30 à n = 6 est une interpolation compatible. Au pire « illustratif non marqué » (critère 11) ; ce n'est pas une formule fermée, donc « non recalculé » (critère 3), pas « inexact ».
- **I16** : la citation de C est exacte. L'inégalité est à la p. 75, Appendice S12.3, point B1 (l. 5473-5477), en plus de la p. 45.
- **I20** : pour l'allumage (seuil d'invasion), la fusion ne dépasse pas ln 2, c'est prouvé (Table 1, p. 6, l. 522 et 547 ; p. 13, l. 1195-1196), et θ < 1 n'ajoute rien au bonus du compartiment (p. 13, l. 1184-1186) : la liste à trois de C est exacte pour cet objet. La synthèse reprend d'ailleurs cette liste à son compte au §4.

**Hors catégorie : 2.**
- **I6** : fond juste ((H2) est une propriété d'un rayon spectral, p. 7-8, l. 666-671), mais c'est une affirmation d'apport (critère 17), pas une lecture fausse du papier.
- **I7** : ne porte pas sur le papier ; les 70 tours de Bailey sont énoncés par la question (critère 3 : ni « RAPPORTÉ » ni « inexact ») ; la synthèse la classe à la fois « RAPPORTÉ » et « inexacte ».

**Indécidable sans la cellule : 1.**
- **I5** : le papier dit « sera déposé à la publication » (p. 22, l. 1860-1864), mais aussi, au présent, « déposé avec le code » ou « avec leurs scripts et journaux » (p. 33, l. 2429 ; p. 53, l. 3942 ; p. 54, l. 3967). Seul le temps employé par B tranche.

**Erreurs de la synthèse hors de sa table.**
- **E1 (importante)** : « Uc(3) = 0,450266 » (§9, vérifiées) et « seuil exact 0,450 à n = 3 » (§4, réponse au point c). 0,450266 est la valeur de n = 2 ; à n = 3, θ = 1, fécondité infinie, Uc = 0,644415 (Table S1a, p. 42, l. 2880 et 2884). Si la valeur vient de B ou de C, c'est une inexactitude manquée, majeure pour B, qui instancie n = 3.
- **E2** : « Théorème 1, θ ≥ 2 ⇒ aucune fidélité ne suffit » est marqué vérifié sans sa condition. Le théorème porte sur le noyau limite (n → ∞, p. 4, l. 350) ; à taille finie le seuil reste positif et décroît en 1/n (p. 18, l. 1640 ; Table S1c, p. 42, l. 2985), ce qui est justement le régime des lots de 3 à 6.
- **E3** : le §3 approuve « à juste titre » que la borne R ≤ n/5 vaut pour toute division aveugle. Elle est prouvée pour le modèle principal (p. 41, l. 2808-2824). Sans effet pratique ici : pour n ≤ 12, la borne ln(2R/(R + 1)), valable pour toute règle aveugle, est meilleure (p. 41, l. 2832).

## 2. Les critères gelés sont-ils appliqués à la lettre ?

Oui pour les critères 1, 2, 4, 6 à 8, 11 à 14 et 18 à 21. Les écarts :
- **Critère 3** : I6, I7 et I15 (point 1) ; une vérification fausse (E1) et une condition omise (E2).
- **Critère 5** : « un parent contre deux parents » est une convergence du T3 (P3 : B-T3, D-T3), que le verdict présente comme « accord réel » ; le §10 la compte en plus parmi les accords indépendants (C + D) : double compte probable.
- **Critère 9** : les lignes 1 et 2 du verdict reposent sur des convergences unanimes du T3 ; la réserve de symétrie existe (§11.2), mais elle n'est pas attachée au verdict.
- **Critère 10** : P1 est dite « signée conditionnelle » alors que sa mesure est invalidée ; elle est « non signée (mesure) ».
- **Critère 15** : « archiver plutôt que détruire (C + D) » est compté comme accord alors que les conditions divergent (C réinjecte sous quota, D jamais) ; le sous-tour de D n'est pas donné.
- **Critère 16** : le contenu du point (f) n'est pas rapporté, seulement sa couverture.
- **Critère 17** : l'étalonnage par simulation est « déjà présent » dans le papier (biais quantifié à 200 protocelles et seuils tirés des seuls noyaux exacts, p. 42, l. 2855-2858 ; contrôle par Monte Carlo du rayon spectral, p. 17, l. 1590-1591) : il ne compte pas comme apport.

## 3. Omissions et déformations par rapport aux demandes (a) à (h)

- **(a)** : la synthèse donne la couverture, aucun contenu.
- **(b)** : deux traits du contexte de la question ne sont pas traités. Le catalyseur de l'organisme est le bisociateur (extérieur, à budget fixé par l'orchestrateur) et non une fiche, alors que dans le papier le débit de copie est porté par les réplicases elles-mêmes (RF, p. 16, l. 1557). Et les paires sont prises dans deux espaces éloignés : paires bipartites, F_A·F_B au lieu de F(F − 1). À chercher dans les cellules.
- **(c)** : E1. De plus, le papier donne déjà des seuils exacts aux petites tailles (Table S1a, n = 2 à 8 ; Table S2, n = 5 à R = 10, 40, 160 : de 0,536 à 0,690 à θ = 1, p. 43, l. 3051-3054). Le recodage du §8 (iv) n'est donc pas nécessaire pour une première lecture.
- **(e)** : la règle est citée tronquée. La note dit « jetée, jamais archivée **comme fiche réutilisable** » (§5 de la note), c'est-à-dire jamais remise dans le vivier : le défaut consolidé de la synthèse (hors du vivier) est en substance la règle de la note. Déformation héritée de la question.
- **(f)** : pires cas, gardes et vérification extérieure ne sont pas consolidés.
- **(h)** : la forme conditionnelle « allumage impossible si … q ≤ 1/2 » omet θ ≥ 1. Pour θ < 1, la condition est q ≤ θ/2 (Théorème 2, p. 4, l. 355). Or un filtre qui fait préférer les fiches vérifiées est justement un θ < 1.
- **Tour 2** : la question prévoit un verdict par piste (note de conv-audit, relectures d'Opus) ; la synthèse le remplace par des duels sans le dire.

## 4. Verdict principal : d'accord sur le fond, conditions mal bornées

**D'accord** : aucune correspondance de noyau n'est établie, et rien ne s'applique à la pince ni à l'arène. On n'y trouve ni population qui se copie en trans, ni compartiments qui croissent et se scindent (modèle, p. 3 ; hypothèses du plafond, p. 13, l. 1187). Les théorèmes du levier portent sur les règles de division du modèle à réplicase (p. 68, Théorèmes L1 et L3), et la « condition nécessaire » de C suppose une unité « paire » que la pince n'a pas.

**Mais la liste « fiche seule stérile, parents non consommés, division aveugle » est :**
- **trop courte pour une application exacte.** Il faut aussi : une copie à partir d'un seul modèle (p. 16, l. 1555 ; c'est la rupture « deux parents » du §5 de la synthèse elle-même) ; un débit de copie porté par les fiches fertiles ; une seule classe de parasites de poids fixe et aucune compétition (p. 16, l. 1529-1531, alors qu'il y a cinq statuts plantés et un budget partagé) ; des paires prises dans une seule population ;
- **trop longue pour le plafond pris comme borne.** Si chaque fusion consomme au moins un parent et donne au plus un enfant, le nombre de fiches vraies ne peut pas croître : l'allumage est exclu quel que soit q. La non-consommation conditionne donc la possibilité de l'allumage et la valeur des seuils, pas la borne ;
- **incomplète sur θ** (point 3, (h)).

## 5. Fusions inachevées : la synthèse a raison

Le papier ne justifie pas « jeter, jamais archiver ».
- Il admet trois sorts : perdue, assez rare pour ne pas compter, ou modèle lent recopié jusqu'au bout (p. 16, l. 1542-1543).
- La perte est une boucle sur place : sans coût sur la charge à fécondité infinie, avec un facteur 1/(1 − τ) sur la fécondité sinon (p. 56, l. 4048-4049 ; p. 10, l. 863).
- Il ne connaît pas l'archive, qui équivaut à la perte pour la dynamique.
- Le bain de brouillons lents n'existe que si θ′ < 2(1 − τ) et sans re-troncation (p. 59, l. 4286 et 4304-4306), et c'est un résultat numérique (p. 21, l. 1782-1783).

Deux nuances manquent à la synthèse :
- l'identité de la perte exige le même τ pour tous les modèles (p. 56, l. 4049-4051) : si l'abandon d'une fusion dépend des statuts des parents, jeter n'est plus neutre ;
- lue avec son complément, la règle de la note est compatible avec le papier tant que θ′ est inconnu.

## 6. Correspondances qui survivent, et la mesure la moins chère

Rien ne survit pour q, θ, R, τ, θ′, le prix ou le coude à θ′ = 2 : tout cela dépend du noyau. Trois lemmes survivent, sous réserve d'une même pièce manquante, le code de l'orchestrateur.

1. **Division ↔ partage des lots au hasard.** C'est de la combinatoire pure, indépendante du noyau : une règle aveugle n'augmente pas en espérance la densité de paires sommée sur les filles (p. 32, l. 2358-2365), chaque fille gardant la fraction α_d² des paires (p. 68, l. 5023). La part r̄ des paires vraies gardées ensemble ne dépend que de la règle (tri partiel : (1 + p)/2, l. 5027-5028).
   - Mesure : lire le code de formation des lots et calculer r̄, exactement ou par simulation sur des étiquettes plantées. Au processeur, sans dépense, sans journaux.
   - Ce n'est pertinent que si la paire est l'unité qui se reproduit.
2. **Sort « perdu » ↔ brouillon jeté ou archivé hors du vivier.** Par l'identité (i) (p. 56, l. 4048-4051), c'est une boucle sur place : détruire ou archiver revient au même pour la dynamique, avec un coût en budget de 1/(1 − τ), à condition que τ ne dépende pas des statuts des parents.
   - Mesure : audit du code au processeur (un brouillon peut-il revenir dans le vivier ? le critère d'abandon voit-il le contenu ?).
   - Mesurer τ par type de paire demande les journaux, après scellement, ou des runs sur devis.
3. **Candidate, esquisse de ce relecteur, à contre-lire (R2) avant tout usage : le plafond comme borne d'un seul côté.** Hypothèses : tirage uniforme des paires dans un lot, hybrides stériles (q_vf = q_ff = 0), parents gardés, partage aveugle à taille fixe. Alors, à chaque fusion, E[φ′]/φ = (N − 1)/N + 2 q_vv F/N² pour φ = F(F − 1)/(N − 1), ce qui reste ≤ 1 dès que q_vv ≤ 1/2. C'est la condition du Théorème 2 à θ = 1 (p. 4, l. 355), et la dérive est toujours au moins aussi défavorable que dans le papier. Conséquence : pas d'allumage si q_vv ≤ 1/2. Avec des paires bipartites, le calcul est à refaire avec F_A·F_B.
   - Mesure : preuve écrite et contre-lue, puis simulation au processeur de la règle réelle de l'orchestrateur avec des q plantés, sans dépense.
   - Seulement ensuite : q_vv et q_vf sur données (journaux après scellement, ou runs sur devis).

## Réserves de ce relecteur

- Cellules non lues : I5, l'origine de E1 et les deux traits du point 3 (b) restent à vérifier sur elles.
- Numéros de ligne reconstruits, non lus dans le fichier servi.
- Fig. 7B lue graphiquement.
- Le point 6.3 est une esquisse, pas un résultat.
