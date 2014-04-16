.SILENT:

.DEFAULT:
	echo je ne sais pas faire $< tapes make help pour connaitre les commandes valides
	make help

clean:
	cd helpers && python clean_app.py

create: clean
	cd helpers && python create_module.py

launch_app: clean
	cd helpers && python launch_app.py

launch_serv: clean
	cd helpers && python launch_serv.py

tests: clean
	cd helpers && python aff_tests.py

trad: clean
	cd helpers && python internationalize.py

help:
	echo "---------------------------| commandes possibles |---------------------------------"
	echo "clean			=> nettoyer l'application et les scripts helper des fichiers compilés"
	echo "create		=> créer un nouveau nouveau module"
	echo "launch_app	=> lancer l'application avec différentes options"
	echo "launch_serv	=> lancer le serveur seul"
	echo "tests		    => voir le résultat des tests unitaire"
	echo "trad			=> lancer la traduction de l'application"