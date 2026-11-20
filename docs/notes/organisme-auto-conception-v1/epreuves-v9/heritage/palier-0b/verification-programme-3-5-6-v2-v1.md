# Vérification différentielle du programme des étapes 3 à 6, version 2 — v1

Vérificateur neuf, modèle S (a vérifié la v1, `5dae3b94…`). 2026-11-20. Rien n'est lancé, aucune graine décisive, aucune écriture dans le dépôt.

## Verdict : **À corriger** (un point, un essai à ajouter ; le programme n'est pas à changer)

1. **Essai de chaîne affaibli : la valeur rendue par `lancer` n'est plus éprouvée nulle part** (§ 4). Correction : ajouter à `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` l'assertion sur le retour de `lancer` (`r["frequences"] == (chemin, empreinte)` et `r["reglages"]` de même, `r["manifestes"]` de clés 3 à 6), et, si possible, un essai de `main` sur ce cas planté (sortie standard : « fréquences gelées : chemin empreinte », « réglages gelés : chemin empreinte »).

Les points 1, 2, 4 et 5 de la demande sont conformes.

## 1. Empreintes
`env -C … sha256sum -c table-empreintes-programme-3-5-6-v2.txt` : 7 lignes, 7 OK (programme `1f04cb46…`, essais, rapport, deux différentiels, deux journaux).

## 2. Point 1 de la demande : la condition 5 — conforme
`liste_d_arret_point_5` (l. 82-97) et son appel (l. 229, 233-238), contre v13:428 (= v15:436, texte inchangé) : « la taille de référence n'est atteignable, pour un contraste, à aucune dose non nulle ; ou la force de référence du suiveur de forme n'est pas atteignable → arrêt ».
- Contraste de l'héritage = K du lecteur réglé pour l'héritage, contraste de la tenue = τ du lecteur réglé pour la tenue (B7) ; référence = taille 1 (`K.TAILLE_REFERENCE`) ; la condition est vraie si, pour l'un des deux, aucune des deux doses non nulles n'est atteignable ; ou si φ à la force 1 est non atteignable. Une cible absente compte comme non atteignable (ligne prudente). Les autres tailles et forces et γ ne comptent pas : à la lettre.
- Format des réglages : celui que rend la 2e valeur de `etape_6` (`reglages_pour_le_plan`, clés `(dose, taille)` et force, `None` si non atteignable) : vérifié dans `etapes.py`. Aucun calcul, aucune fonction neuve du paquet.
- Arrêt par `_arreter` existant : cause scellée, manifeste de l'étape 6 « arrêt » (empreinte du fichier des réglages inscrite à la configuration, fréquences aux gelés), programme arrêté. Le fichier des réglages déjà gelé reste, ce qui convient (l'erratum qui change les valeurs le reprend).

## 3. Point 2 : essais — présents et passants
Rejoués sur copie, code v6 copié (table `639335b9…`), `PYTHONPATH=src`, variables `HERITAGE_*` : **30 passés, 0 échoué (801 s)**, couche « essai-de-forme » seule. Présents : `test_v2_liste_d_arret_point_5_a_la_lettre` (cas sain, deux doses ou une seule par contraste ; artefacts K, τ, φ, K et τ, clé absente, autres tailles sans effet), `test_v2_point_5_artefact_…` (celui de ma v1), `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue`, et cinq essais `test_v2_arrets_nommes_de_l_etape_4` (les cinq classes que j'avais plantées, avec manifeste « arrêt » et sans résultat de l'étape 4). Ils couvrent la correction ; mes cinq cas de la v1 y sont repris.

## 4. Point 3 : l'assouplissement de l'essai de chaîne — il cache un défaut de couverture
La chaîne réduite réelle s'arrête au point 5 aux tailles d'essai (constat du rapport § 3, R4 : sans portée pour le palier ; je ne le lis pas non plus). L'essai admet donc « tenue » ou « arrêt par la seule cause du point 5 » et contrôle, dans le second cas, que seule l'étape 6 a un `arret.txt`, de cause scellée : l'assouplissement est borné, tout autre arrêt fait échouer l'essai ; ce n'est pas un trou en soi.
Mais le différentiel montre ce qui a été perdu : l'ancien essai lisait `r = PR.lancer(...)` puis `r["frequences"]`, `r["reglages"]` ; le nouveau n'utilise plus le retour (il relit les fichiers par chemin) et, quand la chaîne s'arrête, `lancer` ne retourne rien. Or `main` imprime ce retour (« fréquences gelées : chemin empreinte », « réglages gelés : … ») et c'est ce qu'on recopie dans la pièce de contrôle et passe aux programmes 6 bis–7 et 8–9 (ordre : chemin puis empreinte). **Preuve par défaut planté** : sur une copie, j'ai permuté `(chemin_f, sha_f)` en `(sha_f, chemin_f)` (et de même pour les réglages) dans le retour de `lancer` ; les 28 essais hors chaîne passent (le 29e, la chaîne, ne le voit plus). Le défaut ne serait vu par aucun essai de la v2 ; il l'était par l'essai de chaîne de la v1.
Exige-t-on une chaîne réduite qui va jusqu'à « tenue » par un autre réglage factice ? Non : le cas sain « tenue » est déjà joué (`…cas_sain_plante_la_chaine_finit_tenue`, étapes 3 et 4 et étape 6 remplacées par des fonctions rapides, rien de tiré), et chercher des tailles d'essai qui font passer une garde serait lire l'essai comme un résultat. Il suffit que cet essai planté contrôle le retour (correction ci-dessus).

## 5. Point 4 : différentiel v1 → v2 — conforme
`diff -u` v1 → v2 du programme : docstring (version 2, nom du fichier), classe `ArretListeDArretPoint5` et fonction `liste_d_arret_point_5`, la 2e valeur de `etape_6` gardée (`_, reglages, sha_r`), le bloc de la condition 5 avant la clôture de l'étape 6. Rien d'autre : couches, pièces, dossier, arrêts des étapes 3, 4, 5, `ARRETS`, `main` inchangés. Même constat sur le différentiel des essais : repris à l'identique hors la fixture de chaîne, les nouveaux essais et le nom du programme. Conforme au rapport.

## 6. Point 5 : silence n° 11 (point 5 lu à la fin de l'étape 6) — juste
Le point 5 porte sur la possibilité de planter l'effet de référence, que l'étalonnage de l'étape 6 est seul à décider ; le lire à sa fin évite de jouer les étapes 6 bis à 9 sur un banc qui ne sait pas planter l'effet de référence, et l'arrêt reste « avant tout tirage décisif ». À inscrire en v15 (l'étape, et que le fichier des réglages reste gelé et inscrit au manifeste d'arrêt). Les silences n° 2 et 5 de la v1 restent à la mère, avec les recommandations de ma vérification.

## 7. Rappel pour la pièce de contrôle
Le programme exige l'empreinte de la v2 (`1f04cb46…`) dans la pièce de contrôle, à la place de celle de la v1.

## 8. Écarts à mon mandat
Aucun refus de permission, de classifieur ni de garde ; aucune liste de processus ni commande d'arrêt ; aucune écriture dans le dépôt.

Signé : vérificateur, modèle S.
