"""Contre-lecture banque v2 — c1 : équivalence v1 -> v2, par un code indépendant du constructeur et du vérificateur.

Lecture seule des fichiers de la banque ; rien n'est écrit hors de la sortie standard.
Usage : python3 -I c1_equivalence_v1.py DOSSIER_BANQUE
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

ATTENDU = {
    "banque-confrontation-v1.json": "f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc",
    "banque-confrontation-v1-secret.json": "c68d7d4ba34b49b85a9327adfe21d30cc8118f1d100a47db2a47e97329715caf",
    "banque-confrontation-v2.json": "52beb637823b72f475fd1ddcf446e9b79cafa5d2cd47d16c08b663d2b9388d10",
    "banque-confrontation-v2-secret.json": "1775a9e09f6620064769bf7c7a46d4f53a69e8cb1f886377dc5fd886d9d629fa",
}
E_ECRIT = 14234892761277461467225772596104759309
PARTS = ("train", "test", "test_final")

ecarts = []


def note(ok, msg):
    print(("OK    " if ok else "ECART ") + msg)
    if not ok:
        ecarts.append(msg)


def h(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main(d):
    d = pathlib.Path(d)
    # 1. empreintes : fichier, compagnon, valeur attendue (LISEZMOI-v3 / v4)
    for nom, att in ATTENDU.items():
        p = d / nom
        c = p.with_name(nom + ".sha256")
        hh = h(p)
        comp = c.read_text(encoding="utf-8").split()
        note(hh == att, f"{nom} : sha256 {hh[:16]}… attendu {att[:16]}…")
        note(comp[:2] == [hh, nom], f"{nom}.sha256 : compagnon {comp[:2]}")
    # EMPREINTES-banque-v2-v1.txt
    em = d / "EMPREINTES-banque-v2-v1.txt"
    note(em.with_name(em.name + ".sha256").read_text(encoding="utf-8").split()[0] == h(em), "EMPREINTES-banque-v2-v1.txt : compagnon")
    for ligne in em.read_text(encoding="utf-8").splitlines():
        if not ligne.strip():
            continue
        hh, chemin = ligne.split(None, 1)
        p = d / chemin.strip()
        note(p.is_file() and h(p) == hh, f"EMPREINTES : {chemin.strip()} {hh[:16]}…")
        c = p.with_name(p.name + ".sha256")
        note(c.is_file() and c.read_text(encoding="utf-8").split()[0] == hh, f"EMPREINTES : compagnon de {chemin.strip()}")

    v1 = json.loads((d / "banque-confrontation-v1.json").read_text(encoding="utf-8"))
    s1 = json.loads((d / "banque-confrontation-v1-secret.json").read_text(encoding="utf-8"))
    v2 = json.loads((d / "banque-confrontation-v2.json").read_text(encoding="utf-8"))
    s2 = json.loads((d / "banque-confrontation-v2-secret.json").read_text(encoding="utf-8"))

    # 2. structure et clés
    note(list(v1) == ["train", "test", "test_final", "manifeste"], f"v1 clés de tête {list(v1)}")
    note(list(v2) == ["train", "test", "test_final", "manifeste"], f"v2 clés de tête {list(v2)}")
    for p in PARTS:
        note(len(v1[p]) == len(v2[p]), f"{p} : {len(v1[p])} tâches v1, {len(v2[p])} v2")

    # 3. permutation recalculée depuis E (manifeste v2 et LISEZMOI-v4)
    man2 = v2["manifeste"]
    E = man2["identifiants_opaques"]["entropie_seed_sequence"]
    note(E == E_ECRIT, f"E du manifeste v2 = E écrit au LISEZMOI-v4 ({E})")
    note(0 <= E < 2 ** 128, f"E < 2^128 (secrets.randbits(128) possible) : {E.bit_length()} bits")
    perm = np.random.default_rng(np.random.SeedSequence(E)).permutation(200)
    taches1 = [(p, t) for p in PARTS for t in v1[p]]
    taches2 = [(p, t) for p in PARTS for t in v2[p]]
    attendus = [f"t-{int(perm[i]) + 1:04d}" for i in range(200)]
    note([t["id"] for _, t in taches2] == attendus, "identifiants v2 = t-{permutation[i]+1:04d}, rang i dans l'ordre v1 (train, test, test_final)")
    note(sorted(attendus) == [f"t-{k:04d}" for k in range(1, 201)], "identifiants v2 = exactement t-0001 … t-0200")

    # 4. champs, parts, ordre, valeurs
    n_diff = 0
    for (p1, t1), (p2, t2) in zip(taches1, taches2):
        if p1 != p2:
            n_diff += 1
        if list(t1) != ["id", "famille", "texte", "etiquettes", "verite", "source"]:
            n_diff += 1
        if list(t2) != list(t1):
            n_diff += 1
        for k in ("famille", "texte", "etiquettes", "verite", "source"):
            if t1[k] != t2[k] or type(t1[k]) is not type(t2[k]):
                n_diff += 1
    note(n_diff == 0, f"mêmes parts, même ordre, mêmes champs (et ordre des clés), mêmes valeurs à chaque rang : {n_diff} écart(s)")
    ids1 = {t["id"] for _, t in taches1}
    note(not (ids1 & set(attendus)), "aucun identifiant commun v1 / v2")

    # 5. secret v2 = secret v1 + id_v1, même ordre de clés
    note(list(s2) == attendus, "clés du secret v2 = identifiants v2, dans l'ordre du fichier")
    n_s = 0
    for (_, t1), nid in zip(taches1, attendus):
        dos = s2[nid]
        attendu = dict(s1[t1["id"]])
        attendu["id_v1"] = t1["id"]
        if dos != attendu or list(dos) != list(attendu):
            n_s += 1
    note(n_s == 0, f"secret v2[id] = secret v1[id_v1] + id_v1 (valeurs et ordre des clés) : {n_s} écart(s)")
    note(set(s1) == ids1, "secret v1 couvre exactement la v1")
    cles_s1 = sorted({k for v in s1.values() for k in v})
    print(f"INFO  clés du secret v1 : {cles_s1}")

    # 6. manifeste v2 = manifeste v1 sauf nom, quand_utc, identifiants_opaques
    man1 = v1["manifeste"]
    diff = sorted(k for k in set(man1) | set(man2) if man1.get(k) != man2.get(k))
    note(diff == ["identifiants_opaques", "nom", "quand_utc"], f"clés du manifeste qui diffèrent : {diff}")
    note([k for k in man2 if k != "identifiants_opaques"] == list(man1), "ordre des clés du manifeste conservé")
    io = man2["identifiants_opaques"]
    note(io["derivee_de"]["sha256"] == ATTENDU["banque-confrontation-v1.json"] and io["derivee_de"]["secret_sha256"] == ATTENDU["banque-confrontation-v1-secret.json"],
         "identifiants_opaques.derivee_de : empreintes v1 et secret v1")
    print(f"INFO  manifeste v2 : nom={man2['nom']} quand_utc={man2['quand_utc']} numpy={io.get('numpy')} script={io.get('script')}")
    print(f"INFO  manifeste v1 : nom={man1['nom']} quand_utc={man1['quand_utc']} entropie partition={man1.get('entropie_seed_sequence')}")
    print(f"INFO  numpy de cette contre-lecture : {np.__version__}")

    # 7. reconstruction octet à octet (sérialisation du constructeur : json indent=1, ensure_ascii=False, + "\n")
    rv2 = {p: [] for p in PARTS}
    rs2 = {}
    for (p, t), nid in zip(taches1, attendus):
        rv2[p].append({"id": nid, "famille": t["famille"], "texte": t["texte"], "etiquettes": t["etiquettes"],
                       "verite": t["verite"], "source": t["source"]})
        dd = dict(s1[t["id"]])
        dd["id_v1"] = t["id"]
        rs2[nid] = dd
    rman = dict(man1)
    rman["nom"] = "confrontation-v2"
    rman["quand_utc"] = man2["quand_utc"]  # seule valeur reprise du fichier : l'heure de construction
    rman["identifiants_opaques"] = io      # contenu vérifié au point 6
    rv2["manifeste"] = rman
    octets = (json.dumps(rv2, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    octets_s = (json.dumps(rs2, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    note(hashlib.sha256(octets).hexdigest() == ATTENDU["banque-confrontation-v2.json"], "v2 reconstruite depuis v1 + E : mêmes octets que 52beb637…")
    note(hashlib.sha256(octets_s).hexdigest() == ATTENDU["banque-confrontation-v2-secret.json"], "secret v2 reconstruit depuis secret v1 : mêmes octets que 1775a9e0…")

    # 8. ordre du fichier : suit-il la vérité ? (ordre v1 gardé)
    for p in PARTS:
        ids_v1 = [t["id"] for t in v1[p]]
        note(ids_v1 == sorted(ids_v1), f"{p} : ordre v1 = tri par identifiant v1")
        motif = "".join(("H" if t["verite"] == "honnete" else "S") if t["famille"] == "controle-delegation"
                        else ("e" if t["verite"] == "evaluation" else "u") for t in v2[p])
        print(f"INFO  {p} (v2, ordre du fichier) : {motif}")
    print(f"\n{len(ecarts)} écart(s)")
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
