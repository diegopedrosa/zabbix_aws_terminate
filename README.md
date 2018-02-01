# zabbix_aws_terminate

### Esse projeto é PoC funcional para automatizar a remoção das maquinas ec2 do Zabbix:

Abaixo esta um passo a passo manual (por enquanto).

> 1. Importar para o lambda em conjunto com as dependencias, os arquivos zabbix.py e o lambda_function.py;
> 2. Crie as chaves kms e de permissão para o lambda poder utilizar ela através do IAM;
> 3. Adicione o Lambda na VPC e crie o endpoint do kms para poder ser utilizado internamente;
> 4. Adicione as variaveis de ambiente "username", "password" e url no lambda;
> 5. Utiliza a chave do kms que você criou para criptografar as variaveis de ambiente username e password;
> 6. Garanta que a rede do lambda possui acesso liberado ao Zabbix através do Security Group e ACL;
> 7. As maquinas ec2 devem possuir o aws cli previamente configurados e com acesso para executar o lambda;
> 8. Ao criar as maquinas na EC2, adicione o comando abaixo no user data;
> - aws lambda invoke --invocation-type RequestResponse --function-name zabbix_terminate --region sa-east-1 --payload '{"action":"update_description", "description":"'$(/opt/aws/bin/ec2-metadata -i | cut -d' ' -f2)'", "host":"'$NOVOHOSTNAME'"}' /dev/null
>    - OBS: A variavel $NOVOHOSTNAME, deve ser o nome da maquina cadastrada no zabbix.
> 9. Criar uma nova regra no CloudWatch, baseada em evento para executar o lambda utilizando como entrada o "Matched event".


