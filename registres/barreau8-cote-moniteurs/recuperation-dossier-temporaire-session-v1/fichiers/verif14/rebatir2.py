D='brouillons/barreau8-lecture-sondes-v1/'
b13=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon13.md',encoding='utf-8').read()
b14=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon14.md',encoding='utf-8').read()
t=open(S:=__import__('sys').argv[1],encoding='utf-8').read()  # b13 + R-1 + R-2
L14=b14.split('\n')
def rep(o,n,lab):
    global t
    c=t.count(o); assert c==1,(lab,c); t=t.replace(o,n); print('ok',lab)
# (b) ajout du rédacteur, juste après R-1
rep("devient « l'essai n'échoue que par (a) ou (b) » ; tout le reste de l'essai",
    "devient « l'essai n'échoue que par (a) ou (b) » ; les deux phrases qui suivent celle de l'égalité, « Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués. » et « L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier. », sont retirées ; tout le reste de l'essai","(b) ajout b-5")
# O-6
rep("la phrase « Pour les neuf sondes, les scores par jeton sont livrés aussi … sur toutes les actions. » est retirée",
    "la phrase « **Pour les neuf sondes, les scores par jeton sont livrés aussi : la garde de réception r7 recalcule leur maximum et leur moyenne sur toutes les actions.** » est retirée","O-6")
# T-1
rep("sur toute entrée de l'index qui porte le nom de l'une des neuf sondes nommées,",
    "sur toute entrée qui porte le nom de l'une des neuf sondes nommées, dans l'index de chacun des trois fichiers de sondes et de planchers,","T-1")
# T-4 règle mécanique
rep("qui paraît plus d'une fois dans l'index, ne rendent pas","qui paraît plus d'une fois dans l'index de son fichier, ne rendent pas","T-4 règle")
# (c) plan point 3
rep("paraît plus d'une fois dans l'index.","paraît plus d'une fois dans l'index de son fichier.","(c) plan 3")
# (c) P1
rep("ou y paraît plus d'une fois,","ou paraît plus d'une fois dans l'index de son fichier,","(c) P1")
# (c) liste d'arrêt 8
rep("en double dans l'index |","en double dans l'index de son fichier |","(c) arrêt 8")
# T-3, T-2
rep("jamais un score. Pour chaque essai,","jamais un score. Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués. L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier. Pour chaque essai,","T-3+T-2")
# (a) r5
rep("- (r5) cohérence : 2 560 actions ;","- (r5) cohérence : 2 560 actions, le champ `rang` de chaque ligne de l'index étant le rang de cette ligne dans le fichier, à partir de 0 ;","(a) r5")
# fait transmis
rep("refuse de tourner s'ils diffèrent (plan, point 3) ;",
    "refuse de tourner s'ils diffèrent (plan, point 3 ; fait transmis par la session mère, d'après le côté exposé, non vérifiable par le côté des moniteurs, et qui ne change rien à la règle : les deux champs `run_id` — celui de l'extrait du côté exposé qui accompagne la note d'interface, D-13, d'où la trace de la passe tire le nom de la course, et celui de l'extrait des états — reçoivent la même valeur, celle du manifeste de la course ; le côté exposé les compare par programme avant tout versement) ;","fait run_id")
# en-tête : lignes 1,3,5,7,24 et section contre-lecture (440-441) prises du b14, contrôlées par le diff mot à mot
L=t.split('\n')
for i in (0,2,4,6,23): L[i]=L14[i]
L[439:440]=L14[439:441]
t='\n'.join(L)
print('égal au brouillon 14 :', t==b14)
