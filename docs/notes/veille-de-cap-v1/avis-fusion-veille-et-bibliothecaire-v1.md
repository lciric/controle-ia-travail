# Avis — fusionner la veille de cap et la bibliothécaire (v1)

Pièce de travail (classe C), écrite le 22 novembre 2026 vers 15:35Z par la session de conception (`session_01XJ6MgqK7APqd1Hi98jL4GT`), sur la question du directeur relayée par la mère : « oui, fusionnons bibliothécaire et veille de cap, si Fable est d'accord ». Sources : l'additif 1 de la conception (`b215a998…`), l'état de la bibliothécaire (`2a6f4b64…`), sa liste d'autorisation v3 (`6a9a41e3…`), R-4877.

**Décision à prendre.** Sous quelle forme la veille de cap et la bibliothécaire deviennent un seul organe de mémoire.

**Mon avis : d'accord pour fusionner — un organe, une seule session permanente, et la boucle hors de son contexte.** Ni « une session qui fait tout », ni « deux sessions permanentes ».

**Enjeu.** Un seul lieu où demander « où est-ce ? » et d'où vient « ceci attend », sans que la boucle s'étouffe, ni qu'une lecture large passe dans une réponse faite à un rôle restreint.

| Forme | Avantage | Inconvénient |
|---|---|---|
| (a) Une seule session répond et boucle | le plus simple | son contexte s'use en quelques jours ; la demande affame la boucle ; deux périmètres dans une même tête |
| (b) Deux sessions permanentes, un contrat | périmètres séparés | deux sessions à tenir en vie et à relancer ; la veille use aussi son contexte ; ce n'est pas la fusion voulue |
| (c) Une session permanente, la bibliothécaire, au périmètre strict ; la boucle en **cycles à contexte neuf**, lancés à l'heure, liés à elle par un **contrat de fichiers** | un interlocuteur ; aucune charge de contexte ; périmètres séparés ; une seule tâche programmée à recréer au changement de compte | un filtre de plus à écrire et à contre-lire ; les réponses de la mère passent par un fichier ; un démarrage par cycle |

**Recommandation : (c), confiance 0,7.**

**Les trois points demandés.**
- **L'épreuve.** Le mémo ne bat pas la recherche plein texte (42 sur 45 contre 45 sur 45). Fusionner ne doit donc pas grossir le mémo : il reste une carte, non étendue. L'organe vaut par l'état, l'absence, le temps et l'initiative ; son journal reste mince. Les deux moitiés sont « non éprouvées » : chacune passe son épreuve avant d'être jointe.
- **La charge de contexte.** Le registre des décisions prend environ 260 lignes par jour depuis le 13 novembre ; le cycle du passé relit six ou sept journées par jour ; le mémo pèse 850 000 octets. Une session qui porterait cela et des questions vivrait de résumés de résumés. La conception de la bibliothécaire veut déjà un contexte neuf par question ; la boucle suit la même règle : rien ne vit dans la conversation, tout dans les fichiers.
- **Le cloisonnement.** La liste de la bibliothécaire est celle du rôle le plus restreint qui peut l'interroger ; elle est étroite. La boucle doit lire plus large : toutes les notes pour la page du passé, les synthèses pour savoir si un gisement est dépouillé, les traces de procédure. Les deux lectures ne doivent jamais se trouver dans le même contexte. **Je corrige ici l'additif 1 (§ 2)**, qui proposait un périmètre unique étendu aux seules traces de procédure : c'est trop court pour la boucle.

**Le contrat de fichiers.**
1. Deux listes de lecture, appliquées par l'outil borné : la stricte (réponses) et celle de la boucle, relue par la mère.
2. Un journal à deux partitions, comme la mémoire des problèmes : « commune », tirée des seules sources de la liste stricte, lisible par la bibliothécaire ; « mère », le reste, retirée par programme de ce qu'elle lit.
3. Les cycles écrivent dans les fichiers et préviennent la mère d'un chemin et d'une empreinte ; aucun contenu ne passe par la session permanente.
4. La mère répond aux signaux par un fichier du canal, que le cycle suivant lit.

**Ordre de pose.**
1. Tout de suite, sans rien arrêter : les deux sessions continuent ; mandat v2 et additif 1 à la veille ; les deux outils de la bibliothécaire versés sur `main`.
2. Les deux listes et les deux partitions écrites ; la mère relit les premières lignes du journal.
3. Journal, échéancier et calendrier tenus quelques jours ; **reprise à froid réussie** : une session neuve reprend la boucle avec les seuls fichiers.
4. Épreuves passées : banc planté de l'extraction ; épreuve du mécanisme des retours ; porte de périmètre sur une journée entière de cycles, par le journal des fichiers ouverts.
5. Bascule : les cycles passent à une tâche programmée qui ouvre une session neuve à chaque fois ; la session de veille est close après versement de ses fichiers ; le mandat de la bibliothécaire reçoit une section — lire la partition commune pour dire l'état, relayer les retours qui te sont dus, consigner les questions reçues comme indices du présent. Un seul mandat, « la mémoire du dépôt ».

Pas de bascule avant que 3 et 4 tiennent ; au plus tard au prochain changement de compte, si elles tiennent. Si une session neuve par cycle coûte trop, repli : des sous-agents neufs lancés par la session permanente, dont le compte rendu ne porte qu'un chemin et une empreinte.

**Défaut sous 48 heures.** L'étape 1 : deux sessions qui partagent outils et fichiers. Elle est sûre et ne ferme rien.

**Réserves.** Rien n'est mesuré. Je n'ai pas lu le mandat en vigueur de la bibliothécaire (GO-2026-11-22-50) ni vérifié qui l'interroge aujourd'hui en dehors de toi et de la mère ; si aucun rôle restreint ne l'interroge sans passer par la mère, le contrat s'allège. L'outil borné ne lit que les fichiers permis, mais rien n'empêche un agent de lire hors de l'outil : la porte de périmètre le constate après coup, par le journal des fichiers ouverts.
