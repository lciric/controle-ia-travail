"""Mutants de la vérification des corrections VCB (vérificateur neuf, R2).
(1) Mutants nommés, tels quels : RQ-17 et VCB-M01 à VCB-M17 de la vérification des corrections (copie exacte de sa
liste, `liste_mutants_verification.py`, sha256 5747332534241b99…) ; VCB-M01 essayé tel quel (son ancien texte a
disparu), puis porté (VCB-M01p, même substitution que les notes VCB) ; VCB-M18 et VCB-M19 des notes VCB.
(2) Mutants neufs de ce vérificateur (VCB2-M01 à VCB2-M14), contre les corrections VCB et le texte du brouillon 5.
Forme : identifiant, module, ancien texte (une seule occurrence exigée), nouveau texte, tests ciblés, ce qu'il simule."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from liste_mutants_verification import LR, MUTANTS as MV, RQ, T_LR, T_RQ  # noqa: E402

_par_id = {m[0]: m for m in MV}
NOMMES = ["RQ-17"] + [f"VCB-M{k:02d}" for k in range(1, 18)]
MUTANTS = [_par_id[i] for i in NOMMES] + [
    ("VCB-M01p", LR, '    lot = _champ(c, "lot_juge", "configuration de l\'étape")', '    lot = c.get("lot_juge", 8)',
     T_LR, "lecteur : lot_juge absent accepté (8 par défaut) (porté, comme les notes VCB)"),
    ("VCB-M18", RQ, '    for nom, rx in list(CITATIONS.items()) + [("commit du code d\'analyse", COMMIT_CITE)]:',
     "    for nom, rx in CITATIONS.items():", T_RQ, "lanceur : commit cité deux fois, deux valeurs, accepté"),
    ("VCB-M19", LR, "    if isinstance(lot, bool) or not isinstance(lot, int) or lot < 1:", "    if lot is None:", T_LR,
     "lecteur : lot_juge non entier positif accepté"),
    # --- neufs : échéances écrites au « Dépassement » (VCB-06)
    ("VCB2-M01", RQ, '        _avant(cx, echeance, f"avant la conversion et le repère de {nom}")\n', "", T_RQ,
     "lanceur : aucun contrôle d'échéance avant la conversion et le repère"),
    ("VCB2-M02", RQ, '        _avant(cx, echeance, f"avant l\'ancrage de {nom}")\n', "", T_RQ,
     "lanceur : aucun contrôle d'échéance avant l'ancrage"),
    ("VCB2-M03", RQ, '            _avant(cx, echeance, f"avant le rechargement de {nom} pour le témoin")\n', "", T_RQ,
     "lanceur : aucun contrôle d'échéance avant le rechargement pour le témoin"),
    # --- neufs : lot_juge au lecteur (VCB-02)
    ("VCB2-M04", LR, "lots = lots_du_rejeu(h4[j], j, entropie, lot_juge, plafond)",
     "lots = lots_du_rejeu(h4[j], j, entropie, 8, plafond)", T_LR,
     "lecteur : lot_juge exigé mais non employé (8 écrit en dur)"),
    ("VCB2-M12", LR, "    if isinstance(lot, bool) or not isinstance(lot, int) or lot < 1:",
     "    if isinstance(lot, bool) or not isinstance(lot, int) or lot < 0:", T_LR, "lecteur : lot_juge nul accepté"),
    # --- neufs : citations, intitulés non éprouvés par la vérification (VCB-03)
    ("VCB2-M05", RQ, '"configuration": empreinte_config(config), "run du pilote"', '"run du pilote"', T_RQ,
     "citation « Configuration du plan B » présente mais jamais comparée"),
    ("VCB2-M06", RQ, '"tâches": sha_taches, "run des notations": config["run_notations"],', '"tâches": sha_taches,',
     T_RQ, "citation « Run des notations rejoué » présente mais jamais comparée"),
    ("VCB2-M07", RQ, '"résumé des notations": notes["resume_sha256"], "invite RS1": invite["sha256"],',
     '"invite RS1": invite["sha256"],', T_RQ, "citation « Résumé des notations rejoué » jamais comparée"),
    ("VCB2-M08", RQ, '"résumé des notations": notes["resume_sha256"], "invite RS1": invite["sha256"],',
     '"résumé des notations": notes["resume_sha256"],', T_RQ, "citation « Invite RS1 » jamais comparée"),
    ("VCB2-M09", RQ, '"invite RS1": invite["sha256"],\n                    "index de l\'invite RS1": invite["index_sha256"]}',
     '"invite RS1": invite["sha256"]}', T_RQ, "citation « Index de l'invite RS1 » jamais comparée"),
    ("VCB2-M10", RQ, "        if next(iter(cites[juge])) != sha:", "        if False:", T_RQ,
     "citation des notations de chaque juge jamais comparée"),
    ("VCB2-M11", RQ, "        valeurs = set(rx.findall(texte))", "        valeurs = set(rx.findall(texte)[:1])", T_RQ,
     "citations : seule la première occurrence lue (répétition acceptée)"),
    # --- neufs : graine du témoin (VCB-01)
    ("VCB2-M13", RQ, "    torch.manual_seed(int(graine))\n    try:\n        with torch.no_grad():\n"
                     "            generes = modele.generate(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),\n"
                     "                                      generation_config=cfg)\n",
     "    try:\n        with torch.no_grad():\n"
     "            generes = modele.generate(input_ids=ids.to(appareil), attention_mask=masque.to(appareil),\n"
     "                                      generation_config=cfg)\n        torch.manual_seed(int(graine))\n", T_RQ,
     "témoin : graine posée après l'appel"),
    ("VCB2-M14", RQ, "    torch.manual_seed(int(graine))", "    torch.manual_seed(12)", T_RQ,
     "témoin : graine constante, la même pour tous les appels"),
]
