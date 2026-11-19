# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 10 — note du rédacteur — v1

Ce que la version 10 change, ce qu'elle laisse en attente, et ce qu'il faut regarder en premier.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : le mot de Lazar « go recos » du 19 novembre 2026 (`1fcfae81…`) ; la vérification du code de la version 9 (`ab52290f…`) et ses pièces ; le brouillon 32 (`a053eeb8…`), sa note (`a3f47051…`, partie 6) et sa vérification (`0d7b0dff…`, C-1 et M-2) ; **le brouillon 33, qui fait foi** (`dc3bc0236e9103454c988fa24997c698306ef78a2328587430bed553a5020c4a`), sa note (`1f2dc907…`, partie 5) et sa vérification (`3cdd53ca…`, M-1) ; les précisions de la session principale reçues pendant le tour.
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni appel de modèle ; aucun sous-agent ; aucune dépense. `registres/`, `.claude/`, le journal et `prereg/` non touchés. Rien de committé. Aucun fichier existant modifié : les versions 4 à 9 et les programmes du constat 1 et 2 répondent toujours à leur empreinte.
- **Le fichier réel de la configuration n'est pas écrit** : il se scelle avec le texte.
- **Heure** : 2026-11-19, 23:15Z.

## 1. Fichiers

Tous neufs, tous scellés.

| fichier | empreinte |
|---|---|
| `src/controle_ia/organismes_discrets/analyse_bras_a_v10.py` | `b07d425d198cacf5ea3f7db20c6b385ad9c9393dc795b1f7fb4c52353e1b4f01` |
| `src/controle_ia/organismes_discrets/configuration_bras_a_v10.py` | `378b729c46b0f1b4fac7dcb5f8ce7fe9551728a46dbcbcbb90d9e17e40242644` |
| `src/controle_ia/organismes_discrets/arrets_bras_a_v10.py` | `d7206b23067b941320da283d9a889b6ac8b425c890b5dfc69ee61fede254d254` |
| `src/controle_ia/organismes_discrets/graines_bras_a_v10.py` | `c55b60b5d87b2d335498b586816634a5606b535b9de04d22ce4ad34d4c377774` |
| `src/controle_ia/organismes_discrets/verdicts_bras_a_v10.py` | `ed2bdbc8f03e54cad8c27b0c0db2350d85b57d45ce7e3a5360c5b8b9f87df967` |
| `src/controle_ia/organismes_discrets/permutation_etiquettes_bras_a_v10.py` | `c78b00a121c09eb96e32a20acbf998f2b784f984c09ca4731c4d3c209156ff6a` |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v10.py` | `159f2721d266d2c3713cf1e064fdedf017e31d4423c3b5afc2f4f62cbe1139d6` |
| `src/controle_ia/organismes_discrets/depots_bras_a_v10.py` | `8ef66e66dd02e2e058eb52e6d0f816c3ab69954aca237489b5c324936b0347e9` |
| `src/controle_ia/organismes_discrets/mesures_bras_a_v10.py` | `8fd474372be0217067c17de4d1eedc04d138a8fefd8fcb29ccea7a724e37cce4` |
| `scripts/constat_de_lancement_discretion_bras_a_v3.py` | `6ee84152920d0dffe46f0a289279a961648946812ea53e0a86fd28ad7368b17c` |
| `tests/aide_bras_a_v10.py` | `19b8327961f2bb152f6879ef43a6e4955982f15a3bd8cc12eed638eff3c7f17e` |
| `tests/test_analyse_bras_a_v10.py` | `79a9c9e6a75b9e2aa4dd04f14fa82af9b177ff80f5d8100f7424fa7a83e3b2d8` |
| `tests/test_verdicts_bras_a_v10.py` | `289c28066a3aa1e2dc8aa1ba8f96f50ee8a924e02ee27b8e970ecdc6fdc4348c` |
| `tests/test_graines_bras_a_v10.py` | `13764ab1364dbd60695949efec09683f1721533a55f4fe423bb304b6a63b2f8e` |
| `tests/test_cloisonnement_bras_a_v10.py` | `5da96c7603e4f9e486c8ceb1e0dd523a4c4c57405e6a35e5fba038d092bf2f62` |
| `tests/test_permutation_etiquettes_bras_a_v10.py` | `d5a88fe763a2708624f3c25034944028dce8e3aa58f9b949a9f3a9e42178fa0e` |
| `tests/test_mesures_bras_a_v10.py` | `4f4f8cc01bef1b62af29572172516d89950c0d211ebe0f4df8470bfd50192b40` |

- Les modules `depots` et `mesures` sont ceux de la version 9, sous leur nom neuf : aucun calcul n'y change.
- Le relevé des défauts du texte : `defauts-du-texte-trouves-en-codant-v10.md`, dans ce dossier.

## 2. Essais

- **319 essais passent** : 279 dans mes six fichiers (analyse 66, graines 107, garde statique 61, verdicts 27, schéma de permutation 9, mesures 9), 36 dans `tests/test_reponses_lecteurs_v5.py`, 4 dans `tests/test_epreuves_couverture_bras_a_v3.py`.
- **Commande** : `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v10.py tests/test_verdicts_bras_a_v10.py tests/test_graines_bras_a_v10.py tests/test_cloisonnement_bras_a_v10.py tests/test_permutation_etiquettes_bras_a_v10.py tests/test_mesures_bras_a_v10.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py`.
- Lancés une dernière fois après le scellement des modules et des essais. La suite entière du dépôt n'a pas été lancée.
- Données fabriquées dans les essais ; graines par `numpy.random.SeedSequence`.
- Chaque garde neuve a un cas sain et un artefact (parties 3 à 8).

## 3. Les cinq choix restent dans la configuration

- **Aucune valeur par défaut dans le code.** Les cinq choix nommés restent obligatoires ; `ecrire_la_configuration_scellee` exige qu'on les lui donne.
- **Gabarit** : `configuration_bras_a_v10.CHOIX_DU_MOT_DE_LAZAR_DU_19_NOVEMBRE_2026` recopie le mot ; `contenu_de_la_configuration` et `ecrire_la_configuration_scellee` composent et écrivent une configuration à partir des trois parties qu'on leur donne. Aucune fonction de lecture ne lit le gabarit ; un essai le vérifie sur le texte des modules.

| choix | valeur du gabarit | valeurs que la garde admet |
|---|---|---|
| schéma de permutation | échange dans chaque paire | celle-là seule |
| seuil du 1 % | compté sur les tirages demandés | celle-là seule |
| intervalle impossible | lu comme un intervalle dégénéré | « comme dégénéré », « anomalie » : le point 19 reste ouvert |
| moniteur appris non ajustable | « en attente » | « aire non calculable », « module corrigé », « en attente » |
| issue d'un arrêt de la lecture de la discrétion | discrétion non lue, en distinguant les étapes | celle-là seule |

- **Rédactions retirées du texte** : permutation libre par épisode ; seuil sur les tirages calculés ; intervalle impossible « indécis d'office » ; moniteur non ajustable tenu pour une « anomalie » ; issue par la ligne d'arrêt de la course ; issue « non lue » à toute étape. La garde de la configuration les refuse en les nommant (`REDACTIONS_RETIREES`), et leurs branches sont retirées de l'analyse, des verdicts et du schéma de permutation.
- **« En attente »** n'est pas une rédaction : c'est l'absence de choix, écrite en toutes lettres, puisque le choix n'a pas de valeur par défaut. Tant qu'elle est inscrite, le programme s'arrête s'il rencontre le motif « moniteur appris non ajustable », à quelque dose que ce soit. C'est une garde ordinaire : ni événement d'arrêt, ni fichier d'arrêt, ni issue. Elle joue avant l'acte de reprise : l'attente ne dépense aucune ligne de GO. Une livraison sans ce motif se lit.
- **Le nom de règle d'arrêt « moniteur appris non ajustable » a disparu** de ce que rend le programme qui refuse (`arrets_bras_a_v10`). Un constat d'arrêt qui le porterait est hors de sa forme.

## 4. La porte de l'écart à R9 : la phrase diffère de la lecture consignée

- **Le code n'est pas changé.** Il exige, dans la ligne de GO lue à l'état figé du registre, la phrase « écart à R9 accordé pour la table des identifiants opaques », sans égard à la casse.
- **Le mot de Lazar ne porte pas cette phrase.** Sa ligne dit : « écart à R9 : entropie propre de la table des identifiants opaques » — « accepter ». Une ligne de registre qui recopierait ces mots **n'ouvrirait pas la porte**.
- **La ligne à inscrire doit donc porter la phrase du code**, à la lettre. Un essai le fixe : la ligne aux mots du mot est refusée, la ligne à la phrase du code ouvre.
- Le brouillon 33 ne fixe pas cette phrase : relevé, point B.1.
- Deux rappels, inchangés depuis la version 9 :
  - la porte lit la ligne dans une pièce de l'état figé du registre, reconnue à son empreinte ; l'appelant donne cette pièce et son empreinte ;
  - une ligne placée après elle qui nomme son identifiant la ferme, quel que soit son type.

## 5. Les trois mineurs de la vérification de la version 9

- **M-1, le contrôle avant un rejeu** : corrigé, et porté plus loin par le brouillon 32.
  - Le programme du constat, joué à titre de contrôle, scelle `controle-de-lancement-bras-a-<date>.json` dans le dossier de la livraison, **sain ou malsain**. Il s'arrête si ce nom est pris. Il ne touche pas au constat d'origine.
  - Le programme d'analyse, avant tout résultat écrit pour la livraison : s'il y a des contrôles, **le plus récent doit être sain**, daté après le constat d'origine, de la même configuration, du même registre figé, de la même ligne de GO et du programme inscrit. **Il en faut un** pour rejouer une lecture après son acte de reprise. L'étape (n) ne les regarde pas.
  - Le résultat de la règle porte le contrôle sous lequel la lecture est partie (`controle_de_lancement`), et la garde de sortie le relit.
- **M-2, préfixes et identifiants** : corrigé. Seize signes du début de l'empreinte d'une configuration suffisent à la citer. Un identifiant de GO se reconnaît à ses lettres et à ses chiffres, quels que soient la casse et les séparateurs, sans lettre ni chiffre collé avant ou après.
- **M-3, constat écrit à la main** : limite déclarée, inchangée. Le programme d'analyse ne distingue pas un constat scellé écrit à la main de celui du programme.

## 6. Provenance : brouillon 33

- **La clé de provenance est obligatoire.** `cle_du_module_dans_piece_source` est un texte non vide ; absente ou `null`, la configuration est refusée et rien n'est lu. La branche « clé `null`, `piece_source` non lu » a disparu.
- **Constat de provenance.** Quand la garde de provenance arrête le programme, il écrit et scelle `provenance-non-etablie-bras-a-<seize signes>.json` dans le dossier des arrêts : `evenement`, `constat`, `sha256_de_la_piece`, `sha256_de_la_configuration`. Il n'est jamais réécrit. Ce n'est pas un fichier d'arrêt.
  - `constat` est l'une de cinq natures : pièce qui n'est pas du JSON ; pièce qui n'est pas un objet JSON ; `piece_source` absent ou mal formé ; clé de provenance absente de `piece_source` ; empreinte d'un autre module.
- **Première livraison, après un constat** : une sortie d'une autre empreinte n'est pas lue, ni sous la configuration du constat, ni sous une configuration neuve sans ligne de GO. La pièce qui remplace est une livraison refaite : configuration neuve, ligne de GO, acte de reprise.
- **La ligne de GO cite le constat** à la place du fichier d'arrêt, avec le module et le rapport. L'acte de reprise porte l'empreinte de la pièce arrêtée dans `sha256_de_la_livraison_refusee`.
- **Livraison refaite, après un constat** : aucun acte n'est écrit, la ligne n'est pas dépensée, et la pièce qui remplace se lit sous elle si sa provenance passe. Chaque pièce arrêtée laisse son constat.
- **Le rapport compte** les constats de provenance, avec les fichiers d'arrêt (`compte_des_livraisons`).
- **Deux gardes nommées** : `exiger_provenance_etablie` et `exiger_remplacement_par_la_regle_d_octroi`.
- **Un choix à moi** : la pièce arrêtée n'est pas relue sous une autre configuration, même une configuration qui inscrirait son module. Elle tient la place d'une livraison refusée. Relevé, point A.1.

## 7. Erreur de rangement : l'empreinte est consignée tout de suite

Mineur M-1 de la vérification du brouillon 33 ; le prochain brouillon le portera.

- Quand la pièce donnée est refusée pour son compagnon, le programme écrit et scelle `erreur-de-rangement-bras-a-<seize signes>.json` dans le dossier des arrêts, aux mêmes quatre champs. Garde nommée : `exiger_piece_bien_rangee`.
- **La pièce redonnée y est confrontée.** La même, octet pour octet, se lit sans ligne de GO. D'une autre empreinte, elle n'est pas lue : elle passe par la règle d'octroi, et la ligne de GO cite ce constat.
- Essais sur artefact : une autre pièce bien rangée ; d'autres octets sous le même nom et au même chemin.
- **Ce qui est de moi** : le nom du fichier, ses quatre champs, et quatre natures — compagnon absent, illisible, d'un autre nom, d'une autre empreinte. Relevé, point B.3.
- **Conséquence à connaître** : un chemin donné par erreur, s'il désigne un fichier, coûte une ligne de GO. Un chemin sans fichier ne laisse rien.

## 8. Autres changements du brouillon 32

- **Statut du fichier de l'étape (m)** après un arrêt à l'étape (n) : une seule valeur, « inchangé, opposable ».
- **Verdicts** : un arrêt à l'étape (m) rend la discrétion « non lue » ; un arrêt à l'étape (n) garde la table C et rend les grandeurs de cette étape « non rapportées ». La table A n'est jamais touchée par cet arrêt.
- **Une pièce qui n'est pas du JSON, ou pas un objet JSON**, est « provenance non établie », jamais « pièce illisible ».
- **Recomposer n'est pas rejouer** : `resultat_recompose` reste permise après le fichier des grandeurs de l'étape (n). Elle refuse une livraison dont un arrêt est consigné, à l'étape (n) aussi : le texte dit qu'elle « ne lit aucune livraison refusée ». Relevé, point A.3.
- **Réglages rendus** : la livraison doit déclarer l'échange dans chaque paire ; un module resté à la permutation libre est refusé.

## 9. À regarder en premier

1. **Une seconde « première livraison » se lit sans ligne de GO.** Dans une course où le rang 1 a été lu sans arrêt, une autre pièce, sous une configuration de rang 2 qui n'inscrit aucun registre, est lue comme une première livraison. Je l'ai vérifié par une expérience hors du dépôt, sur données fabriquées.
   - Ce défaut est présent depuis la version 8. Je ne l'ai pas corrigé : je l'ai vu après le scellement.
   - Il permettrait deux lectures de la discrétion dans une course. Les deux laissent leurs fichiers, que le compte montre.
   - La garde tient en peu de lignes : dès qu'un autre dossier de livraison de la course porte une lecture, exiger une ligne de GO.
2. **Un constat laissé sous une livraison refaite reste citable.** Le texte ne permet de citer un constat de provenance que « pour une première livraison ». Le programme vérifie que le constat existe, qu'il vient d'une autre configuration et que sa pièce n'a pas d'acte ; il ne vérifie pas que cette configuration était celle d'une première livraison. La session qui inscrit la ligne le vérifie. Fermeture possible par programme : une configuration de première livraison est celle qui n'inscrit aucun registre figé.
3. **Le drapeau `rejeu_sous_le_meme_acte`** du résultat ne se relit sur aucune pièce scellée. La garde de sortie n'en vérifie que la forme.
4. **Préfixes de seize signes** : les abrégés de huit ou douze signes d'usage dans les notes ne sont pas vus. La consigne de tenue du registre demande l'empreinte entière.
5. **Fichiers de contrôle** : le code ne sait pas si le dernier contrôle vient d'être fait. Sans contrôle refait, un contrôle sain plus ancien qu'une révocation passe encore. Pour une première livraison, rien ne lui dit qu'une lecture a été interrompue.
6. **« Module corrigé »** se lit, dans l'analyse, comme « aire non calculable » : la différence est du côté du module.
7. **`arret_de_la_livraison`** ne rend que des arrêts : une pièce que fixe un constat de provenance n'est pas « refusée » pour elle.

## 10. Portée de mes lectures et méthode

- **Lus en entier** : le mot de Lazar ; la note du brouillon 33.
- **Lus pour ce qui touche le code** : la vérification du code de la version 9 (verdict, M-1 à M-3, avis sur les points A.1 à A.3) ; la note du brouillon 32 (partie 6) ; la vérification du brouillon 32 (C-1, M-2).
- **Lus par passages** : les brouillons 32 et 33 — conventions, « Constat de provenance » ; 6.9, « Livraison refaite », « Règle d'octroi », « Ce qui n'est pas un refus d'une livraison », « Recomposer n'est pas rejouer » ; trois lignes de 8.4 ; la ligne de 13.2 sur l'écart à R9. La vérification du brouillon 33 : parties 2 et 3.
- **Les pièces d'attaque de la vérification de la version 9** : leurs titres et leurs sorties, non leur code en entier. Ce qu'elles montraient (M-1, M-2) est repris en essais.
- **Méthode** : les modules ont été composés à partir de ceux de la version 9 par des programmes de remplacement exact, dans le bloc-notes, puis corrigés sur place avant scellement. Rien n'a été scellé avant le dernier passage des essais ; les essais ont été relancés après.
- **Fichiers ouverts hors de mon code** : `src/controle_ia/scellement.py`, pour la forme d'un compagnon. Aucun module habilité.
