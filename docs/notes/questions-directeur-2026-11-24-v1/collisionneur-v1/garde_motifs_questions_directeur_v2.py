"""Garde de motifs sur les pièces neutres du collisionneur, dossier des questions du directeur du 24 novembre (v2 : question groupée v2 après le test de devinette v1 ; faits et question témoin v1 inchangés).

Pièce de travail (classe C). Aucun appel réseau, aucune écriture sur disque : le module du collisionneur est importé
sans fichier de code compilé (sys.dont_write_bytecode), et les invitations du troisième étage sont reconstruites en
mémoire par la fonction même du moteur (construire_prompt), dont la lecture scellée des fichiers est remplacée ici par
une lecture en mémoire. Les pièces des tours deux et trois, qui n'existent pas encore, entrent comme pièces absentes
(bloc du moteur).

Lancement : PYTHONDONTWRITEBYTECODE=1 python3 -I garde_motifs_questions_directeur_v2.py
"""
import hashlib
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[3]
sys.path.insert(0, str(DEPOT / "docs" / "notes" / "collisionneur-v9"))
sys.path.insert(0, str(DEPOT / "src"))
import collisionneur_v9_v8d as col  # noqa: E402

FAITS = ICI / "faits-neutres-questions-directeur-v1.md"
QUESTIONS = {
    "principal": ICI / "question-neutre-groupee-questions-directeur-v2.md",
    "temoin": ICI / "question-temoin-neutre-questions-directeur-v1.md",
}
ESPECES = ["opus", "carbon", "neon"]


def mesure(p):
    brut = p.read_bytes()
    txt = col.lire_entree(p)
    return {
        "octets": len(brut),
        "caracteres": len(txt),
        "mots": len(txt.split()),
        "sha256": hashlib.sha256(brut).hexdigest(),
        "motifs_octets": col.motifs_trouves(brut.decode("utf-8")),
        "motifs_lire_entree": col.motifs_trouves(txt),
    }


def invitations(question_p):
    """Rend {cellule: (longueur, motifs)} pour les neuf cellules du troisième étage, reconstruites en mémoire."""
    memoire = {"faits.md": col.lire_entree(FAITS), "question-etage3.md": col.lire_entree(question_p)}

    def lire_sceau_memoire(chemin):
        texte = memoire[Path(chemin).name]
        return texte, col.empreinte(texte)

    col.lire_sceau = lire_sceau_memoire
    col.cellule_valide = lambda dossier, cid: None
    col.statut_courant = lambda dossier, cid: "jamais lancée"
    col.fixer_composition(ESPECES, nom_cle_anthropic="CLE_FICTIVE")
    rendu = {}
    for tour in col.ORDRE_ETAGE[3]:
        for lettre in col.LETTRES:
            ids = col.entrees(tour, lettre, [])
            prompt, _ = col.construire_prompt(Path("dossier-en-memoire"), tour, lettre, [], set(ids))
            rendu[col.id_cellule(tour, lettre)] = (len(prompt), col.motifs_trouves(prompt))
    return rendu


def main():
    print(f"moteur : {col.VERSION}, empreinte {col.empreinte_fichier(col.__file__)}")
    print("=== 1. Pièces isolées ===")
    sain = True
    for p in [FAITS, *QUESTIONS.values()]:
        m = mesure(p)
        sain &= not m["motifs_octets"] and not m["motifs_lire_entree"]
        print(f"{p.name} : octets={m['octets']} caracteres={m['caracteres']} mots={m['mots']} sha256={m['sha256']} "
              f"motifs_octets={m['motifs_octets']} motifs_lire_entree={m['motifs_lire_entree']}")
    print("=== 2. Invitations assemblées du troisième étage (opus, carbon, neon) ===")
    for bras, qp in QUESTIONS.items():
        for cid, (n, motifs) in invitations(qp).items():
            sain &= not motifs
            print(f"{bras} {cid} : caracteres={n} motifs={motifs}")
    print("=== 3. Témoin positif de la garde (texte synthétique, doit déclencher) ===")
    temoin = "Voir docs/notes/exemple et l'accord GO-2026-01-01-01, ligne R-1234."
    t = col.motifs_trouves(temoin)
    print(f"témoin positif : {t}")
    garde_vivante = len(t) == 3
    print(f"VERDICT : pièces et invitations saines = {sain} ; garde vivante sur le témoin positif = {garde_vivante}")
    return 0 if (sain and garde_vivante) else 1


if __name__ == "__main__":
    sys.exit(main())
