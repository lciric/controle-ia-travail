"""Lecture du corpus, passes d'extraction, vocabulaires et matrices creuses — rétrodiction Swanson v1.

Passe 1 : empreintes 64 bits des termes de chaque document d'avant (fréquences documentaires, vocabulaires).
Passe 2 : tous les documents, projection sur chaque vocabulaire, chaînes des termes et contrôle des conflits d'empreinte.
"""
import multiprocessing as mp
import subprocess

import numpy as np
from scipy import sparse

from termes_v1 import empreinte64, groupe_de, termes_document

_G = {}


def heure_utc():
    return subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()


def lire_corpus(chemin, dossier_temporaire):
    """Une ligne par identifiant (première dans l'ordre catégories, titre, résumé), ordre (année, identifiant)."""
    import duckdb

    con = duckdb.connect(config={"autoinstall_known_extensions": False, "autoload_known_extensions": False,
                                 "temp_directory": dossier_temporaire, "threads": 2, "memory_limit": "3GB"})
    requete = """
        SELECT id, annee, categories, title, abstract FROM read_parquet(?)
        QUALIFY row_number() OVER (PARTITION BY id ORDER BY categories, title, abstract) = 1
        ORDER BY annee, id"""
    curseur = con.execute(requete, [chemin])
    ids, annees, groupes, titres, resumes = [], [], [], [], []
    while True:
        lot = curseur.fetchmany(50000)
        if not lot:
            break
        for identifiant, annee, categories, titre, resume in lot:
            ids.append(identifiant)
            annees.append(annee)
            groupes.append(groupe_de(categories))
            titres.append(titre)
            resumes.append(resume)
    n_lignes = con.execute("SELECT count(*) FROM read_parquet(?)", [chemin]).fetchone()[0]
    con.close()
    return dict(ids=ids, annees=np.array(annees, np.int32), groupes=np.array(groupes, np.int8), titres=titres,
                resumes=resumes, n_lignes=n_lignes)


def _lots(n0, n1, taille):
    return [(i, min(i + taille, n1)) for i in range(n0, n1, taille)]


def _executer(fonction, lots, n_proc):
    if n_proc <= 1:
        return [fonction(lot) for lot in lots]
    with mp.get_context("fork").Pool(n_proc) as pool:
        return list(pool.imap(fonction, lots, chunksize=1))


def _passe1_travail(bornes):
    i0, i1 = bornes
    titres, resumes = _G["titres"], _G["resumes"]
    longueurs = np.empty(i1 - i0, np.int64)
    morceaux = []
    for k, i in enumerate(range(i0, i1)):
        termes = termes_document(titres[i], resumes[i])
        morceaux.append(np.fromiter((empreinte64(t) for t in termes), dtype=np.uint64, count=len(termes)))
        longueurs[k] = len(termes)
    return i0, longueurs, (np.concatenate(morceaux) if morceaux else np.empty(0, np.uint64))


def passe1(titres, resumes, n_docs, n_proc, taille_lot=4000):
    _G.clear()
    _G.update(titres=titres, resumes=resumes)
    resultats = _executer(_passe1_travail, _lots(0, n_docs, taille_lot), n_proc)
    _G.clear()
    longueurs = np.concatenate([r[1] for r in resultats])
    empreintes = np.concatenate([r[2] for r in resultats])
    return longueurs, empreintes


def vocabulaire_empreintes(longueurs, empreintes, n_docs_avant, df_min, df_max_frac):
    """Empreintes (triées) et fréquences des termes de df ∈ [df_min ; df_max_frac × n_docs_avant] sur les n premiers docs."""
    fin = int(longueurs[:n_docs_avant].sum())
    valeurs, df = np.unique(empreintes[:fin], return_counts=True)
    garde = (df >= df_min) & (df <= df_max_frac * n_docs_avant)
    return valeurs[garde], df[garde], int(valeurs.size)


def _passe2_travail(bornes):
    i0, i1 = bornes
    titres, resumes, annees, vocabs = _G["titres"], _G["resumes"], _G["annees"], _G["vocabs"]
    vus = _G.setdefault("vus", {})
    nouveaux = []
    n_v = len(vocabs)
    longueurs = [np.zeros(i1 - i0, np.int32) for _ in range(n_v)]
    ids = [[] for _ in range(n_v)]
    for k, i in enumerate(range(i0, i1)):
        actifs = [s for s in range(n_v) if annees[i] <= vocabs[s][1]]
        if not actifs:
            continue
        compte = [0] * n_v
        for terme in termes_document(titres[i], resumes[i]):
            h = empreinte64(terme)
            trouve = False
            for s in actifs:
                j = vocabs[s][0].get(h)
                if j is not None:
                    ids[s].append(j)
                    compte[s] += 1
                    trouve = True
            if trouve:
                deja = vus.get(h)
                if deja is None:
                    vus[h] = terme
                    nouveaux.append((h, terme))
                elif deja != terme:
                    raise RuntimeError(f"conflit d'empreinte : {deja!r} et {terme!r}")
        for s in actifs:
            longueurs[s][k] = compte[s]
    return i0, longueurs, [np.array(x, np.int32) for x in ids], nouveaux


def passe2(titres, resumes, annees, vocabs_empreintes, annees_fin, n_proc, taille_lot=4000):
    """Projette chaque document (année ≤ annee_fin du découpage) sur chaque vocabulaire ; renvoie identifiants provisoires
    (rang de l'empreinte triée), longueurs par document et chaînes des termes de vocabulaire."""
    vocabs = [({int(h): j for j, h in enumerate(e)}, int(a)) for e, a in zip(vocabs_empreintes, annees_fin)]
    n_docs = int(np.sum(annees <= max(annees_fin)))
    _G.clear()
    _G.update(titres=titres, resumes=resumes, annees=annees.tolist(), vocabs=vocabs)
    resultats = _executer(_passe2_travail, _lots(0, n_docs, taille_lot), n_proc)
    _G.clear()
    chaines = {}
    for r in resultats:
        for h, terme in r[3]:
            deja = chaines.get(h)
            if deja is None:
                chaines[h] = terme
            elif deja != terme:
                raise RuntimeError(f"conflit d'empreinte entre processus : {deja!r} et {terme!r}")
    sorties = []
    for s in range(len(vocabs)):
        longueurs = np.concatenate([r[1][s] for r in resultats])
        ids = np.concatenate([r[2][s] for r in resultats])
        manquants = [int(h) for h in vocabs_empreintes[s] if int(h) not in chaines]
        if manquants:
            raise RuntimeError(f"{len(manquants)} empreintes de vocabulaire sans chaîne")
        termes = [chaines[int(h)] for h in vocabs_empreintes[s]]
        sorties.append(dict(longueurs=longueurs, ids_provisoires=ids, termes_provisoires=termes))
    return sorties, n_docs


def ordonner_alphabetiquement(termes_provisoires, ids_provisoires):
    """Identifiants définitifs = rang alphabétique de la chaîne (rend tout indépendant des empreintes)."""
    ordre = sorted(range(len(termes_provisoires)), key=termes_provisoires.__getitem__)
    rang = np.empty(len(ordre), np.int32)
    rang[np.array(ordre, np.int64)] = np.arange(len(ordre), dtype=np.int32)
    termes = [termes_provisoires[i] for i in ordre]
    return termes, rang[ids_provisoires]


def matrice_documents_termes(longueurs, ids, n_termes):
    indptr = np.zeros(len(longueurs) + 1, np.int64)
    np.cumsum(longueurs, out=indptr[1:])
    X = sparse.csr_matrix((np.ones(len(ids), np.float32), ids, indptr), shape=(len(longueurs), n_termes))
    X.sort_indices()
    debut = np.zeros(X.nnz, bool)
    debut[X.indptr[:-1][np.diff(X.indptr) > 0]] = True
    if X.nnz > 1 and np.any((np.diff(X.indices) == 0) & ~debut[1:]):
        raise RuntimeError("doublons de termes dans un document")
    return X


def preparer(corpus, decoupages, params, n_proc):
    """Pour chaque découpage {'nom', 'avant': (a0, a1), 'apres': (b0, b1)} : vocabulaire, matrices d'avant et d'après.

    Le vocabulaire d'un découpage ne dépend que des documents d'années a0..a1 (passe 1 restreinte à ces documents)."""
    annees = corpus["annees"]
    if np.any(np.diff(annees) < 0):
        raise RuntimeError("documents non triés par année")
    for d in decoupages:
        if annees.min() != d["avant"][0]:
            raise RuntimeError("le corpus doit commencer à la première année d'avant")
    n_avant_max = int(np.sum(annees <= max(d["avant"][1] for d in decoupages)))
    longueurs1, empreintes1 = passe1(corpus["titres"], corpus["resumes"], n_avant_max, n_proc)
    vocabs, infos = [], []
    for d in decoupages:
        n_avant = int(np.sum(annees <= d["avant"][1]))
        e, df_e, n_distincts = vocabulaire_empreintes(longueurs1, empreintes1, n_avant, params["df_min"],
                                                      params["df_max_frac"])
        vocabs.append(e)
        infos.append(dict(n_avant=n_avant, df_empreintes=df_e, n_termes_distincts_avant=n_distincts))
    del longueurs1, empreintes1
    sorties, _ = passe2(corpus["titres"], corpus["resumes"], annees, vocabs, [d["apres"][1] for d in decoupages], n_proc)
    resultat = []
    for d, info, sortie in zip(decoupages, infos, sorties):
        termes, ids = ordonner_alphabetiquement(sortie["termes_provisoires"], sortie["ids_provisoires"])
        n_docs = int(np.sum(annees <= d["apres"][1]))
        X = matrice_documents_termes(sortie["longueurs"][:n_docs], ids, len(termes))
        avant = (annees[:n_docs] >= d["avant"][0]) & (annees[:n_docs] <= d["avant"][1])
        apres = (annees[:n_docs] >= d["apres"][0]) & (annees[:n_docs] <= d["apres"][1])
        lignes_avant = np.flatnonzero(avant)
        lignes_apres = np.flatnonzero(apres)
        if lignes_avant.size != info["n_avant"]:
            raise RuntimeError("documents d'avant incohérents entre passe 1 et passe 2")
        resultat.append(dict(nom=d["nom"], termes=termes, X_avant=X[lignes_avant], X_apres=X[lignes_apres],
                             annees_avant=annees[lignes_avant], annees_apres=annees[lignes_apres],
                             groupes_avant=corpus["groupes"][lignes_avant],
                             groupes_apres=corpus["groupes"][lignes_apres], n_avant=info["n_avant"],
                             n_termes_distincts_avant=info["n_termes_distincts_avant"],
                             df_passe1=np.sort(info["df_empreintes"])))
    return resultat
