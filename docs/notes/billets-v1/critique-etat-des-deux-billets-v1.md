# Critique de « État des deux billets — 21 novembre 2026 — v1 » — v1

Pièce de classe C (travail). Critique neuve (Claude Opus 5.5, sous-agent de la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`), qui n'a pas écrit la note critiquée. Écrite le 2026-11-21 entre 17:55Z et 18:05Z (`date -u`). Pièce critiquée : `docs/notes/billets-v1/etat-des-deux-billets-2026-11-21-v1.md`, empreinte `fe8f75fd6600b9da476a4107f25853e55fb961a630891df341a2c7e8cb061c0c`.

Lu à la source : registres du dépôt (`origin/main` au commit `e6fbe03ae`), branche des lentilles `claude/brave-galileo-jhp684` (`f86c91e67`), clone de « Raisons ou regard ? » au commit `b336f48` (aucun commit plus récent sur `claude/stoic-mayer-51otyy` après un `fetch`), l'interface publique d'Open Science Framework (sans compte). **Non lus, par cloisonnement** : le corps des brouillons du billet sur les sondes, leurs fiches de faits, les verdicts et résultats de P3, P3-bis, de l'étape B et de l'étape B bis, le brouillon du 13 novembre sur la sonde du saboteur instruit, et tout ce que la consigne de ce critique interdit. Aucun chiffre de résultat du programme ici.

## Verdict

- **L'identification des deux billets tient** (R-3125, mots de Lazar ; R-2647). Toutes les empreintes de la section 9 de la note ont été recalculées aux commits qu'elle cite : toutes justes.
- **« Publiable demain » tient pour le billet sur les sondes : non.** Le renvoi de Lazar (GO-2026-11-18-66) n'est pas levé, et le mot de Lazar R-4587 (« on reprend bras A et organismes discrets, on en a besoin pour les billets ») le **confirme** plutôt qu'il ne le lève.
- **Pour « Reasons or watching? », « oui, possible » est trop favorable : possible, mais peu probable en mise en ligne effective demain.** Une condition est déjà remplie (le paquet `ewx4p` est déjà public, la note le croit privé). En revanche, la note sous-estime la contrainte du site sur un premier billet et la taille du texte à réécrire (environ 3 500 mots). Une question de Lazar reste ouverte, et la note ne la cite pas (« sous embargo », décision 203).

## 1. Affirmations vérifiées et justes

| Affirmation de la note | Source relue | Constat |
|---|---|---|
| Les deux billets sont celui sur les sondes et celui de « Raisons ou regard ? » | R-3125 (`registres/decisions.md`, l. 3163), R-2647 (l. 2607) | juste |
| Renvoi « après un vrai résultat sur un saboteur discret, donc après l'entretien » | GO-2026-11-18-66 (`registres/go.md`, l. 430) | juste. Le GO nomme l'entretien du 27 novembre ; `registres/rappels.md` dit 1er décembre |
| Sujet « sondes sur saboteurs discrets » | R-3503 (l. 3641) | juste |
| Version anglaise v2 de 999 mots, sections étape B et étape B bis vides | R-2732 (l. 2692) | juste |
| Onze questions tranchées, environ 1 300 mots, réserves dans le corps, page publique de P3 avant tout lien | R-2739 (l. 2699) | juste |
| Verdict de l'étape B scellé | `registres/scellements-v1.md`, l. 20 (`VERDICT-T07-ETAPE-B`, 2026-11-17T11:20:08Z) | juste ; GO de Lazar sur ce verdict : GO-2026-11-16-15 (R-3042), non cité par la note |
| Verdict de l'étape B bis accepté par Lazar (option A) | `registres/etat.md`, l. 30 | juste |
| Gabarit v2 : sept consignes et deux objections | `gabarit-billets-v2.md`, §§ 1.1 à 1.4 | juste. Quatre consignes sont « non contredites » ; trois (explication concurrente contrôlée, appel à poursuivre, lien vers le code) sont « sous réserve » |
| Session écrit en blocs déclarés, Lazar reformule | GO-2026-11-18-50 | juste |
| « Contact, publication, paiement restent à Lazar » | GO-2026-11-21-69 | juste ; l'autonomie de douze heures court jusqu'à 2026-11-22T05:30Z et ne couvre pas la publication |
| Ordre de mise en ligne de l'autre projet | décisions 167, 168, 183 de `DECISIONS.md` (`b336f48`) | juste |
| Question ouverte : conception 2 bis ou v7 prudente | passation du 21 novembre de l'autre projet, §§ 3.5 et 4 | juste |
| Aucune pièce de billet versée depuis le 19 novembre 10:06Z | historique de toutes les branches après `fetch` | juste (clone partiel : 2 061 commits visibles dans la fenêtre, aucun fichier de billet hors cette note) |

## 2. Erreurs et faits périmés

1. **Le paquet rejouable `ewx4p` est déjà public.** Relevé sans compte le 2026-11-21 vers 18:00Z, à l'adresse `https://api.osf.io/v2/nodes/ewx4p/`, réponse 200 : `public: True`, titre « Reasons or watching? Replication package for the A2 progress report », dernière modification le 2026-11-13T22:39:51. Les six fichiers déposés ont les empreintes du fichier d'état versé (`paquet_public_osf_etat.json`, qui dit encore `public: false`). Les enregistrements `s4wz8`, `7xv2u` et `r4ck9` sont publics et sans embargo. Les sept liens du billet v6 répondent tous (200). **La condition (4) de la note est donc remplie** ; le fichier d'état est à mettre à jour et le geste à consigner. On ignore qui a rendu le projet public : par la décision 167, c'est un geste de Lazar.
2. **Lentilles, pièce 2 : la correction du code est faite.** Le correctif de la pagination a été contre-lu « conforme » (`8ba0f061…`), puis versé sur `main` (R-4650, 2026-11-21T17:59:51Z). L'opérateur est relancé sous le mandat v3 (`d24ab21e…`). La note, écrite à 17:52Z, dit « correction renvoyée ». Il reste la course et la lecture ; la pièce n'est toujours pas bloquante.
3. **La lecture de R-4587 et de GO-2026-11-21-63 est à resserrer.** « On en a besoin pour les billets » attache la reprise du bras A aux billets. Cela va dans le sens du renvoi de GO-2026-11-18-66, pas dans le sens d'une sortie rapide d'une version « saboteur instruit ». Le pluriel « billets » laisse ouverte une lecture où Lazar compte plus d'un billet du programme : à lui faire dire.
4. **R-4647 n'est pas exploité**, alors qu'il porte le commit cité par la note (`ece586d29`). Ce que dit R-4647 : Fable 5.2 et Opus 5.5 refusent le rôle de pilote ; de nouveaux agents sont admis ; les décisions 264 à 266 de Lazar fixent d'autres agents, 100 USD par clé, et le code par Fable 5.2. Ces décisions ne sont pas encore versées dans le dépôt de l'autre projet. Conséquence : l'option « attendre la conception 2 bis » s'éloigne encore (code neuf, lots non partis, solde de la clé jamais lu). La note le dit en substance ; il faut ajouter que le choix de Lazar penche d'autant plus vers v6 ou v7.
5. **« Les PDF sous droit d'éditeur en sont exclus » (règle 3) n'est pas établi.** R-4544 et R-4554 disent « à exclure de toute copie publique » : c'est une exigence, pas un constat. Dans `scripts/depot_expurge_v11.py`, la recherche ne trouve de règle explicite que pour `docs/sources/pdf/**` et `docs/sources/co-scientist-v1/*.pdf`. Or `main` porte des PDF hors de ces dossiers : par exemple `docs/notes/banc-lois-plantees-c2-v1/pdf/`, `docs/notes/veille-organismes-ideation-v2/pdf/`, `docs/notes/revendication-14-approfondie-v1/pdf/` et `docs/sources/juges-de-cartes-v1/`. Aucun motif qui les vise n'a été trouvé. Une autre garde peut les couvrir : ce n'est pas lu ici. Avant toute poussée de la copie expurgée, il faut un essai à blanc (`--a-blanc`) relu. Cela ne touche que le billet sur les sondes, s'il renvoie au code.

## 3. Manques non dits

### « Reasons or watching? »

1. **La règle du site est plus dure que ne le dit la note.** Le résumé de la politique (`resume-politique-v1.md`, points 1 et 6) compte comme production d'un modèle aussi « le texte du modèle retouché par un humain ». Pour un premier billet : « first-time writers are not permitted to use any AI text output » (2025), « closer to a zero-LLM policy » (2026). Une reformulation phrase à phrase d'un texte de 3 502 mots (`wc -w` sur la v6) risque donc d'être lue comme un texte de modèle retouché. Lazar doit l'écrire lui-même à partir des faits. C'était déjà le bloquant 1 de la lecture adverse du 13 novembre (R-2595 : « une fiche de faits en français, pas des phrases »). `RESUME_POUR_LAZAR_fr.md` existe, mais il décrit les textes du 13 novembre, pas la v6. La phrase de la v6 « I wrote this post myself » n'est vraie qu'à cette condition.
2. **Durée de la réécriture par Lazar.** La note dit « quelques heures ». Pour environ 3 500 mots techniques en anglais, écrits de sa main, l'estimation de ce critique est plutôt d'une demi-journée à une journée. Autre voie : une version plus courte, selon le gabarit. Ce n'est pas un devis.
3. **Une question de Lazar reste en suspens (décision 203).** Lazar avait demandé : « dis que c'est sous embargo dans le billet ». La session a répondu que ce serait faux, les embargos étant levés le 13 novembre, et a gardé le texte « sauf mot contraire de Lazar ». Aucun mot n'est trouvé depuis. Le relevé de ce soir confirme : aucun embargo. Il faut une confirmation d'une ligne avant la mise en ligne.
4. **Contrôle « rien de la v6 n'est contredit depuis le 15 novembre » : fait en partie ici.** Les titres des décisions postérieures à la décision 203 (expérience 1, E5, petite mesure du pivot, conceptions 2 et 2 bis) ne montrent aucune course de A3 sur les adaptateurs. La phrase de la v6 « The test on the MSM adapters themselves has not run » reste donc vraie. Les résultats d'E3 et d'E5 n'ont pas été confrontés au texte ; ce contrôle reste à la session.
5. **Le compte du site.** R-2593 : Lazar demande les instructions pour créer un compte. La passation du 18 novembre (`2026-11-18-2010.md`, point 6) laisse ouverte la question « compte LessWrong ancien ou non ». Rien de plus récent n'est trouvé. Sans compte ce soir, la mise en ligne de demain est encore moins sûre. Selon le fichier de brouillons de commentaires de l'autre projet, le premier commentaire d'un compte neuf est lui aussi relu ; ce point n'a pas été vérifié sur la source.

### Billet sur les sondes

6. **Cloisonnement propre à la section étape B bis.** L'étape B bis a un bras « transfert vers un mode tenu à l'écart » (R-2714). Or un texte public ne dit rien du mode tenu à l'écart ni des mécanismes des saboteurs (N-054, R-3503). Il faut donc, en plus du lecteur autorisé, une relecture de cloisonnement de cette section avant toute sortie. Il faut aussi trancher ce qui peut être dit de ce bras sans nommer le mode.
7. **Liste « qui a lu quoi ».** Le lecteur qui écrira les sections étape B et étape B bis sera exposé à ces issues. Il faut l'inscrire dans une version 14 de la liste. Les versions précédentes ont été contre-lues avant d'entrer en vigueur (R-3118), ce qui ajoute une étape et du temps.
8. **Revue externe.** GO-2026-11-20-50, point 6, exige une revue externe avant toute sortie, billet compris, pour les procédés de la course « nouvelles attaques ». GO-2026-11-21-72 met la revue externe de côté « jusqu'à publication du papier » pour le banc fermé. Si le billet sur les saboteurs discrets touche l'attaquant informé ou ces procédés, il faut un mot de Lazar pour dire si un billet compte comme « publication ».
9. **Pièce oubliée.** Un brouillon antérieur sur la sonde du saboteur instruit existe : `docs/notes/publiabilite-ce-soir-v1/` (brouillon 1, registre des affirmations, deux lectures adverses). Sa lecture adverse dit « publiable après corrections, seulement comme notes du billet que Lazar écrira », avec trois bloquants (R-2595). R-2732 dit que ce billet « ne sert pas tel quel » mais que deux morceaux sont réutilisables. La note ne le mentionne pas ; il ne change pas le verdict.

## 4. Estimations de durée

- **Choix de Lazar (« une minute ») : juste.**
- **Sondes, sections B et B bis (2 à 4 heures) et texte entier (2 à 3 heures) : plausibles.** Il faut y ajouter la relecture de cloisonnement, la version 14 de la liste et la réécriture par Lazar d'environ 1 300 mots. Même si le renvoi était levé, « deux ou trois jours » est un minimum, relecture du site non comprise.
- **v7 de l'autre projet (2 à 4 heures) : plausible pour une phrase et ses nombres**, si un modèle rédacteur est disponible sur le nouveau compte (Fable est limité sur l'ancien jusqu'au 27 novembre, 15:00Z).
- **Réécriture de Lazar (« quelques heures ») : optimiste**, voir le point 3.2 ci-dessus.

## 5. Ce qui change dans la réponse à Lazar

- « Reasons or watching? » demain : **possible seulement si**, ce soir, Lazar choisit entre la v6 et une v7, confirme « pas d'embargo » et a un compte sur le site. Demain, il faut ensuite qu'il écrive lui-même le texte, sur une demi-journée à une journée, et que la session repasse ses nombres. Puis vient la relecture d'un premier billet, de durée inconnue. Le paquet public est déjà en ligne.
- Billet sur les sondes : **non**, et pas avant un résultat de sondes sur un saboteur discret, sauf si Lazar lève lui-même son renvoi.

## 6. Sources relues (chemins et empreintes)

| Pièce | Empreinte |
|---|---|
| Note critiquée | `fe8f75fd6600b9da476a4107f25853e55fb961a630891df341a2c7e8cb061c0c` |
| `registres/decisions.md` (copie de travail, après R-4648) | `b5f1a44ede798c8097701f51a7b51712001c46106ca4811f31f1bf5f0bf660da` |
| `registres/go.md` (copie de travail, jusqu'à GO-2026-11-21-72) | `5fa343b8e7c76f9522d0ef6745a505cde89b8da4aed3a6a1ea569baa0b7eb274` |
| `registres/etat.md` | `31c47d74312b011bfbaad441dfb051ae78fb624464099008e9e18dbc610262d4` |
| `registres/qui-a-lu-quoi-v13.md` (lignes 106 et 107) | `ffc4420e378c5e0931757d4da1c6bdae96e1257527221262539d0cd42d000595` |
| `docs/notes/billets-v1/gabarit-billets-v2.md` | `5eee79b3cf051fbecc5a278bfbf6e54f2a6d9164326ec2512b88e3390b46a2a5` |
| `docs/sources/lesswrong-politique-ia-v1/resume-politique-v1.md` | `89f9a9ca1d8b23815421703fd09acf28657e91ed8cc64f074dfc63362a377295` |
| `scripts/depot_expurge_v11.py` (motifs cherchés, non exécuté) | `86afc00653bcacdfbc5c19598883c42166118442731f797b7e3dab4a4b85c20a` |
| R-4650 sur `origin/main` (`e6fbe03ae`) | commit cité |
| Autre dépôt, `DECISIONS.md` (`b336f48` ; décisions 167, 168, 183, 186, 203 et titres suivants) | `bbaf584f0e79d0b1d7ceea4006ea9ce8700f1b7f6c8218c797753dc883ee9825` |
| Autre dépôt, passation du 21 novembre (`b336f48`) | `aee8f55148563cdbeb3feee717ef5ac991c9eb80f1cedfd77b0904a3d8b9bba5` |
| Autre dépôt, `BILLET_FORUM_v6_en.md` (3 502 mots ; liens, « What comes next », « How this was made ») | `6025ab5a7c085d0b51ab3ec629eb42249b6c9fc1fa58b79968f2535754eb876a` |
| Open Science Framework, nœud `ewx4p` et enregistrements `s4wz8`, `7xv2u`, `r4ck9` | relevé sans compte, 2026-11-21 vers 18:00Z |

Écrit le 2026-11-21 vers 18:05Z (`date -u`).
