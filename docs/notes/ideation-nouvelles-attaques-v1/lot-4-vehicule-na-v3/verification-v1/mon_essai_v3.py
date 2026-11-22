import json, threading, sys, os, tempfile
from http.server import BaseHTTPRequestHandler, HTTPServer
R = sys.argv[1]
sys.path.insert(0, R+"/orchestrator"); sys.path.insert(0, R+"/orchestrator/essais")
import aides_na_lot4_v1 as H1
import aides_na_lot4_v3 as H
from pole import adaptateur_claude_direct_na_v2 as ad, appel_garde_na_v3 as ag
SCRIPT=[]; VUS=[]
class Hd(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def do_POST(self):
        n=int(self.headers.get("content-length",0)); self.rfile.read(n); VUS.append(1)
        st,corps=SCRIPT.pop(0) if len(SCRIPT)>1 else SCRIPT[0]
        b=corps if isinstance(corps,bytes) else json.dumps(corps).encode()
        self.send_response(st); self.send_header("content-type","application/json"); self.send_header("content-length",str(len(b))); self.end_headers(); self.wfile.write(b)
srv=HTTPServer(("127.0.0.1",0),Hd); threading.Thread(target=srv.serve_forever,daemon=True).start()
URL=f"http://127.0.0.1:{srv.server_port}"
def err(msg,typ="invalid_request_error"): return {"type":"error","error":{"type":typ,"message":msg}}
M="Your credit balance is too low to access the Anthropic API."
OK200=lambda m: {"id":"x","type":"message","role":"assistant","model":m,"content":[{"type":"text","text":"ok"}],"stop_reason":"end_turn","stop_details":None,"usage":{"input_tokens":1,"output_tokens":1}}
REFUS=lambda m: {"id":"x","type":"message","role":"assistant","model":m,"content":[],"stop_reason":"refusal","stop_details":{"type":"refusal","category":None,"explanation":None},"usage":{"input_tokens":1,"output_tokens":1}}
def adapt(dossier):
    ms=H.MODELES_ADMIS
    return ad.AdaptateurClaudeDirectNA(URL,dossier,modeles_admis=ms,reglages=H.reglages_essai(),admis=H.ADMIS_ESSAI,bareme={m:H.BAREME_ESSAI[m] for m in ms},environnement={},arme=True)
CAS=[ # nom, statut, corps, attendu_credit400
 ("400 ir message exact",400,err(M),True),
 ("400 casse mixte",400,err("YOUR CrEdIt BaLaNcE iS tOo LoW"),True),
 ("400 espaces autour (fragment contigu)",400,err("   credit balance is too low   \n"),True),
 ("400 espaces internes doubles",400,err("credit  balance is too low"),False),
 ("400 message dans un autre champ (top-level message)",400,{"type":"error","message":M,"error":{"type":"invalid_request_error","message":"autre"}},False),
 ("400 message dans error.detail",400,{"type":"error","error":{"type":"invalid_request_error","detail":M,"message":"x"}},False),
 ("400 corps non JSON",400,M.encode(),False),
 ("400 corps JSON liste",400,[M],False),
 ("400 message non chaine",400,err(123),False),
 ("400 autre message",400,err("max_tokens: too big"),False),
 ("400 fragment partiel",400,err("credit balance"),False),
 ("400 billing_error + fragment",400,err(M,"billing_error"),False),
 ("400 authentication_error + fragment",400,err(M,"authentication_error"),False),
 ("429 rate_limit + fragment",429,err(M,"rate_limit_error"),False),
 ("403 permission + fragment",403,err(M,"permission_error"),False),
 ("500 api_error + fragment",500,err(M,"api_error"),False),
 ("402 billing_error",402,err(M,"billing_error"),"402"),
 ("402 billing_error sans fragment",402,err("x","billing_error"),"402"),
]
mauvais=0
for nom,st,corps,att in CAS:
    d=tempfile.mkdtemp(); s=tempfile.mkdtemp(dir=d); SCRIPT[:]=[(st,corps)]; VUS.clear()
    r=adapt(d).lancer("proposeur_ideation","bonjour",s,1.0,1,modele=H.MODELE_ROLE); t=r.tentative
    c=t["classe_erreur"]
    ok = (c==ad.ERREUR_CREDIT_AMONT_400) if att is True else (c==ad.ERREUR_CREDIT_AMONT) if att=="402" else (c not in (ad.ERREUR_CREDIT_AMONT_400,ad.ERREUR_CREDIT_AMONT,ad.ERREUR_PLAFOND_RELAIS))
    mauvais+=not ok
    fiche=json.dumps(t,default=str)+json.dumps(getattr(r,"__dict__",{}),default=str)[:0]
    print("ADAPT","OK " if ok else "KO ",nom,"->",c,"| requetes",len(VUS),"| 'balance' dans fiche:", "balance" in fiche.lower())
# chaine complete
class Mt(H.Montage): pass
def chaine(nom,script,attend13,nreq=None):
    global mauvais
    SCRIPT[:]=script; VUS.clear()
    m=H.Montage(adaptateurs_en_plus={})
    d=m.reponses; m.ad["ad_a"]=adapt(d); m.gen=H.GenerationEssai(m.ad,m.dossier,contexte_na=m.contexte)
    try:
        a=m.appeler("proposeur-espece-3",H1.requete_proposeur()); leve=False; res=a.get("issue_na")
    except ag.ArretCreditNA as e:
        leve=True; res=(e.cle,e.lu_par); txt=str(e)
        assert "balance" not in txt.lower()
    ok=(leve==attend13) and (nreq is None or len(VUS)==nreq)
    mauvais+=not ok
    with open(m.journal.chemin,encoding="utf-8") as f: j=f.read().lower()
    brut=[x for x in os.listdir(m.reponses)]
    print("CHAINE","OK " if ok else "KO ",nom,"-> n13:",leve,res,"| requetes",len(VUS),"| 'balance' dans journal:","balance" in j,"| na_replis:","balance" in str(m.gen.na_replis).lower())
    m.fermer()
chaine("1er appel 400 credit",[(400,err(M))],True,1)
chaine("repli: refus puis 400 credit",[(200,REFUS(H.MODELE_ROLE)),(400,err(M)),(200,OK200(H.REPLI_1))],True,2)
chaine("repli: refus puis 400 casse mixte",[(200,REFUS(H.MODELE_ROLE)),(400,err("CREDIT BALANCE IS TOO LOW")),(200,OK200(H.REPLI_1))],True,2)
chaine("1er appel 402 billing",[(402,err(M,"billing_error"))],True,1)
chaine("400 autre message",[(400,err("max_tokens too big"))],False,1)
chaine("429 + fragment",[(429,err(M,"rate_limit_error"))],False)
chaine("400 billing_error + fragment",[(400,err(M,"billing_error"))],False,1)
chaine("400 corps non JSON",[(400,M.encode())],False)
chaine("400 message ailleurs",[(400,{"type":"error","message":M,"error":{"type":"invalid_request_error","message":"z"}})],False)
chaine("temoin sain",[(200,OK200(H.MODELE_ROLE))],False,1)
print("MAUVAIS:",mauvais)
