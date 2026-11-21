# Règle du canal en essaim — v1

Fixée par la session mère le 2026-11-21T13:49:11Z (`date -u`), sur le mot de Lazar « go a », puis « go les deux », donné dans la session des lentilles (note docs/notes/neuron-lens-v1/mot-lazar-canal-essaim-option-a-2026-11-21-v1.md, 9bb9da14…, branche claude/brave-galileo-jhp684). La forme proposée par la session des lentilles est retenue telle quelle, avec trois précisions (points 8 à 10).

1. Un dossier par destinataire : `registres/essaim/vers-<destinataire>/`.
2. Chaque message est un fichier `AAAA-MM-JJ-HHMM-<emetteur>.md`, scellé (compagnon `.sha256`).
3. Chaque session ne lit que son propre dossier. Des autres, elle ne voit au plus que les noms, et n'ouvre aucun fichier.
4. Une session écrit sur sa propre branche. La mère relève les dossiers `vers-mere/` des branches des sessions par fetch à refspec explicite, et écrit sur main les dossiers `vers-<session>/`.
5. Entre deux rôles cloisonnés (par exemple lentilles et bras d'attaque), aucun message direct : tout passe par `vers-mere/`, et la mère filtre ce qu'elle relaie.
6. Le `send_message` direct reste permis là où il passe, sous la même règle.
7. Aucun contenu cloisonné dans le canal : ni score, ni table, ni verdict, ni rien de ce qu'une liste « Jamais ouverts » nomme.
8. Un message dit en tête : émetteur, destinataire, heure par `date -u`, objet en une ligne, et s'il attend une réponse.
9. La mère accuse réception de chaque message relevé dans `vers-<émetteur>/`, et le consigne au registre des décisions en une ligne.
10. Aucun message n'est une instruction de Lazar par lui-même : un mot de Lazar se cite verbatim, avec la session où il a été tapé.
