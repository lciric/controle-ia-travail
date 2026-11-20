# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 11 — note du rédacteur — v1

Ce que la version 11 change, ce qu'elle laisse en limite écrite, et ce qu'il faut regarder en premier.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : la vérification du code de la version 10 (`538f09c0…`) et ses pièces d'attaque ; **le brouillon 34, qui fait foi** (`0b6413d9d75a838f17aabf46ff714a34c5b086f939e44d6a864326a7e1b247a3`), et sa note (`b8619e79…`, partie 5) ; la vérification du brouillon 34 (`3350ab12…`, M-1 et M-2) ; les précisions de la session principale reçues pendant le tour.
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni appel de modèle ; aucun sous-agent ; aucune dépense. `registres/`, `.claude/`, le journal et `prereg/` non touchés. Rien de committé. Aucun fichier existant modifié : la version 10 et le programme du constat en version 3 répondent toujours à leur empreinte. La copie de sauvegarde du code inachevé n'a été ni ouverte ni touchée.
- **Le tour a été interrompu une fois** (limite du modèle), puis repris sur les mêmes fichiers.
- **Heure** : 2026-11-20, 00:50Z.

## 1. Fichiers

Tous neufs, tous scellés.

| fichier | empreinte |
|---|---|
| `src/controle_ia/organismes_discrets/analyse_bras_a_v11.py` | `ea948d4bef26c1ab25888ff92529c39265e79a6f2b32d8a91690b651d1b7f127` |
| `src/controle_ia/organismes_discrets/configuration_bras_a_v11.py` | `fd06e9429875a9cebe71a896adfeb88d37dcd432037797fece0cbaf0e9304227` |
| `src/controle_ia/organismes_discrets/graines_bras_a_v11.py` | `c1525322dc47918781750214cc6fe578cc003d851fd15a3cd21985a70c8bd68d` |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v11.py` | `23fc448322ea57c3f288518e0281e2f35c4d754877b5265575f8ca8284035e76` |
| `src/controle_ia/organismes_discrets/arrets_bras_a_v11.py` | `e464f10625f9cb3fb3968d1070db340a6751fb9a02408fe392d43f606049f24a` |
| `src/controle_ia/organismes_discrets/verdicts_bras_a_v11.py` | `3a465aed55ea825799adee3292a5fcdf6d7532ee27b53bfb90daf98e871e4396` |
| `src/controle_ia/organismes_discrets/permutation_etiquettes_bras_a_v11.py` | `51049cfe7c4a759be95e6d5b7755a03f65d7d9b3b689b64c630f795c6784c4ce` |
| `src/controle_ia/organismes_discrets/depots_bras_a_v11.py` | `0dd7851f42ce5e2895853fa822cb756b0450c32369cfdec8e00c9adab8aa2a5a` |
| `src/controle_ia/organismes_discrets/mesures_bras_a_v11.py` | `4ee1e49277dc3bd5c4d09ed523117eb753be42bfdbd6cddb1f60b3ed29ddf53c` |
| `scripts/constat_de_lancement_discretion_bras_a_v4.py` | `8ca94b7c9109cdd315457f0d5cbd7f1d5d4ad38b48ece9010b13244da3e73fee` |
| `tests/aide_bras_a_v11.py` | `755aea3278bf5363f3782b90cfea4266eb668b1459ee7b26f1582cbc46885255` |
| `tests/test_analyse_bras_a_v11.py` | `31f01e76f5efeafc7cfccb675566379ab36911b762540c7b5d8ae0aaff2d4bdd` |
| `tests/test_graines_bras_a_v11.py` | `c56f604bec5c89f02ae68bb67917a09425a029cfdeaab2e91b753a6a478a9756` |
| `tests/test_cloisonnement_bras_a_v11.py` | `084c2f2a86e352c1b57d0c568b49b794fc99a9a4870a4f9d9b4ac89e3a58623a` |
| `tests/test_verdicts_bras_a_v11.py` | `3f25250e101a198f81a5fd666449d831833ff90af9b7af380f8914306e39329e` |
| `tests/test_permutation_etiquettes_bras_a_v11.py` | `a91b6f41469cc80a2a00788040e7e4b049898e83044ebe89254dbfc1b4c77ff1` |
| `tests/test_mesures_bras_a_v11.py` | `e165ca234c3563839083ab1384002974560c60fbf0f26726a4144e8f4852ec81` |

- Les modules des arrêts, des verdicts, du schéma de permutation, des dépôts et des mesures sont ceux de la version 10, sous leur nom neuf : aucun calcul n'y change.
- Le relevé des défauts du texte : `defauts-du-texte-trouves-en-codant-v11.md`, dans ce dossier.

## 2. Essais

- **324 essais passent** : 284 dans mes six fichiers (analyse 68, graines 109, garde statique 62, verdicts 27, schéma de permutation 9, mesures 9), 36 dans `tests/test_reponses_lecteurs_v5.py`, 4 dans `tests/test_epreuves_couverture_bras_a_v3.py`.
- **Commande** : `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v11.py tests/test_verdicts_bras_a_v11.py tests/test_graines_bras_a_v11.py tests/test_cloisonnement_bras_a_v11.py tests/test_permutation_etiquettes_bras_a_v11.py tests/test_mesures_bras_a_v11.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py`.
- Lancés une dernière fois après le scellement des modules et des fichiers d'essais. La suite entière du dépôt n'a pas été lancée.
- Données fabriquées dans les essais ; graines par `numpy.random.SeedSequence`.
- **Les essais d'attaque de la vérification de la version 10 sont repris** : les deux formes de C-1, les sept lignes de la phrase de l'écart à R9, la valeur « en attente », les valeurs approchantes d'un choix. Je les ai aussi rejoués hors du dépôt, sur données fabriquées : les deux lectures de C-1 s'arrêtent.

## 3. C-1 — une seule première livraison par course

- **Ouverture de lecture.** Avant toute lecture d'une première livraison, et après les gardes qui reconnaissent la pièce, le programme écrit et scelle `ouverture-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` dans le dossier des arrêts. Quatre champs : `evenement`, `sha256_de_la_piece`, `sha256_de_la_configuration`, `sha256_du_constat_de_lancement`.
- **Ensuite**, toute pièce d'une autre empreinte exige une ligne de GO, sous quelque configuration que ce soit. Garde nommée : `exiger_une_seule_premiere_livraison`.
- **Seul le rejeu de la même pièce reste permis**, sous la même configuration et le constat de son ouverture. Sous une autre configuration, c'est une relecture, refusée.
- **Rang supérieur à 1** : une configuration rangée dans `livraison-<rang>`, rang supérieur à 1, sans registre figé, est refusée à sa lecture. Garde nommée : `exiger_registre_fige_au_rang`.
- **Le résultat de la règle dit son ouverture** (`ouverture`), et la garde de sortie refuse une première livraison lue sans elle.
- **L'essai de la vérification** — « ne repère pas », puis « repère » sous la même configuration — s'arrête à la seconde pièce. Sa première forme, au rang 2 sans registre, s'arrête à la lecture de la configuration.
- **Une garde de plus, de ma conception** : un constat de pièce donnée n'ouvre que la première lecture de la course. Dès qu'une ouverture ou un autre acte de reprise existe, seule une livraison refusée par un arrêt se reprend. Sans cela, une pièce quelconque donnée sans compagnon après une lecture aboutie laissait un constat qu'une ligne pouvait citer pour lire une seconde livraison. Relevé, point A.3.

## 4. M-1 et les précisions sur les lignes d'accord

- **Cellule d'objet exacte.** La cellule d'objet de la ligne de GO est la phrase, comparée sans le gras de Markdown, sans égard à la casse ni aux accents ; un point final est seul admis. Fonction nommée : `graines_bras_a_v11.dit_l_accord`. Vaut pour les deux phrases.
- **Une ligne de type « révocation » ne vaut jamais accord**, même si sa cellule d'objet est la phrase.
- **Les trois empreintes d'une ligne de reprise** sont dans les autres cellules de la ligne.
- **Laquelle des cellules est celle de l'objet** : la quatrième, par une constante nommée (`CELLULE_DE_L_OBJET`).
- **Les sept lignes de l'essai d'attaque** : la phrase ouvre ; « aucun écart… », « pas d'écart… avant le devis », « … ? à trancher », « …, refusé » et les mots du mot de Lazar n'ouvrent rien ; la phrase sans accents ouvre ; la phrase en gras ouvre.
- **Porte de l'écart à R9** : elle reçoit aussi le registre courant. Avant le tirage de la table, aucune ligne entrée depuis l'état figé ne doit nommer la ligne de GO de l'écart, quel que soit son type. Fonction nommée : `lignes_entrees_depuis`.
- **La porte de la version 10 des graines** rejoint les portes que la garde statique refuse.

## 5. M-2 à M-5

- **M-2, contrôle et rejeu** : corrigé, selon le brouillon 34.
  - Tout rejeu exige un contrôle fait pour lui, celui d'une première livraison aussi : son ouverture le signale.
  - Au départ du rejeu, le programme écrit et scelle `rejeu-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json` dans le dossier de la livraison. Quatre champs : `evenement`, `sha256_du_controle_de_lancement`, `sha256_de_la_piece`, `sha256_de_la_configuration`.
  - Un contrôle que porte déjà une trace n'ouvre aucun autre rejeu.
  - La garde de sortie relit sur la trace ce que le résultat dit du rejeu.
- **M-3, abrégés de moins de seize signes** : écart motivé. Le texte fixe seize signes ; la consigne de tenue du registre demande l'empreinte entière.
- **M-4, une autre course** : fermé au lancement, pour un registre commun. Le programme du constat, en version 4, refuse une configuration de rang 1 dès que le registre courant porte la ligne d'inscription d'une autre configuration de l'analyse du bras A, que ne suit aucune ligne de GO de reprise. Le programme d'analyse, lui, ne voit toujours que le dossier des arrêts que sa configuration nomme.
- **M-5, la garde « en attente »** : corrigé. Elle scelle `piece-en-attente-d-un-choix-bras-a-<seize signes>.json`, quatre champs, avant l'ouverture et avant l'acte.

## 6. Précisions A.1 et A.3 à A.6

- **A.1** : la pièce arrêtée par une garde ordinaire se relit sous une configuration neuve et une ligne de GO qui cite son constat. L'acte porte alors deux fois la même empreinte ; c'est refusé pour une livraison refusée par un arrêt.
- **A.3** : recomposer le résultat reste permis après un arrêt à l'étape (n). Le fichier des scores par unité n'est pas rouvert ; une livraison refusée à l'étape (m) reste refusée.
- **A.4** : un constat n'est cité que s'il vient de la configuration d'une première livraison, celle qui n'inscrit aucun registre figé.
- **A.5** : le constat d'erreur de rangement a cinq champs, dont `sha256_que_scelle_le_compagnon`. « La même pièce » est celle que scelle le compagnon quand il en scelle une, sinon celle des octets donnés.
- **A.6** : la valeur « en attente » est une garde ordinaire sans issue, et la pièce est consignée. Quand le choix est tranché, la même pièce se relit par la règle d'octroi.
  - Pour que ce soit possible dans une même course, les cinq choix restent les mêmes pour toutes les livraisons **à une exception près** : une configuration de rang supérieur peut porter une rédaction du point 20 là où celle de rang inférieur portait « en attente ». Jamais l'inverse. Fonction nommée : `memes_choix`. Relevé, point A.2.

## 7. Programme du constat : version 4, et non 3

- **Le texte nomme la version 3.** La première des quatre précisions demande au programme un refus de plus. La version 3 est scellée et committée : la garde est donc dans un programme de nom neuf, `scripts/constat_de_lancement_discretion_bras_a_v4.py` (`8ca94b7c…`).
- **À nommer au prochain brouillon**, avec son empreinte. La configuration inscrit l'empreinte du programme qu'elle emploie : c'est elle qui fait foi.
- La version 4 lit les configurations et les lignes d'accord par les modules de la version 11.

## 8. À regarder en premier

1. **Une configuration inscrite puis abandonnée bloque la suivante.** Avec la garde du registre, une configuration de rang 1 inscrite, jamais lue, puis remplacée — pour une faute de frappe, par exemple — fait refuser toute configuration de rang 1 suivante : son inscription n'est suivie d'aucune reprise, et aucune reprise ne peut exister sans arrêt ni constat. Le texte ne dit pas le remède. Relevé, point A.1.
2. **Un contrôle fait avant le premier départ sert au rejeu.** Une première lecture n'exige aucun contrôle ; s'il y en a un, sain, et qu'une panne suit, ce contrôle ne porte aucune trace et ouvre le rejeu. Rien de scellé ne date le premier départ. Relevé, point A.4.
3. **Le registre courant donné au contrôle** n'est pas forcément le dernier : limite écrite au texte, inchangée.
4. **Le nom `rejeu_sous_le_meme_acte`** du résultat vaut maintenant aussi pour le rejeu d'une première livraison, sous son ouverture. Je ne l'ai pas renommé.
5. **Le gras seul est ôté** avant de comparer une cellule : les accents graves, l'italique et les guillemets ne le sont pas. Une cellule ainsi mise en forme n'ouvre rien.
6. **La valeur « en attente »**, son constat et l'exception aux mêmes choix sont à retirer ensemble au scellement du texte (vérification du brouillon 34, M-3).

## 9. Portée de mes lectures et méthode

- **Lus en entier** : la vérification du code de la version 10 ; la note du brouillon 34.
- **Lus par passages** : le brouillon 34 — conventions (constats de pièce donnée, ouverture de lecture, trace de rejeu, valeur « en attente ») ; 6.9, « Ce qu'est la bonne pièce » et « Une seule première livraison par course » ; les deux lignes neuves de 8.4 ; 13.2, phrases d'accord. La vérification du brouillon 34 : parties 2, 3 et 4.
- **Les pièces d'attaque de la vérification de la version 10** : `attaques_v10.py` et `configuration_v10.py` en entier, avec leurs sorties ; les trois autres par leurs sorties.
- **Méthode** : copie mécanique des fichiers de la version 10 sous leurs noms neufs, puis remplacements exacts par programme dans le bloc-notes. Rien n'a été scellé avant le dernier passage des essais.
- **Fichiers ouverts hors de mon code** : aucun de plus. Aucun module habilité.
