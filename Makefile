SHELL=/bin/bash

# ----------------------------------------------------------------------------
# OS Specific VARS
# ----------------------------------------------------------------------------

ifeq ($(OS), Windows_NT)				# Windows
	SCRIPTS_DIR=./venv/Scripts
else									# Linux/Unix
	SCRIPTS_DIR=./venv/bin
endif

# ----------------------------------------------------------------------------
# VARS
# ----------------------------------------------------------------------------
PYTHON=python
PYTHON_VENV=${SCRIPTS_DIR}/python
PIP=${SCRIPTS_DIR}/python -m pip


# ----------------------------------------------------------------------------
# TARGETS
# ----------------------------------------------------------------------------

#% ----------------------------------------------------------------------------------------
#% Command                         : Information
#% --------------------------------:-------------------------------------------------------

## help                            : Prints this message and exits.
help:
	@sed -n 's/^#% //p' $(MAKEFILE_LIST)
	@sed -n 's/^## //p' $(MAKEFILE_LIST) | sort


## setup                           : Setup the project and install base + test dependencies.
setup: ./venv/pyvenv.cfg

## clean                           : Removes venv.
clean:
	rm -rf ./venv

## run                             : Generate the social host lists.
run: setup
	${PYTHON_VENV} scripts/generate_social_media_hosts.py



# ----------------------------------------------------------------------------
# Helper Targets
# ----------------------------------------------------------------------------

./venv/pyvenv.cfg:
	${PYTHON} -m venv venv; \
	${PIP} install --upgrade pip; \
	${PIP} install -r requirements.txt