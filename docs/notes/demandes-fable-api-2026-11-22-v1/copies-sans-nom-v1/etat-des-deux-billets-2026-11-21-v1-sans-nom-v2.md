# État des deux billets — 21 novembre 2026 — v1

Pièce de classe C (travail), sans contre-lecture. Écrite par un lecteur neuf (Claude Opus 5.5, sous-agent lancé par la session mère `[identifiant de session retiré]`), le 2026-11-21 vers 17:52Z (`date -u`). Elle répond à la question de le directeur : « on en est où pour les deux billets ? on pourra en publier un demain ? il manque quoi exactement à chacun ? ».

Établie sur les registres et les pièces citées en section 8, au commit `ece586d29` de ce dépôt et au commit `b336f48` de la branche `claude/stoic-mayer-51otyy` du dépôt « Raisons ou regard ? » (clone local `/home/user/raisons-ou-regard-travail`). **Non lus, par cloisonnement** : le corps des brouillons du billet sur les sondes, sa fiche de faits, les verdicts et résultats de P3, P3-bis, de l'étape B et de l'étape B bis, et tout ce que la consigne de ce lecteur interdit. Cette note ne porte donc aucun chiffre de résultat du programme.

## Verdict

- **Aucun des deux billets n'est prêt à publier tel quel. Le seul qui peut sortir demain, le dimanche 22 novembre, est celui de l'autre projet, « Reasons or watching? ».** Il faut pour cela que le directeur choisisse ce soir sa version (la v6 telle quelle ou une v7 prudente), la réécrive lui-même, rende public le paquet rejouable sur Open Science Framework, et que le site accepte un premier billet. La relecture de ce premier billet par la modération a une durée qui n'est chiffrée nulle part.
- **Le billet sur les sondes ne sort pas demain.** le directeur l'a lui-même renvoyé « après un vrai résultat sur un saboteur discret, donc après l'entretien » (GO-2026-11-18-66), et l'entretien est maintenant le 1er décembre. Même si le directeur levait ce renvoi, ses sections sur l'étape B et l'étape B bis sont vides, le gabarit n'est pas appliqué et le directeur n'a pas réécrit le texte : au mieux deux ou trois jours.

## 1. Les deux billets

| | Billet sur les sondes (programme de contrôle) | Billet « Reasons or watching? » (autre projet de le directeur) |
|---|---|---|
| Sujet | Sondes linéaires lues sur un saboteur instruit : P3 (le test boîte blanche), P3-bis (le test boîte blanche bis), étape B et étape B bis de l'épreuve des sondes (T0.7) ; puis, par le mot de le directeur du 18 novembre, **les sondes face aux saboteurs discrets** (R-3503 : « je veux les sondes sur saboteurs discrets dans le billet ») | Note d'étape A1–A2 du projet « Raisons ou regard ? » : sur les adaptateurs publiés de Model Spec Midtraining, une phrase de cadrage change ce que le modèle dit, pas ce qu'il fait |
| Titre de travail | « Linear probes on an instructed saboteur » (note des lentilles, `place-lentilles-billet-v1.md`) ; le titre du brouillon n'a pas été lu ici | « Reasons or watching? On Model Spec Midtraining adapters, a framing sentence moves what models say, not what they do » (v6) |
| Défini comme l'un des « deux billets » | R-3125 (18 novembre, 02:13Z) | R-3125 ; R-2647 (« le billet LessWrong de la semaine est celui de l'autre projet ») |
| Auteur du texte | Parties P3 et P3-bis : un rédacteur neuf (modèle A) de l'ancienne mère, R-2732, ligne 106 de la liste « qui a lu quoi » v13 ; lecture adverse par un modèle C, ligne 107. Règle : billet écrit par la session en blocs déclarés, puis reformulé par le directeur (GO-2026-11-18-50) ; sections de résultats par un lecteur autorisé | La session de travail de ce projet (dernière passation : `[identifiant de session retiré]` ; relancée par la mère comme fille `[identifiant de session retiré]`, R-4583). le directeur réécrit avec ses mots et poste lui-même (décision 168 de ce projet) |
| Où | Branche `main` : `docs/notes/billet-nul-avec-controle-positif-v1/` ; pièces des lentilles sur `claude/brave-galileo-jhp684` (et branches sœurs) ; gabarit sous `docs/notes/billets-v1/` | Dépôt `[compte]/raisons-ou-regard-travail`, branche `claude/stoic-mayer-51otyy`, dossier `claude/note_etape_2026-11-13/` |
| Dernière version | Première version anglaise v2, 14 novembre (R-2732), 999 mots, sections étape B et étape B bis laissées vides | v6, 15 novembre (décision 203) ; vérificateur des nombres `verifier_billet_v6.py` |

## 2. Billet sur les sondes : état, pièce par pièce

| Pièce | État | Appui |
|---|---|---|
| Étude des billets publiés (corpus, grille des gestes, double codage, analyse) | **faite** : grille gelée, deux codeurs, arbitrage, analyse de la moitié tenue à l'écart | R-3364 à R-3483 |
| Gabarit de rédaction | **v2 rendue et vérifiée « bon pour le billet »** : sept consignes (dont résumé dans les 250 premiers mots, choix justifié contre une option écartée, dispositif nommé, explication concurrente contrôlée, appel à poursuivre, lien vers le code) et deux objections à prévenir (explication concurrente, antériorité). Il ne dit pas qu'un geste fait le succès | `gabarit-billets-v2.md`, `verification-gabarit-v2-v1.md` ; R-3501 |
| Parties P3 et P3-bis | **rédigées** (anglais v2), lecture adverse « prêt après corrections » (13 constats, 10 appliqués, 2 en partie, 1 laissé à le directeur) ; 28 citations relues sur PDF par programme ; onze questions tranchées par « go recos » (R-2739) | R-2732, R-2739 |
| Section étape B | **vide**. Le verdict est scellé (17 novembre, ligne `VERDICT-T07-ETAPE-B`) : il entre au billet selon la règle de le directeur (scellé avant le dimanche 22) | R-2739 (1), R-3125 |
| Section étape B bis | **vide**. Le verdict est scellé (19 novembre vers 01:01Z) et accepté par le directeur (option A) : il entre au billet selon la même règle | R-2716 (2), état du 19 novembre 12:30Z |
| Application du gabarit au texte | **non faite** : la v2 du billet date du 14 novembre, avant le gabarit (18 novembre) | — |
| Lentilles, pièce 1 (paragraphe de méthode) | **brouillon** avec registre des affirmations, sur une branche, pas sur `main` | commit `36466f6a` ; GO-2026-11-19-33 |
| Lentilles, pièce 2 (lecture des sondes de l'étape B bis par la lentille publique) | texte de lecture v2 **scellé** (20 novembre), ligne du code inscrite (21 novembre 16:02Z), accord donné (GO-2026-11-21-65) ; **l'opérateur s'est arrêté sur un défaut du code** (pagination de l'arbre du jeu de données), correction renvoyée à la session des lentilles | R-4597, R-4617 |
| Lentilles, pièce 3 (nos lentilles réajustées) | aucune ligne de calcul ; texte neuf exigé ; recommandée « après le billet » | GO-2026-11-19-33, note des lentilles |
| Résultat de sondes sur un saboteur discret | **n'existe pas encore.** Saboteur à budget : ligne de calcul neuve accordée (GO-2026-11-21-70), la course attend le code contre-lu, les consignes et l'ordre scellés, dernière création au 27 novembre. Organismes discrets (bras A) : devis des essais d'admission accepté, relance en cours. « Sabotage ou empreinte » (barreau 5) : formation en cours | GO-2026-11-21-66, -68, -70 ; R-4587 |
| Rédaction par la session « en turbo » | GO-2026-11-21-63 et R-4595 disent « billets » lancés ; **aucune pièce de billet n'est versée** dans le dépôt depuis le 19 novembre 10:06Z (relevé par l'historique de toutes les branches) | — |

## 3. Ce qui manque au billet sur les sondes

| Ce qui manque | Qui | Durée estimée | Dépend de | Bloquant pour demain |
|---|---|---|---|---|
| Lever ou garder le renvoi « après un vrai résultat sur un saboteur discret » (GO-2026-11-18-66), c'est-à-dire décider si une version « saboteur instruit » sort d'abord | le directeur | une minute | — | oui |
| Un résultat de sondes sur un saboteur discret, si le renvoi tient | sessions du saboteur à budget, du bras A, du barreau 5 | des jours (pas avant le 27 au plus tôt pour le saboteur à budget) | courses, verdicts scellés par des lecteurs neufs (R13) | oui |
| Sections étape B et étape B bis, écrites d'après les seuls verdicts scellés | un lecteur autorisé, désigné par la mère et inscrit à la liste « qui a lu quoi » (la mère est exposée, R-3501) | 2 à 4 h | verdicts scellés (faits) | oui |
| Texte entier refait selon le gabarit v2, environ 1 300 mots, réserves dans le corps (R-2739, point 10), en blocs déclarés | rédacteur (session) | 2 à 3 h | sections ci-dessus | oui |
| Lecture adverse du texte entier par un autre modèle ; chaque nombre retrouvé dans un verdict par programme ; chaque chiffre de travaux voisins vérifié sur PDF empreinté, page citée (R7) ; registre des affirmations (R6) | lecteur neuf ; programme | 1 à 2 h | texte entier | oui |
| Page publique de P3 mise à jour avec les réserves avant tout lien (R-2739, point 4) ; publication du verdict et du fichier d'issue de P3-bis, et de son texte scellé seulement s'il ne porte aucune consigne de sabotage en toutes lettres (point 5) | session, puis poussée sur mot exprès de le directeur | 1 à 2 h | régénération de la copie expurgée | oui si le billet donne des liens |
| Réécriture par le directeur avec ses propres mots | le directeur | quelques heures | texte final | oui (règle du site pour un premier billet) |
| Compte du site et relecture du premier billet par la modération | le directeur ; le site | non chiffrée | — | oui |
| Lentilles, pièce 1 versée sur `main` et relue | session des lentilles | moins d'une heure | — | non |
| Lentilles, pièce 2 | session des lentilles, opérateur, lecteur neuf | code corrigé, puis 1 à 2 h de calcul (pire 6 h), puis lecture | correction du code | non (facultative) |

## 4. Billet « Reasons or watching? » : état

- **v6 écrite** (15 novembre), avec un vérificateur des nombres par programme ; table des affirmations ; paquet rejouable (table sans texte, script de recalcul, sortie attendue) déposé sur Open Science Framework, projet `ewx4p`, **privé** au dernier relevé versé (`paquet_public_osf_etat.json`) ; embargos du plan (`s4wz8`) et du préenregistrement de A3 (`7xv2u`) levés par le directeur le 13 novembre.
- **Ordre fixé par le directeur** (décisions 168 et 183 de ce projet) : publier sans attendre la suite ; la session écrit le texte complet ; le directeur le réécrit avec ses mots ; la session repasse chaque nombre de la version de le directeur au vérificateur ; le directeur rend public le projet `ewx4p` d'un clic, la session vérifie le lien sans compte ; le directeur poste, puis demande la promotion sur le forum d'alignement.
- **Ce qui a changé depuis la v6** : la fin de l'expérience 1 est lue, sous un verdict scellé « non lisible (jumelles non reconnues) » ; la conception 2 bis (agents de référence) doit fournir l'instrument qui établit la légitimité des jumelles ; ses lots ne sont pas partis (solde de la clé jamais lu, vérification du code interrompue par la limite de Fable sur l'ancien compte, jusqu'au 27 novembre 15:00Z).
- **Question ouverte à le directeur, non tranchée** (passation du 21 novembre, section 4) : attendre la conception 2 bis, ou publier une v7 prudente.

## 5. Ce qui manque au billet « Reasons or watching? »

| Ce qui manque | Qui | Durée estimée | Dépend de | Bloquant pour demain |
|---|---|---|---|---|
| Choix : v6 telle quelle, v7 prudente (une phrase sur la fin de l'expérience 1 et son verdict), ou attendre la conception 2 bis | le directeur | une minute | — | oui |
| Si v7 : rédaction, vérificateur adapté, revue adverse des nombres ; contrôle que rien de la v6 n'est contredit par un résultat scellé depuis le 15 novembre (ce contrôle n'a pas été fait ici) | session « Raisons ou regard ? » (fille relancée) | 2 à 4 h | modèle disponible sur le nouveau compte | oui |
| Réécriture par le directeur avec ses mots, puis nombres repassés au vérificateur | le directeur, puis la session | quelques heures | version choisie | oui |
| Projet `ewx4p` rendu public, lien vérifié sans compte | le directeur, puis la session | quelques minutes | — | oui (le billet renvoie au paquet) |
| Compte du site et relecture du premier billet par la modération | le directeur ; le site | non chiffrée | — | oui |
| Gabarit de l'étude des billets appliqué au texte | session | 1 à 2 h | — | non (la v6 lui est antérieure ; c'est une amélioration) |

## 6. Publiable demain, le 22 novembre ?

- **« Reasons or watching? » : oui, possible, à cinq conditions** : (1) le directeur choisit ce soir la v6 ou une v7 courte ; (2) la session confirme que le texte retenu n'est contredit par aucun résultat scellé depuis le 15 novembre et repasse les nombres ; (3) le directeur le réécrit lui-même demain ; (4) le directeur rend public `ewx4p` ; (5) le directeur a un compte sur le site. Même alors, la mise en ligne effective attend la relecture d'un premier billet, de durée inconnue. Attendre la conception 2 bis rend toute date de demain impossible.
- **Billet sur les sondes : non.** Par le renvoi de le directeur lui-même (GO-2026-11-18-66) tant qu'il tient ; et, même levé, par les sections vides, le gabarit non appliqué, la lecture adverse du texte entier et la réécriture par le directeur.

## 7. Règles de publication qui s'appliquent

1. **le directeur seul publie.** Toute publication, soumission ou ouverture de dépôt public est un nœud (brief v2, sections « Soumission et publication » et interdits ; `CLAUDE.md`). Hors de toute autonomie, il faut son GO exprès au moment de publier (GO-2026-11-18-43, -61 ; GO-2026-11-21-69 : « contact, publication, paiement restent à le directeur »). Dans l'autre projet, la mise en ligne est « son acte » (décisions 164 et 168).
2. **Règle du site** (`resume-politique-v1.md`) : tout texte écrit ou fortement révisé par un modèle va dans des blocs déclarés ; un billet fait surtout de blocs a peu de chances d'être accepté ; pour un compte neuf, la politique est « closer to a zero-LLM policy » ; l'auteur principal est un compte humain qui se porte garant de tout. D'où GO-2026-11-18-50 : la session écrit en blocs déclarés, le directeur reformule avec ses mots. Au 13 novembre, le directeur n'avait aucun compte sur le site (R-2577) ; il crée le sien, la mère n'en crée pas (R-2593).
3. **Copie expurgée publique.** `[compte]/controle-ia` n'est que la copie expurgée, régénérée par `scripts/depot_expurge.py` (dernière version : `depot_expurge_v11.py`) ; ce dépôt de travail n'y est jamais poussé (`CLAUDE.md`, « Dépôt distant ») ; pousser la copie est un geste de publication, à un GO exprès. Les PDF sous droit d'éditeur en sont exclus (R-4544, R-4554).
4. **Engagement daté.** Le texte v2 de l'engagement daté sous embargo est « figeable une fois les marqueurs remplis » (date de fin d'embargo, auteurs), rien n'est soumis (R-2635, R-2636). Il date du 14 novembre : avant tout dépôt, il est à confronter aux décisions de revendication postérieures (N-071 à N-077). Son dépôt est un geste de le directeur.
5. **Embargo et cloisonnement.** Rien du mode tenu à l'écart ni des mécanismes des saboteurs dans un texte public (N-054, R-3503) ; aucune consigne de sabotage en toutes lettres (R-2739, point 5) ; les procédés de la course « nouvelles attaques » restent en quarantaine, avec une revue externe avant toute sortie, billet compris (GO-2026-11-20-50, point 6) ; les sections de résultats sont écrites par un lecteur autorisé, la mère exposée ne fixe rien.
6. **R7** : aucun chiffre de l'état de l'art sans vérification sur PDF empreinté, page citée. **R6** : tout chiffre renvoie à un chemin et une empreinte (registre des affirmations du billet).
7. **R13** : un verdict cité est un verdict scellé, prononcé par un sous-agent neuf qui applique les critères gelés, et soumis à le directeur. C'est le cas de l'étape B bis, accepté par le directeur.
8. **R4** : un résultat trop propre reçoit une réserve dans le corps. La lecture adverse du 13 novembre interdit aussi les phrases de feuille de route et les mots de primauté (R-2595).
9. **Témoin de l'attaque publiée (Bailey)** : recommandé hors du billet, au plus une phrase sans chiffre dans « comment ce travail a été fait » (R-3125, confiance 0,8). Aucun mot de le directeur sur ce point n'a été retrouvé ici.
10. **Autre projet** : aucun texte généré par un modèle cité dans le billet (décision 164) ; aucun texte généré versé dans git ; chaque chiffre recalculé depuis les sorties commitées.

## 8. Incertitudes

- Le compte de le directeur sur le site : inexistant au 13 novembre ; rien de plus récent n'a été trouvé.
- L'état public du projet `ewx4p` aujourd'hui : non relevé (dernier état versé : privé).
- GO-2026-11-21-63 (« turbo max pour boucler les billets ») et R-4587 (« on en a besoin pour les billets ») laissent penser que le directeur veut aller vite ; le renvoi de GO-2026-11-18-66 n'est pas levé au registre. Lecture à confirmer par le directeur.
- Ce que couvre « billets » dans R-4595 : aucune pièce versée ; une session ou un agent peut écrire hors du dépôt.
- La page publique de P3 : sa mise à jour avec les réserves n'a pas été retrouvée au registre.
- La durée de la relecture d'un premier billet par la modération : non chiffrée dans les pièces lues.
- L'entretien : GO-2026-11-18-66 nomme le 27 novembre ; `CLAUDE.md` et `registres/rappels.md` disent le 1er décembre. Cette note suit le 1er décembre.
- Les durées de la section 3 et de la section 5 sont des estimations de ce lecteur, pas des devis.

## 9. Sources (chemins et empreintes)

| Pièce | Empreinte |
|---|---|
| `registres/etat.md` | `31c47d74312b011bfbaad441dfb051ae78fb624464099008e9e18dbc610262d4` |
| `registres/decisions.md` (R-2577, R-2593, R-2595, R-2600, R-2635, R-2636, R-2647, R-2714 à R-2716, R-2732, R-2739, R-3125, R-3501, R-3503, R-3507, R-4544, R-4554, R-4583, R-4587, R-4595, R-4597, R-4617) | `c0fb7ed7c2dba8f406c04283e168f09f1eb923300c31fa6e0205ffd247ccf0bb` |
| `registres/go.md` (GO-2026-11-18-43, -50, -61, -66 ; GO-2026-11-19-27, -28, -33 ; GO-2026-11-20-50 ; GO-2026-11-21-63 à -70) | `bfedf0195c24b80de5e3a4bf1881850711afc4a9fc067b528c36e5ae0621af47` |
| `registres/passations/2026-11-21-1450.md` | `b1fcdc7d7bc9633b0f3c6850f7885344fbd142267df0ea02d42425a391cb0148` |
| `registres/passations/2026-11-21-0745.md` | `94e36fe04aac21b29b49f83130e400297c2895a500462fbc95cdc8f1210c700a` |
| `registres/qui-a-lu-quoi-v13.md` (lignes 106 et 107) | `ffc4420e378c5e0931757d4da1c6bdae96e1257527221262539d0cd42d000595` |
| `docs/notes/billets-v1/gabarit-billets-v2.md` | `5eee79b3cf051fbecc5a278bfbf6e54f2a6d9164326ec2512b88e3390b46a2a5` |
| `docs/notes/billets-v1/verification-gabarit-v2-v1.md` (empreinte seule) | `7a303aca9c4c280b091e5cd38eef5c0db7c71d377181868ed8a5994fd361f367` |
| `docs/notes/billet-nul-avec-controle-positif-v1/billet-premiere-version-en-v2.md` (empreinte seule, non ouvert) | `b69fd6dcbd98db174f910bbed6076ec8cf4cb008b61db5414c16581a395c51f2` |
| `docs/notes/billet-nul-avec-controle-positif-v1/fiche-de-faits-v2.md` (empreinte seule, non ouvert) | `1be265b49da140e1ce1ae69a45d46bb395550f0d3a3eeb128fd5ab6556f92942` |
| `docs/notes/billet-nul-avec-controle-positif-v1/lecture-adverse-modele-c-v1.md` (empreinte seule, non ouvert) | `e111761208faa3d0db805392c3aac6c0f3220dd39fb770590993fe4a453dc479` |
| `docs/notes/neuron-lens-v1/place-lentilles-billet-v1.md` (branche `claude/brave-galileo-jhp684`, commit `65daf233`) | `a6e91e25f0331c7ee311f4a7ec826612ceada4f628acb63032cfb23d85b4dc18` |
| `docs/notes/neuron-lens-v1/billet/paragraphe-methode-lentilles-billet-v1.md` (commit `36466f6a`, empreinte seule) | `47a9d83cbc627ea822f64ddd45e066557b78b7d1dfc623d7de61030d689172ee` |
| `prereg/lecture-sondes-bbis-par-lentilles-v2.md` (empreinte seule) | `a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15` |
| `docs/sources/lesswrong-politique-ia-v1/resume-politique-v1.md` | `89f9a9ca1d8b23815421703fd09acf28657e91ed8cc64f074dfc63362a377295` |
| `docs/notes/engagement-date-v1/texte-engagement-date-v2.md` (empreinte seule) | `cf445a1f0abc0d09f0df6095175101811f6bb6c436439eb5e673a534568c51ce` |
| `scripts/depot_expurge_v11.py` (empreinte seule) | `86afc00653bcacdfbc5c19598883c42166118442731f797b7e3dab4a4b85c20a` |
| Autre dépôt, `claude/PASSATION_SESSION_TRAVAIL_2026-11-21.md` (`b336f48`) | `aee8f55148563cdbeb3feee717ef5ac991c9eb80f1cedfd77b0904a3d8b9bba5` |
| Autre dépôt, `DECISIONS.md` (décisions 164, 167, 168, 183, 186, 203) | `bbaf584f0e79d0b1d7ceea4006ea9ce8700f1b7f6c8218c797753dc883ee9825` |
| Autre dépôt, `claude/note_etape_2026-11-13/BILLET_FORUM_v6_en.md` (titre et plan lus) | `6025ab5a7c085d0b51ab3ec629eb42249b6c9fc1fa58b79968f2535754eb876a` |
| Autre dépôt, `claude/note_etape_2026-11-13/verifier_billet_v6.py` (empreinte seule) | `19108af5840c4344ca416899af935d94ea93f9e34b518e5e3282111d37977a8f` |

Écrit le 2026-11-21 vers 17:52Z (`date -u`).
