"""Pousse au fil de l'eau les sorties du troisième essai d'Argon vers le jeu privé Sirmium/rr-resultats.
Usage : python3 -I pousser_sorties.py <PID de l'envoi>. Pousse toutes les 30 s tant que le PID vit, puis une dernière fois."""
import os, sys, time
from huggingface_hub import HfApi

PID = int(sys.argv[1])
SRC = "/home/user"
DEST = "hors_git/exp1_ter/2026-11-22-astra-tranches"
api = HfApi(token=os.environ["HF_TOKEN"])
MOTIFS = ["rr_hors_git/AR3e/*agent_gpt62_astra__t*", "rr_hors_git/astra_tranches.log", "raisons-ou-regard-travail/claude/papier_2026-11-14/experience_1/lots_agents_reference_ter/agent_gpt62_astra*"]


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
    pousser("Lot d'Astra par tranches : sorties au fil de l'eau")
    for _ in range(120):
        if not vivant(PID):
            break
        time.sleep(1)
pousser("Lot d'Astra par tranches : sorties à la fin de l'envoi")
print("fin", flush=True)
