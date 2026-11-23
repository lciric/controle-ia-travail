import re,sys
from datetime import date
import controle_ia.organismes_discrets.lanceur_bras_a_v6 as L
sys.path.insert(0,'tests')
ligne=("| GO-2026-11-22-148 | 2026-11-22 | calcul | Même mot (GO-2026-11-22-147) : bras A, ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes), devis v5 | 18 USD | 2026-11-30 | Lazar | x |")
def reg(*ls): return "# reg\n"+"\n".join(ls)+"\n"
def essai(nom,r,g="GO-2026-11-22-148"):
    try: L.exiger_ligne_de_go(g,r,date(2026,11,23)); print("ACCEPTE",nom)
    except Exception as e: print("REFUSE ",nom,"|",str(e)[:100])
per="bras A, ligne 1 de carte"
essai("reel",reg(ligne))
for p in ["ligne 2 de carte","bras A, ligne 1 de carte et ligne 2","bras A et bras AB ligne 1","ligne 1 du bras A","Bras  A ; Ligne 1","bras A ligne 1 ; moniteurs","bras A, ligne 1, ligne 2","bras A, lignes 1 et 2","bras A, ligne 1 et 2","bras A ligne 1; lignes 1","bras A ligne 1 (hors bras B)","bras A, ligne 11","bras A, ligne 1,5","bras A, ligne 1-2","bras A, ligne 1 puis la seconde","bras A, ligne 1, sauf la ligne 3","bras A, ligne 1 et suivantes","bras A ligne 1 et 2 lignes","bras A, ligne 1 de carte, bras Ab","bras B, ligne 1","bras A, ligne 1 et ligne 1 du bras C","bras A, ligne 1, ligne1 bis","bras A, ligne 1, lignes 2"]:
    essai(p,reg(ligne.replace(per,p)))
rev="| GO-2026-11-23-150 | 2026-11-23 | révocation | révoque GO-2026-11-22-148 | - | - | Lazar | x |"
for nom,l in [("rev",rev),("rev-sous",rev.replace("GO-2026-11-23-150","GO-2026-11-23-150-P2")),("rev Majuscule",rev.replace("révocation","Révocation")),("rev -1480",rev.replace("148 ","1480 ")),("rev cite -P2",rev.replace("148 ","148-P2 ")),("rev revocation sans accent",rev.replace("révocation","revocation")),("rev dans ref",rev.replace("- | Lazar | x","- | Lazar | GO-2026-11-22-148")),("rev ligne indentee","  "+rev),("rev sans espace apres barre","|"+rev[2:]),("sp mal forme",rev.replace("150","150-P")),("sp date folle",rev.replace("2026-11-23-150","2026-13-45-150-P2"))]:
    essai(nom,reg(ligne,l))
sp=ligne.replace("GO-2026-11-22-148","GO-2026-11-22-148-P1")
essai("sp joue",reg(sp),"GO-2026-11-22-148-P1")
essai("sp seul, go 148 demande",reg(sp))
