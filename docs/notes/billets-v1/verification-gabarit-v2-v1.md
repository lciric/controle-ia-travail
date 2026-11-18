# Vérification courte de la version 2 du gabarit des billets et de son application pas à pas — v1

Écrite par le contre-lecteur de la version 1 (agent Opus 5.5 lancé par la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), repris pour cette vérification, le 2026-11-18T22:46:35Z (heure relevée par `date -u`). Je n'ai écrit ni le gabarit, ni l'application pas à pas, ni le fichier des différences. Je n'ai ouvert aucune copie de billet, aucun commentaire, aucune table de correspondance, ni le programme du rédacteur.

## Verdict

**Bon pour le billet.** Les deux versions 2 sont exactement les versions 1, plus mes 17 couples appliqués à l'octet, les deux changements commandés par la mère et les sept changements d'accompagnement déclarés (V-1 à V-7). Il n'y a aucun autre caractère changé, aucun statut, aucune consigne, aucun chiffre de l'analyse. Les deux calculs refaits à la main par le rédacteur sont justes. Il reste une remarque de forme non bloquante, que mes propres couples ont créée (section 5).

## 0. Pièces et empreintes

Empreintes recalculées par `sha256sum`, égales aux compagnons `.sha256` :

| Pièce | Empreinte |
|---|---|
| `docs/notes/billets-v1/gabarit-billets-v2.md` | `5eee79b3cf051fbecc5a278bfbf6e54f2a6d9164326ec2512b88e3390b46a2a5` |
| `docs/notes/billets-v1/application-regle-gabarit-v2.md` | `e61d1af87070fd4f0bf78157286c6bc8f2c2bf7362740031e9687db9d81249db` |
| `docs/notes/billets-v1/differences-gabarit-v1-vers-v2.md` | `569308ac3fc1beed860a641a6b5479278a8698468cc974395e44c90d7f0b6c5a` |
| `docs/notes/billets-v1/gabarit-billets-v1.md` (inchangée) | `97185452dec7ea4f4f1a024b8dbb52f59f836ff09656bd23cd8d6735d9f91313` |
| `docs/notes/billets-v1/application-regle-gabarit-v1.md` (inchangée) | `573c156411eaabbfbaeb231552193470ead17b4e829d035fe3d4aa3bc4340cc9` |
| `docs/notes/billets-v1/contre-lecture-gabarit-v1.md` (source des couples) | `e125c2a7bb51b1ad94aa4a4f2da3802a76f6a25552cf52fda8343591de79c6c2` |
| `docs/notes/billets-v1/analyse-tenue-v1/analyse-tenue-v1.json` | `e29c0613127feee9e26d72d664d9d21b76c9602a0bd44619eeef944d0f1c2a5e` |

## 1. Chacun de mes couples est-il appliqué à l'octet ?

**Oui, les 17.** Méthode (programme en annexe) : mes couples sont lus dans **mon** rapport scellé, section 7, et non dans le fichier des différences. Le programme les applique aux versions 1 en exigeant une seule occurrence de chaque ancienne chaîne. Il ajoute ensuite les neuf autres changements lus dans le fichier des différences, puis compare le résultat aux versions 2 fichier par fichier, octet par octet.

- Les textes « ancien » et « nouveau » des 17 couples sont identiques entre mon rapport et le fichier des différences.
- Le gabarit reconstruit est identique à `gabarit-billets-v2.md` ; l'application reconstruite est identique à `application-regle-gabarit-v2.md`.

## 2. Rien d'autre ne change que les deux changements commandés et V-1 à V-7

**Oui.** La reconstruction n'utilise que les 17 couples, les deux changements commandés et les sept d'accompagnement : tout autre caractère changé l'aurait fait échouer. Contenu des neuf changements :

- **Écart du modèle du réviseur, désormais déclaré** (M-1, sur le texte neuf du couple G-11) : « non déclaré au registre » devient « déclaré depuis au registre (ligne R-3496 de `registres/decisions.md`) ». C'est exact : la ligne R-3496 déclare l'écart (recodage par Opus 5.5, le modèle du réviseur, contre la procédure).
- **Puissance dans la phrase du résultat principal, en tête** (M-2) : le texte ajouté reprend la correction écrite à la ligne R-3496 (« seuls de très grands écarts pouvaient passer la règle (au moins 10 paires dans un sens et aucune dans l'autre, ou équivalent) : l'étude ne dit pas que la forme n'a pas d'effet »). C'est juste pour 17 comparaisons comme pour 23 : 10 paires contre 0 passent, 9 contre 0 ne passent pas (section 4).
- **V-1 à V-7** : titres « — v2 », en-têtes de version (date, auteur, renvoi aux versions 1 et à leurs empreintes, à la contre-lecture et à son empreinte, au fichier des différences), renvoi du gabarit à l'application v2, état de la contre-lecture. Toutes les empreintes citées sont justes. La phrase « 1 112 contrôles par programme de ses chiffres, aucun écart » (V-7) et le résumé de mon verdict (V-2, V-4) disent ce que dit mon rapport.

Le fichier des différences déclare aussi ce qui n'a pas été appliqué : la forme du point 4 de chaque geste dans l'application, ma remarque 2, sans couple et non commandée. C'est exact, ce texte est inchangé.

## 3. Aucun statut, aucune consigne, aucun chiffre ne change

**Oui.**
- Aucun des 26 changements ne touche un qualificatif, un statut de fiabilité, un texte de consigne, un tableau ou un chiffre recopié de l'analyse. Les seuls chiffres neufs sont ceux de mes couples, que j'avais vérifiés contre l'analyse, plus les empreintes et les dates des en-têtes.
- J'ai rejoué mes deux contrôles de chiffres sur les versions 2. Gabarit : 323 contrôles (lignes de consigne 70, tableau de rattachement 144, sensibilités 24, tableau des gestes sans consigne 85), aucun écart. Application pas à pas : 1 112 contrôles, aucun écart.
- L'analyse est inchangée (même empreinte), donc le rejeu de la règle de ma contre-lecture vaut encore : 25 statuts et 25 qualificatifs identiques, 17 comparaisons pour la correction de Holm, objections à prévenir : explication concurrente du résultat et antériorité.

## 4. Les deux calculs refaits à la main par le rédacteur

**Justes.** Test du signe exact, bilatéral, et premier pas de la correction de Holm sur 17 comparaisons (la plus petite valeur brute multipliée par 17) :
- **10 paires contre 0** : valeur brute 2/2¹⁰ = 0,001953 ; × 17 = **0,0332**, soit 0,033 : sous 0,05, l'écart passe.
- **9 paires contre 0** : valeur brute 2/2⁹ = 0,003906 ; × 17 = **0,0664**, soit 0,066 : au-dessus de 0,05, l'écart ne passe pas.

L'écart observé minimal qui peut passer est donc 10/23 = 0,435, comme le disent le couple G-1 et le changement commandé M-2. Le troisième calcul que cite le fichier des différences est juste aussi : 12/124 = 0,0968 ; 13 codages sur 124 donneraient 0,1048. Ces valeurs ne figurent que dans le fichier des différences, pas dans les versions 2.

## 5. Remarque non bloquante (sans effet sur le billet)

L'en-tête de la section 4 du gabarit v2 dit encore « deux lectures écrites côte à côte dans l'application pas à pas, section 7 ». Or mes couples G-10 et A-2 ont placé les deux lectures de la **huitième** ambiguïté dans le gabarit lui-même ; l'application ne fait qu'y renvoyer, dans son paragraphe des points de forme. Le renvoi est donc inexact pour ce seul point. C'est un effet de bord de mes couples, et non un écart du rédacteur. Couple facultatif, à appliquer seulement si une version 3 se fait pour une autre raison (une seule occurrence dans la version 2) :
- Ancien : `## 4. Règles ambiguës relevées (deux lectures écrites côte à côte dans l'application pas à pas, section 7 ; rien n'est tranché)`
- Nouveau : `## 4. Règles ambiguës relevées (deux lectures écrites côte à côte dans l'application pas à pas, section 7, et ici même pour la huitième ; rien n'est tranché)`

Pour mémoire : les en-têtes des versions 2 disent « la version 2 n'a pas été relue après l'application des couples ». C'était vrai quand elles ont été écrites ; la présente vérification est la relecture. Ce qui cite les versions 2 (le billet en blocs) peut renvoyer à ce rapport.

## 6. Refus, lectures hors mandat, ce qui a été écrit

- **Refus d'outil, de permission, de crochet ou de classifieur** : aucun.
- **Lecture hors des pièces nommées** : la ligne R-3496 du registre des décisions, citée par le changement commandé M-1, pour vérifier ce qu'il en dit.
- **Écrit** : ce seul fichier et son compagnon d'empreinte. Un programme dans le dossier de brouillon de la session, recopié en annexe. Ni commit, ni poussée, rien sous `registres/`, `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.

## Annexe — programme de reconstruction

Empreinte du fichier exécuté : `e1ad6232530ae0a6f9e0db2dba4b2af5ab175afa315ee4ef5031176b7d0d6eef`. Exécuté depuis la racine du dépôt (`python3 -I -B reconstruire_v2.py`). Sortie : 17 couples lus, 26 changements lus ; « ancien » et « nouveau » identiques pour les 17 ; « gabarit reconstruit identique à la v2 : True » ; « application reconstruite identique à la v2 : True ». Les contrôles de chiffres rejoués sont les programmes des annexes B et C de `contre-lecture-gabarit-v1.md`.

```python
"""Reconstruit les versions 2 du gabarit et de l'application à partir des versions 1 :
les 17 couples lus dans la contre-lecture scellée, puis M-1, M-2, V-1 à V-7 lus dans
le fichier des différences ; compare à l'octet aux versions 2. Écrit par le contre-lecteur."""
import re
import sys

B = "docs/notes/billets-v1/"
R = open(B + "contre-lecture-gabarit-v1.md", encoding="utf-8").read()
sec = R.split("## 7. Couples exacts")[1].split("## 8.")[0]
blocs = re.split(r"\n\*\*([GA]-\d+)\*\*", sec)


def code(s):
    s = s.strip()
    m = re.match(r"^``(.*)``$", s, re.S) or re.match(r"^`(.*)`$", s, re.S)
    return m.group(1)


mes = {}
for i in range(1, len(blocs), 2):
    nom, b = blocs[i], blocs[i + 1]
    anc = code(re.search(r"- Ancien : (.*)", b).group(1))
    nouv = re.search(r"```\n(.*?)\n```", b, re.S).group(1) if "```" in b else code(re.search(r"- Nouveau : (.*)", b).group(1))
    mes[nom] = (anc, nouv)

D = open(B + "differences-gabarit-v1-vers-v2.md", encoding="utf-8").read()
diff = {}
for m in re.finditer(r"### ([GAMV]-\d+) — (gabarit|application pas à pas)[^\n]*\n\nAncien :\n\n~~~\n(.*?)\n~~~\n\nNouveau :\n\n~~~\n(.*?)\n~~~", D, re.S):
    diff[m.group(1)] = (m.group(2), m.group(3), m.group(4))
print("couples lus dans la contre-lecture :", len(mes), "; changements lus dans les différences :", len(diff))
for k, (a, n) in mes.items():
    f, a2, n2 = diff[k]
    print(k, "ancien", "identique" if a == a2 else "DIFFÉRENT", "; nouveau", "identique" if n == n2 else "DIFFÉRENT")

ga = open(B + "gabarit-billets-v1.md", encoding="utf-8").read()
ap = open(B + "application-regle-gabarit-v1.md", encoding="utf-8").read()


def remplacer(t, a, n, k):
    c = t.count(a)
    if c != 1:
        sys.exit(f"{k} : {c} occurrences")
    return t.replace(a, n)


for k, (a, n) in mes.items():  # couples lus dans la contre-lecture, pas dans les différences
    if k.startswith("G"):
        ga = remplacer(ga, a, n, k)
    else:
        ap = remplacer(ap, a, n, k)
for k in ["M-1", "M-2", "V-1", "V-2", "V-3", "V-4", "V-5", "V-6", "V-7"]:
    f, a, n = diff[k]
    if f == "gabarit":
        ga = remplacer(ga, a, n, k)
    else:
        ap = remplacer(ap, a, n, k)
print("gabarit reconstruit identique à la v2 :", ga.encode("utf-8") == open(B + "gabarit-billets-v2.md", "rb").read())
print("application reconstruite identique à la v2 :", ap.encode("utf-8") == open(B + "application-regle-gabarit-v2.md", "rb").read())
```
