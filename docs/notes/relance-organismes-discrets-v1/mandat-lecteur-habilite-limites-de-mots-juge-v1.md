# Mandat court (classe C) — lecteur habilité — limites de mots des deux consignes du juge des ancres — v1

Écrit par la session fille de la relance du bras A, le 2026-11-21, à la demande de la session mère, qui l'ouvre sur un agent Opus 5.5 neuf habilité. **L'accès est inscrit au registre par la mère avant toute lecture.**

## Pourquoi
La règle permanente des appels à Google (CLAUDE.md de la branche principale, GO-2026-11-21-71) refuse tout envoi dont « la limite de mots de l'invite ne tient pas dans le plafond de texte ». Pour cela, le programme des essais d'admission (`scripts/chef_essais_admission_bras_a_v8.py`) exige, en configuration définitive, deux champs :
- `consignes.appariement.limite_de_mots` ;
- `consignes.couverture.limite_de_mots` ;

et, chez Google, `jetons_par_mot`. La relance ne les remplit pas elle-même.

## Ce que tu lis, et rien d'autre
Le préenregistrement en vigueur, sur la branche `claude/pensive-bardeen-1fv7hw` du dépôt `lciric/controle-ia-travail` : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md` (sha256 `b30aa902a8135f888911519f4efd0a3583fddd6b8f748889146d9bca5da43eb8`). Seulement deux blocs :
- **consigne d'appariement** : lignes 406 à 431 (empreinte du bloc, lignes jointes par un saut de ligne, sans saut final : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248`) ;
- **consigne de couverture** : lignes 453 à 487 (empreinte du bloc : `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816`).

Vérifie chaque empreinte avant de lire. Pour le rapport jetons par mot chez Google, une seule source publique de Google sur le comptage des jetons, citée avec son adresse et sa date. Sinon, la valeur prudente que tu justifies.

## Ce que tu rends, et rien d'autre
Une pièce courte, `docs/notes/relance-organismes-discrets-v1/limites-de-mots-juge-des-ancres-v1.md`, qui porte :
1. pour chaque consigne, **la longueur de réponse qu'elle demande, en mots** : un entier, celui que la consigne fixe, ou, si elle n'en fixe aucun, « aucune limite écrite » ;
2. **le rapport jetons par mot** retenu chez Google, sa source et sa date ;
3. **le contrôle** : la limite × le rapport, pour chaque consigne, doit tenir sous 16 000 jetons de texte ; écris « tient » ou « ne tient pas ».

**Aucune citation du texte des consignes**, aucun extrait, aucune paraphrase de leur contenu : seulement ces nombres, et les numéros de ligne où la limite est écrite.

## Interdits
Aucun appel payant ; aucune clé ; rien de ce qui touche aux internes des moniteurs ; aucune autre ligne du préenregistrement. N'écris rien d'autre dans le dépôt. Ne scelle pas : la mère scelle.
