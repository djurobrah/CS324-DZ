package BankAccount;
  sub new
  {
    $class = shift;

    $self =
    { #member variables
      balance => shift # ,incase of more variables
    };

    bless $self, $class; #allows referencing the member variables
    return $self; #return the object
  }

  sub setBalance #setter
  {
    my ($self, $new_balance) = @_;
    $self->{balance} = $new_balance if defined;
    return $new_balance;
  }

  sub getBalance #getter
  {
    my($self) = @_;
    return $self->{balance};
  }

  sub deposit
  {
    my ($self, $deposit) = @_;
    $self->{balance} = $self->{balance} + $deposit;
    return $self->{balance};
  }

  sub withdraw
  {
    my ($self, $amount) = @_;
    $self->{balance} = $self->{balance} - $amount;
    return $self->{balance};
  }

1; #all modules return true
