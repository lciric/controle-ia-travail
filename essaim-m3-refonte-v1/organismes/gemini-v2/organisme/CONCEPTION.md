# Essaim de Gemini v2 sous contrat

Enveloppe écrite par la lignée « conv-audit » (24 octobre 2026) autour de `m3_commun.py` (lignée « session-depot »,
branche `outils/essaim-m3-debogage-v1`, `fe56b03`). La conception des scripts du dossier 17 est gardée : castes sur un
tableau partagé, sondes d'écart, extraction par un arbitre, synthèse. Les appels passent par le noyau. L'organisme
répond aux tâches cachées, garde ses extractions dans son substrat (statut `non-verifie`) et se recopie en successeur.
Métrique proposée : capacité de Shannon-Gram du tableau (nom des scripts d'origine ; indice descriptif).
