#!/usr/bin/env ruby

line = ARGV[0]
matches = line.match(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/)
puts "#{matches[1]},#{matches[2]},#{matches[3]}" if matches
