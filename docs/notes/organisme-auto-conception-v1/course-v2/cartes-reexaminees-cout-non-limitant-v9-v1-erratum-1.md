# Erratum 1 — « Les 22 cartes non gardées de la course v9, relues quand le coût ne limite plus — v1 »

- Écrit par le même lecteur (Claude Fable 5.2), sur demande de la mère, le 2026-11-19. Pièce de travail (classe C). Processeur seul, aucune dépense, rien de commis.
- Corrige `cartes-reexaminees-cout-non-limitant-v9-v1.md` (sha256 `de7ed04d06903c507ace3a16130fccf9f22d88e6e16143c3f8f3e0530837d063`), qui n'est pas réécrite (règle R12). Cet erratum prime sur les trois points ci-dessous ; le reste de la note, verdict et lignes, est inchangé.

## 1. Section 2.1, dernière puce : « six », lire « sept »

Le critère « battre le meilleur de N tirages indépendants » figure dans les sept cartes de la ligne, porteuse comprise : `f91a7a590c8fe`, `f0a8378953d43`, `fdafe4598caad`, `f17603c39bc32`, `ff76aee57bba1`, `f38a6ed2f7434`, `f68f93bac44e8`. Compté par programme sur le texte des cartes (mention de « meilleur de N » ou de « N tirages indépendants »). La réserve est la même : critère à réécrire comme pratique citée.

## 2. Section 1, troisième ligne du verdict : « huit cartes sur dix en dépendent » est retiré

Ce chiffre n'était pas compté. Lire à la place : « la plupart des cartes s'y réfèrent ».

Ce qu'un programme peut compter, c'est la mention, pas la dépendance. Sur les 22 cartes : 16 nomment la lecture de la sélection entre générations ou la génération suivante ; 14 nomment les tests de mort ; 20 nomment l'un ou l'autre. Les deux qui ne nomment ni l'un ni l'autre sont `fe15813583b5c` et `ff99ce570c638`. Une mention ne prouve pas que l'épreuve de la carte exige le branchement : ce compte vient en appui, il ne remplace pas le chiffre retiré par un autre chiffre de dépendance.

Programme du compte, gardé hors du dépôt : `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/fable-reexamen-cout-v9/compte_erratum.py`, sha256 `812aa11937d9a50e7e0e1ecfb1307364e40e629a2a9e5441c1a74acbc1ac7596`, lu sur `cartes-non-gardees-v9-sans-espece.json` du même dossier.

## 3. Longueur au-delà du mandat

Le mandat fixait deux pages au plus pour la note et une page au plus pour la définition. La note fait 1 569 mots, environ trois pages ; la définition (`definition-amelioration-considerable-v9-v1.md`, `4eae96bc…`) fait 787 mots, un peu plus d'une page. Écart déclaré, non corrigé : les deux pièces sont scellées.
