# Vérification de la différence entre la commande v7 et la commande v8, et de la garde de priorité v2

Verdict : **employable** (0 défaut majeur, 3 défauts mineurs cosmétiques ou sans effet sur la règle de la mère).

Vérificateur neuf (R2), 2026-11-18. Rien exécuté du loueur ; aucune variable secrète lue ; aucun fichier existant modifié.

## 1. Différence v7 → v8 (diff complet lu)
Annoncé dans l'en-tête de la v8 : titre v8 ; paragraphe de correction (mineurs 1-4, 7 levés, 5-6 déclarés) ; ligne de la table (garde v2, 14 essais, empreintes 9360b9a0 / add2d5c0) ; bloc de l'étape 10 bis (variable J, `rm -f "$F" "$J"`, module v2, attente bornée 2 s x 60, `head -1`, grep v2) ; texte de l'étape 10 bis (120 s, `absences` 1, 14 essais) ; veille (grep du module v2) ; étape 15 (« si encore vivante »). Rien d'autre ne change (aucun seuil, aucune étape de course). Seule non nommée à part : la veille (grep v2), conséquence évidente du renommage.

## 2. Mineurs levés ?
- 1 (absence sur une seule liste) : levé. `tour` compte les listes consécutives sans la machine (compteur remis à 0 si liste illisible ou machine présente) ; fin seulement à 3 absences ET lecture de l'instance disant absente ; sinon la garde continue, lit le crédit et détruit sous 12. `bbis_en_marche` ne déclare l'étape B bis finie que si la machine des lentilles (témoin) est dans la liste : machine absente et crédit bas → destruction tentée puis absence prouvée (essai joué). Étape B bis jamais déclarée finie à tort. Destruction uniquement de `id_lentilles`.
- 2 (preuve d'absence) : levé (`non_vide=True`).
- 3 (exception) : levé (exception de tour ou de destruction = destruction / `destruction_non_prouvee`, code 4 ; journal en échec sans effet sur le code).
- 4 : levé pour le journal et l'attente. Reste le n° 2 ci-dessous.
- 7 : levé. 5 et 6 : déclarés, honnêtement.
Aucune boucle où la garde ne détruirait jamais alors qu'elle le devrait : seules sorties sans destruction = `bbis_finie` (témoin présent, B bis absente d'une liste lue), `lentilles_absentes` confirmée (3 listes + lecture), `continuer` bornée par tours_max seulement en essai.

## Défauts
**Majeurs : aucun.**
**Mineurs**
1. `src/controle_ia/neuron_lens/garde_priorite_bbis_v2.py`, docstring (ligne « Usage » et puce « la machine des lentilles absente d'une liste lue sans erreur → rien à garder ») : encore au texte v1 (module `_v1`, absence sur une seule liste). Corriger au passage d'une v3 éventuelle ; sans effet à l'exécution.
2. `commande-b-beta-v8.md`, étape 7-10 : « Toute branche d'échec des étapes 7 à 10 : destruction » devrait dire « 7 à 10 bis » (reste du mineur 4 de la v7, non levé et non déclaré).
3. `detruire_et_prouver` : si la liste est vide après destruction (étape B bis finie à l'instant), `non_vide` rend « absence non prouvée », code 4 : fausse alarme, dans le sens sévère. Acceptable.

## 3. Joué
- Essais `tests/test_neuron_lens_garde_priorite_bbis_v2.py` : 14 passés.
- Bloc de l'étape 10 bis, réellement lancé (faux `vastai` dans `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/verif-v8/`, `<ID>` = 70000001, chemins de PID, journal et PID-liste dans ce dossier) : première ligne `continuer`, crédit 40,0, `absences` 0 en 2 s ; `ps | grep garde_priorite_bbis_v2` trouvé, `head -1` correct, ligne écrite dans `pids.txt` ; arrêt par PID, mort confirmée.
- Crochet `decider(bloc, date(2026,11,18))` : ne refuse pas (None).
- Empreintes : compagnons `.sha256` de la v8, de la garde v2 et de ses essais OK ; abrégées de la table (9360b9a0, add2d5c0) égales ; v7 citée `c37f873d` égale.
