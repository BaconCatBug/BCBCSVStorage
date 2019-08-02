require 'open-uri'
require 'csv'

google_sheet_id = "1f8OJIQhpycljDQ8QNDk_va1GJ1u7RVoMaNjFcHH0LKk"
sheet_gid_SB= "344457459"
sheet_gid_CM= "1373487754"
sheet_gid_RL= "1623354916"
sheet_gid_AB= "1933803309" 
sheet_gid_MG= "195881060"

buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid_SB}").read
numCards = CSV.parse(buffer).length - 1 #CSV counts the header row; we only want the number of cards.
File.open("C:\\Users\\BaconCatBug\\Documents\\GitHub\\BCBCSVStorage\\SoulBreaks.csv", 'wb') do |file|
    file << buffer
end

buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid_CM}").read
numCards = CSV.parse(buffer).length - 1 #CSV counts the header row; we only want the number of cards.
File.open("C:\\Users\\BaconCatBug\\Documents\\GitHub\\BCBCSVStorage\\Commands.csv", 'wb') do |file|
    file << buffer

end

buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid_RL}").read
numCards = CSV.parse(buffer).length - 1 #CSV counts the header row; we only want the number of cards.
File.open("C:\\Users\\BaconCatBug\\Documents\\GitHub\\BCBCSVStorage\\Relics.csv", 'wb') do |file|
    file << buffer

end


buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid_AB}").read
numCards = CSV.parse(buffer).length - 1 #CSV counts the header row; we only want the number of cards.
File.open("C:\\Users\\BaconCatBug\\Documents\\GitHub\\BCBCSVStorage\\Abilities.csv", 'wb') do |file|
    file << buffer

end

buffer = open("https://docs.google.com/spreadsheets/d/#{google_sheet_id}/export?format=csv&gid=#{sheet_gid_MG}").read
numCards = CSV.parse(buffer).length - 1 #CSV counts the header row; we only want the number of cards.
File.open("C:\\Users\\BaconCatBug\\Documents\\GitHub\\BCBCSVStorage\\Magicite.csv", 'wb') do |file|
    file << buffer

end

sleep(2)
time = Time.now.utc.strftime("%Y%m%d%H%M%S")
system 'python StripColumns.py'
puts 'add'
system 'git add *.csv'
puts 'commit'

system ('git commit -m Blahxxx')
puts 'push'
system 'git push'
