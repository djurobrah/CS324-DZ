module Modul

  def nzd(a, b)
    if (a % b) == 0
      b
    else
      nzd(b, a % b)
    end
  end

  def bla(a)
    puts (self*a)
  end

  class Integer
    include Modul
  end
end
#
#
# module ModulNzd
#   def nzd(broj1, broj2)
#     if (broj1 % broj2) == 0
#       broj2
#     else
#       nzd(broj2, broj1 % broj2)
#     end
#   end
#
#   def metoda(rec)
#     if rec.empty? || rec.nil? || rec == " "
#       "Prazno"
#     elsif rec.length <= 5
#       "Kratko"
#
#     elsif rec.length >= 6 && rec.length <= 11
#       "Srednje dugo"
#
#     elsif rec.length >= 12
#       "Dugo"
#
#     else
#       "Greska"
#     end
#   end
#
#   class Integer
#     include ModulNzd
#   end
# end
#
