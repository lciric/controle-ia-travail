# Rapport court du rédacteur — préenregistrement court v4 et devis v3 de la course « nouvelles attaques » à six espèces — v1

- Rédacteur neuf, modèle F ; je n'ai écrit aucune version antérieure du préenregistrement court ni du devis. Écrit le 2026-11-20 ; relevés de `date -u` : 10:04:49Z avant l'écriture des pièces, 10:14:34Z avant ce rapport.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/mandat-redacteur-preenregistrement-court-v4-devis-v3-v1.md` (`4fa56789a159ba96a5496e1d5f7230c3c6179119031af85726472a5a5121da5f`, égal à son compagnon), sur GO-2026-11-20-33.
- Processeur seul : aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement du relais, du véhicule ni de la sonde, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main` (commit `da0d389cad376ad492d0255b42d7e633fea09f5a`). **Aucun refus de permission, de classifieur ni de garde.**
- Dossier de sortie : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v4/`. **Différence déclarée** : le mandat écrit un autre dossier, qui appartient à une session close ; celui-ci m'a été donné par la session qui m'a lancé.

## 1. Pièces rendues (chacune avec son compagnon `.sha256`)

| pièce | empreinte |
|---|---|
| `preenregistrement-court-course-nouvelles-attaques-v4.md` | `2dabdadf9ac126ee8d931dfde3e3507a3183b50b8f584d0f817e7ebf8adf2b10` |
| `remplacements-preenregistrement-court-v3-v4.json` (46 remplacements) | `f9500b3a7c4654338ffebf8afcaa5c0b81ebff0dd36d4c75e0b3c394421c2bbd` |
| `differentiel-preenregistrement-court-v3-v4.diff` | `5046d4a208c2e8375e4e276c200c8cb66374b19fc58c9e0ccc5dcbfba9e903b3` |
| `devis-course-nouvelles-attaques-v3.md` | `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a` |
| `remplacements-devis-v2-v3.json` (17 remplacements) | `679eb2d225395d4daa25958750152be25d879698d3aeb4912258447e93a13249` |
| `differentiel-devis-v2-v3.diff` | `627b2cb683a2ff95c5d45d111ab27afac328789ed2ea463a31325835a7017382` |
| `calcul_devis_course_nouvelles_attaques_v3.py` | `a50c9983df2acc681cbef519dc78338428b16a7942beb99d2410e4006fc00630` |
| `calcul-devis-course-nouvelles-attaques-v3.json` | `fa4bc8b0448f89fa938e44f170d17f932d8514eba71aa80241cd258a9900108c` |
| `valider_prereg_v4_v1.py` (voir § 6, écart 2) | `63a1c0bcf0375fd4bbd661aa390f763ec2f325f942728c85c567d4224e87fde7` |

Les deux journaux de l'outil de remplacement et leurs compagnons sont à côté des deux textes. Ne sont pas des pièces rendues : les deux registres extraits de `main` (`lecture-main-go.md`, `21f8f184…` ; `lecture-main-decisions.md`, `47ed2a0b…`) et le second jeu du calcul.

## 2. Remplacements

- Outil : `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, recalculée). Chaque ancre tient sur une ligne et a été comptée par `grep -c -F -e` avant l'appel : 46 ancres sur 46 et 17 sur 17 trouvées une fois.
- Préenregistrement : cible `2ea5ad53…` (v3 scellée), « FAIT : 46 remplacement(s) ». Devis : cible `714e4fc6…` (v2), « FAIT : 17 remplacement(s) ».
- Le devis v3 n'efface rien de la v2 : il ajoute des blocs marqués « v3 » ou « à six espèces ». Le préenregistrement v4 change les lignes qui dépendent du nombre d'espèces et ajoute trois blocs à la section « Seuil » : la clé de l'espèce 6, sa sonde de refus, et la table « ce qui dépend du nombre d'espèces, un par un ».

## 3. Calculs

Programme v3, parti du programme v2 (`cefe9783…`) ; joué deux fois, sorties égales à l'octet (`cmp`). Contrôles : le champ `controle_v2` rend les chiffres de la v2 pour cinq, trois et deux espèces ; le contrôle à cinq espèces des rôles Claude rend la table de la v3 (109,38 et 256,02).

Règles du rédacteur pour l'espèce 6, qui n'a aucun coût mesuré dans l'organisme : cas bas, la moyenne des cinq proposeurs de la course v9 ; cas haut, le plus cher des cinq fois le facteur du haut ; pire, onze appels à 6,05 USD. L'aiguilleur et les juges sont comptés au prorata 66/55.

| | cinq espèces | six espèces |
|---|---|---|
| par génération, bas / haut / plafond | 72,51 / 137,81 / 150 | 87,01 / 180,88 / 190 |
| seuils d'une génération | 140, 135, 120 | 180, 175, 160 |
| course, bas / haut / ligne | 217,53 / 413,43 / 450 | 261,04 / 542,65 / 570 |
| total, bas / haut / plafond | 218,72 / 419,43 / 456 | 262,23 / 548,66 / 576,01 |
| espèce 6, sur sa clé, bas / haut / pire | — | 35,19 / 88,55 / 199,65 |
| rôles Claude, bas / haut | 109,38 / 256,02 | 116,25 / 289,31 |
| rapports part / cas haut : Minuit, Luc, Rigaud | 1,547 ; 1,721 ; 1,452 | 1,290 ; 1,566 ; 1,452 (avant recharge) |

## 4. La ligne neuve à demander à Lazar

**Ligne de course de 570 USD exactement (trois générations à 190 USD), plafond total de 576,01 USD** : 570 + 5 (épreuve des témoins) + 1 (sonde de refus des espèces 1 à 5) + 0,01 (sonde de refus de l'espèce 6, sur sa clé). Attendu 262,23 USD. Avec elle : la part au pire de la clé de l'espèce 6, 199,65 USD, comprise dans la ligne. Variante chiffrée au devis, § 9 : garder 450 USD (total 456,01) ; au cas haut, les juges ne sont alors pas lancés.

## 5. Points que la lettre de GO-33 ne tranche pas — écrits en remarque, non tranchés

1. **Le plafond.** GO-33 ne dit rien du montant. J'ai appliqué la règle du plafond du devis v2 (§ 3) à six espèces, ce qui donne 570 USD ; le préenregistrement v4 est écrit sur ce montant, « sous réserve du mot de Lazar ». S'il retient 450 USD, le préenregistrement se récrit (seuils, arrêts n° 6 et 7, parts au pire).
2. **Le coût de l'espèce 6.** Aucune mesure. Les trois règles sont les miennes. Le registre note un tarif de 2 et 10 USD par million de jetons (R-813, R-1780) : je ne l'ai pas relu sur la page du fournisseur ; il n'entre dans aucun total, et n'est cité qu'au devis. À ce tarif le cas bas est sans doute large.
3. **Le pire d'un appel de l'espèce 6.** J'ai pris 6,05 USD, le pire écrit pour les proposeurs de la course v9 ; il est à confirmer par le tarif et la sortie maximale de la configuration (valeur ouverte du préenregistrement).
4. **Le nom de la clé.** `KIMI_API_KEY` est le nom que porte le registre des décisions ; la variable est présente dans mon conteneur (vérifiée par `[ -n "${KIMI_API_KEY:-}" ]` seulement, code 0). Que ce soit la clé du conteneur qui jouera la course, et que son solde soit lisible, reste à dire par la mère.
5. **Les juges et l'aiguilleur.** Laissés inchangés, GO-33 n'en disant rien. Ils lisent 20 % de fiches en plus : c'est ce qui serre Minuit (rapport 1,290).
6. **La diversité.** GO-2026-11-20-32 note que Lazar juge cette espèce peu diverse ; GO-33 la fait entrer. Aucune mesure de la course ne dit ce qu'elle apporte : l'oracle par espèce n'existe pas (N-058). Le lecteur d'antériorité « d'une autre famille que le proposeur si possible » garde sa règle ; je n'ai rien ajouté sur la lignée de l'espèce 6.
7. **GO-2026-11-20-34 (recharge de Rigaud).** Il change des lignes des deux textes, et je l'ai cité à la lettre : la part de Rigaud se lit sur « le solde relu après recharge », moins 8,35 ; les 47, 38,65 et 415,21 USD sont dits « d'avant la recharge ». Le mandat, écrit avant GO-34, ne le listait pas : c'est la note de la session qui m'a lancé qui me le fait porter. Non tranché : le montant de la recharge ; la manière de relire le solde (la v3 dit les soldes Claude « calculés ou déclarés, jamais lus ») ; faut-il rejouer la règle de répartition sur le solde rechargé (je ne l'ai pas fait : GO-22 fixe la répartition, GO-34 garde la part sur Rigaud).
8. **X = 8,35 USD et la borne de 415,21 USD.** L'espèce 6 ne change ni l'un ni l'autre. La borne couvre moins : 1,435 fois le cas haut des rôles Claude au lieu de 1,622 ; au pire, la ligne la dépasse de 154,79 USD au lieu de 34,79, et c'est l'arrêt n° 12 qui tient.
9. **La sonde de refus de l'espèce 6.** Le mandat fixe son plafond (0,01 USD) et son modèle (la sonde de la clé Luc). J'ai écrit qu'elle envoie la question scellée seule, en une requête, à sortie bornée ; la borne en jetons est une valeur ouverte, et la question fait 10 562 octets : si le pire de la requête ne tient pas sous 0,01 USD au tarif du relais, la sonde ne part pas et une ligne neuve se demande. Qu'elle s'ajoute à la ligne de 1 USD plutôt que d'y entrer est ma lecture.
10. **Pièces citées par la v4 mais non récrites.** L'ordre de course v3 et le rapport de conception v3 citent le devis v2 et la composition de la course v9 ; je ne les ai pas touchés. La v4 cite le devis v3 et son calcul au chemin `NA/preenregistrement-court-v4/`, « où la mère le verse » : à corriger s'il diffère.
11. **GO-2026-11-20-08.** Je ne l'ai pas relu ; la v4 dit seulement que la v3 le cite pour 450 USD et qu'il ne couvre pas la ligne neuve.
12. **GO-2026-11-20-20 et -31.** Lus comme le mandat le demande ; ils portent sur le bras A et ne changent aucune ligne. Remarque : GO-31 change les lecteurs du bras A, donc peut-être son besoin sur Rigaud ; X reste celui de GO-22.

## 6. Écarts

1. Le dossier de sortie (en tête).
2. `valider_prereg_v4_v1.py` : le mandat demande de vérifier la v4 par `python3 -B -m controle_ia.prereg`. Ce module n'a pas d'entrée en ligne de commande : la commande, `--help` compris, ne rend rien. J'ai donc écrit un script de quinze lignes qui appelle `controle_ia.prereg.problemes` et n'écrit rien. Résultat sur la v4 : toutes les sections présentes ; un seul problème, attendu, « section vide ou à remplir : Contre-lecture » (l'entrée « Contre-lecture 4 » est laissée à remplir). Sur la v3, en témoin : aucun problème.
3. J'ai retiré de mon dossier deux sorties de brouillon du calcul, écrites avant une correction du programme (égalité de deux répartitions mal rapportée), puis rejoué le programme deux fois.
4. Une commande a listé les têtes de lignes du registre des décisions extrait de `main` (un seul fichier, dans mon dossier) ; elle était inutile. Rien d'interdit n'a été ouvert.
5. La section « Contre-lecture » de la v4 reçoit une entrée « Contre-lecture 3 » pour le contrôle v2 → v3 (`5039197f…`), que la v3 ne pouvait pas porter, et une entrée « Contre-lecture 4 » à remplir.

## 7. Aucune recette

Les ajouts portent sur des montants, des numéros d'espèces, des noms de variables, des règles d'arrêt et des renvois. Ils ne contiennent aucune méthode d'attaque, aucun procédé, aucun identifiant de modèle, aucune valeur de clé. Le nom de variable `KIMI_API_KEY` est écrit comme le mandat le demande.

— rédacteur neuf, modèle F
