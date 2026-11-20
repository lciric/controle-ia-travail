# Rapport du développeur — vérification X6 contre le fichier des cartes — v1

Pièce de travail (classe C). Mandat : `mandat-developpeur-verification-x6-fiches-v1.md` (sha256 9e2b80a1eb12ccd0dab05cc3ea87d3fdef3e45d44bd16ebe4d9f57ba8900e32e, vérifié par son compagnon : OK).

## Fichiers (bloc-notes `dev-verification-x6/`)

| Fichier | sha256 |
|---|---|
| `verifier_x6_contre_fiches_v1.py` | d8f84db2538446727474bbbb365c70096388d602b11693dabeb84dda6964dd96 |
| `essais_verifier_x6_contre_fiches_v1.py` | d57a8f924d1721ba7c88ed1c22d93e40a41634fb1d8345759faf8026f12fb753 |

Chaque fichier a son compagnon `.sha256`. Le dossier `essais-fichiers/` contient les seuls fichiers synthétiques des essais (jetables).

## Programme

- Bibliothèque standard seulement ; arguments `--fiches`, `--extraction`, `--sortie`, obligatoires, sans défaut, sans abréviation, sans `--help` ; toute autre option est refusée (code 2, motif sans écho des arguments).
- Empreintes gelées : `fiches` = ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481 ; `extraction` = f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb (empreinte entière transmise par la session, lue par elle dans le compagnon sur main ; je ne l'ai pas relue moi-même).
- Ordre : refus si la sortie ou son compagnon existe ; lecture des octets ; empreintes sur ces octets ; refus si l'une diffère ; décodage de ces mêmes octets seulement ensuite.
- `fiches` : décodé avec un crochet qui jette chaque valeur au décodage et ne garde que les clés ; refus si la racine n'est pas un objet, si une clé est en double, si le JSON est illisible.
- `extraction` : seule `identifiants_par_classe.a_corriger` est lue ; refus si elle ne compte pas exactement deux chaînes distinctes.
- Sortie : JSON à trois champs exactement (`nombre_de_cles`, `retenues_presentes` dans l'ordre de l'extraction, `empreintes` {`fiches`, `extraction`}), contrôlés avant écriture ; écriture en mode exclusif ; compagnon `.sha256` au format `sha256sum`. Écran : « FAIT » ou « REFUS : motif » ; aucun motif ne contient un identifiant ni une valeur ; toute erreur inattendue donne « REFUS : erreur inattendue ».
- Aucune option d'empreintes d'essai : les essais importent le module et appellent `executer(...)` avec des empreintes en paramètre, ou remplacent les constantes du module par `monkeypatch` ; `principal()` passe toujours les constantes gelées.

## Essais

Commande : `env -C …/dev-verification-x6 python3 -B -m pytest -q -p no:cacheprovider essais_verifier_x6_contre_fiches_v1.py` — **33 passés, 0 échoué** (Python 3.13.18).

Couverts : cas sain (94 clés, deux retenues absentes, compagnon vérifié par `sha256sum -c`) ; retenue présente (dans l'ordre, et ordre inverse) ; empreinte fausse de chaque fichier, sans sortie ; empreinte vérifiée avant tout décodage ; fiches illisibles, racine non objet, clé en double ; extraction à zéro, une, trois retenues, doublon, non-chaîne, `a_corriger` absente ; sortie ou compagnon existant, laissé intact ; clé de plus dans la sortie impossible (refus, rien écrit) ; trois champs exactement ; aucun identifiant ni valeur dans la sortie, le compagnon, l'écran (succès, cinq refus, arguments invalides) ; constantes gelées ; trois options seulement dans le source ; options d'empreinte refusées en ligne de commande ; la ligne de commande refuse les fichiers synthétiques (empreintes gelées), sans sortie.

## Commande unique de jeu

```
python3 -B verifier_x6_contre_fiches_v1.py --fiches CHEMIN_DES_CARTES --extraction CHEMIN_DE_sortie-extraction-x6-v2.json --sortie CHEMIN_NEUF.json
```

## Écarts et refus

Aucun refus de permission, de classifieur ou de garde. Aucun accès au vrai fichier des cartes ni à `archives-reponses-modeles/`. Aucune écriture dans le dépôt, aucun commit. Écart mineur : le nom de fichier des essais ne suit pas le motif `test_*.py`, il faut donc le nommer dans la commande pytest (fait ci-dessus).

Développeur, modèle L′.
