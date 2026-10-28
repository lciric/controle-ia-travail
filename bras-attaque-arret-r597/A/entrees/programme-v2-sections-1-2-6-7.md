## 1. Positionnement

En une phrase : agrégation **séquentielle** (dans le temps et entre agents) de scores de **sondes internes** pour détecter les **menaces diffuses** en évaluation de contrôle, y compris quand l'attaquant est une **population d'agents à poids partagés** — et mesure de la **corruptibilité** des moniteurs eux-mêmes.

La question unique des trois papiers : **que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ?** — à la fragmentation dans le temps (A), à la corruption de l'instrument (C), à la fragmentation entre agents (B). C'est la question de validité de construit de P3, portée au contrôle.

---

## 2. Les trois papiers

| | **A — le temps** | **C — l'instrument** | **B — l'essaim** |
|---|---|---|---|
| Problématique | Le monitoring par action échoue par construction sur le sabotage diffus : chaque action est innocente prise isolément. | Le moniteur est une surface d'attaque : plutôt que passer sous le radar, l'attaquant le déplace. Quelles architectures résistent, et peut-on mesurer la corruptibilité avant déploiement ? | Les attaques distribuées battent les moniteurs par-instance, et le moniteur global est indéployable. L'accès interne rétablit-il l'avantage, et comment décroît-il avec le nombre d'agents ? |
| Thèse | La fragmentation détruit la preuve externe, pas la preuve interne : l'accumulation séquentielle de scores de sondes détecte, avec une garantie de faux positifs toujours valide, ce que le max par action rate. | La corruptibilité est un gain mesurable ; les juges génératifs ont g > 0, structuré par famille d'attaque ; les sondes à agrégation robuste ont g ≤ 0 sous attaque par contenu ; fermer le canal rhétorique impose une taxe chiffrée ; le g bénin prédit la robustesse. | Des copies partagent leurs poids, donc leurs signatures internes co-varient : une statistique spatio-temporelle rend l'essaim plus détectable que l'agent isolé ; se décorréler coûte à l'attaquant de la capacité de coordination. |
| Figure-titre | Plan 2 × 2 accès × agrégation ; rappel en fonction de l'horizon. | g par moniteur et par famille d'attaque ; taxe de déplacement. | Sécurité en fonction de N, boîte blanche contre boîte noire. |
| Hypothèses | H1, H2, L, T, H6, Tr, H8 | HC1 à HC6 (dont HC2b) | H3, H4′, H5, H7 |
| Calendrier | M1–M2 ; papier vers M3 | M1–M3 ; papier vers M4 | M3–M6 ; papier en M7 |

---

## 6. Environnements

Critère directeur : **flou à la relecture, vérifiable en aval** (vérité terrain différée).

- **(a) Propositions d'expériences — papier A, phases 0 à 2.** Des agents rédigent et révisent des propositions d'expériences d'apprentissage automatique, notées par un évaluateur faible de confiance sur rubrique structurée. Sabotage diffus : biais systématique subtil (orienter vers des directions stériles, affaiblir les contrôles, gonfler les choix coûteux), réparti sur de nombreuses propositions. Vérité terrain : cibles semées préenregistrées + vérification différée sur sous-échantillon. Base : le jeu de Terekhov et al. (arXiv 2606.08892), porté en 8 milliards de paramètres. Exigence : décomposable en contributions (i, t) qui resservent telles quelles quand N = k.
- **(b) Pipeline de code multi-rôles — papier B, phase 3.** Codeur, testeur, relecteur ; portes dérobées fragmentées sur plusieurs commits, chaque diff restant innocent. Bases : FakeLab (Makins et al., sur demande aux auteurs) ou Iterative VibeCoding (Hills et al., cadre ControlArena, état persistant), portés en poids ouverts.
- **(d) Curation de données — extension sous porte G3.** Empoisonnement diffus par des exemples individuellement plausibles ; vérité différée = comportement d'un modèle aval entraîné sur les données curées. Ne s'ouvre que si un proxy de vérité différée fiable et bon marché est validé.
- **Transfert concentré.** En fin de phase 1, le moniteur séquentiel est testé sur un cadre de sabotage concentré (ControlArena) — une figure de robustesse, pas un chantier.

---

## 7. Organismes modèles

- **(i) Instruction cachée** dans le message système.
- **(ii) Réglage fin léger (LoRA)** inculquant la politique de sabotage sans aucune instruction à l'inférence (par distillation de contexte depuis la famille (i)).
- **(iii) Organismes publics de l'institut britannique de sécurité de l'IA** (sandbagging, dont un imitant Llama-3.1-8B-Instruct, verrouillés par mot de passe), si la licence le permet — gain de temps et comparabilité.

**Prédiction de validité.** Une sonde qui lit en réalité « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii) ; une sonde d'intention réussit sur les deux.
**Contrôles croisés.** Organisme honnête averti de la surveillance (aucune mission) ; saboteur en régime simulé « non observé » — pour dissocier conscience d'évaluation et intention (alimente H8).
**Anti-circularité.** Une sonde n'est jamais entraînée et évaluée sur les mêmes organismes : entraînement sur données génériques (recettes publiées) ou sur une famille, évaluation sur une autre.

---

