"""Relevé local du défaut et de la voie du correctif du tokeniseur : chargement du tokeniseur par la bibliothèque de
chargement (versions de `requirements-cpu.txt`), dans un processus enfant **en ligne et sans clé**, contre une porte simulée
sur 127.0.0.1. Aucune requête ne sort de la machine ; le tokeniseur est un jouet de cinq jetons ; aucune clé n'est lue.

Deux mondes pour l'hôte simulé :
- « A » : l'interface du dépôt répond sans clé (commit de la branche principale, liste des fichiers) et tout fichier est
  refusé par le code 401 du dépôt à porte — c'est le monde qui reproduit le défaut relayé (refus sur `tokenizer.model`, à la
  révision épinglée) ;
- « B » : l'interface aussi est à porte (le défaut y aurait une autre forme : il ne répond pas au défaut relayé).
Cas joués : monde A sans marqueur, avec un marqueur, avec les trois ; monde B avec les trois.

Emploi : python porte-locale-chargement-tokeniseur-v1.py
Sortie : pour chaque cas, le code de retour de l'enfant, la fin de ses sorties, les requêtes reçues par la porte (méthode,
chemin, clé présente dans les en-têtes), les marqueurs du cache. Les numéros de port et les chemins temporaires varient.
"""
import json
import os
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DEPOT = "meta-llama/Llama-3.1-8B-Instruct"
REV = "0e9e39f249a16976918f6564b8830bc894c89659"
RACINE = ["LICENSE", "README.md", "config.json", "tokenizer.json", "tokenizer_config.json", "special_tokens_map.json",
          "original/tokenizer.model"]


def serveur(monde: str):
    appels = []

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _rep(self, code, corps=b"", en_tetes=()):
            self.send_response(code)
            for k, v in en_tetes:
                self.send_header(k, v)
            self.send_header("Content-Length", str(len(corps)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(corps)

        def _tout(self):
            appels.append((self.command, self.path, "Authorization" in self.headers))
            chemin = self.path.split("?")[0]
            porte = lambda: self._rep(401, b'{"error":"gated"}', [("X-Error-Code", "GatedRepo"), ("Content-Type", "application/json")])
            if monde == "B" or not chemin.startswith("/api/models/" + DEPOT):
                return porte()
            reste = chemin[len("/api/models/" + DEPOT):]
            if reste == "" or reste.startswith("/revision/"):
                corps = json.dumps({"id": DEPOT, "modelId": DEPOT, "sha": REV, "private": False, "gated": "manual",
                                    "siblings": [{"rfilename": f} for f in RACINE]}).encode()
                return self._rep(200, corps, [("Content-Type", "application/json")])
            if reste.startswith("/tree/"):
                sous = reste.split("/", 3)[3] if reste.count("/") >= 3 else ""
                if sous:
                    return self._rep(404, b'{"error":"absent"}', [("X-Error-Code", "EntryNotFound"), ("Content-Type", "application/json")])
                corps = json.dumps([{"type": "file", "path": f, "oid": "0" * 40, "size": 1} for f in RACINE if "/" not in f]).encode()
                return self._rep(200, corps, [("Content-Type", "application/json")])
            return porte()

        do_GET = do_HEAD = do_POST = _tout

    s = ThreadingHTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s, appels


def poser(hf_home: Path, marqueurs=()):
    from tokenizers import Tokenizer, models, pre_tokenizers
    base = hf_home / "hub" / ("models--" + DEPOT.replace("/", "--"))
    inst = base / "snapshots" / REV
    inst.mkdir(parents=True)
    vocab = {"<|begin_of_text|>": 0, "<|eot|>": 1, "a": 2, "b": 3, "ab": 4}
    tok = Tokenizer(models.BPE(vocab=vocab, merges=[("a", "b")]))
    tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
    tok.save(str(inst / "tokenizer.json"))
    (inst / "tokenizer_config.json").write_text(json.dumps({
        "bos_token": "<|begin_of_text|>", "eos_token": "<|eot|>", "clean_up_tokenization_spaces": True,
        "chat_template": "{{ bos_token }}", "model_input_names": ["input_ids", "attention_mask"],
        "model_max_length": 131072, "tokenizer_class": "PreTrainedTokenizerFast",
        "added_tokens_decoder": {"0": {"content": "<|begin_of_text|>", "lstrip": False, "normalized": False, "rstrip": False,
                                       "single_word": False, "special": True}}}))
    (inst / "special_tokens_map.json").write_text(json.dumps({"bos_token": "<|begin_of_text|>", "eos_token": "<|eot|>"}))
    (inst / "config.json").write_text(json.dumps({"architectures": ["LlamaForCausalLM"], "model_type": "llama", "vocab_size": 5,
                                                  "hidden_size": 8, "num_hidden_layers": 1, "num_attention_heads": 1,
                                                  "bos_token_id": 0, "eos_token_id": 1, "transformers_version": "4.42.3"}))
    (base / "refs").mkdir()
    (base / "refs" / "main").write_text(REV)
    for m in marqueurs:
        p = base / ".no_exist" / REV / m
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch()


SCRIPT = ("from transformers import AutoTokenizer\n"
          f"tok = AutoTokenizer.from_pretrained({DEPOT!r})\n"
          "print('CLASSE', type(tok).__name__, type(tok).vocab_files_names, repr(tok.decode([4])), len(tok))\n")


def jouer(hf_home: Path, port: int | None, hors_ligne=False):
    e = {k: v for k, v in os.environ.items() if not k.upper().endswith("_PROXY") and k not in ("HF_TOKEN",)}
    e |= {"HF_HOME": str(hf_home), "HF_HUB_DISABLE_TELEMETRY": "1", "HF_HUB_DISABLE_IMPLICIT_TOKEN": "1", "NO_PROXY": "127.0.0.1",
          "no_proxy": "127.0.0.1"}
    if port is not None:
        e["HF_ENDPOINT"] = f"http://127.0.0.1:{port}"
    if hors_ligne:
        e["HF_HUB_OFFLINE"] = "1"
    return subprocess.run([sys.executable, "-c", SCRIPT], env=e, capture_output=True, text=True, timeout=300)


if __name__ == "__main__":
    import tempfile
    TROIS = ["tokenizer.model", "added_tokens.json", "chat_template.jinja"]
    with tempfile.TemporaryDirectory() as tmp:
        for monde, marqueurs in (("A", []), ("A", TROIS[:1]), ("A", TROIS), ("B", TROIS)):
            hf = Path(tmp) / f"hf-{monde}-{len(marqueurs)}"
            poser(hf, marqueurs)
            s, appels = serveur(monde)
            r = jouer(hf, s.server_address[1])
            s.shutdown()
            print(f"=== monde {monde}, marqueurs {marqueurs} : code de retour {r.returncode}")
            print("sortie :", r.stdout.strip()[-300:])
            print("erreur :", " | ".join(r.stderr.strip().splitlines()[-2:])[-400:])
            for a in appels:
                print("requête reçue :", a)
            print("marqueurs du cache :", sorted(p.name for p in (hf / "hub").rglob(".no_exist/*/*")))
