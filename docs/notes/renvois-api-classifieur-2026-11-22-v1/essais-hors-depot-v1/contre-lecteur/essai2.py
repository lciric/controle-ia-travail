import sys, os, json, shutil
B='/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1/'
sys.path.insert(0,B)
import renvois_api_v1 as R
P=R.P
os.environ['RR_ANTHROPIC_API_KEY_LUC']='dummy'
calls=[]
def ts(url,ent,corps,delai=60.0):
    d=json.loads(corps); calls.append(('simple',d.get('model'),d.get('max_tokens'),d.get('output_config')))
    body={"id":"m","model":d['model'],"type":"message","role":"assistant","content":[{"type":"text","text":"ok"}],"stop_reason":"end_turn","usage":{"input_tokens":8,"output_tokens":1}}
    return 200, json.dumps(body).encode()
def tr(url,ent,corps,brut):
    d=json.loads(corps); calls.append(('reel',d['model'],len(d['messages'][0]['content']),d.get('output_config')))
    brut.write(b'raw')
    return 200, iter([{"type":"message_start","message":{"model":d['model'],"usage":{"input_tokens":100}}},{"type":"content_block_delta","delta":{"type":"text_delta","text":"SECRETREPONSE"}},{"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":100}}])
P.transport_simple=ts; P.transport_reel=tr
D='/tmp/claude-0/t/'
args=lambda t,reg,*e:['--configuration',B+'configuration-renvois-api-v1.json','--plan-envoi',B+'plan-envoi-renvois-api-v1.json','--plan-garde',B+'plan-garde-depart-renvois-api-v1.json','--quarantaine',D+'Q'+t,'--journal',D+'J'+t+'.jsonl','--registre-go',reg,'--go','GO-2026-11-22-97','--reel',*e]
import io,contextlib
for t,reg in (('1',D+'go_incomplet.md'),('2',D+'go.md')):
    calls.clear(); o=io.StringIO()
    with contextlib.redirect_stdout(o):
        rc=R.main(args(t,reg))
    print(t,'rc',rc,'calls',calls); print('stdout has secret:', 'SECRET' in o.getvalue()); print(o.getvalue()[:400])
# envoi-only journal
open(D+'jenvoi.jsonl','w').write(json.dumps({"type_ligne":"envoi","pire_usd":"4.89"})+"\n")
print('depense envoi seul', R.depense_precedente([D+'jenvoi.jsonl']))
# plan à tester : empreinte falsifiée avec compagnon régénéré ; chaine à 2 maillons
c=P.lire_configuration(B+'configuration-renvois-api-v1.json')
pl=json.load(open(B+'plan-envoi-renvois-api-v1.json'))
pl['attribution'][0]['sha256']='0'*64
open(D+'plan_bad.json','w').write(json.dumps(pl)); import hashlib
open(D+'plan_bad.json.sha256','w').write(hashlib.sha256(open(D+'plan_bad.json','rb').read()).hexdigest()+'  x\n')
try: R.lire_plan(D+'plan_bad.json',c)
except P.Refus as e: print('refus plan falsifié:',e)
c2=json.loads(json.dumps(c)); c2['proposeurs'][0]['chaine'].append(c2['proposeurs'][0]['chaine'][0])
try: R.lire_plan(B+'plan-envoi-renvois-api-v1.json',c2)
except P.Refus as e: print('refus repli:',e)
