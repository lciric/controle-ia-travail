# Règle de forme élargie pour le repêchage de la passe X — v1

Écrite et scellée le 2026-11-22T14:00:44Z par la session de l'organisme, **avant tout rejeu**, sur le mot de Lazar (GO-2026-11-22-70) et l'accord de la mère (13:12Z et 13:59Z).

**Ce que montre le diagnostic** (`../passe-x-diagnostic-forme-v1/sortie-diagnostic-forme-passe-x-v1.json`, comptes seuls) :
- les onze réponses rejetées portent leurs titres « Réponse k » au bon nombre (6 ou 3) ;
- leur dernière ligne est « FIN DES RÉPONSES. » **avec un point final** (motif `ligne_finale_ponctuee` vrai, `ligne_finale_exacte` faux) ;
- la garde v4 s'arrêtait à ce contrôle, avant de compter les titres. D'où les « 0 titre » du journal.

**Règle élargie, et seulement elle.** La garde de coupure de `passe_x_na_v4.py` est rejouée à l'identique, avec un seul changement : au contrôle de la ligne finale, la ligne comparée peut finir par **un point unique** (« FIN DES RÉPONSES. »), après le retrait des marques `*`, `_`, `#`, `>` et des espaces déjà prévu. Elle doit toujours être présente **une seule fois, en dernière ligne**.

**Rien d'autre ne change** : titres dans l'ordre exact, au moins 240 mots par section, alertes, et cause « réflexion épuisée » sur fin non normale.

**Application** :
- aux seuls flux classés « défaut » par la garde v4, déjà payés, sans aucun appel neuf ;
- une unité est **« admise par règle élargie »** si son groupe entier passe la règle, ou si ses deux moitiés la passent toutes deux ;
- chaque flux repêché est marqué ainsi au relevé. Rien n'est lu ni affiché.
