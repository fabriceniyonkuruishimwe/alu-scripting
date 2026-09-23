#!/usr/bin/env ruby

ARGV[0].scan(/hbt{2,5}n/) { |match| print match }
puts
