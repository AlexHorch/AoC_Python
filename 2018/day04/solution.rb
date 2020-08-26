require 'date'
#[1518-02-05 00:55] wakes up
#[1518-07-08 00:02] falls asleep
#[1518-05-22 23:50] Guard #797 begins shift




input = File.open("input.txt").read.split"\n"
f = File.open("output.txt", "w")
input.sort_by! {|line| DateTime.parse(line.split(/[\[\]]/)[1])}.each do |line| f.write line + "\n" end

class Entry
    def initialize(text)
        @timestamp = DateTime.parse(text.split(/[\[\]]/)[1])
        @msg = text.split("] ")[1]
    end

    attr_accessor :timestamp
    attr_accessor :msg
end

class Guard
    def initialize(id)
        @id = id
        @sleepcycle = Array.new(60, 0)
        @shifts = Hash.new
    end

    def start_shift(month, day)    end


    attr_accessor :id
end