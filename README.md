# zabbix_aws_terminate

- Para adicionar o instance-id do ec2 no description do zabbix, execute o comando:
aws lambda invoke --invocation-type RequestResponse --function-name zabbix_terminate --region sa-east-1 --payload '{"action":"update_description", "description":"'$(/opt/aws/bin/ec2-metadata -i | cut -d' ' -f2)'", "host":"'$NOVOHOSTNAME'"}' /dev/null

- A variavel $NOVOHOSTNAME, deve ser o nome da maquina cadastrada no zabbix
