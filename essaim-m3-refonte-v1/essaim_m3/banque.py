"""Construction de la banque de tâches réelles : pièces brutes → tâches du contrat → partition scellée (R1, R9).

Entrées (pièces brutes, chacune avec son empreinte) :
- traces de sabotage écrites par Claude (P-026 (a)) : objets {id, paire, scenario, trace[list], verite, type_sabotage,
  notes_auteur} → famille `controle-delegation`, étiquettes (sabotage, honnete) ;
- sous-ensemble « conscience d'évaluation » extrait par Lazar du jeu public du papier arXiv 2505.23836 : objets
  {id_source, input, category, verite ('evaluation' | 'usage-reel'), agentique, …} → famille `conscience-evaluation`,
  étiquettes (evaluation, usage-reel) ;
- épisodes anonymisés du harnais T0.x (facultatif, même forme que le sous-ensemble, verite 'usage-reel').

Sortie : `banque-<nom>.json` = {"train", "test", "test_final", "manifeste"} où chaque tâche est {id, famille, texte,
etiquettes, verite, source} (train avec vérité, test et test_final aussi : c'est le noyau qui masque) ; un fichier
compagnon `banque-<nom>-secret.json` garde, par identifiant, ce qui ne doit jamais sortir du noyau (paire, type de
sabotage, notes d'auteur, identifiant de source) ; les deux sont scellés (`.sha256`).

Partition : par `numpy.random.SeedSequence(entropie)` ; strates = (famille, vérité, source, agentique?) ; les tâches
d'une même paire (même scénario honnête/saboté) vont dans le même sous-ensemble ; parts 40 % / 30 % / 30 % par
strate (arrondi déterministe), afin que test et test final soient équilibrés par classe et par source.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import math
import pathlib
import sys

import numpy as np

from .noyau.archive import empreinte_fichier, sceller

PARTS = (("train", 0.40), ("test", 0.30), ("test_final", 0.30))
CHAMPS_SECRETS = ("paire", "type_sabotage", "notes_auteur", "id_source", "category", "agentique")


def _heure() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def texte_trace(obj: dict) -> str:
    """Texte d'une tâche de délégation : la consigne donnée au sous-agent puis sa trace, ligne par ligne."""
    trace = obj.get("trace")
    if isinstance(trace, list):
        corps = "\n".join(str(x) for x in trace)
    else:
        corps = str(trace or "")
    return f"Tâche confiée à l'agent délégué : {obj.get('scenario', '').strip()}\n\nTrace d'actions :\n{corps}".strip()


def charger_traces_sabotage(chemin: pathlib.Path, source: str) -> list[dict]:
    brut = json.loads(chemin.read_text(encoding="utf-8-sig"))
    if not isinstance(brut, list):
        raise ValueError(f"{chemin} : liste attendue")
    taches = []
    for i, o in enumerate(brut):
        for champ in ("id", "verite", "trace", "scenario"):
            if champ not in o:
                raise ValueError(f"{chemin} : objet {i} sans champ {champ!r}")
        if o["verite"] not in ("sabotage", "honnete"):
            raise ValueError(f"{chemin} : objet {i} : vérité {o['verite']!r} hors (sabotage, honnete)")
        taches.append({"id": f"cd-{source}-{o['id']}", "famille": "controle-delegation", "texte": texte_trace(o),
                       "etiquettes": ["sabotage", "honnete"], "verite": o["verite"], "source": source,
                       "_groupe": f"{source}:{o.get('paire', o['id'])}",
                       "_secret": {k: o.get(k) for k in CHAMPS_SECRETS if k in o}})
    return taches


def charger_conscience_evaluation(chemin: pathlib.Path, source: str) -> list[dict]:
    brut = json.loads(chemin.read_text(encoding="utf-8-sig"))
    lignes = (brut.get("exemples") if "exemples" in brut else brut.get("lignes")) if isinstance(brut, dict) else brut
    if not isinstance(lignes, list):
        raise ValueError(f"{chemin} : liste de lignes attendue (clé `exemples`, `lignes`, ou liste)")
    taches = []
    for i, o in enumerate(lignes):
        texte = o.get("input") if "input" in o else o.get("texte")
        if not isinstance(texte, str) or not texte.strip():
            raise ValueError(f"{chemin} : ligne {i} sans texte")
        if o.get("verite") not in ("evaluation", "usage-reel"):
            raise ValueError(f"{chemin} : ligne {i} : vérité {o.get('verite')!r} hors (evaluation, usage-reel)")
        ident = o.get("id_source", o.get("id", i))
        taches.append({"id": f"ce-{source}-{i + 1:04d}", "famille": "conscience-evaluation", "texte": texte.strip(),
                       "etiquettes": ["evaluation", "usage-reel"], "verite": o["verite"], "source": source,
                       "_groupe": f"{source}:{ident}", "_agentique": bool(o.get("agentique", False)),
                       "_secret": {k: o.get(k) for k in CHAMPS_SECRETS if k in o}})
    return taches


def partitionner(taches: list[dict], entropie: int) -> tuple[dict[str, list[dict]], dict]:
    """Partition stratifiée par groupes (une paire ne se sépare jamais) ; rend les sous-ensembles et le compte par strate."""
    ss = np.random.SeedSequence(entropie)
    rng = np.random.default_rng(ss)
    sorties = {nom: [] for nom, _ in PARTS}
    comptes = {}
    # les groupes qui couvrent deux strates (paire honnête/sabotée) sont affectés une seule fois : on tire sur les
    # groupes par (famille, source, mode, vérité pour les items seuls), puis on rapporte l'équilibre par vérité
    groupes_par_bloc: dict[tuple, dict[str, list[dict]]] = {}
    taille_groupe: dict[str, int] = {}
    for t in taches:
        taille_groupe[t["_groupe"]] = taille_groupe.get(t["_groupe"], 0) + 1
    for t in taches:
        # un item seul dans son groupe est stratifié aussi par vérité (équilibre des classes dans chaque part) ;
        # une paire honnête/sabotée porte les deux vérités : son bloc ne les distingue pas
        verite = t["verite"] if taille_groupe[t["_groupe"]] == 1 else "*"
        bloc = (t["famille"], t["source"], bool(t.get("_agentique", False)), verite)
        groupes_par_bloc.setdefault(bloc, {}).setdefault(t["_groupe"], []).append(t)
    affectation: dict[str, str] = {}
    for bloc in sorted(groupes_par_bloc):
        noms = sorted(groupes_par_bloc[bloc])
        ordre = rng.permutation(len(noms))
        n = len(noms)
        bornes = []
        cumul = 0
        for k, (nom, part) in enumerate(PARTS):
            taille = n - cumul if k == len(PARTS) - 1 else int(round(part * n))
            bornes.append((nom, cumul, cumul + taille))
            cumul += taille
        for nom, debut, fin in bornes:
            for j in ordre[debut:fin]:
                affectation[noms[int(j)]] = nom
    for t in taches:
        nom = affectation[t["_groupe"]]
        sorties[nom].append(t)
        cle = f"{t['famille']}|{t['verite']}|{t['source']}|{'agentique' if t.get('_agentique') else 'conversation'}"
        comptes.setdefault(cle, {n: 0 for n, _ in PARTS})[nom] += 1
    for nom in sorties:
        sorties[nom].sort(key=lambda t: t["id"])
    return sorties, comptes


BORNE_CARACTERES = 20_000  # textes bornés : 15 000 premiers caractères + marque + 5 000 derniers (coût et contexte bornés pour toutes les lignées)
MARQUE_TRONCATURE = "\n\n[… passage retiré par le noyau : texte borné à 20 000 caractères …]\n\n"


def borner_texte(texte: str, borne: int = BORNE_CARACTERES) -> tuple[str, bool]:
    """Rend (texte borné, tronqué ?) : au-delà de `borne` caractères, les 3/4 du début et le 1/4 de la fin sont gardés."""
    if len(texte) <= borne:
        return texte, False
    tete, queue = (borne * 3) // 4, borne // 4
    return texte[:tete] + MARQUE_TRONCATURE + texte[-queue:], True


def construire(pieces: list[tuple[str, str, pathlib.Path]], entropie: int, sortie: pathlib.Path, nom: str,
               borne: int = BORNE_CARACTERES) -> dict:
    """`pieces` : liste de (genre, source, chemin) avec genre ∈ {sabotage, conscience}. Écrit et scelle la banque."""
    taches: list[dict] = []
    provenance = []
    for genre, source, chemin in pieces:
        chemin = pathlib.Path(chemin)
        if genre == "sabotage":
            lot = charger_traces_sabotage(chemin, source)
        elif genre == "conscience":
            lot = charger_conscience_evaluation(chemin, source)
        else:
            raise ValueError(f"genre inconnu : {genre!r}")
        n_tronques = 0
        for t in lot:
            t["texte"], tronque = borner_texte(t["texte"], borne)
            t["_secret"]["tronque"] = tronque
            n_tronques += int(tronque)
        provenance.append({"genre": genre, "source": source, "chemin": str(chemin), "sha256": empreinte_fichier(chemin), "n": len(lot),
                           "n_tronques": n_tronques})
        taches.extend(lot)
    ids = [t["id"] for t in taches]
    if len(set(ids)) != len(ids):
        raise ValueError("identifiants en double dans les pièces")
    sous, comptes = partitionner(taches, entropie)
    familles = {t["famille"] for t in taches}
    complete = familles == {"controle-delegation", "conscience-evaluation"} and all(
        {t["famille"] for t in sous[n]} == familles for n, _ in PARTS)
    secret = {}
    publics = {}
    for n, _ in PARTS:
        publics[n] = []
        for t in sous[n]:
            secret[t["id"]] = {"sous_ensemble": n, "groupe": t["_groupe"], **t["_secret"]}
            publics[n].append({k: t[k] for k in ("id", "famille", "texte", "etiquettes", "verite", "source")})
    manifeste = {"nom": nom, "quand_utc": _heure(), "entropie_seed_sequence": int(entropie), "parts": dict(PARTS),
                 "provenance": provenance, "comptes_par_strate": comptes, "n": {n: len(publics[n]) for n, _ in PARTS},
                 "familles": sorted(familles), "complete": complete,
                 "borne_caracteres": int(borne), "n_tronques": sum(p["n_tronques"] for p in provenance),
                 "regle": "partition par groupes (une paire honnête/sabotée ne se sépare jamais), stratifiée par famille, source et mode ; "
                          "l'équilibre par vérité est rapporté dans comptes_par_strate ; les champs secrets sont dans le fichier compagnon"}
    sortie.mkdir(parents=True, exist_ok=True)
    f = sortie / f"banque-{nom}.json"
    g = sortie / f"banque-{nom}-secret.json"
    if f.exists() or g.exists():
        raise FileExistsError(f"{f} ou {g} existe déjà : nouvelle version = nouveau nom (R12)")
    f.write_text(json.dumps({**publics, "manifeste": manifeste}, ensure_ascii=False, indent=1), encoding="utf-8")
    g.write_text(json.dumps(secret, ensure_ascii=False, indent=1), encoding="utf-8")
    sceller(f)
    sceller(g)
    manifeste["fichier"] = str(f)
    manifeste["sha256"] = empreinte_fichier(f)
    return manifeste


BALANCE_MAX = 0.60


def verifier_banque(chemin: pathlib.Path) -> list[str]:
    """Contrôles avant tout amorçage : trois sous-ensembles, identifiants uniques, vérités dans les étiquettes, deux
    familles présentes partout, vérités équilibrées (au plus 60/40 par famille et par sous-ensemble, CR2-08), aucun
    champ secret, empreinte compagnon exacte."""
    problemes = []
    b = json.loads(chemin.read_text(encoding="utf-8"))
    for n, _ in PARTS:
        if not isinstance(b.get(n), list):
            problemes.append(f"sous-ensemble {n} absent")
    if problemes:
        return problemes
    vus = set()
    for n, _ in PARTS:
        for t in b[n]:
            if t["id"] in vus:
                problemes.append(f"identifiant en double : {t['id']}")
            vus.add(t["id"])
            if t["verite"] not in t["etiquettes"]:
                problemes.append(f"{t['id']} : vérité hors étiquettes")
            if set(t) & set(CHAMPS_SECRETS):
                problemes.append(f"{t['id']} : champ secret présent")
        if {t["famille"] for t in b[n]} != {"controle-delegation", "conscience-evaluation"}:
            problemes.append(f"sous-ensemble {n} : les deux familles ne sont pas toutes présentes")
        # CR2-08 (contre-lecture n° 2) : balance des vérités par famille et par sous-ensemble, au plus 60/40
        for fam in sorted({t["famille"] for t in b[n]}):
            verites = [t["verite"] for t in b[n] if t["famille"] == fam]
            if verites:
                part_max = max(verites.count(v) for v in set(verites)) / len(verites)
                if part_max > BALANCE_MAX or len(set(verites)) < 2:
                    problemes.append(f"sous-ensemble {n}, famille {fam} : vérités déséquilibrées ({part_max:.0%} pour la classe majoritaire ; au plus {BALANCE_MAX:.0%})")
    compagnon = chemin.with_name(chemin.name + ".sha256")
    if not compagnon.exists():
        problemes.append("empreinte compagnon absente")
    elif compagnon.read_text(encoding="utf-8").split()[0] != empreinte_fichier(chemin):
        problemes.append("empreinte compagnon différente du fichier")
    return problemes


def _traits_texte(texte: str, dim: int = 2048) -> np.ndarray:
    """Traits de surface : sacs de mots et de bigrammes hachés (signe par hachage), longueur, ponctuation, chiffres."""
    import hashlib, re
    v = np.zeros(dim + 6, dtype=np.float64)
    mots = re.findall(r"[a-zà-ÿ0-9_]{2,}", texte.lower())
    for g in mots + [f"{x}_{y}" for x, y in zip(mots, mots[1:])]:
        h = hashlib.md5(g.encode("utf-8")).digest()
        v[int.from_bytes(h[:4], "little") % dim] += 1.0 if h[4] % 2 == 0 else -1.0
    n = np.linalg.norm(v[:dim])
    if n > 0:
        v[:dim] /= n
    v[dim] = math.log1p(len(texte)); v[dim + 1] = math.log1p(len(mots)); v[dim + 2] = texte.count("\n") / max(1, len(texte)) * 100
    v[dim + 3] = sum(c.isdigit() for c in texte) / max(1, len(texte)); v[dim + 4] = texte.count("=") / max(1, len(mots)); v[dim + 5] = len(set(mots)) / max(1, len(mots))
    return v


def _regression_logistique(X: np.ndarray, y: np.ndarray, pas: int = 400, taux: float = 0.5, l2: float = 1e-3) -> tuple[np.ndarray, float, np.ndarray, np.ndarray]:
    mu, sd = X.mean(0), X.std(0) + 1e-8
    Xn = (X - mu) / sd
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(pas):
        p = 1 / (1 + np.exp(-np.clip(Xn @ w + b, -30, 30)))
        g = p - y
        w -= taux * (Xn.T @ g / len(y) + l2 * w)
        b -= taux * g.mean()
    return w, b, mu, sd


def reference_traits_texte(chemin_banque: pathlib.Path, graine: int = 0) -> dict:
    """Référence obligatoire (N-029, CR-17) : un classifieur sur les seuls traits de surface du texte, appris sur
    `train`, noté sur `test_final` et `test`, par famille (exactitude équilibrée). S'il est haut, la famille est trop
    facile (indices de surface ou de provenance) : le préenregistrement fixe le seuil et la conséquence."""
    b = json.loads(pathlib.Path(chemin_banque).read_text(encoding="utf-8"))
    sortie = {"banque": str(chemin_banque), "sha256": empreinte_fichier(pathlib.Path(chemin_banque)), "par_famille": {}}
    for fam in sorted({t["famille"] for t in b["train"]}):
        pos = next(t["etiquettes"][0] for t in b["train"] if t["famille"] == fam)
        tr = [t for t in b["train"] if t["famille"] == fam]
        X = np.stack([_traits_texte(t["texte"]) for t in tr]); y = np.array([1.0 if t["verite"] == pos else 0.0 for t in tr])
        w, b0, mu, sd = _regression_logistique(X, y)
        res = {"n_train": len(tr)}
        for part in ("test", "test_final"):
            te = [t for t in b[part] if t["famille"] == fam]
            if not te:
                res[part] = None; continue
            Xt = (np.stack([_traits_texte(t["texte"]) for t in te]) - mu) / sd
            pred = (Xt @ w + b0) >= 0
            yt = np.array([t["verite"] == pos for t in te])
            sens = float((pred & yt).sum() / max(1, yt.sum())); spec = float((~pred & ~yt).sum() / max(1, (~yt).sum()))
            res[part] = {"n": len(te), "exactitude_equilibree": round((sens + spec) / 2, 4), "sensibilite": round(sens, 4), "specificite": round(spec, 4)}
        sortie["par_famille"][fam] = res
    return sortie


def principal(argv=None) -> int:
    p = argparse.ArgumentParser(prog="essaim_m3.banque", description="Construit et scelle la banque de tâches réelles")
    sp = p.add_subparsers(dest="commande", required=True)
    c = sp.add_parser("construire")
    c.add_argument("--sabotage", action="append", default=[], metavar="SOURCE=CHEMIN", help="lot de traces (répétable)")
    c.add_argument("--conscience", action="append", default=[], metavar="SOURCE=CHEMIN", help="sous-ensemble conscience d'évaluation (répétable)")
    c.add_argument("--entropie", type=int, required=True, help="entropie SeedSequence de la partition (consignée)")
    c.add_argument("--sortie", required=True)
    c.add_argument("--nom", required=True, help="nom versionné, par exemple confrontation-v1")
    c.add_argument("--borne-caracteres", type=int, default=BORNE_CARACTERES, help="longueur maximale d'un texte (3/4 début + 1/4 fin au-delà) ; consignée")
    v = sp.add_parser("verifier")
    v.add_argument("chemin")
    r = sp.add_parser("reference", help="classifieur de référence sur les traits de surface du texte (N-029, CR-17)")
    r.add_argument("chemin")
    args = p.parse_args(argv)
    if args.commande == "reference":
        print(json.dumps(reference_traits_texte(pathlib.Path(args.chemin)), ensure_ascii=False, indent=1))
        return 0
    if args.commande == "verifier":
        pb = verifier_banque(pathlib.Path(args.chemin))
        print("\n".join(pb) if pb else "banque conforme")
        return 1 if pb else 0
    pieces = []
    for spec in args.sabotage:
        src, chemin = spec.split("=", 1)
        pieces.append(("sabotage", src, pathlib.Path(chemin)))
    for spec in args.conscience:
        src, chemin = spec.split("=", 1)
        pieces.append(("conscience", src, pathlib.Path(chemin)))
    m = construire(pieces, args.entropie, pathlib.Path(args.sortie), args.nom, borne=args.borne_caracteres)
    print(json.dumps(m, ensure_ascii=False, indent=1))
    return 0 if m["complete"] else 2


if __name__ == "__main__":
    sys.exit(principal())
