# Construit l'erratum 2 du programme v3 (deux épreuves avant la porte G0).
# Ecrit un seul fichier : celui que la consigne nomme.
import hashlib, re

RACINE = '/home/user/controle-ia-travail/'
CIBLE = 'docs/programme-controle-ia-v3.md'
SORTIE = 'docs/notes/dossier-entretien-2026-12-01-v1/erratum-2-programme-v3-epreuves-avant-g0-v1.md'
ERR1 = 'docs/notes/dossier-entretien-2026-12-01-v1/erratum-1-programme-v3-lemme-application-v3.md'
COPIE_B = 'docs/notes/dossier-entretien-2026-12-01-v1/application-demande-27-defaut-2026-11-24/programme-controle-ia-v3-lecture-avec-erratum-1-variante-B.md'

E = [
    ("E-1",
     "**Porte G0 (prêt pour G1)** :",
     "**Deux épreuves avant la porte G0, dans cet ordre** (inscrites le 24 novembre 2026 : GO-2026-11-24-21, GO-2026-11-24-22 et GO-2026-11-24-31). (i) La tenue de nos organismes face à un entraînement sans contenu : la tenue de l'adaptateur sous récompenses au hasard. C'est la première épreuve. (ii) Le témoin bénin apparié, lu sur plusieurs courses d'entraînement : un seul témoin ne suffit pas. Chez Soopal et al. 2026 (arXiv 2611.14950, version 1 ; pages du PDF : p. 6, section 4.3 ; p. 7 et 8, discussion), une sonde apprise contre un adaptateur bénin apparié sépare dans la course d'entraînement où elle est apprise, et ne se transporte pas aux autres courses. Leur terrain est la sous-performance délibérée aux évaluations, non le sabotage diffus : la transposition est notre lecture. Règles en vigueur, rappelées : préenregistrement scellé avant toute lecture décisive, devis avant toute dépense. Cette inscription est de calendrier : elle ne change aucun critère de la porte. **Porte G0 (prêt pour G1)** :",
     "Section 10, phase 0. GO-2026-11-24-21, point 10 : « la première épreuve est de vérifier que nos organismes tiennent face à un entraînement sans contenu : inscris-le dans le programme ». GO-2026-11-24-31, point 3 : tenue de l'adaptateur sous récompenses au hasard, option (a), « AVANT la porte G0 ». GO-2026-11-24-22 : inscrire au programme le témoin bénin apparié, seconde priorité commune à Fable, Carbon et Opus. Soopal et al. : `docs/sources/pdf/2611.14950v1.pdf` (6396abd5), p. 6 : « works within one training run […] It does not carry across runs » ; p. 7 et 8 : « Probes need matched controls across training runs. […] A matched benign adapter fixes this within a training run but not across runs »."),
    ("E-2",
     "| Phase 0, porte G0 |",
     "| Phase 0 ; avant la porte G0, dans cet ordre : (i) tenue de nos organismes face à un entraînement sans contenu (tenue de l'adaptateur sous récompenses au hasard) ; (ii) témoin bénin apparié sur plusieurs courses d'entraînement (Soopal et al. 2026, p. 6, 7 et 8) ; puis porte G0 |",
     "Section 14, table du calendrier, ligne M0. Mêmes décisions. La période écrite dans cette ligne n'est pas touchée."),
]

p = open(RACINE + CIBLE, encoding='utf-8').read()
assert hashlib.sha256(p.encode('utf-8')).hexdigest().startswith('fcc27171')
pb = open(RACINE + COPIE_B, encoding='utf-8').read()

# ANCIEN de l'erratum 1, variante B (huit entrées)
e1 = open(RACINE + ERR1, encoding='utf-8').read()
bloc = e1.split('<!-- variante B : début -->')[1].split('<!-- variante B : fin -->')[0]
anciens1 = re.findall(r'^\*\*L-\d\.\*\* ANCIEN : « (.*) »$', bloc, flags=re.M)
assert len(anciens1) == 8, len(anciens1)
spans1 = []
for a in anciens1:
    assert p.count(a) == 1, a[:40]
    i = p.find(a)
    spans1.append((i, i + len(a)))

spans2 = []
for ident, ancien, nouveau, raison in E:
    for s in (ancien, nouveau):
        assert '«' not in s and '»' not in s and '\n' not in s, ident
    assert 'sous simulation' not in nouveau
    assert p.count(ancien) == 1, ident          # une fois dans le programme scellé
    assert pb.count(ancien) == 1, ident         # une fois dans la copie de lecture, erratum 1 appliqué
    for a in anciens1:
        assert ancien not in a and a not in ancien, ident   # pas de recouvrement de textes
    i = p.find(ancien)
    for (x, y) in spans1:
        assert i + len(ancien) <= x or y <= i, ident         # pas de recouvrement de positions
    spans2.append((i, i + len(ancien)))
spans2.sort()
assert spans2[0][1] <= spans2[1][0]

def applique(t):
    for ident, ancien, nouveau, raison in E:
        assert t.count(ancien) == 1
        t = t.replace(ancien, nouveau)
    return t
h_scelle = hashlib.sha256(applique(p).encode('utf-8')).hexdigest()
h_copie = hashlib.sha256(applique(pb).encode('utf-8')).hexdigest()
lignes = [p[:s[0]].count('\n') + 1 for s in spans2]

tete = """# Erratum 2 du programme v3 — deux épreuves inscrites au calendrier, avant la porte G0 — v1

Écrit le 2026-11-24 vers 18:50Z (`date -u` relevé à 18:40Z au début du travail, à 18:47Z à l'écriture). Rédacteur : Claude Fable 5.2 (`claude-fable-5-2`), effort élevé, sur la consigne `docs/notes/dossier-entretien-2026-12-01-v1/consigne-fable-errata-table-et-programme-v1.md` (80c156c7). Pièce de travail : ni scellée, ni contre-lue à l'écriture.

**Verdict.** Deux entrées inscrivent au calendrier de la phase 0 deux épreuves avant la porte de fin de phase 0 (G0), dans cet ordre : la tenue de nos organismes face à un entraînement sans contenu, puis le témoin bénin apparié sur plusieurs courses d'entraînement. Aucune prédiction, aucun seuil, aucun critère de porte n'est ajouté. Page de Soopal et al. : p. 6 (section 4.3), reprise p. 7 et 8 (discussion).

**Décisions enregistrées** (`registres/go.md` sur `origin/main`, commit `138bb1070`, SHA-256 du fichier d231e77a) :
- GO-2026-11-24-21, point 10 : « la première épreuve est de vérifier que nos organismes tiennent face à un entraînement sans contenu : inscris-le dans le programme ».
- GO-2026-11-24-22 : « go » pour inscrire au programme les deux priorités communes à Fable, Carbon et Opus : le témoin bénin apparié, et la tenue des saboteurs face à un entraînement sans contenu.
- GO-2026-11-24-31, point 3 : tenue de l'adaptateur sous récompenses au hasard, option (a), « AVANT la porte G0 ».

**Lu.** Le programme v3 scellé provisoirement, en entier (`docs/programme-controle-ia-v3.md`, fcc27171). Son erratum 1, version 3, en entier (5b8be265). La copie de lecture avec l'erratum 1, variante B (ad118b3e) : comparée par programme au texte scellé, huit lignes diffèrent, celles des huit entrées de l'erratum 1. Les lignes d'accord ci-dessus. Soopal, Agrawal, Karthikeyan et Lue Chee Lip, « Stress-Testing Sandbagging Detection Under Adaptive Attack », arXiv 2611.14950, version 1 du 11 novembre 2026 (`docs/sources/pdf/2611.14950v1.pdf`, 6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6, identique à son compagnon) : 14 pages ; lues, les pages 1 (résumé), 3 (contributions, travaux voisins), 4 (règle de transfert), 6 (section 4.3 et figure 3), 7 et 8 (discussion, conclusion, limites) ; le reste parcouru par mots.

**Non lu.** Aucun préenregistrement, aucun devis, aucun avis d'Opus, de Carbon ou de Neon sur ces épreuves. Aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ; rien sous `coffre/`.

## Ce que dit la page citée (règle R7)

Le PDF ne porte pas de numéro de page imprimé : les pages sont celles du fichier.

- **p. 6, section 4.3** (« Activation probes detect fine-tuning, not sandbagging »). Une sonde apprise contre le modèle de base signale presque tous les exemples d'adaptateurs bénins. Apprise contre un adaptateur bénin apparié, elle « works within one training run » ; puis : « It does not carry across runs (Figure 3). » En mettant cinq paires de graines en commun et en en tenant une à l'écart, la sonde appariée passe la règle de transfert des auteurs dans 1 pli sur 5 ; avec les négatifs de trois recettes bénignes, dans 2 plis sur 5, quand la règle en exige 4 (règle fixée d'avance, p. 4).
- **p. 7 et 8, discussion.** « Probes need matched controls across training runs. » Et : « A matched benign adapter fixes this within a training run but not across runs ».

**Portée de cette source.** Elle soutient « un seul témoin bénin apparié, dans une seule course d'entraînement, ne suffit pas ». Elle ne dit pas que plusieurs courses suffisent : chez ses auteurs, la sonde échoue aussi à leur règle sur plusieurs courses. Son terrain est la sous-performance délibérée aux évaluations, sur de petits modèles à adaptateur ; l'emploi pour nos saboteurs diffus est notre lecture.

## Forme, pour le programme d'application

Cible : `docs/programme-controle-ia-v3.md` (fcc27171bb87e35a42a6e200bb7ddf8c3df9106141b6eace541e283beb5458c9).

Même forme que l'erratum 1 : trois lignes consécutives par bloc, une ligne vide entre les blocs. Aucun texte ANCIEN ni NOUVEAU ne porte de guillemet français, de saut de ligne ni la marque de simulation.

Vérifié par programme, en lecture seule. Chaque ANCIEN figure une fois dans le programme scellé (lignes %d et %d) et une fois dans la copie de lecture où l'erratum 1 est appliqué. Aucun ANCIEN ne contient un ANCIEN de l'erratum 1, variante B, ni n'y est contenu ; leurs positions dans le texte scellé ne se recouvrent pas. L'entrée E-1 touche la ligne de la porte G0 ; l'entrée L-6 de l'erratum 1 touche la ligne qui la précède. Les deux errata s'appliquent donc dans un ordre quelconque.

Empreintes après application des deux entrées, dans l'ordre, par simple remplacement (calculées en mémoire, aucun fichier écrit) :
- sur le programme scellé seul : `%s` ;
- sur la copie de lecture avec l'erratum 1, variante B : `%s`.

## Entrées

Cible : docs/programme-controle-ia-v3.md

""" % (lignes[0], lignes[1], h_scelle, h_copie)

corps = []
for ident, ancien, nouveau, raison in E:
    corps.append("**%s.** ANCIEN : « %s »\nNOUVEAU : « %s »\nRaison : %s\n" % (ident, ancien, nouveau, raison))

fin = """## Ce qui reste ouvert

1. **Deux précisions viennent de la consigne, non de la lettre des lignes d'accord lues.** La ligne GO-2026-11-24-22 dit « le témoin bénin apparié », sans « sur plusieurs courses d'entraînement » ni le nom de Soopal et al. Seule la tenue de l'adaptateur est dite « AVANT la porte G0 » (GO-2026-11-24-31, point 3) ; la place du témoin bénin apparié avant cette porte me vient de la consigne. J'ai écrit ce que la consigne demande. À confirmer d'un mot, ou par la ligne de registre qui le porte.
2. **Ce que l'issue de chaque épreuve commande.** Les décisions lues inscrivent les épreuves ; elles ne disent pas ce qu'un échec change à la porte G0, aux organismes ou aux sondes. Les critères de la porte ne sont pas touchés (`CLAUDE.md` : « critères inchangés »). C'est un nœud si une issue doit peser sur la porte.
3. **Portée de la première épreuve.** Lazar dit « nos organismes » ; l'option retenue dit « l'adaptateur ». Le programme a deux modes d'induction (consigne cachée, adaptateur). J'ai écrit les deux formules côte à côte, sans trancher si l'organisme à consigne cachée est visé.
4. **Préenregistrements et devis.** Les deux épreuves n'ont, à ma connaissance, ni préenregistrement ni devis ; je n'en ai lu aucun. Ils restent à écrire avant toute lecture décisive et toute dépense.
5. **Dates.** La section 10 et la table de la section 14 portent encore « 5 octobre → 1er novembre 2026 » pour la phase 0. Selon `CLAUDE.md`, la porte G0 est attendue au plus tard fin décembre 2026 (GO-2026-11-18-01). Je n'y ai pas touché : hors de la consigne.
6. **Trois passages de la section 5 attendent leur propre erratum**, par les décisions sur la table des revendications (GO-2026-11-24-21, point 5) : « plate » sans la condition d'indépendance des copies honnêtes (H3), « angle mort identifié » (Tr), la loi sur le nombre et la diversité des moniteurs (H5). Ils ne sont pas dans cet erratum : la consigne le borne au calendrier.
7. **En-tête du programme.** Il cite l'erratum 1, non celui-ci. Une retouche hors blocs reste à la main de la session mère, si le texte corrigé doit le dire.
8. **Transposition de Soopal et al.** Voir « Portée de cette source » : une sonde y échoue aussi sur plusieurs courses. L'épreuve (ii) peut donc échouer chez nous ; rien n'est prédit ici.

## Confiance

Exactitude des deux textes ANCIEN et absence de recouvrement : 0,97, vérifiées par programme. Pages de Soopal et al. : 0,9 (texte extrait du PDF empreinté, citations relues ; pages du fichier, faute de numéros imprimés). Fidélité aux décisions : 0,8, à cause du point 1. Ensemble : 0,8.
"""

texte = tete + "\n".join(corps) + "\n" + fin
open(RACINE + SORTIE, 'w', encoding='utf-8').write(texte)
print(len(E), 'entrées ; lignes', lignes, h_scelle, h_copie)
print(hashlib.sha256(texte.encode('utf-8')).hexdigest())
