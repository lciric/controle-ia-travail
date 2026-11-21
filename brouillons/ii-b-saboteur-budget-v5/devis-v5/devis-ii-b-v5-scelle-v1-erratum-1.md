# Erratum 1 au devis scellé (`cb881522…`) — épisodes distillés comptés jusqu'à 127, non 96

Écrit le 2026-11-21 par la session de reconception. Il prime sur les comptes visés ; il ne change ni le plafond (60 USD), ni la coupure (55), ni la coupure de l'étalonnage (12), ni le fichier d'entrées (45 USD, prix borne 1,38, **coût fixe scellé 6,90 USD, inchangé, tel qu'accordé par GO-2026-11-21-70**), ni le plafond de tours (63), ni les dates.

**Cause.** Contre-lecture du distillateur (`brouillons/ii-b-saboteur-budget-v5/code-v5/distillateur-v5/contre-lecture-cl1/contre-lecture-distillateur-organisme-retenu-v5-cl1.md`, point 2) : la conception d'origine (§ 4) écrit « tous les épisodes acceptés à cet instant sont distillés (au plus 96 + 31 = 127) » ; la course finit le tour où la cible est atteinte. Le devis comptait 96 au plus. Tronquer à 96 choisirait des épisodes : interdit sans règle.

**Recalcul.** `calcul-devis-ii-b-v7.py` (seules deux constantes changent : épisodes acceptés au plus 127 ; actions d'oracle hors tours sous le nœud 7 (b′) : 1 270 + 2 560 = 3 830) et sa sortie `sortie-calcul-devis-ii-b-v7.txt`, à côté.
- Attendu, ligne entière : 15,63 USD à 12 tours (au lieu de 15,46), 21,38 à 24 tours (au lieu de 21,21) [L24, L25].
- Pire d'une course de 24 tours : 53,86 USD (au lieu de 53,41) [L29] ; pire de la ligne, celui que tiennent les gardes : 59,76 USD, inchangé [L52].
- Coût fixe aux durées attendues et au prix borne : 7,03 USD [L40], contre 6,90 scellé ; l'écart de 0,13 USD est absorbé par la tolérance des tours (49 %) ; le plafond de tours reste 63 sous l'une ou l'autre valeur ((45 − 2,97 − 6,90 − 0,75) / 0,542 = 63,4).
- Le fichier d'entrées porte 3 830 actions d'oracle hors tours (au lieu de 3 520).
