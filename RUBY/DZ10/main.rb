require_relative "modul"
class Main
  extend Modul

  puts self.nzd(10, 5)
  puts self.nzd(4, 4)

  def duzina(str)
    if str.nil? | str.empty?
      "prazan"
    elsif str.length <= 5
      "kratak"
    elsif str.length >= 6 && str.length <= 11
      "srednje dug"
    else
      "dug"
    end
  end

  print "Unesite recenicu:"
  rec = gets.chomp
  bla = new.duzina(rec)
  puts "String #{rec} je #{bla}."
end