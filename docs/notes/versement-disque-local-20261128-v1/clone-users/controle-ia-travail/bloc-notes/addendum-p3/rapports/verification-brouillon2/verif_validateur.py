"""Simulation : brouillon 2 avec marqueurs remplis ; validateur et expressions de lancement (lecture seule du dépôt)."""
import hashlib, re, sys
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.prereg import problemes
from controle_ia.harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE

src = Path(sys.argv[1]).read_text(encoding="utf-8")
ici = Path(__file__).parent
def h(s): return hashlib.sha256(s.encode()).hexdigest()
rempli = (src.replace("<<EMPREINTE_MODULE>>", h("m")).replace("<<EMPREINTE_TESTS>>", h("t"))
             .replace("<<EMPREINTE_RAPPORT_R2>>", h("r")).replace("<<EMPREINTE_TRAITEMENT>>", h("x")))
p = ici / "simulation-rempli.md"; p.write_text(rempli, encoding="utf-8")
print("brouillon tel quel :", problemes(sys.argv[1]))
print("marqueurs remplis   :", problemes(p))
# un seul marqueur laissé
for m in ("<<EMPREINTE_MODULE>>", "<<EMPREINTE_TESTS>>", "<<EMPREINTE_RAPPORT_R2>>", "<<EMPREINTE_TRAITEMENT>>"):
    q = ici / "simulation-un-reste.md"
    t = rempli
    # remet le marqueur à sa place
    cle = {"<<EMPREINTE_MODULE>>": h("m"), "<<EMPREINTE_TESTS>>": h("t"), "<<EMPREINTE_RAPPORT_R2>>": h("r"), "<<EMPREINTE_TRAITEMENT>>": h("x")}[m]
    q.write_text(t.replace(cle, m), encoding="utf-8")
    print("reste", m, ":", problemes(q))
print("COMMIT_CITE   :", COMMIT_CITE.findall(rempli))
print("ENTROPIE_CITEE:", ENTROPIE_CITEE.findall(rempli))
# rapport et traitement remplis mais brouillon 2 et vérification absents : le validateur passe-t-il ?
