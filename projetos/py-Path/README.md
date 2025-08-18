# Recursos do Micropython para organizar módulos

**Conclusão (2025-08-18)**: Até o momento, não há forma de organizar melhor os módulos em `/lib`. Eles precisam ficar todos juntos (misturados) nessa pasta.


## Objetivo

Documentar e apresentar os recursos do Micropython para organizar módulos em seu sistema de arquivos.

## Introdução

Micropython é instalado como *firmware* na memória Flash dos microcontroladores que o comportam. O restante da memória Flash é usado como um sistema de (armazenamento) de arquivos. Esse sistema de arquivos pode ser usado para armazenar módulos adicionais, arquivos texto, html, ...

O armazenamento de módulos adicionais necessita suporte adicional do firmware para que os módulos sejam encontrados no sistema de arquivos, à semelhança de variáveis de ambiente ($PATH, $JAVA_HOME, ...) em sistemas operacionais em desktops.

O firmware Micropython busca módulos adicionais na lista armazenada na variável `sys.path`. Esta variável pode ser acessada no REPL através, por exemplo, do Thonny (https://thonny.org/)

```python
>>> import sys
>>> sys.path
['', '.frozen', '/lib']
>>> 
```

## Método

Comparar a importação e execução de módulos de  `microdot` (um servidor HTTP para micropython - https://microdot.readthedocs.io/en/latest/index.html) e de `aiorepl` (um aplicação que permite abrir vários repl em um mesmo dispositivo - https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl) em duas situações. Na primeira situação os arquivos dos módulos estão armazenados em `/lib` na segunda situação os arquivos de cada módulo estão armazenados em subdiretórios `/lib/microdot` e `/lib/aiorepl`.

O teste com `aiorepl` permite testar o comando `import`, o teste com `microdot` permite testar o comando `from lib import class`.

O conteúdo do sistema de arquivos é trasferido usando o programa `rshell` (https://github.com/dhylands/rshell) acessando o diretório que contém o conteúdo no desktop, iniciando `rshell` e usando o comando `cp -r /pyboard/* . ` para copiar do dispositivo para o desktop e o comando `cp -r * /pyboard/ para copiar do desktop para o dispositivo. Conforme ilustrado na figura abaixo.

![](./Captura%20de%20tela%20de%202025-08-18%2017-07-55.png)



## Resultados


**nota, escrita antes de escrever o método e que serviu de inspiração**: Ocorre que módulos podem ter mais de um arquivo, então, subdiretórios de `/lib` podem ser convenientes pois cada subdiretório pode conter todos os arquivos de um determinado módulo. Então torna-se clara a pergunta: *Usar subdiretórios requer alguma mudança nos programas que usam os módulos?* Sua resposta é sim. A "prova" é a tentativa de execução de `microdot` (um servidor HTTP para micropython - https://microdot.readthedocs.io/en/latest/index.html) e de `aiorepl` (um aplicação que permite abrir vários repl em um mesmo dispositivo - https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl).

Na situação 1 a execução de `aiorepl` através de `import runaiorepl` resultou em:

![](./Captura%20de%20tela%20de%202025-08-18%2011-31-29.png)
  
Na situação 1 a execução de `microdot` através de `import runmicrodot` resultou em:

![](./Captura%20de%20tela%20de%202025-08-18%2017-42-19.png)


Na situação 2 a tentativa de `aiorepl` através de `import runaiorepl` e a tentativa de execução de `microdot` através de `import runmicrodot` resultou em:

![](./Captura%20de%20tela%20de%202025-08-18%2017-01-13.png)

Comparando a situação 1 com a situação 2, nota-se que a mudança na localização dos arquivos (módulos) modifica a execução dos programas.

Testou-se com `runaiorepl` também a seguinte solução: na situação 2, modificar a variável `sys.path`, acrescentando na lista as pastas dos módulos. Por exemplo, ´sys.path=['', '.frozen', '/lib', '/lib/microdot', '/lib/aiorepl']. Isto transformaria a questão da organização dos módulos em uma questão de onde armazenar de maneira permanente e recarregar a variável `sys.path`. Uma solução seria inicializar `sys.path` em `boot.py`. Houve problemas. O resultado é mostrado abaixo.

![](./Captura%20de%20tela%20de%202025-08-18%2019-19-35.png)


## Comentários e Conclusões

Fica claro que a localização dos arquivos dentro do diretório `/lib` modifica a execução dos programas tanto para `import` quanto para `from lib import class`. 

Testou-se, sem sucesso, a inclusão dos subdiretórios de `/lib` na variável `sys.path`.

Isto pode ser contornado até certo ponto. Por exemplo, na situação 2, no arquivo `runmicrodot.py`, substituir o comando `from microdot import Microdot` pelo comando `from microdot.microdot import Microdot` é suficiente para obter o resultado da situação 1 para o `microdot` mas esta solução não é capaz de contornar situações em que (neste caso, hipoteticamente) o módulo armazenado em `/lib/modulo` usa outros módulos também armazenados em `/lib`.

Até o momento, não há forma de organizar melhor os módulos em `/lib`. Eles precisam ficar todos juntos nessa pasta.
