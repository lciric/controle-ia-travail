import re, html, pathlib
SRC = '/mnt/user-data/attachments/03748db6-42ca-5241-871c-5399d39c1451/73318461-attachment.txt'
src = open(SRC, encoding='utf-8').read()
reps = [
 # en-tête
 ("(1-5 of 8)", "(sections 1-5 of 8)", 1),
 # 1. Summary
 ("make many harmful decisions (less safe controls, more dead ends, more expensive)", "make many slightly harmful decisions (weaker controls, more dead ends, more expensive)", 1),
 ("Paper A will accumulate probe scores over time with an anytime valid false positive.", "Paper A will accumulate probe scores over time with an anytime valid guarantee on false positives.", 1),
 ("C will depend on a law I discovered", "C will depend on a law I measured", 1),
 # 2. Problem
 ("An agent that can diffuse will outperform monitors", "An agent that can sabotage diffusely will defeat monitors", 1),
 ("\"appear to be theoretically and empirically less promising", "\"seem theoretically and empirically less promising", 1),
 ("that would evade monitoring that looks at actions one at a time (arXiv 2607.07368", "that would evade monitoring that looks at one instance at a time (arXiv 2607.07368", 1),
 ("No one has looked at how much it costs", "We have found no one who has looked at how much it costs", 1),
 # 3. Theory
 ("are the same thing. They are both subgroups of the permutations", "are mathematically the same thing. They both correspond to subgroups of the permutations", 1),
 ("Defender has an anytime valid false positive.", "Defender has an anytime valid guarantee on false positives.", 1),
 ("achieves Θ(γ) delay vs log γ", "finds Θ(γ) delay vs log γ", 1),
 ("They don't account for total budgets or anytime valid.", "They don't account for total budgets or anytime valid guarantees.", 1),
 ("It will have the same power as its false positive.", "It will have the same power as its false positive rate.", 1),
 ("will be able to do better than its false positive.", "will be able to do better than its false positive rate.", 1),
 ("will be greater than their false positive and the max will be less than or equal to (Slepian)", "will be greater than their false positive rate and the max will be less than or equal to it (Slepian)", 1),
 ("marginals vs copulas. Combining time and agents", "marginals vs copulas. Our contribution is combining time and agents", 1),
 ("Determining C and K and what sign they are.", "Determining C and K and the sign of their effects.", 1),
 ("We had between .21 and .35 false positives when there were episode effects.", "We had a false positive rate between .21 and .35 (instead of .05) when there were episode effects.", 1),
 # 4. Two papers / Paper A
 ("C will be finished first and A will begin and continue from month 5.", "C will be finished first and A will begin at the same time and take over from month 5.", 1),
 ("to cause many proposals to be less safe.", "to cause many proposals to be slightly worse.", 1),
 ("Like the setup in arXiv 2606.08892 they didn't release any code or data.", "Like the setup in arXiv 2606.08892, whose authors didn't release any code or data.", 1),
 ("a LoRA that instructs the agent to sabotage", "a LoRA that trains the agent to sabotage", 1),
 ("and TRACE-lite. We will reimplement the monitor from arXiv 2606.07054.", "and TRACE-lite (we will reimplement the monitor from arXiv 2606.07054).", 1),
 ("Given the same aggregation and false positive we will", "Given the same aggregation and false positive rate we will", 1),
 ("per action monitor with a 1% false positive.", "per action monitor with a 1% false positive rate.", 1),
 ("taking actions with an anytime valid false positive.", "taking actions with an anytime valid guarantee on false positives.", 1),
 ("you cannot evade probes that aggregate", "you did not evade probes that aggregate", 1),
 ("The authors believe this is because", "The authors believe this may be because", 1),
 ("sabotage success drops off faster than honest utility", "sabotage success drops off significantly faster than honest utility", 1),
 ("our best black box baseline with all modifications.", "our best black box baseline across all modifications.", 1),
 ("recall at a 1% false positive.", "recall at a 1% false positive rate.", 1),
 ("calibrate our false positive on held out", "calibrate our false positive rate on held out", 1),
 # Paper C
 ("Judges and probes will not be.", "Judges and probes will differ.", 1),
 # Paper B
 ("such that each diff is benign.", "such that each diff is benign on its own.", 1),
 # 5. Rules
 ("Do not run experiments where you expect a positive sign.", "Do not run experiments aiming for a positive sign.", 1),
 ("Ensure all stop guards trigger on a healthy case and artifact. No silent failures.", "Ensure all stop guards are tested on a healthy case and an artifact. No silent fallbacks.", 1),
 ("an adversary that has access to the infrastructure", "an adversary that controls the infrastructure", 1),
 # coquilles
 ("Pages CUSUM", "Page's CUSUM", 3),
 ("ville's inequality", "Ville's inequality", 1),
 ("the saboteurs actions", "the saboteur's actions", 1),
 ("the agents private context", "the agent's private context", 1),
 ("instructors style", "instructor's style", 2),
]
for a, b, n in reps:
    c = src.count(a)
    assert c == n, (a[:70], c)
    src = src.replace(a, b)
pathlib.Path('ws2-v5.txt').write_text(src, encoding='utf-8')
paras = [p.strip() for p in src.split('\n\n') if p.strip()]
e = html.escape
def sub(t):
    t = e(t)
    return t.replace('Xi,t', 'X<sub>i,t</sub>').replace('Σδk', 'Σδ<sub>k</sub>').replace('n0', 'n₀').replace('gprobe', 'g<sub>probe</sub>')
heads2 = {'1. Summary', '2. Problem', '3. Theory: A Lemma, Negative Theorem and Important Question', '4. Two papers one extension', '5. How we will accomplish this'}
heads3 = {'Paper A - Time (Single Agent)', 'Paper C - Instrument (Corrupting the Monitor)', 'Paper B - Swarm (Extension)'}
seuls = {'Hypotheses.', 'Other Hypotheses for Paper C.', 'Gates.', 'Experiments.'}
num = re.compile(r'^\d\. ')
out = [f'<h1>{e(paras[0])}</h1>\n<p class="note">{e(paras[1])}</p>\n<p class="sous">{e(paras[2])}</p>']
rest = paras[3:]; k = 0
while k < len(rest):
    p = rest[k]
    if p in heads2: out.append(f'<h2>{e(p)}</h2>'); k += 1; continue
    if p in heads3: out.append(f'<h3>{e(p)}</h3>'); k += 1; continue
    if p.startswith('Paper A - Time Paper C - Instrument'):
        q = p.split('\n')[1]; m = rest[k+1]; mo = rest[k+2]; g = rest[k+3]
        qa, qc, qb = re.match(r'Question (Can we accumulate .*?\.) (How much .*?\.) (Can we use .*)$', q).groups()
        ma, mc, mb = re.match(r'Method (2 x 2 .*Sequential\)) (Law of deference .*Probes) (How .*)$', m).groups()
        assert mo.startswith('Months 1-7 1-4 8-12') and g.startswith('Gates G1')
        out.append('<table>\n<tr><th></th><th>Paper A - Time</th><th>Paper C - Instrument</th><th>Paper B - Swarm (Extension)</th></tr>\n'
                   f'<tr><td class="l">Question</td><td>{e(qa)}</td><td>{e(qc)}</td><td>{e(qb)}</td></tr>\n'
                   f'<tr><td class="l">Method</td><td>{e(ma)}</td><td>{e(mc)}</td><td>{e(mb)}</td></tr>\n'
                   '<tr><td class="l">Months</td><td>1-7</td><td>1-4</td><td>8-12 Extension Only</td></tr>\n'
                   '<tr><td class="l">Gates</td><td>G1 (End of Month 4)</td><td>GC (End of Month 2)</td><td>G2, G3</td></tr>\n</table>')
        k += 4; continue
    if p.startswith('Δv = g'):
        out.append('<p class="eq">Δv = g · (c̃ − v₀)</p>'); k += 1; continue
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
    if len(p) < 70 and k + 1 < len(rest) and len(rest[k+1]) > 70 and not num.match(rest[k+1]) and not rest[k+1].startswith('Δv'):
        out.append(f'<p><b>{sub(p)}</b> {sub(rest[k+1])}</p>'); k += 2; continue
    out.append(f'<p>{sub(p)}</p>'); k += 1
tpl = pathlib.Path('ws2-final-v3.html').read_text(encoding='utf-8')
pathlib.Path('ws2-v5.html').write_text(tpl[:tpl.index('<body>')+6] + '\n' + '\n'.join(out) + '\n</body></html>', encoding='utf-8')
print(len(out), sum(n for _, _, n in reps))
