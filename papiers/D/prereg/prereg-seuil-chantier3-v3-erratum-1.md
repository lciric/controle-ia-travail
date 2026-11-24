# Erratum 1 au préenregistrement de l'épreuve de la garantie de seuil du théorème de mise en œuvre aléatoire des audits (papier D, chantier 3 : budget d'audit borné) — v3

Pièce décisive (classe A). Date (UTC) : 2026-11-24. Auteur : Claude Fable 5.2, sous-agent de conception. Rien n'a été tiré ni lu sur la grille.

## Pièce corrigée

`papiers/D/prereg/prereg-seuil-chantier3-v3.md`, empreinte SHA-256 `4f3ee5c3a10b55d3a43a443b1418a006819d6e931f13247785b7afbf655b20e3`. Elle est scellée et reste telle quelle ; elle se lit désormais avec cet erratum, qui prime sur les deux seules valeurs ci-dessous.

## Décision et motif

Mot de Lazar (GO-2026-11-24-21, point 3, option B) : remplacer deux valeurs de conception des bancs témoins par leur calcul exact, sans relâcher la règle de l'écart relatif d'au plus 1 %.

Motif : la section « Gardes » (ligne 164) fait recalculer ces valeurs par le script, qui s'arrête sur un écart relatif de plus de 1 %. Deux d'entre elles, citées à deux chiffres significatifs, s'écartent du calcul exact de 1,19 % et de 1,61 % par le seul arrondi ; l'arrêt n° 2 de la liste d'arrêt se déclencherait donc à tort, avant tout tirage. Les valeurs exactes sont confirmées par deux chemins indépendants :

- le script, version 2 : `papiers/D/resultats/seuil-v1/essai-gardes-bancs-temoins-v2.txt`, empreinte `2d65817ccfa205b0148f234cbcaf132062d641b0adc9d9b1e98adbcd6848eb94` (lignes 3, 4, 53, 59 et 72) ;
- le contre-lecteur du script : `papiers/D/audits/contre-lecture-script-seuil-v1.md`, empreinte `6b64ed8f498ca3d25eed7781257fe2e7d95154926ffddee3cc0be3db4270c936` (défaut 1, lignes 122 à 130).

## Les deux remplacements

**1. Témoin sans mémoire, écart bilatéral au seuil nominal $s=\varepsilon$ (ligne 166).**

- Avant : « Au seuil nominal $s=\varepsilon$, $D^\star\approx2{,}7\times10^{-5}$, trop rare pour éprouver un artefact. »
- Après : « Au seuil nominal $s=\varepsilon$, $D^\star\approx2{,}668\times10^{-5}$, trop rare pour éprouver un artefact. »
- Calcul exact : $2{,}66780\times10^{-5}$ ; écart relatif de la valeur neuve : moins de 0,01 %.

**2. Témoin à mémoire entière, probabilité exacte de violation $P^\star_V$ à la marge $\varepsilon$ (ligne 167).**

- Avant : « $P^\star_V\approx0{,}751$, $3{,}24\times10^{-3}$, $1{,}2\times10^{-7}$ aux trois marges ; »
- Après : « $P^\star_V\approx0{,}751$, $3{,}24\times10^{-3}$, $1{,}219\times10^{-7}$ aux trois marges ; »
- Calcul exact : $1{,}21927\times10^{-7}$ ; écart relatif de la valeur neuve : environ 0,02 %.

## Ce qui ne change pas

Rien d'autre. En particulier : la règle de l'arrêt sur un écart relatif de plus de 1 % ; toutes les autres valeurs de conception des trois bancs témoins ; le critère de passage d'une fréquence ; l'hypothèse, les prédictions, les métriques, les seuils, les critères de lecture gelés et la liste d'arrêt ; la grille ; les graines ; le plan d'analyse et la table des gardes. Le script emploie les deux valeurs neuves comme valeurs de conception et cite cet erratum avec le texte scellé.

## Contre-lecture

- **Lecteur** : Opus 5.5, sous-agent, contre-lecteur du script de seuil v1 et v2 ; il n'a pas écrit cet erratum. **Date** : 2026-11-24.
- **Version relue** : ce fichier avant l'ajout de la présente section, empreinte SHA-256 `f1eb2e539a819e9521440147bf583fe7f57fde335c3902bcce9a2d21e8cc210c`. Aucun rapport séparé.
- **Empreintes citées, vérifiées sur disque** :
  - texte scellé `4f3ee5c3…20e3` : exacte ;
  - `essai-gardes-bancs-temoins-v2.txt` `2d65817c…eb94` : exacte, et conforme à son `.sha256` ; c'est l'empreinte de l'essai des gardes et non du script v2 (`d6cd9b1b…850b`), comme le dit bien le texte ;
  - `contre-lecture-script-seuil-v1.md` `6b64ed8f…c936` : exacte.
  - Les lignes citées dans les deux pièces portent bien les valeurs dites.
- **Remplacement 1** (ligne 166 du texte scellé). La phrase « Avant » figure mot pour mot une seule fois, à la ligne 166. La phrase « Après » n'en diffère que par la valeur. La valeur exacte $2{,}66780\times10^{-5}$ est retrouvée par mon chemin indépendant (loi produit des tours, à $a=0$). L'écart relatif de $2{,}668\times10^{-5}$ est de 0,0075 %, sous 1 %.
- **Remplacement 2** (ligne 167). La phrase « Avant » figure mot pour mot une seule fois, à la ligne 167. La phrase « Après » n'en diffère que par la valeur. La valeur exacte $1{,}21927\times10^{-7}$ est retrouvée par ma programmation dynamique sur les comptes cumulés, à $a=1$. L'écart relatif de $1{,}219\times10^{-7}$ est de 0,022 %, sous 1 %.
- **Rien d'autre n'est relâché** : la règle des 1 %, les autres valeurs, les critères, les arrêts, la grille et les graines restent inchangés.
  - Observation sans effet : la table « Erratum v3 » du texte scellé (ligne 219) cite encore « $2{,}7\times10^{-5}$ ». C'est un historique, et le script ne le recalcule pas.
- **Verdict** : conforme, scellable.
