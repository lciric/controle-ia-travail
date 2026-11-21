# Contrôle de la conception v4 du véhicule NA-1 — v1

- Contre-lecteur, modèle O : le même que pour la v1, la v2, le lot 0 et la v3 (règle R2). Je n'ai écrit ni la conception, ni le relevé, ni la v9, ni aucun orchestrateur.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 08:02:05Z, après la lecture, avant l'écriture.
- Processeur seul : aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt.
- Je n'ai ouvert ni branche de quarantaine, ni la branche de la matière première, ni son registre servi.
- Aucun refus de permission, de classifieur ni de garde rencontré.
- Objet : les seuls points de ma contre-lecture de la v3 (`80e064d0…`) et les mots de la mère de 07:46Z, de 07:51Z et de 08:00Z, ces derniers transmis par la coordination.

## Pièces

| pièce | empreinte | contrôle |
|---|---|---|
| conception v4 (CO4) | `3428dfb348c8f367060f587b5953d3c05ed329055f29b07e046ac3538ced2804` | égale au compagnon et au mandat |
| différentiel v3 → v4 | `bd4ee39eeb9cdd6e0ccf5734cd079e0d0616f5e437cc76034bbfa772f797d5ee` | égale au compagnon |
| rapport v4 (RC4) | `0fee3bf3f4566467d97a7e3ffe8d852662749c2720454479f5416549e8bcc1e7` | égale au compagnon |
| table v4 | `6f89eb0826eda512a691f9a8899d09918a984ab9b70a3f7dfd409b2c3a7e7705` | égale au compagnon |

## Verdict

**À corriger, sur A3 et sur l'écriture des mots de 08:00Z seulement**, plus deux retouches de lettre (§ 7). Mes trois défauts de la v3 sont résolus. Le réencodage est juste. Les mots de 07:46Z et de 07:51Z sont portés comme tranchés. Le calendrier est juste.

Les lots 1 à 5 ne touchent ni A3 ni les points de 08:00Z : leurs mandats peuvent partir dans l'ordre du chemin critique. Le mandat du lot 6 attend la v5 courte, qui porte A3. Le lot 10 a attend que la v5 écrive l'état 1 comme tranché.

## 1. Mes trois défauts

1. **Le portier neuf : résolu.**
   - CO4, § 2.4 en fait un code neuf. Il n'appelle ni l'aiguilleur du noyau ni sa lecture (`aiguilleur_v53.py`, l. 30 et 41 à 46, cités juste).
   - Il fait deux sortes d'appel (fiche ; réponse sans fiche), par `self.appel`, donc par la surcharge, et lit les seules étiquettes de D3. Une étiquette hors liste, double ou absente vaut « illisible ».
   - Il délivre ses propres passeports ; l'étape « aiguillage » est surchargée (§ 2.9).
   - Épreuve (§ 6.2) : `a_corriger` donne « illisible », la fiche va au coffre, et l'aiguilleur du noyau n'est jamais appelé.
2. **Le refus écrit, rôle par rôle : résolu.** Table du § 2.13 :
   - proposeur : la case est non jouée et comptée ;
   - portier, appel « fiche » : la fiche va au coffre, classe écrite, au dénominateur de M3 (mère, 07:51Z) ;
   - portier, réponse sans fiche : « réponse illisible », avec un sous-compte ;
   - juge : un verdict absent.

   Aucune fiche rendue ne reste sans classe.
3. **La surcharge de `juger` : résolue.**
   - CO4, § 2.5 : elle exige le passeport du portier neuf, sert l'identifiant réencodé (quatorze lettres) fait des mêmes octets, passe par la surcharge d'`appel` et lève l'arrêt d'A2.
   - Épreuve : une fiche munie du seul passeport du noyau est arrêtée ; la mutation « identifiant du noyau » fait mordre l'arrêt n° 16.
   - *Retouche* : le refus « sans passeport » est la garde héritée A17 (`SansPasseport`, `aiguilleur_v53.py`, l. 33). Elle manque à la table du § 2.13. À rattacher comme arrêt nommé, puisque c'est un défaut de programme, et à nommer.

## 2. Le seuil A3 : 1 + ⌈150 / c⌉, et la valeur d'un million

**La formule n'est juste qu'à une condition.** Elle borne le nombre d'appels d'un rôle par l'argent : au plus ⌊150 / c⌋ appels dans une génération, s'il est vrai que **chaque appel que le suivi compte coûte au moins c**. Or un appel en erreur peut déclarer un coût nul : erreur d'accès, refus du relais avant toute génération de texte. Le noyau ne remplace par le plafond qu'un coût absent, non un coût nul (`noyau_v56.py`, l. 170). Ces appels-là échappent à la borne, alors que ce sont justement les échecs consécutifs qu'A3 compte. La formule n'est donc pas une borne sûre. Les trois valeurs posées (750 octets, quatre octets par jeton, le tarif repère) ne changent rien à ce défaut de principe.

**La valeur d'un million revient à neutraliser A3.** Aucun rôle ne peut l'atteindre. Présentée comme un « seuil chiffré », elle ne l'est pas : c'est une désactivation qui ne dit pas son nom. La règle 4 de la mère n'est pas violée dans son effet (aucune garde n'arrête sans écrire sa cause, et le pas 0 attrape tout arrêt). Elle l'est dans sa forme, que la mère a précisée à 08:00Z : aucune garde n'est neutralisée en silence.

**Mon avis sur les deux voies de la mère (08:00Z) : je recommande la voie 1, A3 désactivée par écrit avec une garde de remplacement. Confiance 0,75.**

**Pourquoi pas la voie 2 (un seuil chiffré depuis le plan) :**
- Le plan ne borne que le proposeur : 11 appels par génération. Il ne borne ni le portier ni les juges, dont le nombre d'appels suit le nombre de fiches rendues, qu'aucune lettre ne borne (CO4, § 2.13).
- Un seuil qu'on peut atteindre arrête un rôle sur une suite de réponses sans texte (erreurs, coupures). Ce sont des « réponses illisibles », une classe de M6 (V9, l. 99), et la V9 dit : « Aucun seuil d'arrêt n'est posé sur M6 » (l. 101). Un seuil atteignable serait donc un écart à la V9.
- Depuis la v3, la lecture rend toujours un objet quand un texte est rendu. A3 ne compterait plus que des appels sans texte : c'est précisément cette part de M6.

**Ce que la voie 1 doit écrire, à mon avis :**
1. « A3, échecs consécutifs : **désactivée** pour tous les rôles de cette course », avec sa raison (V9, l. 97 et 101) et sa mise en œuvre : une valeur hors d'atteinte, déclarée comme désactivation, vérifiée au départ par la configuration.
2. **La garde de remplacement porte sur les refus écrits, non sur M6.** Un refus écrit n'est pas une classe de M6 ; il ne naît que d'une garde héritée qui arrête malgré sa mise hors d'état. La borne, chiffrée depuis le plan :
   - pour un proposeur, 11 refus écrits dans une génération, soit toutes ses cases : arrêt nommé de course, parce que le rôle entier manque et que la composition gelée n'est plus tenue (même raison que pour A2) ;
   - pour le portier, chaque refus écrit envoie une fiche au coffre : l'arrêt n° 5 (strictement plus d'un quart au coffre) borne déjà ce cas ;
   - pour un juge, verdicts absents, comptés et rapportés (I1 seulement).
   - Cas sain : aucun refus écrit, aucun arrêt. Artefact : un rôle marqué arrêté par l'essai donne des refus écrits comptés, puis l'arrêt nommé à 11 pour un proposeur.
3. **Le délai d'A3** (aligné sur 3 600 s) n'est pas touché. Un appel coupé reste lu « réponse illisible ».
4. **A14** est de même nature (une part de M6). Elle est déclarée « désactivée par écrit » de la même façon, et non « inerte ».

## 3. Le réencodage, base 60, longueurs fixes de 18 et 14 lettres

- **Juste.** 60⁹ ≈ 1,008 × 10¹⁶ ≥ 2⁴⁸ ≈ 2,815 × 10¹⁴, et 60⁸ ≈ 1,68 × 10¹⁴ ne suffirait pas : neuf syllabes, dix-huit lettres. 60⁷ ≈ 2,80 × 10¹² ≥ 2⁴⁰ ≈ 1,10 × 10¹², et 60⁶ ≈ 4,67 × 10¹⁰ ne suffirait pas : sept syllabes, quatorze lettres. Ordre de l'entier fixé (premier octet le plus fort), complément à gauche par la syllabe de rang 0, rang = 5 × consonne + voyelle.
- **Aucune suite hexadécimale possible.** Les douze consonnes (g, j, k, l, m, n, p, r, s, t, v, z) sont toutes hors de a à f. Seules deux voyelles, a et e, sont des lettres hexadécimales, et chaque voyelle est suivie d'une consonne ou termine le mot : la plus longue suite hexadécimale fait **un** caractère. Aucun chiffre.
- **Réversible.** La longueur est fixe et le découpage en syllabes unique, puisque chaque syllabe fait deux lettres. Le décodage refuse une longueur fausse, une lettre hors alphabet et un entier au-dessus de 256 puissance le nombre d'octets, sans rien corriger. Les longueurs 6, 14 et 18 ne se confondent pas.
- L'épreuve dans les deux sens est écrite : bornes à zéro et à 255, mots fautifs, mutation « ordre des octets inversé » (§ 6.2).

## 4. La v9, l. 83, et la branche B

- **Fidèle.** La lettre est citée exactement : « Dehors : identifiants, empreintes, tailles, comptes par case. Ni énoncé ni nom de mode dans un registre du dépôt, une passation ou un message. » La ligne interdit qu'un énoncé ou un nom figure en trois lieux ; le chargeur n'y écrit rien et ne garde que des empreintes, que la même ligne range « dehors ».
- La limite que note le concepteur est juste : le registre servi est lui-même un fichier du dépôt.
- **La mère a tranché à 08:00Z** : lecture B. Le registre servi est une **entrée** de la course, versée sous GO-2026-11-21-19, et la l. 83 vise les **sorties**. La « garde seule » reste le défaut ; le chargeur ne garde que les 35 empreintes, et rien n'est écrit ailleurs.
- La v5 doit écrire ce mot comme tranché, dans les termes de la mère (entrée contre sortie), plutôt que dans l'argument du concepteur, qui reste exact. Elle retire la branche A comme hypothèse ouverte (§ 2.14 ; § 9, point 18) et la dépendance du lot 10 a au « mot de la mère sur la l. 83 » (§ 7, table, lot 10 a).

## 5. Les mots de la mère, portés comme tranchés ?

| mot | dans la v4 |
|---|---|
| portier neuf | oui (§ 2.4) |
| fiche refusée au portier : au coffre, classe écrite, comptée | oui (§ 2.4, § 2.13) |
| seuil A3 chiffré pour le portier et les juges, cas sain et artefact | écrit, mais la valeur neutralise A3 : à refaire selon 08:00Z (§ 2) |
| surcharge de `juger` avec passeport | oui (§ 2.5, § 2.9) |
| réencodage écrit et éprouvé dans les deux sens | oui (§ 5.2, § 6.2) |
| sous-compte « cause non établie » | oui (§ 2.3, § 2.7, § 2.8) |
| A2 arrêt nommé de course | oui (§ 2.13 ; § 2.3, pas 7) |
| « dans l'ordre » retiré | oui (§ 2.4, § 5.4, § 9, point 20) |
| « garde seule » par défaut, lot 10 a obligatoire, joué avec les lots 6 et 7 | oui (§ 0, § 2.14, § 7, § 8) |
| comparaison sur l'énoncé entier, par empreinte, jamais sur le nom court | oui (§ 2.14 ; épreuve § 6.2 : le nom court et la reformulation passent, ce qui est voulu) |
| les deux lecteurs d'antériorité parmi les juges de fin, après la clôture | oui (§ 2.14, § 2.15) |
| branche orpheline par le graphe | oui (§ 2.15 ; épreuve sans lecture d'objet) |
| l. 83 citée à la lettre, deux branches | oui ; tranchée depuis (08:00Z) : à écrire (§ 4) |
| dernier octet posé à la mère | oui (§ 5.3) ; tranché depuis (08:00Z) |

**Mots de 08:00Z, que la v4 ne pouvait pas porter, à écrire dans la v5 :**
1. Le dernier octet est **gardé**, et l'empreinte se calcule sur la pièce entière (§ 5.3 ; RC4, § 4, point 1).
2. La l. 83 : lecture B, dans les termes de la mère (§ 4 ci-dessus).
3. L'état 1 ne demande **pas** d'additif à la V9. Il s'écrit au **complément de valeurs**, avec son empreinte. La v5 doit nommer la pièce qui le porte : CV, l. 68 dit « il n'y a pas de lot 2 » et fait valoir la pièce de relevés comme complément. L'état 2 demande l'additif, l'arrêt n° 14, le devis et le mot de Lazar (§ 2.14, table de l'interrupteur ; RC4, § 4, point 3).
4. A3 : l'une des deux voies, écrite (§ 2).

## 6. Le calendrier

- Lots : 1,75 + 2 + 2 + 5 + 6 + 7 + 3 + 6,5 + 4,75 + 3 = **41 h**. Juste.
- Chemin critique : 2, 3, 5, 6, 8, 9 = 2 + 2 + 6 + 7 + 6,5 + 4,75 = **28,25 h**. Juste. Le lot 10 a (3 h), joué avec le lot 6 (7 h), n'y entre pas ; le lot 9 l'attend.
- Le choix de la voie 1 pour A3 coûte de l'ordre d'une demi-heure au lot 6.
- L'attente de 48 à 60 h et l'échéance du 27 « avec une marge mince » restent honnêtes.

## 7. Ce que la v5 courte doit porter

1. **A3** selon la voie choisie par le concepteur, sur l'avis du § 2. Ma recommandation : la voie 1, désactivée par écrit, avec une garde de remplacement sur les refus écrits (11 pour un proposeur, arrêt nommé ; arrêt n° 5 pour le portier ; rapport pour les juges), cas sain et artefact. A14 traitée de même, « désactivée par écrit ».
2. **Les mots de 08:00Z** comme tranchés : dernier octet gardé, empreinte sur la pièce entière ; l. 83 en lecture B, entrée et non sortie, et retrait de la branche A et de la dépendance du lot 10 a ; état 1 au complément de valeurs, la pièce nommée ; état 2 sous additif, arrêt n° 14, devis et mot de Lazar.
3. **Retouche** : A17 (passeport manquant) ajoutée à la table du § 2.13, rattachée à un arrêt nommé.
4. **Retouche** : § 7, « Chemin critique » : « cette v3 et sa contre-lecture » devient « cette v4 (ou v5) et sa contre-lecture ». Au § 9, point 21 et au rapport, retirer des points ouverts ce que la mère a tranché à 08:00Z.

— contre-lecteur de la conception du véhicule, modèle O
