# Contre-lecture de code (classe B) — module des lots du bras A, version 5

**Verdict : à corriger** (un défaut majeur de garde, aucun bloquant ; toutes les règles portées sont conformes à la lettre du texte).

- Objet lu : `src/controle_ia/organismes_discrets/lots_bras_a_v5.py` (`75ce3176376612560f27175c428cbc963c6a6dd5d00ed15fc423e2fb034aca95`, 1070 lignes ; compagnon vérifié), `tests/test_lots_bras_a_v5.py` (compagnon vérifié), note `code-lots-bras-a-v5-note.md` (compagnon vérifié), contre `prereg/T0.7-organismes-discrets-v-a-v2-brouillon54.md` (`59ad88f9…`, mêmes numéros de lignes que le 53 ; l'en-tête du module et la note citent le 53, `8ee69fe6…`, exact).
- Lecteur neuf, rien d'écrit hors de ce fichier ; aucune pièce cloisonnée ouverte ; aucun réseau.
- Rejeu : `pytest tests/test_lots_bras_a_v4.py tests/test_lots_bras_a_v5.py tests/test_graines_bras_a_v4.py` : 237 réussis, comme annoncé. Garde statique du cloisonnement : une violation rendue, dans `scripts/chef_essais_admission_bras_a_v2.py` ligne 508, étrangère à la v5 (aucune violation sur `lots_bras_a_v5`, comme dit la note ; à signaler seulement parce que la phrase de la note « [] » est un filtrage, non la sortie brute).
- Sondes propres (hors essais du dépôt), écrites au bloc-notes : espion sur tous les appels du générateur à 127, 128, 129, 64, 63, 32, 31 actions ; donneuse absente (trois cas) ; relevé ; lot décisif ; ancre des jumeaux et voie de service e′ ; relevé forgé.

## Règles contrôlées (conformes)

| règle | ligne | constat |
|---|---|---|
| Égalité exacte sans appel du générateur | 714, 719, 806, 846 ; garde 1174 | `_prendre` (l. 191) : à 128 : aucun `choice` sur « contrôles d'une autre tâche » (seuls les `integers` des donneuses), aucun sur « texte sans rapport » à 64 ni sur les génériques à 64 (seule la permutation des textes) ; à 129 : `choice` ; lot décisif à 160 : `choice` seulement sur la classe plus longue. Les tirages suivants partent de l'état du générateur tel qu'il est. Plans mécaniques « quatre ou moins » : sans tirage (l. 650). Ancres, sentinelles, plans relus : non touchés, comme le texte. |
| Planchers 64 et 32 ; compte jugé = min(écrit, jugeables) | 806, 808 | 64 : construit ; 63 : constat « contrôles d'une autre tâche », lot reste construit ; texte sans rapport 32 construit, 31 constat ; génériques 32 à 63 à parts égales, 31 constat. |
| 12 plans utilisables | 819 ; garde 1174 | compte sur les plans tirés à artefact et à seconde grandeur, avant tout envoi ; sous 12 : aucun artefact du plan tronqué dans le lot, constat, trois autres épreuves construites ; plan sans artefact ou valeur non booléenne : refusé. |
| Constat unique de couverture, deux comptes | 822 | gardes de compte (64) d'abord (`_etat_de_la_couverture`), puis un seul constat objet « couverture », deux comptes et deux planchers de 32, `sous_le_plancher` dit lequel. |
| Ancre des jumeaux non jouée | 812 | `ancre_jumeaux` rend le constat de la première partie, quel que soit le compte des jumeaux ; aucun constat propre ; e′ rend `[]` et refuse tout autre objet à côté. |
| Action donneuse absente : arrêt avant les planchers | 714, 797 ; garde 1175 | vérifié à 0 action, une tâche à 8 actions, une seule action : `ArretSansDonneuse` portant un `ConstatDArret`, jamais un `Constat` d'effectif ; garde jouée avant tout plancher ; la couverture exige le témoin. |
| Épisodes sans plan au lot décisif | 848 ; garde 1174 | hors des lectures de la couverture, comptés par condition ; plans et épisodes sans plan disjoints et faisant 896, sinon arrêt ; entrée refusée si la couverture n'est pas lue. |
| Relevé des actions relues, A18 | 762, 846, 1011 ; garde 1184 | 80 et 79 par classe ; fichier unique par épreuve (registre `releves-des-actions-relues`, second fichier différent refusé) ; lot décisif refusé après un constat ; comptes du lot égaux à ceux du relevé sinon arrêt. L'arrêt de la course est bien laissé au lanceur. |
| R5 | — | chaque garde nouvelle a son essai sain et son essai artefact (52 essais). |
| R9 | — | tous les générateurs viennent de `g.generateur_de(g.cle(...))` ou `g.cle_sentinelles` ; aucun `random`, `default_rng`, `SeedSequence` direct dans le module. |
| Rien d'autre que l'annoncé | — | diff v4 à v5 relu : changements dans `_prendre`, planchers, garde donneuse, constats, couverture, `lot_decisif`, relevé, manifeste, voie e′ ; `lot_mecanique_couverture` gagne `seconde_grandeur` ; `_classe_relue` retiré, remplacé par `_prendre`. Rien d'étranger. |

## Défauts

### Majeur

**M-1 — le relevé des actions relues se laisse forger sous 80 et le lot décisif le prend (l. 770-786, 842-843 ; garde 1184).**
`Releve.__post_init__` ne vérifie que « compte >= plancher » pour les planchers **que l'appelant écrit lui-même** ; il n'exige pas que les planchers soient ceux de 80. `lot_decisif` ne rejuge pas le plancher : il compare seulement le relevé aux comptes des lots. Sonde : lots à 70 honnêtes et 10 déplacées à effet ; `releve_des_actions_relues` rend bien un `Constat` ; mais `Releve("ouverte", {honnetes: 70, deplacees-a-effet: 10}, {honnetes: 0, deplacees-a-effet: 0})` est accepté et `lot_decisif` construit un lot à `relues-par-classe` = 10. C'est exactement « lot décisif demandé avec un compte sous 80 : refusé » (1184) qui n'est pas tenu contre un relevé mal fait, et aucun essai de la v5 ne couvre cet artefact.
Correction : dans `Releve.__post_init__`, exiger `dict(self.planchers) == {"honnetes": PLANCHER_RELUES, "deplacees-a-effet": PLANCHER_RELUES}` ; et dans `lot_decisif`, refuser `n < PLANCHER_RELUES` (ceinture et bretelles, `n` étant déjà calculé l. 889). Ajouter l'essai artefact.

### Mineurs

- **m-1 — `DonneusesTenues` falsifiable (l. 372-380, 710).** Le témoin est une dataclass publique, constructible sans passer par `garde_de_l_action_donneuse` ; la couverture ne vérifie que l'entropie et « ouverte ». Un témoin construit à la main contourne la garde 1175 sur la couverture. Correction : constructeur interne (jeton privé vérifié dans `__post_init__`), ou comparer `comptes_par_tache` au lot honnête de l'appariement fourni. Sans effet si le lanceur n'en fabrique pas ; à signaler.
- **m-2 — `Constat` d'effectif forgeable (l. 232-252).** Même nature : planchers libres. N'existe pas hors de ce module en pratique ; une table de planchers par objet (`PLANCHERS_PAR_OBJET`) fermerait le cas, y compris celui de M-1 pour `actions-d-epreuve-relues`.
- **m-3 — `ancre_jumeaux` rend le constat de la première partie lui-même (l. 570-572).** Conforme à 812 (« celui de l'ancre sur plans honnêtes en tenant lieu »), mais un lanceur qui inscrit les deux retours (ancre 1 puis ancre 2) l'inscrit deux fois : sans conséquence (inscription idempotente), à écrire en clair dans la note pour éviter un double comptage au rapport.
- **m-4 — en-tête du module et note citent le brouillon 53, la lecture demandée est le 54.** Sans effet (identiques hors 13.1, lignes 1 et 3) ; à actualiser à la prochaine version, ou à dire dans la note.
- **m-5 — la note donne « [] » pour la garde statique.** La sortie brute rend une violation hors v5 (voir plus haut) ; écrire « aucune violation sur `lots_bras_a_v5` ; une violation étrangère : `chef_essais_admission_bras_a_v2.py` l. 508 ».

## Pour la suite
Corriger M-1 (nouveau nom, R12 : `lots_bras_a_v6.py`, ou, si la v5 n'est pas encore scellée, correction avant scellement), rejouer les 237 essais, puis lever le verdict à « conforme ».
