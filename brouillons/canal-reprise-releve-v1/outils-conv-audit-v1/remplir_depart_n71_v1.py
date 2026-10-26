"""Remplit le brouillon v5 du message de départ du pilote 4 et écrit le message n° 71 ; copie la ligne de GO (empreinte du
texte remplie) et les trois formes de lignes de dépense mot pour mot depuis le texte ; refuse s'il reste un ⟦…⟧.
Usage : python -I remplir_depart_n71_v1.py BROUILLON TEXTE SORTIE HEURE TETE"""
import hashlib, pathlib, re, sys

brouillon, texte_p, sortie, heure, tete = (pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]),
                                         sys.argv[4], sys.argv[5])
if sortie.exists():
    sys.exit(f"refus : {sortie} existe déjà (R12)")
b = brouillon.read_text(encoding="utf-8")
t = texte_p.read_text(encoding="utf-8")
sha_t = hashlib.sha256(texte_p.read_bytes()).hexdigest()
assert sha_t == "782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95", sha_t
e = re.findall(r"entropie E = ([0-9]+)", t); assert len(e) == 1
g53 = re.findall(r"graine de la course v5-3 = ([0-9]+)", t); g62 = re.findall(r"graine de la course v6-2 = ([0-9]+)", t)
assert len(g53) == 1 and len(g62) == 1
go = re.findall(r"`(\| GO-2026-10-25-02 \| 2026-10-25 \| calcul \| extension : pilote 4 [^`]*)`", t); assert len(go) == 1
ligne_go = go[0].replace("<empreinte du texte scellé>", sha_t); assert sha_t in ligne_go and "<" not in ligne_go
d62 = re.findall(r"`(\| <date du jour> \| pilote4-gemini-v6-2-v1 [^`]*)`", t); assert len(d62) == 1
d53 = re.findall(r"`(\| <date du jour> \| pilote4-gemini-v5-3-v1 [^`]*)`", t); assert len(d53) == 1
dseg = re.findall(r"`(\| <date du jour> \| <nom de la course> segment K [^`]*)`", t); assert len(dseg) == 1

def rempl(s, a, n, compte=1):
    assert s.count(a) == compte, (a[:70], s.count(a))
    return s.replace(a, n)

# lignes de dépense : mot pour mot depuis le texte (le brouillon en paraphrasait deux)
b = rempl(b, "`| <date du jour> | pilote4-gemini-v6-2-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 |`",
          "`" + d62[0] + "`")
b = rempl(b, "`| <date du jour> | <nom de la course> segment K+1 | GO-2026-10-25-02 | au plus 75 USD moins la dépense déjà faite | après le segment K |`,",
          "`" + dseg[0] + "` (forme du texte, mot pour mot ; pour le segment K+1, écris K+1 à la place de K et K à la place de K−1),")
b = rempl(b, "`| <date du jour> | pilote4-gemini-v5-3-v1 | GO-2026-10-25-02 | 75 USD au pire cas | empreintes de M 5ae4e801423bbef0 ; empreintes de la v6.2 <16 premiers caractères du .sha256 de EMPREINTES-pilote-v1.txt de la v6.2> |`,",
          "`" + d53[0] + "` (forme du texte, mot pour mot ; « <16 premiers caractères> » : ceux du compagnon `.sha256` de\n   `EMPREINTES-pilote-v1.txt` de la v6.2),")

b = rempl(b, "et poussé sur `outils/pilote4-gemini-travail` **avant la fin de la v6.2.1**",
          "et poussé sur ce canal (`envois/lecture-pilote4-v1/`, jamais sur la branche du lancement pendant les courses)\n"
          "   **avant la fin de la v6.2.1**")
b = rempl(b, "(recalculées à part depuis\n  l'entropie : égales ; les contrôles du lanceur sur le texte, rejoués : justes)",
          "(recalculées à part depuis\n  l'entropie : égales ; les contrôles du lanceur sur le texte, la ligne de GO, les lignes de dépense et les chemins,\n"
          "  rejoués par `envois/verification-depart-pilote4-v1/verifier_depart_pilote4_v1.sh`, essayé avant sur un cas sain et\n"
          "  un artefact, journal `depart-v1/verification-depart-v1.log` : tout juste)")
b = rempl(b, "C'est un texte différentiel sur P4v3 (`de7a5559…`, jamais lancé, gardé).",
          "C'est un texte différentiel sur P4v3 (`de7a5559…`, jamais lancé, gardé). Une répétition du script des graines a\n"
          "  tourné une fois, avant, sur une copie jetable (essai de l'outil de vérification) : ses graines ont été masquées et\n"
          "  détruites sans servir (`pieces-pilote4-gemini/traitement-cl7-v1/LISEZMOI-traitement-cl7-v1.md`).")

valeurs = {
    "⟦NUMERO⟧": "71", "⟦DATE⟧": "26 octobre 2026", "⟦HEURE_LUE⟧": heure, "⟦TETE⟧": tete, "⟦TETE_COURTE⟧": tete[:7],
    "⟦SHA_TEXTE⟧": sha_t, "⟦ENTROPIE⟧": e[0], "⟦GRAINE_V62⟧": g62[0], "⟦GRAINE_V53⟧": g53[0],
    "⟦SHA_EMPREINTES⟧": "dbc5928d1645ebaa53cc3a3d35f87bc8f813c473b93de27cceb08f154567d9f3", "⟦N_EMPREINTES⟧": "680",
    "⟦SHA_CL5⟧": "914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240",
    "⟦VERDICT_CL5⟧": "scellable après corrections mineures", "⟦CORRECTIONS_CL5⟧": "constats traités dans le texte",
    "⟦SHA_LU_CL6⟧": "51752266…", "⟦SHA_CL6⟧": "35fe0067ec7477c2e6e82500321bbe23a0683e20f2bbb6de36c55d4103dc7559",
    "⟦VERDICT_CL6⟧": "scellable après corrections mineures", "⟦CORRECTIONS_CL6⟧": "constats traités (`traitement-cl6-v1/`)",
    "⟦SHA_LU_CL7⟧": "4c20ca31…", "⟦SHA_CL7⟧": "68daac567230edcdeded204e55243a92b3046f8fee2c135af7063ba36a461725",
    "⟦VERDICT_CL7⟧": "scellable après corrections mineures",
    "⟦CORRECTIONS_CL7⟧": "constats traités (`traitement-cl7-v1/` ; dont P4C7-01 : à ces tailles, le verdict « au-dessus de la "
                         "référence » est impossible même à un score parfait, seul le test génération 0 contre génération 3 "
                         "peut séparer un changement du bruit des tâches)",
    "⟦LIGNE_GO⟧": ligne_go, "⟦SHA16⟧": sha_t[:16],
}
for k, v in valeurs.items():
    assert k in b, k
    b = b.replace(k, v)
reste = re.findall(r"⟦[^⟧]*⟧", b)
if reste:
    sys.exit(f"refus : marqueurs restants {sorted(set(reste))}")
# contrôle : chaque ligne de dépense et la ligne de GO figurent mot pour mot dans le message
for l in (ligne_go, d62[0], d53[0], dseg[0]):
    assert ("`" + l + "`") in b, l[:60]
sortie.write_text(b, encoding="utf-8")
h = hashlib.sha256(sortie.read_bytes()).hexdigest()
pathlib.Path(str(sortie) + ".sha256").write_text(f"{h}  {sortie.name}\n", encoding="utf-8")
print(f"message écrit : {sortie.name} {h}")
