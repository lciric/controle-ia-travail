import re, sys, hashlib
F = sys.argv[1]
MARQUE = "[retiré, règle 2 : recommandation ou confiance d'auteur]"
L = open(F, encoding="utf-8").read().split("\n")
P, p = [], "tête"
for l in L:
    m = re.match(r"### Pièce (\S+)", l)
    if m: p = m.group(1)
    P.append(p)
def chercher(nom, motif, flags=0):
    r = re.compile(motif, flags)
    hits = [(i + 1, P[i], l) for i, l in enumerate(L) if r.search(l.replace(MARQUE, ""))]
    print(f"\n== {nom} — motif {motif!r} : {len(hits)} ligne(s)")
    for i, q, l in hits[:40]:
        print(f"  l. {i} [pièce {q}] {l[:180]}")
print(f"Balayage de {F} (règle 4 de faits-a-assembler-noeuds-v6.md), session-depot, 31 octobre 2026.")
print(f"Lignes : {len(L)} ; mots : {sum(len(l.split()) for l in L)} ; marques de retrait (règle 2) : {sum(l.count(MARQUE) for l in L)}.")
chercher("chemins donnees/", r"donnees/")
chercher("clés et jetons", r"sk-[A-Za-z0-9_-]{8,}|AIza[0-9A-Za-z_-]{10,}|Bearer\s+[A-Za-z0-9._-]{8,}|API_KEY=\S|_KEY=[A-Za-z0-9]{8,}|ghp_[A-Za-z0-9]{10,}|xox[bp]-")
chercher("mémo des décisions en attente (règle 1)", r"decisions-en-attente-lazar")
chercher("contenu d'attaque (mots repères)", r"jailbreak|obfusc|suffix|suffixe adverse|évasion|contourn|BA-002|mode tenu à l.écart|bras d.attaque|camoufl", re.I)
chercher("texte de fiche réelle (repères)", r"^\s*>\s*\*\*(Titre|Hypothèse|Idée)|«\s*Fiche\s+[A-Z0-9]|texte de (la )?fiche", re.I)
chercher("recommandation, confiance ou défaut restants (hors marques de retrait)", r"recommand|confiances?\s*(?:d.environ\s*)?[0-9]|par défaut", re.I)
