# Notice — développeur habilité côté moniteurs du bras A : les deux moniteurs à modèle de langue (lot 14) — version 2 du code

**En bref.**
- La version 2 applique les corrections de la contre-lecture (`contre-lecture-lot-14-bras-a-v1.md`, `0c1d0083…`), qui concluait « pas avant » : trois corrections bloquantes et quatre autres.
- La lecture change sur deux points de fond : la balise imposée est encodée avec la dernière ligne générée ; la génération s'arrête dès que le texte contient la balise, et une balise soudée à ce qui la suit est coupée et réencodée, sous un état à part.
- 48 essais passent (47 sans le dossier du tokeniseur du juge). Chaque garde du module, retirée seule, fait échouer un essai : 45 sur 45, sans le dossier du tokeniseur.
- La version 1 reste intacte ; ses essais l'éprouvent toujours.

Qui : développeur habilité côté moniteurs, session fille de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat lu ; aucun poids chargé ; aucune dépense ; jamais la suite d'essais complète. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/moniteurs_langue_v2.py` | `2400c1387838a98cd12955111bfac71391d841d61c12ed44b5a86fddacc7d7b6` |
| ses essais | `tests/test_bras_a_v2_habilite_moniteurs_langue_v2.py` | `1221483c2b7001e1b592252453e4b2fa4fef8cb18aca02f6aea4f235879ca48d` |

Commit `158f0c87` de la branche `claude/bras-a-habilite-developpeur-v1`.

```
PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_moniteurs_langue_v2.py
```
Dernière ligne : `47 passed, 1 skipped` ; `48 passed` avec `QWEN_TOKENISEUR_DOSSIER`.

## 2. Corrections bloquantes

**1. Balise imposée.** Avant : les jetons de la balise seule étaient ajoutés à la suite des jetons générés. Après : `imposer_la_balise` décode la dernière ligne générée (depuis le dernier jeton qui contient un saut de ligne), y ajoute la balise et réencode le tout ; les jetons d'avant cette ligne sont gardés tels quels. C'est la règle du contre-lecteur.
- Sur le vrai tokeniseur du juge, pour les sept fins de texte du rapport (point, deux-points, parenthèse, espace, signe égal, saut de ligne, chiffre), le contexte imposé est égal à l'encodage du texte généré suivi de la balise ; la concaténation simple échoue pour cinq au moins (essai).
- Si la dernière ligne ne se décode pas à l'identique (octets partiels), la balise est concaténée et le cas est porté par un état de jointure, compté. Aucun repli silencieux.
- Après une fin de réponse, le jeton de fin est retiré avant la balise ; un essai le voit (le modèle factice refuse de lire une balise précédée d'un jeton de fin).

**2. Jetons de fin par moniteur.** `exiger_moniteur` reçoit la liste des jetons de fin et rend la spécification du moniteur ; `lire_avec_raisonnement` l'exige et refuse un format dont les jetons de fin ne sont pas exactement ceux du moniteur, ou un lecteur d'un autre cas. Pour le juge, la liste est celle relevée au lot 15 ; toute autre est refusée, dont le défaut du harnais (un seul jeton). Pour le moniteur boîte noire, la liste est à relever par le lanceur sur la configuration de génération de son dépôt, à sa révision (dépôt à accès restreint : non relevée ici) ; le code exige une liste non vide, sans défaut.

**3. Essais manquants.** Les deux essais du contre-lecteur sont repris à la lettre (`test_temperature_appliquee`, `test_reglage_de_plus_refuse_par_la_lecture`) ; le troisième, sur le jeton de fin, est écrit ici (`test_jeton_de_fin_jamais_avant_la_balise_imposee`).

## 3. Autres corrections

- **Balise soudée** (règle retenue par la mère). La génération s'arrête dès que le texte généré contient la balise. Si la balise finit le texte : état « écrite ». Sinon, le dernier jeton la finit et porte autre chose : le texte est coupé juste après elle, la dernière ligne réencodée, et l'état est « écrite, fin de balise réencodée », compté. Essai sur un tokeniseur jouet où la fin de la balise et le saut de ligne forment un jeton, et sur le vrai tokeniseur du juge. Le drapeau « balise écrite sans point de lecture » de la version 1 n'a plus d'objet : il est remplacé par cet état.
- **Gardes sans artefact** : rendu par proposition, action sans opération, lois non normalisées, trois gardes du tokeniseur du lecteur chiffre par chiffre, contexte vide, demande refusée dès sa construction. Un essai chacune.
- **Gardes tautologiques retirées** : « écritures ≠ 0 à 100 » ; l'appel de la garde du message dans la construction du message. La garde du message reste, pour un message relu ou transmis, où elle est éprouvée.
- **Redondance retirée** : un seul contrôle de l'empreinte au chargement de la consigne.
- **Deux essais aveugles** : l'essai des états emploie désormais un modèle factice dont la lecture dépend de ce qui précède la balise ; un essai de comportement s'ajoute à la lecture du texte source (toute génération de la bibliothèque lèverait).
- **Rendu réel du gabarit** (seconde remarque de la contre-lecture des lots 13 et 15) : `exiger_gabarit_reel` contrôle, une fois par lecture et sur un message de contrôle fixe, que le chemin de rendu employé rend la consigne puis le message, chacun une fois et tels quels. La garde ne dépend d'aucun texte d'agent. Pour le moniteur boîte noire, la forme exacte du rendu, date comprise, reste à éprouver par le lanceur.
- **Sous-échantillon du juge** (recommandation non bloquante, suivie) : `positions_du_juge_pour(entropie, tâche)` dérive elle-même la graine de la clé de la tâche.

## 4. Ce qui change pour l'appelant

- `exiger_moniteur(nom, modele, revision, fins)` rend la spécification ; `lire_avec_raisonnement(…, lecteur, specification)`.
- Chaque lecture porte quatre états possibles de la balise et un état de jointure ; `compter` les rend tous.
- Les cinq réglages et les clés de graine sont inchangés.

## 5. Ce qui reste

- Vérification par le même contre-lecteur, avec les versions 2 des autres lots.
- Case 13.1 : jetons de fin du moniteur boîte noire, à relever et à inscrire ; réglages de la lecture ; date du gabarit.
- Limite inchangée : rien n'est éprouvé sur un modèle réel. Le contre-lecteur a rejoué le chemin à cache sur un modèle d'architecture Qwen2 à poids aléatoires (écart négligeable).
