# Vérification de cloisonnement de l'extrait du lanceur v3 et du module d'entrée v2 — v1

- **Pièces vérifiées**, compagnons conformes :
  - `docs/notes/relance-organismes-discrets-v1/extrait-lanceur-etape-discretion-pour-le-developpeur-v3.md`, `5d2a48c0f9b6b8a36b20cc466508c44fe1c2aad84a17b98cfb1190f85c631bed` (comparé à la v2) ;
  - `src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v2.py`, `cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10`.
- **Vérification de référence** : `verification-cloisonnement-extrait-lanceur-v2.md`, `c3e6ec974b239b04abcba23bd434fd866e0dc1b84826bd52c2adcd0b62bd15b2`.
- **Relecteur** : le même agent Claude Opus 5.5. Classe C. Mêmes interdits.
- **Essais faits** : j'ai importé le module et appelé la porte sur des registres fictifs, écrits dans mon bloc-notes. L'identifiant était hors de la suite réelle (`GO-2099-01-01-01`). J'ai produit onze cas : dix refus et un cas sain. Aucun réseau, aucun modèle, aucun fichier du dépôt modifié.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir

Les quatre retouches de la v2 sont tenues. Le module n'expose plus que ses cinq noms. Ni ses refus ni ce qu'il rend n'apprennent au développeur quelque chose qui puisse orienter ses moniteurs, ni ce que décident ses réponses. Rien à retoucher avant la sortie.

## 1. Les retouches de la v2

| n° | retouche | tenue ? | preuve |
|---|---|---|---|
| 1 | Ne plus exposer `_graines` | **oui** | `dir(module)` rend exactement `ECART_A_R9_ACCORDE`, `EPISODES_PAR_TACHE`, `GardeArret`, `PAS_PAR_EPISODE`, `admettre_l_entropie_propre_de_la_table_des_identifiants`. L'import se fait par les seuls noms. L'essai `tests/test_entree_lanceur_discretion_bras_a_v2.py` le vérifie (`dir` égal à `__all__`). |
| 2 | Retirer `tirage_de`, `generateur_pour` et `cle_lec6` | **oui** | Absents du module et de sa documentation. L'énumération des usages de l'analyse n'est plus atteignable par le module. |
| 3 | L'extrait s'aligne | **oui** | Le paragraphe « Graines » et la mention de `cle_lec6` sont remplacés par la liste fermée des noms exposés, avec « le lanceur ne tire lui-même aucune graine par ce module ». |
| 4 | Le motif `graines_bras_a_v*` vaut aussi pour sa pièce des demandes | **oui, par renvoi** | La ligne 6 de l'extrait dit que ce motif « complète la liste de non-ouverture de ta pièce des demandes ». Les deux pièces lui sont remises ensemble. |

## 2. Contrôle par programme

- **Empreintes** : aucune chaîne hexadécimale de 8 signes ou plus, ni dans l'extrait v3 ni dans le module v2.
- **Chemins de l'extrait** : seulement les motifs d'exclusion (dont `graines_bras_a_v*`), le chemin du module d'entrée v2 et les deux fichiers de sortie.
- **Chemins du module** : aucun.
- **Mots du plan d'analyse** : ni « brouillon », ni chemin de texte, ni « Page », « DOSES », « aire-cond », « lec6 », « tirage_de » ou « generateur_pour » dans le module. Dans l'extrait, la seule occurrence est « brouillons et texte scellé compris », dans le motif d'exclusion.

## 3. Ce que disent les refus et le dictionnaire rendu

Les cinq points signalés par le rédacteur, jugés sur les messages que j'ai fait produire.

**3.1 — Les numéros de section (« 6.2 », « 8.4 », « 13.2 »).**
- **Sans risque.** Un numéro seul ne dit rien du contenu, et le développeur n'ouvre pas le texte avant sa dernière livraison.

**3.2 — « configuration scellée » (« état figé au scellement de la configuration », « la configuration scellée attend… »).**
- **Sans risque.** Dans cette porte, la configuration est celle du lanceur : l'extrait, en sections 3 et 4, lui dit d'y inscrire l'empreinte et le commit de l'état figé du registre. Si un message dit « de l'analyse », il ne lui apprend que l'existence de cette configuration, que ses demandes 13 et 33 lui donnent déjà.
- **Remarque de clarté, non bloquante.** Pour lui, « la configuration scellée » serait plus juste en « la configuration scellée du lanceur ». C'est à reprendre seulement à la prochaine version du module de graines, sans urgence.

**3.3 — La phrase d'accord entière (« écart à R9 accordé pour la table des identifiants opaques »).**
- **Sans risque.** C'est l'objet de la ligne publique GO-2026-11-19-97 du registre de la branche principale, que l'extrait lui cite déjà.

**3.4 — Seize signes d'empreinte du registre.**
- **Sans risque.** Ce sont les débuts de l'empreinte du fichier qu'il a lui-même remis et de celle que sa propre configuration attend. Ce ne sont pas des empreintes de pièces interdites.

**3.5 — Le dictionnaire rendu.**
- Il rend : `{'usage': "table des identifiants opaques des scores produits avant l'ouverture", 'entropie': …, 'cle_de_6_2': None, 'ecart': "R9 : entropie du système, non dérivée de l'entropie du bras", 'go': …}`.
- **Sans risque.** L'usage décrit la table que l'extrait lui fait tirer, étapes 2 et 4. `cle_de_6_2: None` dit seulement qu'aucune clé de graine n'est employée. L'écart et le GO sont ceux de la section 3.

**3.6 — Ce que les refus apprennent de plus.**
- Le refus sur révocation dit qu'une ligne entrée depuis l'état figé et qui nomme le GO arrête le tirage, « quel que soit son type ».
- C'est une règle de tenue du registre, déjà connue de la session principale (demande 29 du lecteur). Elle ne touche pas les moniteurs. **Sans risque.**

**3.7 — Les traces d'erreur.**
- Une trace Python affiche le nom de fichier `graines_bras_a_v12.py` et la ligne `raise` du refus. Ces lignes ne portent que les messages ci-dessus.
- Ouvrir le source reste interdit par la ligne 6.
- *Réserve déjà dite à la v2* : une introspection volontaire (`admettre….__globals__`) remonte toujours au module v12. La consigne et la contre-lecture du lanceur tiennent ce reste.

## Retouches

Aucune avant la sortie. Remarque facultative, pour une version future du module de graines : écrire « configuration scellée du lanceur » dans les refus de la porte (3.2).
