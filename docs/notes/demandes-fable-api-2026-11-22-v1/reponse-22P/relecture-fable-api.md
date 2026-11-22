# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHpAQEbmvTZjJSQvS3tc`
- Heure (UTC) : 2026-11-22T10:33:48Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-22P-revue-revendications-programme-v1.md` — sha256 2315bfa8291e5dad01928d5e1cbf162204420086cc6d098a7f00ab7b46596d7b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22A/relecture-fable-api.md` — sha256 2255a6a3a65ba04c4acfa16af3edd83c8f3f263e89dad00558a640b6529e461c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22B/relecture-fable-api.md` — sha256 c5980780f80fb7e54c8f925432d118bf698769bc248b846c63aa48108043138b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22C/relecture-fable-api.md` — sha256 f05051442f07b2f55cb06e982bd6c9f1721813c6848eb1182d69d8deed677d2e (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22/relecture-fable-api.md` — sha256 22c5652113797a399d1d1df7fc8d4d6b100bcf04bd655118d51238c5ef3d7b64 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 3598130ed80e8c1ce74d156dc5adfed4a211025ef5861c2da97bb43b3147cf03
- Jetons : entrée 84703, sortie 9616 (dont réflexion 1849), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.062264 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 22P : revue des revendications à l'échelle du programme

**Conclusion d'abord.** Après les retraits, les trois papiers sont des papiers de mesure, et ils tiennent sous une seule forme de thèse : un modèle nul hérité et nommé, un écart mesuré, aucune garantie tirée des moniteurs. Quatre choses ne se voient qu'à l'échelle du programme :
- une même référence honnête, dans quatre unités différentes, conditionne toutes les portes ;
- une même comparaison (texte contre accès interne) est revendiquée à quatre endroits ;
- une seule expérience (« position ou dépendance ») décide du sort du papier B ;
- les cinq revues viennent du même modèle, donc leur accord n'est pas une confirmation.

Confiance d'ensemble : 0,55.

**Réserves.**
- Je n'ai lu aucun PDF.
- La seconde lecture, la lecture de la stéganographie et la réponse 2 ne me sont pas jointes ici : je n'en connais que ce que les revues en rapportent.
- Je n'ai pas le texte des décisions N-003, N-004, N-069, N-075 à N-077.
- Je n'ai recalculé ni chiffre ni empreinte : les ordres de grandeur des revues restent des hypothèses.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Dresser le graphe des dépendances entre papiers**, et non une table par papier : quelles portes partagent une référence, une métrique, une expérience.
- **Faire un budget commun d'exécutions honnêtes.** Les trois papiers puisent dans le même calcul.
- **Vérifier la cohérence avec N-075.** Si les sondes sont « un accélérateur, non une garantie », aucun énoncé de papier ne doit porter une garantie que seul l'audit au hasard fonde.
- **Traiter l'accord des revues comme un risque de mode commun.**
- **Écrire le rapport de rejet du programme entier** : « trois papiers de mesure sans théorème, qu'y a-t-il de propre ? »

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- Les scores pas à pas des exécutions honnêtes au dépôt, avec les identifiants de tâche, d'exécution, de copie et d'essaim.
- Les verdicts bruts des juges sur un même contenu jugé plusieurs fois sans attaque.
- Le nombre d'épisodes honnêtes derrière chaque seuil de chaque porte.
- Le texte des décisions citées, et le fichier des dix-sept décisions du papier C, absent de l'arbre [FAIT RAPPORTÉ, table].
- Les pages et les arbres de citations non lus [FAIT RAPPORTÉ, recherche exhaustive, § 1].

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.
- **Un harnais unique « honnête contre honnête »**, à composantes de variance emboîtées : pas, exécution, tâche, essaim, juge.
- **Un banc à vérité plantée par papier** : exposant et terme entre tâches (A), coalition de position puis de dépendance (B), juge synthétique (C).
- **Une seule métrique d'union**, recalée au même taux total de fausses alertes, partagée par A, B et C.
- **Un calcul de puissance commun**, dans l'unité indépendante de chaque papier.
- **Des substituts par permutation** (pas, copies) pour la question pivot.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Les essais honnêtes et les bancs plantés : leur issue ne dépend d'aucun avis.
- Des énoncés témoins au statut connu, mêlés aux nôtres dans le collisionneur.
- Une seconde famille de modèles pour relire cette revue même.
- Trois spécialistes : stéganalyse, détection de signaux rares, analyse adaptative de données.
- Les auteurs des antécédents (Zhang et Gao ; Parrack et collaborateurs ; Rose et collaborateurs), chacun sur une question fermée.

## Demande reformulée

« Voici la table des revendications d'un programme en trois papiers, les décisions qui la suivent, trois revues par papier et les notes de lecture. À l'échelle du programme :
1. dresse le graphe des dépendances entre revendications, portes et références honnêtes, avec l'unité de chaque référence ;
2. repère toute comparaison revendiquée à plusieurs endroits et désigne un seul porteur ;
3. tranche les désaccords entre revues, en disant sur quelle dérivation ;
4. écris la thèse commune et vérifie qu'aucun énoncé ne porte une garantie que la décision sur l'audit réserve au tirage au hasard ;
5. rends pour chaque revendication un verdict (tenue, à resserrer, à retirer, à remplacer), l'énoncé neuf et l'épreuve qui le réfute ;
6. donne l'ordre des travaux et le budget d'exécutions honnêtes qu'il suppose ;
7. gradue chaque "non trouvé" et chaque "non touché" par la recherche qui le fonde ;
8. liste les phrases à ne plus écrire.

Marque fait rapporté, hypothèse, proposition. Aucune zone vierge n'est déclarée libre. »

## Réponse à la demande reformulée

### Ce qui ne se voit qu'à l'échelle du programme

1. **Une seule loi de la référence, quatre unités** [HYPOTHÈSE]. Chaque revue l'a redécouverte dans son unité, mais N-076 ne compte que m et n. Il faut l'étendre : toute porte déclare l'unité, la taille et le droit d'écriture de sa référence.

| Papier ou porte | Référence honnête | Unité |
|---|---|---|
| A, accumulation | scores honnêtes | pas, par exécution jumelle ou par régime |
| A, porte G1 | seuil à 1 % | épisode |
| B | corrélation honnête entre copies | essaim |
| C | archive du juge statistique | fiche |

2. **Une comparaison, quatre porteurs** [FAIT RAPPORTÉ, table § 4 point 8, et réponse 22C]. « Texte contre accès interne » figure dans la complémentarité (A), la diversité des moniteurs (B), la loi de déférence et le quorum (C). Un relecteur y verra un résultat compté quatre fois.

3. **Une expérience décide de deux papiers** [PROPOSITION]. La question « le sabotage joué déplace-t-il la position, la dépendance, ou les deux ? » est une section de A et l'ouverture de B. C'est une porte du programme, à placer avant G2.

4. **Le budget honnête est commun** [HYPOTHÈSE, ordres de grandeur des revues, à refaire]. Il faudrait environ 150 tâches par extrémité d'horizon pour l'exposant (A), plus de cent essaims par bras (B), un millier d'épisodes par seuil (G1). Ces besoins se disputent le même calcul, d'où l'importance de l'ordre des travaux.

5. **Cohérence avec N-075** [PROPOSITION]. Trois énoncés en vigueur écrivent « garantie toujours valide » : l'accumulation, la statistique conjointe, le juge au nul. Sous une référence estimée, c'est une validité conditionnelle. La seule protection indépendante de l'attaque reste le tirage d'audit à plancher [FAIT RAPPORTÉ, contexte]. Ses antériorités sont à citer :
   - Greenblatt et collaborateurs, 2023, « AI Control: Improving Safety Despite Intentional Subversion » ;
   - Horvitz et Thompson, 1952, « A generalization of sampling without replacement from a finite universe ».
   
   Les deux sont rapportées, non vérifiées sur PDF.

6. **Mode commun** [FAIT RAPPORTÉ, en-têtes]. Les réponses 9, 22, 22A, 22B, 22C et celle-ci sortent du même modèle. Leur convergence sur « retirer, citer, mesurer » peut être un biais partagé, dans les deux sens (retrait excessif compris).

7. **Couverture inégale** [FAIT RAPPORTÉ, réponse 22C]. Les 36 requêtes ne visaient ni les juges sous attaque ni l'organisme. « Non touché » y signifie « non cherché ».

### Désaccords entre revues, tranchés

Tous les arbitrages sont des PROPOSITIONS.
- **Accumulation : « à resserrer » (22) ou « à remplacer » (22A) ?** À remplacer. Un énoncé vrai par construction sous le nul cité ne se resserre pas.
- **Forme du nul : plafond au-delà de n = m (22), ou régime en n/√m inobservable avec des jumelles (22A) ?** Les deux dérivations valent chacune pour un plan. Le nul s'écrit donc par plan de référence, et le plan se fixe avant tout scellement.
- **Courbe selon le nombre d'agents : somme « plate » (22) ou baisse par la corrélation honnête (22B) ?** 22B prévaut : « plate » supposait des copies indépendantes.
- **« Antécédent défectueux » : simulation (22) ou recalcul à la main (22A) ?** Le recalcul d'abord, il est moins cher. La simulation suit si le paramètre publié s'écarte de la valeur prédite.
- **Comparaison juge contre sonde.** A porte la détection, C la corruptibilité, B fournit la corrélation des erreurs sans attaque. La métrique d'union est unique.
- **H8, validité et robustesse.** Diagnostic rapporté dans A à chaque cycle ; la revendication de construit va à C, comme l'écrit N-062.

### Table du programme

La colonne « antériorité » est un FAIT RAPPORTÉ par la pièce citée, lue à travers les revues. « Rech » désigne la recherche exhaustive, « Stég » la lecture de la stéganographie, « Lect2 » la seconde lecture. Verdicts, énoncés neufs et épreuves sont des PROPOSITIONS.

| Revendication | Antériorité qui la touche | Verdict | Énoncé neuf | Épreuve qui le réfuterait |
|---|---|---|---|---|
| Thèse du programme | Ker 2010 ; Avenhaus et Jaech 1981 (Stég) ; Khilar 2610.13083 (Rech) ; Arias-Castro et collaborateurs 2012 (Lect2) | À remplacer par une forme commune | « Pour chaque moniteur : un nul hérité nommé, une référence honnête déclarée (unité, taille, qui l'écrit), un écart mesuré. La garantie vient du seul audit au hasard. » | Un banc planté où l'ajustement ne retrouve pas l'écart planté |
| Lemme d'additivité ; théorème négatif | Stég, Lect2, Rech (§ 2 et § 4) | Retirés (décidé) ; repli de N-004 à fermer | Question pivot : position ou dépendance | Aucun test ne dépasse son niveau sur substituts |
| Accumulation toujours valide (A) | Ker 2010, p. 7, 11 (Stég) ; Khilar, propositions 3-4 (Rech) | À remplacer | Énoncé « écart au nul » de 22A, écrit par plan de référence | Jumeau contre jumeau : ajustement sans résidu |
| Gain de l'accès interne (A) | Parrack, Attubato, Heimersheim 2025, p. 1-8 (Lect2) | Tenue, resserrée | Union « boîte noire et sonde » contre union « deux boîtes noires », à taux total égal | Borne haute de l'écart ≤ 0 sur la famille tenue à l'écart |
| Portes G1, G2, GC | Aucune ; constats des revues | À compléter | Chaque seuil déclare ses épisodes honnêtes et l'intervalle de son taux réel ; G2 ajoute la somme globale ; GC lit une marge d'équivalence | Intervalles disjoints entre moniteurs comparés |
| Règle N-076 | Ker 2010, corollaire 1 (Stég) ; Wen et collaborateurs 2411.17693, p. 18 (Rech) | À étendre | Unité, taille et droit d'écriture, pour pas, épisode, essaim, archive | — |
| Transposition du jeton à l'action (A) | Makins et collaborateurs 2607.07368, p. 1 (Rech) | À resserrer en question | Énoncé de 22A | Le maximum par action ne baisse pas sous fragmentation |
| Co-élévation ; statistique conjointe (B) | Arias-Castro et collaborateurs, p. 14-20 (Lect2) ; Rose et collaborateurs 2604.01151, p. 17 (Rech) | À remplacer | Énoncés de 22B : deux nuls, corrélation honnête, gain contre la somme globale | Aucun gain sur la somme dans la strate « dépendance » |
| Courbe selon le nombre d'agents (B) | Avenhaus et Jaech, p. 25, 31 (Stég) ; Makins, p. 1 (Rech) | À remplacer | Énoncé par agrégateur, avec le terme de corrélation honnête | La somme baisse plus que ce terme ne le prédit |
| Diversité des moniteurs (B) | Kish 1965 (mémoire, non vérifié sur PDF) | Retirée comme loi | Mesure versée à la métrique d'union | — |
| Loi de déférence ; déplacement de la sonde ; taxe (C) | Hors recherche ; N-077 | À resserrer | Nul par placebo ; équivalence à marge scellée ; classe d'attaquant et budget | Destination sous attaque indiscernable du placebo |
| Quorum par type d'accès (C) | Parrack et collaborateurs, p. 1-2 (Lect2) | À remplacer dans sa forme | Quorum « juge et sonde » contre « deux juges », à taux total égal | Borne haute de l'écart ≤ 0 |
| Second terrain ; juge au nul (C, organisme) | Ker 2010, p. 13 (Stég) ; Khilar, p. 9-10 (Rech) | Tenus, complétés | Grille (m, n), bras « archive nourrie » contre « archive gelée » | Taux nominal tenu dans les deux bras |
| Marge asymétrique ; délégation ; interaction flou-net | N-077 ; N-070 ; N-055 | Mesures descriptives | — | — |
| Reste de l'organisme | Non cherché | Non revu | — | — |

### Ordre des travaux

Toutes les étapes sont des PROPOSITIONS.
1. Table version 2, provisoire, avec N-075 à N-077 et les retraits propagés.
2. Harnais honnête unique sur les exécutions au dépôt : composantes de variance, corrélation entre copies, variance des verdicts.
3. Calculs de puissance et bancs plantés, puis budget commun.
4. Scellement des prévisions décidables seulement, le terme entre tâches en tête.
5. Porte G1, avec intervalles de seuil.
6. Question pivot « position ou dépendance », sur les organismes de G1.
7. Selon l'issue : papier B maintenu, ou fondu en section de A (repli scellé d'avance).
8. Recherche d'antériorité propre au papier C, avant son préenregistrement.

### Phrases à ne plus écrire

Elles s'ajoutent aux listes des revues [PROPOSITION].
1. « Garantie toujours valide », dans quelque papier que ce soit, sans l'unité, la taille et le droit d'écriture de la référence.
2. « La sonde voit ce que le texte manque », dans A, B ou C, sans la métrique d'union commune.
3. « Trois papiers, trois résultats indépendants » : ils partagent la référence, la métrique et la question pivot.
4. « Les revues convergent », sans « elles sortent du même modèle ».
5. « Papier C et organisme non touchés par l'antériorité », sans « non cherchés ».
6. « La somme est plate en nombre d'agents », sans la corrélation honnête.
7. « Le programme garde une marge contre un saboteur diffus » : N-075 et N-077 réservent cela à l'audit.
8. « Colonne vertébrale théorique » : il n'en reste pas.
9. « Table en vigueur », pour la version du 19 novembre.

## Question neutre pour le collisionneur

« Une équipe prépare trois études sur des détecteurs appliqués à des programmes autonomes : le suivi d'un seul programme dans le temps, le suivi de plusieurs exemplaires identiques travaillant ensemble, et la fiabilité d'évaluateurs automatiques de textes. Dans les trois, un détecteur est réglé sur des exécutions réputées sans faute. On vous remet une liste d'énoncés et de règles de décision tirés des trois études, dans un ordre tiré au hasard ; certains ne sont pas de l'équipe.
1. Pour chaque énoncé : est-il exact tel qu'écrit, et de quelles quantités non dites dépend-il ?
2. Quels énoncés reposent sur la même mesure ou la même hypothèse, au point de n'en former qu'un ?
3. Quel résultat publié le plus proche connaissez-vous, dans quelque domaine que ce soit, et que suppose-t-il ?
4. Classez chacun : établi ailleurs, conséquence immédiate, ouvert, mal posé, ou faux.
5. Dans quel ordre mèneriez-vous les expériences, et laquelle rendrait les autres inutiles ?

Dites votre degré de certitude et ce que vous citez de mémoire. »

La liste jointe mêle les énoncés anciens, les énoncés neufs et six à huit témoins au statut connu [PROPOSITION].

## Décisions qui reviennent au directeur

**Décision 1 : adopter ou non la forme commune de thèse pour les trois papiers.**
- *Enjeu.* Sans elle, chaque papier garde des mots de garantie que N-075 contredit.
- *Option a : forme commune (nul nommé, référence déclarée, écart mesuré, garantie par l'audit seul).* Avantage : cohérence, aucun énoncé à rétracter. Inconvénient : programme de mesure, exposé au reproche « évident ».
- *Option b : thèse par papier.* Avantage : continuité. Inconvénient : doubles comptes et garanties conditionnelles non dites.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 2 : étendre N-076 à toutes les références (épisode, essaim, archive) avec le droit d'écriture.**
- *Enjeu.* Les portes G1, G2 et le juge au nul reposent sur des références non comptées.
- *Option a : extension maintenant.* Avantage : portes comparables. Inconvénient : trois préenregistrements à retoucher.
- *Option b : papier A seul d'abord.* Avantage : rapide. Inconvénient : B et C restent sans règle.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 3 : désigner un seul porteur de la comparaison « texte contre accès interne ».**
- *Enjeu.* Elle est revendiquée à quatre endroits.
- *Option a : A porte la détection, C la corruptibilité, B une mesure ; métrique d'union unique.* Avantage : frontière nette. Inconvénient : coordination des préenregistrements.
- *Option b : tout au papier A.* Avantage : un seul lieu. Inconvénient : C perd son quorum.
- *Option c : état actuel.* Avantage : aucune réécriture. Inconvénient : double compte visible.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 4 : faire de la question « position ou dépendance » une porte du programme, avec repli scellé du papier B.**
- *Enjeu.* Si seule la position bouge, B se réduit à une section de A.
- *Option a : porte placée après G1 et avant G2, repli écrit d'avance.* Avantage : aucun essaim dépensé à tort. Inconvénient : B attend.
- *Option b : B avance en parallèle.* Avantage : calendrier. Inconvénient : risque de papier vide.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 5 : fixer l'ordre des travaux et le budget honnête commun avant tout scellement.**
- *Enjeu.* Les besoins de A, B et G1 dépassent peut-être le calcul disponible.
- *Option a : harnais honnête et puissance d'abord, puis scellement des seules prévisions décidables.* Avantage : aucune issue indéterminée scellée. Inconvénient : quelques jours.
- *Option b : sceller maintenant.* Avantage : aucun délai. Inconvénient : indécision probable sur l'exposant.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 6 : approuver l'envoi au collisionneur avec témoins, et une relecture de cette revue par une autre famille de modèles.**
- *Enjeu.* Six pièces concordantes sortent d'un seul modèle.
- *Option a : témoins écrits par un agent neuf, plus relecture externe.* Avantage : accord interprétable. Inconvénient : une préparation de plus.
- *Option b : envoi direct.* Avantage : immédiat. Inconvénient : biais commun non mesuré.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
