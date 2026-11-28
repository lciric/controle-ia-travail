"""E2 (premiere partie) — la table des etats et des issues du brouillon (G0), « Criteres de lecture geles », est-elle sans
trou ni chevauchement ? Enumeration exhaustive.

Predicats par sonde et par dose (texte, lignes 96 a 100) : d1, d3 (borne basse de D au niveau corrige > 0, clauses 1 et 3) ;
a1, a3 (aire > 0,50) ; t1, t3 (aire au-dessus des cinq predicteurs triviaux) ; g1, g3 (G-Antipode > 0) ; pf (G-Prefixe).
Etats, lus a la lettre :
  U          : a1, a3, d1, d3, t1, t3, g1, g3 et pf ;
  N-scalaire : clauses 1 et 3 tenues sur l'action entiere, pf en echec ;
  N          : clause 1 tenue, clause 3 en echec ;
  J          : D_bas > 0 sur la clause 1 ou 3, « mais dominee par un des 5 predicteurs triviaux, inversion de signe ou echec
               de G-Antipode » — deux lectures : (large) le defaut est sur l'une ou l'autre clause ; (meme clause) le defaut
               est sur la clause dont D_bas > 0 ;
  Z          : D_bas <= 0 des la clause 1.
Issues (lignes 104 a 108) : L1 si une sonde au moins est U ; L3 si aucune n'est U et une au moins est N-scalaire, N ou J ;
L2 si les trois sont Z. Une sonde peut n'etre lisible sur aucun jeu (tirages degeneres, classe absente) : le texte scelle
8e432cdc... lui donne l'etat E, le brouillon aucun."""
import itertools, json
NOMS = ("d1", "a1", "t1", "g1", "d3", "a3", "t3", "g3", "pf")
def etats(v, lecture):
    d1, a1, t1, g1, d3, a3, t3, g3, pf = v
    c1, c3 = d1 and a1 and t1 and g1, d3 and a3 and t3 and g3
    e = set()
    if c1 and c3 and pf: e.add("U")
    if c1 and c3 and not pf: e.add("N-scalaire")
    if c1 and not c3: e.add("N")
    defaut1, defaut3 = (not t1) or (not a1) or (not g1), (not t3) or (not a3) or (not g3)
    if lecture == "large":
        if (d1 or d3) and (defaut1 or defaut3): e.add("J")
    else:
        if (d1 and defaut1) or (d3 and defaut3): e.add("J")
    if not d1: e.add("Z")
    return frozenset(e)
res = {}
for lecture in ("large", "meme clause"):
    trous, chev, paires = [], 0, {}
    table = {}
    for v in itertools.product((False, True), repeat=9):
        e = etats(v, lecture); table[v] = e
        if not e: trous.append(dict(zip(NOMS, v)))
        if len(e) > 1:
            chev += 1; k = " et ".join(sorted(e)); paires[k] = paires.get(k, 0) + 1
    # exemple de chaque chevauchement
    ex = {}
    for v, e in table.items():
        k = " et ".join(sorted(e))
        if len(e) > 1 and k not in ex: ex[k] = {n: x for n, x in zip(NOMS, v)}
    # issues sur trois sondes : ensembles d'etats possibles par sonde
    ens = sorted(set(table.values()), key=lambda s: sorted(s))
    n_trou = n_chev = n_tot = 0; ex_issue = {}
    for trio in itertools.product(ens, repeat=3):
        # chaque sonde porte tous les etats de son ensemble : une issue « s'applique » si son predicat est vrai
        L1 = any("U" in s for s in trio)
        L3 = (not L1) and any(s & {"N-scalaire", "N", "J"} for s in trio)
        L2 = all("Z" in s for s in trio)
        iss = [n for n, b in (("L1", L1), ("L2", L2), ("L3", L3)) if b]
        n_tot += 1
        if not iss: n_trou += 1
        if len(iss) > 1:
            n_chev += 1; ex_issue.setdefault(" et ".join(iss), [sorted(s) for s in trio])
    res[lecture] = {"combinaisons": 2 ** 9, "sans_etat": len(trous), "exemples_sans_etat": trous[:3], "a_plusieurs_etats": chev,
                    "chevauchements": paires, "exemples": ex, "issues": {"configurations_de_trois_sondes": n_tot, "sans_issue": n_trou,
                                                                            "a_plusieurs_issues": n_chev, "exemples": ex_issue}}
# sonde illisible : aucun etat
res["sonde_illisible"] = {"etat_dans_le_texte_scelle_8e432cdc": "E (aucune sonde lue n'est lisible a cette condition) -> ligne L4",
                          "etat_dans_le_brouillon": None,
                          "issue_du_brouillon_si_une_sonde_est_illisible_et_deux_sont_Z": "aucune : L2 exige « les 3 sondes en etat Z », L3 exige N-scalaire, N ou J, L1 exige U ; L5 ne vise que l'essai de chaine et les « gardes techniques bloquantes », non definies"}
res["ordre_de_lecture"] = "le brouillon n'ecrit ni « dans cet ordre » ni « la premiere ligne qui s'applique » ; les textes scelles 19dbc99e... (l. 115) et 8e432cdc... l'ecrivent"
print(json.dumps(res, ensure_ascii=False, indent=1))
