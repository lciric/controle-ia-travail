import sys, os, json, io, contextlib
B='/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1/'
sys.path.insert(0,B)
import renvois_api_v5 as R
P=R.P; D='/tmp/claude-0/t/'
os.environ['RR_ANTHROPIC_API_KEY_LUC']='dummy'
mode={'s':200}
def ts(url,ent,corps,delai=60.0):
    d=json.loads(corps)
    if mode['s']!=200 and (d.get('output_config') or {}).get('effort')=='high': return mode['s'],b'{}'
    return 200,json.dumps({"model":d['model'],"content":[{"type":"text","text":"ok"}],"stop_reason":"end_turn","usage":{"input_tokens":8,"output_tokens":1}}).encode()
calls=[]
def tr(url,ent,corps,brut):
    d=json.loads(corps); calls.append((d['model'],d['output_config'])); brut.write(b'r')
    return 200, iter([{"type":"message_start","message":{"model":d['model'],"usage":{"input_tokens":100}}},{"type":"content_block_delta","delta":{"type":"text_delta","text":"S"}},{"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":100}}])
P.transport_simple=ts; P.transport_reel=tr
def a(t,*e):
    return ['--configuration',B+'configuration-renvois-api-relance-v1.json','--plan-envoi',B+'plan-envoi-renvois-api-relance-v1.json','--plan-garde',B+'plan-garde-depart-renvois-api-relance-v1.json','--quarantaine',D+'Q'+t,'--journal',D+'J'+t+'.jsonl','--registre-go',D+'go.md','--go','GO-2026-11-22-97','--journaux-precedents',B+'lancement/journal-renvois-api-v1.jsonl','--effort-attendu','high',*e]
def go(argv):
    o=io.StringIO(); e=io.StringIO()
    with contextlib.redirect_stdout(o), contextlib.redirect_stderr(e): rc=R.main(argv)
    return rc,o.getvalue()[:260],e.getvalue()[:200]
print('blanc',go(a('0')))
print('1',go(a('1','--reel')),calls); print(open(D+'J1.jsonl').readline()[:500])
mode['s']=400; calls.clear()
print('2',go(a('2','--reel')),calls,os.path.exists(D+'Q2'))
calls.clear(); mode['s']=200
r=go(a('3','--reel')[:-0 or None]); 
# xhigh par défaut avec config high : doit arrêter
args=[x for x in a('4','--reel') if x not in ('--effort-attendu','high')]
print('4 défaut xhigh',go(args),calls)
