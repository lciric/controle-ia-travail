# Vérification du mot de départ de l'étage 2 de la ligne 3 — v1

Vérificateur neuf (Opus 5.5), qui n'a écrit ni le mot de départ ni l'additif. 2026-11-21, 06:50Z (`date -u`). Classe A (ordre d'une course payante, GO-2026-11-20-68, 88,36 USD au plus).

## Verdict : À corriger (deux corrections exigées, trois recommandées)

La commande du geste 9 est identique à celle de l'additif, aux quatre remplacements permis près (contrôle par programme, § 2). Toutes les valeurs citées sont justes. Deux écarts à corriger avant le scellement : l'arrêt des relais est repoussé au geste 13 alors que l'additif le place à la fin du geste 9, avec un relevé que le mot omet (correction 1) ; la vérification « Conforme » de la version 3 n'est pas citée par sa pièce (correction 2).

## 0. Pièces lues et empreintes recalculées

| pièce | sha256 recalculé | constat |
|---|---|---|
| mot de départ v1 (non scellé), `prereg/organisme-auto-conception-v9/mot-de-depart-etage-2-ligne-3-v1.md` | — | lu en entier |
| additif 6 v2, même dossier | `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01` | égal au compagnon ; lu en entier |
| pièce de scellement de la banque v1, même dossier | `c91c4d338c4a524595df96c45711e0b6094e07afa438d30bc6f79b6ce78856d7` | égal au compagnon ; HEX_BANQUE `70d35e54…4bbd` |
| `registres/scellements-v1.md`, dernière ligne | — | `BANQUE-ETAGE-2-LIGNE-3-V1`, 06:37:05Z, `c91c4d33…56d7` |
| `etalonnage-lecture-v3/etalonner_ligne_3_v3.py`, `lire_ligne_3_v3.py` | `d41533cb…1150`, `c09f4743…13b4` | égaux à l'additif, § 2.1 |
| `etalonnage-lecture-v3/verification-v1/verification-etalonnage-lecture-etage-2-v3-v1.md` | `c5119f0459fbdedbdfb64c0d28bfca685b85c99b9557b2ceab198edb658b8582` | « CONFORME », 49 passés |
| manifeste du lancement des relais, `…/etage-2-portee-200-v1/relais-geste-8-v1/manifeste-relais-etage-2-v1.md`, branche `lot/compte-organisme-v1` (commit b68ff378), par `git show` | `4d877381ff7fe6e947b1997bcc9e5b283ac166637a2c0b6116ce69ff4934d09a` | égal au compagnon ; PID 7533 et 7563, déclaration `58cec567…e376` |
| programme de contrôle du mandataire, `…/controle-mandataire-v1/controler_mandataire_etage_2_v1.py`, tête distante de `lot/compte-organisme-v1` `9555d8b6`, par l'interface de GitHub (aucun `fetch`) | `60523f210e40c20709188f048a567a7eb14053b6e75ade9cdb919d7bbb04bd39` | égal au compagnon ; codes 0 « tenu », 3 refus |
| contre-lecture de ce programme, `…/contre-lecture-v1/contre-lecture-controle-mandataire-v1.md` | `a51027344110e3fd42c1c248e4a943f0fa0befe3068d63540a85ea016850a06f` | égal au compagnon ; « Conforme » |
| `registres/go.md` | — | GO-2026-11-20-64 et GO-2026-11-20-68 |
| `registres/decisions.md` | — | R-4289, R-4293, R-4305, R-4325, R-4326, R-4367, R-4368, R-4373, R-4375 |
| `registres/depenses.md` | — | aucune dépense inscrite sur la clé Luc après la sonde de 0,000002 USD (R-4091) |

La déclaration elle-même et les relais ne sont pas dans ce conteneur (`/home/user/relais-ligne-3-etage-2-portee-200-v1/` absent) : leur empreinte et leurs processus ne sont contrôlés que par le manifeste de l'organisme et par le pas 1 du mot. Le contrôle reste celui de l'exécutant.

## 1. Ce que le geste 8 exige d'être cité

| exigence (geste 8, § 9) | dans le mot | constat |
|---|---|---|
| additif scellé, `CHEMIN`, `HEX` | l. 7 | juste ; `HEX` recalculé égal |
| ligne de scellement de la banque, `HEX_BANQUE` | l. 8 | juste (ligne, pièce, empreinte de la pièce, HEX_BANQUE) |
| vérification « Conforme » de la version 3 de l'étalonnage et de la lecture | l. 9 | empreintes des deux programmes justes, 49 passés juste ; **la pièce de vérification n'est citée ni par son chemin ni par son empreinte** (correction 2) |
| relevé des soldes par clé, par nom seulement | l. 10 | clé Luc : 213,999998 USD, sans relevé possible (R-4305), juste ; aucune dépense depuis, vérifié ; réserve 88,36 sur la part de Luc (R-4289, R-4293 (b)), juste. Clé Google : GO-2026-11-20-64, comme le § 9 ; le nom de la clé n'est pas dans cette ligne (recommandation 5) |
| témoins de plomberie `t01,t07` | l. 11 | juste, ordre dit (R-4326) |
| déclaration et son empreinte, selon le § 9 | l. 12 | chemin de rang 1 juste ; `58cec567…e376` égal au manifeste de l'organisme ; PID, ports, plafond, borne d'Argon égaux à R-4373 et au manifeste |
| confirmation du nom de la variable de la clé Google | l. 13 | `GEMINI_API_KEY`, juste (R-4368) ; le mot renvoie à GO-2026-11-20-64, l'additif à GO-2026-11-20-68 ; la confirmation est inscrite en R-4368 (recommandation 5) |

Aucune valeur fausse relevée.

## 2. Commande du geste 9 : contrôle par programme

Méthode 1 (python) : la ligne `env -i …` de l'additif (l. 211) découpée en mots ; chaque mot commençant par `E/` reçoit `E` développé (`/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1`, définition du § 0) ; `HEX_BANQUE`, `DECLARATION`, `HEX_DECLARATION` remplacés mot pour mot par les valeurs du mot. Remplacements faits : `E/` deux fois, les trois autres une fois chacun. Résultat comparé à la ligne `env -i …` du mot : **identique**, 1 129 caractères de part et d'autre, aucun caractère hors ASCII imprimable dans l'une ou l'autre.

Méthode 2 (sed et diff) : mêmes remplacements par `sed`, sortie comparée par `diff` : **aucune différence** ; empreinte commune des deux lignes `48c9cc6ed55bade89a1f7a1a4057eea9598fb40be57ecc92865a12fdc19a718c`.

La ligne `git -C /home/user/controle-ia-travail fetch origin main` est reprise à la lettre au pas 3, juste avant.

## 3. Règles de l'additif

Tenues : codes 0, 2, 3 ; arrêt de plomberie et ses deux causes ; aucune relance après le code 3 ; relance avec relais relancés et déclaration de rang suivant ; lecture non ouverte avant le geste 12 ; seule la ligne imprimée rendue ; arrêt par identifiant de processus (R10). « Relance seulement sur un mot de la mère » est plus strict que l'additif et ne le contredit pas.

Écart : **pas 6, « Les relais restent vivants jusqu'au geste 13 »**. L'additif place l'arrêt à la fin du geste 9 (puce « À la fin : relais arrêtés par identifiant de processus », dans le geste 9) et le § 9 exige, à la fin, « même relevé, même arrêt, consignés au registre des arrêts » : relevé `/relais/etat` (procédure écrite, § 5), puis arrêt (§ 6). Les gestes 10 à 13 n'appellent aucun fournisseur ; une relance demande de toute façon des relais neufs. Garder deux relais porteurs de clés vivants pendant l'étalonnage, l'audit, la lecture et le verdict n'a pas d'usage et contredit la place de l'arrêt dans l'additif ; le relevé est omis (correction 1).

Omission sans contradiction : le refus (code 2) « revient à la mère ; aucun argument n'est changé pour le lever » (§ 6, en tête) n'est pas repris (recommandation 4).

## 4. Contrôle du mandataire

Demandé au pas 2, « sous `env -i` avec la même liste blanche de variables que la commande ci-dessous, NO_PROXY et no_proxy compris, interpréteur `/usr/local/bin/python3 -I -B` » ; « tout code autre que 0, ou toute décision autre que « tenu », est un refus : rien ne part ». Conforme au § 9, à R-4325 et à la réserve du contre-lecteur (code 1 possible hors du `try`). Le programme (`60523f21…`) refuse une variable passée vide : sous la liste blanche, un `https_proxy` ou `no_proxy` absent de l'environnement de l'exécutant passerait vide et donnerait un refus, ce qui est le sens prudent.

Deux précisions recommandées (recommandation 3) : écrire la commande à la lettre plutôt que par renvoi, pour que l'environnement soit le même par construction ; vérifier l'empreinte du programme de contrôle et celle du code d'appel v4 (`082d19d6…`, additif § 2.1) au pas 1, avant de lancer l'un ou l'autre.

## 5. Valeurs de clé, courriels, noms de personnes

Aucune valeur de clé, aucun courriel, aucune forme de jeton (`sk-`, `AIza`, `ghp_`, `@` : aucune occurrence). Les seuls noms sont des noms de variables (`RR_ANTHROPIC_API_KEY_LUC`, `GEMINI_API_KEY`) et « la part de Luc » dans le relevé, qui ne va à aucun fournisseur : le programme reçoit le nom de la variable, le relais seul lit la valeur. Conforme.

## 6. Corrections

**Correction 1 (exigée) — arrêt des relais.** Au pas 6, remplacer :

« Les relais restent vivants jusqu'au geste 13 ; leur arrêt se fait par identifiant de processus, sur le mot de la mère (R10). »

par :

« À la fin du geste 9 (code 0 ou 3, ou panne), les relais sont relevés (`/relais/etat`, procédure écrite, § 5), puis arrêtés par identifiant de processus, 7533 et 7563 (procédure écrite, § 6 ; R10), sans attendre les gestes suivants, qui n'appellent aucun fournisseur ; relevé et arrêt sont rendus à la mère, qui les consigne au registre des arrêts et verse `Q` avec `S`. Une relance, sur le mot de la mère, se fait avec des relais neufs (additif, § 9). »

**Correction 2 (exigée) — pièce de vérification de la version 3.** Au premier bloc, remplacer :

« - Étalonnage et lecture : version 3, vérifiée « Conforme », empreintes de l'additif 6, § 2 (`etalonner_ligne_3_v3.py` `d41533cb…`, `lire_ligne_3_v3.py` `c09f4743…`, essais 49 passés). »

par :

« - Étalonnage et lecture : version 3, vérifiée « Conforme » par `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/etalonnage-lecture-v3/verification-v1/verification-etalonnage-lecture-etage-2-v3-v1.md` (`c5119f0459fbdedbdfb64c0d28bfca685b85c99b9557b2ceab198edb658b8582`, 49 passés rejoués) ; empreintes de l'additif 6, § 2.1 (`etalonner_ligne_3_v3.py` `d41533cb…`, `lire_ligne_3_v3.py` `c09f4743…`). »

**Recommandation 3 — commande du contrôle à la lettre, empreintes au pas 1.** Au pas 1, remplacer :

« la déclaration à `HEX_DECLARATION` ; les deux relais vivants aux processus 7533 et 7563. »

par :

« la déclaration à `HEX_DECLARATION` ; le code d'appel `…/etage-2-portee-200-v1/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` à `082d19d61922dbecd64d64435d8a8682f9e01abee6735ff01c6cc550c8f5484c` et le programme de contrôle du mandataire à `60523f210e40c20709188f048a567a7eb14053b6e75ade9cdb919d7bbb04bd39`, sur disque aux chemins écrits ; les deux relais vivants aux processus 7533 et 7563. »

Et au pas 2, après « interpréteur `/usr/local/bin/python3 -I -B`. », ajouter : « Commande, à la lettre : » suivi du bloc

```
env -i PATH="$PATH" HOME="$HOME" GO_ID=GO-2026-11-20-68 HTTPS_PROXY="$HTTPS_PROXY" https_proxy="$https_proxy" NO_PROXY="$NO_PROXY" no_proxy="$no_proxy" SSL_CERT_FILE="$SSL_CERT_FILE" REQUESTS_CA_BUNDLE="$REQUESTS_CA_BUNDLE" CURL_CA_BUNDLE="$CURL_CA_BUNDLE" NODE_EXTRA_CA_CERTS="$NODE_EXTRA_CA_CERTS" /usr/local/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/controle-mandataire-v1/controler_mandataire_etage_2_v1.py
```

(même liste blanche, même ordre, même interpréteur que le geste 9, seul le programme change).

**Recommandation 4 — refus.** Au pas 5, remplacer :

« Codes : 0 exécution écrite ; 2 refus avant tout envoi ; 3 arrêt écrit. »

par :

« Codes : 0 exécution écrite ; 2 refus avant tout envoi, rendu à la mère, aucun argument changé pour le lever ; 3 arrêt écrit (plafond, plomberie, coût relevé). »

**Recommandation 5 — clé Google par son nom.** Au premier bloc, remplacer :

« Clé Google : la carte paie au-delà du crédit (GO-2026-11-20-64). »

par :

« Clé Google `GEMINI_API_KEY` : la carte paie au-delà du crédit (GO-2026-11-20-64). »

et, plus bas, remplacer « clé Google `GEMINI_API_KEY` (GO-2026-11-20-64). » par « clé Google `GEMINI_API_KEY` (R-4368 ; GO-2026-11-20-68). »

## 7. Ce que je n'ai pas fait

Aucun appel payant, aucun programme de l'étage 2 lancé, aucun `git fetch`, aucun `rm`. Rien lu sous `archives-reponses-modeles/` ni `docs/notes/bras-attaque/` ; aucun fichier « consigne-privee » ni « conception-ii-b ». Seule écriture : ce rapport et son compagnon (les deux lignes de commande comparées sont dans mon bloc-notes, hors du dépôt).

— vérificateur neuf, Opus 5.5
