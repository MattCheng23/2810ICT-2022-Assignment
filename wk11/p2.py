class DNS:

    def __init__(self):
        self.dataBase = dict()

    def add_Domain_IPA(self, domain, ipa):
        self.dataBase[domain] = ipa

    def get_ipa(self, domain):
        if domain not in self.dataBase:
            return None
        return self.dataBase[domain]


class childDNS(DNS):
    __blacklist = list()

    def add_ipa_to_secret_blacklist(self, ipa):
        self.__blacklist.append(ipa)

    def get_ipa(self, domain):
        if domain in self.dataBase:
            ipa = self.dataBase[domain]
            if ipa in self.__blacklist:
                print('ipa of ' + str(domain) + " : " + 'does not exist')
                return None
        elif domain not in self.dataBase:
            print('ipa of ' + str(domain) + " : " + 'does not exist')
            return None
        print('ipa of ' + str(domain) + " : " + self.dataBase[domain])
        return self.dataBase[domain]


var = childDNS()
var.dataBase = {
    'www.hi.com': '192.10.1.20',
    'www.hello.com': '192.10.1.30',
    'www.facebook.com': '192.10.1.40',
    'www.world.com': '192.10.1.50',
    'www.hihi.com': '192.10.1.60',
}
var.add_ipa_to_secret_blacklist('192.10.1.50')
var.get_ipa('www.hello.com')
var.get_ipa('www.world.com')

print('another check')
var.add_ipa_to_secret_blacklist('192.10.1.40')
var.get_ipa('www.facebook.com')
var.get_ipa('www.world.com')
var.get_ipa('www.hi.com')


