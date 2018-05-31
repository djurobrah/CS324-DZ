# require_relative "modul"
# class Main
#   extend(Modul)
#
#   Main.new.nzd(10, 2)
#   puts (self.nzd(10, 2))
#
#   def duzina(str)
#     if str.nil? | str.empty?
#       "Prazno"
#     elsif str.length <= 5
#       "Kratko"
#     elsif str.length >= 6 && str.length <= 11
#       "Srednje dugo"
#     else
#       "Dugo"
#     end
#   end
# end

#
# require_relative 'modul'
# class Main
#   extend(ModulNzd)
#   puts(self.nzd(100, 50))
#
#
#
#   puts("Unesi rec")
#   ulaz = STDIN.gets.chop
#   puts(self.metoda(ulaz))
#
# end

class Main
  print "Unesite rec:"
  rec = gets
  puts rec
end

