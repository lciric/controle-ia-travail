# Contre-lecture : collisionneur v9 version 7

Écrite le 21 novembre 2026 vers 17:40Z par le contre-lecteur, Claude Fable 5.2 (`claude-fable-5-2`), même rôle que le vérificateur de la version 6, autre modèle que le développeur (Claude Opus 5.5). Pièce d'instrument (classe B). Mot de Lazar : GO-2026-11-21-63.

Ce que je n'ai pas fait : aucun appel à un modèle, aucun comptage, aucune dépense ; aucune clé lue (essais et sondes sous `env -i`, clés factices des doublures) ; aucun commit ; aucun fichier du dépôt modifié hors cette pièce et son sceau. Sur la branche des versements `origin/runs/collisionneurs-reprise-minuit-v1` (761c2c5a), je n'ai lu que des `journal.jsonl` et un `especes.json`, par `git show` ; aucune réponse de modèle, rien sous `archives-reponses-modeles/` ni `/root/.claude/`. Six pages publiques de Google lues sans clé (section 5). Mes sondes, mutations et corrections ont tourné sur des copies, dans mon bloc-notes.

## Verdict

**À corriger, sur la seule option `--repli-lot`** (le repli par l'interface de lot de Google) : deux corrections obligatoires (C-1, C-2) et un essai réel avant tout usage. **Hors de cette option, la version 7 (`319a7b66…`) est conforme** et peut reprendre telle quelle la percée, la dérive v2, les mathématiques et la question fusionnée ; l'antériorité se reprend par un troisième envoi en flux, sans `--repli-lot`.

1. **Les neuf corrections sont portées et justes ; V-1 est au texte exact**, code et essais.
2. **Carbon réfléchit jusqu'au bout au réglage envoyé et la garde ne se déclenche plus à tort** : 21 réponses réelles complètes sur 21 passent la garde de la version 7, dont les 4 que l'ancienne garde avait arrêtées. Règle des 16 000 jetons de texte tenue (65 536 − 49 152 = 16 384). **Argon ne réfléchit pas : 0 jeton de pensées sur 22 réponses réelles sur 22** ; la version 7 envoie le même budget. À dire à Lazar, avec le niveau de réflexion (section 3).
3. **Reprise sans perte ni double paiement : oui** pour les quatre dossiers, et pour la question fusionnée (sonde). `--rejuger-essai` est sans réseau et ses conditions sont justes, les trois ajouts du développeur compris.
4. **Interface de lot** : la forme supposée concorde avec la documentation publique. Trois obstacles : un appel non diffusé de Carbon est plafonné à 32 768 jetons, pensées comprises (15 réponses réelles sur 21 sont au-delà) ; un lot vise 24 heures, le script l'annule à 5 400 s ; un relevé refusé abandonne un lot payé (C-1) et un lot de forme inattendue est jeté (C-2).
5. **Devis au-delà du reste : sûr.** Aucun envoi ne part si la dépense plus son pire cas dépasse la ligne. Le devis surestime : une fois les critiques connues, le pire cas du tour III.3 tombe à 9,45 USD (dérive v2, pour 13,36) et 9,68 USD (mathématiques ; 19,18 avec le tour III.2, pour 21,77).
6. **Refus de crédit** : la lecture « ni texte ni usage final » est la seule qui rende la correction opérante, et elle refuse bien hors du critère. Le coût zéro, lui, n'est établi par aucune pièce : dans le cas des mathématiques, le flux tournait depuis 171 secondes. Correction recommandée C-3, à trancher par la mère.

## 1. Pièces, empreintes, essais

Empreintes recalculées, toutes égales aux compagnons `.sha256` :

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v7.py` | `319a7b66b5b9…` |
| `test_collisionneur_v9_v7.py` | `7afaa354a85f…` |
| `rapport-developpeur-collisionneur-v9-v7-v1.md` | `c055018231a0…` |
| `verification-collisionneur-v9-v6-fable-v1.md` | `523dda3759ae…` |
| `reflexion-relance-collisionneurs-opus-max-v1.md` | `28ce8440d461…` |
| liste versée des modèles de Google | `eeec19e80408…` |
| page de prix versée | `40202cdd6fc4…` |

Essais rejoués une fois, hors réseau, sans clés, dossiers temporaires à moi : **version 7 : 270 passés, 1 sauté ; version 6 : 201 passés, 1 sauté** (le sauté est la copie du run « dopamine », non désignée). Ce sont les comptes du développeur. Les essais sur copies des quatre dossiers ont tourné, non sauté.

Mes 17 mutations, différentes des 25 du développeur, chacune sur une copie, suite entière (témoin sans mutation : 270 passés) :

| mutation | prise |
|---|---|
| rejugement : marqueur du journal non exigé | oui (1) |
| rejugement : coût recompté à la ligne de rejugement | oui (1) |
| vérification : rejugement au journal sans cellule non signalé | oui (1) |
| lot : relevé coupé non repris | oui (1) |
| lot : pire cas au prix plein | oui (1) |
| crédit : refus admis après un usage final | oui (1) |
| crédit : tout message d'erreur admis | oui (1) |
| absence hors cellule acceptée | oui (6) |
| V-1 : plafond de relance lu au lieu de celui de l'envoi | oui (2) |
| rejugement : espèce de Google non exigée | non — redondant avec le statut, sauf journal altéré |
| rejugement : usage lu non exigé | non — idem |
| rejugement : modèle conforme non exigé | non — l'artefact du développeur est refusé par le statut d'abord |
| rejugement : marqueur du texte scellé non exigé | non — redondant (marqueur du journal et empreinte) |
| vérification : empreinte du rejugement non comparée à l'essai | non |
| lot : plusieurs réponses admises | non — sans effet, une seule requête par lot |
| lot : toute coupure compte, quel que soit le mode | non — sans effet |
| **défaut de réglage : essai d'avant la version 7 lu sans budget** | **non — essai témoin proposé (remarque 1)** |

## 2. Question 1 — les neuf corrections

Différentiel de la version 6 à la version 7 relu ligne à ligne (489 lignes) : il ne contient que les neuf corrections, la version et les textes d'aide.

| n° | correction | portée | juste |
|---|---|---|---|
| 1 | V-1 | oui, **au texte exact** : signature de `juger`, les deux lignes, l'appel dans `executer_cellule` ; les quatre essais de ma section 6 à la lettre, les deux anciens retirés ; textes accordés | oui |
| 2 | budget séparé de la provision | envoyé, journalisé (`budget_reflexion`), lu par `reglage_en_defaut`, contrôlé à la composition | oui |
| 3 | Argon | plafonds 32 768, budget 8 192, provision 16 384, prix 4 et 20 ; lignes 347 et 354 de la page versée relues par moi | oui, voir section 3 |
| 4 | Opus à 64 000 dès le premier envoi | oui | oui |
| 5 | `--rejuger-essai` | oui | oui (section 4) |
| 6 | `--repli-lot` | oui, forme conforme à la documentation | **à corriger** (section 5) |
| 7 | refus de crédit | oui | lecture juste, fait non établi (section 7) |
| 8 | `--accepter-absence` | refus avant toute écriture | oui |
| 9 | essai de ma remarque 1 ; copies des quatre dossiers | à la lettre ; rejouées | oui |

Hors de l'option `--repli-lot`, le code du lot est inerte : le mode reste « flux », l'appelant et les prix ne changent pas.

## 3. Question 2 — Carbon et Argon

### 3.1 Ce que la version 7 envoie, et ce que disent les journaux réels

| espèce | plafond envoyé | budget envoyé | seuil de la garde (sortie facturée) | réponses réelles complètes | pensées relevées | texte relevé |
|---|---|---|---|---|---|---|
| Carbon | 65 536 | 32 768 | 114 688 | 21 | 19 727 à 44 101 | 8 400 à 14 401 |
| Argon | 32 768 | 8 192 | 49 152 | 22 | **0 partout** | 6 228 à 17 714 |

- **Carbon.** Les 21 réponses, rejouées dans `juger` de la version 7, sont toutes « OK » ; 4 dépassaient le budget (rapport au plus 1,35), aucune la provision. Sortie facturée au plus 55 125 : jamais le plafond. La garde ne peut plus se déclencher à tort : Google coupe à 65 536, le seuil est à 114 688. Elle reste un filet contre une facturation au-delà du pire cas compté.
- **Règle « Appels à Carbon ».** Tenue par construction et contrôlée avant l'envoi : 65 536 − 49 152 = 16 384. Dans les faits, il restait au moins 21 435 jetons au texte. Limite : la provision n'est pas une borne envoyée ; au-delà de 49 536 jetons de pensées (rapport 1,51, jamais vu), le texte aurait moins de 16 000 jetons.
- **Argon.** La garde ne se déclenche pas à tort (sortie au plus 17 714 pour un seuil de 49 152). Mais 22 réponses sur 22 portent `thoughtsTokenCount` nul et aucune partie de pensée, sous le budget 8 192 que la version 7 envoie encore. Ni la réflexion d'Opus ni le rapport du développeur ne le disent. Les 16 384 jetons de provision ne servent qu'au pire cas compté.

### 3.2 « Jusqu'au bout » : le niveau de réflexion

Page publique de Google sur la réflexion, lue ce jour, non versée (`a964d5cf…`, section 5.1) : pour Carbon et Argon, la réflexion se règle par niveau (bas, moyen, haut) ; **moyen par défaut** (lignes 678, 679 et 702) ; « haut » est la profondeur maximale (ligne 703). Le script n'envoie qu'un budget, jamais un niveau. C'est la limite 2 de ma vérification de la version 6 (section 3.4), restée ouverte, maintenant sur une page lue par moi.

À dire à Lazar : avec la version 7, Carbon réfléchit au niveau par défaut, sous un budget souple ; Argon ne produit aucune pensée. Laisser « réfléchir jusqu'au bout » au sens de Google demande d'envoyer le niveau haut. À instruire avant toute nouvelle course : verser la page ; relever le nom du champ pour `generateContent` (la page décrit `thinking_level` pour une autre interface) et s'il se cumule avec le budget ; un envoi d'essai par espèce. Un niveau sans budget ne borne plus la réflexion en jetons : « la réflexion bornée à part » de `CLAUDE.md` est alors à relire par Lazar. Rien de cela ne bloque la reprise des dossiers en cours, dont les tours faits l'ont été à ce même réglage.

## 4. Question 3 — reprise et rejugement

### 4.1 Les dossiers

Journaux réels relus (statuts, usages, coûts) ; copies du développeur rejouées ; ma sonde sur la question fusionnée.

| dossier | état au journal | reprise par la version 7 | envois |
|---|---|---|---|
| percée (…-114810) | 9 cellules ; critique de Carbon complète (fin `STOP`, marqueur, sortie 55 125, écart nul), arrêtée par l'ancienne garde, essai 1, seul essai | `--rejuger-essai E3-T2-critique-croisee-E:1` | 5 |
| dérive v2 (…-131044) | idem (sortie 44 891) | idem | 5 |
| antériorité (…-131029) | 14 cellules ; réponse de Carbon coupée deux fois | troisième envoi | 1 |
| mathématiques (…-093850) | 5 cellules ; critique de Fable refusée pour crédit | tours III.2 et III.3 | 10 |
| **fusionnée (…-153256)** | arrêtée depuis la réflexion d'Opus : critique de Carbon complète (sortie 44 914), ancienne garde, quatre espèces, Carbon en D | `--rejuger-essai E3-T2-critique-croisee-D:1`, quatre espèces | 4 |
| but (…-152615) | 12 cellules sur 12 | rien | 0 |

Dans chaque cas : `verifier` tient avant et après ; aucun fichier d'avant n'est touché ; le journal d'avant est un préfixe du journal d'après ; un seul changement de script déclaré ; aucune cellule valide renvoyée ; la même commande relancée n'envoie rien. La cellule rejugée n'est ni renvoyée ni comptée une seconde fois. Les envois neufs (Fable des mathématiques, Carbon de l'antériorité) sont des paiements neufs, inévitables.

### 4.2 `--rejuger-essai`

- Sans réseau : `rejuger_essai` n'ouvre aucune connexion ; la cellule vient de la réponse scellée, dont l'empreinte est comparée au journal.
- Les conditions de la section 8.5 de la réflexion sont toutes là. Un essai arrêté par la garde de la version 7 elle-même ne peut pas être rejugé (sortie au-delà de la sortie comptée) : seul un arrêt de l'ancienne garde passe.
- **Les trois conditions ajoutées par le développeur sont justes** : elles ne font que refuser.
  - *Dernier essai de la cellule* : retire tout choix entre deux réponses. À savoir : si deux essais étaient rejugeables, la garde corrigée aurait gardé le premier, pas le dernier ; aucun dossier réel n'est dans ce cas (un seul essai chaque fois).
  - *Sceaux du prompt et de la réponse égaux au journal* : nécessaire, `verifier` l'exige ensuite.
  - *Marqueur en fin du texte scellé* : redondant, sans danger.
- Écart nul exigé à la lettre (un écart négatif, que `juger` accepte, est refusé) : plus strict, juste ; les trois essais réels ont un écart nul.

À savoir (sonde) :
1. Un rejugement refusé sur un dossier d'une autre version, avec `--reprise`, laisse au journal la ligne de changement de script. Le texte d'aide dit « rien n'est écrit » : vrai pour la cellule et la ligne de rejugement seulement (remarque 2).
2. Le rejugement et le tour III.3 partent dans la même commande : on ne peut pas rejuger seul.

## 5. Question 4 — l'interface de lot de Google

### 5.1 Pages lues, sans clé

Lues ce jour, **non versées** (provenance par transcription tant qu'elles ne le sont pas, R7) ; copies dans mon bloc-notes, à verser par la mère :

| page | empreinte |
|---|---|
| guide du lot, `ai.google.dev/gemini-api/docs/batch-api.md.txt` | `eb44b7b33dd0…` |
| référence du lot, `ai.google.dev/api/batch-api.md.txt` | `22fe8141b85f…` |
| réflexion, `…/docs/thinking.md.txt` | `a964d5cf09c7…` |
| longues sorties, `…/docs/long-decode.md.txt` | `a23174377b30…` |

### 5.2 Ce qui concorde

Création (`POST …/models/{modèle}:batchGenerateContent`, corps `batch.display_name` et `batch.input_config.requests.requests[].request`), nom `batches/…`, relevé (`GET …/v1beta/batches/…`, champs `done` et `metadata.state`), annulation (`POST …:cancel`), réponses sous `response.inlinedResponses`, liste imbriquée, chaque élément portant `response` ou `error` : le script suit la documentation. Les états sont `BATCH_STATE_*` dans la référence et `JOB_STATE_*` dans le guide : le script accepte les deux. La liste versée donne `batchGenerateContent` à Carbon et à Argon. Prix : moitié, lignes 43, 184, 191, 403 et 410 de la page versée.

### 5.3 À vérifier avant le premier usage

1. **Plafond d'un appel non diffusé : décisif.** Pour Carbon et Argon, 65 536 jetons par flux mais **32 768 par appel non diffusé**, pensées comprises (réflexion, ligne 917 ; longues sorties, lignes 135 et 168). Un lot est un appel non diffusé ; la liste versée donne d'ailleurs 32 768. Le script y envoie 65 536. Trois issues possibles, aucune documentée : refus à la création (sans coût), erreur dans la réponse du lot (comptée au pire, 1,15 USD, sans facture), ou coupe silencieuse à 32 768. Or 15 réponses réelles de Carbon sur 21 dépassent 32 768 ; les deux envois coupés de l'antériorité portaient déjà 23 731 et 20 622 jetons de pensées. Une coupe donnerait une réponse tronquée, relancée en lot au même plafond, payée deux fois, sans cellule ; la règle des 16 000 jetons de texte ne serait plus tenue.
2. **Délai.** Un lot vise 24 heures (guide, lignes 16 et 2341) et expire à 48. Le script attend le délai de l'espèce, 5 400 s, puis annule et compte au pire. Un lot en file est alors compté 1,15 USD sans rien coûter ; un lot fini entre le dernier relevé et l'annulation est payé et perdu.
3. **Création non idempotente** (guide, ligne 2367). Une création dont la réponse se perd laisse un lot sans nom au journal, facturé s'il aboutit. Tous les lots s'appellent « collisionneur » : avant toute relance, lister les lots à la main (`GET …/v1beta/batches`).
4. **Champs de la réponse en ligne** : `modelVersion` (sinon code 3 après paiement), `usageMetadata` avec pensées et total (sinon code 6, compté au pire), parties de pensée sous `includeThoughts`.
5. **Relevé refusé** : un 429 répété, un 403 ou 407 du mandataire, un 404 abandonnent le lot sans annulation ; la relance en crée un second (sonde : deux lots créés, le premier compté au pire, 1,15 USD, et jamais relu). Correction C-1.
6. **Forme inattendue d'un lot réussi** : la réponse payée n'est pas gardée (sonde : 0 caractère dans `essais/`). Correction C-2.
7. Prix réellement facturé et effet d'une annulation : à lire sur la console après l'essai.

Méthode : un essai réel à la main sur une question factice de Carbon, mêmes `maxOutputTokens` et `thinkingConfig`, relevé brut versé. Quelques centimes, donc un GO.

### 5.4 Recommandation

Ne pas employer `--repli-lot` pour l'antériorité. Reprendre par un troisième envoi en flux : pire cas compté 2,44 USD pour 13,28 restants. Les deux coupures touchent la même cellule ; si la troisième coupe aussi, saisir la mère (absence acceptée de la réponse de Carbon, qui ne nourrit aucune autre cellule, ou lot après corrections et essai).

## 6. Question 5 — devis au-delà du reste de la ligne

**C'est sûr.** Avant chaque envoi, `executer_cellule` refuse (code 4, ligne « refus avant l'envoi », rien d'envoyé) si la dépense plus le pire cas de cet envoi dépasse le plafond ou la ligne. Le coût réel d'un envoi ne dépasse son pire cas que si une garde se déclenche, et la course s'arrête alors. Le pire qui puisse arriver est un arrêt au code 4 avant la fin du tour III.3 : aucune perte, aucun paiement ; les cellules faites restent valides et les réponses du tour III.3 ne nourrissent aucune autre cellule.

Le devis de reprise surestime pour deux raisons (sondes sur copies, USD comptés) :

| dossier | reste (ligne et plafond) | devis | cause | tour III.3 une fois les critiques connues |
|---|---|---|---|---|
| dérive v2 | 13,36 | 15,73 | compte la cellule de Carbon à rejuger (2,54) et borne sa critique à 295 000 caractères pour 30 392 réels | **9,45** |
| mathématiques | 21,77 | 28,45 | borne chaque critique non écrite au plafond de son auteur | **9,68** pour des critiques aux plus grandes longueurs relevées par espèce, soit 19,18 avec le tour III.2 (9,50) |
| percée | 17,23 | 15,86 | idem dérive v2 | 9,64 |

Même si chaque envoi coûtait son pire cas, les trois dossiers finissent sans relance. Avec le coût réel relevé (environ la moitié du pire), une relance tient aussi.

Recommandations :
1. Lancer tel quel, lignes et plafonds de la réflexion d'Opus. Ne pas enchaîner la reprise sur le code de retour de `devis-reprise` : il rend 4 pour les mathématiques et la dérive v2 (sonde).
2. Dire à Lazar avant le départ : un arrêt au code 4 en fin de tour III.3 est possible, sans perte ; aucune version ne sait relever une ligne.
3. Un seul trou connu de la garde : un envoi en vol quand le processus est tué n'a pas de ligne au journal (cas du run « percée », 0,45 USD). Ne jamais couper une session pendant un envoi.

## 7. Question 6 — refus de crédit d'Anthropic

Les deux cas réels (journaux) : `message_start` reçu, modèle servi et identifiant de réponse présents, un bloc de réflexion ouvert, puis l'erreur `invalid_request_error`, « Your credit balance is too low… ».

| run | cellule | durée du flux avant l'erreur | compté par la version 3 |
|---|---|---|---|
| dérive v1 | conception d'Opus, essai 2 | 10 s | 1,29 |
| mathématiques | critique de Fable, essai 1 | **171 s** | 3,03 |

- **La lecture est juste comme lecture.** `message_start` annonce toujours une entrée non nulle : « usage nul » pris à la lettre ne serait jamais vrai. Hors du critère (texte reçu, usage final reçu, autre type, autre message), l'envoi reste compté au pire : mes deux mutations et les quatre artefacts du développeur le montrent.
- **Le coût zéro n'est pas établi.** Aucune pièce versée ne dit qu'un flux arrêté par un refus de crédit n'est pas facturé. La référence de l'interface de Claude livrée avec Claude Code (compétence `claude-api`, `shared/error-codes.md` et `shared/model-migration.md`, non versée) classe `billing_error` en 402 et ne dit rien d'un flux coupé par une erreur ; le cas voisin qu'elle décrit, un refus du modèle en cours de flux, est facturé au tarif normal. Le critère « aucun texte » ignore les pensées, facturées comme de la sortie et non mesurables dans le flux (blocs de réflexion vides par défaut). Pour les mathématiques : 58 083 jetons d'entrée gardés et 171 secondes de génération, soit de l'ordre de 0,6 à 1,4 USD au prix de la table s'ils sont facturés. Ni 0 ni 3,03.
- **Portée.** L'écart ne joue qu'à l'épuisement du crédit, pour les flux en vol. Il affaiblit la garde de ligne d'au plus 1,4 USD par événement ; il ne perd rien et ne paie rien deux fois.

Recommandations : (a) Lazar lit sur la console d'Anthropic le coût du 21 novembre entre 10:02Z et 10:06Z (identifiants de réponse au journal) ; (b) en attendant, compter l'usage annoncé par `message_start` au prix réel et le garder au journal en champ, plutôt que zéro (C-3, section 8).

## 8. Corrections en texte exact

Version neuve, nom neuf (R12) : `collisionneur_v9_v8.py` et ses essais. Éprouvé sur copie : **274 passés, 1 sauté**, avec et sans C-3.

### C-1 (obligatoire avant tout usage de `--repli-lot`) : un relevé refusé n'abandonne pas un lot créé

Dans `appeler_gemini_lot`, remplacer

```python
    releves_coupes = 0
    while True:
        if HORLOGE() - debut > m["delai_s"]:
            annuler_lot(nom, cle)
            return Reponse(echec=f"lot non abouti au délai de l'espèce ({m['delai_s']} s ; {releves_coupes} relevé(s) "
                                 f"coupé(s)) ; annulation demandée", interrompue=True, nom_lot=nom)
```

par

```python
    releves_coupes, dernier_manque = 0, None
    while True:
        if HORLOGE() - debut > m["delai_s"]:
            annuler_lot(nom, cle)
            return Reponse(echec=f"lot non abouti au délai de l'espèce ({m['delai_s']} s ; {releves_coupes} relevé(s) "
                                 f"coupé(s) ou refusé(s), dernier : {dernier_manque}) ; annulation demandée",
                           interrompue=True, nom_lot=nom)
```

et

```python
        except EnvoiInterrompu:
            releves_coupes += 1
            continue
        except EchecSansEnvoi as e:
            return Reponse(echec=f"lot, relevé refusé : {e}", interrompue=True, nom_lot=nom)
```

par

```python
        except (EnvoiInterrompu, EchecSansEnvoi) as e:  # (C-1) un relevé coupé ou refusé ne coûte rien et ne dit rien du
            releves_coupes += 1                         # lot : le lot créé reste suivi jusqu'au délai, puis annulé
            dernier_manque = str(e)[:200]
            continue
```

### C-2 (obligatoire avant tout usage de `--repli-lot`) : le relevé d'un lot fini que le script ne sait pas lire est gardé

Dans `appeler_gemini_lot`, remplacer

```python
    if op.get("error") or etat not in ETATS_LOT_REUSSIS:
        return Reponse(echec=f"lot fini sans succès (état {etat!r}) : "
                             f"{masquer(json.dumps(op.get('error'))[:300], cle)}", interrompue=True, nom_lot=nom)
```

par

```python
    brut = masquer(json.dumps(op, ensure_ascii=False, indent=1, sort_keys=True), cle)  # (C-2) relevé gardé dans l'essai
    if op.get("error") or etat not in ETATS_LOT_REUSSIS:
        return Reponse(texte=brut, echec=f"lot fini sans succès (état {etat!r}) : "
                                         f"{masquer(json.dumps(op.get('error'))[:300], cle)}", interrompue=True, nom_lot=nom)
```

puis

```python
        return Reponse(echec="lot réussi sans une réponse lisible", interrompue=True, nom_lot=nom)
```

par

```python
        return Reponse(texte=brut, echec="lot réussi sans une réponse lisible ; relevé brut gardé dans la réponse de "
                                         "l'essai", interrompue=True, nom_lot=nom)
```

et

```python
        return Reponse(echec=f"lot : réponse en erreur : {masquer(json.dumps(sortie[0].get('error'))[:300], cle)}",
                       interrompue=True, nom_lot=nom)
```

par

```python
        return Reponse(texte=brut, echec=f"lot : réponse en erreur : "
                                         f"{masquer(json.dumps(sortie[0].get('error'))[:300], cle)}",
                       interrompue=True, nom_lot=nom)
```

L'envoi reste « interrompu », compté au pire ; le relevé va dans `essais/…reponse.md`, scellé, jamais dans une cellule.

### C-1 et C-2, essais

Dans `test_v7_lot_artefacts_comptes_au_pire`, retirer le cas `"releve_refuse"` de la liste des paramètres et sa ligne du dictionnaire (`"releve_refuse": [lot_cree(), http_erreur(404, "inconnu")]`). Ajouter :

```python
def test_c1_lot_sain_releve_refuse_puis_abouti_un_seul_lot(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    t = FauxTransport(lot_cree(), http_erreur(404, "inconnu"), http_erreur(403, "mandataire"), lot_fini())
    c.TRANSPORT = t
    assert executer_lot(c, dossier) == "OK"
    assert [(a["methode"], a["url"].rsplit("/", 1)[-1]) for a in t.appels] == [
        ("POST", "gemini-4-carbon:batchGenerateContent"), ("GET", "abc123"), ("GET", "abc123"), ("GET", "abc123")]
    d = journal(c, dossier)[-1]
    assert d["nom_lot"] == "batches/abc123" and c.chemin_cellule(dossier, d["cellule"]).exists()


def test_c1_lot_artefact_releve_refuse_jusqu_au_delai_annule_compte_au_pire(c, tmp_path):
    dossier = coupe_puis(c, tmp_path)
    instants = iter([0.0, 10.0, 20.0, 10.0 + c.CATALOGUE["carbon"]["delai_s"] + 1])
    c.HORLOGE = lambda: next(instants)
    t = FauxTransport(lot_cree(), http_erreur(404, "inconnu"), http_erreur(404, "inconnu"), FauxFlux(corps={}))
    c.TRANSPORT = t
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    d = journal(c, dossier)[-1]
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"] > 0
    assert d["nom_lot"] == "batches/abc123" and "HTTP 404" in d["echec"] and "annulation demandée" in d["echec"]
    assert [a["url"].rsplit("/", 1)[-1] for a in t.appels] == ["gemini-4-carbon:batchGenerateContent", "abc123", "abc123",
                                                                "abc123:cancel"]


@pytest.mark.parametrize("cas", ["forme inconnue", "lot échoué", "réponse en erreur"])
def test_c2_lot_releve_illisible_garde_dans_l_essai_jamais_une_cellule(c, tmp_path, cas):
    dossier = coupe_puis(c, tmp_path)
    fini = {"forme inconnue": FauxFlux(corps={"name": "batches/abc123", "done": True,
                                              "metadata": {"state": "BATCH_STATE_SUCCEEDED"},
                                              "response": {"responsesFile": "files/xyz", "note": CLE_GEMINI}}),
            "lot échoué": lot_fini(etat="BATCH_STATE_FAILED"),
            "réponse en erreur": lot_fini(erreur={"code": 400, "message": "plafond de sortie refusé"})}[cas]
    c.TRANSPORT = FauxTransport(lot_cree(), fini)
    with pytest.raises(c.Arret) as e:
        executer_lot(c, dossier)
    d = journal(c, dossier)[-1]
    garde = (dossier / "essais" / f"{d['cellule']}.essai{d['essai']}.reponse.md").read_text(encoding="utf-8")
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "INTERROMPU" and d["cout_usd"] == d["cout_pire_usd"]
    assert json.loads(garde)["name"] == "batches/abc123" and CLE_GEMINI not in garde and d["marqueur_fin"] is False
    assert d["sha256_texte"] == c.empreinte(garde) and not c.chemin_cellule(dossier, d["cellule"]).exists()
```

### C-3 (recommandée ; à trancher par la mère) : le refus de crédit compte l'usage annoncé

Dans `appeler_anthropic`, branche du refus de crédit, remplacer

```python
                        return Reponse(modele_servi=etat["servi"], identifiant=etat["id"], types_blocs=types,
                                       echec=f"refus de crédit dans le flux, sans texte ni usage final (usage de "
```

par

```python
                        return Reponse(modele_servi=etat["servi"], identifiant=etat["id"], types_blocs=types,
                                       usage={"entree": etat["entree"] or 0, "sortie": etat["sortie"] or 0},  # (C-3)
                                       echec=f"refus de crédit dans le flux, sans texte ni usage final (usage de "
```

Le statut reste « ECHEC », code 5 ; `juger` compte alors l'usage lu au prix réel (0,58 USD pour 58 000 jetons d'entrée de Fable). Dans `test_v7_refus_de_credit_echec_cout_zero`, remplacer

```python
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "ECHEC" and d["cout_usd"] == 0.0
```

par

```python
    assert e.value.code == c.CODE_ECHEC and d["statut"] == "ECHEC"
    assert d["usage"] == {"entree": 58000, "sortie": 1}  # (C-3) usage annoncé par message_start, compté au prix réel
    assert abs(d["cout_usd"] - (58000 * 10 + 1 * 50) / 1e6) < 1e-4 and d["cout_usd"] < d["cout_pire_usd"]
```

et accorder le nom de l'essai et la docstring de `refus_de_credit` (« coût de l'usage annoncé » au lieu de « coût zéro »).

## 9. Remarques (non bloquantes)

1. **Essai témoin** pour ma mutation non prise (éprouvé : passe sur la version 7, échoue sur la copie mutée). Sans le repli sur la provision, un Neon arrêté en `MAX_TOKENS` sans texte sous la version 6 serait renvoyé au même réglage :
   ```python
   def test_cl_v7_reglage_en_defaut_essai_d_avant_le_v7_sans_budget_au_journal(c, tmp_path):
       c.TRANSPORT = FauxTransport(_vide_max("gemini-4-neon"))
       with pytest.raises(c.Arret) as e:
           executer(c, tmp_path, "neon")
       assert e.value.code == c.CODE_REGLAGE
       chemin = tmp_path / "journal.jsonl"
       lignes = [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines()]
       for x in lignes:
           x.pop("budget_reflexion", None)  # la ligne telle que l'écrivait le v9-v6
       chemin.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in lignes), encoding="utf-8")
       l = lettre_de(c, "neon")
       assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T1", l), c.MODELES[l]) is True
   ```
2. Texte d'aide de `--rejuger-essai` : écrire « rien n'est écrit pour la cellule ; la déclaration de reprise du script, elle, reste au journal ».
3. `verifier` ne compare pas l'empreinte de la ligne de rejugement à celle de l'essai dans un essai (mutation non prise) ; un cas à ajouter à `test_v7_verifier_artefacts_du_rejugement`.
4. Lot : donner à chaque lot un nom propre (cellule et essai) pour retrouver un lot orphelin ; faire un dernier relevé avant l'annulation ; une reprise qui relit le lot nommé au journal avant d'en créer un autre est une conception à part.
5. Les pages de Google donnent 20 minutes par flux ; le plus long flux réel de Carbon a duré 12 minutes 11 secondes. Le délai de 5 400 s n'est donc jamais la borne qui joue.
6. Fable est compté 10 et 50 USD par million dans la table ; la même référence de l'interface de Claude (prix relevés le 3 novembre) donne 8 et 40. Surcompte, sans danger ; à décider à part, comme pour Argon.
7. Restent ouvertes, comme le dit le développeur : la relance au même plafond d'une réponse coupée ; les longues sorties au-delà de 65 536.

## 10. Avant tout appel

1. Pour chaque dossier : `verifier` par la version 7, avant et après ; l'ancienne session arrêtée et versée.
2. Commandes de la réflexion d'Opus (section 7), avec deux changements : antériorité **sans** `--repli-lot` ; fusionnée avec `--fable --opus --argon --carbon` et `--rejuger-essai E3-T2-critique-croisee-D:1`.
3. `devis-reprise` lu comme indication, jamais comme condition.
4. À Lazar, avant le départ : Argon sans pensées et le niveau de réflexion (section 3.2) ; l'arrêt possible au code 4 (section 6) ; le coût non établi des refus de crédit (section 7).
5. `--repli-lot` : pas avant C-1, C-2, leur vérification par moi, et l'essai réel de la section 5.3.

## Limites

- Aucun appel réel. Le comportement d'un lot de Carbon à 65 536 jetons n'est pas connu ; mes sondes du lot reposent sur de faux fournisseurs.
- Les pages de Google lues ce jour ne sont pas versées ; celles sur la réflexion et les longues sorties décrivent une autre interface que `generateContent`, à laquelle je les étends par vraisemblance.
- La reprise est éprouvée sur des copies fabriquées depuis les journaux réels (textes factices de longueur réelle), pas sur les dossiers eux-mêmes ; `verifier` sur les vrais dossiers reste à faire par la session de reprise.
- La facturation d'Anthropic et de Google n'est lue sur aucune console.
- Mes outils sont dans mon bloc-notes, non durable : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/outils/test_sondes_cl_v7.py` (sondes), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/outils/test_sonde_s8.py` (tour III.3 une fois les critiques connues), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/outils/mutations_cl_v7.py` (mutations), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/outils/corrections_cl_v7.py` (C-1 à C-3 et leurs essais, appliqués sur copie), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/outils/test_temoin_reglage.py` (essai témoin) ; pages de Google : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/pages-lot/` et `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v7-fable/pages-reflexion/`.
