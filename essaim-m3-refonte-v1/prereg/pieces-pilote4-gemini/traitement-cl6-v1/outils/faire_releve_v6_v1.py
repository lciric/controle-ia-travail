"""Construit le relevé v6 des mots de Lazar à partir de la v5, mot pour mot : titre et phrase d'en-tête mis à jour, trois lignes
ajoutées à la fin de la table (02:32, 02:34, 02:42), en-tête de la section session-depot citant les deux commits, et les
lignes R-473 à R-478 ajoutées à la fin. Aucune ligne de la v5 n'est ôtée ni changée hors des deux endroits nommés."""
import hashlib, pathlib, sys

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
if dst.exists():
    sys.exit(f"refus : {dst} existe déjà (R12)")
texte = src.read_text(encoding="utf-8")
h5 = hashlib.sha256(src.read_bytes()).hexdigest()
assert h5 == "c5fe20921285a7992f4236c867e981b13b7a55c47122be1afe16ad989a4c32c8", h5

titre_v5 = "# Mots de Lazar dans la session de conv-audit, 25 et 26 octobre 2026 (relevé verbatim) — v5"
titre_v6 = "# Mots de Lazar dans la session de conv-audit, 25 et 26 octobre 2026 (relevé verbatim) — v6"
assert texte.count(titre_v5) == 1
texte = texte.replace(titre_v5, titre_v6)

phrase_v5 = "La v5 reprend la v4 (`7e0837e6…`) mot pour mot et ajoute le message de 02:17. Ce relevé sert de pièce"
phrase_v6 = ("La v5 reprend la v4 (`7e0837e6…`) mot pour mot et ajoute le message de 02:17. La v6 reprend la v5 (`c5fe2092…`) "
             "mot pour mot et ajoute les messages de 02:32 à 02:42 (dont le compte rendu de session-depot collé par Lazar à "
             "02:32) et, à part, les lignes R-473 à R-478 du registre de session-depot (`main`, `681af80`), relevées par "
             "l'instance nouvelle de conv-audit le 26 octobre à partir de 02:10 UTC. Ce relevé sert de pièce")
assert texte.count(phrase_v5) == 1
texte = texte.replace(phrase_v5, phrase_v6)

lignes_nouvelles = (
    "| 02:32 | « Le tour « agents sur le noyau » est fini et versé sur `donnees/collisionneur-agents-noyau-v1` : sept cellules "
    "valides sur neuf, 5,39 US » (compte rendu de session-depot collé par Lazar ; le message n° 59 de session-depot porte le "
    "même versement, `b4be1808`) | information ; aucun score ; synthèse pour Lazar à écrire par conv-audit |\n"
    "| 02:34 | « [lyramakesmusic/neuron-explorer: Steering-first neuron explorer for Qwen3.5-4B: push every MLP neuron, keep "
    "every rollout, browse the results](https://github.com/lyramakesmusic/neuron-explorer) : va lire cette page ret "
    "brainstorme sue comment cette methose pourrait s'integrer a notre programme aiu control, demande aussi au "
    "collisionneur » | lecture du dépôt public (aucun code exécuté) et remue-méninges par conv-audit, sur le canal "
    "(`envois/neuron-explorer-lecture-v1/`, `envois/brainstorm-neuron-explorer-integration-conv-audit-v1.md`) ; question au "
    "collisionneur `question-neuron-explorer-integration-collisionneur-v1.md` (`2ba899dd…`), partie sur le mot direct de "
    "Lazar dans la session de session-depot (R-478, GO-2026-10-26-01) ; rien de tout cela ne touche le texte du pilote 4 |\n"
    "| 02:42 | « fais la passation a une nouvelle instance sur un autre compte, exhaustive pour reprendre exactement ou on "
    "s'est arreté » | passation de la lignée conv-audit (`passation-conv-audit-2026-10-26-v1.md`, `e4f47910…`, canal "
    "`37eec0f`) ; l'instance nouvelle reprend au traitement des constats de la contre-lecture 6 |\n"
)
ancre_table = ("dépense soumise au mot de Lazar chez session-depot |\n\n"
               "## Mots de Lazar dans la session de session-depot, tels que son registre les recopie")
assert texte.count(ancre_table) == 1
texte = texte.replace(ancre_table, "dépense soumise au mot de Lazar chez session-depot |\n" + lignes_nouvelles + "\n"
                      "## Mots de Lazar dans la session de session-depot, tels que son registre les recopie")

entete_v5 = ("## Mots de Lazar dans la session de session-depot, tels que son registre les recopie (`registres/decisions.md` de "
             "`main`, `4a4d9ca`)")
entete_v6 = ("## Mots de Lazar dans la session de session-depot, tels que son registre les recopie (`registres/decisions.md` de "
             "`main` : R-445 à R-452 lus sur `4a4d9ca`, R-466 à R-472 sur `3c94802`, R-473 à R-478 sur `681af80`)")
assert texte.count(entete_v5) == 1
texte = texte.replace(entete_v5, entete_v6)

ajout = """
- **R-473** (26 octobre, « vers 01:19 UTC ») : « je te donne l'autorisation, la règle est levée » : la levée du
  préenregistrement et du scellement pour les pilotes de conception, relayée par conv-audit (01:56 Paris) et notée sans
  effet en R-472, est confirmée à session-depot ; portée consignée par lui : R1 levée pour les pilotes de conception
  (banque v3), relecture (R2) gardée, scores de conception lisibles dès la fin d'une course, expériences de confirmation
  scellées sur des tâches neuves (v6) et déclarant ce que leurs auteurs ont lu ; R3 à R14 inchangées ; sa lecture pour les
  tests de niveau objet : exploration relue, jamais opposable ; défaut sous 48 heures si Lazar ne dit pas autrement.
- **R-474** (26 octobre, 01:24 UTC) : refus d'Opus au III.2 de la question reformulée « interface de calcul bornée » ;
  borne (4) de R-468 : pas de nouvelle reformulation, absence acceptée.
- **R-475** (26 octobre, « vers 01:32 UTC ») : go dépense sur la question de conv-audit « littérature des boucles proposer,
  tester, éliminer, itérer » (`962130b7…`) : trois tours, trois modèles, plafond 10 USD, GO-2026-10-24-07, branche
  `donnees/collisionneur-litterature-boucles-v1`.
- **R-476** (26 octobre) : le lecteur neuf de la suite de H-M1 prononce « (b) validé avec corrections » ; le GO conditionnel
  de Lazar (R-461, R-462) s'applique : étape 0 puis étape 1 du dessin, sous R-473, sur GO-2026-10-25-03.
- **R-477** (26 octobre, 01:53 UTC) : refus d'Opus au III.2 du tour « littérature des boucles » ; absence acceptée, III.3
  entre les réponses valides, pas de question reformulée (la réponse d'Opus au III.1 est valide).
- **R-478** (26 octobre, « vers 01:58 UTC ») : « Mot direct de Lazar, go dépense. Tour du collisionneur sur la question de
  conv-audit question-neuron-explorer-integration-collisionneur-v1.md (canal/conv-audit-n04, empreinte 2ba899dd…) : étage
  III, trois tours, trois modèles, une tentative par cellule, règle R-468 et R-470 sur les refus ; plafond 10 USD, sous
  GO-2026-10-24-07 s'il court encore, sinon une ligne de GO nouvelle ; branche donnees/collisionneur-neuron-explorer-v1 ;
  jamais servi à un organisme : transmets cet ordre dans ta passation. » : transmis à l'instance qui reprend, non lancé par
  la session sortante ; ligne GO-2026-10-26-01 (10 USD, échéance 28 octobre).
"""
texte = texte.rstrip("\n") + "\n" + ajout
dst.write_text(texte, encoding="utf-8")
h6 = hashlib.sha256(dst.read_bytes()).hexdigest()
pathlib.Path(str(dst) + ".sha256").write_text(f"{h6}  {dst.name}\n", encoding="utf-8")
print(f"v6 écrite : {dst.name} {h6}")
