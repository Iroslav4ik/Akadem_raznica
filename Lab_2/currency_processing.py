import xml.etree.ElementTree as ET


def parse_currency():
    tree = ET.parse('currency.xml')
    root = tree.getroot()

    currency_dict = {}
    for valute in root.findall('Valute'):
        num_code = valute.find('NumCode').text
        char_code = valute.find('CharCode').text
        currency_dict[num_code] = char_code

    with open('currency_dict.txt', 'w') as f:
        for num, char in currency_dict.items():
            f.write(f"{num}: {char}\n")


if __name__ == "__main__":
    parse_currency()