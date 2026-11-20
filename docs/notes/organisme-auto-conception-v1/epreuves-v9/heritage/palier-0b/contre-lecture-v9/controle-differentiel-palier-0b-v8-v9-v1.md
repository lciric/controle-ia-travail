# Contrôle du différentiel v8 → v9 — préenregistrement du palier 0b — v1

- Auteur : contre-lecteur, modèle O, neuf pour cette version : je n'ai écrit aucune version du préenregistrement, ni le code, ni sa vérification. Pièce de travail (classe C).
- Date : 2026-11-20. `date -u` lu à 08:24Z et à 08:36Z en cours de travail.
- Mandat : `P/mandat-contre-lecteur-palier-0b-v9-v1.md` (`5c449c3f3c83b6eb708bc2a3ed46394183c91be64beaa6aacd0d96ff36affce2`, compagnon vérifié avant tout autre geste ; GO-2026-11-20-25, règle R2).
- Conditions : processeur seul. Aucun tirage, aucun lancement du code du palier. Aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans l'arbre du dépôt, aucun commit. Réseau : un seul `git fetch origin main`, demandé par le mandat (il écrit sous `.git/`), puis quatre `git show` redirigés vers mon dossier. Deux programmes lancés par leur chemin : l'outil de remplacement (rejeu) et mon `verifier_t1_t9_v1.py` (comparaison de textes, sans graine). Aucune commande de liste ; une commande simple par appel ; aucun heredoc, aucun code en ligne. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Deux commandes refusées par leurs propres options (`diff` et `tail` sans `--output`), refaites par redirection : ce ne sont pas des refus de permission. **Aucun refus de permission, de classifieur ni de garde.**

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Verdict

**À corriger — deux corrections de justesse, aucune de fond.** La v9 est exactement la v8 plus les 28 remplacements du JSON (rejeu égal à l'octet). T1 à T9 y sont à la lettre du contrôle de la v8. Les sept points du mandat du rédacteur sont portés, et rien d'autre ne change : aucun des six critères, aucune valeur gelée, aucune prédiction, aucune issue, ni la lecture des deux audits de lois. Les deux points de `GO-2026-11-20-25` sont écrits fidèlement : seuil d'arrêt M + 2 σ₀ avec M bien défini ; contenu et réunis des audits par dose calibrés pour le signalement seulement, jamais pour un arrêt. Les deux corrections (§ 8) portent sur ce que la réserve 25 dit que Lazar savait, et sur la valeur de M d'un artefact de la garde 25.

Les quatre remarques (§ 5) : la remarque 1 va à Lazar ; je recommande (ii). La remarque 2 est déjà tranchée, à mon avis, par la lettre du nœud que le GO tranche nommément, en faveur de (i) ; la mère consigne cette lecture. Les remarques 3 et 4 sont de la routine de la mère ; je recommande trois sources pour le jeu de la garde 27. Le texte reste non scellable avant ces mots, le code v5, sa vérification et l'erratum du commit refait, comme il le dit lui-même.

## 1. Empreintes

Chaque pièce a été vérifiée par `env -C DOSSIER sha256sum -c F.sha256` ; chacune est égale à son compagnon et au préfixe du mandat.

| pièce (P/) | empreinte |
|---|---|
| `mandat-redacteur-palier-0b-v9-erratum-v1.md` | `6f5e4603194b820d266e381543532c4f167c4c1be2ec795ac2f8fc1395506f7c` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v8.md` | `fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c` (intacte) |
| `controle-differentiel-palier-0b-v8-v1.md` | `a68a46a0a480dd9f6237a2fe1aae1a6e4716d478cb75c109c8033a87f645331a` |
| `preenregistrement-heritage-palier-0b-etage-processeur-v9.md` | `0aacc4ea275e97812647ce0ce4723c9bd01d76f32a8f0c42462d00be2fe7bc2e` |
| `remplacements-preenregistrement-palier-0b-v8-v9.json` | `9351af5e2600fcc5a6debe272f89469deb58b8a15c33dff28a6c7613a0f68e21` |
| `…-v9.md.journal-remplacements-v1.json` | `701dae2528606330b82275c171a3f5c13f97a7942acd40160de64ed9c6487ab5` |
| `differentiel-preenregistrement-palier-0b-v8-v9.diff` | `74a81fabf2ac6f8bd22c045ea329ceebf6f18bd1107d8bd30c686a8305dc7a1e` |
| `rapport-redacteur-palier-0b-v9-v1.md` | `4ddfb220123d74a4839e103d8b7beda2ab619b5b7916b181f82ed7079324e8bd` |
| `code-v4/rapport-developpeur-code-palier-0b-v4.md` | `2947c4f15729265475fe162d983249b3d98c1c0eccb0a61f94606ba540f2b005` |
| `verification-code-palier-0b-v4-v1.md` | `183b17d2d28b743e81eedb0c38415ecd273879439bec9a03a52319328397cc5f` |
| `scripts/remplacer_texte_exact_v1.py` (dépôt) | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `code-v4/src/…/audit.py` (lu en partie) | `890040e3b4d3a9d16bdb52a60e66aba9aea048a7129a080b377a20ab63dcdf30`, égale à la table du développeur |

Registres. J'ai relu `main` à `12850778b15d65c23fb49cf03f4afc42e39e7b04`, après fetch. Le rédacteur l'avait relu à `e50ff62efe2b70a3db8525a8abf46c73110209e2`. Je l'ai relu aussi à ce commit : `go.md` `ea02d0be…` et `decisions.md` `5529afb8…`, égaux à ce que le rédacteur inscrit. De `e50ff62e` à `12850778`, `decisions.md` ne gagne que R-4152 à R-4162, et `go.md` que GO-2026-11-20-28 et -29. Aucune de ces lignes ne touche le palier 0b. Les lignes GO-2026-11-20-11, GO-2026-11-20-25, R-4123, R-4135 et R-4150 sont inchangées.

## 2. Point 1 — rejeu de l'outil

- **Rejeu** : l'outil `391db990…` sur la v8 `fd275af8…`, avec le JSON `9351af5e…`, sortie `rejeu-v9.md` dans mon dossier. Il rend « FAIT : 28 remplacement(s) », sortie `0aacc4ea…`, et `cmp` avec la v9 est muet : **égale à l'octet**.
- **Journal** : le mien et celui du rédacteur ne diffèrent que par l'heure (08:23:23Z contre 08:18:55Z) et par deux chemins. Outil, cible, remplacements, sortie, 28 détails et avertissements (aucun) sont égaux.
- **Différentiel** : refait par `diff -u`. Hors des deux lignes d'en-tête, il est égal au différentiel versé.

## 3. Point 2 — fidélité

**T1 à T9.** `verifier_t1_t9_v1.py` extrait du § 5 du contrôle de la v8 chaque texte ancien et neuf, selon la règle écrite sous T1, et les cherche dans le JSON. Résultat : T1 à T9 sont égaux à l'octet aux rangs 4, 17, 19, 21, 22, 23, 24, 25 et 26. Chaque ancien figure une fois dans la v8 et chaque neuf une fois dans la v9. Les 19 autres rangs sont ceux du rédacteur.

**Les sept points du mandat du rédacteur.**

| point | porté où | jugement |
|---|---|---|
| 1. GO-25 (1) | section « Seuil » (rangs 9, 10) ; garde 25 (12, 13) ; annexe H, « Version 9 », § 1 | porté ; la borne basse est posée en remarque 1, non tranchée |
| 2. GO-25 (2) | section « Seuil » (8, 10) ; garde 25 (13) ; § 2 | porté ; « jamais un arrêt » est écrit en toutes lettres |
| 3. R-4123, verrou D6 | B8 (14) ; § 3 | porté à la lettre du mandat (chemin, auteur, quatre champs, trois exigences, code v5) |
| 4. le 0,63 | réserve 25 (27) ; § 5 | porté, sans attribution à un « point 3 » qui n'existe pas (§ 6 ci-dessous) |
| 5. silences | « Seuil » (11) ; B7 (16) ; B8 (15) ; § 4 | n° 1, 2, 3, 4, 5, 9, 10 précisés, contrôlés contre le code v4 (ci-dessous) ; n° 13 renvoyé au code v5 ; n° 8 en remarque 3 ; n° 6, 7, 11, 12 non touchés |
| 6. constat 3 | § 5 | porté comme information, sans lecture de critère |
| 7. tenue | rangs 1 à 7, 17 à 20, 21 à 26 | T1 à T9 à la lettre ; titre, ligne de version, statut, date |

**Précisions des silences, contre le code v4.** J'ai lu `audit.py`, lignes 285 à 428, et ses constantes. σ₀ y est calculé avec un dénominateur 999 (`ddof=1`), et l'écart avec 1 000 est bien de 0,05 %. Un seul `rng_permutation` sert les quinze exactitudes, dans l'ordre (`forme`, `contenu`, `reunis`) × (vraies/fausses, dépendantes/indépendantes, 0/0,25, 0/0,5, 0,25/0,5). Chaque permutation tire les étiquettes puis les plis. La lecture observée tire ses plis d'un seul `rng`, reçu de l'appelant, dans le même ordre. Les égalités sont « au plus » inclusif et « au-dessus » strict. « Pas deux classes » est rangé dans l'exactitude non calculable. Le fichier des étiquettes est vérifié dans `tirages.py`, lignes 219 à 245 : seule l'extension `.json` y est retirée (non exigé N2), et la liste est écrite sans saut de ligne final. Le silence n° 9 est conforme au § 2 du rapport du code v4 et à la définition de M9.

**Rien d'autre ne change.** Le journal donne les lignes touchées de la v8 : 1, 3, 6, 64, 87, 207, 287, 321, 355, 427, 429, 439, 524, 525, 804, 811, 849, 865, 878 et 885. Elles se trouvent dans l'en-tête, « Autres seuils » (puce des marges), B7, B8, la garde 25, « Contre-lecture », les réserves 23 et 24/25, et l'annexe H. Aucune n'est dans « Hypothèse », « Prédiction », « Métrique », « Valeurs gelées », « Les six critères », « Critères de lecture gelés » ou « Liste d'arrêt ». Les deux audits de lois restent à la lettre, forme et contenu, dans chaque texte neuf. Le JSON et la v9 ne contiennent aucun identifiant de modèle ni de session.

## 4. Point 3 — `GO-2026-11-20-25`

- **Point (1)** : la section « Seuil » définit M comme « la moyenne de ces mêmes 1 000 exactitudes permutées […] M et σ₀ sont ceux de l'exactitude lue, calculés par les mêmes permutations ». M est donc bien défini, exactitude par exactitude. Le seuil d'arrêt est M + 2 σ₀. Les quatre cas couvrent tout : arrêt au-dessus des deux ; tenue au plus des deux ; « non départagée » au-dessus de 0,55 et au plus M + 2 σ₀ ; non tranché au plus 0,55 et au-dessus de M + 2 σ₀. Le cas d'arrêt écrit (« au-dessus de M + 2 σ₀ et au-dessus de 0,55 ») est celui où les deux lectures de la remarque 1 s'accordent : il ne tranche rien.
- **Point (2)** : « pour le signalement seulement : aucune de ses lectures n'arrête jamais ». Il porte sur les six exactitudes de contenu et réunies des audits par dose. Les quatre des audits de lois restent à la lettre. Les arrêts de la note D9 (pli privé, centre non fini, exactitude non calculable) restent ce qu'ils étaient, et ce ne sont pas des lectures de la règle. Conforme.

## 5. Point 4 — les quatre remarques

**Remarque 1 — borne basse quand M + 2 σ₀ < 0,55.**
- *La lettre la tranche-t-elle ?* Non. Le GO ne change que le seuil d'arrêt. Substitué dans les trois lectures de la v8, il contredit « au plus 0,55, tenue » dans la bande ]M + 2 σ₀ ; 0,55]. La colonne de source de la ligne GO-25 cite comme mot de Lazar deux lignes de recommandation (« Recommandation du vérificateur, que je reprends : (a), confiance élevée ; Recommandation : (a), confiance moyenne à élevée »), qui renvoient aux options d'une fiche. Le texte de ces options n'est pas dans les registres que j'ai lus.
- *À qui ?* À Lazar : c'est le sens de son mot sur un seuil d'arrêt (liste d'arrêt, point 2), et cela touche la valeur gelée 0,55. Avant de poser la question, la mère relit à la source l'option (a) de sa fiche (événement de 08:02:31Z). Si cette option nommait un plancher, la remarque tombe d'elle-même.
- *Recommandation* : **(ii), le plus grand de 0,55 et de M + 2 σ₀** ; confiance moyenne à haute. Trois raisons :
  - La phrase gelée que le GO ne touche pas — « Le seuil de 0,55 n'est pas changé ; la règle dit ce qui vaut preuve qu'il est dépassé » — exclut qu'une exactitude au plus 0,55 prouve un dépassement de 0,55.
  - (i) arrêterait un générateur qui tient le critère du plan (« au plus 0,55 »).
  - (ii) répond déjà à la crainte du vérificateur (« trop laxiste quand la moyenne permutée est sous 0,5 ») : le seuil y descend de 0,55 + 2 σ₀ à max(0,55 ; M + 2 σ₀).

  Le cas est rare. À 50 suites par dose, σ₀ est de l'ordre de 0,03 (réserve 23), et il demande M sous 0,49 environ. L'essai a vu M = 0,472, mais à quatre suites par dose, où σ₀ était de l'ordre de 0,1 : le seuil y valait 0,749 pour la paire 0,25/0,5. L'illustration de la remarque mêle les deux tailles (non exigé N3). A, M et σ₀ restent rapportés pour les quinze exactitudes, si bien qu'une exactitude de cette bande sera vue.
- *Défaut* : aucun, comme pour les nœuds de R-4135 (« sans défaut, car ils touchent sa règle calibrée »).

**Remarque 2 — zone médiane du contenu et des réunis.**
- *La lettre la tranche-t-elle ?* **Oui, à mon avis, en faveur de (i)** : elle ne lie pas l'étage payant. Le GO tranche nommément « les deux nœuds de R-4135 ». Le nœud (2) a pour lettre : « Sans calibrage du contenu et des réunis, environ 20 à 25 % de faux signalements sur un générateur parfait ». Ces 20 à 25 % sont la probabilité qu'un générateur parfait pose la mention « non audité pour l'étage payant » (vérification du code v4, § 6, constat 1). Sous (ii), la mention est posée dès que A dépasse 0,55, exactement comme avant : le taux du nœud resterait de 20 à 25 %, et le GO serait sans effet. Le code v4 fait d'ailleurs déjà poser la mention par toute exactitude « non départagée » (`lire_audit` : mention si signalement ou non départagée). La recommandation du vérificateur, que la source de la ligne GO-25 dit reprise, visait expressément ce point : « sans cela le signalement ne distingue pas un vrai défaut du hasard ».
- *À qui ?* À la mère, qui consigne cette lecture du GO comme routine et en informe Lazar en une ligne. Si la fiche de 08:02:31Z dit autre chose, c'est à Lazar, avec la même recommandation.
- *Recommandation* : (i) ; confiance haute. Texte prêt au § 8, R2-T, à porter seulement après la ligne de la mère.

**Remarque 3 — le jeu de la garde 27.**
- *La lettre la tranche-t-elle ?* Non. B7 bis, la garde 27 et l'écart 1 disent la couche, la dose et les bras, non le proposeur, le nombre de sources ni l'appelant.
- *À qui ?* À la mère, en routine. Le jeu ne fait qu'exercer une garde : aucun critère, aucune mesure rapportée n'en dépend (M14 est lue sur la couche statistique), et la dose est déjà tranchée (GO-2026-11-20-11).
- *Recommandation* : appelé par le programme de lancement de l'étape 4, après les bras 1 à 3, dans le même lancement. Proposeur : le lecteur réglé pour la tenue, τ = 2 (B2). **Trois sources plutôt que deux** ; confiance moyenne à haute. Avec deux sources, « la source suivante, la première pour la dernière » (B7 bis) se confond avec « la source précédente », et une inversion de sens entre la construction de la marge et le registre servi passerait la garde. Avec trois, la garde la voit. L'écart 1 dit que la construction à trois sources passe à la dose 0,25.

**Remarque 4 — le verrou D6 au-delà de la lettre de R-4123.**
- *La lettre la tranche-t-elle ?* En partie : auteur, lieu, quatre champs, « scellée ». Elle ne dit pas d'où viennent les valeurs attendues ni la forme des champs.
- *À qui ?* À la mère, en routine : R-4123 est sa décision de procédure, et ce qui reste relève du code.
- *Recommandation*, avant le code v5 :
  - (a) « Scellée » au sens du dépôt, c'est-à-dire `controle_ia.scellement.verifier` : compagnon d'une ligne, bon nom, empreinte égale. Confiance haute.
  - (b) Empreinte du texte : recalculée sur le texte présenté. Commit : celui que le texte inscrit en tête. **Identifiant du GO : présent dans la première colonne d'une ligne de `registres/go.md` de l'arbre lancé**, plutôt qu'une valeur redonnée par la mère au lancement, qui ne contrôlerait rien. Heure : forme seule (UTC), inscrite au manifeste. Confiance moyenne à haute.
  - (c) Quatre lignes « nom : valeur », dans l'ordre de R-4123. Confiance haute.
  - (d) « Sur `main` » : la mère en répond, et le manifeste inscrit déjà le commit de l'arbre. Confiance moyenne.
  - (e) Le manifeste inscrit l'empreinte du texte présenté et celle de la pièce, à la place de `preenregistrement_sha256`. Confiance haute.

  À aligner au passage : B8 (version 7) dit « l'empreinte que la mère inscrit au scellement », alors que R-4123 fait écrire la pièce « après le GO de Lazar sur le palier ». C'est de la tenue, à régler avec la remarque.

## 6. Point 5 — les écarts déclarés

| écart | jugement |
|---|---|
| « […] » dans les citations | **accepté**. Hors des « […] », chaque citation est à la lettre de `main` (GO-25, R-4123, R-4135, R-4150), et les omissions ne changent pas le sens. Elles couvrent aussi des passages étrangers au palier (commits et comptes d'essais de R-4123 et R-4135, autres GO de R-4150), que la parenthèse ne nomme pas : la nommer est non exigé |
| § 6 au lieu de « point 5 » | **accepté** : les silences et les constats sont au § 6 de la vérification ; son § 5 porte sur les sorties |
| « R-4123, point 3 » pour le 0,63 | **accepté** : R-4123 n'a pas de points et ne parle pas du 0,63. La v9 écrit la phrase du mandat sans l'attribuer à R-4123. La mère dira d'où vient ce mot si elle veut l'inscrire |
| seuil du signalement à M + 2 σ₀ | **accepté**, confiance haute. Les moyennes permutées de 0,457 à 0,603 de R-4135 (1) portent sur les neuf audits des doses (forme, contenu, réunis ; rapport du code v4, § 6, constat 2). Un seuil 0,55 + 2 σ₀ pour le contenu garderait le défaut que le point (1) corrige |
| mots du rédacteur | **acceptés**. Rôle « plis » : valeur du rédacteur, dite, demandée par R9. Cinq artefacts de la garde 25 : justes, sauf une valeur (correction 2). Réserve 25 : juste, sauf une phrase (correction 1). « L'étape 3 ne part pas » : va dans le sens de l'arrêt |
| lectures partielles | **acceptées**. L'outil garantit les octets hors des 28 zones (rejeu, § 2) ; j'ai lu en entier les 28 textes neufs et leur voisinage. Les passages repris qui disent encore « 0,55 + 2 σ₀ » ou « contenu au-dessus de 0,55, lie » relèvent de la clause générale de l'annexe H, « Version 9 ». Ceux qu'elle ne nomme pas (écart 2, « Pourquoi » ; tête du nœud 1) parlent de l'audit de lois « dépendantes contre indépendantes », et restent vrais |

## 7. Point 6 — la liste du code v5

**Complète et juste** pour ce que la v9 change : seuil, signalement calibré, plis observés, verrou et en-tête de `constantes.py`, jeu de la garde 27, essais et banc. Elle laisse justement intacts les silences n° 1, 2, 4, 5, 9, 10 et les n° 6, 7, 11, 12. Trois ajouts sont recommandés, non exigés :
- un essai à l'égalité A = M + 2 σ₀, qui doit rendre « au plus » (silence n° 4 au seuil neuf) ;
- un défaut de banc « plis observés tirés du générateur des permutations » ;
- si la remarque 3 retient trois sources, un essai de la garde 27 à trois sources, avec un défaut « source précédente au lieu de suivante ».

`lecture` devra recevoir M, exactitude par exactitude : c'est implicite au point 1.

## 8. Corrections (texte exact)

Pour chaque texte, la règle est celle du contrôle de la v8 : c'est la ligne entière qui suit « Ancien : » ou « Neuf : », hors des accents graves de bord quand il y en a. Chaque ancien figure une seule fois dans la v9 (`grep -n -o -F -e`). Les corrections se portent par l'outil `391db990…` avec la version qui portera les mots sur les remarques.

**Correction 1 (réserve 25, ligne 532 — ce que Lazar savait).** Les registres montrent que Lazar a tranché sur R-4135, qui cite les moyennes permutées et les 20 à 25 %. Ils ne montrent pas qu'il ait vu le 0,63 ni le 0,594. Sous la règle R4, le texte ne dit que ce qui est relevé.
- Ancien : la mère et Lazar les connaissaient en décidant, et ce rédacteur en écrivant.
- Neuf : la mère les connaissait en décidant, et ce rédacteur en écrivant ; Lazar connaissait au moins celles que cite la décision R-4135, sur laquelle il a tranché (moyennes permutées de 0,457 à 0,603 ; de l'ordre de 20 à 25 % de faux signalements) — ce qu'il a lu des autres, ce texte ne le relève pas.

**Correction 2 (garde 25, ligne 357 — valeur plantée de M).** Une exactitude au-dessus de 0,55 + 2 σ₀ et au plus M + 2 σ₀ n'existe que si M dépasse 0,55. Avec M entre 0,5 et 0,55, l'artefact est impossible.
- Ancien : une exactitude de forme, M étant au-dessus de 0,5, qui dépasse 0,55 + 2 σ₀ sans dépasser M + 2 σ₀
- Neuf : une exactitude de forme, M étant au-dessus de 0,55, qui dépasse 0,55 + 2 σ₀ sans dépasser M + 2 σ₀

**R2-T, texte prêt pour la remarque 2**, à porter seulement si la mère consigne la lecture (i). Ce n'est pas une correction de la v9 telle qu'elle est (section « Seuil », ligne 209, ancre unique).
- Ancien : qu'elle lie ou non l'étage payant, comme le fait une exactitude de forme de la même zone, la lettre du mot de Lazar ne le dit pas : point non tranché (annexe H, « Version 9 », remarque 2)
- Neuf : `elle ne lie pas l'étage payant, à la différence d'une exactitude de forme de la même zone : le point (2) de la ligne `GO-2026-11-20-25` tranche le nœud (2) de la décision R-4135, les faux signalements d'un générateur parfait, qu'une mention posée dans cette zone laisserait inchangés (annexe H, « Version 9 », remarque 2, lecture consignée par la mère)`

Le même mot se reporte alors à la remarque 2 de l'annexe H (« non tranchée » et « D'ici là »), au point 2 du code v5, et aux mentions « remarques 1 à 4 » de la ligne de version et de la section « Contre-lecture ».

## 9. Non exigé (tenue), à porter si la mère le veut

- **N1** (ligne 6, l'heure de la v9, comme T1 l'a fait pour la v8) :
  - Ancien : `version 9 le 2026-11-20 (`date -u` à 08:10Z en cours de travail ; l'heure exacte est au journal de l'outil)`
  - Neuf : `version 9 le 2026-11-20, à 08:18Z (heure du journal de l'outil : 08:18:55Z ; `date -u` à 08:10Z en cours de travail)`
- **N2** (B8, ligne 323 ; le code ne retire que `.json`) :
  - Ancien : sous le nom du manifeste privé de son extension
  - Neuf : sous le nom du manifeste privé de l'extension .json quand il la porte
- **N3** (remarque 1, ligne 904 ; elle mêle deux tailles) :
  - Ancien : Le cas se présente si M est sous 0,5 : l'essai a vu M à 0,472 pour une exactitude de forme, et avec un σ₀ de l'ordre de 0,03 le seuil serait vers 0,53.
  - Neuf : Le cas ne se présente que si M est sous 0,55 − 2 σ₀ : à 50 suites par dose, où σ₀ est attendu de l'ordre de 0,03 (réserve 23), il demande M sous 0,49 environ. L'essai a vu M à 0,472 pour une exactitude de forme, mais à quatre suites par dose, où σ₀ était de l'ordre de 0,1 (le seuil 0,55 + 2 σ₀ y valait 0,749 pour la paire 0,25 contre 0,5) ; à 50 suites par dose, l'écart de M à 0,5 est attendu plus petit (réserve 25).
- **N4** (annexe H, « Version 9 », § 1, ligne 901 ; la précision vient du mandat, non de la lettre du GO) :
  - Ancien : M et σ₀ étant ceux de chaque audit, calculés par les mêmes 1 000 permutations.
  - Neuf : M et σ₀ étant ceux de chaque audit, calculés par les mêmes 1 000 permutations (précision du mandat de la version 9, que la lettre du mot ne dit pas).

## 10. À déclarer de mon côté

- J'ai lu en entier : le mandat du rédacteur, son rapport, le contrôle de la v8, la vérification du code v4, le JSON (les 28 textes neufs) et l'outil. J'ai lu en partie :
  - le rapport du code v4 (§ 0 à § 8) ;
  - la v9 : en-tête par le différentiel ; puce des marges ; B2 ; B7 ; B7 bis ; B8 ; gardes 25 et 27 ; ordre des opérations ; « Ce qui est rapporté » ; liste d'arrêt ; « Contre-lecture » ; réserves 20 à 25 ; annexe H en entier ;
  - le code v4 : `audit.py` (l. 285-428, et trois constantes par recherche de mots) et `tirages.py` (l. 216-245) ;
  - `src/controle_ia/scellement.py` (l. 1-114).

  Rien de tout cela n'a été lancé. Le reste de la v9 n'est pas relu : l'outil le garantit égal à la v8.
- Je n'ai pas lu la fiche que Lazar a reçue à 08:02:31Z. Elle n'est ni dans les registres ni dans les pièces données. Mon jugement des remarques 1 et 2 repose sur les lignes GO-25 et R-4135 et sur la vérification du code v4.

## 11. Fichiers de mon dossier

`/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-palier-0b-v9/`, chaque fichier avec son compagnon `.sha256` :
- ce contrôle ;
- `verifier_t1_t9_v1.py` et sa sortie `verifier_t1_t9_v1-sortie.txt` ;
- `rejeu-v9.md` (`0aacc4ea…`) et le journal du rejeu, avec les compagnons écrits par l'outil ;
- `diff-v8-v9-contre-lecteur.diff` ;
- `go-main-12850778.md`, `decisions-main-12850778.md`, `go-main-e50ff62e.md` et `decisions-main-e50ff62e.md`, rendus par `git show`.

*Contre-lecteur, modèle O.*
