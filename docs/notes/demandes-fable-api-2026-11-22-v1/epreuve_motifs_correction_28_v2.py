"""Épreuve des motifs de l'article 4 (correction 28 de la relecture de Fable 0cec14ce…), version 2 :
règle de repérage des duels remplacée par celle de la correction 43 (relecture de Fable 44b7d86e…), casse respectée pour A et B.

Dix textes synthétiques, écrits par Opus 5.5 d'après les seules consignes des tours III.1 et III.3 et le préambule
(règle B4 : duel H_A contre H_B) de docs/notes/collisionneur-v9/collisionneur_v9_v8d.py, sans lecture d'aucune
cellule ni d'aucune réponse de modèle. Le nombre de duels attendu est fixé dans le texte, avant toute exécution.
Les textes 3, 4, 5 et 10 nomment H_A (ou H₁) plusieurs fois dans un même duel.
Motifs appliqués tels qu'écrits à l'article 4 de pieces-comparaison-essaim-v4.md ; code des duels copié de la correction 43.
Textes et nombres attendus inchangés depuis la version 1.
Passe si les dix textes rendent le nombre attendu ; échoue sinon (code de sortie 1).
"""
import re
import sys

MOTIF_B = re.compile(r"^\s*(#+\s*)?[\*\(]*\s*\(?b[\)\.]", re.IGNORECASE)   # « casse ignorée »
MOTIF_C = re.compile(r"^\s*(#+\s*)?[\*\(]*\s*\(?c[\)\.]", re.IGNORECASE)   # « le même motif pour (c) »
HA = r"\bH_?A\b|\bH₁"
HB = r"\bH_?B\b|\bH₂"
MOTIF_A = re.compile(HA)                                  # casse respectée
MOTIF_A_OU_B = re.compile(f"{HA}|{HB}")
MOTIF_OPPOSITION = re.compile(f"(?:{HA}).*(?:{HB})")


def ouvertures_duels(section):
    premiere = [MOTIF_A_OU_B.search(l) for l in section]   # première occurrence de A ou de B, par ligne
    ouvertures, opposition_vue = [], False
    for k, ligne in enumerate(section):
        if MOTIF_OPPOSITION.search(ligne):
            ouvertures.append(k)
            opposition_vue = True
        elif not opposition_vue and MOTIF_A.search(ligne):
            suivante = next((m for m in premiere[k + 1:] if m), None)
            if suivante and suivante.group().endswith(("B", "₂")):
                ouvertures.append(k)
    return ouvertures


def duels(texte):
    lignes = texte.split("\n")
    debut = next((i for i, l in enumerate(lignes) if MOTIF_B.search(l)), None)
    if debut is None:
        return None, []
    fin = next((j for j in range(debut + 1, len(lignes)) if MOTIF_C.search(lignes[j])), len(lignes))
    section = lignes[debut:fin]
    ouvertures = ouvertures_duels(section)
    return (debut, fin), [section[k] for k in ouvertures]


TEXTES = [
    # 1 — tour III.1, un duel par ligne, H_A une fois par duel.
    (2, """## (a) Ce que la question suppose
- Le moniteur voit tout l'épisode [HYPOTHÈSE].

## (b) Expériences décisives
1. Expérience 1. H_A : la sonde détecte le sabotage diffus ; contre H_B : elle ne détecte que le sabotage concentré. Métrique : taux de détection à 1 % de fausses alertes. Seuil : 0,5. Contrôle négatif : épisodes honnêtes appariés. Issue qui falsifie : un taux sous 0,5.
2. Expérience 2. H_A : le score croît avec la longueur de l'épisode ; contre H_B : il est constant. Métrique : pente. Seuil : zéro hors de l'intervalle. Contrôle négatif : longueur permutée.

## (c) Mesure minimale par instrument
- Sonde : taux de détection et de fausses alertes sur cas honnêtes appariés.

## (d) Ancrage matériel
- Modèle ouvert de 8 milliards de paramètres, coût illustratif.
FIN"""),
    # 2 — tour III.1, titres de duel sans H_A, une ligne H_A par duel.
    (3, """### (b) Expériences décisives
#### Duel 1
- H_A : le juge est trompé par la persuasion.
- H_B : le juge n'est pas trompé.
- Métrique : écart de verdict ; seuil 0,1 ; contrôle négatif : texte neutre.
#### Duel 2
- H_A : l'effet tient à dix agents.
- H_B : il disparaît.
- Métrique : taux ; seuil 0,2.
#### Duel 3
- H_A : la corrélation des scores dépasse 0,5.
- H_B : elle reste sous 0,5.
- Contrôle négatif : copies de graines distinctes.
### (c) Mesure minimale
- Taux de fausses alertes sur cas honnêtes appariés.
FIN"""),
    # 3 — tour III.1, plusieurs H_A dans un même duel (titre, hypothèse, issue).
    (2, """## (b) Expériences décisives

**Expérience 1 : H_A contre H_B**
- H_A : le saboteur réparti échappe au moniteur de transcription.
- H_B : il est détecté au même taux que le saboteur concentré.
- Métrique : taux de détection ; seuil : écart de 0,1.
- Issue : un écart inférieur à 0,1 falsifie H_A.

**Expérience 2 : H_A contre H_B**
- H_A : la sonde ajoute du signal au moniteur de texte.
- H_B : elle n'en ajoute pas.
- Contrôle négatif : sonde sur couche aléatoire ; sous H_A, l'aire reste à 0,5.

## (c) Mesure minimale
- Détection et fausses alertes sur cas honnêtes appariés.
FIN"""),
    # 4 — tour III.3, expériences corrigées, plusieurs H_A par duel.
    (2, """## (a) Réponse aux critiques
- Critique de B sur la fuite entre construction et évaluation : acceptée.
- Critique de C sur la puissance : transformée en test.

## (b) Expériences corrigées
### Duel 1 (corrigé) — H_A contre H_B
H_A : le moniteur garde sa puissance sous paraphrase.
H_B : il la perd.
Correction : banque d'évaluation séparée ; sous H_A, le taux reste au-dessus de 0,6.
### Duel 2 (corrigé) — H_A contre H_B
H_A : la règle d'audit au hasard borne le dommage.
H_B : elle ne le borne pas.

## (c) Réponse à la question de l'arbitre
Ce qui est établi : peu. L'expérience à faire en premier : le duel 1.
FIN"""),
    # 5 — notation H₁ contre H₂, plusieurs H₁ par duel.
    (2, """**(b) Expériences décisives**
- Expérience 1 : H₁ contre H₂.
  - H₁ : le score de la sonde monte avec la dose de sabotage.
  - H₂ : il ne bouge pas.
  - Issue qui falsifie H₁ : pente nulle.
- Expérience 2 : H₁ contre H₂.
  - H₁ : deux copies voient leurs scores monter ensemble.
  - H₂ : non.
**(c) Mesure minimale**
- Fausses alertes sur cas honnêtes.
FIN"""),
    # 6 — section (b) sans section (c) : fin à la fin de la cellule.
    (1, """## (a) Suppositions
- Le budget d'audit est fixe [HYPOTHÈSE].

## (b) Expérience décisive
- Duel unique. H_A : l'audit à 2 % suffit ; H_B : il ne suffit pas. Métrique : dommage non détecté. Seuil : 1 %.
- Contrôle négatif : épisodes honnêtes.
FIN"""),
    # 7 — titres en gras ; H_A mentionnée dans la section (c), à ne pas compter.
    (2, """**(a) Suppositions**
- Les agents ne communiquent pas hors du canal [HYPOTHÈSE].

**(b) Expériences décisives**
- Duel 1. H_A : la collusion élève les scores ensemble ; H_B : les scores restent indépendants.
- Duel 2. H_A : le juge d'une autre lignée résiste ; H_B : il cède comme les autres.

**(c) Mesure minimale**
- Pour la sonde du duel 1 sous H_A : détection et fausses alertes sur cas honnêtes appariés.

**(d) Ancrage matériel**
- Coût illustratif.
FIN"""),
    # 8 — titre « b) » nu ; notation HA sans tiret bas.
    (2, """a) Suppositions
- La question suppose un moniteur fixe.

b) Expériences décisives
- Duel 1 : HA, le moniteur est contourné par paraphrase ; HB, il ne l'est pas. Seuil : 0,1.
- Duel 2 : HA, la détection baisse avec la longueur ; HB, elle reste stable.

c) Mesure minimale
- Taux de fausses alertes.
FIN"""),
    # 9 — H_A mentionnée en section (a), à ne pas compter ; trois duels, H_A une fois chacun.
    (3, """## (a) Suppositions
- La question suppose que H_A et H_B épuisent les cas [HYPOTHÈSE].

## (b) Expériences décisives
1. H_A : le signal est dans les activations ; H_B : il est dans le texte seul. Seuil : 0,05.
2. H_A : le signal survit au changement de famille ; H_B : non.
3. H_A : l'effet croît avec la dose ; H_B : il est plat.

## (c) Mesure minimale
- Détection et fausses alertes.
FIN"""),
    # 10 — duel décrit sur plusieurs lignes, H_A sur la première et sur la troisième.
    (2, """## (b) Expériences décisives
Expérience 1. On oppose H_A, selon laquelle le saboteur informé contourne la sonde,
à H_B, selon laquelle il ne la contourne pas. La métrique est le taux de détection à 1 % de fausses alertes,
et l'issue qui falsifie H_A est un taux supérieur à 0,5 sous attaque informée.

Expérience 2. On oppose H_A, selon laquelle l'audit au hasard borne le dommage,
à H_B, selon laquelle il ne le borne pas ; un dommage planté non vu falsifie H_A.

## (c) Mesure minimale
- Taux de détection.
FIN"""),
]

PLUSIEURS_H_A = {3, 4, 5, 10}


def main():
    assert len(TEXTES) == 10
    assert len(PLUSIEURS_H_A) >= 3
    echecs = 0
    for n, (attendu, texte) in enumerate(TEXTES, start=1):
        bornes, ouv = duels(texte)
        obtenu = len(ouv)
        ok = obtenu == attendu
        echecs += not ok
        marque = " [plusieurs H_A par duel]" if n in PLUSIEURS_H_A else ""
        print(f"texte {n:2d}{marque} : attendu {attendu}, obtenu {obtenu}, section (b) lignes {bornes} : "
              f"{'PASSE' if ok else 'ÉCHOUE'}")
        if not ok:
            for l in ouv:
                print(f"    ouverture : {l.strip()[:90]}")
    print(f"RÉSULTAT : {'PASSE' if echecs == 0 else 'ÉCHOUE'} ({10 - echecs}/10 textes au nombre attendu)")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
