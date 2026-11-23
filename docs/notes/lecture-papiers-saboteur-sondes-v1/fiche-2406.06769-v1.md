# Fiche de lecture — 2406.06769 v2 — « DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents »

- **Auteurs** : Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord, Peter Clark (Allen Institute, Microsoft Research, Arizona) ; arXiv 2406.06769 v2.
- **PDF** : `docs/sources/pdf/percee-controle-securite-v1/2406.06769v2.pdf`, sha256 `28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91` (recalculée, concorde avec le registre, R11).
- **Décision lue** : `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`, l. 114 (§ 4, banc de recherche à vérité plantée), avec son erratum 1 (E3, E5 : conception par le protocole X) et son erratum 2 (empreinte, sans effet ici).
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46:50Z.

---

**(a) Ce que le papier établit.** Un monde simulé en texte, sous licence Apache 2.0, de 120 tâches : huit thèmes, trois niveaux, variations paramétriques (p. 1 du PDF) ; chaque tâche demande hypothèses, expériences, analyse et conclusion (p. 1). Les variations sont tirées par une seule graine ; le banc officiel joue les graines 0 à 4, soit 8 × 3 × 5 = 120 tâches (p. 5). Trois mesures : achèvement, gestes utiles, connaissance découverte ; la troisième est notée par un humain ou par GPT-4o contre des questions binaires de référence (p. 6). Meilleur agent : 38 % des tâches faciles, 18 % des difficiles ; connaissance au mieux 34 % et 8 % (p. 9). Onze scientifiques : 66 % d'achèvement, 55 % de connaissance (p. 9). Le monde est voulu « realistic (but simplified) rather than counterfactual » (p. 2). Aucun adversaire, aucun sabotage (recherche par motifs sur tout le texte).

**(b) Ce que voulait la décision.** Le ranger parmi les voisins qui occupent une part du banc à vérité plantée : « mondes de découverte sans adversaire ». **Le permet** : la part occupée (mondes engendrés par programme, cycle complet de découverte, graines publiques) est bien là. La part laissée reste une question (R8), non un trou : vérité exacte, contrefactuelle, et dommage d'un sabotage diffus compté par un oracle hors de la machine. Le papier n'en dit rien ; sa connaissance est notée par un modèle, donc approchée.

**(c) Usage.** Pour l'entretien, objection 9 (« pourquoi des mondes plantés ? ») : des mondes de découverte publics existent ; les nôtres diffèrent par des lois contrefactuelles, qui résistent au savoir appris, et par un oracle exact. Pour la conception du banc, il fournit une base nommée et un témoin « un modèle juge qui note la connaissance ». Il crée une antériorité sur « environnement de découverte engendré par graine » : ne jamais dire ce trait neuf.

**(d) Plus petite action.** Ajouter « réaliste, non contrefactuel (p. 2) » et les taux de la page 9 à la ligne de DiscoveryWorld dans la table des voisins du banc à lois plantées (conception v2, l. 340), à sa prochaine version. Coût : dix minutes, aucune dépense. Le rejouer avec un saboteur demanderait un devis et un GO.
