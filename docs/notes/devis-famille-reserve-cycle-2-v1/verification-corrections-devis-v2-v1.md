# Vérification des corrections du devis de la banque d'épisodes de la famille de réserve du cycle 2, version 3 — v1

- **Pièce vérifiée** (classe A, devis) : `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v3.md`, empreinte `1ab6eb4b1134d66384756a83535f031e4f4b6bfda317f362055448cf335c9804`, compagnon conforme. Avec elle : le programme de recalcul de la version 3 (`5007513108a42003…`) et sa sortie (`977573f1ec2ffb3c…`), compagnons conformes.
- **Référence** : ma vérification de la version 2, `verification-corrections-devis-v1.md` (`a94ebada4a21157a…`) : point A à corriger, mises au point B et C, information D, réserve bloquante sur la pièce 6 en version 2.
- **Pièce 6 rapprochée** : `docs/notes/scellement-2-famille-reserve-cycle-2-v1/piece-6-esquisse-de-devis-banque-d-episodes-v2.md`, branche `claude/scellement-2-famille-reserve-cycle-2-v1`, sommet `5d6b7a2aa2879eaf…`, empreinte recalculée `62b99079fb7ca999…a912`, égale à son compagnon ; version 1 du même dossier, `981c85a1911d85e4…b79a0`, recalculée.
- **Vérificateur** : Opus 5.5, même rôle que la contre-lecture et la première vérification. Je n'ai écrit ni la famille, ni l'esquisse, ni le devis, ni aucun moniteur. Fini à 2026-11-21T19:41:05Z (`date -u`).
- **Non lus** : les pièces 1 à 5 et 7 de la famille, le coffre, la valeur de `k` et de `k'`, la pièce de sécurité du banc fermé, le préenregistrement de sa course, tout fichier interdit par le mandat.

## Verdict

**Conforme.** Le point A est corrigé, les mises au point B et C sont faites, l'information D est versée, et la réserve bloquante est levée par un vrai rapprochement de la pièce 6 en version 2.

- Le programme de la version 3, relancé hors du dépôt, rend sa sortie scellée **à l'octet** (`977573f1…`). Ceux des versions 1 et 2 rendent aussi les leurs.
- Un recalcul indépendant, en fractions exactes, redonne au centime les chiffres neufs.
- Les chiffres qui tiennent : attendu au centre **172,76 dollars** (178,02 avec l'ancre par Gemini 4 Neon) ; plafond pessimiste **817** (866 avec cette ancre) ; **226** en lecture groupée (275) ; seuil d'alerte 653,60 (692,80).
- La version 3 n'introduit aucune erreur de chiffre ni de fond. Cinq mises au point d'une ligne suivent (section « Mises au point »). Aucune ne change un total, et aucune n'empêche la demande de la première tranche. Elles se règlent par un erratum, ou à la fiche de lancement.
- **Lignes de calcul** : aucune n'est engagée par cette vérification. Elle lève la condition « aucune ligne engageable avant » (`registres/decisions.md:4805`). La première tranche demandable est le **lancement 1 sur carte, 19 dollars**, puis l'essai, 22 dollars, chacune sous ses propres conditions (section « Ce qui devient engageable »).

## Point A : la règle de lancement

- **Voie retenue : la règle change** (seconde voie offerte par la vérification). Une file part si une fois et demie son coût projeté tient dans son plafond pessimiste. Son plafond est alors le plus petit de deux nombres : deux fois ce coût, ou ce plafond pessimiste. C'est la forme que je proposais. La marge, la moitié, est fixée et justifiée en 4.2 (supposée, marquée S).
- **Les quatre endroits sont repris**, et ils séparent désormais le plafond de dépense de la règle de lancement : le résumé (point 6), la table par effort de 3.3 (deux colonnes), le nœud 5 (options b et c, plus des repères), et le point 6 de la section 11. La section 10 est reprise aussi.
- **Recalculé à part** :
  - seuil du coût par question pour Opus 5.5 : 0,0654 à `k` = 6 et 0,0491 à `k` = 8 ;
  - pour Mistral au prix de repli : 0,0519 et 0,0390 ;
  - sorties équivalentes : 2 315 et 1 537 jetons pour Opus 5.5 ; 9 376 et 6 698 pour Mistral ;
  - plus haut `k` qui laisse partir la file : 14,38 à l'effort bas, 10,38 au moyen, 6,68 au haut, 2,08 à la sortie maximale du corps (règle de la version 2 : 10,78, 7,79, 5,01 et 1,56) ;
  - devis neuf à l'effort haut et `k` = 8 : 338,69 projetés, 677,38 à deux fois, soit 678 ;
  - exemples à l'attendu, `k` = 6 : plafonds 202, 72 et 143, soit 417.
- **Le devis dit maintenant ce que l'effort coûte en accords** : bas et moyen partent pour tout `k` ≤ 8 ; le haut, seulement si `k` est sous environ 6,7. C'est ce que demandait le point A. Le programme applique la règle telle qu'écrite (`regle_lancement`, tolérance de 10⁻⁹).

## Mises au point B et C, information D

- **B : fait.** 0,059 et 0,062 pour Mistral, arrondis au-dessus. L'auteur a trouvé et corrigé de lui-même le même défaut sur Opus 5.5, 0,027 devenant 0,028. 0,011 et 0,139 sont justes. Pour la borne de Neon, 1,05504 donne bien 1,056, et 1,108 avec la marge de change. Les cinq décimales sont données.
- **C : le repli sur Neon et Mistral est retiré**, ce qui règle la remarque. Le plafond de 548 disparaît.
  - L'ancre par Neon reçoit sa ligne de compte en 4.6, sa garde (garde 8) et son chiffrage sous la règle des appels aux modèles de Google (`CLAUDE.md:65-66`, empreinte `eb06c8fd…` relue).
  - Recalculé : 1,05504 dollar par envoi au pire ; 44 envois (38 × 1,15, arrondi au-dessus) ; 46,42 comptés, 48,74 avec la marge, plafond 49. L'attendu est de 0,1386 par appel, soit 5,27.
  - Réglages relus sur pièce : niveau « xhigh » admis pour Neon (`garde_google_v1.py`, `04d233bd…`) ; limite de 65 536 (page du modèle, `2eadc192…`, ligne 53 ; page de Google sur la réflexion, `fe0b8d88…`, ligne 931) ; budget de réflexion déprécié (ligne 939) ; 3 et 15 dollars à l'onglet « Standard » (page de prix du 21 novembre, `40202cdd…`) ; 5,1 jetons par mot (`garde_google_v2.py:73-74`, `9d39a749…`).
  - 49 536 de réflexion plus 16 000 de texte font 65 536 : la règle est tenue.
  - Refuser tout budget est plus strict que la garde commune, qui admet un repli déclaré au budget. C'est sans danger : un refus du niveau arrête l'envoi.
- **D : versée.** Le compte Mistral est en euros, avec un crédit d'au moins 7,87 € (`registres/go.md:674`, relue), et la recharge par Lazar est donnée pour certaine. Le second mot de Lazar est rattaché au nœud 2 et non au point 3. Ce rattachement est juste, et l'erratum de `registres/decisions.md:4807` (relue) l'appuie : l'écart réel est l'envoi de produits dérivés du coffre à un autre fournisseur.
- **Lignes neuves citées, relues derrière un filtre** : `registres/go.md:675-676`, puis `registres/decisions.md:4813`, `:4815`, `:4816`, `:4818`, `:4821`, `:4822`, `:4824`, `:4827` et `:4829`. Chacune dit ce que le devis lui fait dire, ni plus ni moins. Je les ai vérifiées pour la pièce de sécurité en version 15, les douze conditions et la règle de lecture humaine. De même pour le repli à poids ouverts, le lieu d'envoi, le gabarit écrit par le monteur « de chaque famille » et les 2 131 jetons de pensée de Neon. De même enfin pour le régime prudent et les quelque 255 et 670 dollars du bras A.

## Réserve bloquante : le rapprochement de la pièce 6 en version 2

**Levée.** J'ai lu la pièce en entier et fait moi-même la différence des deux versions (`diff`). Elle change exactement les cinq choses de la table 2 bis, et rien d'autre ne touche le devis :

| n° | changement de la pièce (relu) | dans le devis |
|---|---|---|
| 1 | D2 : au moins 5 × 20 ensembles manipulés et autant d'intacts, soit au moins 200 × `k` (au lieu de 3 × 20 × `k`) | 200 ensembles par lecteur, à l'étape 1 |
| 2 | D3, neuf : (4 × `n` × `e`) ensembles × `k'`, `k'` au coffre | 240 ensembles, en deux files (120 et 120), `k'` = `k` (S) |
| 3 | D4 : l'ancre jugée par un agent neuf, 30 questions, 30 × `p_anc` | 30 questions et 8 lectures d'admission ; Neon ou un agent Claude (nœud 1) |
| 4 | point 2 : le modèle de l'agent de l'ancre, « autre famille que les lecteurs si possible » | section 6, point 2 ; nœud 1 |
| 5 | point 3 : un monteur Opus neuf désigné (`go.md:665`) ; la main distincte à désigner | section 6, point 3 |

- **Volumes recalculés** : D1, 4 × 60 + 20 = 260 ; D2, 200 ; D3, 240 ; soit 700 ensembles par lecteur et 460 × `k` + 240 × `k'` questions.
- **Files à `k` = `k'` = 8** : 160, 2 720, 960 et 1 920 questions par lecteur.
- **Plafonds des paires de files** : 22, 368, 130 et 260. Le compte Claude fait 424 (423,94) et le compte Mistral 354 (353,46). Sans arrondi, l'engagement vaut 813,51.
- **Les postes inchangés sont bien inchangés** (`n`, `e`, `n_f`, postes A à C, ordre en deux étapes, points 4 et 5). La carte, le prix d'une question et le pire cas d'un envoi ne bougent pas : j'ai comparé leurs lignes dans les sorties des versions 2 et 3, et seul un intitulé change.
- **Placements d'auteur, déclarés comme tels** : le poste D3 lu sur les épisodes A et B (4 × `n` × `e` = 120 + 120), et le poste D3 des épisodes honnêtes à l'étape 1. Ce sont les lectures les plus naturelles. La case 5 de l'attestation couvre la seconde.
- **Concordance avec le registre** : `registres/decisions.md:4801` dit que les versions 2 changent la « lecture de l'oracle ». `:4784` dit que la famille est acceptée avec la version 2 de l'auteur, `5d6b7a2a`, la branche lue.

## Ajouts de la version 3, vérifiés

Les neuf ajouts de la section 0 bis tiennent : chiffres justes et raisons recevables.

- L'essai mesure aussi la forme du poste D3 : 12 × `k` + 8 × `k'` questions, plafond 22.
- Les exemples de la règle sont comptés au prix de repli de Mistral.
- La borne de l'ancre par Neon est le corps de l'envoi.
- L'attestation passe à six cases.
- Tout envoi de lecture est tenu pour une sortie du coffre. C'est plus prudent que la version 2.
- Le poste D3 des épisodes honnêtes a sa propre paire de files.
- Les lignes de registre neuves sont versées.
- Le monteur ordonne les envois au hasard, par tâche.
- Le doute sur le coût d'une file, qui donne un ordre de grandeur de `k`, est juste et bien posé à l'auteur de la famille.

La note des lignées et sa vérification (`596b5a73…` et `8718c80b…`, compagnons conformes) disent ce que le point 2 leur fait dire : Qwen ; Llama et Qwen ; quatre bases sans famille (lignes 33, 35 et 56) ; Claude et Gemini non exclus (lignes 32 et 33).

Rien dans la version 3 ne nomme, ne décrit ni ne suggère la famille ou un mode. Le seul chemin du coffre qu'elle porte est celui du fichier des tâches du pilote, déjà cité par la pièce 6 ; je ne l'ai pas ouvert.

## Mises au point, d'une ligne chacune, non bloquantes

1. **Seuils arrondis vers le bas dans une phrase en « non au-delà ».** « oui si `k` ≤ 6,6 ; non au-delà » (3.3, 4.2, 10, 11) laisse croire que la file ne part pas entre 6,6 et 6,68. Le seuil est 6,68. Même défaut pour la règle de la version 2, « au-delà de `k` = 7,7 » : le seuil est 7,79. `k` est une moyenne et peut tomber entre les deux. Écrire 6,68 et 7,79.
2. **Poste D2 au-delà de 200 ensembles.** Le texte en dit deux choses. En 4.2, le plafond de la file « ne bouge pas » et la règle tranche. En 9 (condition 2) et en 10, les lectures « se recalculent par la formule de 4.2 », or cette formule, (460 × `k` + 240 × `k'`) × 0,1350, fige le poste D2 à 200. Écrire la formule avec le nombre attesté `d2` : ((260 + `d2`) × `k` + 240 × `k'`) × 0,1350. Dire aussi qu'un plafond recalculé au-dessus de 368 demande un accord neuf.
3. **Coût projeté d'une file qui mêle deux formes.** La file de l'étape 2 porte des questions du poste D1 et du poste D3. Le point 1 de la règle multiplie « le » coût mesuré d'une forme par « le » nombre de questions de la file. Écrire la somme, forme par forme, du coût mesuré multiplié par le nombre de questions de cette forme. C'est ce que fait le programme, qui sépare `ens_k` et `ens_kp`.
4. **Réserve par envoi de Neon.** Garde 8 : « le compteur réserve 1,0550 dollar avant chaque envoi ». Ce chiffre suppose un corps de 24 000 octets au plus. Écrire, comme à la garde 1, que la réserve vaut le corps réel compté à un jeton par octet × 3 + 65 536 × 15 par million, soit 1,0550 au moins. L'écart est de quelques centimes.
5. **Ce qui ouvre chaque tranche.** Trois passages se croisent. La section 9 s'intitule « avant toute demande de ligne de calcul » et pose douze conditions, dont la clé Claude, l'effort et le second lecteur. L'étape 0 de 5.2 les reprend toutes. Mais 5.2 dit aussi : « première tranche demandable, après la vérification de cette version : 1 a ». Écrire, tranche par tranche, les conditions qui l'ouvrent. Ma lecture est dans la section suivante.

Une information pour la mère, déjà présente en version 2 et qui ne touche aucun chiffre. `registres/go.md:663` relève la recharge automatique de la console Mistral « coupée ». Puis `:665` dit, pour le bras A, « recharge automatique gardée allumée », sans nommer le compte. Le devis retient « coupée ». La condition 7, recharge par Lazar, couvre les deux cas, mais la phrase de 4.6 est à confirmer par la mère.

## Ce qui devient engageable

**Rien n'est engagé ni accordé par cette vérification.** Elle remplit la condition 1 de la section 9 et lève le « aucune ligne engageable avant » de `registres/decisions.md:4805`. L'accord général de `registres/go.md:668` (dépenses sur devis, jusqu'au 2026-11-22T05:30Z) ne lève pas les nœuds du devis. Je suis d'accord avec la version 3 sur ce point, et le paiement reste à Lazar.

| tranche | plafond | ce qui l'ouvre, à ma lecture du devis |
|---|---|---|
| 1 a, lancement 1 sur carte (épisodes honnêtes et de dose flagrante) | **19** | cette vérification (faite) ; nœud 3 : Lazar active la réserve ; nœud 2, question (iii) : la carte louée est un banc fermé au sens de la pièce de sécurité (4.1, « avant toute création ») ; point 4 : tâches du pilote ou tirage disjoint ; fiche de lancement, graines, manifeste (condition 9, pour sa part de génération) ; prix du jour (condition 11) ; ligne au registre (condition 12) ; accord cité par `GO_ID` |
| 1 b, essai d'admission et de mesure | **22** (34 si deux réglages d'effort) | 1 a fait ; cases 1 à 3 de l'attestation ; second lecteur arrêté et lignées levées (condition 4) ; voie d'envoi étendue à cette banque, destinataires nommés (condition 5) ; clé Claude désignée et compte du second lecteur rechargé (condition 7) ; nœud 5 tranché (condition 8) ; code des files et gardes éprouvé (condition 10) |
| 1 c et 1 d, files de l'étape 1 | 368 et 130 au plus, moins par la règle | l'essai mesuré dans les deux formes ; la règle de lancement de 4.2 ; préenregistrement de la lecture scellé (condition 9) ; cases 4 et 5 de l'attestation |
| 1 e, ancre par Neon | **49** | nœud 1 ; Google admis comme destinataire (nœud 2) ; crédit Google versé ; garde 8 et garde commune contre-lues |
| 2 a et 2 b | 18 (12,67 au débit mesuré) et 260 au plus | épreuves et préconditions passées ; règle de 4.1 pour le lancement 2, de 4.2 pour les files |

**Aujourd'hui, seule la tranche 1 a est demandable, 19 dollars, et seulement quand Lazar active la réserve et que la carte louée est admise comme banc fermé.** Les lectures ne le sont pas encore : leur second lecteur, leur voie d'envoi, leur clé et leur effort restent à trancher.

## Journal

- Refus d'outil ou de classifieur : aucun.
- Réseau : une récupération de la branche `claude/scellement-2-famille-reserve-cycle-2-v1` par `git fetch`. Aucun appel à un modèle, aucune machine, aucune dépense, aucun commit, aucune poussée.
- De cette branche, je n'ai ouvert que les deux versions de la pièce 6. J'ai vu la liste des noms du dossier, qui ne porte que les pièces 1 et 6.
- Écrit : cette pièce seule, dans ce dossier, scellée par `sha256sum`.
- Au bloc-notes de session, hors du dépôt : les sorties rejouées des trois programmes, un filtre de lecture des registres et le programme de recalcul indépendant.
- Lignes de registre lues derrière un filtre qui masque les motifs interdits par le mandat :
  - lues en entier : `registres/go.md:663` à `:679` ;
  - lues en entier : `registres/decisions.md:4777`, `:4780`, `:4784`, `:4792`, `:4803`, `:4805`, `:4807`, `:4813`, `:4815`, `:4816`, `:4818`, `:4821`, `:4822`, `:4824`, `:4827`, `:4829` et `:4830` ;
  - lues par leurs 200 premiers signes : `:4797`, `:4799` et `:4801` ;
  - aucune ligne masquée.
- Registres à la fin : `registres/go.md` s'arrête toujours à la ligne 679. `registres/decisions.md` a reçu une ligne de plus, `:4830`, qui ne touche pas cette banque. Sommet de l'arbre : `b867f0c7d`.
- Lu aussi, pour les citations : `CLAUDE.md:65-66` ; `src/controle_ia/garde_google_v1.py` (en-tête et constantes) ; `src/controle_ia/garde_google_v2.py:58-78` ; les pages de Google citées, aux lignes données ; la note des lignées et sa vérification ; la contre-lecture des trois choix, lignes 96, 99 et 154.
- Lu en passant, à déclarer :
  - `registres/go.md:663` à `:679` portent des décisions sur d'autres courses, et je n'en garde que ce qui touche cette banque ;
  - `registres/decisions.md:4818` nomme le mode connu d'une répétition générale, et je n'en garde rien ;
  - `:4816` et `:4821` portent des montants du bras A, dont je ne garde que l'ordre de grandeur cité par le devis.
