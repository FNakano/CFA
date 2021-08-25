# Primeira experiência com Mozilla Web of Things

Resultado de colaboração com:

- André Luis Menezes Silva
- José de Jesus Perez-Alcazar
- Vinicius Zacarias Lacerda Brito
- Henrique Nakaema Simões
- Haverá mais colaboradores à medida que este trabalho crescer.

Agradecimentos a Otávio e Daniel Cordeiro.

### Histórico

Copiado em 2021-08-25-115100

## Introdução

[Mozilla Web of Things](https://iot.mozilla.org/) é uma plataforma aberta para controlar e monitorar dispositivos através da Web. 

Segundo [esta referência](https://hacks.mozilla.org/2020/12/flying-the-nest-webthings-gateway-1-0/) é uma iniciativa incubada pela Fundação Mozilla e ganhou autonomia no final de 2020 , sendo, agora, acessada pelo site https://webthings.io/.

Segundo [esta outra referência](https://webthings.io/about/), para usar a plataforma, inicia-se pela instalação do WebThings Gateway, que é uma distribuição de software para gateways para casas inteligentes (*smart homes*), que permite aos usuários monitorar e controlar sua casa inteligente através da Web. (nota do autor: tomei a liberdade de remover do texto original algumas características com as quais não concordo: *directly* e *without a middleman*).

Tutoriais apresentando instalação, configuração e uso da plataforma estão disponíveis na Internet e são de acesso livre. 

Com a finalidade de ter um dispositivo funcionando sobre a infraestrutura Mozilla Web of Things, é necessário seguir vários desses tutoriais, resolver particularidades do sistema utilizado, até, ao final, apresentar os testes do dispositivo e da infraestrutura.

Este documento apresenta quais tutoriais foram seguidos, os resultados obtidos. Cita problemas, soluções e referências adicionais, quando necessário, pelo julgamento dos autores.

## Objetivo

Ter um dispositivo funcionando sobre a infraestrutura Mozilla Web of Things.

## Método

1. Criar gateway seguindo o tutorial https://github.com/WebThingsIO/gateway
   - talvez seja mais conveniente iniciar pelo passo 2 para seguir os passos 1 e 3 em sequência;
2. Construir e programar o dispositivo seguindo o tutorial https://hacks.mozilla.org/2018/04/making-a-web-thing-on-the-esp8266/
3. Configurar gateway e proxy seguindo os tutoriais
   - https://webthings.io/docs/gateway-user-guide.html
   - https://webthings.io/docs/gateway-getting-started-guide.html
4. Testar dispositivo e infraestrutura.
   - [Resultado final deste relatório, apresentado neste vídeo]().

## Resultados

### Criar gateway

Em https://webthings.io/gateway/ são apresentadas algumas maneiras de criar o gateway. Dentre elas, pacotes pré-compilados para algumas distribuições de Linux, mostradas em https://github.com/WebThingsIO/gateway/releases/tag/1.0.0. 

Como o sistema utilizado está baseado na distribuição Ubuntu 20.04LTS, e existe pacote de instalação para essa distribuição, tentou-se essa abordagem, sem sucesso, pois o pacote contém referência para `libffi6`, que não está disponível na distribuição. Detalhes estão anotados neste registro do diário.

Partiu-se para a [instalação a partir do código-fonte](https://github.com/WebThingsIO/gateway#download-and-build-gateway), que foi feita com sucesso. O resultado da execução dos comandos indicados no tutorial são apresentados a seguir.

<pre><font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 13527  100 13527    0     0  10486      0  0:00:01  0:00:01 --:--:-- 10486
=&gt; Downloading nvm from git to &apos;/home/fabio/.nvm&apos;
=&gt; Cloning into &apos;/home/fabio/.nvm&apos;...
remote: Enumerating objects: 333, done.
remote: Counting objects: 100% (333/333), done.
remote: Compressing objects: 100% (283/283), done.
remote: Total 333 (delta 38), reused 150 (delta 25), pack-reused 0
Receiving objects: 100% (333/333), 177.15 KiB | 2.57 MiB/s, done.
Resolving deltas: 100% (38/38), done.
=&gt; Compressing and cleaning up git repository

=&gt; Appending nvm source string to /home/fabio/.bashrc
=&gt; Appending bash_completion source string to /home/fabio/.bashrc
=&gt; You currently have modules installed globally with `npm`. These will no
=&gt; longer be linked to the active version of Node when you install a new node
=&gt; with `nvm`; and they may (depending on how you construct your `$PATH`)
=&gt; override the binaries of modules installed with `nvm`:

/usr/local/lib
├── node-gyp@8.1.0
=&gt; If you wish to uninstall them at a later point (or re-install them under your
=&gt; `nvm` Nodes), you can remove them from the system Node as follows:

     $ nvm use system
     $ npm uninstall -g a_module

=&gt; Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR=&quot;$HOME/.nvm&quot;
[ -s &quot;$NVM_DIR/nvm.sh&quot; ] &amp;&amp; \. &quot;$NVM_DIR/nvm.sh&quot;  # This loads nvm
[ -s &quot;$NVM_DIR/bash_completion&quot; ] &amp;&amp; \. &quot;$NVM_DIR/bash_completion&quot;  # This loads nvm bash_completion
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ . ~/.bashrc
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ nvm install
Found &apos;/home/fabio/Documentos/git/gateway/.nvmrc&apos; with version &lt;lts/dubnium&gt;
Downloading and installing node v10.24.1...
Downloading https://nodejs.org/dist/v10.24.1/node-v10.24.1-linux-x64.tar.xz...
############################################################################################# 100,0%
Computing checksum with sha256sum
Checksums matched!
Now using node v10.24.1 (npm v6.14.12)
Creating default alias: <font color="#859900">default</font> <font color="#002B36">-&gt;</font> <font color="#B58900"><b>lts/dubnium</b></font> (<font color="#002B36">-&gt;</font> <font color="#859900">v10.24.1</font>)
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ nvm use
Found &apos;/home/fabio/Documentos/git/gateway/.nvmrc&apos; with version &lt;lts/dubnium&gt;
Now using node v10.24.1 (npm v6.14.12)
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ nvm alias default $(node -v)
<font color="#859900">default</font> <font color="#002B36">-&gt;</font> <font color="#859900">v10.24.1</font>
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ node --version
v10.24.1
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ npm --version
6.14.12
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ npm ci
<span style="background-color:#073642"><font color="#EEE8D5">npm</font></span> <span style="background-color:#B58900"><font color="#073642">WARN</font></span> <font color="#D33682">prepare</font> removing existing node_modules/ before installation

&gt; sqlite3@5.0.2 install /home/fabio/Documentos/git/gateway/node_modules/sqlite3
&gt; node-pre-gyp install --fallback-to-build

<span style="background-color:#073642"><font color="#EEE8D5">node-pre-gyp</font></span> <span style="background-color:#B58900"><font color="#073642">WARN</font></span> <font color="#D33682">Using request for node-pre-gyp https download</font> 
[sqlite3] Success: &quot;/home/fabio/Documentos/git/gateway/node_modules/sqlite3/lib/binding/napi-v3-linux-x64/node_sqlite3.node&quot; is installed via remote

&gt; segfault-handler@1.3.0 install /home/fabio/Documentos/git/gateway/node_modules/segfault-handler
&gt; node-gyp rebuild

make: Entrando no diretório &apos;/home/fabio/Documentos/git/gateway/node_modules/segfault-handler/build&apos;
  CXX(target) Release/obj.target/segfault-handler/src/segfault-handler.o
In file included from <b>../../nan/nan.h:56</b>,
                 from <b>../src/segfault-handler.cpp:2</b>:
<b>/home/fabio/.cache/node-gyp/10.24.1/include/node/node.h:573:43:</b> <font color="#D33682"><b>warning: </b></font>cast between incompatible function types from ‘<b>void (*)(Nan::ADDON_REGISTER_FUNCTION_ARGS_TYPE)</b>’ {aka ‘<b>void (*)(v8::Local&lt;v8::Object&gt;)</b>’} to ‘<b>node::addon_register_func</b>’ {aka ‘<b>void (*)(v8::Local&lt;v8::Object&gt;, v8::Local&lt;v8::Value&gt;, void*)</b>’} [<font color="#D33682"><b>-Wcast-function-type</b></font>]
  573 |       (node::addon_register_func) (regfunc<font color="#D33682"><b>)</b></font>,                          \
      |                                           <font color="#D33682"><b>^</b></font>
<b>/home/fabio/.cache/node-gyp/10.24.1/include/node/node.h:607:3:</b> <font color="#2AA198"><b>note: </b></font>in expansion of macro ‘<b>NODE_MODULE_X</b>’
  607 |   <font color="#2AA198"><b>NODE_MODULE_X</b></font>(modname, regfunc, NULL, 0)  // NOLINT (readability/null_usage)
      |   <font color="#2AA198"><b>^~~~~~~~~~~~~</b></font>
<b>../src/segfault-handler.cpp:346:3:</b> <font color="#2AA198"><b>note: </b></font>in expansion of macro ‘<b>NODE_MODULE</b>’
  346 |   <font color="#2AA198"><b>NODE_MODULE</b></font>(segfault_handler, init)
      |   <font color="#2AA198"><b>^~~~~~~~~~~</b></font>
In file included from <b>/home/fabio/.cache/node-gyp/10.24.1/include/node/node.h:63</b>,
                 from <b>../../nan/nan.h:56</b>,
                 from <b>../src/segfault-handler.cpp:2</b>:
/home/fabio/.cache/node-gyp/10.24.1/include/node/v8.h: In instantiation of ‘<b>void v8::PersistentBase&lt;T&gt;::SetWeak(P*, typename v8::WeakCallbackInfo&lt;P&gt;::Callback, v8::WeakCallbackType) [with P = node::ObjectWrap; T = v8::Object; typename v8::WeakCallbackInfo&lt;P&gt;::Callback = void (*)(const v8::WeakCallbackInfo&lt;node::ObjectWrap&gt;&amp;)]</b>’:
<b>/home/fabio/.cache/node-gyp/10.24.1/include/node/node_object_wrap.h:84:78:</b>   required from here
<b>/home/fabio/.cache/node-gyp/10.24.1/include/node/v8.h:9502:16:</b> <font color="#D33682"><b>warning: </b></font>cast between incompatible function types from ‘<b>v8::WeakCallbackInfo&lt;node::ObjectWrap&gt;::Callback</b>’ {aka ‘<b>void (*)(const v8::WeakCallbackInfo&lt;node::ObjectWrap&gt;&amp;)</b>’} to ‘<b>Callback</b>’ {aka ‘<b>void (*)(const v8::WeakCallbackInfo&lt;void&gt;&amp;)</b>’} [<font color="#D33682"><b>-Wcast-function-type</b></font>]
 9502 |                <font color="#D33682"><b>reinterpret_cast&lt;Callback&gt;(callback)</b></font>, type);
      |                <font color="#D33682"><b>^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</b></font>
/home/fabio/.cache/node-gyp/10.24.1/include/node/v8.h: In instantiation of ‘<b>void v8::PersistentBase&lt;T&gt;::SetWeak(P*, typename v8::WeakCallbackInfo&lt;P&gt;::Callback, v8::WeakCallbackType) [with P = Nan::ObjectWrap; T = v8::Object; typename v8::WeakCallbackInfo&lt;P&gt;::Callback = void (*)(const v8::WeakCallbackInfo&lt;Nan::ObjectWrap&gt;&amp;)]</b>’:
<b>../../nan/nan_object_wrap.h:65:61:</b>   required from here
<b>/home/fabio/.cache/node-gyp/10.24.1/include/node/v8.h:9502:16:</b> <font color="#D33682"><b>warning: </b></font>cast between incompatible function types from ‘<b>v8::WeakCallbackInfo&lt;Nan::ObjectWrap&gt;::Callback</b>’ {aka ‘<b>void (*)(const v8::WeakCallbackInfo&lt;Nan::ObjectWrap&gt;&amp;)</b>’} to ‘<b>Callback</b>’ {aka ‘<b>void (*)(const v8::WeakCallbackInfo&lt;void&gt;&amp;)</b>’} [<font color="#D33682"><b>-Wcast-function-type</b></font>]
  SOLINK_MODULE(target) Release/obj.target/segfault-handler.node
  COPY Release/segfault-handler.node
make: Saindo do diretório &apos;/home/fabio/Documentos/git/gateway/node_modules/segfault-handler/build&apos;

&gt; optipng-bin@7.0.0 postinstall /home/fabio/Documentos/git/gateway/node_modules/optipng-bin
&gt; node lib/install.js

<font color="#859900">  ✔</font> optipng pre-build test passed successfully

&gt; jpegtran-bin@5.0.2 postinstall /home/fabio/Documentos/git/gateway/node_modules/jpegtran-bin
&gt; node lib/install.js

<font color="#859900">  ✔</font> jpegtran pre-build test passed successfully

&gt; gifsicle@5.1.0 postinstall /home/fabio/Documentos/git/gateway/node_modules/gifsicle
&gt; node lib/install.js

<font color="#B58900">  ⚠</font> Response code 404 (Not Found)
<font color="#B58900">  ⚠</font> gifsicle pre-build test failed
<font color="#2AA198">  ℹ</font> compiling from source
<font color="#859900">  ✔</font> gifsicle built successfully

&gt; core-js@3.9.1 postinstall /home/fabio/Documentos/git/gateway/node_modules/core-js
&gt; node -e &quot;try{require(&apos;./postinstall&apos;)}catch(e){}&quot;

<font color="#93A1A1">Thank you for using core-js (</font><font color="#839496"> https://github.com/zloirock/core-js </font><font color="#93A1A1">) for polyfilling JavaScript standard library!</font>

<font color="#93A1A1">The project needs your help! Please consider supporting of core-js on Open Collective or Patreon: </font>
<font color="#93A1A1">&gt;</font><font color="#839496"> https://opencollective.com/core-js </font>
<font color="#93A1A1">&gt;</font><font color="#839496"> https://www.patreon.com/zloirock </font>

<font color="#93A1A1">Also, the author of core-js (</font><font color="#839496"> https://github.com/zloirock </font><font color="#93A1A1">) is looking for a good job -)</font>


&gt; core-js@2.6.12 postinstall /home/fabio/Documentos/git/gateway/node_modules/@babel/polyfill/node_modules/core-js
&gt; node -e &quot;try{require(&apos;./postinstall&apos;)}catch(e){}&quot;

added 2112 packages in 41.302s
<font color="#859900"><b>fabio@fabio-13Z940-G-BK71P1</b></font>:<font color="#268BD2"><b>~/Documentos/git/gateway</b></font>$ npm start

&gt; webthings-gateway@1.0.0 start /home/fabio/Documentos/git/gateway
&gt; npm run build &amp;&amp; node build/app.js


&gt; webthings-gateway@1.0.0 build /home/fabio/Documentos/git/gateway
&gt; rm -rf build &amp;&amp; cp -rL src build &amp;&amp; find build -name &apos;*.ts&apos; -delete &amp;&amp; tsc -p . &amp;&amp; webpack

Browserslist: caniuse-lite is outdated. Please run:
npx browserslist@latest --update-db

Why you should do it regularly:
https://github.com/browserslist/browserslist#browsers-data-updating
assets by path <font color="#859900"><b>images/</b></font> 151 KiB 120 assets
assets by path <font color="#859900"><b>fluent/</b></font> 680 KiB 35 assets
assets by path <font color="#859900"><b>../</b></font> 56.1 KiB 34 assets
assets by path <font color="#859900"><b>css/</b></font> 96.3 KiB 23 assets
assets by path <font color="#859900"><b>fonts/</b></font> 677 KiB
  assets by path <font color="#859900"><b>fonts/*.woff</b></font> 407 KiB 6 assets
  assets by path <font color="#859900"><b>fonts/*.woff2</b></font> 270 KiB 6 assets
assets by path <font color="#859900"><b>bundle/</b></font> 2.68 MiB
  assets by path <font color="#859900"><b>bundle/*.js</b></font> 2.59 MiB 2 assets
  assets by chunk 83.2 KiB (name: style) 2 assets
  asset <font color="#859900"><b>bundle/24b63530c3891e501ac0-buildCss</b></font> 5.62 KiB <font color="#859900"><b>[emitted]</b></font> <font color="#859900"><b>[immutable]</b></font> (name: buildCss)
asset <font color="#859900"><b>index.html</b></font> 23.9 KiB <font color="#859900"><b>[emitted]</b></font>
asset <font color="#859900"><b>signup/index.html</b></font> 1.39 KiB <font color="#859900"><b>[emitted]</b></font>
asset <font color="#859900"><b>login/index.html</b></font> 1.2 KiB <font color="#859900"><b>[emitted]</b></font>
asset <font color="#859900"><b>app.webmanifest</b></font> 1.05 KiB <font color="#859900"><b>[emitted]</b></font> [from: static/app.webmanifest] <font color="#859900"><b>[copied]</b></font>
runtime modules 9.77 KiB 34 modules
orphan modules 4.14 KiB <font color="#B58900"><b>[orphan]</b></font> 3 modules
modules by path <b>./node_modules/</b> 2.4 MiB (javascript) 260 bytes (css/mini-extract)
  javascript modules 2.39 MiB 418 modules
  json modules 3.07 KiB
    <b>./node_modules/ajv/dist/refs/json-schema-draft-07.json</b> 2.72 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
    <b>./node_modules/ajv/dist/refs/data.json</b> 360 bytes <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  css ./node_modules/css-loader/dist/cjs.js??ruleSet[1].rules[2].use[1]!<b>./node_modules/mobile-drag-drop/default.css</b> 260 bytes <font color="#B58900"><b>[code generated]</b></font>
modules by path <b>./static/</b> 763 KiB (javascript) 81.3 KiB (css/mini-extract)
  modules by path <b>./static/js/</b> 762 KiB 189 modules
  modules by path <b>./static/css/*.css</b> 750 bytes (javascript) 81.3 KiB (css/mini-extract)
    cacheable modules 750 bytes 15 modules
    css modules 81.3 KiB 15 modules
<b>fs (ignored)</b> 15 bytes <font color="#B58900"><b>[optional]</b></font> <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>

<font color="#B58900"><b>WARNING</b></font> in <b>asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).</b>
<b>This can impact web performance.</b>
<b>Assets: </b>
<b>  bundle/45c899104dac777053a5-app.js (1.1 MiB)</b>
<b>  bundle/ce1ae6c4c6d330bb4a6c-local-token.js (950 KiB)</b>

<font color="#B58900"><b>WARNING</b></font> in <b>entrypoint size limit: The following entrypoint(s) combined asset size exceeds the recommended limit (244 KiB). This can impact web performance.</b>
<b>Entrypoints:</b>
<b>  app.js (1.1 MiB)</b>
<b>      bundle/45c899104dac777053a5-app.js</b>
<b>  local-token.js (950 KiB)</b>
<b>      bundle/ce1ae6c4c6d330bb4a6c-local-token.js</b>


<font color="#B58900"><b>WARNING</b></font> in <b>webpack performance recommendations: </b>
<b>You can limit the size of your bundles by using import() or require.ensure to lazy load some parts of your application.</b>
<b>For more info visit https://webpack.js.org/guides/code-splitting/</b>

webpack 5.24.2 compiled with <font color="#B58900"><b>3 warnings</b></font> in 68000 ms

asset <font color="#859900"><b>service-worker.js</b></font> 42.8 KiB <font color="#859900"><b>[emitted]</b></font> <font color="#859900"><b>[minimized]</b></font> (name: service-worker.js)
runtime modules 221 bytes 1 module
modules by path <b>./node_modules/core-js/internals/*.js</b> 63 KiB 95 modules
modules by path <b>./node_modules/core-js/modules/*.js</b> 61.9 KiB
  <b>./node_modules/core-js/modules/es.array.iterator.js</b> 2.1 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/web.dom-collections.iterator.js</b> 1.53 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/es.promise.js</b> 13.2 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/es.array.includes.js</b> 559 bytes <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/web.url.js</b> 31.9 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/es.string.iterator.js</b> 1.01 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
  <b>./node_modules/core-js/modules/web.url-search-params.js</b> 11.6 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
<b>./static/service-worker.js</b> 2.45 KiB <font color="#B58900"><b>[built]</b></font> <font color="#B58900"><b>[code generated]</b></font>
webpack 5.24.2 compiled <font color="#859900"><b>successfully</b></font> in 21933 ms
Creating database: /home/fabio/.webthings/config/db.sqlite3
<font color="#9F9B8E">2021-08-13 11:19:31.440 INFO   : Creating database: /home/fabio/.webthings/log/logs.sqlite3</font>
<font color="#9F9B8E">2021-08-13 11:19:31.512 INFO   : HTTP server listening on port 8080</font>
<font color="#EEE8D5">2021-08-13 11:19:31.594 DEBUG  : Ignoring https://raw.githubusercontent.com/WebThingsIO/gateway-addon-ipc-schema/master/schema.json because it has no messageType</font>
<font color="#EEE8D5">2021-08-13 11:19:32.109 DEBUG  : Ignoring https://raw.githubusercontent.com/WebThingsIO/gateway-addon-ipc-schema/master/messages/definitions.json because it has no messageType</font>
<font color="#9F9B8E">2021-08-13 11:19:43.112 INFO   : Checking for add-on updates...</font>
<font color="#9F9B8E">2021-08-13 11:19:45.889 INFO   : Finished updating add-ons</font>


</pre>

Leva uns até atualizar tudo e conseguir executar. Depois disso é possível acessar o gateway com um navegador através da URL `http://localhost:8080`

![Captura da tela do navegador](Captura%20de%20tela%20de%202021-08-13%2011-22-06.png)

Esta seção cobre os passos 1 a 4 de https://webthings.io/docs/gateway-getting-started-guide.html.

### Construir um dispositivo

#### Materiais e ferramentas

1. NodeMCU-ESP8266 ou similar;
2. LED, resistor 100ohm e protoboard (podem não ser necessários, ver texto)
3. IDE do Arduino
   - biblioteca para placa ESP8266
   - bibliotecas Webthing-arduino, Arduino JSON, ESPAsyncTCP e ESPAsyncWebServer

#### Montagem
   
A leitura da referência: https://hacks.mozilla.org/2018/04/making-a-web-thing-on-the-esp8266/, leva a crer que é altamente provavel que um dispositivo construído com NodeESP8266 ou similar e um LED possa ser programado com as instruções fornecidas e funcione adequadamente. [Alguma informação sobre ESP8266 é apresentada no repositório da disciplina Computação Física e Aplicações](https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP/ESP8266).

Há modelos de Node-ESP8266 que tem ao menos um LED embutido, o que elimina a montagem de circuito adicional. Por exemplo o usado neste [blog externo](https://www.fernandok.com/2017/10/esp8266-blink-led-com-botao.html), ou o [WittyBoard](https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP/ESP8266#wittyboard), que é o componente que escolhi usar.

Usa-se a IDE do Arduino para programar o Node8266. Para isso, a IDE precisa ser configurada (baixar biblioteca da placa). As instruções são fáceis e são fáceis de encontrar. Quando fiz isso, há alguns anos, [deixei as instruções anotadas aqui](https://github.com/FNakano/CFA/tree/master/componentes/controladores/ESP#configurar-arduinoide-para-programar-o-esp8266-ou-o-esp32).

Algumas outras bibliotecas devem ser instaladas. Em geral, faço isso do final para o começo, procurando e instalando as dependências, que são informadas nos erros de compilação, à medida que os erros ocorrem.

As bibliotecas que precisei são Webthing-arduino, Arduino JSON, ESPAsyncTCP e ESPAsyncWebServer. As duas primeiras são instaladas através do gerenciador de bibliotecas da IDE do Arduino. As duas últimas são instaladas através de arquivo .ZIP. [Esta referência mostra de onde baixar os arquivos](https://reacoda.gitbook.io/molemi-iot/introducing-the-nodemcu/display-the-dht11-sensor-reading-on-a-web-server-using-nodemcu./installing-dht-library-on-the-esp8266/installing-the-asynchronous-web-server-library).

[Captura de tela - Inclusão de WebThing-Arduino](Captura%20de%20tela%20de%202021-08-12%2019-15-48.png)


[Captura de tela - Inclusão de Arduino JSON](Captura%20de%20tela%20de%202021-08-12%2019-49-45.png)


A biblioteca Webthing-Arduino traz o exemplo `LEDLamp`, que é o exemplo usado no tutorial, embora não seja mencionado. Além de ajustar SSID e senha do wifi, como mostrado no tutorial, tive de ajustar alguns pontos do ajuste do brilho do LED. Acredito que a placa ESP8266 usada no tutorial não é Node, o que torna o programa publicado específico para a placa usada.

[Código-fonte do programa do dispositivo](LEDLamp-FN-2021-08-13.ino)

Em relação ao exemplo, os pontos modificados foram:

Inserir ssid e senha do wifi ao qual o Node deve se conectar

```c
const char *ssid = ".............";
const char *password = "..........";

```


O LED do WittyBoard está conectado no pino 12.
```c
// #if defined(LED_BUILTIN)
// const int lampPin = LED_BUILTIN;
// #else
const int lampPin = 12; // LED verde do Wittyboard
// #endif
```

Na placa usada no tutorial o brilho do LED é inversamente proporcional ao valor enviado para o pino e a saída "analógica" aceita valores no intervalo [0:255] por isso o autor fez o mapeamento dessa forma. No WittyBoard o brilho é diretamente proporcional e o intervalo é [0:1023]. Por isso algumas linhas foram comentadas e `analogWrite(lampPin, level*10);` foi acrescentada. Desta forma, o percentual vai de [0:100] e o brilho vai de [0:1000].

```c
void loop(void) {
  adapter->update();
  bool on = lampOn.getValue().boolean;
  if (on) {
//    int level = map(lampLevel.getValue().number, 0, 100, 255, 0);
    int level = lampLevel.getValue().integer; // acredito que o tipo de dados number seja float ou double. https://github.com/WebThingsIO/webthing-arduino/blob/master/Thing.h
    analogWrite(lampPin, level*10);
    //Serial.print("..");
    //Serial.println (level);
  } else {
    analogWrite(lampPin, 0); // na minha placa, apagado é zero.
  }

  if (lastOn != on) {
    lastOn = on;
  }
  //Serial.println (on);
}
```

Depois de compilar e enviar o programa para o Node, o monitor serial exibe a mensagem apresentada na captura de tela.

|[Monitor Serial](Captura%20de%20tela%20de%202021-08-13%2012-07-34.png)


### Incluir o dispositivo no gateway

https://webthings.io/docs/gateway-user-guide.html

https://webthings.io/docs/gateway-getting-started-guide.html

A partir da seção 5 de https://webthings.io/docs/gateway-getting-started-guide.html, configura-se o gateway para acesso pela Internet.

Seção 5: fazendo o que o documento indica, é criado no servidor webthings.io um subdomínio (site) através do qual a comunicação através da Internet aberta é encaminhada para o gateway. Um e-mail (provavelmente para comunicação com o administrador do gateway e, talvez, para alguma questão de legislação)

Seção 6: cria no gateway o primeiro usuário (uma espécie de administrador do sistema).

A inclusão do dispositivo é feita a partir da seção III de https://webthings.io/docs/gateway-user-guide.html

Seção III: Acrescentar o add-on Web Thing, que contém informação sobre como comunicar com dispositivos do tipo que foi construído e saltar para a sub-seção [Scan For and Add Smart Devices](https://webthings.io/docs/gateway-user-guide.html#scan-for-and-add-smart-devices)

A busca pelo dispositivo deve retornar `My Lamp`. Acrescente o dispositivo e o controle, como mostrado no [vídeo]().

## Conclusão e discussão


Na opinião do autor, o pacote de software Web Things Gateway provê:

- Um servidor que é executado no sistema do usuário, através do qual o usuário configura o servidor e, através dele,  encontra, monitora e controla os dispositivos no sistema. No vocabulário de Web Things, é um *gateway* e não é acessível diretamente pela Internet;
- Um servidor proxy - https://www.webthings.io. O proxy é acessível pela Internet e encaminha requisições ao gateway, servindo como intermediário entre a rede pública e o sistema do usuário;
- Instruções para configurar o gateway, o proxy, conectar a dispositivos compatíveis e construir dispositivos compatíveis.



## Referências

