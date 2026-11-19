# Note de changements — brouillon 28 du texte neuf du bras A des organismes discrets — v1

**Rédigé par Claude Fable 5.2 (`claude-fable-5-2`)**, le même agent que pour les brouillons 21 à 27.

- **Brouillon** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md`, `604e0410f251c903c7e34d37762292ccafbdac821c2e08d0779f3886991736e9` (2 077 lignes). Les brouillons 20 à 27 ne sont pas modifiés.
- **Pièce jointe** : `docs/notes/relance-organismes-discrets-v1/demandes-a-la-session-principale-bras-a-v1.md`, `5c1d7996072a52e31990584a659ce7a22a381111a991c1e3869ecbc8a1cfbea3` — les trente demandes à la session principale, chacune avec sa question et ce qui en dépend ; elle se lit seule.
- **Fiches pour Lazar : aucun fichier neuf.** Celles du brouillon 23 restent en vigueur (`f20abfed…`).
- **Source** : la vérification du brouillon 27 (`9cdfe30552ae9c2b38052802ca8c1741ca813cd6b95f81056f93a3109da01323`), lue en entier. Verdict : engageable, sans défaut à corriger ; deux remarques mineures.
- **Méthode** : copie du brouillon 27 par `cp`, puis 16 remplacements exacts, chacun vérifié unique par programme.
- **Registre des accords** : relu sur la branche principale distante au commit `5adfc241` ; aucune ligne de plus.
- **Heures (UTC, `date -u`)** : début 18:11:39Z le 2026-11-19 ; brouillon scellé à 18:14:24Z.
- **Interdits tenus** : aucune empreinte de fichier d'un dossier du côté habilité ; aucun interne de moniteur ; aucun code ouvert ; aucune clé ; aucun appel de modèle ; seul appel réseau, `git fetch` de la branche principale ; ni `registres/`, ni `.claude/`, ni le journal touchés ; rien committé ; aucun fichier existant écrasé ; aucun sous-agent.

## Contrôles par programme

| contrôle | résultat |
|---|---|
| section 12 ; « Critères de lecture gelés » en entier ; section 10 | identiques, caractère pour caractère, au brouillon 27 |
| titres ; consignes figées | inchangés ; `98a9bd34…` et `ecf590ea…` recalculées |
| citations à la lettre | brouillon 20 : 935 sur 935 ; brouillon 27 : 1 169 sur 1 169 |
| table d'en-tête, sans les fichiers cloisonnés | 150 lignes à empreinte : 136 recalculées et égales, 0 différente, 14 sautées et non ouvertes |
| marque des cases non remplies | huit lignes, toutes en 13.1 |
| validateur (`problemes()`) | les deux problèmes attendus |
| pièce des demandes | trente demandes ; les dix-huit numéros de la case du module y sont tous |

## Ce qui est porté

| remarque | ce que le texte dit maintenant | où |
|---|---|---|
| M-2 deux demandes absentes de la case du module | demande 17 : les chemins que la garde statique de l'analyse doit élaguer ; demande 18 : comment `piece_source` désigne le module qui a produit la livraison ; la case renvoie à la pièce des demandes | 13.1 |
| M-1 `effectifs` et `exclues` | **je l'approuve, et je l'étends** : rapportés tels quels quand ce sont des comptes — un entier positif ou nul, ou une liste ou une table dont toutes les valeurs sont de tels entiers — ; sinon « non rapportés (forme non reconnue) », sans arrêt et hors de la liste des refus. De même, les aires de la somme et du maximum de l'agrégateur ne sont rapportées que si ce sont des nombres de 0 à 1 | 6.9 ; 8.4 |

Pourquoi l'extension aux aires de l'agrégateur : c'est la même voie. Un texte ou une liste rendus là par erreur atteindraient un rapport de la même façon.

## Ce que le code doit porter

1. `effectifs` et `exclues` : rapportés seulement si la valeur est un entier positif ou nul, ou une liste ou une table dont toutes les valeurs, à toute profondeur, sont de tels entiers. Sinon la sortie porte « non rapportés (forme non reconnue) ». **Aucun arrêt, aucun événement** : ce n'est pas un refus.
2. Aires de la somme et du maximum de l'agrégateur : rapportées seulement si ce sont des nombres de 0 à 1 ; sinon « non rapportées ». Aucun arrêt.
3. Essais : `effectifs` fait d'entiers, rapporté ; `exclues` qui porte un texte, « non rapporté » et la lecture continue ; une aire de l'agrégateur qui est un texte, « non rapportée » et la lecture continue.
4. Rien d'autre ne change depuis la note du brouillon 27.

## Réserves

1. **Les noms des clés d'une table de comptes ne sont pas contrôlés** : un texte pourrait encore passer par un nom de clé. La demande 14 de la pièce jointe demande la forme de ces champs ; quand elle sera connue, le texte pourra fixer leurs clés.
2. **La pièce des demandes cite les motifs de chemins que la relance élague** (noms de dossiers seulement). Ce sont ceux de la liste des interdits ; aucun contenu.
3. **Je n'ai toujours pas relu le texte en entier.** Le vérificateur a dit, section par section, ce qu'il a vérifié identique par programme.

## Fichiers ouverts pour ce brouillon

- `docs/notes/relance-organismes-discrets-v1/verification-brouillon27-bras-a-v1.md`, en entier.
- Du brouillon 27 : la ligne de la case du module de 13.1.
- Mes notes des brouillons 21 à 27 (de mémoire de cette session, sans les rouvrir).
- `registres/go.md` de la branche principale distante, par `git show`, après la ligne 511.
- Par programme, pour leur seule empreinte : les 136 fichiers de la table d'en-tête hors des dossiers cloisonnés.
- Rien d'autre.
