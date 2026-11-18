# Contre-lecture de la lecture entière d'EvoSCM (arXiv 2609.01526 v2) contre O4 — v1

- **Contre-lecteur : modèle J** (J ≠ I ; je n'ai pas écrit la lecture ; autre modèle que son auteur).
- **Pièce contre-lue** : docs/notes/lecture-o4-suite-v1/lecture-entiere-evoscm-o4-v1.md (modèle I), ses deux listes et ses deux résultats de rejeu, et docs/sources/code/lecture-o4-v1/evoscm/provenance-v1.md. Aucun fichier de l'auteur n'est modifié (R12).
- **Heures (date -u, recopiées)** : début, empreinte du PDF et commit du clone 2026-11-18T02:10:49Z ; rejeu des deux listes de l'auteur et des 52 empreintes de fichiers 2026-11-18T02:11:09Z ; rejeu de mes propres listes 2026-11-18T02:15:59Z ; écriture de cette note 2026-11-18T02:17:39Z.
- **PDF** : docs/sources/pdf/lecture-o4-v2/arxiv-2609.01526/2609.01526.pdf, sha256 4094a67b0dddba479f4fd4d3a01ad03b05e4c93a255956516130f1153296cf98 (recalculé, conforme), 34 pages.
- **Code** : clone code-o4/EvoSCM, commit ffb638998da9537d738c20176ad928319889ff96 (git rev-parse HEAD, conforme ; arbre sans modification). Aucun programme du clone lancé.
- **Fichiers lus** : la note de l'auteur en entier ; lecture-o4-englobement-v3.md l. 19-77 et 181-199 ; lecture-pdf-priorite-haute-o4-v2.md (lignes sur EvoSCM, sections 2 à 5) ; provenance-v1.md ; les deux programmes de rejeu (pour leur règle de comparaison seulement) ; le PDF et le code (profondeur en section 1).
- **Règles** : R7, R8, R4, N-067. Je ne déclare rien « libre » ; le verdict en vigueur sur O4 reste **occupée en partie**. Tout écart est posé comme nœud (section 5).

## 0. Verdict

**Tient avec réserves.** Les rejeux sont conformes, les citations ne sont pas sorties de leur contexte, les absences déclarées sur le PDF (e-valeur, validité à tout instant d'arrêt, scellement) résistent à une recherche plus dure que celle de l'auteur. La ligne « conjonction non trouvée » tient à la profondeur lue. Mais trois énoncés de la note sont trop forts ou incomplets, tous dans le sens qui arrange notre revendication (R8, R4) :

1. « Règle d'acceptation d'une hypothèse contre la loi en vigueur ou familière, avec seuil : non trouvée » (section 5, point 3) et « Aucune proposition jugée contre ce qu'une archive de lois prédit déjà » (table, ligne P) : le code contient, à la finalisation, une comparaison par le programme de la loi du modèle de langue à une loi de famille connue ajustée par le programme, avec remplacement au rang et un seuil de 0,995 sur le rapport des pertes (constat 1).
2. « Ce n'est ni un rapport de vraisemblance cumulé ni une e-valeur » (section 4.2) : la première moitié est fausse à la lecture du code ; entre deux hypothèses, le rapport des poids est un rapport de vraisemblance gaussien cumulé, tempéré (constat 2).
3. « choix final par le modèle » (table, ligne iv-b) ne vaut que pour le banc de physique : sur le banc de gènes, le PDF décrit un choix final par le programme, sur une archive de candidats, par erreur hors échantillon (constat 3).

Aucun de ces points ne fait apparaître la conjonction ; chacun rapproche EvoSCM de P, de (iii) ou de (iv-b).

## 1. Ce que j'ai vérifié, et à quelle profondeur

- **Rejeux** : citations du PDF de l'auteur **46 sur 46** (contre-lecture-lecture-entiere-evoscm-o4-v1-rejeu-citations-pdf.json) ; extraits de code **42 sur 42**, code de sortie 0 (…-rejeu-extraits-code.json) ; programmes inchangés. Compagnons .sha256 des cinq fichiers de l'auteur : conformes. Les 52 empreintes de provenance-v1.md recalculées sur le clone : 52 conformes, 0 écart ; 52 fichiers suivis.
- **PDF** : lues en entier par moi les p. 1 à 8, 17, 18, 23, 26 à 32 ; p. 9 (début), 15, 19, 20, 22 lues par passages ; p. 10 à 14, 16, 21, 24, 25, 33, 34 non relues (bornées par la recherche de termes seulement). Recherche de termes refaite sur le texte entier **après recollage des mots coupés en fin de ligne** (ce que la recherche de l'auteur ne dit pas avoir fait).
- **Code** : lus ligne à ligne par moi, dans scm_pipeline.py, l. 526-675, 1440-1745, 1820-1926, 2101-2170, 2237-2263, 2781-2802, 2994-3552, 3553-3776, 3852-3868, 3940-4404 ; dans agent.py, l. 190-470, 589-1051, 1085-1274 ; transfer.py et scripts/run_transfer.py en entier ; release.py l. 60-187 ; scm_protocol.md l. 1-40, 95-110, 160-270. Le reste : recherche de termes sur tout le clone, essais compris, et liste des essais de tests/test_scm_pipeline.py. **Non lus ligne à ligne par moi** : evaluator.py, executor.py, worlds.py, mse_fitting.py, load_trajectories.py, PhysicsSchool/physchool/*, scm_pipeline.py l. 80-525, 676-1439, 1927-2100, 2170-2236, 2264-2780, 2803-2978, la suite de scm_protocol.md, le corps des essais.

## 2. Ce qui tient

- Empreintes, commit, licence, 52 fichiers : conformes.
- Absences sur le PDF, recherche refaite après recollage : e-value, e-process, anytime, martingale, stopping, likelihood, Bayes factor, hash, seal, preregist, timestamp, p-value, significan, Bonferroni, false discovery, nested, encompass, incremental : **zéro**, confirmé. « posterior odds » : une occurrence (p. 18). Absences sur le code (essais compris) : e-process, anytime, martingale, likelihood ratio, Bayes, Bonferroni, p-value, consensus, aggregat, mixture, ensemble : zéro, confirmé.
- Fonction d'empreinte définie et jamais appelée : confirmé (seule occurrence de son nom : sa définition, l. 38). Aucun horodatage par prédiction : confirmé (le seul usage d'une heure est l'identifiant de course).
- Ordre analyse, exécution, validation imposé par le programme ; prédictions copiées au choix du plan ; déduction enregistrée comme texte ; poids uniformes au premier tour seulement, puis logarithme de la confiance déclarée ; retrait à deux conditions (l. 3412-3423) ; capacité 8 dans le code contre 6 dans le PDF : confirmés sur le code.
- Statuts (i), (ii), (iv-a) et la ligne « conjonction non trouvée » : je ne trouve ni passage ni code qui les contredise, à la profondeur de la section 1.
- Les citations relues dans leur contexte (p. 1, 3, 5, 6, 8, 17, 18, 20, 23, 27 à 32 ; celles des p. 9, 10, 11, 21, 22, 24 ne sont vérifiées que par le rejeu) disent bien ce que la note leur fait dire.

## 3. Constats

### Constat 1 — majeur — une comparaison de la loi proposée à une loi connue ajustée par le programme existe, avec seuil ; la note la dit « non trouvée »

La note (section 5, point 3) répond « Non trouvée » à la question d'une règle d'acceptation contre la loi en vigueur ou familière, et sa table dit pour P : « Aucune proposition jugée contre ce qu'une archive de lois prédit déjà ». Elle ne mentionne la substitution de la loi finale qu'entre parenthèses, « non cité » (section 4.5).

Sur le code, à la finalisation (banc de physique) :

- quand la loi rendue par le modèle échoue au contrôle, le programme compile lui-même la loi d'une famille nommée de sa bibliothèque, agent.py l. 843-845 « compact_compiler = getattr( self.scm_pipeline, "deductive_compactified_law", None ) », la soumet au même contrôle, et **remplace la loi du modèle si celle du programme a un meilleur rang** : agent.py l. 897-901 « elif self._final_check_rank(deduced_check) > self._final_check_rank( best_check ): best_law = deduced_law best_check = deduced_check » ;
- pour les lois à modulation dans le temps, la loi de la bibliothèque remplace celle du modèle sous un **seuil chiffré sur le rapport des pertes** : agent.py l. 919-923 « select_alias = bool( not initial_causal_pass or not math.isfinite(initial_loss) or selected_loss <= 0.995 * initial_loss ) », puis l. 962 « best_law = selected_law » ; cela peut jouer même quand la loi du modèle passe le contrôle ;
- le contrôle lui-même devient plus dur quand la bibliothèque a « identifié » une famille : scm_pipeline.py l. 1892-1896 « mechanism_consistent = bool( not strongly_identified_mechanism or max_radius_median_error is None or max_radius_median_error <= 0.3 ) » ;
- l'invite pose un principe de comparaison au modèle emboîté plus simple : scm_protocol.md l. 182-185 « The runtime applies a soft minimum-description-length prior. An extra drag, screening, hidden class, or other mechanism should survive only when it predicts interventions better than the simpler nested model. » (lignes que la note cite comme « non citée » pour la seule pénalité de complexité).

Portée, sans la grossir : c'est une comparaison **en fin de course**, sur des données **déjà observées** (perte de rejeu, non prédictions engagées), contre **une** loi de famille connue ajustée (non une mise en commun), sans garantie d'erreur, et dans le sens « le connu remplace la proposition » ; ce n'est pas un nul formé de l'archive de l'organisme. Mais c'est bien une proposition de modèle de langue jugée par un programme contre une loi connue ajustée, avec un seuil.

**Correction proposée** : section 5, point 3 : remplacer « Non trouvée » par « trouvée sous une forme voisine, à la finalisation : rang de contrôle et seuil 0,995 sur la perte de rejeu contre une loi de famille connue ajustée par le programme (agent.py l. 843-845, 897-901, 919-923, 962 ; scm_pipeline.py l. 1892-1896) ». Table, ligne P : garder **voisin**, retirer la phrase « Aucune proposition jugée contre ce qu'une archive de lois prédit déjà » et écrire « aucune proposition jugée, sur prédictions engagées, contre une archive ; à la finalisation, la loi du modèle est comparée par le programme à une loi de famille connue ajustée, en échantillon ». Ligne (ii) : ajouter que la bibliothèque sert aussi de **loi de remplacement** (pas seulement de « correspondance »).

### Constat 2 — majeur — « ni un rapport de vraisemblance cumulé » est faux à la lecture du code ; (iii) est plus proche que la note ne le dit

La note (section 4.2, dernier paragraphe) écrit : « Ce n'est ni un rapport de vraisemblance cumulé ni une e-valeur […] une note de classement ».

Sur le code : chaque prédiction reçoit une log-vraisemblance gaussienne (l. 4030-4033, cités par l'auteur) ; l'évidence par cible est cette log-vraisemblance **moins celle du meilleur groupe**, scm_pipeline.py l. 4106-4112 « group_scores = { root: max( ( float(target_records[index]["log_likelihood"]) for index in indices ) ) » et l. 4115 « best = max(group_scores.values()) », c'est-à-dire un logarithme de rapport de vraisemblance contre la meilleure concurrente ; elle est ajoutée tour après tour aux log-poids (l. 4143-4145, cités par l'auteur). Pour deux hypothèses qui prédisent les mêmes cibles, le terme « meilleure » s'annule dans la différence : le rapport de leurs poids (les cotes a posteriori de la p. 18) est un **rapport de vraisemblance gaussien cumulé**, à un exposant près (température 0,7, division par la racine du nombre de cibles), entre deux lois prédictives **engagées avant l'observation** et **calculé par le programme**. La règle de retrait somme ces logarithmes de rapport sur les plans (l. 3414-3423) et les compare à -3,0.

Remarque mathématique de ma part, **hors pièce, non vérifiée sur une source, à faire vérifier** (R7 ne la rend pas opposable) : un rapport de vraisemblance élevé à un exposant compris entre 0 et 1 reste d'espérance au plus 1 sous le nul simple ; la température et la racine ne suffisent donc pas, à elles seules, à écarter la parenté avec une e-valeur. Ce qui l'écarte ici, sur pièce : aucune hypothèse n'est désignée comme nul ; la référence est la **meilleure** concurrente, choisie après l'observation ; l'incertitude de chaque loi est déclarée par le modèle ; les prédictions proches sont regroupées ; la log-vraisemblance est bornée ; la pénalité de complexité et la confiance déclarée entrent dans les poids ; aucun seuil n'est relié à un taux d'erreur ; ni le PDF ni le code ne revendiquent rien de tel (zéro occurrence des termes).

**Correction proposée** : section 4.2 : écrire « c'est un rapport de vraisemblance gaussien cumulé et tempéré entre lois prédictives engagées, relatif à la meilleure concurrente ; ce n'est pas présenté ni construit comme une e-valeur : pas de nul désigné, pas de seuil à garantie ». Table, ligne (iii) : **voisin (proche)** au lieu de voisin ; « e-processus non trouvé » maintenu. Le statut exact est un nœud (section 5, nœud A).

### Constat 3 — majeur — banc de gènes : choix final par le programme, sur une archive de candidats, par erreur hors échantillon ; la note ne le porte pas dans (iv-b) ni dans (ii), et n'a pas cherché le mot « archive »

La table de la note dit, ligne (iv-b) : « choix final par le modèle (transfer.py l. 84, 94-96) », sans borne de banc. Le PDF dit autre chose pour le banc de gènes : [p. 31] « The fixed working population size K = 5 is distinct from the candidate archive maintained by the final selector. », [p. 31] « The archive retains every valid unique graph produced during the four rounds », [p. 31] « After the fourth round, EvoSCM retains all valid unique graph candidates encountered during the session. » ; le classement est fait par validation croisée (citation de l'auteur, p. 32), avec [p. 32] « Ties are resolved first by preferring the graph with fewer edges » et [p. 32] « This selector uses neither the target graph nor evaluator metrics, and makes no additional LLM calls or simulator experiments. » ; l'étude de cas le confirme, [p. 20] « the conditional-Hill cross-validation procedure selects the complete signed ».

La note cite la p. 32 sous (iv-a) seulement (« un gel avant la note, pas une prédiction scellée »). Elle ne dit pas que c'est une **règle de promotion finale calculée hors du modèle de langue**, sur une **archive** des candidats de l'organisme, par une statistique d'erreur **hors échantillon**. Le mot « archive » (trois occurrences, p. 31) est absent de sa table de termes.

Portée : archive des candidats de la séance (non de lois connues), classement par erreur de validation croisée (ni e-processus ni nul), PDF seulement (code absent du clone).

**Correction proposée** : table, ligne (iv-b) : « pris pour la statistique (physique : postérieur ; gènes, PDF seulement : choix final par validation croisée, sans appel au modèle) ; choix final par le modèle sur le banc de physique seulement » ; ligne (ii) : ajouter « gènes : archive de tous les graphes valides de la séance, classée hors échantillon, sans rôle de nul (p. 31-32) » ; table de termes 2.1 : ajouter archive (3, p. 31), cross-validation (p. 19, 20, 32).

### Constat 4 — mineur — bibliothèque gelée de structures connues sur le banc de matériaux, non rapportée

[p. 30] « A frozen library of textbook structures » qui [p. 30] « supplies positive, negative, and boundary controls », dont les résultats [p. 30] « are not presented as novel discoveries ». Une bibliothèque gelée de connus sert de témoins d'étalonnage et le texte sépare le connu du nouveau. Ce n'est pas un nul à battre. La note lit la p. 30 « en entier » et ne le relève pas. **Correction** : l'ajouter à la ligne P ou (ii) comme voisin lointain, PDF seulement.

### Constat 5 — mineur — règles à seuil du code non rapportées

En plus du constat 1 : (a) refus par le programme d'une loi finale prématurée tant que des audits manquent, agent.py l. 240-249 « audit_blockers = self.scm_pipeline.finalization_blockers() if audit_blockers: self.scm_pipeline.final_claim = None » et l. 249 « round_entry["rejected_final_law"] = final_law.strip() » — la note dit seulement que les audits « retardent » la loi finale, et écrit ailleurs « Ce n'est pas un refus de la loi » (vrai du contrôle exécutable, pas de ce refus-ci) ; (b) seuil de perte de rejeu rapportée à la variance du bruit, agent.py l. 654-660 « relative_loss = float(loss_after) / max(noise_std**2, 1e-12) training_check = { "available": True, "passed": bool(relative_loss <= 1.25), » ; (c) en mode strict, qui est celui du lancement (release.py l. 101 « strict=True, »), le programme signale un plan sans prédictions d'au moins deux candidates, scm_pipeline.py l. 3070-3073 « if len(predicted_ids) < 2: errors.append( f"design {design['id']!r} must commit predictions from at least two candidate SCMs" ) », mais ne bloque pas : la sélection suit, l. 3141-3144 « if designs: selection = self._select_design( designs, max_episode_cost=max_episode_cost ) ». **Correction** : les ajouter à la section 4.5 ; aucun ne change un statut.

### Constat 6 — mineur — « engagement facultatif » : la preuve donnée est mince, la voie existe

La note s'appuie sur l. 4156 (un indicateur). La voie elle-même est dans l'invite, scm_protocol.md l. 259-262 « For compatibility, a normal `<run_experiment>` may instead be accompanied by `<prediction_commitment>[...]</prediction_commitment>`, using the same prediction schema. Such an action is recorded, but the runtime cannot compare several proposed designs before selecting it. », et dans l'agent, agent.py l. 433-435 « validation = self.scm_pipeline.observe_external_intervention( exp_input, results ) » : une expérience demandée directement est exécutée avec les prédictions jointes, s'il y en a. L'invite interdit la révision après coup (l. 22 « Never revise a prediction after seeing its result. ») ; c'est l'ordre du programme, non l'invite, qui la rend impossible. Le statut (iv-a) ne change pas. **Correction** : citer ces lignes.

### Constat 7 — mineur — la bibliothèque de lois nommées est dite « servie comme correspondance proposée à l'agent » : elle est aussi écrite par le programme dans l'explication notée

agent.py l. 1127-1135 « promote_correspondence = bool( correspondences and ( not support_status_known or selected_supported or quantitatively_supported or (not explicitly_weak_correspondence) ) ) », puis l. 1137-1140 « "Runtime-derived physical conclusion from the controlled data: " + correspondence_text » ; une branche rend une explication entièrement composée par le programme, l. 1243 « return ("Structured SCM conclusion. " + "\n".join(structured_parts)).strip() ». La clé qui devrait restreindre cette promotion n'est écrite nulle part dans le clone (recherche : deux occurrences, toutes deux en lecture, agent.py l. 1103-1104) : la promotion a donc lieu dès qu'une correspondance existe. Le PDF annonce lui-même que l'audit d'échelle sépare [p. 28] « a constant power law from Yukawa screening or a short-distance dimensional crossover ». Cela pèse sur le nœud 4 de l'auteur (validité des résultats d'EvoSCM, hors O4) : la conclusion tirée de la bibliothèque du programme entre dans l'explication que le juge note. Cela nuance aussi (i) pour le produit final (loi et explication peuvent venir du programme), sans changer le statut **pris**, qui porte sur les hypothèses candidates. **Correction** : compléter 4.5 et le nœud 4.

### Constat 8 — mineur — erreurs de détail

- Table 2.1 : « sequential : 2 occurrences (p. 11, 26) » ; il y en a trois, la troisième coupée en fin de ligne, [p. 3] « We formalize agentic scientific discovery as the sequential recovery of an unknown causal model through experimentation. » (sens courant, aucun test).
- Section 2.2 : hashlib « importée en deux endroits » ; elle l'est dans trois fichiers (context_window.py, agent.py, et scm_pipeline.py l. 3 « import hashlib »). La conclusion (fonction d'empreinte jamais appelée) tient.
- Section 4.5 : les familles de la bibliothèque sont plus nombreuses que les quatre citées (les correspondances de scm_pipeline.py l. 1551-1628 nomment aussi un champ de Poisson à deux dimensions, une famille de Riesz, une force à deux charges) ; et la loi d'écran compilée (deductive_screened_helmholtz_law) n'est appelée que par une liste, l. 2253-2261, elle-même sans appelant trouvé : seule la loi à somme d'images et les lois modulées sont effectivement substituées (agent.py l. 843-861). La note dit juste sur ce point ; je le confirme.
- Le PDF porte aussi [p. 18] « composition-related mechanisms are promoted » : vocabulaire de promotion sur le banc de matériaux, lié au seuil de fiabilité ; sans effet sur les statuts.
- transfer.py l. 124 « "candidate_archive": frozen_candidates, » : le mot archive existe dans le code (export des candidates pour le transfert) ; il n'y sert pas de nul (transfer.py et run_transfer.py lus en entier : compilation d'une loi par un autre modèle, sans comparaison).

### Constat 9 — mineur — profondeur déclarée

La note dit scm_pipeline.py lu « en entier » en tête de cellule, puis donne des plages : c'est une lecture par plages (environ la moitié du fichier ligne à ligne). L'en-tête (« lu en entier pour les fichiers qui réalisent […] ») se lit comme plus large qu'il n'est. L'écart à la consigne est déclaré en section 10 de la note, ce qui est correct ; la cellule devrait dire « par plages ». Les plages que j'ai lues et que l'auteur dit seulement parcourues (l. 1440-1480, 1560-1702) ne contiennent rien qui change un statut.

## 4. Effet sur la table de la lecture

| composante | statut de la note | ce que je propose | constat |
|---|---|---|---|
| P | voisin | voisin, maintenu ; phrase « aucune proposition jugée contre… » à corriger ; comparaison à une loi connue ajustée, en fin de course, avec seuil, à porter | 1, 4 |
| (i) | pris (physique) | maintenu | 7 (nuance) |
| (ii) | voisin (lointain) | maintenu ; ajouter loi de remplacement (physique) et archive classée hors échantillon (gènes, PDF) | 1, 3 |
| (iii) | voisin | **voisin (proche)** : rapport de vraisemblance cumulé tempéré entre lois engagées ; e-processus non trouvé, maintenu | 2 |
| (iv-a) | voisin | maintenu | 6 |
| (iv-b) | pris (statistique) ; voisin (promotion) | maintenu pour la physique ; borne de banc à ajouter : sur les gènes (PDF), le choix final est fait par le programme | 3 |
| conjonction | non trouvée | non trouvée, à la profondeur lue ; le verdict en vigueur **occupée en partie** n'est pas modifié | — |

## 5. Nœuds pour Lazar (décisions, pas des conclusions)

- **Nœud A — (iii) chez EvoSCM.** Les cotes a posteriori d'EvoSCM sont un rapport de vraisemblance cumulé et tempéré entre lois prédictives engagées avant l'observation, calculé par le programme, pour des hypothèses de modèle de langue ; non présenté comme e-processus, sans nul désigné ni garantie. Décision : le porter comme « voisin proche de (iii) » dans la note d'englobement et le citer, ou le laisser « voisin ». Option prudente (R4) : le porter et le citer. La remarque mathématique du constat 2 est à faire vérifier avant tout usage.
- **Nœud B — P et (ii) chez EvoSCM.** À la finalisation, la loi du modèle est comparée par le programme à une loi de famille connue ajustée (rang, seuil 0,995), en échantillon. Décision : l'ajouter à la ligne EvoSCM de la note d'englobement comme voisin de P et de (ii), ou non. Option prudente : l'ajouter.
- **Nœud C — banc de gènes.** Choix final par le programme sur une archive de candidats, hors échantillon, lu sur le PDF seulement. Décision : le citer comme voisin de (iv-b) au sens d'une règle de promotion, PDF seulement ; la question du code manquant rejoint le nœud 3 de l'auteur.
- Les nœuds 1 à 5 de l'auteur restent posés ; les nœuds A et B précisent ses nœuds 1 et 2, le constat 7 renforce son nœud 4.

## 6. Ce que je n'ai pas pu vérifier

- Les bancs de matériaux et de gènes sur le code : absents du clone (confirmé : aucun fichier de ces bancs parmi les 52).
- Les parties du clone non lues ligne à ligne (section 1) : une règle qui s'y trouverait m'échappe ; la recherche de termes n'y trouve rien.
- Les p. 10 à 14, 16, 21, 24, 25, 33, 34 du PDF : non relues, bornées par la recherche de termes ; p. 9, 15, 19, 20, 22 lues par passages seulement.
- Les tracés des figures ; la page du projet ; la version v1 d'arXiv.
- La remarque mathématique du constat 2 : raisonnement de ma part, sans source lue.
- Les comptes d'occurrences de la table 2.1 autres que ceux refaits ici (baseline, benchmark, pre-commit, posterior, threshold, spanning, marginal) : non recomptés.

## 7. Rejeux de mes propres citations

- PDF : **12 sur 12** (contre-lecture-lecture-entiere-evoscm-o4-v1-citations-pdf.json ; résultat …-resultat-citations-pdf.json), programme inchangé, premier essai.
- Code : **24 sur 24**, code de sortie 0 (…-extraits-code.json ; résultat …-resultat-extraits-code.json), programme inchangé, premier essai.
- Chaque passage du PDF ou du code mis entre guillemets dans cette note est dans l'une de mes deux listes ; les passages dits « cités par l'auteur » sont dans les siennes ; les autres guillemets reprennent des phrases de la note contre-lue.

## 8. Incidents et refus

- Aucun refus de permission, de crochet ou de classifieur.
- Les fichiers du clone nomment un modèle de langue commercial comme juge par défaut ; son nom n'est pas recopié.
- Aucun accès réseau, aucune dépense, aucun programme du clone lancé.
