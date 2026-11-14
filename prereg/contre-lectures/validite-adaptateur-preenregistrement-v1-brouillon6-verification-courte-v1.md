# Vérification courte du brouillon 6 « validité de l'adaptateur » (commit C7 rempli) — rapport v1

## 0. Identité

- Vérificateur neuf, sous-agent de la session du compte 4, **modèle B** ; l'auteur des brouillons 4 à 6 est le **modèle A**. Je n'ai écrit ni ce texte, ni ses brouillons, ni ses couples, ni leurs relectures, ni T0.7, ni son module ; dans cette course je n'ai ouvert ni T0.7 scellé, ni le contenu d'un fichier de `src/controle_ia/t07/`, ni aucun fichier de P3-bis, de `registres/`, de `donnees/`, de `diag/`, de `runs/`, ni aucune pièce de (ii-b).
- Heures (relevées par `date -u`, dans la commande) : consigne vérifiée à 2026-11-14T06:39:15Z ; empreintes des fichiers à 06:39:29Z ; rejeu à 06:39:44Z ; contrôles `git` à 06:39:45Z ; lecture du différentiel à 06:40:19Z ; rapport écrit à 2026-11-14T06:41:39Z.
- Consigne : `brouillons/validite-adaptateur-v1/consigne-verification-courte-brouillon6-compte4-v1.md`, `1ccb67e33ed0e2ae1daba7b35c034905bced81a295816dc081beb1dd549db96e` (vérifiée « OK »).
- Fichiers lus, empreintes recalculées par `sha256sum` et vérifiées par `controle_ia.scellement verifier` (toutes « OK », égales à la table de la consigne) :

| rôle | chemin | sha256 |
|---|---|---|
| brouillon 6 | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon6.md` | `7f0a29d1e8a656b01e763b43a2948d90eb7cf8df0ea444f068d975716098a0f5` |
| brouillon 5 | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon5.md` | `56fb63e9b2f4ae8cb8361e94568a99c4ddbdb219220670a7e05f004afdaead26` |
| générateur des couples | `brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon6-v1.py` | `f92c31c31eb1a7b6727d58a6d863884a4939f450c821ee90aef20600336915c2` |
| couples appliqués | `brouillons/validite-adaptateur-v1/candidat1-pieces/couples-brouillon6-v1.json` | `540487c02f788ad0c796ac69c37863d619d71939cc733b0a011ee2f690f84a08` |
| script d'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/appliquer-couples-vadapt-v2.py` | `933f0ebe4b97aa9aa5987a30e3f1898487c9dd6a241db71b2df2c2b67c978b71` |
| sortie de l'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/sortie-application-couples-brouillon6-v1.json` | `bc9453722eeb99a634fbfc192a1547591b1b3631c9b95bc4ed4bdad21d70eb22` |
| pièce de confirmation v2 | `brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-fusion-c2fab6cc-v2.md` | `321b169aef79a0ef3291a88f08d60f83ceaacef400615a3d8c14f97de88a440f` |
| annonce recopiée (C4-0056) | `registres-provisoires/compte-4-2026-11-14-v18.md` | `dc6fbfae2eb115731df920ef677870f3b03516f2a9877414fe14e205b4de8830` |
| validateur (appelé, non lu) | `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |

Du brouillon 6, j'ai lu les lignes que le différentiel touche (1, 3 à 6, 14, 266, 317, 324, 330), les lignes 300 à 348, et les passages qui citent le marqueur, le commit, `CODE-T07` ou les modèles (lignes 73, 86, 241, 242, 270, 280, 294, 319, 332, par extraits). Le reste du texte, identique au brouillon 5 à l'octet, n'est pas relu.

## 1. Verdict

**« Candidat conforme »** : le différentiel brouillon 5 → brouillon 6 ne fait que ce que décrit l'en-tête du générateur ; le commit écrit est, à chaque occurrence, celui de l'annonce C4-0056 ; aucun fait cité que je peux lire n'est faux.

Constats : **0 bloquant, 0 majeur, 4 mineurs** (aucune correction exigée avant le scellement ; un couple facultatif, VB6-02).

Résultats des six points de la consigne :

1. **Rejeu** : le générateur, rejoué avec les arguments de la consigne, écrit 14 couples, fichier égal à l'octet au fichier versé (`540487c0…`, `cmp` muet). L'application sur le brouillon 5 rend un fichier égal à l'octet au brouillon 6 (`7f0a29d1…`, `cmp` muet), code de retour 0, aucun marqueur restant. Le différentiel par lignes ne touche que dix lignes (1, 3, 4, 5, 6, 14, 266, 317, 324, 330), toutes couvertes par les 14 couples ; même nombre de lignes (348). Comme chaque « ancien » est exigé une seule fois et que la sortie est égale à l'octet, aucun autre changement n'existe.
2. **Commit** : `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` aux deux occurrences complètes (lignes 6 et 14) ; forme courte `c2fab6cc` aux lignes 14 (deux fois, dont le nom de la pièce), 317 et 324 ; égal au « Nouveau commit C7 » de C4-0056 ; `git rev-parse c2fab6cc` rend ce même identifiant. Le renvoi (« message de la mère du 2026-11-14, R-2617 et R-2642, journal du compte 4, C4-0056 ; ligne `CODE-T07` remplacée une seule fois, S7 `bd4b7cd9` ») reprend fidèlement le message recopié. Aucune occurrence de `<<` dans le brouillon 6.
3. **Couples** : voir la table du § 2 ; chacun fait ce que dit l'en-tête du générateur ; aucune contradiction trouvée avec les autres sections lues ; les phrases historiques (A6-06, A6-09) sont remises au passé sans changer leur fait.
4. **Pièce de confirmation** (dans les limites du § 0 de la consigne) : exactes — un seul fichier du module changé entre `b4cd9953` et `c2fab6cc`, `reextraction_p3_v1.py`, 14 lignes ajoutées et 2 retirées (`git diff --stat` et `--numstat`) ; 26 entrées dans `src/controle_ia/t07/` aux deux commits, toutes des fichiers `.py` ; liste des 25 autres entrées d'empreinte `c89f99637a623309fef4ee215af9d8d54246fdb6e9bd9855cc043d08fc3f5bee` aux deux commits ; `reextraction_p3_v1.py` : `c32696b82af620e5da07fc4ec5bbb801dc385467cbf8235b799ad28b6471eaf9` à C7, `af299587e6c73d7bcc67c881eb968ee997b09e576b28d4b22e76976a74bc7afb` à la fusion ; aucune différence sur `harnais/modeles.py`, `premier_test_ia/figees.py`, `premier_test_ia/conditions.py` ; le message du commit contient « fusion du correctif du contrôle de cache ». **Non vérifié, hors périmètre** : la nature du changement (fonction `revision_au_cache` seule), les numéros de ligne, le contenu des deux champs, la ligne 106 de `harnais/modeles.py`, la pièce précédente et la version 1.
5. **Forme** : `problemes(...)` rend `[]`. Aucun identifiant de modèle de rédacteur ou de lecteur dans le brouillon 6 ; la seule chaîne trouvée par la recherche de noms de modèles est le modèle étudié (ligne 43, hypothèses de travail), qui n'est pas visé. Les deux identifiants du brouillon 5 (lignes 4 et 266) sont remplacés par A6-07 et A6-11.
6. **Faits cités** : conformes — empreintes du brouillon 5 et de la pièce v2, chemin de la pièce, forme courte du commit, renvoi à C4-0056, nombre de modules (26) et de fichiers inchangés (25). **Non vérifiables** (registre ou fichiers hors de ma liste) : R-2593, R-2597, R-2598, R-2604, R-2605 et ses points, R-2617, R-2642, S7 `bd4b7cd9`, l'égalité du commit avec la ligne `CODE-T07` du registre, l'empreinte du brouillon 4 (`417d6aee…`, reprise telle quelle du brouillon 5), l'heure 06:37 (cohérente : journal à 06:36:44Z, consigne à 06:38:35Z).

## 2. Constats

Couples de l'auteur, un par un :

| couple | ligne | ce qu'il fait | avis |
|---|---|---|---|
| A6-01 | 1 | titre : brouillon 5 → brouillon 6 | juste |
| A6-02 | 3 | auteur des brouillons 4 à 6 | juste |
| A6-03 | 3 | origine du brouillon 6 ajoutée | juste ; VB6-03 |
| A6-04 | 5 | date et heure du brouillon 6 | cohérente |
| A6-05 | 6 | statut du brouillon 6 ; statut du brouillon 5 mis au passé | juste ; VB6-01, VB6-03 |
| A6-06 | 6 | marqueur du brouillon 5 décrit au passé | juste |
| A6-07 | 4 | identifiant → « modèle A » | juste |
| A6-08 | 14 | marqueur rempli, parenthèse retirée | juste ; VB6-01, VB6-02 |
| A6-09 | 14 | marqueur rempli par `b4cd9953`, phrase mise au passé | juste (fait historique gardé) |
| A6-10 | 14 | pièce de confirmation neuve citée | juste pour ce qui est vérifiable ; « fonction `revision_au_cache` seule » et « inchangés » : non vérifié, hors périmètre |
| A6-11 | 266 | identifiant → « modèle B » | juste ; cohérent avec les lignes 294 et 319 |
| A6-12 | 317 | table de la contre-lecture 2 mise à jour | juste |
| A6-13 | 324 | VB4-02 : « différé » → « appliqué au brouillon 6 » | juste |
| A6-14 | 330 | « Avant le scellement » mis à jour | juste ; VB6-04 |

- **VB6-01 (mineur) — provenance de l'annonce.** Le brouillon écrit « annoncé par la mère » (lignes 6, 14, 324). Le journal recopie un « message tapé dans ce compte, donné comme celui de la mère », et la pièce de confirmation dit elle-même que l'égalité du commit avec la ligne `CODE-T07` en vigueur n'est pas lue au registre. Ni l'auteur ni moi ne pouvons lire le registre : l'égalité entre `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` et la ligne `CODE-T07` est à confirmer par la mère avant le scellement. Aucune correction du texte exigée.
- **VB6-02 (mineur) — « au 13 novembre ».** Ligne 14 : « avant lui, C7 `b4cd9953` au 13 novembre ». La ligne `CODE-T07` recopiée dans C4-0056 porte l'heure 2026-11-13T23:42:46Z : le 13 novembre, les deux commits ont été tour à tour celui de la ligne. La phrase n'est pas fausse, mais elle est imprécise. Couple facultatif (« ancien » présent une seule fois, compté) :
  - ancien : « avant lui, C7 `b4cd9953` au 13 novembre ; »
  - nouveau : « avant lui, C7 `b4cd9953`, jusqu'au remplacement de la ligne (ligne recopiée datée du 2026-11-13T23:42:46Z) ; »
- **VB6-03 (mineur) — fondement de la notation des modèles cité de trois façons.** Ligne 3 : « R-2598 » puis « R-2605 » ; ligne 6 : « R-2605, point 2 » ; la pièce de confirmation attribue à « R-2605, point 3 » l'annonce du commit ; la seule source que je peux lire est le point 2 du message recopié en C4-0056 (R-2617, R-2642). Aucune contradiction démontrée ; renvois non vérifiables par moi, à contrôler au registre par qui peut le lire. Aucune correction exigée.
- **VB6-04 (mineur) — le brouillon 6 n'est pas le texte à sceller.** « Avant le scellement » dit que l'entrée de cette vérification « s'ajoute à cette section dans le texte qui suit » : le texte scellé sera donc une version neuve (un couple de plus au moins), dont le différentiel avec le brouillon 6 doit se limiter à cette entrée, et au couple de VB6-02 s'il est pris. Cohérent avec le statut (ligne 6) ; rappelé pour que ce dernier pas reste traçable.

## 3. Couples

Un seul couple, facultatif (VB6-02), à appliquer sur le brouillon 6 :

```json
[
 {
  "id": "VB6-02",
  "ancien": "avant lui, C7 `b4cd9953` au 13 novembre ;",
  "nouveau": "avant lui, C7 `b4cd9953`, jusqu'au remplacement de la ligne (ligne recopiée datée du 2026-11-13T23:42:46Z) ;"
 }
]
```

## 4. Limites

- **Écart de modèle entre A et B non vérifiable par moi** : je ne connais pas l'identifiant du modèle A autrement que par ce que les pièces en disent, et un élément de mon contexte d'exécution (la ligne d'attribution des commits de la session) porte le nom de mon propre modèle. La mère compare mon identifiant, donné dans mon seul dernier message, à celui du modèle A (N-052).
- Commandes `git` passées, toutes en lecture et sans afficher de contenu de `src/controle_ia/t07/` : `git diff --stat` et `--numstat` entre les deux commits sur `src/controle_ia/t07/` ; `git diff --stat` sur les trois fichiers de dépendances que nomme la pièce (compte de lignes de la sortie seulement) ; `git ls-tree` (comptes, types, noms, empreinte de liste) ; `git show <commit>:<chemin> | sha256sum` ; en plus de la liste de la consigne, `git rev-parse` sur les deux identifiants courts et `git log -1` (identifiant, titre et parents) sur `c2fab6cc`, qui n'affichent aucun contenu de fichier.
- Contenu de T0.7 (texte scellé et module) : non lu ; tout ce que la pièce de confirmation et le brouillon en disent est « non vérifié, hors périmètre ».
- Registres, pièce de confirmation précédente, version 1 de la pièce, brouillon 4, rapports des contre-lectures : non lus ; leurs empreintes et numéros cités sont « non vérifiables ».
- Vérification courte : le corps du préenregistrement (hypothèse, métrique, seuils, plan, puissance, dépense) n'est pas relu ; il est identique au brouillon 5 à l'octet.
- Aucun script de calcul versé : les contrôles tiennent dans les commandes décrites ci-dessus ; fichiers temporaires du rejeu laissés dans le bloc-notes de la consigne, non versés.
- Aucune écriture git, aucun appel réseau, aucun sous-agent, aucune clé ni variable d'environnement lue ; aucun refus de permission rencontré.
