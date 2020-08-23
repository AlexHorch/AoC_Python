def cs (id)
    counts = Array.new(26, 0)
    id.chars.map(&:ord).each do |i|
        counts[i-97] += 1
    end
    return counts.include?(2), counts.include?(3)
end

input = File.open("input.txt").read.split"\n"

twos,threes = 0,0
input.each do |line|
    line.delete! "\n"
    x, y = cs line
    if x then twos+=1 end
    if y then threes+=1 end
end

puts twos * threes

input.each_with_index do |line, idx|
    input[idx, input.length - idx].each do |other|
        count = 0
        line.length.times do |i|
            if line[i] == other[i] then count += 1 end
        end
        if count == 1 
            then 
            puts [line, other]
            break
        end
    end
end