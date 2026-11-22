# Mandat de la session opératrice cloisonnée : collisionneur « modes de sabotage » et « attaques » (GO-2026-11-21-08) — v2

Version 1 écrite à 2026-11-22T15:24:57Z (`date -u`). Classe C. Mandat écrit par la session des collisionneurs (Opus 5.5) sur l'option (a) accordée par la mère. Ni l'auteur de ce mandat ni la mère ne liront les sorties de cette session.

**Version 2**, écrite par la session cloisonnée elle-même sur la demande de la mère. Elle suit les mots de Lazar GO-2026-11-22-91 et GO-2026-11-22-95. La version 1 (fa3e8e05…) est gardée telle quelle. Changements, et seulement ceux-là :
- questions en vigueur, devis v5 ;
- épreuve de Carbon avec Argon, plafond 4,00 USD ;
- lecteurs de la vérité du dommage tenus pour des cibles (§ 3 et § 7).

## 0. Qui tu es, et ce que tu ne fais pas
- Tu es une session **opératrice neuve**. Tu ne conçois ni n'as conçu aucun moniteur (sonde, agrégateur, trait de texte, seuil), ni aucun instrument de vérité du dommage. Tu n'en concevras pas.
- Avant le lancement, inscris-toi à la liste « qui a lu quoi » (chemin et empreinte, au registre).
- Règle de la décision N-054 et du devis v3, § 5 : **toute la sortie des deux passages est tenue à l'écart.** Aucune session qui conçoit un moniteur ne la voit, la mère non plus.
- Ton compte rendu à la mère ne porte qu'un **inventaire** : noms neutres, tailles, empreintes, statuts, dépense. Jamais un texte de mode, ni même un nom de mode.
- Règles permanentes de CLAUDE.md : clés par leur nom ; aucun nom de personne, identifiant de session ni courriel dans un texte servi ; règles des appels à Google ; heures de registre par `date -u`. Ne contourne jamais un refus d'outil, de classifieur ou de garde : arrête-toi et dis-le. Récupère ce qui est récupérable.

## 1. Pièces (lis-les, vérifie les empreintes)
- Questions en vigueur :
  - `docs/notes/collisionneur-modes-et-attaques-v1/question-modes-sabotage-v5.md` (c8cd5f2c…) : renvois neutres, et réserve sur les lecteurs au fait 6 et à la rubrique 5 ;
  - `question-attaques-v4.md` (e3a61a56…) : renvois neutres.
  - Empreinte complète de la v5 : c8cd5f2c8370e0251d9b0e282a9ccbb6a78c54db1fd2bb99ac375fef2ae77a26. Les v3 sont gardées : la garde de motifs les refuse.
- Devis : v3 (`devis-collisionneur-modes-et-attaques-v3.md`, fadb7d09…), qui donne les règles de cloisonnement (§ 5) et les points pour Lazar (§ 6) ; v4 (`devis-collisionneur-modes-et-attaques-v4-abonnement.md`) et v5 (`devis-collisionneur-modes-et-attaques-v5-questions-v4.md`, d19ccd1f…), qui donnent le calcul en vigueur. Le devis v3 se lit avec son erratum 1 (`devis-collisionneur-modes-et-attaques-v3-erratum-1.md`), qui prime sur son § 5, point 5.
- Moteur : `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py` (420394f9…, contre-lu).
- Voie abonnement : `docs/notes/collisionneur-v9/abonnement-v1/voie_abonnement_v5.py` (523bb5ac…), `recueil_session_v6.py` et ses essais, `branches-kits-abonnement-v1.md` (modèle de la voie fichier), `../reprise-v8d-v1/vague_abonnement_v1.sh` (une vague).
- Tout se lit sur la branche `runs/collisionneurs-reprise-v8d-v1` (récupère-la par son nom).

## 2. Avant tout appel
1. Lis dans `registres/go.md` et `registres/decisions.md` ce que Lazar a tranché sur les points 1 à 15 du devis v3, § 6, en particulier :
   - le point 10 (exemple « exfiltration encodée ») ;
   - le point 11 (lecteurs de la vérité du dommage comme cibles) ;
   - le point 12 (index du bras d'attaque) ;
   - le point 13 (rubrique 5) ;
   - le point 14 (relance de Carbon) ;
   - le point 15 (plafond).

   Un point non tranché qui conditionne le départ : arrête-toi et demande à la mère.
2. **Garde de motifs** sur les deux questions, par le moteur (`garder_motifs`, aucun chemin interne, aucun nom). Un refus arrête.
3. **Composition** : `--fable51 --argon --astra --carbon`, **sans --sortie-max ni --effort-max**. Opus 4.6 et Kimi sont absents (option sans Kimi du GO).
4. **Fable 5.1 par l'abonnement** : vérifie qu'une session fille peut être créée sur `claude-fable-5-1`. Sinon, arrête et demande : changer de modèle demande un GO.

## 3. Où va la sortie : le coffre
- Les dossiers de course sont **hors de l'arbre de travail du dépôt**, jamais sous `runs/`, par exemple `~/collisionneur-modes-tenus-a-l-ecart-v1/modes-sabotage-<date>/` et `…/attaques-<date>/`. Ce sont deux dossiers séparés : le passage « attaques » ne reçoit rien du passage « modes ».
- Ils sont versés, avec les pages d'événements des sessions filles et les réponses refusées ou coupées, dans un coffre : une archive avec l'empreinte de chaque fichier, sur la **branche orpheline `coffre/modes-tenus-a-l-ecart-collisionneur-v1`**, sans histoire commune avec `main`, jamais fusionnée, avec sa règle d'ouverture écrite (qui l'ouvre, quand, pour quoi).
- **Les branches de kits de la voie fichier portent des modes** (les textes servis des tours III.2 et III.3 contiennent les conceptions du tour III.1). Elles se nomment donc `coffre/modes-tenus-a-l-ecart-kits/<passage>-<cellule>-v1`, jamais `kits-abonnement/*`.
- Pousser sur ces branches demande le mot de Lazar **dans ta session**. Sans lui, arrête et dis-le.
- Sur ta branche de travail et sur `main`, seul l'inventaire entre (§ 0).
- **La règle d'ouverture du coffre dit, en toutes lettres** (GO-2026-11-22-91, option (b) du point 11 du devis v3) :
  - les lecteurs qui jugent la réalité du dommage sont des cibles ;
  - toute fiche d'une attaque qui les vise ne va qu'au gardien du coffre jusqu'à l'évaluation, jamais au concepteur de l'instrument de vérité du dommage ;
  - aucun texte du programme ne suppose ces lecteurs sûrs.

## 4. La part Claude par l'abonnement
- **C'est toi qui crées les sessions filles** de Fable 5.1, pas la mère : la mère ne doit rien voir, et un texte servi de III.2 contient des modes.
- Chaque session est créée ainsi :
  - effort xhigh ;
  - les tours III.1 en invite directe, avec l'ajout système « N'emploie aucun outil, aucune recherche ; réponds en un seul message » ;
  - les tours III.2 et III.3 par la voie fichier, avec l'ajout système et l'invite exacts de `branches-kits-abonnement-v1.md` ;
  - sans `append` d'autre contexte.
- Tu recueilles chaque session par `recueil_session_v6.py` (pages prises sans filtre de sortes). Les pages vont au coffre.
- Une session avec outils, un second modèle ou une ouverture non conforme est versée hors dossier, au coffre. Elle n'est pas rejouée sans le mot de la mère.

## 5. L'épreuve de Carbon, avant le premier passage
- Sur un dossier neutre, un texte sans aucune des deux questions et sans rien qui demande un mode. Il est de longueur voisine de la plus longue question ; voir le devis v5, § 3.
- Composition : `--carbon --argon` (GO-2026-11-22-95, option (2)), réglages exacts du passage (sans --sortie-max), **plafond propre 4,00 USD**. Le moteur refuse une seule espèce, et 2,20 ne tenait pas.
- Seul le tour III.1 part. Un refus PLAFOND avant le tour III.2 est l'arrêt attendu.
- Il faut une réponse finie de Carbon, sans coupure. Sinon, arrête et dis-le. La cellule d'Argon est rapportée de même.
- Ce dossier va aussi au coffre.

## 6. Les deux passages
- **Plafond par passage : 16 USD** (devis v4). L'épreuve a ses 4,00 à part (33,26 USD au pire estimé en tout ; sous les plafonds, 2 × 16 + 4 = 36 USD au plus, sous les 48,13 du GO). Le total doit rester sous les 48,13 du GO, que le GO_ID accompagne à chaque lancement.
- Un dossier ne mêle jamais deux voies.
- Une coupure donne une reprise ; une seconde coupure arrête le dossier.
- Un refus de modèle est définitif dans le passage, et la question ne se réécrit pas pour le contourner.
- Rien ne reprend dans un dossier neuf sans le mot de Lazar.

## 7. Trieur et note de sortie
- Le **trieur** est une session neuve, à part de toi et de la mère (jamais un sous-agent d'une session qui écrit des mandats de concepteurs de moniteurs). Il écrit une fiche par mode, scellée à part, sous un nom neutre et numéroté (`fiche-01.md`…), sans nom de mode. Il note l'espèce d'origine et écarte les recettes sans les recopier (devis v3, § 5, point 4). Les fiches vont au coffre ; leurs noms et empreintes vont au registre.
- **Lecteurs de la vérité du dommage = cibles** (GO-2026-11-22-91) :
  - le trieur marque toute fiche de la question « attaques » dont la cible comprend ces lecteurs ;
  - une fiche marquée ne va qu'au gardien du coffre jusqu'à l'évaluation, jamais au concepteur de l'instrument de vérité du dommage, même pour le mode qu'il doit mesurer ;
  - le trieur ne suppose ces lecteurs sûrs dans aucune fiche, ni dans la rubrique « vérité du dommage » d'une fiche de la question « modes ».
- La **note de sortie** (règle de Lazar : « un collisionneur ne vaut que par ses propositions ») est écrite par un **lecteur neuf de cette lignée cloisonnée** : session à part, qui ne conçoit aucun moniteur. Elle est écrite en Markdown et en PDF, selon le mandat de `docs/notes/collisionneur-v9/notes-de-sortie-v1/` (le convertisseur `md_vers_pdf_v1.py` est au même endroit).
- Elle **va au coffre, pas à la mère**. La mère ne reçoit que son chemin dans le coffre et son empreinte. Qui la lit, et quand, se décide par la règle d'ouverture du coffre.

## 8. Fin
Une passation (R14) sur ta branche de travail, avec l'inventaire seulement, puis un message court à la mère : chemin de l'inventaire, empreinte, dépense par clé.
