import hashlib, os, re, sys
v = [os.environ.get(k) for k in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY")]
H = r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z"
J = r"(HF_TOKEN|CONTROLE_IA_GITHUB_TOKEN|GH_TOKEN|VAST_API_KEY)"
FIXES = [re.compile(x) for x in (
    r"KO  4f module commun de S ou textes honnêtes de P3 de S illisibles : recherche des fenêtres et filtre de "
    r"l'affichage impossibles \(repli : jetons masqués ; seules les lignes OK, KO et -- de forme fixe affichées, les "
    r"autres par leur longueur et leur empreinte courte\)",
    r"OK  0 récupération exécutée = copie versée à S|KO  0 récupération exécutée ≠ copie versée à S",
    r"OK  1a S est ancêtre de la branche|KO  1a S n'est pas ancêtre de la branche",
    r"OK  1b seulement des ajouts \([0-9]+ fichiers\)|KO  1b [0-9]+ changement\(s\) autre\(s\) qu'un ajout",
    r"OK  1c ajouts aux seuls chemins permis \(manifeste, résultats et tableaux du run, traces p4-\* ; aucun texte\)",
    r"OK  1d un seul run : [0-9]{8}-[0-9]{6}-p4-[a-z]+|--  1d aucun run sur la branche : récupération des traces seules "
    r"\(arrêt avant le run\)",
    r"OK  1e commits de « instance de calcul \(P4\) » \([0-9]+\)",
    r"KO  4f fenêtres des textes honnêtes de P3 impossibles \([A-Za-z_]+\) : recherche non faite",
    r"OK  6a lignes de progression au journal : [0-9]+, toutes au motif fixe|KO  6a lignes de progression : [0-9]+, dont "
    r"[0-9]+ au motif fixe|OK  6a aucune ligne de progression sans run|KO  6a [0-9]+ ligne\(s\) de progression sans run",
    r"(OK|KO)  7 valeur de " + J + r" : [0-9]+ occurrence\(s\)",
    r"KO  7 " + J + r" absent de l'environnement de la session : recherche impossible",
    r"--  8 heure limite de destruction " + H + r" \((arrêt relu à " + H + r" \+ 24 h, arret\.txt|repli déclaré : "
    r"arret\.txt (absent|illisible|antérieur à la création|sans arrêt confirmé de l'instance [0-9]{6,10}) ; création "
    r"\+ 9 600 s \+ 24 h)\)",
    r"--  8 heure limite dépassée de [0-9]+ s : borne du disque dépassée : nœud de Lazar")]
STATUT = re.compile(r"(OK|KO|--)  [0-9]{1,2}[a-z]? ")
sys.stdin.reconfigure(encoding="utf-8", errors="replace")
for l in sys.stdin:
    l = l.rstrip("\n")
    for x in v:
        if x and len(x) > 6:
            l = l.replace(x, "***")
    if any(f.fullmatch(l) for f in FIXES):
        print(l, flush=True)
        continue
    s = STATUT.match(l)
    print(f"{s.group(0) if s else ''}(ligne de {len(l)} caractères, empreinte "
          f"{hashlib.sha256(l.encode('utf-8', 'replace')).hexdigest()[:12]})", flush=True)
