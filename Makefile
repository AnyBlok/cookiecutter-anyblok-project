

test:
	rm -rf travis
	cookiecutter . --no-input project_name=travis
	make -C travis/ setup-tests
	make -C travis/ test
	make -C travis/ lint
	make -C travis/ documentation
	rm -rf travis_pyramid
	cookiecutter . --no-input project_name=travis_pyramid http_server=anyblok_pyramid
	make -C travis_pyramid/ setup-tests
	make -C travis_pyramid/ test
	make -C travis_pyramid/ lint
	make -C travis_pyramid/ documentation
