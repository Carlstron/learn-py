"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, name, age): ...


class Client(Pessoa):
    def __init__(self, name, age, account_number, account_type):
        self.name = name
        self.age = age
        if account_type == 'savings':
            self.account_number = create_savings_account(
                account_number, self.name)
        elif account_type == 'current':
            self.account_number = create_current_account(
                account_number, self.name)

        else:
            raise TypeError('Tipo de conta inexistente')


class Bank:
    def __init__(self, agency=1):
        self.agency = agency
        self.clients = {}

    def add_client(self, client):
        self.clients.update({(client.name, client.account_number)})
        return print(f'Adicionando {client.name}')

    def validate_client(self, client):
        if (client.name, client.account_number) in self.clients.items():
            return True
        return False


class Account(ABC):
    def __init__(self, accountnumber, client):
        self.user = client
        self.account_number = accountnumber
        self.total = 0

    def __repr__(self):
        return str(self.account_number)

    def check_account_total(self, client, agency):
        if agency.validate_client(client):
            return print(f'Você possui {self.total} em sua conta')
        return print('Cliente inválido')

    @abstractmethod
    def withdraw(self, account_number, client, amount): ...

    @abstractmethod
    def deposit(self, account_number, client, amount): ...


def create_savings_account(account_number, client):
    account = SavingsAccount(account_number, client)
    return account


def create_current_account(account_number, client):
    account = CurrentAccount(account_number, client)
    return account


class SavingsAccount(Account):
    def __init__(self, accountnumber, client):
        super().__init__(accountnumber, client)

    def withdraw(self, amount, client, agency):
        if agency.validate_client(client):
            self.total -= amount
            return print(f'Você tem {self.total} restando em sua conta')
        return print('Cliente inválido')

    def deposit(self, amount, client, agency):
        if agency.validate_client(client):
            self.total += amount
            return print(f'Você tem {self.total} restando em sua conta')
        return print('Cliente inválido')


class CurrentAccount(Account):
    def __init__(self, accountnumber, client):
        super().__init__(accountnumber, client)

    def withdraw(self, amount):
        if self.total - amount < -1000:
            return print('Você não tem direito a mais saques')
        self.total -= amount
        return print(f'Você tem {self.total} restando em sua conta')

    def deposit(self, amount):
        self.total += amount
        return print(f'Você tem {self.total} em sua conta')


banco_central = Bank(1)
p1 = Client('Bruno', 23, 123, 'savings')
p2 = Client('Bianca', 27, 122, 'current')
c_invalido = Client('Inválido', 0, 121, 'savings')
banco_central.add_client(p1)
banco_central.add_client(p2)
print(banco_central.clients)

p1.account_number.deposit(100, p1, banco_central)
p1.account_number.withdraw(50, p1, banco_central)
p1.account_number.check_account_total(p1, banco_central)
print('\n\n\n\n')

p2.account_number.deposit(100)
p2.account_number.withdraw(1100)
p2.account_number.withdraw(1100)
p2.account_number.check_account_total(p2, banco_central)

print('\n\n')

c_invalido.account_number.deposit(100, c_invalido, banco_central)
