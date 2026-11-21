# Erratum 1 au mandat du développeur — véhicule NA-1, lot 6 — versé v2

- Versé par la session du compte organisme (session fille de la mère), 2026-11-21, sur le point 2 du message de la mère `registres/essaim/vers-organisme/2026-11-21-1448-mere.md` (sur `origin/main`).
- Source : extraction scellée par la mère, `origin/main:docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v2/erratum-1-mandat-developpeur-vehicule-na-lot-6-v2.md` (`322dac43…`, recalculée), retenue par la mère (message de 17:44Z), extraite à l'octet de la réponse aux nœuds v2 (`45212734…`, § 2.2 et § 2.1). Remplace la v1 versée (`erratum-1-mandat-developpeur-vehicule-na-lot-6-v1.md`, `1b08d873…`), qui reste intacte ; seul le point E8 change.
- Seul geste fait sur le texte : au point E10, le crochet est remplacé par la partie 1 de la consigne commune, lignes 12 à 26 de `origin/main:docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`), à l'octet, par `sed -n '12,26p'`. Le reste suit à l'octet, sans les commentaires d'extraction.
- Contrôle des chemins par `test -e` et `sha256sum`, 2026-11-21 vers 16:15Z : les dix-sept pièces sous `docs/notes/ideation-nouvelles-attaques-v1/` (mandat, conception v5 et son contrôle, relevé du lot 0, tables, rapports et vérifications des lots 2 v5, 3 v3, 4 v1, 5 v1) et les cinq pièces sur `origin/main` sont présentes, chacune à l'empreinte de la table ; le dossier de la base v68 porte 102 entrées sur `origin/main`.
- **Racine** : la table et les points E2, E3, E9 nomment `/home/user/controle-ia-travail-organisme/`, qui n'existe pas dans le conteneur de cette session ; le dépôt y est à `/home/user/controle-ia-travail/`. Le texte est gardé à l'octet ; le mandat de lancement du développeur dira la racine réelle en tête.

---

# Erratum 1 au mandat du développeur — véhicule NA-1, lot 6 — v1

Pièce de travail (classe C), donnée par la session du compte organisme sur le mot de la mère du 21 novembre 2026. Elle complète le mandat docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-6-v1.md (b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d), qui reste intact. Où ils diffèrent, l'erratum prime.

E1. Chemins complets. Toute pièce que le mandat nomme par un chemin court se lit au chemin complet et à l'empreinte entière de la table jointe. « Dossiers et empreintes donnés au départ » : ce sont les lignes des lots 2 v5, 3 v3, 4 v1 et 5 v1 de cette table. La v9 et ses compléments se lisent sur origin/main aux chemins de la table.

E2. Dossiers où une commande de liste est permise. La ligne de tête « DOSSIERS DES LOTS 1 À 5 » se lit : ton dossier, et les quatre dossiers lot-2-vehicule-na-v5 (qui porte les lots 1 et 2), lot-3-vehicule-na-v3, lot-4-vehicule-na-v1 et lot-5-vehicule-na-v1, sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/. Aucun autre.

E3. Interdit de plus. Tu n'ouvres rien sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/, ni sur disque ni par git show.

E4. Règle du refus écrit (vérification du lot 4, § 6 ; vérification du lot 5, § 5). La fonction appeler que la génération donne au portier rend a["refus_ecrit"] dès qu'il est présent, avant toute lecture de a["r"] ou de a["lu"]. Épreuves : cas sain, un rôle non arrêté, le portier classe comme au lot 5 ; artefact, un rôle arrêté par une garde héritée, le portier rend « au coffre », cause « au coffre par refus du portier », ce compte vaut 1 et le compte « réponse du portier non lue » vaut 0 ; une mutation qui passe le dictionnaire du lot 4 tel quel doit faire échouer un essai. Tu ne modifies pas le lot 5.

E5. Lignes d'arrêt et ligne de la génération. Le journal du lot 3 v3 reste fermé à ses quatre événements. Tu écris les lignes d'arrêt et la ligne de la génération dans un fichier à part, le « journal des arrêts et des générations », en ajout seul, scellé à la clôture, jamais servi. Tu n'ajoutes aucun événement au journal du lot 3.

E6. Comptes. Tu fusionnes dans la ligne de la génération les comptes du mélange (lot 4, na_comptes), du portier (lot 5, portier.comptes()) et du journal (lot 3, comptes), sans renommer ni additionner deux sous-comptes distincts ; « au coffre par refus du portier » reste à part.

E7. Table marquée « artefact ». Une table de routage marquée « artefact » dans le contexte d'une génération refuse le départ ; cas sain et artefact (mutation Z4-25 de la vérification du lot 4, restée vivante).

E8. Transport et enveloppe. Tu ne fixes ni l'adaptateur, ni l'enveloppe, ni aucun texte ajouté à une requête : ils sont lus dans la configuration. Le faux fournisseur de ton module de simulation garde, pour chaque appel, la taille et l'empreinte du corps reçu, et la taille et l'empreinte de la chaîne de contenu de chaque message de ce corps, pour que l'égalité avec le journal puisse être éprouvée. Le contexte du lot 4 peut recevoir plus tard un champ de plus (lecture de l'état d'amont du relais) : n'en dépends pas, et ne l'interdis pas.

E9. Tenue aux redémarrages. À chaque jalon (module écrit, essais passés, rapport), tu copies ton dossier vers /home/user/dossiers-developpeurs-vehicule-na-v1/lot-6/, hors dépôt et hors de tout dossier temporaire. C'est la seule écriture permise hors de ton dossier.

E10. Consigne commune de méthode. 

> **Consigne commune de méthode (v1).** Ta pièce rendue contient une section intitulée exactement « Relevé de méthode », avec les rubriques ci-dessous, dans cet ordre, sous ces intitulés exacts. Une rubrique qui ne s'applique pas porte « Sans objet : » suivi du motif en une phrase ; une rubrique vide ou absente rend la pièce irrecevable.
>
> **Chaîne de raisonnement.** Écris la chaîne, non la conclusion : des pas numérotés, chacun appuyé sur une pièce (chemin et empreinte), un calcul rejouable, un pas antérieur, ou marqué « supposé ». Une affirmation sans pas qui la porte n'est pas reçue.
>
> **Objets de contrôle.** Avant de croire un mécanisme (une sonde, un moniteur, un test de mort, un juge, un argument, une garantie), éprouve-le sur au moins un objet où ce qu'il doit établir est faux par construction, et sur un objet où c'est vrai par construction. Nomme les deux, dis d'avance ce que le mécanisme doit y rendre, puis ce qu'il y rend. Un mécanisme qui « réussit » là où la conclusion est fausse est mort, quel que soit son résultat ailleurs.
>
> **Premier pas non justifié.** Désigne, par son numéro dans ta chaîne, le premier pas que tu ne sais pas justifier entièrement, et dis ce qui le justifierait. « Aucun » n'est reçu que si chaque pas renvoie à une pièce ou à un calcul rejoué.
>
> **Mode d'échec affecté.** (Relecteur seulement.) Tu es hostile et aveugle : tu ne lis ni les autres relectures ni les échanges avec l'auteur. Tu réponds à une seule question, celle de ta ligne ; tu ne « vérifies » pas la pièce en général. Tu rends : tenu ou cassé, le pas visé, la preuve de ce que tu avances.
>
> **Dérivation de l'énoncé seul.** (Agent de re-dérivation seulement.) Tu ne reçois que l'énoncé. Tu le démontres, le recalcules ou le réfutes par ta propre voie, sans chercher la pièce d'origine. Tu rends ta chaîne et ton résultat ; la comparaison n'est pas ton travail.
>
> **Trouvaille de côté.** Si ce que tu cherches se révèle vide, faux ou déjà connu, dis-le en clair, avec ce qui le montre : c'est un résultat. Si tu vois en chemin autre chose que ta cible, note-le en trois lignes sans le poursuivre. Tu n'ouvres aucune course, aucune lecture de résultat et aucune dépense pour le suivre.
>
> **Évaluateur et conseil.** Dis ce qui juge ton produit (programme, épreuve, lecteur), sur quels témoins ce juge a été admis, et par où ton produit pourrait obtenir un bon jugement sans le mériter. Si tu conçois une course : le juge est écrit et admis avant la génération.

 Tu es développeur : les rubriques « Mode d'échec affecté » et « Dérivation de l'énoncé seul » portent « Sans objet : » et leur motif. La rubrique « Objets de contrôle » n'est jamais sans objet pour toi : chaque garde et chaque arrêt a son cas sain et son artefact, nommés, avec ce que tu attendais et ce qui est rendu.

Sous `/home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/` :

| pièce | chemin sous ce dossier | empreinte |
|---|---|---|
| conception v5 | `conception-vehicule-v5/conception-vehicule-course-nouvelles-attaques-v5.md` | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` |
| contrôle de la conception v5 | `conception-vehicule-v5/controle-v1/controle-conception-vehicule-na-v5-v1.md` | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` |
| relevé du lot 0 | `lot-0-vehicule-na-v1/releve-lot-0-vehicule-na-v1.md` | `10ac79ecb0e064f5b5ea80ddb060ae37e303d2d84ff242f653f4cccbd7ff753e` |
| lot 2 v5 (il porte les lots 1 et 2), table du dossier | `lot-2-vehicule-na-v5/table-empreintes-dossier-na-lot-2-v5.txt` | `6a5b5400aa9209f32f9cbd5a14116b5ddff929eac3886aec3753643c8282a2ce` |
| lot 2 v5, rapport ; vérification | `lot-2-vehicule-na-v5/rapport-developpeur-lot-2-na-v5.md` ; `lot-2-vehicule-na-v5/verification-v1/verification-lot-2-na-v5-v1.md` | `5454576f617aac139d8ef49c3f90a8a67f75e88b0a82e832fbe3578f3733340d` ; `e840bf334110858fa3c4f31e90aa33db0503307f0e03775478d9ae64b7670702` |
| lot 3 v3, table du dossier | `lot-3-vehicule-na-v3/table-empreintes-dossier-na-lot-3-v3.txt` | `1be0ffd48b8ade5f0accd106c9682c0b1e3db36bc208046ef66946598bbbed7f` |
| lot 3 v3, rapport ; vérification | `lot-3-vehicule-na-v3/rapport-developpeur-lot-3-na-v3.md` ; `lot-3-vehicule-na-v3/verification-v1/verification-lot-3-na-v3-v1.md` | `a778f8fa5d2ed290ecbafa91dff1da786d53bfc1d449b0f3df50c49349cc148e` ; `a1de709252ccc5596cc6d05fc93ef9830c78949b26a20f652516bf187badc83f` |
| lot 4 v1, table du dossier | `lot-4-vehicule-na-v1/table-empreintes-dossier-na-lot-4-v1.txt` | `747f782bed5c52304b8c7177b1c008c79f2c1554a72aa9069face7c78e3ee554` |
| lot 4 v1, rapport ; vérification | `lot-4-vehicule-na-v1/rapport-developpeur-lot-4-na-v1.md` ; `lot-4-vehicule-na-v1/verification-v1/verification-lot-4-na-v1.md` | `1b16fabb3f84b6d2a316b956a24b99a91f5897121bed5b8a98a769f580dff52f` ; `3c8d1aa2d67b45c2880f3185a6c9da06b1db772d4f869af6c66fd7d7b1ff6e68` |
| lot 5 v1, table du dossier | `lot-5-vehicule-na-v1/table-empreintes-dossier-na-lot-5-v1.txt` | `c7e7bd56aa80b5ab2b90d2a172d54cdab3c0943027999040f3fdaf7817865331` |
| lot 5 v1, rapport ; vérification | `lot-5-vehicule-na-v1/rapport-developpeur-lot-5-na-v1.md` ; `lot-5-vehicule-na-v1/verification-v1/verification-lot-5-na-v1.md` | `695bdcd9695472a431a9ab05d0913419da17b83a95be71be09af8aa4aaf5f741` ; `7742a6490a1492da2a15c7233a97cd8ba8534898c72662187b079d456500c87e` |

Sur `origin/main`, par `git show origin/main:<chemin> > <ton dossier>/<nom>` :

| pièce | chemin | empreinte |
|---|---|---|
| préenregistrement court v9, scellé | `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| complément de valeurs, lot 1, v3 | `prereg/ideation-nouvelles-attaques-v1/complement-valeurs-preenregistrement-court-v9-lot-1-v3.md` | `b4ef87dc6d5cce138f76457771c4cff18b84dfde662916841fc6386d77e202b2` |
| additif 1 à la v9, v5 | `prereg/ideation-nouvelles-attaques-v1/additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v5.md` | `9f731795cd8b9166ad8b78346e3d37c7352010ea0edd1f34ac86cfb0ac689200` |
| additif 1 au complément v3, v2 | `prereg/ideation-nouvelles-attaques-v1/additif-1-complement-valeurs-preenregistrement-court-v9-lot-1-v3-espece-3-sur-minuit-v2.md` | `ce76e0d6a0a6e65ffb99f68d9efced8d26e205ed0e2cf11c0e2469b69f672388` |
| base v68 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/` (un fichier par appel) | par le compagnon de chaque fichier |
| consigne commune de méthode | `docs/procedures/consigne-commune-methode-de-recherche-v1.md` | `d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8` |
