# Veille de cap — conception, additif 1 : la fusion avec la bibliothécaire, les deux sens, leur mesure (v1)

- **Nature** : pièce de travail (classe C), écrite le 22 novembre 2026 vers 15:25Z par la session de conception (`session_01XJ6MgqK7APqd1Hi98jL4GT`). Elle complète `conception-veille-de-cap-fable-v1.md` (`58ca3e28…`), qui reste telle quelle ; là où les deux diffèrent, l'additif prime. Le message de la mère qui porte la précision, daté de 14:59Z, ne m'est parvenu qu'après le rendu de la première pièce.
- **Lu en plus** : sur `main` à `7e2b9b30`, la demande 32 (`f5b44171…`) et la conception du rôle de la bibliothécaire (`docs/notes/demandes-fable-api-2026-11-22-v1/reponse-32/relecture-fable-api.md`, `a19d58fc…`, § C.2, C.3, C.5, D5), `registres/rappels.md` (`21e5b1a1…`), les lignes R-3170, R-4855 à R-4925 qui nomment la bibliothécaire ; sur `claude/bibliothecaire-v1` à `6e7c2d31`, son état (`2a6f4b64…`), le texte de son épreuve v3 (`6d2107f0…`), sa récolte v1 (`1e2255aa…`), le début de sa liste d'autorisation v3 (`6a9a41e3…`), les noms de ses fichiers.
- **Non lu** : aucun dossier « ne-pas-lire » (banque, réponses et verdicts de son épreuve) ; les chiffres de l'épreuve cités ici viennent de son état et de R-4877. Le mémo lui-même n'a pas été ouvert.

## La précision du directeur, verbatim

> au fond ça pourrait être la session dépôt, mais en y ajoutant ce mécanisme de bouclage récurrent qui s'assure de réinjecter dans le futur des éléments du passé ou du présent, et dans l'autre sens de récupérer dans le présent des éléments du passé, a fortiori lointain et pertinent.

La mère lit « la session dépôt » comme la session qui tient la mémoire du dépôt, aujourd'hui la bibliothécaire ; je suis cette lecture. Le nom a aussi désigné une session de relève horaire du canal, dont la tâche programmée a été désactivée le 18 novembre (R-3170).

## Verdict

1. Oui, un seul organe. Mais sa valeur n'est pas de mieux chercher : l'épreuve de la bibliothécaire dit que la recherche plein texte fait aussi bien que le mémo. Elle est dans ce qu'aucune recherche ne donne : **l'état, l'absence, le temps, l'initiative**.
2. Les deux sens deviennent deux objets : un **échéancier des retours** (vers le futur) et une **page du passé** remise au seuil de tout travail neuf (vers le présent).
3. Les deux se mesurent hors des modèles : dates et citations lues par programme, cas marqués par la mère, et un banc rétrospectif où git rejoue le dépôt tel qu'il était à une date passée.

## 1. Ce que l'épreuve de la bibliothécaire apprend à la veille

Essai 2 : 42 justes sur 45 avec le mémo, 45 sur 45 par la recherche plein texte seule ; paraphrases 13 sur 15, seuil de 14 manqué ; statut « non éprouvée » (état de la bibliothécaire ; R-4877). Le mémo v3 pèse 850 000 octets.

Conséquence. Retrouver une chose dont on connaît à peu près le nom, la recherche le fait. Quatre choses lui échappent, et c'est là que la boucle doit porter :

| Ce que la recherche ne donne pas | Exemple | Qui le donne |
|---|---|---|
| **L'état** : ce que l'idée est devenue | elle trouve le texte de l'idée, pas « essai non évaluable » | le journal des idées |
| **L'absence** : ce qui n'a pas eu lieu | la relance qui n'est jamais venue ; l'accord jamais consommé | le grand livre des promesses |
| **Le temps** : ce qui doit revenir à telle date | l'accord qui tombe le 30 ; « après G0 » | l'échéancier des retours |
| **L'initiative** : chercher quand personne ne demande | l'idée oubliée est celle sur laquelle nul ne pose de question | la boucle |

Donc : pas de second mémo. Le journal reste mince — nom, extrait, état, dates, pointeurs. Le contenu se lit dans les sources, par la recherche.

## 2. La fusion : gains, risques, forme

**Ce qu'on gagne.**
- **Un socle déjà fait.** La bibliothécaire a une recherche bornée par code à une liste d'autorisation, avec journal des fichiers ouverts, et un vérificateur de citations mot pour mot au commit épinglé (`epreuve-outils-v1/recherche_autorisee_v2.py`, `verifier_citations_v6.py`, sur sa branche), tous deux jugés conformes après contre-lecture selon sa récolte. Ce sont les contrôles que le mandat v2 demandait à la veille d'écrire. Le cloisonnement passe de la consigne à la garde.
- **Un seul interlocuteur**, pour toi comme pour la mère : « où est-ce ? » et « ceci attend » viennent du même endroit.
- **Chaque fonction nourrit l'autre.** Les questions posées à la bibliothécaire disent sur quoi l'on travaille : ce sont les indices du présent. Ses « non trouvé » signalent des trous. En retour, ses réponses portent l'état et l'échéance : « c'est là ; son essai n'a jamais jugé ; l'accord tombe le 30 ».
- **Une session et un mandat de moins** à relancer à chaque changement de compte.

**Ce qu'on risque.**

| Risque | Parade |
|---|---|
| **Deux périmètres dans une tête.** La liste de la bibliothécaire est celle du rôle le plus restreint ; la veille lit des traces de procédure qui n'y sont pas (dépenses, arrêts, manifestes de fin, noms de branches). Ce que la boucle lit peut fuir dans une réponse. | Un seul périmètre : la liste d'autorisation, étendue aux seules traces de procédure après relecture par la mère. Sinon la boucle tourne dans des agents à part, qui ne rendent que des codes, des dates et des chemins. |
| **La demande affame la boucle.** La bibliothécaire a déjà reçu des travaux hors mémoire (scripts d'appel à Google). | La boucle part à l'heure, dans un contexte neuf, avec son budget ; les critères de cadence le voient ; un travail hors mandat retourne à la mère. |
| **Un seul point de panne.** | Rien dans la mémoire de conversation : chaque question et chaque cycle relit les fichiers. La conception de la bibliothécaire le veut déjà. |
| **Un seul regard, non deux** : une fiche fausse passerait dans les réponses et dans les signaux. | Toute réponse et tout signal partent de la source ; l'extraction à l'aveugle, la clé de la mère et l'examinateur restent hors de l'organe. |
| **L'autorité** : qui répond et alerte à la fois sera cru. | « Index, non preuve » ; jamais cité dans une décision ; la mère confirme tout signal avant de le porter. |
| **« Aucun agent lancé »** est une règle de la conception de la bibliothécaire ; la boucle a besoin d'agents neufs. | Les agents de la boucle lisent par le même outil borné, comme ceux de son épreuve. |
| **Organe non éprouvé.** | La fusion ne repose pas sur le mémo ; la procédure fusionnée repasse l'épreuve, avec les questions des § 5 et 6. |

**La forme que je recommande : un organe, « la mémoire du dépôt », quatre gestes, tout l'état dans des fichiers.**

| Geste | Sens | Quand |
|---|---|---|
| **Répondre** | à la demande | une question de toi ou de la mère ; contexte neuf ; depuis les sources |
| **Rappeler** | du passé vers le présent | au seuil de tout travail neuf : la page du passé |
| **Renvoyer** | du présent vers le futur | l'échéancier ; les anniversaires à 7, 14, 30 et 60 jours |
| **Tenir** | — | le journal mince : états, promesses, faux échecs |

Une session, la bibliothécaire, est l'interlocutrice. Les cycles tournent à l'heure, dans des contextes neufs. Le mémo des 21 et 22 novembre reste une carte ; on ne l'étend pas.

**Le passage, sans rien arrêter.** Dès maintenant, les deux sessions partagent outils et périmètre : la veille emploie la recherche bornée et le vérificateur de citations ; la bibliothécaire lit le journal pour donner l'état. Le mandat unique vient à ton mot, au plus tard au prochain changement de compte, où tout se relance de toute façon.

## 3. Vers le futur : l'échéancier des retours

Ce qui existe : `registres/rappels.md`, lu par toute session à la reprise, pour les rappels qui te sont dus ; des tâches programmées ; les échéances des accords. Ce qui manque : la même chose pour les idées et les essais.

**Une ligne de l'échéancier** porte :
- **ce qui revient** : la fiche ;
- **quand** : une date ; ou un événement que la veille peut constater dans le dépôt (« le verdict est scellé », « l'accord a une dépense », « le chantier est clos ») **avec une date butoir** ; ou un contexte (des mots : « quand quelqu'un travaille là-dessus ») ;
- **pour qui** : la mère ; toi, par une ligne proposée pour `registres/rappels.md` ; un chantier, par la mère ;
- **la lettre au futur**, écrite le jour même, tant que le contexte est frais : ce que c'est, pourquoi cela comptait, ce qu'on comptait faire, ce qui le rendrait caduc ;
- **ce qui la clôt** : fait ; reprogrammé avec une condition neuve ; retiré par décision nommée.

**Trois règles.**
1. **Aucun réveil sur événement sans date butoir.** Un événement qui n'arrive jamais enterre l'idée une seconde fois.
2. **Rendu n'est pas traité.** Un retour n'est clos que par l'une des trois fins.
3. **Les dates vivent dans le fichier**, non dans les tâches programmées du compte. Au premier cycle après un changement de compte, tout ce qui est échu pendant le trou est rendu.

**Retours créés d'office** : toute fiche gardée de côté, à son réveil ; toute promesse, à son échéance ; tout accord de calcul dont aucune course n'a jugé, à dix puis sept jours de sa fin ; tout « plus tard », « après G0 », « au retour du quota » des registres ; tout préenregistrement scellé sans verdict, à quatorze jours.

Les anniversaires du mandat v2 sont ce même sens, à l'aveugle : chaque journée revient quatre fois, quoi qu'elle contienne. L'échéancier en est la version qui sait ce qu'elle renvoie.

## 4. Vers le présent : la page du passé

**Quand.** Au seuil : un mandat, une demande approfondie, un devis ou un préenregistrement qui naît ; un blocage ou un résultat négatif ; une question qui t'est posée ; ou sur demande.

**Comment.**
1. Dire l'objet du travail en deux lignes, puis cinq à dix termes de recherche, avec les anciens noms. Les noms dérivent : « bassins étroits », « puits étroits », « exploration » ; « organisme », « atelier d'idées ». Une **table des synonymes**, à ajouts seuls, les garde.
2. Chercher en plein texte dans les sources par l'outil borné, puis dans le journal.
3. Classer par pertinence, puis par âge : une place réservée à un élément de plus de trente jours et une à un élément de quatorze à trente jours, s'il en existe. Écarter ce que la pièce en cours cite déjà.
4. Ouvrir chaque passage ; ne jamais répondre du journal seul.
5. Rendre cinq remontées au plus : extrait, source, date, âge ; degré (« lu dans la source » ou « rapprochement de ma part ») ; et ce que cela change, d'un mot parmi cinq : **répond** · **contredit** · **déjà testé** (avec l'issue) · **promis, non fait** · **outil réutilisable**. Sinon : « non trouvé dans ce que j'ai lu », avec les termes cherchés.

**Le hasard a sa part.** Chaque semaine, trois fiches anciennes tirées au sort sont confrontées aux chantiers du moment. C'est le rejeu : il remonte ce qu'aucun mot du présent n'aurait appelé.

**Le pont entre les deux sens.** Un réveil « sur contexte » est une intention envoyée vers le futur qui se déclenche sur le présent : elle part d'un côté et arrive de l'autre.

## 5. Mesurer le sens vers le futur

| Mesure | Comment, hors des modèles | Cible |
|---|---|---|
| **Couverture** | par programme : toute fiche retenue ou gardée de côté, toute promesse, tout accord non jugé a une ligne, avec date ou événement et butoir | toutes |
| **Ponctualité** | par programme, sur les dates du journal : rendu le jour dû à un jour près, ou sous 24 heures après l'événement | 95 % |
| **Clôture** | part des retours rendus qui ont reçu l'une des trois fins sous sept jours | 80 % ; mesure la boucle entière, mère comprise |
| **Retours marqués** | la clé de la mère porte de vrais reports dont elle connaît la date : la ligne existe-t-elle sous sept jours ? revient-elle à l'heure ? | 80 % sur dix cas au moins |
| **Épreuve du mécanisme** (R5) | cas sain : un retour d'essai dû sous 24 heures part. Artefacts : un événement qui n'arrive jamais, le butoir doit partir ; une source déplacée, « source perdue » doit être dit ; un changement de compte, tout l'échu du trou doit être rendu au premier cycle | tous passés avant emploi |
| **Retours caducs** | part des retours arrivés sans objet | rapportée ; haute, les conditions sont mal écrites |

## 6. Mesurer le sens vers le présent

**Le banc rétrospectif à date épinglée.** Git garde le dépôt tel qu'il était. On choisit des moments passés où un travail est né, et pour lesquels on sait aujourd'hui, par une autre voie, qu'un élément ancien et pertinent existait : un inventaire l'a retrouvé plus tard, une décision le dit, ou toi. Un agent neuf reçoit le seul objet du travail et le dépôt à la date de ce jour-là ; il applique la procédure du § 4. Réussite : l'élément connu est dans ses cinq remontées. La clé est écrite par un agent qui ne joue pas la procédure, depuis les sources postérieures.

Deux cas vrais pour commencer : l'inventaire du 18 novembre écrit que deux tours du collisionneur du 26 octobre portaient « exactement » sur ce que la lecture par lentille neuronale étudie, « jamais relus » ; et la demande d'aujourd'hui sur l'exploration des idées, contre la synthèse des bassins étroits du 13 novembre. Dix cas pour une première mesure ; à dix, l'intervalle est large, et la borne basse est rapportée avec le taux.

| Mesure | Comment, hors des modèles | Cible |
|---|---|---|
| **Rappel** | banc rétrospectif : élément connu parmi cinq remontées | 70 %, borne basse rapportée |
| **Gain sur la recherche seule** | même agent, même objet, recherche plein texte nue, sans journal ni synonymes ; test exact de McNemar sur les paires, comme à l'épreuve de la bibliothécaire | rapporté tel quel |
| **Reprise** | par programme : la pièce écrite ensuite cite-t-elle le chemin d'une remontée ? | une page sur deux |
| **Nouveauté pour le destinataire** | par programme : part des remontées absentes du mandat et du brouillon | 70 % |
| **Distance** | part des remontées de plus de 14 et de 30 jours ; âge médian | rapportée ; une de plus de 30 jours par page, s'il en existe |
| **À l'heure** | page remise avant que la pièce ne commence, ou sous deux heures | 80 % |
| **Échappées** | élément ancien et pertinent trouvé plus tard par une autre voie | chacune inscrite, avec sa cause |

**Si la recherche nue fait aussi bien** — c'est ce que l'épreuve de la bibliothécaire a trouvé pour le mémo — la valeur de ce sens se réduit à l'initiative : faire la recherche quand personne ne la demande. On garde alors la page du passé comme une recherche programmée, et on retire la table des synonymes. Le résultat est rapporté quel qu'il soit.

## 7. Deux décisions de plus pour toi

**D-5 — Un organe ou deux.** Enjeu : un seul lieu pour la mémoire, sans que la demande n'étouffe la boucle ni que deux périmètres ne se mêlent. Options : (a) un organe, « la mémoire du dépôt » : la bibliothécaire interlocutrice, la boucle à l'heure dans des contextes neufs, un mandat, un périmètre, au plus tard au prochain changement de compte ; (b) deux sessions qui partagent outils et périmètre, comme dès maintenant ; (c) deux sessions séparées. Recommandation : (a), confiance 0,7. Défaut : (b).

**D-6 — La page du passé au seuil.** Enjeu : le réemploi se joue au moment où l'on conçoit, pas après. Options : (a) aucune conception délicate ni aucun devis ne part sans sa page ; si elle n'est pas prête sous deux heures, la pièce part et la page suit ; (b) sur demande seulement. Recommandation : (a), confiance 0,7. Défaut : (b).

## 8. Réserves

- Aucune cible n'est mesurée. Le banc rétrospectif n'existe pas encore ; ses deux premiers cas sont des propositions, à confirmer par celui qui écrira la clé.
- Un des deux cas (les bassins étroits) est connu de la veille par la première pièce : il sert à régler, non à mesurer.
- Je n'ai pas vérifié que les traces de procédure dont la veille a besoin sont sans contenu cloisonné : c'est la relecture demandée à la mère avant d'étendre la liste d'autorisation.
- Le mandat unique de l'organe fusionné n'est pas écrit : il attend D-5 et le texte du mandat en vigueur de la bibliothécaire (GO-2026-11-22-50).
