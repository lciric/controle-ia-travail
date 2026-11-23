# Contre-lecture neuve du brouillon 56 du préenregistrement des organismes discrets, bras A

Contre-lecteur neuf (Claude Opus 5.5, n'a écrit ni le brouillon 56, ni le code, ni la note, ni leur contre-lecture), 23 novembre 2026, processeur seul, sans réseau hors poussage git, sans dépense. Aucun chemin cloisonné ouvert, listé ni empreinté ; `registres/` non ouvert (la portée de GO-2026-11-22-145 n'est donc pas vérifiée ici).

## Verdict : scellable

Le brouillon 56 ne diffère du brouillon 55 que par les trois lignes annoncées, par ajout ou remplacement local ; toutes les empreintes citées sont exactes ; l'ajout est fidèle à la note et à la contre-lecture ; il ne change aucune règle, aucun seuil, aucune issue ; la seule marque restante est l'entier racine de la case « entropie ». Trois défauts mineurs, non bloquants, ci-dessous.

## 1. Différence entre les brouillons 55 et 56, par programme

Brouillon 55 : `cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1` ; brouillon 56 : `561723f15bd777a315aedb561a4cfa406aabdefed4d34548a7432aee535bb012` (confirmées). Même nombre de lignes (2554). Comparaison ligne à ligne puis mot à mot (`difflib.SequenceMatcher` sur les mots) : seules les lignes 1, 3 et 1481 diffèrent.

- **Ligne 1 (titre)** : remplacement `55` → `56`, rien d'autre.
- **Ligne 3 (statut)** : remplacement `55,` → `56,` ; insertion d'une phrase : « Le brouillon 56 porte une inscription seulement, faite par la session de relance sur le mot de la session mère (option (a′), deuxième étage de la chaîne de décision, confiance 0,7) : dans la case « commit du code de l'instrument et de l'analyse » de 13.1, le programme de l'aire conditionnelle, la garde statique du cloisonnement en version 14 et le programme d'enchaînement en version 3, avec leurs empreintes, la preuve de la différence et la contre-lecture ; le code arrêté n'est pas changé ; aucune règle, aucun seuil, aucune issue changés ; reste ouvert l'entier racine de la case « entropie », tiré au scellement. »
- **Ligne 1481 (13.1, case du commit du code)** : une seule insertion, à la fin de la case, commençant par « ; **ajout du brouillon 56 (mot de la session mère, option (a′))** : … » et finissant par « … la réserve de l'épreuve faite sur une livraison fabriquée va au dossier de course ». Aucun mot antérieur de la case n'est retiré ni changé.

## 2. Chemins et empreintes cités dans l'ajout

Tous les fichiers existent ; `sha256sum` :

| fichier | cité | calculé |
|---|---|---|
| `src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py` | `0f1e7640…6df2` (entière) | identique |
| `src/controle_ia/organismes_discrets/analyse_bras_a_v13.py` | `a7ebf29f…` (abrégée) | `a7ebf29f653d…46cf`, accord |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v14.py` | `44e84972…d7f6` (entière) | identique |
| `docs/notes/relance-organismes-discrets-v1/preuve-difference-garde-v14-v1.py` | `b9787b1d…c0ec` (entière) | identique |
| `src/controle_ia/organismes_discrets/enchainement_discretion_bras_a_v3.py` | `05126df3…410c` (entière) | identique |
| `src/controle_ia/organismes_discrets/enchainement_discretion_bras_a_v2.py` | `3b3c3a8b…` (abrégée) | `3b3c3a8be039…ea0a`, accord |
| `docs/notes/relance-organismes-discrets-v1/difference-enchainement-v2-v3-v1.diff` | `7618b8ca…04f6` (entière) | identique |
| `docs/notes/relance-organismes-discrets-v1/aire-conditionnelle-bras-a-v1-note.md` | `65c95e58…522e` (entière) | identique |
| `docs/notes/relance-organismes-discrets-v1/contre-lecture-aire-conditionnelle-bras-a-v1.md` | `362d29f5…8c54` (entière) | identique |

Compagnons `.sha256` présents pour les quatre pièces de notes.

## 3. Fidélité à la note et à la contre-lecture

- **Composition sans calcul propre** : fidèle (note, « Ce que fait le programme », points 1 à 3 ; contre-lecture, point 1 : « aucun calcul propre »). La double vérification de l'empreinte de l'analyse (avant et après l'import) est dans la note, point 1. L'import de `controle_ia.gardes` est déclaré, conformément à la réserve R-a de la contre-lecture.
- **Différence de la garde v14** : fidèle — un chemin ajouté aux programmes de l'aire conditionnelle, la garde v14 ajoutée aux gardes statiques (nécessaire, sinon elle se refuse), l'en-tête ; « preuve tenue » est la sortie de la preuve citée dans la note et confirmée par la contre-lecture (point 2).
- **Différence de l'enchaînement v3** : fidèle en substance. Le `diff` v2/v3 (refait ici) montre l'en-tête, l'import de `cloisonnement_bras_a_v14`, `MODULE` et, dans `MODULES_JOUES`, `cloisonnement_bras_a_v13` devenu `…v14`. L'ajout range cette quatrième différence sous « la garde de la version 14 », ce qui se défend (l'en-tête de la v3 dit « la garde statique importée et relevée ») ; voir défaut m-2.
- **112 essais** : fidèle à la contre-lecture (point 3 : 112 réussis, 0 échec, sur les trois fichiers d'essai par les enchaînements v2 et v3). La note de l'auteur, antérieure à la v3, en comptait 11 ; le chiffre cité est bien celui de la contre-lecture.
- **Verdict « conforme » et deux réserves mineures** : fidèle (« conforme, avec deux réserves mineures »). Le modèle du contre-lecteur (« Claude Sonnet ») n'est pas écrit dans le fichier de la contre-lecture : non vérifiable ici (défaut m-3).
- **Livraison fabriquée** : fidèle (note, « Essais » : livraison fabriquée, entropie fictive déclarée telle `ENTROPIE_FICTIVE = 20261122`) ; l'envoi de la réserve au dossier de course est une décision de l'inscription, non une affirmation sur les sources.

## 4. Règles, seuils, issues ; cohérence avec 13.2 et les mentions de la v13

- L'ajout ne touche à aucune règle, aucun seuil, aucune issue : il nomme des programmes hors du code arrêté, leurs empreintes, leurs preuves et leurs essais. Le code arrêté reste la version 13 (analyse, verdicts, garde), et les mentions de `cloisonnement_bras_a_v13.py` (ligne 157, table des pièces ; ligne 1481, « Trois modules en version 13 ») restent vraies : la garde v13 demeure du code arrêté, la v14 est hors du code arrêté et sert la garde du dépôt. Pas de contradiction. Les autres « v13 » (lignes 3, 153 à 156, 1481, 2381) désignent la note, la vérification et les modules de la version 13 : aucune ne fait de la garde v13 la garde en vigueur pour l'enchaînement.
- **13.2, ligne du programme d'enchaînement** : elle dit « écrit par le rédacteur du code de la relance, Claude Fable 5.2 … ; contre-lu par un agent neuf d'un autre modèle, Claude Opus 5.5 ». L'ajout dit la v3 écrite par Claude Opus 5.5 « (substitution accordée, GO-2026-11-22-145) » et contre-lue par Claude Sonnet. L'exigence de fond de 13.2 (contre-lecteur neuf d'un autre modèle que le rédacteur) est tenue. La lettre de 13.2 (noms des modèles) ne l'est pas, et le GO n'apparaît qu'à cet endroit du texte ; sa portée n'est pas vérifiable depuis cette contre-lecture (`registres/` cloisonné ici). **Suffisant**, à condition que GO-2026-11-22-145 couvre bien l'écriture de l'enchaînement (et de ses versions) par Claude Opus 5.5 et, par suite, le contre-lecteur d'un troisième modèle ; à vérifier par la session au registre des GO avant scellement (défaut m-1).

## 5. Marques restantes

`controle_ia.prereg.problemes(brouillon 56)` rend une seule entrée : « marqueur À REMPLIR restant hors des sections exigées ». Une seule occurrence de « À REMPLIR » dans le fichier, ligne 1475, case « entropie », pour l'entier racine. Même compte au brouillon 55. Conforme.

## Défauts, classés

Bloquants : aucun.

Mineurs (non bloquants) :
- **m-1** — 13.2 nomme toujours Claude Fable 5.2 rédacteur et Claude Opus 5.5 contre-lecteur du programme d'enchaînement ; la substitution n'est portée que par le renvoi à GO-2026-11-22-145 dans 13.1. Vérifier la portée du GO au registre ; facultatif : un renvoi d'une demi-ligne en 13.2 au brouillon suivant.
- **m-2** — « ne diffère de la version 2 que par la garde de la version 14, son nom de module et son en-tête » : la quatrième différence (`MODULES_JOUES`, relevé de la garde jouée) n'est nommée que par le rattachement à « la garde » ; le diff scellé la montre. Exact en substance.
- **m-3** — Le modèle « Claude Sonnet » attribué au contre-lecteur n'est pas écrit dans la contre-lecture citée ; la réserve 2 de la note de l'auteur (essais « garde passée sur le dépôt » des gardes v6 à v13 désormais en échec) n'est pas reprise par l'ajout ; ni l'un ni l'autre ne touche l'analyse.
