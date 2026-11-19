import json
from controle_ia import prereg
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
T='/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif12/'
b=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon12.md',encoding='utf-8').read()
R=[
("M-1a", "Les actions sans jeton noté n'y entrent pas. Pour chaque essai, la graine entière de sa clé sert d'abord au tirage de l'essai (actions étiquetées, jeton injecté, permutation) par un générateur neuf, puis",
 "Les actions sans jeton noté n'y entrent pas. **Égalité des deux chemins, jouée avant (i)** : pour chaque sonde lue et chaque action de `H` d'au moins un jeton noté, le score d'action lu par la fonction même de la lecture décisive (tableau des scores par action livré, colonne de la sonde, case du maximum, ligne désignée par la clé de l'action) est égal, sans tolérance, au maximum des scores par jeton de la sonde que l'essai recalcule ; l'essai déduit lui-même les bornes de chaque action des seuls champs `rang` et `jetons_notes` de l'index (sommes cumulées dans l'ordre de `rang`), sans appeler la fonction de la lecture qui associe les scores aux clés, et ces mêmes bornes placent le jeton injecté en (ii) et les blocs permutés en (iii) ; une seule inégalité fait échouer A0, sans rejeu, et la sortie écrit la sonde et le nombre d'actions inégales, jamais un score. Pour chaque essai, la graine entière de sa clé sert d'abord au tirage de l'essai (actions étiquetées, jeton injecté, permutation) par un générateur neuf, `numpy.random.default_rng(graine)`, puis"),
("M-1b", "**A0 échoue** si et seulement si (a) la même sonde",
 "**A0 échoue** si et seulement si l'égalité des deux chemins n'est pas tenue, ou si (a) la même sonde"),
("M-1c", "; en (iii), « des scores par jeton de la sonde » devient « des scores d'action de la sonde » ; tout le reste de l'essai",
 "; en (iii), « des scores par jeton de la sonde » devient « des scores d'action de la sonde » ; la phrase « **Égalité des deux chemins, jouée avant (i)** : … jamais un score. » est retirée, et « l'égalité des deux chemins n'est pas tenue, ou si » est retiré de la règle d'échec ; tout le reste de l'essai"),
("m-2", "(une permutation tirée par la graine `alignement/<sonde>`)",
 "(une permutation, `permutation(n)` du générateur neuf de la graine `alignement/<sonde>`, n étant le nombre d'actions de `H` d'au moins un jeton noté, rangées dans l'ordre des clés : l'action de rang k reçoit les scores de l'action dont le rang est l'élément k de la permutation)"),
("m-3", "Cette garde tient lieu d'effectif minimal : aucun autre n'est écrit.",
 "Cette garde tient lieu d'effectif minimal : aucun autre n'est écrit. Les blocs d'un jeu sont les tâches qui y portent au moins une action notée : une tâche réduite à une seule classe reste un bloc ; une tâche sans aucune action notée sur ce jeu n'en est pas un."),
("m-4", "leur déséquilibre de tirage touche la sonde et les 800 directions de la même façon, et l'essai ne compare aucun prédicteur trivial.",
 "leur déséquilibre de tirage touche chaque direction, sonde comprise, selon sa propre dépendance au rang et à la longueur, et le rééchantillonnage par tâches en porte la variabilité ; l'essai ne compare aucun prédicteur trivial."),
("m-5a", "au chapeau, « Il est défini sur les scores par jeton livrés des sondes (option (b)) :",
 "au chapeau, « **Il est défini sur les scores par jeton livrés des sondes** (option (b)) :"),
("m-5b", "devient « Il est défini sur les scores d'action livrés :",
 "devient « **Il est défini sur les scores d'action livrés** :"),
("m-6", "l'essai à blanc n'écrit ni trace de livraison ni bordereau.",
 "l'essai à blanc n'écrit ni trace de livraison ni bordereau. Du côté exposé, aucune personne ni aucun programme autre que le code de la passe n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi."),
]
c=b
for k,x,y in R:
    n=c.count(x); print(k,'occurrences',n)
    assert n==1
    c=c.replace(x,y)
p=T+'b12_corrige_essai.md'; open(p,'w',encoding='utf-8').write(c)
print('validateur copie corrigée :', prereg.problemes(p))
L=c.split('\n'); print('marqueurs', [i+1 for i,l in enumerate(L) if 'À REMPLIR' in l], 'lignes', len(L))
json.dump(R, open(T+'remplacements.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
# vérifier la bonne lecture du retour (b-5) sur le texte corrigé : chaînes citées présentes
for s in ["**Il est défini sur les scores par jeton livrés des sondes** (option (b)) : il éprouve la chaîne à partir de ces scores (agrégation par le maximum, étiquettes, clés, aire, plancher, intervalle) ; le produit scalaire, fait sur la carte, est éprouvé par","l'égalité des deux chemins n'est pas tenue, ou si "]:
    print('présent hors (b-5):', c.count(s))
