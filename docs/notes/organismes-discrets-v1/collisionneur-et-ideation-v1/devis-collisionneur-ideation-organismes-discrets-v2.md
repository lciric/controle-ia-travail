# Devis — collisionneur et organisme d'idéation sur le sujet des organismes discrets — v1

**Statut : CONTRE-LU (R2, verdict : « à corriger — 1 significative, 2 mineures » ; corrections intégrées v2). Aucune dépense autorisée par lui.**
Rédigé le 2026-11-17 vers 04:40 UTC (`date -u`), session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`.
Mot direct de Lazar : R-3069. Conception de référence : `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md` (`43a356ab…`). Brouillon de préenregistrement : `docs/notes/organismes-discrets-v1/prereg-organismes-discrets-v1-brouillon1.md`.

## 1. Collisionneur épistémique à cinq espèces

**Script** : `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py` (sha256 de son compagnon).
**Espèces** : A (Fable 5.1), B (Opus 4.6), C (Argon), D (Kimi K3.1 Pro par relais local), E (GPT-6 Astra) — identifiants dans le script, inchangés.
**Étages** : étage III seulement (question ciblée, comme les tours précédents des collisionneurs du programme).
**Pièces d'entrée** : un fichier de faits (`faits-v1.md`, résumé de la conception retenue v2 et du brouillon de préenregistrement), un fichier de question (`question-v1.md`, une question sur le dessin de la section 1.2 — la bras B, couplage anti-monotone intra-classe). Les deux à écrire par un opérateur, contre-lire, sceller.

**Coûts estimés** (au barème du script v8-plafonds-bas-v1, basé sur les tours précédents) :

| poste | attendu (USD) | pire cas (USD) | source |
|---|---|---|---|
| étage III, 15 cellules (5 × 3 tours) | 10 | 15 | quatre tours précédents : 8,51 (12 cellules), 9,54 (14), 13,84 (15), 11,14 (15) ; moyenne des deux tours à 15 cellules : 12,49 |
| relance d'une cellule tronquée (au plus une) | 1,5 | 3 | fréquence : une sur quatre tours |
| **total collisionneur** | **≈ 11,5** | **≈ 18** | plafond du script : 15 par tour (hors relance) |

**Clés nécessaires dans l'environnement** (par nom seulement) :
- `ANTHROPIC_API_KEY` ou passage de `RR_ANTHROPIC_API_KEY_RIGAUD` via `env -i` (à confirmer) ; `ANTHROPIC_WORKSPACE_ID` si la clé l'exige (v2.6 du script) ;
- `GEMINI_API_KEY` : **présente** ;
- `OPENAI_API_KEY` : **présente** ;
- `KIMI_RELAIS_URL` : **absente** — nécessite un relais Kimi (script `relais_kimi_v3.py`) et une clé Moonshot, ou `--accepter-absence D` (cellules de Kimi comptées absentes, 12 cellules sur 15 au lieu de 15, prise en compte dans la synthèse) ;
- `TYPESAFE_API_KEY` : **absente** — les notes de Jev ne sont pas produites ; elles ne sont jamais décisives (option `--jev` rapportée, non exigée).

**Sans Kimi et sans Jev** (option la plus probable dans cet environnement) : 12 cellules sur 15, 4 espèces, **attendu ≈ 9 USD, pire cas ≈ 14 USD**.

## 2. Organisme d'idéation

**Code** : `src/controle_ia/organisme_idees_juge/` (42 fichiers Python).
**Objet** : générer et évaluer des propositions de conception expérimentale sur le sujet, par des modèles (proposeurs) et un juge statistique (orchestrateur, hors de tout modèle).
**Sujet** : section 1.2 de la conception-v2 (couplage anti-monotone intra-classe, grille de Kendall, témoin monotone, prédictions P3–P4 et métrique M2 du brouillon de préenregistrement 1).
**Modèles proposeurs** : Kimi et Argon (par relais locaux), comme dans les courses précédentes de l'organisme ; **aucun modèle de la famille Claude** dans un rôle de l'organisme.

**Coûts estimés** (basés sur les courses précédentes ; **corrigé après contre-lecture R2** : la référence « Regard ou raisons » g1 à 6,20 USD utilisait Claude comme proposeur dominant (5,08 USD, 82 % du total) ; la configuration sans Claude est moins chère) :

| poste | attendu (USD) | pire cas (USD) | source |
|---|---|---|---|
| une génération, 2 proposeurs (Kimi + Argon) | 2,5 | 4 | course de l'organisme v67 (Kimi 1,14 + Argon 0,86 ≈ 2,00 USD proposeurs) ; marge pour le juge et l'orchestrateur |
| une génération, 1 proposeur (Argon seul) | 1,5 | 2,5 | v67 Argon seul : 0,86 USD proposeur ; marge |
| nombre de générations | 1 à 3 | 3 | mot de Lazar (R-3069) ; arrêt si rien de neuf |
| **total organisme (2 proposeurs, 1 gén.)** | **≈ 2,5** | **≈ 4** | |
| **total organisme (1 proposeur, 3 gén.)** | **≈ 4,5** | **≈ 7,5** | |

**Clés nécessaires** (par nom) :
- `GEMINI_API_KEY` (relais Argon) : **présente** ;
- `KIMI_RELAIS_URL` et clé Moonshot sous-jacente : **absentes** — le proposeur Kimi ne peut pas tourner dans cet environnement ; l'organisme peut tourner avec Argon seul (un seul proposeur, perte de diversité) ;
- `RR_ANTHROPIC_API_KEY_RIGAUD` : **présente**, mais n'entre pas dans l'organisme (Claude exclu de tout rôle) ; seulement pour d'éventuels appels de contrôle de la mère.

**Sans Kimi** : 1 proposeur (Argon seul), diversité réduite, **attendu ≈ 1,5 USD par génération, pire cas ≈ 2,5 USD**.

## 3. Total

| scénario | attendu (USD) | pire cas (USD) |
|---|---|---|
| collisionneur 4 espèces + organisme 1 proposeur, 1 génération | 10,5 | 16,5 |
| collisionneur 4 espèces + organisme 1 proposeur, 3 générations | 13,5 | 21,5 |
| collisionneur 5 espèces + organisme 2 proposeurs, 3 générations (clés complètes) | 19 | 30 |

**Plafond recommandé** : **17 USD** (scénario 4 espèces, 1 génération), première passe ; passer à 3 générations sur un second GO si les résultats le justifient.

## 4. Préalables

1. **Devis contre-lu** (R2) par un sous-agent neuf.
2. **GO de calcul de Lazar** sur ce devis, avec le plafond retenu.
3. **Clés d'interface manquantes** : `KIMI_RELAIS_URL` (ou décision de courir sans Kimi) ; `ANTHROPIC_API_KEY` (ou confirmation que `RR_ANTHROPIC_API_KEY_RIGAUD` via `env -i` convient pour le collisionneur).
4. **Fichiers d'entrée du collisionneur** (`faits-v1.md` `b99fee40…`, `question-v1.md` `80b624ee…`) : **écrits et scellés**.
5. **Configuration de l'organisme d'idéation** pour le nouveau sujet : monde planté, grammaire des lois, épisodes de développement ; potentiellement un nouveau module (à évaluer). Le proposeur passe par un relais local (relais Argon et/ou relais Kimi) ; l'orchestrateur et le juge statistique tournent localement sans interface.

## 5. Risque de blocage du classifieur

Les tentatives précédentes de rédaction sur ce sujet par la session mère ont été bloquées par le classifieur (R-3060, R-3064, R-3066). Le mot direct de Lazar (R-3069) lève l'auto-arrêt R-3066. Si le classifieur bloque à nouveau la rédaction des pièces d'entrée, la mère s'arrête et rapporte, conformément aux interdits permanents. Les mécanismes (scripts, code) sont intacts et testés ; c'est la rédaction du texte d'entrée qui est le point bloquant.
