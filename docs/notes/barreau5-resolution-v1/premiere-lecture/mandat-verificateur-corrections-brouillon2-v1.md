# Mandat du vérificateur Opus 5.5 des corrections du texte de la première lecture (brouillon 2) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 19 novembre 2026 vers 15:45Z. Pièce de travail : elle dit quoi lire, quoi vérifier et quoi rendre, sans rien concevoir.

---

Tu es un vérificateur neuf (Claude Opus 5.5) du programme de contrôle boîte blanche, dépôt `/home/user/controle-ia-travail`. Tu n'as écrit aucune des pièces que tu lis (R2). Le contre-lecteur d'origine (Opus 5.5) a écrit la contre-lecture du brouillon 1, mais il est resté sur un autre compte et n'est pas joignable. Tu le remplaces pour vérifier les corrections : c'est un écart déclaré à la règle « vérification par le même contre-lecteur ». Français, mots en clair, identifiants en appui seulement. Aucune dépense, aucun lancement sur carte, aucun commit.

## Pièces
Vérifie d'abord chaque empreinte : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement verifier <fichier>`. Dossier `docs/notes/barreau5-resolution-v1/premiere-lecture/` sauf mention.
- **La contre-lecture d'origine :** `contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md` (13bde378…), avec ses outils dans `contre-lecture-outils-v1/`.
- **Les deux brouillons du texte :** `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md` (c5cd9259…) et `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md` (b346d5bd…).
- **La table des corrections :** `table-corrections-brouillon2-v1.md` (d4d6c9c8…).
- **Les devis :** brouillon 1 `devis-relecture-meme-chemin-v1-brouillon1.md` et brouillon 2 `devis-relecture-meme-chemin-v1-brouillon2.md` (35eb6996…).
- **Les nœuds :** `noeuds-restants-v1.md` et `noeuds-restants-v2.md` (8778c213…).
- **L'outil d'application et son relevé :** dossier `outils-brouillon2-v1/` (2a88a1ba…, f411272d…).
- **Ce que le rédacteur a reçu et rendu :** `mandat-redacteur-corrections-brouillon2-v1.md` (217ea246…) et `rendu-redacteur-corrections-brouillon2-v1.md`.
- **La ligne `GO-2026-11-19-62` de `registres/go.md`.**

## Ce que tu vérifies
1. **Les 44 couples, par ton propre programme**, sans réemployer l'outil du rédacteur :
   - chaque « avant » figure une seule fois dans le brouillon 1 (ou dans le devis brouillon 1) ;
   - chaque « après » figure en entier dans le brouillon 2 (ou dans le devis brouillon 2) ;
   - la différence entre les brouillons 1 et 2 ne contient rien d'autre que les couples, les changements « hors correction » déclarés et les huit ajouts déclarés.

   Tout changement non déclaré est un constat.
2. **Les huit ajouts de conception « à trancher par le vérificateur »** : pour chacun, « garder », « corriger » (couple exact « avant → après ») ou « retirer », avec la raison.
3. **La correction M4.1** (miroir exact de l'épreuve) : le rédacteur la juge fausse en partie et la fait suivre d'une phrase qui la limite. Tranche : le rédacteur a-t-il raison ? Si une correction est nécessaire, donne le couple exact.
4. **Les onze points relevés sans changement** à la fin de la table : dis lesquels doivent être corrigés avant le scellement (couples exacts) et lesquels peuvent rester.
5. **Le devis brouillon 2 et les nœuds v2** : arithmétique et rédaction, dont l'option neuve d'une coupure portée à environ 9 USD.
6. **Le validateur des préenregistrements** (`src/controle_ia/prereg.py`, fonction `problemes`) : appelle-le sur le brouillon 2.
   - Écris les deux refus qu'il rend, et les cinq marqueurs que le rédacteur dit laissés à la mère.
   - Dis ce que la mère doit remplir au scellement, et si quelque chose bloque le scellement.
7. **Si c'est court**, rejoue la simulation de la contre-lecture (m6.1), que le rédacteur n'a pas rejouée.

## Forme
- Verdict en tête, l'un des trois : « scellable tel quel », « scellable après ces couples exacts », « à reprendre ».
- Chaque constat est classé bloquant, majeur ou mineur. Chaque couple exact est donné avec un texte « avant » dont tu as vérifié qu'il est unique dans le brouillon 2.

## Sorties (scellées par `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -B -m controle_ia.scellement sceller <fichier>`, non commises)
1. `docs/notes/barreau5-resolution-v1/premiere-lecture/verification-corrections-brouillon2-v1.md`
2. tes outils et leurs sorties dans `docs/notes/barreau5-resolution-v1/premiere-lecture/verification-outils-brouillon2-v1/`.

## Interdits
- **N'ouvre jamais :**
  - un fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
  - `brouillons/ii-b-saboteur-budget-v1/`, la branche `lot/compte-4-v1`, la ligne R-2059 ;
  - les notes « pour Lazar seul » ;
  - le fichier des scores par unité du bras A ;
  - les valeurs des deux booléens d'aiguillage du texte scellé de validité, où qu'elles soient écrites ;
  - rien sous `/root/.claude/`.
- **R1 :** n'ouvre aucun fichier des scores fermés que ce texte doit lire ; aucune lecture de résultat avant scellement.
- **Recherches :** pas de recherche plein texte sur tout le dépôt. Limite-toi aux dossiers nommés ici, en excluant les motifs interdits.
- **Exécution :** ne lance pas la suite complète des essais. Aucune commande `rm` sur un chemin construit par variable.
- **Refus d'outil :** au premier refus, arrête-toi et dis-le, sans le contourner.
- **Cloisonnement de la mère :** dans ta réponse finale, ne recopie aucun nombre de résultat de l'étape B bis ni d'aucune expérience close (aires, différences, scores, valeurs p lues) ; renvoie par chemin et numéro de ligne. Dans ta vérification écrite sur disque, cite ce qu'il faut pour juger.

## Rends
1. La phrase exacte de ton invite système qui nomme le modèle qui te sert.
2. Les chemins et empreintes de tes sorties.
3. Dix lignes au plus :
   - le verdict ;
   - le nombre de constats par classe ;
   - ce que tu décides des huit ajouts et de M4.1 ;
   - ce qui bloque le scellement ;
   - ce que la mère doit remplir.
4. La liste des fichiers et des dossiers que tu as ouverts, une ligne chacun (registre de « qui a lu quoi »).
