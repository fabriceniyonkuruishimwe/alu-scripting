#!/usr/bin/env ruby

ARGV[0].scan(/\Ah.n\z/) { |match| print match }
puts
