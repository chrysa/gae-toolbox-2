default: help

clean:
	@cd script_helper && python clean_app.py

create: clean
	@cd script_helper && python create_module.py

launch_app: clean
	@cd script_helper && python launch_app.py

launch_serv: clean
	@cd script_helper && python launch_serv.py

tests: clean
	@cd script_helper && python aff_tests.py

trad: clean
	@cd script_helper && python internationalize.py

help:
	@echo "---------------------------| commandes possibles |---------------------------------"
	@echo "clean		=> nettoyer l'application et les scripts helper des fichiers compilés"
	@echo "create		=> créer un nouveau nouveau module"
	@echo "launch_app	=> lancer l'application avec différentes options"
	@echo "launch_serv	=> lancer le serveur seul"
	@echo "tests		=> voir le résultat des tests unitaire"
	@echo "trad			=> lancer la traduction de l'application"