
body_settings_vacinei = {
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "email": {
        "type": "keyword"
      },
      "location": {
          "type": "geo_point"
      },
      "vacina":
        {
          "type": "keyword"
        },
        "date":
        {
          "type":   "date",
          "format": "date_optional_time"
        },
        "data_vacinacao":
        {
          "type":   "date"
        },
      "idade":
        {
          "type": "integer"
        },
      "desperdicio":
        {
          "type": "boolean"
        }
    }
  }
}
