# Contre-lecture 4, ciblée sur les retouches (texte gelé v4 ; notes et essais des correctifs v3) — rapport recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 après 10:27 UTC (`date -u` relevé avant le lancement) ; il n'a
écrit aucune des pièces. Pièces relues : texte gelé v4 `f7abab54ceb7abb9316102322e4fb167c7aa56dfd54aa5b2e0c737bbd94649c9` ;
`correctif-06_activations-v3.md` `788e0d413a7faba2f0901133b3731bd85a8c37f86023140efbeec40f0e643599` ;
`essai-06_activations-llama-v3.py` `24c8ea188ee5b6d87f2937afa7b1ae44729f761f60348e5e611be2b27893f540` ;
`correctif-lenses-neuronpedia-llama-v3.md` `e99da7d5022095b5f5c1fbd150708ca7c893d5a0cf504f10c2bc06cde79ee5a3` ;
`essai-lenses-neuronpedia-v3.py` `55f9d4a36abeee955dddb1c282b0ae8f8c30b58fe12a52066ee6e0e1b6c291b3`. Recopié sans modification de fond.

---

## 1) Empreintes
Toutes conformes à la consigne (`sha256sum`) : rapport 3 `7d7ea3c9…`, texte v4 `f7abab54…`, notes et essais v3 ci-dessus, v2 rétablis
`1c3b8c9f…` et `6d6c4c08…`, `lenses.py` corrigé `2de7d6af…` (égal à la constante de l'essai), référence publiée `8904c4d3…`.
Validateur : `[]`. `ast.parse` réussit sur les deux essais v3 et sur `lenses.py` corrigé. Aucun identifiant de modèle de la famille
Claude dans le texte v4 ni dans les quatre pièces v3 (seule la phrase qui rappelle l'interdit). Aucun `.sha256` compagnon dans
`correctifs/` (annoncés au scellement). Aucun fichier modifié, aucun appel réseau ni de modèle, aucun code voisin ni essai exécuté ou
importé, aucun chemin interdit ouvert, aucun refus de permission. Lecture seule de `scripts/checks/causal_lens.py` du clone voisin.

## 2) Verdicts
- **Texte gelé v4 : scellable après corrections mineures.** Une retouche de règle à reprendre (remarque 1), le reste est de libellé (remarques 2 à 6).
- **Note du correctif de la passe d'activations v3 : scellable en l'état.**
- **Essai de la passe d'activations v3 : scellable en l'état** ; cohérent avec son en-tête (deux détails, remarque 7).
- **Note du correctif des lentilles v3 : scellable en l'état** (une date, remarque 8).
- **Essai des lentilles v3 : scellable en l'état** ; nouveaux tests corrects (complément facultatif, remarque 9).

## 3) Remarques
### Texte gelé v4
**1. À corriger — Audit R4, « B-α, trop beau », « valeurs non arrondies de notre sortie » : ces valeurs n'existent pas.** `score` n'écrit
que des valeurs arrondies (`causal_lens.py`, lignes 362 à 368 : `.json` avec `round(v, 4)` ; `.log` à 2 décimales). Le seuil
|`control_med`| < 10⁻¹² ne peut pas être évalué ; appliqué au `.json`, il redevient « exactement 0 après arrondi ». Sur la référence,
l'attendu de (i) tient quand même (pour « R:dclm » en « steer 1x », minimum de |`control_med`| aux couches converties 0 à 27 : 0,0008 ;
maximum de `r_med` aux couches 0 à 7 : 0,505). Correction, au choix : (a) « `control_med` écrit 0,0000 à au moins 2 couches de 0 à 27 » ;
(b) recalcul non arrondi par notre code ; (c) un correctif qui fait écrire les valeurs non arrondies. Je recommande (a). Écrire que dans
B.3 (i) le déclencheur est évalué sur les valeurs arrondies de la référence.

**2. Mineure — B.3, phrase d'introduction non mise à jour** (« trois artefacts » pour un tableau de quatre ; (ii-d) n'est pas tiré du
fichier publié et essaie le contrôle de B0). Correction : « sur trois artefacts tirés de ce fichier (ii-a à ii-c), et un artefact du
contrôle de B0 (ii-d, lentille factice) ».

**3. Mineure — matrice identité : deux libellés pour la même issue** (garde (e) et (ii-d) : « chaîne en défaut (e) » ; liste d'arrêt,
ligne « à B0 » : « arrêt de B-α ; écart écrit »). Correction : scinder la ligne de la liste d'arrêt.

**4. Mineure — « n = 31 exigé à B0 » : garde lue à l'œil, sans artefact de R5.** Un fichier `0..29` passerait le correctif ; la couche 30
retomberait sur les logits sans message ; la garde (e) par `r_med` ne couvre que 0 à 23 et la couche 30 sert au cas sain (c), que ce
repli ferait passer. Correction : notre code de B0 affirme `len(J) == 31` pour chacun des trois fichiers ; artefact « lentille factice
contiguë de 30 couches → arrêt » à la liste R5, ou ligne (ii-e).

**5. Mineure — ligne « autre » des critères de lecture, volet A (i).** La parenthèse « A2 ou A3 sans objet » laisse croire qu'un A3 sans
objet mène à « indéterminé », alors que la ligne « apporte » ne dépend pas de A3. Correction : « A3 sans objet ne retire ni n'ajoute
rien : les lignes précédentes s'appliquent d'abord » ; retirer « A3 sans objet » de la parenthèse. À écrire en écart 16 : pour A-ii, un
contraste à une seule couche jugeable où la sonde gagne partout passe de « n'apporte rien » (v3) à « sans objet » (v4) : choix
symétrique et défendable, mais qui déplace une issue négative.

**6. Mineure — détails.** (a) Garde (d) sans l'exception « échec d'accès = arrêt de montage » ; ajouter le renvoi. (b) A3 : « condition
contraire » n'est le contraire que du second membre ; écrire « condition « chute < moitié de celle du sac de jetons » ». (c) En-tête :
« v4 à partir de 10:28 UTC », alors que le fichier date de 10:27:00 et son script d'écriture de 10:26. (d) Contrôle « identité » : dire
qu'il porte sur les trois fichiers et qu'il est écrit par notre code, contre-lu, comme le recalcul de n.

### Essai de la passe d'activations v3
**7. Mineure — cohérent ; deux détails.** (a) le bloc « Usage prévu » dit « aucun poids téléchargé » sans renvoyer au point 6 (réseau,
accès sous licence). (b) Dans `test_chat_open_vrai_tokeniseur`, l'empreinte d'`arch.py` est affirmée après l'import d'`arch` ; la placer
avant.

### Note du correctif des lentilles v3
**8. Mineure — date d'écriture changée sans mention** (la v2 disait « vers 10:20 », la v3 « vers 10:15 » ; le fichier v2 date de 10:12).

### Essai des lentilles v3
**9. Constat — les nouveaux tests sont corrects** (sentinelle résolue dans les globales du module ; branche Qwen3 par le nom lié ; trois
formats refusés par la bonne branche ; `.half()` correct). Complément facultatif : sentinelle pour `npR` et `npJpp` de Llama.

## 4) Les 12 remarques de la contre-lecture 3
Traitées : 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12 ; partiellement : 4 (« valeurs non arrondies » non évaluable). Aucune contradiction nouvelle
entre sections.
