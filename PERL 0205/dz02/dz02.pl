#!/usr/bin/perl -w
use warnings;
#ovaj program stampa sve unesene vrednosti

print "Unesite vrednost:\n";
$input = <STDIN>;
chomp($input);
if($input eq "\n")
{
	print "Niste uneli vrednost...\n";
}
else
{
	@lista = ("$input");
	while(!($input eq "\n"))
	{
		print "Unesite vrednost:\n";
		$input = <STDIN>;
		if($input eq "\n")
		{
			last;
		}
		chomp($input);
		push @lista, "$input";
	}
	print "Niz unesenih vrednosti:\n";
	foreach(@lista)
	{
		print "'$_', ";
	}
}
system("pause");
