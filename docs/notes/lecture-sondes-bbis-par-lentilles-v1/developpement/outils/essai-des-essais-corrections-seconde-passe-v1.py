"""Essai des essais des corrections de la seconde passe (R5) : chaque garde neuve de `lanceur_seconde_passe_v2`, de
`nos_lentilles_v2` et de `phrases_v3` est défaite tour à tour dans une copie jetable du dépôt (paquet, essais et jouets copiés
hors du dépôt ; `prereg` et `docs` liés en lecture ; rien n'est écrit sous `src/` ni sous `tests/`), et les essais de
`tests/test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py` doivent tomber sur chaque copie défaite.

Les jouets de la copie calculent la fiche du code sur le paquet de la copie : une défaite ne fait donc pas tomber les essais
par la seule empreinte du module défait. Deux essais sont laissés de côté, qui comparent le lanceur à ce que l'outil de
fabrique rend à partir du lanceur v1 et tomberaient sur toute copie modifiée, sans rien prouver (`-k` ci-dessous).

Emploi (depuis la racine du dépôt, avec l'environnement Python du dépôt) :
    python docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/outils/essai-des-essais-corrections-seconde-passe-v1.py
Sortie : une ligne par défaite (« tombe » attendu partout), puis le compte ; code de retour 1 si une défaite passe inaperçue.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[5]
PAQUET = "src/controle_ia/lentilles_sondes_bbis"
ESSAIS = "test_lentilles_sondes_bbis_seconde_passe_corrections_v1.py"
HORS_FABRIQUE = "not outil_de_fabrique and not lignes_du_lanceur_v1"
DELAI_S = 1200
LANCEUR, LENTILLES, PHRASES = "lanceur_seconde_passe_v2.py", "nos_lentilles_v2.py", "phrases_v3.py"
DEFAITES = [
    # --- B1 ---------------------------------------------------------------------------------------------------------------------------
    ("B1 : lecture paginée du corpus hors de la liste des modules (le défaut d'origine)", LANCEUR,
     '"comparaisons_lentilles_v1", "reproduction_v1", "corpus_pagine_v1", "cache_tokeniseur_v2", "lanceur_v7",',
     '"comparaisons_lentilles_v1", "reproduction_v1", "cache_tokeniseur_v2", "lanceur_v7",'),
    ("B1 : cibles du corpus prises de montage_v1 (première page seule)", LANCEUR,
     "mo.essais_un_octet(transport, cle, cp.cibles_corpus(voisin, transport))",
     "mo.essais_un_octet(transport, cle, mo.cibles_corpus(voisin, transport))"),
    # --- B2 ---------------------------------------------------------------------------------------------------------------------------
    ("B2 : module du cache hors de la liste des modules", LANCEUR,
     '"comparaisons_lentilles_v1", "reproduction_v1", "corpus_pagine_v1", "cache_tokeniseur_v2", "lanceur_v7",',
     '"comparaisons_lentilles_v1", "reproduction_v1", "corpus_pagine_v1", "lanceur_v7",'),
    ("B2 : cache posé à l'ancienne, sans marqueur d'absence (le défaut d'origine)", LANCEUR,
     '    rapport["cache_du_tokeniseur"] = ct.poser_cache_tokeniseur(transport, cle, hf_home, poses, attendus, r.depot_llama,\n'
     "                                                               r.revision_llama)\n",
     '    rapport["cache_du_tokeniseur"] = mo.poser_cache_tokeniseur(hf_home, poses, r.depot_llama, r.revision_llama)\n'),
    ("B2 : essai en ligne et sans clé retiré", LANCEUR, "    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home, attendus)\n", ""),
    ("B2 : essai « en ligne » joué hors ligne", LANCEUR,
     "mo.environnement_enfant(voisin, hf_home, False, ctx.env)", "mo.environnement_enfant(voisin, hf_home, True, ctx.env)"),
    ("B2 : relecture du cache après un essai en ligne réussi retirée", LANCEUR,
     "    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home, attendus)\n    ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n",
     "    essayer_tokeniseur_en_ligne(ctx, voisin, hf_home, attendus)\n"),
    ("B2 : échec de l'essai en ligne avalé", LANCEUR,
     "    except Arret:\n        try:\n            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n",
     "    except Arret:\n        return\n        try:\n            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n"),
    ("B2 : cause non nommée à l'échec de l'essai en ligne", LANCEUR,
     '            cause = f"cause relue dans le cache : « {relecture} »"\n', "            cause = CAUSE_CACHE_INCHANGE\n"),
    ("B2 : cache dit inchangé sans être relu", LANCEUR,
     "            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n            cause = CAUSE_CACHE_INCHANGE\n",
     "            cause = CAUSE_CACHE_INCHANGE\n"),
    ("B2 : cause relue toujours annoncée, même quand le cache est inchangé", LANCEUR,
     "            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n            cause = CAUSE_CACHE_INCHANGE\n",
     "            ct.exiger_cache(hf_home, attendus, r.depot_llama, r.revision_llama)\n"
     '            cause = "cause relue dans le cache : « aucune »"\n'),
    # --- N5 ---------------------------------------------------------------------------------------------------------------------------
    ("N5 : modules neufs hors de la liste (nos_lentilles_v2)", LANCEUR,
     '"phrases_v3", "nos_lentilles_v1", "nos_lentilles_v2",', '"phrases_v3", "nos_lentilles_v1",'),
    ("N5 : condition de lecture de nos_lentilles_v1 seule", LANCEUR,
     "n2.condition_de_lecture(fiche, etat, ctx.racine_depot)", "nl.condition_de_lecture(fiche, etat, ctx.racine_depot)"),
    ("N5 : plusieurs lignes « Lentille nommée » acceptées", LENTILLES, "        if len(nommees) > 1:\n", "        if False:\n"),
    ("N5 : deux lignes acceptées, trois refusées", LENTILLES, "        if len(nommees) > 1:\n", "        if len(nommees) > 2:\n"),
    ("N5 : exigence jamais jouée", LENTILLES, "    if a_consulte_la_piece_du_noeud(conditions):\n", "    if False:\n"),
    ("N5 : exigence jouée même quand la pièce n'est pas consultée", LENTILLES,
     "    if a_consulte_la_piece_du_noeud(conditions):\n", "    if True:\n"),
    ("N5 : pièce non jugée quand la lentille consultée sort non lue", LENTILLES,
     "        if cond.phrase_sans_mesure or cond.motif == nl.NON_LUE.format(lettre=lettre, motif=nl.MOTIF_SANS_MESURE_PROPRE):\n",
     "        if cond.phrase_sans_mesure:\n"),
    ("N5 : pièce non jugée quand la lentille consultée sort lue", LENTILLES,
     "        if cond.phrase_sans_mesure or cond.motif == nl.NON_LUE.format(lettre=lettre, motif=nl.MOTIF_SANS_MESURE_PROPRE):\n",
     "        if cond.motif == nl.NON_LUE.format(lettre=lettre, motif=nl.MOTIF_SANS_MESURE_PROPRE):\n"),
    ("N5 : lignes du registre antérieures à l'avertissement jugées aussi", LENTILLES,
     "        if not (place > place_a and ligne.heure > heure_a):\n            continue\n", ""),
    # --- N2, N2 bis -------------------------------------------------------------------------------------------------------------------
    ("N2 : module neuf hors de la liste (phrases_v3)", LANCEUR, '"phrases_v2", "phrases_v3", "nos_lentilles_v1",', '"phrases_v2", "nos_lentilles_v1",'),
    ("N2 : ligne de la seconde course non recopiée pour une seule lentille au premier palier (le défaut d'origine)", PHRASES,
     "la décrivent.{suite} Réserves qui portent", "la décrivent. Réserves qui portent"),
    ("N2 : ligne de la seconde course non recopiée pour nos deux lentilles", PHRASES,
     "{p2.LIGNE_DE_V}.{suite} Réserves sur nos lentilles", "{p2.LIGNE_DE_V}. Réserves sur nos lentilles"),
    ("N2 bis : ligne recopiée de la fiche sans que la lecture soit inscrite (le défaut d'origine), dans les phrases", PHRASES,
     '    suite = SUITE_SECONDE_COURSE.format(ligne=ligne_de_la_seconde_course) if ligne_de_la_seconde_course else ""\n',
     '    ligne_de_la_seconde_course = (fiche.get("lecture_seconde_course") or {}).get("ligne_d_ensemble")\n'
     '    suite = SUITE_SECONDE_COURSE.format(ligne=ligne_de_la_seconde_course) if ligne_de_la_seconde_course else ""\n'),
    ("N2 bis : ligne recopiée de la fiche sans que la lecture soit inscrite, dans le lanceur", LANCEUR,
     '    ligne_seconde_course = _ligne_de_la_seconde_course(fiche, conditions["course"], etat_registre)\n',
     '    ligne_seconde_course = (fiche.get("lecture_seconde_course") or {}).get("ligne_d_ensemble")\n'),
    ("N2 : ligne relevée par le lanceur non donnée à la tête", LANCEUR,
     'issue["phrases_de_tete"], non_tenues, ligne_seconde_course)', 'issue["phrases_de_tete"], non_tenues, None)'),
    ("N2 : tête qui reprend le verdict d'ensemble de phrases_v2", PHRASES,
     '"verdict_d_ensemble": lignes_du_verdict_d_ensemble(conditions, fiche, course, ligne_de_la_seconde_course),',
     '"verdict_d_ensemble": p2.lignes_du_verdict_d_ensemble(conditions, fiche, course),'),
    ("N2 : refus d'une paraphrase interdite retiré du verdict d'ensemble", PHRASES,
     '    for ligne in lignes:\n        p2.exiger_sans_paraphrase_interdite(ligne["texte"])\n', ""),
    # --- N4 ---------------------------------------------------------------------------------------------------------------------------
    ("N4 : phrase gelée gardée pour une passe achevée depuis le montage (le défaut d'origine)", PHRASES,
     "        if montage == nl.PREMIERE_PASSE_NON_ACHEVEE and calcul == nl.PREMIERE_PASSE_ACHEVEE:\n", "        if False:\n"),
    ("N4 : phrase gelée gardée pour une passe lancée depuis le montage", PHRASES,
     "        if montage == nl.PREMIERE_PASSE_JAMAIS_LANCEE and calcul in (", "        if False and calcul in ("),
    ("N4 : note à la place de la phrase gelée quand rien n'a changé depuis le montage", PHRASES,
     "        if montage == nl.PREMIERE_PASSE_NON_ACHEVEE and calcul == nl.PREMIERE_PASSE_ACHEVEE:\n",
     "        if montage == nl.PREMIERE_PASSE_NON_ACHEVEE:\n"),
    ("N4 : note « lancée depuis » pour la seule passe achevée", PHRASES,
     "calcul in (nl.PREMIERE_PASSE_NON_ACHEVEE, nl.PREMIERE_PASSE_ACHEVEE):", "calcul == nl.PREMIERE_PASSE_ACHEVEE:"),
    ("N4 : tête qui reprend les phrases de la reproduction de phrases_v2", PHRASES,
     '"reproduction": phrases_de_la_reproduction(reproduction, modules_differents),',
     '"reproduction": p2.phrases_de_la_reproduction(reproduction, modules_differents),'),
    # --- N3 ---------------------------------------------------------------------------------------------------------------------------
    ("N3 : note jamais écrite (le défaut d'origine)", LANCEUR,
     '            if c["libelle"] in LIBELLES_QUI_CITENT_LES_MOITIES and e["moities"].get("libelle") == co.NON_CALCULABLE:\n',
     "            if False:\n"),
    ("N3 : note écrite pour tout libellé", LANCEUR,
     '            if c["libelle"] in LIBELLES_QUI_CITENT_LES_MOITIES and e["moities"].get("libelle") == co.NON_CALCULABLE:\n',
     '            if e["moities"].get("libelle") == co.NON_CALCULABLE:\n'),
    ("N3 : note écrite même quand le recouvrement des moitiés est calculable", LANCEUR,
     '            if c["libelle"] in LIBELLES_QUI_CITENT_LES_MOITIES and e["moities"].get("libelle") == co.NON_CALCULABLE:\n',
     '            if c["libelle"] in LIBELLES_QUI_CITENT_LES_MOITIES:\n'),
]


def preparer(d: Path) -> None:
    shutil.copytree(RACINE / "src", d / "src", ignore=shutil.ignore_patterns("__pycache__"))
    (d / "tests").mkdir()
    for f in (RACINE / "tests").glob("*lentilles_sondes_bbis_*.py"):
        shutil.copy(f, d / "tests")
    shutil.copy(RACINE / "pyproject.toml", d)
    os.symlink(RACINE / "prereg", d / "prereg")
    os.symlink(RACINE / "docs", d / "docs")                    # copies versées et outils lus par les essais (lecture seule)


def jouer(d: Path) -> bool:
    try:
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--rootdir", str(d),
                            "-k", HORS_FABRIQUE, str(d / "tests" / ESSAIS)], cwd=d, timeout=DELAI_S, capture_output=True, text=True,
                           env=os.environ | {"PYTHONPATH": f"{d / 'src'}:{d / 'tests'}", "PYTHONDONTWRITEBYTECODE": "1"})
    except subprocess.TimeoutExpired:
        return False
    return r.returncode == 0


inapercues = []
with tempfile.TemporaryDirectory() as tmp:
    d = Path(tmp) / "copie"
    preparer(d)
    origines = {m: (d / PAQUET / m).read_text(encoding="utf-8") for m in (LANCEUR, LENTILLES, PHRASES)}
    print("copie saine :", "passe" if jouer(d) else "TOMBE (inattendu)", flush=True)
    for nom, module, avant, apres in DEFAITES:
        assert origines[module].count(avant) == 1, (nom, origines[module].count(avant))
        (d / PAQUET / module).write_text(origines[module].replace(avant, apres), encoding="utf-8")
        passe = jouer(d)
        (d / PAQUET / module).write_text(origines[module], encoding="utf-8")
        print(f"{nom} :", "PASSE (défaite inaperçue)" if passe else "tombe", flush=True)
        if passe:
            inapercues.append(nom)
print(f"{len(DEFAITES)} défaites, {len(DEFAITES) - len(inapercues)} vues par les essais, {len(inapercues)} inaperçues")
sys.exit(1 if inapercues else 0)
