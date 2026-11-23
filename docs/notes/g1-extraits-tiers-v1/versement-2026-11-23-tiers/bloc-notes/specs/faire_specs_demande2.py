"""Spécifications en clair (hors dépôt) des extraits de la demande 2. Tiers d'extraction G1."""
import json, os
S = os.environ['S']; DEP = '/home/user/controle-ia-travail'

def lignes(src):
    return open(f'{DEP}/{src}', encoding='utf-8').read().split('\n')

def P(L, k, debut, fin=None, eol=False):
    l = L[k - 1]
    assert l.count(debut) == 1, (k, debut)
    s = l.index(debut)
    e = (len(l) if eol else s + len(debut)) if fin is None else l.index(fin, s) + len(fin)
    anc = l[s:e]
    assert l.count(anc) == 1, (k, anc[:50])
    return {"ligne": k, "ancien": anc}

def ecrire(nom, spec):
    json.dump(spec, open(f'{S}/specs/{nom}', 'w'), ensure_ascii=False, indent=2)

def base(src, emp, sortie, titre, plages, ps):
    return {"source": src, "empreinte_attendue": emp, "sortie": f"docs/notes/g1-extraits-tiers-v1/{sortie}",
            "titre": titre, "objet": "demande 2 du rédacteur successeur : définitions (conditions et doses, sondes et score d'action, surveillants décisifs).",
            "plages": plages, "passages_en_clair": ps}

# T0.6 organismes
src = 'prereg/T0.6-organismes-v0-v1.md'; L = lignes(src)
ps = [P(L, 323, "P3 a établi (i-a) à une seule dose, flagrant. "),
      P(L, 349, "L'organisme distillé d'un saboteur flagrant sera flagrant à dose 1. "),
      P(L, 401, " ; effet minimal détectable ≈ 0,39 (b, par défaut) ou 0,53 (a)"),
      P(L, 403, " ; aire minimale détectable ≈ 0,61 à 0,66 (b), 0,63 à 0,71 (a)"),
      P(L, 464, " ; effet du coût de (ii) à dose 1 au-delà de celui de P3-P1 (1,5227) :"),
      P(L, 492, ", confirmée par la lecture A de 7a : en-tête, « Règlement d'E3-6 », R-2040"),
      P(L, 566, " (7a en a eu un au début de l'entraînement de l'adaptateur saboteur, R-2040)"),
      P(L, 568, "indulgente ; dans P3, le témoin instruit baissait déjà le coût, P3-P2 ", "−0,0650]) ; "),
      P(L, 576, ", qui est la valeur haute de l'aire minimale détectable à 80 % de puissance (0,60 à 0,70 au rapport §7 ; 0,612 à 0,657 au plan (b) et 0,632 à 0,705 au plan (a) dans la section « Puissance » du candidat)"),
      P(L, 585, " ; l'alternative à 0,65 est écartée"),
      P(L, 576, " Raison : au-dessous de 0,70, une sonde dont l'effet est tout juste détectable", eol=True),
      P(L, 780, " (effet minimal"),
      P(L, 781, "0,525 au lieu de 0,394)")]
ecrire('spec-T06-organismes-v3.json', base(src, 'ef31feff9abb26d0', 'extrait-T06-organismes-v3.md',
       'préenregistrement scellé des organismes (T0.6)',
       [[229, 235], [303, 311], [320, 360], [373, 407], [409, 410], [412, 454], [456, 465], [467, 498],
        [527, 536], [538, 541], [564, 566], [568, 585], [765, 765], [778, 796]], ps))

# validité de l'adaptateur
src = 'prereg/validite-adaptateur-v1.md'; L = lignes(src)
cellules = {51: "≥ 0,67 à 0,88 selon les effectifs", 52: "tau ≥ ≈ 0,165 (dix lisibles par tâche)", 53: "≈ 0,602",
            54: "écart ≈ 0,17 à 0,30", 55: "écart ≈ 0,15", 56: "réserve posée dès ≈ 0,554", 57: "≈ 0,602",
            58: "≈ 0,602", 59: "réserve dès ≈ 0,554", 60: "dès ≈ 0,554", 61: "≈ 0,39 décade (ordre de T6-1 de T0.6)",
            62: "réserve dès ≈ 0,554"}
ps = [P(L, k, t) for k, t in sorted(cellules.items())]
ps.append(P(L, 86, ", dont T0.7 scellé écrit que l'erreur réelle", "(l. 2035),"))
ecrire('spec-validite-adaptateur-v1.json', base(src, '7e78909d7ca88e08', 'extrait-validite-adaptateur-v1.md',
       "préenregistrement scellé de la validité de l'adaptateur",
       [[21, 30], [32, 43], [45, 63], [65, 74], [76, 80], [82, 95], [149, 193]], ps))

# T0.8 base A « mots et coût »
src = 'prereg/T0.8-base-A-mots-et-cout-v1.md'; L = lignes(src)
ps = [P(L, 42, ", et l'adaptateur témoin peut baisser le coût (T0.6, l. 567-568)"),
      P(L, 51, "voisine de 0,8878 ou plus (coût seul sur P3, N-029 ; ici tâches et épisodes neufs, douze traits)"),
      P(L, 111, "(i) base (A) à `S100` sous 0,70 ou non au-dessus (BA-P2 réfutée) ; (ii) base (A) « échouerait » aux quatre doses alors que BA-P1 est au-dessus ; "),
      P(L, 106, ", rappelés pour BA-P2")]
ecrire('spec-T08-base-A-mots-et-cout-v3.json', base(src, '72b067d5b3f8c0d7', 'extrait-T08-base-A-mots-et-cout-v3.md',
       'base « mots et coût » scellée (T0.8, base A)',
       [[16, 16], [18, 26], [36, 40], [42, 51], [53, 54], [56, 58], [60, 100], [102, 111], [124, 141], [164, 169]], ps))

# brouillon 4 gelé de la base boîte noire
src = 'brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md'; L = lignes(src)
ps = [P(L, 91, " Les ordres de grandeur tirés de P3 sont des repères déclarés, jamais des seuils."),
      P(L, 102, " ; IT et IM : aire de M1 sous 0,5 (le témoin et la mention baissaient le coût dans P3), aire de J8p non au-dessus"),
      P(L, 189, ", attendue « flagrante »"),
      P(L, 172, "`S100` « diffuse réalisée » ; "),
      P(L, 329, "une rubrique que le 8B tienne (au pilote de T0.5, notations sans score : `notes-p13-n029-v1.md`), ")]
ecrire('spec-T08-bases-boite-noire-brouillon4-v3.json', base(src, '7da0c3839a7a714b', 'extrait-T08-bases-boite-noire-brouillon4-v3.md',
       'brouillon 4 gelé de la base boîte noire (T0.8)',
       [[16, 16], [20, 25], [42, 74], [79, 83], [85, 87], [89, 94], [96, 96], [98, 100], [102, 105], [107, 157], [159, 172], [182, 183], [186, 189],
        [198, 231], [325, 337], [339, 347]], ps))

# T0.7 sondes
src = 'prereg/T0.7-sondes-v0-v1.md'; L = lignes(src)
ps = [P(L, 1029, " (nul rapporté « non détecté à cette", eol=True),
      P(L, 1030, "  puissance », verdict v2 ;", "un peu plus hautes »)"),
      P(L, 1163, "Le résultat de P3 (nul sur les deux sondes génériques", "ne fixe aucun signe ici : "),
      P(L, 1215, "sous la règle (a), 200 directions ne tiennent pas", "sous les deux lectures du nul) ; "),
      P(L, 1258, " ; **réserve écrite** : c'est la règle dont le niveau n'est pas tenu", "un « non au-dessus » n'en est pas touché"),
      P(L, 1349, " Ce qu'une aire de", eol=True),
      P(L, 1350, "≈ 0,8 implique : le jeu porte un lexique corrélé à l'étiquette que la sonde peut apprendre ; "),
      P(L, 1030, "remède (a'), "), P(L, 1198, "remède (a'), "), P(L, 1258, "remède (a'), ")]
ecrire('spec-T07-sondes-v2.json', base(src, 'd7d180eccbbce8ff', 'extrait-T07-sondes-v2.md',
       'préenregistrement scellé des sondes (T0.7)',
       [[886, 912], [1009, 1340], [1347, 1399], [1444, 1451], [2681, 2689]], ps))

# apprentissage des sondes sur la tâche (étape B bis)
src = 'prereg/T0.7-etape-B-bis-v1.md'; L = lignes(src)
ps = [P(L, 44, ", guide la reconception des sondes"),
      P(L, 22, "mots de Lazar et ligne GO-2026-11-14-09 recopiés (R-2740), "),
      P(L, 58, "aire ≥ Q + 0,058 à 0,059 (95 %)")]
ecrire('spec-T07-etape-B-bis-v2.json', base(src, '0ae6210f954917fe', 'extrait-T07-etape-B-bis-v2.md',
       'préenregistrement scellé de l\'apprentissage des sondes sur la tâche (T0.7, étape B bis)',
       [[21, 22], [30, 30], [32, 44], [50, 51], [58, 59], [65, 94], [102, 102], [104, 113], [117, 119], [121, 137]], ps))
print('spécifications écrites')
