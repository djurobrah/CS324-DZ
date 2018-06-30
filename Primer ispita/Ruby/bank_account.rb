class BankAccount
  #class variable
  @@num_of_clients = 0

  #instance variables
  attr_accessor :first_name, :last_name, :balance

  #inicijalizacija
  def initialize(first_name, last_name)
    @first_name = first_name
    @last_name = last_name
    @balance = 320
    @@num_of_clients = @@num_of_clients + 1
  end

  #stampanje, instance method
  def to_s
    puts "First name: #{first_name}, " +
             "Last name: #{last_name}, " +
             "Balance: #{balance}."
  end

  #instance method
  def withdraw(x)
    if (balance - x < 0)
      puts "Nemate dovoljno novca na računu"
    else
      @balance = balance - x
    end
  end

  #instance method
  def deposit(x)
    @balance = balance + x
  end

  #class method
  def self.clients_info
    puts "Number of BankAccounts: #{@@num_of_clients}"
  end
  
end

b1 = BankAccount.new("Pera", "Peric")
BankAccount.clients_info
b2 = BankAccount.new("Djurica", "Djuricic")
BankAccount.clients_info

b1.withdraw(20)
b2.deposit(20)

b1.to_s
b2.to_s