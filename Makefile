build:
	poetry build

reinstall: build
	pipx uninstall project
	pipx install dist/project-0.1.0-py3-none-any.whl
