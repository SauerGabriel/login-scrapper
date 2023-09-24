import requests
from bs4 import BeautifulSoup
import re


def get_links(url):
  """
 Return website login list.

  Args:
    url: Website URL.

  Returns:
    Link list.
  """

  links = []

  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  for element in soup.find_all("a"):
    if re.match(r"/(wp-admin|admin)", element["href"]):
      links.append(element["href"])

  return links


def main():
  """
  Main program.
  """

  url = input("Digite o URL do site: ")

  links = get_links(url)

  for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    if soup.find("h1", text="Login"):
      print(f"Login page found: {link}")


if __name__ == "__main__":
  main()
