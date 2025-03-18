import json
import os

class SingletonMeta(type):
    """ A metaclass for Singleton pattern. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class QuerySingleton(metaclass=SingletonMeta):
    """ Singleton class to store and persist a query across programs. """
    _query_file = "/home/niteshchauhan/PycharmProjects/coldEmailGenerator/app/query_store.json"  # File to store query persistently

    def __init__(self):
        self._query = self._load_query()

    def _load_query(self):
        """ Load query from file if it exists, else return default value. """
        if os.path.exists(self._query_file):
            with open(self._query_file, "r") as f:
                return json.load(f).get("query", "")
        return ""

    def _save_query(self):
        """ Save query to file to persist across executions. """
        with open(self._query_file, "w") as f:
            json.dump({"query": self._query}, f)

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
        self._save_query()

# Example Usage in Different Programs
if __name__ == "__main__":
    instance1 = QuerySingleton()
    print("Current Query:", instance1.query)  # Reads the existing query
    instance1.query = "python"  # Modifies the query
