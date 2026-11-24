# Erratum 1 de la réponse à la question 5 : Carbon contre Fable ; faut-il amender le Plan Turing ? (v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée n'est pas modifiée.
- **Heure** : `2026-11-24T16:40:18Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièce visée** : `reponse-q5-carbon-fable-et-plan-turing-v1.md` (`0bdc9810873f40368f9f3128435c9afd97538da14da6dfa3057351668094fa4d`).
- **Source des constats** : `contre-lecture-reponses-q1-q5-q7-q9-v1.md` (`9cefaa1fab6da2328bf99990f06ed03b4ec790c5e954e75c8209af07c68a786f`), section Q5 ; relu pour cet erratum : `reponse-q2-profondeur-surprise-retiree-v1.md` (`7f4cf73f…`, l. 19 et 23) ; `reponse-carbon-v1.md` (`a9532fbb…`, l. 36-40).

## Majeur : sévérité inégale envers Fable et Carbon (règle R4)

**Texte fautif** (verdict) : « le contrôle des sources (Fable vérifie tout ; Carbon ne vérifie rien et se trompe trois fois) ». Le même jugement figure au tableau de la section 2 (ligne « Références »). La pièce relève pourtant elle-même, en section 4, point 2, que « contredite » chez Fable dépasse la source. La question 2 (l. 19 et 23) établit deux faits. Le « contredite pour les nœuds » de Fable prend le parent pour l'idée fille. Et Fable s'appuie sur la v3 de Gu et Krenn, qui disait « strongly negatively correlated » sans coefficient, alors que la v4 donne ρ = −0,166, environ 3 % de la variance des rangs. En section 4, point 5, la pièce relève aussi que la dérivation de l'optimum mobile de Fable repose sur une hypothèse qu'elle ne dit pas (W indépendant de S). Celle de Carbon (`I = d·K`) n'est pas donnée.

**Décompte, à la même aune** (section 4 de la pièce, relue) :
- *Carbon*, trois erreurs de fait à la source : (1) mariage éloigné jugé « soutenu » alors que sa source dit que la récompense ne compense pas le risque [15, résumé] ; (2) transition topologique attribuée à Bettencourt et collègues 2008 au lieu de 2009 [21] ; (3) méthode des jumeaux attribuée à Bikard, Murray et Gans 2015 [22], *erreur probable* : seul le résumé de 2015 est lu, le texte est « à vérifier ». S'y ajoutent une surévaluation, Galison « démontré », que la recension citée [20] ne démontre pas, et une erreur partielle, « sans biais du survivant » pour un plan qui conditionne sur les paires nées (section 3, ligne « Première expérience »). Références non contrôlées, hormis quelques « à vérifier ».
- *Fable* : références contrôlées (46 liens appelés, contenus classés), un dépassement de la source (proximité aux nœuds, partagé avec Carbon, point 2) appuyé sur une version sans coefficient, une hypothèse non dite dans une dérivation (point 5).

**Correction.** Le verdict se lit : « le contrôle des sources : Fable contrôle ses références et dépasse une fois la source (proximité aux nœuds, comme Carbon) ; Carbon ne contrôle pas les siennes et commet trois erreurs de fait, dont une probable, plus une surévaluation et une erreur partielle ». La ligne « Références » du tableau de la section 2 se lit, colonne Fable : « 46 liens appelés, contenus classés ; un dépassement de la source (question 2) ». Le « Fable a raison » du point 1 de la section 4 s'écrit avec le même état de lecture que pour Carbon : « d'après les résumés [15, 17] et la notice [16], dont deux résumés lus par Fable seule et non relus ici ».

**Conséquence sur le verdict.** Les trois écarts de fond tiennent, et le troisième reste une vraie asymétrie : Carbon se trompe plus souvent, et sur des faits. Mais il ne s'agit plus de « tout » contre « rien ». La confiance de 0,7 est maintenue. Le Plan Turing et les amendements A1 à A6 ne changent pas. A5 (errata de provenance) garde les jumeaux de Bikard « à vérifier » et retire « Fable a raison » sur Galison (mineur 3).

## Mineurs

1. **Décompte « trois erreurs ».** Le verdict dit « trois » ; la section 4 en liste quatre au moins (mariage éloigné, Galison, attribution de 2008, jumeaux de Bikard), plus une erreur partielle et un dépassement partagé. *Correction* : celle du majeur, qui classe chacune (trois erreurs de fait, dont une probable ; une surévaluation ; une erreur partielle ; un dépassement partagé).
2. **κ dans la formule de Carbon** (section 3, ligne « Serrure et clé »). Texte : « `K = max κ·e^(−γχ)` ». Chez Carbon, κ est la **couverture** (`reponse-carbon-v1.md`, l. 36-38), à l'inverse du κ de Fable, part des conflits. *Correction* : « `K_C = max c_C·e^(−γ_C χ_C)` » (couverture, pénalité et conflits chez Carbon), selon `erratum-notations-kappa-et-hypergraphe-v1.md`.
3. **Galison** (section 4, point 3). Texte : « Le recenseur juge cet argument convaincant « less compellingly, in my opinion » [20]. **Fable a raison.** » Une recension donne un avis ; elle ne tranche pas un fait. *Correction* : « Carbon surévalue : la source citée ne démontre pas le rôle des horloges ; elle n'établit pas non plus le contraire. »
4. **Ligne « Objets »** (section 3). Texte : « vocabulaire surtout ». La question 7, qui porte la comparaison, conclut à des écarts réels d'expression (Carbon l'emporte sur les critères 1 et 5) et à une fusion. *Correction* : « fond en partie ; voir la question 7, qui fait foi », selon `erratum-notations-kappa-et-hypergraphe-v1.md`, section 2.

Aucun de ces mineurs ne change le verdict au-delà du majeur.
