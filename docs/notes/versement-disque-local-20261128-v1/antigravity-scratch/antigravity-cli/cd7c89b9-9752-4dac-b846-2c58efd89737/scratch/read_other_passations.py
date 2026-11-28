import json
import subprocess
from pathlib import Path

targets = [
    ('organisme/service-groupe-attelage-v1', 'd44d074f'),
    ('dossier-entretien/reprise-2026-11-23-v1', '868f8cc0'),
    ('idees/questions-directeur-2026-11-24-v1', '40ac7870'),
    ('idees/protocole-x-dossiers-3-a-5-fable-v1', 'e873dda3'),
    ('code/dose-reponse-consigne-cachee-v1', 'd6dbe772'),
    ('barreau8/conductrice-lecture-sondes-v1', '974c90b1'),
    ('claude/veille-de-cap-v1', '13fb5803'),
    ('claude/iib-executante-v8', '47437214'),
    ('protocole-x/entrainement-et-juges-v1', '8302c5d1'),
    ('banque/dose-reponse-consigne-cachee-v1', '5756d589'),
    ('idees/note-hypotheses-latex-v1', '788226f7'),
    ('claude/upbeat-edison-t3wegg', '332e95f9'),
    ('lancement/dose-reponse-v1', 'cf9bd87b'),
    ('audit/protocole-x-v1', '1e20084c'),
]

main_passations = [
    '2026-11-24-0920-mere-claude-code-016QhUrvi45g3jX5saFefVED.md',
    '2026-11-24-0935-mere-compte-01Qi7-reprise-chemin-critique.md',
    '2026-11-24-1259-executante-rejeu-activations-v8-phase-2.md',
    '2026-11-24-1406-plan-turing-processeur-file-fable-suspendue.md',
    '2026-11-24-1811-developpeur-cote-moniteurs-code-lecture-sondes-v6.md',
]

out = []

def gh_raw(path, ref=None):
    url = f'repos/lciric/controle-ia-travail/contents/{path}'
    if ref:
        url += f'?ref={ref}'
    p = subprocess.run(['gh', 'api', '-H', 'Accept: application/vnd.github.raw', url], text=True, capture_output=True)
    return p.stdout if p.returncode == 0 else f'[ERR {p.returncode}: {p.stderr.strip()}]'

for mp in main_passations:
    out.append(f'\n==================== MAIN: {mp} ====================')
    out.append(gh_raw(f'registres/passations/{mp}'))

for branch, sha in targets:
    p = subprocess.run(['gh', 'api', f'repos/lciric/controle-ia-travail/commits/{sha}'], text=True, capture_output=True)
    if p.returncode != 0:
        out.append(f'\n==================== {branch} ({sha}) ERR ====================')
        continue
    c = json.loads(p.stdout)
    headline = c['commit']['message'].splitlines()[0]
    out.append(f'\n==================== {branch} ({sha}) | {headline} ====================')
    files = [f['filename'] for f in c.get('files', [])]
    out.append('Files in commit: ' + ', '.join(files[:20]))
    for fn in files:
        low = fn.lower()
        if any(bad in low for bad in ('score', 'verdict', 'coffre', 'episode', 'consigne-privee', 'qui-a-lu-quoi')):
            continue
        if low.endswith('.md') and (
            'passation' in low
            or 'additif' in low
            or 'complement' in low
            or 'cycle' in low
            or 'bulletin' in low
            or 'lancement' in low
            or 'lignes-a-verser' in low
            or 'audit-protocole-x' in low
        ):
            txt = gh_raw(fn, sha)
            if len(txt) > 6000:
                txt = txt[:6000] + '\n...[TRUNCATED]...'
            out.append(f'\n--- FILE: {fn} ---\n' + txt)

dest = Path(r'C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\other_passations_dump.txt')
dest.write_text('\n'.join(out), encoding='utf-8')
print(f'Wrote {len(dest.read_text(encoding="utf-8"))} chars to {dest}')
