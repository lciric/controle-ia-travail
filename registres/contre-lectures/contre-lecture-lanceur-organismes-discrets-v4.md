# Contre-lecture R2 — lanceur de l'organisme d'idéation sur les organismes discrets, version 4

Fichier lu : `scripts/lancer_course_ideation_organismes_discrets_v4.py`, 529 lignes, empreinte
`a6e0dec9662639995add07f9b883fd3f2a4a1bd03a6e139707506f8cfbfa2afa` (vérifiée, identique à l'attendu et au fichier `.sha256` compagnon).
Lecteur neuf (n'a pas écrit le fichier). Lus : le lanceur en entier, les 48 tests, la ligne GO-2026-11-17-06 de `registres/go.md`,
l'enveloppe d'Argon v5, la différence v3 → v4 (deux changements seulement, conformes à la description), la ligne R-3072 (dépense 7,86 USD du collisionneur : constante traçable).

## Vérifications exécutées
- Les 48 tests passent (venv jetable avec pytest ; 32 fonctions, paramétrées jusqu'à 48).
- `verifier_go` sur le registre réel : accepte la ligne (plafond 17 USD, échéance 2026-11-22, Lazar, calcul, 8 colonnes).
- `_est_revocation` : « Révocation » + identifiant → vrai ; « décision » citant l'identifiant → faux (conforme au format du registre, où seules les lignes de type révocation révoquent).
- Somme des plafonds externes de production : 7,2 USD < 9,14 USD ; 7,86 + 9,14 = 17,00 = plafond du GO ; aucun Claude (budget Claude 0.0, drapeaux Claude interdits).
- Les deux corrections annoncées sont bien dans le code (ligne 235 : `--ignored=matching` ; lignes 164-173 : normalisation) et chacune a un test sain/artefact.

## Défauts significatifs (bloquants)
Aucun.

## Défauts mineurs (non bloquants, à documenter)
1. **Test de l'échec après le manifeste de départ inexistant** (R5). `test_manifeste_fin_ecrit_si_popen_echoue` ne provoque aucun échec : c'est un doublon du cas sain. La branche `except BaseException` (manifeste de fin d'échec) est donc non testée, alors que l'étape 7 de l'en-tête l'affirme. À corriger par un vrai artefact (par exemple faire échouer `open` ou `Popen` par monkeypatch) ou à renommer pour ne pas prétendre.
2. **Clé du relais d'Argon non vérifiable ici.** L'enveloppe annonce un relais lancé « par le noyau » avec la vraie clé Gemini dans son seul environnement ; le lanceur retire `GEMINI_API_KEY` (et tout nom en clé/jeton/secret) de l'environnement transmis. Si l'orchestrateur lance le relais en lisant cette variable, la course échouera au premier appel (sans dépense), après le manifeste de départ. Les versions v1 à v3 ont la même conduite, et l'orchestrateur est absent de ce conteneur (`/home/user/lciric/...` inexistant) : à confirmer par la mère avant le lancement (par exemple par la trace d'une course antérieure du même chemin).
3. **Gardes sur l'arbre de l'orchestrateur : faux refus possible.** `--ignored=matching` refuse aussi les `__pycache__` ou autres fichiers ignorés légitimes laissés par une exécution antérieure. Échec sûr (refus), mais à nettoyer avant lancement. En sens inverse, les indicateurs git `skip-worktree` / `assume-unchanged` masquent une modification aux commandes `status` : seuls les neuf fichiers épinglés sont protégés par empreinte (les autres modules de `pole/` ne le sont que par `status`).
4. **Détection des révocations** : le critère « une cellule commence par `revoc` et une cellule contient l'identifiant » est plus large que nécessaire (faux positif sûr) ; une révocation qui ne serait pas de type « révocation » (type de ligne hors format) ne serait pas vue. Conforme au format actuel du registre. Le contrôle du périmètre (`"idéation"`) compare sans normalisation Unicode (forme décomposée → faux refus, sûr).
5. **Arrêt (R10).** Les signaux (SIGTERM, SIGINT, SIGHUP) sont relayés au seul enfant direct, pas au groupe de processus ; une fenêtre minuscule existe entre `Popen` et l'installation du relais de signaux. Si le lanceur lève une exception pendant l'attente, l'enfant n'est pas arrêté. Aucun impact tant que l'arrêt se fait par l'identifiant du processus de l'orchestrateur, consigné dans le manifeste de fin et affiché au départ seulement par le manifeste (pid écrit à la fin) : prévoir de relever le pid par `ps` si un arrêt est nécessaire.
6. **Garde de drapeaux quasi tautologique en production** : elle vérifie la commande que le lanceur construit lui-même (`arguments_en_plus` vide) ; les abréviations d'`argparse` ne seraient pas vues. Sans effet en production, utile seulement aux essais.
7. **`principal` rend 2 aussi pour les erreurs internes** (cohérent avec la correction v3), mais un code d'orchestrateur négatif (signal) est rendu tel quel ; sans conséquence.

## Verdict final : **SCELLABLE**
0 défaut significatif, 7 défauts mineurs (dont le n° 1, un test à corriger, et le n° 2, à confirmer avant le lancement).
Conditions de lancement rappelées (hors périmètre du scellement) : feu de la mère, orchestrateur au commit épinglé sans fichier ignoré, dépense sous le plafond du GO-2026-11-17-06.
