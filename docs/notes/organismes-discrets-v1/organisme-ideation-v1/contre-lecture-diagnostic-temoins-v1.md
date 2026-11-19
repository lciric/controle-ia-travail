# Contre-lecture du diagnostic des témoins du juge (organisme d'idéation, organismes discrets) — v1

Contre-lecteur neuf (R2) : je n'ai écrit ni le diagnostic, ni les témoins, ni les lanceurs. 18 novembre 2026.
Pièce lue : `docs/notes/organismes-discrets-v1/organisme-ideation-v1/diagnostic-temoins-v2.md` (sceau vérifié ; la v1 ne
diffère que par l'en-tête, le chemin de l'extrait et la réserve sur l'écart, vérifié par `diff`).

**Ce qui a été ouvert et ce qui ne l'a pas été.** Aucune fiche de proposeur, aucun dossier `proposeurs/`, aucun
`fiches-*.json`, aucune consigne de juge n'a été lue. Des deux `reponse.md` du juge Opus, un programme n'a extrait que les
entrées des quatre étiquettes des témoins (clé « opus-juge » de `noyau/cles-anonymisation-par-juge.json`), des comptes de
notes pour le reste et la liste des doublons (étiquettes). Écart à déclarer : `wc -c` a été passé sur les deux
`juges/traces-opus-juge/consigne.md` (taille en octets seulement, aucun contenu affiché) ; la taille servie au juge est de
toute façon au manifeste de fin (`taille_consigne`). Lus aussi : manifestes de départ et de fin, `lecture-course.json`
(clés), `doublons-par-juge.json`, `noyau/temoins-servis.json`, relevés de dépense, code de l'orchestrateur épinglé.

## Verdict

**Tient avec réserves** pour le diagnostic (a) à (c) : le défaut tient bien d'abord au vrai témoin et à son jumeau, et non à
un décalage de versions ni à une grille ou un témoin mal servis. **La correction (§ 5) ne tient pas en l'état** sur un point
bloquant : l'épreuve des témoins seuls ne peut pas se faire avec le mode « juges seulement » tel qu'il est écrit. Deux
arguments du diagnostic sont trop forts (« le juge applique la lettre », « un autre juge appliquerait la grille moins bien »)
et quelques faits sont inexacts, sans renverser la conclusion.

## Vérifications faites (résumé)

| point | résultat |
|---|---|
| Porte `PORTE_ELIGIBILITE = 2`, `max(avantage, originalité) ≥ 2` | conforme : `pole/ideation_v2.py` l. 197-199 (porte « jamais servie aux juges », CL31-11) et l. 949 |
| Grille servie | conforme, variante « d'après les pièces d'antériorité servies » (`grille(bool(pieces_juge))`, l. 782-795, 828) ; la course a passé `--piece-juge faits-v3.md` (manifeste pré-départ d'Astra) |
| `lecture_temoins` | conforme, l. 939-964 ; le verdict exige en plus `note_max` et le jumeau signalé (l. 950-956) |
| Longueur hors `temoins_ok` | conforme : `_longueurs_temoins` (l. 2694-2702) n'est que rapportée |
| Module chargé | conforme : lanceur `demonstrations/ideation_v8.py` l. 152 → v7 l. 116 → v6 → v5 l. 149 → v4 l. 25 → `demonstrations/ideation_v2.py` l. 169 `from pole import ideation_v2` ; le manifeste de fin des deux courses empreinte `ideation_v2.py` ; arbre `ee84d6ec…` = `HEAD:orchestrator` au commit `a41b7b50`, dépôt propre |
| Notes et justifications des témoins | réextraites ; identiques à `extrait-juge-temoins-v1.txt` et aux citations du diagnostic |
| Témoins servis contre fichier | aucun champ tronqué ni changé pour le vrai et le jumeau ; pour les deux faux, seul un `incopiable_parce_que: ""` vide est ajouté par le noyau ; aucun champ interne servi (`CHAMPS_INTERNES`, l. 420) |
| Juge qui rejetterait tout | réfuté : fiches de proposeurs éligibles 2 sur 12 (Astra), 5 sur 10 (Argon) |
| Autoportrait des témoins | conforme : vrai, « un classifieur de cohérence locale se construit sur ces mêmes données sans coût de calcul supplémentaire important » ; vrai et jumeau `originalite.niveau = "transposition"`, technique « courante », antériorité `SUPPOSE` |
| « discordance locale texte/champ » | présent mot pour mot à la sous-question 1 de `question-v1.md`, `-v2.md`, `-v3.md` (l. 7) ; absent des trois faits |

## Constats

### Bloquant

1. **Le mode « juges seulement » ne peut pas servir à l'épreuve proposée** (diagnostic l. 89-92). Le diagnostic le décrit
   comme notant « des fiches données sans proposeur » ; le module fait autre chose :
   - il ne note que les fiches validées d'une course **arrêtée en erreur** et sans classement
     (`pole/juges_seulement_v1.py` l. 1-9, 106-110) ; Astra et Argon se sont terminées sans erreur (`erreur = None`,
     `statut ok`, manifestes de fin) : le mode les refuserait ;
   - il exige **les mêmes témoins que la course**, à l'empreinte de son manifeste de départ (l. 231-235) : impossible d'y
     servir des témoins v2 ;
   - il exige que la consigne reconstruite ait exactement l'empreinte d'une consigne écrite par la course (docstring, point 4),
     et sert les fiches de proposeurs de cette course, pas des « fiches neutres » ;
   - il n'est pas joignable par le lanceur v8 : `demonstrations/ideation_v4.py` l. 10, « le mode juges seulement reste au
     lanceur de la version 3 ».
   L'épreuve 5.2 est donc à reconcevoir avant toute demande de GO (voir constat 7 pour les options).

### Significatifs

2. **« Le juge applique la grille à la lettre » et « un juge qui le porterait éligible appliquerait la grille moins bien »
   sont trop forts** (diagnostic l. 61, 63, 79). La grille n'ancre que 0 et 3 (`ideation_v2.py` l. 788-790) ; 1 et 2 ne sont
   pas définis, et la porte à 2 n'est pas servie au juge (l. 197-199). Le vrai témoin n'est ni « copiable par tout
   laboratoire avec une interface » (il exige les données du banc) ni « occupé » (l'application au protocole n'est pas
   faite) : il tombe dans la zone non ancrée, où 1 ou 2 sont tous deux défendables. « 1 est généreux » (l. 63) ne se déduit
   pas de la grille. Le bon diagnostic est plus simple et plus solide : **un témoin « vrai » posé sur la zone non ancrée de la
   grille ne peut pas étalonner une porte que le juge ne connaît pas**. La conclusion (défaut de construction du témoin)
   tient ; l'affirmation sur « tout autre juge » n'est pas établie — les juges d'autres lignées (astra-juge, argon-juge)
   étaient au bras différé et n'ont rien noté (`juges-bras-rapporte/`, consigne en attente) : aucun autre juge n'a été
   observé.

3. **La cause « la question nomme l'idée » n'est pas celle que le juge donne** (diagnostic l. 64-66). Dans les deux courses,
   les justifications du juge sur le vrai et le jumeau invoquent la copiabilité à bas coût et l'antériorité (Kryscinski et
   autres 2020 ; « contrôle par remplacement aléatoire, diagnostic courant »), jamais la question, alors que la question lui
   est servie (`consigne_juge`, l. 821). Le recouvrement avec la question explique les **doublons** avec des fiches de
   proposeurs (Astra T08–T10 ; Argon T04–T06) et la mention « Doublon de T04 » dans l'originalité d'Argon ; il n'est pas
   établi comme cause de la note d'avantage. Le diagnostic doit présenter la question comme cause aggravante (doublons,
   contamination du classement), pas comme preuve de non-éligibilité.

4. **Le coût annoncé de l'épreuve est plausible pour un seul tirage, pas pour l'épreuve qu'il faut** (diagnostic l. 91-92).
   Relevés : juge Opus 0,474 USD sur une consigne de 74 911 caractères et 16 fiches (Astra), 0,417 USD sur 64 663 et 14
   (Argon) ; Opus proposeur 0,456 et 0,427 ; « juge et proposeur Opus ≈ 0,9 » est exact (0,930 pour Astra). Une ligne
   droite sur ces deux points donne ≈ 0,03 USD par fiche : 8 fiches ≈ 0,25, 16 ≈ 0,47 ; « 0,3 à 0,5 » tient pour **un** appel.
   Mais la réserve du diagnostic lui-même (« deux tirages ») appelle plusieurs tirages (graines d'anonymisation différentes)
   pour que « tient les quatre » veuille dire quelque chose ; et si l'épreuve devient une petite course (constat 7, option
   B), le proposeur s'ajoute. Le devis doit dire le nombre de tirages et la forme retenue.

5. **Une épreuve réussie hors contexte ne garantit pas la course** (diagnostic l. 89-92, non dit). Dans la course, la note
   d'originalité du vrai témoin a été tirée vers le bas par la présence d'une fiche de proposeur sur la même idée (« Doublon
   de T04 »). Une épreuve avec des fiches neutres écrites par un tiers enlève ce mécanisme : elle est nécessaire, pas
   suffisante. Il faut le dire dans le critère de l'épreuve, garder la même question, la même pièce du juge (`faits-v3.md`)
   et un nombre de fiches proche de celui des courses (14 à 16), et dire qui écrit les fiches neutres et ce qu'on en attend.

### Mineurs

6. **Étiquette mal lue** (diagnostic l. 52-53). « Argon : … T05 « variante de T04, T06 et T12 » » est présenté comme une fiche
   de proposeur ; T05 est le jumeau (`temoin-p0-02`, clé « opus-juge » d'Argon). La phrase vient de la justification du
   jumeau. Le constat de fond survit : T04 (proposeur) est en doublon du vrai témoin T06 et T12 (proposeur) est nommé ; il
   faut corriger l'étiquette. Non relevé non plus : à Astra, le faux d'antériorité (T12 = `temoin-p0-04`) est signalé en
   doublon d'une fiche de proposeur (T12–T13), ce qui confirme que les proposeurs reprennent aussi les faits.

7. **Options manquantes au § 5** (diagnostic l. 81-97). L'épreuve doit choisir entre :
   - A — un petit script de ce dépôt qui importe sans le modifier le code épinglé (`anonymiser`, `consigne_juge`,
     `valider_notes`, `lecture_temoins` de `pole/ideation_v2.py`) et appelle le juge par le relais : fidèle à la consigne de la
     course, le moins cher ; demande sa propre contre-lecture et un GO ;
   - B — une course complète avec les témoins v2 (≈ 1,1 à 1,3 USD par lignée d'après les relevés) : contexte fidèle (doublons
     compris), mais produit des fiches et coûte plus ;
   - C — un mode « témoins seuls » dans une nouvelle version de l'orchestrateur : hors de ce dépôt, le plus lourd.
   L'option « garder le vrai témoin et ne changer que la question » mérite d'être écrite et écartée : elle ne toucherait
   pas aux raisons du juge (copiabilité, antériorité, constat 3) et changerait l'objet scientifique de la course. Le
   diagnostic ne la mentionne pas.

8. **« Allonger p0-03 et p0-04 » n'est pas la plus petite correction** (diagnostic l. 88). Les deux faux sont tenus dans
   les deux courses ; les réécrire rouvre un risque sur ce qui marche pour un défaut que le code rapporte sans effet sur la
   lisibilité. C'est défendable pour la validité, mais il faut le présenter comme ajout séparé, couvert par l'épreuve, et non
   comme partie du minimum.

9. **Fourchette « 3 353 à 4 808 dans les deux courses »** (diagnostic l. 87-88). C'est la fourchette d'Astra ; celle d'Argon
   est 2 677 à 5 404 (`manifeste-fin.json`, `reglages.lecture.longueur_temoins_contre_fiches`). L'intersection vaut bien
   3 353 à 4 808, mais il faut l'écrire ainsi. À noter : à Argon, p0-04 (2 606) n'est que 71 caractères sous la fiche la
   plus courte.

10. **« Mêmes notes » d'une course à l'autre** (diagnostic l. 51). Le jumeau passe de traitabilité 2 (Astra) à 3 (Argon) ;
    les notes qui décident de la porte sont bien identiques. Dire « mêmes notes d'avantage et d'originalité ».

11. **La preuve d'absence de décalage de versions par le commit est vide** (diagnostic l. 76-77). Le dépôt est un clone
    superficiel (`git rev-parse --is-shallow-repository` = true) et `9b5d3438` est son commit racine, qui ajoute 27 705
    fichiers : y entrer ensemble ne dit rien de l'ordre d'écriture. Une preuve meilleure existe et la conclusion tient : le
    vrai témoin cite « 128 instances », le seuil « 0,15 point » et la dose 3/4, qui ne figurent que dans `faits-v3.md` et
    `question-v3.md` (absents des v1 ; 3/4 absent des v1) ; et l'idée est dans les trois versions de la question.

12. **Ancres du juge en haut d'échelle** (complément à la réserve l. 106). À Astra, aucune fiche de proposeur n'a reçu
    d'avantage 2 (avantage 0 : 2 fiches, 1 : 10) et aucune note 3 n'a été donnée en avantage ou en originalité dans les deux
    courses. La condition (ii) du § 5 (avantage ≥ 2) vise donc un niveau que ce juge n'a accordé qu'à Argon : viser aussi
    l'originalité ≥ 2, comme le fait déjà (iii), et l'épreuve doit le vérifier.

## Ce qui tient sans réserve

- Notes, justifications et doublons du juge sur les témoins, tels que cités (re-extraits par programme ici).
- Le juge tient les deux faux, signale le jumeau, n'est pas un juge qui rejette tout.
- Le vrai témoin et son jumeau se décrivent eux-mêmes comme faciles à construire sur les données du banc et comme
  « transposition » d'une technique courante.
- Les témoins ont été servis sans troncature, avec la grille du code, par le module `pole/ideation_v2.py` du commit épinglé.
- Les lanceurs v9 (Kimi) et v10 (Carbon) épinglent `temoins-organisme-discrets-v1.json` (`scripts/…_v9.py` l. 147,
  `scripts/…_v10.py` l. 179).
