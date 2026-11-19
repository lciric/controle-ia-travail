# Vérification courte des versions 2 de la lecture de Yu et al. (2026) — v1

## En-tête

- **Qui écrit** : le contre-lecteur des versions 1 (modèle Opus 5.5, `claude-opus-5-5`), auteur de `contre-lecture-lecture-yu-v1.md` (`97ac990c…bb9f`). Il n'a écrit aucune des versions 2.
- **Heures** (`date -u`) : début 2026-11-19T07:27:00Z ; écriture à partir de 07:28Z.
- **Empreintes vérifiées** (`sha256sum`, toutes conformes) : `lecture-yu-approfondie-v2.md` `95684255…b8e48f` ; `memoire-retrospective-auto-conception-v2.md` `c490f941…dfcf6f` ; `courriel-auteurs-brouillon-v2.md` `aa13a20b…81b8e` ; `differences-v1-vers-v2.md` `f720f40f…b97764`.
- **Méthode** : `diff` fait par moi entre chaque version 1 et sa version 2 (note : 36 blocs ; mémoire : 14 ; courriel : 4), lu bloc par bloc, puis comparé à la liste des différences. Comparaison par programme de ma rédaction corrigée (1 050 caractères) avec la note v2. Pages revues sur les PDF empreintés : Yu et al. p. 2, 5, 6, 10, 20, 21, 23, 24 ; SkillHone p. 4, 6 ; Meta-Harness p. 5, 15. Décisions relues : N-053 point 5, N-058 (définition de l'oracle), N-045 v2 énoncés 2 et 5.
- Aucune dépense, aucun réseau, aucune réponse de modèle lue, aucun fichier interdit ouvert. **Aucun refus d'outil.**

---

## 1. Les onze corrections, et rien d'autre dans (a), (b), (d)

**Confirmé.** Chacun des 36 blocs du `diff` de la note figure dans la liste des différences, au bon endroit. Aucun changement non annoncé dans (a), (b) ou (d).

| correction | état dans les versions 2 |
|---|---|
| 1 « sans aucune mémoire » | portée : a.1 (deux endroits), a.2 point 1, a.8, (b) 1 ; rédaction remplacée |
| 2 la question est posée (p. 2) | portée : a.2 point 1, (b) 1, premier tiret, avec la citation exacte de la p. 2 |
| 3 « six travaux » | portée : (b) 1, dernier tiret |
| 4 concepteur fort des voisins | portée : a.6 (paragraphe neuf) et réserve 5. Citation neuve vérifiée : « the proposer P is Claude Code [4] with Opus-4.6 » (Meta-Harness p. 5). L'ajout « aucun de ces PDF ne compare Claude Opus 4.6 à Gemini 3.8 Flash » est juste. |
| 5 ablation confondue de SkillHone | portée : a.7, avec la citation exacte de la p. 6 |
| 6 date de SkillHone | **portée, pas mot pour mot** : « déposé en juin 2026 d'après son identifiant » est écrit, mais « 7 juin » est gardé, dit pris à l'interface d'arXiv, hors pièce empreintée. C'est acceptable : la provenance est dite et ce n'est pas un chiffre opposable. Remarque seulement. |
| 7 A2 | portée (mémoire v2) |
| 8 D1, D2 | portée (mémoire v2), avec les lignes 11 des deux devis |
| 9 compte | porté (mémoire v2 et note c.10) |
| 10 renvois à N-045 v2 et failles du plan | portée : c.2 à c.11 (jugée au point 3) |
| 11 courriel | portée (courriel v2, question 4 ; note (d)) |

**Ajouts annoncés hors des corrections** : les quatre remarques sans correction exigée (tableau 7, p. 18, « changée », « +1--3pp ») et la section « Corrections contestées ». Tous sont exacts.

## 2. La rédaction proposée pour N-073, et la précision du lecteur

- **Mot pour mot : confirmé.** Ma rédaction (point 8 de ma contre-lecture, 1 050 caractères) se trouve telle quelle dans la note v2, § (b) 1.
- **La précision est juste (p. 6, p. 8, p. 10, p. 20, p. 23, p. 24).**
  - Les comparaisons principales comptent dix réglages : six changements de banc et quatre changements de modèle (p. 2, p. 6). Trois de ces réglages sont en code : AHE et Terminus-2 au tableau 5 (p. 23), AHE au tableau 6 (p. 24).
  - « Each main cross-dataset and Opus-to-Gemini condition uses one complete RSI run » (p. 20). Ces trois réglages de code sont donc des courses uniques, hors des dix paires de l'étude appariée (p. 8). La ligne Terminus-2 du tableau 5 n'est d'ailleurs aucune des dix paires.
  - « Dans les autres réglages » peut se lire « dans les autres domaines ». C'est même ce que suggère la phrase du papier « the other domains are evaluated with one run per condition » (p. 10) : ma formulation laissait croire que tout le code est répété, ce qui est faux.
  - Le bras « causes seules » n'existe que dans ces dix réglages. Il faut donc aussi le rattacher à eux.
- **Rédaction finale que je soutiens** :
  « Yu et al. (2026) demandent si l'expérience acquise pendant une optimisation source aide à poursuivre l'optimisation après un changement de banc ou de modèle (p. 2). Ils comparent, depuis le même harnais évolué, une procédure complète — mémoire d'amélioration héritée de la source puis tenue à jour pendant la cible — à la continuation sans cette mémoire, qui garde l'historique ordinaire de la course cible. La comparaison est faite une fois par condition dans les dix réglages des comparaisons principales, code compris, avec aussi un bras qui ne garde que les causes (p. 6, p. 20) ; elle est répétée sur dix paires dans un seul réglage de code (p. 8). Ils écrivent que leurs comparaisons évaluent la procédure entière, héritage et mises à jour ensemble (p. 10). Nous posons, pour des découvertes plutôt que pour le score d'un harnais, la question de l'héritage séparé de la tenue : l'archive héritée cause-t-elle les découvertes, au-delà du fait de tenir une archive ? Nous ne la disons ni nouvelle ni propre : plusieurs travaux voisins cités par Yu et al. (p. 3, p. 15-16) n'ont pas été lus sur ce point. »

## 3. La proposition (c) refaite

Les six failles de mon point 10, une à une :

| faille | fermée ? |
|---|---|
| `retenue` porteur du verdict du juge | **fermée dans son principe** : le champ devient `gardee`, décidé par programme sur l'oracle et le coût, et absent si ce qui est gardé dépend du juge. **Rouverte ailleurs** par l'invariant (voir a ci-dessous). |
| historique de la source | **fermée** : règle 2, remise à zéro dans les trois bras, garde de lancement (R5). Le bras de diagnostic D-c rend ce canal mesurable. |
| retour de l'oracle inégal entre bras | **fermée** (règle 3, même grain dans les trois bras), **sous une condition non établie** (voir c ci-dessous). |
| fuite de la clé par la prédiction | **fermée pour les identifiants** (c.3 bis, c.7 point 4). **Pas entièrement pour le nombre d'items** (voir b ci-dessous). |
| entrées fausses dans les bras du critère | **fermée** : elles ne vont que dans le bras D-d. |
| fuite entre bras | **fermée** : règle 7, dossiers séparés, même suite de mondes, graines des mondes communes. |

La multiplicité et les deux renvois à N-045 v2 sont aussi traités : règles 4 et 5, longueur K ≥ 3 « choix repris », section c.5 bis. Cinq choses ont été ouvertes ou laissées par les corrections.

**a. L'invariant « aucune valeur de la mémoire n'est fonction d'une sortie du juge » contredit l'oracle lui-même.**
- N-058 définit l'oracle du monde planté comme « structures retrouvées, **témoins plantés vrais promus et faux rejetés** ». Promus et rejetés **par le juge** : une part de l'oracle est donc une sortie du juge.
- Les champs `resultat` (score de l'oracle) et `gardee` (règle sur ce score) sont alors, par construction, fonction d'une sortie du juge. L'invariant tel qu'écrit est violé par le plan même, et l'essai de code qui le « garde » ne peut pas passer honnêtement.
- Plus largement, tout ce que l'organisme écrit dépend de ce qu'il a lu, qui peut dépendre du juge : l'invariant pris à la lettre n'est pas testable.
- À écrire autrement, au choix :
  - (i) la mémoire n'emploie que la composante « structures retrouvées » de l'oracle, appariée par programme, sans le volet des témoins jugés ;
  - (ii) ou l'invariant est restreint à « aucun champ n'est calculé à partir d'un verdict ou d'un score du juge **sur les fiches de l'agent** », lecture conjointe de N-053 point 5 et N-058 point 2 (l'interdit porte sur la sélection d'agents sur le verdict du juge).
- Dans les deux cas, le texte doit dire laquelle des deux et ce que l'essai teste.

**b. La prédiction réduite au signe et à une tranche.**
- **Falsifiable, oui, mais à peine en l'état.**
  - Une « règle de score propre » exige une prévision **en probabilités**. Un signe et une tranche sont une catégorie ponctuelle : le texte doit demander une probabilité par tranche, sinon dire « justesse » et non « score propre ».
  - Le taux de base par permutation entre tentatives d'une même génération est **dégénéré** si les proposeurs prédisent presque toujours « plus » : permuter des prédictions identiques ne change rien, la justesse égale le taux de base par construction et le test ne peut rien dire. Il faut un taux de base qui ne dépend pas des prédictions (fréquence observée des signes, prévision constante).
  - Le « changement du score de l'oracle » dû à **une tentative** n'est pas défini quand le monde change à chaque génération (N-049, c.7 point 4). L'écart d'une génération à l'autre mêle la tentative et la difficulté du monde neuf. Sans évaluation de l'organisme avec et sans la tentative sur le même monde (coût en plus), la prédiction n'a pas d'objet mesurable propre.
- **Clé de l'oracle** : la prédiction elle-même ne livre rien de neuf, puisqu'elle porte sur l'agrégat déjà servi. Mais l'agrégat servi par la règle 3 peut livrer le **nombre** d'items plantés par son grain : un score de la forme k/m laisse lire m. Cela contredit c.7 point 4 (« aucun nombre d'items plantés n'est … servi »). À trancher : arrondir ou bruiter le score servi, ou accepter que m soit connu et le dire.

**c. La règle 3 suppose que l'organisme reçoit déjà le score de l'oracle.**
- Si le retour ordinaire de l'organisme est aujourd'hui le score de développement rendu par le juge (N-045 v2, énoncé 2), servir le score de l'oracle aux trois bras **change l'organisme** : il s'optimise alors contre l'oracle sur les mondes d'évolution.
- C'est permis (mondes neufs, mesure finale tenue à l'écart, N-050), mais c'est un changement à déclarer. Non vérifié ici : je n'ai pas lu le code de l'organisme.

**d. La procédure de Holm avec le test des rangs signés exact : un plancher sur le nombre de sources.**
- Avec n sources et aucune différence nulle, le plus petit p bilatéral atteignable est 2 / 2^n : n = 5 donne 0,0625 ; n = 6, 0,03125 ; n = 7, 0,0156 ; n = 8, 0,0078 ; n = 10, 0,00195.
- Par Holm, la plus petite des deux valeurs p doit passer sous 0,025. **Avec n ≤ 6, le plan ne peut conclure sur aucun contraste, quel que soit l'effet.** Avec n = 7, il ne conclut que si les sept différences ont le même signe.
- Les scores de l'oracle sont discrets : des différences nulles sont probables et réduisent le n effectif. Le traitement des zéros doit être gelé (retrait, ou méthode de Pratt).
- Le préenregistrement doit donc poser un **plancher n ≥ 7, en pratique de l'ordre de 10 ou plus**, quel que soit le résultat du pilote de bruit. Le texte actuel fait dépendre n du seul pilote.
- Ordre de grandeur, qui n'est pas un devis : une génération de la course jouée a coûté ≈ 45 USD pour la seule étape « proposition ». Trois bras × 10 sources × 3 générations donnent déjà ≈ 4 000 USD avant la mémoire, le pilote et les bras de diagnostic.

**e. Mineur** : la règle 6 retire des lots « uniformément sur toutes les espèces ». Avec 11 lots par espèce, le retrait est entier : la règle d'arrondi doit être gelée.

**Verdict du point 3** : les six failles sont fermées ou presque. Le plan v2 ne peut pas fonder un préenregistrement avant que soient réglés : (a) l'invariant contre l'oracle de N-058 ; (b) la forme de la prédiction et son taux de base ; (d) le plancher du nombre de sources. Le lecteur le dit lui-même, aucune de ces choses n'est engagée : la proposition (c) reste une proposition.

## 4. Le compte de la mémoire rétrospective v2

**Confirmé.**

| | justes | fausses | non vérifiables |
|---|---|---|---|
| à ± 20 % | 6 (C3, C4, D2, D3, D4, E2) | 3 (A1, A3, D1) | 5 (A2, A4, B1, D5, F2) |
| à ± 10 % | 5 (C3, C4, D3, D4, E2) | 4 (A1, A3, D1, D2) | 5 (A2, A4, B1, D5, F2) |

- Sans A1 et E2 : 5 / 2 / 5 à ± 20 % et 4 / 3 / 5 à ± 10 %. Je refais ces deux comptes et je trouve les mêmes.
- « Problème A : deux tranchées, deux fausses, deux intranchées » : exact.
- La règle neuve (« une attente jamais jouée est non vérifiable » ; « un devis se compare à la même étape ») est appliquée de façon uniforme.
- C2 est corrigée comme je le demandais.
- Les nombres D1 (28,32 ; 53,31 ; + 58 %) et D2 (47,26 ; − 10,4 % ; 47 appels sur 55) concordent avec les devis et PO-177 (44 appels d'Opus, Fable, Argon et Astra, plus 3 de Carbon, font 47).
- La phrase « le compte de la version 1 se retrouve par hasard à ± 10 %, par d'autres classements » est exacte.

## 5. Le courriel v2

**Confirmé.** Seule la question 4 change, avec ma correction mot pour mot : « no SIM … (it keeps the ordinary target-run history D_t) » ; « The closest comparison … initial run from the seed harness rather than after a transfer (Appendix C.5), and is a single run ». Le renvoi à l'annexe C.5 est juste : la phrase de la p. 21 est dans la section C.5. Le reste est identique à la version 1, que j'avais trouvée exacte. Aucune donnée personnelle ni identifiant de session dans le corps.

---

## Conclusion

Les versions 2 peuvent fonder la décision sur la revendication, avec la rédaction finale du point 2 (« dans les dix réglages des comparaisons principales, code compris ») ; la proposition (c) ne peut pas encore fonder un préenregistrement, avant correction de l'invariant face à l'oracle de N-058, de la forme de la prédiction et de son taux de base, et du plancher de sept sources ou plus imposé par la procédure de Holm.
