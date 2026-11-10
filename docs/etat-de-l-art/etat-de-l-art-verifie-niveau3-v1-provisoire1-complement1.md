# État de l'art vérifié — niveau 3 — complément 1 à la version provisoire 1

Date : 2026-11-10, vers 11:17 UTC (heure relevée par `date -u`). Session fille `session_01QPDgKefT7L1TvJMZ4BiBNb`.

La version provisoire 1 (`etat-de-l-art-verifie-niveau3-v1-provisoire1.md`, `8adb561d…`) est scellée et ne se réécrit
pas. Ce complément porte ce qui est arrivé après son scellement : le rapport C9 de cette session
(`niveau3-v1/rapports/rapport-C9-pieces-neuves-papiers-C-B-v1.md`, `23ec1f6e…`) et trois rapports de la session sœur à
réseau ouvert (branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `9f648c1d`, dossier
`docs/sources/lecture-pdf-niveau3/`) : `rapport-lot7B-collusion-papier-B-v1.md` (`bf9b6af8…`),
`rapport-lot7C-juges-papier-C-v1.md` (`2b03ede0…`), `rapport-lot7D-delegation-H9-v1.md` (`9f4c3b94…`). Les verdicts de
la sœur sont repris de ses messages, pages comprises, **sans relecture de ses rapports ni des PDF par cette session** :
l'instance suivante les contrôlera sur ses rapports avant la version finale.

**Là où ce complément et la version provisoire 1 diffèrent, ce complément prévaut.** Rien n'est occupé en entier ;
aucune hypothèse n'est modifiée.

## 1. Verdicts qui changent

| énoncé | provisoire 1 | maintenant | par qui, où |
|---|---|---|---|
| **H9** | occupée en partie, suspendu | **occupée en partie sur le cœur de l'énoncé — collision, nœud** ; la réserve d'antériorité de N-035 est confirmée | MasDrift 2608.07556 v3, p. 1-3, 5-8, 14, 18-19, 21-25 ; Sun et collègues 2608.24569 v2, p. 1, 3-7, 13-16 (lot 7-D). Contre-indice sur la prédiction : 88,2 % des pertes au premier relais (MasDrift, p. 6, 23), pas de décroissance régulière. Le bras « moniteur à chaque passage » n'existe que comme concept (2602.11865, p. 16 ; C9) |
| **Statistique de population** | spatio-temporel occupé en partie en boîte noire | **occupée en partie sur états internes — collision, nœud** ; déclencheur de bascule à examiner par Lazar | 2611.02153 v1 (J-PACT), p. 4, 6-9 : score de paire sur représentations internes, cumulé sur les tours, sur NARCBench ; sans sonde, 4 agents, sans garantie. 2611.10620 v1, p. 11-12, 21 : grille temps × agents, alarme à seuil conforme ; forme posée, aucun résultat pour la somme cumulée, pas de test toujours valide (lot 7-B) |
| **H8** | prémisse occupée, prédiction libre sous réserve | prémisse **occupée de plus près** ; prédiction toujours non trouvée | 2611.10620, p. 15, 19 (lot 7-B) |
| **H3** | boîte noire occupée | boîte noire renforcée | 2610.24052, p. 5 (lot 7-B) |
| **H7** | occupée en partie | renforcée | 2609.03035 v2 (rappels changés de la v1 à la v2, sans explication ; lot 7-B) ; STACK 2506.24068, p. 5, 10, 24 (C9) |
| **HC5** | occupée en partie | **occupée en partie, davantage** | 2610.29178, p. 1, 12, 14-16, 35 : transfert des tromperies entre juges, aucune sonde (lot 7-C) |
| **HC6** | libre | **occupée en partie, au niveau de l'item** | 2608.12645, p. 6-8, 10, 12 (lot 7-C) |
| **HC1** | occupée en partie | inchangé ; **deux contre-indices de plus** ; porte GC toujours non déclenchée | 2606.05384, p. 2, 5 : les juges se renversent (19,4 %) mais pas vers la cible nommée (écart signé −0,018), test binaire sur deux juges (C9) ; contre-indice sur la prédiction 3 de N-005 : 2608.12645, p. 9 (lot 7-C) |
| **HC4** | libre | pièce revendiquée libre, **prémisse entamée** (lettre de N-013, « le contexte seul n'y suffit pas ») | 2608.21664, p. 6-7 : une consigne en langage naturel fait tomber une sonde linéaire à 5-21 % de détection à 1 % de faux positifs ; 2602.00750 : suffixe dans le contenu, lecture des poids sans écriture, cinq sondes du lecteur évadées ; côté juge, STACK p. 8, 9, 21 : 507 heures de processeur graphique pour 71 % (C9) ; 2602.08877, p. 17, 18 (lot 7-C) |
| **H5** | occupée en partie | davantage | matrice de co-défaillance entre sondes, hors attaque : 2604.13386, p. 3, 5 ; gain de la diversité « minimal » sous pression : 2510.21531, p. 1, 9 (C9) |

## 2. Phrases pour le jury, mises à jour

- **H9** : « La perte d'une contrainte au passage entre agents est mesurée par d'autres depuis août 2026, et elle se
  produit surtout au premier relais. Nous n'en revendiquons plus la mesure ; il nous reste le bras avec moniteur à
  chaque passage, s'il tient à la lecture. »
- **Papier B** : « Deux prépublications de novembre 2026 posent un score sur les états internes d'agents à modèle
  partagé, cumulé sur les tours. Aucune ne donne un test toujours valide ni un résultat pour la somme cumulée ; c'est ce
  qui reste, et c'est étroit. »
- **HC4** : « Deux travaux montrent qu'un contenu ou une consigne peut déplacer une sonde sans écrire dans les poids. La
  comparaison de coût avec un juge n'est pas publiée ; notre prémisse, elle, est contestée. »
- **HC1** : « Un test binaire de notre prédiction centrale existe et il est négatif, sur deux juges. »

## 3. Corrections de faits repris des pistes de moteur

- « Red-Teaming Auto Mode » (2609.19587 au dépôt) : la session sœur date le billet du 22 octobre 2026 ; le rapport C5
  écrit 27 septembre d'après le PDF. **À réconcilier.**
- « What the Monitor Saw » : communication d'atelier de NeurIPS 2026, sans identifiant arXiv, PDF non obtenu.
- Le billet sur la « dilution » des sondes est « Trusted monitoring, but with deception probes » (juillet 2025).
- Livre blanc du SANS Institute : résumé seul ; il annonce 0 % en topologie superviseur et sous-agent (signe contraire
  possible pour H9).

## 4. Reste, pour l'instance suivante

1. Contrôler ce complément contre les rapports 7-B, 7-C, 7-D de la sœur, puis écrire la version finale
   `etat-de-l-art-verifie-niveau3-v1.md`.
2. Lots de la sœur non rendus à cette heure : 3-A, 2-A, 2-B (billets), 4-A, 4-B, 10-A, 12. Lot 8 versé mais **non lu**
   (13 PDF), dont Koning 2310.01153 (invariance de groupe par e-valeurs : à confronter à l'unification temps et agents
   du théorème), Ramdas et collègues 2102.00630, Vovk 1906.09256, 2609.15994, 2604.15384, 2610.31593.
3. À prendre à la main (accès refusé aux sessions) : « What the Monitor Saw » (OpenReview `s47MeQFSVN`) ; Ramtin et
   collègues (HAL `hal-04744798`) ; « When Monitors Fail, the Model Still Knows » (OpenReview `eckQoUDCSm`).
4. Nœuds à porter à Lazar, en plus des six de la version provisoire 1 : H9 (repli (b) de N-035) ; statistique de
   population et déclencheur de bascule ; lettre de N-013 pour HC4 ; prédiction 1 de HC1.
