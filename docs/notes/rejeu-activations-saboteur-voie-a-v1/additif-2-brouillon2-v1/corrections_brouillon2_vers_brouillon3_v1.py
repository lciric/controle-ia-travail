"""Corrections du brouillon 2 vers le brouillon 3 de l'additif 2 aux sondes du barreau 8.

Rejouable : lit le brouillon 2 (empreinte exigée), applique les corrections de la
vérification des corrections (rapport 9f0d073a…), écrit le brouillon 3. Refuse d'écraser.
Chaque remplacement exige une occurrence, et une seule, de son ancre.
Usage : python corrections_brouillon2_vers_brouillon3_v1.py <brouillon2.md> <brouillon3.md>
"""
import hashlib
import sys
from pathlib import Path

EMPREINTE_B2 = "5b69a914a41d993654a6a148ae406db9b00f2682d3bcc2b67b7a71e8c43ae8ec"


def ligne(texte: str, debut: str, neuve: str) -> str:
    """Remplace la ligne, unique, qui commence par `debut`."""
    lignes = texte.split("\n")
    rangs = [i for i, l in enumerate(lignes) if l.startswith(debut)]
    assert len(rangs) == 1, (debut, len(rangs))
    lignes[rangs[0]] = neuve
    return "\n".join(lignes)


def morceau(texte: str, ancien: str, neuf: str) -> str:
    assert texte.count(ancien) == 1, (ancien[:60], texte.count(ancien))
    return texte.replace(ancien, neuf)


def apres(texte: str, debut: str, ajout: str) -> str:
    """Ajoute `ajout` (une ou plusieurs lignes) après la ligne, unique, qui commence par `debut`."""
    lignes = texte.split("\n")
    rangs = [i for i, l in enumerate(lignes) if l.startswith(debut)]
    assert len(rangs) == 1, (debut, len(rangs))
    lignes[rangs[0] + 1:rangs[0] + 1] = ajout.split("\n")
    return "\n".join(lignes)


def corriger(t: str) -> str:
    # --- en-tête -----------------------------------------------------------------------
    t = morceau(t, "— v1 — brouillon 2\n", "— v1 — brouillon 3\n")
    t = ligne(t, "**Statut : brouillon 2.",
              "**Statut : brouillon 3, candidat final. Il porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément (brouillon 2), puis les neuf défauts et la remarque de forme de la vérification des corrections du brouillon 2 (brouillon 3). Il est soumis à la même vérification, par le même vérificateur, puis au scellement par la session mère (clé `SCELLEMENT-ADDITIF-2-SONDES-IIB`).** Texte mécanique de format : aucun chiffre de résultat, aucun mécanisme du saboteur, aucun fragment de consigne privée, aucun texte d'épisode. Il se lit avec le texte scellé `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`), dit ici « le texte scellé », et avec son additif 1 scellé `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` (`fc5b0610ed004ea4b1565e7a50567d7538b0f9e66b129c874c2f8c5bc2a4d8c2`), dit ici « l'additif 1 ». Il ne réécrit ni l'un ni l'autre (règle R12). La version scellée portera le nom `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md`.")
    t = morceau(t, "  - *Brouillon 2* (ce texte) : écrit par Claude Fable 5.2,",
                "  - *Brouillon 2* (`5b69a914a41d993654a6a148ae406db9b00f2682d3bcc2b67b7a71e8c43ae8ec`) *et brouillon 3* (ce texte) : écrits par Claude Fable 5.2,")
    t = morceau(t, "(`date -u`).\n- **Pourquoi un additif 2",
                "(`date -u`) ; brouillon 3 écrit le même jour, heure relevée à la fin de l'écriture : 09:44Z.\n- **Pourquoi un additif 2")
    t = ligne(t, "- **Ce que le brouillon 2 ajoute après le mot de Lazar",
              "- **Ce que les brouillons 2 et 3 changent après le mot de Lazar (GO-2026-11-24-07), sur les constats de la contre-lecture.** Quatre points. Trois ajouts, qui ne peuvent qu'arrêter une passe ou une lecture, ou rendre sa lettre à l'additif 1 : (i) l'égalité des versions de jetonisation (M-1, constat 2) ; (ii) une table neuve des constantes reportées, écrite par programme (M-4, constat 3) ; (iii) le contrôle de la réponse à la question E-1 (M-3, constat 7). Et (iv) **des raisons corrigées** : la fiche de décision sur laquelle Lazar a dit son mot (`23605aba…`, point 5) disait les faits O-3, O-5 et O-6 « déjà gardés par le texte scellé et vérifiés sur le code de lancement » ; ce texte écrit qu'aucune garde ne tient O-3, que O-6 n'est qu'une raison non attestée (NL2-2), et que la clause (b) de la garde P3 ne compare plus deux enregistrements de la course (NL2-1, inconvénient). L'accord nomme la contre-lecture R2 et la vérification de ses corrections ; la session mère dit au champ AD2-1 si elle tient ces quatre points pour couverts par cet accord ou si elle les porte à Lazar. Recommandation du rédacteur : (i) à (iii) couverts, confiance 0,8 ; (iv) porté à Lazar en une ligne, puisque ce sont les raisons d'un nœud qui changent.")

    # --- table des corrections de la vérification, après celle de la contre-lecture R2 ---
    t = morceau(t, "## Ce que cet additif est, et n'est pas\n",
                "## Corrections de la vérification des corrections (brouillon 2 → brouillon 3)\n\n"
                "Rapport : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/verification-corrections-additif-2-brouillon2-opus-v1.md` (`9f0d073a1e86f1339bb1317a0c479f218668e05feef9f8f38cdada74f7312d9f`), conclusion « à corriger » : les seize points de la contre-lecture R2 portés ; trois défauts moyens, six mineurs, une remarque de forme. Tous corrigés, par le programme `corrections_brouillon2_vers_brouillon3_v1.py` du même dossier (rejouable). Aucun n'est refusé.\n\n"
                "| défaut | gravité | correction | où |\n|---|---|---|---|\n"
                "| 1 | moyen | point (iv) ajouté : raisons de NL2-2 et inconvénient de NL2-1 corrigés après le mot de Lazar ; renvoyé à la session mère par le champ AD2-1 | en-tête ; AD2-1 |\n"
                "| 2 | moyen | bornes (b1) à (b4) redites à la lettre de l'additif 1 ; écart à la lettre de (b1) et (b4) pour la chaîne de cet additif déclaré ; critère de l'attestation écrit ; compte de la fiche de décision déclaré ; question « Lazar avait-il vu une sortie » rétablie ; suite de « non faite » écrite | « Borne du scellement » ; AD2-3 ; « Expositions » ; ligne 30 (a) |\n"
                "| 3 | moyen | provenance du programme de comparaison de version 1 attestée au champ AD2-3 ; à défaut, la version nouvelle réécrit la pièce de comparaison sous un nom nouveau | M-4 ; AD2-3 |\n"
                "| 4 | mineur | phrase du champ `empreinte` récrite sans attribution infondée à la note version 7 | M-2 |\n"
                "| 5 | mineur | quatre lignes de plus dans la liste fermée des passages touchés | « Ce que cet additif est, et n'est pas » |\n"
                "| 6 | mineur | ligne 21 : « ni une règle M-1 à M-5 » ; bloc (9) : phrase des lectures dite sans effet sur le texte scellé | ligne 21 ; « Blocs changés » |\n"
                "| 7 | mineur | liste exacte de ce que demandent les clauses (a) à (d) | M-1 |\n"
                "| 8 | mineur | « les quatre pièces que la condition D-14 de l'additif 1 nomme, aux chemins de l'en-tête » ; la table neuve dite cinquième pièce | AD2-3 ; ligne 30 (a) ; ordre des opérations ; table des passages |\n"
                "| 9 | mineur | changements du programme dits sans contradiction | M-4 |\n"
                "| forme | — | « lettre du texte scellé, complétée » | M-1 |\n\n"
                "## Ce que cet additif est, et n'est pas\n")

    # --- défaut 2 : borne du scellement ------------------------------------------------
    t = ligne(t, "- **Borne du scellement.**",
              "- **Borne du scellement.** Comme l'additif 1, cet additif est scellé après la fin de la course lue (écart déclaré de l'additif 1, nœud NL-0, accordé). Sa borne propre est celle de la ligne 21 de l'additif 1 : avant toute passe. Les quatre bornes dures de l'additif 1 se redisent pour lui, à leur lettre : (b1) aucun agent du côté des moniteurs, ni aucun agent de la chaîne de rédaction et de contre-lecture de cet additif, n'a lu une sortie de la course lue ou de l'étalonnage, ni un état des lectures du dommage et de la diffusion ; (b2) l'extrait des seuls états n'est pas écrit ; (b3) la passe n'est pas partie ; (b4) aucune demande qui a fait écrire ou changer cet additif ne porte un contenu d'une sortie de la course lue ou de l'étalonnage, ni ne vient d'un agent qui en avait lu une. **Les bornes (b1) et (b4) ne sont pas tenues à leur lettre pour la chaîne de cet additif : c'est déclaré.** Le brouillon 1 est d'un agent du côté exposé, qui a relevé sur les fichiers de sortie de la course des métadonnées, dont des longueurs ; la note version 7 et la fiche de décision portent des comptes tirés de ces fichiers, que la chaîne a lus (section « Expositions déclarées pour l'additif 2 »). **Ce qui tient, d'après les déclarations de la chaîne** : aucun score, aucun texte d'épisode et aucun état des lectures n'a été lu par un agent du côté des moniteurs, ni par un rédacteur, un contre-lecteur ou un vérificateur de cet additif ; les règles M-1 à M-5 sont récrites par un rédacteur non exposé et ne dépendent d'aucune valeur tirée d'une sortie, hors de la forme du fichier des identifiants. Le rédacteur ne peut rien en vérifier. La session mère atteste au champ AD2-3 les bornes (b2) et (b3) ; elle y atteste (b1) et (b4) dans ce sens restreint ; et elle y dit sous quel accord l'écart à leur lettre est couvert, ou qu'elle le porte à Lazar. Recommandation du rédacteur : le porter à Lazar en une ligne, avec le champ AD2-1. Une borne (b2) ou (b3) non tenue, ou un score, un texte d'épisode ou un état lu : pas de scellement ; nœud de Lazar.")

    # --- défaut 5 : quatre passages de plus ----------------------------------------------
    t = apres(t, "| « Hypothèse », hypothèses de travail : « (2) Activité égale aux arrondis près : fait O-3 » | additif 1 |",
              "| « Activité interne », premier alinéa : « hypothèse de travail (2) ; fait O-3 » ; nœud NL-11, option (a) : « non au bit près (fait O-3) » | additif 1 | se lisent avec M-3 ; sans effet sur une règle | M-3 |\n"
              "| table de la fiche, ligne `conditions` : « toutes les conditions que portent les deux fichiers de l'évaluation » | additif 1 | se lit « que porte le fichier des identifiants » | M-1 |\n"
              "| RP-4, dernière phrase : « une sortie de la recette calculée avant cet additif ne vaut que si la table des constantes dit T, E, A et m égaux à ceux de la version 6 » | additif 1 | « la table des constantes » s'y lit « la table neuve de M-4 » | M-4 |")
    # --- défaut 8 : la ligne D-14 de la table des passages --------------------------------
    t = morceau(t, "| additif 1 | « la table des constantes reportées » s'y lit « la table neuve de M-4 » ; la table de l'additif 1 reste une pièce de constat | M-4 |",
                "| additif 1 | « la table des constantes reportées » s'y lit « la table neuve de M-4 » pour toute source, tout contrôle et toute pièce remise ; la condition D-14 garde les quatre pièces qu'elle nomme, la table de l'additif 1 y restant comme pièce de constat, et reçoit la table neuve en cinquième | M-4 |")

    # --- champs ouverts -------------------------------------------------------------------
    t = ligne(t, "| AD2-1 |",
              "| AD2-1 | accord de Lazar sur les nœuds NL2-1 et NL2-2 : identifiant de la ligne du registre des accords et mots de Lazar ; et le mot de la session mère sur les quatre points changés après cet accord (en-tête : trois ajouts, et les raisons corrigées de NL2-1 et NL2-2) : couverts, ou portés à Lazar, avec sa réponse | À REMPLIR |")
    t = ligne(t, "| AD2-3 |",
              "| AD2-3 | attestation de la session mère, dans la forme : « les quatre pièces que la condition D-14 de l'additif 1 nomme, versées aux chemins de l'en-tête à <heure>, empreintes égales, vérifié par programme ; relecture de cloisonnement de la note version 7 et de sa fiche avant ce versement : <pièce et empreinte ; ou « non faite », fait alors porté à Lazar avant le scellement, avec sa réponse> ; auteur et contre-lecture du programme de comparaison de version 1 : <développeur du côté des moniteurs et contre-lecteur d'un autre modèle, pièces et empreintes ; ou « non attesté »> ; bornes (b2) et (b3) de l'additif 1 tenues à l'heure de cette attestation : oui ; aucun score, aucun texte d'épisode, aucun état des lectures lu par un agent du côté des moniteurs ni par un agent de la chaîne de cet additif : oui ; source : <registre « qui a lu quoi », chemin et empreinte> ; écart à la lettre des bornes (b1) et (b4) (métadonnées relevées par le rédacteur du brouillon 1 ; comptes de la note version 7 et de la fiche de décision) : <couvert par l'accord nommé, ou porté à Lazar, avec sa réponse> ; Lazar avait-il vu une sortie avant ses mots : <oui ou non ; la fiche de décision porte un compte tiré des sorties> ; lectures du dommage et de la diffusion jouées avant le scellement de l'additif 2 : <oui ou non> ; attestation écrite à <heure, `date -u`> » | À REMPLIR |")

    # --- expositions ----------------------------------------------------------------------
    t = ligne(t, "- **Comptes portés par la note version 7 : fait déclaré",
              "- **Comptes tirés des sorties, portés par la note version 7 et par la fiche de décision : fait déclaré, porté à la session mère.** La note version 7 porte, à sa question (3) et à son point (d), des comptes d'identifiants et de jetons notés relevés sur le fichier des identifiants de la course lue, dont des comptes par condition. La version 6 ne portait que des tailles estimées. Quiconque lit la note version 7 les lit : le rédacteur des brouillons 2 et 3, le contre-lecteur R2, le vérificateur des corrections, puis les développeurs des deux codes et le contre-lecteur de leur conformité. La fiche de décision (`23605aba…`, point 1) porte, elle aussi, un compte d'ensemble tiré du même fichier ; l'ont lue le rédacteur des brouillons 2 et 3, le contre-lecteur R2, le vérificateur des corrections et Lazar. Aucune valeur n'en est recopiée ici, et aucune règle de cet additif n'en dépend. Le lecteur des sondes, le juge et l'auditeur ne reçoivent ni la note version 7 (additif 1, « Critères de lecture gelés ») ni la fiche de décision : ils ne les lisent pas. C'est l'écart à la lettre de la borne (b1) que nomme l'alinéa « Borne du scellement » : la session mère dit au champ AD2-3 sous quel accord il est couvert, ou le porte à Lazar (ligne 25 de l'additif 1). La longueur notée d'une action est l'un des prédicteurs triviaux du texte scellé (prédiction B8-P7) ; sa règle est scellée depuis le 19 novembre et n'est pas touchée.")

    # --- M-1 ------------------------------------------------------------------------------
    t = morceau(t, "aucune relance ni aucun autre décodage avant son mot (lettre du texte scellé, inchangée).\n",
                "aucune relance ni aucun autre décodage avant son mot (lettre du texte scellé, complétée : « ni aucun autre décodage » est ajouté, et ne fait que durcir).\n")
    t = ligne(t, "- **Les clauses (a) à (d) sont jouées en entier avant le chargement des poids**",
              "- **Les clauses (a) à (d) sont jouées en entier avant le chargement des poids** : elles ne demandent que le jetoniseur et le fichier `config.json` de la révision, l'extrait du côté exposé, la table neuve de M-4, le fichier des identifiants et le fichier des tâches.")

    # --- M-2 ------------------------------------------------------------------------------
    t = ligne(t, "- **Champ `empreinte` des lignes d'état.**",
              "- **Champ `empreinte` des lignes d'état.** D'après la note version 7 (question (5)), la course a relu la dose et l'empreinte à chaque condition. Ce champ n'est pas l'empreinte du fichier d'adaptateur : les valeurs de l'extrait diffèrent de celles des trois fichiers ci-dessus. Rien n'arrête : le texte scellé ne compare ce champ à rien (D-13).")

    # --- M-4 ------------------------------------------------------------------------------
    t = ligne(t, "- **Programme.**",
              "- **Programme.** Le programme de comparaison et de report passe en version nouvelle, sous un nom nouveau (règle R12). C'est un instrument : il est écrit par le développeur du côté des moniteurs à partir de l'additif 1 et de cet additif seuls, contre-lu par un autre modèle, et ses corrections sont vérifiées par le même contre-lecteur. Ses seuls changements sont cette liste fermée et les trois différences de la table neuve ; le chemin et l'empreinte de la table de l'additif 1 y sont des constantes. Il ne lit que la note version 6 (à son empreinte), la note version 7, la fiche et leurs compagnons. Il n'écrit que la table neuve ; la pièce de comparaison (`e744d824…`) n'est pas réécrite, hors du cas de l'alinéa suivant.\n"
              "- **Provenance de la version 1 du programme.** L'additif 1 veut que ce programme soit écrit par le développeur du côté des moniteurs et contre-lu par un autre modèle. La version 1 (`51ce5970…`) et ses deux pièces se trouvent dans le dossier des préalables du côté exposé ; le rédacteur ignore qui l'a écrite et qui l'a contre-lue. La session mère l'atteste au champ AD2-3. **Si elle y écrit « non attesté »** : la version nouvelle, écrite selon la règle, réécrit aussi la pièce de comparaison, sous un nom nouveau (`comparaison-interface-v6-v7-v2.json`, même dossier, avec son compagnon) ; cette pièce remplace `e744d824…` partout où l'additif 1 écrit « la pièce de comparaison » ; elle doit rendre les mêmes états de blocs (huit identiques, les quatorze changés de la table de cet additif, aucun ajouté, aucun absent) et les mêmes champs changés ; sinon : nœud (ligne 21).")

    # --- ordre des opérations (défaut 8) ---------------------------------------------------
    t = morceau(t, "« conforme » ; versement des quatre pièces de D-14 aux chemins cités ; attestation AD2-3 ;",
                "« conforme » ; versement, aux chemins de l'en-tête, des quatre pièces que la condition D-14 de l'additif 1 nomme ; attestation AD2-3 ;")

    # --- blocs changés (défaut 6) ----------------------------------------------------------
    t = ligne(t, "| (9) lectures du dommage et de la diffusion |",
              "| (9) lectures du dommage et de la diffusion | noms de fichiers retirés ; scellements exigés | RP-10 et M-5 pour le programme de l'extrait des états ; la phrase qui dit les lectures conduites après les scellements exigés : sans effet sur le texte scellé (engagement du côté exposé) ; vocabulaire et portée égaux d'après la fiche |")

    # --- liste d'arrêt ---------------------------------------------------------------------
    t = morceau(t, "porte une exigence que ne couvrent ni M-1, ni M-2, ni une règle de report de l'additif 1 | écart : nœud de Lazar ; rien avant son mot ; la suite s'écrit dans un additif 3",
                "porte une exigence que ne couvrent ni une règle M-1 à M-5, ni une règle de report de l'additif 1 ; ou, dans le cas « non attesté » de M-4, la pièce de comparaison réécrite rend d'autres états de blocs ou d'autres champs changés | écart : nœud de Lazar ; rien avant son mot ; la suite s'écrit dans un additif 3")
    t = morceau(t, "ou sans l'attestation AD2-3 (pièces de D-14 absentes de leurs chemins cités ou d'une autre empreinte ; une borne (b1), (b2) ou (b3) non tenue), ou sans sa ligne",
                "ou sans l'attestation AD2-3 (l'une des quatre pièces que la condition D-14 de l'additif 1 nomme absente de son chemin de l'en-tête ou d'une autre empreinte ; borne (b2) ou (b3) non tenue ; un score, un texte d'épisode ou un état des lectures lu par un agent du côté des moniteurs ou de la chaîne de cet additif ; écart à la lettre des bornes (b1) et (b4) ni couvert par un accord nommé ni porté à Lazar ; relecture de cloisonnement « non faite » non portée à Lazar), ou sans sa ligne")

    # --- contre-lecture --------------------------------------------------------------------
    t = morceau(t, "- **Contre-lecture 2 (finale : vérification des corrections, texte rempli)** : À REMPLIR",
                "- **Vérification des corrections du brouillon 2** — sous-agent neuf, modèle Claude Opus 5.5, du côté des moniteurs, non exposé au saboteur, lancé par le rédacteur du brouillon 2 ; il n'a rien écrit de cet additif ; faite le 2026-11-24 entre 09:29Z et 09:40Z. Brouillon vérifié : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon2.md`, empreinte `5b69a914a41d993654a6a148ae406db9b00f2682d3bcc2b67b7a71e8c43ae8ec`. Rapport : même dossier, `verification-corrections-additif-2-brouillon2-opus-v1.md`, empreinte `9f0d073a1e86f1339bb1317a0c479f218668e05feef9f8f38cdada74f7312d9f`. Conclusion : « à corriger » ; les seize points de la contre-lecture 1 portés ; trois défauts moyens, six mineurs, une remarque de forme. Traitement : table « Corrections de la vérification des corrections » en tête de ce texte.\n"
                "- **Contre-lecture 2 (finale : même vérification, par le même vérificateur, du brouillon 3, texte rempli)** : À REMPLIR")
    t = morceau(t, "(6) que le marqueur d'attente ne paraît qu'aux quatre lieux permis",
                "(6) que le marqueur d'attente ne paraît qu'aux quatre lieux permis (les trois cellules d'état et l'entrée « Contre-lecture 2 »)")
    return t


def main() -> int:
    source, cible = Path(sys.argv[1]), Path(sys.argv[2])
    brut = source.read_bytes()
    assert hashlib.sha256(brut).hexdigest() == EMPREINTE_B2, "le brouillon 2 n'a pas l'empreinte attendue"
    if cible.exists():
        raise SystemExit(f"refus : {cible} existe (règle R12)")
    cible.write_text(corriger(brut.decode("utf-8")), encoding="utf-8")
    print(hashlib.sha256(cible.read_bytes()).hexdigest(), cible)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
