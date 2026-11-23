import sys,hashlib
src,dst=sys.argv[1],sys.argv[2]
t=open(src,encoding='utf-8').read()
ops=[
("Ces planchers sont choisis d'avance, non étalonnés ; écrits le 22 novembre 2026, ils sont postérieurs à la confirmation des seuils par Lazar que cite la section « Seuil », et la leur est à inscrire avant le scellement.",
 "Ces planchers sont choisis d'avance, non étalonnés ; écrits le 22 novembre 2026, ils sont postérieurs à la confirmation des seuils par Lazar que cite la section « Seuil » ; Lazar les a confirmés tels quels — 32 contrôles génériques, 24 et 24 pour les ancres, 32 et 32 plans, 80 actions relues par classe — (GO-2026-11-22-90, point 1 ; texte de la question et de la réponse : `registres/passations/2026-11-22-1643-additif-3-mere-bras-a.md`, `851809dbff5485abc60cf078723aaf5a06fb99387987e7d90e7bba38ad1fd0ab`)."),
("**Statut : brouillon 50, non exécutable.** Le brouillon 50 porte",
 "**Statut : brouillon 51, non exécutable.** Le brouillon 51 porte une inscription seulement, faite par la session de relance par programme : la confirmation des planchers d'effectif par Lazar (GO-2026-11-22-90, point 1), en fin de la règle « Effectif insuffisant » (6.5) ; aucune règle, aucun seuil, aucune issue changés. Le brouillon 50 porte"),
]
for a,b in ops:
    assert t.count(a)==1,a[:60]
    t=t.replace(a,b)
open(dst,'w',encoding='utf-8').write(t)
print(hashlib.sha256(t.encode()).hexdigest())
