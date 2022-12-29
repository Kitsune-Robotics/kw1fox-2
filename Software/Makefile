ROOT := $(PWD)
SRC := $(ROOT)/kw1fox_2

# Shortcuts and stuff

all: help

help:
	@echo
	@echo "Targets:"
	@echo "   deploy           Shortcut for rsync deploy."
	@echo

# Shortcut for deploy
deploy:
	# Transfer
	scp -r $(SRC) joe@10.85.3.154:/tmp

	ssh joe@10.85.3.154 "/tmp/kw1fox_2/scripts/install.sh"

	# Restart
	# ssh joe@10.85.3.154 "sudo -S systemctl daemon-reload"
	# ssh joe@10.85.3.154 "sudo -S systemctl restart kw1fox"
