#!/usr/bin/perl -w
use warnings;

@result = ();

my $filename = 'fajl_za_citanje.txt';
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";

while (my $row = <$fh>)
{
  chomp $row;
  push @result, "$row";
}

while (scalar @result != 0)
{
  my $temp = pop @result;
  print("\n" . $temp . "\n");
}
system("pause");
