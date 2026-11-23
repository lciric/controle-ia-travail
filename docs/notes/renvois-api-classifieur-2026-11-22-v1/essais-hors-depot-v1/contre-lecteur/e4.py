import sys, os, json, io, contextlib, hashlib
B='/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1/'
sys.path.insert(0,B)
import renvois_api_v3 as R
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

import os
rc,out=go(a('1','--journaux-precedents','--reel')); print('fable400',rc,out[:200],calls,os.path.exists(D+'Q1'))
# sain
def ts2(url,ent,corps,delai=60.0):
    d=json.loads(corps); return 200,json.dumps({"model":d['model'],"content":[{"type":"text","text":"ok"}],"stop_reason":"end_turn","usage":{"input_tokens":8,"output_tokens":1}}).encode()
P.transport_simple=ts2; calls.clear()
rc,out=go(a('2','--journaux-precedents','--reel')); print('sain',rc,out[:160],calls)
