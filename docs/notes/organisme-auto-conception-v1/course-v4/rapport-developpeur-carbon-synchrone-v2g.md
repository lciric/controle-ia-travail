# Rapport du développeur — Carbon par la commande synchrone d'Argon, sans troncature, plafonds relevés, clé Minuit (v2g)

Développeur unique de la version (modèle L′), 19 novembre 2026. **Rien n'a été lancé en réel** : aucun appel à un fournisseur, aucun relais réel, aucune dépense ; essais sur relais factices, faux amont Gemini local et moteur simulé de l'orchestrateur épinglé.

## Verdict

Prêt pour la contre-lecture (modèle K) : Carbon passe par la chaîne synchrone d'Argon **sans modifier aucun fichier épinglé** (enveloppe neuve + `commande_argon_v3d.py` inchangée + `relais_gemini_v2.py` inchangé, port 8792) ; réglage sans troncature (sortie 65 536, budget de pensée non fixé, provision 65 536) ; pire cas d'un appel **5,817437 USD ≤ 6** au compte de la commande ; essais 353 passés (227 + 89 + 37), essai à blanc v7 code 0, épreuve hors ligne v7 « témoins éprouvés hors ligne ».

## 1. Comment Carbon passe par la chaîne synchrone d'Argon

- **Enveloppe neuve** `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` (`b380be0b83ed31317141933d501518eb15d9f9318ceb77923d57dbcbf614c0a2`) : refuse tout argument (code 2), pose la clé factice, lance `commande_argon_v3d.py` (`46c91df4…`, épinglée, inchangée) par `exec /usr/bin/timeout -k 20 1720 /usr/local/bin/python3 -I -B "$COMMANDE" --modele gemini-4-carbon --prix-entree 8.3 --prix-sortie 41.5 --provision-pensee-jetons 65536 --sans-config-pensee --max-sortie-jetons 65536 --sortie-min-jetons 4096 --caracteres-par-jeton 3 --marge-entree 0.05 --delai-s 1680 --url-base http://127.0.0.1:8792/v1beta`. Contrairement à l'enveloppe d'Argon v5, aucun `"$@"` : le noyau ne peut rien changer.
- **Analyseur de la commande lu** (`analyseur()`, l. 692-722) : toutes ces options y existent (`--modele`, `--url-base`, `--prix-entree`, `--prix-sortie`, `--caracteres-par-jeton`, `--max-sortie-jetons`, `--sortie-min-jetons`, `--provision-pensee-jetons`, `--sans-config-pensee`, `--marge-entree`, `--delai-s`) ; `argparse` admettrait des abréviations : le lanceur v7 exige chaque option écrite en entier, une fois (`lire_reglage_enveloppe_carbon`), puis passe la ligne à l'analyseur de la commande épinglée et compare les valeurs typées au réglage de l'additif (`controler_reglage_carbon`) ; `config_pensee` faux, `compter_jetons` vrai, `recherche_web` faux exigés.
- **Relais** : `relais_gemini_v2.py` (`2b0043bc…`) lancé à part pour Carbon, `--port 8792 --modele gemini-4-carbon --max-appels 60` (≥ 2 × 11 + 2 = 24 : countTokens puis generateContent par appel), amont de Google, variable de clé effacée — contrôlé par PID et par `/relais/etat` (`controler_relais_externe`).
- **Prix et codes** : la commande compte le coût sur l'usage (entrée × 8,3 ; candidats + pensées × 41,5, par million), rend 3 (HTTP), 4 (pire cas au-dessus du plafond, rien envoyé), 5 (non conforme : vide, `MAX_TOKENS`, modèle servi autre, usage absent), 6 (délai), 7 (pensée au-delà de la provision), 10 (coût au-delà du plafond), 11 (`totalTokenCount` incohérent).

## 2. Réglage retenu et pourquoi

Mot de Lazar « enlève la troncature pour Carbon » :
- **Sortie maximale 65 536** = le maximum de la commande : `MAX_SORTIE_JETONS_DEFAUT = 65536` (`commande_argon_v3d.py` l. 348 ; usage l. 324). C'est la seule source du dépôt ; ni l'orchestrateur ni une documentation interne ne donnent un maximum propre à `gemini-4-carbon` (point ouvert 3).
- **Budget de pensée non fixé** (`--sans-config-pensee` : aucun `thinkingConfig`, défaut du fournisseur) plutôt qu'égal au maximum : un `thinkingBudget` de 65 536 pourrait être refusé en 4xx si la plage du modèle est plus basse (code 3, aucun repli), et en lot le budget n'était de toute façon pas tenu (v62, PO-178).
- **Provision de la garde 65 536** (≥ la sortie) : si la pensée compte dans `maxOutputTokens` (documentation lue par la session principale ; observation du lot v6 : 32 765 + 3 = 32 768), elle ne peut dépasser la provision, et la garde « pensée > provision » (code 7) ne refuse plus une réponse complète.
- **Délai** : 1 680 s pour la commande (son minuteur global couvre countTokens et generateContent), arrêt dur 1 720 + 20 s = 1 740 s ≤ 1 770 s (délai fixe de 1 800 s de l'orchestrateur, moins 30 s).

## 3. Comment la commande synchrone compte la pensée (note l. 260-261)

Dans sa garde avant envoi, la provision s'ajoute à `maxOutputTokens` : pire = entrée gardée × 8,3 / 10⁶ + (sortie + provision) × 41,5 / 10⁶, prudent quel que soit le comportement de l'interface ; elle réduit d'elle-même la sortie pour tenir `PLAFOND_SESSION_USD`. Après coup : coût sur l'usage, code 7 si `thoughtsTokenCount` > provision, diagnostic `lecture_pensees` = `hors_max_sortie` si candidats + pensées > `maxOutputTokens`. La note l. 260-261 dit que, pour Argon en synchrone, l'interface **ne comptait pas** la pensée dans `maxOutputTokens` ; la documentation du fournisseur et le lot v6 disent l'inverse pour Carbon. La sonde réelle le mesure (`pensees_jetons`, `lecture_pensees`).

## 4. Pire cas d'un appel

Plus grande entrée servie (recalculée par programme, `plus_grande_entree` : consigne du proposeur puis case, comme `GenerationV54._proposer`) : lot 1 « famille « exploration » », 136 265 octets, 130 101 caractères, sha256 `e5aeddbb7f172fd666adc7dbb1959af220333115f3ec086f8f7a402556d4e753`.
- **Au compte de la commande** (⌈130 101 / 3⌉ = 43 367, marge 5 % → 45 536 jetons gardés) : sortie retenue **65 536** (aucune réduction), pire **5,817437 USD ≤ 6**. Le lanceur v7 refuse toute réduction de la sortie et dit alors le plafond nécessaire (5,82 USD ici).
- À la borne prudente (octets / 2 → 71 540 jetons) : 6,03327 USD ; la commande réduirait la sortie à 64 734 ; **plafond nécessaire 6,04 USD** (à porter à Lazar s'il veut cette marge ; non pris).

## 5. Plafonds relevés (mot de Lazar « augmente le plafond »)

Configuration v3 (`8e54a61c…`) : proposeur 6,00 USD par appel ; S17 120 USD (ligne de GO de la course à 120 USD exactement) ; étapes sacrifiables 121 USD ; relais Claude 120 USD ; rien d'autre. Plafonds d'étape recalculés (règle d'A1) : proposition 110 (80 en v6) ; aiguillage lancé si cumul ≤ 105 ; juges si cumul ≤ 90 (60). **Aucun seuil interne ne bloque à l'estimation (48,05 avant les juges) ni au haut (74,41)** ; onze pires cas de Carbon (≈ 64 USD) priveraient l'étape « juges » de budget (non mesurée, C13) — dit au devis et à l'additif. Parts au pire : Claude 120, Gemini 120, Astra 66 ; relais d'Astra à `--plafond-usd 67`.

## 6. Clé Claude Minuit

`RR_ANTHROPIC_API_KEY_MINUIT` admise pour cette course seulement, sur le mot de Lazar cité dans la pièce (`cle_claude_mot_de_lazar`, qui doit dire « Clé Minuit ») ; Rigaud refusée (pièce et relais) ; gabarit : crédit 200 USD (R-3228), réserves vides, dépense antérieure 0 + 0,000108 (R-3616) à reporter au relevé. Reste net estimé ≈ 199,03 > 120.

## 7. Pièces neuves (empreintes)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v7.py` | `b10b2d18efaa6ce4936cbc98d081fee37d3df220afc771158dc23d6a9a1d901d` |
| `course-v4/additif-preenregistrement-course-auto-conception-v2g.md` | `2b0d3e7a553c60c013f81c37f6150c27285e80377219920495fba8a8816bb867` |
| `scripts/sonde_carbon_synchrone_v1.py` | `77e313689641a062efc97590ff1030e966d51c53c319a53f553f771b5b2ff447` |
| `scripts/epreuve_temoins_auto_conception_v7.py` | `0f980b18271f2337dd2ace6663662eb13641cee1da943dd2de23a417cbca44b3` |
| `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` | `b380be0b83ed31317141933d501518eb15d9f9318ceb77923d57dbcbf614c0a2` |
| `course-v4/configuration-course-auto-conception-v3.json` | `8e54a61c4d5f7ea4ac04c89db52d10646bfdef9d5174ceb5342774781e0e2eb9` |
| `course-v4/piece-de-depart-gabarit-auto-conception-v2g.json` | `6af1df039f34f9f88bdcc3b2ece324a56a358c95b47b703a520e8c32fbd63989` |
| `course-v4/calcul-devis-course-auto-conception-v2g.py` / `.json` | `bf1e8a04…` / `b01678ad8db9790fcef5f0ae5debb542f0ee5c36d772c5f8953f85bc1a821be5` |
| `course-v4/devis-course-auto-conception-v2g.md`, `course-v4/commandes-exactes-course-auto-conception-v2g.md` | compagnons `.sha256` |
| essais : `tests/test_lancer_course_auto_conception_v7.py` (227), `tests/test_epreuve_temoins_auto_conception_v7.py` (89), `tests/test_sonde_carbon_synchrone_v1.py` (37) | `3de14cd3…`, `b3f5d53d…`, `c2b92d13…` |

## 8. Essais (R5 : sain, artefact, mutation par garde)

- Essais v6 portés (gardes générales, course jouée par le vrai noyau, bornes Gemini, épreuve recalculée, sonde d'Astra, composition) ; lanceur v7 : 227 passés ; épreuve v7 : 89 passés ; sonde : 37 passés, dont un bout en bout par le vrai `relais_gemini_v2.py` (clé factice) devant le faux amont, qui compte bien 2 appels de relais.
- Gardes neuves, chacune saine, en artefacts et mutée : réglage de l'enveloppe (16 artefacts : provision, sortie, drapeaux, abréviation, doublon, `--x=v`, modèle, port, timeout, délai, prix, garde d'arguments, `"$@"`, autre commande), déclaration exactement `["bash", enveloppe]`, pièces épinglées par la pièce de départ, pire cas sans troncature (6 ; 5,8 → « 5,82 » ; 3), relais Carbon Gemini v2, sonde de Carbon du jour (15 artefacts), configuration v3, ligne de la course à 120, clé Minuit, courses v4 et v6 closes, lignes -67 et -68.
- Sonde : sain ; tronquée (`MAX_TOKENS`), pensée > provision (code 7), modèle servi non admis, 400, usage absent → « non réussie », rapport écrit sans texte ; GO, relais jeté, clé dans l'environnement, rapport existant, plafond insuffisant → refus **avant tout envoi** (le faux amont n'a rien reçu) ; mutants (texte gardé, modèle non contrôlé, borne non contrôlée) attrapés.
- Essais existants rejoués (lanceurs v4 à v7, épreuves v3 à v7, sonde, Astra et Carbon déclarés v2b, commande d'Argon v3d, relais Gemini v2) : 1 288 passés, 1 sauté, 6 échecs **préexistants et sans lien** avec cette version (aucun fichier suivi n'est modifié) : `test_epreuve_temoins_auto_conception_v3.py::test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs` (le rapport réel v3 existe depuis le 18 novembre) et cinq essais de `test_commande_argon_v3d.py` qui lisent `/opt/argon/commande_argon_v2.py`, absent de ce conteneur. Les essais v4, v5 et v6 des lanceurs et des épreuves passent tous.

## 9. Points ouverts

1. **Contre-lecture** par le modèle K : non faite (R2 : je ne peux pas la faire) ; chemin `course-v4/contre-lecture-tentative-carbon-synchrone-v2g-auto-conception.md`.
2. **Trois lignes de GO neuves** à accorder par Lazar : course **120 USD** exactement (« auto-conception », « tentative neuve »), épreuve 5 USD (« témoins »), sonde de Carbon **6 USD** (« sonde », « Carbon »).
3. **Maximum réel de sortie de `gemini-4-carbon`** non documenté au dépôt : 65 536 est le maximum de la commande ; si le modèle en accepte moins, l'appel rend un 4xx (code 3), la sonde le dira sans coût.
4. **Comptage de la pensée en synchrone** inconnu pour Carbon (note l. 260-261 pour Argon : hors de la sortie) : si elle n'est pas comptée et dépasse 65 536, code 7 ; la sonde mesure `pensees_jetons` et `lecture_pensees` sur le plus grand lot.
5. **Plafond par appel à 6,04 USD** si Lazar veut tenir la sortie maximale même à la borne prudente (octets / 2) ; à 6 USD, elle tient au compte de la commande (hypothèse : `countTokens` ≤ caractères / 3, relevée par la sonde).
6. **Budget des juges** : onze pires cas de Carbon priveraient les juges (seuil 90 USD avant les juges) ; à l'estimation et au haut, aucun blocage.
7. **Durée** : un appel de Carbon jusqu'à 1 740 s ; onze cases, plusieurs heures possibles (lancement détaché exigé).
8. **Réserve de la mère** sur la clé Minuit (variable commune ; relevé de facturation de Lazar fait foi).
9. Écart de consigne de ma part, à signaler : une commande d'essai a contenu une fois un heredoc vide (aucun fichier ni script écrit, aucun effet) ; aucun autre écart aux règles permanentes.
