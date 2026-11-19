# Note du rédacteur — brouillon 10 du texte neuf du bras A des organismes discrets — v1

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon10.md`, `16a93810f4f9791f65b0aa2cdaf9e340aad230e75a276990f3b52b5fddc84a18` (1 609 lignes). Brouillon 9 inchangé (`a1b0e9b904b89004e79516bda841ffd36111690bdc6c2636a1ad642e5fec5709`, vérifié).
- **Fiches à jour pour Lazar** : `docs/notes/relance-organismes-discrets-v1/decisions-bras-a-brouillon10-v1.md` (les six fiches et le complément, mot pour mot ceux de la section 12 ; il remplace pour la lecture les deux fichiers précédents, non modifiés).
- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même agent que pour les brouillons 6 à 9.
- **Contre-lecture traitée** : `contre-lecture-preenregistrement-v2-brouillon9-v1.md`, `c78c97c7f3aa2ee2d785345834046837400cf3f17a62a6079ced69d34e278413` (Claude Opus 5.5), lue en entier ; ses pièces n'ont pas été ouvertes. Pièce des réponses de la session principale : `reponses-de-la-mere-desaccords-et-lot16-v3-v1.md`, `9b4a1b123a53c6ed53898582a579877eb1a56a6cc15a737ddee421854aaca18e`.
- **Heures (UTC, `date -u`)** : travail repris à 2026-11-19T12:20:59Z, après une interruption par une limite d'usage du modèle (rien n'avait été écrit avant elle) ; brouillon et fiches finis à 2026-11-19T12:25:31Z selon la même horloge.
- **Interdits tenus** : les mêmes ; aucun appel de modèle ; aucun fichier existant modifié ; rien committé ni scellé. Trois fichiers neufs : le brouillon 10, les fiches, cette note.
- **Contrôles faits** : validateur — deux problèmes attendus (marque dans neuf cases de 13.1 et nulle part ailleurs ; contre-lecture 10 sans ses empreintes ; la contre-lecture 9 est inscrite avec ses deux empreintes) ; consignes inchangées (`98a9bd34…`, `ecf590ea…`) ; les huit textes des moniteurs transmis restent des sous-chaînes exactes ; les six fiches à jour et le complément sont dans le texte à l'octet près, et l'ancienne fiche 6 n'y est plus ; table d'en-tête, 88 empreintes égales, 3 sautées (interdits) ; titres de section identiques à ceux du brouillon 9, sauf celui de 3.5, complété comme la contre-lecture le demandait (C-8).

## 1. Table de correspondance, brouillon 9 → brouillon 10

Numéros stables. Neufs : 14.22 ; contre-lecture 10 (à faire). Tout ce qui n'est pas listé est le texte du brouillon 9 à l'octet près.

| section | changements | d'où |
|---|---|---|
| titre, statut, en-tête | brouillon 10 ; contre-lecture 9 faite ; six décisions, dont un nœud sans défaut ; ce qui a été ouvert de plus ; date ; commit ; note et fichier des fiches ; trois lignes à la table des pièces (brouillon 9, sa contre-lecture, réponses de la session principale) | C-9 |
| 3.2 | « json » sans égard à la casse | R-7 |
| 3.5 | titre : « sous réserve du point 15 » ; paragraphe de réserve ; invariant (b) écrit sous les deux branches du point 15, avec les trois conditions de l'option (a) ; « moniteurs figés » corrigé | C-8 ; C-12 ; L-1 |
| « Métrique » | point 7 : trois motifs ; point 8 : permutations des étiquettes d'épisode, classe honnête et scores de l'aire conditionnelle | C-3 ; B-1 ; C-7 |
| 6.2 | préfixe sous la révision ; quatre familles de clés du hasard des moniteurs ; soixante et une clés « pour la lecture commune et l'aire conditionnelle », et qui tire les vingt dernières selon le point 15 ; qui tire `lec6` | R-8 ; C-5 ; C-6 ; R-13 |
| 6.3 | (l9) sans le déclencheur de la table C ; (m) : ce déclencheur et son audit après la table C | C-1 |
| 6.4 | point 2 : trois motifs ; part d'actions non permutables « champ final ouvert » rapportée par dose ; témoin bénin : dernier champ | C-3 ; R-11 ; C-4 |
| 6.9 | unité de la permutation : par épisode (version 4 du module habilité) ; famille de Holm : valeur absente comptée pour 1, champ rendu par le module et pris tel quel ; aire conditionnelle écrite sous les deux branches du point 15 ; portée du choix d'unité | B-1 ; B-2 ; L-1 ; R-10 |
| 6.10 | le module qui rend les nombres est la version 4 | message du coordinateur |
| 7.2 | sous A15 ou A16, étapes (m) et (n) non jouées ; « A15, A16 ou les deux » ; ligne A11 : trois moments | R-4 ; R-5 ; C-1 |
| 7.6 | spécificité de l'épreuve trop propre : celle des honnêtes relues du lot des jumeaux ; contenu de l'audit côté habilité pour une dose en C6 | R-6 ; C-2 |
| 8.4 | quatre lignes neuves (unité de la permutation ; famille de Holm complète ; scores remis à l'analyse, option (b) ; liste des épisodes retenus, option (a)) ; sous la table : limite de la garde d'ordre ; ce que la base lit de la table B | B-1 ; B-2 ; C-8 ; R-2 ; R-9 |
| 12 | les six fiches mises à jour ; point 15 : titre et fiche réécrits, nœud sans défaut | avis du contre-lecteur ; session principale |
| 13 | étape 6 (contre-lecture 10) ; 13.1 : cases « nœuds » (point 15 sans défaut, branche écartée à retirer avant scellement), « renvoi de la base » (quatre vérifications de plus), « module des cinq moniteurs » (version 4, tête `44e3f325`, `23018822…`) ; 13.2 : lanceur de l'étape de discrétion (une seule exécution ; sortie ou entrée selon le point 15), registre (trois ou quatre cellules) | C-10 ; B-1 ; R-2 ; R-3 |
| 14 | 14.17, ligne R-11 ; 14.21, pièce citée ; 14.22 neuf | C-10 ; C-9 |
| « Contre-lecture » | contre-lecture 9 inscrite avec ses deux empreintes ; contre-lecture 10 à faire, fichiers à donner | C-10 |

## 2. Traitement de la contre-lecture (détail : section 14.22)

**Repris tels quels** : B-1, B-2, C-1 à C-4, C-7, C-10, C-11, C-12, R-2 à R-5, R-8, R-10, R-11, R-12.

**Repris avec un écart, dit ici** :
- **C-5, C-6** : la quatrième famille de clés (aire conditionnelle) est tirée par l'instance d'analyse ou par le côté habilité, selon la branche retenue au point 15.
- **C-8** : ses trois conditions sont écrites, mais sous l'option (a) du point 15, qui n'est plus la branche de tête.
- **C-9** : la pièce porte le nom sous lequel la relance l'a versée, non celui que le contre-lecteur proposait.
- **R-6** : tranché — spécificité des honnêtes relues du lot des jumeaux.
- **R-7** : tranché — sans égard à la casse.
- **R-9, R-13** : écrits comme exigences à vérifier par le côté habilité (la base ne lit de la table B que son existence et son empreinte ; `lec6` est tirée côté habilité).
- **L-1** : repris — nœud sans défaut. **De plus, et contre l'avis du contre-lecteur**, l'option (b) est mise en tête, sur le mot de la session principale ; la divergence est exposée dans la fiche.

**R-1, pris acte** : la note du brouillon 9 disait les règles de la table A « corrigées en version 2, à vérifier » ; le contre-lecteur a vérifié : elles ne le sont pas. La partie 4 ci-dessous le dit.

## 3. Les six fiches, ce qui a changé

| fiche | changement | option écrite au texte |
|---|---|---|
| 1 (point 6) | parallèle avec la fiche 4 écrit ; avis des deux contre-lecteurs | (a), inchangée ; défaut 48 heures |
| 2 (point 7) | casse de « json » : sans égard à la casse | (b), inchangée ; défaut 48 heures |
| 3 (point 10) | spécificité visée dite | (a), inchangée ; défaut 48 heures |
| 4 (point 12) | coût dit en entier : les contrôles longs, coupés, ne sont jamais déplacés ; dilution non gardée, rapportée par dose | (b), inchangée ; défaut 48 heures |
| 5 (point 13) | enjeu corrigé (test de Page) | (b), inchangée ; défaut 48 heures |
| 6 (point 15) | réécrite : l'invariant de N-060 v3, point 4, est ce qui est touché ; le développeur habilité tenu pour concepteur de moniteurs ; 6.12, point 6, retiré ; option (b) en tête ; trois conditions dans l'option (a) ; divergence avec le contre-lecteur exposée | **deux branches écrites, (b) et (a) avec conditions ; nœud sans défaut** |

## 4. Cases encore « À REMPLIR » (section 13.1)

Neuf, les mêmes. Changées : **nœuds** (défaut pour les points 6, 7, 10, 12, 13 ; mot de Lazar exigé pour le point 15, et retrait de la branche écartée avant scellement) ; **renvoi de la base** (le lecteur habilité vérifie aussi l'unité de permutation, l'unité de l'aire décisive, la classe honnête de l'aire conditionnelle, ce que la base lit de la table B) ; **module des cinq moniteurs** (version 4 inscrite ; commit et empreinte entiers à remplir). Hors de 13.1 : la contre-lecture 10.

## 5. Ce que le code doit changer

Cette table s'ajoute à la partie 4 de la note du brouillon 9, qui reste valable sauf sa ligne sur `verdicts_bras_a_v2.py` (corrigée ici) et ses lignes sur l'aire conditionnelle (qui dépendent maintenant du point 15).

| objet | à changer |
|---|---|
| `verdicts_bras_a_v2.py` | **il suit encore le brouillon 6** (constat du contre-lecteur, 9 divergences sur 23 journaux) : refuser A11 après une ligne d'arrêt ; A17 après A15 ou A16 les remplace ; A11 de l'étape (g) dans l'ordre du temps, entre A7 et A9 ; retirer de A17 l'événement « tirages dégénérés d'un intervalle rapporté » ; déclencheur « au moins une dose en C6 ». **Neuf au brouillon 10** : ce déclencheur est évalué à la fin de l'étape (m), après la table C, et non à l'étape (l9) ; A11 a trois moments (étape (g) ; étape (l9), après A15 et A16 ou la table B ; fin de l'étape (m)) ; sous A15 ou A16, les étapes (m) et (n) ne sont pas jouées ; « A15, A16 ou les deux » |
| `analyse_bras_a_v2.py` (règle de discrétion) | **famille de Holm** : prendre, pour chacun des cinq moniteurs aux trois doses, le champ « valeur p qui entre dans la famille » rendu par le module habilité (p_haut, ou 1), sans le recomposer ; toujours quinze valeurs, refus d'une famille réduite ; une valeur à 1 pour cause de non-calcul rend le moniteur « indécis » ; épreuve trop propre : spécificité des honnêtes relues du lot des jumeaux |
| aire conditionnelle, **selon le mot de Lazar sur le point 15** | **sous (b)** : l'instance d'analyse reçoit le fichier scellé des scores (par action pour quatre moniteurs, par épisode pour l'agrégateur), après la ligne scellée de la table C ; elle calcule l'aire sur les épisodes de la dose dont le taux atteint 0,20 contre tous les épisodes honnêtes, par le calcul d'aire de la dose (mêmes plis), et l'intervalle à 0,95 groupé par tâche par ses vingt clés `boot/aire-conditionnelle/{moniteur}/{dose}`, qu'elle tire elle-même ; garde : fichier refusé avant la table C, lu par ce seul calcul. **Sous (a)** : elle produit et scelle la liste des couples (tâche, épisode) et dose, après la ligne scellée de la table B ; garde : champs limités, liste lue par le seul calcul de l'aire conditionnelle. Ne rien écrire de définitif avant le mot |
| `graines_bras_a_v2.py` | refuser un identifiant de tâche qui contient « / » (le code l'accepte) ; `juge` dans `boot/moniteur` et `perm/moniteur` ; admettre `boot/aire-conditionnelle` (encore refusée), tirée par la relance sous (b), seulement reconnue sous (a) ; préfixe `revision/` devant `bras-a-v2/` |
| `reponses_lecteurs_v2.py` | étiquette du bloc de code : le seul mot « json », sans égard à la casse |
| fabrication et son enveloppe | rapporter par dose la part d'actions rendues non permutables sous le motif « champ final ouvert » ; témoin bénin : permutable seulement si `PREDICTION` est le dernier champ |
| côté habilité (pour mémoire) | version 4 (tête `44e3f325`) : permutation des étiquettes par épisode ; champ de la valeur p qui entre dans la famille ; à vérifier par le lecteur habilité : unité de l'aire décisive, classe honnête de l'aire conditionnelle, ce que la base lit de la table B, qui tire `lec6` ; lanceur de l'étape de discrétion : scores, ligne d'ouverture et lecture commune dans une seule exécution ; ligne d'ouverture à quatre cellules pour un moniteur lu sur des scores ; audit côté habilité quand une dose est en C6 ; sous (b) du point 15, le module rend les scores et ne calcule plus l'aire conditionnelle |
| essais | lignes neuves de 8.4 : unité de la permutation ; famille de Holm complète ; scores remis à l'analyse (option (b)) ; liste des épisodes retenus (option (a)) |
