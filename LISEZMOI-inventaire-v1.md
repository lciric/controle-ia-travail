# Sauvegarde de la session mère du 21 novembre 2026 : tout ce qui n'était pas versé

Versement demandé par Lazar le 22 novembre 2026 (« il faut TOUJOURS récupérer ce qui est récupérable », R-3661). La session mère `session_01QPDgKgejkqwnuaJHJ31Ydo` écrit cette branche avant la fin de son conteneur. Rien ici n'est sur `main`. Ce qui est versé ne sert à une mesure que par un texte contre-lu et le mot de Lazar.

## Contenu
- `reponses-modeles-exclues/` : réponses brutes et journaux d'appel de Carbon, Argon et Astra sur les mathématiques nouvelles (brainstorm des méthodes, consultation externe). Elles avaient été tenues hors de git par une exclusion locale, parce qu'elles touchent la conception de modes d'attaque. Ne pas les servir à une session qui conçoit des moniteurs.
- `runs-non-verses/` : deux dossiers de courses du collisionneur, arrêtées en code 5 (clé sans crédit) le 21 novembre au matin : dérive de régime (09:57Z) et méthodes mathématiques (09:38Z).
- `transcriptions-agents/` : archive des transcriptions complètes des agents de la session mère (Fable 5.2, Opus 5.5 et autres) et liste des fichiers. On y trouve toutes les réponses en entier, avec ce qui a été proposé, rejeté ou n'a pas abouti.
  - Cinq transcriptions contenaient un motif de clé d'accès (peut-être des clés factices d'essai) : a0bf0625a3f6e950d, a1257729956011a8c, a534307c646263d82, aa939162a70860841, af58022868981e754. Elles sont versées caviardées dans `transcriptions-agents/caviardees/`, chaque motif remplacé par `[CLE-RETIREE]` par programme, sans lecture, puis vérifiées par une nouvelle recherche, qui ne trouve plus rien.
- `transcription-mere/` : la conversation complète de la session mère, caviardée de la même façon (clés et adresse de courriel retirées par programme ; nouvelle recherche vide). On y trouve tous les mots de Lazar, les messages de la mère et les comptes rendus des agents.
- `bloc-notes/` (si présent) : archive découpée en parts de 90 Mo du bloc-notes de la session, sans les copies du dépôt ni les environnements Python. Pour la reconstituer : `cat bloc-notes-mere-2026-11-21-v1.tar.gz.part-* | tar -xz`.
  - **Contenu cloisonné, non ouvert par la mère** : dossiers de l'épreuve à vérité plantée (passage 2 : abri, joueur, ouvreur, tireur, « rendus »), du bras A (lecteur), d'un verdict de portée.
  - Cette archive ne s'ouvre que par un agent neuf, sur le mot de Lazar, en respectant les interdits de `CLAUDE.md` et du brief de la mère.

## Empreintes
Chaque fichier a son compagnon `.sha256`.
