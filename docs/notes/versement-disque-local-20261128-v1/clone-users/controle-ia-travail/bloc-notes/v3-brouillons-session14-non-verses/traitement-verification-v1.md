# Traitement des constats de la vérification de la v2 du programme fusionné — v1

Session 14, 15 octobre 2026. La v2 (`brouillons/pain-axis-programme-fusionne-v2/programme-fusionne-v2.md`, `189d049a0880afb799bb2c298a009ee54d7dbb4be557cbe9a5a445bdcd3187cf`) et le traitement des contre-lectures (`traitement-constats-v1.md`, `9d82e0b2bea644555b0aaa261106df4eaf392ebd26a66dcfd75254658bcfa098`) ont été vérifiés par un troisième sous-agent neuf, en lecture seule, fichiers donnés explicitement (R2). Rapport brut versé et scellé dans ce dossier : `verification-v2-v1.md` (`7e07756ddfab3d8fc3deb3bab742a625ccb5091b14bb208d09266767ed7f844b`). La v2 étant scellée (R12), les corrections vont dans `programme-fusionne-v3.md` (ce dossier).

**Règle de traitement.** Mêmes sorts que pour les contre-lectures : retenu, retenu en partie, non retenu, tranché par la session. Les numéros de section renvoient à la v3.

**Bilan.** 20 constats (0 bloquant, 3 majeurs, 7 mineurs, 10 pour information) : 20 retenus ; aucun non retenu. Les trois constats des contre-lectures que la v2 portait en partie (DI-02, DI-24, EX-20) sont complétés dans la v3 ; DI-26, non porté, l'est dans `registres/etat.md`. La catégorie « retenu en partie » aurait dû servir dans `traitement-constats-v1.md` pour DI-02 et DI-24 (réserve R4 du rapport) : c'est noté ici, le traitement scellé ne se réécrit pas.

## 1. Constats

| Constat | Gravité | Sort | Où dans la v3 | Traitement |
|---|---|---|---|---|
| VT-01 | majeur | retenu, option recommandée | statut ; « Contre-lectures et vérification » ; § 3 (colonne des niveaux, couverture) ; § 5 (PA-2 à PA-5, PA-7 à PA-10, PA-12, PA-13, PA-16) ; § 6 ; § 8 ; § 9, nœud 1 | Une seule règle : toute entrée d'une unité dans un préenregistrement, à quelque titre que ce soit, est un nœud sans défaut (nœud 1) ; seule la préparation (code, plan écrit) relève de la routine ; seul le choix du lecteur de C-P4b reste une proposition. PA-3, PA-4, PA-8, PA-9, PA-12 et PA-13 sont ajoutées au nœud 1 ; la colonne des niveaux du § 3 commence par « entrée : nœud 1 » pour toutes les unités ; « PA-4 peut entrer comme contrôle » est remplacé. |
| VT-02 | majeur | retenu | § 9, nœud 2 | Phrase proposée reprise : rien n'est prévu côté moniteur ; côté agent, le programme prévoit les organismes (section 7, (ii) ; T0.6) et le bruit d'activations de H6 (E1.6 ; revendication au nœud ouvert N-015) ; les écritures listées n'en font pas partie. Vérifié par la session sur `docs/programme-controle-ia-v2.md` (l. 97, l. 132, l. 188). |
| VT-03 | majeur | retenu | § 2 (Berg et Kaiser) ; § 9, nœud 14 ; § 12 | Les deux doses publiées ne sont plus recopiées (« sous les deux doses négatives publiées, p. 10, non recopiées »). La v1 et la v2 du programme, scellées, les contiennent : elles sont ajoutées aux pièces du nœud 14. |
| VT-04 | mineur | retenu | § 5 (PA-13) ; § 3 (PA-13) ; § 9, nœud 3 | NK12 (ton hostile adressé au modèle lu dans l'interrogatoire des poids) ajouté. Vérifié : `revue-croisee-NK1-NK19-v1.md` l. 317 (« Exposer un modèle à un contenu hostile, même dans une branche jamais renvoyée, est un nœud »). |
| VT-05 | mineur | retenu | § 5 (PA-3) ; § 3 ; § 6 ; § 9, nœuds 5 et 6 | Attaquant en boîte grise et cellules visant une copie du juge : modèle de menace, porté au nœud 6 (élargi aux « attaques hors des familles et du modèle de menace actuels ») plutôt qu'à un nœud neuf, pour garder la numérotation. Conclusion sur D1 : proposition, sauf si elle change de juge (nœud 5). |
| VT-06 | mineur | retenu | § 3 (NK14) ; § 9, nœuds 7 et 11 | Principe de NK14 déplacé au nœud 7, avec l'énoncé de la règle (« aucune accommodation ne réduit la surveillance », `correspondance-v1.md` l. 78) ; le nœud 11 ne garde que la collision. |
| VT-07 | mineur | retenu | statut ; § 9, nœud 1 | « Tout préenregistrement (papier C, T0.6, T0.7, T0.8, pilote T0.9, G1) ». |
| VT-08 | mineur | retenu | § 1, point 2 ; § 2 (lignes de la figure 10) | « Lecture graphique » ajoutée à toutes les valeurs tirées de la figure 10 : RP-PA-11 s'applique dès ce texte. |
| VT-09 | mineur | retenu | § 12 | Le filtre de sûreté n'a rien refusé pendant la contre-lecture de discipline et pendant la vérification (leurs rapports) ; le rapport d'exactitude n'en parle pas ; rien non plus pendant la rédaction des v2 et v3. |
| VT-10 | mineur | retenu | § 13 | Les deux PDF ont été versés le 6 octobre (niveau 2, lots 2 et 3) ; `197e909` est la racine du clone partiel de la session (`.git/shallow`), pas leur commit de versement. Lecture corrigée de `traitement-constats-v1.md` (EX-21) et du rapport d'exactitude (EX-21) : « versés le 6 octobre », non « au commit 197e909 ». |
| VT-11 | pour information | retenu | § 5 (PA-8) | Vérifié sur `2506.14261v4.pdf` p. 7, tableau 1 : sonde linéaire à la moyenne, Llama 3 8B 2,8, Qwen 2.5 14B 3,1, Llama 2 7B 3,85. Réserve ajoutée (R4). |
| VT-12 | pour information | retenu | § 1, point 1 | Renvoi aux requêtes consignées (l. 453) ; la formule « balayage, pas une preuve » (l. 256, à propos de NK9) n'est plus citée. |
| VT-13 | pour information | retenu | « Pièces » | « (EX-01, EX-02, EX-15, EX-22 à EX-24) ». |
| VT-14 | pour information | retenu, avec une donnée neuve | § 9, nœud 11 | La session a cherché de nouveau le 15 octobre vers 13:00 UTC (deux recherches sur le web, par titre puis par auteurs) : seule répond la page de conférence (`neurips.cc/virtual/2026/168176`), sans PDF ni version arXiv. Cette recherche est la dernière consignée. |
| VT-15 | pour information | retenu | § 0 | Daté à l'heure : « au 15 octobre à 11:56 UTC (R-182), ni à la rédaction de cette v3 ». |
| VT-16 | pour information | retenu | § 9, nœud 4 | « La v1 confiait la rédaction des cellules de PA-1 à un sous-agent, en routine (elle soumettait déjà à Lazar les textes de PA-5) ». |
| VT-17 | pour information | retenu | § 9, nœud 14 | « Par le retrait prévu par R-173, à écrire » ; `travail/correspondance.md` nommé à part (version de travail de `correspondance-v1.md`). |
| VT-18 | pour information | retenu | § 9, nœud 6 | « Volet attaque de NK5, y compris comme facteur de PA-5 ». |
| VT-19 | pour information | retenu | `registres/etat.md` | La ligne du dossier sous « Documents pour les évaluateurs » dit : aucune diffusion sans GO (DI-26). |
| VT-20 | pour information | retenu | § 2 | « 138/200 sous la direction douleur ». |

## 2. Points que la vérification n'a pas pu vérifier

- **Demandes de fusion n° 9 et n° 10** : lues par la session le 15 octobre par l'interface du dépôt distant : n° 9 = `canal/programme-k-n04` (`f9b6557`), n° 10 = `canal/programme-conv-n05` (`035d668`), n° 11 = `canal/session-depot-n01`, n° 12 = `passation/session-13-v1` (fermée, fusionnée dans `main` par `b5903d7`). La v2 et la v3 sont justes sur ce point.
- **Aucune instruction au-delà du n° 02** : la session a listé les branches du dépôt distant le 15 octobre vers 12:30 UTC (aucune branche `canal/` nouvelle depuis le 15 octobre 03:54 UTC) et relu l'en-tête des messages n° 03, n° 04 et n° 05 de programme-conv : aucun ne porte « INSTRUCTION ».
- **Demande des contre-lectures par Lazar le 15 octobre** : message de Lazar à la reprise de la session 14 (point 5) ; consignée par la ligne de registre qui accompagne cette v3.
- **EX-14, total de programme-k** : la source (`programme-k-coercition-v1.md` l. 474) écrit « Hors K11 et K13, le total tient en 25 à 39 heures de carte » puis « Les greffes de phase 0 pèsent 1,7 à 2,6 heures », sans dire si le total les comprend. La correction de EX-14 (« greffes de phase 0 comprises ») allait au-delà de la source : la v3 écrit que la source ne le dit pas, et donne les deux poids de greffes (environ 1,5 heure pour programme-conv, 1,7 à 2,6 heures pour programme-k).
- **Branche distante `donnees/t05/…`** : relevée par la session sur le dépôt distant (`git ls-remote`, puis récupération de la seule branche, 15 octobre vers 12:35 UTC).
