input=File.open('input.txt').read
input.gsub!(/\r\n?/, "\n")
f=0
fs =[0]
input.each_line do |line|
    f+=line.to_i
    fs << f
end
puts f
fs.each_with_index do |v,i|puts v,i end