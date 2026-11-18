"""Essais de l'outil de la session (session_pilote_mr2_v74_v1.sh et .py) — v1, sans réseau ni clé réelle : dépôt nu local (banc de
essai_amorce_v1.py), doublure de l'outil du loueur (écrite ici : `show instances`, `show user`, `create instance` qui consigne ses
arguments), clés factices. Usage : python3 essai_outil_session_v1.py DOSSIER_JETABLE SORTIE.json"""
import base64
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essai_amorce_v1 as EA  # noqa: E402

FACTICES = {"CONTROLE_IA_GITHUB_TOKEN_2": "jetonfactice_session_0123456789", "RR_ANTHROPIC_API_KEY_RIGAUD": "clefactice-anthropic-session-01",
            "GEMINI_API_KEY": "clefactice-gemini-session-0123", "OPENAI_API_KEY": "clefactice-openai-session-0123"}
DOUBLURE = r'''#!/usr/bin/env bash
case "$1 $2" in
  "show instances") cat "$DV/instances.json";;
  "show user") cat "$DV/user.json";;
  "create instance") printf '%s\n' "$@" > "$DV/create-args.txt"; echo '{"success": true, "new_contract": 777}';;
  *) echo "doublure : $*" >&2; exit 1;;
esac
'''


def main(argv):
    base, sortie = argv
    banc = EA.Banc(base)
    dv = os.path.join(base, "doublure-vastai")
    os.makedirs(dv)
    vf = os.path.join(dv, "vastai")
    open(vf, "w").write(DOUBLURE)
    os.chmod(vf, 0o755)
    envp = os.path.join(base, "envoi")
    os.makedirs(envp)
    cles_dans_liste = "clefactice-anthropic-session-01"

    def liste(insts):
        json.dump([dict(i, extra_env=[["RR_ANTHROPIC_API_KEY_RIGAUD", cles_dans_liste]]) for i in insts], open(os.path.join(dv, "instances.json"), "w"))

    def outil(*a, **kw):
        env = dict(os.environ, W=banc.session, ENVP=envp, VASTAI=vf, DV=dv, **kw.get("env", FACTICES))
        return subprocess.run(["bash", os.path.join(EA.CODE, "session_pilote_mr2_v74_v1.sh"), *a], env=env, capture_output=True, text=True)

    rech = os.path.join(envp, "recherche.json")
    json.dump([{"id": 11, "num_gpus": 0, "cpu_cores_effective": 4, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.15},
               {"id": 12, "num_gpus": 1, "gpu_name": "RTX 3060", "cpu_cores_effective": 8, "cpu_ram": 32000, "disk_space": 40, "dph_total": 0.12},
               {"id": 13, "num_gpus": 0, "cpu_cores_effective": 4, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.25},
               {"id": 14, "num_gpus": 0, "cpu_cores_effective": 2, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.05}], open(rech, "w"))
    cl, cp, cm = banc.commits["lot/compte-organisme-v1"], banc.commits["prep/pilote-mr2-compte-organisme-v1"], banc.commits["main"]
    bs, be, etiq = "calcul/pilote-mr2-v74-sortie-v1", "calcul/pilote-mr2-v74-entree-v1", "pilote-mr2-v74-20261115"
    cas = {}

    def note(nom, ok, detail=""):
        cas[nom] = {"conforme": bool(ok), "detail": detail[-300:]}
        print(f"{nom:40s} {'CONFORME' if ok else 'ÉCART'}", flush=True)

    for i, attendu in ((11, 0), (12, 2), (13, 2), (14, 2), (99, 2)):
        r = outil("offre", rech, str(i))
        note(f"offre {i} → {attendu}", r.returncode == attendu, r.stdout)
    r = outil("commande", rech, "11", cl, cp, cm, bs, be, etiq, env=dict(FACTICES, GEMINI_API_KEY=""))
    note("commande, clé absente → 2", r.returncode == 2 and "GEMINI_API_KEY absente" in r.stdout, r.stdout)
    r = outil("commande", rech, "12", cl, cp, cm, bs, be, etiq)
    note("commande, offre à carte → 2", r.returncode == 2, r.stdout)
    r = outil("commande", rech, "11", cl, cp, cm, bs, be, etiq)
    lignes = r.stdout.splitlines()
    cmd = "\n".join(lignes[-2:])
    ok = (r.returncode == 0 and lignes[-1].startswith("GO_ID=GO-2026-11-14-14 ") and lignes[-2].startswith('GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"')
          and not any(v in r.stdout for v in FACTICES.values()) and "$RR_ANTHROPIC_API_KEY_RIGAUD" in lignes[-1])
    b64 = lignes[-1].split("echo ", 1)[1].split(" | base64", 1)[0] if ok else ""
    ok = ok and base64.b64decode(b64) == open(os.path.join(EA.CODE, "amorce_pilote_mr2_v74_v1.sh"), "rb").read()
    note("commande conforme, aucune valeur imprimée", ok, r.stdout)
    # la commande imprimée, jouée avec la doublure à la place de l'outil du loueur : arguments reçus et sortie privée
    jouee = cmd.replace(vf, vf)
    rr = subprocess.run(["bash", "-c", jouee], env=dict(os.environ, DV=dv, **FACTICES), capture_output=True, text=True)
    args = open(os.path.join(dv, "create-args.txt")).read().splitlines() if os.path.exists(os.path.join(dv, "create-args.txt")) else []
    i_env = args.index("--env") + 1 if "--env" in args else None
    envs = args[i_env].split(" -e ") if i_env else []
    ok = (rr.returncode == 0 and "code=0" in rr.stdout and i_env is not None
          and f"GH_TOKEN={FACTICES['CONTROLE_IA_GITHUB_TOKEN_2']}" in args[i_env]
          and all(f"{k}={FACTICES[k]}" in args[i_env] for k in ("RR_ANTHROPIC_API_KEY_RIGAUD", "GEMINI_API_KEY", "OPENAI_API_KEY"))
          and args[args.index("--args") + 1] == "-c" and "base64 -d > /root/amorce_pilote_mr2_v74_v1.sh" in args[args.index("--args") + 2]
          and oct(os.stat(os.path.join(envp, "creation.json")).st_mode & 0o777) == "0o600" and len(envs) == 13)
    note("commande jouée sur doublure : arguments et --env justes, sortie 0600", ok, rr.stdout + rr.stderr + " | " + " ".join(a[:40] for a in args))
    os.unlink(os.path.join(dv, "create-args.txt"))
    r = outil("commande", rech, "11", cl, cp, cm, bs, be, etiq)
    meme = r.returncode == 0
    note("commande réimprimée : acceptée à la même échéance, refusée à une autre", (meme and "COMMANDE" in r.stdout) or (r.returncode == 2 and "echeance.txt existe déjà" in r.stdout), r.stdout)
    # création, inventaires, relecture
    liste([{"id": 60480302, "label": "autre"}, {"id": 501, "label": "x"}])
    r = outil("inventaire", "avant")
    note("inventaire avant", r.returncode == 0 and open(os.path.join(envp, "ids-avant.txt")).read() == "501\n60480302\n", r.stdout)
    r = outil("creation")
    note("creation → 777, fichier supprimé", r.returncode == 0 and "ID=777" in r.stdout and not os.path.exists(os.path.join(envp, "creation.json")), r.stdout)
    r = outil("creation")
    note("creation rejouée → 2", r.returncode == 2, r.stdout)
    liste([{"id": 60480302, "label": "autre"}, {"id": 501, "label": "x"}, {"id": 777, "label": etiq, "dph_total": 0.15, "actual_status": "running"}])
    r = outil("inventaire", "apres-creation")
    r2 = outil("ajoute")
    note("inventaire après, seule ajoutée", r.returncode == 0 and r2.returncode == 0, r.stdout + r2.stdout)
    r = outil("relire", etiq)
    note("relire : étiquette et prix", r.returncode == 0, r.stdout)
    r = outil("relire", "pilote-mr2-v74-20991231")
    note("relire, autre étiquette → 2", r.returncode == 2, r.stdout)
    json.dump({"credit": 10.5, "email": "jamais@lu"}, open(os.path.join(dv, "user.json"), "w"))
    r = outil("credit")
    note("credit 10,5 → 0", r.returncode == 0 and "jamais" not in r.stdout, r.stdout)
    json.dump({"credit": 3.0}, open(os.path.join(dv, "user.json"), "w"))
    r = outil("credit")
    note("credit 3 → 2", r.returncode == 2, r.stdout)
    # destruction
    r = outil("detruire", etiq)
    note("detruire : commande par l'identifiant, -y", r.returncode == 0 and f"GO_ID=GO-2026-11-14-14 {vf} destroy instance 777 -y" in r.stdout, r.stdout)
    r = outil("verifier-destruction")
    note("verifier-destruction, encore listée → 2", r.returncode == 2 and "toujours listée" in r.stdout, r.stdout)
    liste([{"id": 60480302, "label": "autre"}])
    r = outil("verifier-destruction")
    note("verifier-destruction, témoin manquant → 2", r.returncode == 2 and "témoin" in r.stdout, r.stdout)
    liste([{"id": 60480302, "label": "autre"}, {"id": 501, "label": "x"}])
    r = outil("verifier-destruction")
    note("verifier-destruction, absente, témoins listés → 0", r.returncode == 0, r.stdout)
    liste([{"id": 777, "label": etiq}, {"id": 778, "label": etiq}])
    os.rename(os.path.join(envp, "identifiant.txt"), os.path.join(envp, "identifiant-1.txt"))
    r = outil("trouver", etiq)
    note("trouver, deux de l'étiquette → 2", r.returncode == 2, r.stdout)
    # aucune valeur de clé dans le dossier d'envoi, aucun fichier de liste gardé
    fuite = [n for n in os.listdir(envp) if cles_dans_liste in open(os.path.join(envp, n), errors="replace").read()]
    note("aucune valeur de clé gardée dans le dossier d'envoi", not fuite and not any(n.endswith("instances.json") for n in os.listdir(envp)), str(fuite))
    res = {"cas": cas, "tout_conforme": all(c["conforme"] for c in cas.values()), "outil_session_sha256": EA.hashlib.sha256(
        open(os.path.join(EA.CODE, "session_pilote_mr2_v74_v1.sh"), "rb").read()).hexdigest(),
        "aide_session_sha256": EA.hashlib.sha256(open(os.path.join(EA.CODE, "session_pilote_mr2_v74_v1.py"), "rb").read()).hexdigest()}
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    return 0 if res["tout_conforme"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
