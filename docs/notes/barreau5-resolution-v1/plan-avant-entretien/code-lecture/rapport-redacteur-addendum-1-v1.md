# Rapport du rédacteur de l'addendum 1 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

Écrit le 20 novembre 2026 vers 02:05Z (horloge du conteneur) par le rédacteur de l'addendum 1, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce de travail. Mandat `mandat-redacteur-addendum-1-plan-v1.md`, empreinte vérifiée avant lecture, égale à l'attendue (`1645afecf90c18ee0fec7babe5ff85413178b4f906b6d2b6dacd4b92967a74ce`).

## Sorties
| fichier | sha256 |
|---|---|
| `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon1.md` | `1c7d6e51fb355ab0349b93435bcb404a9bee82f5cb5064be5f4d8640c38632a8` |
| `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/etat-redacteur-addendum-1-01-regles-arretees.md` (état intermédiaire) | `b3fd3cc6901c26a0e7c0944d0af755733972923bc62047342f13f90a671592f8` |

Ce rapport est scellé par son compagnon. Aucun commit, aucun réseau, aucune dépense, aucun code modifié, aucun refus d'outil.

## Les trois règles
1. **Niveau d'une issue sous huit familles.** La lecture du code est celle du texte. Une épreuve est à 99 dès huit familles présentes, à 95 à six et sept, sans niveau sous six. Une issue porte le plus faible des niveaux de sa liste : S — M1, M3, E1, E2a, E2b, E3 ; D et C — M1, M3, E3. Les issues E, N et « non interprétable » n'en portent pas. Une épreuve qui n'est pas « séparé » ne compte pas pour D. Aucun changement de calcul dans le code.
2. **Tâche sans coût lisible chez un seul membre.** Elle sort pour tous les membres présents de la famille. Un seul jeu de tâches retenues par famille, pour M1 et M3 ; rien n'est apparié action par action. Le code change dans `manipulation` (l. 725 à 730).
3. **« [borne] » de la phrase « empreinte ».** La moitié de la séparation apprise, ½ × Δ_app, au format des autres nombres de la phrase. Le code change à la ligne 1133 de `phrases`.

## Sources
- Texte scellé (`bdff244f…`) : « Métrique » (m_i, M1, M3) ; « Seuil » (manipulation établie, issue « empreinte ») ; « Plan d'analyse », points 3, 5, 11 et 17 ; « Puissance », limite déclarée de l'issue « empreinte » ; « Critères de lecture gelés » (table, bornes, paragraphe « Sous huit familles ») ; « Ce que dira chaque issue au jury », issue E. Lu par une copie où seize lignes sont masquées (celles qui nomment « B bis » ou la phrase de la consigne).
- Rapport du développeur (`a140273f…`), questions 2.1 (4), (6) et (10) ; contre-lecture v2 (`f2f81f32…`), réponses 2 et 4, constats m-2, m-4, M-2, mutation C7.
- Code `lecture_v1.py` (`c3db0074…`), aux lignes citées dans le brouillon.

## Doutes
1. **Exposition.** Les lignes 59 à 61 du texte scellé citent des chiffres de courses antérieures sans porter les mots de mon masque ; je les ai lues. Déclaré dans le brouillon. Aucune des trois règles n'en dépend ; au contre-lecteur d'en juger.
2. **Point 2, cas limite** : aucune tâche retenue dans une famille. Le brouillon garde le comportement du code (famille absente de M1 et de M3, motif écrit) et le nomme. Le texte ne l'écrit pas : c'est le passage le plus proche d'un choix neuf. Si le contre-lecteur le juge hors de portée, il se retire sans toucher la règle.
3. **Point 3** : le plus grand d_k était défendable aussi (borne haute valide d'une médiane commune, même erreur). Retenu ½ Δ_app : c'est ce que le texte appelle « la borne », elle est toujours positive, et elle affirme moins.
4. **Point 1, pour D** : une épreuve E1, E2a ou E2b « séparé » à 95 % sous une issue D à 99 % n'abaisse pas le niveau de D. Défendu par ce que D affirme ; la lecture inverse serait plus prudente encore, mais elle n'est pas celle du code et ne suit pas « les épreuves qui la fondent ».
5. **Épreuve à vérité plantée** : les règles 2 et 3 ne sont vues par aucune règle gelée du point 11 telle qu'elle est écrite ; elles ne le sont que par des essais du code, ou si la fabrique plante des coûts illisibles. Je ne pouvais pas ajouter d'épreuve.
6. **Heure de l'en-tête du brouillon** : il dit « vers 02:00Z à 02:30Z » ; l'horloge du conteneur donnait 01:59Z au début et 02:02Z au scellement. Le brouillon scellé n'est pas réécrit ; à corriger au brouillon suivant.

## Ce qui va à Lazar
- La demande de scellement de l'addendum, après contre-lecture et vérification.
- Avec elle : le cas limite du point 2 (garder « absente », ou compter une différence nulle ; recommandé : garder ; confiance 0,7) ; le choix de ½ Δ_app au point 3 (confiance 0,8).
- Hors de mon mandat, encore ouverts : le cas m-4 de la contre-lecture (M1 ou M3 sous six familles quand E3 en a six ou plus) et « M1 dans toutes les épreuves » (constat M-2). Le point 1 ne dépend d'aucun des deux.

## Ce qui menace le gel
- Les règles 2 et 3 changent `lecture_v1.py`, donc l'empreinte de `CODE-LECTURE-B5F` ; elles s'ajoutent aux corrections M-1 à M-3 et repassent par le contre-lecteur du code.
- La chaîne de l'addendum (contre-lecture par Opus, vérification, mot de Lazar) doit finir avant la seconde programmation et l'épreuve à vérité plantée.
- La seconde programmation doit recevoir la table du point 1, niveau compris : l'accord exigé est exact.
