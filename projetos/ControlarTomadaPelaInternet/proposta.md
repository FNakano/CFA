<!--- 1. Título --->

# Controlar Tomada Pela Internet - Proposta

## Objetivo geral (O que fazer)

Controlar Tomada Pela Internet

## Motivação (Por que fazer: Relevância, experiência, conhecimento acumulado, motivação pessoal,...)

Nos projetos que vi sendo desenvolvidos no curso percebi grande dificuldade em controlar (a energia de) uma tomada residencial.

Sem grandes divagações sobre o tema, são necessários alguns cuidados para evitar choques de 110 ou 220V que são, no mínimo, doloridos.

Pretendo fazer isso com ESP32, que é alimentado a 3,3V. O shield de relé mais comum é alimentado a 5V. O projeto combina 3.3V com 5V com 110/220V.

Existe uma variedade de fontes com espelhos e caixas prontas que poderia servir como caixa e fonte de alimentação para este projeto:

<https://produto.mercadolivre.com.br/MLB-1535420121-carregador-turbo-tomada-parede-2-usb-3a-5v-bivolt-master-23-_JM?matt_tool=11528875&matt_word=&matt_source=google&matt_campaign_id=6542939187&matt_ad_group_id=77294333743&matt_match_type=&matt_network=u&matt_device=c&matt_creative=385098657789&matt_keyword=&matt_ad_position=&matt_ad_type=&matt_merchant_id=160952330&matt_product_id=MLB1535420121&matt_product_partition_id=358100205965&matt_target_id=pla-358100205965&gclid=Cj0KCQjw8fr7BRDSARIsAK0Qqr5pQglXTUnztV_b7lwh74z4lDgqg45SsxnleQeNJiM4HBOEVyZn4RYaAioBEALw_wcB>

<https://www.amazon.com.br/Multiplicador-Tomadas-Bivolt-Elg-PWC-X4U/dp/B076TGXZ6Y/ref=asc_df_B076TGXZ6Y/?tag=googleshopp00-20&linkCode=df0&hvadid=379728510613&hvpos=&hvnetw=g&hvrand=7226729273556580368&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001736&hvtargid=pla-834081918194&psc=1>

<https://produto.mercadolivre.com.br/MLB-908074022-modulo-tomada-4x4-master-28-com-usb-_JM?matt_tool=11528875&matt_word=&matt_source=google&matt_campaign_id=6542939187&matt_ad_group_id=77294333743&matt_match_type=&matt_network=u&matt_device=c&matt_creative=385098657789&matt_keyword=&matt_ad_position=&matt_ad_type=&matt_merchant_id=238716652&matt_product_id=MLB908074022&matt_product_partition_id=358100205965&matt_target_id=pla-358100205965&gclid=Cj0KCQjw8fr7BRDSARIsAK0Qqr7xgVmjYXzwCI_qUohHLkNViThHli0euAPd00pSJO8cDQrIY5fS6ZoaAijHEALw_wcB>

Deixar este projeto como exemplo provavelmente atenderá as dificuldades encontradas pelos alunos e atenderá também a demanda de colaboradores sobre atuadores IoT.

## Caso seja parte de uma sequência/cadeia/rede, quais relações com as outras atividades/elos são conhecidas.

(Navegador web) -> Tomada controlada -> eletrodoméstico controlado.
semantic web    -------^


## Referências

