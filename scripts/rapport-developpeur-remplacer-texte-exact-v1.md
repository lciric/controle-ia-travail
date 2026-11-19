# Rapport du développeur — outil de remplacement de texte exact, v1

Développeur, modèle L′ — 2026-11-19T22:51Z. Écrit dans le bloc-notes seulement : rien n'est écrit dans le dépôt, rien n'est
commité ni poussé. Aucun appel à un fournisseur de modèles, aucune dépense.

## Verdict

L'outil `scripts/remplacer_texte_exact_v1.py` (bibliothèque standard seulement) et ses essais sont écrits. **55 essais passés,
0 échoué.** Les 9 défauts réintroduits dans des copies de l'outil sont tous vus.

## Fichiers

| Chemin relatif au dépôt | Empreinte SHA-256 |
|---|---|
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |
| `tests/test_remplacer_texte_exact_v1.py` | `e71c606c6db919edace6f618cd5564bc622fb3a4dbbba10c2b905f593095e03c` |
| `scripts/rapport-developpeur-remplacer-texte-exact-v1.md` | (ce fichier : son empreinte est donnée dans le compte rendu) |

## Appel

    python3 -B scripts/remplacer_texte_exact_v1.py --cible FICHIER --remplacements R.json --sortie NOUVEAU [--sur-place-interdit]

`R.json` est une liste non vide de `{"ancien": "...", "neuf": "..."}`. Le fichier est écrit avec l'outil d'écriture, jamais par
un heredoc. L'outil écrit `NOUVEAU`, `NOUVEAU.sha256`, `NOUVEAU.journal-remplacements-v1.json` et son compagnon `.sha256` (les deux
compagnons sont vérifiables par `sha256sum -c` depuis le dossier). La cible n'est jamais touchée : pour installer la sortie à sa
place, il faut une étape à part, décidée hors de l'outil.

Codes de retour : 0 fait ; 2 refus (motif après `REFUS :` sur la sortie d'erreur, rien d'écrit) ; argparse rend aussi 2 pour un
usage invalide.

## Règles appliquées (toutes vues par un cas sain et par un artefact)

- **Ancien exactement une fois**, occurrences chevauchantes comptées (« aa » figure deux fois dans « aaa ») ; le message donne
  les numéros de ligne des occurrences.
- **Zones disjointes** (deux zones contiguës sont permises), et application **simultanée** aux positions d'origine : un texte neuf
  n'est jamais relu par un autre remplacement.
- **Texte neuf** : il figure k fois de plus qu'avant, k étant le nombre de remplacements qui portent ce même texte neuf.
- **Contrôle interne avant écriture** : la longueur est vérifiée, tous les octets hors des zones sont identiques et la sortie est
  en UTF-8 strict.
- **Refus sur les entrées** : cible ou JSON absent, dossier, non UTF-8 ; JSON mal formé, autre chose qu'une liste, liste vide,
  objet attendu, clés manquantes ou en trop, clé en double, valeur non chaîne, substitut isolé, marque d'ordre des octets en
  tête du JSON, `NaN` ; « ancien » vide ; « neuf » égal à « ancien ».
- **Refus sur les sorties** : refus si la sortie, l'un des compagnons ou le journal existe, même en lien symbolique pendant. Refus
  aussi si la sortie est la cible, ou si le dossier de la sortie manque. Chaque fichier est créé en mode exclusif. Si une
  écriture échoue, les fichiers déjà créés par cet appel sont retirés et l'outil refuse ; s'il ne peut pas en retirer un, il le
  nomme.
- **Octets** : tout est lu et écrit en octets. La marque d'ordre des octets, les fins CRLF, LF et CR seul, les espaces de fin et
  l'absence de saut final sont gardés à l'octet.
- `--sur-place-interdit` est accepté et toujours vrai. Aucune option n'écrit sur place. Les abréviations sont refusées
  (`allow_abbrev=False`), donc `--sur` et `--sur-place` donnent un refus.

## Choix à signaler (consigne non explicite)

1. **Plusieurs remplacements avec le même texte neuf** : la consigne dit « une fois de plus ». Je lis cette règle comme « k fois
   de plus » pour k remplacements identiques. Pour des textes neufs distincts, c'est exactement la consigne. Si tu veux la
   lecture stricte, il suffit de refuser les doublons de texte neuf ; dis-le et je fais une v2.
2. **Texte neuf vide (suppression)** : permis. Le compte d'occurrences n'a pas de sens pour une chaîne vide ; c'est le contrôle
   interne des octets et de la longueur qui couvre ce cas.
3. **Conséquence voulue de la règle sur le texte neuf** : un remplacement qui raccourcit un texte en gardant son début
   (« foo bar » → « foo ») est refusé, parce que « foo » figurait déjà dans l'ancien. Un texte neuf recréé par jonction avec ses
   voisins (« a_c », « _ » → « cc ») est aussi refusé. L'agent doit alors élargir le contexte de l'ancien et du neuf.
4. **Avertissement non bloquant** : quand un texte neuf apporte un style de fin de ligne absent de la cible (« \n » seul dans un
   fichier en CRLF, par exemple), l'outil écrit quand même mais le signale sur la sortie d'erreur et dans le journal.
5. **Le journal** porte l'heure UTC et l'empreinte de l'outil, donc deux exécutions identiques ne produisent pas un journal
   identique à l'octet. La sortie, elle, est déterministe.

## Contrôle « trop beau » (R4)

J'ai réintroduit chaque défaut ci-dessous dans une copie de l'outil. Pour chacun, le contrôle nommé passe sur l'outil et échoue
sur la copie : les 9 défauts sont vus.

| Défaut réintroduit | Contrôle qui l'a vu |
|---|---|
| Comptage des occurrences sans chevauchement | `verif_refus_ancien_chevauchant` |
| Contrôle des zones chevauchantes retiré (le contrôle interne refuse encore, mais pour un autre motif) | `verif_refus_zones_chevauchantes` |
| Lecture en mode texte (fins de ligne converties) | `verif_sain_octets` |
| Sortie existante réécrite (absence non vérifiée, ouverture en `wb`) | `verif_refus_sortie_existe` |
| « Ancien » vide accepté (l'outil plante au lieu de refuser) | `verif_refus_ancien_vide` |
| Contrôle du texte neuf retiré | `verif_refus_neuf_jonction` |
| Clé en double acceptée | `verif_refus_json_cle_en_double` |
| Nettoyage retiré après une écriture interrompue | `verif_refus_ecriture_interrompue` |
| Application séquentielle au lieu de simultanée | `verif_sain_application_simultanee` |

**Défauts vus dans l'outil lui-même** : aucun. Les 55 essais sont passés au premier lancement ; vu R4, je donne ce résultat avec
une réserve. Elle est en partie levée par le contrôle par défauts réintroduits, qui montre que les essais savent échouer.

**Limite** : je n'ai pas essayé un très gros fichier. La recherche des occurrences chevauchantes est en O(n·m) dans le pire des
cas, ce qui ne pose pas de problème pour des fichiers sources.

## Essais et essai manuel

- Commande : `PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider tests/test_remplacer_texte_exact_v1.py`,
  lancée depuis le bloc-notes. Résultat : 55 passés en 2,5 s.
- Essai manuel : deux remplacements sur `CLAUDE.md`, lu seulement, avec une sortie dans le bloc-notes.
  - `diff` montre les deux seules lignes changées ;
  - `sha256sum -c` des deux compagnons donne OK ;
  - une seconde exécution vers la même sortie est refusée (code 2) ;
  - `git status` du dépôt reste vide.
