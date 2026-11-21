# Limites de mots des deux consignes du juge des ancres — v1 (classe C)

Écrit le 2026-11-21T23:39:00Z (`date -u`) par un lecteur habilité neuf (Opus 5.5), sous le mandat `mandat-lecteur-habilite-limites-de-mots-juge-v1.md` (`8b3243ba0c690557390b3b7006db8fb2f3b53577fc15ba183f4db185611f0202`, vérifié par son compagnon), accès inscrit au registre (R-4748). Non scellé : la mère scelle.

## Ce qui a été lu, empreintes vérifiées avant lecture
- Préenregistrement `prereg/T0.7-organismes-discrets-v-a-v2-brouillon44.md`, branche `claude/pensive-bardeen-1fv7hw` : `b30aa902a8135f888911519f4efd0a3583fddd6b8f748889146d9bca5da43eb8` (concorde).
- Bloc de la consigne d'appariement, lignes 406 à 431 : `98a9bd34d280fc7d9db07a733bc78557ff350538a3ace7a2926999ecf14c9248` (concorde).
- Bloc de la consigne de couverture, lignes 453 à 487 : `ecf590eae0c06d413d173f7f03c5575e52d6034613e0a1a30d681149435a1816` (concorde).
- Aucune autre ligne lue ; la copie entière du fichier a été effacée du dossier temporaire avant la lecture des blocs.

## 1. Longueur de réponse demandée, en mots
| consigne | limite en mots | ligne où elle est écrite |
|---|---|---|
| appariement (`consignes.appariement.limite_de_mots`) | **aucune limite écrite** | — |
| couverture (`consignes.couverture.limite_de_mots`) | **aucune limite écrite** | — |

Remarque : la seule borne de longueur écrite dans chaque bloc est en caractères, non en mots (ligne 424 pour l'appariement, ligne 474 pour la couverture : 24 et 300 caractères) ; elle ne fixe pas la longueur de la réponse entière.

## 2. Rapport jetons par mot chez Google
- Source publique de Google consultée : https://aistudio.google.com/docs/tokens (adresse atteinte par redirection permanente depuis https://ai.google.dev/gemini-api/docs/tokens), consultée le 2026-11-21 ; la page ne porte pas de date de mise à jour. Elle donne environ 4 caractères par jeton et 100 jetons pour 60 à 80 mots anglais, soit 1,25 à 1,67 jeton par mot.
- **Rapport retenu : 5,1 jetons par mot** (valeur prudente). Justification : le chiffre de Google est une moyenne approchée pour de la prose anglaise ; les mesures du programme sur 43 réponses réelles donnent jusqu'à 5,06 jetons de texte par mot de limite (Argon), et la garde v3 retient 5,1 pour les modèles de Google sans mesure (`docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v8c-v1.md`, table du rapport par espèce). Le chiffre de Google sous-estimerait la sortie d'un facteur trois environ.

## 3. Contrôle : limite × rapport sous 16 000 jetons de texte
| consigne | limite × 5,1 | verdict |
|---|---|---|
| appariement | non calculable (aucune limite écrite) | **ne tient pas** |
| couverture | non calculable (aucune limite écrite) | **ne tient pas** |

Sans limite de mots écrite, le produit ne peut être formé et la règle des appels à Google (GO-2026-11-21-71) ne peut être satisfaite : le contrôle est rendu « ne tient pas » par prudence, non sur un dépassement mesuré.
