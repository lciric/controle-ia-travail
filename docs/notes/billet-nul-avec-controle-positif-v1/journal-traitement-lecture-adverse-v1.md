# Journal : traitement de la lecture adverse du « modèle C » sur le billet P3 / P3-bis — v1

- **Rédacteur** : le rédacteur des pièces v1 (« modèle A », R-2718). 14 novembre 2026, de 11:38 UTC à 11:50 UTC environ (`date -u`). Rien commité, rien publié, aucun contact.
- **Lecteur adverse** : sous-agent neuf, « modèle C » (R-2718 : jamais le « modèle B », indisponible jusqu'au 20 novembre), lancé à 11:33:59 UTC par la commande `claude -p` en mode non interactif, depuis le bloc-notes de la session, avec le seul droit de lire le dépôt ; outils permis : Read, Grep, Glob, `date`, `sha256sum`, `wc` ; refusés : écriture, édition, réseau, sous-agents. Fin du processus à 11:38:19 UTC, code 0, sortie d'erreur vide ; heures écrites par le lecteur : 11:34:02Z à 11:37:35Z.
- **Consigne** : `consigne-lecteur-adverse-v1.md` (`821bb54b48f453591b5dbf8142f1fbd06c8681ccb6030ed1b906965afe98c112`) : fichiers à lire donnés un à un (R2), interdits de lecture, méthode, forme du rapport.
- **Rapport versé tel quel** (copie à l'octet de la sortie standard) : `lecture-adverse-modele-c-v1.md` (`e111761208faa3d0db805392c3aac6c0f3220dd39fb770590993fe4a453dc479`).
- **Pièces relues** (scellées avant la relecture) : `fiche-de-faits-v1.md` (`fd8041db…`), `relecture-billet-v2-contre-verdict-v1.md` (`0e6dd370…`), `billet-premiere-version-en-v1.md` (`d6474ea3…`).
- **Verdict du lecteur** : « Prêt après corrections. » Aucun nombre faux ; phrases gelées fidèlement traduites ; 13 constats (C-1, C-2, C-3, C-4 et C-13 majeurs ; les autres mineurs).

## 1. Constat par constat

| constat | gravité | décision | où |
|---|---|---|---|
| C-1 — réserve B3 tronquée (« au plancher et à la demi-largeur observés », « calculée avant le scellement, sur des nombres déjà lus ») | majeur | **appliqué** : les deux membres sont dans le billet. (Le rapport renvoie à « verdict de P3-bis, l. 109-110 » : ce sont les l. 109-110 du verdict de **P3**, qui portent bien les deux phrases B3.) | billet v2, « P3's null » |
| C-2 — réserve PB-4 non dite comme réserve déclenchée | majeur | **appliqué en partie** : nombre, 53 tâches, « a triggered frozen reservation ; its bearing on A vs T is left open » (VB l. 491-494). **Non repris** : la conséquence proposée par le lecteur (« le texte planté seul déplace donc le comportement, ce qui touche la lecture de A contre T ») : le verdict ne la dit pas et en laisse la portée à Lazar | billet v2, « Results » |
| C-3 — « this outcome opened a preregistered follow-up's probe scores » dépasse les pièces | majeur | **appliqué** : « A rule fixed in advance makes this outcome the condition for reading a preregistered follow-up's probe scores. » « Preregistered » vérifié : ligne `SCELLEMENT-T07` (SC l. 8 ; fiche v2, F67) | billet v2, « What comes next » |
| C-4 — aucune marge de mots | majeur (forme) | **appliqué en partie** : la section « Related work », absente des sections demandées, sort du corps (phrase prête dans les notes hors billet) ; quelques détails sortent aussi (voir section 2). Le corps reste à 999 mots : la marge pour les deux sections à remplir ne tient pas sans sortir des réserves obligatoires du corps. **Nœud de Lazar** : fiche v2, section 6, point 10 (budget suggéré : 100 à 150 mots par section marquée) | billet v2 ; fiche v2 |
| C-5 — réserves des addendums et de l'ouverture comptées par nombre seulement | mineur | **appliqué** : les quatre réserves des addendums nommées ; les trois de l'ouverture dites « écrites après la lecture fermée, aveugles par cette seule fermeture » | billet v2, « Limits » |
| C-6 — B1 portée partiellement ; « did so » contre « exceeded » | mineur | **appliqué** : « inflated it beyond that » ; borne basse de `E_sf` 1.3211 contre log10 3 = 0.4771, hors des cinq formes mesurées ; causes non mesurées (unité, échelle des propositions, gonflement) | billet v2, « The question », « P3's null » |
| C-7 — résumé plus fort que le corps | mineur | **appliqué** : « at this power » et « caveats below » pour le nul ; la phrase persona, forme, longueur ; « Sentence written before the run » au lieu de « Fixed in advance » ; « preregistered » retiré de la dernière phrase du résumé ; ligne neuve dans « ce qu'il ne faut pas dire » (fiche v2) | billet v2, TL;DR ; fiche v2, section 3 |
| C-8 — réserve (1) de R-2299 difficile à lire | mineur | **appliqué** : règle de P3 définie entre parenthèses ; « false "above" readings » (R-2299 : le défaut « ne fabrique que des « au-dessus » ») ; « lower bounds of the difference » ; « floor's 0.95 quantile » partout. L'omission de « est celle de T0.7 » reste posée à Lazar (fiche v2, section 6, point 2) | billet v2, « P3's null » |
| C-9 — question PB-10 cryptique | mineur | **appliqué** : « the signal's spread over the action differs from the plan's expectation (one area 0.9856, outside the "too good" audit) » ; les nombres de la différence restent dans la fiche (F51) | billet v2, « Limits » |
| C-10 — « planted-word mentions » | mineur | **appliqué** : « mention patterns 0.5025 » | billet v2, « Results » |
| C-11 — « AI agents (Claude models) » | mineur | **non appliqué**, laissé à Lazar (fiche v2, section 6, point 7) ; « no human redid the computation » gardé (le lecteur le juge exact) | — |
| C-12 — F01 : ligne fausse (l. 121 vide) | mineur | **appliqué** : P3 l. 122 (modèle), l. 143 et 291 (couches) ; vérifié sur pièce | fiche v2, F01 |
| C-13 — « contredit » trop fort pour « la sonde lit la consigne » ; ligne 12 « confirme en principe » | majeur | **appliqué** : « laisse ouvert, en tension avec PB-5 et PB-6 (ni appuyé ni réfuté) » ; ligne 12 « laisse ouvert (compatible) » ; légende précisée | fiche v2, section 3 ; relecture v2, lignes 12 et 30, section 2 |

Compte : 13 constats ; 10 appliqués, 2 appliqués en partie (C-2, C-4), 1 laissé à Lazar (C-11).

## 2. Constats du rédacteur lui-même, appliqués dans la v2

- « One random direction of 800 beats the probe » affirmait une seule direction : le verdict dit seulement que le maximum du plancher (0.8743) dépasse l'aire de la sonde (VB l. 253-254). Devenu « Some random direction beats the probe on A vs T (floor maximum 0.8743) ».
- « an earlier attempt stopped at batch 19 of 30 » : la v2 écrit « an earlier attempt stopped and was destroyed unread » (arrêtée seule, cause probable non confirmée : VB l. 435-439) ; le lot 19 sur 30 reste dans la fiche (F31).
- « (2) they belong… » était ambigu après la réserve (1) : « the minimum detectable areas belong… ».
- Le TL;DR citait le nul sans renvoyer à ses réserves : « (caveats below) ».
- Sortis du corps pour la longueur, gardés dans la fiche ou les notes : travaux voisins (fiche v2, section 5) ; « no honest episode reproduced P3's hashes » (F53) ; « batch 19 of 30 » (F31) ; les nombres de PB-10 (F51).

## 3. Contrôles faits après la correction

- Corps du billet v2 : 999 mots (`wc -w`), 976 mots alphanumériques ; une seule section `<<ETAPE_B>>` et une seule `<<ETAPE_B_BIS>>`, vides.
- Chaque nombre décimal du corps v2 se retrouve, arrondi, dans `docs/verdicts/verdict-P3-bis-v1.md` ou `docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (62 nombres ; seuls « 3.1 » du nom du modèle et l'identifiant arXiv ne sont pas des nombres à vérifier) ; le contrôle signale bien un nombre faux planté (artefact : 0.8021 au lieu de 0.8012). Script dans le bloc-notes, non versé : `controle_nombres_v1.py` (`1b4ee316…`).
- Recherche dans le corps v2 des mots interdits (identifiants de modèle, « held-out », « attack », « TASTE », « T0.7 », gabarit de l'action, phrase de persona) : aucun.
- Les citations des travaux voisins (28) avaient été contrôlées sur PDF avant la relecture (fiche v2, section 5) ; le lecteur ne les a pas relues (limite de son rapport).

## 4. Ce que le lecteur n'a pas contrôlé (ses limites, recopiées en substance)

Le compte de 998 mots de la v1 (il n'a pas pu isoler le corps) ; les pages publiques de P3 et de R1 ; les PDF et leurs citations ; les lignes 1400-1401 du texte scellé de P3-bis ; le rapport d'audit de R-2299 ; les empreintes de la fiche autres que celles des quatre pièces qui font foi.

## 5. Pièces v2

`fiche-de-faits-v2.md`, `relecture-billet-v2-contre-verdict-v2.md`, `billet-premiere-version-en-v2.md` : empreintes dans leurs compagnons `.sha256` (scellement après ce journal). Les v1 restent telles quelles (R12). Aucune seconde lecture adverse n'a été faite sur les v2.
