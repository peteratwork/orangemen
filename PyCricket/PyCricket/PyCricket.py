import csv
import lxml.html
import re

url1 = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;template=results;type=batting'
url2 = 'http://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;page=2;template=results;type=batting'
urls = [url1, url2]

with open('Data\TestCricket_PlayerStats.csv','w', newline='') as data:
    out = csv.writer(data)
    out.writerow(['Player', 'Country', 'StartYear', 'EndYear', 'Matches', 'Innings', 'NO', 'Runs','Highest','Average','100s','50s', '0s'])

    for page in urls:
        bmen = []
        country = []
        syear = []
        eyear = []
        match_counts = []
        inns_counts = []
        no_counts = []
        run_counts = []
        highest_scores = []
        avg_scores = []
        hundred_counts = []
        fifty_counts = []
        duck_counts = []

        content = lxml.html.parse(page)
    
        bats = content.xpath('//tr[@class="data1"]/td[1]/a')
        ct = content.xpath('//tr[@class="data1"]/td[1]/*')
        spans = content.xpath('//tr[@class="data1"]/td[2]')
        matches = content.xpath('//tr[@class="data1"]/td[3]')
        inngs = content.xpath('//tr[@class="data1"]/td[4]')
        nos = content.xpath('//tr[@class="data1"]/td[5]')
        runs = content.xpath('//tr[@class="data1"]/td[6]/b')
        highest = content.xpath('//tr[@class="data1"]/td[7]')
        avg = content.xpath('//tr[@class="data1"]/td[8]')
        hundreds = content.xpath('//tr[@class="data1"]/td[9]')
        fifties = content.xpath('//tr[@class="data1"]/td[10]')
        ducks = content.xpath('//tr[@class="data1"]/td[11]')

        batsmen = [bat.text for bat in bats]
        count = [re.sub('[(/) ]', '', c.tail.replace("ICC",'')) for c in ct]
        startyear = [(span.text.split('-')[0]) for span in spans]
        endyear = [(span.text.split('-')[1]) for span in spans]
        mtchs = [m.text for m in matches]
        innings = [i.text for i in inngs]
        no = [n.text for n in nos]
        rn = [r.text for r in runs]
        hghst = [h.text for h in highest]
        average = [a.text for a in avg]
        centuries = [h.text for h in hundreds]
        halfcents = [f.text for f in fifties]
        dks = [d.text for d in ducks]

        bmen.extend(batsmen)
        country.extend(count)
        syear.extend(startyear)
        eyear.extend(endyear)
        match_counts.extend(mtchs)
        inns_counts.extend(innings)
        no_counts.extend(no)
        run_counts.extend(rn)
        highest_scores.extend(hghst)
        avg_scores.extend(average)
        hundred_counts.extend(centuries)
        fifty_counts.extend(halfcents)
        duck_counts.extend(dks)

        zipped = zip(bmen,country,syear, eyear, match_counts, inns_counts, no_counts, run_counts, highest_scores, avg_scores, hundred_counts, fifty_counts, duck_counts)
        for row in zipped:
            out.writerow(row)
        zipped = None
