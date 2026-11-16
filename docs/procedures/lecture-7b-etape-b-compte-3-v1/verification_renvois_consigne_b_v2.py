"""Vérification par programme d'une version de la consigne du lecteur B — v2 (aide du rédacteur et du contre-lecteur ;
lecture seule). Nom neuf (règle R12) : `verification_renvois_consigne_b_v1.py` reste tel quel.

Pourquoi une v2 : la v1 lit un chemin figé, celui de la commande de la phase C en version 3, dont elle exige l'empreinte
dans la consigne ; or le brouillon 3 de la consigne nomme la commande en version 4, avec un jeton de mise au propre à la
place de son empreinte. La v2 ne fige aucun chemin ni aucun compte : elle prend en arguments la consigne, la commande d'où
elle lit les filtres, la commande dont elle lit le bloc C5, et le chemin de commande, avec son empreinte ou son jeton, que la
consigne doit nommer ; les comptes de la liste fermée sont tirés de la table de la consigne elle-même. Contrôles 1, 2, 4 et
5 : ceux de la v1 ; contrôle 3 : celui de la v1 pour les textes cités, refait pour la commande ; contrôles 6 à 8 : neufs.

Usage :
  python3 -I -B verification_renvois_consigne_b_v2.py RACINE CONSIGNE COMMANDE_FILTRES COMMANDE_PIECES COMMANDE_NOMMEE \
          EMPREINTE_OU_JETON [MOTIF_DES_NOMS_DE_MODELES]
  (chemins des commandes relatifs à RACINE ; COMMANDE_NOMMEE peut ne pas exister encore)

Contrôles, sans rien écrire :
 1. chaque renvoi de la table 3.2 (« Rnnn | fichier | ligne | citation ») : la citation est une sous-chaîne exacte de la
    ligne citée du fichier cité ;
 2. chaque « Rnnn » employé dans le corps existe dans la table, et chaque renvoi de la table est employé au moins une fois ;
 3. les empreintes écrites dans l'en-tête pour les textes cités égalent celles des fichiers ; la consigne nomme
    COMMANDE_NOMMEE une seule fois, suivi de EMPREINTE_OU_JETON entre accents graves, présent une seule fois (une empreinte
    de 64 caractères hexadécimaux doit égaler celle du fichier nommé ; sinon, un jeton de majuscules, chiffres et tirets) ;
    aucun autre nom de commande du compte 3, ni l'empreinte de l'une des deux commandes lues si elle n'est pas l'attendue ;
 4. les noms de la liste fermée de la section 9 répondent au motif recopié de la commande, et ce motif est dans
    COMMANDE_FILTRES (bloc C7) ;
 5. aucune ligne touchée par la variable INTERDITS_CONTENU_B du bloc 1C de COMMANDE_FILTRES ; aucun nom de modèle, si un
    motif est passé en septième argument (expression régulière, casse libre ; écrite ni ici ni dans la sortie) ; aucun
    marqueur à chevrons doubles ;
 6. comptes de la liste fermée : table de la section 2 numérotée de 1 à n ; une seule phrase « **2n − 1 lignes** attendues :
    <n − 1> fichiers, leurs <n − 1> compagnons » ; « lignes 1 et 3 à n » et « (<n − 1> compagnons) » ; une seule mention
    « ; 2n − 1 lignes ; » au contrôle du bordereau (section 6.1) ;
 7. pièces contre le bloc C5 de COMMANDE_PIECES : chemins littéraux de sa boucle de copie (la variable R7 remplacée par sa
    valeur, lue au bloc 1C de la même commande) égaux aux chemins des lignes de la table écrits seuls entre accents graves,
    l'extrait mis à part ; autant de variables dans la boucle que de lignes de la table sans chemin seul ; n − 1 fichiers
    dans la boucle ; noms de l'extrait et du bordereau du bloc C5 présents dans la consigne ;
 8. aucune pièce de la table nommée dans la puce « Jamais remis ».
Code de sortie : 0 si aucune faute, 1 sinon, 2 sur un usage fautif. Ne lit que la consigne, les deux commandes et les
textes scellés cités ; aucune donnée, aucun résultat.
"""
import hashlib
import pathlib
import re
import sys

FICHIERS = {"T07": "prereg/T0.7-sondes-v0-v1.md", "T06": "prereg/T0.6-organismes-v0-v1.md",
            "T08A": "prereg/T0.8-base-A-mots-et-cout-v1.md", "N063": "docs/decisions/decision-N-063-v2.md",
            "AUD": "prereg/T0.7-consigne-audit-fuites-v1.md", "ADD": "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md",
            "CONFIG": "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"}
MOTS = {10: "dix", 11: "onze", 12: "douze", 13: "treize", 14: "quatorze", 15: "quinze", 16: "seize", 17: "dix-sept"}
HEX64 = re.compile(r"^[0-9a-f]{64}$")
JETON = re.compile(r"^[A-Z0-9]+(-[A-Z0-9]+)+$")


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def table_des_pieces(texte: str) -> list:
    """Lignes « | n | pièce | ce qu'elle est | ce que tu y lis | » de la liste fermée (section 2)."""
    i = texte.find("**Liste fermée des pièces**")
    if i < 0:
        return []
    lignes = texte[i:].split("\n")[1:]
    rangs, vu = [], False
    for l in lignes:
        m = re.match(r"^\| (\d+) \| (.+?) \| (.+?) \| (.+?) \|$", l)
        if m:
            rangs.append((int(m.group(1)), m.group(2)))
            vu = True
        elif vu and not l.startswith("|"):
            break
    return rangs


def boucle_c5(commande: str):
    """(jetons de la boucle de copie du bloc C5, valeur de R7, nom de l'extrait, nom du bordereau) ou None."""
    i = commande.find("### Bloc C5")
    j = commande.find("### Bloc C6", i + 1)
    if i < 0 or j < 0:
        return None
    bloc = commande[i:j]
    a = bloc.find("for f in ")
    b = bloc.find("; do", a)
    if a < 0 or b < 0:
        return None
    jetons = [x.strip('"') for x in bloc[a + len("for f in "):b].replace("\\\n", " ").split()]
    r7 = re.search(r"\bR7=([0-9A-Za-z-]+)", commande)
    extrait = re.search(r"\$P/(extrait-[a-z0-9-]+\.md)", bloc)
    bordereau = re.search(r"(bordereau-remise-v[0-9]+\.txt)", bloc)
    if not (r7 and extrait and bordereau):
        return None
    return jetons, r7.group(1), extrait.group(1), bordereau.group(1)


def main(argv):
    if len(argv) not in (7, 8):
        print(__doc__.split("\n\n")[2])
        return 2
    racine, consigne = pathlib.Path(argv[1]), pathlib.Path(argv[2])
    ch_filtres, ch_pieces, nommee, attendue = argv[3], argv[4], argv[5], argv[6]
    texte = consigne.read_text(encoding="utf-8")
    lignes = {k: (racine / v).read_text(encoding="utf-8").split("\n") for k, v in FICHIERS.items() if k != "CONFIG"}
    cmd_filtres = (racine / ch_filtres).read_text(encoding="utf-8")
    cmd_pieces = (racine / ch_pieces).read_text(encoding="utf-8")
    fautes = 0

    # 1. table des renvois
    table, f1 = {}, 0
    for ligne in texte.split("\n"):
        m = re.match(r"^(R\d{3}) \| ([A-Z0-9]+) \| (\d+) \| (.+)$", ligne)
        if not m:
            continue
        ident, cle, n, citation = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        if ident in table:
            print(f"FAUTE : renvoi {ident} en double")
            f1 += 1
        table[ident] = (cle, n, citation)
        if cle not in lignes or not (1 <= n <= len(lignes[cle])) or citation not in lignes[cle][n - 1]:
            print(f"FAUTE : {ident} : citation absente de {cle} l. {n} : {citation[:80]}")
            f1 += 1
    print(f"1. renvois de la table : {len(table)} ; citations retrouvées à leur ligne : {len(table) - f1}")
    fautes += f1

    # 2. emplois dans le corps
    corps = "\n".join(l for l in texte.split("\n") if not re.match(r"^R\d{3} \| ", l))
    employes = set(re.findall(r"\bR(\d{3})\b", corps))
    for a, b in re.findall(r"\bR(\d{3}) à R(\d{3})\b", corps):
        employes.update(f"{i:03d}" for i in range(int(a), int(b) + 1))
    employes = {"R" + x for x in employes}
    inconnus = sorted(employes - set(table))
    inutiles = sorted(set(table) - employes)
    print(f"2. renvois employés dans le corps : {len(employes)} ; inconnus de la table : {inconnus or 'aucun'} ; "
          f"dans la table sans emploi : {inutiles or 'aucun'}")
    fautes += len(inconnus)

    # 3. empreintes de l'en-tête ; commande nommée
    ok3 = 0
    for cle, rel in FICHIERS.items():
        h = sha(racine / rel)
        if h in texte:
            ok3 += 1
        else:
            print(f"FAUTE : empreinte de {rel} ({h}) absente de la consigne")
            fautes += 1
    print(f"3. empreintes des textes cités présentes et égales aux fichiers : {ok3} sur {len(FICHIERS)}")
    f3 = 0
    n_nom = texte.count(f"`{nommee}`")
    n_att = texte.count(attendue)
    suite = re.search(re.escape(f"`{nommee}`") + r"\s*\(`" + re.escape(attendue) + r"`\)", texte)
    if n_nom != 1 or n_att != 1 or not suite:
        print(f"FAUTE : commande nommée {n_nom} fois (une attendue), empreinte ou jeton présent {n_att} fois (une attendue), "
              f"chemin suivi de « (`{attendue}`) » : {bool(suite)}")
        f3 += 1
    if HEX64.match(attendue):
        p = racine / nommee
        if not p.is_file() or sha(p) != attendue:
            print(f"FAUTE : l'empreinte attendue n'est pas celle du fichier nommé ({'absent' if not p.is_file() else sha(p)})")
            f3 += 1
        nature = "empreinte, égale au fichier nommé" if not f3 else "empreinte"
    elif JETON.match(attendue):
        nature = "jeton de mise au propre, à remplir"
    else:
        print("FAUTE : ni empreinte de 64 caractères, ni jeton de majuscules, chiffres et tirets")
        f3 += 1
        nature = "forme inconnue"
    autres = sorted(set(re.findall(r"commande-compte-3-[a-z0-9-]+\.md", texte)) - {pathlib.Path(nommee).name})
    if autres:
        print(f"FAUTE : autre(s) commande(s) nommée(s) : {autres}")
        f3 += 1
    lues = {ch_filtres: sha(racine / ch_filtres), ch_pieces: sha(racine / ch_pieces)}
    restes = sorted(c for c, h in lues.items() if h in texte and h != attendue)
    if restes:
        print(f"FAUTE : empreinte d'une commande lue présente dans la consigne : {restes}")
        f3 += 1
    print(f"   commande nommée : {nommee} ; suivie de « {attendue} » ({nature}) ; une seule fois : {n_nom == 1 and n_att == 1} ; "
          f"autres commandes nommées : {autres or 'aucune'} ; empreintes des commandes lues présentes : {restes or 'aucune'}")
    fautes += f3

    # 4. noms et motif
    motifs = re.findall(r"^\^verdict-T0.*\$$", texte, flags=re.M)
    if len(motifs) != 1:
        print(f"FAUTE : {len(motifs)} motif(s) de noms dans la consigne, un attendu")
        fautes += 1
    else:
        if motifs[0] not in cmd_filtres:
            print("FAUTE : le motif de noms de la consigne n'est pas dans la commande des filtres (bloc C7)")
            fautes += 1
        noms = sorted(set(re.findall(r"`(verdict-T0\.7-etape-B-v1[^`/ ]*)`", texte)))
        mauvais = [n for n in noms if not re.match(motifs[0], n)]
        print(f"4. noms de fichiers du verdict cités : {len(noms)} ; hors du motif : {mauvais or 'aucun'} ; motif présent dans "
              f"la commande des filtres : {motifs[0] in cmd_filtres}")
        fautes += len(mauvais)

    # 5. contenu interdit, noms de modèles, chevrons doubles
    m = re.search(r"^INTERDITS_CONTENU_B='([^']+)'$", cmd_filtres, flags=re.M)
    if not m:
        print("FAUTE : INTERDITS_CONTENU_B introuvable dans la commande des filtres")
        fautes += 1
    else:
        touchees = [i + 1 for i, l in enumerate(texte.split("\n")) if re.search(m.group(1), l, flags=re.I)]
        print(f"5. lignes de la consigne touchées par le filtre de contenu de la commande : {touchees or 'aucune'}")
        fautes += len(touchees)
    if len(argv) > 7:
        mod = [i + 1 for i, l in enumerate(texte.split("\n")) if re.search(argv[7], l, flags=re.I)]
        print(f"   lignes portant un nom de modèle (motif passé en argument, non écrit) : {mod or 'aucune'}")
        fautes += len(mod)
    else:
        print("   noms de modèles : non cherchés (aucun motif passé en argument)")
    chevrons = [i + 1 for i, l in enumerate(texte.split("\n")) if "<<" in l or ">>" in l]
    print(f"   lignes portant un marqueur à chevrons doubles : {chevrons or 'aucune'}")
    fautes += len(chevrons)

    # 6. comptes de la liste fermée
    rangs = table_des_pieces(texte)
    n = len(rangs)
    f6 = 0
    if n == 0 or [r for r, _ in rangs] != list(range(1, n + 1)):
        print(f"FAUTE : table de la liste fermée absente ou mal numérotée : {[r for r, _ in rangs]}")
        f6 += 1
    else:
        mot = MOTS.get(n - 1, "?")
        phrases = re.findall(r"\*\*(\d+) lignes\*\* attendues : (\S+) fichiers, leurs\s+(\S+)\s+compagnons", texte)
        if phrases != [(str(2 * n - 1), mot, mot)]:
            print(f"FAUTE : phrase du bordereau {phrases} ; attendu : [('{2 * n - 1}', '{mot}', '{mot}')]")
            f6 += 1
        comp = re.findall(r"Chaque pièce des lignes 1 et 3 à (\d+) a son compagnon `<pièce>\.sha256` \((\S+) compagnons\)", texte)
        if comp != [(str(n), mot)]:
            print(f"FAUTE : phrase des compagnons {comp} ; attendu : [('{n}', '{mot}')]")
            f6 += 1
        c61 = re.findall(r"à son compagnon ; (\d+) lignes ;", texte)
        if c61 != [str(2 * n - 1)]:
            print(f"FAUTE : compte du contrôle du bordereau {c61} ; attendu : ['{2 * n - 1}']")
            f6 += 1
        print(f"6. liste fermée : {n} lignes numérotées de 1 à {n} ; bordereau attendu : {2 * n - 1} lignes ({mot} fichiers, "
              f"{mot} compagnons, l'extrait) ; phrases de la section 2 et du contrôle 6.1 conformes : {f6 == 0}")
    fautes += f6

    # 7. pièces contre le bloc C5 de la commande des pièces
    f7 = 0
    lu = boucle_c5(cmd_pieces)
    if lu is None or n == 0:
        print("FAUTE : boucle de copie du bloc C5 introuvable (ou table absente)")
        f7 += 1
    else:
        jetons, r7, extrait, bordereau = lu
        jetons = [j.replace("$R7", r7) for j in jetons]
        variables = [j for j in jetons if "$" in j]
        litteraux = {j for j in jetons if "$" not in j}
        seuls = {}
        for r, cellule in rangs:
            mm = re.match(r"^`([^`]+)`$", cellule)
            if mm:
                seuls[r] = mm.group(1)
        sans_chemin = [r for r, _ in rangs if r not in seuls]
        table_lit = set(seuls.values()) - {extrait}
        if table_lit != litteraux:
            print(f"FAUTE : pièces de la table hors du bloc C5 : {sorted(table_lit - litteraux) or 'aucune'} ; "
                  f"fichiers du bloc C5 hors de la table : {sorted(litteraux - table_lit) or 'aucun'}")
            f7 += 1
        if extrait not in seuls.values():
            print(f"FAUTE : l'extrait du bloc C5 ({extrait}) n'est pas une ligne de la table")
            f7 += 1
        if len(variables) != len(sans_chemin):
            print(f"FAUTE : {len(variables)} variable(s) dans la boucle ({variables}) ; {len(sans_chemin)} ligne(s) de la table "
                  f"sans chemin seul ({sans_chemin})")
            f7 += 1
        if len(jetons) != n - 1:
            print(f"FAUTE : {len(jetons)} fichiers dans la boucle du bloc C5 ; {n - 1} attendus (table de {n} lignes, extrait à part)")
            f7 += 1
        if bordereau not in texte:
            print(f"FAUTE : bordereau du bloc C5 ({bordereau}) absent de la consigne")
            f7 += 1
        print(f"7. bloc C5 de {pathlib.Path(ch_pieces).name} : {len(jetons)} fichiers copiés ({len(litteraux)} chemins écrits, "
              f"{len(variables)} variables : {', '.join(variables)}) ; table : {len(seuls)} chemins seuls dont l'extrait, "
              f"{len(sans_chemin)} lignes sans chemin seul ({', '.join(map(str, sans_chemin))}) ; accord : {f7 == 0}")
        for p in sorted(litteraux):
            print(f"     {p}")
    fautes += f7

    # 8. aucune pièce de la table dans la puce « Jamais remis »
    f8 = 0
    i = texte.find("- **Jamais remis")
    if i < 0:
        print("FAUTE : puce « Jamais remis » introuvable")
        f8 += 1
    else:
        fin = texte.find("\n- ", i + 1)
        puce = texte[i:fin if fin > 0 else len(texte)]
        noms_pieces = sorted({pathlib.PurePosixPath(p).name for p in (seuls.values() if lu and n else [])})
        dedans = [b for b in noms_pieces if re.search(r"(?<![\w.-])" + re.escape(b) + r"(?![\w.-])", puce)]
        if dedans:
            print(f"FAUTE : pièce(s) de la table nommée(s) dans la puce « Jamais remis » : {dedans}")
            f8 += 1
        print(f"8. puce « Jamais remis » : {len(noms_pieces)} noms de pièces cherchés ; présents : {dedans or 'aucun'}")
    fautes += f8

    print("VERDICT :", "CONFORME" if fautes == 0 else f"{fautes} FAUTE(S)")
    return 0 if fautes == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
