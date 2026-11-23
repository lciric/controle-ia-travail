"""Monte le candidat au scellement 1 de la table de correspondance à partir du brouillon 3 :
les sections 1 à 8 sont recopiées à l'octet ; seuls le titre, l'en-tête, les sections 9 et 10 et la section
« Contre-lecture » sont réécrits. Emploi : python3 monter_table_candidat1.py BROUILLON3 CANDIDAT HEURE"""
import hashlib
import sys

src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()
L = t.split("\n")
i1 = L.index("## 1. Définitions et vocabulaire")
i9 = next(i for i, l in enumerate(L) if l.startswith("## 9. "))
bloc = "\n".join(L[i1:i9]) + "\n"
empreinte_bloc = hashlib.sha256(bloc.encode("utf-8")).hexdigest()

# lignes d'en-tête du brouillon 3 reprises mot pour mot
sources = [l for l in L[:i1] if l.startswith("- **Sources servies") or l.startswith("  ") and l.lstrip()[:2] in ("1.", "2.", "3.", "4.", "5.")]
assert len(sources) == 6, len(sources)
exposition = next(l for l in L[:i1] if l.startswith("- **Exposition de l'auteur**"))
suivi = next(l for l in L[:i1] if l.startswith("- **Suivi des corrections et contrôle formel**"))

entete = f"""# Table de correspondance — des issues du test « sabotage ou empreinte » sur les adaptateurs jumeaux aux trois classes de la conception des sondes (version 1, candidat au scellement 1)

- **Ce que c'est** : la table que demande la section 7 de la note de conception des sondes de la boîte blanche (`conception-sondes-v2-candidat1.md`, dans le même dossier). Elle range chaque issue du texte scellé du test « sabotage ou empreinte » sur les adaptateurs jumeaux (barreau 5) dans l'une des trois classes de cette section 7. Elle ne fait rien d'autre. **Candidate au scellement** : elle remplace le brouillon 3 (`9b0e2c1304ab914ef943c4e99693d1fd9b60e6d4e4b4bee6f392e02264d6bf42`, gardé), qui remplaçait le brouillon 2 (`ce24edde4c4eeca61f7fb191dd3e118f222d871269fc2aface40f5c647676562`, empreinte donnée par le brouillon 3 ; pièce absente du dépôt à la date de ce candidat, à y verser par la session mère) et le brouillon 1 (`66ed4874ec2b6968bbd3ac0059cbcbdb971dad7c02213e077559daa9a16d92c6`, gardé).
- **Ce qui change par rapport au brouillon 3, et rien d'autre** : le titre et cet en-tête ; la section 9, où les quatre points de jugement sont tranchés ; la section 10, qui dit l'état avant le scellement et déclare l'écart de calendrier ; la section « Contre-lecture ». **Les sections 1 à 8 sont celles du brouillon 3, à l'octet** : le bloc qui va de la ligne « ## 1. Définitions et vocabulaire » à la ligne qui précède « ## 9. » a pour empreinte `{empreinte_bloc}` dans les deux pièces. Aucune ligne de la table, aucune règle, aucun préclassement ne change.
- **Classe de la pièce** : décisive (critère de décision). Chaîne complète : contre-lecture par un autre modèle, vérification des corrections par le même contre-lecteur, puis scellement et inscription au registre par la session mère **avant** le scellement du verdict du test ; les deux horodatages du registre en font la preuve (section 7, condition 3).
- **Accords** : accord de reprise de conception des sondes (`GO-2026-11-22-126`, décision 2) ; accords de reprise sur un autre compte et de relance (`GO-2026-11-23-09`, `GO-2026-11-23-30`) ; accord de remplacement temporaire du concepteur par des sous-agents séparés pour l'auteur et le contre-lecteur (`GO-2026-11-23-33`, écart déclaré à la règle « Qui conçoit ») ; **mots de Lazar qui tranchent les quatre points de jugement selon les recommandations** (`GO-2026-11-23-36`) ; mandat de scellement donné par la session mère (ligne F9 de sa passation du 23 novembre 2026 à 22:20, ligne R-5205 du registre des décisions).
- **Auteurs** : sections 1 à 8, le sous-agent neuf **Concepteur des sondes de la boîte blanche** du brouillon 3 (Carbon en effort élevé, conversation `408edcf5d0ec826fe4a61c5b411328fe`) ; titre, en-tête, sections 9 et 10 et section « Contre-lecture », la session de conception `session_016QhUrvozGuPrL4eYUqDJvi`, servie par le modèle que la règle « Qui conçoit » réserve aux conceptions (attesté par l'attribution du commit de cette pièce), qui avait écrit le brouillon 1 et porte ici les décisions de Lazar sans rien changer à la correspondance.
- **Date et heure en temps universel coordonné** : 2026-11-23, {heure} (`date -u`).
"""
entete += "\n".join(sources) + "\n"
entete += """  6. Vérification finale du brouillon 3 par le même contre-lecteur indépendant : `verification-finale-table-brouillon3-et-conception-brouillon5-v1.md`, empreinte `7488baf06bca644ca82a6c723adb7825125a6c0d73c298dd6cd6fedb2cb36390` : « conforme, prêt à sceller après les mots de Lazar ».
  7. Faits de calendrier (section 10, point 5) : ligne R-5193 du registre des décisions (2026-11-23T21:08:47Z) et message de la session mère à la session de conception, reçu le 23 novembre 2026 à 23:26 ; ni l'un ni l'autre ne porte un résultat.
"""
entete += exposition.replace("- **Exposition de l'auteur** : l'auteur n'a ouvert", "- **Exposition de l'auteur des sections 1 à 8** (déclarée au brouillon 3) : l'auteur n'a ouvert") + "\n"
entete += """- **Exposition de la session qui porte ce candidat** : elle n'a ouvert ni le texte scellé du test, ni son code, ni ses sorties, ni aucun verdict, ni `registres/etat.md`. Du texte scellé, elle n'a lu que les trois pièces servies ci-dessus (sources 1 à 3), empreintes vérifiées avant lecture. Des registres, elle n'a lu que des lignes ou des débuts de lignes des registres des accords et des décisions (dont les lignes d'accord citées dans cet en-tête, R-5193 et R-5194), et la ligne F9 de la passation de la session mère ; sous `docs/verdicts/`, les seuls noms de fichiers. Aucun résultat du test lu.
"""
entete += suivi + "\n\n"

section9 = """## 9. Points de jugement, tranchés par Lazar avant le scellement

Les quatre points que le brouillon 3 soumettait à Lazar ont été tranchés le 23 novembre 2026 : mots de Lazar reçus de 21:47:22 à 21:48:06 en temps universel coordonné, inscrits sous `GO-2026-11-23-36` (« go a tout go recos de carbon high » : toutes les recommandations acceptées, dont ces quatre points ; la ligne du registre les dit « § 9 de la conception des sondes boîte blanche brouillon 5 » : ce sont les quatre points de la section 9 de cette table, que la note de conception cite à sa section 7, condition 5). **Chaque point est tranché selon la recommandation du brouillon 3.** Aucune ligne de la table ne change de ce fait : les sections 1 à 8 portaient déjà les choix recommandés. Les lectures écartées restent écrites ici, avec leur coût. Après le scellement de cette table, toute modification devient un nœud (section 7, condition 5 de la note de conception).

1. **Tranché : les issues « sabotage » et « contraire » au niveau de 95 % vont à « Non établi », dans les deux sens** (lignes 2 et 8).
   - *Lecture écartée pour l'issue « contraire »* : ranger une issue « contraire » à 95 % dans « Contraire, ou empreinte seule », par prudence ; son coût aurait été de cesser toute ligne décisive supervisée sur un adaptateur sur une preuve de niveau diagnostique (six ou sept familles).
   - *Lecture miroir écartée pour l'issue « sabotage »* : ranger une issue « sabotage » à 95 % dans « Au-delà de l'empreinte » ; son coût aurait été d'engager la poursuite vers la marche 2 et le critère 3 de la porte de fin de phase 0 sur une preuve de niveau diagnostique.
   - *Coût accepté du choix retenu* : pour l'issue « sabotage » à 95 %, il diffère la conduite « Au-delà » faute de puissance à 99 % ; pour l'issue « contraire » à 95 %, il laisse ouvertes les lignes décisives supervisées sur un adaptateur alors même que les preuves disponibles penchent contre la sonde.
   - *Motif* : symétrie entre les deux classes extrêmes (règle gelée `R4`) ; recommandation du brouillon 3, confiance 0,85.
2. **Tranché : l'issue « empreinte » sous huit familles va à « Non établi »** (ligne 5) ; la ligne 4 exige au moins huit familles dans l'épreuve principale.
   - *Lecture écartée* : la ranger à « Contraire, ou empreinte seule » (ligne 4) dès sept familles, voire dès six, puisque le texte scellé calcule pour cette issue une borne d'erreur de 2 puissance moins le nombre de familles (0,0078 à sept familles, 0,0156 à six) sans imposer en toutes lettres la borne de huit familles à l'issue « empreinte » ; son coût aurait été de fermer toutes les lignes supervisées sur adaptateur à six ou sept familles, alors que les autres issues décisives exigent au moins huit familles.
   - *Coût accepté du choix retenu* : une empreinte établie à sept familles (ou six) est rangée « Non établi », ce qui laisse ouvertes les lignes décisives supervisées sur un adaptateur malgré une séparation non transportée.
   - *Motif* : borne uniforme de huit familles ; le renvoi (b) du conducteur du barreau 5 dit que le texte scellé ne tranche pas ce point : il est tranché ici, par Lazar. Recommandation du brouillon 3, confiance 0,75.
3. **Tranché : l'issue « différence établie, non attribuée » va à « Non établi » pour tous ses motifs** (ligne 3).
   - *Lecture écartée* : la ranger « Au-delà de l'empreinte » quand seul manque le saboteur de la recette (motif « saboteur non établi ») ; son coût aurait été de faire d'une sonde qui ne sépare pas le saboteur de son jumeau une candidate au critère 3 de la porte de fin de phase 0.
   - *Coût accepté du choix retenu* : exclure de la marche 2 une sonde qui distingue les adaptateurs édités à poussée égale mais échoue sur la recette cible.
   - *Motif* : recommandation du brouillon 3, confiance 0,90.
4. **Tranché : le préclassement des quinze gardes de la section 2 est approuvé, et l'attente bornée est maintenue** (règle 4, lignes 9 à 11).
   - *Ce qui est approuvé* : (i) la manipulation non établie va toujours à la ligne 10 (a) et les gardes de la liste d'arrêt sont préclassées avant tout verdict, comme à la section 2 ; (ii) la ligne 11 (« rien n'est rangé ») est maintenue quand une panne hors liste survient avant sa déclaration au registre.
   - *Lecture écartée* : ranger « Non établi » d'office, sans ligne 11 ; son coût aurait été d'ouvrir trop tôt les données gardées alors qu'une relance technique légitime est due.
   - *Coût accepté du choix retenu* : la suite est bloquée le temps d'écrire la ligne du registre, en cas de panne technique hors liste ; l'attente est signalée à chaque passation (règle 8).
   - *Motif* : recommandation du brouillon 3, confiance 0,85.

"""

section10 = f"""## 10. État avant le scellement

1. **Attestation reçue et intégrée** : le conducteur du barreau 5 a rendu l'attestation sur l'extrait (`attestation-extrait-issues-b5f-v1.md`, `24122337…`) et l'extrait de la liste d'arrêt et des niveaux (`extrait-liste-d-arret-et-niveaux-b5f-v1.md`, `b14e35ac…`).
2. **Contrôle formel exécuté** : zéro recouvrement et zéro trou logique sur les 38 cas limites et les 172 combinaisons de `verification-formelle-table-correspondance-brouillon3-v1.py` (`092b9651cba86b6c87f494f0347e22a6bb8e4fcda6c071c0747fc922a1112571`). Le script vise les sections 1 à 3, inchangées ; la session qui porte ce candidat l'a rejoué le 23 novembre 2026 à {heure} : même bilan.
3. **Décision de Lazar sur les quatre points de jugement** : rendue (`GO-2026-11-23-36` ; section 9).
4. **Vérifications** : le brouillon 3 a été vérifié conforme par le même contre-lecteur indépendant (`7488baf0…`). Ce candidat reçoit une vérification finale par un contre-lecteur neuf, d'un autre modèle que ses auteurs (section « Contre-lecture »).
5. **Écart de calendrier, déclaré.** La condition 3 de la section 7 de la note de conception demande que la table soit scellée et inscrite avant le scellement du verdict : c'est ce que fait la session mère en scellant cette pièce, et les deux horodatages du registre l'attesteront. L'écart est de calendrier : les sorties du test existaient déjà quand la table a été corrigée, tranchée et scellée.
   - *Les faits* (ligne R-5193 du registre des décisions ; message de la session mère reçu le 23 novembre 2026 à 23:26) : la marche de relecture des familles jumelles du test a fini le 23 novembre 2026 à 10:12:09, au code 0, et ses sorties existent depuis ; elles ont été rapatriées sans lecture d'aucun score (attestation scellée citée par R-5193, 21:08:47) ; selon la session mère, qui tient les registres, elle n'a trace d'aucune ouverture de score par quiconque, aucun verdict du test n'est scellé ni inscrit au registre à la date de ce candidat, et aucun verdict n'existait quand Lazar a tranché les quatre points, le 23 novembre à 21:47.
   - *Ce qui est déclaré* : la table est scellée **après** la production des sorties de la relecture (10:12:09), mais **avant** toute ouverture d'un score et **avant** le verdict ; les deux horodatages du registre (scellement de la table, scellement du verdict) l'attesteront.
   - *Ce qui borne l'écart* : ni l'auteur des sections 1 à 8, ni la session qui porte ce candidat, ni les contre-lecteurs n'ont ouvert une sortie du test (expositions déclarées dans chaque pièce) ; la correspondance est celle du brouillon 3, versé sur la branche principale le 23 novembre 2026 à 21:13:56 (commit `9163ba4d`), dont les sections 1 à 8 sont reprises ici à l'octet ; les points de jugement ont été tranchés selon des recommandations écrites avant les mots de Lazar, sans qu'aucune ligne change.
   - *Ce que l'écart ne permet pas* : il ne couvre aucune ouverture de score antérieure au scellement de la table. Si une telle ouverture était constatée, la condition 3 ne serait plus tenue : nœud, porté à Lazar.
6. **Relecture par la session de conception** : `relecture-concepteur-avant-scellement-v1.md` (même dossier) : réserves non bloquantes, dont aucune ne change une ligne de la table.
7. **Scellement et inscription au registre par la session mère** avant le scellement du verdict du test sur les adaptateurs jumeaux, et report de l'empreinte scellée dans la note de conception (section 7).

"""

contre = """## Contre-lecture

- **Brouillon 1** (`66ed4874…`) : contre-lecture `contre-lecture-table-v1-opus-v1.md` (`2fe4c33b…`), verdict « à corriger », cinq constats majeurs et six mineurs, portés au brouillon 2.
- **Brouillon 2** (`ce24edde…`) : contre-lecture indépendante `contre-lecture-table-brouillon2-et-conception-brouillon4-v1.md` (`5956ea60…`), deux constats majeurs et quatre mineurs, portés au brouillon 3.
- **Brouillon 3** (`9b0e2c13…`) : vérification finale par le même contre-lecteur (`7488baf0…`), verdict « conforme, prêt à sceller après les mots de Lazar ». Sa remarque non bloquante sur le cumul fictif « phrase de manipulation et garde 13 » n'est pas portée : les deux lignes en cause (10 et 12) mènent à la même classe, « Non établi », le script compagnon range ce cas à la ligne 12, et les sections 1 à 8 restent ainsi celles de la pièce vérifiée.
- **Ce candidat** : vérification finale par un contre-lecteur neuf, d'un autre modèle que ses auteurs, dans un rapport à part qui cite l'empreinte de ce candidat ; elle porte sur l'identité à l'octet des sections 1 à 8, sur la fidélité des sections 9 et 10 aux mots de Lazar et aux faits du registre, et sur la cohérence avec la note de conception. La session mère ne scelle que sur un verdict conforme.
"""

open(dst, "w", encoding="utf-8").write(entete + bloc + section9 + section10 + contre)
print("bloc des sections 1 à 8 :", empreinte_bloc, "| lignes", i1 + 1, "à", i9)
