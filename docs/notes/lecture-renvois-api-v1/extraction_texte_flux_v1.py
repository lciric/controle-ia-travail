import json,sys
for p in sys.argv[2:]:
    txt=[];stop=None;kinds={}
    for line in open(p,encoding='utf-8'):
        if not line.startswith('data:'): continue
        try: d=json.loads(line[5:])
        except Exception: continue
        if d.get('type')=='content_block_start': kinds[d['index']]=d['content_block']['type']
        if d.get('type')=='content_block_delta' and d['delta'].get('type')=='text_delta': txt.append(d['delta']['text'])
        if d.get('type')=='message_delta': stop=d['delta'].get('stop_reason')
    out=sys.argv[1]+'/'+p.split('/')[-2]+'__'+p.split('/')[-1]+'.txt'
    open(out,'w').write(''.join(txt))
    print(out, stop, kinds, len(''.join(txt)))
