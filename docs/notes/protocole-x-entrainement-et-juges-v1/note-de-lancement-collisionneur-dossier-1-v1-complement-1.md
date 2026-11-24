# Note de lancement du collisionneur, dossier 1 — complément 1 : reprise à deux voix après la coupure de Carbon

Écrite le 2026-11-24T12:05:06Z (`date -u`), avant la reprise. Complète `note-de-lancement-collisionneur-dossier-1-v1.md` (`ad975603…`), qui n'est pas réécrite.

## Ce qui s'est passé

- Première commande, partie à 11:52:38Z : la conception d'Opus 5.5 est valide (0,42 USD). La conception de Carbon, partie à 11:55:46Z, a été coupée à 12:00:46Z, 300 secondes après, sans aucune réponse ; la commande s'est arrêtée (code 5). Cellule comptée au pire : 2,31 USD. Dépense comptée sur la ligne : 2,73 USD.
- Dossier et sortie d'écran versés (commit `e40814bc`) ; compte rendu à la mère ; rien relancé.

## Décision nommée

Message de la mère reçu à 12:04:21Z : option (a), décision nommée R-5272, dans la ligne de `GO-2026-11-24-20`. « On finit à deux voix : absence acceptée des trois cellules de Carbon, puis même commande pour Neon et les tours 2 et 3. Si Neon est coupé de la même façon : arrêt, sans relance, et compte rendu. » À l'heure de cette note, la ligne R-5272 n'est pas encore visible au registre de la branche principale (dernier commit lu : `d269b7e5`, 11:59:33Z) ; je la relis à la fin de la course.

## Ce qui part

La même commande, dans le même dossier, avec trois absences acceptées :

```
PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py etage3 \
  --opus --carbon --neon --cle-anthropic RR_ANTHROPIC_API_KEY \
  --faits docs/notes/protocole-x-entrainement-et-juges-v1/faits-neutres-demande-1-v3.md \
  --question docs/notes/protocole-x-entrainement-et-juges-v1/question-neutre-collisionneur-demande-1-v2.md \
  --sortie runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-20261124-115219 \
  --plafond-usd 21 --ligne-usd 21 \
  --accepter-absence E3-T1-conception-B --accepter-absence E3-T2-critique-croisee-B --accepter-absence E3-T3-reponse-B
```

- Cellules restantes : conception de Neon ; critique croisée et réponse d'Opus 5.5 et de Neon. Pire cas de ce reste : 7,44 USD ; total compté au pire : 10,17 USD, sous la ligne de 21 USD. Attendu : environ 5 USD en tout.
- Aucun envoi à Carbon dans cette reprise.
- Si Neon est coupé de la même façon : arrêt, aucune relance, compte rendu à la mère.
