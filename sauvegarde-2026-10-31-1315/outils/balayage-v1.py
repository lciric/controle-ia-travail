import re, sys, hashlib
F = sys.argv[1]
MARQUE = "[retiré, règle 2 : recommandation ou confiance d'auteur]"
L = open(F, encoding="utf-8").read().split("\n")
P, p = [], "tête"
for l in L:
    m = re.match(r"### Pièce (\S+)", l)
    if m: p = m.group(1)
    P.append(p)
def chercher(nom, motif, flags=0):
    r = re.compile(motif, flags)
    hits = [(i + 1, P[i], l) for i, l in enumerate(L) if r.search(l.replace(MARQUE, ""))]
    print(f"\n== {nom} — motif {motif!r} : {len(hits)} ligne(s)")
    for i, q, l in hits[:40]:
        print(f"  l. {i} [pièce {q}] {l[:180]}")
print(f"Balayage de {F} (règle 4 de faits-a-assembler-noeuds-v4.md), session-depot, 31 octobre 2026.")
print(f"Lignes : {len(L)} ; mots : {sum(len(l.split()) for l in L)} ; marques de retrait (règle 2) : {sum(l.count(MARQUE) for l in L)}.")
chercher("chemins donnees/", r"donnees/")
chercher("clés et jetons", r"sk-[A-Za-z0-9_-]{8,}|AIza[0-9A-Za-z_-]{10,}|Bearer\s+[A-Za-z0-9._-]{8,}|API_KEY=\S|_KEY=[A-Za-z0-9]{8,}|ghp_[A-Za-z0-9]{10,}|xox[bp]-")
chercher("mémo des décisions en attente (règle 1)", r"decisions-en-attente-lazar")
chercher("contenu d'attaque (mots repères)", r"jailbreak|suffixe adverse|évasion|contourn|BA-002|mode tenu à l.écart|bras d.attaque|camoufl", re.I)
chercher("texte de fiche réelle (repères)", r"^\s*>\s*\*\*(Titre|Hypothèse|Idée)|«\s*Fiche\s+[A-Z0-9]|texte de (la )?fiche", re.I)
chercher("recommandation, confiance ou défaut restants (hors marques de retrait)", r"recommand|confiances?\s*(?:d.environ\s*)?[0-9]|par défaut", re.I)
print("""
Lecture humaine des occurrences (session-depot) :
- donnees/ : en-têtes et table d'empreintes des pièces SD-1 et SD-2 (états des runs des questions 6 et 7, servis comme pièces de session-depot, sans aucune réponse de cellule) ; mentions de chemin sans contenu (« rien lu sous donnees/ », nom du dossier de la moisson OpenAlex dans l'état des lieux de Gu-Krenn).
- clés : aucune.
- mémo : absent.
- attaque : la ligne de la pièce SD-4 est la liste de termes du vocabulaire du contrôle dont l'état des lieux de Gu-Krenn mesure la couverture (aucun contenu) ; sinon mentions de procédure seulement (aiguilleur, garde de niveau méthode, essai du bras d'attaque « décrit par classe seulement », R-888 levée de R-611) ; aucun paramètre, aucune recette, aucun contenu du bras d'attaque ni du mode tenu à l'écart.
- fiches réelles : aucun texte de fiche ; seules des fiches synthétiques ou des comptes sont cités.
- recommandations restantes : en-tête (énoncé de la règle 2) et lignes de métadonnées des pièces 6 et 13 (note « règle 2 étendue ») ; pièce 3 (préenregistrement de la bisociation v2 : valeurs déjà gelées par Lazar, R-580, « égale à la recommandation » ; forme F-A marquée « recommandée » dans un texte scellé) ; pièces 1 et 2 (phrases « n'est pas une recommandation », « aucune recommandation de seuil assoupli »). La règle 2 ne s'y applique pas : textes scellés ou occurrences sans recommandation. Les pièces 6, 12 et 13 ont reçu la règle 2 en plus de la liste (configuration recommandée, confiance d'auteur, option recommandée).""")
print(f"\nEmpreinte du fichier balayé : {hashlib.sha256(open(F,'rb').read()).hexdigest()}")
