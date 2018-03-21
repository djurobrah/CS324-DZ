#!/usr/bin/perl -w
use warnings;

%hashmap =
(
  "Djurica" => "Djuricic",
  "Pera" => "Peric",
  "Zika" => "Zikic",
  "Mika" => "Mikic"
);

print("\n Unesite ime osobe cije prezime vas zanima: \n");
$ime = <STDIN>;
chomp($ime);

if (exists $hashmap{"$ime"})
{
    print("Puno ime osobe je: " . "$ime " . "$hashmap{$ime}" . "\n");
}
else
{
    print("\n $ime ne postoji u hashmapi! \n");
}
