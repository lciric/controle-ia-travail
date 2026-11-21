# Vérification du lanceur de l'étape de discrétion, version 2, contre l'extrait des six étapes v3 et le module d'entrée v2 — réponse sans interne — v1

- **Par** : agent habilité neuf de la mère (Claude Opus 5.5), le 21 novembre 2026, sous GO-2026-11-20-21. Classe B.
- **Ce qui ne figure pas ici** : aucun nom de moniteur, de famille, de seuil ni de trait, aucune valeur, aucun extrait de code de moniteur. Le fichier des scores par unité n'a pas été ouvert.
- **Lieu de travail** : clone à moi dans mon dossier temporaire, à la tête `5e5c17d8dbfbe360de7b66404b2e928a0be572e6` de la branche habilitée (le lanceur et ses essais y sont ceux du commit `848c17649`, inchangés depuis), sans les fichiers à cloisonner ; environnement Python à moi. Aucun commit ni poussée, aucun appel payant, aucune clé lue, aucun outil refusé.
- **Une précision** : pour importer le vrai module d'entrée, j'ai copié dans ce clone temporaire les modules de graines de la relance qu'il importe, sans lire leur source. Seules leurs lignes d'import me sont passées sous les yeux.

## 1. Verdict

**Conforme** sur ce que l'extrait exige : les six étapes, dans l'ordre ; les quatre conditions ; une seule exécution pour la production, les ouvertures et la lecture commune ; la reprise après une panne ; aucune suppression ; l'appel du module d'entrée ; la configuration ; les fichiers et leurs formes.

Restent **trois corrections mineures**. Aucune n'agit sur un score, sur un ordre ou sur une garde. Elles sont à faire à la prochaine version du lanceur, ou avant la course :

1. **Dossier du fichier des rangs (section 5 de l'extrait).** À l'étape 1, le lanceur liste le contenu de ce dossier pour s'assurer qu'il est vide. Or l'extrait veut que ce dossier ne soit parcouru par aucun programme. À cet instant, le fichier n'est pas encore écrit dans une course normale, et rien n'est ouvert. Correction : ne plus lister le dossier, et tester seulement si le fichier des rangs ou son compagnon existe déjà sous son nom.
2. **Manifeste du lanceur, réglages de la carte (réserve déjà relevée par la vérification habilitée précédente, toujours ouverte).** Les réglages de déterminisme ne sont versés au manifeste qu'après la boucle de production. Si la production s'arrête sur une panne, le manifeste d'arrêt porte donc ce champ à nul. Correction : verser ces réglages dans un bloc qui s'exécute en fin de boucle, panne comprise.
3. **Manifeste du lanceur, fichiers écrits (section 5 : « l'empreinte de chaque fichier écrit »).** Le relevé scellé d'une reprise n'est pas porté aux fichiers écrits du manifeste. Son empreinte n'y figure que dans le texte de la ligne inscrite au registre. Correction : l'ajouter aux fichiers écrits.

Points qui ne relèvent pas du code et restent renvoyés à la mère, sans changement :
- Le module de graines qu'importe le module d'entrée n'est pas cité par empreinte dans la configuration.
- L'extraction et la base se jouent par deux sous-commandes à part, avant l'étape de discrétion, avec entre elles les versements de la session principale. La règle « une seule exécution » de l'extrait vise la production, les ouvertures et la lecture commune : elle est tenue.
- L'engagement de la table, les manifestes de production et les reprises vont dans un registre propre au bras (décision 2 de la mère). Les lignes que lit la garde de production restent au registre des scellements.
- Le chemin réel n'a été éprouvé que par doublures : chargement sur la carte et relevé des jetons de fin restent à essayer sur la machine de calcul.

## 2. La version qui fait foi

| pièce | chemin | sha256 | commit |
|---|---|---|---|
| lanceur, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v2.py` | `c3840745ccaad9b889b676ff7ac2450397f60192b72391e2c42ec37eb5e5ca7e` | `848c17649d3c324461747daa99fb8784c88a8baa` (branche `claude/bras-a-habilite-developpeur-v1`) |
| ses essais | `tests/test_bras_a_v2_habilite_lanceur_discretion_v2.py` | `7729f5bdd09c99af56170663b37899365ef985395d61ec3363b1c9e9141e7760` | même commit |
| gabarit de sa configuration, version 2 (pas jouable tel quel) | `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v2.json` | `9a944d74986445deb096f13cc834456e624592a08ab24fd5f164c78d2d1e25e9` | même commit |
| extrait des six étapes v3 (référence) | `docs/notes/relance-organismes-discrets-v1/extrait-lanceur-etape-discretion-pour-le-developpeur-v3.md` | `5d2a48c0f9b6b8a36b20cc466508c44fe1c2aad84a17b98cfb1190f85c631bed` | `45d79625a` (branche `claude/pensive-bardeen-1fv7hw`) |
| module d'entrée v2 (référence) | `src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v2.py` | `cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10` | `e1b2fd297` (branche `claude/pensive-bardeen-1fv7hw`) |

Les empreintes sont égales à leurs compagnons. Les treize modules que cite le gabarit ont l'empreinte qu'il leur donne : les douze premiers sur la branche habilitée, le module d'entrée sur la branche de la relance.

**Sous-commandes** : `extraire`, `base`, `discretion`, `relever-fins`.

## 3. Ce que j'ai rejoué

| épreuve | résultat |
|---|---|
| essais du lanceur v2 | 30 réussis sur 30 |
| les trois fichiers d'essais ciblés ensemble (lanceur v2, préparation v3, module des autres moniteurs v11) | 42 réussis sur 42 |
| épreuve par retrait v2, en entier (script de la branche habilitée) | les 70 retraits mordent ; fichiers remis à l'identique, empreintes vérifiées |
| essai à moi : la chaîne entière avec le **vrai** module d'entrée v2, le registre des accords figé au commit où la ligne d'accord est inscrite (`f174bb1fb840f7ef049e1d70dd621e6410391a42`) et le registre courant, avec des doublures pour les moniteurs | réussi ; l'accord est consigné tel quel au manifeste |
| essai à moi : copie figée changée | refus levé par le module d'entrée, avant le tirage ; aucune table tirée, aucun engagement inscrit |
| interface du module d'entrée | les cinq noms de l'extrait, et eux seuls ; signature à la lettre ; l'exception du module est celle du lanceur |

## 4. Réponses aux sections 5 et 6 de l'extrait

- **Dossier du fichier des rangs** fixé par le gabarit : `donnees/bras-a-v2-discretion/rangs-par-unite`, disjoint des six autres dossiers, ce que le lanceur exige. **Six programmes** nomment ce fichier (recompté sous `src` et `scripts`) : quatre versions du module des autres moniteurs et les deux versions du lanceur. Aucun ne l'ouvre après son écriture ; seuls les outils de scellement en prennent l'empreinte. Seule exception au « jamais parcouru » : la liste faite à l'étape 1 (correction 1).
- **Garde d'équivalence du jeu d'épisodes** : le lanceur ne joue aucun épisode, et cette garde ne le concerne donc pas.
- **Pièce qui rejoue un lot** : non commandée, non écrite.
