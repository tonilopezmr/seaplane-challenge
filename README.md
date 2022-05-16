# seaplane-challenge

API to get the shortests path between two words that are included in a given dictionary.

# Run 

Activate your venv and install the requirements.txt

```
pip install -r requirements.txt
flask run
```

# Run tests

```
chmod 557 tests.sh
./tests.sh
```

or you can run unit tests:

```
cd tests
python3 test_word_ladder.py
```

and integration tests

```
cd tests
pytest
```

# How it works

Once you run `flask run`, you have to open a browser or make a GET Request to `https://localhost:5000` with the next three parameters:

`start` The start word
`target` The end word 
`dictionary` The dictionary  with the intermediate words

Example: 

```
http://localhost:5000/?start=an&target=men&dic=ban,bean,ben,hen,mean,mesn,men
```

Will return 

```
["an", "ban", "ben", "men"]
```