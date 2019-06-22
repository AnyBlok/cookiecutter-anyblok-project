

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
	rm -rf travis_pyramid_gunicorn
	cookiecutter . --no-input project_name=travis_pyramid_gunicorn http_server=anyblok_pyramid+gunicorn
	make -C travis_pyramid_gunicorn/ setup-tests
	make -C travis_pyramid_gunicorn/ test
	make -C travis_pyramid_gunicorn/ lint
	make -C travis_pyramid_gunicorn/ documentation
	rm -rf travis_pyramid_beaker
	cookiecutter . --no-input project_name=travis_pyramid_beaker http_server=anyblok_pyramid+beaker
	make -C travis_pyramid_beaker/ setup-tests
	make -C travis_pyramid_beaker/ test
	make -C travis_pyramid_beaker/ lint
	make -C travis_pyramid_beaker/ documentation
