run:
	@uvicorn workout_api.main:app --reload
	
# @uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

# Gerar requirements

# Nome do arquivo final de requisitos
REQUIREMENTS_FILE = requirements.txt

# Regras para gerar requirements.txt
all: gorequirements

gorequirements: $(REQUIREMENTS_FILE)

$(REQUIREMENTS_FILE):
	conda list --export > conda-requirements.txt
	pip freeze > pip-requirements.txt
	cat conda-requirements.txt pip-requirements.txt > $(REQUIREMENTS_FILE)
	rm conda-requirements.txt pip-requirements.txt

# Limpar arquivos temporários
clean:
	rm -f conda-requirements.txt pip-requirements.txt $(REQUIREMENTS_FILE)