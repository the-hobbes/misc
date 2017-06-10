#!/usr/bin/ruby

=begin
  Concurrent programming example with Ruby.
  Calling Thread.join blocks the current (main) thread. However not calling join
  results in all spawned threads to be killed when the main thread exits. You
  can spawn persisten child threads in Ruby and not block the main thread by
  accumulating the threads in another container (e.g., an array) and then join
  them one by one after they've been created.

  You can see this is different from the python paradigm, where 
=end

puts 'start the program <=== thread 1'

def sleepyTime()
  sleep 5
  puts 'sleepytime thread here'
end

# basic thread usage
thr = Thread.new { puts 'basic thread here' }
thr.join

# container thread usage to handle multiple threads at once
threads = []
threads << Thread.new { puts "Whats the big deal" }
threads << Thread.new { 3.times { puts "Threads are fun!" } }
threads << Thread.new { sleepyTime }

# After creating a few threads we wait for them all to finish consecutively
threads.each { |thr| thr.join }

# Using a queue to synchronize a fixed pool of reused threads.

strings = ['these', 'are', 'some', 'strings']
q = Queue.new
strings.each { |s| q << s }  # codeblock to fill the queue
threads_1 = []
2.times {
  threads_1 << Thread.new {
    while !q.empty?
      s = q.pop
      sleep(rand(5))
      puts "#{Thread.current.inspect}: #{s}"
    end
  }
}
threads_1.each { |t| t.join }

puts 'end of the program'

