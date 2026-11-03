# Classement D — question de Jérémy Scheurer (tendance d'échelle d'un comportement désaligné) — v1

Classeur neuf D, 3 novembre 2026, de 14:52:48 à environ 15:13 (temps universel, `date -u`) ; interruption par le redémarrage du serveur après l'écriture de `notes-v1.json`, reprise à 15:05:47 sur la même consigne scellée (`b2990e43…`, vérifiée deux fois). Aucune recherche, aucun modèle autre que le classeur, aucune provenance connue.

**Pas de témoin déguisé (échéance) : l'axe d'originalité n'est pas contrôlé.** Les notes d'originalité ne viennent que de la moisson (non opposable : résumés et métadonnées).

## Entrées (empreintes vérifiées avant lecture)
- Fiches : `/home/claude/scratch/soir-rapport/scheurer/prep-v1/fiches-servies-v1.json`, `e1545f70…5cda`, conforme ; 14 fiches.
- Moisson : `/home/claude/scratch/soir-rapport/scheurer/moisson-C/moisson-fusionnee-v1.json`, `f0c30258…64a0`, conforme ; 14 entrées, toutes « voisin », aucune réfutée.
- Protocole du soir, étape D : `fbbbb520…b347`, conforme. Ancres : protocole Heimersheim v1, section 5 (empreinte lue `942b9324…ad18`, aucune attendue donnée). Pièce du mentor, section 1 (empreinte lue `2d0e60fc…3796`, aucune attendue donnée).

## 1. Porte
- **Dans le sujet (10)** : SC-01, SC-03, SC-04, SC-06, SC-07, SC-08, SC-09, SC-10, SC-12, SC-13 (chacune vise un énoncé « croît ou décroît d'un facteur X » par mois, par an ou par unité de calcul).
- **Hors sujet, en annexe, non classées (4)** : SC-02 (déférence d'un moniteur à une note impérative ou déclarative ; deux tailles en bras de réplication, aucun axe ; cas limite, car elle touche la surveillance) ; SC-05, SC-11, SC-14 (mécanismes de la complaisance d'un seul modèle ou d'une campagne, aucun axe, aucune tendance).

## 2. Notes (raisons d'une ligne dans `notes-v1.json`)
Règles de lecture gelées avant tout jugement (dans `notes-v1.json`). Le classeur ne complète jamais une fiche de ses propres connaissances.

| Fiche | Originalité | Testable en jours | Outil du mentor | Somme |
|---|---|---|---|---|
| SC-03 | 1 | 2 | 3 | 6 |
| SC-12 | 1 | 1 | 3 | 5 |
| SC-01 | 2 | 1 | 1 | 4 |
| SC-13 | 2 | 1 | 1 | 4 |
| SC-04 | 1 | 1 | 2 | 4 |
| SC-09 | 1 | 1 | 2 | 4 |
| SC-06 | 1 | 1 | 1 | 3 |
| SC-10 | 1 | 1 | 1 | 3 |
| SC-08 | 1 | 1 | 1 | 3 |
| SC-07 | 1 | 1 | 0 | 2 |

**Départage au seuil des huit** : SC-06, SC-08 et SC-10 sont à égalité sur la somme, l'originalité, la testabilité et l'outil. J'ai donc fait un tirage annoncé avant le tirage : `default_rng(SeedSequence(e).spawn(1)[0])`, avec e = 16236707493325541679 (les 16 premiers hexadécimaux de l'empreinte des fiches). Ordre tiré : SC-06, SC-10, SC-08. **SC-08 sort neuvième.**

## 3. Comparaisons par paires et forces de Bradley-Terry
- 28 paires × 2 ordres = 56 jugements, présentés dans l'ordre `default_rng(SeedSequence(e)).permutation(56)` (indice j : paire j // 2 des huit triées, ordre canonique si j est pair). Question gelée : « laquelle ferait une réponse à cette question plus juste, plus originale et plus mémorable pour ce mentor, sur ces trois critères ? ». Jugements écrits en quatre lots (`paires-v1.jsonl`).
- Script `bradley_terry_scheurer_v1.py` (numpy 2.5.3, algorithme MM). Avant tout calcul, 14 épreuves passent : 3 cas sains (cycle à trois ; forces connues retrouvées ; chaîne complète à cohérence 25/28) et 11 artefacts (jugement manquant, double, identifiant inconnu, gagnant hors paire, paire réflexive, même ordre deux fois, position fausse, ordre hors tirage, tournoi parfait, non-convergence, sortie existante). Chacun lève son erreur ; aucun repli silencieux. Un premier cas sain mal construit a été refusé par la garde, puis corrigé.
- **Maximum de vraisemblance inexistant** : SC-03 ne perd jamais et SC-06 ne gagne jamais, donc le graphe des victoires n'est pas fortement connexe. Je l'ai déclaré, puis j'ai calculé une estimation régularisée annoncée (pseudo-compte de 0,5 victoire par sens et par paire). Son ordre est identique à l'ordre par victoires, sans égalité.

| Rang | Fiche | Victoires sur 14 | Force régularisée (somme 1) | Log centré |
|---|---|---|---|---|
| 1 | SC-03 | 14 | 0,390 | +1,61 |
| 2 | SC-10 | 12 | 0,230 | +1,08 |
| 3 | SC-13 | 10 | 0,146 | +0,63 |
| 4 | SC-01 | 7 | 0,078 | −0,00 |
| 5 | SC-12 | 6 | 0,063 | −0,21 |
| 6 | SC-04 | 5 | 0,051 | −0,42 |
| 7 | SC-09 | 2 | 0,026 | −1,08 |
| 8 | SC-06 | 0 | 0,016 | −1,61 |

- **Cohérence** : 27 paires sur 28, soit 0,964. Seule discordante : SC-01 contre SC-04 (rangs 22 et 48 ; chaque fois la fiche présentée en premier gagne). Part des jugements gagnés par la position A : 0,518.

## 4. Réserves
- **Cohérence presque parfaite d'un juge unique** (seuil gelé : 0,95). Un même juge a fait les deux ordres en se souvenant du premier, et a pesé chaque paire critère par critère. Les deux ordres ne sont donc pas indépendants : la cohérence ne mesure pas la robustesse du classement, seulement l'absence de basculement par l'ordre.
- L'ordre par paires s'écarte de l'ordre par somme. SC-10 passe de la queue (3, entrée par tirage) au 2e rang ; SC-12 passe du 2e au 5e rang. Les paires ont pesé le « plus juste » (vérité mécanique, protocole chiffré, thèse non contestable), que les notes grossières ne voient pas : 9 fiches sur 10 ont 1 en testabilité. Sans le tirage, SC-10 aurait été hors des huit. Le haut du classement dépend donc d'un tirage au seuil.
- Les jugements serrés sont signalés dans `paires-v1.jsonl` (rangs 5, 8, 22, 28, 34, 48, 52) : SC-12 contre SC-04, SC-01 contre SC-04, SC-09 contre SC-06, SC-04 contre SC-13. Les rangs 4 à 6 sont presque à égalité de force.
- Les fiches de tendance datée partagent une même déclaration d'échec : sans panel ouvert multifamille daté, aucune pente calendaire. Aucune fiche ne nomme un tel panel chiffré.

## 5. Drapeaux de risque devant ce mentor (affirmation qu'il pourrait contredire de ses propres travaux)
- **SC-12 : oui, fort.** Elle affirme que la pente de sa sous-performance sans but suit les refus (corrélation > 0,7, supposée). Or le mentor a les données : tableau 6 de 2412.04984, où sonnet-3.5 et opus-3 sous-performent et o1 non. Le billet de son groupe de juin 2025 (moisson) trouve aussi des taux plus élevés chez les modèles plus capables. Enfin, le sens des deux scores du tableau 6 n'est pas donné par la pièce : risque de mal lire sa propre table.
- **SC-09 : oui, fort.** C'est la question que son groupe déclare étudier (mise à jour du 13 mai 2026), donc il peut avoir des résultats non publiés contre la croissance monotone. De plus, 2509.15541 ne donne que deux points (2,0 % puis 20,5 %, ou 20,6 % sur l'étiquette de la figure) : une courbe monotone n'en découle pas.
- **SC-03 : oui, faible.** Elle prédit une surveillance par la trajectoire entière (le mode de son outil) en progrès, alors que son groupe écrit que la détection deviendra plus difficile. Elle doit donc se présenter comme une détection d'anomalies non adaptatives, et non comme une détection du désalignement.
- **SC-04 : oui, faible**, pour la même raison (trajectoire entière, signe positif, +5,1 % par mois supposé).
- **SC-01, SC-06, SC-10, SC-13 : non.** Rien de la section 1 ne mesure leur grandeur. SC-01 s'accorde avec sa limite de sous-estimation. SC-10 prévoit déjà, par son duel de transport, l'érosion par des attaquants contemporains.
- Hors des huit : **SC-07 : non ; SC-08 : non** devant le mentor. Mais la moisson signale qu'un auteur tiers a abandonné la même idée (horizon dépendant du moniteur et du modèle).

## 6. Fichiers (dans ce dossier seulement)
- `notes-v1.json` — `e3903a01c7975f0353290ae72fcf7dcf7c90ae6965c921a71c15d7ac42e84558`
- `paires-v1.jsonl` — `70978b058f359db68ae5dd6f5687aed53000c1077ef957ce4506ee644a8170f8`
- `bradley_terry_scheurer_v1.py` — `f9d1d0a6e760e79759f9ce87d36b61878fba58dcab58956538f1842d12d53835`
- `bradley_terry_scheurer_v1-sortie.json` — `3ae0beb402cb4e150eb607df056e524a2eee165300cd1a28f521471196a34d76` (porte les empreintes du script, des paires et des notes qui l'ont produite)
- `classement-v1.md` — ce fichier, empreinte donnée dans la réponse finale.

Interdits tenus : aucun commit, aucun `.sha256`, aucun `git`, aucun fichier existant modifié hors de ce dossier neuf, rien sous `donnees/`, aucune recherche sur le web, aucun dossier interdit ouvert.
