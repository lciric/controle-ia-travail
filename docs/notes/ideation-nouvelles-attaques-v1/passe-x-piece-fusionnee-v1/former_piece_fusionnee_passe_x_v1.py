"""Forme la pièce fusionnée de la passe X, à l'octet, par les fonctions du devis v3 scellé
(calcul_devis_passe_x_v3.py : lire, fusion avec séparateurs), et refuse si son empreinte
diffère de celle du devis (39fb4e93…). Écrit la pièce sans l'afficher ; n'écrase jamais."""
import hashlib, importlib.util, sys
DEVIS = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/devis-passe-x-v3/calcul_devis_passe_x_v3.py"
ATTENDUE = "39fb4e93f26f6447822a9f548053b1ca8f8156d714d3d55bb8c0369a11b9db2a"
spec = importlib.util.spec_from_file_location("devis_v3", DEVIS)
dv = importlib.util.module_from_spec(spec); spec.loader.exec_module(dv)
_, corps_l, _ = dv.lire()
texte = dv.fusion(corps_l, True)
b = texte.encode("utf-8")
h = hashlib.sha256(b).hexdigest()
if h != ATTENDUE:
    sys.exit("REFUS : empreinte %s différente de celle du devis v3" % h)
with open(sys.argv[1], "xb") as f:
    f.write(b)
print("conforme", h, len(b), "octets", len(texte), "signes")
