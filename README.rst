# tentativo di interfaccia web al GDA

creare un nuovo progetto django:

django-admin startproject gda

cd gda
mv gda gda.orig

clonare il progetto da github nella cartella appena creata

con git clone

python3 manage.py makemigrations 

python3 manage.py migrate 


-- promemoria

per esportare la definizione di un modello:

python3 manage.py inspectdb tabella

da inserire poi in models.py

se si vuole anche l'admin va inserito li il modello
