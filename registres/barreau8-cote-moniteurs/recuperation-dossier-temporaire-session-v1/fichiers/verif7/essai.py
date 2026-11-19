import sys
from controle_ia import prereg
S=sys.argv[1]
src='brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon7.md'
t=open(src,encoding='utf-8').read()
f3_old='À REMPLIR — À FIXER : tirée par la session mère au scellement'
lines=t.split('\n'); l413=lines[412]
h1='a'*64; h2='b'*64
new413='- **Contre-lecture 4 (finale, texte rempli)** — essai : brouillon relu `'+h1+'`, rapport `x.md`, empreinte `'+h2+'`.'
def essai(nom, txt):
    open(f'{S}/{nom}.md','w',encoding='utf-8').write(txt); print(nom, prereg.problemes(f'{S}/{nom}.md'))
t1=t.replace(f3_old,'0x1234abcd (essai)').replace(l413,new413)
essai('c1-tout-rempli', t1)
essai('c2-F3-ouvert', t.replace(l413,new413))
essai('c3-entree-ouverte', t.replace(f3_old,'0x1234abcd'))
essai('c4-entree4-une-empreinte', t1.replace(h2,'sans'))
essai('c5-3bis-amputee', t1.replace('2ab73c2f5d5210cb5102b3f805b4653e9dfef6efcfddde22cc47a30a0f603587','x'))
essai('c6-entree3-amputee', t1.replace('79be6f7eec2534cb9b01cc20ecc3b8720fb21952965ee09912a979cff0a57c30','x',1))
essai('c7-entree4-meme-empreinte-deux-fois', t1.replace(h2,h1))
h='79be6f7eec2534cb9b01cc20ecc3b8720fb21952965ee09912a979cff0a57c30'
i=t1.rfind(h); essai('c6b-entree3-amputee', t1[:i]+'x'+t1[i+64:])
