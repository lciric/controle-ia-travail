# Devis v4 : deux questions au collisionneur (modes de sabotage, attaques), part Claude par l'abonnement

Écrit à 2026-11-22T15:24:22Z (`date -u`). Classe C, recalcul. Session des collisionneurs, Opus 5.5, sur l'option (a) accordée par la mère. Le GO reste GO-2026-11-21-08 (48,13 USD au pire, échéance le 28 novembre). Ce devis remplace le calcul de la v3 (`devis-collisionneur-modes-et-attaques-v3.md`, fadb7d09…, gardée telle quelle) pour une seule raison : la v3 visait un script v8 à écrire ; le moteur est désormais le **collisionneur v9-v8m** (`docs/notes/collisionneur-v9/collisionneur_v9_v8m.py`, 420394f9…, contre-lu). La part Claude passe par l'abonnement : voie abonnement v5, recueil v6.

## Composition (option sans Kimi de la v3, celle du GO)
- **Fable 5.1** (`claude-fable-5-1`) : la seule espèce Claude, par l'abonnement, à 0 USD d'interface.
- **Argon, Carbon** : par `GEMINI_API_KEY`.
- **Astra** (`gpt-6.2-astra`) : par `OPENAI_API_KEY_2`.
- Opus 4.6 et Kimi sont absents, comme dans l'option du GO.

Le v8m remplit les quatre conditions de la v3, au § 6, point 2 :
- budget de réflexion et provision comptés ;
- écart de total compté ;
- aucun renvoi d'une requête partie, et tout envoi interrompu compté au pire ;
- délais longs.

## Devis au pire, par question, sans --sortie-max (moteur v8m, commande devis)

| espèce | clé | modes de sabotage | attaques |
|---|---|---|---|
| Argon | GEMINI_API_KEY | 5,27 | 5,27 |
| Carbon | GEMINI_API_KEY | 7,25 | 7,25 |
| Astra | OPENAI_API_KEY_2 | 2,11 | 2,11 |
| **par l'interface** | | **14,63** | **14,63** |
| Fable 5.1 (abonnement, non facturé) | — | 8,26 | 8,26 |

- **Épreuve de Carbon** : plafond propre de 2,20 USD.
- **Total au pire par l'interface** : 14,63 + 14,63 + 2,20 = **31,46 USD**, sous les 48,13 du GO.
- **Plafond proposé par passage** : 16 USD.
- **Par clé, au pire** : GEMINI_API_KEY 2 × 12,52 + 2,20 = 27,24 ; OPENAI_API_KEY_2 4,22 ; Luc 0.
- **Avec --sortie-max**, Astra passe à 20,11 par question et le total à 67,46. C'est au-delà du GO : **ne pas l'employer**.
- **Prix d'Astra** : la table du moteur l'applique à 10 / 50 USD par million, alors que le prix relevé est de 8 / 40. C'est une surestimation d'environ 20 %, déclarée (`docs/notes/collisionneur-v9/prix-gpt-6-2-astra-releve-v1.md`).

Calcul brut : `devis-brut-v8m-modes-sabotage-v1.txt` et `devis-brut-v8m-attaques-v1.txt`, dans ce dossier.

## Réserves
- **Fable 5.1 par l'abonnement** : il n'est pas établi qu'il soit proposé comme modèle de session fille. S'il ne l'est pas, l'espèce Claude manque. La suite sans elle, ou un autre Claude, demande le mot de Lazar ; changer de modèle demande un GO.
- **Taille des textes servis** : ceux des tours III.2 et III.3 dépasseront ce qu'on peut mettre en invite. Ils passent par la voie fichier : branche `kits-abonnement/*` et recueil v6. Pour la session cloisonnée, les branches de kits portent des textes qui contiennent des modes : elles doivent avoir un nom de coffre (voir le mandat).
