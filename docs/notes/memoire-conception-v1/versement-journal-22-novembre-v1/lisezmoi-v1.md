# Candidats au journal des idées — versement du 22 novembre sur main (v1)

Classe C (travail), sans dépense, sans modèle externe. Écrit le 22 novembre 2026 par un agent Opus 5.5, sur mandat de la session bibliothécaire. Le journal lui-même n'est pas touché : la veille de cap importe, numérote et tranche.

## Méthode

- Périmètre : les fichiers de `docs/notes/index-pistes-v1/liste-fichiers-verses-v1.tsv` (hors `.sha256`), dans les dossiers du mandat ; `memoire-conception-v1` et `veille-de-cap-v1` exclus (déjà au journal).
- Gisement : un par lot cohérent (sous-dossier, chantier ou série de demandes). Chemin représentatif : synthèse, LISEZMOI, note ou premier `.md` ; extrait = le titre ou une ligne d'en-tête. `nb_fichiers` = fichiers du lot dans la liste, hors `.sha256`. `depouille` dit si une synthèse ou une note nomme les idées retenues (« source » = le chemin cité).
- Idée ou promesse : seulement ce qu'une synthèse, une note de décision, une demande de Fable, un mandat ou un mot du directeur retient, recommande ou promet. Porteur « mot du directeur » quand l'extrait cite ses mots ou un GO ; sinon « synthèse ou décision ».
- Champs ajoutés : `depouille` et `nb_fichiers` (gisements) ; `lot` (idées et promesses, code local qui les rattache à leur gisement, à retirer à l'import) ; `note` (recoupements). `fiche` vaut « G-? », « I-? » ou « P-? ».
- Lignes en JSON compact, 600 signes au plus. Pour tenir cette borne, 35 extraits sont raccourcis à un début de ligne (coupé à un blanc) ; ils restent mot pour mot.
- Vérification par programme : chaque extrait est cherché dans `git show 2f6876df:CHEMIN`, espaces normalisés. 92 extraits vérifiés sur 92, aucun retiré. Contrôles aussi : longueur de ligne, extrait de 300 signes au plus, trois à six mots, aucun chemin interdit cité.

## Comptes

92 lignes : 30 gisements, 42 idées, 20 promesses.

| Dossier | Gisements | Idées | Promesses |
|---|---|---|---|
| chantiers-21-novembre-v1 | 7 | 16 | 4 |
| demandes-fable-api-2026-11-22-v1 (demandes 40 et 41) | 2 | 6 | 4 |
| exploration-idees-fable-v1 | 2 | 10 | 1 |
| lentilles-noyau-sabotage-v1 | 1 | 3 | 1 |
| mathematiques-nouvelles-v1 et sa passation | 5 | 3 | 5 |
| papier-c-banc-de-juge-v1 | 1 | 0 | 0 |
| protocole-x-conscience-anesthesie-v1, preparation-experiences-anesthesie-v1, demande-sommeil-consolidation-v1 | 5 | 4 | 5 |
| docs/sources (organisme d'idéation, PDF des puits étroits, score apparié, prix, Lean) | 5 | 0 | 0 |
| registres/essaim (vers la mère, vers la veille) | 2 | 0 | 0 |

Les idées et promesses tirées des messages en essaim sont comptées avec le dossier dont elles parlent.

## Recoupements avec le journal (à trancher par la veille)

- La ligne anesthésie et conscience est déjà fichée (G-0010 ; propositions 1 à 4 en I-0319 à I-0322 ; agents arrêtés en I-0323). Seules les décisions et promesses neuves sont proposées ici ; le gisement du dossier est marqué « recoupe G-0010 ».
- La liste exhaustive jointe à la demande 41 est identique octet pour octet à celle de G-0005 : pas de gisement à part.
- La relance de l'organisme à bassin étroit recoupe I-0004 ; les recommandations 1 et 2 sur l'exploration recoupent I-0056 ; la lecture par lentille recoupe I-0317 (voisine, pas la même idée).

## Ce qui n'a pas été lu, et pourquoi

Pour cloisonnement ou doute :
- Cinq fichiers écartés par prudence parce que leur nom contient « 24 » (aucun n'est la demande ou la réponse 24) : `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/v5_r24.py`, `docs/notes/protocole-x-conscience-anesthesie-v1/sources/arxiv-2609.01924.pdf`, `…/sources/bayne-2024-tics.pdf`, `…/travail/textes-extraits/arxiv-2609.01924.txt`, `…/travail/textes-extraits/bayne-2024-tics.txt`.
- `docs/notes/mathematiques-nouvelles-v1/brouillon-2-fable-v1/copies-sans-nom-v1/preenregistrement-pilote-generation-v1-brouillon-sans-nom-v1.md` : copie d'un préenregistrement (doute, règle sur `prereg/`).
- `docs/sources/ideation-organism-a41b7b50-v1/copie/orchestrator/prereg/` : préenregistrements copiés (doute) ; seul l'inventaire du dossier est lu.
- `docs/notes/mathematiques-nouvelles-v1/versement-bloc-notes-2026-11-22-v1/` : seul le LISEZMOI est lu ; le reste porte des rejeux, des sorties et une « sous-banque-cle » (doute sur des clés de mondes plantés).
- `docs/notes/lentilles-noyau-sabotage-v1/` : objet jugé au titre (lire, avec une lentille, ce qui distingue un agent saboteur ; c'est de la détection). Lus seulement le mandat (§ 1), le verdict et les § 7 et 8 de la réponse ; corps (§ 1 à 6), calculs, PDF et sources de la toile non lus. Cloisonnement à juger par la mère.

Par économie, sans motif de cloisonnement : les réponses une à une des modèles (question du seuil du devin, demandes 40 et 41), le corps des trois conceptions hors décisions et ordre d'écriture, les contre-lectures et vérifications de code, les rapports de lecture de l'exploration, les PDF et pages archivés.

Déclaration : en listant `registres/essaim/vers-mere/`, des messages du 22 novembre (04:52Z à 06:28Z) de la session des lentilles, hors de la liste du versement, ont été lus en partie. Ils parlent de devis, de machines et d'une lecture des sondes de l'étape B bis, sans aucun résultat. Rien n'en est tiré ici.
