# Contre-lecture du programme d'extraction du cas X6 — v1

Agent neuf, Claude Sonnet 5.5, 20 novembre 2026. Pièce de travail (contre-lecture d'instrument).

Empreintes vérifiées : programme `e2da19df...bacb19`, essais `39d282ee...11431b`, mandat `7cf9d488...0bf` (conformes au mandat).

## Verdict : conforme

- Écritures : le rapport ne contient que la version, le commit, le suffixe, le chemin du seul fichier, son empreinte et sa taille, les noms de clés, des comptes, des identifiants passant le motif `[A-Za-z0-9._:/-]{1,120}`, des classes passant `[a-z_]{1,40}`. Ni `categorie`, ni texte, ni motif de contenu. Le message d'erreur de JSON n'écrit que le nom du type d'exception. Au code 3 la « forme » ne donne que des noms de clés et des types.
- Gardes : codes 2, 3, 4, 5, 6 chacune par un code non nul et un rapport d'arrêt ; pas de repli silencieux.
- Essais : douze réussis ; cas sain et artefact pour les codes 2, 3, 4 (absent, texte libre, ambigu), 5, 6 (JSON illisible).

## Réserves mineures (non bloquantes)
1. Un identifiant non textuel (nombre) avec une clé parente texte retombe sur la clé parente, comptée dans `source_identifiant.parent` : visible, pas silencieux.
2. Un nom de fichier non UTF-8 dans le commit lèverait une exception non rattrapée (code non nul, pas de rapport).
3. La borne de profondeur (code 6) n'a pas d'essai propre.

## Passage unique sur le vrai commit
Code de sortie 4 (identifiant absent, ambigu ou illisible), sans rejeu. Sortie : `sortie-extraction-x6-v1.json`, sha256 `a13699aa74777d3814c09a335774314ca3cdb76ec2855799ce376847447f9f3b`. Chemin trouvé : un seul fichier, 957 octets, sha256 `e2ba2a332438ced587c2d0a68ab1bc5105c8c9950d350d6a38cacd9be5e995df`. Deux objets portent une clé `classe`, tous deux sans identifiant lisible ; aucune ambiguïté. Noms de clés : categorie, classe, contenu, empreinte, fournisseur, ident, origine, refus_aiguilleur. Aucun compte par classe n'est produit (arrêt avant). La sortie ne contient que des noms de clés et des comptes.

Cause probable de l'arrêt : la clé d'identifiant réelle est `ident`, absente de la liste CLES_ID du programme ; aucune clé parente textuelle exploitable non plus. Je n'ai rien rejoué ni corrigé.
