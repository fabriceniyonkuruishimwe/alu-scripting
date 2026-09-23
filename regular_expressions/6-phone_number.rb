#!/usr/bin/env ruby

ARGV[0].scan(/\A\d{10}\z/) { |match| print match }
puts
