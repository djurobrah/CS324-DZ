#!/usr/bin/perl -w
use warnings;

#stampanje kvadrata brojeva (range operator)
@brojevi = (1..10);
print("\n Niz kvadrata brojeva od 1 do 10: \n");
foreach $broj (@brojevi)
{
	print("$broj" * "$broj".", ");
	#print("sta");
}

#stampanje kvadrata brojeva (shift funkcija)
print("\n Niz kvadrata brojeva od 1 do 10 (via shift): \n");
@array = (1..10);
while($element = shift(@array))
{
	print("$element" * "$element".", ");
}


#obrtanje unosa korisnika
print("\n Unesite recenicu za obradu: \n");
$input = <STDIN>;
chomp($input);
$result = reverse $input;
print("Obrnuta recenica :\n $result \n");
system("pause");
