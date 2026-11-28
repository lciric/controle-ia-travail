"""Une page d'une source citée par la synthèse v5 (correcteur v5).

Sources : PDF versés de docs/sources/pdf/ (empreinte complète recalculée, comparée au préfixe de la table des clés),
sinon extraits texte page par page (txt-nouveaux/, extraction/txt-representations/), les PDF de [N] et [X] étant absents
du bloc-notes restauré.
Usage :
  python3 -I -B pagev5.py --page CLE PAGE [raw|layout]
  python3 -I -B pagev5.py CLE PAGE "phrase" [raw|layout]
"""
import hashlib, re, subprocess, sys, unicodedata
from pathlib import Path

D = Path("/home/user/controle-ia-travail/docs/sources/pdf")
RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
PDF = {"AP": ("2502.03407v1", "a4820ad5"), "PAR": ("2507.12691v3", "0c00a77b"), "OA": ("2602.15515v2", "f6547ec8"),
       "CA": ("2610.12445v1", "7e141758"), "YS": ("2609.02893v1", "b76151cd"), "BX": ("2509.21344v2", "aaac4ff9"),
       "AG": ("2512.07810v1", "77e64bcd"), "KU": ("2605.27958v1", "43f55118"), "MK": ("2506.10805v4", "54bf5555"),
       "GM": ("2601.11516v4", "c4a36db5"), "EM": ("2604.07729v1", "afe70d72"), "RO": ("2604.01151v3", "bde99a62")}
TXT = {"K": RD / "txt-nouveaux/2511.17408v4", "LB": RD / "txt-nouveaux/2511.16035v2",
       "AU": RD / "txt-nouveaux/2504.04072v3", "DYL": RD / "txt-nouveaux/2606.12618v2",
       "RH": RD / "txt-nouveaux/2609.19101v2", "CC": RD / "txt-nouveaux/2601.04603v1",
       "BU": RD / "extraction/txt-representations/2407.12831v2", "LIAR": RD / "extraction/txt-representations/2309.15840v1",
       "FQ": RD / "extraction/txt-representations/2312.10029v2"}


def texte(cle, page, mode):
    if cle in PDF:
        nom, pre = PDF[cle]
        p = D / f"{nom}.pdf"
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if not h.startswith(pre):
            sys.exit(f"empreinte en écart pour {cle} : {h}")
        opt = "-raw" if mode == "raw" else "-layout"
        return subprocess.run(["pdftotext", opt, "-f", str(page), "-l", str(page), str(p), "-"],
                              capture_output=True, text=True, check=True).stdout
    f = TXT[cle] / f"p{page:02d}.txt"
    return f.read_text(errors="ignore")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def main():
    a = sys.argv[1:]
    if a[0] == "--page":
        mode = a[3] if len(a) > 3 else "raw"
        for i, l in enumerate(texte(a[1], int(a[2]), mode).splitlines(), 1):
            print(f"{i:3d}: {l}")
        return
    cle, page, phrase = a[0], int(a[1]), a[2]
    mode = a[3] if len(a) > 3 else "raw"
    ici = norm(phrase) in norm(texte(cle, page, mode))
    print(f"{cle} p.{page} {mode} {'TROUVÉ' if ici else 'ABSENT'} {phrase[:90]!r}")
    sys.exit(0 if ici else 1)


if __name__ == "__main__":
    main()
