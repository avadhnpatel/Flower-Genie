# flower_genie
Flower Genie is a survey tool used to help customers decide on a certain floral arrangement or flowers at a local flower shop based on their answers to a short survey. 

## setup
1. Create python env
2. execute this in terminal: `pip install flask flask_sqlalchemy pymysql pyyaml`
3. Make sure you are in the flower_genie directory
4. execute this in terminal: `export FLASK_APP=app`
5. next execute: `export FLASK_DEBUG=1`
6. Go to GCP instance and go to "Connections". In connections add your IP address to authorized networks. (Search "whats my IP address" on google)
7. Finally run `flask run` to deploy the site locally
