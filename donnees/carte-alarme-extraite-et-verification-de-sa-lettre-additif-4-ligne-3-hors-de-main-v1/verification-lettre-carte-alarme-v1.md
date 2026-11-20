# Vérification de la lettre de la carte de l'alarme contre le § 1 de l'additif 4 scellé — v1

Pièce de travail (classe C), écrite le 2026-11-20 (`date -u` : 10:55Z) par un vérificateur neuf, modèle O, sur le mandat `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-4-mot-alarme-v1/extraction-carte-v1/mandat-verificateur-lettre-carte-alarme-v1.md` (`bc348b4607663ce86a5fb36ce2e6afc4bb697b5bb53e1984469a7312799dc814`, égale à son compagnon), sous GO-2026-11-20-39, point (6), et R-4202. Cette pièce va avec la sortie, hors de `main`. Elle ne retouche ni la règle, ni l'additif. Le mot de la carte reste « mesurée, sans mot » au registre.

Règle d'aveugle tenue : aucun fichier ouvert sous les dossiers d'exécution et de verdict de l'étage 1, ni sous `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Sous `archives-reponses-modeles/`, un seul geste hors du programme : `test -f` sur le fichier des cartes. Aucune autre carte lue.

## 1. Commandes exactes, codes de retour, empreintes

| # | commande | retour |
|---|---|---|
| 0 | `env -C …/extraction-carte-v1 sha256sum -c mandat-verificateur-lettre-carte-alarme-v1.md.sha256` | OK |
| 0 | `sha256sum …/extraction-carte-v1/extraire_carte_alarme_v1.py` | `79f2cc69245a0e00f2c9bc77202440447cbd0db32dc491a7c5dc8ed6bf539659`, égale au mandat |
| 0 | `sha256sum …/extraction-carte-v1/contre-lecture-extraction-carte-alarme-v1.md` | `d75699edadcc829ec1a00c5cca82e660540a8237e0a7ee235df3165fd2350820`, préfixe égal au mandat |
| 0 | `cp` du programme vers `programme/extraire_carte_alarme_v1.py`, puis `sha256sum` de la copie | `79f2cc69…539659`, égale |
| 0 | `test -f /home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json` | 0 |
| 0 | `git -C /home/user/controle-ia-travail fetch origin main` | 0 |
| 0 | `git -C … show origin/main:prereg/organisme-auto-conception-v9/additif-4-preenregistrement-ligne-3-mot-alarme-v2.md > …/additif-4-v2.md` | `841cef1e99126762019f45bdacca7ff7d6291c91b34c4f3d434c854c262db704`, égale au mandat |
| 0 | `git -C … show origin/main:prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md > …/ligne-3-v7.md` | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`, préfixe égal au mandat |
| 1 | `python3 -B /home/user/controle-ia-travail/scripts/verifier_environnement_agent_v1.py` | code 0, statut « lu », aucune anomalie ; Python 3.13.18 |
| 2 | `env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verificateur-lettre-carte-alarme/programme /home/user/controle-ia-travail/.venv/bin/python -I -B extraire_carte_alarme_v1.py --fiches /home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json --sortie /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verificateur-lettre-carte-alarme/sortie/carte-alarme-v1.json` | **code 0**, sortie standard « FAIT » ; joué une fois |
| 2 | `env -C …/sortie sha256sum -c carte-alarme-v1.json.sha256` | OK |

Empreintes de la sortie : `carte-alarme-v1.json` = `c1b0947cd97614d54dd443a7a1eb2c7e787f941473e76f5d64c1c21e5c396bce` ; son compagnon `carte-alarme-v1.json.sha256` = `f343cbd6ffd5f5a7853d71010823b6b99e01c122f321300008a223bd5eb93665`. Le programme a vérifié lui-même l'empreinte du fichier des cartes ; la clé qui la porte dans la sortie concorde avec le préfixe `ba65c411…` du mandat.

## 2. Ce que porte l'enregistrement, hors de `contenu`

- Au niveau de la carte : `empreinte`.
- Au niveau haut : `empreinte_fiches`, `identifiant`.
- `meta` absent (retiré, comme voulu).

Aucune de ces trois clés ne semble désigner l'espèce du proposeur : deux sont des empreintes, la troisième un identifiant de carte, qui concorde avec celui que porte le titre de l'additif 4. Valeurs non recopiées ici.

## 3. La lettre de la carte

Titre : « Sentinelle de dérive des juges sur un panier d'ancrage » ; axe : robustesse. Clés de `contenu` : `axe`, `ce_qui_distingue`, `ce_qui_la_refuterait`, `cout`, `epreuve_monde_plante`, `limites`, `mecanisme`, `module_change`, `plus_proche_voisin`, `titre`.

Passages qui portent sur la règle de mot, cités à la lettre :
- Mécanisme : « À chaque génération, l'orchestrateur compare les erreurs de chaque juge sur les ancres à la référence scellée, par un test séquentiel préenregistré : statistique, seuil et taux de fausse alarme gelés d'avance, validité à tout instant ou nombre de regards fixé. »
- Critères (épreuve) : « Critères calculés par programme : taux de détection ; délai en générations après le point planté ; taux de fausse alarme sur les suites sans changement ; part des alarmes portant sur un changement qui modifie réellement l'exactitude des juges contre l'oracle. »
- Bras (épreuve) : « C, base bon marché : test de rupture sur le taux brut de « vrai » rendu par chaque juge sur toutes les cartes ; D, C avec autant d'appels supplémentaires que B, dépensés à rejuger des cartes de production. Coût apparié entre B et D, en appels et jetons lus dans le journal. »
- Réfutation, entière : « Le mécanisme est abandonné si, à coût apparié, B ne détecte pas mieux que D (même délai, même taux de détection) sans faire moins de fausses alarmes. Il l'est aussi si le taux de fausse alarme mesuré sur les suites sans changement dépasse le taux gelé, ou si B signale surtout des changements sans effet sur l'exactitude contre l'oracle (alarmes sans conséquence sur la vérité). »

**Seuils et chiffres.** La carte ne porte **aucun seuil chiffré** : ni taux de fausse alarme, ni marge de détection, ni délai, ni part, ni nombre d'ancres (« Le nombre d'ancres nécessaire n'est pas calculé ici »). Ses seuls nombres sont des renvois de catalogue et un numéro d'article. Le point 6 du § 9 de l'additif (« si sa clause de réfutation porte un seuil que le texte tait ») reçoit donc la réponse : **non**. En revanche, deux de ses clauses portent un **seuil en mots** (« le taux gelé » ; « surtout ») que l'additif lit autrement (lignes 5 et 7 de la table).

## 4. Table de comparaison

Poids : effet sur ce que le calcul contre-lu prédit pour la carte (« réfuté sur le banc » à au moins 0,9999, additif 4 § 3.1). « Nul » = aucun effet sur ce mot prédit ; l'écart de lettre est dit à part.

| # | point de la carte | ce que disent l'additif (§ 0 à § 2) et le texte (l. 141, 185, 228, 318) | accord ou écart | poids |
|---|---|---|---|---|
| 1 | Revendication : sentinelle sur ancres à vérité connue, comparées à une référence scellée, qui signale qu'un juge a changé alors que le nom servi reste le même | § 1 : « Une sentinelle sur ancres signale qu'un juge a changé sous un nom inchangé » ; l. 228, référence scellée | accord | nul |
| 2 | La carte revendique aussi un arrêt écrit « dérive de juge », la décision au directeur, la référence par juge **et par classe de témoin**, un vivier d'ancres stratifié renouvelé, jamais servi aux proposeurs | Le texte (l. 228) ne joue qu'un test binomial sur le nombre total d'erreurs contre un taux de référence ; l'additif n'en dit rien et ne le revendique pas | écart de portée (le banc n'éprouve que la détection) ; choix du texte, non de l'additif | nul |
| 3 | Test « séquentiel préenregistré », « validité à tout instant ou nombre de regards fixé » | l. 228 : onze tests par suite au niveau 0,05 / 11, nombre de regards fixé | accord (seconde branche de l'alternative) | nul |
| 4 | Critères : détection ; délai ; fausse alarme sur les suites sans changement ; part des alarmes à effet | l. 228 : « taux de détection, délai, fausse alarme sur les suites sans changement, part des alarmes qui portent sur un changement à effet » ; § 1, points (1) à (4) | accord, mot pour mot en substance | nul |
| 5 | Réfutation, fausse alarme : « dépasse le taux gelé » | Texte l. 185 : « taux de fausse alarme gelé 0,05 par suite ; borne de réfutation 0,08 » ; additif clause 1 : atteinte si plus de 80 sur 1 000 (0,08) ; § 1 (1) : « plus que la borne » | **écart de lettre** : la carte réfute au-dessus du taux gelé (0,05 dans le texte), l'additif, après le texte, au-dessus de la borne 0,08 ; la marge de 0,03 est celle du texte (référence estimée), non celle de la carte. Le texte prédit lui-même (P6, l. 141) une fausse alarme entre 0,05 et 0,08, zone où la carte, à la lettre, serait réfutée | nul sur le mot prédit, qui ne ferait que se renforcer : à 40 ancres, valeur de population 0,116, au-dessus des deux seuils ; à 20 ancres, 0,064 passerait au-dessus du seuil de la carte (ma lecture, approchée, hors du calcul contre-lu : la cellule à 20 ancres serait alors réfutée environ 19 fois sur 20) ; moyen sur la lettre |
| 6 | Réfutation, détection : abandonné si B « ne détecte pas mieux que D (même délai, même taux de détection) sans faire moins de fausses alarmes » | Additif clause 2 : atteinte si EB ≤ ED, sans exception ; plafond, plancher, marge 0,05 et test du signe pour « tenue » ; § 9 point 5 | **écart de lettre** : la carte ne se réfute sur la détection que si, en outre, B ne fait pas moins de fausses alarmes que D ; la carte compare aussi le délai **à D** ; l'additif lit la seule lettre du texte (l. 141, « détection non supérieure au bras apparié ») | nul : sur le banc, B détecte 0,40 à 0,89 des changements à effet, D 0,03 à 0,05 ; la clause n'est atteinte à aucun m |
| 7 | Réfutation, part : abandonné si B signale « surtout » des changements sans effet | Additif clause 4, lecture (b), EB / A : tenue si plus d'un demi, atteinte si un quart ou moins, indécise entre les deux | **écart de lettre** : « surtout » se lit naturellement « plus de la moitié des alarmes sans effet », soit une réfutation sous un demi ; l'additif ouvre une zone indécise entre un quart et un demi que la carte n'a pas, et son dénominateur compte aussi les fausses alarmes des suites sans changement (lecture (b) de l'additif 1), que « changements sans effet » ne nomme pas | nul : part de population 0,72 à 0,79 aux trois m, au-dessus d'un demi sous toute lecture |
| 8 | Délai : critère, et comparé à D dans la réfutation ; aucun seuil absolu | Additif clause 3 : seuils absolus d'une génération et de 17/6, choix du rédacteur (§ 9 point 3) | écart : les seuils de délai et la réfutation par délai absolu ne viennent pas de la carte | nul sur le mot de la carte (décidé par la fausse alarme à 40 ancres) ; il décide en revanche le « sans prise » prédit des cellules à 10 et 20 ancres, qui n'entre pas dans le mot prédit |
| 9 | Bras C et D : taux brut de « vrai » de chaque juge sur toutes les cartes ; D = C plus autant d'appels que B, à rejuger des cartes de production | l. 228 : C, test de deux proportions sur le taux brut de « notable » contre la première génération ; D, C avec m cartes de plus, coût apparié à B ; § 1 (2) | accord en substance (« vrai » de la carte, « notable » du texte ; la forme du test de rupture est précisée par le texte) | nul |
| 10 | Le sens des trois mots | La carte ne les emploie pas ; elle dit « abandonné ». § 1 et l. 318 : « tient » = les quatre points tenus ; « réfuté » = l'un démenti ; « sans prise » = banc qui ne sépare pas ou clause entre ses deux seuils | accord : « réfuté » répond à « abandonné » ; « sans prise » est une catégorie du texte, sans pendant dans la carte, et ses zones d'indécision viennent des seuils doubles de l'additif (écarts 7 et 8) | nul |
| 11 | La carte ne dit pas la taille du panier | P6 (l. 141) : « à partir de 20 ancres par génération », chiffre du rédacteur du texte ; additif : mot lu à 20 et 40 | accord avec le § 1 (« Le texte ne rapporte aucun seuil de la carte ») | nul |

## 5. Conclusions

1. La lettre de la carte, extraite seule par le programme contre-lu, en un passage, `meta` retiré, s'accorde avec le § 1 de l'additif 4 sur la revendication centrale, sur les quatre critères et sur les bras. Le § 1 dit juste en écrivant que le texte ne rapporte aucun seuil de la carte : **la carte ne porte aucun seuil chiffré**.
2. Trois écarts de lettre, dans la clause de réfutation : (a) fausse alarme au-dessus du « taux gelé » (0,05 dans le texte) dans la carte, au-dessus de la borne 0,08 dans le texte et l'additif ; (b) réfutation par la détection, dans la carte, seulement si B ne fait pas en outre moins de fausses alarmes que D, et avec le délai comparé à D ; (c) réfutation par la part dès que les alarmes sans effet sont « surtout » là (sous un demi), contre un quart ou moins et une zone indécise dans l'additif. S'y ajoute un écart de provenance : les seuils de délai et la réfutation par délai absolu sont de l'additif, non de la carte (déjà dits au § 9, point 3).
3. **Aucun écart ne change ce que le calcul contre-lu prédit pour la carte.** Les écarts (a) et (c) rendent la lettre de la carte plus sévère que la règle ; l'écart (a) renforcerait « réfuté sur le banc » (à la lettre de la carte, la cellule à 20 ancres le serait aussi, le plus souvent) ; l'écart (b) n'a pas de prise sur ce banc, où B détecte bien plus que D. Le mot prédit reste « réfuté sur le banc » à au moins 0,9999.
4. Le seul écart de poids moyen est l'écart (a) : la clause 1 de l'additif est fidèle au texte (l. 185), non à la carte. Il relève de la mère et de Lazar ; je ne retouche rien.
5. Observation sans poids : la ligne de statut de l'additif 4 v2 tiré de `main` dit encore « non scellée » ; son empreinte est bien celle que le mandat donne pour le texte scellé.

Vérificateur neuf, modèle O.
