"""Lanceur v11c, dérivé du lanceur v11b (`a6f64e79…`) par remplacements exacts comptés (corrections de la contre-lecture du
lanceur v11b, `contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`, demandées par la mère).
Usage : python3 faire_v11c.py RACINE SHA_CONF_V11C SHA_COMMANDE_V2 SHA_SONDE_COMMUNE_V3"""
import hashlib
import sys
from pathlib import Path

racine, SHA_CONF, SHA_CMD, SHA_SONDE = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]


def r(src, a, b, n=1):
    k = src.count(a)
    assert k == n, (k, n, a[:120])
    return src.replace(a, b)


src = (racine / "scripts/lancer_course_affinage_mentors_v11b.py").read_text(encoding="utf-8")
assert hashlib.sha256(src.encode("utf-8")).hexdigest() == "a6f64e79ef1f6e480b0b64ebd04a9643d63ee1833f455bb961cd38bf329c7b1a"

# --- en-tête ------------------------------------------------------------------------------------------------------------------
src = r(src, '#!/usr/bin/env python3\n"""Lanceur v11b (dérivé du lanceur v11,', '''#!/usr/bin/env python3
"""Lanceur v11c (dérivé du lanceur v11b, `a6f64e79…`, par remplacements exacts ; v11 et v11b restent en place, R12).

Ce qui change en v11c (contre-lecture du lanceur v11b, `course-v11/contre-lecture-lanceur-v11b-v1.md`, `cd7e5455…`,
« Scellable après corrections » ; corrections demandées par la mère ; numéros des constats de la contre-lecture) :
1. prix par appel d'Argon du devis interne à 4 / 20 USD par million (constantes nommées, que Fable recalculera aux réglages
   réels) et prix d'un appel de Carbon exact (0,480472) : base de l'écart au devis = 35,683 USD pour cinq espèces, celle du
   texte (calcul du devis v11b) ;
3. ligne de la clé LUC au relevé des crédits exigée : `solde_non_lu` vrai et `reference` = GO-2026-11-22-124, aucun champ de
   solde, de crédit, de reste, de couverture, de réserve ni de recharge ; sinon refus ;
4. libellé exigé de la contre-lecture du préenregistrement : « Opus 5.5, contre-lecteur neuf » ;
5. relecture finale de l'état et du journal du relais Claude après l'arrêt de l'orchestrateur : un refus lu alors vaut le
   code 5 et l'alerte ;
6. chaque lecture du relais Claude écrite au journal du run (`journal-part-claude-au-fil-de-l-eau.jsonl`, scellé à la fin) ;
   compte des appels par statut, dépassement et réserve lus dans l'état, au manifeste de fin ;
7. déclencheurs gardés (tout 4xx sauf 429 au journal, `refus` > 0, part engagée au plafond, lectures illisibles), mais
   l'alerte écrit la nature, le statut et la cause réels (motif du relais quand la ligne en porte un) ;
8. réserve par appel du relais Claude lue au départ (arguments par PID, s'ils la donnent, et état) et écrite au manifeste ;
   constante inutilisée retirée ;
9. sonde d'Astra commune v3 (`scripts/sonde_astra_courses_v3.py`) : variable de clé du relais jeté contrôlée ;
10. plafond de session des juges exigé égal à 1,00 USD ;
11. garde Google rejouée sur la plus longue entrée de chaque rôle ; entrée de juge de la forme de l'orchestrateur
    (`fiches_v54.entree_une_fiche` : consigne, « ## La fiche », fiche JSON) ;
12. commande Gemini en flux v2 (`scripts/commande_gemini_flux_v2.py`) : hypothèse « réflexion comprise dans la sortie
    maximale » vérifiée après chaque réponse ;
15. « haut » de la part Claude retiré du manifeste ; GO-2026-11-22-124 : le montant « part Claude 45 USD » lu au plafond, égal à
    45 (plus de sous-chaîne).

Texte du lanceur v11b :

Lanceur v11b (dérivé du lanceur v11,''')
src = r(src, 'VERSION = "lancer_course_affinage_mentors_v11b"', 'VERSION = "lancer_course_affinage_mentors_v11c"')
src = r(src, '"configuration": (f"{COURSE}/configuration-course-affinage-mentors-v11b.json", "c69620daa06a9c39b129038788ebdfd7f6530123d9726674ee14a3244f4795f2"),',
        f'"configuration": (f"{{COURSE}}/configuration-course-affinage-mentors-v11c.json", "{SHA_CONF}"),')

# --- 12 : commande en flux v2 ; 9 : sonde commune v3 -----------------------------------------------------------------------
src = r(src, '"carbon": {"commande_gemini_flux_v1.py": "6aaf235df31eccd7199c0bcea1e8b68009d56d03c66a01427d05ae8137fdbf55"}}',
        f'"carbon": {{"commande_gemini_flux_v2.py": "{SHA_CMD}"}}}}  # v11c : commande en flux v2 (constat 12)')
src = r(src, '"commande_carbon": ("scripts/commande_gemini_flux_v1.py", "6aaf235df31eccd7199c0bcea1e8b68009d56d03c66a01427d05ae8137fdbf55"),',
        f'"commande_carbon": ("scripts/commande_gemini_flux_v2.py", "{SHA_CMD}"),')
src = r(src, 'VERSION_SONDE_COMMUNE = "sonde_astra_courses_v2"', 'VERSION_SONDE_COMMUNE = "sonde_astra_courses_v3"\n'
        'VARIABLE_CLE_SONDE_ASTRA = "OPENAI_API_KEY_2"  # v11c, constat 9 : clé du relais jeté, contrôlée par la sonde commune v3')
src = r(src, '"sonde_commune": ("scripts/sonde_astra_courses_v2.py", "80074c82c8ea79d059c9f74b3ae89f7f50635283672a4bd26f1c2e77c27d6704"),',
        f'"sonde_commune": ("scripts/sonde_astra_courses_v3.py", "{SHA_SONDE}"),')
src = r(src, '''    if rj.get("programme_sha256") != PROGRAMMES_RELAIS["astra"][1] or rj.get("max_appels") != 1 \\''',
        '''    if rj.get("variable_cle") != VARIABLE_CLE_SONDE_ASTRA:  # v11c, constat 9
        ecarts.append(f"variable de clé du relais jeté {rj.get('variable_cle')!r}, {VARIABLE_CLE_SONDE_ASTRA} exigée")
    if rj.get("programme_sha256") != PROGRAMMES_RELAIS["astra"][1] or rj.get("max_appels") != 1 \\''')

# --- 1 : devis interne ---------------------------------------------------------------------------------------------------------
src = r(src, '''DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": 0.276, "prop-kimi": 0.276, "prop-astra": 0.276,
                      "prop-carbon": 0.4805, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}''',
'''# v11c (constat 1) : Argon ramené de 8,3 / 41,5 à 4 / 20 USD par million (postes mesurés du devis v6 × 20 / 41,5, comme le
# calcul du devis v11b, `calcul-devis-course-affinage-mentors-v11b.py`) ; constantes nommées, que Fable recalculera aux réglages
# réels ; Carbon au prix exact d'un appel estimé (2 618 × 4 + 23 500 × 20, par million = 0,480472) : base 35,683 (cinq espèces).
PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD = round(0.276 * 20 / 41.5, 6)   # 0,133012
PRIX_ARGON_JUGE_PAR_APPEL_USD = round(0.0347 * 20 / 41.5, 6)       # 0,016723
PRIX_CARBON_PAR_APPEL_USD = round((2618 * 4 + (20000 + 3500) * 20) / 1e6, 6)  # 0,480472
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": PRIX_ARGON_PROPOSEUR_PAR_APPEL_USD, "prop-kimi": 0.276,
                      "prop-astra": 0.276, "prop-carbon": PRIX_CARBON_PAR_APPEL_USD, "aiguilleur": 0.031, "juge-opus": 0.037,
                      "juge-argon": PRIX_ARGON_JUGE_PAR_APPEL_USD}''')
src = r(src, '''DEVIS_V5_TOTAL = {"cinq_especes": 40.848, "six_especes": 48.5504}  # v11 (R-5018) : + 16 × (0,4805 − 0,4985) = − 0,288''',
        '''DEVIS_V5_TOTAL = {"cinq_especes": 35.683424, "six_especes": 42.81056}  # v11c : base du texte (35,683 pour cinq espèces)''')

# --- 15 et 8 : haut retiré ; constante de réserve retirée --------------------------------------------------------------------
src = r(src, '''# v11 : part Claude estimée et haut du devis v10 (deux proposeurs, aiguilleur, premier juge ; marge comprise ; table du § 4) :
# écrits au manifeste pour information ; GO-2026-11-22-124 : aucune condition de départ sur le solde de LUC.
PART_CLAUDE_ESTIMEE_USD = 20.65
PART_CLAUDE_HAUT_USD = 74.62
''', '''# v11 : part Claude estimée (deux proposeurs, aiguilleur, premier juge ; marge comprise) : écrite au manifeste pour information ;
# GO-2026-11-22-124 : aucune condition de départ sur le solde de LUC. v11c (constat 15) : aucun « haut ».
PART_CLAUDE_ESTIMEE_USD = 20.65
''')
src = r(src, '''RESERVE_APPEL_CLAUDE_USD = 0.40  # réserve par appel par défaut du relais Claude (procédure neutre, § 2.1)
''', '''LIBELLE_CONTRE_LECTURE = "Opus 5.5, contre-lecteur neuf"  # v11c, constat 4 : libellé exigé (le texte écrit le même)
JUGE_PLAFOND_EXIGE_USD = 1.00  # v11c, constat 10 : plafond de session des juges exigé égal à 1,00 USD
PART_CLAUDE_GO_124_USD = 45.0  # v11c, constat 15 : montant écrit au plafond de GO-2026-11-22-124 (« part Claude 45 USD »)
''')
src = r(src, '''                       "part_estimee_usd": PART_CLAUDE_ESTIMEE_USD, "part_haut_usd": PART_CLAUDE_HAUT_USD,''',
        '''                       "part_estimee_usd": PART_CLAUDE_ESTIMEE_USD,''')

# --- 15 : montant 45 lu dans GO-124 ---------------------------------------------------------------------------------------------
src = r(src, '''    if GO_EXCEPTION_CLE not in perimetre or "45" not in plafond + perimetre:
        raise Refus(f"{go_id} : le périmètre doit nommer {GO_EXCEPTION_CLE} (prolongée) et le plafond de la part Claude (45 USD)")''',
'''    m45 = re.search(r"part Claude\\s+(\\d+(?:[.,]\\d+)?)\\s*USD", plafond)  # v11c, constat 15 : le montant lu, pas une sous-chaîne
    if GO_EXCEPTION_CLE not in perimetre or not m45 or float(m45.group(1).replace(",", ".")) != PART_CLAUDE_GO_124_USD:
        raise Refus(f"{go_id} : le périmètre doit nommer {GO_EXCEPTION_CLE} (prolongée) et le plafond, « part Claude 45 USD » "
                    f"(lu : {m45.group(0) if m45 else 'aucun montant'!r})")''')

# --- 4 : libellé de la contre-lecture -----------------------------------------------------------------------------------------
src = r(src, '''    if "modele k" not in _normaliser(texte):
        raise Refus("la contre-lecture ne dit pas être du modèle K (contre-lecteur attendu)")''',
        '''    if _normaliser(LIBELLE_CONTRE_LECTURE) not in _normaliser(texte):  # v11c, constat 4
        raise Refus(f"la contre-lecture ne porte pas le libellé « {LIBELLE_CONTRE_LECTURE} » (contre-lecteur attendu, v11)")''')
src = r(src, '''    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI par le modèle K (aucune valeur réelle)\\n\\nPréenregistrement lu : {prereg_sha}\\n"''',
        '''    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI, {LIBELLE_CONTRE_LECTURE} (aucune valeur réelle)\\n\\nPréenregistrement lu : {prereg_sha}\\n"''')

# --- 10 : plafond des juges égal à 1,00 -------------------------------------------------------------------------------------------
src = r(src, '''    if v is None:
        return {"plafond_session_juge_usd": avant, "emplacement": None, "statut": "en attente du mot de la mère"}
    if not _nombre(v) or not 0 < float(v) <= float(fixe["plafonds_session"]["proposeur"]):
        raise Refus(f"configuration : argon_v11.plafond_session_juge_usd = {v!r} : réel dans ]0 ; plafond d'un proposeur] exigé")''',
'''    if not _nombre(v) or float(v) != JUGE_PLAFOND_EXIGE_USD:  # v11c, constat 10 : égalité exigée (vide compris : refus)
        raise Refus(f"configuration : argon_v11.plafond_session_juge_usd = {v!r} : {JUGE_PLAFOND_EXIGE_USD:.2f} USD exactement "
                    "exigé (devis v11, texte v11)")''')

# --- 3 : ligne de LUC au relevé des crédits ------------------------------------------------------------------------------------
src = r(src, '''        if nom == CLE_CLAUDE:  # v11 (GO-2026-11-22-124) : solde non lu, aucune condition de départ sur la clé Claude
            sortie[nom] = {''', '''        if nom == CLE_CLAUDE:  # v11 (GO-2026-11-22-124) : solde non lu, aucune condition de départ sur la clé Claude
            verifier_ligne_luc(x)  # v11c, constat 3 : l'entrée « solde non lu, GO-2026-11-22-124 » est exigée, sans montant
            sortie[nom] = {''')
src = r(src, '''def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict | None = None) -> dict:''',
'''REFERENCE_LUC_SANS_SOLDE = "GO-2026-11-22-124"
CHAMPS_LUC_PERMIS = ("solde_non_lu", "reference", "source", "note")
MOTS_DE_MONTANT = ("solde", "credit", "reste", "couverture", "reserve", "recharge", "plancher", "usd", "eur", "montant")


def verifier_ligne_luc(x) -> dict:
    """v11c (constat 3 ; brouillon 3, « Règle des clés », point 1) : l'entrée de la clé LUC au relevé des crédits est exigée ;
    elle porte `solde_non_lu` = vrai et `reference` = GO-2026-11-22-124 ; elle ne porte aucun montant (aucun champ de solde, de
    crédit, de reste, de couverture, de réserve, de recharge ni de plancher) ; champs permis : `solde_non_lu`, `reference`,
    `source`, `note`. Toute autre forme : refus (aucun repli)."""
    if not isinstance(x, dict):
        raise Refus(f"relevé des crédits : entrée de la clé {CLE_CLAUDE} absente — « solde non lu » avec "
                    f"{REFERENCE_LUC_SANS_SOLDE} s'écrit, il ne s'omet pas")
    if x.get("solde_non_lu") is not True or x.get("reference") != REFERENCE_LUC_SANS_SOLDE:
        raise Refus(f"relevé des crédits : clé {CLE_CLAUDE} : « solde_non_lu » vrai et « reference » = {REFERENCE_LUC_SANS_SOLDE} "
                    f"exigés (lus : {x.get('solde_non_lu')!r}, {x.get('reference')!r})")
    montants = sorted(k for k in x if k != "solde_non_lu" and any(m in _normaliser(k) for m in MOTS_DE_MONTANT))
    autres = sorted(k for k in x if k not in CHAMPS_LUC_PERMIS)
    if montants or autres:
        raise Refus(f"relevé des crédits : clé {CLE_CLAUDE} : champ(s) {sorted(set(montants) | set(autres))} refusé(s) : la ligne ne "
                    "porte ni solde, ni crédit, ni reste, ni couverture, ni réserve (GO-2026-11-22-124)")
    return x


def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict | None = None) -> dict:''')

# --- 11 : entrée de juge de la forme de l'orchestrateur ; plus longue entrée de chaque rôle ------------------------------------
src = r(src, '''def controler_pire_cas_argon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:''',
'''def entree_juge_la_plus_longue(consigne_juge: str) -> str:
    """v11c (constat 11) : entrée d'un juge de la forme que bâtit l'orchestrateur épinglé (`pole/fiches_v54.py`,
    `entree_une_fiche`, l. 59 : consigne figée, « ## La fiche », fiche JSON indentée), pour la carte la plus longue que la consigne
    du proposeur permet (9 000 caractères) et 1 000 caractères de cadre de fiche (SUPPOSÉ : identifiant servi, champs) ;
    caractères non ASCII, comme le texte des cartes."""
    fiche = {"identifiant": "F" + "x" * 5, "carte": "é" * CARACTERES_PAR_CARTE_MAX, "cadre": "é" * 1000}
    corps = json.dumps(fiche, ensure_ascii=False, indent=1)
    return consigne_juge.rstrip() + "\\n\\n## La fiche\\n```json\\n" + corps + "\\n```\\n"


def controler_pire_cas_argon(decl: dict, fixe: dict, liste: dict, pieces: dict) -> dict | None:''')
src = r(src, '''                  "juge": len(consigne_j) + CARACTERES_PAR_CARTE_MAX + 1000}''',
        '''                  "juge": len(entree_juge_la_plus_longue(consigne_j))}  # v11c : forme de l'orchestrateur''')
src = r(src, '''    plus_long = max((texte_de_case(f) for f in liste["fils"]), key=len)''',
'''    consigne_p_texte = Path(pieces["consigne_proposeur"]["absolu"]).read_text(encoding="utf-8")
    consigne_j_texte = Path(pieces["consigne_juge"]["absolu"]).read_text(encoding="utf-8")
    # v11c (constat 11) : la plus longue entrée de chaque rôle : proposeur, consigne servie de la case la plus longue ; juge,
    # entrée de la forme de l'orchestrateur pour la carte la plus longue permise
    plus_longue = {"consigne_proposeur": max((consigne_servie_proposeur(consigne_p_texte, expurger(texte_de_case(f))[0])
                                              for f in liste["fils"]), key=len),
                   "consigne_juge": entree_juge_la_plus_longue(consigne_j_texte)}''')
src = r(src, '''            consigne = consigne_servie_proposeur(Path(pieces[consigne_piece]["absolu"]).read_text(encoding="utf-8"), plus_long)''',
        '''            consigne = plus_longue[consigne_piece]''')
src = r(src, '''            roles.append({"role": role_pole, "plafond_session_usd": fixe["plafonds_session"][role_plafond],''',
        '''            roles.append({"role": role_pole, "plafond_session_usd": fixe["plafonds_session"][role_plafond],
                          "entree_caracteres": len(consigne),''')

# --- 8 : réserve par appel du relais Claude -------------------------------------------------------------------------------------
src = r(src, '''        out["journal"] = journal
    egal_a_l_etat: dict = {}''', '''        out["journal"] = journal
    egal_a_l_etat: dict = {}
    if nom == "claude" and _valeur_arg(args, "--reserve-par-appel") is not None:  # v11c, constat 8 : lue par PID si donnée
        try:
            egal_a_l_etat["reserve_par_appel_usd"] = float(_valeur_arg(args, "--reserve-par-appel"))
        except ValueError:
            raise Refus("relais claude : --reserve-par-appel illisible") from None''')
src = r(src, '''        out["reserve_par_appel_usd"] = reserve
    out["etat_neuf"] = True''', '''        out["reserve_par_appel_usd"] = reserve
    if nom == "claude":  # v11c, constat 8 : réserve par appel lue dans l'état au départ, écrite au manifeste
        reserve = etat.get("reserve_par_appel_usd")
        if not (_nombre(reserve) and 0 <= reserve < float(out.get("plafond_usd") or 0)):
            raise Refus(f"relais claude : réserve par appel {reserve!r} USD illisible ou hors de [0, plafond du relais[ ; elle "
                        "borne le dépassement possible du plafond de la part Claude")
        out["reserve_par_appel_usd"] = reserve
        out["reserve_par_appel_source"] = "arguments lus par PID et état" if "reserve_par_appel_usd" in egal_a_l_etat \\
            else "état (défaut du programme épinglé, absent des arguments)"
        out["depassement_possible_par_appel_en_vol_usd"] = round(float(fixe["plafonds_session"]["proposeur"]) - reserve, 6) \\
            if fixe and _nombre((fixe.get("plafonds_session") or {}).get("proposeur")) else None
    out["etat_neuf"] = True''')

# --- 5, 6, 7 : surveillance --------------------------------------------------------------------------------------------------------
debut = src.index("class SurveillanceCleClaude:")
fin = src.index("# --- (6) orchestrateur ---")
src = src[:debut] + (Path(sys.argv[0]).resolve().parent / "surveillance_v11c.py").read_text(encoding="utf-8") + "\n\n" + src[fin:]
src = r(src, '''        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], plafond_luc, journal_claude)''',
        '''        surveillance = SurveillanceCleClaude(r, decl["fournisseurs"]["claude"]["url_relais"], plafond_luc, journal_claude,
                                             journal_run=dossier_run / JOURNAL_PART_CLAUDE)''')
src = r(src, '''    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident,''', '''    if surveillance is not None and arret_luc is None:  # v11c, constat 5 : relecture finale, après l'arrêt de l'orchestrateur
        try:
            arret_luc = surveillance.lecture_finale()
        except Exception as exc:  # noqa: BLE001 — jamais tu
            arret_luc = {"code": 5, "nature": "relecture finale impossible", "statut": None,
                         "cause": f"{type(exc).__name__}: {exc}", "motif": f"relecture finale du relais Claude impossible ({type(exc).__name__})"}
        if arret_luc:
            arret_luc = dict(arret_luc, moment="relecture finale, après l'arrêt de l'orchestrateur")
            print(json.dumps({"arret_cle_claude": arret_luc, "pid": pid}, ensure_ascii=False), file=sys.stderr, flush=True)
    journal_part = surveillance.sceller_journal() if surveillance is not None else None
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident,''')
src = r(src, '''             "cle_claude_au_fil_de_l_eau": dict(surveillance.bilan(), arret=arret_luc) if surveillance else {"moteur": "simulé"}}''',
        '''             "cle_claude_au_fil_de_l_eau": dict(surveillance.bilan(), arret=arret_luc, journal_du_run=journal_part)
             if surveillance else {"moteur": "simulé"}}''')
src = r(src, '''                      {"alerte": f"course arrêtée proprement sur la part Claude ({CLE_CLAUDE}) : premier refus du relais, plafond de "
                                 "la part atteint, ou part non comptable ; sans relance",
                       "code": arret_luc["code"], "motif": arret_luc["motif"], "bilan": surveillance.bilan(),''',
        '''                      {"alerte": f"course arrêtée proprement sur la part Claude ({CLE_CLAUDE}) : {arret_luc.get('nature')} ; "
                                 "sans relance",
                       "nature": arret_luc.get("nature"), "statut": arret_luc.get("statut"), "cause": arret_luc.get("cause"),
                       "moment": arret_luc.get("moment", "au fil de l'eau"),
                       "code": arret_luc["code"], "motif": arret_luc["motif"], "bilan": surveillance.bilan(),''')

(racine / "scripts/lancer_course_affinage_mentors_v11c.py").write_text(src, encoding="utf-8")
print("lanceur v11c :", len(src.splitlines()), "lignes")
