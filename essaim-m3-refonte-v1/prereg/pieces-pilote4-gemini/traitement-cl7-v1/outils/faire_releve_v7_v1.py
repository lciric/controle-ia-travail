"""Construit le relevé v7 des mots de Lazar à partir de la v6, mot pour mot : titre et phrase d'en-tête mis à jour, six
lignes ajoutées à la fin de la table (03:01 à 03:48), en-tête de la section session-depot citant aussi `162418c`, et les
lignes R-479 à R-484 ajoutées à la fin. Aucune ligne de la v6 n'est ôtée ni changée hors des trois endroits nommés.
Usage : python -I faire_releve_v7_v1.py RELEVE_V6 RELEVE_V7 (refuse d'écraser ; vérifie l'empreinte de la v6)."""
import hashlib, pathlib, sys

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if dst.exists():
    sys.exit(f"refus : {dst} existe déjà (R12)")
texte = src.read_text(encoding="utf-8")
h6 = hashlib.sha256(src.read_bytes()).hexdigest()
assert h6 == "2e6387b912f1c5d3c2c3cff053656df1e37eb1895dfa54197030445171d13914", h6

def remplacer(t, ancien, nouveau):
    assert t.count(ancien) == 1, ancien[:60]
    return t.replace(ancien, nouveau)

texte = remplacer(texte, "(relevé verbatim) — v6", "(relevé verbatim) — v7")
texte = remplacer(texte, "relevées par l'instance nouvelle de conv-audit le 26 octobre à partir de 02:10 UTC. Ce relevé sert de pièce",
                  "relevées par l'instance nouvelle de conv-audit le 26 octobre à partir de 02:10 UTC. La v7 reprend la v6 "
                  "(`2e6387b9…`) mot pour mot et ajoute les messages de 03:01 à 03:48 (03:01 dans la session sortante, cité par "
                  "sa passation v2 ; les suivants dans la session de l'instance nouvelle) et, à part, les lignes R-479 à R-484 "
                  "du registre de session-depot (`main`, `162418c`), relevées le 26 octobre à partir de 02:58 UTC. Ce relevé "
                  "sert de pièce")

lignes = (
    "| 03:01 (session sortante, cité par la passation v2, § en-tête) | « Toujours en attente de toi : les graines de plus pour "
    "le pilote 4 (question de 02:05). C’est aussi une dépense, sans défaut. :transmets aussi cette question dans la "
    "passation » | passation v2 de la lignée (`f6136738…`, § 5 bis : la question des graines, complète, à reposer à Lazar, "
    "avec le calcul de l'écart minimal selon le nombre de graines) |\n"
    "| 03:27 | « Décision en attente, sans défaut (dépense) : graines de plus pour le pilote 4 — (a) trois par objet, "
    "recommandée ; (b) cinq ; (c) une course par objet : demande au collisionneur 3 tours » | question au collisionneur "
    "`question-graines-pilote4-collisionneur-v1.md` (`6f8c507f…`, canal `9d6d91e`), dépense soumise à son mot chez "
    "session-depot ; la décision des graines reste pendante ; conv-audit ne lit aucun score de ce pilote d'ici là |\n"
    "| 03:33 | « lis cette page : [Neural Networks Are Already Clean](https://already-clean.goodfire.com/) peut on s'en servir "
    "pour notre programme ai control; pour le brainstorm de notre organsome sur eval awareness et maieutique ? brainqtoirm "
    "et lance aussi le collisioonneur 3 tours dessus » | lecture et remue-méninges par conv-audit sur le canal (`d5546aa`) ; "
    "question au collisionneur `question-already-clean-collisionneur-v1.md` (`252f4922…`), partie sur le mot de Lazar chez "
    "session-depot (R-483) ; sans effet sur le texte du pilote 4 |\n"
    "| 03:43 | « que reste t il avant de lancer le pilote 4 ? » | réponse de conv-audit : rapport de la contre-lecture 7, "
    "traitement, graines et empreintes, vérification, poussée, message de départ ; session-depot lance |\n"
    "| 03:46 | « on a dit plus de scellement et de prereg tant qu'on est dans la phase de conception !!! » | ni "
    "préenregistrement ni scellement au sens de R1 pour ce pilote ; le script `sceller_pilote4_v4.py` ne fait qu'écrire "
    "l'entropie, les graines et les empreintes que le lanceur v10 exige ; décision soumise : attendre ou non la "
    "contre-lecture 7 |\n"
    "| 03:48 | « (1) Attendre la 7 (elle a fini le `diff` et les contrôles ; le rapport s’écrit : quelques minutes à un "
    "quart d’heure). Avantage : un seul texte, relu en entier. Inconvénient : le délai. » | (1) retenue : départ après le "
    "rapport de la contre-lecture 7 et le traitement de ses constats |\n"
)
ancre = "\n\n## Mots de Lazar dans la session de session-depot, tels que son registre les recopie"
assert texte.count(ancre) == 1
texte = texte.replace(ancre, "\n" + lignes + ancre)
texte = remplacer(texte, "R-473 à R-478 sur `681af80`)", "R-473 à R-478 sur `681af80`, R-479 à R-484 sur `162418c`)")

ajout = """
- **R-479** (26 octobre, ligne écrite à 02:05 UTC) : reprise de session-depot par l'instance que désignent la passation n° 12
  et son complément ; clés vues dans cette session (noms seulement) ; demande de Lazar dans cette session d'une course de
  l'organisme sur une question de programme destinée à une candidature (P-030 ; la question n'est pas versée, elle est
  confidentielle) ; recopié ici sans ses mots, qui touchent cette candidature.
- **R-480** (02:06 UTC) : correction de R-479 : le tour « littérature des boucles » n'est pas perdu (versé, `4b20fb4`).
- **R-481** (« vers 02:09 UTC ») : « il y a plusieurs cles anthropic utilise luc », puis « je viesn de la verser » : clé des
  courses `RR_ANTHROPIC_API_KEY_LUC` ; la clé `RR_ANTHROPIC_API_KEY` refuse toute requête sans l'en-tête
  `anthropic-workspace-id` (collisionneur v2.6, qui l'envoie quand il est défini).
- **R-482** (« vers 02:25 UTC ») : « (b) La même question au collisionneur d’abord (≈ 8 USD, 40 minutes), l’organisme
  ensuite. : go » (P-030 ; GO-2026-10-26-02 et -03) ; la session redémarrée voit `RR_ANTHROPIC_API_KEY_LUC`,
  `GEMINI_API_KEY_2`, `OPENALEX_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY` et `BRAVE_API_KEY` ; le tour « neuron explorer » part.
- **R-483** (« vers 02:41 UTC ») : « Mot direct de Lazar, go dépense. Tour du collisionneur sur la question de conv-audit
  question-already-clean-collisionneur-v1.md (canal/conv-audit-n04, commit d5546aa, empreinte 252f4922…) : étage III, trois
  tours, trois modèles, une tentative par cellule, règles R-468 et R-470 sur les refus ; plafond 10 USD, sous
  GO-2026-10-24-07 s’il court encore, sinon une ligne de GO nouvelle ; branche donnees/collisionneur-already-clean-v1 ;
  jamais servi à un organisme. »
- **R-484** (02:46 UTC) : refus d'Opus au III.1 du tour sur la question de P-030 ; aucune question reformulée (borne (5) de
  R-468) ; la course de l'organisme sur cette question est suspendue jusqu'à la décision de Lazar.
"""
texte = texte.rstrip("\n") + "\n" + ajout
dst.write_text(texte, encoding="utf-8")
h7 = hashlib.sha256(dst.read_bytes()).hexdigest()
pathlib.Path(str(dst) + ".sha256").write_text(f"{h7}  {dst.name}\n", encoding="utf-8")
print(f"v7 écrite : {dst.name} {h7}")
