"""r5 — vérifications du rapport : lectures interdites (prose hors citations), motifs de valeurs de clés
(comptes seuls ; aucune valeur n'est écrite), empreintes des fichiers extraits.

Usage : python3 -I r5_verifications.py RAPPORT EXTRAIT_M EXTRAIT_S SORTIE_TXT SORTIE_EMPREINTES_M SORTIE_EMPREINTES_S
"""
import hashlib
import os
import re
import sys

# Lectures interdites de T2 (l. 518–525), en motifs ; toute occurrence est listée pour relecture humaine.
INTERDITS = [
    r"\bbat\b", r"\bbattu", r"dépass", r"reste sous", r"fait mieux", r"moins bien", r"apprentissage", r"apprend", r"appris",
    r"mémoire qui marche", r"\bbonne?s?\b", r"profonde?s?\b", r"\bfausses?\b", r"\bfaux\b", r"meilleur", r"supérieur",
    r"inférieur", r"plus haut", r"plus bas", r"élevée?s?\b", r"\bfaibles?\b", r"excellent", r"médiocre", r"amélior",
    r"progress", r"hausse", r"baisse", r"\bécart", r"différence", r"moins que", r"plus que", r"au-dessus", r"en dessous",
    r"au-delà", r"intelligen", r"causé", r"à cause", r"grâce à", r"explique", r"effet",
]
# Motifs de valeurs de clés (préfixes connus et affectations) ; seuls des comptes sortent.
CLES = {
    "anthropic sk-ant-": re.compile(rb"sk-ant-[A-Za-z0-9_\-]{16,}"),
    "google AIza": re.compile(rb"AIza[0-9A-Za-z_\-]{30,}"),
    "brave BSA": re.compile(rb"\bBSA[0-9A-Za-z_\-]{20,}"),
    "affectation de clé": re.compile(rb"(?i)(x-api-key|authorization|api[_-]?key)\s*[:=]\s*[\"']?(bearer\s+)?[A-Za-z0-9_\-]{20,}"),
}


def main():
    rap, em, es, sortie, sm, ss = sys.argv[1:7]
    lignes = open(rap, encoding="utf-8").read().split("\n")
    out = []
    # 1. prose hors citations (lignes qui ne commencent pas par « > »)
    out.append("## 1. Lectures interdites — occurrences dans la prose (hors lignes citées « > »), à relire")
    n_occ = 0
    for i, l in enumerate(lignes, 1):
        if l.startswith(">"):
            continue
        for m in INTERDITS:
            for x in re.finditer(m, l, flags=re.I):
                n_occ += 1
                debut = max(0, x.start() - 70)
                out.append(f"l. {i} motif {m!r} : …{l[debut:x.end() + 70]}…")
    out.append(f"occurrences : {n_occ}")
    # 2. motifs de clés : rapport et arbres extraits
    out.append("\n## 2. Motifs de valeurs de clés (comptes seuls)")
    b = open(rap, "rb").read()
    for nom, rx in CLES.items():
        out.append(f"rapport : {nom} : {len(rx.findall(b))}")
    for etiquette, racine in (("extrait-M", em), ("extrait-S", es)):
        totaux = {k: 0 for k in CLES}
        fichiers = {k: [] for k in CLES}
        for r, _, fs in os.walk(racine):
            for f in fs:
                p = os.path.join(r, f)
                contenu = open(p, "rb").read()
                for nom, rx in CLES.items():
                    k = len(rx.findall(contenu))
                    if k:
                        totaux[nom] += k
                        fichiers[nom].append(os.path.relpath(p, racine))
        for nom in CLES:
            out.append(f"{etiquette} : {nom} : {totaux[nom]} occurrence(s) ; fichiers : {fichiers[nom] or 'aucun'}")
    # 3. empreintes des fichiers extraits
    for racine, dest in ((em, sm), (es, ss)):
        with open(dest, "w", encoding="utf-8") as f:
            for r, _, fs in sorted(os.walk(racine)):
                for x in sorted(fs):
                    p = os.path.join(r, x)
                    f.write(f"{hashlib.sha256(open(p, 'rb').read()).hexdigest()}  {os.path.relpath(p, racine)}\n")
        out.append(f"\nempreintes des fichiers de {racine} : {dest}")
    open(sortie, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
