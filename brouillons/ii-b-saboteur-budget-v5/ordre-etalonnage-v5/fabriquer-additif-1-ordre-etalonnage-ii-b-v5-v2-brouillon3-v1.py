"""Fabrique l'additif 1 à l'ordre v2 de l'étalonnage, brouillon 3, depuis le brouillon 2, par remplacements à ancre comptée.
Porte les deux précisions d'exécution du vérificateur (note-verification-additif-1-brouillon2-v1.md, « conforme ») :
p1 identité git pour git am et contrôle de propreté sans les fichiers non suivis ; p2 préalables de la sous-commande
surveillance, un code 2 dit aussitôt à la mère. Rien d'autre.
Usage : python3 fabriquer-additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3-v1.py (depuis ce dossier)."""
import hashlib, pathlib

ICI = pathlib.Path(__file__).resolve().parent
SOURCE = ICI / "additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon2.md"
CIBLE = ICI / "additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3.md"
t = SOURCE.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode("utf-8")).hexdigest().startswith("0fed5e44"), "brouillon 2 inattendu"
REMPLACEMENTS = [
    ("versement par lot dit selon le code (brouillon 2)", "versement par lot dit selon le code (brouillon 3)", 1),
    ("> **Brouillon 2, fabriqué par programme** depuis le brouillon 1",
     "> **Brouillon 3**, fabriqué par `fabriquer-additif-1-ordre-etalonnage-ii-b-v5-v2-brouillon3-v1.py` depuis le brouillon 2 "
     "(`0fed5e44a3c4f846559397a07fb3c16f632ce12a01d1897937c49dee058dce49`, vérifié « conforme » par un Opus 5.5) : il ne porte que "
     "les deux précisions d'exécution du vérificateur au § 3 (identité git et propreté du dépôt, étape 3 ; préalables de la "
     "relance, étape 5). **Brouillon 2, fabriqué par programme** depuis le brouillon 1", 1),
    ("et `git -C \"$DEPOT\" status --porcelain` vide) :",
     "et `git -C \"$DEPOT\" status --porcelain --untracked-files=no` vide : le dossier `$D` peut se trouver dans `$DEPOT`, ses "
     "fichiers non suivis ne comptent pas) ; `git am` exige une identité git, donnée sur la ligne de commande :", 1),
    ('   git -C "$DEPOT" am --keep-cr "$D/$P"',
     '   git -C "$DEPOT" -c user.name="executante iib v5" -c user.email=executante-iib@invalid am --keep-cr "$D/$P"', 1),
    ("   Consigner le numéro de processus. Vérifier dans",
     "   La sous-commande refuse (code 2) si `$D/lancement.txt` manque ou ne nomme pas cet identifiant, si le jeton GitHub ou, en "
     "mode réel, `HF_TOKEN` manque, ou si l'outil du loueur ne se résout pas : vérifier ces préalables avant l'étape 2. **Un "
     "code 2 à la relance laisse l'étalonnage sans surveillance** (la minuterie seule reste) : le dire aussitôt à la mère, "
     "avec la ligne de refus, et relancer dès la cause levée. Consigner le numéro de processus. Vérifier dans", 1),
]
for ancien, nouveau, n in REMPLACEMENTS:
    assert t.count(ancien) == n, (ancien[:70], t.count(ancien))
    t = t.replace(ancien, nouveau)
CIBLE.open("x", encoding="utf-8").write(t)
print(CIBLE.name, hashlib.sha256(t.encode("utf-8")).hexdigest())
