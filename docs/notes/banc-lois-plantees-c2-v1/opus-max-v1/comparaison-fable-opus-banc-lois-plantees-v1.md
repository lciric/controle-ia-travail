# Comparaison — banc à lois plantées : conception de Fable 5.2 (v2) et réponse d'Opus 5.5 en effort maximal (v1)

- **Nature** : classe C (travail). Comparateur neuf : Claude Opus 5.5 (`claude-opus-5-5`), le 21 novembre 2026. Il n'a écrit aucune des deux pièces. Aucun appel payant, aucun commit.
- **Grille scellée avant toute lecture** : `grille-comparaison-banc-lois-plantees-v1.md`, `b87c2f11f22050321e88a2bd23f2d7c2b6a3173b1b42a010418870963020b71f`.
- **Pièces lues** (empreintes conformes à leurs compagnons, `sha256sum -c`) :
  - Fable v2 : `../conception-fable-banc-lois-plantees-v2.md` (`62c519c0…64aa`), lue en entier ; sa sortie de calculs v2 (`6bb7f5a5…21f2`), blocs A, B et J.
  - Contre-lecture de la v1 (`122f2afd…6b8e`, verdict « à corriger », 0 bloquant) et vérification des corrections de la v2 (`verification-corrections-banc-lois-plantees-v2-opus-v1.md`, verdict « conforme », quatre remarques mineures R1 à R4).
  - Opus max : `reponse-opus-max-banc-lois-plantees-v1.md` (`a8a0ef02…d912`), lue en entier ; sa sortie de calculs (`ce7e9f67…9c8e`), blocs A, C et D.
- **Cloisonnement** : aucun chemin interdit n'a été ouvert. J'ai relu une seule ligne de décision, le point 4 de `docs/decisions/decision-N-060-v3.md` (ligne 33), pour trancher la contradiction 2.

## 1. Chiffres vérifiés à la page

Le texte des PDF a été extrait par `pdftotext` dans mon bloc-notes. Chaque PDF est vérifié contre son empreinte compagnon.

| réponse | chiffre ou citation | source, page | état |
|---|---|---|---|
| Fable | « Labels are behavioural: they cannot separate a deliberate shortcut from confusion » | 2611.00407v1 (`b37f97b2…c5a7`), p. 4 | exact |
| Fable | 60 épisodes, 14 tentatives de triche | 2611.00407v1, p. 1 | exact |
| Fable | meilleure aire sous la courbe 0,77 ; « one human attacker (the lead author) » | 2604.16286v2 (`833a48e6…1cc0`), p. 1 et p. 3 | exact |
| Fable | DiscoveryWorld, cinq graines, de zéro à quatre | 2406.06769v2 (`docs/sources/pdf/percee-controle-securite-v1/`), p. 5 | exact |
| Fable | 324 tâches, 12 domaines (NewtonBench) ; 14 scénarios (CausalGame) ; « Prior-only, Fixed, and Adaptive » (SciGame) | 2510.07172v2, 2607.04293v1, 2610.37919v1, p. 1 | exact |
| Fable | 1,55 fois le budget pour réfuter une loi fausse à la limite ; 0,12 % ; aire 0,694 et 2,330 lois | sortie v2, l. 18, 43 et 312 | exact (1,546) |
| Opus | moniteur 8B à 0,64, Gemini 3.1 Flash-Lite à 0,80 ; « A two-rule deterministic check caught every known exploit » | 2611.00407v1, p. 1 | exact |
| Opus | « not validated quantitatively against human judges » | 2606.08892v3 (`8858355c…4beb`), p. 10 | exact |
| Opus | sondes qui signalent 99 % des ajustements bénins | 2611.14950v1 (`6396abd5…94d6`), p. 1 | exact |
| Opus | sondes appariées qui ne transfèrent qu'à 1 entraînement sur 5 | 2611.14950v1, p. 3 | **incomplet** : la page dit 1 sur 5 avec une recette bénigne, et 2 sur 5 avec trois |
| Opus | « The novice agent is always gpt-4o » | 2501.01540v2, p. 9 | exact |
| Opus | auditeurs humains à 0,59, meilleur modèle à 0,73, 10 traces bénignes et 12 sabotées | 2611.21832v2, p. 1 | exact |
| Opus | 0,92 % contre 31,1 % ; 1,10 % contre 29,9 % ; commission 0,07 à 0,14, omission 1,02 à 1,12 ; banc 39 à 203 USD, juge de pointe 332 USD | sortie Opus, l. 11, 64-66, 98-101, 139 et 151 | exact |

## 2. Notes par critère (0 à 5)

| critère | Fable v2 | Opus max | motif |
|---|---|---|---|
| 1. Chiffres à la page | 5 | 4 | Tous les chiffres de Fable que j'ai vérifiés sont exacts. Opus a une citation tronquée, celle du « 1 sur 5 ». |
| 2. Profondeur | 5 | 4 | Fable a un prototype à treize épreuves qui trouve trois défauts contre sa propre v1. Opus pose un cadre statistique propre, mais sur des modèles jouets gaussiens. |
| 3. Originalité | 4 | 5 | Fable apporte la règle de cohérence, le devin conditionné à la fiche, les doses au niveau des gestes et l'oracle dégradé à q connu. Opus apporte l'appariement à deux niveaux, le jumeau à traitement égal, le flou par composante, le dommage égal par une règle d'analyse, l'attribution par acte, la balise publique et le certificat. |
| 4. Honnêteté et R8 | 5 | 4 | Fable écrit contre lui-même et baisse ses chances. Opus déclare avoir lu R-4577, mais généralise trop « à peine flou pour la commission » (contradiction 1). |
| 5. Règles et nœuds | 4 | 5 | Opus voit le conflit avec l'invariant de l'oracle et la divergence entre N-058 et N-060 v3. L'épreuve 12 de Fable heurte cet invariant. |
| 6. Actionnabilité | 4,5 | 4,5 | Fable donne une table d'épreuves avec leur état, fait ou à faire. Opus donne douze critères de mort, cinq premiers pas et des défauts écrits. |
| 7. Coût | 4 | 4 | Les deux chiffrages sont supposés et cohérents par épisode (contradiction 5). |
| 8. Ce qui manque (note haute = peu de manques) | 3,5 | 3 | Voir la section 3. |

**Qui l'emporte.** Fable l'emporte comme base : sa réponse est plus profonde, ses chiffres sont exacts, et il a trouvé lui-même des défauts au banc. Opus l'emporte sur la conformité aux règles du programme et sur le dessin statistique. Quatre de ses pièces manquent à Fable et lui sont nécessaires.

## 3. Ce que chacune a que l'autre n'a pas

**Seulement chez Fable.**
- La forme de la fiche laisse deviner la vérité : aire de 0,694, et 2,33 lois au lieu de 1,80 (bloc J). L'agenda fermé de la v1 d'Opus, avec ses candidates « fausses plausibles par construction », est exposé à cette même fuite, et Opus ne la voit pas.
- Aucun handicap essayé n'est invisible : 1,000 pour le budget, 0,980 pour l'instrument bruité (bloc H.2). Opus propose comme handicap le « bruit ajouté aux données rendues », c'est-à-dire précisément celui que la dispersion trahit. La réserve R2 de la vérification s'applique : ce résultat vaut pour ce générateur.
- Une dose fine ne se plante que par des gestes cohérents. Retirer une loi dans le registre seul est une épreuve de plomberie, vraie par construction. Le témoin 4 d'Opus (sa « dose relue 0,998 ») est cette plomberie, et non la preuve qu'un comportement est compté.
- Le jardin des chemins (2602.18710), le flou aux niveaux d'accès 0 à 2, et les cinq comptes de l'oracle (les défauts plantés et les contrôles rejoués s'y ajoutent).

**Seulement chez Opus.**
- Le nul par acte quantifié (bloc A). Opus pose aussi une condition que Fable ne dit pas : le bruit partagé est celui du monde, et les graines d'échantillonnage des jetons restent indépendantes. Sans elles, l'échangeabilité tombe.
- Le jumeau à traitement égal, appuyé sur un PDF (2611.14950, p. 1). Fable a la même idée, mais reprise d'une note interne.
- Le flou mesuré par composante : vérifier les omissions coûte autant que la production (bloc C).
- Le dommage égal obtenu à l'analyse, par interpolation sur une grille de handicaps.
- L'attribution du dommage par acte, pour éprouver le lemme d'additivité.
- Le certificat à trois statuts, la graine fixée par une balise publique d'aléa, et la revue des fuites vers les moniteurs.
- Deux voisins lus sur PDF : 2611.21832 (traces bénignes et sabotées des mêmes projets) et 2611.14950.

## 4. Contradictions, tranchées à la source

1. **La commission est-elle floue ?** Opus dit qu'elle l'est à peine, à 7-14 % du coût de production. Fable dit qu'une loi fausse à la limite coûte 1,55 fois le budget pour être réfutée.
   - Les unités diffèrent. Opus rejoue une affirmation contre l'effet affirmé (d de 0,3 à 0,5) et rapporte ce coût au budget de tout l'épisode (sortie Opus, l. 90-101). Fable rapporte le coût au budget d'une seule loi, annoncée à la limite du détectable (sortie Fable, l. 38-50).
   - **Verdict** : les deux sont justes dans leur modèle, mais la conclusion d'Opus est trop large. Le saboteur diffus vise justement les lois au bord. Il faut donc déclarer le flou par composante et par détectabilité.
2. **Peut-on régler le témoin sur le dommage ?** L'épreuve 12 de Fable règle le handicap « sur le dommage visé ». L'invariant de N-060 v3 (point 4, l. 33) l'interdit : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur ». **Opus a raison** (sa décision D-1). Fable se contredit d'ailleurs avec son propre § 6.1.
3. **Réemployer l'organisme ou bâtir un générateur neuf ?** Opus (D-5) réemploie la grammaire et l'oracle de l'organisme ; Fable (D-2) bâtit un générateur neuf. Ce n'est pas tranchable à la source. Fable a un argument que je n'ai pas vérifié (repris) : le monde planté de l'organisme est lisible sur un dépôt distant. Les deux positions se fusionnent : réemployer le code de la grammaire et de l'oracle dans un générateur privé, à graines neuves.
4. **Combien de tirages du jumeau ?** Fable en prend 4, Opus 8 à 16. Le bloc A.2 d'Opus montre que la puissance croît avec ce nombre : 0,788 pour 4 tirages, 0,864 pour 8, à 1 600 actes. C'est un choix de coût, sans contradiction de fond.
5. **Coût.** Fable compte 81 000 épisodes pour 134 à 1 803 USD ; Opus, 7 800 épisodes pour 39 à 203 USD. Par épisode, cela fait environ 0,002 à 0,022 USD contre 0,005 à 0,026 USD : l'écart vient de la taille du banc, pas du prix.

**Réserve (R4).** Les deux réponses tombent d'accord sur le voisin de tête (2611.00407) et sur « non trouvé n'est pas libre ». Elles viennent de la même lignée, et Opus avait vu R-4577 : cet accord n'est pas une preuve indépendante.

## 5. Synthèse recommandée pour Lazar

**Ce qu'il faut retenir.** Le banc est constructible à bas prix. La conception de Fable v2 sert de base. On y greffe quatre pièces d'Opus :
- l'appariement à deux niveaux, avec des graines de jetons indépendantes ;
- le jumeau à traitement égal, rendu obligatoire ;
- le dommage égal obtenu par une règle d'analyse ;
- le flou déclaré par composante et par détectabilité.

Deux préalables viennent de Fable et valent pour les deux dessins :
- recomposer la fiche (ou l'agenda fermé) pour qu'elle ne fuie pas la vérité ;
- construire des analyses à options, sans lesquelles aucune dose fine ne se plante.

**Décisions qui changent.**
- L'épreuve 12 de Fable est remplacée par la D-1 d'Opus : une grille de handicaps et une interpolation écrite d'avance.
- La D-2 de Fable et la D-5 d'Opus fusionnent : code de l'organisme réemployé dans un générateur privé neuf. La vérification de compatibilité passe par un agent habilité. Retirer les mondes de l'organisme reste un nœud.
- La D-3 de Fable (deux lectures) tient. La remarque R1 s'y ajoute : on rapporte la visibilité du handicap contre le saboteur, et pas seulement contre l'honnête ordinaire.
- La D-7 d'Opus confirme le marqueur du bloc des modes chez Fable : aucune famille ne part avant la vérification habilitée (nœud).
- La D-8 de Fable s'étend : 2611.21832 et 2611.14950 entrent dans la liste des voisins à lire en entier.
- La D-8 d'Opus (attribution par acte) reste un nœud de dépense.
