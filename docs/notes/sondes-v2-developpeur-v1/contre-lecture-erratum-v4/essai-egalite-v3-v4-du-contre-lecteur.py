import sys, json
import numpy as np
from controle_ia.sondes_v2 import monde_plante_v3 as v3, monde_plante_v4 as v4, statistiques_v1 as s1
S={"alpha":0.05,"u_fort":0.9}
V3,_=v3.charger_verites(); V4,_=v4.charger_verites()
communs=("interaction","interaction_brute","interaction_sans_controle","decalage_maitrise","transport","transport_controle","identite","texte","fuite")
ok=True
for nom in sys.argv[1:]:
    for r in range(2):
        p3=v3.parametres(V3,nom,8,1,8,3,32,"complet"); p4=v4.parametres(V4,nom,8,1,8,3,32,"complet")
        assert p3==p4
        _,g3=s1.generateurs_nommes(11,f"complet/x/{nom}/{r}/"); _,g4=s1.generateurs_nommes(11,f"complet/x/{nom}/{r}/")
        a=v3.lire_monde(p3,g3,"/tmp/claude-0/-home-user-controle-ia-travail/f6a0de81-4b86-5f89-b882-c755727ab92d/scratchpad/eq/j3.jsonl",nom,S,19,100,k_externes=3,n_nul_identite=9)
        b=v4.lire_monde(p4,g4,"/tmp/claude-0/-home-user-controle-ia-travail/f6a0de81-4b86-5f89-b882-c755727ab92d/scratchpad/eq/j4.jsonl",nom,S,19,100,k_externes=3,n_nul_identite=9,doses_rejeu=1)
        eq={k:(a.get(k)==b.get(k)) for k in communs if k in a or k in b}
        eq["holm=alpha"]= b.get("interaction_holm")==b.get("interaction") and b.get("interaction_brute_holm")==b.get("interaction_brute")
        # état des générateurs après lecture : mêmes tirages consommés
        eq["rng"]=all(g3[n].bit_generator.state==g4[n].bit_generator.state for n in g3)
        print(nom, r, all(eq.values()), [k for k,v in eq.items() if not v])
        ok &= all(eq.values())
print("TOUT EGAL", ok)
