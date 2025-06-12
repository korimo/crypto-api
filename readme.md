
assumptions

windows 11

postgress 12 database on local with 
	database cryptodb 
	username postgres 
	password postgres

run docker-compose up --build
api documentation 
	http://localhost:8000/docs

in doc subdir there is 
	openapi yaml documentation of the API, and 
	yaml test collectio for postman

directory tree
│   .env
│   .gitignore
│   docker-compose.yml
│   docker-compose.yml.bak
│   Dockerfile
│   Dockerfile.bak
│   requirements.txt
│
├───app
│   │   coingecko.py
│   │   crud.py
│   │   database.py
│   │   database.py.old
│   │   main.py
│   │   models.py
│   │   redis_client.py
│   │   schemas.py
│   │
│   └───__pycache__
│           coingecko.cpython-311.pyc
│           crud.cpython-311.pyc
│           database.cpython-311.pyc
│           main.cpython-311.pyc
│           models.cpython-311.pyc
│           redis_client.cpython-311.pyc
│           schemas.cpython-311.pyc
│
└───doc
        crypto_api.zip
        Crypto_API_Postman_Collection.json