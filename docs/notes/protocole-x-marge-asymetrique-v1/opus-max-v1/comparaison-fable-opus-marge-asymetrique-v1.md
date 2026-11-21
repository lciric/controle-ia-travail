# Comparaison : la marge asymétrique après « Ctrl-Z », réponse de Fable 5.2 (v2) et réponse d'Opus 5.5 en effort maximal (v1)

- **Pièce de travail (classe C).** Auteur : Claude Opus 5.5, comparateur neuf, qui n'a écrit aucune des deux pièces. 21 novembre 2026. Processeur seul : aucun appel payant, aucun commit, aucune recherche en ligne. Aucun refus d'outil.
- **Grille écrite et scellée avant toute lecture** : `grille-comparaison-marge-asymetrique-v1.md` (`f4e56aa8a23b2825205625faf64c45bf394ff5ae206da606465a4dea92ae858a`), même dossier.
- **Pièces lues, empreintes égales aux compagnons** : réponse de Fable v2, `reponse-fable-marge-asymetrique-v2.md` (`6c7e1c2f…050d`, scellée ; elle remplace la v1) ; sa contre-lecture par Opus, `contre-lecture-reponse-fable-marge-asymetrique-v1-opus-v1.md` (`738f05f1…d3e0`, début et verdict) ; la vérification des corrections, `verification-corrections-marge-asymetrique-v2-opus-v1.md` (en entier, verdict « conforme ») ; réponse d'Opus effort maximal, `opus-max-v1/reponse-opus-max-marge-asymetrique-v1.md` (`4f2cc955…982b`), ses calculs `.py` (`776d4de5…`) et `.txt` (`0cf775ab…`) et sa provenance (`sources/…`). Pour trancher un point de portée : `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v6.md`, lignes 48, 106, 107, 258, 355 (par motifs).
- **Non ouvert** : aucun chemin cloisonné ; rien sous `archives-reponses-modeles/`, `diag/`, `donnees/`, `/root/.claude/`.

## 1. Chiffres vérifiés à la page

PDF dont l'empreinte est égale au compagnon ; texte par `pdftotext -layout`, rang de page du fichier ; calculs refaits à la main.

| Pièce | Chiffre | Source | Sort |
|---|---|---|---|
| Fable | « around 80% of the time » ; +3,9 points, intervalle [−2,1 ; +10,9] | Lucassen et Kaufman, `2605.26047v2.pdf` (`947724f4…`), p. 10 | exact |
| Fable | corrélations 0,19 (honnête) et 0,43 (attaque) ; bascule à 0,031 ; le rouge optimal rend ses attaques « as highly correlated as possible » | même PDF, p. 7 | exact |
| Fable | 79 % des seconds scores plus bas | même PDF, p. 5 | exact |
| Fable | sûreté de 89 % à 46 % (le saboteur sait qu'il est rééchantillonné), 69 %, 17 % (il simule le moniteur) | Kutasov et al., `2511.02997v1.pdf` (`1dcffc49…`), p. 5, table et texte | exact, attribution juste |
| Fable | table de « Ctrl-Z » : 41,8 % à 100 % d'utilité, 72,7 %, 83,2 %, 87,1 % à 95 % | Bhatt et al., `2504.10374v1.pdf` (`5f802d67…`), p. 5 et 8 | exact |
| Fable | majorité de trois à 2 % : succès divisé par 16,9 ; gain du maximum 1,70 à quatre répliques et ρ = 0,19 | refait : 0,02 / (3 × 0,02² × 0,98 + 0,02³) = 16,89 ; 1 / (0,19 + 0,81 × 0,492) = 1,699 | exact |
| Opus | sûreté de 61 % à 71 %, +10,2 points [+6,1 ; +14,3] | Lucassen et Kaufman, p. 1 et 2 | exact |
| Opus | −20,5 et −37,9 points dans le régime brassé ; utilité −1,0 point [−2,8 ; +0,9], 298 tâches | même PDF, p. 11 | exact |
| Opus | 22 points de baisse moyenne au seul retirage | même PDF, p. 5 | exact |
| Opus | sécurité de 41 % à 63 % ; « Safety improves because monitor performance improves » ; « no harder » | Sandoval et Rushing, `anteriorite-P-041-v2/c5/2512.02157v1.pdf` (`c3a2c6c5…`), p. 1 | exact |
| Opus | Kutasov et al. : de 50 % à 89 % ; « un attaquant qui sait quand on rééchantillonne ou qui simule le moniteur la ramène à 17 % » | Kutasov et al., p. 1 | **fidèle au résumé, imprécis** : la table de la p. 5 donne 46 % pour le seul fait de savoir quand on rééchantillonne, 17 % pour la simulation du moniteur |
| Opus | placebo : rapports 4,88 et 8,50 ; banc : 1,0000 contre 0,0435 ; mémoire : 1,45 % à δ/σ = 0,3 ; facteur 2,841 à ρ = 0,19, k = 5 | sortie `.txt`, lignes 49, 54, 131, 73, 143 ; 1 / (0,19 + 0,81 / 5) = 2,841 | exact ; mais 2,841 est le gain de la **moyenne** des k tirages (voir § 4, contradiction 2) |

Coûts unitaires : l'erratum 1 de la conception des expérimentateurs donne 0,14 USD (0,081 + 0,061) et 4,10 USD par greffon. Fable arrondit (18 × 0,14 = 2,52) ; Opus garde la somme exacte (21 × 0,142 = 2,98). L'écart est sans portée.

## 2. Notes par critère (0 à 5)

| Critère | Fable v2 | Opus max v1 | Raisons |
|---|---|---|---|
| 1. Justesse des chiffres à la page | 5 | 4 | Fable : tout tient, et elle a été contre-lue puis vérifiée (vingt et un points vérifiés à la v1, « conforme » à la v2). Opus : tout est exact à la page, mais les 17 % de Kutasov et al. sont attribués au résumé mêlé, et le facteur 2,841 est donné sans dire qu'il vaut pour la moyenne seule |
| 2. Profondeur | 5 | 4 | Fable : deux familles de scores qui rangent les règles en sens contraires (calcul B) ; sensibilité à la ressemblance des scores d'attaque (G1 bis) et à la réplique reconnue (H) ; corrélation de queue avec la part d'égalités (F). Opus : irréfutabilité de l'énoncé par placebo et par dopant (C, B, F), borne par la valeur de la ressource (H), corollaire de la mémoire au second ordre (D), mais l'agrégateur boîte blanche n'est pas mis sous attaque |
| 3. Originalité des solutions | 3 | 4 | Fable : sa « taxe de cohérence » (H6′) est publiée en boîte noire depuis juillet (Lin Yulong et al.), et elle le dit ; 6.3 et 6.5 sont modestes. Opus : la lecture contre un placebo à utilité égale, réglé par le noyau ; la borne marge ≤ V(R) ; « la mémoire qui compte est celle du défenseur » ; la prédiction « aucun gain aux positions lues avant le premier jeton tiré » ; la meilleure riposte énumérée chez la mère, jamais écrite par un modèle |
| 4. Honnêteté des limites et R8 | 5 | 4 | Fable : premier pas non justifié nommé (lecture « fabrication », pas 11), attentes manquées déclarées, deux recommandations contraires du même auteur le même jour signalées. Opus : limite d'indépendance déclarée, pages web marquées non opposables, « non trouvé » ≠ « libre » ; mais « j'arrive seul au retrait » est trop fort, puisqu'il avait lu tôt GO-2026-11-21-64 qui accordait le retrait |
| 5. Respect des règles et des nœuds | 4 | 4 | Fable : D-1 traitée en un seul nœud avec l'ancienne D-2 ; mais elle ne pose pas la lecture « hors audit, aucun moniteur dans l'intervention » que Lazar a demandée le 13 novembre (état de l'art v6, l. 106). Opus : il part de cette lecture, tient la règle des trois chantiers et « Qui conçoit » ; mais il propose un bras à agrégation par moyenne entre tirages (D-3), que la note de Fable montre défait par un attaquant qui se dilue |
| 6. Actionnabilité | 4 | 5 | Fable : cinq décisions claires, mais un plan lourd (quatorze mondes, dix-huit témoins). Opus : sept tests de mort rattachés aux formes de la note des expérimentateurs, barreaux, versés au banc d'étalonnage commun (lot S1), sans chantier neuf |
| 7. Coût | 4 | 5 | Les deux : étape 0 à 0 USD, étape 1 sur devis (2,52 à 73,80 USD contre 2,98 à 86,10 USD). Seul Opus chiffre la mesure réelle (2 400 à 15 200 épisodes) et recommande de la greffer sur des épisodes déjà payés. Fable a coûté deux versions du quota rare de Fable et une contre-lecture |
| 8. Ce qui manque (5 = rien d'important) | 4 | 3 | Il manque à Fable : l'artefact du seuil chiffré contre un placebo (elle n'a que « le signe dépend de l'échelle », D2) ; Sandoval et Rushing ; le lien au lemme d'additivité ; une famille à queue lourde (déclaré). Il manque à Opus : Lin Yulong et al. (cohérence entre contextes, le voisin le plus proche), Mallen et al., Serrano et al. ; le lien à la marge qui survit au protocole connu (H10) ; la sensibilité du gain d'information à la ressemblance des scores d'attaque ; une contre-lecture |
| Total indicatif | 34 | 33 | |

## 3. Ce que chacune a que l'autre n'a pas

**Fable seule** : la décomposition de la table de « Ctrl-Z » (61 % de la baisse vient de la cession, utilité non égale) ; deux familles de scores et le fait que la bonne règle dépend de la loi que l'attaquant choisit ; le gain d'information défait quand les scores d'attaque se ressemblent (−0,045 à 0,90) ou quand la réplique est reconnue (−0,19) ; la corrélation de queue et sa dépendance aux égalités ; la paraphrase de l'entrée distinguée de celle de la sortie ; quatre retouches à H10 ; l'inventaire des dépendances des organismes ; le couple neutre et la sous-question pour le collisionneur et l'organisme (le Protocole X complet).

**Opus seul** : la lecture de Lazar posée d'emblée ; la preuve que l'énoncé de N-015 est satisfait par un placebo sans cible (rapport de 1,7 à 8,5) et par un dopant, et qu'une lecture par pentes déclare une fausse marge dans 100 % des cas contre 4,35 % pour la lecture contre placebo ; la borne marge ≤ V(R) et le coût de l'oublier (100 % mesuré contre 2 % réel) ; le corollaire chiffré de la mémoire (au plus 1,45 % du dommage à δ/σ ≤ 0,3), face attaquant du lemme d'additivité ; Sandoval et Rushing, seule pièce empirique sur une restriction de contexte ; la convergence « tout le gain passe par l'information du moniteur » ; deux voisins à lire sur PDF (« Caught, Not Taught », « Safety Does Not Compose »).

## 4. Contradictions, tranchées à la source

1. **Les 17 % de Kutasov et al.** Opus les rattache à « savoir quand on rééchantillonne ou simuler le moniteur » ; Fable à la simulation seule, 46 % pour le savoir. La table de la p. 5 (« Careful on resample 0.46 », « Simulating Monitor 0.17 ») donne raison à Fable ; la phrase d'Opus recopie le résumé de la p. 1, qui regroupe les deux. Erratum d'une ligne dû à la pièce d'Opus.
2. **Le gain du rééchantillonnage pour information dans l'agrégateur boîte blanche.** Opus (D-3) : budget effectif multiplié par 2,841 à ρ = 0,19 et cinq tirages, « contre un attaquant cohérent ». C'est la formule 1 / (ρ + (1 − ρ) / k), celle de la moyenne. Fable l'avait écrite à sa v1 et l'a retirée à la v2 (constat 6) : le maximum ne rend que 1,70 à quatre tirages ; la moyenne tombe à 0,263 devant un attaquant qui se dilue (calcul B) ; et le maximum perd lui-même son gain quand les scores d'attaque se ressemblent (G1 bis), ce que le rouge optimal recherche (Lucassen et Kaufman, p. 7). **Fable a raison.** Le bras proposé par Opus reste utile, mais sa prédiction doit être écrite avec le maximum, la ressemblance des scores d'attaque déclarée, et le plafond 1 / ρ.
3. **Le cadre de la question.** Fable garde la lecture de tous les tirages par le moniteur dans la table de H6 ; Opus l'exclut, sur la lecture « hors audit, aucun moniteur dans l'intervention » demandée par Lazar le 13 novembre et non encore inscrite (état de l'art v6, l. 106 et 258). **Opus est fidèle au mot de Lazar.** Les conclusions ne divergent pas : Fable range aussi ce rééchantillonnage « dans la preuve, hors de H6 ».
4. **« Il ne perd rien »** (N-077, § 0, sur la note de Fable) contre « il ne perd que la valeur de la ressource détruite » (Opus). En général, Opus a raison : la table de Fable chiffre elle-même un coût contre la majorité (treize tirages d'attaque par dommage). Pour le sabotage diffus additif du papier A, les deux disent la même chose.
5. **La taxe de cohérence.** Fable la garde comme option (c) à confiance 0,25 ; Opus la dit nulle ou négative sous le maximum, puisque le rouge optimal cherche la cohérence. Le calcul G1 bis de Fable va dans le sens d'Opus. N-077 l'a laissée non inscrite : rien à changer.
6. **La confiance dans le retrait** (0,6 contre 0,8). La raison d'Opus (irréfutabilité par placebo, plus le nul contre la meilleure riposte) ne dépend pas du pas « fabrication », que Fable marque comme supposé. **La raison d'Opus est la plus solide** ; sa revendication d'indépendance est à atténuer.

## 5. Synthèse recommandée pour Lazar

**À retenir.** Les deux réponses arrivent au même retrait de la marge asymétrique, déjà accordé (N-077, GO-2026-11-21-64), par deux raisons qui se complètent : contre un saboteur qui répond au mieux, aucune intervention ne garde de marge ; et l'énoncé, tel qu'il est écrit, est satisfait par un simple placebo. Le seul gain établi du rééchantillonnage est l'information donnée au moniteur, et il se défait quand les scores d'attaque se ressemblent ou quand la réplique est reconnue.

**Décisions qui changent ou s'ajoutent.**
1. **N-077 confirmée, avec une raison de plus** : l'irréfutabilité par placebo (calculs C et F d'Opus) entre dans la décision. Le retrait ne dépend plus du pas « fabrication ». Format de décision, défaut sous 48 heures : l'inscrire par erratum.
2. **Lecture de la mesure gardée, au préenregistrement** (D-1 (a) d'Opus, jointe aux nuls prédits et au contraste entre modes d'induction de Fable) : placebo réglé par le noyau à utilité égale ; baisse du succès exigée ; échelle linéaire rapportée à côté de l'échelle à seuil ; meilleure riposte énumérée chez la mère. Recommandation : oui, confiance 0,8.
3. **Un seul banc d'épreuve** : les deux recommandent le banc d'étalonnage commun des expérimentateurs, sans chantier neuf (D-3 de Fable, D-2 d'Opus). Fusionner les quatorze mondes et dix-huit témoins de Fable avec les tests placebo, dopant, riposte contre organisme figé et valeur de la ressource d'Opus. La conception de la liste fusionnée est une pièce pour Fable (règle « Qui conçoit »). 0 USD à l'étape 0.
4. **Le bras d'information dans l'agrégateur boîte blanche** (D-3 d'Opus) : à garder, mais **réécrit avec le maximum**, avec la ressemblance des scores d'attaque déclarée et la prédiction « aucun gain aux positions lues avant le premier jeton tiré ». Sur devis.
5. **Toujours ouverts, sans changement** : les quatre retouches à H10 (D-2 de Fable) ; l'inventaire des dépendances des organismes (D-4 de Fable, défaut (a)).
6. **Lectures d'antériorité** (D-5 de Fable) : ajouter Sandoval et Rushing, « Caught, Not Taught » et « Safety Does Not Compose » sur PDF, et Ker 2006 et 2007 pour le corollaire de la mémoire. Ce corollaire reste un nœud (texte du papier A), après contre-lecture du calcul D d'Opus.
7. **Errata dus à la pièce d'Opus** : la phrase des 17 % de Kutasov et al. ; la mention « moyenne seule » au facteur 2,841 ; « j'arrive seul » à atténuer.

Aucune des deux pièces ne l'emporte nettement. Fable l'emporte sur la justesse, la profondeur de l'agrégateur et l'honnêteté. Opus l'emporte sur la portée fidèle au mot de Lazar, l'originalité de la lecture par placebo, l'actionnabilité et le coût. Retenir les deux.
