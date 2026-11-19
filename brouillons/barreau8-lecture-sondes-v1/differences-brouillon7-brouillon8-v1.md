# Différences entre le brouillon 7 et le brouillon 8 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 7 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md`, empreinte `8749b51816fca87987c3e163fd0b5e872164812f19287f102f95ad92c7fcf337`.
- Contre-lecture du brouillon 7 (Opus 5.5, contre-lecteur neuf) : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon7-v1.md`, empreinte `b62ec7795e8495ed693a3fd8dd2cdbb43219bfb73afb5d735e219d80dfd6194e` (vérifiée ; lue en entier).
- Brouillon 8 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon8.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T01:24Z et 2026-11-19T01:25Z (`date -u` ; mêmes heures que la ligne de date du brouillon 8), par programme, à partir du brouillon 7 : dix remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie aussi que les deux chaînes de la procédure de remplissage restent uniques et qu'il reste exactement deux marqueurs.

## Une ligne par remarque

| n° | objet | état | où, dans le brouillon 8 |
|---|---|---|---|
| M-1 (bloquante) | la règle de la dernière contre-lecture interdisait de verser l'entropie après elle | appliquée, textes de remplacement repris mot pour mot (deux remplacements) | liste d'arrêt, ligne 2 ; entrée « Contre-lecture 4 (finale, texte rempli) », « Règle » |
| M-2 (mineure) | garde d'alignement : fichier de configuration du jetoniseur absent | appliquée, mot pour mot | garde P3, clause (b) |
| M-3 (mineure) | passage (b-10) incomplet | appliquée, mot pour mot | bloc de décision « scores par jeton », liste du retour à (a) |
| M-4 (mineure) | le texte scellé dirait « il reste deux marqueurs ouverts » et « non scellé » | appliquée, mot pour mot (trois remplacements) | titre (« brouillon 8 ») ; statut ; phrase des marqueurs de la section « Champs ouverts » |

Remarques refusées ou adaptées : aucune.

## Changements hors remarque (trois, demandés par la conductrice ou de conséquence)

- Ligne de date : le brouillon 8 s'ajoute.
- Section « Contre-lecture » : entrée **« Contre-lecture 3 ter »** ajoutée avant l'entrée 4 (contre-lecture du brouillon 7 : empreintes du brouillon 7 et du rapport). Le motif du validateur (`src/controle_ia/prereg.py`, ligne 29, `^\s*-?\s*\**Contre-lecture (\d+)\**`) la reconnaît comme une entrée à part, contrôlée sur son propre segment, comme « 3 bis ».
- En-tête, auteur : « contre-lecteurs des brouillons 1, 3, 4, 6 et 7 ».

Rien d'autre ne change.

## Marqueurs restants et chaînes de la procédure de remplissage

Deux marqueurs, et deux seulement : F-3 (entropie racine des graines) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Les deux chaînes à remplacer au scellement paraissent chacune une seule fois dans le brouillon 8 : `À REMPLIR — À FIXER : tirée par la session mère au scellement` ; la ligne qui commence par `- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :` et finit par `versée avec l'empreinte du texte scellé.`

Sortie exacte du validateur sur le brouillon 8 : `['section vide ou à remplir : Contre-lecture']`.
