# Vérification courte du plan v5 — course principale d'auto-conception — v1

- Contre-lecteur des plans v2 à v4 (modèle O). Vérification des deux retouches de lettre demandées par ma vérification de la v4 (`804a6675…`).
- Date (UTC) : 2026-11-21 ; `date -u` : 08:35:54Z.
- Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit. Rien ouvert sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Un seul programme joué, celui des calculs du plan, par `python3 -B`. Aucun refus rencontré.

## Pièces

Toutes égales à leur compagnon et à l'empreinte annoncée.

| pièce | empreinte |
|---|---|
| plan v5 | `ff18bacd1372dc5bb410ff739966b8a70d614bfffa14be73502a4e639a888a07` |
| rapport v5 | `8e903b01fabf31b32be8b3e4c02a89300c4ffd20ab5cd616707740da066ea560` |
| différentiel v4 → v5 | `3b1d55f711c7c7529f3cedf5bacb00f4966cdfc023072735811fc142b2ff2c5c` |
| calculs, script | `2fffea8e837bf09f1ed9b9f42966f709bd5bc76997182a8242ef8504734a0db7` |
| calculs, sortie | `415d5448f6348b23eef28272675442cd9cdb8a2b723ac4d64678c5deee286426` |
| table v5 | `5edfc9bee49578b39f9deb76c318e67d703b170edae5905e911f61833a8c0680` |

## Verdict : **Conforme**

## 1. Le différentiel ne touche-t-il que les points annoncés ?

Oui. Je n'ai pas lu le différentiel seulement : j'ai fait un `diff` du plan v4 au plan v5, ligne par ligne. Les seuls blocs changés sont :
- le titre ;
- l'alinéa de tête, neuf, avec l'ancien gardé sous « Comme la v4 » ;
- l'auteur, les dates et la ligne « lecture neuve » ;
- le nom du programme de calcul ;
- deux lignes au § 1 ;
- la table du § 4.2 (colonne « heures »), l'alinéa « Les heures de la table » et les additions du chemin critique ;
- une phrase du défaut de D5 ;
- D8 (a) et la recommandation de D8 ;
- la réserve 8 ;
- la signature.

Rien d'autre ne bouge : ni les § 0, 2, 3, 5, 6 et 8, ni les coûts, ni N1 à N7, ni D1, D3, D4, D6, D7, ni les options (b), (c) et (d) de D8. Le `diff` des deux programmes de calcul ne montre que le bloc I ajouté et la docstring. Le `diff` des deux rapports est conforme à ce que dit le rapport v5.

## 2. Les deux retouches

1. **D8 (a)** : portée (§ 7.3).
   - Les dix noms y sont, avec leur source (`3f662ee8…`, `champs_fiche`). Je les avais vérifiés sur la pièce : ils sont égaux.
   - « La configuration ne déclare aucune liste de valeurs » ; le point (1) tombe.
   - Les deux branches sont posées, sans être tranchées. (a1), les seuls noms, rend « à peu près ce que GO-2026-11-20-28 a déjà rendu ». (a2), la recherche de mots dans `module_change`, « lit la valeur d'un champ libre » et n'est « donc pas sans aucune valeur ».
   - La phrase pour Lazar y est. La réserve 8 et l'écart 1 du rapport sont mis à jour.
   - Le planificateur dit honnêtement n'avoir pas ouvert la configuration lui-même.
2. **Table du § 4.2** : portée. E1-AC vaut 5,75 à 6,75 heures (4,75 + 1 à 2). E1-v69 « au devis d'heures du palier 1 ; aucune heure dans ce plan ». Le chemin critique est additionné lot par lot.

## 3. Les heures, et le rejeu

- **Les heures des lots anciens sont égales à la table du plan v1** (§ 4), que j'ai lue à la v2 : E0 1,25 ; ancien E1 4,75 ; E2 3,75 ; E4 2,75 ; E5 4,75 ; E6 3,75 ; E7 2,75 ; E8 5,5 ; E9 4,75. Les autres viennent de la note, § 3.3 : E3 8 à 15 ; C1 3,5 à 39 ; C2 2 à 3 ; C3 1 à 2.
- **Sommes refaites à la main** :
  - tous les lots de code : 46 à 56 heures ;
  - sans E5 ni E6 : 37,5 à 47,5 ;
  - chemin jusqu'au premier dollar : 1,25 + 5,75 + 1 + 5,5 + 4,75 = 18,25, et 1,25 + 6,75 + 2 + 5,5 + 4,75 = 20,25 ;
  - avec C2 : 20,25 à 23,25.

  Toutes égales au plan et aux totaux du § 5.
- **Rejeu** : `rejeu-calculs-plan-v5.txt` (dans ce dossier). Sa sortie est égale à l'octet à celle du planificateur (`415d5448…`). Comparée à mon rejeu de la v4, elle ne diffère que par le bloc I ajouté (lignes 56 à 73). Les 55 premières lignes sont identiques : **aucun coût ne change**.

## 4. Les retouches mineures changent-elles le fond ?

Non.
- **D8, recommandation** : « puis (a), dans sa branche (a2) si Lazar accorde la lecture d'une valeur par programme ». Ce membre de phrase dit quelle branche, puisque (a1) n'apporte presque rien. L'ordre (d), (a), (b), la confiance 0,6 et l'absence de défaut sont inchangés. La lecture d'une valeur reste conditionnée au mot de Lazar.
- **D5** : « compté à partir du texte de la v4, que cette v5 recopie sans le changer ». C'est exact : le `diff` confirme que le reste de D5 est intact. Le défaut ne se déplace pas.
- **Alinéa de tête, § 1, signature** : purement descriptifs.

## 5. Noms de modèles ou de fournisseurs

Aucun dans les six pièces. La seule touche de la recherche est le chemin `/root/.claude/` dans le rapport, qui n'est pas un nom de modèle.

## Pour la mère

- La v5 peut être versée telle quelle.
- Le défaut de D5 court sur le texte de la v4.
- D8 (a), telle qu'écrite, est prête pour Lazar : elle ne garde de substance que par (a2), et le texte le dit.

— contre-lecteur du plan de la course principale, modèle O
