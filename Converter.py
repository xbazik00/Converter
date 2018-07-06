import getopt, sys, json
import requests

class MissingCurrencyOrAmount(Exception):
    pass

class Converter():
    def __init__(self):
        with open('currencies.json') as f:
            self.data = json.load(f)

    def _convert_to_all(self, in_curr, amount):
        self._get_rates({'base':in_curr})

    def _get_rates(self, pars):
        r = requests.get("https://ratesapi.io/api/latest", params = pars)
        print(r.json())


    def convert(self, in_curr, out_curr, amount):
        if amount is None or in_curr is None:
            raise MissingCurrencyOrAmount("Currency or amount was not provided!")
        elif out_curr is None:
            self._convert_to_all(in_curr, amount)
        else:
            pass


    def _parse_currs(self,curr):
        for _, y in self.data.items():
            if 'currencySymbol' in y.keys():
                pass
                #print(y['currencySymbol'])

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:i:o:", ["amount=", "input_currency=", "output_currency="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)
    amount = None
    input_curr = None
    output_curr = None
    for o, a in opts:
        if o in ("-a", "--amount"):
            amount = float(a)
        elif o in ("-i", "--input_currency"):
            input_curr = a
        elif o in ("-o", "--output_currency"):
            output_curr = a
        else:
            assert False, "unhandled option"
    conv = Converter()
    try:
        conv.convert(input_curr, output_curr, amount)    
    except MissingCurrencyOrAmount as identifier:
        print(identifier)
    

if __name__ == '__main__':
    main()