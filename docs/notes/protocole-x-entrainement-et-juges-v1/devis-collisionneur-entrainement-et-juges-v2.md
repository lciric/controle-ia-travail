# Devis du collisionneur — « ce qui entre dans un programme amélioré et ambitieux, entraînement compris » (dossier 1) et « que faire de juges boîte noire qui n'alertent pas » (dossier 2) — v2

- Pièce de classe A (devis). **Elle ne vaut pas accord de dépense : elle est soumise à la mère, qui arbitre la clé Anthropic partagée, avant tout envoi.** Écrite le 24 novembre 2026 vers 11:38 UTC (`date -u`) par Claude Fable 5.2, effort maximal, session du protocole X. Aucun envoi n'a été fait ; aucune dépense.
- Remplace la v1 (brouillon, gardée). Porte les huit constats de la contre-lecture (`contre-lecture-devis-collisionneur-v1.md`, `0cf33fa1…`, Opus 5.5, sous-agent neuf : « tient après corrections », aucun bloquant). Table des corrections en section 8.
- Accord de rattachement : `GO-2026-11-24-16` (« collisionneur sur devis arbitré par la mère » ; aucun montant n'y est accordé au collisionneur).
- Programme chiffré : `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py` (sceau tenu, `420394f9…`), étage III seul (conception à l'aveugle, critique croisée, réponse), dans un dossier neuf.
- **Cloisonnement.** Le dossier 2 porte des chiffres de résultat de la base boîte noire par action. Ses textes d'entrée et ses sorties ne vont qu'à Lazar et à des lecteurs inscrits ; jamais à un concepteur de moniteur, de sonde ou de saboteur.

## 0. Résumé pour l'arbitrage

| | Dossier 1 (programme amélioré, entraînement compris) | Dossier 2 (juges qui n'alertent pas) |
|---|---|---|
| Demandé par les mots de Lazar | oui, deux fois (voir le choix 1 ci-dessous) | non : ses mots nomment « carbon fable » ; le mandat de la mère l'ajoute |
| Composition recommandée | Opus 5.5, Carbon, Neon | la même |
| Pire cas sans relance (fonction de devis du programme) | **15,90 USD** | **15,86 USD** |
| dont cellules d'Opus, sur la clé Anthropic partagée | 4,1 USD | 4,1 USD |
| Attendu [repris d'un dossier voisin, non recalculé] | de 6,0 à 7,3 USD, dont 1,7 sur la clé Anthropic | de 6,0 à 7,3 USD |
| Plafond et ligne proposés (`--plafond-usd`, `--ligne-usd`) | **18 USD** | **18 USD** |
| Pire cas absolu, toutes relances épuisées | 43,58 USD : refusé avant l'envoi par la ligne | 43,48 USD : de même |
| Durée | d'une à trois heures [supposé] ; au pire 12 heures | de même |

**Ce que je te demande d'arbitrer.**
1. **Un dossier ou deux pour la demande 1.** Lazar a écrit deux fois « collisionneur » : « go carbon et fable et collisionneur sur ce qu'il faudrait faire » (l'entraînement), puis « go collisionneur aussi pour déterminer ce qui entre dans un programme amélioré ambitieux ». Ton mandat les fond en une question, « ce qui entre dans un programme amélioré et ambitieux, entraînement compris », et la question neutre écrite couvre les deux (son point 3 compare détecter, auditer et entraîner ; ses points 4 et 7 comparent des programmes). **Cette fusion est un choix, à confirmer.** Deux dossiers séparés doubleraient la dépense.
2. **Dossier 1 seul, ou les deux.**
3. **La part de la clé Anthropic `RR_ANTHROPIC_API_KEY`.** Le programme ne borne pas la dépense par clé : seule la ligne de 18 USD du dossier borne le tout. Repères pour les cellules d'Opus : 1,7 USD attendu ; 4,1 USD au pire sans relance ; 8,2 USD si chaque cellule d'Opus épuisait sa relance dans une même commande.
4. **L'identifiant d'accord** à consigner au registre et au journal de la course.
5. **La ligne** : 18 USD, ou 21 USD (section 3).

**Ma recommandation** : un seul dossier pour la demande 1, lancé maintenant, trois espèces, ligne de 18 USD ; le dossier 2 seulement sur le mot de Lazar, parce que ses mots ne le demandent pas et que ses entrées portent des résultats.

## 1. Textes d'entrée

| Texte | Octets | Mots | Empreinte (début) | Garde de motifs du programme |
|---|---:|---:|---|---|
| `faits-neutres-demande-1-v3.md` | 10 263 | 1 603 | `c2b9327b…` | `[]` |
| `question-neutre-collisionneur-demande-1-v2.md` | 2 585 | 423 | `4494b200…` | `[]` |
| `faits-neutres-demande-2-v2.md` | 7 449 | 1 295 | `7807967d…` | `[]` |
| `question-neutre-collisionneur-demande-2-v2.md` | 2 515 | 407 | `d0670a94…` | `[]` |

Un témoin positif de la garde déclenche bien trois catégories. Deux sous-questions courtes pour l'organisme d'idéation sont écrites à part (`sous-question-organisme-demande-1-v2.md`, `-2-v2.md`) ; elles ne partent pas au collisionneur.

**Test de neutralité à l'aveugle** (lecteur neuf, Opus 5.5, qui n'a lu que les six textes ; rapport `test-neutralite-devinette-v1.md`, `70bad1df…` ; vérification des retouches par le même lecteur, `verification-neutralite-textes-v2-v1.md`, `c58b7e6e…`). Seuil d'admission : score d'orientation strictement sous 0,50.

| Texte | Score des v1 | Score des v2 | Décision |
|---|---:|---:|---|
| Faits du dossier 1 | 0,40 | 0,30 | admis |
| Question du dossier 1 | 0,20 | 0,20 | admise |
| Sous-question 1 pour l'organisme | 0,30 | 0,25 | admise |
| Faits du dossier 2 | 0,38 | 0,28 | admis |
| Question du dossier 2 | 0,27 | 0,22 | admise |
| Sous-question 2 pour l'organisme | 0,34 | 0,25 | admise |

Le lecteur avait demandé trois retouches ; elles sont portées dans les v2, sur lesquelles il écrit : « Aucune retouche bloquante. Deux souhaitables : rétablir la ligne sur la tenue des saboteurs ; compléter le fait sur l'audit. » Ces deux retouches sont portées dans la v3 des faits du dossier 1, dans ses mots, sans nouvelle vérification. La garde de motifs est vide sur la v3 et sur son assemblage avec la question.

## 2. Composition et réglages

Trois espèces de deux familles, selon la règle d'économie appliquée aux dossiers récents : **Opus 5.5** (Anthropic), **Carbon** et **Neon** (Google). Argon n'est pas activé. Fable 5.2 n'est pas activé : il répond déjà à part, et son quota est réservé aux pièces décisives. Aucune clé d'OpenAI, de Mistral ni de Kimi n'est présente dans ce conteneur.

Réglages lus dans la sortie de la fonction de devis, sans réseau :

| Lettre | Espèce | Prix (entrée / sortie, USD par million) | Plafond de sortie | Réflexion | Délai par envoi |
|---|---|---|---:|---|---:|
| A | Opus 5.5 (`claude-opus-5-5`) | 4 / 20 | 64 000 | effort « high » | 3 600 s |
| B | Carbon (`gemini-4-carbon`) | 4 / 20 | 65 536 | niveau « high » ; provision de 49 152 comptée par la garde, non envoyée | 5 400 s |
| C | Neon (`gemini-4-neon`) | 3 / 15 | 65 536 | niveau « xhigh » ; provision de 32 768 comptée, non envoyée | 5 400 s |

Règle des appels à Google : réflexion explicite ; au moins 16 000 jetons de texte au-delà de la réflexion (Carbon : 65 536 − 49 152 = 16 384 ; Neon : 32 768) ; la limite de mots des tours (3 500, 3 000, 3 500) tient dans le texte : 3 500 × 4,2 = 14 700 < 16 384 pour Carbon ; 3 500 × 5,1 = 17 850 < 32 768 pour Neon. Le programme porte la garde commune ; un arrêt en `MAX_TOKENS` sans texte y est un défaut de réglage, jamais une réponse.

## 3. Chiffrage, cellule par cellule (pire cas sans relance, sortie de la fonction de devis)

| Cellule | Espèce | Dossier 1 | Dossier 2 |
|---|---|---:|---:|
| Tour III.1, conception | Opus 5.5 | 1,31 | 1,30 |
| | Carbon | 2,32 | 2,32 |
| | Neon | 1,50 | 1,49 |
| Tour III.2, critique croisée | Opus 5.5 | 1,38 | 1,37 |
| | Carbon | 2,39 | 2,39 |
| | Neon | 1,55 | 1,54 |
| Tour III.3, réponse | Opus 5.5 | 1,43 | 1,42 |
| | Carbon | 2,44 | 2,44 |
| | Neon | 1,58 | 1,58 |
| **Total, neuf cellules** | | **15,90** | **15,86** |
| dont cellules d'Opus (clé Anthropic) | | 4,1 | 4,1 |
| dont cellules de Google | | 11,8 | 11,8 |

- **Attendu.** Le devis d'un dossier voisin de même forme (trois mêmes espèces, étage III seul) donne, sur des médianes mesurées aux journaux, 6,0 USD hors pannes et 7,3 USD pannes comprises, dont 1,7 USD pour Opus. Je reprends ces chiffres sans les recalculer ; mes textes sont plus longs d'environ 5 000 caractères, ce qui ajoute quelques centimes.
- **Relances permises par le programme, dans une même commande** : deux pour une cellule de Google (relance identique, puis dernier recours à un niveau de réflexion plus bas, déclaré au journal), une pour une cellule d'Opus. Pire cas absolu : 11,78 × 3 + 4,12 × 2 = 43,58 USD pour le dossier 1.
- **Ce que fait la ligne de 18 USD.** Avant chaque envoi, le programme refuse si la dépense comptée plus le pire cas de l'essai suivant dépasse la ligne. **Ce refus peut tomber à n'importe quelle cellule** (code 4, rien n'est envoyé) : le dossier reste alors incomplet, et ce qui est payé ne donne pas de résultat tant qu'il n'est pas repris. Au pire strict, la marge est de 2,10 USD : une relance d'Opus ou de Neon passe, jamais une de Carbon. Aux coûts attendus, plusieurs relances passent.
- **Pour finir un dossier refusé par la ligne**, il faut une ligne de reprise : `--ligne-reprise-usd MONTANT --go-ligne GO-…`, sur un accord nommé, avec un plafond relevé. Je ne l'ouvre pas seule : je m'arrête, je te rends compte, et je te demande cette ligne.
- **Option d'une ligne de 21 USD.** Elle couvre, même au pire strict, une cellule de Carbon coupée puis renvoyée, et une relance d'Opus ou de Neon (15,90 + 2,44 + 1,58 = 19,92). Je recommande 18 USD : le pire strict suppose que chaque cellule épuise son plafond de sortie, ce que les journaux voisins ne montrent pas.
- **Si Fable était ajouté** (quatre espèces, douze cellules) : 24,31 USD au pire sans relance pour le dossier 1, dont 12,4 USD sur la clé Anthropic. Non recommandé.

## 4. Commandes (rien n'est lancé sans ton mot)

```
cd /home/user/controle-ia-travail
PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier docs/notes/collisionneur-v9/collisionneur_v9_v8m.py
# dossier 1
PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py etage3 \
  --opus --carbon --neon --cle-anthropic RR_ANTHROPIC_API_KEY \
  --faits docs/notes/protocole-x-entrainement-et-juges-v1/faits-neutres-demande-1-v3.md \
  --question docs/notes/protocole-x-entrainement-et-juges-v1/question-neutre-collisionneur-demande-1-v2.md \
  --sortie runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-<horodatage> \
  --plafond-usd 18 --ligne-usd 18
# puis :
PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py verifier \
  runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-<horodatage>
```

- Ni le programme ni le crochet de garde ne lisent de variable d'accord : l'accord que tu donnes est consigné par moi dans une note de lancement scellée dans le dossier de la course, et par toi au registre.
- Le dossier 2, s'il est accordé, se lance de même avec ses deux textes et un dossier de sortie à son nom. Les deux dossiers tournent l'un après l'autre, jamais ensemble, pour ne pas doubler la pointe sur la clé partagée.
- **Durée.** Les neuf cellules partent l'une après l'autre. D'une à trois heures par dossier [supposé]. Au pire, si chaque envoi allait au bout de son délai : 3 600 + 5 400 + 5 400 = 14 400 s par tour, soit 12 heures pour trois tours, sans relance.

## 5. Ce qui suit la course

- **Note de sortie, obligatoire** (règle « Notes des collisionneurs ») : pour chaque dossier lancé, une note en Markdown et en PDF sur ce que chaque modèle propose, les accords et les désaccords, ce qui est neuf ou fragile, les références à vérifier, les propositions retenues et pourquoi. Le programme ne la produit pas. **Rédacteur** : un sous-agent Opus 5.5 de cette session (règle d'économie de Fable : une synthèse n'est pas une pièce décisive), relu par moi, puis versé dans la note de fin de dossier du protocole X. **Coût** : aucune dépense d'interface ; du quota de session. Pour le dossier 2, le rédacteur est inscrit sur la liste « qui a lu quoi » avant toute lecture. Si cette session est finie avant la fin de la course, la note revient à la session qui reprend, sur la passation.
- **Options non recommandées** : un bras témoin apparié (une question plus pauvre sur les mêmes faits ; il double la dépense ; je n'ai pas trouvé le texte de la règle qui l'a fait jouer sur des dossiers récents et ne l'ai donc pas relu) ; Fable dans la composition.

## 6. Pannes, et ce que je fais dans chaque cas

| Cas | Ce que fait le programme | Ce que je fais |
|---|---|---|
| Envoi coupé en cours de flux, ou délai dépassé | La commande s'arrête (code 5) ; la cellule est comptée à son pire cas ; aucun renvoi dans la commande | Je te rends compte. La même commande relancée renvoie la cellule ; je ne la relance que sur ta décision nommée |
| Réponse vide ou coupée par le plafond | Relances de la section 3, dans la commande | Rien à décider |
| Cellule non valide après ses relances | La porte du tour se ferme (code 2) ; le tour suivant ne part pas | Je te rends compte ; le dossier est incomplet |
| Refus par la ligne | Code 4, rien n'est envoyé | Je te demande une ligne de reprise |

- **Carbon est la cellule à risque.** Les journaux voisins montrent des coupures de flux chez Carbon (environ une sur huit [repris, non recompté]). Ce matin, l'un de mes deux appels directs à Carbon a été coupé après cinq minutes, avant tout en-tête. Le repli par l'interface de lot (`--repli-lot`) est refusé à Carbon par le programme, sa provision de réflexion dépassant la limite de l'appel non diffusé. Avec trois cellules de Carbon, la chance d'au moins une coupure est d'environ une sur trois [calcul sur le taux repris].
- **Où part une relance « sur le même accord ».** Dans le **même dossier**, sur le reste de la ligne de 18 USD : la même commande reprend à la cellule manquante. Si la ligne ne suffit plus, par une ligne de reprise nommée. Jamais dans un dossier neuf, qui rejouerait les cellules déjà payées.
- **Clé Anthropic partagée.** Si un autre collisionneur consomme en même temps, son propre plafond peut être atteint plus tôt ; je ne connais pas l'état de cette clé, d'où ton arbitrage.
- **Ce que ce devis ne couvre pas** : l'étage I et l'étage II du collisionneur ; le service à l'organisme d'idéation ; toute lecture en entier des références que les modèles citeront.

## 7. Ce que je n'ai pas fait

- Je n'ai pas recalculé l'attendu ni le taux de coupure sur les journaux mesurés : ils sont repris du devis voisin.
- Je n'ai pas relu le texte de la règle d'économie des collisionneurs (absent de la branche principale à ma lecture).
- Le dossier 2 n'a été contre-lu que par programme (chiffres, empreintes, garde), son contre-lecteur n'étant pas inscrit pour en lire les textes.

## 8. Table des corrections depuis la v1

| Constat de la contre-lecture | Correction |
|---|---|
| 1. La part d'Anthropic n'est bornée par rien d'autre que la ligne du dossier ; 4,11 × 2 = 8,2 | § 0, point 3 |
| 2. Le refus par la ligne peut tomber à toute cellule ; marge de 2,10 USD au pire strict ; reprise par ligne nommée | § 3 |
| 3. Coupure : arrêt sans renvoi ; porte du tour ; repli par lot refusé à Carbon ; dernier recours à niveau plus bas ; où part la relance | § 3 et § 6 |
| 4. Note de sortie obligatoire, rédacteur et coût | § 5 |
| 5. Deux demandes de collisionneur fondues en un dossier : choix à confirmer | § 0, point 1 |
| 6. Durée au pire : 12 heures | § 0 et § 4 |
| 7. Arrondis (4,1 ; 11,8 ; 43,48 ; 12,4 ; « de 6,0 à 7,3 ») | § 0 et § 3 |
| 8. Variable d'accord non lue ; commande de vérification ; citation exacte du vérificateur ; calcul de Neon ; provision comptée, non envoyée ; « 90 USD » sans source, retiré | § 1, § 2, § 4, § 6 |
