Bonjour. Je suis la session mère Claude Code (session_01QPDgKfh86KrPUDxcz8M1GQ) qui reprend ton dossier v4.

## Ce qui est déjà versé
Branche `claude/happy-davinci-j4xp7t` du dépôt `lciric/controle-ia-travail` :
- ta passation et ses 7 pièces, empreintes vérifiées ;
- les trois GO du 28 inscrits dans `registres/go.md` ;
- tes travaux non commis, transmis par Lazar, versés tels quels sous `brouillons/prereg-v4-c-furtif-g1/` : nœuds GO en texte intégral, brouillons G0 et G1.

Tu n'as pas d'accès git. Pour chaque point ci-dessous, donne donc soit le contenu exact, soit l'emplacement exact sur disque. Une session Claude locale de Lazar versera ensuite.

## 1. Inventaire de ce que tu as produit ou modifié et qui n'est pas sur GitHub
Depuis le commit `c3e3ee73`, et sur les branches `calcul/dose-reponse-20261125-093202-doses-jugees-critere3` (`42cdfcf29`) et `calcul/barreau8-20261126-083755-lecture-et-audit-sondes-v1` (`5817bb0a5`). Pour chaque fichier, donne :
- son chemin sur disque (devbox Antigravity, dossiers `scratch` de jetski, poste Windows) ;
- sa taille et son empreinte SHA-256 ;
- son rôle.
Cela couvre :
- les registres modifiés localement : `registres/go.md` (le « Tour 1 » que tu cites), `registres/decisions.md`, `registres/etat.md` ;
- les scripts de calcul ou d'oracles ;
- les brouillons ;
- les sorties.

## 2. Pièces d'entrée de la contre-lecture R2
Les trois fichiers remis au contre-lecteur : `gemini-code-1795778660659.md`, `kit-r2-lot1-slim.txt`, `kit-r2-lot2-slim.txt`, avec leurs empreintes. Sans eux, on ne peut pas établir ce que ce lecteur a vu.

## 3. Écarts à trancher
- **Empreinte de la contre-épreuve.**
  - Tes textes citent `59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac` pour `contre-epreuve-r2-volets-11-13-v1.md`.
  - Le fichier versé par Lazar a pour empreinte `8547ee1c332b1551bcf7d0d6a0ec3791fd1b5e97fef456c6236ebd73b17bf8e6`.
  - Quelle est la version finale ? Existe-t-il un fichier d'empreinte `59a2a571…`, et où ?
- **Seuil des reprises.**
  - La ligne GO-2026-11-28-01 de la passation porte « arrêt si > 3/N_ep ou écart > 2/N_ep ».
  - Ton texte du nœud et ton brouillon G0 portent « > 3/128 » et « > 2/128 » sur 256 épisodes par condition, soit 6 et 4 reprises.
  - Laquelle Lazar a-t-il arbitrée ?
- **Dose `gonfle_2`.** Le GO dit « (-> gonfle_2 si inclus) », alors que ton brouillon G0 l'inclut d'office comme cinquième condition (12 800 actions). Était-ce arbitré ?

## 4. Identités, pour le registre « qui a lu quoi »
Pour chacune de ces pièces, quel modèle et quelle session l'ont écrite ?
- la Proposition 2 ;
- les corrections B-1, B-2, M-3, M-4 ;
- les Livrables 1 et 2 ;
- la contre-lecture R2 (session `contre-lecteur-r2-architecture-etages-1-2-temporaire-20261126-01`) ;
- la contre-épreuve des volets 11 à 13 ;
- le texte des nœuds GO ;
- les deux brouillons de préenregistrement.

Pour chaque auteur, dis aussi ce qu'il a lu. A-t-il ouvert un `.npz`, un score ou plancher de sonde, une consigne privée ? Comme attestation, oui ou non suffit.

## 5. Volets 1 à 13
Ta passation parle de « Volets 1 à 13 ». Y a-t-il des pièces de ces volets (questions posées, réponses, calculs) autres que la contre-lecture R2 et la contre-épreuve ? Si oui, donne leur emplacement.

## Ce qu'il ne faut pas faire
- N'ouvre aucun `*.npz`, aucun `*.safetensors`, aucun poids, score ou plancher de sonde, aucune consigne privée : la garde P8 vaut aussi pour l'inventaire.
- Donne les noms et les empreintes, jamais les contenus de ces fichiers.

Merci.
