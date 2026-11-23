"""Pousse au fil de l'eau les sorties du troisième essai d'Argon vers le jeu privé Sirmium/rr-resultats.
Usage : python3 -I pousser_sorties.py <PID de l'envoi>. Pousse toutes les 30 s tant que le PID vit, puis une dernière fois."""
import os, sys, time
from huggingface_hub import HfApi

PID = int(sys.argv[1])
SRC = "/home/user/rr_hors_git"
DEST = "hors_git/exp1_ter/2026-11-22-pilote3-argon"
api = HfApi(token=os.environ["HF_TOKEN"])
MOTIFS = ["AR3e/preparation.json", "AR3e/reponses_pilote2_agent_gemini4_argon/**", "argon_pilote3.log"]


def vivant(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


def pousser(msg):
    try:
        api.upload_folder(folder_path=SRC, repo_id="Sirmium/rr-resultats", repo_type="dataset",
                          path_in_repo=DEST, allow_patterns=MOTIFS, commit_message=msg)
        print(time.strftime("%H:%M:%SZ", time.gmtime()), "poussé", flush=True)
    except Exception as e:  # journalisé, jamais tu ; on réessaie au tour suivant
        print(time.strftime("%H:%M:%SZ", time.gmtime()), "ÉCHEC de la poussée :", type(e).__name__, str(e)[:200], flush=True)


while vivant(PID):
    pousser("Troisième essai d'Argon : sorties au fil de l'eau")
    for _ in range(30):
        if not vivant(PID):
            break
        time.sleep(1)
pousser("Troisième essai d'Argon : sorties à la fin de l'envoi")
print("fin", flush=True)
