#!/usr/bin/env python3
"""Construction déterministe de la bibliothèque unifiée des idées, hypothèses et pistes (v1).

Rassemble, dédoublonne et classe selon quatre axes (Objet, Thème scientifique, Source/Modèle,
Régime matériel d'exécution) l'ensemble des idées, propositions, mécanismes et verrous produits
dans le dépôt et ses branches autorisées, sous filtrage strict de cloisonnement.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parents[4]
SORTIE = Path(__file__).resolve().parent

MOTIFS_INTERDITS = (
    "coffre/",
    "docs/verdicts/",
    "/verdict/",
    "verdict/",
    "reponses-ne-pas-servir",
    "protocole-x-attaquant-v1",
    "evasion-moniteurs",
    "modes-et-attaques",
    "modes-attaque",
    "modes-v8",
    "organismes-discrets",
    "lot-quarantaine",
    "taches-sabotage",
    "conscience-anesthesie-v3-reserve",
    "verite-dommage",
    "tableau-partage",
    "questions-fortes",
    "bras-attaque",
    "attaque-goodhart",
    "barreau8",
    "barreau5",
    "dose-reponse-consigne-cachee",
    "versant-honnete",
    "sondes-v2",
    "modes-attaque-reponse-24",
)


def est_interdit(chemin: str) -> bool:
    c = chemin.replace("\\", "/").lower()
    return any(m in c for m in MOTIFS_INTERDITS)


def gh_raw(branche: str, chemin: str) -> str:
    if est_interdit(chemin) or est_interdit(branche):
        raise ValueError(f"Chemin interdit refusé : {branche}:{chemin}")
    out = subprocess.check_output(
        [
            "gh",
            "api",
            "-H",
            "Accept: application/vnd.github.raw",
            f"repos/lciric/controle-ia-travail/contents/{chemin}?ref={branche}",
        ],
        text=True,
    )
    return out


def sha256_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def nettoyer(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip())


OBJETS = {
    "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT": (
        "1. Métrologie, attelage du Plan Turing, critères sans juge et tests de mort"
    ),
    "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION": (
        "2. Architecture de l'organisme d'idéation, mémoire, sélection et auto-conception"
    ),
    "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET": (
        "3. Mathématiques nouvelles, modèle à trois graphes, réification hors alphabet et Lean 4"
    ),
    "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES": (
        "4. Contrôle de l'intelligence artificielle, menaces diffuses, audit et sondes"
    ),
    "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B": (
        "5. Étalonnages empiriques sur corpus datés (PubTator 3, Gu et Krenn, cit-HepTh) et GPU 8B (dopamine H10, compression T4)"
    ),
}


def classer_entree(titre: str, enonce: str, source_chemin: str, famille_source: str) -> tuple[str, str, str]:
    """Retourne (objet, theme, regime_execution) de façon déterministe."""
    txt = f"{titre} {enonce} {source_chemin}".lower()

    # Statut déjà réfuté
    if "pas0-rang1-foyers-tension" in txt or ("foyers de tension" in txt and "0,1667" in txt):
        regime = "DEJA_REFUTE_OU_ECARTE"
    elif any(k in txt for k in ("dopamine", "h10", "neurones de récompense", "perte de prédiction", "8 milliards", "8b", "vast.ai", "carte graphique", "gpu")):
        regime = "GPU_VAST_8B_SOUS_GO"
    elif any(k in txt for k in ("pubtator", "gu et krenn", "scimuse", "cit-hepth", "openalex", "zbmath", "arxiv 2000", "semmeddb")):
        regime = "CPU_DONNEES_PUBLIQUES_REEL"
    else:
        regime = "CPU_0_USD_SYNTHETIQUE"

    # Objet + Thème
    if any(k in txt for k in ("pubtator", "gu et krenn", "scimuse", "cit-hepth", "dopamine", "h10", "préfixer une idée", "perte de prédiction")):
        objet = "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B"
        if "pubtator" in txt or "semmeddb" in txt:
            theme = "5A. Graphes biomédicaux datés et polarités causales (PubTator 3)"
        elif "gu et krenn" in txt or "scimuse" in txt:
            theme = "5B. Surface contre structure sur notes d'experts et graphe dynamique (Gu et Krenn 2026)"
        elif "dopamine" in txt or "h10" in txt or "perte de prédiction" in txt:
            theme = "5C. Signal interne d'erreur de prédiction (« dopamine » H10) et compression 8B sur GPU Vast.ai (T4)"
        else:
            theme = "5D. Rétrodictions sur archives scientifiques datées (cit-HepTh, OpenAlex, arXiv)"
        return objet, theme, regime

    if any(k in txt for k in (
        "hypergraphe", "hors de l'alphabet", "hors alphabet", "réification", "reification",
        "méta-mathématique", "meta-mathematique", "méta-espace", "meta-espace", "homomorphisme",
        "gromov-wasserstein", "modes propres", "laplacien", "faisceau", "holonomie", "scission",
        "macros latex", "algèbres amassées", "cluster algebras", "arbres d'équations", "stitch",
        "dreamcoder", "lean 4", "lean4", "mathlib", "lagrange", "gauss", "catégorie", "topos",
    )):
        objet = "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET"
        if any(k in txt for k in ("réification", "reification", "hors de l'alphabet", "hors alphabet", "lagrange", "méta-mathématique", "méta-espace")):
            theme = "3A. Sortie de l'alphabet, obstructions d'alignement et réification sur les trois graphes"
        elif any(k in txt for k in ("scission", "faisceau", "holonomie", "fausse identité", "identités tenues")):
            theme = "3B. Opérateur de scission conceptuelle et détection des faux amalgames"
        elif any(k in txt for k in ("macros", "stitch", "dreamcoder", "arbres d'équations", "longueur de description", "mdl", "compression")):
            theme = "3C. Compression inter-bassins (MDL / Stitch), macros et arbres d'opérateurs"
        elif any(k in txt for k in ("gromov-wasserstein", "modes propres", "spectr", "weisfeiler", "homomorphisme", "serrure")):
            theme = "3D. Recherche de correspondances en puits étroit (spectral, transport optimal, typage)"
        elif any(k in txt for k in ("lean", "mathlib", "preuve formelle", "théorème nu")):
            theme = "3E. Vérification formelle Lean 4 et cibles mathématiques ouvertes"
        else:
            theme = "3F. Hypergraphe fusionné à quatre couches et couche des problèmes ouverts"
        return objet, theme, regime

    if any(k in txt for k in (
        "sonde", "moniteur", "sabot", "contrôle diffus", "controle diffus", "audit", "pince",
        "écriture de poids", "programmation de poids", "adaptateur", "essaim", "collusion",
        "aléa partagé", "empoisonnement", "halberstadt", "évasion", "evasion", "marge asymétrique",
        "conscience", "anesthésie", "anesthesie", "porte g0", "porte g1", "papier a", "papier b", "papier d",
    )):
        objet = "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES"
        if any(k in txt for k in ("poids", "adaptateur", "halberstadt", "post-entraînement", "post-entrainement", "papier d")):
            theme = "4A. Dynamique d'entraînement, écriture de poids et tenue des garanties"
        elif any(k in txt for k in ("réapprendre", "empoisonnement", "sonde", "lentille", "boîte blanche", "marge")):
            theme = "4B. Sondes internes, lentilles et sas de réapprentissage sous adversaire"
        elif any(k in txt for k in ("essaim", "aléa partagé", "collusion", "papier b", "co-élévation")):
            theme = "4C. Surveillance d'essaims, copies à mêmes poids et aléa partagé"
        else:
            theme = "4D. Audit séquentiel, dommages plantés et architecture du contrôle diffus"
        return objet, theme, regime

    if any(k in txt for k in (
        "attelage", "borne de handicap", "clopper-pearson", "intersection-union", "canonicalisation",
        "témoin faux", "épreuve morte", "epreuve morte", "nomination scellée", "chasseur d'étroitesse",
        "divergence triviale", "brier", "juge au nul", "nul composite", "e-valeur", "thresholdout",
        "protocole x", "suivisme", "fausses découvertes", "prévalence",
    )):
        objet = "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT"
        if any(k in txt for k in ("handicap", "clopper", "étroitesse", "chasseur", "divergence triviale")):
            theme = "1A. Certification d'étroitesse, borne de handicap et contrôles actifs (CN-1, CN-2)"
        elif any(k in txt for k in ("témoin faux", "épreuve morte", "résolveur mécanique", "profondeur", "4 quadrants", "quatre quadrants")):
            theme = "1B. Profondeur par résolveur mécanique, micromondes plantés et tests de mort"
        elif any(k in txt for k in ("canonicalisation", "nomination", "intersection-union", "prévalence", "bayes")):
            theme = "1C. Canonicalisation, nomination scellée, intersection-union et calibration bayésienne"
        else:
            theme = "1D. Gouvernance expérimentale, neutralisation des juges et audit du Protocole X"
        return objet, theme, regime

    objet = "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION"
    if any(k in txt for k in ("auto-conception", "autoconception", "auto-modification", "se réécrire", "greffon", "anneau")):
        theme = "2A. Auto-conception, greffons d'architecture et porte transactionnelle"
    elif any(k in txt for k in ("mémoire", "memoire", "héritage", "heritage", "archive", "redite", "tentatives")):
        theme = "2B. Mémoire négative des morts, héritage inter-générations et contrôle 2x2"
    elif any(k in txt for k in ("cinétique", "cinetique", "arrhenius", "catalyseur", "percolation", "émergence", "protocelle", "parent")):
        theme = "2C. Cinétique des collisions d'idées, catalyse, percolation et recombinaison"
    elif any(k in txt for k in ("budget", "allocation", "bandit", "diversité", "puits étroit", "mélange défensif", "énumérateur")):
        theme = "2D. Allocation de budget, mélange défensif sans modèle et diversité fabriquée"
    else:
        theme = "2E. Topologie des rôles (cartographe, proposeurs, réfutateurs, expérimentateurs)"
    return objet, theme, regime


def parser_table_md(lignes: list[str]) -> list[list[str]]:
    rows = []
    for l in lignes:
        s = l.strip()
        if not s.startswith("|") or not s.endswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r"[-:\s]*", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def construire() -> None:
    entrees: list[dict] = []
    stats_sources: dict[str, int] = Counter()
    exclus_compteur = 0

    def ajouter(
        id_orig: str,
        titre: str,
        enonce: str,
        famille_source: str,
        espece_auteur: str,
        source_chemin: str,
        source_branche: str = "main",
        statut: str = "proposé",
    ) -> None:
        nonlocal exclus_compteur
        if est_interdit(source_chemin) or est_interdit(f"{titre} {enonce[:120]}"):
            exclus_compteur += 1
            return
        titre_n = nettoyer(titre)
        enonce_n = nettoyer(enonce)
        if not titre_n and not enonce_n:
            return
        if not titre_n:
            titre_n = enonce_n[:110]
        objet, theme, regime = classer_entree(titre_n, enonce_n, source_chemin, famille_source)
        cle_dedup = sha256_texte(f"{id_orig}|{titre_n[:120]}|{enonce_n[:240]}")[:16]
        entrees.append(
            {
                "id_unifie": f"BIB-{len(entrees)+1:04d}",
                "cle_contenu": cle_dedup,
                "id_origine": nettoyer(id_orig) or f"SRC-{len(entrees)+1}",
                "titre": titre_n[:260],
                "enonce": enonce_n[:1200],
                "objet": objet,
                "theme": theme,
                "famille_source": famille_source,
                "espece_auteur": nettoyer(espece_auteur) or "non_specifie",
                "source_chemin": source_chemin,
                "source_branche": source_branche,
                "statut": nettoyer(statut) or "proposé",
                "regime_execution": regime,
            }
        )
        stats_sources[famille_source] += 1

    # 1. Attelage du Plan Turing (U01..U31)
    p_att = RACINE / "docs/notes/collisionneur-v9/notes-de-sortie-v1/note-de-sortie-collisionneur-attelage-plan-turing-v1.md"
    for cells in parser_table_md(p_att.read_text(encoding="utf-8").splitlines()):
        if len(cells) >= 7 and cells[0].startswith("`U"):
            uid = cells[0].strip("`")
            ajouter(
                uid,
                cells[1],
                f"Accord lecteurs: {cells[4]} | Modèles: {cells[5]} | Fournisseurs: {cells[6]}",
                "S01_Collisionneur_Attelage_Plan_Turing",
                cells[5],
                str(p_att.relative_to(RACINE)),
                "main",
                cells[4],
            )

    # 2. Jeu des 361 propositions Protocole X / Collisionneurs (branche audit/protocole-x-v1)
    jp = json.loads(gh_raw("audit/protocole-x-v1", "docs/notes/audit-protocole-x-v1/sorties/jeu-des-propositions-v2.json"))
    for item in jp:
        src = item.get("note") or item.get("dossier") or "audit-protocole-x-v1"
        esp = ", ".join(item.get("especes_porteuses") or []) or "multi-modeles"
        ajouter(
            item.get("id", ""),
            item.get("texte", "")[:140],
            f"[{item.get('genre','')}/{item.get('nature','')}] {item.get('texte','')} (Dossier: {item.get('dossier','')})",
            "S02_Protocole_X_et_Notes_Collisionneurs_361_Propositions",
            esp,
            src,
            item.get("branche_note", "audit/protocole-x-v1"),
            f"{item.get('etat','')} ({item.get('sous_etat','')})",
        )

    # 3. Unités granulaires des 99 courses de collisionneurs (unites-v2.json : T1 et T3 + premières expériences)
    un = json.loads(gh_raw("audit/protocole-x-v1", "docs/notes/audit-protocole-x-v1/sorties/unites-v2.json"))
    for u in un.get("unites", []):
        ajouter(
            u.get("id", ""),
            f"[{u.get('racine','')} | T{u.get('tour','')} | {u.get('espece','')}] {u.get('titre','')}",
            u.get("extrait", ""),
            "S03_Cellules_Brutes_99_Collisionneurs_Unites",
            f"{u.get('espece','')} ({u.get('fournisseur','')}, tour {u.get('tour','')})",
            u.get("chemin", ""),
            "audit/protocole-x-v1",
            "extrait_cellule_brute",
        )
    for pr in un.get("premiers", []):
        ajouter(
            f"PREM-{pr.get('racine','')}-{pr.get('lettre','')}-T{pr.get('tour','')}",
            f"Première expérience proposée [{pr.get('racine','')} | {pr.get('espece','')}]",
            pr.get("texte", ""),
            "S03_Cellules_Brutes_99_Collisionneurs_Premieres_Experiences",
            pr.get("espece", ""),
            pr.get("chemin", ""),
            "audit/protocole-x-v1",
            "premiere_experience_proposee",
        )

    # 4. Journal horodaté de la Veille de cap (4 parties JSONL sur main) + 2 transmissions sur claude/veille-de-cap-v1
    par_fiche: dict[str, dict] = {}
    for jf in sorted((RACINE / "registres/veille-de-cap").glob("journal-des-idees-v1*.jsonl")):
        for line in jf.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            ev = json.loads(line)
            fid = ev.get("fiche") or ev.get("id") or ""
            if not fid:
                continue
            cur = par_fiche.setdefault(fid, {"fiche": fid, "nom": "", "etat": "", "source": "", "porteur": "", "notes": [], "fichier": str(jf.relative_to(RACINE))})
            if ev.get("nom"):
                cur["nom"] = ev["nom"]
            if ev.get("etat"):
                cur["etat"] = ev["etat"]
            if ev.get("porteur"):
                cur["porteur"] = str(ev["porteur"])
            src_ev = ev.get("source")
            if isinstance(src_ev, dict) and src_ev.get("chemin"):
                cur["source"] = src_ev["chemin"]
            elif isinstance(src_ev, str) and src_ev:
                cur["source"] = src_ev
            for k in ("sert", "note", "raison", "issue"):
                if ev.get(k):
                    cur["notes"].append(f"{k}: {ev[k]}")
    for fid, info in sorted(par_fiche.items()):
        ajouter(
            fid,
            info["nom"] or fid,
            " ; ".join(info["notes"]) or info["nom"],
            "S04_Veille_de_Cap_Journal_JSONL",
            info["porteur"] or "veille-de-cap",
            info["source"] or info["fichier"],
            "main",
            info["etat"] or "consignée",
        )

    for rp in (
        "docs/notes/veille-de-cap-v1/transmissions/transmission-registre-pistes-octobre-v2.md",
        "docs/notes/veille-de-cap-v1/transmissions/transmission-registre-organisme-et-plan-turing-v1.md",
    ):
        txt = gh_raw("claude/veille-de-cap-v1", rp)
        for cells in parser_table_md(txt.splitlines()):
            if len(cells) >= 5 and cells[0].lower() not in ("fiche", "id", "n°"):
                ajouter(
                    cells[0],
                    cells[2] if len(cells) >= 6 else cells[1],
                    " | ".join(cells[1:]),
                    "S04_Veille_de_Cap_Transmissions_Octobre_et_Turing",
                    "veille-de-cap",
                    rp,
                    "claude/veille-de-cap-v1",
                    cells[4] if len(cells) >= 6 else cells[3],
                )

    # 5. Bibliothécaire du 23 novembre (registre-idees-pistes-v1.md)
    p_bib = RACINE / "registres/bibliotheque/session-mere-2026-11-23/registre-idees-pistes-v1.md"
    for cells in parser_table_md(p_bib.read_text(encoding="utf-8").splitlines()):
        if len(cells) >= 7 and re.match(r"^I-\d+", cells[0]):
            ajouter(
                cells[0],
                cells[3][:160],
                f"{cells[3]} | Piste organisme: {cells[6]} | Pourquoi: {cells[-1]}",
                "S05_Bibliothecaire_Registre_Idees_Pistes",
                cells[4],
                str(p_bib.relative_to(RACINE)),
                "main",
                cells[5],
            )

    # 6. Registre des 62 idées du 23 novembre (naissance des idées fécondes)
    p_lot8 = RACINE / "docs/notes/idee-interessante-v1/lot-8/registre-idees-session-2026-11-23-v1.md"
    for cells in parser_table_md(p_lot8.read_text(encoding="utf-8").splitlines()):
        if len(cells) >= 7 and cells[0].startswith("IDE-"):
            ajouter(
                cells[0],
                cells[3],
                f"[{cells[2]} | Origine: {cells[1]} | Score: {cells[5]}] {cells[6]}",
                "S06_Registre_62_Idees_Naissance_Idees_Fecondes",
                cells[1],
                str(p_lot8.relative_to(RACINE)),
                "main",
                cells[4],
            )

    # 7. Inventaire des pistes du Plan Turing (15 oct - 24 nov)
    p_inv_tur = RACINE / "docs/notes/inventaire-plan-turing-v1/inventaire-pistes-plan-turing-depuis-23-novembre-v1.md"
    lignes_tur = p_inv_tur.read_text(encoding="utf-8").splitlines()
    for cells in parser_table_md(lignes_tur):
        if len(cells) >= 9 and re.match(r"^[PO]\d+$", cells[0]):
            ajouter(
                f"TUR-PIECE-{cells[0]}",
                cells[1],
                f"[{cells[7]}] {cells[8]} (Chemin origine: {cells[2]} sur {cells[3]})",
                "S07_Inventaire_Plan_Turing_101_Pieces",
                cells[7],
                cells[2].strip("`"),
                cells[3].strip("`"),
                "répertoriée",
            )
        elif len(cells) in (4, 5) and cells[0].lower() not in ("piste", "n°", "tâche", "script", "mesure", "devenir des 130 propositions retenues"):
            ajouter(
                f"TUR-PISTE-{sha256_texte(cells[0])[:8]}",
                cells[0],
                f"{cells[1]} | Source: {cells[2]}" + (f" | Épreuve: {cells[4]}" if len(cells) == 5 else ""),
                "S07_Inventaire_Plan_Turing_Catalogue_Pistes",
                cells[2],
                str(p_inv_tur.relative_to(RACINE)),
                "main",
                cells[3],
            )

    # 8. Inventaire des ~360 idées de l'organisme (10 familles)
    p_inv7 = RACINE / "docs/notes/rapports-directeur/programme-organisme-complet-v1/inventaire-idees-organisme-v7.md"
    for cells in parser_table_md(p_inv7.read_text(encoding="utf-8").splitlines()):
        if len(cells) >= 6 and re.match(r"^[A-Z]{2,4}-\d{3}$", cells[0]):
            ajouter(
                cells[0],
                cells[1][:160],
                f"[{cells[2]}] {cells[1]} (Source: {cells[5]})",
                "S08_Inventaire_Organisme_Complet_v7_10_Familles",
                cells[3],
                str(p_inv7.relative_to(RACINE)),
                "main",
                cells[4],
            )

    # 9. Matière première structurée de l'auto-conception (21 lots JSON)
    for lf in sorted((RACINE / "docs/notes/matiere-premiere-auto-conception-v1/lots").glob("lot-*.json")):
        items = json.loads(lf.read_text(encoding="utf-8"))
        for it in items:
            mecs = it.get("mecanismes") or []
            if isinstance(mecs, list) and mecs:
                for idx_m, m in enumerate(mecs, 1):
                    m_txt = json.dumps(m, ensure_ascii=False) if isinstance(m, dict) else str(m)
                    nom_m = m.get("nom") or m.get("mecanisme") or m.get("titre") or it.get("titre", "") if isinstance(m, dict) else it.get("titre", "")
                    ajouter(
                        f"MP-{lf.stem}-{it.get('indice',0)}-{idx_m}",
                        f"{it.get('titre','')} — {nom_m}",
                        m_txt,
                        "S09_Matiere_Premiere_Auto_Conception_21_Lots",
                        str(it.get("nature", "littérature_et_interne")),
                        str(lf.relative_to(RACINE)),
                        "main",
                        str(it.get("mesure_selon_la_table", "à_éprouver")),
                    )

    # 10. Catalogue des 18 verrous mathématiques canoniques
    p_ver = RACINE / "docs/notes/cartographie-mathematiques-ouvertes-v1/catalogue-verrous-v1.json"
    cv = json.loads(p_ver.read_text(encoding="utf-8"))
    for v in cv.get("fiches_maitresses", []):
        ajouter(
            v.get("id", ""),
            f"{v.get('titre','')} ({v.get('famille','')})",
            f"Énoncé: {v.get('enonce_formel_canonique','')} | Noyau ouvert: {v.get('noyau_mathematique_ouvert','')} | Test de mort miniature: {json.dumps(v.get('miniature_test_de_mort',''), ensure_ascii=False)}",
            "S10_Cartographie_18_Verrous_Mathematiques",
            "cartographie-verrous-v1",
            str(p_ver.relative_to(RACINE)),
            "main",
            "test_de_mort_défini",
        )

    # 11. Réponses directes de Fable en amont / hors collisionneur, Opus max, Google (Carbon/Neon/Argon), Astra, Kimi & Dossiers Protocole X
    fichiers_directs_locaux: list[tuple[str, str]] = [
        ("Fable 5.2 (avis organisme)", "docs/notes/avis-fable-organisme-ideation-v1/avis-fable-organisme-ideation-v1.md"),
        ("Fable 5.2 effort max (idée intéressante)", "docs/notes/idee-interessante-v1/reponse-fable-max-v1.md"),
        ("Opus 5.5 effort max (idée intéressante)", "docs/notes/idee-interessante-v1/reponse-opus-max-v1.md"),
        ("Carbon (idée intéressante)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-v1.md"),
        ("Carbon (méta-espace mathématique)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-meta-espace-v1.md"),
        ("Carbon (homomorphisme de graphes)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-homomorphisme-v1.md"),
        ("Neon (idée intéressante)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-neon-v1.md"),
        ("Neon (homomorphisme hypergraphes)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-neon-homomorphisme-v1.md"),
        ("Argon (idée intéressante)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-argon-v1.md"),
        ("Argon (homomorphisme)", "docs/notes/idee-interessante-v1/reponses-google-v1/reponse-argon-homomorphisme-v1.md"),
        ("Fable 5.2 (demande 28 puits étroits)", "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-28-effort-max/relecture-fable-api.md"),
        ("Opus 5.5 (demande 28 puits étroits)", "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-28-opus55-max/reponse-opus55-v1.md"),
        ("Fable 5.2 (demande 40 méthodes math)", "docs/notes/demandes-fable-api-2026-11-22-v1/reponse-40/relecture-fable-api.md"),
        ("Protocole X synthèse puits étroits", "docs/notes/demandes-fable-api-2026-11-22-v1/synthese-protocole-x-puits-etroits-v2.md"),
        ("Carbon amont Protocole X (boucle organisme-contrôle)", "docs/notes/protocole-x-boucle-organisme-controle-v1/reponse-approfondie-carbon-boucle-organisme-controle-v1.md"),
        ("Fable amont Protocole X (dommages plantés tiers)", "docs/notes/protocole-x-dommages-plantes-tiers-v1/reponse-fable-dommages-plantes-tiers-v2.md"),
        ("Fable amont Protocole X (dommage)", "docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md"),
        ("Fable amont Protocole X (marge asymétrique)", "docs/notes/protocole-x-marge-asymetrique-v1/reponse-fable-marge-asymetrique-v2.md"),
        ("Fable amont Protocole X (programmation de poids)", "docs/notes/protocole-x-programmation-de-poids-v1/reponse-fable-programmation-de-poids-v2.md"),
        ("Protocole X (structure du langage)", "docs/notes/protocole-x-structure-du-langage-v1/synthese-structure-du-langage-v1.md"),
        ("Fable amont Protocole X (dynamique papier D)", "docs/notes/dynamique-papier-d-protocole-x-v1/demande-approfondie-dynamique-papier-d-fable-v1.md"),
        ("Fable (conception banc lois plantées v2)", "docs/notes/banc-lois-plantees-c2-v1/conception-fable-banc-lois-plantees-v2.md"),
        ("Cahier v3 des 10+4 mondes plantés du contrôle", "docs/notes/plan-turing-processeur-v1/cahier-des-charges-banc-mondes-plantes-verrous-controle-v3.md"),
        ("Argon et Kimi espèces seules (sélection générations)", "docs/notes/reponses-especes-seules-2026-11-01-v1/lecture-verifiee-selection-generations-v2.md"),
        ("Argon seul (questions ouvertes A/B/C)", "docs/notes/argon-seul-v1/lecture-argon-questions-ouvertes-abc-v1.md"),
        ("Fable 5.1 brainstorm primaire oct. 23", "gemini/01_DONNEES_PRIMAIRES_BRUTES/meta-brainstorm-decouverte-2026-10-23/cellules/E3-T1-conception-A.md"),
        ("Gemini brainstorm primaire oct. 23 (opérateur-invariant)", "gemini/01_DONNEES_PRIMAIRES_BRUTES/meta-brainstorm-decouverte-2026-10-23/cellules/E3-T1-conception-C.md"),
    ]
    # Ajouter aussi les autres dossiers protocole-x-* autorisés sur main
    for px_dir in sorted((RACINE / "docs/notes").glob("protocole-x-*")):
        if est_interdit(str(px_dir)):
            continue
        for md in sorted(px_dir.rglob("*.md")):
            rel = str(md.relative_to(RACINE))
            if est_interdit(rel) or any(rel == r for _, r in fichiers_directs_locaux):
                continue
            if any(k in md.name for k in ("reponse-", "synthese-", "demande-approfondie", "explication-")):
                fichiers_directs_locaux.append(("Protocole X (pièce amont/synthèse)", rel))

    def extraire_sections_md(texte: str, auteur: str, rel: str, branche: str, fam: str) -> None:
        blocs = re.split(r"(?m)^(#{2,3}\s+.+)$", texte)
        if len(blocs) < 3:
            ajouter(f"DOC-{sha256_texte(rel)[:8]}", Path(rel).stem, texte[:900], fam, auteur, rel, branche, "texte_complet_indexé")
            return
        for i in range(1, len(blocs), 2):
            sec_titre = blocs[i].lstrip("#").strip()
            corps = nettoyer(blocs[i + 1]) if i + 1 < len(blocs) else ""
            if len(corps) < 80:
                continue
            if any(skip in sec_titre.lower() for skip in ("référence", "bibliograph", "table des matières", "annexe : empreintes", "traçabilité")):
                continue
            ajouter(
                f"SEC-{sha256_texte(rel + sec_titre)[:8]}",
                f"{Path(rel).stem} — {sec_titre}",
                corps[:1000],
                fam,
                auteur,
                rel,
                branche,
                "section_extraite",
            )

    for auteur, rel in fichiers_directs_locaux:
        p = RACINE / rel
        if p.is_file() and not est_interdit(rel):
            extraire_sections_md(p.read_text(encoding="utf-8"), auteur, rel, "main", "S11_Reponses_Directes_Fable_Amont_et_Modeles_Hors_Collisionneur")

    fichiers_directs_distants = [
        ("idees/questions-directeur-2026-11-24-v1", "Fable 5.2 (Q1 quatre étapes oracles)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q1-quatre-etapes-oracles-organisme-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q2 profondeur surprise retirée)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q2-profondeur-surprise-retiree-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q3 cinétique collisions idées)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q3-cinetique-collisions-idees-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q4 émergence et percolation)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q4-emergence-transition-et-groupes-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q5 Carbon vs Fable et Plan Turing)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q5-carbon-fable-et-plan-turing-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q7 couche problèmes hypergraphe)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q7-couche-problemes-hypergraphe-v1.md"),
        ("idees/questions-directeur-2026-11-24-v1", "Opus 5.5 (Q9 trois graphes méta-mathématiques)", "docs/notes/questions-directeur-2026-11-24-v1/reponse-q9-expose-graphe-meta-mathematique-v1.md"),
        ("protocole-x/entrainement-et-juges-v1", "Protocole X (six dossiers retenus)", "docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-propositions-retenues-six-dossiers-v1.md"),
        ("protocole-x/entrainement-et-juges-v1", "Protocole X (synthèse idées originales)", "docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-idees-originales-v1.md"),
        ("protocole-x/entrainement-et-juges-v1", "Protocole X (questions concurrents)", "docs/notes/collisionneur-v9/syntheses-protocole-x-v1/note-synthese-questions-concurrents-v1.md"),
        ("runs/collisionneurs-reprise-2026-11-24-v1", "Collisionneur (boucle organisme-contrôle)", "docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-boucle-organisme-controle-v1.md"),
    ]
    for br, auteur, rel in fichiers_directs_distants:
        try:
            txt = gh_raw(br, rel)
            extraire_sections_md(txt, auteur, rel, br, "S11_Reponses_Directes_Fable_Amont_et_Modeles_Hors_Collisionneur")
        except Exception as exc:
            print(f"Info distant {br}:{rel} -> {exc}")

    # Dédoublonnage exact sur cle_contenu tout en conservant les variantes distinctes
    vues: set[str] = set()
    uniques: list[dict] = []
    for e in entrees:
        if e["cle_contenu"] in vues:
            continue
        vues.add(e["cle_contenu"])
        e["id_unifie"] = f"BIB-{len(uniques)+1:04d}"
        uniques.append(e)

    # Écriture des sorties structurées
    par_objet_dir = SORTIE / "par-objet"
    par_objet_dir.mkdir(parents=True, exist_ok=True)

    # JSONL maître
    p_jsonl = SORTIE / "corpus-unifie-idees-v1.jsonl"
    p_jsonl.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in uniques) + "\n", encoding="utf-8")

    slugs_objet = {
        "OBJ-1_METROLOGIE_ATTELAGE_ET_TESTS_DE_MORT": "01-metrologie-attelage-et-tests-de-mort",
        "OBJ-2_ARCHITECTURE_ORGANISME_MEMOIRE_ET_AUTOCONCEPTION": "02-architecture-organisme-memoire-et-autoconception",
        "OBJ-3_MATHEMATIQUES_NOUVELLES_3_GRAPHES_ET_HORS_ALPHABET": "03-mathematiques-nouvelles-3-graphes-et-hors-alphabet",
        "OBJ-4_CONTROLE_IA_MENACES_DIFFUSES_ET_SONDES": "04-controle-ia-menaces-diffuses-et-sondes",
        "OBJ-5_ETALONNAGES_CORPUS_REELS_ET_GPU_8B": "05-etalonnages-corpus-reels-et-gpu-8b",
    }

    par_obj: dict[str, list[dict]] = defaultdict(list)
    for e in uniques:
        par_obj[e["objet"]].append(e)

    for obj_key, slug in slugs_objet.items():
        lot = par_obj[obj_key]
        (par_objet_dir / f"{slug}.jsonl").write_text(
            "\n".join(json.dumps(e, ensure_ascii=False) for e in lot) + ("\n" if lot else ""),
            encoding="utf-8",
        )
        par_theme: dict[str, list[dict]] = defaultdict(list)
        for e in lot:
            par_theme[e["theme"]].append(e)
        md_lines = [
            f"# {OBJETS[obj_key]}",
            "",
            f"- **Entrées dédoublonnées dans ce rayon** : **{len(lot)}**",
            f"- **Fichier machine compagnon** : `par-objet/{slug}.jsonl`",
            "",
        ]
        for th in sorted(par_theme):
            items_th = par_theme[th]
            md_lines.append(f"## {th} ({len(items_th)} entrées)")
            md_lines.append("")
            md_lines.append("| ID unifié | ID origine | Régime | Source / Modèle | Titre et énoncé résumé | Chemin source |")
            md_lines.append("|---|---|---|---|---|---|")
            for it in items_th:
                res = f"**{it['titre']}** — {it['enonce'][:280]}".replace("|", "/")
                src_p = f"`{it['source_branche']}:{it['source_chemin']}`".replace("|", "/")
                md_lines.append(
                    f"| `{it['id_unifie']}` | `{it['id_origine'].replace('|','/')}` | `{it['regime_execution']}` | "
                    f"{it['espece_auteur'].replace('|','/')[:50]} | {res} | {src_p} |"
                )
            md_lines.append("")
        (par_objet_dir / f"{slug}.md").write_text("\n".join(md_lines), encoding="utf-8")

    # Index par thème
    c_obj = Counter(e["objet"] for e in uniques)
    c_theme = Counter((e["objet"], e["theme"]) for e in uniques)
    c_src = Counter(e["famille_source"] for e in uniques)
    c_reg = Counter(e["regime_execution"] for e in uniques)

    idx_theme = [
        "# Index général par Objet et par Thème scientifique (v1)",
        "",
        f"**Total dédoublonné** : **{len(uniques)} entrées** (extraites de {len(entrees)} occurrences brutes ; {exclus_compteur} entrées filtrées par la liste noire de cloisonnement).",
        "",
        "## Répartition par Objet et Thème",
        "",
        "| Objet | Thème scientifique | Nombre d'entrées | Rayon détaillé |",
        "|---|---|---:|---|",
    ]
    for (ok, th), nb in sorted(c_theme.items()):
        slug = slugs_objet[ok]
        idx_theme.append(f"| {OBJETS[ok]} | {th} | **{nb}** | `par-objet/{slug}.md` |")
    (SORTIE / "INDEX-PAR-OBJET-ET-THEME-v1.md").write_text("\n".join(idx_theme) + "\n", encoding="utf-8")

    # Index par source + branches brutes restantes à ouvrir à chaud si besoin
    idx_src = [
        "# Index général par Famille de sources, Modèles et Régimes d'exécution (v1)",
        "",
        "## 1. Comptes par famille de sources ingérées",
        "",
        "| Famille de source | Entrées brutes lues |",
        "|---|---:|",
    ]
    for fam, nb in sorted(stats_sources.items()):
        idx_src.append(f"| `{fam}` | **{nb}** |")
    idx_src += [
        "",
        "## 2. Comptes par régime matériel d'épreuve",
        "",
        "| Régime d'exécution | Entrées uniques | Usage en Étape 1 / Étape 2 |",
        "|---|---:|---|",
        f"| `CPU_0_USD_SYNTHETIQUE` | **{c_reg['CPU_0_USD_SYNTHETIQUE']}** | Tests de mort immédiats sur processeur local (0 USD) |",
        f"| `CPU_DONNEES_PUBLIQUES_REEL` | **{c_reg['CPU_DONNEES_PUBLIQUES_REEL']}** | Étalonnages réels processeur (PubTator 3, Gu et Krenn 2026 bras A/C, cit-HepTh) |",
        f"| `GPU_VAST_8B_SOUS_GO` | **{c_reg['GPU_VAST_8B_SOUS_GO']}** | Épreuves sur modèle ouvert 8B loué sur Vast.ai sous `GO-2026-11-25-05` (dopamine H10, préfixage T4) |",
        f"| `DEJA_REFUTE_OU_ECARTE` | **{c_reg['DEJA_REFUTE_OU_ECARTE']}** | Mémoire négative initiale (ne jamais relancer tel quel) |",
        "",
        "## 3. Branches de cellules brutes supplémentaires non encore synthétisées (pointeurs pour lecture à la demande)",
        "",
        "- `origin/donnees/collisionneur-v8-runs-v2` : dossiers `donnees/collisionneur-v8-runs-v1/selection-generations-v1/` et `bac-a-sable-v1/` (30 cellules à 5 espèces du 2 novembre).",
        "- `origin/donnees/collisionneur-v9-brainstorm-v1-suite` : 15 cellules du remue-méninges des 2-3 novembre.",
        "- `origin/donnees/course-*-run*` : 10 branches de courses de l'organisme sur les questions des mentors (3 novembre).",
        "- `origin/matiere-premiere/visees-mathematiques-v1` : trois réponses externes sur les visées mathématiques.",
        "- `origin/claude/upbeat-edison-t3wegg` : cellules du premier tour `runs/collisionneur-protocole-x-idees-interessantes-abonnement-v1-20261123-135306/cellules/`.",
    ]
    (SORTIE / "INDEX-PAR-SOURCE-ET-MODELE-v1.md").write_text("\n".join(idx_src) + "\n", encoding="utf-8")

    manifeste = {
        "version": "v1",
        "total_occurrences_brutes_autorisees": len(entrees),
        "total_entrees_uniques_dedoublonnees": len(uniques),
        "entrees_exclues_par_liste_noire_cloisonnement": exclus_compteur,
        "par_objet": dict(c_obj),
        "par_regime_execution": dict(c_reg),
        "par_famille_source_brute": dict(stats_sources),
    }
    (SORTIE / "manifeste-couverture-sources-v1.json").write_text(
        json.dumps(manifeste, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lisezmoi = [
        "# Bibliothèque unifiée des idées, hypothèses, mécanismes et verrous — version 1",
        "",
        "Pièce de travail (classe C) générée déterministiquement par `construire_corpus_unifie_v1.py` sous filtrage strict de cloisonnement (aucun coffre, aucun verdict sous embargo, aucune réponse des questions témoins, aucun dossier d'attaque ou de sabotage ouvert).",
        "",
        "## Rôle pour l'Étape 1 de l'organisme en boucle fermée",
        "",
        "Au lieu de fouiller 946 branches à chaque lancement et de brûler des jetons de contexte, tout workflow ou essaim lit directement ce dossier unique :",
        "- `corpus-unifie-idees-v1.jsonl` : fichier maître dédoublonné de toutes les entrées, prêt pour le filtrage mécanique et le tirage aléatoire `1 c` sous `numpy.random.SeedSequence` ;",
        "- `INDEX-PAR-OBJET-ET-THEME-v1.md` : vue analytique complète en **5 Objets** et **21 Thèmes scientifiques** ;",
        "- `INDEX-PAR-SOURCE-ET-MODELE-v1.md` : traçabilité par gisement d'origine (Bibliothécaire, Veille de cap, Protocole X amont Fable/Opus/Carbon, 99 courses de collisionneurs T1/T3, modèles consultés seuls, 21 lots d'auto-conception, Plan Turing et 18 verrous) et par régime matériel (`CPU_0_USD_SYNTHETIQUE`, `CPU_DONNEES_PUBLIQUES_REEL`, `GPU_VAST_8B_SOUS_GO`, `DEJA_REFUTE_OU_ECARTE`) ;",
        "- `par-objet/01-...` à `05-...` (`.md` et `.jsonl`) : les cinq rayons thématiques prêts à servir séparément aux agents spécialisés.",
        "",
        f"**Chiffres clés vérifiés** : **{len(uniques)} entrées uniques** dédoublonnées ({len(entrees)} occurrences lues, {exclus_compteur} filtrées par liste noire).",
        "",
    ]
    (SORTIE / "LISEZMOI-v1.md").write_text("\n".join(lisezmoi), encoding="utf-8")
    print(json.dumps(manifeste, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    construire()
