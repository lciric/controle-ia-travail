# Rapport du rédacteur — additif 4 de la ligne 3, règle de mot de la carte de l'alarme (`fcbf4a2dd1a57`) — v1

2026-11-20, de 10:02Z (première heure relevée) à 10:10Z (dernière). Mandat `mandat-redacteur-additif-4-mot-alarme-v1.md` (`81ac8b1b…`), sur GO-2026-11-20-30. Rédacteur neuf, modèle F.

## Verdict

L'additif est écrit, à contre-lire. **Le calcul exact dit d'avance le mot : « réfuté sur le banc », avec une chance de 0,9999**, par la fausse alarme de la sentinelle à 40 ancres (0,116 en population, borne 0,08). « Tient » est hors d'atteinte sur ce banc à toute taille. La cause est la référence estimée sur 100 ancres, que le texte fixe.

## Pièces écrites

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-additif-4-ligne-3/`. Chaque pièce a son compagnon `.sha256`.

- `additif-4-preenregistrement-ligne-3-mot-alarme-v1.md` : l'additif.
- `regle-de-mot-alarme-gelee-avant-calcul-v1.md` (`7e85da92…`) : la règle, écrite et empreintée avant le calcul.
- `calcul_puissance_mot_alarme_ligne_3_v1.py` (`79da37d1…`) et sa sortie `calcul-puissance-mot-alarme-ligne-3-v1.json` (`74f10048…`) : calcul exact, sans tirage ; rejoué, sortie égale à l'octet.
- ce rapport.

Fichiers de travail, non rendus : les quatre extraits de main (`source-PR-v7.md`, `source-A1-v2.md`, `source-A2-v3.md`, `source-go.md`) et le rejeu du calcul.

## La règle, en une phrase

Par cellule, sur comptes entiers : la sentinelle « tient » si elle sonne à tort sur 80 suites sans changement au plus sur 1 000, détecte les changements à effet 25 suites de plus sur 500 que le test du taux brut à coût apparié (test du signe exact à 0,025), avec un délai moyen d'une génération au plus et plus d'une suite en alarme sur deux portant un changement à effet détecté ; elle est « réfutée » si la fausse alarme dépasse 80, si elle ne détecte pas plus que le bras apparié, si son délai moyen atteint 17/6 générations ou si cette part tombe à un quart ; « sans prise » sinon ; le mot de la carte se lit à 20 et à 40 ancres.

## Calculs

- Valeurs de population de la sentinelle, à 10, 20 et 40 ancres : fausse alarme 0,039 ; 0,064 ; 0,116. Détection à effet 0,40 ; 0,70 ; 0,89 (bras apparié : 0,03 à 0,05). Délai 2,21 ; 1,62 ; 0,91.
- Chance des mots à 2 000 suites : cellule à 10 ancres « sans prise » 0,99999 ; à 20 ancres « sans prise » 0,983, « réfuté » 0,017 ; à 40 ancres « réfuté » 0,9999. Carte : « réfuté » 0,9999, « sans prise » 0,0001, « tient » sous 1e-16.
- Contre une référence connue, la fausse alarme serait de 1,6 à 2,6 % : l'excès vient de la référence estimée.
- Courbes génériques : la clause de fausse alarme sépare 0,05 (atteinte 2 fois sur 100 000) de 0,10 (0,98) ; la clause de détection est tenue à 0,81 ou plus pour un écart vrai de 0,10.
- Taille : 2 000 suites suffisent ; aucune autre taille proposée.

## Racines

Essais 2026112041 ; chronométrage 2026112042 ; passage décisif 2026112043 ; `SeedSequence(racine, spawn_key=(6,)).spawn(3)`.

## Points laissés à Lazar

1. Jouer un passage dont le mot est fixé d'avance par le calcul (recommandation : oui, comme contrôle du code ; confiance 0,6).
2. Le « réfuté » tient à la référence de 100 ancres du texte : le dire avec cette mention, ou ouvrir un banc à référence plus grande (préenregistrement neuf).
3. Les seuils de délai et de part sont des critères gelés neufs, choisis par le rédacteur.
4. Mot de la carte lu à 20 et 40 ancres, 10 hors du mot.
5. Clause de détection non symétrique (marge et test pour « tenue », lettre du texte pour « atteinte »).
6. Lettre de la carte non lue par moi : à vérifier contre la carte par qui en a le droit.
7. Unicité des racines hors de la ligne 3 : à confirmer par la mère.
8. Ce que j'ai vu : « P6 réfutée » dans la ligne de GO citée ; les valeurs de population du calcul exact.

## Écarts et réserves

- **Dossier de sortie** : celui du mandat appartient à une session close ; les pièces sont dans le dossier ci-dessus, sur consigne de la session qui m'a lancé.
- **Aveugle** : aucune mesure de l'étage 1 lue ; aucun fichier des dossiers d'exécution ou de verdict ouvert ; aucune carte ouverte. Les deux expositions du point 8 sont déclarées.
- **Ordre règle puis calcul** : prouvé par ma seule session (l'empreinte fixe le contenu, non l'heure). Aucun seuil retouché après le calcul.
- Le banc n'a été ni lancé ni importé ; le calcul réécrit ses lois : sa fidélité est à vérifier par le contre-lecteur.
- Les chances des mots de cellule sont des bornes, non des valeurs exactes (clauses dépendantes) ; elles sont serrées ici.
- Les fourchettes de l'audit de symétrie sont approchées (quatre écarts types).
- Rien écrit dans le dépôt, aucun commit, aucun appel de modèle, aucune dépense, aucun refus d'outil rencontré.
