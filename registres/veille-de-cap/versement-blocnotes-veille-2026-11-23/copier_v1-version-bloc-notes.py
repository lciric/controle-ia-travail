"""Copie octet pour octet d'un fichier du dépôt, lu par recherche_bornee_v5 (bras boucle), vérifié par empreinte."""
import hashlib, os, re, subprocess, sys
OUTIL = "docs/notes/memoire-conception-v1/fusion-outils-v1/recherche_bornee_v5.py"
COMMIT, AGENT, JOURNAL = sys.argv[1], sys.argv[2], sys.argv[3]
def appel(*args):
    r = subprocess.run([sys.executable, "-I", OUTIL, *args, "--commit", COMMIT, "--bras", "boucle", "--agent", AGENT,
                        "--journal", JOURNAL], capture_output=True)
    return r.returncode, r.stdout
for paire in sys.argv[4:]:
    src, dst = paire.split("=>")
    lignes, de = {}, 1
    while True:
        code, out = appel("lire", src, "--de", str(de))
        if code != 0:
            sys.exit(f"ARRET {src} : {out[:200]!r}")
        suite = None
        for l in out.split(b"\n")[:-1]:
            m = re.match(rb"^(\d+)\t(.*)$", l, re.S)
            if m:
                lignes[int(m.group(1))] = m.group(2)
            elif l.startswith(b"[suite : --de "):
                suite = int(re.match(rb"\[suite : --de (\d+)", l).group(1))
            else:
                sys.exit(f"ARRET {src} : ligne inattendue {l[:80]!r}")
        if suite is None:
            break
        de = suite
    n = max(lignes)
    assert sorted(lignes) == list(range(1, n + 1))
    corps = b"\n".join(lignes[i] for i in range(1, n + 1))
    code, e16 = appel("empreinte", src)
    h = hashlib.sha256(corps).hexdigest()
    if code != 0 or e16.strip().decode() != h[:16]:
        sys.exit(f"ARRET {src} : empreinte {h[:16]} contre {e16!r}")
    if os.path.lexists(dst):
        sys.exit(f"ARRET {dst} existe (R12)")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "xb") as f:
        f.write(corps)
    print(f"{h}  {src} => {dst}")
