MODULE = "lecture_entree_v1.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_lecture_comparaisons_v1.py"]
ALTERATIONS = [
 ("K à droite au lieu du covecteur à gauche", "return k.T @ c", "return k @ c"),
 ("pas de normalisation", "u = torch.where(calculable[None, :], g / torch.where(calculable, normes, torch.ones_like(normes))[None, :], torch.zeros_like(g))", "u = g"),
 ("plongements non centrés", "return plongements - plongements.mean(0, keepdim=True)", "return plongements"),
 ("norme nulle non vue", "calculable = torch.isfinite(normes) & (normes > 0) & torch.isfinite(g).all(0)", "calculable = torch.isfinite(normes) & (normes >= 0) & torch.isfinite(g).all(0)"),
 ("garde de S : artefact (ii) non joué", "    artefact(ARTEFACT_TRANSPOSEE, k.T.contiguous(), plongements)\n", "    artefacts[ARTEFACT_TRANSPOSEE] = 64\n"),
 ("garde de S : seuil de 32 colonnes abaissé", "if differentes < K.MIN_COLONNES_ARTEFACT:", "if differentes < 0:"),
 ("garde de S : écart du cas sain toléré", "        raise Arret(f\"garde de la fonction de lecture (notre S, couche {couche}) : écart sur le cas sain", "        continue\n        raise Arret(f\"garde de la fonction de lecture (notre S, couche {couche}) : écart sur le cas sain"),
 ("plongements liés : artefact (iii) joué quand même", "if plongements_lies:\n        artefacts", "if False:\n        artefacts"),
 ("rapport à ε : moitiés oubliées", "repli = not all(tenue.values())", "repli = not all(v for l, v in tenue.items() if l in K2.LENTILLES_R)"),
 ("rapport à ε : seule la lentille fautive refaite", "\"lentilles_refaites\": [l for l in K2.LENTILLES_R if repli and l in rho_min],", "\"lentilles_refaites\": [l for l in K2.LENTILLES_R if repli and l in rho_min and not tenue[l]],"),
]
