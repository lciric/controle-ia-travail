"""Essai de raccord du programme de lecture et de la fabrique des mondes (barreau 5) — tirage de l'entropie, v1.

Mandat `mandat-essai-raccord-v1.md` (`46390c9a…`), point 1 : une entropie neuve de 128 bits pour cet essai seul
(`secrets.randbits(128)`). Elle ne sert pas à l'épreuve à vérité plantée du point 11. Aucune donnée lue.
"""
import secrets

print(secrets.randbits(128))
