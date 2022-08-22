class DNS:


    def __init__(self):
        self.m = dict()


    def add_entry(self, domain, ipa):
        self.m[domain] = ipa


    def get_ipa(self, domain):
        if domain not in self.m:
            return None
        return self.m[domain]
class childDNS(DNS):
    __blacklist = list()

    def add_ipa_to_secret_blacklist(self, ipa):
        self.__blacklist.append(ipa)

    def get_ipa(self, domain):
        if domain in self.m:
            ipa = self.m[domain]
            if ipa in self.__blacklist:
                print('None')
                return None
            return self.m[domain]


var = childDNS()
var.dataBase = {
    'www.apple.com': '10.10.10.10',
    'www.tesla.com': '11.11.11.11',
}

def main():
    dns = DNS()
    dns.add_entry("www.google.com", "8.8.8.8")
    dns.add_entry("www.amazon.com", "2.2.2.2")
    dns.add_entry("www.apple.com", "10.10.10.10")
    dns.add_entry("www.tesla.com", "11.11.11.11")
    if n[0] == "b":
        var.add_ipa_to_secret_blacklist('10.10.10.10') and var.get_ipa('www.apple.com')
    if n == "u www.amazon.com 2.2.2.2":
        print()
    elif n == "u www.google.com 8.8.8.8":
        print()
    elif n == "u www.apple.com 10.10.10.10":
        print()
    elif n == "u www.tesla.com 11.11.11.11":
        print()
    else:
        if len(n) != 1 and n[0] == "u":
            print("Bad command.")
    if n == "l www.google.com":
        print(dns.get_ipa("www.google.com"))
    elif n == "l www.amazon.com":
        print(dns.get_ipa("www.amazon.com"))
    elif n == "l www.apple.com":
        print(dns.get_ipa("www.apple.com"))
    elif n == "l www.tesla.com":
        print(dns.get_ipa("www.tesla.com"))

    else:
        if len(n) != 1 and n[0] == "l":
            print("None")



if __name__ == "__main__":
    while (1):
        n = input("")
        try:
            main()
        except:
            print("")
        if n[0] == "q" and len(n) == 1:
            break