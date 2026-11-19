# Rapport du rédacteur — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 5 du préenregistrement et du devis — v1

- Auteur : rédacteur neuf, modèle F. Je n'ai écrit aucune des versions 1 à 4.
- Heure (`date -u`) : 2026-11-19, de 16:32 à 16:38 (textes finis à 16:37). Processeur seul ; aucun appel de modèle, aucune dépense, aucun tirage, aucune écriture dans le dépôt, aucun commit. Réseau : un `git fetch origin main` seulement.
- Mandat : `mandat-redacteur-ligne-3-v5-v1.md`, `a5864b782ff9ac0079f06012e8b207d04f5c605479f198d6fbc63800e37053eb`, vérifié avant de commencer. Précision reçue en cours de travail de la session qui m'a lancé : les deux décisions de Lazar sont inscrites sur main en GO-2026-11-19-77 ; mot tapé à 16:18:19Z. Vérifié sur main avant de citer.
- Pièce de travail, classe C. Ce rapport ne peut pas porter sa propre empreinte.

## Fichiers rendus (bloc-notes seulement)

| fichier | empreinte sha256 |
|---|---|
| `preenregistrement-ligne-3-votes-effectifs-juges-v5.md` | `915fbe4b7ab17d83b9d39b92f21fd4cf4d52394d974b8b5b9c6e9e589d2fed12` |
| `devis-ligne-3-etage-payant-v5.md` | `43bcb1c887de4f8e683510ceac5871ff4c07464f6dfe396480937567b8761c4f` |
| `calcul_predictions_ligne_3_v2.py` | `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` |
| `calcul-predictions-ligne-3-v2.json` | `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724` |

À ne pas verser : `outils/appliquer.py` (remplacements exacts, chacun trouvé une fois et une seule, sinon rien n'est écrit) et `travail/` (les fichiers de remplacements et le second rejeu du calcul).

**Comment la version 5 est faite.** Par remplacements exacts sur la version 4 (`26bb2214…`) et sur le devis v4 (`0051297a…`), jamais par récriture : le différentiel fait 24 morceaux pour le préenregistrement (28 points à la table « Différentiel avec la version 4 ») et 8 pour le devis (11 points). Tout le reste est égal à l'octet.

**Le calcul neuf.** `calcul_predictions_ligne_3_v2.py` est le calcul de la version 1 sans changement, plus une partie : le lieu, sur l'axe δ, où la clause (i) du double rendu bascule, par loi du lecteur de surface. Joué deux fois (`python3 -I -B`), sorties égales à l'octet (`cmp`). Toutes les valeurs de la sortie de la version 1 y sont égales, clé par clé, sauf « version » ; une clé ajoutée. Résultat : suiveur séduisant, « réfuté » puis « tient » à δ = 0,385 ; lecteur séduit qui juge le fond sinon, à δ = 0,544 ; suiveur repoussant, jamais « tient ». Un seul changement de mot par loi sur la grille de δ (pas de 0,001). Ce sont les valeurs que le vérificateur donnait à la main (≈ 0,39 et ≈ 0,54).

**Le devis v5.** Aucun chiffre ni calcul ne change : le calcul du devis reste `calcul_devis_ligne_3_v3.py` (empreintes recalculées, non rejoué par moi). Une version 5 du devis était nécessaire pour trois raisons : la correction 7 demande le même ajout au § 5 ; il doit renvoyer au préenregistrement v5 ; il porte les deux décisions de Lazar au § 6 bis.

## Les neuf corrections

Toutes appliquées ; à la lettre partout où la vérification donne un texte exact (présence de chaque texte vérifiée par programme).

1. **Liste d'arrêt, garde « recouvrement ».** Cas sain remplacé par le texte donné. *Ajout de ma part, dans la même ligne* : trois artefacts de cloisonnement (fichier d'une autre empreinte ou d'un autre compte ; carte factice dont le champ `meta` porte seul un paragraphe d'un témoin ; rapport portant un champ hors de la liste), joués sur des cartes factices. Raison : règle R5, et la condition (4) de la mère demande un contrôle dans le code.
2. **Rejeu.** Étage 2, « Appels » : texte donné. « Seuil » : « ; un envoi revenu sans coût lisible n'est pas rejoué ». Annexe A : « rejeu unique d'un envoi refusé, coupé ou en erreur ». Le devis n'est pas touché sur ce point : son vérificateur le disait déjà juste.
3. **P5 quater et réserve 11.** Les deux textes donnés. Les deux bascules sont chiffrées dans une phrase de P5 quater qui renvoie au calcul neuf (0,385 ; 0,544).
4. **Bras « double rendu ».** Les deux phrases données, placées après la raison du sens (a).
5. **P10.** Prédiction de portée et sa réfutation, texte donné.
6. **Règle gelée de portée.** « aucun monde de cette famille … ne le porte », texte donné.
7. **Plafond, (i).** Texte donné ; même ajout au devis v5, § 5, condition (i).
8. **Plafond, (ii).** Phrase donnée, après « Reprendre la mesure demande un devis neuf et une ligne neuve. »
9. **Statut et « Contre-lecture ».** « par un agent du modèle O qui n'a écrit aucune version », à l'en-tête (auteur) et à « Contre-lecture ». La demande que la version 4 faisait à son vérificateur est gardée, marquée « pour mémoire ».

## Les quatre conditions de cloisonnement de la mère

Écrites à la section « Étage 2 », « Garde de recouvrement, avant scellement » ; rappelées à Q3 ; artefacts à la liste d'arrêt ; plan du code à l'annexe A.

- **(1) Entrée — traitée.** Le fichier des cartes est nommé (chemin, empreinte `ba65c411…`) avec ses 94 cartes, seule entrée du côté des cartes ; empreinte et compte vérifiés avant toute comparaison, refus de tourner sinon ; aucun autre fichier de l'archive.
- **(2) Lecture — traitée.** Par programme seulement ; champ `meta` retiré au chargement, avant tout usage ; les bardeaux des cartes ne vivent qu'en mémoire.
- **(3) Sortie — traitée.** Rapport à liste de champs fermée : comptes, empreintes, décision de la garde, identifiant du témoin refusé (ce dernier vient du texte de la correction 1). Jamais un contenu de carte, un bardeau, un extrait ni l'identifiant de la carte en cause.
- **(4) Contrôle — traitée, avec une lecture à confirmer.** Le code de la garde n'existe pas : il s'écrit après le scellement (ordre de la consigne R-3864). J'ai donc écrit que le contrôle « dans le code » se fait à la contre-lecture du code de la banque, par l'agent du modèle O, avant la première ouverture du fichier, et que sans lui la garde ne tourne pas ; le vérificateur de la version 5, lui, contrôle que les quatre conditions sont écrites au texte. Si la mère voulait dire autre chose, c'est une phrase à changer au (4).

Ajouts liés, de ma part : un repli écrit d'avance (les sept cartes nommées, écart au manifeste, si une condition ne peut pas être tenue) ; une phrase qui dit ce que le rédacteur des fragments sait d'un refus (l'identifiant du témoin et un compte, rien de la carte).

## Les deux décisions de Lazar

Citées sur la ligne **GO-2026-11-19-77** (main, commit `2ec5da6cd813e2912959289dd199eb5ce1a34139`, `registres/go.md` `5750c7fabeb66968e340f8dcc6aeec5ffe1a676a5415d7f726b3fb4b99fefe32`, relu ; mot « go reprise, go recos », 16:18:19Z). Les lignes GO-2026-11-19-55 à -74 y sont égales à l'octet à celles du commit relu pour la version 4.
- Décision 1, option (a) : Q4 du préenregistrement ; devis v5, § 6 bis.
- Décision 2, option (a) : « Lecture par colonne » du préenregistrement ; devis v5, § 6 bis. La question est écrite, et le texte dit que la porter dans la note de conception du juge revient à la mère.
- Les deux points ne sont plus des questions ouvertes : ce rapport ne les rend plus à Lazar.

## Ce que j'ai ajouté sans qu'on me le demande

- Les artefacts de cloisonnement à la ligne « recouvrement » (règle R5).
- Le repli si une condition de cloisonnement ne peut pas être tenue.
- La phrase sur ce que le rédacteur des fragments sait d'un refus.
- À « Contre-lecture », le rappel du § 10 de la vérification (information pour Lazar, portée par la mère).
- La liste des empreintes recalculées pour la version 5, et la mention « aucune carte affichée pour la version 5 ».
Tous sont nommés à « Contre-lecture », « Hors vérification, ajouté par le rédacteur en version 5 ».

## Ce que je n'ai pas pu faire, ce qui reste ouvert

- Le mot de la mère sur le cloisonnement (vers 15:39Z) n'est écrit nulle part ailleurs que dans le mandat : je le cite par le mandat. Le fichier des consignes de la mère sur la branche (`986e3a3c…`) ne le porte pas.
- La condition (4) : lecture à confirmer par la mère (ci-dessus).
- Je n'ai ouvert ni affiché aucune carte ; j'ai seulement recalculé l'empreinte du fichier des cartes. Les phrases de cartes citées viennent des versions 1 à 4.
- Empreintes : recalculées pour les pièces du dossier, les consignes de la mère, le fichier des cartes et `registres/go.md` aux deux commits de main. Les autres empreintes de l'en-tête sont reprises de la version 4 (recalculées par son vérificateur) ; celle du code de l'organisme reste non recalculée.
- Le calcul du devis n'est pas rejoué par moi (aucun chiffre ne change).
- Dans la sortie du calcul neuf, le suiveur repoussant porte une « bascule » à δ = 1 : c'est l'égalité de deux taux nuls, et le mot y passe à « sans prise », non à « tient ». Le texte le dit (« ne passe jamais à « tient » ») ; la clé du fichier peut tromper un lecteur pressé.
- Les fichiers compagnons `.sha256` ne sont pas écrits : la mère les pose au versement.
- La version 5 doit être vérifiée sur son différentiel par un agent du modèle O qui n'a écrit aucune version, avant scellement. Aucune carte n'est à lui donner.
- Aucun outil n'a refusé.

## À dire à Lazar (information, portée par la mère)

Repris de la vérification de la version 4, § 10 : si la prédiction ajoutée à P10 se vérifie, l'étage payant de 25 USD ne pourra rendre que « non » (un juge répété vaut le collège), « non concluant » ou des mesures ; jamais « oui ». Le pire cas reste « non concluant par manque de témoins », jamais lu comme un « non ».

## Décisions neuves pour Lazar

Aucune. Rien dans la version 5 ne change une hypothèse, une revendication, une dépense ni une décision prise.
