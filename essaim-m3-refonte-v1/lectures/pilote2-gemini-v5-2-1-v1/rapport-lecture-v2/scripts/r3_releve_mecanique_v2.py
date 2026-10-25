"""r3 v2 — relevé mécanique d'une course extraite (lecture de JSON et de texte seulement ; rien n'est exécuté).

Usage : python3 -I r3_releve_mecanique.py DOSSIER_EXTRAIT EXTRAIT_MECANIQUE_JSON SORTIE_JSON

Relève, pour la course : manifeste, rapport, événements ; par génération : résumé (exécution, `caches`),
journal des appels (par espèce, par rôle, par statut ; jetons ; appels qui ont réfléchi ; coûts ; durées ;
appels de la question), recherches et téléchargements, castes, taille de mémoire, archives de l'organisme
(membres, empreintes, empreinte d'arbre recalculée comme `boucle.empreinte_arbre`), réponse à la question
(structure mécanique). Ne calcule aucune différence de score et ne lit aucun score hors de `juge/score.json`
(champs `calibration` et `non_repondu` de `test`, recopiés tels quels).
"""
import collections
import datetime
import hashlib
import io
import json
import os
import re
import sys
import tarfile

LIGNEE = "gemini-organisme-v5-2-1"


def sha_fichier(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def compagnon(p):
    """Compare l'empreinte d'un fichier à son compagnon `.sha256` s'il existe."""
    c = p + ".sha256"
    if not os.path.exists(c):
        return {"compagnon": None}
    attendu = open(c, encoding="utf-8").read().split()[0]
    e = sha_fichier(p)
    return {"sha256": e, "compagnon": attendu, "conforme": e == attendu}


def jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def t(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


def empreinte_arbre_fichiers(fichiers):
    """fichiers : liste de (chemin relatif, octets) ; même calcul que `boucle.empreinte_arbre`."""
    h = hashlib.sha256()
    for rel, contenu in sorted(fichiers):
        parts = rel.split("/")
        if rel.endswith(".pyc") or "__pycache__" in parts:
            continue
        h.update(rel.encode("utf-8") + b"\0")
        h.update(hashlib.sha256(contenu).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()


def fichiers_dossier(d):
    out = []
    for racine, _, fs in os.walk(d):
        for f in fs:
            p = os.path.join(racine, f)
            out.append((os.path.relpath(p, d).replace(os.sep, "/"), open(p, "rb").read()))
    return out


def fichiers_tar(p, prefixe="organisme/"):
    out = []
    with tarfile.open(p, "r:gz") as tf:
        for m in tf.getmembers():
            if not m.isfile():
                continue
            nom = m.name[len(prefixe):] if m.name.startswith(prefixe) else m.name
            out.append((nom, tf.extractfile(m).read()))
    return out


def table_fichiers(fs):
    return {rel: {"octets": len(b), "sha256": hashlib.sha256(b).hexdigest()} for rel, b in sorted(fs)}


def releve_appels(appels):
    r = {"n": len(appels)}
    par_triple = collections.Counter()
    par_role = {}
    par_espece = {}
    fins = collections.Counter()
    echecs = collections.Counter()
    max_tokens = collections.Counter()
    tot_e = tot_s = 0
    tot_c = 0.0
    for a in appels:
        esp, role, st = a.get("espece"), a.get("role"), a.get("statut")
        par_triple[(esp, role, st)] += 1
        u = a.get("usage") or {}
        e, s = int(u.get("entree") or 0), int(u.get("sortie") or 0)
        c = float(a.get("cout_usd") or 0.0)
        tot_e += e
        tot_s += s
        tot_c += c
        refl = "thinking" in (a.get("types_blocs") or [])
        dur = (t(a["fin_utc"]) - t(a["debut_utc"])).total_seconds() if a.get("fin_utc") and a.get("debut_utc") else None
        for cle, dico in ((role, par_role), (esp, par_espece)):
            x = dico.setdefault(cle, {"n": 0, "par_statut": collections.Counter(), "entree": 0, "sortie": 0,
                                      "cout_usd": 0.0, "reflexion_par_statut": collections.Counter(),
                                      "duree_s_somme": 0.0, "duree_s_max": 0.0, "especes": set(),
                                      "modeles_servis": set(), "roles": set()})
            x["n"] += 1
            x["par_statut"][st] += 1
            x["entree"] += e
            x["sortie"] += s
            x["cout_usd"] += c
            if refl:
                x["reflexion_par_statut"][st] += 1
            if dur is not None:
                x["duree_s_somme"] += dur
                x["duree_s_max"] = max(x["duree_s_max"], dur)
            x["especes"].add(esp)
            x["roles"].add(role)
            x["modeles_servis"].add(a.get("modele_servi"))
        fins[a.get("fin")] += 1
        if st != "OK":
            echecs[(st, str(a.get("echec"))[:160])] += 1
        max_tokens[a.get("max_tokens")] += 1

    def propre(d):
        out = {}
        for k, x in d.items():
            out[str(k)] = {"n": x["n"], "par_statut": dict(x["par_statut"]), "entree": x["entree"],
                           "sortie": x["sortie"], "cout_usd": round(x["cout_usd"], 6),
                           "reflexion_par_statut": dict(x["reflexion_par_statut"]),
                           "duree_s_somme": round(x["duree_s_somme"], 3), "duree_s_max": round(x["duree_s_max"], 3),
                           "especes": sorted(map(str, x["especes"])), "roles": sorted(map(str, x["roles"])),
                           "modeles_servis": sorted(map(str, x["modeles_servis"]))}
        return out

    r["par_espece_role_statut"] = [{"espece": k[0], "role": k[1], "statut": k[2], "n": v}
                                   for k, v in sorted(par_triple.items(), key=lambda kv: tuple(map(str, kv[0])))]
    r["par_role"] = propre(par_role)
    r["par_espece"] = propre(par_espece)
    r["par_statut"] = dict(collections.Counter(a.get("statut") for a in appels))
    r["fins"] = {str(k): v for k, v in fins.items()}
    r["echecs"] = [{"statut": k[0], "echec": k[1], "n": v} for k, v in echecs.items()]
    r["max_tokens"] = {str(k): v for k, v in max_tokens.items()}
    r["entree"] = tot_e
    r["sortie"] = tot_s
    r["cout_usd_somme"] = round(tot_c, 6)
    r["cumul_usd_dernier"] = appels[-1].get("cumul_usd") if appels else None
    r["reflexion_par_statut"] = dict(collections.Counter(a.get("statut") for a in appels
                                                         if "thinking" in (a.get("types_blocs") or [])))
    r["types_blocs"] = dict(collections.Counter(",".join(a.get("types_blocs") or []) for a in appels))
    r["premier_debut_utc"] = min(a["debut_utc"] for a in appels) if appels else None
    r["derniere_fin_utc"] = max(a["fin_utc"] for a in appels) if appels else None
    r["reel"] = sorted(set(map(str, (a.get("reel") for a in appels))))
    r["go_id"] = sorted(set(map(str, (a.get("go_id") for a in appels))))
    return r


def releve_question(appels, journal_gen):
    """Appels de la question : l'appel de formulation des requêtes et tous ceux qui le suivent (ordre des identifiants)."""
    ordre = sorted(appels, key=lambda a: a["id"])
    idx = [i for i, a in enumerate(ordre) if a.get("role") == "moissonneur_formulation_requetes"]
    if not idx:
        return {"appels": [], "note": "aucun appel de formulation"}
    q = ordre[idx[0]:]
    lignes = [{"id": a["id"], "espece": a.get("espece"), "role": a.get("role"), "statut": a.get("statut"),
               "entree": (a.get("usage") or {}).get("entree"), "sortie": (a.get("usage") or {}).get("sortie"),
               "cout_usd": a.get("cout_usd"), "types_blocs": a.get("types_blocs"), "fin": a.get("fin"),
               "debut_utc": a.get("debut_utc"), "fin_utc": a.get("fin_utc"), "caracteres": a.get("caracteres")}
              for a in q]
    avant = ordre[:idx[0]]
    par_phase = {}
    for etiquette, groupe in (("avant la question", avant), ("question", q)):
        c = collections.Counter((a.get("espece"), a.get("role"), a.get("statut")) for a in groupe)
        par_phase[etiquette] = [{"espece": k[0], "role": k[1], "statut": k[2], "n": v} for k, v in sorted(c.items(), key=lambda kv: tuple(map(str, kv[0])))]
    qo = (journal_gen or {}).get("question_ouverte") or {}
    castes = [{k: v for k, v in c.items() if k in ("id_caste", "role", "espece", "mode", "confiance")}
              for c in (qo.get("votes_castes") or [])]
    return {"appels": lignes, "par_phase": par_phase,
            "par_statut": dict(collections.Counter(a.get("statut") for a in q)),
            "plafond": sum(1 for a in q if a.get("statut") == "PLAFOND"),
            "refus": sum(1 for a in q if a.get("statut") == "REFUS"),
            "organisme": {k: qo.get(k) for k in ("question_ouverte_traitee", "fichier_ecrit", "n_castes_question",
                                                  "appels_question_tentes", "appels_question_ok",
                                                  "appels_question_echec", "confiance_agregee")},
            "castes_question": castes,
            "moissonnage": qo.get("moissonnage")}


RE_ARXIV = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?![\d])")
RE_DOI = re.compile(r"\b10\.\d{4,9}/[^\s\)\]>,;\"'`]+")
RE_URL = re.compile(r"https?://[^\s\)\]>\"'`]+")
RE_CROCHET = re.compile(r"\[\d+(?:\s*[,–-]\s*\d+)*\]")


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", (s or "").lower())).strip()


def notices_moisson(dossier_noyau, index_corpus):
    """Notices rendues par les recherches d'une génération : (source, identifiants, titre)."""
    out = []
    for r in jsonl(os.path.join(dossier_noyau, "journal-recherches.jsonl")):
        p = os.path.join(dossier_noyau, "recherches", r["id"] + ".brut")
        if not os.path.exists(p):
            continue
        brut = open(p, "rb").read().decode("utf-8", "replace")
        src = r["source"]
        if src == "arxiv":
            for e in re.findall(r"<entry>(.*?)</entry>", brut, flags=re.S):
                i = re.search(r"<id>(.*?)</id>", e, flags=re.S)
                ti = re.search(r"<title>(.*?)</title>", e, flags=re.S)
                ids = set()
                if i:
                    m = RE_ARXIV.search(i.group(1))
                    if m:
                        ids.add(m.group(1))
                out.append({"source": src, "ids": sorted(ids), "titre": re.sub(r"\s+", " ", ti.group(1)).strip() if ti else ""})
        else:
            try:
                d = json.loads(brut)
            except Exception:
                continue
            if src == "openalex":
                items = d.get("results") or []
                for it in items:
                    ids = set()
                    doi = (it.get("doi") or "").lower().replace("https://doi.org/", "")
                    if doi:
                        ids.add(doi)
                    if it.get("id"):
                        ids.add(str(it["id"]))
                    loc = json.dumps(it.get("locations") or [])[:20000]
                    for m in RE_ARXIV.finditer(loc):
                        if "arxiv" in loc.lower():
                            ids.add(m.group(1))
                    out.append({"source": src, "ids": sorted(ids), "titre": it.get("title") or it.get("display_name") or ""})
            elif src == "semanticscholar":
                for it in d.get("data") or []:
                    ids = set()
                    ex = it.get("externalIds") or {}
                    if ex.get("DOI"):
                        ids.add(str(ex["DOI"]).lower())
                    if ex.get("ArXiv"):
                        ids.add(str(ex["ArXiv"]))
                    if it.get("paperId"):
                        ids.add(str(it["paperId"]))
                    if it.get("url"):
                        ids.add(str(it["url"]))
                    out.append({"source": src, "ids": sorted(ids), "titre": it.get("title") or ""})
            elif src == "web":
                for it in ((d.get("web") or {}).get("results") or []):
                    out.append({"source": src, "ids": [it.get("url") or ""], "titre": it.get("title") or ""})
    for doc in index_corpus:
        ids = set()
        for champ in ("adresse", "reference"):
            v = doc.get(champ) or ""
            m = RE_ARXIV.search(v)
            if m and "arxiv" in v:
                ids.add(m.group(1))
            elif v:
                ids.add(v)
        out.append({"source": "telechargement", "ids": sorted(ids), "titre": doc.get("titre") or ""})
    return out


def structure_reponse(p, notices_g1, notices_g0):
    b = open(p, "rb").read()
    s = b.decode("utf-8")
    lignes = s.split("\n")
    titres = [(len(l) - len(l.lstrip("#")), l.lstrip("#").strip(), i + 1) for i, l in enumerate(lignes)
              if re.match(r"^#{1,6}\s", l)]
    organisation = [i + 1 for i, l in enumerate(lignes) if "ORGANISATION" in l]
    arxiv = sorted(set(m.group(1) for m in RE_ARXIV.finditer(s)))
    dois = sorted(set(m.group(0).rstrip(".").lower() for m in RE_DOI.finditer(s)))
    urls = sorted(set(m.group(0).rstrip(".") for m in RE_URL.finditer(s)))
    s_norm = norm(s)

    def cites(notices):
        vus = []
        for n in notices:
            ok = False
            for i in n["ids"]:
                if not i:
                    continue
                if RE_ARXIV.fullmatch(i) and i in arxiv:
                    ok = True
                elif i.lower() in s.lower():
                    ok = True
            tn = norm(n["titre"])
            if len(tn) >= 20 and tn in s_norm:
                ok = True
            if ok:
                vus.append({"source": n["source"], "ids": n["ids"], "titre": n["titre"][:140]})
        # dédoublonnage par titre normalisé ou identifiant
        uniq, cles = [], set()
        for v in vus:
            k = norm(v["titre"]) or "|".join(v["ids"])
            if k in cles:
                continue
            cles.add(k)
            uniq.append(v)
        return uniq

    refs = [("arxiv", a) for a in arxiv] + [("doi", d_) for d_ in dois] + \
           [("url", u) for u in urls if not re.search(r"arxiv\.org/(abs|pdf)/", u)]

    def provenance(ref):
        genre, v = ref
        out = []
        for etiquette, notices in (("g001", notices_g1), ("g000", notices_g0)):
            for n in notices:
                if any(i and (i == v or i.lower() == v.lower()) for i in n["ids"]):
                    out.append(etiquette + ":" + n["source"])
        return sorted(set(out))

    references = [{"genre": g_, "valeur": v, "provenance": provenance((g_, v))} for g_, v in refs]
    return {"octets": len(b), "sha256": hashlib.sha256(b).hexdigest(), "caracteres": len(s),
            "references": references,
            "lignes": len(lignes) - (1 if s.endswith("\n") else 0), "lignes_non_vides": sum(1 for l in lignes if l.strip()),
            "mots": len(s.split()), "titres": [{"niveau": n, "texte": x, "ligne": i} for n, x, i in titres],
            "lignes_ORGANISATION": organisation, "arxiv_distincts": arxiv, "doi_distincts": dois,
            "url_distinctes": urls, "et_al": len(re.findall(r"\bet al\.", s)),
            "crochets_numeriques": len(RE_CROCHET.findall(s)),
            "notices_moisson_g001": len(notices_g1), "notices_moisson_g000": len(notices_g0),
            "moissonnes_g001_cites": cites(notices_g1), "moissonnes_g000_cites": cites(notices_g0)}


def main():
    base, extrait_p, sortie = sys.argv[1], sys.argv[2], sys.argv[3]
    course = os.path.join(base, "course")
    arch = os.path.join(course, "archive", LIGNEE)
    ext = json.load(open(extrait_p, encoding="utf-8"))
    out = {"dossier": base, "extrait": {"chemin": extrait_p, "sha256": sha_fichier(extrait_p)}}

    man = json.load(open(os.path.join(course, "manifeste-run.json"), encoding="utf-8"))
    out["manifeste"] = man
    out["manifeste_sha256"] = sha_fichier(os.path.join(course, "manifeste-run.json"))
    out["manifeste_egal_extrait"] = (man == ext.get("manifeste"))
    rap_p = os.path.join(course, "rapport-v1.json")
    rap = json.load(open(rap_p, encoding="utf-8"))
    out["rapport"] = {k: rap.get(k) for k in ("depense_totale_usd", "fin_utc", "n_appels_total", "generations_invalidees",
                                              "arrets", "arret", "raison_arret")}
    out["rapport"]["lignees"] = {k: {kk: vv for kk, vv in v.items() if kk in ("active", "fin", "generation", "uid", "impose")}
                                 for k, v in (rap.get("lignees") or {}).items()}
    out["rapport"]["cles"] = sorted(rap.keys())
    out["rapport_compagnon"] = compagnon(rap_p)
    out["evenements"] = [{k: v for k, v in e.items() if k in ("etape", "statut", "quand_utc", "raison", "generation", "usage", "problemes")}
                         for e in jsonl(os.path.join(course, "evenements.jsonl"))]
    out["index_archive"] = jsonl(os.path.join(course, "archive", "index.jsonl"))
    for e in out["index_archive"]:
        e.pop("score", None)  # le score global est dans les tableaux ; il n'est pas repris ici

    gens = {}
    notices = {}
    for g in ("g000", "g001"):
        A = os.path.join(arch, g)
        T = os.path.join(A, "travail")
        res = json.load(open(os.path.join(A, "resume.json"), encoding="utf-8"))
        x = {"resume_compagnon": compagnon(os.path.join(A, "resume.json"))}
        x["statut"] = res.get("statut")
        x["invalide"] = res.get("invalide")
        x["anomalie_noyau"] = res.get("anomalie_noyau")
        x["execution"] = {k: v for k, v in (res.get("execution") or {}).items() if k != "tmp_prives"}
        x["execution"]["n_tmp_prives"] = len((res.get("execution") or {}).get("tmp_prives") or [])
        for k in ("cout_usd", "n_appels", "n_recherches", "n_telechargements", "relance", "elements_ecartes",
                  "n_elements_ecartes", "refus_noyau", "empreinte_organisme", "question_ouverte", "non_conformes",
                  "indisponibles", "successeur", "problemes_successeur", "appels_simultanes_max", "n_reponses_test",
                  "quand_utc", "n_entrainements", "gel", "phase"):
            x[k] = res.get(k)
        ja = os.path.join(A, "journal-appels.jsonl")
        x["journal_appels_compagnon"] = compagnon(ja)
        x["journal_appels_identique_travail"] = sha_fichier(ja) == sha_fichier(os.path.join(T, "noyau", "journal-appels.jsonl"))
        appels = jsonl(ja)
        x["appels"] = releve_appels(appels)
        jg = json.load(open(os.path.join(T, "journal_generation.json"), encoding="utf-8"))
        x["castes_taches"] = jg.get("castes")
        x["n_castes_recrutees"] = jg.get("n_castes_recrutees")
        x["bascule_parallele_a_la_tache"] = jg.get("bascule_parallele_a_la_tache")
        x["temps_s_organisme"] = jg.get("temps_s")
        x["compteurs_appels_organisme"] = jg.get("compteurs_appels")
        x["moisson_taches"] = jg.get("moisson_taches")
        x["question"] = releve_question(appels, jg) if g == "g001" else None
        # recherches et téléchargements
        jr = jsonl(os.path.join(T, "noyau", "journal-recherches.jsonl"))
        x["recherches"] = [{k: r.get(k) for k in ("id", "source", "statut", "n_demande", "n_rendus", "n_retires_fuite",
                                                   "recoupements_courts", "requete", "echec", "debut_utc", "fin_utc", "octets_brut")}
                           for r in jr]
        x["recherches_par_source_statut"] = {}
        for r in jr:
            x["recherches_par_source_statut"].setdefault(r["source"], collections.Counter())[r["statut"]] += 1
        x["recherches_par_source_statut"] = {k: dict(v) for k, v in x["recherches_par_source_statut"].items()}
        idx_p = os.path.join(T, "corpus", "index.jsonl")
        idx = jsonl(idx_p) if os.path.exists(idx_p) else []
        x["corpus_index_compagnon"] = compagnon(idx_p) if os.path.exists(idx_p) else None
        x["telechargements"] = [{k: d.get(k) for k in ("id", "statut", "adresse", "reference", "octets", "caracteres_texte",
                                                       "genre", "type_contenu", "echec", "debut_utc", "fin_utc")} for d in idx]
        x["telechargements_par_statut"] = dict(collections.Counter(d.get("statut") for d in idx))
        jf = os.path.join(T, "noyau", "journal-fuite.jsonl")
        x["journal_fuite"] = [{k: v for k, v in l.items() if k in ("statut", "n_retires", "sha256_recoupement", "id", "objet")}
                              for l in jsonl(jf)] if os.path.exists(jf) else None
        notices[g] = notices_moisson(os.path.join(T, "noyau"), idx)
        x["n_notices_moisson"] = len(notices[g])
        # mémoire
        mem = {}
        for nom, p in (("travail/memoire_isvd.json", os.path.join(T, "memoire_isvd.json")),
                       ("travail/organisme/memoire_isvd.json", os.path.join(T, "organisme", "memoire_isvd.json")),
                       ("travail/successeur/organisme/memoire_isvd.json", os.path.join(T, "successeur", "organisme", "memoire_isvd.json")),
                       ("lignees/%s/organisme/memoire_isvd.json" % g, os.path.join(course, "lignees", LIGNEE, g, "organisme", "memoire_isvd.json"))):
            mem[nom] = {"octets": os.path.getsize(p), "sha256": sha_fichier(p)} if os.path.exists(p) else None
        x["memoire"] = mem
        # archives et code
        ot = os.path.join(A, "organisme.tar.gz")
        x["organisme_tar_compagnon"] = compagnon(ot)
        ft = fichiers_tar(ot)
        x["organisme_tar_fichiers"] = table_fichiers(ft)
        x["organisme_tar_empreinte_arbre"] = empreinte_arbre_fichiers(ft)
        code_tar = [(r, b) for r, b in ft if r not in ("memoire_isvd.json", "etat_generation_precedente.json")]
        x["organisme_tar_empreinte_arbre_sans_memoire"] = empreinte_arbre_fichiers(code_tar)
        lig = os.path.join(course, "lignees", LIGNEE, g, "organisme")
        fl = fichiers_dossier(lig)
        x["lignee_entree_fichiers"] = table_fichiers(fl)
        x["lignee_entree_empreinte_arbre"] = empreinte_arbre_fichiers(fl)
        x["lignee_entree_empreinte_arbre_sans_memoire"] = empreinte_arbre_fichiers(
            [(r, b) for r, b in fl if r not in ("memoire_isvd.json", "etat_generation_precedente.json")])
        # extrait : recoupement des comptes
        eg = [e for e in ext["generations"] if e.get("chemin") == f"{LIGNEE}/{g}"]
        if eg:
            eg = eg[0]
            x["recoupement_extrait"] = {
                "n_appels": (eg.get("n_appels"), x["n_appels"], len(appels)),
                "par_statut": (eg["appels"]["par_statut"], x["appels"]["par_statut"]),
                "cout_usd_appels": (eg["appels"]["cout_usd"], x["appels"]["cout_usd_somme"]),
                "recherches": (eg["services"]["recherches"], x["recherches_par_source_statut"]),
                "telechargements": (eg["services"]["telechargements"], x["telechargements_par_statut"]),
                "empreinte_organisme": (eg.get("organisme_tar_sha256"), (x["organisme_tar_compagnon"] or {}).get("sha256")),
                "fichiers_travail_memoire": [f for f in eg.get("fichiers_travail") or [] if f.get("chemin") == "memoire_isvd.json"],
                "duree_s": (eg["execution"].get("duree_s"), x["execution"].get("duree_s")),
            }
        # scores de `test` stockés (calibration et non-réponses), recopiés tels quels
        sc = json.load(open(os.path.join(A, "juge", "score.json"), encoding="utf-8"))
        x["test_stocke"] = {fam: {"brier": v.get("calibration", {}).get("brier"), "ece_10": v.get("calibration", {}).get("ece_10"),
                                  "non_repondu": v.get("non_repondu"), "n": v.get("n")}
                            for fam, v in (sc.get("par_famille") or {}).items()}
        x["test_stocke"]["(score du juge)"] = {"brier": sc.get("calibration", {}).get("brier"),
                                               "ece_10": sc.get("calibration", {}).get("ece_10"), "non_repondu": None, "n": sc.get("n")}
        x["score_json_compagnon"] = compagnon(os.path.join(A, "juge", "score.json"))
        x["score_final_json_compagnon"] = compagnon(os.path.join(A, "juge", "score-final.json"))
        gens[g] = x
    out["generations"] = gens
    # identité du code : g000 contre g001
    a0, a1 = gens["g000"]["organisme_tar_fichiers"], gens["g001"]["organisme_tar_fichiers"]
    out["code_g0_g1"] = {
        "communs_identiques": sorted(k for k in a0 if k in a1 and a0[k]["sha256"] == a1[k]["sha256"]),
        "communs_differents": sorted(k for k in a0 if k in a1 and a0[k]["sha256"] != a1[k]["sha256"]),
        "seulement_g000": sorted(k for k in a0 if k not in a1),
        "seulement_g001": sorted(k for k in a1 if k not in a0),
    }
    # réponse à la question
    rq = os.path.join(arch, "g001", "reponse-question.md")
    out["reponse_compagnon"] = compagnon(rq)
    out["reponse_identique_travail"] = sha_fichier(rq) == sha_fichier(os.path.join(arch, "g001", "travail", "reponse-question.md"))
    out["reponse_structure"] = structure_reponse(rq, notices["g001"], notices["g000"])
    # la question servie (dans contexte.json de g001)
    ctx = json.load(open(os.path.join(arch, "g001", "travail", "contexte.json"), encoding="utf-8"))
    qo = ctx.get("question_ouverte")
    if isinstance(qo, dict):
        texte = qo.get("texte") or qo.get("question") or ""
        out["question_servie"] = {"cles": sorted(qo.keys()), "caracteres": len(texte),
                                  "sha256_texte": hashlib.sha256(texte.encode("utf-8")).hexdigest()}
    else:
        texte = qo or ""
        out["question_servie"] = {"type": type(qo).__name__, "caracteres": len(texte),
                                  "sha256_texte": hashlib.sha256(texte.encode("utf-8")).hexdigest() if texte else None}
    rep_txt = open(rq, encoding="utf-8").read()
    out["question_servie"]["recopiee_mot_pour_mot_dans_la_reponse"] = bool(texte) and (texte.strip() in rep_txt)
    ctx0 = json.load(open(os.path.join(arch, "g000", "travail", "contexte.json"), encoding="utf-8"))
    out["question_g000"] = ctx0.get("question_ouverte")
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True, default=lambda o: sorted(o) if isinstance(o, set) else str(o))
    with open(sortie.replace(".json", "-question-servie.txt"), "w", encoding="utf-8") as f:
        f.write(texte)
    print("écrit", sortie)


if __name__ == "__main__":
    main()
