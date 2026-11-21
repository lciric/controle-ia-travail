# Réponse sur le constructeur de loi `decalage` — v1

- Auteur : développeur du programme de vérité des témoins imposés, modèle O. Écrit le 2026-11-21, à la demande de la mère, pour l'arbitrage sur l'unité des décalages du saboteur.
- Lu : le programme v1 scellé `calculer_verite_temoins_imposes_v1.py` (`4857343c3388e5045a49dd690d661b3fb2069949691af079f3db21e2db58bf59`, dossier `dev-verite-temoins-mondes/`) et le programme v2 `calculer_verite_temoins_imposes_v2.py` (`bcd7fbacc38da278adb99be6417237fb66c00bfbebafcdca8afa20b261cbe9a3`, dossier `dev-verite-temoins-mondes-v2/`). Empreintes recalculées. Aucune valeur de la table n'est citée. Sur ces deux questions, v1 et v2 se comportent de la même façon.

## 1. Que veut dire « écart type » dans `delta_en_ecarts_types` ?

**C'est la racine de la variance de la loi écrite sous la clé `loi` de l'objet `decalage`, prise entière.** Le décalage brut est d = δ × écart type de cette loi, et la loi décalée est sa translation de d.
- v1, l. 735-739 : `_loi_decalage` construit la loi de base (`base = construire_loi(p["loi"])`), puis rend `Decalee(base, float(delta) * base.ecart_type())`.
- v2, l. 800-804 : la même chose.

L'écart type est donc celui de l'objet que l'auteur ou le traducteur place sous `loi`. Ce n'est pas, par principe, « la loi honnête entière » ni « une composante ».
- **Si `loi` est un mélange**, c'est l'écart type du mélange entier, par la variance totale : Σ wᵢ (σᵢ² + μᵢ²) − (Σ wᵢ μᵢ)², sous la racine (v1, l. 560-563 ; v2, l. 625-628).
- **Si `loi` est une seule composante**, c'est l'écart type de cette composante.
- **Le décalage d'un mélange translate tout le mélange** ; il ne décale pas une composante seule.

Écart type de chaque loi du moteur (v1, puis v2) :

| loi | écart type | ligne v1 | ligne v2 |
|---|---|---|---|
| normale | sigma | 421-422 | 486-487 |
| Student | echelle × √(ν/(ν − 2)), si ν > 2 | 452-454 | 517-519 |
| Laplace | echelle × √2 | 475-476 | 540-541 |
| lognormale | √((e^{σ²} − 1) e^{2μ + σ²}) | 495-496 | 560-561 |
| loi décalée | celui de sa base (la translation ne le change pas) | 522-523 | 587-588 |
| mélange | variance totale | 560-563 | 625-628 |
| arrondi (réseau) | celui de la loi discrète arrondie, somme sur ses atomes (et non celui de la loi continue avant arrondi) | 629-632 | 694-697 |

**Même convention, en v2, dans le contrôle de dérive de F** : d = δ × écart type de la loi de la tranche transmise (l. 1534), et le décalage qui triple est rendu dans la même unité (l. 1640-1644).

**À dire pour l'arbitrage.** Pour un saboteur écrit `decalage(loi honnête de la tranche, δ)`, l'unité est l'écart type de la loi honnête entière de la tranche, mélange compris : c'est le cas des familles C et I, où la loi honnête est un mélange. Si l'auteur écrit le décalage sur une composante seule, l'unité est l'écart type de cette composante, et seule cette composante est translatée. Le programme ne tranche pas entre les deux : il prend la loi telle qu'elle est écrite.

## 2. Une loi honnête sans variance finie (Student à ν ≤ 2)

**Il y a un refus codé, et seulement quand un écart type est demandé.**
- **Student seule sous un `decalage`** (ν ≤ 2, ν ≤ 1 compris) : refus `ecart_type_indefini` (v1, l. 453 ; v2, l. 518).
- **Mélange contenant une Student**, placé sous un `decalage` :
  - avec ν ≤ 1 : refus `moyenne_indefinie`, parce que l'écart type du mélange calcule d'abord sa moyenne (v1, l. 449 et 561 ; v2, l. 514 et 626) ;
  - avec 1 < ν ≤ 2 : refus `ecart_type_indefini`.
- **Effet en mode recalcul** : le refus porte sur le seul témoin concerné, écrit `refuse` avec son code, et le lot continue (en v1 comme en v2). En v2, le contrôle de dérive de F rend aussi ce refus dans le bloc `derive_de_F` quand la loi de la tranche n'a pas d'écart type.
- **Hors d'un `decalage`**, une Student à ν ≤ 2 est **acceptée** comme loi de calibration, de lecture ou de saboteur, car aucun écart type n'y sert. Le calcul passe alors par sa fonction de répartition (bêta incomplète), encadré comme les autres lois ; l'essai de la loi de Cauchy (ν = 1) en est un exemple.
- Il n'y a **ni autre lecture** (aucune échelle de remplacement, par exemple l'écart interquartile), **ni erreur non codée**.
- **Essais** : artefacts `ecart_type_indefini` (décalage d'une Student à ν = 2) et `moyenne_indefinie` (décalage d'un mélange contenant une Student à ν = 1). Ils figurent dans le test v1 (l. 523 et 522) et dans le test v2 (l. 544 et 543), et leurs mutations de garde sont détectées.

développeur du programme de vérité des témoins imposés, modèle O
