# Mot de Lazar : canal en essaim entre sessions, option (a) — 2026-11-21 — v1

Note de la session des lentilles (session_01QPDgKhLLz1oJQwPBeB5aFs). Mot tapé par Lazar dans cette session, vers 2026-11-21T13:44Z, verbatim : « go a ».

## La question posée, avec ses options
Faut-il un canal en essaim entre les sessions, et sous quelle règle ?
- **(a)** Un canal dans le dépôt. Chaque session ne lit que les messages qui lui sont adressés. Tout échange entre rôles cloisonnés passe par la mère, qui filtre.
- **(b)** Le relais à la main par Lazar.
- **(c)** Chaque session relève les fichiers des autres sur leurs branches.

La recommandation de la session des lentilles était (a).

## Le contexte
- La session de l'attaquant informé a proposé le canal le 21 vers 13:08Z, en invoquant le mot de Lazar « mettez-vous en canal de communication en essaim ».
- Ses envois vers la mère sont refusés, comme ceux de la session des lentilles depuis 10:25Z. L'erreur est « elevated_session_untrusted_device ».

## Forme proposée par la session des lentilles, à fixer par la mère
1. **Dossiers par destinataire.** Un dossier par destinataire : `registres/essaim/vers-<destinataire>/`.
2. **Nom et sceau des messages.** Chaque message est un fichier `AAAA-MM-JJ-HHMM-<emetteur>.md`, scellé (compagnon `.sha256`).
3. **Lecture.** Chaque session ne lit que son propre dossier. Des autres dossiers, elle ne voit au plus que les noms, et elle n'ouvre aucun de leurs fichiers.
4. **Écriture et relais.**
   - Une session écrit sur sa propre branche.
   - La mère relève les dossiers `vers-mere/` des branches des sessions, par fetch à refspec explicite.
   - La mère écrit sur main les dossiers `vers-<session>/`.
5. **Rôles cloisonnés.** Entre deux rôles cloisonnés, par exemple les lentilles et le bras d'attaque, aucun message direct : tout passe par `vers-mere/`. La mère filtre ce qu'elle relaie.
6. **Envois directs.** Le `send_message` direct reste permis là où il passe, sous la même règle de cloisonnement.
7. **Contenu interdit.** Aucun contenu cloisonné dans le canal : ni score, ni table, ni verdict, ni rien de ce qu'une liste « Jamais ouverts » nomme.
