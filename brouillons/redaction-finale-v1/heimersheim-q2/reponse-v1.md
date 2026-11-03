I want to work on mechanistic interpretability because reading a behaviour did not let me control it. In Llama-3.1-8B-Instruct, a probe direction tracked sycophancy (ρ = 0.684, possibly training fit), yet no single-direction intervention I tried reduced it (github.com/lciric/sycophancy-construct-validity). Your paper with Ferreira da Silva finds that contrastive directions, readable by construction, are privileged under your error-correction test (p > 2). My question is whether a direction the network privileges also controls the behaviour it predicts. If yes, your test could screen steering targets, such as an evaluation-awareness direction; if no, privilege and control need separate tests. I have preregistered both measurements on the directions that social pressure adds to the activations: your test, and whether rotating toward them moves the model's ratings (R9 and R9-bis, github.com/lciric/sycophancy-psychophysical-law; not yet run).

---

Compte de mots par script (3 novembre 2026, 13:05 UTC, `date -u`). Le texte compté est le premier paragraphe de ce fichier, au-dessus du trait. Script hors dépôt, `/tmp/q2-heim-scripts/compter2.py`, lancé avec `nice -n 10 python3 -I` :

```python
import re, sys
t = open(sys.argv[1], encoding="utf-8").read().strip()
print("espaces:", len(t.split()))
print("coupe aux tirets (espaces puis '-'):", sum(len([p for p in j.split('-') if p]) for j in t.split()))
print("regex \\w+ (pire cas, liens eclates):", len(re.findall(r"\w+", t)))
```

Sortie :

```
espaces: 130
coupe aux tirets (espaces puis '-'): 141
regex \w+ (pire cas, liens eclates): 148
```

Limite : 150 mots au plus. Les trois comptes sont en dessous. Les liens ne sont pas épinglés à un commit, parce que le pire cas passerait à 155 (voir `note-piste-v1.md`, § 5).
