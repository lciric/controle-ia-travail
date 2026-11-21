MODULE = "comparaisons_lentilles_v1.py"
ESSAIS = ["test_lentilles_sondes_bbis_seconde_passe_lecture_comparaisons_v1.py"]
ALTERATIONS = [
 ("p de recouvrement non conservateur", "return float((1 + int((o >= int(valeur)).sum())) / (o.numel() + 1))", "return float((1 + int((o > int(valeur)).sum())) / (o.numel() + 1))"),
 ("lecture commune sans le recouvrement", "if libelle_publique == c and libelle_notre_r == c and libelle_du_recouvrement == RECOUVREMENT_AU_DELA:", "if libelle_publique == c and libelle_notre_r == c:"),
 ("lecture propre : lentille mal nommée", 'return {"libelle": LECTURE_PROPRE, "lentille": K2.LENTILLE_NOTRE_R, "autre": K.LENTILLE_PUBLIQUE}', 'return {"libelle": LECTURE_PROPRE, "lentille": K.LENTILLE_PUBLIQUE, "autre": K2.LENTILLE_NOTRE_R}'),
 ("niveau du recouvrement changé", "if p_iso <= K.P_ISO_CONCENTREE and p_signes <= K.P_SIGNES_CONCENTREE:\n        return RECOUVREMENT_AU_DELA", "if p_iso <= K.P_NON_DISTINCTE and p_signes <= K.P_SIGNES_CONCENTREE:\n        return RECOUVREMENT_AU_DELA"),
 ("notre S comparée à une lentille R", "if K2.LENTILLE_NOTRE_S in (a, b) or K2.PLONGEMENTS_SEULS in (a, b):", "if False:"),
 ("paire hors du texte acceptée", "if (a, b) not in PAIRES:", "if False and (a, b) not in PAIRES:"),
 ("moitiés sous le nul des signes", "if paire == PAIRE_MOITIES and set(rangs_nuls) - {K.NUL_ISOTROPE}:", "if False:"),
 ("appariement non exigé", "if len(valeurs) != 1:", "if len(valeurs) < 1:"),
 ("calibration : borne basse appliquée", '"tenue": bool(compte <= haut)}', '"tenue": bool(_ <= compte <= haut)}'),
 ("calibration : borne haute ignorée", '"tenue": bool(compte <= haut)}', '"tenue": True}'),
 ("recouvrement des colonnes faux", "return (rangs_a[:, None, :] == rangs_b[None, :, :]).any(1).sum(0).to(torch.int64)", "return (rangs_a == rangs_b).sum(0).to(torch.int64)"),
 ("médiane basse", "return float(np.median(torch.as_tensor(recouvrements_nuls).numpy()))", "return float(torch.as_tensor(recouvrements_nuls).median())"),
 ("témoins : égalité non comptée contre le témoin", "au_moins = nuls.numel() - torch.searchsorted(nuls, o_t, right=False)", "au_moins = nuls.numel() - torch.searchsorted(nuls, o_t, right=True)"),
]
