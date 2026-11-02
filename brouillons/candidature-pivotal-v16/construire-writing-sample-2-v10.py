import re, html, pathlib
SRC = 'ws2-v10.txt'
src = open(SRC, encoding='utf-8').read()

paras = [p.strip() for p in src.split('\n\n') if p.strip()]
e = html.escape
def sub(t):
    t = e(t)
    return t.replace('Xi,t', 'X<sub>i,t</sub>').replace('Σδk', 'Σδ<sub>k</sub>').replace('n0', 'n₀').replace('gprobe', 'g<sub>probe</sub>')
heads2 = {'1. Summary', '2. Problem', '3. Theory: A Lemma, Negative Theorem and Important Question', '4. Two papers. One extension.', '5. How we will accomplish this'}
heads3 = {'Paper A - Time (Within 1 agent)', 'Paper C - Instrument (Corrupting the Monitor)', 'Paper B - Swarm (Extension)'}
seuls = {'Hypotheses.', 'Other Hypotheses for Paper C.', 'Gates.'}
num = re.compile(r'^\d\. ')
out = [f'<h1>{e(paras[0])}</h1>\n<p class="note">{e(paras[1])}</p>\n<p class="sous">{e(paras[2])}</p>']
rest = paras[3:]; k = 0
while k < len(rest):
    p = rest[k]
    if p in heads2: out.append(f'<h2>{e(p)}</h2>'); k += 1; continue
    if p in heads3: out.append(f'<h3>{e(p)}</h3>'); k += 1; continue
    if p.startswith('Paper A - Time Paper C - Instrument'):
        q = p.split('\n')[1]; m = rest[k+1]; mo = rest[k+2]; g = rest[k+3]
        qa, qc, qb = re.match(r'Question (Can we accumulate .*?\?) (What would .*?\?) (Can we detect .*)$', q).groups()
        ma, mc, mb = re.match(r'Method (2 x 2.*?Sequential\)) (Seek law of deference .*?Probes?) (How .*)$', m).groups()
        moa, moc, mob = __import__('re').match(r'Months (\S+) (\S+) (.*)$', mo).groups()
        ga, gc, gb = __import__('re').match(r'Gates (G1 \(.*?\)) (GC \(.*?\)) (G2.*)$', g).groups()
        out.append('<table>\n<tr><th></th><th>Paper A - Time</th><th>Paper C - Instrument</th><th>Paper B - Swarm (Extension)</th></tr>\n'
                   f'<tr><td class="l">Question</td><td>{e(qa)}</td><td>{e(qc)}</td><td>{e(qb)}</td></tr>\n'
                   f'<tr><td class="l">Method</td><td>{e(ma)}</td><td>{e(mc)}</td><td>{e(mb)}</td></tr>\n'
                   f'<tr><td class="l">Months</td><td>{e(moa)}</td><td>{e(moc)}</td><td>{e(mob)}</td></tr>\n'
                   f'<tr><td class="l">Gates</td><td>{e(ga)}</td><td>{e(gc)}</td><td>{e(gb)}</td></tr>\n</table>')
        k += 4; continue
    if p.startswith('Δv = g'):
        out.append('<p class="eq">Δv = g · (c̃ − v₀)</p>'); k += 1; continue
    if all(l.startswith('- ') for l in p.split('\n')):
        out.append('<ul>\n' + '\n'.join(f'<li>{sub(l[2:])}</li>' for l in p.split('\n')) + '\n</ul>'); k += 1; continue
    if num.match(p):
        items = []
        while k < len(rest) and num.match(rest[k]):
            items.append(num.sub('', rest[k])); k += 1
        out.append('<ol>\n' + '\n'.join(f'<li>{sub(x)}</li>' for x in items) + '\n</ol>'); continue
    if p in seuls:
        out.append(f'<p><b>{sub(p)}</b></p>'); k += 1; continue
    if p == 'Negative Theorem (T) Due to invariance. Blind.':
        out.append('<p><b>Negative Theorem (T) Due to invariance.</b></p>')
        out.append(f'<p><b>Blind.</b> {sub(rest[k+1])}</p>'); k += 2; continue
    if len(p) < 70 and k + 1 < len(rest) and rest[k+1].startswith('- '):
        out.append(f'<p><b>{sub(p)}</b></p>'); k += 1; continue
    if len(p) < 70 and k + 1 < len(rest) and len(rest[k+1]) > 70 and not num.match(rest[k+1]) and not rest[k+1].startswith('Δv') and not rest[k+1].startswith('- '):
        out.append(f'<p><b>{sub(p)}</b> {sub(rest[k+1])}</p>'); k += 2; continue
    out.append(f'<p>{sub(p)}</p>'); k += 1
tpl = pathlib.Path('ws2-final-v3.html').read_text(encoding='utf-8')
pathlib.Path('ws2-v10.html').write_text(tpl[:tpl.index('<body>')+6] + '\n' + '\n'.join(out) + '\n</body></html>', encoding='utf-8')
print(len(out))
