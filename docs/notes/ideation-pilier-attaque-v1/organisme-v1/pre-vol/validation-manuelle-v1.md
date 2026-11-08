# Validation manuelle du pré-vol — pilier attaque, v1

Date : 2026-11-08.
Raison : le lanceur externe (`ideation_v8.py`) n'a pas pu être exécuté
dans cette session (classifieur de permissions : « Code from External »).
Les vérifications ci-dessous ont été faites à la main.

## 1. Empreintes des pièces

| Pièce | SHA256 | Statut |
|---|---|---|
| Question scellée | `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4` | OK |
| Synthèse d'antériorité | `48adeac041d21c375473f2af1ed85ed88f7e5c97b5f88ba21021cc0c99e49997` | OK |

## 2. Sonde de la garde de refus (simulée)

Résultat : 3/3 modèles acceptent (claude-fable-5-1, claude-opus-5-5, gemini-4-argon).
Mode : `--simuler` (aucun appel réel).
Fichier : `pre-vol/sonde-garde-refus-v1.json`.

## 3. Liste blanche

Fichier : `pre-vol/liste-blanche-v1.json`.
Contenu : 2 fichiers (question + synthèse), empreintes vérifiées.
Note : les témoins (CL31-03) devront être ajoutés quand ils existeront.

## 4. Compatibilité CLI du lanceur v2

Corrections apportées après lecture du code (`ideation_v2.py`, 1413 lignes) :

| Point | Constat | Action |
|---|---|---|
| `--verifier-seulement` | N'existe pas dans le lanceur v2 (seulement v5+, avec `--course-2`) | Remplacé par `--mesurer-consignes` |
| `--bras-rapporte-differe` + `--proposeur-externe` | Incompatibles (ligne 1126) | Course en deux temps : (a) course, (b) bras séparé |
| `--temoins` | Requis pour la course (ligne 1113), écrits par tiers (CL31-03) | Prérequis non satisfait pour `--moteur simule` |
| `--moteur` | Choix : `simule` ou `claude-sdk` (pas `reel`) | Corrigé |
| `--budget` | Format `role\|modele=plafond` | Les défauts du lanceur (somme 25,3 USD) dépassent `--budget-total-usd 15.0` |

## 5. Budgets

### Défauts du lanceur (devis v7 quinquies)

| Rôle | Modèle | Plafond session (USD) |
|---|---|---|
| proposeur_ideation | claude-opus-5-5 | 5,0 |
| proposeur_ideation | claude-fable-5-1 | 9,3 |
| juge_ideation | claude-opus-5-5 | 4,0 |
| juge_ideation | claude-fable-5-1 | 7,0 |
| proposeur externe | gemini-4-argon | 2,5 |
| juge externe | gemini-4-argon | 3,5 |

Somme Claude : 25,3 USD > 15,0 USD → `--tolerer-somme-plafonds-claude` requis,
ou ajuster les plafonds par session avec `--budget role|modele=plafond`.

### Option recommandée : plafonds ajustés au scénario minimal

| Paramètre | Valeur |
|---|---|
| `--budget-total-usd` | 15.0 |
| `--budget-externe-usd` | 5.0 |
| `--budget proposeur_ideation\|claude-opus-5-5` | 2.5 |
| `--budget proposeur_ideation\|claude-fable-5-1` | 2.5 |
| `--budget juge_ideation\|claude-opus-5-5` | 1.5 |
| `--budget juge_ideation\|claude-fable-5-1` | 1.5 |
| Somme Claude | 8,0 < 15,0 |

## 6. Commandes à exécuter (hors de cette session)

### (a) Mesure des consignes (sans appel, sans écriture)

```bash
cd /chemin/vers/ideation-organism/orchestrator
python -I -B demonstrations/ideation_v8.py \
    --mesurer-consignes \
    --question QUESTION.md \
    --piece SYNTHESE.md \
    --piece-juge SYNTHESE.md \
    --liste-blanche LISTE_BLANCHE.json \
    --proposeur opus=claude-opus-5-5 \
    --proposeur fable=claude-fable-5-1 \
    --proposeur-externe argon=gemini-4-argon \
    --juge opus-juge=claude-opus-5-5 \
    --juge fable-juge=claude-fable-5-1 \
    --seconde-passe \
    --nombre 8 \
    --budget-total-usd 15.0 \
    --budget-externe-usd 5.0
```

### (b) Passe simulée (course, sans le bras)

Prérequis : témoins plantés (`--temoins`, CL31-03).

```bash
python -I -B demonstrations/ideation_v8.py \
    SORTIE \
    --question QUESTION.md \
    --piece SYNTHESE.md \
    --piece-juge SYNTHESE.md \
    --temoins TEMOINS.json \
    --liste-blanche LISTE_BLANCHE.json \
    --proposeur opus=claude-opus-5-5 \
    --proposeur fable=claude-fable-5-1 \
    --proposeur-externe argon=gemini-4-argon \
    --juge opus-juge=claude-opus-5-5 \
    --juge fable-juge=claude-fable-5-1 \
    --seconde-passe \
    --nombre 8 \
    --budget-total-usd 15.0 \
    --budget-externe-usd 5.0 \
    --budget "proposeur_ideation|claude-opus-5-5=2.5" \
    --budget "proposeur_ideation|claude-fable-5-1=2.5" \
    --budget "juge_ideation|claude-opus-5-5=1.5" \
    --budget "juge_ideation|claude-fable-5-1=1.5" \
    --moteur simule
```

## 7. Éléments en attente

- Témoins plantés (CL31-03) : écrits par un tiers, dans la liste blanche.
- `--mesurer-consignes` non exécuté (classifieur de permissions).
- `--moteur simule` non exécuté (classifieur + témoins absents).
- Sonde réelle de la garde de refus (≈ 0,003 USD, sur le mot de Lazar).
