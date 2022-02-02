update_ui:
	pyside6-uic monitor/view/from_ui.ui > monitor/view/from_ui.py
uml_generation:
	pyreverse -o svg monitor
update_requi:
	pip3 freeze > requirements.txt