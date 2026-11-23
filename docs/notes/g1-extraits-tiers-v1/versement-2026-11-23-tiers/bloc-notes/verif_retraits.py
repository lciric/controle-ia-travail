import sys
f7 = open("prereg/T0.7-sondes-v0-v1.md", encoding="utf-8").read().split("\n")
fb = open("prereg/T0.7-etape-B-bis-v1.md", encoding="utf-8").read().split("\n")
R = [
 (f7, 1029, " (nul rapporté « non détecté à cette"),
 (f7, 1030, "  puissance », verdict v2 ; **candidat 2** : réserves de l'audit de P3 jointes telles quelles (R-2299 ; audit `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md` (`57f16378d0bf15e5d95cb771cbc181cc41c610cb947a22f33c6a16746e08997e`, § 7)) : « (1) le niveau écrit de P3-P3 n'est pas tenu sous un plancher à signal commun (le nul n'en est pas touché) ; (2) les grandeurs B3 sont celles d'une règle un peu libérale : le nul n'exclut pas des aires un peu plus hautes »)"),
 (f7, 1163, "Le résultat de P3 (nul sur les deux sondes génériques, organisme flagrant ; **candidat 2** : réserves de l'audit de P3 jointes telles quelles (R-2299 ; audit `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md` (`57f16378d0bf15e5d95cb771cbc181cc41c610cb947a22f33c6a16746e08997e`, § 7)) : « (1) le niveau écrit de P3-P3 n'est pas tenu sous un plancher à signal commun (le nul n'en est pas touché) ; (2) les grandeurs B3 sont celles d'une règle un peu libérale : le nul n'exclut pas des aires un peu plus hautes ») ne fixe aucun signe ici : "),
 (f7, 1215, "sous la règle (a), 200 directions ne tiennent pas le niveau des lectures décisives (note v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/erreur-premiere-espece-lectures-decisives-t07-v3.md` (`760a562c15991421e6c1eca2b8f65072d82976a956482c599fdeb0cc1c46b602`), § 2 et § 3 : à 200 directions, dépassement établi, évidence regroupée, 0,0139 [0,0090 ; 0,0204] et 0,0144 [0,0095 ; 0,0211] par sonde au lieu de 0,00625 ; 800 est la plus petite valeur sans dépassement établi dans aucune cellule, sous les deux lectures du nul) ; "),
 (f7, 1258, " ; **réserve écrite** : c'est la règle dont le niveau n'est pas tenu sous un plancher à signal commun (audit de P3, `docs/notes/g0-deux-semaines-v1/audit-p3-regle-plancher-v1/audit-verdict-p3-regle-plancher-v1.md`, `57f16378d0bf15e5d95cb771cbc181cc41c610cb947a22f33c6a16746e08997e`, § 3 et § 7, réserve d'audit 1 ; non simulé pour l'aire stratifiée) ; le défaut ne fabrique que des « au-dessus » : un « au-dessus » de T4 est rapporté avec cette réserve, un « non au-dessus » n'en est pas touché"),
 (f7, 1349, " Ce qu'une aire de"),
 (f7, 1350, "≈ 0,8 implique : le jeu porte un lexique corrélé à l'étiquette que la sonde peut apprendre ; "),
 (f7, 1200, " ; ≈ 63 fois plus rapide que la boucle (rapport du code du plancher v3, `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v1.md` (`cb31edc844c6bc4ee285219a819d2943fd140bf9d70f56d1da2e9e031520db92`), § 4)"),
 (f7, 1200, " ; écart mesuré ≤ 10⁻¹⁴, essais versés"),
 (fb, 44, ", guide la reconception des sondes"),
]
for lines, n, s in R:
    c = lines[n-1].count(s)
    print(n, c, len(s))
# show results after retrait for check
def apply(lines, n, s): return lines[n-1].replace(s, "", 1)
for n in (1029,1030,1163,1215,1349,1350):
    pass
print(apply(f7,1163,R[2][2])[:120])
l = apply(f7,1215,R[3][2]); i = l.find("**Raison**"); print(l[i-60:i+200])
l = apply(f7,1258,R[4][2]); i = l.find("comme au candidat 1)"); print(l[i-80:i+60])
print(repr(apply(f7,1349,R[5][2])[-60:])); print(repr(apply(f7,1350,R[6][2])[:60]))
print(repr(apply(f7,1029,R[0][2])[-50:])); print(repr(apply(f7,1030,R[1][2])[:60]))
