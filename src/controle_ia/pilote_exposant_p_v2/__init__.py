"""Pilote préenregistré de l'exposant p, version 2 (brouillon 2 du préenregistrement) : plan (évaluation, registre) sur
Llama-3.1-8B-Instruct, instrument de Ferreira da Silva et Heimersheim (arXiv 2606.24964).

Fichiers neufs (R12) ; ce qui ne change pas est importé de `controle_ia.pilote_exposant_p` (v1) sans modification :
copie amont, références publiées, ajustement, directions, balayage, ancres.

Modules neufs :
- `stimuli` : stimuli v2 (paires minimales, porteur de statut au dernier mot, partagé entre registres ; R-S1 à R-S10),
  garde des classes lexicales et du modèle stylisé (contre-lecture R2, B1), jumeau neutre (emprunt à R9-bis) ;
- `analyse` : critères de lecture gelés v2 (moyenne de famille, qualificatif de famille, sensibilité sur le modèle lu,
  jumeau neutre, identification par moitiés, phrases bornées), audit de retrait d'un sous-ensemble, symétrie ;
- `courbes` : lectures descriptives des courbes d'un axe sur la fenêtre W de R9-bis ;
- `go` : vérification d'un GO de calcul dans `registres/go.md` (amorce) ;
- `run` : lanceur v2 (ordre gelé, réserve de temps des blocs décisifs, gardes éprouvées en mode jouet) ;
- `puissance` : simulation refaite (effet commun des sous-ensembles, plan lu tiré de la famille, bruit recalé).
"""
VERSION = "pilote-exposant-p-v2"
MARQUEUR_R9_BIS = "<<DOI_R9_BIS>>"
