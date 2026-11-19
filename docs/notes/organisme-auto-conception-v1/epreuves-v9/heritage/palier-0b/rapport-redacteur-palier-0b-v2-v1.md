# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 2 — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Rendu le 2026-11-19T16:52Z (`date -u`), le texte ayant été fini d'écrire à 16:51Z.
- Mandat : `mandat-redacteur-preenregistrement-palier-0b-v2-v1.md` (`311a2272c3bc5fc56c4868e3f0a02f4790f289912a6bd75227c53884d4ac7f8e`), empreinte vérifiée avant de commencer. Toutes les empreintes des pièces citées par le mandat ont été vérifiées sur disque (version 1 `a7189bbb…`, contre-lecture `127aa59f…`, mandat de la version 1 `e8eff361…`, plan v5 `9085bbe9…`, devis v5 `30c87fa6…`). `main` lu au commit `0bf0a3b0`, dont `2ec5da6c` est un ancêtre ; lignes `GO-2026-11-19-71`, `-75`, `-76` et `-77` lues.
- Sur processeur seul : aucun appel à un fournisseur de modèles, aucune dépense, aucun commit, aucune poussée, aucune écriture dans le dépôt, aucun tirage, aucune simulation. **Aucun refus d'outil.** Non lus : aucune carte, rien sous `archives-reponses-modeles/`, aucun dossier interdit.

## 1. Fichiers rendus (bloc-notes, dossier `redacteur-palier-0b-v2/`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v2.md` | `0a80a1adac833a3858754855f09bc420e569f2aeeb8c62e7cb0630bd4677becf` |
| `calcul_ordres_de_grandeur_palier_0b_v2.py` (analytique, sans tirage) | `470f3385aa2c21b10c3e50eab769599c0963a4d1799a45ac23074151f5e7dc13` |
| `calcul-ordres-de-grandeur-palier-0b-v2.json` (joué deux fois, sorties identiques à l'octet ; tous les champs de la version 1 y sont égaux) | `b97ed1f15361179252cdb4cf3a8fc546a53aea3b04d2c38b53adfbf002db9083` |
| `appliquer_corrections_v2.py` (65 remplacements exacts sur la version 1, chacun trouvé une seule fois) | `bd947b1795752b1a15f3156e18ccd965153d44f98e006afb98f218dc7c04d446` |
| `queue-v2.md` (réserves 12 à 16 et annexe E, ajoutées à la fin) | `90ea7fda4917d9e26fafcdecf05d0376912748f17b423beedb128f55b1844aef` |
| `differentiel-v1-v2.diff` (55 lignes de la version 1 changées) | `20e4011e7eb52391f96b6d6ab710e8be7976816cc16c3e0e4ae6fd12e43a5fd7` |
| `rapport-redacteur-palier-0b-v2-v1.md` | compagnon `.sha256` à côté |

La version 1 est intacte (R12). La version 2 passe le validateur du gabarit à la même remarque près, voulue : la section « Contre-lecture » n'a pas encore ses deux empreintes, puisque la vérification des corrections reste à faire.

## 2. Les onze corrections, une par une

| n° | où, dans la version 2 | comment |
|---|---|---|
| 1 (majeure) | M10 ; pronostic 6 | part = D / (D + max(I, 0)), mots du contre-lecteur ; I rapporté à part ; pronostic : « la part vaut un » |
| 2 (majeure) | M7 ; S7 ; B7 (ligne du lecteur, réglage, « Le repli du point 7 ») ; famille D ; valeurs gelées ; pronostic 7 ; réserve 12 | nombre fixe K de paires par génération, le même au repli ; R dit propriété du banc ; part des entrées gardées et facteur d'enrichissement rapportés ; ligne « tenue sous le repli » retirée, sans objet par construction. **De moi** : la plage de K (0 à 256) ; le pronostic du point 7 récrit (R sous 0,3 au lieu de 0,3 à 0,8), parce que la mécanique a changé |
| 3 | C1, C4 ; valeurs gelées ; « Comparaisons multiples » | règle du contre-lecteur. Le nombre de cases est écrit en chiffres : 72 pour C1 (douze nombres, deux doses, trois taux d'échec) et 72 pour C4 (douze nombres, deux sourds, trois taux, par la correction 7) ; échec à 5 236 rejets ou plus sur 100 000. Je n'emploie pas la lettre K ici, prise par la correction 2 |
| 4 | B2 ; M12 ; S8 (i) ; B7 (criblage) ; hypothèse de travail (iii) | classe tirée une fois par loi et par monde ; échec de l'expérimentateur par tentative |
| 5 | B9, gardes 23 à 26 ; annexe C | les quatre gardes ; le comparateur redonne la table du palier 0a. **Deux précisions de moi** : l'artefact de la garde 23 divise par deux la fréquence de « tient » des lois vraies et se lit sur le bras 3 du lecteur (M1 ne dépend de cette fréquence que là) ; la garde 26 plante des comptes (500, 501, 5 235, 5 236), non un taux de 0,055, qui n'arrêterait que 986 fois sur 1 000 |
| 6 | B4 ; garde 11 ; ordre des opérations, 6 bis | champ nommé : `enonce` (à confirmer au code) ; part de données gelée ; classement écrit par l'enveloppe ; 6 bis inséré. J'ai retiré « hypothèse » de la liste des textes neutres, puisque `enonce` porte la description |
| 7 | table des critères ; définition de m | taux d'échec écrits pour C3, C4, C5 et m |
| 8 | M9 ; B7 (réglage) | jumelles à l'étalonnage seulement ; écart-type gelé au fichier des réglages |
| 9 | marges du générateur | « ni les lois vraies des fausses », sur la forme écrite des lois de la clé |
| 10 | annexe C | phrase du contre-lecteur ; l'essai de forme mesure aussi le temps de calcul |
| 11 | B8 ; famille B ; ce qui est rapporté ; réserve 8 | « sans effet planté » ; part des tirages où l'autre contraste passe la première marche, rapportée par case |
| forme | critères de lecture ; annexe B ; B6 ; B7 ; annexe C | les sept points appliqués ; l'heure de rendu est juste dans ce rapport-ci, celui de la version 1 n'est pas réécrit |

## 3. Les trois décisions de Lazar (`GO-2026-11-19-77`)

Portées dans une table à part, à la section « Hypothèse ». Décision 1 : doublure ici, lecteur réel au seul palier 1, aucune dépense engagée par ce texte. Décision 2 : la phrase « servir un registre tenu, forme comprise » est gelée aux critères de lecture. Décision 3 : la forme imposée est dite forme des paliers payants ; les deux phrases du contre-lecteur sont en B4, avec ce que cela change : rien dans le dessin, `GO-2026-11-19-75` n'est pas rouvert ; la liste de l'expérimentateur garde la description à cet étage ; la garde 11 est éprouvée sur les deux listes ; le taux d'échec de 0,25 n'est pas changé. **Je n'ai pas réduit la liste à l'engagement seul** : c'est la décision B ci-dessous.

## 4. Les deux ajouts

**Bras de diagnostic « registre d'une autre source »** (B7 bis, M14, famille H, garde 27), sans critère. Le plan ne dit pas quel registre est remplacé ; j'en joue deux lectures. Le bras 4a (registre **hérité** d'une autre source, puis tenu) est la lettre du plan. Mais contre le suiveur à la lettre il ne peut rien dire de la tenue : à la génération finale, les bras 2, 3 et 4a servent tous un registre non vide, et la continuation y lit son propre registre tenu. J'ai donc ajouté le bras 4b (registre **tenu** par une autre source, servi à la place du sien), seul à pouvoir séparer la présence du contenu pour la tenue. **Le bras 4b est de moi, non du plan** : la mère peut le rayer d'un mot, le reste tient sans lui.

**Puissance du seul contraste de l'héritage** (M13, S9), sans critère, sur les mêmes tirages, lue aussi à 6, 7, 8 et 9 sources. **Seuil chiffré de « beaucoup plus de sources »** : la condition du devis est remplie si le n des deux contrastes dépasse celui du seul contraste **d'au moins 8 sources et d'au moins une fois et demie**. Huit sources : le devis a déjà pesé un écart de six (5 280 USD) et recommandé deux contrastes quand même ; huit font 7 040 USD. Une fois et demie : le prix attendu de la procédure de Holm est d'un rapport de 1,21 (9,95 sources contre 8,22). Si les deux contrastes ne sont atteints nulle part jusqu'à 48 : remplie quand le seul contraste l'est à 32 ou moins. Remplie : la mère repose le nœud 4 à Lazar ; sinon rien ne change. La décision du nœud 4 n'est pas touchée.

## 5. Information pour Lazar, sans décision

Le suiveur de forme répond à la **taille** du registre servi, non à sa seule présence. C'est un écart à la lettre du plan, nécessaire : à la génération finale les bras 2 et 3 ont tous deux un registre non vide, et le suiveur du plan n'aurait aucun écart d'héritage à montrer à la règle de validité ; l'étage s'arrêterait. Aucun effet sur une hypothèse ni sur une revendication. Le suiveur à la lettre est gardé à côté, sans critère.

## 6. Ce que je n'ai pas pu faire, ce qui reste ouvert

- La vérification des corrections par le même contre-lecteur ; le texte n'est pas scellable avant elle, ni avant l'erratum du commit du code.
- Je n'ai toujours pas lu le code de l'organisme (absent du conteneur) : le champ `enonce` et la composition par sous-population restent à confirmer par le développeur.
- La plage de K, le décalage de la garde 23 et le seuil de S9 sont des valeurs de rédacteur, sans appui mesuré.
- Rien ne dit que la taille de référence est atteignable avec K à la dose 0,25 ; la règle « non atteignable » et la liste d'arrêt disent quoi faire.
- Aucun chiffre de la littérature relu sur PDF ; l'annexe D n'est pas changée.

## 7. Décisions pour Lazar

**Décision A — Le chiffre de « beaucoup plus de sources » convient-il ?**
Enjeu : il décide seulement si le nœud 4 (deux contrastes décisifs) est reposé à Lazar après le palier 0b ; il doit être fixé avant tout tirage.
- (a) Au moins 8 sources de plus et au moins une fois et demie (écrit). Avantage : au-delà de ce que le devis a déjà pesé et de ce que la procédure de Holm coûte d'ordinaire. Inconvénient : un écart de six sources ne rouvre rien.
- (b) Au moins 4 sources de plus. Avantage : rouvre plus tôt. Inconvénient : se déclenche sur le seul écart des planchers (dix contre six), sans fait neuf.
- (c) Un montant, par exemple 10 000 USD. Avantage : parle en dépense. Inconvénient : dépend de la composition, non tranchée.
Recommandation : (a), confiance 0,6. Défaut sous 48 heures : (a).

**Décision B — Aux paliers payants, l'expérimentateur reçoit-il l'engagement seul ?**
Enjeu : avec la forme imposée, la loi est dans le texte du test ; la description bornée n'a plus de raison d'être servie et reste un canal du proposeur vers l'expérimentateur. Le plan (§ 3.0) permet de la retirer au préenregistrement. L'expérimentateur modèle reste gardé (`GO-2026-11-19-75`), avec un script fixe à lancer.
- (a) Engagement seul dès le palier 1. Avantage : un canal fermé, sans coût ; la garde est déjà éprouvée sur cette liste. Inconvénient : écart à la valeur proposée par le plan.
- (b) Engagement et description, comme écrit ici. Avantage : lettre du plan. Inconvénient : un canal sans fonction.
Recommandation : (a), confiance 0,65. Défaut sous 48 heures : (a), pour le seul préenregistrement court du palier 1.

**Pour la mère, sans décision de Lazar** : garder ou rayer le bras 4b (§ 4) ; faire vérifier les corrections par le même contre-lecteur, avec les sept points listés à la section « Contre-lecture » du texte.
