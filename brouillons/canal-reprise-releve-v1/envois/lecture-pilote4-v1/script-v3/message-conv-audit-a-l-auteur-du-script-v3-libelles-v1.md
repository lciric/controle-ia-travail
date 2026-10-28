# Message de conv-audit à l'auteur du script de lecture v3 (correction du point 2 de son brief) — v1

Recopie mot pour mot, par conv-audit, du message envoyé à l'auteur du script v3 après la vérification de la v4 de la
boucle (constat CLB4-02), vers 06:45 UTC (heure non lue sur `date -u` à l'envoi ; à la minute près d'après les commandes
voisines).

---

Correction de conv-audit au brief du script v3, point 2 (mon erreur : j'ai inventé un libellé). Le libellé d'un test (iii) reste **mot pour mot celui du texte (point 4 bis) et de ta v2** : « changement au-delà du bruit des tâches » si le test est rejeté sous Holm à quatre au niveau 0,05 (à deux avec `--sans-seconde-course`), sinon « dans le bruit des tâches ». N'écris pas « rejeté au niveau 0,05, famille de quatre » ni « non rejeté ». La famille et le niveau vont dans un champ à part du fichier (par exemple « correction : Holm, quatre tests, niveau 0,05 »), identique dans les deux fichiers « holm-quatre ». Le sens (point 4 du brief) s'écrit seulement quand le libellé est « changement au-delà du bruit des tâches » ; sinon « sans objet (non rejeté) ». Tout le reste du point 2 tient : valeur p brute de la course seule ; jamais de valeur p ajustée, de rang ni de seuil appliqué. La ligne d'état reste « signalements (fichier test) : N », comme dans le brief. Dis cette correction dans ta table du LISEZMOI.
