"""Plomberie des corrections CLA (CLA-09 : retrait de `nr` et `concepts_absents` de la vue observée) : empreinte de
chaque monde d'essai, 14 conditions v2 et les deux conditions NR, indices 980000 à 980059 (RACINE_VALIDATION, hors
plages du § 7), pour comparer le code d'avant (version-v2-avant-cla, complétée des modules inchangés) et le code
corrigé. Deux empreintes par monde :
  - « latents » : mo.empreinte_latents (conditions v2) ou graine v1, champs, vrais et plantés (NR) ;
  - « obs_hors_cla » : TOUS les champs de la vue observée (__slots__) sauf `_fige`, `nr` et `concepts_absents`,
    sérialisés de façon déterministe (cos par octets, df trié).
Plus tentatives et replantations. Ne lit que des égalités et comptes ; aucun bras n'est exécuté.
Usage (depuis experience-v2/, T = ../../trancher-recombinaison, chemin absolu) :
  avant : PYTHONPATH=<dépôt>/src:$PWD:$T python3 -B plomberie-corrections-v2/identite_avant_apres_cla_v1.py version-v2-avant-cla identite-avant-cla-resultats-v1.json
  après : PYTHONPATH=<dépôt>/src python3 -B plomberie-corrections-v2/identite_avant_apres_cla_v1.py . identite-apres-cla-resultats-v1.json
(version-v2-avant-cla ne contient que les modules modifiés : les autres viennent de $PWD, inchangés.)"""
import hashlib
import json
import sys
from pathlib import Path

D = str(Path(sys.argv[1]).resolve())
sys.path.insert(0, D)
import graines_v2 as gr  # noqa: E402
import monde_v2 as mo  # noqa: E402

RETIRES = {"_fige", "nr", "concepts_absents"}


def empreinte_obs(o):
    h = hashlib.sha256()
    for nom in mo.Obs.__slots__:
        if nom in RETIRES:
            continue
        v = object.__getattribute__(o, nom)
        h.update(nom.encode())
        if nom == "cos":
            h.update(v.tobytes())
        elif nom == "df":
            h.update(json.dumps(sorted(dict(v).items())).encode())
        elif nom in ("etiq_op", "etiq_co"):
            h.update(json.dumps([sorted(x) for x in v]).encode())
        else:
            h.update(json.dumps(v, default=str).encode())
    return h.hexdigest()


def empreinte_lat(w, nr):
    L = w.latent(mo.JETON_MESURE)
    if not nr:
        return mo.empreinte_latents(w)
    corps = {"graine_v1": L.graine_v1, "champ": L.champ, "vrais": sorted(L.vrais), "plantes": L.plantes,
             "plante": sorted(L.plante.items())}
    return hashlib.sha256(json.dumps(corps, sort_keys=True, default=str).encode()).hexdigest()


out = {}
for cond in list(mo.CONDITIONS_V2) + ["NR_bien", "NR_moyen"]:
    nr = cond.startswith("NR_")
    for i in range(980000, 980060):
        w = mo.generer(cond, gr.RACINE_VALIDATION, i)
        L = w.latent(mo.JETON_MESURE)
        out[f"{cond}|{i}"] = {"latents": empreinte_lat(w, nr), "obs_hors_cla": empreinte_obs(w.obs),
                              "tentatives": L.tentatives, "replantations": L.replantations}
Path(sys.argv[2]).write_text(json.dumps(out, sort_keys=True, indent=0), encoding="utf-8")
print(len(out), "mondes")
