# Note de lancement du collisionneur — dossier 1, « ce qui entre dans un programme amélioré et ambitieux, entraînement compris » — v1

Écrite le 2026-11-24T11:52:19Z (`date -u`), avant le lancement, par la session du protocole X (`session_01Qi7Gr31b1s4znXx53GF1ik`). Elle applique le devis contre-lu et vérifié ; elle n'ajoute aucun choix au-delà de l'arbitrage reçu.

## Accord

- `GO-2026-11-24-20`, type calcul, 21 USD, échéance 2026-11-30, lu ce jour au registre des accords de la branche principale (commit `7a90f4ba1fdbdc18a08f85d54c15abc99b3f0a71`, 11:43:33Z, R-5270) : collisionneur du protocole X, dossier 1 seul ; étage III, Opus 5.5, Carbon et Neon ; clé Anthropic `RR_ANTHROPIC_API_KEY` ; aucune relance sans décision nommée ; le dossier 2 n'est pas lancé. Il s'appuie sur les mots de Lazar du 24 novembre vers 10:31Z (`GO-2026-11-24-16`).
- Arbitrage de la mère reçu à 11:43:36Z : un seul dossier pour les deux « go collisionneur » ; dossier 1 seul ; départ maintenant ; ligne de 21 USD ; aucune relance ni ligne de reprise sans décision nommée ; note de fin de dossier en Markdown et en PDF.

## Ce qui part

- Devis : `devis-collisionneur-entrainement-et-juges-v3.md` (`2249c61b…`), commande de sa section 4 avec l'option de 21 USD de sa section 3 (`--plafond-usd 21 --ligne-usd 21`).
- Programme : `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py` (`420394f9…`, sceau vérifié ce jour).
- Faits : `faits-neutres-demande-1-v3.md` (`c2b9327b…`). Question : `question-neutre-collisionneur-demande-1-v2.md` (`4494b200…`). Sceaux vérifiés ce jour.
- Clés lues par leur nom : `RR_ANTHROPIC_API_KEY` ; `GEMINI_API_KEY` (le programme ne lit aucune autre clé de Google).
- Dossier de la course : `runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-20261124-115219`.

```
PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py etage3 \
  --opus --carbon --neon --cle-anthropic RR_ANTHROPIC_API_KEY \
  --faits docs/notes/protocole-x-entrainement-et-juges-v1/faits-neutres-demande-1-v3.md \
  --question docs/notes/protocole-x-entrainement-et-juges-v1/question-neutre-collisionneur-demande-1-v2.md \
  --sortie runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-20261124-115219 \
  --plafond-usd 21 --ligne-usd 21
```

## Bornes et conduite

- Pire cas sans relance : 15,90 USD ; attendu : de 6,0 à 7,3 USD. La ligne de 21 USD refuse avant l'envoi tout essai qui la ferait dépasser.
- Cellules d'Opus sur la clé partagée : 1,7 USD attendu, 4,1 USD au pire sans relance. Le programme ne borne pas par clé et relance lui-même une cellule vide ou coupée par son plafond : je rapporte la dépense réelle d'Opus à la fin.
- Tout arrêt (envoi coupé, porte fermée, refus par la ligne, défaut de réglage, garde de dépense, modèle servi différent) : je m'arrête, je rends compte à la mère, et je ne relance rien sans décision nommée.
- La commande tourne détachée, sa sortie d'écran est gardée ; l'arrêt, s'il en faut un, se fait par numéro de processus.
- À la fin : vérification du dossier par le programme, versement scellé, note de sortie en Markdown et en PDF.
