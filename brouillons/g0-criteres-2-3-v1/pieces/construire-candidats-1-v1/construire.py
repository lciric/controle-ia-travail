"""Construit les candidats 1 (préenregistrement, désignation, devis) à partir des brouillons 4 scellés par compagnon :
la vérification 3 est citée (constat V3-01), l'article cité entre à l'en-tête de la désignation (V3-02), l'avis du
contre-lecteur après le retrait est rapporté ; rien d'autre ne change. Usage : python3 construire.py DOSSIER"""
import hashlib, sys
D = sys.argv[1].rstrip("/") + "/"
P, G, V = "T0.6-organisme-consigne-cachee-dose-reponse-v1", "G0-critere-3-designation-course-v1", "devis-dose-reponse-consigne-cachee-v1"
sha = lambda c: hashlib.sha256(open(c, "rb").read()).hexdigest()
journal = []
def un(t, a, n, idc, piece):
    k = t.count(a)
    if k != 1:
        raise SystemExit(f"{idc} : {k} occurrence(s) dans {piece}")
    journal.append(f"{piece}\t{idc}\tappliqué")
    return t.replace(a, n)
H_V3 = sha(D + "verification-3-des-brouillons-4-v1.md")
SUITE = "- **Vérification 3**, courte, du seul écart entre le brouillon 3 et ce brouillon 4, par le même contre-lecteur : demandée ; son rapport est cité au candidat."
def cite(h_b4, verdict, suite):
    return (f"- **Vérification 3**, courte, du seul écart entre le brouillon 3 et le brouillon 4 (`{h_b4}`), par le même contre-lecteur : rapport `brouillons/g0-criteres-2-3-v1/verification-3-des-brouillons-4-v1.md`, `{H_V3}`. États de V2-01 à V2-07 : quatre corrigés, trois corrigés autrement de façon acceptable (V2-02, V2-04, V2-06) ; les citations de l'article et la description des témoins du premier test sont vérifiées sur leurs pages. Constats neufs : aucun bloquant, aucun majeur, deux mineurs. Verdict sur ce texte : « {verdict} ». {suite} Ce candidat ne diffère du brouillon 4 que par ces citations (`pieces/construire-candidats-1-v1/`) : il n'appelle pas de vérification de plus.")
for piece in (P, G, V):
    t = open(D + piece + "-brouillon4.md", encoding="utf-8").read()
    h = sha(D + piece + "-brouillon4.md")
    t = un(t, "— v1 — brouillon 4", "— v1 — candidat 1", "EN-1", piece)
    if piece != V:
        t = un(t, "- Statut : **brouillon 4, non scellé** :", f"- Statut : **candidat 1 au scellement, non scellé** : le brouillon 4 (`{h}`) où la vérification 3 est citée ; auparavant :", "EN-2", piece)
    if piece == P:
        t = un(t, "devis d'une page `devis-dose-reponse-consigne-cachee-v1-brouillon4.md`.", "devis d'une page `devis-dose-reponse-consigne-cachee-v1-candidat1.md`.", "EN-3", piece)
        t = un(t, "ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-brouillon4.md`", "ligne de dépense : `devis-dose-reponse-consigne-cachee-v1-candidat1.md`", "EN-4", piece)
        t = un(t, SUITE, cite(h, "prête à sceller sous les corrections mineures listées", "Traitement : V3-01 (pas de garde pour la vérification 3) : la vérification 3 est citée ici même."), "V3-01", piece)
    if piece == G:
        t = un(t, "v1-brouillon4.md` au jour de ce brouillon ;", "v1-candidat1.md` au jour de ce candidat ;", "EN-3", piece)
        t = un(t, "<<EMPREINTE_PREREG_DOSE_REPONSE_SCELLE>>.", "<<EMPREINTE_PREREG_DOSE_REPONSE_SCELLE>> ;\n  - littérature citée à la raison 3 de la section 1 : `docs/sources/pdf/2611.14950v1.pdf` (`6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6`), p. 7 et 8, lues par l'auteur sur le PDF (R7).", "V3-02", piece)
        t = un(t, "en faire une condition si ce lancement tombait, la laisser rapportée sinon.", "en faire une condition si ce lancement tombait, la laisser rapportée sinon ; après le retrait (vérification 3), son avis pèse pour en faire une condition.", "AVIS", piece)
        t = un(t, SUITE, cite(h, "prête à sceller sous les corrections mineures listées", "Traitement : V3-01 : la vérification 3 est citée ici même ; V3-02 : l'article entre à l'en-tête."), "V3-01", piece)
    if piece == V:
        t = un(t, "jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md`.", f"jointe au préenregistrement `T0.6-organisme-consigne-cachee-dose-reponse-v1-candidat1.md`. Candidat 1 : le brouillon 4 (`{h}`), que la vérification 3 dit prêt à sceller, sans autre changement.", "EN-2", piece)
    open(D + piece + "-candidat1.md", "w", encoding="utf-8").write(t)
open("journal-construction.txt", "w", encoding="utf-8").write("\n".join(journal) + "\n")
print(len(journal), "opérations")
