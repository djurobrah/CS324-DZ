#!/usr/bin/perl -w
use warnings;

@a = ("a", "b", "c", "d", "e");
@b = ( 1,   2,   3,   4 );

print("\n Prvi niz: \n");
foreach my $x (@a)
{
  print("$x, ");
}
print("\n Drugi niz: \n");
foreach my $x (@b)
{
  print("$x, ");
}

print("\n Zipovani niz: \n");
if ((scalar @a) > (scalar @b))
{
  for (my $j = 0; $j < ((scalar @a) - (scalar @b)); $j++)
  {
    pop @a;
  }
}
if ((scalar @a) < (scalar @b))
{
  for (my $k = 0; $k < ((scalar @b) - (scalar @a)); $k++)
  {
    pop @b;
  }
}

@result = zipuj(\@a, \@b);
print(@result);

sub zipuj
{
  @temp = ();
	my(@c) = @{$_[0]};
  my(@d) = @{$_[1]};
  for (my $i = 0; $i < scalar @c; $i++)
  {
      push @temp, $c[$i];
      push @temp, $d[$i];
  }
	return @temp;
}
