# Devis — lecture de fin de la colonne « matière première » de la course « nouvelles attaques », sur une ligne à part — v1

- **Nature** : pièce décisive (classe A), devis. **Non scellé, non contre-lu.** Il ne lance rien et ne dépense rien.
- **Auteur** : concepteur neuf, modèle F ; 2026-11-21, après 11:40Z. Processeur seul. Sur GO-2026-11-21-41 ; mandat `fadb3ab5…`.
- **Ce qu'il chiffre** : les huit appels des deux juges de la course à la lecture de fin (additif `additif-matiere-premiere-preenregistrement-court-v9-v1.md`, § 5). Rien d'autre ne coûte d'appel.
- **Hors des 570 USD de la course et de son plafond total de 576,05 USD** (préenregistrement court v9, `864f39a7…`, section « Seuil ») : ce devis ne les touche pas, et rien de lui n'est compté dans les parts des clés de la course.

## 0. Verdict

| | montant |
|---|---|
| cas bas | **0,29 USD** |
| cas haut | **4,48 USD** |
| pire | **16,00 USD** |
| **plafond d'arrêt de la ligne** | **16,00 USD** : 8,00 sur la clé Minuit (juge de l'espèce 3), 8,00 sur le deuxième relais (juge de l'espèce 1) |

**Les deux tarifs des juges ne sont écrits dans aucune pièce lue : ils sont à relever.** Les trois cas sont donc calculés sur des repères, non sur des tarifs relevés ; seul le plafond est ferme, parce qu'il est tenu par les bornes de la requête et par le relais à coût borné, quel que soit le tarif. **Les tailles des trois réponses brutes sont à relever aussi**, tailles seules, sans les ouvrir.

**Ligne de GO à demander à Lazar**, après la clôture des trois générations : « Lecture de fin de la colonne "matière première" de la course "nouvelles attaques" : interrupteur `colonne_matiere_premiere` à l'état 2, registre servi `3bcb94e6…` ; ligne de calcul à part de **16,00 USD au plus**, 8,00 sur Minuit et 8,00 sur le deuxième relais, hors des 570 USD de la course ; huit appels, aucun relancé. » Aucun défaut : sans mot, l'état 1 vaut et rien n'est dépensé.

## 1. Sources de chaque chiffre

| n° | chiffre | source | empreinte |
|---|---|---|---|
| E1 | deux juges ; trois réponses brutes ; routage : juge de l'espèce 3 sur Minuit, juge de l'espèce 1 sur le deuxième relais ; ligne à part | conception du véhicule v5, § 2.14 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` |
| E2 | un appel témoin par juge ; requête de 120 000 octets au plus ; sortie de 16 000 jetons au plus | additif, § 5 et § 6 : valeurs du concepteur | compagnon de l'additif |
| E3 | compte des jetons : un par octet au pire, 2,5 octets par jeton au bas | devis v6 de la course, § 4, table des sondes | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` |
| E4 | repère de tarif 2 et 10 USD par million de jetons, entrée et sortie, « non relu » ; il est noté pour une autre espèce | devis v6, § 2 et ligne S9 | même |
| E5 | repères de tarif 4 et 20, et 10 et 50 « en borne haute », USD par million | note d'arbitrage, point 2 | `44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06` |
| E6 | à la course v9 : juges 6,86 et 2,41 USD pour 94 appels chacun (lu dans le devis v6, ligne S1, non à sa source) | devis v6, § 1 | même que E3 |
| E7 | tailles de 20 000 et 60 000 octets par requête aux cas bas et haut | **règle du concepteur, sans mesure** : à relever | — |

Aucun de E4 et E5 n'est dit être le tarif d'un juge : aucune pièce lue n'écrit le tarif du relais de Minuit ni du deuxième relais.

## 2. Le calcul

Programme `calcul_devis_lecture_de_fin_matiere_premiere_v1.py` (`aa777c12145ab896b523c5f3dd5a004b5a242f592d2252939e04c91051cb8862`), arithmétique décimale seule ; entrées `entrees-devis-lecture-de-fin-matiere-premiere-v1.json` (`cea4bc382a0064d5e171e9726057abfa422d59e936dc945b5e5be15f41a293cc`) ; sortie `calcul-devis-lecture-de-fin-matiere-premiere-v1.json` (`e42246a2358875e98b24f2faebc8e30aff398168faa47351c6df4384b39ccc65`). **Joué deux fois, `cmp` muet.** Rejeu : `python3 -I PROGRAMME ENTREES SORTIE`, Python 3.13.18.

Coût d'un appel = jetons d'entrée × tarif d'entrée + jetons de sortie × tarif de sortie. Huit appels : par juge, trois réponses brutes et un appel témoin, compté à la taille d'un appel réel.

| cas | octets par requête | octets par jeton | jetons de sortie | tarif (entrée ; sortie) | par appel | par juge | total |
|---|---|---|---|---|---|---|---|
| bas | 20 000 | 2,5 | 2 000 | 2 ; 10 | 0,036 | 0,144 | 0,288, soit **0,29** |
| haut | 60 000 | 1 | 16 000 | 4 ; 20 | 0,56 | 2,24 | **4,48** |
| pire | 120 000 (la borne) | 1 | 16 000 (la borne) | 10 ; 50 | 2,00 | 8,00 | **16,00** |

Au pire des tailles, selon le repère de tarif : 3,20 USD à 2 et 10 ; 6,40 à 4 et 20 ; 16,00 à 10 et 50 (champ `grille_par_repere_de_tarif`).

Repère mesuré, qui n'entre dans aucun total : à la course v9, un appel de juge sur une fiche a coûté 0,0730 USD (espèce 3) et 0,0256 USD (espèce 1) (E6 ; champ `reperes_mesures_qui_n_entrent_dans_aucun_total`). Un appel de fin porte un texte bien plus long qu'une fiche : le cas bas, 0,036 par appel, est sans doute trop bas pour l'espèce 3.

## 3. Plafond d'arrêt, et ce qui le tient

- **Plafond de la ligne : 16,00 USD**, 8,00 par juge ; réservé avant le premier appel.
- **Avant chaque appel** : le cumul de la ligne, plus le pire de l'appel à lancer (2,00 USD), ne dépasse pas le plafond ; sinon l'appel ne part pas, arrêt nommé, aucune bascule vers une autre clé (additif, § 9, arrêt C).
- **Si le tarif relevé dépasse 10 et 50** : le pire d'un appel aux bornes dépasse 2,00 USD. Alors, ou bien la mère abaisse la borne de sortie pour que le pire tienne (16 000 jetons valent 0,80 USD au repère), et l'écrit avant le mot de Lazar ; ou bien une ligne neuve se demande. Le plafond n'est jamais relevé en silence.
- **Si une réponse brute fait plus de 120 000 octets, texte servi et liste compris** : sa requête ne part pas (arrêt D) ; la borne n'est relevée que par une version neuve de l'additif.
- **Le reste des clés.** La ligne n'est pas comptée dans les parts de la course, mais elle se paie sur les mêmes clés. Minuit : sa part de course est de 162,56 USD, son cas haut de 126,06 (V9, « Répartition retenue ») ; le reste du jour est relevé après la course et doit couvrir 8,00 USD, sinon le départ est refusé. Deuxième relais : son solde est « inconnu : aucune borne, aucun relevé » au devis v6, § 6 ; la dispense de lecture de solde est redite ou refusée par la mère pour cette ligne.

## 4. Ce qui n'est pas chiffré

1. **Les deux lecteurs d'antériorité** : sessions à part ; du temps de sessions, zéro dollar d'appels d'interface si ce sont des sessions du compte (devis v6, § 7, points 2 et 7). Leur charge croît de 24 visées et 2 témoins, au même périmètre que pour une fiche.
2. **Le lot 10 b** (programme de lecture de fin, table de routage, table de comparaison) : de l'ordre de 2 heures de développeur, zéro dollar (conception v5, § 8) ; sa contre-lecture.
3. **La contre-lecture de l'additif et de ce devis**, la vérification des corrections.
4. **L'affinage par l'organisme** (conception v5, § 2.14, option (b)) : hors de ce devis ; son propre devis s'il est voulu.
5. **L'épreuve des visées « sur devis »** qu'annonce GO-2026-11-21-19 : hors de ce devis.

## 5. Ce qui ferait changer ce devis

Le relevé des deux tarifs et des trois tailles : les cas bas et haut se recalculent par le même programme, sur un fichier d'entrées d'une version neuve ; le plafond ne monte que par un mot de Lazar. Une garde de motifs qui refuse les trois requêtes (additif, § 10, valeur 4) : la ligne tombe à zéro, et la lecture de fin se fait sans l'avis des juges, ce que l'additif permet.

## 6. Relevé de méthode

**Chaîne de raisonnement.**

1. Seuls les deux juges passent par un appel payant ; les lecteurs sont des sessions (E1 ; devis v6 `d825cb31…`, § 7).
2. Huit appels : deux juges, trois textes et un témoin chacun (E1, E2).
3. Le coût d'un appel se borne par la taille de la requête, la borne de sortie et le tarif (E2, E3).
4. Supposé : les tarifs des deux relais des juges ne dépassent pas 10 et 50 USD par million. Aucune pièce lue ne les écrit.
5. Supposé : les tailles des cas bas et haut (E7).
6. Total au pire : 8 × (120 000 × 10 + 16 000 × 50) / 1 000 000 = 16,00 USD (calcul rejoué, `e42246a2…`).
7. Le plafond est tenu par l'arrêt C et le relais à coût borné, non par les pas 4 et 5 (additif, § 9).

**Objets de contrôle.** Écrits au fichier d'entrées avant le premier jeu. Faux par construction : tarif de 15 et 75, attendu à la main 8 × (1,80 + 1,20) = 24,00 USD, « ne tient pas » ; requête de 120 001 octets au tarif le plus bas, « ne tient pas » malgré 0,93 USD. Vrai par construction : le pire, 16,00 USD, égal au plafond, « tient ». Rendu : les trois conformes (champ `objets_de_controle`) ; le programme n'écrit aucune sortie si l'un diffère.

**Premier pas non justifié.** Le pas 4. Le justifierait : le relevé du tarif de chaque relais, sur la page du fournisseur ou au journal de la course.

**Mode d'échec affecté.** Sans objet : je suis concepteur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.** Le devis v6 de la course n'écrit aucun tarif par jeton pour les juges, seulement des coûts par rôle : un devis au jeton n'est possible pour eux qu'après un relevé. Non poursuivi.

**Évaluateur et conseil.** Jugé par le contre-lecteur O, qui rejoue le programme et refait les trois totaux à la main. Par où il pourrait passer sans le mériter : les cas bas et haut reposent sur des tailles que personne n'a mesurées ; seul le plafond est défendable. Conseil : vérifier d'abord que l'arrêt C lit bien le plafond de cette ligne et non les parts de la course.

— concepteur neuf, modèle F
