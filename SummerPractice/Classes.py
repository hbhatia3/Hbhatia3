class mobile:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year


class samsung:
    def __init__(self, SamsungPay, company, model, year):
        mobile.__init__(self, company, model, year)
        self.SamsungPay = SamsungPay


class apple:
    def __init__(self, ApplePay, company, model, year):
        mobile.__init__(self, company, model, year)
        self.ApplePay = ApplePay


S = samsung(True, 'Samsung', 'Galaxy 10', '2018')
print(S.SamsungPay)
print(S.company)
print(S.model)
print(S.year)
