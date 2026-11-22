# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ19Sfx2PhSksJpgrA2L`
- Heure (UTC) : 2026-11-22T12:59:12Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 128000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/attaquant-informe-v1/course-brouillon17-v1/demande-brouillon17-remplacements-v2.md` — sha256 dcb24c356f6d3be7b189fcdcbee3eb71a95296e73f14f14ff9da3d760d3fc429 (compagnon : vérifié)
  - correction : `docs/notes/attaquant-informe-v1/course-brouillon17-v1/copies-sans-nom-v1/course-banc-ferme-v1-brouillon16-marques-v1.md` — sha256 40fd2ce33eeb50d66924140bcaccaeeb8a25c7b70833e0385eba565c4fe536f4 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/course-brouillon17-v1/copies-sans-nom-v1/verification-corrections-brouillon16-v1-copie-sans-nom-v1.md` — sha256 cbdbaae86f01fdfa8ef056285ecc1ab8e99c33b0d089e38e35185452e151823d (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/course-brouillon16-v1/reponse-v1/relecture-fable-api.md` — sha256 83371480a3358394f7fecde7ecd6897fb48460941e34c63dc72b7ac0401014fb (compagnon : vérifié)
- Empreinte de l'invite envoyée : e6f3dae4033a1a8e9813a326ee2757dadf3bb80497025b621b8c922e788eef4c
- Jetons : entrée 84320, sortie 20860 (dont réflexion 14553), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.508960 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
Motif 1 : point 8 — le titre se désigne « brouillon 17 ».
<<<ANCIEN 1
v1, brouillon 16, candidat à la version définitive
===NOUVEAU 1
v1, brouillon 17, candidat à la version définitive
>>>FIN 1

Motif 2 : point 7 — défaut ancien : le paragraphe d'état disait « la même contre-lectrice », alors que les brouillons 15 et 16 ont été lus par un contre-lecteur neuf, le même pour les deux.
<<<ANCIEN 2
la vérification des corrections par la même contre-lectrice, et le mot
===NOUVEAU 2
la vérification des corrections par qui a fait cette contre-lecture — pour les brouillons 15 et 16, un contre-lecteur neuf (Opus 5.5), le même pour les deux —, et le mot
>>>FIN 2

Motif 3 : point 8 — la phrase d'état du brouillon 16 devient un fait d'histoire ; son empreinte est celle que donne le commentaire de la copie servie.
<<<ANCIEN 3
**Ce brouillon 16 porte ceci, et rien d'autre :
===NOUVEAU 3
**Le brouillon 16 (`d0c767b377a5dfd6a8994ddb926a6d49e9103535e8bba12d688cfe69f7c2cf3f`, archivé lui aussi) portait ceci, et rien d'autre :
>>>FIN 3

Motif 4 : point 8 — le paragraphe d'état dit ce que le brouillon 17 porte de neuf.
<<<ANCIEN 4
aucun critère de lecture gelé ne change.** Les brouillons 1 (
===NOUVEAU 4
aucun critère de lecture gelé ne change.** **Ce brouillon 17 porte ceci, et rien d'autre : les corrections de la vérification du brouillon 16 (« à corriger » : un majeur nouveau, le reste acquis ou mineur) — le cas où la règle de l'oracle ne peut pas appliquer son seuil sans les contrôles hors gabarit, écrit « rien ne part ; nœud pour ⟦D⟧ » en D6 et à la ligne d'arrêt jumelle, avec l'attestation du monteur à l'addendum O ; le monteur ne lit pas les sorties du jugement par programme ; ces sorties aux entrées des agrégats ; les signalements à ⟦D⟧ et un nœud ouvert, sous « Champs ouverts et nœuds » ; la colonne de [GO85] ; les dates ; la mention d'attente du champ n° 19 ; deux défauts anciens — la ligne d'arrêt de la seconde confirmation, et « la même contre-lectrice » dans ce paragraphe ; l'en-tête. Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance, aucun critère de lecture gelé ne change.** Les brouillons 1 (
>>>FIN 4

Motif 5 : point 8 — la ligne « Auteur » nomme l'auteur du brouillon 17 ; ce qu'elle dit des brouillons 15 et 16 reste tel.
<<<ANCIEN 5
**Pour les brouillons 15 et 16**
===NOUVEAU 5
**Auteur du brouillon 17** : le même Claude Fable 5.2, appelé de même ; il n'a lu que la copie marquée du brouillon 16, le rapport de la vérification de ses corrections et sa propre réponse précédente ; il n'a lu ni le lot, ni les sorties, ni le coffre, ni le registre, et n'a conçu aucun moniteur ; le signalement à ⟦D⟧ qui suit vaut aussi pour lui. **Pour les brouillons 15 et 16**
>>>FIN 5

Motif 6 : point 6 — dates des brouillons 15 et 16 ; celle du brouillon 17 garde la marque.
<<<ANCIEN 6
vers 12:44 UTC ; brouillon 16 : [heure lue par date -u au scellement]
===NOUVEAU 6
vers 12:42 UTC ; brouillon 16 : 2026-11-22, vers 12:51 UTC ; brouillon 17 : [heure lue par date -u au scellement]
>>>FIN 6

Motif 7 : point 5 — la colonne des empreintes de [GO85] ne dit plus « non recalculées ».
<<<ANCIEN 7
valeurs fournies par la session qui a appelé l'auteur du brouillon 16, qui ne les a pas recalculées et n'a pas lu le registre
===NOUVEAU 7
valeurs fournies par la session qui a appelé l'auteur du brouillon 16 ; recalculées par le vérificateur des corrections du brouillon 16 et trouvées justes, selon son rapport ; l'auteur des brouillons 16 et 17 ne les a pas recalculées et n'a pas lu le registre
>>>FIN 7

Motif 8 : point 9 — le champ n° 19 reçoit la mention d'attente, sous la forme des autres champs ; le marqueur reste, rien n'est rempli.
<<<ANCIEN 8
— fournisseur, image, type de carte.
===NOUVEAU 8
(attend l'étalonnage du saboteur à budget) — fournisseur, image, type de carte.
>>>FIN 8

Motif 9 : point 1 — D6, puce « Contrôles hors gabarit » : la limite du repli est écrite, avec l'attestation du monteur à l'addendum O.
<<<ANCIEN 9
aux lecteurs externes. **Le mot de ⟦D⟧ ne fixe
===NOUVEAU 9
aux lecteurs externes. **Limite du repli.** Si la règle scellée de l'oracle ne peut pas appliquer son seuil sans les contrôles hors gabarit, **rien ne part ; nœud pour ⟦D⟧**. Le dommage tenu ne se mesure jamais en silence sur une partie des contrôles (R5). Le monteur de l'oracle atteste, sans contenu, à l'addendum O, que ce cas ne se présente pas ; s'il ne peut pas l'attester, c'est ce cas. **Le mot de ⟦D⟧ ne fixe
>>>FIN 9

Motif 10 : point 2 — D6 (i) : le monteur ne lit pas les sorties du programme qu'il lance.
<<<ANCIEN 10
Les sorties de ce programme sont scellées en quarantaine avant le second temps.
===NOUVEAU 10
Le monteur ne lit pas les sorties de ce programme : elles sont scellées en quarantaine avant le second temps.
>>>FIN 10

Motif 11 : point 2 — D8 : la même chose, là où le monteur est désigné comme lanceur.
<<<ANCIEN 11
([GO85] ; D6, choix de conception de l'auteur) ;
===NOUVEAU 11
([GO85] ; D6, choix de conception de l'auteur) ; il n'en lit pas les sorties, scellées en quarantaine ;
>>>FIN 11

Motif 12 : point 3 — déroulement, point 9 : les sorties du jugement par programme entrent dans les agrégats.
<<<ANCIEN 12
de la table de correspondance et des réponses des lecteurs
===NOUVEAU 12
de la table de correspondance, des réponses des lecteurs et des sorties scellées du jugement par programme des contrôles hors gabarit (D6)
>>>FIN 12

Motif 13 : point 1 — la ligne d'arrêt jumelle porte le même cas ; sa part sur les jumeaux ne change pas.
<<<ANCIEN 13
il ne se ramène pas au gabarit pour ce qui part
===NOUVEAU 13
il ne se ramène pas au gabarit pour ce qui part ; ou sa règle scellée ne peut pas appliquer son seuil sans les contrôles hors gabarit, ou le monteur de l'oracle n'atteste pas à l'addendum O que ce cas ne se présente pas (D6, limite du repli)
>>>FIN 13

Motif 14 : point 1 — l'attestation entre à la liste de ce que porte l'addendum O.
<<<ANCIEN 14
; attestation de provenance par empreinte (chaque paramètre
===NOUVEAU 14
; attestation du monteur de l'oracle, sans contenu, que la règle de l'oracle applique son seuil sans les contrôles hors gabarit (D6, limite du repli) ; attestation de provenance par empreinte (chaque paramètre
>>>FIN 14

Motif 15 : point 7 — défaut ancien : la ligne d'arrêt de la seconde confirmation disait « points 8 et 21 », alors que la condition 17 dit 8, 18 et 21.
<<<ANCIEN 15
(points 8 et 21) absente après
===NOUVEAU 15
(points 8, 18 et 21) absente après
>>>FIN 15

Motif 16 : point 10 — la phrase « aucun nœud ne reste ouvert » est accordée avec le nœud ouvert que la mère demande d'inscrire.
<<<ANCIEN 16
Aucun nœud de cette liste ne reste ouvert ;
===NOUVEAU 16
De ces deux nœuds, aucun ne reste ouvert ; un nœud reste ouvert pour ⟦D⟧, le 15, écrit après eux ;
>>>FIN 16

Motif 17 : points 10 et 4 — le nœud ouvert et les signalements à ⟦D⟧ entrent sous « Champs ouverts et nœuds », à la fin de la section.
<<<ANCIEN 17
## Réserves, et ce que l'auteur n'a pas lu
===NOUVEAU 17
15. **Questions qui diffèrent entre jumeaux : nœud ouvert, que la mère portera à ⟦D⟧ avec la version définitive.** Réserve de l'auteur, gardée par la mère telle qu'il l'a écrite : l'auteur a gardé « rien ne part » pour les questions différentes entre jumeaux, faute d'avoir lu la question posée à ⟦D⟧ ; rien de ce qu'il a lu ne dit que [GO85] couvre ce cas. Le texte qui règle ce cas ne change pas (D6 ; ligne d'arrêt jumelle).

**À signaler à ⟦D⟧ au scellement**, sans que ce soient des nœuds. (i) Les trois choix de conception de l'auteur sur les contrôles hors gabarit (D6), que le mot de ⟦D⟧ ne fixe pas : le lanceur du programme de jugement — le monteur de l'oracle ; le lieu du rapport — le fichier sous embargo ; le sens de « à part » — ni dans la métrique 3, ni dans l'accord des lecteurs, ni dans aucun critère de lecture gelé. (ii) La ligne « Auteur » : depuis le brouillon 15, l'auteur est appelé par l'interface, à la demande de la session de l'attaquant informé, quand D8 tient l'auteur de ce texte pour distinct d'elle ; à ⟦D⟧ d'en juger.

## Réserves, et ce que l'auteur n'a pas lu
>>>FIN 17

Motif 18 : point 8 — la section « Contre-lecture » dit l'état des brouillons 17 et 16 ; le chemin et l'empreinte du rapport sont ceux du commentaire de sa copie servie.
<<<ANCIEN 18
**Brouillon 16, non encore vérifié.** Écrit par
===NOUVEAU 18
**Brouillon 17, non encore vérifié.** Écrit par Claude Fable 5.2, appelé par l'interface d'Anthropic, en remplacements exacts appliqués par programme au brouillon 16. Il porte les corrections de la vérification du brouillon 16 : A, limite du repli interne (D6, ligne d'arrêt jumelle, addendum O) ; B, le monteur ne lit pas les sorties du jugement par programme (D6, D8) ; C, entrées des agrégats (déroulement, point 9) ; D, signalements à ⟦D⟧ (« Champs ouverts et nœuds ») ; E, colonne de [GO85] ; point 8, dates ; point 6, mention d'attente du champ n° 19, tranchée par la mère ; deux défauts anciens — « points 8, 18 et 21 » à la ligne d'arrêt de la seconde confirmation, « la même contre-lectrice » au paragraphe d'état. S'y ajoute, à la demande de la mère, le nœud 15, ouvert pour ⟦D⟧.

**Brouillon 16, vérifié : « à corriger »**, un majeur nouveau, le reste acquis ou mineur, par le même contre-lecteur (Opus 5.5), le 22 novembre 2026 (`docs/notes/attaquant-informe-v1/course-brouillon16-v1/verification-corrections-brouillon16-v1.md`, `926fd33f0f74b677f37e89f15c8f85cdeb39007ef6edc9b192ead8fa016b49db`, selon le commentaire de la copie servie). Écrit par
>>>FIN 18

## Table des corrections

| Point | Traitement | Motif | Blocs |
|---|---|---|---|
| 1 : seuil inapplicable sans les contrôles hors gabarit | appliqué | Le cas est écrit dans la puce « Contrôles hors gabarit » de D6, non dans la puce « deux cas », dont le texte sur les jumeaux ne doit pas changer. L'attestation entre à la liste de l'addendum O et à la ligne d'arrêt. | 9, 13, 14 |
| 2 : le monteur ne lit pas les sorties | appliqué | Dit en D6 (i) et dans la colonne « Lit » de D8. | 10, 11 |
| 3 : entrées des agrégats | appliqué | — | 12 |
| 4 : signalements à ⟦D⟧ | appliqué | Un paragraphe « À signaler à ⟦D⟧ au scellement », à la fin de la section. | 17 |
| 5 : colonne de [GO85] | appliqué | Le recalcul est dit « selon son rapport » : je ne l'ai pas refait. | 7 |
| 6 : dates | appliqué | Les heures sont celles de la demande. | 6 |
| 7 : deux défauts anciens | appliqué | Chaque motif le nomme « défaut ancien ». | 2, 15 |
| 8 : en-tête | appliqué autrement | La phrase « Pour les brouillons 15 et 16 » reste telle : je ne sais pas qui a écrit la demande du brouillon 17. La ligne « Auteur » reçoit une phrase propre à ce brouillon. | 1, 3, 4, 5, 18 |
| 9 : champ n° 19 | appliqué | Mention seule ; le marqueur reste. | 8 |
| 10 : réserve sur les jumeaux | appliqué | Inscrite comme nœud 15. La phrase « Aucun nœud de cette liste ne reste ouvert » est accordée, sans quoi le texte se contredirait. | 16, 17 |

## Vu et non corrigé

- **Addendum O.** La condition de lancement 12 et le paragraphe « L'oracle est figé… » de D6 ne nomment pas la nouvelle attestation. La liste de l'addendum O et la ligne d'arrêt la portent.
- **Puce « deux cas » de D6.** Elle annonce deux cas, et la limite du repli en fait un troisième, écrit dans la puce suivante. Je ne l'ai pas touchée, pour ne pas changer le texte sur les jumeaux.
- **Définition du « dommage tenu ».** Elle ne renvoie pas à la limite du repli. Je n'y ai pas touché : c'est une définition gelée.
- **Ligne [PR-3].** Elle dit « l'auteur des brouillons 15 et 16 ne les a pas recalculées ». Cela vaut aussi pour le brouillon 17.
- **« Sa contre-lectrice ».** D8 et une ligne d'arrêt disent « l'auteur de ce texte et sa contre-lectrice ». Depuis le brouillon 15, c'est un contre-lecteur.
- **Contre-lecture 6, M2.** Elle dit toujours « nœud 14 ouvert » : c'est de l'historique, laissé tel.

## Réserves

1. **Ancres.** Elles sont recopiées à vue. Une espace insécable ou une apostrophe courbe que je vois comme ordinaire ferait refuser un bloc. Les blocs 8, 15 et 17 portent sur du texte ancien ; les autres ancres reprennent du texte que j'ai écrit moi-même.
2. **Limite du repli.** Je ne connais ni l'oracle ni sa règle. La phrase « s'il ne peut pas l'attester, c'est ce cas » est mon ajout : elle suit la forme déjà employée pour l'attestation de provenance.
3. **Nœud 15.** Le numéro est mon choix. Le nœud est écrit sans option ni recommandation : je n'ai pas lu la question posée à ⟦D⟧.
4. **Ligne « Auteur ».** Le signalement (ii) dit « depuis le brouillon 15 ». Pour le brouillon 17, je le déduis du dossier où la demande est rangée et ne l'ai pas vérifié.
5. **Empreintes et heures.** Je n'en ai recalculé aucune. L'empreinte du brouillon 16, le chemin et l'empreinte du rapport viennent des commentaires des copies servies. Les heures viennent de la demande.

FIN DE LA RÉPONSE
