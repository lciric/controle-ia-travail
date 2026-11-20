# Contre-lecture de l'additif 1 au préenregistrement court v9, du devis v7 et du calcul v6 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 13:56:46Z, après les rejeux et les relevés, avant l'écriture. Contre-lecteur neuf, modèle O : je n'ai écrit ni lu, avant ce mandat, aucune version du préenregistrement court, du devis, de la question, de la note de périmètre, de la partie servie, du complément de valeurs ni de leurs contre-lectures. Mandat : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-v1/mandat-contre-lecteur-additif-1-v9-devis-v7-v1.md` (`799b14c63be98386f435e7cb6dae880e432838c9c0347886e51f282d7ecbbf09`, recalculée). Processeur seul : aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Aucune méthode d'attaque, aucun procédé, aucun nom ni énoncé de mode, aucune case nommée, aucune valeur de clé, aucun identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**À corriger.** Vingt corrections : quinze sur l'additif (A1 à A15), cinq sur le devis v7 (D1 à D5). Aucune ne change un total, un plafond, un seuil, un tirage ni une condition de GO-2026-11-20-59 ; dix-huit sont de lettre ou de renvoi, deux (A9, A10) précisent la suite d'un arrêt neuf et sont à accepter par la mère. Les chiffres sont justes au centime : le calcul v6 rejoue à l'octet, l'outil rejoue le devis v7 à l'octet, et mon recalcul indépendant retrouve chaque chiffre. **Un point pour la mère prime sur les corrections** : GO-2026-11-20-62 (13:44Z, après l'écriture de l'additif) demande que l'écart au garde-fou 6 pour le fournisseur de l'espèce 2 soit écrit « dans l'additif 1 de la v9 » ; l'additif ne le porte pas (§ 9, point 1).

## 1. Pièces et empreintes

| pièce | empreinte | vérification |
|---|---|---|
| mandat du rédacteur v2 | `39482c8e…c5e6` | recalculée |
| additif 1 v1 | `0f79de55fd94c81b22185bd5e04e41d9c0f6aee335050c7063997ecc28a8f9be` | compagnon « OK » |
| devis v7 | `bd92d8661935c34617fdcc97ac21981608dacc2ae71cbaab0be406921643e518` | compagnon « OK » ; rejeu `cmp` égal |
| calcul v6 | `b622bca0850bcf47f1ee11b6f0e14e058df0e7dd3c66fa7f93016d19a5d36d54` | compagnon « OK » |
| sortie du calcul v6 | `096597dfc48543d08b470a19622d0ab10de985220032674f91664e81bea8337b` | compagnon « OK » ; deux rejeux égaux |
| jeu devis v6 → v7 | `4b9c6b9c68aa7c56535d3cc381d4511478b83d5368cc8af0034a5e27c338ace1` | compagnon « OK » |
| différentiels devis et sorties ; rapport du rédacteur (`741fd0cf…`) | — | compagnons « OK » |
| v9 scellée, `origin/main` (`e16fc79dc`) | `864f39a7…00c2` | recalculée ; lue en entier, lignes 1 à 430 |
| devis v6 scellé, aux deux chemins de `main` (`prereg/ideation-nouvelles-attaques-v1/` et `NA/preenregistrement-court-v7/`) | `d825cb31…9c2c` | recalculée aux deux chemins |
| calcul v5 et sa sortie | `cdec1d2d…f1e8` ; `2a0d2a58…b2c` | recalculées |
| ordre de course v3 | `b12cdc12…9e22` | recalculée ; § 10, ligne 144 lue |
| N-054, `docs/decisions/decision-N-054-v1.md`, sur disque et sur `main` | `c8a00b3f…4c2f` | égales ; compagnon « OK » |
| `registres/go.md` et `registres/decisions.md` cités par l'additif au commit `5f317ad8…` | `a70e220a…` ; `e28321c0…` | sur `origin/main` (`e16fc79dc`) les registres ont grandi (GO-2026-11-20-61 et -62 ; R-4278 à R-4280) ; leurs 591 et 4 415 premières lignes rendent exactement `a70e220a…` et `e28321c0…` : les lignes citées sont celles de `main` |

## 2. Rejeux

- Calcul v6, deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN SORTIE`) : les deux sorties valent `096597df…337b`, égales à la sortie rendue. Le programme écrit dans le fichier passé en argument et refuse la sortie standard : la redirection `>` du mandat ne s'applique pas (écart C1, § 10).
- Outil `scripts/remplacer_texte_exact_v1.py` (`391db990…3d6`) avec le jeu sur le devis v6 : 15 remplacements, sortie `bd92d866…e518`, `cmp` égal au devis v7.

## 3. Recalcul indépendant

Programme `recalcul_independant_cinq_especes_v1.py` (module `decimal`, arrondi au demi supérieur ; constantes recopiées du calcul v5 et de la v9 ; espèce 6 retirée ; joué deux fois, sorties égales, `cmp`). Tout est égal au centime à la sortie du calcul v6 et au texte :

| chiffre | recalcul | calcul v6 / additif |
|---|---|---|
| ligne de course ; plafond d'une génération ; seuils | 450 ; 150 ; 140, 135, 120 | idem |
| plafond total | 456 | idem |
| attendu (cas bas, lignes à part estimées comprises) | 218,72 | idem |
| cas haut | 419,43 | idem |
| Minuit : bas, haut, rapport | 20,58 ; 105,05 ; 1,547 | idem |
| Luc : bas, haut, rapport | 66,51 ; 124,35 ; 1,721 | idem |
| Rigaud : bas, haut, part avant recharge, rapport | 22,29 ; 26,61 ; 38,65 ; 1,452 | idem |
| les trois : bas, haut, borne, borne / haut | 109,38 ; 256,02 ; 415,21 ; 1,622 | idem |
| ligne moins borne ; ligne moins 423,56 | 34,79 ; 26,44 | idem (lignes 235 et 191 de la table de l'additif) |
| règle de choix | 12 répartitions admissibles ; seule la retenue au meilleur, 1,4522 | idem |
| deuxième relais | 93,90 ; 140,39 ; part au pire 450 | idem |
| troisième relais | 14,25 ; 17,01 ; reste estimé 8,91 à 11,51 ; manque au bas 2,74 à 5,34, au haut 5,51 à 8,11 | idem |

Remarque, sans correction : la somme des quatre lignes arrondies du premier relais fait 256,01 ; 256,02 est la somme non arrondie, celle de la table de la v3 et de GO-2026-11-20-22. La v9 disait, à six espèces, « 289,30 (289,31 sans arrondir les lignes) » ; l'additif ne donne que 256,02. Sans suite.

## 4. Première partie — le mode tenu à l'écart

**Source.** Juste, à la lettre : ordre v3, § 10, ligne 144 (citée depuis « La mère conçoit… », la phrase d'amorce « Une conséquence à connaître. » omise sans dommage) ; v9, ligne 65. Motif : R-4274, cité exactement. GO-2026-11-20-59, point 1 : cité exactement jusqu'à « avant toute lecture. » ; la phrase suivante (qui écrit, qui contre-lit) n'ajoute aucune condition. GO-2026-11-20-57, point 4 : extrait juste. N-054, point 3 (lignes 40 à 42) : juste. **Mais** la citation « sans aucune pièce des moniteurs », donnée comme de N-054 dans la condition (b), vient de sa ligne 60, sous « Ce que la décision ne fixe pas (reste à proposer) » : une proposition, non une décision (A8).

**Les trois conditions** sont reprises à la lettre de l'accord. Chacune a son arrêt et son épreuve sur cas sain et artefact.

- **(a), arrêt n° 24.** Vérifiable : pièce « choix de la carte » scellée en quarantaine, journal des lectures (arrêt n° 18). Trou 1 : si la lecture hors règle est constatée après que le mode a été conçu avec la carte, l'arrêt dit seulement que la carte « ne nourrit pas » ; il ne dit pas ce que devient le mode déjà conçu. L'arrêt n° 25 le dit (« déclaré « vu » ») ; A9 l'écrit pour le n° 24, A10 pour le n° 26. Trou 2, plus lourd, déjà nommé au silence 4 : l'instance qui conçoit le mode doit lire la carte et n'est pas à la liste nominative ; la remise de la carte tombe donc sous l'arrêt n° 18 (ou n° 17 hors quarantaine). Tant que ce silence n'est pas tranché, la levée ne peut pas servir (A13).
- **(b), arrêt n° 25.** Vérifiable par un programme qui confronte un inventaire scellé à la liste des pièces des moniteurs ; mais cette liste n'existe pas (silence 3) : sans elle, l'épreuve ne se joue pas (A12). La limite dite au § 2 (chemins et empreintes, non ce qu'une instance a vu par une autre voie) est juste.
- **(c), arrêt n° 26.** Vérifiable : empreinte du choix de la case avant la première ligne du journal des lectures ; vérification par programme, sur les identifiants, en quarantaine. Le classement des juges étant en quarantaine, sa lecture fait une ligne du journal : il est couvert. Ce qui n'est pas couvert, à la lettre : les comptes par case (M3, M6, M7), qui sortent de la quarantaine et peuvent précéder le choix ; ce ne sont pas des lectures de fiche (point pour la mère, § 9). Le troisième cas de l'arrêt (une fiche de la case citée par une pièce de conception) déclare le moniteur « spécialisé », ce que la v9, ligne 86, impose déjà pour toute fiche de la course ; la suite pour le mode tenu à l'écart face à ce moniteur n'est pas tirée : c'est le nœud de Lazar que l'arrêt nomme (§ 9).
- « La case entière » est une des trente-trois cases servies : juste (la case de la sonde, en réserve, ne rend aucune fiche).

**Les neuf silences du § 4.**

| n° | jugement |
|---|---|
| 1 | juste, à trancher par la mère ; la phrase sur le tirage est imprécise : la v9 ne prévoit de clé neuve que pour l'identifiant neutre (ligne 254) et dit « Aucune autre méthode de tirage n'est permise » (ligne 311) (A11) |
| 2 | juste, à trancher |
| 3 | juste, à trancher ; bloquant pour l'épreuve de l'arrêt n° 25 (A12) |
| 4 | juste, à trancher ; bloquant pour toute la levée (A13) |
| 5 | juste : c'est le risque résiduel de R-4274 ; à garder comme réserve ou à trancher |
| 6 | juste : l'accord dit « la carte » |
| 7 | juste |
| 8 | juste ; aggravé depuis GO-2026-11-20-62 : le fournisseur de l'espèce 2 garde les envois, registre servi compris, qui peut porter des noms et énoncés de fiches de la case retirée (§ 9) |
| 9 | juste, à trancher |

## 5. Seconde partie — le retrait de l'espèce 6

**La v9 relue en entier**, ligne à ligne, contre la table du § 6.

- **Numéros de ligne** : tous exacts (45, 51, 61, 67, 133, 144–163, 171–175, 191, 197–207, 209–223, 225–233, 235, 236, 247, 250–252, 264, 266–272, 298, 313, 340–365, 373, 377, 378, 382–384, 402, 404, 411, 412), sauf **276 à 293** : la table « un par un » finit ligne 294, la ligne « relais | trois | quatre », que la règle neuve vise (« trois relais ») (A1). L'écart 8 du rapport est donc levé, à une plage près.
- **Lieux manquants** : ligne **101** (« le volume attendu de fiches (de l'ordre de 338) peut baisser ») ; ligne **127** (« la composition à six espèces » parmi ce sur quoi l'erratum de l'ordre ne dit rien : à cinq espèces, les deux textes ne diffèrent plus sur ce point) ; ligne **387**, arrêt n° 16 (« pour les deux sondes de refus ») (A2, A3). L'arrêt n° 16 change donc de lettre : la phrase « ne change pas » du § 6 le compte à tort parmi les arrêts inchangés (A4). Lignes 7 et 47 : la règle « rien ne court avant le mot de Lazar sur le devis neuf » (ligne 7) et le versement du devis v6 (ligne 47) sont rattachés aux lignes 412 et 45 (A5, A6). Ligne 32 : « devis » seul renvoie au devis v2 ; la règle neuve « les renvois au devis se lisent sur son § 10 » pourrait se lire comme changeant ce renvoi (A5). Lignes 14, 274, 385 et 400 : rien à écrire (la phrase de version de la v8 est histoire, et sa règle tombe avec la ligne 264 ; « chaque sonde de refus » reste vrai ; « les deux lignes à part » de la ligne 400 redevient exact).
- **Règles neuves** : justes. Lignes 171 à 175, 191, 197 à 207, 225 à 233, 235 : chiffres retrouvés (§ 3). Ligne 225 à 233 : la clé la plus serrée devient Rigaud, et la règle de choix ne trouve pas mieux (12 admissibles, une seule au meilleur) : juste. Ligne 383 : « les trois autres cas restent » (cas sain et deux artefacts) : juste ; la ligne doit renvoyer à l'extension que le complément portera (A7).
- **« Aucun tirage ne change »** : juste. La racine, les clés 0 à 3, 12, 13 et 20, les comptes 11, 33, 20, 67 et la borne de 60 ne dépendent pas du nombre d'espèces (lignes 279 et 280). Seuls les n des clés 12, 13 et 20 (lignes du registre, fiches qui passent la relecture) baissent ; ils n'étaient fixés d'avance à aucune composition. La phrase du § 5 le dit trop vite (A15).
- **La sonde des espèces 1 à 5** : les deux règles que l'additif lui reporte (partie servie remplie, seule ; première case de la réserve) étaient déjà dans la v9 (lignes 77, 268 et 313, « aux sondes de refus ») ; garde de motifs et journalisation : lignes 77 et 387. Juste. Ce que le paragraphe retiré portait et qui n'a jamais été écrit pour la sonde des espèces 1 à 5 — refus pour crédit, erreur d'accès, réponse que la garde ne sait pas lire — reste non écrit ; l'ordre, § 3 (ligne 52), n'en dit rien non plus. Ce n'est pas un recul de l'additif ; c'est un silence (§ 9).
- **Arrêts n° 2, 6, 7, 11, 12, 13** : lettres neuves justes. Le n° 2 garde « retirée de tous les rôles » et « version neuve et mot de Lazar ».

## 6. Le devis v7

- **Couches datées** : la phrase de version pose deux règles — ce qui vaut est au § 10 et dans les passages qu'il nomme ; ne valent plus les passages marqués « v3 », « à six espèces » ou « v6 ». Un passage à six espèces n'est pas marqué : « **Par espèce, sur la course** » (§ 3), avec l'aiguilleur à 16,52 et 73,66, les espèces 1 et 3 au prorata 1,2 et un pire de 570 USD. Par la seconde règle, il vaudrait encore. D2 dit lequel prime ; D3 le marque et donne les chiffres à cinq espèces de la sortie du calcul v6. Le statut récrit garde « À six espèces, rien ne court avant ton mot sur ce devis » au présent (D1). Le bloc « à lire avant tout le reste » tait Rigaud et le deuxième relais, que le § 10.6 dit (D5).
- **§ 10** : chiffres justes (§ 3) ; 10.2 (six espèces pour mémoire : 87,01 et 180,88 par génération) juste ; 10.4 (34,79 contre 154,79 ; 34,96 de solde relu minimal) juste ; 10.6 juste, mais il renvoie l'arrêt du troisième relais à « additif 1 », qui ne le porte pas (D4).
- **Retraits** : huit au champ du calcul ; le § 10.1 en fait sept puces (repères de tarif et confrontation de la clé réunis) : contenu égal, sans suite. Les compositions à trois et à deux espèces restent écrites aux § 2 à § 9, histoire non retenue : juste.
- **Écart 2 — ce que la lettre dit, sans trancher.** GO-2026-11-20-08 est un accord de calcul par anticipation de 450 USD, « la ligne pleine », arrêt net au plafond, rapproché du devis v2 (plafond total 456 USD), échéance au 30 novembre ; sa condition « recharge … sinon, repli sur deux espèces » est remplacée par GO-2026-11-20-16 (v9, ligne 237). La v9, ligne 171, le dit cité « pour 450 USD, à cinq espèces » : à cinq espèces, son montant est exactement la ligne du devis v7. Mais GO-2026-11-20-33 (« Rien ne court avant le mot de Lazar sur le devis neuf ») est devenu règle du texte scellé (lignes 7 et 412 : « Sans ce mot, rien ne court ») ; GO-2026-11-20-60 ordonne l'additif, le devis neuf, le recalcul, la contre-lecture et le scellement par la mère, et ne dit rien de ce mot ni de GO-2026-11-20-08. À la lettre, donc : le montant est couvert par GO-2026-11-20-08 ; la règle du mot sur le devis neuf n'est levée par aucun accord. Que GO-2026-11-20-60 en tienne lieu est une lecture, à la mère. L'allumage reste à part (ligne 403). A6 et D1 écrivent cela sans trancher.
- **Écart 3 — recharge du troisième relais.** La restriction est dite à l'additif, § 7 ; l'écart (recharge, part au reste relu, arrêt n° 12 étendu) est laissé au complément, sur la précision de la mère de 13:30Z. À la lettre, la v9 (ligne 260) fait du complément le porteur de valeurs ; l'extension d'un arrêt est une règle. La mère l'a voulu ainsi ; je n'y touche pas, et je fais seulement dire aux deux textes où l'extension se trouve (A7, D4). Rien n'est exposé entre-temps : sans complément scellé, la part au pire de 199,65 USD dépasse le reste, et l'arrêt n° 11 refuse le départ.
- **Écart 5 — chemin de versement.** Précédent : le devis v6 est sur `main` à deux chemins (`prereg/ideation-nouvelles-attaques-v1/` et `NA/preenregistrement-court-v7/`), même empreinte ; le calcul v5 et sa sortie, au second. À la mère de l'écrire à la table au scellement.
- **Écart 6 — N-054** : présente sur `main` au même chemin, même empreinte, compagnon « OK ». Levé. La citation de la condition (b) est corrigée (A8).

## 7. Aucune recette

Programme `releve_aucune_recette_v1.py`, sortie `sortie-releve-aucune-recette-v1.json` : sur l'additif et sur les passages neufs du devis v7 (bloc « Ce que la v7 change » et § 10), aucune valeur de la légende des axes (6, 5 et 4 valeurs, tirées du source du calcul v6 sans l'exécuter et jamais écrites), aucune ligne de case, aucun emplacement, aucun bloc de code, aucune étape numérotée, aucun mot de consigne, aucun identifiant de modèle. Les 26 occurrences du mot « mode » dans l'additif sont toutes « mode tenu à l'écart », « mode de sabotage » (terme de N-054), « mode vu » ou des mentions génériques ; dans le devis, une seule, le nom du collisionneur. Deux noms de maison figurent dans la citation de GO-2026-11-20-60 (écart 1 du rapport) : ce ne sont pas des identifiants de modèle. **Conforme.**

## 8. Corrections

Le texte exact fait foi dans les deux jeux JSON (format de l'outil) ; chaque ancre est comptée une fois par `grep -c -F -e` sur la pièce, et les deux jeux passent l'outil sur une copie (15 et 5 remplacements, sorties `728102d4…` et `5c73949c…`, essais seulement).

**Sur l'additif** (`corrections-additif-1-v1.json`) :

A1 — § 6, ligne de la table « un par un ». Motif : la table finit ligne 294.

    Ancien : | 276 à 293 (table « un par un ») |
    Neuf : | 276 à 294 (table « un par un ») |

A2 — § 6, deux lieux manquants, insérés avant la ligne 133.

    Ancien : | 133 (« Prédiction ») |
    Neuf : | 101 (« Réponse vide motivée ») | « le volume attendu de fiches (de l'ordre de 338) peut baisser » | de l'ordre de 282 fiches |
    | 127 (« Lecture de l'ordre de course ») | « la composition à six espèces » parmi ce sur quoi l'erratum ne dit rien | la composition est à cinq espèces, celle que l'ordre suppose (course v9) : sur ce point, les deux textes ne diffèrent plus ; le point (e) vaut pour le reste |
    | 133 (« Prédiction ») |

A3 — § 6, lieu manquant, arrêt n° 16.

    Ancien : | 402 (« Ce qui reste », point 1) |
    Neuf : | 387 (arrêt n° 16) | la garde vaut « pour les deux sondes de refus » | elle vaut pour la sonde de refus des espèces 1 à 5 ; le reste de l'arrêt ne change pas |
    | 402 (« Ce qui reste », point 1) |

A4 — § 6, « Ce que le retrait ne change pas ».

    Ancien : les arrêts n° 1, n° 3 à n° 5, n° 8 à n° 10 et n° 14 à n° 23
    Neuf : les arrêts n° 1, n° 3 à n° 5, n° 8 à n° 10, n° 14, n° 15 et n° 17 à n° 23 (le n° 16 ne change que par le compte des sondes, ligne 387)

A5 — § 6, lignes 45 et 67 ; ajoute 47, le plafond de la clause (d) et le renvoi de « devis » seul (ligne 32).

    Ancien : | 45 et 67 (table des pièces ; clause (d)) | le devis en vigueur est le devis v6 | le devis en vigueur est le devis v7 ; les renvois au devis se lisent sur son § 10 |
    Neuf : | 45, 47 et 67 (table des pièces ; phrase sous la table ; clause (d)) | le devis en vigueur est le devis v6, « devis à six espèces » ; son plafond total est de 576,05 USD | le devis en vigueur est le devis v7, à cinq espèces, scellé par la mère avec cet additif ; son plafond total est de 456 USD ; « devis v3 », « devis v5 » et « devis v6 » renvoient à lui et se lisent d'abord sur son § 10 ; « devis » seul renvoie toujours au devis v2 (ligne 32) |

A6 — § 6, ligne 412 ; ajoute la ligne 7 ; dit la lettre sans trancher (écart 2).

    Ancien : | 412 (point 11) | mot de Lazar sur 570 et 576,05 USD, la sonde de l'espèce 6 et la part de sa clé | il se lit sur le devis v7 : 450 et 456 USD ; devis v7, § 10.8 |
    Neuf : | 412 (point 11) et 7 (statut) | mot de Lazar sur 570 et 576,05 USD, la sonde de l'espèce 6 et la part de sa clé ; « rien ne court avant le mot de Lazar sur le devis neuf » | le mot se donne sur le devis v7 : 450 et 456 USD ; que ce mot soit encore demandé, ou que GO-2026-11-20-08 en tienne lieu, la mère le dit (devis v7, § 10.8) ; d'ici là, « sans ce mot, rien ne court » vaut |

A7 — § 6, ligne 383 (arrêt n° 12), renvoi à l'écart 3.

    Ancien : | vaut pour les clés Minuit, Luc et Rigaud ; l'artefact de l'espèce 6 est retiré de l'épreuve, les trois autres cas restent |
    Neuf : | vaut pour les clés Minuit, Luc et Rigaud ; l'artefact de l'espèce 6 est retiré de l'épreuve, les trois autres cas restent ; son extension à la clé du troisième relais n'est pas écrite ici : elle se déclare au complément de valeurs (§ 7) |

A8 — § 2, condition (b) : lieu exact de la citation.

    Ancien : (N-054 : « sans aucune pièce des moniteurs »)
    Neuf : (N-054, ligne 60, sous « Ce que la décision ne fixe pas » : une instance « sans aucune pièce des moniteurs dans ses entrées » y est proposée, non fixée)

A9 — § 2, arrêt n° 24 : le mode déjà conçu (précision de règle, à accepter par la mère).

    Ancien : La carte ne nourrit pas le mode tenu à l'écart ; consigné, sans recopier la carte ;
    Neuf : La carte ne nourrit pas le mode tenu à l'écart ; un mode déjà conçu avec elle est déclaré « vu » ; consigné, sans recopier la carte ;

A10 — § 2, arrêt n° 26 : même précision.

    Ancien : Dans les deux premiers cas, la carte ne nourrit pas le mode tenu à l'écart |
    Neuf : Dans les deux premiers cas, la carte ne nourrit pas le mode tenu à l'écart, et un mode déjà conçu avec elle est déclaré « vu » |

A11 — § 4, silence 1.

    Ancien : Un tirage demanderait une clé de tirage neuve, que le texte scellé ne permet que par une pièce contre-lue.
    Neuf : Un tirage demanderait une clé de tirage neuve : le texte scellé n'en prévoit que pour l'identifiant neutre (ligne 254) et dit « Aucune autre méthode de tirage n'est permise » (ligne 311) ; ce serait un écart de plus, par une pièce contre-lue.

A12 — § 4, silence 3.

    Ancien : qui l'écrit, et à quelle date elle est arrêtée.
    Neuf : qui l'écrit, et à quelle date elle est arrêtée ; sans elle, l'épreuve de l'arrêt n° 25 ne peut pas être jouée.

A13 — § 4, silence 4.

    Ancien : Son inscription, pour cette seule carte, n'est pas écrite ici : l'additif ne change pas la liste nominative.
    Neuf : Son inscription, pour cette seule carte, n'est pas écrite ici : l'additif ne change pas la liste nominative. Tant que ce silence n'est pas tranché, la remise de la carte à cette instance tombe sous l'arrêt n° 18 (lecteur absent de la liste nominative) ou, hors de la quarantaine, sous l'arrêt n° 17 : la levée ne peut pas servir avant.

A14 — § 0, point 3.

    Ancien : 3. La recharge jusqu'au cas haut ne vaut plus que pour la clé du troisième relais.
    Neuf : 3. La recharge jusqu'au cas haut de GO-2026-11-20-55, point 2, ne vaut plus que pour la clé du troisième relais ; la recharge de Rigaud (GO-2026-11-20-34) n'est pas touchée.

A15 — § 5, « Aucun tirage ne change ».

    Ancien : Seul le nombre de lignes du registre servi et de fiches rendues baisse, ce qui ne change ni clé ni règle.
    Neuf : Seuls baissent le nombre de lignes du registre servi et celui des fiches rendues, c'est-à-dire les n que permutent les clés 12 et 13 et parmi lesquels tire la clé 20 : ni clé ni règle ne change, et ces n ne sont fixés d'avance à aucune composition.

**Sur le devis v7** (`corrections-devis-v7-v1.json`) :

D1 — statut.

    Ancien : À six espèces, **rien ne court avant ton mot sur ce devis** (GO-2026-11-20-33).
    Neuf : À six espèces, **rien ne courait avant ton mot sur ce devis** (GO-2026-11-20-33) ; à cinq espèces, ce que ton mot doit dire, et si GO-2026-11-20-08 en tient lieu, est au § 10.8.

D2 — phrase de version de la v7 : laquelle des deux règles de lecture prime.

    Ancien : **Ce qui vaut est au § 10**, neuf, et dans les passages à cinq espèces de la v2 qu'il nomme.
    Neuf : **Ce qui vaut est au § 10**, neuf, et dans les passages à cinq espèces de la v2 qu'il nomme ; là où un autre passage, marqué ou non, diffère du § 10 ou de la sortie du calcul v6, ceux-ci priment.

D3 — § 3, passage à six espèces non marqué.

    Ancien : **Par espèce, sur la course** (champ `par_espece_sur_la_course_usd` ; une espèce additionne ses rôles) :
    Neuf : **Par espèce, sur la course, à six espèces (v3) — ne vaut plus depuis la v7** (champ `par_espece_sur_la_course_usd` ; une espèce additionne ses rôles ; à cinq espèces, même champ de la sortie du calcul v6 : espèce 1, 19,74 et 51,84 ; espèce 3, 42,87 et 131,67 ; aiguilleur, 13,77 et 61,38 ; espèces 2, 4 et 5 inchangées ; pire de l'aiguilleur et d'un juge, 450 USD) :

D4 — § 10.6, renvoi de l'arrêt du troisième relais.

    Ancien : (préenregistrement court v9, additif 1 et complément de valeurs)
    Neuf : (préenregistrement court v9, arrêt n° 12, étendu à cette clé par le complément de valeurs ; l'additif 1 ne l'étend pas)

D5 — § 0, bloc « à lire avant tout le reste ».

    Ancien : une clé ne tient pas, même au cas bas : celle du troisième relais (manque 2,74 à 5,34 USD).
    Neuf : une clé ne tient pas, même au cas bas : celle du troisième relais (manque 2,74 à 5,34 USD) ; Rigaud ne tient que si ses deux lots en cours n'ont rien coûté ; le deuxième relais est indécidable.

Le calcul v6 et sa sortie : aucune correction.

## 9. Points pour la mère

1. **GO-2026-11-20-62** (13:44Z, R-4280) : « écart au garde-fou 6 de GO-2026-11-20-50 pour ce seul fournisseur, à écrire dans l'additif 1 de la v9 ». L'additif, écrit à 13:34Z sur `5f317ad8`, ne le porte pas. Il faut un texte neuf (lettre de l'accord, arrêt n° 23 et quarantaine touchés, réserve sur les fiches de la case retirée, silence 8), écrit puis vérifié, ou une décision de le porter ailleurs. Je ne l'écris pas : ce serait un texte de fond, non une correction.
2. **GO-2026-11-20-62, second volet** : « crédit suffisant selon Lazar pour le deuxième relais », alors que le devis v7 (§ 10.6, § 10.8) le dit indécidable ; et GO-2026-11-20-61, remplacé, portait un solde relevé et une recharge pour la clé de la course chez ce fournisseur. Ce qui en reste vaut-il au complément ?
3. **Écart 2** : la lettre est au § 6 ; à la mère de dire si GO-2026-11-20-60 tient lieu du mot sur le devis neuf.
4. **Écart 3** : une extension d'arrêt portée par le complément, que la v9 définit comme porteur de valeurs ; choix de la mère (13:30Z), à confirmer en connaissance de cause.
5. **Écart 5** : chemins de versement du devis v7, du calcul v6 et de sa sortie (précédent : deux chemins pour le devis v6).
6. **Silences 3 et 4** : bloquants (A12, A13) ; les autres sont à trancher ou à garder comme réserve (§ 4).
7. **Silences que je trouve en plus** : (i) la sonde des espèces 1 à 5 n'a jamais eu de règle écrite pour un refus pour crédit, une erreur d'accès ou une réponse illisible ; (ii) les comptes par case qui sortent de la quarantaine peuvent précéder le choix de la case retirée ; (iii) au troisième cas de l'arrêt n° 26, la suite pour le mode tenu à l'écart face à un moniteur conçu avec une fiche de la case retirée.
8. A9 et A10 ajoutent une suite (« déclaré « vu » ») aux arrêts n° 24 et n° 26, sur le modèle du n° 25 : à accepter ou à refuser.
9. Le complément de valeurs v1 est à récrire à cinq espèces (additif, § 7), et doit tenir compte de GO-2026-11-20-62. Le rapport du rédacteur garde « 276 à 293 » (pièce non scellée, sans suite).

## 10. Écarts du contre-lecteur

- C1. Calcul v6 rejoué avec le chemin de sortie en argument, non par `>` : le programme l'exige et écrit en mode exclusif. Un premier lancement sans argument est parti avant ma lecture du programme ; il a rendu son message d'usage, code 2, sans rien écrire.
- C2. Les empreintes des registres au commit `5f317ad8` sont vérifiées sur les premières lignes des registres de `origin/main`, non par `git show` sur ce commit.
- C3. Recherches bornées à un fichier nommé (registres extraits, ordre v3, N-054) ; `wc -l` sur des fichiers nommés pour borner les lectures.
- C4. Les essais des deux jeux par l'outil ont écrit, dans mon dossier, deux copies corrigées et leurs journaux ; ce sont des essais, non des pièces.

## 11. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`. Chacun a son compagnon `.sha256`.

- `contre-lecture-additif-1-v9-devis-v7-v1.md` (cette pièce)
- `corrections-additif-1-v1.json` ; `corrections-devis-v7-v1.json`
- `recalcul_independant_cinq_especes_v1.py` ; `sortie-recalcul-independant-cinq-especes-v1.json`
- `releve_aucune_recette_v1.py` ; `sortie-releve-aucune-recette-v1.json`

— contre-lecteur neuf, modèle O
