# Vérification du lot 3 (requête et journal) du véhicule NA-1 — v1

Vérificateur du lot 3 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices seules ; le gabarit servi réel n'est lu qu'en octets, avec une racine factice (le tirage réel n'est pas joué).

## Verdict

**Conforme. Les lots 4 et 5 peuvent partir.** Les comptes rejoués sont égaux aux comptes annoncés ; aucune exigence n'est manquante ; aucun des treize points « que la lettre ne fixe pas » n'est tranché à tort. Quelques gardes sans essai (liste au § 3) et six points à porter à l'additif ou aux mandats des lots 4 et 6 : rien ne bloque.

## 1. Empreintes et rejeu

| pièce | sha256 | état |
|---|---|---|
| mandat du lot 3 | `6a494f65…` | égal à l'annonce |
| table du livrable | `9fd8834ad0299406bb471f56193bed3593afbe1b857d2dc7e9a0e69d70022dbd` | égale ; les 14 fichiers vérifiés OK |
| rapport | `974bcc9a194e74d716cb3cf4266322f04d31f88e481b2d3382e1b38e9fb367a6` | égal |
| manifeste | `a021e6e980a4fa2e07d79685de788da99f650b19b4338f01fe8948fd1739010d` | égal |
| programme d'application | `6e4bbd1522c3191df1291fdf885be55819b2fc499f0d1e97093a95683ca36eda` | égal |
| orchestrateur | commit `a41b7b50…` | copie neuve, sans `.git` |

Copie neuve ; paquet v2 des lots 1 et 2 appliqué par son programme, puis paquet du lot 3 par le sien (`--lancer-essais`).

| | annoncé | rejoué |
|---|---|---|
| essais | 164 (92 + 72) | **164 passés** |
| mutations du développeur | 58 sur 58 tuées | **58 sur 58 tuées** ; témoin non muté passe ; témoin inerte survit |
| mes mutations (38) | — | 24 tuées, 14 survivent (§ 3) |

## 2. Exigences, une à une

Lieux : `requete_na_v1.py` (RQ), `journal_na_v1.py` (JN). Essais : `test_na_v1_requete.py`, `test_na_v1_journal.py`.

| exigence | faite | où | essai qui la tient (échoue sans la garde) |
|---|---|---|---|
| partie servie remplie à l'octet, dernier octet gardé, empreinte sur la pièce entière | oui | RQ `remplir_partie_servie` (l. 232-248) ; `Piece` (l. 121-134) ; `Element.piece_sha256` (l. 254) | `test_partie_servie_a_l_octet`, `TestDernierOctet` ; L3-12 ; **sonde réelle : 33 parties remplies égales à `avant + ligne + après`, dernier octet `\n` gardé** |
| gabarit : empreinte, un seul emplacement sur ligne propre ; question refusée par son nom (avant ouverture) et son empreinte | oui | RQ l. 150-193, 165-172 | `TestGabarit` ; L3-01 à L3-06 |
| enveloppe sans ajout (D2) | oui | RQ `SEPARATEUR` (l. 52), `assembler_proposeur` (l. 358-389), `assembler_sonde_refus` (l. 392) ; invariant de séparateur l. 306 | `TestEnveloppeSansAjout` ; L3-13, L3-14, L3-32 ; Y-34 et Y-37 tuées ; **sonde réelle : gén. 1, gén. 2 avec registre et sonde de refus exactes à l'octet** |
| registre vide : section omise ; gén. 1 sans registre | oui | RQ l. 371-387 | L3-15, L3-16 |
| arrêt n° 8 : cas sain (borne égale) et artefact (un octet de plus) | oui | RQ `verifier_borne` (l. 482-489) | `TestArret8Taille` ; L3-28 à L3-30 ; sonde réelle : levé à borne − 1, message sans contenu |
| encodage UTF-8 fait une seule fois ; le noyau reçoit la même suite | oui | RQ `_assembler_forme` (l. 427, un seul `.encode`) ; `chaine_pour_le_noyau` (l. 503) ; JN `EnvoiJournalise.chaine_pour_le_noyau` (l. 120) | `TestChaineDuNoyau`, `test_le_lot_4_rejoue_l_egalite_sur_les_octets_remis` ; sonde : chaîne ré-encodée = octets gardés = octets de la requête |
| ligne « envoi » écrite avant l'envoi, après la garde ; sans ligne, rien ne part | oui | JN `journaliser_envoi` (l. 235-262) | `test_ligne_envoi_apres_la_garde_avant_l_envoi`, `test_un_appel_sans_ligne_ne_part_pas` ; L3-43, L3-46, L3-47 |
| journal : ajout seul, refus de toute réécriture | oui | JN `_verifier_intact` (l. 187), `_ajouter` (l. 194, `O_APPEND`, rang, chaînage), `sceller` (l. 215), `verifier_journal` (l. 302) | `TestAjoutSeul` ; L3-36 à L3-42 ; **sonde : un octet changé, l'ajout suivant refusé (`JournalReecrit`)** |
| ligne « non envoyé » : numéro d'arrêt, clé, coût nul ; texte trouvé au seul journal | oui | JN `journaliser_non_envoye` (l. 264), l. 246-251 | `TestNonEnvoyeEtNonLance`, `test_refus_de_la_garde_…` ; L3-44, L3-45, L3-52 ; **sonde : texte absent de `str`, `repr` et `args`, présent au journal ; aucune ligne « envoi » pour la requête refusée** |
| ligne « non lancé » : renvoie à sa ligne « envoi », une seule fois, du même journal | oui | JN l. 273-285 | `test_non_lance_*` ; L3-50, L3-51 |
| refus écrits rendus par rôle (§ 2.13) | oui | JN `RENDUS_REFUS_ECRIT` (l. 53-67), `journaliser_refus_ecrit` (l. 287) | `TestRefusEcrit` ; L3-55 à L3-58 ; Y-12 à Y-16 tuées |
| forme de la fiche servie (portier, juge), égale au noyau octet pour octet, identifiant du juge en dernière clé et réencodé | oui | RQ `_assembler_forme` (l. 418), `assembler_juge` (l. 447) | `TestFormeFicheServie` (égalité avec `fiches_v54.entree_une_fiche`) ; L3-20 à L3-26 ; Y-31 et Y-32 tuées |
| aucun identifiant de modèle, aucune clé | oui | grep du livrable : aucun nom de modèle ni de clé ; « claude » n'apparaît que dans un chemin et dans « adaptateur Claude » | — |

Contrôle des refus écrits contre la table du § 2.13 : proposeur « rien, case non jouée, cases non jouées » ; portier « fiche » « au coffre, au coffre par refus du portier, fiche rendue » ; portier « réponse sans fiche » « réponse illisible, étiquette du portier illisible » ; juge « verdict absent, la fiche reste passée, verdicts absents ». Conforme à la lettre.

## 3. Gardes sans essai (mes 38 mutations, 14 survivantes)

Aucune ne touche une exigence du mandat. À renforcer au gré de la mère, non bloquant :

- **Y-08** (`fsync`) : équivalente, attendue.
- **Y-10** (taille du rejeu) : équivalente (l'empreinte implique la taille).
- **Y-22, Y-23** (forme canonique, ligne coupée à la relecture) : couvertes par le chaînage et l'analyse JSON ; équivalentes en pratique, comme le dit le rapport.
- **Y-09** (rejeu : sorte, génération, case non comparées), **Y-24** (événement inconnu à la relecture), **Y-19** (clé vide acceptée sur « non envoyé »), **Y-04** (compagnon existant non vu à la création), **Y-07** (écriture incomplète) : sans essai.
- **Y-11** (« non lancé » sans comparaison d'empreinte) : l'objet est figé, donc peu exploitable.
- **Y-27** (titre invalide accepté avec un registre vide), **Y-28** (sorte inconnue), **Y-29** (empreinte ou taille d'une requête forgée) et **Y-30** (empreinte ou taille d'une pièce forgée) : les contrôles d'intégrité des objets figés n'ont pas d'essai. Une requête forgée serait de toute façon refusée plus loin, par la comparaison de la garde dans `journaliser_envoi` (L3-47).

Un constat de plus (sonde) : si le fichier de journal est supprimé en cours de course, l'ajout suivant lève `FileNotFoundError`, qui n'est pas un `JournalRefuse`. Il refuse bien, mais un appelant qui n'attrape que `JournalRefuse` le manquerait. À dire au lot 4.

## 4. Les treize points « que la lettre ne fixe pas » (§ 5 du rapport)

Aucun n'est tranché à tort ; aucun ne contredit la conception v5. À l'additif du véhicule :

1. **Séparateur de l'enveloppe** (point 1) : « \n » après chaque pièce, donc une ligne vide seulement si la pièce finit par une fin de ligne. C'est vrai du gabarit réel (fini par `\n`) ; la synthèse réelle (`f74c6064…`) est à vérifier à son tour. À écrire.
2. **Titre de la section du registre et règle du registre vide** (point 2) : valeurs ouvertes de l'additif.
3. **Forme de la réponse sans fiche servie au portier** (point 3) : proposition du développeur (`## La réponse`, `{"reponse": …}`) : à fixer avec la consigne de D3.
4. **`rstrip` du noyau** (point 4) : la forme retire tous les blancs de fin de la consigne, pas seulement la fin de ligne : à dire à l'additif ; la composition journalise l'empreinte de la consigne entière.
5. **Ordre des clés de la fiche servie** (point 5) : donné par le lot 5.
6. **Numéro des arrêts neufs** (point 7), **liste fermée des champs d'une ligne « non envoyé »** (point 8), **un fichier de journal par génération** (point 9), **sceau exigé à la relecture** (point 10, le lot 7 doit passer `exiger_sceau=True`), **colonnes `fiche_rendue` et `appel_compte_m6`** (point 12) : valeurs du développeur à fixer.
7. Points 6, 11 et 13 : sans conséquence.

Deux ajouts de ma part, à porter aux mandats des lots 4 et 6 :

- **Égalité refusée après la ligne « envoi »** : `chaine_pour_le_noyau()` lève `EcartApresGarde` après que la ligne « envoi » est écrite (c'est l'ordre du § 2.3, pas 4 puis pas 5). L'erratum 1 du mandat du lot 4 demande alors une ligne « non envoyé ». La requête compte donc comme un envoi et comme un refus. À dire : l'arrêt qui porte ce refus (numéro ou nom, à l'additif) et si la ligne « non lancé » le couvre (la cause est un argument libre).
- **Pas de ligne « arrêt » générale ni de « ligne de la génération »** dans ce journal : `EVENEMENTS` est fermé à quatre événements. Le § 2.7 demande aussi des lignes d'arrêt et une ligne de la génération. Les lots 6 et 8 devront les écrire ailleurs, ou une v2 du journal les prendra. À choisir avant le lot 6.

## 5. Interface pour les lots 4 et 5

Comparée au § 5.1 de la v5 et à l'erratum 1 du mandat du lot 4 (`docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-4-v1-erratum-1.md`) :

- **`requete`** (§ 5.1 : gabarit, synthèse, ligne de case, registre servi, consignes fixes, enveloppe vers octets et composition) : `charger_gabarit`/`lire_gabarit`, `charger_piece`/`lire_piece`, `cases_du_tirage`, `assembler_proposeur`, `assembler_sonde_refus`, `assembler_portier_fiche`, `assembler_portier_reponse_sans_fiche`, `assembler_juge`, `mesurer`, `verifier_borne`, `tailles_par_sorte`. Complète.
- **`journal`** (§ 5.1 : ligne d'envoi, ligne de la génération, arrêt, vers fichiers d'ajout seul scellés par génération) : `JournalRequetes`, `journaliser_envoi`, `journaliser_non_envoye`, `journaliser_non_lance`, `journaliser_refus_ecrit`, `sceller`, `verifier_journal`, `verifier_rejeu`, `comptes`. Complète pour le mandat du lot 3 ; les lignes d'arrêt et de génération manquent (§ 4).
- **Erratum 1, point 1** : la requête est encodée une fois ; cette suite d'octets est celle que la garde lit, que le journal décrit et que `envoi.octets` rend ; `verifier_avant_envoi(envoi.requete_gardee, octets_remis)` est offert ; un écart se journalise par `journaliser_non_envoye`. Cohérent. À noter pour le lot 4 : la surcharge d'`appel` reçoit une chaîne ; elle appelle `envoi.chaine_pour_le_noyau()` et remet ce qu'il rend.
- **Erratum 1, point 2** : le texte trouvé ne va qu'au journal : tenu (sonde).
- **Erratum 1, point 3** : le lot 3 est écrit sur `garde_motifs_na_v2`. Une v3 du lot 2 est livrée ; sa compatibilité est vérifiée dans la pièce `verification-lot-2-na-v3-v1.md`.
- **Lot 5** : le portier et les juges produisent leurs requêtes par ces fonctions ; l'identifiant servi au juge s'encode par `identifiants_na_v1.encoder_identifiant_juge` ; le registre servi est une `Piece` lue à son empreinte.

## 6. Ce que je n'ai pas fait

Je n'ai pas relu à la source le texte système de l'adaptateur (hors lot). Je n'ai pas lu la synthèse servie réelle (je ne la signale que comme point d'additif). Je n'ai pas joué le tirage réel.

— vérificateur du lot 3 du véhicule NA-1, modèle S
