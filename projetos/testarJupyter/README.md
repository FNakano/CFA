Instalar Jupyter notebook no termux android

depois de instalar termux, atualizar com `pkg update` (instala ssh, tls o que resolve a instalação de crypt), depois instalar python com `pkg install python` depois instalar Jupyter com `pip install notebook`. Nota: instalar python instala python3 e pip. Caso dê erros de instalação:
- instala rust com `pkg install rust` (https://www.geeksforgeeks.org/how-to-install-rust-on-termux/);
- instala packaging com `pkg install packaging` (https://www.datasciencelearner.com/modulenotfounderror-no-module-named-packaging-solved/)
- instala wheel com `pip install wheel`
- instala zero-mq com `pkg install libzmq` (https://stackoverflow.com/questions/49805480/could-not-install-pyzmq-using-apt-pip-pip3-easy-install-etc-any-command)
	- tentar compilar zmq a partir do fonte dá errado: `/data/data/com.termux/files/usr/include/string.h:146:8: note: previous declaration is here: size_t strlcpy(char *__dst... 1 error generated
	- https://wiki.termux.com/wiki/Python (para instalar zmq, mas não deu certo) https://github.com/pypa/pip/issues/11358 (deprecate install options)
	- para compilar zmq mas não deu certo:
		- https://github.com/zeromq/pyzmq/issues/1469
		- https://github.com/termux/termux-packages/issues/10594
		- https://www.reddit.com/r/termux/comments/s5rsau/help_install_jupyter_lab_cant_built_pyzmq_and/
		- https://github.com/termux/termux-packages/issues/6241#issuecomment-802854734
		- https://github.com/termux/termux-packages/issues/5752
	- para instalar crypt (TLS, SSH) - isto foi resolvido com o update do termux.
		- https://cryptography.io/en/latest/installation/
		- https://community.home-assistant.io/t/termux-compilation-error-cryptography/472002
		- https://github.com/cher-nov/cryptg/issues/6
		- https://github.com/termux/termux-packages/blob/master/packages/libcrypt/crypt.h

Acho que esses são os problemas, depois que filtrei. Se precisar de algo mais, `pkg install build-essential`, `pkg install binutils` (https://stackoverflow.com/questions/71443172/error-could-not-build-wheels-for-coincurve-which-is-required-to-install-pyproj) pode ajudar.

Para acessar o notebook no navegador de outro computador na mesma rede local:
	
	- ajustar a senha com `jupyter notebook password` e seguir as instruções;
	- executar com `jupyter notebook <IP> --port 8888;
	- https://stackoverflow.com/questions/39155953/exposing-python-jupyter-on-lan

Criar um novo notebook:
	- https://www.dataquest.io/blog/jupyter-notebook-tutorial/
	
Parece que tem algum problema para conectar com o kernel do jupyter notebook (talvez o Android esteja desligando o wifi para poupar energia). Isso pode tornar a operação pouco confiável...
