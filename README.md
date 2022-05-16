# seaplane-challenge

API to get the shortests path between two words that are included in a given dictionary.

# Run 

```
flask run
```

# Run tests

```
./tests.sh
```

# How it works

You have to open a browser or make a GET Request to `https://localhost:5000` with the next three parameters:

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