# Vérification du devis v4 « serveur loué, palier 0b, essai 3 » — v1

**Verdict : À corriger.** Mes points de la v3 sont portés (quatre sur cinq sans réserve, l'ordre destruction/versement avec une réserve). Mais la v4 casse une chose : l'arithmétique de l'heure d'arrêt du gardien. « H0 + 94 h » est avant les 94,6 h du relevé le plus pessimiste, alors que la phrase dit « au-delà ».

Pièce vérifiée : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/devis-serveur-loue-palier-0b-essai-3-v4.md`, sha256 `64cdbd7bc30ed5fd1a62711bb0c2d1d113fa3fa7e77a0299cbf5f31fa9736185`. Bases : journal de tenue `bbfb4473…a8`, mesure `7605afc3…6d34`. Non vérifié : le prix de la cpx42 (aucun appel permis ; aucune pièce) ; `registres/go.md` non relu ; les chemins `sourd-egal/0.0/0` à `19` (hors de mon périmètre de liste ; seul leur nombre, 20, égale n = 20).

## Un point par ligne

| point | état | ligne de la v4 |
|---|---|---|
| 98 Go dit comme reste | **Porté** | § 1, « Place » : « un reste, non une mesure ; la place des étapes 5 et 6 et des archives n'est pas mesurée ». Recalcul : 320 − 218,6 − 3,4 = 98,0. |
| plus aucune « borne haute » | **Porté** | Recherche de « borne » : une seule occurrence, ligne 9, « non une borne établie ». Lignes 15, 20 et 42 de la v3 réécrites (« relevé le plus pessimiste » ; § 6 (c) : « 218,6 Go contre 38,7 Go libres »). |
| t3 au relevé | **Porté** | § 3 (relevé : « n, les fichiers, les octets alloués et t3 ») et § 6 (a) (« l'heure de dernière modification du manifeste de l'étape 3, t3 »). |
| voie de la racine sans accès déposé | **Porté** | § 6 (a) : copie de l'arbre `d7f949ac` du poste au serveur, « aucun accès au dépôt privé n'est déposé … le clonage depuis le serveur est écarté », contrôle du commit et de l'empreinte `1f04cb46…` avant départ. |
| ordre destruction/versement, trois heures fixes | **Porté, mais l'heure H0 + 94 h est fausse** | § 3 et § 5 : ordre sans ambiguïté (la destruction prime à H0 + 98 h). Défaut : voir pas 3. |

## Casse-t-elle autre chose ? Oui

**Cassé : le § 3, ligne 21.** « H0 + 94 h : arrêt de durée du gardien … **au-delà du relevé le plus pessimiste de l'étape 4 (94,6 h) si la mise en place prend moins de 4 h** ». Or 94 h est plus petit que 94,6 h, et la marche ne commence qu'après la mise en place : même avec une mise en place nulle, l'étape 3 (0,16 h) plus l'étape 4 au relevé le plus pessimiste (94,64 h) font 94,8 h, soit après H0 + 94 h. Dans ce cas l'étape 4 **ne finit jamais** ; la v4 dit l'inverse (« au-delà … si moins de 4 h ») et réserve « peut ne pas finir » au cas d'une mise en place longue. Le passage de 96 h (v3) à 94 h pour laisser 4 h de versement a supprimé la couverture du cas le plus pessimiste sans le dire.

## Relevé de méthode

### Chaîne de raisonnement

1. Durée de marche au relevé le plus pessimiste : étape 3 = 9 min 19,6 s (journal ligne 1, mesure ligne 3) = 0,155 h ; étape 4 = 525,8 × 648 / 1 = 340 718,4 s = 94,644 h (journal ligne 22). Total : 94,80 h, sans étapes 5, 6 ni garde 27 (hors mesure).
2. Fin du gardien : H0 + 94 h (§ 3 ligne 21 ; § 4 point 2). Marche débutée à H0 + m, m = durée de la mise en place ≥ 0. La marche disponible est 94 − m heures, au plus 94 h : inférieure aux 94,80 h du pas 1 pour tout m ≥ 0. Donc l'étape 4 ne se termine pas dans le cas le plus pessimiste, à aucune durée de mise en place.
3. Phrase de la v4 : « au-delà du relevé le plus pessimiste (94,6 h) si la mise en place prend moins de 4 h » : fausse d'après le pas 2. Elle serait vraie pour une heure d'arrêt de H0 + 98 h + m ou pour un relevé inférieur à 90 h. Pièce : v4, ligne 21.
4. Les cas favorables restent couverts : à n = 20 (10,7 h) ou 17,4 h, la marche tient largement dans 94 h. Le relevé à 6 h (§ 3, ligne 26) permet la décision. Le défaut est donc d'énoncé (une promesse fausse), non de sécurité : le coût est borné (pas 5).
5. Coût : 96 × 0,11436 = 10,97856 EUR ; × 1,25 = 13,7232 USD (« 10,98 » et « 13,73 », exacts) ; 98 × 0,11436 = 11,207 EUR ; × 1,25 = 14,009 USD (« 11,21 » et « 14,01 », exacts) ; plafond 15 USD = 12 EUR = 104,9 h. Heure entamée : si la destruction a lieu à H0 + 98 h plus quelques minutes, 99 h facturées : 99 × 0,11436 = 11,32 EUR = 14,15 USD ; sous 15 USD. Le plafond tient à condition que la destruction ait lieu avant H0 + 104 h (104 × 0,11436 × 1,25 = 14,87 USD ; 105 h donnent 15,01 USD, au-dessus).
6. Ordre des deux règles : § 5 : « en marche normale, destruction dès le versement prouvé » ; « à H0 + 98 h, la destruction prime » ; « écrit ce qui n'a pas été versé ». Conflit de v3 résolu. Réserve : le § 3 écrit « versement des sorties et des journaux » (ligne 22) ; la règle du complément n'archive l'étape 4 que si la place libre dépasse sa taille de 4 Go (complément 1 v3, « Tenue du lancement ») : dans le cas à 218,6 Go sur 320 Go, l'étape 4 ne serait pas archivée et ses sorties seraient détruites avec le serveur ; seuls les inventaires et compagnons seraient versés. La v4 doit dire « inventaires et compagnons », pas « sorties », ou dire ce qui est perdu.
7. Une heure fixe de destruction sans personne nommée : « celui qui a créé le serveur » (le poste local de Lazar) doit être présent à H0 + 98 h (quatre jours plus tard) ; aucune destruction automatique (assumé). Le plafond laisse 6,9 h de marge après H0 + 98 h (pas 5). Réserve inchangée par rapport à la v3, assumée dans la v4.
8. Doses du plan : `/home/user/palier-0b-racine/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v19.md`, ligne 208 : « doses de dépendance | 0 ; 0,25 ; 0,5 | celles du plan (§ 5) » : **vérifié**. La v4 le cite exactement.
9. « 38,7 Go libres » (§ 6 (c)) : le journal donne 38,36 Go libres à 17:31:47 (ligne 3) et 37,57 Go à 17:59:47 (ligne 32) ; 38,7 n'est pas une valeur du journal (le maximum lu est 39,12 Go, ligne 10). Écart de moins de 1 Go, sans effet sur la conclusion (218,6 ≫ 38,7), mais le chiffre n'a pas de pièce.

### Objets de contrôle

Mécanisme : le contrôle de cohérence des heures fixes (94 h d'arrêt, 98 h de destruction, 94,8 h de marche pessimiste). Objet où la conclusion « l'arrêt est au-delà du relevé le plus pessimiste » est fausse par construction : une mise en place nulle (m = 0), cas le plus favorable à l'énoncé ; prédiction avant : si l'énoncé est vrai, 94 h ≥ 94,8 h ; résultat : 94 < 94,8, la phrase est fausse même dans le cas le plus favorable. Objet vrai par construction : le cas de la mesure à n = 20 (10,7 h) : 94 h couvre (10,7 + 0,16 = 10,9 h) ; la v4 reste vraie pour lui.

### Premier pas non justifié

Le pas 1 en sa partie « étapes 5 et 6 et garde 27 hors mesure » : leur durée n'est pas mesurée ; ce qui la justifierait : une mesure ou une lecture du programme. Elle aggrave seulement le défaut du pas 3.

### Mode d'échec affecté

Les cinq points demandés, plus « la v4 casse-t-elle autre chose ». Réponse : l'heure H0 + 94 h et son commentaire (pas 2 et 3) ; en réserve : « sorties » contre « inventaires » (pas 6), le chiffre de 38,7 Go (pas 9).

### Trouvaille de côté

Si l'on veut couvrir le cas le plus pessimiste (94,8 h de marche plus mise en place, plus étapes 5 et 6), il faut un arrêt vers H0 + 100 h et une destruction vers H0 + 104 h : 104 × 0,11436 × 1,25 = 14,87 USD, sous 15 USD mais sans marge d'heure entamée (105 h : 15,01 USD). Le choix revient à la mère ; la rédaction honnête de la v4 est de dire que dans le cas le plus pessimiste l'étape 4 ne finit pas et que le relevé à 6 h sert à le savoir.

### Évaluateur et conseil

Ce qui me juge : la session mère. Mes témoins : recalculs à la main, concordants avec les chiffres de la v4 ; l'erreur trouvée est dans une comparaison de deux nombres que la v4 écrit elle-même. Je serais jugé bon sans le mériter en ne contrôlant que les chiffres isolés.

Corrections demandées : (a) § 3, ligne 21 : écrire que H0 + 94 h est **avant** le relevé le plus pessimiste de l'étape 4 (94,6 h, plus 0,16 h pour l'étape 3), que l'étape 4 ne finit donc pas dans ce cas quelle que soit la mise en place, et que le relevé à 6 h sert à le savoir ; ou déplacer les heures fixes et refaire le coût (pas 5) ; (b) § 3, ligne 22 : « inventaires et compagnons » au lieu de « sorties », ou dire que les sorties de l'étape 4 sont perdues à la destruction ; (c) § 6 (c) : remplacer ou sourcer les 38,7 Go.
