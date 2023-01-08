from elasticsearch import Elasticsearch

elastic_connection = Elasticsearch([{'host': 'localhost', 'port': 9200, "scheme": "http"}])

# if elastic_connection.ping():
#     print('Elastic Connect')
# else:
#     print('No elastic')
    # raise 'No Elastic Connection'


def create_index(es_object, index_name='books'):
    created = False

    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "books": {
                "properties": {
                    "title": {
                        "index": "not_analyzed",
                        "type": "text"
                    },
                    "description": {
                        "index": "not_analyzed",
                        "type": "text"
                    },
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index=index_name):
            es_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


# print(f'Elastic index creating: {create_index(elastic_connection)}')
