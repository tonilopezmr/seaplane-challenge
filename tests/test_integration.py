from flask import json

def test_app_returns_shortests_path_given_start_target_and_correct_dictionary(client):
    response = client.get("/?start=an&target=men&dic=ban,bean,ben,hen,mean,mesn,men")
    result = json.loads(response.data)
        
    assert result == ["an", "ban", "ben", "men"]

def test_app_returns_error_when_start_is_missing(client):
    response = client.get("/?target=men&dic=ban,bean,ben,hen,mean,mesn,men")
    result = json.loads(response.data)
        
    assert result == {"error": "start parameter is missing"}


def test_app_returns_error_when_target_is_missing(client):
    response = client.get("/?start=an&dic=ban,bean,ben,hen,mean,mesn,men")
    result = json.loads(response.data)
        
    assert result == {"error": "target parameter is missing"}

def test_app_returns_error_when_dictionary_is_missing(client):
    response = client.get("/?start=an&target=men")
    result = json.loads(response.data)
        
    assert result == {"error": "dictionary parameter is missing"}

def test_app_returns_error_when_dictionary_is_empty(client):
    response = client.get("/?start=an&target=men&dic=")
    result = json.loads(response.data)
        
    assert result == {"error": "dictionary parameter is missing"}