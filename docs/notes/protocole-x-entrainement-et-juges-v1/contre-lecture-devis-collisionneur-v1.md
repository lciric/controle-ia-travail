# Contre-lecture du devis du collisionneur (entraînement et juges) — v1

Opus 5.5, sous-agent neuf, non auteur, sans réseau. Pièce : `devis-collisionneur-entrainement-et-juges-v1.md`.

## Verdict : tient après corrections

Chiffres, textes, garde et commande justes ; aucun bloquant ; six constats importants.

## Constats

**1. Important — part d'Anthropic (§ 0, point 2).** Le plafond et la ligne bornent la dépense du dossier entier (l. 988, 2580-2588), sans borne par clé. Les relances (`nombre_relances`, l. 2665) se comptent par commande : après un arrêt, une nouvelle commande renvoie la cellule. La borne dure d'Anthropic est donc de 18 USD, et non de 8,3. De plus 4,11 × 2 = 8,2. Texte proposé : « 8,2 USD si chaque cellule d'Opus épuisait sa relance dans une commande ; seule la ligne de 18 USD du dossier borne le tout ».

**2. Important — effet du plafond (§ 3).** Le programme refuse un envoi quand la dépense réelle plus le pire cas de l'essai suivant dépasse 18 USD. Ce refus peut tomber à n'importe quelle cellule (code 4, rien n'est envoyé). Le dossier reste alors incomplet, et ce qui est payé l'est en pure perte. Au pire strict, la marge est de 2,10 USD : une relance d'Opus ou de Neon passe, jamais une de Carbon. Aux coûts attendus, plusieurs relances passent. Pour finir le dossier, il faut `--ligne-reprise-usd` avec `--go-ligne` et un plafond relevé. Le devis doit le dire.

**3. Important — pannes (§ 6).** Une coupure de flux arrête la commande : code 5, coût compté au pire, aucune relance (l. 2627). Une cellule non valide ferme la porte du tour (code 2, l. 2890). `--repli-lot` est refusé à Carbon. La seconde relance de Google baisse le niveau de réflexion (l. 581). Dire aussi si la relance « sur le même accord » part dans le même dossier, sur le reste de la ligne, ou dans un dossier neuf avec 18 USD de plus.

**4. Important — note de sortie (§ 5.4).** La règle « Notes des collisionneurs » la rend obligatoire : ce n'est pas une option. Le programme ne la produit pas, et le devis n'en nomme ni le rédacteur ni le coût.

**5. Important — mots du directeur (§ 0).** `GO-2026-11-24-16` porte deux demandes de collisionneur : « ce qu'il faudrait faire » sur l'entraînement, et « ce qui entre dans un programme amélioré ambitieux ». Le devis les fond en un seul dossier ; cette fusion est un choix, à nommer pour confirmation. Pour le dossier 2, le devis est fidèle : « carbon fable », et aucun montant n'est accordé au collisionneur.

**6. Important — durée (§ 4).** Les cellules partent l'une après l'autre. Au pire, les délais font 14 400 s par tour, soit 12 heures sans relance. Écrire ce pire à côté de « une à trois heures [supposé] ».

**7. Mineur — arrondis.** Dossier 2 : clé Anthropic 4,10 (le devis dit 4,09), Google 11,76 (11,77), pire absolu 43,48 (43,49). Variante avec Fable : 12,40 sur la clé Anthropic (12,39). Dans le tableau, écrire « de 6,0 à 7,3 » au lieu de « de 6 à 7,5 ».

**8. Mineur.** `GO_ID=` n'est lu ni par le programme ni par le crochet : consigner l'accord au registre. Écrire `collisionneur_v9_v8m.py verifier runs/…`. La citation « aucune retouche ne bloque l'envoi » n'est pas verbatim (le rapport : « Aucune retouche bloquante »). Ajouter Neon : 3 500 × 5,1 = 17 850 < 32 768. La provision est comptée, non envoyée. Les « 90 USD » sont sans source.

## Vérifié et tenu

- Cellules et totaux (15,90 ; 15,86 ; 24,31 avec Fable) rejoués à l'identique.
- Octets, mots, empreintes, garde `[]` (assemblages compris) et sceau `420394f9…` justes.
- Relances conformes : deux pour Google, une pour Opus sans `--effort-max`.
- Réglages : 16 384 ≥ 16 000 ; 14 700 < 16 384 ; niveaux maximaux.
- Options existantes ; `--nom-espace-anthropic` superflue ; la ligne tient si `--plafond-usd` est oublié.
- Attendu (6,01 ; 7,26 ; 1,70 pour Opus) : option B, bras principal, étage III du devis voisin ; reprise honnêtement marquée.

## Fichiers ouverts

- le devis ;
- `collisionneur_v9_v8m.py` et `garde_google_v3.py` (extraits) ;
- `question-neutre-collisionneur-demande-1-v2.md` ;
- `faits-neutres-demande-1-v3.md` (lignes ajoutées depuis la v2) ;
- `test-neutralite-devinette-v1.md` (extraits) et `verification-neutralite-textes-v2-v1.md` ;
- `registres/go.md` d'`origin/main` (l. 892-896) ;
- le devis voisin (§ 0-2) ;
- `.claude/hooks/garde_calcul.py` (en-tête).

Dossier 2 : contrôle par programme seulement.
