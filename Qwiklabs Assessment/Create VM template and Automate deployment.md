In order to enable hello_cloud.py to run on boot, copy the file hello_cloud.py to the /usr/local/bin/ location.
```
sudo cp hello_cloud.py /usr/local/bin/
```
Also copy hello_cloud.service to the /etc/systemd/system/ location.
```
sudo cp hello_cloud.service /etc/systemd/system
```
Now, use the systemctl command to enable the service hello_cloud.
```
sudo systemctl enable hello_cloud.service
```
