# Vérification courte — portée des décisions de l'organisme, v2

Auteur : modèle C ; vérificateur : modèle D ; C ≠ D. Écrit le Sat Nov 14 09:49:32 UTC 2026 (heure lue par `date -u` dans la commande qui écrit ce fichier). Rejeu du programme lancé le Sat Nov 14 09:48:00 UTC 2026 (heure rendue par `date -u` dans la commande du rejeu).

**Verdict (une ligne) : recevable avec une réserve — le rejeu est identique à l'octet, le décompte égale la table, les 14 constats ont une réponse et les cinq nœuds sont au format ; mais six articles classés « organisme d'idéation (par inférence écrite) » (N-058.1, .2, .4, .5 ; N-059.5, .6) n'ont aucun nœud, alors que leurs décisions n'écrivent pas « organisme d'idéation ».**

## Ce qui a été lu et fait

- Lus entiers : `critique-portee-decisions-v1.md`, `portee-decisions-organisme-v2.md`, `compter_articles_decisions_v2.py`. Lu par programme : `articles-decisions-v2.json` et `articles-decisions-v1.json` (comparaison). `portee-decisions-organisme-v1.md` n'a pas été relu en entier : je ne m'appuie sur lui pour aucun constat.
- Décisions relues (fichiers nommés sous `docs/decisions/`) : N-052, N-058, N-059, N-065 en entier ; N-044 et N-045 v2 aux sections d'articles ; N-045 v1 lignes 9-14 et 70-80 ; titres de section des neuf fichiers. N-049 et N-050 : titres et début des sections exclues seulement.
- Rejeu : copie du programme dans un dossier provisoire neuf (`/tmp/claude-0/-home-user-ideation-organism/a931cfdf-f0bc-5d82-9b93-b9a1d86a5bbd/scratchpad/verif-portee-v2/prog/`), exécution `python3 -I -B` avec `--sortie …/verif-portee-v2/sortie`. Rien n'est réécrit dans le dépôt.
- Non lus : le document de l'affinage v2 cité par N-059, la page v7, le catalogue, la question et la conception de la course. Aucune recherche dans un arbre. Aucun refus de permission rencontré.

## Constats

**1. Sortie égale à l'octet (conforme).** Le JSON rejoué a l'empreinte `ba2124f3293a06a936f134c0611f7594a92ea24cebf64a4c38cc9645dbd48432`, celle du fichier scellé ; `cmp` : identiques. Les trois empreintes recalculées (`991e73a1…`, `ba2124f3…`, `6db5d45e…`) égalent les compagnons `.sha256`.

**2. Décompte égal à la table (conforme).** Totaux du rejeu : N-044 7 ; N-045 v1 9 ; N-045 v2 12 ; N-049 3 ; N-050 3 ; N-052 5 ; N-058 5 ; N-059 16 ; N-065 5 ; total 65, en vigueur 56. Les 65 lignes de `--table` sont identiques aux lignes 39-103 du document (`diff` vide). Les 13 lignes de `--totaux` sont identiques aux lignes 107-119 (`diff` vide). `--verifier-md` : aucun identifiant manquant ni en double. Objets en vigueur : 4 / 9 / 26 / 3 / 3 / 1 / 2 / 8, comme au § 0.

**3. Les 50 articles de la v1 sont intacts (conforme).** Comparaison des deux JSON sur identifiant, texte, ligne et ligne de fin : aucune différence. Quinze identifiants neufs : N-044.6, .7 ; N-045v1.6 à .9 ; N-045v2.9 à .12 ; N-052.0 ; N-058.4, .5 ; N-059.0 ; N-065.5. Types : 42 points numérotés, 15 puces, 6 paragraphes, 2 amorces.

**4. Chaque constat de la critique a une réponse (conforme).** Le § 3 répond aux 14, un par un, avec des lignes. Contrôlé sur les textes : constat 4 (N-044 l. 58-59 et N-065 l. 28-29 sont maintenant des articles) ; constat 5 (N-045 v2 l. 115-117 dans N-045v2.12 ; N-058 l. 36-39 dans N-058.4 et .5 ; N-052 l. 29 dans N-052.0) ; constats 6 et 7 (N-045v2.1 à .3 en « lignée conv-audit seulement », base S, critère R-c écrit une fois) ; constat 8 (nœud 3 scindé en 3a, 3b, 3c) ; constat 10 (les quatre reclassements faits) ; constat 11 (phrase de la Portée de la v1, lignes 12-13, absente de la v2 : exact ; mots de 09:35 aux lignes 23-24 de la v2 : exact) ; constat 12 (plus de ligne de sortie sous la table). Les trois refus partiels (constats 6, 8, 9) sont fondés sur une ligne citée ; celui du constat 9 tient : N-065 l. 20 dit « jamais une preuve », N-044 l. 48 dit « jamais une consigne ».

**5. Réserve : six portées par inférence sans nœud.** Aucune phrase de N-058 ni de N-059 n'écrit « organisme d'idéation » (relecture des deux fichiers entiers ; le § 1 du document le dit lui-même). Neuf articles sont pourtant classés « organisme d'idéation (par inférence écrite) ». Le nœud 3b demande la ratification pour N-059.1, .11, .14 (et .15). Les six autres — N-058.1, .2, .4, .5 et N-059.5, .6 — ont « — » dans la colonne nœud et le statut « retenu ». Le § 1 écrit que Lazar « peut défaire » la chaîne I1, mais aucun nœud du § 6 ne la lui soumet pour ces six articles. La chaîne est sérieuse (N-058 l. 29-30, « prise « idéation » » ; « fiches » aux l. 22 et 38 ; N-065 l. 19-20, « ses fiches » ; N-065 l. 16, « Son juge statistique »), mais c'est une inférence de l'auteur sur un texte muet. Correction demandée dans une v3 : un nœud au même format (« ratifier I1 pour N-058.1, .2, .4, .5 et N-059.5, .6 ? »), ou l'extension du nœud 3b à ces six articles. La critique v1 (constat 10) demandait seulement que l'inférence soit écrite : c'est fait ; la réserve vient de la règle « portée sur texte muet = nœud ».

**6. Pas d'autre portée affirmée sur un texte muet.** Les huit articles « portée à établir » sont au nœud 3a ; N-059.12 et .13 au nœud 3c ; N-059.15 aux nœuds 3b et 3c ; N-044.4 et N-065.2 au nœud 2 ; N-045v2.1 à .3 au nœud 1. « Lignée conv-audit seulement » est défini comme une étiquette, non comme une exclusion (§ 1, R-c ; § 7). Rien n'est déclaré « libre ». Le verdict « occupée en partie » n'est pas contredit.

**7. Nœuds au format demandé (conforme).** Les cinq nœuds (1, 2, 3a, 3b, 3c) portent chacun : la décision en question, l'enjeu avec lignes, des options avec avantage et inconvénient (trois options, deux pour 3c), une recommandation et une confiance chiffrée (55 %, 60 %, 70 %, 55 %, 80 %). Les articles de chaque nœud dans le document égalent la colonne « nœud » du JSON.

**8. Limite dans l'enjeu du nœud 1 (à dire à Lazar).** La phrase « La course « conception propre » applique déjà ces leviers à l'organisme d'idéation » vient du § 4 de la v1, non revérifié par l'auteur ni par la critique ni par moi (pièces hors lecture). Le § 5 le dit ; l'enjeu du nœud 1 et celui du nœud 2 ne le redisent pas à l'endroit où Lazar lira.

**9. Écarts mineurs, sans effet sur les comptes.**
- § 4, dernière ligne : « 72-77 de la v1 ». Les deux puces sont aux lignes 73-78 de la v1 (table : N-045v1.6 73-76, N-045v1.7 77-78).
- Nature de N-044.7 : « conséquence », parce que sa section s'intitule « Ce que cela change, et ce que cela ne change pas » ; le même contenu (« Ne change pas : … ») est « borne » pour N-065.5. Le reste du constat 4 de la critique subsiste donc dans la colonne « nature », pas dans le décompte.
- Base « T » pour N-065.3 et N-052.0, .1, .3 : l'objet vient du titre de la décision ou de la section, pas d'une phrase de l'article ; selon le § 1 ce serait « S ». Le classement ne change pas.
- § 1, chaîne I1 : « son juge statistique » est cité « lignes 16-17 » ; le texte est « Son juge statistique », ligne 16.

**10. Masque (conforme).** Recherche des noms de la famille de l'assistant dans les trois fichiers nommés de l'auteur : zéro occurrence.

## Limites de cette vérification

- Le classement reste un jugement de l'auteur (§ 1 du document) : j'ai contrôlé les articles de N-058, N-059, N-065, N-052, N-044 et N-045 v2 contre leur texte, pas ceux de N-049 et N-050.
- Le § 5 du document (page v7, catalogue) n'est pas vérifié.
- Je n'ai rien modifié ; ce fichier est le seul écrit dans le dépôt, il n'est pas poussé.
