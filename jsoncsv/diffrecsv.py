import os

# Read in the original and new file
orig = open('201811300347-pattersondental_listings_20181122.csv','r')
new = open('201812140435-pattersondental_listings_20181206.csv','r')
#in new but not in orig
bigb = set(new) - set(orig)
# To see results in console if desired
print(bigb)
# Write to output file
with open('different.csv', 'w') as file_out:
    for line in bigb:
        file_out.write(line)
#close the files
orig.close()
new.close()
file_out.close()

# import difflib
# import sys
#
# fromfile = "201811300347-pattersondental_listings_20181122.csv"
# tofile = "201812140435-pattersondental_listings_20181206.csv"
# fromlines = open(fromfile, 'U').readlines()
# tolines = open(tofile, 'U').readlines()
#
# diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile)
#
# open("diff.html", 'w').writelines(diff)
#
# sys.stdout.writelines(diff)
