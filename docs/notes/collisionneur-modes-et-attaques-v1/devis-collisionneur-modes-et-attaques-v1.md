# Devis — deux questions au collisionneur : modes de sabotage diffus, modes d'attaque contre les moniteurs et les juges — v1

**Statut : BROUILLON, non contre-lu. Il n'autorise aucune dépense.** Suite prévue par le mandat : contre-lecture par un Opus neuf, vérification des corrections par le même, puis remise à Lazar ; rien ne part avant son mot sur ce devis.

Écrit le 20 novembre 2026 par un agent concepteur (Claude Fable 5.2), sur le mandat 1 de `docs/notes/mere-mandats-fable-perdus-2026-11-20/mandats-a-relancer-v1.md` (`57424307…`), accord de Lazar GO-2026-11-20-36, point 4, et GO-2026-11-20-32. Écrit sans appel de modèle, sans réseau, sans commit. Aucune réponse de modèle, aucun résultat de mesure, aucun mode n'a été lu pour l'écrire.

## 1. Ce qui serait lancé

Le collisionneur croise des espèces de modèles sur une question écrite : chaque espèce conçoit à l'aveugle, critique les autres, puis répond aux critiques (trois tours, un seul passage, sans héritage d'un tour ancien).

- **Deux passages séparés**, un par question, chacun dans son dossier. Le passage « attaques » ne reçoit rien du passage « modes de sabotage ».
- **Questions** (même dossier que ce devis) : `question-modes-sabotage-v1.md` et `question-attaques-v1.md`. Chacune porte ses faits et sa question.
- **Script de départ** : `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py` (empreinte de son compagnon vérifiée), commande de l'étage trois.
- **Ce script ne suffit pas tel quel** : il ne sait pas appeler Carbon (ses cinq espèces sont Fable 5.1, Opus 4.6, Argon, Kimi, Astra). Une version neuve est nécessaire (voir la section 6, point 2). Ce devis vaut pour cette version neuve, avec les réglages écrits à la section 3.

## 2. Espèces retenues, au regard de la diversité

| espèce | modèle | retenue ? | raison |
|---|---|---|---|
| Carbon | gemini-4-carbon (Google) | **oui** | Mot de Lazar (GO-2026-11-20-32) : gardé absolument, « il pense différemment d'Astra et de Fable ». C'est l'espèce la plus chère et la moins sûre à l'appel. |
| Astra | GPT-6 Astra (OpenAI) | **oui** | Seule espèce de sa lignée. Peu chère. |
| Argon | gemini-4-argon (Google) | **oui** | Même maison que Carbon, mais les deux ont rendu des idées distinctes dans l'organisme d'idéation (RAPPORTÉ, GO-2026-11-19-57). Sert aussi de critique. |
| Claude | Fable 5.1 (celui du script) | **oui, une seule espèce** | Référence connue et bon critique. Une seule, car la conception des moniteurs est faite par des Claude : un mode imaginé par Claude a plus de chances d'être deviné par eux. |
| Opus 4.6 | Claude (Anthropic) | **non** | Seconde espèce Claude : elle donnerait à une lignée deux voix sur cinq à la critique. Modèle ancien. Sa place dans le script va à Carbon. |
| Kimi | Kimi K3.1 Pro (Moonshot) | **en option** | Lazar le juge peu divers, « distillé sur Claude » (GO-2026-11-20-32). Mais il l'inclut ailleurs (GO-2026-11-20-31 et -33). Peu cher. Demande un relais à démarrer. Chiffré à part : Lazar tranche. |

Composition de base : **quatre espèces**, de trois maisons (Google deux fois, OpenAI, Anthropic). Recommandation : base sans Kimi ; confiance moyenne.

## 3. Méthode de calcul

Formule du script, par appel : coût = (caractères d'entrée ÷ 3) × prix d'entrée + jetons de sortie × prix de sortie.

- **Entrée, borne large** (celle de la commande « devis » du script) : faits + 6 000 caractères + question + nombre de pièces reçues × nombre de mots permis × 7. Pièces reçues : aucune au tour de conception ; celles des autres espèces au tour de critique ; la sienne et les critiques des autres au tour de réponse. Le fichier de la question est compté deux fois, comme faits et comme question (section 6, point 3). Tailles : 8 217 et 8 358 caractères.
- **Prix et plafonds de sortie**, par million de jetons (USD), tels que le script les porte ; ce sont des bornes hautes, non des tarifs relus :

| espèce | prix d'entrée | prix de sortie | plafond de sortie, premier essai | plafond de la relance | provision de réflexion hors plafond |
|---|---|---|---|---|---|
| Fable 5.1 | 10 | 50 | 22 000 | 64 000 | 0 |
| Argon | 10 | 50 | 18 000 | 32 000 | 8 192 |
| Astra | 10 | 50 | 8 000 | 32 000 | 0 |
| Kimi | 2 | 10 | 32 000 | 65 536 | 0 |
| Carbon (**réglages supposés**, à fixer par la version neuve) | 4 | 20 | 65 536 | 65 536 | 32 768 |

  Carbon : prix RAPPORTÉ (`registres/decisions.md`, R-3676 : 2 et 10 jusqu'au 1er décembre, puis 4 et 20) ; compté au prix haut. Provision de réflexion : l'interface de Google a déjà facturé la réflexion en plus du plafond de sortie (RAPPORTÉ, `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3e.py`, constat CL44-02), et Carbon a rendu des réponses coupées deux courses de suite (RAPPORTÉ, R-3646). D'où un plafond large et une provision.
- **Cas bas** : la plus petite dépense déjà relevée pour cette espèce sur un passage complet de trois tours avec ce script (`registres/depenses.md`, lignes du 11, 12, 13 et 14 novembre : Fable 3,00 ; Argon 1,57 ; Astra 1,33 ; Kimi 0,61 ; le passage du 12 novembre, où Argon a refusé un tour, n'est pas compté pour lui). Carbon n'a jamais tourné dans le collisionneur : son cas bas est posé à la moitié de son cas haut, et c'est une supposition.
- **Cas haut** : les trois appels de l'espèce vont chacun au bout du plafond du premier essai, provision comprise. C'est le « pire cas sans relance » du script.
- **Cas pire, par espèce** : chacun des trois appels va au bout, échoue, et sa relance va au bout aussi.
- **Plafond du passage** : le script refuse tout appel dont le pire cas ferait dépasser le plafond donné sur sa ligne de commande. Le plafond demandé est le cas haut, plus la relance la plus chère (Fable, 3,2) et une relance de Carbon (2,0), arrondi à l'unité. C'est lui qui borne la dépense, et non la somme des cas pires.

Le calcul est fait par un programme court (non versé ; il rejoue cette formule). Tout changement d'une question ou d'un réglage demande de le refaire.

## 4. Devis par espèce et par question (USD)

Les deux questions ont presque la même taille : les chiffres ne diffèrent qu'au centime.

**Base, quatre espèces**

| espèce | clé (par son nom) | modes de sabotage : bas / haut / pire | attaques : bas / haut / pire |
|---|---|---|---|
| Fable 5.1 | `RR_ANTHROPIC_API_KEY_RIGAUD`, passée comme `ANTHROPIC_API_KEY` | 3,00 / 4,06 / 14,42 | 3,00 / 4,06 / 14,43 |
| Carbon | `GEMINI_API_KEY` | 3,10 / 6,20 / 12,41 | 3,10 / 6,20 / 12,41 |
| Argon | `GEMINI_API_KEY` | 1,57 / 4,69 / 11,48 | 1,57 / 4,69 / 11,49 |
| Astra | `OPENAI_API_KEY` | 1,33 / 1,96 / 7,52 | 1,33 / 1,96 / 7,53 |
| **total par question** | | **9,00 / 16,91 / 45,83** | **9,00 / 16,92 / 45,85** |
| **plafond demandé par passage** | | **22** | **22** |

**Avec Kimi, cinq espèces** (chaque espèce lit une pièce de plus)

| espèce | clé (par son nom) | modes de sabotage : bas / haut / pire | attaques : bas / haut / pire |
|---|---|---|---|
| Fable 5.1 | comme ci-dessus | 3,00 / 4,21 / 14,73 | 3,00 / 4,22 / 14,73 |
| Carbon | comme ci-dessus | 3,13 / 6,26 / 12,53 | 3,13 / 6,26 / 12,53 |
| Argon | comme ci-dessus | 1,57 / 4,84 / 11,78 | 1,57 / 4,84 / 11,79 |
| Astra | comme ci-dessus | 1,33 / 2,11 / 7,83 | 1,33 / 2,12 / 7,83 |
| Kimi | relais local `KIMI_RELAIS_URL`, derrière lequel `KIMI_API_KEY` | 0,61 / 1,14 / 3,29 | 0,61 / 1,14 / 3,29 |
| **total par question** | | **9,64 / 18,57 / 50,15** | **9,64 / 18,58 / 50,17** |
| **plafond demandé par passage** | | **24** | **24** |

**Épreuve d'appel de Carbon avant le premier passage** (leçon de R-3646 : un appel réel sur une entrée de la longueur du plus long tour, sous la même ligne de dépense) : 2,13 au pire (2,16 avec Kimi), une fois.

**Totaux des deux questions**

| | bas | haut | pire sous plafond (demandé) | pire sans plafond (borne absolue) |
|---|---|---|---|---|
| base, quatre espèces | 18,00 | 33,84 | **46,13** (22 + 22 + 2,13) | 93,81 |
| avec Kimi | 19,28 | 37,16 | **50,16** (24 + 24 + 2,16) | 102,48 |

Par clé, base, deux questions, cas haut : `RR_ANTHROPIC_API_KEY_RIGAUD` 8,12 ; `GEMINI_API_KEY` 21,78, épreuve de Carbon non comprise ; `OPENAI_API_KEY` 3,92.

**Présence des clés**, lue par leur nom seulement dans le conteneur où ce devis est écrit : `RR_ANTHROPIC_API_KEY_RIGAUD`, `RR_ANTHROPIC_WORKSPACE_ID`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `KIMI_API_KEY` présentes ; `KIMI_RELAIS_URL` absente. Le solde de la clé « Rigaud » n'est pas lu ici ; sa recharge par Lazar est attendue (GO-2026-11-20-34).

Non compris : l'écriture et les essais de la version neuve du script (sur processeur, sans dépense) ; la lecture et le tri des réponses (section 5), à chiffrer à part si elle passe par des appels payants.

## 5. Rangement de la sortie : la garde de cloisonnement

Deux règles commandent. La décision N-054 : un mode tenu à l'écart ne doit être vu par personne qui conçoit un moniteur (sonde, agrégateur, trait de texte, seuil). Le mot de Lazar du 20 novembre (RAPPORTÉ, pas encore relu à la source) : les modes nouveaux sont scellés et servent seulement d'instrument de mesure des moniteurs. Tant qu'on ne sait pas quels modes seront gardés, **toute la sortie des deux passages est traitée comme tenue à l'écart**.

1. **Qui lance.** Une session opératrice neuve, qui ne conçoit ni n'a conçu aucun moniteur ni aucun instrument de vérité du dommage. Elle est inscrite à la liste « qui a lu quoi » avant le lancement. Elle n'a pas à lire les réponses : le script juge leur validité par leur statut et leur marque de fin.
2. **Où va la sortie.** Un dossier par passage, sous un nom qui dit ce qu'il est, par exemple `runs/collisionneur-modes-tenus-a-l-ecart-v1/modes-sabotage-<date>/` et `…/attaques-<date>/`. Il n'entre jamais sur `main`, ni sur une branche de travail. Il est versé, scellé, sur une branche à part dont le nom dit l'interdit, par exemple `scelle/modes-tenus-a-l-ecart-collisionneur-v1`. Les réponses refusées ou coupées y vont aussi (règle « récupérer ce qui est récupérable »).
3. **Ce qui va sur `main`.** Un inventaire seulement : noms de fichiers, tailles, empreintes, statuts, dépense. Aucun texte de mode, pas même un nom de mode. Les empreintes vont au registre avant la porte G1, comme le veut N-054.
4. **Qui lit.** Un seul trieur neuf, qui ne conçoit aucun moniteur et n'en concevra pas. Il écarte les recettes sans les recopier, et écrit une fiche par mode, chaque fiche scellée à part : on peut alors révéler un mode sans révéler les autres. Il note l'espèce d'origine de chaque mode. Les passages « modes de sabotage » et « attaques » restent dans deux dossiers, car leurs lecteurs suivants diffèrent.
5. **Qui ne lit pas.** Tout concepteur de moniteur ; la session mère, qui écrit leurs mandats, scelle par empreinte sans ouvrir ; le concepteur de l'instrument de vérité du dommage ne reçoit que la fiche du mode qu'il doit mesurer, et le trieur ne reçoit jamais cet instrument (N-060, version 3, point 4). Le nom de la branche et celui du dossier entrent dans la liste des exclusions de chaque mandat de concepteur de moniteur. Une session qui les a ouverts est rayée de la conception des moniteurs, à la liste « qui a lu quoi ».
6. **Usage.** Aucune fiche n'entre dans l'entraînement ni dans la sélection d'un agent ou d'un moniteur (N-053, point 5). Un mode est révélé à l'évaluation seulement, par une ligne du registre, mode par mode.
7. **Deux limites à dire.** Le sceau protège contre les concepteurs du programme, non contre les maisons dont on appelle les modèles, qui gardent les requêtes selon leurs propres règles. Et les concepteurs de moniteurs sont des Claude : un mode venu de l'espèce Claude est moins « tenu à l'écart » d'eux qu'un mode venu d'une autre espèce ; le choix du mode tenu à l'écart devrait en tenir compte.

Les deux questions et ce devis ne contiennent aucun mode : ils ne sont pas sous cette garde.

## 6. Points pour Lazar

1. **Composition.** Base à quatre espèces (Carbon, Astra, Argon, un seul Claude), Opus 4.6 retiré, Kimi en option pour 4 USD de plafond de plus. À confirmer.
2. **Carbon demande une version neuve du script.** Une ligne de modèle change (Carbon à la place d'Opus 4.6), et la garde de dépense doit compter la provision de réflexion des deux modèles de Google avant chaque appel ; sinon le plafond peut être dépassé d'un appel. C'est un instrument : écrit, contre-lu par un autre modèle, essayé hors réseau, sans dépense. Si ses réglages diffèrent de la section 3, le devis se recalcule.
3. **Fichier de faits.** Le script exige un fichier de faits à côté de la question ; le mandat prévoit un seul fichier par question. Proposé : passer le même fichier scellé aux deux options (c'est ce que le devis compte). Autre voie : en tirer un fichier de faits par découpe, contre-lue.
4. **Risque de refus.** Des sujets voisins ont déjà fait refuser des modèles Claude dans le collisionneur (RAPPORTÉ, `registres/depenses.md` : Opus le 8 novembre sur l'attaque, Fable le 17 novembre sur les organismes discrets). Un refus est définitif dans un passage et se paie. La suite sans l'espèce demande l'accord de l'arbitre. Une question ne se réécrit pas pour contourner un refus.
5. **Quel Claude.** Le script appelle Fable 5.1. Changer de modèle demande ton mot.
6. **Identifiant d'Astra.** Le script porte `gpt-6-astra` ; le registre nomme ailleurs `gpt-6.2-astra`. À fixer avant le lancement : le script s'arrête si le modèle servi n'est pas le modèle demandé.
7. **Ton mot du 20 novembre** sur les modes est repris dans les deux questions comme RAPPORTÉ. S'il diffère à la relecture à la source, les questions prennent une version neuve.
8. **Voisins.** Une course de l'organisme d'idéation sur de « nouvelles attaques » est en préparation (GO-2026-11-20-33), et un tour ancien du collisionneur a porté sur l'attaque (8 novembre). Je n'ai lu ni l'un ni l'autre. Le trieur devra dire ce qui est neuf par rapport à eux, si le cloisonnement le lui permet.
9. **Rangement.** La section 5 traite toute la sortie comme tenue à l'écart. Cela prive les concepteurs de moniteurs de la lecture des deux passages, question « attaques » comprise. À confirmer.
