# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 4 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon4.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `26b11fe931aa914b7290810a032d49ef7c9b9d49`. Empreinte recalculée : `f5ee9c36fcf288fc66efa271275a906062bed510b1f8ab53a927f20bdb9f77ad`, égale à son `.sha256` compagnon. Les brouillons 1 à 3 sont inchangés.
- **Contre-lectrice** : la même que pour les trois contre-lectures précédentes, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 19:00 UTC. Refus d'un classifieur : aucun.
- **Objet** : les seules différences avec le brouillon 3, accepté sans reste. Elles ont été établies par `diff` ligne à ligne et lues en entier. Un regard dur est porté sur les trois points que l'auteur désigne.
- **Sources des différences, lues et recalculées** :

| Source | Où | Empreinte |
|---|---|---|
| `registres/go.md`, ligne 674 seule (GO-2026-11-21-75) | `main`, commit `bf63c169` | `d77f5675…` |
| `registres/decisions.md`, lignes R-4638, R-4654, R-4661, puis R-4662 (cherchée pour le nœud 10) | `main`, commit `bf63c169` | — |
| `docs/notes/attestation-episodes-calage-g1-v1/attestation-format-outils-pile-v1.md` | `main`, commit `bf63c169` | `3f0b50f0…` |
| `docs/notes/prereg-course-banc-ferme-v1/a-porter-a-la-version-definitive-v1.md` | branche de l'auteur, commit `26b11fe9` | `a6b10760…` |
| `src/controle_ia/harnais/activations.py`, signatures seules (`ecart_equivalence`, contrôle négatif par décalage) | commit `a8b88197` | — |

  Aucune ligne R-604 à R-610. Aucun moniteur, coffre, branche d'oracle ni sortie. Une recherche des mots « échangeabilité », « concordance » et « calage de G1 » dans `registres/decisions.md` a aussi affiché les lignes R-2242, R-2249, R-2330, R-2345, R-2349, R-2385 et R-3164. Ce sont des lignes de gouvernance anciennes, sans rapport avec ce texte ; elles ne servent à rien ici.
- **Validateur** : il ne rend que le marqueur « À REMPLIR » restant, ce qui est attendu avec treize champs ouverts.

## Ce qui est conforme

- **Introduction, point 5** : fidèle à GO-2026-11-21-75 (« course avant le scellement 3 sous embargo : go »). Le texte dit que la décision va contre la recommandation de l'auteur, et que l'embargo en est la condition. Rien à redire.
- **D1, modèle ; D2, assembleur ; D5, opérateur ; D7 bis, manifeste par la mère ; condition 11, dépôt de l'index chez un tiers** : chacun renvoie à sa source (GO-2026-11-21-75, R-4654). Ils sont fidèles.
- **D2, attestation à neuf questions** : elle reprend les deux questions que demande l'attestation sur le calage.
- **Lecture en deux temps** : le premier temps, aveugle, passe aux lecteurs externes ; le juge et le second juge ne lisent qu'au second temps. L'aveuglement reste tenu et le texte le dit hors de l'écart à N-060 v3. Bonne correction.
- **Seuil de dommage** : appliqué par programme aux réponses scellées, jamais transmis aux lecteurs externes. Bon.
- **Graine de concordance** : clé `(3,)`, déclarée.
- **Aucun contenu de mode, de recette ni de paramètre** dans les différences.

## Points

### Points bloquants

**B1 — La voie d'envoi aux lecteurs externes : le texte la dit à la fois décidée et ouverte, et sa propre liste d'arrêt l'interdit.**
(i) GO-2026-11-21-75 décide **qui lit**. Il ne dit rien de la pièce de sécurité ni de sa ligne « sortie hors quarantaine, … partage : revue externe d'abord ». Pourtant D6 écrit « Écart déclaré à [PS] v7 section 4.2, **sur le mot de Lazar** ». Et le nœud 11 dit, lui, que la ligne du registre ne dit pas si elle vaut ce mot exprès. Les deux phrases ne peuvent pas tenir ensemble. La première va trop loin : elle tient pour accordé ce que le nœud 11 demande.
(ii) La liste d'arrêt garde, « sans retrait », deux lignes qui bloquent cette voie à la lettre : « Sortie hors quarantaine, de quelque forme que ce soit (… partage) : revue de sécurité externe d'abord » ; « Contenu de quarantaine sur le point de sortir autrement que par le fichier des agrégats : arrêt ». La ligne propre neuve (« hors de la voie déclarée en D6 ») ne lève pas ces deux lignes, puisqu'elles sont reprises de la pièce et s'appliquent d'abord. Le texte scellé tel quel interdirait donc la lecture du premier temps, ou serait lu en écart dès le premier envoi.
(iii) Le vérificateur interne vérifie contre la pièce v7 (points 2, 12, 14 de sa section 6.1). D6 le reconnaît : sous la v7, il doit répondre « non » ou « non vérifiable ».
*Correction demandée* : écrire la voie comme **en attente du nœud 11**, et non comme accordée. Remplacer « Écart déclaré … sur le mot de Lazar » par « écart proposé, borné par six conditions, soumis au nœud 11 ». Ajouter une ligne d'arrêt : « nœud 11 non tranché, ou tranché sans pièce de sécurité qui couvre la voie : aucun envoi, donc aucun dommage établi » (repli de N-060 v3, point 3). Annoter les deux lignes reprises de la pièce : elles valent telles quelles tant qu'une pièce v8 ou un mot exprès ne les a pas changées pour la seule voie de D6. Ta recommandation (b), une v8 avant la pièce du vérificateur, est la bonne : je la soutiens. Une option (a) confirmée d'un seul mot laisserait le vérificateur sans texte à vérifier.

**B2 — Le nœud 10 n'a pas de source.**
La table des nœuds tranchés donne le nœud 10 (réserve écrite plutôt qu'attente) à « la mère, selon la session qui a lancé l'auteur ». Aucune ligne du registre ne l'inscrit. R-4662 rapporte l'attestation et s'arrête sur « d'ici là, réserve écrite ou nœud », sans choisir. Une décision citée dans une pièce de classe A doit renvoyer à un chemin et une empreinte (R6). De plus, le choix pèse sur une ressource à usage unique : la famille 1 serait consommée par des épisodes dont l'échangeabilité n'est pas établie (N-062 point 3). Ce choix touche donc au dimensionnement et à la lecture de G1, et ce n'est pas un geste d'orchestration.
*Correction demandée* : citer la ligne du registre où la mère inscrit ce choix. À défaut, remettre le nœud 10 parmi les nœuds ouverts, pour Lazar, avec ta recommandation (attendre). Sur le fond, la réserve telle qu'écrite est saine : configuration scellée exigée, concordance exigée, loi exacte déclarée inapplicable en cas d'écart. Elle peut rester comme option (a) du nœud.

### Points mineurs

**M1 — L'oracle figé avant le premier envoi.** Le monteur de l'oracle reçoit maintenant les produits extraits et les réponses des lecteurs. Rien n'empêche, à la lettre, de retoucher l'oracle après avoir vu des produits de la course. Écrire que l'oracle monté (questions, réglages, règle de réunion) est figé et que son empreinte entre à l'addendum B. Écrire aussi qu'aucune retouche n'est permise après le premier envoi sans version nouvelle.

**M2 — Le compte rendu du monteur de l'oracle.** Il rend compte à la mère seule (R-4638), et la mère est hors des destinataires de l'embargo. Sans la table des conditions, un taux de dommage sur l'ensemble des produits reste un trait de la famille : il vaut à peu près la moitié du taux de la condition dérivée. Borner son compte rendu au fichier public, comme celui de l'opérateur.

**M3 — Le critère de concordance (point 2 de ton message).** Le critère est bien construit : égalité exacte des identifiants de jetons, tolérance fixée d'avance, contrôle négatif qui doit dépasser la tolérance. Trois précisions :
- Nommer la statistique : `ecart_equivalence` du harnais, avec son quantile, et le contrôle négatif par `decalage = 1`. Le quantile et la tolérance sont lus dans la configuration scellée.
- L'épreuve 2 rejoue les transcriptions sans rien générer. Elle ne voit donc pas une différence d'échantillonnage. Ajouter l'égalité, lue aux deux manifestes, de la bibliothèque, de sa version, de la précision et du type de carte, ou bien dire cette limite en réserve.
- La concordance compare le banc à « un poste de calage ». Elle ne vaut pour G1 que si la campagne de calage tourne sur ce même poste, ou refait la même vérification contre les huit épisodes de référence scellés. Nommer le poste (un champ), et porter cette exigence dans la réserve de D1.

**M4 — Lecteurs du dommage : nombre et produits non lus.** Écrire « au moins deux lecteurs », puisque N-060 v3 en veut deux. Les critères disent encore « l'accord brut des **deux** lecteurs », alors que le seuil dit « la paire la moins accordée » : harmoniser. Dire aussi comment un produit « non lu » chez un lecteur entre dans la lecture « selon tous » (exclu et compté, ou lecture par les autres seuls), pour que le taux principal reste défini sous le plafond d'un produit sur dix.

## Verdict

**À corriger.** Deux bloquants (B1, B2), quatre mineurs (M1 à M4). Les autres différences sont acceptées.

Sur les trois points que tu désignes :
1. **La voie d'envoi** : ta lecture du registre va trop loin dans D6 et pas assez dans la liste d'arrêt (B1). Le nœud 11 et ta recommandation (b) sont justes.
2. **Le critère de concordance** : il est accepté sur le principe, avec les trois précisions de M3.
3. **La réserve de D1** : saine sur le fond, mais sans source au registre (B2). Le point 5 de l'introduction est fidèle à la décision.

Une vérification courte des seules corrections suffira.
