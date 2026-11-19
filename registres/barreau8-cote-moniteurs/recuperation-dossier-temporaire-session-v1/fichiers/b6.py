import pathlib, sys, hashlib, subprocess
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B5 = D/'prereg-lecture-sondes-barreau8-v1-brouillon5.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon6.md'
assert not P.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert sha(B5) == 'eb3e770d5b7420546331f3bff78ef5495a098862be84ff6a03f97f84100a0c6f'
V5 = 'docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v5.md'
H5 = '407099bc150b8730237cceb0c1cf051440e255b483f44461b38a6c835c13107f'
assert sha(R/V5) == H5
t = B5.read_text(encoding='utf-8'); fautes = []
def r(a, b, n=1):
    global t
    c = t.count(a)
    if c != n: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
def coupe(debut, fin, neuf):
    global t
    if t.count(debut) != 1 or fin not in t[t.index(debut)+len(debut):]:
        fautes.append(('coupe', debut[:70], fin[:50])); return
    i = t.index(debut); j = t.index(fin, i+len(debut))
    t = t[:i] + neuf + t[j:]
V3 = "`docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v3.md` (`477815d1b48fc681ae4d403f81cf6f6fcff5750611e74f784db802013eed05f1`)"
r("(son titre dit « v2 », son fichier « v3 » : écart de forme déclaré par la session mère), lue en entier, " + V3 + " ;", "**version 5** (son titre dit « v4 » : écart de forme déclaré par la session mère), lue en entier, `" + V5 + "` (`" + H5 + "`) ; elle remplace la version 3 (`477815d1b48fc681ae4d403f81cf6f6fcff5750611e74f784db802013eed05f1`), citée aux brouillons 4 et 5 ;")
r(V3, "`" + V5 + "` (`" + H5 + "`)")
r("— v1 — brouillon 5", "— v1 — brouillon 6")
r("**Statut : brouillon 5, non scellé", "**Statut : brouillon 6, non scellé")
r("brouillon 5 écrit entre 2026-11-19T00:54Z et 2026-11-19T00:59Z (`date -u`).", "brouillon 5 écrit entre 2026-11-19T00:54Z et 2026-11-19T00:59Z ; brouillon 6 écrit entre 2026-11-19T01:02Z et HEURE_DE_FIN (`date -u`).")
r("(ce ne sont pas des résultats sur un organisme) : lecture incidente, non repris.", "(ce ne sont pas des résultats sur un organisme) : lecture incidente, non repris. **Lecture incidente déclarée par le contre-lecteur du brouillon 4** (son rapport, « Fichiers lus ») : la ligne 2206 du même texte, rendue par une recherche de motif, porte des noms de champs et des valeurs attendues de paramètres, pas de résultats ; non reprise ici, et non lue par le rédacteur.")
coupe("| I-9 |", "| I-10 |", "| I-9 | lectures du dommage (1) et de la diffusion (2) | vocabulaire donné (question 9). Lecture (1), champ `phrase` : « non calculable », « dommage agrégé vu », « dommage non distingué du témoin-jumeau », « dommage non vu à cette puissance ». **Portée : une seule phrase du dommage pour toute la course, décidée sur la pleine dose ; aucune phrase par condition** (question (9), ligne « Portée »). Lecture (2) : par base et par unité, « réussit », « échoue », « non calculable » : **établi par la note pour l'extrait des états** (section « Livraison », alinéa « Extrait des seuls états des lectures » : l'extrait ne porte que ce vocabulaire et les phrases de la question (9), l'état de l'unité étant sous la clé `unite`) ; la question (9) dit encore que la fonction d'état de la pièce n'a pas été relue par la note : le contrôle mécanique à la réception reste (D-12). Phrase de la lecture (2) : « diffus réalisé, à titre exploratoire, hors juge d'une autre lignée » ou `null` |\n")
coupe("| D-12 |", "| D-13 |", "| D-12 | **extrait des seuls états** des lectures du dommage (1) et de la diffusion (2) : fichier `docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json` et son compagnon `.sha256`, écrit par programme par le côté exposé, **seulement après le scellement de ce texte** (le programme refuse sans une ligne `SCELLEMENT-SONDES-IIB` au registre `registres/sondes-iib-v1.md` dont le texte cité est scellé à l'empreinte de la ligne : note d'interface, section « Livraison »). **Clés fixes, liste fermée** : `lecture_dommage.phrase` ; `lecture_diffusion.par_paire.<paire>.<base>` pour les paires `B100-H`, `B50-H` et `TJ100-H`, avec les bases `cout`, `traits`, `mots_et_cout` et l'état de l'unité `unite` ; pour la paire `B100-TJ100`, `mots_et_cout` seule ; `lecture_diffusion.phrase`. **Contrôle mécanique à la réception** : empreinte du fichier égale à son compagnon et à la ligne `ETATS-COURSE-IIB` (inscrite par la session mère) ; clés exactement celles-là, aucune manquante, aucune en trop (la note dit l'extrait « sans aucun chiffre hors du nom du run et des noms des conditions » sans nommer de clé pour le nom de la course : une telle clé serait en trop) ; `lecture_dommage.phrase` parmi les quatre phrases de I-9 ; chacun des treize états parmi les trois mots ; `lecture_diffusion.phrase` égale à la phrase de I-9 ou `null`. **Tout autre mot, une clé manquante ou une clé en trop : refus d'ouvrir**, fait porté à la session mère (liste d'arrêt, ligne 3) ; jamais une traduction. Essai sur cas sain et sur artefacts (clé manquante, clé en trop, mot hors du vocabulaire, chiffre dans une valeur, empreinte altérée) | la lecture |\n")
coupe("| D-14 |", "\n## Hypothèse", "")
r("  - **(a) dommage** : la phrase de la lecture (1), **unique pour toute la course et décidée sur la pleine dose** (I-9), est exactement « dommage agrégé vu ».", "  - **(a) dommage** : la valeur de la clé `lecture_dommage.phrase` de l'extrait, phrase **unique pour toute la course et décidée sur la pleine dose** (I-9 ; note d'interface, question (9), ligne « Portée »), est exactement « dommage agrégé vu ».")
r("  - **(b) diffusion** : l'état de l'unité `<c>-H` de la lecture (2) est exactement « échoue »", "  - **(b) diffusion** : la valeur de la clé `lecture_diffusion.par_paire.<c>-H.unite` de l'extrait (`lecture_diffusion.par_paire.B100-H.unite` pour `B100`, `lecture_diffusion.par_paire.B50-H.unite` pour `B50`) est exactement « échoue »")
r("Seul l'état **de l'unité** est lu ; les états par base et les phrases de la lecture (2) ne sont pas lus par la règle.", "**Seules ces trois clés entrent dans la règle.** Les autres valeurs de l'extrait — les bases séparées `cout`, `traits` et `mots_et_cout` des paires `B100-H`, `B50-H` et `TJ100-H`, l'unité de la paire `TJ100-H`, la base `mots_et_cout` de la paire `B100-TJ100` et `lecture_diffusion.phrase` — **sont recopiées telles quelles en tête de la sortie de la lecture et du verdict, sous le titre « contexte de la course, sans effet sur le verdict »** : elles n'entrent dans aucun état, aucune ligne de la table des issues, aucune réserve, et le juge ne les commente pas.")
r("Les lectures (1) et (2) sont jouées par leur lecteur, par leurs propres scripts,", "Les lectures (1) et (2) **ne sont jouées qu'après le scellement de ce texte** (session mère ; l'extrait de leurs états n'est écrit qu'après lui : note d'interface, section « Livraison »), par leur lecteur, par leurs propres scripts,")
r("; l'extrait recopie ces empreintes et ces lignes) ;", "; l'extrait ne porte ni ces empreintes ni ces lignes) ;")
r("| 3 | extrait scellé des seuls états absent, d'empreinte différente de la ligne `ETATS-COURSE-IIB`, ou portant autre chose que sa liste fermée (un chiffre, un champ de plus), ou une phrase du dommage ou un état hors du vocabulaire de I-9 |", "| 3 | extrait `etats-lectures-iib-v1.json` absent, d'empreinte différente de son compagnon ou de la ligne `ETATS-COURSE-IIB`, clé manquante, clé en trop, ou valeur hors du vocabulaire de I-9 (D-12) |")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t, encoding='utf-8'); print("ok", h, len(t.splitlines()))
