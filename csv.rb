require 'open-uri'
require 'csv'

sleep(2)
time = Time.now.utc.strftime("%Y-%m-%d-%H:%M")
puts 'python'
system 'python FFRK_Soul_Break_etc_Data_Format.py'
system 'python FFRK_Relic_Data_Format.py'
puts 'add'
system 'git add *.csv'
puts 'commit'

system "git commit -m #{time}"
puts 'push'
system 'git push'
