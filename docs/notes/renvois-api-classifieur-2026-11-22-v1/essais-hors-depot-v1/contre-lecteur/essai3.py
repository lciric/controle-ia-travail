import sys, os, json, io, contextlib, hashlib
B='/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1/'
sys.path.insert(0,B)
import renvois_api_v2 as R
P=R.P; D='/tmp/claude-0/t/'
os.environ['RR_ANTHROPIC_API_KEY_LUC']='dummy'
def ts(url,ent,corps,delai=60.0):
    d=json.loads(corps)
    if d['model']=='claude-fable-5-1' and (d.get('output_config') or {}).get('effort')=='xhigh': return 400,b'{}'
    return 200,json.dumps({"model":d['model'],"content":[{"type":"text","text":"ok"}],"stop_reason":"end_turn","usage":{"input_tokens":8,"output_tokens":1}}).encode()
calls=[]
def tr(url,ent,corps,brut):
    d=json.loads(corps); calls.append(d['model']); brut.write(b'r')
    return 200, iter([{"type":"message_start","message":{"model":d['model'],"usage":{"input_tokens":100}}},{"type":"content_block_delta","delta":{"type":"text_delta","text":"S"}},{"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":100}}])
P.transport_simple=ts; P.transport_reel=tr
def a(t,*e,reg=D+'go.md',plan=B+'plan-envoi-renvois-api-v1.json'):
    return ['--configuration',B+'configuration-renvois-api-v1.json','--plan-envoi',plan,'--plan-garde',B+'plan-garde-depart-renvois-api-v1.json','--quarantaine',D+'Q'+t,'--journal',D+'J'+t+'.jsonl','--registre-go',reg,'--go','GO-2026-11-22-97',*e]
def go(argv):
    o=io.StringIO(); 
    try:
        with contextlib.redirect_stdout(o): rc=R.main(argv)
    except SystemExit as e: rc='exit%s'%e.code
    return rc,o.getvalue()
print(go(a('0','--journaux-precedents')))           # à blanc, aucune précédente
print(go(a('0b')))                                   # option omise
rc,out=go(a('1','--journaux-precedents','--reel')); print(rc,out[:500],calls)
print(open(D+'J1.jsonl').readline()[:400])
# orphelin
open(D+'orph.jsonl','w').write(json.dumps({"type_ligne":"envoi","proposeur":"x","relance":None,"modele_demande":"m"})+"\n"+json.dumps({"type_ligne":"envoi","proposeur":"y","relance":None,"modele_demande":"m"})+"\n"+json.dumps({"type_ligne":"tentative","proposeur":"y","relance":None,"modele_demande":"m","cout_usd":"1.0"})+"\n")
print(R.depense_precedente([D+'orph.jsonl']), R.depense_precedente([D+'orph.jsonl',D+'orph.jsonl']))
print(go(a('2','--journaux-precedents',D+'orph.jsonl')))
# plafond: 2 journaux donnent 2*(4.89+.05)+1+... 
# texte hors fixes
pl=json.load(open(B+'plan-envoi-renvois-api-v1.json')); pl['attribution'][1]['texte']='autre-texte'; pl['attribution'][1]['sha256']='a'*64
open(D+'p.json','w').write(json.dumps(pl)); open(D+'p.json.sha256','w').write(hashlib.sha256(open(D+'p.json','rb').read()).hexdigest()+' x\n')
c=P.lire_configuration(B+'configuration-renvois-api-v1.json')
for adm in ((),('a'*64,)):
    try: R.lire_plan(D+'p.json',c,adm)
    except P.Refus as e: print('refus',adm,e)
    except Exception as e: print('autre',type(e).__name__,adm)
