# Vérification courte des corrections — préenregistrement de la course du banc fermé, brouillon 5 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon5.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `0d4637700155f9e119afd2edf16b172234f2402e`. Empreinte recalculée : `0bccc493204303e9f5b2ea07a92f6f7f147690665562a82a235b4ed5d75a3ab6`, égale à son `.sha256` compagnon. Les brouillons 1 à 4 sont inchangés.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Elle répond à `prereg/course-banc-ferme-v1-verification-brouillon4-v1.md` (`3b4b63ed966862215930c43ea7043bc9795ef4e11fcb94b5e5bc8b3c61a01a44`).
- **Date** : 21 novembre 2026, vers 19:05 UTC. Refus d'un classifieur : aucun.
- **Méthode** : `diff` ligne à ligne du brouillon 4 au brouillon 5, lu en entier. Source neuve lue : la note du mot de Lazar `registres/passations/2026-11-21-1850-attaquant-informe-mot-lazar-piece-securite-v8.md`, branche `claude/loving-lamport-7ol5ws`. Empreinte recalculée `1b750a1c906e6e1bbe6c67c6d6cab0089ba52da0f968daf91a2c7b988def5b1b`, égale à celle que cite le brouillon. Verbatim : « go reco b, pièce de sécurité v8 ».
- **Validateur** : il refuse encore (« section vide ou à remplir : Plan d'analyse », marqueur du champ n° 19). C'est attendu.

## Constats

| Point | Correction | État |
|---|---|---|
| B1 | D6 ne déclare plus aucun écart à la pièce v7 : la voie d'envoi est « en attente de la v8 », elle n'existe pas avant que la v8 soit acceptée, et ses six conditions sont proposées à la v8. Les deux lignes reprises de la pièce sont annotées « valent telles quelles ». Une ligne d'arrêt neuve dit : v8 non acceptée ou ne couvrant pas la voie, donc aucun envoi, aucun dommage établi (repli de N-060 v3 point 3), et le vérificateur n'est pas lancé. Le vérificateur vérifie contre la v8. Le nœud 11 est tranché sur le mot de Lazar cité, et l'identifiant de GO à inscrire par la mère est dit en réserve. L'en-tête dit que le texte ne peut pas devenir définitif avant la v8. | levé |
| B2 | Le nœud 10 est rendu aux nœuds ouverts, pour Lazar, avec deux options, l'enjeu et une recommandation. La réserve de D1 est dite « proposée ». La liste d'arrêt porte « nœud 10 non tranché : aucune course ». | levé |
| M1 | L'oracle est figé (questions, réglages, règle de réunion, seuil), son empreinte est à l'addendum B, aucune retouche n'est permise après le premier envoi, et la liste d'arrêt porte la ligne correspondante. | levé |
| M2 | Le compte rendu du monteur de l'oracle est borné au fichier public, sans aucun taux, même d'ensemble (D6, D8, ligne d'arrêt). | levé |
| M3 | `ecart_equivalence` au quantile de la configuration scellée, le maximum par défaut ; contrôle négatif `decalage = 1` à chaque couche ; épreuve 0 sur la pile déclarée aux deux manifestes, avec sa limite dite ; poste de calage au champ n° 19 ; exigence « même poste, ou même vérification refaite » portée à la réserve de D1 ; verdict sur trois épreuves. | levé |
| M4 | « Au moins deux » lecteurs ; « paire la moins accordée » dans la prédiction, le seuil et les critères ; un produit « non lu » sort du numérateur et du dénominateur du lecteur et de la lecture « selon tous », et il est compté par lecteur ; au-delà d'un produit non lu sur dix chez un lecteur, le dommage est « non établi ». | levé |

Aucun autre changement. Aucun retrait. Aucun contenu de mode, de recette ni de paramètre.

## Remarque de forme, non bloquante

La condition « Pièce de sécurité v8 acceptée, et ce texte scellé dans une version qui la cite » est insérée entre les conditions de lancement 5 et 6, sans numéro. Elle est à numéroter dans la version qui citera la v8, avec les renvois qui en dépendent (« condition 7 » pour le vérificateur). Cela peut se faire dans ce même geste.

## Verdict final

**Accepté.** Les deux points bloquants et les quatre mineurs de la vérification du brouillon 4 sont levés.

Le texte ne devient définitif qu'après cinq conditions :
- la pièce de sécurité v8 acceptée, et ce texte remis en version qui la cite (le rapprochement de ses six conditions avec la v8 se vérifiera alors, sur les seules différences) ;
- le mot de Lazar sur la v8 inscrit au registre des GO ;
- les champs ouverts remplis ;
- le nœud 10 tranché par Lazar ;
- le nœud 8 tranché.
