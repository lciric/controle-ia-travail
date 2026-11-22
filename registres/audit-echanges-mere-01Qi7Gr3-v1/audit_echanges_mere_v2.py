"""Audit des échanges de la mère contre le dépôt — v2 (classe B, à contre-lire). v2 : ajoute les messages de Lazar arrivés en cours de tour (rendus dans les résultats d'outils).

Lit les journaux bruts de la session (JSON Lines de Claude Code), en extrait :
  1. chaque message de Lazar (texte saisi, hors notifications et rappels du système), horodaté ;
  2. chaque consigne de la mère aux sessions filles (send_message, create_session) ;
  3. chaque mandat donné à un agent (Agent : description, prompt) et chaque rapport rendu (<agent-message>) ;
  4. chaque fichier écrit par Write/Edit sous le dépôt, et sa présence dans `git ls-files` ;
et pour chaque message de Lazar, les lignes GO et R écrites dans les trois heures qui suivent.
Sorties : JSON Lines et un rapport Markdown, dans le dossier --sortie. Le courriel de l'utilisateur est masqué.
Usage : python3 audit_echanges_mere_v1.py --journal J1.jsonl [--journal J2.jsonl] --depot CHEMIN --sortie DOSSIER --masque COURRIEL
"""
import argparse, json, os, re, subprocess, datetime as dt

def textes(contenu):
    if isinstance(contenu, str):
        return [contenu]
    out = []
    for c in contenu or []:
        if isinstance(c, dict) and c.get('type') == 'text':
            out.append(c.get('text', ''))
    return out

BRUIT = ('<system-reminder', '[SYSTEM NOTIFICATION', '<task-notification', 'This session is being continued',
         'Stop hook feedback', '<command-name>', 'Tool loaded.', 'Another Claude session sent a message')

def lire(journaux):
    for j in journaux:
        with open(j, encoding='utf-8') as f:
            for n, l in enumerate(f):
                try:
                    yield j, n, json.loads(l)
                except Exception:
                    continue

def heure(e):
    t = e.get('timestamp')
    return dt.datetime.fromisoformat(t.replace('Z', '+00:00')) if t else None

def main():
    a = argparse.ArgumentParser()
    a.add_argument('--journal', action='append', required=True)
    a.add_argument('--depot', required=True)
    a.add_argument('--sortie', required=True)
    a.add_argument('--masque', default='')
    x = a.parse_args()
    os.makedirs(x.sortie, exist_ok=True)
    m = (lambda s: s.replace(x.masque, '[courriel masqué]')) if x.masque else (lambda s: s)
    lazar, consignes, mandats, rapports, ecrits = [], [], [], [], []
    vus = set()
    for j, n, e in lire(x.journal):
        msg = e.get('message') or {}
        if e.get('type') == 'user' and msg.get('role') == 'user' and not e.get('isSidechain'):
            for t in textes(msg.get('content')):
                s = t.strip()
                if not s:
                    continue
                if s.startswith('<agent-message') or 'Subagent hand-back' in s[:400]:
                    rapports.append({'heure': e.get('timestamp'), 'texte': m(s)})
                    continue
                if any(s.startswith(b) or b in s[:200] for b in BRUIT):
                    continue
                cle = (s[:200], e.get('timestamp', '')[:16])
                if cle in vus:
                    continue
                vus.add(cle)
                lazar.append({'heure': e.get('timestamp'), 'uuid': e.get('uuid'), 'texte': m(s)})
        if e.get('type') in ('user', 'attachment', 'system') or 'The user sent a new message' in json.dumps(e, ensure_ascii=False)[:0] or True:
            brut = json.dumps(e, ensure_ascii=False)
            for mm in re.finditer(r'The user sent a new message while you were working:\\n(.*?)\\n\\nThis is how', brut):
                s = json.loads('"' + mm.group(1) + '"').strip()
                cle = (s[:200],)
                if s and cle not in vus:
                    vus.add(cle)
                    lazar.append({'heure': e.get('timestamp'), 'uuid': e.get('uuid'), 'texte': m(s), 'en_cours_de_tour': True})
        if e.get('type') == 'assistant':
            for c in msg.get('content') or []:
                if not isinstance(c, dict) or c.get('type') != 'tool_use':
                    continue
                nom, inp = c.get('name', ''), c.get('input') or {}
                if nom.endswith('send_message') or nom.endswith('create_session'):
                    consignes.append({'heure': e.get('timestamp'), 'outil': nom, 'session': inp.get('session_id'),
                                      'texte': m(inp.get('message') or inp.get('prompt') or ''), 'titre': inp.get('title')})
                elif nom == 'Agent':
                    mandats.append({'heure': e.get('timestamp'), 'description': inp.get('description'),
                                    'type': inp.get('subagent_type'), 'prompt': m(inp.get('prompt', ''))})
                elif nom in ('Write', 'Edit'):
                    ecrits.append({'heure': e.get('timestamp'), 'outil': nom, 'chemin': inp.get('file_path')})
    lazar.sort(key=lambda q: q['heure'] or '')
    suivis = set(subprocess.run(['git', '-C', x.depot, 'ls-files'], capture_output=True, text=True).stdout.split('\n'))
    for w in ecrits:
        p = w['chemin'] or ''
        rel = os.path.relpath(p, x.depot) if p.startswith(x.depot) else None
        w['dans_depot'] = (rel in suivis) if rel else None
    regs = []
    for nomf in ('registres/go.md', 'registres/decisions.md'):
        for l in open(os.path.join(x.depot, nomf), encoding='utf-8'):
            h = re.search(r'(2026-11-\d\dT\d\d:\d\d(:\d\d)?Z)', l)
            ident = re.match(r'[-|] *(R-\d+|GO-\d{4}-\d\d-\d\d-\d\d)', l.strip())
            if h and ident:
                regs.append((dt.datetime.fromisoformat(h.group(1).replace('Z', '+00:00')), ident.group(1)))
    for q in lazar:
        t = dt.datetime.fromisoformat(q['heure'].replace('Z', '+00:00')) if q['heure'] else None
        q['lignes_3h'] = sorted({i for (h, i) in regs if t and t <= h <= t + dt.timedelta(hours=3)})[:40] if t else []
    for nom, l in (('mots-lazar', lazar), ('consignes-aux-filles', consignes), ('mandats-agents', mandats),
                   ('rapports-agents', rapports), ('fichiers-ecrits', ecrits)):
        with open(os.path.join(x.sortie, nom + '.jsonl'), 'w', encoding='utf-8') as f:
            for r in l:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
    hors = [w for w in ecrits if w['dans_depot'] is False]
    sans = [q for q in lazar if not q['lignes_3h']]
    with open(os.path.join(x.sortie, 'rapport-audit.md'), 'w', encoding='utf-8') as f:
        f.write('# Rapport d’audit des échanges de la mère contre le dépôt (v2)\n\n')
        f.write(f'- Journaux lus : {len(x.journal)}\n- Messages de Lazar : {len(lazar)} ; sans ligne GO ni R dans les trois heures : {len(sans)}\n')
        f.write(f'- Consignes aux sessions filles : {len(consignes)}\n- Mandats d’agents : {len(mandats)} ; rapports rendus : {len(rapports)}\n')
        f.write(f'- Fichiers écrits sous le dépôt : {sum(1 for w in ecrits if w["dans_depot"] is not None)} ; absents de git : {len(hors)}\n\n')
        f.write('## Messages de Lazar sans ligne de registre dans les trois heures (à lire un par un)\n\n')
        for q in sans:
            f.write(f'- {q["heure"]} — {q["texte"][:300].replace(chr(10), " ")}\n')
        f.write('\n## Fichiers écrits sous le dépôt et absents de git\n\n')
        for w in hors:
            f.write(f'- {w["heure"]} — {w["chemin"]}\n')
    print(len(lazar), len(sans), len(consignes), len(mandats), len(rapports), len(ecrits), len(hors))

if __name__ == '__main__':
    main()
