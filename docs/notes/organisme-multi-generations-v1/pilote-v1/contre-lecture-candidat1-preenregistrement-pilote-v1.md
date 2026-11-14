# Contre-lecture du candidat 1 du préenregistrement du pilote MR-2 (compte organisme) — v1

- **Rédacteur du candidat : modèle A ; contre-lecteur : modèle B ; A ≠ B** (identités données par la session mère ; je ne les ai
  pas vérifiées moi-même). Je n'ai écrit ni le candidat, ni les brouillons 1 à 4, ni les codes v68 à v73, ni la conception v4.
  Réserve de lignée : le modèle B est de la même maison que le modèle A et de la même lignée qu'un des proposeurs du pilote.
- **Heures** (`date -u`) : début 2026-11-14 10:55:56 UTC ; fin : dernière ligne.
- **Interdits** : aucune dépense, aucun appel réseau, aucune clé lue, aucun chemin interdit ouvert, aucune recherche récursive,
  aucune écriture git, aucun `git fetch`, aucun refus rencontré ; ni sonde ni pilote lancés. Lancés, sur processeur seulement :
  la sous-commande `bloc` du lanceur v73 sans relevé, les fonctions de lecture de la configuration et des lignes de GO sur un
  registre d'essai écrit au brouillon de session, `controle_ia.prereg.problemes` sur le candidat, et mon programme de comptage.
  Rien d'écrit dans le dépôt hors de ce fichier et de son compagnon.

## Verdict (une ligne)

**Scellable après la sonde et des corrections** : 0 bloquant, 7 majeurs, 13 mineurs ; aucune hypothèse, prédiction, métrique
principale, seuil ni critère de lecture n'est changé ; le code nommé est celui de l'arbre ; les chiffres du devis sont justes.

## Pièces vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| candidat 1 | `48065053ea5647cf7563071aafd00bb20e43ff9853e149f85951efa5179c3e82` | égale au compagnon ; lu en entier (575 lignes) |
| brouillon 4 | `04ada9fae5d93f67674af2d98282efc5ebe6d2fb81f755dcc5789b7b4fba450a` | égale au compagnon |
| différentiel brouillon 4 → candidat 1 | — | refait par `diff -u` : identique au fichier donné ; lu en entier |
| vérification courte v2 ; contre-lecture v2 | `9b662803…` ; `823b6e9e…` | égales aux compagnons |
| rapport du développeur v73 ; devis et lignes ; empreintes du code ; paquet | `e41ed80f…` ; `a382e9c0…` ; `f734fe55…` ; `2b4017c7a4d675cde73b2e0bf9abc6e6c455f4854668f591668c1d2bba293b6e` | les quinze compagnons du dossier `code-v73-compte-organisme/` conformes |
| arbre de l'organisme | tête `ce8c6967e59f6ebbfa7b30654bde04fba716c70c`, propre | lanceur v73 `88f99766…`, sonde v72 `636d5a95…`, configuration v12 `f69503dd…`, lecture v72 `de6bc923…`, cœur v70 `7541b0c3…`, programme v4 `676d5f37…` : égales au rapport et à la pièce des empreintes |
| bloc gelé provisoire | — | `bloc` (sans relevé) rendu par l'arbre : **égal à l'octet** à `EMPREINTES-code-pilote-v73.txt` ; aucun identifiant de modèle, aucun crochet |
| registre | — | R-2542, R-2548, R-2596, R-2599, R-2613, R-2620, R-2621, R-2663 (registre local) ; R-2690, R-2700 et la ligne GO-2026-11-14-02 (`origin/main`, tête `ade0a404`, 10:16:38Z) : lues. **R-2712 : absente** des deux (constat 6) |

## Réponses aux sept questions

| # | question | réponse |
|---|---|---|
| 1 | R-2542 et R-2548 portées, exactement ? | **Oui.** Parts 20,00 (12 + 8) et 21,72 (9,36 + 9,36 + 3,00) ; plafonds de session 3 ; 2 ; 2,34 ; 2,34 (part = 4 plafonds, contrôlé par le code) ; bornes 64 000 ; 89 000 ; 36 000 ; 36 000, chacune sous la borne que le plafond paie (64 395 ; 89 395 ; 36 195) ; effort « high » aux deux proposeurs sur crédits de Claude, objet vide aux deux autres ; loi de référence hors de ±4 récrite en `transformee` (code : `pole/pilote_mr2_v70.py`, ligne 659) ; coût au-dessus du pire cas = arrêt, code 3, appel porté au relevé partiel ; `mesurer` et `lire` liés aux mondes du manifeste ; sonde avant le scellement, deux lignes à part 4,39 et 3,68. Réserves : constats 4, 7, 14 et 15 |
| 2 | Le code nommé est-il celui de l'arbre ? | **Oui.** Noms, empreintes et options exacts : `jouer --mode reel` avec ses huit options exigées, `mesurer --sortie --mondes --mondes-sha256`, `lire --sortie`, `bloc --releve-sonde`, `sonde`. La liste des sous-commandes est incomplète (constat 10) |
| 3 | Sections reprises intactes ; rien d'autre changé ? | **Oui pour le fond.** Hypothèse, Prédiction, Seuil, Critères de lecture gelés, Audit de symétrie, Décisions de Lazar, Portée : aucun octet changé. Métrique : un point ajouté (« Réflexion et coût », secondaire, aucune issue). Plan d'analyse : étapes 2 et 3 récrites (R-2548). Liste d'arrêt : deux arrêts ajoutés. Écarts hors décisions, à dire : constats 4, 15, 17, 18 |
| 4 | Devis et lignes | **Chiffres justes** (rejeu ci-dessous) ; les quatre lignes proposées, marqueurs levés, sont **lues** par le lecteur gelé au montant exact, mots du périmètre présents ; trois artefacts refusés. Réserves : constats 7, 12, 13, 14 |
| 5 | Marqueurs | Liste **complète** pour les crochets (9 marqueurs, 27 occurrences, aucun autre) ; **mais** quatre d'entre eux ne peuvent pas être levés avant le scellement, deux servent à deux inscriptions, un est employé à tort, et des phrases en attente n'ont pas de marqueur (constats 1, 2, 3, 8) |
| 6 | Identifiant de modèle Claude dans le texte ? | **Aucun** (recherche des formes d'identifiant et des noms de modèle : zéro ligne). « Claude » n'y figure que comme nom de fournisseur (« crédits de Claude », « voie de Claude ») ; les proposeurs sont nommés par leurs clés de configuration, ce que R-2690 a choisi |
| 7 | Ce qui manque | section finale |

## Rejeux

**Pires cas** (règle de la commande, fonctions `pire_cas_d_un_appel` et `borne_de_sortie_max` du code, égales au calcul à la main) :

```
fable52: sonde 2.568992 + 0.019232 = 2.588224 ; part sonde 2.59 ; pilote à 52000 octets 2.984192 ≤ plafond 3.0 : True ; borne max 64395 ; 4 × plafond = 12.00 ; part 12.0
opus55: sonde 1.784496 + 0.009616 = 1.794112 ; part sonde 1.8 ; pilote à 52000 octets 1.992096 ≤ plafond 2.0 : True ; borne max 89395 ; 4 × plafond = 8.00 ; part 8.0
argon: sonde 1.811240 + 0.024040 = 1.835280 ; part sonde 1.84 ; pilote à 52000 octets 2.330240 ≤ plafond 2.34 : True ; borne max 36195 ; 4 × plafond = 9.36 ; part 9.36
astra: sonde 1.811240 + 0.024040 = 1.835280 ; part sonde 1.84 ; pilote à 52000 octets 2.330240 ≤ plafond 2.34 : True ; borne max 36195 ; 4 × plafond = 9.36 ; part 9.36
total sonde 8.052896
```

Sommes : 2,59 + 1,80 = 4,39 ; 1,84 + 1,84 = 3,68 ; 4,39 + 3,68 = 8,07 ; 20,00 + 21,72 = 41,72 ; 41,72 + 8,07 = 49,79. Tous les
chiffres de la table du devis (lignes 464 à 477) sont justes.

**Lecteur gelé des lignes** (`lire_go_de_la_sonde`, `lire_go_du_pilote` de `pole/proposeurs_pilote_v70.py`, lecteur v66 ; registre
d'essai au brouillon de session ; date d'essai le 14 novembre 2026) :

```
== lignes proposées du candidat, marqueurs levés (identifiant nu, date, mot)
leve lire_go_de_la_sonde LU : {'s1': (4.39, 'montant seul'), 's2': (3.68, 'montant seul')}
leve lire_go_du_pilote LU : {'pi1': (20.0, 'montant seul'), 'pi2': (21.72, 'montant seul')}
== artefact : identifiant entre crochets laissé
crochets lire_go_de_la_sonde REFUS : GO s1 : A15 : GO-2026-11-14-91 absent du registre
crochets lire_go_du_pilote REFUS : GO pi1 : A15 : GO-2026-11-14-93 absent du registre
== artefact : montant de s1 changé en 4.40
montant lire_go_de_la_sonde REFUS : GO s1 : A15 : la ligne GO-2026-11-14-91 porte 4.4 USD (montant seul), pas exactement le montant requis 4.39 USD
== artefact : mot « pilote » retiré de la ligne pi2 (Même pilote -> Même essai)
perimetre lire_go_du_pilote REFUS : GO pi2 : périmètre sans ['pilote']
```

« 20 USD (sur crédits) » est lu 20 (montant seul). `controle_ia.prereg.problemes` sur le candidat rend une liste vide (constat 5).

## Constats

### Majeurs

**1. Quatre marqueurs ne peuvent pas être levés avant le scellement** (lignes 553 à 565, contre 271 et 449). Le titre dit « aucun
ne doit rester au scellement » ; [GO-PI1] et [GO-PI2], avec leur date et leur mot, attendent « l'inscription des lignes du
pilote » ; or l'ordre (ligne 271) est « texte scellé → lignes π1 et π2 inscrites », et la ligne π1 exige elle-même le
« préenregistrement […] scellé ». Tel qu'écrit, le texte ne peut jamais être scellé sans défaut. Le brouillon 4 le tolérait
(« normal avant inscription »). Correction, mot pour mot : aux lignes 502 et 503, remettre les formes du brouillon 4
« GO-AAAA-MM-JJ-NN (π1) », « GO-AAAA-MM-JJ-NN (π2) », « AAAA-MM-JJ », « mot de Lazar à recopier » et « mêmes conditions que la
ligne π1 » ; retirer de la table la ligne « [GO-PI1], [GO-PI2] » ; ajouter sous la table : « Les deux lignes du pilote restent
proposées, non inscrites, dans le texte scellé : elles s'inscrivent après le scellement (section « Ordre ») ; leur identifiant,
leur date et le mot de Lazar vivent au registre des GO, pas dans ce texte. »

**2. [DATE-GO] et [MOT-LAZAR-GO] servent à deux inscriptions** (lignes 495, 496, 502, 503, 565) : les lignes de la sonde et
celles du pilote s'inscrivent à des moments différents, sur des mots différents. Un remplacement global écrirait la date et le mot
de la sonde dans les lignes du pilote. Correction : avec la correction 1, ces deux marqueurs ne restent qu'aux lignes 495 et 496 ;
ligne 565 : « | [DATE-GO], [MOT-LAZAR-GO] | l'inscription des lignes de la sonde | la date d'inscription et le mot de Lazar,
recopié verbatim (lignes de la sonde seulement) | ».

**3. [BLOC-GELE-V73] employé à tort à la ligne 111.** La cellule dit « [BLOC-GELE-V73] (empreinte au bloc gelé définitif ; paquet
scellé avec son compagnon) ». Preuve : le bloc que rend le code (`bloc_gele`, lanceur v73, lignes 123 à 152) porte les empreintes
des fichiers, jamais celle du paquet ; l'empreinte du paquet est connue aujourd'hui et ne dépend pas de la sonde. Un remplacement
du marqueur par le bloc (36 lignes) casserait la table, et `verifier_bloc_du_texte` lit la **première** occurrence du marqueur de
début. Correction, mot pour mot : « | `2b4017c7a4d675cde73b2e0bf9abc6e6c455f4854668f591668c1d2bba293b6e` (paquet scellé avec son
compagnon ; les empreintes de ses fichiers sont au bloc gelé) | ». Le marqueur ne reste alors qu'à la ligne 433.

**4. La suite d'un arrêt n'est pas écrite** (lignes 379 à 395 ; critères, lignes 354 à 361). R-2548 ajoute un arrêt du pilote
plausible (coût au-dessus du pire cas, que le devis lui-même dit possible chez `argon`, ligne 482). Preuve dans le code : après un
arrêt, le manifeste est partiel et `CARTES-partiel.json` est écrit ; `mesurer` refuse un manifeste partiel (lanceur, ligne 524) ;
un second lancement réel pour ce texte est refusé (ligne 246). Aucune issue n'est donc calculée, pas même P-0, dont la condition
(« moins de 12 appels répondus ») est lue au champ `regle` d'un programme qui n'a pas tourné. Un lecteur pourrait y lire P-0, un
autre rien. Correction proposée, à ajouter en fin de liste d'arrêt (décision de la mère : elle touche la lecture) : « Tout arrêt
(code 3) après le premier appel : le relevé et le manifeste sont partiels, la mesure n'est pas lancée (le lanceur la refuse),
**aucune issue n'est lue, pas même P-0** ; les pièces sont versées, la cause écrite ; les quatre mondes ne sont jamais
réutilisés ; nœud de Lazar ; toute reprise demande un texte neuf, scellé, et des mondes neufs. »

**5. Section « Contre-lecture » : entrée absente, et que la garde mécanique ne verra pas** (lignes 547 à 549). Le candidat dit sa
contre-lecture « à faire […] après la sonde (le bloc gelé définitif recopié) » ; la présente lecture a lieu **avant** la sonde.
Preuve : `problemes()` rend déjà une liste vide sur le candidat (cinq empreintes d'anciennes lectures suffisent à sa règle) :
`sceller_prereg` scellerait un texte dont la contre-lecture n'est pas consignée. Correction, mot pour mot : « - **Contre-lecture
du candidat 1** : lecteur neuf, modèle B, autre modèle que le rédacteur (modèle A ; A ≠ B) ; texte relu
`48065053ea5647cf7563071aafd00bb20e43ff9853e149f85951efa5179c3e82`, avant la sonde ; rapport
`pilote-v1/contre-lecture-candidat1-preenregistrement-pilote-v1.md` (empreinte de son compagnon) ; verdict « scellable après la
sonde et des corrections ». - **Vérification courte du différentiel candidat 1 → texte à sceller** (corrections portées, bloc gelé
recopié, marqueurs levés) : lecteur neuf, autre modèle que le rédacteur ; texte relu, rapport et empreintes. » Et à la réserve de
lignée : « le lecteur du candidat est de la même maison que son rédacteur et de la même lignée qu'un des proposeurs. »

**6. « inscrite R-2712 » : non vérifiable, et employée pour deux objets** (ligne 443). R-2712 n'est ni au registre local ni à
`origin/main` tel que je peux le lire (dernière entrée R-2701, tête de 10:16:38Z) ; le candidat l'emploie pour la sonde du seul
relais Astra, la pièce du devis pour sa soumission à Lazar (« qui le soumet à Lazar (R-2712) »). Le relevé `40eb7b32…` et
« 0,0167 USD » concordent avec la section 6 du rapport du développeur, mais le candidat ne donne pas le chemin du relevé (R6).
Correction : écrire le chemin du relevé de la sonde du seul relais, et, à la place de « inscrite R-2712 », le numéro que le
registre de `main` porte réellement au jour du scellement, relu ; s'il n'y en a pas : « consignée au journal du compte organisme ».

**7. Aucun critère sur les prix lus à la console** (ligne 443, préalable 3 ; ligne 481). Les pires cas, les plafonds et la garde
« coût au-dessus du pire cas » sont calculés aux prix de la configuration ; ceux d'`argon` et d'`astra` y sont « supposés »
(ligne 461). Si un prix réel est plus haut, la garde ne voit rien et les parts ne bornent plus la dépense. Le texte dit de
« rapprocher », pas quoi faire d'un écart. Correction, mot pour mot, au préalable 3 : « (3) prix lus par Lazar à la console,
rapprochés des coûts du relevé ; **si un prix réel d'entrée ou de sortie dépasse celui de la configuration v12 : nœud de la mère,
aucun scellement** (les pires cas et les parts ne seraient plus des bornes ; une configuration neuve demande un code qui la nomme
et une sonde neuve) ; ».

### Mineurs

**8. Phrases en attente sans marqueur** : lignes 3 (statut), 13 à 15, 32, 146, 231, 244, 314 à 315 (« à confirmer par la sonde »,
« doit confirmer »), 115 (« (à jouer) », chemin du relevé absent), 437 à 447 (préalables au futur). La section des marqueurs
elle-même garde ses crochets (lignes 560 à 565). Correction : à la levée, mettre ces phrases au passé avec le chemin du relevé
(`…/releve-sonde-pilote-v72.json`) ; remplacer la table par « Aucun marqueur ne reste » et la liste de ce qui a été levé, écrite
sans crochets ; rejouer le programme ci-dessous : il doit compter zéro marqueur.

**9. Heure de début absente** (ligne 24 : « début […] : dernière ligne » ; la ligne 575 ne donne que la fin).

**10. Sous-commandes** (ligne 427) : la liste omet `secret`, `generer`, `preparer` et `sonde-un`, que le lanceur porte et que
l'ordre (ligne 272) emploie. Correction : « (sous-commandes `secret`, `generer`, `preparer`, `sonde`, `sonde-un`, `jouer`,
`mesurer`, `lire`, `relire`, `rapatrier`, `bloc`) ».

**11. Essais et bancs du code v72 et v73 dits sans chiffres** (lignes 416 et 437 : « bancs de mutations passés »). Le rapport du
développeur dit plus : v73, 138 essais ; banc v72, 72 mutations tuées sur 73 (N18 survit, reciblée en N18b, tuée au banc v73) ;
banc v73, 35 sur 35, dont B03 au second passage après reciblage ; U14 non couverte. Les deux contre-lectures du code
(`a4420d6b…`, `aa53683e…`) ne sont pas à la table des documents. Correction : écrire ces chiffres tels quels et ajouter les deux
lignes (chemin, empreinte).

**12. Trois attendus de la sonde** : « < 1,00 » (candidat, lignes 144 et 470), « < 0,85 » (pièce du devis), « moins de 0,10 »
(R-2548). L'écart à R-2548 est dit et motivé (ligne 479). N'en garder qu'un entre le candidat et la pièce du devis.

**13. Deux textes « mot pour mot » des lignes de la sonde** : le candidat cite « R-2621 » et « la ligne [GO-S1] » ; la pièce du
devis cite « R-2621, R-2690, R-2712 » et « la ligne s1 ». Les deux sont lus par le lecteur gelé ; n'en garder qu'un.

**14. Ligne π2 fragile** : le mot exigé « pilote » (minuscule) n'y figure qu'une fois, dans « Même pilote » (artefact rejoué :
refus sans lui). À ne pas retoucher à l'inscription ; le dire sous les lignes.

**15. `transformee` (R-2542)** n'est écrite qu'à la table du code (ligne 424) ; la liste d'arrêt (ligne 383) et la ligne 57
(« `softmax`, `si_sinon`, `par_sous_population` seulement », historique) ne le disent pas. Correction, ligne 383 : « (une loi de
référence refusée au gardien, après récriture en `transformee` équivalente de toute feuille hors des bornes ±4, R-2542 ; écart
d'évaluation > 10⁻⁹) ».

**16. Portée** (ligne 535) : la mesure vaut « devant ce gabarit » ; depuis R-2542 elle vaut aussi pour les réglages envoyés.
Suggestion (ajout d'une limite, décision de la mère) : « devant ce gabarit, **sous ces réglages (effort « high » aux deux
proposeurs sur crédits de Claude, aucun aux deux autres) et ces bornes de sortie** ».

**17. Retraits non dits à la table des changements**, sans effet sur le fond : la ligne « Calculs » de l'en-tête (versions de
Python et de numpy ; numpy reste au bloc gelé) ; la phrase « Ses titres de niveau 2 sont ceux du gabarit » (vérifié : les huit
sections exigées sont présentes) ; « Chaque garde neuve essayée sur un cas sain et un artefact (R5) […] servent aussi la
course » ; les trois entrées détaillées de la section « Contre-lecture », fondues en une.

**18. Définitions de C-1 à C-18** : la table qui les énonçait est remplacée par une table de correspondance ; elles ne vivent plus
que dans le brouillon 4, cité avec son empreinte (ligne 413). Acceptable ; la liste d'arrêt s'appuie sur C-16 et C-17 par ce
renvoi.

**19. Hors du différentiel, pour mémoire** : ligne 258, `echelle` et `enveloppe` ne sont pas des types du gardien de l'arbre
(`TYPES_PERMIS` : `softmax`, `par_sous_population`, `si_sinon`, `melange`, `fixe`, `transformee`) ; phrase du brouillon 4, sans
effet. Les entrées R-2620 et R-2621 du registre portent la date du 14 novembre à 23:45 UTC, avant R-2663 (07:38 le 14) : erreur du
registre, pas du candidat.

**20. Dépenses déjà faites absentes du devis** : sonde v71 (1,865848 USD comptés, R-2621) et sonde du seul relais Astra
(0,0167 USD) ; une ligne « déjà dépensé » rendrait la table complète.

## Programme de comptage des marqueurs, et sa sortie

```python
"""Contre-lecture du candidat 1 : compte les marqueurs entre crochets et les compare à la liste écrite."""
import collections, re, sys
chemin = sys.argv[1]
lignes = open(chemin, encoding="utf-8").read().split("\n")
MARQUEUR = re.compile(r"\[[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\]")   # [MOT-EN-CAPITALES]
CROCHET = re.compile(r"\[[^\]\n]*\]")                          # tout crochet fermé sur la ligne
debut = next(i for i, l in enumerate(lignes) if l.startswith("## Marqueurs restants"))
fin = next((i for i in range(debut + 1, len(lignes)) if lignes[i].startswith("## ")), len(lignes))
liste = []
for l in lignes[debut:fin]:
    if l.startswith("| ["):
        liste += MARQUEUR.findall(l.split("|")[1])
ou = collections.defaultdict(list)
autres = collections.defaultdict(list)
for n, l in enumerate(lignes, 1):
    for m in CROCHET.findall(l):
        (ou if MARQUEUR.fullmatch(m) else autres)[m].append(n)
print("liste écrite (%d) : %s" % (len(liste), " ".join(liste)))
print("doublons dans la liste :", sorted(m for m, k in collections.Counter(liste).items() if k > 1) or "aucun")
total = 0
for m in sorted(ou):
    hors = [n for n in ou[m] if not debut < n <= fin]
    total += len(ou[m])
    print("%-20s %2d occurrence(s), dont %d hors de la section des marqueurs ; lignes %s" % (m, len(ou[m]), len(hors), ou[m]))
print("total des occurrences :", total)
print("dans le texte, absents de la liste :", sorted(set(ou) - set(liste)) or "aucun")
print("dans la liste, absents du reste du texte :",
      sorted(m for m in liste if not [n for n in ou[m] if not debut < n <= fin]) or "aucun")
print("autres crochets (ni marqueur en capitales) :")
for m in sorted(autres):
    print("  %-40s lignes %s" % (m, autres[m]))
ATTENTE = re.compile(r"à faire|à jouer|AAAA|À REMPLIR|<<|à recopier|à confirmer|à figer|à écrire|TODO", re.I)
print("mots d'attente hors crochets :")
for n, l in enumerate(lignes, 1):
    for m in ATTENTE.findall(l):
        print("  ligne %d : %s" % (n, m))
```

Sortie sur le candidat `48065053…` :

```
liste écrite (9) : [BLOC-GELE-V73] [RELEVE-SONDE-V72] [PRIX-CONSOLE] [GO-S1] [GO-S2] [GO-PI1] [GO-PI2] [DATE-GO] [MOT-LAZAR-GO]
doublons dans la liste : aucun
[BLOC-GELE-V73]       3 occurrence(s), dont 2 hors de la section des marqueurs ; lignes [111, 433, 560]
[DATE-GO]             5 occurrence(s), dont 4 hors de la section des marqueurs ; lignes [495, 496, 502, 503, 565]
[GO-PI1]              3 occurrence(s), dont 2 hors de la section des marqueurs ; lignes [502, 503, 564]
[GO-PI2]              2 occurrence(s), dont 1 hors de la section des marqueurs ; lignes [503, 564]
[GO-S1]               3 occurrence(s), dont 2 hors de la section des marqueurs ; lignes [495, 496, 563]
[GO-S2]               2 occurrence(s), dont 1 hors de la section des marqueurs ; lignes [496, 563]
[MOT-LAZAR-GO]        5 occurrence(s), dont 4 hors de la section des marqueurs ; lignes [495, 496, 502, 503, 565]
[PRIX-CONSOLE]        2 occurrence(s), dont 1 hors de la section des marqueurs ; lignes [481, 562]
[RELEVE-SONDE-V72]    2 occurrence(s), dont 1 hors de la section des marqueurs ; lignes [115, 561]
total des occurrences : 27
dans le texte, absents de la liste : aucun
dans la liste, absents du reste du texte : aucun
autres crochets (ni marqueur en capitales) :
  ["k1"]                                   lignes [44]
  [0 ; 0,0377]                             lignes [176]
  [0,0003 ; 0,0582]                        lignes [177]
  [0,0026 ; 0,0774]                        lignes [178]
  [0,0069 ; 0,0966]                        lignes [179]
  [0,0125 ; 0,1163]                        lignes [180]
mots d'attente hors crochets :
  ligne 32 : à confirmer
  ligne 33 : à faire
  ligne 38 : à figer
  ligne 61 : à figer
  ligne 115 : à jouer
  ligne 231 : à confirmer
  ligne 244 : à confirmer
  ligne 547 : à faire
```

Lecture : 9 marqueurs écrits, 9 trouvés, 27 occurrences, aucun marqueur hors de la liste, aucun marqueur de la liste absent du
texte. Les autres crochets sont des intervalles de confiance (lignes 176 à 180) et un indice de code (ligne 44). Des mots
d'attente, « à faire » ligne 33 est une consigne de calcul, « à figer » lignes 38 et 61 est de l'histoire ; les autres relèvent
du constat 8.

## Ce qui manque avant « scellable après la sonde »

1. Porter les corrections 1 à 7 (texte neuf sous un nom neuf, R12), et les mineurs retenus par la mère ; les corrections 4 et 16
   touchent la lecture ou la portée : décision de la mère, nœud de Lazar si elle les juge un changement de critère.
2. Inscrire les deux lignes de la sonde (identifiant nu) sur le mot de Lazar ; jouer la sonde complète une seule fois par la
   commande versée ; verser relevé et dossier entier.
3. Prix lus par Lazar, comparés aux prix de la configuration (correction 7).
4. `bloc --releve-sonde RELEVE` : bloc recopié tel quel à la ligne 433 seulement ; empreinte du relevé et chemin à la ligne 115 ;
   phrases en attente mises au passé (constat 8) ; programme de comptage rejoué à zéro.
5. Section « Contre-lecture » complétée (correction 5) ; vérification courte du différentiel candidat 1 → texte à sceller par un
   lecteur neuf d'un autre modèle que le rédacteur.
6. Scellement par `controle_ia.prereg.sceller_prereg`, jamais par le rédacteur.

Si le relevé ne confirme pas la configuration v12 (réflexion d'`argon` non observée, par exemple) : aucun scellement, nœud de la
mère, comme le dit le préalable 4.

Fin de la contre-lecture : 2026-11-14 11:02:20 UTC (`date -u`).
