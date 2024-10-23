from rdflib_neo4j import Neo4jStoreConfig, Neo4jStore, HANDLE_VOCAB_URI_STRATEGY
from rdflib import Graph

def run():
    return None
    neo4j_config_path = 'untracked/Neo4j-Created-2024-10-23.txt'
    def read_and_parse_config(file_path):
        config = {}
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # Strip whitespace and ignore comments
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    # Split key and value
                    key, value = line.split('=', 1)  # Limit split to 1 occurrence
                    config[key.strip()] = value.strip()
                    
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return config

    # Read and parse the configuration
    user_config = read_and_parse_config(neo4j_config_path)
    auth_data = {'uri': user_config['NEO4J_URI'],
            'database': "neo4j",
            'user': user_config['NEO4J_USERNAME'],
            'pwd': user_config['NEO4J_PASSWORD']}

    # Print the configurations for verification
    #for key, value in config.items():
    #    print(f"{key}: {value}")
    
    # Define your custom mappings & store config
    config = Neo4jStoreConfig(auth_data=auth_data,
                          #custom_prefixes=prefixes,
                          handle_vocab_uri_strategy=HANDLE_VOCAB_URI_STRATEGY.IGNORE,
                          batching=True)
    
    # Step 3: Specifying RDF Data Source
    ttl_path = 'gbad/from_draw_io_parser/authority/mapped_LARGE_postprocessed.ttl'

    # Create the RDF Graph, parse & ingest the data to Neo4j, and close the store(If the field
    # batching is set to True in the Neo4jStoreConfig, remember to close the store to prevent the loss
    # of any uncommitted records.)
    neo4j_aura = Graph(store=Neo4jStore(config=config))

    # Calling the parse method will implicitly open the store
    try:
        neo4j_aura.parse(ttl_path, format="ttl")
    except Exception:
        pass
    finally:
        neo4j_aura.close(True)

    return None

if __name__ == "__main__":
    print(run())
