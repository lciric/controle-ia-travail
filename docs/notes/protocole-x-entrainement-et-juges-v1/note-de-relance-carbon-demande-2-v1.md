# Note de relance de l'appel à Carbon sur la demande 2 (juges qui n'alertent pas) — v1

Écrite le 2026-11-24T12:10:46Z (`date -u`), avant la relance, par la session du protocole X. Classe C.

## Accord

`GO-2026-11-24-21`, lu ce jour au registre des accords de la branche principale (commit `741b4df8`, ligne 899, R-5273), point 4 : « une relance de l'appel à Carbon sur la demande 2 du protocole X, plafond porté à 9 USD ». Message de la mère reçu à 12:09:48Z : une seule relance ; si elle est coupée encore, arrêt, sans autre relance.

## Risque connu, dit avant l'envoi

Deux envois à Carbon sur trois ont été coupés aujourd'hui depuis ce conteneur, à 300 et 301 secondes de silence, avant tout octet de réponse (`diagnostic-coupures-carbon-cinq-minutes-v1.md`, `d87c7f0a…`). Cette relance a de l'ordre d'une chance sur deux d'être coupée de la même façon. Une coupure est comptée au pire : 2,78 USD.

## Ce qui part

- Le même script (`appel_carbon_protocole_x_v3.py`, `2a24a4b1…`), la même invite (`invite-carbon-demande-2-v2.md`, empreinte `ba44084aed9ec945f760677a3d76bf310845e7a39547932f627c35ae58189a1e`), les mêmes réglages. L'invite porte des chiffres du verdict de la base boîte noire par action : envoi au service de Google sur le mot du directeur.
- Le verrou du premier essai (`tentative-carbon-demande-2-v1.verrou`) est levé par cette décision nommée : son contenu est gardé dans `tentative-carbon-demande-2-essai-1-coupe-verrou-archive-v1.txt`, et le fichier d'origine est retiré pour que le script accepte l'envoi. Le journal du premier essai reste dans l'historique de la branche (commit `7fe6e48a`) ; le script y ajoute ses lignes.

## Compte des appels directs

Demande 1 : 1,67 USD réels. Demande 2, premier essai coupé : de 0 à 2,78 USD, inconnu. Cette relance : 2,78 USD au pire. Total au pire : 7,22 USD, sous le plafond de 9 USD.
