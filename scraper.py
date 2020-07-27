from bs4 import BeautifulSoup
import urllib3
import certifi

def level1(url, soup, n):
    for i in soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2'):
        if '/dp/' in i.find('a').attrs['href']:
            global c
            if c<n:
                level2(str('https://www.amazon.in' + i.find('a').attrs['href']))
                c+=1 
                  
    return print(" MU>>> Done")

def level2(purl):
    p_http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    p_response = p_http.request('GET', purl)
    p_soup = BeautifulSoup(p_response.data,features="lxml")
    
    f.write('"')
    try:
        f.write(p_soup.find('span', id='productTitle').text.strip().replace('"', "'"))
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')
    
    print('[ =', end=' ')

    f.write('"')
    try:
        f.write(p_soup.find('a', id='bylineInfo').text.strip())
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')

    print('=', end=' ')
    
    f.write('"')
    try:
        f.write(purl)
        #print(purl)
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')

    f.write('"')
    try:
        for div in p_soup.findAll('div', {'id': 'imgTagWrapperId'}):
            f.write(div.find('img')['data-a-dynamic-image'].split('"')[1])
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')
    
    print('=', end=' ')

    f.write('"')
    try:
        f.write(p_soup.find('span', class_='priceBlockStrikePriceString a-text-strike').text.strip())
    except:
        try:
            f.write(p_soup.find('span', id='priceblock_ourprice').text.strip())
        except:
            try:
                f.write(p_soup.find('span', id='priceblock_dealprice').text.strip())
            except:
                print("Item not found", end=' ')
    f.write('"')
    f.write(',')

    print('=', end=' ')

    f.write('"')
    try:
        f.write(p_soup.find('span', id='acrCustomerReviewText').text)
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')
   
    print('=', end=' ')

    f.write('"')
    try:
        for div in p_soup.findAll('a', {'id': 'askATFLink'}):
            f.write(div.find('span', class_='a-size-base').text.strip())
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')

    print('=', end=' ')

    f.write('"')
    try:
        for div in p_soup.findAll('div', {'id': 'productDescription'}):
            f.write(div.find('p').text.strip().replace('"', "'"))
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')
    
    print('=', end=' ')

    f.write('"')
    try:
        for div in p_soup.findAll('div', id='feature-bullets'):
            for i in div.findAll('span', class_='a-list-item'):
                f.write(i.text.strip().replace('"', "'"))
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write(',')
    
    print('=', end=' ')

    f.write('"')
    try:
        for div in p_soup.findAll('div', class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content'):
            for i in div.findAll('span'):
                f.write(i.text.strip().replace('"', "'"))
                
    except:
        print("Item not found", end=' ')
    f.write('"')
    f.write('\n')
    
    print('= ]', end=' ')

    return print(' Product '+str(c+1)+'>>> Done')

c=0


if __name__ == "__main__":

    f=open('output.csv','w')
    f.write('Product_name,by_info,Product_url,Product_img,Product_price,total_review,ans_ask,prod_des,feature,cust_review\n')
    

# URL MUST BE amazon.in 

    url="https://www.amazon.in/s?k=phones&ref=nb_sb_noss"


# CHANGE THE VALUE OF n FOR SCRAPING No. OF PRODUCTS    
    n=2 

    
    while c<n:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, 'html.parser')
        for li in soup.findAll('li', {'class': 'a-last'}):
            next = 'https://www.amazon.in' + str(li.find('a').attrs['href'].strip())
            print(next)
        level1(url, soup, n)
        url = next
        print("url",url)