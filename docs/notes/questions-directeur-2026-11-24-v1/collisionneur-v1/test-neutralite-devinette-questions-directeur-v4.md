# Test de neutralité par devinette — question groupée v4, témoin v2, faits v1

Heure de fin (`date -u`) : 2026-11-24, vers 17:50 UTC. Devinettes écrites et empreintées à 17:41 UTC, avant toute lecture des réponses : `devinettes-avant-lecture-questions-directeur-v4.md` (`5a69cf200736aae6f291c352f170be83ec7439098ae7a30f39cf4ad11d0afdb5`).
Lecteur neuf, à l'aveugle. Seuil strict : 0,50 ; toute pièce ou partie à 0,50 ou plus échoue.
Pièces jugées : `faits-neutres-questions-directeur-v1.md`, `question-neutre-groupee-questions-directeur-v4.md` (`13565a79…`), `question-temoin-neutre-questions-directeur-v2.md`.
Lues après les devinettes, pour juger : `reponse-q1-quatre-etapes-oracles-organisme-v1.md`, `reponse-q2-profondeur-surprise-retiree-v1.md`, `reponse-q3-cinetique-collisions-idees-v1.md` et son `-erratum-1.md`, `reponse-q7-couche-problemes-hypergraphe-v1.md` (verdict, sections 1 à 7), section « Question 11 » de `demandes-reformulees-quatre-points-q8-q11-v1.md`. Aucun rapport de test antérieur, aucune version antérieure des questions, rien sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`. Aucune dépense, aucun appel à un modèle externe.

## Tableau

| Pièce ou partie | Avant | Après | Devinette juste ? | Fuite constatée | Verdict |
|---|---|---|---|---|---|
| Faits v1 | 0,35 | 0,45 | oui, pour la critique du fait 3 | faible : la sélection livre les chiffres de la critique de la réponse à la question 2 | passe |
| Groupée v4, cadre | 0,30 | 0,30 | oui (règle « mesurer, pas choisir ») | non : ce sont des règles posées | passe |
| Groupée v4, partie 1 | 0,45 | 0,42 | à moitié | non sur le point clé | passe |
| Groupée v4, partie 2 | 0,40 | 0,45 | oui, pour (a) | faible | passe |
| Groupée v4, partie 3 | 0,45 | **0,50** | oui, verdict exact et raison | oui | **échoue** |
| Groupée v4, partie 4 | 0,35 | 0,40 | en partie | faible | passe |
| Groupée v4, partie 5 | 0,35 | 0,42 | en partie | faible, tempérée par « d'abord tes propres familles » | passe |
| Groupée v4, partie 6 | 0,20 | 0,20 | sans objet (aucune réponse attendue lue) | non | passe |
| Groupée v4, pièce entière | 0,40 | 0,50 (maximum des parties) | — | une partie | **échoue** |
| Témoin v2 | 0,38 | 0,35 | non : il pousse plutôt à l'opposé de l'attendu en piste 2 | non | passe |

## Par pièce et par partie

**Faits v1 (0,35 puis 0,45, passe).** La réponse à la question 2 conclut que le fait « tient, mais il est petit » (Spearman −0,166, environ 3 % de la variance, contre un R² de 0,48 sur moyennes de classes) et qu'il peut se lire comme « pertinence pour soi », puisque le premier concept vient de la liste de l'évaluateur. Ma devinette avait vu ces deux points, à partir de la juxtaposition des deux statistiques et de la mention « tiré de la liste de concepts du chercheur qui évalue ». Ce sont des faits exacts, page citée, et qu'un expert verrait aussi dans la source : l'orientation est réelle mais vient de l'information, pas du ton. Le point le plus fort de la réponse (le fait porte sur le concept parent, non sur l'idée fille) n'est pas soufflé. Sous le seuil.

**Cadre (0,30, passe).** La réponse à la question 1 applique la séparation « oracles mécaniques : choix ; lecteurs modèles : mesure seulement », qui découle des règles du cadre. C'est le cadre qui pose les contraintes, non une conclusion attendue.

**Partie 1 (0,45 puis 0,42, passe).** Juste : le second classement par une autre famille de modèles ne fait que mesurer ; la répétition générale et le pilote à témoin donnent des oracles mécaniques. Faux : j'avais placé la tension entre les règles sur l'étape (iv) ; la réponse la place sur l'étape (i), une vérité tirée de la graine mais lue par des modèles lecteurs (« oracle du monde planté » ou « score de juge » ?). La question ne dit pas que (i) passe par des lecteurs : le nœud principal n'est pas soufflé. Légère baisse.

**Partie 2 (0,40 puis 0,45, passe).** Juste pour (a) : corrélation faible au niveau de l'idée, cause non établie, familiarité de l'évaluateur. L'hypothèse rivale « pertinence pour l'évaluateur » nommée dans la question est celle que retient la réponse ; elle est posée comme rivale à éprouver, ce qui est équilibré. Non soufflé : parent contre fille, symétrie et borne de la surprise retirée, verdict « mesure rapportée seulement tant qu'un monde planté ne l'a pas validée ». La mention « le rôle d'une pondération éventuelle » laisse deviner que la pondération est suspecte (la réponse dit qu'elle fait revenir le nœud par la fenêtre) ; je ne l'avais pas deviné à l'aveugle.

**Partie 3 (0,45 puis 0,50, échoue).** Ma devinette à l'aveugle donnait le verdict exact de la réponse, « garder en partie », et sa raison principale : le « champ d'interaction » de la cinétique double le « terme de champ » du modèle existant (la réponse : « champ, au sens physique : écarté », déjà absorbé). Deux phrases y poussent : (1) le modèle existant est décrit comme faisant intervenir « un terme de champ », ce qui désigne d'avance la redondance du champ ; (2) le point (b) présuppose l'existence d'un apport, « Les prédictions que la cinétique ferait et que le modèle existant ne fait pas, chacune avec son test », sans le « s'il y en a » que portent les parties 2 (d) et 4 (c) ; avec l'option « écarté » en (a), cela tire vers le verdict médian. Non soufflé : les quatre prédictions de forme, l'identification de la barrière par la température d'échantillonnage. À 0,50 : échec au seuil strict.
**Retouche (une ligne)** : écrire en (b) « Les prédictions, s'il y en a, que la cinétique ferait… » et décrire le modèle existant par « la structure du graphe, la proximité en surface et un terme propre à la paire » au lieu de « un terme de champ ».

**Partie 4 (0,35 puis 0,40, passe).** Juste en partie : « aucune ne l'emporte » (la réponse : aucun modèle ne domine, d'où une fusion) et l'hypergraphe parmi les choix plausibles. La forme retenue (hypergraphe orienté, hyperarcs « prémisses → cible », poids selon Laudan et Kuhn, couplage par un paramètre δ) n'est pas soufflée. Le « dis si aucune ne l'emporte » rend le nul légitime sans l'imposer.

**Partie 5 (0,35 puis 0,42, passe).** La section « Question 11 » montre que les six familles listées sont celles de l'auteur, et que les contrôles demandés (« graphe recâblé », « à l'intérieur d'un même champ ») sont ses nuls (recâblage, effets fixes par champ). La réponse à la question 7 extrait d'abord des « conflits de signe entre groupes indépendants », la famille que je devinais en tête. La v4 corrige l'ancrage du texte d'origine (« Par exemple, sans t'y limiter ») par « Propose d'abord tes propres familles… Puis seulement » ; aucune famille n'est désignée comme attendue. Sous le seuil. Retouche facultative : présenter la liste dans un ordre tiré au hasard, ou y ajouter une famille que l'auteur ne retient pas.

**Partie 6 (0,20, passe).** Aucune réponse attendue lue pour l'ordre d'ensemble ; aucune phrase d'orientation.

**Témoin v2 (0,38 puis 0,35, passe).** La formule la plus orientée (« Comment le mesurer, et comment s'en servir ? », piste 2) pousse vers l'usage, alors que la réponse attendue limite l'usage à une mesure rapportée : elle ne fait pas deviner l'attendu. Piste 3 « s'il y a quelque chose » équilibre. Retouche facultative : « et faut-il s'en servir ? ».

## Verdict

- Faits v1 : passe (0,45).
- Témoin v2 : passe (0,35).
- Question groupée v4 : **échoue**, par sa seule partie 3 (0,50, fuite constatée : verdict « garder en partie » et redondance du champ devinés à l'aveugle). Cadre et parties 1, 2, 4, 5, 6 passent (0,20 à 0,45).
- **Verdict global : échec**, réparable par une retouche d'une ligne de la partie 3 (« s'il y en a » en (b) ; « un terme propre à la paire » au lieu de « un terme de champ »), puis nouveau test par un lecteur neuf. Parties 1 et 2 et faits proches du seuil (0,42 à 0,45) : à surveiller au prochain test.
