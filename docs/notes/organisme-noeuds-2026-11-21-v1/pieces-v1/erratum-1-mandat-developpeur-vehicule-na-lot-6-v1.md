# Erratum 1 au mandat du développeur du véhicule, lot 6 — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 2.2 (erratum 1 au mandat du lot 6) et § 2.1 (table commune des pièces, à coller dans les deux errata).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : Le crochet du point E10 est laissé tel quel : la consigne commune se colle à l'octet par la session du compte organisme, qui contrôle aussi chaque chemin par test -e (§ 2).

<!-- lignes 191 à 213 de la source : texte de l'erratum, à l'octet -->

# Erratum 1 au mandat du développeur — véhicule NA-1, lot 6 — v1

Pièce de travail (classe C), donnée par la session du compte organisme sur le mot de la mère du 21 novembre 2026. Elle complète le mandat docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-6-v1.md (b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d), qui reste intact. Où ils diffèrent, l'erratum prime.

E1. Chemins complets. Toute pièce que le mandat nomme par un chemin court se lit au chemin complet et à l'empreinte entière de la table jointe. « Dossiers et empreintes donnés au départ » : ce sont les lignes des lots 2 v5, 3 v3, 4 v1 et 5 v1 de cette table. La v9 et ses compléments se lisent sur origin/main aux chemins de la table.

E2. Dossiers où une commande de liste est permise. La ligne de tête « DOSSIERS DES LOTS 1 À 5 » se lit : ton dossier, et les quatre dossiers lot-2-vehicule-na-v5 (qui porte les lots 1 et 2), lot-3-vehicule-na-v3, lot-4-vehicule-na-v1 et lot-5-vehicule-na-v1, sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/. Aucun autre.

E3. Interdit de plus. Tu n'ouvres rien sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/, ni sur disque ni par git show.

E4. Règle du refus écrit (vérification du lot 4, § 6 ; vérification du lot 5, § 5). La fonction appeler que la génération donne au portier rend a["refus_ecrit"] dès qu'il est présent, avant toute lecture de a["r"] ou de a["lu"]. Épreuves : cas sain, un rôle non arrêté, le portier classe comme au lot 5 ; artefact, un rôle arrêté par une garde héritée, le portier rend « au coffre », cause « au coffre par refus du portier », ce compte vaut 1 et le compte « réponse du portier non lue » vaut 0 ; une mutation qui passe le dictionnaire du lot 4 tel quel doit faire échouer un essai. Tu ne modifies pas le lot 5.

E5. Lignes d'arrêt et ligne de la génération. Le journal du lot 3 v3 reste fermé à ses quatre événements. Tu écris les lignes d'arrêt et la ligne de la génération dans un fichier à part, le « journal des arrêts et des générations », en ajout seul, scellé à la clôture, jamais servi. Tu n'ajoutes aucun événement au journal du lot 3.

E6. Comptes. Tu fusionnes dans la ligne de la génération les comptes du mélange (lot 4, na_comptes), du portier (lot 5, portier.comptes()) et du journal (lot 3, comptes), sans renommer ni additionner deux sous-comptes distincts ; « au coffre par refus du portier » reste à part.

E7. Table marquée « artefact ». Une table de routage marquée « artefact » dans le contexte d'une génération refuse le départ ; cas sain et artefact (mutation Z4-25 de la vérification du lot 4, restée vivante).

E8. Transport et enveloppe. Tu ne fixes ni l'adaptateur, ni l'enveloppe, ni aucun texte ajouté à une requête : ils sont lus dans la configuration. Le faux fournisseur de ton module de simulation garde, pour chaque appel, la taille et l'empreinte du corps reçu, pour que l'égalité avec le journal puisse être éprouvée. Le contexte du lot 4 peut recevoir plus tard un champ de plus (lecture de l'état d'amont du relais) : n'en dépends pas, et ne l'interdis pas.

E9. Tenue aux redémarrages. À chaque jalon (module écrit, essais passés, rapport), tu copies ton dossier vers /home/user/dossiers-developpeurs-vehicule-na-v1/lot-6/, hors dépôt et hors de tout dossier temporaire. C'est la seule écriture permise hors de ton dossier.

E10. Consigne commune de méthode. [Coller ici, à l'octet et sans la reformuler, la partie 1 de docs/procedures/consigne-commune-methode-de-recherche-v1.md (d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8), de « Consigne commune de méthode (v1). » jusqu'à la fin de l'alinéa « Évaluateur et conseil. ».] Tu es développeur : les rubriques « Mode d'échec affecté » et « Dérivation de l'énoncé seul » portent « Sans objet : » et leur motif. La rubrique « Objets de contrôle » n'est jamais sans objet pour toi : chaque garde et chaque arrêt a son cas sain et son artefact, nommés, avec ce que tu attendais et ce qui est rendu.

<!-- lignes 161 à 186 de la source : table jointe, à l'octet -->

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
