# Vérification brève du brouillon 28 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 27. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md`, `604e0410f251…`. Note : `94f704edb42b…`. Les deux compagnons sont vérifiés.
- **Méthode** : comparaison des brouillons 27 et 28 phrase par phrase, faite par programme. J'ai lu les blocs touchés et leur contexte en 6.9 (ligne 724), en 8.4 (ligne 992) et en 13.1 (ligne 1306). Je n'ai ouvert aucun code.

## Verdict : **engageable**

1. **Aucune règle de jugement ne change.**
   - Par programme, sont identiques au brouillon 27 : la section 12, les critères de lecture gelés (7.1 à 7.8), la section 10, et les sections de l'hypothèse au seuil, 6.1 à 6.8, 9 et 11.
   - Les fiches 9 à 12 parties à Lazar restent mot pour mot dans le texte.
   - Les ajouts portent sur trois choses :
     - **ce qui est rapporté**, sous une marque « non rapportés », sans arrêt et hors de la liste fermée des refus ;
     - **deux demandes** de plus à la session principale (17 et 18), dans la case du module ;
     - **un renvoi** à une liste consolidée de ces demandes.
2. **L'extension aux aires de l'agrégateur est juste.** Elle ne touche pas l'aire qui fait l'état de ce moniteur.
   - **Les aires visées** : celles de la somme et du maximum. Elles sont rendues dans `agregateur_somme_sans_etat` et `agregateur_maximum_sans_etat`, deux clés de la sortie de la lecture commune.
   - **Leur statut, déjà écrit** : depuis le choix de Lazar GO-2026-11-19-48, elles sont « rapportées, sans état ni verdict ».
   - **L'aire décisive de l'agrégateur** est celle de la moyenne des scores des actions lues. C'est le champ `aire` de ses lectures, aux trois doses de la famille. Elle relève toujours de la table des formes : une aire qui n'est pas un nombre de 0 à 1 y est un écart de structure, donc un arrêt (6.9, écart (iii)). La règle neuve ne l'atteint pas.
   - **L'asymétrie est voulue et cohérente** :
     - une faute sur une grandeur qui sert un état arrête ;
     - une faute sur une grandeur seulement rapportée se dit « non rapportée », sans arrêt, sans cause de refus nouvelle ;
     - c'est le même principe que « non rendue » au cas C et à la dose ¼.
3. **Intégrité tenue** (partie 2).

## 1. Remarques mineures (aucune ne retient le texte)

- **M-1.** La phrase neuve de 6.9 sur les aires de l'agrégateur gagnerait une incise : « la somme et le maximum seulement ; l'aire de la moyenne, décisive, reste sous la table des formes ». Rien ne les confond aujourd'hui, puisque les clés sont distinctes. Mais ce serait la lecture la plus sûre pour le rédacteur du code et pour l'agent du verdict.
- **M-2.** La forme de ces deux clés n'est pas transmise : un nombre par dose, ou une table par dose qui porte aussi d'autres champs ? « Rapportées quand ce sont des nombres de 0 à 1 » doit s'entendre valeur par valeur, à toute profondeur, comme pour les comptes. Sinon, une table qui porterait aussi un effectif serait dite « non rapportée » tout entière. À dire en 6.9 et à joindre à la demande 14.
- **M-3.** « Un entier positif ou nul » : en JSON, `true` et `false` ne sont pas des entiers. À préciser pour le code, car Python les tient pour des entiers.
- **M-4.** La liste consolidée des demandes (`docs/notes/relance-organismes-discrets-v1/demandes-a-la-session-principale-bras-a-v1.md`, scellée) est citée trois fois, mais elle n'a pas de ligne à empreinte dans la table d'en-tête (R6). À ajouter au prochain brouillon, ou au plus tard avec les cases remplies.

## 2. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 27 intacts | compagnons vérifiés (`b076e3f9…` à `428f9e55…`) |
| brouillon 28 et note | `604e0410…`, `94f704ed…` : compagnons vérifiés |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 27** ; fiches 9 à 12 mot pour mot dans le texte |
| hypothèse au seuil ; 6.1 à 6.8 ; sections 9 et 11 | identiques au brouillon 27 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 27 : 1 169 sur 1 169 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1293, 1294, 1296, 1297, 1299, 1304, 1305, 1306), toutes en 13.1 |
| table d'en-tête, trois lignes neuves | empreintes égales (brouillon 27, sa note, ma vérification) ; **aucune empreinte de fichier cloisonné prise** |

## 3. Fichiers ouverts

- Le brouillon 28 (par différence, et les lignes 724, 992 et 1306).
- Les brouillons 20 et 27, par programme.
- La note du brouillon 28, pour son empreinte seule.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Pour la liste consolidée des demandes : son existence et son compagnon seulement, sans lire son contenu.
- Rien d'autre. Aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
