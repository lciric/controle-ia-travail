"""Typographie française : espaces insécables dans les nombres, avant : ; ? ! % » et après «."""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()
NB = " "
# séparateur de milliers
t = re.sub(r"(?<=\d) (?=\d{3}(?!\d))", NB, t)
# avant ponctuation double, pourcentage, guillemet fermant
t = re.sub(r" (?=[:;?!%»])", NB, t)
# après guillemet ouvrant
t = re.sub(r"« ", "«" + NB, t)
# obèle de statut collé au titre
t = re.sub(r" †", NB + "†", t)
# flèche : garder les blancs ordinaires
open(dst, "w", encoding="utf-8").write(t)
