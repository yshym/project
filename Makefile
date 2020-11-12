build:
	poetry build

reinstall: build
	pipx uninstall project
	pipx install dist/project*.whl
