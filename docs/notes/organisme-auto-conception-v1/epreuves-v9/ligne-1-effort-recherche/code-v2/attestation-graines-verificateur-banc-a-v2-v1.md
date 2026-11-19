# Attestation sur les graines — vérificateur du code du banc A, ligne 1

Qui atteste : contre-lecteur, modèle S.
Heure (`date -u`) : 2026-11-19T22:00Z.

**Pendant ma contre-lecture du code v1 et ma vérification du code v2, je n'ai dérivé aucune graine des racines 2026111901, 2026111902 ni 2026111903.**

## Sur quoi je la fonde

Ce que j'ai exécuté, et rien d'autre que cela :
- lecture de fichiers (préenregistrement, code v1 et v2, rapports, essais), calcul d'empreintes, `git fetch`, `git show`, différentiels ;
- comparaison des deux configurations en objets (aucun calcul de graine) ;
- trois lancements de la suite d'essais, tous dans des copies de mon bloc-notes : le code v1 avec un substitut de la mémoire (41 passés, 1 échoué), puis, avec le vrai fichier de mémoire, le code v2 (58 passés) et le code v1 (42 passés) ;
- aucun étalonnage, aucune course décisive, aucune fumée, aucune analyse de sorties de course, aucun lancement du lanceur.

Les essais n'emploient que la racine des essais, 2026111900. Dans chacun des trois lancements, le dernier essai (`test_zz_aucune_racine_interdite_derivee`) a passé : il vérifie, dans le processus des essais, qu'aucune des racines 2026111901, 2026111902, 2026111903 n'apparaît parmi les premières dérivations de graine consignées. Les essais écrivent dans le dossier temporaire de pytest, pas dans le dépôt.

## Limite

Cette vérification porte sur le processus des essais, où les graines sont consignées ; mon affirmation repose aussi sur la liste exacte de ce que j'ai lancé, donnée ci-dessus. Je n'ai pas lu les sorties des autres sessions.
