#!/usr/bin/env python3
"""Recopie pure, par programme, des corrections de la contre-lecture de la synthèse DiscoveryAgent (v2).

Écrit le 19 novembre 2026 par Claude Opus 5.5, en écart déclaré à la règle « la
conception par Fable » (précédent R-3791) : rien n'est conçu ici, tout est recopié.

Se lance avec `python3 -I`, depuis n'importe où :
    python3 -I appliquer-couples-v2.py [--ecrire] [--sortie=CHEMIN]

Sans `--ecrire`, tout se fait en mémoire et rien n'est écrit (essai).
Avec `--ecrire`, trois fichiers neufs sont écrits ; le programme refuse d'en
écraser un qui existe déjà (règle R12) :
  1. `../synthese-discoveryagent-pour-l-organisme-v2.md` : la note v1, à laquelle
     les couples « > AVANT : » / « > APRÈS : » du § 8 de la contre-lecture sont
     appliqués à la lettre et dans l'ordre. Le texte d'un couple va du premier
     caractère après le préfixe jusqu'à la fin de la ligne du fichier brut.
     Chaque « avant » doit se trouver une seule fois (occurrences chevauchantes
     comprises) dans le texte courant au moment où son couple s'applique. Au
     premier couple qui ne s'applique pas, le programme s'arrête net et n'écrit
     aucun des trois fichiers. Contrôle croisé : l'empreinte du texte corrigé doit
     égaler celle que donne la sortie scellée du programme du contre-lecteur.
  2. `citations-synthese-v2.json` : le registre v1 du rédacteur, plus les
     citations marquées « a_verser » du registre de la contre-lecture, champ
     « a_verser » retiré, dans la forme du registre du rédacteur (même mise en
     page, éprouvée en reproduisant le registre v1 octet pour octet) ; chaque
     citation neuve suit la dernière citation de sa lettre (P, A, C, X, N).
  3. `verifier_citations_synthese_v2.py` : copie du programme v1 du rédacteur où
     seuls changent les noms des fichiers lus (registre et note).
`--sortie=CHEMIN` écrit aussi le journal dans ce fichier (refusé s'il existe).
Aucun réseau, aucun appel à git, aucune exécution d'un autre programme. Les
gardes d'arrêt sont éprouvées à chaque lancement, sur un cas sain et sur des
artefacts (règle R5).
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
DOSSIER = ICI.parent
NOTE_V1 = DOSSIER / "synthese-discoveryagent-pour-l-organisme-v1.md"
NOTE_V2 = DOSSIER / "synthese-discoveryagent-pour-l-organisme-v2.md"
CONTRE_LECTURE = DOSSIER / "contre-lecture-synthese-discoveryagent-v1.md"
OUTILS_CONTRE = DOSSIER / "outils-contre-lecture-synthese-v1"
REG_CONTRE = OUTILS_CONTRE / "citations-contre-lecture-v1.json"
SORTIE_CONTRE = OUTILS_CONTRE / "sortie-verification-contre-lecture-v1.txt"
REG_V1 = ICI / "citations-synthese-v1.json"
REG_V2 = ICI / "citations-synthese-v2.json"
PROG_V1 = ICI / "verifier_citations_synthese_v1.py"
PROG_V2 = ICI / "verifier_citations_synthese_v2.py"

# Préfixes d'empreinte donnés par le mandat ; chaque entrée est aussi contrôlée contre son compagnon.
ENTREES = (
    (NOTE_V1, "06d55b7c"),
    (CONTRE_LECTURE, "da3f39be"),
    (REG_V1, "8626bba0"),
    (PROG_V1, "b2d9ba6f"),
    (REG_CONTRE, None),
    (SORTIE_CONTRE, None),
)
PREFIXE_AVANT = "> AVANT : "
PREFIXE_APRES = "> APRÈS : "
TITRE_8 = "## 8. Constats et corrections"
TITRE_TABLE = "## Annexe — table des citations vérifiées"
NB_COUPLES = 54
NB_A_VERSER = 60
# (ancien nom, nouveau nom, nombre d'occurrences attendu dans le programme v1)
NOMS_PROG = (
    ("citations-synthese-v1.json", "citations-synthese-v2.json", 2),
    ("synthese-discoveryagent-pour-l-organisme-v1.md", "synthese-discoveryagent-pour-l-organisme-v2.md", 1),
)
MOTIF_ID = re.compile(r"\b([PACXN]\d{2})\b")

JOURNAL = []


class Arret(Exception):
    """Arrêt net : aucun fichier de sortie n'est écrit."""


def dire(texte=""):
    JOURNAL.append(texte)
    print(texte)


def muet(texte=""):
    pass


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def lire_scelle(chemin, prefixe):
    octets = chemin.read_bytes()
    h = sha(octets)
    ligne = Path(str(chemin) + ".sha256").read_text(encoding="utf-8").strip()
    m = re.fullmatch(r"([0-9a-f]{64})  (\S.*)", ligne)
    if not m or m.group(1) != h or m.group(2) != chemin.name:
        raise Arret(f"{chemin.name} : empreinte {h[:12]}… non conforme à son compagnon")
    if prefixe and not h.startswith(prefixe):
        raise Arret(f"{chemin.name} : empreinte {h[:12]}… au lieu de {prefixe}… (mandat)")
    dire(f"entrée {chemin.name} : sha256 {h} ; compagnon conforme"
         + (f" ; préfixe du mandat {prefixe} conforme" if prefixe else ""))
    return octets


def texte_brut(octets, nom):
    texte = octets.decode("utf-8")
    if "\r" in texte:
        raise Arret(f"{nom} : retour chariot trouvé, lecture brute ambiguë")
    return texte


def lire_couples(texte_cl):
    """Couples du § 8, dans l'ordre du fichier : (nom, ligne, avant, après)."""
    lignes = texte_cl.split("\n")
    if lignes.count(TITRE_8) != 1:
        raise Arret("titre du § 8 de la contre-lecture introuvable ou multiple")
    debut = lignes.index(TITRE_8)
    fin = next((i for i in range(debut + 1, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
    hors = [i + 1 for i, l in enumerate(lignes)
            if (l.startswith(PREFIXE_AVANT) or l.startswith(PREFIXE_APRES)) and not debut < i < fin]
    if hors:
        raise Arret(f"lignes de couple hors du § 8 : {hors}")
    couples, nom, par_titre = [], None, {}
    i = debut + 1
    while i < fin:
        l = lignes[i]
        m = re.fullmatch(r"#### (Correction \S+)", l)
        if m:
            nom = m.group(1)
            if nom in par_titre:
                raise Arret(f"titre répété : {nom}")
            par_titre[nom] = 0
        elif l.startswith(PREFIXE_AVANT):
            if nom is None:
                raise Arret(f"ligne {i + 1} : « avant » sans titre de correction")
            if i + 1 >= fin or not lignes[i + 1].startswith(PREFIXE_APRES):
                raise Arret(f"ligne {i + 1} : « avant » sans « après » sur la ligne suivante ({nom})")
            couples.append((nom, i + 1, l[len(PREFIXE_AVANT):], lignes[i + 1][len(PREFIXE_APRES):]))
            par_titre[nom] += 1
            i += 1
        elif l.startswith(PREFIXE_APRES):
            raise Arret(f"ligne {i + 1} : « après » sans « avant » ({nom})")
        i += 1
    ecarts = {n: k for n, k in par_titre.items() if k != 1}
    if ecarts:
        raise Arret(f"titres de correction sans exactement un couple : {ecarts}")
    return couples


def occurrences(texte, motif):
    """Nombre de positions où commence le motif, chevauchements compris."""
    n, i = 0, texte.find(motif)
    while i != -1:
        n += 1
        i = texte.find(motif, i + 1)
    return n


def appliquer(texte, couples, journal=dire):
    for k, (nom, ligne_cl, avant, apres) in enumerate(couples, 1):
        n = occurrences(texte, avant) if avant else 0
        if n != 1:
            journal(f"{k:02d} {nom} (contre-lecture, l. {ligne_cl}) : ÉCHEC — « avant » trouvé {n} fois "
                    f"au moment de l'appliquer ; arrêt net, à trancher par le contre-lecteur")
            journal(f"   avant : {avant}")
            raise Arret(f"couple {k} ({nom}) non appliqué")
        pos = texte.find(avant)
        ligne_note = texte.count("\n", 0, pos) + 1
        texte = texte[:pos] + apres + texte[pos + len(avant):]
        journal(f"{k:02d} {nom} (contre-lecture, l. {ligne_cl}) : appliqué à la ligne {ligne_note} "
                f"de la note ; « avant » {len(avant)} car., « après » {len(apres)} car.")
    return texte


def refuser_si_existe(chemin):
    if chemin.exists():
        raise Arret(f"{chemin} existe déjà : la règle R12 interdit d'écraser")


def eprouver_gardes():
    """Règle R5 : la garde d'arrêt sur un cas sain et sur cinq artefacts ; la garde R12 sur deux cas."""
    sain = appliquer("un deux trois", [("sain", 0, "deux", "2")], muet) == "un 2 trois"
    artefacts = {"« avant » absent": [("absent", 0, "quatre", "4")],
                 "« avant » double": [("double", 0, "a", "b")],
                 "« avant » chevauchant": [("chevauchant", 0, "aa", "b")],
                 "« avant » vide": [("vide", 0, "", "x")],
                 "second couple gêné par le premier": [("premier", 0, "un", "deux"), ("second", 0, "un", "1")]}
    textes = {"« avant » absent": "un deux", "« avant » double": "a et a",
              "« avant » chevauchant": "aaa", "« avant » vide": "un",
              "second couple gêné par le premier": "un trois"}
    arrets = 0
    for cle, liste in artefacts.items():
        try:
            appliquer(textes[cle], liste, muet)
        except Arret:
            arrets += 1
    r12 = False
    try:
        refuser_si_existe(NOTE_V1)
    except Arret:
        r12 = True
    try:
        refuser_si_existe(DOSSIER / "fichier-qui-n-existe-pas-v0.md")
    except Arret:
        r12 = False
    if not (sain and arrets == len(artefacts) and r12):
        raise Arret("une garde d'arrêt ne se comporte pas comme attendu")
    dire(f"gardes éprouvées : cas sain appliqué ; {arrets} artefacts sur {len(artefacts)} arrêtés "
         f"({', '.join(artefacts)}) ; écrasement d'un fichier existant refusé, chemin libre accepté")


def serialiser(reg, avant_blanc):
    """Mise en page du registre du rédacteur : une source et une citation par ligne,
    une ligne vide avant chaque citation dont l'identifiant est dans `avant_blanc`."""
    lignes = ["{", ' "sources": {']
    src = list(reg["sources"].items())
    for i, (k, v) in enumerate(src):
        lignes.append(f"  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}"
                      + ("," if i < len(src) - 1 else ""))
    lignes += [" },", ' "citations": [']
    cit = reg["citations"]
    for i, c in enumerate(cit):
        if c["id"] in avant_blanc:
            lignes.append("")
        lignes.append("  " + json.dumps(c, ensure_ascii=False) + ("," if i < len(cit) - 1 else ""))
    lignes += [" ]", "}"]
    return "\n".join(lignes) + "\n"


def blancs_du_registre(texte):
    """Identifiants des citations précédées d'une ligne vide dans le registre v1."""
    lignes = texte.split("\n")
    ids = []
    for i, l in enumerate(lignes[:-1]):
        if l == "":
            m = re.match(r'  \{"id": "([PACXN]\d{2})"', lignes[i + 1])
            if not m:
                raise Arret(f"registre v1 : ligne vide inattendue à la ligne {i + 1}")
            ids.append(m.group(1))
    return ids


def registre_v2(octets_v1, octets_contre):
    texte_v1 = texte_brut(octets_v1, REG_V1.name)
    v1 = json.loads(texte_v1)
    contre = json.loads(texte_brut(octets_contre, REG_CONTRE.name))
    if list(v1) != ["sources", "citations"]:
        raise Arret(f"registre v1 : clés {list(v1)} inattendues")
    avant_blanc = blancs_du_registre(texte_v1)
    if serialiser(v1, set(avant_blanc)) != texte_v1:
        raise Arret("la mise en page du registre v1 n'est pas reproduite octet pour octet")
    dire("forme du registre du rédacteur : la mise en page reproduit le registre v1 octet pour octet "
         f"(lignes vides avant {', '.join(avant_blanc)}, gardées aux mêmes places ; aucune ajoutée)")
    if contre["sources"] != v1["sources"]:
        raise Arret("les sources du registre de la contre-lecture diffèrent de celles du rédacteur")
    dire("sources du registre de la contre-lecture : identiques à celles du rédacteur")
    formes = {(c["src"], tuple(c)) for c in v1["citations"]}
    neufs = []
    for c in contre["citations"]:
        if c.get("a_verser") is True:
            d = {k: v for k, v in c.items() if k != "a_verser"}
            if (d["src"], tuple(d)) not in formes:
                raise Arret(f"{d['id']} : champs {tuple(d)} absents des formes du rédacteur")
            neufs.append(d)
        elif c.get("a_verser") is not False:
            raise Arret(f"{c.get('id')} : champ « a_verser » absent ou illisible")
    if len(neufs) != NB_A_VERSER:
        raise Arret(f"{len(neufs)} citations « a_verser » au lieu de {NB_A_VERSER}")
    ids_v1 = [c["id"] for c in v1["citations"]]
    ids_neufs = [d["id"] for d in neufs]
    if len(set(ids_v1)) != len(ids_v1) or len(set(ids_neufs)) != len(ids_neufs):
        raise Arret("identifiant répété dans un registre")
    if set(ids_v1) & set(ids_neufs):
        raise Arret(f"identifiants déjà au registre v1 : {sorted(set(ids_v1) & set(ids_neufs))}")
    lettres = []
    for cid in ids_v1:
        if not lettres or lettres[-1] != cid[0]:
            lettres.append(cid[0])
    if len(lettres) != len(set(lettres)) or any(i[0] not in lettres for i in ids_neufs):
        raise Arret("les lettres du registre v1 ne sont pas groupées, ou une lettre neuve apparaît")
    citations = []
    for lettre in lettres:
        anciennes = [c for c in v1["citations"] if c["id"][0] == lettre]
        ajoutees = [d for d in neufs if d["id"][0] == lettre]
        citations += anciennes + ajoutees
        dire(f"   {lettre} : {len(anciennes)} du registre v1, puis {len(ajoutees)} versées "
             f"({', '.join(d['id'] for d in ajoutees) or 'aucune'})")
    v2 = {"sources": v1["sources"], "citations": citations}
    texte_v2 = serialiser(v2, set(avant_blanc))
    if json.loads(texte_v2) != v2:
        raise Arret("registre v2 : relecture JSON non conforme")
    return texte_v2.encode("utf-8"), set(ids_v1), set(ids_neufs)


def programme_v2(octets_v1):
    texte = texte_brut(octets_v1, PROG_V1.name)
    neuf = texte
    for ancien, nouveau, attendu in NOMS_PROG:
        n = neuf.count(ancien)
        if n != attendu:
            raise Arret(f"programme v1 : « {ancien} » trouvé {n} fois au lieu de {attendu}")
        neuf = neuf.replace(ancien, nouveau)
    a, b = texte.split("\n"), neuf.split("\n")
    if len(a) != len(b):
        raise Arret("le nombre de lignes du programme a changé")
    changees = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
    nb_lignes = len(texte.splitlines())
    dire(f"programme v2 : {len(changees)} lignes changées sur {nb_lignes}, et seulement les noms des fichiers lus :")
    for i, x, y in changees:
        dire(f"   l. {i} : {x.strip()}")
        dire(f"      → {y.strip()}")
    return neuf.encode("utf-8")


def ecrire(chemin, octets):
    refuser_si_existe(chemin)
    chemin.write_bytes(octets)
    if sha(chemin.read_bytes()) != sha(octets):
        raise Arret(f"{chemin.name} : relu différent de ce qui a été écrit")
    dire(f"écrit {chemin.relative_to(DOSSIER)} : sha256 {sha(octets)} ({len(octets)} octets)")


def main(argv):
    ecrire_ok = "--ecrire" in argv
    sorties = [a.split("=", 1)[1] for a in argv if a.startswith("--sortie=")]
    autres = [a for a in argv if a != "--ecrire" and not a.startswith("--sortie=")]
    mode = "écriture" if ecrire_ok else "essai, rien n'est écrit"
    heure = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dire(f"Commande : python3 -I {sys.argv[0]} {' '.join(argv)}".rstrip())
    dire(f"Heure (UTC) : {heure} ; mode : {mode}")
    if autres:
        raise Arret(f"arguments inconnus : {autres}")
    if len(sorties) > 1:
        raise Arret("une seule option --sortie")
    if sorties:
        refuser_si_existe(Path(sorties[0]))
    dire()
    dire("== 0. Entrées et gardes")
    octets = {chemin: lire_scelle(chemin, prefixe) for chemin, prefixe in ENTREES}
    eprouver_gardes()
    dire()
    dire("== 1. Couples de la contre-lecture, appliqués à la lettre et dans l'ordre")
    note = texte_brut(octets[NOTE_V1], NOTE_V1.name)
    couples = lire_couples(texte_brut(octets[CONTRE_LECTURE], CONTRE_LECTURE.name))
    dire(f"couples lus au § 8 : {len(couples)} (attendus : {NB_COUPLES})")
    if len(couples) != NB_COUPLES:
        raise Arret("nombre de couples inattendu")
    corrige = appliquer(note, couples)
    dire(f"couples appliqués : {len(couples)} sur {len(couples)} ; aucun non appliqué")
    attendue = re.findall(r"empreinte du texte corrigé ([0-9a-f]{64})",
                          texte_brut(octets[SORTIE_CONTRE], SORTIE_CONTRE.name))
    obtenue = sha(corrige.encode("utf-8"))
    dire(f"empreinte du texte corrigé : {obtenue}")
    dire(f"celle de la sortie scellée du contre-lecteur : {attendue[0] if len(attendue) == 1 else 'introuvable'}")
    if attendue != [obtenue]:
        raise Arret("le texte corrigé diffère de celui du contre-lecteur")
    dire("contrôle croisé : égales")
    dire()
    dire("== 2. Registre v2 : registre v1 du rédacteur, plus les citations « a_verser »")
    reg_v2, ids_v1, ids_neufs = registre_v2(octets[REG_V1], octets[REG_CONTRE])
    dire(f"citations au registre v2 : {len(ids_v1)} + {len(ids_neufs)} = {len(ids_v1 | ids_neufs)}")
    cites = set(MOTIF_ID.findall(corrige.split(TITRE_TABLE)[0]))
    inconnus = sorted(cites - ids_v1 - ids_neufs)
    non_cites = sorted((ids_v1 | ids_neufs) - cites)
    dire(f"note corrigée, avant la table : {len(cites)} identifiants cités ; inconnus du registre v2 : "
         f"{inconnus or 'aucun'} ; au registre v2 mais non cités : {non_cites or 'aucun'}")
    dire()
    dire("== 3. Programme v2 : copie du programme v1 du rédacteur")
    prog_v2 = programme_v2(octets[PROG_V1])
    dire()
    dire("== 4. Écriture")
    if not ecrire_ok:
        dire("essai : rien n'est écrit")
        return 0
    for chemin in (NOTE_V2, REG_V2, PROG_V2):
        refuser_si_existe(chemin)
    ecrire(NOTE_V2, corrige.encode("utf-8"))
    ecrire(REG_V2, reg_v2)
    ecrire(PROG_V2, prog_v2)
    dire("la note v2 écrite ici précède l'en-tête et l'annexe, faits ensuite à l'outil d'édition ;"
         " son empreinte finale est celle de son compagnon")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        code = main(args)
    except Arret as e:
        dire(f"ARRÊT : {e}")
        code = 1
    dire(f"code de sortie : {code}")
    chemins = [a.split("=", 1)[1] for a in args if a.startswith("--sortie=")]
    if len(chemins) == 1 and not Path(chemins[0]).exists():
        Path(chemins[0]).write_bytes(("\n".join(JOURNAL) + "\n").encode("utf-8"))
    sys.exit(code)
