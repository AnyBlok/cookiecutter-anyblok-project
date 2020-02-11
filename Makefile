

test:
##	rm -rf travis_mysql
##	cookiecutter . --no-input project_name=travis_mysql db_driver_name=mysql
##	make -C travis_mysql/ setup-tests
##	make -C travis_mysql/ test
##	make -C travis_mysql/ lint
##	make -C travis_mysql/ documentation
##	rm -rf travis
##	cookiecutter . --no-input project_name=travis
##	make -C travis/ setup-tests
##	make -C travis/ test
##	make -C travis/ lint
##	make -C travis/ documentation
##	rm -rf travis_pyramid
##	cookiecutter . --no-input project_name=travis_pyramid http_server=pyramid
##	make -C travis_pyramid/ setup-tests
##	make -C travis_pyramid/ test
##	make -C travis_pyramid/ lint
##	make -C travis_pyramid/ documentation
##	rm -rf travis_furetui
##	cookiecutter . --no-input project_name=travis_furetui furetui=yes
##	make -C travis_furetui/ setup-tests
##	make -C travis_furetui/ test
##	make -C travis_furetui/ lint
##	make -C travis_furetui/ documentation
	rm -rf travis_furetui_custom
	cookiecutter . --no-input project_name=travis_furetui_custom furetui=custom
	make -C travis_furetui_custom/ setup-tests
	make -C travis_furetui_custom/ test
	make -C travis_furetui_custom/ lint
	make -C travis_furetui_custom/ documentation
