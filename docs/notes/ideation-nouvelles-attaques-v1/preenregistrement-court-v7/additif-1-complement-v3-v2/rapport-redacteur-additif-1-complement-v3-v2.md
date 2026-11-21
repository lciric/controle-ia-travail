# Rapport du rédacteur — additif 1 au complément de valeurs v3 (espèce 3 sur la clé Minuit) — v2

Rédacteur de l'additif 1 au complément v3, modèle F. Date (UTC) : 2026-11-21 ; relevé de `date -u` : 06:19:17Z, après les deux jeux portés, avant la passe de tenue. Rien n'est scellé ; rien n'est écrit dans le dépôt ; aucun commit ; aucun appel à un fournisseur ; aucune clé lue ; aucune dépense. Aucun refus de permission, de classifieur ou de garde. La v1 n'est pas touchée.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-1-complement-v3/v2/`.

## 1. Pièces reçues, vérifiées contre leur compagnon

Dossier C = `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-complement-v3-v1/contre-lecture-v1/`.

| pièce | empreinte | compagnon |
|---|---|---|
| C/`contre-lecture-additif-1-complement-v3-v1.md` (verdict « À corriger ») | `34ea5da0bea8984a22b73ddb74978d0edd4bfb44e2b59b82442a54c98238b2b2` | égale |
| C/`corrections-additif-1-complement-v3-v2.json` (dix remplacements) | `9d67cc4b7822bda19e42d717708623a9de3f1db03b831659eb6c6323365344fb` | égale |
| C/`essai-additif-corrige-v2.md` | `1c8cae2b733199e364baef4386d37412a9a11a41ffcf5f41b12842a3c853a1ee` | égale |
| C/`corrections-calcul-additif-1-complement-v3-v2.json` (un retrait) | `a4b7b1b75f178e47d24293663e15d9a8cb68737e4f82a68554725106902a8378` | égale |
| C/`essai-calcul-corrige.json` | `61ec2db091d98494e93ccd60e6f395f7f11d9cebaafedf49e04b4648b69a5c01` | égale |
| `/home/user/controle-ia-travail-organisme/scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | égale |

## 2. Ce qui est fait

1. **Jeu de l'additif, tel quel.** Copie de la v1 (`copie-additif-v1-avant-jeu.md`, `e5ec3a17…`, égale à la v1). Les dix ancres comptées avant l'appel, par `grep -c -F -e` : une occurrence chacune. Sortie de l'outil : `additif-1-complement-v3-v2-passe-1-jeu-tel-quel.md`, `1c8cae2b733199e364baef4386d37412a9a11a41ffcf5f41b12842a3c853a1ee`. `cmp` contre l'essai du contre-lecteur : **aucune différence**.
2. **Jeu du programme, tel quel.** Copie du programme v1 (`copie_calcul_v1_avant_jeu.py`, `d620b981…`, égale à la v1). L'ancre comptée : une occurrence. Sortie de l'outil : `calcul_additif_1_complement_v3_v2.py`, `9175f7960a98ca1f15d9722f51b9f94736d68231ce9728b4b0a306363843e133`, l'empreinte de l'essai du contre-lecteur. Joué par `python3 -B`, sortie redirigée vers `calcul-additif-1-complement-v3-v2.json`, `61ec2db091d98494e93ccd60e6f395f7f11d9cebaafedf49e04b4648b69a5c01`. `cmp` contre `essai-calcul-corrige.json` : **aucune différence**. Les neuf contrôles restent tenus.
3. **Passe de tenue**, par l'outil, jeu `tenue-additif-1-complement-v3-v2.json`, sept remplacements : le titre (« v1 » devient « v2 ») ; la ligne de date, qui garde l'heure de la v1 et ajoute celle de la v2 ; la ligne de version, ajoutée ; les deux lignes de la table des pièces (nom et empreinte du programme v2 et de sa sortie) ; au § 9, le nom et l'empreinte du programme v2, le nom et l'empreinte de sa sortie, et la commande de rejeu. Sortie : l'additif v2.
4. **Différentiels v1 → v2** : de l'additif, du programme, de la sortie du programme. Celui du programme et celui de sa sortie portent une ligne retirée chacun.

## 3. Aucun nombre ne change

Marge de Minuit 24,90 USD ; reste après les lignes à part 156,56 USD, soit 24,90 USD au-delà du cas haut de 131,66 USD ; Rigaud 25 USD, réserve 8,35 USD couverte ; troisième relais 17,01 USD ; somme des parts 439,59 USD. La sortie v2 ne diffère de la v1 que par la clé retirée, `rigaud.part_de_la_course_apres_l_additif_usd`.

## 4. Signalements

1. **Clé retirée** : aucune ligne de l'additif, en v1 comme en v2, ne la cite.
2. **Nom du programme v1** : la première passe le citait à trois lignes (deux lignes de la table des pièces, une au § 9, avec le nom de la sortie v1). La passe de tenue les a portées à la v2. Après elle, l'additif v2 ne cite plus ni le programme v1 ni sa sortie.
3. **Le programme v2 se dit encore « v1 »** : dans son en-tête (titre et ligne d'usage) et dans le champ `piece` de sa sortie. Je n'y ai pas touché : hors du jeu, et la sortie devait être égale à l'essai à l'octet.
4. **Statut et § 9 de l'additif v2 laissés tels quels** : le statut dit encore « non contre-lue », et le § 9 « Contre-lecture : à faire ». La ligne de version, juste au-dessus du statut, dit la contre-lecture et son verdict. Ces deux lignes sont hors des trois objets de la tenue demandée ; elles restent au traitement de la mère au scellement, ou à une passe qu'elle demanderait.
5. **Les empreintes des deux registres** données par l'additif (`44dabda6…`, `0f01e3d7…`) sont celles du commit `7487d273…` ; le contre-lecteur a lu un commit plus récent, sans changement des entrées citées, et ne les a pas recalculées. Inchangé.

## 5. Points laissés à la mère

Cinq, au § 8 de l'additif v2 : n° 2 (Rigaud dans la pièce de relevés et le véhicule), n° 3 (les 16,65 USD, pour information), n° 4 (ce que l'attestation du troisième relais doit dire), n° 5 (troisième relais sans recharge automatique mais avec un reste d'au moins 17,01 USD), n° 7 (rappel : répartition à confirmer par la contre-lecture du véhicule). **Les points 2, 4 et 5 restent non tranchés.** Les n° 1 et n° 6 sont tranchés par la lettre, par le jeu du contre-lecteur.

## 6. Écarts

1. **Noms des copies.** L'outil refuse d'écrire sur place et refuse une sortie qui existe. Les copies de la v1 portent donc des noms d'attente (`copie-additif-v1-avant-jeu.md`, `copie_calcul_v1_avant_jeu.py`), la première passe de l'additif un nom propre, et seule la sortie de la passe de tenue porte le nom `…-espece-3-sur-minuit-v2.md`. Le programme v2 porte son nom dès la sortie du jeu.
2. **Titre** : la passe de tenue change aussi « v1 » en « v2 » dans le titre, au-delà des trois objets nommés. La ligne de version le dit.
3. **Commandes simples hors de celles nommées** : `mkdir` du sous-dossier, `cp`, `diff -u` redirigé, `grep -c -F -e` et `grep -n -F -e` sur un fichier nommé, `cat` de plusieurs compagnons en un appel.
4. Le rapport et la table d'empreintes de la v1 ne sont pas refaits : la table de la v2 couvre le sous-dossier `v2/`.

— rédacteur de l'additif 1 au complément v3, modèle F
