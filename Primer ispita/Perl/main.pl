use Try::Tiny;

@a = ("a", "b", "c", "d", "e");
@b = ( 1,   2,   3,   4 );

@result = recursive(\@a, \@b)
sub recursive
{
  try
  {
    if ((scalar @a) != (scalar @b))
    {
      die "foo";
    }
  }
  catch
  {
      warn "caught error: $_";
  };
  my(@a) = @{$_[0]};
  my(@b) = @{$_[1]};
  if ((scalar @a) != (scalar @b))
  {
    # baci exception
  }

  @temp = ();

  # for (my $i = 0; $i < scalar @c; $i++)
  # {
  #     push @temp, $c[$i];
  #     push @temp, $d[$i];
  # }
	return @temp;
}
