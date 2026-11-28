# Chaque « ancien texte » des corrections VCB4 : trouve une seule fois (blancs reduits) dans le texte ou le plan ? En memoire.
import re
B = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b/brouillon4/"
T = re.sub(r"\s+", " ", open(B + "P3b-seconde-lecture-v1-brouillon4.md", encoding="utf-8").read())
P = re.sub(r"\s+", " ", open(B + "plan-code-et-chaine-P3b-v4.md", encoding="utf-8").read())
Q = re.sub(r"\s+", " ", open(B + "questions-ouvertes-P3b-v4.md", encoding="utf-8").read())
anciens = {
 "01": ("T", "elle s'applique mot pour mot au texte principal, après le retrait des marqueurs et des autres versions, puis elle est retirée."),
 "02-1": ("T", "(60 tâches ; Version de repli (B) de P-016 : 40)"),
 "02-2": ("T", "Version de repli (B) de P-016 : « 40 tâches pour les bras génériques et la double comptabilité ; plis de T4 résiduel des bras génériques : clé `plis/lecture-40`, 5 plis de 8 tâches. »"),
 "02-2a": ("T", "se lisent sur les 60 tâches"),
 "02-3": ("T", "Version de repli (B) de P-016 : « Le leurre de la double comptabilité est tiré parmi les 40 tâches"),
 "02-4": ("T", "Version de repli (B) de P-016 : « 5 plis de 4 tâches de confirmation ; l'oracle du pli k apprend sur la découverte et les 16 autres tâches de confirmation. »"),
 "02-4a": ("T", "5 plis de 8 tâches ; l'oracle du pli k apprend, au réglage choisi, sur la découverte et les 4 autres plis"),
 "02-5": ("T", "`plis/lecture-60`, Version de repli (B) de P-016 : `plis/lecture-40` ; oracle"),
 "02-6": ("T", "sur 60 tâches (Version de repli (B) de P-016 : 40)"),
 "02-7": ("T", "`plis/lecture-60` (Version de repli (B) de P-016 : `plis/lecture-40`)"),
 "02-8": ("T", "; Version de repli (B) de P-016 : « bras génériques lus sur 40 tâches, oracle sur les 20 de la confirmation »)"),
 "02-8a": ("T", "bras génériques lus sur 60 tâches, oracle sur les 40 de la confirmation"),
 "03-1": ("T", "Version de repli (A) de N-032 : « **Mesure avant le scellement"),
 "03-2": ("T", "Version de repli (B) de N-032 : « **Mesure avant le scellement (M-P3b-2, processeur, par code ; lit"),
 "03-2a": ("T", "**Contrôle avant dépense M-P3b-2"),
 "03-3": ("T", "Version de repli (A) de N-032 : « Mesure M-P3b-2"),
 "03-4": ("T", "Version de repli (B) de N-032 : « Compte unique"),
 "03-5T": ("T", "Version de repli (B) de N-032 : de même, avec « mesure M-P3b-2 avant le scellement (un seul compte, toutes conditions confondues) ».)"),
 "03-5P": ("P", "Version de repli (B) de N-032 : de même, avec « mesure M-P3b-2 avant le scellement (un seul compte, toutes conditions confondues) ».)"),
 "04": ("T", "le marqueur se remplit au candidat par le seul texte de la version retenue, mot pour mot]**"),
 "04Q": ("Q", "`<<PARTITION_P016>>` se remplit au candidat par le seul texte retenu (CR-P3b-texte-15)."),
 "05-1": ("T", "(borne de l'étape : 7,5 USD ; Version de repli (B) de P-024 : 8,6 USD)"),
 "05-2": ("T", "borne de l'étape 7,5 USD (Version de repli (B) de P-024 : 8,6 USD)"),
 "05-3": ("T", "+ 1,2 USD (Version de repli (B) de P-024 : + 2,16 USD)"),
 "05-4": ("T", "(7,5 USD ; Version de repli (B) de P-024 : 8,6 USD)"),
 "05-5": ("T", "compris dans la borne de 7,5 USD)"),
 "06": ("T", "dans P3b-P9, « T4 de P3 (quintiles) » devient « T4 résiduel (deux spécifications, recouvrement) » ;"),
 "06a": ("T", "sur les 32 couches, est au-dessus"),
 "07-1": ("T", "écart (vii) retiré ; « Oracle », étiquettes : « **positifs** = actions du saboteur étiquetées 1 par T1 (coût"),
 "07-2": ("T", "seule. » ; étiquettes : « **positifs** = actions du saboteur étiquetées 1 par T1 ; **négatifs** ="),
 "07-3": ("T", "la puce « entrée » et la puce « choix » sont remplacées par"),
 "08-1": ("T", "Version de repli (C) de P-024, suite : à l'étape 2.6, « jamais poussés » devient « poussés seuls, en morceaux, à leurs chemins et empreintes ». Dans tous les cas, la garde après un refus de poussée reste bornée à 24 heures (liste d'arrêt)."),
 "08-2": ("T", "confiance ≈ 60 %]** Version (A), écrite ici : « Les états à t_cost"),
 "08-3": ("T", "gardés **en mémoire et sur le disque de l'instance seulement** (scellés, jamais poussés ;"),
 "09-P": ("P", "(toute suite d'espaces et de retours à la ligne lue comme une espace)** (cas sain : candidat sans ces chaînes ; artefacts : chacune, au singulier et au pluriel, et chacune coupée par un retour à la ligne suivi d'espaces)"),
 "09-T": ("T", "sans égard à la casse ni aux retours à la ligne."),
}
src = {"T": T, "P": P, "Q": Q}
for k, (f, s) in anciens.items():
    print(k, f, src[f].count(re.sub(r"\s+", " ", s)))
