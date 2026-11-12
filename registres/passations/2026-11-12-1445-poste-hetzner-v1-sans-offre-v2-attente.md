# Témoin de Bailey — poste Hetzner v1 arrêté faute d'offre ; v2 avec attente bornée — 12 novembre 2026, 14:45 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Ne se réécrit pas (R12). Suit
l'ordre v5 (`2026-11-12-1425-…`) et la note de refus (`2026-11-12-1426-…`).

## Fait
- Lazar a quitté le mode « Auto » pour « Accept edits » (« c'est fait, passé en accept edits, relance ») ; la commande de
  création, présentée à son approbation, a été exécutée : serveur Hetzner **175838275** (`poste-temoin-bailey-v1`,
  `cx23`, `fsn1`) créé à 14:30:26Z. Données de démarrage effacées (`shred -u`) aussitôt après l'envoi ; réponse de l'API
  conservée sans données de démarrage ni mot de passe.
- Le poste a cloné la branche (`c3516b3c`), monté Python 3.11.2 et `vastai` 1.11.0, lu les clés, trouvé l'inventaire
  Vast sans instance du poste, puis : « aucune offre conforme : rien ne tourne » (14:34:42Z, commit `84d9d3f1` poussé
  par le poste). Aucune instance Vast créée, aucune dépense Vast.
- Relevé de la session à 14:35Z : zéro offre conforme ; six A100 80 Go louables, toutes hors filtre (disque sous 200 Go
  ou mémoire allouée de 101 à 129 Go pour une garde à 128 × 10⁹ octets).
- Poste 175838275 inactif détruit par son identifiant à 14:35:38Z (HTTP 200 ; absent de la liste relue à 14:35:53Z) ;
  coût ≈ 0,001 EUR. Autres serveurs du compte, non touchés : `organisme-v67-course` (175834755) et `lean-outillage-d1a`
  (175838427).

## v2 (routine, code du lanceur distant ; aucune ligne du préenregistrement ni du code du run ne change)
- `poste-hetzner-v2.sh` : v1 + attente bornée d'une offre conforme (même filtre que l'ordre v4) : 144 essais espacés de
  600 s (24 h au plus), état poussé tous les six essais, rien n'est loué pendant l'attente ; au-delà : arrêt, « aucune
  offre conforme en 24 h ». Fichiers d'état `poste-hetzner-v2-etat.txt`, marque `poste-fini-v2.json`.
- `construire-donnees-demarrage-v2.py` : v1 dont seuls changent le script assemblé et le nom du serveur
  (`poste-temoin-bailey-v2`).
- Épreuves : syntaxe ; sélection d'offre, code 1 sur une liste vide, code 0 sur une liste réelle.
- Coût de l'attente : poste seul, ≈ 0,011 EUR/h, soit ≈ 0,26 EUR pour 24 h.
