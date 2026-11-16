"""Écrit la version qui fera foi v1 du crible (v) à partir du brouillon 9, par remplacements nommés.

Usage : python3 -I appliquer-version-foi-crible-v-v1.py HEURE_FIN   (HEURE_FIN lue par `date -u`, forme HH:MM)
Lancé depuis le dossier `cribles-v1/`. Vérifie l'empreinte du brouillon 9 et celles des pièces recopiées,
applique chaque remplacement (ancien présent une seule fois, aucun chevauchement), écrit une cible neuve
(refus si elle existe). Aucune donnée lue hors de ce dossier ; bibliothèque standard seule.
"""

import hashlib
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
SOURCE = ICI / "crible-v-brouillon9.md"
CIBLE = ICI / "crible-v-version-foi-v1.md"
EMP_SOURCE = "c574e39d700aaff64c59efd0319aaf565c906ff2518304c6c2f2a752dcd5da23"


def emp(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def compagnon(p):
    return Path(str(p) + ".sha256").read_text(encoding="utf-8").split()[0]


heure_fin = sys.argv[1]
assert re.fullmatch(r"\d\d:\d\d", heure_fin)
assert emp(SOURCE) == EMP_SOURCE, "empreinte du brouillon 9"
assert not CIBLE.exists(), "cible existante : nom neuf exigé (R12)"

pieces = {
    "devis": ICI / "devis-crible-v-foi-v1.py",
    "devis_sortie": ICI / "devis-crible-v-foi-v1-sortie.txt",
    "placebo": ICI / "placebo-crible-v-chrono-v1.py",
    "placebo_sortie": ICI / "placebo-crible-v-chrono-v1-sortie.txt",
    "part": ICI / "part-chere-crible-v-foi-v1.py",
    "part_sortie": ICI / "part-chere-crible-v-foi-v1-sortie.txt",
    "cl9": ICI / "contre-lecture-crible-v-b7-tour3-v1.md",
}
E = {}
for nom, p in pieces.items():
    E[nom] = emp(p)
    assert E[nom] == compagnon(p), f"compagnon de {p.name}"
assert E["cl9"] == "0b4fdd00c8ac7ed4cfa8a806ff3364158628975c735e8669f806746f0e3ee8ac"

# Programmes de l'annexe A, tirés des blocs de code de crible-iii-brouillon1.md, empreintes vérifiées.
iii1 = ICI / "crible-iii-brouillon1.md"
assert emp(iii1) == "00c92559d54349101dfcc0c59afe402c388b192c32fa6018bbf809eb02f22af0"
blocs = re.findall(r"```(?:python)?\n(.*?)```", iii1.read_text(encoding="utf-8"), re.S)
prog = {hashlib.sha256(b.encode()).hexdigest(): b for b in blocs}
P_COMPTES = "f06bcfe7219a22d9b2c117be141739fe21c878d99b8f233725523072088e0f59"
P_CERT = "8c0432df23cb78270c851d2c8f81e40b069a41ffefb8f3ddce03fa72804d9e39"
S_COMPTES = "5d53092e5fc4a6ef087a894035db490536cb9312936cc72dfacf5b6e0eab0cf8"
for h in (P_COMPTES, P_CERT, S_COMPTES):
    assert h in prog, f"bloc {h[:8]} absent"
    assert "\n## " not in "\n" + prog[h] and "```" not in prog[h]

sortie_devis = pieces["devis_sortie"].read_text(encoding="utf-8")
sortie_placebo = pieces["placebo_sortie"].read_text(encoding="utf-8")
sortie_part = pieces["part_sortie"].read_text(encoding="utf-8")
for t in (sortie_devis, sortie_placebo, sortie_part):
    assert "\n## " not in "\n" + t and "```" not in t

VERDICT_CRIBLES = """- Comptes (`corps.appels`) : répondus 14, tronqués 2, en échec 0.
- Durées (`duree_s`, secondes, relevé), monde puis proposeur : 1 `argon` 96,004 ; 1 `astra` 80,106 ; 1 `fable52` 388,807 ; 1 `opus55` 109,396 ; 2 `argon` 38,287 ; 2 `astra` 61,164 ; 2 `fable52` 430,542 ; 2 `opus55` 54,737 ; 3 `argon` 75,664 ; 3 `astra` 78,847 ; 3 `fable52` 553,242 (tronqué) ; 3 `opus55` 72,991 ; 4 `argon` 47,464 ; 4 `astra` 34,411 ; 4 `fable52` 510,008 (tronqué) ; 4 `opus55` 36,425. Manifeste : `debut_utc` 2026-11-16T12:14:34+00:00, `fin_utc` 2026-11-16T12:59:07+00:00.
- Coûts : dépense rapprochée totale 15,378197 USD ; détail du registre des dépenses : `fable52` 10,019552 USD (4 appels : 2 complets, 2 tronqués), `opus55` 1,057336 USD (4 complets), `argon` 2,471620 USD (4 complets), `astra` 1,671750 USD (4 complets), machine 0,082018 USD (0,052222 USD/h).
- `corps.temoin_positif`, tel quel : `{"appels_portant_la_condition": 6, "appels_portant_une_autre_composante": 14, "n": 14, "sous_la_moitie": false}`.
- Information : les deux appels tronqués sont ceux de `fable52` aux mondes 3 et 4 (réponse illisible), 553 s et 510 s, soit 5,585992 USD des 10,019552 USD de ce proposeur.
"""

texte = SOURCE.read_text(encoding="utf-8")
remplacements = []   # (nom, ancien, nouveau)


def par_bornes(nom, debut, fin, nouveau):
    """Remplace le morceau qui va de `debut` (compris) à `fin` (exclu) ; chaque borne présente une fois."""
    assert texte.count(debut) == 1, f"{nom} : début"
    i = texte.index(debut)
    assert texte.count(fin, i) == 1 or texte[i:].count(fin) >= 1, f"{nom} : fin"
    j = texte.index(fin, i)
    remplacements.append((nom, texte[i:j], nouveau))


# ---------------------------------------------------------------------------------------------- titre, en-tête
remplacements.append(("titre", "(regroupement, sans juge) — brouillon 9\n",
                      "(regroupement, sans juge) — version qui fera foi v1\n"))

remplacements.append(("en-tete",
"""  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le 2026-11-16T15:31:06Z (`date -u`) ; aucun commit, aucune poussée
  (section « Contre-lecture »).
""",
f"""  aucun identifiant de modèle dans ce texte pour ce tour), écrit et scellé le 2026-11-16T15:31:06Z (`date -u`) ; aucun commit, aucune poussée
  (section « Contre-lecture »).
- **Version qui fera foi v1** : écrite par un rédacteur neuf du modèle A (lettre de R-2598 ; il n'a écrit ni le brouillon 1, ni
  les brouillons 2 à 9, ni aucun des neuf rapports, ni aucune pièce citée hors les quatre programmes de cette version ; aucun
  identifiant de modèle dans ce texte), le 2026-11-16 de 23:09 à {heure_fin} UTC (`date -u`), à partir du brouillon 9
  (`crible-v-brouillon9.md`, `{EMP_SOURCE}`, scellé comme pièce de travail, jugé scellable au tour 9) ; prédictions
  V1 à V6 gelées dans la rédaction du brouillon 9 par R-2993, **non changées** ; seuls changent, par les règles écrites
  du brouillon 9, les attendus du devis, la borne par appel B_a, la règle de M, le budget de durée, la garde de départ, la
  probabilité d'atteindre le minimum (information) et les mots de la ligne κv2 sur la tolérance de Pr-1 ; écarts listés un à
  un (section « Écarts au brouillon 9 ») ; différentiel `diff-crible-v-b-vers-foi-v1.txt` ; dépôt lu sur `main` (tête
  `fc727e80`) ; aucun commit, aucune poussée.
"""))

remplacements.append(("documents",
"R-2981, R-2982 (registre vivant) ;\n",
"""R-2981, R-2982, R-2993 (gel des prédictions avant toute lecture du pilote)
    et R-3005 (GO de Lazar sur le verdict du pilote ; devis des cribles à refaire) (registre vivant, `7889442a…` à la lecture) ;
  - section « Pour les cribles » du verdict du pilote MR-2 v14 (verdict `verdict-issue-pilote-mr2-v14-v2.md`,
    `e64458e82bae1d03e40656ad3b65456769eefd2603a7306e9a7d401eba8e1a3d`, branche `verdict/pilote-mr2-v74-v14-v1`, empreinte reprise
    de GO-2026-11-16-08, non vérifiée par moi) : **seule part du verdict lue**, transmise par la consigne de la mère (le verdict
    n'a pas été ouvert), recopiée à l'annexe A, point 13 — **[VERDICT-CRIBLES]** ; registre des dépenses `registres/depenses.md`,
    lignes 478 à 480 (montants du pilote ; base de prix : celle de la configuration ; `08aa7d16e225679031dfa6ff6f06a2d0a0b9b95e2db1f00de1613dbc78020e59`
    à la lecture) ;
"""))

# ---------------------------------------------------------------------------------------------- statut
par_bornes("statut", "**Statut.** Brouillon 9, **contre-lu huit fois**", "\n\n## 0. En dix lignes",
"""**Statut.** **Version qui fera foi v1**, écrite sur le brouillon 9, **contre-lu neuf fois** (tours 1 à 9 ; le tour 9 le juge
scellable sans correction, section « Contre-lecture ») ; **scellée ici comme pièce de travail** ; elle fera foi après le tour
différentiel que demande R-2993 (contrôle limité aux écarts de la section « Écarts au brouillon 9 »), son scellement par
`sceller_prereg` et sa copie sous `prereg/` (R1, R2). Aucune dépense, aucun appel de modèle, aucun monde tiré. L'accord de
dépense GO-2026-11-15-06 (enveloppe des cinq cribles : 247,20 USD attendus, 1 275 au pire, crédits de Claude employés au
maximum) **n'autorise encore aucun appel** : les lignes « calcul » κv1 et κv2 s'inscrivent par la mère sur ce devis refait et
contre-lu, citant ce mot (lecture de la mère, l. 339). **Ce qui a été lu du pilote MR-2 v14** (déclaré, consigne de la mère,
R-3005) : la seule section [VERDICT-CRIBLES] (comptes d'appels, durées par appel, heures du manifeste, coûts par proposeur et de
la machine, champ `corps.temoin_positif`, information sur les deux appels tronqués), recopiée à l'annexe A, point 13, et les
lignes 478 à 480 du registre des dépenses (base de prix des montants) ; rien d'autre (issue non ouverte). **Les prédictions V1
à V6 ont été gelées avant cette lecture** (R-2993, inscrit à 2026-11-16T15:33:25Z, avant le lancement du lecteur du pilote) et
ne changent pas : elles restent écrites sans aucune donnée du pilote ; V7, que R-2993 ne nomme pas, ne change pas non plus
(aucune règle ne la refait) ; le témoin positif est recopié à titre d'information et n'entre dans aucun chiffre. Le budget de
durée reste **« non lançable »** par sa règle écrite tant que quatre durées du journal d'états de la machine du pilote,
absentes de [VERDICT-CRIBLES], ne sont pas relevées (section « Devis »). Validateur `controle_ia.prereg.problemes` : aucun
défaut sur cette version (vérifié avant son scellement comme pièce de travail)."""
)

# ---------------------------------------------------------------------------------------------- en dix lignes
par_bornes("dix-lignes-8", "8. **Devis (brouillon, estimé)**", "9. **Durée** : ≈ 7 à 10 heures",
"""8. **Devis (refait sur les coûts mesurés du pilote MR-2, règle d'avance de la section « Devis »)** : **≈ 66,5 à 67,2 USD
   attendus** aux prix publics (proposeurs 66,21, dont 55,38 sur crédits de Claude et 10,83 hors crédits ; machine 0,16 à 0,89 ;
   sonde neuve 0,10) ; 76,10 pour les proposeurs au compte de la configuration (Pr-1 y est cinq fois plus cher) ; **196,60 au
   pire** à 20 mondes (100 sur crédits, 96,60 hors crédits) et **204,67** avec la sonde neuve exigée (κv1 104,39 sur crédits,
   κv2 100,28 hors crédits ; point 8 de « Choix et doutes », R-2992), inchangés (règle (a)) ; au-dessus des 183 de [NOTE]
   (+ 13,60 par les plafonds de 2,34 de Pr-1 et Pr-3 du bloc gelé de [PILOTE], + 8,07 par la sonde) ; enveloppe de
   GO-2026-11-15-06 : ce crible y tient seul (aucune ligne encore inscrite sous ce mot) et avec (iii) (474,67) ; les cinq
   ensemble non (≈ 1 323,67 contre 1 275) : nœud de Lazar au dernier crible (R-2992, point 3 ; section « Devis »).
""")

par_bornes("dix-lignes-9", "9. **Durée** : ≈ 7 à 10 heures", "10. **Nœuds**",
"""9. **Durée** (refaite sur le pilote) : **B_a = 900 s** par appel, donc par monde (les quatre appels d'un monde partent
   ensemble ; plus long appel répondu du pilote 430,542 s) ; appels au pire 20 × 900 s = 5 h à M = 1 ; **M = 1** si les durées
   de mise en place, de génération et de mesure de 20 mondes et de rapatriement, plus l'énumération du placebo (0,291 s), font
   au plus 12 400 s, M = 2 jusqu'à 15 400 s ; ces quatre durées ne sont pas dans la section lue du verdict : budget **« non
   lançable » tant qu'elles ne sont pas relevées** (règle écrite) ; garde de départ : 24 000 s + 3 D à M = 1 (section
   « Devis ») ; appels attendus ≈ 2 h 37 min ; le code est neuf, la date de lancement en dépend.
""")

# ---------------------------------------------------------------------------------------------- écarts au brouillon 9
remplacements.append(("ecarts-section", "\n## Hypothèse\n", f"""
## Écarts au brouillon 9 (version qui fera foi v1)

Texte de départ : `crible-v-brouillon9.md` (`{EMP_SOURCE}`), scellé comme pièce de travail le
2026-11-16T15:31:06Z, jugé scellable au tour 9 (`contre-lecture-crible-v-b7-tour3-v1.md`, `{E['cl9']}`).
Programme d'application : `appliquer-version-foi-crible-v-v1.py` (même dossier, empreinte dans son compagnon `.sha256`) :
il vérifie l'empreinte du brouillon 9 et des pièces recopiées, applique les remplacements nommés ci-dessous (chaque ancien
présent une seule fois, aucun chevauchement) et écrit une cible neuve ; différentiel complet : `diff-crible-v-b-vers-foi-v1.txt`.
**Écarts, un à un** :

1. Titre (« version qui fera foi v1 ») ; en-tête (ligne « Version qui fera foi v1 ») ; documents qui font foi ([VERDICT-CRIBLES],
   registre des dépenses l. 478 à 480, R-2993, R-3005) ; paragraphe « Statut » (ce qui a été lu du pilote, gel de V1 à V6).
2. Cette section.
3. « En dix lignes », points 8 (devis) et 9 (durée), refaits.
4. Section « Devis » : titre ; sous-section neuve « Devis refait sur le pilote MR-2 (fait foi) » : attendus et parts (règle
   (b)), pires cas et montants des lignes inchangés (règle (a)), règle (c), tolérance de la réflexion de Pr-1 non retenue (ligne
   « coût d'un appel »), B_a, table du budget, règle de M, garde de départ, machine attendue, enveloppe ; l'estimation du
   brouillon 9 est gardée sous un sous-titre qui dit qu'elle ne fait plus foi, les règles écrites d'avance qu'elle porte restant
   en vigueur.
5. Section « Taille » : probabilité d'atteindre le minimum refaite sur le taux du pilote (information).
6. « Lignes de GO proposées » : κv2, clause de la tolérance de Pr-1 (non retenue) ; montants inchangés.
7. Section « Contre-lecture » : tête (tours 1 à 9) ; entrée « Contre-lecture 9 ».
8. Annexe A : la phrase « À recopier en entier… » dite faite ; la phrase du point 11 sur la probabilité d'atteindre le minimum
   renvoie au point 13 ; points 13 ([VERDICT-CRIBLES] recopiée ; programmes et sorties du devis, du placebo et de la part de la moitié chère) et 14 (programmes
   `comptes_cribles_v2.py` et `compte_certifiees_mr2_v1.py` recopiés en entier, empreintes vérifiées) neufs.

**Inchangés** (le différentiel le montre) : H-v, H-v-a et les hypothèses de travail ; les prédictions **V1 à V7** (rédaction,
chiffres, zones, confiances ; V1 à V6 gelées par R-2993 ; V7, que R-2993 ne nomme pas, n'est refaite par aucune règle) ; la
faculté de l'étape 2 de refaire V1 et V6 après lecture du pilote **n'est pas employée** (R-2993) : V1 et V6 restent écrites
avant toute lecture du pilote ; ε, ε_strat, 0,8, la définition de copie ; la métrique ; N = 20, le minimum de 16, la définition
du monde complet, la table W_min ; les seuils ; les étages et leurs verdicts, l'ablation (étage 5) rapportée sans verdict
(R-2992, point 2) ; la liste d'arrêt entière, la ligne « coût d'un appel » comprise (tolérance non retenue : forme par défaut),
et la règle d'abandon d'un fournisseur reprise du pilote, gardée telle (R-2993) ; les graines ; la partie A ; les étapes ;
« Écarts, nœuds » ; antériorités ; « Choix et doutes » ; les plafonds, les pires cas et les montants des lignes de GO. III-7
est une prédiction du crible (iii) : sans objet ici.

**Mentions de rédacteur** (R-2992, point 0) : les 22 occurrences de « modèle C » du brouillon 9 relues une à une ; celles qui
désignent un rédacteur de corrections (en-tête, ligne « Brouillon 2 » ; entrées « Contre-lecture 1, 2, 4 et 5 ») portent déjà
« modèle A » et la correction de R-2992 ; les autres désignent des lecteurs (modèle C, juste) ; aucune mention fausse ne reste,
aucune ligne n'est changée à ce titre ; le rédacteur de cette version est du modèle A.

**Réserves de cette version** : (1) les durées de mise en place, de génération, de mesure et de rapatriement ne sont pas dans
[VERDICT-CRIBLES] : par la règle écrite, le budget est « non lançable », mot de la mère, tant qu'elles ne sont pas relevées sur
les états nommés (section « Devis ») ; la garde de départ reste sous forme littérale ; une version suivante, sous un nom neuf
(R12), écrira leurs valeurs ; (2) les états `pieces et arbre`, `secret`, `preparer` et `essai a blanc` de la machine ne tombent
dans aucun des cinq termes de la règle du budget, que les états consécutifs bornent : le budget ne les compte pas (règle gelée ;
point pour la mère) ; (3) le manifeste du run du pilote couvre 790,401 s de plus que la somme, sur ses quatre mondes, du plus
long appel de chaque monde ; ce temps n'est pas un terme de la règle (point pour la mère) ; (4) fourchette par appel non
refaite et plus grand rapport coût compté / plafond de Pr-1 non transmis : à lire sur la pièce de dépense du pilote
(`53c72308…`, R-2993) avant l'inscription des lignes ; un rapport au-dessus de 1 ferait refaire ce texte par la même règle ;
(5) énumération du placebo chronométrée par un programme de remplacement déclaré (0,291 s), le programme de mesure n'étant pas
écrit : à remesurer par lui à l'étape 0 ; (6) attendu de la sonde neuve (0,10 USD) non refait, aucune règle ne le visant ;
(7) Pr-4 tronqué dans 2 appels sur 4 au pilote (5,585992 USD des 10,019552 de ce proposeur) : un appel tronqué compte dans les
dollars et dans aucune couverture ; la sensibilité « mondes à quatre appels seulement » ne portera probablement que sur la
moitié environ des mondes (section « Taille ») ; (8) la phrase de la section « Seuil » qui lit S_R ≥ 0,25 en nombre de mondes
(« la moitié chère pèse 0,71 à 0,75 du coût ») repose sur les prix de [NOTE] ; aux moyennes du pilote, la moitié chère pèse
0,8828 de l'attendu des proposeurs aux prix publics (0,7681 au compte de la configuration), et S_R ≥ 0,25 revient à k_R ≤ 14
(k_R ≤ 13 au compte de la configuration) sous la même approximation (`part-chere-crible-v-foi-v1.py`, `{E['part']}`, sortie
`{E['part_sortie']}`, annexe A, point 13) ; information seulement : le seuil 0,25, l'étage 3 et la phrase gelée ne changent pas.

## Hypothèse
"""))

# ---------------------------------------------------------------------------------------------- devis
remplacements.append(("devis",
"## Devis (brouillon ; tout est estimé sauf les plafonds ; à refaire sur le coût mesuré du pilote)\n\n**Hypothèses de coût.**",
f"""## Devis (refait sur le coût mesuré du pilote MR-2 ; version qui fera foi)

### Devis refait sur le pilote MR-2 (fait foi)

**Lu et calculé.** Entrées : [VERDICT-CRIBLES] (comptes d'appels, durées, coûts ; annexe A, point 13) et le registre des
dépenses, l. 479 et 480, qui donne la base des montants : **prix de la configuration v12** (« prix de la configuration, la
console de Lazar fait foi », R-2803) ; au prix public, seul Pr-1 diffère (configuration 10 / 50, public 2 / 10 jusqu'au
30 novembre : rapport 5 à l'entrée comme à la sortie, donc à tout appel) ; Pr-2, Pr-3 et Pr-4 ont le même prix aux deux comptes
(table des proposeurs, section « Plan d'analyse »). Calcul : `devis-crible-v-foi-v1.py` (`{E['devis']}`) et sa sortie
`devis-crible-v-foi-v1-sortie.txt` (`{E['devis_sortie']}`), même dossier, lancés le 16 novembre à 23:16:46 UTC
(`date -u`, heure du fichier de sortie) par `nice -n 19 python3 -I` (Python 3.13.18, bibliothèque standard, fractions exactes) ;
énumération du placebo : `placebo-crible-v-chrono-v1.py` (`{E['placebo']}`) et sa sortie
(`{E['placebo_sortie']}`), même heure ; sorties recopiées à l'annexe A, point 13. Rapprochement (sortie, point 1) :
les quatre proposeurs et la machine font 15,302276 USD ; avec l'épreuve des clés (0,001164) et la machine de la tentative v13
(0,074757, registre des dépenses, l. 480), 15,378197, égal au total transmis.

**Attendus (règle (b) : moyenne des coûts de tous les appels du pilote, répondus ou tronqués, tels que facturés ; quatre appels
par proposeur)** et pires cas (règle (a), inchangés), USD :

| poste | crédits | appels du pilote (complets, tronqués, en échec) | coût mesuré des 4 appels (configuration) | attendu par appel : public (configuration) | attendu, 20 appels : public (configuration) | pire (plafonds × 20) |
|---|---|---|---|---|---|---|
| Pr-1 `argon` | hors | 4, 0, 0 | 2,471620 | 0,123581 (0,617905) | 2,47 (12,36) | 46,80 |
| Pr-2 `opus55` | Claude | 4, 0, 0 | 1,057336 | 0,264334 | 5,29 | 40,00 |
| Pr-3 `astra` | hors | 4, 0, 0 | 1,671750 | 0,417938 | 8,36 | 46,80 |
| Pr-4 `fable52` | Claude | 2, 2, 0 | 10,019552 | 2,504888 | 50,10 | 60,00 |
| machine (0,052222 USD/h, relu au pilote) | hors | — | 0,082018 | — | 0,16 à 0,89 (ci-dessous) | 3,00 |
| **crédits de Claude** (Pr-2, Pr-4) | | 8 | 11,076888 | | **55,38** (55,38) | **100,00** |
| **hors crédits** (Pr-1, Pr-3, machine) | | 8 | 4,225388 | | **10,83** (20,72), plus la machine | **96,60** |
| **total** | | 16 | 15,302276 | | **66,21** (76,10), plus la machine | **196,60** |
| sonde neuve (exigée, R-2992) | les deux | — | — | — | 0,10 (attendu du brouillon, aucune règle ne le refait) | 8,07 (κv1 + 4,39 ; κv2 + 3,68) |
| **lignes de GO** | | | | | | **κv1 104,39 ; κv2 100,28 ; 204,67** |

Attendu total : **≈ 66,5 à 67,2 USD** aux prix publics (principal, R-2977 : proposeurs 66,21, machine 0,16 à 0,89, sonde 0,10) ;
≈ 76,4 à 77,1 au compte de la configuration. Part sur crédits de Claude : 0,84 de l'attendu des proposeurs aux prix publics,
0,73 au compte de la configuration, 0,51 du pire cas (104,39 / 204,67) ; 100 % de ce que la configuration v12 permet pour ce
dessin (point 3 de « Choix et doutes »). Contre l'estimation du brouillon 9 (73,30 selon [NOTE] ; fourchette 79,95 à 92,75) :
l'attendu mesuré est plus bas ; Pr-4 en porte 0,76 (50,10 / 66,21).

**Fourchette (règle (b), plus petit et plus grand coût d'un appel)** : **non refaite** : [VERDICT-CRIBLES] ne donne que les
totaux par proposeur (pour Pr-4 : 5,585992 USD pour ses deux appels tronqués, 4,433560 pour les deux complets, moyennes 2,792996
et 2,216780) ; le plus petit coût d'un appel est au plus la moyenne, le plus grand au moins (réserve (4) de la section « Écarts
au brouillon 9 »).

**Règle (c)** : aucun coût mesuré au-dessus d'un plafond de session n'est visible dans [VERDICT-CRIBLES] : moyennes par appel de
0,26 (Pr-1, compte de la configuration, 0,617905 / 2,34), 0,13 (Pr-2), 0,18 (Pr-3) et 0,83 (Pr-4) du plafond ; les deux appels
tronqués de Pr-4 font 0,93 de son plafond en moyenne (2,792996 / 3,00) ; coûts par appel non transmis.

**Tolérance de la réflexion de Pr-1 (ligne « coût d'un appel » de la liste d'arrêt)** : **non retenue**. Elle n'existe que si
le plus grand rapport coût compté / plafond (2,34) mesuré sur les appels de Pr-1 du pilote dépasse 1 ; aucun dépassement n'est
observé : rapport moyen 0,2641 ; pour qu'un seul appel dépasse 2,34, les trois autres devraient coûter ensemble au plus
0,131620 USD (sortie, point 8) ; le rapport par appel n'est pas transmis. La ligne d'arrêt garde sa forme par défaut (« tout
dépassement du pire cas d'un appel arrête (code 3) »), sans essai de plus ; κv2 le dit (section « Lignes de GO proposées »).

**Borne par appel et par monde (règle de B_a)** : plus long appel **répondu** du pilote : Pr-4 au monde 2, 430,542 s ;
1,5 × 430,542 = 645,813 s ; **B_a = 900 s** (plus petit multiple de 300 s au moins égal, sous 3 600 s ; sortie, point 4). Les
quatre appels d'un monde partant ensemble, la part des appels d'un monde est bornée par B_a : **900 s par monde** (par file de
M mondes). Aucun appel du pilote ne dépasse 900 s (le plus long, tronqué, 553,242 s) : le taux lu avec cette B_a est celui des
comptes (section « Taille »).

**Budget de pire cas et M (règle de la section « Devis », « Durée »)** : budget = 6 000 s de barrières + 3 × (mise en place +
génération de 20 mondes + mesure de 20 mondes + rapatriement) + 3 × énumération du placebo + ⌈20/M⌉ × B_a, au plus 61 200 s
(17 h). Énumération du placebo, pire cas (n_c = 20, k_R = 10, 184 756 ensembles) : **0,291 s** (le plus long de deux lancements ;
programme de remplacement déclaré, réserve (5)). **Les quatre autres durées ne sont pas dans [VERDICT-CRIBLES]** ; par la règle
écrite (point (8) des « Points à remesurer »), une durée sans état qui la borne n'est pas relevée et le budget est **« non
lançable », mot de la mère**, tant qu'elles ne le sont pas. **États nommés** (`etape=` du journal `etat.txt` de la machine du
pilote, [PROC-14] § 0 ; deux états consécutifs) : mise en place, de `mise en place` à `pieces et arbre` ; génération, de `mondes`
à `attente du feu 2 (mondes)`, rapportée à 20 mondes (cinq fois la durée des 4 mondes du pilote) ; mesure, de `mesure` à
`rapatriement`, rapportée à 20 mondes de même ; rapatriement, de `rapatriement` à `fini`. Avec D = somme de ces quatre durées
(génération et mesure rapportées à 20 mondes) et de l'énumération, plus grande valeur de D qui tient sous 17 h (D_max ; sortie,
point 6) :

| B_a | M = 1 : appels ; D_max | M = 2 : appels ; D_max |
|---|---|---|
| **900 s (règle)** | 18 000 s ; **12 400 s (3,444 h)** | 9 000 s ; 15 400 s (4,278 h) |
| 1 800 s | 36 000 s ; 6 400 s (1,778 h) | 18 000 s ; 12 400 s (3,444 h) |
| 2 400 s | 48 000 s ; 2 400 s (0,667 h) | 24 000 s ; 10 400 s (2,889 h) |
| 3 000 s | 60 000 s ; non lançable | 30 000 s ; 8 400 s (2,333 h) |
| 3 600 s | 72 000 s ; non lançable | 36 000 s ; 6 400 s (1,778 h) |

**Règle de M, sur B_a = 900 s** : M = 1 si D ≤ 12 400 s ; M = 2 si 12 400 s < D ≤ 15 400 s ; « non lançable » et mot de la
mère si D > 15 400 s ou si l'une des quatre durées n'est pas relevée. **Garde de départ** (ligne « minuterie de la machine » de
la liste d'arrêt) : arrêt (A) sans appel si le temps restant avant l'échéance de la minuterie est inférieur au budget de pire
cas, soit **24 000 s + 3 D à M = 1** (barrières 6 000 s et appels 18 000 s) ou **15 000 s + 3 D à M = 2** ; sa valeur en
secondes s'écrit avec D.

**Machine dans l'attendu (règle (b))** : moyenne, sur les quatre mondes du pilote, du plus long des quatre appels (388,807 ;
430,542 ; 553,242 ; 510,008 s ; aucun au-delà de B_a) : 470,650 s ; appels attendus 20 × 470,650 = 9 413 s à M = 1 (4 706 s à
M = 2) ; avec les barrières, 4,28 h à M = 1, soit 0,224 USD à 0,052222 USD/h (0,155 à M = 2) ; les quatre durées non relevées
s'y ajoutent, sans le facteur trois ; le budget borne le tout à 17 h, soit 0,888 USD : **machine attendue entre 0,16 et 0,89
USD** (sortie, point 7) ; pire cas inchangé, 3,00 (règle (a)). **Durée attendue** (information) : appels ≈ 2 h 37 min à M = 1,
barrières 1 h 40 min, plus les quatre durées non relevées. Le manifeste du run du pilote couvre 2 673 s (12:14:34 à 12:59:07),
790,401 s de plus que la somme, sur les quatre mondes, du plus long appel de chaque monde (1 882,599 s) ; ce temps, de nature
non dite dans [VERDICT-CRIBLES], n'est pas un terme de la règle du budget (réserve (3)).

**Enveloppe de GO-2026-11-15-06** (1 275 USD au pire, échéance 2026-11-30 ; sortie, point 9) : aucune ligne « calcul » n'est
encore inscrite sous ce mot (`registres/go.md`, `029cc2e2…` à la lecture : la ligne 339 seule le cite) et aucune dépense n'y
est portée (`registres/depenses.md`) : **ce crible y tient seul** (204,67) ; avec le crible (iii) tel que son brouillon 8 le
chiffre (`crible-iii-brouillon8.md`, `d3406878…` : 263 au pire et 7 de sonde des gabarits ; 270 aussi dans sa version qui fera
foi v1 en cours, `crible-iii-version-foi-v1.md`, `91b4bf30…` à la lecture), 474,67 : **tient** ; avec (i), (ii) et (iv) aux
pires de [NOTE] (123, 483 et 243, plafonds de 2,00 non refaits), 1 323,67 : **ne tient pas** (48,67 de trop) ; par R-2992
(point 3), la ligne du crible qui ne tiendrait pas sous 1 275 est un nœud de Lazar. Les lignes κv1 et κv2 ne s'inscrivent que
si le cumul des lignes déjà inscrites, elles comprises, reste sous 1 275 USD.

### Estimation du brouillon 9 et règles écrites d'avance (l'estimation ne fait plus foi ; les règles s'appliquent, ci-dessus)

**Hypothèses de coût.**"""))

# ---------------------------------------------------------------------------------------------- taille
remplacements.append(("taille",
"La version qui fera foi refait ce compte sur les taux du pilote à titre d'information ;",
"""**Refait sur le taux du pilote** (version qui fera foi, à titre d'information ; sortie du devis, point 5) : 14 appels répondus,
2 tronqués, 0 en échec sur 16, aucun au-delà de B_a = 900 s, soit r = 0,875 : P(monde complet) = 0,9690, P(n_c ≥ 16 sur 20) =
0,9997, P(monde à quatre appels) = 0,5862 ; aux taux par proposeur (quatre appels chacun ; Pr-4 à 1/2, les trois autres à 1) :
P(n_c ≥ 16 sur 20) = 1,0000 (arrondi) et P(monde à quatre appels) = 0,5000 ; mêmes réserves que la grille (appels
indépendants, abandon d'un fournisseur après une panne de relais non compté), et la sensibilité « mondes à quatre appels
seulement » ne portera probablement que sur la moitié environ des mondes ;"""))

# ---------------------------------------------------------------------------------------------- ligne κv2
remplacements.append(("go-kv2",
"mêmes conditions que la ligne κv1, sauf « coût au-dessus du pire cas = arrêt », qui reçoit pour Pr-1 la tolérance de la réflexion si la règle de la ligne « coût d'un appel » de la liste d'arrêt la retient |",
"mêmes conditions que la ligne κv1, « coût au-dessus du pire cas = arrêt » compris, sans exception (tolérance de la réflexion de Pr-1 non retenue par la règle de la ligne « coût d'un appel » de la liste d'arrêt : aucun dépassement du plafond observé au pilote) |"))

# ---------------------------------------------------------------------------------------------- contre-lecture
remplacements.append(("contre-lecture-tete",
"Tours 1 à 8 faits (entrées « Contre-lecture 1 » à « Contre-lecture 8 » ci-dessous)",
"Tours 1 à 9 faits (entrées « Contre-lecture 1 » à « Contre-lecture 9 » ci-dessous)"))

remplacements.append(("contre-lecture-9",
"    `appliquer-corrections-crible-v-brouillon9.py`, la ligne R-2992 de `registres/decisions.md`, [PILOTE] (liste d'arrêt,\n    « Panne d'un relais »).\n\n## Annexe A",
f"""    `appliquer-corrections-crible-v-brouillon9.py`, la ligne R-2992 de `registres/decisions.md`, [PILOTE] (liste d'arrêt,
    « Panne d'un relais »).

- **Contre-lecture 9** (tour 9, sur le brouillon 9 ; tour 3 de la boucle B7) : sous-agent neuf du modèle C (lettre de son
  rapport), qui n'a écrit aucune pièce citée ; lecture de 15:31Z à 15:33Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-b7-tour3-v1.md`, empreinte
  `{E['cl9']}` (égale à son compagnon) ; brouillon relu : `crible-v-brouillon9.md`, empreinte
  `{EMP_SOURCE}`. Verdict : **scellable** ; aucune correction exigée, aucune remarque facultative
  nouvelle ; application du tour 8 jugée fidèle (8 zones du `diff`) ; validateur sans défaut.
  - **Suite** : prédictions V1 à V6 gelées dans la rédaction du brouillon 9 par la mère (R-2993, 15:33:25Z), avant le
    lancement du lecteur du pilote ; version qui fera foi v1 écrite par un rédacteur neuf du modèle A (R-2982, R-2992 point 0)
    par les règles écrites du brouillon 9, après la lecture de la seule section [VERDICT-CRIBLES] (R-3005) ; écarts listés dans
    la section « Écarts au brouillon 9 » ; différentiel `diff-crible-v-b-vers-foi-v1.txt`.
  - « Points pour la mère » 1 à 3 du rapport : (1) règle d'abandon d'un fournisseur : gardée telle (R-2993) ; (2) enveloppe :
    refaite (section « Devis ») ; (3) scellement : cette version passe un tour différentiel (R-2993) avant `sceller_prereg` et
    sa copie sous `prereg/`.
  - **Contrôle suivant** (tour différentiel, R-2993) : lecteur neuf, d'un autre modèle que le rédacteur, qui n'a écrit ni ce
    texte, ni ses brouillons, ni aucun rapport, ni les programmes de cette version. **Fichiers à lui donner** : ce texte ; le
    brouillon 9 ; `diff-crible-v-b-vers-foi-v1.txt` ; `appliquer-version-foi-crible-v-v1.py` ; `devis-crible-v-foi-v1.py` et
    sa sortie ; `placebo-crible-v-chrono-v1.py` et sa sortie ; les lignes R-2977, R-2992, R-2993 et R-3005 de
    `registres/decisions.md` ; la ligne GO-2026-11-15-06 de `registres/go.md` ; les lignes 478 à 480 de `registres/depenses.md` ;
    [PROC-14] § 0 (états de la machine) ; jamais le verdict du pilote au-delà de [VERDICT-CRIBLES].

## Annexe A"""))

# ---------------------------------------------------------------------------------------------- annexe
remplacements.append(("annexe-recopie",
"**À recopier en entier dans la version qui fera foi de ce texte (le brouillon (iii) sera remplacé), avec les calculs de C-02 et C-05.**",
"**Recopié en entier à l'annexe A, point 14, de la version qui fera foi ; les calculs de C-02 et C-05 sont aux points 11 et 12.**"))

remplacements.append(("annexe-11",
"la probabilité d'atteindre le minimum sur le taux mesuré du\npilote reste à calculer par programme dans la version qui fera foi (section « Taille »).",
"la probabilité d'atteindre le minimum sur le taux mesuré du\npilote est calculée au point 13 (version qui fera foi ; section « Taille »)."))

remplacements.append(("annexe-13-14", "\n## Citations obligatoires", f"""
**Point 13 — pilote MR-2 v14 : section lue et calculs de la version qui fera foi.** [VERDICT-CRIBLES], recopiée telle que la
consigne de la mère la transmet (seule part du verdict lue ; « tel quel » pour le témoin positif) :

```
{VERDICT_CRIBLES}```

Programmes `devis-crible-v-foi-v1.py` (`{E['devis']}`) et `placebo-crible-v-chrono-v1.py`
(`{E['placebo']}`), même dossier, déposés avec leurs compagnons `.sha256` ; lancés le 16 novembre
à 23:16:46 UTC (heure des fichiers de sortie, `date -u`) par `nice -n 19 python3 -I` (Python 3.13.18, bibliothèque standard ;
machine de développement à 4 processeurs) ; aucune donnée lue par eux (entrées recopiées à la main de [VERDICT-CRIBLES] et du
registre des dépenses, l. 478 à 480), aucun tirage, aucun appel. Sortie du devis (`{E['devis_sortie']}`), recopiée :

```
{sortie_devis}```

Sortie du chronométrage du placebo (`{E['placebo_sortie']}`), recopiée (mondes simulés par une formule fixe ; seul le temps
compte) :

```
{sortie_placebo}```

Programme `part-chere-crible-v-foi-v1.py` (`{E['part']}`), même dossier, lancé le 16 novembre à 23:24:53 UTC
(`date -u`) de même ; sortie (`{E['part_sortie']}`), recopiée (information, réserve (8) de la section « Écarts au
brouillon 9 ») :

```
{sortie_part}```

**Point 14 — programmes de l'annexe A recopiés en entier** (le brouillon 9 le demandait à la version qui fera foi). Tirés des
blocs de code de `crible-iii-brouillon1.md` (`00c92559d54349101dfcc0c59afe402c388b192c32fa6018bbf809eb02f22af0`) par le
programme d'application de cette version, qui en recalcule les empreintes : égales à celles que l'annexe cite. Programme
`comptes_cribles_v2.py` (`{P_COMPTES}`) :

```python
{prog[P_COMPTES]}```

Sa sortie (`{S_COMPTES}`) est celle dont les points utiles sont recopiés en tête de cette annexe ; elle est recopiée en
entier à l'annexe A de `crible-iii-brouillon1.md`. Programme `compte_certifiees_mr2_v1.py` (`{P_CERT}`) :

```python
{prog[P_CERT]}```

## Citations obligatoires"""))

# ---------------------------------------------------------------------------------------------- application
positions = []
for nom, ancien, nouveau in remplacements:
    n = texte.count(ancien)
    assert n == 1, f"{nom} : ancien présent {n} fois"
    i = texte.index(ancien)
    positions.append((i, i + len(ancien), nom, nouveau))
positions.sort()
for (a, b, n1, _), (c, d, n2, _) in zip(positions, positions[1:]):
    assert b <= c, f"chevauchement {n1} / {n2}"
sortie, k = [], 0
for a, b, nom, nouveau in positions:
    sortie.append(texte[k:a])
    sortie.append(nouveau)
    k = b
sortie.append(texte[k:])
neuf = "".join(sortie)
for nom, _, nouveau in remplacements:
    assert neuf.count(nouveau) == 1, f"{nom} : nouveau non unique"
with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(neuf)
print(f"{len(remplacements)} remplacements appliqués ; cible {CIBLE.name} ; {hashlib.sha256(neuf.encode()).hexdigest()}")
for _, _, nom, _ in positions:
    print("  ", nom)
