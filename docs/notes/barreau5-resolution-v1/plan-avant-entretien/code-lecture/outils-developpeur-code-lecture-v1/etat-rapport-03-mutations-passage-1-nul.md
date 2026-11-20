# Rapport du développeur du code de lecture (barreau 5) — état 3 : premier passage de mutations nul

Écrit le 2026-11-20 vers 01:00Z (Claude Opus 5.5). État intermédiaire scellé.

- Essais verts sur l'état courant du code : lecture 80, sondes 16, relecture 20, lanceur 14.
- **Premier passage de mutations (00:55Z à 00:57Z) : nul.** Les 57 mutations jouées y passaient toutes pour « attrapées »,
  en une demi-seconde chacune : trop beau (R4). Cause, vue en rejouant le témoin à la main : l'outil passait à pytest un
  `--basetemp` dont le dossier parent n'existait pas ; le premier essai qui demande un dossier temporaire échouait d'entrée,
  avec ou sans mutation. Les quatre témoins sans mutation de ce passage échouent (code 1), ce que le bilan montre ; l'outil
  ne les exigeait pas verts avant de compter. Bilan gardé dans le bloc-notes, non compté.
- Outil corrigé (`mutations-code-lecture-v1.py`) : dossier des temporaires créé ; cinq témoins sans mutation exigés verts
  avant tout compte ; une mutation n'est attrapée que si pytest rend le code 1 (un essai échoue) ; tout autre code est une
  erreur de l'outil, comptée à part. Second passage lancé vers 00:58Z.
