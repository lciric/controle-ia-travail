# Devis du collisionneur — « ce qui entre dans un programme amélioré et ambitieux, entraînement compris » (dossier 1) et « que faire de juges boîte noire muets » (dossier 2) — v1

- Pièce de classe A (devis), **non scellée comme accord : soumise à la mère, qui arbitre la clé Anthropic partagée, avant tout envoi**. Écrite le 24 novembre 2026 vers 11:25 UTC (`date -u`) par Claude Fable 5.2, effort maximal, session du protocole X. Aucun envoi n'a été fait ; aucune dépense.
- Accord de rattachement : `GO-2026-11-24-16` (« collisionneur sur devis arbitré par la mère »). Ce devis ne vaut pas accord de dépense.
- Programme chiffré : `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py` (sceau tenu, `420394f9…`), étage III seul (conception à l'aveugle, critique croisée, réponse), dans un dossier neuf.
- **Cloisonnement.** Le dossier 2 porte des chiffres de résultat de la base boîte noire par action. Ses textes d'entrée et ses sorties ne vont qu'à Lazar et à des lecteurs inscrits ; jamais à un concepteur de moniteur, de sonde ou de saboteur.

## 0. Résumé pour l'arbitrage

| | Dossier 1 (programme amélioré, entraînement compris) | Dossier 2 (juges muets) |
|---|---|---|
| Demandé par les mots de Lazar | oui, deux fois (« go […] collisionneur », « go collisionneur aussi ») | non : ses mots nomment Carbon et Fable seulement ; le mandat de la mère l'ajoute |
| Composition recommandée | Opus 5.5, Carbon, Neon | la même |
| Pire cas sans relance (fonction de devis du programme) | **15,90 USD** | **15,86 USD** |
| dont sur la clé Anthropic partagée | 4,12 USD | 4,09 USD |
| Attendu [repris d'un dossier voisin, non recalculé] | de 6 à 7,5 USD | de 6 à 7,5 USD |
| Plafond et ligne proposés (`--plafond-usd`, `--ligne-usd`) | **18 USD** | **18 USD** |
| Pire cas absolu, toutes relances épuisées (refusé avant l'envoi par le plafond) | 43,58 USD | 43,49 USD |

**Ce que je te demande d'arbitrer** : (1) lancer le dossier 1 seul, ou les deux ; (2) la part de la clé Anthropic `RR_ANTHROPIC_API_KEY` que tu me réserves (4,2 USD par dossier au pire sans relance ; 8,3 USD si chaque cellule d'Opus épuisait sa relance ; 1,7 USD attendu) ; (3) l'identifiant d'accord à citer au lancement ; (4) les options de la section 5.

**Ma recommandation** : dossier 1 maintenant, avec trois espèces ; dossier 2 seulement sur le mot de Lazar, parce que ses mots ne le demandent pas et que ses entrées portent des résultats.

## 1. Textes d'entrée

| Texte | Octets | Mots | Empreinte (début) | Garde de motifs du programme |
|---|---:|---:|---|---|
| `faits-neutres-demande-1-v3.md` | 10 263 | 1 603 | `c2b9327b…` | `[]` |
| `question-neutre-collisionneur-demande-1-v2.md` | 2 585 | 423 | `4494b200…` | `[]` |
| `faits-neutres-demande-2-v2.md` | 7 449 | 1 295 | `7807967d…` | `[]` |
| `question-neutre-collisionneur-demande-2-v2.md` | 2 515 | 407 | `d0670a94…` | `[]` |

Un témoin positif de la garde déclenche bien trois catégories. Deux sous-questions courtes pour l'organisme d'idéation sont écrites à part (`sous-question-organisme-demande-1-v2.md`, `-2-v2.md`) ; elles ne partent pas au collisionneur.

**Test de neutralité à l'aveugle** (lecteur neuf, Opus 5.5, qui n'a lu que les six textes ; rapport `test-neutralite-devinette-v1.md`, `70bad1df…` ; vérification des retouches par le même lecteur, `verification-neutralite-textes-v2-v1.md`). Seuil d'admission : score d'orientation strictement sous 0,50.

| Texte | Score des v1 | Score des v2 | Décision |
|---|---:|---:|---|
| Faits du dossier 1 | 0,40 | 0,30 | admis |
| Question du dossier 1 | 0,20 | 0,20 | admise |
| Sous-question 1 pour l'organisme | 0,30 | 0,25 | admise |
| Faits du dossier 2 | 0,38 | 0,28 | admis |
| Question du dossier 2 | 0,27 | 0,22 | admise |
| Sous-question 2 pour l'organisme | 0,34 | 0,25 | admise |

Le lecteur avait demandé trois retouches (un dossier 1 qui laissait deviner une thèse par trois manques alignés et penchait contre la détection ; un titre inexact et un choix à deux causes dans le dossier 2 ; la phrase d'ouverture de la question 2) : elles sont portées dans les v2, qu'il juge fidèles, « aucune retouche ne bloque l'envoi ». Il gardait deux retouches souhaitables sur les faits du dossier 1 (rétablir la ligne générale sur la tenue des saboteurs à l'entraînement ; dire aussi, au fait sur l'audit, qu'un juge durci résiste) : elles sont portées dans la v3 de ce seul fichier, dans ses mots, sans nouvelle vérification. La garde de motifs est vide sur la v3 et sur son assemblage avec la question.

## 2. Composition et réglages

Trois espèces de deux familles, selon la règle d'économie appliquée aux dossiers récents : **Opus 5.5** (Anthropic), **Carbon** et **Neon** (Google). Argon n'est pas activé. Fable 5.2 n'est pas activé : il répond déjà à part, et son quota est réservé aux pièces décisives. Aucune clé d'OpenAI, de Mistral ni de Kimi n'est présente dans ce conteneur : Astra, Mistral et Kimi sont hors de portée ici.

Réglages lus dans la sortie de la fonction de devis, sans réseau :

| Lettre | Espèce | Prix (entrée / sortie, USD par million) | Plafond de sortie | Réflexion | Délai |
|---|---|---|---:|---|---:|
| A | Opus 5.5 (`claude-opus-5-5`) | 4 / 20 | 64 000 | effort « high » | 3 600 s |
| B | Carbon (`gemini-4-carbon`) | 4 / 20 | 65 536 | niveau « high », provision 49 152, soit 16 384 jetons de texte | 5 400 s |
| C | Neon (`gemini-4-neon`) | 3 / 15 | 65 536 | niveau « xhigh », provision 32 768 | 5 400 s |

Règle des appels à Google : réflexion explicite, au moins 16 000 jetons de texte au-delà de la réflexion ; limites de mots des tours (3 500, 3 000, 3 500) : 3 500 × 4,2 = 14 700 jetons pour Carbon, sous 16 384. Le programme porte la garde commune ; un arrêt en `MAX_TOKENS` sans texte y est un défaut de réglage, jamais une réponse.

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
| dont clé Anthropic (Opus) | | 4,12 | 4,09 |
| dont clés Google | | 11,78 | 11,77 |

- **Avec relances** : une cellule de Google peut être relancée deux fois, une cellule d'Anthropic une fois. Pire cas absolu : 11,78 × 3 + 4,12 × 2 = 43,58 USD pour le dossier 1. Le plafond de 18 USD le refuse avant l'envoi : au-delà, le run s'arrête et revient vers toi.
- **Attendu.** Le devis d'un dossier voisin de même forme (trois mêmes espèces, étage III seul, textes un peu plus courts) donne, sur des médianes mesurées aux journaux, 6,0 USD hors pannes et 7,3 USD pannes comprises, dont 1,7 USD sur la clé Anthropic. Je reprends ces chiffres sans les recalculer : mes textes sont plus longs d'environ 5 000 caractères, ce qui ajoute quelques centimes.
- **Si Fable était ajouté** (quatre espèces, douze cellules) : 24,31 USD au pire sans relance pour le dossier 1, dont 12,39 USD sur la clé Anthropic.

## 4. Commandes (rien n'est lancé sans ton mot)

```
cd /home/user/controle-ia-travail
PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier docs/notes/collisionneur-v9/collisionneur_v9_v8m.py
# dossier 1
GO_ID=<accord donné par la mère> PYTHONPATH=src .venv/bin/python -B docs/notes/collisionneur-v9/collisionneur_v9_v8m.py etage3 \
  --opus --carbon --neon --cle-anthropic RR_ANTHROPIC_API_KEY \
  --faits docs/notes/protocole-x-entrainement-et-juges-v1/faits-neutres-demande-1-v3.md \
  --question docs/notes/protocole-x-entrainement-et-juges-v1/question-neutre-collisionneur-demande-1-v2.md \
  --sortie runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-<horodatage> \
  --plafond-usd 18 --ligne-usd 18
# puis : … verifier runs/collisionneur-protocole-x-programme-ameliore-entrainement-v1-<horodatage>
```
Le dossier 2, s'il est accordé, se lance de même avec ses deux textes et un dossier de sortie à son nom. Durée : d'une à trois heures par dossier [supposé]. Les deux dossiers peuvent tourner l'un après l'autre ; je ne les lance pas ensemble, pour ne pas doubler la pointe sur la clé partagée.

## 5. Options

1. **Bras témoin apparié** (une question plus pauvre encore, sur les mêmes faits, pour mesurer ce que le cadrage de la question apporte) : il double la dépense du dossier (15,9 USD de plus au pire). Les dossiers récents l'ont joué sous la règle d'économie ; je n'ai pas trouvé le texte de cette règle sur la branche principale et ne l'ai donc pas relu. Je ne le recommande pas ici ; si tu le veux, j'écris la question témoin et la fais passer au même test avant l'envoi.
2. **Fable dans la composition** : non recommandé (section 3).
3. **Dossier 2** : sur le mot de Lazar seulement.
4. **Note de sortie** : chaque dossier lancé rend sa note en Markdown et en PDF (ce que chaque modèle propose, accords, désaccords, neuf ou fragile, références à vérifier, propositions retenues), versée dans la note de fin de dossier du protocole X.

## 6. Risques et gardes

- Coupures de flux chez Google : observées sur des dossiers voisins ; chaque coupure coûte au plus le pire cas de sa cellule. Le plafond borne le tout.
- Clé Anthropic partagée : si un autre collisionneur consomme en même temps, le plafond de la clé (90 USD comptés, selon ton registre) peut être atteint ; d'où ton arbitrage.
- Une panne technique n'est pas un résultat : un dossier arrêté pour cause technique a droit à une relance sur le même accord, par décision nommée.
- Ce que ce devis ne couvre pas : l'étage I et l'étage II du collisionneur ; le service à l'organisme d'idéation ; toute lecture en entier des références que les modèles citeront.

## 7. Ce que je n'ai pas fait

- Je n'ai pas recalculé l'attendu sur les journaux mesurés : il est repris du devis voisin.
- Je n'ai pas relu le texte de la règle d'économie des collisionneurs (absent de la branche principale à ma lecture).
- Ce devis n'est pas encore contre-lu : la contre-lecture par un autre modèle, puis la vérification de ses corrections, précèdent tout envoi (classe A).
