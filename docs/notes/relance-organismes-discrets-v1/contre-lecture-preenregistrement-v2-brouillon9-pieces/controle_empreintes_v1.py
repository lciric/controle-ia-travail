"""Contre-lecture 9 : empreintes de la table d'en-tête du brouillon 9 et des pièces citées ailleurs (empreintes
entières de 64 signes), recalculées ; fichiers visés par les interdits de la contre-lecture sautés, jamais ouverts."""
import hashlib, re, sys, pathlib
B9 = "prereg/T0.7-organismes-discrets-v-a-v2-brouillon9.md"
INTERDITS = ("prereg/T0.6-organismes-v0-v1.md", "prereg/T0.8", "registres/code-mots-et-cout", "scripts/mots_et_cout",
             "bras_a_v2_habilite", "/bases/", "/sondes/", "docs/notes/bras-a-moniteurs-v1/notice-",
             "docs/notes/bras-a-moniteurs-v1/contre-lecture-code-")
texte = pathlib.Path(B9).read_text(encoding="utf-8")
vus = set(); egales = differentes = absentes = sautees = 0
for l in texte.splitlines():
    for chemin, h in re.findall(r"`([^`\s]+\.(?:md|py|json|txt))`[^`|]*?(?:\|\s*)?`([0-9a-f]{64})`", l):
        if (chemin, h) in vus: continue
        vus.add((chemin, h))
        if any(i in chemin for i in INTERDITS):
            sautees += 1; print(f"SAUTÉE (interdit)  {chemin}"); continue
        p = pathlib.Path(chemin)
        if not p.exists():
            absentes += 1; print(f"ABSENTE            {chemin}"); continue
        r = hashlib.sha256(p.read_bytes()).hexdigest()
        if r == h: egales += 1
        else: differentes += 1; print(f"DIFFÉRENTE         {chemin} cité {h[:12]}… calculé {r[:12]}…")
print(f"égales {egales} ; différentes {differentes} ; absentes {absentes} ; sautées {sautees}")
