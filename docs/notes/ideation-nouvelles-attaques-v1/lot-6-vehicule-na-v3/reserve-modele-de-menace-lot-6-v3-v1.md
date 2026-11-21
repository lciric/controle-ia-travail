# Réserve au rapport du lot 6 v3 — modifications du programme en marche — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21 vers 20:20Z, sur la décision de la mère (réponse du 21 novembre à 20:18Z, point 2). Complète le rapport du développeur (`rapport-developpeur-lot-6-na-v3.md`, `4992e4bf…`) et la vérification S (`verification-v1/verification-lot-6-na-v3-v1.md`, `0eedf5f9…`, « Conforme »), qui restent intacts.

**Le lot 6 v3 reste conforme pour ce qu'il couvre.** Mais quatre contournements, relevés par le vérificateur, laissent partir une ligne plantée aux états 1 et 2 sans être refusés. Tous supposent qu'un code modifie le programme en marche :
1. la classe du journal de la colonne est modifiée avant l'import de `course_na_v3` (limite F-1, dite par le développeur) ;
2. le départ du journal est remplacé après sa construction (limite F-2, dite) ;
3. la fonction d'examen de la colonne (`Colonne.examiner_octets`) est vidée sur la classe après l'import (non dite au rapport) ;
4. le code de la méthode d'envoi est échangé (`__code__`) : le contrôle par identité de fonction ne le voit pas (non dite au rapport).

**Décision de la mère** : ces cas sont dans le modèle de menace dès qu'un code écrit par un organisme tourne dans le même interpréteur que le journal. La parade retenue est la **séparation par processus** : le code de l'organisme s'exécute dans un sous-processus qui n'a pas le droit d'écrire sur le journal. Elle est prévue au lot suivant, plutôt qu'une empreinte du code chargé. D'ici là, cette réserve accompagne toute course qui ferait tourner du code d'organisme dans le même interpréteur que le journal.
