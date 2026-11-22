# Sauvegarde de la session mère du 21 novembre 2026 : tout ce qui n'était pas versé

Versement demandé par Lazar le 22 novembre 2026 (« il faut TOUJOURS récupérer ce qui est récupérable », R-3661). La session mère `session_01QPDgKgejkqwnuaJHJ31Ydo` écrit cette branche avant la fin de son conteneur. Rien ici n'est sur `main`. Ce qui est versé ne sert à une mesure que par un texte contre-lu et le mot de Lazar.

## Contenu
- `reponses-modeles-exclues/` : réponses brutes et journaux d'appel de Carbon, Argon et Astra sur les mathématiques nouvelles (brainstorm des méthodes, consultation externe). Elles avaient été tenues hors de git par une exclusion locale, parce qu'elles touchent la conception de modes d'attaque. Ne pas les servir à une session qui conçoit des moniteurs.
- `runs-non-verses/` : deux dossiers de courses du collisionneur, arrêtées en code 5 (clé sans crédit) le 21 novembre au matin : dérive de régime (09:57Z) et méthodes mathématiques (09:38Z).
- `transcriptions-agents/` : archive des transcriptions complètes des agents de la session mère (Fable 5.2, Opus 5.5 et autres) et liste des fichiers. On y trouve toutes les réponses en entier, avec ce qui a été proposé, rejeté ou n'a pas abouti.
  - Cinq transcriptions contenaient un motif de clé d'accès (peut-être des clés factices d'essai) : a0bf0625a3f6e950d, a1257729956011a8c, a534307c646263d82, aa939162a70860841, af58022868981e754. Elles sont versées caviardées dans `transcriptions-agents/caviardees/`, chaque motif remplacé par `[CLE-RETIREE]` par programme, sans lecture, puis vérifiées par une nouvelle recherche, qui ne trouve plus rien.
- `transcription-mere/` : la conversation complète de la session mère, caviardée de la même façon (clés et adresse de courriel retirées par programme ; nouvelle recherche vide). On y trouve tous les mots de Lazar, les messages de la mère et les comptes rendus des agents.
- `bloc-notes/` : archive du bloc-notes de la session, découpée en parts de 90 Mo (797 Mo en tout). Pour la reconstituer : `cat bloc-notes-mere-2026-11-21-sans-chaine-ni-passage-2-v1.tar.gz.part-* | tar -xz`. On y trouve les textes extraits des PDF, les PDF téléchargés (dont ceux qui ne sont pas versés sur main), les outils, les essais et les sorties de travail des agents. Quatre fichiers y portaient un motif de clé (jouets d'essai, page de prix) : ils sont caviardés par programme, et une nouvelle recherche ne trouve plus rien.
  - **Non archivés, inventoriés seulement** (noms et tailles, `bloc-notes/inventaire-dossiers-non-archives-v1.tsv.gz`, 431 054 lignes) :
    - `chaine/` : la chaîne d'outils Lean, 10,3 Go, reconstructible de ses sources ;
    - les copies de code faites pour les essais de mutation (`mutations*`, `mut`, `retrait-*`, `corrige*`), reconstructibles ;
    - les trois dossiers de travail cloisonnés du second passage de l'épreuve à vérité plantée (`ouvreur-passage-2`, `abri-epreuve-passage-2`, `joueur-passage-2`, 1,8 Go), non ouverts par la mère. Leurs sorties ont été versées par leurs agents sous `docs/notes/barreau5-resolution-v1/plan-avant-entretien/epreuve-verite-plantee/passage-2/`, à vérifier contre l'inventaire. Ils restent sur le disque du conteneur de l'ancienne mère tant qu'il vit.
  - Cloisonnement : l'archive peut contenir d'autres sorties de travail des chantiers cloisonnés (bras A, verdict de portée). Elle ne s'ouvre que par un agent neuf, sur le mot de Lazar, en respectant les interdits de `CLAUDE.md`.

## Empreintes
Chaque fichier a son compagnon `.sha256`.
