"""Pôle « scientifique automatique », version 0 : fiches gelées, expérimentateurs et vérificateurs, sélection par
sévérité ou par pari, mesure de qualité sur témoins, mémoire, recombinaison bisociative corrigée.

Version 0.2.0 (dossier `orchestrateur-pole-v2`) : juge v1 de la sélection par pari (ordre d'exécution secret,
membre « urne », loi « sans remise », garde du plan d'exécution) et contrôles de l'expérience 1 du pôle
(`controles_pari_v1.py`, `experience_juge_v1.py`). La version 0 reste dans `orchestrateur-v0` (jamais écrasée).

Cœur en bibliothèque standard ; `claude_agent_sdk` n'est importé que par l'adaptateur réel, au premier lancement.
"""

__version__ = "0.2.0"
