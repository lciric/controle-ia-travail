# Tolérance propre aux réseaux du programme de vérification de la sortie des mondes — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 6.2 (la tolérance proposée) et § 6.5 (valeur et phrase à ajouter à l'arbitrage).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : La valeur 0,02 est celle que la pièce recommande ; la mère la retient.

<!-- lignes 356 à 366 de la source : règle, à l'octet -->

Pour une famille dont la loi honnête de la tranche est arrondie, par tranche et par aire dite a (0,69, 0,80, 0,95) :

1. **Aires atteignables.** Le programme calcule, par la somme finie qu'il a déjà, les valeurs de palier et de saut autour de a. Soit **v_sous** la plus grande aire atteignable inférieure ou égale à a, et **v_sur** la plus petite supérieure ou égale à a.
2. **(a) conforme** : inchangé (aire réalisée à 0,005 de a).
3. **(a bis) conforme au pas du réseau** : (a) échoue pour cette aire ; l'aire réalisée sous la lecture retenue est égale à v_sous ou à v_sur (à 10⁻⁹ près) ; et elle est à **0,02 au plus** de a. La famille est conforme si chaque couple (tranche, aire) est (a) ou (a bis).
4. **Chaque (a bis) est un écart nommé** : une observation de code neuf, avec le chemin du décalage et le rang de la tranche ; au compte rendu, v_sous, v_sur et l'aire réalisée (aires calculées sur les lois de l'auteur, non valeurs vraies de témoins) et un champ qui dit que la tolérance des réseaux a servi.
5. **(b) unité brute constatée** : comme aujourd'hui, le critère (a) ou (a bis) étant appliqué sous l'unité brute pour les lois arrondies.
6. **(c) non lisible**, avec une raison neuve, **« réseau trop grossier pour l'aire dite »**, quand ni v_sous ni v_sur n'est à 0,02 de a : aucun décalage ne pouvait passer. Elle se distingue de « aucune unité ne réalise les aires », qui veut dire que les nombres de l'auteur manquent une aire atteignable.
7. **Ordre** : les trois aires réalisées d'une tranche sont strictement croissantes ; sinon (c).

Les témoins à saboteur d'une famille conforme par (a bis) sont convertis comme pour (a) : la vérité se calcule sur la loi et le décalage réels.

<!-- lignes 384 à 385 de la source : valeur et phrase pour la pièce de scellement, à l'octet -->

- **La règle du § 6.2. Confiance 0,75 sur sa forme ; 0,6 sur la valeur 0,02** (0,015 à 0,03 se défendent ; à geler par la mère).
- C'est une **lecture déclarée de session**, de la mère, comme l'arbitrage ; elle ne change ni hypothèse ni revendication. Phrase à ajouter à celle de l'arbitrage (§ 4) dans la pièce de scellement : « Pour une loi honnête arrondie, où l'aire ne prend qu'un ensemble discret de valeurs, un décalage est aussi reçu si l'aire qu'il réalise est l'une des deux aires atteignables qui encadrent l'aire dite et s'en écarte de 0,02 au plus ; ce cas est compté et nommé ; si aucune aire atteignable n'est à 0,02 de l'aire dite, le saboteur de la famille n'est pas converti et le cas est rapporté sous son nom. »
