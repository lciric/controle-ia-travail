# Préparation du tour du collisionneur et de l'appel d'Argon à part — bisociation à deux espaces — v1

Session-depot (sous-agent de préparation), 2026-10-29 23:09 UTC. **Rien n'a été lancé** : aucun appel aux API, ni de contrôle ni de tour.

## Pièces et empreintes (toutes vérifiées)
| Fichier | Empreinte | Origine |
|---|---|---|
| question-bisociation-deux-espaces-v1.md | 73a30ab727445969… | origin/canal/conv-audit-n04, n° 217 (attendue 73a30ab7…) |
| faits-bisociation-v1.md | 0045b0384256a3a3… | assemblé ici : glossaire + pièces A à D mot pour mot |
| collisionneur_v3.py | 0c6e3fb6b6758138… | origin/donnees/collisionneur-question-mere-v2 (identique au run du 29 octobre) |
| appel_controle_v6.py | d7e6394954ea3ae1… | dossier du run du 29 octobre (absent de la branche ; 11 copies identiques dans le scratchpad) |
| lancer-tour-bisociation-v1.sh | bc60115ebf610078… | écrit ici |
| lancer-argon-bisociation-v1.sh | 3c2ce5d1d885759d… | écrit ici |

Pièces servies dans les faits (branche de conv-audit, dossier `pole-scientifique-automatique-v1/`) :
- A `orchestrateur-pole-v7/pole/recombinaison.py` `71faad38…`, égale à la ligne de `EMPREINTES-orchestrateur-pole-v7-v47.txt` (`f232c2e2…`) ; entier, 329 lignes.
- B `trancher-recombinaison/trancher-recombinaison-v1.md` `72cff8a0…` ; entier, 276 lignes ; préenregistrement cité par empreinte `5335614b…` (celle que donne la question).
- C `question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v1.md` `f89e0791…`, lignes 22 à 31 (préambule).
- D `conception-pole-scientifique-v1.md` `a4f94148…`, lignes 29 à 33 (point 5 de la section 1).
- Taille des faits : 46 822 caractères, ≈ 11 700 jetons. Aucun vocabulaire d'attaque, aucune fiche réelle, aucun mode, aucune carte des hypothèses.

## Réserves
1. **Pièce D** : la question décrit le « § 5 » comme portant aussi sur la « mémoire qui refuse les redites » et l'« héritage récompensé » ; ces notions ne figurent pas dans le fichier (une seule version, identique aux copies des lots). Le point 5 est servi seul ; la réserve est écrite dans les faits.
2. **Consignes de l'étage III** : aucune n'emploie « évasion » ni « attaque » (B1 : « tu les critiques »). E3-T1 (c) est taillée pour un instrument de détection (« taux de détection et de fausses alertes, sur quels cas honnêtes appariés, contre quelles vérifications mécaniques à battre ») : pour un opérateur de recombinaison, elle se lit « mesure minimale qui dit si l'opérateur fonctionne » ; adaptée de biais, pas bloquante. Les cellules du tour 2 gardent le nom de fichier « redteam » (nom technique de `TOURS`) : cosmétique.
3. **Python** : `collisionneur_v3.py` importe `anthropic` (l. 388) ; `/usr/bin/python3` ne l'a pas. Le lanceur prend le venv survivant `scratchpad/collisionneur-priorites/venv` (anthropic 2.3.0, vérifié) et s'arrête s'il manque.
4. **Argon** : le relais Gemini local v1 est mort avec l'ancien conteneur ; le lanceur le relance lui-même (clé par variable sous `env -i`, 4 appels au plus) et l'arrête par son PID. Enveloppe et commande installées vérifiées (`24d5d16c…`, `6905ac71…`). Argon reçoit la consigne seule (sans les pièces A à D, conformément au n° 217).
5. Modèle A = claude-fable-5-1 par l'API (clé RR_ANTHROPIC_API_KEY_3) : la limite d'usage Fable de Claude Code ne s'applique pas à cette clé, mais un refus ou un 429 arrête le tour (code 5), sans repli.

## Devis
- Tour (étage III, devis hors ligne du script, sans réseau) : **20,59 USD au pire cas sans relance** (A 10,58 ; B 4,24 ; C 5,78). Le run comparable du 29 octobre (faits trois fois plus longs) a coûté 10,01 USD : attendu ≈ 6 à 10 USD.
- Appel de contrôle : ≈ 0,002 USD.
- Argon à part : pire cas garanti par la commande ≈ 1,68 USD ; réel du 29 octobre 0,81 à 1,15 USD.
- **Plafonds proposés** : tour **25 USD** (`--plafond-usd 25`) ; Argon **3 USD** (`PLAFOND_SESSION_USD=3`) ; total **28 USD**, dans l'enveloppe « 20 à 30 USD » de R-514.

## Commandes exactes (depuis la racine du dépôt, en root)
```
bash donnees/collisionneur-bisociation-v1/lancer-tour-bisociation-v1.sh > donnees/collisionneur-bisociation-v1/journal-tour-bisociation-v1.log 2>&1
sh donnees/collisionneur-bisociation-v1/lancer-argon-bisociation-v1.sh
```
(les deux peuvent tourner en parallèle ; les clés sont lues dans l'environnement de la session par nom de variable.)

## Ligne de GO proposée (`registres/go.md`, 8 colonnes ; à inscrire par la session)
`| GO-2026-10-29-20 | 2026-10-29 | calcul | **collisionneur (étage III, trois modèles) et Argon à part sur la question « recombinaison bisociative à deux espaces »** (conv-audit n° 217, \`73a30ab7…\`) : tour plafonné à 25 USD, Argon à 3 USD ; devis hors ligne 20,59 USD au pire cas pour le tour, ≈ 1,68 USD pour Argon ; sous GO-2026-10-29-19 (GO anticipé renouvelé, dépassements compris) ; dépense demandée par Lazar (mot direct relayé par conv-audit, R-514 : « collisionneur + Argon sur la bisociation ≈ 20 à 30 USD » go) | 28 USD | 2026-10-30 | Lazar | mot direct de Lazar dans la session « session-depot », 29 octobre 2026, ≈ 22:30 UTC, verbatim : « je renouvelle mon GO poiur toutes les depenses y compir sles depassements » (GO-2026-10-29-19) ; objet de la dépense : mot de Lazar relayé par conv-audit (R-514, 23:41 heure de Paris) |`
