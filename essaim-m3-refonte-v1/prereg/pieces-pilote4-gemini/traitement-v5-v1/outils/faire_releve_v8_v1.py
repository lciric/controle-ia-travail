"""Construit le relevé v8 des mots de Lazar à partir de la v7, mot pour mot : titre et phrase d'en-tête mis à jour, sept
lignes ajoutées à la fin de la table (04:29 à 05:13 Paris), en-tête de la section session-depot citant aussi `f52a75d`, et
les lignes R-485 à R-492 ajoutées à la fin. Aucune ligne de la v7 n'est ôtée ni changée hors des trois endroits nommés.
Usage : python -I faire_releve_v8_v1.py RELEVE_V7 RELEVE_V8 (refuse d'écraser ; vérifie l'empreinte de la v7)."""
import hashlib, pathlib, sys

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
if dst.exists():
    sys.exit(f"refus : {dst} existe déjà (R12)")
texte = src.read_text(encoding="utf-8")
h7 = hashlib.sha256(src.read_bytes()).hexdigest()
assert h7 == "a99eb30607fee9b13a7cd35e1bf5ce69d7f24352122ff72da39f2eb21f3f0234", h7

def remplacer(t, ancien, nouveau):
    assert t.count(ancien) == 1, ancien[:60]
    return t.replace(ancien, nouveau)

texte = remplacer(texte, "(relevé verbatim) — v7", "(relevé verbatim) — v8")
texte = remplacer(texte, "relevées le 26 octobre à partir de 02:58 UTC. Ce relevé sert de pièce",
                  "relevées le 26 octobre à partir de 02:58 UTC. La v8 reprend la v7 (`a99eb306…`) mot pour mot et "
                  "ajoute les messages de 04:29 à 05:13 Paris (session de l'instance nouvelle de conv-audit) et, à part, les lignes "
                  "R-485 à R-492 du registre de session-depot (`main`, `f52a75d`), relevées le 26 octobre à partir de 04:27 UTC. "
                  "Ce relevé sert de pièce")

lignes = (
    "| 04:29 | « le pilote est pret ? » | réponse de conv-audit : oui de son côté ; la suite est chez session-depot (lignes "
    "de GO et de dépense, copie, test de dépense, segment 1) |\n"
    "| 04:31 | fichier joint : l'échange de session-depot avec Lazar sur la course de l'organisme sur la question « programme "
    "TAIF » (R-486, R-487 : refus de contourner un refus de sûreté, reformulation non écrite) | conv-audit ne reformule pas "
    "non plus ; aucun mot de ce fichier n'est recopié ici (question confidentielle) |\n"
    "| 04:47 | « la methode poutr trouver un neurone dans already clean est elle detaillee ici ? "
    "https://already-clean.goodfire.com/neuron-scientist/moe/L32_E134_N510/#ablation-kinds » | lecture de la page par "
    "conv-audit (`envois/already-clean-neurone-L32-E134-N510-v1/`) ; synthèse « already clean » v2 ; sans effet sur ce "
    "pilote |\n"
    "| 04:48 | « One choice is still yours: the extra seeds. The collider run can no longer go before the first segment, "
    "since it uses the same key as the pilot : lance le collisionneur now » puis « un iu deux tours » | question des "
    "graines v2 (`79336386…`, canal `c9c8575`) ; phrase donnée à Lazar pour session-depot ; mot écrit chez elle vers "
    "04:05 UTC (R-491) : deux tours, 8 USD, entre les deux courses |\n"
    "| 05:06 | « Nos organismes réutilisent un jeu de test en s’adaptant à lui. Se réécrire à partir du score de `test` "
    "(36 tâches) fait monter ce score par simple sélection, sans aucune compétence : c’est l’attaque décrite dans "
    "« Ladder ». Et c’est justement sur les petits jeux de test que ce sur-ajustement a été observé. : comment eviter "
    "cela ? » | réponse de conv-audit : mesurer (écart test − test_final), borner la fuite, tâches fraîches, tenir la "
    "boucle extérieure ; décision soumise sur la lecture de test_final |\n"
    "| 05:13 | « Des tâches fraîches (la seule chose qui marche vraiment). […] Et la confrontation reste sur la v6 scellée, "
    "famille tenue à l’écart, déjà décidé. : go » et « Options : (a) `test` dès la fin de chaque course, `test_final` "
    "une fois en fin de boucle : ok » (verbatim complet : note `envois/decision-N-taches-fraiches-et-lecture-test-final-v1.md`, "
    "`4b23e00f…`) | N-049 et N-050 proposés : vivier par génération dès le pilote 5, banque sœur v3-bis sur devis, "
    "test_final lu une seule fois en fin de boucle ; effet sur ce texte : § Plan, point 3 |\n"
)
ancre = "\n\n## Mots de Lazar dans la session de session-depot, tels que son registre les recopie"
assert texte.count(ancre) == 1
texte = texte.replace(ancre, "\n" + lignes + ancre)
texte = remplacer(texte, "R-479 à R-484 sur `162418c`)", "R-479 à R-484 sur `162418c`, R-485 à R-492 sur `f52a75d`)")

ajout = """
- **R-485** (26 octobre, 02:50 UTC) : refus de Fable et d'Opus au III.2 du tour « programme TAIF » ; III.3 entre les réponses
  valides ; correction de R-484 sur la façon dont l'organisme pose la question.
- **R-486** (vers 03:26 UTC) : mot de Lazar « on le fait » sur la course de l'organisme sur la question « programme TAIF » :
  **non exécuté** (contournement d'un refus de sûreté ; consigne gelée) ; GO-2026-10-26-03 inutilisé.
- **R-487** (vers 03:31 UTC) : demande de reformulation « conceptuelle, mathématique et technique » : **non exécutée** (même
  motif).
- **R-488** (03:36 UTC) : départ du pilote 4 : ligne d'extension de GO-2026-10-25-02 et dépense de la v6.2.1 inscrites mot
  pour mot d'après le n° 71 ; préparatifs (course M de référence, Python du gel, clé LUC sans en-tête, tours finis).
- **R-489** (03:43 UTC) : tentative 1 de la v6.2.1 refusée avant le manifeste (essai du noyau `test_sources_reelles_de_moisson_si_reseau`
  en échec sur un 429 d'arXiv) ; 0,0015 USD ; une seule tentative 2 quand arXiv répond.
- **R-490** (03:51 UTC) : tentative 2 : 169 essais sur 169 ; **la v6.2.1 (question M) est partie à 03:51:14 UTC**, PID 14184,
  minuteur 14185, échéance 04:43:40 ; dossier `pilote4-gemini-v6-2-v1-tentative2` ; aucun score lu.
- **R-491** (04:06 UTC) : mot direct de Lazar (vers 04:05 UTC) : tour du collisionneur sur la question des graines v2
  (`c9c8575`, `79336386…`), deux tours, 8 USD, branche `donnees/collisionneur-graines-pilote4-v1`, **entre les deux
  courses** ; outil `deux_tours_etage3_v1.py` qui limite l'étage III à E3-T1 et E3-T2.
- **R-492** (04:15 UTC) : mot direct de Lazar (vers 04:13 UTC, verbatim : « pas besoin de faire v5.3, en revanche ppose la
  question de la structure de l'organsime S ») : **la v5.3 ne court pas ; la seconde course est la v6.2.1 sur la question
  S** (`a54da93e…`, commit `4772b525`), mêmes bornes, après la course M et le tour des graines, dans l'enveloppe du
  pilote 4 ; texte et lanceur nouveaux demandés à conv-audit (n° 64) ; la partie v5.3 de l'extension de R-488 reste
  inutilisée.
"""
texte = texte.rstrip("\n") + "\n" + ajout
dst.write_text(texte, encoding="utf-8")
print(f"relevé v8 écrit : {dst.name} {hashlib.sha256(dst.read_bytes()).hexdigest()}")
