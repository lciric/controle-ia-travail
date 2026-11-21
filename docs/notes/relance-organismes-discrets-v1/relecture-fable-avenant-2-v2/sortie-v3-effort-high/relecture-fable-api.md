# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGtpiirKUSjYM8EP1Jus`
- Heure (UTC) : 2026-11-21T22:58:38Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 120000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-2-v2/consigne-relecture-v1.md` — sha256 4432ef984a4afc9247a41f3748f2501531f710e03823733b3f2128d6a34e35b7 (compagnon : vérifié)
  - correction : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-2-v2/entrees/correction-avenant-2-v2.md` — sha256 774e285102c3cb49662ad54c734d5e2e7ccd14b5f667a805c72e645032ef65b3 (compagnon : vérifié)
  - remarques : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-2-v2/entrees/remarques-verification-avenant-2-v1.md` — sha256 e1a8e580928e66a4c8ef93f9fb86029fc9d266bacdf9ec08bfda945038deb2a7 (compagnon : vérifié)
  - remarques : `docs/notes/relance-organismes-discrets-v1/relecture-fable-avenant-2-v2/entrees/remarques-decision-regime-prudent-od315.md` — sha256 f6949a2618a5ba25e8c5d72cd5df8c5e060d5ca64133f40cb3a0518c43ac303f (compagnon : vérifié)
- Empreinte de l'invite envoyée : c239835c9557f4ad75eaace7aef063b0300a6a5c743fd9901d93939487b31920
- Jetons : entrée 109526, sortie 38031 (dont réflexion 32999), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.397448 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Relecture de l'avenant 2, version 2 — verdict

**Scellable après corrections.** Les chiffres sont justes, les sept corrections sont appliquées et les trois lignes de Google sont cohérentes avec les plafonds et avec la décision OD-315. Trois retouches de texte restent à faire, aucune ne touche un chiffre ni le texte d'une ligne de calcul.

**R-1 — en-tête, « État ».** Remplacer « **Les corrections viennent de deux sources, et d'elles seules** : » par « **Les corrections viennent de deux sources** : ». Après « entrée OD-315 du journal. », insérer : « Ce qui n'en vient pas mot pour mot — demandes du mandat de la mère, lecture des pages de Google versées, lecture du chef v7 et de ses notes — est dit, changement par changement, à la section 13. »

**R-2 — section 7.** Après « les coder est une livraison de plus. », ajouter : « **Réserve du rédacteur de la version 2 (section 13.1, point 2), non vérifiée à la relecture.** Selon lui, le chef v7 exige « ; fixage publié le : AAAA-MM-JJ » à la fin de la ligne de taux, refuse la forme ci-dessus, et rien ne part alors (aucune dépense). La ligne de taux de la pièce de constat s'écrit à la forme que lit le programme qui fait foi, confrontée à sa note avant tout lancement. »

**R-3 — section 10, réserves.** Ajouter : « 16. **La ligne de taux de la section 7 est à la forme du chef v4** : selon le rédacteur de la version 2 (section 13.1, point 2), le chef v7 la refuse. À écrire à la forme du programme qui fait foi avant toute pièce de constat. »

Ces trois changements sont à consigner en 13.2, avec cette relecture pour source.

## 1. Corrections et mineurs de la vérification

| remarque | état |
|---|---|
| Correction 1, section 0 point 2 | appliqué, mot pour mot |
| Correction 1, section 10 point 1 | appliqué, mot pour mot |
| Correction 1, ligne 4, forme « levier (a) » | appliqué autrement : la parenthèse « (décision de la session mère sous GO-2026-11-21-69, R-4682) » est insérée dans le texte prescrit ; le retrait prescrit est fait à la lettre |
| Correction 2, section 4 (paragraphe et phrase) | appliqué, mot pour mot |
| Correction 2, lignes 2 et 4 | appliqué, mot pour mot ; étendu à la ligne 6 et repris en section 0 point 5 |
| Correction 2, section 9 point 8 | appliqué, mot pour mot |
| Correction 3, section 3.3 | appliqué, mot pour mot, mis en puce |
| Correction 3, section 8 | appliqué, mot pour mot |
| Correction 3, sections 0 point 4 et 10 point 2 | appliqué (phrase des 9,18 € reprise) |
| Correction 4, section 3.1 | appliqué, mot pour mot |
| Correction 4, tableau de la section 9 | appliqué, à une ponctuation près (« ; sous » au lieu de « . Sous ») |
| Correction 5, tableau | appliqué autrement : les cinq lignes sont retirées et le tableau est posé à part ; dix lignes sur onze mot pour mot ; la ligne `lignes.file-neon.delais` est récrite d'après OD-315 (levier (d) non pris) |
| Correction 5, points 2 et 9 | appliqué ; point 9 mot pour mot |
| Correction 6 | appliqué, mot pour mot |
| Correction 7 | appliqué, mot pour mot |
| m-1 | appliqué : « vaut au plus 7,30 USD (7,41 pour un envoi d'appariement) » |
| m-2 | appliqué autrement : les deux relevés sont cités au point 1 de « Ce qu'il faut relever », non au point 3 ; le point 1 est la place qui parle de ces relevés |
| m-3 | non appliqué : l'alternative est recopiée, non tranchée |

Mes jugements « mot pour mot » valent contre la copie de la vérification que j'ai reçue (sha256 `e1a8e580…`). La pièce cite `037aa7f7…` pour le fichier d'origine : je ne peux pas établir que les deux sont identiques.

## 2. Ajouts sans source dans la vérification ni dans la décision

1. **L'en-tête dit « deux sources, et d'elles seules » ; la section 13 en nomme trois**, dont le mandat de la mère, non versé au dépôt. Plusieurs changements n'ont que lui pour source : C-01, C-19, C-31, C-32, C-36, C-43, C-59 à C-62. D'où R-1 ; le mandat est à verser avec son empreinte.
2. **Le chef v7 pris pour « programme qui fait foi »** (13.1 point 1, C-19, C-31, C-46, section 12.2). La vérification s'en tient au chef v4 ; OD-315 n'en dit rien.
3. **Le contenu des pages de Google** (C-07, C-08, C-21, C-23, C-25, C-57). OD-315 autorise leur lecture, mais leurs citations sont des faits neufs que je n'ai pas pu confronter. Elles sont en texte, non en PDF comme la vérification le demandait.
4. **Les textes des lignes** :
   - les trois empreintes y sont insérées (C-32, C-36) ;
   - la ligne 6 est écrite en entier (C-35) ;
   - la clause de la dépense retirée est récrite sans texte prescrit (C-34, C-42) ;
   - « quand la file part sur un mot du directeur, » est retiré (C-38) ;
   - la forme des lignes du registre est ajoutée (C-43).
5. **Chiffres neufs, dérivés de la décision ou du mandat** : colonne et ligne « après le versement » (C-17, C-18 : 4,69 €, 4,71 €, 0,24 €) ; section 5 (C-27, C-28 : 8,09 ou 8,15 USD ; 41,07 USD). Je les ai refaits, ils sont justes.
6. **Le champ `regime_file_google`** (C-46) : le nom du champ et « une configuration définitive l'exige » viennent du chef v7.
7. **Sourcés à OD-315, sans texte prescrit** : les mentions « nœud tranché » et « régime courant écarté » (C-04, C-05, C-10 à C-15, C-53, C-55), la puce « Rien de plus avant les pièces vérifiées » (C-20).
8. **Reprises de cohérence** : C-09 et C-24 étendent la correction 2 à des places qu'elle ne nomme pas.

Aucun de ces ajouts ne contredit la vérification ni la décision. Sans la version 1, je ne peux pas confirmer que rien d'autre n'a changé hors de la section 13.2.

## 3. Chiffres recalculés

Aucun écart.

| grandeur | mon calcul | pièce |
|---|---|---|
| sortie pleine | 65 536 × 15 ÷ 10⁶ = 0,98304 | 0,98304 |
| seize envois de la file | 2 × (6 × 0,99804 + 2 × 1,05504) = 16,19664, plafond 16,50 | 16,50 |
| trois envois d'une vérification | 3 × 0,98352 = 2,95056, plafond 3,00 | 3,00 |
| excès, file | 8,07 − 0,98304 = 7,08696, soit 7,09 | 7,09 |
| excès, vérification | 2,67 − 0,98304 = 1,68696, soit 1,69 | 1,69 |
| borne du compteur au régime prudent, file | (16,50 − 1,05504) + 8,142 = 23,58696, soit 23,59 | 23,59 |
| borne du compteur, vérification | (3,00 − 0,98352) + 2,67048 = 4,68696, soit 4,69 | 4,69 |
| pire cas au régime prudent | 2 × 4,69 + 23,59 = 32,97 (exact 32,96088) | 32,97 |
| seuils par projet | 4,69 + 23,59 = 28,28 ; 23,59 | 28,28 ; 23,59 |
| taux net | 1,0990 × 0,95 = 1,04405 | 1,04405 |
| après le versement de 17,28 € | 11,93 + 10,47 = 15,59 + 6,81 = 22,40 € ; × 1,04405 = 23,38672, soit 23,38 USD | 23,38 |
| solde à voir au pire | 32,97 ÷ 1,04405 = 31,5789, soit 31,58 € (31,57 € ne comptent que 32,96) | 31,58 € |
| manque au pire, après le versement | 31,58 − 22,40 = 9,18 € par projet, 18,36 € en tout | 9,18 ; 18,36 |
| autres manques, après le versement | 27,09 − 22,40 = 4,69 € ; 27,11 − 22,40 = 4,71 € ; 22,64 − 22,40 = 0,24 € | idem |
| reprise | 16,50 − 8,142 − 1,05504 = 7,30 ; 16,50 − 8,085 − 0,99804 = 7,41 | 7,30 ; 7,41 |
| délai relevé à 5 400 s | 2 × 4,69 + 16,50 + 15,19 = 41,07 | 41,07 |

- **Arrondi du crédit.** Les résultats ci-dessus ne changent pas selon que le crédit est arrondi au centime inférieur ou au plus proche.
- **Portée de la borne.** 32,97 USD est une borne de compteur sous les trois suppositions du devis. À 400 jetons par seconde, elle vaut 46,38 USD, encore sous 84,06.
- **Risque de lecture.** « 4,69 € » (manque avant la première vérification) et « 4,69 USD » (plafond et excès d'une vérification) coïncident par hasard.

## 4. Lignes de calcul de Google

1. **Cohérence : oui.** Les lignes 2 et 6 portent 3,00, 1,69, 4,69 et 28,28 ; elles ne diffèrent que par le nom de la clé. La ligne 4 porte 16,50, 7,09, 8,09 ou 8,15, 7,30 (7,41), 32,97, 23,59 et 24,4. Le régime prudent y est dit « quelle que soit l'issue des sondes », et le passage du régime courant est retiré. Aucun crochet ne reste ouvert.
2. **Citables telles quelles, sous quatre conditions que je n'ai pas pu lever :**
   - l'empreinte `0bec479f…` de la vérification du devis ne figure dans aucune autre pièce reçue ;
   - le passage de la garde 8 repose sur la sortie d'un programme que je n'ai pas rejoué ;
   - l'empreinte de l'avenant 2 ne peut figurer qu'à la référence de la ligne du registre, et le champ qui la vérifie est « à coder » ;
   - les textes font 2 500 à 2 733 signes, contre une borne de 600 que la réserve 15 rappelle : la dérogation ou le renvoi par empreinte est à trancher avant l'inscription.
3. **Restes non bloquants, que la décision rend caducs :**
   - 2.4 et 9 point 6 disent encore « file partie sur un mot du directeur » ;
   - 9 point 5 dit encore « régime courant » ;
   - la section 6 dit la limite de mots à la sonde « à confirmer », alors que 9 point 9 la dit tranchée ;
   - 10 point 3 nomme « quatre parts » sans le régime prudent ;
   - les numéros de ligne cités sont ceux du chef v4.

## 5. Réserves déclarées

1. **Ligne de taux de la correction 6 : non bloquante pour le scellement, à porter au corps (R-2, R-3).** Le corps affirme « sans code neuf, la pièce de constat écrit… », alors que 13.1 dit cette forme refusée. Le refus ne dépense rien, mais il bloque la pièce de constat. Pour confirmer la forme du chef v7, il me faudrait le chef v7 ou la note de la livraison 6.
2. **m-3 non tranchée : réserve à porter, déjà portée** (section 7 et réserve 8). La règle des cinq jours n'entre dans aucun chiffre ni dans aucune ligne ; au cas présent, le fixage date de la veille du relevé. La trancher demande la page du calendrier de la banque, que je n'ai pas.
3. **Borne de 49 536 supposée : réserve à porter, déjà portée**, jusque dans le texte des lignes. Elle n'entre dans aucun montant, puisque la réserve est comptée à la sortie pleine. À dire à la mère : OD-315 comptait fonder la borne sur les pages versées ; la pièce conclut qu'elles ne la fondent pas et que le budget explicite n'est plus offert chez Neon.
4. **Conditions d'engagement, distinctes du scellement.** Aucune ligne de Google ne part avant :
   - le versement et une pièce de constat neuve ;
   - le champ de l'avenant 2 codé ;
   - la configuration définitive (`regime_file_google` à « prudent », seuils, plafonds) ;
   - les limites de mots inscrites par un lecteur habilité ;
   - `outputTokenLimit` constaté à 65 536 ou plus.

## 6. Limites de cette relecture

- **Pièces manquantes.** Je n'ai eu ni la version 1, ni le mandat de la mère, ni le chef v7 et ses notes, ni les pages de Google, ni le registre.
- **Indépendance.** Je suis du même modèle que le rédacteur de la version 1. Mon regard indépendant porte sur les corrections d'Opus 5.5 ; le corps inchangé repose sur sa vérification.
- **Copie relue.** Ce verdict vaut pour la copie reçue de la pièce corrigée (sha256 `774e2851…`).
