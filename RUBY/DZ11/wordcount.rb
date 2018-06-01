class WordCount
  def initialize(stringic)
    @stringic = stringic
  end

  def count_words()
    hesic = Hash.new(1)
    res = @stringic.split
    res.select do |item|
      if hesic.has_key?("#{item}")
        hesic["#{item}"] += 1
      else
        hesic["#{item}"] = 1
      end
    end
    hesic.each do |key, value|
      puts key.to_s + ' : ' + value.to_s
    end
  end
end