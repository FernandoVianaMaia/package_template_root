import requests


class HTTPClient:
    """
    A simple HTTP client that retrieves data from a web service using the requests library.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initializes a new instance of the HTTPClient class.
        :param base_url: The base URL of the web service.
        """
        self.base_url = base_url
        self.session = requests.Session()

    def retrieve_data(self, resource_path: str) -> dict:
        """
        Retrieves data from the specified resource path and returns it as a dictionary.
        :param resource_path: The path of the resource to retrieve.
        :return: A dictionary containing the retrieved data.
        """
        url = f"{self.base_url}/{resource_path}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    base_url = "https://myservice"
    http_client = HTTPClient(base_url)
 
    resource_path = "get_something/123"
    data = http_client.retrieve_data(resource_path)
    print(data)
