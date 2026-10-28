# Fiche — Zolkowski, Xing, Lindner, Tramèr et Jenner, *Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability* (arXiv 2510.19851v1, 21 octobre 2025) — v1

- **Nature** : prépublication (MATS, ETH Zurich, Google DeepMind).
- **Fichier** : `pdf/zolkowski-2510.19851/2510.19851v1.pdf`, SHA-256
  `0ce332cebeb2aaac2723c6e242979a5660bf9efa3083bca69b2c0edd7dcf5948`, 1 044 549 octets, 39 pages.
- **Provenance** : `https://arxiv.org/pdf/2510.19851v1`, téléchargé le 2026-10-26 à 10:36 UTC ; titre conforme.
- **Pages lues** : 1.
- **Chez session-depot** : **non**.

## Ce que la source établit sur un mode d'échec

1. **Sans pression d'obscurcissement, la surveillance de la chaîne de pensée est exacte et efficace** (p. 1).
2. **Sous forte pression d'obscurcissement par la consigne, certains modèles accomplissent la tâche adverse sans être
   détectés** (p. 1), y compris dans SHADE-Arena.
3. **Asymétrie interne/externe** : les modèles obscurcissent moins leur raisonnement interne (traces de raisonnement)
   que leur raisonnement externe demandé dans la sortie (p. 1).
4. Conclusion des auteurs : un déploiement robuste demande des tests de résistance de la surveillabilité **propres à
   chaque modèle** (p. 1).

## Conditions

- Pression exercée par des consignes (taxonomie de consignes ; non décrite ici) ; tâches jouets et SHADE-Arena.

## Ce qu'elle ne dit pas

- Rien sur des moniteurs d'activations ; la pression est par consigne, pas par entraînement.

## Ce que ça touche chez nous (avis)

- E1.5 (a) (attaques par contenu : consigne de rester sous le seuil) : contre une base boîte noire qui lit le
  raisonnement, la consigne seule peut suffire à faire passer certaines attaques ; la comparaison H1 doit déclarer la
  pression appliquée à chaque bras et la mesurer par modèle.

## Phrase citée

« (ii) Under strong obfuscation pressure, some models successfully complete adversarial tasks while evading
detection. » (p. 1)
