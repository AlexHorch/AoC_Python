require 'date'
#[1518-02-05 00:55] wakes up
#[1518-07-08 00:02] falls asleep
#[1518-05-22 23:50] Guard #797 begins shift

input = File.open("input.txt").read

class Entry
    def initialize(text)
        @timestamp = DateTime(text.split(/[\[\]]/)[1])
        @msg = text.split("]")[1]
    end

    attraccessor :timestamp
    attraccessor :msg
end