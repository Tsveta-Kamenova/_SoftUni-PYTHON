class Websites:
    def __init__(self, h, d, q):
        self.h = h
        self.d = d
        self.q = q


list_websites = []
list_queries = []

data_input = input().split(" | ")

while len(data_input) != 1:
    host = data_input[0]
    domain = data_input[1]
    if len(data_input) == 3:
        list_queries = data_input[2].split(",")
    else:
        list_queries = []

    current_website = Websites(host, domain, list_queries)
    list_websites.append(current_website)

    data_input = input().split(" | ")

for i in range(len(list_websites)):
    if not list_websites[i].q:
        print(f"https://www.{list_websites[i].h}.{list_websites[i].d}")
    else:
        print(f"https://www.{list_websites[i].h}.{list_websites[i].d}/query?=[", end="")
        print(*list_websites[i].q, sep="]&[", end="")
        print("]")
