require_relative "wordcount"

class Main < WordCount
  def self.izdvojKvadrate(org)
    result = org.select do |item|
      Math.sqrt(item) % 1 == 0
    end
  end

  puts izdvojKvadrate([1,5,7,49,48,22,9])

  wc = WordCount.new("aaa bbbb aaa cc cc cc")
  wc.count_words()
end