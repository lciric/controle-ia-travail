"""Produit la note v7 = note v6 + erratum 1 appliqué (deux corrections), rien d'autre."""
import re, sys, hashlib, pathlib
D = pathlib.Path(sys.argv[1])
v6 = (D/"note-entretien-controle-diffus-v6.md").read_text(encoding="utf-8")
er = (D/"note-entretien-controle-diffus-v6-erratum-1.md").read_text(encoding="utf-8")
blocs = re.findall(r"```markdown\n(.*?)\n```", er, re.S)
assert len(blocs) == 2, len(blocs)
anc1, nouv1 = blocs
inl = re.findall(r"\*\*(Ancien|Nouveau) texte\*\* \(ligne 132\) :\n  `(.*?)`\n", er)
assert [k for k, _ in inl] == ["Ancien", "Nouveau"], inl
anc2, nouv2 = inl[0][1], inl[1][1]
anc3 = ("   - *Pour toi, si on te l'oppose* : Gasteiger et al. disent le signal trop faible pour **empêcher** "
        "le sous-rendement à l'inférence ; c'est Gan et al. qui disent « incriminer » (p. 10). "
        "La phrase reste dicible telle quelle, puisque c'est ton mot.")
m = re.search(r"remplacée par : « (.*?) »\s*$", er, re.M)
nouv3 = "   - *Pour toi, si on te l'oppose* : " + m.group(1)
t = v6
for a, b in [(anc1, nouv1), (anc2, nouv2), (anc3, nouv3)]:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, b)
h6 = hashlib.sha256(v6.encode()).hexdigest(); he = hashlib.sha256(er.encode()).hexdigest()
tete = f"""# Note pour l'entretien du 1er décembre — « Diffuse AI Control on Fuzzy Tasks » — v7

- **v7, 23 novembre 2026 (`date -u`).** Produite par programme (`produire_v7.py`) par la session du dossier de l'entretien (Opus 5.5) : la v6 (`{h6[:8]}…{h6[-6:]}`, gardée) avec son erratum 1 (`{he[:8]}…{he[-6:]}`) appliqué, rien d'autre. Chaque ancien texte est retrouvé une seule fois.

## Ce qui change par rapport à la v6

| N° | Où | Ce qui change | D'où |
|---|---|---|---|
| 1 | § 5, objection 1 | Gasteiger et al. : quatre moniteurs, dont le modèle du saboteur, qui sépare mieux ; « détecter » (Gasteiger et al.) et « incriminer » (Gan et al.) distingués ; deux phrases sur le rôle des sondes : accélérateur et aiguillage d'un audit au hasard, non garantie | erratum 1, correction 1 ; réponse d'une page, `9aac8d6b…`, contre-lue `a5624652…` |
| 2 | § 3, phrase 10 | « trop faible pour détecter (Gasteiger et al.) ou pour incriminer (Gan et al.) » | erratum 1, correction 2 |
| 3 | § 3, note sous la phrase 10 | Remplacée par la forme que donne l'erratum ; la citation « prevent one-shot sandbagging at inference time » est relue dans la page de Gasteiger et al. (`4a7e0eb9…dad7e5`, liste des résultats en tête de page). L'erratum laissait le choix entre garder et remplacer : à confirmer par toi | erratum 1, « Effet sur la ligne 134 » |

L'état décrit reste celui de la v6, au 21 novembre ; la mère le relit contre les registres la veille de l'entretien.

## En-tête de la v6, gardé

"""
corps = t.split("\n", 1)[1]
(D/"note-entretien-controle-diffus-v7.md").write_text(tete + corps.lstrip("\n"), encoding="utf-8")
print("v7 écrite")
