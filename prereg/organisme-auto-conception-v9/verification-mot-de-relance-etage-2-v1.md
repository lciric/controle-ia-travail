# Vérification du mot de relance de l'étage 2 de la ligne 3 — v1

Vérificateur neuf (Opus 5.5), non auteur, le 2026-11-21. Pièce vérifiée : `prereg/organisme-auto-conception-v9/mot-de-relance-etage-2-ligne-3-v1.md` (non scellée, non commitée, 5 453 octets, lue à 09:47Z de modification). Références : mot de départ v2 (`mot-de-depart-etage-2-ligne-3-v2.md`, recalculé `c89ec85b244d4b3e82e82acb0dd16b24feec75dc81cc5be9d755c2cd28faea79`, égal au compagnon) ; additif 6 v2 (`additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`, recalculé `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01`, égal au compagnon), geste 9 (l. 214 à 216), § 8, § 9 (l. 319), § 11 n° 10 ; `registres/decisions.md`, R-4376, R-4440, R-4470 à R-4472, R-4496 ; `registres/go.md`, GO-2026-11-20-68 ; code d'appel v4, compteur (l. 619 à 700) et sortie (l. 1436 à 1448). Aucun appel payant, rien lu sous les chemins cloisonnés.

## Verdict : À corriger (deux corrections exigées, deux recommandées)

## 1. Commandes, par programme

- Extraction des blocs de commande des deux mots (python, expression régulière sur les blocs délimités) : deux blocs dans chacun, une ligne chacun.
- Contrôle du mandataire : identique au mot de départ v2, caractère pour caractère (égalité de chaînes vraie).
- Geste 9 : après les deux seuls remplacements `declaration-relais-ligne-3-etage-2-v1.json` → `…-v2.json` et `58cec5678b174d2929e50b22be9c13514316d8a4e308fb75c5c129ed794be376` → `5617d47adf71d0b4e3c2197b5211aeea63ecc5fa2673ec8a792331dd78c69664` appliqués au mot de départ v2, égalité de chaînes vraie ; `diff` des blocs : une seule ligne diffère, aux deux seuls endroits ; longueurs égales (1 129 caractères).
- `setsid`, `nohup`, redirection, `&` et fichier d'identifiant : absents des deux blocs, présents dans la prose seule. **Tenu.**
- Non vérifiable d'ici : la déclaration v2 et son empreinte (le dossier `/home/user/relais-ligne-3-etage-2-portee-200-v1` n'existe pas sur cette machine) ; l'empreinte 5617d47a… est reprise de R-4496 ; le pas 1 de l'exécutant la vérifie au compagnon.

## 2. Conformité à l'additif 6 et au mot de départ v2

Tenu : relais neufs aux mêmes ports (8787, 8788) ; fichiers et déclaration de rang 2 (l. 214 : « `…-v2.json` à la première relance ») ; même `S`, même banque (`HEX_BANQUE` 70d35e54…), mêmes témoins `t01,t07` dans cet ordre ; compteur repris, jamais remis à zéro ; relance écrite au manifeste (exécution K + 1) ; relais Argon borné à 2 410 ; panne et non arrêt écrit (code 3), donc relance permise (l. 216) ; relance sur le mot de la mère (mot de départ v2, pas 5) ; relevé et arrêt des relais de rang 1 faits (R-4471) ; mot de Lazar cité (R-4496) ; GO-2026-11-20-68 valide jusqu'au 2026-11-27, montant égal à `PLAFOND_C`. Rien ne contredit le mot de départ v2, hors les deux points ci-dessous.

## 3. Plafond du relais et relevés

Le plafond de 88,36 n'est pas un écart à l'additif : c'en est la lettre (§ 9, l. 319 : « le plafond du relais du juge Opus reste 88,36 USD (§ 11, n° 10) ») ; c'est un écart à l'option (a) de R-4471 et à la seconde défense, que le § 11, n° 10 dit perdue. Les relevés avant le lancement (pas 2) et à mi-course (pas 6) sont prévus. Mais deux phrases sont fausses sur le compteur : celui-ci relit son propre journal, qui porte le cumul compté des deux juges (envois non relevés à 0,60, engagements orphelins à 0,60), non la dépense du seul relais Claude ; à 08:07Z ce cumul valait 15,61 USD pour 11,44 relevés au relais Claude (R-4440). Il ne « reprend » donc pas « à 18,848097 », et la lecture du pas 6, qui ajoute 18,848097 au cumul compté, compte deux fois la dépense d'avant la panne : en fin de course normale (cumul compté proche de 87,77, § 8) elle crierait au dépassement sur un cas sain (R5), et elle ne contrôle pas ce qu'il faut contrôler, que le compteur ne compte jamais moins que la dépense réelle du juge Opus.

## 4. Clés, courriels, noms

Aucune valeur de clé ni de jeton (recherche par motifs), aucun courriel. « Lazar » (citation du mot) et « Luc » (dans le nom de variable `RR_ANTHROPIC_API_KEY_LUC`, argument du programme local, jamais servi aux juges) figurent déjà dans le mot de départ v2 scellé. Rien n'est servi à un fournisseur hors de la banque scellée. **Tenu.**

## Corrections

1. **Exigée.** Remplacer :
   « écart accepté par la mère, R-4472 : le relais neuf repart de zéro, la garde de la ligne est le compteur du programme, qui reprend son journal à 18,848097 USD) »
   par :
   « écart accepté par la mère, R-4472, à l'option (a) de R-4471 mais à la lettre de l'additif 6, § 9 et § 11, n° 10 : le relais neuf repart de zéro, son plafond ne borne donc plus la dépense de la ligne sur la clé Claude (au pire 18,848097 + 88,36 = 107,208097 USD si le compteur faillait) ; la seule garde de la ligne est le compteur du programme, qui relit son journal et reprend à son propre cumul compté, les deux juges compris, qui doit être au moins égal aux 18,848097 USD relevés au relais Claude de rang 1) »

2. **Exigée.** Au pas 6, remplacer :
   « cumul compté par le programme plus 18,848097 doit rester sous 88,36. »
   par :
   « deux lectures : le cumul compté par le programme, relu à son journal, dépense d'avant la panne comprise (ne rien lui ajouter), reste sous 88,36 ; la dépense du relais Claude de rang 2 plus 18,848097 ne dépasse pas ce cumul compté (le compteur ne compte jamais moins que la dépense réelle du juge Opus). Un écart à la seconde lecture est rendu à la mère sur-le-champ. Mêmes deux lectures au relevé de fin (pas 7). »

3. **Recommandée** (le lancement détaché ne rend pas le code de sortie). Au pas 5, remplacer :
   « identifiant de processus écrit dans un fichier, suivi par ce seul identifiant (R10), jamais par motif : »
   par :
   « identifiant de processus (`$!`) écrit dans un fichier et vérifié par `stat -c %n /proc/<identifiant>` et `/proc/<identifiant>/cmdline` (l'interpréteur et le code d'appel), suivi par ce seul identifiant (R10), jamais par motif ; le code se lit à la seule ligne, écrite au journal : ligne `refus`, 2 ; `arret` nul, 0 ; `arret` nommé, 3 ; processus mort sans ligne, panne : »

4. **Recommandée.** Au pas 1, remplacer :
   « Pas 1 du mot de départ v2, à l'identique, avec la déclaration v2 »
   par :
   « Pas 1 du mot de départ v2, à l'identique, plus ce mot de relance et son compagnon, avec la déclaration v2 »
