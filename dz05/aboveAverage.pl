#!/usr/bin/perl -w
use warnings;

my @array = (1..10);
my $avrg = avrg(@array);

print("\n Brojevi veci od " . $avrg . " su: \n");
foreach(@array)
{
	if ($_ > $avrg)
  {
		print("$_, ");
	}
}

sub avrg
{
	my $sum = 0;
	foreach(@_)
  {
		$sum += $_;
	}
	return $sum / scalar @_;
  print("$avrg");
}
