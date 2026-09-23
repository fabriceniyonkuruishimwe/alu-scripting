#!/usr/bin/env ruby

ARGV[0].scan(/[A-Z]/) { |match| print match }
puts
