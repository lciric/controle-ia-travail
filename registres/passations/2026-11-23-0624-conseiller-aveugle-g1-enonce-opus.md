# Passation — conseiller aveugle sur l'énoncé du critère ajouté à la porte de fin de phase 1 (G1), Opus 5.5 — 2026-11-23 06:24 UTC

- **Session** : `session_013QMayjrAL9gi7azMa1K8Rm` (Opus 5.5, effort très haut), fille de la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Écrite à la demande de la mère (mot de Lazar GO-2026-11-23-09 : reprise possible sur un autre compte, sans perte). Heure relevée par `date -u` : 2026-11-23T06:24:47Z. Classe C.

## Mandat

Conseil aveugle à Lazar sur un seul choix : l'énoncé du critère ajouté à la porte de fin de phase 1. Les trois énoncés étaient : « le contraste » (la porte se gagne aussi contre le témoin apparié), « la garde de spécificité », « la garde décide, le contraste est rapporté » (sur des épisodes à part, ou sur les épisodes de la garde à 5 %). Il fallait rendre la recommandation, la confiance, cinq raisons au plus, ce qui me ferait changer, et les risques de chaque énoncé. Aucune issue d'expérience ne devait être lue ; seules les pièces permises nommées par la mère l'étaient. Un autre modèle répond en parallèle. Aucune dépense.

## Fait

1. Ligne « qui a lu quoi » envoyée à la mère avant toute lecture de fond (colonnes du registre v21).
2. Pièces permises lues ; liste et empreintes à la section 8 de la note. Aucun fichier ne s'est ouvert sur un résultat.
3. Calcul de méthode sur processeur, en mondes synthétiques à suppositions déclarées, sans dépense : `docs/notes/avis-g1-enonce-opus-v1/calcul_avis_g1_enonce_v1.py` (`d87abd8d…`), sortie `sortie-calcul-avis-g1-enonce-v1.txt` (`c5ede31c…`), scellés.
4. Note scellée : `docs/notes/avis-g1-enonce-opus-v1/avis-enonce-critere-G1-opus-v1.md`, `4e89806307561e4b14e35575ca068617a533039182a86a6a793ae024c4ded441`.
   - **Recommandation** : le contraste, à l'échelle du calibrage honnête, jamais au minimum de 300 épisodes. La dépense de ce calibrage n'est engagée qu'en second temps, si le critère actuel et la garde sont tenus ; c'est une seule lecture en deux temps, règle scellée d'avance. Confiance 0,6.
   - **À défaut de second devis** : la garde décide et le contraste est rapporté, sur les épisodes de la garde à 5 %.
   - **Ne pas retenir le contraste au minimum** (confiance 0,85).
5. Commit `f9c313d797551d38e97607a1491d2bdaa4d2b6b1` poussé sur `avis/g1-enonce-opus-v1`. Le premier commit (`e4c53657`) portait la recommandation dans son sujet ; il a été remplacé par un sujet neutre, sur cette seule branche, par une poussée protégée par l'état connu de la branche.
6. Mère informée : chemin, empreinte, recommandation, confiance et trois écarts. Les écarts sont : aucune demande de fusion ouverte, pour ne pas exposer l'avis à l'autre modèle ; le sujet de commit remplacé ; scipy installé dans le conteneur pour le calcul.
7. Ce versement (2026-11-23) : la sortie intermédiaire du calcul (questions 1 à 5), sous `docs/notes/avis-g1-enonce-opus-v1/essais/sortie-intermediaire-calcul-avis-g1-enonce-questions-1-a-5-v1.txt`, scellée.
   - Elle vient d'un état antérieur du script, non gardé : les questions 1 bis et 6 et trois lignes d'en-tête manquaient.
   - Ses lignes des questions 1 à 5 sont identiques à celles de la sortie finale, contrôle par `diff` ; mêmes graines par question.
   - La toute première sortie (questions 1 à 4) a été écrasée par la deuxième exécution ; ses chiffres sont ceux des questions 1 à 4 de la sortie finale.

## Reste

Rien pour cette session : le conseil est rendu. Le choix est à Lazar, par la mère, avec l'avis de l'autre modèle.

## Réserves

- Le calcul suppose un modèle à deux lois normales, un décalage pur, aucune corrélation intra-unité et un seul comparateur (section 7 de la note). Aucun chiffre n'y est une mesure du programme.
- La différence de coût d'environ 8 100 USD est déduite des deux devis donnés par le mandat ; elle n'a pas été chiffrée.
- Je n'ai pas lu la ligne du GO d'accord de principe ni le brouillon 2 de N-074 lui-même, seulement son extrait.

## Prochaine action

Aucune de cette session. Pour une session qui reprend : rien à continuer, sauf si la mère demande une suite. Les questions possibles sont les contrôles du second temps et la taille intermédiaire du calibrage du témoin (section 5 de la note).

## Branches et commits

- `avis/g1-enonce-opus-v1` : `f9c313d7…` (note, calcul, sortie), puis le commit de ce versement (passation et sortie intermédiaire).
- Lu seulement, par refspec explicite : `g1/extraits-tiers-v1` au commit `9133d6dc`.

## Copies locales non reversées

Le bloc-notes de la session contient deux copies identiques à des pièces déjà sur `g1/extraits-tiers-v1` : `extrait-G1-brouillon6-v2.md` (`ceca3970…`) et `extrait-pari-apparie-conception-v2-v1.md` (`db63b19b…`), même empreinte. Elles ne sont pas recopiées ici, pour ne pas étendre leur cloisonnement à une autre branche. Aucun autre fichier, aucun brouillon, aucune réponse de modèle externe : aucun modèle externe n'a été appelé.

## Tâches planifiées et instances actives

Aucune tâche planifiée, aucune tâche de fond, aucune instance de calcul.
