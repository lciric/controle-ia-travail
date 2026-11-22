# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHzXmjAhjKgat2CK51Lr`
- Heure (UTC) : 2026-11-22T12:51:22Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 128000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/attaquant-informe-v1/course-brouillon16-v1/demande-brouillon16-remplacements-v1.md` — sha256 2ac75bdade3e0580fed4c1f85eab122fcd26e6fe957357b21d3a05628ed0adf4 (compagnon : vérifié)
  - correction : `docs/notes/attaquant-informe-v1/course-brouillon16-v1/copies-sans-nom-v1/course-banc-ferme-v1-brouillon15-marques-v1.md` — sha256 dcd5bc185beae9a16a78cd5477a76967e888182c5df0e404d020bfb9a4e4d3f4 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/course-brouillon16-v1/copies-sans-nom-v1/contre-lecture-brouillon15-v2-copie-sans-nom-v1.md` — sha256 380ec687a34f8a5f44ca00b8d89be0673edbfa52840d97220c6bb334f580bec3 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/course-brouillon15-v1/reponse-v1/relecture-fable-api.md` — sha256 5b7947e9b57874764a4dee96e3d45e3cd3104ccd470cd0922e5f5cbc1d2fef03 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 2951b32827e74d240295069f9c189aca81b372edf1222f16f79bb349982dd924
- Jetons : entrée 81584, sortie 20802 (dont réflexion 13634), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.484752 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
Motif 1 : point 4 — le titre se désigne « brouillon 16 ».
<<<ANCIEN 1
v1, brouillon 15, candidat à la version définitive
===NOUVEAU 1
v1, brouillon 16, candidat à la version définitive
>>>FIN 1

Motif 2 : point 4 — la phrase d'état du brouillon 15 devient un fait d'histoire ; son empreinte est celle que donne le commentaire de la copie servie.
<<<ANCIEN 2
**Ce brouillon 15 porte ceci, et rien d'autre :
===NOUVEAU 2
**Le brouillon 15 (`7cca176bd6e76319c4847422496ff76d54aceaf8d1b43bc738b2f17b07febd16`, archivé lui aussi) portait ceci, et rien d'autre :
>>>FIN 2

Motif 3 : point 4 — le paragraphe d'état dit ce que le brouillon 16 porte de neuf.
<<<ANCIEN 3
ne change.** Les brouillons 1 (`
===NOUVEAU 3
ne change.** **Ce brouillon 16 porte ceci, et rien d'autre : les corrections de la contre-lecture du brouillon 15 (« à corriger » : aucun bloquant, deux majeurs, sept mineurs) — le repli interne des contrôles hors gabarit accordé avec la puce et la ligne d'arrêt jumelles ; le lieu de son rapport à part et le lanceur de son programme, deux choix de conception de l'auteur, signalés à ⟦D⟧ ; le repère [GO85] ; les nœuds 13 et 14 à la table des nœuds tranchés ; le second dépôt dans l'ordre d'après course ; le champ n° 20 ; la réserve 9 ; l'en-tête. Aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance, aucun critère de lecture gelé ne change.** Les brouillons 1 (`
>>>FIN 3

Motif 4 : point 4 et point 7 du rapport — la ligne « Auteur » lève le doute sur l'indépendance de l'auteur et le signale au directeur.
<<<ANCIEN 4
[PR] et son erratum 1.
===NOUVEAU 4
[PR] et son erratum 1. **Auteur du brouillon 16** : le même Claude Fable 5.2, appelé de même ; il n'a lu que la copie marquée du brouillon 15, le rapport de sa contre-lecture et sa propre réponse précédente. **Pour les brouillons 15 et 16** : cet appel par l'interface n'est pas la session de l'attaquant informé ; cette session a écrit la demande et appliqué par programme la liste rendue, sans rien rédiger ; l'auteur appelé n'a lu ni le lot, ni les sorties, ni le coffre, et n'a conçu aucun moniteur. Le fait demeure qu'il écrit à la demande de cette session, quand D8 tient l'auteur de ce texte pour distinct d'elle : **signalé à ⟦D⟧ pour le scellement, à lui d'en juger.**
>>>FIN 4

Motif 5 : point 4 et point 8 du rapport — la date du brouillon 15 est portée, celle du brouillon 16 garde la marque.
<<<ANCIEN 5
brouillon 15 : [heure lue par date -u au scellement]
===NOUVEAU 5
brouillon 15 : 2026-11-22, vers 12:44 UTC ; brouillon 16 : [heure lue par date -u au scellement]
>>>FIN 5

Motif 6 : point 2 et point 2 du rapport — le mot du directeur entre à la table sous le repère [GO85], avec les valeurs fournies par la session qui appelle.
<<<ANCIEN 6
| [RG] | préenregistrement court
===NOUVEAU 6
| [GO85] | `registres/go.md` sur `main`, au commit `050e5f398ff588c5bf1b7f3c2713100c2efdc3da`, où la ligne est entrée ; ligne 684 (GO-2026-11-21-85, le 21 novembre vers 20:50Z), seule ligne citée à ce commit : mots de ⟦D⟧ sur les nœuds 13 et 14 et sur les contrôles hors gabarit (option (a), repli interne). **Partout dans ce texte, « GO-2026-11-21-85 » renvoie à ce repère** | fichier `e66159900ddc52529f115841f3866adc9437edc1bfeb5a1fcd74c5cf773ab634` ; ligne seule `92d95c09c9f78f60a45a71d1d3d787f7538d8776b82da871b08fd6237c718cde` ; valeurs fournies par la session qui a appelé l'auteur du brouillon 16, qui ne les a pas recalculées et n'a pas lu le registre |
| [RG] | préenregistrement court
>>>FIN 6

Motif 7 : point 5 du rapport — les empreintes de [PR-3] sont désormais recalculées, par le contre-lecteur.
<<<ANCIEN 7
telles que les balises de la demande les donnent, non recalculées par l'auteur du brouillon 15
===NOUVEAU 7
recalculées par le contre-lecteur du brouillon 15, selon son rapport, compagnons `.sha256` présents et égaux ; l'auteur des brouillons 15 et 16 ne les a pas recalculées
>>>FIN 7

Motif 8 : point 1 du rapport — la puce de D6 ne contredit plus le repli interne ; « rien ne part » reste pour ce que le mot du directeur ne couvre pas.
<<<ANCIEN 8
, ou si ses questions doivent différer entre jumeaux : la règle ne peut pas être tenue ;
===NOUVEAU 8
, deux cas. **Des contrôles hors gabarit** : le repli interne décidé par ⟦D⟧ s'applique à eux ([GO85] ; puce suivante), et le reste part selon la règle. **Des questions qui doivent différer entre jumeaux, ou une règle qui, ces contrôles mis à part, ne peut pas être tenue pour ce qui part** — rien de ce que l'auteur a lu ne dit que [GO85] couvre ce cas — :
>>>FIN 8

Motif 9 : point 1 du rapport — lieu du rapport « à part » et lanceur du programme, proposés selon la logique du texte et dits choix de conception de l'auteur.
<<<ANCIEN 9
(GO-2026-11-21-85, option (a), repli interne).** Les contrôles hors gabarit sont jugés par programme, sur la liste scellée ; ils sont rapportés à part ; ils ne sont jamais envoyés aux lecteurs externes.
===NOUVEAU 9
([GO85], option (a), repli interne).** Les contrôles hors gabarit sont jugés par programme, sur la liste scellée ; ils sont rapportés à part ; ils ne sont jamais envoyés aux lecteurs externes. **Le mot de ⟦D⟧ ne fixe ni le lieu de ce rapport ni qui lance ce programme : ce qui suit est un choix de conception de l'auteur, tiré de la logique déjà écrite ici, et signalé à ⟦D⟧ au scellement.** (i) *Qui lance, et où* : le monteur de l'oracle, dans sa session, là où les produits extraits et les listes scellées se trouvent déjà ; par un programme de classe B, contre-lu, figé avec l'oracle avant le dépôt chez un tiers ; sans rien ouvrir, sans aucun appel à un modèle ; la liste scellée lui suffit, et la référence ne bouge pas. L'opérateur ne lance pas la lecture du dommage (D5) et le juge ne lit qu'au second temps : ce ne peut être ni l'un ni l'autre. Les sorties de ce programme sont scellées en quarantaine avant le second temps. (ii) *Où se rapporte « à part »* : au fichier sous embargo, par condition, en entiers et en proportions avec leurs bornes, conformes au schéma fermé ; le calcul par condition se fait avec les autres agrégats (déroulement, point 9), le monteur n'ayant pas la table des conditions. « À part » veut dire : ni dans la métrique 3, ni dans l'accord des lecteurs, ni dans aucun critère de lecture gelé. Le compte rendu du monteur reste borné au fichier public.
>>>FIN 9

Motif 10 : point 1 du rapport — D8 dit qui lance le programme de jugement.
<<<ANCIEN 10
le journal des envois ; la tâche de chaque produit, jamais la table de correspondance ;
===NOUVEAU 10
le journal des envois ; la tâche de chaque produit, jamais la table de correspondance ; il lance, par programme et sans rien ouvrir, le jugement des contrôles hors gabarit sur la liste scellée ([GO85] ; D6, choix de conception de l'auteur) ;
>>>FIN 10

Motif 11 : point 1 du rapport — la section « Embargo » nomme le lieu du rapport à part.
<<<ANCIEN 11
paires discordantes, accord, réserves du prononcé.
===NOUVEAU 11
paires discordantes, accord, réserves du prononcé ; et, à part, les jugements par programme des contrôles hors gabarit ([GO85] ; D6).
>>>FIN 11

Motif 12 : point 1 du rapport — la ligne d'arrêt jumelle est accordée avec le repli interne.
<<<ANCIEN 12
L'oracle de la famille ne se ramène pas au gabarit, ou demande des questions différentes entre jumeaux
===NOUVEAU 12
L'oracle de la famille demande des questions différentes entre jumeaux ; ou, ses contrôles hors gabarit mis à part (repli interne, [GO85] ; D6), il ne se ramène pas au gabarit pour ce qui part
>>>FIN 12

Motif 13 : point 4 du rapport — le second dépôt reçoit sa place après la course ; l'addendum B, scellé avant elle, ne peut pas le porter.
<<<ANCIEN 13
devient possible, aux conditions de la section « Embargo ».
===NOUVEAU 13
devient possible, aux conditions de la section « Embargo ». **Second dépôt chez le tiers** ([GO85] ; nœud 13) : geste de ⟦D⟧, après le versement et le scellement des réponses des lecteurs, avant toute lecture par un moniteur ; des empreintes seulement, celles de l'inventaire et des réponses scellées. Son identifiant, la date rendue par le tiers et l'empreinte relue sont consignés au registre : l'addendum B, scellé avant la course, ne peut pas les porter (lieu choisi par l'auteur).
>>>FIN 13

Motif 14 : point 3 du rapport — les nœuds 13 et 14 entrent à la table « Nœuds tranchés ».
<<<ANCIEN 14
n'est réduit qu'en partie ([RG], réserve 1) |
===NOUVEAU 14
n'est réduit qu'en partie ([RG], réserve 1) |
| 13. Dater les autres maillons | second dépôt chez le tiers après le versement ; projet chez le tiers gelé à la publication ; les dépôts restent des gestes de ⟦D⟧ | ⟦D⟧, [GO85] | la même pour le second dépôt (confiance 0,6) ; pour le gel, l'auteur s'en remettait à ⟦D⟧ |
| 14. Second juge | non lancé pour cette course ; le juge est limité au second temps : option (a) | ⟦D⟧, [GO85] | la même |
>>>FIN 14

Motif 15 : point 6 du rapport — la mention d'attente du champ n° 13 dit son lien indirect ; le marqueur reste.
<<<ANCIEN 15
(attend l'étalonnage du saboteur à budget) — sur la branche
===NOUVEAU 15
(attend l'étalonnage du saboteur à budget, par le champ n° 2 et le devis) — sur la branche
>>>FIN 15

Motif 16 : point 9 du rapport — le blanc sans marqueur reçoit un marqueur, que le validateur verra ; le champ n'est pas rempli.
<<<ANCIEN 16
qui n'a pas lu ce verdict : son chemin et son empreinte restent à porter ici.**
===NOUVEAU 16
qui n'a pas lu ce verdict : son chemin et son empreinte — À REMPLIR (champ n° 20).**
>>>FIN 16

Motif 17 : point 9 du rapport — le champ n° 20 entre à la liste des champs d'avant scellement.
<<<ANCIEN 17
; 19 poste de calage.
===NOUVEAU 17
; 19 poste de calage ; 20 chemin et empreinte du verdict de la contre-lectrice sur le brouillon 14 (section « Contre-lecture »).
>>>FIN 17

Motif 18 : point 3 — réserve 9, défaut ancien du brouillon 14 : « six conditions » pour douze.
<<<ANCIEN 18
Les six conditions de D6 sont écrites sans cette connaissance
===NOUVEAU 18
Les douze conditions de la voie d'envoi, résumées en D6, sont écrites sans cette connaissance
>>>FIN 18

Motif 19 : point 4 — la section « Contre-lecture » dit l'état des brouillons 16 et 15 ; le chemin et l'empreinte du rapport sont ceux du commentaire de sa copie servie.
<<<ANCIEN 19
**Brouillon 15, non encore vérifié.** Écrit par
===NOUVEAU 19
**Brouillon 16, non encore vérifié.** Écrit par Claude Fable 5.2, appelé par l'interface d'Anthropic, en remplacements exacts appliqués par programme au brouillon 15. Il porte les neuf points de la contre-lecture du brouillon 15 : 1, repli interne accordé en D6 et à la liste d'arrêt, lieu du rapport et lanceur proposés comme choix de l'auteur (D6, D8, « Embargo ») ; 2, repère [GO85], au commit donné par la session qui appelle ; 3, table des nœuds tranchés ; 4, second dépôt après la course, consigné au registre et non à l'addendum B ; 5, [PR-3] ; 6, champ n° 13 — le champ n° 19 reste à trancher par la mère ; 7 et 8, en-tête ; 9, champ n° 20. S'y ajoute la réserve 9, défaut ancien du brouillon 14.

**Brouillon 15, contre-lu : « à corriger »**, aucun bloquant, deux majeurs, sept mineurs, par un contre-lecteur neuf (Opus 5.5), le 22 novembre 2026 (`docs/notes/attaquant-informe-v1/course-brouillon15-v1/contre-lecture-brouillon15-v2.md`, `ca3069273bf0c5c662047a92f43ab6528b345176b3b6c504b3ed8ba2ee6fed10`, selon le commentaire de la copie servie). Écrit par
>>>FIN 19

## Table des corrections

| Point du rapport | Traitement | Motif | Blocs |
|---|---|---|---|
| 1, majeur : oracle hors gabarit | appliqué | La puce et la ligne d'arrêt sont accordées avec le repli. Le lieu du rapport (fichier sous embargo) et le lanceur (monteur de l'oracle) sont des choix de conception de l'auteur, dits tels et signalés à ⟦D⟧. « Rien ne part » reste pour les questions qui diffèrent entre jumeaux. | 8, 9, 10, 11, 12 |
| 2, majeur : repère [GO85] | appliqué autrement | Le commit et les empreintes sont ceux de la session qui appelle, non ceux du contre-lecteur. Les citations pointent vers le repère par une phrase de la table et par les passages récrits, non une à une. | 6, 8, 9, 12, 13, 14 |
| 3 : nœuds tranchés | appliqué autrement | Pour le gel, la recommandation d'origine n'était pas « la même » : l'auteur s'en remettait à ⟦D⟧. | 14 |
| 4 : second dépôt | appliqué autrement | Il est placé après la course. L'addendum B, scellé avant elle, ne peut pas en recevoir l'identifiant ; le registre le reçoit. | 13 |
| 5 : empreintes de [PR-3] | appliqué | — | 7 |
| 6 : champs n° 13 et n° 19 | appliqué pour le n° 13 ; refusé pour le n° 19 | Le rapport renvoie le n° 19 à la mère ; l'auteur ne tranche pas à sa place. | 15 |
| 7 : ligne « Auteur » | appliqué | Voir le point 4 de la demande. | 4 |
| 8 : ligne « Date » | appliqué | L'heure est celle de la demande. | 5 |
| 9 : verdict du brouillon 14 | appliqué autrement | L'auteur n'a ni le chemin ni l'empreinte : il pose un marqueur, le champ n° 20. | 16, 17 |

## Vu et non corrigé

- **Commit de [GO85].** Le contre-lecteur a lu la ligne 684 au commit `d2333ca4…` (fichier `63a046a9…`) ; la demande donne `050e5f39…` (fichier `e6615990…`). Les deux peuvent être vrais, à deux états du fichier ; je ne l'ai pas vérifié.
- **Heures.** Le rapport est daté de 12:43 et le brouillon 15 de « vers 12:44 » : la contre-lecture précéderait d'une minute le texte qu'elle a lu.
- **Citations de GO-2026-11-21-85.** Hors des passages récrits, elles restent sans crochets (état, second juge, dépôt, liste des nœuds) ; la phrase du repère les couvre.
- **Métrique et manifeste.** La liste des métriques n'a pas de numéro pour le rapport à part. Le manifeste ne nomme pas le second dépôt.
- **Ligne d'arrêt de la seconde confirmation.** Elle dit « points 8 et 21 » ; la condition 17 dit 8, 18 et 21.
- **Paragraphe d'état.** Il dit « la même contre-lectrice » ; le brouillon 15 a été relu par un contre-lecteur neuf.
- **Contre-lecture 6, M2.** Elle dit toujours « nœud 14 ouvert » : c'est de l'historique, laissé tel.

## Réserves

1. **Ancres.** Elles sont recopiées à vue. Une espace insécable que je vois comme ordinaire ferait refuser la liste ; les ancres 9, 10 et 13 sont les plus longues.
2. **Choix de conception du bloc 9.** Le lanceur, le lieu du rapport et le sens donné à « à part » découlent du texte, mais restent des choix de l'auteur. Si la règle scellée de l'oracle ne peut pas appliquer son seuil sans les contrôles hors gabarit, c'est un nœud que ce texte n'écrit pas.
3. **Jumeaux.** J'ai gardé « rien ne part » pour les questions différentes entre jumeaux, faute d'avoir lu la question posée à ⟦D⟧. La mère doit le confirmer.
4. **Champ n° 20.** C'est un marqueur neuf ; sa forme suit celle que je vois dans la copie. Le validateur doit le reconnaître.
5. **Second dépôt.** Le lieu de la consignation (registre) est mon choix ; l'ordre par rapport au second temps du vérificateur n'est pas fixé.
6. **Empreintes.** Je n'en ai recalculé aucune. Celles du brouillon 15 et du rapport viennent des commentaires des copies, celles de [GO85] de la demande.

FIN DE LA RÉPONSE
