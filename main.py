import time
import re

starttime = time.time()


def getWordFrequency(string):
    wordList = string.split(' ')

    dictWords = {}
    for word in wordList:
        if word.lower() not in stopwords:
            dictWords[word] = dictWords.get(word, 0) + 1

    stuff = sorted(dictWords.items(), key=lambda word: word[1], reverse=True)
    total = 0

    for k, v in stuff:
        # print(f"{v}: {k}")
        total = v + total
    dictWords["WordCount"] = total
    # print(f"World Count: {dictWords['WordCount']}")
    return (dictWords)


def queryWord(word, n):
    try:
        print(word, ShareHolderWordFrequency[n][word])
    except:
        print(word, 0)


# Do not count these words
stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
             "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into",
             "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the",
             "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were",
             "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to",
             "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have",
             "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can",
             "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself",
             "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by",
             "doing", "it", "how", "further", "was", "here", "than"}
# abc = 'To our shareholders: 1997 LETTER TO SHAREHOLDERS (Reprinted from the 1997 Annual Report) Amazon.com passed many milestones in 1997: by year-end, we had served more than 1.5 million customers, yielding 838% revenue growth to $147.8 million, and extended our market leadership despite aggressive competitive entry. But this is Day 1 for the Internet and, if we execute well, for Amazon.com. Today, online commerce saves customers money and precious time. Tomorrow, through personalization, online commerce will accelerate the very process of discovery. Amazon.com uses the Internet to create real value for its customers and, by doing so, hopes to create an enduring franchise, even in established and large markets. We have a window of opportunity as larger players marshal the resources to pursue the online opportunity and as customers, new to purchasing online, are receptive to forming new relationships. The competitive landscape has continued to evolve at a fast pace. Many large players have moved online with credible offerings and have devoted substantial energy and resources to building awareness, traffic, and sales. Our goal is to move quickly to solidify and extend our current position while we begin to pursue the online commerce opportunities in other areas. We see substantial opportunity in the large markets we are targeting. This strategy is not without risk: it requires serious investment and crisp execution against established franchise leaders. It\xe2\x80\x99s All About the Long Term We believe that a fundamental measure of our success will be the shareholder value we create over the long term. This value will be a direct result of our ability to extend and solidify our current market leadership position. The stronger our market leadership, the more powerful our economic model. Market leadership can translate directly to higher revenue, higher profitability, greater capital velocity, and correspondingly stronger returns on invested capital. Our decisions have consistently reflected this focus. We first measure ourselves in terms of the metrics most indicative of our market leadership: customer and revenue growth, the degree to which our customers continue to purchase from us on a repeat basis, and the strength of our brand. We have invested and will continue to invest aggressively to expand and leverage our customer base, brand, and infrastructure as we move to establish an enduring franchise. Because of our emphasis on the long term, we may make decisions and weigh tradeoffs differently than some companies. Accordingly, we want to share with you our fundamental management and decision-making approach so that you, our shareholders, may confirm that it is consistent with your investment philosophy: \xe2\x80\xa2 We will continue to focus relentlessly on our customers. \xe2\x80\xa2 We will continue to make investment decisions in light of long-term market leadership considerations rather than short-term profitability considerations or short-term Wall Street reactions. \xe2\x80\xa2 We will continue to measure our programs and the effectiveness of our investments analytically, to jettison those that do not provide acceptable returns, and to step up our investment in those that work best. We will continue to learn from both our successes and our failures. \xe2\x80\xa2 We will make bold rather than timid investment decisions where we see a sufficient probability of gaining market leadership advantages. Some of these investments will pay off, others will not, and we will have learned another valuable lesson in either case. \xe2\x80\xa2 When forced to choose between optimizing the appearance of our GAAP accounting and maximizing the present value of future cash flows, we\xe2\x80\x99ll take the cash flows. \xe2\x80\xa2 We will share our strategic thought processes with you when we make bold choices (to the extent competitive pressures allow), so that you may evaluate for yourselves whether we are making rational long-term leadership investments. \xe2\x80\xa2 We will work hard to spend wisely and maintain our lean culture. We understand the importance of continually reinforcing a cost-conscious culture, particularly in a business incurring net losses. \xe2\x80\xa2 We will balance our focus on growth with emphasis on long-term profitability and capital management. At this stage, we choose to prioritize growth because we believe that scale is central to achieving the potential of our business model. \xe2\x80\xa2 We will continue to focus on hiring and retaining versatile and talented employees, and continue to weight their compensation to stock options rather than cash. We know our success will be largely affected by our ability to attract and retain a motivated employee base, each of whom must think like, and therefore must actually be, an owner. We aren\xe2\x80\x99t so bold as to claim that the above is the \xe2\x80\x9cright\xe2\x80\x9d investment philosophy, but it\xe2\x80\x99s ours, and we would be remiss if we weren\xe2\x80\x99t clear in the approach we have taken and will continue to take. With this foundation, we would like to turn to a review of our business focus, our progress in 1997, and our outlook for the future. Obsess Over Customers From the beginning, our focus has been on offering our customers compelling value. We realized that the Web was, and still is, the World Wide Wait. Therefore, we set out to offer customers something they simply could not get any other way, and began serving them with books. We brought them much more selection than was possible in a physical store (our store would now occupy 6 football fields), and presented it in a useful, easy- to-search, and easy-to-browse format in a store open 365 days a year, 24 hours a day. We maintained a dogged focus on improving the shopping experience, and in 1997 substantially enhanced our store. We now offer customers gift certificates, 1-ClickSM shopping, and vastly more reviews, content, browsing options, and recommendation features. We dramatically lowered prices, further increasing customer value. Word of mouth remains the most powerful customer acquisition tool we have, and we are grateful for the trust our customers have placed in us. Repeat purchases and word of mouth have combined to make Amazon.com the market leader in online bookselling. By many measures, Amazon.com came a long way in 1997: \xe2\x80\xa2 Sales grew from $15.7 million in 1996 to $147.8 million \xe2\x80\x93 an 838% increase. \xe2\x80\xa2 Cumulative customer accounts grew from 180,000 to 1,510,000 \xe2\x80\x93 a 738% increase. \xe2\x80\xa2 The percentage of orders from repeat customers grew from over 46% in the fourth quarter of 1996 to over 58% in the same period in 1997. \xe2\x80\xa2 In terms of audience reach, per Media Metrix, our Web site went from a rank of 90th to within the top 20. \xe2\x80\xa2 We established long-term relationships with many important strategic partners, including America Online, Yahoo!, Excite, Netscape, GeoCities, AltaVista, @Home, and Prodigy.  Infrastructure During 1997, we worked hard to expand our business infrastructure to support these greatly increased traffic, sales, and service levels: \xe2\x80\xa2 Amazon.com\xe2\x80\x99s employee base grew from 158 to 614, and we significantly strengthened our management team. \xe2\x80\xa2 Distribution center capacity grew from 50,000 to 285,000 square feet, including a 70% expansion of our Seattle facilities and the launch of our second distribution center in Delaware in November. \xe2\x80\xa2 Inventories rose to over 200,000 titles at year-end, enabling us to improve availability for our customers. \xe2\x80\xa2 Our cash and investment balances at year-end were $125 million, thanks to our initial public offering in May 1997 and our $75 million loan, affording us substantial strategic flexibility. Our Employees The past year\xe2\x80\x99s success is the product of a talented, smart, hard-working group, and I take great pride in being a part of this team. Setting the bar high in our approach to hiring has been, and will continue to be, the single most important element of Amazon.com\xe2\x80\x99s success. It\xe2\x80\x99s not easy to work here (when I interview people I tell them, \xe2\x80\x9cYou can work long, hard, or smart, but at Amazon.com you can\xe2\x80\x99t choose two out of three\xe2\x80\x9d), but we are working to build something important, something that matters to our customers, something that we can all tell our grandchildren about. Such things aren\xe2\x80\x99t meant to be easy. We are incredibly fortunate to have this group of dedicated employees whose sacrifices and passion build Amazon.com. Goals for 1998 We are still in the early stages of learning how to bring new value to our customers through Internet commerce and merchandising. Our goal remains to continue to solidify and extend our brand and customer base. This requires sustained investment in systems and infrastructure to support outstanding customer convenience, selection, and service while we grow. We are planning to add music to our product offering, and over time we believe that other products may be prudent investments. We also believe there are significant opportunities to better serve our customers overseas, such as reducing delivery times and better tailoring the customer experience. To be certain, a big part of the challenge for us will lie not in finding new ways to expand our business, but in prioritizing our investments. We now know vastly more about online commerce than when Amazon.com was founded, but we still have so much to learn. Though we are optimistic, we must remain vigilant and maintain a sense of urgency. The challenges and hurdles we will face to make our long-term vision for Amazon.com a reality are several: aggressive, capable, well-funded competition; considerable growth challenges and execution risk; the risks of product and geographic expansion; and the need for large continuing investments to meet an expanding market opportunity. However, as we\xe2\x80\x99ve long said, online bookselling, and online commerce in general, should prove to be a very large market, and it\xe2\x80\x99s likely that a number of companies will see significant benefit. We feel good about what we\xe2\x80\x99ve done, and even more excited about what we want to do. 1997 was indeed an incredible year. We at Amazon.com are grateful to our customers for their business and trust, to each other for our hard work, and to our shareholders for their support and encouragement. Jeffrey P. Bezos Founder and Chief Executive Officer Amazon.com, Inc.'
# print(abc.translate(string.maketrans("",""), string.punctuation))

# rewrite this so it's gathering file names by looking at contents of directory
ShareHolderLetters = {}
year = [1997, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
        2016, 2017, 2018]
for n in range(len(year)):
    filename = "./ShareHolderLetters/" + str(year[n]) + ".txt"
    shareholderyear = str(year[n])

    with open(filename, "r") as myfile:
        temp = myfile.read().replace('\n', ' ')
        temp = re.sub(r'[^\w\s]', '', temp).lower()

        # print(temp.translate(string.maketrans("",""), string.punctuation))
        ShareHolderLetters[shareholderyear] = temp
    # print(ShareHolderLetters[shareholdertext])

ShareHolderWordFrequency = {}
for n in ShareHolderLetters:
    ShareHolderWordFrequency[n] = getWordFrequency(ShareHolderLetters[n])

phrases = ['customer', 'amazon', 'Amazon.com', 'trust', 'management', 'team', 'innovation', 'shareowners',
           'shareholders', 'Long-term']
for n in ShareHolderWordFrequency:
    print(f"\nYear {n}, with {ShareHolderWordFrequency[n]['WordCount']} words")
    for i in range(len(phrases)):
        queryWord(phrases[i], n)

print(f"Time to process: {time.time() - starttime}")
