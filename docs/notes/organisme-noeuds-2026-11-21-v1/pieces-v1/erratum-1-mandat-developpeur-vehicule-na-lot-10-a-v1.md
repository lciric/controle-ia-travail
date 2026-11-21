# Erratum 1 au mandat du développeur du véhicule, lot 10 a — extraction v1

- Source : `docs/notes/organisme-noeuds-2026-11-21-v1/reponses-fable-noeuds-organisme-v1.md` (sha256 `dd4e1ccc53dbe142a4a64ae054114dd17feec20f07eb9d050d9de714ac3ed587`), sur main.
- Section : § 2.3 (erratum 1 au mandat du lot 10 a) et § 2.1 (table commune des pièces, à coller dans les deux errata).
- Retenu par la mère, décision de routine, R-4573.
- Extrait à l'octet par programme le 2026-11-21T14:48:35Z (`date -u`), sans aucun changement ; conçu par Claude Fable 5.2.
- Note d'extraction : Le point E7 renvoie au point E10 de l'erratum du lot 6 : la consigne commune se colle à l'octet par la session du compte organisme, qui contrôle aussi chaque chemin par test -e (§ 2).

<!-- lignes 219 à 235 de la source : texte de l'erratum, à l'octet -->

# Erratum 1 au mandat du développeur — véhicule NA-1, lot 10 a — v1

Pièce de travail (classe C), donnée par la session du compte organisme sur le mot de la mère du 21 novembre 2026. Elle complète le mandat docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-10-a-v1.md (9f9f20f9bc7fd9476d49445b5509cffee255158c2de23455ad57d46f8ae79795), qui reste intact. Où ils diffèrent, l'erratum prime.

E1. Chemins complets. Comme à l'erratum 1 du lot 6 : table jointe ; « Dossiers et empreintes donnés au départ » : les lignes des lots 3 v3, 4 v1 et 5 v1.

E2. Dossiers où une commande de liste est permise. Comme à l'erratum 1 du lot 6, point E2.

E3. Interdit de plus. Tu n'ouvres rien sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/, ni sur disque ni par git show. Ce que tu dois savoir de la lecture de fin tient dans les points E4 et E5.

E4. Où se lit l'empreinte de l'additif (décision de la mère sur l'épinglage). L'état « lecture de fin » est refusé si le manifeste de la lecture de fin n'existe pas, ou s'il ne porte pas l'empreinte de l'additif. Cette empreinte ne se lit jamais dans la configuration de la course, qui ne la porte pas. Tu écris contre un manifeste d'essai, déclaré comme tel. Épreuves : cas sain, manifeste présent avec l'empreinte attendue ; artefacts, manifeste absent, empreinte absente, empreinte fausse, empreinte posée dans la configuration de la course seulement : état refusé dans les quatre cas.

E5. Identifiant de ligne. La source des octets de l'identifiant de ligne n'est pas tranchée. Tu la reçois par une fonction donnée à ton module, tu n'en fixes aucune, et tu éprouves ton module avec deux fonctions d'essai différentes.

E6. Tenue aux redémarrages. Comme à l'erratum 1 du lot 6, point E9, vers /home/user/dossiers-developpeurs-vehicule-na-v1/lot-10-a/.

E7. Consigne commune de méthode. Comme à l'erratum 1 du lot 6, point E10, collée à l'octet.

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
