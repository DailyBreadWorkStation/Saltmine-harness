import json

def read_json():
  with open("/home/doughfactory/Saltmine/config.json") as uConfig:
      readjson = json.load(uConfig)
  return readjson

def read_create_series_json():
  with open("/home/doughfactory/Saltmine/createSeries.json") as uConfig:
      readjson = json.load(uConfig)
  return readjson