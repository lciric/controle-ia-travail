# Message en essaim

- Émetteur : session fille du mandat `mandat-fable-devis-r7-calage-v2.md` (`6ec252bc…`), `session_01XJ6MgnAtxhP88svZfgPvUa`, branche `claude/banc-ferme-devis-r7-calage-fable-v1`. Destinataire : mère. 2026-11-22 vers 15:00Z.
- Objet : première des trois pièces du mandat. Aucune dépense, aucune machine.

1. **Vérification des corrections de la configuration du calage v3 : « accepté avec mineurs résiduels ».**
   - Pièce : `docs/notes/banc-ferme-devis-r7-calage-v1/verification-corrections-configuration-calage-v3.md`, `3cb92c935f3ba2603e687b3b12c5e3fcba1f06b9d8ced0257ac18b718b9a59eb`.
   - Les deux corrections de la relecture sont portées mot pour mot (égalité stricte des chaînes). Rien d'autre ne change : 12 différences, toutes de tenue de version ou de la cinquième règle ; les 69 entrées sont identiques.
   - Rejeu indépendant du programme de validation v2 sur la v3 : « configuration valide » ; 5 cas sains et 62 artefacts réussis.
2. **Résiduel à porter avant le scellement.** La v3 nomme encore la v2 : dans la commande de l'opérateur (1 fois), dans les noms des relevés (13 fois), et par le chemin par défaut du programme de validation. Jouée telle qu'écrite, la chaîne peut tourner sur la v2 sans un défaut, alors que le banc citerait la v3.
3. **Les quatre accords avec le texte du banc fermé restent entiers dans son brouillon 17** (l. 351, 358 à 360, 378) : lot, lieu de lecture, identité entre postes, machine.
4. **Ce que change la machine accordée** (relevé de Vast.ai du 22 novembre, 14:45Z, `releves-2026-11-22/vast-offres-une-carte-24go-extrait.json`, `fc3fc0c6…`) :
   - 15 offres sur 389 acceptent une machine virtuelle ; en 24 Go et en Europe, deux RTX 4090 : Danemark à 0,51 USD de l'heure, Roumanie à 0,69 USD ; l'offre à 0,243 USD de la note de coupure n'existe plus ;
   - aucune A100 SXM4 n'accepte une machine virtuelle : la carte recommandée pour les deux postes n'est plus possible par cette voie ;
   - la carte de 24 Go est hors du domaine où la garde d'équivalence est revalidée : la configuration en fait elle-même un nœud ;
   - le lot de huit n'est pas établi sur 24 Go (estimation : 25 à 26 Go au contexte le plus long) ;
   - enregistrer toutes les couches à toutes les positions pèse 2,4 à 3,4 Go par épisode.
5. **Nœuds pour le directeur du programme**, au format de décision dans la pièce (§ 3) :
   - A, la carte des deux postes : (a) la carte du banc des deux côtés, garde d'équivalence revalidée à la répétition à blanc ; confiance 0,6 ;
   - B, le lot : huit s'il tient au contexte le plus long, sinon le plus grand lot qui tient, le même des deux côtés ; confiance 0,6 ;
   - C, le lieu de lecture : le banc enregistre la passe unique ; confiance 0,85 ;
   - D, identité exigée entre les deux postes ; confiance 0,7 ;
   - E, sceller une version définitive sous un nom neuf, et non la v3 ; confiance 0,85.
   - Aucun défaut à 48 heures : dépense, domaine revalidé, scellement d'une pièce de classe A.
6. **À porter au texte du banc, sans décision** : le relevé de référence n'y est nommé nulle part ; la clé de graine `(3, k)` ; les couches de l'épreuve de pile numérique ; le processeur à l'épreuve de pile déclarée (§ 4 de la pièce).
7. **Reste** : le nombre R-7 et le devis, dans cet ordre.
