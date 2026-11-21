# Erratum 1 au mandat du développeur — véhicule NA-1, lot 10 a — versé v1

- Versé par la session du compte organisme (session fille de la mère), 2026-11-21, sur le point 2 du message de la mère `registres/essaim/vers-organisme/2026-11-21-1448-mere.md` (sur `origin/main`).
- Source : extraction scellée par la mère, `origin/main:docs/notes/organisme-noeuds-2026-11-21-v1/pieces-v1/erratum-1-mandat-developpeur-vehicule-na-lot-10-a-v1.md` (`e9dd96c15f5d41480c0c9bc002adb080ddf18ebf2395977e37390772f2859f79`, recalculée), elle-même extraite à l'octet de la réponse aux nœuds (`dd4e1ccc…`, § 2.3 et § 2.1).
- Seul geste fait sur le texte : après le point E7, la partie 1 de la consigne commune, lignes 12 à 26 de `origin/main:docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`), à l'octet, par `sed -n '12,26p'`, suivie de la phrase « Tu es développeur : … » du point E10 de l'erratum du lot 6, que E7 reprend. Le reste suit à l'octet, sans les commentaires d'extraction.
- Contrôle des chemins par `test -e` et `sha256sum`, 2026-11-21 vers 16:15Z : mêmes pièces que pour l'erratum du lot 6, toutes présentes, chacune à l'empreinte de la table.
- **Racine** : la table et les points E2, E3, E6 renvoient à `/home/user/controle-ia-travail-organisme/`, qui n'existe pas dans le conteneur de cette session ; le dépôt y est à `/home/user/controle-ia-travail/`. Le texte est gardé à l'octet ; le mandat de lancement du développeur dira la racine réelle en tête.

---

# Erratum 1 au mandat du développeur — véhicule NA-1, lot 10 a — v1

Pièce de travail (classe C), donnée par la session du compte organisme sur le mot de la mère du 21 novembre 2026. Elle complète le mandat docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-10-a-v1.md (9f9f20f9bc7fd9476d49445b5509cffee255158c2de23455ad57d46f8ae79795), qui reste intact. Où ils diffèrent, l'erratum prime.

E1. Chemins complets. Comme à l'erratum 1 du lot 6 : table jointe ; « Dossiers et empreintes donnés au départ » : les lignes des lots 3 v3, 4 v1 et 5 v1.

E2. Dossiers où une commande de liste est permise. Comme à l'erratum 1 du lot 6, point E2.

E3. Interdit de plus. Tu n'ouvres rien sous /home/user/controle-ia-travail-organisme/docs/notes/ideation-nouvelles-attaques-v1/additif-matiere-premiere-v1/, ni sur disque ni par git show. Ce que tu dois savoir de la lecture de fin tient dans les points E4 et E5.

E4. Où se lit l'empreinte de l'additif (décision de la mère sur l'épinglage). L'état « lecture de fin » est refusé si le manifeste de la lecture de fin n'existe pas, ou s'il ne porte pas l'empreinte de l'additif. Cette empreinte ne se lit jamais dans la configuration de la course, qui ne la porte pas. Tu écris contre un manifeste d'essai, déclaré comme tel. Épreuves : cas sain, manifeste présent avec l'empreinte attendue ; artefacts, manifeste absent, empreinte absente, empreinte fausse, empreinte posée dans la configuration de la course seulement : état refusé dans les quatre cas.

E5. Identifiant de ligne. La source des octets de l'identifiant de ligne n'est pas tranchée. Tu la reçois par une fonction donnée à ton module, tu n'en fixes aucune, et tu éprouves ton module avec deux fonctions d'essai différentes.

E6. Tenue aux redémarrages. Comme à l'erratum 1 du lot 6, point E9, vers /home/user/dossiers-developpeurs-vehicule-na-v1/lot-10-a/.

E7. Consigne commune de méthode. Comme à l'erratum 1 du lot 6, point E10, collée à l'octet.

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
