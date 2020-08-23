require 'set'

input=File.open('input.txt').read
input.gsub!(/\r\n?/, "\n")
f=0
fs = Set[0]
solution = false
first = false
until solution do
    input.each_line do |line|
        f+=line.to_i
        if !solution & fs.include?(f) 
            puts f
            solution = f
        end
        fs.add f
    end
    if first then
        first = false
        puts f
    end
end
puts f