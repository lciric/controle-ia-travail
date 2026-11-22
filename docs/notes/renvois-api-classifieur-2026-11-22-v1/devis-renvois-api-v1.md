# Devis — renvois par l'interface des trois demandes arrêtées par le classifieur (v1)

Pièce de classe A (devis). Écrite par la session des renvois (session_013QMayj5YDSrZN5yVG1XgG2) le 2026-11-22, sans aucun appel payant. Mots de Lazar : GO-2026-11-22-90, GO-2026-11-22-96 (« go » sur devis ; la dépense attend la ligne chiffrée).

## Les trois demandes
| demande | modèle | texte servi (scellé, branche lot/compte-organisme-v1) | effort | sortie au plus |
|---|---|---|---|---|
| passe X, groupe 2 | claude-opus-5-5 | passe-x-textes-groupes-v1/textes/groupe-2.md (fc9bed7f…, 7 495 octets) | xhigh, réflexion adaptative | 96 000 jetons |
| exploration et allumage | claude-opus-5-5 | question-neutre-exploration-et-allumage-servie-v1.md (2bf01492…, 2 489 octets) | xhigh, réflexion adaptative | 96 000 jetons |
| exploration et allumage | claude-fable-5-1 (jamais un autre modèle en repli) | même texte (2bf01492…) | xhigh, réflexion adaptative | 96 000 jetons |

Réglages repris de la configuration vérifiée de la passe X (configuration-passe-x-groupes-v4.json : tarifs, effort xhigh pour les modèles 5.x, sortie 96 000). Le groupe 2 n'a jamais été envoyé par l'interface (arrêt à la barrière, 13:55:34Z, SIGKILL avant tout envoi des groupes 2 et 3).

## Chiffrage au pire (entrée bornée par les octets, comme l'outil de la passe X)
| demande | entrée au plus | prix entrée / sortie (USD par million) | pire |
|---|---|---|---|
| passe X groupe 2, Opus 5.5 | 8 007 | 4 / 20 | 1,952 |
| exploration, Opus 5.5 | 3 000 | 4 / 20 | 1,932 |
| exploration, Fable 5.1 | 3 000 | 10 / 50 | 4,830 |
| premier envoi, total | | | 8,714 |
| un seul renvoi resserré par demande, au plus, même plafond | | | 8,714 |
| **plafond total demandé** | | | **17,50 USD** |

Attendu réaliste : Opus 5.5 groupe 1 a coûté 1,19 USD par l'interface ; premier envoi vers 5 à 6 USD.

## Règles d'envoi
- Clé lue par son nom seulement. Recommandation : `RR_ANTHROPIC_API_KEY_LUC` (sous-part Anthropic de la passe X) si son solde lu à la console couvre 17,50 USD ; sinon la clé que Lazar nomme (`RR_ANTHROPIC_API_KEY_RIGAUD`, `_MINUIT`, `_2`, `_3` présentes dans l'environnement). Lazar choisit.
- Code : réemploi du code vérifié de la passe X (passe_x_na_v4.py) ou de la mini-passe (mini_passe_v2.py) sur une configuration neuve réduite à ces trois envois ; contre-lecture de la configuration par un autre modèle (classe B) avant envoi.
- Sorties versées sans lecture sur des branches de quarantaine neuves (prep/quarantaine-…-api-v1), comme les précédentes.
- Refus (fin « refusal » ou classe « refus du modèle ») : aucun repli vers un autre modèle ; question resserrée à un niveau purement technique, écrite par Fable 5.2 par l'abonnement (limite levée vers 18:00Z), sinon par Opus et marquée « à revoir par Fable » ; test de neutralité ; renvoi une seule fois sous le même plafond. Second refus : arrêt, nœud à la mère.
- Risque connu : Fable 5.1 a déjà refusé le groupe 1 par l'interface (13:05Z, 0,027 USD) ; Opus 5.5 a refusé par l'abonnement (« reasoning_extraction »). Un refus coûte quelques centimes.
