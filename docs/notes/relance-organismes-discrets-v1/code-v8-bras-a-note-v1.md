# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 8 — note du rédacteur — v1

**En bref.** La version 8 porte les deux défauts à corriger et les six mineurs de la vérification du code de la version 7, et s'accorde au brouillon 28, qui fait foi. Toute pièce que le code scelle s'écrit sous un nom provisoire, y reçoit son sceau, puis prend son nom : une panne ne laisse plus de dossier illisible. Une lecture interrompue se rejoue, étape par étape. Le registre des accords est remis comme une pièce, dans son état figé au scellement de la configuration ; un programme fait le constat de lancement, et l'analyse l'exige avant toute lecture. Les valeurs p se comparent à leurs comptes en fractions exactes, et les états se disent de même. 309 essais passent. Rien n'est committé.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle.
- **Références** : brouillon 28 (`604e0410…`) et sa note (`94f704ed…`) ; notes des brouillons 26 (`c066b4f0…`) et 27 (`fdc51961…`) ; vérification du code de la version 7 (`db3a8a06…`) et ses essais d'attaque ; vérifications des brouillons 25 (`10bcc89e…`) et 26 (`fa988381…`) ; précisions de la session principale, dont la dernière sur l'exemple fictif (partie 5).
- **Interdits tenus** : aucun interne de moniteur ouvert, ni par moi ni par mes programmes ; aucune fiche de l'organisme d'idéation ; aucune réponse de l'essai de mesure ; aucune clé ; aucun appel réseau ni de modèle ; ni `registres/`, ni `.claude/`, ni le journal, ni `prereg/` touchés ; rien committé ; aucun sous-agent ; aucun fichier des versions 4 à 7 modifié.
- **Heure** : 2026-11-19, 18:50Z.

## 1. Fichiers

Sous `src/controle_ia/organismes_discrets/`, chacun avec son compagnon :

| fichier | empreinte | ce qui change depuis la version 7 |
|---|---|---|
| `depots_bras_a_v8.py` (neuf) | `4ed4f03dd54512a4b3c1ab624319358c69af0b8a717aca0fd2df51f16d385cda` | écriture scellée sans reste : provisoire, sceau, renommage |
| `analyse_bras_a_v8.py` | `0600918680fd9d15415f81a56aeb7dac896242566b3870f8bedd29c2eb6018d3` | fractions exactes ; constat de lancement exigé ; rejeu par étape ; dossiers lus dans la configuration ; cinq natures ; formes reconnues |
| `verdicts_bras_a_v8.py` | `a8bb52b9df3fe2adb1d4b1a55d44fb24ec03355e3bfee1ed51ba8dfe05493145` | ni dossier des arrêts ni fichier de l'étape (m) donnés par l'appelant ; dix champs aux constats |
| `configuration_bras_a_v8.py` | `3abafbed303c7ee69219bf38f08552141354627ecb9e52f9ba62c48c8d36ad6b` | quatre pièces attendues ; un dossier par livraison ; dossier des arrêts ; configurations voisines |
| `graines_bras_a_v8.py` | `7de5ff1ac9eb4d3d4d8aca53fb397ad9afca254f7bcca52cd72b6608d28660f1` | registre remis comme une pièce, reconnu à sa seule empreinte |
| `arrets_bras_a_v8.py` | `3521eee0dc8183e69ad0788058d0b14534687ca0d629ff82953810e84828d00b` | cinquième nature : « un champ hors de son ordre » |
| `cloisonnement_bras_a_v8.py` | `5236c0dae7f309d7acd705fb1d4d61cef8261e6f8fdf04990931cbb4eba6cc44` | motifs sans égard à la casse ; portes des graines des versions 1 à 7 refusées |
| `permutation_etiquettes_bras_a_v8.py` | `411761323f368f8a82bb8b073c8415616e2800c7c37620e7b5315089149b8182` | imports de la version 8, rien d'autre |
| `mesures_bras_a_v8.py` | `5e1a1afd86cae4e9288f088abb1b3cc50833215857190e9267a71465ffce9c48` | imports de la version 8, rien d'autre |

Sous `scripts/` : `constat_de_lancement_discretion_bras_a_v1.py` (`21c38f97875b233104c240752ae7c81089deb65ae428cc4903051e0f9564b758`), le programme du constat de lancement, sous le nom que le texte fixe.

Sous `tests/` : `aide_bras_a_v8.py` (`35666341…`), `test_analyse_bras_a_v8.py` (`405a8890…`), `test_verdicts_bras_a_v8.py` (`cf877edc…`), `test_graines_bras_a_v8.py` (`88857759…`), `test_cloisonnement_bras_a_v8.py` (`9ee65497…`), `test_permutation_etiquettes_bras_a_v8.py` (`93c3bd20…`), `test_mesures_bras_a_v8.py` (`20b7f212…`).

**Restent et sont importés tels quels** : `reponses_lecteurs_v5.py`, `instrument_appariement_v4.py`, `epreuves_couverture_bras_a_v3.py`, `fabrication_v3.py`, `graines_bras_a_v4.py`. La chaîne de la version 8, programme du constat compris, n'importe aucun module des versions 5 à 7 (essai).

## 2. Essais

Commande :

```
PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v8.py tests/test_verdicts_bras_a_v8.py tests/test_graines_bras_a_v8.py tests/test_cloisonnement_bras_a_v8.py tests/test_permutation_etiquettes_bras_a_v8.py tests/test_mesures_bras_a_v8.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
```

**309 essais passent** : 269 de la version 8 (analyse 62, verdicts 27, graines 104, garde statique 58, permutation 9, mesures 9), 36 des réponses des lecteurs, 4 des épreuves de couverture. Toutes les données sont fabriquées dans l'essai. La suite entière n'a pas été lancée.

L'essai de la garde statique sur le vrai dépôt ne passe que si les quatre modules autorisés de la version 8 répondent à leur compagnon : ils sont scellés, et l'essai passe.

## 3. C-2 — la panne

**Écriture sans reste** (`depots_bras_a_v8.ecrire_et_sceller`). Trois temps : le contenu sous `<nom>.provisoire` ; le compagnon `<nom>.sha256`, lui-même écrit sous un nom provisoire puis renommé ; enfin la pièce prend son nom, d'un seul geste. Une pièce ne porte donc jamais son nom sans son sceau. Rappelée avec le même contenu, la fonction finit ce qu'une panne a laissé, ou ne fait rien ; avec un autre contenu, elle refuse (R12). Passent par elle : le fichier d'arrêt, l'acte de reprise, le fichier de l'étape (m), ses constats et le constat de lancement.

**Les restes** (fichiers provisoires, compagnon sans son fichier) ne sont jamais lus comme des pièces. `compte_des_livraisons` les rapporte sous `restes_d_ecritures_interrompues`.

**Rejeu, étape par étape** (6.9, « Panne pendant une lecture »).
- Étape (m), première livraison : interrompue avant son résultat, elle se rejoue d'elle-même. Rien ne la distingue d'une première lecture ; le code ne peut ni le voir ni le dire.
- Étape (m), livraison refaite : si l'acte de reprise est déjà scellé, la lecture ne se rejoue que sous la même ligne de GO. La ligne est confrontée de nouveau à la configuration donnée. Le résultat porte `rejeu_sous_le_meme_acte` à vrai ; c'est à l'enchaînement de le consigner au manifeste. Sous une autre ligne, ou sans ligne : refusé.
- Le résultat de l'étape (m) est son fichier scellé. Dès qu'il existe dans le dossier de la livraison, relire est refusé. L'étape (m) écrit ses constats d'abord, son fichier ensuite : une panne entre les deux laisse l'étape sans résultat, jamais un fichier sans ses constats.
- Étape (n) : elle se rejoue seule. `lire_fichier_des_rangs` relit le fichier des scores par unité sur le fichier scellé de l'étape (m), qui n'est ni réécrit ni rejoué. `resultat_pour_l_etape_n` recompose le résultat de la règle pour les grandeurs de l'étape (n) et exige que ses états soient ceux du fichier scellé. Après un fichier d'arrêt de l'étape (n), plus de rejeu.

**Essais de panne simulée** : à chacun des trois temps, pour le fichier d'arrêt, l'acte de reprise, le fichier de l'étape (m) et l'arrêt de l'étape (n) ; pendant la lecture, après l'acte scellé ; pendant l'étape (n).

**Limite.** Le texte demande « la même configuration (même empreinte) ». L'acte de reprise a quatre champs, et aucun ne garde l'empreinte de la configuration. Le code vérifie ce qu'il peut : la ligne de GO de l'acte doit citer le module et le rapport que la configuration donnée inscrit. Une configuration qui inscrirait les mêmes empreintes et d'autres chaînes passerait. Proposition au relevé, point 2.

## 4. C-1 — le registre, et le constat de lancement

**Point d'entrée nommé** : `graines_bras_a_v8.lire_le_registre_fige(registre_fige, sha256_au_scellement)`. Le registre du dépôt n'est plus lu ; le module ne nomme plus aucun fichier de registre.

**Hypothèse codée, celle du brouillon 26.** La session qui lance remet une pièce : le registre des accords de la branche principale, tel qu'il était quand la configuration a été scellée. Le code la reconnaît à sa seule empreinte, celle de `pieces_attendues.sha256_du_registre_des_accords`. Son nom, son dossier et un compagnon ne comptent pas. La ligne de GO d'une reprise s'y lit : une ligne et une seule, la phrase d'accord à la lettre, aucune forme de refus, aucune ligne de type « révocation » qui la nomme dans cet état figé, et trois empreintes entières — un seul fichier d'arrêt du dossier dont la livraison n'a pas encore d'acte, le module et le rapport que la configuration inscrit.

**Constat de non-révocation : le constat de lancement.** `scripts/constat_de_lancement_discretion_bras_a_v1.py` reçoit la configuration scellée, la pièce de l'état figé (ou rien), le registre courant, son commit et la date. Il rend le constat à six champs.
- Constat sain : scellé sans reste dans `livraison-<rang>/constat-de-lancement-bras-a.json`. Code de sortie 0.
- Constat malsain : affiché, **non scellé**. Code de sortie 1. Il peut ainsi être refait sans rien écraser.
- Pièces fautives : arrêt, code de sortie 2.

Le programme d'analyse exige ce fichier avant toute lecture, à l'étape (m) comme à l'étape (n) (`exiger_constat_de_lancement`) : présent, scellé, six champs, l'empreinte de la configuration lue, celle du registre figé qu'elle inscrit, `configuration_inscrite` vrai, `revocation_entree` faux. Sinon : garde ordinaire. La pièce de la livraison n'est pas même cherchée ; aucun événement, aucun fichier d'arrêt, aucun acte.

**Essais demandés** : un cas sain, et trois artefacts où rien n'est lu — configuration absente du registre courant ; constat absent ; révocation entrée depuis l'état figé. S'y ajoutent : constat non scellé, d'une autre configuration, d'un autre registre figé, écrit à la main avec un champ faux, recopié d'une autre livraison.

**Mes hypothèses, à confirmer** (relevé, point 4).
- « La ligne de GO que la lecture emploie » n'est pas une entrée du programme. Il la retrouve : toute ligne de l'état figé qui porte la phrase d'accord d'une livraison refaite et cite le module et le rapport de la configuration. S'il y en a plusieurs, la révocation de l'une quelconque compte.
- Une révocation est une ligne de type « révocation », entrée depuis l'état figé, qui nomme l'identifiant.
- La configuration est « inscrite » quand son empreinte entière se lit dans une ligne du registre courant.
- Le programme refuse un registre courant qui ne contient pas chaque ligne de l'état figé : ce ne serait pas le même registre.
- Le commit et la date sont donnés par la session ; le programme ne lit ni horloge ni dépôt.

## 5. Les valeurs de l'exemple fictif (précision de la session principale)

Le programme du constat s'arrête, sans constat ni fichier, sur :
- une empreinte de soixante-quatre zéros inscrite dans la configuration (module, rapport, registre) ;
- une ligne du registre dont l'identifiant est `GO-0000-00-00-00`, ou qui cite soixante-quatre zéros.

**Hypothèse sur la portée.** Pour les lignes du registre, seules sont regardées celles sur lesquelles le constat s'appuie : dans l'état figé, les lignes qui portent la phrase d'accord d'une livraison refaite ; dans le registre courant, les lignes qui inscrivent la configuration. Raison : le registre ne perd jamais de ligne ; un refus sur une ligne étrangère serait sans remède. Si tu veux le refus sur toute ligne du registre, c'est une ligne à changer dans `refuser_les_lignes_fictives`.

Une épreuve sur artefact pour chacune des deux valeurs, à chaque endroit, et le cas sain à côté. Le programme d'analyse ne refait pas ce contrôle : il exige le constat, que ces valeurs empêchent d'exister.

## 6. La tolérance : fractions exactes

**Écart (i), règles (α) et (β)** (`valeur_p_qui_ne_repond_pas_a_ses_comptes`). La valeur rendue est lue de son écriture décimale dans la pièce, par une seconde lecture du JSON en fractions. (α) : l'écart à la formule est de moins d'un demi-pas de la grille ; un écart égal est refusé. (β) : la valeur rendue et sa formule tombent du même côté de chacun des quinze niveaux 0,05 ÷ k, et de 0,05 pour la valeur p basse. Aucune tolérance ne se lit dans la configuration. M-3 est réglé : 0,5 contre 1 000 ÷ 2 001 est refusé.

**Valeurs ajustées** : calculées sur les valeurs rendues (un essai le fixe).

**Ce que j'ai ajouté de moi-même, à juger.** Les états se disent aussi en fractions exactes : rejets de Holm, valeur p basse contre 0,05, borne haute contre 0,60 (`rejets_de_holm_exacts`). Sans cela, une écriture longue admise par (α) et (β) changeait un état. Exemple, dans les essais : `0.0033333333333333333343` dépasse 0,05 ÷ 15, comme sa formule 7 ÷ 2 001 ; le nombre à virgule qu'on en lit, multiplié par quinze, ne dépasse pas 0,05, et Holm rejetait. De même, la valeur de la famille doit s'écrire comme la valeur p haute, et non seulement s'arrondir au même nombre ; une écriture qui dépasse 1 est refusée. Sur des écritures de six décimales, rien ne change. Relevé, point 1.

## 7. Les mineurs

- **M-1** : les constats de l'étape (m) ont dix champs ; `revision_refusee` et `taches_gardees_lues` y entrent, et la garde rejoue le journal avec eux. L'essai d'attaque (journal `["A7"]`, révision refusée) est refusé. Je confirme ces deux noms.
- **M-2** : le dossier des arrêts se lit dans `pieces_attendues.dossier_des_arrets`, chemin relatif au dossier de la configuration ; le fichier de l'étape (m) est celui du dossier de la livraison. `issues`, `table_a_apres_un_arret`, `regle_de_discretion` et `lire_fichier_des_rangs` n'ont plus d'argument pour les donner. L'essai d'attaque (dossier neuf et vide, sans pièce, renvoi dit non vérifié) n'a plus où s'écrire.
- **M-3** : voir partie 6.
- **M-4** : les motifs de la garde statique répondent sans égard à la casse. `T07/`, `Bases/`, `SONDES/`, `Mots_Et_Cout_…` sont élagués.
- **M-5** : une clé en double ailleurs que directement dans une liste fermée est une « pièce illisible », où qu'elle soit ; la désignation est celle de la pièce, sans moniteur ni dose.
- **M-6** : la chaîne `cle_du_module_dans_piece_source`, si la configuration l'inscrit, fait confronter `piece_source` à l'empreinte du module ; nulle, `piece_source` n'est pas lu et le résultat le dit (`module.confronte_a_la_livraison`). La forme de `piece_source` ne m'est pas transmise : je n'en devine aucune.

## 8. Natures, formes reconnues, booléens, fichier des rangs

- **Cinq natures** : « un champ hors de son ordre » s'ajoute ; « un champ de moins » prime sur « un champ de plus ».
- **Formes reconnues** (brouillon 28) : `effectifs` et `exclues` sont rapportés s'ils sont faits d'entiers positifs ou nuls à toute profondeur ; sinon « non rapportés (forme non reconnue) ». Les aires de la somme et du maximum de l'agrégateur sont rapportées valeur par valeur ; sinon « non rapportée ». Jamais d'arrêt, la lecture continue. L'aire de la moyenne reste sous la table des formes.
- **`true` et `false`** ne sont pas des entiers : refusés aux cinq comptes, aux réglages, aux nombres d'une lecture, à `pli`, `etiquette`, `rang` et `scores_par_unite.lignes`.
- **Fichier des rangs** : un autre nom, pas de compagnon, ou une empreinte qui n'est pas celle de `scores_par_unite.sha256` sont des gardes ordinaires, sans événement ni fichier d'arrêt. `scores_par_unite.fichier` n'est pas lu. Un fichier vide annoncé tel est lu.

## 9. Essais d'attaque repris

- `attaques_v7.py` : M-1, M-2, M-3, M-5, M-6, C-1 et C-2 ont chacun leur essai, nommé dans sa description.
- `audit_cloisonnement_v7.py` : les noms sous une autre casse sont plantés dans le faux dépôt ; le crochet d'audit prouve qu'aucun n'est ouvert ni listé.
- `attaques_cloisonnement_v7.py` : les trois modules qui manquaient aux essais (`n4`, `n5`, `n7`) y entrent.
- `fuzz_livraison_v7.py` : repris d'après sa sortie (400 livraisons, 120 fichiers de rangs) ; je n'ai pas relu son programme.

## 10. En attente, limites, réserves

- **Les cinq choix nommés** restent sans valeur par défaut ; aucune issue n'est codée comme choisie.
- **Liste des chemins à élaguer** : toujours à confirmer par le lecteur habilité.
- **Limite de M-2** : `issues` lit le dossier que la configuration donnée nomme. La configuration d'une autre course, au dossier vide, cacherait un arrêt. Ce qui tient : la configuration est inscrite au registre et citée au manifeste.
- **Limite du constat** : un constat écrit à la main, scellé, aux six bons champs, n'est pas distingué de celui du programme.
- **Portée de mes lectures** : du brouillon 28, les lignes qui diffèrent des brouillons 25 à 27 en « conventions », 6.9, 8.4 et 13 ; ses notes. Le reste n'a pas été relu.
- **Une commande dite pour mémoire** : j'ai lancé une fois, hors essai, `listages_a_relire` sur le vrai dépôt, avec ses valeurs par défaut. Elle a imprimé des noms de programmes de `scripts/`, sans rien ouvrir de cloisonné. C'est ce que fait l'essai du vrai dépôt.
