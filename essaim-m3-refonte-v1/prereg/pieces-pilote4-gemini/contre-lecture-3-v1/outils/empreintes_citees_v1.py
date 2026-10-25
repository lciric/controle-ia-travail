# Relève les empreintes citées par le texte (64 caractères, et préfixes de 8 caractères suivis de « … ») et les cherche
# dans des fichiers d'empreintes donnés et dans des empreintes recalculées (fichiers donnés) ; lecture seule.
import hashlib, re, sys, pathlib
texte = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
connues = {}
for f in sys.argv[2:]:
    p = pathlib.Path(f)
    if p.name.startswith("EMPREINTES") and p.suffix == ".txt":
        for l in p.read_text(encoding="utf-8").splitlines():
            if l.strip():
                h, n = l.split(None, 1)
                connues.setdefault(h, set()).add(str(p.parent.name) + "/" + n.strip())
    else:
        connues.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(), set()).add(p.name)
pleines = sorted(set(re.findall(r"(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])", texte)))
print("empreintes pleines citées :", len(pleines))
for h in pleines:
    print(("  OK  " if h in connues else "  ??  ") + h[:16] + "  " + ", ".join(sorted(connues.get(h, []))[:3]))
prefixes = sorted(set(re.findall(r"(?<![0-9a-f])([0-9a-f]{8})…", texte)))
print("préfixes cités :", len(prefixes))
for p in prefixes:
    t = [n for h, ns in connues.items() if h.startswith(p) for n in ns]
    print(("  OK  " if t else "  ??  ") + p + "  " + ", ".join(sorted(t)[:2]))
