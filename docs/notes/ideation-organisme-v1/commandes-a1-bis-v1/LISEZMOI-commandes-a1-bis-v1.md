# Commandes externes d'A1-bis : Claude (port 8806) et Astra (port 8807), v1

Écrit le 2 novembre 2026 par la session fille de session-depot, à la demande de la session mère (A1-bis ; GO-2026-11-02-11 à -13
inscrits, rien de lancé). **Aucun appel réel** : essais hors réseau seulement, avec de faux amonts sur la boucle locale.

## Fichiers

| Fichier | Rôle |
|---|---|
| `commande_pole_v56_commun_v1.py` | contrat commun repris de `commande_argon_v56_nuit_v2.py` (221df610…) : `servir` (relais local, plafond propre réservé au pire cas sous verrou, max-appels, modèles permis, réglages comparés, journal sans texte ni clé) et `appeler` (PLAFOND_SESSION_USD, registre cumulé et porte « environnement », ROLE_POLE, MODELE_DEMANDE_POLE, modèle servi exact, dernière ligne JSON) ; mêmes codes de sortie (0, 2, 3, 4, 5, 6) |
| `commande_claude_a1bis_v1.py` | Claude par le SDK `anthropic` (flux, `max_retries=0`) ; `--modele` explicite parmi claude-fable-5-1, claude-opus-5-5, claude-opus-4-6 ; **aucune bascule** (pas de `fallbacks`) ; `--effort` et `--reflexion` (adaptative / omise) obligatoires aux deux bouts, refus 409 du relais s'ils diffèrent ; xhigh refusé sur Opus 4.6 |
| `commande_astra_a1bis_v1.py` | Astra par `collisionneur_v8.appeler_openai(attentes=(0,))` ; **double compte corrigé** : sortie facturée = `completion_tokens` seul |
| `registre_depense_cumulee_v1.py` | copie à l'octet (8ba92066…) du registre partagé de la mini-course |
| `collisionneur_v8.py` | copie à l'octet (22e5ed8a…), empreinte vérifiée par le relais Astra au démarrage |
| `test_commandes_a1bis_v1.py` | 15 essais (voir plus bas) |

## Prix utilisés (USD par million, entrée / sortie)
Claude : Fable 5.1 10 / 50 ; Opus 5.5 4 / 20 ; Opus 4.6 5 / 25 — table des modèles de la documentation de l'interface (cache
du 6 octobre 2026), lue le 2 novembre. Le collisionneur v8 comptait Opus 4.6 à 15 / 75 (supposé) : ses coûts de l'espèce B sont
donc surestimés d'environ trois fois. Astra : 10 / 50, SUPPOSÉ haut (inchangé depuis le v8).

## Essais (hors réseau), 15 passés
```
PY_RELAIS=<python avec anthropic> <même python> -m pytest -q -p no:cacheprovider test_commandes_a1bis_v1.py
```
Claude : cas sain (coût lu, modèle exact, corps envoyé : effort, thinking adaptatif, pas de `fallbacks`, aucune clé dans le
journal, la sortie ni le registre) ; modèle servi différent → 5 ; budget de session dépassé → 4, rien envoyé ; plafond cumulé
dépassé → 4 ; amont en erreur (529) → 3, coût au pire cas ; réglages différents → 409 → 3, rien envoyé ; xhigh sur Opus 4.6 → 2 ;
ANTHROPIC_BASE_URL tierce → refus de servir ; plafond propre du relais → 402 → 4. Astra : cas sain avec sortie = completion_tokens
(2 000, contre 3 500 en double compte) ; modèle servi différent → 5 ; budget dépassé → 4 ; amont en erreur (503) → 3 ; modèle
hors table → 2. Registre partagé : fournisseur « claude » consigné.
Contre-épreuve (R4, trop propre au premier passage) : quatre mutations des gardes (modèle servi, correction du double compte,
comparaison des réglages, plancher de sortie) font chacune échouer 1 ou 2 essais.

## Ce qui reste à faire avant tout appel
Configuration v3 d'A1-bis (commandes et ports) et code v3 du lanceur chez conv-audit (FOURNISSEURS figés à kimi et argon) ;
choix de l'effort et de la réflexion par modèle (décision, écrite au texte scellé) ; relais Claude lancé avec le Python qui porte
`anthropic` ; calibrage (GO-2026-11-02-12) avant la course.
