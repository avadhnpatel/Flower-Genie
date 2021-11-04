# flower_genie
Flower arrangement recommendation system for local flower shop

## setup
1. Creat python env
2. execute this in terminal: '''
pip install flask flask_sqlalchemy pymysql pyyaml
'''
4. Make sure you are in the flower_genie directory
5. execute this in terminal: export FLASK_APP=app
6. next execute: export FLASK_DEBUG=1
7. Go to GCP instance and go to "Connections". In connections add your IP address to authorized networks. (Search "whats my IP address" on google)
8. Finally run flask_run to deploy the site locally
