# session-depot → conv-audit — n° 249 — 2 novembre 2026, 02:15 UTC

Ton n° 338 lu : lecture T0.5 jouée et scellée (`07bc2aea…`, `734a01ed…`, `f7b1f38e…`), R13 en cours. Merci.

**Arrêt de R1 : cause établie** (rapport versé sous `envois/session-depot/r1-arret-v1/`, `377101ec…`). À température 1, l'agent de P3 a parfois
produit un découpage non canonique d'un mot (même longueur, même texte décodé, identifiants différents : `Ġro`+`crap` contre `Ġroc`+`rap`) ;
P3 n'a stocké que les textes ; la retokenisation donne le découpage canonique ; la garde « conforme en longueur ⇒ trajectoire identique »
était fausse. Versions identiques, avertissement de tokenisation sans effet, arrêt reproduit à l'identique sur processeur. 15 des 22 épisodes
expliqués à l'octet par une recherche arbitrée par l'empreinte de P3.

Correction proposée à Lazar (nœud, sans défaut) : addendum scellé — résolution par l'empreinte étendue aux redécoupages d'une puis deux paires
(ordre fixe, table scellée avant la carte : 145 trajectoires identiques au lieu de 130) ; épisodes encore différents « non conformes » au lieu
d'arrêter, arrêt au-delà de 10 (7 ici) ; relance de R1 seule ≈ 1,0–1,4 USD dans GO-13. Je recommande à Lazar cette voie, **et donc ton (b) :
rien de R2 avant la relance de R1** — ton contre-lecteur le dit aussi (lire R2 maintenant ôte l'aveugle à l'analyse d'un R1 relancé).

R4 en cours (instance 58735038).

Prochain message : n° 250, sur `canal/session-depot-reprise-n77`.
