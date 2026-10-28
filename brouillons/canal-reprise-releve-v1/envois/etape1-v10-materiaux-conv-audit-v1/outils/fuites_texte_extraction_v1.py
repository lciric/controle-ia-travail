"""Le texte donné au modèle à l'extraction des traits portait-il l'identifiant v1 ou autre chose qui livre la vérité ?
Rejoue, sans modèle, l'entrée de `extraire_activations_v2.py` (l. 153 : système = GABARIT_SYSTEME, utilisateur =
t["texte"]) et cherche dedans : l'identifiant de la tâche, tout identifiant de la banque, une marque -H/-S isolée, la
valeur de `source`, de chaque `etiquettes`, de `famille`, et la vérité en toutes lettres (comptes par famille, avec le
même compte pour la vérité de l'autre classe, pour séparer fuite et contenu). Compare enfin les textes de la v5 à ceux
de la v1 (empreinte du texte UTF-8). N'imprime AUCUNE valeur : seulement des comptes.
Écrit le 25 octobre 2026 (sous-agent conv-audit, étape 1 v10). Essais : --essai-artefact (injecte l'identifiant dans un
texte et la vérité dans un autre, sur une copie en mémoire ; les comptes doivent passer à 1).
Usage : python -I fuites_texte_extraction_v1.py BANQUE_V1.json BANQUE_V5.json [--essai-artefact]"""
import collections
import copy
import hashlib
import json
import pathlib
import re
import sys

GABARIT_SYSTEME = "Tu lis une trace ou un extrait d'interaction. Réponds ensuite aux questions posées."


def charger(chemin):
    p = pathlib.Path(chemin)
    if p.name.endswith(("-cle.json", "-secret.json")):
        sys.exit(f"refusé : {p.name}")
    return json.loads(p.read_bytes())


def taches(b):
    return [t for n in ("train", "test", "test_final") for t in b[n]]


def h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def controle(b, nom):
    ts = taches(b)
    ids = [str(t["id"]) for t in ts]
    verites = sorted({str(t["verite"]) for t in ts})  # jamais imprimées
    marque = re.compile(r"(?<![A-Za-z0-9])-[HS](?![A-Za-z0-9])")
    c = collections.Counter()
    par_famille = collections.defaultdict(collections.Counter)
    for t in ts:
        entree = GABARIT_SYSTEME + "\n" + str(t["texte"])
        ident = str(t["id"])
        c["taches"] += 1
        c["id_propre_dans_texte"] += ident in entree
        c["un_id_de_la_banque_dans_texte"] += any(i in entree for i in ids)
        c["marque_-H/-S_isolee"] += bool(marque.search(entree))
        c["source_dans_texte"] += bool(t.get("source")) and str(t["source"]) in entree
        c["une_etiquette_dans_texte"] += any(str(e) and str(e) in entree for e in (t.get("etiquettes") or []))
        c["famille_dans_texte"] += str(t["famille"]) in entree
        fam = par_famille[str(t["famille"])]
        fam["n"] += 1
        v = str(t["verite"])
        mot = lambda s: re.search(r"(?<![a-zà-ÿ0-9_])" + re.escape(s.lower()) + r"(?![a-zà-ÿ0-9_])", entree.lower()) is not None
        fam["sa_verite_en_toutes_lettres"] += mot(v)
        fam["verite_de_l_autre_classe_en_toutes_lettres"] += any(mot(a) for a in verites if a != v)
    print(f"== {nom} : {dict(c)}")
    print(f"   nombre de valeurs de vérité distinctes : {len(verites)} (non imprimées)")
    for f, d in sorted(par_famille.items()):
        print(f"   {f} : {dict(d)}")
    return c


def principal():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    v1, v5 = charger(args[0]), charger(args[1])
    if "--essai-artefact" in sys.argv:
        v1 = copy.deepcopy(v1)
        t0, t1 = v1["train"][0], v1["train"][1]
        t0["texte"] = t0["texte"] + "\n" + t0["id"]
        t1["texte"] = t1["texte"] + "\nverdict : " + t1["verite"]
        print("ESSAI SUR ARTEFACT : identifiant injecté dans 1 texte, vérité dans 1 autre")
    c1 = controle(v1, "v1 (entrée du modèle à l'extraction)")
    controle(v5, "v5")
    textes_v1 = collections.Counter(h(str(t["texte"])) for t in taches(v1))
    ts5 = taches(v5)
    communs = sum(h(str(t["texte"])) in textes_v1 for t in ts5)
    print(f"== textes v5 présents à l'identique dans la v1 : {communs} sur {len(ts5)} ; "
          f"textes v1 en double : {sum(n - 1 for n in textes_v1.values())}")
    ids1 = [str(t["id"]) for t in taches(v1)]
    print(f"== identifiants v1 cités dans un texte v5 : {sum(any(i in str(t['texte']) for i in ids1) for t in ts5)}")
    return 0 if (c1["id_propre_dans_texte"] == 0 and c1["un_id_de_la_banque_dans_texte"] == 0) else 2


if __name__ == "__main__":
    sys.exit(principal())
