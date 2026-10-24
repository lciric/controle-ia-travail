# Organisme factice (tests du noyau)

Écrit par la session Claude pour tester la mécanique du noyau (bac à sable, serveur d'appels, archive, succession,
jugement) sans réseau. Il n'est jamais donné à l'essaim réel. Il apprend de façon simple : il demande à une espèce
des indices sur les exemples positifs, les fait vérifier par une autre, garde ceux qui sont validés dans
`connaissances.json`, s'en sert pour répondre aux tâches, puis se recopie en successeur avec sa mémoire.
