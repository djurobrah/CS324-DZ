#!/usr/bin/perl -w
use warnings;

use lib "lib";
use BankAccount;

print("\n Unesite kolicinu novca za otvaranje racuna: \n");
$start_money = <STDIN>;
chomp($start_money);
my $bank_acc = new BankAccount($start_money); #object creation
print("\n Racun kreiran sa iznosom od:" . $bank_acc->getBalance() . "\n");

print("\n Unesite kolicinu novca za dodavanje na racun: \n");
$deposit_money = <STDIN>;
chomp($deposit_money);
$bank_acc->deposit($deposit_money);
print("\n Trenutno stanje racuna:" . $bank_acc->getBalance() . "\n");

print("\n Unesite kolicinu novca za skidanje sa racuna: \n");
$withdraw_money = <STDIN>;
chomp($withdraw_money);
$bank_acc->withdraw($withdraw_money);
print("\n Trenutno stanje racuna:" . $bank_acc->getBalance() . "\n");
