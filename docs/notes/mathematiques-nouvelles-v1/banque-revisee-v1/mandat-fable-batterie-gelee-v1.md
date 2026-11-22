# Mandat — Fable 5.2, effort maximal — texte de la batterie de fuite de la banque révisée (mathématiques nouvelles) — v1

- Émis le 2026-11-22 par la session des mathématiques nouvelles, sur GO-2026-11-22-115 (registres/go.md sur main) et le retour de la mère du 2026-11-22T19:02Z. Pièce à concevoir : critère de décision (règle « qui conçoit » de CLAUDE.md), effort maximal (GO-2026-11-22-114).
- Aucun appel de modèle payant, aucune dépense. Processeur seul si tu veux éprouver une formule.
- Branche : `claude/mathematiques-nouvelles-v1`. Écris tes pièces dans `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/batterie-v1/`, scelle-les (`PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER…`), commite et pousse sur cette même branche (retente le push jusqu'à 4 fois). Ne réécris aucun fichier existant.

## À lire (en entier)

1. `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/rapprochement-batteries-fable-opus-v1.md` (bd5c2af3…) — la batterie unique proposée, C1 à C4 ; c'est la base.
2. `…/banque-revisee-v1/juges-recus/juge-fable-max-v1.md` (b1380fe3…) et son erratum 1 ; `…/juges-recus/juge-opus-max-v1.md` (f82e0c8f…), § 2.3 et 2.4 surtout.
3. `…/banque-revisee-v1/diagnostic-opus-v1/note-diagnostic-v6-opus-v1.md` (da4d80f4…) et, au besoin, sa sortie texte.
4. `prereg/mathematiques-nouvelles-v1/preenregistrement-pilote-generation-v1-brouillon-4-v2.md` (212c6eca…) — règle aveugle A, lectures en preuve et en verdict, sous-banque.

## Décisions déjà prises (ne pas rediscuter)

- Critère de Lazar (GO-2026-11-22-115) : les quatre conditions du juge Fable, 0,75 gardé comme condition nécessaire, complétées des deux sondes du juge Opus (style, nombres).
- **Lecture provisoire, en attente du mot de Lazar** : « rappel au plus de 10 % à fausses alarmes fixées » se lit « excès au-dessus du hasard ≤ 0,10 », soit rappel ≤ 0,20 à fausses alarmes ≤ 0,10. Défaut sous 48 heures. Le texte le marque en tête « en attente du mot de Lazar » et prévoit en une ligne la variante si Lazar choisit autrement.
- Branches (mère, étage 2) : version 7 si C1 et C4 tenues au plus tard le 2026-12-04T23:59Z ; lecture en verdict seulement si C2 et C3 tiennent aussi ; sinon les bras courent sur la version 6, lecture en preuve seule, verdicts en description.
- Troisième sonde (tenue à l'écart du concepteur, écrite par le vérificateur après le gel de la banque) gardée ; retirable en premier, avec une ligne d'écart.
- Lecture en preuve gardée dans toutes les branches, libellé « réfutations certifiées » ; relecteur : aucun bras payant neuf ; toute affirmation porte sur « le système avec outil ».

## Ce que tu écris

`batterie-fuite-banque-revisee-v1.md`, court, phrases claires, sans acronyme non développé, gelable tel quel :
1. Les conditions C1 à C4, chacune avec : ce qui est mesuré, sur quoi (racines neuves, sous-banque), comment (point de fonctionnement, règle des ex æquo, rééchantillonnage, borne haute à 90 %, « non calculable = non tenu »), le seuil.
2. La spécification exacte de la sonde des nombres (traits, apprentissage, plis par mondes entiers) et celle, à la lettre, de ce que le vérificateur aura le droit de faire pour la sonde tenue à l'écart.
3. Le protocole des racines neuves (au moins 40, `secrets.randbits(128)` au gel, empreintes commises avant mesure, une seule mesure ; une version 8 sur un autre lot ; toutes les tentatives rapportées).
4. L'épreuve de la batterie avant emploi (règle R5) : une banque saine et au moins trois artefacts (vérité par la grandeur du littéral, vérité par le gabarit, contre-exemple au plafond), avec ce que chacun doit faire tenir ou tomber.
5. La lecture et les branches ci-dessus, et la relecture sur la banque réelle (valeur hors de la plage des racines neuves : lecture en verdict fermée, dit en tête du rapport).
6. Les faits du diagnostic à prendre en compte, en particulier : l'identifiant de gabarit sépare tout (aire 1,000) ; la longueur en jetons sépare en partie (0,646) — dis si elle entre dans une sonde ou dans C1 ; la règle aveugle à 63 sur 75 ; la puissance du test qui compare le bras outillé à la règle aveugle à 0,12 sur la version 6.
7. Une liste « ce qui pourrait rendre cette batterie fausse », et ta confiance.

Et `notes-a-la-mere-batterie-v1.md` : tout écart aux décisions ci-dessus, tout nœud, chaque nombre que tu as ajusté et pourquoi.

## Ensuite

La batterie sera contre-lue par un Opus neuf, puis tu vérifieras ses remarques (ou il vérifiera tes corrections). Elle ne se scelle comme gelée qu'après le mot de Lazar ou l'échéance du défaut. La version 7 du générateur viendra après, par un mandat à part. Ne commence pas la version 7.

Rends à la fin : chemins, empreintes, commit, et le modèle servi.
