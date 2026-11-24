# Rapport du développeur — corrections du v8q : moteur v9-v8r, voie abonnement v8, script de vague v4 (v1)

- 24 novembre 2026, vers 23:10Z. Développeur : Claude Opus 5.5, session des collisionneurs. Classe B. Répond à la contre-lecture `contre-lecture-collisionneur-v9-v8q-opus-v1.md` (`c22da939…`, verdict « à corriger », aucun défaut bloquant). Vérification des corrections : par le même contre-lecteur. **Rien n'est lancé avec ces pièces.**
- Le v8q (`047489b8…`), la voie v7 (`fd1c37b7…`) et le script v3 (`51c27240…`) restent intacts (R12). La voie v8 n'admet plus le v8q.

## Pièces
| pièce | empreinte | base |
|---|---|---|
| `collisionneur_v9_v8r.py` | `1656351a…` | copie du v8q, corrigée |
| `test_collisionneur_v9_v8r.py` | `47049da4…` | neuf |
| `mutations_collisionneur_v9_v8r.py` | `4f0edcf3…` | neuf (campagne de mutations, rejouable) |
| `abonnement-v1/voie_abonnement_v8.py` | `98f1a1d6…` | copie de la v7 |
| `abonnement-v1/test_voie_abonnement_v8.py` | `966c553e…` | neuf |
| `reprise-v8d-v1/vague_abonnement_v4.sh` | `7819b2aa…` | copie de la v2, en-tête refait |

## Réponse aux défauts

1. **Repli silencieux (majeur) : corrigé.**
   - `cle_gemini(m)` passe par `cle_par_son_nom(m, "--cle-gemini", PREFIXE_CLE_GEMINI)`, sans repli. Elle refuse en plus, au moment de l'envoi, un nom de `NOMS_CLE_GEMINI_REFUSES` (défense en profondeur).
   - Les trois lectures (`appeler_gemini`, `appeler_gemini_lot`, `compter_gemini`) l'emploient.
   - Essais : sans nom dans la composition, rien ne part (flux, lot, comptage) ; un nom refusé injecté ne part pas non plus.
2. **Essais en ligne de commande non étanches (majeur) : corrigé, et question éclaircie.**
   - Tous les essais tournent désormais dans le même processus. Les deux transports (`TRANSPORT`, `TRANSPORT_COMPTE`) sont remplacés par un intercepteur qui relève chaque requête puis lève une exception. Les essais de refus exigent zéro requête.
   - Le script des essais se relance dans un environnement vidé, où ne restent que PATH, HOME, la langue, PYTHONPATH et TMPDIR. La campagne de mutations se lance sous `env -i`.
   - **Réponse à la question du contre-lecteur.** Oui : ma première campagne de mutations du v8q a lancé les essais en ligne de commande, qui passaient par un sous-processus au transport réel.
     - Avec la mutation qui retirait le refus de `GEMINI_API_KEY_3`, l'essai « refus de la clé épuisée » a fait tourner le moteur muté, la variable `GEMINI_API_KEY_3` étant posée à la valeur « factice ».
     - Une requête de comptage (`countTokens`, gemini-4-argon) est donc, selon toute vraisemblance, partie vers `generativelanguage.googleapis.com`, avec la valeur « factice » en en-tête.
     - Aucune vraie clé n'est sortie, et un comptage ne coûte rien. C'est toutefois contraire à « sans réseau » : je le déclare ici. La cause est corrigée dans les essais de la v8r.
3. **Couverture (majeur) : corrigée.**
   - Essais ajoutés, avec les lettres du contre-lecteur :
     - (a) une valeur factice posée pendant `declarer_cle_gemini`, absente du journal et de l'écran capté ;
     - (b) un lot complet sur transport simulé (création, relevés, délai dépassé sous horloge simulée, annulation) : la clé nommée figure dans toutes les requêtes ;
     - (c) un étage sans option ni variable : arrêt qui nomme exactement `['GEMINI_API_KEY']` ;
     - (d) un comptage, variable nommée absente et défaut présent : refus, zéro requête ;
     - (e) « GEMINI_API_KEY-2 » : refus « mal formé » ;
     - (f) un dossier sous une autre empreinte de script, lancé sans `--reprise` : arrêt, et aucune entrée `nom_cle_gemini` au journal.
   - Le contrôle textuel est remplacé par une lecture de l'arbre syntaxique. Il refuse tout `os.environ.get`, `os.getenv` ou `os.environ[...]` dont l'argument est un littéral `GEMINI_API_KEY…` ou `NOMS_CLES["gemini"]`.
   - **22 essais sur 22 passés.**
   - **16 mutations sur 16 tuées** : les quatre premières, les dix du contre-lecteur (C1 à C7, C9, C10, et les deux qui écriraient ou afficheraient la valeur) et deux nouvelles (restriction de la clé libre ; espace d'Anthropic).
   - La mutation C7 (défaut changé en `GEMINI_API_KEY_2`) survivait d'abord, car « GEMINI_API_KEY » est contenu dans « GEMINI_API_KEY_2 ». L'assertion exige maintenant le nom exact.
4. **`GEMINI_API_KEY_FREE` non gardée (majeur) : corrigé.**
   - `NOMS_CLE_GEMINI_RESTREINTS = {"GEMINI_API_KEY_FREE": ("carbon", "neon")}` : refus au code 1 si une espèce de Google de la composition n'y figure pas.
   - Essais : un cas sain (Carbon et Neon, et une espèce hors de Google en plus) et un artefact (Argon et Carbon, refusé, Argon nommé).
   - R-5294 est bien au registre : `registres/decisions.md` de `origin/main`, ligne 5438, mot de Lazar vers 13:55Z le 24 novembre, « utilise la clé gemini free : GEMINI_API_KEY_FREE pour Carbon et Neon ». Ce registre n'est pas sur la branche de travail de la session ; d'où l'absence que le contre-lecteur a relevée.
5. **Espace d'Anthropic (majeur, antérieur, depuis la v9-v8l) : corrigé dans cette version et déclaré.**
   - `--nom-espace-anthropic` subit le même refus de préfixe que `--cle-anthropic`.
   - Essai : le défaut est admis, `GEMINI_API_KEY_2` est refusée.
   - Le choix de corriger plutôt que de déclarer en limite est le mien. La mère peut demander l'inverse.
6. **Motif du refus de `GEMINI_API_KEY_3` (mineur) : corrigé.**
   - Le motif devient « consigne de la mère du 24 novembre », dans le message, le commentaire et l'en-tête.
   - Le commentaire de la constante interdit d'y mettre le nom par défaut, ce qui ferait tomber `verifier`, `devis` et `devis-reprise`.
7. **En-tête et docstring du journal (mineur) : alignés.** Le journal s'écrit au premier lancement sous un nom autre que le défaut, puis à chaque changement ; l'écran affiche le nom à chaque lancement.
8. **Script v3 et code 2 (mineur) : corrigé.**
   - Script v4, en-tête refait : moteurs v8m, v8p, v8r ; `--cle-gemini` avec le v8r seulement ; `--reprise` pour un dossier commencé sous v8m.
   - La voie v8 refuse `--cle-gemini`, sous ses deux formes, avec v8m, v8p et essaim, par un arrêt nommé au code 1, avant tout chargement.
9. **Voie sans essais (mineur) : corrigé.**
   - `test_voie_abonnement_v8.py`, 5 sur 5 :
     - table des moteurs (v8r à son empreinte, v8q absent) ;
     - refus d'une copie modifiée ;
     - devis identique, octet pour octet, entre la voie v6 avec le v8m et la voie v8 avec le v8r ;
     - refus de `GEMINI_API_KEY_3` à travers la voie, dans le même processus, transport coupé, zéro requête ;
     - refus de `--cle-gemini` hors du v8r.
   - Je n'ai pas copié les essais de la v6, qui sont sur la branche des courses : seuls les changements de la v8 sont éprouvés ici.
10. **Commandes autres que v8r (mineur) : déclaré**, dans l'en-tête de la voie v8 et dans celui du script v4. Par la voie, v8m, v8p et l'essaim gardent la clé de Google sous son nom fixe.
11. **Docstring des essais (mineur) : corrigée.** Les essais se relancent dans un environnement vidé et ne lisent donc aucune valeur réelle. La docstring dit exactement ce qui est fait.

## Remarques reprises
- Le défaut reste `GEMINI_API_KEY`, la clé dont le crédit est épuisé. Une vague lancée sans `--cle-gemini` retrouvera le refus 402, qui est un échec sans coût. Le script v4 n'exige pas l'option : à la mère de dire s'il doit l'exiger avec le v8r.
- `declarer_cle_gemini` prend le seul nom de la composition. Un seul nom vaut pour toutes les espèces de Google ; à revoir si l'on passe un jour à un nom par espèce.

## Commandes de contrôle (sans réseau)
```
PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/test_collisionneur_v9_v8r.py
PYTHONPATH=src python3 -B docs/notes/collisionneur-v9/abonnement-v1/test_voie_abonnement_v8.py
env -i PATH="$PATH" HOME="$HOME" PYTHONPATH=src ESSAIS_V8R_ENVIRONNEMENT_VIDE=1 python3 -B docs/notes/collisionneur-v9/mutations_collisionneur_v9_v8r.py DOSSIER_TEMPORAIRE
```
