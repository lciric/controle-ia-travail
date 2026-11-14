# Contre-lecture 3, ciblée sur les points modifiés (texte gelé v3 ; retouches du correctif de la passe ; correctif des lentilles v2) — rapport recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 à 10:18 UTC ; il n'a écrit aucune des pièces. Pièces relues :
texte gelé v3 `f52be8b9cc2404689f5f0235587d9d8df92cb7eae4cf3c2d47883f9e8533e75e` ; note du correctif de la passe (retouchée)
`be2f5825c7fdafea9068775a24050946faac72f5912a90f66e2ff8a6ec18d977` ; essai (retouché)
`999c0eace55241584292fea8be555dfac954243dad59f60c91baecd7a9961d3a` ; note des lentilles v2
`ae20219e95f701d33d37a427a8b2d3fb14145e70c70c1bc7a2f83c4810707802` ; différence des lentilles v2
`616434bc98394c191e00ae02cb9342317e7fbdaea780d771224babc45c12a3bc` ; essai des lentilles v2
`73f72af251f6ae49b3f2d8788e4eebe0af2b17f35f98b1df938e5921c4e9b473`. Rapport rendu vers 10:24 UTC. Recopié sans modification de fond.
Note de l'autrice : l'écart d'empreinte signalé pour la note des lentilles vient d'une faute de frappe dans la consigne donnée au
contre-lecteur (« …7707 ») ; l'empreinte relevée par `sha256sum` avant l'envoi était `ae20219e…7802`, celle que le contre-lecteur a trouvée.

---

## 1) Empreintes
| pièce | résultat |
|---|---|
| texte gelé v3 | `f52be8b9…e75e`, conforme |
| note du correctif de la passe d'activations (v2 retouchée) | `be2f5825…d977`, conforme |
| essai de la passe d'activations (v2 retouché) | `999c0eac…1d3a`, conforme |
| différence de la passe d'activations | `76b639a0…43ed`, inchangée depuis la contre-lecture 2 |
| note du correctif des lentilles v2 | `ae20219e…7802` : la consigne écrit « …7707 », début conforme, fin différente (faute de frappe probable de la consigne) |
| différence des lentilles v2 | `616434bc…a3bc`, conforme |
| essai des lentilles v2 | `73f72af2…b473`, conforme |
| `lenses.py` corrigé (carnet) | `2de7d6af…b3e4`, conforme, égal à la constante en dur de l'essai |
| `lenses.py` original (clone à `849bfe16`, arbre propre) | `00591cd7…3b6c` |
| rapports de la contre-lecture 2 | texte `1a4a1b8d…925e`, correctifs `50f6f7d5…1fb5`, conformes à leurs compagnons |
| référence publiée | `8904c4d3…30d3`, conforme |
| annexes citées par la v3 | v1, v2, plans v1 et v2, passation 09:33, rapport 1 expurgé, outil de comptes et sa sortie, tokeniseur du carnet : toutes conformes |

- Différence des lentilles : `git apply --check` réussit ; rejouée en mémoire sur l'original, elle redonne exactement `2de7d6af…b3e4`.
- `ast.parse` réussit sur le fichier corrigé et sur les deux essais. Validateur : `[]`.
- Aucun fichier modifié, aucun appel réseau ni de modèle, aucun code voisin ni essai exécuté ou importé, aucun chemin interdit ouvert, aucun refus de permission.
- Aucun `.sha256` dans `correctifs/` (annoncés « au scellement »).

## 2) Verdicts
- **Texte gelé v3 : scellable après corrections mineures.** Quatre retouches de règle (remarques 1 à 4) demandent une v4 (R12), relue sur ces seuls points.
- **Correctif de la passe d'activations, retouches : scellable après corrections mineures.** Restent le nom de version (remarque 9) et l'en-tête de l'essai (remarque 10).
- **Correctif des lentilles v2 : scellable en l'état** pour la différence et la note. Qwen3 est inchangé. L'essai est cohérent ; deux compléments conseillés, non bloquants (remarque 11).

**Tableau B.3, recalculé** (partie entière de l × 36/32, « R:dclm » pour `npR`, « J » pour `J` et `npJpp`, n = 64) : les quatre attendus sont exacts.
| cas | résultat du calcul |
|---|---|
| (i) référence | B-2, B-3, B-7 « reproduit » ; aucune garde (a), (c), (e) |
| (ii-a) | B-2 « non reproduit » (12 couches sur 12) ; B-3 et B-7 « reproduit » ; aucune chaîne en défaut |
| (ii-b) | garde (a) seule |
| (ii-c) | garde (e) aux 24 couches 0–23 ; garde (c) non déclenchée (0,935 à 0,957, au-dessus de 0,85) ; rien d'autre ne contredit |

- Marges de (i) : `r_med` minimum 0,567 (8–15), 0,786 (16–23), 0,969 (24–27) ; `pass` minimum 0,9375 ; B-3 minimum +0,352 ; B-7 maximum 0,134 (0–15), minimum 0,673 (26–29) ; témoin maximum absolu 0,039.
- Garde (e) à tort sur la référence : non. Écart minimal aux couches 0–23 : 0,042 pour J et 0,048 pour R, à la couche 1.
- Sous (ii-c), les seuils donneraient B-3 « non reproduit » et B-2 « partiel » : le code doit bien faire primer la chaîne en défaut.

## 3) Remarques
### Texte gelé v3
**1. À corriger — Seuil A, A3, « dépendance non lue » : règle inversée à la lettre.** Le texte écrit « toutes négatives pour la condition « chute < moitié de celle du sac de jetons » » ; « négative » veut dire que la condition tient dans au plus 1 découpe : lu ainsi, c'est le contraire de l'intention. Correction : « toutes **positives** pour la condition « chute < moitié » ». À dire aussi : avec une seule couche non sans objet, « dépendance lue » est inatteignable alors que « non lue » reste possible.

**2. À corriger — préambule (correctif 2) et garde (e) : « couches `0..30` exigées » est faux pour le code.** `neuronpedia_lens` exige `0..n−1` contiguës pour n quelconque ; le contrôle « 31 » n'existe que comme lecture à B0. Correction : (a) ajouter au correctif le nombre attendu ; ou (b) écrire « couches contiguës `0..n−1` exigées par le correctif ; n = 31 lu à B0 sur la ligne imprimée, sinon arrêt ».

**3. À corriger — B.1 « étapes » et Liste d'arrêt : l'essai du correctif (2) n'est joué nulle part** ; le contrôle « matrice égale à l'identité » de la garde (e) n'est pas placé dans B0. Correction : les ajouter à B0 (avant `score`) et l'essai à la liste d'arrêt, « aucun test sauté ».

**4. À corriger — Audit R4, « B-α, trop beau : `control_med` exactement 0 » : se déclenche sur la référence publiée.** Le fichier publié, arrondi à 4 décimales, porte `control_med` = 0 à trois endroits (« ablate pos » : logits couche 7 ; J couches 8 et 26 de Qwen3). Correction : « valeur non arrondie, |`control_med`| < 10⁻¹², pour `npR` en « steer 1x » (ou toute cible, à dire) » ; écrire dans l'attendu de (i) « aucun déclencheur « trop beau » ».

**5. Mineure — garde (e), bras « matrice identité » : pas d'artefact de R5** ; norme de « à 10⁻⁶ près » non dite (matrices en demi-précision). Correction : artefact « lentille factice égale à l'identité à une couche » ; « écart maximal en valeur absolue ».

**6. Mineure — Métrique.** (a) n : la règle omet la restriction aux neurones tirés au hasard (`is_rand`) ; sans effet sur Llama ; à écrire. (b) « seuls les poids non nuls comptent » : sous `lbfgs`, fixer une tolérance (|poids| > 10⁻⁸). (c) Témoins « sur les deux signes » : vrai pour A1 ; pour A2, ρ signé. (d) Cas sain (iii) : « Ġworld » = 1879 vérifié ; ajouter « arrêt s'il n'est pas dans les jetons gardés » et « sans division par σ ».

**7. Mineure — Seuil.** (a) A-ii : « chaque partie non sans objet (en distribution, hors distribution) » laisse entendre qu'une partie hors distribution peut être sans objet. (b) A-ii : avec une seule couche non sans objet, « apporte » est inatteignable ; à dire. (c) L'ordre de priorité est sans effet (verdicts déjà exclusifs) ; inoffensif. (d) Avec la partie entière, les rapports seuil / publié valent 0,54 à 0,71 ; 0,63 à 0,76 ; 0,87 à 0,88 ; le texte garde ceux d'une autre conversion.

**8. Mineure — Contre-lecture, remarques 17 (tableau 1) et 13 (tableau 2) : affirmation non vérifiable gardée dans un texte à sceller.** Le tableau 1 garde « modèle A ≠ modèle B. Le contre-lecteur s'est fié à une ligne d'attribution qu'il a mal lue ». Même constat que le contre-lecteur 2 : la ligne d'attribution que je vois nomme le modèle que mon environnement me donne pour le mien, avec l'adresse de la session autrice ; je ne peux pas certifier « autre modèle ». R2 n'exige qu'un sous-agent neuf non auteur, ce qui est tenu. Correction : « déclaré par l'autrice d'après l'outil de session ; non vérifiable par pièce ; R2 tenu de toute façon », et retirer « qu'il a mal lue ».

### Correctif de la passe d'activations (retouches)
**9. À corriger ou à assumer par écrit — R12.** La note et l'essai « v2 » ont été réécrits sous le même nom après avoir été commités et contre-lus (`1c3b8c9f…` → `be2f5825…`, `6d6c4c08…` → `999c0eac…`). Correction : renommer en v3, ou écrire au § 7 la phrase d'exception avec les deux empreintes de l'essai.

**10. Mineure — en-tête de l'essai non mis à jour.** `test_chat_open_vrai_tokeniseur` est juste à la lecture, mais il télécharge un tokeniseur sous licence alors que l'en-tête dit « aucun poids téléchargé » ; sans jeton d'accès à B0, il échoue et la liste d'arrêt en ferait une « chaîne en défaut » ; il ne vérifie pas l'empreinte d'`arch.py`. Correction : sixième point à l'en-tête (« réseau et accès au dépôt sous licence requis ; un échec d'accès n'est pas une chaîne en défaut mais un arrêt de montage ») ; affirmer `SHA_ARCH_CORR` dans le test.

### Correctif des lentilles v2
**11. Mineure — essai : deux compléments.** Ce qui tient : formats refusés par la bonne branche ; empreinte fausse refusée avant `torch.load` ; `KeyError` de `npR` sur Qwen3 atteint ; remplacement de `hf_hub_download` sur le nom lié dans le module. (a) Aucun test ne montre que `load_lens("J", Llama)` passe par `neuronpedia_lens`, ni que Qwen3 n'y passe pas ; ajouter un test à sentinelle pour chacun, plus « couches décalées 1..n », « J vide » et « matrice non carrée ». (b) `torch.randn(..., dtype=torch.float16)` sur processeur dépend de la version de `torch` ; préférer `torch.randn(d, d).half()`.

**12. Constat — code.** Qwen3 inchangé ; un modèle tiers garde le même `KeyError` ; empreinte calculée sur le chemin rendu, avant `torch.load` ; `score` reçoit des clés entières ; la couche 31 rend bien `None` (logits), comme la v3 l'écrit ; forme 4096 × 4096 non exigée (carré et formes égales) : une autre dimension ferait échouer `score` avec bruit, acceptable ; révision non épinglée, l'empreinte la remplace.

## 4) Les 35 remarques de la contre-lecture 2
Texte : traitées 1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 14 à 21 (réserves mineures sur 3, 7, 10, 12, 15, 17) ; partiellement 4 et 6 ; non 13 (maintien motivé, sans pièce). Correctifs : traitées 3, 4, 5, 7, 8, 9, 10, 12, 14 ; partiellement 11 (révision non épinglée, motif écrit, acceptable) ; constats 1, 2, 6, 13. Bilan : aucun traitement annoncé n'est absent ; trois incomplets (texte 4 et 6, correctifs 11), un maintenu sans pièce (texte 13). Seule contradiction nouvelle : remarque 1 ; la remarque 4 vient d'un déclencheur laissé tel quel.
