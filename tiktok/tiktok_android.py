import time
#import pandas as pd

'''
this is for undetected chrome
'''
import undetected_chromedriver as uc
uc.TARGET_VERSION = 126

options = uc.ChromeOptions()
options.headless = True
#options.use_subprocess=False
options.add_argument('--headless=new')
#options.add_argument('--use_subprocess=False')
#driver = uc.Chrome(executable_path='/data/data/com.termux/files/home/.local/share/undetected_chromedriver/undetected_chromedriver', options=options)
driver = uc.Chrome(options=options)

'''
this is for selenium webdriver
'''
#from selenium import webdriver
#options = webdriver.ChromeOptions()
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headless=new")
#options.add_argument("--display=:1") # localhost:1 -> display ID = 1
#driver = webdriver.Chrome(options=options)

print('driver sucessfully launched')
driver.get('https://tiktok.com')
time.sleep(3)
driver.save_screenshot('tiktok-firstpage-screenshot.png')

channels = ['@vicenews','@wsl']

js_get_titktok_videos = """       
    function get_videos(){
        var video_list = []
        var video_elements = document.querySelectorAll('a[title]');
        //console.log(video_elements)
        if (video_elements){
            v = video_elements;
            v.forEach( (video, index_v) => {
                video_list.push( {
                    title: video.title,
                    url: video.href,
                    source: window.location.pathname.split('/')[1],
                    status: '',
                    views: '',
                    date: '',
                    duration: ''
                })
            })
                
        }else{
            print('No posts found.')
        }
        
        return video_list
    }
    return get_videos();
"""
js_tiktok_scroll_down_command = 'window.scrollBy(0,1000)'
tiktok_videos = []
for cha in channels:
    driver.get(f'https://www.tiktok.com/{cha}')
    time.sleep(5)
    driver.save_screenshot(cha+'-firstpage-screenshot.png')

    print('')
    print('')
    print(f'************* channel: {cha} **************')
    print('')
    print('')
    c = int(1)

    #scrolldown
    while c <= 1 :
        driver.execute_script(js_tiktok_scroll_down_command)
        time.sleep(2)
        c = c + 1
    
    #videos = driver.execute_script(js)
    #time.sleep(1)
    
    videos = driver.execute_script(js_get_titktok_videos)
    print('videos found: ', len(videos))
    for v in videos:
        tiktok_videos.append(v)
        print(v)
        print('------------')
        print('')

    time.sleep(3)
#df = pd.DataFrame(tiktok_videos)
#df.to_csv('tiktok-data.csv')
print('')
print('')
print('----------------- TOTAL DE VIDEOS TIKTOK ',len(tiktok_videos))

driver.quit()
