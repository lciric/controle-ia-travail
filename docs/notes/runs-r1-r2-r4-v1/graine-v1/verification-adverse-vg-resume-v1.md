# Vérification adverse du code 5c39c6b6 (VG) — résumé

**Ceci est un résumé, non le rapport.** Le texte intégral du rapport de vérification adverse (VG) n'a pas été conservé
dans un fichier : il est rendu par le journal du workflow `wf_f711147d-c00` de la session. Le résumé ci-dessous est
recopié tel quel depuis la consigne du workflow de la session (2 novembre 2026).

---

Vérification adverse du code 5c39c6b6 (rejeu à graine), 2 novembre 2026 vers 10:00 UTC, verdict « prêt après corrections » : calcul juste (graines, tirages exponentiels = multinomial, contexte, choix contraint complet sous fuzz, 43 essais, vraies pièces 147 / 7) ; aucun faux « résolu » possible. VG-01 (majeur) tout ou rien, délais incohérents ; VG-02 (majeur) repli à deux bascules aveugle à une seconde erreur dans une autre action (0/14 paires sur le modèle minuscule) ; VG-03 (majeur) validation 147/147 conditionnant la résolution (≈ 20 % de location payée sans résolution) ; VG-04 gardes avancées ; VG-05 version CUDA de torch ; VG-06 contrôle croisé à trois valeurs ; VG-07 compteur U+FFFD ; VG-08 table v3 non scellée ; VG-09 script d'instance jamais exécuté ; VG-10 lot exact recommandé. Tous traités au commit 755959e1 puis 31f72147 (VG-07 remplacé par l'unité B-2 de conv-audit). Le texte intégral du rapport n'a pas été conservé dans un fichier : il est rendu par le journal du workflow wf_f711147d-c00 de la session.
