# Vérification de collisionneur_v9_v8j.py (d199a14b…) — rendu v1

Verdict : **conforme**, sans bloquant. Je n'ai trouvé aucun chemin réel ou interne qui parte.

Le différentiel depuis la v8i contient deux changements, et seulement ceux-là : un chemin accepté a exactement deux composants, et le nom n'est fait que d'ASCII. Les sceaux tiennent, et 393 essais passent.

Toutes mes attaques (v8g, v8h et v8i) sont refusées, sauf deux cas que j'admets volontairement :
- `scripts/pipelines`, qui est le faux positif à accepter ;
- un nom inventé très long.

L'essai à blanc en lecture seule sur la conception F redonne `['scripts/pipelines']`.

Mutations : 15 tuées, 4 survivent.
- Tuées : les mutations des versions précédentes, plus « deux composants retiré » et « Unicode admis ».
- Les 4 survivants :
  - le témoin sans mutation, qui doit passer ;
  - trois mutants équivalents :
    - le contrôle des formes retiré, que couvre la liste blanche ;
    - « . » et « .. » admis, que la forme des composants exclut déjà ;
    - la comparaison sans extension retirée, que couvre la règle des préfixes.

## Non-bloquant
Un jeton coupé par une ponctuation que le contrôle du caractère suivant admet passe encore : `scripts/depot'expurge.py`, `scripts/depot,expurge.py`, `scripts/depot:expurge.py` et `docs/sour)ces`. Le contrôle ne voit que `scripts/depot` ou `docs/sour`. Le texte envoyé ne contient aucun chemin réel exact, et il faudrait un rédacteur qui déforme exprès un nom qu'il connaît.

Correction possible, en une ligne : exiger que la suite du texte après le jeton corresponde à `[,;:!?)\]}»"'’]*(\s|$)`. Les préfixes de moins de six caractères, comme `docs/sourc`, restent admis : c'est voulu.
