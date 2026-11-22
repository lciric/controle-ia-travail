# Passation — rédacteur du préenregistrement v11 de la course d'affinage, brouillon 3 et devis v11b

- Écrite le 2026-11-22T20:34:12Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v8-v1`. Elle suit la passation `2026-11-22-1958-redacteur-preenregistrement-affinage-v11-brouillon-2.md`, qui reste en place et dont les réserves valent encore.
- Aucun appel à un modèle externe, aucune dépense, aucune instance de calcul.

## Fait

Seul objet : porter un fait lu par Lazar à la console, le seuil de déclenchement de la recharge automatique de la clé LUC, 5 USD (registre des décisions de `main`, R-5042, relu au commit `61ec4bb16537d899d431fe7a74d10b0c17053d86`), et ce qu'il implique pour le risque de refus pendant le délai de recharge.

| pièce | chemin, sous `docs/notes/organisme-affinage-mentors-v1/` | sha256 |
|---|---|---|
| devis v11b (le devis v11 plus le § 5 bis ; aucun chiffre du v11 ne change) | `devis-course-affinage-mentors-v11b.md` | `13d962b1c56f17235e1e4b90b9b166239c5bb6d0c1bb6c400b3f07ac59a88c03` |
| programme de calcul v11b (131 chiffres contrôlés ; les 116 du v11 inchangés) | `course-v11/calcul-devis-course-affinage-mentors-v11b.py` | `cf316ba4db4005e2d64a114f4f4aea93187ebfa372a3bf072594e5513f8cd0e6` |
| brouillon 3 du préenregistrement v11 (326 lignes, 14 lignes du brouillon 2 touchées, aucune ajoutée ni retirée) | `course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-3.md` | `af226efacd7775ab651e10ec9f0e5c25bd60bebcca72094ab5dc8aab4d1927c0` |
| programme d'assemblage du brouillon 3 | `course-v11/assembler-brouillon-3-preenregistrement-v11.py` | `d0a955a414a9385b206b0f090605b683c109ea1e3208d3bff687e0e9c8ba6223` |

Les brouillons 1 et 2, le devis v11 et son programme de calcul restent en place (R12). L'annexe du brouillon 2 (`abb967a9e2190f0ca607e8f136e1527105137d42c8225ed8f30a8234f9096b95`) vaut ligne pour ligne pour le brouillon 3 : ses 70 citations y sont retrouvées aux mêmes lignes.

Rejeu du brouillon 3, à l'octet près : `python3 -I course-v11/assembler-brouillon-3-preenregistrement-v11.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-2.md <sortie> 2026-11-22T20:33:49Z`.

Contrôles : 17 sections identiques à la v10 scellée, hors saut de ligne final ; chaque nombre neuf retrouvé dans la sortie du programme de calcul v11b.

## Ce que le seuil implique, tel qu'écrit

Si le solde est au-dessus de 5 USD, la recharge se déclenche alors qu'il reste près de 5 USD : aux prix par appel du devis, c'est plus que tout l'aiguillage et 84 % de la part Claude des juges ; un refus pendant le délai de recharge suppose donc une recharge qui tarde à l'échelle d'une étape, ou qui échoue. Trois cas restent entiers : des sessions près de leur plafond ; un solde déjà sous 5 USD au départ (il n'est pas lu) ; une recharge qui échoue ou qui a épuisé ses 40 euros. La règle ne change pas : arrêt au premier refus, sans relance.

## Reste, réserves, prochaine action

Inchangés depuis la passation de 19:58Z. En plus : la valeur du plafond de session des juges (1,00 ou 1,10 USD) suivra la convention de la commande d'Argon, selon la session de l'organisme ; à 1,10 USD, un devis et un texte à ce chiffre sont à écrire. Le délai de la recharge, le montant de chaque recharge et ce qu'elle fait sous le seuil ne sont dans aucune pièce lue.

## Instances actives

Aucune.
