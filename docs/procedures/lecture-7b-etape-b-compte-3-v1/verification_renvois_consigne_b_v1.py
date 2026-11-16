"""Vérification par programme de la consigne du lecteur B (aide du rédacteur et du contre-lecteur ; lecture seule).

Usage : python3 -I -B verification_renvois_consigne_b_v1.py RACINE_DU_DEPOT CONSIGNE [MOTIF_DES_NOMS_DE_MODELES]

Contrôles, sans rien écrire :
 1. chaque renvoi de la table 3.2 (« Rnnn | fichier | ligne | citation ») : la citation est une sous-chaîne exacte de la
    ligne citée du fichier cité ;
 2. chaque « Rnnn » employé dans le corps existe dans la table, et chaque renvoi de la table est employé au moins une fois ;
 3. les empreintes écrites dans l'en-tête de la consigne pour les textes cités égalent celles des fichiers ;
 4. les noms de la liste fermée de la section 9 répondent au motif recopié de la commande, et ce motif est celui du bloc C7 ;
 5. aucun mot de la liste de contenu interdite par la commande (variable INTERDITS_CONTENU_B du bloc 1C, lue dans la
    commande elle-même) ; aucun nom de modèle, si un motif de noms est passé en troisième argument (expression
    régulière, casse libre ; elle n'est écrite ni ici ni dans la sortie) ; aucun marqueur à chevrons doubles.
Ne lit que la consigne, la commande et les textes scellés cités ; aucune donnée, aucun résultat.
"""
import hashlib
import pathlib
import re
import sys

FICHIERS = {"T07": "prereg/T0.7-sondes-v0-v1.md", "T06": "prereg/T0.6-organismes-v0-v1.md",
            "T08A": "prereg/T0.8-base-A-mots-et-cout-v1.md", "N063": "docs/decisions/decision-N-063-v2.md",
            "AUD": "prereg/T0.7-consigne-audit-fuites-v1.md", "ADD": "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md",
            "CONFIG": "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"}
COMMANDE = "docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v3.md"


def main(argv):
    racine, consigne = pathlib.Path(argv[1]), pathlib.Path(argv[2])
    texte = consigne.read_text(encoding="utf-8")
    lignes = {k: (racine / v).read_text(encoding="utf-8").split("\n") for k, v in FICHIERS.items() if k != "CONFIG"}
    fautes = 0

    # 1. table des renvois
    table = {}
    for ligne in texte.split("\n"):
        m = re.match(r"^(R\d{3}) \| ([A-Z0-9]+) \| (\d+) \| (.+)$", ligne)
        if not m:
            continue
        ident, cle, n, citation = m.group(1), m.group(2), int(m.group(3)), m.group(4)
        if ident in table:
            print(f"FAUTE : renvoi {ident} en double")
            fautes += 1
        table[ident] = (cle, n, citation)
        if cle not in lignes or not (1 <= n <= len(lignes[cle])) or citation not in lignes[cle][n - 1]:
            print(f"FAUTE : {ident} : citation absente de {cle} l. {n} : {citation[:80]}")
            fautes += 1
    print(f"1. renvois de la table : {len(table)} ; citations retrouvées à leur ligne : {len(table) - fautes}")

    # 2. emplois dans le corps
    corps = "\n".join(l for l in texte.split("\n") if not re.match(r"^R\d{3} \| ", l))
    employes = set(re.findall(r"\bR(\d{3})\b", corps))
    # plages « R001 à R006 »
    for a, b in re.findall(r"\bR(\d{3}) à R(\d{3})\b", corps):
        employes.update(f"{i:03d}" for i in range(int(a), int(b) + 1))
    employes = {"R" + x for x in employes}
    inconnus = sorted(employes - set(table))
    inutiles = sorted(set(table) - employes)
    print(f"2. renvois employés dans le corps : {len(employes)} ; inconnus de la table : {inconnus or 'aucun'} ; "
          f"dans la table sans emploi : {inutiles or 'aucun'}")
    fautes += len(inconnus)

    # 3. empreintes de l'en-tête
    ok3 = 0
    for cle, rel in FICHIERS.items():
        h = hashlib.sha256((racine / rel).read_bytes()).hexdigest()
        if h in texte:
            ok3 += 1
        else:
            print(f"FAUTE : empreinte de {rel} ({h}) absente de la consigne")
            fautes += 1
    hc = hashlib.sha256((racine / COMMANDE).read_bytes()).hexdigest()
    if hc not in texte:
        print("FAUTE : empreinte de la commande absente de la consigne")
        fautes += 1
    print(f"3. empreintes des textes cités présentes et égales aux fichiers : {ok3} sur {len(FICHIERS)} ; commande : {hc in texte}")

    # 4. noms et motif
    commande = (racine / COMMANDE).read_text(encoding="utf-8")
    motifs = re.findall(r"^\^verdict-T0.*\$$", texte, flags=re.M)
    if len(motifs) != 1:
        print(f"FAUTE : {len(motifs)} motif(s) de noms dans la consigne, un attendu")
        fautes += 1
    else:
        if motifs[0] not in commande:
            print("FAUTE : le motif de noms de la consigne n'est pas dans la commande (bloc C7)")
            fautes += 1
        noms = sorted(set(re.findall(r"`(verdict-T0\.7-etape-B-v1[^`/ ]*)`", texte)))
        mauvais = [n for n in noms if not re.match(motifs[0], n)]
        print(f"4. noms de fichiers du verdict cités : {len(noms)} ; hors du motif : {mauvais or 'aucun'} ; motif présent dans la commande : {motifs[0] in commande}")
        fautes += len(mauvais)
        for n in noms:
            print(f"     {n}")

    # 5. contenu interdit, noms de modèles
    m = re.search(r"^INTERDITS_CONTENU_B='([^']+)'$", commande, flags=re.M)
    if not m:
        print("FAUTE : INTERDITS_CONTENU_B introuvable dans la commande")
        fautes += 1
    else:
        touchees = [i + 1 for i, l in enumerate(texte.split("\n")) if re.search(m.group(1), l, flags=re.I)]
        print(f"5. lignes de la consigne touchées par le filtre de contenu de la commande : {touchees or 'aucune'}")
        fautes += len(touchees)
    if len(argv) > 3:
        mod = [i + 1 for i, l in enumerate(texte.split("\n")) if re.search(argv[3], l, flags=re.I)]
        print(f"   lignes portant un nom de modèle (motif passé en argument, non écrit) : {mod or 'aucune'}")
        fautes += len(mod)
    else:
        print("   noms de modèles : non cherchés (aucun motif passé en argument)")
    restes = [i + 1 for i, l in enumerate(texte.split("\n")) if "<<" in l or ">>" in l]
    print(f"   lignes portant un marqueur à chevrons doubles : {restes or 'aucune'}")
    fautes += len(restes)
    print("VERDICT :", "CONFORME" if fautes == 0 else f"{fautes} FAUTE(S)")
    return 0 if fautes == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
