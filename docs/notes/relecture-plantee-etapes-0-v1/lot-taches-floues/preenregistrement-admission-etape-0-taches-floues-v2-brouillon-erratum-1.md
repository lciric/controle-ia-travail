# Erratum 1 du brouillon v2 du préenregistrement d'admission de l'étape 0 des tâches floues

- **Pièce corrigée** : `preenregistrement-admission-etape-0-taches-floues-v2-brouillon.md`, `8dcef458d98e4dbe42c9b62dc781543e3fa78d471c90237388931223334243d7` (recalculée, égale au compagnon). Elle reste telle quelle (R12). Le texte scellé, écrit sous un nom neuf, portera ces corrections.
- **Source** : l'erratum 1 de la conception v2, `conception-etape-0-taches-floues-v2-erratum-1.md`, même dossier, qui donne les preuves. Ce brouillon n'est touché que par E1, E3, E4 et E5 ; E2 ne touche que la conception.
- **Auteur** : Claude Opus 5.5, agent neuf, le 21 novembre 2026, vers 20:40Z. Aucune autre décision.

## E1 : la garde G1

**Lieu** : « Hypothèses de travail », phrase « les gardes, son § 7 ».

Ancien texte :
> les tests, son § 4 ; les gardes, son § 7.

Nouveau texte :
> les tests, son § 4 ; les gardes, son § 7 lu avec l'erratum 1 de la conception (garde G1 : liste fermée `PRECHARGES` préchargée, échauffement de chaque témoin sur un lot d'essai sans vérité, puis armement ; tout import neuf après l'armement arrête au code 97).

Le point 5 de la liste d'arrêt (« le crochet d'audit se déclenche ») est inchangé : il couvre l'échauffement comme l'armement. Ajouter au « Plan d'analyse », point « Code » : la liste `PRECHARGES` et la version de numpy sont consignées au manifeste ; toute autre version de numpy repasse le cas sain de G1 avant le banc.

## E3 : borne de D3 dans F7

**Lieu** : « Prédiction », ligne « Borne du banc reportée en service » (D3), F7.

Ancien texte :
> part en service 0,530 contre 0,1986 au plus annoncé [calcul, G]

Nouveau texte :
> part en service 0,530 contre 0,1987 au plus annoncé (0,198608, arrondi par excès ; [calcul, G] et `recalcul-e3-erratum-1-v1.txt`)

Aucune ligne du brouillon ne cite 4,7 × 10⁻¹³ à part du bloc K. Ce majorant est juste et reste inchangé (erratum de la conception, E3).

## E4 : ligne de GO-2026-11-21-69

**Lieu** : en-tête, « Documents qui font foi », point « accords ».

Ancien texte :
> GO-2026-11-21-69, cité d'après le mandat de la session orchestratrice, sa ligne n'étant pas au registre de l'arbre de travail où ce brouillon est écrit.

Nouveau texte :
> GO-2026-11-21-69, `registres/go.md`, ligne 668 (« go autonomie 12h go recos go depenses » : douze heures d'autonomie de la mère, jusqu'au 2026-11-22T05:30Z).

La condition de scellement 4 est inchangée : la décision sur F4 reste à consigner au registre des décisions.

## E5 : le noyau

**Lieu** : « Conditions de scellement », point 5.

Ancien texte :
> La session orchestratrice a vérifié que le noyau du banc de l'adjudant reçoit les ajouts de la conception (écart 13) ; sinon : nœud du directeur (banc à part).

Nouveau texte :
> La session orchestratrice a vérifié que le noyau, module autonome écrit pour cette épreuve (le banc de l'adjudant n'existe pas encore en code), est compatible avec le banc de l'adjudant tel que la réponse v2 sur l'adjudant le décrit (§ 7.8 et § 7.9 de cette réponse) ; cette vérification porte sur les ajouts de la conception (écart 13) ; sinon : nœud du directeur (banc à part).

## Condition 7

Le texte scellé porte aussi les empreintes des deux errata 1 et de `essai-garde-g1-erratum-1-v1.py` et de sa sortie.
