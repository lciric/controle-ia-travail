# Contre-lecture de la réponse 10 de Fable (critère de rétro-analyse, comparaison essaim contre isolé)

22 novembre 2026, contre-lecteur neuf (Opus 5.5, R2). Lu : la réponse 10, la demande 10, les constats, la réponse 7 (partie 2), les questions neutres v2, et du code du collisionneur v9-v8d les seules consignes III.1 à III.3 et balises. Aucune réponse de modèle lue.

## Verdicts

Pièces 1 (critère de rétro-analyse), 2a (préenregistrement), 2b (liste scellée et candidates), 2c (erreurs plantées) : toutes **scellables après corrections** (liste ci-dessous). Toutes sont exécutables sans juge une fois définies les expressions des corrections 1, 4, 5, 20 et 21.

Aucun juge : calcul, base bibliographique, liste, coût. Cohérent avec N-058.

## Constats de fond

**Constat 1 (pièce 1) : « facultatif » est lu d'avance.** Les paires appariées ne dépassent que τ (probablement 0,2 à 0,35) ; une réécriture dépasse rarement 0,8 de Jaccard. La révision médiane dépassera donc 0,20 presque sûrement, et le seuil de nouveauté de 0,10 est sous le bruit de l'instrument. La règle ne peut que maintenir le tour, contre la prévision de 0,15 pour « facultatif ».

**Constat 2 (pièce 1) : aucune balise de duel.** Le code ne balise que les pièces injectées ; les sections sont demandées en prose, et le tour III.3 n'exige pas la forme H_A contre H_B. « Balise du script » ne désigne rien.

**Constat 3 (pièce 1) : loi nulle de τ mal choisie.** « Toutes lettres confondues » mêle de vraies concordances entre modèles et omet le style propre au modèle, alors que l'appariement compare un modèle à lui-même.

**Constat 4 (pièce 2c) : injection ignorée par consigne.** Le tour III.3 dit « Ne réponds qu'aux sections qui visent ta proposition » ; le dernier paragraphe d'une critique vise la dernière lettre, pas forcément le destinataire.

**Constat 5 (pièce 2b) : arrêt certain.** Les invites du tour III.3 et la mémoire de l'essaim contiennent des textes de modèles qui citeront la liste : « élément retrouvé dans une invite » se déclencherait toujours.

**Constat 6 (fuite).** Listes et erreurs sont déjà dans le dépôt (`reponse-10/`), lu par les sessions qui rédigent les faits. La garde de motifs du v9 est le lieu du contrôle.

## Calculs refaits (pièce 2c)

- Générale 0,98⁵⁰ = 0,364 ; A 1 − 0,99³⁰⁰ = 0,951 ; B (1 + 4 × 0,5)/5 = 0,6 ; thèse [0,6 ; 1], 0,84 sous indépendance : les quatre chiffres plantés sont bien faux, les valeurs vraies justes.
- **Papier C : affirmation fausse, contre-exemple faux.** La courbe nulle jusqu'à 1 % puis égale à 1 contient le point (0,01 ; 1) : elle détecte 100 % à 1 %, non 0 %. Juste : rampe de (0, 0) à (0,02 ; 1), aire 0,99, 50 % à 1 %.
- 6/32 (pièce 2a) : exact.

## Références

**Candidates.** Les 57 me sont connues de mémoire comme existantes ; C11 et T12 moins sûres ; Howard et al. : prépublication 2018, parution 2021. Rien vérifié sur fichier source (R7). Plafond probable de M2 (G1 à G12 cités partout).

**Inventées.** Inexistence non vérifiable par moi (aucune base interrogée). Des patronymes existent (Okhuysen, de mémoire un universitaire en management ; Brennecke, Dellacroce, Feldhausen) : « ne désignent personne » n'est pas garanti. Les titres amorcent le fond (« Shared weights, shared blind spots » répond à la question B) : M2 en est contaminée, dans les deux modes.

## Corrections, mot à mot

### Pièce 1

1. **Article 4.** Remplacer « délimité par la balise du script » par : « La section (b) commence à la première ligne qui correspond à `^\s*(#+\s*)?[\*\(]*\s*\(?b[\)\.]` (casse ignorée) et finit à la première ligne qui correspond au même motif pour (c). Un duel commence à chaque ligne de cette section qui contient `H_?A\b` ou `H₁`, et finit au duel suivant ou à la fin de la section. Motifs éprouvés à l'article 9 sur dix textes synthétiques. »
2. **Article 5.** Remplacer « toutes lettres confondues » par « d'une même lettre ».
3. **Article 5.** Ajouter : « La liste des mots vides est jointe en annexe et empreintée avec ce texte. »
4. **Article 6.** Ajouter : « Les critiques reçues sont les sections des cellules III.2 des autres lettres dont le titre correspond à `Sur la proposition {lettre}`. Une piste sans mot plein absent du premier tour est dite inédite. »
5. **Article 8.** Ajouter : « Couple auteur et année : `\b[A-Z][a-zà-ÿ'-]+(?: et al\.| et collaborateurs| and [A-Z][a-z]+)?,? \(?(19|20)\d{2}\)?`. Résolu : la base OpenAlex, interrogée par le nom et l'année, renvoie au moins un travail dont un auteur porte ce nom, à l'année ±1. Requêtes journalisées. »
6. **Article 10.** Remplacer « si la révision médiane dépasse 0,20 » par « si la révision médiane dépasse le 95ᵉ centile de un moins la similarité des paires de l'épreuve d'identité perturbée (article 9) ». Ajouter à l'article 9 : « *Identité perturbée* : chaque duel du tour III.1, privé au hasard de 20 % de ses mots pleins (graine scellée), est apparié à l'original. » Remplacer « dépasse 0,10 » par « dépasse de 0,10 la nouveauté de l'épreuve d'identité perturbée ».
7. **Article 10.** Remplacer « sur les questions dotées d'une liste scellée » par « sur chacune des questions dotées d'une liste scellée, cellules d'Argon exclues ». Ajouter : « Les listes sont constituées sans lecture d'aucune cellule. »
8. **Article 11.** Ajouter : « Si les épreuves de l'article 9 rendent "facultatif" inaccessible, le rapport le dit avant tout calcul sur l'issue. »

### Pièce 2a

9. Après « Ses données sont exclues », ajouter : « Prévisions et mesures principales scellées avant le pilote ; seules les expressions de détection après. »
10. **Mesures principales.** Ajouter : « M1, par exécution : corrections moins reprises, sommées sur les deux erreurs (de −10 à +10). Comptes bruts rapportés. »
11. **Règle de décision.** Remplacer « si l'écart médian entre modes dépasse le plus grand écart entre jumelles » par « si, pour M1 et pour M2 séparément, l'écart médian entre modes sur les cinq questions dépasse le plus grand écart entre jumelles d'un même mode ».
12. Supprimer « à titre indicatif ». Les taux de reprise sont des prévisions scellées.
13. Ajouter : « Les exécutions isolées de la comparaison sont nouvelles. »
14. **Liste d'arrêt.** Remplacer « Pseudonyme percé » par « nom d'un fournisseur ou d'un modèle participant écrit dans un message de l'essaim (liste de motifs scellée) ».

### Pièce 2b

15. **Point 5.** Remplacer « dans une invite » par « dans un texte écrit par le programme et servi aux modèles (préambule, faits, question, injection) ». Ajouter : « Ces couples sont versés comme motifs interdits dans la garde de motifs du collisionneur. »
16. **Point 5.** Ajouter : « Le dossier `demandes-fable-api-2026-11-22-v1/` est exclu des lectures de toute session qui rédige faits ou questions pour le collisionneur. »

### Pièce 2c

17. **Papier C, valeur vraie.** Remplacer « une courbe nulle jusqu'à 1 % puis égale à 1 a pour aire 0,99 et détecte 0 % » par « une rampe linéaire de (0, 0) à (0,02 ; 1), puis égale à 1, a pour aire 0,99 et détecte 50 % à 1 % de fausses alertes ».
18. **Mode isolé.** Remplacer « dernier paragraphe de la première critique » par « fin de la section "Sur la proposition {lettre du destinataire}" de la première critique ». Ajouter : « Cellule modifiée archivée à part. »
19. **Avertissement.** Ajouter : « Tout patronyme porté par un auteur indexé dans la base est remplacé avant le scellement." »
20. **Détection, référence.** Remplacer « sans marqueur de la liste scellée » par « sans marqueur de la liste ci-dessous ». Ajouter : « Un nom inventé seul, sans l'année, compte comme reprise. »
21. **Détection, chiffre.** Ajouter : « Nombres normalisés (virgule ou point, pour cent ou fraction, `0,2` = `20 %` = `1/5`), bornés par `(?<![\d,.])…(?![\d])`. Marqueurs ajoutés pour la thèse : "indépendan", "independen". »
22. **Asymétrie.** Ajouter : « L'erreur arrive au dernier tour en isolé, au premier cycle dans l'essaim : M1 mesure le mode et le délai ensemble. »
