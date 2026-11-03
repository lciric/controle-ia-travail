# Classement A — réponse à la question 1 de Heimersheim (direction (c)) — classeur neuf D — v1

Écrit le 2026-11-03 12:18 UTC (`date -u`) par le classeur neuf D, aveugle à la provenance et aux témoins ; aucune recherche, aucun appel de modèle.

- Consigne : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/ideation-rapport-classeur-D-A-prompt.md` (sha256 `d12ee04cdd997d29ffe9329b099395a516f29dcf6a758285ea0b40612e5b427f`).
- Protocole : `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v1.md` §5 (`942b93241b6e033e34cc7cb035fe1d70f6e944a8a98bc4c556b83b0d7fdbad18`) et `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/protocole-rapport-idees-v2.md` §2 (`cfff33cf1b6ed74790a5615147868e96668334912379755e8aae66dcbe5d86ed`).
- Fiches : `/home/claude/scratch/ideation-rapport/melange-v1/fiches-classement-A-v1.json` (`a5ca1deed4dba13060e3f10452ec3fbf5837400b935c80c06fac43530d02983d`) ; moisson : `/home/claude/scratch/ideation-rapport/moisson-C/moisson-fusionnee-v1.json` (`4033b82331eef2b7e3360c2e8af707899b43b23f7c83464d52dd5be4b3f85f20`) ; question servie : `/home/claude/controle-ia-travail/brouillons/ideation-heimersheim-v1/question-ideation-heimersheim-v1.md` (`e9528e254e2dcad9506e323d3bcd9101e458628dd9c6dabfa4e96174ce660007`).
- Notes : `/home/claude/scratch/ideation-rapport/classement-D/notes-A-v1.json` (`2e0b932e26273d06b2e9a3e4fefca86c95dfcc31755c360c9cd9cc64e4e5b956`) ; jugements : `/home/claude/scratch/ideation-rapport/classement-D/paires-A-v1.jsonl` (`5c09ccef4073be6338f86090968195f659a41e68b8fc8f1a6f7dec930580d74c`) ; script : `/home/claude/scratch/ideation-rapport/classement-D/bradley_terry_v1.py` (`347e3de27ebc6692e0d0ce38f8bab0d86889b0721374deaed32e36c68a9b0756`) ; sortie : `/home/claude/scratch/ideation-rapport/classement-D/bradley_terry_v1-sortie.json` (`901733ee359be0aafa0a02b9d7252d5a8ec2eba7c85aa444012157cef327fe4b`) et `/home/claude/scratch/ideation-rapport/classement-D/bradley_terry_v1-sortie.txt` (`9863a954deb9b41adbc631b2a1abd26bd098606c6ca779ac6b696831e2c1baf3`).

## Verdict

Ordre final : 1 M-066 ; 2 M-079 ; 3 M-020 ; 4= M-014 ; 4= M-023 ; 6 M-058 ; 7 M-032 ; 8 M-072 ; 9 M-075 ; 10 M-025 ; 11 M-042 ; 12 M-001.

Cohérence : 65 paires sur 66 concordent dans les deux ordres, soit 0.985 (au-dessus de 0,8, donc pas de réserve de seuil) ; seule discordante : M-014 / M-023. La réserve 1 ci-dessous s'applique (R4 : une cohérence presque parfaite d'un juge unique est une réserve).

Drapeaux de risque devant ce mentor : **oui** pour M-014 et M-023 (4ᵉ ex aequo) ; **non** pour les dix autres, avec quatre mises en garde (M-020, M-058, M-079, et hors des douze M-033).

| rang | fiche | originalité | testable | outil du mentor | somme | force (alpha = 1) | victoires–défaites | drapeau |
|---|---|---|---|---|---|---|---|---|
| 1 | M-066 | 2 | 3 | 3 | 8 | 69.3848 | 22–0 | non |
| 2 | M-079 | 1 | 3 | 3 | 7 | 21.5635 | 20–2 | non |
| 3 | M-020 | 2 | 3 | 2 | 7 | 9.1778 | 18–4 | non |
| 4= | M-014 | 1 | 3 | 3 | 7 | 3.2809 | 15–7 | oui |
| 4= | M-023 | 1 | 3 | 3 | 7 | 3.2809 | 15–7 | oui |
| 6 | M-058 | 1 | 3 | 3 | 7 | 1.3448 | 12–10 | non |
| 7 | M-032 | 2 | 3 | 2 | 7 | 0.7571 | 10–12 | non |
| 8 | M-072 | 2 | 3 | 1 | 6 | 0.4196 | 8–14 | non |
| 9 | M-075 | 2 | 3 | 1 | 6 | 0.2224 | 6–16 | non |
| 10 | M-025 | 2 | 3 | 1 | 6 | 0.1086 | 4–18 | non |
| 11 | M-042 | 2 | 3 | 1 | 6 | 0.046 | 2–20 | non |
| 12 | M-001 | 2 | 3 | 1 | 6 | 0.0143 | 0–22 | non |

## Porte

71 fiches reçues ; aucune n'est passée en réfutée à la moisson (ses contradictions sont des propositions « à trancher » : les fiches restent gardées) ; 7 hors sujet d'après la règle du protocole v1 §2 (ne porte ni sur pourquoi la direction (c) échouerait, ni sur comment l'éprouver), jugées sur le seul texte ; 64 classées.

Hors sujet, en annexe, non classées :
- M-002 (moisson : voisin) — Origine de l'attraction sous éloge de la note finale (prose générée contre suffixe) : ni conscience d'évaluation, ni direction, ni pilotage.
- M-006 (moisson : voisin) — Lisibilité d'une sonde de sycophantie dans la reconstruction de l'autoencodeur Goodfire : aucun lien énoncé avec la direction (c).
- M-012 (moisson : voisin) — Critère d'instrument pour une sonde de sycophantie : ne porte ni sur l'échec de la direction (c) ni sur son épreuve.
- M-045 (moisson : voisin) — Position du chiffre dans l'auto-notation sous éloge : ni conscience d'évaluation ni pilotage.
- M-056 (moisson : voisin) — Lieu de calcul du gain de sycophantie (perceptrons précoces) : ni conscience d'évaluation ni pilotage.
- M-059 (moisson : voisin) — Spécificité de l'ablation de rang 3 de sycophantie contre des ablations aléatoires appariées : même logique de témoins, mais sur la sycophantie, sans lien énoncé avec la direction (c).
- M-062 (moisson : ouverte) — Mélange contre contraction des notes sous pression (sycophantie) : seule fiche « ouverte » du fichier, mais hors du sujet de la direction (c).

Contradictions proposées par la moisson, à trancher par le directeur (fiches gardées et classées) : M-003, M-014, M-017, M-033, M-046, M-073, M-078.

## Les douze : notes, raisons, drapeau

### 1. M-066 — somme 8, force 69.3848
- Originalité vérifiée 2 : La géométrie avant pilotage prédit la pilotabilité de traits d'autoencodeur (2609.22782, 2606.08365) ; 2606.24964 donne p sans le relier à la sélectivité causale.
- Testable en jours 3 : Superellipse sur plans gelés, seuils mesurés séparément, seuil (borne < +0,20), 3 à 4 jours.
- Prolonge un outil du mentor 3 : Mesure neuve : corrélation entre p et la fenêtre statut / dégât, que ses papiers ne font pas.
- Drapeau : **non** — Lit p > 2 comme correction par trait, comme ses papiers ; aucune prédiction contraire.

### 2. M-079 — somme 7, force 21.5635
- Originalité vérifiée 1 : SteerCheck (2608.24335) emploie des directions nulles du sous-espace principal à budget apparié (complaisance, Qwen3-14B) ; 2410.12555 donne la base améliorée pour la sensibilité de GPT-2.
- Testable en jours 3 : 50 témoins par dose, seuil (99ᵉ centile à toutes les doses de 0,5 à 1,5 fois la dose de travail, médiane ≤ 5 points), 3 jours.
- Prolonge un outil du mentor 3 : Sa base appariée à la covariance et l'argument du plateau deviennent la mesure de spécificité du vecteur d'évaluation.
- Drapeau : **non** — Conforme à ses résultats (gaussiens isotropes sous le plateau) ; ne pas affirmer que sa base « occupe le même sous-espace que les traits » sans le vérifier sur le PDF.

### 3. M-020 — somme 7, force 9.1778
- Originalité vérifiée 2 : Comportement qui bouge sans verbalisation (Vu et Saunders, atelier ICML 2026), axes faiblement couplés (2606.23583) ; l'ordre des doses de rupture verbalisation / action n'est mesuré nulle part.
- Testable en jours 3 : Choix forcé en un jeton, témoin de registre, seuils (rapport dans [0,9 ; 1,1] ; 25 %), 6 heures sur une A100.
- Prolonge un outil du mentor 2 : Fait de la rupture du plateau la grandeur mesurée, sortie par sortie (verbale, action), lue en doses à 50 % plutôt qu'en divergence.
- Drapeau : **non** — Aucune prédiction contraire à ses résultats ; l'emploi de « plateau » pour une dose à 50 % est à préciser devant lui.

### 4=. M-014 — somme 7, force 3.2809
- Originalité vérifiée 1 : Même mesure et même modèle dans 2606.24964 (exposant p, témoins aléatoires à p ≈ 2) ; seul le plan évaluation × registre orthogonalisé est neuf.
- Testable en jours 3 : 36 angles, rupture à KL > 0,1, seuil (p ≥ 2,25 avec IC excluant 2,05), 2 jours sur une carte.
- Prolonge un outil du mentor 3 : Mesure p dans un plan que ses papiers n'ont pas testé, pour trancher trait d'évaluation contre registre.
- Drapeau : **oui** — Prédit p ≈ 2 dans le plan de deux directions contrastives ; 2606.24964 rapporte p > 2 pour les directions contrastives, Llama-3.1-8B compris (proposition de réfutation partielle de la moisson).
- Remarque : Contradiction proposée par la moisson, à trancher par le directeur (fiche gardée) : {"nature": "proposition de réfutation partielle (résultat général contre prédiction particulière ; à trancher)", "identifiant": "arXiv:2606.24964", "phrases": ["We find $p>2$ for contrastive, MELBO, and SAE-decoder directions", "These results replicate across Gemma-2-9B, Qwen3-1.7B, Llama-3.1-8B"], "portee": "La fiche prédit p ≈ 2 (comme le témoin aléatoire) dans un plan de deux directions contras

### 4=. M-023 — somme 7, force 3.2809
- Originalité vérifiée 1 : Méthode publiée (2606.24964 : p, directions pures contre mélanges, témoins à p ≈ 2) ; la comparaison plan d'évaluation / plan de registre est neuve.
- Testable en jours 3 : Procédure à norme constante, seuil (différence ≤ +0,10), 4 jours, 16 heures de calcul.
- Prolonge un outil du mentor 3 : Mesure neuve : p comparé entre plan d'évaluation et plan de registre avec la même non-caractéristique.
- Drapeau : **oui** — Prédit p ≈ 1,9 à 2,1 dans le plan d'une direction de registre contrastive ; 2606.24964 rapporte p > 2 pour les directions contrastives, Llama-3.1-8B compris.

### 6. M-058 — somme 7, force 1.3448
- Originalité vérifiée 1 : Méthode et modèle mêmes dans 2606.24964 (plateaux, p sur mélanges de deux directions, Llama-3.1-8B) ; seul le plan (évaluation⊥, registre⊥) est neuf.
- Testable en jours 3 : Rupture en KL sur 200 invites, superellipse sur trois plans, seuil (rapport ≤ 1,3), environ 7 heures.
- Prolonge un outil du mentor 3 : Seuil de rupture et p appliqués à la composante d'évaluation orthogonale au registre : mesure absente de ses papiers.
- Drapeau : **non** — Prédictions conformes à ses résultats (p > 2 pour les directions contrastives) ; les valeurs de référence citées (≈ 2,3 ; 2,05 ; ≈ 70) viennent de la pièce, à vérifier sur le PDF.

### 7. M-032 — somme 7, force 0.7571
- Originalité vérifiée 2 : Plan 2 × 2 en lecture seule (2603.19426), direction qui suit le cadrage sans test causal (2608.13329) ; le transfert causal croisé entre registres manque.
- Testable en jours 3 : Plan 2 × 2, tâches tenues à l'écart, oracle, seuil (avantage ≤ 0,05), 3 jours.
- Prolonge un outil du mentor 2 : Étalonne toutes les directions à dose de rupture du plateau comparable : l'outil sert d'étalon.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

### 8. M-072 — somme 6, force 0.4196
- Originalité vérifiée 2 : Organisme à indice unique (2510.20487), facteurs empilés sans pilotage (2605.23055) ; dose de retour au plancher en fonction du nombre d'indices, absente.
- Testable en jours 3 : LoRA 4 h, 6 conditions, seuil (15 points sous le plancher, au-delà du 95ᵉ centile), 4 jours sur 40 Go.
- Prolonge un outil du mentor 1 : Témoins appariés à la covariance (base de 2410.12555) pour fixer la dose de dégât.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

### 9. M-075 — somme 6, force 0.2224
- Originalité vérifiée 2 : Format de banc par sondes (2603.19426), organisme à un seul marqueur chargé en registre (2510.20487) ; l'organisme à deux marqueurs dont un neutre en registre manque.
- Testable en jours 3 : LoRA 3 h, 6 doses, lecture syntaxique, seuils (10 % ; 30 points), 2 jours sur 24 Go.
- Prolonge un outil du mentor 1 : Témoins appariés à la covariance (base de 2410.12555) pour borner l'effet générique.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

### 10. M-025 — somme 6, force 0.1086
- Originalité vérifiée 2 : Non-surjectivité générale (2604.09839) et mise à jour partielle (commentaire Alignment Forum) ; la batterie de 20 comportements comparée aux conditions « sans indice » et « déploiement » manque.
- Testable en jours 3 : Quatre conditions, distances de profil, seuil (d(i, iv) ≤ d(i, iii)), 2,5 jours sur une carte de 40 Go.
- Prolonge un outil du mentor 1 : Témoin de 20 vecteurs appariés à la covariance (base améliorée de 2410.12555), employé comme simple témoin de distance.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

### 11. M-042 — somme 6, force 0.046
- Originalité vérifiée 2 : 2510.20487 pilote en présence de l'indice seulement ; condition sans indice, plancher et asymétrie entre les deux sens absents des voisins.
- Testable en jours 3 : LoRA 3 h, 8 doses × 2 sens, seuil (15 points sous le plancher, au-delà du 95ᵉ centile), 2 jours sur 24 Go.
- Prolonge un outil du mentor 1 : Témoins appariés à la covariance (base de 2410.12555) parmi d'autres.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

### 12. M-001 — somme 6, force 0.0143
- Originalité vérifiée 2 : Voisins sur la conscience d'évaluation (2608.27340 : agrégat qui masque une composante ; 2505.14617 : signe variable entre modèles) ; signe de l'excès spécifique variable entre tâches d'un même modèle, absent.
- Testable en jours 3 : Protocole préenregistré clair (9 doses, 24 tâches dont 12 réservées), seuil de mort à 0,25, 4 jours sur une carte de 24 Go.
- Prolonge un outil du mentor 1 : Cite le plateau comme région de la grille de doses (plateau, rupture, dégât), sans le mesurer.
- Drapeau : **non** — Aucune affirmation sur les outils du mentor.

## Notes des 64 fiches classées

Ordre : somme, puis originalité, puis identifiant. Raisons en une ligne dans `notes-A-v1.json`.

| fiche | originalité | testable | outil | somme | drapeau |
|---|---|---|---|---|---|
| M-066 (douze) | 2 | 3 | 3 | 8 | non |
| M-020 (douze) | 2 | 3 | 2 | 7 | non |
| M-032 (douze) | 2 | 3 | 2 | 7 | non |
| M-014 (douze) | 1 | 3 | 3 | 7 | oui |
| M-023 (douze) | 1 | 3 | 3 | 7 | oui |
| M-058 (douze) | 1 | 3 | 3 | 7 | non |
| M-079 (douze) | 1 | 3 | 3 | 7 | non |
| M-001 (douze) | 2 | 3 | 1 | 6 | non |
| M-025 (douze) | 2 | 3 | 1 | 6 | non |
| M-042 (douze) | 2 | 3 | 1 | 6 | non |
| M-072 (douze) | 2 | 3 | 1 | 6 | non |
| M-075 (douze) | 2 | 3 | 1 | 6 | non |
| M-081 | 2 | 3 | 1 | 6 | non |
| M-033 | 1 | 3 | 2 | 6 | non |
| M-078 | 1 | 2 | 3 | 6 | non |
| M-082 | 1 | 3 | 2 | 6 | non |
| M-011 | 2 | 3 | 0 | 5 | non |
| M-026 | 2 | 3 | 0 | 5 | non |
| M-028 | 2 | 3 | 0 | 5 | non |
| M-031 | 2 | 3 | 0 | 5 | non |
| M-035 | 2 | 3 | 0 | 5 | non |
| M-037 | 2 | 3 | 0 | 5 | non |
| M-038 | 2 | 2 | 1 | 5 | non |
| M-046 | 2 | 3 | 0 | 5 | non |
| M-047 | 2 | 3 | 0 | 5 | non |
| M-049 | 2 | 3 | 0 | 5 | non |
| M-052 | 2 | 3 | 0 | 5 | non |
| M-055 | 2 | 3 | 0 | 5 | non |
| M-057 | 2 | 3 | 0 | 5 | non |
| M-067 | 2 | 2 | 1 | 5 | non |
| M-083 | 2 | 3 | 0 | 5 | non |
| M-003 | 1 | 3 | 1 | 5 | non |
| M-043 | 1 | 3 | 1 | 5 | non |
| M-061 | 1 | 3 | 1 | 5 | non |
| M-068 | 1 | 3 | 1 | 5 | non |
| M-080 | 1 | 3 | 1 | 5 | non |
| M-004 | 2 | 2 | 0 | 4 | non |
| M-013 | 2 | 2 | 0 | 4 | non |
| M-022 | 2 | 2 | 0 | 4 | non |
| M-074 | 2 | 2 | 0 | 4 | non |
| M-007 | 1 | 3 | 0 | 4 | non |
| M-009 | 1 | 3 | 0 | 4 | non |
| M-010 | 1 | 3 | 0 | 4 | non |
| M-016 | 1 | 3 | 0 | 4 | non |
| M-019 | 1 | 2 | 1 | 4 | non |
| M-021 | 1 | 3 | 0 | 4 | non |
| M-024 | 1 | 3 | 0 | 4 | non |
| M-027 | 1 | 3 | 0 | 4 | non |
| M-029 | 1 | 3 | 0 | 4 | non |
| M-030 | 1 | 3 | 0 | 4 | non |
| M-034 | 1 | 3 | 0 | 4 | non |
| M-036 | 1 | 3 | 0 | 4 | non |
| M-039 | 1 | 3 | 0 | 4 | non |
| M-040 | 1 | 3 | 0 | 4 | non |
| M-044 | 1 | 3 | 0 | 4 | non |
| M-048 | 1 | 3 | 0 | 4 | non |
| M-050 | 1 | 3 | 0 | 4 | non |
| M-063 | 1 | 3 | 0 | 4 | non |
| M-069 | 1 | 3 | 0 | 4 | non |
| M-070 | 1 | 3 | 0 | 4 | non |
| M-073 | 1 | 3 | 0 | 4 | non |
| M-064 | 0 | 3 | 0 | 3 | non |
| M-015 | 2 | 0 | 0 | 2 | non |
| M-017 | 1 | 0 | 0 | 1 | non |

## Comparaisons par paires et forces

- Douze premières par somme, égalités départagées par l'originalité ; à la coupure, six fiches restent ex aequo (somme 6, originalité 2, mêmes trois notes) : M-001, M-025, M-042, M-072, M-075, M-081. Départage résiduel, hors protocole : ordre des identifiants opaques (réattribués par permutation à l'étape B). M-081 est donc la treizième, non comparée (réserve 2).
- 66 paires × 2 ordres = 132 jugements sur la question gelée, ordre de présentation tiré par `numpy.random.default_rng(numpy.random.SeedSequence(entropie)).permutation(132)`, entropie 11946393873164247344 (16 premiers hexadécimaux `a5ca1deed4dba130` du sha256 des fiches) ; chaque jugement écrit au fichier par lots, dans l'ordre tiré, avec son heure ; le script refait le tirage et vérifie l'ordre rang par rang.
- La fiche présentée en premier gagne 67 fois sur 132.
- Condition d'existence de l'estimateur (Ford) : non remplie (séparation : M-066 gagne ses 22 jugements, M-001 perd les siens) ; forces régularisées par un témoin fictif de force 1 (une victoire et une défaite virtuelles par fiche, alpha = 1), algorithme de minorisation-maximisation, moyenne géométrique 1. Rangs identiques pour alpha = 1, 0,5 et 0,1 : oui ; seules les valeurs des forces dépendent d'alpha.
- Auto-contrôle des gardes (R5), dans la sortie : garde de l'ordre, cas sain (fichier réel) : réussi ; garde de l'ordre, artefact (deux rangs échangés) refusé : réussi ; garde de l'ordre, artefact (jugement manquant) refusé : réussi ; Ford, artefact (ordre parfait) détecté non rempli : réussi ; Ford, cas sain (cycle) détecté rempli : réussi ; forces retrouvées sur données exactes (écart log < 1e-6) : réussi.

## Drapeaux de risque devant ce mentor

- **M-014, oui** : prédit p ≈ 2 dans le plan de deux directions contrastives (évaluation, registre orthogonalisé) ; 2606.24964, son papier, rapporte p > 2 pour les directions contrastives, Llama-3.1-8B compris (extrait de la moisson ; la moisson en fait une proposition de réfutation partielle).
- **M-023, oui** : prédit p ≈ 1,9 à 2,1 dans le plan d'une direction de registre, contrastive elle aussi ; même papier, même raison. Le volet évaluation (p de 2,2 à 2,6) est, lui, conforme.
- Mises en garde, drapeau non : M-020 (« plateau » employé pour une dose à 50 %, à préciser devant lui) ; M-058 (valeurs de référence ≈ 2,3, 2,05 et ≈ 70 reprises de la pièce, à vérifier sur le PDF) ; M-079 (ne pas affirmer que sa base appariée à la covariance « occupe le même sous-espace que les traits » sans le vérifier) ; M-033, hors des douze (tension possible avec ses directions sensibles).
- Base des drapeaux : extraits de la moisson et ce que je sais de ces papiers ; aucun PDF rouvert (pas de web) ; R7 : aucun chiffre de ces papiers n'est opposable ici.

## Réserves

1. **Cohérence presque parfaite (0.985), lue comme réserve (R4)** : un seul juge, dans une seule session, qui se souvient de ses jugements précédents ; les deux ordres d'une paire ne sont pas indépendants. Le chiffre mesure seulement l'absence de basculement par l'ordre de présentation (67 victoires sur 132 pour la première présentée), pas la fiabilité entre juges. La seule discordance (M-014 / M-023) tient à deux fiches de notes identiques.
2. **Départage résiduel hors protocole** pour la douzième place (six fiches à notes identiques) ; avec un autre départage neutre, M-081 entrerait à la place de l'une des cinq autres (M-001, M-025, M-042, M-072, M-075).
3. **Porte** : les sept hors sujet sont ma lecture du seul texte, sans la provenance ; la v2 du protocole met dans le classement A les idées que le collisionneur destine à Heimersheim. Si certaines de ces sept en viennent, c'est au directeur de les réintégrer. M-062, la seule fiche « ouverte » du fichier, en fait partie.
4. **Originalité d'après la moisson seulement** (métadonnées et résumés, non opposable) ; toute la moisson fusionnée a servi : pour M-070, M-078 et M-082, le voisin décisif vient de la moisson d'une autre fiche (M-073, M-079, M-043), c'est dit dans la raison. M-064 est « déjà fait » (originalité 0).
5. **M-010** : la moisson n'a pas pu lire 2607.20436 (« Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch… ») et demande de l'ouvrir avant le classement ; je n'ai pas de web : sa note d'originalité (1) est provisoire. M-010 n'est pas dans les douze.
6. **Contradictions à trancher** : la moisson propose une réfutation partielle pour M-014 (dans les douze, par le papier du mentor lui-même), M-003, M-017, M-033, M-046, M-073 et M-078 ; je ne les ai pas tranchées.
7. **Testabilité** : notée sur les coûts que les fiches annoncent, souvent « supposés ».
8. **Troisième critère** : un lien implicite clair compte 1 (M-061, M-068) ; le témoin apparié à la covariance est lu comme la base améliorée de 2410.12555, comme le fait la moisson.

## Incident

À 12:15:13 UTC, l'écriture de mon `bradley_terry_v1.py` a remplacé un fichier du même nom déjà présent dans `classement-D/`, très probablement le script du classeur du classement B (ses fichiers `bradley_terry_v1-B-*`, `notes-B-v1.json`, `paires-B-v1.jsonl`, `classement-B-v1.md`, écrits entre 12:07 et 12:14 UTC, sont intacts, et sa sortie a été produite avant le remplacement). Je n'avais pas lu ce fichier ; son contenu et son empreinte me sont inconnus et je ne peux pas le restaurer. La sortie B n'enregistre pas l'empreinte de son script. Pour que le mien survive à un nouvel écrasement, j'en ai gardé une copie identique sous `bradley_terry_v1-A.py`. Les deux consignes demandaient le même nom de fichier dans le même dossier.

