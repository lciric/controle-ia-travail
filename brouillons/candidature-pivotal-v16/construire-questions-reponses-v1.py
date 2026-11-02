import html, pathlib, re, sys
M = pathlib.Path('/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/mentors')
P = pathlib.Path('/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16')
def between(s, a, b=None):
    i = s.index(a) + len(a); j = s.index(b, i) if b else len(s)
    return s[i:j].strip()
def rd(n): return (M/n).read_text(encoding='utf-8')
h = rd('mentor-3-heimersheim-v22.md'); k = rd('mentor-2-kirchner-v24.md'); jf = rd('mentor-6-jang-feng-v20.md')
sc = rd('mentor-4-scheurer-v14.md'); ib = rd('mentor-1-ibrahim-v16.md'); cw = rd('mentor-5-colognese-ward-v14.md')
sel = (P/'selection-mentors-champ-libre-v1.md').read_text(encoding='utf-8').strip().split('\n\n')[-1]
S = [
 ('Stefan Heimersheim', 'mentor-3-heimersheim-v22.md', [
   ("Pick an interpretability direction from this list and explain the most likely reasons the research direction might fail (won't solve interpretability / won't achieve its goal), and why you think that: a) Sparse Autoencoders in general; b) Activation steering in general; c) Activation steering against evaluation awareness; d) Manifold steering; e) Stochastic Parameter Decomposition or Attribution-based Parameter Decomposition; f) Feature-specific error correction as a way to identify LLM features; g) Training weight sparse transformers. If you're not familiar with these, pick another method that you know, though I prefer if you chose one of the above if possible. You're allowed to use LLMs for search (though be aware that this may lead you to the same boring answer as everyone else). You must NOT use LLMs to write the answer to this question nor closely follow an AI-written answer, please stick to 100% human-written text. Don't worry if your language / grammar aren't perfect.", between(h, '### Full version\n', '### 150-word version'), None),
   ("Why do you want to work on Mechanistic Interpretability? Max. 150 words; spend the majority of time on Q1.", between(h, '(under 150 words)\n'), 150)]),
 ('Jan Hendrik Kirchner', 'mentor-2-kirchner-v24.md', [
   ("Describe an empirical research project you drove yourself. What was the question, what did you build or run, and what was the most surprising thing you found? If relevant, you may choose your project answer from the main application.", between(k, '## Q1 — an empirical research project you drove yourself\n', '## Q2'), None),
   ("Pick an open problem in AI alignment you think is underrated. What experiment would you run first, and what result would change your mind?", between(k, '## Q2 — an underrated open problem, the first experiment, and what would change my mind\n'), None)]),
 ('Shi Feng & Eyon Jang', 'mentor-6-jang-feng-v20.md', [
   ("What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations?", between(jf, '## Answer\n'), None)]),
 ('Jérémy Scheurer', 'mentor-4-scheurer-v14.md', [
   ("Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring. You are free to chose whatever concept works best for you. What I mean by a scaling trend is a similar trend to METR's task horizon or the scaling trend of research taste. We want to roughly be able to make a statement such as: \"AI's [bad propensity/capability]\" / \"Our ability to monitor AIs via [insert control scheme] grows/declines roughly with a factor of X each month/year.\" You are allowed to leverage existing literature and get inspired by it. Be aware that both trends mentioned above are for standard capabilities, doing this for misalignment and related concepts can be hard for various reasons. Try to design your approach such that it is likely to be successful. Go", between(sc, '## Answer\n'), None)]),
 ('Lujain Ibrahim', 'mentor-1-ibrahim-v16.md', [
   ("Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading.", 'Direction 1:' + between(ib, 'Direction 1:', '## Q2'), None),
   ("Describe a technical project where you trained or evaluated LLMs (feel free to link to code or any public documentation/write up if you have something to share).", between(ib, '## Q2 — Describe a technical project where you trained or evaluated LLMs\n'), None)]),
 ('Paul Colognese & Francis Rhys Ward', 'mentor-5-colognese-ward-v14.md', [
   ("Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words)", between(cw, '## Q1 — Describe an ML experiment you ran end to end (max 200 words)\n', '## Q2 (optional)'), 200),
   ("(Optional) Read this post (\"Character training can mitigate reward hacking, but can also make it harder to detect\"). Should we have done anything differently? What was the most interesting finding in your view and why?", between(cw, '## Q2 (optional) — their post: anything to do differently, most interesting finding\n'), None)]),
 ('Mentor selection', 'selection-mentors-champ-libre-v1.md', [
   ("(Optional) Is there anything else you want to say about your mentor selection?", sel, None)]),
]
e = html.escape
def body(t):
    t = re.sub(r'([1-9])️?⃣', r'(\1)', t)
    paras = [p.strip() for p in t.split('\n\n') if p.strip()]
    return '\n'.join('<p>' + '<br>'.join(e(l) for l in p.split('\n')) + '</p>' for p in paras)
out = []
for name, src, qs in S:
    out.append(f'<h2>{e(name)}</h2>')
    for qi, (q, a, lim) in enumerate(qs, 1):
        n = len([w for w in a.split() if w not in ('—', '–')])
        meta = f'{n} words' + (f' (limit {lim})' if lim else '') + f' · source: {src}'
        out.append(f'<div class="q"><span class="qn">Q{qi}.</span> {e(q)}</div>\n<div class="a">{body(a)}</div>\n<div class="meta">{e(meta)}</div>')
css = """@page { size: A4; margin: 15mm 15mm 14mm 15mm; }
body { font-family: 'DejaVu Serif', serif; font-size: 9.2pt; line-height: 1.32; color: #111; background: #fff; }
h1 { font-size: 13pt; margin: 0 0 2mm 0; } .sous { color: #444; margin: 0 0 4mm 0; font-size: 8.5pt; }
h2 { font-size: 11pt; margin: 6mm 0 2mm 0; border-bottom: 0.4pt solid #888; padding-bottom: 1mm; break-after: avoid; }
.q { font-weight: bold; margin: 3mm 0 1.5mm 0; break-after: avoid; } .qn { color: #333; }
.a p { margin: 0 0 1.8mm 0; text-align: justify; } .meta { color: #666; font-size: 7.5pt; margin: 0 0 3mm 0; }"""
doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Pivotal mentor answers</title><style>{css}</style></head><body>
<h1>Pivotal Research Fellowship 2027 Q1 — mentor questions and answers</h1>
<p class="sous">Lazar Ciric · final versions, 2 November 2026 · keycap numbers rendered as (1)…(6) in this PDF only</p>
{chr(10).join(out)}
</body></html>"""
pathlib.Path(sys.argv[1]).write_text(doc, encoding='utf-8'); print('ok')
