#!/usr/bin/env ruby

args = ARGV.select { |arg| arg.match?(/\A-?\d+\z/) }
           .map(&:to_i)
           .sort

args.each do |num|
  puts num
end
