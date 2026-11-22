# Compte rendu de la course des renvois par l'interface (v1)

Course du 2026-11-22, 17:42Z à 18:20Z, sous GO-2026-11-22-103 (clé RR_ANTHROPIC_API_KEY_LUC, plafond 17,50 USD), programme renvois_api_v4.py. Aucune réponse lue : seules les métadonnées du journal sont rapportées.

| demande | modèle servi | fin | entrée / sortie (jetons) | coût réel (USD) | issue |
|---|---|---|---|---|---|
| passe X, groupe 2 | claude-opus-5-5 | end_turn | 3 000 / 76 948 | 1,550960 | rendue ; garde de coupure : 6 titres dans l'ordre, ligne finale présente, aucune section courte |
| exploration | claude-opus-5-5 | max_tokens | 963 / 96 000 | 1,923852 | défaut technique : texte coupé au plafond de sortie (faux échec, « non évaluable ») |
| exploration | claude-fable-5-1 | end_turn | 963 / 55 739 | 2,796580 | rendue (garde réduite : fin normale, texte non vide) |

- Coût réel des trois envois : 6,271392 USD, plus quelques jetons pour la garde de départ et l'essai d'effort (forfait de 0,05 USD retenu sur le plafond). Plafond restant : environ 11,18 USD.
- Aucun refus du classifieur : aucune question resserrée n'a été nécessaire.
- Effort xhigh admis pour les trois modèles à l'essai d'effort.
- Avant le départ, la v3 a refusé l'identifiant GO-2026-11-22-103, son motif n'admettant que deux chiffres en fin de numéro (0 USD) ; corrigé en v4, vérifié.
- Sorties versées sans lecture : branche prep/quarantaine-renvois-api-v1, commit 8f0bf585, empreintes des flux vérifiées. Elles ne se lisent que par un lecteur habilité.
