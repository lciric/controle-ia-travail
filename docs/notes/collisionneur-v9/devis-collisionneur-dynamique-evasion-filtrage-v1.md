# Devis : collisionneur sur la dynamique de l'évasion sous filtrage pendant l'entraînement

- **Classe A (devis).** Session fille des collisionneurs, 24 novembre 2026. Calcul par la commande `devis` du programme v9-v8o (f63c513c…, contre-lu conforme).
- **Question et faits** : `docs/notes/dynamique-papier-d-protocole-x-v1/question-neutre-dynamique-v2.md` (main, c292925f…, 408 mots), servie mot pour mot, comme question et comme faits.
- **Étage** : III seul, trois tours (conceptions, critiques croisées, réponses), quatre espèces, soit 12 cellules.
- **Espèces et clés** : Opus 5.5, lettre A (effort « high » du programme, sans --effort-max ; clé RR_ANTHROPIC_API_KEY) ; Astra, lettre B (OPENAI_API_KEY_2) ; Carbon, lettre C, et Neon, lettre D (--google-arriere-plan, clé GEMINI_API_KEY_FREE). Pas de Fable.
- **Plafonds de sortie** : ceux du programme par défaut, sans --sortie-max. Avec --sortie-max, le pire cas monte à 39,83 USD, dont 20,0 pour Astra seul.
- **Bras témoin** : aucun. Aucune question témoin n'a été écrite ni testée pour ce dossier ; en ajouter une demanderait une pièce neuve et son test de neutralité.

## Chiffres (comptés par le programme, en USD)

| Poste | Opus (A) | Astra (B) | Carbon (C) | Neon (D) | Total |
|---|---|---|---|---|---|
| Pire cas par tour (III.1 / III.2 / III.3) | 1,30 / 1,40 / 1,46 | 0,45 / 0,70 / 0,84 | 2,31 / 2,41 / 2,47 | 1,49 / 1,56 / 1,61 | 17,99 |
| Attendu (relevés des dossiers du jour) | environ 2,0 | environ 1,5 | environ 2,7 | environ 2,0 | environ 8 |

- **Pire cas sans relance** : 17,99. Chaque relance ajoute au plus le pire cas de sa cellule ; deux relances au plus pour une cellule de Google, une pour les autres.
- **Dépense réelle attendue** : environ 3,5. Seuls Opus et Astra sont facturés : la clé Google gratuite ne coûte rien, mais le programme compte Google à son prix.
- **Attendu avec pannes** : environ 10 (une coupure de Google comptée au pire en moyenne).

## Plafond proposé

**20 USD** (`--plafond-usd 20 --ligne-usd 20`). Le programme vérifie le plafond avant chaque appel : il arrête la course au lieu de le dépasser. Deux coupures de Google comptées au pire pourraient l'atteindre avant la fin ; dans ce cas, la course s'arrête, et une relance demande un mot nommé.

## Commande

```
GEMINI_API_KEY="$GEMINI_API_KEY_FREE" GO_ID=<GO> PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/collisionneur_v9_v8o.py etage3 \
  --opus --astra --carbon --neon --google-arriere-plan --cle-anthropic RR_ANTHROPIC_API_KEY --cle-openai OPENAI_API_KEY_2 \
  --sortie runs/collisionneur-protocole-x-dynamique-evasion-filtrage-v1-<horodatage> \
  --faits <question v2> --question <question v2> --plafond-usd 20 --ligne-usd 20
```
