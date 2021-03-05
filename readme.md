#### Reset Server

```shell script
ssh  -o StrictHostKeyChecking=no -i ruponline -p 2209 aakashlabs@202.166.194.143 "sudo systemctl restart gunicorn.service; sudo systemctl daemon-reload;"
````
