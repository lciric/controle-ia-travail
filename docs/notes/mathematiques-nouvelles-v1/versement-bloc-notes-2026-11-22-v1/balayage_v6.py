import tempfile, os, json
from fractions import Fraction
from controle_ia.oracles_plantes_v6 import banque, parametres
from controle_ia.oracles_plantes_v6.rejeu import rejouer_batterie_banque
from controle_ia.oracles_plantes_v6.cles import cle_du_monde
from controle_ia.oracles_plantes_v6.lignee import Registre
from controle_ia.oracles_plantes_v6.forme_seule import mesurer, ecarts_p9, ecarts_p10
from controle_ia.oracles_plantes_v6.graines import generateur
p,_=parametres.charger()
refus=[]; ec=0; col=0; rep=0; aires=[]
for r in list(range(40))+[20261122, 11]:
    try:
        B=banque.construire_banque(r,p)
    except BaseException as ex:
        refus.append(r); print(r,"REFUS",type(ex).__name__,ex, flush=True); continue
    cles=[cle_du_monde(m,"x",pl) | {"identifiant_monde": str(m.indice)} for m,pl in B]
    reg=Registre(os.path.join(tempfile.mkdtemp(),"r.jsonl"))
    rap=rejouer_batterie_banque([m for m,_ in B],cles,reg)
    mes=mesurer(B, generateur(r,10,0), 4, "1", Fraction(3,4))
    e = rap["ecarts"] + ecarts_p9(mes) + ecarts_p10(mes)
    ec += bool(e); col += rap["collisions_de_lignee"]["nombre"]
    rep += any(x.rang_candidat > 0 for _,pl in B for x in pl)
    cs=mes["classifieur_de_style"]; hv=cs["hors_textes_vus"]
    aires.append((r, hv["aire_pieges_contre_verites"], hv["aire_faux_tot_contre_verites"], cs["aire_qui_fait_foi"]))
    print(r,"ecarts",e,"aires hors vus",hv["aire_pieges_contre_verites"],hv["aire_faux_tot_contre_verites"],"foi",cs["aire_qui_fait_foi"],"etage3",rap["redites_par_l_etage_3_seul"], flush=True)
foi=[Fraction(a[3]) for a in aires]
print("refus",refus,"racines avec ecarts",ec,"collisions",col,"racines avec repli",rep)
print("aire qui fait foi : min",float(min(foi)),"max",float(max(foi)),"au-dessous de 3/4 :",sum(1 for x in foi if x<=Fraction(3,4)),"sur",len(foi))
json.dump(aires, open("/tmp/claude-0/-home-user-controle-ia-travail/20208902-dd97-5b17-8c00-94a98e64b0f0/scratchpad/v6-aires.json","w"))
