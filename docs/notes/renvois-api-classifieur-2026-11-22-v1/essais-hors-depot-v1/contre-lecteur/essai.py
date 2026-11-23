import sys, os, json, io, contextlib
sys.path.insert(0,'/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1')
import renvois_api_v1 as R
P=R.P
D=R.D
base='/home/user/controle-ia-travail/docs/notes/renvois-api-classifieur-2026-11-22-v1/'
c=P.lire_configuration(base+'configuration-renvois-api-v1.json')
attr,textes=R.lire_plan(base+'plan-envoi-renvois-api-v1.json',c)
print({k:(v,len(textes[v])) for k,v in attr.items()})
envoyes=[]
def mk(sortie, fin='end_turn', texte='x'*50, entree=2000):
    def tr(url,ent,corps,brut):
        d=json.loads(corps); envoyes.append((d['model'],len(d['messages'][0]['content']),url,d.get('output_config'),ent.get('x-api-key')))
        evs=[{"type":"message_start","message":{"model":d['model'],"usage":{"input_tokens":entree}}},
             {"type":"content_block_delta","delta":{"type":"text_delta","text":texte}},
             {"type":"message_delta","delta":{"stop_reason":fin},"usage":{"output_tokens":sortie}}]
        brut.write(b'raw'); return 200, iter(evs)
    return tr
def course(tr, plafond, tag, env={"RR_ANTHROPIC_API_KEY_LUC":"k"}):
    q=f'/tmp/claude-0/t/qq{tag}'; j=f'/tmp/claude-0/t/jj{tag}.jsonl'
    r=R.Renvois(c,textes,env,tr,q,j,attr,plafond); os.makedirs(q)
    buf=io.StringIO()
    out=r.courir(); return out,j,r
# 1 pire cas: tous au maximum de sortie
envoyes.clear()
out,j,r=course(mk(96000),R.PLAFOND_TOTAL,'a'); print(out); print(len(envoyes), [e[:2] for e in envoyes])
print('cumul',r.cumul)
# 2 refus
envoyes.clear()
out,j,r=course(mk(5,fin='refusal',texte=''),R.PLAFOND_TOTAL,'b'); print(out, len(envoyes))
# 3 depense precedente + plafond serré
print(R.depense_precedente([j]), R.depense_precedente(['/tmp/claude-0/t/jja.jsonl']))
envoyes.clear()
out,j3,r=course(mk(96000),D('9.0'),'c'); print(out, len(envoyes), r.cumul)
envoyes.clear()
out,j4,r=course(mk(96000),D('5.0'),'d'); print(out, len(envoyes), r.cumul)
# 4 usage illisible
def tr_ill(url,ent,corps,brut):
    envoyes.append(1); brut.write(b'r'); return 200, iter([{"type":"message_start","message":{"model":"claude-opus-5-5"}}])
envoyes.clear(); out,j5,r=course(tr_ill,R.PLAFOND_TOTAL,'e'); print(out, r.cumul)
# 5 modèle substitué
def tr_sub(url,ent,corps,brut):
    brut.write(b'r'); return 200, iter([{"type":"message_start","message":{"model":"claude-sonnet-4-6","usage":{"input_tokens":1}}},{"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":1}}])
out,j6,r=course(tr_sub,R.PLAFOND_TOTAL,'f'); print(out)
# 6 crédit
def tr_cr(url,ent,corps,brut):
    envoyes.append(1); brut.write(b'r'); return 400, iter([{"error":{"type":"invalid_request_error","message":"credit balance is too low"}}])
envoyes.clear(); out,j7,r=course(tr_cr,R.PLAFOND_TOTAL,'g'); print(out,len(envoyes))
# journal : contenu sans texte?
print(open(j).read()[:600])
