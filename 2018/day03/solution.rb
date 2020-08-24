fabric = []
1000.times do
    sub = []
    1000.times do
        sub<<0
    end
    fabric << sub
end

inputs = File.open("input.txt").read.split"\n"
class Pattern
    def initialize (text)
        values = text.split(/[#,( @ )(: )x]/)
        @id, @a, @b, @x, @y = [1,4,5,7,8].map{|i| values[i].to_i}
    end

    def paint(fabric)
        @x.times do |i|
            @y.times do |j|
                fabric[@a+i][@b+j] += 1
            end
        end
    end

    def overlap?(fabric)
        @x.times do |i|
            @y.times do |j|
                if fabric[@a+i][@b+j] > 1
                    then return true
                end
            end
        end
        puts @id
    end
end

patterns = inputs.map{|p| Pattern.new(p)}
patterns.each do |pattern|
    pattern.paint fabric
end

count = 0

fabric.each do |line|
    line.each do |cell|
        if cell > 1 
            then count += 1 
        end
    end
end
puts count

patterns.each do |pattern|
    pattern.overlap?(fabric)
end