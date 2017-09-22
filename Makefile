

test:
	rm -rf travis
	cookiecutter . --no-input project_name=travis
	make -C travis/ setup-tests
	make -C travis/ test
	make -C travis/ lint
	make -C travis/ documentation
