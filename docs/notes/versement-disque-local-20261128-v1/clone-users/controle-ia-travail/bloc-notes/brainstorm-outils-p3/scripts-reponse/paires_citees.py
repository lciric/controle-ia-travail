# Usage : python3 -I paires_citees.py REPONSE.md LISTE_VERIF.txt
# Extrait les paires (clé, page) citées « [CLÉ p. N] » et les compare aux pages vérifiées par verifier.sh.
import re, sys
texte = open(sys.argv[1], encoding="utf-8").read()
fichiers = {
 "JL":"j-lens-2607.15495.pdf","BX":"bx-2509.21344v2.pdf","TG":"sandbag-games-2512.07810.pdf","YS":"2609.02893.pdf",
 "YG":"2602.20273.pdf","KT":"exec-2502.00873.pdf","SU":"cs-2507.12379.pdf","CL":"suite-2608.31084.pdf","TT":"cs-2406.00799.pdf",
 "OBE":"cs-2509.03531.pdf","GE":"ci-2304.14767.pdf","AP":"2502.03407.pdf","DYL":"ci-2606.12618.pdf","PV":"persona-2507.21509.pdf",
 "AO":"ao-2512.15674.pdf","AB":"auditbench-2602.22755.pdf","AU":"audit-2503.10965.pdf","ADL":"adl-2510.13900.pdf",
 "LS":"llamascope-2410.20526.pdf","KA":"2502.16681.pdf","KI":"2511.17408.pdf","LG":"exec-2410.11781.pdf","MK":"ci-2311.17030.pdf",
 "OT":"ci-2307.09476.pdf","CA":"ci-2311.15131.pdf","LQ":"2412.08686.pdf","ATP":"exec-2403.00745.pdf","CRV":"crv-2510.09312.pdf",
 "OB":"2412.09565.pdf","KR":"2601.11516.pdf","PB":"2507.12691.pdf","LB":"ci-2511.16035.pdf","SM":"ci-2511.22662.pdf",
 "AS":"ci-2112.00861.pdf","QK":"2312.01037.pdf","FQ":"exec-2312.10029.pdf","CCS":"ci-2212.03827.pdf","PS":"2401.06102.pdf",
 "TL":"2303.08112.pdf","MAD":"2504.08812.pdf"}
cites = set()
for bloc in re.findall(r"\[([^\]]*?\bp\. [^\]]*)\]", texte):
    for morceau in bloc.split(";"):
        m = re.match(r"\s*([A-Z]{2,4})\s+(p\..*)", morceau.strip())
        if not m: continue
        cle, pages = m.group(1), m.group(2)
        for a, b in re.findall(r"(\d+)(?:-(\d+))?", pages):
            for p in range(int(a), int(b or a) + 1):
                cites.add((cle, p))
verifiees = set()
for ligne in open(sys.argv[2], encoding="utf-8"):
    pdf, page, _ = ligne.rstrip("\n").split("|", 2)
    verifiees.add((pdf.split("/")[-1], int(page)))
manque = sorted((c, p) for c, p in cites if (fichiers.get(c, "?"), p) not in verifiees)
print("paires citées :", len(cites)); print("citées sans phrase vérifiée par script :", manque)
