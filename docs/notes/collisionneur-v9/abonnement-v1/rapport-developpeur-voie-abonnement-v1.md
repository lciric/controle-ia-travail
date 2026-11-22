# Rapport du développeur : voie abonnement v1 (kits des cellules Claude)

Écrit à 2026-11-22T14:12:01Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs, sur le mot de la mère (14:03Z : « écris la version du code des kits, classe B, contre-lue, sans dépense, sobrement »). Aucune cellule témoin, aucun kit envoyé.

## Ce que fait le code
`voie_abonnement_v1.py` est une **enveloppe** : les moteurs scellés ne sont pas modifiés. Il charge le moteur par empreinte :
- v8m, 420394f9… ;
- v8p, 5979c712… ;
- essaim v7, 98397f49…, sur v8p.

Il remplace, en mémoire, `executer_cellule` pour les espèces d'Anthropic. Sans réponse recueillie, il écrit le kit (`DOSSIER/abonnement/kits/CID/texte-servi.md` et `fiche.json`, scellés) et rend « KIT ». Avec une réponse recueillie, il passe par le chemin ordinaire du moteur, avec un appelant qui rend la réponse versée :
- `fin` vaut end_turn, le coût est zéro, l'usage vaut zéro (« non mesuré ») ;
- `id_reponse` vaut « abonnement » ;
- une ligne `voie_abonnement` au journal porte la session, le modèle servi, l'effort et les empreintes.

Le collisionneur ferme sa porte d'origine en fin de tour. L'essaim reçoit une copie de `derouler` avec une porte après chaque temps. L'essaim n'est admis qu'en ordre « simultane ».

Commandes :
- `v8m|v8p|essaim [--branche B] -- <arguments du programme>` ;
- `kits DOSSIER` liste les kits en attente ;
- `recueillir DOSSIER CID --texte F --session S --modele-servi M` refuse un modèle autre que celui de la fiche, une réponse vide, un kit mal scellé.

## Choix à contre-lire
1. **Comptage retiré** (`COMPTEURS.pop("anthropic")`) : l'estimation du moteur sert de garde. Il n'y a aucun appel sur Luc, pas même gratuit.
2. **Plafond** : le pire cas des cellules Claude reste calculé aux prix d'Anthropic avant la « lecture ». Le plafond du dossier doit donc le couvrir ; c'est prudent, et aucun argent n'est engagé.
3. **Mélange de voies** : une cellule d'Anthropic qui a un essai par l'interface dans le dossier arrête tout (code 1).
4. **Effort** : le champ `effort` de la ligne d'essai garde la constante du moteur ; l'effort vrai (max) est dans la ligne `voie_abonnement` et dans la fiche.
5. **Parts de l'essaim** : un coût Claude nul change les dépenses par agent. Avec des parts non bloquantes (configuration v7), seules les lignes de journal changent.
6. **Réessai à l'identique** : une réponse versée relue en VIDE ou TRONQUE serait relue telle quelle au second essai du plan. Ce cas est exclu en pratique : `recueillir` refuse le vide.

## Essais (`test_voie_abonnement_v1.py`, 14 essais, aucun réseau)
- **Équivalence** : le même dossier est joué tout par l'interface (doublures déterministes), puis par la voie abonnement (vagues de kits, recueil, relance).
  - Résultat : cellules identiques et invites identiques, cellule par cellule.
  - Comptes : trois vagues au v8m et au v8p, quatre vagues à l'essaim (deux cycles).
  - Il n'y a aucun appel ni comptage chez Anthropic, et `verifier` tient.
- **Gardes** (cas sain et artefact) :
  - modèle servi différent, réponse vide ;
  - réponse altérée, fiche de recueil altérée sans sceau ;
  - texte servi changé, mélange de voies ;
  - kit jamais écrasé, moteur altéré, essaim séquentiel refusé, appel direct refusé.
- **Mutants** : 11 mutants (comptage, mélange, empreinte du texte servi, porte de l'essaim, modèle du recueil, vide, sceau, séquentiel, écrasement, empreinte du moteur, effort) ; tous tués, le témoin survit.

## Ce qui reste hors du code
- La création des sessions (par la mère) et la lecture de la réponse finale par les événements (par la session des collisionneurs) se font par les outils de session, pas par ce script.
- La cellule témoin par modèle attend le mot de Lazar.
